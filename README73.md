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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceaf50b1-5502-32b3-a41f-81037107e953 | -9.47291 | -64.33157 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6e02bea1-8144-3c16-8575-450981feb2fc | -9.57017 | -66.29874 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 648b323d-194e-3bc3-a661-a097cae4333a | -9.40377 | -65.90855 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f1b175f9-413e-3aae-a258-f56e7721a586 | -9.67902 | -64.31533 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b450ebf5-224d-39dd-954a-342fd064fd99 | -9.48264 | -64.33283 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 82753494-d598-3a29-b3fe-f1f68454afec | -8.8645 | -66.65977 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| acf4cafd-9c8e-349b-a25e-304439a3ec77 | -9.48738 | -64.68824 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 907d25e4-7383-3a58-a166-242faf2217a5 | -9.03465 | -67.47002 | 2026-10-04 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a6df752-ce9d-35cd-8b35-b99266ac2112 | -9.21098 | -64.44341 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37efcad9-ead6-3fc9-a5ba-d1b32b2ba950 | -9.11859 | -67.71555 | 2026-10-04 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a0e1f6c8-9b65-32a2-8a88-c11cfd085f04 | -9.57259 | -65.09081 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6db8b1bf-8bcb-3b39-b2b9-4858bd16f5e1 | -8.85569 | -66.78515 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0cf2a3ad-fa47-3047-a220-f41aeaf32693 | -9.67753 | -64.32631 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 56d3647e-5c38-3309-a8ac-410d1bc60925 | -9.04409 | -66.04025 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca336ed3-6de0-326b-aecb-808bd43d1251 | -9.88709 | -65.13758 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0ddb3c2c-235b-39b9-a1df-9e4e76fd63f0 | -10.01357 | -65.23252 | 2026-10-04 13:01:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 796ca9e1-c6a3-355e-b56f-5de06bae2196 | -9.05571 | -65.42759 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52ff96e8-261d-3add-9699-bd27b9aa83f9 | -9.13385 | -68.24977 | 2026-10-04 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d3a93237-6da7-3e04-9025-a4e266fa6df8 | -9.50463 | -68.49508 | 2026-10-04 13:01:00 | TERRA_M-T | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4fad8eab-3f5d-3b7d-a46f-d395e40d6042 | -9.12847 | -65.89933 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c5d68585-eca8-35ae-bc42-9a7843740632 | -9.89409 | -65.0151 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cabceabf-3333-3cf3-be89-bcffc39f59a2 | -8.89094 | -66.72681 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 73553f95-b2e7-3b24-aceb-ecb26383fbf9 | -9.13105 | -65.94662 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1828c35c-9bf2-30e2-ac08-e2aaa92f3163 | -9.92088 | -65.02907 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ad3a5d98-ce0f-3435-8560-a9266cf25006 | -9.15931 | -68.26929 | 2026-10-04 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7fa0aa1b-9877-3ca2-ae87-9d4d4d4980e3 | -9.40505 | -65.89928 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84f7feee-c128-3431-997d-fcfb36919d99 | -8.88875 | -66.88612 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa893337-4278-324b-9f8d-25d474cd6fe4 | -11.793 | -43.5452 | 2026-10-04 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| bf32fc5f-0a9d-3460-a934-e1c9ae0fa91f | -11.487 | -43.4981 | 2026-10-04 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b7f19c92-6aca-350f-b1bb-4444d71942d5 | -11.2621 | -44.3066 | 2026-10-04 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 091cf40a-f446-3be7-b478-77061f06b2ce | -11.8123 | -43.5422 | 2026-10-04 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 19b9fcdb-c0ca-3589-8b75-46b85caac7a0 | -11.2242 | -44.2888 | 2026-10-04 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4505c33f-3195-37ae-84e8-2f6476c5d26a | 3.4155 | -51.3021 | 2026-10-04 13:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ca694c47-26bd-3ba3-98c4-6ad835fde958 | -11.1775 | -44.7832 | 2026-10-04 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 462e900b-9f4f-3f38-9aac-5a6644936592 | -3.11 | -53.69 | 2026-10-04 13:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f9b4b6-69df-317b-b0c1-704d1c720093 | -3.11 | -53.75 | 2026-10-04 13:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4430c86-77e0-3f8f-8ecc-2f3e825a5090 | -11.6404 | -43.4981 | 2026-10-04 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 23ce2076-325d-355f-ba7e-eeaf920a3357 | -11.7147 | -43.6283 | 2026-10-04 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| aad4d73a-8591-3f62-bef8-7869a7a02e85 | -11.1775 | -44.7832 | 2026-10-04 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 1abf12cc-f908-35c4-82d4-83f3a96f49e2 | -11.3551 | -43.3764 | 2026-10-04 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e92e3811-7b6c-39bc-ab8f-cf6e8ccbe4ff | 4.1882 | -60.687 | 2026-10-04 13:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5b5a319d-88c1-3bf0-b83a-9d0d761721be | 2.8909 | -60.465 | 2026-10-04 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e67a0802-3039-33b2-8c14-3cba5baa7c07 | 4.1882 | -60.687 | 2026-10-04 13:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8114dd23-35ad-3c3c-9528-50173379c21b | -10.9445 | -43.8849 | 2026-10-04 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 97614afe-633d-30e5-80cc-9a8b5a718dd7 | -11.7147 | -43.6283 | 2026-10-04 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1929ede2-0f42-393c-be72-86d09d52b74f | -11.4695 | -43.4062 | 2026-10-04 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 6a4d8a97-764a-308c-a802-e7c674a94738 | -11.8127 | -43.5184 | 2026-10-04 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f55df9ca-0a38-3e1e-a07b-a25023ba87a9 | -11.793 | -43.5452 | 2026-10-04 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| f9f80030-3b1d-3c21-b79c-c3d3ce29217c | 4.1702 | -60.5924 | 2026-10-04 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 487be25a-9b47-313e-9d8b-6d1eb19eafa5 | 3.6757 | -60.8116 | 2026-10-04 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b18dcfe6-494f-39c9-ae46-46224775002d | -11.1775 | -44.7832 | 2026-10-04 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 0cd6f20b-62ce-3d89-b358-937e91caaa6b | 2.8909 | -60.465 | 2026-10-04 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.3 |
| d1c297f2-e735-3101-bd2a-6c6d57d457e6 | -11.2058 | -44.2448 | 2026-10-04 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a5e24841-0f70-3035-a7bd-0374f31e30b0 | -11.4695 | -43.4062 | 2026-10-04 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 3ff39ee0-dee8-3752-943e-1215c2b47150 | 4.1882 | -60.687 | 2026-10-04 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.8 |
| d8f98466-decb-317e-8077-1f46efdbce95 | -8.0159 | -42.9154 | 2026-10-04 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 44bca50e-5419-338d-bb25-939c32476a88 | -9.8257 | -44.8011 | 2026-10-04 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 15c2b184-50d3-35fb-821c-bc67168abfc7 | -9.9175 | -65.0313 | 2026-10-04 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 85c22822-4657-318d-b672-bbee8e1a7382 | 4.1883 | -60.668 | 2026-10-04 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 626d9185-e03f-3e63-a831-aaa9c7c96e1c | 3.8215 | -60.9792 | 2026-10-04 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6dcdbfb5-177f-3c38-b656-5574546acdc7 | -9.9175 | -65.0313 | 2026-10-04 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7e37ce2f-c0a2-3a86-bc6f-939758725421 | 4.1702 | -60.5924 | 2026-10-04 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 74dde888-fdfc-3087-b91d-29de8d7c9607 | -11.1775 | -44.7832 | 2026-10-04 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 318fbb7e-5c88-3626-81a8-21c719a6c0ff | -11.2621 | -44.3066 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 1551f1d2-3fc7-3682-9327-0f68f37fb7a6 | -11.2438 | -44.2626 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 36ce116c-7279-3764-8856-adca8c74cfa6 | -10.9445 | -43.8849 | 2026-10-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e9dc1c87-5636-3b82-904a-3541b490ffb3 | -11.2058 | -44.2448 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 38543092-902d-30cd-812e-9bc9ca6169db | -9.8254 | -44.8242 | 2026-10-04 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8647a134-2119-3110-bea2-c615d84201b6 | -11.32 | -44.2748 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| fbe317db-46b0-3b8e-8ecd-6051226e6dc8 | -11.2246 | -44.2654 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| da7e08c1-ccd6-3207-b901-4f5ee524b1a8 | 4.1883 | -60.668 | 2026-10-04 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 34a781d1-cae1-329b-a832-f489bda06a67 | 4.1882 | -60.687 | 2026-10-04 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 36d95a26-5f80-3556-9e83-f8f979efea43 | -11.2633 | -44.2364 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 7edfb85e-5ebc-3d59-8ca3-4bc579442dce | 3.9686 | -60.6918 | 2026-10-04 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7a091a26-16da-3a96-935e-5df4f59b7a98 | 3.4155 | -51.3021 | 2026-10-04 14:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2ed785f3-cb86-3cf5-9007-45bd386fbd90 | -11.2629 | -44.2598 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d9f71487-c33f-33c9-9620-4f34be188c6e | -11.3009 | -44.2776 | 2026-10-04 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 7b6b4855-8244-33f7-a423-e1c7380cf6f9 | -7.5248 | -44.5485 | 2026-10-04 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2cb76365-2093-3313-959b-5c5cf1fde562 | 3.531 | -60.2446 | 2026-10-04 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 472e876b-79fb-3d21-9bf0-886795010867 | -6.6882 | -47.4675 | 2026-10-04 14:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 39029ddf-5217-3fb2-a44c-f4bd8fd0975f | -11.4106 | -43.4862 | 2026-10-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 99328459-fbdb-3693-810e-39694dd61a9e | 2.8909 | -60.465 | 2026-10-04 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 9212a698-0ad4-3a18-be27-30cf0c35f550 | 4.1526 | -60.3836 | 2026-10-04 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 35e481d0-2336-3153-b834-82568e6807de | 3.7483 | -60.9807 | 2026-10-04 14:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7ca209fb-5421-3e19-9aa1-9a65470dec63 | 3.6211 | -60.7368 | 2026-10-04 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f3f63500-31d0-3171-b580-06d0b2460933 | -11.4294 | -43.507 | 2026-10-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0b1650bf-8fb9-334d-95a8-cad0949ed774 | 4.1698 | -60.7253 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a746a7af-f8ae-3923-8a34-066340e0724f | -11.2434 | -44.286 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9665016e-3e57-381b-96ec-9f9603e9a612 | 3.7483 | -60.9807 | 2026-10-04 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f422638a-bd79-33e3-bf20-9c202f59f3e1 | -11.7174 | -43.4861 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a4e37ad6-cec1-3e5f-9ffe-94e693a22498 | 3.9686 | -60.6918 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ca032be7-22a6-3bc5-991d-05ff28e26939 | -11.4678 | -43.5011 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4b540fd4-2414-34fd-8c8c-d086bdd7eba0 | -7.4156 | -42.6241 | 2026-10-04 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 6d3dbcc9-fbb0-3944-8f52-b98e4ff6778e | -11.3009 | -44.2776 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 3dba3b21-1bf2-30f1-af1e-97e6d5af49b5 | -11.2817 | -44.2804 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 453ea0d9-0c8d-304f-8831-8b47e8c29310 | -9.0844 | -44.9811 | 2026-10-04 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4a5e0273-5919-309b-bd17-00efd866472c | -11.4499 | -43.4329 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 6341b3d4-b8c4-3bde-accb-c8c59ce92ac3 | -11.4879 | -43.4507 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5d7a9d29-030c-3299-934c-5f60b6e342c4 | 4.1882 | -60.687 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1be12456-3212-30c3-b491-beac8e9164a9 | -11.3747 | -43.3497 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |


[Clique aqui para ver as próximas entradas](README74.md)
