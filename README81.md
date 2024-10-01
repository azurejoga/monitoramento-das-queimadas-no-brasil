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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a838e81-ed06-3648-8431-a984c4d36f85 | -10.52301 | -51.08727 | 2024-10-01 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41e7f80a-6df7-3c0b-a556-74d0a6e20bb8 | -10.52218 | -51.09182 | 2024-10-01 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa6ca774-157c-30b0-b59b-7c3dc8ed84b7 | -10.44069 | -50.80817 | 2024-10-01 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 017e34cc-fe0c-3a17-a3c5-b175e4d70257 | -12.27154 | -51.539 | 2024-10-01 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c51c16e3-9d9d-300b-b40f-09bb7efab07d | -13.24748 | -51.23961 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a8ce7db-3158-3e0d-a780-897b174bf56c | -13.24666 | -51.24408 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c95d7338-01aa-375d-a7d2-44e4f2dd131b | -13.24584 | -51.24858 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 238b375b-3f85-3300-a75b-dcbfc768818f | -13.24387 | -51.23425 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 557f5e44-85a8-328b-9d5b-eb19978a6d26 | -13.24305 | -51.23874 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 712fa17b-81bd-35e7-9ad5-49ce6b69fd0f | -13.23862 | -51.23785 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c8471b-f406-3921-8a81-1143bf7333d1 | -13.23583 | -51.22799 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8913a252-e676-3459-a0cf-840ced1206e5 | -13.23501 | -51.23248 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17be3049-8cd8-3cd0-ab15-48869b413954 | -13.23418 | -51.23698 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39d2faa1-6617-3e8f-9e30-6102329915b2 | -13.2314 | -51.22712 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32f96cec-6143-386a-b25c-2bdd8eeda5a3 | -13.23057 | -51.23162 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ace7bcc-448a-39cb-b1ef-8e3b0a7e4a95 | -13.22696 | -51.22625 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf4042cc-c3a3-3137-80d8-532cd01523b2 | -13.22614 | -51.23075 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d10658d-962a-3fbb-b32a-16325e2d49d1 | -13.22253 | -51.2254 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c2f577d-b57a-36d5-90c3-1a932bbdf46e | -13.2181 | -51.22454 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93969832-7c1c-3c67-a6ad-28155fc980ff | -13.04455 | -51.23661 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0b5c98cc-0f65-3f40-8f17-e9daf296b6c6 | -13.04373 | -51.24113 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 88af7fde-d63d-345f-9e2f-20c2a3a67c2b | -13.04092 | -51.23122 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a81595ea-5d91-3802-9d8b-13d71025b5f7 | -13.04009 | -51.23574 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 611b4937-b4da-3ef0-95e1-b1ed21901902 | -13.03927 | -51.24027 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1e62b3e6-5763-3d84-8a9d-277d04d06cc5 | -13.03845 | -51.24479 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d70de242-d348-3edc-9aec-c11943e89774 | -13.03748 | -51.30111 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| c2ca715f-d6b0-3a9e-9c78-36e1f3574a9a | -13.03665 | -51.30568 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 84b59876-9333-3a84-988e-f4245fbb5adc | -13.03564 | -51.23487 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d7c089d4-b3b8-3a31-b967-2f1026e37e46 | -13.03499 | -51.31485 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 25d6b129-68e8-306f-a8fc-1006680ea6e8 | -13.03482 | -51.2394 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 51976081-2ada-35ff-aa2a-2f4d6eac9c8e | -13.034 | -51.24392 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 5dd24e59-7712-3df1-9a38-18b6a4ca04f2 | -13.03317 | -51.24845 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7b3694c9-2ea9-3552-9b1e-5ec47fe711fd | -13.03301 | -51.30024 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| c4f029b5-738b-3183-8287-df5a94238e15 | -13.03235 | -51.25299 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b3c188a-1c66-3a24-ab7b-c1d3e9fd29c6 | -13.03218 | -51.30482 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| b98bfadf-16b4-39f8-b26b-f18b7f54a542 | -13.03135 | -51.3094 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| e9a50c3a-47b6-3714-83b5-3c3ae68c56af | -13.03051 | -51.31398 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ee69bf10-f9aa-346e-b3c5-f2ea94fccd4c | -13.02969 | -51.31855 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a8f06e3d-42da-3710-8e3e-90ed141f03e1 | -13.02955 | -51.24306 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7127c5d3-db2d-3c8a-889b-5a9e40ddfd04 | -13.02872 | -51.2476 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 45e7fed4-c8ab-38e2-a6bf-8cbddc4e5c15 | -13.02854 | -51.29937 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5870f62c-23d8-3c5d-aae7-6fdd88b0dbce | -13.02839 | -51.22411 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ff79d8f7-c096-333f-b789-255d5295df41 | -13.02789 | -51.25212 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 55b07346-f741-3eca-b446-dd126a82a38e | -13.0277 | -51.30395 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 93f26193-7e78-3159-b0a4-bbe0998426d1 | -13.02757 | -51.22863 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4d965e8d-89d4-314c-9a33-a3442447be6e | -13.02707 | -51.25665 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 22466f92-025f-3e38-964a-f07856e15d0f | -13.02687 | -51.30853 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f7a6fc4c-2c47-3875-b41c-1e0fdc53415c | -13.02624 | -51.26119 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c281f9a5-4ec2-3d87-adf7-5f6cd12dd68f | -13.02604 | -51.3131 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 490b24db-dc3b-3624-88ec-024c58361331 | -13.02541 | -51.26574 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b42e9465-85d5-3b4a-b38b-c0e36ab7a5de | -13.02521 | -51.31768 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7bded004-a732-3d0b-ba4e-b3b788691db8 | -13.0249 | -51.29394 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6fecf26a-0382-3b8a-9f9c-10661f0542e1 | -13.02394 | -51.22324 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cf58751d-d78c-36f8-bd64-7570efcb99b6 | -13.02354 | -51.32685 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4c1d710d-ed11-3183-8f6f-2f72380af753 | -13.02344 | -51.25125 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0f65c2a9-3d1e-35c9-9431-bdd531b089c2 | -13.02312 | -51.22776 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a596e098-f624-39ce-a1e4-6d96989aeacd | -13.02261 | -51.25578 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37fd1812-1143-3c6b-a177-9d60709f21c8 | -13.02229 | -51.23228 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3c43ad49-0a4d-31b1-a15e-da3e42c818be | -13.02178 | -51.26033 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 879568d4-6ee7-3ca9-85dc-490e0fee6aec | -13.02147 | -51.2368 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a5c37ddb-c667-352a-8294-89769b466ba9 | -13.02095 | -51.26488 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a218bd8d-0b18-3f96-ba17-1820b72a2b4b | -13.02012 | -51.26941 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 582099ce-0580-38fe-8859-d6268d839cc8 | -13.01981 | -51.24585 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8d553bf-d0f7-34fc-a276-7b7bbdbd33a0 | -12.9872 | -51.27245 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8f3f8e1-27d1-3758-8d71-3d7df2241472 | -12.98668 | -51.22537 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 20e6622d-91aa-3512-9847-db27ea434c10 | -12.98636 | -51.277 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7c44803-6509-3cd7-ad41-5a0caf58e606 | -12.98602 | -51.32904 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| daff1264-ac0c-39ca-b48b-62260c04e91b | -12.98584 | -51.2299 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 5af1c15a-868c-3528-a39b-4f51e063ce1c | -12.98541 | -51.35753 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 300875c6-0fc4-3216-b608-a2cc4db7cfb5 | -12.98517 | -51.33364 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41194cf5-bda7-300c-8cd2-df36a645608f | -12.98501 | -51.23442 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8b03252f-29a7-3e43-94fa-dacccc24edfa | -12.98442 | -51.26249 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28a3c18e-5137-3682-aa8f-98accb7a0f23 | -12.98358 | -51.26703 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 927f3974-874d-361f-84b2-e334c31c8e8b | -12.98262 | -51.34744 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09dc4423-c200-3a46-8123-3a9acc6973ee | -12.98223 | -51.22451 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2aca6ae1-fc73-3f48-b92c-d625c425641c | -12.98165 | -51.25254 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b68344b-e397-3d6a-a543-e23eceb4a6d1 | -12.98139 | -51.22903 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 08b90f69-96e0-39ae-b0e9-45b02333f8aa | -12.9808 | -51.25708 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0b88470e-3633-35bb-9128-1c55b20a3f5e | -12.98055 | -51.23356 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 783c84b1-b089-3ed5-93c1-d221cb462211 | -12.97996 | -51.26162 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 572d8fee-c2b8-3325-8ad0-94d920e4df14 | -12.97971 | -51.23809 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dba9f9d8-8b55-307c-a736-6a6e0d7c1c7c | -12.97912 | -51.26617 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdd64e9d-0a74-385a-ba42-86d893a7612d | -12.97728 | -51.35118 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 128c4b1e-c5e4-3a76-8455-63b143bc9cec | -12.97694 | -51.22816 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5a49b5c3-7429-34ea-b31e-128202923434 | -12.97634 | -51.25621 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b48944d-1828-3b00-a599-21c8b2b3a012 | -12.9761 | -51.23269 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 78ab97cf-d338-3655-a1b4-c08452c10558 | -12.9755 | -51.26076 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1713543-cc48-368a-8d8b-cf3315a6b103 | -12.97535 | -51.33649 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbfe9a2e-2322-30ff-b849-375e7492b6cb | -12.97526 | -51.23722 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 85931e9d-1151-316e-b3dc-ab866895fbf1 | -12.97465 | -51.2653 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29395fc9-f151-37b8-b29c-5cdcfc02f886 | -12.97441 | -51.24175 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 79aa53ef-6f0b-3da8-876c-a583ed37b9cf | -12.97364 | -51.3457 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf8ad192-1060-3b4a-bf72-e9d5e2c7f0b2 | -12.97258 | -51.42709 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2d6b630-e3fb-3c79-8be2-439017674b31 | -12.97188 | -51.25535 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f5f118f-7f6b-3197-846f-3321ee84ff82 | -12.97172 | -51.43176 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ea45a10e-d13d-3c9c-b9f2-9aa332f10562 | -12.97104 | -51.25989 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 719a67f7-d9ab-37af-8e57-6f49ce5e117c | -12.9708 | -51.23635 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| effd2416-e368-33b0-b9b3-3ecb6d4c07c9 | -12.97064 | -51.31181 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85c20694-00f6-33d2-a9f1-bf644d89e1a4 | -12.96996 | -51.24088 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a35a6aeb-d01e-3b52-995d-e6b08e337b90 | -12.96911 | -51.24542 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README82.md)
