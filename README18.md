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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad8d91de-ab58-31ff-a1b8-cf33336f3d87 | -6.7655 | -59.3059 | 2024-10-10 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c4063501-ecbd-315f-b984-f24264fe389c | -6.7798 | -60.0552 | 2024-10-10 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ffb94275-997e-3af7-85b2-90c0022dd0ee | -6.7799 | -60.036 | 2024-10-10 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9ba30307-0bd8-32a5-b043-98697db8342d | -6.7839 | -59.3245 | 2024-10-10 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 8795a289-c507-3760-b474-5868ed0ffd7f | -6.784 | -59.3052 | 2024-10-10 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 5fa4ba5a-5841-3f8a-9993-beda7e073b99 | -7.0234 | -59.3725 | 2024-10-10 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8cee11f0-06b8-37bc-afcf-12effed7efa0 | -7.0419 | -59.3717 | 2024-10-10 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 46961c5f-c2fb-31e3-8811-aa32c4922ffd | -7.1346 | -59.3099 | 2024-10-10 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e491ad96-5595-3bb2-bcf0-f8c61b499314 | -7.153 | -59.3092 | 2024-10-10 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4991cf03-821c-36b8-967e-c554fe7f8139 | -7.5934 | -46.7984 | 2024-10-10 00:55:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 843f295d-d262-3648-82f5-67d3842ec4c3 | -8.2325 | -61.1823 | 2024-10-10 00:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e708d2e9-5746-3a97-8de1-97325bc3651e | -8.6843 | -63.1009 | 2024-10-10 00:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ff1c3f9c-203f-37ad-b15f-275a59f67d5a | -8.6844 | -63.082 | 2024-10-10 00:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f3db0799-1c75-3de7-aed1-67c324f4a57e | -8.8422 | -61.4992 | 2024-10-10 00:55:57 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| aa32bd89-b340-3b62-9837-a8117d99eaa1 | -8.9898 | -61.6261 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6affa6d6-3044-3a28-9a3f-38c419b89939 | -8.9899 | -61.607 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 48f56532-0412-343d-9bf3-6159a81ac254 | -9.0084 | -61.6253 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 080e83aa-3e4a-384b-a59b-67e8e623399b | -9.0085 | -61.6062 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 578c6bdc-e00a-33e3-987a-3e8900009f89 | -9.027 | -61.6244 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 2193ef6f-e78f-333c-923a-c10d3cef1a91 | -9.0271 | -61.6053 | 2024-10-10 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dbe1f42d-485a-3f10-9592-a8836001ef1b | -9.0656 | -61.3934 | 2024-10-10 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 187e83b0-b17b-31f8-8a0c-abc47956b932 | -9.0841 | -61.4117 | 2024-10-10 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 045d4eef-9bf9-36e7-bb51-bea6bd63d4d8 | -9.0842 | -61.3925 | 2024-10-10 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 9e6a051e-71d4-3f5e-b63d-b67a24ea58af | -9.0857 | -61.1629 | 2024-10-10 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ba4fd061-45d2-3e98-a3e3-678d9f9c2ead | -9.0859 | -61.1437 | 2024-10-10 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4a269105-6c79-30d8-95d1-abb1b0d39fe0 | -9.1221 | -61.276 | 2024-10-10 00:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5d8bba7b-765f-3a24-b4be-3709599880a5 | -9.4819 | -63.1443 | 2024-10-10 00:56:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 748c22bb-243b-38ac-bdf4-7ae86863c824 | -9.482 | -63.1253 | 2024-10-10 00:56:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 33b5b348-cdab-3338-81b7-577f6401cfdf | -10.6056 | -44.7696 | 2024-10-10 00:56:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 30a136e0-610c-313e-9502-3db932a6eedb | -10.3707 | -61.2513 | 2024-10-10 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b78a200c-c4c5-3d37-b7c0-cf9cdcf818e2 | -10.3708 | -61.232 | 2024-10-10 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 726cd7c2-0913-3471-858b-a4159e48323d | -10.6258 | -55.8953 | 2024-10-10 00:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| d257e376-b685-3036-af58-51ca1f0190be | -11.0252 | -57.2436 | 2024-10-10 00:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 72c3f05a-20ec-379d-b653-2bb4ddcc2b0f | -11.0254 | -57.2237 | 2024-10-10 00:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 296.0 |
| aa06f6f0-bbd3-3d8e-a4c1-468eb3210824 | -11.0256 | -57.2038 | 2024-10-10 00:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 293.6 |
| 306453d7-c75e-34b2-82aa-4d0c67331fec | -11.0443 | -57.2222 | 2024-10-10 00:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 3dd930fe-8485-3792-9057-2ba7290f3eda | -11.0445 | -57.2023 | 2024-10-10 00:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 198.6 |
| e1f0579e-96eb-3201-b521-464b8e795226 | -11.2763 | -60.4844 | 2024-10-10 00:56:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ae45bc13-2d56-3ee0-a5d7-b33982a9b5de | -11.8188 | -58.8459 | 2024-10-10 00:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ea13e8dc-3469-353a-8a25-904ccd5308c2 | -12.2888 | -43.7495 | 2024-10-10 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 78b34f96-87ee-3e27-8d0c-8fbd57e03bea | -12.2893 | -43.7258 | 2024-10-10 00:56:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| e495b82b-444b-3be4-a0d2-b3c19b21bb66 | -12.3086 | -43.7227 | 2024-10-10 00:56:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5b5ff397-1e23-321a-b4ed-02ab2a266e59 | -12.3067 | -59.1641 | 2024-10-10 00:56:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| adcbeb40-4f8b-35e6-8748-1f82ba0a5d16 | -12.3256 | -59.1627 | 2024-10-10 00:56:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b75b0a0e-aac5-3b62-88c5-9d155c4b26d5 | -12.3987 | -54.5816 | 2024-10-10 00:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8343fdad-0320-3043-a63d-bc3daf6a1b6e | -12.4177 | -54.5797 | 2024-10-10 00:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| df336870-4178-389b-bf41-79f36a57b9f3 | -12.418 | -54.5592 | 2024-10-10 00:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 82c41b2b-dc6d-3081-82c5-e18125d603be | -13.8374 | -44.5455 | 2024-10-10 00:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4b160594-a024-3688-b899-7a6136095725 | -13.8379 | -44.522 | 2024-10-10 00:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 63475cd9-9dbe-3380-bf25-9f6f2081780c | -13.8569 | -44.5421 | 2024-10-10 00:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| a0f02dc2-700a-3be5-8c79-3ce3e3eb7ce4 | -13.8574 | -44.5185 | 2024-10-10 00:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7507343b-9a22-3ec3-b634-33de595d91f0 | -13.8579 | -44.4949 | 2024-10-10 00:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| fb9ea768-50b8-3f64-ac21-8d54302aaa4a | -13.7346 | -60.6079 | 2024-10-10 00:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fdcc7ec3-b2c4-38ee-84cd-c1db9b4ec6a7 | -17.0549 | -45.2808 | 2024-10-10 00:56:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 38b4b519-e98d-3f82-9549-8d92adda9011 | -21.621901 | -47.109299 | 2024-10-10 01:02:05 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6307466f-d984-3c5b-936d-6fb83d3050d2 | -21.624901 | -47.120899 | 2024-10-10 01:02:05 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 18227add-236d-331b-b4de-6f4387238f52 | -17.0481 | -45.2617 | 2024-10-10 01:03:11 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab43e2a5-a733-37aa-b58b-71c4043460f0 | -17.033701 | -45.246498 | 2024-10-10 01:03:11 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7f80a4-2ad4-3f5d-8b15-afc35bc68437 | -17.0385 | -45.2645 | 2024-10-10 01:03:11 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0ba46a-6d40-3d92-b82e-05739255c15d | -13.8386 | -44.489201 | 2024-10-10 01:03:59 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19e3a0bc-aff1-3f91-9ef5-fc94ae26dfde | -13.829 | -44.491901 | 2024-10-10 01:03:59 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4e15dcb-2499-3fc1-8e47-d584af388789 | -13.8351 | -44.514702 | 2024-10-10 01:03:59 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 968225bf-afdf-3b17-99ee-d38ab0ed710e | -13.8193 | -44.494598 | 2024-10-10 01:04:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f14ba39-14b1-3b56-bf3a-67ac68eddf25 | -13.8255 | -44.517399 | 2024-10-10 01:04:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d47585c-4e82-32b6-b0d5-fc21ca2be12e | -13.8097 | -44.497398 | 2024-10-10 01:04:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 357bb231-b0c7-3a23-901e-a25e31486632 | -13.8159 | -44.520199 | 2024-10-10 01:04:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c607b70a-5f34-39e5-937d-1a9133c9c969 | -16.6112 | -57.085201 | 2024-10-10 01:04:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9c9da43-6f0d-38a3-b136-e0e0b33dc8cf | -16.6129 | -57.0937 | 2024-10-10 01:04:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a0a5b5a-64bf-3a70-b1da-319058be15bc | -12.2636 | -43.697399 | 2024-10-10 01:04:21 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8d1ee4d-212b-3396-a290-d3261c4ba192 | -12.271 | -43.7248 | 2024-10-10 01:04:21 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9daf1fa6-8738-3e59-ad90-e8e8d78e1c5b | -12.2541 | -43.7001 | 2024-10-10 01:04:21 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d03397c-abc8-3bad-bd63-fbcc0e584e15 | -12.2615 | -43.727501 | 2024-10-10 01:04:21 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2156cfa-161d-3a90-ba7b-e794ea59ba27 | -12.9659 | -46.193802 | 2024-10-10 01:04:21 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4a422d93-1ab7-3998-98b4-4ba44516b87d | -12.3488 | -44.708302 | 2024-10-10 01:04:24 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98000040-7d8c-326b-8233-d205dda8ba9f | -14.1441 | -54.202 | 2024-10-10 01:04:33 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2345e7f-effd-3b0c-9ca0-bbaeee762d9d | -11.5102 | -43.996399 | 2024-10-10 01:04:35 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| faa88210-8bbc-3003-b05d-e94b5ca2073a | -12.1847 | -46.6889 | 2024-10-10 01:04:35 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0fd949f-d000-35d0-b768-6e78aff5f999 | -12.1891 | -46.706299 | 2024-10-10 01:04:35 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48d9335f-83fe-3b91-a365-3213515af04c | -12.1936 | -46.723499 | 2024-10-10 01:04:35 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a44f338-e109-3306-b4fb-25c65bb1d7a1 | -12.1794 | -46.708801 | 2024-10-10 01:04:35 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d72a71d4-a1e2-3245-b1c8-aa7bdec8d3ba | -13.1883 | -51.697201 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55227994-4470-31ea-b3db-59150bce1351 | -13.1902 | -51.705502 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c39c4c3-c292-37dc-a486-2948d338b191 | -13.1706 | -51.6661 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| caeeeb74-e698-37cf-931a-2c0fc0134221 | -13.1726 | -51.6745 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7b1eef1-4df1-3df4-8a63-ef95eca0e080 | -13.1746 | -51.682899 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9907db7b-283a-3c8e-a246-a94e84139405 | -13.1785 | -51.6996 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f45b507-c492-39d3-8755-f8b72afe75a9 | -13.1804 | -51.707901 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a896ff7a-9c15-3c22-bcf5-b9ec47dc54d0 | -13.1608 | -51.6684 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8baa1c1-371d-3ec5-8787-80281e6f1895 | -13.1628 | -51.6768 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4403e449-1364-347b-8777-9291136043ba | -13.1648 | -51.6852 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbcce69c-38d0-34b0-9045-a947df39d733 | -13.1667 | -51.693501 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a14ef2f8-54c4-3511-afcf-99b655ebbaf2 | -13.1687 | -51.7019 | 2024-10-10 01:04:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3362d98d-8397-3db7-a19d-1a75eab8df8c | -13.1276 | -51.658798 | 2024-10-10 01:04:40 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 944fdc6a-0aad-3cc1-be24-fe13214e645c | -12.926 | -51.112 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dff1e56b-039d-3edc-acd7-04a61a1cc362 | -12.9281 | -51.120998 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 691d4fff-55cf-399d-ab79-3310a6491676 | -12.9302 | -51.129902 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12b75c6a-36c6-3582-a40f-9e6421899178 | -12.9323 | -51.138901 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbc900cf-3eb5-36bd-b573-3a3663b7e249 | -12.9163 | -51.114399 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58a43e49-860d-32cd-89b3-481ba480f13a | -12.9184 | -51.123402 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a00c188e-0034-3374-b825-442e7fa3e19b | -12.9205 | -51.132301 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
