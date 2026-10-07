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

## Dados Diários - Página 240

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54477fd8-2919-393c-80a1-76fbd2c340ef | -2.94422 | -54.11559 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f90c3847-8c31-3349-bca3-8ec14eaadee8 | -2.49362 | -56.15044 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| af9ca4a3-4a51-321f-b3c7-48173e87458b | -1.96241 | -56.47887 | 2026-10-07 16:39:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc3e9ee8-a7eb-379b-b30c-0ac8453174c2 | -1.88645 | -54.38293 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c0615fd4-dfba-30c5-b3d6-4f0dadb5280b | -2.99024 | -54.05315 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9f3a29b3-9153-3848-aad7-325fc65faa59 | 3.21086 | -51.30594 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4edb63aa-0e6c-33f6-a514-3beb7b3b1665 | -1.4252 | -55.42747 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| db47bc56-c3fa-3b56-b40d-b28cfe218f58 | -3.84078 | -55.97527 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b643ece7-3016-3e41-b5d9-0078bb6b27c7 | -2.27082 | -53.85427 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7b9bd499-e1ab-31e3-82b1-5a3ddecc2eea | -2.49975 | -56.1495 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d34aa92c-646e-34cf-9cc4-ce956274783c | -3.99888 | -56.26035 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0efaab66-7b47-3b06-aae5-6d534d93980c | 1.87344 | -55.7278 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5195eb2c-8359-3e5b-ab4f-f9660dcc4dc8 | 1.6385 | -55.8047 | 2026-10-07 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f97636c9-8344-3e42-8c81-61b2417222b6 | -9.4317 | -45.8519 | 2026-10-07 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| c8de781e-0daf-311f-860b-e452069aaa7e | -9.6572 | -65.022 | 2026-10-07 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6234578d-13c0-3da2-bfce-e43240301148 | -9.432 | -45.8293 | 2026-10-07 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| ef10a305-f23a-3ef1-bd63-18a61a16aa28 | -12.2136 | -44.6758 | 2026-10-07 16:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 417fadab-db00-3b83-b9df-e57e2f473a97 | 1.8221 | -55.5456 | 2026-10-07 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b42da6c3-b497-3cf8-a143-06492ef50c91 | -12.2132 | -44.6991 | 2026-10-07 16:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 6cc5cf28-8a28-37ae-891e-fc3024c55d47 | -9.806 | -65.0167 | 2026-10-07 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| c725845d-1bf1-3c93-bc32-b8c6be4afd1c | -11.0863 | -45.6688 | 2026-10-07 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 63edb913-2183-375e-8757-16e46ef03fd0 | -8.3391 | -72.6012 | 2026-10-07 16:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1491a8e1-5242-3d78-86ce-59d2a4c95dc6 | 1.8038 | -55.5458 | 2026-10-07 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fe129ead-f656-3b8d-abbc-be605096f1f8 | -11.1556 | -46.0916 | 2026-10-07 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 474622b3-e4b7-36ca-8ba1-65bc73d80a1f | -9.6757 | -65.0401 | 2026-10-07 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.1 |
| ad8536c4-afc5-346a-ba2b-0193f2251583 | -1.3927 | -49.2727 | 2026-10-07 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 20c0361c-3665-3fdc-a15d-e04479271f88 | -11.2295 | -46.2403 | 2026-10-07 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 68ed5100-eef5-3223-af55-01388fb9b150 | -0.3952 | -52.0152 | 2026-10-07 16:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a6bc1425-ff8f-36ca-9700-e2e7069efb11 | 3.5287 | -51.27068 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa22812b-cca3-3b8a-9a44-4df02d554210 | 3.74676 | -51.61929 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 01da62d8-06ac-3ca3-928b-207416b6bc43 | 3.52469 | -51.27006 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8fbc4498-289b-30bd-a1d4-4e91c6ffea6c | 3.57578 | -60.21716 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6a8c564d-5a14-3335-b96f-39138caafe42 | 3.51666 | -51.26096 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4bafebb0-9398-3fcc-b24d-9ed56b5dd95d | 3.66545 | -60.21021 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 747a1190-b2d2-363d-97e1-a6eb93616c75 | 3.99478 | -51.72335 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29a9c68e-62f7-38a5-be37-8f34b52642eb | 3.54909 | -60.27051 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 58ca07cf-ac2d-346d-b45d-fbfd21dcf790 | 3.52124 | -51.26595 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 01a47f95-c52d-34c8-84cf-3edb7b812a12 | 4.29366 | -60.16187 | 2026-10-07 16:41:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f0042a52-0374-37cc-b96c-bae80cf1fda9 | 4.46332 | -59.94962 | 2026-10-07 16:41:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a3763d4f-5ff4-3548-a0e2-f8554790f2f5 | 3.74618 | -51.62292 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a6bf1ca3-edcd-38f9-a747-196ba188e5ce | 3.51264 | -51.26032 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7699e07-137c-3f14-9f06-ba5a0cdb48e4 | 3.47876 | -51.47636 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c8b18f5-c592-309c-9ec5-f84f3da4c44b | 3.5121 | -51.26381 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 115878af-97ed-342f-9e8a-e8ba58f06279 | 4.02203 | -51.60845 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c177cd67-e484-36e0-9e56-92a1a29e8d5a | 3.52013 | -51.26508 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f83a602e-e370-3913-8f93-432c0716a911 | 3.86518 | -51.80456 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 913ab322-0204-38c0-93b4-1e4149fca4c8 | 3.53561 | -51.27891 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 36afa382-716f-33b9-8a88-67bdac43483d | 3.57702 | -60.21008 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 54734fc0-b45b-398d-82c5-75c36e98dd7f | 3.70208 | -51.71361 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d0ac5d96-68ba-3211-b984-dcbc035ef9b6 | 4.29801 | -60.15669 | 2026-10-07 16:41:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a656ad45-0f6b-3161-a900-3cb2a0dbeb2f | 3.53504 | -51.28239 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d00adb8e-4942-323f-8803-089608f13822 | 3.5236 | -51.26921 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8031bec4-83f9-3035-963f-2d34661dc8e9 | 3.53215 | -51.27479 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 166bebbc-4b4e-3aed-b348-06a597351093 | 3.55391 | -60.2575 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 44e307b1-6227-3d2d-b0b9-a5a8ec9ae583 | 3.55985 | -60.2658 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 337b8841-62e2-34b0-b08f-61564a858684 | 3.53617 | -51.27542 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a149f5da-73a4-310a-869a-989e8013395a | 3.522 | -51.46525 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b507a9e7-b654-3bf5-abc4-f1b5d3e6a5b7 | 3.30308 | -60.04273 | 2026-10-07 16:41:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| aa89658f-8aec-3986-884a-811690aefa4b | 3.47468 | -51.47571 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 59de9c62-ae05-3413-b2a7-d65dfcd22780 | 3.2959 | -60.04186 | 2026-10-07 16:41:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 25abd348-fcf2-3246-9a15-c20dfee77fdc | 4.01616 | -51.61876 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 16390514-1f81-319d-bb8b-6ef65d86dedf | 3.55859 | -60.27296 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f676f058-ede8-36e9-8c85-361e20b0a0bb | 4.47455 | -59.92691 | 2026-10-07 16:41:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b8585dc1-9d78-3d36-928e-daa458b87d8c | 3.73685 | -51.7342 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 8acb9736-8fb8-3e99-ba6d-d7a99e50edde | 3.47932 | -51.47274 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3fec200e-f2b2-3ca7-9e5d-1099218b09d8 | 3.55607 | -60.28728 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bcf41e77-6970-3282-adbb-66fd1d200f8b | 4.01675 | -51.61514 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 34ba00f6-6c68-31dd-8bff-8c5af436e9ad | 3.55139 | -60.27178 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8bde60d0-4392-3f8e-acab-aa8d28b3a76f | 3.48283 | -51.47701 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e25b58d-5131-35dc-963f-bc65e695e000 | 4.29495 | -60.15443 | 2026-10-07 16:41:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5bcb1c67-5596-3d05-9ace-d24e17d75846 | 3.47061 | -51.47506 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab2dd3dd-a59c-3353-befa-f5afb38a4101 | 3.51155 | -51.2673 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d86bf13-4363-3bc8-9ce2-843465065e20 | 3.53272 | -51.27131 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 33acddc5-5218-384d-95db-52b25513d037 | 3.30187 | -60.04975 | 2026-10-07 16:41:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 696e68ec-3cb6-3a2c-b20d-749d2e22d131 | 3.49348 | -51.48652 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0732f6f2-2753-3cc8-b2ac-7ca0de1ccc50 | 3.52814 | -51.27417 | 2026-10-07 16:41:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 410a5707-7fbd-3c17-bfdf-b0e411f8887e | 3.56453 | -60.2813 | 2026-10-07 16:41:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6590b93f-01a6-3f90-8746-40265cf93f87 | -1.1898 | -49.2542 | 2026-10-07 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 85eb210a-c738-30a9-a7d6-2e8991a274eb | -12.1746 | -44.7051 | 2026-10-07 16:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 285.2 |
| cf3c1add-b555-3134-956d-4b69338a7c61 | -9.4131 | -45.8314 | 2026-10-07 16:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 5206e15d-1032-34a7-bf12-fc6d3c8bd1d6 | -1.4662 | -49.4625 | 2026-10-07 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b38cb0d6-9e15-3161-9bf1-f9aad4cb5e4b | 1.8038 | -55.5458 | 2026-10-07 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 62474dc2-3aee-32b2-a86c-c7f2522a45e5 | -9.7499 | -65.075 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 52f52456-90c6-3a9a-8bd3-6ada2e684d36 | -9.75 | -65.0562 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| da5a245a-4876-3bdd-90b8-b2ea24cb9641 | 1.8038 | -55.5261 | 2026-10-07 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| dd3036cd-0b11-3bb5-86c4-3bd3201891cb | -12.2132 | -44.6991 | 2026-10-07 16:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 8729369c-de0b-3858-b8e2-3ef46e1a2984 | -9.806 | -65.0167 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 90dc5c5e-982f-36f3-8642-f010dcd96794 | -9.8246 | -65.016 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f9c58d34-fdc4-3ed2-9cda-d3bc99d443f8 | 2.1878 | -55.935 | 2026-10-07 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 76fb72d6-e06a-3d30-b5dc-25f18791593b | -11.0863 | -45.6688 | 2026-10-07 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| fdd48e78-99a8-3bd2-960f-e158f60a4d1c | -8.3391 | -72.6012 | 2026-10-07 16:50:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 684495e2-302b-3140-81eb-44da69c446af | -9.7126 | -65.0951 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a5c17db9-f1e6-3351-a8e7-2225386a5653 | -9.432 | -45.8293 | 2026-10-07 16:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 272.3 |
| d1fc7eaf-39c2-3576-a793-bbad32ec4b08 | -9.6757 | -65.0401 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| df09b51d-5886-3a10-ab25-426887d1f01c | -9.8061 | -64.9979 | 2026-10-07 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 1f29ea8f-620a-34bf-9e63-135c77153d29 | 1.8038 | -55.5458 | 2026-10-07 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5a11555d-5156-384b-a0e3-f12ebcb01c1c | -9.6572 | -65.022 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1b710397-45d8-3f31-97d2-119920123883 | 1.8038 | -55.5261 | 2026-10-07 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8610dc7a-4cae-3a79-ac55-1730b865a4c9 | -9.8246 | -65.016 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0f730793-409f-317b-88bc-af0ea4c364ab | -11.0859 | -45.6916 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |


[Clique aqui para ver as próximas entradas](README241.md)
