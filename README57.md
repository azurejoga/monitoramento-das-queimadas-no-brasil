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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c2fce5-5aff-363e-af74-b0000f0b043a | -9.3303 | -50.8186 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 749d6ff6-ab3a-3004-97e7-1134e63341ce | -9.3306 | -50.7974 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 411.6 |
| 0ee8924a-3196-31ec-93c9-581e29e3c888 | -9.3308 | -50.7762 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| d4eb45f0-0345-3a59-8d32-89767204591e | -9.3494 | -50.7957 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| cede8e99-a006-3d7f-958d-5ba9738e09d5 | -11.0918 | -46.5069 | 2024-10-04 03:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ee3b931a-0123-3760-a311-ffbd67db88f3 | -11.0921 | -46.4843 | 2024-10-04 03:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ce064560-d189-38d1-8dc3-d5748aabd83e | -11.1108 | -46.5044 | 2024-10-04 03:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8d3e87b3-def8-33f1-af2b-c12ec0b11359 | -11.1112 | -46.4818 | 2024-10-04 03:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e7cfb440-a9a3-38fb-9926-7b4aad8f4d61 | -11.8242 | -56.6009 | 2024-10-04 03:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a5dd2926-0c8a-3b58-81fe-e82fa1125d54 | -11.8244 | -56.5808 | 2024-10-04 03:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 165be6d1-8de7-36af-885f-0c7e586dfede | -12.5898 | -53.1359 | 2024-10-04 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| f68f3168-d0de-33f7-a33d-a0a680e08dea | -12.5901 | -53.115 | 2024-10-04 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 360bf017-1b02-3c09-901d-3917757ee71a | -13.1587 | -48.6764 | 2024-10-04 03:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 20719eba-28ea-3942-b99d-13d860441d37 | -13.0598 | -51.1195 | 2024-10-04 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 59b1bbaa-df61-35e7-8d80-1f99626a1bd7 | -13.079 | -51.1171 | 2024-10-04 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 14df9363-8b7a-3080-9f89-a7d32f2a4b12 | -15.3564 | -58.1632 | 2024-10-04 03:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b98dc439-7ced-3e4b-8c4a-bd47ef32f8e9 | -15.3567 | -58.143 | 2024-10-04 03:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6b1b5dbb-252b-311c-9940-d107adaaa601 | -16.4148 | -57.4028 | 2024-10-04 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 6db5b2db-9b24-3f24-ac01-3ff8dcf25869 | -16.4151 | -57.3823 | 2024-10-04 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| b9ef5fe8-e15b-3f88-bed0-b50e4e462e97 | -16.5935 | -57.1988 | 2024-10-04 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| b45703b1-77bf-336c-b0a2-413daedff137 | -16.5938 | -57.1783 | 2024-10-04 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.3 |
| 26596946-7b8d-34bd-a4b9-577a52cae8c4 | -16.613 | -57.1965 | 2024-10-04 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 173.6 |
| b0299d09-5de6-3b92-9339-473916808f72 | -16.6133 | -57.176 | 2024-10-04 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 245da01b-4dca-39b7-9f9a-0adb884ea02b | -16.6868 | -57.4741 | 2024-10-04 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 64b130a6-f5f5-3a3d-a6cd-d643225b6aac | -16.6871 | -57.4536 | 2024-10-04 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 0f6014f1-a27d-3345-b708-5dd0a43519ee | -16.7455 | -57.4674 | 2024-10-04 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| e4d24456-9178-36b3-a2aa-43b8bb1f82de | -16.7647 | -57.4856 | 2024-10-04 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| 8e3a79d5-b41a-3083-9990-458ac3d03996 | -16.765 | -57.4652 | 2024-10-04 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 89ab2c15-d2e0-3f89-a932-c2cbecad8e3e | -16.9283 | -55.8405 | 2024-10-04 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 0338a2ec-71f8-30c2-87d3-f3b7370135c9 | -16.9287 | -55.8197 | 2024-10-04 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| de15d971-27ed-3569-bc55-4570fdc359b5 | -17.0888 | -56.7915 | 2024-10-04 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| e8e29103-0669-307c-a34f-5f993cb3a6a2 | -17.1085 | -56.7892 | 2024-10-04 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 4e208ba3-49fe-3879-9a93-a867e2946fbf | -17.1088 | -56.7685 | 2024-10-04 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| e083d599-390d-332a-9c56-740f6c64c867 | -17.1378 | -57.4016 | 2024-10-04 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 6d9caa34-2532-363b-923c-db4ea128cb93 | -17.1574 | -57.3993 | 2024-10-04 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| de1aff24-8b4b-3abe-a09e-b45d1ee850f7 | -17.1577 | -57.3787 | 2024-10-04 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 0cfe4db1-5e3a-3f7c-ab53-030d35c2f1c4 | -17.1771 | -57.3969 | 2024-10-04 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 8383486a-7b75-3bfb-905e-d9282c29ba45 | -17.7307 | -43.8127 | 2024-10-04 03:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 135.5 |
| ac5a3636-6fb1-30aa-8c67-c782a2b91393 | -17.7508 | -43.8079 | 2024-10-04 03:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 0deda560-a320-39af-a380-7f8b414d0f8e | -17.7515 | -43.7835 | 2024-10-04 03:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 51f5121b-44a8-342b-ab57-716afbc3c4d9 | -18.8613 | -43.5837 | 2024-10-04 03:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.3 |
| a7196ae9-24d1-3e5e-98e4-fb7a254323d0 | -18.9081 | -42.0315 | 2024-10-04 03:56:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 96094052-7826-3aa6-91a0-e024de45603a | -19.0148 | -43.1749 | 2024-10-04 03:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| a8ff1842-15a4-3d18-852f-c0393c3bb214 | -19.0344 | -43.1944 | 2024-10-04 03:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| ba1e8fef-3c63-330b-b039-e4603b3bb892 | -19.0352 | -43.1695 | 2024-10-04 03:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.2 |
| 542f60f0-9e1d-355f-a32b-004433005dd2 | -19.3159 | -42.5976 | 2024-10-04 03:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| ee9e7dec-9416-3529-96f8-67471c9c2e0e | -19.3167 | -42.5724 | 2024-10-04 03:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 6633c977-91e6-35b5-8f9c-59cbea398f73 | -19.3363 | -42.592 | 2024-10-04 03:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| c122313b-0ac3-3ff3-86a9-8486e0f7416f | -19.4899 | -42.8746 | 2024-10-04 03:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| cf25fb59-298f-3d08-81bd-552ed88f40ec | -19.5104 | -42.8691 | 2024-10-04 03:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 24e0e329-cb56-3d06-a701-ce1b05c8307f | -19.831 | -42.3796 | 2024-10-04 03:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| 1dc5fe59-fde8-3c23-8080-aa1b18e1bd50 | -19.8516 | -42.3738 | 2024-10-04 03:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 267.6 |
| bd46d841-8971-3479-b477-fffd1a045a5a | -19.8524 | -42.3484 | 2024-10-04 03:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| dd920f43-720f-3f1b-8fb2-6454bc9148f8 | -21.7773 | -48.3976 | 2024-10-04 03:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c5c6f31b-21e2-3e63-869a-7ef3d66c69bc | -9.32 | -50.78 | 2024-10-04 04:04:33 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f44bb112-a3a9-334e-a20f-2dbab3598fa0 | -4.67 | -45.86 | 2024-10-04 04:04:59 | MSG-03 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b8baf74-34f0-3762-9ce4-239603f080d7 | -3.37 | -42.31 | 2024-10-04 04:05:07 | MSG-03 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 5668f399-5a11-3e35-85fa-d25246b1ef07 | -3.37 | -42.27 | 2024-10-04 04:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1cac39b-7fcf-3a31-b97f-69fa6c547628 | -3.29 | -50.43 | 2024-10-04 04:05:10 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2626c003-2471-3da1-b23c-8e69b5a5906d | -3.2899 | -50.4725 | 2024-10-04 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| a3579a41-3177-3d2a-b065-1d3d84bfa952 | -3.2899 | -50.4516 | 2024-10-04 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 22207378-5e6e-3ac5-8962-86e51a967635 | -3.3083 | -50.4719 | 2024-10-04 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 702208f7-50ff-32f4-9dbd-ce8e2f066298 | -3.3084 | -50.451 | 2024-10-04 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 857206b6-4ef4-3b8a-8e33-4df50e01cc43 | -3.3665 | -42.3112 | 2024-10-04 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 131.0 |
| fdf999b0-3a58-399f-89b5-6a18ffb00fba | -3.3667 | -42.2875 | 2024-10-04 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 253.2 |
| 09163628-a1bf-3267-8291-ec59b307d690 | -3.3852 | -42.3103 | 2024-10-04 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 6425ab47-4a02-3b21-8c54-ffe0913ba899 | -3.3854 | -42.2866 | 2024-10-04 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e533c99d-c6e1-33b3-a2c3-1193b5abc639 | -4.0763 | -48.4902 | 2024-10-04 04:05:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 9c7b9914-9a52-3abf-a36d-7994fbf33a6a | -4.0949 | -48.4894 | 2024-10-04 04:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 27039ebd-dce9-3254-8051-37f0113f5f07 | -4.5375 | -43.304 | 2024-10-04 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 676cd8b3-d4a6-34e4-a3b6-f2cc4b7f1ef3 | -4.6684 | -45.8961 | 2024-10-04 04:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cb9d84d7-96e3-3c8c-b470-ee6df41ec536 | -4.6686 | -45.8738 | 2024-10-04 04:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 115.0 |
| b1380395-1665-3ba2-8035-640a6c77767b | -4.687 | -45.8951 | 2024-10-04 04:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 2f535e42-570a-3d7a-b2b8-92dd5bbf5db1 | -4.6872 | -45.8727 | 2024-10-04 04:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 210.6 |
| b43dddec-181d-36ab-b770-6d8254795d6f | -7.6259 | -45.5639 | 2024-10-04 04:05:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fbd7e159-68bd-3f8f-bedf-0c4cdc63b6f5 | -7.6262 | -45.5413 | 2024-10-04 04:05:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| bf8e7fd4-d764-363d-a1da-44d4d033aef5 | -7.8539 | -45.3611 | 2024-10-04 04:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| cbff0dce-2a25-3b84-b2c9-5e15aaf7ffb7 | -1.58828 | -48.03056 | 2024-10-04 04:06:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fac4e94-fe8e-305c-8ef6-67e88e1da3c5 | -1.4918 | -47.33873 | 2024-10-04 04:06:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4e2936c-bd3e-390b-a0c4-c335c04f5817 | -1.03688 | -47.79342 | 2024-10-04 04:06:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aed1d4e1-5bba-319c-8665-1fa5711b4dfb | -2.39501 | -47.66264 | 2024-10-04 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d62870d-e0b6-3e34-a0d3-bc6e13c3b722 | -2.34009 | -47.9715 | 2024-10-04 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2636535c-dfda-3c65-9bf7-10d52f12dd3b | -2.33928 | -47.9765 | 2024-10-04 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d84294-9a7f-3f09-a2bb-aeb1cfa8f13b | -2.29806 | -47.89061 | 2024-10-04 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd9854c6-2008-34ae-9e64-5c4223763a64 | -2.29506 | -47.89242 | 2024-10-04 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab90f51d-f789-38bd-a3b7-2d43e0dec785 | -2.29337 | -47.8898 | 2024-10-04 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 207ed071-1214-362b-993e-42810702189c | -1.38449 | -48.97436 | 2024-10-04 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4fd2501-7150-303d-a017-25ed66890b68 | -1.37884 | -48.97663 | 2024-10-04 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60d7ca1-840a-3771-9913-bbcf70317561 | 3.23376 | -51.21409 | 2024-10-04 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff1a9a5e-a1c7-330a-9436-1d5f267ed625 | -3.71406 | -38.66827 | 2024-10-04 04:06:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68ae586f-4660-3ba3-a769-db812724d3c0 | -3.656 | -39.81073 | 2024-10-04 04:06:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41ec3628-6fc5-368c-8906-a18cf24182ce | -2.94718 | -41.74804 | 2024-10-04 04:06:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 92acbb38-34f4-39ef-88e4-b9e0b96ee437 | 3.233 | -51.20897 | 2024-10-04 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d62fe1e2-dc3e-3d10-8806-4eb606d6aa2f | 3.23223 | -51.20375 | 2024-10-04 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8290661d-0a13-3eb7-8dd8-7d507755cd59 | 3.22662 | -51.20984 | 2024-10-04 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 441b1e35-5159-3ae2-b38c-46c50e96bea4 | -11.0914 | -46.5294 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 1be3a9a6-1254-310f-8b2f-0db2cb565620 | -11.0918 | -46.5069 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 228a2f17-369c-3c45-96dd-1282cb45ae04 | -11.0921 | -46.4843 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1379a515-4b68-3368-94bb-bda27be3efea | -11.1105 | -46.5269 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 63080c24-a26f-3fe4-a37c-f32f77a62014 | -11.1108 | -46.5044 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |


[Clique aqui para ver as próximas entradas](README58.md)
