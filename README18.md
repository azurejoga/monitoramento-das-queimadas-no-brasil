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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37195469-821f-3cdc-adf8-a56efa1f28d9 | -4.3537 | -48.6068 | 2024-11-02 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8f641f38-f163-374a-9d03-a1b9c8702bf1 | -4.4054 | -43.4746 | 2024-11-02 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5336e90e-2e25-3800-943c-5a7c4de6d1f8 | -4.5575 | -43.1162 | 2024-11-02 02:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8a3bc2e6-a83e-3ab0-943a-57333e639238 | -4.5577 | -43.0928 | 2024-11-02 02:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 38d7c7ea-e3e0-3ef7-b1a0-def5fbb67fcd | -4.8067 | -44.8061 | 2024-11-02 02:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| cbbe07b9-9c1a-309c-90b3-bde5df867569 | -4.8068 | -44.7834 | 2024-11-02 02:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7615b056-44ff-3742-b0ec-37133df496f5 | -4.8253 | -44.805 | 2024-11-02 02:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 07112e25-6b98-3101-afe7-02c98a068dbd | -4.8255 | -44.7822 | 2024-11-02 02:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8220d17d-072f-350a-b359-fe2e807fe61d | -4.9252 | -49.1573 | 2024-11-02 02:05:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8a1aaefb-91f6-3648-9282-adb2c607d5f1 | -4.9438 | -49.1564 | 2024-11-02 02:05:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8d28067f-e80a-3059-a328-9ce3c5a3e2f4 | -5.1146 | -46.0264 | 2024-11-02 02:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0381be5b-33af-3ffb-993f-e8bacb9e17de | -7.1294 | -46.3711 | 2024-11-02 02:05:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 73be6739-3da3-3828-8064-b8134ff52146 | -1.5715 | -52.1894 | 2024-11-02 02:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e1bd8d74-839d-3df6-8e8c-2766433b2058 | -2.2568 | -50.4376 | 2024-11-02 02:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f8ebf5f3-129c-392c-a3a0-b4e71ca353d7 | -2.2663 | -53.7422 | 2024-11-02 02:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6c2ccd3b-d6fa-34e7-b0d0-b22c34ab76b7 | -2.8386 | -52.8794 | 2024-11-02 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e8ff6c15-39c6-3be8-baf5-ab0e9d6179c5 | -3.0734 | -54.167 | 2024-11-02 02:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 28fa99dd-bd5a-3644-aa41-b011a97d72de | -3.1097 | -54.2865 | 2024-11-02 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 88d7564e-d32a-38c0-af07-e6e29e287027 | -3.1098 | -54.2665 | 2024-11-02 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d5cf9100-1892-3836-8888-52a5e432a60b | -3.1281 | -54.266 | 2024-11-02 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 6ffe0cd0-0784-35ea-8027-1ecbfc6ee26d | -3.1282 | -54.2459 | 2024-11-02 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 935cb2f9-a817-3fe0-a9aa-bf24ddb92ca5 | -3.1767 | -51.0812 | 2024-11-02 02:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 01c23858-a8b3-344f-ad9a-c6114209d2e5 | -3.2249 | -44.431 | 2024-11-02 02:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e752760a-08ed-33d5-b7c4-3dbcf2694221 | -3.2417 | -53.3562 | 2024-11-02 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 66b016d4-c4ca-32d6-9870-e2269cddc47d | -3.2601 | -53.3557 | 2024-11-02 02:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9b978ba9-2a7d-3f84-9c2c-d06b6a1ce2e1 | -3.7701 | -43.5554 | 2024-11-02 02:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 0aed7286-774b-32d5-a6bd-ae8b4ac0f652 | -3.9473 | -48.3666 | 2024-11-02 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e10f00e4-f239-3a32-a169-1ba6aa253d29 | -3.9474 | -48.3451 | 2024-11-02 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| e4d9f74d-3a2d-39cc-99d5-e8a23fa1169b | -3.8144 | -48.9729 | 2024-11-02 02:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 175865c6-f09b-3dc6-b348-3decc192db2f | -4.3537 | -48.6068 | 2024-11-02 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| e06cbde0-eaa7-37fd-92ca-b6cd6db00c3e | -4.4054 | -43.4746 | 2024-11-02 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d161a2c7-6b8b-36f4-93ba-b4da88870b7f | -4.5575 | -43.1162 | 2024-11-02 02:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8e75fd50-ac1b-3023-851d-e7f4bf013948 | -4.5577 | -43.0928 | 2024-11-02 02:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d23dc4f7-469f-3bbf-b31c-f12cda51cc39 | -4.9252 | -49.1573 | 2024-11-02 02:15:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 65cd1070-1cda-3b89-9b75-d865cfc6152a | -4.9438 | -49.1564 | 2024-11-02 02:15:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a93184c0-d3ba-3cbe-90b1-1e6703f81cc9 | -5.1146 | -46.0264 | 2024-11-02 02:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 00cced77-222e-3b8b-9818-cae4b5141a4d | -7.1294 | -46.3711 | 2024-11-02 02:15:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4fcbffc4-3565-3c6a-b9e3-9bb4b12bc25e | -1.5531 | -52.1896 | 2024-11-02 02:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ba93c645-9b0a-3d72-ad53-115b34792b29 | -2.2568 | -50.4376 | 2024-11-02 02:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 79a3a696-8c95-3246-acf0-256bc34d7727 | -2.2663 | -53.7422 | 2024-11-02 02:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 72e0fe47-e30d-3feb-80d8-4562ff348b0d | -2.8061 | -51.6095 | 2024-11-02 02:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5bed6495-a047-3cc5-af77-764c936c1e94 | -2.8386 | -52.8794 | 2024-11-02 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2d397328-849f-36be-986d-599f7313feeb | -3.0088 | -51.5834 | 2024-11-02 02:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 98aeab9a-c286-3e4a-bce8-56a3c9034db9 | -3.0734 | -54.167 | 2024-11-02 02:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 49f230a0-512e-332e-bd27-edb7d3ddf697 | -3.1282 | -54.2459 | 2024-11-02 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2cf27f44-ee7c-33a9-b135-91531d430088 | -3.2417 | -53.3562 | 2024-11-02 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| d844faa1-9d38-3c66-a118-afd87787e9d0 | -3.1097 | -54.2865 | 2024-11-02 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ef1a0ac3-7a1e-356a-8d4a-a789e3615cdb | -3.1098 | -54.2665 | 2024-11-02 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b23d004e-4247-3753-b38d-0cba24faf394 | -3.1281 | -54.266 | 2024-11-02 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 1d39dbe9-97e5-3c24-880d-e0e5ab4bd2eb | -3.2601 | -53.3557 | 2024-11-02 02:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 068d58ef-812b-34a9-91e3-e1685c4fe676 | -3.7701 | -43.5554 | 2024-11-02 02:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f99914a8-e7d3-3a2a-9093-06d7c7237395 | -3.7888 | -43.5545 | 2024-11-02 02:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e11bec16-6410-3fad-aba7-c973b2d020f9 | -3.9473 | -48.3666 | 2024-11-02 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e6bd81b2-d490-3d4f-88f4-dce79b5ee11b | -3.9474 | -48.3451 | 2024-11-02 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 07bdbd8b-e790-3f74-9205-c1cde9023644 | -4.3536 | -48.6283 | 2024-11-02 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 2372047a-93cb-39f1-a7c9-148241777f31 | -4.3537 | -48.6068 | 2024-11-02 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f6e47638-b484-329d-8ba4-16f27f9df595 | -4.4054 | -43.4746 | 2024-11-02 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c5152739-326e-3b7c-ab64-f3b94dfc6ab0 | -4.5575 | -43.1162 | 2024-11-02 02:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8ce32838-97e7-315c-918a-25331cd5cd9b | -4.5577 | -43.0928 | 2024-11-02 02:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ae0e332f-1513-35cd-b1c0-00867eff814d | -4.9252 | -49.1573 | 2024-11-02 02:25:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bbf8c3df-b3b4-36b3-8693-7fa691c2976a | -8.03072 | -71.31954 | 2024-11-02 02:32:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f8588e80-c24b-3053-86ef-359e6ef76550 | -8.03201 | -71.32862 | 2024-11-02 02:32:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 01552754-e61d-30ab-bc25-367ff8df237a | -8.11378 | -71.3199 | 2024-11-02 02:32:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d570989-0486-3923-ab66-f2c8342bcbc2 | -1.2014 | -53.9184 | 2024-11-02 02:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a97eae6f-af3c-3d87-ab09-9769d4968b6b | -1.2014 | -53.8983 | 2024-11-02 02:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6ce1b46c-532d-3d1b-a26c-329ca313fe37 | -2.2568 | -50.4376 | 2024-11-02 02:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cfa778e0-153c-3a06-8342-6e9192c2eb03 | -2.2663 | -53.7422 | 2024-11-02 02:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c4bab49d-b42c-3630-a560-fa578736d1dc | -2.8386 | -52.8794 | 2024-11-02 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 98bc8f6a-6004-384c-a6f8-ed078c96ab44 | -3.0734 | -54.167 | 2024-11-02 02:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1645d1b9-4947-3e4c-ac75-b51d4208fe32 | -3.1097 | -54.2865 | 2024-11-02 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b2e85271-c015-3faa-bca1-53cad4de16e8 | -3.1098 | -54.2665 | 2024-11-02 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 05577736-4d6a-3fa5-b845-eb6b13bcb72c | -3.1281 | -54.266 | 2024-11-02 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3e08e978-64a1-31f1-8645-405415b6ad51 | -3.1282 | -54.2459 | 2024-11-02 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| be9b72be-c49c-38ec-a703-b6e23b643e4e | -3.1767 | -51.0812 | 2024-11-02 02:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bf2c0794-21ad-3170-a86c-7b72236a5bbe | -3.2207 | -45.2925 | 2024-11-02 02:35:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 02885099-0faa-3c93-82d9-7bd5e9f0794c | -3.2249 | -44.431 | 2024-11-02 02:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| cc9e9f7d-beb6-3d5c-b1cc-312d74a96faa | -3.2601 | -53.3557 | 2024-11-02 02:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1c25d8be-cf19-3131-8767-4ef35c23a42d | -3.7701 | -43.5554 | 2024-11-02 02:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ebffd72c-86ee-3844-bb92-828eb507fa0c | -3.9289 | -48.3458 | 2024-11-02 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 651154b5-32b6-311f-94cc-e8e1432f591c | -3.9473 | -48.3666 | 2024-11-02 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 14196ace-44d2-3db8-902f-da011a6ea4d6 | -3.9474 | -48.3451 | 2024-11-02 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6a7dbd05-cc9c-3f4f-a9e0-58776e877ea0 | -4.298 | -48.6309 | 2024-11-02 02:35:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| bc9f2202-d1a1-31cd-9d42-7256058ddaf0 | -4.4054 | -43.4746 | 2024-11-02 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8691bfc1-354d-3840-9485-ca12bccca666 | -4.3537 | -48.6068 | 2024-11-02 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e38eccd9-6d42-3f43-854d-98c8022e926d | -4.5575 | -43.1162 | 2024-11-02 02:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a182e98d-826c-34f2-9a4f-751699df9f36 | -4.5577 | -43.0928 | 2024-11-02 02:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e64699b1-5f1b-3e6a-9414-e6471d540435 | -4.9438 | -49.1564 | 2024-11-02 02:35:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 35c51882-87f4-334c-9f86-a5cc3ba765e8 | -1.2014 | -53.9184 | 2024-11-02 02:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3e826a11-110c-315e-96bc-a9f9f3e009ba | -1.2014 | -53.8983 | 2024-11-02 02:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 34d7aa05-630b-328f-8100-05574a142f0b | -2.2663 | -53.7422 | 2024-11-02 02:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1c391e0b-f7fb-3227-a674-d02494f0a723 | -2.8386 | -52.8794 | 2024-11-02 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c090da72-18e9-3264-91cb-77cb22570b24 | -3.0734 | -54.167 | 2024-11-02 02:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| be7f0d36-fb4c-3619-88b0-33885b652588 | -3.1281 | -54.266 | 2024-11-02 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| aebea062-8fa6-3eae-87b4-0ba75c473637 | -3.1282 | -54.2459 | 2024-11-02 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 72f4ca4c-ab97-3c22-a0e0-39a43ba8d4f5 | -3.1098 | -54.2665 | 2024-11-02 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4319be41-c0f6-3158-9e4f-129d2e4dab8c | -3.1097 | -54.2865 | 2024-11-02 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5d920923-97e7-3e7f-855f-e0e27997b7ab | -3.1767 | -51.0812 | 2024-11-02 02:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 03e493cd-e15e-354d-ae08-cfd942207a76 | -3.2021 | -45.2932 | 2024-11-02 02:45:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| eb518fdb-1c05-3d5d-a10f-b1ba8424e14b | -3.2205 | -45.315 | 2024-11-02 02:45:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 866a411e-c7e7-3e32-be28-988db053874d | -3.2207 | -45.2925 | 2024-11-02 02:45:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 147.1 |


[Clique aqui para ver as próximas entradas](README19.md)
