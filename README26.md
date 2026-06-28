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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0b5b6dd-d191-3ae6-a5cf-62aa0df5c508 | -10.3443 | -46.9142 | 2026-06-28 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d0f4d868-fdd0-39d2-bc16-6b44a6fb5e62 | -10.3253 | -46.9165 | 2026-06-28 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| aa3543cf-5e77-32b2-88a2-d206db2b488d | -13.2201 | -54.415 | 2026-06-28 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6d95d02e-7c21-325c-9206-bf746fae3e1a | -10.3253 | -46.9165 | 2026-06-28 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a926a316-339b-317f-bc84-d5dcb53b468f | -12.1937 | -52.8866 | 2026-06-28 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1a043955-e707-333d-a33e-67e9a8c2f02d | -10.3443 | -46.9142 | 2026-06-28 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bae4ce27-eda1-3d1a-bed2-984e6941e169 | -13.2201 | -54.415 | 2026-06-28 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| d52d8b0e-051d-3b12-800c-46d4d171ea31 | -12.1937 | -52.8866 | 2026-06-28 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4deb0cda-cd77-3f7c-b88d-d0b5f6cfec67 | -13.2201 | -54.415 | 2026-06-28 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0d9530cb-10ce-3928-bd30-634305c59492 | -12.1937 | -52.8866 | 2026-06-28 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 616a6104-493d-39df-a587-581f752b4405 | -8.3085 | -48.2731 | 2026-06-28 12:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 190d5256-6fa9-3402-9ff8-45b5e3b2304f | -8.3088 | -48.2514 | 2026-06-28 12:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 6e7549e8-66f2-36d9-af25-83b56ef99f68 | -12.1937 | -52.8866 | 2026-06-28 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| df21b8c9-c9bb-3827-afe9-c1d521c582ee | -8.3088 | -48.2514 | 2026-06-28 13:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| e6a4c8c8-0ff1-3392-8caa-cb9ae1e3aeee | -12.194 | -52.8657 | 2026-06-28 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c3066c55-9d78-3f03-98f0-36bb8c7b095e | -8.3085 | -48.2731 | 2026-06-28 13:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 6099ea09-1331-3bfe-b1ea-4eeb019f01cf | -12.1937 | -52.8866 | 2026-06-28 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 82604485-9225-37a7-92bb-e249f39fe3ef | -12.45395 | -58.48832 | 2026-06-28 13:06:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5a446303-6f5f-3e4b-9edb-8353dbb307ca | -6.95057 | -63.5479 | 2026-06-28 13:06:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b8141ed-322e-3ea5-a339-cb089f9208a9 | -12.17751 | -57.14446 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6ebc6aa5-7f93-379a-a9d1-aa93b190833a | -12.29823 | -57.55555 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 5f0fa596-99bb-3886-b8a2-7c261fb6fa11 | -10.30277 | -57.13489 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4d511d1e-4a4d-370b-9e66-18de50ae9085 | -12.45689 | -58.46483 | 2026-06-28 13:06:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 496d80ac-c5b2-36a3-8b74-c834845575b0 | -12.29469 | -57.58864 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| d8fc20ae-eb2d-36b5-95fa-2a552ae704f2 | -12.54902 | -57.20951 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 1c50aafe-c478-3ba4-b85e-0a39f8507f10 | -12.28918 | -57.54747 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6acbecc4-f3fa-3c0d-b908-3de57cf90adc | -12.45378 | -58.49354 | 2026-06-28 13:06:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| bdae63cd-c692-3674-8787-60d81b84223b | -9.08432 | -59.40928 | 2026-06-28 13:06:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 750389f2-ffcc-3540-9583-214373d3e235 | -12.28543 | -57.58067 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 260.4 |
| d6bcee44-e11c-31a7-bb2f-9a3f7d0da1f0 | -10.29431 | -57.12688 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| f59decc3-173a-3cdf-9404-d44b58ea1eb7 | -12.55291 | -57.17315 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4f5f7fe7-7f2e-3031-926c-7ed20493eafa | -12.17108 | -57.13639 | 2026-06-28 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d9833977-cd21-3001-b44e-caff3a5bd085 | -15.37647 | -60.1712 | 2026-06-28 13:08:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ebf60309-f48c-3b12-948c-93273c34216c | -8.3085 | -48.2731 | 2026-06-28 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4c0fcd69-489e-36a8-acf6-05f8cb3c4fce | -12.1937 | -52.8866 | 2026-06-28 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c5522c0f-8fb0-37c0-9bea-36e12df06310 | -8.3088 | -48.2514 | 2026-06-28 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5240aa3a-35b9-38e3-932e-b1cbc3cdacd6 | -12.2862 | -57.5621 | 2026-06-28 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f78688f4-054c-3271-bec2-81d3fca4714d | -12.194 | -52.8657 | 2026-06-28 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9356ada8-5af7-3fb3-bdb4-bb9b0b0150cb | -8.3088 | -48.2514 | 2026-06-28 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 35f75495-5b3a-3ba6-9fec-744aad2f8424 | -12.1937 | -52.8866 | 2026-06-28 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9c018a69-4e8d-37ed-9c36-5737b5b78e11 | -12.2862 | -57.5621 | 2026-06-28 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 644053f9-d8fb-3ca4-b6bf-c15d9f02fd11 | -8.9619 | -45.6552 | 2026-06-28 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ef984975-84f5-3af1-aa2c-0a4034f524de | -17.712 | -46.7798 | 2026-06-28 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4b958009-4432-3821-aaec-bb9436847418 | -12.194 | -52.8657 | 2026-06-28 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3065ba1e-5054-3ecb-a6be-8996f8bc4a2f | -8.3085 | -48.2731 | 2026-06-28 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d3d1542a-271e-33c7-9ed4-58d20b77f7da | -8.3088 | -48.2514 | 2026-06-28 13:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e2e241f0-2755-36cc-9d1f-5e60dfbc32c9 | -8.9619 | -45.6552 | 2026-06-28 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 81555667-be01-325c-99ec-efd4c4366c6f | -12.194 | -52.8657 | 2026-06-28 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 07a1d41c-6ed5-34fe-9472-2d1f4c3920fb | -17.712 | -46.7798 | 2026-06-28 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1eee4f23-d80b-3ddc-8d27-9b4c8fb0b4ae | -12.2862 | -57.5621 | 2026-06-28 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| d0cadb74-d33c-3b9e-86df-4cf6d362151a | -12.1937 | -52.8866 | 2026-06-28 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| acff74fb-dcef-318d-9209-855b8b1e769b | -8.3085 | -48.2731 | 2026-06-28 13:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6b63bf73-9070-3444-ace2-ad3c1e4999de | -12.1937 | -52.8866 | 2026-06-28 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| fd75067b-88f4-30c6-a788-2a05fff3475e | -8.3088 | -48.2514 | 2026-06-28 13:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 93e58ac8-b1a5-3222-ac71-4df557938fb4 | -9.2131 | -46.6404 | 2026-06-28 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8fd83d4c-be6d-373c-a0df-b8e141cdef92 | -8.9619 | -45.6552 | 2026-06-28 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| aa9d5dc9-86ad-3664-8abc-acaf9a5cecee | -8.3085 | -48.2731 | 2026-06-28 13:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 325e7755-8508-3420-8f19-04a2736e9ed4 | -12.2862 | -57.5621 | 2026-06-28 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| f8031d56-da67-3d20-b7f2-12de60a5de50 | -17.712 | -46.7798 | 2026-06-28 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 40ac827a-c712-361f-8a2c-a5844b79c5e0 | -12.194 | -52.8657 | 2026-06-28 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1b413143-64ae-35ca-8be9-0c45932851d1 | -8.3085 | -48.2731 | 2026-06-28 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1f190ded-6c5c-3ec9-8189-28a4c955b4bc | -12.194 | -52.8657 | 2026-06-28 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 31232039-bda5-37eb-b9c4-99034be93b8b | -8.9619 | -45.6552 | 2026-06-28 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 76054e5c-e0c1-3e18-8c78-13b163ccd86c | -9.2131 | -46.6404 | 2026-06-28 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 2e7930a2-0272-35b3-bee4-8ebbb090f253 | -17.712 | -46.7798 | 2026-06-28 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ce333ad2-f523-37fb-9a20-2c51c21781d2 | -12.2862 | -57.5621 | 2026-06-28 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 828131c7-1e30-3755-952a-ca32d3d572b4 | -17.7126 | -46.7565 | 2026-06-28 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| dd8dc54b-c535-381e-be61-637881974f87 | -8.3088 | -48.2514 | 2026-06-28 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 087847a3-6776-395f-9639-3bd5a3c23b20 | -12.1937 | -52.8866 | 2026-06-28 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d236159d-ca35-3b84-b257-945d42af48f4 | -12.2862 | -57.5621 | 2026-06-28 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 8d62bd9b-a881-3a05-8382-cdecc4cad346 | -8.9619 | -45.6552 | 2026-06-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0be2e5ac-13f1-31d6-ab7c-01f8d54f7062 | -12.194 | -52.8657 | 2026-06-28 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b285b696-f404-3529-8849-efdd08d3927c | -12.1937 | -52.8866 | 2026-06-28 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| f8e46449-e11f-3eff-9edc-2877efe9d556 | -8.3085 | -48.2731 | 2026-06-28 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 617872d8-f51a-3930-affb-6da9a5f8f947 | -9.2131 | -46.6404 | 2026-06-28 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| d29dbe6c-70db-3320-a2fa-3dcdef8a8801 | -8.3088 | -48.2514 | 2026-06-28 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 170a5035-de0b-3635-a388-120bd03a84f5 | -10.3443 | -46.9142 | 2026-06-28 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 04805692-2de8-3721-af7c-b3360c5dcc54 | -8.9619 | -45.6552 | 2026-06-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 6218d719-7135-35f9-9dca-762762b1808d | -12.194 | -52.8657 | 2026-06-28 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3c99e1f5-d076-3e7b-9ae5-091a4254a426 | -12.1937 | -52.8866 | 2026-06-28 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0ba136d8-9de2-399a-a2bc-f6b21f049cad | -12.2862 | -57.5621 | 2026-06-28 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 4c5905c6-00ea-386c-8a26-3eb962840d65 | -8.3088 | -48.2514 | 2026-06-28 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0291ff2b-d645-378c-9632-252bf82d4301 | -8.3085 | -48.2731 | 2026-06-28 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9dc95ca2-02fc-3dcf-9771-bd99514ff251 | -12.1937 | -52.8866 | 2026-06-28 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 2056cc18-3556-31fa-b457-31cf341c9f3c | -9.2131 | -46.6404 | 2026-06-28 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| aba2caa6-181e-38c3-8cb4-75a337ddd4c7 | -8.3088 | -48.2514 | 2026-06-28 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c71eb595-3593-3b9a-9af6-09f3fb340146 | -8.2429 | -47.4471 | 2026-06-28 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f8c2a97e-8084-308e-a70d-ab18b8787467 | -8.3085 | -48.2731 | 2026-06-28 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 69c3faf5-451a-3cd7-85e5-e576739d7036 | -8.9619 | -45.6552 | 2026-06-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 960c5496-4067-3050-91f8-18735a57a45b | -10.3443 | -46.9142 | 2026-06-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7b54f2ff-873a-338a-b943-44a2c659c05c | -10.3936 | -50.1418 | 2026-06-28 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a7e40bca-5d12-324b-ada0-c2adae67fa8d | -12.194 | -52.8657 | 2026-06-28 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2b5ce1c3-dcdf-3656-9cac-4e6d5d49bda0 | -12.2862 | -57.5621 | 2026-06-28 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 18d37841-d682-3ca8-afd7-bae9537b2fdf | -12.1937 | -52.8866 | 2026-06-28 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c59179c8-181d-3abc-ae80-63049cc5dad1 | -12.2862 | -57.5621 | 2026-06-28 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| b3b01dbc-7779-3ec2-ac70-b829c88b7be4 | -8.9619 | -45.6552 | 2026-06-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6927f287-c068-3b41-b338-fadbefe9ab61 | -12.194 | -52.8657 | 2026-06-28 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ef47bc37-4fea-323a-b23a-dfd8504ebfad | -8.3085 | -48.2731 | 2026-06-28 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d122e477-4261-32b0-ae25-4f54a4ceb01c | -17.7126 | -46.7565 | 2026-06-28 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 0d5ec20b-7434-3e8c-be58-547ea2ebd08a | -8.2429 | -47.4471 | 2026-06-28 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |


[Clique aqui para ver as próximas entradas](README27.md)
