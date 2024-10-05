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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a4de77d-4da8-3700-9535-0adc36bc9f1d | -17.1178 | -57.4244 | 2024-10-05 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 0b519fec-052b-387c-bd5f-e0127048a497 | -18.484 | -52.9309 | 2024-10-05 10:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1de7a6de-5828-3d10-8914-e351f54895b8 | -18.4844 | -52.9092 | 2024-10-05 10:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 256.7 |
| cf1fd7b5-bcc2-3d59-8b63-6f3cc9983523 | -18.4849 | -52.8876 | 2024-10-05 10:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| e030eee6-2ed7-3fc9-b7be-6e82e163150e | -18.5044 | -52.906 | 2024-10-05 10:36:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 204922fe-39b6-3ea6-8cb8-b318b7488263 | -18.5048 | -52.8843 | 2024-10-05 10:36:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 6da4d675-f799-3405-9b97-9b398773988b | -18.6586 | -57.2759 | 2024-10-05 10:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 1074fe58-e00c-3c1b-ad05-54869bdd3686 | -18.6785 | -57.2734 | 2024-10-05 10:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| ab1e9954-1aa4-3f92-bc59-a1438e509bf2 | -17.1178 | -57.4244 | 2024-10-05 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 9605629f-6577-3bf7-b841-52a807e1cd4f | -17.1182 | -57.4039 | 2024-10-05 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| a8a92d30-abbd-356b-9f58-8c86f81c8c28 | -17.1375 | -57.4221 | 2024-10-05 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 2465aabd-3772-3740-98da-fa6d3d0c2876 | -17.1378 | -57.4016 | 2024-10-05 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 75cb51de-d0eb-3c8e-bf78-06464c5d9b45 | -18.484 | -52.9309 | 2024-10-05 10:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 7efac82c-b8b5-3aff-8c29-38473178d087 | -18.4849 | -52.8876 | 2024-10-05 10:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 447.2 |
| 19c034c5-f4a7-31e1-9875-6f0c4ecfaf38 | -18.5039 | -52.9276 | 2024-10-05 10:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 2baab409-9b52-378d-a8b1-a49b09dcb874 | -18.5048 | -52.8843 | 2024-10-05 10:46:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 407.7 |
| 14812942-6b1b-3fa0-b37b-4c3c227b56dc | -18.5044 | -52.906 | 2024-10-05 10:46:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 597.8 |
| 1c027036-d4c0-3a06-8c29-26b1f879d778 | -18.6785 | -57.2734 | 2024-10-05 10:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 7a6aad52-fadc-30e0-8531-d1b05411c6f4 | -18.6586 | -57.2759 | 2024-10-05 10:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 500e9a79-2dd1-371f-a820-f774dabee948 | -17.0103 | -56.8011 | 2024-10-05 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 5ec77ccf-74dd-3a7f-ad63-55a9b28c1f80 | -17.0106 | -56.7804 | 2024-10-05 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 46017eeb-7292-32ec-819f-204ab5d8602c | -18.464 | -52.9341 | 2024-10-05 10:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 401f4943-64f6-33d5-96bf-a2dfa64bfb42 | -18.4644 | -52.9125 | 2024-10-05 10:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 68034dd1-369d-30ad-bf90-44be8a243e23 | -18.5039 | -52.9276 | 2024-10-05 10:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 266.0 |
| f9295b58-f716-3655-a23c-44f9541b52c5 | -18.5048 | -52.8843 | 2024-10-05 10:56:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 257.6 |
| c31fb7e9-8c8c-3d88-a7a5-ea01c617808e | -18.6586 | -57.2759 | 2024-10-05 10:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| c008b149-8d18-3f76-a10e-459a245de20e | -18.6785 | -57.2734 | 2024-10-05 10:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| a63a4718-108a-3a64-a807-66e218a76a59 | -18.46 | -52.95 | 2024-10-05 11:03:39 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b01f8ef1-bd98-3452-9633-92fc54b58106 | -18.49 | -52.91 | 2024-10-05 11:03:39 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d051f877-faa4-3b94-980f-ce3e4dce3e6d | -18.49 | -52.97 | 2024-10-05 11:03:39 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 48f4df4b-59cf-338e-9464-34269792ac07 | -6.9514 | -59.0666 | 2024-10-05 11:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ddfb3c15-97e1-3306-b162-2e66b660e5f3 | -10.2901 | -45.4763 | 2024-10-05 11:06:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 09c8c5ec-31d6-3614-91d8-c438bddff245 | -17.0103 | -56.8011 | 2024-10-05 11:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| a067743d-8eee-3271-822d-8f1cb43e51da | -18.6586 | -57.2759 | 2024-10-05 11:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| e051be81-aa76-342f-8ea7-c5b6b44fa741 | -18.6785 | -57.2734 | 2024-10-05 11:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| f38467b2-6702-39d8-b8b3-1fda28b3e310 | -6.9514 | -59.0666 | 2024-10-05 11:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8bcf067d-8195-3b20-862d-6f932f07f6f2 | -8.8714 | -48.3297 | 2024-10-05 11:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 47ed8e97-41dd-38cf-8fa4-46fd2fdd2a7f | -10.2901 | -45.4763 | 2024-10-05 11:16:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| e0a95b35-ff8e-3fe3-88ba-7f92c87ee668 | -12.7627 | -50.5567 | 2024-10-05 11:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 752db0d8-ab2f-389a-8070-8ad18d25102f | -16.554 | -57.2237 | 2024-10-05 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| f40495a2-0c0a-36f3-bb90-7e4dd71442a4 | -17.0106 | -56.7804 | 2024-10-05 11:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 66eefcec-df88-320c-b1f8-8022da2cf1ad | -17.0103 | -56.8011 | 2024-10-05 11:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 431937e8-1187-3894-93d9-33dfd6ccc1f9 | -17.0299 | -56.7987 | 2024-10-05 11:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 3799772c-4ec2-37f6-a2b7-d132deefc143 | -18.5053 | -52.8626 | 2024-10-05 11:16:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8642c68c-4cca-324a-808c-ed38f4696a96 | -18.6785 | -57.2734 | 2024-10-05 11:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 6d4c7111-96e0-33ea-a42b-a3442634b8a0 | -18.6586 | -57.2759 | 2024-10-05 11:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 852ea078-80da-32d3-9aa4-b1c9c2f4fbec | -6.9514 | -59.0666 | 2024-10-05 11:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 687a8059-bcbd-35b0-99b8-0ab7a540646c | -8.8714 | -48.3297 | 2024-10-05 11:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 0b72959a-a7b2-327c-9f18-c7f800ef9d7a | -11.3662 | -47.2113 | 2024-10-05 11:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9fc67d9d-5d07-336c-afc3-58764c0944ff | -12.7627 | -50.5567 | 2024-10-05 11:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b5dae108-c2fb-37c1-8d76-4ed5e2471700 | -14.0572 | -45.1614 | 2024-10-05 11:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ae43d00e-7905-3cf2-ad19-5ed6a3ac81bd | -14.0373 | -45.1882 | 2024-10-05 11:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5cd10be6-a1f2-3e11-8aef-1f7479a112a9 | -16.7647 | -57.4856 | 2024-10-05 11:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 0685350e-c8be-38f4-99e0-9f7be4126473 | -16.991 | -56.7828 | 2024-10-05 11:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 205d8011-7b66-330e-af00-66cf69756b23 | -17.0103 | -56.8011 | 2024-10-05 11:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 8e24c6f6-124c-3eac-825d-98aa20e1fdd9 | -17.0106 | -56.7804 | 2024-10-05 11:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 4a07d3e6-7649-380c-82f4-029ea2c01355 | -17.0299 | -56.7987 | 2024-10-05 11:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 1faee704-e9d0-33a8-b54c-bf44dab6d7c9 | -17.1375 | -57.4221 | 2024-10-05 11:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.1 |
| fdcd65da-91b7-3c1f-a367-009ceb534ba3 | -17.1378 | -57.4016 | 2024-10-05 11:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.7 |
| c9a48698-5e3c-390b-bc15-81ae4752f06a | -17.1182 | -57.4039 | 2024-10-05 11:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.0 |
| ad17a5b1-4841-30dc-9955-edfccd9a0e3a | -17.6273 | -46.9825 | 2024-10-05 11:26:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2a20edf7-df06-36a7-aa77-64fdb4e520a8 | -18.6785 | -57.2734 | 2024-10-05 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.9 |
| ff9ef7a5-8af5-3ad5-92d1-11277fab3069 | -18.6586 | -57.2759 | 2024-10-05 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| a4f217e1-679f-3247-94d9-6e2100b0751b | -6.9699 | -59.0658 | 2024-10-05 11:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 11947992-b181-3845-b6a5-4c2779f87722 | -6.9514 | -59.0666 | 2024-10-05 11:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a864b7ff-a670-3eef-b32e-95e7dbdfb3cc | -8.8714 | -48.3297 | 2024-10-05 11:35:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 568354ca-97fb-33b6-bdae-12a1930dd476 | -9.8545 | -46.7257 | 2024-10-05 11:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 4feedc9c-68b1-3bfe-b9dd-edafdadf4b41 | -9.8858 | -47.1901 | 2024-10-05 11:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 7f31c20f-ae6c-3ac5-8ba9-48fafefbc988 | -9.8356 | -46.7278 | 2024-10-05 11:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| d47a96d0-1faa-3464-a1c4-68e2e542eded | -12.7627 | -50.5567 | 2024-10-05 11:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 017c103d-07ad-3a36-85e4-3a98e4a99524 | -12.8202 | -50.5495 | 2024-10-05 11:36:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 18e64f35-58a9-3ee2-bdbb-6376c76aaabb | -13.1241 | -46.3748 | 2024-10-05 11:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| effee184-e00c-36b3-b785-275f06588b56 | -14.0378 | -45.1648 | 2024-10-05 11:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5b3d762f-ab66-3d02-9765-425a2aa79c7e | -14.0373 | -45.1882 | 2024-10-05 11:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9d06b38f-4266-3e1a-904e-1f479b67d7c0 | -17.0106 | -56.7804 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.7 |
| e47bff8d-16f9-3c49-a8c4-52fdf80f5303 | -17.0103 | -56.8011 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.7 |
| b9d30e60-21e3-3e80-875d-261776e95310 | -16.9717 | -56.7646 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| ad781584-fc05-3015-9c4c-4e22e709db45 | -17.0316 | -56.6956 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| a057309d-9c11-356b-84f9-ce1b5ebcb684 | -16.991 | -56.7828 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| aef3ad2b-eab4-3e37-9408-6cec4be840b0 | -17.0299 | -56.7987 | 2024-10-05 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 74f83d26-51ac-3724-8667-20f077f8f65f | -17.1378 | -57.4016 | 2024-10-05 11:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 176.4 |
| 9500cc5e-fa7d-3c18-9eec-274707d6f929 | -17.1375 | -57.4221 | 2024-10-05 11:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.2 |
| 2b80223e-fecb-35b7-a405-43de26fe157c | -17.1182 | -57.4039 | 2024-10-05 11:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.0 |
| 87848854-ac73-3829-8401-bfd2ddc0eb41 | -18.6785 | -57.2734 | 2024-10-05 11:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.6 |
| 1586a756-6367-3338-8ab7-d4ff11084f69 | -18.6586 | -57.2759 | 2024-10-05 11:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.0 |
| a4d3317a-c9b2-3cd2-90da-41ef9eee856b | -6.9514 | -59.0666 | 2024-10-05 11:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 688c71f2-310e-3eef-895b-3591a744742f | -8.8714 | -48.3297 | 2024-10-05 11:45:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| dc224e2a-465e-350c-8133-227585979999 | -8.8738 | -45.1875 | 2024-10-05 11:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5f133e8e-ae02-3ff8-87bd-f4d6e1dde4ad | -9.8545 | -46.7257 | 2024-10-05 11:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3a80dbbb-29e6-3536-8be8-f3f9bbcf729c | -9.8356 | -46.7278 | 2024-10-05 11:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 73a9ae60-b987-32e2-a7ba-2b335d52fe8e | -12.7819 | -50.5543 | 2024-10-05 11:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| bcd92129-4bab-3feb-9da5-a0d50617a0d2 | -12.7627 | -50.5567 | 2024-10-05 11:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 9bf09bff-96ca-32d1-9e84-9982e6c8f20a | -13.1241 | -46.3748 | 2024-10-05 11:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b9db5b1e-3e1d-3ddc-836a-433e70076933 | -17.0299 | -56.7987 | 2024-10-05 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.9 |
| f04a1c45-588b-32fc-b6b6-519c18b2435f | -17.0316 | -56.6956 | 2024-10-05 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| bef7be5d-c6b4-3699-be53-9ce658c90a03 | -17.0303 | -56.7781 | 2024-10-05 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| cc1a690d-41f0-3da9-b485-19723aca57aa | -17.1378 | -57.4016 | 2024-10-05 11:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 184.3 |
| d963e8eb-caf4-3a55-89ac-a97e523d02bd | -17.1375 | -57.4221 | 2024-10-05 11:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 179.6 |
| 0f9f67a8-7298-3f0e-b67a-2acacef6d9d6 | -17.1182 | -57.4039 | 2024-10-05 11:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 177.1 |
| a6c5e4ad-c469-33b1-9809-eabaf5ec6e0d | -18.6586 | -57.2759 | 2024-10-05 11:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |


[Clique aqui para ver as próximas entradas](README157.md)
