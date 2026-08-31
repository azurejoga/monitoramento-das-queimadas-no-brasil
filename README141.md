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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb5686b8-c33b-36b9-84c0-947ac0462290 | -14.23465 | -43.8201 | 2026-08-31 16:48:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ca36acca-86a4-3ea6-9a65-0943520a4816 | -13.51097 | -43.51606 | 2026-08-31 16:48:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b31c72de-045b-3f6a-bc99-9a6b60f7debd | -14.99643 | -48.13242 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f3cedfe6-255d-3af3-ab8d-c44f66bd7a04 | -16.2841 | -42.58622 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 71cf3697-c088-339d-9e3b-7159d83bc0a3 | -19.18156 | -57.39734 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 0c251c64-a948-3a9c-bfbf-deb28b07a5c1 | -17.89745 | -52.08438 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3b99c797-337a-3da3-bc30-f958aa0bfb76 | -15.64509 | -50.10228 | 2026-08-31 16:48:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f73dc09d-a8ed-3652-8cac-8028a6fd8260 | -13.41011 | -40.96297 | 2026-08-31 16:48:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 352c926b-8bf8-3bd3-b3ae-d5c9bb7d75ea | -16.20187 | -48.73269 | 2026-08-31 16:48:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 071295d3-3b20-3601-8cac-f2b4c5506fb8 | -19.23076 | -57.34658 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 85cf37c9-a4cc-30f0-9f09-464c2374e941 | -14.08817 | -41.34642 | 2026-08-31 16:48:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9c175868-2f13-39db-a54e-1ca010fad277 | -17.89116 | -52.1011 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| df594627-14bd-3ae6-930c-d6c99515e625 | -19.07103 | -46.20998 | 2026-08-31 16:48:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3d296a2-077f-364f-8aa7-868c6f4bed8b | -15.65787 | -56.37344 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88279251-1a90-33f8-84d7-b6f145f8d8a2 | -14.86704 | -40.73016 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f05bc30d-1de1-343b-8574-2f6f45cbbbd6 | -15.2314 | -56.36499 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5e00a535-01e5-3409-9876-4b71753346da | -15.87214 | -56.48829 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d1e3f812-cb29-39e5-aa60-a4d312f6ceeb | -16.69322 | -49.89305 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1b8d9a2e-5c8c-3b67-8d16-cbb70e2c3755 | -18.27013 | -52.6938 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5a17bd13-0ed4-3d3e-a648-b8b1d50cf069 | -20.26143 | -58.15499 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f009d05b-cf7d-3965-8639-b97c97cbc99f | -17.3111 | -42.69888 | 2026-08-31 16:48:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 112b7cd6-d025-35d3-8c0c-d087b6ac03e5 | -15.36909 | -41.18504 | 2026-08-31 16:48:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7630c7b8-5cc9-3bd0-8676-9b5a9a54ecd0 | -16.87404 | -48.28001 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6e081efb-6a7e-31d8-891d-bfdf5d7c7b0e | -15.97274 | -55.95218 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| aef22d69-5015-344f-9386-3f922ef026fc | -19.1195 | -57.37625 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| e0148a3a-748f-3b62-8e33-8d028b6d45ae | -15.62739 | -56.4198 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 46a13ab6-f1f4-3a86-a4c1-cb34d1c5ce39 | -13.31592 | -40.78885 | 2026-08-31 16:48:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 343151c7-72cd-3ea9-a437-ee2362be969a | -17.84694 | -50.50011 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 07ae5302-e46d-31bc-b62e-7471654f2d40 | -19.12115 | -57.3944 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 3ba00c5c-bc5a-3a17-a943-d8761c2ece36 | -19.12424 | -57.3968 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| ee759a32-1fe8-3934-a625-0d5a855eecc8 | -14.23099 | -43.82074 | 2026-08-31 16:48:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f5bd7dcd-3498-37ac-99ac-f0be83c95ecc | -14.48443 | -52.12862 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b63d8d7d-4b90-3443-8608-fb0a15a9437c | -15.34415 | -53.79889 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c290fcf-5805-3f1b-abcc-3bae2e24b5f6 | -15.99053 | -48.04759 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 36c0224b-32c7-3a93-86d4-419e87b40c12 | -18.12683 | -51.61543 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 98dcacee-d138-3ec6-bcc6-aa8c54209a03 | -15.56148 | -56.26841 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9b94379d-5ee4-37e6-bc50-169a5a92d1ff | -15.34249 | -53.78527 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| baeca49e-27b8-35ef-ae21-8977b1ee9fcf | -15.22004 | -56.35974 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7407e50d-a13f-367f-92f8-2ef60341d072 | -19.13526 | -57.38652 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 23d53561-2de2-3239-bae0-5c3f4ed92aff | -15.46573 | -53.95502 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2b6013e2-5a22-3388-aeb2-e5ff62154c7b | -17.72362 | -44.25988 | 2026-08-31 16:48:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab5ccc10-8402-36e5-9c80-94c1af82c792 | -15.18771 | -46.24732 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4b44cf38-179f-30f6-9656-1f19bf1c030e | -16.36474 | -46.88042 | 2026-08-31 16:48:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57e1b0b2-65d5-3707-b075-d8241702664c | -17.87687 | -44.25695 | 2026-08-31 16:48:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8be98127-fdbc-39b2-8ede-9dc9a9b3a53a | -18.41372 | -47.96161 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a8fbc73f-53a9-3873-ba04-98acc9961d0b | -14.19943 | -46.56936 | 2026-08-31 16:48:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4b09b7ae-ece1-37fd-9a52-f3bc33fa1f86 | -17.87921 | -52.10656 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 1d134cfa-0b56-3cd4-92b4-ccbb3f73a8e0 | -19.1705 | -57.40767 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| f2a404d0-0b80-365d-88ac-e1e70754bdd1 | -19.23976 | -57.33945 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.4 |
| b9c96d99-6b00-3ca1-aca3-1ab01e5369a5 | -14.96594 | -54.58899 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 84ce2ede-f12d-3580-a5ce-d7826ee7f083 | -13.37548 | -40.36068 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| bcc1a301-90d8-37e5-bfc4-97b693e7b06f | -16.97906 | -53.28426 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d0523927-21fd-3b05-908f-b6e5360ae2c8 | -14.6389 | -45.11543 | 2026-08-31 16:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1fda5dc2-9423-3e93-98cc-fefa5b37a56d | -19.14707 | -57.41467 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 0b674a59-d0b3-33f4-9efe-20393f61a921 | -18.26396 | -52.75166 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 7751656b-0eff-3f42-9ac6-b4e58e53722e | -14.79188 | -48.74382 | 2026-08-31 16:48:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72d884da-852f-302a-a6a5-b1a6910555a8 | -15.40638 | -52.71627 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3c99eabc-9231-347e-bd66-9eaaa1e650f6 | -14.5942 | -54.11563 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c91648c-86ec-3725-97cb-eabc8d0c251f | -14.19019 | -45.3098 | 2026-08-31 16:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d19e7790-ed31-3044-93fb-7e21b8b14c03 | -18.88735 | -48.24184 | 2026-08-31 16:48:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1ca644a-de5a-3017-b76f-cfe90d98ba78 | -15.91822 | -56.22079 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9d323bf9-bf57-35ea-aa4b-c1d0f8b3b8e4 | -15.42979 | -52.68908 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eb9b95ef-b9c9-3c45-980f-38f91761d952 | -17.53481 | -52.54947 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c94859ef-2319-3abc-aa15-8ead2e8b5d7b | -14.80221 | -40.67358 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| d9a2ba03-169d-322b-bea2-193ffe69407d | -14.82419 | -55.73113 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6165adf-8265-33c6-9632-0bb3b23efb12 | -15.24352 | -56.37701 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7927416d-ee7a-39fe-bdf9-2f922f65cd17 | -19.17984 | -57.37918 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 4cf589c9-b492-3c5f-ae94-f2067216aeb1 | -17.86261 | -52.10864 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |
| e2b4606b-3506-3111-b866-1e7d3fd8d499 | -13.736 | -42.48806 | 2026-08-31 16:48:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 74ba2be8-8466-380c-a8a7-68e43e296e20 | -17.18953 | -54.31483 | 2026-08-31 16:48:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51a47ad6-cd23-3558-9d32-e528482729da | -18.29539 | -45.02191 | 2026-08-31 16:48:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ed5d8bf-184c-3f81-a050-1d01da53c941 | -15.23065 | -56.3583 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d6156921-7f7a-3b4b-b889-399c3e52c048 | -15.9828 | -55.9477 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 7c3e3dc3-cde1-3249-9d6d-e68907bc5d03 | -14.60142 | -44.90913 | 2026-08-31 16:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a3ab867-c777-3187-b502-5783d32bb198 | -16.07895 | -41.4453 | 2026-08-31 16:48:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2a04a28c-d56e-315a-a032-a479547f145b | -17.89843 | -52.09207 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 3ffc0100-4e7a-30cf-b328-f17533a6bd90 | -17.86431 | -52.0886 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| c670b054-1404-33a9-9a26-b66f7dce453f | -19.15477 | -57.36804 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 9560380b-f58e-398c-909a-61e6f34993d4 | -19.14111 | -57.41529 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d81714d1-2b02-32b4-ad5e-5ba6863dced3 | -19.15051 | -57.38678 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 7ff16d52-a403-37f1-a09e-34d1615d1857 | -15.552 | -56.27973 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a896dd39-65dc-3c6e-854a-83136d9dfb68 | -19.09955 | -57.39011 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| caaf4d45-7f8c-3199-ae42-b1f169246f64 | -19.20148 | -57.3541 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 19dcd88d-1ee4-31f2-be1a-bc78b0a4bd20 | -15.87253 | -56.49191 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ee1b843-d3d9-30e6-9a9e-f4bfe39e5887 | -19.1302 | -57.39619 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| e8618c39-a130-3830-aa3d-a2ab34ac312e | -14.98975 | -48.13346 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a8a4d89c-bc0a-3b44-a8b3-bd5fa6f5268a | -19.18321 | -57.35138 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| aba56092-c3da-3c63-8900-857ac7b080ef | -18.90975 | -50.88278 | 2026-08-31 16:48:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7ec435a9-0a94-38c9-9828-fe78841ddfbb | -17.88089 | -52.08661 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| fcaea574-42c8-3cb6-acbe-fd8a2f57730e | -19.083 | -57.40559 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 7523aaac-07a3-3df6-8a31-2e84a6e266a8 | -15.49503 | -56.00853 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| deb3e3e1-54ca-3087-8944-df3af4b27303 | -19.21722 | -57.35552 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 64f76c93-19bb-394d-a594-4d1e0372ccd2 | -16.00054 | -43.5462 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 52844bab-a128-3b23-92ed-139d8d8ed4a7 | -19.1439 | -57.41314 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 5937e32e-bb56-32f1-b6d7-89bad90e1cd4 | -13.07359 | -45.17038 | 2026-08-31 16:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 939a9875-1290-3887-a8e8-56a59573399d | -17.85798 | -52.10526 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 65990975-2ea9-35dd-9816-f0bdb822835c | -19.10682 | -57.40312 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 78dc6feb-3a80-33c3-968b-4b761b607775 | -15.42669 | -41.21564 | 2026-08-31 16:48:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b09fac8f-6cd4-3895-9952-e76c3c6bbfcb | -16.55558 | -52.51023 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a3b4d5b8-9c44-34e9-9c57-5b63e8af2c0d | -15.83305 | -42.00281 | 2026-08-31 16:48:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |


[Clique aqui para ver as próximas entradas](README142.md)
