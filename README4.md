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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb74fbc-ee39-3870-830e-0ae5b6883e1c | -8.0696 | -43.1452 | 2025-07-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| b620a93e-8b26-37dc-be3c-ec5808d08690 | -7.9259 | -44.0706 | 2025-07-25 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9b04a9c2-2b39-374e-abff-fccd41d703f4 | -8.0883 | -43.1667 | 2025-07-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| d3520665-db49-3d0b-b060-f3dffc7fd839 | -8.0886 | -43.1431 | 2025-07-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.2 |
| 993ca991-8bd2-3a77-aef9-801812315897 | -7.907 | -44.0725 | 2025-07-25 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 7f74aa16-055a-305d-b641-aca9125867b6 | -6.9422 | -44.5562 | 2025-07-25 01:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2c5d1331-efc3-36c9-b43b-3ee594575c06 | -10.6438 | -44.7645 | 2025-07-25 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| cfabbdff-4444-3895-96c9-ff7a3ba941f7 | -2.9108 | -48.254 | 2025-07-25 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 602964ca-ff44-33cd-9ed7-5de5dc19faf8 | -11.9516 | -58.7771 | 2025-07-25 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b61b8e97-a258-3589-aafb-0327217c21ec | -14.9518 | -46.9845 | 2025-07-25 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c3c5ab1c-25db-3a24-9a69-fabdecaf5499 | -6.9607 | -44.5775 | 2025-07-25 01:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| cfc8424a-a28a-3a84-8485-4a72370241ed | -11.9518 | -58.7574 | 2025-07-25 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 56b86f38-50f1-3fac-af05-e6654d24d651 | -7.2597 | -43.0645 | 2025-07-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.7 |
| 737e18b1-bd51-355f-a946-089d381933e5 | -7.9256 | -44.0937 | 2025-07-25 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bc59df29-c987-3c24-b4fe-520bae55ab7a | -11.4584 | -45.1126 | 2025-07-25 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 020d6a2d-6159-3a28-bced-3ecdb9134a3b | -11.9329 | -58.7588 | 2025-07-25 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 20db6077-1fe4-38e0-be59-a050c15a5eec | -7.9068 | -44.0957 | 2025-07-25 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| aebc21c7-67ff-3cf6-b6d3-c17537c24b97 | -6.961 | -44.5546 | 2025-07-25 01:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 5677eac1-85a2-3b31-9e80-919600f19baa | -21.6486 | -54.0324 | 2025-07-25 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ce95bee8-3850-383e-93cd-570b2ac319b4 | -7.9259 | -44.0706 | 2025-07-25 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8d96e0d5-7708-31f2-8354-511bf91fad23 | -7.9256 | -44.0937 | 2025-07-25 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3e581a0f-b894-3dee-b15f-29df46128c6f | -7.9068 | -44.0957 | 2025-07-25 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b1804d89-db88-3ced-99ec-97efa6544599 | -21.628 | -54.0362 | 2025-07-25 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 139c8b91-956f-300b-a561-15ccf71befa9 | -8.0696 | -43.1452 | 2025-07-25 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| e1534829-2d6c-39e1-9d0b-4b2c7a96f02a | -8.0883 | -43.1667 | 2025-07-25 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| dc1c5c1d-5313-32d7-a007-51714fc441e5 | -11.4584 | -45.1126 | 2025-07-25 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 14264212-0262-3405-985b-ca549b920801 | -6.961 | -44.5546 | 2025-07-25 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a1cb3358-7247-3d84-b1de-af4e5f78886c | -11.9516 | -58.7771 | 2025-07-25 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 8ac8f8f4-92a0-38b0-b607-e50d68708688 | -10.6438 | -44.7645 | 2025-07-25 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2f9ddcdb-2535-3a50-9ab7-25a4cb54decf | -11.9518 | -58.7574 | 2025-07-25 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6ba59578-101e-3aea-86c6-78cead548a53 | -7.2597 | -43.0645 | 2025-07-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.8 |
| ca4828b2-f760-3306-9601-4f3520ef2700 | -14.9518 | -46.9845 | 2025-07-25 01:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0851bf14-2914-3d2b-86ae-34b9295d3e5f | -8.0886 | -43.1431 | 2025-07-25 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.9 |
| aac3e987-8537-3bf7-ac84-214f228f899a | -6.9422 | -44.5562 | 2025-07-25 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7ae7b82e-c473-3469-9624-007c7564652d | -11.4393 | -45.1154 | 2025-07-25 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2468255a-723f-39c6-8e32-90c34f8e180a | -11.458 | -45.1357 | 2025-07-25 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 09d2e36f-37a8-3937-96d1-bc40e3fb15e1 | -11.9516 | -58.7771 | 2025-07-25 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 5ed8f922-d282-349f-b1b4-128dc7d6e22e | -11.9518 | -58.7574 | 2025-07-25 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 58520f65-bbf0-373c-a640-5a1b4d346d61 | -21.6285 | -54.0143 | 2025-07-25 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 97ce0475-5688-37ec-ac16-be556480bc21 | -14.9518 | -46.9845 | 2025-07-25 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 34b19f5d-cafb-350c-aa67-95a5a8d17da7 | -11.4584 | -45.1126 | 2025-07-25 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 35ca081c-f34b-3d81-a502-f68e6790e633 | -8.0696 | -43.1452 | 2025-07-25 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 05a15a9e-b912-37c6-8115-77dd66aeb1c9 | -8.0883 | -43.1667 | 2025-07-25 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 744d8e04-a46f-3d3e-b481-a8db5f5a1f2b | -11.458 | -45.1357 | 2025-07-25 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2bd7e65b-7f24-3d5d-a030-fc7bee22c827 | -8.0886 | -43.1431 | 2025-07-25 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.0 |
| 7c730c5f-b5b9-3d05-bafa-0c66e4439044 | -6.961 | -44.5546 | 2025-07-25 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1e5cc6dc-9303-3f98-af81-f4f2dd144b72 | -7.9259 | -44.0706 | 2025-07-25 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 402d7da3-dc3e-3b02-809b-ceb6b447b388 | -6.9422 | -44.5562 | 2025-07-25 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3c78b9d2-0aae-32aa-805b-da914a97349e | -7.9068 | -44.0957 | 2025-07-25 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 18377b0e-9f3a-3c1d-ad02-e570ebe9f2ef | -10.6438 | -44.7645 | 2025-07-25 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 99ed50c0-f4da-337e-affb-958de7062cb3 | -7.9256 | -44.0937 | 2025-07-25 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 90e74de8-93bf-30bd-a367-6a90c237bf9c | -21.628 | -54.0362 | 2025-07-25 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 8f846893-50b1-345d-820a-50c721ccac4b | -14.9523 | -46.9616 | 2025-07-25 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| dc726b1e-9374-3c66-9426-e6f36488c107 | -11.4393 | -45.1154 | 2025-07-25 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 4f1da0e5-51e8-3e1c-bf22-a00e38ed2856 | -21.6486 | -54.0324 | 2025-07-25 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 9db99e3f-56a0-3f98-88d8-95b460750e01 | -21.6491 | -54.0105 | 2025-07-25 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 98.2 |
| de598c03-adb2-3bdc-80f1-dbdb7c95d4da | -7.2597 | -43.0645 | 2025-07-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.3 |
| 516a041e-6b6b-3d7f-ad6f-78c5d49ff8f3 | -11.458 | -45.1357 | 2025-07-25 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 29a1fafc-823c-36fb-b96a-75a5b60ad722 | -10.6438 | -44.7645 | 2025-07-25 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1d664bbc-a550-3966-9e28-4ef4e896071a | -8.0886 | -43.1431 | 2025-07-25 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| f387eb3b-0f71-37df-9752-c3ce6561e3e8 | -11.4584 | -45.1126 | 2025-07-25 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 738c5dc1-cdc7-371c-97d5-6e7e4993307f | -7.9259 | -44.0706 | 2025-07-25 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ca035d13-bd55-3f5b-b9cd-009382c2a9f9 | -14.9523 | -46.9616 | 2025-07-25 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| aa4da9b2-9627-36b9-adc7-ffb1216a9d42 | -6.9422 | -44.5562 | 2025-07-25 01:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 70563426-8d62-33d5-90c2-f94b36c2f410 | -8.0883 | -43.1667 | 2025-07-25 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 5d1eea12-f06f-3408-8b3e-ab0f28b78c96 | -11.9516 | -58.7771 | 2025-07-25 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 9a75441e-81f8-319e-b9dc-504b42ae3c29 | -7.2597 | -43.0645 | 2025-07-25 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| 956cfde3-ad48-3b61-b2c6-7c3d8fd83b86 | -21.628 | -54.0362 | 2025-07-25 01:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 78edc573-83c9-3747-81f7-e6f83fc5880f | -6.961 | -44.5546 | 2025-07-25 01:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a6f6dc43-dde4-3351-9905-947e5e033267 | -21.6285 | -54.0143 | 2025-07-25 01:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 829237e7-eac1-369f-ac9d-82b92266f13e | -7.9256 | -44.0937 | 2025-07-25 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| e993acb8-ce6f-32fa-bfc6-b967b729cfc5 | -14.9518 | -46.9845 | 2025-07-25 01:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 562f92f7-8ddb-3078-8b46-c4c4cff6ef79 | -7.9068 | -44.0957 | 2025-07-25 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9319f1fc-58f4-3723-a9b1-95669710f508 | -11.9518 | -58.7574 | 2025-07-25 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 76a0e06f-2a65-3f80-8702-84ad4a777eae | -8.0886 | -43.1431 | 2025-07-25 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 77ad2fae-32f6-3b48-b24a-11ef961f99ae | -7.2597 | -43.0645 | 2025-07-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| db7338ea-521e-3e5e-94f9-d2792f60751f | -11.9518 | -58.7574 | 2025-07-25 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fb72b541-21da-3f67-a5b8-3dc6ef55347d | -7.9068 | -44.0957 | 2025-07-25 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f16aca3b-0fe5-32d0-b180-7a63e559a30d | -11.4584 | -45.1126 | 2025-07-25 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| df7dc070-6259-3d6a-a653-c066308d5e9f | -14.9518 | -46.9845 | 2025-07-25 01:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f163199b-17e3-3f2d-b262-6899ddf6032f | -11.9329 | -58.7588 | 2025-07-25 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 1e7a1515-7529-3cdd-894d-0644b73b459b | -11.458 | -45.1357 | 2025-07-25 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c9ca0aaf-c76d-3cc5-92e0-68bbc408b7c2 | -7.9259 | -44.0706 | 2025-07-25 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 833c8f4f-e22b-3766-a706-862fe5fa1524 | -7.9256 | -44.0937 | 2025-07-25 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 04c65b1f-fc3d-35f0-8fb0-0cfd21f25abe | -7.2597 | -43.0645 | 2025-07-25 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| adccd250-6c0d-3bd2-839e-f6f83c29b2e8 | -11.4584 | -45.1126 | 2025-07-25 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 1b0c3932-eba2-3fa3-ac88-4083c67f8e74 | -14.9518 | -46.9845 | 2025-07-25 01:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| de902d78-edf1-3916-8ea2-c4cacb8bb373 | -8.0886 | -43.1431 | 2025-07-25 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| ca482119-e465-3781-8cee-a6a98b72afb0 | -11.458 | -45.1357 | 2025-07-25 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9778f0a1-286e-30cf-81d1-e3b4b0fcf083 | -6.9422 | -44.5562 | 2025-07-25 01:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3abc7b46-99f9-3038-baf7-330f90d8ccb6 | -7.9256 | -44.0937 | 2025-07-25 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6998a6c8-799c-353f-86e6-7a65330d9a61 | -8.8308 | -45.5788 | 2025-07-25 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 6b7137fb-68f2-3219-8a5c-4fc87f19c9f7 | -7.9068 | -44.0957 | 2025-07-25 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 95508a23-0c65-3f7e-bd94-1e1a8c586db4 | -6.961 | -44.5546 | 2025-07-25 01:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 317e24ba-567e-3421-8f61-3576ce07859f | -11.9518 | -58.7574 | 2025-07-25 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4089ac4f-e1ef-3926-94b9-28697a970172 | -11.9518 | -58.7574 | 2025-07-25 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e19ac1f6-fff5-326a-9be3-2f2ab012dc56 | -8.8308 | -45.5788 | 2025-07-25 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7a1a202e-a5bf-3f8a-955c-31dd517232f8 | -6.961 | -44.5546 | 2025-07-25 02:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3d49cb4f-61da-3496-8273-082d7a012845 | -11.4584 | -45.1126 | 2025-07-25 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 0deea868-5fb8-348a-a8d2-784efb0541cc | -11.458 | -45.1357 | 2025-07-25 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README5.md)
