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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 065744a5-ff9a-39c9-af98-b1027b9a4e10 | -12.6283 | -53.1108 | 2024-10-06 01:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 9ad3b3f5-fbfa-39e1-aab3-4ed0361c3c11 | -12.6474 | -53.1088 | 2024-10-06 01:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0da8f974-7a5c-36f4-bdd2-577a3dbdbebc | -12.6532 | -54.0415 | 2024-10-06 01:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| fc068946-a6a5-342c-a2c5-c9592df2b06c | -12.763 | -50.5352 | 2024-10-06 01:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 9f70613b-0645-3503-bbd7-73c6d12db76a | -13.3976 | -61.957 | 2024-10-06 01:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e823322c-52ee-373a-9c4f-2fe38906b25b | -13.6531 | -51.1936 | 2024-10-06 01:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a2bb95cd-4ee1-35b7-9d8c-85f05e8cf2b3 | -13.672 | -51.2125 | 2024-10-06 01:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 10577150-0f07-3f87-b611-b0ae095edb4a | -13.6724 | -51.1911 | 2024-10-06 01:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 42827f8a-6ceb-3a9b-af7e-40f08e507add | -13.6917 | -51.1886 | 2024-10-06 01:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 45fac8ff-4516-3f78-9530-da6405e10199 | -16.3956 | -57.3845 | 2024-10-06 01:46:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.1 |
| d815f6d1-dfe1-3b4b-9d04-3c06b7bfaca1 | -16.3959 | -57.3641 | 2024-10-06 01:46:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| 3d4e8ecd-2c78-37a2-88c9-f0a2edd7018a | -16.4151 | -57.3823 | 2024-10-06 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 2a139fb6-8bd3-3e24-942c-4c36bb57dcff | -16.4359 | -57.2984 | 2024-10-06 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 92763511-6ab3-3d10-b20b-c17ef57f6647 | -16.4362 | -57.278 | 2024-10-06 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 68032c4e-c0f9-39ef-85ff-8e19c1e955cf | -16.4554 | -57.2962 | 2024-10-06 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 13811a44-856c-3afb-bd6a-df6a65d06223 | -16.4557 | -57.2758 | 2024-10-06 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 8d6efbbe-737d-3404-a0a4-4eded8ef8034 | -16.614 | -55.9214 | 2024-10-06 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 9c4b038a-e838-3643-85ff-d36c07e4ec8f | -16.6398 | -55.5452 | 2024-10-06 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| d412d6c8-dc64-341f-93ba-84b0fe01ce7f | -16.6923 | -55.9117 | 2024-10-06 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| ae49446b-240c-3529-9600-325f7e27cdda | -16.7067 | -57.4514 | 2024-10-06 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 0c3e451d-6387-312d-aaa9-fc8295cffe43 | -16.7647 | -57.4856 | 2024-10-06 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 44d83f8d-1442-36de-b991-4fa7b153bc5b | -16.8238 | -57.4584 | 2024-10-06 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 9d4fad18-1a7a-3291-afba-20c4a6a05e6a | -16.9545 | -56.6226 | 2024-10-06 01:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| fda0e7ec-bc42-3dc4-b28b-8a3f7fdfceb1 | -17.1182 | -57.4039 | 2024-10-06 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 7df9e8a7-f125-3002-8479-a3091581fd71 | -17.1375 | -57.4221 | 2024-10-06 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 86e4e5cd-be3c-3dce-a18d-0c7a4eaf632f | -17.1571 | -57.4198 | 2024-10-06 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 92f62e4c-63b5-3ffc-99c4-6e45b2994a0e | -18.6586 | -57.2759 | 2024-10-06 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 04fc0df8-cade-3538-b67a-0cb964a84a48 | -18.659 | -57.2552 | 2024-10-06 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| aefb8d69-75c3-3850-91de-b015c27e6d8c | -20.5813 | -49.3865 | 2024-10-06 01:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 152.4 |
| bc0b97e2-d9c2-3b50-bccd-2f2d38d0a735 | -20.582 | -49.3635 | 2024-10-06 01:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 2f865b99-8d64-3ec3-9d45-8dbb5b89f4f5 | -20.6018 | -49.3821 | 2024-10-06 01:47:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 102b7faf-28e5-3849-b1dd-50e895888425 | -20.6024 | -49.3591 | 2024-10-06 01:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d6d319ce-065b-3e30-82f0-9abae52f74ec | -21.5218 | -50.9088 | 2024-10-06 01:47:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| 68a20ac2-7334-30c8-affb-74de9fc56c23 | -1.7668 | -47.1984 | 2024-10-06 01:55:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 81ea5d12-337d-3be7-b6e2-38a9ec4c032a | -2.6858 | -49.0752 | 2024-10-06 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7b652c3f-64e8-3228-9b16-ae3c564d2a3f | -2.7043 | -49.0747 | 2024-10-06 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b909f11b-bc06-3dfd-8707-ff2130897ada | -2.7981 | -48.6873 | 2024-10-06 01:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8b595da7-5e5e-3da1-9906-a88058c24542 | -2.8165 | -48.7082 | 2024-10-06 01:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 112226a7-3ca4-347e-acf5-feebe24a38ae | -2.8166 | -48.6867 | 2024-10-06 01:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 219.6 |
| b6c1e4a4-f332-32af-8501-c46e715860ef | -2.8167 | -48.6653 | 2024-10-06 01:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fce06ddd-8334-39cc-8c0a-6e17891f8e50 | -2.847 | -50.4648 | 2024-10-06 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| bd2f1daa-f127-3ccc-8e2f-5fd861cc8672 | -3.1129 | -48.6131 | 2024-10-06 01:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 0650c29f-cd48-3419-ac3e-e1ce15a9a51d | -3.1314 | -48.6125 | 2024-10-06 01:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0186afc0-3bfa-38bc-ba10-9776a6e36693 | -3.2223 | -48.9733 | 2024-10-06 01:55:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e7cff7dd-9e56-348a-9386-96a922f674f2 | -3.7066 | -41.6997 | 2024-10-06 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| d32122c4-bb27-3ec5-bcca-fb778a1a48b6 | -3.7068 | -41.6758 | 2024-10-06 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| f5ffad40-c90c-3491-b164-c443ec041b2a | -3.7255 | -41.6748 | 2024-10-06 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 5760265b-2b92-3779-b53e-69456e87294f | -3.8008 | -41.5989 | 2024-10-06 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 302d16e5-89fd-351a-9f3d-d30781df161f | -3.801 | -41.575 | 2024-10-06 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| b595c728-6563-380c-9d63-d8612a654f9b | -3.7934 | -49.4849 | 2024-10-06 01:55:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 034c9517-f795-3480-b708-e71347e32fa5 | -3.7935 | -49.4636 | 2024-10-06 01:55:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1d2c9c23-9d78-35d6-b8a2-7f81b34d7334 | -5.5718 | -44.87 | 2024-10-06 01:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6f873a70-444d-3d86-9e5b-ba52a63cdf82 | -5.5905 | -44.8687 | 2024-10-06 01:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4297ac7c-e0e4-3bd4-98a5-ed79059f9497 | -5.8214 | -44.1426 | 2024-10-06 01:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 20ac5534-02a5-3656-9356-f9273209395a | -6.9514 | -59.0666 | 2024-10-06 01:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 414f23a7-65bf-3a4d-8e3e-211ccfb8cfdc | -6.9699 | -59.0658 | 2024-10-06 01:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fb2c4099-6709-3f3f-bdb4-f73d7c9fcdbd | -7.1532 | -59.2898 | 2024-10-06 01:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 36f7dd3b-4bef-359f-9c98-dbd20a05778b | -7.964 | -54.7562 | 2024-10-06 01:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| efa38dab-009d-3404-8f9c-70682aab0f20 | -7.9825 | -54.7752 | 2024-10-06 01:55:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ee739c63-6660-3d95-a210-3c747c1e8cdb | -7.9826 | -54.7551 | 2024-10-06 01:55:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 59d47045-c9c7-3058-8ac3-356332d8d43d | -8.2139 | -61.2022 | 2024-10-06 01:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e2004d34-e329-3b08-8709-fcca70503082 | -9.1449 | -60.6612 | 2024-10-06 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5589d591-9d59-3d7b-af06-cbbcbccab742 | -9.3278 | -46.5385 | 2024-10-06 01:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ff29cfa9-7d38-37ef-ac15-9913ed4979cd | -9.3464 | -46.5589 | 2024-10-06 01:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 951f03d8-3c63-31d6-9dfa-d785a34d32f9 | -9.3467 | -46.5365 | 2024-10-06 01:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 236.2 |
| ad63393b-24f5-326d-ad57-1b4c4440bc31 | -9.347 | -46.514 | 2024-10-06 01:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8c940059-292e-3945-8846-0f7dea4c41e1 | -9.3647 | -51.0898 | 2024-10-06 01:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5230000b-9227-33f3-ac33-3d1a8d8b0399 | -9.365 | -51.0687 | 2024-10-06 01:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ccbcb258-e1b3-3809-829e-b0a1ef0b696f | -9.3835 | -51.0881 | 2024-10-06 01:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 65a416dc-38a8-390b-81e3-916fda061c43 | -9.3838 | -51.067 | 2024-10-06 01:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4a182152-a162-3244-9dc1-92bd99c004a0 | -9.8551 | -60.3159 | 2024-10-06 01:56:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| cb703459-abcc-3f9e-9341-1a019e68d578 | -9.8552 | -60.2966 | 2024-10-06 01:56:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f8ae91d7-2a48-34c5-bdac-36b6584797df | -12.0211 | -63.7478 | 2024-10-06 01:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 58127205-600b-304e-8af9-e60492da0662 | -12.6089 | -53.1338 | 2024-10-06 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 926ce693-32e4-3b4d-98ff-875b8197c28f | -12.6092 | -53.1129 | 2024-10-06 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3b275355-6f56-35bb-bebe-0b89513ff4bd | -12.628 | -53.1317 | 2024-10-06 01:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 669e2043-20db-3059-a083-c88a594cc798 | -12.6283 | -53.1108 | 2024-10-06 01:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| d0ffd760-0d7f-3a0e-967f-a66bc1dc88aa | -12.6474 | -53.1088 | 2024-10-06 01:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9077ee89-55ae-358e-849d-a441c222deda | -12.763 | -50.5352 | 2024-10-06 01:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 097804f4-482d-3a3b-b06b-9f9b0bd39187 | -12.7634 | -50.5136 | 2024-10-06 01:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3180981b-778d-312c-900a-f2d3924afb30 | -13.3976 | -61.957 | 2024-10-06 01:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d80f36d8-17dd-306f-966d-bc778051258d | -13.6724 | -51.1911 | 2024-10-06 01:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 196.9 |
| cc5b0683-0a84-30fc-8206-24f8aac40339 | -16.4362 | -57.278 | 2024-10-06 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 3372bf31-1e53-3016-a63b-2d095bb965d2 | -16.4554 | -57.2962 | 2024-10-06 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 60497a04-0064-3be7-ae23-ae48d733515a | -16.4557 | -57.2758 | 2024-10-06 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| bc1b627f-e5dd-3ccc-9036-26ebef284bed | -16.614 | -55.9214 | 2024-10-06 01:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 1347244d-d663-3b1a-a1c6-f49c2dc1cff9 | -16.6398 | -55.5452 | 2024-10-06 01:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 4e5a2c9d-c6fb-3a29-b41f-dc16cd5856b4 | -16.6923 | -55.9117 | 2024-10-06 01:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| 96051885-1d7c-37af-9d7c-1c7cc7a673e8 | -16.6927 | -55.8909 | 2024-10-06 01:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| d63651b7-960f-35df-8cf7-ea573c48f910 | -16.8238 | -57.4584 | 2024-10-06 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 06e0b7ce-e062-36cd-8a34-18d677dedacb | -16.8241 | -57.438 | 2024-10-06 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 530335cd-7b2e-3cc3-9ada-3ac41d44386c | -17.0203 | -55.0581 | 2024-10-06 01:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ba287ceb-9ba2-32bc-8ab8-dd4bd1273a63 | -17.1182 | -57.4039 | 2024-10-06 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| c9a91d21-be11-3889-9ac5-7fd0b5befd94 | -17.1284 | -56.7661 | 2024-10-06 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| a66cdd30-d08f-37e7-a05a-ccca712fe7a6 | -17.1375 | -57.4221 | 2024-10-06 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 1febe045-de5b-39a9-afb2-b5e2012a0d16 | -17.1571 | -57.4198 | 2024-10-06 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 69692212-1f3b-39d0-a6f3-014db986bd3e | -18.6586 | -57.2759 | 2024-10-06 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| ce8cc83e-9721-3647-9e8c-be172379d3e8 | -18.659 | -57.2552 | 2024-10-06 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 3e56fdfb-6f64-315f-8b68-6285662a572d | -20.6018 | -49.3821 | 2024-10-06 01:57:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 104.4 |
| fc6a459c-748f-3f65-83ec-69ff2d792e1e | -20.5813 | -49.3865 | 2024-10-06 01:57:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 106.3 |


[Clique aqui para ver as próximas entradas](README34.md)
