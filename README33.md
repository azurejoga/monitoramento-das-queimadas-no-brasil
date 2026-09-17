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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b048ede0-204d-3863-8654-431dbd0d813d | -2.89831 | -50.43413 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e364a0b0-ca9e-3233-978f-875550b5a809 | -2.96032 | -50.32567 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 41e3786a-fa0c-37fa-ba65-4ef19dd0ffe0 | -2.93431 | -54.15652 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f30b8fa7-ca57-3b8a-bbaa-d2c6a1f376a9 | -2.89493 | -50.43361 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5a1efb3-3194-3fc1-9ea8-c590e8c7d061 | -3.48569 | -54.71292 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 66926671-012d-32af-beb0-adf35bd466df | -1.61048 | -55.56505 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb72dd4a-d9b6-398b-95f8-77b97b450aea | -2.64254 | -54.69294 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| de9647d7-90b1-3b84-b915-d06e141319fe | 1.95829 | -50.9505 | 2026-09-17 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf47a64c-ed9d-3a86-99b8-50a0b13e5961 | -2.91133 | -50.39547 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6491d110-4840-30b0-9a1d-84d140d31d59 | -3.71163 | -51.10933 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adaf97c2-2463-36db-af91-0513a24a9c02 | -4.84329 | -43.55393 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be6ac60c-8568-36c1-98eb-acf04f7c4641 | -2.90371 | -54.16969 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49fed999-fa6c-317c-82f3-5434653a71a3 | -3.47855 | -54.70372 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7a57175-4787-3c85-81ac-096c988b593e | -3.54511 | -53.99584 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af7ea865-50e4-323d-8e1c-ee4ef21c4542 | -2.90893 | -54.18278 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cffeadb-c88b-340a-a3e4-cda31e038ea8 | -4.19098 | -49.28785 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83307be0-f916-3919-b6b1-0ea97b1dc70c | -3.42254 | -50.47441 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6136025c-8034-3d9d-80e6-a3db5d060731 | -2.89888 | -50.43052 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f7175f-1e9a-3ce3-abd9-cc0a55c929da | -4.55447 | -42.95062 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 228dd613-9a34-33d7-8a44-21f0e55eb001 | -2.95638 | -50.30671 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33132dd9-0a31-374c-88cb-f96f425f540e | -1.74461 | -55.2535 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a93f1f6-5e18-3778-949e-ac814f805f5f | -2.91976 | -50.40786 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a192639-b6f8-3a35-b6e9-b955a2d0c22c | -2.90169 | -50.43466 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa785987-d16e-3937-901d-e3bb58fd60b5 | -1.14864 | -54.16457 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eed33a3c-964a-3fcb-bb6c-abbc5cc290fe | -2.73054 | -48.68546 | 2026-09-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe643c9-515c-3d9b-96fe-182b9ebc2655 | -3.47908 | -54.69947 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba08162b-e035-3bbf-bc7b-43bd8434bbf6 | -2.91635 | -50.42953 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2ea0750-8b4d-3a30-8913-c0abcbe198ba | -3.47722 | -54.71118 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a40351a8-0b1f-3ee8-bb82-bba497faed27 | -2.8893 | -50.42534 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeccd211-2dab-3ad2-874a-73f0c6f824b3 | -2.91863 | -50.41508 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feb2780d-e64c-3c26-b7fa-9beaae0959c8 | -2.10064 | -52.05767 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62207bb9-f18a-30c1-aa35-2fff58016868 | -3.2635 | -54.26511 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a547cfe-12a5-3793-8937-ddde6b81b50c | -2.89784 | -54.18016 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22af369f-7fcc-3d31-8f5c-290fa23e3aad | -3.01762 | -51.21267 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6fde20a-91b2-3c3f-b20a-d21a5445070c | 2.51514 | -50.84662 | 2026-09-17 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f164130e-b5d9-354f-b032-ab3b2050d28e | -4.18767 | -49.28734 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59b90eb-a8ab-3e11-b52a-2d9fd5e33a47 | -2.96931 | -50.33441 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4001c948-5d75-3869-80b7-48f94fa4512e | -2.9203 | -50.42645 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a36ff968-f933-3296-b251-5c07475bdaf2 | -3.47785 | -54.70723 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc54b313-957f-3f77-b7f3-e759c144efd1 | -1.78491 | -47.83249 | 2026-09-17 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 685603c8-b5b8-3edd-b9b1-7e2d43fb95c7 | -3.50369 | -43.96328 | 2026-09-17 04:38:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5faa6a24-785c-3895-9d53-597eaf407f8e | -2.88706 | -50.41759 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d59de3-ce68-3c36-8a23-6cf0648d0f73 | -2.64319 | -54.68894 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 543eba67-1eab-3e19-b232-bf6a30d0c87c | -2.95245 | -50.30977 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17b8a010-d5dc-38f7-af20-c9ab671d0bc8 | -3.66965 | -49.18438 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1565838c-afb2-3b2a-be59-0bee6a315ac0 | -3.47609 | -54.69103 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a12f1f5c-2e05-3a50-b4e4-b4b68116934f | -2.72212 | -47.55819 | 2026-09-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72c2f936-b102-3991-adeb-27e228dc695a | -2.46732 | -54.67932 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b879cb63-e4d0-39e8-9c07-6fa1083fca84 | -3.47498 | -54.69915 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b0ed849-2926-311b-ab57-b78d3a72430d | -3.47919 | -54.69987 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63c2e23b-5f4c-30e8-a451-885d5a167848 | -3.50731 | -53.21283 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9020f3f6-ca94-386e-81e0-b73ed20b7888 | -3.37917 | -50.45312 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 914982e9-5ff4-39ad-9726-304908921188 | -3.4779 | -54.70763 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6432870-6a21-3f1c-889f-c7cbbecc69b7 | -2.97178 | -54.159 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15aa1d97-7536-3fdc-a678-59b090d0b29e | -2.96313 | -50.32978 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 15fa20fd-8898-3989-b6d1-4009bb1ccccc | -3.47659 | -54.71548 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1507757-3e3b-3740-95be-bd5c7eb854aa | 2.71752 | -60.29912 | 2026-09-17 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96f98738-825c-380b-8212-b37531185838 | -3.50675 | -53.2003 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc26134-4468-3aca-8e8b-79b8375062d1 | -2.89664 | -50.42277 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb89999e-ff86-38d0-aede-bdfc546d82c0 | -2.95863 | -50.33644 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f6c728-311a-3979-b35c-2fa91aade32e | -2.36893 | -48.42859 | 2026-09-17 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 425aacea-9b49-366c-9b2c-11eb8ae36a17 | -3.04868 | -51.27645 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a34ae55-0a51-3a2b-8d5a-2a5dd1220591 | -3.08013 | -50.57333 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7894821-726f-3b62-b0eb-0d7c4ee27a95 | -3.76616 | -51.14107 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca674bb4-1bb5-335c-8a5f-25967410ef02 | -3.50809 | -53.20803 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc516e9-8d3a-3d7c-ac69-6fa703dbf849 | -3.12859 | -52.7184 | 2026-09-17 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb116cfa-b5e3-307e-a77c-6855c72d0bec | -3.08129 | -50.56602 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a5c9727-2374-3701-bc41-322ddc74060a | -2.91525 | -50.41455 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3714ccd6-2b74-3a3f-9768-2d13edca223a | -2.97296 | -54.15165 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d711c3a4-5e5d-31a5-8160-02fc41ead3f3 | -3.63897 | -49.70683 | 2026-09-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a2f5d63-4157-3206-b5c5-df9e794d09d4 | -2.89607 | -50.42638 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f39e71e3-3986-3207-aa17-9dd07b39e55f | -3.54568 | -53.99235 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480e9b29-df14-39c2-af7b-61681575f5cf | 1.95853 | -50.97609 | 2026-09-17 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81858384-3e27-33b9-a367-649b0a31a81d | -1.14802 | -54.16854 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 92cafd8e-1fb7-3ea6-87dd-c6bb895ba241 | -1.81776 | -54.93208 | 2026-09-17 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 960acd00-df0a-39d2-97fb-185fa8a48bc7 | -1.77127 | -55.84576 | 2026-09-17 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| defad460-9634-3255-b314-f92f106a13e4 | -1.1474 | -54.17251 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 43c61529-d5c1-3dbd-90d7-3aa53be5f153 | -2.90621 | -50.42795 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce2301ea-7406-3128-9dcd-1bd6a47a24a4 | -2.10132 | -52.05341 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6dc36e9-871a-38c9-8207-e78f33c5c98f | -2.90959 | -50.42847 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4175b28a-6dd9-3ef4-af51-110277724d08 | 1.28655 | -50.89482 | 2026-09-17 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79bedeae-d5b4-33c5-a3c5-5c0b2b1b3f63 | -3.4802 | -54.71973 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a8162b7e-0119-32c8-9479-d93949575f07 | -3.47426 | -54.70259 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d440181-6233-3ce7-88ed-cf79631eb779 | -0.95528 | -52.3281 | 2026-09-17 04:38:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46f9f55b-d419-3560-b1f4-766b57893743 | -1.1969 | -54.21577 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6999590-5ad5-3bd3-a3a2-a14647b23017 | -2.962 | -50.33696 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1a22031-107e-3a0e-a6ad-9616a8ab5898 | -2.82328 | -51.33791 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9041f5-c0fe-3062-8260-a6568ca3b204 | -3.47303 | -54.71086 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9a21fe2-e9d4-3cfe-b7da-384d72639d55 | -3.55093 | -48.1781 | 2026-09-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b567aa91-dc1e-3c04-b774-f978a9f0a832 | -3.17277 | -53.92582 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c46071-50fb-3ef9-a400-0041d1f258a6 | -2.96602 | -52.15708 | 2026-09-17 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2afab3d-3c7c-39ed-a6b1-2718590038e0 | 1.25918 | -51.00368 | 2026-09-17 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acc6da16-0eef-3e9c-8632-7ad95f45ee1d | -2.90254 | -54.17709 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf65eb48-5030-3c66-b4e4-e8757e72dad2 | -2.9113 | -50.41764 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ed6334f-fcee-3e4f-b086-3c892f2e27f1 | -4.55569 | -42.94212 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c4c03c52-69f5-383f-95ad-9a6c7dbe9807 | -2.9192 | -50.41147 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7610ffa5-303b-386e-8313-c89a9835ccee | -1.03529 | -53.73871 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 22d5238a-876c-3e27-a870-6875314933aa | -3.05032 | -51.27674 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38333d10-8d3c-33d8-98a9-0c61571f4c12 | -3.48082 | -54.7158 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 89e35729-b2b4-330e-9692-9ab6187e782e | -2.90782 | -54.17031 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
