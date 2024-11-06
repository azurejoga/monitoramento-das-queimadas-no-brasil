# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3093d158-ed60-3163-802c-40f9266b069b | -6.4827 | -47.4827 | 2024-11-06 00:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 558bd2f2-a29a-35db-8198-99a97dec6231 | -3.0207 | -53.4227 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 59d1098d-45f2-32cf-ad5d-8b9da42ad73a | -3.2053 | -53.2356 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 57d2a4c5-2b47-344d-a1ef-4d3c0d65c9cf | -2.7243 | -54.1552 | 2024-11-06 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 2e89c7e9-34cb-3c8e-b30c-b5da6a7b2aba | -6.5094 | -44.6847 | 2024-11-06 00:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 893a63d6-e6db-30ab-badf-9da548a4455a | -2.7244 | -54.1351 | 2024-11-06 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| edb5db1a-97bd-3529-b094-c91e55d2da4f | -3.1213 | -51.1036 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a07bdb37-7343-3f4c-87e9-92a4089d640c | -6.1226 | -43.9809 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 190.3 |
| f714a127-c7b0-3459-91cd-06d08870ba15 | -1.2922 | -54.5784 | 2024-11-06 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 0b5b980b-2047-3b39-a502-f254d448f352 | -6.4825 | -47.5046 | 2024-11-06 00:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 01bda742-f1f6-35dc-945a-2909dccfa701 | -2.1746 | -53.6834 | 2024-11-06 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 587c6aae-fdc1-306a-8d8b-be24c34503d8 | -3.0212 | -53.281 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cd38e0ee-b40a-3517-87c4-0aef2e6c4db3 | -2.7639 | -53.2265 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 567b5117-3632-3ec6-91a2-8229f61adea7 | -6.1229 | -43.9578 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| dda7c28f-6b0e-3d2e-97cd-2224de6c9a8d | -0.8539 | -52.8501 | 2024-11-06 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| ec782a50-baf6-38d6-81d2-a0a628a51231 | -3.0213 | -53.2607 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| cbf26813-c5f6-3fd7-9e7d-b5f3b9e6deb7 | 3.61296 | -51.34357 | 2024-11-06 00:20:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fae88ec0-927d-35cb-833a-0a20622d6219 | 3.61934 | -51.30238 | 2024-11-06 00:20:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1d344f6c-052f-3436-ac8a-d9dc228d75c8 | 3.61961 | -51.30947 | 2024-11-06 00:20:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f5155603-bcab-3e00-94c5-b7c13ed4f281 | -2.07377 | -47.06203 | 2024-11-06 00:20:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3ecd31d1-5a6b-3e97-9947-351b2730a42a | -2.09813 | -46.47799 | 2024-11-06 00:20:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f955bf6d-119a-3253-be1b-63893f53ecdf | -2.8607 | -51.7937 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 61c44901-0034-3279-b965-347faad303bc | -3.2348 | -50.3904 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b4bdd4ba-0de4-33c3-8637-2c841c526ae4 | -2.2691 | -46.4614 | 2024-11-06 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 59ef1225-4694-3c74-86ba-c4e37550e0d0 | -6.1039 | -43.9824 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 79ee5363-bb89-3603-912e-71768a533e4a | -2.1746 | -53.7036 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ae101ad9-573d-3381-b292-9da1426c8ff7 | -6.1229 | -43.9578 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 098013c3-bff8-3029-89da-cd1d3a5b7f5e | -5.6748 | -45.9456 | 2024-11-06 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a22fd22e-3e72-3af1-86be-9fa66ebb3743 | -3.0023 | -53.4434 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 463a6dd5-5509-322a-9fef-790028680a70 | -2.8423 | -51.7942 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 39995eda-4948-3d48-99b4-1a67e9863758 | -2.1563 | -53.6838 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d2f7297e-52f0-37b2-89a9-e3b40d949962 | 3.6184 | -51.3162 | 2024-11-06 00:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7c9e90b1-1815-3f91-80e9-88ef9074cda7 | -3.7255 | -41.6748 | 2024-11-06 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 3f6f72ca-491c-3872-b5a5-8c9538ff2a93 | -2.764 | -53.2062 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 43ec0cc3-574a-3ead-9dd8-16c55601d958 | -5.5445 | -43.7012 | 2024-11-06 00:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 05e4e84a-88df-3fd1-b123-61f87ba89bd9 | -6.5014 | -47.4813 | 2024-11-06 00:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 355.1 |
| d8f5bb4d-015a-3721-813b-110a48a22f39 | -6.1414 | -43.9794 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 1e72921d-2e2d-3630-872d-e4e53570bd4f | -3.2349 | -50.3695 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a0c85bdd-f585-3933-a6f8-5a0cb960eb33 | -5.6561 | -45.9468 | 2024-11-06 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 28b7704b-7caa-3c7c-962a-8f0deaf645e4 | -3.7564 | -45.9422 | 2024-11-06 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f597ed02-2c89-34cf-8990-e5ecea5aa097 | -6.5012 | -47.5033 | 2024-11-06 00:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 634e1297-9b70-3180-acdb-ea43e03db8e5 | -6.1041 | -43.9593 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| cf441545-37c3-388d-8790-fa1c96438155 | -0.8539 | -52.8298 | 2024-11-06 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 1acd9059-669e-3d96-adec-323a80908b6f | -2.7243 | -54.1552 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 39cfc153-bc96-3818-9a22-a704547ecb07 | -6.5094 | -44.6847 | 2024-11-06 00:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 8c99cabf-8ae2-399f-889a-4667e49113cf | -2.6764 | -51.8189 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7af92a6a-80ff-3377-a241-a8d44f58d57c | -3.1213 | -51.1036 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 73ce92c1-6357-3292-8ce0-478bd4638636 | -6.5096 | -44.6618 | 2024-11-06 00:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8445212e-b3b5-385b-8a37-c6ecfd70b519 | -3.0396 | -53.2805 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 26fcc5db-0f50-3f6a-b169-1788b35ca1b2 | -2.3999 | -46.1699 | 2024-11-06 00:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2236e11f-3fed-30e8-9e20-0807ee74b72a | -3.2053 | -53.2356 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d7f29c65-3479-3e60-b7c4-e7eb9bf2f2f7 | -3.1617 | -50.2038 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d8d8a58b-4f3f-33c4-ae30-b748fd347b8a | -2.2505 | -46.484 | 2024-11-06 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c635bd8b-b4df-32e2-9b40-0c9976b8d9df | -3.0607 | -52.5066 | 2024-11-06 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 91fb4b0c-dc17-326d-a721-39811cbdc97e | -2.8608 | -51.7731 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 487.6 |
| d6d75698-0de0-38ea-9c24-f72902051752 | -23.9306 | -54.0564 | 2024-11-06 00:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| e6ded03c-d231-3cb3-87ea-3ed8b7b9643c | -3.7068 | -41.6758 | 2024-11-06 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| eab999c9-e63f-35ca-8989-9d1d3221aad4 | -4.5616 | -47.9925 | 2024-11-06 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3bd6ed08-3389-3373-89d9-b488ea8c601b | -3.0213 | -53.2607 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 24f8028d-5b59-317d-9cbc-72240deaef73 | -2.8661 | -45.6201 | 2024-11-06 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 8b509701-94cc-38d6-bba1-eb79f402da82 | -3.2164 | -50.3701 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| e0596770-373d-3f76-8840-6880fe0dda0d | -6.1416 | -43.9563 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fa870afe-c1de-3196-915f-6b9376bc1b41 | -3.7066 | -41.6997 | 2024-11-06 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 6949a4da-d293-3997-ad52-88d34aec06ff | -3.9669 | -48.1716 | 2024-11-06 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4ac25f9c-3d7a-3f43-a499-a54319836b36 | -3.0397 | -53.2603 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| cfb98f49-4c9c-3699-b1d2-f29e739904c3 | -2.8065 | -51.4855 | 2024-11-06 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 8e2e0f18-b79c-3b8a-b4cd-efdd61e5d6b8 | -3.2415 | -53.3967 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2c498466-926e-382c-a3db-99af88b3d32a | -0.8539 | -52.8501 | 2024-11-06 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5aa29f3d-c9c5-319a-b9c7-3b2b0a0dcb1f | -5.675 | -45.9232 | 2024-11-06 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 174b6275-db92-399f-87c2-445ebebc9320 | -3.2163 | -50.391 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| f714ae48-4256-3b60-9c98-7efdca9f7f35 | -3.2231 | -53.3972 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 11144aab-e04f-3f36-82c2-cdbb99c1eadb | -3.0207 | -53.4227 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4f897dda-5a9a-34ac-b5c1-20d5e35426d6 | -0.8355 | -52.8299 | 2024-11-06 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c6546d38-64dd-35c2-a8cf-c91373413db3 | -6.5016 | -47.4594 | 2024-11-06 00:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 526897ae-531d-3c21-ab31-d366375a98cc | -4.1246 | -43.5833 | 2024-11-06 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 955bc420-d42d-3904-b239-18edf4a85843 | -2.8423 | -51.7735 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 208.2 |
| de669676-9986-3227-9273-20d4b87ccf33 | -3.0212 | -53.281 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 90921135-ec5a-3b43-9a5f-8dd34789490c | -6.4827 | -47.4827 | 2024-11-06 00:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| dab8ec9b-0a8b-3ece-bf43-ef7363c4e8ca | -6.4825 | -47.5046 | 2024-11-06 00:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| c1a0914b-d918-3ede-8b9a-7311afe48098 | -3.0207 | -53.443 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a016ba7d-21d2-3f22-8849-ac93d50b2e32 | -2.8608 | -51.7524 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c04f4e74-5374-3f50-b4d6-68f679741a44 | -23.93 | -54.0787 | 2024-11-06 00:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 295296ae-9311-3139-bc20-70ed0fd7b62e | -6.4909 | -44.6633 | 2024-11-06 00:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5cb62589-9ab2-3f12-bf5b-3a5d9e913852 | -4.5614 | -48.0141 | 2024-11-06 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 829f287a-a9c4-33a2-8686-1ea3ac043990 | -3.2054 | -53.2153 | 2024-11-06 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 92980260-f45f-305e-ad9d-ce6290d5d1de | -2.1746 | -53.6834 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 6b96e4bb-439e-332e-bf2e-044c13d459a9 | -3.7254 | -41.6987 | 2024-11-06 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 0fade317-8639-359a-b6b0-cccebc1dd6c4 | -0.8355 | -52.8503 | 2024-11-06 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e3a26a53-2eab-3c8d-92f9-4534558c065f | -2.6131 | -54.5381 | 2024-11-06 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| ebb0df59-e764-3e42-9bd8-6a829560dcfe | -0.8723 | -52.8297 | 2024-11-06 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7ddc905f-64a5-38b8-bab9-a1713d6e6d6a | -6.1226 | -43.9809 | 2024-11-06 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 08cd2bb4-d99b-3637-9fe8-e9f2ebcb8036 | -6.4906 | -44.6862 | 2024-11-06 00:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 8334bba8-c0e4-3efe-8367-8566cd09b97d | -2.7244 | -54.1351 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c2d75bb1-7dac-3b6d-bab5-add98e84ff08 | -2.6764 | -51.8395 | 2024-11-06 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0bd2334e-1508-3302-a23f-fd52a0becf05 | -2.658 | -51.8194 | 2024-11-06 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| c519f491-5562-3ba5-8fba-fd2d7b75bb3c | -3.967 | -48.15 | 2024-11-06 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f3a41327-5792-3ac9-9c0a-6804c61f43c7 | -4.1432 | -43.5822 | 2024-11-06 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8d45d965-bbf9-33ea-a3cf-747aa27f2c3e | -5.6563 | -45.9244 | 2024-11-06 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8543357e-087c-30cb-83ad-24d74102fee1 | -5.5632 | -43.6998 | 2024-11-06 00:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 2270ad9b-4b92-3be3-9962-22d31bbf4511 | -2.1563 | -53.6636 | 2024-11-06 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |


[Clique aqui para ver as próximas entradas](README6.md)
