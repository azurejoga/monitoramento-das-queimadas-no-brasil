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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e78a4d08-4ff3-3205-9e75-7d37608fed4d | -10.60995 | -44.7515 | 2025-06-04 05:18:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 303d8797-665a-36ad-997f-8da01f3aad34 | -6.96229 | -42.89584 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| adfe4dbb-64a7-34a1-8c12-77ee576f1bc4 | -8.07557 | -43.12093 | 2025-06-04 05:18:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 04b0e648-5d49-3cb1-9d1d-7f5907a43688 | -6.97023 | -42.90797 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| dd668712-da40-3f43-b8b3-c0963e93aefd | -7.00991 | -44.59819 | 2025-06-04 05:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 193ab901-9a98-3443-adba-9f70352afe7f | -8.07723 | -43.11031 | 2025-06-04 05:18:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 9742f0e2-b0b8-36c0-a31f-356aebc1eb88 | -7.01204 | -44.58478 | 2025-06-04 05:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2a611dc5-4c7a-3f1b-bcf2-69ce7ed01292 | -10.61827 | -44.76563 | 2025-06-04 05:18:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 08f3aa63-359b-3c42-95c2-8d67fd2dc644 | -7.0077 | -44.61205 | 2025-06-04 05:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c0b97c0e-8f3b-3c86-b171-2871a1ed5659 | -8.06596 | -43.11943 | 2025-06-04 05:18:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1cfd3def-7b70-3432-9d26-e5135c5b4e71 | -7.90011 | -50.36263 | 2025-06-04 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c52569c1-fc3f-3310-89fc-c4910f12abef | -4.80681 | -45.26322 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0d5e023-c3f1-3fb7-b16b-a589ad15959c | -8.75406 | -49.77479 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 42f2d49b-55bb-36ee-84b2-6dd9a8e04aa0 | -8.75753 | -49.77406 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6862ff5-394f-3825-8123-492f3a8093a1 | -8.84405 | -49.84962 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c790b7-4e04-36a5-aa8c-017fb8176d41 | -8.95374 | -47.27889 | 2025-06-04 05:18:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb025ad-7ee6-3a49-aace-b6e0ed852775 | -4.81377 | -45.26466 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfc32d7f-3038-3ee2-8806-7f3d4fd3a658 | -8.9523 | -47.28202 | 2025-06-04 05:18:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7773ae8e-5054-3655-83b5-ebea92762be9 | -8.75195 | -49.77323 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8218de5b-147e-399f-a1d0-9fec5a101a37 | -7.58293 | -45.86726 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f775071-59e8-3103-86b6-c1db6043d465 | -4.80768 | -45.25683 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8238b5c6-aaa7-3fb1-825f-8b55789b43b1 | -8.75457 | -49.77106 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11eb7660-22fe-365d-9433-95c6e89bc074 | -7.08148 | -49.59739 | 2025-06-04 05:18:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac98860-0ec7-39e7-ab92-a77df69a9df0 | -4.81526 | -45.26604 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ecf34fe-6981-36e5-a900-adc1796bd099 | -8.9072 | -50.0458 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c914860b-f481-389d-9440-0de6f6fe7c89 | -8.91319 | -50.04291 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e73f0685-5378-33b4-80f4-fc8d9529c2ce | -7.89687 | -46.18995 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18d9291f-a242-30b5-86bb-918c6d60cb02 | -6.29546 | -47.0083 | 2025-06-04 05:18:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b0828cb-1726-3bdc-84cd-b0c87268378d | -7.90541 | -50.36342 | 2025-06-04 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 408ffe48-b0ba-3785-9af7-82cf464d8d69 | -9.40014 | -48.43519 | 2025-06-04 05:18:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20b4f3b7-c88d-34d6-955e-e76b995a904d | -8.91236 | -50.04515 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f4778a5-23bd-33b5-8447-44ef0c75e37f | -7.88989 | -46.18958 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2354cae5-67c5-307d-a6aa-c695d2741c7b | -7.82148 | -55.37918 | 2025-06-04 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9d51e5-0de0-367f-8168-ebbef4d19745 | -4.24783 | -47.5846 | 2025-06-04 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c59e33a3-e08b-3241-860d-acf1630955b8 | -8.74899 | -49.77024 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9de1562-f6d8-3406-bb6d-ed9c4b33050c | -8.90767 | -50.04224 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 949f97cf-b2a4-3601-bd17-09ea3a407e41 | -2.53337 | -53.95802 | 2025-06-04 05:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925a00e0-07b8-3a87-8251-70eb06cc0605 | -8.75243 | -49.76949 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 127649a1-0661-33bc-9b1a-fa31bdf6985d | -4.80921 | -45.25826 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44e2abf0-2fee-3f6e-89cd-0fa7c22aff0c | -7.88912 | -46.19564 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de050779-7a2d-3b57-98d2-f865f77387a8 | -8.91271 | -50.04647 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f157060e-3be0-3cc3-b90c-0387ae9d6411 | -7.58751 | -45.86663 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e009a25-e30e-3f1c-89ae-6ba807a78adb | -8.75508 | -49.76731 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7cd6ad44-3b4e-3135-8c5f-72be1bc40aca | -7.90587 | -50.36013 | 2025-06-04 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4d55c36-96ea-39c9-9ba1-230c082dcbb6 | -6.86669 | -47.84835 | 2025-06-04 05:18:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e63ad35c-1971-31ef-b0db-bcee484cec41 | -6.29477 | -47.01342 | 2025-06-04 05:18:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 653ffe47-af43-38b1-b582-eabd65faf40a | -7.58833 | -45.86012 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9ae2853-9268-34e1-9fdf-521ba3e865b8 | -4.80829 | -45.26471 | 2025-06-04 05:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c76214a3-4501-3f40-87f0-056167ef17c0 | -6.86733 | -47.84364 | 2025-06-04 05:18:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ae6c927-3f06-35f0-9e51-15d4f3014335 | -9.39401 | -48.43427 | 2025-06-04 05:18:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 368d9240-d651-385a-a8a7-d0f5464bf194 | -7.90632 | -50.35687 | 2025-06-04 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19c30883-2d4e-334d-a163-c68da98f5a33 | -7.90056 | -50.35938 | 2025-06-04 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5aa203e8-cb49-3c5a-974d-51858dd528bb | -7.9854 | -47.2355 | 2025-06-04 05:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c7d97f2-6837-3ce3-be23-8a57a009ab73 | -7.88909 | -55.36402 | 2025-06-04 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a219b2-0a26-30e6-9507-a2b6d948254e | -7.88303 | -46.18826 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5382c9fa-8fdd-3a24-bf90-a6d1f96eff79 | -8.75801 | -49.77031 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08a6eb4e-be15-3318-8040-1aaf85dbb432 | -7.58379 | -45.86084 | 2025-06-04 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c266f51f-64c1-3268-ae9e-f46b7deb50b9 | -7.97951 | -47.22996 | 2025-06-04 05:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f018ad61-c00e-3ce3-9ec5-ff41175ae6a3 | -8.75291 | -49.76573 | 2025-06-04 05:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 498434fb-135c-3055-8f3d-a38bcdc6be9a | -2.95599 | -60.01632 | 2025-06-04 05:18:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d8ded6-66a1-313c-820c-1c7c8fb0ff97 | -6.9602 | -42.9052 | 2025-06-04 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| cb3d9512-aa0c-3c49-ae54-0fbb89fb03f7 | -14.71391 | -45.09454 | 2025-06-04 05:21:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 55fe768a-928a-31dd-bbf0-9856052a2272 | -11.64155 | -58.01714 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a19c542-9f94-31c7-a551-30cc30550e9a | -14.33777 | -54.13885 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576a981f-a755-30fc-bb56-fea570964207 | -13.96082 | -56.77903 | 2025-06-04 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1d9b8bb-d8a3-31cc-ad68-2e3381bc9e86 | -9.41094 | -62.44792 | 2025-06-04 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5c386cb-625d-3f97-9382-7178d4f20f9a | -11.91888 | -54.80949 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ab29496-5d37-3c24-8ffe-c01732c5e677 | -12.64551 | -54.12114 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 642bccf6-c9db-3335-9837-f693ea88f693 | -10.69691 | -57.64553 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d563307-44f6-38c7-b5d8-1d21d5a464dc | -12.17272 | -64.19973 | 2025-06-04 05:21:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3829b58a-ca80-3c86-9211-ac4cfb900392 | -11.55888 | -56.4193 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d06c0ee-eb12-3e80-b1b4-abc605b459bf | -12.51732 | -57.1821 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172406b2-d403-3d5f-9f17-e049cd5c3ec5 | -12.51795 | -57.17781 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe8dbec8-8311-338d-818f-dbd902502e50 | -10.68991 | -57.6445 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33cca85-3cc7-32c4-ba54-36dcd26cae99 | -11.83864 | -51.28192 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77861433-fb23-304d-9cb0-0b95faa8b34d | -11.64508 | -58.26346 | 2025-06-04 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1bcfaaa-3b61-3716-9a2e-6f1eec84a1f0 | -11.90788 | -47.45441 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc20600-d79e-3c14-a396-663c1d509ab2 | -11.55513 | -56.41876 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cf5d364-24a1-338a-a042-607c58843312 | -8.67391 | -64.26828 | 2025-06-04 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abcd3d4e-2c32-3c9e-83b8-afb73bc256d6 | -11.92026 | -54.80824 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dea11c2d-393e-3e2c-985f-13b387e49f13 | -10.69341 | -57.64502 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13fd5800-4689-38f0-b3e1-2c5dbebc2edb | -11.90024 | -54.7914 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f8e8d19-3830-3e13-af6c-58fda5623691 | -10.832 | -56.96082 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19a1855b-4e2a-3b46-a2cf-45c65caa4464 | -11.25275 | -49.49158 | 2025-06-04 05:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b92dce2-e2e6-3e2f-8409-f7e9e4d01b01 | -10.49456 | -53.6576 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 78fd2228-bee2-34c4-ae62-9dde70561765 | -10.26125 | -48.45387 | 2025-06-04 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c88f31aa-4344-3d5e-bd97-ea3a1f91d861 | -11.38335 | -56.54684 | 2025-06-04 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03237e1f-4075-3dd9-a17d-c876c66ff734 | -13.09579 | -52.02479 | 2025-06-04 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6309c762-8f08-3ebf-91d1-b258543d5f6e | -11.5494 | -56.4318 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d89a0686-c5d2-3b2a-9517-36eff8fc97bc | -12.04516 | -53.43819 | 2025-06-04 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e6925e9-4c78-36b4-900a-32021a8ee1b4 | -10.38439 | -53.5115 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27eeb2a1-b98c-3cd2-a9cc-a096e84e3905 | -9.25419 | -56.31798 | 2025-06-04 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a998507-1121-31cc-abf2-554c743758bf | -10.69633 | -57.64941 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f129f05-b1b9-3a2e-876f-a5bc12d7a998 | -12.16897 | -64.19906 | 2025-06-04 05:21:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70c127fd-afc9-3854-8093-a847b94eaee2 | -14.56336 | -59.49699 | 2025-06-04 05:21:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632d10bd-1cb2-360a-8cf1-f353f39d3bea | -11.55446 | -56.42331 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72f60aa5-f64e-3204-909d-4e00e03cd90c | -14.02489 | -55.13338 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3a07150-5eed-39d7-bcf6-6184260fc8a2 | -11.83815 | -51.28141 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edeca6e2-d6a6-318e-b764-41573b8ff66b | -10.68583 | -57.64785 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b636bd6-32c8-3be7-b2f5-1287bec9c522 | -11.90185 | -47.44772 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
