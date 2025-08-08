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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a287a47-f4d0-3a51-88f8-d0208b93b62c | -7.91804 | -45.52846 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1a68cd9-4355-33b2-a155-9cc0000e88ba | -10.48503 | -44.3848 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cf2d069-cdf3-3914-99b6-2df7abe65fc6 | -12.57839 | -47.16114 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a314da7-70b9-38f3-9846-b1308ca4cdab | -11.15815 | -49.70335 | 2025-08-08 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9745eafe-9103-33cc-9e79-edb3638d511a | -12.55059 | -47.14219 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b999053d-8fdb-333b-a176-65d1d71f577e | -8.5273 | -43.30975 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0708afc0-3e4a-32da-828e-a2efbdbeef78 | -7.15128 | -44.4784 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e4067d4-f8ec-33f2-91bf-5f01dc2c004f | -10.64042 | -44.74788 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c522f2e-a296-3b47-bb56-ec7d37a0db10 | -8.21282 | -45.06415 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66a155f7-f1b4-3878-9fd6-0d925e6b374f | -11.75803 | -47.50208 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d07f168-da01-348f-8f37-8b4018ceb41b | -10.63958 | -44.74476 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a7da7f3-b48a-3ad3-a629-f46b2aa985b2 | -11.07436 | -50.48846 | 2025-08-08 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68984d14-20d8-386d-8ff7-05c8220371d3 | -11.7745 | -47.50835 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c348473d-55d1-367b-ab0e-053153aa4308 | -9.47392 | -57.84961 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94c640a8-f1bd-39fa-9b2a-f272844612f2 | -9.94034 | -60.50864 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c0969e6-077d-3c4b-859c-7a2ff7e0e555 | -8.99121 | -45.68372 | 2025-08-08 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7d09ea0-ef98-376f-afc4-8b02fb15a9bb | -9.46993 | -57.8419 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2b6874b-a339-3908-bb48-659d8a02a5e7 | -12.31058 | -50.00846 | 2025-08-08 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c111941c-2c3a-312d-b157-cd2598b6e3b2 | -11.74883 | -47.51249 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff08771c-0074-3338-9581-9986fb0ee521 | -9.60373 | -40.56078 | 2025-08-08 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9024154f-72f1-39a1-aaab-d77ac1abd36f | -10.48409 | -44.33378 | 2025-08-08 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11ea4950-e6ae-32e0-a7cf-997e779df64f | -9.93175 | -60.48666 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3a5c0be-0e31-380b-a6c4-b8be2513f6ac | -12.72487 | -46.37241 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b71211c-8a6f-3e36-909f-f40bb98dbe1d | -8.8776 | -44.791 | 2025-08-08 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9032d4f-0727-3859-a557-09ac9dc8b538 | -7.69325 | -45.53069 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08bac5a8-86b1-3d86-a5e5-0b26297e88cd | -8.86754 | -47.46877 | 2025-08-08 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbd33515-0a70-35f4-9249-bf9990b8b8ff | -7.11608 | -44.21614 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 591d6ccf-ba5d-35b2-8b51-8f3e7e50251f | -12.5813 | -47.16555 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 138e56d3-6332-3317-bc3f-c2b237f36c57 | -8.92285 | -60.74542 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d7c341e-b4bc-3f5f-a4e4-9fa3c61c49b6 | -11.74016 | -45.02737 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ca8676f-8a64-318c-b7c5-44e710af32c1 | -12.98655 | -47.45819 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2956bb1-3687-3680-acd0-adbea3ec52b2 | -12.57387 | -47.19216 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e913177b-abef-3a46-a06d-0b7333f77716 | -7.89968 | -45.33465 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba2c368d-ffac-3e1e-8447-f93dc47af7ea | -12.07531 | -43.98929 | 2025-08-08 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b987b74-5f2b-337a-b766-eedd18c874f1 | -11.78076 | -47.51295 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb876098-ce1d-388b-86b9-60cf0d19a623 | -11.20829 | -45.36265 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3eb01e8-82d6-3de2-bd96-eb928786b849 | -10.70805 | -48.77918 | 2025-08-08 04:34:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3962e6ff-ea0c-3140-97c4-3f28c0956923 | -12.5223 | -47.14168 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08e0c2b6-b686-32f7-bcb8-60fcb123fa65 | -9.65594 | -43.84976 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5fbe1bd4-55f6-3914-a08b-03bf7547d879 | -9.93266 | -60.4819 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3549b0f9-9823-33fc-acdd-4b97d44743cd | -8.91936 | -46.84723 | 2025-08-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a5f0282-47d5-3380-9d98-6dd343fda3bf | -7.74175 | -47.3883 | 2025-08-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fcd81c2-0430-3039-80d8-36442cef8b81 | -6.95803 | -44.49852 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0664e395-ef31-3d35-9c2b-cf59eec97d0f | -12.49625 | -47.50566 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 533edc01-8e53-37e0-aa36-4af3d764dfc3 | -11.07231 | -48.35834 | 2025-08-08 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b139dcac-935e-3b13-83fe-4ec8cb181da8 | -12.56969 | -47.1479 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 154c118b-e65d-3688-96ea-b6be92c2939e | -8.2493 | -45.0697 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68dbeca2-9258-3a1d-8be7-de558438d647 | -12.58709 | -47.1744 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db2380bb-2241-3ce4-8a01-069686876777 | -11.746 | -47.50824 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b9edf53-e434-337e-b4af-915d8b13d6e8 | -11.74655 | -47.50455 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87433db9-a40f-3c86-bcf3-be856aa523b2 | -7.58887 | -44.90723 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25763fba-9770-35df-9b8a-4cc4d922cb02 | -7.38006 | -44.65339 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0a158061-69a4-31ff-9558-d90ed8d3b63e | -11.74205 | -47.51134 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db142dfb-5fa8-3fbc-86b6-91307c0ffe72 | -8.2098 | -45.05931 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0e6c74b-6393-3c3f-9c93-28abbc3c5209 | -11.75729 | -47.50259 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a7627fa-20b2-3990-9728-1d654e6e7edd | -8.90427 | -62.42727 | 2025-08-08 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0b11ec8-ed6b-3a21-8c10-79f0545b493c | -8.20918 | -45.06357 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da0b709c-fb29-3962-92df-38f0c7d26534 | -8.24867 | -45.07397 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27ae95e5-d326-374a-b530-a73df5d0a7d7 | -9.47516 | -57.84301 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d53429bb-e117-3a22-8019-c71b6c6f94d5 | -9.46978 | -57.8447 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| beb54d8d-075c-32c9-a259-78a4d385fb60 | -11.76143 | -47.50266 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2b224a6-6309-3d75-a842-145f3fd7d1bc | -9.7068 | -61.30407 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ccce8f8b-6268-385e-a9c5-2c738933d2f9 | -12.57726 | -47.1689 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ac0ecfab-c872-3919-af56-b552d3d7a7ac | -8.52272 | -43.31278 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b491ffe2-362d-3212-9fcf-6e3861a61449 | -7.38071 | -44.64901 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b7542550-8857-3168-998d-eb31929c0fa1 | -7.37637 | -44.65283 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d7fe868d-d412-37b0-8920-09d5cf9e94a8 | -8.06944 | -49.71984 | 2025-08-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10ca0c98-3eda-3b0b-a435-e0899920f708 | -7.14689 | -44.48238 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4d2bf4-27c9-3a22-b97e-26a56519a454 | -11.77323 | -47.39749 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70e1ddc8-6974-3647-86f2-ba5d6fa62a91 | -9.65546 | -43.85315 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52a4bed9-eeb8-3248-affb-5526df28d3d5 | -12.56735 | -47.14867 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4de660b9-c003-3ede-847d-bf197271ac5d | -11.20117 | -51.44275 | 2025-08-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a87604ef-0dda-3247-adb0-0ecd4253fc48 | -12.31932 | -50.06081 | 2025-08-08 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a60ce55-d386-3f7c-823e-145db9d01feb | -9.70892 | -61.29299 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 127a0346-9947-34db-87a0-4d1a97ed7257 | -9.71373 | -61.30116 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d3ab1db-0289-3bac-b877-eb6f1e446dad | -8.91134 | -62.42841 | 2025-08-08 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1eab51f-4127-3ea5-a180-4677db00717b | -9.55519 | -47.88072 | 2025-08-08 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d334402-45e8-3aaa-8abc-c38babeb9807 | -13.03316 | -44.08577 | 2025-08-08 04:34:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2e1853b-b31b-32ee-9bf1-f86383cb119c | -13.36418 | -43.76536 | 2025-08-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9be848e-6843-3780-b854-cae3617640e1 | -7.36953 | -44.67331 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dc0f482-a400-3412-9c34-bd4ee2482ea0 | -10.43316 | -44.35414 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 990f118d-421d-3ac9-9323-e46b295a3742 | -7.81997 | -46.88172 | 2025-08-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cdb3938-3a14-3b44-b3c9-c13d2f65e23b | -7.90378 | -45.35637 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 381d350f-2ccd-3e71-8389-43c66167f155 | -9.65291 | -43.84245 | 2025-08-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5512f199-f6e4-3153-a1c0-bd1063faa31d | -7.30242 | -44.66839 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9efc959-ab59-3460-b849-b765753e2b32 | -11.73589 | -45.0023 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5a750f0-7a9c-3dca-8515-6a01d6d86d8d | -12.52285 | -47.11396 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d77ba014-edae-3905-b6d5-b24407f21f79 | -10.61854 | -44.76411 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 910a986c-701c-3a2f-a61a-3c0cbdf3c1f4 | -7.91081 | -45.55219 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22400ec7-ad32-38d5-b3c1-a834233ab3f3 | -12.58652 | -47.17827 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16bc8c7a-812a-3622-a3fa-d82d13ea3639 | -10.61471 | -44.76355 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dddafcee-2104-34a7-94d5-2bc91b260f87 | -7.8542 | -39.7103 | 2025-08-08 04:34:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a53f48ad-8cb6-3c0e-a117-a6f7b2c02eab | -9.9334 | -60.50509 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e9f09b-314f-353e-a719-4eaf3c251f2c | -12.54713 | -47.14159 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bb483b5-2e78-39b8-887f-539905fb1844 | -9.9416 | -60.46859 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d163044-1fe2-35f6-9bdb-da62899764b5 | -7.38679 | -44.24519 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c168fbb1-c572-368b-8491-a61d44cc6d1f | -9.07572 | -45.06445 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ddb2ed4-2468-3a6c-8cbb-61be1b85a8ce | -11.07285 | -48.3548 | 2025-08-08 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d6750e2-2455-3545-a53a-a21e894c45ff | -8.07001 | -49.71626 | 2025-08-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26f963d0-3f2b-347c-b072-e11f00da55e3 | -11.76512 | -47.5712 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
