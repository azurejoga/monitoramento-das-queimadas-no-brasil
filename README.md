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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7679d92e-4347-3a3b-9365-be882c3b7977 | -6.6537 | -43.4256 | 2025-10-21 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5e61f492-5faf-3abe-bc1c-591f383d8018 | -3.3337 | -53.3536 | 2025-10-21 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a9e3f7c6-d8c2-3af0-8db0-e75487338752 | -4.7155 | -47.1777 | 2025-10-21 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 14650a87-7adb-399d-8682-76394fc3f342 | -3.4968 | -45.8195 | 2025-10-21 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 75cb74da-c71d-3e9f-aaf9-6a23e3921454 | 1.6935 | -55.7448 | 2025-10-21 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8d2e49fa-365a-3e7b-9428-34461b2a49ba | -3.9739 | -50.3644 | 2025-10-21 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6c033051-a5cf-379e-8088-ba1afbf93629 | -3.9923 | -50.3636 | 2025-10-21 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d434a43b-0ed8-371b-958a-91168411d583 | -4.6463 | -46.4095 | 2025-10-21 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| db54acbd-d595-3974-becb-ec566d6631ed | -3.5153 | -45.8411 | 2025-10-21 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 448627c7-6a47-3edb-9e79-a2008ca2e63a | -4.7156 | -47.1557 | 2025-10-21 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| aa19c358-5be3-359e-84dc-baefb80c176b | -6.7399 | -44.1602 | 2025-10-21 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c3189578-76fa-3f7d-b2b2-c808088af5b3 | -3.5154 | -45.8187 | 2025-10-21 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 5ca6cab8-3122-349c-b51d-83e292e016c8 | 1.7302 | -55.7049 | 2025-10-21 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e19eac4e-ed74-343e-a886-74c0bf77c603 | -4.5213 | -45.6131 | 2025-10-21 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 00d1cb5b-9177-38f1-a87b-d6291357207d | -6.7401 | -44.1371 | 2025-10-21 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 34489187-28da-3b18-ad20-86313569f063 | -3.3153 | -53.3541 | 2025-10-21 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8146a67c-cbd2-35e5-acf1-2a25bf54d1c1 | 1.7303 | -55.6851 | 2025-10-21 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0e5c5013-b77c-387e-8d2f-2cef3a2937bc | -4.4806 | -49.0936 | 2025-10-21 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0805286e-7488-35b0-a525-3d5e8d4824f0 | -4.6649 | -46.4084 | 2025-10-21 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9f0ae722-5826-3d4f-929d-8e0dab25d7f5 | -3.4967 | -45.8418 | 2025-10-21 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 9c06bbc1-9487-32ad-bc56-efee2c410ceb | -17.6852 | -52.2398 | 2025-10-21 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| abc3316c-e49d-33c9-947e-efda29908a12 | -4.3879 | -43.3129 | 2025-10-21 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2211ca23-7e67-30d7-9ba9-02a4586c0693 | -4.6461 | -46.4316 | 2025-10-21 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3c791ca8-300f-3438-9b7b-c67fa85f06cc | -3.3441 | -50.7426 | 2025-10-21 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 10001bef-701e-34d9-9957-857e2bb3bbf9 | 1.7119 | -55.7248 | 2025-10-21 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a5572de3-c57e-3b4d-8089-cb9a3339cd28 | -4.4066 | -43.3118 | 2025-10-21 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| dea1b796-b55f-329e-b917-51efc19c2c59 | -4.6277 | -46.4105 | 2025-10-21 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5a49f715-d5c0-31e3-95d8-2773a51e7bf2 | -9.0221 | -65.9407 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5a994e67-5575-3ac6-8444-a695fd48ef2d | -4.6461 | -46.4316 | 2025-10-21 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 8cbbcdd3-6c0a-343c-95ae-59a481a98831 | -4.6464 | -46.3873 | 2025-10-21 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 113dbfda-864b-3ccd-b413-e9843ce1d0de | -17.6852 | -52.2398 | 2025-10-21 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1d02b70e-711e-3a47-a123-6d97e02481f6 | -9.0036 | -65.9226 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 1653878b-a467-325d-aa28-0c88f322df65 | -9.0037 | -65.904 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| eb263773-c0d6-3c57-a395-2cbe443376ab | 1.7302 | -55.7049 | 2025-10-21 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8319b9fe-7ce1-38c8-b560-b46fc2d502cd | -9.0222 | -65.922 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ea69c604-64ff-3a20-983d-19b7d321ca41 | -3.5154 | -45.8187 | 2025-10-21 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 5ad6dd97-d26d-33fd-bf8d-8964218151a1 | -9.0036 | -65.9412 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 5416d7bc-df28-3658-8e3d-bff526a93b68 | -3.4968 | -45.8195 | 2025-10-21 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 188.4 |
| d0809a01-2695-3d18-bbb1-d85a0b94d794 | -9.0417 | -65.6976 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ebcf46a6-9fe0-37a0-b932-6ab33a10423c | -6.7401 | -44.1371 | 2025-10-21 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c5feb9dd-c0ab-34b0-9c7e-86b1af8d2927 | -4.3879 | -43.3129 | 2025-10-21 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b7c15323-0883-3702-a0ca-bae382496932 | -8.9851 | -65.9232 | 2025-10-21 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 05b9d617-e35a-3c52-82de-caf9ac19e094 | -14.2588 | -51.7978 | 2025-10-21 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4deb2c25-df2d-34c2-b0d4-2442b3a8ac2b | -3.5153 | -45.8411 | 2025-10-21 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b41e1137-e8c7-343c-9ace-8fdf1c6cc784 | -3.4967 | -45.8418 | 2025-10-21 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 97f8e469-5cb5-3079-a08d-ad52def0e603 | -4.6463 | -46.4095 | 2025-10-21 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 242.1 |
| a7fdea64-7f86-35cd-8657-b1bc1ee43632 | -6.7213 | -44.1387 | 2025-10-21 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 194d65d6-2dba-31a4-a7af-7c165477d376 | -3.3153 | -53.3541 | 2025-10-21 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 08b7a2e7-6a01-3331-a040-b7b01bbab4d4 | -4.7341 | -47.1767 | 2025-10-21 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0ef6be79-c6a9-3594-8583-0d0e2262e1f9 | 1.7119 | -55.7051 | 2025-10-21 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 38469645-43f4-31ad-865a-27916fad7bae | -10.0842 | -65.1754 | 2025-10-21 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 38000500-47d9-3c70-92e7-9019f863ac27 | -4.4621 | -49.0945 | 2025-10-21 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 99958cd5-9837-3883-bec1-b09a17e3f6b7 | -4.7155 | -47.1777 | 2025-10-21 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| a6d14635-aacc-3be8-85ed-8ecd66e7e6b4 | -6.6537 | -43.4256 | 2025-10-21 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9b7e37cc-f43c-3775-9340-de127f2d9b04 | -4.6649 | -46.4084 | 2025-10-21 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 05cf1903-91b8-3d32-977f-b5d775a9ddac | -4.7156 | -47.1557 | 2025-10-21 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| c266556a-c783-3d58-aa75-e0eac0620994 | -3.9739 | -50.3644 | 2025-10-21 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7874ba56-ec73-3438-b5c1-bf346e3fa5da | 1.7303 | -55.6851 | 2025-10-21 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 40a41745-9ea2-3488-b447-3c0108da0792 | -3.4968 | -45.8195 | 2025-10-21 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 244.1 |
| 07afc4f7-9988-38ed-a637-ee1e02e9e38e | 1.7119 | -55.7248 | 2025-10-21 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8f7ac05f-8229-3032-8d26-e29d3454bb32 | -9.0036 | -65.9412 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 7e4539a5-dcdf-3694-a841-b13a9df9ec33 | 1.7302 | -55.7049 | 2025-10-21 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f35a58ee-0476-33c0-8b72-e4b68efbd216 | -3.3256 | -50.7432 | 2025-10-21 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0d2f865e-c59b-3b87-b259-36866d46ad01 | -9.0036 | -65.9226 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 262.4 |
| 8c43cb18-3d46-3b28-8709-3361b1744ded | -4.4066 | -43.3118 | 2025-10-21 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| da9552c4-4c33-351a-aac4-ad874686cef1 | -3.5153 | -45.8411 | 2025-10-21 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5051d253-13e2-3636-85b1-b63313de3e91 | -4.7155 | -47.1777 | 2025-10-21 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| bbac230f-08b8-377f-842d-3188ddfb90d6 | -4.3879 | -43.3129 | 2025-10-21 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| de47f080-82ad-3b81-a45a-b9c360beed57 | -4.6649 | -46.4084 | 2025-10-21 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e52668d8-bb0f-3d16-a50c-dda100d8f028 | 1.7303 | -55.6851 | 2025-10-21 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b80ed7be-962b-385b-a9a8-347ed7208749 | -4.6464 | -46.3873 | 2025-10-21 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 81cf9409-b4d7-31d2-b0a4-5763f0c8ac24 | -3.3441 | -50.7426 | 2025-10-21 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| eb795dc3-25ee-30d2-9be1-7b9dbfeeafa8 | -4.6463 | -46.4095 | 2025-10-21 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 170b9328-696d-32fd-8e0c-5e8d102407eb | -8.9851 | -65.9232 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 061cdc47-ba8c-3f78-b5eb-7c6d7a62c969 | -4.7156 | -47.1557 | 2025-10-21 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 274fa415-ae47-3a35-a8f8-63f715c7bac6 | -4.6277 | -46.4105 | 2025-10-21 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f3b78ccb-ca54-37ee-8603-2239ddc32665 | -9.0221 | -65.9407 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f69a3ba1-951c-3222-a45a-5160cc53a803 | -5.4366 | -41.0797 | 2025-10-21 00:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 4c033ddf-7b2c-31b6-988c-9f51c0aad956 | 1.7119 | -55.7051 | 2025-10-21 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| dd2153d1-6d70-3c07-8514-764d2039dd1c | -3.2321 | -46.7836 | 2025-10-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 06234ae2-f2f4-3824-a049-f13e8c69e0db | -6.6537 | -43.4256 | 2025-10-21 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 848a578d-9fe8-3e33-97c5-605e686936ed | -3.3153 | -53.3541 | 2025-10-21 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9eab8a10-7229-3a90-8b3d-9f4e50fd72bf | -3.5154 | -45.8187 | 2025-10-21 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 4c5368fb-ebb9-3ebf-a325-1d972127798a | -3.9739 | -50.3644 | 2025-10-21 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 08d0810a-9b4c-3289-9e93-b04ab5d7a066 | -9.0037 | -65.904 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e81bd8fa-126e-3960-98c4-a13a5e5c721f | -6.7213 | -44.1387 | 2025-10-21 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ac26e42c-d491-3fbe-bbd4-9d7fed7d7f3e | -4.6461 | -46.4316 | 2025-10-21 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e8a5d14c-c9b4-3b66-9ba6-8d4daf029260 | -6.7401 | -44.1371 | 2025-10-21 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9ad6dd2d-64ae-38dd-bb98-45b70ea7dbe4 | -17.6852 | -52.2398 | 2025-10-21 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 420758bf-de54-32b3-9aa3-eae2d2694d82 | -3.4967 | -45.8418 | 2025-10-21 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 124.3 |
| b8568b62-b0c0-3ac1-9c2e-19f7d338fd72 | -3.2136 | -46.7843 | 2025-10-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f731aafb-a136-317f-8a2d-006e784b56fb | -3.9923 | -50.3636 | 2025-10-21 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b3f88b1c-e97f-33f2-8f75-9f47ef2d5159 | -9.0222 | -65.922 | 2025-10-21 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b5416285-ddf7-3646-afee-53468928183d | -4.6464 | -46.3873 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a351454a-29a1-3331-a019-92550c321aaa | -4.5213 | -45.6131 | 2025-10-21 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3c35b193-6a55-3f09-b285-7d4a96853649 | -6.7401 | -44.1371 | 2025-10-21 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2c5fe53d-f66a-38e4-b7c2-bba6b16be86f | -4.6647 | -46.4306 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4364a38d-7f76-3cfe-8e36-f251bb24ed33 | -3.87 | -48.9707 | 2025-10-21 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 96d06e75-11fa-313b-8ff9-7d8b5fdb628c | -4.2645 | -45.0184 | 2025-10-21 00:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9a3bc753-268e-34fc-adb4-f59622dcfed8 | 1.7302 | -55.7049 | 2025-10-21 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |


[Clique aqui para ver as próximas entradas](README2.md)
