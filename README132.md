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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7847ac5-db04-379c-9ca4-bcbeb364a178 | -11.9137 | -46.35802 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7ddf33f5-6cfe-3c0e-bb2c-d783e2712757 | -11.91928 | -46.40928 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5d28666e-334d-372e-9fd3-863fe5dbce48 | -11.80289 | -45.0183 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 91439056-b5a5-3710-acaf-57cbfe0ba6d9 | -13.9839 | -48.18521 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 70964ecb-b0c0-3aab-9e47-b4f70dc91345 | -13.3916 | -47.54231 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c16ed78b-f20c-347e-bba4-5c61d88ff0af | -13.10513 | -47.85125 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 4f56836e-aedd-307a-81ae-cd228ae450d0 | -13.18141 | -50.94401 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 46ba9879-8e24-3649-97ed-1a30dee8ec99 | -11.14939 | -43.38369 | 2025-10-04 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4db91fd7-d9b0-3b65-8421-aa34e07732a9 | -11.91136 | -46.37227 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 76223945-2a19-3e7c-9d10-0f98c2a916cc | -11.92008 | -46.38803 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d13713e4-0485-3546-9c8d-f03b311759d5 | -11.9224 | -46.37378 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 33cbe526-2639-35b5-8a56-7fab1ef0a6f6 | -13.38771 | -47.5469 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fc2b0278-5957-333a-ba76-1fd91d0dfe19 | -12.53297 | -45.9617 | 2025-10-04 05:36:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 42a7634d-9527-3b47-9544-baa757f03686 | -12.90835 | -46.90855 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 99d72f78-7cde-392b-b457-4b900a9ddc5c | -13.16612 | -50.94102 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b52e1302-253c-3c0b-9a82-85be7272b0fe | -11.7916 | -46.81476 | 2025-10-04 05:36:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 465a735a-15ba-3a48-aba5-f9b96efe36c6 | -13.30905 | -48.13328 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| dba1ce27-2d69-3a92-8b6b-91f28ecebdfd | -13.11918 | -47.94802 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f9c3dcc9-844a-3c2d-9835-92fdad0e2a12 | -13.11442 | -47.94196 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| eabf6348-d7b3-3547-bf60-47c98a0a6c96 | -11.4542 | -45.1418 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| edafdf0a-ecc3-3e92-be3b-7a6e38ea09a9 | -13.24406 | -47.83086 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d78e45fb-c799-3312-a85a-ee109a6446f1 | -13.12611 | -47.80152 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 57888c39-3870-3ac9-8773-7fb8d793bb74 | -10.33537 | -50.32483 | 2025-10-04 05:36:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 2d6da7a8-8e95-3d95-8d24-09b8f3692780 | -14.00037 | -48.19467 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a702c247-c6e6-3486-97d2-769876d06223 | -13.31865 | -47.61529 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| d2a1405c-7682-3006-9abc-f8ec82db3954 | -12.70764 | -48.54736 | 2025-10-04 05:36:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| b4b5e0f6-6dc0-31e3-9af0-2b21fd2c37e3 | -12.64467 | -46.9719 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fe7fa789-0733-3bda-9215-2b586f9586ae | -11.49208 | -46.74334 | 2025-10-04 05:36:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d2c0358e-0556-3a17-898d-2f897912794b | -11.4471 | -43.49037 | 2025-10-04 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e91728c-4641-34c7-831a-2b741f80dab0 | -11.48327 | -45.02497 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 03feac56-6b42-36ac-9afc-211220f97f8d | -11.11712 | -47.89698 | 2025-10-04 05:36:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f6231b6e-083d-317b-98b9-950a7d28ecaa | -13.93618 | -48.14996 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c397bbac-edaa-3de3-9db0-182030847967 | -13.11745 | -47.92431 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c5212ad5-3db8-3576-a365-9362ec2a2cf4 | -13.33112 | -48.07965 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2a8f6ef2-bd06-3701-8a91-6fa1d2412f0b | -17.90883 | -57.625 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3a57594d-c34d-3421-bea5-e87f38520c9f | -18.17392 | -53.34921 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61cc05c-0c7e-385e-b2c6-3daa48f15565 | -16.15525 | -57.58287 | 2025-10-04 05:36:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6fc74b78-da1a-3a02-b11f-9f3b86190e75 | -18.1797 | -53.35358 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c95a8ee-21f4-364d-95c6-1192e5821c87 | -17.88916 | -57.63206 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8121ad4f-831e-32dc-9492-be3ca0f15efc | -16.35888 | -51.47611 | 2025-10-04 05:36:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f43dcf88-85ff-35cf-b01c-b6ed4a411d6f | -18.17325 | -53.3534 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aca76cc-bb92-3ea9-8479-434343fe2ffd | -18.17384 | -53.34758 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c189bf5-7ea7-312e-8438-16c281265481 | -18.17865 | -53.36122 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a8ecb0e-a0b5-3d54-8a15-3b76b998aa33 | -18.17277 | -53.3581 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeb9676d-2a70-3ff3-a0b0-08754a173438 | -17.86337 | -57.61226 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f51d50a0-32c2-3791-b007-5bea2c001da2 | -18.17908 | -53.35693 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb25d3bc-c88c-36ec-bd1b-4796a26ae9c9 | -18.17926 | -53.35811 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f4517b58-6cf7-3eb2-8583-b3c89d91613a | -17.95736 | -57.56293 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ad779f31-d3d1-3421-a8e4-9f54db63a527 | -17.90752 | -57.62632 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| aafbc85b-d601-30a0-85cb-7e0e124dfebf | -16.15974 | -57.58379 | 2025-10-04 05:36:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9566a2cd-0a82-371f-b213-c6a9923e84a7 | -17.99354 | -51.63638 | 2025-10-04 05:36:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 612f0d99-700d-32cc-932d-055955a1dfce | -18.18534 | -53.35636 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 604fa24e-cc59-3239-b602-facc4b264db4 | -16.35945 | -51.47047 | 2025-10-04 05:36:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31bfdcfd-af89-30bb-b1ca-5d326b0e1d1a | -18.1734 | -53.35474 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e725f6c9-5685-3ef8-bcaa-2bc65ce4af57 | -18.19783 | -53.35809 | 2025-10-04 05:36:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30fa8e47-5365-3476-990b-aaca89c684da | -18.23393 | -53.36888 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d8ad22-3ad9-3255-99c5-b4c3507c8665 | -18.23446 | -53.36354 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dbf358c-ddf8-33c6-a388-bc50c6886ee5 | -17.99479 | -51.63641 | 2025-10-04 05:36:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bbba46d-4429-36d9-9f4c-c3d3f47844d1 | -17.99291 | -51.6432 | 2025-10-04 05:36:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67c23c45-8382-35bd-bd07-7e8f52b36991 | -18.23347 | -53.37353 | 2025-10-04 05:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 719c143c-d6ef-371f-926b-2a977d35e89f | -21.04019 | -55.74414 | 2025-10-04 05:36:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aefa2f74-607d-3e02-9387-5d233b7b8778 | -17.89326 | -57.63697 | 2025-10-04 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a0c603a8-c38c-3215-96bb-1bebbbfb2029 | -19.96607 | -43.70346 | 2025-10-04 05:38:00 | AQUA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a57d6e03-c0cf-3de4-a029-c2beba84dc30 | -20.12371 | -44.00051 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| 72010954-928c-3fa1-aa1e-10c18c731376 | -15.72897 | -46.27681 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6a1189e-9a1d-3d13-96bd-b760ca256e29 | -15.72753 | -46.26989 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 11e71c81-81fe-3737-951a-bce10fc85178 | -22.28442 | -46.75483 | 2025-10-04 05:38:00 | AQUA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| a67cb172-aba0-3ba8-9ece-ae16915cc8f6 | -20.2245 | -44.17835 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| fa3004e5-22fb-3ec1-95b7-53af3df07904 | -14.8883 | -48.29987 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 70365faf-eebb-3f43-8c57-dc6fa78f84f8 | -14.8908 | -48.35685 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 94da1abd-2988-33a2-9e29-5dbe52152f46 | -17.94638 | -47.02578 | 2025-10-04 05:38:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5c510362-9d7b-3745-8d44-e0ecdc9eb053 | -20.12515 | -43.99105 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 145.2 |
| 50030c7e-ce11-3dd7-acb5-187343f77dcd | -20.13396 | -43.99261 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 682fc7e2-7c7c-32a5-846c-d673ab45bb5f | -15.534 | -46.82559 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 09b40e8b-4460-3705-b3d5-36d3d6b364d4 | -15.53175 | -46.839 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 89e51f6f-83fd-3127-9f23-fa7f4fb2d0cf | -14.8664 | -48.35354 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0544fd61-9ad1-3854-8728-a962e6a738b3 | -15.37774 | -47.9449 | 2025-10-04 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 48db8592-7c9b-302d-a8ff-6715d0d4e198 | -20.13737 | -46.4184 | 2025-10-04 05:38:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2cfed1d-f1ee-30c8-a9ba-2a53649b3059 | -15.03571 | -46.97784 | 2025-10-04 05:38:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9730ebef-23cf-3c87-9048-1f93488c2d16 | -17.98587 | -45.00528 | 2025-10-04 05:38:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41bae925-9247-3829-aa00-209d973096fe | -20.13539 | -43.98319 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 847af823-0a68-3cbd-b64e-cc5142f3f5e6 | -15.52323 | -46.82457 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8b298247-4c14-3c47-a5d8-c2177c58b136 | -15.35482 | -46.30246 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1faffb85-7064-3e04-a23e-9cfd6686e872 | -15.19462 | -46.38511 | 2025-10-04 05:38:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ab56c5da-6b77-3384-9eb4-a046a0dde7aa | -21.59777 | -45.28155 | 2025-10-04 05:38:00 | AQUA_M-M | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2f6da17c-4d12-324a-b860-192916cfc0f1 | -15.67804 | -44.51188 | 2025-10-04 05:38:00 | AQUA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| afc69fbd-e30a-3ac1-885a-b10950550417 | -16.29102 | -45.2387 | 2025-10-04 05:38:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cc9919d8-7b9d-30c2-97f5-01fa287a05cd | -16.35301 | -47.06532 | 2025-10-04 05:38:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b49a67bf-3643-3e4f-9ad2-d91470d0f989 | -14.68349 | -48.27108 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2ddcf44e-4326-35b7-97b3-1c2bde30d658 | -15.35262 | -46.29541 | 2025-10-04 05:38:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f14bbd46-61ff-3366-9ba7-79236d3a35d7 | -21.68898 | -50.0611 | 2025-10-04 05:38:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| f86e5780-9e00-358f-9e42-1df26bb0d1f1 | -14.66535 | -48.30288 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| ca147272-486d-30c5-977a-3e3bd62f458b | -20.22594 | -44.16903 | 2025-10-04 05:38:00 | AQUA_M-M | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 0c05f58c-8f1b-3478-a927-2140b0815780 | -14.89148 | -48.28168 | 2025-10-04 05:38:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 204d97f6-f2d6-321e-b65a-92130210cb79 | -15.03819 | -46.96306 | 2025-10-04 05:38:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 719b8d8a-6ce5-3d70-a47a-dadb8c06078f | -15.62043 | -46.93268 | 2025-10-04 05:38:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b444bb5e-7fe2-3908-9848-e471bb5739a9 | -21.78469 | -45.32788 | 2025-10-04 05:38:00 | AQUA_M-M | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| ddd8c911-777d-31ae-9370-cb669bcceb83 | -15.62273 | -46.93975 | 2025-10-04 05:38:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2e533f87-0359-3014-94ae-c93373021c5a | -21.67708 | -50.05824 | 2025-10-04 05:38:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| d22e1ac1-d13b-3567-93b8-f0cf1551cd30 | -17.70064 | -47.0837 | 2025-10-04 05:38:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |


[Clique aqui para ver as próximas entradas](README133.md)
