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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65707ff0-0149-3082-b6cf-9edf91fbd1a2 | -8.7772 | -49.955 | 2024-10-05 02:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b626c53d-3ae1-348a-ad5f-f4f206f95cb6 | -8.7957 | -49.9747 | 2024-10-05 02:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 11b14a70-f376-32ec-bd67-8b2d9e4c5127 | -8.7959 | -49.9533 | 2024-10-05 02:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 11a68d1a-874a-3e8d-8b20-21a3048a2f61 | -9.3457 | -51.1125 | 2024-10-05 02:05:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6880d668-28aa-3500-997d-6e34650065e2 | -9.2839 | -65.4283 | 2024-10-05 02:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 924fcef5-5c1e-313d-ba10-53833cf8ef41 | -9.284 | -65.4096 | 2024-10-05 02:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| db4e0e3d-bf90-39fa-972b-1a8ea3282fe7 | -10.294 | -50.536 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c8acc32c-cb28-38e3-854d-3ca848a77498 | -10.3126 | -50.5554 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| e1b4bfd1-62cd-3e30-a5a0-f293743062de | -10.3129 | -50.5341 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| f353531e-7749-3e84-ac02-4f983511dd41 | -10.3131 | -50.5128 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 297ca2e7-efa8-3993-af53-bcbd657c6fa5 | -10.3315 | -50.5535 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 23e45904-7ee6-35fd-b4d0-4dc707de5f6b | -10.3318 | -50.5322 | 2024-10-05 02:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e9c93b77-3fad-356e-b860-6a42146cb738 | -10.4424 | -50.7336 | 2024-10-05 02:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 57093a1e-256b-3e09-a2eb-0367a052407d | -10.4421 | -50.7548 | 2024-10-05 02:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| a763c7eb-8ae7-3788-bcfa-329537552122 | -11.1155 | -54.2319 | 2024-10-05 02:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8af2eff0-c89b-3ca7-abce-375862c50fce | -11.0966 | -54.2336 | 2024-10-05 02:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 22e270a3-c04f-3031-9d19-93c4af7cf3b2 | -11.7187 | -47.8107 | 2024-10-05 02:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 25eca744-1eea-3df5-b548-e1b3c8c71773 | -13.1543 | -51.1931 | 2024-10-05 02:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 91c62b5d-f03c-3289-ac35-40edd244db5c | -13.6136 | -51.2629 | 2024-10-05 02:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b756343b-6621-3a57-ab2d-0369ac33f9a6 | -15.5791 | -57.4532 | 2024-10-05 02:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 0d2b4430-378c-3414-837d-24236e778ada | -15.5788 | -57.4735 | 2024-10-05 02:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bafe1c94-9352-3dd6-b7b5-3cd6aa8c98da | -15.5597 | -57.4553 | 2024-10-05 02:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 013e557f-25f7-32a2-85af-3736d64564e0 | -15.7151 | -57.4184 | 2024-10-05 02:06:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b2ab3bcf-b31a-3f6b-bf56-e81f059a5fee | -16.7644 | -57.5061 | 2024-10-05 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 7108f323-1b25-3752-a617-aabc8452b092 | -16.6871 | -57.4536 | 2024-10-05 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 8cd39dc3-0143-3a18-962e-cece3b0ab514 | -16.765 | -57.4652 | 2024-10-05 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 475c8d72-4c8c-3c6c-80b3-c36f25f65a73 | -16.7647 | -57.4856 | 2024-10-05 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 6aac1806-50e0-3762-a54e-8fc65919f46a | -16.6598 | -55.5219 | 2024-10-05 02:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 41fc6a5b-dba3-30ee-98ea-db09ab1deb70 | -16.6594 | -55.5427 | 2024-10-05 02:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 51c90404-13e2-397a-bfd8-1726e28c90d7 | -16.7843 | -57.4834 | 2024-10-05 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| fa060d63-a36f-39d1-bc01-07576c5990d7 | -17.1381 | -57.381 | 2024-10-05 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 1bfb80af-a579-3bcc-aff9-e8ac001a3edf | -17.1378 | -57.4016 | 2024-10-05 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 215.8 |
| a9ef59eb-2779-37f3-8ecf-a6fa70fdf856 | -17.1375 | -57.4221 | 2024-10-05 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.2 |
| 32d114e9-9591-3c84-ac51-bda5c1f93fe0 | -17.1182 | -57.4039 | 2024-10-05 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 166.5 |
| f3984b2c-20e1-37e6-ac84-c53c740bcf28 | -17.1178 | -57.4244 | 2024-10-05 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| e898ed2b-8b54-3668-afeb-c3cd3d2aaa8f | -17.0892 | -56.7709 | 2024-10-05 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| d40f6c59-0a1c-389b-ada7-c1e4763d94b3 | -17.0888 | -56.7915 | 2024-10-05 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 40b42717-6208-356d-852b-af3a067d6955 | -18.8606 | -43.6084 | 2024-10-05 02:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| 1abb833c-7fe9-3bd5-8160-42676c6c312c | -18.8809 | -43.6032 | 2024-10-05 02:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| ac446c91-5d1f-3c72-bd9c-423daf72c4ac | -18.8816 | -43.5785 | 2024-10-05 02:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| a3c42ced-b928-3d57-9737-76a4de0429a4 | -18.6586 | -57.2759 | 2024-10-05 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.0 |
| fcc8e4c8-12d6-319f-8bf4-24d52b1e15e4 | -18.6782 | -57.2941 | 2024-10-05 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 515f1910-871e-3855-a906-6162f229af64 | -18.6785 | -57.2734 | 2024-10-05 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.5 |
| 0b6e16ae-bf7d-3540-b6fe-6f5faef7c63c | -18.6981 | -57.2915 | 2024-10-05 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 7927589e-12e0-3082-a102-a6fb52cf8c9a | -2.6072 | -45.337 | 2024-10-05 02:15:21 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 12170edd-8da5-36ad-af68-8ebdff662ee2 | -2.9014 | -50.7142 | 2024-10-05 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 359fe811-9296-360d-8801-07f95a153ac9 | -3.2899 | -50.4516 | 2024-10-05 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| eff6dbda-daff-3268-ba3e-2abda0861a8d | -3.3083 | -50.4719 | 2024-10-05 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0cece0c1-d2e9-34f6-b93a-8d0266d06837 | -3.3084 | -50.451 | 2024-10-05 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1f5c9f36-98ec-36b3-8889-5af304a9b7c7 | -3.618 | -47.5352 | 2024-10-05 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3b327af9-6185-3682-bc58-1bc8177c6455 | -3.6181 | -47.5134 | 2024-10-05 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c96c0c9d-8e7b-3539-997e-ca5cfb887704 | -4.9451 | -43.7888 | 2024-10-05 02:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0c28340b-0131-3e8e-8c87-88fd8824f1fc | -4.9452 | -43.7657 | 2024-10-05 02:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c8acbd9c-4c3e-3a06-b480-41b5d00068e5 | -5.8214 | -44.1426 | 2024-10-05 02:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b4e84a02-180e-38ba-b819-8fd3b735f2a8 | -5.8216 | -44.1196 | 2024-10-05 02:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 836fb1cc-3f86-32e8-bef1-43ae9cc78a5a | -6.9514 | -59.0666 | 2024-10-05 02:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e94d1fd1-4f6c-3e05-b20a-ce7e740f87f2 | -7.0233 | -59.3918 | 2024-10-05 02:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 546f430c-5724-31d9-ba99-bf043bd7d724 | -7.153 | -59.3092 | 2024-10-05 02:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ae8de9c2-7710-31b7-8592-c9279c20b57d | -7.5193 | -63.2558 | 2024-10-05 02:15:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b0810769-c1d5-37f0-ab30-910412108f4f | -8.7652 | -44.8335 | 2024-10-05 02:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 520f9987-2e90-3501-94df-dd51187d1a1c | -8.7655 | -44.8106 | 2024-10-05 02:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 7bb83fbe-0a26-3e97-b28d-8099aca84eab | -8.7841 | -44.8315 | 2024-10-05 02:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| a778ad58-e98e-3064-b5d6-6b6223392294 | -8.7844 | -44.8085 | 2024-10-05 02:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 237.7 |
| c74505b5-2f96-3078-b98d-0db0248db437 | -8.7959 | -49.9533 | 2024-10-05 02:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6e3205e0-9217-35ee-946f-71524ed3e1f0 | -8.7769 | -49.9763 | 2024-10-05 02:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 220ae4d0-40b1-330c-874d-5480bcaa14a4 | -8.7772 | -49.955 | 2024-10-05 02:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fd8d3b60-ed16-35b5-8fa6-25a348375ce2 | -8.7957 | -49.9747 | 2024-10-05 02:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ce528275-6cc5-347b-b7c6-4442fa3f4642 | -9.3457 | -51.1125 | 2024-10-05 02:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4ef04ed1-5265-355f-8221-3923ca1ecf9a | -9.3645 | -51.1109 | 2024-10-05 02:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 0222ac2e-2fe0-3a82-a2bd-aaabfdd9016a | -9.3647 | -51.0898 | 2024-10-05 02:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 355a313b-0756-30e9-8656-b8a627821ecf | -10.3129 | -50.5341 | 2024-10-05 02:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 9cf793e9-03ce-37c2-8d2f-fe368393c2a5 | -10.4424 | -50.7336 | 2024-10-05 02:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 4e161a7a-39df-337b-82b2-c03de84dddb4 | -11.0966 | -54.2336 | 2024-10-05 02:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1f6bb9cd-f043-3e11-afc4-18298b1c57c9 | -11.1155 | -54.2319 | 2024-10-05 02:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f661108c-3b68-3ec6-9f44-ac90d4e598be | -13.117 | -51.1337 | 2024-10-05 02:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| bc9f26aa-17ce-3746-8852-e182791ca0ed | -13.1362 | -51.1313 | 2024-10-05 02:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| af379f77-ab55-3186-9a19-59dcdc6d27b6 | -13.1543 | -51.1931 | 2024-10-05 02:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| be4d94cf-64f2-3bd3-811f-fe4b85075cc8 | -13.3978 | -61.9376 | 2024-10-05 02:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| a3236c87-eecd-3d04-be3e-d5eaf2120fda | -13.3976 | -61.957 | 2024-10-05 02:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 74fc650b-aeaf-35d5-b012-ec61389e4308 | -13.3786 | -61.9582 | 2024-10-05 02:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 19113f86-4c19-3010-8c3c-da15a817744f | -15.5791 | -57.4532 | 2024-10-05 02:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| ee265e83-3a0e-3f78-955a-ca63aacdcc22 | -15.5597 | -57.4553 | 2024-10-05 02:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 021167c5-853c-36ef-a969-c28cb9f0e0d0 | -16.4155 | -57.3619 | 2024-10-05 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 8396c04a-a20e-3115-a019-5ff2f9bd6b03 | -16.5745 | -57.16 | 2024-10-05 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| e9750cbb-7016-3968-b69d-0b8076817419 | -16.5742 | -57.1805 | 2024-10-05 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| b82071af-a30d-38f3-bee0-bc0d283738da | -16.554 | -57.2237 | 2024-10-05 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| a6f96a6e-adc7-322b-8f8e-02f6d3c2da29 | -16.765 | -57.4652 | 2024-10-05 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 21f79e58-bb0d-3af9-9a63-76250d00c6b3 | -16.7647 | -57.4856 | 2024-10-05 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.2 |
| 5092541d-e170-3c14-b039-e75822fd0a1b | -16.6871 | -57.4536 | 2024-10-05 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 7fbac00c-e4c5-301c-ba32-681e5750017f | -16.679 | -55.5402 | 2024-10-05 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| cd304914-5e50-3a2d-88af-7b4618723521 | -16.6601 | -55.501 | 2024-10-05 02:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| d45bd402-c939-3269-95fd-3c99d386a905 | -16.6598 | -55.5219 | 2024-10-05 02:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| c3868cf0-6155-3e4d-b683-c6cb86c75dc5 | -16.6594 | -55.5427 | 2024-10-05 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 1f3ef865-c0df-38f3-b3ed-59bde892ed87 | -16.7843 | -57.4834 | 2024-10-05 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 12186a0b-0400-3714-ae92-0b003712d409 | -17.1381 | -57.381 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| a77fb7e7-fa46-3286-a191-ff8c2c73f84f | -17.1378 | -57.4016 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.4 |
| a0a5fa0b-e39a-39d0-b3fb-ff4b3f710ce4 | -17.1375 | -57.4221 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.8 |
| 41a483b3-9285-32ae-bd3f-6ec5f9a210cd | -17.1185 | -57.3834 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 854137b3-b954-35e2-947d-69091dedca09 | -17.1182 | -57.4039 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.9 |
| ad9399e7-bfde-32e8-904e-0cd9aeca796e | -17.1178 | -57.4244 | 2024-10-05 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |


[Clique aqui para ver as próximas entradas](README33.md)
