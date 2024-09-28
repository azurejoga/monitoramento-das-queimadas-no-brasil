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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e352e43-4fc6-3f47-ba5e-a356393d93f6 | -12.7637 | -62.618698 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19306ce1-c40b-393e-ae00-cc2e6f6199f2 | -12.7661 | -62.628601 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61d4fe6e-4954-338f-a143-5252fbed87c2 | -12.7845 | -62.7481 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf6a629-57c8-3dca-9eea-4a3a1b3db965 | -12.7868 | -62.757801 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78b928e1-c181-307b-8b64-f2c2cce7ab9f | -12.7891 | -62.767502 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0c45b25-6bf8-3bef-9d0e-cafb4ed0ab57 | -12.7914 | -62.7771 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01ab7c53-79d6-35de-9b39-d7785fc7eb82 | -12.7747 | -62.750599 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d661d808-621f-34a0-ab5b-dd29a35b9bb2 | -12.777 | -62.7603 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d11585d-4972-36a1-a291-7980274f2624 | -12.7793 | -62.77 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 376ea9af-f251-3cd8-8941-104f42b3626b | -12.7816 | -62.779598 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70c1056c-d1e1-3d46-85d6-bbb10ee002ec | -12.784 | -62.789299 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 56815348-36d4-337e-bddd-9c5b1a425a73 | -12.7719 | -62.782001 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61d52c5b-7532-30d3-8bff-d24b950ca1c5 | -12.7743 | -62.791698 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77c68c3e-0b32-3fc7-bab5-dd9607de5af5 | -12.7645 | -62.794102 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f086158b-6e95-36b5-ac3d-826763ae9f82 | -12.7668 | -62.803699 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9ec808e-617c-37d3-b1cc-ec02dd1968a2 | -12.7691 | -62.813301 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b68ebb5b-c84f-3551-97aa-cab28cc53988 | -12.7714 | -62.822899 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c64f524-5759-33e1-87ef-72e14c7b6958 | -12.7737 | -62.8325 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69d3e00c-a98a-3f5e-8919-a79bacce6373 | -12.764 | -62.834999 | 2024-09-28 01:54:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5e6d712-f025-3890-bcd7-45dd9e33f7f0 | -12.7663 | -62.844601 | 2024-09-28 01:54:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aeb351cd-44fa-3d07-9d80-ba59a0ba722c | -12.7565 | -62.847 | 2024-09-28 01:54:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 994ea7c5-ae32-3c88-837e-e5533cd20cc3 | -12.0083 | -61.215199 | 2024-09-28 01:54:05 | METOP-B | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bceb8277-f54d-306b-9efe-f479c0411a73 | -10.9066 | -60.852699 | 2024-09-28 01:54:22 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc05684-dbd3-3438-93df-fe0096bd1cff | -11.5859 | -63.700901 | 2024-09-28 01:54:22 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 865b1086-3e8d-3fd7-8649-02bc5b1ee71c | -9.4132 | -63.4202 | 2024-09-28 01:54:56 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 507b48ad-a7a5-3e6b-84bf-867b12823e9c | -9.6647 | -65.729401 | 2024-09-28 01:55:01 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63c43c10-e1c1-3285-828b-3a8a2fdfebbd | -9.6664 | -65.7369 | 2024-09-28 01:55:01 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6b9104-0214-32ed-824f-c2b131f242f1 | -7.5934 | -60.582298 | 2024-09-28 01:55:14 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 529cbfc0-e863-3a56-b1dd-abfe7ca1c5ed | -7.4546 | -60.394001 | 2024-09-28 01:55:16 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca7900c-a614-3c61-a31e-f6d71de03910 | -9.1136 | -67.886299 | 2024-09-28 01:55:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35d2e290-6bc6-34a2-910c-447a7e44bee6 | -9.1038 | -67.888496 | 2024-09-28 01:55:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4e7b60-adc3-3fef-8a12-4237c316aa96 | -6.6698 | -69.945297 | 2024-09-28 01:56:04 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76964457-7821-3a33-8d57-ef7a5635c541 | -6.6567 | -69.933197 | 2024-09-28 01:56:05 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d505c50-981e-339b-b7bc-26757972d41f | -26.26643 | -50.26822 | 2024-09-28 01:58:00 | TERRA_M-M | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| afeade74-77c5-3d3e-b571-b1511c96ad1a | -26.2601 | -50.27705 | 2024-09-28 01:58:00 | TERRA_M-M | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| a47addc4-6a01-3c78-97e8-3079fd60dbee | -22.7019 | -53.23493 | 2024-09-28 02:00:00 | TERRA_M-M | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| 67ac4667-29fc-3228-aa85-16ac41f76c0b | -17.11853 | -56.2246 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 7c8ab4d5-0d3e-3359-93f9-5a490af3ec06 | -17.11666 | -56.21835 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| efb80c00-40d5-3248-a736-d154103310a2 | -17.11497 | -56.20374 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 77bfefad-4877-3987-89b5-6f90a1f0f780 | -17.11295 | -56.19752 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 5144236c-4578-3e3e-a37a-ea7eab225c5d | -17.1114 | -56.18283 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| ce62f8bd-ae5f-3721-98a8-c2ec3df744a8 | -17.10923 | -56.17665 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.5 |
| 533d4b83-49bf-3b16-b762-988245fb75f5 | -17.10569 | -56.22713 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| fc28d517-3338-3513-81bb-1cec259f176e | -17.10382 | -56.22085 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 6d67af54-822d-3899-b754-1b4b7b3866de | -17.10211 | -56.20627 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 6574bf9d-b98b-3205-b17d-fc7ce80531b9 | -17.10008 | -56.20003 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 3f152325-c10e-3fec-be0f-a17a54b78576 | -17.0922 | -56.37825 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 1dfac279-b383-327b-befe-dd33a0d3f94b | -17.06542 | -56.14839 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 54f7fe28-51f0-3c69-9f7a-99bc5ff93ed0 | -17.06173 | -56.12723 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| ef9142d5-3fde-3c15-a6b1-3b37976619bc | -16.9957 | -56.12379 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 6ea13fc4-72d1-3b17-9e77-5beba6928c53 | -16.99315 | -56.11876 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| d1c45158-cecb-3c8e-b9e8-a4170b46a076 | -16.99203 | -56.10248 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| ad3ca5a8-bd8f-34f7-9541-1bfe2e2c0105 | -16.90196 | -57.97594 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| e32c9ec4-7727-3224-8ddb-75fd0dfa57b8 | -16.74559 | -55.82244 | 2024-09-28 02:02:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| c939c5bd-3f4f-38dc-9900-4e17685a5f09 | -16.67389 | -57.45386 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 45c3c58a-a86b-3eeb-99b4-4dfeb3163c8c | -16.48794 | -57.37605 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| e3cfcd1c-b9b6-303a-91e0-2fb087339c62 | -16.4829 | -57.38268 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| f3cd4caf-6cc0-349e-9310-ca579aec9f1c | -16.47604 | -57.37829 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 0ddd24f7-2e16-3dd6-97db-67c36762d365 | -15.84506 | -57.39506 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a2c6cc00-1479-338d-b881-76dd8ab13226 | -15.84079 | -57.40248 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e481e519-e844-323d-98ce-e712d448b3da | -15.83793 | -57.38506 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c391756e-84a1-3158-9f50-3c4364ebc859 | -15.62132 | -57.48955 | 2024-09-28 02:02:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bd42c4e9-58dc-3fa5-af4c-2a07129669f2 | -15.59734 | -57.49412 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7640342a-d3ad-39a3-9720-c6d16bce2a8f | -15.58535 | -57.49648 | 2024-09-28 02:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 72a3faa8-8bde-346f-a83d-3bc78f48e653 | -15.30802 | -58.16773 | 2024-09-28 02:02:00 | TERRA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3faf36ca-a269-355e-a702-2fc561c4fbd3 | -14.89684 | -57.97912 | 2024-09-28 02:02:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| dfd7d595-c450-3929-8aaa-19594ad9036d | -9.96017 | -64.73413 | 2024-09-28 02:04:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3715bda-7b44-3df9-90fb-4855a82a060e | -9.70854 | -60.75766 | 2024-09-28 02:04:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a95c84bd-bdd5-3675-8543-0aad9bf9baa5 | -9.41612 | -63.42763 | 2024-09-28 02:04:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b986193b-8bab-34d0-96e9-62acab7bc3ff | -9.34988 | -63.80092 | 2024-09-28 02:04:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ed3be620-d3d4-3172-9686-5a55d5534059 | -9.24252 | -68.31734 | 2024-09-28 02:04:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e82f3bc4-a5df-32bd-b087-a0a2de9be3d4 | -9.24096 | -68.30519 | 2024-09-28 02:04:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 774ed661-71f7-321f-a61f-68ca5f36cbc3 | -9.23814 | -60.69116 | 2024-09-28 02:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 74aaa930-581c-3d63-8724-44fe5cfae422 | -9.2362 | -60.6782 | 2024-09-28 02:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3e6e6722-55b7-3ab0-accc-fab6c5a20f5a | -9.23515 | -60.49624 | 2024-09-28 02:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0527a821-e0fc-3f68-a896-47133ff7e20a | -9.20825 | -59.80924 | 2024-09-28 02:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9314dd5c-f96b-3537-9297-b8bc282e12ff | -9.1528 | -58.89092 | 2024-09-28 02:04:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 01fdfe13-15f9-32aa-a94c-57e240aca76c | -9.14933 | -58.89725 | 2024-09-28 02:04:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ec47df3e-99fb-3c26-99b4-0ad7f94ff24e | -9.08743 | -61.12744 | 2024-09-28 02:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b88fb674-4937-3651-9a94-5627108da7dc | -8.67617 | -58.21835 | 2024-09-28 02:04:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 171b99c7-fae7-36fb-b941-d5289c7e8523 | -8.10708 | -58.03982 | 2024-09-28 02:04:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| bf8d551c-6c5d-37d7-8f14-0f85ba7f00af | -8.09816 | -58.04686 | 2024-09-28 02:04:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8d1b3f49-6cf4-3d5e-86b6-50637e64621b | -7.6026 | -60.59624 | 2024-09-28 02:04:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 297c764f-3277-3963-801e-cc05721651c3 | -7.60046 | -60.58224 | 2024-09-28 02:04:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ca9e6d9c-2654-38cb-963f-6334e33b9998 | -7.46964 | -60.40389 | 2024-09-28 02:04:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c6c9fcf5-b25e-3b30-8374-51d3c2bc5d5b | -6.66701 | -69.95639 | 2024-09-28 02:04:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1eaafcac-cd24-3f6e-abe8-2d530e276970 | -6.66506 | -69.94187 | 2024-09-28 02:04:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b86b572f-b865-31a4-9f7a-5d585e50d147 | -13.69569 | -60.70475 | 2024-09-28 02:04:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a04309a2-c98f-34d3-8c04-2da5dcb5c781 | -13.48979 | -57.26505 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d23f0adf-1d78-3a39-9af6-d0547ee73b97 | -13.48901 | -57.25955 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 377ce311-4d05-3825-8ff6-6cd57232582c | -13.48648 | -57.24496 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 43cc2209-fdb0-3e8e-9087-f7b6489d05b8 | -12.8599 | -62.76084 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e2950eac-63b3-38e9-a577-f13a4883c0bc | -12.85855 | -62.75146 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 20eedd9a-6664-31f3-83f8-3d0bae1e55c4 | -12.85721 | -62.74209 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8bb3546c-8587-388b-920a-e2e0081fb370 | -12.84685 | -62.73409 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dbb993fc-cdda-3f25-a416-81c6956c52af | -12.82928 | -62.80379 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90eb6a7d-2697-3ba9-96c7-c1a1f331f149 | -12.82163 | -62.81451 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eefbe017-9617-344b-87fe-16c36d9f2798 | -12.82028 | -62.80517 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 826b9c8b-19e9-3203-9a13-8affb5e5a67e | -12.7955 | -62.76115 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9b9a8126-4636-3a9f-b3c3-e5a5a55d0052 | -12.79414 | -62.75178 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README25.md)
