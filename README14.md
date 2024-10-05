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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be258e86-2dcb-3ab0-8231-df29804d029d | -15.768 | -49.9334 | 2024-10-05 00:56:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a488a82d-af0a-3b85-adf8-051c53002bf1 | -15.5597 | -57.4553 | 2024-10-05 00:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f7fe12dc-677d-3db5-ab11-09b2fe06baac | -15.5791 | -57.4532 | 2024-10-05 00:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 95bde94f-68e6-3570-818c-8937c613e3ef | -15.7151 | -57.4184 | 2024-10-05 00:56:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 658abb04-89a5-3e1a-a04f-45c2b132fd44 | -15.7346 | -57.4164 | 2024-10-05 00:56:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| fdc864b9-a448-34fa-96c3-64ec0f277626 | -16.4155 | -57.3619 | 2024-10-05 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| a133e815-6ad0-3f02-8e61-7c500bab8764 | -16.554 | -57.2237 | 2024-10-05 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.2 |
| e14b7ed0-76a3-3304-99ae-cf93c694d5a2 | -16.5544 | -57.2032 | 2024-10-05 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 65f9b149-4de1-3a14-b5a1-4170da212792 | -16.5742 | -57.1805 | 2024-10-05 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| a8030a89-74d7-3d50-8751-fb1327528474 | -16.5745 | -57.16 | 2024-10-05 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 5a8bfbc2-df6b-3f44-8a7e-733f471310e5 | -16.6594 | -55.5427 | 2024-10-05 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| bec0923c-4506-354e-a8b5-319eeae25847 | -16.6598 | -55.5219 | 2024-10-05 00:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 9ad7965c-63c1-32e2-ba79-12439467f6e0 | -16.6871 | -57.4536 | 2024-10-05 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 358d38ae-ac14-3c4f-b913-8b95bd43f064 | -16.7452 | -57.4878 | 2024-10-05 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 922ab0ee-694c-33e2-b5b2-fe8e852014ed | -16.7647 | -57.4856 | 2024-10-05 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.2 |
| 2157cd51-7b1c-3026-bdf5-bd2e8f22b35c | -16.7843 | -57.4834 | 2024-10-05 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 7d6986db-859d-3859-9c2f-f218254bdad2 | -16.8238 | -57.4584 | 2024-10-05 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 2919feed-ab25-3a11-8ff2-4c965f805d0f | -17.1381 | -57.381 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 96702224-d723-381f-b5c6-4a4a3eff4bbc | -17.0888 | -56.7915 | 2024-10-05 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 9d93a88f-0088-30d3-8056-e6057f60592c | -17.0892 | -56.7709 | 2024-10-05 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| a19cfc89-c36c-3d39-be8c-4fa51dfe0d12 | -17.1085 | -56.7892 | 2024-10-05 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 3c4fe377-2144-3950-a9dc-d5686ba583b7 | -17.1178 | -57.4244 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.4 |
| 4975871c-8da6-3c45-a0bc-713a31044937 | -17.1182 | -57.4039 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 216.9 |
| c601530e-4001-34d9-9514-f487e8526b0e | -17.1185 | -57.3834 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| da1bc8e9-4b63-385c-8363-e11eac296749 | -17.1375 | -57.4221 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.0 |
| 5590d91d-885a-3afa-8200-06e55f604139 | -17.1378 | -57.4016 | 2024-10-05 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 236.6 |
| 42a20102-61b9-3f1b-bc9e-51cc8aaedb8b | -18.2786 | -54.2261 | 2024-10-05 00:56:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 107.3 |
| ad63c81a-19c2-3c73-9ec2-78049c67ba91 | -18.2985 | -54.2231 | 2024-10-05 00:56:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 63de14cc-a073-38ca-9806-905d021b81c9 | -18.4867 | -52.8009 | 2024-10-05 00:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4cee6628-d0ea-3cba-8aa7-6cda0e8b7e1d | -18.4872 | -52.7792 | 2024-10-05 00:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8b33030d-7ecf-3dea-91d5-dd0e31bd1943 | -18.8809 | -43.6032 | 2024-10-05 00:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.2 |
| d4b4debf-baac-3d18-9a99-aa43e93d62d6 | -18.8816 | -43.5785 | 2024-10-05 00:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| 2b113fb5-a582-314a-96de-8575ca6e3e3a | -18.6582 | -57.2967 | 2024-10-05 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 346ce383-e5c3-30b4-abcc-fa4b655822df | -18.6586 | -57.2759 | 2024-10-05 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 3072e695-4f5e-3c31-a3ae-2fbde514029d | -18.6782 | -57.2941 | 2024-10-05 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 3ad873c5-e325-3cbb-999b-c92e3c255792 | -18.6785 | -57.2734 | 2024-10-05 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 0ee7e2db-8785-3f49-bd8d-03c183c600fe | -19.0156 | -43.15 | 2024-10-05 00:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 59447a7e-0e84-3742-ba2d-013beda28f79 | -18.6981 | -57.2915 | 2024-10-05 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 45412274-b976-39ef-b93e-d41cedfedd34 | -19.0944 | -48.2415 | 2024-10-05 00:56:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 27842911-74b7-3783-94cc-c1a47ad90b2c | -20.5904 | -51.3907 | 2024-10-05 00:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.3 |
| 9d19d61d-1b94-3214-b72f-46102ace954c | -20.7696 | -47.7514 | 2024-10-05 00:57:00 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3c491070-f16b-33ee-9ca4-d6d52208b084 | -20.7895 | -47.77 | 2024-10-05 00:57:01 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 731f1bf8-5d4d-3c46-9cd3-959423fef838 | -20.7901 | -47.7465 | 2024-10-05 00:57:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 2800af93-d50d-3c90-98de-7f61f3ec3a2e | -20.79 | -47.79 | 2024-10-05 01:03:24 | MSG-03 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2af1091c-4d1b-34a9-a6ba-2e225a4b9305 | -18.51 | -52.8 | 2024-10-05 01:03:40 | MSG-03 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b142230c-819c-3a00-bcb2-f976b42f891b | -18.48 | -52.84 | 2024-10-05 01:03:40 | MSG-03 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43dbe6f7-4acb-3e01-8ff5-710692571732 | -18.48 | -52.78 | 2024-10-05 01:03:40 | MSG-03 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba228941-4dac-3619-aa84-814e03ea6f41 | -18.51 | -52.86 | 2024-10-05 01:03:40 | MSG-03 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0855f286-749a-3c27-b9f5-ef292f3eb3a3 | -17.41 | -40.47 | 2024-10-05 01:03:43 | MSG-03 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a971acb-9109-301a-bf6c-9a25e56db062 | -16.97 | -56.82 | 2024-10-05 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 019a5f51-7b1b-329b-b433-ed18ad7cc45a | -16.96 | -56.74 | 2024-10-05 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0be33cca-7806-3d1c-b76a-3cd23ccf31ad | -17.0 | -56.76 | 2024-10-05 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21d45847-9785-365a-ad4e-e2bbfdb0245f | -17.03 | -56.71 | 2024-10-05 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc43212e-e966-38bb-a1df-bc1f23a856fd | -12.59 | -53.11 | 2024-10-05 01:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4da8289-51bc-3dd9-85b1-b7af21dd03e9 | -12.62 | -53.18 | 2024-10-05 01:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 412f7152-36c1-32c1-a9e4-9f8deb180b45 | -12.62 | -53.12 | 2024-10-05 01:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d31c2e1c-9c0e-3967-8d87-be74b1157fa7 | -2.9014 | -50.7142 | 2024-10-05 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 0f8d84ce-f155-3e9c-b1b0-cb2e8255aac5 | -2.9015 | -50.6933 | 2024-10-05 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7ad177d0-43b9-37d9-90ec-8d0c787ba538 | -3.1432 | -50.2254 | 2024-10-05 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cb69f345-1d63-3452-ab1a-09c4d0dce7ba | -3.2575 | -49.398 | 2024-10-05 01:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f2313948-fb38-3c3f-bdfe-1d0d9c642481 | -3.3083 | -50.4719 | 2024-10-05 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| dd90a366-4d2f-3dea-9e3a-92395f6e52a6 | -3.3084 | -50.451 | 2024-10-05 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 562e41a2-8650-3a00-aaa0-5d7c4df86d5a | -3.4751 | -50.3406 | 2024-10-05 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0f87d4e3-1aff-3686-a7a2-c0b5f39c5a19 | -3.618 | -47.5352 | 2024-10-05 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 3e3d39e8-1675-3b01-b275-cde3b089c63a | -3.6181 | -47.5134 | 2024-10-05 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| f3a9aa87-421c-3d69-84bc-e5a780849a2f | -4.0794 | -47.9502 | 2024-10-05 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 39a41ab9-8de8-3b0a-bfbb-ddcb6f2cbf52 | -4.6633 | -49.5322 | 2024-10-05 01:05:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 71131e97-28a9-3890-b656-9cdd9ebd2c83 | -4.9451 | -43.7888 | 2024-10-05 01:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e92284fe-4763-393b-b2c2-27083f152e69 | -4.9452 | -43.7657 | 2024-10-05 01:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a5200876-adcd-38cc-bb42-cd655a0bdd84 | -5.8214 | -44.1426 | 2024-10-05 01:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 28cce2f2-8a0d-3205-99d9-e2ec62752236 | -5.8216 | -44.1196 | 2024-10-05 01:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| abb19eee-16ae-3adf-b080-6d13178bc82f | -5.8403 | -44.1181 | 2024-10-05 01:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| caf72b24-bc3c-3115-8c02-94218c60cd91 | -6.1972 | -35.2595 | 2024-10-05 01:05:40 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 102.5 |
| 8d7cfcc7-59d9-3444-b9e6-9f1d30666ec2 | -6.2163 | -35.2573 | 2024-10-05 01:05:40 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 18e44a06-9ba4-3041-90c1-16b7464319ba | -23.6945 | -52.137501 | 2024-10-05 01:05:45 | METOP-B | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 951c225c-f396-30ee-962d-31c125951fc1 | -23.6798 | -52.117199 | 2024-10-05 01:05:46 | METOP-B | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d2a92cf-1760-3861-b050-36b654421fa4 | -7.1346 | -59.3099 | 2024-10-05 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c8aaaf58-9400-33e8-8ea9-c92a58117931 | -7.1347 | -59.2906 | 2024-10-05 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 32e88846-5ff8-3f73-bb4a-4e3d4d7f4527 | -7.153 | -59.3092 | 2024-10-05 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 532a37e5-c00a-3b50-bfd0-8b991ae025b4 | -7.7362 | -49.2297 | 2024-10-05 01:05:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 97db8222-97df-3879-88f0-674a419b4249 | -7.7364 | -49.2082 | 2024-10-05 01:05:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 2a91521a-1504-3c21-a8a1-e7a90d02bdb4 | -7.7549 | -49.2282 | 2024-10-05 01:05:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| d11b2962-f35f-3c59-863c-1c716c93bf0b | -7.7551 | -49.2067 | 2024-10-05 01:05:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 599e55db-ebaf-3ae9-9879-a62bd0a924ce | -8.6367 | -49.11 | 2024-10-05 01:05:55 | GOES-16 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1857331b-4901-3373-8e21-ee1c97d805b3 | -8.6555 | -49.1083 | 2024-10-05 01:05:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 73f2ad43-1710-3314-91b4-fc6ce9fcd730 | -8.6558 | -49.0868 | 2024-10-05 01:05:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a729e683-c7ef-3044-82cb-0887fd141979 | -8.7769 | -49.9763 | 2024-10-05 01:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 41823669-f773-323c-8852-6244535ba108 | -8.7772 | -49.955 | 2024-10-05 01:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 31997de8-fd61-31d7-96cf-f572996d2062 | -8.7957 | -49.9747 | 2024-10-05 01:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1151ee57-3f3b-3966-9ac5-9bb8eb15c2fe | -8.7959 | -49.9533 | 2024-10-05 01:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e6c6a4c1-ce82-38af-9e50-428381bf34ea | -8.9853 | -49.8083 | 2024-10-05 01:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 06c32c39-f953-3c10-86f3-124913bff58d | -21.760599 | -47.0243 | 2024-10-05 01:05:57 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 788e2f03-5cee-3e66-ae20-1c384bf9c531 | -21.764099 | -47.037498 | 2024-10-05 01:05:57 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 97c86027-4e12-3322-b038-0b770d00d19d | -21.7976 | -48.729599 | 2024-10-05 01:06:03 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 734b43e4-fd79-3925-9441-9d74b22e7639 | -21.8002 | -48.7402 | 2024-10-05 01:06:03 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| de3f9ab8-17f4-3e03-9ea9-ae0f7e423020 | -21.802799 | -48.750702 | 2024-10-05 01:06:03 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0529aec0-c52a-3c97-beba-924724511ac2 | -10.3126 | -50.5554 | 2024-10-05 01:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4b5ff07b-9518-3fde-9146-fce912ee8cc2 | -10.3129 | -50.5341 | 2024-10-05 01:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| aa452f80-dc18-309d-8c3b-0d6e7f12b5bf | -10.3315 | -50.5535 | 2024-10-05 01:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| bd003cf8-eddc-39ce-b587-520272233be1 | -10.4424 | -50.7336 | 2024-10-05 01:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |


[Clique aqui para ver as próximas entradas](README15.md)
