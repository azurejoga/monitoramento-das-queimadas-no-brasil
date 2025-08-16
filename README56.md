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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c812a583-f081-3fbb-a85f-9cdbeb83378b | -7.92906 | -61.74128 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fecf8e7-8fe3-3e04-88eb-72ee3813117a | -8.96966 | -61.67926 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 820a281f-1565-385f-9588-8458743fbade | -10.01052 | -59.22292 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab208ab2-c519-36d3-b688-044d11b979c2 | -7.91191 | -61.74216 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba924f2d-cccd-37aa-a44f-6f57f8749e8f | -2.37999 | -47.66182 | 2025-08-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1082e6d-09e3-3383-9ed5-8fa53a1be6fd | -7.53117 | -61.33108 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ed85b8b-bc91-3bff-bfb1-d5db6bd3c7d2 | -8.99672 | -60.50091 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c90ab754-6b96-3c75-b49f-ba37caa83cc1 | -8.81293 | -52.04038 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e729e596-ba91-3550-8ee1-c0f81b14c40f | -6.63477 | -60.01364 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2a6c88f-f548-354c-b879-15eb38be70ab | -8.66239 | -62.45669 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57fdc997-d6de-3578-96a7-0ba2577bca68 | -6.93139 | -60.07432 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bfcfb2ef-7770-3714-a767-9139d48a2c00 | -8.98464 | -60.53506 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f5f42abf-1b92-318e-ae48-b6bdf3e02a87 | -9.06193 | -58.94746 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46fb965d-c128-3ac8-b141-ddea6bbac095 | -7.6909 | -63.32051 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91ca059b-3aa7-373b-b4da-e18617520ef1 | -8.90186 | -60.74109 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a348651e-8397-361d-8555-c78364b1f038 | -8.98402 | -60.51696 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8426431f-6485-3779-ad02-c2392f91c97e | -7.61695 | -63.32444 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9a8158-7bce-32a2-8e40-101a3145e5e0 | -6.94417 | -59.52631 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c4eea16-5e85-3b60-a62e-d1639b0c8320 | -7.07743 | -59.2285 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18c180b9-9fc6-32c1-90db-65d7e1fa07df | -8.99848 | -60.53364 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 566a9f04-0480-32b3-9e4d-e69efd28b6cf | -9.39418 | -60.54538 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cfbe5e-bcdd-3185-b06b-264010378642 | -7.09548 | -59.22379 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad1ed11f-0c10-3095-a04f-74e1faed40bc | -9.20015 | -59.654 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aca7219-c9ca-3879-8914-4a73ddfe5987 | -9.1597 | -59.64014 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31db41c2-0b4c-32bf-8702-d0f1e6c02afb | -8.1012 | -61.18765 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25cc1af3-6d4c-3d33-b963-d4f8eecdc676 | -8.11003 | -61.19614 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6279b420-aa3f-37d1-ac45-f5c0495b71d8 | -7.43103 | -60.02983 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e5aa3e-4c23-3e4c-b1b8-5b590ffb121a | -7.91025 | -61.75266 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceaaff85-4af5-3b13-81b8-355b658f479d | -8.99515 | -60.53312 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4df69249-6ab3-36a7-9d4b-0a5f747bb7ac | -7.88088 | -61.80902 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e9cfbe5-d423-3975-b2f2-564440693150 | -7.95451 | -61.75248 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d51203e-7e1a-3e31-b559-3b8839f630fa | -9.19051 | -59.6488 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7def692-214d-3fbc-b090-c2a6d55683a9 | -8.1513 | -62.77528 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f483f26-73c4-3c13-b468-24b8726fa3c5 | -7.43824 | -60.02736 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36bea9dc-4cbe-3020-b9a7-b3468ae3909e | -8.98742 | -60.5391 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 68d225ed-97a3-3e24-9046-59f0a37faa91 | -7.49666 | -63.8262 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 825c5fd7-39a3-3b52-9743-89971ccfe30e | -8.6646 | -62.46437 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3db9da3-d87e-3681-b190-d44cd1eb58ea | -7.8206 | -61.32754 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2eaca27-3eca-3e3d-b114-e5c62e5c0fef | -7.07577 | -59.23941 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 784fa5c9-0b63-3a1b-b865-71af9e9c2154 | -7.94732 | -61.75494 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78db5020-7138-34cf-8b04-faebc70bba2c | -7.62597 | -63.32581 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31cf088f-6fbc-3e65-950c-167651dab0bb | -6.95096 | -59.5493 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83b6b40f-a72a-374e-a381-8e17004affea | -8.99237 | -60.52908 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42e13b2c-6ccc-3a6c-8971-4bc925d36d6a | -6.90931 | -59.61953 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53ddb7d8-4334-3893-b7c2-0268668faed5 | -9.20237 | -59.63927 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d037f64c-de8f-3fa1-975f-6ee88b266fc6 | -7.67072 | -63.31332 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e5e9304-bc6c-316a-801f-8f8ab86a0a93 | -6.91049 | -59.63428 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74de3717-b4a1-3fc9-bd43-4b342d6ce13b | -6.79721 | -59.81964 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f67af81-1f43-3058-835f-aeb4747482d1 | -7.45463 | -59.94322 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be55b11-5d06-3e6d-b1d2-cbaf01a6c8af | -6.93191 | -59.53906 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab31b7cf-a0c9-326d-9a7e-f8a3e2cf9d05 | -7.50087 | -63.82274 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c963c024-772c-3326-9ea9-ae2ee05861bb | -8.97297 | -61.67978 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 91bc1305-8383-391a-9146-682901aa4a7c | -7.09887 | -59.22432 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09de52eb-b60c-3794-8bc4-96cfa08b3169 | -8.92554 | -62.23664 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8229c500-3ad8-32a2-ad90-71752c4e1d37 | -9.17047 | -59.66064 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa1c8096-0fb5-3f5e-bfae-0a909f7bf936 | -7.28791 | -60.62539 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4853ec10-dc7c-33ab-b967-082ec3908996 | -8.98789 | -60.51396 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7d31548-b85b-342b-84c9-bd4cf35818c7 | -6.48204 | -62.93495 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b7596dd-72b7-3494-8c5f-41a6df270c9a | -8.94276 | -62.23577 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71c47a02-387d-3df2-83f9-e2685f0d385f | -7.95415 | -63.21331 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d33f624a-3467-3a1a-bd54-c52ce5d3c350 | -8.98139 | -60.55615 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dd68bd0-836a-3930-a501-6dd050b489d2 | -9.16989 | -59.64168 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9935cb3-6009-349e-ad09-767fa45fabc9 | -8.994 | -60.51853 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7049cf8-33cc-373c-87de-1c63829f080c | -9.51303 | -60.54568 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51bb7c37-c441-3d39-bbc0-c56f9022bbcc | -9.17102 | -59.6343 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50f21794-c66b-3a51-90b4-a6ccca17ec47 | -9.00126 | -60.53767 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f55a422-8908-3eb8-8af6-fe84829b3a8b | -9.16481 | -59.65222 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea18e91-9db6-3838-a718-69f46dc54914 | -8.98565 | -60.50639 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4e04b4b9-06c1-3891-a891-ee5008bb856b | -6.63028 | -59.9986 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97cca255-65a8-39f7-a60c-2ef084a1fcc6 | -9.80918 | -48.5393 | 2025-08-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2cd2afc-055d-379f-9aff-0397d97cde50 | -7.05175 | -59.62317 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aa86e56-7c4b-3443-a340-737c69d2b2eb | -7.46057 | -60.41098 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25ea8ac-91d1-38db-bbd3-53d971b4672b | -9.00174 | -60.51252 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3cd68ce-fed8-3136-882d-84f5c94ba9fe | -8.98341 | -60.49883 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 255cc915-7b54-30d7-88df-fd3fb48d224a | -9.18435 | -59.66665 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7da2b2ac-eef2-3238-b49e-cc0b828ac7b3 | -7.92795 | -61.74828 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ea88f37-5d8c-3331-a663-644bb63a871b | -6.93363 | -59.55031 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ae181be-1b6a-3c3b-8663-bd7552a2a8b2 | -7.28021 | -64.69825 | 2025-08-16 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63209792-cc7a-36e7-b67e-803e36df5aa9 | -9.26389 | -60.7731 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328fe4d3-4817-346a-a563-f6c779633335 | -7.88033 | -61.81253 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ccc3cbb-537f-3ca1-8607-b58a1b6f0264 | -9.50583 | -60.54819 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc924c28-9cda-3832-8d1b-874338dd4e77 | -8.96856 | -61.68623 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7990d17-91dd-3c07-81b7-c9411fea3bc6 | -10.05035 | -59.12181 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad30dfa-9f6f-3b71-b474-6ca8fb4f9f85 | -9.53269 | -63.71964 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 192fb626-0051-37e3-884c-e71c0ceffad4 | -9.21096 | -59.67445 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1885c976-0a54-30b1-ab92-3257d3eb0cdc | -7.56609 | -61.43264 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e3028cd-ef9b-335d-8c4c-21b5523112d8 | -7.52564 | -61.3231 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bab98a7e-eea4-3596-b466-dc7e3b7847e8 | -8.9902 | -60.54314 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4c4c649-7cd9-35bb-bf12-62fc4cc8ff23 | -8.57641 | -69.69417 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b937f521-a0b1-38e4-bffd-436065bdf685 | -7.9606 | -61.75704 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a7a5dd-c949-375b-b6ee-d8039d3e4a34 | -8.03616 | -61.51529 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf716b8e-1c98-33d0-8357-a566ace14f6b | -8.67302 | -62.45472 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f46686ce-4cfd-36f5-8af6-c360f74aa8d3 | -8.98905 | -60.52856 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b71819f6-eba2-3a1e-ab43-0ed6aad59c09 | -7.91135 | -61.74566 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a24d62a-ad85-31ba-9094-71a8f6e43a3b | -11.65826 | -51.62376 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1b48d96-55b6-3e17-90ae-b5418ae0acbc | -9.16424 | -59.65591 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cd4d843-d557-37cf-bd2d-fc8d7d80efca | -8.99067 | -60.51801 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad506bcb-8b84-3d6d-be14-478bda6a2047 | -7.28105 | -57.65543 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b3c12b5-2d18-3cb8-a60e-5c8bd0fdd6af | -7.57155 | -61.3979 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4a1459f-8746-3994-9011-f2e4784d4cf9 | -9.50242 | -60.52594 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README57.md)
