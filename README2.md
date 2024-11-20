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
| 7789b58f-5150-35ec-b3ef-b970dad4af28 | -8.3075 | -45.101799 | 2024-11-20 00:09:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 225d828e-916f-3b04-9fca-b3308297c09c | -3.421 | -44.383202 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c272df18-86e2-357c-bf03-daf03c59f877 | -5.4077 | -44.696602 | 2024-11-20 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e19935a3-3168-31d9-89ed-ffb3dc28a1f2 | -0.9512 | -51.710701 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 10b0dee7-a37d-32eb-96e3-96d38333bcaf | -3.3713 | -44.071899 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11531f11-14f9-3e8b-9883-9046b2994b46 | -14.323 | -51.4991 | 2024-11-20 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc719eb8-916b-39db-b054-2c2d5badacf5 | -3.7181 | -44.238499 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8896e3-ed2a-312b-956d-d11ab417b3c7 | -2.8117 | -46.669899 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67efa479-43ba-3287-856e-2120a85b30a8 | -3.8599 | -46.063599 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36a94159-8da8-3dbc-9cff-d8988378fd41 | -3.3474 | -45.1091 | 2024-11-20 00:09:00 | METOP-B | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76c0e432-9a1b-3d19-83c4-723c6b690dfe | -4.1439 | -43.978901 | 2024-11-20 00:09:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9920c62b-22d1-36ea-852d-75bb71034f87 | -1.4387 | -47.112499 | 2024-11-20 00:09:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6096a23-260c-339f-bb76-f02f5273cfb4 | -4.1326 | -43.974201 | 2024-11-20 00:09:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 751b806a-c7ca-3734-a98d-e5b6d7f96bc8 | -6.294 | -41.511101 | 2024-11-20 00:09:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f910da26-717c-3909-b3ce-958c59731d70 | -2.6843 | -46.239101 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0780b218-e30e-3a53-8a57-f4a8c3eecc25 | -2.6058 | -51.791599 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d509a643-4070-3610-81a5-76cb487f11bb | -2.8992 | -53.029499 | 2024-11-20 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4bdc9d-3a9a-35fb-b0d7-1d378f4339a6 | -5.4966 | -46.437801 | 2024-11-20 00:09:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce2771bc-11ff-3988-ae9e-4fedb3adb3d2 | -4.0556 | -46.8494 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0570c094-d923-3299-bca4-6ad6d7b43bf6 | -4.3977 | -38.9771 | 2024-11-20 00:09:00 | METOP-B | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0790eb0b-a1a1-373b-be24-b6e69fd4f05f | -2.7686 | -47.628502 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0fb587a-8715-33ae-96aa-129c8084860d | -1.7222 | -46.678299 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca5e3f9-0287-35d4-9c4c-e343d4107899 | -7.9851 | -44.3876 | 2024-11-20 00:09:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd50786-4ba5-3a1a-b93e-3b12ca5bf439 | -2.2919 | -48.487301 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c234248-ba68-3cc8-b464-e73f7312da62 | -4.0539 | -46.841702 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2355179a-4d2b-3a45-be49-c76c339f7f92 | -4.1644 | -45.629501 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3199e200-23b7-3351-a3ad-0eddf1947b0a | -2.8346 | -46.680401 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc87f901-addb-3f6f-9f13-d7c1c3051ef1 | -5.1717 | -45.437302 | 2024-11-20 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e76445bb-34ac-335c-873c-b83176149b60 | -2.2014 | -46.473801 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d21e509-5c1e-3ade-9cef-b573b07ebddb | -3.717 | -47.3619 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26cde052-60af-3215-bc2e-5e8f20332e2a | -2.8313 | -46.6656 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7bbc87e-e103-3fbb-b0ae-2d399a2742b7 | -10.8711 | -44.414299 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2ac2ec4-e6cc-3bd1-8d7a-82a6421f479f | -2.9132 | -48.323799 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc41163f-c908-3dcc-8b3c-276859426861 | -2.0803 | -48.368099 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3548ac0-e74f-3be9-a37f-fe953aa7ddbf | -3.2983 | -45.395 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30ec1b2f-7768-3b46-99d5-e6a1601db3c0 | -11.9722 | -44.231998 | 2024-11-20 00:09:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40e6b46d-6412-3430-80af-2c8917c90521 | -2.978 | -45.4366 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aaf26cc-beee-3983-9643-d9623e82cfdf | -3.0422 | -45.126202 | 2024-11-20 00:09:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a692b496-bdeb-3bf0-874a-60822d414ed6 | -4.534 | -47.990002 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8de467cf-69dc-39bd-943b-3338a51d6c4b | -2.6256 | -46.206902 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7757cac-af81-3e8c-8b52-6511046a3558 | -2.4363 | -49.134899 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb5da89-27fb-36f9-81e7-3a7f715783a2 | -2.0178 | -45.794102 | 2024-11-20 00:09:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4541fef9-25c7-3e59-9d3e-a2b857b3cfe2 | -3.3682 | -44.058201 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7d9c7dd-44f6-3efd-a362-7cea4323b5df | -2.6811 | -46.224701 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc1c502-b888-396c-910c-e305292f3d54 | -1.1846 | -46.532001 | 2024-11-20 00:09:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 603e1c0a-5b3a-330b-a50e-bbe85f677d51 | -3.5772 | -43.614799 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dfe21de-5ece-315e-a759-05e47a0692fe | -4.5595 | -48.012501 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a4584e-3b98-3212-9986-ed05f78338dd | -3.5365 | -50.260502 | 2024-11-20 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025591f4-6de2-36f6-9e82-304cf48a6a88 | -2.6149 | -47.1245 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2acf256f-e890-3eed-9862-533385e201a9 | -3.3667 | -44.416801 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6ab394e-cba9-3fe3-84e1-2f732e466858 | -6.2957 | -41.5187 | 2024-11-20 00:09:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e1e19bd-45ac-3982-86f8-d16d427cb5d3 | -2.6434 | -46.240501 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d67b9df-6ec8-3337-9c9c-32034b668e7d | -2.8799 | -48.266499 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529dbd86-d5e3-3914-a15b-07a25ed37620 | -1.8548 | -47.820301 | 2024-11-20 00:09:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe7b4b28-226a-370f-9f0b-8b1a1a7c6c11 | -4.16 | -46.810398 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fbae8538-ee14-315b-a3ed-bed4f7aa4f2e | -2.6304 | -46.228401 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb6f44fd-8a1a-3057-99bb-da1c8d1df6cd | -10.9299 | -44.401199 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ade1971-4ffb-3053-8416-e82334939b8b | -0.2902 | -51.551102 | 2024-11-20 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6311a3-ad9b-354e-b785-8ccc21be4654 | -3.1842 | -54.282902 | 2024-11-20 00:09:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d287ce-2511-3ee5-a5dc-487777bdb884 | -1.1873 | -51.759201 | 2024-11-20 00:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79c5a61-e3df-3dfb-8f58-604408cb1b01 | -3.9997 | -43.250301 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5479253-2de2-3ed4-8c9a-6d91a00e152d | -2.6698 | -46.174599 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59fb658f-a8e0-3405-b020-b9d129342636 | -0.892 | -51.766499 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cdbb4b1e-7894-36b6-98e8-15a3f1b1be7f | -4.5673 | -48.0014 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f95c8a2-187a-3d4f-95cd-0482a1ee5f8c | -3.1326 | -49.126999 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c29f9fe-30fc-3d18-a9b4-695acaf79a85 | -2.1349 | -47.416801 | 2024-11-20 00:09:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e262ec39-8a13-39e9-a11a-30320ba240fd | -3.7188 | -47.369999 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1b89c9d-03c7-3a52-a3ce-085f10a5e653 | -2.6615 | -46.229099 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccad9589-f739-3ed1-ac89-d134a31e2ae7 | -2.6406 | -46.1362 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb7e1fd1-a29b-31d0-ad18-eab5e47446ed | -7.801 | -42.738998 | 2024-11-20 00:09:00 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59010bb1-42e0-3062-a82a-075c67d3a45f | -5.4853 | -41.8069 | 2024-11-20 00:09:00 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e6e24637-4f77-35d2-8227-4afa314fd7aa | -2.1715 | -46.9828 | 2024-11-20 00:09:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d89f9c-9a90-38e4-976f-c27a4fe1aafd | -4.8234 | -43.474201 | 2024-11-20 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd066231-c59e-3e98-9318-78679c884479 | -2.6233 | -46.564301 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573ebf4f-3d12-387a-bd95-e35a98907404 | -5.9674 | -45.3592 | 2024-11-20 00:09:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e79361b9-b70e-345f-9ab5-3d170fd31321 | -2.6225 | -46.836498 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e7ce59-d7ff-316f-95dc-c6f14f2e2473 | -1.0774 | -51.7258 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c34a7125-264e-3be0-a536-84a43fc85f03 | -9.1586 | -44.716499 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89f9a85e-e746-387b-be62-f95337b808c5 | -3.8665 | -46.047001 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31d4d4dc-7005-3b79-96fd-0a81a3b296e3 | -4.6075 | -46.417099 | 2024-11-20 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0768099-d81f-3687-8c90-481efb101236 | -3.1184 | -49.109402 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2b2dc4-8af9-33d1-beb6-36f7843834f2 | -5.3741 | -40.651501 | 2024-11-20 00:09:00 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e16963b7-9abf-3881-932c-4660831ea75e | -10.4022 | -44.479698 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f62caa10-6d7b-3f89-bac3-791edf179796 | -2.6397 | -46.5453 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3476ab1c-211a-3f8a-8822-749a40d1df4f | -5.407 | -47.383701 | 2024-11-20 00:09:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d94cc36-f9c8-3847-8120-4fc969800a44 | -2.6568 | -46.162601 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d046d80-8ccc-38d0-a7e3-b0a625e178aa | -5.4304 | -45.5825 | 2024-11-20 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 632106cc-c50a-37bf-adb0-7df03768b4ec | -11.4237 | -44.688301 | 2024-11-20 00:09:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 625d99a5-b082-3d72-828c-ef7a9d7aab8e | -2.2647 | -53.614201 | 2024-11-20 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11cca956-ee3e-33b4-b5a8-6cd6385ce334 | -3.3682 | -44.423599 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 371e2f07-1020-357f-b678-667d9e8ffe72 | -5.5917 | -46.1702 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37791ea8-2521-36bb-af9c-eff23753a554 | -3.7924 | -43.2453 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8655acdf-5421-3536-9a80-8769e2628866 | -10.8059 | -44.398102 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeb6b49d-a28e-3fcc-aa27-f5be67b42b77 | -12.0018 | -43.004002 | 2024-11-20 00:09:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 92524a95-bc43-31f0-810b-8aee6426416a | -2.9884 | -46.9543 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd067f25-8d60-3b07-a2c3-3aabf2a8d364 | -5.9099 | -39.145802 | 2024-11-20 00:09:00 | METOP-B | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca08b235-0e7e-3425-92bb-dcfc47861918 | -5.5818 | -46.172298 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2dcef9-ddbd-3a45-98b7-1d51d6941e16 | -2.6026 | -51.7771 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab4dafd-1bab-3e18-a06e-c20a49726d0d | -1.8669 | -50.952702 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8bbdb4-6be9-347a-a24f-00798e18eb3d | -3.2916 | -45.4109 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
