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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67a9b772-048d-3c97-b21b-77bb232d756c | -2.94532 | -54.1446 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 988befe2-3d80-315e-bb8b-dbd17ff86e0a | -3.18529 | -58.98262 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e468a348-662f-31ee-9bce-f96212b5342a | -2.86673 | -54.13417 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5de8a139-1ccf-39a7-955e-b4efd2ef16f5 | -3.27782 | -53.99765 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 06b677c9-2977-34aa-92cc-cda6f0aec347 | 0.44385 | -60.5466 | 2026-10-06 12:38:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| c5660310-1ea8-3024-8a33-d2c25603679d | -3.06086 | -54.1511 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3042f84e-f4f7-386b-b828-9774ece4397e | -3.47412 | -60.32183 | 2026-10-06 12:38:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e2076687-c3b2-3051-91a8-df9ec6789e4f | -3.47286 | -60.33066 | 2026-10-06 12:38:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dc2b724e-cefb-337c-8ae5-41696ca164fa | -2.87982 | -54.13597 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| a4b21a94-6ac6-3147-b916-aece3691eff2 | -4.32644 | -55.66143 | 2026-10-06 12:38:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 922e7ea1-4514-37d3-9762-a6e9a13d2996 | -3.44429 | -59.82062 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3cff9aa5-f7df-38b7-9d3e-eb3ff1e9d449 | -3.33454 | -59.49203 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1f8629a8-2cc1-34d8-b87b-bfaa459d5076 | -2.94561 | -54.12891 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 0f269e96-d064-3cd7-bf45-a71350c886df | -3.22469 | -54.30357 | 2026-10-06 12:38:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d514c018-5718-36cb-b03f-aa27c7507552 | -3.8587 | -55.99104 | 2026-10-06 12:38:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d5de3c3e-2f8f-374e-b14b-d8805b9818f8 | -3.69177 | -59.64076 | 2026-10-06 12:38:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| de78e73c-05d5-3e91-ae85-70117cdbb6a3 | -3.7093 | -58.92292 | 2026-10-06 12:38:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4873f448-9e15-3c02-84dc-2bce03fde77a | -2.57736 | -57.78735 | 2026-10-06 12:38:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b6f04acc-c044-3fdc-9386-7886c68e1bb7 | -3.11262 | -53.76132 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 6547f40e-08fe-3cc7-8b03-d3381a8c4492 | -3.18392 | -58.99225 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b3a1c0c0-0f02-32d0-9629-6d758bf3f169 | -3.86079 | -55.97578 | 2026-10-06 12:38:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| a794dae4-a822-34c1-bf22-f33cba0b0810 | -3.69145 | -55.95597 | 2026-10-06 12:38:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d65f958e-bf68-39c2-afcb-cbd9b765d3fc | -3.03282 | -53.8794 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 322.2 |
| 70163e80-7e4b-384a-9e68-c813a90a4e1b | -2.13733 | -56.69962 | 2026-10-06 12:38:00 | TERRA_M-T | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| cfc2ff2a-19e4-32d4-ac50-a4c4fd269357 | -2.33717 | -55.69791 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a19a716e-473d-32ab-9ad5-0cd6be3acab9 | -3.35387 | -59.48528 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0bf1f763-9459-36bc-a241-f37002968328 | -2.78794 | -57.67011 | 2026-10-06 12:38:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 243fccbe-4e9e-330e-a3d7-edd0fced8690 | -3.35257 | -59.49452 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| d02f0c29-235e-3762-bbe7-6d3703cde1fc | -3.38771 | -58.20502 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e4448f72-a3a4-35b9-8d8a-1e8c6dfe120d | -3.1339 | -59.01485 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 97b98f76-7717-3a15-8470-461b40fc5ac2 | -3.71858 | -58.92417 | 2026-10-06 12:38:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4cdd30e9-03bd-3de4-8bd3-585c90c07aac | -3.01121 | -54.13772 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 332.3 |
| 2b7c42b8-aecb-34a2-867c-59ce8192b0ab | -3.01406 | -54.11686 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 8cc0458a-3445-31bb-9ee9-ea5bb3ed60b7 | -3.79316 | -59.38016 | 2026-10-06 12:38:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 924b8d09-bf93-3553-8381-2c981e27cc66 | -3.87014 | -55.99248 | 2026-10-06 12:38:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 6ce21f39-16e7-378e-8a95-9f1c46728d49 | -3.34355 | -59.49327 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8e02e069-03c5-3845-9fb5-e68f39a88bbb | -3.27491 | -54.01939 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 920d1353-1920-3e52-a141-ae09047fce0a | -3.6342 | -58.93613 | 2026-10-06 12:38:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 55493377-965b-378a-877c-058d3198c98c | -3.06371 | -54.14465 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f1577620-a6d8-36a5-b39b-e10a6875845d | -3.54871 | -59.47709 | 2026-10-06 12:38:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d5756303-bbcb-331a-b301-abce87a9ed77 | -3.33713 | -59.47354 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 1c5f57e5-8685-319e-ad9b-ef639c24d923 | -3.38921 | -58.1944 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 00316b68-2f58-3e8e-92f5-eb7dfe8eb9ce | -3.01941 | -53.87762 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| b8fb16d7-1ad1-301c-8983-35470eab6062 | -3.10029 | -54.15586 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 34a498a3-c3b3-31b6-ad55-055c5b68abf2 | 2.4585 | -50.8299 | 2026-10-06 12:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d03c50c0-783f-3074-b98f-cd6ca72f011a | -10.9758 | -45.4324 | 2026-10-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 98706b73-4f05-3d5e-8a8a-8b52cf01975c | -11.2798 | -45.5052 | 2026-10-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0f3bed93-da98-3923-835c-8a7e1f83ddc7 | -11.2607 | -45.5078 | 2026-10-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9f66a6e1-0708-33a5-b122-cde1ac36481e | -10.9762 | -45.4094 | 2026-10-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9d74c1fb-774c-3bf8-9152-6795451f37a5 | 2.4584 | -50.8507 | 2026-10-06 12:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 93604093-5d99-3233-b80e-5b0602786d11 | -9.17091 | -61.40764 | 2026-10-06 12:40:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4bdd8498-e7da-3c5a-a1ba-58bb49f7be3d | -9.52619 | -62.98433 | 2026-10-06 12:40:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63f5d21f-d24e-3467-b8bb-2d8a94307a54 | -9.14728 | -65.40887 | 2026-10-06 12:40:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 29765cac-fda0-3aa7-9b48-a89cd707bf06 | -6.4883 | -62.86396 | 2026-10-06 12:40:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 947b124a-d9da-3a1d-ab35-bbbed542ebf8 | -7.22638 | -55.18504 | 2026-10-06 12:40:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a3956b81-c610-3e8c-855f-8d83408d7676 | -6.48964 | -62.85474 | 2026-10-06 12:40:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63bc7c35-e7e6-3112-92ae-1af73e9310b6 | -9.4664 | -64.32722 | 2026-10-06 12:40:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3b88d7c-bd5f-34fc-82b3-96104171080b | -9.1645 | -68.25067 | 2026-10-06 12:42:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8b261641-ff24-3161-a142-2fc5f91aaf03 | -9.82799 | -65.0514 | 2026-10-06 12:42:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b4c8eb0-bbc5-338b-8b1f-c6de252a38cb | -9.73047 | -65.08582 | 2026-10-06 12:42:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1c4980df-026c-334e-a80f-47e547b4de67 | -9.40229 | -65.89644 | 2026-10-06 12:42:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b3bc3d49-6773-34cf-8882-78ac254ac18e | -11.2798 | -45.5052 | 2026-10-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 6edcc23a-7445-3a98-8408-ee3b5b8e8c0f | 2.4584 | -50.8507 | 2026-10-06 12:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 159.9 |
| f20c2e8d-0bdd-3f03-b82b-854f0cda1c17 | 2.4585 | -50.8299 | 2026-10-06 12:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 63cb45d6-2b8a-38fa-98e2-f5d187fd7d80 | -10.9758 | -45.4324 | 2026-10-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 507cc778-617e-3642-8b05-ea3cd437bd3c | -10.9762 | -45.4094 | 2026-10-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 414c3adf-fede-3c57-a291-63c61ba6c5a8 | -10.7493 | -45.3024 | 2026-10-06 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 9920a279-c114-3a47-bddd-2fa123ec8b56 | -10.491 | -47.2533 | 2026-10-06 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f4467829-089e-3d95-8711-9a5133d81f23 | 1.4922 | -55.6682 | 2026-10-06 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 28f0dd51-9bb6-36c1-ade6-03544724fa2f | -11.2798 | -45.5052 | 2026-10-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| a9cb0eb8-7e8c-34df-a333-137547357158 | -10.9758 | -45.4324 | 2026-10-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 4dabc67b-2c26-352a-8314-661b898313f6 | -11.0485 | -45.6511 | 2026-10-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 19feaf0e-1c10-3c13-8ce7-d5854259739c | -10.9762 | -45.4094 | 2026-10-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 18faa166-a220-395f-8c52-3d6b50e6b357 | -10.9567 | -45.4349 | 2026-10-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 003d64e6-acb9-3206-8ddc-ad322884204a | -11.6754 | -43.6817 | 2026-10-06 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1b40a338-68c1-33d5-8805-914cb4032dcd | -11.6946 | -43.6787 | 2026-10-06 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| ef9f2cf5-ab19-3dae-937d-70fbedc92623 | -15.5222 | -42.6342 | 2026-10-06 13:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 193.0 |
| 5e20036c-c580-35e4-8429-f2c429db33f4 | -11.0485 | -45.6511 | 2026-10-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 15475689-7123-3b5b-9314-ebb3d1c6980d | -11.8315 | -43.5391 | 2026-10-06 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| fbf40af7-5b85-3b76-b142-71191a6c8a37 | -10.9762 | -45.4094 | 2026-10-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 352.3 |
| a6c647f1-2168-38ea-ae97-82e6d901f13c | -7.8682 | -44.169 | 2026-10-06 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e47056bf-fe7f-32ee-9ae2-599a7876757e | -10.9571 | -45.412 | 2026-10-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ffb88619-aeca-3cc7-b865-2cf1fdf15eeb | -7.8496 | -44.1478 | 2026-10-06 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3e63cd9a-751f-3e97-a223-8812e715614e | -10.7493 | -45.3024 | 2026-10-06 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 765c396b-a324-3270-94fb-bd550446efa6 | -10.9758 | -45.4324 | 2026-10-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 350.8 |
| ff0be146-bdd6-3129-b7aa-cb2f42e11c44 | -11.3562 | -46.6522 | 2026-10-06 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a702cc96-0df1-31ee-ab3f-58054d560903 | -9.42 | -45.81 | 2026-10-06 13:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49b032c8-b705-3b2e-9b7a-c38eb2245872 | -7.2079 | -44.3024 | 2026-10-06 13:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fd39f06b-cfc4-3485-b28a-d3d629d4f468 | 3.055 | -60.5952 | 2026-10-06 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a0a39b43-f1e5-3c80-b509-39b8cb134e8a | -11.6754 | -43.6817 | 2026-10-06 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 955d98bf-b9fe-3db1-b14f-81f69d26858c | -10.9762 | -45.4094 | 2026-10-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a5d7ca9c-6334-38c2-8673-e3d4eb677be5 | -7.2077 | -44.3255 | 2026-10-06 13:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b595accf-9461-3e31-8f92-3b4844d0f392 | 3.0732 | -60.5949 | 2026-10-06 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 28d53663-20b0-30a8-a08c-44884ed8bf05 | 3.0733 | -60.576 | 2026-10-06 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fd3bdc39-1902-328a-91ed-6c5329683efe | -7.8682 | -44.169 | 2026-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| c67850b6-0e29-307c-8610-16f21a9995c8 | -11.8315 | -43.5391 | 2026-10-06 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| e85e07ce-74b8-3d64-aed3-1585fada5c39 | -10.491 | -47.2533 | 2026-10-06 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| eaa0b74b-489f-3df7-b50c-af0c630ee79d | -7.8496 | -44.1478 | 2026-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 55f17720-ca3c-3311-b8e9-1e07fc7d3f6d | -9.96 | -43.481 | 2026-10-06 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fd6fc89f-f6f5-358f-afe5-6ea490eed0cb | -10.9758 | -45.4324 | 2026-10-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |


[Clique aqui para ver as próximas entradas](README82.md)
