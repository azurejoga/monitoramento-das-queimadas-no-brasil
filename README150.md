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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d78657ce-69d0-33f0-9272-9519e3f2603e | -11.9254 | -48.0051 | 2025-10-01 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 32d913ab-add0-325a-8960-eb781466290d | -11.4776 | -45.1099 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0c150913-491d-317b-b73a-5f2c40d2aaeb | -8.5267 | -47.2879 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7073e88b-fe39-328a-97fa-800789ce43ac | -10.8433 | -45.3815 | 2025-10-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 57cb64f6-e54e-3a46-8fea-a7f43767e8ba | -7.5749 | -46.7778 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 195.0 |
| d51f384d-4d83-3364-949a-33df9e72a97a | -10.1084 | -50.299 | 2025-10-01 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6e0b5bae-109b-318c-9b4b-a5a557296ee3 | -14.3714 | -45.9172 | 2025-10-01 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ba52223d-4ebc-386e-a901-083a3f5676b9 | -8.6911 | -47.6906 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e1454a39-fec5-3d29-88ba-873a8dee566a | -11.4592 | -45.0664 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9facd634-a986-378c-b24c-05e9b9e68bff | -7.8884 | -47.259 | 2025-10-01 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 343e9e1a-520e-31d5-a579-436fd0c02e08 | -12.7022 | -45.2715 | 2025-10-01 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 192867c2-eeae-39c7-9295-73a8d690796b | -7.5559 | -46.8017 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c9115f76-54f3-3db7-ab6d-78c7cd9a53f4 | -16.0221 | -50.8989 | 2025-10-01 12:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3321df87-2dc9-3790-be1d-156e1e7840a1 | -12.7815 | -50.5758 | 2025-10-01 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 3b5d8d59-cb2f-3bd1-9b9d-5ecccd87924f | -14.4943 | -48.4553 | 2025-10-01 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 720a070c-194f-31b1-99a5-8a47335b91e3 | -14.3519 | -45.9206 | 2025-10-01 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| feb96665-27c5-36ee-80e1-ff863f05bc11 | -12.2536 | -47.806 | 2025-10-01 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 7b5cdbbb-01f0-345b-8f0b-7f97785df593 | -9.9376 | -43.6953 | 2025-10-01 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| ad3369ba-a48b-3771-8e04-79964fc9ed9f | -12.763 | -50.5352 | 2025-10-01 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e01ae24a-dbbd-3739-af72-caf33a1bfd27 | -12.8831 | -46.9101 | 2025-10-01 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ab8da7cc-43d9-324f-a39d-e88818fdb9d6 | -9.9383 | -43.6483 | 2025-10-01 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 4bcb0b86-09ab-3bd9-b56e-ed8d5fd5eaac | -8.8797 | -47.6502 | 2025-10-01 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d7557dec-b45a-3479-b744-23cee04286bc | -8.5867 | -45.4914 | 2025-10-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0c3d1f1e-b78c-37b2-b8b2-4bd999110b50 | -9.9193 | -43.6508 | 2025-10-01 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3c626a96-6f29-3b27-9b83-746745fa46bc | -12.7627 | -50.5567 | 2025-10-01 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 282.7 |
| 3fe6b8a4-2362-316a-940b-c436887ac142 | -11.8482 | -48.0595 | 2025-10-01 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| f8281bcd-8915-3ef3-a9c0-70caec718954 | -14.3514 | -45.9437 | 2025-10-01 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2002159b-ec58-3141-9a31-1b2de2ddcc5e | -9.9186 | -43.6978 | 2025-10-01 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| f816c998-aa1f-36d7-85af-e7dd0d4bd0cb | -11.829 | -48.0619 | 2025-10-01 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7659e86b-886c-362d-a43b-dbfd1a0c5956 | -7.8882 | -47.281 | 2025-10-01 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 299.6 |
| 48ded302-8063-35a8-8c3d-bbb6d914eac5 | -13.2973 | -50.6605 | 2025-10-01 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b40b0ed4-96d1-3108-8a82-9ca65d6d6749 | -8.672 | -47.7144 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1095464e-39b8-3875-a1cd-3b29c776202d | -8.5079 | -47.2897 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 99e194f5-686f-3995-ae2f-d100bee06e2e | -11.8478 | -48.0816 | 2025-10-01 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 5ed36ecb-fded-3233-83b0-d26b53c66d0c | -9.4644 | -47.6124 | 2025-10-01 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2c669f45-179a-3479-a93e-7c7210b82f3c | -10.7864 | -45.3662 | 2025-10-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 52962f49-1520-396b-98e0-260aced31cda | -9.1248 | -47.6256 | 2025-10-01 12:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 1ce03309-c72b-3606-b149-46b7575efce5 | -13.6707 | -48.0476 | 2025-10-01 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9f6defe3-14ce-3b3f-81f3-e172494f53dc | -9.938 | -43.6718 | 2025-10-01 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 2b3b03fe-1d3d-32a0-bad4-2a051b41e7c1 | -7.5746 | -46.8 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ffd68063-0e82-35fd-9406-f0fd23cda298 | -9.0236 | -46.7052 | 2025-10-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2448230b-5a74-3ca8-8ef8-3fd8ac95ae4f | -9.4458 | -47.5923 | 2025-10-01 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d631dc0f-1bcb-3935-b1c9-ef284b4db3df | -12.7002 | -48.5637 | 2025-10-01 12:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d36b0d20-5114-3905-af8b-d547d73832c7 | -11.9411 | -47.0675 | 2025-10-01 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| d90df9fd-ed6c-3043-824f-b6a9fc7111b4 | -7.5561 | -46.7795 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 40799a66-db45-372e-8440-df6c16765029 | -15.5384 | -45.214 | 2025-10-01 12:50:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 72601837-a0c9-3b6d-b824-288dbba8cbb4 | -10.1081 | -50.3203 | 2025-10-01 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 79ef072f-6278-31db-a1b7-bc22762131b0 | -8.5587 | -44.7414 | 2025-10-01 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b2b41147-58c1-347a-9f25-4356f0f638ca | -13.6703 | -48.07 | 2025-10-01 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 6100d344-65cf-374b-b318-22a4d42fc432 | -11.1757 | -47.2134 | 2025-10-01 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b0201ef2-d890-3db5-994b-fd151f36a5c9 | -8.2105 | -47.0084 | 2025-10-01 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a789cfe0-7497-3473-a953-2611d0cc82e7 | -8.5864 | -45.5141 | 2025-10-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 53f0c175-7f48-3945-9646-3fe595afddcb | -11.8622 | -45.0075 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 2400cf62-63f2-360a-b039-1eaadc1e3462 | -8.9115 | -46.6276 | 2025-10-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f898e14e-4473-3e15-8c0f-516edab5ccc5 | -9.4115 | -47.3308 | 2025-10-01 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 6f65d53e-b39f-3724-86c9-ecf08ba8b0af | -7.8165 | -46.9781 | 2025-10-01 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cf6449ac-43d9-35d4-8bac-03e8595a6f4d | -10.7074 | -46.7581 | 2025-10-01 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 271cd9ea-fe26-3c2b-995b-a7a68e084316 | -7.8353 | -46.9764 | 2025-10-01 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ee83a52c-2548-33ab-bd60-917d583d0592 | -9.1889 | -48.5166 | 2025-10-01 13:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 14bfbc53-c09a-3e00-86a2-45ef19f2d5e3 | -7.5749 | -46.7778 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 251.7 |
| e5450cf9-6ded-372d-b39d-5d9254649d13 | -13.3808 | -48.0908 | 2025-10-01 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 33a2a940-1534-3239-9f51-a548d304c022 | -14.3714 | -45.9172 | 2025-10-01 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f9eab148-55d9-35e4-bbcd-f31b0971ba96 | -15.5379 | -45.2375 | 2025-10-01 13:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c196fa05-71bc-3e90-a9ba-7bf2be60b15e | -8.5404 | -44.6975 | 2025-10-01 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6e94e52e-d499-3f0d-bc53-45b73d8ca8cc | -12.7022 | -45.2715 | 2025-10-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1f3aa3fe-9461-3513-8eab-95b5c7c65e23 | -8.5407 | -44.6745 | 2025-10-01 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 87b2899b-62ce-357a-bb2f-971b513e397d | -11.7797 | -47.5806 | 2025-10-01 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 211.4 |
| b8124e8c-d1cd-3c5e-96d2-6b51445aae06 | -10.7864 | -45.3662 | 2025-10-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 93517a45-ae90-35ef-8e92-1d3cd137de7d | -9.4458 | -47.5923 | 2025-10-01 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 142f7778-0382-3191-aab0-01f1b40a5442 | -13.3278 | -47.8313 | 2025-10-01 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a2c70512-398a-37e8-82ee-14f64a387ddc | -11.9272 | -47.8941 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b5541ea3-5496-36c5-ac96-5dc677830f02 | -9.9383 | -43.6483 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| ebfdff8d-c6c7-3dd5-8eed-fbaea485ebbf | -11.8673 | -48.057 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 023fca2c-8ded-3b57-961b-281707746f85 | -8.5079 | -47.2897 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 0347e497-31f9-33da-8dd4-a3dc7d040483 | -10.0337 | -50.2424 | 2025-10-01 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 26a9bc41-57f3-31a2-8754-c33b7c939907 | -8.2105 | -47.0084 | 2025-10-01 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 02b41a78-2a63-3c2e-81c8-d0530215ef53 | -8.8926 | -46.6296 | 2025-10-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5e7d95d7-ae8b-3398-98bb-23b78eee67db | -14.3519 | -45.9206 | 2025-10-01 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| b30b158f-535d-3277-98d7-d157cb69f800 | -11.4405 | -45.0461 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c5c39219-90f7-3591-8721-7f6bd17c0ff9 | -15.5384 | -45.214 | 2025-10-01 13:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f9a2f35c-c6ff-320a-b040-95551775f9eb | -8.6911 | -47.6906 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 418fd555-d029-394d-8915-b557c18a7364 | -9.8845 | -45.9576 | 2025-10-01 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f9f2901a-23bc-319b-ba43-3b3461fb462b | -8.483 | -47.7983 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 1edba359-019c-3ea2-92e6-eb3a23f42064 | -11.7793 | -47.6029 | 2025-10-01 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 3d4a1d5d-38f8-3241-be2c-8df54f4dc0b6 | -11.9258 | -47.9829 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ab7dd9be-258f-313b-b14d-55574ceed800 | -14.5133 | -48.4745 | 2025-10-01 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3e5c8c4f-c6e4-381e-adb4-01cd99f9c2b4 | -8.8929 | -46.6072 | 2025-10-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3c5e6c90-fbe6-3f53-b4f5-d84ea765eaf4 | -11.9411 | -47.0675 | 2025-10-01 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 99ca9294-3465-36b7-a216-7d82e7e10cd6 | -8.5018 | -47.7965 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c3b1a72e-23fe-3881-aa11-81b4cea3b649 | -13.0307 | -45.2189 | 2025-10-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 4e9853d3-43a4-3f72-b098-be133de192b8 | -13.4736 | -47.2489 | 2025-10-01 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b018a9a6-5f0d-3ce2-81a2-de21e13a3b89 | -11.9063 | -48.0076 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c8b4a9e7-f91c-33b0-8338-ead843e15b24 | -9.938 | -43.6718 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 4af6a820-f2e2-3ecc-9891-ef841665e249 | -9.1248 | -47.6256 | 2025-10-01 13:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 1e66fb3c-f589-3bd8-b5ba-a00f79d45c67 | -13.2973 | -50.6605 | 2025-10-01 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1a95f8bf-8acd-35b7-8043-834e571ae396 | -7.5746 | -46.8 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| cf1f45e9-b6b0-3832-9161-14abf59c8fc7 | -11.8482 | -48.0595 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| d65abeb7-2f2d-3acd-9b3e-5ad8f2a5e611 | -7.5559 | -46.8017 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5c7f623e-faf5-33ed-bb59-dd091406d7b7 | -13.3615 | -48.0936 | 2025-10-01 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e48a2c59-1fc8-3727-ae3b-7477b82bac1a | -14.4943 | -48.4553 | 2025-10-01 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |


[Clique aqui para ver as próximas entradas](README151.md)
