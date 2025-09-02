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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2179ac3-596f-3f89-a0db-6d20281d0e8e | -7.5476 | -61.3437 | 2025-09-02 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 198.4 |
| 46f45c9f-bd3a-3fe6-b4b2-71154a9607bc | -12.9385 | -56.9655 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b4333974-e3a3-3e97-8c06-3523c9e97c50 | -11.1037 | -44.6315 | 2025-09-02 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4c3acf36-2a42-39d4-8172-fbb54df8fed2 | -11.6647 | -57.3533 | 2025-09-02 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d4dfd27b-7921-3919-b0ec-6c418cc6dd7e | -5.6079 | -45.0265 | 2025-09-02 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| db7c9335-e6df-31c0-9ef4-2baa05fc85aa | -5.6081 | -45.0038 | 2025-09-02 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| c3f84e33-9fce-383d-8ecd-f38efc2ed8c2 | -11.6458 | -57.3548 | 2025-09-02 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 25cbfd65-968c-34fd-bf27-8135bd51c692 | -15.5666 | -48.3469 | 2025-09-02 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8a1fbd97-2899-3398-bf6f-c74280005fe8 | -7.5291 | -61.3444 | 2025-09-02 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ccd2f08b-ec22-32c0-823b-e030cceeabbe | -11.0526 | -45.399 | 2025-09-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 73e677ab-b3f7-356d-bb6f-5c87d8e0b91e | -17.8815 | -47.161 | 2025-09-02 01:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2e2020b8-449e-3457-84e0-8d6606a14b11 | -6.8279 | -52.8348 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bed95f1e-a527-30f3-a78c-42acd902b018 | -10.45 | -54.7785 | 2025-09-02 01:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 23f46348-bc26-3f0a-960a-ca4a0257216e | -9.8617 | -65.0334 | 2025-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 14fe9c58-622a-3b61-b542-f463049a0478 | -7.5292 | -61.3254 | 2025-09-02 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6b33bdb8-3592-3658-bc00-e2bbd81f4a5f | -7.5476 | -61.3437 | 2025-09-02 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 182.9 |
| e691d5b6-a19d-31c9-8700-55b5771d214a | -5.6079 | -45.0265 | 2025-09-02 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 368f3489-ee96-3d77-82d7-03380fb0e39e | -22.5307 | -46.8109 | 2025-09-02 01:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.6 |
| de749ff0-85f9-31a3-9ffa-d38b01fd73b2 | -5.6266 | -45.0252 | 2025-09-02 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d2adf33c-37f6-3ca3-9f58-8d24a58392c8 | -7.4778 | -45.3739 | 2025-09-02 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 38771942-87c7-3b09-a43f-87920e3d583e | -10.0617 | -48.1417 | 2025-09-02 01:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b65d2101-3910-376f-9600-159231963044 | -8.5135 | -63.8987 | 2025-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 27163e34-8b49-323a-a02a-079670840564 | -8.9664 | -65.961 | 2025-09-02 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 2ca3399b-b854-3935-9233-e9fd5d70813b | -8.9664 | -65.9796 | 2025-09-02 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 918cf696-c33c-3608-bdfe-e06096a5905d | -11.0845 | -44.6343 | 2025-09-02 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a273b8f2-4b2e-3a9c-8d4e-290281c8afcb | -17.7096 | -46.873 | 2025-09-02 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| df6f4a15-26d1-3f52-b8c0-786235d6a9e8 | -6.1859 | -47.2845 | 2025-09-02 01:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 064c671a-b2e5-3f74-aeea-ded88bdbae02 | -6.1672 | -47.2858 | 2025-09-02 01:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b066cb72-05b8-3e25-8f60-aba4242e5728 | -11.1037 | -44.6315 | 2025-09-02 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| b2e4b0f0-e9c9-31b7-9024-859cca7a5ee3 | -7.5477 | -61.3247 | 2025-09-02 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 36004432-4502-32ed-ae56-af260e397d2d | -8.6673 | -62.8369 | 2025-09-02 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 13bad49e-1886-3b1a-a739-ff3a26dec1d2 | -6.8095 | -52.8154 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 091ab86b-f46e-3c14-907c-3d69611bbd75 | -6.8281 | -52.8143 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ae452701-1859-3daa-9255-a75dd626ea37 | -5.6268 | -45.0025 | 2025-09-02 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 733b094c-d4d2-390a-bfd9-234ee130fb34 | -17.7091 | -46.8962 | 2025-09-02 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 28562722-6110-36f4-bf19-32f10d0783f6 | -3.2305 | -47.135 | 2025-09-02 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 431581e3-b773-3d58-b64d-dc9f069462a2 | -7.6783 | -61.0908 | 2025-09-02 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 94cc449f-aa65-35a9-8282-79c60fa04213 | -6.7909 | -52.8165 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| dd72b5cb-a0e8-3821-b1a0-0f95554cd06f | -10.062 | -48.1197 | 2025-09-02 01:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 976682ab-1a3a-3252-bb5c-6b8499562fa7 | -6.4029 | -58.2173 | 2025-09-02 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 69721ce6-b602-3539-912b-6f15a415e250 | -9.8616 | -65.0522 | 2025-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 2125dca4-9e69-3df3-b116-05569cd3750a | -12.9197 | -56.9471 | 2025-09-02 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3a6b0f36-eedf-3d37-9002-f648e5921284 | -6.2674 | -44.5213 | 2025-09-02 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c7e126e5-204d-3279-9593-88999576a60e | -9.5913 | -40.3448 | 2025-09-02 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 643dbe4e-40c6-383b-a70e-878a3aae29fd | -6.403 | -58.1979 | 2025-09-02 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2539c23b-dc44-3f9c-9ea0-91456997241c | -12.9385 | -56.9655 | 2025-09-02 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a2707238-e61e-3e08-aecf-cb932625ab8d | -9.1207 | -61.4864 | 2025-09-02 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 701d0fd3-9169-3f60-a8e0-bdf752f736bb | -5.6081 | -45.0038 | 2025-09-02 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 4821305b-906a-37dc-8282-cde5c75c0f42 | -11.1033 | -44.6548 | 2025-09-02 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8e8f29e8-9b68-32e3-8d50-05185669edf6 | -6.8466 | -52.8132 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 991c4bd4-4469-3987-a98d-2f2f616fbb50 | -8.5134 | -63.9175 | 2025-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 40b4407f-2fd2-31ea-aa03-f7bedde79611 | -12.9194 | -56.9672 | 2025-09-02 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e344ea17-3f53-3513-bd83-ef46b0dd8b9d | -6.8093 | -52.8359 | 2025-09-02 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1fa5dd67-68b9-3a5c-b4ce-ac537a0df40a | -3.2306 | -47.1131 | 2025-09-02 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 55c28466-22d6-38cc-9858-d946b86122bd | -6.1672 | -47.2858 | 2025-09-02 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 8113ae12-821c-3b88-9aab-c6142b8ea90a | -7.5476 | -61.3437 | 2025-09-02 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 80e49d54-853e-3c81-90ab-ef6366b7ee52 | -7.5477 | -61.3247 | 2025-09-02 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 177.8 |
| d931abb1-03ff-3478-b45e-fe19bd729cf7 | -8.5135 | -63.8987 | 2025-09-02 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 67653043-9d34-390d-9617-74f48334e98d | -6.8279 | -52.8348 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b5349195-4df9-3976-8097-1adb1b17a6d5 | -6.1859 | -47.2845 | 2025-09-02 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 3a24ece3-7f5e-3fea-82c8-5911ad1fb301 | -15.5666 | -48.3469 | 2025-09-02 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a8f31bd8-7b2b-35a7-80f7-a26211c53a53 | -9.1207 | -61.4864 | 2025-09-02 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2d210254-4094-3dbb-80e0-13dff2e01bd7 | -6.7909 | -52.8165 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 379d7e5f-6865-3611-a585-9bd9c7fa073e | -6.8093 | -52.8359 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c7c40165-d6bd-3908-a2ed-b0cd1af2750a | -17.7091 | -46.8962 | 2025-09-02 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e063fdff-cfe1-3e4a-ab45-620e5dc832b9 | -3.2305 | -47.135 | 2025-09-02 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 01315f26-110d-3dbd-8b89-f7556635a36a | -6.8281 | -52.8143 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e408eb03-9c86-366a-857b-122a42ca056a | -12.9385 | -56.9655 | 2025-09-02 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0dc2ab90-a054-305e-bcf7-0b14556274a9 | -6.8466 | -52.8132 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c9898cc0-cd15-3e27-9291-a90bc0c4ffc6 | -6.8095 | -52.8154 | 2025-09-02 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b89c518d-ff9d-358f-94ea-3117f981b6ba | -14.2692 | -45.2403 | 2025-09-02 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| d24bd50a-5a7c-3e4c-b464-73302ef0ca72 | -22.5307 | -46.8109 | 2025-09-02 01:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 4a96bac2-2243-30a8-b0fe-0ed96e23761d | -7.5292 | -61.3254 | 2025-09-02 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1dbce3f1-2363-39ca-9a32-8b0520d75eed | -9.5908 | -40.3696 | 2025-09-02 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 53b2562e-d2b3-3a55-8de7-bb5057ab3be9 | -9.5913 | -40.3448 | 2025-09-02 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 158.3 |
| e8046b5f-7274-3cee-8b8b-5ae231e3bf0a | -6.4029 | -58.2173 | 2025-09-02 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d55af70d-dcdf-3371-aa9c-8bb7b9081642 | -8.5134 | -63.9175 | 2025-09-02 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 91ad4476-dda2-3f49-947f-b98ee9668b76 | -6.403 | -58.1979 | 2025-09-02 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1661964b-8253-380d-b561-aa60dd87b8e6 | -17.9016 | -47.1569 | 2025-09-02 01:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 87647d6e-f4c6-3167-a25b-e14ee45ea96d | -17.7096 | -46.873 | 2025-09-02 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| cdb8567e-05b1-3d99-a1ba-11c4035be6f3 | -12.9197 | -56.9471 | 2025-09-02 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 1bcfc9c8-5183-3785-ba16-3c679f3cfa7a | -11.6647 | -57.3533 | 2025-09-02 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 46a07cfa-126a-3b5c-aa7c-91eec7f2cdba | -5.6081 | -45.0038 | 2025-09-02 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ab6b00a5-a559-31a9-a0c7-b952ba8251b9 | -10.0623 | -48.0978 | 2025-09-02 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0738956e-7fdb-3692-98c0-d39e03561ff8 | -5.6266 | -45.0252 | 2025-09-02 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 6b8fa01a-8a63-38fa-a3d7-d6432de62a14 | -5.6079 | -45.0265 | 2025-09-02 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e359d9ef-2cc5-37ee-9fe4-8966b1433b47 | -5.6268 | -45.0025 | 2025-09-02 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0bc97dee-86d1-3b6b-8eb1-e4f7f3acc99d | -11.1033 | -44.6548 | 2025-09-02 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 036c8134-4db4-35a5-8b82-ae07b2faf5d9 | -8.9664 | -65.9796 | 2025-09-02 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| d43d4d50-089c-368e-a098-f09f533329ab | -10.0617 | -48.1417 | 2025-09-02 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 02463e0a-dc3f-3a15-8883-ce12fde25302 | -10.062 | -48.1197 | 2025-09-02 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 93dd001a-68d8-3a41-8ad3-09209c23511a | -7.6783 | -61.0908 | 2025-09-02 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 467f1ad9-ec26-3716-8a2b-b4afffb96d3a | -7.5291 | -61.3444 | 2025-09-02 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 28f88b43-5bbf-3d77-8c4b-00e65e2e986a | -17.8815 | -47.161 | 2025-09-02 01:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 17b4cf27-b5e7-3383-93ed-9292fcf4d31c | -8.6673 | -62.8369 | 2025-09-02 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f747c89f-87ad-3f1a-bf9f-9b34d63d0997 | -11.1037 | -44.6315 | 2025-09-02 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d8628aed-5bfe-3125-8495-af3ed80b9d01 | -6.7909 | -52.8165 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 24799bf8-2033-3782-957a-4f4adce0a41d | -7.5476 | -61.3437 | 2025-09-02 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 3d170cf3-7d95-36db-a4a1-ccb1c9c01ce9 | -8.5135 | -63.8987 | 2025-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8c3c59aa-9493-3b9a-aae0-9a82bce32193 | -10.45 | -54.7785 | 2025-09-02 01:40:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |


[Clique aqui para ver as próximas entradas](README9.md)
