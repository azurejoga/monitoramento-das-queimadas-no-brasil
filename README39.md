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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38c3b6f6-766f-3f2d-ac6d-be87f7b15396 | -2.31193 | -47.28925 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79ed3501-a940-3d17-8ac1-c625c9a28310 | -2.06244 | -50.71969 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f5dc556-0a36-3301-a45d-2cea8ddc9a6e | -4.80609 | -45.00233 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32042fe4-5613-3bd5-9f77-b266f15d1fbb | -5.45116 | -44.82434 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c315be7-23a0-3afc-bf89-e73be587a04a | -3.24983 | -53.65126 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09730138-5635-36e2-926c-fc849d6e6ac8 | -3.15906 | -46.63298 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19901372-e267-3fce-af01-df87fca88d03 | -4.27007 | -50.85129 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2462bb3-abff-3f83-9d77-99a48feeb234 | -4.8026 | -45.00182 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c6284fb-c017-3ff4-82f6-8f47eaef85ea | -2.67977 | -46.11533 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27554a17-9ea3-363d-b631-0c29423d780c | -3.70322 | -51.83014 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afbcf197-c2e9-3d44-ad43-203baf5d4625 | -2.7232 | -46.20745 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22371795-4250-34bd-9d5d-603138de2b5d | -3.26189 | -46.45419 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c03b8ef-329b-3cea-a894-a9b270cf6ba1 | -4.04286 | -46.86637 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 352440f7-2894-3f77-90f7-346a81a948a1 | -2.81052 | -53.05347 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c843d2a-fbe5-3bda-851a-71968e38a609 | -4.04746 | -48.08801 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41ee4f61-f9f9-3fbf-a15f-8cc2b45ee8d9 | -2.11263 | -50.57494 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11189830-c2c2-3e35-90a3-ae37a1ab3ad1 | -2.85675 | -45.8301 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21327049-9770-3a10-add1-eb566614f91b | -4.50277 | -45.65697 | 2024-12-03 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e31e0172-85a6-31a1-93f4-c8d8c8d95179 | -1.17554 | -53.4281 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab330c3-2410-3d81-b220-eef306c15b4e | -2.754 | -46.11971 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6dac446-cbde-31c7-95a0-d0f90fe3cc63 | -3.29036 | -53.67005 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9c8cf417-4322-3b8d-9a03-3d62ddcf91fa | -3.13747 | -45.98918 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9292953e-6d12-3cc6-b410-aad869c29b50 | -1.74003 | -52.62551 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 814f684c-9600-3c70-8db6-9503d7ac1777 | -2.24006 | -48.80718 | 2024-12-03 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9a9fd5-79c4-3ed3-99e0-dfcc01073fbc | -2.81586 | -54.14561 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b055fd96-c318-34e9-a896-a47b6efb764d | -3.02113 | -54.03965 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f96ce65-a70a-30e3-98b3-6ff72d4fe57b | -3.90042 | -46.64962 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67e145c4-f692-3cca-9804-da60dfb432bb | -3.32638 | -46.60576 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59cc6efd-9933-3795-b45e-dcffed8c9079 | -4.1147 | -48.48077 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9be8caf-7556-34e6-8ff1-22991f7de339 | -2.69319 | -46.16015 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5b44d5-5231-33e0-83d7-f7a476d08b1f | -3.26243 | -53.6304 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 481fea65-ec46-35f7-a852-46c5243e9aae | -6.68141 | -46.38358 | 2024-12-03 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 748b04f7-7ee0-3a2b-a194-470b03a83b6c | -4.06038 | -46.81961 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b04122-589c-3fd8-9e3b-ae1494229661 | -2.80051 | -53.06038 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d358df4-cc24-37ae-a695-602d9d9976a9 | -2.59072 | -46.2718 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c86ace6-69aa-3947-bab5-00ac6266eb67 | -2.58686 | -47.48412 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e85c283-6ad4-3c95-bf15-ad9b62fe5716 | -3.93096 | -46.71459 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9842d2a-b42a-323b-a200-f776a099facc | -2.89273 | -54.16087 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 308645ec-2857-3d4f-b158-4e77adf4711e | -4.25763 | -44.14655 | 2024-12-03 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0222532c-0464-399c-90d0-26863849489f | -2.65257 | -46.61383 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 939ce82c-bc80-3986-88cd-82f1fbc6a0dc | -3.18739 | -54.33743 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2708124-06e3-3728-80a7-296c8f19bd53 | -4.94631 | -43.7794 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b0bcb0c-9f21-3741-bab6-83036bdc7c96 | -2.65798 | -46.57943 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f22abe3c-f663-37af-a387-1e12c865dbc3 | -2.65359 | -46.5858 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 670cfd62-6e8d-3221-b91e-7bfc64ba60bf | -3.26906 | -46.45175 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79266138-df8c-382d-ac15-f12de941a0cb | -3.02469 | -53.87785 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7a53428-2d89-3803-9403-8c99d584b5c9 | -4.01186 | -46.99909 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e45c9f-c7bc-3ec2-80f1-751f0ec9eb63 | -4.03781 | -46.83379 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6541a4a5-ea6d-32cd-8a57-e16385b01c9c | -3.90319 | -46.65359 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed2229f3-325b-3c2a-8735-05d7dda059c4 | -3.12637 | -45.99465 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c446bd74-34ab-37fb-ae51-6585183ea1a0 | -3.60462 | -45.59099 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ebea141-7e11-3f38-9461-e8b95c9cbe1a | -2.63073 | -46.12524 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9621f3d3-fc36-30fc-b5eb-d762f85e70b9 | -2.46798 | -54.11463 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf0ba02d-ed6e-355a-aae6-06bec52253f1 | -4.31585 | -48.21617 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af7469b1-0d27-3cf2-b7ac-84465fa60a35 | -5.69968 | -45.04498 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 324955ca-ead9-3cec-94f3-07212a03e692 | -4.0507 | -46.9915 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df6c8f0-ce3e-34af-a2b6-5cebdbe7ce0d | -2.04845 | -51.20004 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 160d0ac2-699b-311a-b967-1479ca991467 | -4.47183 | -45.72268 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f39163d-b88e-372a-b6d5-1df0dc3ee7ab | -2.56385 | -46.33492 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2639778f-baf0-385c-a927-2315afbc4c18 | -4.02982 | -46.92786 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc434aa7-99d5-3110-8310-7cf82d3d64ef | -3.825 | -46.56658 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e03c74fe-f12f-3071-a4cc-7fd75d614ae3 | -4.13035 | -44.75737 | 2024-12-03 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fbf77f0-0dfe-3961-9ed1-b3b3467566db | -4.1119 | -47.20547 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7243f0-7d51-345b-80ec-c7813342cfa9 | -2.67095 | -46.12823 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db220347-5a84-3fe5-a8f1-9329d262af87 | -6.98595 | -43.50846 | 2024-12-03 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e72a0f1b-dcf9-35dc-b98d-9b127b7b2e2b | -2.72617 | -46.29667 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ae606e-6d87-3155-bb98-412ccd3aadb1 | -3.25867 | -53.62529 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2404b225-fb65-3ce4-95e1-fd577f6ad9a6 | -4.1665 | -48.196 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be180b2e-61ee-3a36-b987-2d729f0703d5 | -4.06013 | -48.3488 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ad146a-3bd6-3af0-b274-0d21d9d29edd | -3.40274 | -50.23292 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 882f7d7e-b1ba-3773-8594-41012f95fe00 | -3.81706 | -46.68235 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ab2d9b-6fc4-3504-9fe5-f2632a05d65b | -1.87725 | -53.30404 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eec2268b-b498-3543-aae4-3ee55e8c0d41 | -3.80835 | -46.54271 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1546e6ef-4b7f-3bb5-8680-42163632c020 | -2.55469 | -53.41054 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09bb88ea-fb69-32de-9567-7781375d4f95 | -6.12195 | -43.96317 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 68ea252f-7aa2-3863-9b81-7bab2b0b4217 | -5.84384 | -44.7859 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d21cd67d-5801-34b4-9a9f-f50ea535bb23 | -3.81167 | -46.54323 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f0ae66-d657-3c5c-8d53-85b39178aebe | -2.41597 | -54.15453 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e98e3a8-91c2-3e3e-b1fc-c85d9f69e211 | -2.72627 | -45.2058 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ff6a485-f2cb-3e88-b3b0-2638fc2f3116 | -1.74192 | -52.624 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51753f7a-b058-3b48-9645-8dad395280a0 | -4.08202 | -47.35236 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e962a4-e3c0-3c9d-ac5b-59cdee4897c0 | -3.25104 | -54.21548 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 075405a3-eb37-3ffd-80aa-8e913e29ec82 | -4.04991 | -46.82153 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 582f586c-42b7-31cd-bfbd-5c67343a6516 | -3.96472 | -48.82925 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f4d8215-44c1-35da-861d-7542fa617016 | -2.71574 | -47.55066 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af0330b-007f-35e2-9db3-9b6a6c8d9b25 | -3.69928 | -51.82953 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ead5b466-202b-352c-9d54-ba27ffdfd113 | -2.26338 | -46.30199 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a374904f-d7f4-32d3-be9c-11c5b5a1e05d | -2.80552 | -53.05692 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 724aaa41-8b51-3d1b-b5bf-4e6b08141016 | -3.14602 | -50.34142 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c74200-89a1-3e86-8d7a-978fcbf0dd34 | -4.049 | -50.57208 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 255e2d72-9565-310e-87d7-85c93c65e112 | -3.29367 | -47.03083 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a05254f8-7ed3-324f-8dc4-eb098c84e8fe | -4.8037 | -45.43158 | 2024-12-03 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989a2237-1fde-30ce-be6f-9a2cad93f0ed | -2.81419 | -53.05831 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adcecb0b-86a2-3baa-9dbf-e76c29fca884 | -2.67242 | -46.61691 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7722ce67-e260-3ea4-942d-fedf3da6bfbf | -4.41954 | -46.15055 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc350537-6017-3e0f-9aee-0b157bb454d1 | -2.86 | -53.99344 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a00389c-9844-31e0-85b8-ae123fb35b8e | -3.24283 | -45.37713 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 960c5423-e0cb-3875-8bad-b6f2b977c579 | -2.85389 | -45.39624 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bf3a1039-6a33-3f18-9678-f9aa3c0dff3c | -4.03733 | -46.85844 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aea2e7ea-94be-3164-8bc2-cada32497b1f | -3.40194 | -52.87943 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
