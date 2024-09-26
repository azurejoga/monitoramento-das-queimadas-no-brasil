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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ede19214-db42-36e0-81e1-fbb0d159f3fc | -14.96487 | -53.62006 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f45028c-dc49-3a57-9495-f0c66a5bdb3c | -14.78653 | -53.86347 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cb55354-f5ee-3dc9-a506-6f82248f6458 | -14.7831 | -53.88651 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a53503f9-4a24-3053-beaf-fc2943feab9f | -14.78309 | -53.86288 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20e1bb44-9c70-3f2a-8163-279e2dda9d9a | -14.78252 | -53.86673 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ab816cf-b8be-3046-ab9c-66d0c4fa8119 | -14.78195 | -53.87057 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efde1a8f-deac-3b70-b607-04d21b67fbdc | -14.78137 | -53.87442 | 2024-09-26 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adc64f20-136a-3dfb-b5dc-7a271b208550 | -14.52023 | -53.06662 | 2024-09-26 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef2bd6e2-623f-3930-866f-80fbf7aaaf8e | -13.80102 | -53.84537 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a808fd01-32e6-39ea-83d9-a5b572421e74 | -16.09236 | -53.57092 | 2024-09-26 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b797d7b-9b44-30d6-aeff-3373ddac252f | -15.58928 | -54.30698 | 2024-09-26 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 674be8be-e138-3b90-aa74-673050bb7afa | -15.23136 | -53.79271 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a29fab48-eea6-36e6-b036-1636574fb2e8 | -15.22789 | -53.79218 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92b18152-19fe-3d7f-a78a-c265061eedf0 | -10.38951 | -53.71152 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9382db3b-cdad-38d1-afa8-3220e734e52b | -10.38793 | -53.74453 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18d89a40-b2cd-31e3-a787-667d7093c80a | -10.38781 | -53.70013 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adc15d3e-b411-3b0f-8d0a-d4eb199017d2 | -10.38567 | -53.7368 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a04347-e028-3850-a61d-056f0856d7c3 | -10.38561 | -53.71461 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e373429-75d1-39d4-9acc-aba83861bf2d | -10.38512 | -53.7404 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99c1a327-7334-33e9-aa0d-b5b55d50be91 | -10.385 | -53.69597 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd25d9c9-a89b-3506-b02d-d0b2de81eac0 | -10.38445 | -53.6996 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a083e5-7ba0-3429-ae81-9caa2b6416d2 | -10.37458 | -53.76459 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27705b6a-c174-32ac-bc69-cba8987cad04 | -10.37403 | -53.7682 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56a872f2-2919-3bcc-95c2-ee12a1e61cef | -10.37349 | -53.7718 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01cb1e32-62c7-365e-a4f6-a1ef67755751 | -10.37294 | -53.77541 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cb02dde-ecb1-35ac-8b87-575979ea7880 | -10.37164 | -53.71608 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5d5e199-072d-30f2-b11e-d347a96635d6 | -10.37123 | -53.76406 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c45c7140-57f4-38dd-95ac-b7172b5a47bd | -10.37068 | -53.76767 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c92ee2a8-ded4-3088-8607-3b8cbfda2b05 | -10.37013 | -53.77128 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c709cd76-7a60-3433-9ad1-7dd4caf6e9e6 | -10.36959 | -53.77488 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fee524f8-c01f-3259-9015-a07406443579 | -10.36904 | -53.77848 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a6d1a31-eb54-3493-ba57-e85424aadd9a | -10.36624 | -53.77435 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ecd9ca84-ffeb-3063-98e9-5993eeefd872 | -10.36569 | -53.77795 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5edd6f72-a6ca-3d8f-97f3-01b102411d94 | -10.36514 | -53.78154 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 465116ad-4a5a-3031-ad2d-458ef60c5024 | -10.36289 | -53.77382 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b80ae748-9dc6-3307-84c5-3a40722f41ce | -10.36234 | -53.77741 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c3624db-c668-3cfc-806d-bb415a97e74b | -10.36179 | -53.78101 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc54791b-769c-3287-95b1-512cd2e00013 | -10.35954 | -53.77328 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16422422-ba29-3021-bb6a-3e21b7126aec | -10.35899 | -53.77688 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 121419ee-ca6f-3542-9976-48618440c931 | -10.35845 | -53.78048 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62e94c60-1cf8-3d74-8008-02292b840ffe | -10.35782 | -53.76195 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8019f54d-1b67-3839-9bb6-dfb69c1fa25c | -10.35549 | -53.73204 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a2a21cb-4c3f-3353-bf98-4525cfb78e5b | -10.35494 | -53.73565 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb9dd47b-9bcf-3b42-a0e5-84f40871b6e1 | -10.35447 | -53.76143 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8ed98d-79f0-31ad-9492-b0f1ea69837e | -10.35393 | -53.76503 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 564d4989-66fb-37aa-8a03-4b7f509ae467 | -10.35338 | -53.76862 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 917fb831-3947-3367-9d0c-3a69e5585cad | -10.35311 | -53.73214 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a43a7917-22b0-3701-94cc-141ccde0fc9b | -10.35031 | -53.72801 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 060bc30f-4706-389c-a494-78e78400c639 | -10.35003 | -53.76811 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04cfe5c7-63f2-3cc3-8202-07aa2bbd3f23 | -10.26445 | -53.99701 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 299bf0ec-9899-3aad-aaea-0c2f87856749 | -10.2442 | -54.10645 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a57f1c71-ab1b-3d2c-baae-0d0ef63b972f | -10.24366 | -54.10999 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ab93bf0-e3e5-3554-9de9-1470381e8c9d | -10.23973 | -54.09126 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 388ba7b0-bc30-3e41-8d12-90b6b9bf4f5a | -10.23918 | -54.0948 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f67b47da-be63-3193-8f61-a47fd33583fc | -10.2347 | -54.07962 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc3d7bf0-8279-30da-a88f-8d57f7a59d4a | -10.23416 | -54.08317 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 196682b4-f4f5-3390-beed-ba8efde015ab | -10.22872 | -54.11855 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dbb8359-0754-3aa2-90e4-110cedfa4e58 | -10.22817 | -54.12209 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3dbb0f7-7724-3bdc-8378-0438936f4d1b | -10.2275 | -54.08216 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52c76bdf-eebd-39e1-a3a5-793f37315959 | -10.22594 | -54.11449 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee7e08d7-1c8d-30b9-9d4c-087b8b2b2919 | -10.22539 | -54.11802 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e944d79-3ffe-3618-909d-cc3ad296cfc0 | -10.22472 | -54.0781 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 681f6503-5c47-33b5-bdcf-39f3b1891303 | -10.22261 | -54.11397 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3865ffd6-617a-359e-9927-cd5d4e1cbec2 | -10.21202 | -54.09423 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9b13ee-1323-36ba-9307-093f2f9d3c49 | -10.21148 | -54.09777 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d389576c-0633-3591-95d6-5e6d6eefc6ac | -10.21093 | -54.10131 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01431c54-63c0-3d97-98e6-24349920d5a2 | -10.20815 | -54.09724 | 2024-09-26 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 510327c8-002c-3433-94e4-2a247bf72ea4 | -10.42975 | -53.69562 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cc657f2-c7a9-3ebe-bee3-92e69982c057 | -10.42584 | -53.69871 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eec462a-fe52-38b8-a831-3b60d6f52dc2 | -10.42248 | -53.69817 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e2a3fa-17b5-3689-90c4-8147437e32c9 | -10.42193 | -53.7018 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b79aba42-6e5d-3786-bb8c-cb2b3af41f96 | -10.42137 | -53.70541 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccce9cee-b205-3595-b0e8-6a089841bbba | -10.41912 | -53.69764 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68901672-1f38-34bb-80d5-13ff4547fc8d | -10.41857 | -53.70127 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 56f314e5-46e8-368b-b010-d22094432a60 | -10.41576 | -53.69711 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46d4dd7b-ab1a-31b7-8bbd-d5362cfbf92a | -10.41241 | -53.69659 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598663d0-21ef-3bbd-8b6e-cf8c2e016ff6 | -10.40905 | -53.69606 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02eee352-870e-3d8d-94e8-0007a0cc32c6 | -10.40569 | -53.69552 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c5b9f6-69e1-30f0-8bb8-3331c74bac2b | -10.40404 | -53.70637 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42f7c910-24ce-3bac-9dfa-9d05724f8a37 | -10.40349 | -53.70998 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84f2e428-488c-3bc7-935b-280b50ed7e82 | -10.40068 | -53.70585 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a30ec1-868e-3034-99b2-92ff4c4d601c | -10.40013 | -53.70947 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b46cf0a-7eed-350f-b89f-1c015b0f2494 | -9.85554 | -54.53046 | 2024-09-26 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96609131-65a1-39df-89a7-243699fc3419 | -10.60187 | -54.23521 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8057a067-6e1c-3c89-be71-a0a6a57cb5d9 | -10.59855 | -54.23468 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee652d9-7f97-3845-8670-5faa923be7c0 | -10.58471 | -54.23613 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ee0fe99-b254-323e-ab7f-2e10fdac00b3 | -10.58416 | -54.23967 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89a094ba-5745-3eb6-8cdb-a69a2706c206 | -10.58361 | -54.24321 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ce33236-94be-30ba-a42a-bfd6919c5b3e | -10.58084 | -54.23916 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef66664-4acc-3b74-a6cb-85c654fa1d28 | -10.4685 | -54.21754 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5f239ca-3bd2-3b6e-8095-aa30d74de693 | -10.46573 | -54.21349 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec2d3078-1fe4-31e7-8a14-c3fc9cdbfed6 | -10.46463 | -54.22057 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e5bfe6d-d273-34a8-a884-80b1c2a20dde | -10.46131 | -54.22005 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8cf0641-ebf0-31d2-b747-beaf927518e9 | -10.40136 | -54.34421 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa123d55-c1ec-3f40-8815-609e2b607f04 | -11.6734 | -54.45116 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a73556fd-fe1f-3039-b53a-d04bcb2051ee | -11.67286 | -54.45472 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58908097-5148-3e02-9df3-9d1c318d6767 | -11.67062 | -54.44708 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566d9efa-691e-3a80-9d59-9df7b5d0d4cd | -11.67007 | -54.45063 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a730a71-6240-3f2a-b21f-d0463549e97a | -11.50841 | -54.6394 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6656e1d1-0236-3655-926c-7a494048194c | -11.46655 | -54.44793 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README127.md)
