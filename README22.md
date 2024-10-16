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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a075cf34-51e6-341b-bdcf-8b4a9240cd2f | -3.1283 | -54.2259 | 2024-10-16 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 171.9 |
| ffc1b4fe-c654-3a98-91db-60e6754a053a | -3.958 | -46.4442 | 2024-10-16 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| d0dab989-6297-350a-8564-a1bc5e89d9d7 | -3.9581 | -46.422 | 2024-10-16 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 1f30120c-c294-35f8-acbc-d2c2e4273066 | -9.1728 | -65.3945 | 2024-10-16 02:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ef907d72-94e9-3f35-b593-7871c38fa5f6 | -11.6917 | -65.2243 | 2024-10-16 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 14f31f8c-0773-3a80-abde-7544010c8162 | -11.6918 | -65.2054 | 2024-10-16 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 3f66ee13-ded0-36bf-b8b8-8ea5277fadab | -11.7103 | -65.2424 | 2024-10-16 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d947b903-955a-3de6-b818-86a49ed180ea | -11.7104 | -65.2235 | 2024-10-16 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ec5571ad-e581-30c4-aa1a-e548147ea5a4 | -11.7106 | -65.2046 | 2024-10-16 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e4598184-bf6f-3b5f-8378-ec3af9f65e2b | -11.9381 | -64.8729 | 2024-10-16 02:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a8e4d549-33a0-3c7a-baaf-8a76c124c8a9 | -11.938 | -64.8919 | 2024-10-16 02:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 73983d0e-ebfd-300a-9057-9896df3edb82 | -12.4733 | -47.2846 | 2024-10-16 02:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c4e090d2-3aa2-3509-b1ae-61c96b0e152e | -12.4925 | -47.2818 | 2024-10-16 02:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 95a64bd1-cb7b-3e32-8302-a737b23f5e3f | -12.3793 | -63.7294 | 2024-10-16 02:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 75bae69e-4679-3c5d-9d8d-a8b1915522dd | -12.3795 | -63.7103 | 2024-10-16 02:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2b6208ef-c6d2-3098-8762-dddf27f8f0f3 | -12.3982 | -63.7284 | 2024-10-16 02:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9dddcb0f-d5ba-38bd-ab38-e3bfc472e2b9 | -12.3983 | -63.7093 | 2024-10-16 02:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 838a8e42-23e7-3956-8431-2648a6eb51da | -12.7822 | -62.9409 | 2024-10-16 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 8d0bc955-2214-3dec-af24-27a04c46c153 | -12.8012 | -62.9398 | 2024-10-16 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3fd8f09b-446d-36db-96e8-426d777df611 | -17.3041 | -42.643 | 2024-10-16 02:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 17061179-9862-3dc9-ac42-ea3053112ff5 | -17.2639 | -42.6527 | 2024-10-16 02:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c429d508-e1ff-37b1-a00a-b78118c5ea9f | -17.2439 | -42.6575 | 2024-10-16 02:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5fb25fc8-1c46-3171-9926-586b8dd84038 | -16.9403 | -57.5063 | 2024-10-16 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 96f665d6-2129-32c2-a6ff-f51d924eb6e0 | -16.9596 | -57.5245 | 2024-10-16 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| d4d38024-8e1e-3df1-8dd4-f1f43efda4f4 | -16.9599 | -57.5041 | 2024-10-16 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 1f6ea886-33df-32c2-95b5-40cb7b661ee3 | -17.0066 | -58.2934 | 2024-10-16 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 6c65f381-b545-3788-8207-1c9c37c1da2b | -17.0262 | -58.2912 | 2024-10-16 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| fdbb65f3-91dc-379b-8d1c-13c8cf556d83 | -17.1754 | -57.4995 | 2024-10-16 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| c25bd72d-fa31-39ae-b21f-4e9d62b5bac4 | -17.1758 | -57.479 | 2024-10-16 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 466a7835-d1c3-3b7e-9e11-05be7c92babf | -17.1951 | -57.4972 | 2024-10-16 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.7 |
| a4e7a553-0978-36e8-a041-5d13264a9e4e | -17.1954 | -57.4767 | 2024-10-16 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| d4a76049-ea28-3f7a-8d8e-ca5ed7231ae5 | -17.2081 | -56.6946 | 2024-10-16 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 43a7ef60-9dd9-322a-9ee4-3ff1e939864b | -17.9043 | -57.4122 | 2024-10-16 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| f63f04ba-9300-3785-b0de-aad77f67a2a6 | -17.904 | -57.4328 | 2024-10-16 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| ca7b96d3-6a11-3a86-a3d4-82ac7dc9b177 | -17.8842 | -57.4352 | 2024-10-16 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 86b54c6f-5b76-3d93-8486-370c325ee071 | -17.9241 | -57.4098 | 2024-10-16 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 5d0bab4c-54e2-30a4-9998-46803d11dca7 | -17.9237 | -57.4304 | 2024-10-16 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| eca6fb95-86e4-3ddb-a984-5015a8110d26 | -18.254 | -56.6029 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| b4a81be8-2e39-36da-894e-ee9477580782 | -18.2544 | -56.5821 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 202.1 |
| 8cde06e0-44fa-3e7a-9832-1199fe06e42d | -18.2548 | -56.5613 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| f00e3fe0-1032-3484-8d93-e0a10741788e | -18.2739 | -56.6003 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 6d219def-2fec-3c1f-bdb0-cb59adf309de | -18.2742 | -56.5795 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.9 |
| f00a85fd-30cf-3130-a36f-fd93c2e697fe | -18.2746 | -56.5587 | 2024-10-16 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 7e356398-0757-3bc9-826d-7f82bf463226 | 1.0199 | -52.2162 | 2024-10-16 02:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a54bcb8e-cf59-3fcb-bf88-77501d8f5db1 | 1.0016 | -52.2164 | 2024-10-16 02:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 8b40743b-987a-3658-80de-9ddbbb0b31ce | -3.0687 | -50.3746 | 2024-10-16 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ea78c290-323e-3f50-bd12-d696373baaa0 | -3.1098 | -54.2464 | 2024-10-16 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c223a648-49b1-3b5b-a2b7-0ed69684d3b8 | -3.1099 | -54.2263 | 2024-10-16 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| d1c3e336-ab0a-3e2f-b371-3446ae63890b | -3.1282 | -54.2459 | 2024-10-16 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| e2146601-0e03-333e-b2d8-dae41b8d7b47 | -3.1283 | -54.2259 | 2024-10-16 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| c66c9be4-f9d0-328a-92c0-bae61e70b05e | -3.2862 | -47.133 | 2024-10-16 02:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0a6ce6b9-faaf-3966-a8bb-e89a43cefc80 | -3.958 | -46.4442 | 2024-10-16 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| f5f465bf-7928-3d22-b536-457779db61a5 | -3.9581 | -46.422 | 2024-10-16 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| abd6dc7f-4150-3ead-8d8c-91f0c9ee502e | -9.0948 | -47.0316 | 2024-10-16 02:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 707b5a28-2f81-39ff-ae3a-dfa2bd803e16 | -9.1137 | -47.0296 | 2024-10-16 02:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fbf0fcc7-68e1-3d5c-9c9f-51718307b58c | -9.1712 | -46.9569 | 2024-10-16 02:35:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 735bb202-e923-37af-bc2d-46bd70e6c55c | -9.1728 | -65.3945 | 2024-10-16 02:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 15b79387-68b1-3114-8a03-10e0f15f99a1 | -12.38214 | -63.71781 | 2024-10-16 02:36:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d283262e-3526-36f0-8ea7-4291332e2ced | -11.70826 | -65.21316 | 2024-10-16 02:36:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 212f3c54-afcc-32e6-bb77-52be0f208b17 | -11.6917 | -65.2243 | 2024-10-16 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c073df4b-12e4-3530-beea-0a7aa9004661 | -11.6918 | -65.2054 | 2024-10-16 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ad33985c-2645-3c4f-89a1-9e52419c6f2f | -11.7103 | -65.2424 | 2024-10-16 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b3c2f2a0-28e0-3185-ae4f-1bcf3ad2b359 | -11.7104 | -65.2235 | 2024-10-16 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4d07d44d-6dd3-3ba0-8c18-aca60d86429c | -11.7106 | -65.2046 | 2024-10-16 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 998c6230-8278-3a4f-a1e3-05ffbd1db33f | -11.938 | -64.8919 | 2024-10-16 02:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| faf77c13-ed25-32ab-9d0e-f578e88424f5 | -11.9381 | -64.8729 | 2024-10-16 02:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 31f01e8b-15a5-3b05-89f1-245d30d11de3 | -12.3793 | -63.7294 | 2024-10-16 02:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5da6fe80-7592-3c38-afa3-bad03ef1aece | -12.3795 | -63.7103 | 2024-10-16 02:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 338b9da9-641b-3dc2-a0bd-1654216becf2 | -12.3982 | -63.7284 | 2024-10-16 02:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| dce7a591-fefe-346d-a4ae-ddbb50af2797 | -12.3983 | -63.7093 | 2024-10-16 02:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4e19f53c-b0d5-3b81-90a7-b17719586d9b | -12.515 | -63.263 | 2024-10-16 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| af28cc0a-5678-3f5d-a37d-a096e68ee261 | -12.5152 | -63.2439 | 2024-10-16 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 3a336e15-107e-358f-a217-a43408c28e67 | -12.5339 | -63.262 | 2024-10-16 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bff96993-680b-3b41-9ebb-aff25effe94e | -12.5341 | -63.2428 | 2024-10-16 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b85b4c16-a7f5-3c10-b283-f2f9d1594828 | -13.383 | -46.947 | 2024-10-16 02:36:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8efbc4cf-ebd5-3c9d-a59c-1faebc5fd4f6 | -17.1754 | -57.4995 | 2024-10-16 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 4417a08a-5da3-3cbd-a714-7cb95d67bcc3 | -17.1758 | -57.479 | 2024-10-16 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 815ad84e-9e9c-3f24-bb9f-ff0dcf38ef96 | -17.1951 | -57.4972 | 2024-10-16 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 1d7150b7-ff5b-3260-9214-f3c7fe9e9a1f | -17.1954 | -57.4767 | 2024-10-16 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 4dc5d334-72b6-32b7-8bca-88ac54fdaef7 | -17.2081 | -56.6946 | 2024-10-16 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| e179965b-8662-3832-b703-83c45b4ca553 | -10.19154 | -68.31709 | 2024-10-16 02:38:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d8066714-eb7e-3ae8-81f0-923b09c79567 | -10.11307 | -69.16744 | 2024-10-16 02:38:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9495856e-d067-3c9e-aeb0-842c61e64170 | -10.63203 | -67.83398 | 2024-10-16 02:38:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 18a824cc-b10f-32ad-ad9a-2a279d4c72a2 | -9.46868 | -68.48366 | 2024-10-16 02:38:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa3e7abd-22e7-355d-a003-2c6fb8758d0d | -9.7772 | -67.95166 | 2024-10-16 02:38:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 82d2da6a-4c7e-342a-9a58-b3dafbb1c7ff | -9.45342 | -67.15401 | 2024-10-16 02:38:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0b621c49-477d-3f3d-ba80-2a69ae6ad0c6 | -8.61352 | -70.04205 | 2024-10-16 02:38:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4403ed99-32ea-348a-a0da-ed3d0296f115 | -8.1787 | -72.93237 | 2024-10-16 02:38:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf3e385c-373a-3d08-b477-36a0ef1a7a4e | -8.17742 | -72.92334 | 2024-10-16 02:38:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 58a55ce4-229f-364e-922d-4a2f8bcbeb87 | -7.40535 | -72.61863 | 2024-10-16 02:38:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7491e2f3-773d-3765-bfb9-ece14ab547b2 | -7.40402 | -72.60936 | 2024-10-16 02:38:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dff4a256-4649-33ad-b84a-5857b47b4def | -7.38931 | -72.507 | 2024-10-16 02:38:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2fd7355-5bbf-3907-8dfe-4471b305cd38 | -10.62496 | -67.84177 | 2024-10-16 02:38:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1a720ff4-e2a1-3666-b87d-1e1ec8328be9 | -10.8999 | -69.64205 | 2024-10-16 02:38:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 55a9b204-dcdc-320f-8f7d-998b4a2cdc1c | -10.86859 | -69.43351 | 2024-10-16 02:38:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97d300e7-7f38-36e3-bb7d-abad748bb17f | -10.63664 | -67.8398 | 2024-10-16 02:38:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 855dd168-3151-3a34-b86d-8afb47265308 | 1.0199 | -52.2162 | 2024-10-16 02:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 3e85e28a-7cef-3a62-ad79-7a939028211e | -2.5444 | -47.2231 | 2024-10-16 02:45:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 7e7625e9-97f9-3d2b-bd26-5086d6dadf68 | -3.1098 | -54.2464 | 2024-10-16 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 82ee5dea-a360-3f68-876a-c6dfa28d4aee | -3.1099 | -54.2263 | 2024-10-16 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |


[Clique aqui para ver as próximas entradas](README23.md)
