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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 893bb9ed-8d1c-3269-8bd1-2656a2a5871e | -2.93482 | -51.05222 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 12a853dc-df1e-37e9-9853-f4b7974cc8b2 | -3.33154 | -50.07741 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 865da02f-3fcf-323e-8d24-5c22d1b8dbd2 | -2.8212 | -52.9416 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0a508af1-f1ca-3bf7-80dd-15cb04eb2ebb | -3.09784 | -50.26164 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39084870-5360-3cbb-b8fa-7e6bde04012e | -3.03453 | -53.2645 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b2378ab1-ab67-3969-98bc-24703e9765be | -2.60471 | -54.53944 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceedf68b-868e-3d99-8a32-64704eb4e9d5 | -2.8266 | -52.90543 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23ca6547-f0e0-3e0b-890b-2d62bcf7d13a | -3.15377 | -54.25863 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8d9f343-d9da-3c84-880b-3dc36997b735 | -2.57866 | -51.33786 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e680c21-45ef-377d-ad2c-eba93c8e25f4 | -2.81883 | -52.92255 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6390ed54-5a93-3fbe-bf47-7aae02a7f427 | -2.8272 | -52.93638 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06b2340f-3d08-3d32-9a21-07bdca4c49c6 | -3.0945 | -50.24169 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcce1db0-e5e0-3edd-b3dd-e71e51a9623c | -2.70524 | -61.03628 | 2024-11-06 05:31:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db428a77-3ead-37b3-a053-6d077afe940b | -3.01971 | -53.43705 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7eca0738-3c97-378d-85a7-72b8cc658a2d | -9.45331 | -66.6429 | 2024-11-06 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bde5d34-97e2-36d8-9567-3b74e1935d73 | -2.79865 | -51.49509 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 817ada8c-3c10-3e55-967a-403a4659e4d1 | -10.52275 | -67.79415 | 2024-11-06 05:31:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 353b03cd-41c6-3c76-89d7-15a4cf339e04 | -3.66617 | -50.2319 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4d2ccb72-f36c-3e76-ba6d-7dcedab85986 | -2.78415 | -52.87423 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb8d44d9-5555-3537-9549-e2e07f6a5109 | -3.19877 | -51.03423 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31371492-7250-3b11-9296-fc40639498bf | -2.17334 | -53.69972 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa5bd219-964a-39b8-a7cb-67a73218c76f | -1.06762 | -62.65216 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0b822de-4a12-375c-a6d6-94af6e97231c | -2.74502 | -59.47648 | 2024-11-06 05:31:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b93b9a3d-e220-3ff8-8604-ab5a11475ee8 | -1.33246 | -54.60442 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62888d1b-9c3d-36b2-9efc-3eafeb515a5e | -2.94715 | -54.13277 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5abb9861-9bee-39a1-a344-44eaae02fb3b | -2.60739 | -51.76009 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 986e3a70-24ab-3a7b-9ddf-6ad6d3090d27 | -2.81554 | -52.90955 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9cad3a5f-805c-3c64-8d78-45f0c193418f | -1.33557 | -54.61396 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b80a8cd-0ac0-3cde-807c-be137d119503 | -3.25058 | -53.36372 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347ccfde-75cd-3b8f-ad41-fb031917866d | -3.18777 | -50.58766 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b25f65c-de99-37cf-9ea1-501b9d624dd4 | -3.16951 | -53.07411 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77b62dbe-7627-315f-8cc3-445011c3a232 | -2.67581 | -51.82954 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de1656b9-ebb2-3ded-96ea-bab2e1a0e640 | -3.02858 | -53.26908 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 56ed2c26-ec13-308c-aae8-893fc0a44bd5 | -3.02507 | -51.00335 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df2411f-1a7b-3289-97ef-52b8a28f2722 | -3.11667 | -51.11029 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6fb18d44-eb2e-397f-9e67-b8c2c303e9ea | -2.65867 | -48.56856 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a437f0a2-0163-326e-ab75-f7073efbc9db | -3.24026 | -53.39985 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca782579-13d3-369c-8deb-2200ce3c8f2c | -2.58474 | -51.871 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f15b68e-bd10-30c3-8a83-f2ef3a2c671c | -3.01137 | -53.42485 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a957b894-f955-3672-ade8-b14697feb837 | -2.84738 | -49.47562 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ccb071e2-bb53-385e-a969-20082a497bdf | -2.92908 | -51.04945 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 35e0aae8-a039-39e2-b542-678a38f412d6 | -3.53436 | -52.99688 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77a2ef4-1a8a-3fee-8659-62acb6b5c05e | -3.01396 | -53.4419 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f386e2db-28cf-302b-bc93-48cd22693a68 | -3.2046 | -51.03508 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d2ef5ff-4e65-3e6e-b918-b2bd79af4aa0 | -3.09619 | -53.72005 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 398b3b86-44d1-365f-bd50-2b704a36fdf3 | -3.10395 | -50.26256 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d822e062-8f6b-380d-bfbc-91dee5a0f8a1 | -2.5252 | -51.1688 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1cb3277-13cf-34c6-96c3-2bda9dd36173 | -2.22611 | -59.10978 | 2024-11-06 05:31:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cbdaf30-55d1-35a1-bf0d-dda2c1f1038b | -0.65273 | -62.92216 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ffc92c5-4463-3f74-b120-dc27107d5748 | -2.9117 | -51.04678 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b3a70fdc-707b-34f5-9150-c7ccc38defee | -2.85221 | -51.78264 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae54fe66-65e1-3778-b281-5270f7c45e59 | -9.44366 | -68.53304 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7cefa8-45ae-3b65-8e82-5a0e5960e751 | -3.68361 | -49.85075 | 2024-11-06 05:31:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 950dadb9-f6ca-38d2-9414-1aa2750c6f69 | -2.70248 | -61.03233 | 2024-11-06 05:31:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6b93c81-07ff-36e0-bf3e-2c9bc874348b | -3.03827 | -53.27404 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| df5d3c0e-9343-3d02-a3af-c2213e51d4b8 | -3.85932 | -52.26931 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2216cc75-efbe-38f6-a9fe-6f927ea8a7b8 | -2.84776 | -51.77448 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 28fbc2cc-7900-3b45-8804-26717eff4359 | -2.42374 | -53.66277 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8eeb9dd0-1f96-39ef-90c9-20250e7496e7 | -9.64832 | -65.74061 | 2024-11-06 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae29034b-2b0d-3f86-958a-4b8d82751968 | -3.06368 | -52.5036 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc1c99bc-635a-3c8a-a339-3f45eb6d14aa | -11.77314 | -64.98863 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a372cb3-6457-338d-a281-03df59698dee | -2.61259 | -51.30389 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d303878-43a6-3447-b0f5-a9b993ceb956 | -3.16284 | -50.20393 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f885f60c-8788-3c93-b20a-dafd83264f42 | -2.72666 | -51.71577 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7f6e71b-97c5-3c7d-85a4-86fee9276be5 | -2.92324 | -51.05044 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 86cfbfba-950e-337c-affa-eeea7fdc7fef | -3.45654 | -50.38235 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6874ab-22b0-3ec2-a3ab-19165da55a68 | -3.67375 | -50.22787 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f5ca7a7-370f-36fe-9ce6-c5d59b862234 | -3.14937 | -51.33239 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba7c614b-1fa4-3b65-99c2-e87a09555dac | -2.84099 | -52.91401 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744e3aaa-fbe0-3555-afba-c7b38ffb60ec | -2.99438 | -53.84699 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 223e6c17-a375-32f7-9710-e3cf53301416 | -2.8331 | -52.89688 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46477e70-db92-3b84-972b-4215165aaefe | -3.59813 | -51.57047 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec9def65-9eef-3b40-97b7-8287dee45cae | -3.0175 | -53.44172 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e97b6bf0-a947-38a7-b4ad-3d46a1ccf489 | -3.15253 | -51.14876 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8ddf96b-ca9e-36f9-ba6a-aefc6b227df2 | -3.8955 | -50.25043 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae1fb8f-f709-3c15-b723-7c9657f00e5b | -3.74034 | -50.06426 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb67003c-e5ec-3515-a015-4fca1b10b528 | -3.80285 | -51.95626 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f587c6ae-ff8c-3db2-ab61-91c089242540 | -3.00096 | -54.09514 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c33c4701-7077-3cbd-824e-f2a1a8280c1f | -2.8424 | -52.90459 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 88d6c195-c887-34d3-9b85-bc3e6621ec27 | -2.81927 | -52.91958 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5cb656b-b026-3fdc-b3ae-fcd97a364357 | -2.96115 | -50.99305 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ad1e555-4a9c-386e-9b55-db5993096376 | -3.1692 | -54.46949 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c0f34684-ea8c-3b33-a0e9-bb3b3e171818 | -3.2252 | -50.37633 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| dfb9d54b-86f2-3f4c-b7a2-24398d5051a8 | -2.77902 | -52.87354 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f808c21-5a0a-3603-b48d-8c396aa7e8a4 | -3.09186 | -54.54883 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47be863b-19b3-3c8c-9480-94e7f850e287 | -3.53145 | -50.34297 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ad46cde2-b5b2-335f-b869-1fb4c689f501 | -2.58431 | -51.91992 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 508fad1b-3347-39be-8b0a-f58f454639eb | -3.10595 | -50.29148 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 494ae2b7-a0d0-3100-8be6-04ec0f6a5664 | -2.82198 | -52.90138 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73220daf-fc20-344a-a98e-465e31b36af4 | -3.12777 | -51.11261 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f203bd63-18de-392c-98b6-1182339aee39 | -9.40367 | -68.9927 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b52b9776-0353-34f6-aac3-a9f68ff4488f | -3.87109 | -52.3787 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abeb12bb-fe92-3f3d-8dd0-ab37d34552c6 | -2.77945 | -52.87059 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 912b98c8-a029-300b-8f66-96f41f1e665c | -3.10664 | -50.28678 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d094fcd7-3b2f-3214-b8af-a3b836608b42 | -2.92328 | -51.0486 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62852b63-84d4-3f5f-a287-90025d94a78b | -2.75888 | -53.22208 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6a9ca141-ebca-3ea9-af38-b69815875680 | -3.01917 | -53.43076 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 05b0d148-d01d-3510-8dd2-fab366e27c6b | -3.11725 | -51.10615 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6abe79c-a05b-3670-8c2d-abd965cb388e | -4.36297 | -48.64574 | 2024-11-06 05:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 66fda6e0-54df-3e08-8e68-a08c90df9c7b | -2.60926 | -54.54016 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README65.md)
