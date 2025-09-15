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
| 82b28bd9-7b49-34b0-bc24-a5ea6ba69ea3 | -5.11776 | -46.12972 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2aeefb1e-589d-3c3d-aa65-107b39da6367 | -8.10679 | -50.16217 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b9581fb-79b6-38ba-93f0-b7245e18af2c | -7.97231 | -45.64274 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 734311af-758a-373f-b727-a4c89b40f0b0 | -9.0959 | -44.81197 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02858bc0-d3ec-3730-86a2-18dbc21d59a1 | -7.869 | -43.57425 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d995d665-b170-35df-9616-2a36a636d46a | -6.63142 | -44.7346 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 318c5666-5c2d-3fc9-b143-d6869fc214b8 | -8.94248 | -45.79509 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c60eda1f-c5aa-377f-9975-4773dfe6a5fd | -7.69869 | -44.67299 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 43f8869d-5189-3c56-9018-251faec12f28 | -8.64523 | -45.69384 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fbb15b8-9dc3-39e7-9ed2-2750b0ba34b3 | -5.60791 | -42.90414 | 2025-09-15 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2aac0f9e-cb94-3cc1-9309-7979ed7bb117 | -8.14179 | -43.6525 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c29bc52-b421-33f4-b7dc-2910d32026f8 | -7.85745 | -46.11179 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8362156a-a357-3c05-91bb-f6f5830061db | -7.38716 | -49.98581 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73aec8b0-e4c9-3cdb-8875-eeb128a9e7aa | -8.75713 | -46.08324 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b908b45c-dd90-3db3-979f-00baa2dd59e4 | -9.23888 | -45.66118 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8acc5ce6-d439-35e2-b4e0-fc264224ae9e | -8.78971 | -46.04904 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23bfb054-65dd-3d21-9d21-6a481e49ba82 | -7.87214 | -43.56381 | 2025-09-15 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80a4df1b-51a0-3875-a699-e53e112d8310 | -7.87223 | -43.58611 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1e5fa163-1cf0-3cfe-80e0-9206e687b4d6 | -8.79192 | -46.05727 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edd31f1a-7da5-3734-8d08-199329b98578 | -5.65398 | -42.60118 | 2025-09-15 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90d6b107-5886-3d82-9d4c-810bf9073799 | -5.98035 | -45.82286 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcd86283-e87b-3d99-b5b8-390ad090e828 | -3.5152 | -52.74784 | 2025-09-15 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1da072fb-2bfa-36ce-b98c-c84272cda028 | -7.30683 | -43.93143 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5ab1cd9-4171-34d2-8a2a-a02f324e765e | -6.80892 | -46.93466 | 2025-09-15 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d0dbfd5-9f59-34eb-ac98-14b9de8fad80 | -7.43118 | -44.84031 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c39ca2b-a679-3833-b8fd-ceb42546faa4 | -5.7792 | -43.73813 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbca1dc5-bc2e-3f5d-be26-02d567c662c6 | -9.24933 | -45.65927 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9775662-12fd-3044-8252-d56c113f56a0 | -8.91937 | -45.46423 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022211b3-93cc-3c61-ace8-4a2382491912 | -6.99952 | -44.55562 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b315968-4f91-38d0-8744-3076d05874bd | -4.33126 | -46.73968 | 2025-09-15 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5dc3500-2e00-351d-a651-207504a247f4 | -7.89468 | -43.57473 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81a98b53-335f-3023-abdb-b61a49a9dfe1 | -7.88573 | -43.58821 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| da648f11-4857-3010-aadb-cd578b0941ee | -7.84359 | -46.11317 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4335d13d-b2aa-3878-a0dc-8cbc88b0f964 | -6.40848 | -42.64347 | 2025-09-15 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2bb6df47-c2bc-3b13-89f0-8ffc80eab1ff | -8.09882 | -50.16074 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd05946a-05f7-3471-9dbc-b5a273cd559e | -5.0831 | -41.16394 | 2025-09-15 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 414dbcbb-5d69-319f-9a4f-97014361e527 | -6.89492 | -45.63403 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af6a9fa-56bc-38b3-9e2f-88f98d7c3544 | -7.88565 | -43.5659 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 860a9f08-6350-398a-9b4c-ad0522c11b29 | -6.63198 | -44.73121 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d11c36ac-9a7d-3fcb-93c5-099f1ec8dc0c | -8.35116 | -44.72327 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 093ef5bf-41f8-3d24-bf06-190deda4cb2b | -6.84245 | -45.62216 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deb536f7-c8cc-385c-b5e0-b758cf1b620d | -3.5147 | -52.75086 | 2025-09-15 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0491b540-6d62-374b-ae7e-9ba6ee589a22 | -7.37462 | -44.35143 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7f0d44f-bc1f-31c0-8723-2deaf0950568 | -7.78893 | -46.1148 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27af173-2d73-36f9-bb6b-e46c6799a3a7 | -8.981 | -45.76556 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff91dfd1-4221-3a47-9134-0ddd7cd3b466 | -8.99146 | -45.76365 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8d0a7e1-5f1a-35b2-95a1-f477d89e4467 | -7.50406 | -44.37205 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e5b6743-4824-33a3-b22a-ae10d2f74d60 | -7.90504 | -46.23904 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9ca96ae-7457-3420-8fe4-bcd20b247335 | -8.91343 | -45.50231 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 945b4991-fadc-3615-ae67-601a89393c84 | -8.11713 | -43.67835 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b15cd32-0380-39d8-b941-6b902b946c96 | -8.13842 | -43.65198 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e00e6ce-73fb-39c2-90e7-3198b62fc8bc | -3.65342 | -54.05367 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb877ba-b219-34f3-bba9-29ea0ad80823 | -6.15938 | -41.17912 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 542ca086-0ec5-3d58-a3b8-1b60d66a2e93 | -9.00266 | -47.03846 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b2c19ea-72c9-3ed8-ba5e-941e84bdb552 | -8.91662 | -45.46024 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7844fa8a-9141-3ce4-b8d3-7211cda7fd4a | -6.97747 | -44.54515 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2d241d45-c91d-31b3-bb53-2909c9fd9601 | -6.42455 | -42.6071 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a008f38-a2d1-3297-9137-5850b38abff5 | -8.62595 | -45.73005 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 541a1176-876d-3440-8089-bafde3d9adb6 | -6.25907 | -43.46829 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97fab7f6-dcc2-3585-a413-59f4905e5d8e | -7.05594 | -44.6749 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d2fa7c5-8751-304b-a9b1-7f3ddefca309 | -7.86114 | -43.58045 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5664c96-96f1-39f9-9e61-4dd9002df065 | -9.00495 | -46.10909 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac03c510-fa23-3e8a-ba24-1add3c2e4e39 | -8.41375 | -47.22439 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 877234ef-5a5e-3c49-91f9-9f0fb3c33985 | -7.88236 | -43.58768 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 7b2e86f4-fe46-3bac-9ec7-eed7efd66117 | -7.51934 | -44.71237 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f36ff50e-17b3-3646-92b0-d64f45d4877c | -5.18482 | -45.16994 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd50582d-02ed-3e7e-97ee-65e21d8fffec | -4.13595 | -48.81624 | 2025-09-15 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9606a3d-10a3-3ad3-8ad5-38b7f73a6bba | -5.9439 | -43.83876 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bb625c2-4852-312f-b7d5-839cd0ccaf47 | -6.68947 | -45.51225 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 681a21f0-2e4d-3a22-bdea-2371d877288e | -7.38659 | -49.9893 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 577f2b32-6436-30d5-b468-19755033d67f | -5.39527 | -42.82681 | 2025-09-15 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 259a6082-cb31-3541-b9fb-3af524bc50d1 | -9.23449 | -45.6676 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e94e7eda-d880-39ed-8a0e-e66906527498 | -5.39132 | -42.82992 | 2025-09-15 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bb5087ed-f2b3-39fc-b023-693387e3e6cd | -6.9244 | -44.77752 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc513ab2-ae68-3504-a5ac-6aff4261a104 | -4.8651 | -49.33306 | 2025-09-15 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 942bc5e5-631b-377b-9626-5417bcd7d3f8 | -3.60044 | -47.51481 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3eb4c2d-2e02-310d-9caf-1c28179e69d4 | -7.98702 | -45.65947 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 970a615d-7aac-372e-b9d4-383642246980 | -6.92938 | -44.78888 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45f2ca2b-8760-3553-b284-d78e080ae954 | -8.34428 | -44.72156 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1c0d07c-4a2a-3e8f-8f25-1b090aeac6eb | -6.16306 | -41.17968 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20c74592-0f25-322e-832d-deecf554cd16 | -6.88276 | -45.62495 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a68290ae-165b-3e62-9e97-ff11451bf0a6 | -8.01241 | -43.81008 | 2025-09-15 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b6e3d91-d715-3cf6-adcd-cc7490140e0a | -5.60508 | -42.89993 | 2025-09-15 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5840ce37-9be6-3189-b1e9-a65a135dfa0c | -6.32693 | -43.33936 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c28ba284-eb49-3c29-abbd-7b6de3f0224a | -7.44053 | -45.84324 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df3d29ee-7613-3e80-aab0-e900d25bf07b | -6.40853 | -46.93351 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c393037-5e84-3cc4-a4d2-3152dcc56f9a | -3.42068 | -47.60661 | 2025-09-15 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f283bc99-e957-343f-82bc-083684535085 | -5.75069 | -43.92324 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dec4931b-e46c-3284-98f8-916a4ff4c284 | -6.25 | -43.46674 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d78a2e03-663c-3d8f-a6e1-40bac40a1793 | -8.96065 | -45.80869 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8ef4f0a-a50f-3f77-bd85-76f17c44004b | -5.67474 | -43.49118 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdfa0445-08ed-3f8a-bec5-ff481eb4a3e0 | -8.09427 | -50.16343 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e59ad4ad-39f4-3137-a631-bef327e17e2f | -5.33679 | -45.8043 | 2025-09-15 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e73cda-6373-3280-92d8-82fd364a3b35 | -7.63933 | -49.72456 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e6c1c3-5686-3c31-aefa-c7adc0277887 | -7.89186 | -43.57057 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a18ca41a-fd95-3c5d-8d3b-6cffe5e669f5 | -8.77755 | -46.01846 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38b55e58-e8da-3ad9-a60c-b2b673461521 | -6.99844 | -44.56253 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4366d454-084f-3656-aa1b-ad57ccd928c7 | -8.91386 | -45.45625 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53c36420-3ba9-383b-b042-909014e351ea | -8.63916 | -45.68935 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| edb4f74b-567b-3787-acf9-b046671b3b3f | -8.91829 | -45.47116 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README26.md)
