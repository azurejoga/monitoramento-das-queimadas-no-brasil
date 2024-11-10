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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d933ec13-6789-359d-9833-14e638e9c18e | -2.31053 | -53.98273 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c9b6207-3bb6-3ccf-bab1-3dbc8a1a9dbd | -2.61977 | -49.79103 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e651e24-3d70-312d-9e05-011e16c32303 | -2.86566 | -49.27052 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c27e5e-ea5b-364e-a1d4-ccd2d3290c3a | -3.96263 | -49.00906 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c82488c5-bc0f-38ce-b28c-3af60a613311 | -1.937 | -52.16861 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a90cd90c-e5f4-37fe-9fd2-3fbf29413448 | -2.27253 | -50.67643 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcdd81ee-188f-3aca-97b0-ba422ff46d26 | -2.83141 | -49.44424 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09c5bcc1-381b-3bd0-87f0-b59fcefbacff | -4.10845 | -50.73023 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fc6a0e5-7c87-30c8-a960-166e64783d7d | -2.48679 | -50.14414 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 040d7200-3bd1-3475-85b8-c8e457e71838 | -2.63881 | -49.84529 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ace23a-3627-3aa1-90b3-0569d881d030 | -4.08076 | -50.42112 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4711d34-5c0b-320d-8bba-56fb9a8d763f | -2.4285 | -49.87162 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dda3d11f-b8f3-311b-8a58-e870d8b6e11d | -3.20121 | -48.66688 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c53fbfd6-6a68-3814-aef3-cb27f15d4f33 | -2.46291 | -49.78521 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58ab221e-ecee-3f88-a0c8-3f84b1e83f05 | -4.3995 | -49.41123 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13ade9ed-e9c3-3827-9cc5-a7ba23174d42 | -2.63824 | -49.84887 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0548c7d-e704-3382-aa0c-bdbefe5e80af | -3.23242 | -46.52972 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8120dc8-79d0-35ae-89b9-3b1f386a872c | -3.25388 | -48.73841 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5432d492-8eb9-36de-b116-c2bfaa7369cb | -4.10049 | -45.69956 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e26c2593-b88b-32d5-b9f9-5d5ee2d24e4a | -3.82135 | -49.85858 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d25f571-bb75-354b-8a70-acdad102ed45 | -4.4401 | -44.62328 | 2024-11-10 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 24582bdb-4462-3332-aa4a-bd127ce27424 | -5.29308 | -46.22871 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 078f7087-18c9-3680-9cb9-1f8343a3a16f | -3.38003 | -43.7948 | 2024-11-10 04:38:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21593fd6-039c-3450-826a-b7e584c13b1d | -3.30121 | -50.14333 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb7ad6e-c8ee-34dc-9735-7a74ee47fd7f | -2.8156 | -51.80684 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62e83895-4c35-30cc-9f1b-9b5c73f9afd1 | -2.59817 | -49.26766 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17490aee-c3c0-35e5-8671-2c96b8d9b908 | -2.96461 | -48.01764 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eb795bc-1f2a-3da8-a84e-d0b7555bd9d9 | -4.1038 | -49.12311 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a5454a39-0f1f-3962-b825-167e2010912d | -6.73475 | -40.81566 | 2024-11-10 04:38:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b100eae-520f-3a54-bce2-9b1ef42af2e4 | -2.83921 | -49.43827 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01622290-e2d4-3960-b555-df9499d1647a | -4.19733 | -48.55043 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d4ab1f2-eda6-376b-bd83-a3e406e64942 | -3.48154 | -48.24058 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8067439-11a1-3514-aa17-64aaf1f5201f | -2.67605 | -51.81715 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0040daf-346c-3ef7-9cfd-e19af9816224 | -2.1085 | -51.09502 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d87b11e-ed10-3b50-b7db-c79dbe181643 | -2.90088 | -54.01855 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0aa0bb55-ca2e-33d8-91dd-57feae43354d | -3.24513 | -46.49314 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 141847ad-2b27-35dc-b504-1e4e8de4cc2b | -3.09829 | -51.04181 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ea47022-8175-39fb-b1a3-66590a05643b | -8.40896 | -44.11768 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb10a50-6981-384a-9396-41aa2584f8e8 | -3.51861 | -44.03397 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 5282f54a-684f-3a18-bee4-f0add1508ec2 | -8.40193 | -44.13653 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6e23404-3093-38fa-b56e-ec365db4a401 | -3.22257 | -50.28383 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3a0e2b10-40c4-3747-87c4-32ff974cb962 | -4.6127 | -45.9824 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fed28c-48b2-38f4-b94e-fb02d8d7a2ef | -8.38818 | -44.14237 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c89e269e-9253-3548-a9ce-9cfbe4dde80f | -4.57641 | -45.40533 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0962974b-39c5-3a74-aaa7-015ffc195817 | -3.02556 | -48.03834 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02a4ac1f-03c6-3390-acb0-6492f7b83c22 | -3.10163 | -49.42134 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eb63d8f6-ceff-304e-864b-ead0b310ea8b | -2.90228 | -49.24754 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3216ffe7-8692-3abb-8371-30201cfc9482 | -4.172 | -46.59938 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab116103-79ef-3dd3-a4e6-471be72262e4 | -3.8129 | -44.46641 | 2024-11-10 04:38:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e132e309-db0e-373a-ba90-3aef90077c3d | -3.9586 | -48.12633 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 76067b16-ef7b-3c22-9d34-bb51aead7d11 | -4.92853 | -48.52674 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e13a8843-0731-37d1-a0d7-8c32650adfb8 | -3.12482 | -45.96279 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5442857a-b9dd-33bc-87c0-e67db358e57d | -3.29047 | -43.54147 | 2024-11-10 04:38:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 335ac7f7-fa7d-3f3d-a87f-0b5220713333 | -7.43812 | -46.6318 | 2024-11-10 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ee0e4fd-496c-3d36-9be6-85f6d80d0d24 | -3.97152 | -48.17467 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc7a9812-6118-32c6-a974-bf04eae81751 | -5.23644 | -46.66478 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6d70246-3d8e-3d02-8e4b-76c191f05787 | -5.56527 | -47.78126 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 475ee671-9c8f-3e05-ad87-73588348aae4 | -2.91751 | -49.51867 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f094f0d-26f8-30f1-a78a-91e6229d8252 | -4.1444 | -48.25835 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e2ee22-89c1-3df8-9433-f45c0cc04ffc | -4.07714 | -46.07104 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 293d13a8-9e8f-3afb-8c02-d2dc20846a9c | -3.24813 | -50.27668 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0daf0ac-52f3-34dc-a573-5260c93c12a5 | -2.2952 | -50.40167 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ce31762-035e-31a7-b0b6-181e15955f8f | -5.81414 | -44.11772 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 34cd2c1a-5442-3b0c-a74c-ad01fc903002 | -4.2486 | -49.18899 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 697c9016-2676-3405-9957-daa65367e2b0 | -5.8136 | -44.1213 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2edd1b61-d1b0-363d-8305-4dfc705817bc | -3.22539 | -50.28801 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 231ed5a7-3be6-39e6-bd8d-006be3cccd23 | -2.6735 | -48.66191 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30f1e9b5-2fb8-3e97-93e4-cecc2a5392e2 | -2.84128 | -49.82588 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d70a064-e01a-36c2-87e0-c8e3b71bc665 | -3.66634 | -50.25958 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b2fca0d-fa3e-36e7-9a39-a8130c193ab3 | -8.38368 | -44.11383 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c9ce5d-5907-3b97-8e02-f2fe1fd3357d | -2.92587 | -49.50918 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b9471c-8602-332c-8244-07819b25f39b | -2.23071 | -53.77993 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf535255-b779-3160-b6c6-d94c7bdcdee8 | -4.1815 | -48.79936 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60191270-a9de-3df3-b766-74b2e6149649 | -8.85363 | -47.69834 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93f7e437-6541-31d1-aae4-cf0a6eb64818 | -2.91348 | -49.34933 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44a3f576-3b7d-3cff-899b-cd6f244a39f3 | -4.26783 | -46.92075 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af016f3-3b79-3417-80c6-84f0e625cec5 | -2.5802 | -48.18142 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06245bb7-28b1-3a82-872a-477a1bbe655f | -3.02512 | -54.20626 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 645e41e0-69a5-3e2a-899a-e509cc7fe321 | -3.76096 | -52.66569 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64049cee-d180-3f4a-8115-3a85be5e7da4 | -3.22315 | -50.28019 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4950c506-8fb9-3a68-8626-96321633540e | -2.2537 | -50.44972 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3ef92b-8af5-3401-ad5b-13b21d5bd97f | -3.95147 | -48.15018 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7ed0e26a-5704-360a-b8d4-fcc95e57716e | -2.14445 | -50.71231 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bb06c90-09dd-3a69-8228-cc28f793e023 | -2.86431 | -50.31859 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4141387-cea0-35e5-99f8-3074f59a021a | -3.21908 | -50.30574 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee15f704-49b0-33e8-8cc6-a2458a1866b0 | -2.89673 | -49.26094 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3960efd1-22b3-37ce-b5f2-121c68237033 | -3.61259 | -51.21115 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b6c6bb3a-49a8-3444-b403-a3a03d2ed5ee | -4.17643 | -45.96216 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f94f1a7-839f-32ac-b1d9-31e51ac2438d | -2.83197 | -49.44073 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36cf9473-c9e1-383e-84e7-1dc6bdb7845c | -3.58176 | -50.41784 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff5cc98-8825-35bb-9fa4-daaa8c0e9b1f | -3.23336 | -50.28181 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b8cac16d-d2bf-3615-8812-9acffc52decb | -3.13935 | -50.43678 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f28fd3e5-58de-30e4-951b-2d594320273f | -1.95788 | -53.06706 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1e9325cd-4341-3a66-b5bb-7c391526ae37 | -2.56773 | -48.26075 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec984f2-a737-3759-a96b-f6da738a61e8 | -2.67946 | -48.49672 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd5ebf31-06d2-39a3-9dfe-398ff0dea376 | -2.39886 | -49.07264 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62ed1069-333c-36c1-804f-02541174bdf6 | -2.93256 | -49.51023 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc226518-a815-3256-ba89-3da1a383e2eb | -5.22208 | -49.68722 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e19089ac-ea2f-3b43-a4c5-7d0c6b3cb39d | -3.24176 | -48.75065 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8d2824-9342-32c4-9ef4-09c9dd44f205 | -3.81012 | -48.96392 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README89.md)
