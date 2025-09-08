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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e09bac14-12a4-37d4-87ec-b74669c7a6a7 | -9.27722 | -60.97561 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2a1803-38cf-3cb6-b05e-e9bf42e1455a | -13.82279 | -46.24899 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1befac6-0adb-3f7a-932c-fba4120e6ca1 | -9.98813 | -51.68904 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55ea3b5d-dfad-3051-9825-472d34b9f5ed | -6.53956 | -49.5084 | 2025-09-08 05:21:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ad78e9-dfaa-38b5-90ef-2dacbc69e1e1 | -9.18183 | -60.76712 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00708dae-8dd3-3bd4-b408-edc0502c9b2a | -6.8759 | -47.91323 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0f1b63fc-c551-3687-9c78-cf493ae4367c | -12.93433 | -54.78997 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d17cbac2-8c15-3e64-896e-77f91189acc5 | -6.86321 | -47.91512 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c87ae731-e24e-3e10-b009-bc6c60096888 | -6.26979 | -53.4364 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6b5b524-8057-39ac-9686-1ddecdbd83cc | -11.19833 | -55.01149 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1f0a6ac-5f75-373b-8164-2cc05dc94899 | -7.73996 | -50.31535 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0d96e0-f94c-380f-8680-1ad27b036ff7 | -6.63096 | -53.35452 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c60497-ecb1-3938-8795-fcf9fa9cef6b | -6.876 | -47.91552 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4af8de4e-28ef-31f7-b6f6-31eabcab95ab | -11.3192 | -55.12139 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8895fb94-2483-34b4-a122-c7263c7b9a2e | -10.35249 | -57.50604 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0abe41c3-0390-3461-8a9b-c37bf5c322e5 | -7.1895 | -59.8382 | 2025-09-08 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 496bc7fb-c375-3bc7-8b08-03285782839b | -10.29043 | -67.2746 | 2025-09-08 05:21:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03f87a7-a031-3ed9-855f-ce84f9265bec | -8.20554 | -50.14162 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce1c5c67-e374-3725-af8d-2250efa4c7d7 | -12.12232 | -59.83804 | 2025-09-08 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05eee6e3-cc2b-3d7d-be38-8cef2a49f82d | -10.51207 | -57.80088 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7beaf5cb-0b63-3fca-bbbd-af4fbca6bf73 | -8.0917 | -54.75666 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bd6386e-425b-3ffe-b558-d5c21bf8b71f | -12.7212 | -56.56456 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8494f16d-5cbd-30c4-a7a9-ef310433b9f3 | -9.07793 | -65.41012 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b35e114-282d-389e-b23f-edef1bd78f03 | -12.81939 | -56.52574 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c54ff69-3ef8-323b-b65d-abef751a01c9 | -10.10077 | -48.11196 | 2025-09-08 05:21:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb45619-153a-3440-b6f3-9f58e3445aaa | -10.47389 | -53.60693 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06c0eb02-196c-3e9d-8f36-f8e40089d288 | -9.62426 | -64.21013 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58590678-01d1-3223-baff-501e2008ecef | -13.70521 | -46.87037 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e8a99c7-cf6c-3268-a20d-9a8ed5edd65a | -10.00715 | -51.62833 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f26fb04-199d-3139-9445-45625bd262f8 | -9.11661 | -61.48861 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a338d3a6-9d77-3d86-8f10-dc5ed92dd8c4 | -6.82941 | -52.80024 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5623fad-08fe-3cf5-a98c-f39f183cb685 | -10.00593 | -51.6335 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4fc8f08-4b58-3cd0-8e06-cc0539149f2f | -7.78422 | -52.12571 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dad73305-6b63-354b-a906-8b9f7a9c897e | -8.21138 | -50.13889 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d63be69d-a607-3551-b6f0-e4c3670784b8 | -9.05696 | -50.46909 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e5152fb-8b0a-3913-af95-6253974cd166 | -12.95264 | -54.81229 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ff588bd-dde1-3247-8f6a-84e4914caeb2 | -9.13597 | -65.95246 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df7bd237-5eb5-3032-bd65-ef76ac93e312 | -10.58024 | -61.25422 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6442090b-1e6b-37d2-8f93-6c6697d8e3dc | -10.02774 | -63.47905 | 2025-09-08 05:21:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c5f7dc-f882-3a10-9491-936fd8f04d8c | -12.94795 | -54.7841 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd56c6ec-b7f3-308b-b2be-0381a8829549 | -10.47332 | -53.61119 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a352009-ec04-352a-b106-dc65822f12dc | -10.22122 | -50.51917 | 2025-09-08 05:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 678d31ec-dcb1-3885-a9c1-4fd8a0a56358 | -9.27711 | -60.91222 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b024a22a-ae41-3827-8359-902e09fe85be | -8.08705 | -54.76105 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3e60485-1f05-3372-8c4d-820ecfdea52d | -9.17276 | -59.36978 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e2510e8-dcc6-3f98-8a92-b0cb372f0bcb | -6.22871 | -55.93436 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b87d6b92-4448-3cc5-8fc7-802c5932c916 | -7.40461 | -61.62698 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 8a197eb4-ddbc-3bac-999c-bac11517b760 | -9.44863 | -61.82288 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d43e1018-64cd-3601-bd27-5c8d198b7713 | -6.96756 | -62.93771 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95f66b92-d188-33cb-a44d-f0d9647c91ca | -12.95062 | -54.76458 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f431aac-2793-3d15-8c6c-c51710c0d1d2 | -12.81694 | -56.51608 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f998aa33-823c-3112-98e0-8d1de2e0d3f7 | -13.80971 | -46.29301 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2eb528bf-9289-3691-b87b-6c5fa8d3a50b | -11.22789 | -60.4422 | 2025-09-08 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbbc7901-a17e-316c-a857-59a72c730e37 | -10.14474 | -46.21682 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 27651a98-d0b4-3fa6-8a18-8d3307924387 | -11.86953 | -50.96569 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55c73b38-8e28-3749-9c98-99b5f0a730e3 | -7.66924 | -50.29206 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5eac8bc-cc65-3c40-aecb-aa4bae82420e | -9.53828 | -59.06489 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4660ed1b-84d0-3f49-9cff-ef4395ac7162 | -7.40749 | -61.63147 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9a416a-8487-380d-a6d1-466fb17d615f | -7.87468 | -46.25584 | 2025-09-08 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fcd0e7f-8521-3ef9-9c23-f062b6aac604 | -13.81398 | -46.26331 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59937d23-e37a-3d5c-bcff-c0c91d7d9479 | -7.11524 | -63.07091 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d5b718e-17ee-35af-930b-e885a260dafe | -11.62663 | -47.14927 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e2da28d-8d9c-3f4c-8b57-5b122a626a58 | -9.08826 | -64.01421 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e47f266-c396-318f-8eb9-1181636a80c2 | -7.82632 | -45.41302 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c20b794-7163-35c6-9c1b-aacee6435dc3 | -8.87772 | -69.34483 | 2025-09-08 05:21:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31499ffd-29e6-3136-8dbd-e9107181b32e | -11.60569 | -47.15198 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ba05393-8c8a-3b14-a233-300f5756609a | -8.18364 | -50.14175 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14e7a21b-33be-355f-819a-1c41a9099434 | -9.98904 | -51.68959 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ee92ed0-601b-3e29-94b5-598e2e13d780 | -6.64185 | -53.36796 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76dba10-e2e3-316c-a27a-619ede9447ca | -11.28713 | -46.46213 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dbfe97d-63a8-3f78-8227-cae6568cc0a8 | -9.19689 | -65.909 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11190c3c-316b-357f-89e6-e930fd26d194 | -8.60536 | -54.67138 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d1088c1-4a4a-31d3-a7bd-21eb1d8134c2 | -5.7672 | -56.52113 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c111a0a1-43d9-3477-a329-7aa2d52e664f | -5.25239 | -57.12528 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64bdde44-9d68-3e12-b9c3-50b02da7f8bd | -9.07753 | -46.98145 | 2025-09-08 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a696879-c446-3925-8ee4-4224f093dd44 | -13.28666 | -51.74185 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfc2f55f-0265-307a-89df-213b3442d3cb | -9.24196 | -57.0656 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f697438b-4969-35b1-8c4b-c3860dde7488 | -9.48071 | -60.4924 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd75bc99-6cd4-325e-877e-1cb0a7cbcc12 | -9.99609 | -51.66802 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b537c139-0f40-3ce8-b565-55c62f03d480 | -6.64177 | -53.36676 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 236876cc-5bd2-36b2-991d-9e314e38b50d | -9.16833 | -59.37624 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2815fe7-cce2-33c1-839b-90118208a3ee | -10.13757 | -46.18981 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d394eb9b-c017-3adb-94c8-e123b0c8862c | -6.96906 | -62.9286 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dedf78f8-86ba-3ac5-82dc-08111ac3c78b | -8.70201 | -45.3123 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85731d85-3d3e-3823-b81c-0be95fe50882 | -9.20047 | -67.55948 | 2025-09-08 05:21:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64fa7fda-d468-38df-a6f7-acf9e38bceee | -9.81642 | -53.32633 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1ade603-68bf-34ed-ba89-d7f5c93b614b | -10.46457 | -53.60987 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c0643be-5393-3b38-9bc9-f30650596d26 | -12.19708 | -53.89991 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6defbd55-cd6d-3d92-9c77-ea7e897871a8 | -10.10138 | -48.1071 | 2025-09-08 05:21:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb54aefe-5633-3df1-b8f1-f69d701309be | -11.90766 | -50.98576 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 108543b9-4d13-3dec-9460-392caf3861b5 | -9.67471 | -51.06898 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6196f773-c9b0-3713-af69-95dc2a5e7d84 | -10.56964 | -61.2339 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5fb334-9be1-3d92-b32a-dcbbc47d9768 | -9.13521 | -65.95682 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e46d2a8-2674-30c0-a3ad-5f93a06ded47 | -9.15018 | -60.85121 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0192cf-37c9-36e6-a04f-2c29d1c1abff | -12.00987 | -50.37994 | 2025-09-08 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aca2efe-78fa-371a-a1ad-0766493157f1 | -10.44823 | -53.60075 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbd46ac6-61ec-348f-a83a-7417dae195bf | -11.20335 | -55.00504 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1cb011b0-2a91-313c-8e4e-6ea2d74943c0 | -13.00796 | -54.81932 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03c5ac5e-bcd0-35ca-90a3-0afa0ddb4397 | -12.93802 | -54.76277 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77fd9c13-d4c7-3a76-b028-74af1cd29827 | -11.19973 | -55.05953 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README84.md)
