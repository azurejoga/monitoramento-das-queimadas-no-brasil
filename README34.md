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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9255aa8f-2627-347b-a4b5-98a9c341595b | -4.53589 | -42.91117 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a917a656-1572-3de0-8c24-9eee8f8c1b54 | -4.85022 | -49.36251 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 342d42ff-d841-374b-92a3-c7189ceeffb3 | -4.70056 | -45.69832 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0e565bb-8661-3595-9363-1f263fa048ed | -5.19096 | -49.15868 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1c1c9b05-b261-37b8-8c4f-a85a77fa0a00 | -5.11441 | -46.16864 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10e40f05-9788-3ae7-b944-d7fc18d480e5 | -4.40576 | -45.90038 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6715785c-acd0-3ed9-8cc5-18efe256cd61 | -2.66005 | -46.13794 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f159f5-d9fd-332f-8722-ceea5f84fac3 | -2.01548 | -46.30009 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae8b087b-d5a6-32d7-a922-2fd0d46e699a | -5.49725 | -46.24975 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3688751-1f11-3cc6-aa3f-b5ffe9e763f8 | -3.08992 | -51.32781 | 2024-11-24 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ff32883f-9326-3e54-a25a-0af7589b7ce0 | -5.79238 | -42.47313 | 2024-11-24 03:57:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e366cfcb-c0ab-3940-82d7-9b36ba3e7a57 | -2.64206 | -46.85723 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66a2f886-e0ce-3e9b-8c46-432e641f2692 | -7.64194 | -37.99796 | 2024-11-24 03:57:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 49b3e451-29a1-3c80-ab27-fdedf8618710 | -2.28978 | -49.20578 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d15ee5f-6f67-3d7b-87cf-255c9c6197c8 | -3.84057 | -46.01853 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe9fa51c-b229-37fd-9c07-dfd3a3c9ae52 | -2.69679 | -46.28246 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fad4e7ad-9493-3dcb-ba32-87571b18dc24 | -5.10294 | -43.15874 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 52cac34f-6451-3db2-8b2c-cdd1ae390da5 | -5.1909 | -49.15428 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5cb46425-7273-3dd3-9b2f-aa19467c2049 | -2.53905 | -46.40065 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 419032d2-0a4e-3fe3-a847-ae47acf1ac00 | -3.96784 | -46.73152 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e6488df-cebc-3063-8d8e-864e26ea0977 | -2.95617 | -45.79588 | 2024-11-24 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6f44e58-306e-3b98-891a-f72abc2bcc75 | -3.60282 | -47.51352 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6fa5a9ca-cf40-3c74-8e7d-cc11a404586d | -3.69593 | -42.31096 | 2024-11-24 03:57:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51a1d944-ac7a-3720-a77b-c9de0cda5ba1 | -4.49718 | -37.85999 | 2024-11-24 03:57:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a375066e-0b2d-39b9-97ad-976dc4b2a810 | -3.12973 | -45.3784 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e762eb4-0a9d-39ac-a860-11232c54a4c1 | -5.46847 | -43.23409 | 2024-11-24 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18bafff3-b1df-3036-8830-4e3a9d24323a | -2.27613 | -47.97734 | 2024-11-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd2eb33c-b9fc-338d-a80d-ac3993b16b74 | -5.19031 | -46.14279 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f206120-f1d6-32f3-a4db-1fd3a6a47cb0 | -3.83605 | -46.01777 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6026564a-1076-3e5a-9a7a-e61d3e300a33 | -4.58359 | -46.38837 | 2024-11-24 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eaab2711-4e79-392d-bf46-f3ede7651bca | -2.67085 | -46.15973 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ac48a8a-0de0-3e3d-baf1-8716525c6e21 | -4.69621 | -45.69757 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75fd3921-6651-39fa-a765-8c843c82b73a | -2.93351 | -46.69523 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b798264-15fa-35cc-8a35-47e07d9c4b7d | -4.19068 | -50.69421 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d0276df-7e89-3a10-ae81-86af9c33181d | -2.91274 | -50.32262 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90af5584-8f70-343f-8f1e-2468694fc63c | -0.88215 | -51.72743 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b860f5-1a83-3b56-a0e1-af5c8cd08e7a | -4.23021 | -44.63646 | 2024-11-24 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e36dc0c6-63c5-3337-a411-62c27f03426c | -2.55321 | -46.55735 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f687cd6-60f4-3586-aa09-71a0130288ed | -2.9147 | -45.36845 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aefbddb-80fa-3fc3-ae39-b3327d9bcf71 | -4.07923 | -46.83313 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c4c999a-ef78-300a-a374-f6fda2f7a399 | -3.29265 | -45.72588 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 433ad50c-1b85-35b4-9ace-fb16220829e2 | -1.94983 | -49.52937 | 2024-11-24 03:57:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04237af2-51a3-38d6-baa4-617884ab5140 | -3.6033 | -47.51063 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d38fc62-b810-363a-a933-195f1ed60612 | -4.84467 | -49.36142 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa40c0d-02ce-3842-b01b-a63614878647 | -4.21403 | -50.40913 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 33128f6f-b666-3c4e-b0c7-640f14756b5a | -3.82063 | -52.41616 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ec63f32b-e7db-3a8d-98ad-90488d6005bd | -3.68515 | -50.11529 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38d36063-952b-34d3-9231-1fc237672e29 | -2.45988 | -49.0425 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c29f57d4-3bf2-3a19-a82c-84c842d5c396 | -4.23119 | -44.6337 | 2024-11-24 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8d3843b-7276-30b6-b725-1e32022b37ae | -4.03244 | -51.01938 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c449ac-f266-378d-ac53-3ecb2310666e | -3.84132 | -46.01396 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be37376c-12d4-3399-aeda-373f61b4ec2b | -4.11704 | -49.44032 | 2024-11-24 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 176db97e-0ca8-3591-b98c-c43a124add65 | -3.35199 | -50.51786 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b38b1d7-4810-3268-98ae-df5d51458a59 | -3.86281 | -50.06065 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6538a054-5f42-350c-8f7d-4042c836282c | -2.23877 | -49.2233 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c649728-3d1c-3156-8a37-58ba09495235 | -3.6743 | -45.76986 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 047ca91b-70a5-360c-b378-107dfd34860f | -3.68053 | -47.13566 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95247a5d-3581-37b2-a1e4-093db3595531 | -2.80743 | -46.80933 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1c1ef20-18a5-3758-b780-a136870189b2 | -3.0866 | -40.05481 | 2024-11-24 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9980490c-25e5-39c9-ae95-76ac6cd0d192 | -2.64147 | -46.13502 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 771a1e57-96d0-37c8-b5c4-5ed65a40710d | -0.2529 | -51.63802 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| af3a8e38-861f-3275-87ea-96cb8ca9b109 | -3.13404 | -45.37643 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2edcde7-2134-3537-a432-8753cd9ae134 | -4.49662 | -37.86361 | 2024-11-24 03:57:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0101aed7-db30-3af2-953c-4f77d9fd1923 | -1.59932 | -52.59578 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e7f078c-c2e8-3dfd-b632-39aaf885b579 | -3.74512 | -50.01387 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2abc668-7570-305b-8267-cabf22ef9575 | -5.64791 | -35.47137 | 2024-11-24 03:57:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f69f6ea-665d-3e53-a0e3-2c8fc31fbeab | -4.34929 | -48.68018 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de0749a9-77ed-3046-b5f5-430d6b1458bd | -4.53449 | -42.91973 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e234158a-2aa9-30b9-b45b-643b2fa9a992 | -5.10335 | -45.7197 | 2024-11-24 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448703c3-5961-3826-a69f-48d34292edaf | 0.41242 | -50.86046 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| addb4700-5d98-3c22-b094-5dbfb47a39ca | -3.95442 | -50.2063 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18b89784-cd89-3107-b10f-955dc24d82be | -3.03531 | -49.45113 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0ae745f2-8b98-3b28-9c5c-b8fee2fd4917 | -4.34394 | -48.67917 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc867ff8-2ee9-35ab-9a2b-81a4cfca8353 | -2.74304 | -49.12167 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8ae3ae65-97bf-3633-b512-93ae7b571334 | -6.57763 | -42.39329 | 2024-11-24 03:57:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 91001cde-eadf-3e1a-af82-4ea96fa088bf | -3.697 | -47.1271 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d873e169-8848-3cf3-964e-711ad3ccae4a | -3.94851 | -45.99154 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08a62fff-b81f-324e-ba4a-b66813a706e6 | -6.25167 | -43.56115 | 2024-11-24 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b21a3caa-11d8-3dd0-a60e-032ddd1fbf79 | -3.29711 | -45.72661 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 853886ab-0793-3285-97b6-a1a29719cf3f | -3.77424 | -44.05123 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8d74fd1-c9f0-31a4-ae24-664cfe35503e | -5.9531 | -48.04974 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4633e6da-3836-3c92-8c8f-224d8ef9db27 | -5.10989 | -49.13091 | 2024-11-24 03:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f47fbecc-42f4-33ff-ba24-205e040aa818 | -4.23177 | -44.63007 | 2024-11-24 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c013984a-6c06-3f84-8782-72187bbf0053 | -3.61335 | -47.51229 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22a1ad48-9292-30d2-be08-8e31ae2358f7 | -4.69256 | -47.18462 | 2024-11-24 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e78726d-275e-30ed-9f21-b4dd21450c45 | -3.29099 | -49.91167 | 2024-11-24 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a7edb9c-2330-399a-8531-43fd5acb0d6f | -2.66392 | -46.14351 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30e1e080-ce2c-3422-8de0-1132e66b6944 | -3.99668 | -46.49757 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f009d55-96ec-3940-bbdf-161e4dd6e9e0 | -3.30757 | -50.03079 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11c090be-2369-3108-80d0-c8e5e90dd8d2 | -4.53223 | -42.91056 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80e0fe3-4d9c-377d-9c02-d105a2760bd3 | -3.19198 | -48.58883 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d581b1a1-7e82-363f-b932-64dc15c5a91e | -4.00509 | -45.67693 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb883dec-fd9e-3474-8a76-41cfe9d24b38 | -4.24851 | -48.70518 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afa582e9-05d6-396f-8108-573f2569aab8 | -3.84173 | -44.05269 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf727f6e-d825-3d4a-b7d3-f0be04143207 | -2.68905 | -46.27108 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39d70939-194e-3b1d-b9f1-b2a083134177 | -4.94624 | -47.80429 | 2024-11-24 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 270b762b-23f5-329d-8049-639898adf402 | -3.86105 | -50.05598 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60c02d2c-36fa-3d5c-ab34-bef3560ce69c | -1.77123 | -52.72676 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c158c6c7-deff-3d7d-a0df-b46eede0a9c0 | -2.71165 | -46.27979 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c94d691c-0a3a-33ef-a19b-426a150a88b5 | -4.23176 | -48.70585 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
