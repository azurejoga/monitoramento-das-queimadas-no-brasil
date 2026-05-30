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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 273e519b-1032-3ba4-a00b-d5cf2da84594 | -11.62769 | -56.86599 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a371fcb8-4cf0-3ea0-bfd2-9a52df8da029 | -10.7669 | -46.98248 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d88dc9de-250a-3494-8aab-bb0d1f7cfcc8 | -10.77948 | -48.5471 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7dfa535-4d52-3412-b774-86dd14c5e6bf | -18.24089 | -54.59475 | 2026-05-30 04:57:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 143ec126-35b0-31a2-8c0c-d47f12ccf4a5 | -18.4638 | -54.70673 | 2026-05-30 04:57:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfec173d-ecdb-35a0-ab12-b0636c8eb981 | -21.21035 | -48.54348 | 2026-05-30 04:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5fed06a4-8758-3b1f-85a5-d4481b7eec0f | -18.23756 | -54.59419 | 2026-05-30 04:57:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c11b88e1-a752-3680-80db-bfc6b1b693e6 | -15.82506 | -58.6092 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2552a2d8-6267-30a3-9fb1-ce565dd470ad | -15.82427 | -58.61377 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7494cb90-faea-31fd-929c-7618edee5226 | -20.62632 | -51.70269 | 2026-05-30 04:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1534bf0-af2e-3e21-85f8-c43fcea0962f | -18.97711 | -57.63663 | 2026-05-30 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| df0c1552-06fb-3a20-ab64-144f04c6f182 | -19.72459 | -54.65003 | 2026-05-30 04:57:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db3adc48-7b5b-3bdf-a888-8e5b3aa70abd | -15.80478 | -58.68138 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 16bbfa2a-80a3-3e17-a669-6b989f989517 | -21.80963 | -49.13199 | 2026-05-30 04:57:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e584ffba-f662-30e1-9d66-be3bc34c11cf | -16.16359 | -58.47479 | 2026-05-30 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7226e13a-2f97-3382-adb0-bfe26f0fffd4 | -18.46324 | -54.7104 | 2026-05-30 04:57:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b79265fc-327b-3eed-867c-706a7eb6a590 | -18.46048 | -54.70617 | 2026-05-30 04:57:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62633f7d-77a3-3ed9-8337-2b5c526a6cfd | -20.62568 | -51.7076 | 2026-05-30 04:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2da693b-46a0-3d7f-bfac-06d9203e5c2b | -15.42105 | -56.30995 | 2026-05-30 04:57:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8234ec34-1f3c-3cd6-b9e3-670de7badea6 | -15.82215 | -58.60395 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5e414561-4b6c-3f44-b538-5475b153ceca | -15.78486 | -58.66333 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 040b09b6-123a-3242-828e-4f0b5a536039 | -15.82585 | -58.60466 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c673ef45-1944-3d58-9197-ed526cedb9ff | -15.78114 | -58.66263 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2e53aa26-4a10-336d-af60-37a401b80bf7 | -15.79959 | -58.62328 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c961b504-3cae-3966-acae-df469e70c5aa | -15.78567 | -58.65874 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 14e65d67-8cf7-39b7-b679-94468c294431 | -18.45991 | -54.70984 | 2026-05-30 04:57:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 634afc2c-10a0-35ef-807e-6b1c0a3a3c41 | -16.16281 | -58.47929 | 2026-05-30 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3cfe52d4-118b-383c-a8f4-c465b4c7fe27 | -16.16648 | -58.47997 | 2026-05-30 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ffd6620a-2f9f-398c-bbef-22deef6e78b9 | -15.82346 | -58.61839 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6e6ee7f1-41f8-394a-a708-1d2da6646cd4 | -19.72402 | -54.65378 | 2026-05-30 04:57:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1de4d8ce-56c0-354c-8105-b9acdac9fb8d | -16.15914 | -58.4786 | 2026-05-30 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 63ed19b0-8e55-322c-8212-371fe4af2b5e | -16.17171 | -58.47166 | 2026-05-30 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2f43e0a3-c1f3-3c36-8643-f36da7bdad2a | -15.90551 | -50.55288 | 2026-05-30 04:57:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144f07f4-2a9e-31cd-b742-4d1933461c7d | -21.21242 | -48.54219 | 2026-05-30 04:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e6000ab-97a0-39db-889f-baa67ce5cc5c | -22.3818 | -49.78649 | 2026-05-30 04:57:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c08d699a-691e-3d5d-9879-67e5da133d80 | -15.80559 | -58.67678 | 2026-05-30 04:57:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aa1824ef-f9ae-35be-9296-94e27e0c9271 | -21.29998 | -48.58582 | 2026-05-30 04:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 82e29b5c-7049-35b3-aad6-c6dd5aed4a15 | -21.29535 | -48.58511 | 2026-05-30 04:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 35830082-5e15-3c45-b8ef-aeffa15672a9 | -10.7614 | -46.9529 | 2026-05-30 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e3799105-6a78-3ccb-a742-8bd47e05beff | -14.13003 | -58.94706 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5062f79e-4f79-3537-a1e3-41975bbaa22d | -14.1274 | -58.95265 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2dc90b14-dddd-3bf4-bc0b-62f4b50f1329 | -14.12516 | -58.94632 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bb61021d-b512-3436-af49-4aa70f3c430b | -14.1349 | -58.9313 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae62a07f-80d8-329d-a113-0f09841b3b7c | -14.13213 | -58.93048 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6266a26f-ba27-3763-a226-dbf14626ebd3 | -14.12872 | -58.94154 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 20278a74-b68e-35d4-8bd7-5471eb48fde8 | -14.12805 | -58.94714 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 313890e4-630b-3a0b-b40e-e99d90769241 | -11.80383 | -57.00987 | 2026-05-30 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 623bbd2b-cce7-36e3-87e3-08b060f4b220 | -9.25225 | -60.33184 | 2026-05-30 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0817e611-5d5c-351d-968f-7cd88be0b0b6 | -14.13144 | -58.93593 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 15ccd00e-ffe1-34cc-b4f0-e312552c54fc | -14.12933 | -58.95255 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 983fba9a-cfb6-3628-a0a9-e57d18b398f9 | -11.80424 | -57.00642 | 2026-05-30 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4339425-ac5a-3f55-8491-573b88179691 | -12.71855 | -54.19596 | 2026-05-30 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f71e24c7-bab1-3cf2-a8bf-0f86235a971e | -12.71917 | -54.19039 | 2026-05-30 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86e347ef-56b6-398c-b671-f4f90692f6a5 | -14.12938 | -58.93597 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1a281cb1-b078-3367-91d8-e003ecd2b0ab | -9.25171 | -60.33566 | 2026-05-30 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d62f8cde-3b06-3464-9c57-79e970b20850 | -14.13425 | -58.93678 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ce37d69-6fdd-3bce-a464-9e17d2cd42e0 | -14.13073 | -58.94149 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7cce1fb4-5d8d-3501-8374-4f25f3a863b8 | -14.12446 | -58.95187 | 2026-05-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bd3fc436-0cd5-3cd9-8a24-d276d7c06f68 | -9.93499 | -65.00421 | 2026-05-30 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10feeaac-618e-39dc-aaa8-8783cad136e7 | -15.78493 | -58.66426 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 197c97b2-ceba-3bd8-87c6-77599607ac23 | -15.78528 | -58.66115 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| befac8a7-736d-367a-9827-6fbf8bb40f03 | -16.16293 | -58.47843 | 2026-05-30 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3990967f-ad4d-30ba-84be-7e99fd252b56 | -15.78563 | -58.65801 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 355889dd-5ffd-3ebf-a3df-29f9c0a3765c | -15.82669 | -58.61612 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 18126c8b-65c0-3a54-9226-1737e90d9cf1 | -15.82778 | -58.60672 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 24a1e56c-0648-33e4-9112-9a9ee61bd3a9 | -15.82741 | -58.6099 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c070109c-b5cb-36fa-97c3-3275e0f61388 | -16.17402 | -58.47345 | 2026-05-30 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8e9d74be-cb16-3577-992a-ce881c06dd46 | -15.82705 | -58.61304 | 2026-05-30 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f514e903-f951-3874-a60c-3324335e92a5 | -16.17439 | -58.47025 | 2026-05-30 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cc5ba854-bdd0-32d6-b170-f0d0a2ef6e30 | -18.46045 | -54.71119 | 2026-05-30 05:46:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 963ff7f0-6cb4-360e-bee5-f7a0e0cea623 | -16.16811 | -58.47915 | 2026-05-30 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8b4f9e64-ec73-3450-97fd-cca797872a76 | -9.64054 | -67.21541 | 2026-05-30 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1124b9af-57a9-3908-84b3-a90a5eb3e8bf | -7.33674 | -49.8531 | 2026-05-30 06:50:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3701ee90-4749-357a-8c79-6ea4a99d205c | -10.75399 | -46.93956 | 2026-05-30 06:52:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c5ef618d-0313-3637-a13d-e36462c872b8 | -10.76657 | -46.94128 | 2026-05-30 06:52:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5469ce31-b560-3a82-9643-7a52ebae58bc | -11.57922 | -47.45099 | 2026-05-30 06:52:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 9179aa9f-31b9-3a46-9ec4-43403d147b78 | -10.79178 | -46.94428 | 2026-05-30 06:52:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4d3c9487-ff0d-36c8-bc38-3b8828da3121 | -11.58856 | -47.44505 | 2026-05-30 06:52:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 239fe6c8-c0bf-308f-8468-1b17702ea56e | -10.78931 | -46.96325 | 2026-05-30 06:52:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| befc7b15-7762-3139-8f36-82470861807b | -10.63193 | -48.32011 | 2026-05-30 06:52:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 032f4803-863f-31f1-abfc-ade0ccee0cc6 | -10.8379 | -46.921 | 2026-05-30 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4f668a95-0d10-3c6e-b9d1-d7392b11d6af | -5.80087 | -45.12356 | 2026-05-30 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 65cc91d7-7cab-3d48-9fef-5555ca7070ad | -10.05586 | -49.10961 | 2026-05-30 12:14:00 | TERRA_M-T | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7c17bbf9-574f-3ec0-8089-353d5675596a | -10.78494 | -46.93001 | 2026-05-30 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2b15c942-b00f-37af-b09d-345304f69960 | -7.83832 | -46.25162 | 2026-05-30 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 922bcb91-1fb9-3c59-b77a-a76a6a035f25 | -11.5879 | -47.44899 | 2026-05-30 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 092bbbdf-d75d-3f29-bc00-ed716b83de1f | -10.78066 | -46.96439 | 2026-05-30 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 55555f26-5314-3d9d-88bd-48bc02026269 | -10.40061 | -52.54353 | 2026-05-30 12:14:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a0d368e2-7968-3108-83ed-e5d2e445de0a | -11.27412 | -53.96404 | 2026-05-30 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dff6fc29-7168-388b-b33a-c84718e37b4d | -6.11773 | -44.69462 | 2026-05-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| f22382f1-4e9e-398e-adce-36e3e9709957 | -6.75627 | -45.01554 | 2026-05-30 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8c05a072-c404-3d30-815f-b297f211df1b | -6.99981 | -42.88366 | 2026-05-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 0619b3d5-2221-3800-8c01-7f4c81a10fe3 | -11.5919 | -47.44364 | 2026-05-30 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8cdac8ab-7806-3450-b2c7-f0d35e576a15 | -11.1682 | -46.78876 | 2026-05-30 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fd991f47-e2d1-3563-aa28-2cb198720bf0 | -10.39934 | -52.55243 | 2026-05-30 12:14:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 09dcd8eb-9678-32cb-9536-cd4a3835a883 | -10.39053 | -52.55117 | 2026-05-30 12:14:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4d0388b5-35aa-39af-812d-efed09ffd05c | -10.7828 | -46.9472 | 2026-05-30 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 7938b174-4738-3439-b34f-c02b9727e56d | -11.62535 | -55.18361 | 2026-05-30 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 05ccdbe5-f279-3dc3-a3c1-ef3883117a4b | -10.40815 | -52.55369 | 2026-05-30 12:14:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4feff48-88e3-35ec-9e11-68e57ad5b0c9 | -7.85045 | -46.25304 | 2026-05-30 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |


[Clique aqui para ver as próximas entradas](README11.md)
