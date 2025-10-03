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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a739ebb-6ca7-38cc-b6fd-5c16b0ddacb1 | -12.7627 | -50.5567 | 2025-10-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| cb60875c-3438-3309-9444-299c94aab53d | -8.1699 | -44.1608 | 2025-10-03 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6af29c77-efba-3a70-a950-461c91f6594d | -10.2781 | -50.3032 | 2025-10-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fd6ddb66-4151-307b-8a96-538c1fdb6afa | -13.1973 | -50.9095 | 2025-10-03 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 640018e8-7382-36f6-b8f6-b78f7d24213d | -7.2911 | -45.2775 | 2025-10-03 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 87a4d670-82cf-3911-895b-d37ff28c0b4f | -9.355 | -45.9284 | 2025-10-03 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 5e8052fb-93e8-318d-b51d-9abdefa0143e | -7.8165 | -46.9781 | 2025-10-03 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| be199730-b3eb-3f11-bd97-aca0bda262cb | -10.222 | -50.2662 | 2025-10-03 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 094ef143-d30e-3046-9e5c-0221d816c409 | -9.3357 | -45.9532 | 2025-10-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0b8d82c1-4329-376a-be5d-8e8e4191363e | -14.6497 | -44.7499 | 2025-10-03 13:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ea98d4b8-8acc-38c4-bc53-e07614e85e3f | -11.458 | -45.1357 | 2025-10-03 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c74d4ac4-76e8-3cf8-9889-9c95623f0154 | -13.1341 | -47.9043 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d2589586-ee4e-3764-905d-bdbd9d63d586 | -16.0583 | -51.0454 | 2025-10-03 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 74a2ae69-610a-3a90-a11a-264ed6ff126b | -7.7496 | -46.2496 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d45a53ac-51d8-3e37-b6fc-d9c060544741 | -13.155 | -47.8121 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 071f8bb8-c0a5-32bf-9abe-302e9f6bbab2 | -14.0027 | -44.9845 | 2025-10-03 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 2f24cb9c-7261-37e8-a817-c47161c613a9 | -8.1699 | -44.1608 | 2025-10-03 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 8b2159c3-bc36-35d5-ae4d-ba878785110c | -10.948 | -51.0846 | 2025-10-03 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 47f48920-0e83-3878-b0ef-33c6cd3a189d | -7.7499 | -46.2272 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 1d84b5f4-afa1-366d-ba1c-65e1069f4508 | -10.2779 | -50.3246 | 2025-10-03 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5d093dbe-3899-38c3-8e84-f8337b563203 | -14.0032 | -44.961 | 2025-10-03 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 283.1 |
| cd80d5ac-5337-37bd-864d-9ca0a6799ab7 | -8.8343 | -46.7694 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 97430e72-5328-3d27-8fa9-3431b5a8102c | -7.7687 | -46.2255 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 11319b91-7b64-3139-9d83-5b4039905db5 | -12.7435 | -50.5591 | 2025-10-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3c1010a9-c063-320d-b4d3-93223109ebe9 | -9.3386 | -45.7493 | 2025-10-03 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 85f5ad8e-445c-30f3-b177-e095958c16c0 | -8.9118 | -46.6052 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4eef2cff-5785-3903-bfb8-16a736418de5 | -13.1973 | -50.9095 | 2025-10-03 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a5cc9d0c-5cd3-3aab-9443-9d6d9aa35d13 | -9.8772 | -47.8103 | 2025-10-03 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4e3e3f0e-98bb-3c51-92d6-f9688eaf5822 | -12.7627 | -50.5567 | 2025-10-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 739e9c00-661d-3ca6-9af0-481c7fb5f3df | -12.5305 | -47.2988 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| dfa5ec18-5cd8-395a-8690-5da04d02d826 | -14.0037 | -44.9376 | 2025-10-03 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 5a54d0a2-c746-3cea-8a59-3f00570a1426 | -8.5599 | -44.6494 | 2025-10-03 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 32e26bb9-8250-3461-a587-6458696472d8 | -10.019 | -48.4964 | 2025-10-03 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 1ecce747-09d0-3ae5-864a-5b23bfddf9de | -15.7905 | -43.7155 | 2025-10-03 13:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 160.1 |
| d0f3ab93-fcff-3902-96e9-f00a47cb85df | -7.646 | -45.4489 | 2025-10-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0de845fd-b3c2-39a9-bf05-572328e0119c | -9.1813 | -46.1956 | 2025-10-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 71ce891e-90c5-338d-9bca-8c1b33670346 | -7.2845 | -44.18 | 2025-10-03 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ca888ee3-5bc7-33e2-b98e-9c0fce0f77aa | -9.9369 | -43.7422 | 2025-10-03 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 0b5ac2bc-54cd-385c-81ab-724cff71dfd7 | -16.0779 | -51.0424 | 2025-10-03 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 120.5 |
| fbbcab10-df28-3784-ac01-7bc5e4daab5c | -13.1534 | -47.9015 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 5a9cfe17-5ce5-33b3-a0da-56779ddfd7ca | -10.297 | -50.3013 | 2025-10-03 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2b2a3942-7a94-3f54-918f-11e51c803ea0 | -13.8244 | -51.2997 | 2025-10-03 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0a2c203b-0bfb-31a4-be39-696548c1d286 | -11.5687 | -47.6526 | 2025-10-03 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 055ed016-65bf-3153-aee9-9fd580f66ed7 | -13.8055 | -51.2807 | 2025-10-03 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| d3e1eeae-c5d8-31c2-89ba-2e6d2f6787e0 | -11.1444 | -43.3845 | 2025-10-03 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 101.9 |
| df73c913-3109-30fc-afe0-5cf811cb941b | -7.7684 | -46.2479 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 241.6 |
| dc14872d-bb77-3237-82bb-fa0a335d4b1d | -6.0809 | -42.4881 | 2025-10-03 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 0094d2e5-a5bb-3015-a341-80034e0b5d86 | -12.1088 | -45.1554 | 2025-10-03 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b593b945-02d6-3154-8ce8-03cd347d6cd2 | -14.2939 | -45.9076 | 2025-10-03 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 57f9aece-a08c-3c73-ab80-0d440364c705 | -8.8543 | -46.6781 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 7f25d16a-bc10-3630-963c-7908c2bd85e1 | -8.5959 | -44.7833 | 2025-10-03 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5443a40d-dc90-3f4f-a18e-02820f3e37d6 | -9.355 | -45.9284 | 2025-10-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4a269c63-db55-379a-be92-e44d8b929f88 | -14.607 | -46.7249 | 2025-10-03 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| fb680a85-12b8-3ab9-875b-edb2fb0489b9 | -11.8818 | -44.9815 | 2025-10-03 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 82ef76fe-2523-3dc1-988a-2244626bb73e | -6.6787 | -42.8372 | 2025-10-03 13:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 7bd3a285-7fe9-31aa-84c2-13a2110e6d2d | -9.9182 | -43.7212 | 2025-10-03 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| b5530d47-51e8-3673-a7a9-9079be3cb74f | -13.3418 | -48.1188 | 2025-10-03 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 9f901aa6-5e97-393d-a0f7-9fef08e44c40 | -13.1152 | -47.8848 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 135ebafd-936b-38d6-aafe-2b093fb455fc | -11.1271 | -47.8856 | 2025-10-03 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 63109ad5-0ebc-3f38-a73c-19a5785e3e74 | -14.2316 | -46.1024 | 2025-10-03 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2334a09d-b323-3142-989c-04834d402ae1 | -18.9673 | -48.4968 | 2025-10-03 13:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 50e9bebd-7eb9-3b34-9673-b1072fb2b61d | -6.33 | -43.8716 | 2025-10-03 13:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ca59fb39-0f58-3ed5-8a3e-7c586aacf95a | -7.7682 | -46.2703 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 19357fce-42dc-311f-b2bd-94a31ab8189b | -13.3422 | -48.0965 | 2025-10-03 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1e1f491f-7489-3952-8f3a-821e6b8a6365 | -9.9394 | -43.5777 | 2025-10-03 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 9c9b4a76-f46b-399a-844f-3f5e160c4f4f | -7.3101 | -45.2531 | 2025-10-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 0f0183bd-7c8b-3000-a8f8-400e18a25cba | -10.345 | -48.176 | 2025-10-03 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d07ff0be-745b-3fb0-9367-d196a4125483 | -7.7746 | -47.3792 | 2025-10-03 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fc8e7c54-2d27-3c35-86cf-c57dc1288e0a | -10.2781 | -50.3032 | 2025-10-03 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f323188c-5325-3e12-b3ef-98ed38d5594e | -13.1727 | -47.8987 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a137cb13-6bea-3ce7-acae-f6744049f51a | -18.9667 | -48.5198 | 2025-10-03 13:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b2d6425d-5826-3613-b6b3-51f3c5cb4f83 | -11.1275 | -47.8634 | 2025-10-03 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2d9e4407-06c2-3531-887c-e60748894b79 | -7.2913 | -45.2548 | 2025-10-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 66751ef2-77f3-39d3-ac8c-32e88b4e77ef | -8.1702 | -44.1377 | 2025-10-03 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b240872f-127f-3a9c-b7b5-71e4b24c6231 | -11.9159 | -46.3044 | 2025-10-03 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 9bc4653e-6850-30cb-b2f6-1aa1b222cdbc | -8.8729 | -46.6985 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 256.6 |
| e5a20f49-c14b-3e76-ba45-d83cae65c7aa | -11.8238 | -45.0132 | 2025-10-03 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6702ad45-4013-3fc6-be00-f6a714edd4d1 | -13.1546 | -47.8345 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0ee18f13-3b5f-3263-b75d-4b2a8f2d72fb | -9.3547 | -45.951 | 2025-10-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 634f0ff7-f5f2-3a33-b67a-24b57bbd257d | -13.9771 | -48.1793 | 2025-10-03 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 437f466b-ae6c-3b89-b632-80c3b3e95c35 | -6.0806 | -42.5118 | 2025-10-03 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| e36f9bd4-da35-3c25-bcf5-9825d2bea737 | -13.1156 | -47.8625 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a43fbeec-010f-337b-8203-085e470eb4ee | -6.679 | -42.8136 | 2025-10-03 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 08d13a9e-6940-310f-933e-c92c8937613b | -12.6131 | -46.9725 | 2025-10-03 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| d1b23abf-65db-36c8-be79-c54f56c32940 | -8.1917 | -47.0101 | 2025-10-03 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e13d1a58-8ce5-384b-9430-47116382d63e | -9.9186 | -43.6978 | 2025-10-03 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 33d4a684-6709-3c00-97a8-6cd615025882 | -13.1345 | -47.882 | 2025-10-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| f4a0c9e6-14b5-31f3-b255-fdfa784981f8 | -13.7865 | -51.2618 | 2025-10-03 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 420e03bd-18fe-3263-bd0b-26a8c475319b | -9.9035 | -45.9553 | 2025-10-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 63f46ef7-2ef3-3a56-8942-a8a0f3c52009 | -7.2911 | -45.2775 | 2025-10-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 306.0 |
| 17c68946-fabe-3c72-8d31-15b42657d9f4 | -12.9314 | -46.3818 | 2025-10-03 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d2c93281-f97a-328c-9cfb-e3279051cd19 | -12.1215 | -43.4453 | 2025-10-03 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b50fefbc-3ab4-3cd7-822c-3964faa29523 | -10.0278 | -44.0108 | 2025-10-03 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 9ebece3c-ee63-302a-a9bd-a16c003caf68 | -6.3297 | -43.8948 | 2025-10-03 13:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e28066e3-f406-36e7-a3f7-736256c0fd17 | -6.6976 | -42.8354 | 2025-10-03 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 17107c45-d10b-37f6-9017-b727617d1f5d | -11.9155 | -46.3272 | 2025-10-03 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 415.9 |
| 19f89919-ba2b-3982-b8ce-031f264cacc4 | -7.7933 | -47.3776 | 2025-10-03 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6c9f85d8-f038-3a14-b0a1-1f89879870b0 | -9.8769 | -47.8324 | 2025-10-03 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e675c1c0-81dd-39c2-a0ac-f92d7ebc3cb3 | -8.9948 | -47.4845 | 2025-10-03 13:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cedd6b2d-5115-390e-8ed3-73903cf647cb | -7.7494 | -46.272 | 2025-10-03 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 202.9 |


[Clique aqui para ver as próximas entradas](README150.md)
