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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c310006e-a771-3085-8fb6-9bd352ee2544 | -15.8832 | -42.71739 | 2025-09-16 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86b219e0-521c-3f3c-a3d4-b1b1814c6eb7 | -12.70324 | -47.74774 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ebdc1c-0939-3414-8bd6-8f7e1eb9760f | -15.81209 | -53.46404 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57800796-a943-3253-b8e4-2602fa32dee4 | -15.81875 | -53.47216 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66317d97-5c73-3373-a461-acc1b0bc0ed9 | -12.97668 | -47.95822 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cec5ade8-f8ef-3d93-9cda-fab0b7b205b4 | -19.58896 | -44.06419 | 2025-09-16 04:04:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b54d0724-4ac7-37f0-9f8f-8020255e4e1f | -12.66102 | -47.72309 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9fc64c39-af69-3f03-82f8-2dede540a756 | -18.50365 | -43.99416 | 2025-09-16 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7116a7a1-a0c7-37e8-8abb-a3f024336030 | -12.69892 | -47.74698 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8017df1-5eda-3571-8832-ebcb47f00272 | -15.40158 | -41.70881 | 2025-09-16 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 43f9d29c-f48b-3a10-91d2-91147535e99b | -12.69039 | -47.93919 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 401ea877-96c5-30c1-ad96-8f143219d3bd | -12.81085 | -47.23168 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e8f39a4-d22c-33b7-92b6-4ebee307a4df | -13.03452 | -47.99167 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8d3166d-54d4-31e9-b7bc-730572f959d1 | -14.66316 | -46.84135 | 2025-09-16 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcf22e7f-92cc-3488-9551-9492d06d41a2 | -12.65 | -47.9595 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73d90e09-e928-30f0-bc86-935878a78af9 | -13.20638 | -47.27869 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b92e6c-023b-3139-8850-95a47e8aaf59 | -12.67501 | -47.94593 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9689854c-da6c-36f1-806e-58afc239323f | -15.7882 | -53.44195 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 335ef15b-b68f-3a39-9923-eae14ed720ac | -14.53231 | -47.38319 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ba42adf-48cb-322d-9e12-38d5d14c4a9d | -12.73348 | -47.19858 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc8c78b4-69a9-375e-9e1d-1b2d63567e8d | -12.79335 | -47.2569 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a00f6cc9-7c7b-3f40-b5e0-22ec91ab19a1 | -16.43154 | -45.67861 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8811fc0f-9e53-31b1-8f34-c5f232355851 | -12.80407 | -47.18737 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94205ecd-d9ed-324d-ab17-f958128bee04 | -13.0221 | -47.96124 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfe1e45f-8a9f-3992-b796-bfd63a1d30e4 | -13.74765 | -48.77194 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c01c1a39-a5a5-3be6-8fd9-48c8822eff93 | -14.61691 | -46.37444 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9ae3056-a9d6-34bd-9542-d08c77d01adc | -12.53998 | -45.87178 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d19e9de9-f239-3192-8920-64e43911fa74 | -11.91279 | -48.56007 | 2025-09-16 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 57764124-6d99-33e5-8580-1148d7ed2c45 | -15.8278 | -53.47681 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29ce62f7-7ce9-3b5e-b225-576d8b738ac9 | -17.07724 | -45.82473 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd1144c6-f733-3e4f-b1a8-9a290b972f62 | -12.67213 | -47.94029 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 352406c4-eff9-34b1-ac54-582a24fbb30d | -12.28884 | -46.40466 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e7d5e364-b610-3742-a671-e7e9774dd28f | -15.24035 | -44.03347 | 2025-09-16 04:04:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da70702b-cec9-381a-bc06-0492b1535fb7 | -12.29345 | -46.40182 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84636234-aa58-3923-8774-2f804458e94e | -14.52077 | -47.37715 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2be1226c-e72b-3bdd-8785-e680342ad053 | -17.08222 | -45.83084 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a356d2c1-5840-324a-bd14-c958124e18b8 | -13.19292 | -47.30635 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0b0f5f6-264b-30de-9414-b0d674aa39ad | -13.20965 | -47.30872 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8770e192-acb6-3a2d-87d0-36276ca5deba | -17.08083 | -45.82542 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f62e7d4-3a43-3359-bdee-fef8bad769b6 | -12.62805 | -47.52091 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0c18c1f-fa18-3156-b42d-902891d7c5cf | -15.41584 | -47.34781 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d0a51ae-1645-3d76-9a48-2c12367c603b | -12.66882 | -48.00712 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a48d8d11-80b8-33c2-87e5-ecbf4e1f2725 | -14.51797 | -47.36937 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75a88f5a-8197-3c99-9a45-6bdefd91b3e0 | -17.73581 | -46.76603 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe4b3bbc-52e5-3b25-b5bc-6beb7a01e1f8 | -13.18598 | -47.2971 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f34aa38-b183-398f-a122-635dbb9f7f5d | -12.96204 | -47.96464 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 89215c65-bca2-37f1-8ad2-66ad6bf5004b | -14.52245 | -47.34493 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78fc1238-c849-38f3-b7d6-6661ec9ce3b0 | -15.15865 | -52.46013 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 865b634b-11df-38b4-bfb9-e7f7ac97d374 | -12.83506 | -47.21649 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e83b3ef-5d59-372c-9748-29231d7a4a0f | -14.28246 | -45.99454 | 2025-09-16 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07c09321-3f92-3886-a734-00b284a135b7 | -13.21598 | -41.98062 | 2025-09-16 04:04:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9b794d6d-10ec-3dd3-9ce8-106012078254 | -16.68787 | -49.78075 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2000a07d-be21-3756-91cb-ff1a1635e8a8 | -12.75566 | -47.19455 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9215014e-91bb-383e-8a20-5b23c03865ec | -14.52274 | -47.38938 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669ca80e-6d83-3871-b2fa-4b83f88a4757 | -18.97398 | -45.5646 | 2025-09-16 04:04:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e588c7f-d9fc-3f6e-af70-7080f277bf46 | -14.97579 | -46.55512 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a189f042-ec23-3f94-907d-a9923486de17 | -18.77627 | -47.63645 | 2025-09-16 04:04:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee02f2b5-d8f5-3aa3-ac9a-61c11e4753ba | -14.51867 | -47.38856 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69433ef9-c645-3920-92a4-342e214b4f71 | -19.87166 | -46.74078 | 2025-09-16 04:04:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f48d9e3c-2372-3fe4-aed1-d6dc047c5cd4 | -13.51557 | -44.30339 | 2025-09-16 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5d25c0f-3788-32a6-8693-8464b409dafc | -14.91249 | -51.64569 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2a3051b3-5e9c-37d1-a64e-004ae837d5eb | -13.94065 | -44.78344 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d22f8e07-d811-356c-bf57-01ac2c655cb4 | -14.30137 | -49.5313 | 2025-09-16 04:04:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a41c0bd-6d6e-3bf6-b50b-389a3eef5046 | -12.69236 | -48.00241 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6a853767-67d1-3556-ab1f-8c93921c7920 | -12.95832 | -47.96033 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f0a3a02a-09b7-3e6e-a2a3-b379e7717a2c | -12.76974 | -47.97478 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67b5aa9b-3dcc-384e-a523-c781c15700d3 | -12.75012 | -47.20154 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6277f78f-8a47-3354-9a8c-08622e63935f | -14.54021 | -47.36293 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ed9c9b2-02eb-345a-b78a-b16b74086690 | -16.59151 | -42.90804 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f56e4e6-ad30-372c-98d1-3a36e5ee1d1a | -15.78742 | -47.72471 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b642f80-dabe-35e4-b158-a57d7552146c | -15.61359 | -47.36937 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c57e906-fde2-3825-bef9-514adba1ae0b | -12.75739 | -47.96811 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 847343eb-98e5-38ee-89ac-96e62dc47621 | -16.69683 | -49.78367 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f93ebd8-f79b-31d9-b1f8-9c4fc8bc6516 | -12.67063 | -47.94514 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2f70d80-62c5-35d3-9ccc-4296095d8424 | -12.8191 | -47.23355 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c6fa3a9-6551-3786-a148-3b7a1edb0f07 | -17.7275 | -46.76927 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12e25826-f30d-3221-b978-21f825ca7dfc | -20.01827 | -43.78782 | 2025-09-16 04:04:00 | NOAA-21 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5a812e32-4fb7-33f0-855d-deddd48e24c5 | -15.72293 | -39.32368 | 2025-09-16 04:04:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c8f5e341-5d60-37b3-be4c-b44ffe3558f0 | -14.27646 | -46.14197 | 2025-09-16 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e4fedb3-244d-37ff-87de-3b30fb32e3f2 | -17.59664 | -46.67417 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 383a5148-5f36-3481-8bde-4c8a8b3c6095 | -12.79662 | -44.74149 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74d65b1f-3c84-3074-aa52-85633df89b64 | -12.82951 | -47.2235 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67f44dce-658b-35f1-a76e-1946da9b6e7c | -12.80384 | -47.24658 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6827f34-35ab-3d4d-aa49-59919041b650 | -15.82871 | -53.47259 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32ddbc70-6d2b-3759-9004-40165c10b7e7 | -12.62645 | -45.7579 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ceb606d5-4102-35b5-b1be-60c49beeda22 | -12.79493 | -44.76152 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eece8f93-9347-36bc-9837-b934b5ab4158 | -12.85667 | -47.14381 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 655f3024-7444-3da3-8759-712a34026c64 | -17.3049 | -40.68626 | 2025-09-16 04:04:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd98768f-63d8-3fdf-a800-04967e37a7bb | -13.21117 | -47.3001 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fa0126b1-333a-34ab-b05d-a6f1091fd27b | -17.22528 | -43.43626 | 2025-09-16 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6763152-77a0-3fa5-aeeb-2b8230b43bd8 | -12.69971 | -47.74274 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2777834d-4c7c-37cb-a1f0-c29e0479157d | -14.92356 | -51.67352 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e7add48-d9e9-3182-b94b-941e76fc75c2 | -12.29132 | -46.40048 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68465601-2e4e-30c2-92cb-cf6190891428 | -12.73626 | -47.20705 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa0abe0a-a41b-337b-9104-1443eb32326b | -12.76172 | -47.96914 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b6204e6d-4964-30d2-a885-2f078c3247ce | -17.22859 | -43.43686 | 2025-09-16 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e21857f0-5541-3af5-ad39-2e12a9dea16b | -12.66684 | -47.71545 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cdd61c0-c08d-3b73-a461-1cca183ba75e | -14.52345 | -47.38548 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e48c7a6f-fde9-3987-996b-ad0ddf0379bd | -16.35453 | -46.84363 | 2025-09-16 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05479eb-ae96-36b8-ba25-1df59b0573fc | -13.21531 | -47.30091 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README22.md)
