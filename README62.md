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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 801bcb59-10ea-34f0-94a4-d1039c21efa8 | -12.21221 | -43.74705 | 2025-09-28 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6291ce81-cfd2-3a8f-aca6-7ac899814ed0 | -8.82989 | -46.20509 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc0460dd-22ef-3abb-9b72-0f91db8f6742 | -5.21363 | -50.95485 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b28c98f3-9f2e-359f-93d3-3e619eccfd53 | -9.09925 | -45.82596 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44b6f4cc-fb92-348c-8032-534730b71d9a | -11.85429 | -48.23468 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8e293bb-3088-32c8-897b-54dcc2a4bcbd | -12.97968 | -46.84784 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc516ca5-c3ca-3b6e-a136-8d46e88c6b62 | -8.27496 | -45.44997 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33f85ae-eae8-389b-bbd0-736bcd730b8d | -6.61919 | -43.82915 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 532bc8a9-c9b2-38c5-a6ef-76660e0c21c5 | -6.4214 | -43.51604 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2026d1a7-ab40-3dde-8105-548e421fdc3c | -8.71686 | -47.98333 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74a61c81-0961-36f8-9280-dbc28510888d | -11.94289 | -47.9368 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd43e8f4-90d1-329f-9fea-e97a7a0d01e5 | -6.77997 | -44.07981 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e3e01a0b-f708-313d-90a2-2f42e4128ca6 | -10.41708 | -48.15245 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbbb9d6a-e164-3d8b-bc6b-ac0a2a48c2b6 | -7.37149 | -47.03154 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc084773-4ece-3e1d-831a-f32331db5b72 | -11.35605 | -44.99854 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f0b89a5-5412-3c39-bd88-e2fd4ba840b0 | -7.94353 | -45.68547 | 2025-09-28 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 748a0488-9f45-39a0-991e-78c920485b53 | -7.85341 | -43.79745 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2a94a336-6a29-30fa-9d84-2ee59a282506 | -8.16672 | -46.4281 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 916ebf86-646e-3697-869f-fe5f1af07bfd | -6.15427 | -42.81055 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b054a21-c39f-3f61-a1bb-f7e06479296d | -11.44039 | -48.68946 | 2025-09-28 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1b22f788-872a-303d-a997-0f8ca142d872 | -11.52155 | -54.31094 | 2025-09-28 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fff812d5-8810-3b05-acc7-bcf5ae2f75cb | -7.75657 | -47.0037 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d2bb6f5-8400-315e-abcb-004d0d7199cd | -11.6472 | -52.87185 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e28eeb17-712c-3836-a349-e218ef9991e7 | -7.17655 | -41.71096 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c6f9c93-b08c-39dc-b3af-2243e8b92372 | -7.53782 | -46.1083 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24154e77-81ca-3577-ae1a-bde569c48db8 | -11.85762 | -48.23523 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0ee467-1576-3124-80c4-98f81e527616 | -12.29854 | -45.64602 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5889c9dd-6603-3ac0-ac8e-3d320affe818 | -11.41579 | -44.90758 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78e4847f-8fc8-3ba7-8bad-648bcfcc6681 | -7.80448 | -47.02206 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2639d026-2586-383e-9160-706d6844736b | -11.35671 | -44.95923 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3c0ad02-de90-37dc-969f-5636fead62af | -7.23375 | -44.77153 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0276ea11-8db5-385d-a459-bf5e67179d05 | -11.44173 | -44.99575 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 211daef7-1ba0-3d75-8b74-48c4cd3d94ab | -11.36654 | -45.04754 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f005ff5-4102-30ef-bb52-f6ddf94fb6dd | -11.51463 | -46.94816 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0666485d-d7e1-3601-9ad7-207ea18b33b9 | -11.14436 | -54.30923 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c323bbcf-7ee0-3aea-8ec4-6923fe43bb67 | -5.9694 | -46.44777 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7da559f9-698f-38a0-8dcb-89f0f604e58e | -8.16832 | -46.39635 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d012fed9-1ac2-3f38-862b-287daaa54447 | -12.00104 | -47.0947 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 775d2091-3e48-3c26-871a-e84e2d8fa522 | -12.88958 | -47.09978 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f6261b-49de-3d11-96eb-62b18a067ee3 | -7.30691 | -42.94962 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9aebcfe8-00cd-3b69-b9b9-3f99b4e4803d | -6.61208 | -45.88379 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e6a176e-5d7b-315d-9080-e22ba2cbeaca | -9.33458 | -48.94723 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a7188bd-be42-34ba-aa6e-3ccca71247f2 | -10.44931 | -48.20106 | 2025-09-28 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63b8f82e-49ea-38e2-b277-236b6989a798 | -11.44055 | -45.00354 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9226187-54e0-3e5c-ab27-de7dca84cbed | -7.31122 | -42.94589 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b8874dd-e526-3642-8f69-6cdfe1a13921 | -10.32443 | -48.17398 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5932f066-aa37-334e-9c42-e5a62d01335e | -13.24865 | -44.11392 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb523957-a338-3f48-acf7-dd12e15206a0 | -6.70824 | -44.59119 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35b0f9e8-fc49-3b3c-b794-80bb7717cd02 | -5.82615 | -44.43117 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f86dcc94-4042-3da0-95e5-27d099dd9c5d | -5.95199 | -43.32379 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ec0e7c4c-7091-305c-aa04-61a7a7492aca | -6.04706 | -44.76402 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ac1914-acd9-37fc-85b7-52f810986fea | -11.99828 | -47.06897 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51594fc4-6adb-3de8-8f43-537c957c470c | -5.45331 | -46.61843 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1118279-3ba2-3696-9462-bea13d9f647f | -8.17388 | -46.42569 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16372b72-d0de-3662-91d1-b9dd5453f0ed | -7.78143 | -47.01841 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1baed2e0-b90f-3a67-a5cb-97658ebe0a6e | -11.66322 | -45.334 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e9b9044-04d7-38ca-8af2-ef389f8a25a5 | -11.43474 | -45.01854 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d55339f6-6299-32ae-b30a-a199b6eb8edb | -9.11993 | -46.67258 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04d0acff-b7e7-3efd-9f41-f3559bd18c37 | -11.99128 | -47.95182 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d13f364-5556-3a8e-aa53-8b26157c2f0b | -11.99165 | -47.88683 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b46f010e-4031-3f26-80cc-88ba0d877703 | -7.76152 | -45.72164 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab6b438a-eb7f-3f97-9d60-f0e9e9c06f02 | -8.1689 | -46.41424 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 82a2315e-810c-3f14-b0bf-608b13a64e12 | -10.97194 | -49.5706 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1cc4c6b-dfb2-39d6-b3cd-5ab5ff276d2e | -6.27375 | -43.63273 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dddc755d-9ae7-34db-b905-ec417a49cd24 | -11.79772 | -44.91096 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc17e292-b1c7-3806-a929-b2812d70e33f | -11.95065 | -47.93082 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b10c3b6-fe5d-3236-9318-7021ec800ec0 | -6.75731 | -44.59443 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7da7a5ac-dc6f-3070-92b1-4d05da1c3736 | -12.68717 | -46.87458 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43315cf2-992f-3e0d-8341-bc384c19c141 | -7.86907 | -44.5569 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb966704-241f-363a-bc67-11ca6ed49110 | -8.26886 | -45.46729 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e77eb87-5e6d-3f6a-964b-d6b45bae00df | -6.11647 | -41.81327 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7fee7605-31d3-363b-a31f-d1560c18ff96 | -7.34902 | -42.10954 | 2025-09-28 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1d0ac46-bcd9-3303-a730-2ebd6dcba5a2 | -12.88072 | -47.09113 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 685eff3d-82c9-3ec6-896d-8a0a0963f04c | -12.93311 | -45.12288 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf1e2b99-4766-305b-bc4c-06d7902d4434 | -11.71021 | -44.43132 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d0072c-4d47-3e7c-b891-79a24243ef26 | -6.91644 | -39.58554 | 2025-09-28 04:25:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3e83dc8f-2b3b-3597-beba-ce7c1cca4105 | -10.41083 | -46.14706 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ab81504-75d1-3b83-a4b0-bafc9ef4159b | -6.47784 | -44.24718 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb40effd-1601-325e-b09b-bd5ffebaca10 | -12.68217 | -46.88478 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6503a458-3fdc-326c-bc58-96ed40f397bf | -11.99221 | -47.88332 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 994b72b4-4259-35a3-9ca9-7a3022f43909 | -11.60486 | -44.38722 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c46c4861-8251-3660-93a2-142ea01c5704 | -6.60712 | -44.10871 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfef87ae-aaa4-31fb-9f46-4f913b35e277 | -11.50801 | -46.9471 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0b9a7ef-ea45-3b8f-a328-1827061fb2c2 | -6.07083 | -44.06772 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 602ed0e9-d33b-35cf-942e-ef9106f034cd | -7.77812 | -47.01788 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88fb484f-9ef1-35ef-95ea-bca5d0f6f9ed | -9.04569 | -45.51466 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 529ddb79-95d4-3685-a456-2bca335b1d68 | -8.71479 | -50.05284 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 791fc2c2-335a-3a4b-886c-2cdfb0cfd264 | -9.41237 | -54.69202 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 863ca77b-37a7-34ca-bc6f-a20a3fdaeae6 | -5.89877 | -45.88511 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f99c27e-3264-37f0-a7ba-8518503613ba | -6.21601 | -42.84864 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 33eaa1a0-0212-3176-9a7d-541a7e23cecf | -9.61402 | -46.68343 | 2025-09-28 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f622537-47ae-3a4b-82ce-f72574eb9f80 | -6.78401 | -44.07653 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34c7ec31-f10d-3ea7-ae93-ca68a53b24fe | -11.95407 | -47.88795 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9f4ebdd-2aff-33d5-bea1-0beed3675551 | -6.5125 | -54.88485 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33df1a29-fe83-3290-bbe5-a86508914a66 | -8.86044 | -46.61728 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecba4cff-db5c-32d0-9e09-083d6a63b772 | -8.81504 | -45.99438 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53abff7b-c733-33e3-b584-f7e053f8f3b6 | -5.57775 | -46.96826 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b719fd3-a074-3629-b294-db2f59b59934 | -6.56147 | -45.10261 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 322a93b0-491f-33e6-ab77-5d90f8643d43 | -5.82898 | -44.43538 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bc81186-ca3f-360f-9d09-403016fbb546 | -11.62204 | -44.41938 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
