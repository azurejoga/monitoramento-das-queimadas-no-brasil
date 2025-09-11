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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e895045c-8128-34cc-8c3d-f847c1d2c3d2 | -15.52752 | -48.56541 | 2025-09-11 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63bd6573-3f68-37e0-bc94-eb331321dd81 | -17.90202 | -44.60627 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b4511c4-103b-3a41-9a91-23d42d996526 | -19.66771 | -45.85347 | 2025-09-11 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 366bf6b7-a8b5-3caa-9319-d0f4090b4881 | -15.59466 | -49.39339 | 2025-09-11 03:57:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b0e6746-9b55-3de5-9c1b-3c098f9af87d | -19.13704 | -43.05368 | 2025-09-11 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d3c8616-2a44-3bb1-8671-965d6d800e45 | -12.98126 | -46.7424 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abbf16a8-284b-3ada-abca-255c16703c31 | -17.93275 | -44.4781 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92abcfd9-06bc-331b-9742-2e40ec85e7ea | -16.62932 | -49.76897 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a3d98f5-ff05-3776-b118-7f023f5e39a4 | -18.33264 | -44.35999 | 2025-09-11 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05116e5c-094b-38b6-b921-7bc9095b3deb | -14.22612 | -43.08887 | 2025-09-11 03:57:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3a0e6702-8271-3862-8104-854564fd0d2d | -19.95878 | -46.88466 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| afeba9a6-396d-3a6e-beb9-6e41fe3d682c | -20.33262 | -46.61454 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3610e68-1b1b-33fd-af2e-2d210082a1e8 | -15.62776 | -47.54076 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeeda4e4-5267-3280-bab7-3c1d33b22935 | -16.60619 | -49.77848 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5abc2e03-fdba-38d9-8f88-244dbc9891c8 | -15.59401 | -49.3966 | 2025-09-11 03:57:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84d8aad6-3612-3300-884d-f312818390f1 | -16.30262 | -50.06047 | 2025-09-11 03:57:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed6be1e5-e6b5-3d96-9bc9-8fa9653d6b84 | -17.06956 | -49.67136 | 2025-09-11 03:57:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbac3881-b81b-3d62-bf7f-8a4854d06e82 | -15.71872 | -41.87691 | 2025-09-11 03:57:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 07a77518-8a6b-3a3c-95f7-5878dd8c246a | -16.08725 | -47.35065 | 2025-09-11 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40a7a815-70e8-3231-b0d2-7d39f16b2738 | -15.56046 | -54.7719 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f1e6a74c-0294-3759-88f2-20ab0b29b72d | -18.15331 | -48.09949 | 2025-09-11 03:57:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a1d52ce-ec98-372b-a55b-596de4514c13 | -15.21722 | -44.05668 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d84718d-7b66-3fc1-9f66-fb48b0d38d84 | -20.16073 | -41.04269 | 2025-09-11 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 43a615bd-1aa2-31b8-b7d7-caa2baf353bf | -14.41537 | -47.33063 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1d372f0-1e65-30dc-9ed7-8dda0ac5ba28 | -20.53893 | -47.61729 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71e85707-2e08-3966-983a-76b2c98563bb | -17.90427 | -44.59318 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9f00de8-af2a-3d3a-89cb-625d4e1170a0 | -15.95485 | -50.22266 | 2025-09-11 03:57:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38b8a317-99ca-3bff-bd2f-3793cb4f6312 | -15.58352 | -43.42385 | 2025-09-11 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f50ff4d-3646-3538-b24d-7723b73684ce | -15.81285 | -52.22561 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d59249c0-bd16-35c2-8c43-230d51fa6f3c | -17.33438 | -46.69641 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7c87048-f6b3-391e-a902-08fe10dbd9d3 | -14.77492 | -48.23198 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c15b23a-1b7d-3cdd-8314-d0d02985baeb | -17.50609 | -43.75311 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 471703d8-7cb9-3dd0-a1b8-933010e29478 | -15.15875 | -52.42189 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dec9126-4dde-315a-be5d-f1e86f2d10f7 | -20.39171 | -45.79602 | 2025-09-11 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32519f8d-cd2e-3018-9afc-642072477e28 | -14.3833 | -47.30233 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa241c89-4194-3d08-87d6-7a7c706e8331 | -12.96871 | -46.73553 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51a12a81-34c9-3c60-b0bb-226ee73a4b62 | -20.22658 | -41.01258 | 2025-09-11 03:57:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f6afcc9-118a-350d-856d-8f80e4eee672 | -18.01459 | -47.99689 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11cec7ca-93a5-3b22-b64d-e8233bc606c6 | -17.25002 | -46.08566 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f74b0a3-c8b7-33ca-946e-41fc6df35c9a | -15.14298 | -52.43565 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f231d65-7b79-3ad9-b0c2-f75520c23c9e | -15.22528 | -44.05357 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 544682be-1de3-3dcf-bba5-818276fe213b | -17.73736 | -44.45308 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5bb0582-db34-359a-9770-d4ea6c686ea4 | -20.23861 | -43.58294 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3708a0fd-2784-32ec-87aa-545186ef343a | -13.58855 | -47.7034 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea864f20-08da-36dd-a2e7-4c66e126701c | -12.98206 | -46.73803 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb6b95d5-4ec9-3a53-94e8-9b6944141983 | -20.24035 | -44.81638 | 2025-09-11 03:57:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f531435-ad2b-39e9-8ff4-576dfe7e1880 | -14.71673 | -45.34146 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bbabbc8-d451-31bc-a6ea-32adbe074b73 | -19.91032 | -44.23823 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 80f08ae9-d67e-35ce-90c0-d21563b45af1 | -20.70053 | -46.07457 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d3ac46bf-0eb5-3468-99cc-ca411ace3ae6 | -18.50378 | -47.41973 | 2025-09-11 03:57:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7acac97-a7f6-308a-b664-9d2636309291 | -16.6055 | -43.67892 | 2025-09-11 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31bfcf0d-a937-3b3f-ac14-5f07ba3bd204 | -19.99485 | -47.62454 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b204cdb1-cbb1-3abd-8560-13c6d0f01575 | -14.56229 | -48.76822 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52e1c14b-5f3e-34e0-962f-4f28a2e1d56c | -17.2042 | -50.15498 | 2025-09-11 03:57:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfb43790-4f39-374c-99e3-753b79d857a2 | -15.941 | -41.82843 | 2025-09-11 03:57:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 510e0dbf-fb9b-37e3-a504-7ee3c65643cd | -18.40663 | -44.43483 | 2025-09-11 03:57:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73c266da-1cf1-357c-aa3c-229c8a6f2c60 | -20.39895 | -46.27486 | 2025-09-11 03:57:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e56b7450-5c2f-3a7f-8925-29d1fd8d9be2 | -18.84755 | -46.8727 | 2025-09-11 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25dfb51e-5018-3d73-8a25-07ffd14f66e4 | -14.53805 | -42.47739 | 2025-09-11 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77e0b938-9bd1-305f-b0cc-1e12c3fc32e5 | -17.25257 | -46.75667 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43a42aec-180a-3f95-943a-458478ac04da | -16.62114 | -49.78312 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2dd88da3-cef0-3a8e-af3b-eeec27c1dee8 | -15.98036 | -42.98368 | 2025-09-11 03:57:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 287a2287-6489-35c8-bdf5-a330cc8f6124 | -13.92915 | -48.23172 | 2025-09-11 03:57:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2ca6afb-795a-3152-9982-0cef15795e78 | -16.60743 | -49.77242 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5cd311c-699f-39f3-96c6-d6a18efe7ebe | -15.6746 | -47.03036 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e8839f7-ce7d-34bd-9e63-624d1fc548fe | -19.65731 | -44.90271 | 2025-09-11 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8452e3e9-5422-3b82-975d-a0cc619199e4 | -19.78479 | -45.59006 | 2025-09-11 03:57:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 162cf013-b3f3-3d71-9e4d-fdb0da50786f | -19.70172 | -45.92467 | 2025-09-11 03:57:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbaf04b5-d071-3290-91f3-b52454a97ab8 | -15.48701 | -49.36034 | 2025-09-11 03:57:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 397c0a5e-747c-3cd3-9e49-2741fe827888 | -14.30145 | -41.68973 | 2025-09-11 03:57:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6ac476c-e896-37df-bc4f-e0e625314047 | -15.79437 | -52.25312 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccbd9a5a-8827-3549-b073-d386a58aa095 | -17.55821 | -44.55001 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c8c5f69-e454-3925-9180-64ee9b3f97ad | -19.66088 | -44.90351 | 2025-09-11 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d8f37cf9-2b6a-3615-b85c-6e9cfb0ffedd | -17.26736 | -46.08064 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecc1ecb2-863d-3731-a6c5-4ba99fb265e8 | -19.37277 | -43.64899 | 2025-09-11 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 369518e3-8aa2-31da-b54d-cebe0abc658c | -18.0093 | -48.00053 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d68d10-e28d-3553-b0ae-85cb6f39e64a | -20.52046 | -47.63444 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80d9f90-8eb4-3bed-8806-681ecbd78899 | -17.25186 | -46.76055 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91b23567-f7d1-38e7-b575-92bef6d755d6 | -15.80689 | -52.28281 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed07aede-86b5-38dd-94f6-dbc073da874b | -15.89362 | -48.18082 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c11b378-3b26-36ba-8ed4-f9868285ed14 | -14.38577 | -47.33879 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f41b8018-67d9-3580-8d7e-928d776c715d | -19.16238 | -43.4968 | 2025-09-11 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfdbc071-070b-3596-925a-2de62703e4af | -13.01731 | -48.72121 | 2025-09-11 03:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99b006cc-591d-39b0-91a7-12810c004c51 | -17.25725 | -46.09105 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7aad5679-6d2e-37f8-b587-6c7af94a8401 | -17.8395 | -46.7396 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52c66a72-2f10-3f2f-8aca-54741858d69a | -17.84628 | -46.74889 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16ae17ec-4250-3f10-ad70-2087352b2bfc | -12.98006 | -46.72388 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca721729-6ddd-31aa-9ffb-9934a2e00f5e | -19.15876 | -43.05717 | 2025-09-11 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 337cd6e6-8516-3edc-8f2d-1cb98083efc0 | -17.7268 | -44.42859 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1a26ee1-2b18-3959-af4f-4623d11d0cde | -17.90285 | -44.6049 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b7dd2ec-bec6-3e0e-bc3c-006f89bce70a | -19.80189 | -47.16247 | 2025-09-11 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b30b0e-8d07-3f49-aa94-38b1c2df3cf2 | -20.07088 | -45.29153 | 2025-09-11 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 423663a7-c4ab-3878-a3f1-c79b8d253820 | -15.13719 | -48.61099 | 2025-09-11 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6aea37b9-67f6-326b-a004-94e7d767702c | -19.48117 | -44.32274 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 893d54aa-2674-3a80-a12a-189bb2d9d3e7 | -12.88771 | -47.96125 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ca90367-1e53-3cad-a48a-c6061fdcf804 | -17.90564 | -44.60695 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81b0eb6e-3943-3897-9518-e25181d992bb | -13.78849 | -46.2891 | 2025-09-11 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b0bc66b-8322-3bcc-9b04-2020fe999a83 | -14.74188 | -46.29227 | 2025-09-11 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac07ec6b-a059-35a9-aab6-85d887efb4e6 | -17.96155 | -44.48333 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4b66d58-025f-30db-b68e-25bef22d4721 | -16.62317 | -51.82171 | 2025-09-11 03:57:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README33.md)
