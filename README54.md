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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39cc7d5a-4dd2-3b75-aa24-7731d7c39e44 | -11.4033 | -44.9822 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1a704aa5-c696-38e4-a64a-cead99c34641 | -11.9655 | -47.8891 | 2025-09-26 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c2f29c84-66a8-3833-bddf-ed6ea1f8cb36 | -11.385 | -44.9386 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3ffd1069-07e5-3962-9f1b-e53172a25994 | -11.0131 | -44.3424 | 2025-09-26 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 562972e4-0941-360d-ba29-dacb1620bc49 | -11.6814 | -44.4078 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 3919eb04-f06c-302e-b4da-383961334032 | -7.6584 | -46.0114 | 2025-09-26 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| ea51a1a5-e128-3964-a25b-443cf5cc91c4 | -6.9303 | -45.6931 | 2025-09-26 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 08fc9702-bee7-3e04-927c-7815d500c803 | -12.1031 | -43.4008 | 2025-09-26 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 0ff50b78-e48a-3b57-8ac0-85bb2731e236 | -13.3463 | -47.8732 | 2025-09-26 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 69ee756b-6fbf-3753-a0d3-745a9d4501c9 | -10.1217 | -45.3148 | 2025-09-26 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a0bf59c2-2068-3861-b685-4530e9232e00 | -9.8921 | -46.7437 | 2025-09-26 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b106e21e-223e-3919-abe9-bc1ffd1d935d | -7.2206 | -46.6084 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 4db4226b-504d-3095-b618-06b4d995f688 | -7.6772 | -46.0097 | 2025-09-26 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a2a20094-e3ef-31f8-a384-3d824dbf292f | -5.475 | -43.0774 | 2025-09-26 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| dbec1868-75f9-3abf-ac22-7614ea79e97f | -20.7338 | -57.8083 | 2025-09-26 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 225.0 |
| a39e0743-369e-3356-bf88-260c504db297 | -17.1746 | -56.3478 | 2025-09-26 13:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| e929c609-5117-3ddf-ae84-e5506250800d | -14.8309 | -45.3714 | 2025-09-26 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3ed822a9-2937-33c4-91f9-26211fe36db3 | -14.1153 | -51.1753 | 2025-09-26 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7c29b9b9-53d2-30f6-bf11-05a820ef0c64 | -10.8051 | -45.3866 | 2025-09-26 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b29ec4c1-03db-37a3-b064-df0c76b94e68 | -7.8735 | -45.2911 | 2025-09-26 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4972c3c6-ff2b-3ef4-8692-ef31d8619123 | -14.0309 | -45.4911 | 2025-09-26 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| edf1662a-b170-3019-ad72-8169372aa636 | -10.9377 | -44.2832 | 2025-09-26 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 3ef6f3f5-2578-3b47-a60e-5093276e324d | -20.7342 | -57.7873 | 2025-09-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.5 |
| 6dff2f77-f157-31bc-b2ae-46787f1b4a17 | -11.7006 | -44.4049 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 0f2955b8-5309-3455-b295-ea031167d79f | -11.7019 | -44.3347 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 8beb5263-692d-35b7-95a3-d4e755e97877 | -10.4129 | -46.142 | 2025-09-26 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 84e78222-ce54-333b-8bc0-db7be3c584d9 | -13.3463 | -47.8732 | 2025-09-26 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3a2a603c-8e72-3fd9-a6d8-20859ac93352 | -7.6772 | -46.0097 | 2025-09-26 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| aa7a0c70-47a7-3605-ae09-69498cfcb082 | -11.4102 | -43.5099 | 2025-09-26 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6ae29e3e-06b9-3e2a-80c8-e01366b95bd8 | -7.2796 | -42.9685 | 2025-09-26 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 47b79f9e-37ee-3fc9-8f0b-009ce60d3e71 | -10.5979 | -44.0741 | 2025-09-26 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7148b699-b18e-399f-aecf-facaf1a81c6b | -11.6826 | -44.3376 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| eab531bd-26eb-374e-8a09-a6221e48f66a | -10.0062 | -44.1766 | 2025-09-26 14:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 044409ee-19ed-33f9-81b8-f1d1fad29a53 | -20.7334 | -57.8293 | 2025-09-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 197.0 |
| 8bef0ea9-873c-3f07-8bef-90b6d2c486a8 | -11.044 | -45.9249 | 2025-09-26 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0c53dde8-7fcb-31f1-952d-ac814ba2600f | -11.0635 | -45.8996 | 2025-09-26 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6fa22922-ba9a-327e-bf3c-d2b497dab17b | -8.7708 | -43.0417 | 2025-09-26 14:00:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 67bf7773-0430-3292-8412-3a10224d9746 | -10.9377 | -44.2832 | 2025-09-26 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 00d16ed9-6695-3cc4-b311-f914227ee52d | -11.4229 | -44.9563 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6f0c98bb-2e5a-3345-813c-9c7a1783907b | -13.7123 | -47.8851 | 2025-09-26 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 561f71e1-6316-3749-a968-24587c4ec25b | -10.3938 | -46.1444 | 2025-09-26 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9709cccb-9b91-354a-ae6a-7d38d60f6062 | -10.8051 | -45.3866 | 2025-09-26 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 4a9b8d77-73bc-32bb-bd7a-859fbc2f8607 | -9.8658 | -45.9372 | 2025-09-26 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b319873c-e913-3396-a7fc-0e5ec1f548cb | -17.1746 | -56.3478 | 2025-09-26 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 60289b53-ff3f-37c8-83ce-866c9c1de328 | -7.2206 | -46.6084 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f5bbfc05-eb86-3fe2-b98e-c1224ea743bb | -11.9655 | -47.8891 | 2025-09-26 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f415bf4f-178c-30b6-a2a6-a08427987f50 | -10.9374 | -44.3065 | 2025-09-26 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e4055c3d-ab62-3b45-b343-aecffffa4338 | -5.4752 | -43.054 | 2025-09-26 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8554772e-d370-3883-825d-cc638cbf5550 | -14.1153 | -51.1753 | 2025-09-26 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1c29c970-d806-3023-90f6-1410fd49f488 | -11.6233 | -44.4398 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7471b0e4-60ed-35fe-a8bb-410d8c087e6f | -11.385 | -44.9386 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f59fc130-a663-37e7-8a95-fa5afda7ec90 | -14.8304 | -45.3947 | 2025-09-26 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3b537b6e-9a61-345d-9267-d53f0146b070 | -10.4125 | -46.1647 | 2025-09-26 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b09c5a33-8e5e-3068-9787-34ee52da7468 | -11.4033 | -44.9822 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a756ed81-030b-3339-b65a-a75369093097 | -6.9303 | -45.6931 | 2025-09-26 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 3a0456c8-7639-38d9-a661-664f528eee87 | -11.0131 | -44.3424 | 2025-09-26 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a5b2c71e-71ef-350e-a931-ee6720595764 | -8.8409 | -46.2544 | 2025-09-26 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| b0b2dca6-0aa7-3365-ae8a-45a7a3871c4f | -5.3695 | -42.284 | 2025-09-26 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 78e56af7-48fa-371e-a548-018ce0ca61de | -20.7338 | -57.8083 | 2025-09-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 535.1 |
| 50f94eed-ee20-3d86-a761-dd72c8a4c712 | -11.681 | -44.4312 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f5bf4a5b-fbf4-3a06-b055-5157e803b5ce | -12.631 | -48.1313 | 2025-09-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bdb61091-8319-3a44-b9ec-51b45d0ee0f0 | -5.475 | -43.0774 | 2025-09-26 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 580668d1-a856-3744-a930-7a2d89def6cc | -11.6238 | -44.4164 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 406ae005-02d0-3d96-9a77-472e9498c8cc | -17.1743 | -56.3685 | 2025-09-26 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 725a38c4-cca9-3943-86fb-b1bb0f302534 | -6.5801 | -45.1117 | 2025-09-26 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| dcea5c0a-4d0b-3768-bb4d-da98a53d5319 | -9.8921 | -46.7437 | 2025-09-26 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1df266c1-e5b9-3651-a4c6-99f5efd53f1f | -11.9659 | -47.8669 | 2025-09-26 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0cd5df38-511b-38ca-b2d2-5e78546573c0 | -11.0444 | -45.9021 | 2025-09-26 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 2cc10dbf-ce5e-38e0-af70-fd1e2037566f | -11.4225 | -44.9794 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 474.0 |
| f5e315cb-835b-3835-a7a5-44ef648cb9d7 | -8.8415 | -46.2095 | 2025-09-26 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b00a5981-cca0-3654-bb9f-42ad65fcdcf2 | -8.8603 | -46.2075 | 2025-09-26 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1061a441-815f-327e-a382-8d6498f45e22 | -5.4562 | -43.0788 | 2025-09-26 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9a1356ff-8c61-3a93-b063-7b32e16dd605 | -12.3424 | -50.5655 | 2025-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 08b4bf11-688d-3745-96bb-c6389aff1d86 | -13.3266 | -47.8984 | 2025-09-26 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| d3d46fe3-22f4-3d43-b739-2c4fa8fd407b | -5.3091 | -42.761 | 2025-09-26 14:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| dec3e30d-185f-3632-9c05-ed1b86698db5 | -7.3559 | -46.2177 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ac09c377-fea0-3de7-857b-db897667e3bf | -5.4565 | -43.0554 | 2025-09-26 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| b20ebac6-65e5-3fd9-b529-f53b96ec3f87 | -20.7537 | -57.8265 | 2025-09-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 80f7318e-6b75-34cc-b364-a7ffd97473e7 | -9.5648 | -48.5877 | 2025-09-26 14:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ebbfa3a3-51af-3ab7-a238-d59771939770 | -11.6457 | -45.3388 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 43175d54-0254-3d56-8642-4a5c6df642fc | -7.6584 | -46.0114 | 2025-09-26 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 79fb6963-e504-3cbe-b042-8266b9193cac | -14.0964 | -51.1564 | 2025-09-26 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9cf62079-c3a4-3128-8078-9e4c4aed4777 | -7.8735 | -45.2911 | 2025-09-26 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 7226098f-5606-34bb-9c8f-1db600fb44af | -7.6775 | -45.9872 | 2025-09-26 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 0dacc6ab-84b2-32b2-9392-00eb93fe0c03 | -11.7977 | -47.6449 | 2025-09-26 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d2e2ee4e-66e6-36c6-a76f-082b3cf3c956 | -6.9115 | -45.6947 | 2025-09-26 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c886158f-93d0-3a5d-9f12-fbbc7110bcde | -11.6814 | -44.4078 | 2025-09-26 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f5df23ef-4fb7-3c35-9cc4-2e3a734c54c3 | -8.1363 | -42.3801 | 2025-09-26 14:00:00 | GOES-19 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 9612a07a-5c4b-3ad9-92c8-022fb43e9a81 | -14.7723 | -60.191 | 2025-09-26 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1d5478da-3835-345c-aebc-e859d407ab11 | -7.3371 | -46.2194 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3189cf6e-c8b6-3344-9355-9264766dbff6 | -8.8551 | -46.6111 | 2025-09-26 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1437cbfb-bfbc-3467-aceb-bbe61b0c5ad1 | -13.201 | -47.4026 | 2025-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 594bc95d-fda4-3b12-976c-be8443a95eab | -10.5975 | -44.0975 | 2025-09-26 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b9f64f3d-3800-366c-a8a4-e7d1d3b974a5 | -12.3427 | -50.544 | 2025-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2836eee1-e2fb-37fb-9f71-90312698f8df | -17.1939 | -56.3661 | 2025-09-26 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| eb32ad3f-6173-380c-9a45-0cf3cd8c0549 | -7.2203 | -46.6306 | 2025-09-26 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b95cb0fe-7adb-33ca-b2b8-c7ba36a446f2 | -5.4752 | -43.054 | 2025-09-26 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cf1b0cd7-c395-372e-a047-b9cea4549f3b | -5.7775 | -42.7961 | 2025-09-26 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 8000a73b-710d-30c6-9b2f-437ed220d24d | -6.0782 | -44.719 | 2025-09-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fe1f0d6d-c0f9-3420-8637-345b0ea78d63 | -10.9377 | -44.2832 | 2025-09-26 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |


[Clique aqui para ver as próximas entradas](README55.md)
