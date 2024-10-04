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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c22bb93-dedf-383c-91fa-2b39c251aa0e | -16.4148 | -57.4028 | 2024-10-04 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 55e70215-5f2e-3b82-8cbb-b9c1460f8033 | -16.4151 | -57.3823 | 2024-10-04 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| c1992204-084d-3806-8e42-137068a5b724 | -16.5935 | -57.1988 | 2024-10-04 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.0 |
| 98ce0a90-821f-3f53-a624-7b1a98bd9652 | -16.5938 | -57.1783 | 2024-10-04 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.1 |
| 63924d27-971d-3a12-8366-a1d5b33f0ca1 | -16.613 | -57.1965 | 2024-10-04 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.7 |
| 416f136f-4b73-3c55-84a6-8f060d188964 | -16.6133 | -57.176 | 2024-10-04 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| f769cb72-d209-31e1-8ac6-ccd67abae0d7 | -16.6871 | -57.4536 | 2024-10-04 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 0b4b4b28-a01f-365d-bddd-2b3732e86c30 | -16.7455 | -57.4674 | 2024-10-04 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 4f53a3cd-003e-3847-b3cb-b05548bacde9 | -16.7647 | -57.4856 | 2024-10-04 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 35af0378-e1ec-318d-8fc7-09c96966ea38 | -16.765 | -57.4652 | 2024-10-04 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 3cd15e95-9d4d-30d1-a662-912b5ebf8292 | -16.7859 | -57.3811 | 2024-10-04 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| 35e024cd-11d2-331e-8621-32b93b510771 | -16.843 | -57.4767 | 2024-10-04 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 1f3ec4a4-0c6a-37b9-b7a4-191d221a3b6e | -16.9283 | -55.8405 | 2024-10-04 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 00e1d40b-0fe7-3156-af3c-040b4961b25e | -17.0888 | -56.7915 | 2024-10-04 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 4762d99d-ddac-3075-bbe1-3a3598ce8aaa | -17.1085 | -56.7892 | 2024-10-04 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 21c48163-9812-3145-856e-b3ee21d6fe58 | -17.1088 | -56.7685 | 2024-10-04 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 5427f71a-a323-34f1-afe8-34b608ea4c4a | -17.1378 | -57.4016 | 2024-10-04 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| df05de6d-fd1a-332c-8f35-0fc852629a52 | -17.1574 | -57.3993 | 2024-10-04 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 24314690-add4-3f2d-996d-09ad903facaa | -17.1577 | -57.3787 | 2024-10-04 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 7bb53b57-8c6d-31f9-8507-177bfded967b | -17.1771 | -57.3969 | 2024-10-04 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 78c639a9-e55d-3ed0-81b2-338b9170b93e | -17.1774 | -57.3764 | 2024-10-04 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| c9373125-2de9-38af-9231-28c29b19752f | -17.7508 | -43.8079 | 2024-10-04 04:16:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 41cb5959-de64-381b-b7e2-8b9b257d6357 | -19.0148 | -43.1749 | 2024-10-04 04:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| cf579b21-dca9-3147-aef3-6861c9491eca | -19.0344 | -43.1944 | 2024-10-04 04:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 98925f7e-13d8-37ba-9442-07f0ad21371a | -19.0352 | -43.1695 | 2024-10-04 04:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| 25833767-1b33-3ce5-b90b-42b10f664473 | -19.3159 | -42.5976 | 2024-10-04 04:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.5 |
| af0861a1-5043-3c5a-84cb-62305820a94c | -19.3167 | -42.5724 | 2024-10-04 04:16:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 47caf731-4dbf-3fda-a015-ab17acdfb70d | -19.4891 | -42.8997 | 2024-10-04 04:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 67bd13ca-568f-35c1-add4-ecd43dc57e44 | -19.4899 | -42.8746 | 2024-10-04 04:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.5 |
| 894b6a75-73f7-305c-affd-00b1b0c75ff7 | -19.5096 | -42.8942 | 2024-10-04 04:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 591fb11d-9eda-3b22-92bf-dca3ca82761d | -19.5104 | -42.8691 | 2024-10-04 04:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.0 |
| c44ffa96-457c-34aa-ab8c-0ed7786664bc | -19.8516 | -42.3738 | 2024-10-04 04:16:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 280.6 |
| 2e32d4c5-4dbc-3dea-82f0-4e4c83b48964 | -19.8524 | -42.3484 | 2024-10-04 04:16:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 218.8 |
| 2a5ebf13-c178-3551-b067-c070316db8d4 | -21.3334 | -48.8044 | 2024-10-04 04:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| 4deba8b3-cbe9-3cfb-b4ee-4919e4f2e717 | -21.7773 | -48.3976 | 2024-10-04 04:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 77.0 |
| da28b5d9-b6a5-32b0-9909-f6f9fe880409 | -21.7981 | -48.3926 | 2024-10-04 04:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5eb777eb-be5c-305d-a9b1-bfae6568cd8a | -21.8397 | -48.3826 | 2024-10-04 04:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ff856c5c-98ea-3d4e-959c-eee4187790f2 | -3.29 | -50.4306 | 2024-10-04 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 55d713a0-ac89-3399-9dc9-9ed218d54392 | -3.2899 | -50.4516 | 2024-10-04 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 219.6 |
| bfa58d37-5ab8-3c30-b91e-aa12870daa94 | -3.3083 | -50.4719 | 2024-10-04 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8c4cb0de-180d-3ba4-a328-a22b27d1b506 | -3.3084 | -50.451 | 2024-10-04 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 291.4 |
| 53e047a5-4c91-3de7-90d1-8925b3eed47b | -3.3085 | -50.43 | 2024-10-04 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ba6d00da-c24f-3a4c-8753-c68f9d6b42e7 | -4.0765 | -48.4687 | 2024-10-04 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3705b59b-142c-33a9-beab-353f8de1d009 | -4.0949 | -48.4894 | 2024-10-04 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d8379580-3102-3d99-b44a-62c19358105b | -4.095 | -48.4679 | 2024-10-04 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 46982c48-e26b-3ab0-9e77-0453ced2adb0 | -4.6686 | -45.8738 | 2024-10-04 04:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| add87e8e-f32e-378a-b6ba-187de2c1b510 | -4.6872 | -45.8727 | 2024-10-04 04:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 190.6 |
| f3c3e4f2-e8f2-342f-9bef-d836c7bcbf8a | -4.6873 | -45.8504 | 2024-10-04 04:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6d135210-2034-3e1e-94c7-87d589ad471d | -7.6262 | -45.5413 | 2024-10-04 04:25:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| cbc21a6d-54dc-3342-886e-be2f175ce572 | -7.6264 | -45.5186 | 2024-10-04 04:25:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 56f0955a-4bee-30e3-a494-83b2ff6d262c | -7.8539 | -45.3611 | 2024-10-04 04:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 11ae2948-563c-3b0b-9a2f-8129adce4548 | -7.8541 | -45.3384 | 2024-10-04 04:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 893bd143-3b66-3672-b6b3-2fc0f849edf5 | -9.3118 | -50.7991 | 2024-10-04 04:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 3561f65b-1f7b-3fa2-9704-8b594014f817 | -9.312 | -50.7779 | 2024-10-04 04:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| fa06844b-4a60-3dc1-86a9-012e917102b0 | -9.3306 | -50.7974 | 2024-10-04 04:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 9b431511-f039-3412-88f8-4a43deb4e705 | -9.3308 | -50.7762 | 2024-10-04 04:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1b810b54-6ba9-3390-8214-b8278e9d4ad7 | -9.845 | -68.9623 | 2024-10-04 04:26:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 66089662-c4d5-380d-a29a-4b04d27f5cff | -10.8018 | -45.5927 | 2024-10-04 04:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 19230023-5e2e-3871-8519-b4fed214edfc | -11.0918 | -46.5069 | 2024-10-04 04:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5cbdc5c6-88dc-37e1-ab37-d37d44e8eb06 | -11.1112 | -46.4818 | 2024-10-04 04:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5272e34d-b742-3bf2-905d-a0793b92f6a1 | -11.2566 | -60.5825 | 2024-10-04 04:26:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8ecd0b7e-b0df-3b72-aee3-1dc6342b2923 | -12.5901 | -53.115 | 2024-10-04 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 5d352f1b-b036-3c04-af02-259fe5218c4e | -13.1587 | -48.6764 | 2024-10-04 04:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e52941aa-95ec-3b10-ad32-f7636690e8e1 | -13.1591 | -48.6543 | 2024-10-04 04:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 53fec273-d8aa-343f-b2bd-6d15e0a6ba11 | -13.0598 | -51.1195 | 2024-10-04 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 91ccda39-8104-38b5-b154-c2ab77ae293a | -13.0786 | -51.1385 | 2024-10-04 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cff9fd12-653f-3310-9024-0e7cb1e769a4 | -13.079 | -51.1171 | 2024-10-04 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 19842e8c-222c-394a-a3a9-307454d07054 | -16.4151 | -57.3823 | 2024-10-04 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 668d6f18-27dc-388a-b35c-266eff46307b | -16.5935 | -57.1988 | 2024-10-04 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 1a7909cd-31d1-38d3-bc82-08a928e6ac55 | -16.5938 | -57.1783 | 2024-10-04 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 5ea47990-de1e-37d6-9d00-619e36f9d031 | -16.613 | -57.1965 | 2024-10-04 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| d37a6189-4a85-3e22-8f34-3b929f0379f8 | -16.6133 | -57.176 | 2024-10-04 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| c067da69-7d20-3e51-82ff-b5a84bde6646 | -16.6871 | -57.4536 | 2024-10-04 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 6d67305c-e082-3dc5-a655-57d347a3ac37 | -16.7455 | -57.4674 | 2024-10-04 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| b6c10f36-a343-3fdb-82f8-384ffbd7a08c | -17.0888 | -56.7915 | 2024-10-04 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 5425f65a-3f39-36db-b9a5-c25975b22e7e | -17.1085 | -56.7892 | 2024-10-04 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| f40b053b-2783-33a1-b994-a0559400f83c | -17.1088 | -56.7685 | 2024-10-04 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| fded0ed4-5bd6-3307-b2a3-6f25df59f7cb | -17.1378 | -57.4016 | 2024-10-04 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.7 |
| e00431eb-1309-3c28-83d6-b17fb26a78ac | -17.1771 | -57.3969 | 2024-10-04 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 8e04f986-a998-3e64-9ada-dc224fed6f4b | -17.1774 | -57.3764 | 2024-10-04 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| a181b047-18f7-3514-af0d-2562fb770633 | -17.1574 | -57.3993 | 2024-10-04 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| d8267419-93c3-3609-9e75-754e13c068ff | -17.1577 | -57.3787 | 2024-10-04 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 0382dbfd-e8a0-3d51-bae7-985852d4ed33 | -17.7508 | -43.8079 | 2024-10-04 04:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7b23477f-1140-36b9-beda-9bd3d1395ca8 | -19.3159 | -42.5976 | 2024-10-04 04:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 6380fbf8-faf0-342c-a72a-38c6d695f3e4 | -19.3167 | -42.5724 | 2024-10-04 04:26:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| e65ac971-2114-3150-83d3-a21b4499e77f | -19.831 | -42.3796 | 2024-10-04 04:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| 58a99e8e-c3fb-3243-8538-29c577a302ec | -19.8318 | -42.3542 | 2024-10-04 04:26:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 86b9d377-7638-3f5f-afaf-63696dfc335d | -19.8524 | -42.3484 | 2024-10-04 04:26:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 484.0 |
| 89ae009c-fbb7-3cf6-afdb-a8575d3e6619 | -21.2888 | -48.9302 | 2024-10-04 04:27:03 | GOES-16 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| df946c52-4006-38dc-b2ff-fb908b82017b | -21.3334 | -48.8044 | 2024-10-04 04:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 170.4 |
| 9a683e3e-a7a8-39d0-8340-e6d90831b557 | -21.3341 | -48.7811 | 2024-10-04 04:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| cb242976-6a68-3115-8bab-502f5430264f | -21.778 | -48.3741 | 2024-10-04 04:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ab4ce500-a206-3aa0-a7a8-a8daa7b46c90 | -21.8397 | -48.3826 | 2024-10-04 04:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 139.2 |
| c87cce67-e7dc-38f2-82a8-0e9c1aedf569 | -3.37935 | -42.30526 | 2024-10-04 04:29:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 705a704a-498b-370f-a223-10c41fedf2b3 | -3.36308 | -42.30265 | 2024-10-04 04:29:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 9d497659-a4aa-3b64-b484-1a533d467233 | -3.38479 | -42.27121 | 2024-10-04 04:29:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 45e0292f-9bba-334f-bb15-fc904352295e | -3.36855 | -42.26862 | 2024-10-04 04:29:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 97543be5-4991-3e78-86c9-d4b38e6eba38 | -7.69232 | -42.97766 | 2024-10-04 04:29:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| fd3a3c01-a7f0-38fa-bcda-514fa140c052 | -4.53269 | -43.30404 | 2024-10-04 04:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3efb3f1a-b6ec-31a7-b43d-a57b95ea5e40 | -4.53229 | -43.29591 | 2024-10-04 04:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |


[Clique aqui para ver as próximas entradas](README93.md)
