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
| 185db0a1-25c9-3fc5-95e7-91ad7747a76d | -2.46234 | -50.41591 | 2024-10-28 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a4564ce8-4a38-3b9c-bc02-ed08c85a3ccb | -2.45592 | -48.50621 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2bad2100-26e1-3194-a137-0d15183f9fd5 | -2.45221 | -48.47947 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1f75eb5-1fea-372d-9ae0-70f822e8bc69 | -2.44379 | -46.90104 | 2024-10-28 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f06f051-61c0-30fb-acd3-a1e214f8fa3a | -2.43615 | -49.16282 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa2d8e50-ad78-3788-b78b-0c3761886263 | -2.42941 | -46.20528 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7ea90f9-7c15-3173-a025-d3fb2d2cd8be | -2.42686 | -49.22733 | 2024-10-28 00:52:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f3833c74-33a5-327a-8c33-9e08913cb605 | -2.41414 | -50.42262 | 2024-10-28 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 80acc549-ac98-35ea-b727-6512c95a98f3 | -2.40965 | -46.72199 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2ac9d3f8-1be5-3aba-a647-ab133acf25d8 | -2.40838 | -46.71293 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9af47100-85d2-3c28-a86f-50c0039ff231 | -2.40711 | -46.70387 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ff73a8d5-03a4-3228-8a8a-a8305f409b96 | -2.40694 | -48.55539 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0a62b7ac-1b7d-39b0-a1d3-bdf9d557d287 | -2.40569 | -48.54645 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| fc6c22b4-2b48-37a7-a056-e6258dec1281 | -2.40445 | -48.53753 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c7f213c7-e429-3e37-b399-0f51afeba7cf | -2.40069 | -46.72327 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 88cc05ae-1764-33e5-b11f-a95ec7e19cb2 | -2.39838 | -49.02397 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 037468ec-c9e9-399b-acdc-24b19a0e7a5c | -2.39679 | -48.5477 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 47c6cc57-f00a-3325-9cea-830f7e028abf | -2.39555 | -48.53878 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a6eeb460-b651-335a-8547-44b93dec83e6 | -2.379 | -48.55021 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 0ddbd29a-ad3f-3271-9557-4a09dc310db0 | -2.37776 | -48.54128 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 8c1e4223-8027-3aed-a97d-4118cd8177ae | -2.37134 | -49.02775 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4317c8e-669e-327e-81a4-aa7ce6672d82 | -2.36715 | -47.67325 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4e9aef64-1448-37f1-9058-f55834f04885 | -2.36593 | -47.66447 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 32386ae4-31fd-3a1d-8b52-4ee2cc9571b9 | -2.36481 | -46.53313 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0a46e595-72c7-31bb-876a-41be464161ec | -2.35862 | -48.9363 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4589d4d7-6fc5-3411-9925-73ec433be662 | -2.35547 | -46.20288 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ccf5b8e-dbee-39e7-8722-39a9c871c9da | -2.35282 | -48.42677 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a2cbda35-c24a-39dc-9b36-ef4377e5d957 | -2.3467 | -49.11562 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 869b3f3a-7f7e-36ca-9c15-02a573ed53f4 | -2.3464 | -48.44579 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9ce0722-025f-3fae-99d3-301b0789872c | -2.34635 | -46.20419 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebc92d8c-ce46-3daa-913f-1f93c23372e4 | -2.34543 | -49.1064 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 869c149d-2cd4-3952-8432-da34c74cd74e | -2.33629 | -48.43816 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d26cdd77-a5c9-32dd-bef4-00d01bfae3ba | -2.33513 | -48.57173 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0231f018-f525-3d9c-9abb-c5b6b2f2c060 | -2.33485 | -46.32047 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8f461ce4-5e15-33aa-9e59-108d3e704568 | -2.32538 | -46.64725 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6593b992-a399-3a0f-b2bb-808364d75521 | -2.32411 | -46.63814 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d1dd7ef-c575-3090-b1fa-15667dd519af | -2.32283 | -46.62901 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2f106056-7acb-32aa-ab6a-f9b7720e602e | -2.32043 | -46.47972 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3635413f-82d1-3cf9-b2eb-da9123cf4e2e | -2.31915 | -46.47049 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c82e938-05bc-381b-94c9-7731db616e59 | -2.31894 | -46.66673 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db2094d5-c81c-3223-9bae-333710815aae | -2.31396 | -46.49942 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ad34d4b-f12f-3f69-a332-c511e3fc3e9c | -2.30996 | -46.668 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 325ea5db-4a41-33f6-b691-cc1a174c8520 | -2.30869 | -46.65891 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 45570f7e-a576-35fc-8dac-fe2789469dcc | -2.29971 | -46.66018 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8e88cc28-9acc-3dbd-9c6a-cccb66141a7f | -2.29647 | -46.11483 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f90d2ccd-2212-3d24-8bb3-348bffb7f9ed | -2.29454 | -46.75352 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 10d1a999-7f71-3d43-9577-63e10f7c4e00 | -2.28945 | -46.65237 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 86cec23b-898c-3f39-89bc-8016ab7c7636 | -2.28817 | -46.64326 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bf2e25cc-85b4-3de4-8efc-aa3354d45f0d | -2.28686 | -46.76383 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1c9c5041-f5ad-3baa-b65f-70a10f2c80b9 | -2.28664 | -53.80345 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5ded1a81-751a-3446-ab51-c986d61c0542 | -2.28559 | -46.7548 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d3d828aa-6669-35f5-b0dc-00179a213e24 | -2.28431 | -46.74574 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08b52248-73f0-3317-be5c-a05bac7cf135 | -2.28411 | -53.78505 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 785b9b88-6fe5-361f-993a-80c9401170b2 | -2.28158 | -53.76676 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 324f9765-9440-32eb-b679-51b7571b41fa | -2.27919 | -46.64453 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e052ccac-c573-384b-b0f2-8fdc7bd7e6a1 | -2.27816 | -46.11747 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 25cc1b72-342a-3990-bda5-327e4c247313 | -2.27423 | -53.80533 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1b4d0bb5-34c3-3e89-a4e8-129a2448ec7c | -2.2717 | -53.78685 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 495.4 |
| fecc2fa5-c79d-379e-9b2b-8290f266cbc1 | -2.26918 | -53.76844 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0602b8fe-a331-3d8d-9c81-cb5f24765285 | -2.2689 | -46.77272 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2eaf9e95-9630-36ef-be79-5b5b460d67c9 | -2.26765 | -46.76368 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6916bd39-455d-3031-917a-a052d6c91e46 | -2.26211 | -46.26035 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 666133d1-3fbb-3b25-a98b-d57827925518 | -2.25932 | -53.78883 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3ac3fff4-85ef-3445-82ee-c473c973d929 | -2.253 | -46.26166 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 13e97e71-cbfd-37aa-a1d7-4a04d0e26a28 | -2.25169 | -46.25228 | 2024-10-28 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 19e2a453-7d12-34c8-af73-bed649d6fc7c | -2.22541 | -46.78809 | 2024-10-28 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae4d9fcd-7719-30e5-a773-21430488c375 | -2.21172 | -50.3198 | 2024-10-28 00:52:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae595ecd-f37b-3a62-aac4-9e1ec6112e16 | -2.18864 | -48.84256 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7778bb80-c96f-318d-8e48-59fc94fb4173 | -2.1759 | -48.81671 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1bc5549-d7ae-3b0d-ad2d-23f832ff5afa | -2.12807 | -48.99925 | 2024-10-28 00:52:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5a1c73b5-f67c-36fa-8065-a722b65d44f6 | -2.06037 | -52.1656 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d49d92e8-b221-3cbd-973f-72e1a499ffda | -2.05182 | -46.53645 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0bb254d7-602b-37e6-bd33-17b1089d9744 | -2.05097 | -52.09769 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4b4e41c1-650d-36bb-b26a-c1e8936e1c8a | -2.04953 | -52.16709 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 36e4be02-f566-3391-80c9-943f72632534 | -2.0491 | -52.08418 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b8ac9028-c1ca-3be2-8ca1-ff3583dbc068 | -2.04725 | -52.07077 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e4473229-bec8-34e4-a1d3-a92da47392ce | -2.03887 | -46.31394 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ee416c42-78f2-32eb-9ced-1bbef56dc5d6 | -2.03833 | -52.08573 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d499765b-d4a9-3737-b242-d8fa65fdb0e6 | -2.02976 | -46.31523 | 2024-10-28 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 304dfef2-ef28-3d39-811b-655c511bb963 | -1.97703 | -48.4406 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d4feb0f-956e-3680-a160-de8c440c2ed8 | -1.9758 | -48.43172 | 2024-10-28 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1b00996e-c753-33a7-be53-b55c831d3913 | -1.9639 | -47.95737 | 2024-10-28 00:52:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 41d4c91f-dbe9-3f2a-893f-93dd7a64a905 | -1.96267 | -47.94859 | 2024-10-28 00:52:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb9b08bc-f073-3fd0-9418-fa52ea8a0382 | -1.94896 | -47.91472 | 2024-10-28 00:52:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 747b6808-bd64-36cb-b2eb-2f06db45ddde | -1.78411 | -47.8458 | 2024-10-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| afd34c0f-8c35-3f94-b92a-bc26d718f6fe | -1.78289 | -47.83702 | 2024-10-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5518ccdd-c789-38b3-8623-d728c3aca1b8 | -1.76465 | -54.00613 | 2024-10-28 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| af37baa6-1294-37d1-82e4-bcfa67e66ed3 | -1.73393 | -55.00505 | 2024-10-28 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 02d0e1dc-0b17-3984-aa24-b7c014d249d3 | -1.60225 | -52.5003 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d64b3c7d-1d63-3f49-8094-a552fb03fd71 | -1.60138 | -52.5068 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8e18bb3b-aa7c-347c-93f5-bb7912b01ce8 | -1.59935 | -52.49262 | 2024-10-28 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 89cfda52-4e04-3933-925c-d5d2bfde4656 | -1.5643 | -54.44722 | 2024-10-28 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a1a09b69-895b-3955-b84e-eed372990057 | -1.55016 | -52.11565 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5d0c32ee-873c-32bf-9483-670c7f488539 | -1.54836 | -52.10239 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 1268da43-1d40-36b4-b2d1-b266d343dd25 | -1.54656 | -52.08914 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f591cd5d-a548-39df-b955-215622d10564 | -1.54277 | -52.0961 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7a184fc4-bf51-36d5-b32a-691a3dfe62ab | -1.54089 | -52.0829 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8879cbe6-54b6-38f2-8998-1c6387fe0444 | -1.53587 | -52.09064 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 898886b9-4639-3dcf-a09c-0b9d51b1818c | -1.53409 | -52.07742 | 2024-10-28 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9be69e2f-2c5c-337b-9451-da0e30ee27a4 | -1.52888 | -47.21019 | 2024-10-28 00:52:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README17.md)
