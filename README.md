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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3436037d-8d7c-3f34-812d-827c10547c01 | -3.8407 | -51.1423 | 2025-11-09 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| bbd6026c-e9cf-3b9d-a2b8-cc6ec8832f19 | -3.3367 | -44.4034 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 43a811c6-c550-39a3-a3a8-ad175ad1cbe6 | -5.2722 | -44.9585 | 2025-11-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 79314fca-bb6a-349c-a726-d3282aefce5b | -4.4074 | -45.955 | 2025-11-09 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 165.1 |
| ad870953-5ca3-3a78-9c93-5c800fac5f81 | -4.6278 | -46.3883 | 2025-11-09 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 78839343-221d-3f1d-b7ab-8d1dc31086a0 | -10.3437 | -49.6321 | 2025-11-09 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 6b6e0675-2969-36e8-9ed6-930182675a46 | -3.1659 | -45.0691 | 2025-11-09 00:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4c9913e2-4699-3694-9d70-d30e4367ecab | -3.8408 | -51.1215 | 2025-11-09 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| d27d6696-88f2-38d3-9129-eea1e84ad4bc | -4.6463 | -46.4095 | 2025-11-09 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| adb90d8e-b678-3e73-90a5-d254497795b9 | -3.3182 | -44.3814 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 860b2eda-9981-36e8-a754-339a740002c4 | -3.1472 | -45.0924 | 2025-11-09 00:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c78f9c81-1890-3e11-8c11-a1d3bef71636 | -3.1473 | -45.0699 | 2025-11-09 00:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 60c3ba30-0f75-3a02-954a-3096d41d8c72 | -4.3887 | -45.956 | 2025-11-09 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a2025714-92b3-3df0-8268-6a8337e67508 | -3.8679 | -49.3757 | 2025-11-09 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9bde1a09-cad9-3106-9d83-73bb71c13d39 | -2.5929 | -49.2268 | 2025-11-09 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| eae3c575-0028-3de5-9b7f-993d7ed60767 | -3.3555 | -44.3798 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3fb7ea9f-34c5-383e-bce7-c7da4f85f770 | -2.9435 | -49.3443 | 2025-11-09 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 14bcc290-4c6f-306f-8da6-d679c1e797c3 | -2.7379 | -45.1751 | 2025-11-09 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 7bf357f5-f634-3e62-925d-fe537c69b7ef | -4.4072 | -45.9773 | 2025-11-09 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0e627c69-1345-3a2c-b9e5-1206b8edb616 | -2.7565 | -45.1744 | 2025-11-09 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 53ce8293-9ccf-3f84-8314-1903857dcafa | -2.6113 | -49.2263 | 2025-11-09 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 65590ca2-b07c-345b-8d32-91cd64f84710 | -10.3248 | -49.6341 | 2025-11-09 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5fd20e07-16ca-3929-a3b8-6c4c0d838a86 | -5.2908 | -44.9572 | 2025-11-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bc2bd129-7803-3e27-a3bf-fbefe89dc1c4 | -3.3369 | -44.3806 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 458.6 |
| b3b57f42-07b3-398f-b607-116a94e24caa | -4.6464 | -46.3873 | 2025-11-09 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1f3ebaa5-f7eb-3d2f-9ce9-2b2e354ae775 | -4.6277 | -46.4105 | 2025-11-09 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 0b2db4ab-247d-362c-9b6f-d093eac2fcf2 | -3.8119 | -45.9842 | 2025-11-09 00:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ace7e307-ad1a-38c6-9b71-273c0e2b3814 | -3.8223 | -51.1222 | 2025-11-09 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 8cfe3255-f51f-3045-b91b-60a934d2105c | -4.426 | -45.954 | 2025-11-09 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e24e2226-d93e-3985-a138-754e54d3aa16 | -3.5946 | -41.6577 | 2025-11-09 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| bc815255-825e-3021-bd5f-2a58a6050dc4 | -3.3183 | -44.3585 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a4abb595-2684-35dc-abb8-4c1cb968c158 | -3.337 | -44.3577 | 2025-11-09 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 2f4eae36-f17a-35d3-97fc-10a94f082c83 | -10.3434 | -49.6536 | 2025-11-09 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a5c2f258-d173-30c7-8fef-d91844bacac7 | -4.4534 | -44.6447 | 2025-11-09 00:00:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 49a8967c-e08b-38ab-b7ee-58c96077d0bd | -2.9434 | -49.3655 | 2025-11-09 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 371b069b-9248-3ca6-94c1-6664ada27de4 | -3.8222 | -51.143 | 2025-11-09 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 635788fd-b7c4-39d0-b42f-d384fa7b9cfa | -2.6114 | -49.205 | 2025-11-09 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1d0f4d45-ae16-33a1-9497-cb8eeeeabf2a | -4.4075 | -45.9327 | 2025-11-09 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 17deb071-0214-3c61-a5b8-cdcad821aca3 | -7.8765 | -42.003 | 2025-11-09 00:00:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 0d93e6bc-09b5-3beb-b13a-d47ff11c899d | -2.738 | -45.1525 | 2025-11-09 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 13cb8fea-167c-3057-a641-bafff788ff95 | -10.344 | -49.6105 | 2025-11-09 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7b2fe36e-af50-39ce-a0cc-120280ad4bc6 | -3.337 | -44.3577 | 2025-11-09 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 2c96fc31-92e7-3ce9-b2b0-78df478365ec | -3.3182 | -44.3814 | 2025-11-09 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 0d77896b-73a9-3bbc-91e1-7ad8b35449e7 | -3.8223 | -51.1222 | 2025-11-09 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e61f3544-4094-3c98-866f-d82986ee2443 | -2.7379 | -45.1751 | 2025-11-09 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 6bfd5aa9-c5da-31f8-940f-c28407fb14e4 | -4.6464 | -46.3873 | 2025-11-09 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 93e845cc-f0ca-3344-8b70-e5f9770598ff | -3.8407 | -51.1423 | 2025-11-09 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f6855513-925d-3f49-bd60-9fa40b3fadab | -4.6278 | -46.3883 | 2025-11-09 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c4602bef-f7bb-3f57-85ff-643c8048db4c | -3.8408 | -51.1215 | 2025-11-09 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| c089f195-7928-380a-ad73-2ab4f2d25800 | -2.7365 | -45.5124 | 2025-11-09 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2c69b28d-c5ae-3980-9525-fdcaf2a09daf | -5.2908 | -44.9572 | 2025-11-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 95a64e53-129b-30d0-920b-92a2c364d93e | -4.6463 | -46.4095 | 2025-11-09 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| dc81fccf-e71e-3fc9-9713-219735db6e56 | -3.8222 | -51.143 | 2025-11-09 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 169701b2-5355-312a-aee4-13901960702a | -3.3183 | -44.3585 | 2025-11-09 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| fcb0bddc-250f-348a-bc05-9d37e3d5ba78 | -2.5929 | -49.2268 | 2025-11-09 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 8f070ed5-6db2-3a30-b5f2-6f23181c7dff | -4.4074 | -45.955 | 2025-11-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 6ff0f4f7-5455-3db7-a9e6-f981826bbc53 | -3.3555 | -44.3798 | 2025-11-09 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 578dffde-bac1-3076-89e3-5481532a5691 | -3.5946 | -41.6577 | 2025-11-09 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| b82718bb-9e31-3205-a7c6-6c54043fc55d | -2.9435 | -49.3443 | 2025-11-09 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 893c8f02-c525-339c-ba74-1ce150086f19 | -2.6113 | -49.2263 | 2025-11-09 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 82b99248-295b-3580-8a93-6127d351e5b9 | -10.3437 | -49.6321 | 2025-11-09 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2d02f129-0143-3fdb-81f3-7e314aebad45 | -4.6277 | -46.4105 | 2025-11-09 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e354ef8f-e3ea-376b-9c44-3c8ee8b92e22 | -2.738 | -45.1525 | 2025-11-09 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 8ef58a81-4abf-359e-8819-2a53acad7a6e | -2.6114 | -49.205 | 2025-11-09 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| df888675-36e5-3a04-8273-3721b5654380 | -7.4096 | -40.0563 | 2025-11-09 00:10:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 742696b4-f40e-3978-8d32-cf879c69ba8b | -2.7366 | -45.49 | 2025-11-09 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ba2b5072-776e-3b1a-b4a0-fbf621d79de4 | -4.3887 | -45.956 | 2025-11-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 807f66b7-ca56-3ae2-b7c5-a7f9489b1c92 | -4.4534 | -44.6447 | 2025-11-09 00:10:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9fb569eb-aef7-37cc-88f7-c9af6d2ac9bd | -5.291 | -44.9345 | 2025-11-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| cb2c78bb-6e9c-34a4-9b1c-3eadbab1197b | -2.9434 | -49.3655 | 2025-11-09 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| aa1dc796-04da-3d8b-867f-2e0edf2a5822 | -3.8679 | -49.3757 | 2025-11-09 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 002b120b-ddd3-3acd-aa68-01edfb1bcea8 | -3.3369 | -44.3806 | 2025-11-09 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 335.3 |
| 5bcb5d7e-9136-3998-923d-7ed9470957ae | -3.1063 | -50.2055 | 2025-11-09 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3c728f04-aee8-3ec1-bce7-8a55ef2614d2 | -2.7379 | -45.1751 | 2025-11-09 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0aef4cdf-dbd7-325f-b9a7-93758960f816 | -4.4534 | -44.6447 | 2025-11-09 00:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 90c551a5-9d61-343c-9deb-1e84b8363945 | -3.8679 | -49.3757 | 2025-11-09 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| cd5eacf4-fec4-38d5-8f88-e6691d33abbe | -2.7565 | -45.1744 | 2025-11-09 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c6038a0a-b31a-31c5-9525-31e06127d3ea | -2.6113 | -49.2263 | 2025-11-09 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 0b5e535d-a69e-30fc-8fdd-ff68e017fc13 | -10.3437 | -49.6321 | 2025-11-09 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| de4d8386-d1b8-31cd-ae11-a2d68a327195 | -4.6278 | -46.3883 | 2025-11-09 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 413deef9-51cd-3abf-a53d-f4f7a6651c1d | -3.3555 | -44.3798 | 2025-11-09 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 845cba0f-665f-3f5e-805b-6dedc92f25e4 | -2.7566 | -45.1519 | 2025-11-09 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 446de7f6-4413-37ec-a37a-44cc436aaa4e | -3.337 | -44.3577 | 2025-11-09 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d2999a4e-b784-3188-904c-93c72bb7e605 | -3.8223 | -51.1222 | 2025-11-09 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 477f3b9b-ade1-3d80-9624-33a993289622 | -3.3369 | -44.3806 | 2025-11-09 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 261.5 |
| b6bba02d-e905-3f77-8067-912e6fcd6dae | -2.9435 | -49.3443 | 2025-11-09 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d4f538fa-c97b-3d1a-a9a9-ae423ca4f318 | -3.1063 | -50.2055 | 2025-11-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| be5e9083-534c-306a-8218-c5a32536a96c | -2.9434 | -49.3655 | 2025-11-09 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 45f110ce-b438-3247-8a56-da353769f742 | -3.3182 | -44.3814 | 2025-11-09 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 478e246a-74be-3801-bbe5-2dfae1fd834a | -4.6464 | -46.3873 | 2025-11-09 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9a87e402-1a4b-34bc-903e-86ae9feac8e9 | -2.5929 | -49.2268 | 2025-11-09 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4fed0df8-7266-33fc-b70c-c5bcf4a0493b | -4.4074 | -45.955 | 2025-11-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e78e6145-3cfb-32cd-bb0a-2314a11e1857 | -3.3183 | -44.3585 | 2025-11-09 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 999710b3-9002-3774-a746-780bd2b79376 | -5.291 | -44.9345 | 2025-11-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b17b1794-4d22-3ce6-8747-e35ef26a7280 | -2.738 | -45.1525 | 2025-11-09 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| c369fc24-7dc2-30fa-bc87-1801027cbbd4 | -3.5946 | -41.6577 | 2025-11-09 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| e25952ac-8fda-31f6-8608-c4e7103e1b33 | -3.8407 | -51.1423 | 2025-11-09 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a37e14f8-d736-312f-9e2e-1bf894b18db1 | -5.2908 | -44.9572 | 2025-11-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f22867a2-3f9a-3878-b778-c50a709f880f | -4.6277 | -46.4105 | 2025-11-09 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6698c92b-80f1-37d9-825f-eabcf5df5ae5 | -7.4096 | -40.0563 | 2025-11-09 00:20:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 45.2 |


[Clique aqui para ver as próximas entradas](README2.md)
