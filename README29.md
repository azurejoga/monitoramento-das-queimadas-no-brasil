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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d75a3534-5fa4-3dff-841d-5264acfde598 | -9.7138 | -43.4192 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 485.2 |
| b928decb-999f-36b5-ac32-7099146dfd43 | -9.7328 | -43.4168 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5d29b389-fd06-3a0a-859c-600ea41acc00 | -9.7515 | -43.4378 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| b33b4c0a-1705-39ae-af87-e5c37935e273 | -7.697 | -44.3016 | 2026-09-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| dbe2c472-bad1-3107-ab8c-1b3fc93d6f17 | -10.8049 | -60.7644 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 16b1eefe-35db-3742-bf8c-436bc1a8b925 | -10.1155 | -45.7257 | 2026-09-08 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| cb51c626-a8b8-302b-999b-cf247f1df4e7 | -10.8233 | -60.8019 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 52dba28a-19fe-37c5-a533-c1bd1ffd46cf | -10.7862 | -60.7655 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 00fdb0db-ae89-36ac-a06e-356bdbf25d0b | -10.7674 | -60.7666 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 17df22c8-7ed2-3b6f-a36f-4e7df1a2515f | -10.8421 | -60.8009 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f17d71a6-75bb-3627-8137-a3fe8040658f | -9.7508 | -43.485 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 7d31e926-d429-37e7-b249-82eb36d408f8 | -7.7156 | -44.3228 | 2026-09-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d3fef278-6039-3b80-8eaf-c824fbe5218d | -9.7702 | -43.4589 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 540.3 |
| 65ccdc10-a77b-361e-9201-57d82abfc25e | -3.8289 | -53.7634 | 2026-09-08 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d6080526-90f4-34a7-94ef-852e67010a90 | -9.7511 | -43.4614 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 258.4 |
| be9b2e5e-7033-33b6-9507-d2033da2594e | -8.7066 | -62.4374 | 2026-09-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| be917998-1363-3494-b737-e18aec35f339 | -9.7332 | -43.3932 | 2026-09-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 109.5 |
| a72774c6-4c16-3dfd-846b-d9185c34e2d5 | -10.0964 | -45.728 | 2026-09-08 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 0b4aa9bf-6279-3e8e-822e-4a38f8b4ffed | -3.5406 | -48.1889 | 2026-09-08 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 7a228f0e-2718-3bbc-b2ad-5426e85c4771 | -8.7252 | -62.4367 | 2026-09-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 811a0f5a-fc16-3e5a-90d0-1515519a289c | -3.8604 | -44.0585 | 2026-09-08 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f4dc276e-647f-3b1a-b852-e28471721317 | -10.7676 | -60.7472 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 16fbd850-337f-3c5d-a14a-c342c597a1e1 | -7.6779 | -44.3266 | 2026-09-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 549e591d-8a69-385b-9dc4-cc0b26d8c0d3 | -5.3646 | -56.0249 | 2026-09-08 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 13c1913e-304e-3ebc-a62d-6b4d78ae3875 | -10.8233 | -60.8019 | 2026-09-08 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ff2fe2dc-7c02-359b-be34-5e7839d608fb | -9.7332 | -43.3932 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 116.6 |
| f3df63b4-a777-3f0d-a40f-17dcbe1c569a | -7.6968 | -44.3247 | 2026-09-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| fd91f917-29ba-32d7-ad6d-e7469a929d81 | -7.6779 | -44.3266 | 2026-09-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6a229fc9-b782-371b-bd00-8d1979a451ba | -9.7321 | -43.4639 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b250afcd-d521-3a02-861b-432e98c96fe9 | -3.5592 | -48.1666 | 2026-09-08 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| bba8ccf3-77ac-363d-bae0-80d2da6996fa | -9.7511 | -43.4614 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 9a0647ca-9a73-307c-86d6-874779f95a30 | -3.8289 | -53.7634 | 2026-09-08 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f46d8923-6cac-3d54-87a1-a8cd6304c18b | -10.0964 | -45.728 | 2026-09-08 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 2ec8d548-4206-360e-9222-019893080b1c | -9.7138 | -43.4192 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 708.2 |
| 819805f8-5be5-303c-9320-d8066a9287fc | -7.697 | -44.3016 | 2026-09-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| dfbf55b7-b05e-32ee-8869-cc9463add448 | -3.5407 | -48.1673 | 2026-09-08 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| e8f04361-b080-35eb-8c3a-00f565509e96 | -9.7328 | -43.4168 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 324aaccc-a50c-3561-a105-f0ca7b19daca | -9.7508 | -43.485 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 244.9 |
| cbc3639f-4bec-3bdd-978d-4195fec57dc7 | -9.7515 | -43.4378 | 2026-09-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 9f9fb40b-514d-32bb-aa0a-65daf5baa114 | -8.7252 | -62.4367 | 2026-09-08 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 41d27cf2-950f-35a0-8c04-d1738b6a5894 | -3.5407 | -48.1673 | 2026-09-08 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2f00bcb9-7bf4-34ca-88ab-dd05bf208e16 | -7.697 | -44.3016 | 2026-09-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7708b6c4-bbcf-3028-a908-ad3f1bd15822 | -8.5321 | -63.8792 | 2026-09-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 32c8e5b2-aa9a-3e65-a18c-7c1268dc0930 | -3.9546 | -59.3569 | 2026-09-08 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| bc14520f-7244-3f4b-a729-8d4a8c081218 | -10.2372 | -45.2087 | 2026-09-08 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 04a2d24a-d431-31c6-8ca1-236cb56dd96b | -9.7332 | -43.3932 | 2026-09-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 49cebe71-9c70-3746-a07e-a92613fc1f75 | -9.7328 | -43.4168 | 2026-09-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 686ce895-ecd3-36f5-8b2a-c5567d605c99 | -10.0964 | -45.728 | 2026-09-08 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 9ee893bb-9dd8-3d24-9a82-992d9c66b10c | -7.6968 | -44.3247 | 2026-09-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7480af56-ea21-3dda-816f-a96de3c70769 | -7.6779 | -44.3266 | 2026-09-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 252475f9-8f26-325e-a5e4-6d9eb4c01b77 | -8.7066 | -62.4374 | 2026-09-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| fcd35449-6b88-3c68-bc3d-93adebcaa236 | -8.7622 | -62.4351 | 2026-09-08 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fad2780f-8e0d-33af-b66f-0c44efa22f39 | -8.5506 | -63.8786 | 2026-09-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 2e85df00-1d82-39fe-9166-76e9dd26d613 | -1.1991 | -55.7501 | 2026-09-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e96c7df0-67cc-348c-9ebe-245a4cba473e | -7.2158 | -43.6069 | 2026-09-08 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0fe4811a-eed9-319a-80a4-6e0dddfd7908 | -9.7511 | -43.4614 | 2026-09-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 16a5d2f8-27c6-3ee6-a316-3e02a59d7156 | -2.7398 | -49.4776 | 2026-09-08 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| bf91abe4-660e-366d-947c-f533617a9d89 | -3.364 | -50.4072 | 2026-09-08 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ebc09597-b1df-38b7-8647-c74c2be413a2 | -5.5793 | -43.9992 | 2026-09-08 14:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7b0e57cc-3e82-3256-b256-912a14d602bd | -8.7252 | -62.4367 | 2026-09-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4a822c36-cadd-34dc-a2ba-663de8886f9d | -3.3641 | -50.3863 | 2026-09-08 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b0fe6188-0c86-36f5-92b4-f92c0bacdfc8 | -9.7138 | -43.4192 | 2026-09-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 607.9 |
| d106c0cb-22cb-3098-8477-a8c3012a444e | -9.7325 | -43.4403 | 2026-09-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| b502947b-e196-38a9-a486-3e7ba34b4464 | -8.8175 | -62.4898 | 2026-09-08 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 100cde6b-c2fb-3ad6-9ee7-e8668d189ca2 | -10.786 | -60.7848 | 2026-09-08 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 929208ad-34f0-3cbf-9a63-2b59ef090e43 | -8.7437 | -62.4359 | 2026-09-08 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a51cdb06-73ff-3077-ad10-95cf4ecae4e4 | -8.7622 | -62.4351 | 2026-09-08 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7a2ea3ff-a2b7-3b58-95e5-19136c4dc03d | -7.6968 | -44.3247 | 2026-09-08 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b550e28c-a54f-34f6-a960-06b2f150512b | -9.7508 | -43.485 | 2026-09-08 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| c8b7c547-d594-302b-ad64-2b1e56f19f40 | -8.688 | -62.4572 | 2026-09-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f7043c51-e65f-38f6-8b69-d2cab25eccb4 | -1.1991 | -55.7304 | 2026-09-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5fb8d9ae-c9f9-3928-9784-754863c05269 | -10.1151 | -45.7484 | 2026-09-08 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 8490968b-0799-39b0-9b48-de2923672689 | -10.1155 | -45.7257 | 2026-09-08 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 03acb93b-8fe6-3d46-b82d-17b5944c71ae | -7.2158 | -43.6069 | 2026-09-08 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 445cc0fd-6b2c-38b0-809f-7bacfe2f8e77 | -8.5321 | -63.8792 | 2026-09-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 05d7118c-dfc2-3ce7-817b-33618d0d3fe5 | -10.0964 | -45.728 | 2026-09-08 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 0485dfe9-7be5-360c-9a19-660a224c9f25 | -1.2174 | -55.7302 | 2026-09-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 14051b82-947e-3dea-8499-9cc2238fbc6d | -7.6779 | -44.3266 | 2026-09-08 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a059cb5f-f56e-3bd3-bb0c-46bcd64f97ac | -9.7511 | -43.4614 | 2026-09-08 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 59b09901-a102-3ee2-bccb-0ec77259a1c9 | -10.8049 | -60.7644 | 2026-09-08 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f105cda2-c904-31f8-83e1-db70867c32da | -8.7066 | -62.4374 | 2026-09-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1c4287d9-eaab-3c2e-a173-4316b243da12 | -8.5506 | -63.8786 | 2026-09-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cf78b47b-662f-3445-8268-744132760b9d | -10.8233 | -60.8019 | 2026-09-08 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 037d6d24-23fb-3942-b0e8-1289b2fae3bc | -8.7252 | -62.4367 | 2026-09-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 234b7501-a10b-3f19-a60f-053e031e8477 | -10.8047 | -60.7837 | 2026-09-08 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1ff20cac-bf03-381d-8ae8-81fa1fd131e0 | -10.2372 | -45.2087 | 2026-09-08 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9585e2c3-9cb6-397f-aa74-d3512d42bd19 | -7.697 | -44.3016 | 2026-09-08 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6beaeb26-f477-3760-a444-8c35ba2b3571 | -10.7862 | -60.7655 | 2026-09-08 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8722a04b-9aae-3335-bdcd-00cd90b0afc3 | -7.6968 | -44.3247 | 2026-09-08 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 04936692-f55e-3076-98b4-f1f9325bb73d | -1.2174 | -55.7302 | 2026-09-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 982ed940-8a0b-38e2-8784-a20cbb0cd463 | -10.0964 | -45.728 | 2026-09-08 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 664c7155-1315-3a04-8b32-eecc580d8a9b | -8.5506 | -63.8786 | 2026-09-08 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 43d393c7-3fd4-359c-ac33-120526623d81 | -8.5321 | -63.8792 | 2026-09-08 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c7d88f7e-de53-34df-b192-b676fd43a201 | -1.1991 | -55.7304 | 2026-09-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 78e8cb0a-05c0-3ac9-8831-8a498d350da5 | -9.7138 | -43.4192 | 2026-09-08 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 429.7 |
| e9123df4-eca8-3f71-8894-03c147ab1b82 | -2.7398 | -49.4776 | 2026-09-08 15:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| af8d7528-1da6-36a9-9dc0-e1f34906e598 | -3.9439 | -49.0104 | 2026-09-08 15:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e6f42975-48c3-3ccf-8ae7-ae40c0152e1d | -8.8175 | -62.4898 | 2026-09-08 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3f471bf8-1adb-3b97-8a97-b4a967a68089 | -2.7582 | -49.4983 | 2026-09-08 15:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 31893202-88c0-3e94-85b7-17e6a498c807 | -8.5322 | -63.8604 | 2026-09-08 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README30.md)
