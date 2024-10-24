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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 823b89d7-ed1a-3fae-9679-e0631b1462c0 | -17.6671 | -57.4616 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| e99c1935-3d0f-354c-bf9a-f2b23fa7bfcc | -17.765 | -57.4909 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 3d96ce06-8906-3e4c-a8d8-2e4e1f4d9608 | -17.7453 | -57.4933 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 144746b9-f53e-32a9-b28a-6641666abdc5 | -17.6868 | -57.4593 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 61250c9f-a2ba-397d-bfbe-233b4de44730 | -17.6865 | -57.4798 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 43599d8d-2085-3aba-a134-9890a7f1b74c | -17.7654 | -57.4703 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 894ff892-b931-3796-9e64-c42996da4374 | -17.7082 | -57.3539 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| d1bdc172-e50d-3417-9f84-038b31fb2f78 | -17.7841 | -57.5296 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 147ff8cb-faa0-3c38-a0e4-46d856be3dfa | -17.7644 | -57.532 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 7a476fa7-ead8-3479-a999-db4031a87732 | -17.764 | -57.5526 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 73960cc4-d301-360f-8795-3498ab22bac0 | -17.7062 | -57.4774 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 15f62e0f-45b0-374b-a92e-b41991bc331a | -17.744 | -57.5756 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| c0d179c5-3042-368d-922f-b6d3787d4309 | -17.8229 | -57.566 | 2024-10-24 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 4c31cd88-a361-308b-a3d5-be13b9350298 | -17.8226 | -57.5866 | 2024-10-24 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 5dbb5d0f-4f6a-3d1c-9572-0c572aaaf7ac | -17.9268 | -57.2447 | 2024-10-24 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 48b92329-6f8c-3812-826e-d6c88a5f63e1 | -17.8427 | -57.5636 | 2024-10-24 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 42b4fd3f-31f5-3fa8-bc17-eca170cd5531 | -17.8423 | -57.5842 | 2024-10-24 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 44ca4bf8-c3b5-3c91-9064-e3327749617f | -18.0639 | -57.3101 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 53296b96-4232-3ae7-a21b-1fdd74040af8 | -18.083 | -57.3489 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 763b37c0-a7c3-3d25-b267-f97e5e4eb951 | -18.0841 | -57.287 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 6f2cf468-0ef8-3bae-838e-8042faf99732 | -18.0834 | -57.3283 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 1dba4907-9e39-3a24-b6ac-cc9b7ef86095 | -18.0837 | -57.3076 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 538082af-cd15-3a27-b885-ed7adec003ee | -18.1802 | -56.3008 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 57a3e073-48dd-33ab-b740-769c61bc0ef2 | -18.0636 | -57.3308 | 2024-10-24 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 77a3b2c4-1a82-3266-8e99-e7ed63bdd961 | -18.3 | -56.2431 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 83d8296c-bafa-336b-857d-5d370ce2ca15 | -18.284 | -56.0367 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 299.8 |
| 3b419eeb-e819-3386-8e21-a4e1425cdc06 | -18.2836 | -56.0576 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.3 |
| c53cf0dc-46a1-30dd-9bd2-8d740191801d | -18.3199 | -56.2404 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 70495b01-0d0e-3afa-b904-4d8e0e36f784 | -18.2641 | -56.0394 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 336.5 |
| d82bf0f1-84c0-3700-be7f-b751c125fe7d | -18.2637 | -56.0603 | 2024-10-24 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.2 |
| 121b869a-c5dd-3b6d-8003-34a2e9c0b381 | -19.6863 | -56.7204 | 2024-10-24 12:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 140.3 |
| cb4de21f-87cb-3ba4-97c9-45297982ed86 | -19.7061 | -56.7386 | 2024-10-24 12:36:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 046ccfb2-4ff6-34cd-8b72-bb4dc830c95d | -19.7065 | -56.7176 | 2024-10-24 12:36:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 849f2d40-4dac-37c2-bb33-f634caa7306a | -16.9792 | -57.5223 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 209.1 |
| ea788ad1-642d-3a95-b7f9-0d4b296b374a | -17.0184 | -57.5178 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 3547b8bd-6bb3-38d7-9ab2-6367ddf9cd39 | -17.0188 | -57.4973 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 3818bf1e-bb4c-3d32-bc89-23c61a026016 | -16.9596 | -57.5245 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 96baa6b6-93c7-3120-bd4d-8e105f7f1c33 | -17.0191 | -57.4768 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 881822aa-78fd-3af5-b8f2-647164f2cb87 | -17.039 | -57.454 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 6e7891c0-ae08-37d7-9397-fecc66a437cc | -17.0387 | -57.4745 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 7c22c37b-402e-3725-a3d3-e3d309f265cf | -17.0384 | -57.495 | 2024-10-24 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| e08e6cf3-c831-3f8f-8ff2-57172fef713a | -17.7436 | -57.5961 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 7b92cbc2-74cc-3484-9b5c-1adbed602d15 | -17.7079 | -57.3745 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 13e02245-bc1b-316e-b822-56f333216d47 | -17.7654 | -57.4703 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| d9c868b5-15d3-33cd-8ac0-ced9156cbbf3 | -17.7082 | -57.3539 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| fe5c2499-1daf-3973-ad3a-ed4bfbea6658 | -17.7644 | -57.532 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 5f7ae848-9206-309c-a871-9d58d380458e | -17.744 | -57.5756 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 45d50cda-7548-3d9c-9b70-b0c336bf69e8 | -17.7841 | -57.5296 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 06626063-e7aa-3fd9-88f5-599a4a1ec281 | -17.7453 | -57.4933 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| e9763c29-3918-3a86-ba46-88cbf10c1a0e | -17.764 | -57.5526 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| be172b56-608b-39f3-8f9f-91f97743df75 | -17.765 | -57.4909 | 2024-10-24 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 8b1a3f28-7f38-3eed-adf4-821039b1ab88 | -17.8229 | -57.566 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 7710c2d8-e98a-349a-9e9b-160fc684f6f8 | -17.8427 | -57.5636 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 90786e1c-cad2-350c-96b1-fa7e7618289e | -17.9469 | -57.2216 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 103aa95c-93aa-3865-8d52-8c5773625ae0 | -17.9268 | -57.2447 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| de7bc21c-3265-3080-b32e-6290316ef8ec | -17.8226 | -57.5866 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 8f96c203-0d29-39c4-a1c7-c2f68274a978 | -17.8423 | -57.5842 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 676bfd13-9aa2-37e3-84bb-7b2ed5a3b2c4 | -17.9272 | -57.224 | 2024-10-24 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 14c0df22-1e4c-32a1-8a40-a00a3d24d872 | -18.1802 | -56.3008 | 2024-10-24 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 9a0c934a-eaed-36bf-9c3a-1ef7a3fa31b8 | -18.284 | -56.0367 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 405.2 |
| c6ef3103-8cd6-32f9-af5e-cde18eb966aa | -18.3199 | -56.2404 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 9c6571d5-86cb-30ea-99b6-1659a1135b27 | -18.2641 | -56.0394 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 676.0 |
| 7b3126de-61c2-33d9-bc06-d57f2cec43ae | -18.2836 | -56.0576 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 5c998128-a3ef-35b9-b761-56bfee137c10 | -18.2637 | -56.0603 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 326.7 |
| 67cd5922-5d0d-3ec0-bd2c-c8caa9b7587a | -18.3203 | -56.2195 | 2024-10-24 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| c38798d5-9970-3c5a-8579-089d1a87cf40 | -12.1719 | -46.9906 | 2024-10-24 12:56:15 | GOES-16 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7048b6bc-47c5-3c15-bdc0-af74a6a1b424 | -12.2754 | -47.6473 | 2024-10-24 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 046f0d58-7cc4-322a-8964-11a063ed792b | -17.0188 | -57.4973 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 95810d1e-a874-382c-88cc-618304b034d7 | -16.9792 | -57.5223 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 152.0 |
| c68e481c-ef7b-3663-bb8a-0d8971d2f4d1 | -17.0184 | -57.5178 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 9b9148f0-22bf-34f4-9af7-532b32474cb4 | -17.0387 | -57.4745 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| fa324ef8-9649-3a1d-960d-5e5b53ca5e23 | -17.0384 | -57.495 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 155f432e-3378-3113-9804-dea42360c41e | -17.039 | -57.454 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 171cb7fb-5978-3b66-91e5-3300e28f6e87 | -17.0191 | -57.4768 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 429b932e-c0cd-3df9-8fc1-d25d6c7b84e8 | -16.9596 | -57.5245 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.7 |
| ba73053d-b9a2-3cc8-93e7-e7f3e4db056b | -17.0011 | -57.3766 | 2024-10-24 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 0f11ba0d-12c2-3d82-b7c6-91b2c3ade8b7 | -17.7079 | -57.3745 | 2024-10-24 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| ba63017c-c862-38ad-97a2-4ad0a5521e89 | -17.7082 | -57.3539 | 2024-10-24 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 70a78d37-f122-3a59-abc6-6e0e7269f859 | -17.8423 | -57.5842 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.2 |
| 076bfa46-e6b1-3528-b352-807d9726410b | -17.8226 | -57.5866 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| a4dd0325-3f56-3c5e-901c-604b8f54dac2 | -17.9268 | -57.2447 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| c3f58c0c-efa1-3cc8-99c3-751afb040bb6 | -17.8427 | -57.5636 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.8 |
| 1e907140-e516-36b8-9fe6-0b0687dabab0 | -17.9469 | -57.2216 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| e97f9f75-3f5c-3f95-8aec-b0524daea600 | -17.8229 | -57.566 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 7c6b5ea2-04aa-3455-9678-919d9ce0adc8 | -17.9473 | -57.2009 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 10ac1f10-d4de-3291-9937-da7edefd61f9 | -17.9272 | -57.224 | 2024-10-24 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 7bff1c55-edbb-39c0-b62d-dc12dff0aee6 | -18.0841 | -57.287 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.2 |
| f0022e1a-5793-369d-aa9f-761faac109c9 | -18.1604 | -56.3035 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 90d4bc30-0ebb-3bc5-bcc5-ce0cab70c225 | -18.1798 | -56.3217 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 9e7478e0-9101-3cf9-851a-c04f3dced5cc | -18.0837 | -57.3076 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 22187b07-9ef0-3484-8e67-ec310dae8098 | -18.083 | -57.3489 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| ceba0ea3-2dc1-39df-9ec6-600d2070ebc3 | -18.0639 | -57.3101 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 9329cd61-460c-33be-83b7-2815c3624ff7 | -18.1802 | -56.3008 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 9aa0f092-554d-3ff8-b214-321fc8108ee3 | -18.0636 | -57.3308 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| c07ed6b7-1653-3d32-ac97-ef2e52deadb1 | -18.0834 | -57.3283 | 2024-10-24 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 893988be-b329-3ef7-869d-a21cced746cb | -18.3203 | -56.2195 | 2024-10-24 12:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 40616b95-1354-3414-af6d-f73e904ae427 | -18.3199 | -56.2404 | 2024-10-24 12:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| ee19096b-d144-31b9-8596-71439518d178 | -18.3 | -56.2431 | 2024-10-24 12:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 04941ae3-159f-3dfd-9a4d-99d44262a0b9 | -11.9028 | -43.8348 | 2024-10-24 13:06:13 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 62c91418-b7fa-3e53-9e19-451ee8c8d2c6 | -12.0526 | -47.2538 | 2024-10-24 13:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |


[Clique aqui para ver as próximas entradas](README118.md)
