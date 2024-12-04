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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c385e4f1-24f4-3bde-b62d-24be4d887398 | -5.57814 | -45.14735 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 505e176d-8b5c-3000-aef5-6a43d20fdc96 | -5.69931 | -45.04346 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e5ac968-1785-3ef0-9783-0ce89d952485 | -10.17542 | -51.52092 | 2024-12-04 05:05:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d428319-7ae0-3286-b080-dcab873e188c | -10.18363 | -51.52211 | 2024-12-04 05:05:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c7f18e-c2e0-3eda-be24-01743000c4e9 | -2.8196 | -53.0629 | 2024-12-04 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c70760e6-420b-3056-868e-219957f43771 | -1.7544 | -52.6363 | 2024-12-04 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8c6d41a6-9588-3950-9659-29c58e06a065 | -5.588 | -45.1638 | 2024-12-04 05:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5e34e762-14fc-3920-af4f-498e811d808b | -3.2591 | -53.6186 | 2024-12-04 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d5dc441b-768b-3585-abf9-facc6c6af16c | -1.7361 | -52.6162 | 2024-12-04 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 6d8b0907-e487-3a30-a552-98a0fbdf12f4 | -1.7728 | -52.636 | 2024-12-04 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 28ab9dad-5404-3a7b-ad27-aaf6c7e923f8 | -5.5882 | -45.1412 | 2024-12-04 05:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a8da415a-4673-31a3-83ce-1ad0732a28cf | -3.259 | -53.6388 | 2024-12-04 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1b8fd65f-efa0-38c1-892d-29845838a569 | -1.7545 | -52.6159 | 2024-12-04 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 53a747d2-a2f1-34d1-87b4-ee0655e158ca | -3.259 | -53.659 | 2024-12-04 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 55a36b42-ebe9-3805-8a2c-bfa877140942 | -3.259 | -53.6388 | 2024-12-04 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 07a4325d-2131-38b7-8eae-dc2523ecbe26 | -1.7361 | -52.6162 | 2024-12-04 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c9c6cb2a-00fd-30fd-aa2f-a165e7470a68 | -3.259 | -53.659 | 2024-12-04 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e7c0df4b-8ae1-33a3-aa59-86fc5c748e2c | -3.2591 | -53.6186 | 2024-12-04 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 86976476-c178-31e5-9d5d-066a4f087d06 | -2.8197 | -53.0425 | 2024-12-04 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| beb8f988-cc97-37a3-816b-6c7a3ebbfce3 | -1.7544 | -52.6363 | 2024-12-04 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 60da19b4-8256-31bd-b87f-09d8c2978156 | -1.7728 | -52.636 | 2024-12-04 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d0c374ee-5061-3969-a915-b3b2df025a90 | -2.8196 | -53.0629 | 2024-12-04 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 394d0fa8-2e3c-3afb-99e0-a702ef95846c | -1.7545 | -52.6159 | 2024-12-04 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 5e577c82-2b9b-31a7-9831-534b0b8bf300 | 1.3277 | -60.72505 | 2024-12-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d5be966-01ee-312e-a778-78344074f391 | 2.70113 | -61.2848 | 2024-12-04 05:27:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69974535-0ffb-3b9e-86ed-faf9518b6afd | 1.28291 | -60.54845 | 2024-12-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e3ced08-300d-3cc1-a9af-732bae198ff5 | 1.12702 | -55.95942 | 2024-12-04 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b7687b-d521-3c7c-884b-8ee05ba3ec3a | 1.94791 | -60.8624 | 2024-12-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 553947ed-a1d1-3cb3-a886-cf686b82a651 | 2.42267 | -60.64985 | 2024-12-04 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfe311b4-a1d3-3fda-b2bf-e41f491d21eb | 3.02219 | -60.50337 | 2024-12-04 05:27:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f3a9c4-dc40-3fa9-9faf-5a563616fcc3 | 2.10028 | -60.53762 | 2024-12-04 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 271db901-f0ca-34df-8584-e9d67efbc60f | 2.42321 | -60.65332 | 2024-12-04 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fa5f3a5-6374-3abc-8a0a-200606f13403 | 3.01886 | -60.50388 | 2024-12-04 05:27:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41dbe9a1-d877-328c-926e-6ca91a716f9b | 3.13881 | -60.27652 | 2024-12-04 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e9c2b7d-2362-3624-8014-c9f835ce5911 | 1.96993 | -60.91592 | 2024-12-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37f16280-d756-37ad-96bb-09424f21c7d8 | 2.42654 | -60.6528 | 2024-12-04 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 892657b4-685d-3dd1-a87a-ca4db1e34d39 | 1.96938 | -60.91245 | 2024-12-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb4d80aa-3f3b-3fd9-9854-cd4143c6a881 | -3.25967 | -53.65257 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 454db5c6-1675-31a8-a51b-f2c033e726b2 | -3.17818 | -54.33179 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d066f846-1016-3372-894b-2ec9a76c685c | -2.88561 | -51.81911 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c93b293-683b-3161-ad0c-790d32d1521b | -2.88108 | -54.12051 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37b66503-5418-3f1a-a96d-181119747cc9 | -3.17857 | -54.33995 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cecc6ca2-e16e-3542-b3f7-d6e7189cd176 | -3.05484 | -54.50739 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf39b39a-1f6f-3289-935a-a1810a8d6a52 | -2.99131 | -54.11012 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ada985-a3db-3874-b82c-ea81c65bbaac | -3.25479 | -53.65183 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46ebf844-485a-3ca3-b2cc-df92abad0001 | -3.18977 | -54.5089 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd8c0ab4-a4ed-3daf-90a7-f230ba36c898 | -3.4223 | -54.02605 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f4e131b-77bc-342d-8304-de51cc46d429 | -3.13114 | -54.6163 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| adbaa6cb-5630-3992-a5d8-c8d8adb1630b | -3.37258 | -51.09892 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f97d8a5-f1a2-3f99-9954-a9987ff731f7 | -3.24528 | -53.87289 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55d1b76c-8f82-3955-8d10-148037daf92c | -2.7969 | -54.13772 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8329785e-d665-30dd-945e-47765fc20c56 | -1.78574 | -52.75061 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eba7cd1-a04a-3ab0-897b-c0d52a46535b | -3.20103 | -50.65194 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa4066e9-c8ae-3445-b9aa-2d280d379cb7 | -2.88444 | -54.16079 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c78f41-6450-3a1b-8ce1-58274647a2fd | -3.33356 | -51.20457 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b0c147-08f2-398e-bd73-4d5c210228c3 | -3.26456 | -53.65329 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b827010f-327a-3df5-8348-efb7b84334a3 | -2.85607 | -54.82659 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5df36a00-c569-3c6a-b1bf-da06f24c7999 | -3.12802 | -54.60634 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b3346b3-4332-3b48-83c5-a989828e17c0 | -2.82131 | -53.05055 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e53f1d-0405-3e2e-b3f5-6587a623e80d | -3.25317 | -53.66256 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64b1b066-880f-3d8b-983f-ac44ad44dcd5 | -3.17615 | -54.32478 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deeb7c91-237b-366f-9e99-2bdc8d46d40a | -2.81997 | -53.05929 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37cb7af2-cad0-3698-be06-a506e46a3084 | -1.72525 | -52.4824 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 221f9d31-99d8-3561-b129-6d3c661cf221 | -2.94297 | -53.28928 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 542c6f65-2520-364a-a557-bbc617ae6ca7 | -3.4851 | -53.79907 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e0cfe7b-5e66-3ea4-bb72-abdbbb24d172 | -5.37377 | -60.10126 | 2024-12-04 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4233adcf-4cc8-3e3b-8f5c-e51fba3c10e3 | -2.86121 | -54.06177 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2e92ca6-bfab-3c82-a856-c37f28ffe974 | -2.02177 | -59.77545 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ac93ec7-22a1-33dc-aa58-14706d2727bf | -3.12561 | -54.62653 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0de1f9b5-b755-382e-8630-e57bae314150 | -3.41251 | -50.27214 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95eea832-d2c6-32dc-94e2-0e9ce45e7f5b | -3.98257 | -50.51448 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81095a1e-ddd2-31c9-a660-52e02c3d4855 | -5.12562 | -60.3293 | 2024-12-04 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63c20f34-be29-3280-b28e-e7c083bde766 | -1.7488 | -52.61702 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1858389-f84b-39d1-a212-7403159a0a0b | -2.88832 | -51.80125 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a63c6bf1-1632-303f-b716-ea1815ebcd00 | -2.79239 | -55.35637 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 675ed9c4-a4df-3c20-b6c1-885332573c29 | -1.06547 | -62.65171 | 2024-12-04 05:29:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ecb20c-624d-32b4-8398-6aa3f388cdc6 | -1.90167 | -52.85188 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21bb825d-25c7-31db-8643-aaa454df652d | -3.12659 | -54.61557 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e7d8874c-2c86-3fcc-9d8b-3b9d4f4ef604 | -5.37035 | -60.10075 | 2024-12-04 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6418f8-4bfb-30e3-b84f-8295feb39a6b | -3.18005 | -54.33038 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 775c4474-8efa-361f-a463-85d5e46edeee | -3.1168 | -54.61863 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fa07a8d7-e997-39fe-b491-189fed812449 | -3.7867 | -50.96844 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9d3be3c-8788-34d9-90b6-7a5a127a587b | -1.31674 | -54.57158 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40400543-571a-3531-8ca7-caadf228096f | -3.60472 | -50.79754 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 441d6b6b-2a18-3c8e-bb95-acfd5cbbaec0 | -3.18282 | -54.33257 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b12b862-815e-3b17-b0a0-f4b6d6ff0198 | -1.48304 | -54.42745 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac9912ad-0d24-3280-948a-ad051ab375ac | -1.346 | -54.96333 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 476fa9a9-377a-36c9-8b67-5f8127b048d3 | -1.71312 | -52.78448 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbaa2f71-b76c-36e8-b07f-08b0217f03da | -2.81952 | -53.0622 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 657baa2f-1809-35ff-ae66-9f3dae214b45 | -3.55846 | -51.52136 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fef5577-9478-3645-b9ef-9f13fb5b8aeb | -2.98677 | -53.90706 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5a0c5e3-0ec0-37f4-b110-5572240a2114 | -2.89108 | -54.15857 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a759dc7-0755-3dc7-94a6-db9a88d89a43 | -1.68862 | -52.51433 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0866e45-e7a9-3555-b5e3-f00bae308fcf | -1.44351 | -60.08108 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224fe81b-d236-3162-8fa8-222cec27fcd8 | -2.9438 | -53.28373 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d78a46d5-f426-3dd4-8d3f-387ca6343a35 | -1.72573 | -52.47934 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0018565f-1d57-3c47-8170-8e63b75649d5 | -2.22906 | -53.69611 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300e2d19-a016-3ff5-9143-98890428c411 | -2.84722 | -53.96235 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9003e98-51b4-3163-839e-c8ba41f70301 | -1.76325 | -52.6254 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80831406-e058-3392-a3b1-5283ccc7a634 | -1.61965 | -53.53421 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README53.md)
