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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4634ea4e-19af-304c-bc7e-39bc657c717f | -12.3434 | -48.1485 | 2026-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b5f6622a-68c8-34b3-8512-232a543a0302 | -6.6883 | -59.9436 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 9eae2525-650b-3659-bdc3-448de77971f8 | -7.9611 | -44.275 | 2026-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6863996b-d117-3a8b-a200-d3187e0f7583 | -7.566 | -61.343 | 2026-09-03 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| db3adf59-981c-34ba-af38-006ca1571465 | -7.5138 | -60.7728 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 44e9e33f-7635-3219-9bb2-0624fc047491 | -12.1269 | -44.1755 | 2026-09-03 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 2e19d466-41fc-30ad-94d3-c6f819b929a3 | -11.4895 | -50.3225 | 2026-09-03 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6565f6b7-83b6-3585-a8a8-796750e8f629 | -10.8818 | -45.3534 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 12f39268-abfa-34b4-9882-2ef6ca387350 | -11.2478 | -45.1425 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 65cb4044-0b74-3081-97e8-d27611b3e0a3 | -8.4235 | -44.9849 | 2026-09-03 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 871b6efb-a6e7-3dba-ae61-37ceb82b8c22 | -11.4898 | -50.301 | 2026-09-03 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 64ae0474-2e56-32bd-aba4-f5b83618b301 | -11.1824 | -50.5706 | 2026-09-03 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f6e0906a-3014-3c8b-835e-a66baab519c7 | -1.4752 | -54.8157 | 2026-09-03 13:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 67f85e14-1958-3d72-8d56-f8340b35bf2e | -5.565 | -60.1739 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4dd5b8d1-18ba-3fba-9fd4-2b5922e275dd | -3.6215 | -60.566 | 2026-09-03 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 02a6a714-49e6-30a8-9872-e2815ef2b34c | -11.2879 | -54.0317 | 2026-09-03 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f0565980-e4f2-3b7e-b5dd-3c3402a21608 | -13.3813 | -51.378 | 2026-09-03 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4d50db23-0ca7-310c-ba4f-3e7ac8596c92 | -7.1187 | -42.2264 | 2026-09-03 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| bf5b1209-fe8c-342b-8193-75d31459f440 | -8.4483 | -54.725 | 2026-09-03 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d848610d-0fd2-389e-8400-107af87c6cfe | -6.6357 | -59.4459 | 2026-09-03 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 489a40a4-2ead-3e66-8c01-c8ea6d78b7b0 | -12.0749 | -47.0715 | 2026-09-03 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c783843d-4907-3f89-9980-631edb577824 | -12.1462 | -44.1725 | 2026-09-03 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4fd979b0-67ca-3d1c-9e85-9eec7c85132c | -1.8019 | -47.9586 | 2026-09-03 13:50:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| c88b8cb8-9be4-3073-be92-49365de5e358 | -12.0936 | -47.0913 | 2026-09-03 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1c74be46-9c82-3b6b-a8ec-633ba12ee5d5 | -12.3626 | -48.1459 | 2026-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 92d6e22c-4e06-3757-a25c-4517df587525 | -7.6149 | -44.8833 | 2026-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1fd63fbf-d9a0-3c8a-8b88-33db5ff8f04b | -8.4675 | -54.6631 | 2026-09-03 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| c56ac88c-4130-3802-88af-14ba21eae19a | -5.3264 | -60.143 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 872dac75-77a1-3b25-aeb2-af2b7b32424f | -9.6293 | -54.3158 | 2026-09-03 13:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| ceb77b02-3eec-3312-85d1-e219d0c05b09 | -12.0557 | -47.0741 | 2026-09-03 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 86f9a027-fdf0-3a7a-a543-db27135e526d | -11.5086 | -50.3204 | 2026-09-03 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 32fae6a9-9c54-35ef-9fc3-f12b2ed82866 | -8.4673 | -54.6833 | 2026-09-03 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| dfac1801-6fb1-357d-8dfa-d3902a77b206 | -12.094 | -47.0688 | 2026-09-03 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 07c571fd-422b-38e1-91c8-b20c76afac05 | -8.4677 | -54.6429 | 2026-09-03 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 298.3 |
| 63d85bca-bdfe-3d89-93c9-4a19190de9d9 | -6.6541 | -59.4452 | 2026-09-03 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 94b390bf-4f8a-3b74-9147-01f186574eae | -10.3959 | -49.9703 | 2026-09-03 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f5609782-baf1-32bd-8aa8-8d96929bea00 | -7.6171 | -49.9226 | 2026-09-03 14:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 85dbb162-e951-32c8-9315-cf9ec276e8f9 | -10.3961 | -49.9488 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 528f4567-62fa-302b-a927-b4da60d36c61 | -13.3625 | -51.359 | 2026-09-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0e7697fa-3377-3f39-a02c-30047e351966 | -11.4218 | -43.9321 | 2026-09-03 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 311cd4de-cc4f-34ac-8022-41ee060312b1 | -12.3434 | -48.1485 | 2026-09-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4748bc12-5b6d-3d16-af2e-ddffd82e5d86 | -11.2879 | -54.0317 | 2026-09-03 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a9a99aaf-073a-3327-baea-42272ee05615 | -6.7648 | -59.4408 | 2026-09-03 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 19f48bfa-3c1d-3015-ab03-27478fbe5a3f | -5.5098 | -60.1947 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 97aa85f1-f610-303e-b0c2-3b39941e535b | -12.1457 | -44.196 | 2026-09-03 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7486e01a-a2ae-3b00-b728-5af751081fe2 | -11.4895 | -50.3225 | 2026-09-03 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bce1e1b9-9393-30b9-9de9-a0aafa21bf75 | -8.4483 | -54.725 | 2026-09-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ac0fe1d8-c074-3a79-8376-7d77e5bea31a | -11.2126 | -46.1066 | 2026-09-03 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 85db1f22-566d-344b-be73-84a6b31a4934 | -7.6505 | -46.7268 | 2026-09-03 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2528a0e6-10f8-3da7-856a-16b4b4f16541 | -12.3622 | -48.1681 | 2026-09-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3e2b3e13-3552-36fb-b805-587543c5ce85 | -1.5127 | -54.2761 | 2026-09-03 14:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e529f541-382f-3ffb-b98c-b70bae3fbb8a | -7.5982 | -49.9453 | 2026-09-03 14:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 91dfb71c-7219-33b9-bd34-a9bd38f0d348 | -9.2144 | -47.99 | 2026-09-03 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 01de4277-b061-356f-98e0-6960dc8ecad8 | -10.3959 | -49.9703 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1e966885-e0c4-3786-8ee8-5cf62b814466 | -8.4677 | -54.6429 | 2026-09-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 98eb5993-08d6-3d29-9d75-a25c3ba5019e | -12.1269 | -44.1755 | 2026-09-03 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 82828024-cf7c-37cc-a359-2b6478cb1899 | -5.3264 | -60.143 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bdfa52e3-e6ce-3bd0-a1d8-c7e4865189e6 | -10.3956 | -49.9918 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 9f59c1e0-9519-3eec-a832-55fc4e7db055 | -6.6697 | -59.9635 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 296fe619-aacd-3e77-809a-ea091c289c09 | -7.6144 | -44.929 | 2026-09-03 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5c9a80fb-337c-3f19-93ac-5c46b60b4a85 | -9.7157 | -47.1869 | 2026-09-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 68918828-c72c-3b3b-ac79-b8efd78b1fd0 | -11.0247 | -49.6656 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fdf5bc32-e719-353f-a986-12a424a50e57 | -10.3394 | -49.9547 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cac7f5a9-1976-32f9-9749-d60cd1ea9180 | -9.6418 | -45.7144 | 2026-09-03 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8d025071-03f4-3e12-a4b1-a827de53802d | -8.4235 | -44.9849 | 2026-09-03 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 48d349e8-7d5a-34f6-9f1d-6846ad3e1020 | -1.8019 | -47.9586 | 2026-09-03 14:00:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0ffce4cc-cae2-3a98-93b5-17df81330aa6 | -9.6293 | -54.3158 | 2026-09-03 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e1fa56eb-ad63-3cfe-a4e7-3d3bc234ebba | -3.6215 | -60.566 | 2026-09-03 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c593326d-8ec5-3cf4-899a-f9f3acd67f84 | -7.1187 | -42.2264 | 2026-09-03 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 2cb4007b-6249-3b32-be32-e64a2cf7432f | -12.1512 | -47.0833 | 2026-09-03 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 489177fe-e1d0-33bd-960d-656d2d62d374 | -10.7564 | -44.8647 | 2026-09-03 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a5f2877a-e7e8-3851-87e8-e99d7cd7a8fa | -6.6698 | -59.9443 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| dcee1f8a-a97d-3f96-a265-23b6a1016f94 | -7.2255 | -42.7616 | 2026-09-03 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| b2c54e61-49e8-345d-885e-440a74673570 | -11.4898 | -50.301 | 2026-09-03 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| be3ba26e-98bf-31ae-b5ba-723eea1bf5dd | -7.8068 | -47.8591 | 2026-09-03 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 544db8f6-bc94-3a56-b1a5-704d53b474de | -1.5128 | -54.2561 | 2026-09-03 14:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 03f51793-bc1b-3664-b7c7-3903e7103ef5 | -11.006 | -49.6461 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7da3a7bb-31ae-30e4-9d27-767848413a7d | -10.4145 | -49.9898 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4f23d371-de48-35bb-ba66-92fc2215602a | -10.7154 | -46.2395 | 2026-09-03 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a4730b06-ae7c-3093-bbc6-9bcc2034d371 | -8.4046 | -44.9869 | 2026-09-03 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b46a7a0f-5643-3af4-ae4f-80cdbe563fc1 | -10.696 | -46.2646 | 2026-09-03 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a799dd98-adf6-3725-98a6-6e5fbba8cc70 | -12.3626 | -48.1459 | 2026-09-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 145f9dd1-0ba2-324e-95ca-010da0c507d4 | -8.4675 | -54.6631 | 2026-09-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 71fca09a-633e-3a5f-af42-711d6d0e5137 | -6.6357 | -59.4459 | 2026-09-03 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a1f67dfa-6ec5-3d72-938c-574586419e95 | -10.6967 | -46.2193 | 2026-09-03 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 284d969c-15d5-300c-831f-73eb41f22c9e | -3.2455 | -47.9187 | 2026-09-03 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1f5e11c6-5597-32c0-abb4-1398c475a37b | -8.4481 | -54.7452 | 2026-09-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 7784e62d-bf87-3e05-905d-2fa40a168d95 | -11.0623 | -49.6829 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2260bb62-b4b6-303e-9508-fbb04128888c | -8.4485 | -54.7048 | 2026-09-03 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f5d9f4bc-dd29-3c77-8b9f-9a65e53ecb1f | -13.3813 | -51.378 | 2026-09-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ed35b343-623f-3966-8a11-4c1726ef55bb | -9.5964 | -47.6204 | 2026-09-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 6abb1d3d-86d8-3737-a79e-47aabfb75fb9 | -11.062 | -49.7045 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 54c3573e-8f98-325a-9444-9902b7945581 | -1.4752 | -54.8157 | 2026-09-03 14:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 88fc863c-d992-3bef-a8b4-3f8feec97c9b | -13.3817 | -51.3566 | 2026-09-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 288cdab3-8a78-386a-a6ba-c8304b356b95 | -11.5086 | -50.3204 | 2026-09-03 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1490707a-fbde-301c-87b3-a78a2067cc2d | -10.6964 | -46.242 | 2026-09-03 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| eb9bf35f-a113-3893-b5a7-fa49b94dfd77 | -6.6541 | -59.4452 | 2026-09-03 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 90d95b64-69a5-39ec-8861-41a72d5aebbc | -7.6169 | -49.9439 | 2026-09-03 14:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 95417f87-ddfc-35dd-8f7a-ea0c496f8918 | -7.5138 | -60.7728 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ea2726c7-e34e-3437-967c-f4874a5a4d39 | -6.6883 | -59.9436 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |


[Clique aqui para ver as próximas entradas](README59.md)
