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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa8d4802-0c17-3fdf-b2fb-7b3f68a31cbd | -11.82757 | -43.54185 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 749ffaff-3dd2-3852-ae3f-0218b9f2bca4 | -10.95144 | -45.39069 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1bb2b083-a57b-38d4-9a81-80081d4dcb7d | -12.81009 | -43.31545 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5a155cbf-9d0b-3d3f-898d-a86fcf55eb59 | -15.88601 | -40.7168 | 2026-10-05 17:13:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 86a6db3a-d75f-34fc-b883-8cf8ad953a46 | -11.82824 | -43.54546 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 836d7f53-9f2a-3f73-90fa-daed98c01fa8 | -14.9596 | -41.43079 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 8f8ec6a1-cc00-32db-aa0f-c6722d2ba3bf | -13.52015 | -61.11403 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 44f323ce-a43d-3ff3-8cdc-eadbec1b4af7 | -11.34025 | -46.66647 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c6d4d827-79fa-3f01-a2e5-a91c76d958fa | -11.63597 | -43.61357 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7b7da451-523e-3054-8f9e-5b99ed0fca0d | -13.50616 | -61.13271 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba6caf44-8421-3d7a-8b77-1ae4cbc529f6 | -9.40264 | -40.31899 | 2026-10-05 17:13:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4be4ed88-22d4-3199-b56f-ff0ae707d809 | -10.96853 | -45.43232 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec8b8f62-3d86-3cab-b981-f1e569622eb3 | -11.72411 | -43.50681 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4196dbae-e995-3998-aa32-29f84473b4d1 | -10.36658 | -48.10344 | 2026-10-05 17:13:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b59a8c67-e38c-3ed1-90c6-3182fc817f8b | -10.94769 | -45.42263 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 63bccf4c-dfdb-356c-ab6d-1dadcd17d838 | -9.84841 | -44.78551 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7bd98afc-3c05-3a38-b517-e534218c11fe | -11.68512 | -43.66732 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 12603be2-e170-320c-80b3-bc08385f9da7 | -13.6037 | -42.49948 | 2026-10-05 17:13:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| a9ca321e-b1d0-3b73-aaf6-375cf6dc9106 | -14.52869 | -41.56856 | 2026-10-05 17:13:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 727e0be4-d06f-3188-875e-db199aa5052f | -12.76833 | -44.20421 | 2026-10-05 17:13:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8fa9c0f8-eb91-37b3-80af-4a88d6499142 | -9.8446 | -44.79237 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b12462a5-b512-3f72-9732-80de1ea8b213 | -11.95432 | -40.64051 | 2026-10-05 17:13:00 | NPP-375 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 400d9876-e8d2-35fb-8659-637071ad7489 | -11.37981 | -42.55161 | 2026-10-05 17:13:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| fe895345-9756-368b-9434-2d45782cd16b | -14.0114 | -41.01629 | 2026-10-05 17:13:00 | NPP-375 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 15f49c1e-1dac-3466-b4eb-f17cdb602e92 | -15.58584 | -40.31746 | 2026-10-05 17:13:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 01a8741a-0206-3aae-9d1f-38b7ee554675 | -10.44789 | -48.32644 | 2026-10-05 17:13:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| dc0228e6-c040-349d-8b27-bd5019290d00 | -10.98206 | -45.45452 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 96874d36-922d-310e-ab58-064113a33839 | -14.55466 | -41.70518 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f5e1c93f-17b5-3cab-9d4d-38e08a95c1df | -11.65606 | -43.60688 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b0c8571-03de-3a7e-8816-08202a3cc5fb | -11.6423 | -43.61893 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 606d4bc4-ecf1-32a8-bbdd-5d0cd1dbf062 | -11.80963 | -47.36428 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26f4a7bb-dfd0-376d-8011-32fbce68c267 | -14.08212 | -43.76977 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c00a29bc-d0f0-35e0-a9c1-08d445223d9b | -10.24362 | -49.65274 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf04664b-5153-30da-b1ba-6c5de4375f2d | -13.5027 | -61.13747 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7c1e6a8f-6ff1-3352-acc5-27128650285b | -10.21708 | -46.6806 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc57779c-794e-306d-898f-4bf46df90ac0 | -12.34935 | -47.06514 | 2026-10-05 17:13:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0eaf3ce9-4b13-3467-97d2-74e2a7262596 | -11.80622 | -47.36855 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a614a890-c6b2-3cd0-8f3f-8d0cb249a025 | -10.44709 | -48.32161 | 2026-10-05 17:13:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| eb90b72e-283b-3420-b39d-00cec212ce1b | -9.6189 | -45.82158 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d349782d-847f-3df8-9d8b-344f76f6e10b | -15.70937 | -41.34394 | 2026-10-05 17:13:00 | NPP-375 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 49f24734-16a9-3c6f-b81c-2f26a10cf14a | -10.34308 | -43.73259 | 2026-10-05 17:13:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 553f3dd1-564f-3130-966b-69e28ba79b98 | -11.19077 | -50.80565 | 2026-10-05 17:13:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc64ec18-7277-3814-a4d0-68396d2ec44e | -12.62492 | -40.45905 | 2026-10-05 17:13:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 82dd197b-7a8c-3014-af15-d1c25ca6d46b | -11.3516 | -46.65648 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d566e20d-4e87-3d14-a1e1-be52df80083a | -14.92314 | -41.41182 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c88ae2cb-7dfe-3d2b-9b8a-c4cf608c3fae | -11.07419 | -47.49401 | 2026-10-05 17:13:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b8eded1-0a9e-327a-9298-42b79b81ddbb | -10.34956 | -45.02663 | 2026-10-05 17:13:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aba004db-3023-384c-80ff-8184a694dfbf | -13.50992 | -61.11866 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d2e92190-0cb7-30c9-890a-6a96a385d0b0 | -12.63026 | -40.70463 | 2026-10-05 17:13:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 36c31bfc-4d21-3edb-a0f0-6d71e816d6e9 | -11.2628 | -54.07104 | 2026-10-05 17:13:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3151783a-5ac5-32ef-b550-1b8ece92b6a1 | -11.19076 | -50.80538 | 2026-10-05 17:13:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| aba6655d-aa0b-3edc-b169-5384e41f39fe | -16.13573 | -40.7058 | 2026-10-05 17:13:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 6bf4f4ea-2654-344e-9742-204a1db69e8a | -16.27472 | -41.80413 | 2026-10-05 17:13:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 38f2b633-02c4-3dae-b6a1-c05f35d952da | -11.16088 | -43.49487 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a74e688-0fd9-36ac-905d-f7fa4172a7a7 | -13.51031 | -61.12202 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1102fb5c-aac3-3190-a5c5-5014f9267d33 | -10.24345 | -49.65674 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4942c993-bb5c-38a7-a867-ba826d2b769c | -12.86536 | -39.92349 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1f4b2809-f000-3d15-8268-76c67fc4f5f3 | -11.85406 | -47.30762 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fd41a464-37b3-3c92-b41c-b0ff22ab2106 | -12.81523 | -43.31445 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 06a0870a-509a-3c5f-a697-1d51dd4e5ed2 | -12.16063 | -60.74578 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6babb59f-198f-36c4-8d76-58e279633693 | -11.34363 | -46.686 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfadb1ac-652a-36e9-9a23-f4a8b5b60f0a | -11.68023 | -43.65126 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 530be58d-fa37-3227-864f-989a0ed6f0e0 | -9.82428 | -44.79786 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 001eae61-a13f-3f20-bbf8-9ae41179d5b5 | -9.84784 | -44.78753 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 38c677b3-72b4-3672-a4a2-a235b90f46a1 | -13.5168 | -61.13144 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7241e827-be1f-337e-8c85-4d01d9e4f7d1 | -15.26948 | -42.18439 | 2026-10-05 17:13:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 27c654fc-97c9-3730-811a-7fa04aebe13c | -11.11179 | -45.94836 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| a8d51f93-85cc-3fe8-a06d-a329ee3f834f | -11.68759 | -43.66237 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7c2bb28-9798-349e-8f10-3c3f2de21096 | -9.81933 | -44.79856 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 56f15cae-728d-39cd-bfef-321567bcd650 | -10.35246 | -48.18612 | 2026-10-05 17:13:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b88a5d1e-23d2-3b58-8a1f-434a23e00956 | -11.20471 | -47.13605 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c26ffe95-d353-3785-8d2c-7b10a92dbd30 | -10.44322 | -48.32224 | 2026-10-05 17:13:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e779faef-305c-33a7-84a7-c2be646cc9a7 | -10.94857 | -45.42746 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3e8f715d-e847-3b87-9801-82be7db7e6ef | -13.44716 | -40.05478 | 2026-10-05 17:13:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c5588971-0ccd-3f96-b000-36f7d89b38fa | -14.37198 | -41.67107 | 2026-10-05 17:13:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d8e0f178-28db-3796-ab6e-3cebd8e8c799 | -11.37471 | -47.52149 | 2026-10-05 17:13:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3143d6e1-b74f-3dc5-aad0-08231675baf5 | -9.87422 | -44.81558 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8d371328-6e4d-37ce-a978-21e0168b88a6 | -9.83768 | -47.01121 | 2026-10-05 17:13:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e53d7cab-dcf0-3a39-b049-40f7bf71b71e | -11.20665 | -47.14742 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62ad94d7-d50d-3130-9e1d-7f7a003d051a | -11.2514 | -43.5168 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a571828b-4110-356a-9c9e-9f73c6eaac7a | -15.83997 | -44.69738 | 2026-10-05 17:13:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7a94e3d8-5686-3a9c-ac61-2de0f0f38125 | -13.5832 | -58.89286 | 2026-10-05 17:13:00 | NPP-375 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45eb5cc5-1e42-3309-add1-ca7616776813 | -13.02173 | -47.77632 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af916d38-f326-3006-a2a6-01a144811382 | -12.5507 | -43.08331 | 2026-10-05 17:13:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22732c6c-84a2-30d7-bcfd-19ad65f40117 | -10.97053 | -45.41699 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9117d43a-0f1c-3af7-bbc9-529c8c0354a6 | -13.90634 | -43.86457 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 63657850-8d0d-3376-8b16-b38e30d3bf77 | -13.96844 | -40.98474 | 2026-10-05 17:13:00 | NPP-375 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 449cb260-0b10-3c81-804e-c4d13f3d2f2e | -13.64761 | -40.87988 | 2026-10-05 17:13:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| d1b45b2d-5e91-3d59-b0d5-775eb6546a4d | -11.37656 | -47.72391 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96b34892-8b8b-37fa-a753-9a5a27309995 | -11.75306 | -43.54715 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d33cefa4-bd7f-3654-b1fc-825ae5773287 | -13.45347 | -40.05383 | 2026-10-05 17:13:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| b387dbc6-2df1-37a6-823d-551f919198c2 | -16.55097 | -56.24142 | 2026-10-05 17:13:00 | NPP-375 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 50d2797a-5e9d-39b9-b3ee-a4e0a95ad6f3 | -13.52055 | -61.11739 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| baf29a9d-557b-3a9b-a820-2cfa6b865b37 | -10.49308 | -47.24305 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 437a5e88-100b-3908-8d8b-8d9e13f1c8b9 | -10.12073 | -45.89569 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93c240fa-4cef-3ab4-a58a-f63fceb0649a | -14.96048 | -41.43507 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a358a743-c9dd-395c-90b0-26866002e6a9 | -14.28365 | -41.49447 | 2026-10-05 17:13:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2f6b35f7-bef0-3666-8760-2ae89176d522 | -11.35004 | -46.67274 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 82e7affe-3f43-33a1-bf1b-f607ba0eed10 | -11.3777 | -42.55027 | 2026-10-05 17:13:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| e71c124d-f241-30e9-8a98-da096ea76837 | -11.70454 | -43.43121 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
