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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bd26de6-5b7d-37de-bb73-5982366422f5 | 1.09755 | -56.01731 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df5857fa-6d90-3e61-aba2-20f8f5ced548 | -2.63615 | -53.35538 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b89fccea-0549-325b-b7ea-aa4acf57a4f0 | -2.90535 | -51.5801 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 126d4088-47c1-3296-807f-fa96b088ac88 | -2.26482 | -53.60814 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 970b4cd8-1c3d-3d17-99ac-75ee046f4b12 | -3.62281 | -51.54033 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bff2729-2242-39ba-a2f1-ead81ec1be42 | -3.30819 | -53.86865 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16e36375-92f6-3fc8-8775-660be7e2d002 | -2.44179 | -53.99621 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 833b4df5-ec35-3a53-8922-71fb85ddbbdc | -1.95356 | -53.3426 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e5825be-56f6-32b3-a7c3-cbf6019b7f60 | -1.94674 | -53.34634 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d55d23aa-4c0e-3f47-8c72-2afb3a8a3215 | 1.10302 | -56.00311 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78440b9c-ba7f-3daa-a95d-78718b633355 | -2.91751 | -54.11911 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fa702f1-4be9-3b66-bb3b-48ae2440481b | 1.21279 | -56.0126 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5321a100-5f15-30ec-9c5d-ab91ce682ad6 | 1.12261 | -55.9852 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd844abb-990d-37bd-99ab-4ef112d0fee7 | -3.62373 | -51.53376 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c56d30ae-f71d-303c-9b96-ec346188f3c1 | 1.14747 | -55.96793 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6ef0804-54fb-39b5-81c9-e0604a7b4bff | -3.25592 | -53.62024 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7b72b13-c3d6-3f25-9edb-523bc0fcb0c1 | 1.10964 | -55.99852 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28a3a1cf-857d-3b69-8479-953c6e8c1371 | 1.20575 | -56.01999 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d4f76662-542a-3bda-b30b-8280298cc693 | -1.70111 | -52.64165 | 2024-12-02 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92ade995-c2a7-3817-b9a7-c353b5b1cda1 | -2.74502 | -51.75391 | 2024-12-02 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e69c6e3-1116-39b4-b938-8ca773eb5361 | -3.13043 | -54.52871 | 2024-12-02 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f648656f-59bd-3b91-ad55-ea4dff958678 | -1.56997 | -55.33537 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c59bbe6e-1384-3608-963d-ce0d34f01bdd | -3.55129 | -51.45015 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a5b6d14-e384-3850-964f-ac2cbb8ff185 | 1.14258 | -55.96872 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aec9c34f-7092-3f38-a189-6b3a0a0baaf7 | 0.90974 | -59.44715 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9a4cc31-de4a-38d2-ab4b-8e367362d487 | -1.09796 | -53.64843 | 2024-12-02 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20033779-3ba0-3580-bd44-91fe2cb958ab | -3.25995 | -53.6356 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec5c7e18-2548-3536-9045-9302a73a1276 | -2.196 | -53.77899 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6e468ac1-6659-3a1d-8378-3704701bf4cd | -3.29928 | -52.07582 | 2024-12-02 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7fe4c0b-33a9-3718-bad3-41c204c35d3a | -3.43375 | -54.60765 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 773bbb33-19f8-360e-bb3c-0f2fc59558af | -3.29777 | -53.84298 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe27ddcc-0b9b-338d-8017-b0d4e616ec32 | -1.49939 | -54.95284 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 411c65ab-d9ac-3350-be19-4e31666a06af | -3.64839 | -51.12174 | 2024-12-02 05:42:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f498bcbe-c32d-3913-aa83-f2805279f3c9 | 0.7715 | -59.89395 | 2024-12-02 05:42:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f39cc5f-ad3d-3975-8349-2f8ef6d45feb | -2.26639 | -53.60941 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebeda6d4-7b6c-32c4-a0ab-13efef858d8c | -3.75016 | -52.26989 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9307033d-fbc3-30c2-a3f8-3aa62b718ee6 | -2.35217 | -54.36689 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85a1c90d-3e78-332d-bd47-1a4f326f2437 | 1.10731 | -56.01574 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 828c0247-56ad-36dd-a746-33386fc52298 | -3.25523 | -53.62502 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f8c5c51-8cb9-3be5-8f49-7d5de1951786 | -2.63469 | -53.36498 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 09be106f-464a-3b73-8891-d4803095c25a | -2.45723 | -53.62686 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c85b1b7b-435f-3f03-a343-7a5be4db7917 | 0.80639 | -59.66833 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1242a156-134e-3615-ac6c-1e8305fdcbff | -1.24902 | -54.55233 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6ea11ba-123a-3fe2-908a-9a05af006eb6 | 1.13456 | -55.98124 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e769f488-958b-330a-b721-e1a8a40f35f2 | -1.4415 | -55.43005 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcac3056-fd41-3934-84f0-30ab2466402b | 1.11589 | -55.9898 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fad0e6fa-134b-3a05-82d4-bdaa1e83d99b | -1.27138 | -54.55587 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a24a23fb-153a-3e36-b1d6-5a5edf11b934 | -3.49936 | -53.84038 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa33545-4fc5-3d46-acb0-f25db52e8e12 | -3.79104 | -58.97871 | 2024-12-02 05:44:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6435a7cd-4666-362f-a27a-2db0e049b491 | -3.79595 | -58.9753 | 2024-12-02 05:44:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28c97df6-ca8d-3224-bc23-b281446feb03 | -3.70062 | -64.59131 | 2024-12-02 05:44:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c76d3aa-1e4c-3d2f-a73d-5b31a6781dda | -9.34806 | -58.22945 | 2024-12-02 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6540164-c8b9-3e54-a92c-09b6264857c9 | -3.79165 | -58.97466 | 2024-12-02 05:44:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1447991e-6e96-3414-a66a-0d0d3dbfcbda | -9.29052 | -64.2423 | 2024-12-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f0d990-0ffa-3e23-a223-e72fd17c14fa | -9.59159 | -53.40209 | 2024-12-02 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae6828e2-c6bf-34d3-87d1-a55cf6836d35 | -9.82512 | -62.37671 | 2024-12-02 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f09fb86f-d1ec-3ee7-b3c2-2cf6e3bc8473 | -9.51821 | -62.93541 | 2024-12-02 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e914b53b-607b-39c3-88e3-9821b60a8c99 | -9.64719 | -65.73383 | 2024-12-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| beaca677-0b4f-37a0-be50-c3c1e3bd4bec | -9.67191 | -66.73155 | 2024-12-02 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 840ba858-b1a1-38ce-9506-00e1895b8dbf | -3.60703 | -59.73202 | 2024-12-02 05:44:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a127faa0-0aa4-3338-9086-7baef148cede | -9.34879 | -58.22387 | 2024-12-02 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3e5fa22-6513-39f5-9237-1c21ff3adbfc | -9.52184 | -62.93595 | 2024-12-02 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6af87f17-488d-37fd-b487-7b7853fe95e0 | -4.47697 | -61.08205 | 2024-12-02 05:44:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80073fb2-3854-3512-ae61-6760f9fd8ff5 | -9.8858 | -66.73398 | 2024-12-02 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da13d5ed-ab0a-3fc7-a391-a68d9f482592 | -9.82597 | -62.37494 | 2024-12-02 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c1370e0-734e-3e6f-86d1-bfe141ac6655 | -3.60715 | -59.73207 | 2024-12-02 05:44:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50c65973-db57-37f0-aea2-f11033132775 | -9.29338 | -64.24657 | 2024-12-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fabba8e9-cf0e-3e62-9fd2-dbb88a3f05c0 | -9.28996 | -64.24606 | 2024-12-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a594be8e-73d9-3cec-a118-d3821872457d | -9.36627 | -58.24321 | 2024-12-02 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7257f96-2814-389a-9cc3-eda7576385bf | -12.38329 | -63.67187 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21403bbe-4891-3094-82b9-90deaa265cad | -12.43129 | -63.74829 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15b69e47-7620-3cb7-944a-49942a0099e9 | -12.43551 | -63.74461 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1427d9c3-a57c-30fe-a311-723d38080a80 | -12.80341 | -62.14738 | 2024-12-02 05:46:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 777edb68-fb05-3f27-b5e3-6518df282faa | -12.3863 | -63.67665 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b568c246-6c78-3f24-b132-3f48a7f6bac1 | -12.41749 | -63.74189 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81adf2e2-b439-3acb-843a-67ef318e1d74 | -12.40368 | -63.73549 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00ccbfe7-e9c7-35f7-bd26-14aa5dc87be4 | -12.4283 | -63.74353 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37075cdf-210f-3133-a59a-927eb09c768f | -12.4349 | -63.74884 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76628090-886a-364c-883e-c3270b2c4e82 | -11.81668 | -61.73333 | 2024-12-02 05:46:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47ca5bdc-9641-3d5f-bf74-dba5382dbfec | -12.79746 | -62.00964 | 2024-12-02 05:46:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 921c6fa4-fd16-3b99-be47-3626d7972449 | -12.25601 | -63.46302 | 2024-12-02 05:46:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c1853ab-ad76-3d72-b9e3-1db8018a348c | -12.88143 | -60.0041 | 2024-12-02 05:46:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 170d5326-6cea-33fc-9a7b-31dab4a136df | -12.42769 | -63.74775 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 406e9dac-7cd5-39df-8128-c56cda7ffd50 | -15.09521 | -59.63989 | 2024-12-02 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 656cc512-d102-3e38-ba2b-56c03e755fab | -15.07454 | -59.64825 | 2024-12-02 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29d858eb-30b8-3409-a7ff-ddbe2f6308a3 | -13.50424 | -61.53744 | 2024-12-02 05:46:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e922b6d-716e-3647-9ea0-c9967ca01269 | -15.09587 | -59.63446 | 2024-12-02 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ba9a8c1-4e2d-3422-884c-130afd06827f | -12.40429 | -63.73129 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd8cda02-b05e-3f00-b7d7-357b9928693b | -12.4085 | -63.72761 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd9585d2-f438-3b4e-96d5-3a117ac21be0 | -12.25634 | -60.50979 | 2024-12-02 05:46:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbd70d4e-aa1d-321a-a593-e1a118da1dc0 | -12.25236 | -63.4625 | 2024-12-02 05:46:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 45beefdb-261a-3dc0-98c3-df85110004f6 | -15.0697 | -59.6476 | 2024-12-02 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d8d1cd2-8b52-327f-8798-0cc42c1c5e67 | -11.91187 | -63.681 | 2024-12-02 05:46:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 245bff27-b81f-3df6-acda-4c443a891fdd | -12.42408 | -63.7472 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48cbfcd9-a7df-3448-9fa9-37d2eeb0eb13 | -12.41266 | -63.7498 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb4a501c-82ba-3653-a6ad-3c8dec60a683 | -12.2735 | -64.33479 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed22b972-b58d-372c-bf05-f7a7485c6edf | -12.43191 | -63.74407 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d11a650f-9c6c-3655-a0bc-60bb48341fbc | -13.50602 | -61.53704 | 2024-12-02 05:46:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7d54c1f-c750-3d46-a4a8-76d84c109b6d | -12.26999 | -64.33426 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e65c1c-5098-3d7e-9a4d-62ba5f169ccb | -11.81717 | -61.72976 | 2024-12-02 05:46:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README75.md)
