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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cac9957-ff0b-392f-b601-0581799a9a1f | -17.27244 | -58.11796 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 52d3d402-9754-32d7-bb1c-6bc9b9bcce0b | -14.24084 | -60.17114 | 2025-10-08 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 919fb273-e00a-3b63-930f-62dfc1a52090 | -17.93414 | -57.50515 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7b285473-d591-3b5d-9986-b8c6bb3de9a9 | -13.20733 | -51.64804 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71494ac9-2618-3e59-bedd-c56494058f63 | -18.05726 | -57.53057 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad6af04e-41c3-3095-93cd-c3d4023cf453 | -15.61424 | -52.58094 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 50cfb122-488d-3a01-8136-e7cb396dcc65 | -13.20677 | -51.6532 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9100aa1-b89e-3023-8ade-101aa32a8b54 | -18.05803 | -57.52374 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d3855857-2a1e-3ee0-9ce1-36ce5d0a3306 | -12.92829 | -54.72114 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07e019ee-a5ec-3589-9fea-b1129c09265d | -12.90594 | -54.73126 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc6a64cc-682f-3ca8-a0ce-9328d6e5ec02 | -12.88699 | -54.74728 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84535aef-c0e6-37be-a4cc-2778c8872247 | -17.26804 | -58.11735 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5d1585b8-797b-34ca-9379-6934e27ca75c | -12.40652 | -63.89445 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caf5a796-1f63-36e5-adc1-c79d38e58b74 | -12.87856 | -54.73 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c03133cc-6a6d-3d2b-922b-64e185ad855a | -15.64135 | -52.5554 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32e42c1e-5d3c-3f5a-a781-c7f7ddce7df1 | -12.8866 | -54.75042 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb9ce66-1be8-3521-9e34-a39969d35d69 | -17.85805 | -57.64048 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5c99a106-a3a6-3b93-afc6-c927aae163b7 | -14.85493 | -59.65738 | 2025-10-08 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73cca385-3778-37e9-bf48-3cf5b7339d4f | -17.92917 | -57.515 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ad3375fb-e898-356e-8777-d9869e82a22a | -13.46206 | -60.97929 | 2025-10-08 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1540ada1-8e1a-3ba8-829a-e477f2fed7d2 | -15.20997 | -56.78537 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e725e4b-fe5a-3f8a-8bf4-903c56acf89e | -15.99599 | -59.54156 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd99501f-2f16-355a-9a9e-262e3202ac07 | -12.33721 | -64.245 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3cbd51d-375c-325c-b86c-0fc9e446b191 | -15.2278 | -56.75708 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2e2deb4-eb8a-313e-a2af-ebd14c694e63 | -12.90377 | -54.7398 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56cdf118-263d-3c2f-8ec8-f3418b206061 | -18.02367 | -51.1483 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b60c9f0a-de33-327e-a47d-f8c132cd6efe | -15.20166 | -56.81384 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 773e362e-ef15-3d77-bc3e-6782a69c607a | -15.20597 | -56.77938 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4906c801-f53c-362a-b57f-2d23d8278287 | -13.21423 | -51.64396 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d8edfe9-1cc8-3da9-9c21-18c7d4f51fd1 | -12.43916 | -54.22267 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f74f70-99b1-30c1-922a-a91369104067 | -12.88219 | -54.74339 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 308ba0f7-1400-33cf-9f00-e0cc29ebdf6d | -12.93389 | -54.71851 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30f6cebd-38ce-3fe7-8240-c3b6a78e2194 | -12.89296 | -54.74171 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9d0a446-eb7f-357b-87c0-85bcf61816e4 | -15.63322 | -52.57373 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bda2c171-796f-3f3e-b8d4-667b7aec3f97 | -16.60502 | -58.15513 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4070f004-d1f7-3379-8686-d4423fa52aa0 | -12.90479 | -54.74101 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 258d7024-f374-3535-9eab-3d9c113675f4 | -15.12122 | -59.0281 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a93148d-533c-3f08-bd82-14a66a3d16d1 | -18.01645 | -57.56292 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d08932ed-e847-367c-9259-5bd2a1918801 | -17.85751 | -57.64495 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3db677d8-946f-3c67-99d4-ae2c2ead5d29 | -12.89257 | -54.74487 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 265c4901-4908-3d47-a20f-4633287701e7 | -12.88376 | -54.73071 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98e6e8be-22f9-3180-804d-656e0c2b982e | -15.63432 | -52.56289 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 85c7235d-9d0f-3f3f-85e3-32f087638423 | -12.64116 | -50.56142 | 2025-10-08 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad100bb6-a06e-3b27-8259-cd332ac51cc5 | -18.01905 | -51.03655 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8619f1c-9e78-304c-9fa9-e22ef417a072 | -17.92886 | -57.51034 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1347c7c7-c27f-3ae8-a6c2-5b3df82c1eb3 | -12.88777 | -54.74101 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4eac774b-1476-3999-bd89-13b37fa439b1 | -12.90977 | -54.73407 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a803fbfa-983b-3b4f-b25d-a107a414549a | -18.03692 | -51.15247 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bbe995e-d476-3882-9213-c93e67cd3ea9 | -12.87817 | -54.73316 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 054a5cc2-23e0-3e77-9312-70e6332b581b | -18.02657 | -51.03072 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38a92bc5-27a3-3abf-9b79-9739c7df63da | -12.88896 | -54.7314 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c62ff09f-1eca-38bb-b21d-d5ae0796181c | -17.30223 | -58.05836 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da5b5844-f395-3f5b-bb86-87fa9d297053 | -17.83113 | -57.63214 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 06a6a213-0636-31ef-b807-ece8093e548c | -17.16246 | -56.59798 | 2025-10-08 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| dda82ea6-596f-3e98-92a3-0c1035016b53 | -12.40047 | -63.88986 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 909dedec-3491-3e34-8986-4cd4e3f9982f | -17.86669 | -57.64594 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 26b1d5cc-997a-3bf9-ace2-763e72cab381 | -12.90418 | -54.73655 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6ee6323-31b3-33fb-9d00-11926e658b21 | -18.05124 | -57.54221 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cd4e6f06-3618-3cb3-9c00-63e61be25627 | -17.92816 | -57.51653 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5ebaad02-4ba7-3ff7-879b-2af6595284a5 | -17.85291 | -57.64456 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| db7e5d9c-71d9-317e-89f6-71af3df29568 | -12.89897 | -54.73593 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a968e91-0609-37b3-8ac7-97e6182003da | -17.16115 | -56.60914 | 2025-10-08 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 05c63752-c134-37f1-9c83-96ca30d5beb0 | -17.92843 | -57.52107 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8e2b1da4-81ec-3f0c-bfc0-4becdb9e713a | -17.30167 | -58.06286 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b10644bb-caf9-3a8b-b0ce-da25fb17f076 | -12.89856 | -54.73917 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba5ee46f-be40-310a-90ec-b6a1e698bcca | -12.91018 | -54.73085 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1e53ba7-bca8-36ae-ab43-45297dc2784e | -12.39498 | -63.88176 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b8715b9-cb75-3d57-803f-10bfb6b9b1c6 | -15.22938 | -56.76458 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 432e7c72-4f8c-32e5-9ade-5bd4756e712a | -15.63476 | -52.5586 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5286369c-1aef-3ae2-91c9-8a25906f11a9 | -18.03115 | -51.14191 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e45ba11a-2c96-36c3-b18a-0e796ae5415b | -18.05596 | -57.54186 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 59b9bfa5-7020-3440-a5af-19a6acef91e9 | -12.88816 | -54.73786 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6df04ce1-b579-322a-8f4b-ca85de299a1f | -18.03003 | -51.15584 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 579a5a24-0115-3ac0-bf62-f04f804ad581 | -18.0216 | -57.55908 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 94492ebe-4666-38b2-b18c-ccba105ea2b2 | -15.2238 | -56.75102 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81e03646-0a7d-38a3-9cb9-9aa71cc38441 | -17.82981 | -57.64359 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c48792b8-09c8-3154-928e-1e2f983d71cf | -12.91619 | -54.72509 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b8e6543-7503-321f-9cff-2bf09b191b70 | -17.94562 | -57.52777 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d0f88bd4-332e-3851-b772-aab04b8f235a | -18.03061 | -51.14502 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dece4142-e1ef-3101-b0a1-58befcf8e245 | -12.91578 | -54.72834 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5698844a-d695-3a57-8637-f73c75039209 | -12.91113 | -54.73206 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fe79fb4-6849-3ebe-adf2-c438890c00e7 | -15.15413 | -52.75988 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed90e45-7f5e-394f-b3c8-595a084e5eb5 | -15.21935 | -56.7864 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dc993a8-4fcc-3046-abd9-db194fd84123 | -15.15367 | -52.76435 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d6df1d8-a9af-3969-8cdd-d8153c81b700 | -17.86262 | -57.64111 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 81a0c6b4-7940-3c08-a83f-3ea74b338512 | -17.84953 | -57.59429 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ee7bccc2-e768-3c8d-a7d9-e4758665f104 | -12.18935 | -57.23316 | 2025-10-08 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8217949-de5d-3461-83fd-3596fdfb3df3 | -12.89959 | -54.74035 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46544ebd-1f88-3c65-b3cf-6333556500fd | -14.85335 | -59.65454 | 2025-10-08 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b31f42a-947b-3fb9-8f6c-d50f17b15c52 | -12.4396 | -54.2192 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d54fb2-1d3a-3ace-8c90-ca93a06e62df | -17.8621 | -57.64542 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c325591c-43a9-3c48-98a0-f8c329b2b38e | -18.01963 | -51.02983 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9fca1c0-73da-317d-8e17-b075dad9e1d6 | -15.9802 | -59.53954 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 026cec19-44b1-3563-b2a7-3665d0069fc5 | -12.91099 | -54.7244 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3850540-2c38-3101-b0e2-96f2741ca3e7 | -18.01694 | -57.55882 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7979b943-a0a4-36b5-ab31-53e0f9a2d5a7 | -18.05657 | -57.53656 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2afceca9-beeb-3516-a3e0-1cda35a93ed4 | -12.30164 | -55.10345 | 2025-10-08 05:31:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bbe5a50-2153-3093-9270-7ae1c5a6e5f5 | -17.93627 | -57.52763 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2af80492-3276-3852-a99c-a313ebbf8755 | -17.94095 | -57.52768 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 63395db8-0719-3e19-af49-857b06900bac | -18.00119 | -57.49432 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |


[Clique aqui para ver as próximas entradas](README95.md)
