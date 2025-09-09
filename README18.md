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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27f876f5-36d3-3ba1-9fc7-4800ac258451 | -12.8592 | -47.97643 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b2eaa5f-94c2-3291-83f6-81fc6a41f4f7 | -13.29061 | -43.73585 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e456b50-abf1-3ff3-906b-786e12519d53 | -13.46087 | -40.55438 | 2025-09-09 03:45:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dfa165c4-9c8b-3e4f-b861-de8107fc270e | -17.57385 | -44.54588 | 2025-09-09 03:45:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 998e6544-b213-3681-a4f5-f845b7a6950c | -14.33672 | -47.33041 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4318e4-1702-33ed-9511-61ab19d4721a | -13.79158 | -46.27418 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47156ba0-f19d-3d5a-a7d9-32e92573b88c | -14.2805 | -45.02292 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e274553-9397-314b-952c-a7ba57ddde58 | -18.6655 | -47.54745 | 2025-09-09 03:45:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52f5d8fd-cc3d-35dc-b288-3a74d83a4813 | -16.44049 | -41.97948 | 2025-09-09 03:45:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 929b9e24-2b46-3887-bc31-f5317ea12764 | -17.25973 | -46.68504 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbde8f71-c65a-336a-8214-399806c19010 | -14.76605 | -47.78315 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d97d8645-3e68-3ca3-8322-3f0d2a83d475 | -11.83616 | -46.75899 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe289627-6c0d-3ec2-8dfe-9aa5c220f86d | -13.65143 | -46.97066 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6adf57d-bc3f-3403-b7cc-0ef46990fada | -11.84271 | -46.77373 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a98d9ae2-afe8-36ce-89f6-5e2ae1ddd861 | -13.27533 | -43.7426 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9a8fe9-3390-3c9d-8c9f-85ce3e3a3489 | -11.30265 | -46.50094 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ba6e021-1044-3682-b593-5f74c6b1e169 | -13.64967 | -46.97937 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428cd30e-5b4e-31be-8fd2-8dc84953aace | -15.11355 | -48.05433 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d893498-4130-3f55-bba7-d61775d88a45 | -14.32801 | -47.31599 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e0de63e-b630-3472-9d98-70ea275525a3 | -17.26746 | -46.75276 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b51c4f7f-78d4-3bc5-9c7c-dc0f449ac12a | -14.33562 | -47.30738 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0f1fc3e-8353-3240-96b2-55b7a03b4634 | -16.69933 | -48.64338 | 2025-09-09 03:45:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9dda7e0-ae42-3fc5-93fd-6ab76c45670f | -13.75183 | -46.90044 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba562bf2-b7fa-34b0-9736-6ad73979ed79 | -16.88929 | -45.78791 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2feec224-1e68-308e-a2c0-902e64db4104 | -17.26807 | -46.74968 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 442ede42-4b16-3872-85fa-a5ca0a5f9a4e | -18.02368 | -47.12701 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17ced0ea-9d84-384c-91c2-9bce2cf88360 | -13.0037 | -45.20993 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a94b4c03-e62d-34ac-8789-d81243641592 | -11.45414 | -49.27081 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cde21cc2-8333-3be8-ae85-a6d54692cefe | -13.82029 | -43.86465 | 2025-09-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f242af-a6d4-3912-9cd8-ab9fca2d66c9 | -14.33441 | -47.31325 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 706d57a4-cc00-3a4d-8153-4e18dea7d06f | -15.15002 | -44.03045 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 955eb366-9b89-3e85-8de3-e18cf8eb1cec | -17.27658 | -46.69295 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e169cd8d-2b4c-3278-a342-36e7b701115a | -17.2698 | -46.75132 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3fa69fc2-98e6-30a0-9e62-f61e09509d88 | -18.14499 | -43.39244 | 2025-09-09 03:45:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fa83139a-1216-34a7-a222-02303e8718f8 | -11.32487 | -46.53716 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c2d0283-d359-35c1-87f3-6bdae23b1d02 | -18.02452 | -47.1229 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 636286a7-ef16-3587-9a05-620e9e7e7db7 | -16.95718 | -49.68384 | 2025-09-09 03:45:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a6caa57d-9046-3dbc-9879-830e96d085b6 | -11.3437 | -46.57431 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6c99d4c-352a-31e1-b473-3e3188ef6849 | -12.8189 | -48.17604 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c8f4c54-9f0a-3f02-bdd9-f40efb8da2f4 | -11.82336 | -46.78261 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87f27e31-f9ba-34f9-9f47-26b1c5fdf3d6 | -16.43921 | -41.97679 | 2025-09-09 03:45:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef02260f-1929-36e7-8ecc-3ced4e085e8a | -15.18116 | -41.84571 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 31a480ab-34d3-3b2e-b91c-a79b5267382c | -16.43267 | -49.28835 | 2025-09-09 03:45:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b62990ae-7bb1-3d8f-8528-76999a20f87e | -14.78703 | -48.23068 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7a9fba3-2adf-3222-8fe8-57a81d6997d1 | -17.34086 | -43.5837 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5ad9fbf0-404d-3bf2-a653-0af9f604e4e0 | -15.5406 | -48.36931 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 471e43f6-2196-3bd1-8ea8-e0c35c586a32 | -16.89822 | -45.81969 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3e82ab5-d116-3383-bb0f-e839ef6d548b | -11.64249 | -46.63043 | 2025-09-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55912cf8-8fe3-326d-9cd8-f057759ef289 | -17.08238 | -49.22679 | 2025-09-09 03:45:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a151e74-d086-3e1e-b99a-c50bfe6504e4 | -16.89933 | -45.81397 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbc3d19b-7ae0-32de-8789-5f255a6dfe60 | -13.79959 | -46.26166 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 049867dd-62bf-3b38-bc2c-867f1fb974cb | -13.65646 | -46.97439 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb8564be-06ef-34d7-adbc-1efa797f58ee | -15.82213 | -48.95618 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a795532b-77cc-3738-b73b-f7cc51da30f7 | -13.1788 | -47.2528 | 2025-09-09 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8927e555-fd4f-34e6-92e1-25c934b4a086 | -15.54649 | -48.37033 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23966e91-9a44-3514-8fa0-710ebddd7f33 | -11.30414 | -46.49323 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ad933979-ee41-35ae-a577-3b413836a378 | -14.24055 | -44.95272 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1786cb4a-1a0e-3483-9238-2a8a314c2d08 | -12.5738 | -43.78397 | 2025-09-09 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c384c022-b3f9-333e-87a2-61006d581096 | -13.93913 | -48.23269 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf057306-d6d3-39d9-81a8-76bc9bb5e040 | -13.75116 | -46.9005 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e8e799b-b994-3168-8509-3f3ad9d1c790 | -16.28069 | -45.67992 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b615206a-9468-3167-a461-27c601d0b1c3 | -17.71912 | -44.47192 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5b105ac-6025-36c9-aa44-f3b7f66549f2 | -13.94893 | -48.24546 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 618b586f-041f-39ff-98e9-98909133c451 | -18.74256 | -40.08673 | 2025-09-09 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d347c80f-6af2-3e9f-9f74-0750cdc9dd8c | -13.27361 | -43.75201 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6847565-81c8-3abd-afa1-43e207803a69 | -14.32209 | -47.32866 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8986486-9409-347e-aaae-1ef0dccc68f4 | -14.33193 | -47.3086 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7edb297-7a12-3bf8-b2db-2eae0db08182 | -14.90052 | -41.45522 | 2025-09-09 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b4377e0-de8d-30da-ac10-4dc3851003d7 | -11.81558 | -46.76196 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7963b88-72c6-3787-a653-20b9260bf51c | -14.99415 | -44.45373 | 2025-09-09 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 926f9812-962f-3111-a63f-4ad5523c0987 | -13.2919 | -43.73415 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf9e56fe-f057-3579-b655-c9cfbcd738db | -14.79825 | -48.18592 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b681d189-0d95-311b-8b1c-6d3f18d5f44c | -14.35029 | -47.32117 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f51cb0c-46e5-395c-ad7e-eae82eb57cf6 | -14.67384 | -48.19513 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17f43b09-a55c-3032-a277-ab7a010c3dca | -12.77974 | -38.49838 | 2025-09-09 03:45:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9f39f156-1d46-3cca-8ab4-480f124df758 | -12.82519 | -47.99022 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3a3d474-50d6-3dfb-8d76-dee1e0ae011b | -16.42571 | -49.29107 | 2025-09-09 03:45:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 266ab901-34e3-3c2d-ac8f-c16d32e9d035 | -14.35587 | -47.32245 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ce82134-5366-3ed3-9afe-d3e3e4b797aa | -17.48581 | -43.33546 | 2025-09-09 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab3ae391-a37c-3a7b-a0a7-ec8e87e5721d | -13.9367 | -48.2329 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cb62877-7716-31d3-a25b-2c71e7e65fda | -14.25748 | -47.10321 | 2025-09-09 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa87a3a-f099-3dfc-8576-5960182c6834 | -13.79756 | -46.27183 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98da6aed-1733-3b00-b153-b8fbef9d8249 | -11.32775 | -46.5366 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4fbe201-f0bc-3d9c-b61a-2874a33254bc | -11.63693 | -46.62891 | 2025-09-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84b21250-1176-3aa3-b94a-d0acf53397bd | -17.71822 | -44.47655 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42c280a4-40cd-3efb-af25-73df11536a8c | -12.51319 | -45.2936 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4123e913-e279-3bd3-9925-76b385dceb39 | -15.02542 | -42.15011 | 2025-09-09 03:45:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0b9b6712-4c13-3245-a0e9-7f040d6bb01a | -11.33191 | -46.56152 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcdebf8d-06c3-3ead-b3bd-5ef7553cd23f | -13.80786 | -46.27542 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d1a6043-6c27-3adf-9b2d-a5d4ec33a320 | -17.26421 | -46.68918 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e6807d3-a1cd-3be9-ab01-acacf7bab6c1 | -14.32164 | -47.31855 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e04d97c2-18b5-3a3f-add3-f85e1cda347d | -12.15338 | -43.70866 | 2025-09-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1bd16b1-0693-31a7-a44d-8239bc225058 | -18.00592 | -45.64183 | 2025-09-09 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18a557b6-dac6-350b-b45f-7713b0487a0e | -16.96581 | -45.84844 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b92b790-8fca-33fd-a8e0-9b0cc210a043 | -12.8329 | -47.98301 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fec4fb42-ae76-33ac-b1db-22ed701b35fc | -13.27478 | -43.75028 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24c03564-87e8-3c46-a42f-9b13ed20e56f | -14.33826 | -47.30609 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9d3cd9d-3875-35b8-b07d-5a94a75185dd | -15.52461 | -48.39621 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be704be7-6e72-389f-a731-122dd7007b2f | -13.74646 | -46.89858 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3954b1f9-c823-3819-862f-7517b4cb50dd | -12.82664 | -47.98311 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README19.md)
