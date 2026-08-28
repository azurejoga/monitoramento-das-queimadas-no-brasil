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
| 2fdeb67d-3c01-3ff3-a25b-fa8e3015c2dc | -10.77938 | -50.63379 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c323e75b-7c46-32fc-8875-75675d68bf86 | -11.81689 | -47.21429 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a6ef3731-a1c1-3ba2-ada9-689b580f5984 | -8.77467 | -49.95437 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2079e19c-08a8-3631-b941-374175c357b4 | -10.79183 | -54.00029 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f66b554-00aa-34cc-8bfd-85806d62ff65 | -12.43075 | -42.88953 | 2026-08-28 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a944f0ac-798b-3d20-8d2c-671993ede2d9 | -13.84014 | -54.04174 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0148044-7053-3659-a2d1-a98fda73249a | -11.56712 | -45.50285 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7023aabc-46c2-399a-a962-a80a85ff93c5 | -11.57045 | -45.50343 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0b08e0d-6d3d-399e-a437-b5b142283c69 | -13.40313 | -51.41488 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e36fb78c-5acb-3550-a001-7af20b41aae1 | -11.79937 | -47.66968 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcd5f1e1-3bfb-362d-9cdb-d1468efe5c96 | -10.79534 | -50.64554 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00a0ba46-8b8a-3431-8e5d-ab3a2f4b9b6e | -12.25312 | -50.57825 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 29a117ad-7895-38d5-928a-fa83ef3d9014 | -11.27894 | -54.01768 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| deb2be13-be4f-379a-bed6-24a462899a1a | -10.78376 | -50.63457 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ba4c189-7af8-3218-b44a-60e2c6ef3ba0 | -14.17388 | -52.82048 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d502380a-0c61-3de5-a998-db3a2eecc92a | -13.58401 | -45.78438 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228744ca-bc94-322d-b469-0b0a4632cb5b | -14.39908 | -50.12739 | 2026-08-28 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49322e92-53b0-32c2-8eab-84adfecbb6e3 | -12.76215 | -44.2628 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d8b992b5-d2f5-3d89-b9e6-edbfc8681e5e | -10.48631 | -46.18918 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b0fcb7-e29a-37be-9e35-4a32b5289881 | -15.52738 | -41.92897 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 818b8415-1f49-3f01-89cc-2f7588863bfc | -8.94988 | -50.17035 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 50f5c526-f12a-3300-ba3c-d307fc1cd5d5 | -15.79287 | -43.30846 | 2026-08-28 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6541654d-48af-30b0-b152-1574bfa8f3a2 | -9.88577 | -49.71595 | 2026-08-28 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e919af6-cbbe-3013-a638-d2622b52df32 | -8.80662 | -50.08114 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d96c4f21-7b3b-31fd-b601-ca1e7a86d33e | -15.62236 | -45.93059 | 2026-08-28 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0ae5d13-ac68-3c19-8290-12354cda91db | -11.61989 | -54.5849 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9c13d59-5631-3976-82be-ada0b2f538cb | -10.17667 | -48.4702 | 2026-08-28 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 255a5cbf-69d8-3c31-8669-af8c327a8a80 | -10.76305 | -54.03253 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 805aace2-302e-3687-a1e6-1ea0c50ecad5 | -10.90299 | -50.5271 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 551b92d3-7065-39c1-b579-f3de632ec699 | -10.84086 | -50.51708 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ad7a9b-fbbf-3cc0-ae21-2b1764512d71 | -13.28294 | -46.64157 | 2026-08-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c412e229-a178-3d30-a749-42bfbfd54269 | -11.72555 | -54.53813 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 123e4099-4ee6-3064-8e1f-848346bfcee7 | -14.32905 | -51.70772 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 96fcf147-9569-3ffc-a6e0-12d4e347a6e0 | -13.58573 | -45.77362 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f062415b-bec8-3d7b-8b60-f4b7ff80341c | -12.20631 | -50.56975 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea7feb3f-4efd-38c8-95f5-0349850dad86 | -12.21971 | -43.14666 | 2026-08-28 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 518f98df-5bb9-3238-93f3-f545938c82bd | -14.11546 | -44.38908 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dc09ec6-3144-3156-b31a-b0ba545a892e | -13.4813 | -48.16631 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ed5f510-a652-3998-b760-66042c0c8ace | -8.60202 | -54.78168 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ddd19e-bb65-38f1-87d3-a566635018fe | -8.58922 | -54.78408 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 65213bfb-2fcd-38d5-833f-a0736610e4c9 | -13.42177 | -46.73864 | 2026-08-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d61198b-5589-3359-aa04-a26be7b0b7a8 | -11.21854 | -54.00235 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109405b7-d234-37d1-a1c8-03013081b5ef | -11.20563 | -51.24579 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c67a2646-686e-36d8-8a5c-e19414e52da3 | -10.06199 | -46.93739 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ad50fc0-0a21-3600-b46f-e0e4df457893 | -8.80281 | -50.49548 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a25cedf6-5c4c-305d-96a2-ad192d1bc5ab | -11.46874 | -46.94854 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06033794-d9be-31f6-9650-38e3b0b10481 | -11.48937 | -45.07361 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00eb812e-bfcc-32c4-9473-51fe9553d085 | -13.59906 | -45.77581 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c8232df9-6230-32ad-a466-c6f8fa612a8c | -9.15824 | -49.96735 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d6c511b-dc61-3ae3-bc35-3294f63f493b | -15.15009 | -43.79462 | 2026-08-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d7c991d-0a85-3fb2-ac3e-a0263febed9e | -11.79796 | -47.67815 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d472ab-1e39-3403-86bc-691184063355 | -11.56988 | -45.50699 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2c1382d-b93a-367e-94e5-6e27c55ed741 | -14.09829 | -41.66039 | 2026-08-28 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 994e59c7-b3ef-34c9-ad03-e5faed078faa | -9.79293 | -43.55124 | 2026-08-28 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 236ec682-0248-3750-b56c-c6d13ac4f4f9 | -16.05037 | -47.23293 | 2026-08-28 04:17:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa91e8b1-bbd1-3a81-a90d-4e9eec6b63ec | -13.41113 | -51.42095 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6289e2cd-44c5-32ee-83c2-01c6c4577688 | -10.17886 | -48.46805 | 2026-08-28 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 165ec996-7af0-31bf-8625-b798f4155472 | -11.8317 | -47.21254 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83666436-b87d-3dc6-9798-099783e8f4d8 | -14.60209 | -47.97792 | 2026-08-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bef7e0c9-c8f4-3058-b30f-ecd2ca0dd993 | -11.21442 | -53.99432 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 626ffa38-5215-35a7-93d7-48b4e90648f9 | -11.01661 | -45.07301 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a12ec925-7195-3a77-b286-8b6dfbcf64e1 | -10.93694 | -50.53752 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c96f673d-3489-3969-87bf-d9c2981ccd23 | -15.53717 | -42.36432 | 2026-08-28 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a2f9134-4645-38ae-82ac-1dfa5f6b71fb | -11.57589 | -45.53371 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c5c76a-8cfd-32a8-9108-3bbffe86bcdc | -8.5959 | -54.79477 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33ba2e06-f908-3432-87cf-55d6ac6be293 | -9.21377 | -51.55099 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf3b8e7c-1194-3a84-9e42-f355f9a57dbc | -9.16465 | -49.96852 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68c4b72d-1014-36d3-bb05-1e2bc97162cf | -11.29247 | -54.03528 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a1298b77-d260-3e62-8463-092c48e1483e | -12.21057 | -50.57051 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0836998f-da21-3122-828f-a0e6af725c96 | -12.4206 | -42.88766 | 2026-08-28 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eac50e0d-9dce-3a2c-bfe6-c3049c56b1bd | -13.41912 | -51.79166 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4935085-e587-3462-a47a-f75f738257f9 | -11.19287 | -51.23866 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3baaa752-9e21-32a3-8523-fc23f0a3145c | -10.89802 | -50.52296 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3abe0c17-9210-3c08-8b1d-486197124468 | -10.32366 | -49.97309 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 429d02d9-bf02-33e4-81a2-efa8e652c637 | -13.41275 | -51.41213 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| db0f8bf8-6094-3261-bde1-324c67b54c5b | -20.42921 | -47.53032 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58f08da7-5c5d-3904-96da-e95dd7138e5a | -11.49269 | -45.07417 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f5d9b0b-2f95-38df-933f-19f43435e325 | -11.18999 | -51.22855 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4c7d7a09-995d-3552-b332-be04796add15 | -9.6614 | -48.29801 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20edf1b5-2af3-3415-bfdd-eec5fc340c1d | -16.61718 | -43.41822 | 2026-08-28 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 531cc91a-634d-3d1a-904e-017ee13b60a5 | -14.89472 | -52.59941 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4b335792-3241-338e-8abb-31ad6be9312a | -11.20899 | -53.99329 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bef1b315-a74c-37be-bf07-7b3a4b5b2c22 | -11.72775 | -54.52684 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04c98889-e30b-3c5e-92bd-13c7cc74de77 | -10.55221 | -50.48173 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63d14343-1238-30c0-b032-d16bc33fb600 | -12.50529 | -43.81113 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 96de2c83-bf4c-3c07-82b8-b3da5c3afd20 | -14.11878 | -44.38961 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7beaac2-adcf-3f20-9e33-4912a7371a6a | -11.16168 | -51.20411 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da9f28cb-853e-33ba-a73c-7ba32950d298 | -9.34112 | -48.16733 | 2026-08-28 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab8f9fda-60c6-39a4-8815-4948d77e7dc7 | -12.76492 | -44.26686 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d458f6ef-a03c-3dbe-8c1f-c8c45e9bc9c4 | -14.42768 | -52.60003 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e53c048-b327-34a4-93dc-0983bf63d3b1 | -22.25525 | -47.51695 | 2026-08-28 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a65803e-8a19-3d1e-af35-a7aa78948f03 | -8.78117 | -49.94261 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48502e34-6424-3060-826a-2103c89dd46c | -9.22437 | -51.54697 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 410543bd-c88e-33c0-a821-31ce7903cc82 | -8.95497 | -50.16699 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d5ec4163-281a-368d-a1a1-51ba7a33d870 | -13.42332 | -51.86968 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 048934d7-e2ee-3b23-a431-2843e4d5a97a | -14.93263 | -52.60244 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 76a4b6c8-e30e-3644-ad65-fcd233fdd613 | -12.24887 | -50.57747 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 5f450df8-9e5f-365e-b23f-f33c1e054835 | -8.672 | -49.54218 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0889a971-825d-3f53-9b2c-ca48f9c1536c | -11.57312 | -45.52958 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8ae09a3-ab48-393b-8b30-1de99816d40a | -12.26869 | -50.58949 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README21.md)
