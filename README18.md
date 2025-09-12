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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da5b15c2-e49a-3965-ab70-00f9c1a04646 | -11.45264 | -43.57635 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fd72942-4a21-36c9-b3d8-0d4df4c15392 | -15.65926 | -47.0437 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c50409da-aae0-3b40-be9f-71162e8745cc | -9.03895 | -47.07281 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 207a5f3f-1e44-3865-99ea-9b69ccad011f | -13.31975 | -44.09216 | 2025-09-12 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ad39f78b-0f3e-340d-b532-5f036802e558 | -9.03097 | -47.11452 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 462f4a5e-147d-32f8-9d62-78b7c6fb5c69 | -9.93839 | -42.33233 | 2025-09-12 03:38:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 541e832f-8ee5-39ed-b734-89eac96e605f | -14.16873 | -46.18546 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb62132d-a2c0-3310-b152-b5e356901f0e | -10.64908 | -48.65806 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28994ab4-b31a-3354-b2db-5663db71deae | -10.43027 | -40.5485 | 2025-09-12 03:38:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6dbe3f3-89b4-38fd-b625-58862c0c1461 | -15.83125 | -42.5968 | 2025-09-12 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 676921c8-f43a-3f71-be76-c09604555943 | -11.64509 | -46.68222 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9169a5f1-6d1d-370c-b22f-b5038c6b2c7a | -14.18398 | -46.19825 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46567916-d5d0-3151-bd56-9dedcd7e2b3f | -11.69984 | -46.53571 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e353866d-7fbe-378d-ac5f-9316b1fa1cbd | -10.84873 | -48.17072 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40886ca0-0b07-3191-95f8-8a4eda19f94a | -15.66697 | -47.03629 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 243145a2-4a30-38f8-a29e-43cb9dd052f6 | -9.03433 | -47.09701 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3db70b50-64e6-3bff-b005-36190923a872 | -12.86105 | -47.95481 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a6e436d-7836-3f1b-bdb1-0a229ee96ffe | -14.17603 | -46.20291 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ace05b83-421b-3117-99d4-8877c89eae89 | -11.12296 | -45.11931 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c6e6325-8db6-3426-a672-93d2a1b38f18 | -11.14617 | -45.31441 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 139b83f7-7243-37ae-a2b5-ce828f5ab08a | -13.35876 | -41.92698 | 2025-09-12 03:38:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 835fd00a-1920-390f-8f15-702c89eb0a26 | -11.69408 | -46.56476 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| db55db58-7888-354e-a0ed-3c518644b3e2 | -15.07633 | -48.0148 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bbaab06-9f97-38ec-b6b5-20b094411501 | -12.09351 | -47.5944 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb01f452-8854-3f04-af0f-c9e08fbc1fe4 | -9.35132 | -46.59571 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 519960cc-374c-3db3-bbe4-d6603bc8dc61 | -11.97506 | -46.65128 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b71d8ce7-756e-3d17-90c6-28e66f8544aa | -14.36971 | -47.28815 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37d7ae9e-e530-38ab-bd97-ecd10a4cf8e0 | -9.04374 | -47.07183 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf535c8d-06cf-3a97-b345-f68d6eec39b6 | -8.48769 | -47.27497 | 2025-09-12 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bf79fd1-3d71-38ee-835e-949da8d3b94e | -13.8951 | -48.23378 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3a174a3-b271-355e-811e-46cbbf5aaf07 | -12.02396 | -43.78982 | 2025-09-12 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60b3d2a1-f616-30eb-bc58-e270dad436c6 | -11.41941 | -43.54062 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc5f5b26-0e1b-315a-842f-139ccfbdb6a9 | -13.31194 | -40.56614 | 2025-09-12 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 55039561-0500-3ab3-b767-272e89b9b59a | -14.12807 | -45.37931 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8939147a-14c7-3af4-b287-f857a2c80c4c | -13.24679 | -43.77401 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c78899ca-2c8b-3e2f-a692-bf67df7ec1a7 | -11.36692 | -43.51208 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f91ab1c7-a869-3362-a641-540708b88e81 | -11.43213 | -48.56698 | 2025-09-12 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 721fcf9a-ff5e-3a18-a7ef-f27014d1d4e1 | -10.13883 | -46.30612 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09ee1ffa-40c8-3219-b9b4-1b1202ee585f | -10.74571 | -48.17956 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cda56ae7-e8a4-335b-9aad-6ba6957c10ef | -11.67003 | -46.62155 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 19632fd0-095b-3522-aafa-0e26d9d61ea0 | -15.11098 | -48.00618 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c18a9add-dab3-3653-9fe6-41cbe05d1868 | -11.19739 | -37.23138 | 2025-09-12 03:38:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2aa0e2b0-29f3-3a72-a73e-f98b2214fc1c | -15.1057 | -48.01431 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ab588850-56cf-3321-ac99-7fb3b9e3acf4 | -11.48523 | -43.62735 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01d6589e-7b65-36db-bc68-f000e6c8451a | -15.08187 | -48.00311 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fefa40f0-646f-33bc-bdbe-63a9ca5a1604 | -11.4672 | -43.61086 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d48d2c44-6b82-357a-9f37-ba4cd8330090 | -15.1046 | -48.01936 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5476ca13-5432-30c7-8908-d9d3ec922f1a | -9.73816 | -45.42768 | 2025-09-12 03:38:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b9a84ac-279d-3eab-9afa-de93186d9aa3 | -15.49198 | -47.34804 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efb5e207-16f6-37dc-8638-6420bf0716d8 | -11.68128 | -46.59714 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eaf3111d-4620-3750-bcf6-c319d6cc46e6 | -11.69504 | -46.55993 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d70e6dde-eb21-32ea-b62f-14d67cf16352 | -10.65764 | -48.65191 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 14c49a66-3db9-3053-939a-22b91b08f0ef | -12.08582 | -47.59904 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2ca3474-52e9-3ec1-97bb-adabc1aa13e1 | -10.87615 | -45.55976 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e7b9b73-5026-3c2c-8820-fd672c7abc08 | -8.64287 | -45.71836 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2a88851-6007-3eb0-9051-cadffdd6e409 | -9.85807 | -43.13031 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d92ad99-b644-313c-b16a-907e4daf7b80 | -11.67526 | -46.62736 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bc7f054-7def-3e10-bb23-b9aaff08d08a | -15.65839 | -47.04782 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dacc96a1-94fa-317b-b940-c33039a271c6 | -14.15086 | -44.45337 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7c93c2-6782-3d8b-a097-cd3ac884107b | -15.52989 | -41.433 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 575968c1-6152-307f-b823-77b9a74b1370 | -14.1335 | -45.38051 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02b74be6-e017-3583-bb8f-e4161af0c710 | -9.68345 | -47.54997 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0d4f255-f67d-3ca0-8943-84e807e24263 | -11.66323 | -46.65564 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00d6684a-cfdf-3683-86fe-ab905c3ad6e0 | -14.18647 | -46.21038 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a03c3e1b-e2d9-31e3-8f90-42fe65ce0807 | -15.80646 | -41.64135 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d79fb475-b751-336e-9b4b-d095cf2c5a08 | -13.3089 | -42.38745 | 2025-09-12 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a0a66597-7367-3508-b476-fa491f8aa841 | -12.99337 | -46.74222 | 2025-09-12 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c829bd0c-d9aa-3958-b273-7d2f6b463d87 | -14.18069 | -46.21411 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71d3d20e-4218-3f34-881f-ae0bbe144d4a | -11.65128 | -46.68333 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb2b4697-d20e-3886-a12b-d2ef66612af9 | -14.16168 | -46.19066 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 830009a4-e812-3964-9eda-616303ab6e86 | -9.71882 | -48.30961 | 2025-09-12 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f286d0d7-91eb-3a59-8808-f4329ab190eb | -11.68791 | -46.56377 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72534304-898f-3a7b-a097-2d15eecde294 | -15.83209 | -42.5923 | 2025-09-12 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0c7cab09-31c0-35cd-88b8-16a24dca9f01 | -9.8473 | -43.54662 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 769b9f80-408a-3b08-b36c-a41eaa60522a | -9.72289 | -43.51641 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9399efa5-cb5f-3b50-9b8e-4b79f5247422 | -10.13375 | -47.9211 | 2025-09-12 03:38:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ac3657ca-098a-3927-9dc3-b5dcaa57575b | -14.16797 | -46.18908 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffe729e1-d2ad-3d15-b112-e1ef2f09e9f7 | -15.2451 | -44.04468 | 2025-09-12 03:38:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e982de7-5bb0-3fff-866a-47f4cec6bb26 | -11.65649 | -46.68939 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b41797a5-ca35-3c86-9247-c69ff2d41df3 | -14.56977 | -41.01028 | 2025-09-12 03:38:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fb4528f-5ce4-368f-b661-5796f19c4dc5 | -14.18798 | -46.20776 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| daff52da-8f9c-3746-b79a-0dde0694379a | -12.83236 | -47.96191 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 875b77b9-5494-3480-8268-19ca95412c71 | -11.14273 | -45.24091 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b8075c7-cdd7-332e-9b1e-e326cf94333f | -14.45372 | -47.31242 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba14e6e7-9c41-3068-9700-a63373e6f057 | -9.03211 | -47.10858 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1627e68-a8df-3262-803d-4894c0e9e49c | -9.08718 | -46.95527 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58ed9f79-345d-3e2c-9c3f-3c976e2cd928 | -9.04277 | -47.05287 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78752399-908d-3473-804b-c31349332258 | -14.11597 | -44.31934 | 2025-09-12 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3efb3d2-b1fd-3b60-a82d-7c94c378d60b | -11.68956 | -46.52357 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b31dfeba-02aa-30d5-a067-bb37845f0511 | -9.45858 | -47.64891 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 499b6d42-f06e-32c6-8517-c00749e36c56 | -11.66841 | -46.6618 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ccb3dbe-ae7b-3b83-b991-80488875ebf2 | -12.8058 | -44.75468 | 2025-09-12 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bafdd39-973d-3522-821b-f22a2c679660 | -11.37765 | -43.51091 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dd4bfba-2731-30a0-943c-2e057a6806a5 | -9.03577 | -47.07749 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aeaa5e64-d77f-303e-94f4-48734d0b96cd | -9.02195 | -46.11885 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1e0be0f-3794-3b31-8875-53c0811261f4 | -12.09472 | -47.58857 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 76c66d4b-63f3-3351-b0d8-9aac056d09a2 | -15.71902 | -42.19498 | 2025-09-12 03:38:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7795e53b-c267-3f7f-915e-83e248eb16be | -9.68606 | -47.55148 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cf9e1af-c728-35eb-affb-bb36848e91ae | -14.17047 | -46.20087 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b227145-0fd0-394f-894d-233e42869787 | -13.31879 | -44.65245 | 2025-09-12 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
