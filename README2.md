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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e46c1d3b-0a54-34ed-844e-3cad4758a7d5 | -9.0139 | -47.4605 | 2024-10-16 00:15:57 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ea7a4599-07f3-36c2-98ea-588e14013fbc | -9.1543 | -65.3951 | 2024-10-16 00:15:58 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| da4bb7d6-02a0-3053-908f-884b35939ea6 | -9.1727 | -65.4132 | 2024-10-16 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ac778b2a-1d7c-3cac-bdb2-306c18eaa35e | -9.1728 | -65.3945 | 2024-10-16 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 8bcc2c5b-2396-3ffc-a2b3-80b6dcc479fd | -9.1914 | -65.3939 | 2024-10-16 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 56409d7c-c0ab-32dd-ae23-21655c1190ab | -10.822 | -49.256 | 2024-10-16 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2c1ca023-c105-38e1-bcc1-e181fcd02b6a | -10.8224 | -49.2343 | 2024-10-16 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e15c75c8-aa12-3b3f-b7a2-74530cd400ea | -11.6915 | -65.2432 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 55be889d-7615-3edb-8389-e2c271691be1 | -11.6917 | -65.2243 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.9 |
| ca447202-0611-3e6c-a33b-e48ff3cee4cf | -11.6918 | -65.2054 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1774ad7f-932e-3f92-a381-5abe0f7e62d6 | -11.7103 | -65.2424 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 99b8069f-a5ae-3611-ba50-8d7c2c0fd3af | -11.7104 | -65.2235 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| fca29b96-1f4a-30ee-9c3e-89cb7c21cf6b | -11.7106 | -65.2046 | 2024-10-16 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8131304b-4abc-3c2a-9bbd-7122bfe92a92 | -12.0427 | -46.7161 | 2024-10-16 00:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e8bc27a3-bbdf-316a-8c46-451c5014de64 | -12.0431 | -46.6935 | 2024-10-16 00:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 833a2844-7968-31f8-b672-ece57f58458d | -12.0619 | -46.7134 | 2024-10-16 00:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 1f64b38e-e56c-39ce-88e2-2f0d0575efc2 | -12.0623 | -46.6908 | 2024-10-16 00:16:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 323a903e-4d65-3a9a-8f86-2a487fdfe963 | -11.9381 | -64.8729 | 2024-10-16 00:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 09b96f83-59f5-3263-8513-38ab0e2885e5 | -12.3795 | -63.7103 | 2024-10-16 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2dff3ec9-5dcf-3b77-b28c-3eef6d2a007c | -12.3983 | -63.7093 | 2024-10-16 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ea2add2c-c919-3471-a11e-75771bb7e067 | -12.4602 | -63.0361 | 2024-10-16 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 172b43de-57b5-3728-a6f5-97bd3c38e640 | -12.5149 | -63.2822 | 2024-10-16 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1e111d4f-adb9-3a8b-afb6-8fb704d7c7de | -12.515 | -63.263 | 2024-10-16 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cf58a394-8388-32d5-929a-414375aeccfe | -12.5338 | -63.2812 | 2024-10-16 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b07a38a5-a17a-3a6c-b160-afb7462842c5 | -12.9757 | -62.448 | 2024-10-16 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 622e6c7d-fe18-3746-95c9-16370d01c1d0 | -12.9759 | -62.4287 | 2024-10-16 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0a7f532d-e531-31ee-90b4-395cd4e18d0e | -13.0325 | -62.4638 | 2024-10-16 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 12ca77f3-6faf-3989-885b-97dedeb5c917 | -13.0326 | -62.4445 | 2024-10-16 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2839eaec-372a-3f8f-80af-a988ecb5afd6 | -13.383 | -46.947 | 2024-10-16 00:16:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b0d21469-a385-39e5-87d0-829943f3799b | -15.6612 | -59.975 | 2024-10-16 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| dc749fd6-0d58-366d-959d-495c7ce75660 | -15.6615 | -59.955 | 2024-10-16 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3b30068d-3c57-3683-a6c4-95b9f40dfae5 | -17.2439 | -42.6575 | 2024-10-16 00:16:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 6f2b32f5-7a9b-3eb5-a9fb-a1132df51e45 | -17.2639 | -42.6527 | 2024-10-16 00:16:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9f6a4858-457e-33f3-87be-26d3275df654 | -17.0066 | -58.2934 | 2024-10-16 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.6 |
| 8318d633-d4f4-30ca-acfe-7f3af4b6531c | -17.0262 | -58.2912 | 2024-10-16 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 64b5f4f9-7ce1-3b4c-8824-9d9483078692 | -17.0678 | -56.8764 | 2024-10-16 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 410a6e70-6bf2-3720-a7ff-fabbe8be17f8 | -17.0682 | -56.8558 | 2024-10-16 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 2bea94d5-3d9e-30b8-8afc-ce02e6db944d | -17.1754 | -57.4995 | 2024-10-16 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 447428ec-4621-3ce4-b76c-59140a02a4e6 | -17.1758 | -57.479 | 2024-10-16 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| c49b4988-7363-3a26-bd42-dbda1e066621 | -17.1951 | -57.4972 | 2024-10-16 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| 07b303f9-9cbc-313b-ab5e-1da59338289d | -17.1954 | -57.4767 | 2024-10-16 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.0 |
| e8cff791-e274-36f1-9c82-4e52c2eeae12 | -17.196 | -57.4357 | 2024-10-16 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| e4253dc8-3693-34bf-b25c-21394ffe677e | -17.2177 | -57.3102 | 2024-10-16 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 86bf7db9-a5be-3073-adfa-986cfefee54e | -18.2544 | -56.5821 | 2024-10-16 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 4c354996-98ab-33f9-9239-f3bb45f80902 | -18.2742 | -56.5795 | 2024-10-16 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.6 |
| e9e7a64d-795e-3486-901e-710b3fab533e | -18.2746 | -56.5587 | 2024-10-16 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| f3bc7c50-6507-31bb-9758-b7b88c8d8b3e | -19.5414 | -56.9708 | 2024-10-16 00:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 8108613e-7d91-3a1a-b7eb-a709c4d379f0 | -19.5615 | -56.968 | 2024-10-16 00:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 202.2 |
| 601d951a-58ed-3e57-a448-7f962b5bcac5 | -19.5619 | -56.9471 | 2024-10-16 00:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 42f68c53-5e8c-3db7-b827-c2916305e569 | -19.5816 | -56.9653 | 2024-10-16 00:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.8 |
| 64105622-afee-3090-8f5e-2769840f0fa7 | 1.0016 | -52.2164 | 2024-10-16 00:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3f861a5c-6aeb-3543-922c-b6ab167e0247 | -3.1098 | -54.2464 | 2024-10-16 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5854c4e9-921c-399d-b0ff-fdeeff07ce54 | -3.1099 | -54.2263 | 2024-10-16 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 777cc836-1056-3379-acb4-db35c926c1ea | -3.11 | -54.2063 | 2024-10-16 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7fa579ad-f068-33cc-abe7-4f7e001a59a9 | -3.1282 | -54.2459 | 2024-10-16 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 07f19203-3bf8-3d95-b0ed-faf4bd793f6f | -3.1283 | -54.2259 | 2024-10-16 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 16951237-63c3-3097-9b6a-b1b6c0dba12e | -3.2225 | -48.9306 | 2024-10-16 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1bc7a61c-855e-3201-9707-dbcd413d26a9 | -3.2226 | -48.9092 | 2024-10-16 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3bbde530-bc2c-345c-913c-1e5d4a12e92a | -3.2695 | -50.9327 | 2024-10-16 00:25:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7eb71288-8d9e-3de0-81e2-26be9a59b5a0 | -3.288 | -50.9321 | 2024-10-16 00:25:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 2d216fd9-b99c-3b7b-95c4-eaf6023602bc | -3.5107 | -43.2429 | 2024-10-16 00:25:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 15920888-831d-349b-adbc-3469ac57196a | -3.958 | -46.4442 | 2024-10-16 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| d3cb352d-62ff-3fd2-b250-142093ba26e1 | -3.9581 | -46.422 | 2024-10-16 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 6490b4ff-fb1f-38fc-b233-4e6cd1b1bd34 | -3.963 | -45.597 | 2024-10-16 00:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 93d2abcb-c276-3ac2-807b-061dd3732070 | -3.9816 | -45.5961 | 2024-10-16 00:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 0b23c1a7-d791-35cb-a659-1d3bd2511eae | -3.9817 | -45.5737 | 2024-10-16 00:25:28 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9d4fa1d7-e14b-36cf-b763-edf2b23db126 | -5.2306 | -47.9566 | 2024-10-16 00:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| fb51e50b-53a3-341b-a030-d58dcb55e27b | -5.4991 | -46.9121 | 2024-10-16 00:25:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 7d68198d-cdff-3fb4-af06-424675d22f02 | -5.4993 | -46.89 | 2024-10-16 00:25:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0f619fab-f095-3fe4-9a0e-0ea5fc2cf621 | -5.5178 | -46.9109 | 2024-10-16 00:25:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 1efd6592-2d82-3f38-8aed-90429984ba09 | -5.5179 | -46.8889 | 2024-10-16 00:25:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 354.0 |
| c15f9679-6eaf-3d3b-868a-78c420d51701 | -9.1328 | -47.0054 | 2024-10-16 00:25:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 35936365-6317-3c3e-94e6-fdb11588f4f1 | -9.1514 | -47.0257 | 2024-10-16 00:25:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9045b4d1-1b3c-36ec-af3d-a1724ec831d5 | -9.1517 | -47.0034 | 2024-10-16 00:25:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7d76d6b9-f3f8-3d1e-96aa-c1290feab4ed | -9.1706 | -47.0014 | 2024-10-16 00:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 86d5e7a0-f818-3117-8862-0dd5f8f04b9e | -9.1709 | -46.9792 | 2024-10-16 00:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 602feea0-4ae9-3943-ae65-6473affbf344 | -9.4574 | -40.3641 | 2024-10-16 00:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 192.1 |
| a5e9e1fc-8480-3c97-862d-87fe129a0a45 | -9.4578 | -40.3392 | 2024-10-16 00:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 17c36402-2ac3-392f-9af7-9aae6cd6a553 | -9.1727 | -65.4132 | 2024-10-16 00:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| dbbade30-2e15-347d-9494-efac98b7e4ef | -9.1728 | -65.3945 | 2024-10-16 00:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.2 |
| a6c7c186-221b-31ec-98bd-c05e51bcae6c | -9.9588 | -47.3816 | 2024-10-16 00:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d74aee55-39aa-390a-bb90-2465c9b72563 | -9.9777 | -47.3795 | 2024-10-16 00:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d29a2988-acff-312d-87b0-e45356ee4476 | -10.2442 | -47.2824 | 2024-10-16 00:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 63dd6916-1345-3086-b2b7-1000faeb5cf9 | -10.822 | -49.256 | 2024-10-16 00:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2929b93f-b618-3c99-954a-420702d57086 | -11.6138 | -47.2235 | 2024-10-16 00:26:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ae48ba2e-33b8-3a06-a5be-512a33156d74 | -11.6915 | -65.2432 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 54089c6e-c0dc-3977-a6c0-0eb3e985bf2b | -11.6917 | -65.2243 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 911726c7-8a38-39a1-bf36-b04b60c8b05b | -11.6918 | -65.2054 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ae78a752-8d37-3dde-8ff7-d226f5ea9a24 | -11.7103 | -65.2424 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3f574908-faa5-3413-8cd4-67a732dc78a2 | -11.7104 | -65.2235 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3ba71dc2-ff02-313d-ad63-6eeeb36fd917 | -11.7106 | -65.2046 | 2024-10-16 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 688cad07-0211-32b0-9d7b-60d312c54df6 | -12.0427 | -46.7161 | 2024-10-16 00:26:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 713b7a82-030c-35f8-bd1b-2214957b1793 | -11.9381 | -64.8729 | 2024-10-16 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 14264c8a-ae3e-3ea6-8891-5f8e94ff18f8 | -12.004 | -63.5199 | 2024-10-16 00:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 27491bf0-e3dd-3e07-9c8e-fc6c644d449f | -12.0041 | -63.5008 | 2024-10-16 00:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 11919be2-37f8-3bb1-b006-e7e204cd2ae2 | -12.3793 | -63.7294 | 2024-10-16 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ad68f8b1-6d06-3baa-ac8e-01bf26359fea | -12.3795 | -63.7103 | 2024-10-16 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 118.7 |
| f3d4b031-7c59-3b58-98e5-a3a11fb2a0f5 | -12.3982 | -63.7284 | 2024-10-16 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| d1f97173-9d5a-341a-ae54-0b4e4867689d | -12.3983 | -63.7093 | 2024-10-16 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 8f2e572e-3f7c-3df3-92ef-477316a699b0 | -12.9759 | -62.4287 | 2024-10-16 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |


[Clique aqui para ver as próximas entradas](README3.md)
