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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73b8603d-3c85-3c4a-b646-aa7fa280d4ce | -14.40381 | -52.50578 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9c03f3ee-9117-3414-820d-c64a9f8fb08d | -14.38739 | -52.54406 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8402de9-40dc-3f06-bfe0-0633f137ff79 | -15.84109 | -47.69086 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c38cd7df-d585-34fb-9299-b48ea8694a48 | -14.37997 | -52.5689 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b7f53f7-7686-36c3-9607-4ee823684d5d | -15.85239 | -47.69262 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff128399-29a8-3abe-9080-326c190779dc | -15.65927 | -45.91034 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d25b9248-545e-3b18-88ce-104647166595 | -14.39204 | -52.51497 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 772a2f59-571c-3eaf-90bc-350a089b29f2 | -14.2566 | -52.88331 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61a41fac-e4af-3b5b-b4e6-82735508c13b | -15.19103 | -46.22539 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d05d681-ba3c-3792-9c50-839c92cdf7a1 | -15.18386 | -46.24806 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87aefa92-28d0-3327-8d56-c6361b0a2bb8 | -15.67195 | -45.91146 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bc64da4-2a4d-38fd-9a2a-6958a254be38 | -13.40165 | -51.83364 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a72b9490-919b-3eff-b31c-be9cf64408fb | -15.75919 | -56.10018 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2cac2461-f8da-3f5a-be03-406e56563026 | -15.43658 | -52.70588 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79b4a1e6-470f-3f90-b9a4-e22651268d24 | -15.0323 | -52.76097 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b833bcd-b842-3365-b42f-981bc044dab5 | -15.59069 | -46.46376 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dee627a-e7b5-31bc-a8a1-1e21ebcef144 | -14.5785 | -53.61636 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdaeb01d-9a39-3b34-9737-8f8123dbf3de | -14.26828 | -52.89671 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed32ab7f-ead4-37ae-b66d-c7185e966fad | -13.45684 | -51.87176 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 132c7824-1dee-35e9-85e4-4344d03ad66e | -13.95653 | -54.39978 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97fd624f-b78f-33e5-950c-34a941efe94d | -14.97641 | -48.14234 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba59652d-fb4f-3278-86a1-dc42a80580ae | -15.25153 | -53.84224 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f0a5a76-864b-3a36-b284-c7cc72996ad2 | -13.46592 | -51.40421 | 2026-09-01 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18cbb6ef-3464-3cb3-92d7-0dfda45f7609 | -12.95226 | -45.96322 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 710252c8-4cad-3b14-b5f2-ca42b32aab5f | -14.72865 | -53.58167 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 904fdf10-c3de-3295-a853-9eeb0c30a2b5 | -14.26637 | -52.86593 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6ba0a5f-66f7-34a2-98ca-a6ae05861ecd | -15.01092 | -52.77272 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d913fb3-3fa6-3a9a-8cc3-3c4591d4fecf | -14.39931 | -52.51246 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70249e5e-827e-3ea4-8622-efe4eed1c38b | -15.1854 | -46.23642 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13d4c0ec-df2f-32aa-a45b-9e62dcab4eb2 | -16.60942 | -43.37317 | 2026-09-01 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a8f638-5fba-344a-8a06-13077c156801 | -11.47937 | -58.51507 | 2026-09-01 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6143e8af-1c53-3294-a73d-d31717d3486b | -14.71617 | -53.57174 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d2ddeaa-3d00-3ec9-8aee-23199f48b089 | -17.37611 | -42.38126 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adfaee6b-c725-3352-b5d8-f67fcd6acc2f | -13.27545 | -48.55041 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59526666-0ff5-300a-a5b5-c828206be914 | -17.19147 | -54.30847 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e6c42e9-8f07-3563-9ca0-6bd2d888daff | -17.90271 | -50.64312 | 2026-09-01 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3519cb4f-1ae4-334e-8861-f7e7cede4cf9 | -14.42029 | -52.50451 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a68c1df-a7f7-341e-9180-e66e9ea084be | -17.39146 | -42.35369 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f35baf92-f488-3601-9e93-c234e54f841f | -15.76686 | -56.10147 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| c0abb176-f282-3d49-a438-ac5424ecc22a | -14.58851 | -54.12024 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bca45ba8-1289-3596-bbd9-26182b98d0f1 | -13.44167 | -51.75274 | 2026-09-01 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8670df2-1edc-30cd-984e-04b6966c9e93 | -14.38913 | -52.53314 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62b73e4c-a80e-396d-abb3-19de479c1674 | -15.01545 | -52.76596 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66035116-c03f-33a8-aa0d-6858e403bf5d | -17.37258 | -44.87463 | 2026-09-01 04:42:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32e0010c-6dd4-33da-b3bf-c8237891a381 | -15.17568 | -46.24703 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 150a592a-f09b-3bf7-8349-09b71023f852 | -16.45034 | -51.40478 | 2026-09-01 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 027fcf27-de1d-3e94-b36d-8477da82346e | -14.27432 | -52.85966 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14bc6c3b-66b2-372e-b2fe-903ca8d2e860 | -16.35713 | -51.01536 | 2026-09-01 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e183b76-dcd8-30ef-9ee2-d99d03afc225 | -15.48928 | -56.01398 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c74a1772-be05-3721-8469-5e86da7de673 | -14.57261 | -54.08125 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 694d24d2-5e7a-345b-a612-ce406048d1d6 | -15.76774 | -56.09639 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 86afb8ed-10e0-3a34-9998-3a9aae7d01e1 | -15.0272 | -52.77126 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76825d82-1597-3fab-a5aa-91d45af26470 | -13.32692 | -51.72598 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8ad968d-4eb4-3a97-a0f8-2bbccf740a88 | -15.29903 | -53.84972 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 885e963e-9f7e-3167-ac07-613d4b644761 | -14.43366 | -52.50676 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1cf18da-fdb1-3956-bcfb-abc249fe0dde | -16.27864 | -49.02611 | 2026-09-01 04:42:00 | NOAA-21 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af42ba72-baa6-3839-b485-34c32e0c4245 | -16.3581 | -46.87658 | 2026-09-01 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1bd1d3-ffb5-34cc-90e2-74dd4b58f0ce | -17.88864 | -52.08297 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd51e2e6-f107-38e1-9973-348adf367bdd | -15.76779 | -56.08885 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f2a6ddcd-d4ae-38e1-8952-141b7a025dcd | -14.73146 | -53.58607 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37dd5c28-5046-3b96-9a56-ab6f1796443b | -15.23412 | -56.35775 | 2026-09-01 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba801611-62b0-3b8f-9fe1-d49358d07417 | -14.23253 | -52.85208 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fd69769-b1f9-341f-b99d-617f77e338e9 | -15.76856 | -56.0916 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ac39a7a3-3006-3f1c-9ccf-8eea5b721209 | -18.30288 | -45.08617 | 2026-09-01 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfe988e3-b029-3847-b49f-3b3665e643ad | -16.48448 | -47.95234 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f39172bb-888f-389b-81e3-aa8311c28141 | -14.13233 | -52.79755 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ff92207-f336-3359-b443-3ef4e35a0cf1 | -14.44369 | -52.50842 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c44d35f-59ad-3683-b77b-d8da15fce057 | -17.72277 | -49.23284 | 2026-09-01 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1324bb8-6f04-3681-bed2-83b182e6d5e5 | -15.64895 | -50.10871 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4be6b472-10b2-343f-bea8-fdf2e8fa3e78 | -16.44094 | -51.3995 | 2026-09-01 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d7d7f8-9f94-3eb2-9ef7-b5eb7428d54d | -14.45095 | -52.50595 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df026951-2495-3790-baff-05561e74e096 | -16.44647 | -51.40784 | 2026-09-01 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8ede6be-c0f1-363b-aeb2-43a63a3245dc | -14.5892 | -54.11619 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba5aa534-0b37-39ab-9006-78b3a8071ac3 | -14.27156 | -52.85538 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f864b3ec-2a74-374b-aacf-aa06151278d3 | -14.46532 | -52.52328 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 706d21c7-1bcc-3b18-b85f-61914659f02e | -15.0007 | -48.15479 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36413938-e105-3649-81b5-9c6fa98f82d2 | -19.39289 | -40.86588 | 2026-09-01 04:42:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 79fff576-bc54-378e-8226-fb6286aa4ca7 | -15.6342 | -56.37962 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c18b55ed-0c9c-328f-bab8-b24d9b0d76d6 | -15.6671 | -47.2661 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3f977b6-f818-35da-981a-31aee103d256 | -14.79216 | -48.25585 | 2026-09-01 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9b1b6a6-6d09-380d-a08e-d0a054be7a1d | -14.38579 | -52.53259 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77377422-742c-32e8-a75b-9a178f7dc6a6 | -13.47754 | -57.06589 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9ad0930-e824-361f-b5f1-6f9ba94635f0 | -17.88747 | -52.11243 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6687240e-1638-3efb-b896-1f9639853b48 | -15.65705 | -48.69638 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b839bf7f-ce7f-38ce-9038-059cd4e5a058 | -16.48137 | -47.9472 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 11bbb7bb-1d83-35d6-a2b8-1cd5b112593f | -15.30741 | -49.09801 | 2026-09-01 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9913efea-5b7c-3658-9ccc-c062834177a1 | -11.62904 | -54.56987 | 2026-09-01 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7c9551ce-ac2b-390d-a46b-a308654e9eb9 | -17.39001 | -42.35499 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc348c4f-f6a1-3638-87a5-509b46a77e69 | -15.87434 | -56.48151 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 53e9cc99-b80c-3a05-8ac9-761e221a4756 | -12.8816 | -45.84208 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84194acb-ab71-3582-98ed-3dc303262de6 | -17.49131 | -48.86937 | 2026-09-01 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6ebf125-6a07-30b0-acca-aac8515d5931 | -12.89584 | -45.82892 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a5fb05b-b92c-3b49-b04b-10a82f8ca054 | -13.82829 | -54.01525 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fdebb5d-b9e5-3e09-84f5-457d9ff10d80 | -15.62687 | -56.42038 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 442b764f-98ae-3cdd-b0f5-dc1bd46dca94 | -16.06587 | -52.17168 | 2026-09-01 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33bf81b6-ecf1-3490-9700-9a45706657e7 | -14.58569 | -54.1156 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3a46fc-3409-3697-94a8-58c2458f5e3b | -18.15187 | -49.59406 | 2026-09-01 04:42:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d65e7026-6301-37f5-bb32-9ec98661b8bf | -16.44758 | -51.40061 | 2026-09-01 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8271a779-b06f-369c-84f2-0e53f57d4013 | -15.84548 | -47.68686 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| abfd5c63-9546-362c-982a-dcbae810673d | -14.40831 | -52.49907 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README46.md)
