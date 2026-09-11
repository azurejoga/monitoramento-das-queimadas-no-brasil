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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bc4ba54-f721-3fcd-9e13-b2e5dccdca13 | -8.99455 | -65.41982 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38045a48-24b5-3e84-954a-d39528254f99 | -8.62514 | -66.51111 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67801f7b-9647-369b-8297-dce06195d1ee | -9.09184 | -65.49299 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36d810f8-ee41-316d-a7ee-90986b28dfc9 | -8.99123 | -65.41929 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f53e7f4-2ca9-31d0-b16e-ed848909990e | -9.14348 | -67.80357 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38df481b-9080-3266-8cbb-b95f70308f99 | -11.80796 | -60.4549 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92e6c1de-b6f1-3613-9695-8d873c8bb9c9 | -9.04275 | -65.41663 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b19ab5f-c6cc-30c0-bf91-b4c7b93aae51 | -9.47975 | -68.83987 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1458cb35-963d-3518-8111-a617adfff724 | -13.2562 | -61.60688 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25c7509d-e723-3a37-b7dd-ad8ff4066dfd | -7.75641 | -66.90558 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 093cc105-31ee-356c-9757-5280899bd465 | -9.71003 | -64.94186 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9335b2e9-4f82-332d-aae4-d8c0b821530e | -9.4146 | -67.41137 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d403ba30-00f2-3c06-ba85-785fe93b3c1a | -9.18576 | -68.208 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bb1aa7cb-6120-320d-abbd-422c1a7da67c | -9.19206 | -65.78431 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| beef0fde-0345-3162-9fbd-d46ff32441fd | -9.28983 | -65.8109 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a4f3d9-8d49-3404-b27d-5b022b1e5823 | -9.17349 | -71.85139 | 2026-09-11 05:50:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70be736a-b00b-36c4-a4c7-d7104dd8d884 | -9.40074 | -65.86081 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b66f3801-7573-342b-adb7-06676dab7bee | -8.65257 | -69.78924 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dedca2c-6c3d-3084-883b-497be5dfd5ab | -8.63785 | -66.51673 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e2d49b3-efa5-306c-8ff9-cc66a181e8e1 | -8.54194 | -66.98809 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d673e50d-6e50-3da0-8695-753c1c03deee | -9.09294 | -65.48598 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 060a12ba-a4f7-30de-a4e1-92020ff57bbf | -9.18858 | -68.21234 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4dc3ee1-65b1-3179-ae01-9a1966d837f1 | -9.34807 | -65.67686 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4518df2d-190d-340a-834c-e33236987218 | -9.18982 | -68.20481 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a74717f-fa3d-3ca3-8cb0-cfe291b978bf | -9.03942 | -65.41611 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e74752cc-e1c4-3023-a243-644a8287c65c | -13.22421 | -61.62548 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc2576d7-1d00-3691-b97a-0a8b16e7c381 | -9.48894 | -68.49975 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88c037ad-9870-313f-a2bd-b604782aac4b | -8.8397 | -62.48289 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1ec95a2-5d69-3db8-8aad-b7433704770d | -11.81173 | -60.45982 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b192ff35-66d0-390f-b8bb-eafcf0810076 | -7.79087 | -72.50061 | 2026-09-11 05:50:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8102c9b8-c308-3f0b-aa49-958421f77a64 | -9.22672 | -65.58557 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdfcc2ff-0cf3-36ed-bbf8-c80c566b66b9 | -9.17764 | -68.21443 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36e7ba09-0032-36e9-aa3b-423118680203 | -9.89476 | -67.60098 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25f4e076-d332-3d70-bab4-779411208d3f | -8.93763 | -66.85344 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b69ef0-4d21-3f09-b77e-9a4b1b78ab51 | -9.75489 | -64.9415 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f1018b8-848e-30ee-b520-639a14c53faf | -8.97845 | -65.39207 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac151ece-4dcc-3a53-b8fa-84b61ce42271 | -7.76024 | -67.15916 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 342b73c1-68cd-3b61-beef-867659185e0d | -7.13974 | -73.11681 | 2026-09-11 05:50:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b33a1d9f-36de-3014-994e-c3d2585f411e | -9.01615 | -65.41244 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7deeb8-74ab-3614-8baf-a3a1e8bfc909 | -9.14168 | -67.81461 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 445cd74e-bb14-3e0c-8105-fb28b70d6a47 | -9.15785 | -65.80747 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d243ebcc-1f30-3655-9bd8-ba2e33e39e51 | -11.40704 | -62.03094 | 2026-09-11 05:50:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de549f09-a9c2-373e-b4ca-c0257956d22d | -9.09129 | -65.4965 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff049546-7f48-3e04-9173-2cfbad83d6a3 | -8.98568 | -65.41121 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f72e6bf-b26c-37db-b36c-ca8c3a6f4055 | -9.41786 | -65.85996 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5a1c64a-f800-3f83-b855-30d39d6d481a | -11.80737 | -60.45917 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d178371-609b-3653-bfbf-feade390ffcc | -9.10013 | -65.48351 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc6e4901-c8c8-38db-86bc-cde73f7a3d5e | -7.13907 | -73.11414 | 2026-09-11 05:50:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4357348d-ebdd-31e2-9033-570ca4ba505c | -9.22782 | -65.57858 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06de7a91-09be-3620-8944-bcf04168fb82 | -9.0073 | -65.42542 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20252220-f0f7-3ef8-9036-587f1c1d1ed6 | -8.88178 | -70.84601 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17251ead-5588-3064-b571-e1bef791e15a | -9.32025 | -68.20245 | 2026-09-11 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f38e45c-6d45-3246-b54b-82cf491a2885 | -9.08835 | -65.38444 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd55f109-9552-3508-af8d-5de338a7f6e8 | -8.52453 | -70.95682 | 2026-09-11 05:50:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca57c639-3d41-3f17-9283-146f611ad4f1 | -8.93486 | -66.84938 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac792fa-d4b8-32d6-80fe-b0e6714e436d | -8.63729 | -66.52023 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 416a4532-5469-32c2-aa8c-31d029eac073 | -9.46229 | -61.03679 | 2026-09-11 05:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e14052-aef0-338e-ad9f-86ec4d8d9c23 | -13.21907 | -61.63245 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d070a363-c473-39b4-89b7-a035e454dad8 | -9.1817 | -68.2112 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9c1206c0-0eb0-3d7a-876a-6286224547ab | -8.6481 | -69.79312 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 380f21ef-f8ad-339b-a6a3-85979d80a00e | -8.82549 | -63.81413 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6a865af-23d3-3858-aa7e-1d6fcd0c2984 | -8.93599 | -66.84234 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca186764-7e88-397c-9a3e-224f6269958d | -10.19507 | -68.7688 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccadddaa-8657-3042-987b-a9169d565bd9 | -9.18985 | -65.7768 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44806532-fc94-349a-8cea-63a05637151a | -8.53526 | -66.98701 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54ff121f-7b7e-3ef5-8c82-ca574a7cad98 | -9.49749 | -66.79237 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05831db0-7131-347d-aba8-efc81b32d24f | -9.23613 | -65.59064 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0128f740-a495-3cab-9d2a-b1d6ee8c9cfe | -13.32954 | -61.67491 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64d234d5-b6f4-309f-a12f-033024852c2e | -10.28884 | -68.85969 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 678610c3-c6be-3728-998a-6d2eb377720b | -9.54055 | -66.26588 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1921921b-cb0c-3aa9-a9fb-e4a2be60266d | -8.84005 | -69.11195 | 2026-09-11 05:50:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b72bb566-6584-34a4-bbb9-5de0ce5c1f23 | -9.28707 | -65.80688 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daa9ac87-e11f-31aa-8f57-6cec63230b36 | -8.82203 | -63.8136 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83275dba-ab43-3658-b59b-4a79a75dc2d2 | -9.23281 | -65.59012 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f1816c-f887-3abe-8e70-5877efdbbadb | -13.3424 | -61.6729 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36033ef4-ef02-3271-9134-165d4b8520f4 | -8.83535 | -62.48672 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb716b79-84b3-37c7-bb84-cbeb1c6bdb43 | -11.40665 | -62.0328 | 2026-09-11 05:50:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e27b16e-2dfd-351f-ab30-6b81055e0adc | -9.14543 | -64.39982 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29880a6-b38f-39c1-9fb3-8ca8965204d0 | -9.33592 | -68.23609 | 2026-09-11 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84ec68e-0379-308b-a4d0-d5be0a564523 | -9.41454 | -65.85944 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1cee4b-6f07-3f07-a0b3-ef674e3e8ccd | -8.65721 | -66.50195 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb326273-d502-3725-bbc4-78224033492a | -8.63288 | -66.5052 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef2989e-94c0-39d0-a592-97ca1dd26f63 | -8.15022 | -69.87097 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc919c70-392d-398d-8395-bdd9856a7d93 | -13.21805 | -61.64 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94f5f3d3-cf8b-3cd4-bd21-46431c38dbd7 | -9.13867 | -67.83302 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccb0c8a4-c161-3c29-a488-8ff41f7382c3 | -9.39743 | -65.86028 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a573e11-fc1a-3dbe-a142-87599a3fcd16 | -13.3244 | -61.68185 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52b4eb37-307b-3121-85c3-413fe0561505 | -9.03551 | -68.20735 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9439b76c-86f2-3d49-a672-74ab1300dc0b | -8.63675 | -66.50224 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bac78e78-9726-3e87-99e6-1f91a2461f0d | -8.989 | -65.41174 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df8803c-1093-345e-8922-fe066f8cb36d | -9.75433 | -64.94511 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 685b3695-f6cf-3d14-a752-af7f2afcb556 | -8.63183 | -66.99931 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e207156e-6f11-3b73-a9cc-03b876e012bc | -9.988 | -67.58951 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dee7844c-6f62-3860-8f8d-d28243f78cd5 | -10.57812 | -68.77156 | 2026-09-11 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ce01334-0a9b-3593-bcfa-cc2d7714f22d | -9.39688 | -65.86377 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0725f63-1fc9-3734-b1a8-2d927a3f43f9 | -8.7188 | -71.5477 | 2026-09-11 05:50:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a28ab947-3b28-3d79-9308-dcf239ed4f4b | -9.15678 | -64.41669 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8709fac9-0f71-39cc-9cf7-ab881b4f740d | -9.02722 | -65.40698 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09bfe2d4-6109-3f43-aab4-ee85e5428ff0 | -8.82151 | -71.80304 | 2026-09-11 05:50:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfebe76a-3ef7-3761-9e00-2247b4798953 | -9.70965 | -65.07807 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README34.md)
