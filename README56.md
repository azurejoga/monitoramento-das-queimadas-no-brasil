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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a863a1-b9c4-3524-b1c5-16ff8c2ae2f7 | -20.121 | -43.5219 | 2024-10-04 03:36:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| da79b342-9ad0-3204-9312-3d35c9dd046c | -21.8168 | -48.4581 | 2024-10-04 03:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7265ebb3-c561-3aa1-bdec-8b9a55b04dae | -21.8397 | -48.3826 | 2024-10-04 03:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 111.7 |
| b04aa53d-fe76-3c59-8c94-21cf6ab59fb7 | -3.2349 | -50.3695 | 2024-10-04 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c24bdeba-c284-3c17-82ca-1f6bde5fb129 | -3.3665 | -42.3112 | 2024-10-04 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 3031f107-9c05-37c9-9edb-f602b2bc310e | -3.3667 | -42.2875 | 2024-10-04 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 189.2 |
| df2ea64c-3288-3077-b064-5b37773bf34d | -3.3852 | -42.3103 | 2024-10-04 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 3ad566d0-49cf-32ef-9b6e-65d167a5370d | -3.3854 | -42.2866 | 2024-10-04 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 64b0bb50-1bbe-33a1-99be-f65617851b19 | -3.2899 | -50.4725 | 2024-10-04 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 5ffeb3db-01a6-3bc2-90ed-07786d2f560d | -3.2899 | -50.4516 | 2024-10-04 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 7876f666-e9b7-307b-b898-5e0b0359b7d2 | -3.3083 | -50.4719 | 2024-10-04 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 67064b01-30d8-3f3c-9fd0-485a7ed9dc16 | -3.3084 | -50.451 | 2024-10-04 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 186.4 |
| 606b9dde-4f18-3b8b-a2d2-51e8ecd8d374 | -4.0763 | -48.4902 | 2024-10-04 03:45:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| cfa26242-bdaa-3c89-88be-a7184596feb6 | -4.0949 | -48.4894 | 2024-10-04 03:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| dbcf2349-79ba-30b5-901f-e68a2f0d59aa | -4.095 | -48.4679 | 2024-10-04 03:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9e668c34-a98b-3847-b2ad-7ab70cc17e32 | -4.5375 | -43.304 | 2024-10-04 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 11f4cead-9900-326e-8986-5e6803f09fdc | -4.6684 | -45.8961 | 2024-10-04 03:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e22b458a-8779-3846-9297-f43d71d674aa | -4.6686 | -45.8738 | 2024-10-04 03:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 160.0 |
| ffabe0ce-2d5d-32a6-a9ca-7db5228877e4 | -4.687 | -45.8951 | 2024-10-04 03:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 69fcbb8c-2845-31ee-b61c-36f9a6c2477a | -4.6872 | -45.8727 | 2024-10-04 03:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 214.0 |
| e5dab467-4705-30df-beab-e93fa30aed1e | -7.6074 | -45.543 | 2024-10-04 03:45:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| aba67010-a742-3bf4-a309-76836f201cee | -7.6259 | -45.5639 | 2024-10-04 03:45:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| dd35246e-78eb-35ae-b9fe-b16544e08b08 | -7.6262 | -45.5413 | 2024-10-04 03:45:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 434.3 |
| 758da723-1a41-33a2-ae61-0e926de4c046 | -7.6264 | -45.5186 | 2024-10-04 03:45:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1ac20cf4-3db8-3d1b-b1ee-11e414363f33 | -7.8539 | -45.3611 | 2024-10-04 03:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 13716b96-5091-3c5f-86bd-f22b4d0b7320 | -9.3115 | -50.8203 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 8d8e9bea-2462-3a05-a7be-221bcab0613f | -9.3118 | -50.7991 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 206.7 |
| 44582616-2f8f-3949-9aa3-397340c9d2ac | -9.312 | -50.7779 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ac274725-a2f4-30bd-9fe1-524a077abde7 | -9.3303 | -50.8186 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 1cf4ae38-9327-3844-b395-f2750361c1f5 | -9.3306 | -50.7974 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 334.4 |
| 4b3e2de3-2ce4-33b5-bf17-f0856a488798 | -9.3308 | -50.7762 | 2024-10-04 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0cd8ca23-103d-3c6f-bd3e-3b3f4d26586a | -11.0914 | -46.5294 | 2024-10-04 03:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3ef660ce-9104-3e05-b1ff-02460ffd20c8 | -11.0918 | -46.5069 | 2024-10-04 03:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8f04e1c3-17eb-3dfa-8bec-6dbf8458c391 | -11.0921 | -46.4843 | 2024-10-04 03:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4bc25825-9e0e-3010-8e1c-a97326dd7786 | -11.1108 | -46.5044 | 2024-10-04 03:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| be68a493-a98d-30e6-8031-327f7a931d70 | -11.1112 | -46.4818 | 2024-10-04 03:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 4aa4a713-c3ad-3a06-8dbd-79ff2c068aa5 | -11.8242 | -56.6009 | 2024-10-04 03:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 35396977-2aa1-31cd-b717-a14ff39d71be | -11.8244 | -56.5808 | 2024-10-04 03:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a2cd1100-08e5-336a-91aa-dbf656381edd | -12.5898 | -53.1359 | 2024-10-04 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| e5e04461-bb82-34d0-9768-8d29cb02c7d2 | -12.5901 | -53.115 | 2024-10-04 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 27e77417-e4dc-3cf2-b6ba-93bd6c8313d9 | -13.1587 | -48.6764 | 2024-10-04 03:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b972143d-758c-3918-a819-e845d9ca9aea | -13.0598 | -51.1195 | 2024-10-04 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 668c1f8d-8693-3e6f-b486-f0d1e58f7129 | -13.0786 | -51.1385 | 2024-10-04 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6cc002c0-e4b6-3084-9402-58cd87dafc1b | -16.5935 | -57.1988 | 2024-10-04 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.6 |
| c94c1a72-e579-3f2c-a132-e181f78c1ea9 | -16.5938 | -57.1783 | 2024-10-04 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.1 |
| d845e059-60ee-3aa0-95ff-f45fd92332ba | -16.613 | -57.1965 | 2024-10-04 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 176.0 |
| 7793ab92-8f06-3a03-a8fa-b1d5ffd2dbb3 | -16.6133 | -57.176 | 2024-10-04 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| 64b07b84-64cc-3669-9b38-965fbe897180 | -16.6868 | -57.4741 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 42291b2e-6f22-3e67-bc17-bfe8cfaea22a | -16.6871 | -57.4536 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 3e4c29f0-684c-38f1-9f3c-d84a600db876 | -16.7259 | -57.4696 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| ebfaaeb3-e53d-3a51-b069-38b7abd06696 | -16.7455 | -57.4674 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 27df84ad-0d46-3f01-8820-2bfc453f21e4 | -16.7647 | -57.4856 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 98512eae-5ab7-3d58-a3a4-7a96854651b9 | -16.765 | -57.4652 | 2024-10-04 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 68041ccf-62f7-3f39-b142-0e105efdff09 | -16.7859 | -57.3811 | 2024-10-04 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| e16d296c-34b4-3ddd-bcc0-509353217dea | -16.9283 | -55.8405 | 2024-10-04 03:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| d24fae56-4924-38d3-8488-3760ef6d3e75 | -17.1085 | -56.7892 | 2024-10-04 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| afdc967b-c23c-3c46-bb99-ac12d168002e | -17.0888 | -56.7915 | 2024-10-04 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 69958975-dd9d-3670-b8ff-8ff8e0081cc5 | -17.1574 | -57.3993 | 2024-10-04 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 824c28e7-2c0a-3ea6-9ec9-c033cada1f5d | -17.1771 | -57.3969 | 2024-10-04 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 5bd477fb-131c-36bf-8bb6-f30b1d4fa396 | -17.7307 | -43.8127 | 2024-10-04 03:46:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| df8bb913-8973-3d2e-8ea5-517668859431 | -17.7508 | -43.8079 | 2024-10-04 03:46:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d787e7b3-b239-3eea-a888-95f0c7a7a54b | -18.8613 | -43.5837 | 2024-10-04 03:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 7daea471-4a87-33a6-bd1e-53c4d2c5475b | -18.9081 | -42.0315 | 2024-10-04 03:46:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.2 |
| 8abc2045-3164-3079-8f98-7986e2e3fbfb | -18.9285 | -42.0259 | 2024-10-04 03:46:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 47c8fd6d-3289-3692-a273-4b674f5bdeec | -19.0148 | -43.1749 | 2024-10-04 03:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.4 |
| e8c7327c-25fe-3474-8007-27ed03152828 | -19.0344 | -43.1944 | 2024-10-04 03:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| aa896450-c159-3fa5-8e21-35461e4b4493 | -19.0352 | -43.1695 | 2024-10-04 03:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 62ac616a-47b2-3fcf-8985-760ffb53f325 | -19.3159 | -42.5976 | 2024-10-04 03:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| e3eb9735-d8e5-316b-be19-cb4f93924d00 | -19.3167 | -42.5724 | 2024-10-04 03:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 80c7b2c3-08b3-3f1d-a67f-165b16a387d3 | -19.3363 | -42.592 | 2024-10-04 03:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 934278bb-2799-37ec-9e54-72ab8eadee18 | -19.4899 | -42.8746 | 2024-10-04 03:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 6b49408f-8d9c-3ba6-9e9e-29fd41058b3a | -19.5104 | -42.8691 | 2024-10-04 03:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 320a82ea-fc32-320f-84ea-77d55e86dab7 | -19.831 | -42.3796 | 2024-10-04 03:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.4 |
| 0341f5d6-d2bf-383b-9fcb-a33cef035aaf | -19.8516 | -42.3738 | 2024-10-04 03:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 321.2 |
| db884834-fad5-3f32-b0c5-5b0149cac105 | -19.8524 | -42.3484 | 2024-10-04 03:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.3 |
| 1ace43f1-4c8a-3727-be31-c8bc3bf5ab3f | -19.8721 | -42.368 | 2024-10-04 03:46:55 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| eb241692-a38b-3388-8dbc-b9aabef4dc5b | -21.7773 | -48.3976 | 2024-10-04 03:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4b734a97-db09-3278-9549-2a87b4d39900 | -21.778 | -48.3741 | 2024-10-04 03:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 82.3 |
| afd6d7bf-f8d1-3604-8775-93e7f2195f9d | -21.7981 | -48.3926 | 2024-10-04 03:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3140bd9f-1c94-3f29-942b-2e1fd96c4f0d | -21.7988 | -48.3691 | 2024-10-04 03:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 87.6 |
| fa618a8f-aa5a-3e1b-ad73-c7a5146382b2 | -21.8397 | -48.3826 | 2024-10-04 03:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fe58015c-5720-3d65-bf9e-2cb08b0b4ee3 | -3.3665 | -42.3112 | 2024-10-04 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 115.5 |
| c607e3a8-69d8-3385-810b-d1cd43ad26b5 | -3.3667 | -42.2875 | 2024-10-04 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 225.6 |
| 6622c566-b301-3adf-8331-eb5fedb63f39 | -3.3854 | -42.2866 | 2024-10-04 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 923d1a12-1887-3c39-9e83-6b1f5f8a2c37 | -3.2899 | -50.4725 | 2024-10-04 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| ee0930bf-5166-3768-abc4-525797e9f92b | -3.2899 | -50.4516 | 2024-10-04 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 196.9 |
| b7abf0ba-d193-37de-a7e2-d39a11f5d92f | -3.3083 | -50.4719 | 2024-10-04 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| b4985669-5438-3796-aeb4-069019e0624c | -3.3084 | -50.451 | 2024-10-04 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 732ab0ee-8325-359c-a5b4-a2013c4723f7 | -4.0763 | -48.4902 | 2024-10-04 03:55:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f7f3f7ae-d346-37a1-9f9e-7df4a95ce1bf | -4.0949 | -48.4894 | 2024-10-04 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 62a33dbf-3508-3c02-bb81-170c41d53b92 | -4.095 | -48.4679 | 2024-10-04 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1817af30-4160-33df-9ee1-bdc02a171f9c | -4.5375 | -43.304 | 2024-10-04 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f69be723-e606-3b52-97dc-1dc8ec4cb125 | -4.6684 | -45.8961 | 2024-10-04 03:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5c557b5b-fe9a-311a-98a7-84151f6f150b | -4.6686 | -45.8738 | 2024-10-04 03:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 160.2 |
| cd1c81a1-1153-3ebb-a4fb-809619d2ada1 | -4.687 | -45.8951 | 2024-10-04 03:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 5c0fb29e-9ff1-3eb4-b78d-d6a2539cd959 | -4.6872 | -45.8727 | 2024-10-04 03:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 40d26e06-8633-34f9-abc3-504cedecf06c | -7.6262 | -45.5413 | 2024-10-04 03:55:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 743baba2-7ef3-3857-9a26-f823f785a3c8 | -7.8539 | -45.3611 | 2024-10-04 03:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 15310914-c5be-378a-bcb1-71dda2820c49 | -9.3115 | -50.8203 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 50f77738-a87f-3b2a-9dac-6eb878daccbd | -9.3118 | -50.7991 | 2024-10-04 03:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |


[Clique aqui para ver as próximas entradas](README57.md)
