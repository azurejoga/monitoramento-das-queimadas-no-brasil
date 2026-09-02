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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b33c9b3d-e110-3112-ba9c-dfb7da270e9c | -15.45286 | -52.68802 | 2026-09-02 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b7b56f2-43a2-3299-8569-ca235219e757 | -14.50442 | -59.8431 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3b1a791-3f55-3960-9a1b-387c1608fca8 | -17.09144 | -56.85624 | 2026-09-02 05:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 72ac186f-b294-3995-8ff1-9deaa4c121f9 | -16.19749 | -47.48872 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d184b1e-a7ee-3a69-b8e2-ab0082fba143 | -16.19151 | -47.49199 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c757d704-bf7a-3df1-902d-0a3e144aed09 | -14.51768 | -59.84531 | 2026-09-02 05:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f2fd1c8-3791-3601-80fa-fdd566b4f753 | -16.18348 | -47.49836 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9230ebc-7cfa-3450-8ef7-eda6109aed51 | -14.49893 | -59.83484 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ffdf261-d43b-34f9-9172-7d9162f776de | -14.49389 | -59.84501 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd21c2ea-2cfc-38c2-bec7-835a1dbe6c4c | -15.39644 | -52.7332 | 2026-09-02 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 593c0bf7-1f09-3005-be9c-4b86af87af56 | -14.51163 | -59.84061 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf7ae65-d94a-3e34-aa85-4d73d97fd64c | -14.49836 | -59.83842 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6378bcc5-d5df-359c-9117-892f2fc03d7d | -17.08783 | -56.85569 | 2026-09-02 05:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6830a744-1e4d-35ad-a487-ddf23db28628 | -14.50053 | -59.84611 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879d93a1-1900-3d8c-b1c7-697571bce61a | -16.18993 | -47.49895 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 984d30eb-cee9-3e77-bd6f-7d48c2cc53a2 | -14.5011 | -59.84254 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 921ee4f8-8bd5-3393-b95e-33c596c24399 | -16.19797 | -47.49247 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f8ae4fe-c7c3-3ee8-92de-46b45b68353d | -16.19694 | -47.49403 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21ae90d2-b389-3f85-9492-f7eb3bd4f86a | -17.08907 | -56.84707 | 2026-09-02 05:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4d10c17d-923e-3e12-885f-744fc26b94f7 | -14.51826 | -59.84172 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb93554-d07b-35f2-9220-cce36576b68b | -16.18402 | -47.49313 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bf4f013-7991-3d27-823e-318108845b39 | -14.51437 | -59.84476 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2ddd7ce-043f-3885-8610-49955f309d82 | -15.46737 | -52.64634 | 2026-09-02 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcb46af8-89c3-3679-92db-189bd94b34aa | -16.19101 | -47.48838 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79675ec7-d310-34d9-8e30-1b120b6d9d90 | -10.9009 | -45.3509 | 2026-09-02 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 50336ade-0bfc-3721-86dc-b3c6c0747eed | -6.6764 | -58.7686 | 2026-09-02 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 00b90366-d5ce-3489-891a-685cad144566 | -10.7774 | -44.7463 | 2026-09-02 05:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 061933f3-9f74-3e4d-b024-99d6f627af4b | -10.9204 | -45.3253 | 2026-09-02 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 046a1bdb-a498-319a-8f93-99b464b22a61 | -8.4671 | -54.7035 | 2026-09-02 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3e044c4a-3bf2-3f6c-a343-9e020aa7175d | -10.7962 | -44.7669 | 2026-09-02 05:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 3150fce3-2163-33b4-a3b0-a244cda2dc1c | -10.9013 | -45.3279 | 2026-09-02 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 4cb1ac05-a597-3a5b-b804-7dad2eda5092 | -10.92 | -45.3483 | 2026-09-02 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e6078474-62ac-3573-a1ce-36c3dcdec4ca | -8.4856 | -54.7225 | 2026-09-02 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3efd6feb-55c1-3142-9a69-d4dbcd7ed3f3 | -6.6949 | -58.7485 | 2026-09-02 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 111813d9-7ffb-30d0-9431-8abec4039c87 | -8.4669 | -54.7237 | 2026-09-02 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 1fdb93a3-8a43-3569-91aa-da2f76a57fcb | -6.6948 | -58.7678 | 2026-09-02 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ad07a1a1-e9cb-3236-9b37-a97f3a687919 | -11.3048 | -45.1575 | 2026-09-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| eed41b8b-cd56-3c4a-be93-72d3b27f5bfa | -8.4669 | -54.7237 | 2026-09-02 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| eff6757d-f29e-3a72-8ead-a675adb1fb10 | -10.92 | -45.3483 | 2026-09-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 62687d02-c4fb-39d5-a0e6-ca72bd4347f8 | -10.9013 | -45.3279 | 2026-09-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bec3873f-b9ae-3a0b-b71a-6f51eae49f26 | -12.6483 | -45.0718 | 2026-09-02 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 65aa7723-0391-3b1c-86da-347c17d8ea0e | -6.6948 | -58.7678 | 2026-09-02 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 556a7f91-14a5-3dfa-b27e-e7ec45650e42 | -10.9204 | -45.3253 | 2026-09-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| ad2f33f3-b422-3486-b8a2-25b4921d05cf | -10.9009 | -45.3509 | 2026-09-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1734a342-8b4e-333b-a479-743ed20507e7 | -10.9204 | -45.3253 | 2026-09-02 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| f98b31a4-f33e-36ce-9bcc-e1287f65708a | -10.92 | -45.3483 | 2026-09-02 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b994a9f2-d643-38bd-9931-e3d96186dbf1 | -10.9013 | -45.3279 | 2026-09-02 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| dba9783f-ba1b-345d-ab11-35348260957a | -8.4669 | -54.7237 | 2026-09-02 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 36ae31e8-bef8-3198-99f1-1e34a0695e1c | -10.9009 | -45.3509 | 2026-09-02 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 90c14714-b476-3e27-af5e-ea2a2f4c4808 | 4.32954 | -60.8204 | 2026-09-02 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a61126-41c1-3187-8f9f-2f649702b346 | 4.32502 | -60.82162 | 2026-09-02 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0adbc4e5-c195-3923-9179-41d92bec0cd4 | 4.32496 | -60.82026 | 2026-09-02 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8465b791-4e3c-3946-b9b9-158eff689b87 | -3.62392 | -60.56293 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef38b0c3-8e81-3513-9eb3-7b6a513ef898 | -3.11651 | -61.23668 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e35803-5b89-364e-bd99-6a985304d60d | 1.67015 | -60.13765 | 2026-09-02 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d646a502-98cc-3de9-9068-4591852ac83b | -3.12281 | -61.22875 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1179953-9ffc-335d-bc2b-bc193c1443f3 | -3.74939 | -59.32215 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7685b1ce-76c6-38a9-b7f7-afca6157a89a | -3.66488 | -58.91653 | 2026-09-02 05:59:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1295be00-0407-3622-8954-4e383c1c3e75 | 0.97755 | -59.38255 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9917febc-dbcd-3ab5-9a92-99f6be369a39 | -3.1973 | -61.13871 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbdf6642-c340-3475-bc2d-a4326a655c9b | 0.97492 | -59.4001 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8cb8ae-2a30-32d4-801e-940155b41612 | -2.65262 | -60.94898 | 2026-09-02 05:59:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d5d3ef2-4a51-3255-9232-e101a0df2582 | 0.97409 | -59.38213 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b1e3bf1-d10d-334a-abd8-8260c6aa886c | 0.65369 | -59.57329 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc12544-47c9-3242-9aa5-4182d0f10ea5 | -3.62005 | -60.55227 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21f9a8ce-b8bb-3544-ba4f-dca88c4249f2 | -3.6191 | -60.55884 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc5223e1-fb63-3174-a4e5-bc7942ce9dcd | -3.65897 | -58.91562 | 2026-09-02 05:59:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 885e84c0-c8b2-3b52-9cd0-f392c642eb28 | 0.97461 | -59.38549 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f003858-e2d5-3502-8aae-e03665a1f537 | -3.19687 | -61.14165 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8259d6f8-4a63-3bfc-9cda-ceb2228e757f | -3.80064 | -59.29294 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d68df88-f77c-3c3c-90ec-da7e8b4305a4 | -3.12195 | -61.23456 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1a9a319-1271-36c2-a521-79f932f1e2e8 | -3.12741 | -61.23236 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b7efbd2-3945-3624-a417-b70f81e24fb4 | -3.80007 | -59.29695 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4d1d0ec-42f5-3644-9af8-e6b983772567 | -3.62053 | -60.54897 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 939daec2-fab6-3513-b579-3e8aabb3a9b6 | -3.12325 | -61.22584 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3247761d-0184-3286-a728-06d915147884 | 0.97616 | -59.39557 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 399ac951-3989-36fe-96a9-d4fe9426aa0d | -3.0978 | -61.18928 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2a0214-7daf-3556-bb5f-48830521cfba | -3.09439 | -61.21257 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 854bb65b-7c54-386d-b6ba-2bcf0afe19ba | -3.74886 | -59.32055 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 931313fe-b503-3670-ac52-200d29ec3fdd | -2.65308 | -60.946 | 2026-09-02 05:59:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09bfe677-ed8f-3441-8b53-a3aa10e73b3c | -3.11149 | -61.2359 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1890b80b-a891-3fa6-97a6-b00d33cb6e58 | -3.65307 | -58.91472 | 2026-09-02 05:59:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 029c5806-966b-3e5f-8947-04be7080bfcd | -3.29016 | -60.64463 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f20fc6a9-1dcb-3933-8048-51d40125ccc9 | -3.61311 | -59.06818 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00ae3918-27da-3140-ab2a-766cbbd69358 | 0.97438 | -59.39675 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 735aef70-a2b0-3f4a-a745-ecf542dc9923 | -3.09276 | -61.18853 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 009f7b86-f382-32b4-9b34-fea36cb91953 | -3.6225 | -60.57277 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc5f3353-82e4-394a-9516-e1555854a373 | -3.62345 | -60.5662 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dfc00a4-5101-3727-b8da-ecba3a300807 | 0.97668 | -59.39892 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e858bb2-9219-3773-a700-9b55577a1d52 | -3.12238 | -61.23165 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7808e079-c352-30ae-a737-3fc704739286 | 0.97275 | -59.38669 | 2026-09-02 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7481cd59-4437-37cf-a7b7-c5a10addb265 | 1.67062 | -60.14059 | 2026-09-02 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e063d939-2d79-378c-a041-b255b596ca81 | -3.61863 | -60.56212 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4199c44-8748-3156-bc42-40a427576913 | -3.75462 | -59.32142 | 2026-09-02 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f393223-5a53-324f-a752-6a0ecdd6026f | -2.32912 | -60.06621 | 2026-09-02 05:59:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 797627cc-a21f-3245-afcc-d96c2c3638d2 | -3.61958 | -60.55556 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75d4435b-738f-3a12-99d9-b2bdaa554737 | -3.62297 | -60.5695 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edfe4934-b9ea-35bb-af7d-a289bdd85c00 | -3.65836 | -58.9199 | 2026-09-02 05:59:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1314570c-cad6-3f6f-b1b0-90ebc151b8a6 | -3.63691 | -60.54806 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e720f5e-abd3-324f-9e24-34ad507511fa | -3.6316 | -60.54731 | 2026-09-02 05:59:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README61.md)
