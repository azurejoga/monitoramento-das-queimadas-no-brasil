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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a1d87a8-48b9-3ca3-acb9-4917ce44077a | -3.36206 | -45.29739 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f27eec46-889b-3bde-92ce-6b2966383838 | -3.345 | -50.20461 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3819b85a-da03-345e-80e5-71a9ff45caab | -2.98981 | -48.70533 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b76ba0b-fbd6-30cf-9d59-0b43761b4690 | -4.39091 | -45.35953 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1e852b-bc18-30f9-9996-456f23612f67 | -4.75829 | -45.78534 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca0de619-b8f1-3ee2-ab71-d64b4f4db3f5 | -3.03506 | -50.27231 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02dabf35-8794-30aa-8556-8ee4bd90a6c2 | -4.37993 | -45.68357 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a0ba726-df1a-3fad-86da-36a00e93502c | -3.5667 | -50.41536 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdc042ad-8847-3318-a67e-f22ab7c3e7bd | -2.71306 | -49.54363 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e23daf24-5deb-3fd2-92ac-e95e70b86050 | -2.19196 | -49.13186 | 2025-11-08 04:55:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c68f9cd-2f94-3dc0-93ca-b88aeaffcbc9 | -1.18914 | -49.05467 | 2025-11-08 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e4042db-dec2-3486-b5af-42185b0e7762 | -3.91885 | -50.04328 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dd51692-db7b-3055-9690-0ebf6e837989 | -3.4885 | -53.31347 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc66dba4-341c-3001-a9ee-964857e49551 | -4.10574 | -47.2738 | 2025-11-08 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95012f84-96ac-31b1-9e3c-6ff64e00e376 | -3.44297 | -43.17307 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b442fb12-e77e-3307-8710-ac089f041267 | -3.01561 | -49.43731 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13e7a3b1-fae1-3cb6-b443-17bcbd0a0d44 | -3.53116 | -47.54093 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de144eb7-b473-35ec-85c1-840dec793ccc | -3.51535 | -49.94447 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c8eb6e9-1b98-365c-9720-fbc78f194202 | -3.40548 | -50.26965 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c27c63e6-2ff6-3733-bf65-e5c63a4c1671 | -2.22182 | -48.3727 | 2025-11-08 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85b32d96-6e87-36b3-b456-c2298406cfc2 | -4.89385 | -47.96434 | 2025-11-08 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e73db41-e668-3863-9983-c580144ab0f5 | -3.02785 | -50.27119 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8dad19c-80dc-337c-aa29-7042e389c799 | -3.54011 | -53.00768 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92711431-2d29-375c-a89f-d416ea56e8d0 | -4.39203 | -45.36161 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef29ee4-9280-391a-bad1-49a881424364 | -2.66392 | -54.76522 | 2025-11-08 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea0808ad-5a5c-3b15-a239-5c76a36f198b | -3.03355 | -50.30603 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aecf6f83-b100-3e88-8ac6-116537e62715 | -2.79705 | -48.9423 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32317ba6-b0df-31a9-8c25-06e1570a09c3 | -4.71762 | -42.93413 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1497db5e-33c7-3183-805b-21c3c501062d | -4.38114 | -49.67237 | 2025-11-08 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d998a92-0012-3751-a10d-e9968ff120b7 | -3.30449 | -50.05218 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b4f5c6-38eb-3610-89b7-da40e112b345 | -3.32486 | -53.36176 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e95eba4e-f77f-3ae7-887f-87614025dd27 | -3.03082 | -50.27588 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd34562b-6102-33a6-9fff-df8138707556 | -2.88019 | -54.23869 | 2025-11-08 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ef3de1d-f12c-3ae1-ab0e-d248d7e6a7d2 | -3.4522 | -49.84716 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c094164a-8c41-3123-9fcd-a6e2ffb33aed | -3.4078 | -45.43359 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61bb3ea4-21d8-3f4d-a65b-49edc1a4dd66 | -3.45458 | -48.83699 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec5c1375-a4eb-3411-a89c-e345f9b10347 | -5.39386 | -44.24293 | 2025-11-08 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fcf9d28-3abb-3122-b0ac-c18de15e7082 | -3.69013 | -52.13348 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6945abd9-a6c6-375a-ae4a-eeebbebc73e1 | -3.13309 | -49.10367 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b9f5da2-b29c-35e3-9d9e-c285e5fe3c00 | -3.47326 | -49.93093 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e3fc60d-556e-362b-8276-e42fd324b1ef | -5.90494 | -44.52942 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9513f7aa-2841-3a0f-883f-4ecb03fffa8e | -3.2537 | -50.14007 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfa7f637-b509-3122-80db-c2d32916b77c | -2.25645 | -47.87511 | 2025-11-08 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19b6ea11-6e7a-3709-a2f2-bd0c14760969 | -5.97598 | -44.17809 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d3821dc-3a79-3f83-a772-e5441d69a701 | -3.4413 | -43.14375 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7496c4cd-ee6a-3bdf-8463-c26bd94f7467 | -3.39803 | -45.43847 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5af647f6-5a30-38d0-b462-3c522f7b467d | -3.09755 | -49.25834 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12065ef6-8e7b-3843-9c6d-aa638b4edcaf | -4.59365 | -45.99836 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9deab262-cf40-3513-97e8-be63fd169082 | -3.33737 | -50.20023 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f71a3cc3-df83-34e4-b643-a01b0e300d80 | -2.19351 | -48.22625 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00d189d1-fcd3-3737-a92c-410cd73c2792 | -4.27336 | -48.3383 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b51069a-4714-3b24-88ad-e440bbdd6856 | -2.70559 | -49.54248 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90253976-ffcc-315a-9abd-421a97133090 | -3.43792 | -43.16555 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b4befec-c2f9-334d-ad74-a717ca9a6d4a | -3.64126 | -45.89059 | 2025-11-08 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b63ec8b-4edf-3c97-9e42-57e88e1d28dc | -4.82767 | -48.555 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23e067a6-8361-3c38-bf93-31fa5d4e9337 | -5.12077 | -40.76138 | 2025-11-08 04:55:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7326ee21-f5b7-324f-8c7b-f7f7220567cf | -3.40693 | -45.43924 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6273b36e-a69d-333b-ba4e-2b7431766954 | -4.23264 | -55.65968 | 2025-11-08 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f67393e-dcfd-3e2d-833d-f79dbb3908ec | -3.90458 | -52.17398 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b78126dd-32b0-3df9-9257-16674a805914 | -4.03053 | -49.27415 | 2025-11-08 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f97035a-2334-35e9-bf04-4bf824c973ad | -3.09635 | -50.32832 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4239a93-0205-394c-8331-e9dfe31d202e | -3.97715 | -46.03218 | 2025-11-08 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 769c21f2-f6cc-3674-ac3c-dabc35fb5a29 | -4.68066 | -46.39683 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01ae9ea6-40d6-3a0f-9b0c-ba34f584b287 | -4.23671 | -51.22892 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bed292c-4f65-317e-bf0b-105e697a279b | -1.67176 | -47.40535 | 2025-11-08 04:55:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c899703-2950-30d8-aff3-978008e37d6d | -4.72638 | -42.9333 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a735663-695e-3b9d-a838-f1b5092eca86 | -2.84987 | -50.46777 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d83ee865-bc3c-3b01-93ec-a17eaef67c6c | -3.49427 | -49.95908 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58816777-dd20-31eb-852d-1931a429d43a | -0.92205 | -47.75227 | 2025-11-08 04:55:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 615d3201-7772-3358-bbe6-cd6834fead2f | -3.34736 | -50.21354 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 34995a70-c164-3d8c-9e84-8faab7b8cbda | -4.46797 | -45.32856 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce8af155-e048-3b98-98a1-43287d30823b | -3.54108 | -50.39017 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24138b89-abeb-39ba-a7ae-3a327dca588e | -4.10543 | -47.27204 | 2025-11-08 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6482e94-a627-38ec-8dc6-7cad4e34284f | -4.10989 | -48.00988 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4c836ad-d9a0-3430-b1e6-8572e4a5277d | 0.90424 | -50.75003 | 2025-11-08 04:55:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1de2817-7498-3aa9-b7d8-cddcfcaef22c | -3.14761 | -49.213 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2eddaffd-d3ee-3527-98f2-51a86bdf76f0 | -4.2916 | -45.69184 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f448f2f-cef6-3431-b27f-f6a9bb60d07b | -3.58558 | -53.54033 | 2025-11-08 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 089c75c8-fd07-3757-9162-83cf62b9a84a | -3.14721 | -50.29717 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a6d1c4-82cc-342c-bc35-81050b4e0621 | -5.25861 | -47.16422 | 2025-11-08 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17414880-b3e0-3428-ae63-323e55ef3ac1 | -2.62773 | -50.07493 | 2025-11-08 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a365a34b-c15f-3e22-97b2-ac47a2378f26 | -3.01866 | -49.44244 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c71518f-4d44-3905-873d-57f4dfe555ab | -4.68365 | -45.84707 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7e24015-9edd-3e05-912f-1ca961e3591d | -3.3367 | -50.20448 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1acd58c-c374-31c6-9c05-f81f6aae502c | -3.09045 | -50.31903 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb37eef-8f68-3caa-91a9-0ff163353fe9 | -4.82268 | -48.06742 | 2025-11-08 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d9ac041-a80e-3024-97ee-13706c9a56f3 | -2.55195 | -48.39132 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d5ac3c3-eeb0-3504-9670-1eabaf715dcf | -4.63363 | -45.89799 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 449674cf-4490-34cf-9e6c-c1ad38c7adb3 | -4.68947 | -46.41035 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 594a6dfa-4630-3dd6-a46d-7899323693ba | -3.33475 | -52.56351 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0adc7fd6-9f44-32e1-94af-1d87392fb76f | -4.36274 | -45.62279 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b28c306f-637d-3f51-814d-643ff50b5ab1 | -3.14627 | -50.60937 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db588866-31c5-3f1d-a5be-f25d5228fe2a | 1.16737 | -52.6274 | 2025-11-08 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d08ebdf3-d85f-3c2a-8fe1-2dc4eaa1a3e8 | -3.55987 | -50.81129 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 920133ab-77c5-352d-963c-eb574d0acc4d | -3.65276 | -50.26636 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50094229-d6b1-34ab-b0c5-e1628148beda | -3.50188 | -50.05736 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4de04b59-77db-3e44-9c84-0648dadd0bce | -3.34982 | -53.22491 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e0196e2-d5b2-305c-a57a-5da69e6145db | -3.01559 | -49.44012 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b43b945a-ee16-3d59-b7a0-833165aa3064 | -3.34437 | -50.20879 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4a398c74-b86e-3b90-97c3-e075b13a1bfa | -4.72488 | -42.92619 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README30.md)
