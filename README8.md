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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0aafa08-69b4-3fee-895c-bed31d45d8ce | -3.31297 | -47.38093 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3d3ba6e-5c9a-3ed9-9b7a-1db133b41653 | -6.32187 | -39.98935 | 2025-12-27 04:18:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96fe0b44-9611-3399-842b-bf57ecc639eb | -2.92652 | -48.2338 | 2025-12-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 433942f1-9e40-3a2e-9683-bc106188c2c0 | -3.75177 | -49.73013 | 2025-12-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee35f597-e65e-33f0-9ff0-a0743113d2c0 | -5.60473 | -39.73186 | 2025-12-27 04:18:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23ce0df2-9f77-3cb4-b621-931e98fde5b3 | -2.37721 | -51.91288 | 2025-12-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 830703be-7553-3ab9-b402-0c949cd894be | -4.10369 | -38.25764 | 2025-12-27 04:18:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec531a49-2b70-3959-bab7-01f29ed9dc32 | -3.30967 | -47.37602 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8e4d3c60-71a3-3e1f-b1f2-b45617252619 | -5.33714 | -37.05906 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2965f94f-1f80-3712-a13f-8c4bec5c8b56 | -7.22379 | -43.07939 | 2025-12-27 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5099ce5-fd60-38aa-93eb-23c6feaa321d | -5.34144 | -37.05972 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0dcdacbb-f591-3e5f-a6df-3b58c82046ca | -2.13473 | -48.00135 | 2025-12-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e379cfd1-50d7-39d5-ae74-6c71349b20e1 | -3.65214 | -43.51553 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4d95cc0-3a96-3369-9ea0-f7f4dd1863f6 | -5.34879 | -37.05102 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| edef7ac8-e097-3903-a7cb-6c8e8bd638b2 | -2.8996 | -52.58981 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08c27e99-ba03-35f0-9885-ab353545327d | -3.65939 | -43.51308 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 886fe4d3-931b-36ff-8c36-f92454d71379 | -5.34512 | -37.03542 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7c1c80d4-7d53-3ad8-9e09-97047dfd1b08 | -3.75985 | -43.56102 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83a8dd6-d520-35f3-a942-a6ddb3879a54 | -5.78991 | -43.77818 | 2025-12-27 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f45f660-c9b4-3fb1-ac96-242112007bee | -2.69727 | -51.64464 | 2025-12-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95a7cc3b-79c0-3676-b924-3db216ac3146 | -3.7632 | -43.56156 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62b0b581-b6b9-33ac-9bba-1fa154ed1dea | -6.75666 | -35.16684 | 2025-12-27 04:18:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf44c1c7-ae29-3aaf-845e-7b03dfe2d141 | -5.00814 | -39.71389 | 2025-12-27 04:18:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 917fcb06-f974-3538-ab08-3a8f38630c17 | -3.90233 | -42.55546 | 2025-12-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b99a7ae8-48d4-3158-88cf-ed9a17ce6055 | -3.65717 | -43.50552 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77840ac3-56e0-3028-b725-85c7f524a49f | -6.72171 | -39.67862 | 2025-12-27 04:18:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5e0c765d-bd2e-3f1c-b490-258d4a93d0da | -3.73335 | -44.5394 | 2025-12-27 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c341933b-d36f-365f-8954-d406adc1bb90 | -5.8586 | -40.34399 | 2025-12-27 04:18:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4026f53-a0af-3151-9177-b7155db9051e | -0.08783 | -51.27795 | 2025-12-27 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad5ab62e-3d58-38da-b0b3-8f69f5ade8ce | -2.89897 | -52.59357 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70735fd8-ee4b-388b-b58a-6f749f25de47 | -6.55032 | -43.10136 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09494767-40d8-39b4-9c90-837a797e9634 | -2.37165 | -51.91212 | 2025-12-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 273611dc-d6df-3f5d-8611-4d28f3ff95be | -7.22657 | -43.08339 | 2025-12-27 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5eb36b3-b12f-37c4-99db-0dcf44e131bf | -5.34996 | -37.0429 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71f40eb3-e215-34d1-aa96-98cecbee2b11 | -3.64601 | -43.51096 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28d2c12c-5bda-3d7a-b1e1-02aa74319911 | -5.45266 | -46.17635 | 2025-12-27 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2968534-0dde-3058-983d-00a2abe72316 | -5.93718 | -44.45467 | 2025-12-27 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e754d70d-e34c-320f-ba5d-4417ff2ef3de | -3.90179 | -42.55891 | 2025-12-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| df14262e-1055-3786-9365-d42265c85276 | -2.96684 | -46.7857 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55e12d3d-e749-3fea-9960-b45b43ff6260 | -5.75001 | -45.1139 | 2025-12-27 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41b32735-f576-3813-8e91-54c8fe9476da | -3.76376 | -43.55804 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03473dc5-3033-3458-b5ae-76f6026e716a | -7.22712 | -43.07991 | 2025-12-27 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a33ad764-b091-32bc-84b6-f014014648b8 | -10.4889 | -44.9235 | 2025-12-27 04:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 66036aa4-54fd-3339-aae2-8924026b2b62 | -0.0828 | -51.2738 | 2025-12-27 04:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c40ba39b-75de-37fc-8ff3-bebd7747f197 | 2.5247 | -60.982 | 2025-12-27 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 63a90e51-6463-3288-850e-14688a7b3c16 | 2.5065 | -60.9822 | 2025-12-27 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ade795f5-0dfd-3964-98d8-bd53d22e7b11 | 2.5247 | -61.0009 | 2025-12-27 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bbdc1018-df5d-39bd-ac2a-089dcf22c88e | -11.39343 | -47.99665 | 2025-12-27 04:21:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5255f523-a8ee-3695-838d-89da2de3835c | -12.72056 | -47.72742 | 2025-12-27 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6642dae-cc8c-3b29-b646-f37ab287c5d8 | -12.17799 | -38.81381 | 2025-12-27 04:21:00 | NPP-375D | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 03d7d737-bce9-3ba3-b8be-97a44833721e | -11.46271 | -54.35321 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d5a29f-891e-3b5e-a4e2-6b35001ce46c | -11.63706 | -49.4217 | 2025-12-27 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9153b10-03f9-3e43-aaa2-c01b7231dab5 | -10.54236 | -48.70986 | 2025-12-27 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618ca5a5-5d2b-3fb2-93de-30859c67a82f | -12.51957 | -48.38249 | 2025-12-27 04:21:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce17c6e7-35f1-36d8-97b1-bd181ebe3563 | -10.02472 | -42.32927 | 2025-12-27 04:21:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c844e57d-8505-38f6-8795-7d7931bcafd3 | -12.15955 | -46.6723 | 2025-12-27 04:21:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce476a7a-a920-3169-9b07-1eaa3a21c782 | -13.01634 | -40.6296 | 2025-12-27 04:21:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0e8b16e-bb93-3f47-a9dd-80a27636da3d | -12.80233 | -46.65311 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec07ff60-d8a5-3807-9c81-fa48c5f9113f | -12.67143 | -46.76936 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b5ed19d-09f3-35df-88d3-d150d324a75c | -11.15931 | -43.31959 | 2025-12-27 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c466944c-4c6c-3369-bfd9-59ff83c39e49 | -11.10506 | -49.09957 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e38d60d-74cb-3c21-8ad5-027b1f8286fd | -11.01416 | -45.25795 | 2025-12-27 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a17140a-9127-35fe-8490-e9b132e6a37f | -10.49299 | -44.92764 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bad63683-42b2-382d-ac09-c8b4450e99e1 | -11.01808 | -45.25494 | 2025-12-27 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5b878b3-3c45-3b75-afc7-1ede5e0c185a | -11.46197 | -54.35699 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab97e6ff-006e-3f51-b721-b22a359f672e | -12.49288 | -46.34568 | 2025-12-27 04:21:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d5ee706-167c-34e6-acea-21f9491f7adc | -11.17104 | -43.31043 | 2025-12-27 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d03ee193-3a9e-33a9-a50f-1f64941f6b24 | -14.43746 | -43.97989 | 2025-12-27 04:21:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf2730a8-fd08-3a6e-8b62-103e2926f9b8 | -11.84358 | -43.79007 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13b868d5-bcf0-356a-a698-b7d6c3ff4913 | -11.45814 | -54.35645 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c57ce63-0bba-346c-843f-a01877189212 | -12.5166 | -48.37738 | 2025-12-27 04:21:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7fce68b-d973-3b00-9273-07937736baae | -12.29675 | -44.34923 | 2025-12-27 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b604055f-d340-3f8a-8a3a-8a0b15469705 | -12.52032 | -48.37806 | 2025-12-27 04:21:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 607b3ea8-55ef-300e-aa16-5ff97dda43aa | -10.9774 | -44.54305 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8b9c22f-09c2-3d52-8240-1a83ba8ecd13 | -12.70726 | -46.79831 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25691655-5e78-3dc0-807f-5a9627b823e3 | -9.00512 | -44.34624 | 2025-12-27 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa1c3baf-0a91-3ac7-84c8-1a6fe48a08eb | -10.48239 | -44.92957 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c58cd507-314c-3252-8318-2d2c7af250dc | -12.16301 | -46.6729 | 2025-12-27 04:21:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53af4b36-1517-33a3-86dc-c67432a3b9d5 | -10.77301 | -45.01716 | 2025-12-27 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3ed5140-71ff-316e-8733-0883cdf6b0ec | -12.51481 | -43.69116 | 2025-12-27 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 510562ff-23b6-3111-9881-ec46cc6b1c88 | -10.4863 | -44.92656 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b9500b06-6893-3100-8b5f-a53ecb3a67d4 | -10.23104 | -47.15477 | 2025-12-27 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eedaf5e0-13f8-39a6-9041-4d2e316c90b1 | -13.55106 | -49.90703 | 2025-12-27 04:21:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85278985-81be-393d-acea-032f1557e966 | -10.48296 | -44.92602 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d817b373-f33e-3e8a-b2f8-9eeed588f4a3 | -10.88047 | -48.98122 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9905c111-2743-3ae0-b125-69f182298674 | -10.49633 | -44.92818 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cf7a63d4-7215-3db8-8c1e-24a8015703f2 | -12.65979 | -46.7753 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2004b70-1e44-36c6-a4fa-bbf7e300adf3 | -10.53109 | -43.61764 | 2025-12-27 04:21:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20018b6d-b2bb-32a4-83bb-80cec299fb16 | -10.76967 | -45.01661 | 2025-12-27 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a46ec49-b1bd-3938-a71a-8d15ff3f6e69 | -11.97929 | -44.28325 | 2025-12-27 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c97986c2-ab30-387f-b4b0-a6b8e8908d97 | -12.51736 | -48.37291 | 2025-12-27 04:21:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1a97a8c-4671-314a-aba7-2fe505754d26 | -10.54151 | -48.71487 | 2025-12-27 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c87593ee-5faa-31d6-8b81-2434018cafc9 | -11.13316 | -44.28772 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 853a2d0f-ed5f-3d0a-957d-0516aad142e4 | -10.54626 | -48.71054 | 2025-12-27 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e938a0-c706-3ded-b831-b7ce92f26538 | -10.49021 | -44.92355 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3e8104eb-de61-34b7-b199-7a7e4838ebdc | -10.47503 | -36.77336 | 2025-12-27 04:21:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a268207-52b9-379b-8437-f3beaf4ed043 | -14.44189 | -44.85844 | 2025-12-27 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed343e4e-7321-3912-8de6-64e197dd8cb1 | -10.0213 | -42.32874 | 2025-12-27 04:21:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b42fc92d-bd55-3ab3-a7c1-818fdd72f798 | -11.80213 | -48.27864 | 2025-12-27 04:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb70bb38-34b3-3ff8-83f5-df8c2f0e222e | -11.84691 | -43.79061 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
