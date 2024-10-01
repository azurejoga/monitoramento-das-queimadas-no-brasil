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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f10e2b21-b04c-38a9-94f1-d78de28432a1 | -16.85128 | -55.94446 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42ac8db9-0271-30e5-acde-5972b4b4be8b | -16.85127 | -55.89976 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4073e805-79f8-328f-b2ff-d7b1ff9696a0 | -16.85094 | -57.69486 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b0d30054-81a2-3602-a080-1a1eba891168 | -16.85092 | -55.90282 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0cb9307f-7f2d-3b4b-a81b-1965410fed4d | -16.85057 | -55.90587 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ffa2c986-44b2-3537-90b0-abfe53b6f679 | -16.85022 | -55.9089 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4272f9df-b95c-323b-924c-4450db5c9f28 | -16.84987 | -55.91193 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3d72faa3-13d5-34af-9f82-caa97f7f24e9 | -16.84953 | -55.91498 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a58ee85a-c7d3-31ea-8d81-f7a28aac583c | -16.84917 | -55.91803 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 83e3c8a9-1802-37a7-9d98-e603fe133681 | -16.84883 | -55.92106 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| aa9308aa-f274-38c4-9e7a-cc15b7af36c7 | -16.84654 | -55.89603 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 73a59e40-087c-39b1-8849-9fa0107dc8b1 | -16.84619 | -55.89909 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 25ebfe3d-e0b5-3f58-8767-69d5bc293f35 | -16.84584 | -55.90217 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 15ff3fc6-d834-3afc-9893-1a41d1f5f4e8 | -16.84549 | -55.90522 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c3a16a91-4eba-3729-b314-a2f1212077c2 | -16.84514 | -55.90826 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 2396b8d9-ba47-32a6-a533-7e2bec50a8f5 | -16.8448 | -55.91129 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bef56b39-a9c7-3a1b-a5cc-9a3d6073ec20 | -16.84445 | -55.91433 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 967568b5-a873-3970-bc7f-2747a6c414c5 | -16.8441 | -55.91738 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d74b700-7f2b-3199-a94e-b4e3a900c14c | -16.84375 | -55.92041 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 50a6ca6d-9bb3-38a2-b286-ce1354d41750 | -16.8418 | -55.89234 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c19fad0f-6ee9-36b5-b6e8-f655436be71f | -16.84146 | -55.89539 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5ad40583-a013-3e9b-83f1-2eb8d1b028ac | -16.84111 | -55.89845 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9beee8e0-5138-3ebb-bc1b-1f153a865bf4 | -16.84076 | -55.90153 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d161cf7f-61d9-32c8-af39-858dfa9b64c6 | -16.84041 | -55.90458 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 5201c25a-05a1-3835-bac2-4d28e348cba3 | -16.84007 | -55.90762 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 7ac42f1d-db74-3dc1-a70c-f6c4501d9983 | -16.83972 | -55.91066 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dc5bd6f6-b55a-3873-bdd8-97b0839895a7 | -16.83937 | -55.9137 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ffdaaf55-afaa-34d5-93a9-b64faa8f4a57 | -16.83903 | -55.91674 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 95a8f0d5-054a-3d12-af83-4f4930edc7ec | -16.83868 | -55.91978 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 08738472-dae0-3894-b815-000f6c2db144 | -16.83833 | -55.92283 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b92c6778-9582-344e-9d08-508dc93b8133 | -16.83799 | -55.92587 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f5700dd9-169e-361c-8f67-6a27ed488d8b | -16.83672 | -55.89172 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 726b5df9-f848-372f-b7b3-9cbd3202a1bd | -16.83638 | -55.89477 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f3bd4a9f-cc3e-34c4-aa36-4cfcd9384126 | -16.83603 | -55.89783 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 65e388a7-9dc6-3eb1-911d-a49c185c883a | -16.83568 | -55.90088 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 75bce231-baa5-32ba-8480-05cf6f8c29f8 | -16.83533 | -55.90395 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 50c13095-2b80-39e1-933c-98a14e985c61 | -16.83499 | -55.907 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f2040352-a9aa-35f1-afe2-7c1f0da2b943 | -16.83464 | -55.91004 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a496d9ff-c143-3b29-8750-0b4f7bfcaddc | -16.83429 | -55.91309 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 504a338b-d0e2-3208-8035-7c795c08d8c3 | -16.83395 | -55.91613 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 28b8391c-71f8-333c-a603-990bba231f63 | -16.8336 | -55.91917 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 86c7c5de-f489-35c6-a2f7-767932a48a94 | -16.83326 | -55.92221 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 62d059ea-845d-3a6d-8e11-f5a515c3d18f | -16.83291 | -55.92524 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7280d79a-b43f-32fc-80d9-8dbc58869bdc | -16.8324 | -55.92979 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 29f35311-b24e-3305-8d20-8fe7b0d24f29 | -16.8306 | -55.90028 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1a449dcb-1580-30c0-8925-64789abc3437 | -16.83025 | -55.90332 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 9186621d-9240-3b2e-9872-7971d5de5f0d | -16.8299 | -55.90638 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 079d4557-90df-325c-9972-a8e1e329f6df | -16.82964 | -55.95401 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 11a7dfb6-5cd5-3937-b717-043b6b42b3d0 | -16.82956 | -55.90944 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 213f3a2d-f60e-3618-84c7-e4e577cec24c | -16.82922 | -55.91247 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a2f2aa7c-7aea-3113-8947-36847721580d | -16.82895 | -55.96004 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e50adea8-5a38-3843-81a8-f048fd0827da | -16.82887 | -55.91552 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ea5c8b54-6bcd-3c27-b1aa-9106fa18c154 | -16.82853 | -55.91855 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8dd18400-0b05-3f1e-bd8c-a897896a12fd | -16.82818 | -55.92159 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 449f4475-21ee-3dfc-91a1-8484d41b6fb9 | -16.82784 | -55.92461 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 531814b7-a4c7-3b3b-88c7-1654982dbde4 | -16.82321 | -55.96543 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d1ba8a1d-3afa-34b1-9b6b-b0ed91d35283 | -16.82277 | -55.92397 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71b83aeb-9328-36dc-b82b-186b593f537d | -16.82225 | -55.92852 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 45f20f7c-616f-38cc-9000-83065a8b70df | -16.82207 | -57.47862 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4fb92fe8-1543-3cf2-b5a9-bf5f884df272 | -16.82105 | -57.56234 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5771e4f2-ab2a-3bac-aee0-5350a5afb01a | -16.82097 | -57.56061 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 07034d3e-f55f-32cb-a152-658b158e4e92 | -16.81933 | -55.92786 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 484d757e-b780-3caf-864a-e9cc06ee15c1 | -16.81882 | -57.54111 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7939ffe4-0591-3e67-9b22-cbc43db4c1c9 | -16.81876 | -57.54279 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a9cdf675-5b41-33de-a9ef-083d3a2ffe6f | -16.81718 | -55.92788 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eb3d6904-5880-3e2c-9878-ae5eb0994482 | -16.81691 | -57.48278 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aa7c32b9-c24c-371f-bee0-c194c49bdc41 | -16.8165 | -55.93394 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a4ee8633-a8d4-339f-b2d5-afc5d339b01c | -16.81445 | -55.88256 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f98c6b05-405c-3628-8f9d-584fdb03b21a | -16.81426 | -55.92723 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bc3ad1e1-8e8f-3513-b33f-87e5c04b8ea2 | -16.81353 | -55.93329 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5b6ccd66-ab18-318f-bd1e-3b414cb2e99c | -16.81281 | -55.93935 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8a432973-1e4d-30b5-84b9-f2b721ff5927 | -16.81232 | -55.87938 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d9dc4fc4-e7d1-3611-97f5-f78c67d5d02a | -16.81208 | -55.9454 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 18e30889-4c70-3abd-9791-1e29db6552d3 | -16.81198 | -55.88243 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3c262bbb-f9f4-39b2-8101-549507a74f4f | -16.81164 | -55.88547 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 16ed1756-c885-3226-8f7c-b5fbae90dec9 | -16.81143 | -55.9333 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6dc5c065-e1f2-36ad-8737-2681d052f312 | -16.81075 | -55.93936 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 37b5d558-12ce-3c5c-bdef-9bbf03440996 | -16.75898 | -57.7973 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c1e03a03-a8fe-3718-8fa8-e937c9833807 | -16.80973 | -55.87886 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9284a0d6-f7f9-3a98-9d7a-7c6767e78ed8 | -16.80937 | -55.88191 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 819a0f27-cc13-3717-a719-f83e0a62e250 | -16.80901 | -55.88496 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f1b05ddb-1787-3e1e-aa79-ee579c3877d5 | -16.80792 | -55.87258 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d42ff5ca-0625-3682-b425-d9e0a81756fb | -16.80775 | -55.93869 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 985b4e79-9c80-3080-b058-2632346712db | -16.80724 | -55.8787 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c44020b4-0044-3b78-b00e-f0e7fcd6926d | -16.8069 | -55.88176 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 47093810-fbc4-3bd5-832d-2ca212965627 | -16.80656 | -55.88482 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| acdd72e4-1195-3f11-a519-6608a30754fb | -16.80569 | -55.93867 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fa6e3a6e-12cc-3157-9c08-a0d2c4465a3f | -16.80393 | -55.88432 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 531a3c3b-e171-3722-abf4-81c01c6dcb11 | -16.78833 | -57.48867 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 823a4225-bab7-3938-9f75-baa7de9ec0d2 | -16.78594 | -57.81679 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e3293845-13f8-374e-bf62-322aea01df11 | -16.779 | -57.81853 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5af4e7a4-2da7-3c58-abca-b7cdf7a388bc | -16.77536 | -55.77464 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3131ba8d-963d-31a7-ab7f-d20c397fcf4e | -16.775 | -55.77774 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9e79068e-6fa9-33d8-b87a-d865a12f935a | -16.77453 | -57.81793 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f0f02c86-208d-35fb-bd0d-09cdb2d7aadf | -16.77393 | -55.78703 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2b207d53-1d0f-3c36-9b21-7d5e11cf0078 | -16.77357 | -55.79012 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 365342dd-dd26-3185-8021-61b0212a98a1 | -16.77321 | -55.79321 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9ca255dd-4f28-3896-8258-3fcc82bda81d | -16.77286 | -55.7963 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf4430fe-7e12-3e75-9aed-3faae353baf3 | -16.7725 | -55.79939 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0190d24-ee05-3050-9e47-51756830752a | -16.77206 | -57.3937 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README148.md)
