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
| 4cf6ead2-e823-3817-a3ad-40c303ca272a | -5.0287 | -43.59849 | 2025-08-01 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e2d0753-6b35-34f4-b720-dfad1baa1e26 | -8.5181 | -43.31922 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd1c8c50-317c-3f23-9b77-27373c27a252 | -6.99747 | -41.93858 | 2025-08-01 03:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8763042-b230-38c3-aa8e-2f5c0c85f6e2 | -7.28413 | -43.06088 | 2025-08-01 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ce831a1-a05a-3259-b6b9-376153d122f2 | -4.31643 | -48.10059 | 2025-08-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 30d5473e-37b5-3b30-964d-ac6c7fbb1a9f | -8.03389 | -43.12083 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| e65b97fa-93bd-3bf9-bfdf-d5b3b4e04101 | -3.40652 | -43.01522 | 2025-08-01 03:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30020202-2abf-39c5-8241-93bb7ae0ed0d | -6.57025 | -41.54045 | 2025-08-01 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 20f0cf40-21f7-35bb-b787-bc4d662cfb79 | -8.0396 | -43.11333 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| e404a02b-e711-3cee-b08b-3e2106588eae | -8.04252 | -43.12234 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 001aae16-90ce-3d91-90fc-b38f8edfe77a | -5.48245 | -42.15742 | 2025-08-01 03:49:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ac271fe-5d3a-32ea-8393-241793b23bc5 | -8.05511 | -43.11046 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 833aca6e-e63f-325d-aa77-dc7899d58658 | -8.51305 | -43.32261 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cd240b18-ba88-37ad-8044-48a6a6da197a | -7.72313 | -45.09217 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c4cbfe5-e65f-3e63-87d8-aa57d261145c | -7.74203 | -45.07224 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 299a5db4-eec7-351f-b27a-9a4a4517d421 | -3.50826 | -43.24055 | 2025-08-01 03:49:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8df73e02-2835-3533-87b1-981f437075c3 | -7.27978 | -43.06011 | 2025-08-01 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0879677-6a75-3b1c-b726-6751194235aa | -6.98938 | -41.9371 | 2025-08-01 03:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e99d7661-f037-3e7f-a96e-381f94b3f923 | -8.04649 | -43.10896 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b09d255b-9081-320b-b230-d008cbc8e414 | -3.69573 | -43.43561 | 2025-08-01 03:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56dc61ab-6dd8-3306-85a4-4348d21ac882 | -3.82278 | -41.56084 | 2025-08-01 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31aa100e-e047-37ed-9cca-10ae4296a786 | -3.50357 | -43.23979 | 2025-08-01 03:49:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c481dc8-4498-39fd-93d1-0409744c349e | -6.99402 | -41.93428 | 2025-08-01 03:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6c18135-244f-3357-80c8-94a09054e1f6 | -7.73305 | -45.09392 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b553b2c6-288a-30d0-8329-11cf1e877d60 | -6.69211 | -43.07461 | 2025-08-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f92986ba-8972-3130-99fe-1ced109a5d2a | -8.05008 | -43.11381 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 195e1848-a47c-34cd-8cef-0d26fbeeaacd | -6.41582 | -41.12674 | 2025-08-01 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25da56d7-db64-3e9a-a726-a418f78bfe94 | -8.05439 | -43.11457 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 032e5348-7675-388e-9cbf-44a240373fa4 | -8.04001 | -43.12053 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 1d65dd3b-2786-32c0-bd77-e30d5bb67dc6 | -8.53636 | -36.29571 | 2025-08-01 03:49:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ff203942-e7be-3c96-897d-e7f6ae744eb2 | -8.04391 | -43.11409 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 7886eb55-806f-332e-99dd-d605d3d231fb | -8.0446 | -43.10998 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 279fcf9d-a7b9-346d-aac7-bec1b225b656 | -8.06014 | -43.10712 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c88cb21-ad6f-3a07-a9af-bb1f1854af4d | -9.65096 | -40.58433 | 2025-08-01 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b91d2f05-bfb0-383d-9d9d-3ab26935401c | -8.04073 | -43.11641 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 24cc0cde-f562-3c3e-819a-9a6d9f004bc8 | -9.5228 | -40.34609 | 2025-08-01 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b949549-a91d-389a-a0cc-d7eed29077f4 | -3.50274 | -43.24469 | 2025-08-01 03:49:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b41962ac-54f5-3818-9da2-9dc749f6f7cb | -6.41982 | -41.12957 | 2025-08-01 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e233f778-5ed3-3203-92d6-ab766eeda0c6 | -8.0508 | -43.10971 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f4438b28-3b64-3059-b154-17a3ec96c085 | -8.38488 | -36.70305 | 2025-08-01 03:49:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96876cf0-ba5e-3bf7-a291-e05b62429d6a | -8.04577 | -43.11305 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 82b65a70-daf5-359a-992d-d38f479f17d0 | -8.03319 | -43.12495 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| ec323cac-c8e3-3eb8-9407-19e8275fb261 | -9.40354 | -40.52391 | 2025-08-01 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0e34c12-bfe4-337d-9080-938bb61a0da3 | -8.03642 | -43.11567 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cdb09c72-b06b-36ba-b736-ec3ef8a64282 | -8.04432 | -43.12128 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 18a8ff3d-8c70-3a55-9ea4-9c203be4a589 | -8.51448 | -43.31429 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 97dad13a-13c1-3233-af7e-c53e1d1911f0 | -7.7291 | -45.08739 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a13d2a44-1595-3949-9dfb-9ce35e6c1872 | -8.0382 | -43.12159 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 562ed948-90bb-3cf3-bbd8-1708c7646fca | -8.51519 | -43.31013 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 2bbc3705-0987-3b89-aea7-cef84b11b073 | -9.65166 | -40.58012 | 2025-08-01 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d23988c5-caae-3537-9d7f-4411297baf18 | -8.05654 | -43.10228 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7c6dce2-d7a4-3f9b-857e-9196722aeb09 | -3.69097 | -43.4349 | 2025-08-01 03:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2cfd319-b62b-3921-8d36-2848ae5c4414 | -8.03424 | -43.12801 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f07395c0-56f5-3d31-a32b-48e5b3cecb1e | -6.99343 | -41.93782 | 2025-08-01 03:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1081a49-7d40-3b5b-8202-3b7e4dc1b570 | -8.0389 | -43.11746 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| a937b9d2-4708-3b09-959b-800091395cae | -4.30916 | -48.10458 | 2025-08-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b13ac08a-b062-3edf-a2da-1c67a6c3dce0 | -6.57421 | -41.54122 | 2025-08-01 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1928ea7d-d8ac-3455-ad4a-776846bdb1ed | -7.73507 | -45.08262 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63db16d1-1590-3e5c-a189-2153a1b0f6ef | -7.87385 | -45.5407 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c1a79e9-1007-3f73-be7e-182036fd0730 | -5.0698 | -37.71612 | 2025-08-01 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 098c4d7c-4149-3c64-9cdd-dc5a39047b87 | -7.73607 | -45.07697 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4139f689-513d-3bc1-a0b1-4607184054af | -3.824 | -41.55333 | 2025-08-01 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7774c5ba-5c24-35ef-a95a-a41a54183e40 | -8.03751 | -43.12571 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| ffd38060-ad65-34c6-9652-4e79e6b46857 | -8.05583 | -43.10636 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 65e05ca4-7ec3-376f-a0f9-4aaeb4641e26 | -8.0357 | -43.11978 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| a55e6b46-8f8c-3ebb-b374-8b11bfa629e4 | -7.72708 | -45.09871 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03a50ee8-6a02-3d37-b132-e1991c600205 | -7.86873 | -45.53985 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c87c5445-a0a8-3f93-ac9f-35189917327d | -6.41891 | -41.13231 | 2025-08-01 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c8068a8-9a93-342c-aafa-bb24e8a02c0c | -7.8728 | -45.54653 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2ab06a6-4adb-3d7a-bb05-1b0f875210ad | -3.82339 | -41.55709 | 2025-08-01 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e67ebc6-f9c3-32c2-b891-2d7009db7864 | -8.51881 | -43.31506 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ef935e6-7ccd-3798-86bf-d1110eb7abf1 | -8.03928 | -43.12464 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 6f63b0f5-bb8b-30e6-98d4-9b011ffdb386 | -3.82509 | -41.57286 | 2025-08-01 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c39c9e9-4e13-394f-a554-ba50c0cfeaa1 | -8.04321 | -43.11821 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 6796208b-22d7-3c3e-89b7-cfd9b3366199 | -7.0503 | -44.40686 | 2025-08-01 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84dbc27c-a3dc-32c0-8c4d-579508cf4f21 | -7.86821 | -45.54275 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcccab98-12b6-3e9c-8263-6f15c481a5b2 | -6.57333 | -41.54638 | 2025-08-01 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c64f2628-74c5-3a6c-b08a-378b1b2079d4 | -6.7293 | -59.1916 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b1a99937-9ca4-3e55-8e0b-bbb12b3b3ff4 | -6.748 | -59.1523 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 5e6fd085-2cdd-3c75-8c15-650c3ff18bd9 | -8.0513 | -43.1001 | 2025-08-01 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 2b86f05f-418f-353d-a30f-887ce7a7fc20 | -6.7477 | -59.1909 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8869d078-e44c-3af3-9be6-0f208a668009 | -8.051 | -43.1237 | 2025-08-01 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| d02b1cc0-513e-3948-a068-69cd47f89d5f | -6.7294 | -59.1723 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 1b364bfd-daea-3570-899e-a4aa99bbfca7 | -8.0324 | -43.1022 | 2025-08-01 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| d4d336d0-c95b-3a98-ac9d-145fee03801d | -6.7478 | -59.1716 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.1 |
| c4d38c8c-468c-3197-8867-de9309475145 | -8.0321 | -43.1257 | 2025-08-01 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| eab9f865-1559-3441-8907-43c5c09a4828 | -6.7295 | -59.153 | 2025-08-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4f8eeb74-6fc9-3538-829b-2137d3ac694d | -12.43634 | -44.74827 | 2025-08-01 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a066605-7b87-39de-af35-dbe71240c100 | -16.1312 | -46.88213 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f8d40b8-5a3c-359f-8bc5-0b75a0587ce7 | -10.44999 | -47.27465 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df2077e-8686-3e9b-999a-850100476533 | -14.20937 | -42.84375 | 2025-08-01 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7657713c-536f-30a3-95e5-57787b3b55e7 | -10.4493 | -47.27825 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdeff2e4-e5bb-33b3-9586-5dd04e2a2461 | -9.86745 | -44.70449 | 2025-08-01 03:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c06e479-04c8-3dc4-932c-f32227393c4b | -9.80183 | -47.04674 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56a603b8-5713-3d72-b949-42ea837bf860 | -10.45543 | -47.27583 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfaa98ae-b5e5-34ec-b313-f574dc73f7b1 | -11.76469 | -44.99833 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b827d09-9605-34ab-b54e-65b7be270a61 | -10.08142 | -46.74266 | 2025-08-01 03:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03cdc497-8f46-35e3-8033-ce89acd3412f | -13.22385 | -47.24081 | 2025-08-01 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| afb5c8de-7bbe-35c3-933d-17d2176b53c8 | -9.52696 | -46.39734 | 2025-08-01 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f4dd7d7-e703-31e9-9dea-2c4880270a8a | -10.43505 | -47.26387 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
