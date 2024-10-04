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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b602e69-1f69-3f72-b6df-d67ad8ad7dd1 | -17.1574 | -57.3993 | 2024-10-04 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 89ee8ee8-72e6-3fda-89a8-55eee7ea29d1 | -17.1771 | -57.3969 | 2024-10-04 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| a68944a0-4440-3e1d-9e91-45eb119371ad | -17.7508 | -43.8079 | 2024-10-04 03:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c35ecec2-d278-3a24-998c-4c579badc75e | -18.8617 | -42.8932 | 2024-10-04 03:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 5c1fa776-c661-3771-94c3-3f7d72240f87 | -18.8613 | -43.5837 | 2024-10-04 03:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| d71751ba-93eb-3cd8-80e0-c25fb6186aaa | -18.9081 | -42.0315 | 2024-10-04 03:26:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| ae71a394-7a17-332a-b320-377d6de6a7e7 | -18.9285 | -42.0259 | 2024-10-04 03:26:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 06b2851c-4374-361c-b196-e843f6f10954 | -19.0148 | -43.1749 | 2024-10-04 03:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| e34beed7-4c47-3c80-8a0a-d8be26545f7c | -19.0344 | -43.1944 | 2024-10-04 03:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.2 |
| 7e8efec7-2eba-37da-b6a3-274d211475e1 | -19.0352 | -43.1695 | 2024-10-04 03:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.2 |
| fef576f3-de90-38e0-b36a-9d911428c9ee | -19.3159 | -42.5976 | 2024-10-04 03:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.6 |
| 9fd7d9f0-443b-3ae1-9f2d-f3f12d08f105 | -19.3167 | -42.5724 | 2024-10-04 03:26:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.2 |
| c5468477-c771-3b69-8ad3-121ae545d4ba | -19.5104 | -42.8691 | 2024-10-04 03:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 15eaa83e-eb1e-3f1f-93f0-26eca8cca0ad | -19.8516 | -42.3738 | 2024-10-04 03:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.5 |
| 59b27b42-b2e8-3c1a-8aaa-194b2cb3484f | -19.8524 | -42.3484 | 2024-10-04 03:26:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| 1dfbc42f-dd75-3c72-9411-cc6c6d9d13cd | -20.121 | -43.5219 | 2024-10-04 03:26:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| c6fd6575-d174-3743-b510-ce22c1c7e28f | -20.1416 | -43.5162 | 2024-10-04 03:26:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 450ea3eb-d5dc-381b-ab2b-83171ceb81fe | -21.2888 | -48.9302 | 2024-10-04 03:27:03 | GOES-16 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1fd8b75c-5748-3de9-9518-6a6cf5aaceca | -21.2895 | -48.907 | 2024-10-04 03:27:03 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 257.8 |
| ddaf806c-750e-316f-b50a-11328ec72fd5 | -21.3101 | -48.9022 | 2024-10-04 03:27:03 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 318fd880-ecba-3bb8-aea9-98db93788669 | -21.3108 | -48.879 | 2024-10-04 03:27:03 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 250e6a5a-a069-32f9-a7e4-903c62c40edc | -21.2901 | -48.8837 | 2024-10-04 03:27:03 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 136.5 |
| e5cd3a12-32c9-3987-b9c4-a32198802091 | -21.3308 | -48.8974 | 2024-10-04 03:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3e6ef84a-7ea0-3eca-b346-ac5239c42787 | -21.3514 | -48.8927 | 2024-10-04 03:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 85.0 |
| dbc268ea-0b26-34ae-8a2f-5b06f30e5c38 | -21.8397 | -48.3826 | 2024-10-04 03:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a537237c-1e94-3f91-ac25-c160c59aa668 | -2.9014 | -50.7142 | 2024-10-04 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 04e7a70b-628c-365f-9a0e-9e465a29dc35 | -3.2349 | -50.3695 | 2024-10-04 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 65872a88-2ea3-372d-a6c7-8983e0f25071 | -3.2534 | -50.3689 | 2024-10-04 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 60259747-4a5e-3743-bb8d-2b0c351d12a3 | -3.3665 | -42.3112 | 2024-10-04 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 5af4ff2d-907f-326a-a6f7-8609b90f075c | -3.3667 | -42.2875 | 2024-10-04 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 00c3bea7-584b-3a60-8222-3785dfa7cd34 | -3.3852 | -42.3103 | 2024-10-04 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 0f42c224-6c09-34f1-a0c2-b55822f51e04 | -3.3854 | -42.2866 | 2024-10-04 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| d286bc51-8c65-3de9-b516-e9cfce355b23 | -4.0763 | -48.4902 | 2024-10-04 03:35:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 7211ebf7-4eb1-3ed1-8d71-548f33dcad37 | -4.0765 | -48.4687 | 2024-10-04 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b94e7afd-1bbe-39cd-91d2-5e6034424d7f | -4.0949 | -48.4894 | 2024-10-04 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 8afab2db-4621-36c3-9b12-bbdbeef054b3 | -4.095 | -48.4679 | 2024-10-04 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 6e9fc1a1-58e7-3cf0-8f71-eea363f6abf1 | -4.5375 | -43.304 | 2024-10-04 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c5f6ffb7-228e-317d-a81b-beafddbe0c42 | -4.6684 | -45.8961 | 2024-10-04 03:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1302e60c-c8f6-39e6-ba48-0e1ef8aa9094 | -4.6686 | -45.8738 | 2024-10-04 03:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 4eb4671f-3f3f-3505-b065-a0b70783724d | -4.687 | -45.8951 | 2024-10-04 03:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 25ae7cce-58f7-3103-b77c-90b5d066253b | -4.6872 | -45.8727 | 2024-10-04 03:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 306.3 |
| 18a72923-a58b-333e-84ef-ad1494e30a27 | -6.2524 | -44.132 | 2024-10-04 03:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fe84834e-ddb6-3bf9-b0ea-43321a1a4d0b | -7.0529 | -71.7544 | 2024-10-04 03:35:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9c54d555-52dd-31d2-a4ac-efe4e7c97c54 | -7.6071 | -45.5656 | 2024-10-04 03:35:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0f21831c-c693-3ffe-b080-04f4a6cee2f5 | -7.6074 | -45.543 | 2024-10-04 03:35:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 217.7 |
| ac0d99f5-f5d7-318c-9f71-197970ab7539 | -7.6259 | -45.5639 | 2024-10-04 03:35:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9a8e9f3f-839c-31be-b9f8-154b7ee728bf | -7.6262 | -45.5413 | 2024-10-04 03:35:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 249.5 |
| ba9cb421-6687-3477-b595-c12d8fd4442d | -7.8539 | -45.3611 | 2024-10-04 03:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f6d62b15-cf11-326a-8594-9555b3193652 | -9.3115 | -50.8203 | 2024-10-04 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 15e54e3c-5264-3ff7-9388-d519ddeb96b5 | -9.3118 | -50.7991 | 2024-10-04 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 214.5 |
| 7cf3870f-970f-3848-af2a-6c13cc355e4d | -9.3303 | -50.8186 | 2024-10-04 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| e25c4193-9cb1-31e8-bd43-68b271a1e5a5 | -9.3306 | -50.7974 | 2024-10-04 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 322.4 |
| 6263a037-7060-326e-b5f2-3f9e06651770 | -9.3308 | -50.7762 | 2024-10-04 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 9e369cfd-cc89-3e94-806b-b62c21c0be66 | -9.625 | -40.6122 | 2024-10-04 03:36:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.3 |
| d7997ab3-dc75-31d7-8da0-c375cfbe7a75 | -9.845 | -68.9623 | 2024-10-04 03:36:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2b049039-f773-3aed-afbf-25a77dfeeb68 | -10.4964 | -48.1807 | 2024-10-04 03:36:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d143a007-3c97-3ead-9cd1-f52c8cd6b2b8 | -11.0914 | -46.5294 | 2024-10-04 03:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5e825547-8a84-3774-85eb-c1f147030bb6 | -11.0918 | -46.5069 | 2024-10-04 03:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c7bfdfbe-2561-3ba8-b487-8d8ab2003c01 | -11.0921 | -46.4843 | 2024-10-04 03:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 89cb4345-722b-333f-847a-7756b3b036d0 | -11.1112 | -46.4818 | 2024-10-04 03:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6f7e0f17-987b-3a2a-a4bc-3146df6438ee | -11.8242 | -56.6009 | 2024-10-04 03:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| fa0b74dc-a9b9-317b-860d-55651c20bc28 | -11.8244 | -56.5808 | 2024-10-04 03:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8c3b3918-75a2-3193-a5af-dc08a6104939 | -12.5898 | -53.1359 | 2024-10-04 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| bd76d947-be64-3cc2-8cf0-4cbfa8551c0d | -12.5901 | -53.115 | 2024-10-04 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 1f358439-e644-308c-857a-e8ffb3f7759d | -13.0598 | -51.1195 | 2024-10-04 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bf40c729-da6a-383d-bdc8-7a5e554c57b6 | -13.079 | -51.1171 | 2024-10-04 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5a1b5ec6-f978-3e85-b9f9-88ead02d6deb | -13.1166 | -51.1551 | 2024-10-04 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 208ab9ad-e24f-3eaa-9aed-85f34f49771b | -14.982 | -49.3093 | 2024-10-04 03:36:30 | GOES-16 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c25629ca-20f1-370d-9fd9-2233bd4e8c45 | -15.4794 | -49.7376 | 2024-10-04 03:36:33 | GOES-16 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 4960f1a4-acef-3493-b5f5-92d5fe6af97b | -15.4989 | -49.7345 | 2024-10-04 03:36:33 | GOES-16 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 64fe08cb-41b3-3491-a5b0-55d4c5c8250e | -16.5935 | -57.1988 | 2024-10-04 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| 4da50414-287b-3d08-9784-0af957c0dd22 | -16.5938 | -57.1783 | 2024-10-04 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.1 |
| 796f567e-0164-35e4-a102-528e540b5111 | -16.613 | -57.1965 | 2024-10-04 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.5 |
| bf01231a-380c-39e1-90bd-3951bab20b2f | -16.6133 | -57.176 | 2024-10-04 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| a86b238f-3d83-3776-ac39-75709d967269 | -16.6868 | -57.4741 | 2024-10-04 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 8d21a584-147c-3a0e-949c-0460d95b12aa | -16.6871 | -57.4536 | 2024-10-04 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| ce884312-5814-39c5-8148-f7d4c82b8b37 | -16.7455 | -57.4674 | 2024-10-04 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 99640c28-a657-32e7-8ca3-33e892ff6978 | -16.7647 | -57.4856 | 2024-10-04 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 26a23662-ef1d-3f2b-ae92-40e05d97b358 | -16.765 | -57.4652 | 2024-10-04 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 666fac65-5940-35b1-a624-a60a0e077332 | -16.7843 | -57.4834 | 2024-10-04 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 6e9bdfc4-9945-3bc5-a5b9-ffae03c9aa16 | -16.7856 | -57.4015 | 2024-10-04 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 138fc937-0349-3145-853c-159b62569701 | -16.7859 | -57.3811 | 2024-10-04 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 57a06de3-6ef0-33d1-91bd-6e5da6c5cb41 | -16.8055 | -57.3788 | 2024-10-04 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 98eb02a3-f762-36d4-93b3-50be72eed510 | -16.9283 | -55.8405 | 2024-10-04 03:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 68fcea09-38dd-3cd8-a538-1e7cf1707b5f | -16.9287 | -55.8197 | 2024-10-04 03:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 2510f0aa-7737-3bde-ad87-8d8fb34df8ee | -17.1574 | -57.3993 | 2024-10-04 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 3fc891f2-86bc-3145-aee0-e35a488ab50f | -17.1771 | -57.3969 | 2024-10-04 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 264960ab-a2fd-332e-aa78-10be25b0b612 | -17.7307 | -43.8127 | 2024-10-04 03:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0fcdac59-54fe-3e56-b554-e76e68e0c84a | -17.7508 | -43.8079 | 2024-10-04 03:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 171.9 |
| b0733217-1304-3492-b403-73af73bdad85 | -18.8613 | -43.5837 | 2024-10-04 03:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 4cd8fa50-b3da-3112-9764-781b5e33a893 | -18.9285 | -42.0259 | 2024-10-04 03:36:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| 2f0af9fe-71d4-30b3-93ac-9f9a9ba5da54 | -19.0148 | -43.1749 | 2024-10-04 03:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| a6b4f884-cb96-3ed6-a8a4-07e8edbc459d | -19.0344 | -43.1944 | 2024-10-04 03:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| 1d9aed34-fe37-3c2a-a833-7b2f4b6ef6d5 | -19.0352 | -43.1695 | 2024-10-04 03:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.8 |
| ef50b84d-675a-3736-b2fc-66d9e0082cc0 | -19.3159 | -42.5976 | 2024-10-04 03:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 6829947c-c360-361d-9342-cc18a7cc1c75 | -19.3167 | -42.5724 | 2024-10-04 03:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| 14415dec-ff72-3488-941f-30d1ab8853be | -19.4899 | -42.8746 | 2024-10-04 03:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 3fc5c56e-d0f7-3e6f-990a-89e2aca95a05 | -19.5104 | -42.8691 | 2024-10-04 03:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 63a7fd3e-4bfd-3f67-bf0a-f7f0516ba90b | -19.8516 | -42.3738 | 2024-10-04 03:36:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 225.9 |
| 223a847d-adbe-31a9-961c-97e089ff5d9c | -19.8524 | -42.3484 | 2024-10-04 03:36:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |


[Clique aqui para ver as próximas entradas](README56.md)
