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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe78bfe9-5b0a-370c-b171-d4e7a7aad80e | -4.56198 | -48.01075 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b46e32d-8b2d-30f8-b95f-63fbd06c6fe7 | -4.80293 | -43.22001 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3822338-9a7c-3122-a819-e3750fc2c7af | -4.78199 | -43.7886 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e1e6806-539c-35b7-91cb-57f36ce5a5c6 | -4.22255 | -46.81769 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 369a1ab8-af0b-3fa4-8cad-1ae109e70cf7 | -4.19257 | -40.47562 | 2024-11-16 04:01:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66377909-0fea-3ae3-964f-8309bffd2aa8 | -6.97783 | -38.45975 | 2024-11-16 04:01:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99a6ee58-2633-3581-b762-78930b3a4bd8 | -5.26129 | -47.18409 | 2024-11-16 04:01:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b16e60db-5013-39d4-a526-1a160deafdff | -2.03108 | -46.36959 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97539c66-8537-3887-9723-9b7969611354 | -2.18272 | -47.94824 | 2024-11-16 04:01:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c40540-2b0e-3d60-9092-a64f54955562 | -3.11933 | -45.74472 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eab7300b-09fb-30c3-8b88-29081b4ece41 | -2.08185 | -48.95468 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dc173fb-2ba2-3a8f-9e3f-bde43917e84c | -6.02037 | -48.03598 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d846e539-434c-3905-889e-5751ef464506 | -2.47513 | -46.36817 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4cc4b754-b0e9-3fb0-beb9-51cd6defd842 | -4.37698 | -45.62478 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2643f16-ada7-348a-bcb7-a33af83e6e11 | -1.89712 | -47.00851 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d9dc69a-ab88-3856-b7c3-f84441800088 | -3.56033 | -50.24325 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15a15b8-a4bd-365a-a6d7-c94a82c4f92a | -3.79423 | -40.9944 | 2024-11-16 04:01:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc5a166e-4eb6-3c4e-91b7-31ce19b6c19e | -6.16884 | -41.16847 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cceac106-0050-33ce-bd25-d8e562cc1bce | -4.3747 | -48.08126 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdceaf93-e005-3b9d-a2b9-2f3206486ded | -5.59048 | -44.58196 | 2024-11-16 04:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deb0a926-41f7-3292-b194-4390fc7a7f90 | -3.98116 | -43.72391 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8d730dd-6d7b-355e-977d-71e99d31f708 | -2.61767 | -46.18269 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64424fde-974f-37d6-8e2c-78374cf69d6a | -3.61556 | -44.79234 | 2024-11-16 04:01:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8ab5ce9-e6bf-3a64-bde7-a86fdfe6bb3d | -3.49556 | -47.20713 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4238877c-c2f2-3379-bf36-c6dc218d4c47 | -3.92274 | -46.40662 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3a1352b-c29c-32e5-85f3-02a47bd8db3e | -2.88591 | -40.38947 | 2024-11-16 04:01:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 92e51a01-e4ed-3997-9a81-dd80e9d4ac77 | -2.94762 | -48.01608 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45d08fee-88a5-38e0-9dc4-75e8746cc545 | -2.23946 | -47.2094 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9378b38b-6070-3d49-b307-3559470ff68f | -3.15294 | -44.02901 | 2024-11-16 04:01:00 | NOAA-21 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae264a01-b33a-38b5-99af-f1d4109e9cc7 | -3.22135 | -42.08266 | 2024-11-16 04:01:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9ab1847-513b-3c56-9d0f-ea4163c39779 | -2.6694 | -46.18143 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b8737c1-d977-3c03-bf2c-595246f6409f | -3.79111 | -43.91446 | 2024-11-16 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7d8adf1-505f-3e3b-a42c-2e5b27da243c | -3.50439 | -47.21384 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67a21794-9f8d-371b-a484-13dfa36ff4a3 | -2.51037 | -47.47755 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a45376e4-051d-3e47-8f79-49a8fb504bcc | -3.32378 | -45.51405 | 2024-11-16 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daa3a9d7-b2ab-3347-958b-da38ce480603 | -3.12347 | -45.7467 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a1aa561-008d-3655-9b4b-ec987d01f80d | -4.65 | -45.13102 | 2024-11-16 04:01:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88107b27-8e9d-3013-9f88-8311b85b47dc | -3.12232 | -45.89126 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 176b09dc-660a-3dc2-a771-63ac6fa6e4e3 | -2.66102 | -46.17537 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a1b00a7-e5a8-363f-9288-da77ff9cdb62 | -3.27025 | -45.50267 | 2024-11-16 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8e31c455-1f11-3904-8688-1acde94d7d07 | -4.35818 | -45.87415 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc1cea9-2f55-3631-811d-66f3f03e5e97 | -3.88121 | -45.0281 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc9f0414-99f4-3277-91ec-8e12c771ac24 | -2.77384 | -48.57867 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 293dcb1d-ac7a-3d52-967c-94b0fde43c0d | -6.64006 | -47.34347 | 2024-11-16 04:01:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e7151d2-eea3-363a-a59b-d79619a1ab18 | -3.43287 | -44.60727 | 2024-11-16 04:01:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 123d0698-d8da-3e1d-aaa6-2b12824824e2 | -3.74226 | -45.66224 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| e6f62b13-a77a-3e6d-85d7-ab60d7eb4c2d | -6.16996 | -41.16142 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40c7484d-d1c3-34a8-b7a5-599cd6c079f7 | -2.6131 | -46.18198 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4290a63-0eee-3742-ad79-89b276dbc2dd | -3.26834 | -45.50122 | 2024-11-16 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 061f8251-8b7e-35e5-8b1a-fd0f95cdc8b2 | -3.30353 | -42.48137 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 440c9fdb-3235-3f46-912a-c92263df5237 | -2.66582 | -46.84098 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05efeaa8-5ad0-3bbd-b0c0-7a2443603c58 | -3.93115 | -42.40846 | 2024-11-16 04:01:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df8a2058-cb1f-379e-b936-71937583e331 | -2.74028 | -48.56277 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 566f0fca-98dc-3304-9752-706ff3ad1d34 | -3.88184 | -45.02438 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3acb3915-e8d7-36ef-9650-c8f1de55c3f6 | -2.97511 | -47.99035 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d34289f4-b99f-3900-8b27-eed6b2610658 | -2.36069 | -49.11472 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8401fe7-3587-34ec-b140-c58f4e7e04c1 | -2.09603 | -46.59398 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca00cd36-21ef-3b7e-8852-6dce23a48503 | -2.10157 | -46.58971 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2ef2f0d-e83d-383a-98fe-5b62e1ab4a99 | -4.00484 | -44.33766 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73ab77bd-3b4a-36d6-8218-ff8e7f8505f2 | -2.78684 | -48.56686 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 078b4209-5e5b-3ac0-ac48-f96617721dbc | -3.21783 | -42.0821 | 2024-11-16 04:01:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6352188e-ecae-3d49-8929-4147336ffe2a | -5.31793 | -35.49614 | 2024-11-16 04:01:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 274eb1e8-60c0-38d4-a3da-31cbee778433 | -2.77031 | -48.58149 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b91a6dd9-289f-326e-84ba-545e900d4e66 | -1.46361 | -48.19658 | 2024-11-16 04:01:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1250af-02bf-3363-99fc-e018906d2cfc | -4.13433 | -47.23721 | 2024-11-16 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b29f0304-8475-3063-b940-91abbac5ace5 | -4.18571 | -43.94342 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55576dfc-c9d8-3301-98c1-e29f25ebb377 | -4.18494 | -45.63406 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebe898e-e43e-3076-8231-d1b317556c05 | -5.29643 | -43.07224 | 2024-11-16 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 959180ca-2197-32c0-a92a-c80849042bab | -5.67911 | -35.65081 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2b4b7e1-76fa-39de-bcc2-f422169fd8ea | -3.2005 | -45.55054 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 8dbcfabf-c087-33c5-88cd-1802ea2beeb4 | -4.29522 | -48.06557 | 2024-11-16 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 280e9517-e8a8-37ab-91f8-e53f6d282918 | -6.17217 | -41.169 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa2d0e98-9467-358d-8dff-90edbb21572c | -4.90713 | -44.02573 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 776ee184-9933-3a87-8a2e-5031b563557a | -4.91018 | -44.03119 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ccd7204-7811-37aa-8df9-2bb9b6e3c34c | -2.03494 | -46.37526 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6a7e322-80b5-3021-b3e1-a2974b901ad1 | -5.66299 | -35.65319 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6d70f68a-048d-306b-a391-82b6b53409cf | -3.94095 | -46.40928 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b87fd1a-12de-3a8d-b2d7-49ac1e13ea25 | -4.37214 | -48.56788 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af0be8d8-3dda-38f6-8aab-3d6c48c1acd5 | -2.9035 | -40.12703 | 2024-11-16 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e33e219-7e28-3ddd-b4f0-dcd0244045d3 | -8.2862 | -45.97639 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4143e7b0-de5c-30f5-95ae-7a4af97d7e3a | -7.24825 | -46.7855 | 2024-11-16 04:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c76299e-5d86-345a-bb26-7f22e6fa3dcb | -12.69237 | -43.37637 | 2024-11-16 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 973cfcac-a7ba-3bac-91fd-8e1ff820a9c0 | -7.25267 | -46.78617 | 2024-11-16 04:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a610e3c-dabf-3af9-9257-580eb040d1bb | -10.69451 | -44.91123 | 2024-11-16 04:04:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cddc18ac-1459-310c-8517-5ed92fc45148 | -9.12395 | -44.42286 | 2024-11-16 04:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ccd6730-d00c-3fc7-b15d-1328d00516f4 | -8.28408 | -45.97128 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 454eed96-5672-3295-9fd3-4d270d425c59 | -8.27521 | -45.97382 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31863975-3e6a-3b1c-8f34-2ac41ca4df5c | -8.28686 | -45.97262 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c5cf94-7019-3c7d-8a7d-602a9bd39b57 | -15.64767 | -41.28482 | 2024-11-16 04:04:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| abd988dc-a21f-344a-b85f-ad1dbb4efac1 | -9.50159 | -43.18783 | 2024-11-16 04:04:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b7d93dc-c96f-31f4-9ca3-f28440111c41 | -8.27933 | -45.9744 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df75bcf1-6a72-3c01-a54f-f2a255648227 | -12.79227 | -42.3554 | 2024-11-16 04:04:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 058d6190-2e06-345a-b7ed-052296b6255d | -12.13625 | -43.48972 | 2024-11-16 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c750e615-8296-3eec-8283-076fe3d25be2 | -10.83393 | -44.45794 | 2024-11-16 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c83a5b2-6e12-3e40-b0b9-af1e46a2bfc3 | -8.27584 | -45.96999 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c76503-2335-3e71-8689-9d03ba5d7d46 | -8.28756 | -45.97574 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ffa5f2c-626d-3fbb-995b-e5faef5c5a86 | -15.64712 | -41.28846 | 2024-11-16 04:04:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2faa6a72-1050-343b-8d31-79710ded58a3 | -8.28345 | -45.97507 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff45d2f6-8975-30ca-8d84-5bb1e38155f4 | -10.54236 | -44.67776 | 2024-11-16 04:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de981c72-3948-3a17-892b-1de8b5053cf0 | -10.83324 | -44.46218 | 2024-11-16 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
