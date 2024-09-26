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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42c9286-d777-3f91-b960-bc484c2cbb42 | -9.80166 | -53.55822 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e53e4e2f-9b37-332b-aa65-4645b60ae682 | -9.80051 | -53.54328 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19add8d8-eabc-31e8-8be7-48adf10266aa | -9.79996 | -53.54689 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21ce6336-5eea-3432-b44a-d4d7dfb5e7d0 | -9.7994 | -53.5505 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a075cb6-6882-3cbe-9493-871903667cf6 | -9.79715 | -53.54277 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48407a7b-b348-352f-8545-92a87bb77de4 | -9.78206 | -53.55148 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eac1df1-71a3-3524-b9a8-2a486378eff2 | -9.77871 | -53.55095 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5da245a2-d593-35ba-9218-96e1834ef751 | -9.77755 | -53.53598 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41c2e592-914d-32c9-ad4d-4773ddc2cd8f | -9.7759 | -53.54681 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70c8d762-485d-3484-9d19-bcb3cd27a9f9 | -9.77535 | -53.55042 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c305ba8-8c7b-3401-b7bb-9ef835450c32 | -9.77364 | -53.53905 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d3f114a-268a-3233-b83f-f09f5c038646 | -9.7731 | -53.54266 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7c0e16-531d-3a8d-863f-840346e4c75f | -9.77255 | -53.54626 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80c86a55-249f-3c7b-bf0f-01a7aa624474 | -9.6913 | -53.50076 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 852e12d7-27e0-3df0-bb2a-be0949bfaa2f | -9.68793 | -53.50024 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 149b5a34-43af-38ba-bf81-2a5b1dbc4d8c | -9.68738 | -53.50386 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2691a294-007a-38c3-acb6-fcb7ca098667 | -9.679 | -53.51367 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 308d959c-1e09-3543-8197-457d93e19e56 | -9.67845 | -53.51727 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e0d6797-8331-3b45-ae19-e0eb40649fbf | -9.6751 | -53.51675 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f61ffd-4b41-3a27-a17a-89c539d1ab29 | -9.67455 | -53.52036 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76360cc4-d8df-3a0c-b0c7-57f987a363b4 | -9.67174 | -53.51622 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ec31bb8-9bf2-38a7-8d76-67799d8eacaa | -9.67119 | -53.51982 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c795ad-4a49-3e6d-8fc9-fa2063d28599 | -9.67064 | -53.52343 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f7f8d1-893b-3cd7-a4a4-5163c23f9d74 | -9.67009 | -53.52705 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 323d5bb8-5c66-3eaf-bd3a-9c2869e3c751 | -9.66838 | -53.51569 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8146488-835c-3980-a683-0044ce171af6 | -9.66783 | -53.51929 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53eed432-01d5-3b73-a550-36146befb94a | -9.66673 | -53.52651 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 867046ff-6591-36ac-97cb-fa45eb0679c3 | -3.39509 | -53.71995 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95b771d1-4ee9-325e-825c-905c8adcd2a9 | -3.39179 | -53.71944 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9680ad9-b82b-3bdc-bab6-acb3797bd8fa | -3.32716 | -53.69525 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4732ff2e-899e-3fcb-bc3b-d3fd39642b90 | -3.52062 | -52.82798 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| add367f2-de9a-39d3-8fb6-9de42b2fd1cc | -3.4447 | -52.72754 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2ac4ab1-6c23-34e9-9335-868aed795bab | -3.4145 | -53.20308 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f2d172d-fe45-3c5b-ab76-5d4d31b1dad6 | -3.41132 | -52.87405 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff5c85c-edc8-3c39-86d6-e95307cd61f5 | -3.3266 | -53.2203 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 288175ab-c5e5-3d04-838d-addb745a32db | -3.3249 | -53.20957 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 442ef7e7-5180-3aa1-8f6d-262d47619b7c | -3.32437 | -53.213 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97534bae-1e5e-33e5-b9d6-ad8ba3369c18 | -3.32383 | -53.21643 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8c5c88d2-dd14-3247-a232-4bc4cae1ee26 | -3.3233 | -53.21979 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 207a34fd-e306-3a5f-a505-242846dc609f | -3.32161 | -53.20906 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5a6fc38-ba99-3fea-8e1d-df9f0ad259fa | -3.32107 | -53.21249 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc60707b-b966-3cf5-b7e3-70e180a92b60 | -3.32053 | -53.21592 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 59b1d4b8-6f9e-3dd3-84d3-6a9a97b5bdea | -3.30213 | -52.98778 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 421f2280-2cee-3b17-8835-0e48016a8af8 | -3.29883 | -52.98726 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ab84c9-f560-3fe5-9cd2-feee521ec671 | -3.25771 | -53.31503 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93434a90-970c-37dc-a7b7-7d0fb22eace5 | -3.25717 | -53.31846 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015b90d1-8e5b-3a19-aff6-c06d686e1959 | -3.25663 | -53.32189 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13629398-eba7-3c98-96cb-e0be205abbbd | -3.25441 | -53.31452 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f360de-fd3f-3e7a-bd19-98d1329e52e8 | -3.25387 | -53.31795 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e9c6673-f304-33e3-9777-333fe5dfe8e4 | -3.24433 | -52.26657 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f15c2bd-42b5-3019-ab1a-e75268560f04 | -3.01977 | -52.35407 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfdcf7f5-0883-3ff9-ab96-660dbef0fd55 | -3.01496 | -52.18755 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c495e30b-dd58-3826-b4ff-015c62b2674c | -3.01217 | -52.18349 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cd44462-ce2e-3189-8045-88cf8d7ba820 | -3.01162 | -52.18703 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b72fa493-cda2-3528-9fb5-0a9387d7e9a8 | -2.9528 | -53.04571 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dca8b565-b95b-308d-9288-1d4c3c71cff6 | -2.86243 | -53.31601 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88732cf0-1113-3e4d-88d9-0e5b40315ef7 | -2.85967 | -53.31208 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b3e2f49-2567-3b68-b0ea-245f42506a28 | -2.85913 | -53.3155 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 102f25d4-d2d4-332a-8ce5-8557ff47b7a0 | -2.85584 | -53.31499 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0796fede-1590-3001-ad7e-a760eff5c1a5 | -4.20435 | -53.85114 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14b3d5df-32cb-3c83-9653-6146716e12be | -4.20051 | -53.85406 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd8b950d-d14a-3329-84a5-0235697cbf5c | -3.88762 | -52.3299 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee5d978-00ec-37a8-b7b6-be610fa18fcd | -3.88427 | -52.32938 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfed285c-60cc-3a83-a5ac-8a3b270f188a | -3.7852 | -52.28829 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82d32e8c-9120-3e80-bde1-d528625a6e06 | -3.7824 | -52.28425 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13a76c53-fc9b-3a25-9def-80e76ee87584 | -3.74971 | -52.3625 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8947fd9-989f-32f2-8c15-1c421af7d1a6 | -3.74916 | -52.36604 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58167bfb-134f-360d-a068-148f42355ee0 | -3.74844 | -52.30433 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c870d278-474d-383e-b314-5a5807697e71 | -5.9346 | -53.73453 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c37def1-21a7-32f0-bf7a-aec46aaa715e | -5.93406 | -53.73798 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 115b572f-8f8b-3c4d-bee4-f94866194566 | -5.92255 | -53.74678 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32f2a3ee-0469-3557-abea-dc48666d3941 | -5.92201 | -53.75023 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca7b761-66af-3a79-a48f-bd5434cce19f | -5.91925 | -53.74628 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5f85d3-c922-38ab-a3f5-4358fc3702ee | -5.91548 | -53.77038 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e788d235-71f3-3c14-b4f5-a7c89c7cee24 | -5.73364 | -53.69189 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 888223ff-0956-315d-9dc1-d20177b55b7b | -5.73034 | -53.69138 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76088de-201d-33b4-bd13-0a3058fd2558 | -5.7298 | -53.69482 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc8ad6d2-fb32-3492-ac88-6cc72a21571e | -5.72704 | -53.69086 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ba51af-c85e-3b95-acae-77e43e43efaa | -5.7265 | -53.69431 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8bed43b9-6903-37a9-80ba-d03c3d272942 | -5.71108 | -53.68483 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e5406fd-cf21-33a8-81d8-485876559668 | -5.71054 | -53.68827 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318070ce-373f-3841-ab2c-5e1ba91d6fac | -5.7096 | -53.73757 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ef46c4d-d937-3aac-a429-403382d980c4 | -5.70906 | -53.74101 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bcb4189-1e1e-32a1-807c-ed15c687eccc | -5.70778 | -53.68432 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46fc88b2-153e-3f1e-ad99-ad21aa9f6ca0 | -5.69034 | -53.73101 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce4e2208-d9d9-3c8b-aff1-1df8ddba8671 | -5.68927 | -53.7379 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36950424-2c12-349d-802f-17c92260d427 | -5.67168 | -53.91493 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25c81f15-e95e-358b-8a41-2c59b24c5155 | -5.66785 | -53.91786 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77762766-9b2d-3f16-bea8-abdcbf92a9fe | -5.64726 | -53.87228 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f278bf0-afa4-3020-a3db-5348066069d7 | -8.05697 | -53.18294 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d537e2e8-817a-3337-ad5f-d52676956ae4 | -8.05362 | -53.18242 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b50890e2-8fd9-399e-9ccf-415dd55320ea | -8.05026 | -53.1819 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06219120-14e3-3d49-a8f1-fa4fa15c4865 | -8.04987 | -53.22954 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44f2c624-1e2f-3207-8a8a-1115875eb0f2 | -8.04932 | -53.2331 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 911c7aca-f9c1-33ca-9271-867a3f0d5cb3 | -8.04878 | -53.23667 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd4b215b-2de3-3a5f-a7ea-c70e8b294e0b | -8.04769 | -53.2438 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fadeebf4-0467-39e7-b477-403201ca043b | -8.04715 | -53.24737 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a2850bc-c1ca-32df-92ab-5673312a7ca8 | -8.0466 | -53.25094 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9abdd163-543a-37d0-b091-fafeff3c6ef4 | -8.04652 | -53.22898 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20f2a1b3-23b1-31ae-a76f-8416f2191090 | -8.04605 | -53.25451 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README96.md)
