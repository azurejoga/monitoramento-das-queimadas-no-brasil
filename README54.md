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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2b5e8fa-9133-3bac-84dc-4ed4210ea167 | -9.60607 | -68.55048 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e445c58-350d-371d-b702-9d502c13c4f6 | -9.59188 | -68.50718 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cfbe3ac-9feb-3191-821c-488af281dc6d | -9.58765 | -68.50645 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68fac36c-d92b-3999-a172-306135012575 | -9.587 | -68.53475 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ab5b33-c71a-3532-b484-ac58877d1c51 | -9.56805 | -68.49926 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783fd98c-7100-3f3d-9ff1-6c28934cc1ef | -9.56587 | -68.60459 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 939efc6c-e4e7-305a-bd21-eda62b59fd2c | -9.56386 | -68.60069 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eeffdc1-0cd3-38b2-842e-f4334bd1c451 | -9.56318 | -68.6047 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fda15efd-7b5e-3252-952e-d0330ff70c1f | -9.56162 | -68.60384 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65cb1404-6ec0-3998-9b2c-9623472d02f8 | -9.52983 | -68.59457 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27fbbd47-7b74-3238-b1d7-d39a8accfa2c | -9.52914 | -68.59856 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03172bae-614f-30de-a49f-5e4f42905765 | -9.51166 | -68.4728 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa34e2d7-2ae4-3546-bcf2-ccade0101274 | -9.50322 | -68.47133 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fad7528c-ff99-3060-b799-16b649e47064 | -9.499 | -68.47054 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7429cdd1-9193-34d4-80b5-3126c2f27f0a | -9.49831 | -68.47447 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2543ce0a-d59c-3865-ba58-ffb956cf7d43 | -9.48296 | -68.53682 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5809fff2-633e-3dd9-85d0-31983089b2ea | -9.47732 | -68.56881 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0065b62-6d08-3ac0-aff3-2deb07ea3367 | -9.47661 | -68.5728 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ca1e593-eafb-3231-ac4b-c02d60c19311 | -9.47159 | -68.47775 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5bce9a-9125-3993-b80c-b62369519066 | -9.46666 | -68.48096 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb63935f-fa68-3057-bff4-c9ba43e92538 | -9.46316 | -68.53013 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a3a69c7-5bcb-32ba-9b53-e58ce257ccdc | -9.46247 | -68.52901 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b56bc2e9-6c05-39c3-938b-c4a7a7572248 | -9.46177 | -68.53297 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 360d9498-2c36-30f9-89b5-7a98ae2e0ce1 | -9.45909 | -68.55404 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a730282-945c-370b-b73c-9f46f2e098e7 | -9.45892 | -68.52938 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c710ab1-d256-31e2-9245-778789611ab5 | -9.45823 | -68.55286 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e207d49-ac1f-3254-a724-74aea3926ef8 | -9.45772 | -68.5621 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81704a09-5bbb-3edd-994f-b84a0d0d86b3 | -9.45704 | -68.56609 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91bdf45f-37b7-3840-be1f-841275064ebe | -9.4568 | -68.56088 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b973ac3-d89d-38cb-9699-8729051b5df1 | -9.45609 | -68.56487 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a62edfd5-5abe-3971-8824-3803883b98c0 | -9.43526 | -68.06983 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e4f01b5-749f-3bbd-ad83-b1a2c4d0a981 | -9.4346 | -68.07355 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64e19517-78ea-3c61-9199-b1a3bfe6aecf | -9.41902 | -68.21035 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a1af29f-fdf1-32f6-835b-f8579105c88d | -9.41205 | -68.20125 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b74c0fc2-a634-32ff-ad67-4864a04d8275 | -9.41103 | -68.20208 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa5764c1-8459-3e8c-8caa-e792b6090812 | -9.39587 | -68.29272 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6123547-413f-3f2d-a430-63116b683ac9 | -9.39549 | -68.29382 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cefb165-b032-38a4-8f0e-c23a10913265 | -9.39519 | -68.29658 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f1c061e-8d55-3c76-9575-0c4894827d6c | -9.39484 | -68.29769 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7ee00d1-8436-3f6f-85da-1e0844c53e45 | -9.39451 | -68.30043 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1deae80c-8b18-31b7-a492-2648df0a3011 | -9.39419 | -68.30155 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ee69a0e-4812-306b-83ce-dda2ae429722 | -9.39383 | -68.30427 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14f9566f-dd7d-3e9b-9add-0f18c566b450 | -9.38964 | -68.30355 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f49ec39b-29f2-34a7-8fc3-a723f00b5eed | -9.38935 | -68.30467 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a32c0a1-b641-3a0b-b23e-98452887d9e8 | -9.73819 | -68.41534 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd8e3210-5b79-362b-bdb2-d1211590bbf7 | -9.68535 | -68.59196 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d26d035a-2485-3a69-8db4-acc6995e3299 | -9.68464 | -68.59599 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bebb3739-5e6f-3bb7-80ec-667651fdc686 | -9.68182 | -68.58717 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9979f3-a598-3844-808b-5990aa36090f | -9.68111 | -68.59119 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb118de-e072-3de1-a034-c4a687326d6b | -9.6811 | -68.56663 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de0afcbc-e6fe-3d59-9ca6-559feae5c08c | -9.6804 | -68.57057 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf8ea33a-487a-33e4-9c7c-04727fca04b9 | -9.68039 | -68.59522 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f46c11-b37f-397f-a79b-66f85fc4feda | -9.67745 | -68.56712 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad03b866-28b0-340a-81bf-da44561626e8 | -9.67687 | -68.59043 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16cef159-07a2-3e2c-803b-9faa8f7bda86 | -9.67678 | -68.57107 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3eb6bbb-3de4-3cab-b640-1d8435749a5d | -9.67616 | -68.56982 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db7a718c-17aa-3efe-b55f-e82c397da58e | -9.67407 | -68.58697 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae009a4-8685-36a4-ae94-7c0e002804e7 | -9.67334 | -68.58568 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d13032d6-1573-375f-bd71-a24676a39d8e | -9.67191 | -68.5937 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481ff617-dd39-3834-92ff-9f1e36c4bdd2 | -9.66983 | -68.58624 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 560d87e0-46c1-3b4b-965a-64f10df04141 | -9.66914 | -68.59025 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4a9efec-16d9-3768-95db-05ddd0c50c6f | -9.66909 | -68.58495 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b903d01-967e-37de-9f0f-cba6b89ff687 | -9.66838 | -68.58894 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce56fd0c-c0e6-3a11-8cad-3b55950787de | -9.66677 | -68.55299 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec9b2ca-3827-34b9-bb7b-cc52c6b05bd7 | -9.66489 | -68.58953 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8343772-07f2-3305-a889-c4b23e494fdd | -9.65708 | -68.58405 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55cce8ee-886f-3d2e-b8d3-f8a129fddaed | -9.65664 | -68.51045 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 382ebc52-4163-3221-81fa-625b20a758e7 | -9.65639 | -68.58807 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f44401c9-4c4d-3d76-b2d5-ceda64a6a29e | -9.65489 | -68.57131 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4106fe6c-b042-3e02-8b8d-848a7c81b13b | -9.65134 | -68.56658 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a13d78fb-45f9-33fc-8323-3f557869c2f8 | -9.65066 | -68.57053 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf13f9bc-e95f-3156-92ea-5ba99f351765 | -9.64874 | -68.60715 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5abbede3-f2f7-3885-9d8c-0c428c543504 | -9.64806 | -68.61111 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d243819b-8f43-38fb-85ae-85fa4a22a247 | -9.64642 | -68.56975 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2b0d6e2-0cf9-3bd0-b297-b8f2f96c9600 | -10.88224 | -68.20672 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 570ed44e-8a95-35b6-8dff-c2c0c63b7ee8 | -10.88161 | -68.2103 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1f82c90-9f5f-355d-af7b-417a48320af1 | -10.81244 | -68.82552 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e340121-a455-3cff-922c-d7c22a1e5090 | -10.80901 | -68.82634 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58b2de46-2211-3bdf-808f-22eced9baaa7 | -10.84018 | -69.14024 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf19830-0643-386b-a657-ca5b9a211984 | -10.81404 | -69.01233 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d25a533-c305-318c-be8f-a535a811902f | -10.78315 | -68.92488 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a594de-1a42-36cf-80c0-07e763c0d9f2 | -15.31794 | -52.981 | 2024-10-17 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1d8bee-0eb3-3e9f-9db0-5c0d4fc94aed | -12.36661 | -53.13763 | 2024-10-17 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cf690f9-3fc7-3e45-9ba7-891b5352e748 | -12.36613 | -53.14159 | 2024-10-17 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfa1c708-4197-3332-b736-6996007e4d68 | -12.50489 | -55.1947 | 2024-10-17 05:29:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 643aaf16-b157-3593-9c4b-d250ee5fa327 | -9.61499 | -55.81696 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f64b2f4c-300e-3bf4-af8d-584f4f5ece6a | -9.61432 | -55.81501 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 524005a0-5c03-3ad8-ae5b-eed8987b3d0f | -9.60117 | -55.81536 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1249ff96-192e-3c72-b8f2-d4c5b791e890 | -9.60052 | -55.81993 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 214b797c-2ec8-3a34-8cca-27f0e73f1076 | -9.59988 | -55.81804 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f90006a-94f8-3360-b8d7-e2ebf5ad0417 | -9.59656 | -55.81481 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f947d9b9-d8eb-34e3-920e-14b300bf5aac | -9.59593 | -55.81931 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f9ad9b5-753e-3c4a-ab6e-5ad548569a9c | -9.59528 | -55.81744 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d147b937-79a9-3e7b-bd97-e9eae9acb3ee | -9.57559 | -55.79726 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53ce5269-8cc7-3969-a7af-c9f1616a562b | -9.57428 | -55.80668 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4316ab87-4fff-35b1-aa16-abfe7a0c0caf | -9.57034 | -55.80137 | 2024-10-17 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3c12964-7b61-3436-bba9-17ebb104fb16 | -14.57294 | -56.71085 | 2024-10-17 05:29:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8f02c41-3076-3ff3-ab9a-60a4c940efca | -9.254 | -57.7785 | 2024-10-17 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a8e9b5-1366-37f2-b025-9a023a0b0d99 | -9.28475 | -62.3264 | 2024-10-17 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d3d980-ae16-36ec-b8ab-887329ddfba4 | -9.28421 | -62.3299 | 2024-10-17 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README55.md)
