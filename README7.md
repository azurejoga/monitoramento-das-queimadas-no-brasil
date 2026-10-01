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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea05b314-e3fe-3ae7-a6cb-f95e73fdc06e | -7.71487 | -54.80224 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fc10ee71-10cf-3454-ad45-1ed37a0fcc1a | -7.49013 | -54.98063 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2ea63724-b60b-36ca-a922-6b77bf0a4463 | -6.00142 | -53.66431 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8dbee970-c9b1-3db5-97de-93765812e566 | -3.99392 | -51.82708 | 2026-10-01 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ec2a767-c126-3707-b807-d43134c4aa30 | -6.66629 | -55.08567 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fda8ffdf-7f7e-3655-88cf-a5ef6ec71ef4 | -6.92852 | -59.28761 | 2026-10-01 00:20:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f45c1a7b-cd41-3b22-9bf6-33f0f9b781d6 | 1.72711 | -55.96625 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f73895dd-4075-3aea-bd28-ab24279daf06 | -6.76104 | -48.67719 | 2026-10-01 00:20:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1b12a900-d1d0-349e-9f69-eea418699c1b | -6.36155 | -55.21071 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b961ca3e-823a-3e55-9aa7-af9e034919ab | -6.4961 | -58.52748 | 2026-10-01 00:20:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 77c72fd8-9e37-3531-8814-81418e54a9c8 | -1.63273 | -55.12416 | 2026-10-01 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ea62d968-9a85-3840-acda-856ffc2ccb13 | -3.00903 | -54.21533 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dcfb314b-1af1-32ee-9eda-563be277d448 | -3.81116 | -51.03448 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1bfb08b3-6b94-34d3-a808-36e21ee9fb20 | -2.05475 | -56.87016 | 2026-10-01 00:20:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 74234e92-abbe-3097-b129-c68bbb429169 | -4.15322 | -48.90163 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3fd412e0-2706-3aa7-9c02-4c28e1fa0be1 | -3.26274 | -52.59424 | 2026-10-01 00:20:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8dd1a477-e525-3d2d-a61f-e0be36a0d766 | -6.37082 | -55.14492 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c2caf059-1900-3e89-bf1c-99eeed12de66 | -3.10875 | -50.28038 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 7efcb45c-57b7-38fd-8a7f-824c69ef6917 | -3.00899 | -53.88699 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ec891324-77c4-3cff-8a2e-3157e3457798 | -7.68394 | -55.11859 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7ee21289-946f-31ea-8234-b24601a0e6ee | -3.15814 | -54.09154 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 045edea3-c378-3ba1-aa79-51d9a8045307 | -3.07525 | -54.3685 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12043ade-e347-35f0-a23d-868fc747a51d | -7.59459 | -55.0718 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 73759f73-42c2-31f2-822e-b461abf936d4 | -4.0656 | -51.10379 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7712c0d3-7934-3911-8ac6-2fd2afe27cb5 | 1.12485 | -50.72996 | 2026-10-01 00:20:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 847fca22-f2bc-3d7f-923c-ad034a2904da | 1.8588 | -55.67843 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e06f1cf7-c0b8-3b62-baa2-c539f992a542 | -2.27139 | -48.75333 | 2026-10-01 00:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c7b12feb-843d-346c-bd68-3214c7c71a67 | -6.08104 | -53.30273 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5c000f38-802e-31d7-8e93-7e6d055e5c71 | -7.46581 | -55.00256 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8257186c-3d9e-31e0-b857-982a47d75a5f | -4.03033 | -54.20332 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 738a5568-0795-315b-984a-1507f66e8713 | -2.89706 | -54.13724 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 9ac27015-4088-3c7d-ad9c-d6c49954ddd4 | -3.48411 | -54.72606 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3917a8aa-9c4c-3917-8705-d74145275ca1 | -4.28078 | -50.75058 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a83c293c-d9f1-313b-b5e6-a434abee942f | -6.08232 | -53.31183 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| dfaafab4-bfe7-3f80-8b72-154241bc48a6 | -5.91124 | -53.48298 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 156ea170-e44d-33ce-bb9b-663df29b8cda | -2.55091 | -57.84681 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 29ef1995-69e4-3329-b03d-26c1ab864a61 | -3.11982 | -50.27882 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 9bd96487-36a7-314e-9737-5f0f4062474b | -6.14722 | -53.32113 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4a308a5f-606c-3e09-a117-ee0928df4787 | -3.01166 | -51.46292 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 81243461-fb2a-3b8f-ade0-9ac8668da01b | -3.03615 | -53.87696 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82feef83-9bd6-33f5-9159-1f1aaf4df02f | -3.27463 | -54.00524 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ba9a64a0-b54d-3b81-b64c-0f016685ef07 | -6.13454 | -53.29524 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6667b8ef-6f47-3f67-82ae-cf282cb2db81 | -6.34041 | -55.33112 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c2a73fa2-3b92-3a97-b4df-09826da52ad3 | -7.35261 | -55.59737 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8f0be4de-7aca-3ac9-a3ba-7473aa49dff7 | -5.87006 | -57.74804 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0537ed4c-12b3-3c88-a9fe-bdba985de9b0 | -3.18553 | -51.242 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 059599fc-0aab-30ed-8806-96cbe8407646 | -5.12616 | -48.8126 | 2026-10-01 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 98864e5d-8644-3dcc-b3d0-e10bfc57c27c | -2.5543 | -57.85163 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 74ef05a6-54c1-3cb9-8040-226779305d0c | -1.64153 | -55.12293 | 2026-10-01 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 86a80bc7-429b-3e81-b8a0-530d7d78d9a6 | -3.56621 | -51.47778 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 663.9 |
| 42fdac29-b98a-3ea0-a3a2-c902d5aaff3c | 2.08756 | -50.74788 | 2026-10-01 00:20:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e0621b60-8ff1-3d06-ae4e-9ffb7aed7922 | -4.28624 | -50.78852 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 06c2b6ae-761b-37c8-875e-688e04ac0967 | -1.80128 | -55.35321 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9634c3d-0297-392d-9b86-6dcd1c1138f8 | 1.83481 | -55.65724 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87336cfc-85de-34f4-9b23-a884a2e21ba6 | -3.48532 | -54.73482 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a51772bb-a9a8-3eb7-a4f8-51b8f2ed65eb | -5.76187 | -45.16442 | 2026-10-01 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| c3e9e891-4db1-31c3-bd0c-8d5a134eec7f | -5.92338 | -53.49327 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a9f88cf9-a38a-3042-84ce-aa9d0f4f2c42 | -3.95395 | -49.05037 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| d8e545a6-761c-3a96-9a30-2d69ea56375d | -3.85501 | -55.81173 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 78ebee8d-68ce-39fa-aa22-1f75bad3f0a2 | 1.81321 | -55.61851 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 95fd6f04-bc35-3e85-b865-294b448b608b | -3.95035 | -48.12488 | 2026-10-01 00:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 36fad3f9-d359-3d5f-9030-47c786094372 | -7.69497 | -54.72235 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7bb9ebf6-9412-3e58-b9b1-6bc0bc856267 | -5.8515 | -57.75614 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d756d7b9-8508-305c-bf59-db3ef5890afa | -6.54527 | -55.27498 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 644437ef-3c92-33af-8c9e-fcb95f02b5dc | -4.68818 | -55.91268 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 76212d24-12f3-3ad1-bf9a-9aac88decc70 | -5.12613 | -56.018 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 51d47e17-00b7-359c-a709-96b53068b780 | -4.24192 | -50.74947 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 889332f3-edf8-3f17-9703-b2f1a8ba5660 | -7.73391 | -54.80877 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0e042d0d-b4e1-3540-9008-9df9a7b93cf9 | -2.97032 | -51.0192 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6f9fe079-59dd-3945-93af-d6ff63dd635a | -6.24737 | -53.17433 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 845f420d-899d-34db-be6e-a8f677f1d5c9 | -3.48049 | -54.69975 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4f5ccd69-864b-3908-801c-f7a612042275 | -1.96224 | -50.62646 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa30964b-3169-3b9f-9534-2868be45f0f7 | -7.72255 | -54.79196 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e4d506a1-302b-3cba-9a7f-63396374c867 | -4.1247 | -53.81557 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 93e2bf3f-3e4f-3dc9-b9bf-209c7c62b848 | -7.03664 | -50.76785 | 2026-10-01 00:20:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e7ececbe-0d13-3a2d-a04b-59f537c8f702 | -3.80945 | -51.02224 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f620802f-2617-3a59-bac1-6a52899a5c24 | -7.5538 | -55.0401 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d26c8c21-8725-39c8-94ad-af736140686b | -2.96164 | -51.0334 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0c6628c5-ab45-38e5-b434-978f263e4d59 | -3.80068 | -50.61364 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 235b6de6-03ef-3c77-916a-2925503b8306 | -6.33916 | -55.32201 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d662955-93bc-38d1-93da-cf9b63a90a01 | -7.60508 | -55.70014 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8164f751-9216-3aa4-b352-8bfd88e5c404 | -3.14802 | -54.08388 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bf0e4516-29a6-3361-adad-55e25a45f275 | -6.34812 | -55.32078 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 447dc4f1-d815-38ef-8ebb-a3ece876dce8 | -4.26353 | -50.77884 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 251.8 |
| 3eb807be-46f6-3c53-8e39-dd979dcb1061 | -3.47754 | -55.414 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e5e2822-8833-3206-a453-ce740d5962f2 | 1.87483 | -55.62711 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c272a8b2-dcf0-341d-8426-c268ec8a2321 | -6.09243 | -53.38389 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92be209a-cfb0-3c78-80e9-13619c0c02eb | 1.79922 | -55.63749 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e1fc41a0-ab12-3868-9209-a15fdd3a2687 | -3.17589 | -54.08905 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bfed4e39-8beb-354b-b103-1d3bb5a37697 | 1.85685 | -55.56206 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f52d126e-900d-3e48-9561-e67854d51c31 | -6.23244 | -47.44086 | 2026-10-01 00:20:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ff63598e-9e07-3ebe-9d6e-00c47876cf39 | -3.01668 | -53.87671 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8ef3dd29-6287-3231-90f6-2fa094290ecf | -6.00667 | -49.5628 | 2026-10-01 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 7fce6c49-90d8-3c1b-a01d-9a6bd8ff4c9c | -2.8983 | -54.14615 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 17bd85df-ec1c-303e-a30d-170fe0f9b181 | -4.04404 | -54.2374 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 96bfd2ee-5498-31e7-8670-1ee4cd079b44 | -4.274 | -50.77752 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 753.6 |
| 0886173e-5603-35c5-9df5-751cc44f97c4 | -3.24434 | -50.8111 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fbaa3d82-40d5-306e-9d19-73ad9d69f77c | -3.08455 | -50.26928 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 09683f8c-ef31-35e1-849e-9b51ecf7efa6 | -4.03642 | -54.24739 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 19393c8f-dc1e-31ec-b255-0df0108690ec | 1.71553 | -55.92008 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README8.md)
