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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ad1fb59-4fd9-3632-b506-45d2e5c6cfc7 | -13.0135 | -62.465 | 2024-10-13 08:46:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 59c9a0a3-f6c5-3401-ab23-e9a3d299aead | -16.9995 | -57.4791 | 2024-10-13 08:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 2428cbd1-efa3-3128-9cb7-6577dcc72fab | -16.9998 | -57.4586 | 2024-10-13 08:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| b381799e-0e53-3bff-9be8-1906a8fe764e | -17.0001 | -57.4381 | 2024-10-13 08:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| efad1c2f-c275-3d13-a0bb-e20058cd8681 | -17.1761 | -57.4585 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| e7c9366e-cc71-3e1f-b563-a171d0b4ee90 | -17.1764 | -57.438 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 6ec171ee-1852-333d-aeac-1196005f6e2a | -17.1954 | -57.4767 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 8438d111-54ce-352e-af9a-800144c570d5 | -17.1957 | -57.4562 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 6ca87dc2-2408-3bfc-b0af-de990fa25559 | -17.196 | -57.4357 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| eb6ca8f3-af18-33ab-98ac-48edb3aeb3a7 | -17.1758 | -57.479 | 2024-10-13 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 9165c741-423e-3412-9644-c8a696f67cab | -17.6474 | -56.2876 | 2024-10-13 08:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.9 |
| 467f367d-bc87-35dd-92d7-f147a1805a87 | -17.6478 | -56.2668 | 2024-10-13 08:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 780fbf1b-890e-32a0-9eea-07d1373dacd9 | -17.6672 | -56.2851 | 2024-10-13 08:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 5659360d-d280-39ae-aa87-62faf60dd7e3 | -9.8551 | -60.3159 | 2024-10-13 08:56:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3b0b27d3-df93-3856-8916-88849ddc4788 | -9.8364 | -60.3169 | 2024-10-13 08:56:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c6722524-a2ba-3522-b3d3-986e67d753f9 | -12.4792 | -63.0159 | 2024-10-13 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 2a3e80cf-681b-38d4-958d-3b710ca2bdcf | -12.4794 | -62.9967 | 2024-10-13 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 9fd7280b-f20a-3978-885d-b5ad61d60826 | -12.4981 | -63.0148 | 2024-10-13 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.1 |
| e3f9a8ff-1199-33ee-a7d1-3b95371483de | -12.4983 | -62.9956 | 2024-10-13 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 897819f4-ab89-3b47-a197-c648b4aa5578 | -12.9372 | -62.5275 | 2024-10-13 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ce8e9b74-b1fa-3e7d-af87-670378061664 | -13.0133 | -62.4843 | 2024-10-13 08:56:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b40514f5-c3b1-3bc5-923b-bf1a286bd478 | -13.0135 | -62.465 | 2024-10-13 08:56:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6a8c97ee-31cb-3a60-81a1-e1c37d5d9f47 | -17.93 | -57.38 | 2024-10-13 09:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 462483ed-7944-346c-9f98-8ce68b03dd38 | -17.9 | -57.28 | 2024-10-13 09:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1018e789-afd3-3d6c-a7ba-e8f7ca964edc | -17.9 | -57.36 | 2024-10-13 09:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 78d53624-eac6-3387-b915-95609baf0270 | -12.4983 | -62.9956 | 2024-10-13 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0e58b996-2d38-35c7-9148-50a72f3d439b | -12.4981 | -63.0148 | 2024-10-13 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 8003f666-a6c1-3385-9218-465bb3b930f4 | -12.4794 | -62.9967 | 2024-10-13 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 144.0 |
| baf15258-627c-31e2-a0ab-3a73c57f8bb9 | -12.4792 | -63.0159 | 2024-10-13 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 234.8 |
| 29373bb0-289e-3c73-a780-28b5619e96db | -13.0135 | -62.465 | 2024-10-13 09:06:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8b459396-c2be-3401-861e-623764aa8826 | -13.0133 | -62.4843 | 2024-10-13 09:06:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e333be55-41bc-3577-96eb-c484655e17e5 | -17.6474 | -56.2876 | 2024-10-13 09:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 231.9 |
| 77b6a183-ccb9-3a1b-a2a7-6e5afc1d26c8 | -17.6672 | -56.2851 | 2024-10-13 09:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.7 |
| ed4eedba-787e-3240-bd6e-6922c0b5dc91 | -17.6672 | -56.2851 | 2024-10-13 09:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.6 |
| 348883e3-51e5-348b-9831-b4e7ffe8d1e2 | -17.6474 | -56.2876 | 2024-10-13 09:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.2 |
| 79aec272-0aa3-3a28-a8fb-203c327b84e6 | -17.8467 | -57.3164 | 2024-10-13 09:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 94287899-2116-348f-b657-42a7aad43ef9 | -17.9643 | -57.3637 | 2024-10-13 09:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| ce951a9a-75f9-35b6-8cdb-31ab218a65c4 | -17.964 | -57.3843 | 2024-10-13 09:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.2 |
| 4c467eb2-9284-3896-8c45-ba7adf4eec9a | -17.6474 | -56.2876 | 2024-10-13 09:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.6 |
| dcb10e26-a19b-3bf7-a77a-ab884a2e1a96 | -17.9643 | -57.3637 | 2024-10-13 09:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 096ddad0-4722-39c8-b1d6-2bd7e6710842 | -17.8467 | -57.3164 | 2024-10-13 09:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 4bab706c-2418-35bc-98cf-5472b4edd834 | -12.1872 | -50.7339 | 2024-10-13 09:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 6ab2b9ae-0ca0-3c96-807a-16747c31058f | -17.6474 | -56.2876 | 2024-10-13 09:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 196.8 |
| 2ef56bd3-f95d-3d39-a1da-bd1f40c58092 | -17.9643 | -57.3637 | 2024-10-13 09:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 87ca04cb-cb30-35c3-8cd4-0f1717d32076 | -17.9841 | -57.3612 | 2024-10-13 09:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 75618d77-e3ca-393c-85a2-9052cf8a204a | -12.1872 | -50.7339 | 2024-10-13 10:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 280.6 |
| f3931d4f-d7cc-3d6c-8fc8-291cec33e84b | -12.1869 | -50.7553 | 2024-10-13 10:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 0bb4a185-2558-3edc-a797-df0adfbf0312 | -12.2063 | -50.7316 | 2024-10-13 10:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| f1566c97-0dbc-368e-845e-73f19e15b9a6 | -17.6474 | -56.2876 | 2024-10-13 10:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.6 |
| 62198697-3830-310e-ac38-326644217835 | -17.9643 | -57.3637 | 2024-10-13 10:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 8ff1496e-8e0c-39b0-be5c-742c6cf1c81a | -17.964 | -57.3843 | 2024-10-13 10:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 7d3c455d-1287-3e6b-8476-55b0590a64cf | -17.9841 | -57.3612 | 2024-10-13 10:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| ecc050d5-20ff-3022-be02-89e06e12596b | -12.1872 | -50.7339 | 2024-10-13 10:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 61feba9e-6717-3fba-aacd-3a3767736d56 | -12.2063 | -50.7316 | 2024-10-13 10:16:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 56898f0b-30dc-3a42-a0bc-64d3732551ec | -17.6474 | -56.2876 | 2024-10-13 10:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.6 |
| 21bfcedf-fa77-329e-8fe3-7892c465be34 | -17.9643 | -57.3637 | 2024-10-13 10:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.4 |
| eda7b341-86a5-39a0-94a6-892110e8ec68 | -17.964 | -57.3843 | 2024-10-13 10:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 779def16-8bdc-3ce2-ad56-c664f8f20664 | -17.9841 | -57.3612 | 2024-10-13 10:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.9 |
| a628a921-45d3-3246-af42-4d8b2f4e3276 | -12.1872 | -50.7339 | 2024-10-13 10:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 1eb6952a-27b7-3048-99f2-f1c7061192c4 | -17.6474 | -56.2876 | 2024-10-13 10:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.4 |
| d8bfce92-aed0-3c1f-92b4-6ce25146f6be | -17.9643 | -57.3637 | 2024-10-13 10:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| dda4c1f9-1ce1-3f1f-8469-c2bd7b8c2a35 | -17.6474 | -56.2876 | 2024-10-13 10:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.7 |
| a0715a2c-c986-3a07-a905-9b06c4f2b38f | -17.8856 | -57.3528 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 5139b185-ba91-3004-9640-ddc13c27b767 | -17.8863 | -57.3115 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 7ee45ce5-04cb-398b-a37e-a051a2c44a66 | -17.905 | -57.371 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| e059e7c3-ef8f-314c-aa61-237bc480409b | -17.9057 | -57.3297 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 525.1 |
| 1ab7353b-6ed3-3d2b-9c26-54f3266db337 | -17.906 | -57.3091 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.2 |
| ff0b2018-c761-371b-80a7-9332446f3a81 | -17.964 | -57.3843 | 2024-10-13 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 690c2c2e-19d8-3df1-956f-7ded480015f6 | -17.6474 | -56.2876 | 2024-10-13 10:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.0 |
| 33f1ed58-40b9-3c6e-b99a-11ade8562044 | -17.6672 | -56.2851 | 2024-10-13 10:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 98bac9fd-5036-3d61-a716-6d7ecb2f54a3 | -14.2821 | -41.2229 | 2024-10-13 10:56:26 | GOES-16 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 3b1f8394-a649-33db-903b-a1ccd8e4a025 | -10.7645 | -46.751 | 2024-10-13 11:06:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 2013fb14-9142-3b16-8acf-fe6e790186fc | -17.1761 | -57.4585 | 2024-10-13 11:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 3c893699-ccc1-37a8-a84e-b20bcd1c2fde | -10.7645 | -46.751 | 2024-10-13 11:16:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 3a0c6a15-2f49-3d49-8f41-f595dd8e9bc3 | -10.9311 | -44.6789 | 2024-10-13 11:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 814574d8-8ede-3e55-b262-fbb7e94a28c1 | -10.7645 | -46.751 | 2024-10-13 11:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1f60a883-5b74-3a3e-b6f1-fe145ff1b512 | -10.9311 | -44.6789 | 2024-10-13 11:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| f008c864-7982-3095-8134-e29718290219 | -11.9443 | -45.7769 | 2024-10-13 11:26:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| cc092654-2a68-37fc-bf75-b48ff20f3323 | -10.7645 | -46.751 | 2024-10-13 11:36:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f909ae98-5429-3b8e-ab5b-497871470dd2 | -10.9307 | -44.7021 | 2024-10-13 11:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| fbc28b52-53a0-38a6-97a0-add08752eb27 | -10.9315 | -44.6557 | 2024-10-13 11:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8e854aca-46cb-34fe-a7b0-86c5980b36f3 | -10.9502 | -44.6762 | 2024-10-13 11:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 716cad72-261d-3bff-9c0c-6e9c36be0abe | -10.9311 | -44.6789 | 2024-10-13 11:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 753087e0-9e4f-37af-9d0e-c79d503d6beb | -11.6334 | -48.3736 | 2024-10-13 11:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1fee4ddc-c72f-3ff6-bb2b-e583e6c75e58 | -11.9251 | -45.7797 | 2024-10-13 11:36:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 28413811-4b88-3137-b2ea-f15428a13f80 | -11.9443 | -45.7769 | 2024-10-13 11:36:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 1a14dadf-ca6b-348e-838d-74b8a52a0546 | -10.2597 | -46.2286 | 2024-10-13 11:46:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 1a360a99-1dea-32a4-8eba-701aa6cf6eb6 | -10.2594 | -46.2512 | 2024-10-13 11:46:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 576a5f1f-4a85-360d-9255-a1d851233f99 | -10.9315 | -44.6557 | 2024-10-13 11:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 28fa9820-3dbb-3c72-a53f-0eb55a2f2fc2 | -10.9502 | -44.6762 | 2024-10-13 11:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 235.1 |
| ff0d37fa-7002-3260-b94d-c9450c11c77b | -10.9311 | -44.6789 | 2024-10-13 11:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 885.0 |
| 4ca4f9a0-659d-367c-8492-d48605bd3979 | -11.6334 | -48.3736 | 2024-10-13 11:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d4917667-7378-3c34-a642-5f085a7cb3c2 | -11.9251 | -45.7797 | 2024-10-13 11:46:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d919280a-6e46-3e70-a0bc-105b7499294b | -11.9443 | -45.7769 | 2024-10-13 11:46:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| c30e3b35-5414-3fd8-93db-e79735efd749 | -10.1637 | -46.3079 | 2024-10-13 11:56:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f6e3723c-d41c-32f0-bc2f-34adc25d8dec | -10.7835 | -46.7486 | 2024-10-13 11:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2fc8388f-add5-3d3b-8385-7f91cde5ce23 | -10.7645 | -46.751 | 2024-10-13 11:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cd9f3f3f-f860-349b-b018-42ba2eced14f | -10.9311 | -44.6789 | 2024-10-13 11:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 498.1 |
| 0c875198-3863-39f1-b130-bd5c26154a50 | -10.9502 | -44.6762 | 2024-10-13 11:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 1cbcdce0-aa72-3c72-b085-0c6b4ec07d3a | -10.9116 | -44.7048 | 2024-10-13 11:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |


[Clique aqui para ver as próximas entradas](README117.md)
