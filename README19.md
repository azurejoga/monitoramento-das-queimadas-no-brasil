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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad09740b-300f-34fc-8e60-17d5b4121805 | -3.21101 | -54.24103 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c86c753b-d752-3633-98f5-93ec51872f4e | -2.68308 | -46.25154 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49a2264f-0a4a-3b0d-b2eb-170a2cfbb95c | -4.00709 | -49.92159 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93a5b66e-a5b7-3ecc-9c7b-fd47a58e4c58 | -4.44572 | -48.19639 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea0b39c-c51c-3490-bc10-f1860f3a92d8 | -4.91682 | -44.38436 | 2024-11-22 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84b0e152-4dea-3451-8799-44bed241ae84 | -2.15859 | -53.79064 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fdfec7f0-0082-36f8-9aa8-12086f898202 | -5.10887 | -43.1644 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c025c2d3-7cbb-3242-a72b-f8b27f770bba | -4.72011 | -41.87475 | 2024-11-22 04:12:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91348109-3fb0-3585-8848-bc6c13460cce | -2.72464 | -46.09165 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8297e387-b1cd-3732-992c-374ede822907 | -5.03746 | -39.8519 | 2024-11-22 04:12:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf0c4cd5-2a15-3c53-93ad-bcb320677623 | -1.20601 | -51.95605 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86e5ee5c-47cb-3898-be3f-94e41ddbf937 | -2.78583 | -51.40738 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29b9ac9f-91ec-3ac6-b8bd-9bc7cca88e3b | -3.46132 | -45.90285 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 94414993-e990-371f-8ced-0f1f9fdfa2fa | -4.11828 | -51.05202 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edaa7e03-1aba-351d-9a78-4742528ae233 | -1.25596 | -53.36842 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 877c81bc-d3ce-32fa-9866-3ce2d6bce09f | -1.71288 | -52.48848 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 259971ef-d161-37e8-a649-022bf6c40753 | -5.72731 | -46.18748 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d6a5172-b1ba-3698-ac30-0715eb01694b | -4.50668 | -43.911 | 2024-11-22 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6639493a-de64-3e2d-9df6-cebc758f2fad | -3.75067 | -46.12116 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efa06ab2-b181-36c4-8d25-9af3ddb7a088 | -2.4571 | -46.05062 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3790afc-7c64-3a9b-b341-ebeeb80bcdd2 | -3.00349 | -51.5524 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 976aa0a8-915c-3d4a-b4ed-57bccaaff4c1 | -2.98133 | -45.12353 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c6561973-b2d6-3e82-b946-4ddc499c687d | -3.23671 | -54.24564 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a8c8b730-4a01-3579-afe5-7284e7edc651 | -7.00519 | -45.61518 | 2024-11-22 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d5e1f83-c056-3179-a449-f6f40f877be1 | -0.81061 | -51.79391 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a6b6be9-b119-377a-aaee-e97ed0420da1 | -3.76191 | -46.12292 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b211019-735a-3c4c-add8-1e9d0fc18dfc | -2.35676 | -48.55228 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c7aad229-bb23-3cef-a402-b8435e36a824 | -3.32245 | -54.08792 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01168988-ccc2-382a-8772-c21abd15b4a7 | -3.63761 | -42.0687 | 2024-11-22 04:12:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d50f611-f820-3656-b559-6b2218461d08 | -3.83573 | -52.26089 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d87166-74b4-335f-a544-6ff3b35f35ee | -1.81308 | -52.16405 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4568c542-0b99-3382-befa-4d347be83898 | -4.68482 | -40.69 | 2024-11-22 04:12:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f8059616-fb25-3cc7-9207-0de7cc9e48f4 | -0.92234 | -51.73549 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e66e4a4d-b75e-38cb-ac6d-c63c0934c681 | -1.77107 | -53.60334 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bf2ffd8-acf6-3fa8-96b1-40a5eabaefa0 | -3.29165 | -49.1937 | 2024-11-22 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8c77beed-aeea-3e6a-841b-68061336cb1d | -5.96002 | -48.05975 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fca76c69-4eb4-3731-b393-b2af8879bc0b | -6.18708 | -45.45224 | 2024-11-22 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a555fca-6207-3542-b2ed-f80b96c25d63 | -1.88077 | -47.88361 | 2024-11-22 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c2c79e6-dbac-30dc-bd48-8c00d1f264cc | -3.84889 | -52.35302 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d25ad7e7-323e-3672-aa3c-7c1a9093f601 | -1.67242 | -47.38686 | 2024-11-22 04:12:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7772a2-807a-3fbc-9060-9904abba2198 | -4.11205 | -51.05754 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 904e6a8c-7cf9-3172-a9bc-f5978cdcb578 | -4.72634 | -43.25394 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91621860-0411-336f-a533-54a4e07ac626 | -2.52683 | -46.39931 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51a02417-2ccd-3385-ab66-73351b1b7c84 | -3.25743 | -54.24461 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fee5909-fa06-3c9d-bb77-6ee548ab64db | -2.07547 | -50.32568 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1178fa7e-f4d5-3723-9c28-b1d1dc8608ff | -3.85349 | -51.40715 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fbffa87-9bb5-3261-b3da-e1dd715f97c6 | -3.96245 | -46.72739 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de3cc95d-83f9-364a-848f-53fc92aea9e4 | -6.27006 | -44.55158 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bfc9a36f-15dd-3f93-9f29-bc641e822f42 | -3.20371 | -54.24495 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0c90c59e-ee8e-3572-950e-a8957d03642b | -3.20174 | -54.25639 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| baa4e9c9-0e94-3bd8-b4f4-aa28d5cbe384 | -0.2729 | -51.5593 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5b4cb3d-ec44-36a1-9556-97709531fc3a | -3.73479 | -50.43401 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb073acd-ed67-3ed9-ace3-658ffbfc067b | -3.85007 | -45.70626 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91b6095f-38e6-33f4-bc6e-0043edcf9a7d | -4.40304 | -44.12415 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d8c7b3-6270-30e5-b454-699ddd5f7887 | -4.00906 | -43.24851 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d430d35-60e0-339b-aeeb-4d6afa0f3aee | -3.18974 | -54.32608 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 018a05fe-ef15-311b-9687-c24af1b8993c | -0.91958 | -51.73989 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a084b7-e3ed-3333-a5b5-388a46019a41 | -3.83077 | -52.25609 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7590bf4-d6a6-3d4e-a83b-d96b8123d5a2 | -2.71632 | -46.09502 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0feaed9-39b6-3be3-ad5f-a9b50b9102fc | -4.40503 | -43.71879 | 2024-11-22 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aa9ccbc-76f2-324e-b40f-e83e5026b38d | -1.04546 | -51.74197 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0bdd349-3aac-3c5d-90dc-6f12e969bbd3 | -1.94058 | -49.52318 | 2024-11-22 04:12:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79ed7e55-a637-3388-807d-b1e6fbc71fd7 | -1.59012 | -53.80576 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e31e0956-d420-3971-a0e8-d36bc895a90a | -4.87014 | -48.21598 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3466e01f-30d1-3e69-a826-0a03767ec7d6 | -3.46736 | -45.91284 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7e9ca56-3060-352a-89ce-c8966f56d3f1 | -3.52571 | -54.64669 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ad30c6c-6001-39e1-a00a-6dd58085531a | -4.48445 | -48.11872 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159964cd-8a9d-38ca-a951-55ad595cc064 | -6.26784 | -44.54364 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| edacabaf-0a8f-37a0-a7a3-d2bf95c1093a | -2.70449 | -46.24054 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 040141ce-b09f-3e7f-ae46-1c6610b78bbf | -6.26725 | -44.54733 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 43199ddb-8121-3e8e-ba74-2bfddb65387f | -7.15573 | -40.22606 | 2024-11-22 04:12:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 475dba11-ba0b-36ae-8f04-349e43ce98be | -0.91602 | -51.7384 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d7b0414-c5e6-35cf-b876-2c52aaa2e8cd | -3.3394 | -53.30773 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af83fe7-2186-36f4-b8f3-8777e602ebba | -3.34096 | -53.33601 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc7bf783-6f1a-3333-9529-dffa27d94462 | -2.19483 | -53.65521 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d88992b3-7ca7-3220-b5f1-49e1791fbe29 | -3.51465 | -54.68492 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4ca8b12-3c1d-3e6e-992a-2d66ed3c3028 | -4.70637 | -48.2938 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea291d4d-2418-3d43-af21-1a113ecb2d95 | -4.5358 | -46.61922 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45599cb7-3b24-3f53-a031-cd89f8963a03 | -2.69433 | -46.08684 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43df8993-ee25-3f06-8aae-ee40fb3ae255 | -4.11776 | -51.05513 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abdb87a4-883f-31ee-8a3a-a0ebf3c67a0e | -3.23025 | -54.24465 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| da8a84b5-33f7-30d0-ba18-8d5fc3d4243e | -6.00474 | -41.96638 | 2024-11-22 04:12:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ba4aaba-e52d-3fff-978a-9cadea30bfcf | -1.19988 | -51.95921 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 099fe4eb-a523-3aa5-a310-167ca1ffea27 | -1.61618 | -53.27518 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b5ad84f-f887-3cf9-81e5-7eaca413fd21 | -3.22286 | -54.24916 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4147c85c-0d83-39ac-8642-27c8933f1b12 | -1.80629 | -48.77161 | 2024-11-22 04:12:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4cbabe7-4e70-33cc-b9a3-7822c73e667c | -3.66577 | -51.57156 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecec137b-a9f7-3bc5-bd21-e1157a590fe4 | -4.95751 | -45.62198 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f700644-ee76-34c6-912b-aafd1423498f | -2.35158 | -48.55596 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd32d46f-53cb-325c-8dfe-11350a948272 | -1.78301 | -45.9668 | 2024-11-22 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6651018d-a90f-3b08-8d11-181b1fe84b26 | -6.5042 | -42.18803 | 2024-11-22 04:12:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc74e74d-b9f2-3066-b5c9-72e8c60e71e9 | -7.00584 | -45.61128 | 2024-11-22 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd7217b8-a517-334d-91e8-409e76f97258 | -4.82565 | -43.69045 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 148c117e-7524-339d-baed-bfce79cadc83 | -6.19687 | -37.43405 | 2024-11-22 04:12:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 01dd364e-3377-3d9d-a66c-5fc9626f727e | -1.60021 | -53.21677 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2da71cba-9965-3cfc-b64e-7fc3eb75136c | -1.09384 | -53.16298 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5149a16f-c601-3101-aa8b-a0c18a06586b | -3.51887 | -54.68552 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a0cc0ee-7a04-3c97-84f8-f71a50056eb1 | -4.00297 | -43.2506 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17b6369-360e-3852-b470-e6f32b667ee1 | -5.44876 | -42.46911 | 2024-11-22 04:12:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b58bacb4-404e-3364-a64f-e448f9b1f1a9 | -2.5258 | -46.40142 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
