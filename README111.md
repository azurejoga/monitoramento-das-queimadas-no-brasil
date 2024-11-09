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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 147f0ab2-d1b3-3b29-9853-fcde85baf7ea | -3.59831 | -47.35128 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5cea4825-9a03-3b8e-a211-96ee298f438a | -2.58252 | -53.98378 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d88c7c2c-315d-3d69-955a-985717385533 | -2.88283 | -48.29538 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f67e4a3c-2e94-3222-ac67-2c75a120e00c | -2.68335 | -51.82865 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cc11b62a-8f52-3e34-9883-ebb1510afaee | -2.23061 | -46.55419 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2153051-3c43-3933-bf2e-39ce10d9cfb7 | -1.22788 | -55.76923 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce701eee-bb48-33c2-8ad3-82706f40122f | -2.18944 | -47.95094 | 2024-11-09 05:20:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be3269a3-1fe5-3847-b051-d330558059d4 | -4.8961 | -48.61592 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e3b747e-13b8-3634-9c2a-a6dfef769726 | -2.15712 | -53.65387 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a97a742-dace-3d83-aa91-3f382c89e9a2 | -4.24949 | -47.57531 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7caedb86-dced-344c-93bb-f47702ef27af | -3.60497 | -51.24485 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7db2dd61-8897-3d67-a6df-4993422da33e | -3.89812 | -51.92303 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36f156ed-dcfc-3671-a8a8-c52e59b3250b | -3.03882 | -50.37304 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc73a3ac-bd74-3819-a0eb-51b53d74c090 | -3.23525 | -53.39448 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cf159dd-dfb6-397f-9828-44b2ee1fc160 | -1.18836 | -51.9925 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b1a3e7a-7be7-3902-9767-658b9a09cbb2 | -2.57916 | -49.13113 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eeacbcad-42b7-3c1d-8583-33e958acb8f7 | -2.80552 | -51.49469 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcbb8800-85b4-3949-bb44-02e09775751e | -3.17076 | -51.31239 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d6a3483-e7a1-38eb-9d64-bd5982103ee0 | -2.35886 | -54.75415 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17059563-af53-3258-9df9-b338a093d15f | -2.91389 | -51.05186 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dfd270c-9da4-3a40-a2ad-37c2fe70b93b | -2.87628 | -51.46962 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e6b0844-df97-3064-98ba-7f5e818f4ec1 | -2.91532 | -51.04241 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2eb5f0e-84b2-306c-8a1e-eccb2c62346e | -3.08588 | -53.88386 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8bdf633-2069-34aa-857e-be58c652cfa2 | 0.85173 | -50.17315 | 2024-11-09 05:20:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 752c2ead-4f18-385a-acf9-5b332cd42594 | -3.88806 | -50.23743 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0446cfb3-d4b0-39ec-919b-4d8b502379f2 | -1.97378 | -53.1408 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62873f75-dfbc-343f-89b2-d9265846d024 | -3.45056 | -52.7218 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df624702-6b62-34a1-a8e1-9d9878c49961 | -2.84245 | -53.97964 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eab926c5-de23-3cde-868e-aa4fd29c8824 | -3.38853 | -51.46714 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4fa1535-9f2d-3bb6-8fe8-806059348f65 | -2.92475 | -51.05026 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6de45720-ba42-3b0a-bb4e-f295b6c298e2 | -2.43308 | -53.66533 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50fe2536-222e-316b-a6a3-b6577be3da07 | -2.57212 | -47.34912 | 2024-11-09 05:20:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2adf847-f0f2-3fc3-95ec-b85c3d054726 | -2.88626 | -51.74321 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c249e21-c30a-32a0-93be-047a94d35253 | -3.91446 | -46.45418 | 2024-11-09 05:20:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b8ce290-14cc-355f-913d-ac7d47d6e3e9 | -3.58888 | -50.27766 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d01b479c-e4e0-3f51-ae63-3aa786314c62 | -2.44991 | -46.31102 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a80729d-dc92-30b0-8769-0755f52be5a8 | -3.67046 | -50.22283 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec44dab-7966-37da-b06b-c498ab2d265c | -3.74813 | -52.10313 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16cee619-4034-32fe-8ae2-553f7be86df9 | -3.03105 | -51.52748 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a5b89d-5363-3089-8d80-21f220ff2e3d | -3.5707 | -53.52804 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7370925-a043-3ae9-a7f6-201df19128c1 | -1.15757 | -52.0033 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 636bd819-23fc-37b4-b03c-7a953ab4e688 | -3.91806 | -59.11579 | 2024-11-09 05:20:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73946088-39cc-3971-88c1-77c7e8dd1210 | -2.91436 | -51.04873 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd1e35fc-cbbf-313b-bbd1-38b148979866 | -0.84308 | -53.03159 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92798ee1-3f42-3165-873b-2328a70650c8 | -3.03209 | -50.30703 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| acc6d6d4-d19c-3a7d-964d-6bc34f031474 | -3.10708 | -53.71253 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d1b6fbe-b069-3f6b-a56a-e64b82f7a60a | -3.3231 | -49.91231 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fdd2725-42d0-35db-ad51-5570189cd934 | -2.87241 | -50.32308 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25e5e69d-382d-3299-a81f-688c0da61503 | -3.11372 | -50.13947 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 719cedf6-9bab-3d66-acbe-9743c90933b4 | -3.58713 | -51.43659 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e14d1754-41ae-3f17-8473-5a88dbee475c | -1.24334 | -51.76521 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 543264df-b231-3faf-842b-f34c33df722f | -2.07655 | -52.05001 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e08a2ff1-5844-38ce-85bb-ed40f235e761 | -2.97686 | -50.30235 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45011bee-e50f-3c7a-bf90-f703e00339fe | -3.6817 | -51.30829 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93f7ee41-d4b3-384d-b892-bbd4d5346527 | -2.23143 | -48.37586 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ec0d501-efc5-372c-93dd-d40694245049 | -0.30465 | -51.72182 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62fb0514-50ca-30a8-bd9d-2171c0f5fc84 | -1.13071 | -53.60812 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff43072d-b44a-300a-a7eb-2df1b25ca09b | -2.36987 | -46.86466 | 2024-11-09 05:20:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0930ce25-ec1e-3a6a-a78c-28f945f5f613 | -2.68011 | -51.81688 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 552ce2fa-4da7-30e3-9b04-94ce527bf8c1 | -0.90989 | -52.56747 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99b9b219-7fc5-3f6d-a7a4-5bd6ea7326d4 | -3.72462 | -53.40296 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cff319a4-23f4-3869-8fbe-2779930ccdae | -2.45339 | -53.69215 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117bd431-926f-3869-8b4d-b57e4adea64d | -2.87448 | -51.48134 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 579b6715-bd58-3ee3-aaf0-fd839ec51612 | -1.72822 | -52.46474 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14d88959-2f37-3811-a468-43d2451ca1e7 | -1.77417 | -52.35314 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa2124c4-850b-3067-966e-c6ebfe98fc47 | -3.26981 | -52.74474 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dacbf173-b9b8-34ef-b51c-31e3e194003c | -3.0919 | -51.12011 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d2472e-906c-322d-bf1d-b07305f819a7 | -2.81933 | -52.96621 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c78fed7-27c3-3e7a-8a63-d77042d03785 | -1.52077 | -52.19431 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8aae27a4-efdc-35c1-a0e3-b14b996d449d | -2.20968 | -50.34431 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d710568b-1f48-3d2b-bf1f-c7c782e847cf | -3.04172 | -50.36331 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66139ce1-2b17-3f72-878c-be7dded5d0e7 | -3.76747 | -51.38506 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11aa1c99-d63f-3327-9e3c-c76c59eee7f8 | -3.25173 | -53.4058 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7fc708c-9428-3325-8987-c14de8dbbdfb | -3.85195 | -51.24163 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a5287e6-2f30-3647-a970-fbc2617968f7 | -4.07089 | -50.01621 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95805033-6dd1-3b93-b880-d7012c9020a3 | -4.62981 | -48.72316 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b1ba793-c716-36ac-9c43-7694700b9c3a | -2.15088 | -49.14236 | 2024-11-09 05:20:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d69e86b7-3218-3afd-8452-56641a0d3d46 | -2.283 | -48.74089 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5600fe9a-fcc0-399c-9b5d-71e01bce2327 | -2.31665 | -50.67143 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f31d144c-8e56-3cc9-ac8d-53113d23dc89 | -1.14889 | -51.99683 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b2c8d5d-dabc-3334-b73b-dfab07f76a20 | -2.18849 | -54.86707 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ed94266-22cd-3ce8-a719-62c22b9a6d50 | -3.38115 | -52.35807 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c6becac-037b-3fbe-8673-59a524abe0bc | -2.46256 | -53.68959 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a925efcb-3836-3ac7-85bb-f6f25c564de5 | -4.24863 | -47.5813 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 3f3d804c-ff42-3797-950e-57bd9971b382 | -2.94288 | -51.50257 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bd31def-fb23-3107-b7e6-d5d6caffb883 | -1.13133 | -53.6042 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97457c9c-dde3-3882-84af-a0a714f9efda | -2.67183 | -49.89419 | 2024-11-09 05:20:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d174d5e5-bbd1-3564-bc64-bae4e7be43de | -2.81544 | -51.81274 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b5ce1e3-5ab0-3ed0-a03e-284001a42588 | -3.58758 | -51.43361 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4adca12c-281d-3f97-92d1-7617e5b1dca6 | -3.40718 | -50.0132 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8a13db-b39d-382c-8892-3094bb76b931 | -1.46274 | -53.41974 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53080498-b746-3054-b215-089aa75038b2 | -3.83576 | -50.04545 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4112e393-8a73-3161-8a4a-6c9faec5e44d | -1.24254 | -51.77047 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5530ff9e-952a-34b1-9132-1ef9ed944762 | -4.20459 | -48.54415 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1567e26f-3622-3301-88e2-8c9a282d741a | -4.72638 | -48.96848 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e84007d-965c-36bb-8786-ff64cb61af7f | -1.13581 | -54.10286 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2f6ef11-f294-34a6-8be9-f253d77e5380 | -3.24132 | -50.45185 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b592acf9-df0e-3b54-a737-67f59d58c8a4 | -3.23572 | -53.39688 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8baaabf-2f75-3095-be93-4f518e5a27b8 | -3.54925 | -47.38164 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2926a705-ea91-34ab-a9c2-11f305193a53 | -2.22615 | -50.52617 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README112.md)
