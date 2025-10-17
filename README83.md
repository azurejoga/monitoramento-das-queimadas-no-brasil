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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51e15d73-bfee-3186-9f5f-00bdf86a57a9 | -6.75083 | -42.36061 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b472297f-f415-36f0-886d-aa108a98fbbd | -6.07554 | -49.40215 | 2025-10-17 04:49:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97af96d5-231b-3e38-ba26-e4771a90d5cf | -5.22052 | -46.19356 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3be7e03-0bea-371a-abc3-5ff36051c683 | -5.2855 | -47.93059 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a39c4089-33c8-3b06-a9f6-a183396d7137 | -6.20857 | -41.75327 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b95833f5-17bf-3c1c-b9ee-b20fdf46632b | -5.02922 | -56.19486 | 2025-10-17 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfeb723e-9e74-326f-9a81-cb6d19c0d6ff | -5.39521 | -45.91364 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e72b799-5f50-3ad2-92f1-410d065b7c85 | -6.74509 | -46.99839 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cf40e37-15e0-3386-b339-71cdb77d20ca | -5.24431 | -50.96083 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44103d5f-1daf-359c-aac9-41a7111d14d6 | -7.74796 | -42.50841 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 540473fd-4b56-3dfe-8563-4fcae68c3de3 | -3.12974 | -50.20977 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 653bc0d5-bcd4-3cd5-993a-cbd11a4c65aa | -2.87629 | -50.72248 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47b200a2-3ce4-3b30-8d09-a4f3d55c2490 | -3.297 | -50.00976 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 360cff9b-1084-3bff-923b-30641cdd721c | -4.36879 | -48.71214 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd49725c-555b-3346-9e84-5f7884223d2a | -7.35364 | -43.85365 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e3f57dc1-7bb8-3ba1-8d09-2b475e7eb0b0 | -6.87693 | -44.70747 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 716df34e-60c4-38c8-9da4-c82a7bc4bad6 | -3.78303 | -49.43011 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3a5e23cf-95ce-33a7-8e28-3c1bedd8e72c | -5.71767 | -44.51617 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 467239a7-1ee2-36d1-98db-75bb81a4d748 | -7.98245 | -44.15689 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c27b5bde-54c2-3c72-aa86-5e96132e489e | -5.25796 | -44.20869 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81efd3f7-a3ab-3a41-abfc-710301f1d3d6 | -3.53387 | -54.17529 | 2025-10-17 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7825f23-c9b3-3897-94ac-528c2ba9a6a1 | -8.20811 | -43.96955 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa666c60-6de7-3dbf-b800-12264aeed235 | -3.28685 | -52.54753 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae3b2b5d-f24c-3554-a15d-eccd39c180c1 | -8.09682 | -44.98665 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965db2d4-a9f2-3a35-be1d-1dc227e86c41 | -7.43614 | -43.74979 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85644666-9770-3fc3-8803-bae13675e9c3 | -8.21958 | -43.99244 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eab2d57e-22c9-33a5-91e6-f4267f9293d8 | -3.84179 | -50.97403 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4016f82b-0a1a-3fd1-aafe-e6872bd78f93 | -3.97277 | -42.49115 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f809619e-15ac-399d-b2f8-360d7563a0be | -6.24413 | -41.54707 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22f767d2-776f-365b-a6ba-aac1ae215e38 | -4.01323 | -44.19081 | 2025-10-17 04:49:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ed69802-0d8f-3641-a116-26dc1d4eeff3 | -4.29914 | -48.0674 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a2de545-af64-3d58-9bdd-383bc232361c | -6.54741 | -43.92149 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8c6d65d-d298-3e27-9e4c-6f71c9c311f1 | -6.74439 | -44.37702 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65a829da-8871-3204-8a5c-9798450a69f8 | -8.23507 | -44.02098 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c454b882-9e57-3d56-b8e3-9a621ff2a814 | -7.46495 | -42.16293 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0fd3b5d1-bc4f-37dc-b31d-877aca58f688 | -7.86772 | -44.54182 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4704f16-ce3c-308b-b567-1bc773d7385a | -8.25752 | -44.03448 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| caae4bbc-35d7-3ca3-9526-05a0a3437cd8 | -7.35348 | -41.90707 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 991c4e6f-6846-3ddd-80ae-01c605e60dd2 | -6.75558 | -42.36486 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ed96a28c-c176-3337-a976-c2d9e3e50e1f | -3.32674 | -42.79331 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c40a9b0d-5a9c-3bd3-8762-3e4f4f128a7c | -5.61577 | -42.68019 | 2025-10-17 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0019eff0-4839-3c0b-bbb8-825996ca365b | -2.87296 | -50.72195 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20b1a68f-80a5-3f11-9889-abc8c615ce02 | -4.17203 | -42.31675 | 2025-10-17 04:49:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15c42828-1ffe-302f-8208-fdc186c73a79 | -5.14952 | -46.05686 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2a4f4a0-6f4b-3015-b5a0-4e5247923a06 | -2.86966 | -50.74275 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85c892af-09af-36cb-adf4-8b6c488d45f0 | -8.17646 | -44.02179 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d699e0a4-f634-3354-9fc8-8b713bfbc9b0 | -5.9042 | -44.74847 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7761dd51-1813-3174-9852-c323703e5f73 | -2.74805 | -49.39236 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 001f83b8-5c05-38e2-a980-d271ff5b5552 | -8.27711 | -43.36103 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5bdc451-8eeb-3d9b-9a69-f5d3b9b6bfc9 | -4.18504 | -48.92996 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4e5be4-d332-3eeb-87e6-0e5d9e0506fb | -6.53552 | -44.68679 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 975d97f8-319b-377b-acf5-33b397bc5953 | -7.20181 | -45.49191 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0c6d8f5-75d6-3a71-8d33-03433763926b | -4.13357 | -51.07326 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63d30431-66d0-391f-8f65-89f51053d218 | -3.84283 | -47.0679 | 2025-10-17 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9b3977-c545-30ea-87cd-5bf08914960b | -7.1709 | -42.36852 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6baa2a81-66ab-3f51-8517-525723e6158e | -3.98187 | -42.49827 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e61da684-27d1-37f1-9e84-bb1f38152b0f | -4.61255 | -50.82547 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1293d296-c4c1-3a80-855d-696bb97e589c | -6.20314 | -41.75254 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f682a324-3b9b-36e8-b0d0-6703cd10131a | -3.86585 | -50.04891 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6ed9e13-31fd-3f23-afb6-84264e9df6b2 | -6.98746 | -39.23103 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9581c7ec-514b-3fef-b7be-87ec57de23a2 | -3.234 | -45.97138 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8182fa45-34d7-3b16-ab95-27d99479c846 | -8.19707 | -43.31882 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| ecfe6dc8-445c-32e4-8564-838a859ed88b | -8.24538 | -44.01711 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 690bc55e-80cf-3a10-9a63-8c21f2d1aabe | -7.4677 | -42.14261 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2347ce3e-cb76-3043-bda6-bb6826b6a49c | -3.35173 | -49.94379 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba42377a-ba2c-3480-a9e0-eca887f1861f | -2.70741 | -49.41116 | 2025-10-17 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9a2dced-eb65-31d2-b2d4-62fd91b3e45d | -7.48498 | -47.0336 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a98083ad-efa3-3cb1-ae6d-82575cf96771 | -7.56853 | -47.14074 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1788d5ce-8621-36d3-92ae-c794d9369463 | -7.32993 | -44.15751 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de896934-083b-33c3-a770-3424f7c6c259 | -6.37782 | -41.47665 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05898a4d-6a1a-399d-8e3f-52724f44b023 | -8.21365 | -43.30996 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 04b3fa71-e1d9-3fab-b6e2-3d8a11e2c66f | -4.87844 | -45.93962 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 104d6669-0aa4-32b2-a65c-9e3e7e6bcb62 | -7.46186 | -42.14526 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa1898bc-d945-3261-9b34-d8b7b185b749 | -6.0057 | -43.1169 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3ae02028-4058-3259-b45e-03a91ad155f4 | -5.85031 | -43.88394 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdc490f8-b427-36cc-903e-4d9c5647b741 | -6.68872 | -44.2769 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c4218e-3a4c-376d-8817-3119a50515fd | -7.45853 | -42.67646 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ece1a05-fc70-3e81-b374-55155ae2b85e | -4.83638 | -42.75595 | 2025-10-17 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c15f4dc8-4c56-3dea-974b-3db1dc767004 | -7.17155 | -46.93765 | 2025-10-17 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e88a0822-85ac-367f-9a23-5e017d8c38ca | -6.93484 | -45.1354 | 2025-10-17 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10ca89af-4b77-3db3-ba82-36518d789e99 | -5.867 | -41.23418 | 2025-10-17 04:49:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8ac5551-ede0-3192-9711-52c08da9df4c | -3.63527 | -51.81797 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc1dd471-63ff-3425-b9fb-430013bb546a | -4.93541 | -47.07758 | 2025-10-17 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c97012b-aa63-36a4-b6c6-0a471b511bfa | -8.16777 | -43.3087 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e13e0020-68c6-3d4a-8c6a-9d62246cb07b | -3.65675 | -51.32735 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2b349f4-8b4b-3a45-be85-5d5d00600f51 | -5.77504 | -49.80673 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c63498c-c745-3372-a25e-1016ce13a936 | -6.03681 | -41.90454 | 2025-10-17 04:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66f49a94-374b-31e2-ba2a-9020eaa39ebc | -3.82843 | -52.40081 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93f72476-dd5b-3235-882e-51a1c0ab2828 | -1.38234 | -55.37085 | 2025-10-17 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a5475a7-dba1-3db5-8578-ac769e3c6267 | -3.51568 | -52.49403 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f831ec21-f606-3675-b7f2-60bca9a2b178 | -2.70849 | -49.86036 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35dc0ccd-39b9-3c6f-ac8a-8839a49e79c7 | -7.20664 | -45.48852 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd9d755f-cd82-3a2d-967c-4d9e94926bac | -5.15589 | -44.56985 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19d654ae-f8ca-3ba7-a9e9-eff705e72ae6 | -5.9691 | -44.0349 | 2025-10-17 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a59f1f5-b68e-3997-b7ab-c91c06c4bdd6 | -6.42374 | -44.03796 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 529f9f7b-7c6f-31c4-8cac-ed0ba6a2cdbf | -7.46985 | -42.16712 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d721bbbe-316d-3bcc-b6c0-3cea3525207d | -5.88414 | -44.76255 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85331f5b-826f-307b-a2b2-4840bca93c3f | -2.74136 | -49.39132 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 55cbc3a9-1dcf-3121-b73d-080f2c27755e | -2.87354 | -50.7398 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c2c268-8c8a-3067-866b-84442d8ac29d | -6.13195 | -41.74783 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README84.md)
