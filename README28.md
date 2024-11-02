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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89cf254a-3283-35c6-a096-4d64202d1ebe | -3.91112 | -48.93451 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9273af15-b153-34e8-8f1c-c015dc452cd5 | -3.90541 | -48.92729 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30fd0bf6-3799-30a5-acd0-e89283326e1a | -3.82499 | -48.98207 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d027755b-cb41-3983-9f7e-79cf2387d321 | -3.82199 | -48.88775 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d1dcd7b-2cb5-33f1-9b19-a646b1fdf2a0 | -3.82049 | -48.97415 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b92cb11-1bfe-3aaa-b28f-7f18083e09d1 | -3.82022 | -48.88807 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f77f1fdd-d7c6-3a88-8fe4-5667b7e86ac8 | -3.8194 | -48.98029 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28fd8870-3276-3f81-83db-1c17ac92c3b5 | -3.81927 | -48.97468 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4067c033-e2c2-34c0-9aad-02e8db3bf189 | -3.81822 | -48.9808 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d574ecd-149d-3947-b7d2-eb7b39030a02 | -3.81522 | -48.88673 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4daac40-f43d-302d-94ee-cdff99ffddb9 | -4.93623 | -49.15534 | 2024-11-02 03:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b2622e3-9c24-3070-aebe-1e65b5dbb3f3 | -4.93422 | -49.15373 | 2024-11-02 03:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 58ac5520-c228-386b-9dfc-99ae2f46c87f | -4.93415 | -48.51567 | 2024-11-02 03:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0899afe8-1f12-3663-bd93-4572c8a4261e | -4.92951 | -49.15405 | 2024-11-02 03:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a4eb6d5-1378-3dea-83a5-058d0da33592 | -4.9251 | -48.6338 | 2024-11-02 03:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43d75b6f-fc67-346e-ade8-666f6c610250 | -4.88309 | -48.4262 | 2024-11-02 03:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47fd3514-39f6-3521-bca1-ed543f48084b | -4.84359 | -48.57656 | 2024-11-02 03:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e313c2cc-cd9f-32d9-8bc2-b5f4ee19ffe8 | -4.84352 | -48.57246 | 2024-11-02 03:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5fb766ca-f7b7-3f87-98df-dfc720a63624 | -4.84257 | -48.57774 | 2024-11-02 03:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5cb4c54e-f3fb-3659-8d3a-39374ce721d9 | -5.23024 | -48.08102 | 2024-11-02 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f61654c-c2dd-373b-84b5-9ff0f11a3526 | -5.22936 | -48.08603 | 2024-11-02 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6a1a29-5066-3906-8b45-eeb524cc7811 | -4.38532 | -49.42088 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df58498b-d9f5-352a-945a-c0edcb6aa5a9 | -4.38462 | -49.41942 | 2024-11-02 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29c51a80-94b9-34e6-92a0-5530ceb6e65e | -3.70139 | -50.14865 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cf29badd-d6d2-3a73-aaaf-64af07d71631 | -3.7001 | -50.14908 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b5f1147-1e7d-3e2d-8a90-15d838f740ef | -3.70004 | -50.15613 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9e620e38-5c1d-31d0-89ac-eabe5215448a | -3.6988 | -50.15652 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e17eeb51-b98b-3b68-b495-e6874abbc5ab | -3.69411 | -50.14754 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b4dacee-331c-371d-84ac-fff9edd4c13c | -3.69281 | -50.15469 | 2024-11-02 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7291b86-8b10-344e-86ed-88dffb7ec24f | -4.80488 | -49.48689 | 2024-11-02 03:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dcff249-3ddb-3ce6-a565-f87a77cb290e | -4.79806 | -49.48534 | 2024-11-02 03:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bfbc883-5dea-330c-9beb-c19a5c2ed2be | -4.71202 | -49.60862 | 2024-11-02 03:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7bcf028-adf4-31b4-9bae-309b35139710 | -4.7051 | -49.6073 | 2024-11-02 03:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df5a406-412a-3274-9113-7abec2803a2c | -5.22958 | -43.48244 | 2024-11-02 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94135095-9c7c-378a-9243-dfa10b1ec04f | -23.6091 | -46.83673 | 2024-11-02 03:51:00 | NPP-375D | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0afab52-016a-39cb-81ed-455828962cd0 | -23.58397 | -47.03186 | 2024-11-02 03:51:00 | NPP-375D | VARGEM GRANDE PAULISTA | SÃO PAULO | Brasil | 3556453 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce01c88e-c594-3d64-a676-006de93e5a29 | -20.70275 | -41.71862 | 2024-11-02 03:51:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29eaf828-2943-3e62-b4a0-8f3ca3ce31cc | -21.65938 | -42.10901 | 2024-11-02 03:51:00 | NPP-375D | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3318bf66-c151-3d68-b2c7-b3a1dbb0a97c | -21.65873 | -42.11292 | 2024-11-02 03:51:00 | NPP-375D | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b05dab83-cf82-3bc9-b9a6-daaccd8e6456 | -21.65596 | -42.10843 | 2024-11-02 03:51:00 | NPP-375D | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 783d3d1a-cbb3-389a-84b3-b18e77e1cfc7 | -21.65529 | -42.11238 | 2024-11-02 03:51:00 | NPP-375D | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2cbd1e5-1327-3d75-b4c4-184f295adbb1 | -22.57608 | -42.16947 | 2024-11-02 03:51:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43c4e813-ca55-31b0-a8b1-0aa4290874df | -21.62491 | -43.46869 | 2024-11-02 03:51:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2515940c-ac2d-3520-9515-fdc70c12f5b5 | -22.85726 | -42.98104 | 2024-11-02 03:51:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bb7cbe01-1ee4-354b-b5da-6444a74312be | -20.97261 | -46.2951 | 2024-11-02 03:51:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c6ec504-5757-31db-9681-dd133b34f9c6 | -20.94934 | -46.99133 | 2024-11-02 03:51:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 540a1dcd-c8a0-3057-bb00-b800c9c76431 | -20.42604 | -47.45826 | 2024-11-02 03:51:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cac372c5-ad31-35eb-bd2d-81c1cedd3d33 | -20.42502 | -47.46331 | 2024-11-02 03:51:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73c5529c-40f3-3419-b797-c469ce5a2172 | -20.32117 | -48.82453 | 2024-11-02 03:51:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0739f8b2-0869-3c5a-9b23-39cfc281ab23 | -1.4717 | -46.7214 | 2024-11-02 03:55:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 78529de5-1e59-3fb9-929a-08cb6af0185f | -2.2663 | -53.7422 | 2024-11-02 03:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0993742d-7d04-3c14-b619-8b4dc65ffd0c | -2.8386 | -52.8794 | 2024-11-02 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d48de578-951f-3120-ab24-6a5cd330b874 | -2.8061 | -51.6095 | 2024-11-02 03:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| e7c8a8db-3122-34a4-84af-f39185ac964c | -3.0734 | -54.167 | 2024-11-02 03:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d9fbaa63-f6a1-313b-8183-8fda9133a9ea | -3.1282 | -54.2459 | 2024-11-02 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 50090a8a-3b9b-319a-a3a0-e0a6cb6dfbee | -3.1281 | -54.266 | 2024-11-02 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e0a56510-b6de-37d3-b914-4f781da18e7b | -3.1097 | -54.2865 | 2024-11-02 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7c8a8ae1-ce33-38a8-8ded-a79379055372 | -3.7701 | -43.5554 | 2024-11-02 03:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e901aa5a-905c-3cd6-b173-ac7f737e3449 | -3.9474 | -48.3451 | 2024-11-02 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| cb9b4144-bb1c-3b94-8936-47b12c0ec551 | -3.9473 | -48.3666 | 2024-11-02 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7ab6e270-b37e-35e5-8a42-d80c8a675197 | -4.3165 | -48.63 | 2024-11-02 03:55:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 9af99406-1390-3968-a931-5ce115dfaec1 | -4.2032 | -45.8762 | 2024-11-02 03:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 06913ae5-74c1-32a3-b932-224f54aaa66d | -4.3537 | -48.6068 | 2024-11-02 03:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 883a0dce-9db1-3d92-b74c-73ad194f32e4 | -4.3536 | -48.6283 | 2024-11-02 03:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 19be385e-b4ee-3043-b566-4318ea72b334 | -4.4054 | -43.4746 | 2024-11-02 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 519c7f3a-e4a1-39a3-a24e-f8c4191b6d4a | -4.3869 | -43.4525 | 2024-11-02 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 631e3b30-1a09-3a8c-acd0-e98761590213 | -4.3867 | -43.4757 | 2024-11-02 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a2ae9a99-699e-3f06-adce-ad5f33d43052 | -1.4717 | -46.7214 | 2024-11-02 04:05:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| aa62bb9a-23e6-3ebc-b5d4-7ade1ddc5bca | -2.2663 | -53.7422 | 2024-11-02 04:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e44e4eff-9290-3b34-bbe9-734f112dfeba | -2.8386 | -52.8794 | 2024-11-02 04:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0d8c8274-4ff1-3eeb-86d7-46b97784360b | -3.0734 | -54.167 | 2024-11-02 04:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2fbca8a9-ca4a-3cc6-b48a-fb0561a44376 | -3.1281 | -54.266 | 2024-11-02 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c6b44d2d-681c-3bc8-b752-9025f8a8c16c | -3.1098 | -54.2665 | 2024-11-02 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d7020742-785b-31d3-b24b-9ef7a6cf6e32 | -3.4082 | -44.9914 | 2024-11-02 04:05:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8b66f596-1f85-35d3-933b-c812ad0a223f | -3.7701 | -43.5554 | 2024-11-02 04:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a5b9420a-d7d4-32d7-8c16-b9dd504eefba | -3.7888 | -43.5545 | 2024-11-02 04:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d569d737-f17d-3b7e-ae4d-e5a468f38827 | -3.9474 | -48.3451 | 2024-11-02 04:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ab188dd0-8268-383c-989b-e24988c5ed02 | -3.9473 | -48.3666 | 2024-11-02 04:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0e461974-b0f6-3497-a4ca-a8e88fb26a46 | -4.3164 | -48.6515 | 2024-11-02 04:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 47296715-c549-34f0-a37c-4fd90f31ad15 | -4.3867 | -43.4757 | 2024-11-02 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ceff3dba-313a-3ff4-82e1-29ecd2bdbf45 | -4.3869 | -43.4525 | 2024-11-02 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| cc9b8c4d-3901-3b2d-b0ee-18e532c6997a | -4.4054 | -43.4746 | 2024-11-02 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| eba9b2ea-7f42-34f9-afbf-5d6b465974c8 | -4.3537 | -48.6068 | 2024-11-02 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e0617989-97a4-3fb5-b1cb-18774e909118 | -4.3536 | -48.6283 | 2024-11-02 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 535ea468-e7d2-3498-8fb6-3276b497a5ec | -1.92938 | -48.28937 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc4e4c5b-bd80-36a7-bb9c-4560a4122e69 | -2.96973 | -40.32719 | 2024-11-02 04:10:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79155721-f256-3add-aeba-6cbf3ac0c6ee | -2.96179 | -40.24187 | 2024-11-02 04:10:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ac5bcfd-1613-3211-9415-b0592544fa87 | -3.40032 | -41.64326 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 21998a9e-1883-34cc-a491-75387ee8b89f | -3.397 | -41.64275 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bcdca867-a2e5-3f18-8c6b-f4fc7c11d0d8 | -3.39646 | -41.64622 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34166cee-850d-365d-9241-d10b3aba623a | -3.39313 | -41.6457 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab7cdc4a-e946-30ca-b2d2-2e2410d995da | -3.39259 | -41.64918 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e72bba3-d167-309d-9f87-e10ac4ff6f19 | -3.40086 | -41.63978 | 2024-11-02 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 210f20e4-11c9-3e6d-86af-20558cbb11e8 | -1.05467 | -47.64144 | 2024-11-02 04:10:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 502cb3af-f673-3149-a316-2104c10a4066 | -3.53311 | -40.66875 | 2024-11-02 04:10:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57b696c2-8a68-3643-b31d-63da42860acb | -3.50462 | -40.76167 | 2024-11-02 04:10:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 410d1032-bc0a-3d34-88d3-eb6c5643e5bc | -3.50123 | -40.76114 | 2024-11-02 04:10:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c541c1a9-76aa-3cf0-9eaf-194a8dd97317 | -3.86433 | -40.63629 | 2024-11-02 04:10:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78f6484f-46c5-39dc-9015-112efe870acf | -3.84934 | -40.70959 | 2024-11-02 04:10:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c4f0167-f2da-3d8a-a458-07f98c1a2fec | -3.22753 | -44.42101 | 2024-11-02 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README29.md)
