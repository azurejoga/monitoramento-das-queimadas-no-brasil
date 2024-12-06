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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f70b27-4117-3da9-a9a6-9a00636e5ed6 | -5.58464 | -35.55545 | 2024-12-06 03:10:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be473005-5d13-322f-8774-fef2bd0552c2 | -8.33719 | -36.83358 | 2024-12-06 03:10:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd3818f9-fb13-3540-96d4-1aef0e295ed3 | -6.14087 | -35.32448 | 2024-12-06 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4d58e833-4b29-3fac-960c-d1fbc9110cc6 | -8.34246 | -36.83482 | 2024-12-06 03:10:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2bd73d9-63a9-31ef-99be-91ff07f5242a | -6.13589 | -35.32354 | 2024-12-06 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d1dd867d-f36b-3b10-aab4-16e2a0d778af | -6.14183 | -35.31896 | 2024-12-06 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 85af5e44-c979-3705-a40a-77d6d6ab0cd3 | -6.13686 | -35.31797 | 2024-12-06 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 12a48250-3353-340f-9dc9-63eeb3b33146 | -5.58516 | -35.55246 | 2024-12-06 03:10:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c24fd89a-d7e3-312f-b97d-541573a4bb2b | -10.28415 | -36.31464 | 2024-12-06 03:12:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f50ccd15-4a99-351c-8b30-2d6c8fa2b1fc | -19.59175 | -40.45157 | 2024-12-06 03:14:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77f09319-7368-3e92-960a-bd1ad887a8d8 | -19.591 | -40.45504 | 2024-12-06 03:14:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7172932d-61df-3ead-912e-97aec24ebf08 | -3.88732 | -42.5563 | 2024-12-06 03:32:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 443e5f5d-07e2-32d6-9e96-707a6f36c517 | -3.88764 | -42.55317 | 2024-12-06 03:32:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3b581695-7a82-3ad7-94c2-4fedef5f5847 | -3.88793 | -42.5526 | 2024-12-06 03:32:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7192a2ed-a49d-370f-acae-b6166a84a690 | -6.45565 | -46.34996 | 2024-12-06 03:34:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bb39c66-f714-3224-89ae-648d05464d41 | -9.48357 | -35.78643 | 2024-12-06 03:34:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b295010-b509-3bd5-bbd1-22fe6ec83356 | -12.35349 | -38.14236 | 2024-12-06 03:34:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5357c94-f0b3-3b79-8b19-c4b11030287f | -10.24325 | -37.59648 | 2024-12-06 03:34:00 | NOAA-20 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1973781-41b1-374d-b667-7f0e1308f394 | -7.87735 | -40.54966 | 2024-12-06 03:34:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18b38bdb-99e6-3b94-a641-fc34f864866b | -6.93331 | -42.83426 | 2024-12-06 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a27bb2de-811c-3f14-819d-589401ffe039 | -12.53695 | -38.60509 | 2024-12-06 03:34:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c9e496b4-36ba-3421-af1a-e64641280728 | -10.33611 | -36.74936 | 2024-12-06 03:34:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c488adcb-ddc1-374f-857a-d646352112fd | -9.83508 | -37.08061 | 2024-12-06 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cea00f19-456b-3383-8847-105f1a359a58 | -10.21857 | -42.187 | 2024-12-06 03:34:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e16ee1b9-3bd8-327d-8302-7ede0ee0cd39 | -6.7844 | -40.22846 | 2024-12-06 03:34:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 000a3fc0-e0a6-3388-85d3-7043ddaebb04 | -7.88638 | -38.53384 | 2024-12-06 03:34:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 82f20843-42ff-37c5-85c6-507cdd9455ea | -10.49517 | -36.70341 | 2024-12-06 03:34:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06775eae-8708-39fb-8f67-648dd4077f5a | -9.83863 | -37.08121 | 2024-12-06 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d9d4fd02-2956-3ea5-8173-89199d94d9e0 | -11.87612 | -38.34957 | 2024-12-06 03:34:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a7c2024b-6bc0-38e0-978b-eb11cef12a35 | -8.89543 | -35.41134 | 2024-12-06 03:34:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6678d50d-ac1c-36b9-bad8-a26f7c8f6800 | -6.78275 | -40.22686 | 2024-12-06 03:34:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3286b178-3707-3173-a3ef-d57c4d495f14 | -10.47902 | -36.78031 | 2024-12-06 03:34:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34a68c99-e9a9-3e80-8e53-51fb78237534 | -10.28849 | -36.3132 | 2024-12-06 03:34:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6326de65-98a1-3037-b312-f4fda5eb2e62 | -6.7872 | -40.22794 | 2024-12-06 03:34:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c26a591-e7b4-3b5a-a6d0-88c46018b8c9 | -10.28507 | -36.31263 | 2024-12-06 03:34:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9ee176df-7209-3328-87b5-5d4f75f07330 | -9.98124 | -36.52163 | 2024-12-06 03:34:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8c76e9bc-0003-3f30-bb15-b9fab87f56b3 | -6.92798 | -42.83324 | 2024-12-06 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dad8255e-9139-3d86-b3a1-47fbe421f75c | -9.47329 | -36.6179 | 2024-12-06 03:34:00 | NOAA-20 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83da15bd-429d-3734-b6d1-2a9ab6ff8106 | -11.88323 | -40.95855 | 2024-12-06 03:34:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29dad70d-62db-3e85-bb61-35b1664632e8 | -11.10339 | -42.0302 | 2024-12-06 03:34:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5de88228-551c-3b6a-9325-ac396bfae976 | -6.92737 | -42.83667 | 2024-12-06 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe8a46cc-18d2-3d53-bfea-50b964bb0b6f | -11.87442 | -38.35106 | 2024-12-06 03:34:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 302e5790-540c-31ca-a474-8d95114e7692 | -6.75776 | -39.25564 | 2024-12-06 03:34:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7a67942-ba80-3c46-b973-d6bce7b25b81 | -7.90758 | -35.20103 | 2024-12-06 03:34:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b5ce9374-949e-332e-b066-3e43f26221bf | -10.21669 | -42.18896 | 2024-12-06 03:34:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a95ef564-225d-3bf2-9f00-a868b1ff4b17 | -4.54418 | -43.3045 | 2024-12-06 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ad7e51e-8767-3861-a44c-fbd14499288e | -8.33869 | -36.83412 | 2024-12-06 03:34:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46d18f94-3432-35fb-a45c-b5cf1cb33bb8 | -9.3566 | -36.00501 | 2024-12-06 03:34:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c386a19b-afc3-3b26-8e84-c541dbfcb7e7 | -7.42527 | -39.89519 | 2024-12-06 03:34:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 345bcb36-3189-3aea-a04f-88edc8efe5a6 | -12.35282 | -38.14397 | 2024-12-06 03:34:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e05dc8c-1657-3792-be53-3504a6347d93 | -7.83995 | -38.47327 | 2024-12-06 03:34:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7d23dacb-f30c-3b30-bcb1-9d5128127f89 | -12.35353 | -38.13968 | 2024-12-06 03:34:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25e831c4-8c30-3583-b2c5-7a905e5d38d7 | -10.49581 | -36.69954 | 2024-12-06 03:34:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ee61e61-2e64-3238-b6d0-931bebb8a805 | -12.53247 | -38.60896 | 2024-12-06 03:34:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7285ba78-3181-3fdb-b748-3e73ed0615a6 | -13.22429 | -43.97934 | 2024-12-06 03:36:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a659618-fb97-3cd0-9b06-fafb25965c8f | -13.22489 | -43.97618 | 2024-12-06 03:36:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a868525-2392-3d10-9061-49b994bf8c01 | -13.09679 | -43.37367 | 2024-12-06 03:36:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 411d564e-bc46-3e80-b31a-7974a4b152f2 | -16.66554 | -40.95149 | 2024-12-06 03:36:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d7277e47-1332-37db-a141-f76441d3a18a | -13.61462 | -44.0925 | 2024-12-06 03:36:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74102659-3119-38ae-8b4a-8387627eacaf | -17.91298 | -40.10861 | 2024-12-06 03:36:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| daaf7306-a099-3dff-8071-bf0abb31cf40 | -17.91382 | -40.10394 | 2024-12-06 03:36:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| b4b61e18-4e86-39b8-8606-cc59130b63f4 | -17.9101 | -40.10322 | 2024-12-06 03:36:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| da329146-cc9a-3036-89a3-a94ec257a384 | -11.69021 | -45.38943 | 2024-12-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8afac640-0111-35ac-a79e-bda821c7e663 | -16.68117 | -43.88568 | 2024-12-06 03:36:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca77613e-841c-3576-981b-1299c5fc674d | -13.0497 | -41.41615 | 2024-12-06 03:36:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5beb2989-0f7d-346d-a2b2-42a86b42b033 | -15.44617 | -43.65751 | 2024-12-06 03:36:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8abcfb36-c5c5-33a2-909e-784b889942d5 | -16.34734 | -43.69595 | 2024-12-06 03:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3996ccc-d7ac-3042-a1cc-5c7f1e4453c7 | -12.01998 | -43.00749 | 2024-12-06 03:36:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ef496cb-a590-3586-8b4f-7f3bbf21bcba | -13.23003 | -43.97729 | 2024-12-06 03:36:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 045f32ab-f149-3211-b578-59e684596488 | -17.15243 | -40.3147 | 2024-12-06 03:36:00 | NOAA-20 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 85ee9778-7f3d-3217-b61d-e74614061b89 | -13.61978 | -44.09356 | 2024-12-06 03:36:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8e5800e-a9e3-3ca9-81cd-4a896326853d | -13.61915 | -44.09679 | 2024-12-06 03:36:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d739172-b808-3e26-8963-e001f13efb2a | -17.15708 | -40.31076 | 2024-12-06 03:36:00 | NOAA-20 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8cce8e38-9089-3b03-9a77-0c84609bba37 | -19.58841 | -40.44984 | 2024-12-06 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f279365a-c946-3ec4-b4ce-f12a76fa7dcf | -20.34873 | -40.36332 | 2024-12-06 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68c0f6b6-15a8-3312-aa8c-ac6e3a2d7db5 | -18.97681 | -42.38847 | 2024-12-06 03:38:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c410f21-1c74-3a7f-a108-73182ecbee0f | -18.97759 | -42.38432 | 2024-12-06 03:38:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b028e44d-2c22-3a42-976e-2e1a223355cc | -19.59187 | -40.86183 | 2024-12-06 03:38:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e586bd2-b729-3547-b86c-4d93736847ea | -19.58759 | -40.45436 | 2024-12-06 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8d54fd0-c5d7-32cf-9e89-bbd06cc5946d | -3.2136 | -46.7843 | 2024-12-06 03:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| be794cf7-94df-394d-a602-82f0c634d801 | -10.2773 | -36.2786 | 2024-12-06 04:10:00 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 68de8f5a-9046-399a-a412-fbf8dc159c23 | -10.2579 | -36.2821 | 2024-12-06 04:10:00 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 155.5 |
| 99e876b8-950f-3e12-8371-f424910aebb0 | -1.65757 | -53.19967 | 2024-12-06 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 67cfc0a1-84a9-3152-8a27-a563de508bf7 | -1.87892 | -53.28956 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 670fe713-27b1-31d9-956d-000c0049bf05 | -1.87841 | -53.30425 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5cb94a9c-307a-3957-ab07-f5b744874af6 | -3.40184 | -42.30044 | 2024-12-06 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edeb6d56-06c1-31bc-aa91-6812a695994f | -1.81604 | -52.73508 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b44eac0b-d85b-329c-b1d5-3151c85276a8 | -1.87925 | -53.29885 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2320b5c-2e25-324b-9c40-fba3a98ef705 | -3.39816 | -42.29988 | 2024-12-06 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc43e8b1-59a1-3a66-b437-5edd8815e132 | -1.87627 | -53.30572 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37bec1ef-016a-33f0-abe9-ee4b625d1e2f | -1.66135 | -52.75467 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42e8ce0b-0fdc-319f-a37a-178882448298 | -1.87716 | -53.30032 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8674fbd5-b7df-3fa9-b50f-7d07e4411389 | -1.6809 | -52.78331 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc80bdb7-5322-39b2-97d1-ea7d8b0b14b7 | -1.68561 | -52.78404 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6281ca-5036-38e6-85cc-b0b93529cc03 | -1.68953 | -52.78979 | 2024-12-06 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aff81b2f-7861-33f7-95c8-17fbc02949b4 | -2.26896 | -53.82592 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 900c568f-28cd-365a-9bbc-2febc9ee97b9 | -2.24503 | -53.84625 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| acaf2e2a-d198-3ddf-a4ee-ca001864e5f7 | -2.38212 | -53.95308 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6841e17-0f8f-33b4-9795-eb0d324eb4cc | -1.8801 | -53.29346 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4566ae4-9164-32b5-8e97-def8ba7dc82c | -2.38258 | -53.95023 | 2024-12-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README3.md)
