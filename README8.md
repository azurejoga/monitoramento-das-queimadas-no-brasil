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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4245441-ec06-30d4-b846-29e91fe7c3c9 | -3.8166 | -52.3608 | 2024-11-21 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c855e949-b9fd-3d64-8dfa-9e5cbaceb980 | -4.5799 | -48.0349 | 2024-11-21 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 45cc5466-7002-344e-8614-ca4e117f6638 | -6.214 | -46.2202 | 2024-11-21 01:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 3e069387-23c7-3c5c-bd31-fe5889ab10ba | -4.5614 | -48.0141 | 2024-11-21 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 878e3ca5-591e-375e-a6d3-6b39aba51beb | -3.2757 | -45.4477 | 2024-11-21 01:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1db2b1c9-fb10-3882-9800-c6e1e5d28d1c | -4.2388 | -46.1197 | 2024-11-21 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 52f1b432-590d-30e4-907b-272106e561fa | -4.1413 | -43.8828 | 2024-11-21 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a41670b1-e3ef-3e9e-ba65-61b7fff1ef00 | -6.8258 | -46.7737 | 2024-11-21 01:40:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a6aae5ee-619a-3ca6-82fb-d1cda2beaa66 | -4.7717 | -44.4891 | 2024-11-21 01:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6166b31c-015e-3ce1-93fe-55bf6814f107 | -3.2951 | -53.8395 | 2024-11-21 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 64de9296-a912-3f38-a27d-73eac46fb489 | -3.8167 | -52.3403 | 2024-11-21 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 01226f80-6a95-3c0b-884b-71e6f111ec79 | -4.16 | -43.8818 | 2024-11-21 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7d508bc0-39e6-3e82-80c1-ac0d65199738 | -2.7676 | -52.1045 | 2024-11-21 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2bf6c642-de52-3d25-8dd9-76d67f196054 | -3.2768 | -53.8199 | 2024-11-21 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 891b686a-4fc0-33d5-89c4-a30b3ae6cda6 | -10.1223 | -65.0237 | 2024-11-21 01:40:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fa72c52f-7596-3990-bb0d-286c8bca3e2e | -3.0354 | -49.4688 | 2024-11-21 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| af3bc7e4-4d38-33f8-ab7a-5557395d0a02 | -2.0259 | -54.5289 | 2024-11-21 01:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 36f67346-a248-31db-bdf6-90bc2cde7d18 | -3.374 | -52.4568 | 2024-11-21 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| e215f458-18fc-3c7e-b27d-c83180fa07a7 | -3.0354 | -49.4688 | 2024-11-21 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ac3db512-0ab1-3546-bfba-045d3d7ece0a | -3.8166 | -52.3608 | 2024-11-21 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 7db61ea3-4dcb-3c3e-8061-061ec7dd6371 | -4.2575 | -46.1188 | 2024-11-21 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f3303360-3ef3-323f-a3d5-8977036f0b1a | -2.0259 | -54.5289 | 2024-11-21 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 44a90ae9-349e-3dbd-bcef-ad51d15ed379 | -4.5986 | -48.0123 | 2024-11-21 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3427dad0-f3f0-30a3-ad61-e1a1e9125e11 | -1.601 | -46.8729 | 2024-11-21 01:50:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b5b37722-a729-3273-b5f9-a31b7e100e0f | -3.2767 | -53.84 | 2024-11-21 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| f836236e-b283-351b-8b9c-08460cb36b20 | -2.0075 | -54.5292 | 2024-11-21 01:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4ccb7b1a-6ae5-320c-9e33-3f131f013d41 | -4.5799 | -48.0349 | 2024-11-21 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c055647e-c9e2-3352-8700-5006c4852ffa | -3.374 | -52.4568 | 2024-11-21 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2d425a39-af19-3a55-a686-bd146b7f46c5 | -4.5614 | -48.0141 | 2024-11-21 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c29f22ed-bcd8-3ef3-9c08-a6738b169a85 | -3.2951 | -53.8395 | 2024-11-21 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 668c87bf-c9f1-393c-ae8f-157ae0af5da1 | -4.7717 | -44.4891 | 2024-11-21 01:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 981c5f45-e0d1-3357-92be-164d2c6c83e1 | -3.2768 | -53.8199 | 2024-11-21 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ce0c1645-8eee-30da-8aa3-72653a0778d0 | -4.16 | -43.8818 | 2024-11-21 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a9a91c9d-8bb1-36af-938b-3bd1e2fb652b | -6.214 | -46.2202 | 2024-11-21 01:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2db0baa9-869c-3da3-9389-5faf35d60400 | -3.8167 | -52.3403 | 2024-11-21 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 704808da-11dc-3b21-8987-ac56e89671c6 | -10.1223 | -65.0237 | 2024-11-21 01:50:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 939a42e1-8bd1-30eb-bf0f-cbf3bda60841 | -4.2388 | -46.1197 | 2024-11-21 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a46993fc-32f7-3255-933b-536f1f2fde00 | -4.58 | -48.0132 | 2024-11-21 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 6a05105f-feee-30eb-bb9c-c7600328f66c | -3.295 | -53.8597 | 2024-11-21 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8481da7f-af60-3557-9ca2-6669c5edac70 | -3.3924 | -52.4563 | 2024-11-21 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 17e6a398-2ee8-390d-a64e-bf9d57485bf8 | -3.0354 | -49.4688 | 2024-11-21 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b8b6cc26-41f5-3a44-86f3-f1a7b2115e01 | -1.601 | -46.8729 | 2024-11-21 02:00:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f00c3827-53a6-3d48-9314-33979b46ea63 | -3.2952 | -53.8194 | 2024-11-21 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3ab42c29-140c-3878-baa1-ae88cc589bda | -4.58 | -48.0132 | 2024-11-21 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 16d1145e-b0d7-3733-91be-1910b639badf | -3.374 | -52.4568 | 2024-11-21 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 8f4abea3-1911-3bca-a529-0a74c2723d1c | -4.16 | -43.8818 | 2024-11-21 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2a8ae102-e78c-3ea3-b77c-46f658aa2d78 | -4.2388 | -46.1197 | 2024-11-21 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 413d3d7b-b056-3d34-9438-199bb0e74f03 | -5.0996 | -43.1744 | 2024-11-21 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 13bf649b-4185-3c7b-80db-9f8eef475424 | -4.1413 | -43.8828 | 2024-11-21 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8122d39d-4558-3b64-8a58-4d4c760836cb | -4.2575 | -46.1188 | 2024-11-21 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 37982601-2c0d-3a79-aefc-056dfcd3de0f | -4.5614 | -48.0141 | 2024-11-21 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b9cb9718-7e48-37cd-8df7-ffcdd62d855a | -2.0259 | -54.5289 | 2024-11-21 02:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 37e7d95b-e43c-3f22-bda5-bff57dcd9058 | -3.2951 | -53.8395 | 2024-11-21 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8b50f326-de2e-369d-a220-d2cf2c87c62d | -3.2768 | -53.8199 | 2024-11-21 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f438bf2a-378e-327d-ae89-78295f02e2d4 | -3.3924 | -52.4563 | 2024-11-21 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fff77eb4-03a9-351f-a3e0-64e1bbb3691a | -6.1182 | -42.5086 | 2024-11-21 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| cb23c7c5-8917-3410-9f1c-8883e57a3e83 | -2.0075 | -54.5292 | 2024-11-21 02:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 63531cad-77ff-3ee3-997a-7f826c69bc5c | -3.2767 | -53.84 | 2024-11-21 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0c408f0f-b15c-39b4-b8cf-a206216f38c3 | -4.7717 | -44.4891 | 2024-11-21 02:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 258fce14-99ed-3456-889f-2bd3aad7ecf0 | -3.8167 | -52.3403 | 2024-11-21 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 248789fc-5335-39db-9f59-e00236bc38e2 | -4.5799 | -48.0349 | 2024-11-21 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 3dff5b58-3ad7-3fb3-84dd-7ddf57e594f7 | -5.1183 | -43.1731 | 2024-11-21 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a3aa61e3-ab1f-3d9f-8b17-74e96ea940f0 | -6.8258 | -46.7737 | 2024-11-21 02:00:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e070e485-3b27-3e52-8563-e3ad2fc4a2a4 | -6.214 | -46.2202 | 2024-11-21 02:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c0f444c2-8665-3424-a864-3679abd1889d | -3.295 | -53.8597 | 2024-11-21 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3fff127d-0ca7-3ff5-a1a1-40e9385e5ad8 | -9.65105 | -65.74252 | 2024-11-21 02:04:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ebd1bc4e-076f-30e9-b04f-b8d4170f6038 | -10.12275 | -65.01967 | 2024-11-21 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 45c8b0fa-890c-3472-94bb-da5d0cdd54bc | -10.124 | -65.02863 | 2024-11-21 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f0b79472-11dd-3d34-9aa4-5aa3d74ce038 | -4.58 | -48.0132 | 2024-11-21 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 990542c5-fb01-3e6f-b8bf-bce08131cfd7 | -4.16 | -43.8818 | 2024-11-21 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 42b14d12-c532-3963-9022-b1ec0257031a | -4.5799 | -48.0349 | 2024-11-21 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 85791244-6aac-317b-9710-eeae7b8b8867 | -2.7676 | -52.1045 | 2024-11-21 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5d5e5a5a-4572-37ae-9b00-aac66e69598c | -4.1413 | -43.8828 | 2024-11-21 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e83a9317-4bdd-378d-82a4-ac3c7d1aebb3 | -3.2951 | -53.8395 | 2024-11-21 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 34ab3f65-9ac3-331b-8ff0-e12f1c4d7eeb | -3.8167 | -52.3403 | 2024-11-21 02:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c44da032-3362-3537-84e2-8708bac471c6 | -4.5614 | -48.0141 | 2024-11-21 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a1320a8b-65bf-3da5-8184-f643a2c748a2 | -3.374 | -52.4568 | 2024-11-21 02:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 548c3f8a-1f69-396b-b038-18854b406c9c | -3.2768 | -53.8199 | 2024-11-21 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 992fd2a1-6e3c-305d-8a97-6ab494112c14 | -3.295 | -53.8597 | 2024-11-21 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 13e2ff9f-5e5a-3e31-98a4-c579dd3c0787 | -5.1183 | -43.1731 | 2024-11-21 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2d624a6f-92e3-3a47-b2f8-493e4b62f6c7 | -2.0259 | -54.5289 | 2024-11-21 02:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e7d3b880-3352-3920-b7a6-ef74978a6185 | -1.601 | -46.8729 | 2024-11-21 02:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b0b3e7d7-63e9-3bc6-8179-c9a2d99a21e2 | -3.2952 | -53.8194 | 2024-11-21 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| efbc474e-9117-33c0-8291-9ded27cad654 | -3.0354 | -49.4688 | 2024-11-21 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d177a842-a6e5-3037-b804-431b44df2444 | -2.0075 | -54.5292 | 2024-11-21 02:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 418cdaa5-d7f9-3555-940c-5c9c5ac7eeff | -4.2575 | -46.1188 | 2024-11-21 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 106.5 |
| f8d9ba7a-ad30-353e-afdf-137bc31bcc97 | -4.7717 | -44.4891 | 2024-11-21 02:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a96aae03-573d-320b-94f4-1ef177c44ebc | -6.8258 | -46.7737 | 2024-11-21 02:10:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5ac4706d-d209-344c-9d4c-7605159b275c | -4.2388 | -46.1197 | 2024-11-21 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1bb97cf7-fd82-33dd-95e2-409ecef5640a | -3.2767 | -53.84 | 2024-11-21 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 760b54cd-e72d-3012-8e89-f5f42e2cda4a | -6.1182 | -42.5086 | 2024-11-21 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| ef5a3ba3-a501-3b6c-9b3e-8de7b24e3395 | -3.2951 | -53.8395 | 2024-11-21 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| b3186768-fc01-30f8-ae49-4eb03008a2b4 | -3.0354 | -49.4688 | 2024-11-21 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 291cc462-8beb-3e4b-be3e-566be10d1e32 | -3.2768 | -53.8199 | 2024-11-21 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a16c086e-3237-397c-b148-5a976ac2e7e2 | -1.601 | -46.8729 | 2024-11-21 02:20:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 90e3f1c9-26ef-3ecf-b1f6-a7b7dcc0850a | -2.0259 | -54.5289 | 2024-11-21 02:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 25270102-ea7f-3183-bbb3-48818acc6181 | -3.374 | -52.4568 | 2024-11-21 02:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cfb67275-1e05-3148-beb4-370595c0eb44 | -6.214 | -46.2202 | 2024-11-21 02:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0b7cfac6-b974-39c7-82b5-49b67d4973be | -4.5614 | -48.0141 | 2024-11-21 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 842034ab-a097-305f-b305-46c7eb2c3d77 | -3.2952 | -53.8194 | 2024-11-21 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README9.md)
