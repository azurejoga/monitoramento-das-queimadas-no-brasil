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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2455582-b715-3364-81f8-1ad7609de5be | -8.08006 | -44.11121 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fae22ac1-c285-3a0f-908c-b0cca26290e6 | -8.7144 | -48.33211 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7effe61a-7aa2-3046-962b-71c1927ccb48 | -8.07876 | -44.12216 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade11f40-0d7b-36e0-b3dc-5e40860c705e | -8.08642 | -44.10786 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edc75990-ef3b-3e4d-be01-3263f4b6ac90 | -7.38188 | -46.80486 | 2026-05-19 04:59:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ae5bb5d-8650-3e85-83e9-da98c8349849 | -8.08669 | -44.10637 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 682a8ffd-6d8c-33d1-8da7-f941c624b659 | -8.37124 | -49.64001 | 2026-05-19 04:59:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 338d78d0-3b5e-3a91-9aca-6843f750db12 | -8.07427 | -44.11041 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b51ac4e3-b8e3-3d43-9602-65bd96389e96 | -8.71939 | -48.32843 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| db679b21-ef77-3a14-8c51-4a94613ac3f1 | -8.71879 | -48.33274 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f79a505-f29e-345a-af12-49ea0917050b | -8.71999 | -48.32408 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 79ef7ffc-15e9-3268-918c-c51fe7ef90c9 | -8.72928 | -47.97696 | 2026-05-19 04:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 142e4384-827a-383f-9302-0ccb71da5b6d | -2.75139 | -54.59176 | 2026-05-19 04:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112f3a68-2be9-3e2a-9aef-95f9f9aa177e | -8.72318 | -48.33339 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ae41617-16e9-3572-9c65-890b2d143579 | -8.55436 | -45.98802 | 2026-05-19 04:59:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1662b1a-b624-3800-9566-543fddc70732 | -8.08036 | -44.1097 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6004cdd1-b99f-3e61-baa4-6353de283448 | -8.07258 | -44.1228 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 003c14a6-be30-308e-bd95-4e75955cea6d | -8.54922 | -45.98721 | 2026-05-19 04:59:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3b3d29a-b07a-3f7b-bcb1-53df6bbbb18e | -8.70486 | -47.92229 | 2026-05-19 04:59:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46dfb4f2-0a2a-3361-8c6d-d2a7b8659a36 | -8.07822 | -44.1263 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c8c0ff3-7955-326b-8d5d-65c1328d7881 | -8.07781 | -44.12776 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c843a8ba-f641-3abf-8cda-28840f038cfa | -8.70036 | -47.92156 | 2026-05-19 04:59:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dab19393-6039-3ae8-a15a-3ea9e5f18a04 | -8.715 | -48.32776 | 2026-05-19 04:59:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 31558efa-c894-372a-af3b-722f23a46292 | -2.75333 | -54.59225 | 2026-05-19 04:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a6d101-8055-390d-8cdd-d9464aa83f09 | -8.72864 | -47.98141 | 2026-05-19 04:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33b8e81c-23b4-3264-866e-52da412ebd00 | -8.07837 | -44.12363 | 2026-05-19 04:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bb21783-1979-3d9d-ac8d-5be2e6d2d976 | -11.43443 | -55.10115 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf13e20-b196-3a9d-a4ee-d3f156b349fd | -10.45925 | -47.94026 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ead6adb-5d4f-3866-b058-4622c34a008d | -11.32834 | -47.43882 | 2026-05-19 05:01:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc03f29-f3f5-37a8-a615-e9adf57f4f17 | -10.39986 | -49.44117 | 2026-05-19 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eec0abfb-6f33-3eca-8ecd-ae2b195e1aba | -11.45982 | -55.11246 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40572668-7460-3b38-be7b-412b2abae2a2 | -11.97587 | -52.46246 | 2026-05-19 05:01:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 003d7bde-b74c-3ca9-9ef5-105672a97dbc | -11.45925 | -52.91896 | 2026-05-19 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1045f2b1-07b7-3a05-95df-f5c3d35a10c4 | -11.45871 | -55.11948 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dad5ed4-891a-33a0-a96f-f143d381d91f | -14.70508 | -48.32541 | 2026-05-19 05:01:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04689b7d-cc92-3a59-b99b-b03e93766f28 | -12.05126 | -45.27242 | 2026-05-19 05:01:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ead57e9b-3bf7-37d6-a9de-e9a375d02af2 | -9.30282 | -45.48321 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eb660a5-58e5-3f44-9f24-44ede9e42e9a | -14.70513 | -48.32445 | 2026-05-19 05:01:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c528d0b4-fefc-30df-b2f8-bc57310c2856 | -11.1893 | -55.91532 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1341f31e-6d38-395f-a44f-4159cc8614ee | -11.45518 | -52.92233 | 2026-05-19 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41e14200-3d35-302f-82fb-aac1dfb69912 | -11.18265 | -55.91423 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf792b1-c0a8-3845-9ccb-c8ef4f9ffdc1 | -11.44989 | -55.11085 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29ab07be-c8cd-3c8f-8ea5-c18d7a4fe9ef | -10.45438 | -47.94806 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba549df1-37d9-3448-a93e-26998c631168 | -11.61132 | -47.10366 | 2026-05-19 05:01:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e892a11b-9c7d-3d6c-a868-fef588f234c4 | -14.16555 | -52.8863 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3dee6cb0-1f6d-33de-afbd-2095d5c7d3c2 | -11.45927 | -55.11597 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe8b8299-d21a-3b7e-8cde-695d34514b2e | -9.93949 | -52.45772 | 2026-05-19 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 535c966f-74cb-32f3-a3e5-d692eb99d05c | -10.45043 | -47.94254 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3a05f23-ea0c-316f-82fc-59018dda01a8 | -10.46036 | -47.93897 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6431108-7b6a-3e89-a303-ef958fd161a9 | -10.45644 | -47.93326 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3fccc38-ecfa-3b9d-a003-c62cc1586364 | -9.2999 | -45.48529 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc16725-2372-3ed1-8ba5-e448a6c4f664 | -14.15544 | -52.88042 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 470b3fc1-4704-3db3-a30f-69417730536d | -11.18598 | -55.91478 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5baf0bb1-d336-3ca7-b83e-458df4e7364c | -10.57193 | -46.67313 | 2026-05-19 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77667ca2-f340-39ea-9dc2-893905c062b2 | -11.07962 | -48.26202 | 2026-05-19 05:01:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24d774f4-6b74-357e-a45a-1fd52985dbae | -11.43519 | -54.09125 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 158e8868-275d-3a78-8dc4-bcf755e41eb3 | -10.44515 | -47.9467 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cf6dfe35-f1a1-39e1-b23e-0392a8add958 | -10.45574 | -47.9383 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 411e6e24-710c-371b-a236-9a9b6a6374e9 | -11.45375 | -55.10788 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d52586f-0bc6-323b-ae62-fc0ee89afecb | -11.46203 | -55.12001 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fa5c6e-b64d-34b8-91f4-ae173b63dc10 | -9.29742 | -45.48258 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4ddb9da-973f-3108-a504-2bf5fca27e36 | -11.32345 | -47.43847 | 2026-05-19 05:01:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4556428-4c8b-311a-8938-101e6cfc8fd8 | -9.30034 | -45.48183 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81ea3c9c-a8e1-36c0-9371-a95d4a2f2cf4 | -10.11926 | -52.41241 | 2026-05-19 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d047fa9-049d-33b6-944e-6a30c72caf51 | -11.97481 | -47.36937 | 2026-05-19 05:01:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6ec035-b1dc-3dab-9517-92ecfa80a205 | -11.91905 | -54.10371 | 2026-05-19 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e331694f-0fee-3cf3-a97c-3c42243490b6 | -11.75112 | -54.791 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77a4eb36-5c25-3e14-9d7c-378e94d828fa | -12.05646 | -45.27694 | 2026-05-19 05:01:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6b42e44-84bc-3c7f-8b56-f1f22a1b02d9 | -10.45182 | -47.93252 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0effa0d8-b7aa-3977-97b3-ede89933d5c7 | -14.15902 | -52.88097 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0242490e-acc2-3ccf-9e8f-6bcb183263ff | -11.45196 | -54.09389 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e7010c6-ac03-3d4a-b39f-b9667e3a5e89 | -11.4447 | -54.09645 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ae62b8f-e999-3bf4-8b0b-ad2d5eaeca54 | -11.6071 | -47.09712 | 2026-05-19 05:01:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57e3c7d6-671f-304c-a532-81a60b14680d | -11.20811 | -55.92566 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eafe4f8-2687-331b-a152-1612b7e75585 | -11.74725 | -54.794 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1531508b-d651-3517-b0c9-db1d46ee161e | -10.65356 | -42.31357 | 2026-05-19 05:01:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| baf9965c-969b-3943-91a4-cb48e1776573 | -10.66652 | -49.69861 | 2026-05-19 05:01:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12c0161f-2037-3ed8-a8f5-d97a04ebbfae | -10.65083 | -42.30961 | 2026-05-19 05:01:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8f2f93e-1780-3b5f-b076-79f3a2257f97 | -9.47391 | -46.0771 | 2026-05-19 05:01:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6c0ab1f-1bd1-39ca-8b29-3b1b69879440 | -11.3208 | -47.4209 | 2026-05-19 05:01:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31b8f475-123a-3d54-9a26-2fc566e30fbe | -10.67013 | -49.70295 | 2026-05-19 05:01:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 999e65a1-6e5c-3473-ba45-3e4d8b92c9a7 | -11.45596 | -55.11543 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21f4e487-a757-39c9-8717-28e273caa8fe | -14.15002 | -52.89246 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a338b357-61a5-3816-b02c-9f0373c6570b | -9.30979 | -45.4935 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd487830-8a7f-3ce8-bdb3-12269e55e834 | -13.03353 | -49.93475 | 2026-05-19 05:01:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3138387-462d-3f30-acf9-41e9796a4108 | -11.44916 | -54.08976 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ba9c70b-4f43-3728-9f9c-af084f3333fb | -10.57232 | -46.67014 | 2026-05-19 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37ad06d3-ccca-3323-b885-df8dd29c8302 | -9.2925 | -45.47849 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c529c65d-7c12-331d-970b-717fdccec92c | -9.30529 | -45.48594 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c4ffeb3-d23a-3857-b075-2cb1b0c80def | -12.05693 | -45.27311 | 2026-05-19 05:01:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d27888a7-f62f-3a20-a04b-6115571f9522 | -14.16198 | -52.88575 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8efa624b-b356-30ac-9d93-9c3904876ab2 | -11.97974 | -47.37003 | 2026-05-19 05:01:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148811bd-31f6-35b6-9eed-9ce912120470 | -10.44976 | -47.94739 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ba7e1357-2a71-3ab7-8eb5-9dca093d7529 | -10.45991 | -47.93528 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3688943-8bd4-3892-b0fb-d6613266253d | -11.17876 | -55.91721 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd4520bb-fb3c-38ca-b073-aa16ded71ed9 | -10.65424 | -42.30766 | 2026-05-19 05:01:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0227e62-ff1a-37f9-8354-cc7109fec757 | -9.30774 | -45.48729 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d08729d3-8f45-31cc-9a3f-7096487ecae2 | -13.02933 | -49.93419 | 2026-05-19 05:01:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d0e76b-1466-3c14-90cf-cc44c1c58483 | -11.46314 | -55.113 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22933f5c-0251-32c2-9a10-c0e7d84be393 | -11.46258 | -55.1165 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
