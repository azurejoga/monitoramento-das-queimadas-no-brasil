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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab7e4b81-cbd3-3270-9d7e-ca2646e97bd6 | -3.59648 | -55.46025 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c050eeea-3163-3120-975d-340d829c5d3b | -3.59364 | -55.45606 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1697d9bd-36ec-3bb9-af71-0f20cefc61fe | -3.59306 | -55.45974 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5070dc9d-9f75-38d0-845e-c9891f7415f9 | -3.59073 | -55.56519 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebafcdf6-82d7-36cc-b93a-35ff8c336156 | -3.59042 | -55.56548 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d11b3e-8447-3472-9513-0cd38254b992 | -3.58816 | -55.55758 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9100d52-7fac-30ca-bc0a-33c366b70d2d | -3.58758 | -55.56128 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc8827c9-9864-3412-8504-74b973d1dbb6 | -3.587 | -55.56495 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbdf7a1a-41db-37ea-900a-96d777d7ac4b | -3.54415 | -55.45968 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3dd8935-e901-3304-9278-60c40bd9c3a3 | -3.54356 | -55.46337 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e316b098-c590-37de-bf12-1585933cd6fe | -3.52709 | -55.45703 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2fad056-9ec8-300d-a09c-ed90387691d1 | -3.5158 | -55.44023 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87c9aeef-d8d1-33fd-84c7-bead3dcaf7a7 | -3.51239 | -55.43969 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e9e395a-380a-348d-af36-dbdb601882ef | -3.5118 | -55.44337 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b936a416-a9e3-3225-a543-b25c59924af4 | -3.51121 | -55.44705 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 210da381-95cf-35b1-8f0e-de6c2c5d7b03 | -3.5038 | -55.44964 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd4b5c7a-3bf8-3179-ac4d-cdb3dc7d7d34 | -2.7748 | -56.50901 | 2024-10-12 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d38b1f4-9b98-3709-82ba-9a60f42bbe70 | -5.00775 | -56.17443 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5614fa-f2a7-3f10-a206-19235d8f9d73 | -4.99192 | -56.20701 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f6376e8-758a-329b-bdcc-c42626a1218b | -4.97991 | -56.19321 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dabbef9-e201-3534-83bb-3803f7088431 | -4.97645 | -56.19267 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b114e003-90ac-3f70-ba11-4f3c50ce3fbc | -4.94454 | -56.01706 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 927073f5-fd93-3ed6-8ea7-c8c612e6bb25 | -4.90273 | -55.90671 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509f632c-5033-3735-8ced-114caa7720d2 | -4.8999 | -55.90241 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3a3415f-0027-374c-a420-768b64039237 | -4.89931 | -55.90612 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fbd3447-3fc7-3333-94b0-f66a70b09179 | -4.89648 | -55.90183 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f7dd4ea-d99b-3074-8268-2b43f92f24c9 | -4.89589 | -55.90554 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f17eda7c-6b76-3f8d-a3b6-ece4d9c5f7ed | -4.89468 | -55.91307 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4f757a-b02a-37f1-b4a2-2c6d169b1e2f | -4.89408 | -55.91685 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5f708e-3e57-3c1f-9c15-8f9ae82d404b | -4.89246 | -55.90503 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29941ecd-15cb-3faf-8efb-7c72ed633e1e | -4.87484 | -56.16971 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43a80773-2299-3661-94e4-4509b9d90885 | -4.86649 | -56.00099 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d48befa-817c-32f2-a4ec-52bc605d692b | -4.8659 | -56.00467 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685e8a56-52e4-37a7-9e57-994437c3c8a9 | -4.86531 | -56.00831 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2c75ef-6578-3d0b-b7de-eab6fa025270 | -4.86246 | -56.00409 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9f5bb08-12b2-3c4c-9b22-db7c0309eed4 | -4.86188 | -56.00771 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c92dd9e-ffe2-3fce-9dce-635b8bed50f0 | -4.85569 | -56.17841 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb3cba22-2ab5-34a5-9db9-19cd7ebb9100 | -4.85507 | -56.18225 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67f46fd0-a6ae-3a01-8b53-e4fd5466a13c | -4.85223 | -56.17786 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cf6fcc9-5561-348d-a237-76aeee0a2dbe | -4.85161 | -56.18169 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06883792-b6e8-380b-a88d-9d4e81702996 | -4.85099 | -56.18553 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80f1bd48-10a4-3788-874c-68a915734a2d | -4.82702 | -56.15793 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a36e22d6-0287-3c6b-94ff-649e81638585 | -4.82356 | -56.15737 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be1911b5-bda3-3c93-8c18-ce781a2842c6 | -4.80972 | -56.15512 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 59db515f-7893-3b65-8151-79964720b253 | -4.80911 | -56.15888 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 51b9696f-5039-35fc-87b7-8afbddf76d73 | -4.78891 | -55.89312 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 452a444d-d8f7-36d0-8f46-9745cd79e13b | -4.77627 | -56.19392 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac7adc95-6a50-3b57-8188-0e6c6192c011 | -4.77089 | -55.85214 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e795bc-be32-3800-8322-20ed18d7217f | -4.73608 | -55.73973 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cb10dd0-a3ff-3b03-be8b-6657a4a193f2 | -4.73218 | -55.72023 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5de1cb54-3682-3a19-96f6-fd25d25fd72d | -4.72344 | -56.03686 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90c2bd52-4c5f-3611-a446-ed3311a8056d | -4.64607 | -56.01707 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3803ea51-3409-3a52-bfc6-82cbfe083c95 | -4.60817 | -56.12012 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6444af8-56e3-3e52-a1fe-c369e94638ca | -4.60755 | -56.12397 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 42a29c00-cf4d-3ded-a49d-4d79b8efb354 | -4.60408 | -56.12343 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 118449fd-38ac-3128-9da1-7f75b7dbaec5 | -4.56416 | -55.73937 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0df392e-94eb-3b3d-b2af-0d375795dae6 | -4.53402 | -56.12453 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd99fc85-5c3d-3af3-ae89-3a2eddd83a26 | -4.53054 | -56.12407 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8caedc-afdb-3080-bd2a-20178b29fcf5 | -4.51486 | -55.82769 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb7a1d61-7c98-3e4c-bc30-1e388f96fbca | -4.43583 | -56.30397 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0325252-1d7f-3a22-8adc-4ff34470f361 | -4.3353 | -55.74199 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5432f0a3-c513-344e-99fb-4b5a1127d5bf | -4.3347 | -55.74571 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a24694bf-df93-3fb8-9818-c856d11b4083 | -4.33127 | -55.74519 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f79844e-be77-39d1-b7ec-f7a94321d4fa | -4.27349 | -55.55811 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae16d7d-69c6-3690-80ef-5e4023f5049e | -4.23807 | -55.53421 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535b63bc-3967-3eae-9bdf-c537b0dcb841 | -4.01663 | -56.1792 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f750169-8b68-32b7-82f1-72f223d60ef4 | -5.27507 | -56.03788 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98e82a6a-0738-3dbe-b07b-7a047574a702 | -5.25497 | -55.96611 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af8d1fc6-1345-3d60-ae24-ad82d0b6d8c0 | -5.25438 | -55.96983 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 948646d9-d37f-34e6-b505-d48e99de4192 | -5.2098 | -56.0509 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c31a9cbf-74c8-350b-a53d-c195f55907bf | -5.20921 | -56.05458 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfcf0ce-0e49-367d-9c0e-c6c372bd7ab2 | -5.20578 | -56.054 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79f4858b-6174-3698-9bdd-c6a8318c60ad | -5.17986 | -55.99619 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| faa5768c-5bcc-360d-9a3b-fac664d76a83 | -5.17925 | -55.99996 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80f6e5fc-5b01-3317-b115-a545a3600487 | -5.13292 | -56.26445 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d388af-e5e0-38e4-9a8e-07c969745bb1 | -5.12277 | -56.23938 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbacf358-a771-3dee-9c92-dc122a0ad8fa | -5.12253 | -56.11508 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6217e58-f0e4-32d9-a28f-4ca72e505dbb | -5.12215 | -56.24319 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3431413-64d4-344e-9aa3-32a57dac11f7 | -5.11868 | -56.24265 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a8fd1a-9a65-3b7d-9485-ff96d361b60e | -5.10174 | -56.20128 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed962197-1138-388d-8262-e69aa1623285 | -5.09889 | -56.19692 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0439df8-1a42-36fb-b5c2-3ecb093d1513 | -5.09828 | -56.20073 | 2024-10-12 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 747873ad-df6b-3c24-83ea-0ff78e941d80 | -2.07525 | -56.66494 | 2024-10-12 04:57:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d788e6-298f-3759-9d45-dab549ea776e | -3.16834 | -57.9464 | 2024-10-12 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 419dc993-4b96-3773-b292-ed8ec8f936dc | -3.16446 | -57.94578 | 2024-10-12 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d09a5c05-332c-3d89-8bda-07b793069f95 | -2.98773 | -57.0844 | 2024-10-12 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a1f1da-0fe3-38fa-ac95-ef56f2ab0730 | -2.62291 | -57.5736 | 2024-10-12 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dfc3707-86e5-3512-bc50-358a373e665a | -2.62228 | -57.57117 | 2024-10-12 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21971c79-2521-3e58-9a10-ce817af40c8a | -2.61674 | -57.56295 | 2024-10-12 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fbede3b-32fa-3e2e-a52c-3f587514793e | -2.41253 | -57.16119 | 2024-10-12 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6994f5e2-4124-344c-8021-eac99641453a | -2.40583 | -57.88307 | 2024-10-12 04:57:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d6f00ff-1130-3ee5-92dc-9e84d24144cf | -2.3963 | -57.6466 | 2024-10-12 04:57:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4991a44f-a8b0-3e96-b09e-8a6a041b6adc | -2.39462 | -57.64407 | 2024-10-12 04:57:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31f0a7f9-d2f8-3bf7-81cd-a3b37b5ba7ec | -3.64635 | -58.2527 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39735da8-52db-3017-855a-9a702d54724f | -3.89232 | -57.95574 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb139c05-0897-305a-a359-d2ce7068c524 | -6.47512 | -58.43767 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 614e597e-2fd4-3a2c-9db9-b644fbb2c273 | -6.47131 | -58.43702 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d36fbbf-4c2f-3da4-b564-889e4c4a4ff1 | -6.35414 | -58.18051 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e47df095-d65b-3a31-9917-c9c1c3ecb9c9 | -6.35338 | -58.18507 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ee77d3-70aa-3d3e-91a0-433057021185 | -6.35114 | -58.17531 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README63.md)
