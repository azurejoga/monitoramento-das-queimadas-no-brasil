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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8710dde1-5ae6-3e81-a70f-b2d911d8a5fb | -6.82096 | -51.89307 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0b3526e-faf5-36fe-b66e-90dd8cb9713c | -11.24253 | -49.41135 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98d635b1-edff-37d8-9639-e1cbf742ebcf | -7.43705 | -44.98233 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d59258f-d5c9-3ab6-917f-89a1638ef5fa | -8.08281 | -50.18682 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5352cd78-52ca-3a45-a6c5-c7dc4ad0ca14 | -11.686 | -46.60548 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b8e96d-51a2-31ab-a0e3-c092dad596a5 | -8.8971 | -49.93623 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a7d6665a-74b6-3606-ba3e-8dd0bdc4ec9b | -10.23561 | -48.93839 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd3ddcb6-0d4f-3906-8325-196564029033 | -9.04342 | -47.04737 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49aa82fc-9e75-37f6-b749-653a8b00a756 | -11.67764 | -46.57125 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77496a23-d59f-348c-a641-172feeaf572c | -7.72205 | -50.35378 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f32aaf-199a-3b0d-9138-38bdda9ee4bf | -11.53895 | -50.40811 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ddb8f678-22af-3d38-9fb9-a765fcc41753 | -8.49393 | -47.27697 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c683a6-22cd-38ee-9c06-508cff59d8f1 | -9.64538 | -48.06275 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 016e6700-032f-39c5-813e-c331a2442f4a | -11.53539 | -50.40749 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 74033df6-6136-3636-ad13-54deecbbd5a2 | -8.54939 | -48.95265 | 2025-09-12 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2f9e6bb9-1721-3023-8507-ed4fef0d2efd | -10.20425 | -48.16068 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5587b659-ffa3-3af5-b618-4c524c0f5cfb | -7.23008 | -43.9853 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67389959-7793-3620-9250-85cb7f2e8e78 | -12.00664 | -47.7667 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42ba8788-fbad-3618-81b6-ae5fc6a1cfff | -9.11348 | -47.11933 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 527e53b9-075d-3463-98f8-c457f9138e61 | -10.35819 | -57.48653 | 2025-09-12 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e774162-7107-3407-bb96-7f9d62f5387a | -6.83609 | -45.62104 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b96a4edd-bfbc-3f90-96bf-4be4dd33bafe | -9.77739 | -47.85861 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2817e12-0bcb-354d-b17c-e7560f115f35 | -11.09403 | -48.42072 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83ef69d9-cc5c-3ad5-ba8c-5aa3441fc550 | -11.70093 | -46.53112 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb21e4f-f4a7-3285-8f58-0169d9104051 | -8.48122 | -47.27135 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1352844-4185-3cac-8f39-a1f32ea7c0a0 | -5.81913 | -52.33159 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5546843-a652-352a-82a2-7104e2918f87 | -11.18246 | -48.62318 | 2025-09-12 04:25:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 989dade8-0f8a-3403-baeb-c8c4f2204236 | -11.47861 | -49.27594 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bb5ad4e-1c59-3bcd-8092-fa9d131a27e9 | -11.6749 | -46.61096 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f9fa0f9-9014-31ad-a6a2-a8ad91ad12b7 | -8.43612 | -47.25702 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acece4de-0546-3998-861f-3ec666a23ab5 | -9.83739 | -54.53749 | 2025-09-12 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72d2b68e-b764-3a91-bce1-65695a59b4fa | -6.45448 | -44.04149 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d795b29-f480-3279-9937-fc7eb98d8c3a | -9.02075 | -45.74002 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c3976e-3c8d-3340-af31-e9cd3a0c5501 | -7.32339 | -44.37497 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5ad3487-78b8-356d-b053-371b24e10c86 | -11.43582 | -49.28028 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5414f36b-4198-3415-a39b-76aeba987866 | -11.19666 | -48.41536 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b93e3c7-b229-3533-aee6-14adbbf2a375 | -10.3543 | -50.52423 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8c3e2a3a-ebb2-3713-9746-a143a9c5df6e | -7.4874 | -54.94685 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4afe099e-e202-3f94-9bb4-27d11133f3ba | -6.40814 | -45.13952 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ea92c23-f903-3669-a34e-444fa9cf5a98 | -9.05831 | -47.03903 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f55f12e-8517-3b1c-860f-9352bfce786a | -9.08196 | -46.95372 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be3d8c1-1f71-3bbd-bb48-0eddc97ccd45 | -6.5973 | -44.31656 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 901ce044-d7ca-336a-9b99-8e701c001b2a | -3.80807 | -51.1395 | 2025-09-12 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3ed0a72-f3ce-3f3a-a76b-cad0b54b6586 | -8.38088 | -47.60439 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 803aa683-8685-371d-aa34-b18a5abf6373 | -8.18992 | -47.13859 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfcb5d17-b250-342d-84e6-2f4475e972d6 | -11.68262 | -46.56108 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ac85d47-de16-3cb9-98e8-426e50077722 | -9.03624 | -47.09266 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e96cd166-5ff0-354e-aee7-5484f432c08b | -10.19213 | -46.19255 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916e1b16-9737-3b04-af3e-c6a018fe5a30 | -10.34848 | -50.53646 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 551b238a-bd45-30ad-8ecc-cdb35c85b0ce | -8.15876 | -46.1078 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73d17efd-89f2-3c0f-af73-1e0c66a3effe | -8.69677 | -54.69294 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2797cf7e-2da3-3ee3-b8fc-e14004a8ce6e | -6.32353 | -42.22395 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 137098d9-7cd3-37af-a169-24123dd76dd7 | -9.98644 | -51.70963 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094f190f-faf0-3997-9121-b06e47663c36 | -7.24304 | -44.42051 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0c22f16-2f37-30c6-8d5b-9033dcb87e22 | -10.08502 | -47.16083 | 2025-09-12 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a824fe0-beef-3639-a636-d81128dd2e69 | -6.30807 | -42.22431 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9554bfb-1e85-3a63-bc87-1d454ae031c9 | -6.16956 | -53.50397 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 106c2a45-de1d-37b0-a81d-d5bb56d79ca8 | -5.29092 | -48.13288 | 2025-09-12 04:25:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20ff635-f0ab-372f-acea-ebeaa1388691 | -9.0776 | -47.00288 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d9387e5-ebba-3400-adf2-45e0fdfda114 | -4.90235 | -56.04026 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 384e3fa3-b952-3b0d-91c6-277f04ec563b | -6.3057 | -42.21445 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54573363-beba-34d9-b8a2-bd3b62938c5c | -8.20098 | -47.13317 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9611d0d3-5db6-34b3-9023-d08472a14bb1 | -6.52894 | -44.6017 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5edf2ce-f643-3d5e-a937-6d990ae76caf | -7.9802 | -43.66331 | 2025-09-12 04:25:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0aa6681-07cc-3996-bfaa-98d5cdfa35be | -11.69704 | -46.53417 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 335bd087-a3bc-3ff6-9bc5-2f7e455acc0d | -7.23117 | -55.06515 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4d5019f-3322-3e2e-ac10-1d0a9b59c513 | -9.06429 | -50.50214 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0eb227d-41d9-34b9-ac56-f10a0547d8bf | -5.64182 | -51.86668 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f13f2c7-ecec-30c4-bbbe-d03faae3b589 | -6.10023 | -45.93988 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86bc76e4-3469-336b-9820-31ea270c6310 | -7.22766 | -55.05507 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c8b7b4-00b1-3821-b2f4-85d84cac21bd | -7.12548 | -44.5024 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dff1f2f-6360-34e3-af35-f9312530bc7c | -8.64024 | -45.71775 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9ce5202-fa51-36c9-9bad-3237a0010d92 | -11.67931 | -46.58249 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dc8ab84-eb41-3a27-96dc-6be6ee63dcf9 | -7.17686 | -44.87155 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 529ce41a-1a62-3eeb-8226-755a24e9f4cb | -11.56762 | -43.2387 | 2025-09-12 04:25:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cb542c3-1cd1-32cb-9cc8-3509df365271 | -10.34993 | -50.52789 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81e413f5-343f-3986-ad86-7acbd9c7a8ce | -11.09577 | -48.40985 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 706ca398-5c03-36e8-9c9a-bd627fc9c741 | -6.10409 | -45.93694 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e2280c7-8276-36da-a943-94a4992465ad | -10.55998 | -43.66469 | 2025-09-12 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6c7b1ef-e1f8-3054-b1e0-bdf63d244423 | -8.94591 | -46.71772 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e690e412-2507-3627-bab0-bac12c486388 | -11.18929 | -48.43991 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb230826-5b3b-3ac7-8326-2daf202c5c70 | -11.68212 | -46.60849 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f4d8f15-e3fc-3d52-9a6e-d089ebe01abd | -10.90086 | -47.24171 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c36719e-15cb-396a-865e-736a72245a45 | -8.05884 | -52.32266 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1281e1b7-2bcd-332e-ae21-a25b634c5a9e | -8.42617 | -47.25543 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dce89a2c-3811-37c6-bd75-d88efd598cd1 | -8.89111 | -49.94096 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9356de73-77d2-38af-9b47-48acbf4c5a1f | -7.55451 | -44.39788 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05267508-9ced-3160-96b2-80f0324bb3ca | -6.83692 | -47.87323 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ff3017b-3bbb-3ce5-a09b-eb333ed908ce | -9.34379 | -48.94391 | 2025-09-12 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c63ab01-dd71-327a-8c0c-f518df142b71 | -8.35862 | -47.61528 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92e86972-d447-3957-b9f8-5263026767e3 | -7.51619 | -55.01909 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a65f948-2616-3f87-8697-147e6e282c79 | -4.53292 | -55.68718 | 2025-09-12 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c745e185-6270-3e07-84c6-00de8df10fd8 | -4.3943 | -48.91847 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 814f9450-b039-3eb9-a3e4-9e1a5d5a1ddb | -4.48491 | -48.1122 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17447992-2e5c-370f-a323-b04697845e7f | -9.95784 | -51.68857 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4b490b1-9299-35be-898b-755d0c6d8409 | -9.71055 | -46.90769 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddd02c51-fb20-396c-ad0c-c7e4d1cf296f | -10.36019 | -57.48583 | 2025-09-12 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9293a6bd-54a4-31d1-8ffc-2d5775fa2dd6 | -8.36244 | -44.83628 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac0483cb-0cc7-3791-8831-f51191cc557a | -5.53865 | -46.42101 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0b8026b-0451-3591-a40f-de79733bab84 | -4.92885 | -55.78543 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
