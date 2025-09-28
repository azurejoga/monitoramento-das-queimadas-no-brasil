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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ee79ec8-719f-36f4-a81e-5bfbce00baab | -18.0453 | -51.1556 | 2025-09-28 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 319.8 |
| 8eddc060-d9bb-397f-85ee-ea7a5f2c2341 | -7.7787 | -47.0036 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| dbc235ca-08f8-31f8-8af2-0f10c953b92a | -11.0083 | -57.0658 | 2025-09-28 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9d4023af-1dad-3b8f-9237-b070c5f5a47d | -14.7856 | -45.6586 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 999abeee-75dc-330e-be19-7db66e04c94c | -18.0648 | -51.1742 | 2025-09-28 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 3ca3ca49-f16a-3edb-80b1-675a54d73280 | -18.0448 | -51.1777 | 2025-09-28 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 7f786733-0ea6-32f7-86ac-ff53f391d027 | -14.765 | -45.7086 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a8bc9a1a-c53a-3e1d-afed-5a063e9b9a0a | -9.6512 | -62.8336 | 2025-09-28 01:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 103.4 |
| b957da75-9adf-3972-aae1-0ddb27f1fa72 | -8.483 | -47.7983 | 2025-09-28 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| bc2f8b52-a276-3804-b685-1ee550815208 | -7.7602 | -46.9831 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ae5d9641-ddd4-36b0-acd0-bbb1cdbc387b | -9.077 | -45.5292 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 360.6 |
| b72e6b6a-27e6-3522-889b-d3283d167fa6 | -7.7787 | -47.0036 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6ff9d8dc-478e-3351-a770-678ae3c1f452 | -14.7846 | -45.7051 | 2025-09-28 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 901d6647-3190-3213-8c1a-ec52ef88142f | -18.0448 | -51.1777 | 2025-09-28 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 214.5 |
| bddb9940-ef1e-3328-aa73-a671d714c443 | -7.7975 | -47.0019 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 78520614-1bb8-3651-81f1-9f2fea9e6349 | -9.0766 | -45.5519 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 1d7c4ce7-7802-3d56-adfe-334c8f9b9a78 | -14.7851 | -45.6818 | 2025-09-28 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 4fd1f658-38c9-3e0d-ba72-ff3cce71e48a | -6.7782 | -44.0876 | 2025-09-28 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f7f912eb-0a19-325c-96b3-22e81137a99b | -6.1252 | -41.8175 | 2025-09-28 01:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| d8d71be9-2ae8-3a74-918c-bbfa3371cd63 | -14.7655 | -45.6854 | 2025-09-28 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 636811e1-5dbb-3541-a505-93721a77d809 | -9.0577 | -45.554 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 21264ae4-1a89-3e49-b080-f7252c238a91 | -18.0254 | -51.1591 | 2025-09-28 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8491a011-9680-3b30-8b76-5540196706dd | -5.4554 | -41.0782 | 2025-09-28 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 9bd06b29-a482-3e34-8dd8-fadc5acf0f10 | -5.8149 | -42.8167 | 2025-09-28 01:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 63fd749c-b024-3cf2-835c-f2f5067b68c3 | -9.0773 | -45.5064 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 91634957-20bd-3450-ad01-93185986692d | -5.4742 | -41.0767 | 2025-09-28 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 1598cab1-c74e-3058-b667-88037f32dbbd | -6.1254 | -41.7935 | 2025-09-28 01:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| abecbc28-d019-318c-9c26-8fa14141fd92 | -11.9828 | -47.9976 | 2025-09-28 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2675696c-a589-3144-a7fc-2abd48698874 | -9.058 | -45.5313 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 361.8 |
| e2cd2685-db4d-3ab3-848e-e390ebb1b768 | -7.7785 | -47.0258 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| daaa9e52-836f-32c9-ac0c-a36218d68022 | -14.7856 | -45.6586 | 2025-09-28 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 39ce3441-4c4e-3e6c-a04c-630a3b66c2ec | -7.7599 | -47.0053 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f41d3972-536c-3b55-836d-6f1f5ef4d1be | -14.7861 | -45.6353 | 2025-09-28 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 42c743fb-5159-3d60-8948-0cd0c5e8a65e | -10.9894 | -57.0672 | 2025-09-28 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4262af0e-d1f3-3726-b0c7-b4277b12196d | -6.4319 | -43.0707 | 2025-09-28 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 2e97ee72-8bc2-35db-b533-f3d2609dd119 | -16.9667 | -53.6975 | 2025-09-28 01:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3b2442e5-4e95-33d5-92ce-939418ee73bd | -5.8187 | -44.4413 | 2025-09-28 01:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a7e304ea-f139-3313-8e30-381493878096 | -18.0653 | -51.1522 | 2025-09-28 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| d1fe9ea5-6d91-31e4-bdd2-000f1e9c3bc5 | -18.0453 | -51.1556 | 2025-09-28 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 303.9 |
| efb6bd19-fe46-3301-ace8-34ab1f925976 | -9.6511 | -62.8526 | 2025-09-28 01:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| aecbd0f8-90ee-3563-a9a5-0d65058de207 | -11.9846 | -47.8865 | 2025-09-28 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ce2cddfb-e7f9-3b2b-af92-e86ea3910189 | -9.0583 | -45.5085 | 2025-09-28 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6ba0603b-7d83-396b-9dc1-8d86b2565ae1 | -7.7412 | -47.007 | 2025-09-28 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 92d899b6-a0e4-3fee-ac47-fcaee30af0f5 | -2.5772 | -48.4146 | 2025-09-28 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6665dad3-7d30-3b04-954a-05932d565898 | -12.0038 | -47.884 | 2025-09-28 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5ce3ece7-8b66-3894-aae3-e3e11969a318 | -18.0254 | -51.1591 | 2025-09-28 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c8a58dd7-6f58-3132-bbd2-0f9b55151d34 | -9.6511 | -62.8526 | 2025-09-28 01:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| a4584af7-df17-35b9-b1a3-53e55f806e60 | -7.7787 | -47.0036 | 2025-09-28 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3dbc89b6-e42e-3be4-a69f-e0c83ea6c3dc | -14.7861 | -45.6353 | 2025-09-28 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 24fd7452-8aad-3fec-8bfd-e1e7401b46f2 | -9.058 | -45.5313 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 2a4edf37-77c1-395a-a06c-ca7907182a00 | -14.7851 | -45.6818 | 2025-09-28 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a656fcbf-00ad-397c-aa66-bd1cbba885de | -9.0577 | -45.554 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 0e80ebe7-659b-3766-88e0-c6a387a0a8c7 | -7.7412 | -47.007 | 2025-09-28 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 78ed7e48-78e1-3716-8d84-7c2195719be7 | -7.7555 | -45.7324 | 2025-09-28 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| ae54dcdc-c5a8-3d56-bb07-ca9752084ed1 | -5.8149 | -42.8167 | 2025-09-28 01:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 2082cdc9-97b1-34ba-a527-d29207a490d2 | -16.9667 | -53.6975 | 2025-09-28 01:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0e3481cb-150d-3015-889b-de78bf876581 | -17.7338 | -46.7056 | 2025-09-28 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6fc50b30-287a-36c1-ba6c-c12ec65217af | -9.0583 | -45.5085 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ef128ab4-8621-3852-99ad-254d60dbb580 | -18.0448 | -51.1777 | 2025-09-28 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 168.3 |
| d1925878-9c41-3c38-9dae-8cad3aa87985 | -14.7856 | -45.6586 | 2025-09-28 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| cb61e2bb-002d-33c8-b778-69f70930a755 | -11.9846 | -47.8865 | 2025-09-28 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| fb719c9e-84e4-3c59-804f-1f3933bf2aa1 | -7.7975 | -47.0019 | 2025-09-28 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 225f5113-d4b7-3f92-8430-b0904fc7e95e | -18.0458 | -51.1336 | 2025-09-28 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0fd96ba5-a9ea-3262-bd24-59dbeaad6269 | -7.3847 | -47.0378 | 2025-09-28 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6933ab36-90ee-36ce-b5bc-a3d623c528c6 | -18.0453 | -51.1556 | 2025-09-28 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 284.4 |
| ce4b7848-46c9-32c7-abaf-ee54153aff3c | -14.7846 | -45.7051 | 2025-09-28 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c2215229-eaee-3ced-9c41-48a1b1298866 | -18.0259 | -51.1371 | 2025-09-28 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9843c9fa-a304-369b-a561-4836a2ce1110 | -10.9894 | -57.0672 | 2025-09-28 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| ac6ac5fc-2a6b-39b3-a906-37ce0d187044 | -11.9828 | -47.9976 | 2025-09-28 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2a7d8a16-355f-34cf-a5d7-917a20ec7404 | -9.077 | -45.5292 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 449.5 |
| 40cd04c6-5163-3655-9501-3c3137a9393b | -9.0773 | -45.5064 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 38d49f49-225c-3764-9b21-4f8d791456ce | -9.0766 | -45.5519 | 2025-09-28 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 235.4 |
| e7783351-62aa-3e6e-a12d-ac06c5289151 | -9.6512 | -62.8336 | 2025-09-28 01:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| fa50f902-6651-33b8-8e73-896f69888a16 | -5.7396 | -42.8461 | 2025-09-28 01:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 24c9a5a0-96d0-31d0-9907-653516bf5472 | -7.7599 | -47.0053 | 2025-09-28 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ec553014-29fd-330c-af9c-e1c0b49b89ed | -18.0448 | -51.1777 | 2025-09-28 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 32300320-2e58-3455-850d-5cf4bef0cfe7 | -7.7412 | -47.007 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f6c21639-bc34-3903-b883-274585ae8165 | -9.6511 | -62.8526 | 2025-09-28 01:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f14b5d02-954c-3df4-a61b-b5b3b933dfbf | -18.0458 | -51.1336 | 2025-09-28 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 12d2b09f-b8f5-3e2c-9cb6-c3075b7574d9 | -5.3057 | -43.1599 | 2025-09-28 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 502a2ee3-b8fa-3f03-adcd-822152a15462 | -9.058 | -45.5313 | 2025-09-28 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| a255051d-7477-3de0-b29c-47ba91370c49 | -14.8242 | -45.6747 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 865bbc81-f73d-3384-8ba7-e96f8fa7040e | -7.3847 | -47.0378 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e887ddcb-171f-3220-a8eb-e79f8a25fb42 | -9.077 | -45.5292 | 2025-09-28 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 8dd1831e-3bbf-30c7-8c92-22723219467b | -5.8187 | -44.4413 | 2025-09-28 01:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| f761e0ef-b3ef-3dfc-8a01-4478b9368edc | -14.7655 | -45.6854 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 03533310-b4cf-3bf9-86c0-8037847c3192 | -18.0259 | -51.1371 | 2025-09-28 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9f6306ee-a664-3e9b-8cf2-c6c63bc802e5 | -7.7599 | -47.0053 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 740e2f49-b5a2-3e52-a4a5-de46ef688db1 | -16.9667 | -53.6975 | 2025-09-28 01:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| dac14c54-bbbd-399a-add8-ef3833f3e0ac | -14.7851 | -45.6818 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5bfe1389-4dc3-301a-b3da-d3518d897d05 | -14.7856 | -45.6586 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 056561ea-8b17-3560-afca-af9f88aac5df | -14.766 | -45.6621 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8c91e438-6771-39c1-83cb-6c419606ef5b | -12.0038 | -47.884 | 2025-09-28 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 97580a2d-ce20-389c-8970-25986d7de218 | -5.8149 | -42.8167 | 2025-09-28 01:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| c6adaba8-490f-36da-a972-f8c4970ca7b7 | -5.7396 | -42.8461 | 2025-09-28 01:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 6d12c215-81dc-3bae-8f3f-dc8a30b52782 | -5.8374 | -44.4399 | 2025-09-28 01:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0a380473-26b0-3246-aca9-babb7e123f54 | -18.0254 | -51.1591 | 2025-09-28 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c2d39d1d-35a6-397f-a43b-5f24b1a2cd86 | -7.7972 | -47.0241 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fc8c16c8-782c-3886-a074-cbb968ffa11e | -18.0453 | -51.1556 | 2025-09-28 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 35c96f51-1627-3e05-b185-a8fab9170802 | -9.0583 | -45.5085 | 2025-09-28 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |


[Clique aqui para ver as próximas entradas](README8.md)
