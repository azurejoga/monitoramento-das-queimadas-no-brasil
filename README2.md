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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dddb25e8-19ce-3e33-bab6-7064acf0b9c0 | -3.7703 | -43.5323 | 2024-11-02 00:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 302dd57b-c494-3b8c-aa56-48247c70376b | -3.7888 | -43.5545 | 2024-11-02 00:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b1abc6a5-3a75-3636-986c-832999068669 | -3.7372 | -46.0545 | 2024-11-02 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 34545962-88a1-321b-9a81-e6856a3e14b3 | -3.7373 | -46.0322 | 2024-11-02 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 42c5e3d6-cde9-3bdb-b41c-6aa45d831dc9 | -3.8144 | -48.9729 | 2024-11-02 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 33674dad-dcc8-3d1f-8cce-cd01afbd5112 | -3.833 | -48.9722 | 2024-11-02 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e732f294-7607-3e3d-93dd-9f3427fa1858 | -3.9473 | -48.3666 | 2024-11-02 00:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| da125e4f-6337-3509-ae01-286347995af7 | -3.9474 | -48.3451 | 2024-11-02 00:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7ef9c567-848a-3766-be6a-518fa1344160 | -4.3867 | -43.4757 | 2024-11-02 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7bfc7d28-bbc3-3692-ae65-ec148b7ba7d7 | -4.4054 | -43.4746 | 2024-11-02 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ed86168f-7aeb-3b78-9eda-891d092ad132 | -4.3537 | -48.6068 | 2024-11-02 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ffdd9247-745f-3b1f-ac91-448dea9dece6 | -4.4094 | -45.6416 | 2024-11-02 00:15:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 207fb052-50f7-3f11-95a1-770dbc426abb | -4.5575 | -43.1162 | 2024-11-02 00:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5578af29-e47e-35b5-a576-e55976ce7297 | -4.5577 | -43.0928 | 2024-11-02 00:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 230.8 |
| c347b2cc-c866-3e46-bd80-4d2fe7737303 | -4.5885 | -43.9956 | 2024-11-02 00:15:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1b5484c6-3b37-3bfb-a17b-28e29f2eba4a | -4.6072 | -43.9945 | 2024-11-02 00:15:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ca045278-aa69-3080-a00d-f04d33d84856 | -4.665 | -46.3862 | 2024-11-02 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dd93c53a-3959-3079-bf64-842a93207603 | -4.6837 | -46.3852 | 2024-11-02 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 1b92b119-ff6d-3bfa-baa8-f11f3d2ff8c5 | -4.8362 | -48.5832 | 2024-11-02 00:15:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| daa5db89-58d4-3b4f-9cc0-69328e071c4e | -5.1146 | -46.0264 | 2024-11-02 00:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4fcec6b7-39b4-3a76-9360-bda430644ef1 | -5.1882 | -46.1557 | 2024-11-02 00:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a2ccf024-1794-3e0e-aeff-ecb0e6ca995e | -5.3065 | -43.0663 | 2024-11-02 00:15:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 99131f1f-c96d-3979-b910-72a6a9990cb9 | -10.9808 | -45.1335 | 2024-11-02 00:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8449ab37-eb8c-37e0-a282-7d0904435088 | -10.9811 | -45.1104 | 2024-11-02 00:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3eedbdea-0299-3b50-9ae0-72dc91234b78 | -23.9717 | -54.0925 | 2024-11-02 00:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 18b6ac4a-e3a0-3d9e-b3c8-d42ee480ac52 | -23.9723 | -54.0702 | 2024-11-02 00:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 2fd008d4-8bdd-346e-92bb-50a24b99f40b | -23.9934 | -54.0659 | 2024-11-02 00:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| d377e1e8-1232-36d4-a757-bae3b2cf4b8b | -1.5531 | -52.2101 | 2024-11-02 00:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1e648a6f-f781-31c2-a43e-d6a96294142f | -1.5531 | -52.1896 | 2024-11-02 00:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a7ad2402-6847-3cc9-984e-da503657992e | -1.5715 | -52.1894 | 2024-11-02 00:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 16e0c7bf-8551-346a-aedc-26ea66e73fbf | -1.5899 | -52.1481 | 2024-11-02 00:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 94bdf8b7-c25a-34ab-ad03-82192f6ab3b1 | -2.195 | -46.4634 | 2024-11-02 00:25:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| e4a06f26-83d7-35b7-9000-0fd644309ff7 | -2.2568 | -50.4376 | 2024-11-02 00:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 26144b7e-00c6-377a-8fea-a00f79aaf68d | -2.2663 | -53.7422 | 2024-11-02 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| db9dd6d4-f4f7-3bbd-802f-a587e55c3d9c | -2.2847 | -53.7419 | 2024-11-02 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8af7c944-37f8-355e-a2d3-e026d4067494 | -2.6944 | -46.758 | 2024-11-02 00:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 707f0146-eaa0-3f03-8476-7482964e9c1b | -2.6759 | -46.7585 | 2024-11-02 00:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 8461fc8b-cf81-3a9d-991e-a003ec92ca2d | -2.8056 | -51.7539 | 2024-11-02 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 20938f10-ba62-3a5a-bae8-2070177b579c | -2.8386 | -52.8794 | 2024-11-02 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6eb77bdd-ff79-3c77-89c7-48084ab026b2 | -2.8509 | -49.3895 | 2024-11-02 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 90602ce3-b222-3e14-9bd7-0a8ecc84baf8 | -2.8555 | -53.3459 | 2024-11-02 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6461bf08-1d33-38a6-ba69-98b131dcd432 | -2.8808 | -51.3179 | 2024-11-02 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| de08d8de-bacd-3ab7-bee6-63fd0fc4c9e7 | -2.78 | -48.5806 | 2024-11-02 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| bdc40d54-3b8a-3759-9316-123421b66334 | -3.0088 | -51.5834 | 2024-11-02 00:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 92e89a24-847f-3e84-853b-f7230252cd32 | -3.055 | -54.1675 | 2024-11-02 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a2ada202-4870-36e3-8308-5c3d7be282fc | -3.0734 | -54.167 | 2024-11-02 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8d8ef6f1-4df2-3212-bcce-6c567d7744b4 | -3.1027 | -51.1249 | 2024-11-02 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0b572371-460c-3aed-a7e3-e1a0d4982ac7 | -3.1097 | -54.2865 | 2024-11-02 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f7fefb1d-269b-3d06-a957-e50823e3be01 | -3.1098 | -54.2665 | 2024-11-02 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b7ef618e-4cfe-3ac9-ba46-95a672cabe83 | -3.1281 | -54.266 | 2024-11-02 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| eb66e666-8bdc-3ebe-9f7a-999e23a4714e | -3.1282 | -54.2459 | 2024-11-02 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e8f3d8a8-9b1d-3fe8-b2e6-b4c4dff0667d | -3.1767 | -51.0812 | 2024-11-02 00:25:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fda8476d-fd48-3852-9272-b06d7b136018 | -3.2249 | -44.431 | 2024-11-02 00:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 158.9 |
| fab559fd-3714-330e-b9eb-a25abd757ca0 | -3.225 | -44.4081 | 2024-11-02 00:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 6684673c-0369-30cf-92ce-4a41eaf30e06 | -3.2719 | -50.3473 | 2024-11-02 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b48e8ad8-b50f-3d74-a715-3b3c7a51262f | -3.3461 | -50.2609 | 2024-11-02 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 33583200-f820-3c31-ae4e-3b37a540f10d | -3.3646 | -50.2603 | 2024-11-02 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 337c6333-3b72-35a1-a934-2ea8ff5ba5c3 | -3.4199 | -50.2795 | 2024-11-02 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ef6b7ec2-0e71-30f4-9e01-0829feb0eeb3 | -3.7701 | -43.5554 | 2024-11-02 00:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a1b0c6e7-d606-3431-9623-6598fe857ab4 | -3.7703 | -43.5323 | 2024-11-02 00:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a88959e6-da25-37ef-8b67-56f3612f6f02 | -3.7372 | -46.0545 | 2024-11-02 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 141.3 |
| aacd1a13-79f1-3dad-b687-89f6972ecda6 | -3.7373 | -46.0322 | 2024-11-02 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| aa819465-88d8-39e5-98b0-2f72bed38536 | -3.8144 | -48.9729 | 2024-11-02 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| baa4d611-f900-3d67-90bd-6503626d515f | -3.9473 | -48.3666 | 2024-11-02 00:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bc7c06af-7979-3a35-940d-e7188a5e6913 | -3.9474 | -48.3451 | 2024-11-02 00:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ee6686cc-4cda-3dbc-98a6-25035669d944 | -4.3867 | -43.4757 | 2024-11-02 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c29de66d-de90-3839-80b3-0add2ca235f3 | -4.4054 | -43.4746 | 2024-11-02 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| aa85f2a9-c724-3a76-b7eb-68d80a9da761 | -4.3537 | -48.6068 | 2024-11-02 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cf7e5956-f575-35d0-a32c-d4cee7890961 | -4.5575 | -43.1162 | 2024-11-02 00:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 395ef352-239a-36e0-9067-82d3e90b6d3e | -4.5577 | -43.0928 | 2024-11-02 00:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 167.7 |
| cc1b9a0b-2ae7-3fd5-9356-17db6217fc62 | -4.6072 | -43.9945 | 2024-11-02 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ed0b1ce1-5ba2-39a4-bf8a-a1a9067e64a5 | -4.665 | -46.3862 | 2024-11-02 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 45f69489-1297-385c-ab0c-1b456a0196ff | -4.6837 | -46.3852 | 2024-11-02 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 344eee55-8f9d-30f9-86c1-f6ee510158a8 | -4.8362 | -48.5832 | 2024-11-02 00:25:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ecf4cfd7-d187-39d0-92b5-9889a23b37e5 | -4.8363 | -48.5617 | 2024-11-02 00:25:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| bdfb6d4c-4c78-31fb-86c1-ae69c45ac9ec | -5.1146 | -46.0264 | 2024-11-02 00:25:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3015e462-0b32-3227-9510-eb3358aa1fc1 | -5.3065 | -43.0663 | 2024-11-02 00:25:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 76982737-be2d-3cb9-bff0-7643023726b1 | -5.3252 | -43.065 | 2024-11-02 00:25:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| aee3b1e7-ba8e-32ab-a571-5c824aabf9cd | -6.1302 | -47.2444 | 2024-11-02 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3391388d-b458-39c7-92cb-e4095db63698 | -6.1489 | -47.2431 | 2024-11-02 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2a698dbd-69ff-32bc-8126-80957d5959d2 | -6.5631 | -51.1126 | 2024-11-02 00:25:43 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| badf89e7-15b8-3db4-bd40-0925ea68cf98 | -8.0836 | -70.8676 | 2024-11-02 00:25:53 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 55cef68a-363e-3731-b958-e9133d7c06b2 | -10.9811 | -45.1104 | 2024-11-02 00:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 240925af-83a4-385a-bc7c-17e53d2a8794 | -23.9717 | -54.0925 | 2024-11-02 00:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 12cda018-9ac4-342b-b3c6-10ada663ac52 | -23.9723 | -54.0702 | 2024-11-02 00:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 5f7b954c-1e32-3c88-bd88-c74a01b9ad1d | -23.9934 | -54.0659 | 2024-11-02 00:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 55b75840-b9eb-32c6-b78a-b6d2829452ef | -1.5531 | -52.1896 | 2024-11-02 00:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0761baf9-7b91-3483-b70c-bb4fcd5f0bc1 | -1.5899 | -52.1481 | 2024-11-02 00:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 105c0050-d831-3b7f-8ad6-237c08189563 | -2.195 | -46.4634 | 2024-11-02 00:35:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8081eb04-cb82-32b6-95e3-bca41e686f5d | -2.2135 | -46.4629 | 2024-11-02 00:35:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f5001929-f3bc-34d7-b4d3-0335946c17ff | -2.2568 | -50.4376 | 2024-11-02 00:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4ab13e8c-46d4-3449-8894-76f79e9e3073 | -2.2663 | -53.7422 | 2024-11-02 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| cd347c14-17ac-3852-9c36-b69f67f7f5a9 | -2.2847 | -53.7419 | 2024-11-02 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| dad6ae25-b127-37af-87f8-aa0b8d305ec6 | -2.6759 | -46.7585 | 2024-11-02 00:35:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 58c39f05-365d-31f7-af07-9d50b7d8be12 | -2.8061 | -51.6095 | 2024-11-02 00:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 900fc055-27bd-3a2a-99cd-f766d6b30380 | -2.8386 | -52.8794 | 2024-11-02 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3dd7e8ae-cc5f-345f-a078-503f10f04fe6 | -2.78 | -48.5806 | 2024-11-02 00:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3d726db0-0f97-3206-aa14-5cda6f6ab40d | -2.8056 | -51.7539 | 2024-11-02 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8d2527e8-a897-32dd-a0ec-69aaabfe1a65 | -2.8555 | -53.3459 | 2024-11-02 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9587dc2f-86d0-332b-99de-249d62b3b333 | -2.8808 | -51.3179 | 2024-11-02 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README3.md)
