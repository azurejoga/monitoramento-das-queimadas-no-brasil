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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 252f0bec-1b04-3d6a-94d9-6725acb19536 | -10.06487 | -46.94204 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a5ad6e9d-e09d-36aa-8ac4-48daa52cf9c2 | -10.76032 | -53.98701 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f41a1f18-9b81-3263-addc-e625953947b9 | -11.01425 | -49.65493 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e87dc4f6-e236-3a3b-beb8-91a95d367755 | -8.59441 | -54.7894 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 146480f2-906e-3b5e-b135-b5450058d39a | -13.60239 | -45.77635 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b16bb2e-bbfe-3078-89e2-c455f3109b08 | -8.77606 | -50.07592 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a950a7e6-4bf1-36b7-b35e-661f6350ccfd | -12.50474 | -43.8147 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e66271cb-4b0f-3442-9082-7a63f9b9194c | -11.2384 | -45.04709 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b15d08b0-0d56-39fe-ad84-7008e6408432 | -14.88441 | -52.60299 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 03980c1a-1169-30e9-9d94-4bc2c1914b45 | -10.7744 | -50.63446 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d59a8ae-7100-34c6-93d6-38514d5a9c85 | -14.91031 | -43.40996 | 2026-08-28 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4c70c319-ae5f-357c-bb3e-8873eb7e828b | -10.84954 | -50.51864 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 363b2158-fe21-3b4e-9ba7-58ff1d993063 | -8.72335 | -48.22908 | 2026-08-28 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 235bfa60-3112-3866-b3a3-dd47dbf95190 | -12.26018 | -50.58793 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 07622f65-a42e-3d97-b8b2-ccf655aa060c | -14.88668 | -52.60095 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2c0d4d56-25a9-3ee1-a5d7-5536b9729072 | -8.81165 | -50.08189 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c894bef-899b-35b2-be15-565784be50d3 | -11.81255 | -47.19696 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6091e72e-d21b-30ed-a1c1-b85661e60700 | -10.79116 | -54.00384 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a61aa8ac-b2ad-36e8-87cb-0ff1d55e5a57 | -14.86949 | -52.60539 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f2a42b2-fcc6-3748-8e3b-aadb603203b7 | -11.64123 | -46.73483 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 934c7c35-0136-3b9f-ae91-f863d5601f8e | -13.58182 | -45.77666 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46cb7457-064c-3320-9ad8-bf433062fd73 | -13.28355 | -46.6378 | 2026-08-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd2602db-e9e2-3507-8700-98981b8bf902 | -14.16378 | -52.82208 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6330312c-e32b-3fed-9386-d4cd68bac8da | -11.24287 | -47.06304 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b1b280f-6b05-3f4f-845e-919d84a6a8a1 | -11.01605 | -45.07654 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7375d11c-b247-303b-9469-159110107722 | -10.88501 | -50.52062 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3218ad20-979f-33bc-81ac-0a0b34f6e85b | -10.55466 | -50.41675 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b73bba69-ef9a-398f-b1fd-c696fd72ad6e | -14.42026 | -52.58785 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be0ac485-2a62-394a-8696-b363249b2d0f | -14.90403 | -52.60106 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30d27b48-465d-3356-a491-648eb8fffcd8 | -10.80552 | -54.01806 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e83c66-5d69-3cfa-b58a-91d4cbdf5416 | -13.8395 | -54.04497 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca2ce9c-45dd-3bc5-a500-84ae751db377 | -10.79595 | -54.00854 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cc4236d-ee55-3504-8e08-71379458ce9a | -10.94053 | -50.54252 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c222a369-4bee-3987-97c8-e0fd9065fc86 | -11.37598 | -45.14598 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33de7437-686f-3b77-afa6-6a1192fde110 | -13.86316 | -54.11679 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8066722e-b185-3145-b8c9-51dedc289a01 | -9.47009 | -48.18005 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 365c6c4a-f1d6-31d0-95f9-f6f1b740cd9e | -14.15225 | -52.83081 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d4738d0-77e3-3c38-9857-d232831184fa | -19.85162 | -46.30486 | 2026-08-28 04:17:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05627c86-f367-328b-a378-03f64797acd7 | -15.582 | -41.77719 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| df809028-0f29-3b0b-9297-905645b939e8 | -13.60457 | -45.78407 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d3d8d28-3937-3b1b-8193-fdf73f07e05c | -11.28301 | -54.02583 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa6c93e9-7961-301d-af17-54ca26f5f88f | -10.77002 | -50.63368 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5428d070-4767-3225-9889-c2afca0622f6 | -11.57485 | -45.51882 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba1fece2-09fc-32d2-82ac-29c8d5ab296a | -15.62568 | -45.93114 | 2026-08-28 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6247cb7-2f68-3b50-84a9-fa085590b0e7 | -10.53734 | -50.77448 | 2026-08-28 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1c4f639-7bcf-3511-b367-7b8f20383811 | -14.40079 | -53.0559 | 2026-08-28 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564fe14c-a82b-3db8-b133-14b8bfe3f37a | -12.28782 | -50.6056 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b4c795ed-ec2a-3d14-b9ab-7810ef2b8810 | -10.95251 | -46.26076 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a99ad6df-6513-3ec4-94ea-9cfe894e9db4 | -11.47291 | -46.94506 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3cf183d-abb5-373e-9974-baef9dda2e12 | -9.44619 | -51.71246 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 849568a8-b8f7-3723-9866-6ca9812c6dea | -10.46571 | -46.18591 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b024db2-1db1-366a-9563-973cfc7a2b69 | -12.25738 | -50.57902 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8e539a0f-57c0-3659-bfc4-f380f68b852b | -11.76937 | -44.91666 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2f4f16-6d5b-31ff-b09c-0934653e0a2b | -13.25419 | -45.09855 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b2cc353-ab30-3c56-bc59-3d129166c7d0 | -11.27962 | -54.0141 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adc619d8-1900-38b8-a47f-d75ccfa35def | -12.01779 | -47.16146 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac3a04f-7702-3d81-a049-8e769a674e36 | -11.83454 | -47.21724 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2fef992d-1406-3043-92cf-5baf811889cb | -11.64342 | -46.74324 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5df4072b-f8e7-3fe8-abda-afa1b1df1040 | -9.4718 | -48.17712 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e9f69f5-a164-3fb2-b1f2-71778429006e | -14.87276 | -52.59821 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8adba5ee-7372-33f4-9874-b4226140bd19 | -13.40951 | -51.42978 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95606e45-67d3-3806-b5b8-b49dfd97dee2 | -9.16104 | -49.96364 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc486744-211f-393c-8ed4-ba0cdf76567b | -14.87717 | -52.59066 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8a3d8f23-4858-369a-8063-5f04e25bdb7c | -11.5737 | -45.52599 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4bfe1b6-594b-3e7b-83bf-2d267c55d419 | -9.61814 | -55.1191 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d3fe1add-4c53-3eaa-b906-e7b25c1846cd | -14.11655 | -44.38193 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18cb7511-1aa7-3f68-af68-4e0b2a6ea393 | -8.78552 | -50.07316 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93b7ea42-6ff0-39d8-95aa-448c4bad043b | -12.77209 | -44.26439 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c061bf-4e25-3d4f-85b6-5722fef3d52f | -11.23478 | -54.00577 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd14f7d9-6729-3565-8773-37905eada0e2 | -15.65035 | -46.47755 | 2026-08-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2bfc751-425f-3ccf-a499-ab2aafab8d77 | -11.34136 | -48.38314 | 2026-08-28 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7114122f-20d3-3a99-ba60-a2650bf3f1ca | -11.23612 | -54.00608 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 02fb6b35-16c5-3bc9-a5d0-61c5f313407f | -13.32612 | -48.19661 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8ef278f-fe56-37e2-a80e-22d9b9fb4a53 | -8.83436 | -49.60926 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f385d915-94f0-3dd8-8b72-5763ee48176f | -11.56769 | -45.49929 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bda350e-8503-3181-b138-5ade9f116d60 | -11.64878 | -46.73215 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6339cd20-17e6-331f-90cb-f0a59b8a02be | -12.50916 | -43.8081 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd3423da-b9cc-349e-9233-65f86b46ee0f | -9.66798 | -55.08607 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfa7f82c-ede4-30bf-9fcd-256229ab68f3 | -10.14546 | -46.87121 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51f972d7-4045-3f19-bede-9309d29d3145 | -12.42923 | -43.41664 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5e10a2af-bd90-34ab-baf4-3540dcab0b80 | -12.43313 | -43.41356 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ba52b554-2760-3104-a01b-5e93990d8270 | -12.07192 | -47.16557 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee35a58-0ddc-3b10-a08d-3b06273c1274 | -11.18917 | -51.23318 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7ad7b084-5c94-3b39-b3fa-40c63a76317e | -8.95423 | -50.17124 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 584532a8-ffe6-360d-9af5-ac4a4b0ddbd1 | -12.6921 | -48.43012 | 2026-08-28 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d430a83-497b-3cc1-9aa7-194cf277bd41 | -13.59572 | -45.77526 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b206033-7a52-3eab-92f5-da4c5423fc7b | -13.32538 | -48.20094 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b78bf93a-ac32-38f5-8a9f-64804017e88a | -11.74032 | -54.52157 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cd97681-2e40-3bd9-9df2-302ede4c4667 | -9.98772 | -48.59108 | 2026-08-28 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62ed1b59-9b38-3b96-afb0-bc0838d8606a | -13.6079 | -45.78461 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b28c89a-d0a7-319a-8ade-ba9e7369d984 | -10.53657 | -50.7789 | 2026-08-28 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02c72eb4-3289-3e55-a9b7-b9161371756f | -8.939 | -50.77047 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c7937b9-d685-338e-b592-1ef473d4c488 | -9.66195 | -55.08522 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4236a7-b3dd-3c5c-abe2-39c52506b972 | -9.97219 | -53.93922 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 99b7a893-a339-3582-8c98-b5bf1ff1e32c | -12.76823 | -44.26739 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3966e1f-0918-38d8-8545-7269bb741bfe | -9.22131 | -51.56387 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4f4ad33-3f6f-3fa3-ab1e-3292ec848dc5 | -11.01993 | -45.07355 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1cead2aa-5d16-36ab-8ecc-3d156349c1a4 | -11.28913 | -54.02325 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ad1b386-3a23-396b-bd2d-f6aae16b0de8 | -9.9726 | -53.93972 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d7a8eb27-98c6-3387-b63b-3c7fa364930e | -14.88544 | -52.59766 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README26.md)
