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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac993068-0e24-37a2-857a-17dd3964e78e | -5.2156 | -44.9058 | 2024-11-23 00:00:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 813959c2-5f64-3969-9e11-db2459bcca8e | -4.5907 | -46.478901 | 2024-11-23 00:00:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a171bd2-aeec-3803-92d7-289307d71619 | -4.4135 | -44.108002 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ebca07b-da7f-3e63-ac19-4f2658315c78 | -4.406 | -44.120201 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6280723e-a160-32fe-9ecc-67181569e2cd | -3.9971 | -43.714802 | 2024-11-23 00:00:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06ec706f-c78f-37c3-a056-806b745ecdac | -2.7182 | -45.6968 | 2024-11-23 00:00:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6738e8d-a59e-3656-a3e4-a195231266bd | -2.6945 | -46.274399 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee2c17d9-cf07-3fb1-8e82-02d74e81e2f0 | -4.6579 | -45.670898 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1894c7c3-f792-3774-a049-cfa70c1c46ea | -6.2518 | -43.562599 | 2024-11-23 00:00:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0075e23-1948-38c9-ad1a-80655f759b41 | -3.1658 | -45.727901 | 2024-11-23 00:00:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f1d49ca-aa9c-391c-bdca-0fc173e9742f | -4.1071 | -42.466301 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0df8928-de49-3f72-a0b5-ca4467365c24 | -9.8173 | -39.152 | 2024-11-23 00:00:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| abb7fdd7-a607-3ef5-b24a-3b0e9dbe9018 | -9.7263 | -37.029598 | 2024-11-23 00:00:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 029f65ba-9bd5-3bcf-823b-9169acef27f2 | -5.5689 | -46.2859 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d35f298-e8a1-3ac5-8c63-1b67e48e1256 | -4.5393 | -45.875198 | 2024-11-23 00:00:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 434f7b92-41d4-340b-9f69-a809a06b722a | -4.6932 | -44.396801 | 2024-11-23 00:00:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b728640-8ba5-3766-820c-96e3b678b7f1 | -3.1676 | -44.4114 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a546dc1e-ac1e-3834-a559-5dcc74c11b9b | -3.4713 | -48.242298 | 2024-11-23 00:00:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa307ec-d411-33dc-ac7c-ee8d0b65a3ac | -4.9739 | -44.9701 | 2024-11-23 00:00:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2ce12e9-cfbe-34de-8ab4-553e0fca806b | -3.6165 | -45.682301 | 2024-11-23 00:00:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8301f6e3-5bd3-36e3-b800-2eeee209ce27 | -2.7585 | -45.921398 | 2024-11-23 00:00:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8caa9d-ca0c-328f-857c-fd066cc005a5 | -6.0322 | -39.683701 | 2024-11-23 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ac315157-0dac-3730-ba7c-3265a753fc6c | -3.6291 | -45.6926 | 2024-11-23 00:00:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7555293b-4c33-3922-8d82-87cd38f80d8e | -4.6857 | -45.8438 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f288c5ad-f0b7-3f3c-9838-3229fa84a4be | -9.6337 | -40.548199 | 2024-11-23 00:00:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab322668-7f76-3993-8ed7-16fac91ebc6e | -9.931 | -36.353901 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e381fb92-1fa5-3303-8072-669fc3d84e9a | -6.1531 | -46.677101 | 2024-11-23 00:00:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 876d90ca-3370-3cdc-b041-784d323876dc | -6.2496 | -43.552601 | 2024-11-23 00:00:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15b68a11-df28-3cad-9469-5e279f4a4567 | -3.893 | -47.9398 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f522ec09-f2b1-3fb2-8bc8-11e333202328 | -3.8498 | -43.928398 | 2024-11-23 00:00:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4348021b-5e31-33b5-9af5-57c5b45bbbe8 | -4.0991 | -42.4767 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86e87717-5957-32f5-96f5-125cd6ae3fad | -3.0835 | -45.7719 | 2024-11-23 00:00:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0bfef8-36d0-342d-b2d4-4ee5530a3f27 | -6.4991 | -47.056499 | 2024-11-23 00:00:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f23edb18-3948-3ff8-b5b3-24c2dd2bcbf6 | -4.5491 | -45.8731 | 2024-11-23 00:00:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c198294-3088-3d92-b070-0aeee6b906f6 | -3.4574 | -48.2257 | 2024-11-23 00:00:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0850840-2590-3444-9b8d-1e66bf2ed5b5 | -2.6886 | -46.247898 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16abed86-a4c7-3a60-8e60-2c6a8f955d13 | -3.4657 | -48.2631 | 2024-11-23 00:00:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70bf752a-1b49-3227-9980-b3d29fe86ff1 | -3.3465 | -43.837101 | 2024-11-23 00:00:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b25cfb5-424c-3873-b584-87f25774387d | -3.7407 | -49.9669 | 2024-11-23 00:00:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec56b16-6f6d-3952-b366-a0d34e4fa7f4 | -4.6647 | -45.655899 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7342fc84-eebb-3941-b7de-6803e251f948 | -3.8988 | -47.919601 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f235537-eea4-3e76-bef8-160694352a29 | -5.5592 | -46.287998 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a44089f-ec82-3291-8e21-16ed26c0a8a8 | -6.5798 | -38.378601 | 2024-11-23 00:00:00 | METOP-C | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 45120e76-30f8-31bf-bc92-cd36fec9b1d0 | -4.4233 | -44.1059 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d395c575-ea50-39f3-bb49-bf63b8d823e0 | -3.1412 | -44.385201 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6f7bfe-b64d-3465-9652-f6c018b38b6a | -3.4682 | -42.098099 | 2024-11-23 00:00:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f84fa29-86a8-3835-ae19-aeee86a67fe5 | -3.9296 | -47.1828 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2bd550-888f-33ee-a91e-5a0117eded47 | -3.9359 | -47.949501 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0408d0b0-98ad-3313-aa44-596f090a0914 | -3.2657 | -45.122002 | 2024-11-23 00:00:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 828b2a23-f11f-3b8f-8097-4106daf71f9a | -7.0537 | -40.419998 | 2024-11-23 00:00:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb868273-8a17-3cb1-88a4-70ce1755f963 | -3.7232 | -46.023201 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d51cc7b-3c29-379c-b28d-a6d3bacaf48e | -9.8189 | -39.1591 | 2024-11-23 00:00:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0e1c7e85-4f44-3d4d-9f39-b17080ebc145 | -2.8887 | -45.360699 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 440c8bf6-8e28-3fcb-bce3-63cf8bcb89f2 | -3.1434 | -44.258202 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4af0e766-60f9-39a0-bda4-0475a467e844 | -5.1078 | -43.169998 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d858301-1311-3cdc-8f17-3f87bf5999f9 | -5.9459 | -39.666698 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7849fbca-4f05-361e-8137-b5003cb7c8f3 | -4.5541 | -48.030701 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9dbb616-9466-339f-8a46-0a346bc85b20 | -5.7575 | -46.261501 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba36686f-d177-3be5-8d3b-df774765c724 | -3.4518 | -48.246399 | 2024-11-23 00:00:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c467d1d-49e4-3098-b508-81b701f20bad | -4.5343 | -42.902699 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f126521f-bc46-3865-b809-e39ce8f68e86 | -2.7043 | -46.272202 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf564cbe-6890-3abd-b4f4-f88a5b5883e0 | -3.1314 | -44.387402 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27c19b97-131f-33e3-ae60-a85e688b7c87 | -8.1487 | -38.247101 | 2024-11-23 00:00:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 14d4681c-9b74-3f30-bfc7-106d2a67ed3c | -4.0866 | -47.016102 | 2024-11-23 00:00:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5e17422-ec46-3100-8249-5ebd40c87614 | -6.4767 | -39.1003 | 2024-11-23 00:00:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9e16af7d-6c15-39e7-b6d4-6f0e9e3b4a4c | -4.3569 | -45.005402 | 2024-11-23 00:00:00 | METOP-C | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22444a44-2f3e-322e-a555-8f8f392462ce | -9.9391 | -36.344299 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7eb41a5-1cf7-3fb7-ab7b-d0d93573a609 | -5.9443 | -39.659801 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a8663da3-ec6d-3a01-985b-f546f7ec7311 | -3.6092 | -41.675598 | 2024-11-23 00:00:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 907910d3-3f8d-37bb-a489-4bc6527d5a9c | -3.6614 | -47.123901 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd8a5f27-97cb-36d0-872e-6feea009e44d | -3.9949 | -43.705399 | 2024-11-23 00:00:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2b16ca1-decb-33e4-a800-8ea3c801ab73 | -2.9575 | -45.165501 | 2024-11-23 00:00:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b715260-24b4-3eb4-9e7c-4def97ce38ca | -4.6704 | -45.681801 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a92111c-9020-3839-9cba-519af811d59d | -4.4256 | -44.116001 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89111f78-e26e-3b86-8b6d-e8832e92c641 | -4.1232 | -43.223701 | 2024-11-23 00:00:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbb1e46d-f256-3a01-a026-e4e931eef7f9 | -9.7345 | -37.020302 | 2024-11-23 00:00:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 2a42336e-04f7-3484-ae49-8392212fbab3 | -4.7188 | -45.483898 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5632a7-b957-380e-9a0a-7763b4c7c856 | -2.813 | -45.161598 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed02d5d7-3d78-3490-8007-12d2a0f4e2ab | -9.9374 | -36.337002 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e61d7f8a-bd88-32ce-a42d-6eb49abad764 | -3.2683 | -45.1334 | 2024-11-23 00:00:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8df7970-72f5-3ed1-9939-119abe21aa2b | -2.8326 | -45.157398 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9486d8e2-a19d-3e15-945b-7716d77dc2a9 | -3.5294 | -43.3256 | 2024-11-23 00:00:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 302a26f1-3266-3dc1-b28d-7688d817717a | -4.3818 | -38.9603 | 2024-11-23 00:00:00 | METOP-C | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f26beebd-9755-374b-8dfe-cd687339961b | -4.5363 | -42.9114 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31570a1c-38cf-3aee-8b3f-097b65e69397 | -3.3852 | -45.2892 | 2024-11-23 00:00:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d25ac8b-5642-342a-9a16-74e9653f3c20 | -4.6004 | -46.476799 | 2024-11-23 00:00:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a122d5d6-a544-37b4-9bc8-a1f655532689 | -10.5067 | -36.698898 | 2024-11-23 00:00:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35d3c4c8-5b91-3915-9a4e-a1984cb32860 | -7.0121 | -39.232601 | 2024-11-23 00:00:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d4c7c5cc-dddd-338e-a174-29145e08b574 | -8.1471 | -38.240299 | 2024-11-23 00:00:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 16ea041c-ccbd-3922-8bf1-24ea3e393d6c | -4.6834 | -44.398899 | 2024-11-23 00:00:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95b8cbd2-093a-3ccc-9bb2-3afce67cc61a | -2.9375 | -45.623501 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f731c989-0fad-39ac-8056-3a0ea7b710b6 | -4.55 | -48.011902 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd0e453-06f8-36c1-a2e0-2c8d5b1cf348 | -5.1293 | -47.028599 | 2024-11-23 00:00:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61c14d05-bd60-3e25-9822-46f400973482 | -4.6887 | -45.857101 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8126560f-20d5-3cd6-9728-44b1e483e21c | -4.1053 | -42.458199 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f89e6671-c6bb-3c47-8446-25dd9a093503 | -2.9503 | -45.178902 | 2024-11-23 00:00:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3db895-74f8-3577-a7cf-11501dabb3ca | -4.2637 | -46.293098 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3230b2a-b43c-3682-8b71-58d58e60527d | -9.9293 | -36.3466 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b92dc55-4d68-3f39-8cbf-10cd95062b06 | -5.5824 | -38.977798 | 2024-11-23 00:00:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b7d91920-dd7b-3980-ae7e-809c2a37d9d4 | -5.231 | -45.115002 | 2024-11-23 00:00:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
