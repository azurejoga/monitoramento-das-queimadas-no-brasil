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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86befded-3fa4-3dd0-97ca-f97cc9707486 | -10.66172 | -48.52224 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0373382f-f197-336f-be85-3d154fed01df | -9.6274 | -46.63705 | 2025-10-02 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fca7a172-94b8-3376-bdbe-3f70a520ba98 | -13.7551 | -47.99044 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e539f27-1f34-37b3-899b-6ab6f191dcd0 | -12.87549 | -47.01954 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa732589-c601-39f8-a245-7a0793cd6c05 | -14.88193 | -48.13203 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9458bfc2-72bc-3b34-b3ac-ffd815a23bec | -13.32118 | -47.21971 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9257f981-1a52-31b7-aa57-978fea30b09c | -11.48021 | -45.11822 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46b0b580-5b44-3ccc-be6a-ef1efda6c01d | -14.85645 | -48.29252 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d4df25d-b444-33a3-9635-d27ceb3507ed | -15.16307 | -52.79601 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60b40ff0-2f7a-3942-9aea-ce225d98e462 | -11.98927 | -50.5722 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e26e271c-e1d9-35ab-9fb4-4769e2169a58 | -13.65076 | -47.65523 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45f4519b-4e9c-394a-af7e-1271d0ee8b50 | -13.96213 | -48.11959 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0863743f-b78c-39f9-aaf8-2378f075b010 | -10.84042 | -46.62995 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbc55eb2-c5db-380d-9766-13952e332fc2 | -14.41356 | -46.07919 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0826441d-e1e1-397b-b538-9ed32594a3d4 | -9.92774 | -43.72247 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 224bb1a8-ae74-3c8a-9b0b-57111f45fb22 | -12.68975 | -48.58035 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96858ab6-54ad-311c-b974-ee0f2ab46164 | -11.00595 | -46.57949 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 215219da-4c51-3246-9af6-b28c987496ea | -11.00128 | -46.545 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b06bf162-f6d9-3490-af5d-a7009704968e | -15.18237 | -46.41284 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cbe66fb-a57d-3d94-9c37-549164488a9e | -13.15246 | -47.83642 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16d20a9f-1639-3d80-a6cb-448278ef74f3 | -9.90965 | -47.70913 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c82af7dd-c2d1-31bc-9f76-338d3c189a0f | -10.2392 | -50.31521 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fe6ff64-cbf0-3f75-a0cc-fc5a3d23e2da | -11.86823 | -45.00085 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b60ae3d-a2e2-3e10-a23c-ceb2d48d256c | -14.35443 | -43.84086 | 2025-10-02 04:51:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 341da7aa-f66e-33cd-8856-22f35f451d3f | -13.30969 | -47.86043 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c59d4c99-0618-3691-a072-e13cc64b502f | -11.07875 | -47.80013 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dbd0209-7f55-355f-a62e-c6c6787bba00 | -11.80107 | -47.58561 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f399641c-e0e1-3cf6-9529-78bfcd827003 | -11.82621 | -48.06937 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4b4b898-d601-3e74-98cf-c3fd9ad79fe1 | -11.19855 | -47.77531 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1dd438a-6961-340a-bbeb-9dca107221e5 | -11.5949 | -47.22236 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 292cb688-39bf-343f-8dbb-cfb12c5717f6 | -13.31452 | -47.19934 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c52adb7a-7386-3f2b-8b54-b7568853445a | -13.86569 | -47.95599 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f00e1538-1e5d-3c16-98ec-c05fe6826fb4 | -9.93602 | -43.74504 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 72584fda-f075-377e-abd7-db4635531b39 | -15.14231 | -48.02372 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d276903-ae1f-3cca-8c5d-517948a8b663 | -15.28144 | -56.79462 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7370cc9d-fa16-375f-b3ef-9c0183648345 | -10.79996 | -44.2447 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569351ab-b06a-3fb0-a5b8-541f3f2329a5 | -13.21189 | -48.51803 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1de39634-7094-3314-9c0e-fe8eb478b084 | -12.41927 | -45.17285 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efb59ed9-997d-3512-953f-8346d6b62a0b | -11.83926 | -45.02206 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f497199-8f8a-3a68-9085-0c5deba67668 | -12.80671 | -46.90353 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89f29901-4f75-3db1-8729-98bf25fac0a4 | -10.81658 | -46.63021 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb7394e6-afee-3e94-a97b-50c9cc8db062 | -14.42056 | -46.14371 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f26be0d1-e142-3bc4-b3f3-f447f07fad99 | -14.47661 | -48.42973 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d4347308-dcd0-39c7-9767-eb860901f4eb | -14.70726 | -48.20671 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efb56515-27ad-3cb2-8d04-d5ff73dbae7c | -10.84845 | -48.00566 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eea3e378-198b-3ac9-8cd9-002aa3ea8f43 | -13.2935 | -47.24619 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb24bd64-ee61-3d7c-b0bf-8ee8918e6e3e | -13.17958 | -47.83184 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cba804ae-0405-3992-949e-73b2064211b9 | -10.66397 | -48.52219 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2150f28e-b29f-3d62-81cd-1b664e6cb37f | -14.59678 | -48.3332 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aec171fa-5a2e-30f6-a708-a2d47c5a0012 | -14.19034 | -46.12544 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e198fa90-923a-3f09-9a6c-22e40ca76416 | -14.42915 | -46.11575 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 993a2146-d543-38d3-ac72-212874929512 | -13.75936 | -47.99158 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ad9718c-03dd-3640-af09-1722e20a10e9 | -16.36698 | -47.02454 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c26e5bc-2913-3555-b728-14a570575e31 | -14.8645 | -48.29797 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 836cd28b-c167-3cfa-a766-404fb6232223 | -12.76173 | -48.25233 | 2025-10-02 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c000e333-0913-30a6-aee4-d374ea48d264 | -14.86022 | -48.2972 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ed3563-0d17-3677-a1fb-b403ae917ef8 | -10.25059 | -50.31268 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb674673-d7bc-3110-9161-08fc395589dc | -13.17288 | -47.81559 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e093431-3696-3143-98c3-1e8af3f26973 | -13.21404 | -48.5023 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2db878e-4015-3801-9500-c25d9617ae26 | -11.46329 | -45.12905 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f616772-dcc9-3b3a-a1f5-0300faa8f284 | -15.22954 | -48.72492 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 467149ba-55ea-3ee7-bb84-0066618c295d | -12.68259 | -48.57167 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1f9a9cd-95cf-3263-881a-10a790545c36 | -11.98467 | -47.01576 | 2025-10-02 04:51:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ccc6b3d-1aa6-3d14-8354-9047cf6291d2 | -11.75258 | -46.82429 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c882596-8dbf-34e9-b455-86b6798f672e | -12.18408 | -47.90483 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73214401-e509-358a-b50f-f3c28dfff512 | -10.26793 | -50.31954 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2362a6ea-8c1d-36af-b9ec-b4184562a3ff | -13.75423 | -47.96275 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94fe8dec-e675-3fbe-84ca-1bbf52f96357 | -9.94194 | -43.74225 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cf772977-ef58-38fa-94ba-a5f242160695 | -10.93391 | -48.58611 | 2025-10-02 04:51:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5060ee1-0017-314b-87b4-823c6d1dbfbf | -15.22405 | -47.17757 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c5bc756-1737-36df-9d96-109199b10774 | -11.17506 | -54.11597 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ad0198-b46a-3f5a-b5a7-46bb76d76122 | -16.00293 | -50.90543 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a92c8678-858a-3a00-8ef9-c4b65aeaeee8 | -14.90393 | -48.31438 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5701d4da-d0bb-326b-bbaa-75371c016505 | -14.88145 | -48.33522 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99f38020-4825-32a0-8852-64e0fc74954f | -14.40226 | -46.08875 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71f854a1-e1c9-386f-ab1c-bfe737f43f3b | -15.14273 | -48.01746 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc0f6e0-3a6e-3b81-8456-336bf5b6aa7a | -10.33088 | -48.18463 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0345519-79fe-3753-b0ef-843d150ece15 | -14.86502 | -48.29408 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89b18d74-1ac2-37b8-8355-9d2c3d13aa0f | -13.69874 | -48.61884 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f394ee4-c5fa-359a-a3cf-a79d6448bc61 | -11.03732 | -47.81956 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6e1d4b6-4c79-3ee7-8320-bdc8b669958a | -11.00005 | -46.58857 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea321100-4143-3d90-a182-d0edbde3dee3 | -9.83459 | -48.26429 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97e5bc02-0b6d-3eff-8b8b-43b92328ce4a | -11.99476 | -46.57822 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a1cdee6-639e-3b18-b417-dc42a761ccf4 | -13.37704 | -47.28642 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffc199b6-6d17-3b39-803a-22c4452b3d01 | -14.03961 | -47.99879 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2a09f49-19dc-3560-9488-8caf5f5d802a | -12.25622 | -47.82286 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ddd344b-81a8-35ca-9533-b9d0a6e3454d | -12.81069 | -46.90881 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1af7588d-eb4c-3bfe-ada7-96c0c25a59d5 | -11.93359 | -47.88299 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e7058e-d388-35f2-b82e-52e787af4868 | -13.80004 | -47.54358 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ec42c94-e77b-3ed5-b372-86e29aa6931f | -14.76593 | -50.53654 | 2025-10-02 04:51:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3f5a6083-8ce4-3b1d-a12c-96e404a7cb12 | -12.18783 | -47.90915 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27efae6a-6a36-3831-8022-8c295e7d239c | -16.04057 | -50.85432 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a602ce00-775b-388e-8ffc-b5ada4e311c8 | -11.27468 | -47.81698 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f2d2983-037e-3d6c-ad72-4033f9f83f28 | -9.93466 | -43.75571 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59a157dd-dc48-3620-8d68-46a10bffb918 | -13.65466 | -47.31015 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cd3e3ee-42d5-3bb9-90da-debf0ae9c697 | -13.40459 | -47.78989 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 933dcd12-08f2-3c4a-a295-0a4f486b12f4 | -14.41439 | -46.12198 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f0b3277-36b6-3a56-b594-b6b0aaa80a71 | -11.14296 | -54.12516 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2287c7e2-f84c-3cad-b630-7d4cb4dfe437 | -14.49358 | -48.43226 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d4183f1-b357-39b9-bb4e-be2821e1e039 | -14.21473 | -46.11946 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README112.md)
