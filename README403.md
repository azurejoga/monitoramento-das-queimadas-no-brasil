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

## Dados Diários - Página 403

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e00693f6-93ad-3670-9d04-261f8005c279 | -6.2355 | -52.6841 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 16c8179e-c349-3c54-8245-455e6a0de549 | -6.9331 | -43.6566 | 2026-10-08 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d8aac48f-cafa-328f-b134-9c54d9b41b51 | -11.7738 | -43.5482 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 60d56faa-b1ea-3d67-9bbc-1d6d2c064e34 | -10.9193 | -45.3942 | 2026-10-08 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 79bfd083-53e2-3345-b86c-07db87320313 | -4.0628 | -51.0508 | 2026-10-08 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 116eb6c4-1006-3117-956c-f3c1e74c60f9 | -4.6641 | -56.2281 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e1188edf-5b16-3eb0-8204-a3d3239ab9de | -2.8434 | -57.4696 | 2026-10-08 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 2dffd2cd-11dd-3892-bf0c-bef1d12e0ff9 | -3.86 | -44.1274 | 2026-10-08 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 18c5a778-f670-3b37-9bc3-a9f988f316db | -6.4397 | -52.6522 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b5880c28-43dc-3691-8888-05ae08f1e897 | -2.9005 | -56.6685 | 2026-10-08 19:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6ad2479f-6bf8-32bf-a803-a26a7bc0b318 | -2.5491 | -58.0566 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7382680d-ddd2-39cc-80e3-5805d6d82e5f | -6.2542 | -52.6625 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 9ea1a67b-a245-3a94-98d3-81653beb3e6b | -2.5903 | -56.1642 | 2026-10-08 19:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e826cb94-45cc-301f-9c1c-0002bfed106a | -5.6935 | -53.4464 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 37ec2739-b830-3018-a6be-8bc6800312e4 | -14.4541 | -43.912 | 2026-10-08 19:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 796787dc-0aed-3141-89d3-ee14d6ef35cf | -14.4339 | -43.9396 | 2026-10-08 19:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 2e32e564-0395-3dec-b903-1b2697b396b6 | 1.8222 | -55.5258 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5134b2c9-7829-3172-b213-2b181c134eb3 | -2.7612 | -54.1142 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 6b5c4799-de19-317d-850d-d781c52adc23 | -3.1114 | -53.7839 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 8ca9ef81-4602-3f96-aba3-ec2dc08976fd | -9.8439 | -47.483 | 2026-10-08 19:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 9640903a-51a4-3ef8-9447-402f341a6f3a | -8.3011 | -45.7245 | 2026-10-08 19:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cdeb683f-2a18-3b18-a026-7e601936c578 | -6.4978 | -43.9732 | 2026-10-08 19:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 04e2aacd-2538-38b8-a4d9-7dac0de0c406 | -2.7428 | -54.1146 | 2026-10-08 19:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| cda72609-c5a4-3882-82a9-ed215b3ea3a2 | -6.1227 | -55.6955 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| fda9dcd8-aa17-332a-9684-062b213a0f2a | -6.1783 | -52.9124 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| afd48179-4db3-3d86-be1a-237c0b20d4d4 | -6.1617 | -52.6471 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 892864ba-035e-38a3-87ef-1135fdcda344 | -13.3666 | -43.8979 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 133fac08-869c-33ca-b5eb-f7d409d3e183 | -14.0472 | -43.8222 | 2026-10-08 19:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 741e1f58-7a0f-3fa4-a5a4-788de0f1945a | -11.2478 | -46.2831 | 2026-10-08 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 293.0 |
| 8ed3c07b-95bc-38e4-a03d-432dfef14ee4 | -6.3134 | -54.7884 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| b584aa85-8823-3011-ba8f-528a7000302d | -6.0076 | -53.4919 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 83117c9d-bb4e-3532-9608-5ed334258c46 | -3.8413 | -44.1283 | 2026-10-08 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 708fb5dc-d649-38d5-a85a-1076a3e8ef90 | -3.0256 | -57.7768 | 2026-10-08 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 05f8aa6b-28d6-35e7-8dcb-b4e24a0c9024 | -3.3139 | -59.3898 | 2026-10-08 19:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 9b26f855-96f6-3abe-a014-3ed78da555ba | -2.8571 | -59.2641 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 30d6922d-6666-39b1-bd8e-a9276d6791c5 | -3.7809 | -41.7913 | 2026-10-08 19:10:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 169abf79-a33a-35ac-adf5-f825a619fd8f | -6.4905 | -55.9563 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 03a990cf-4eea-3172-b2ae-72501c6d8576 | -3.93 | -56.0143 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 159.2 |
| acee3cfd-4580-3e7e-bde5-763921644376 | -6.8762 | -43.7083 | 2026-10-08 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0bc20d07-a06d-3729-a7e3-af4bde808c2d | -4.0629 | -51.03 | 2026-10-08 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0c58a750-89e8-3414-a30a-f28b5964dc62 | -6.5322 | -55.2577 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| d276fffd-eae7-3ac6-9ca0-732880469570 | 3.5448 | -51.2772 | 2026-10-08 19:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 887bbf6f-7b3a-3bc2-b211-73f906abdd94 | -4.6364 | -50.9437 | 2026-10-08 19:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 352.6 |
| 6120e2a2-cb0a-3732-b93a-e652d8272137 | -1.6394 | -55.2708 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f4b51860-4c6a-3b6b-98d8-663dfbbd6652 | -5.8613 | -45.9774 | 2026-10-08 19:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3f9e0565-69f3-3924-b017-02dc7eb35841 | -3.2136 | -42.9764 | 2026-10-08 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 706ea6f2-b0af-3d1d-b1f8-f387f85d143c | -8.6106 | -67.0486 | 2026-10-08 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 2cea8ce4-56c7-3c69-9818-3f49238b8560 | -4.6642 | -56.2083 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 1d4ab6f0-2a10-351c-9f10-6a4271c3d084 | -8.0578 | -45.6131 | 2026-10-08 19:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4928a300-62fa-3ad1-954d-b03f253cbf13 | -3.9299 | -56.034 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 219.3 |
| afa81518-7427-3eca-8951-f643fc42bfdd | -11.755 | -43.5275 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| ba17982f-44d5-38b2-b2f1-72c80fb4aa81 | -9.0402 | -46.8817 | 2026-10-08 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2aa9ef1d-a47e-3cde-97e5-60d62bca23bb | -5.3763 | -45.943 | 2026-10-08 19:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 0cdf28ff-87da-3595-b99d-50bb92a801e3 | -5.8842 | -43.4199 | 2026-10-08 19:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 189.4 |
| f3da1803-c7d6-3b31-a0a2-df212e4b693e | -6.5399 | -45.3868 | 2026-10-08 19:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 01603bcd-0d13-34ea-b911-1f963c8e867b | -3.1879 | -58.6433 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 114ace36-539a-3422-b716-bf90c0e43883 | -6.4032 | -55.1842 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| bf0befc0-1413-3e30-8079-65696c040192 | -1.3264 | -56.4176 | 2026-10-08 19:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 8d2e4c36-509e-344c-ba60-1f7aa566cfdc | -2.7428 | -54.1347 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| f36d829d-0db2-37b0-ab37-6850504645f8 | -4.1642 | -43.2326 | 2026-10-08 19:10:00 | GOES-19 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c6a2551d-9071-36cb-be0b-2a66f26df35f | -3.8383 | -55.9774 | 2026-10-08 19:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 51481be4-eeeb-3f96-8277-aa0762239c4d | -5.6136 | -44.3647 | 2026-10-08 19:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 0e6c71e4-07b7-34d0-ac11-a413e4447a9d | -4.9433 | -49.2204 | 2026-10-08 19:10:00 | GOES-19 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 415ec933-8909-3263-8337-85936bab871b | -6.4949 | -55.2995 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 309.6 |
| 36577f15-1321-392d-91d0-9a72a60c72c4 | -2.9451 | -54.0497 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 54ede67a-be40-3de9-bea6-eb7ebcae93fe | -5.9267 | -51.8151 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f625f1e8-170e-373f-ad0b-499fda796a75 | -11.7742 | -43.5245 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 95c0968a-dc69-3c84-adb9-ff52f0322608 | -3.2956 | -53.6984 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 5dbc21c6-d030-353a-b258-e287ec054082 | -3.2717 | -50.3893 | 2026-10-08 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d343a1fe-4297-396b-b73a-fdc64911f26a | -6.521 | -45.4109 | 2026-10-08 19:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| fc176f4e-1ba1-36ac-8847-3461cab7bfdc | -8.9775 | -45.9023 | 2026-10-08 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 261ed874-f04a-3c77-ab47-b64a8e5b44a8 | -2.5069 | -47.3771 | 2026-10-08 19:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 21a6e43d-2379-324a-ab17-9dc23e9b749c | -3.1951 | -42.9538 | 2026-10-08 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d7daa361-d34c-3de8-82f9-d7137c4b6215 | -1.5485 | -54.8348 | 2026-10-08 19:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e07e8fae-103b-3d4f-b590-8c0a74642d0e | -2.5125 | -58.0765 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cd5eae99-6028-39e4-b398-51b5dce500ed | -8.2433 | -54.7384 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 287.1 |
| 4a92c953-e2c2-344b-91a2-604160ae17e6 | -3.1697 | -58.6437 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 4dd03ad2-270a-3399-b0e1-6b676230dc8b | -14.4585 | -41.2104 | 2026-10-08 19:10:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 4a23c952-d67f-3f88-8d12-60222922346f | -2.572 | -56.1842 | 2026-10-08 19:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 237.9 |
| c557677a-0e1d-34d8-b544-2666fef51fe6 | -2.0834 | -46.5765 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 035ea2b6-ef8b-3e01-a8f4-c0ee3b81722b | -5.2351 | -56.1287 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 19552b4a-96c5-3207-951c-fd7a7343f46b | -5.7119 | -53.4658 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 268.7 |
| 18672abb-d054-3656-b763-92b63fc19c4c | -6.8907 | -45.8988 | 2026-10-08 19:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 6e5b9777-07c0-3390-b172-42cf71fc9dc5 | -8.0766 | -45.6112 | 2026-10-08 19:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 8eb935f5-3ec2-3e16-a871-05eb7bc57031 | -6.4411 | -55.0424 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 237.9 |
| fb934364-a5ca-3bf5-98c1-c51a89fae0da | -5.9587 | -55.3448 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| eafcc08c-979f-3609-bae6-16719530f577 | -6.1429 | -47.9432 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0b6572b7-c04b-3780-a88c-e201ae79113a | -7.4697 | -42.8315 | 2026-10-08 19:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| e5fb6f62-e424-30a9-9f9e-c26e41eb6924 | -11.6382 | -43.6166 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 95337a98-b7db-3824-8171-f0f3dbb25cbf | -11.1145 | -44.0009 | 2026-10-08 19:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 62598a92-bc84-3ea8-b667-fe5e1cb59afb | -1.3447 | -56.3979 | 2026-10-08 19:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4b3800aa-30c3-3df5-8834-4a105fc8481c | -5.3718 | -44.1981 | 2026-10-08 19:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2961f2b9-f442-31a6-97d9-21264d93c524 | -11.0949 | -44.0271 | 2026-10-08 19:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3b1f371e-e984-3413-8d68-dc63ec6a2d06 | -6.1484 | -51.927 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 1787f240-ba55-39b7-8bd4-e97cffd68b96 | -3.2634 | -57.8689 | 2026-10-08 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a43a02b8-042e-3d8e-843b-fb2b09b31eeb | -2.0759 | -56.8784 | 2026-10-08 19:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 7f1df0b8-df45-3c91-a99a-4968483da162 | -11.7545 | -43.5512 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 01340483-0eb0-370e-a968-9c45adb7e67c | -6.1226 | -55.7154 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 115dde97-89fc-3511-8e73-5eb41dfc1a72 | -3.4496 | -56.9303 | 2026-10-08 19:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| df5befc4-2214-32da-a27b-e05ee3ba4b4d | -3.1697 | -58.6244 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |


[Clique aqui para ver as próximas entradas](README404.md)
