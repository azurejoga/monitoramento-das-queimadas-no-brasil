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
| 639edfa7-1357-3e17-bc85-4746f3e105ec | -5.52967 | -35.52243 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4943f66b-d0f0-3f61-b49c-84d58a1ce942 | -5.53372 | -35.51514 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37b79bc8-411a-3e11-8537-04d4eb1fdd0f | -5.51515 | -35.59221 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 28f3df47-f588-3e79-965d-5baa7104a8a3 | -5.53038 | -35.51772 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8f1319c-ebb3-3172-a3df-0d25f656a7ec | -8.32002 | -40.60233 | 2026-03-27 04:02:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aec71fa8-79a3-397a-9f8c-49cf7eea387c | -5.44814 | -36.78902 | 2026-03-27 04:02:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a75f1481-5432-3120-9625-4b9b477d96b8 | -3.91664 | -40.73344 | 2026-03-27 04:02:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96e20920-f12c-3f0e-b8cd-c11efcf1ec92 | -5.44458 | -36.78848 | 2026-03-27 04:02:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d201a30-6814-3e9f-bfc0-9eee22b8a0a7 | -5.53348 | -35.52304 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0dbac67e-b3fa-3ecd-8dcd-ea3e0d904f7f | -9.60199 | -37.60813 | 2026-03-27 04:02:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dbdee3bc-7c7b-3324-8086-f3227decdd8c | -4.97007 | -37.40573 | 2026-03-27 04:02:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ae6594ff-a595-3f02-acd6-be38d775e647 | -5.53303 | -35.51988 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 957ec11f-30ea-3449-b133-b309b082d2b9 | -5.53234 | -35.5246 | 2026-03-27 04:02:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4656ad32-5430-3b12-a21d-6ab6fb9312ab | -12.21018 | -38.98356 | 2026-03-27 04:04:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd25528a-3311-3710-a416-8be2866673b0 | -11.89066 | -38.0974 | 2026-03-27 04:04:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d735fbaf-9a42-3b05-979b-d958f2dc777d | -18.64306 | -45.03062 | 2026-03-27 04:06:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ff20cc5-ec82-3c80-be07-1bfc1f1cb8a2 | -22.17805 | -43.13905 | 2026-03-27 04:06:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 640e5f97-a3a9-3ccb-bad6-6bbd8df909d4 | -22.93667 | -44.09321 | 2026-03-27 04:06:00 | NOAA-21 | MANGARATIBA | RIO DE JANEIRO | Brasil | 3302601 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| acff3e71-5f35-324a-bec6-2d9c18a529c8 | -21.71532 | -48.43648 | 2026-03-27 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdd93a55-c382-3e0d-9c64-f5df3002b7da | -22.26744 | -48.47146 | 2026-03-27 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db63ef00-4e8d-37a4-a345-5158b81673ce | -22.87379 | -43.47555 | 2026-03-27 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 48dbb93d-22c6-3ea8-a9de-893aaefc51d8 | -22.93824 | -43.38643 | 2026-03-27 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2bae83e-5c3a-304b-9b1e-c95be19765ea | -19.37567 | -39.83286 | 2026-03-27 04:06:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a2eaf9f8-3d26-3c8b-8b83-574da9ea198c | -23.03909 | -47.87904 | 2026-03-27 04:08:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c56a1128-d4d9-3231-ba7a-5a46f5afe9de | -23.04003 | -47.88266 | 2026-03-27 04:08:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e48431ad-968e-3e49-95d1-05bafd6d4e69 | -23.7879 | -49.04725 | 2026-03-27 04:08:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cd96b68-2fa0-30e8-a785-25eab4dd0e32 | -27.45618 | -48.45274 | 2026-03-27 04:08:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13ff020a-ccea-3300-bf69-4fda675d96c5 | -30.03827 | -50.16491 | 2026-03-27 04:08:00 | NOAA-21 | TRAMANDAÍ | RIO GRANDE DO SUL | Brasil | 4321600 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| af7d680b-0f7c-3d27-98c1-09c2c0e4a46f | -26.45903 | -51.51153 | 2026-03-27 04:08:00 | NOAA-21 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a13ba789-a049-38f5-aaaa-eb9273b3bb44 | -1.62357 | -54.60713 | 2026-03-27 04:32:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62b011d0-5ba9-35fc-aad0-2911a822c2a8 | -1.62414 | -54.60368 | 2026-03-27 04:32:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 263336a0-e9d2-3f86-8c76-9c5db7f22a07 | -5.52985 | -35.51618 | 2026-03-27 04:32:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 377c0f5a-92f0-302c-86c1-ba37971d0dc3 | -4.97091 | -37.40551 | 2026-03-27 04:32:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7c382782-2062-3bbb-83a4-114b0b6717a9 | -5.52924 | -35.52039 | 2026-03-27 04:32:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e255db6e-478c-384c-8d8e-66edf7ec5c37 | -3.50424 | -48.03782 | 2026-03-27 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ed0caa3-49a8-3b02-af04-add369c1c896 | -5.44551 | -36.79031 | 2026-03-27 04:32:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9fcb78e-49f7-31f4-b24c-eabf6a9f57fa | -4.96576 | -37.40472 | 2026-03-27 04:32:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ba5422e-b9e0-318d-9765-9285236c0549 | -5.44692 | -36.78999 | 2026-03-27 04:32:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a62ccdda-dcd7-3d5f-b0a2-c94dc6c322e9 | -13.75589 | -43.2786 | 2026-03-27 04:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30722e7d-a006-302c-b1e2-9b19f2fd5bd6 | -13.75729 | -43.27745 | 2026-03-27 04:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2772bd7a-2671-3e2d-bf78-13f370f6a845 | -18.63987 | -45.03126 | 2026-03-27 04:36:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3447d5f4-e53d-3ead-9394-91b78232870b | -27.5388 | -48.70467 | 2026-03-27 04:38:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b7cf225-66ac-3d90-a00e-db75de06a784 | -23.78609 | -49.04554 | 2026-03-27 04:38:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a90fb31b-2522-3b70-a2b2-3e7f7236e51d | -26.46139 | -51.51181 | 2026-03-27 04:38:00 | NPP-375D | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d997369a-ade0-3ae9-b323-f986605ce1ef | -22.53154 | -53.90363 | 2026-03-27 04:38:00 | NPP-375D | NOVO HORIZONTE DO SUL | MATO GROSSO DO SUL | Brasil | 5006259 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d6f73f5-eb48-3958-9af1-46e082c5d851 | -23.02431 | -48.45061 | 2026-03-27 04:38:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3a611a2-2306-3623-a6a1-ae1461db853a | -27.31059 | -49.30065 | 2026-03-27 04:38:00 | NPP-375D | VIDAL RAMOS | SANTA CATARINA | Brasil | 4219200 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0855ea89-9f7a-30b6-a35a-54cb1492e27f | -23.35119 | -48.73654 | 2026-03-27 04:38:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9035643e-fe1f-365e-ad8c-888131ad8654 | -22.17703 | -43.13891 | 2026-03-27 04:38:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f00d8a5-2dc2-3b34-96e4-d35da55f1933 | -22.2655 | -48.47173 | 2026-03-27 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20432b1b-5649-339d-9d4a-467bcd348607 | -23.37477 | -47.31273 | 2026-03-27 04:38:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd7ac2f3-8ab4-3e59-abca-c1a6921dcd81 | -23.78946 | -49.04615 | 2026-03-27 04:38:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fac32adc-9b2e-3d16-8254-8c39dfe297ac | -27.53884 | -48.70268 | 2026-03-27 04:38:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c4909252-4f96-309b-9f18-2ceb56eb84bc | -21.71323 | -48.43614 | 2026-03-27 04:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5345b2cc-70d7-3185-906c-aceabab88e30 | -30.03971 | -50.1673 | 2026-03-27 04:40:00 | NPP-375D | TRAMANDAÍ | RIO GRANDE DO SUL | Brasil | 4321600 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 4719c326-cf21-345a-b9da-e390b1d82ba6 | -30.04032 | -50.16309 | 2026-03-27 04:40:00 | NPP-375D | TRAMANDAÍ | RIO GRANDE DO SUL | Brasil | 4321600 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 7ef82349-8cc8-3793-ba7a-a73794a5d391 | -1.67367 | -54.46115 | 2026-03-27 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 637a3673-b0fa-3a8a-8562-da0e927532cc | -1.27336 | -53.5765 | 2026-03-27 04:51:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bad5c932-3aa3-3fb8-8288-9ec0bc75fa78 | -1.26994 | -53.57594 | 2026-03-27 04:51:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5330c098-10c0-33ee-9892-6649d48e86d0 | -1.2891 | -53.10356 | 2026-03-27 04:51:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dae7daa-cc5c-3e5b-a8fa-d43a6c7ee6cc | -1.27052 | -53.57224 | 2026-03-27 04:51:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b35e62e2-f7fc-3687-a600-4f1c52452736 | -1.62255 | -54.28257 | 2026-03-27 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dce664e1-9033-3d15-876c-9de6e5f2491d | -1.83525 | -54.23895 | 2026-03-27 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 893f8599-ef59-3cba-a40f-29e603226c7e | -1.62222 | -54.60163 | 2026-03-27 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54441d7f-66b5-3b2c-8010-0004aa792e5d | -1.62157 | -54.60567 | 2026-03-27 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe7ba383-52b3-3768-a10d-f464f707efba | -23.37343 | -47.30991 | 2026-03-27 04:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08424512-6d65-317b-8055-e056bb4800c4 | -20.44367 | -53.7737 | 2026-03-27 04:57:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e4f489c-de10-3977-8e55-f879aa172663 | -23.78943 | -49.04707 | 2026-03-27 04:57:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c87c85e-f11b-3a7f-89f5-68e8555a0ea9 | -23.02533 | -48.44976 | 2026-03-27 04:57:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5601cf4c-6c36-3dfc-aa10-2ac0e49e2c8b | -22.53197 | -53.90124 | 2026-03-27 04:57:00 | NOAA-20 | NOVO HORIZONTE DO SUL | MATO GROSSO DO SUL | Brasil | 5006259 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1849842c-fa55-3c4f-bf52-7d0855d70d8f | -23.78715 | -49.04352 | 2026-03-27 04:57:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6dcd612-b645-357b-9c81-9c50e3f51317 | -26.46112 | -51.50885 | 2026-03-27 04:59:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f2c9f1e-68b2-3fec-8473-da9f7937c060 | -26.46063 | -51.51302 | 2026-03-27 04:59:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85c6f4b1-98ed-36a2-bde9-8f87dcf2f7dc | -4.96455 | -37.40791 | 2026-03-27 05:29:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 27d69cb1-eb6a-3397-b5d8-b052a8a568f8 | -4.96645 | -37.39594 | 2026-03-27 05:29:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f0cc34b1-cbc5-3724-a93a-478a9f25b526 | 4.46624 | -60.61755 | 2026-03-27 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787e6707-99e0-3372-9f69-f2e3b07fe44a | -1.27382 | -53.57416 | 2026-03-27 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0273553b-bf28-3680-a7d2-53e5f2513c2e | -8.85021 | -44.17663 | 2026-03-27 11:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0013cfac-1fb6-3614-af0a-22315e48f767 | -7.02972 | -35.74577 | 2026-03-27 11:28:00 | TERRA_M-M | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 17117354-e9b7-3a3c-bf20-13fa8acbe7ea | -8.86454 | -44.16195 | 2026-03-27 11:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 65770eb0-93e4-3fe0-853a-3aba999e8495 | -8.85287 | -44.16003 | 2026-03-27 11:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| aa483d4c-dee0-3d09-b30e-e53279de8730 | -7.02658 | -35.7393 | 2026-03-27 11:28:00 | TERRA_M-M | ALAGOA NOVA | PARAÍBA | Brasil | 2500403 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 07f4ec27-70db-3919-a8e3-827d0770926c | -13.56879 | -42.55618 | 2026-03-27 11:30:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 594c45b2-396e-3b7e-804f-9b58e78f38a8 | -4.39481 | -59.59267 | 2026-03-27 13:04:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ebe16ed-d80c-3e22-8e8a-a8bbc84be2d0 | -2.82513 | -57.69876 | 2026-03-27 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 336dea71-5b69-30c0-b3cc-d49deace1be6 | -19.601 | -40.0608 | 2026-03-27 13:30:00 | GOES-19 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 138.1 |
| 4c180053-2b76-3687-b290-fe2fc5c69021 | -19.601 | -40.0608 | 2026-03-27 13:40:00 | GOES-19 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 195.5 |
| 79822dba-1c71-3e20-b27c-0d0450895170 | -19.601 | -40.0608 | 2026-03-27 13:50:00 | GOES-19 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 163.2 |
| b41b2c44-7c00-3941-a835-90f1c8881131 | -19.601 | -40.0608 | 2026-03-27 14:00:00 | GOES-19 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 287.7 |
| f526fadd-0759-35e8-ad12-b59b2ad29c1f | -19.601 | -40.0608 | 2026-03-27 14:10:00 | GOES-19 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 263.8 |


