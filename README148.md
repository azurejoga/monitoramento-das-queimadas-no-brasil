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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b5854da-b23e-3829-9f31-d21a8d223f1a | -9.1572 | -60.51149 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61e1c2c3-ded5-36f9-8c99-b0a61af07e04 | -9.94599 | -60.09737 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e79e0e-b23f-3edf-9d51-26a441fa0516 | -9.79996 | -60.48032 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9bd349cb-0f16-3afa-a3b9-f9063e2ce92e | -9.79957 | -60.48339 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fe6c56ad-2e88-32b5-9483-166b6fe8c718 | -9.79857 | -60.48012 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eee90e99-9557-3770-b553-2b6015742dca | -9.79815 | -60.48318 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39234fb4-742b-37f1-8c4f-b38dea62a4c3 | 1.08017 | -60.42507 | 2024-10-05 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cba0c5cc-30db-3201-bbc7-6d4d488c00fd | -3.24169 | -60.652 | 2024-10-05 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f0250e3-655c-35cc-a4f1-d6d380e2daa4 | -7.89038 | -61.45962 | 2024-10-05 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cb97991-eb0a-3487-825f-7ea31473aac4 | -7.88969 | -61.4646 | 2024-10-05 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a17d23b1-a805-3af8-b9f7-4d7ae287ec54 | -7.28504 | -61.08927 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ded106a4-9923-30ff-92a6-3fb849e8b300 | -7.28433 | -61.09439 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9ab87ad-9f46-350f-92b8-8c286d6a02dc | -7.28191 | -61.08233 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 37cad5db-7e29-3407-9b40-a582dffaf596 | -7.28118 | -61.08741 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5b3bbb4-46da-3fc7-8ee6-26e742505f0b | -7.28096 | -61.08347 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3196863-7e10-3d47-90c8-ddbbc75943aa | -7.28043 | -61.09255 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb67c128-8db8-3402-859b-b9f975bed857 | -7.28025 | -61.08858 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6583126c-d6bd-3cd2-9fda-dad7789dfef3 | -7.27968 | -61.0977 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ae14d5ca-fae7-3bd2-b42c-09fe06d6f36a | -7.27954 | -61.09374 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| aca82e9a-3e7a-37af-9602-f2d343cda4a2 | -7.27638 | -61.08677 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d2d33f1-fa4b-35ff-af39-6d04e2fc023a | -9.62314 | -62.29798 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90488115-43d8-3b9f-a899-1d1c0f3be6a9 | -9.6956 | -62.17089 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6b8af43-0486-3792-a068-cd6403a952bb | -9.08845 | -61.13527 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267ec80c-fca2-32e3-bea2-984a11c50187 | -9.09334 | -61.136 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1f8bc34-c6b3-366d-a6b3-12a2da7484ca | -9.16795 | -61.57409 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69be98cc-30b2-35da-8ab9-1d7a74546a0d | -9.17202 | -61.57979 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 529ee3ad-82b2-3611-9d3c-3da6a190f225 | -9.17271 | -61.57472 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0a010e6-1eb5-3379-b706-e882b7370ecf | -8.22467 | -61.2216 | 2024-10-05 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19f9f618-068f-32fe-ba60-1579b70225e9 | -8.66991 | -62.50708 | 2024-10-05 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| decb5560-3df1-3905-b30b-e89ecfe49973 | -8.97474 | -62.46914 | 2024-10-05 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3d33a5-5475-3854-aaef-37b9c79a2102 | -9.17203 | -62.29552 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a9bf090-5d42-3da9-abb9-bbf7bc2ca628 | -4.71013 | -55.98631 | 2024-10-05 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a517ecd7-f407-3d1b-89d8-cbd62ec0a3fa | -4.7093 | -55.99197 | 2024-10-05 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8692c94b-bddd-3061-9f5c-97ec2915fa3f | -6.95437 | -59.06584 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9078b8fc-2f66-35e6-9709-fb573e073e31 | -6.94891 | -59.06501 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9b0f0370-6bd9-3163-9adc-5e44eceb4cfb | -9.89005 | -59.49933 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c547a2e2-a494-3b64-a31f-e5f33741c19a | -9.88959 | -59.5029 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9084af22-cdc0-35e3-bb44-f43e16dfd42f | -9.88452 | -59.49853 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3d289f2-4ef0-3361-9c18-455997814b9a | -9.88406 | -59.50211 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40f888ea-143e-3526-9883-70b6065829f3 | -9.88359 | -59.50577 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aa0cffb-df33-3852-a5ea-f91a0e9605f0 | -9.87853 | -59.50132 | 2024-10-05 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7eb93e6-903f-3a0d-b322-85624b58ce64 | -9.80455 | -58.98059 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c3da207-2042-3106-a383-c7dea3aaaa08 | -9.80327 | -58.97835 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7245c5e2-41b1-3505-a100-3fdb2f26f386 | -9.80274 | -58.98236 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c49e77e-b520-3c0d-a3f4-858d8ec640b5 | -9.79831 | -58.98396 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d10af58c-956a-3fcb-aeb9-d5263c568c4a | -9.79782 | -58.98789 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf5e102-db79-3b52-a7d9-da11b4005c30 | -9.79648 | -58.98567 | 2024-10-05 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45e6082d-5734-3133-8515-f26d63f55bba | -3.1004 | -59.36528 | 2024-10-05 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea13226e-4931-3057-b2e2-0cea2e0e25e8 | -3.09996 | -59.36818 | 2024-10-05 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c67c4990-b8df-354b-a0eb-2595bace7b9b | -3.09533 | -59.36458 | 2024-10-05 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63cdae2f-5f9c-38f5-bf94-9a915bb6036c | -3.09489 | -59.36751 | 2024-10-05 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 823c4eea-0e35-3048-996d-b34035c79e03 | -3.87018 | -59.74007 | 2024-10-05 05:53:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6fda5fd-9a1f-36f3-8a5d-7354fdb30d2b | -3.86519 | -59.73933 | 2024-10-05 05:53:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a1e021-83e2-32c5-845d-094f26e88cbb | -3.76325 | -59.33382 | 2024-10-05 05:53:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e27d9c9d-3d52-3d6c-bbda-a861d8d69a9c | -9.17656 | -62.29621 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9c594c0-ca9f-325f-a641-afaa7e159229 | -9.18108 | -62.29686 | 2024-10-05 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14f02d59-8189-3181-a494-42c4a6b09e69 | -7.27476 | -61.09307 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fec76ca3-0c9c-34e0-b8c6-4c4e9e6f6fc8 | -7.27489 | -61.09704 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fd294f74-144e-3cc3-bf09-3097fab62d0d | -7.27546 | -61.08794 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 09bfc475-0ea5-3884-bd5c-110d3ebed3cb | -7.27564 | -61.0919 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 97be55cd-c39c-32ae-8ce3-161bb4515210 | -7.27616 | -61.08281 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea936660-c8bc-39ce-8975-3e2c864048e3 | -7.20403 | -59.61697 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f69d4882-7e39-310b-b974-d4b5a8464d00 | -7.14848 | -59.36339 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe441425-e39e-3b7c-8d29-10d4ce88dd8d | -7.14801 | -59.36678 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf842eb-b765-301b-9b42-692897967639 | -7.06587 | -59.27309 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa1310a2-861c-3a94-85fe-495c7e95b07b | -7.06205 | -59.30045 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66b62031-7ede-3610-be41-cd7441c8ec66 | -7.06094 | -59.26888 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b3ad2b-9aed-3367-9281-1dc41a172467 | -7.06047 | -59.27227 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb62f33b-5493-383b-8972-dc26e716f986 | -7.05666 | -59.29969 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7906aa32-5530-33bd-844e-729da5cf4017 | -7.05618 | -59.3031 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0979ca5d-97bd-32dc-ad11-f83e428bcc47 | -7.05554 | -59.26811 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d07e0b7a-c338-3b85-a443-92a5e9ad0b09 | -7.02114 | -59.39782 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 315f08c7-86e0-3990-8880-3a019ce24269 | -7.02069 | -59.40111 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46c8d75c-63d0-3991-b533-7deee6b9cbb4 | -7.02024 | -59.4044 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ffe4bbb-c26e-3fcd-9743-d94f9a456f7f | -7.01977 | -59.40773 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6864b686-4a1e-3904-8482-48ad50a96f45 | -7.01715 | -59.38713 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ea59e9-ad15-3fec-90ed-7bc8e48a141c | -7.01534 | -59.40034 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d0ab4bc-de44-356d-895e-ddd7d988ea34 | -7.01227 | -59.38294 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3af4c9b8-7d8c-3f40-b611-7c376ac43968 | -3.05279 | -66.20603 | 2024-10-05 05:53:00 | NPP-375D | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db02361-2ee1-3a9e-8b3d-fc5c2b2bf429 | -7.8818 | -54.88428 | 2024-10-05 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2827ac47-e135-3d47-a37f-812da4575d46 | -7.88016 | -54.88231 | 2024-10-05 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea67e27c-d8bf-3463-9d39-f9ccefd9250e | -7.87551 | -54.87609 | 2024-10-05 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af7fae63-311b-3dfb-883f-ee2d07705e07 | -7.8739 | -54.87422 | 2024-10-05 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56b16a48-100e-30bc-bea9-9f4ecb5d39f6 | -8.51243 | -55.15458 | 2024-10-05 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb4057fd-5fc5-3d74-a4b8-a412e77eb2c8 | -9.23908 | -65.60417 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e985c822-56fa-301a-a5a9-a7edad6eb518 | -9.26631 | -65.36628 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a31208fe-9114-374e-8dbf-e1fcfef58d69 | -9.26695 | -65.3619 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48af3285-d536-3a43-b4e4-19205056ab3a | -9.27003 | -65.36683 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78b10ce1-a74a-3e65-8e2d-3457aa397e1e | -9.27067 | -65.36244 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc74fad5-124b-3f57-a532-9afd7e751ffc | -9.2852 | -65.41885 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d1f5cad-179e-3996-a792-9e5c6333c4c8 | -9.28585 | -65.41444 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ed0fa5-24d0-3e93-a821-674104c93282 | -9.28762 | -65.42822 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 850ef142-788c-3fe2-bad2-30f88e85ab17 | -9.28826 | -65.42384 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b91cfa7e-d5cb-376e-a699-7e5d8b7b3341 | -9.28891 | -65.41945 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3748204-3799-3e3e-95dd-ba951ac3983d | -9.29132 | -65.42881 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89a8f091-2567-35c1-b376-134658466ee8 | -6.81731 | -64.32191 | 2024-10-05 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf2c50bd-31c3-3441-8761-aece6ee15a2e | -7.29143 | -64.66076 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15137dfb-d919-3069-8709-664c33cbd2f5 | -7.29178 | -64.65856 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 388f2f28-b9f3-3ff9-b1d4-1d2b40b9e967 | -7.32856 | -64.67101 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8215f4d-f076-3414-9639-c324575d17d4 | -7.33234 | -64.67157 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README149.md)
