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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0657fd0b-95d4-3ee9-a353-017f75256f96 | -3.84804 | -50.31297 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71fb981b-d8ae-38c1-92d9-9f4dc3d81f3d | -3.10274 | -53.70572 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0a21313-fcfe-3dbc-acd5-83da2c7259ad | 2.26523 | -50.81865 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 987685df-fa05-3182-bfd6-f219f649768d | -3.10144 | -53.71431 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9daf0c0-9daf-34a3-8306-fea0a6edf452 | -3.83698 | -50.31039 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efbda2b3-0fba-3a06-96b6-74942d383afb | -3.5825 | -54.31014 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91a1f6d5-7555-3421-befd-d0e3aeb65c1f | -3.04094 | -54.25449 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04c8e4dc-16cf-3049-9ff2-701e9494ed37 | -3.08049 | -54.25162 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1f35d383-8db4-3a65-b5e3-fd236d9847c5 | -3.84517 | -50.3218 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60a5009-a091-3df9-94c7-c912717d471f | -3.23149 | -53.87328 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9413685e-2bb8-3e8f-a6db-fa9d6b589f0a | -3.06791 | -54.16079 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04bde72a-3afa-3449-bf15-c78ea6b9351a | -3.71336 | -51.14361 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c0ecff4-53cf-36f2-ad3a-d2502f08a342 | -3.04027 | -54.26095 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a941e3f6-dcde-313b-a4f8-578a57bfb615 | -3.09826 | -54.16127 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f7e8da3-ab52-38b0-bc53-f9bcf14bbaaf | -2.98677 | -54.12547 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 505cafba-b7b1-38f8-b548-fcb16078a1a8 | -4.15686 | -53.91716 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39d0470d-f4a6-31c2-9de5-40065ce4ffa1 | -2.94074 | -54.14464 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b71a326e-2d8a-3dbb-aa4c-6170740152a2 | -2.95535 | -54.07779 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3211e4d9-f04a-3608-865b-992b0a46cd6e | -3.06115 | -54.14761 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 471e8d36-ccee-3091-b03a-a575a02102bb | -3.38038 | -58.2022 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed3d14cf-00cd-37d7-8c96-1e0ff1872d6c | 1.78625 | -55.56392 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abfc2b51-5aa2-3c09-a84b-ec8b2d78a515 | -4.35875 | -47.77782 | 2026-10-06 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8051b528-f22c-3a80-9775-23ad054c0e3f | 0.44271 | -60.53366 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4339a6a9-6488-39e7-bedc-56d2e5da1847 | -2.86321 | -54.1408 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f693a2cc-5576-36a6-9900-ca63dc1a5ee2 | -3.38022 | -59.43283 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b3f167a-9c92-3a51-8132-adb60e087c65 | -2.86803 | -54.13754 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41b2c669-fb1e-38f3-bc5e-bdebcf3283f4 | -3.02099 | -53.89466 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| bcc93d2a-9a56-371f-a866-284121680a5d | 1.98233 | -60.61431 | 2026-10-06 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9d4d9d9-43bd-3e42-91b8-de3a1b89d46a | -2.53651 | -58.03001 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7b9668-936e-3ca3-b09a-b8c5e1c6f2ed | -2.94812 | -54.15197 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9446626a-912a-39fd-b089-225272731d0c | -3.11377 | -53.7509 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d005fb7-adb8-35b1-a629-9ec0f1a27b9b | -6.75979 | -55.47345 | 2026-10-06 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 681b40aa-0684-3e3b-a39e-ba47db50716c | -2.78094 | -57.6738 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70972ed4-19d4-3b1b-b0ad-3e28051cffa2 | -3.07264 | -54.2463 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0474bd36-779c-346a-a680-6717e39fe1c7 | -3.67399 | -54.54121 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0336baa7-ba57-370b-be43-3fbc4fe0b1a1 | -2.6366 | -57.72202 | 2026-10-06 05:23:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bd64668-2acc-3c85-bf37-21120415e89f | -3.50547 | -51.67588 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d23078d-4d36-36ed-9505-342d2f278a3a | -2.13556 | -56.7027 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1a6421f-001d-300f-b90a-3caf5d949d06 | -3.12169 | -53.76301 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63864d18-039b-3929-b24b-7abc360e8b72 | -8.65804 | -66.49574 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdce8b17-5392-36d5-87ed-24452998ecff | -2.88134 | -54.13557 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3c50176-bf01-37b0-9a0e-4e93c9b2e002 | -3.07333 | -54.15347 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b90ab216-89ca-348e-be61-3bbc5374c406 | 1.72471 | -55.62803 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a7930b2-cd0a-3db7-85af-e74c3b6d2b7d | -2.87112 | -54.14593 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 06efac4c-22c4-3f88-a08a-385e285a0455 | -3.1223 | -53.75879 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1b2bab-27bc-3fbb-98e1-ffb794b1fe0b | -3.22402 | -54.30442 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a39f2e6-ff0a-378d-8553-a676f00bee67 | -3.9967 | -56.25642 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78fd2071-d5aa-3842-850e-e512074087be | -3.08253 | -54.17944 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 521b0214-94f3-3050-9f84-a328eef7348b | -7.44604 | -63.55885 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af45475b-adda-3065-9938-8522922beaf3 | -8.5437 | -66.97897 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a6b509a-26c4-37c7-b53b-aa6fecb43935 | -3.58669 | -53.47194 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6ff34c8-5fef-3aa5-9ca9-c5e0da3a591a | -7.52452 | -70.39194 | 2026-10-06 05:23:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b422f1b-6490-395b-b906-3f92d84e1062 | -1.88522 | -56.25164 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2af503fd-01fa-357f-a19a-82ead8fab38a | -3.38379 | -58.20272 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ab594264-cc22-30d4-92be-8282d7276015 | -3.47099 | -50.1036 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 673e75c6-4b98-3665-9f81-fd1b5f8b8616 | -3.32494 | -53.85133 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd07af5-f9ff-3b97-9677-554d21fe1ae9 | -8.51741 | -67.00672 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68087bcb-54fd-32d4-bd35-fe312fd3a8a2 | -2.79499 | -54.13479 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a2159a-7eb9-36b2-a4d7-0ba8ce73a1b3 | 1.72536 | -55.6253 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45bb94ca-c407-3360-8db1-3a42303fc3b2 | -2.98605 | -54.10096 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef150c89-312c-3887-ae58-bf7cfed1124f | -3.08492 | -54.16327 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e52df00d-d199-318b-9208-64c256472251 | 0.44381 | -60.54076 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 86fb7514-081d-3f58-b4c4-5a6fba963aca | 3.05797 | -60.60179 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95b35d87-136e-36ca-b12f-8d497ba19f4e | -2.95179 | -54.15656 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e663d25e-4082-3a05-b794-e5d875cf9687 | -3.07817 | -54.15013 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8c272ae-4424-36ac-b1d2-331cce6680e3 | -3.06308 | -54.16418 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2af295d2-3267-3739-809a-eaebb32dee88 | -3.7128 | -51.1427 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7433870-19a8-37e6-88f7-e4e255a997cd | -2.32603 | -57.98382 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c09389a-e77c-3cb3-89a6-ccb14e8a5d5c | -3.47153 | -50.09983 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83de514d-787c-3015-b071-5225d290a336 | -3.49322 | -54.61588 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95c210c9-97d8-3c67-a49f-c3c1c659f98b | -3.06168 | -54.23269 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae91c0a7-bba2-34ea-b4f2-c38a1ba436a9 | -2.55874 | -54.73374 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97183c20-3771-3ce8-a770-0878634d0c8f | -3.84749 | -50.31666 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a64da8df-5863-3cec-9ca0-13d8dcfc356a | -3.04478 | -54.23009 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da2be5e2-197d-3c17-ba3b-add95cea3379 | -3.07889 | -54.17474 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dbf0ea6-24ce-31c7-833f-e5f20b129bb8 | -3.88364 | -55.80321 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9dd154b-b4ba-3593-91f8-374967104df1 | -2.94805 | -54.06845 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb86395-c259-3e2e-9a07-4c343ce31885 | -3.09449 | -53.73063 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6e4a1621-e363-3d55-9f3a-4b0315291f35 | -2.94656 | -58.01216 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e0e0acf-dcaa-3347-aa12-a9dcf88c7cfc | -3.14039 | -53.72686 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e23d26ce-9978-3585-b350-0c66310fae87 | -2.87227 | -54.13819 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a41c35c0-43a5-38b7-87c3-90fd7f2567ef | -3.05293 | -54.23273 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe279e8b-b7a6-3f1e-b3b4-f8c79208c072 | -2.78555 | -57.66674 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8f38f3d5-865f-3879-852b-68c5001707b1 | 0.31942 | -60.44079 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0159a34e-9fcf-3b55-a404-ccec43c4bd7c | -2.78337 | -51.6725 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5662770-9978-3747-9beb-8d51d05ef7d0 | -3.05964 | -54.16111 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a189067-ddb3-3f01-91b3-c7d9582af745 | -3.51108 | -54.63792 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f292c01-ae59-3f06-830d-554b8007b726 | -3.50824 | -59.50613 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11773b14-360f-3ed8-8dc4-b8da7f2fd013 | -2.32205 | -57.98699 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e8b151b-5345-3c44-bf63-72f59851deb7 | -2.90553 | -54.11907 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab27f8a0-18ae-3c9d-83d7-4db35a30d24f | -3.05717 | -54.20523 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0c0922a-4bca-36b7-9c6a-5662f710e029 | -3.32781 | -53.8539 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c30d51b3-584a-3e2d-a0fd-aa33651b46bd | -2.07171 | -56.83964 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2b58702-883e-38cc-9759-7ebde2a961a0 | -3.09706 | -53.71365 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2ed240e-561b-334a-b92a-9355cadf93f6 | -3.05234 | -54.20851 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 346482f5-95a1-3712-b4d9-cc1fe4c8e43c | -3.33804 | -59.48645 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 551bc95c-9ff0-31c5-a5a0-2c4c1c689d82 | -3.22966 | -53.88578 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3416a8b3-0e57-3d7f-8c1f-e8d93c632653 | -4.11315 | -52.07157 | 2026-10-06 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01b45dc-d749-3935-92eb-185ceb7d256b | -2.9559 | -54.159 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdad262d-73cc-3027-b620-1bb736a840c9 | -2.77736 | -54.10774 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README62.md)
