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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1819606c-efb6-3aea-96a8-05a7bcd9cae3 | -4.447 | -42.8889 | 2024-11-01 13:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a3f0bd5c-c720-3cc3-a768-7d389ac6b042 | -4.3869 | -43.4525 | 2024-11-01 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 64249f86-e65c-3330-b2cb-b18e2561d840 | -4.7372 | -44.1016 | 2024-11-01 13:35:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 282f2ac0-1dd2-3a3c-9e43-7e65cd0dfb52 | -4.7373 | -44.0786 | 2024-11-01 13:35:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e0b47142-cdf8-33bc-a890-92b23aecc150 | 3.4342 | -51.2601 | 2024-11-01 13:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| cca3ae05-0240-34e1-875a-cd5ceceacf1c | 3.4157 | -51.2606 | 2024-11-01 13:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1acaddbc-71ff-3064-97d3-4a1a45180230 | 1.796 | -50.4467 | 2024-11-01 13:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 59c0d984-e9fc-351a-8280-c0c215627dc8 | -0.6896 | -51.6847 | 2024-11-01 13:45:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 44450160-fbfd-367b-b07e-e22b24c69e01 | -1.4244 | -52.1913 | 2024-11-01 13:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 01e84d3f-7d38-3a5a-a1a0-e22b229d6ded | -1.4426 | -52.273 | 2024-11-01 13:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cd2e1c55-f552-3261-af47-0fe9d0130db4 | -1.4244 | -52.2118 | 2024-11-01 13:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8c2c3a4c-273f-314b-8bb8-62ee5fb8769f | -1.8471 | -52.308 | 2024-11-01 13:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e94a9d07-3240-38dd-b555-3bfa51d874c8 | -2.1695 | -48.7252 | 2024-11-01 13:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 19be3231-53f5-3c2d-84f4-5390640ea52c | -2.2499 | -46.6606 | 2024-11-01 13:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 7a119c1e-83de-34a3-b713-97f0554e38f3 | -2.2685 | -46.6601 | 2024-11-01 13:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 785bb034-3e6b-31a3-9697-46e5c4fb1370 | -2.466 | -48.5035 | 2024-11-01 13:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e0a6d354-d733-3781-a218-ae9095c34174 | -2.3898 | -49.1895 | 2024-11-01 13:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 7494e3f4-9e3e-3665-ba15-948b2fe530f6 | -2.836 | -48.4501 | 2024-11-01 13:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 72839ea9-989d-37cd-811e-d1eb790f9f33 | -2.8361 | -48.4286 | 2024-11-01 13:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 54829a3e-4895-337e-853e-7861811b63d7 | -2.7961 | -49.2211 | 2024-11-01 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4fc8dd26-7a29-3708-971f-10822503167d | -2.8175 | -48.4506 | 2024-11-01 13:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| fd015912-b2bd-3c86-a99f-f7a326b959a7 | -3.0353 | -49.4901 | 2024-11-01 13:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 4ef3dd44-ed31-39f2-9daf-37128059cae6 | -3.0354 | -49.4688 | 2024-11-01 13:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 576033e3-03eb-3f23-93df-1987d30a52e1 | -3.0949 | -44.3677 | 2024-11-01 13:45:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| af345004-42ee-3719-8278-28446de0541c | -3.2535 | -50.3479 | 2024-11-01 13:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 469fa799-2d46-3b43-b91d-05b2f7a75638 | -3.3891 | -41.6201 | 2024-11-01 13:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| fc345657-ea79-3bcb-9bc1-f451b4a9d9ea | -3.272 | -50.3263 | 2024-11-01 13:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 8af87295-61c2-38bf-b1bb-a444917640c4 | -3.2231 | -53.3972 | 2024-11-01 13:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| dfabb5af-ccdd-3877-b836-d0014ebd21ec | -3.2535 | -50.3269 | 2024-11-01 13:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 30e139ac-0edc-3e95-93cf-f6e24c8500dd | -4.3867 | -43.4757 | 2024-11-01 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 882d8126-03fd-3b20-8601-57a00931355c | -4.3866 | -43.4989 | 2024-11-01 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fe0819a5-2a20-3ad8-b317-97b3e4ac63f9 | -4.4657 | -42.8877 | 2024-11-01 13:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ad84e5d7-bf28-330e-bd19-dd1b23fdc944 | -4.4387 | -46.8624 | 2024-11-01 13:45:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ce90b5af-bca1-3ee7-88fc-a7e9b272ba63 | -4.3869 | -43.4525 | 2024-11-01 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 936b04f6-8304-3c78-aa74-33a341ea26d5 | -4.3157 | -45.7362 | 2024-11-01 13:45:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 73116585-a9d6-3d37-96c8-38fe4cc5c14e | -4.4056 | -43.4514 | 2024-11-01 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 8c9421d1-b4d7-3957-8e35-4a4713fdc2f8 | -4.7372 | -44.1016 | 2024-11-01 13:45:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d4dda7a8-067f-3a19-82b0-565c741c92a9 | -4.7373 | -44.0786 | 2024-11-01 13:45:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 86f29ad3-cd9b-3b14-b502-3d86b3d1eac3 | -16.9207 | -57.5086 | 2024-11-01 13:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 3bc33825-4c38-379a-aab1-3e05da3a6eaf | 3.4342 | -51.2601 | 2024-11-01 13:54:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| be6d89a5-20b1-30c0-9a79-7d6518117d9e | -0.6896 | -51.6847 | 2024-11-01 13:55:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 57.7 |
| dc078ea6-4153-3ddb-ac12-beeb5181eea2 | -1.4244 | -52.2118 | 2024-11-01 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 347fd274-b76b-39a2-b689-062c65e1c1ae | -1.4244 | -52.1913 | 2024-11-01 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 0f386f9b-2697-351f-a590-49343105a220 | -1.7366 | -52.3507 | 2024-11-01 13:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e8f1bc68-c0c1-3d2b-badf-bcda955bdb7a | -2.2685 | -46.6601 | 2024-11-01 13:55:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 71fface3-7e7b-3ed7-9dd7-7a2c7e7d67a1 | -2.2931 | -50.6668 | 2024-11-01 13:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| a640b612-ff02-30f4-a465-a8d074a51f2e | -2.2499 | -46.6606 | 2024-11-01 13:55:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 09af8073-59d3-3af1-9ed3-21d93d32916b | -2.3946 | -53.8606 | 2024-11-01 13:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8805aa80-5457-37d1-8e71-7c376f075382 | -2.4344 | -46.8976 | 2024-11-01 13:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| a7bf12c9-1160-3ead-b869-ed1b51d25c92 | -2.466 | -48.5035 | 2024-11-01 13:55:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 80cc85a6-3a1d-3d59-a73d-37751128e964 | -2.7961 | -49.2211 | 2024-11-01 13:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3cd24223-f7ce-33bc-a718-8cf41b679f68 | -2.8361 | -48.4286 | 2024-11-01 13:55:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 453a8f58-c542-34d3-8aa6-212308d9c548 | -2.836 | -48.4501 | 2024-11-01 13:55:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 1551771f-ca40-3cc6-8d95-d69b51f23bc4 | -3.0538 | -49.4895 | 2024-11-01 13:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f04dc23f-6d00-3a08-844b-edf2406844d8 | -3.0539 | -49.4683 | 2024-11-01 13:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 73e8043e-48ed-3f69-b41f-9874eab500e0 | -3.3891 | -41.6201 | 2024-11-01 13:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 8b9ecb2e-79d4-34b5-b9cc-d9be41e104b3 | -3.2535 | -50.3479 | 2024-11-01 13:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d6e4362a-3c30-3936-bb45-5f8457122e98 | -3.2232 | -53.3769 | 2024-11-01 13:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7d6c8720-fa77-37f0-9634-958326f5f165 | -3.272 | -50.3263 | 2024-11-01 13:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 2a16a1b0-5668-3a71-abd9-69c0cb80ae78 | -3.2231 | -53.3972 | 2024-11-01 13:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 0d2066d7-f174-35bc-99cb-0cb46c6aebeb | -3.2535 | -50.3269 | 2024-11-01 13:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c72a2649-dc17-353a-ab46-ac7c724bae4f | -3.5762 | -44.8935 | 2024-11-01 13:55:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7c41033d-390d-355e-852f-e043acb74781 | -3.9473 | -48.3666 | 2024-11-01 13:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 16b0204f-d2cb-30ea-91dd-a17028fd672c | -3.9474 | -48.3451 | 2024-11-01 13:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 809b9583-8ae1-3e20-af1b-f726be988a15 | -4.4056 | -43.4514 | 2024-11-01 13:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ce313218-a42c-3909-b5ad-b28c4c38b26a | -4.4387 | -46.8624 | 2024-11-01 13:55:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| bd210733-d54c-3fd1-ac53-6a216e136363 | -4.3867 | -43.4757 | 2024-11-01 13:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 3c959114-88b3-3dfc-b5f6-42b63aa36e90 | -4.3869 | -43.4525 | 2024-11-01 13:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b5a705ff-482e-3c8b-b3e3-feea221598dc | -4.4468 | -42.9123 | 2024-11-01 13:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8241e32e-d325-3133-a0ca-3e30a660513a | -4.7373 | -44.0786 | 2024-11-01 13:55:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e8e260c3-f557-3f65-af13-6a6b8a11a361 | -6.9971 | -41.3258 | 2024-11-01 13:55:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 52821137-5783-30a3-987d-5517546c6ef9 | -7.016 | -41.3239 | 2024-11-01 13:55:46 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 02073d1e-513a-32cd-adf8-f55590afa25c | -17.62 | -57.46 | 2024-11-01 14:03:45 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39d5a332-c95d-3924-826d-d1a61d9af297 | -17.66 | -57.48 | 2024-11-01 14:03:45 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08943574-0ea7-3ca0-8254-4ae49224d1bd | 3.4342 | -51.2601 | 2024-11-01 14:04:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 3b2b22cd-e4d1-3ce0-8e32-5830947b8bd8 | 1.796 | -50.4467 | 2024-11-01 14:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 355f8873-05bc-3edf-a28a-4ab41fa0dd24 | -4.41 | -43.44 | 2024-11-01 14:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec398c0-a871-3a2c-b47a-d2a057640364 | -4.51 | -38.94 | 2024-11-01 14:05:01 | MSG-03 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bad53d20-bdc8-388c-b68c-27e617d51680 | -4.39 | -43.49 | 2024-11-01 14:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae8823ef-4faf-37de-b71f-2b078c00c328 | -4.39 | -43.44 | 2024-11-01 14:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e975ac3-6ce6-36ae-97c9-3b7d72bebd16 | -4.41 | -43.49 | 2024-11-01 14:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd2da4d-9773-3013-a7a8-14ad6f08f4b3 | -0.6896 | -51.6847 | 2024-11-01 14:05:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| cd5fc8bc-0461-37dd-a788-e5aeca07eca1 | -1.4426 | -52.273 | 2024-11-01 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6833080e-1029-3895-bf2b-dd17451ba988 | -1.4244 | -52.2118 | 2024-11-01 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| b1287b5b-7080-3970-97f7-0487f3b94b7a | -1.406 | -52.2121 | 2024-11-01 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f593b88d-07ca-31fc-a62b-213a173005f2 | -1.4244 | -52.1913 | 2024-11-01 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2ccbc06b-9519-3d4b-b4d3-04f7932a06b6 | -1.7366 | -52.3507 | 2024-11-01 14:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 199062e6-1575-317c-9ed5-da78901d574a | -2.1563 | -53.6636 | 2024-11-01 14:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 32148805-7de9-3c19-9884-160e08ee3ba4 | -2.1695 | -48.7252 | 2024-11-01 14:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 12ec888a-3ef9-32e2-8a16-631c1b4581e6 | -2.2685 | -46.6601 | 2024-11-01 14:05:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 48a530d5-95a5-302a-a4ff-d98ab44038cf | -2.2499 | -46.6606 | 2024-11-01 14:05:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 81b33a35-5ca8-3e4e-afb6-f803dfceb57b | -2.3444 | -46.127 | 2024-11-01 14:05:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d0f5efce-0e02-3b09-b300-0190fcca0a8a | -2.2088 | -54.7454 | 2024-11-01 14:05:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1aa01ce0-5397-3712-8c8a-d90b0d73bad8 | -2.4344 | -46.8976 | 2024-11-01 14:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b15e372b-6d77-374f-a130-e02e494c9df9 | -2.466 | -48.5035 | 2024-11-01 14:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c7b786e7-01a7-347a-8874-eb98cb1e12e4 | -2.4471 | -48.6113 | 2024-11-01 14:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cf7ca937-97f4-3c13-a99c-1baf981b4708 | -2.676 | -46.7365 | 2024-11-01 14:05:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 30f2282a-aa93-3925-b4c4-cac578f8e097 | -2.8722 | -48.6636 | 2024-11-01 14:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c51026c6-c799-3b85-9c8e-35141f5a781e | -2.836 | -48.4501 | 2024-11-01 14:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 60a72292-a90b-3434-9291-5cd00e45396a | -3.0354 | -49.4688 | 2024-11-01 14:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |


[Clique aqui para ver as próximas entradas](README61.md)
