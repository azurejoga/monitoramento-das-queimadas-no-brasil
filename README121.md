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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 461f7f67-fc6f-31a7-9d0b-fca328cc3db5 | -15.45815 | -47.33447 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8b393e89-6416-3cc2-9200-745e25ee3639 | -15.4734 | -47.33744 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 62eb036e-1c44-3bd8-90bf-fba23dcb35f5 | -14.21964 | -46.28782 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 9c0393e3-0255-363b-bfaa-68307c883054 | -10.36977 | -45.4301 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7def2b7c-3fff-329a-8a9f-d9e28f767614 | -14.17922 | -46.16444 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 7957c196-b353-3183-9c73-dd32ba89d0cb | -12.1288 | -44.83793 | 2025-09-13 11:38:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| c7b3f230-c233-3965-951d-73a48f1e8370 | -16.32292 | -43.10701 | 2025-09-13 11:38:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 13917ae7-8fa7-3049-9a5d-98b56d6da7f3 | -16.40776 | -41.31497 | 2025-09-13 11:38:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| f93e2237-5300-36d5-b572-f8efda6ac3f5 | -11.4403 | -45.60582 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 56324470-7ddd-379e-b079-f12fac0e64b8 | -11.87061 | -46.75829 | 2025-09-13 11:38:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f3975083-16f1-3f34-9afe-5fd7409d5b08 | -11.71785 | -46.5573 | 2025-09-13 11:38:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 6c0a88ed-b19f-362c-9f62-99f01781e8a2 | -14.3027 | -46.09159 | 2025-09-13 11:38:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 840edadf-8921-3426-a34a-f164a160911b | -14.16086 | -46.26914 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 258d9127-c25b-3f63-87b0-20f293eb7f5a | -10.94038 | -47.2067 | 2025-09-13 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 187ba3a0-e598-34aa-97fd-15b7c39525ed | -10.36886 | -45.42391 | 2025-09-13 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d039b8d4-01b2-390b-83f8-64636996945a | -12.8381 | -47.92659 | 2025-09-13 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 275.5 |
| eebab174-2812-34a5-aec0-bcc70e04cf00 | -14.28539 | -45.09552 | 2025-09-13 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 710e1413-c5b0-3d69-a11b-1c828217bbb5 | -11.75861 | -46.59785 | 2025-09-13 11:38:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e372803e-f299-3a14-8df9-fbec7ea20829 | -11.86409 | -46.7645 | 2025-09-13 11:38:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 81172cb6-0f20-3b68-aef6-d899f3a1e43b | -14.30732 | -46.06604 | 2025-09-13 11:38:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b27cc589-e839-3b8b-8b9f-a5c4d79c8933 | -12.59093 | -45.71126 | 2025-09-13 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 8ea4a9cc-7ee7-3a7a-b228-6da22baedddf | -14.1754 | -46.27134 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 273.4 |
| 87e84e47-c42a-3b94-b5c3-09e630496a90 | -16.31954 | -42.30591 | 2025-09-13 11:38:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| a2e45f20-2482-3509-a867-f6214eb3612c | -14.21459 | -46.23267 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 464b15ff-3077-3569-b4a1-e23cee887303 | -12.93204 | -40.38791 | 2025-09-13 11:38:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a823c3a9-7baa-3530-8c5f-a57de6efdb6f | -13.92156 | -48.20914 | 2025-09-13 11:38:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| bcb82faa-97db-39e2-a5f6-87016516c3ac | -15.04841 | -47.9778 | 2025-09-13 11:38:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 61886e16-6258-3bed-8ff1-7e0bb314b11f | -14.82758 | -40.91858 | 2025-09-13 11:38:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3bbf1907-a02d-3d6a-9f52-23fac50465a7 | -14.16693 | -46.16792 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 52d8092c-fa05-33f9-af70-b36be9f63b1b | -16.32316 | -42.29987 | 2025-09-13 11:38:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 2de21fcc-2348-33fb-9f89-e1c1b42d2d82 | -11.44163 | -45.61212 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e1d7c330-fecf-3c5c-aac8-b1f263f3ea4b | -10.93371 | -47.24312 | 2025-09-13 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 16f021d1-8ad4-3aec-b594-dd9f29f4ec68 | -15.86241 | -47.21883 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 783925e0-e815-34b0-ba88-d1962acb0e44 | -13.82534 | -41.75551 | 2025-09-13 11:38:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cc4e1f27-47d9-31cc-847c-ed7d4b7c747e | -14.2816 | -45.10074 | 2025-09-13 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e1ac223c-5e7f-3a5c-bbdd-259801a7956f | -15.87728 | -41.93715 | 2025-09-13 11:38:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3bb19f2e-4193-343b-a2fd-16babea7fca5 | -10.92838 | -47.23615 | 2025-09-13 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 66e4a283-7f7e-339a-8020-4058101477f0 | -10.93483 | -47.19963 | 2025-09-13 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 49280a16-b514-391c-96e3-567237e81ff4 | -12.85484 | -47.92977 | 2025-09-13 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8e55c809-65b3-3bfe-a5c1-3fd329971944 | -15.46929 | -47.34421 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 37973ebe-8a47-3ffc-a1c5-abaa44919fe2 | -14.16574 | -46.24132 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 225cddae-1727-34b7-9546-f0526779c6c8 | -14.21487 | -46.31462 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 226.9 |
| cbf8d320-9fff-30a7-b264-d1f46c64d35d | -14.20528 | -46.28463 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 131.5 |
| c1c958a2-09bc-35e4-8da1-05067dad5175 | -12.92744 | -40.39164 | 2025-09-13 11:38:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 8f1817ac-ece6-31ff-92af-d7f302161946 | -14.3139 | -46.08791 | 2025-09-13 11:38:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 1c0af39d-898f-3818-9979-951339eac592 | -12.87629 | -40.40559 | 2025-09-13 11:38:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f49edcc8-f0f2-386c-9dce-6ea801eb643f | -14.16195 | -46.27633 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3f572c06-a941-3e30-bacc-c0e164b95e7a | -12.8255 | -47.92974 | 2025-09-13 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 6bf6f188-40ac-3df9-8b93-931f4b42f24f | -12.94065 | -47.9906 | 2025-09-13 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 51e89c66-3cee-3abd-8d54-fdc329243cd8 | -15.85706 | -47.24861 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e525da7a-01c0-32a1-b05e-f9ed2a1fbd6c | -15.87511 | -47.22861 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 70c86b98-78a0-3eea-9e14-78d24c2a7aea | -14.17652 | -46.27838 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 357.9 |
| d14d841e-5d55-309c-848e-e2c79e315149 | -12.58871 | -45.70382 | 2025-09-13 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 241efdbb-125e-3eb5-8ca5-6164b4219cb4 | -15.8546 | -47.2551 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| dff64eea-e062-3f69-8e91-adf6885537b7 | -11.8284 | -50.5406 | 2025-09-13 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a2bea4fb-6f05-3b00-97c1-a0969b9726d8 | -14.1698 | -46.2735 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 278.4 |
| 4cbbbb83-1576-3108-8d47-cbb760f3690c | -16.0805 | -49.9489 | 2025-09-13 11:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6c3ee5cd-5fb7-3472-8815-0dc1a8b6c3bf | -16.4527 | -49.044 | 2025-09-13 11:40:00 | GOES-19 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 3906846b-dd3a-3e78-bcc9-cf0236aca2e5 | -16.433 | -49.0474 | 2025-09-13 11:40:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b078fff6-3876-3d5a-a1b8-3666c8a1f435 | -11.8475 | -50.5384 | 2025-09-13 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 0dcc6130-bcd5-3ad2-bf47-b8e4c67600fd | -14.2078 | -46.3129 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 123.2 |
| b05c51f1-ef82-3c44-841f-df385a803e8f | -14.1694 | -46.2965 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 321779b6-eb89-3777-ba08-8e20198dc598 | -14.2083 | -46.2899 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 71facd06-0c4e-3aa3-8744-651802972d45 | -8.9595 | -44.4436 | 2025-09-13 11:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5f7a5c46-4591-3be1-9555-e54ef061bb59 | -12.8456 | -47.9236 | 2025-09-13 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| e3ade7b3-72bd-380f-8a8f-9cf9e48d69e6 | -15.8213 | -52.2015 | 2025-09-13 11:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e039b29d-a34e-3021-92ba-93178551a9db | -10.8972 | -45.58 | 2025-09-13 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ce64387b-fdca-35d0-b05b-2961f8c91e19 | -15.4713 | -47.3256 | 2025-09-13 11:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a6f7928a-ab95-3a15-96f6-d02715ec767b | -11.8094 | -50.5428 | 2025-09-13 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| fd812490-8b00-30aa-bfc3-17f254f36132 | -12.8452 | -47.9459 | 2025-09-13 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 709727f9-c368-36b8-9378-7387c45446e8 | -12.8259 | -47.9486 | 2025-09-13 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 2e5e97ea-69c7-36ed-ba42-a360330a245d | -9.2658 | -59.3997 | 2025-09-13 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 655e65f4-371c-3e75-9399-5882f15fddcf | -15.4517 | -47.3291 | 2025-09-13 11:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| dee82f46-d074-3385-ba27-6ddff38663c5 | -14.1893 | -46.2702 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 453ca741-416e-3991-9848-7ab0b2529750 | -14.2277 | -46.2866 | 2025-09-13 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c70fa3c3-6d09-3353-bfba-9bbd576959c4 | -12.8263 | -47.9263 | 2025-09-13 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3a5aa209-7bd4-3e92-86b0-2a7a56783306 | -17.63688 | -44.08218 | 2025-09-13 11:40:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 814b68b5-2b3c-3aee-9683-2da7074a643d | -18.00469 | -46.94929 | 2025-09-13 11:40:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6518a2c4-93a4-3c4e-9229-7aecd681b859 | -19.76616 | -43.02298 | 2025-09-13 11:40:00 | TERRA_M-M | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 18b349f6-7425-3779-a1b9-82642ffd13ad | -19.36043 | -44.80484 | 2025-09-13 11:40:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fd9f7180-c96c-304a-b705-ec740c973033 | -18.51647 | -41.41449 | 2025-09-13 11:40:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b3fb7fd7-11eb-3c1f-8509-26f190b0f86b | -19.3325 | -45.10364 | 2025-09-13 11:40:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d013ced9-d3a2-36b2-b6ab-2e4b1c02e4cd | -17.15623 | -47.27845 | 2025-09-13 11:40:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 898f2f2e-011f-364a-91a3-3275e65eb291 | -19.63947 | -45.07306 | 2025-09-13 11:40:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e9341931-e354-301c-b772-1ad0003e7c36 | -20.47532 | -44.57681 | 2025-09-13 11:40:00 | TERRA_M-M | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 7f7c0e84-21e6-379e-a1e9-0b2f9e5683f1 | -20.26224 | -44.19558 | 2025-09-13 11:40:00 | TERRA_M-M | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| fe9868ba-5d16-3b15-a358-c142d7bbb52a | -20.47353 | -44.58652 | 2025-09-13 11:40:00 | TERRA_M-M | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 288226be-455d-33d2-a8cc-301f305bb76f | -18.00547 | -46.91833 | 2025-09-13 11:40:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c2092955-63db-3654-a953-aa1a00bcda43 | -18.00097 | -46.9429 | 2025-09-13 11:40:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d2cd0aa0-8b47-3d56-b59a-5a6cb6dbc13e | -20.39047 | -45.53656 | 2025-09-13 11:40:00 | TERRA_M-M | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 708e9005-70b4-3e37-80c1-5b64780b85a7 | -18.00938 | -46.92463 | 2025-09-13 11:40:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 157e2461-212b-3d7b-aade-8cd6d45e0bee | -19.64526 | -45.08032 | 2025-09-13 11:40:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 48900d6f-56d8-3cc6-b6f8-7f0d3d1aa801 | -20.26569 | -44.1877 | 2025-09-13 11:40:00 | TERRA_M-M | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| e7bac5e8-3123-38fe-839d-12ba89ee7bc3 | -19.63637 | -45.09098 | 2025-09-13 11:40:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 78d9562c-5b1d-33b6-8ec3-1f7e5ab70323 | -19.98692 | -45.13013 | 2025-09-13 11:40:00 | TERRA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4e9c2354-728a-3fb9-9fbe-caea37ef700b | -19.32939 | -45.12143 | 2025-09-13 11:40:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 06b2ad00-a2ca-3ada-8c04-ab49d84b1515 | -20.1164 | -46.9104 | 2025-09-13 11:40:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 78d9c17c-906b-3b3d-89be-eadf03c7f420 | -21.37534 | -51.16871 | 2025-09-13 11:42:00 | TERRA_M-M | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.2 |
| c3d0135d-c6eb-3fd3-9065-bd04b229c169 | -21.3762 | -51.16326 | 2025-09-13 11:42:00 | TERRA_M-M | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.3 |
| 3e8993bc-aa6d-3cbb-88cd-e6da0614914f | -7.4511 | -44.4177 | 2025-09-13 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |


[Clique aqui para ver as próximas entradas](README122.md)
