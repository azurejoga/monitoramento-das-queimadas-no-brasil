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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20ecab33-e4d4-3fc7-907c-a9a5124ba34a | -7.7971 | -42.55227 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5c4004c5-f298-3367-965f-3719bb34359b | -7.1605 | -44.99318 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bf96bd4-f3d0-3440-bb8f-7145b9dfbedb | -6.87176 | -47.23943 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2398c2d3-8ed7-3c4c-9eeb-c68b72424a37 | -7.01682 | -42.30812 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b57329f-eb0e-3c12-8bea-7bd80400a856 | -5.25747 | -39.26025 | 2025-10-04 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d322b8d-1b3c-3ccf-8388-7236131b6c39 | -5.99915 | -44.5575 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b620138b-57c9-31c1-afcb-45b02dec0812 | -6.74525 | -44.58557 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89aba544-7f96-3887-be5b-6b28e7b80932 | -7.71279 | -42.57133 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 646f54e1-3ed5-32c3-b16d-9b19b1de4073 | -7.79546 | -42.56277 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d0a616c1-47e0-38ea-b7a4-0343a6ce8968 | -4.88692 | -45.06442 | 2025-10-04 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c9889f-ae29-3d2d-be6d-ee6fea922739 | -5.6623 | -42.71796 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fd9a9ed0-d1c3-3d25-9298-140104649dff | -5.89488 | -42.53493 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7f9115e-a597-3304-80af-e0d92189e87f | -6.09129 | -43.48389 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2466d56-9537-3026-b9e4-667a5cfad644 | -6.04655 | -42.51971 | 2025-10-04 04:12:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| c34d60f1-1934-328a-9535-3abd6593f435 | -4.42987 | -43.24888 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c4afe3f-34e8-38ed-bfca-f4d4ef359ffe | -5.48728 | -44.0989 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eba7d36b-bfe7-3c02-b329-99f46624a65d | -4.42818 | -40.76343 | 2025-10-04 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 171a6543-439d-3828-91b8-9e5e57d81486 | -6.69052 | -44.00999 | 2025-10-04 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff8f7bf-e640-31a3-b2be-57142f38655b | -5.4835 | -42.79548 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f08dad21-577d-3fe4-aacc-0ff306654cd6 | -7.32837 | -41.43991 | 2025-10-04 04:12:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be783594-bba1-3407-9fe7-290a17bc5d3a | -6.23907 | -44.22088 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12629e64-cd6b-3f85-b338-27b32e3ad97d | -3.8464 | -41.56405 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c03377f7-13c0-374e-bb20-384f13eb7f44 | -5.80109 | -42.8919 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 325b8020-b749-3f7e-827e-bedccd5e3168 | -4.44536 | -43.23706 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44a8025b-39ee-3ff1-ae86-cfaebdc0dd7f | -5.71707 | -44.2378 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bf713da-49e0-3e3a-84d7-a0911d46c703 | -4.25525 | -48.56266 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dc01a8d-baba-35b7-8945-72188f912d98 | -7.74283 | -42.55093 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc66a3cc-ecb9-38d8-937a-6da95514cbb1 | -7.54485 | -42.40471 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2e8a3796-58f7-3712-bcac-2e18f9f6e242 | -6.20388 | -44.33313 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a74183d-1a6b-3372-80be-3d0ef4f13583 | -5.44607 | -41.99488 | 2025-10-04 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5755e12-0286-3ee5-bbb7-c7b464b9b639 | -6.16193 | -44.61615 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1f80572-75ff-3c7a-8650-4e016458f7ae | -5.60964 | -43.22271 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b556a297-7425-3cff-94b2-1bacfffdece5 | -7.75335 | -42.54897 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7dab188-a0dd-30da-91d8-2a3b47e9904e | -6.6439 | -41.95482 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6efcc07-26b0-3b64-a817-1592f30ed5b1 | -7.05439 | -42.78509 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65d30f22-ee72-3383-9f90-409d8d15c02c | -6.3699 | -43.88981 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3f3e33-2a0c-3cda-bdc9-2f31c8464259 | -6.36544 | -43.89637 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be6343e4-f549-3718-bf0d-2380d9a7301d | -4.73372 | -43.26129 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c9e168a-1d7b-3eb5-a967-4f46fa08c1b0 | -3.09048 | -48.49139 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af02b464-3566-37ca-a98b-1b6109f290b8 | -6.13934 | -46.55399 | 2025-10-04 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e797be8b-82e2-3577-b6ae-602a478bc0e0 | -4.42765 | -43.24141 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e362982-edb0-3785-8a46-6190dc8c9d13 | -5.80406 | -42.72261 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47735037-11b3-304a-aa1a-cd246f74a135 | -6.07081 | -42.51642 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b2039918-23f7-3956-afa2-7568a1d54d55 | -7.29492 | -55.32078 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 300b88eb-070a-3e43-b221-0ceef6d0dc94 | -8.95806 | -48.68872 | 2025-10-04 04:14:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 963e8270-c7bd-38cf-8c7f-de64560f22c2 | -12.42279 | -45.15724 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa0a237a-8587-3435-a259-ae3783a0d2d1 | -11.83291 | -45.01989 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6ef731d-6f0b-3867-b6ef-b2e0bcaaeb66 | -9.99516 | -48.27482 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0111e16c-6236-3729-a0bf-3e1061772041 | -14.64642 | -48.30629 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20d8dad9-b5ee-354f-a774-b67cb005a868 | -11.88117 | -45.01701 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74675d39-2189-3521-9406-f5d01cc782df | -10.28019 | -44.33902 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47d8d213-7cd5-37b1-aaf1-11078c5a6c04 | -11.14737 | -43.38234 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3b3ab08-5b18-3a53-a2ae-f803436302ef | -12.86277 | -44.63396 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51dcfd66-c04d-3bbb-aed9-607895befdfb | -14.31752 | -45.86018 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0282158-8dce-39b5-baf9-f8a48ba56ef9 | -11.45578 | -45.14362 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fba81331-2ede-3036-a5f5-5397efd01169 | -11.04787 | -47.79945 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2c254e0-8fc3-3425-b356-98ff23880465 | -13.2957 | -47.82476 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39bf5dbb-16f5-366b-ad43-dd7292291e61 | -13.30434 | -47.56937 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e948ea15-89e3-3835-b909-a69c51a60d4b | -9.95508 | -48.7692 | 2025-10-04 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f79b4df1-f6bc-3088-869e-9bcb9aa13785 | -13.51288 | -47.27896 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f36ca61-bac5-380b-b238-dbfd037a2907 | -11.45188 | -44.96054 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 228c0833-50db-3c56-9b38-3e81ea8fd0bc | -13.10016 | -47.89048 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e402f5b1-3c63-30b5-84b8-89a98aa9c6f3 | -14.22338 | -46.08753 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b9729be-c20a-384b-a833-c583c30adc3e | -13.69643 | -47.35144 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5cfece65-0aca-31f2-a8d1-b2d5a168781c | -13.93767 | -48.14985 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 785f1070-8a8b-38e4-b053-0b4a29a09d75 | -11.73979 | -46.82188 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e4836c5-44cc-3676-a026-5f3e73d9661a | -15.67307 | -44.51099 | 2025-10-04 04:14:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe5df31d-434a-31fd-84aa-9f2273354b67 | -11.62085 | -45.02855 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8570580-1bf8-339c-98f7-c245fd771ad3 | -8.12913 | -50.23392 | 2025-10-04 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748720c1-b5ca-3a69-89f9-ad09b77984ca | -11.10374 | -47.71748 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d77cb165-ea26-350c-8bf8-b6cf870cbbd9 | -9.95044 | -43.76226 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9ddde8b-cf73-38e9-a572-155a6fc6a200 | -12.08143 | -45.18837 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1d6b0bd-7a51-393e-9034-94820c60ca30 | -11.8056 | -45.04099 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40e0b7d6-e49f-3693-a942-c77bbed606c8 | -13.67278 | -47.29826 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc6acf2-75bb-3510-b271-081fcb63bbf8 | -14.38788 | -45.96898 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c37c89df-2f9c-3345-8291-febd219c1a28 | -11.15238 | -43.39392 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 31ac922f-a8b3-3ee9-8ed1-d2bf43e03f4c | -8.50485 | -54.59953 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a74c491-faa8-394b-bb7c-c18166ad5c39 | -15.03597 | -46.97568 | 2025-10-04 04:14:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 35550028-93dc-33fc-8c1b-707178a80182 | -13.33372 | -50.95339 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f2368a9-62d6-3f36-9999-5715f014950c | -12.95437 | -42.42068 | 2025-10-04 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 610bc736-87ee-3feb-b938-18e916bfbb13 | -9.92105 | -50.89643 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2fcf32-86ca-36cf-8f99-938d73fa2d1a | -13.23729 | -47.83377 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 441f150d-e26e-3fe4-82f1-332160b665a6 | -14.44196 | -46.10218 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1447639-05e1-30fc-98a2-9be4f18c8f61 | -11.91561 | -46.35838 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89ad1356-5aa7-3b9e-b109-de1c9d0eebfd | -11.08755 | -47.88164 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eba3b2d6-9e18-36b8-9a58-595c281b571e | -13.33278 | -48.08865 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e6a4519-4f29-3dec-9f3a-fa845c79b7b6 | -10.03113 | -44.02587 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7308a1ca-4f75-33e6-9ca9-021d1e3615c5 | -13.63357 | -48.6702 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 955803e5-5703-3ec7-80ba-7b264c733630 | -14.66139 | -48.28491 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a16168-b0c4-3aa6-935b-13ca97708b20 | -14.74999 | -48.13809 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fe1ecad-4ae2-33c1-b62a-9d419891177e | -9.33469 | -54.53172 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de6b9ed9-b2d1-376b-b0be-f1a7cfe3e8da | -12.47268 | -54.42639 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a96eb17-de7f-3af7-9faf-28af3881698b | -14.69994 | -48.19162 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d6a95bd-4472-3f38-b522-50160e96611a | -11.63122 | -45.07034 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ff28b7d-0805-3cbd-8164-358aa09d3f94 | -11.82889 | -45.04489 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c555b983-1c69-325a-88e6-72c22d9fb3fb | -8.85126 | -46.79235 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fc4b635-531d-376d-862c-193b99aea78a | -11.47331 | -45.01873 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e6d1f30-90b4-3f8b-b21e-d08629ec6340 | -11.51153 | -45.01038 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c90c0f21-9dac-3014-82be-15411434605b | -11.49599 | -46.75879 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59f2a218-e859-3ae4-a8d6-10667d7f759c | -9.93636 | -50.24157 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README66.md)
