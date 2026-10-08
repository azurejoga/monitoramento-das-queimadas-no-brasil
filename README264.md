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

## Dados Diários - Página 264

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc973e25-fd1f-3e07-a873-56fa0b82bb53 | -7.57285 | -40.00278 | 2026-10-08 16:18:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 15.7 |
| bb5f8300-18b7-3d27-81f3-04c678d431d9 | -9.90168 | -44.81075 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 591dab64-4784-3f8d-9f94-c868f0829489 | -8.33006 | -45.04215 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f747cb3c-a894-3404-a58d-800a7fb014f0 | -13.18773 | -43.504 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0b6e78f6-5d79-394b-afa9-2b15b0acf036 | -11.13681 | -46.11923 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 90480057-b528-3a27-bdbc-79a3e01142fe | -8.95632 | -45.1431 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 6c51d80e-a584-35a3-9f38-fd64b5e7c2b6 | -10.7636 | -46.57945 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dac37e21-f5b4-3db6-8954-cf215c4abe83 | -10.94046 | -45.3807 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7b65214e-8b8e-3024-89fa-e28d080c6db3 | -13.69663 | -49.12472 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 06f1b76c-d080-385c-af48-2c6dd4a0b832 | -11.31011 | -46.68991 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7a17c7b9-6ca4-31de-835a-2386ab032198 | -11.95457 | -47.76824 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 401b577e-2c40-33a4-bc4f-89fcb6e179ed | -11.30622 | -44.83494 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b6790c8c-cec7-3576-b9e1-85d73a825376 | -12.41082 | -46.43999 | 2026-10-08 16:18:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1f8e0989-5268-300b-bdc4-51b2b80e466f | -13.11983 | -46.36185 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e88f8ded-c69a-3948-925f-1a4cd9768032 | -10.16826 | -44.66942 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 753e4805-75a8-3cdc-9e47-50b3acf3c8da | -9.03105 | -44.36934 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ce73baf7-84db-37da-89aa-8f18ad244202 | -10.87874 | -47.60693 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1a619f2-f62e-3853-a08d-11a96d834d10 | -9.59967 | -48.66042 | 2026-10-08 16:18:00 | NPP-375 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32ecae9f-b0e8-33c0-b881-6f4825631067 | -11.34535 | -46.72239 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1d0339e5-a937-36b3-abb6-f5ea7e58ee11 | -11.76763 | -47.74268 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 48a6e4d4-efd6-3747-85df-3e6f01310d53 | -8.28747 | -45.48168 | 2026-10-08 16:18:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8e5bc474-ab81-3ab1-85fc-5d7c702a3948 | -8.7517 | -46.84174 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| dfb2357c-eb56-35f6-b0cf-06ff57e9333c | -12.90632 | -43.28577 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f9dbfce6-2a4f-35ac-a835-55161c2b7466 | -9.07525 | -42.62963 | 2026-10-08 16:18:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 46103947-ce8d-3ed1-831f-555f2a73355b | -11.77279 | -43.5376 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 81bd9184-571e-3dc8-a67e-fb8201aa5dcb | -10.76561 | -38.72677 | 2026-10-08 16:18:00 | NPP-375 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fb11314c-645b-31a0-a78f-cde542848954 | -9.55236 | -45.22959 | 2026-10-08 16:18:00 | NPP-375 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 715ceebc-5e66-3772-9de0-d8aaec4572ba | -8.96774 | -45.1339 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 92d8ae13-56b3-32ae-8328-2d4a2489953a | -12.75491 | -39.55936 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| d3be7c83-726b-3db6-81a3-ad96484c0f7f | -10.41663 | -47.2872 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10925647-d398-3ceb-a75a-42bfc307e14b | -11.35244 | -43.15011 | 2026-10-08 16:18:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 2d0b80c2-e66d-3954-818f-221d78c1c051 | -11.30888 | -46.67998 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ef177461-86b0-3741-b87e-c383e6902126 | -8.94734 | -45.1756 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| e10c9521-cd4f-323c-a908-4f5795d39ac4 | -12.97167 | -46.93659 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 812ea0f8-7bfa-383d-b230-41015d8a472a | -10.83942 | -48.12992 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b9bf9daf-4ee3-3ddb-b8ba-0e07298a9c4c | -12.30801 | -47.23139 | 2026-10-08 16:18:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e354fbad-cdab-36e7-b38d-4ef09671debd | -11.63623 | -43.7067 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a1982d1e-248b-3b5d-9a49-3bf403dc1465 | -13.11945 | -46.35873 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7f5cb4c5-d048-3c22-97e4-6d277f74f46f | -9.77695 | -45.88659 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7a8b891b-ac50-3ba4-a4bf-e9e07441c001 | -6.75288 | -35.98724 | 2026-10-08 16:18:00 | NPP-375 | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8019aefd-4b8d-39f3-b1c7-3a40016bd28d | -11.20141 | -49.41878 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 14697bc6-205e-3494-b29a-b130dd177dde | -13.01449 | -47.202 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afc37c87-e582-3d04-967d-c86f47c022db | -11.25398 | -45.18412 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f5b14e1e-4167-3415-853e-4f1c96bf3935 | -10.41923 | -47.27068 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3259e530-9327-3c1b-bc7a-2e7074195ba6 | -8.55446 | -46.92598 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 32d19158-63b0-3836-9006-85421e599f1f | -11.00254 | -45.42101 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2c357ae4-ab8e-3c63-bca5-7595b9574e1b | -10.95504 | -45.38385 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a946d514-1bb2-348b-8164-64c1af40025b | -11.58041 | -43.67168 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| e43bd6df-74b9-3333-9860-5da1f9936c1d | -8.28802 | -45.72387 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 08883a9a-dbdd-366f-a05e-6ab508fbb2b3 | -9.92307 | -44.8034 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e85f7bd4-3d17-3b42-bedc-ca5a014e148e | -11.09273 | -44.00346 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 129aed96-c492-3173-acc6-41496380bf52 | -12.2241 | -44.73977 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c08dbcf1-7fc5-3226-99d8-9b0d46915d3f | -12.15979 | -44.74658 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 015d0bfa-6b14-3de4-8715-4f781a8dbac6 | -9.90104 | -45.19208 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 62cf4da7-f95f-3c1d-9e03-088cf9a849c7 | -11.72495 | -43.42139 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6241b36-e3be-36bf-96a2-2f725bc6b5c3 | -12.04316 | -43.43804 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ef28903c-e907-32e6-92bd-d8d3b27bfef6 | -11.22174 | -45.26126 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 47ba79e4-57ac-30f7-94ff-fc381cbcae3b | -9.35708 | -46.57371 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0da0769c-5919-3cb1-aa2f-4d135ea4a126 | -11.77823 | -47.73776 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7259c156-795f-39ed-9e78-64d67b2ffaa4 | -9.90815 | -44.79229 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d4e07124-c883-3e34-9ce5-308172539bcd | -11.2075 | -49.4179 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| dffdc2fc-c3f1-3bb5-83ad-df724d41c06c | -11.21147 | -47.71806 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15ba578b-3838-3579-869c-f9014e83f641 | -13.95494 | -44.85864 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| dc86e63b-b5ea-397b-b278-349f9df7547b | -10.60329 | -43.8394 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 44bf08c7-a415-3425-a13a-86a683d419e6 | -10.46429 | -47.24779 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8a35b043-8b34-331f-ac1e-7a276eeb887a | -11.46355 | -43.38687 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 7b1824ef-55ea-3fe6-b9ac-86b74254329f | -10.45279 | -47.28306 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 79c233dd-2f4c-3c7d-a777-0ca2480e2fe2 | -9.93632 | -43.57689 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3b76d607-b319-314a-992d-c4bb015acd96 | -9.76857 | -44.78442 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d394d6b5-fd60-3684-900a-d92751bd4684 | -9.84206 | -47.85523 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 978cf1d5-ef07-3fac-bffb-044f812c5ebb | -11.6498 | -43.67686 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9067e941-5907-364b-91b6-db54701b967c | -9.80453 | -47.82029 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a4835106-0928-30ba-9174-c0a962701869 | -11.82246 | -40.4904 | 2026-10-08 16:18:00 | NPP-375 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8fe17813-9e8b-3ddd-85d9-3d2a401f922e | -11.45946 | -43.38744 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b4c0e3fc-b6b9-3a11-bb2d-cd6ace2ad04c | -11.77228 | -43.53382 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| f467400c-1517-3f21-82f7-658cbc0efbbe | -11.77536 | -45.57326 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dfa1c71b-7bec-3bc7-aa26-1f410ad53104 | -9.35043 | -46.57537 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 11890c9a-469d-316e-beb2-f197c66c2e09 | -10.96559 | -45.39224 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 07a58bea-f7a9-382b-a41a-34fd8269039c | -10.33147 | -46.61369 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 834d44c6-3211-37f4-a0ab-1c8a8a3d1063 | -11.09169 | -44.02781 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| afc460cf-34b5-32e2-9aa3-7af35877a4f1 | -7.56607 | -39.04527 | 2026-10-08 16:18:00 | NPP-375 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51d424e3-d80b-3d41-a755-aac62e10aaca | -10.48249 | -47.22378 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a75ad91-e7e0-33a2-97ca-58f544b76787 | -8.5952 | -45.0857 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 74b7ca84-e604-39f1-bc1d-bcfe8bad65db | -12.25601 | -44.42434 | 2026-10-08 16:18:00 | NPP-375 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd217e6c-9e42-3935-9492-ee44dcbafcea | -14.02895 | -44.03031 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e524aa5-b6fe-3bd4-a570-5516e32de944 | -11.21771 | -45.26649 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 59e770cb-37ae-34ff-830b-c9f5b59fdb50 | -10.61387 | -46.27585 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| afb10da5-b711-3746-867e-9c0d9815da77 | -9.97499 | -43.49922 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fcf6c47f-8e4e-3e74-b254-fccc368e31d3 | -10.68405 | -47.83159 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f57b3f7-e792-32e0-9f6c-f1dac74a2287 | -12.61338 | -44.54574 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| b1db4fe2-06e5-3279-946e-78810cf73a36 | -11.76938 | -45.52777 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a0c1ba70-9853-3514-99f1-e638effca969 | -8.88928 | -45.39281 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e5b27ce9-5492-397e-a781-a178a149116f | -11.40569 | -47.5748 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bbf38429-48d3-3987-a494-a55c0069e0f7 | -12.03316 | -43.43916 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 274aa891-4b91-3d8b-9a9e-f28ad75f6709 | -12.17669 | -44.80559 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4f245b2d-4591-3684-9bb7-ca09023bee16 | -8.30356 | -45.73551 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c0d725e-40d4-37bf-8a4f-7868421bc644 | -12.28625 | -45.31898 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 134487f7-2af1-377f-ab03-c314c2de93c1 | -10.49983 | -47.31633 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e10dc1d-fd70-35f6-9663-fa8e498e2afd | -14.18064 | -48.6734 | 2026-10-08 16:18:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27b3bf47-9fd7-3c14-9ad8-9c2b9e00adec | -10.47317 | -47.23403 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README265.md)
