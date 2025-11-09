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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61056a3d-e6ae-3554-96a9-3caa6dfaaec1 | -3.29485 | -50.19794 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd4ea1c0-8f2f-3271-80d9-919899a4b505 | -4.8805 | -48.58578 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fcf7b01-3531-3c69-a07b-c98ecf778c3a | -3.09434 | -49.22493 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f400b6f7-49bd-38f9-aaa9-01921f6c1bcf | -3.52931 | -47.54166 | 2025-11-09 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46c376c8-b352-3072-8760-c367dd0cfff6 | -4.75291 | -42.77831 | 2025-11-09 04:16:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bde117a6-694a-3630-a7ff-b5e3e73e0f62 | -3.56162 | -51.12644 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba7ae08-9986-35ae-8ca9-dd1121d78440 | -5.21875 | -42.91566 | 2025-11-09 04:16:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ae02c50-2f8c-32db-b6fe-b16134fb6abc | -4.28611 | -50.66737 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ec56b76-c2ff-3166-99c2-4eba6487a413 | -3.0161 | -49.44111 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd8b6730-7578-3f2f-9e2e-b5af5717135c | -3.08533 | -52.92141 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1672d830-c0c4-3cbe-9e65-82836d0005c3 | -3.2339 | -51.38042 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88540fad-358e-3066-a208-c96f59b872bb | -3.95215 | -49.02589 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d631d3b2-b702-3c36-ae9a-5b09b7113668 | 0.66282 | -51.54375 | 2025-11-09 04:16:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c97d13c4-08b1-3944-8f14-4fadb3da6387 | -4.39168 | -45.95838 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 956b1220-41a7-3dce-8704-0e96c6955b5d | -4.16602 | -46.80837 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d5699f-acf2-30e8-9bd2-b8afc45b4e63 | -2.64173 | -43.46404 | 2025-11-09 04:16:00 | NPP-375D | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22dfcd28-80ff-320f-910e-d3252bd43fab | -2.60661 | -49.22701 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d497bff1-2e2e-3d78-a05a-37ee47a1840c | -2.9414 | -49.3582 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e501f24a-b523-3520-a24d-6057d8690768 | -2.55053 | -45.15618 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5463d10b-a068-30f5-9f30-a77379177d57 | -3.45593 | -50.03053 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0084a049-8878-3e18-93cf-9e135b40047a | -4.95889 | -44.94494 | 2025-11-09 04:16:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e7529e-f115-3ff9-b798-920fd23c32ea | -2.78916 | -49.65756 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5effbf16-168e-3241-87a8-2b68133f41b9 | -3.80687 | -45.99504 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b839a67-c63f-3beb-a8c6-ed9ed0594c85 | -2.83339 | -50.44508 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca1ab7c-8a00-3943-9b91-fbdb29e70a52 | -4.94318 | -45.26498 | 2025-11-09 04:16:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 564dd912-5736-39d4-bf51-f3ddeaf512e9 | -2.9763 | -44.5894 | 2025-11-09 04:16:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8969ec4-146f-3b74-87e9-59003c9040dd | -3.51247 | -40.35606 | 2025-11-09 04:16:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ae3ab617-9484-3bf9-85cc-42fb6aeea4d1 | -4.39765 | -45.96783 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f11ae076-0378-3aa4-b4b9-90feb52ad75d | -3.341 | -39.9983 | 2025-11-09 04:16:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62bd3903-1d74-35e9-8700-d8c58adcc428 | -4.58169 | -45.62069 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7834c158-610c-3463-a1ee-8f586df7645c | -3.58717 | -41.65767 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 413da27e-dba6-37c4-856c-df6f5a55e535 | -5.49282 | -45.86383 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc55dac5-c366-3b81-b60e-acec34153f1e | -4.24435 | -44.67229 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a1e661-dfc3-3495-bc09-0b3ffcb56a64 | -3.85672 | -43.29022 | 2025-11-09 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3031cee-72a4-3758-bd8a-19c39567feb8 | -4.33646 | -39.36492 | 2025-11-09 04:16:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7bce2a7-466a-3588-9292-57d7f33acfcf | -3.26325 | -50.04389 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55cbe63f-bb9d-3b48-805c-f6f61bb03709 | -4.63306 | -46.40117 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32b3e06d-ae0d-3d1f-b649-0eacc28be292 | -4.43303 | -43.57907 | 2025-11-09 04:16:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb196f3c-a310-35ce-8a32-5c2210a5cd9c | -2.2959 | -47.87016 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 826fd72e-1777-36d1-8af8-70a5acfde80b | -4.63921 | -49.5429 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2e919f0-c540-3379-b3a3-a6a187308803 | -3.33338 | -44.36679 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c4335e4c-0b61-3cf4-88eb-12c12d740f12 | -3.1049 | -50.31959 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 965f1658-c57c-3cad-bc67-c42321a5f071 | -4.27017 | -45.53677 | 2025-11-09 04:16:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dc9c7a1-fabe-3261-8cef-1ee47a9dd88a | -4.3944 | -49.77497 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d1ec2e3-49a8-3a60-82c9-55437f859a44 | -3.05567 | -50.22128 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57ebe2d6-bea0-36a0-8bc1-4e2c9a2ea20a | -2.49636 | -48.15234 | 2025-11-09 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3d75c7-7483-3c8c-8e9c-9dbb9ef60df4 | -3.89358 | -47.18532 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd2c1f49-0813-393c-9fb2-9f8c2a005579 | -4.14661 | -46.26192 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b461e59-6d35-3c71-b6df-3d9b98ac4b17 | -5.31137 | -44.2085 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33265021-0fc6-3c85-91f7-2b1638aa452f | -2.62283 | -46.85136 | 2025-11-09 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 467b9174-a10e-3b49-bffa-562284bd6356 | -3.07898 | -49.37755 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ed9dd4e-bafd-3cfe-8fa1-a6addfc4d74a | -4.39668 | -45.95058 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f0b454-aba9-3eee-ad92-c576385b8cde | -4.79759 | -46.00933 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6802f78a-e08a-378a-9cda-23b00637858e | -3.45287 | -45.64752 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad74760c-351e-3473-b763-19f59856329b | -3.33779 | -53.25081 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4da8187-2c78-3053-a8c8-59fba5760f6a | -4.39977 | -49.65738 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8689a648-8365-3167-8962-318055053b2c | -4.61501 | -49.65905 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b484e20f-cdb7-3d86-b0d5-17646e61d2fa | -5.21928 | -45.14479 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c54e037-bd49-3cc2-9978-5fb742ae2c8e | -3.33444 | -44.38223 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 14c495b4-7610-3e30-97fb-564dbacf58fa | -3.32538 | -53.35881 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d50189ae-8297-3f77-8312-338ff4050a58 | -3.8645 | -49.38425 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6c8cf127-9f8e-3d97-8119-2c6c03e5c8cb | -3.28384 | -49.77234 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fa6d998-ec2f-326e-a92f-bbd88259f406 | -3.3246 | -53.36335 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dfeeef5-8a8c-30b3-a46d-acee99516d3a | -3.05959 | -50.22074 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75ed7c85-0209-3e1e-9c9c-84174c132af3 | -3.91473 | -50.03997 | 2025-11-09 04:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccce993b-7ce1-3cd5-b5fb-7710573103a9 | -4.81923 | -46.80422 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccc8b19c-3ab6-381f-984e-b8e95b5b9b63 | -3.33262 | -53.24515 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c9dcc4-4f39-3334-9a02-cb7397bf9d29 | -2.60199 | -49.22628 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f615049-e521-379b-82d4-735f0755bea4 | -3.8011 | -48.90993 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82089105-f158-3316-9049-dae102750558 | -3.58662 | -41.66117 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a3171d7-3576-3c59-8453-027f55f3df0a | -4.91274 | -45.98851 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6ac34ea-0540-3f67-a338-b898116ab996 | -3.09951 | -50.20043 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ceb37297-e99e-3dc0-a5bd-6823ea3c3665 | -3.58916 | -41.65772 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e7dbbfe3-6f21-32cc-846f-a9be2d9d66b2 | -3.36241 | -51.2857 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3a862a0-1449-3bd8-a842-c37978a822d1 | -4.58102 | -45.62474 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 987348d4-540c-3595-b2b8-a96bb8e83e55 | -3.31243 | -50.12371 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b4960c5-f253-31cb-8a1c-3227ec774024 | -4.41283 | -43.1116 | 2025-11-09 04:16:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73b9c49c-bc75-3082-ab2d-92617038af5e | -4.04893 | -46.43153 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d8b5972-01ca-39be-a75e-3c7b3d6b041e | -4.18438 | -45.73919 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24a7116-f100-3d18-ad57-6acf84d6e91e | -3.91905 | -51.01614 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73d2e02-5c2e-3be7-9718-d66234c6bd36 | -3.58392 | -51.24652 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8faceab9-2c6a-3b9e-be9b-a28a0f129959 | -5.27909 | -44.95171 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9abbd7e8-ebe5-3d63-ac63-d52d8664ae1e | -4.8062 | -45.39692 | 2025-11-09 04:16:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05c3985-2d50-32ae-bfc7-55eeafa6c9fc | -3.79737 | -48.90489 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cce8db47-e1fd-3118-afb6-3fe6164ec645 | -3.14085 | -50.28585 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ff3a201-adcc-3892-9f71-c2888a3bbb3d | -3.44857 | -45.65113 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ae4588f-2e4d-3438-8d01-bf531c2c6b2a | -2.43265 | -48.04031 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4d0ad93-c317-32ee-bdd9-4e5d134d8f32 | -6.28494 | -38.87862 | 2025-11-09 04:16:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ff77ad5-88c8-3e4e-9beb-d7679df0a91c | -2.83415 | -50.44483 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d012a58a-9fde-30cf-b7c9-e5d202091c14 | -2.74008 | -45.16373 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c893ba40-4962-3e3d-989d-b20a88fd3be6 | -5.37834 | -44.72598 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63841718-7a17-371d-96c6-f2a51816dda1 | -3.33966 | -50.19989 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1427145-8532-3f94-8efe-cb409a68a0bb | -2.743 | -45.16833 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 610f81f1-5c74-3ecc-9f95-e6123b77c2fd | -3.42321 | -52.89394 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbddc9c-81d4-38f0-9583-c1a22fdd9603 | -3.3316 | -44.37796 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a25e3fc6-8860-3b89-b0f4-a80dea0e01e8 | -4.33229 | -49.75798 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2fddf6f5-a8cf-3b17-bdfc-a03c92c97628 | -2.62037 | -49.25854 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710313eb-791a-346e-8ff1-566fcff85925 | -3.79808 | -48.90059 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02d44a37-6ec2-3576-b79c-f712e5669d98 | -5.48924 | -45.86321 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b2217ef-06d8-3b98-8ca5-39f034f22438 | -2.59816 | -49.22084 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README15.md)
