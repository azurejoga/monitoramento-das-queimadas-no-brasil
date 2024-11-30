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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45fe9915-4fa3-33b2-9f4d-d5b41fc3668e | -6.9344 | -43.5401 | 2024-11-30 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a1e3f4f7-0e43-3cef-b967-49f51cd44d9f | -3.2406 | -53.6393 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9535fb4e-1123-328d-bc1d-47368b70ebe8 | -4.8523 | -41.317 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 9c1df3a8-6e1b-3ce2-b174-5cb7daa9131d | -17.6651 | -57.585 | 2024-11-30 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| fc3a3128-ab5e-3935-b9ff-7ab10ee95f18 | -6.0862 | -48.0339 | 2024-11-30 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 07d2d608-3c75-3321-ba76-9d611f6d9e73 | -17.6654 | -57.5645 | 2024-11-30 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 791dcfa9-d684-3a14-93c9-4406f851f432 | -3.6758 | -47.1176 | 2024-11-30 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 00f5ee50-cf26-313c-981a-f4709edcb4f6 | -3.9699 | -41.5176 | 2024-11-30 02:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 66c43748-24cc-30b5-b54b-79c7b0a9eccc | -1.6938 | -46.7833 | 2024-11-30 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8600c3b5-cc9d-3220-bc69-624d552fc0c5 | -6.9156 | -43.5418 | 2024-11-30 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 414.8 |
| befd0aff-36c3-3cac-8d8e-321cc8e21d13 | -6.8967 | -43.5436 | 2024-11-30 02:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5d739b80-e0e4-3e24-90db-08cefa571095 | -2.1928 | -47.1451 | 2024-11-30 02:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 25d8110a-91ac-3c76-adf9-cceb7506e000 | -4.8899 | -41.3143 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 83532428-df0c-3164-a938-c0aac8da80be | -3.6757 | -47.1395 | 2024-11-30 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0a2a3a1c-7fa5-312f-aa5a-836082261f7a | -4.8713 | -41.2915 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 386.3 |
| badd491b-985d-3765-82cb-385f9550bb87 | -1.6419 | -53.8731 | 2024-11-30 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4d43adcf-72fa-3b25-919c-7aacc53e61a6 | -3.9886 | -41.5165 | 2024-11-30 02:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 97dfa2d4-b974-3e03-b7c2-18cdcf322e85 | -1.6753 | -46.7836 | 2024-11-30 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4d346414-079b-38e1-99c0-dfa00cbab05d | -4.8525 | -41.2928 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| c91aaa82-5ed1-3a8c-894a-7d851986a873 | -4.8903 | -41.266 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| ede1c916-f225-3bed-8aac-ddfa90ac1921 | -3.4975 | -53.8137 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 666eb435-761e-3c1a-acbe-f477782e267f | -4.8715 | -41.2674 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 161.4 |
| ad3d629f-5c56-3c9d-951d-a9bf501076a1 | -6.9158 | -43.5185 | 2024-11-30 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 1d2c801c-61d9-39be-9146-a9cc9fbfa792 | -4.8901 | -41.2902 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 298.6 |
| a7907bb1-e184-376b-8b4a-c9812c1bce8c | -3.4791 | -53.8142 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2bbfe513-1f99-342c-bdb8-04cc81bb71c5 | -3.4976 | -53.7935 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1d3e011b-f4b8-398d-a560-c7d4b0e43816 | -3.259 | -53.6388 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 2d7a4618-9820-39a8-93d6-62c504a3b1e3 | -17.6457 | -57.5668 | 2024-11-30 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| c358e431-7ce2-3189-80cb-e92746755c87 | -3.2591 | -53.6186 | 2024-11-30 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 26f105bd-e5d1-3b9e-ab59-a2b5604b053d | -6.9153 | -43.5652 | 2024-11-30 02:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 18f59baf-2765-3796-8cd0-87093ecb9dc2 | -2.1351 | -54.8861 | 2024-11-30 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4bb2f32a-297d-3e7d-a873-d3b224b9f97f | -2.0163 | -50.7768 | 2024-11-30 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 622d4884-bba5-3ec1-b02f-afa3504ed183 | 1.1805 | -55.9671 | 2024-11-30 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| bdaca5b8-a5b0-32be-96a9-e7eb79248ddb | -6.0676 | -48.0352 | 2024-11-30 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1f779f6b-de83-385d-9e55-2cac06fb2892 | -2.0347 | -50.7765 | 2024-11-30 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b0d4f52b-70ae-3f8a-986d-c2f9128d9baa | -6.086 | -48.0557 | 2024-11-30 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 024df3ca-a4f2-3223-bcfc-b9a6eaff63c3 | -6.086 | -48.0557 | 2024-11-30 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 99ecf64e-b30a-351d-8982-a3c7b1aaa699 | -3.6757 | -47.1395 | 2024-11-30 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 98f27249-be2e-36d5-8af4-834ddd07d820 | -6.9158 | -43.5185 | 2024-11-30 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 73cd3f42-dc7a-3e2e-9fd4-9d431b391380 | -6.0674 | -48.0569 | 2024-11-30 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2413fc03-44d9-3a43-8c68-90db1e16a7f8 | -3.9699 | -41.5176 | 2024-11-30 02:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 5b0d7213-ddd2-3be6-8f3a-2b81de414d6b | -3.6758 | -47.1176 | 2024-11-30 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f25d9527-6e13-3f87-8177-fc1891464661 | -6.0862 | -48.0339 | 2024-11-30 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6489cf3c-9bd7-3d0f-bda2-de18162f6151 | -1.6419 | -53.8731 | 2024-11-30 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 37e37020-b488-3fdc-a003-64c7211bb95a | -2.0163 | -50.7768 | 2024-11-30 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 01333af9-dca4-3f44-8a35-92b6d6054637 | -4.8711 | -41.3157 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 180.9 |
| 6db11fff-5bfe-3542-a562-95b24592505e | -3.9886 | -41.5165 | 2024-11-30 02:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| e4d558c9-f031-3cf8-8016-40f8ef70cfd0 | -3.259 | -53.6388 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 51107883-759e-39fc-9e4c-6b80a8528591 | -3.2406 | -53.6393 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 62becb99-cfc2-3e76-b28e-feaa61ae37b0 | -4.8903 | -41.266 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 2e409f02-6e9c-3acf-81de-b2e0df5bc281 | -17.6651 | -57.585 | 2024-11-30 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| ad3e58f0-b662-34cc-a1c6-9e1103017eec | -2.1535 | -54.8858 | 2024-11-30 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 23542c71-6fcc-3866-9137-305b288992b5 | -6.0676 | -48.0352 | 2024-11-30 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5f56ef23-5fc6-376a-bb41-02ca808458aa | -3.4976 | -53.7935 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7f886f98-879e-3127-84ae-59e8f3f16bd4 | -3.2407 | -53.6191 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8e8a1403-e3f7-347a-8850-7d37fb42f05c | -4.8715 | -41.2674 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 168.3 |
| 28bc151e-6775-327f-a80d-a6c494847836 | -17.6457 | -57.5668 | 2024-11-30 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| ea880bbd-5d6f-326f-873e-d7c89345ced5 | -6.9156 | -43.5418 | 2024-11-30 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 458.3 |
| e5cbe0ff-62a6-3450-a7c9-97d032af9c67 | -2.1928 | -47.1451 | 2024-11-30 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8d2d85ac-04df-3cc6-82dc-0a7b29691624 | -3.4975 | -53.8137 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 522b6723-c98e-34a1-80b7-629c9ee0e5c3 | -6.9153 | -43.5652 | 2024-11-30 02:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 249.1 |
| f0389eb7-ff5c-382b-8ecf-30e9d591c4f5 | -3.4791 | -53.8142 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| aaf2c4ac-fcb9-346a-9a15-0bb1c2ad05e6 | 1.1805 | -55.9671 | 2024-11-30 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c536097b-f749-3e7d-b152-8d1fa9685b12 | -2.1351 | -54.8861 | 2024-11-30 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 216a273e-3914-3b2a-a45c-c11f18fa0d66 | -6.8967 | -43.5436 | 2024-11-30 02:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| bfa9b9cb-275d-3610-9f30-733cf6e82427 | -6.9344 | -43.5401 | 2024-11-30 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8014baaf-d29d-3d88-a0bf-a8f644c64724 | -4.8899 | -41.3143 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 41a8504c-1dc7-3068-b38b-a3adf8ff8dd8 | -17.6654 | -57.5645 | 2024-11-30 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| ea7e37e9-de8c-305b-a0dc-b1ec9368eacd | -1.6753 | -46.7836 | 2024-11-30 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0de0c13f-a4ea-37b8-a69a-bdf7d0a41344 | -4.8525 | -41.2928 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 6430f68e-3d8b-38b1-8c17-aac4425180a5 | -3.2591 | -53.6186 | 2024-11-30 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 211c8e14-6949-3ff7-8c45-64322911cb8b | -4.8713 | -41.2915 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 340.8 |
| bb9b3bbd-0a20-341d-93b7-b598eb7d1420 | -1.2739 | -54.5587 | 2024-11-30 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7d0daa01-937b-33a1-8611-7acca4176ee3 | -2.0347 | -50.7765 | 2024-11-30 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 97b73775-1ba3-3231-be8f-540de15f44ee | -1.6938 | -46.7833 | 2024-11-30 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c5e6de5c-f039-3300-b563-543f305b8f83 | -4.8901 | -41.2902 | 2024-11-30 02:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 220.8 |
| 6dc83cbd-53f2-3a85-963f-20e540e2621b | -17.6457 | -57.5668 | 2024-11-30 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| c6644437-ed39-3e9c-9441-39567aff70a5 | -2.1928 | -47.1451 | 2024-11-30 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4b8b4d69-2aeb-3ac2-91c7-fdc8d47e7223 | -4.8715 | -41.2674 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| 54531eb4-71e7-36a1-b912-e13608f430b3 | -6.9153 | -43.5652 | 2024-11-30 02:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 8b5dc8d0-739d-30b6-a097-d6737e235a61 | -6.8967 | -43.5436 | 2024-11-30 02:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| db06be71-72f3-3ed5-a465-31b372f1ff49 | -2.1351 | -54.8861 | 2024-11-30 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 04ac11f3-15ad-3dd2-a30f-f79113ae5c2d | -4.8525 | -41.2928 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| d2d3557a-e015-3d50-8ebc-ed104cb0e9a3 | -3.4976 | -53.7935 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1d9b9e64-d149-3bb0-b0ad-8e9499824115 | -1.6938 | -46.7833 | 2024-11-30 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 57af56ab-91cd-329e-8aa4-80e9152a0a3f | -4.8899 | -41.3143 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 5797ccd0-dfca-3ad1-8199-0ed3a32ee4c5 | 1.1988 | -55.9472 | 2024-11-30 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 64c3a603-b4f7-363f-85fa-100d786f998d | -3.4975 | -53.8137 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 58880e33-46a5-35c0-9612-4751e1e65153 | -4.8523 | -41.317 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 8c8391ff-fdcc-3101-b284-c8c33188fe58 | -4.8903 | -41.266 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 6f8c6e93-d50a-3950-8cb3-140d9904a5de | -6.9156 | -43.5418 | 2024-11-30 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 527.6 |
| df7c8675-b283-34c1-bf9a-02d9317746d4 | -6.0676 | -48.0352 | 2024-11-30 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ba4c22f5-8007-3154-9a16-b2914370a681 | -6.9158 | -43.5185 | 2024-11-30 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a2c31eb8-79ba-3811-98d2-4c491c2fb693 | -1.2739 | -54.5587 | 2024-11-30 02:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9153f40b-b823-3840-afc7-3e9c034c5572 | -3.2406 | -53.6393 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d8059263-b16a-305a-ba5f-314c60d8a3a6 | -3.6757 | -47.1395 | 2024-11-30 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4b0c1f13-6c1b-3df0-85fe-11c79fa37a7b | -17.6651 | -57.585 | 2024-11-30 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 25773073-8199-3f57-90d7-5724095421b2 | -1.0733 | -53.6378 | 2024-11-30 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5cb53267-0c24-3238-ae83-989e3bd52ef6 | -3.4791 | -53.8142 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 03bb53f2-a51a-3c5f-87ba-e876d0a67bc9 | -2.1535 | -54.8858 | 2024-11-30 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |


[Clique aqui para ver as próximas entradas](README12.md)
