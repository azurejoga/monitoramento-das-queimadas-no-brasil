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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea1ca27-1d8e-3816-a09c-b00c833fea8c | -14.9438 | -54.7166 | 2025-08-16 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 334a57d3-43a1-3f54-b031-b68e63779786 | -7.4258 | -60.0292 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9978af7b-5267-3d20-9164-e22878cb4f3d | -7.0981 | -59.2343 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7ebdcdd8-ed15-3071-8282-50b28c4636e1 | -9.1708 | -59.6568 | 2025-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| d8b03614-b103-3160-87ba-80d6282929c5 | -14.6018 | -47.9243 | 2025-08-16 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 1b70ebb7-dd20-3cbd-b980-949e66bc453a | -9.1711 | -59.618 | 2025-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 50052bb8-9f2f-359f-89ab-12a8b6e410ce | -14.9441 | -54.6959 | 2025-08-16 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 23a710a7-81d5-3da0-b805-55c0dce82630 | -3.821 | -47.7227 | 2025-08-16 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c9ea0bf4-19fa-3407-b797-72f474b09dfa | -11.2593 | -50.4981 | 2025-08-16 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9be00b45-3515-3ef1-8b64-7b2620a317f8 | -14.9435 | -54.7374 | 2025-08-16 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 673122a8-519a-3205-b92e-4c2363017b00 | -7.0612 | -59.2358 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 49442d44-9b90-3674-8625-b109f020740d | -4.9305 | -43.2558 | 2025-08-16 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f71ae761-083d-3b52-a213-a9aac1508c1e | -12.9966 | -56.8798 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 2073a1ec-125c-3561-a839-58358fec060c | -11.3655 | -55.431 | 2025-08-16 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8e43f5c3-8028-3679-9fa6-3fbf33e1d00a | -7.9333 | -61.7471 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5965b507-0ad7-31c8-961f-560563f8074b | -14.9628 | -54.7351 | 2025-08-16 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 13f63212-8d3a-386d-9f5c-e90da3509a47 | -3.8394 | -47.7436 | 2025-08-16 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0b7047b3-5ddb-3052-8c01-8a1fc30364b2 | -11.3466 | -55.4326 | 2025-08-16 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 6822e371-a19b-3964-9483-b0b0e2add249 | -13.1074 | -57.1511 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 89b67254-be17-34e8-9c7c-0f553c4cf775 | -13.4294 | -43.6733 | 2025-08-16 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cc53f037-aeab-3e05-9752-2ff7a502c5d9 | -4.9118 | -43.257 | 2025-08-16 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| e151b799-9357-3ba3-a84b-78ba42011800 | -6.9303 | -59.5305 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d5f89fda-2afd-3807-9000-c189907badcc | -6.6327 | -60.0033 | 2025-08-16 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 109600e8-f0f5-3ac4-b94a-b2b988d97632 | -9.4992 | -60.547 | 2025-08-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4e87e812-ed8d-3391-982f-faa0d7f45689 | -13.1262 | -57.1695 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 7774b9b5-3d5a-329d-b917-452bec3893a2 | -9.0346 | -67.427 | 2025-08-16 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5611bbe9-f0bf-30bc-9d14-7b1efb2e7ce8 | -13.4099 | -43.6768 | 2025-08-16 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 667a82f7-ed91-323c-b79c-86b50c4e8e62 | -2.3763 | -47.6636 | 2025-08-16 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7c6955c1-df78-3016-b5ec-39fa32797503 | -9.5179 | -60.5461 | 2025-08-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 6549fb39-627c-378f-9b71-9fb19ed5bb98 | -6.9486 | -59.549 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 3e694b01-c771-30ed-b8a6-6cf72a39173e | -17.615 | -46.684 | 2025-08-16 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 00b3c0d5-eb95-334d-9aa0-f70e14d18913 | -13.1077 | -57.131 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 195.1 |
| c58a1c89-892e-3a37-8079-9264108e2560 | -6.9488 | -59.5105 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 74af85c1-8949-3e60-b08a-c322d737b242 | -3.8209 | -47.7444 | 2025-08-16 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 892b6b6f-6571-3979-bc91-ed74254c4488 | -7.9148 | -61.7478 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 98333062-f9c7-3914-8ec6-d02f0f22cd11 | -7.5292 | -61.3254 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4df65cf2-6176-3733-95d0-d4aa7aed8830 | -6.6326 | -60.0224 | 2025-08-16 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b7987b0e-a604-3b12-86f9-3a298a60b19a | -14.9635 | -54.6936 | 2025-08-16 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 563ba76d-a7a7-3c45-b01a-7c3575e46e80 | -7.0589 | -59.6215 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 64914bbd-c88d-39dd-8945-1a04409c7ac6 | -7.1325 | -59.6569 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0f2eb3ae-e9f7-3359-a326-c7d258ab8ab5 | -7.8963 | -61.7485 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 04d327ff-e4a2-3106-b56b-89ee068e9787 | -4.9116 | -43.2803 | 2025-08-16 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 21d5b2a5-1ad3-3e85-9407-633614116e01 | -9.518 | -60.5268 | 2025-08-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 3f4643cf-cd41-3851-a860-76cc105720e9 | -7.9334 | -61.7281 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 170f0103-3c5b-3673-96cb-1fd3f1fb4426 | -6.9302 | -59.5497 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| cd28b406-6ea9-3c9c-8c32-b79a2314caa3 | -6.5638 | -43.0357 | 2025-08-16 00:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 280aeef7-dc2a-336d-b94b-e877f24016cd | -6.9296 | -59.646 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 98f6a6a7-5ee0-330c-bb39-c0bfd0ea30cb | -7.8247 | -61.3327 | 2025-08-16 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c11df978-ad3c-361b-a74f-81c52da9c29d | -14.9632 | -54.7143 | 2025-08-16 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| f09722f5-996a-3291-a892-62aa107e87cf | -6.9485 | -59.5682 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ea4db247-e7c6-3eb7-93b8-9d027c9ab28a | -9.0531 | -67.4265 | 2025-08-16 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 045e759b-1a77-3ea0-a564-d2a26de2b11d | -13.1265 | -57.1494 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 70d0ba7c-681e-3268-b50d-31ab43c07b42 | -9.1523 | -59.6384 | 2025-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ee79a376-3ee7-3592-82a7-3f053872f6c5 | -6.7811 | -59.8249 | 2025-08-16 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 58098b2f-4020-33bf-b266-9431dedf10bb | -7.9439 | -63.2225 | 2025-08-16 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2ca98b3e-4c06-3710-ae17-3650fdb84480 | -11.2596 | -50.4767 | 2025-08-16 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5555e7a5-5343-30c1-972e-436277204e89 | -7.0796 | -59.2351 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| e110545e-d852-321b-bf4b-fca1ea57b4c1 | -9.2082 | -59.6354 | 2025-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e6992350-525a-378a-a0a4-f94c60d63136 | -9.1709 | -59.6374 | 2025-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 0bcad217-3b79-308d-a426-f22b501857f6 | -6.7995 | -59.8242 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3336e233-decf-3e4a-a8c4-27ff00557a21 | -7.9149 | -61.7288 | 2025-08-16 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 141.6 |
| b6749566-abe6-3e12-9ff1-318454a5a66d | -7.8248 | -61.3137 | 2025-08-16 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 712f2c2f-70ad-3aae-9d6d-1f3c66115466 | -11.3468 | -55.4124 | 2025-08-16 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e23cfaa5-b26f-30cf-8bc2-dcf2830643bb | -13.1267 | -57.1293 | 2025-08-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 87b0c1a7-eb0e-388c-b52a-66f4313dc3a2 | -7.944 | -63.2037 | 2025-08-16 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 82161893-1a88-3aa9-991b-0710424d58da | -7.0797 | -59.2157 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8d2a6de0-6e6b-3757-beb9-6b8c61b1473b | -7.0404 | -59.6222 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c987654a-7ab3-3d8f-88d2-4a12412e1806 | -6.9487 | -59.5297 | 2025-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 8d8f1103-2b8c-3612-91d0-7b227ce1221b | -22.53185 | -46.89442 | 2025-08-16 00:24:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 8b3b67d4-4f61-3e3d-b7c0-2726878078ce | -21.52412 | -49.14316 | 2025-08-16 00:24:00 | TERRA_M-M | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 31e34dd6-b2e3-3f32-851f-001c482a40e7 | -14.52314 | -48.58229 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61968de8-d104-37b9-b439-d3cb2dee3a0f | -13.58138 | -46.96685 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1fc2590-d88f-3f26-acc6-40105c787d5c | -19.19408 | -46.25101 | 2025-08-16 00:26:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71527f07-dd41-30dd-b56f-23331b36dc3f | -13.4226 | -43.68189 | 2025-08-16 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 256a26a2-9484-3abb-a3de-09dc060485c9 | -19.86649 | -44.94109 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1bf02a0a-60e2-3df9-8ccb-75287e9247d5 | -12.81527 | -46.0014 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11283b60-6963-3f4a-a845-198d2ce0dd7b | -14.94162 | -54.69643 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1764bd4a-3a03-33cb-ab94-d48373079162 | -20.01607 | -41.88519 | 2025-08-16 00:26:00 | TERRA_M-M | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 658a012b-f4d0-39ec-9b33-05e6fefe3982 | -13.61115 | -46.91504 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e00abe61-bbc2-3008-99e4-ef68cf8a4f82 | -20.41387 | -46.54106 | 2025-08-16 00:26:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b2e47e22-d190-317a-91d2-fe341e2f97e1 | -14.53296 | -48.58089 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 46d27269-8130-3e9a-87e7-6b9967f2690c | -15.9039 | -41.60423 | 2025-08-16 00:26:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 9dce3736-b894-34a7-bd50-83f7387ed77e | -12.8266 | -46.01812 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7f6e5a60-a6fd-31a8-9c8c-e7382fa765cf | -14.58747 | -47.90287 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a46b797e-e7c0-3e71-b78e-8b7c82b05304 | -13.58262 | -46.97612 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e15b115b-3f12-341c-92a6-c9faa433ba10 | -14.95817 | -54.75851 | 2025-08-16 00:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5ef5c345-5a4e-388b-9983-1e2882ecccd0 | -12.82411 | -46.0001 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 33f8aa18-8051-33b1-ad00-093e0f6bb715 | -14.58885 | -47.91348 | 2025-08-16 00:26:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c0e37a12-ded8-35b5-9a27-8f6db8b0f28f | -18.36204 | -41.79555 | 2025-08-16 00:26:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| b3c7b242-f269-3900-9166-743695c0d156 | -20.30469 | -42.64338 | 2025-08-16 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DO GRAMA | MINAS GERAIS | Brasil | 3160108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 05894c6f-6579-3d38-a12c-a453f9c693f0 | -19.93737 | -41.24212 | 2025-08-16 00:26:00 | TERRA_M-M | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| fd2a3dc7-cad6-3b84-88b8-c3dc85649143 | -18.04249 | -47.72703 | 2025-08-16 00:26:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3b9bd594-c9be-3f17-aab1-a56a23920bf5 | -12.68716 | -44.96257 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a4d9e5be-c242-3f00-a080-77f9df90a51a | -13.33141 | -45.22255 | 2025-08-16 00:26:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7e1957f0-9a89-3470-ba5c-8a7bdd4c3874 | -18.36534 | -41.80028 | 2025-08-16 00:26:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| a3286018-58e5-3f78-980f-e611e3f0553a | -18.51513 | -50.7386 | 2025-08-16 00:26:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8880d423-3d96-3f1a-877e-ec2ddc099db1 | -12.82535 | -46.00911 | 2025-08-16 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 92053f3b-af46-3f49-88dd-4d23cda0155e | -18.5238 | -50.74321 | 2025-08-16 00:26:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 91f90b48-84ce-3766-a66c-c6fee793d441 | -17.33322 | -46.55987 | 2025-08-16 00:26:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1501b95b-9786-3037-ace9-987d7857ad80 | -14.97038 | -54.71995 | 2025-08-16 00:26:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |


[Clique aqui para ver as próximas entradas](README4.md)
