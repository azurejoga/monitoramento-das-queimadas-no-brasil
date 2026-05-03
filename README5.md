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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6c74dc4-97c3-35ec-9259-76481f54e60d | -17.94806 | -52.98497 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d26c81cb-483e-3a05-9e33-6e28a129b14e | -21.57402 | -48.36278 | 2026-05-03 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1bc5434-f616-35d0-b50f-3ff0169e4886 | -17.94869 | -52.98189 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db947e70-0cd3-3e4e-acb6-877342bbe67b | -18.25268 | -49.30824 | 2026-05-03 04:12:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9901fd7c-07c6-3a90-bd6b-edf71600b054 | -21.07057 | -43.88268 | 2026-05-03 04:12:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68960608-4022-3901-a052-9ccdae6af8a7 | -20.19317 | -46.46246 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbf35a94-d570-3f98-8e99-e6291179f79d | -17.95631 | -52.97044 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f07708-f612-3147-a4df-41e98b591f1a | -20.18637 | -46.46127 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25c3c6bb-b359-333c-8202-85e880c394b5 | -20.18977 | -46.46185 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0220a846-9996-3b62-aba8-9bd143f0fc74 | -18.05409 | -52.94818 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1f58a37-c5a6-36c5-8895-992dabeb3361 | -16.3734 | -52.63848 | 2026-05-03 04:12:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c08e6dc9-f11e-31ea-aa56-70f118c12556 | -21.07674 | -46.56746 | 2026-05-03 04:12:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5d7c7a28-6089-3538-9cb3-07bda3df186a | -16.47822 | -49.21218 | 2026-05-03 04:12:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 942f8eff-4e69-33ba-b39a-be872f30b625 | -17.94239 | -52.98688 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4479ef4-9cd0-3c5a-8737-0387405d87b6 | -20.19657 | -46.46305 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13a41006-ba44-3d17-82f5-cb15f8813129 | -22.61539 | -47.41579 | 2026-05-03 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2dd2c5c7-0c4d-343e-aada-cc37d6b0cb36 | -21.06724 | -43.88211 | 2026-05-03 04:12:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da2c6641-71b6-31cb-9f4f-942b9990888a | -17.94302 | -52.98382 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5586bbe0-4a89-39dc-b74e-dc745d71b5dc | -17.96263 | -52.96527 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b71114db-5fbf-30b6-a9a8-b07814051102 | -17.95695 | -52.9673 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f613ff23-169e-3079-be6a-1b3fa3e9b69d | -18.25488 | -51.25945 | 2026-05-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 175f9286-d2df-39d0-b004-5b290b1b272e | -16.37843 | -52.63981 | 2026-05-03 04:12:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1894c03c-4914-377e-9001-5c49de6a713c | -18.25571 | -51.26322 | 2026-05-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 747968fa-374e-3c4f-9c25-9a7256827054 | -17.21245 | -46.87723 | 2026-05-03 04:12:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f94b6b6-b018-36c6-a057-c08d987fd56d | -20.18744 | -46.43376 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbb0632c-561c-31fd-94ee-f22c69f7b958 | -20.01772 | -41.61728 | 2026-05-03 04:12:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6cb95b30-30c0-3a0e-87e2-9cade0b2ffe1 | -17.9531 | -52.98607 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9b2434b4-7193-3193-999c-b89ef69c2f81 | -18.05974 | -52.94623 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a284ebe-9d7a-3455-bbe8-f0d6d38f4f72 | -20.62696 | -51.71041 | 2026-05-03 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a60d053-312a-3888-abd4-535e35412ad2 | -18.05912 | -52.94927 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d24bc315-e22e-3dc9-968c-22e614826750 | -21.10421 | -46.84276 | 2026-05-03 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14f21625-a706-3515-adcd-054bfad7bd3e | -20.18144 | -46.4488 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b838007c-9bb4-3e06-b7a6-efb32bb7c213 | -17.95688 | -52.99339 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7834724c-a348-3041-ab33-8d4df4d084e4 | -19.03265 | -40.53159 | 2026-05-03 04:12:00 | NOAA-21 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ac038f5-3fa9-3ab6-9fcc-145db63a935f | -17.95119 | -52.9954 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9638925d-91a8-3cad-92c5-ba0217bf7ecd | -22.40715 | -41.92439 | 2026-05-03 04:12:00 | NOAA-21 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38d7a77a-ba39-3116-96cc-32ac9b35e099 | -18.25771 | -47.01746 | 2026-05-03 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4388e188-9285-3107-8ee9-7f33c50278cb | -20.22695 | -50.91436 | 2026-05-03 04:12:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| daa1f414-0257-3451-895b-36af77baa212 | -13.1992 | -54.5408 | 2026-05-03 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 335bc47b-0995-31f8-830e-9ef1a636b057 | -13.2183 | -54.5388 | 2026-05-03 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e8928853-031a-3e3c-bd78-235fd5a7d97a | -12.3508 | -50.0266 | 2026-05-03 04:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f1b5afc3-5024-3231-9e6b-f72e56007f49 | -13.2183 | -54.5388 | 2026-05-03 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9b04baf4-aff4-32cb-9453-506cec1e1c87 | -12.3508 | -50.0266 | 2026-05-03 04:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f31b7fa0-3460-3506-b4d2-6d50724575a6 | -13.1992 | -54.5408 | 2026-05-03 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| b65559ef-f71d-3442-9921-27155f1587ba | -12.37 | -50.0242 | 2026-05-03 04:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 31f2b5ce-9a0e-3d09-bee2-25d01433fc36 | -12.3508 | -50.0266 | 2026-05-03 04:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 90ef6231-e2cd-3617-aae5-ffd312345b98 | -13.1992 | -54.5408 | 2026-05-03 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| e1745d5c-728c-3feb-b15e-31730cb27bdb | -13.2183 | -54.5388 | 2026-05-03 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 26bf90f5-fdbd-3425-8ebb-91e5bc20be3f | -12.28268 | -44.62862 | 2026-05-03 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb6aeaec-6bb8-312d-ab6f-02f63b25540f | -13.68452 | -44.29321 | 2026-05-03 04:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7195b167-480c-3e1e-8b06-630665921d0b | -10.98074 | -45.08781 | 2026-05-03 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e41a556-d951-31db-835f-2636bc6f433c | -11.88119 | -43.80299 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c779697-d959-38b3-97cf-d7e346f342a3 | -12.35502 | -50.03048 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d13d528e-134b-37e8-bcd7-12bb96ac7a15 | -12.35893 | -50.02747 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 250ce78e-4498-32f2-a79c-8967fd718756 | -11.88896 | -43.80798 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73304c2b-c11c-3c45-b4a3-47344ed02426 | -12.35836 | -50.03104 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 369bf66e-9fa4-3297-871a-abd84ae0b7f8 | -11.3007 | -54.72888 | 2026-05-03 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac66fae-2c05-3e0a-97d2-ec3f18cf6d36 | -11.35924 | -47.03559 | 2026-05-03 04:42:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 333b325e-73d2-3c67-a98b-847acdb159ec | -9.67562 | -43.79509 | 2026-05-03 04:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7998db5-7b93-3851-8968-dd577e7f44bb | -9.67512 | -43.79566 | 2026-05-03 04:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d3629a3-d3b0-3690-b8f1-fa1311e533a9 | -10.57662 | -44.32845 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 51021551-f385-3cd2-94b1-c61714a36ded | -12.35445 | -50.03405 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f0cb8891-a8ca-3c8b-a62d-38f525db55d3 | -10.98143 | -45.08315 | 2026-05-03 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb5f8eb2-f9d9-3fff-a665-b800fe5f7da3 | -12.46476 | -44.29741 | 2026-05-03 04:42:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 777553ca-07c2-3556-bd05-0f2a2b6cf61b | -11.95759 | -43.96683 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b351923d-d336-3ccd-bc46-e8edb0beb180 | -12.28196 | -44.63376 | 2026-05-03 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fa124cc-0489-3d45-83ab-8022845d1a11 | -11.6441 | -52.56658 | 2026-05-03 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d15cd2d-ad43-3520-a116-d967eb851934 | -10.58845 | -44.33017 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4180b10d-5952-36c4-babf-2d07ce2a343a | -12.37667 | -50.04506 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f9f9ed-4897-37c9-ac7e-8e4cadd23550 | -11.84185 | -43.96532 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e712ddb2-f504-33ee-af39-e8355ae0aaf9 | -11.88482 | -43.80738 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90ff901c-621f-3854-9b5d-78de231320e0 | -12.38067 | -50.02013 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd8f1a67-384e-3091-9b1a-c0e0aebdc776 | -11.64482 | -52.56228 | 2026-05-03 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1224491-99f9-35d4-bdc8-0f1a24371d99 | -13.24271 | -44.46518 | 2026-05-03 04:42:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5050d100-0868-38ce-923f-c85f085df439 | -10.97696 | -45.0872 | 2026-05-03 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea757e72-5163-359c-ab7d-d4aa52f553e4 | -10.58056 | -44.32903 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| dbfaa44c-3d9a-39c7-9851-317ba88afa41 | -11.63753 | -52.56098 | 2026-05-03 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cb8f6ca-a3a4-3381-b11a-454532d42cdb | -12.3617 | -50.03159 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 18a6d30c-e46d-3f13-af4d-0b5c9a5f2ca5 | -10.58522 | -44.32456 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ec712acf-5369-3537-a374-e8ef91416297 | -10.58451 | -44.3296 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f658eaa6-8b4f-3ee8-afe6-ca7f46117232 | -10.98452 | -45.08841 | 2026-05-03 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a36a0d4d-830e-3992-b6a7-76fdda636159 | -9.56894 | -50.68365 | 2026-05-03 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b14d21b-3f31-3962-85dd-257caf427551 | -12.278 | -44.63323 | 2026-05-03 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94b8d0ed-6422-33b3-9878-368575bf2d8f | -12.374 | -50.01902 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18d488a2-8623-3931-bad4-75878de94fa1 | -12.38058 | -50.04205 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 928db16e-c79c-3e01-80fd-eaacd2b66e87 | -10.57762 | -44.32692 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d307ffe-f7cc-3337-8584-af22001da80b | -12.36227 | -50.02803 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 405ff877-ba15-36d7-8b75-5d4b0676609a | -10.97765 | -45.08255 | 2026-05-03 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a575900f-eace-391c-a9b6-4c8c9c093218 | -9.57238 | -50.68422 | 2026-05-03 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2878000-68cc-3db8-869c-d3c684e073e9 | -12.27872 | -44.62808 | 2026-05-03 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3b82331-a57e-3847-894e-f8b40bc58326 | -11.30487 | -54.7296 | 2026-05-03 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15da3e1d-3148-3eb6-bfc9-feafe5c3738e | -11.64045 | -52.56594 | 2026-05-03 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf9969e0-e6d9-3154-ab6b-a321b5743fc9 | -10.59239 | -44.33075 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df3e6abf-f63d-3ec6-a974-1b973c1539e1 | -12.23071 | -54.37905 | 2026-05-03 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c235625d-0db5-3751-a06a-7601d4afcc59 | -10.6385 | -48.00903 | 2026-05-03 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 697b398a-e3ce-3045-af55-edfc5c90e971 | -9.56956 | -50.67987 | 2026-05-03 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec64f26a-f538-3b14-b826-eb8f6d72b144 | -10.57368 | -44.32634 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cd0e785-2fb9-32e1-b51e-99d1ad0accd1 | -10.58127 | -44.32398 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c6ef2cfe-a8b8-3fdc-a766-9ae53af643d6 | -12.46022 | -44.30034 | 2026-05-03 04:42:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55ce7bc0-2b0f-3591-a24d-54a9e571fa22 | -11.55438 | -48.26992 | 2026-05-03 04:42:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
