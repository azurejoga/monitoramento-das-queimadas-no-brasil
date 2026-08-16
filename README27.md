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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5338cc32-b8f7-3403-bfcc-90e65eb7a73e | -14.39239 | -51.91814 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f4a5512-9ff1-34aa-b773-57a75295f2b5 | -12.70814 | -48.46868 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32e9047b-d832-32ac-829a-fd430635a3ce | -14.52263 | -53.28916 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60304dd2-bca0-3f37-99bf-9065219cc482 | -11.58289 | -54.69149 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afc98a08-7a67-3375-a192-bd53efb7fdf1 | -17.19784 | -54.22324 | 2026-08-16 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e71c92-36e1-34fc-aadc-daa7c4836a4c | -13.81344 | -53.78116 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdf1f5fd-6bc2-3d63-93b1-5455c729b278 | -14.33388 | -49.17381 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 273ef98c-387a-3aa8-af33-19970152e6b4 | -14.89983 | -46.64525 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb738ecc-4681-303f-82a9-a153640c1c1b | -13.82273 | -49.39008 | 2026-08-16 04:42:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d3b7cd0-ecef-33fe-a432-4c93ea12aa38 | -14.47918 | -45.69065 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0916ba9-50a5-3025-ae55-4d5bbebb10f6 | -14.30888 | -51.952 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b957d08-1a6b-3535-9657-fa2ca4e4de18 | -14.4183 | -51.94809 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0fb09ed-119e-3c86-af30-0ce9b9861e33 | -17.17065 | -53.40958 | 2026-08-16 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e7e70e-bc7e-3a4e-b997-d55a466ce3ac | -14.30403 | -53.05839 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b65d73d2-0c99-3bf8-b353-d44a34fef0d7 | -14.48512 | -54.02456 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee25cdb7-32b5-3764-a63d-fc87170abaa3 | -14.49108 | -52.00399 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e03d40b8-2614-3533-8063-c10e06c4ec90 | -12.67309 | -48.45597 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ac65566-96bd-3b03-9674-b3ce2e786da8 | -13.80818 | -53.81318 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aaf1e43-d972-35d9-9b58-f54c83e23d31 | -14.71743 | -52.88771 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03e75422-631d-3f87-8683-fb0815ba1470 | -13.8062 | -53.82524 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d451ca0-0db2-323b-b768-211156f035e6 | -15.16472 | -50.07375 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c1991d8-44c7-3504-83fa-35b5db604feb | -12.69061 | -48.44143 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88aef85c-81f2-3dcf-8fbb-385bf8aa15eb | -14.49001 | -45.68354 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ec075f4-e350-3dc3-925f-aeb780736b32 | -14.90506 | -46.63622 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b6b34747-a630-3d71-ba57-d730c6ef7001 | -14.37316 | -53.10907 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 630b35e1-95c6-3387-835b-cfd1b0548b13 | -15.16526 | -50.0701 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f67b39f-3f3f-38a2-b8fc-0585b39e7c46 | -15.05332 | -47.01769 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d3e4159-e16c-3fc6-9111-eca97885bc86 | -13.79504 | -53.82742 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0112a7f7-f7a6-3c28-8359-52392f08a0fc | -14.91043 | -46.6261 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05e85715-f657-3a0f-97c0-c7c6423086c4 | -15.06598 | -47.02145 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422a2c1c-2fa2-356c-a26c-ac36091fa500 | -15.10103 | -48.73712 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2e6ed41-c5a8-3e4b-8443-d1b0d19d0672 | -14.07182 | -53.71785 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 298c3f88-b3ec-3bfe-bc89-a464cbb079f0 | -13.53946 | -46.24695 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7dbbde85-8a10-3f38-8509-d7a8eee19aa3 | -13.65016 | -46.24436 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd9496e3-f2ee-3849-b9d8-94fbacb53873 | -12.68532 | -48.46986 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49e5c355-3f19-3a76-aaf6-edc716f5ebe6 | -15.14286 | -50.04784 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da0a353b-fd4b-3856-8f78-4d622efe3344 | -14.3257 | -53.31102 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cbe2e27-5781-3492-8d58-3c0cff431e3d | -12.69003 | -48.44554 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4556cc67-783c-3601-b7f7-1288d150238b | -12.73957 | -48.42471 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 042d9515-2aea-3050-aa6e-507158a0d122 | -15.04949 | -47.01683 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b458253-59f4-31ef-a3c8-c3b6c6064247 | -11.98055 | -53.45023 | 2026-08-16 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c2180e1-f7e4-3ec7-bbd3-30003dc29c69 | -15.15589 | -50.0761 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ef1c857-3d7f-3c7a-ae7e-08b7e068b57d | -12.71861 | -48.4704 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24971f1f-76f3-37f3-8dd1-1d4660b38267 | -15.54152 | -47.38804 | 2026-08-16 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a112f82-fa59-3a96-a321-812a876caddf | -14.41863 | -51.83832 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97e348eb-69f8-3941-a522-966280af414e | -14.37863 | -51.89754 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4185cca-ad00-3011-8cd5-60702e7677d2 | -14.08413 | -58.74321 | 2026-08-16 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09bc04b8-cd76-3a76-b70d-194cb72389af | -12.69305 | -48.47414 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 774d124a-cfff-32b5-8bc1-3295057407df | -15.23108 | -57.65429 | 2026-08-16 04:42:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d954e18b-b618-33ca-83d2-49dfa67cef38 | -12.69248 | -48.47807 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d391f3e-6f35-32e6-9296-356bf483bda2 | -15.79238 | -55.57769 | 2026-08-16 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dd5cf1a-1b1d-3e14-9cea-a31568177fe8 | -15.04539 | -47.02789 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3516f376-0406-33df-b804-8701d59c7358 | -18.61568 | -47.49572 | 2026-08-16 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60517730-d478-365b-8afb-cf9807f219ef | -13.79817 | -53.78654 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f686dd31-a215-35cf-bf37-e8b3481f20f3 | -13.81454 | -53.78063 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf088d35-9f23-3ec9-ac8c-ea121fd1f490 | -12.68124 | -48.44923 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ad4a2c1-2984-3a2a-9037-d570b1f1cba3 | -12.6872 | -48.46512 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b38132c-f2ff-3bb6-989a-b8ea95eed50c | -14.42307 | -51.83174 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5815678-57fd-3cc0-9e8a-9fe1fdf8a7bf | -14.32634 | -53.30721 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d59685bc-efda-3a5e-8091-e7f8002b159e | -12.68899 | -48.4775 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d918a054-ddb0-3531-afc7-75cfc73ffeed | -13.80295 | -53.77936 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad424892-ea77-3c10-8782-399560d48f13 | -13.91375 | -53.94588 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7800a1e2-0d11-3292-8477-81e1c9cd8ae1 | -14.47698 | -45.68567 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 441fbfde-37ba-39b5-abf5-0e469590e5eb | -12.68591 | -48.46591 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a972afa-8ccf-321f-bcf7-c316b3f0af97 | -13.54983 | -46.24916 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b16d7dce-c591-3868-b5f1-e2f4983efc36 | -14.40192 | -51.87945 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04d8f649-5560-3313-ad90-4419520e8ed7 | -14.32907 | -53.09739 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c30b372-3797-3470-9b4f-e47633d5d270 | -15.06925 | -47.02658 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0239fb6c-8731-39d5-881a-5c3188dc9935 | -14.38195 | -51.89809 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced3b381-8c8f-380b-8923-480730f63182 | -14.07464 | -53.72239 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 218ac969-132c-38d5-bc60-74a5572e8e01 | -16.18279 | -55.95459 | 2026-08-16 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8e19b982-e2d0-3ab4-b31f-96b4eab9b6d6 | -13.79551 | -53.80267 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e3e145c-f5a4-3875-8f5b-2c276230b46f | -15.10752 | -48.74229 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d493689b-f86e-32a6-8dbe-04b8e52ea62d | -14.13265 | -53.69598 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21a5e0b7-5c8e-3daa-897c-6228a76c4a9b | -12.67715 | -48.45266 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8720081f-b520-3946-8401-e63a3467ebd2 | -14.38639 | -51.89151 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfc23fd0-e143-3ca5-84a2-8e875287afde | -14.48165 | -45.68235 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7289519c-470d-3480-9bc3-04a0d9827743 | -13.83803 | -57.77105 | 2026-08-16 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ad7e605-4591-3bf6-ad21-251adf01197a | -14.30002 | -53.06157 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95781eb5-1241-39df-b752-d315d6d30456 | -15.06861 | -47.03133 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1d046bd-c457-3286-bcd1-1bc69de5022c | -15.06103 | -47.01908 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf2598e5-ac2c-3f00-ac07-a75e74d1ce5f | -14.0753 | -53.71844 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dbaebf8-8b1c-3ddd-8ce2-508179219e8f | -15.05054 | -47.01882 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab97a582-5730-3210-be42-1726221fc985 | -14.89835 | -46.63378 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba6c6a20-de19-3747-be0f-671412b5eb5a | -18.57628 | -47.15601 | 2026-08-16 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5dd2dde-d278-3e7e-b209-05858e0e8528 | -14.9011 | -46.63575 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e00fa96-7b66-33bd-8931-f6c2cbbc5939 | -18.42721 | -48.57193 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf0f1c20-ee3e-339d-8906-31bbc2c170c8 | -13.44328 | -57.04052 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3197a2f-932d-354a-8ed6-1b570ff88de7 | -13.48992 | -48.23259 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a769b8-4e83-3098-a731-a58288d7cd0a | -12.67486 | -48.44396 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c82f984a-efe4-3116-9fb7-e059363f0442 | -14.44377 | -53.2992 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4bdffa2-7c94-3693-94c0-e3f51abfcf1b | -11.58665 | -54.69209 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0530f83f-c343-3c89-a3ba-35a0ca3f6226 | -12.71918 | -48.46648 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8797da87-e7c0-30a5-8177-edd15d1dab9f | -14.78253 | -56.95167 | 2026-08-16 04:42:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e6cdb3d-f98a-34ac-b234-017a6c34067f | -14.49052 | -45.67961 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40b29de6-1c4b-303e-b84e-c7c360fdcded | -15.32349 | -53.9047 | 2026-08-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36bfbe91-3ed1-3308-ab55-15958d920248 | -12.69946 | -48.47924 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8132ddf7-b0cb-3410-9728-c299cd5d5758 | -14.90575 | -46.63098 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b03cef9-b4ad-3629-ae43-48681f40335c | -13.79902 | -53.80326 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f34aeeb8-de2b-3a52-996c-883d9eb14fdc | -13.49348 | -48.23314 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
