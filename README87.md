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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28f901cd-2bb6-3fca-a4d0-c536ebbb531d | -10.8215 | -50.6519 | 2026-08-31 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| edf65f7b-7bc9-3e54-8b02-57bf2159e122 | -14.4007 | -52.5226 | 2026-08-31 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 77bb6729-b1df-3b0e-a5b2-f7201dae253e | -11.2503 | -54.0146 | 2026-08-31 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6bf535b9-dd92-3a40-9d55-374be21e28ab | -5.5831 | -60.2307 | 2026-08-31 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 325.1 |
| 6de645b3-52d4-3022-b63f-921566097142 | -11.2482 | -45.1194 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0a4b940b-f727-3f9a-a8ca-0609d54ea3f9 | -7.9907 | -46.5177 | 2026-08-31 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6a997cee-63cf-3fda-ba94-03602fc45fa3 | -18.2704 | -52.6851 | 2026-08-31 13:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 9f81e9e1-92f9-3b5a-be62-4b7b3d84b980 | -10.1538 | -45.6982 | 2026-08-31 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 161.8 |
| fabde95a-8c56-37f9-8acc-a0f3d6bea0d4 | -19.114 | -57.4031 | 2026-08-31 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 9d12d137-2691-3139-bd81-31785770390b | -7.5658 | -61.3811 | 2026-08-31 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b6d2a088-1daa-3fcd-900a-498d583048c6 | -8.7442 | -46.4437 | 2026-08-31 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5185bb29-d67e-3ba2-8d7c-47c71d720f2e | -11.3767 | -45.423 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| bf62a016-88f9-313c-b6a3-7519fc75cead | -7.6317 | -46.7284 | 2026-08-31 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e0269a5a-c94d-3f88-807d-7795baacfa16 | -7.9239 | -44.2327 | 2026-08-31 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 9d6b2453-a2dd-3d50-9391-aa19e01e8ccf | -19.134 | -57.4005 | 2026-08-31 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.5 |
| 705e01ea-9e63-33da-ac56-a53525d25276 | -18.27 | -52.7068 | 2026-08-31 13:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| d81520d6-0f68-30a7-b6fa-6b14a96fe12e | -6.6035 | -58.6166 | 2026-08-31 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| af1c0580-d732-3304-b10c-292630fe73ca | -10.5598 | -50.4236 | 2026-08-31 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 868679f7-e379-3a0b-9546-13b1593a6bc8 | -5.2362 | -55.9112 | 2026-08-31 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4487a54c-da80-390f-9d77-162d393bc811 | -10.3394 | -49.9547 | 2026-08-31 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 784394cd-ccdf-3984-842a-37a2973eeef3 | -8.7442 | -46.4437 | 2026-08-31 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 72306feb-c8e6-3c39-b82e-9f8b33346879 | -5.2547 | -55.9105 | 2026-08-31 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 93d788df-1754-3f42-bdff-8acfde6fa34b | -13.6425 | -51.8347 | 2026-08-31 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 648825cd-5afd-335d-8539-df26d1348b3b | -7.1123 | -42.7727 | 2026-08-31 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| e1cd7886-2410-31aa-a545-0c21c75d99ba | -7.5658 | -61.3811 | 2026-08-31 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 19a6aa49-1c20-35d5-af69-cf8e9254c9bb | -10.8624 | -45.3789 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7839f73d-a35c-35b1-b4ef-926990957891 | -10.7407 | -54.0401 | 2026-08-31 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 1989c5fe-3174-36bc-93f6-7113f63f2105 | -8.799 | -62.4905 | 2026-08-31 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3988d6fe-5682-3f8e-b442-3ba3b0c77f2d | -7.3119 | -60.5706 | 2026-08-31 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| d1284b37-fc47-31fa-8223-a65e56286f69 | -11.5279 | -45.5162 | 2026-08-31 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ee7f3b62-b6e6-30d6-a45f-2b648f477a5b | -7.5844 | -61.3613 | 2026-08-31 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 39a7f140-9eed-331e-ab86-ded3b41e1225 | -7.1126 | -42.749 | 2026-08-31 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 4081a7ed-a81f-3436-aadf-a1569e860abe | -11.4828 | -58.5159 | 2026-08-31 13:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 244.8 |
| cafeafe7-e6cf-31c3-97a4-abdfe48d86be | -11.2506 | -53.9941 | 2026-08-31 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0c6646da-a242-3835-92af-38842c1fac6b | -11.5283 | -45.4933 | 2026-08-31 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 3e8e1f3b-2aee-3ce5-9797-68841a2f754f | -7.5843 | -61.3803 | 2026-08-31 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 209b5d29-9371-37de-86f7-af74831b2bc4 | -14.2796 | -52.8547 | 2026-08-31 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7c0dbeda-372a-3661-8460-ad766ae8a545 | -6.6036 | -58.5972 | 2026-08-31 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 754.2 |
| ff425541-4317-3241-9874-a310dc1013b1 | -14.9858 | -48.1529 | 2026-08-31 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 498984ec-fd4a-3ac6-b843-26d32a28e6f0 | -14.1459 | -52.7871 | 2026-08-31 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2e1ea457-2462-3a05-8c4d-6cf49d25714e | -14.2792 | -52.8758 | 2026-08-31 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 9a553836-159c-31ed-8b41-0530ec899abe | -18.2904 | -52.6818 | 2026-08-31 13:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 643d1266-8498-3e62-b7ca-ae9b8521a712 | -5.5831 | -60.2307 | 2026-08-31 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 270ea605-b1fa-3cae-90ad-877d3b472796 | -18.2899 | -52.7035 | 2026-08-31 13:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7635f99c-2d02-339d-a1dd-5a216f9e177f | -18.27 | -52.7068 | 2026-08-31 13:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 185.4 |
| b1f5667c-b58b-3c83-913a-0b4b55c77552 | -5.5647 | -60.2312 | 2026-08-31 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7128df21-7d2c-3f6e-ad3f-f43783978afa | -14.4201 | -52.5201 | 2026-08-31 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 953d4380-73e1-383c-85e8-343758b8b1f1 | -7.9236 | -44.2558 | 2026-08-31 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a130872e-c286-3240-8941-7d0c497e0f8a | -6.9367 | -55.636 | 2026-08-31 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8b8171f4-ac5e-3cc6-b629-23f378cd67c9 | -11.3236 | -45.1778 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a2997936-f6bf-3ebe-82c6-168c991c582c | -10.1538 | -45.6982 | 2026-08-31 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 6cc72de9-8a3a-36f9-9bca-f87841579226 | -9.8015 | -46.4629 | 2026-08-31 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0740a334-6d79-30c0-9ab1-46bce4dfb887 | -11.5017 | -58.5145 | 2026-08-31 13:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cd67eb84-f08d-3cf5-ab39-35d22dbedcb5 | -11.2503 | -54.0146 | 2026-08-31 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3ce4de66-26f7-3062-95a0-9c30cb3b5b0c | -11.2294 | -45.099 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a2f56382-88da-3252-887f-f4b337e51ec8 | -6.9176 | -55.7166 | 2026-08-31 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2bd26fb4-8561-3b91-90db-dd8ef0fde7fd | -6.1109 | -57.684 | 2026-08-31 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 00c2116c-e410-3d5a-af52-80523ac4c5e3 | -9.6676 | -47.9429 | 2026-08-31 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 269.9 |
| c42b07f8-cfee-378d-9f3b-1eca101d8a1b | -8.7439 | -46.4661 | 2026-08-31 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 54ca1bb0-1c46-3cee-805c-2920ced7e413 | -14.4007 | -52.5226 | 2026-08-31 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fc0392fd-3451-35ce-b1a9-f2f855832282 | -10.7596 | -54.0384 | 2026-08-31 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 79b7b092-2a21-3667-986d-c35da6137767 | -11.9378 | -45.0656 | 2026-08-31 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6daf1439-2f2a-3dfc-b6a8-7e622841d40a | -7.5659 | -61.362 | 2026-08-31 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7c4d9a56-64d1-398e-949a-a7f239ed3fda | -11.2482 | -45.1194 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8fce9364-3825-38cd-8e6c-ca3593900011 | -11.5475 | -45.4906 | 2026-08-31 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 265b50bf-13a8-3258-94fd-bf0d98a4ba17 | -11.2485 | -45.0963 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 1136f762-bfc4-313e-a50c-458773a485eb | -18.2695 | -52.7284 | 2026-08-31 13:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 67cddaa3-a3f9-3763-9407-a8c750562f02 | -11.3423 | -45.1982 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| c78cb008-ef00-3b6a-8af9-e1a1398f0cfb | -11.1821 | -50.592 | 2026-08-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1e4b78a9-64a3-367c-b409-c2e607ce02fd | -10.8046 | -50.5046 | 2026-08-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 89e0dc5f-874d-35a5-a518-4a2bc2b063ef | -5.8692 | -52.0868 | 2026-08-31 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9930ea6b-2b34-30dc-88cb-787ded082e69 | -8.7989 | -62.5095 | 2026-08-31 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cf4b7a44-a830-320c-8a9c-8e8a13b05b2b | -14.5868 | -54.1153 | 2026-08-31 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8b12bb14-9331-323c-ad9d-fb629b842f08 | -11.1634 | -50.5727 | 2026-08-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 03246796-f009-3c5a-929d-07244ab97d28 | -7.9239 | -44.2327 | 2026-08-31 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 12889f4c-0779-3201-96d0-9fb42525b9cf | -8.1672 | -54.9246 | 2026-08-31 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| df0b93a3-9b06-3fc1-91bf-b810224d9c3b | -3.6215 | -60.566 | 2026-08-31 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1e170298-e5ac-35ea-bba8-e7a69b4d5fb8 | -7.3118 | -60.5897 | 2026-08-31 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 5c8af125-7682-3025-81d2-4582abd78ea4 | -6.1295 | -57.6637 | 2026-08-31 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 652fbbb2-2fd0-3db0-99a2-61b40271f066 | -12.9032 | -45.8382 | 2026-08-31 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9db2cd0d-e961-38ff-9a09-78069adf1438 | -7.9907 | -46.5177 | 2026-08-31 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3e8c5316-a0b7-305e-9b5d-acfcffe39312 | -18.2704 | -52.6851 | 2026-08-31 13:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 120137c3-682b-3630-9f7f-8d2a1cafbca4 | -10.1535 | -45.721 | 2026-08-31 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ca5f32b4-fd13-349b-a1db-49c1c5756476 | -11.3232 | -45.2009 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b16ed250-fcab-331f-9f3c-0a12f3817a62 | -11.1824 | -50.5706 | 2026-08-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 33b84b43-c6ab-3eae-ad60-a4c707a26f93 | -10.7598 | -54.0179 | 2026-08-31 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 84a29a01-2261-38bb-8f18-a2f1b72f18ee | -11.3615 | -45.1955 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 9b2d5976-3684-370f-be7b-41172a025f19 | -10.3205 | -49.9567 | 2026-08-31 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 9d6bb614-c0d6-38bd-9557-1d0cb3ce1e46 | -5.5832 | -60.2116 | 2026-08-31 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 124633bc-f924-314b-81b6-d959a0a5cc93 | -11.3806 | -45.1928 | 2026-08-31 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c8eb8623-661d-3957-862e-78314c395742 | -7.1123 | -42.7727 | 2026-08-31 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 8b88c5f1-ba0b-3868-ade3-75aad2f4c689 | -11.3232 | -45.2009 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 13a19d18-ec68-3c1c-88e9-043be850ae22 | -6.2469 | -53.6826 | 2026-08-31 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bc683bdd-35c0-33d4-8e83-5bad06667d22 | -5.2548 | -55.8907 | 2026-08-31 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 028bbd45-fadc-3a47-bb07-ac10846e2ae4 | -10.7407 | -54.0401 | 2026-08-31 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 8ea0c3d7-6a9c-3d13-813c-6e5ac8787c7f | -13.9667 | -54.4157 | 2026-08-31 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| abd36c59-a438-3ce1-ab27-b038fbf26250 | -11.1634 | -50.5727 | 2026-08-31 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b2d738cf-b0b3-3e01-9702-b3169af6f265 | -7.1126 | -42.749 | 2026-08-31 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| dfc93c90-b5a9-3e1d-948d-1b2acfd2ff99 | -7.3119 | -60.5706 | 2026-08-31 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| dabf64f5-2d31-3d9c-9d35-fd11626e9c3b | -11.3423 | -45.1982 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |


[Clique aqui para ver as próximas entradas](README88.md)
