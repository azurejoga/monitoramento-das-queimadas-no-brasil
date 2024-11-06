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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2738960-8948-35e4-8dff-00a17ad55386 | -3.0207 | -53.4227 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| fc4dac1b-a7f6-3cfc-a50a-8e25620f8d00 | -2.3999 | -46.1699 | 2024-11-06 01:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1a5766bb-7f88-3dae-bce0-7eec78eb5bb7 | -3.5446 | -51.3187 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0e88a849-8aa8-3cfb-8bbd-889c5ad45f0c | -6.1226 | -43.9809 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 78be4301-3494-360f-822e-7f17f98637c0 | -2.7243 | -54.1552 | 2024-11-06 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| aa052401-8118-38b7-b035-880efb53099c | -3.2415 | -53.3967 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 740939e5-e839-370c-b00d-bcfacae62e73 | -2.7244 | -54.1351 | 2024-11-06 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| acf5335d-72a6-3179-a674-78ebeeb8c74e | -6.5094 | -44.6847 | 2024-11-06 01:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 2ab9fa61-a47a-3034-9040-c02fb205b281 | -2.8506 | -49.4744 | 2024-11-06 01:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 600145a1-4ab8-3a13-9591-44a7d9c104ab | -4.1244 | -43.6064 | 2024-11-06 01:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 88fcbbb2-6944-3fb7-b33a-aeb0584d7945 | -6.5096 | -44.6618 | 2024-11-06 01:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cbbf3603-c071-3c95-b945-9c999025c037 | -5.5632 | -43.6998 | 2024-11-06 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 62e2928e-be82-3b0a-a768-3cc9ac2a4133 | -3.0023 | -53.4232 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d11502f6-92d9-3a44-be08-2d1adbc6da1e | -2.028 | -53.5852 | 2024-11-06 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| e4b848fd-e03f-3101-a660-ade6048f4bc2 | -3.5262 | -51.3193 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ec5c21f7-d7fc-3d6a-978d-ae871207f6f0 | -2.8608 | -51.7731 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 217.9 |
| 18312a5b-702b-3744-85b9-482a0482271d | -2.9187 | -51.0262 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1e6bd3b4-1ebb-3af0-821b-bba67002309f | -3.1617 | -50.2038 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 22a2199d-2dcc-3573-b3dc-48fd977254a9 | -2.8065 | -51.4855 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b16aef7c-f3ae-32e1-baa8-2573b51bb106 | -6.521 | -35.2488 | 2024-11-06 01:10:00 | GOES-16 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| 38134acc-a025-3def-9cab-8c362d5bede7 | -4.5614 | -48.0141 | 2024-11-06 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| ac34c466-8ed6-35ea-9afb-01bceed4cca4 | -0.8539 | -52.8298 | 2024-11-06 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2f269ee5-3819-39bf-bad0-a9af3c20a7f1 | -2.8661 | -45.6201 | 2024-11-06 01:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 30931e4c-9bb1-385d-8445-996ab291f001 | -4.5616 | -47.9925 | 2024-11-06 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fe8f48ed-85f0-3bb1-bf0f-c5c419193515 | -6.5014 | -47.4813 | 2024-11-06 01:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 9ebebcce-d2fe-362e-80e2-9637cd2dbe3c | -2.8424 | -51.7529 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b258efeb-f3e0-34a9-a20d-e29552c02d19 | -2.6764 | -51.8189 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c63dc841-4092-3c32-8e0b-163775613d80 | -3.2231 | -53.3972 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 6c877f9e-6461-3700-b7dd-91c97aa45f6e | -2.9185 | -51.0678 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 32e89152-8a8f-351c-a4d4-de8c3da41f83 | -3.0023 | -53.4434 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ac5f4c0b-1ba2-3984-9c6c-4b185262c62f | -6.1229 | -43.9578 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 6c277674-a905-30cb-8037-39c4076c71c3 | -2.6764 | -51.8395 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 5798d486-7f81-3d76-a247-376dacfb87b7 | -2.9186 | -51.047 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| f9401144-dc6d-37e2-8d08-dc4796ee8145 | -8.1936 | -43.787 | 2024-11-06 01:10:00 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 649f7f12-10a0-35c2-ba34-f2408260ea09 | -2.1746 | -53.6834 | 2024-11-06 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 68e36ce6-43f7-3752-bba9-76ad8f0b21eb | -3.1394 | -51.1861 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 75a1cfc2-fd4c-3b6e-9be9-36ce1f8d8140 | -2.9371 | -51.0465 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ebe0ec2b-d9dd-369b-8c72-aa51c6187be8 | -3.1759 | -51.2681 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| ea09e322-4ef4-34b2-bcfd-35c86a4f7e49 | -6.4825 | -47.5046 | 2024-11-06 01:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 84f96f50-21ba-3b72-898e-eb14c1d2224d | -4.1247 | -43.5601 | 2024-11-06 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 962feed3-f5a1-34f9-9a47-6c6c9ad9ac5b | -5.5445 | -43.7012 | 2024-11-06 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4c0dab9b-76e5-3b6a-a645-a129525533ce | -2.082 | -47.0602 | 2024-11-06 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 83ef617a-637f-3aaf-b8bd-8a8a5bae0650 | -6.1041 | -43.9593 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e1d5ac7e-7b95-3af4-9b15-379b5cc32cdb | -2.8423 | -51.7735 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 69d38b49-70c2-36f2-a231-b8dbf94dae57 | -3.9669 | -48.1716 | 2024-11-06 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c953d2d2-f944-33c4-a699-6f78c3e3e386 | -4.1432 | -43.5822 | 2024-11-06 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| cf2b8645-b9ff-3a95-b5a2-abddd7ebab6d | -5.6563 | -45.9244 | 2024-11-06 01:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7291b95a-53d0-36af-a307-ebd56dde8be3 | -3.0212 | -53.281 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 82c76174-58f7-3c9c-a52d-36fe38cac13a | -2.8064 | -51.5061 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0da52667-8b6f-3a3c-a690-7a014f8a643c | -2.706 | -54.1556 | 2024-11-06 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9be08bd0-9ba8-3eb8-9911-333c5fac7ceb | -3.1212 | -51.1244 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 6b10643c-44ce-3886-b86f-790fe0c1cbd2 | -6.1039 | -43.9824 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 173191ff-46c8-31eb-bbb5-d55c6d78077d | -4.2165 | -53.5686 | 2024-11-06 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c5961099-3598-3d40-852a-d9138336e042 | -6.4827 | -47.4827 | 2024-11-06 01:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| fd7d8b45-6c3e-3671-b265-e8fc3076f217 | -3.967 | -48.15 | 2024-11-06 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9ed8f13c-52d7-39dd-8e35-19ce4f4c8be8 | -6.4906 | -44.6862 | 2024-11-06 01:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 30312d1c-7865-3951-8a4e-b9d84c31c189 | -3.0207 | -53.443 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 1e3ddec3-28cf-3be4-8198-a819b5dc8ab4 | -6.1416 | -43.9563 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f9c3480d-2482-34db-a48f-b26243b72f83 | -2.2505 | -46.484 | 2024-11-06 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 6a8abdb6-c9c7-3b03-a7e8-edcce30c7cdf | -3.1393 | -51.2069 | 2024-11-06 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3adac2d1-266c-33f5-acda-edb9f0201d82 | -2.8607 | -51.7937 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 8598043c-0e7d-3e0a-a9a5-08eafd892503 | -3.9961 | -43.2418 | 2024-11-06 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 45eb5a98-58d0-3c86-9b8d-6bbdd9399353 | -2.8423 | -51.7942 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6bd2ec78-fdfa-34e2-8b1f-91bedd2cc0dc | -6.1414 | -43.9794 | 2024-11-06 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| de5399dc-660c-309b-b5d2-e3f3d258983f | -3.0213 | -53.2607 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4b1f848b-fd25-31a5-b894-dd43ad6c3e22 | 3.6184 | -51.3162 | 2024-11-06 01:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e1ee34d0-56e1-3c66-96ab-b140c249fb15 | -2.6131 | -54.5381 | 2024-11-06 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6d41e683-283e-35fa-8d69-c5f58b9756d8 | -3.0397 | -53.2603 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| e086d9cf-cdb1-3de8-8443-7fcf9a8f1fcc | -3.7254 | -41.6987 | 2024-11-06 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| bfa36142-f3bd-316b-aaa3-7d871b5845f4 | -2.937 | -51.0673 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0f1ede3c-2871-32c3-8c46-f572aaa5999a | -4.1246 | -43.5833 | 2024-11-06 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 305.4 |
| 8dd5c499-3531-3e72-bb23-eec3c1f50be3 | -3.2415 | -53.3967 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4d034f2a-4eb0-3671-b933-c8514248cc97 | -2.9186 | -51.047 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 114b7cc3-8f35-36a2-8d09-837f35181826 | -2.9187 | -51.0262 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 3a582f2a-846e-361e-a677-6d7f0010038a | -4.1246 | -43.5833 | 2024-11-06 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 233c331f-e742-317a-8115-da67552adfac | -3.1213 | -51.1036 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 652a9831-ebcb-30d5-859d-939e8dfc7fb8 | -2.937 | -51.0673 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| df97c807-f46d-3f69-9748-96a6b9712325 | -2.6764 | -51.8189 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| aac7915d-805d-3d29-a9d2-33626c55f31a | -6.1229 | -43.9578 | 2024-11-06 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 2ca7d976-6149-330d-8f6f-fcfdfa2bd5a4 | -3.1393 | -51.2069 | 2024-11-06 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6d145986-6087-397c-ba76-095cf7e84bf4 | -6.5096 | -44.6618 | 2024-11-06 01:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2dec522c-5a5e-3be6-9f69-5691e162fe9f | -2.082 | -47.0383 | 2024-11-06 01:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3ded553e-9f6b-38c9-9901-5eec485a0c5f | -6.5014 | -47.4813 | 2024-11-06 01:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 6bfbfe70-36bf-3eb6-9e78-1646f4bcef99 | -3.0207 | -53.4227 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f8ee0377-67c5-369f-95bf-a372bd3d5ad1 | -4.5614 | -48.0141 | 2024-11-06 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 51af8f49-644b-378e-9b6c-bb6cded229c7 | -2.082 | -47.0602 | 2024-11-06 01:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| bf49cd96-bcf9-373c-95ad-2ff11a4fab38 | -2.1563 | -53.6838 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 2e5ced8c-44c7-34fa-91eb-e66f4cb1a197 | -3.3285 | -50.0723 | 2024-11-06 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 18c3c241-a4db-3a6d-a90b-ef124fafcfd4 | -6.5094 | -44.6847 | 2024-11-06 01:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| c19c87f0-d27a-38eb-ad8c-0c0fa218019c | -4.1432 | -43.5822 | 2024-11-06 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| abc0dc13-aac2-32fd-ad7e-724e95ee2a37 | -3.2053 | -53.2356 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ab479e30-f9f4-3db2-933b-9c7477e729cf | -2.8661 | -45.6201 | 2024-11-06 01:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ef05fdf8-a838-3946-ae76-514488e93200 | -6.1039 | -43.9824 | 2024-11-06 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 46188e57-2857-3f19-bbf2-6ff6e1014283 | -3.1617 | -50.2038 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b31b55cc-d217-3542-872d-7c27044213c9 | -2.9185 | -51.0678 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 4df1963c-0841-392f-9b09-6ea49836d87c | -3.1577 | -51.2064 | 2024-11-06 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8eea689f-f0ce-3b6a-9163-5223070ab411 | -3.0023 | -53.4232 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| defcb702-54c6-346a-af21-8d5a3c8cf0fc | -6.4906 | -44.6862 | 2024-11-06 01:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| be21b98d-c902-3c64-a0cd-e96a62350233 | -6.1414 | -43.9794 | 2024-11-06 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dd897eff-9cca-3241-8592-8d63afb11f31 | -4.5616 | -47.9925 | 2024-11-06 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |


[Clique aqui para ver as próximas entradas](README14.md)
