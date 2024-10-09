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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9672db74-c747-372d-af1c-6f78b00dca96 | -20.34918 | -48.78018 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deaedf95-d1e4-3927-bf2d-2c4cc23b88c6 | -20.34852 | -48.72769 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a76f5fb5-6e50-3900-b60c-5767eae65632 | -20.34495 | -48.72057 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de289e2f-6c9b-3006-9053-6ce5ea9ff331 | -20.34184 | -48.86384 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c99286c-14e1-3f04-8e28-8e5ff9aa9e34 | -20.34122 | -48.72003 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aee8e76a-d19e-3d1c-a1c9-d31d8148edeb | -20.33999 | -48.86624 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d17cc96-7ff8-3876-90ec-49a69c5e7f5f | -20.33994 | -48.72932 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ebe5c3bc-3b48-3091-a0ce-952580c480b9 | -20.3393 | -48.73397 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bd9ce86-c207-3bb2-9c34-1e4ea16fe65c | -20.33814 | -48.86327 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40afa4b2-f5e4-3ea8-b9eb-0596a84695ff | -20.33685 | -48.72412 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 468568a8-8347-37e0-bd67-5de4e409c2d5 | -20.33629 | -48.86568 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7455c5c1-5543-34f3-80fa-ea9b9b4928c3 | -20.33622 | -48.72874 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ed8b7bb3-64bb-3983-ac46-e7294e80d892 | -20.33562 | -48.82536 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6f6bfcf-11e6-3924-b707-060b3a6b383d | -20.33396 | -48.82784 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c21e2c6f-d354-3723-9ea1-8d49d646406a | -20.32505 | -48.72695 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 3a62d6f0-427d-3876-bf01-4443c3378c45 | -19.81406 | -52.23828 | 2024-10-09 04:42:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 24f590f7-ace4-3e91-bc2a-67cb3b7d6688 | -19.81349 | -52.24195 | 2024-10-09 04:42:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2e2e0dd6-5a60-3fc7-8d29-420496aa2bc7 | -19.81016 | -52.24137 | 2024-10-09 04:42:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5b0abbbe-6d23-3edd-a144-255fc349f783 | -22.48154 | -47.59495 | 2024-10-09 04:42:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c2503424-7757-39ae-9347-2e7a99bfe7f6 | -22.47745 | -47.5944 | 2024-10-09 04:42:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc545bd5-ab35-3dae-ac98-705925228a86 | -22.23038 | -43.41063 | 2024-10-09 04:42:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2784890e-02de-3112-954a-de53b26490d3 | -22.23003 | -43.41408 | 2024-10-09 04:42:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ffb91f8c-d92e-30b4-b60d-0ad9bc37294d | -21.62871 | -44.63895 | 2024-10-09 04:42:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 040e8471-40e7-3b0c-9eb2-d1bbe25dc566 | -21.62501 | -44.62712 | 2024-10-09 04:42:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 09b5c7ae-67c9-36c2-8d66-761e03d129b4 | -21.62437 | -44.63322 | 2024-10-09 04:42:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f8ff021c-520b-3f34-935a-de07b1ea5a97 | -21.62376 | -44.63903 | 2024-10-09 04:42:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf56163a-84ab-3d96-9f7b-0feb84dc537a | -21.5197 | -45.59787 | 2024-10-09 04:42:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 47ab222f-9fea-3384-9a92-4f92cd0c4c06 | -21.51915 | -45.60276 | 2024-10-09 04:42:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5edaf29f-02e4-3a68-9f67-a64c5b71ae44 | -20.70019 | -44.61205 | 2024-10-09 04:42:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 05323059-3263-3d4e-972f-edce655fb356 | -20.68007 | -42.32975 | 2024-10-09 04:42:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f06bca71-8f3f-3ddb-ac29-da4d22fe0a66 | -20.67971 | -42.33357 | 2024-10-09 04:42:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45069b6e-4f55-330b-99a5-c9355b1dd9bc | -20.67692 | -42.3314 | 2024-10-09 04:42:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f3012769-4285-3292-97a6-5a3fb0d7dbcd | -20.5835 | -43.28028 | 2024-10-09 04:42:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 98571df3-14e4-3ac0-9e8a-ec623e68dff7 | -20.58232 | -43.27937 | 2024-10-09 04:42:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 82acc0e6-9413-384c-a9ef-74b8f6504c14 | -20.57823 | -43.27964 | 2024-10-09 04:42:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa27c838-4916-3069-8808-8f408e1b2ace | -20.38967 | -45.39474 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d869f759-7bd8-3a6f-acf9-0db2009fb639 | -20.35792 | -45.31535 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| de838993-3b8e-3fd9-8e95-921cb5a12824 | -20.35732 | -45.32037 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bf80f8f3-fa96-3cde-baf4-4ad6f62f8c82 | -20.35666 | -45.31656 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c28215f2-7849-3915-b767-92d8c01afe34 | -20.35609 | -45.32158 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44684671-71a0-3283-8733-d1d452c49f0e | -20.35271 | -45.31989 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ab859e08-f388-3464-b359-ca10e8049045 | -20.35149 | -45.32108 | 2024-10-09 04:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f0f6aab6-dc1f-3378-b280-d103f90b7390 | -20.35113 | -41.84378 | 2024-10-09 04:42:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0305c236-3d11-314c-ac81-acac2ae4564e | -20.35078 | -41.8474 | 2024-10-09 04:42:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 40128874-6ea0-333b-947f-d4be693fbfc7 | -20.34542 | -41.84263 | 2024-10-09 04:42:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 979aef64-80b2-30b9-bb57-9de7ebb5ac53 | -20.34505 | -41.84642 | 2024-10-09 04:42:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2f2de393-eed6-3ca7-8f1f-09c9b7198a34 | -20.23074 | -42.89355 | 2024-10-09 04:42:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83db2b13-6704-399c-b640-7ee7171e03f3 | -20.23035 | -42.89733 | 2024-10-09 04:42:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b0abb775-d8ee-3fc5-a75f-c5524d95c82a | -20.22538 | -42.8926 | 2024-10-09 04:42:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e85ff0b4-bb66-3db8-8749-ef6df991c53f | -20.22499 | -42.8965 | 2024-10-09 04:42:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 67c9ca10-f9fe-3e6d-bbfb-8f8fdcae6cc5 | -20.22461 | -42.90032 | 2024-10-09 04:42:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 754297d0-909b-3c86-9ca7-557579982abd | -20.16302 | -44.40263 | 2024-10-09 04:42:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b85272b5-c363-339f-a61e-64df5cee0210 | -20.16241 | -44.40823 | 2024-10-09 04:42:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53b5dbc2-c63d-3eb9-a76f-d5fdfbfd0436 | -20.15362 | -43.8323 | 2024-10-09 04:42:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 39caed98-407a-373e-80c4-adb6f68c6208 | -20.1485 | -43.83228 | 2024-10-09 04:42:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1584d2c5-3b5d-398a-9489-2fc1c79b3166 | -20.14783 | -43.83848 | 2024-10-09 04:42:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b415a2bc-31af-342f-9994-bcceff66a877 | -23.77869 | -46.70829 | 2024-10-09 04:42:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8052dff0-c5b6-3602-9c6a-9a051bf91ddf | -23.46147 | -47.34066 | 2024-10-09 04:42:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbbabb02-0856-3971-b919-e3bc9dcd5f61 | -23.40556 | -46.55676 | 2024-10-09 04:42:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd701449-9230-34fc-ab6f-caa27d653f41 | -23.33589 | -46.77324 | 2024-10-09 04:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 308059d8-7595-32ac-97af-bcd66cd4b3bc | -23.05109 | -46.26659 | 2024-10-09 04:42:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| efa63a30-25cf-3f03-bca4-843404671d0c | -22.79063 | -46.76071 | 2024-10-09 04:42:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2f7cdaf-d4fb-37be-b12b-f0bb8327cec3 | -22.77606 | -46.99635 | 2024-10-09 04:42:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8743e345-8297-37ef-a0a4-204b1f39c383 | -22.75329 | -47.00595 | 2024-10-09 04:42:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 56bf58f6-7e1b-3eed-b033-b848eabf5b7a | -22.74903 | -47.00541 | 2024-10-09 04:42:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b4099277-e82a-3f68-b613-d2e82560f76c | -22.57984 | -46.69945 | 2024-10-09 04:42:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d04a60d0-772a-3bf6-a6c7-07158ee7e997 | -22.57938 | -46.70337 | 2024-10-09 04:42:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7baa85f0-48b3-3b13-ae53-d97d47d464f3 | -22.57918 | -46.66709 | 2024-10-09 04:42:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28b4dcda-88b4-3b77-b69c-b7f373973bcf | -22.57524 | -46.58611 | 2024-10-09 04:42:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 45b61e29-5dc1-349e-b261-894889df07c1 | -22.57486 | -46.66633 | 2024-10-09 04:42:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36b52634-f448-37db-9f36-17ad9cece43e | -22.57441 | -46.67027 | 2024-10-09 04:42:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e79e1233-30fb-3cc1-8418-b65a72857bca | -21.88752 | -46.7184 | 2024-10-09 04:42:00 | NPP-375D | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cecdb3ce-f831-31f0-b417-cfe57c1c833f | -21.80858 | -47.40767 | 2024-10-09 04:42:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94b1ac16-de8b-36ea-9883-86505397bd87 | -21.80602 | -47.40864 | 2024-10-09 04:42:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ccda03f1-5daf-3cd0-ba6b-9337c2071f58 | -21.79757 | -47.37627 | 2024-10-09 04:42:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7ea032ac-d608-37f2-aadd-19719171f45c | -21.79709 | -47.38012 | 2024-10-09 04:42:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 19fbcc95-76f5-38d3-a193-4fdc809e574c | -21.60387 | -46.61003 | 2024-10-09 04:42:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 947ca590-0104-3f15-8fec-02609f3e580d | -21.30066 | -46.12388 | 2024-10-09 04:42:00 | NPP-375D | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 163c82c8-e500-3610-8bcd-3607ad9a760d | -21.29915 | -47.21327 | 2024-10-09 04:42:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 80b320e4-fd88-3a90-9fce-3902b532c93f | -21.29753 | -47.2128 | 2024-10-09 04:42:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cce68591-b433-3bf8-adb5-3c163d5868be | -21.29502 | -47.21278 | 2024-10-09 04:42:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72b06bc4-251b-3f0b-9924-0bfcf47ba11a | -21.29089 | -47.21231 | 2024-10-09 04:42:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| af31f932-b381-3b19-ac00-517622aec0a9 | -21.01035 | -46.09679 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c89d59bf-9d8a-3eb2-b283-6d34f7891e52 | -21.00965 | -46.09867 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8dca2ff-1d26-328c-950e-2b35efe8639c | -21.00645 | -46.09196 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 579ec022-c1ba-3365-82b5-5a58f34ca128 | -21.00589 | -46.09664 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3d5f08b4-07b1-3b06-99f3-f85594b80823 | -21.00573 | -46.09392 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3ded0198-2ecb-3009-99d8-1b40eb7310c1 | -21.0052 | -46.09855 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8997893b-8660-3be4-a4dc-b5f7d7f975e9 | -21.00125 | -46.09392 | 2024-10-09 04:42:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e3689d54-14d9-3139-8cba-e388be3a3e90 | -20.92192 | -46.46121 | 2024-10-09 04:42:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 04b4202c-b745-391f-8d08-adcddde3eda5 | -20.9214 | -46.46545 | 2024-10-09 04:42:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| bca85295-eb01-3bbe-91aa-8688745ced6a | -20.91713 | -46.46463 | 2024-10-09 04:42:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 50599784-f569-33c1-aaa4-18e3064044a3 | -22.29024 | -50.00008 | 2024-10-09 04:42:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 560d61f5-840a-3506-a5a1-5ae8fea300f7 | -21.82903 | -49.1613 | 2024-10-09 04:42:00 | NPP-375D | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93ddcbaf-a3a3-3c23-83b7-57eea40606bc | -21.28271 | -51.0409 | 2024-10-09 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ad3d4fd9-5c67-3e79-bb01-60c88cb7dda4 | -20.8657 | -50.9631 | 2024-10-09 04:42:00 | NPP-375D | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9c5eca4-573c-3631-9c90-1aa2aef2c11b | -20.54716 | -50.11406 | 2024-10-09 04:42:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 57331425-90ce-3281-8e81-26365d8aacc5 | -20.54658 | -50.11813 | 2024-10-09 04:42:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5a9f6baf-3d6d-3437-8f8c-6eb5645e47ab | -20.44969 | -48.83511 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a8b257c4-9ecf-3e20-b3ef-060244c311ca | -20.44908 | -48.83975 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README157.md)
