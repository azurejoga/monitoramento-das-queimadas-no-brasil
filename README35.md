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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 473daec5-5b73-38b9-9c60-86cd3c3bbcc9 | -1.67674 | -48.46445 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b254c268-e41c-3bbe-8067-fb3a6efdf7fe | -4.01431 | -46.53871 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2a12426-33d8-392b-bf8a-ea443d7a85b4 | -5.33337 | -40.89906 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 82a7cb4b-3b44-340d-8261-8d34b196e90e | -3.78887 | -50.10514 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df15cd3d-0670-3266-9b8b-ce4ab1d2731a | -2.11338 | -48.27482 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b527d33f-2a42-3614-a349-761d0875ec19 | -3.19773 | -45.55585 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2dcdf1c7-38b6-3b22-af23-56da09a33cfd | -3.96801 | -46.70129 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1ee93e2-3aff-3f3a-bc61-13fe02a12c76 | -3.99166 | -45.86438 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9482500-21b6-3dbd-9f16-552378af8af2 | -3.61274 | -44.7882 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6346062b-b69c-3c5a-91c0-077addbe4597 | -2.55271 | -54.03586 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cad88212-a55e-30dc-b7a1-2ce9d556d49a | -2.20673 | -46.04376 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f644184b-e87d-3d6b-bf39-9d7aae6009f9 | -2.91935 | -40.30799 | 2024-11-16 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85ac6054-4eb2-32f3-9f7d-792c6d8bf075 | -4.80196 | -43.21859 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 261bf521-93ba-3798-af56-77cf173244e9 | -3.95346 | -46.70625 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47eb1814-5ab9-3865-841d-ab89eeb77455 | -2.23215 | -53.60815 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 124f58bd-88e9-3d5e-adb5-892077dc4697 | -2.63478 | -46.52227 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a6bcb50-8378-3dd6-8be4-1bc78bac7b97 | -3.94675 | -46.70517 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 089dab1a-9e95-3a30-9a2c-2b45babc7f6f | -3.7913 | -43.91301 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f5dfd75-0a94-315b-a14e-24b4d7853572 | -4.22274 | -46.81704 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7325280-4c06-3993-9e76-1733bcb08d6d | -3.01789 | -47.97935 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fedcb064-7dad-3d7d-936d-5e1206aa1264 | -5.67127 | -35.64375 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 8f0332cb-387e-33ae-9410-5f86e0f965c6 | -3.92525 | -45.85399 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5cfc287-520c-3f45-a646-329f48cdd507 | -2.15399 | -50.52034 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f1440c3-8916-3265-bdfa-e3cfc6a5f260 | -2.67188 | -46.18832 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01377e7e-ffa4-348b-98d8-e74752983ba6 | -3.94909 | -46.40994 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aff8425a-64d3-3ca6-8daf-c649252caa9a | -4.10331 | -46.11996 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ffe7a71-9b88-3c1e-9309-bca34e872d72 | -2.8959 | -45.34661 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9d80846-7d68-3e7f-981b-ff5f1bd61887 | -3.76489 | -50.78253 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 694203c6-ef64-38ae-a787-6bdffb79832f | -2.63763 | -45.97199 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7c61556-6ccb-3a47-ae2b-85ba804bf1e7 | -3.4521 | -40.97058 | 2024-11-16 04:23:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c79ecd4f-994b-3026-8390-fca55c7af4f6 | -4.76433 | -43.60318 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea2fe72-c23a-3a51-9644-02eca67c245a | -3.78279 | -46.67546 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e08bd12-50d7-3272-8554-be6396c34f29 | -2.1425 | -46.55891 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8d12a84a-1ebb-33b4-880a-25d7f95f14c6 | -3.75527 | -44.74203 | 2024-11-16 04:23:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbb40301-a5c9-3fee-a596-6253a4fb0396 | -3.54621 | -51.58833 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ab154f-73e9-3ffe-a259-8b0a5f3ccf68 | -3.06851 | -45.34514 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8239aad5-e867-3cd1-9331-3a59af203b05 | -3.98239 | -43.71717 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50d452f2-5417-3f7e-bfa1-dcc8c5a35df7 | -1.08758 | -53.17933 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0856cf48-7d06-384a-ac6d-06898baeb5d6 | -3.76843 | -50.78676 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563afc4e-972c-386c-b038-3c3fcc543bc0 | -3.57562 | -50.51324 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4fe8d94-d8ab-3cbd-97ff-9d31152e7d0d | -2.18907 | -48.38787 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d81ca4ee-faf8-316f-986d-cfd9635a7103 | -3.29742 | -44.1702 | 2024-11-16 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| befbdf91-82f9-3fcc-a489-a5bf317c7b09 | -5.33391 | -40.89534 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2f019e0-ce2b-350e-9c37-35e6e6a4536d | -2.62763 | -47.91618 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92a93c9b-14a2-3e07-afb3-25c13a67ba89 | -3.03492 | -47.98608 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5661b00-92a5-3218-a6df-e4edf416983b | -3.88013 | -45.02222 | 2024-11-16 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| f8698256-ab9f-3404-9581-36fdb1138760 | -3.27956 | -45.50916 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43efe805-4f95-32cd-b607-eecff83c2541 | -5.14595 | -37.69909 | 2024-11-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4715d475-db47-301f-9776-327c55d9079a | -2.79527 | -46.64931 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfeb1fdd-8cf7-370c-be48-172877868f11 | -3.28234 | -45.51313 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbc11277-8b4d-39f2-9970-cd9b1274a08c | -3.15896 | -46.60736 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cd3e40f-0b7f-342b-a5a3-b38092ff7d1b | -3.49898 | -47.21023 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1edc92b-01d2-3f64-8636-2e28acf96515 | -2.62805 | -46.52122 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62566615-15a1-3c2e-8288-ae31bc55b1ec | -4.01821 | -46.53572 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1127fa6-b83a-3cac-88c1-c135ec2ecb45 | -2.66964 | -46.18078 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c68daf1-2dcb-31b4-b0bd-71f72798fd7f | -4.01586 | -44.58487 | 2024-11-16 04:23:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1f4efe6-c56f-3af1-9359-04fedf891c1a | -6.82468 | -46.77823 | 2024-11-16 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7b371f-a6aa-3bf0-b01f-3bd717072f64 | -6.92337 | -47.83965 | 2024-11-16 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 688012c4-0eda-31dc-ac7f-7cf5abac251a | -4.95761 | -49.50328 | 2024-11-16 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0551239b-a621-30de-b92c-6a9ff21f843c | -5.89706 | -46.24976 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c33b53f6-ba5a-3e98-b667-aad6bc7db041 | -5.87303 | -42.2771 | 2024-11-16 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b189571d-530b-3056-b110-624512530964 | -0.96868 | -46.93592 | 2024-11-16 04:25:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69931599-c0f1-3cdc-8350-1199e0b368fc | -6.27233 | -44.54636 | 2024-11-16 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ec8829b-676e-3ca3-908d-329d2e66306f | 0.15884 | -51.13664 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5b4c8a0-c4cb-321f-835f-86c1f85f1f25 | -7.4017 | -40.39122 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 06b3d24d-65fa-3374-8466-6b91f458b3d9 | -7.06872 | -46.75605 | 2024-11-16 04:25:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77d85b41-f533-3e07-b1a1-851e1ba75140 | -6.04103 | -44.0357 | 2024-11-16 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f86373ff-6749-360d-990e-985454869e89 | -6.26981 | -44.96853 | 2024-11-16 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22dcd6ca-4ebd-3667-8df8-4c7bead5cd3c | -10.38863 | -44.87636 | 2024-11-16 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a00c0ad-4fcc-34bb-80e7-ea096e57b98e | -6.02498 | -48.03929 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1ee2f50-12c3-3c38-9db2-9341aa3d4d93 | -4.38822 | -50.82788 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5906fb93-ca32-31a9-876a-a1428fdf42d8 | -5.78948 | -48.1577 | 2024-11-16 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 700eff93-bae3-37e8-a25d-d0fefb267b90 | -0.96809 | -46.93967 | 2024-11-16 04:25:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43864758-8db7-3d60-b8cb-3ced973b61cf | -0.25804 | -48.51612 | 2024-11-16 04:25:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 023747d7-d5cd-3e60-a38a-4c855b63749d | -5.97728 | -45.37017 | 2024-11-16 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 057146a3-5db7-3d6c-aee1-25bb5316118e | -4.36085 | -50.81616 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c1ebe3f-0e5a-3b48-97a9-318391a90e65 | -10.83264 | -44.4607 | 2024-11-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f682e6ba-267c-3079-82f2-ddda9077f540 | -6.02215 | -48.03499 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 80500af5-4cde-3295-b2e1-4d82ca26c632 | -7.81524 | -48.62967 | 2024-11-16 04:25:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb1d4fdb-cb44-3f9a-a4be-d2543c7becb4 | -5.95343 | -44.464 | 2024-11-16 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24a25fc9-40f3-35f1-8f2a-532ff23a1068 | -7.49755 | -47.35701 | 2024-11-16 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efc81b71-c3d3-3bf0-ab75-d9d5a03c6712 | 0.15955 | -51.14105 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bd97b1d-2b2b-3e12-b4bb-4597f549d7bd | 0.05046 | -49.52613 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f37c28a-1f33-3414-9400-40759b119209 | -9.12113 | -44.42384 | 2024-11-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca608d00-905e-3fb4-a504-da6a87db04e6 | -7.40052 | -40.39939 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| be9decdf-5b89-30f3-a562-3b40d7c28646 | 0.81998 | -51.13772 | 2024-11-16 04:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f8d2321-6b31-3877-be7e-6629923225e6 | -7.25058 | -46.7816 | 2024-11-16 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 445d958f-7845-3273-8374-ca95c3ef3cb4 | -7.25003 | -46.78508 | 2024-11-16 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a16813f6-a120-385c-a2d3-b5cc5baf467f | -6.02619 | -48.03181 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 22451e1a-4289-3506-b217-ac722d3f3f49 | -8.28738 | -45.97821 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5e3e370-609b-3a02-b743-dc4e8534bf5f | -0.3874 | -50.01566 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e834d86f-a055-327b-a21c-9b1ad67f4930 | -6.17147 | -41.1686 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 56dc055d-9cbd-39e2-b1a5-add1c1fb8caa | -5.93575 | -45.57069 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e95f258-f309-375d-ae11-596d9cd4d653 | -5.90697 | -46.23002 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a76bf1b-8ad9-3bb2-9ccd-b87e0f1b48e3 | -8.28405 | -45.97768 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d3eb30c-991d-3d21-9cae-79b993cf61df | -5.90311 | -46.23296 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc67a3bb-d95f-3eb2-a21f-735282ec6d37 | -11.80085 | -47.06419 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3189604f-b8f4-3ba9-9cbd-58a23e6e99fd | -9.11821 | -44.41945 | 2024-11-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f6985f4-9835-34fa-bb73-0c73fc9f6881 | -8.28126 | -45.97366 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1c7c9b6-a625-32b0-adbd-bb0deb50e028 | -6.02559 | -48.03555 | 2024-11-16 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README36.md)
