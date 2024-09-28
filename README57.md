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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd63b0f9-250b-3555-84a8-2c2da2c8ac29 | -8.71407 | -54.81111 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7de12e4-0ccb-3207-81e8-f3341c357cfa | -8.70845 | -54.811 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87610c0f-30ff-3db5-8463-39e4fbe095bb | -8.61259 | -54.57968 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32e32673-7a6f-33f8-a01a-e59bb7f818d5 | -8.60935 | -54.58114 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3c39480-bf07-3146-b464-ab3ede706965 | -8.60722 | -54.5787 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a9b51a-695c-36bf-a7ee-f4fae48df7a9 | -8.60658 | -54.58224 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9884b79-26ac-3d94-843d-b3d3648e50b5 | -8.55938 | -54.5669 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e258d6c2-9e2e-34b0-8d61-f0f2f11d814b | -8.55399 | -54.566 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a07004a4-7910-34fb-95d1-3b9d724bf2b5 | -8.55336 | -54.56942 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c786b6-5aa4-3d8c-a186-63858ff3fbdb | -8.54136 | -54.57422 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c1c8b1-7c43-36a0-9534-cb65d3dc92dc | -8.53597 | -54.57332 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aa0044a-0587-3e80-bf83-ab4abb4e8424 | -8.53535 | -54.57669 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 530e4ebe-f17e-315a-9ea9-857f25a75ca6 | -8.53472 | -54.5801 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d78930f-776e-3a00-a73e-bbfee3b27239 | -8.51417 | -54.69147 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d683a6-b94a-3078-b6a1-71c63f664d6a | -8.51352 | -54.69502 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3edf72f-a087-3fa4-83a9-abe910e40ea1 | -8.5081 | -54.69402 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 610f7da9-6e6f-3a02-97a0-e3ad2f0b6807 | -8.42179 | -54.69688 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d8b61e6-973c-309d-9c8b-5b1fed654638 | -8.41979 | -54.70776 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c02fecf8-80ec-3358-95fc-a788c1d84752 | -8.41568 | -54.69954 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8c0b733-3711-37c8-bc5c-7af0c25b9259 | -9.65083 | -53.5923 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30b24d4d-6a35-3354-a549-04c4e06bde17 | -9.64902 | -53.59611 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad5a0e8e-d167-3d5d-9787-90a8f86d2fcb | -9.64588 | -53.5914 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91db9ab2-7e6a-3797-afc0-962536a16b7c | -9.6451 | -53.58947 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a657e8fe-a577-3e65-9e5b-cb755f6cf6f7 | -10.92823 | -54.25743 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9276e14d-b694-347a-a406-693af6f8bf16 | -9.64408 | -53.5952 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97dcf143-011b-36c9-ae1c-f10451913e5f | -9.64201 | -53.58479 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 304d8d9c-67cf-39e2-8c78-d62b12484ce3 | -9.64094 | -53.5905 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aeb0d5e8-c788-3487-b40d-e691db549f7e | -9.64016 | -53.58855 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b25ef35d-b0ec-35f0-8836-2a139520b1c4 | -9.63913 | -53.59431 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5080cf8-0867-313e-835d-fb9c0edcffb0 | -9.63522 | -53.58766 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d1f7a60-35ca-37a6-8c44-989bdd0fd5ff | -11.62416 | -54.57214 | 2024-09-28 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76d537cb-f4df-3208-99da-c99c578e7ee1 | -11.61908 | -54.5711 | 2024-09-28 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eebbdcc-b694-3a0f-8f58-cbf2b4739459 | -11.28114 | -54.16432 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc0806f-27ad-34cf-89b7-99b8e1618925 | -11.21405 | -54.76617 | 2024-09-28 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c1044f8-ce82-3c9b-b6c9-9e58ac1ee7f2 | -11.18329 | -53.9109 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08488796-5d50-3a62-a70f-b65a0b581304 | -11.1794 | -53.90442 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bba2e33e-3458-3b26-b102-469599d8d2bd | -10.93888 | -54.25634 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 163141a1-3e0a-3c54-ac53-2cc396beb22d | -10.93834 | -54.2593 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70ebf775-44a2-3615-81ed-6e4c01afe6ba | -10.93779 | -54.26227 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86f46b5e-e0b0-3c70-ad09-8548d05b7679 | -10.93775 | -54.25589 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6c0df993-511e-32df-8fb0-0a17de161329 | -10.93719 | -54.25885 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 43b79dae-846d-302a-9a9e-8b5654dc1631 | -10.93662 | -54.26182 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0018aacd-2665-31f3-8ab7-d9f5fcda3180 | -10.93605 | -54.26481 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7be454f4-e2d0-3379-b090-66f86f407ffd | -10.93491 | -54.24946 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0dc60bb1-d39c-3b10-a0c6-342008ac454c | -10.93437 | -54.25242 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c4cf9c6-3d01-3128-b878-9133f2d43365 | -10.93383 | -54.25539 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e99e58e6-ba0b-373a-a2c3-8616f02ebce4 | -10.93328 | -54.25835 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ec10d968-197e-346a-8658-cb7dd0ff46f4 | -10.93274 | -54.26133 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e8cff9a-3bfa-3b8e-8b1a-283211f1104b | -10.93219 | -54.26431 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04b1c480-a424-30b2-9d97-b1d09b4cff68 | -10.92932 | -54.25149 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 291ad984-2b38-3e67-ba81-7942b86ebe06 | -10.92877 | -54.25446 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3aaea09-f209-3191-9192-b2403b7a7b14 | -10.92768 | -54.26042 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23bc733e-391b-3892-b838-6d2b1e778fd9 | -10.92713 | -54.2634 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31a18264-facd-354a-bf9f-2471e5afbac9 | -10.92372 | -54.25349 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59a6fe03-ec9f-3964-8b18-cffce74fccb6 | -10.92317 | -54.25649 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d53e994-84a3-36d3-b304-617f246b73df | -10.92262 | -54.25951 | 2024-09-28 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baa76f47-8bb8-3d20-be80-9248ebc4c6c0 | -12.66777 | -54.6561 | 2024-09-28 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1acb385f-d398-3307-82b9-1bcf876df156 | -12.66721 | -54.65902 | 2024-09-28 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9484e3b8-7310-377c-9af4-299065ebc367 | -12.66665 | -54.66195 | 2024-09-28 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4973eba4-78d2-342a-8580-eced459c4a9f | -13.97623 | -54.5824 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbf8545e-611d-3d69-879c-c4063806f9cc | -13.97406 | -54.59367 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28b474f7-0dd6-34ed-b353-12c1b2208a52 | -13.97025 | -54.5871 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbde8045-96c4-3e89-8673-8b4cfcb71f1f | -14.75564 | -55.32069 | 2024-09-28 04:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a5dbbe5-cd8e-3be9-bf2a-d2ee8c2ca40e | -16.99951 | -56.12135 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bdfdfc49-fdbc-3cf1-87bf-ef405ad1e339 | -16.99925 | -56.13668 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5f6f919f-88e0-3dcb-b698-26fc06ad6877 | -16.99821 | -56.12766 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2ea6fb30-aac5-36fe-87f8-011837b6a5cf | -16.99793 | -56.11658 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bc535008-948e-37f2-940a-fb97e39e13c1 | -16.99755 | -56.13082 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0cd663a7-6c23-3673-96e7-ba20b2f9f6fa | -16.9973 | -56.11974 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bd168757-e848-3172-a36c-37277edfdee8 | -16.9969 | -56.13398 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 864f8b6b-3c85-3572-bad4-185110622c86 | -16.99662 | -56.09652 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec81412c-0bfe-3b8d-b10b-dec8df0ae3ce | -16.99624 | -56.13715 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e056d030-2f91-32f8-b65a-357484acdcf2 | -16.99604 | -56.12606 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5feb2475-5fe8-394e-a66f-69e82d6eefa0 | -16.99572 | -56.11395 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ea1848e3-78a1-3eda-a73f-ff3f0eb33812 | -16.99541 | -56.12922 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 773363ba-2e4f-305c-9d00-4f80a1647bef | -16.99507 | -56.11709 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 72670595-ff98-30ef-a8bb-bf56f4df7f1a | -16.99478 | -56.13239 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3e9c1e7b-d42a-3d19-88f1-41a22fe10894 | -16.99454 | -56.09396 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 16302cf2-aefe-3c31-b140-2928f728d3c9 | -16.99415 | -56.13558 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4bcd99a7-e32f-3d15-80b6-bc212869c405 | -16.99347 | -56.1123 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3c738e74-42c6-376c-8bdd-15af8af4e9bb | -16.99284 | -56.11547 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a4ffa0cc-3ac7-33fa-a026-f8497fdbc687 | -16.99221 | -56.11863 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1db7e59a-6a07-3c41-a549-a0f74112fdfe | -16.99216 | -56.09226 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 193dc9e2-5967-3d6b-a0cc-cb1f23ab6719 | -16.9918 | -56.13287 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 625fcf9d-19a4-3975-8e76-01c605ce138a | -16.99153 | -56.09541 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 79bb49ee-c872-3aa2-b8c6-a014c2b37ef2 | -16.99128 | -56.1097 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9a636288-69ff-3869-8b5f-2069e87741cd | -16.99063 | -56.11284 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b8b88516-a2cb-3c12-aa05-43fe9e127918 | -16.98997 | -56.11599 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 25416772-d7a0-3277-a2da-0f298d08ab6d | -16.98838 | -56.11119 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b9e54988-8c96-3d6b-b640-8828726def76 | -16.98775 | -56.11435 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 810cac41-b8d9-3834-8a58-25aaa635d6ab | -16.98711 | -56.11752 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| feafc270-c82b-3af7-96bd-3c544e392512 | -16.98645 | -56.0943 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ddd5c92f-0086-3be8-b7da-621e02af0f2c | -16.98455 | -56.10377 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8eba3867-48e3-3c4e-b575-21bd6f07a778 | -16.98392 | -56.10692 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 8cc6f5a9-06f3-3920-8bfc-07b40c18254d | -16.98329 | -56.11007 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 07ccdba8-2b6b-32ab-953b-587ff5a88be6 | -16.98265 | -56.11324 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 514de48c-8333-3d49-aac6-d8ed12bec3e0 | -16.97819 | -56.10896 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| e05ead4e-d9de-32b6-b38b-488e65f3141f | -16.97756 | -56.11213 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 09d9145e-2a32-35d3-a29e-6eb1cf53f40b | -16.71748 | -55.91099 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0bca1803-879b-373a-86fb-0dc37c44be9e | -16.71628 | -55.90831 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README58.md)
