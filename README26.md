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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dfdcb80-dd1c-3658-81e9-afdeb290778d | -11.20785 | -54.78149 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d89262ca-7fdc-399f-9d86-3f113acdfdc1 | -12.6958 | -54.69199 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 327b1c6d-b3a5-332a-8f57-6c80224aafd3 | -12.69454 | -54.68282 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a9e331c2-f36d-309d-a35c-0ae7dca9a18b | -12.68812 | -54.70243 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d8edb9ff-dd7b-3399-b5c7-e30900402172 | -12.68687 | -54.69327 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3cdfe4ee-24aa-3160-9b5e-253218820a0b | -12.68561 | -54.6841 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d13d2375-552d-3a95-9313-4f512407e5ff | -12.68311 | -54.66578 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a25f0e64-6272-3ce6-9fc4-43e4990df7c2 | -12.68185 | -54.65662 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 862a37c5-3ac2-37aa-9b57-9edfc2e4bb9b | -12.67919 | -54.70372 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 30153731-599c-375c-9aba-1996b2b254e3 | -12.67794 | -54.69456 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| d3c93cc1-cc0d-3a00-81f6-eff460328b9d | -12.67669 | -54.6854 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dd2a8263-3f80-339d-92e2-1984bf0c4d71 | -12.67418 | -54.66706 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 41622a3e-5526-3c20-b03d-e6c5986daa59 | -12.67293 | -54.6579 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 8b036e28-17d0-3270-970e-02f3648bde24 | -12.66901 | -54.69583 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b5475255-ce6c-34b8-9103-091cf2e467ed | -12.66776 | -54.68667 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e7851d9b-3519-3b07-aed6-013418dfb2f4 | -12.66526 | -54.66834 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 78fc0643-07e6-3eb5-897a-3006d0c16d00 | -12.65883 | -54.68796 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b3189d4e-58f7-3c2e-8d40-0d955e066363 | -12.65633 | -54.66964 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 74cb239e-5397-341b-b3db-5ca98554ac7c | -12.45247 | -54.9996 | 2024-09-27 01:24:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cec92339-1f1b-3ed6-91bb-ab88b91fe3af | -12.44349 | -55.00091 | 2024-09-27 01:24:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b515ae1d-10dc-3180-9284-9cb36a37cb41 | -3.64127 | -54.04889 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| db1fe478-0a56-364e-b4d6-acf8f740c3a9 | -3.6399 | -54.03921 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 166fb524-b2d1-3cf7-8c92-9c16c6ad5642 | -3.35532 | -53.7802 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2041e664-c929-3f06-a9fe-fbd412a80fa8 | -3.34597 | -53.7815 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| da6bf4e9-db18-3343-bb38-5167098360cf | -4.57562 | -54.98401 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e97438d-d1cd-31cd-9b94-2fb687f7b8a9 | -4.57061 | -54.94839 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8fdfeece-2540-3ff6-94b6-de1827336f1b | -4.51807 | -54.84349 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8ef183ad-7ec1-39dd-9b70-55454cdfd392 | -4.50646 | -54.95478 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d7e71114-eb3e-3e84-b28f-390cc1eaed84 | -4.4937 | -54.99292 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 080bdc16-04ab-31e7-a8a7-400eae806145 | -4.48742 | -54.94833 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| efe52fb6-3b1a-3ecb-b758-63b321985e6d | -4.48482 | -54.99419 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ec2c155f-56e8-3533-b9aa-21fdad399a58 | -4.4798 | -54.95853 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 343e945b-404d-3486-9414-b72fdeb385d0 | -4.47854 | -54.94961 | 2024-09-27 01:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 036267c5-0625-3e1c-9dc0-22df113395cd | -3.74451 | -53.86008 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| adf5cc38-24ed-334f-b2f2-c5c83c744c43 | -7.92813 | -54.71782 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4edc8539-dead-311a-a9f4-063d4d87b97f | -7.91929 | -54.7191 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f1070b54-8e95-3299-9564-5dfd6bd34fc9 | -7.91805 | -54.71022 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9fb3ab71-8c50-3b06-9d0c-a255ecaee64d | -7.91058 | -55.10964 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 008f9a1f-4263-32ae-851f-4d38270b874c | -7.91045 | -54.72038 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa97842d-bbc9-3d64-9ea5-21024a8a3959 | -7.894 | -54.73182 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 065ae9c3-0d67-301f-b963-f27e3c89da10 | -7.88516 | -54.7331 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bd40ecdd-dd2a-39ec-8b27-f8742e017faf | -7.88391 | -54.72424 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3128f14c-fee0-3d05-af2c-7806da7037b3 | -7.87771 | -55.53907 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82759c3e-7622-33f4-8782-bd73f8f23745 | -7.87524 | -55.52111 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9e5e5644-5487-3426-9a8c-e2a5045a5de6 | -7.87401 | -55.51215 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 498c2e59-5680-3986-8c55-d4c84856857c | -7.86882 | -55.54032 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0bc14288-d413-3225-a330-dd5d331c2527 | -7.86513 | -55.51343 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 615d7cd1-bed9-30b9-a7eb-58805523a6d7 | -7.82094 | -54.73964 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f7efba81-bd32-364f-bbbc-d52e040f8658 | -7.8197 | -54.7308 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 54da7801-d8b3-35eb-822f-10706d798ad1 | -7.81846 | -54.72193 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2f7039e2-94c6-39e0-94a1-7cffedcf60a8 | -7.81209 | -54.74091 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 479b6852-29bb-35b7-9bb0-2c400ce76ae9 | -7.81085 | -54.73206 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5fe63a4a-933b-34e3-823f-d9d42dc4226f | -7.80961 | -54.72322 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5315ee3a-d3cf-34ae-955f-c37a5eb13fa7 | -7.80837 | -54.71432 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4760c79c-43a3-35f9-8496-38ddfd4612cf | -7.80325 | -54.74219 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 72886c55-64f6-353f-9898-11f853c98e1b | -7.80077 | -54.72446 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| faa1adfd-b5a0-335c-8ecd-56f20a3b2591 | -7.79068 | -54.71683 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2217023-6efe-3fe4-9cee-201973d2de09 | -7.74405 | -54.78379 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3ef514a3-8ab4-3e45-a7fa-a5f4d67ffda4 | -7.7352 | -54.78506 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 912a2567-672c-348f-bf8d-7d0b8da03f0a | -7.69203 | -55.33171 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ab41349-0a2e-3537-9c37-cefc95061684 | -7.65808 | -55.28214 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb2cc41a-c456-362b-87eb-388e2c658f11 | -7.62397 | -55.37455 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a252f7a9-b696-399a-bfc1-d0471c16235a | -7.61492 | -54.9715 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5bdfe62a-bb42-3e8b-88b8-5c091aa68e36 | -7.61265 | -55.35801 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b0dfa8ee-271b-3869-9acf-94894760d1cb | -7.6104 | -55.27671 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86e128cc-fdee-3fd5-8d2e-ee86ea38ea51 | -7.59806 | -55.18789 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c612332-6cd3-3d64-9eaa-75f917830628 | -7.59559 | -55.17014 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dd0dae3a-54cc-37e9-839a-8441e996ab1e | -7.59371 | -54.96238 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3ad81a6-0f2b-3c10-b4bb-5fcbdb909b4c | -7.57441 | -55.0827 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37d2e51d-2c70-3d80-a4d9-cadb8a8c5c71 | -7.56782 | -55.16505 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 56db17eb-11de-370e-a59c-11a78501e91b | -7.55405 | -55.13084 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78dccc66-4ffd-38de-a413-b2743890ba2d | -7.55282 | -55.12197 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ef1e6faa-df63-355c-9bc5-ebc53868cb34 | -7.4065 | -55.20024 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5210716d-a261-3f82-89e7-1d453181f811 | -7.37418 | -55.50138 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 363195ef-ab4d-37ac-a64e-830d7c94f6da | -7.30152 | -54.91441 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e1e21888-6870-3e4b-85f7-6ed806f60006 | -7.77301 | -61.19563 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| eb15c943-ef58-30a5-a9fd-1ece90c4ab8b | -7.78272 | -61.18135 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a7681551-02d8-3734-a8ed-490be8e4c91a | -7.92643 | -55.76171 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ac99a24-14d5-3733-9647-2e85811224e6 | -7.78522 | -61.2005 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d5c32350-8fe0-3514-be48-eed74717e5b4 | -10.68468 | -55.53486 | 2024-09-27 01:24:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 11e2e1e5-6a59-34c4-9d8e-fc16a62f7c22 | -7.7857 | -61.19405 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| e443aef4-c581-3eba-bc55-c416c1cf95c9 | -6.56872 | -60.0612 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ddf96954-eb2b-34fc-8282-95aa1cbf46dc | -6.74385 | -60.08775 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f0c59827-a925-3580-8d4b-f4a6acc56326 | -7.46092 | -60.4021 | 2024-09-27 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8490594c-c11f-3ed7-9156-953547bf50eb | -13.48532 | -57.25848 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f489f08d-c4e0-349f-88f7-4008a41dbce8 | -13.12076 | -57.19681 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cee9f655-00f4-35a5-a49d-acc525a6b98b | -7.47276 | -60.40075 | 2024-09-27 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5b3ff82f-d003-3744-88a8-404ca0483f22 | -13.06759 | -57.2648 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d46bc9d0-b70e-33f1-8e46-4e161b4d4e34 | -6.82454 | -59.0464 | 2024-09-27 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d62d5346-67fb-34a8-8897-c08694c2d403 | -13.78573 | -56.50775 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb326e6f-43b9-303e-aca0-17ef1e115939 | -13.77453 | -56.49802 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47143dd4-7242-32f1-8b6d-86f2e3fdc912 | -3.59155 | -55.53158 | 2024-09-27 01:24:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbae45b7-cb8a-37ad-a3af-49f35d4337a9 | -3.58314 | -55.4067 | 2024-09-27 01:24:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8d1e7a1c-0e22-384f-97aa-74f639bfb532 | -9.61387 | -57.76106 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ff68ea52-0c55-320c-a5c8-5638c3aa5f92 | -4.28436 | -56.40596 | 2024-09-27 01:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8e20c7c0-e2e7-3f88-9309-2efd12bd4073 | -7.29334 | -55.11439 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 95f24691-ab6e-3599-8d3a-bbbcf0489f1a | -7.29211 | -55.10553 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5d98c196-be66-3f31-b446-96f9142a054f | -7.98257 | -55.03008 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d77a051c-e165-3a73-b98f-b7ca24a1df13 | -7.19152 | -55.04445 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c9a45b3c-0e76-3297-8207-c57c1284be29 | -7.19029 | -55.03559 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |


[Clique aqui para ver as próximas entradas](README27.md)
