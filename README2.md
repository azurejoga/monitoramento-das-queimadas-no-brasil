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
| 98d50753-efc3-3ef1-bafc-959369156451 | -15.3626 | -46.935 | 2025-03-19 01:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 07126e57-a136-3e8d-989c-d9ec49021f17 | -15.3425 | -46.9614 | 2025-03-19 01:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 3276105b-a194-332f-8fc6-916aaafd6ace | -15.343 | -46.9385 | 2025-03-19 01:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c82a3040-e4f1-37e4-b3e4-30e5dfa5cd44 | -15.3626 | -46.935 | 2025-03-19 02:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2c3a189d-1262-3a84-897c-02609c1eb23f | -15.3621 | -46.958 | 2025-03-19 02:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 81c6180e-095d-3fbc-9d2d-32fe38295bbe | -15.3425 | -46.9614 | 2025-03-19 02:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 8bcc95c1-dbf0-33b4-9f27-b393ae94ccca | -15.343 | -46.9385 | 2025-03-19 02:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| cb58a12c-b255-32ca-ae1f-fc9117e51a7e | -15.3621 | -46.958 | 2025-03-19 02:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 3a0e3673-1030-36a0-9bb7-8d5ef3891d53 | -15.3425 | -46.9614 | 2025-03-19 02:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| bdb1c328-da29-31a3-be7c-bbbc28091d79 | -15.343 | -46.9385 | 2025-03-19 02:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 60c61c2a-106f-3735-949b-4049869268a0 | -15.3626 | -46.935 | 2025-03-19 02:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7f428e47-c708-31cf-9cdb-0907f996a501 | -15.3621 | -46.958 | 2025-03-19 02:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.6 |
| af4b6491-b76f-38aa-a943-0c47ae3cc862 | -15.3626 | -46.935 | 2025-03-19 02:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fe097009-9055-3553-8f77-1fbe105999b3 | -15.3425 | -46.9614 | 2025-03-19 02:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 132.1 |
| a4132eac-7913-3e3f-99c2-e6921e556c41 | -15.343 | -46.9385 | 2025-03-19 02:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 66a203bb-5d05-3ecf-91ec-e7d5daadbe3a | -15.343 | -46.9385 | 2025-03-19 02:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 24e2e82c-0cff-357f-bf47-046f12c82040 | -15.3621 | -46.958 | 2025-03-19 02:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2c30f6b1-ea1b-3276-af19-531ce09f6e52 | -15.3626 | -46.935 | 2025-03-19 02:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| efb1e315-03da-387c-b83f-4c975915c240 | -15.3425 | -46.9614 | 2025-03-19 02:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f696449a-5ca1-3576-80d5-3e6d76f6ab94 | -15.3626 | -46.935 | 2025-03-19 02:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 18d08b52-d9bb-3103-8404-2c78719a21fc | -15.343 | -46.9385 | 2025-03-19 02:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 69c3a746-3458-318f-b831-4082a244ed32 | -15.3425 | -46.9614 | 2025-03-19 02:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8e878991-4fa8-3f78-96cd-0107435d55fa | -15.3621 | -46.958 | 2025-03-19 02:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c5f273b0-cd3f-300c-8029-8919edd51550 | -15.3621 | -46.958 | 2025-03-19 02:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7b6408e7-4110-38d8-9616-0b36a23f65d1 | -15.3425 | -46.9614 | 2025-03-19 02:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| afd3ea1d-b5f5-3e58-9939-7c6ce954d2a2 | -15.343 | -46.9385 | 2025-03-19 02:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 3cd61db2-b870-3b9e-8d76-2a5174ce354d | -15.3626 | -46.935 | 2025-03-19 02:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6e9a8ca6-fe0f-34f3-8e8b-d55ec9790b84 | -15.3621 | -46.958 | 2025-03-19 03:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d34788c3-5a29-39e8-a641-ea25e07dc6e3 | -15.343 | -46.9385 | 2025-03-19 03:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7ca6e0a1-35da-3cb6-bb14-14714c6d1ade | -15.3425 | -46.9614 | 2025-03-19 03:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0346250f-a1dd-3234-8195-1e5b670ab356 | -15.79735 | -42.03575 | 2025-03-19 03:04:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 497e1dce-8364-3bcd-8383-54c75285afb7 | -11.84874 | -37.58836 | 2025-03-19 03:04:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ce622f57-0b37-3bc5-81db-3f55238be55b | -15.80025 | -42.03485 | 2025-03-19 03:04:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1e4880f1-82da-3565-bbad-0f51f477a580 | -16.08627 | -40.89233 | 2025-03-19 03:04:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eec98306-f0a4-3c80-b8ae-b471c9b1c379 | -11.84791 | -37.59259 | 2025-03-19 03:04:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1c39e59-efe8-39b4-a617-a5f4604f5696 | -15.3621 | -46.958 | 2025-03-19 03:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 760b8ae4-3c13-3dfd-9350-fe2cd4ebb21d | -15.3425 | -46.9614 | 2025-03-19 03:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d6c6834b-a797-3236-bbaa-f7a25c9107b7 | -15.343 | -46.9385 | 2025-03-19 03:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1cc5d670-aaa5-3c8f-a41e-20f8f829e57f | -15.3621 | -46.958 | 2025-03-19 03:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e4208031-583e-3e3f-9e47-d303f5ea5041 | -15.3425 | -46.9614 | 2025-03-19 03:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ee8c59d4-54dd-3100-b4de-0916fbc43e91 | -15.3425 | -46.9614 | 2025-03-19 03:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1189e306-0932-3202-9e55-6e70f4cd4d97 | -15.3621 | -46.958 | 2025-03-19 03:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2f9b9023-7879-3465-a5fd-f6d33fdde412 | -15.3425 | -46.9614 | 2025-03-19 03:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 44870770-fffc-3097-9f32-5e2a2d9a0a44 | -5.77628 | -44.38327 | 2025-03-19 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bc36aab-39d7-3354-962e-5e428dd9c0ce | -11.96338 | -48.08915 | 2025-03-19 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb9babd2-438f-3452-98ea-2d2c2bb0fc88 | -11.62462 | -37.71384 | 2025-03-19 03:55:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 72bbb717-a848-3acf-afa5-03d2218e71ea | -11.67591 | -39.99591 | 2025-03-19 03:55:00 | NOAA-21 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04dba5c0-7ccd-35c2-884b-97213e5028a9 | -10.34751 | -38.4824 | 2025-03-19 03:55:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c8cd14c9-b2dd-362a-95a3-2c5fd10d7699 | -7.24681 | -44.78006 | 2025-03-19 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5347958f-7d34-3617-9a3a-df2f2a4318fd | -11.57996 | -47.62972 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a63b1019-7b35-3b93-b1b6-53a16c210c0c | -13.54403 | -45.44712 | 2025-03-19 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59f9294a-0465-3e6b-ae6a-05292de21c4c | -12.08907 | -45.64015 | 2025-03-19 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3fee7c3-ab82-3771-a5b6-1c5436b00b15 | -8.87944 | -36.52945 | 2025-03-19 03:55:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 366598cd-9b83-3cb0-8f94-e0ede2268c36 | -12.09052 | -45.63211 | 2025-03-19 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bb5814c-6f28-3ffb-99b7-3af7f4f5119e | -12.08556 | -45.63536 | 2025-03-19 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bb7e073-25ec-3ff7-91ee-9743b3496e19 | -12.08349 | -45.62255 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2839a06-461a-31bb-87e2-28a285c6096c | -8.73305 | -36.83096 | 2025-03-19 03:55:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20dfb093-a564-33cd-8949-83092090fc3a | -11.85203 | -37.59665 | 2025-03-19 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 223374cb-690e-3bdc-b2fb-40dab41f7487 | -10.30353 | -38.74582 | 2025-03-19 03:55:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46c6dd6f-e660-3979-9bec-4a8b3e6214b4 | -11.26841 | -44.53131 | 2025-03-19 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dd4753b-0e2a-387d-bafb-a3d5d3564447 | -10.65023 | -44.40062 | 2025-03-19 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2adb4c45-861c-32c0-9267-807022122ee5 | -14.11933 | -41.67776 | 2025-03-19 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c2dd599-2537-3e62-889a-960ec08c38b8 | -7.05841 | -44.38065 | 2025-03-19 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24faff89-939c-3f94-813f-849754cd72da | -12.14873 | -40.29788 | 2025-03-19 03:55:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 095420ff-80d0-3708-bf11-db7c73de1a18 | -14.13444 | -41.69144 | 2025-03-19 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44adcca0-6dff-36fd-b4d1-70b166a08903 | -7.05774 | -44.38452 | 2025-03-19 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 910a9760-2e5b-33b4-a1a9-3f98d380a4f5 | -12.08773 | -45.62331 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4134bef6-2903-30ac-b331-6cd4c449f747 | -9.56266 | -35.69357 | 2025-03-19 03:55:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91718418-bf3d-3276-ae99-c2664ca921cc | -12.0898 | -45.63612 | 2025-03-19 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 793b820d-182f-3f10-902d-f7e2fb954baa | -11.85259 | -37.59286 | 2025-03-19 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8583a62e-a30d-3b60-9b9a-4d8e99b2c30c | -9.14541 | -38.36502 | 2025-03-19 03:55:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1e02209-5f90-3099-9dfa-ecc5744aeef8 | -13.89136 | -41.65448 | 2025-03-19 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51283ebe-00fc-3633-8634-ecc61b1aa827 | -13.54063 | -45.4426 | 2025-03-19 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f5735a-49d2-3cfb-89c9-e16714fa917f | -13.89762 | -43.85075 | 2025-03-19 03:55:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a8c6160-7d7e-3ac0-9479-3b6f033b07f0 | -13.5447 | -45.44341 | 2025-03-19 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac2b09ff-c2dc-3f06-aa6c-31ebee3d3dbd | -12.42164 | -46.72524 | 2025-03-19 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff842b0e-a822-30a7-af0a-f0a3479c8a71 | -10.50739 | -42.42863 | 2025-03-19 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 16d23ab9-19ad-3b8f-a301-0119428390b6 | -11.58275 | -47.62864 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e25397c-817a-3f46-8620-16c434bcb414 | -11.96835 | -48.0902 | 2025-03-19 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0343d9bf-43c4-35c8-8ca2-a7e9cf7aef10 | -10.5038 | -42.42804 | 2025-03-19 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5bc885fe-a02f-31bb-8518-e6386ac862d0 | -12.08277 | -45.62656 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 199e31f0-423d-3f4e-a043-87ee70c8a7d7 | -11.85315 | -37.58905 | 2025-03-19 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 05e8136f-c2aa-303c-a97b-674675e70ca9 | -14.31156 | -39.5333 | 2025-03-19 03:55:00 | NOAA-21 | GONGOGI | BAHIA | Brasil | 2911501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ee352e32-e09d-3c2b-95e9-d3210bab445a | -11.8549 | -37.60098 | 2025-03-19 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1eae1ed1-485a-3191-8a36-4e0c72ebb3b1 | -6.83369 | -44.32359 | 2025-03-19 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b6f057a-7cce-3423-8bac-fb3af8182ec3 | -13.8965 | -43.84856 | 2025-03-19 03:55:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0ecc1ed-b267-3ad9-ac4c-665bd3df4f6c | -12.86158 | -38.36769 | 2025-03-19 03:55:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b78d5d2f-8027-3a6f-8afe-15619313574f | -13.88798 | -41.6539 | 2025-03-19 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9fdd2951-74be-3da5-9a1a-edb7950ffc77 | -11.57508 | -47.62879 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d16d3c57-d869-3f69-8a0c-9ce48252b610 | -11.57612 | -47.62332 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2845aef3-6beb-3524-8b50-2821e72eb6e4 | -10.65486 | -44.39779 | 2025-03-19 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bc6cce1-c1fd-3d80-b704-92ab9e7007d4 | -10.88054 | -44.1715 | 2025-03-19 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35893b97-a740-3435-b29e-e394efba6249 | -12.08701 | -45.62732 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ef14dff-c34c-306c-8dac-d5c66c36d516 | -7.24751 | -44.77592 | 2025-03-19 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7787dd62-fa7b-334a-9305-fef0f0deaaba | -11.57788 | -47.62769 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 754c1604-7a8e-3b7f-be78-f30828335236 | -12.14929 | -40.29435 | 2025-03-19 03:55:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 776d0c18-a4d4-3666-8909-36488236c571 | -9.1793 | -40.56997 | 2025-03-19 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 42f33d45-d281-32d8-8098-5d85762d147a | -12.08205 | -45.63057 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ce2e24f-8e8c-3724-ada8-0791e80147fb | -7.05863 | -44.38148 | 2025-03-19 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d88c81f8-f59c-301f-bd2f-827bef0c8d97 | -12.09124 | -45.62809 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README3.md)
