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
| 23e125f6-8ff6-3715-b16d-b5f257e444d5 | -3.8197 | -41.56395 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c2c9eb1-8b30-377c-a212-00891e0cc64b | -8.66677 | -36.23185 | 2025-08-23 03:38:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 50263855-2856-380e-b225-8af3a78d488a | -6.60992 | -44.57232 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4423d872-d156-3980-bd56-041461d4dbcb | -4.34861 | -46.47034 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2c8734d1-8af8-35a0-88f0-d90192974098 | -4.33848 | -46.4706 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb653787-82b5-36c0-885f-3ead8761ef55 | -6.48335 | -43.46262 | 2025-08-23 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e188833-f264-36e1-a80f-bdeb8686b15c | -8.29728 | -47.26767 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bb4bcae-6240-3064-9c3c-d43afc3209d5 | -9.2789 | -40.54537 | 2025-08-23 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca6cc842-04d1-32ac-b74a-8dbdc66ebadf | -6.42731 | -41.2262 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0d89ca71-a7be-3814-845b-6c8c10157656 | -3.81863 | -41.57022 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f6c52a6-7207-3c5d-9757-e6840de260a5 | -6.42432 | -41.21436 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| beb156bd-1e75-3bd9-bd7e-282be3d20249 | -6.42682 | -41.21666 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 776570ec-49fd-36da-9f9c-de26534e3168 | -8.29794 | -47.26097 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bef8a4c0-ce45-384b-9dbc-f93e1bcec47c | -4.34551 | -46.4717 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5b72553f-fe55-3d18-94c3-52e6c2d66e50 | -7.4289 | -45.41828 | 2025-08-23 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58e1f169-b71f-3830-9cba-64f982c23576 | -4.14556 | -46.4622 | 2025-08-23 03:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774e80c5-a540-3a66-9b92-7f2c79e80e11 | -6.60392 | -44.57096 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f134b1d5-b100-34f0-b4de-1eeaac27a6f1 | -7.65007 | -45.24361 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f1179aa-2249-3ee3-afad-06918822eb34 | -7.61189 | -44.37307 | 2025-08-23 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b507f538-0948-3ef4-8af6-3537a59afb04 | -6.60458 | -44.5701 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9ca46afc-d969-3dc9-80c0-6190a222719d | -6.40731 | -45.48912 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8522dea4-8e24-3ee1-99db-a5344d9cb8e8 | -9.44205 | -47.66218 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56dca094-766e-3ab0-bd46-efcd0ef32e71 | -9.33056 | -37.98124 | 2025-08-23 03:38:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7b2174d0-548d-375e-911e-f0ef00d259ad | -6.40801 | -45.48687 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 468a5f8a-1784-391f-a83c-b4fd90d141e1 | -7.02602 | -44.64078 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2953cee1-c969-3cad-bb1f-7323793837ff | -7.07943 | -44.06519 | 2025-08-23 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08e0f612-e24c-3578-9416-4cd925e186f8 | -4.33962 | -46.46433 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07ce0c3f-d329-38f6-aee3-0b3f9390b195 | -6.42195 | -45.48139 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0956f7e-058c-3c19-9bf2-936ead3b7a26 | -6.60538 | -44.56575 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 167edf4e-09dc-3607-9a27-8eca7941f3ef | -6.5971 | -44.57423 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 55aa7543-b343-3c61-83b7-c1b288bf970a | -4.34041 | -46.47593 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8945621e-1c28-39fc-ac6e-0a4e729fbdb0 | -6.11222 | -44.40771 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5cdf35-5e7a-3513-9b95-43744ecfbb4d | -7.64386 | -45.24255 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc16015d-437d-386b-a8c3-9e60dbc269fb | -6.61153 | -44.56322 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bed8e07a-6c1c-3f5d-a3a1-5a85df3c1e59 | -4.17866 | -40.71875 | 2025-08-23 03:38:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8c36e2bb-3bf2-3097-8ac6-097a7dc1d09f | -6.37245 | -42.67256 | 2025-08-23 03:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b233d37b-ba16-3192-8f57-ce9a8eef691c | -9.44894 | -47.66376 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c74c253-843b-3149-b247-bcfb5dfdd658 | -6.4227 | -45.47922 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f84f1c1a-cce3-324a-8e5e-af68893504f6 | -6.61059 | -44.57133 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 399319a2-fe5d-3bc3-b78c-3505ffb40e45 | -6.71248 | -43.21332 | 2025-08-23 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 39f335bb-72b9-3e2b-be6c-5fc29d7c7fd8 | -3.82023 | -41.56084 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63c9ce3c-186a-3bb2-9f99-2ba8de7e8c5f | -8.30414 | -47.26919 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0506991-477b-3cdf-a42d-a308a01eb9d2 | -6.18331 | -45.43927 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| eb1aca1c-8c19-346f-b6ba-faf5a584b3dd | -6.93444 | -39.56152 | 2025-08-23 03:38:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cb40943-1e2b-3877-9d64-0b26c7a1ea3c | -5.90619 | -43.46786 | 2025-08-23 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 628877ab-371d-39d3-b2b9-c20d31cdeaaf | -3.81556 | -41.55685 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 393d33b0-c94a-32d5-a542-f78edb216646 | -6.70632 | -43.21591 | 2025-08-23 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 645556d9-bff5-3eba-8822-c0f6d020734f | -6.42198 | -41.21573 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 10b7d213-948e-36ed-a5bf-8e25d6e60be5 | -6.59772 | -44.57341 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0935c9e6-0083-3a22-af40-97b2c5c79c8e | -3.81755 | -41.57654 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4d520b7-997e-3b9f-80c4-2d8570075445 | -5.83336 | -45.16947 | 2025-08-23 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42cabf4b-b45f-39de-afc5-7ca3c69fa252 | -6.93258 | -39.56124 | 2025-08-23 03:38:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77f3d2f6-5996-3351-9bc1-95c582c06374 | -5.89052 | -43.45677 | 2025-08-23 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e82e32cc-2904-3459-932d-dd7949be5aef | -6.93189 | -39.56539 | 2025-08-23 03:38:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3922e2c3-3b0f-3dc6-8d85-85dbc9789cee | -7.02519 | -44.64528 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cd2012e0-5854-3ac5-9513-ad7a42932254 | -6.41561 | -45.47982 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd7b6d2d-d973-38a7-b990-68c92b6e8da7 | -7.63353 | -45.23804 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e94a239d-1b0e-380f-8cfe-4c0c4ab7141f | -8.66246 | -36.89901 | 2025-08-23 03:38:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b235ee81-b325-38b2-a68c-a40d9bf309f2 | -9.31379 | -40.22292 | 2025-08-23 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf5cfd86-cdfe-321e-8e88-adbbf1000b8b | -7.02956 | -44.65532 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ac529676-abae-3068-81d9-5ccd2b0e149a | -6.42585 | -41.22209 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d6e7941f-4437-3793-905c-ac6e9b0463b2 | -4.34664 | -46.46546 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5ac3b539-99c7-3827-9307-7e60fc01b7e0 | -7.63972 | -45.23918 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03656bed-b47c-34d9-9c8d-7e50c99e297b | -7.49373 | -34.90979 | 2025-08-23 03:38:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 0a070c83-d63b-3847-a59e-a1836989c698 | -7.63767 | -45.24142 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96310c7c-cc40-3043-93ee-de40f6026697 | -6.6031 | -44.57561 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 21e63cb1-8b66-3a9d-809c-bc67275cde14 | -5.49066 | -42.15444 | 2025-08-23 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7b416fc-ea67-3f50-ae46-fc2745db52cf | -8.30347 | -47.26914 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b5b06f-9482-3d4c-9fe9-0628fa61daec | -7.63244 | -45.23526 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93765602-ce36-3490-a840-348ad3fb7ddc | -6.61143 | -44.56678 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c7dc10a8-c990-3daf-9a95-35e8592c2ea1 | -10.22124 | -47.56566 | 2025-08-23 03:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ee1f066-6845-31d4-8976-fb59f5f2dc4c | -6.58429 | -44.57606 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8ec876e-b4c0-371e-8edc-2a9d364904a7 | -7.63443 | -45.23312 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84e504da-fe70-343c-81d1-237fcfcc63d0 | -6.1114 | -44.41219 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2aaff64-0e40-3a46-ace7-2c6831d705e1 | -8.0143 | -45.49068 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 175c692f-cbc2-3eec-aca4-2578c50cef19 | -7.03119 | -44.64653 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 91d1942e-ea3c-330d-9edb-473ae0d0e34d | -7.03037 | -44.65092 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5b3e6c46-9b74-3b05-9abb-b01db3aa26ea | -3.81916 | -41.56708 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 154e78c4-6390-3918-9cce-09d3854e80ee | -6.95065 | -37.39336 | 2025-08-23 03:38:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ffa8ac72-2612-33d4-9f04-2f1569f46686 | -10.21993 | -47.57211 | 2025-08-23 03:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a482e3a1-be83-32b3-9b5f-e95b74ca931a | -6.59789 | -44.56981 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc4317d9-b6b4-3d2b-8a33-b6628657c0dd | -4.14666 | -46.45588 | 2025-08-23 03:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1b53e5-be52-3a35-b408-78b3598caf87 | -6.37186 | -42.67596 | 2025-08-23 03:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48c00787-e31a-3bc7-9bce-8c0ca1a73eb1 | -7.43519 | -45.41942 | 2025-08-23 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52939e41-9137-3164-b2ff-1ba9f8b18f0b | -7.03201 | -44.64209 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fc688fb2-1174-382e-8b35-43a40e112da3 | -7.63148 | -45.24027 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 07453be6-e786-3079-9689-e33b59f286fd | -9.83087 | -46.37852 | 2025-08-23 03:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fca01276-e1c2-3efb-b1be-ca80fe994fac | -5.71957 | -38.30704 | 2025-08-23 03:38:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a63155b-e799-3554-a9d9-1b2f9a826a19 | -7.63049 | -45.24544 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22cb7011-150e-39ee-a53d-65c4b764a802 | -5.72015 | -38.30355 | 2025-08-23 03:38:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e903aff-5038-34af-9b29-45c72f696478 | -6.58574 | -44.57067 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 234e2eaa-b816-3659-9dd7-88226ec3032d | -6.61074 | -44.56765 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e132f38a-8dc2-31c7-b3e8-c2231b37bf0b | -7.13801 | -44.16567 | 2025-08-23 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9bff3e8-9e8f-38d5-b8cf-44cf657f201c | -4.97632 | -38.60131 | 2025-08-23 03:38:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 76b6dddb-7fc4-3c69-98dd-12d130f4b237 | -6.41538 | -45.48292 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 809b1565-57f4-3718-ac97-4107fa72343a | -4.98047 | -38.60207 | 2025-08-23 03:38:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a06878f4-10ca-3523-af46-d02733038730 | -7.63258 | -45.2432 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64a4d157-ac89-3cd6-9302-8e8dc9efbb75 | -6.60372 | -44.57474 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b94b0a0f-58c0-364f-8eda-9cbbf5fd0c6f | -7.02508 | -44.6412 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8714d771-7fb4-3964-b9da-b2c97713324f | -4.34741 | -46.47726 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README15.md)
