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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40fa2468-4a41-3145-8f0a-547ea0af9af1 | -17.26296 | -46.69539 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72f5057-e3de-3ecb-9958-ea0182ebd487 | -14.30846 | -44.8776 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0db371a-16a3-33d7-9370-dd1c3d9c4a10 | -13.00312 | -45.21289 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80fea8d9-7eb7-3999-aad1-cb328614fad5 | -15.82364 | -48.95401 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55c087d0-4974-3826-94d1-593146a132e1 | -11.33463 | -46.56091 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b280994-66a0-3856-a73d-e8ea42a1d761 | -15.82806 | -48.95798 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a9d3470-31f9-395a-8817-d84d8636fb32 | -15.11929 | -48.05574 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3e13329-52e9-37b5-ac02-39e21c7ad5ac | -13.95464 | -48.24797 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7203040a-27c1-3000-9473-d38e83d7c69c | -13.72526 | -46.8897 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09781e3e-26ce-3592-80be-87efe14ecb47 | -16.95231 | -49.68359 | 2025-09-09 03:45:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb515318-e35e-3c6b-bf22-9bd278376662 | -18.66617 | -41.43338 | 2025-09-09 03:45:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a08a92e2-706d-3ec2-9576-99138a14ff2e | -11.82434 | -46.75925 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9688808-8a2d-3a14-8a82-d983bf82a66e | -16.19772 | -44.21935 | 2025-09-09 03:45:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af8801c5-99d4-3e5f-821d-ceac47cb23e6 | -17.65364 | -44.17865 | 2025-09-09 03:45:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95067cb1-d997-3467-8990-8c2ad11e30dd | -16.95851 | -49.68479 | 2025-09-09 03:45:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94334252-5d09-3448-b1ac-43d8f1aa351d | -13.47944 | -43.51067 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 706bc07e-8fbc-30b8-ba5a-b88770d91532 | -16.42678 | -49.28617 | 2025-09-09 03:45:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 329a5a8f-d2a5-3a5c-b5b7-60b49027cdee | -12.15631 | -49.08168 | 2025-09-09 03:45:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 890a7d25-cae5-36f6-bf80-85fdd31e3863 | -17.3407 | -43.58075 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4c521b5-1c6d-354e-b12f-652fbfbb0788 | -21.3274 | -46.69478 | 2025-09-09 03:47:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a96f7184-11b2-31ba-856c-56b51a818d11 | -22.22803 | -49.72701 | 2025-09-09 03:47:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| eacd371f-7f18-34b3-872e-4e617e939613 | -18.76798 | -48.19656 | 2025-09-09 03:47:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 206684ed-7a15-32f1-b85e-2e278be0e8ab | -21.62544 | -47.02824 | 2025-09-09 03:47:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2e7a2c2-682c-38f5-b2c3-92f3936280c2 | -18.81701 | -49.68258 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 64c62bbd-5fe0-3cc0-8afb-befa32957bad | -19.36388 | -47.4625 | 2025-09-09 03:47:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d73951-a83d-3afe-bdc3-98f4e40dfd56 | -21.00258 | -46.06227 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aa443776-ef65-3a00-a322-ab97e0204d4a | -18.82503 | -49.6911 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6214789c-00c1-3288-af3d-29735aa163fe | -22.48087 | -44.43064 | 2025-09-09 03:47:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 85c26661-a7e3-30bc-9dfe-4e93d086fa07 | -22.32852 | -48.81755 | 2025-09-09 03:47:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4a06d26d-0458-3a7e-928b-55cb179e2038 | -23.59903 | -46.35452 | 2025-09-09 03:47:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46e310f2-68ad-361b-ac84-b6c50f85759e | -20.07076 | -47.3599 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 111acf0f-700c-357b-84ed-5c07c386ce09 | -23.71501 | -47.46328 | 2025-09-09 03:47:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 34b819cd-ce0f-38a8-af6f-19ad435391a5 | -18.46672 | -49.55608 | 2025-09-09 03:47:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 372de68b-991a-3a82-b211-d157078addd4 | -21.4342 | -48.86066 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c44d1e7d-c639-3b44-a62d-5471395045bd | -21.44364 | -48.84352 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 46f5209f-9059-31ce-9fc0-2c2be46db658 | -18.47255 | -49.55795 | 2025-09-09 03:47:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6372a53d-3c69-3ad6-bfdf-a4a2a9053c6d | -22.66736 | -44.98434 | 2025-09-09 03:47:00 | NOAA-20 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c04e7c5-8030-308d-a702-3cdd8171cd6c | -21.43789 | -48.86953 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2230a01-44ab-39d7-bf8e-340df3f6d322 | -20.04364 | -42.03707 | 2025-09-09 03:47:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0592ac09-96b0-3170-afbd-dcc279fe0b6f | -21.58247 | -50.35165 | 2025-09-09 03:47:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a25eeb1f-2e9a-3195-aa37-b7a63cc3c5c3 | -20.07577 | -47.36114 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 110b39ad-9fed-364f-b627-b6d3f177e0ae | -19.90762 | -43.85514 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 2d8bab0e-b891-3b1a-b91c-114889d93ed9 | -19.5348 | -46.09641 | 2025-09-09 03:47:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 095de249-e671-3167-a667-47b431c14fe1 | -20.4803 | -43.6301 | 2025-09-09 03:47:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b719d517-f3a5-36cc-8b38-3a68ffba1be2 | -19.82919 | -48.16866 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e468269-a477-35bf-a995-9de46176a65e | -19.70516 | -43.52691 | 2025-09-09 03:47:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3b4f7f3-f617-34d7-b90a-dd53fe4c4c5c | -18.82118 | -49.68015 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5581ad49-17a2-339c-abdf-d06d56c9abd3 | -21.58041 | -50.35086 | 2025-09-09 03:47:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 50919013-076b-3a18-932d-805e977f9ab4 | -18.79327 | -49.63693 | 2025-09-09 03:47:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d03a2bd-8910-348b-8e28-2fb819287739 | -23.14305 | -48.26139 | 2025-09-09 03:47:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a0006618-8c7b-351d-a415-fed6ea4a0ac6 | -19.78467 | -47.99729 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6470d1d-ebda-3cab-a787-4c16083aae7c | -23.06341 | -44.96379 | 2025-09-09 03:47:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 55014f5a-d500-3a52-acb4-fb613ef3bf60 | -23.60002 | -46.34972 | 2025-09-09 03:47:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c6dfaab3-a64f-3432-8256-7e72f5026926 | -21.23463 | -49.88336 | 2025-09-09 03:47:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a52e56bf-24f2-3181-8a2b-a20d1188ea0c | -19.93527 | -43.61827 | 2025-09-09 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 34807a7c-9a66-3b98-8ac1-381c31341d94 | -18.76714 | -48.20052 | 2025-09-09 03:47:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7ce1d01f-b24d-363c-8e6f-9ecaaafd9ca3 | -21.1949 | -46.12021 | 2025-09-09 03:47:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1e95fd82-79f9-395f-8e9d-a5df958d428e | -20.44742 | -48.05857 | 2025-09-09 03:47:00 | NOAA-20 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fe32edd-a589-323a-9155-b8bb195bbac6 | -23.34091 | -45.44672 | 2025-09-09 03:47:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b736aa06-369c-3ccf-bf11-a9fdb620d2ec | -20.56188 | -46.362 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3c77ac-6ae7-37fa-b055-70611635ca95 | -18.82775 | -49.69036 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3f614e5-2492-39a4-905a-875c1fd4a142 | -20.45583 | -42.51115 | 2025-09-09 03:47:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d7e3c60e-6463-3b1f-be9c-447feaab0d4a | -22.33441 | -49.01897 | 2025-09-09 03:47:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba5e970e-601c-3b92-8c4c-bae1303651b7 | -21.63616 | -47.02491 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10e69a55-ff7a-3959-889e-f8ead2400f5e | -20.99925 | -49.31707 | 2025-09-09 03:47:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b5b026cf-45a5-3b16-aff9-330f17d2bc74 | -21.39672 | -43.85872 | 2025-09-09 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df94f739-887d-3e6b-a8f7-b35e3dae5f55 | -18.81806 | -49.67793 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a035dc9e-759b-3a9f-96d9-9ba0171417fc | -20.44666 | -48.06214 | 2025-09-09 03:47:00 | NOAA-20 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b9bdaa6-b293-3e90-89a7-3d071dd85a92 | -22.22888 | -49.72327 | 2025-09-09 03:47:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d942d76d-0aec-3879-9052-5013ba1abe29 | -20.04442 | -42.03278 | 2025-09-09 03:47:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 355e2962-fcc3-31a8-9299-bfc16c10e7e7 | -21.43172 | -48.87186 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3d47acf-5d21-35f5-a333-e2a626d2d0b8 | -19.41465 | -46.5158 | 2025-09-09 03:47:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d655c4b1-3e78-3af9-aa22-8ced23fcb5ff | -21.57938 | -50.35524 | 2025-09-09 03:47:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 884bba98-ba39-3762-b87a-69d70ba0c210 | -19.93598 | -43.61443 | 2025-09-09 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8e747a30-0c0f-3eea-804b-119e71b59b5b | -20.07967 | -47.35908 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b831114-cc0c-3a67-b104-bc9f6ad3f3ad | -22.92832 | -49.16953 | 2025-09-09 03:47:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b47783e-d4ad-38ee-aa06-df2d919991cf | -19.68458 | -43.70445 | 2025-09-09 03:47:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2fc7c6c-5fde-3eca-bd6e-d7593cc9d300 | -18.82014 | -49.68489 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 514caff8-2167-3785-ae37-f1649e4d46eb | -19.89788 | -44.55807 | 2025-09-09 03:47:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d55448ec-d317-3a1a-859c-696fb392f29b | -21.43906 | -48.8387 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 05f07f18-9214-3646-aeae-8350e8403b89 | -19.78992 | -47.99856 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8544b1dc-f8cd-3551-a4ce-ba68a393416a | -21.44444 | -48.83989 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| a4c72397-49f8-3084-b212-af375b7123e9 | -21.63498 | -47.03057 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0f4098c-8d6e-3f46-a5ae-eb0281e3ffed | -23.14229 | -48.26492 | 2025-09-09 03:47:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6757d073-2c46-3473-9774-9fd0a0b8f9d1 | -22.92473 | -49.16052 | 2025-09-09 03:47:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7484e6a-444a-39fc-958b-d1ee07c61332 | -18.79917 | -49.63844 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f9e0e09-4a03-3721-8aa4-a3560ae9af78 | -18.77344 | -48.19772 | 2025-09-09 03:47:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f0c50a6-b083-3e6d-aa35-927bc586cef2 | -20.16923 | -44.79854 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de045b6-7576-386c-9fc5-2c3282774541 | -21.72244 | -46.23367 | 2025-09-09 03:47:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0feb753b-a603-37a6-aa74-c761974ae887 | -18.81912 | -49.68958 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 24c129ce-7680-31ba-8eb0-cab8a2f6a968 | -21.19032 | -46.11933 | 2025-09-09 03:47:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98cfb107-4d84-3821-9ea7-a1dd6fa6c26d | -18.82222 | -49.6754 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2694b668-41cb-3d0e-986c-3be7df2c4e42 | -18.82288 | -49.68423 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e65416c0-87e8-36ba-a2c0-79559ee6db8d | -20.07715 | -47.35444 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ab51b5e-b3e0-3fe5-8830-c7e4628130d4 | -20.0751 | -47.36443 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eed0c4e-167e-3119-8d20-e133462aa642 | -23.43786 | -47.12846 | 2025-09-09 03:47:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b25bc52-7e18-3878-ba7f-7aeca5b56951 | -21.63976 | -47.03167 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 35713a86-1f6f-3919-9f10-52f369df87d6 | -20.07646 | -47.3578 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68964a56-2e82-360c-996a-b6d593097204 | -20.02526 | -48.53111 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6c82fcf8-2de8-33cd-9946-2880c3616164 | -21.22893 | -49.88186 | 2025-09-09 03:47:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README21.md)
