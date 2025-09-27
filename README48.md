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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e99379ea-d621-3cec-9ab5-7a42ebbcf266 | -7.34627 | -42.0952 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a22dca8-b296-3777-8dc4-015562f05b4f | -6.24953 | -42.48082 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 573f55ca-c138-3e66-86bd-e4c4d0aa538f | -7.28347 | -42.97446 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d2396e2a-c32a-3f3e-8bb6-7d80f5dcefed | -5.08298 | -44.85049 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7690e72b-5982-3252-9bad-a8698d5cf165 | -6.54622 | -43.82721 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 551a188f-3d85-37a9-9622-50c7fa883ce6 | -9.18689 | -46.63708 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e2a85bd-63cc-3002-8628-b5cf1329debe | -6.70299 | -44.59398 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df68ca7f-9e3f-3ae7-a431-b66c48c2aec0 | -5.62873 | -51.94393 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf1967d8-710a-33b4-9c5c-c3c7e6b76a3e | -8.83008 | -46.22379 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f66b20de-ea59-3379-9177-fad309d47c18 | -8.69507 | -47.02419 | 2025-09-27 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 765c291f-b5c2-354c-bbe2-2b06f1ab6bfb | -5.73897 | -44.97049 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b47e899-db8e-3197-953a-0d4fe5e31119 | -7.62958 | -43.80762 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3753b3a-dd89-3813-87d1-a07cfac2b203 | -8.83258 | -46.26507 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b28dff21-adff-3724-9f7b-9429c1cd8544 | -2.30413 | -48.14749 | 2025-09-27 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74635f19-236d-3538-8b41-4582754ebd28 | -7.63963 | -46.77447 | 2025-09-27 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da479b3d-2bf4-35b9-8571-0f8193c6f866 | -5.63302 | -45.33643 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b87d3c97-b65d-3ab8-be07-9c288465b9ef | -4.70085 | -46.45881 | 2025-09-27 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a7cd9d0-4b5d-3b38-934b-92b5e9a6dada | -5.74088 | -44.9867 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e7c3f28-fca2-3ffe-aa1c-c03630f25363 | -5.7645 | -42.806 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 986100b0-5096-3c2a-a858-5f62b570a637 | -8.62344 | -49.07864 | 2025-09-27 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d7c303-c76e-3192-a70f-afa3d999ef4e | -4.5895 | -50.65531 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d279b83-92de-3136-9730-92dc2a931ea8 | -7.12109 | -42.17972 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f1721a7-c774-3d9d-8d92-d55560317270 | -8.30442 | -47.04485 | 2025-09-27 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a980b336-ec6a-30a9-b65c-9eae7b053629 | -9.96828 | -43.60767 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 211a16bf-5096-34e9-b8a4-13b8a205c322 | -10.02863 | -45.41225 | 2025-09-27 04:44:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdb238e0-5443-3174-abe5-0ae9d37f72fa | -4.67141 | -50.97542 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f0ea296-c462-39d8-a171-001d8c15a806 | -3.2403 | -46.80124 | 2025-09-27 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e7cd44-10f5-3316-bab4-405e5a3a7cfc | -2.26907 | -47.1941 | 2025-09-27 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 188bcca0-9eac-3f47-8a98-77a19860dde0 | -4.70998 | -40.41993 | 2025-09-27 04:44:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b55a835-1efe-385c-8bfb-c04609f2d0cf | -6.70106 | -42.75863 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 676f723b-c7c9-3899-9d32-29caaff79d98 | -9.16208 | -46.65465 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ffad194-1457-38ad-8270-9d37c66fd057 | -7.85523 | -49.64144 | 2025-09-27 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bed0793-ee6e-39b2-ba4a-6a48a5ec3e39 | -5.22242 | -44.49074 | 2025-09-27 04:44:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c7dae40-1680-3d72-aeb8-945106d2a05e | -8.32126 | -47.03758 | 2025-09-27 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf448c8-3c9f-32db-b04f-2bcbb8926c4e | -4.26257 | -48.55124 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedaf227-aa97-336b-a876-66ad38e24ac3 | -7.72183 | -47.30161 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd35fd70-9914-31cd-8871-3d37c0e82b09 | -8.88354 | -49.4879 | 2025-09-27 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00cc92f2-bd7d-3e93-b14b-4587e36cfb74 | -6.98955 | -42.38926 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97b6f7c3-8f22-3cd1-9004-3525465e27c1 | -8.25971 | -44.94214 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b9c74f6-250c-392e-a53b-230a9bc17b64 | -7.62511 | -43.83877 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df374ae-16b1-3f99-822d-53601dae005d | -8.73822 | -47.00801 | 2025-09-27 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d435cb9-103c-3097-9e31-22d27ed49deb | -6.92971 | -44.64161 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a415fa38-f58e-35b6-b5f2-e1080d10a8bc | -7.72048 | -47.31074 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60cd4a21-6a3b-3e70-9de9-0ad865674517 | -5.07694 | -44.86189 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b1dc6d7-cd70-3d44-981e-90e17c8112d5 | -2.18083 | -47.08181 | 2025-09-27 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d26ad919-07db-3a81-a310-f7b3702ae937 | -4.38293 | -41.92546 | 2025-09-27 04:44:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7da3e75e-1d62-3312-a475-3b95e4491d24 | -6.33494 | -43.36381 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57b2bf70-f910-35aa-9b9b-d0ae53f83c99 | -5.94222 | -44.8797 | 2025-09-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01c70a4e-55b1-38a2-9c17-c5da482c35c0 | -6.49532 | -43.648 | 2025-09-27 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d877c0d4-c365-3aa1-accb-49c02f761c47 | -4.07261 | -48.04098 | 2025-09-27 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab2e6f0b-50fb-3b68-85bf-f551c50ef505 | -5.08805 | -47.48044 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bc4fc2e-0570-314d-b54f-3a4a636fc7d9 | -9.00716 | -49.16288 | 2025-09-27 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41c62bf-3996-33cf-bf32-83f304b92bac | -7.5269 | -47.28626 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d9d21e-cbc4-3cd6-bdcb-dccc5e71a5e8 | -6.31661 | -43.39085 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db9c87a7-628f-3dda-85f1-12175916c404 | -3.80633 | -41.57415 | 2025-09-27 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cac705a7-2d62-37a5-add3-3b08742285fb | -14.9429 | -47.50103 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1af2210d-cd1b-30a9-8ef3-f231e3e7bfd7 | -13.78956 | -48.33364 | 2025-09-27 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a21fb83-9a8f-3f24-8b19-f1b0221c0ec1 | -15.89283 | -46.19095 | 2025-09-27 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b88aa41-778e-3664-bab7-ee33ca1e2075 | -10.24034 | -50.25409 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83a77777-0e21-34d4-854f-8f8f886b16de | -15.02744 | -46.96207 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99b06459-8370-3b52-a47b-b93e2b3fa76d | -15.88768 | -46.19513 | 2025-09-27 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f6d2540-3313-3955-8a9b-6cba2d1f0a66 | -14.06714 | -48.82691 | 2025-09-27 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1419b510-d75b-348a-92c8-fd1e7329a8f4 | -13.61343 | -47.31279 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c321833-a9d1-3b32-89d2-97763dc92ef1 | -13.50933 | -47.40916 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cda4e70-fc1b-3bea-a421-d00389d0c6ca | -13.61352 | -47.3137 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8b4af42b-1abb-327f-b469-68d1592a6514 | -10.8124 | -45.38348 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762e9bca-5c42-37e1-b5b8-cbc7f13da266 | -11.5407 | -46.95144 | 2025-09-27 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a863b9-5db1-3fef-87ac-68f8a4028010 | -10.53419 | -49.56317 | 2025-09-27 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb63cfe7-805d-31f0-8565-02ee429a4074 | -15.55463 | -47.9113 | 2025-09-27 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac003f0-a4ac-3777-9ff8-a6d55abbcf30 | -11.5023 | -46.92773 | 2025-09-27 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a357384-4f9d-3023-b5f5-27f527e2bb78 | -15.04075 | -46.95981 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13be127c-f223-3b68-ad01-812eca32f87f | -14.63815 | -48.27349 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 377ede9b-7362-3fb8-a436-5a902ad9294e | -14.94751 | -47.49788 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e87a605b-ca9d-3c2f-8bbb-222e28c760e9 | -10.0086 | -46.71894 | 2025-09-27 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68ebe3f7-c7eb-3069-a448-b2e6744d56c0 | -10.1822 | -46.92797 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1468a03b-1355-31a4-91a2-a522840748c9 | -15.54018 | -44.34521 | 2025-09-27 04:46:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8172a60-0027-35e3-a845-86fd50c5d1f0 | -15.42427 | -48.22306 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e631e0de-58c9-3dce-8479-98ba485a0073 | -12.0349 | -47.0645 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b690a8d9-8a79-3ec5-b2a2-6c59d9c48f68 | -11.64672 | -52.87084 | 2025-09-27 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c00bee-9468-368d-bfde-d27d6ac42b27 | -12.30878 | -44.35534 | 2025-09-27 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63e6f243-7938-3645-9207-af3535329394 | -10.04332 | -50.4025 | 2025-09-27 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a325b10b-b6d8-3f99-a0fb-5048de8e6866 | -13.17976 | -47.42659 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44c2d16d-255f-3570-b7cc-765cd5c18468 | -11.61247 | -45.41919 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d8226c9-e32a-3a08-9517-1109c5e46a8b | -15.03645 | -46.95952 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe7ef939-842b-331e-808d-6adc69f6d7ba | -10.29806 | -48.79333 | 2025-09-27 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 814fd217-435d-3a63-bdae-a569c41c5c05 | -15.94033 | -57.49592 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85288be1-448b-30ff-a6e6-89bf5562d745 | -10.01213 | -46.72301 | 2025-09-27 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976a259f-ef2c-3e8a-b9f4-85f55019d8aa | -15.20366 | -48.46486 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f59d331-5c17-3ef6-9404-e9f50e7b644d | -12.29906 | -47.22213 | 2025-09-27 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44388ccd-e52a-3478-810a-cd6e9cc1fa9e | -11.98684 | -46.6123 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b860b306-1379-3e6f-be18-ccb9a0912f78 | -15.93366 | -57.48891 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04611a5a-dcb9-3cac-956d-44033b3cf752 | -9.40997 | -54.68861 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fec5f84e-881a-3f1f-b07e-7e7365b5fc98 | -11.42916 | -44.96914 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3020f600-aa54-3593-ad5b-57f657ed2ca4 | -10.11286 | -45.35088 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c0cc991-5539-3465-b260-1baf5910274c | -10.49157 | -48.03962 | 2025-09-27 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5500a926-e517-30f4-b0ff-0ed603247f91 | -13.51745 | -47.4102 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb644b50-5935-38f0-9b07-116fe5d9dc2d | -13.62533 | -48.08662 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 420d4229-6e20-309e-8444-2f8bd00656af | -10.19384 | -44.8468 | 2025-09-27 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d98b45-857d-38bc-bd76-2882fd1df228 | -13.78331 | -46.93485 | 2025-09-27 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf660be-ab0d-3ea0-a97d-37ecc1bd3360 | -11.68692 | -44.46346 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README49.md)
