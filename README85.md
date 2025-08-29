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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbbb1ac0-f8f4-364b-acab-b55187568fbb | -9.17421 | -59.45393 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 187763d3-8c45-36ba-a249-945f060d29d1 | -9.46886 | -60.56665 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0df48ac9-d0e6-30f0-ac41-863459551880 | -9.45381 | -60.57226 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be535d8f-2c90-3edc-b3bb-fe02b9b909ea | -9.15905 | -59.58516 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4fb777-b017-3ed7-8eee-53933d7e5838 | -10.85553 | -60.8117 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb589261-2cb8-3dc1-a2ed-8946f6b98ad9 | -8.77104 | -71.30449 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c513b465-3dc8-338b-ba05-72b2695a7688 | -9.12673 | -65.76625 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c27667c-83d5-3e15-852f-f4ee932ea1fe | -9.4171 | -60.56711 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5aff246d-da6f-39a7-b9ae-1bd52d378a7c | -14.50686 | -52.06758 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d882903-ec44-3bd7-b7b8-ab0ec2668a05 | -9.77723 | -64.25039 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 861dc223-129e-3527-92fe-0a8c3963dd27 | -10.36398 | -57.8002 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6d8cc8e-aa49-3884-9c1f-60ae68c9e1f5 | -9.18819 | -67.75621 | 2025-08-29 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7adb0198-6d84-397e-b468-decb1c118cd0 | -9.11129 | -65.79316 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4079876d-0190-384d-a6e6-49a3468cd74d | -10.4539 | -59.12214 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6d9efa0-e8eb-32c7-b0a2-55f03a196a2a | -10.2891 | -64.48942 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdbe0104-2a3e-36ed-9efa-682358caf941 | -10.62148 | -54.91355 | 2025-08-29 05:29:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52f9cd8a-c4b4-38b1-8eca-e0bbe784e8f0 | -9.1555 | -59.57746 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 941472bd-3a75-37cc-be27-146f22df1ab7 | -9.75771 | -67.53387 | 2025-08-29 05:29:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a239f9f2-8049-3149-b548-91d51b06a8be | -9.53728 | -65.69281 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e4ab8a48-4669-3348-8d0e-92f3094de1dd | -9.16875 | -59.56947 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cecc6ce-1d8d-372b-ae19-4b65eb1db5a6 | -9.16026 | -59.5769 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da2f8284-95df-3d67-bc5f-5381b9a254a9 | -13.4212 | -46.9637 | 2025-08-29 05:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4fa64fa3-b090-379b-88a7-dcb107b1bbd5 | -9.462 | -60.549 | 2025-08-29 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| eb94c7f5-9490-37e0-ae12-42668eb2f3e5 | -13.4208 | -46.9864 | 2025-08-29 05:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 88e6d55d-3847-36ac-a705-f5dca0c821ea | -9.7728 | -64.2657 | 2025-08-29 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 044f2f51-3e03-3ad8-870f-351f8b19b0cf | -9.1155 | -65.7699 | 2025-08-29 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d8c448f5-12f8-3f3b-80bb-c7c5a8010cd0 | -9.4618 | -60.5682 | 2025-08-29 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| fa83e05a-d4f3-3cc6-bf6d-a936d6d0ce79 | -9.4433 | -60.5499 | 2025-08-29 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 81afd70d-eec5-31e1-9e96-c9881d82bc35 | -3.7693 | -54.8286 | 2025-08-29 05:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9f483a87-48eb-3f9e-861f-bf93a30219e5 | -3.4254 | -49.0517 | 2025-08-29 05:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4d93213e-67ee-3b1f-8de5-2aa3cb416013 | -9.4432 | -60.5692 | 2025-08-29 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7c8116dc-6c52-399a-b161-7ccc2b276274 | -9.773 | -64.2469 | 2025-08-29 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 33766e91-2ca1-3ea6-a8ab-982f33eeeaed | -9.1154 | -65.7886 | 2025-08-29 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 44cb46f1-fc66-30b1-845e-864a9d2bd09b | -14.78918 | -59.7283 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67399b3e-6a39-38e7-aed1-8f99423cdeb1 | -14.78018 | -59.7366 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bfd657d0-cd9d-3aed-bf17-aec1fb2c5835 | -14.58654 | -54.52355 | 2025-08-29 05:31:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 796f7b46-71f2-30bf-b01a-f77ea79c91a1 | -14.79494 | -59.71497 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e4384b9-01e9-35fc-a1b7-aad244133b9a | -14.78141 | -59.72768 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f66baf7b-30e7-30b5-ac0b-9f5c19d1b638 | -15.16924 | -52.33094 | 2025-08-29 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35837643-d7db-343d-a59c-68dd3f074119 | -14.78979 | -59.72385 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bfe67580-32b7-3de9-bbe9-a6bd5f4cc837 | -14.77117 | -59.74515 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3427104-74c8-3a82-810d-70968a6a0aba | -15.16879 | -52.3352 | 2025-08-29 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a14ebebd-f4a0-36f0-9ea5-d6a3c0dd5e05 | -15.533 | -54.27013 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50744aab-bd00-3b87-b70d-cf0b76072541 | -15.16836 | -52.33934 | 2025-08-29 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2c94936-650d-3fa9-a98f-e13f80dc4504 | -14.79173 | -59.70966 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0081a593-67b9-32e2-bfb6-f34ffc16abc2 | -14.78529 | -59.72801 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a71dd0cc-10af-369b-b361-58a4d00e3e11 | -14.60527 | -54.50434 | 2025-08-29 05:31:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e93c3203-60e2-3ee7-bd7d-9d11b07abd47 | -15.5373 | -54.26955 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2896e400-944e-3424-b66a-3c147d95c2a0 | -14.60023 | -54.50025 | 2025-08-29 05:31:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a7c9e1e-a63c-3210-ae2d-e18087a4af4d | -14.79041 | -59.71931 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6cf0fe27-2d6a-3837-b2eb-c0532ce3a485 | -14.79431 | -59.71955 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba5a4f96-f0af-3f94-85cb-c66cb08ba355 | -15.54246 | -54.27412 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ddcf624-6838-314b-9780-33f5895b447e | -14.77567 | -59.7409 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7648b0e3-a830-31d6-b969-86fc114f5225 | -15.53859 | -54.27073 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a17bfce3-fc9d-33e8-a478-c348ec7b0b6f | -14.60568 | -54.50074 | 2025-08-29 05:31:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5034f6eb-8f1e-3de7-b860-99dd0bce263f | -14.59197 | -54.52417 | 2025-08-29 05:31:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 976afd0d-de7c-30c5-96a3-fe5c29f60305 | -15.53813 | -54.2747 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b78e41e-c588-3fbd-88e7-8c67a0a35701 | -19.14545 | -57.79081 | 2025-08-29 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6291a7c0-acdc-3265-8c2a-2619cd111746 | -14.77629 | -59.73638 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 476f162d-93de-3445-ace6-d93ab0781926 | -14.7808 | -59.73212 | 2025-08-29 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba2b221e-698d-3d39-bde1-351c6e19d189 | -15.53172 | -54.26894 | 2025-08-29 05:31:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3c366d1-0e82-31bb-860d-fc254b9ac600 | -28.73114 | -55.64963 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 84fd4caa-dd01-3d0d-a3e6-8d923f640214 | -28.73051 | -55.65909 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 8f10936b-1496-3843-9943-0785ba0ab9e0 | -28.70235 | -55.58731 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 33f0d96c-59d4-3318-a79e-88cbaa4f9bbb | -28.70269 | -55.58246 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| f4f7beb2-0255-3be6-aa74-bead0c2fc7fa | -28.73675 | -55.6549 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 36cca16e-1116-3717-adab-bb53a8e0e6e6 | -28.7377 | -55.64076 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| e43f819c-ba99-332e-8ce7-b9441d82e6e1 | -28.73417 | -55.64352 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 5e1cf050-8891-3a45-ad0b-ad29acc01812 | -28.73383 | -55.64821 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| e26f62b7-5100-335d-b104-4f86dc252433 | -28.73314 | -55.65765 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 1d0c02a1-3768-3839-8a40-1eb62fba9f1c | -28.73145 | -55.64493 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 07a24f3b-226e-32a6-aa8e-4a1057147987 | -28.73349 | -55.65293 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| d388c7c4-cb98-3c92-987d-313269509ba7 | -28.73176 | -55.64026 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 9fcb9b39-b46d-3138-9226-35aada5c4760 | -28.73451 | -55.63884 | 2025-08-29 05:33:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 0e215807-e1f4-330a-bcc0-a8e0632bdc28 | -9.462 | -60.549 | 2025-08-29 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3e04299f-8e75-3e43-b6c7-054d9cdd2ed3 | -10.3812 | -57.8245 | 2025-08-29 05:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e9cbacba-b8a3-3f89-8664-57a656964aed | -9.4433 | -60.5499 | 2025-08-29 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0e0c16af-6bde-3d6c-b501-70385bbebb4b | -9.1154 | -65.7886 | 2025-08-29 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 390aca63-a453-340d-a6bf-45f1cdd8e7b3 | -9.773 | -64.2469 | 2025-08-29 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b0625dde-8cec-3c56-8552-c1fff658add7 | -13.4208 | -46.9864 | 2025-08-29 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9a9bdb21-13c4-3419-9510-817a61eba699 | -9.7728 | -64.2657 | 2025-08-29 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c19f9cbc-f408-3b18-9f60-96d4013cd092 | -9.1155 | -65.7699 | 2025-08-29 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 023aa7c9-36f7-3afc-9f95-dc8de6006c5a | -10.9709 | -46.9266 | 2025-08-29 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5ce17153-fa88-363d-9f3a-5fec00669891 | -3.7693 | -54.8286 | 2025-08-29 05:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2e63c4e4-2f6c-3af8-a4f3-2fe29ecac212 | -3.4254 | -49.0517 | 2025-08-29 05:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0c6fef16-975f-3798-99ec-5b00ef9bc74d | -13.4212 | -46.9637 | 2025-08-29 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e0532630-a6ba-3971-bb54-8aa3ffea9fd8 | -9.4618 | -60.5682 | 2025-08-29 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4d45245e-28ed-39b3-9b58-2f5f5d054018 | -10.99 | -46.9242 | 2025-08-29 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bba28efc-8b0a-336f-b635-fdc62603dc42 | -9.4432 | -60.5692 | 2025-08-29 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c02317f2-ab98-3c29-8228-a637b238a0b2 | -9.4433 | -60.5499 | 2025-08-29 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 9a54225d-1fff-34bb-9547-99e2cd299ced | -9.7728 | -64.2657 | 2025-08-29 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c4c1941e-9cf4-320d-b151-52df3d8a0f85 | -13.5386 | -46.8775 | 2025-08-29 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| dcce6ff6-fb29-323c-9ffa-c4925f1e601b | -9.4949 | -45.3906 | 2025-08-29 05:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d8fa6fae-5efa-39a8-b25f-400e32d7989c | -3.4254 | -49.0517 | 2025-08-29 05:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c49e65df-49b8-3a0f-9c4d-388b136c3474 | -9.4432 | -60.5692 | 2025-08-29 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 13a9b889-b9e4-323e-be44-8ed7f494d26a | -9.1154 | -65.7886 | 2025-08-29 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| cf9e598a-d3d6-39aa-ab2d-9bdfe99132b6 | -3.7693 | -54.8286 | 2025-08-29 05:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 52be2d4e-01bb-3952-99e6-6c9e45735c1f | -9.462 | -60.549 | 2025-08-29 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 314f96b9-d48d-3d78-8f9d-02831609001b | -9.4618 | -60.5682 | 2025-08-29 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 8543fc4f-58ba-339e-95e0-116e3ce56491 | -9.773 | -64.2469 | 2025-08-29 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README86.md)
