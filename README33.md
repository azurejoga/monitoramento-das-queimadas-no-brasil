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
| 1ca6735f-c0e2-3b02-addd-a917bb57b9cf | -5.22843 | -44.91484 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02b20da0-291c-3a98-89e1-4fb680b33107 | -2.76126 | -53.23145 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5501d5ee-abc5-38b6-9176-a3e3c4a1fbb2 | -3.57229 | -50.54562 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 843899ae-66a8-3f6c-be1a-f4b18b4666e2 | -2.84592 | -49.81723 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c453ca92-cc12-35b9-ae41-69820486738e | -4.93783 | -43.62808 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 012e6728-6a04-3830-b625-36ba976265a7 | -4.51183 | -42.86942 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d4bdfd4-ee34-34f3-8d8d-e1feebac47ed | -7.16485 | -35.10056 | 2024-11-07 04:18:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 12f54b2c-9634-38d5-97b8-ec2d2b379078 | -4.34805 | -48.62682 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbe841ef-5bee-3bbf-9779-cc999f9fe9fa | -2.80757 | -52.95379 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6bea7dee-7d42-3d1d-9008-e06875d6200d | -4.23805 | -48.53766 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b50163e-e708-32a7-af43-fac47d3fc6e6 | -2.81929 | -52.9489 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 159bc3a3-b983-328b-a358-3e442ba60982 | -5.59007 | -45.20659 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8ce67c4e-0061-3ffa-9718-912174110133 | -2.66643 | -49.87756 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa0cad83-41b4-337c-9fd7-94db8e4fb449 | -6.73241 | -46.96589 | 2024-11-07 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73479e36-b224-37e4-ab2e-fc3ec67c1128 | -5.44725 | -43.58552 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe0bd086-a008-3514-9133-1e1a1c6e0c36 | -2.43367 | -53.66505 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e62e302-259e-3365-82fc-4f1d7cf981a5 | -3.00431 | -53.43375 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ff22518-b2e1-3987-9c89-acd710938a00 | -2.83164 | -52.90716 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5fb580c-0a08-3fdb-b365-6f7f33d2ec9a | -3.01943 | -53.44426 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 299d93c5-ea41-3349-a51a-1fd3d1d48f16 | -2.63946 | -46.77467 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8829ac6e-0d19-3e44-9e81-661094776990 | -2.82196 | -52.9328 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5daba7da-e7a0-31d5-8671-2075e9516968 | -3.11882 | -51.10696 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc8299fe-3a14-3d90-8234-69c164eab407 | -1.20487 | -54.20413 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba5f1e85-caeb-3bd8-b37e-de7000781a5f | -6.96356 | -39.82682 | 2024-11-07 04:18:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 31442b30-f830-38ca-9bb3-0d0821a14d6c | -5.49848 | -43.34488 | 2024-11-07 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 172c7c92-a3da-30c5-ad5a-590df3f0788e | -3.03835 | -49.53697 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2887a28-e520-390f-9f83-8c821a191ffc | -3.66369 | -50.2646 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7fdf3a8-eaae-3829-b1b6-75347a11b83f | -2.91566 | -49.35101 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caeef9fe-4563-330e-a64e-f4ef8015d479 | -3.30858 | -50.08739 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81dc419c-bec5-3b7a-81b9-8907955020cc | -2.82457 | -52.94988 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3d40da1-a2ef-3159-9bdc-7e638b6530bc | -5.98213 | -45.56281 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65384371-5f98-3bdf-933f-b2906bb7b692 | -2.84821 | -51.77324 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9aa68b6-4bf3-377a-9cb0-a3fc6fee6363 | -3.11637 | -54.27954 | 2024-11-07 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54c6c66d-cd85-32a2-9671-3775440c2140 | -2.83743 | -52.90498 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d63d215-409d-387f-b2a2-deaf1fdae62c | -2.43539 | -53.66494 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cba0d85d-4bcd-37b3-9ddf-1c846742a17e | -2.80283 | -49.7853 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1546a7f-f983-3844-b087-ebf262533737 | -4.5 | -42.86777 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e490f577-bcbd-3118-83cc-fa2382f24499 | -6.65197 | -47.28486 | 2024-11-07 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ac1fe3a-63c5-3213-ae91-01207077d7b9 | -1.22386 | -54.54281 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5737631a-0a72-380b-a608-09736c27bd24 | -4.60321 | -48.69477 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b755670-0eb0-3a5a-a584-bf5da7eaa415 | -2.23577 | -53.67943 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b6ab2f3-001b-3d67-a0b5-23c5ca66d2a8 | -3.24272 | -50.46471 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2f722f8a-fed2-31d9-8451-350991b47b51 | -1.3868 | -52.20163 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71ab57f9-9592-34e5-b5cd-748bbe6b6f8b | -1.06125 | -53.6622 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c27c3b5-6f5d-3333-b1ed-60cf5a967c66 | -1.05924 | -53.66516 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 576a5d2d-c896-3c21-acfd-3dcf9589c879 | -5.72329 | -43.81813 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96fbbbee-ea0e-35fb-87c9-1bfcb1947a91 | -4.66607 | -46.33545 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60e732a9-9fdf-33da-b3eb-2f0f71c941ff | -2.81873 | -52.95224 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 634c3b56-c05e-3b2d-a681-7b94745f44f1 | -3.52318 | -50.34827 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 626edd3c-ccfc-36f1-aaf0-593c76982ecf | -2.79996 | -51.49123 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c3d2a1e-f2ad-306c-82e9-8d65d2ab516f | -1.14759 | -53.7189 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 15c94f3a-7fcc-3ef4-8ed3-aad92709b305 | -3.17779 | -50.58094 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c270850-f4c1-3c9e-8d6f-fb655127ee31 | -4.92837 | -45.63176 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92c9f0d6-989b-3cfa-8112-447b2c8ca093 | -3.97191 | -48.40237 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb3c8ee3-4b43-3d9d-9af8-44af273ee5d9 | -2.83842 | -51.34904 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7f72437-4e55-3b73-a8f5-4df2493d71de | -1.55155 | -52.27367 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3773b097-5878-3b9c-9156-cb067498ff23 | -2.04544 | -53.28011 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8d08853-7ca3-319a-ad59-1f1761bb341a | -3.2147 | -50.30455 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a2a16d1-91e0-340b-a1d5-d9289aa6414d | -2.9198 | -49.35169 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c31dfbfe-09d7-3ab1-b8ad-32933f6834ec | -5.7061 | -45.95174 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7180a833-6783-3ee5-a58e-4c08c726b09a | -3.54567 | -47.38634 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c703a0d1-bd04-3614-a583-ca534f72a772 | -3.34403 | -50.25877 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 522ec802-e381-31f4-aff4-c4603b7245a9 | -3.70984 | -48.99941 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| eb75691e-9b4c-34b7-90e6-293d730c4638 | -7.77825 | -42.92139 | 2024-11-07 04:18:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2931a72f-40a7-3583-bac1-fbb1fc177aff | -3.13177 | -49.22268 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb43faf-6de1-3cd2-b951-3001bf90dc78 | -3.66874 | -50.26111 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7733c6fc-f2a8-3d98-8503-f4a6bf433af4 | -4.70853 | -43.79171 | 2024-11-07 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8345a47d-978a-35c4-a9a4-fb9e2cdd8477 | -1.22577 | -54.54198 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7817ef-5b56-3b1c-856c-52ba7b98c2b0 | -3.03169 | -53.26612 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13d72b9-2819-31d5-82c6-370f6f9ec7c8 | -2.51779 | -47.18545 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbd62ea-9e62-3894-9bc9-0118f5716d87 | -5.02327 | -46.84217 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f13db84-8465-35d1-b9e5-3b4980672483 | -1.20416 | -54.20845 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef36779d-4d26-3eed-83eb-f6f9f3151212 | -5.44447 | -43.58149 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d37ca613-5e8f-3b41-a835-040ced4459d0 | -5.04705 | -46.8501 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 464094a7-e49a-34cb-b5c7-d7b622dda515 | -2.66577 | -49.88164 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96b5f1fb-9a3e-314b-a4db-ccbce50eeefe | -2.81343 | -52.95137 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7b5c97bd-e9b6-3838-99e2-99442e349fb0 | -5.37699 | -46.43037 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bd88a44-97b1-372a-a5c6-d288e01db1bb | -1.18851 | -53.90359 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 79d4d2d0-75bc-3e54-a0ea-26718b4d0fac | -5.24733 | -46.66846 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f18679d-cd51-30a2-9908-36d544d82e36 | -4.37639 | -48.58457 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2f2aee2-7d57-3eb4-a92c-7e963dbd310c | -2.82527 | -52.91283 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937353aa-7e05-3fe3-a75e-c84381d0d303 | -2.95836 | -48.72342 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b046e4cb-ca7a-388b-a78d-a465f894c4c9 | -3.53283 | -50.29153 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda8f3b7-e1fd-33ec-ac88-c324d830598f | -4.48067 | -48.11435 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d06c318c-6fb3-3e7b-9095-d5372e3001f4 | -3.5192 | -50.34585 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61c3c70-4080-3193-8593-60a643b5cde6 | -2.84734 | -51.77864 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa4e1fa3-351d-3792-993b-9df32f8dd524 | -5.04008 | -46.84892 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 991e11e6-dc84-33c1-88f0-0f1d67b14ea4 | -2.83803 | -49.46242 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a580ab5f-40fe-31c7-8041-f0b8a40f921b | -5.59283 | -45.2106 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a33e5f-4cb4-3f1d-895c-9bcdcafaa99a | -3.32653 | -50.08612 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d41759d4-8c49-376d-9e5c-8102ce037bd8 | -6.95955 | -39.82618 | 2024-11-07 04:18:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f84f011-ab22-3967-8908-80191e097c2f | -8.50074 | -42.08298 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee859ef0-4d5e-3d79-afde-92bd374598cc | -3.01033 | -53.43122 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31c733fb-3332-315a-8019-6b6bc732f28b | -3.34472 | -50.25459 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fd7e304-137e-337b-8ea3-63ca66431fd5 | -2.82416 | -52.9195 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 882a48a3-2fe5-3f2d-8fe1-b6e02d4671fa | -8.77736 | -44.06803 | 2024-11-07 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0245116-2f32-306a-b563-f91d3540c100 | -5.1587 | -46.06127 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e6aaf9-ca7a-3215-93fc-f57c663cce50 | -3.28723 | -53.11901 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30c53135-d5ed-3ce0-9d47-62db53db65d1 | -5.24672 | -46.67227 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5709b10-c88a-31da-8635-5c2c798a19ce | -5.95302 | -44.30494 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
