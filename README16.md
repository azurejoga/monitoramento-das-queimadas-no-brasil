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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afa0d704-c782-370e-80ed-da7db2d21d71 | -10.4355 | -67.68208 | 2025-06-03 05:38:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd15a51b-2b1a-32e7-b759-e54497fb6334 | -11.91724 | -54.82033 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 110b1b96-f70d-3a32-8786-3ae8bfd99841 | -9.58018 | -63.24775 | 2025-06-03 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2293c8f4-3def-30cd-bd18-260f73f85b46 | -18.8675 | -53.6434 | 2025-06-03 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 5aefb416-edd4-3cba-8fad-7e13b3069b4f | -6.9791 | -42.9034 | 2025-06-03 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 337410ef-3d0e-3391-bcd8-61bfadc9457b | -18.8875 | -53.6402 | 2025-06-03 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 125.8 |
| e065fa1c-7524-35c3-b01b-fd0b31b4ecd8 | -18.888 | -53.6186 | 2025-06-03 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8f5761a9-b029-32a9-af59-6c28677683f7 | -18.8679 | -53.6218 | 2025-06-03 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 818b9463-8588-338d-b3a7-32b10074370a | -18.87776 | -53.64085 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7adf52ec-7599-3f07-9069-733dbc6d5ac7 | -14.01966 | -55.12437 | 2025-06-03 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb709c53-11b3-33a2-bb17-4f3f95204729 | -18.87725 | -53.64667 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7cf02708-9e54-3ec7-800d-c49d6e5c5424 | -14.02014 | -55.12018 | 2025-06-03 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cb67082-fd35-3555-b7cb-47ea858031ef | -18.8716 | -53.63431 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1b071f47-6193-3985-ac2d-a9427997c969 | -13.6375 | -52.18665 | 2025-06-03 05:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30e64416-b01b-35db-94ff-f67a987a2e79 | -14.02397 | -55.13762 | 2025-06-03 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ad798c-67b9-3fd1-a86a-ecd32c9b1b86 | -12.87961 | -61.63939 | 2025-06-03 05:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 574d2081-3970-3b61-a605-860c78b122f7 | -18.87109 | -53.64017 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 73219185-1215-322d-9fca-b55f247b1375 | -14.02972 | -55.1384 | 2025-06-03 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ceeb2686-9d3c-35d9-8abf-56dd906147b8 | -16.70238 | -57.963 | 2025-06-03 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 42a29f88-87eb-3eb5-8059-334eca51a347 | -14.0139 | -55.12362 | 2025-06-03 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc1f2c61-bb92-3123-b8ee-ed0e90f47155 | -12.14697 | -64.15203 | 2025-06-03 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee144976-7cf0-3d18-8f83-df9a44c8aa77 | -18.86493 | -53.63354 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 18.9 |
| add1d268-e65a-31bf-aff0-971370573acc | -18.86443 | -53.63936 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 324a96bc-46ff-39dc-8e63-d3a373cd044a | -16.70734 | -57.96356 | 2025-06-03 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dcf35f8f-c2d5-3882-897b-dde25ac511f7 | -13.63742 | -52.18526 | 2025-06-03 05:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 299c3ee6-fe77-3068-a423-ca527dca0ef7 | -13.72213 | -58.67183 | 2025-06-03 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c0e9ec6-275f-34ca-aa86-e2fe697980d8 | -13.72153 | -58.67639 | 2025-06-03 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0925f1ee-05d4-3289-8080-4fb728400df3 | -18.87059 | -53.64585 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 02a17665-dc6e-3957-8016-5f800d711a5d | -18.86393 | -53.6451 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cd4f9a3c-47d7-3630-ba3b-41fd2276951e | -16.70338 | -57.96409 | 2025-06-03 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec4d2f96-e8e0-3e60-9380-6f197b7d6136 | -16.70403 | -57.95838 | 2025-06-03 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a13edd4a-dbd4-3471-a557-4c61652e831b | -18.87828 | -53.63489 | 2025-06-03 05:40:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2e20dfb6-4b37-363d-9e4b-d54ab0c3e4e1 | -20.71773 | -56.63373 | 2025-06-03 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ff80b05-d635-3634-b0a2-3fe5b3407833 | -20.71815 | -56.62939 | 2025-06-03 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 110bd15b-a054-3297-a1c3-c323e8bf49ff | -20.71249 | -56.62856 | 2025-06-03 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54432d65-8d10-3d74-95a4-564934e56bc3 | -20.72382 | -56.63014 | 2025-06-03 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90bd06b5-a1b7-3989-acee-2774177ab4a5 | -18.8875 | -53.6402 | 2025-06-03 05:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1bfb8895-b313-3add-9f0d-96ce9c1e8ffc | -18.8675 | -53.6434 | 2025-06-03 05:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 62dc81c6-9d33-32d2-a8e6-abefb5ddfb7b | -18.8679 | -53.6218 | 2025-06-03 05:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a94865ab-00f1-37f6-bd85-d1f4b516bb65 | -9.96313 | -64.96367 | 2025-06-03 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7861c360-58fd-3261-b4fe-fb5def64e2f5 | -9.23577 | -63.29354 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2120d419-8093-39ce-af61-94074f9fe55f | -9.75703 | -67.3276 | 2025-06-03 05:59:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1bd451-0b28-36cf-a26e-ae7334fccb85 | -9.23948 | -63.29227 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4327f63-f50d-33d8-b18f-09b9d0820c70 | -9.24117 | -63.28913 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d474887-14e3-3ac2-9349-477813ea862d | -9.63779 | -65.40748 | 2025-06-03 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4442a787-c80f-3e44-94ba-9928a3218868 | -9.61697 | -67.29209 | 2025-06-03 05:59:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 841e2d1b-a7af-310b-be1d-c116cbc54239 | -9.24019 | -63.28722 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c67fe923-c3a6-3560-aeda-4d1e80fd5aae | -9.62064 | -67.29263 | 2025-06-03 05:59:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2461d1c1-75c0-3e32-9877-fd6f36ce9bec | -9.24184 | -63.28405 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a05cf0f-9dab-3cc2-b14f-8bd820a34550 | -10.01474 | -67.00576 | 2025-06-03 05:59:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cd792f0-e060-3bb0-8b99-641f5dde4154 | -9.67799 | -67.41023 | 2025-06-03 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b9ae81e-f0a2-3a1a-bdd6-694709d62c27 | -9.2405 | -63.2942 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 173ddf0c-083c-3350-b811-f95b6b1b8faa | -9.23878 | -63.29733 | 2025-06-03 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1604eab1-eae5-3c55-bbdb-32b8e1431f57 | -10.01606 | -67.00298 | 2025-06-03 05:59:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 287389df-a41f-34a6-97b5-8daf9d1ddea7 | -9.75731 | -67.32943 | 2025-06-03 05:59:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d41ff6b7-a0f8-318d-aa9c-1beb10b6a614 | -18.8875 | -53.6402 | 2025-06-03 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f6018fff-9530-3931-9272-72eb2ba7750c | -13.1028 | -52.0281 | 2025-06-03 06:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 04f57f8f-c72d-3732-9e18-61661df2dee2 | -18.8679 | -53.6218 | 2025-06-03 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 31ec4597-7378-3660-96bf-4ff5118e70dc | -18.8675 | -53.6434 | 2025-06-03 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 139.1 |
| f35cfa3b-63f2-33c7-bafe-03f83a0c13e3 | -13.72507 | -58.67122 | 2025-06-03 06:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 798c8477-297a-3066-b627-d7474ee4a15b | -13.1028 | -52.0281 | 2025-06-03 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7342b981-cadf-3922-8fca-76d64eb691bb | -18.8679 | -53.6218 | 2025-06-03 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b0d8a98b-5e1f-32a1-a3d1-48a68e5b0901 | -18.8875 | -53.6402 | 2025-06-03 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 51119675-e7cc-361e-8782-5f31512ebf5b | -18.8675 | -53.6434 | 2025-06-03 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 137.9 |
| c1edae8c-8a7e-376a-baee-ce6742267603 | -13.08786 | -52.02917 | 2025-06-03 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| fa74e092-b5a5-30e8-bed0-330cc6628247 | -11.90926 | -54.78521 | 2025-06-03 06:18:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3044c56a-ea8b-32ec-86aa-21c67f70a159 | -11.92324 | -54.81608 | 2025-06-03 06:18:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 85ed9f32-41d2-344f-9c23-af3f8399cde4 | -13.0968 | -52.04456 | 2025-06-03 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cdb5e1e0-eca1-3d5e-80b5-905b217363c8 | -11.89888 | -54.79331 | 2025-06-03 06:18:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 32615c94-bce1-3ea3-bf17-b1d6729383be | -11.90023 | -54.78389 | 2025-06-03 06:18:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 6edf0c5d-63e7-30bc-b02c-b5197d6654e2 | -13.36531 | -54.26051 | 2025-06-03 06:18:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4d84a3ea-f34c-3fc2-ba6c-724f7fc85259 | -8.90325 | -50.04256 | 2025-06-03 06:18:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0c64b241-1dae-350d-9914-15e87a2c9638 | -11.55455 | -56.42327 | 2025-06-03 06:18:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d9f9f59f-7dc6-30e0-bd1a-c2d5313fe951 | -11.5532 | -56.43222 | 2025-06-03 06:18:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fc3176b-98ec-35ee-b088-fbf895b05c1d | -13.08974 | -52.01522 | 2025-06-03 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ff7a6d4f-4043-37b3-9163-22ff8e35ae16 | -10.81935 | -56.94129 | 2025-06-03 06:18:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1c1fadb-4b10-3bdf-9cd1-c3e31eac54d8 | -13.64007 | -52.18286 | 2025-06-03 06:18:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9c6c7c21-2fa4-3778-b3ef-af9493d83f58 | -13.09869 | -52.03059 | 2025-06-03 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 85a7e383-b129-360b-9149-82512fb1dc79 | -18.8875 | -53.6402 | 2025-06-03 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b804491f-f641-3626-b090-08d3cf361124 | -18.8679 | -53.6218 | 2025-06-03 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 5218d6ff-b710-386e-a0e1-4f1f6faf2254 | -18.8675 | -53.6434 | 2025-06-03 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 142.6 |
| a0f91b45-157c-3922-b053-ae634b77d297 | -14.01812 | -55.12247 | 2025-06-03 06:20:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| affe27ec-7721-37c8-800d-da5ddd567617 | -18.87016 | -53.62508 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 2362b1d4-a098-34a2-8f1b-e4fff674b99d | -20.71594 | -56.63117 | 2025-06-03 06:22:00 | AQUA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f30e69de-18da-3100-a5e4-c48e0be3aa4b | -18.8685 | -53.63844 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 179.1 |
| e7e3d719-e855-36c5-8322-53d9a2807fe9 | -20.71736 | -56.62111 | 2025-06-03 06:22:00 | AQUA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67a2c25a-e852-36ae-8beb-497f5e9b4bf1 | -18.8807 | -53.62647 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 19daba0a-0636-3d10-8bbb-45f2fad2d613 | -18.86093 | -53.64542 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1f958a71-b173-3a59-969c-671175d10a1f | -18.86266 | -53.6322 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 497a6383-1bd9-3df1-8490-b39982516a1f | -18.87902 | -53.63987 | 2025-06-03 06:22:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 4ab6af8f-5394-3616-8532-aaff2c9f5f2e | -18.8679 | -53.6218 | 2025-06-03 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 952dbfbb-fa1c-3b36-9593-8f62192b7c24 | -18.8675 | -53.6434 | 2025-06-03 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 3827f658-460b-315c-8e9c-efff37160e88 | -18.8875 | -53.6402 | 2025-06-03 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2e844ea5-f6f9-39c6-99d0-f8758106e748 | -13.1028 | -52.0281 | 2025-06-03 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 99cbda03-c331-3c4f-9473-def1a5ee6188 | -18.8679 | -53.6218 | 2025-06-03 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 28ffca5d-a1b3-30cc-bea9-ab75e874ce35 | -18.8675 | -53.6434 | 2025-06-03 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 896dfa3e-2dc9-3ccd-b66d-e2dd8829be5c | -18.8875 | -53.6402 | 2025-06-03 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b0a6ea09-da48-34a9-bac0-425df71acba7 | -18.8875 | -53.6402 | 2025-06-03 06:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 507eefcf-a266-3d4e-be09-942a02c6ebe2 | -18.8679 | -53.6218 | 2025-06-03 06:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| af122bde-bcfd-32ca-9a0e-3e92e730e755 | -18.8675 | -53.6434 | 2025-06-03 06:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 129.6 |


[Clique aqui para ver as próximas entradas](README17.md)
