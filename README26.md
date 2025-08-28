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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c74d4d5b-9eba-3c55-806a-7d7c3adf282c | -21.13923 | -45.89935 | 2025-08-28 03:47:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3192739-ef1b-310c-a40a-7a68f3d58643 | -14.13643 | -45.41074 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ecc1eb8-c9af-380b-8506-7b2962f009b9 | -11.6527 | -44.87114 | 2025-08-28 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2d674a5-406c-340d-a6b6-f6b95ac8a10c | -20.11547 | -44.34549 | 2025-08-28 03:47:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c10cd335-5fb9-3769-b9d6-11be5e8b4882 | -12.77627 | -48.16798 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69cab207-abcb-3414-9ef4-df457fc6a173 | -12.80085 | -48.16479 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2994e5a-491e-3376-8607-768c93d24796 | -14.23306 | -48.03822 | 2025-08-28 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d13ce2-d453-37d2-ab73-7d182babf012 | -12.80197 | -48.15936 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 544f9fe4-cbd4-33db-9f02-a047f27fb112 | -10.80639 | -46.36679 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06b318ed-b976-38b0-9051-c25fa5394e0b | -12.81756 | -48.11462 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7eef480d-816b-3807-8794-58de4a74e37e | -13.99279 | -46.34274 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f12a9154-1368-3a7f-b58f-fce58ba5abf1 | -13.4559 | -46.85204 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fda3d198-110b-380b-876a-d21343b0156c | -11.2505 | -44.97163 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14582d82-765a-383a-89af-5b7a0a59f919 | -12.67923 | -48.17263 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa2b6299-3ee5-3f58-8fbf-10c0e7f9fd09 | -12.80809 | -48.12965 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7efab2ae-9461-3100-8940-f96664a8f573 | -13.98792 | -46.33913 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d452520-36d4-3002-8862-1688d555a978 | -11.57321 | -46.41863 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 897645cb-d459-3d6c-b624-a4b3faf8377a | -13.66784 | -46.88503 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d173253-3085-3847-8343-697b5395d279 | -13.66713 | -46.88851 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7519956-8f12-3926-9327-4ec488f778ec | -13.46446 | -46.85214 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ac3e4e0-3696-3aee-9ce6-6d31099ffc6b | -20.52661 | -43.96482 | 2025-08-28 03:47:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9c2118c-f30e-37d0-b941-2aeef0d9f7a3 | -12.4039 | -47.78811 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e2b2ff5-b0eb-39b3-8a45-37e6aaa2fcc7 | -12.43725 | -45.96427 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f7d71df-d6df-38d8-a67d-65d4ce097a33 | -13.1874 | -45.28774 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bc05e95-42c3-3ea8-a8cc-88203657ae31 | -13.54973 | -46.90759 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92b75671-2c37-3066-979b-b1ac0ed782e7 | -21.02423 | -46.23175 | 2025-08-28 03:47:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a3107750-daf0-38eb-a8af-079cd920565e | -16.88515 | -44.61154 | 2025-08-28 03:47:00 | NPP-375D | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da58e108-83e1-3ffb-ba97-e455958b7da5 | -13.63308 | -48.24087 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49f9eec2-acd2-3d07-a5ac-470541e3cb4e | -12.9578 | -44.58043 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a2b3b970-efca-33f4-8e50-a90a7242ed2b | -10.53728 | -46.70879 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d8b119-2d37-36d3-9d67-a2889c588451 | -12.79463 | -48.16394 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2292b2a9-e519-38a7-95af-7c3512ed797f | -12.79321 | -48.14718 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 815ddbea-b312-3799-9810-a49f18c7edd0 | -14.13759 | -45.40477 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9a2d2e8-7fea-3da7-b491-24a1c7f211db | -16.54178 | -42.34655 | 2025-08-28 03:47:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a254760-e94d-3b52-b149-872bc048fbdd | -12.67892 | -48.18051 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65d2299e-9106-3c98-be13-650b342ae2d7 | -13.60366 | -48.23009 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbcbe16d-a713-3510-a8f4-e37df3b696c3 | -13.66827 | -46.91139 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d155c9b-b843-3849-a0bb-a4da5b1cbc57 | -13.41412 | -46.85709 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8e937b78-7f06-3fcf-9aeb-8fd7592056eb | -12.80501 | -48.14458 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d77b2de0-ff5c-3e5c-afac-36a4ef11fa7f | -14.2417 | -44.11787 | 2025-08-28 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8095b76a-30b8-3471-bcef-04fd303c58d1 | -12.40342 | -47.78897 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fd14bf2-1fd8-3b07-930b-61492c2e3c09 | -11.83283 | -46.80372 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cb5ba1d-4384-303b-9d31-a42ac02bae74 | -13.62239 | -48.23318 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70327bad-c259-3170-88f6-3ec1f56925f6 | -13.08183 | -46.32944 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f3176ec-f482-3bbb-90f9-4bcea6f018ff | -12.96158 | -44.5871 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3314596b-e9b3-30cd-a903-e62456adee68 | -12.8957 | -48.10417 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b8363e2-3985-3f0d-ac7d-60ae1fad5168 | -13.47085 | -46.99353 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 655133ac-70df-3583-a595-efbc4d70860d | -12.18215 | -47.18455 | 2025-08-28 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c89b67e-9180-3d5d-9975-9a5a20257182 | -16.15527 | -40.34887 | 2025-08-28 03:47:00 | NPP-375D | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67d3248e-1794-348e-a1a0-15ab915c8cb8 | -12.77457 | -48.16804 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15ebeb3c-aad3-3e85-bdeb-795f44e9eb95 | -19.27746 | -49.71301 | 2025-08-28 03:47:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b53229aa-bcd4-3ed0-9cea-5e20a8d23f81 | -21.89511 | -43.31313 | 2025-08-28 03:47:00 | NPP-375D | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 92206abc-2d6e-33a1-8762-e9cdd93db4db | -13.43682 | -46.97852 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72bcdf55-7e46-330a-bc3b-62e6fcdf280e | -12.89063 | -48.09793 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ab05f75-1aca-3829-94a7-3e7b71c04e77 | -12.9599 | -44.56946 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1fe8ec8c-ec25-3a16-918a-a5b1f7e6c9a2 | -11.33889 | -43.54374 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eb949d92-2d96-3e9b-ad17-62004f82b404 | -13.42814 | -46.9724 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b7abf11-b270-363b-a1d5-7aa8c7b4c8ee | -12.71832 | -48.16962 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 999daafc-6239-34ee-8edf-903aca5678fa | -12.891 | -48.09788 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5340afea-3aa9-30f0-afe2-422ac1753d44 | -13.52215 | -46.8839 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a06fe8fc-01d8-34f4-8475-31b8a4d65306 | -12.7896 | -48.18829 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00e079c4-9449-3f44-99cd-180b0fd1289c | -13.44557 | -46.96378 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1255347d-ab0f-3783-9879-ba5a15f37cd7 | -13.98974 | -46.3386 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 640c4042-92fb-35f8-b680-a7de763374f0 | -13.53541 | -46.93459 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b617d31c-9418-3940-89ea-31357da8df28 | -13.99212 | -46.34617 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91dd845a-8dab-371f-9e8b-b4a00250869d | -12.68452 | -48.1781 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c0cad66-a457-3d90-a51f-f015c4e203d0 | -13.83439 | -46.68401 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4029867-bc3c-3203-bcf5-58dc9d4f496e | -12.92762 | -46.33249 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ef87c0-2c5f-3b19-8ceb-d098ce158f62 | -11.25037 | -45.47985 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4716555c-0540-32d2-afa1-16a310393703 | -20.14686 | -47.37324 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b9accdd-60d4-37cf-abf4-4af30c95759c | -12.92844 | -46.32996 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a114ae2a-4b6a-38bc-b522-66b3a0e178bf | -12.69906 | -48.16977 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ce87406-02a3-3860-96ea-525a1803ed2b | -12.68638 | -45.08518 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cba9f057-d13b-319b-922c-1edd94b6223a | -10.53549 | -46.68675 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bdb6883-5325-3013-9966-178e49a0a916 | -10.81279 | -46.36426 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e608e76b-a495-37f3-aa15-8ca5996930ba | -13.63145 | -48.21967 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b18f32e-b561-3bf4-aeda-138f8525019d | -21.20337 | -45.41032 | 2025-08-28 03:47:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8eb813bf-0cef-3556-b2e2-7dabafdd425b | -13.17665 | -45.28873 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fda6a454-3edf-3d31-aaaf-a6007298ffc8 | -13.63267 | -48.24497 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d5e55a0-6133-3306-bcc2-f40145c1676c | -12.43657 | -45.9678 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c18c0913-ef4d-3fd5-b5f0-58873dae380d | -12.7912 | -48.15726 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f95f93a-9a8c-30f2-b2d2-79f3adeeb43b | -20.14026 | -47.37926 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5dcc18e-deee-3c06-813b-4ff950821e69 | -13.53051 | -46.92981 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b0d1ee1-29bf-3d95-8e15-5b5c9e36c63b | -13.5526 | -46.90676 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb943263-cd99-31b8-a091-098b408b8370 | -13.17334 | -45.27855 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae2bb65f-b471-3953-8b25-7a8cf83be4a7 | -13.18114 | -45.29282 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd86d9f3-aab6-37e6-a8bd-f034e6c4f6ce | -12.8687 | -48.11143 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ddd0d70-a904-3336-83f9-ab1f959b9555 | -11.80507 | -46.79312 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8447e86-3421-3fb4-b3e8-9e91e0ff030f | -12.95496 | -46.33792 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ec472ac-22c6-3be1-badf-9c905df65a43 | -21.21895 | -44.98923 | 2025-08-28 03:47:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0bd9e06-eb99-3c45-b340-06b0f3e7abd2 | -15.08228 | -48.51974 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 640fcfac-30d2-30ab-9c11-dd1c9417823a | -13.43477 | -46.96871 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc6afa03-a9bc-3e92-9034-0d504c287df8 | -13.62041 | -48.24084 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4075cc5-4186-35a7-abee-3804ee80ffb6 | -13.41486 | -46.85344 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4d46150b-d256-3efc-b501-08e207f82bf0 | -12.41613 | -46.48349 | 2025-08-28 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa141ea8-257e-345b-822e-dcb2d97869d9 | -12.74156 | -48.18138 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e9c4c2b-7adb-3688-a744-cb7978ea4a3c | -14.14203 | -45.40886 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b760fa0b-523b-3e41-8036-fed9e137f3f2 | -12.78132 | -48.17471 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c9030f4-c5f5-33a0-97e2-85295aec2986 | -11.55851 | -46.34425 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a1a11bc-ad80-3601-a8c3-8737ba44bc37 | -11.57347 | -46.38715 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
