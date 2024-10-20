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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b387c39f-ad03-30c9-9600-e053d866d199 | -2.81159 | -51.34766 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f4d061c-320e-3b3f-b606-0320ba8ad6d4 | -2.80815 | -51.34713 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b7e1a0-aba9-3796-86ee-0dbbf1611c35 | -2.80574 | -51.02179 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1be1e2d9-1560-3538-ba82-1c76af960a87 | -2.80354 | -51.60242 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1230d8d-88e6-3a49-abf0-5e8b7ce89bde | -2.80014 | -51.6019 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ca9696-06c8-35c3-a990-b8b6850e1804 | -2.79954 | -51.35725 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e9b80ce-3592-3a6c-ad0a-2e95bfd14e51 | -2.79896 | -51.36098 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cca827b7-5835-3874-b90f-3e86b311974e | -2.79611 | -51.35672 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a720b3a7-2909-3f43-ada1-e4310a1d5722 | -2.79553 | -51.36045 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ad540d1-8644-3677-8d95-bc1abf97f7dc | -2.79495 | -51.36417 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f3bc212-89aa-3498-8ff5-ed9e46e85c5b | -2.7921 | -51.35992 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1eac221f-23ff-3eaa-999e-643bb22551af | -2.79152 | -51.36365 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 246d9467-e379-35c7-9076-c3188d63dbb2 | -2.79094 | -51.36736 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8acb8490-72ed-3dd9-bc02-c887d9cd1bd0 | -2.78809 | -51.36312 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca617f97-f97f-3fcf-861e-ae6a41322585 | -2.78751 | -51.36683 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54e6a6d7-f4c5-3cfa-9df7-6dc58388ad86 | -2.77066 | -51.97096 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 757e29f6-debf-3956-8006-27a3456d9111 | -2.7673 | -51.97045 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 59a58282-e0d5-31be-a082-ba1bd10fb84e | -2.76674 | -51.97402 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3211dc8c-aeb9-384e-8ed2-e0f23ee381a9 | -2.73986 | -51.6273 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee825bb0-02e3-3da8-aca8-bd7465fa87c5 | -2.70703 | -51.34325 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c66d8ec-e655-3426-8d45-ece440978b87 | -2.7036 | -51.34271 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c33f2e5-6185-3879-8acd-725ed7e5bb7c | -2.65422 | -51.84391 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a15f34d-10e0-31b0-ad3c-a06d7985fadf | -2.62394 | -51.76181 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ee02c4-9edb-3a9f-a21f-61bcb30c81be | -2.62338 | -51.76542 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc8803e-89f8-3a47-bd9c-2c6c8fa33d29 | -2.62056 | -51.7613 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5166d07c-4fd0-326e-9f7f-7d77476793b7 | -2.59637 | -51.84965 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ba9c495-ec93-3294-b06c-b9d3910eb77f | -2.55076 | -51.24335 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3156fdb1-23b2-383f-baac-2f0ba52ccb5e | -3.72453 | -50.71725 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 098979f8-a613-3030-9b65-64b86ee6969e | -3.72392 | -50.72126 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e2ad1f0-61d4-3282-89fc-ddb3a2c9ea41 | -3.89218 | -52.12385 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b1e89d-289c-3aae-9867-0d22314bf2e5 | -3.88881 | -52.12333 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc54a1a7-7b1c-3b3e-bb52-76c10519ed2a | -3.86343 | -51.95284 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e5f1888-0f28-3594-aa04-6528d130394d | -3.83289 | -51.9258 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16c6d91-5917-32cc-bed3-726537055ac3 | -3.81591 | -52.2149 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19db5f35-6ea8-394f-87c5-41bd09ba9edd | -3.78664 | -51.97171 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22153d8d-13c5-3b31-b2f4-a2499327fe9d | -3.78325 | -51.97118 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54ae0701-9525-37f6-b50a-286848877bc8 | -3.77987 | -51.9929 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dda3a440-dd02-399c-b5c1-39e0763537d8 | -3.77253 | -51.97324 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42c7c8d-50f2-319b-a440-ff50f7514ee0 | -3.77197 | -51.97686 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae9a1ddd-61ff-36d6-9c00-0ba74918818a | -3.69225 | -52.01268 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cd33d9d-2dde-3b5c-a1b8-13ab7d228697 | -3.64101 | -52.03067 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ae82e4f-698a-3252-a7f2-1e6b1f1247f6 | -3.63764 | -52.03015 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92ace1c8-4761-33f4-8ca0-5373f1e752f9 | -4.49153 | -50.90518 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f973d4b-db35-3372-bd81-13c9e70ec162 | -4.25365 | -50.99316 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5f6092-562e-3902-b454-807017d33ba8 | -4.25304 | -50.9971 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27cf84f6-c031-31f8-be96-03a07b1dc290 | -4.25072 | -50.98874 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1df21191-402a-3d8b-8999-55a380fcdccb | -4.25011 | -50.99267 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24f5d4c4-bf87-34e7-8929-832a836908d0 | -4.24951 | -50.9966 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e941a95-0999-3464-bf7e-378e478c9afb | -4.24718 | -50.98825 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45735e56-e66e-35ea-a670-74df0e65722b | -4.24658 | -50.99218 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bb5fe27-9a3d-3a49-b93c-7118b5085fce | -4.24597 | -50.99611 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8762a8d1-2929-39ea-bb53-3ca1c96ed181 | -4.24537 | -51.00004 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b116f251-385d-37a9-a82a-b9954b478174 | -4.24304 | -50.99166 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79916f99-3be4-3a3b-93d9-01e1f128ce34 | -4.24244 | -50.99559 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eea0d3aa-7a2b-3123-aa7b-f8644139be3d | -4.07715 | -51.13202 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bff488d-bd54-31cf-9ff9-e81cb204d225 | -4.0678 | -51.12282 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9030f1ec-8355-3fa2-9cf4-c0904128b9ab | -4.0228 | -51.01225 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07ef30b-0a32-32ba-8203-77f63635a6af | -4.02219 | -51.0162 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cda29cd6-aaec-36b1-b519-15fd796dd5ec | -3.86507 | -50.98151 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 637ffcc9-d71c-368f-94f4-7d4321f9f734 | -3.86447 | -50.98544 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab7b793c-112d-3aca-8e56-32403ff192a9 | -3.86155 | -50.98098 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 361dc666-f157-3d3b-83e8-6130ce9b4adc | -3.86096 | -50.9849 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ac8813c-9d1f-3b4c-88df-29d75ab77e93 | -3.86086 | -50.98145 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 351a193d-4e46-348d-b0a0-0257b1507780 | -3.86025 | -50.98536 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa7412e8-fdf2-3069-8393-71790da2d646 | -3.71409 | -51.11155 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16955085-b559-3c02-92c8-496dbfd45b1f | -3.71348 | -51.11541 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d17444-42eb-30d7-afb7-4c613d4a0b2f | -3.67924 | -51.08246 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b9713df-b8f9-3c2c-8d7a-34bb004d1f91 | -4.17079 | -51.2289 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d80452b5-b9f7-3be0-a9d5-a59aac5a3abc | -4.1702 | -51.23277 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e31d1dbe-6264-33f6-a3e8-fb7da40e8941 | -3.83529 | -51.29433 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6d368f3-f3bb-3ee2-966f-b0ab201d1bd1 | -3.7976 | -51.60873 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98c7b396-0676-3202-92f8-dc1238c5d179 | -3.78892 | -51.35019 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1f72b5c-1ea0-36ed-97d7-cffbb9f87fc6 | -3.7833 | -51.31805 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6747affd-4142-3899-8ee2-1b0bb288fd5b | -3.77755 | -51.30939 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb1ffb90-92f7-3706-b0ce-6514b0ccc005 | -3.77409 | -51.30879 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee5f9fc-12cc-3dc8-975c-16135af26b06 | -3.70394 | -51.60226 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ece3a3f-0506-3f1f-b344-12c8cd5d56b7 | -3.70051 | -51.60174 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e4a8f41-228b-340a-8968-1ca9818344c9 | -3.67823 | -51.74584 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec70ffc7-9ec9-3d6c-a20f-0886fd088c0d | -3.67426 | -51.68108 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53a3114e-8348-3f74-9606-4f9cb6dd3baa | -3.6374 | -51.78458 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffc4d84c-965b-3c69-9084-c8f3e31e4e9a | -5.94857 | -51.69333 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd5b639-6103-32ef-92fa-956d24a25f63 | -5.94798 | -51.69719 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b96bdd9e-6271-3ac7-9409-f80451b833b5 | -2.21039 | -51.94753 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f56b7560-e645-3101-b88f-a14ab47af948 | -2.20984 | -51.95108 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cba36060-940f-34eb-8e3c-6746547dcc8a | -2.20942 | -52.01997 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 752286d5-7d3c-33a9-a10b-ea8965292200 | -2.07376 | -52.30152 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc235c15-91a7-3c78-8cc7-eeb0157706bd | -2.00873 | -52.28436 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f06d1ddc-a029-3e8a-ad14-3f07d9610c3c | -2.00818 | -52.28785 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee2a8a64-0ca3-3848-941f-fa8138ccd8c1 | -1.99179 | -52.1312 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 104de314-64dd-3b3f-9d72-b2cf78d438a6 | -1.98845 | -52.13068 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5093eac2-fe63-384f-985f-05c104e96676 | -1.9879 | -52.13419 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5123b937-146d-3522-bc8d-7fb71d1542da | -1.93902 | -52.72773 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3e0f41f-758c-3d7c-b390-05c7a7b7bd0f | -1.78947 | -52.05657 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ca4c372-ee3a-32b3-9cff-050d8ed52f99 | -1.78668 | -52.05254 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 87289991-d49f-3336-b02e-468501c3ea57 | -1.78613 | -52.05605 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e49339a7-7931-3261-bc38-2a98082e4020 | -1.76485 | -52.23561 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f57ea86-e3fe-3631-bfc6-93213b5a2c50 | -1.70704 | -52.53941 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2177bd45-65bf-36d6-9d20-76a54a685890 | -1.7065 | -52.54286 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 908781a1-b14e-3fc4-88bc-889bb018626e | -1.70596 | -52.54631 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19dbb45d-1e70-302c-9e8f-eb2997f539c0 | -1.70535 | -52.52854 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
