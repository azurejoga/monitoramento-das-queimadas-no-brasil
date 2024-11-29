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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6cf539f-fdcd-3c40-8624-0438dfd829a6 | -2.83398 | -49.84668 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 973c63ad-d426-32fe-8ba0-0170f4116162 | -2.88498 | -46.84247 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19087801-e4d0-3cd2-b0cd-09b7cdc185ec | -3.1047 | -50.37077 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d027caa4-fab1-31f2-abf0-fb83aec77b43 | -4.92604 | -44.52791 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4d0ba5-c5c4-3015-98e5-3a3c60b10f28 | -3.95281 | -52.20454 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4ed85be-2e54-389a-90e4-15495155dcdc | -4.10016 | -53.98369 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0abcfe2b-28b4-3dd6-94c1-2ea2e8634866 | -5.1563 | -39.36834 | 2024-11-29 04:04:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 300a9e23-70f3-3676-b823-6c4bab197cb8 | -5.99859 | -44.57024 | 2024-11-29 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f1af8a1-c614-387a-af80-def6319365b2 | -2.96869 | -53.29659 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| c48b2c2c-18fa-3639-bdfe-f43badac8d60 | -5.22032 | -44.90665 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e92bda2-a72f-38fe-a1c8-41469646ea7e | -3.05278 | -48.52269 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2f31126-7012-35cb-b429-da4123bee119 | -1.03815 | -51.74041 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94c89048-9786-3410-a897-c40df1a6eb89 | -7.2653 | -35.15382 | 2024-11-29 04:04:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e390ca69-1068-39b8-893e-5be298bf36ef | -3.49667 | -50.46172 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae9a3ca-1fe1-3c56-98cc-2d68362e6ef9 | -5.27843 | -45.12202 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50ca119a-ea2a-3605-bebe-2860ae7c39ab | -3.24889 | -53.65026 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 783242c3-dc00-3cd6-9689-fd8e545f20cf | -3.8731 | -48.36353 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f5c6e9fd-c259-34a6-b549-f727bf2d14cc | -2.591 | -53.9746 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d14ea41-9509-3337-8574-663a11d58c91 | -2.58328 | -51.92632 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5db0872b-58be-32ec-98f8-8af42c0552cc | -2.58667 | -47.47596 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09105c65-3673-3625-b7cc-f456abd9af0b | 0.98533 | -50.12604 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 85a6f756-cd9d-3a85-9dd0-74cb96c36f72 | -3.05937 | -45.06406 | 2024-11-29 04:04:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4403f339-0964-359b-b9e2-c759a831f150 | -4.64411 | -47.14729 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29a0c3b5-4eaf-38fe-b96d-328617ca3abc | -4.22366 | -45.76808 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8986014e-313a-342d-b0e5-dcf1de128000 | 0.94633 | -50.73401 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179fcc4d-70a1-3ea7-9977-7086634cc87a | 1.32637 | -50.6804 | 2024-11-29 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d516cbd-b11c-3378-8ae7-c1d401709786 | -3.2924 | -50.36501 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c773352-8b87-3eed-a1a2-5307e1bd2eed | -2.65948 | -48.79824 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 721d5c91-a434-3744-9f2d-e4b1ab0e1ffd | -3.04815 | -49.52111 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ee8516-f0b9-3d8e-81f7-ceb829165ca9 | -3.47428 | -49.92988 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126f3e17-f7cf-3537-b33b-1621c4ce32fc | -5.50889 | -46.25486 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c4f4771-632c-3e96-9a2b-6f1064c9bf66 | -4.23474 | -45.77523 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f2ff225-c1ed-3f96-870b-22c2d4130f7c | -4.05724 | -49.0722 | 2024-11-29 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ccfabd44-474c-38ec-bb68-1f6ae7080a51 | -2.94631 | -45.72404 | 2024-11-29 04:04:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42d76462-944d-3aa5-952c-551a670c23da | -3.91469 | -53.66961 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3687311d-a5d2-3fcd-ac3d-6a2a2202178c | -5.89021 | -35.41359 | 2024-11-29 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 03656a7a-297b-3b8c-8877-dbbca2913899 | -3.44289 | -40.83296 | 2024-11-29 04:04:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6643c3f4-2198-312f-ab39-f4698d618cec | -1.65774 | -45.57332 | 2024-11-29 04:04:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96e54a87-e11c-3084-9f01-6761bc64af53 | -3.11398 | -53.26992 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bcd38ac-3291-33c2-9f1a-eb242e3a9227 | -5.52962 | -45.40855 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cd8f4a6-7800-3c3b-8ade-349b0ba8fed4 | -2.97538 | -53.29751 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 3fccb66c-e99c-332b-ab8d-3f8873ba2853 | -1.0813 | -53.39435 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1efc3f16-498b-3b71-9c76-84c644ff73a1 | -3.29978 | -50.76368 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aad93958-1ff1-39f1-b1df-f3c1228bbb53 | -4.66856 | -42.38615 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f507aa2e-4e74-3549-9c48-e1f5b67947a1 | -4.68877 | -46.66722 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67f83e44-5193-3d7c-bb01-ff52acfffa78 | -3.31202 | -52.15518 | 2024-11-29 04:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9cb60d4f-d8fb-3ada-a892-41dcf0b84495 | -2.10233 | -46.66537 | 2024-11-29 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2d07c3e-e6cb-39d5-a8b2-8fea79dae781 | -3.24632 | -50.77017 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfcaf9e8-f700-3eed-bcb9-12acae53365b | -2.65493 | -48.79456 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 70382cb2-659e-3817-aa37-e175fc2191e6 | -2.83903 | -46.82224 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35aeed83-a6ec-39d3-91eb-2dd43f9473eb | -5.01186 | -45.9072 | 2024-11-29 04:04:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cea823b-9c1d-3063-a330-649c68b75537 | -5.55798 | -43.78311 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6218c15d-ead8-3458-aa83-d08db32528ee | -2.86699 | -45.54229 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b46b9ed-60f1-3a6a-9754-894bd49f21c4 | -3.30107 | -50.75591 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 546ee141-3e2c-3816-87b8-b251b819482a | -4.19997 | -50.69008 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db12ac0c-dead-3fac-abdb-3163b9675054 | -2.65681 | -48.78299 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 85bad405-893c-3d3e-8f7f-21b49a722061 | -4.56574 | -46.70351 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b248df5f-08aa-39b8-8697-3a54cb5a4034 | -1.61556 | -52.46644 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 873a1982-99c1-3106-bff2-121d4d984b42 | -4.07816 | -47.02626 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1901e532-2e89-34be-8654-9a168d198fdf | -4.31322 | -44.59029 | 2024-11-29 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48720ecf-b03d-3302-b536-5b13a280e051 | -1.6975 | -52.45577 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3121fef0-2e38-3acb-a03f-7b767ecd7bc2 | -2.40801 | -48.54239 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c2a8675-524b-3b71-bac2-1a3e5627af29 | -3.26649 | -49.899 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce49a70b-45ee-3a06-b75a-615cd8d292a2 | -3.70411 | -47.13059 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f5144b8-7e73-3769-8d53-934cb7e3b836 | -1.04205 | -51.74267 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 864845e8-ff86-37dd-b87a-369c1826ad62 | -3.10714 | -53.81666 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64d47c04-e66e-3690-b4aa-8b01e9ad3835 | -3.78995 | -50.13582 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d01a47-772a-3632-a6e9-eeb07ddd09f5 | -2.83262 | -48.47272 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d97a4ff-ca74-33c9-b7e9-ed1c12bc069f | -3.22065 | -54.18664 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 572608dd-8c44-3b27-8df6-0d372ceff568 | -3.46227 | -50.53465 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c90cae8-f5d6-3cb8-a7f5-a6d89e8bef4a | -3.26704 | -49.89563 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 451d7aa8-ff78-3144-b32b-c59dc5a18cba | -4.4302 | -46.57639 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b60ac97-2d57-3187-b86f-78303d27bd70 | -4.88911 | -45.4356 | 2024-11-29 04:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce72e68-5221-3ef7-b4e4-9657a7987811 | -4.05675 | -46.68687 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 051bbb00-36ec-3efa-bcfb-254523c5e0b1 | -4.1421 | -48.2505 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e764c63-c30e-30c2-bccd-7df138ea1dec | -3.26857 | -46.44514 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ac9116-63a8-3427-b51d-b56849b61c0f | -1.19346 | -53.88122 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b08f0d4a-5e47-36d5-bdb4-320b2e6499f9 | -3.50203 | -50.49693 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2a28b16-2b07-3a64-b8be-c69ff639219c | -3.09226 | -53.82128 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92c0173a-88fe-3ab0-867d-11b87bfcbf4f | -2.83972 | -46.81802 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7edc23d-0509-34f5-b817-27a564722dc1 | -6.90549 | -39.42319 | 2024-11-29 04:04:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c79dafbb-724f-32b9-9776-1285658ee1fd | -2.87691 | -46.83693 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae6e16ae-35fb-3e4c-84a8-526937d32bc8 | -3.92141 | -53.67073 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6123c6b-0c78-3eea-92a6-977225527532 | 0.04371 | -51.11683 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 388fe2f4-eb6f-3cd1-92bf-4c4ec34b12a4 | -5.4479 | -46.34317 | 2024-11-29 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 701a6cb5-b005-37e0-b2b4-d8436c3e2423 | -4.09169 | -44.85988 | 2024-11-29 04:04:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3623c34-7ef3-3436-b4a4-694ea2eade8d | -2.62555 | -46.26926 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ec7c6f-fa01-3798-ac38-8c05e854186c | -1.69106 | -52.45466 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6069b19-98e9-38a3-a851-68dfa111682e | -5.57752 | -47.13518 | 2024-11-29 04:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27624f69-a2ce-3c57-a713-7a00f65d9183 | -2.57712 | -51.92531 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b266a6-32c3-345c-b86d-22c0b2c051b9 | 0.98269 | -50.26603 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1023b13f-6930-3a5d-80ff-737d48c8fcf1 | -2.53086 | -47.32869 | 2024-11-29 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6d1c96-14f5-3dd6-b0a9-3af95cf899ee | -2.97778 | -53.30643 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8647e858-9bc6-3f9f-bd8c-536add96e38f | 0.34341 | -49.71816 | 2024-11-29 04:04:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71a3450f-11bb-372d-aa07-9b4c04da310a | -5.03718 | -43.61894 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e1116527-936e-3a33-ad1d-4541351637a9 | -3.25076 | -50.61993 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe9e72b4-df03-3a12-8c7d-0e980b84e1ae | -2.66734 | -49.87002 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3dd8cd0-adf8-3f28-979c-f19fcb5f24da | -2.84067 | -46.83965 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b204a67-3d89-3df4-bd80-3491622d8bfc | -3.0586 | -45.06888 | 2024-11-29 04:04:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2c700f7-a0c4-386a-a618-de139860430c | -1.71053 | -52.77458 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README29.md)
