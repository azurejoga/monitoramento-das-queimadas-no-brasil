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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e54295a-3a93-34f1-9e9d-b55c313e59f8 | -3.77773 | -49.25529 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd780ae9-5dc5-3c91-b338-eb6dc5938e4e | -3.64894 | -50.22813 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50563364-14d7-3f06-9ace-302167c9914c | -6.7183 | -42.9357 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01e134a2-4f60-37b6-bdda-c81d7fd5103d | -4.31249 | -46.0041 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8caeb2b5-cc08-3493-af6f-6d419004ae7b | -0.91607 | -46.84133 | 2025-11-17 04:38:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf20b12a-2624-373c-a313-470e84ee1a8f | -4.5345 | -46.40064 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a865fc7-45cb-3321-8e3a-eb397d88f80d | -7.12831 | -41.65471 | 2025-11-17 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cfa9f7bb-e4e2-3333-bc69-7c1e7d5b2f03 | -3.34938 | -51.37502 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41a1a333-7a19-3fe6-bb2b-9e3138cda3bd | -3.5244 | -50.53268 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1da041de-9e53-3358-b47a-bfae25a5f1b9 | -4.30893 | -45.88906 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91654c76-f66c-38d8-b386-f89ee7758d4e | -4.7673 | -44.42348 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e461813b-0396-375a-83dc-cbf12044bc07 | -5.61708 | -37.8074 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| affcac1e-b3d8-3424-9a01-a57565a4123c | -8.09956 | -46.05282 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8cb06a7-ff24-3885-bd20-c30b193197e6 | -4.65855 | -46.54455 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb0fa3a-7255-360b-803b-dae42c1799be | -6.21956 | -46.98535 | 2025-11-17 04:38:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d25bb99-b7f9-3dd3-a389-8723c6d1894e | -8.32948 | -45.41171 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aadc0046-b93d-3d09-97b5-ca34f925d26a | -5.49489 | -41.38633 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 827a5790-523d-3b6b-b0e3-f67e351afce3 | -3.51452 | -53.03488 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96f249f7-f950-3028-b1c7-2550ae8df174 | -3.78177 | -45.68838 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28eb316a-48e1-31ea-b5d6-7330c96c0c45 | -3.33524 | -49.90482 | 2025-11-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69077440-b86d-364c-aa1b-7845aa935a4a | -4.67908 | -46.94245 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ea6cce-9224-31f6-b50f-f8f678504da9 | -4.82698 | -47.60651 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76604891-038c-3f93-ab9c-8dfe3d599c76 | -2.2073 | -50.82306 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74ba142f-c5bb-3313-8143-b3743f80f8b2 | -3.33002 | -50.78408 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853ae8e8-4f97-3d12-8505-f3fcc924ec5e | -3.47173 | -50.24444 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00c76cd3-941b-3a0d-9723-adec8c07bac3 | -3.59883 | -49.31189 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54467742-8641-3a5e-931f-82662da04f61 | -3.30147 | -53.85022 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8454a82c-a7f9-3229-9dde-9b4f6fd32901 | -5.73726 | -46.28073 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a50f41e5-70db-3143-acef-0a47333215fb | -3.71659 | -45.92302 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd7c3ea-5139-368a-992f-84da7b88c06e | -3.68744 | -50.5428 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61d43072-83e1-31f5-abb6-8c4737b67937 | -7.96829 | -49.9996 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a55a1993-c044-3510-8d88-322aad861fe5 | -4.47705 | -46.63605 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f4dbf41-e7dc-3964-b43a-4de1afee16ac | -4.73391 | -46.37732 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acac5970-5807-3072-ad40-4c9f05bf28a6 | -2.64514 | -49.10187 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308813fe-4340-3609-bd22-13e4974e8897 | -8.31726 | -47.91962 | 2025-11-17 04:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5807b162-75ca-32f9-953d-2d3f313204e8 | -3.83526 | -51.20007 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5a80d8e-524e-3c74-8a8f-949db68d2ae4 | -5.68764 | -47.11217 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb61d9f4-6772-3ec4-a7ff-772f36d8983b | -5.49569 | -39.16607 | 2025-11-17 04:38:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 233ccccf-02f8-3d5e-8069-b9f2da25d3e8 | -4.69635 | -46.31235 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0235b49-d9a9-31bd-8229-3d607f1f1b05 | -7.70959 | -42.94075 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06c63d14-217f-3cd9-85fe-ebac82f8fb1f | -3.60059 | -43.60299 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76bbe7fa-d673-3769-92de-f4fa4bfc932a | -2.9248 | -51.76528 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4d281c2-e201-3699-86b7-4082c9d80261 | -5.64323 | -51.31964 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58be25b8-a3e7-3932-a69f-f776c1b6933c | -4.24168 | -49.68011 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bf019a7-1159-396e-a5db-3047a528e9a1 | -3.90341 | -45.18653 | 2025-11-17 04:38:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25f02571-1cf0-34d2-89e5-7d6021f60d29 | -6.71387 | -42.93498 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6bf74458-999e-3905-8d53-0018d5ca6aa9 | -4.76874 | -48.42367 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2a89226-456d-348e-ad9f-04bb9e22ba2d | -2.54856 | -47.458 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8dfc4d-99f2-3bf8-a074-4023aa6431be | -3.46419 | -50.11808 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab54ebe-e452-33ad-ab0e-78ec85501883 | -8.28299 | -41.43313 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8e8a72b1-f523-3b80-bce8-e73f1f1d40fd | -6.83563 | -46.65416 | 2025-11-17 04:38:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19f38d2d-c3c4-3551-8bfc-f088dad52f56 | -3.17555 | -50.64931 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 938f55f0-ea4b-37e1-9216-9bd0534850d6 | -5.33058 | -43.04258 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 049c1ce3-221c-3630-ac8a-5a0d720b486d | -2.47872 | -50.23938 | 2025-11-17 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a3d385c9-0c0c-3314-9f64-f95bd1540f51 | -3.52052 | -49.82855 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6883e374-d492-3cb7-a72b-edf1664a0c2c | -4.8416 | -45.69189 | 2025-11-17 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9903542-8b04-3a5c-8854-e20aef1efac0 | -4.40027 | -45.8344 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8994fdc4-df2b-3642-be81-bceb8da2f18b | -3.51499 | -50.3215 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b105d155-d58d-3aff-b943-514c248dbbbc | -5.41938 | -41.02349 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d361bbae-1c9c-3e03-82ad-62108dfbf2a2 | -4.65565 | -46.84352 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8d5cbf6-afd5-3d8e-89da-1a57a8951dc1 | -4.7298 | -46.38074 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f5f84468-ab1d-3940-aec4-1889560d53c8 | -3.35887 | -50.18272 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcb0cb51-4aac-370c-b14a-b73a6637f7ed | -8.41028 | -40.45005 | 2025-11-17 04:38:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b137a7b-14ac-307e-b1fa-5d9fefaab60b | -3.91567 | -45.80283 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cc47140-f054-30d5-a827-7dab18764874 | -7.619 | -42.57728 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6d7bcd4e-498b-3c9a-9cf2-2d400956a0a6 | -2.23985 | -47.86553 | 2025-11-17 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974f70a5-d4a7-37df-8151-7877a93546f7 | -3.66721 | -44.81992 | 2025-11-17 04:38:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d896a2e-b068-37cb-b7b1-ed04ace02e7c | -8.30366 | -43.94163 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b5820f9-f3f1-3ee4-8a45-c501eb2c5b9d | -3.8605 | -49.98319 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6af7272-181a-3884-8b1a-e96e0a3b33e8 | -7.08661 | -42.73824 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 77348f20-337f-3588-8e38-b2bcbd7b420a | -7.06179 | -42.2431 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 01bae2c1-2538-362f-a337-717ac39b5778 | -4.77035 | -44.42639 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ff7f6d-976b-3b3b-bc61-3207af63bdc6 | -2.51299 | -47.81645 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1b9e4111-bf87-3bc2-8f18-08d8eafee687 | -5.33119 | -43.03841 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7605be19-2f40-3532-986e-33019ba4dd79 | -5.32627 | -43.04195 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b6edd23-e93d-321c-b0ac-b20bb9859d5d | -2.6446 | -49.10532 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a02ed003-426b-35db-908c-aa15eb2e9aa4 | -6.2222 | -47.24062 | 2025-11-17 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c36f342c-5b39-363e-9dc7-92534264cb7c | -3.96544 | -44.46439 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6edb83a6-cc56-30fc-b5d9-78ea8213ba02 | -0.75841 | -48.63535 | 2025-11-17 04:38:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d00a21b5-5d1f-3964-b39f-35d957aa6c12 | -6.32466 | -46.13258 | 2025-11-17 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfd3bd7-ae47-3bc7-9694-2ee90a0b498b | -3.30549 | -50.07163 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17bb156f-9331-30d3-b0ab-cdf8d7978e2a | -3.80694 | -43.33917 | 2025-11-17 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fec83177-faee-3ab2-8ae4-0c92439ae344 | -3.32811 | -50.28887 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f444b63-79cc-3769-9575-6d4fe8990a10 | -4.66088 | -46.37906 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f43c001a-1bbe-3d47-9c11-391afab0a5ba | -2.46465 | -48.55875 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 334a442c-cd20-34d2-88ea-d1788db78a57 | -4.24662 | -48.15085 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aeccb28-bd03-3d79-9e74-53c16fa3772a | -4.99191 | -44.10179 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c19ab446-1335-3a5c-b287-0facaa3e208d | -4.64551 | -50.96783 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9b0641-8b15-3e66-9140-7d3d31244bf4 | -2.51353 | -47.81299 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 200a347b-b774-308e-8cc1-8e7267bcce2a | -4.69365 | -46.31086 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954b6d60-6fab-3899-bfeb-f6a8e07db8bd | -7.13644 | -47.13126 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47364743-7da9-3ec3-8953-78853f80da3b | -4.44312 | -43.08033 | 2025-11-17 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7beb822d-7995-3fdb-b990-aeec5f160533 | -2.90996 | -46.72232 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e655ad0-bba1-3600-9819-c65efdffc5fc | -4.1388 | -38.35133 | 2025-11-17 04:38:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df6721fa-dd53-3d7d-bdb7-e9c9e4b0c413 | -5.96546 | -47.24501 | 2025-11-17 04:38:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb8eb98-9968-3233-93bf-dbcd4d340a5a | -4.70009 | -46.31587 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1788f85-0c83-35a2-bfec-8560219f4e8a | -7.97435 | -50.00411 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70046270-15e7-339c-9633-4d665d21bedd | -4.11608 | -47.29952 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d63c1c8-9d2e-3c07-87a1-2d8003ab7ed5 | -3.1484 | -53.13818 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f69e99df-b750-399e-88fa-37f9a0722837 | -3.89322 | -50.52998 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README25.md)
