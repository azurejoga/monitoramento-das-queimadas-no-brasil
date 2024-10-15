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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 783e8f35-a7e8-3705-81a3-cd31e997c8c3 | -2.38229 | -49.12977 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c228f21-c709-3cd0-8bd4-06d4621df384 | -3.70347 | -50.11827 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a407461-af53-32af-aae3-9cfd86717a9d | -3.70237 | -50.1201 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a8d9637-4572-3c29-ad1c-94f8c54bd66e | -3.69953 | -50.11764 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a039599-abe3-3564-9776-fb3a27a3ea26 | -3.69874 | -50.12259 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daef2698-7527-3834-9ae0-0739aa38e65f | -3.69559 | -50.11701 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f733551-1159-3b38-b3e3-75ae6c27a231 | -3.6948 | -50.12194 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2da00b01-604b-3916-a79f-54540c76c738 | -3.57308 | -50.36921 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 212828d5-3c11-3c71-9731-f05ead177db9 | -3.83002 | -51.40823 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a50596-3506-3ad4-8fbf-50af651fef67 | -3.07534 | -51.18872 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b747100-7067-35d5-964e-0607ab64d72e | -3.0747 | -51.19267 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7b0de4-d653-3185-ae52-becc27183e80 | -3.07106 | -51.18809 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde2d5f3-4cd6-3949-926c-ed6a3bbc3a3e | -2.90444 | -51.93435 | 2024-10-15 04:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 602ea0cc-0fee-3373-8e7f-c968c225b3a3 | -2.90371 | -51.93879 | 2024-10-15 04:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89f84dcb-0364-3806-8619-c54b6e35cdc8 | -3.53632 | -51.22057 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ccb4aa-64a5-3f2d-9091-49a21a0be953 | -3.53576 | -51.21951 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76290500-30be-3ac3-b2d5-f49eb081d5d8 | -3.34329 | -51.64492 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fd34f34-3892-3085-8f8e-70b0f99e3aa0 | -3.07298 | -51.17619 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7a88639-772b-3acf-aaa5-9a05aedc25b8 | -3.07234 | -51.18016 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 503b2d9c-f922-3b16-8d2b-105fabd25675 | -3.0717 | -51.18412 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f243113-4693-3a70-9fc7-50c4f189192c | -3.0209 | -51.20038 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fab029e-7a61-37fe-8463-f99a6cf4c1ee | -2.8992 | -51.93808 | 2024-10-15 04:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7929daea-a251-3736-82ad-ed28ebbae3f5 | -2.89847 | -51.94252 | 2024-10-15 04:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442165c9-56fe-30b4-b046-e0435ec6e9be | -4.07738 | -51.07558 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1648eeb-3879-3006-81c3-07c0bcae6ce9 | -4.07322 | -51.0749 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5d87768-d742-3389-abfc-b1abd4e6348b | -4.07261 | -51.07867 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb93f141-ffb6-3c52-8199-d57e348e43b7 | -4.072 | -51.08246 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04778165-c245-3f9c-b5e0-aab8a2352e18 | -4.06844 | -51.078 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6d2f86f-afd7-3fae-a451-2a09b9b69915 | -4.06783 | -51.08179 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 632245f4-8b7b-3aa6-9c20-38f17ad6e7f2 | -3.92224 | -51.25988 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c38878-1c65-3354-8752-94d807c39d58 | -3.87378 | -52.13446 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da3a24d0-7ce9-3c9e-ac81-886d3adeaca3 | -3.87305 | -52.13892 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da23fc18-9788-3ceb-aa78-287b3933baed | -3.8704 | -52.26811 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1dd2cd0-b315-3337-b5b5-306c95e31e50 | -3.86965 | -52.27266 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 231a437a-465d-353c-b4ad-03b2a7bc6355 | -3.85362 | -51.33298 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 692d13ec-ece9-31d6-90b8-8d703a33d72e | -3.8533 | -51.02165 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf93fd04-641c-338a-a02e-3a98c787c23c | -3.85297 | -51.33689 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d495720e-58d7-37cb-a124-d89b9f12410d | -3.85003 | -51.32833 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5ce3931-e43f-307d-9ac1-8f94e656791a | -3.84937 | -51.33224 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798be0e4-ec42-3a31-90fb-beb40978c4cf | -3.84915 | -51.02086 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5f3f376-5eed-370a-a2de-7e421dbc943d | -3.84475 | -51.35995 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9593fdbe-ada5-3bb1-a6b0-d5a06cf27907 | -3.84274 | -51.32862 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3222cccd-78d3-368d-ba3a-46a50406d6af | -3.84155 | -51.32684 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ea0553-edc9-3242-a044-83455bd57768 | -3.84089 | -51.33077 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed80fd73-511c-31ae-9174-d15e40d39844 | -3.83251 | -51.40692 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddac9a28-183a-375d-97ca-203035695974 | -3.83066 | -51.40421 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4cabe7-ff9e-3a89-b4f9-9749083d896e | -3.82938 | -51.41227 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e44a922-de45-3538-a796-b625a8c266e9 | -3.82824 | -51.40622 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ff8ac40-74dd-3df6-9cd8-216464e68954 | -3.82756 | -51.41024 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a77e4f4-031b-37ac-88fe-1d3de74161b9 | -3.8269 | -51.41423 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b4a521-81db-38ef-a3e9-7c647e7a0102 | -3.82575 | -51.40751 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f93a367a-0ad1-3248-b856-e343abecc02e | -3.80307 | -51.1978 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffbd7e6b-4b47-3942-8c3e-750a4ecc8704 | -3.71397 | -51.79539 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1941a1d-10c2-3a0c-8f12-fcea657afc1e | -3.71276 | -51.24797 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2994218f-7df1-3113-abde-4a600682c8e1 | -3.70853 | -51.24726 | 2024-10-15 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d70424-b3d7-3697-8c13-e98d93bc3624 | -3.68196 | -51.17099 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2442186-10a9-31fe-b2bb-f40bab6b3cb7 | -3.68131 | -51.17488 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3889a32e-7842-3515-bcc3-1b680dbb5100 | -3.64406 | -51.81103 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 629c9bef-ca71-38ec-8e69-1d96f884e8b8 | -3.64382 | -51.80947 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 327e245f-f97e-33f5-a9e7-2e38d455e8b9 | -3.61719 | -52.03522 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a217271e-341e-396a-9af0-9be4da8167f6 | -3.55006 | -52.02397 | 2024-10-15 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b56228f-153c-30f6-b1d7-40df06545505 | 1.00875 | -52.21935 | 2024-10-15 04:23:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a9c00e70-d51e-37ee-8723-c469fc3098f3 | 1.00791 | -52.21401 | 2024-10-15 04:23:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1fa8eff1-78fd-31f9-a3a6-9fe6caeeb205 | -1.39584 | -53.10632 | 2024-10-15 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3c97958-8753-3ad2-9c12-041532233db6 | -1.20235 | -52.94117 | 2024-10-15 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7100483-af33-3a25-9a8f-c9d97d407af5 | -1.20217 | -52.94047 | 2024-10-15 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5de64635-e3cc-3bc6-9378-d82a24329cf4 | -3.14541 | -53.16743 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c658376-08ed-38e7-99b7-d7863a695e70 | -3.10011 | -53.03333 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f03ea67a-1115-323e-b806-63f6d4802b1a | -3.09926 | -53.03855 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab9b8059-80d1-3cdf-842e-5837e757b179 | -3.09841 | -53.04382 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c535cdf-8cb5-3241-8c96-11782fe5e414 | -3.09754 | -53.04916 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3078805-2bef-3028-b558-04ea4f1e33de | -3.09441 | -53.03782 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fae5d26-b2d3-30b1-9400-f797f7e7d0bf | -3.05263 | -53.26299 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 25c68eb1-9e46-3849-b241-489a8a74b43a | -3.04953 | -53.25113 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7126c056-1707-397e-9258-e20183137b75 | -3.04863 | -53.25662 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5c8c371-6988-3d39-a63d-b494fda84332 | -3.0477 | -53.26229 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8408ff76-4562-3865-bfd3-4434b2609cae | -3.04548 | -53.24502 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b7a4e4f-193f-3947-81b4-5744e17c4cbc | -3.04371 | -53.25585 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 286776d8-01c4-3c9f-8dec-6b12e7094443 | -3.04278 | -53.26148 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9b69560-d893-35d0-834a-1f6d70af3aee | -3.04056 | -53.24428 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 115afad3-251f-34b8-9bff-a7beff7b087d | -3.47705 | -52.87773 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 082461f8-cf2c-31da-a669-474dbce825ba | -3.4724 | -52.87881 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 830e8c78-fb9c-3bc2-ba9a-3b78040e4a5d | -3.4723 | -52.87691 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc44289-2450-364a-bf0a-a54d2235e096 | -3.42358 | -52.72936 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c829c486-fef2-3894-8973-bcc7dd0d5f5a | -3.41801 | -52.73372 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9467e28-cb30-3d9c-8bb8-af60c784582d | -3.08956 | -53.0371 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06c73582-0d1e-306a-8dd9-25c0b99f4953 | -3.05356 | -53.25736 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3660fa47-127a-3254-8175-9e3a03e85baf | -3.0504 | -53.2458 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1961cf3b-d740-3ffa-b819-1346bca7d17b | -3.0446 | -53.25039 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7c616da-e276-358a-99c7-8530990a189a | -3.03968 | -53.24966 | 2024-10-15 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75463e34-5f97-317d-b089-f48e025d42fa | -2.85891 | -52.47126 | 2024-10-15 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0813264-98c9-38ec-89ce-dd9e92323ea0 | -2.86437 | -52.46721 | 2024-10-15 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6310cff9-7ac3-30d0-a2d1-d3e45da38339 | -2.86359 | -52.47202 | 2024-10-15 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dffd7d43-fdf3-3a3a-832d-66632b3033d1 | -3.82574 | -52.39768 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170d1ae4-313b-32e7-ad5c-3768caba2949 | -3.82496 | -52.40237 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f966fece-7f41-3ffc-9188-335a073b1807 | -3.82117 | -52.39687 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 711fd5f3-1239-3849-8684-5711a2104d69 | -3.82039 | -52.40162 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90828d04-d21c-3830-8850-d700bf2b9d83 | -3.73552 | -52.31879 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72b08240-a6e4-3497-882c-da8b7a27d82f | -1.53971 | -54.34662 | 2024-10-15 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3778426e-7f04-3b42-891c-0abe9800c6a4 | -1.53431 | -54.34561 | 2024-10-15 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
