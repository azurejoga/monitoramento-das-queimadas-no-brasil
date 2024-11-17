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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c757e4d3-a76e-39c8-b932-b209814d0b65 | -3.74651 | -54.71968 | 2024-11-17 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd87df98-3463-3c7d-a48b-51da7a0986bb | -5.49397 | -46.25573 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06ca9232-30e6-35e2-820e-3e2e0c20e9ce | -2.89784 | -48.31633 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d07977ac-32c1-32d0-9595-b0037a4bb95b | -2.12224 | -48.91385 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eaad07bb-4dd8-331f-bcb4-685dda0afb34 | -3.70685 | -53.75381 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e24cc83-4293-3686-8de3-9bd2529a437a | -2.16566 | -48.33022 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1440a074-47c9-3e15-91dc-e4ee720d6ce2 | -1.13724 | -51.69585 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f33b636f-819c-3f28-b755-cb8df77066f8 | -2.93416 | -48.32563 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42c96ab6-520e-3cea-81ac-a16bd21cf080 | -2.61132 | -46.25399 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf883194-39e0-3589-a251-76303e6e18f9 | -2.22729 | -48.36534 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f73579e-624f-3d88-a137-667c242baa86 | -1.91295 | -46.56878 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c1d00198-b21b-34de-a92c-1f71842227d8 | -2.30268 | -46.44645 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e618214-a4db-3a50-8de4-5852c97e4612 | -4.22775 | -50.67968 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f031508-9d51-3506-b70c-41f2847b2edd | -4.40167 | -45.52151 | 2024-11-17 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cdbaf26-83ee-3e6e-9934-9515de530952 | -2.60883 | -46.81184 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3b6d340-bb25-3066-a6d8-4c97d443ee13 | -1.21322 | -51.79165 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ecf5ec-c234-302c-8548-2fc069c30360 | -2.13961 | -48.12548 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c21bd605-9516-397b-b8c8-cd4bebf84eca | -2.46075 | -45.60863 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 557eb31c-149f-3b69-a765-489490ca56a9 | -2.94813 | -48.32419 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47436a81-e943-3406-b99d-2000177f917e | -2.25511 | -46.87901 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e135709e-aed1-3a12-b2e1-511a463b1dcb | -3.24206 | -43.43147 | 2024-11-17 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19470b0e-f653-3abe-bcda-615d7fffd31c | -4.4617 | -42.93372 | 2024-11-17 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27eef931-e09c-3cf3-a06d-db51fb0d41f0 | -3.87638 | -46.65699 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d41511bf-c3f6-34bf-9fc5-aa32dab6816f | -2.82987 | -46.65943 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ec5307b-4540-3b84-ba03-2e775e66c369 | -2.90902 | -48.31079 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bb09c61-61b3-33aa-b135-fdb8950abf98 | -3.35402 | -46.06528 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4737ec60-1e72-31e0-894e-9141902ed8a1 | -3.64736 | -44.91456 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a97787b-0928-3ac2-89a6-0553b85578b7 | -3.15766 | -46.60495 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5476c0d5-06f2-3036-b2d4-d32439db4955 | -2.60507 | -47.54726 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f550386-69d7-3fc9-af04-461fd031a917 | -3.89395 | -46.61 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ec42ecb-ccfa-33a4-979b-d0bff8e4df78 | -2.84137 | -42.88523 | 2024-11-17 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 00d77b03-6ee6-3622-98e9-f8114d2c072d | -3.66471 | -50.20136 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e74d71e-1a48-30bc-9f2a-4a94b4744070 | -2.91338 | -46.86267 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931d4651-64f1-3584-a19c-83fee2154211 | -2.64354 | -46.82779 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b545b54e-428d-35b9-be23-83134694c8f9 | -4.40802 | -44.31686 | 2024-11-17 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45fd758f-8fab-32f0-9413-6603c5723ac0 | -2.61226 | -46.18297 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3a2f5a4-603f-30d6-9307-ef2c4a9607e8 | -3.58534 | -50.526 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3e5516b-416a-34ca-8661-c63eec582022 | -1.9668 | -48.38811 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f92d2c6-0891-315f-9fee-05f70d552b07 | -5.54654 | -45.20036 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae2f1d32-4236-316c-bae2-f3e412c4babd | -4.55507 | -48.00291 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 293a46ba-1dce-3156-9904-7cc917eded60 | -0.16283 | -51.50296 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a51289f-08b8-3c08-97b1-0923db4169d8 | -3.38548 | -53.26543 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 007a9c22-38b1-3b71-8b34-ff3b3ef931d1 | -5.02237 | -45.00932 | 2024-11-17 04:29:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea0705c-d2d0-3c9a-8df1-3a4ecd8c2558 | -3.85205 | -46.63901 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1136b95a-b810-3625-98e7-73082922c283 | -5.58522 | -44.87246 | 2024-11-17 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 68e4a76d-a67f-3a8b-89ba-7157f23cd266 | -2.21763 | -48.4043 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50e90108-d2c7-3670-9aff-f1c114ded945 | -3.97471 | -49.92025 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea21e747-2de5-3b00-a1e7-65ecfec28d76 | -3.95238 | -46.71464 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4581cdc-58c1-30f7-8921-051b66ede6ec | -2.5362 | -46.21389 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cc1ea15-855a-3ea8-841a-394daeb4b47d | -3.91092 | -46.52349 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c11f680-b3f7-39fa-9756-aa0a94218506 | -2.6648 | -46.21632 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51a5a4c1-e9f3-350e-9617-cd2de64e4fae | -4.63739 | -50.41782 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbd958d3-d665-3f60-afcf-f1c3754923e3 | -3.27562 | -53.01741 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51dba921-1f45-31a6-899c-9bd1431baf9e | -3.91756 | -46.5245 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6891d95a-a087-3426-bc6a-efa9ad86916d | -3.61519 | -50.15294 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b851b74-804b-3253-a896-d22313571e27 | -2.45344 | -45.58926 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1b13f32-c01a-3d34-909d-161e3c3cfa11 | -2.53278 | -46.92618 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f54c892-0ab0-3a85-8017-e9052f17d571 | -3.88133 | -46.64709 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7b41c96-0735-3597-8204-ab9e3d364880 | -3.65871 | -50.606 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 832080c3-a5b6-30a4-976e-945059b49f14 | -2.71867 | -46.06762 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4cb052-4d05-380b-9eb8-14e529edbfcd | -3.62816 | -43.15995 | 2024-11-17 04:29:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 47ac8e96-1bfd-392f-83ca-bc4a9ab93762 | -3.60762 | -44.79218 | 2024-11-17 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dec5840-ccf7-320f-8cbe-b498df1279d6 | -3.9507 | -46.70374 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bab61654-1872-3dcc-8edb-f09609b54583 | -2.22755 | -46.83655 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6754530-643c-3516-b1a1-d1a4810ffa9e | -2.67205 | -46.86396 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 464f79f5-c5f1-34b8-83bd-35485d177c2d | -1.96736 | -48.38451 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f316eb70-f4f3-37da-bd70-12b27f829578 | -2.67576 | -46.81881 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb07e71-366f-35ec-9f7d-9781691cdec5 | -2.22311 | -46.8218 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7817f58b-2a29-3e38-a588-6f63a2b77ab0 | -5.66349 | -46.28456 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8d675cd-cd6d-3450-8244-1ef2fe6c14ec | -2.29937 | -46.44593 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebf5fa32-f996-3966-89ba-148d06b03390 | -3.77875 | -46.67373 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e08a5f1-9458-365d-8971-8681d16b7251 | -6.38249 | -45.69092 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb6a2b0c-419b-3037-a3dd-b2b2ca4bac23 | -4.64996 | -45.00346 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a361e11b-cff6-3b10-9d0f-2bb12510a655 | -4.69249 | -45.20093 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1db6d5-3830-323b-a034-aa4b6f92be93 | -3.71337 | -51.84441 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ec067c2-d3b6-38d4-9c73-292bb584cf61 | -4.36629 | -43.00708 | 2024-11-17 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 59825f5d-7b46-3030-afd3-5d3473e48bbd | -6.47804 | -47.50671 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e426f09-75d6-3b64-b767-f0c5f2f568a2 | -3.91473 | -49.04287 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7128aef-aff4-37fc-b44e-6707577e3c1b | -3.24784 | -51.51899 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9e8cc19-c40e-39c1-8e8f-1151cb3b6f8d | -2.29623 | -49.12569 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8187497e-e541-3677-9df0-bf7309f90a71 | -2.64108 | -46.56327 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d90ab6-a2ce-3dfe-a3c1-886dda26b5d3 | -2.62944 | -48.57121 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c52b0ad-97d8-3392-a22f-3a1189c44054 | -4.00606 | -46.52401 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7dbce8c-0d09-3daa-994b-f708729d4429 | -1.29597 | -51.74266 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d0d5aa3-1b64-3de4-a6ec-0107c2688c1f | -2.92835 | -46.72415 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e73d3c4-6bdc-3656-ad74-a29d6005ea8b | -2.32975 | -53.57565 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ef5ab2f9-9a42-3122-a33b-8143f3891bb6 | -4.02636 | -46.545 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a43643-de7d-3918-90bd-7746347e5936 | -4.20397 | -47.88032 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e8cee1b-bf12-3983-b50b-e4dda4e8a239 | -2.66806 | -46.19546 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 913e88bf-48b7-3aaa-a661-ff00268e42a0 | -2.08747 | -50.49846 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ed13d51-4627-327c-ae69-e9231b5e52f7 | -1.71216 | -46.16038 | 2024-11-17 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a19439e-273a-3c08-9306-cc2a76311b33 | -0.9311 | -51.73221 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4ee863a-90b2-308a-9545-d6b65475df00 | -5.20853 | -43.79144 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8320cb25-24af-3428-a3e3-a475296a7c45 | -3.33832 | -46.4278 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a553ed-e75c-3306-b9e0-0c73b0072447 | -1.64415 | -50.44664 | 2024-11-17 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40c1d74e-bf9d-3329-a909-138a06ca0797 | -2.20099 | -49.54949 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43bb3e27-0ab4-37c6-a552-6c01ba9a9c22 | -1.19593 | -52.05354 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cea35040-568f-3419-9d0d-389d0c8a3a7a | -2.03159 | -48.99988 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84df374e-58ef-3d30-8208-ad963d6dc27c | -2.91392 | -46.85923 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c0a804-ffed-3d34-bdce-e48db157856a | -4.2689 | -48.54174 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README42.md)
