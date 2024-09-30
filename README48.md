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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de5d3611-58ce-3628-b53c-8b282218832b | -17.12095 | -56.1768 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab41949e-3c19-35d4-857f-d118e9ab7c26 | -17.12019 | -56.18083 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 10a83a8c-f5e3-3f00-9b5c-2db174c466cb | -17.11943 | -56.18487 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 14d7dbb4-cdea-3c6e-a574-76959573ea6a | -17.11867 | -56.18892 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0a4d3189-d6c9-38c9-b2f4-b7b1250ca4db | -17.11675 | -56.17595 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9e3c3d42-aff3-3439-a17e-50d4fd3ea7c5 | -17.116 | -56.17998 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8e5af4a9-2c7b-333e-8d14-16c36d7e9c37 | -17.11523 | -56.18402 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| dc5fec73-83d2-30e9-8c22-d5cb54b1597a | -17.11447 | -56.18807 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| adafaf96-214e-33c9-8db3-0a7aad8f8708 | -17.10682 | -56.13631 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 48ba4280-4485-30bf-955f-0b4689d1efa1 | -17.10606 | -56.14032 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 435d9b40-b7fb-3316-9a1b-b598df1de062 | -17.10188 | -56.13947 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b61e378e-8a04-3197-9754-7c7b234ef388 | -17.04901 | -56.11781 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 67d78c08-1e2a-3548-9844-70c76e02f412 | -17.04558 | -56.11293 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 509b7f25-978f-301f-80a4-a066b3d93d88 | -17.04214 | -56.10806 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| da6add17-f243-3b1b-956b-67fbb521c922 | -17.03945 | -56.09919 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9c7e55c9-a6d3-31fb-bbfe-c286d27a1ab9 | -17.0387 | -56.1032 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| df22fe47-1387-3064-b7e4-13abaa842a52 | -17.03109 | -56.09747 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 18c1ecb2-632d-3afd-8f86-349c8ed9b9aa | -17.03035 | -56.10147 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1a21e1e0-b535-38af-ac4d-6ce2310be5dd | -17.02691 | -56.09662 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 342acec2-d69d-3eba-9fed-80a385bfc685 | -17.02617 | -56.10062 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8e93bd86-8967-35d1-9e19-e5ef4f486e97 | -17.02349 | -56.09175 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1609db70-6630-39a3-9361-3f6c17f25e0e | -17.01931 | -56.0909 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 986819b0-634c-38e6-b431-5ccaa16a5779 | -17.01856 | -56.0949 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bf1db963-a6fe-355a-b035-bec848caba41 | -17.01438 | -56.09405 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b35541c7-8254-3853-bef5-c9da319b435c | -17.01258 | -56.17311 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 05e8b14a-2e8b-3289-8df6-a575c24804dd | -17.01106 | -56.18124 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 30b2d45c-9fef-32b1-ae27-c4184bb5fbd0 | -17.01095 | -56.08919 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c6f702e0-8676-3db1-91b7-8b1ce17ca954 | -17.00762 | -56.17631 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4681c820-fde6-3e76-83b8-0ea806bc3557 | -17.00686 | -56.18037 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b22a31b2-4b3c-3a56-843a-c61a0a26f16e | -17.00677 | -56.08834 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 76dfefac-6d20-3548-8084-3c470c72e137 | -17.0061 | -56.18441 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cd3a472a-d0a5-3750-b845-7148233c4f9b | -17.00342 | -56.17545 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ec66aaba-715a-3961-851c-58ac1425c886 | -17.00335 | -56.08349 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ebc8e6d4-fc7d-3055-8b55-c1dd442a3433 | -17.00266 | -56.1795 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0299be62-28e6-397f-856e-59c9f4d67ec9 | -16.99922 | -56.17459 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bd9c7e32-a7c3-3431-a665-3edcabc36ef0 | -16.99845 | -56.17865 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ab71b402-221f-3ff3-9667-8dc9edbb11b6 | -16.99578 | -56.16966 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0076f528-dd15-38c1-88d7-e19e13664a54 | -16.99501 | -56.17373 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4b2b3b7b-b69f-36f5-84d0-8a112d92eeeb | -16.995 | -56.08178 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 20b55ea2-7c36-3aa1-b0d1-ec011649a620 | -16.99196 | -56.14374 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 58ee6998-0dd8-3c4f-b75d-a71aa0655c64 | -16.99158 | -56.1688 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 01c364d8-5185-3cb7-bfca-cb201d601143 | -16.99082 | -56.08093 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4c06318b-d711-3a4a-97e7-a5d1a4598755 | -16.99022 | -56.082 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1c2b4607-1352-35ee-bc59-d4b0523f3dc7 | -16.98777 | -56.14288 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6ae1bcca-0032-3420-8916-ee814794db4d | -16.98738 | -56.16795 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9d76a603-1d96-3fc8-8e34-47d0fc576d58 | -16.97819 | -56.10034 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 64fe1fda-9850-3a8c-b173-a62c5081fd3f | -16.97327 | -56.1035 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a1e250e0-e41b-3834-8480-95c7b7391306 | -16.97254 | -56.10752 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 14504813-592c-3e11-a2b7-b24ccf35c38e | -16.97179 | -56.11155 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dcff8e42-ddb5-33cf-b18e-36f85b153159 | -16.96835 | -56.10666 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5005a917-0aaf-3421-ad88-a921c06e5579 | -17.26074 | -56.45083 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b6679587-1907-3d9a-b417-3db07b720441 | -17.25994 | -56.45501 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0d5b29dd-cad7-350d-a000-3bd4545f2688 | -17.25728 | -56.44577 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ac8b7dc6-84f5-31f5-bc06-a6c6c44227d5 | -17.25648 | -56.44995 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dd70bb26-3f22-3ca0-af6d-6c7e7517ac2e | -17.25568 | -56.45413 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7a9bddb-82fe-377d-92cf-af29ec85f8a6 | -17.25223 | -56.44907 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2d3b962d-e66a-36b6-8bfa-c840e587bbde | -17.25142 | -56.45326 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 73589cac-ec7c-3663-9aab-270600c2a49d | -17.11214 | -56.38794 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0a0d927a-c7a5-3d10-b7f3-7221d556f1e3 | -17.10633 | -56.3954 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 218b2c86-f64a-3d0c-bf0b-f09a7df22d5a | -17.10286 | -56.39032 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 539f9eed-6250-3496-94f8-c18d632ae1f3 | -17.10208 | -56.39451 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9ef4628a-4efe-38a6-bc47-9d565718795a | -17.09861 | -56.38943 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3a54a1ef-1b7f-335d-a742-eeaa02555125 | -17.09783 | -56.39362 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e3bb033f-5456-3723-8f23-af4f8ea16244 | -17.09357 | -56.39273 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bc8f6201-57d3-3707-9f66-598df87ef45a | -17.07892 | -56.37672 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f7f5f8d5-da17-3b8f-ad2f-351813fe036c | -17.07814 | -56.38087 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fa2a187a-76a7-3292-9cb1-f5cbc01084b6 | -17.07388 | -56.38 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3273ee28-2094-3909-85d3-503666c84171 | -17.05132 | -56.40572 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d2793e64-3c9f-3294-9bdf-8e434ec678db | -17.04706 | -56.40483 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a1ee2629-06fd-37ef-ba26-03f0461d4819 | -19.64988 | -56.48537 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fc6a316f-2fc4-30f7-85f6-deebaa8ae226 | -19.58293 | -56.53226 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 21aab61c-f97b-3c2b-87d6-8d474465fe8d | -19.57882 | -56.53138 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e1523ff7-b0ea-334e-81fa-2603e85e3e12 | -21.04174 | -57.50835 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1f7fee46-4401-3ec3-991d-ef52a3d9f993 | -21.03749 | -57.5074 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e7982fd5-b5e5-396a-bc1a-c8e437b77611 | -21.03323 | -57.50651 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1728c9e0-5698-30e8-b1e2-3dc7fe2707cf | -21.02897 | -57.50562 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3b7313a1-a64c-358d-858a-be19b4d5bffd | -21.00864 | -57.51889 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b2d6413-210f-3edf-8f3e-a1418c40610e | -21.00525 | -57.51357 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ebb74f82-1a4e-32b2-97ef-26fafe7e70b7 | -21.00439 | -57.51795 | 2024-09-30 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 47aed1be-e72a-3e2f-860a-f2c3193d1be2 | -13.75626 | -56.47998 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf69ff6e-5b11-33a1-9167-fe919a012ee3 | -13.75606 | -56.4783 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c5a6ae1-1f47-3917-9352-c326246b05f7 | -13.75521 | -56.48295 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2f1ac2b-7816-38ea-8c47-f672637be732 | -13.75175 | -56.47896 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2953d435-f317-3671-938a-bbec0158d8dd | -13.75069 | -56.48193 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f91cbd2-35d5-3756-90a7-61701a51e1b0 | -15.6141 | -57.4577 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fefb4dc-e485-310a-99ca-3a08ebde68e2 | -15.61312 | -57.46285 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31aed72c-746d-3047-a68e-33404302ad1e | -15.60942 | -57.45672 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bda42912-e8bb-3ff1-8786-765b4453dec8 | -15.60572 | -57.45061 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37ec0974-b7d7-3ff6-9e54-a295be58d78c | -15.60474 | -57.45576 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5071f9f5-e3a3-3bee-a02b-cc7822f796fc | -15.60376 | -57.4609 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da128dba-0738-3218-b975-24d0c9f0eb11 | -15.60104 | -57.44962 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b70d1587-56c8-320f-b02c-05354e905135 | -15.60006 | -57.45476 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d055a195-3526-3447-9777-9bdc9d6f811a | -15.59637 | -57.44863 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fff6a24-a7af-3c23-9a9f-95c9eac5e8a2 | -15.59538 | -57.45377 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51a4f9ee-3db7-34c2-8ea1-600f3f81f14b | -15.5944 | -57.45892 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5793e5c1-b769-3aa7-b2cc-471c13f607b0 | -15.59169 | -57.44764 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7ee7675-3402-3e32-8303-5e4c382eb02c | -15.5907 | -57.45278 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ed69cb4-ee9b-33cb-a827-c2780e0c514f | -15.58972 | -57.45792 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 464ba8cf-489f-3549-bade-71585c9ab683 | -15.57398 | -56.91972 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef191636-74ad-34ba-b4ad-dca4f8954203 | -15.56953 | -56.91839 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README49.md)
