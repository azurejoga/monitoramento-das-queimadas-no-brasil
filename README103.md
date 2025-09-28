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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 790b679b-4e8a-3330-86b4-a9f065eb96ef | -9.4007 | -54.6984 | 2025-09-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| cb3a3ef4-c09c-3f26-8ba5-780a9b6ae245 | -8.8226 | -46.2115 | 2025-09-28 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 432ae513-79fe-36e5-a57f-47253c2e6b5f | -9.9581 | -43.5987 | 2025-09-28 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 60ddf665-4995-3f1d-9e81-f27f6e363f9b | -11.9982 | -47.0821 | 2025-09-28 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6d7d55ce-f8eb-370d-b851-3d16641704f8 | -8.1614 | -46.3899 | 2025-09-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 882980de-e89f-3795-ba5b-9ddb5b610020 | -6.6002 | -44.9736 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| e8a60eda-9748-3fc4-af30-3453c74b7970 | -14.7851 | -45.6818 | 2025-09-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 54404d30-9800-3ea9-98ff-7d099cec55b2 | -14.885 | -45.5708 | 2025-09-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e9f85f59-860c-3e5d-bae9-5460b5420648 | -8.6798 | -47.0738 | 2025-09-28 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d46a3cdf-3e0c-3d16-91c5-1582297f2dd5 | -8.2854 | -45.4772 | 2025-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 8d9eca1d-f299-3a4f-81fb-a72eb1e77f6c | -7.2605 | -42.9939 | 2025-09-28 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| ab5a4826-270c-3adc-8c29-0a5098db40e5 | -8.8759 | -45.0274 | 2025-09-28 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 4eb45984-d340-37eb-9c03-eb1344e5be5f | -11.9824 | -48.0197 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 1fde4ac4-f447-3bd1-ae01-c8654b21e9d7 | -6.5065 | -44.9813 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cb6841e4-ae2c-3f56-8e00-735249804cd9 | -5.7583 | -42.8447 | 2025-09-28 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 00eec044-744e-3bd6-ad94-7a38ad9195e9 | -4.6757 | -37.6624 | 2025-09-28 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1035.4 |
| d7f58828-37ba-3c7e-9f4a-2fb938f5261c | -11.4409 | -45.0229 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0a5de16e-3138-3770-9489-82222c2217ae | -12.1072 | -44.2021 | 2025-09-28 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b83d8ec5-d889-33f0-8d0b-cbb443ef3f94 | -10.8242 | -45.3841 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 3284300d-3aab-385f-b63e-dcede77dd454 | -11.904 | -44.8161 | 2025-09-28 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| fab1575b-4bb3-3d2d-9679-ba008b61e07b | -19.7518 | -50.1034 | 2025-09-28 14:00:00 | GOES-19 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| 3fa0fa8e-f038-3363-ad0d-86360b082d06 | -6.6978 | -44.6003 | 2025-09-28 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1d3809e4-41af-3795-bc7b-e0c10561d2e2 | -12.2636 | -44.0599 | 2025-09-28 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 205.1 |
| fe01b9ee-c22e-39c4-8c9c-3fdd8fbcf715 | -12.9717 | -46.2846 | 2025-09-28 14:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cc0c6023-a554-3b63-8781-060cebed4e6a | -12.1076 | -44.1785 | 2025-09-28 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| adf22089-200a-3204-b587-56354b1e0594 | -11.7002 | -44.4283 | 2025-09-28 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f7e08510-0928-3bd4-9bc5-c6a984744c1b | -9.106 | -47.6275 | 2025-09-28 14:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| bc0e2a80-41b1-3dea-80ba-d6c0bee6c2bd | -11.979 | -47.0847 | 2025-09-28 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 9786bb4b-6371-3f53-8de2-ab0186e8fd3e | -9.4194 | -54.697 | 2025-09-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 492d2d9e-d727-3ba7-acbf-9a51558752c7 | -9.4196 | -54.6767 | 2025-09-28 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0c02e051-274e-356b-b562-fc4e70c521aa | -6.3 | -45.0205 | 2025-09-28 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 39be4dfc-c29b-32b4-83b8-c1ff720833ef | -5.3059 | -43.1365 | 2025-09-28 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4765c7df-8fc3-39d7-b464-1ca137cc4e0f | -13.77 | -47.8987 | 2025-09-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 497c59e2-18e0-39f2-8f25-5500754ef99c | -7.7604 | -46.961 | 2025-09-28 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| cd5d66ab-7793-35f3-8e92-4b8446b22885 | -5.9004 | -43.6976 | 2025-09-28 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 9b84715f-7951-3054-b0cd-94801e35896d | -12.0218 | -47.9481 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a5b226aa-a3df-337b-b232-4b9e22f7f833 | -11.3842 | -44.9849 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 5b3c9762-95ea-308a-87c0-019a042d4123 | -6.3107 | -45.8775 | 2025-09-28 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2b22c4b1-f212-30eb-bcc0-41ec623accab | -6.2759 | -43.6442 | 2025-09-28 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ad89a07a-90f9-3abd-8b20-a7af00b71916 | 1.8687 | -50.8629 | 2025-09-28 14:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 91666069-95c0-3e72-9bd9-ffd49fb8a10f | -7.3659 | -47.0394 | 2025-09-28 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 45d4b363-79c6-3908-8633-a6c22bc05495 | -12.9156 | -45.1912 | 2025-09-28 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 93e8cd15-dce8-3187-8587-1456d8dfbd60 | -11.946 | -47.9138 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9ac6b02c-50c6-3d4a-bea9-ef60ade60896 | -14.3813 | -54.9472 | 2025-09-28 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 2921b86b-ecc6-3508-862c-f4029fb6ec82 | -7.3849 | -47.0157 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 6e420f6b-3bc0-3727-a8d3-4322c97f50cb | -11.3654 | -44.9645 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 5e2c8b27-9376-3499-9d1e-e5f1eeb17b61 | -12.0214 | -47.9703 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| abb60231-ee9f-3ee0-b460-0283a3991dea | -9.1102 | -45.8653 | 2025-09-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 01f0cbb6-37f3-3a1b-9762-3860ad198ccf | -11.4217 | -45.0257 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 4d935feb-5f00-39cf-8b55-fba956b7d55f | -8.1611 | -46.4122 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2ccbbab0-abeb-3230-8c74-1e39df566103 | -12.9363 | -45.1184 | 2025-09-28 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 13675794-72e7-3a0f-b157-2eb36c7e4ec6 | -6.6181 | -45.0631 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ba44aff8-56c9-3cf5-b46b-fc790b765fb2 | -7.8823 | -44.5594 | 2025-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 39b09311-e38c-3239-9a46-d2a420198cb3 | -8.2856 | -45.4545 | 2025-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 278d6e6a-f8dd-3a5c-9797-fba8a5a2feb4 | -4.6946 | -37.661 | 2025-09-28 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 493.4 |
| abcc74e4-b75e-30e3-92ce-a94c652a88d1 | -18.1977 | -53.3208 | 2025-09-28 14:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 6053f2a3-a491-3448-b7d6-ecea1ab7881d | -9.7643 | -47.7786 | 2025-09-28 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e6965c84-ea00-385f-aef2-c60e01d0533c | -8.2665 | -45.4791 | 2025-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5ef6d231-8c4d-3d23-a427-1223cd91ddab | -11.7194 | -44.4254 | 2025-09-28 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| a2e15191-b955-36c8-a4eb-7d9a96932a9e | -4.676 | -37.6366 | 2025-09-28 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 174.3 |
| 5e2a006b-7829-3821-ad1e-a23b05c90b66 | -6.5616 | -45.0905 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 26f19f77-5506-3299-a3bf-f7cc9eca4065 | -14.3816 | -54.9266 | 2025-09-28 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| db5bb022-e0bd-32ef-984b-7f08cfe89796 | -8.2419 | -47.5352 | 2025-09-28 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 24a26399-4048-38b3-84be-a636d8d1eba9 | -6.619 | -44.9721 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 180f0bdb-a76c-3a36-9919-624ad418db5b | -10.8238 | -45.407 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| d5d6bfdd-61fd-3706-81f2-bc05a27943c7 | -18.1778 | -53.3239 | 2025-09-28 14:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 1c5f618a-65d6-3526-9bea-629414de1a89 | -6.3105 | -45.8999 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 22c2121f-3b8b-39bb-84d6-ede0b1c759cf | -13.2966 | -50.7036 | 2025-09-28 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c676bc86-a8cf-358f-b4fb-b660e4123a45 | -6.6005 | -44.9509 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 65ec0d88-9678-348b-b66c-e65d2e61ac19 | -10.9137 | -45.7375 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 7c3648d5-09ed-3145-bbba-8e258972fdd9 | -14.765 | -45.7086 | 2025-09-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| a7319db2-22cf-37c5-95de-b6cbe9c49ef8 | -11.4083 | -46.9597 | 2025-09-28 14:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 71322873-81c4-3b0e-a97b-a4babcffae08 | -11.3889 | -46.9847 | 2025-09-28 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| ae9decfc-10d2-3cdc-ad8f-8d67959224d5 | -9.0913 | -45.8673 | 2025-09-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| aaf5c4ad-b3af-371d-9f5c-7750ef1a9efa | -11.3658 | -44.9413 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c39062aa-6bf8-337d-9597-2f372417fca2 | -10.9923 | -45.5901 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4bd1c2ca-d1d0-38cc-b1ff-987d2b1f8045 | -12.0222 | -47.9259 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 97141c3c-3f58-3a2f-93fa-240371562d0f | -11.3892 | -46.9622 | 2025-09-28 14:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 4f5d96cd-30f4-376b-b688-2f8fd017ebe6 | -12.0019 | -47.995 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 83ad199b-060c-39fc-ab31-d18aa49dc461 | -9.1099 | -45.8879 | 2025-09-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6934a936-bd03-310a-88f0-45836b9e5599 | -4.6948 | -37.6351 | 2025-09-28 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 1e202696-61b2-3e96-8f95-e44489deae6f | -9.4455 | -47.6144 | 2025-09-28 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b9e1f6a6-5b7b-311b-93ed-d22759ad57d4 | -9.0874 | -47.6074 | 2025-09-28 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 69027565-5449-30d3-ac63-87a564dd033a | -8.2668 | -45.4564 | 2025-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c919ba5d-1d8e-3e48-96d9-1a9d3c58b9fb | -13.7893 | -47.8957 | 2025-09-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 28c8fbca-db82-395b-8cc4-a038f2f841e3 | -11.4413 | -44.9998 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| daec3176-398f-3b63-8f04-567fbcf5f966 | -13.7704 | -47.8763 | 2025-09-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c68427e9-4c2e-3469-90c7-3c05b8534fdd | -12.2825 | -44.0804 | 2025-09-28 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 4dc832db-920c-3fe4-80ab-c20680f7e44e | -5.2869 | -43.1613 | 2025-09-28 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 24005182-6c73-35e7-bc35-f866e29d8b3c | -7.8634 | -44.5612 | 2025-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ea8d3036-cf2a-3e01-a0f5-cbef5fe9ea35 | -9.9578 | -43.6222 | 2025-09-28 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e89b4f6c-c308-3fd8-ac95-6570986d037b | -6.3154 | -43.4548 | 2025-09-28 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d2daecc4-ed92-3d75-9798-f81f456df6bc | -4.6944 | -37.6868 | 2025-09-28 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 369.5 |
| 751bfd63-7bf5-31c7-a831-7fcb3d39e42e | -13.5884 | -47.2987 | 2025-09-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a1953599-a755-394b-8a65-cf367f7a27ff | -9.0874 | -47.6074 | 2025-09-28 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 73c0e494-7f53-3c18-9e21-cfcbbbc7bb26 | -11.3846 | -44.9618 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 551d1325-0ec0-3c7c-b65b-303edc8d7289 | -11.3658 | -44.9413 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0bb64c97-0b74-3460-a899-787fc696df5a | -6.3105 | -45.8999 | 2025-09-28 14:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0988c96a-e125-39e3-b2f7-3660975a01ee | -13.2966 | -50.7036 | 2025-09-28 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3c09262a-d237-324d-bd55-9add3b69cd0e | -9.9578 | -43.6222 | 2025-09-28 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |


[Clique aqui para ver as próximas entradas](README104.md)
