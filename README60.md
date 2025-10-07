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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b63d0c6-fb3f-33ed-8af3-10c818da791c | -13.09139 | -47.85723 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1022c534-140b-34e6-ad29-10f0edc37ca3 | -13.71013 | -48.07361 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9805c34-3aa3-343a-a4f7-d41295da70d6 | -11.93948 | -46.42188 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7633cdd-ea2c-3ef9-af39-3c268e17ce8e | -10.3798 | -50.29247 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23a21222-5829-3d2c-b625-99e95452936f | -12.38442 | -51.08707 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32293820-72e7-3317-aa8d-ec60df04731f | -10.61597 | -48.65701 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e2db68-a35a-36fc-b93b-239c5e23cd41 | -13.54188 | -42.99968 | 2025-10-07 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 71a16495-cb65-33bb-9cfe-9e2891abc9b9 | -15.17084 | -52.76964 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a16fbd0-ff33-32e6-b699-8510bb9e4beb | -13.35581 | -43.66715 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d05345a-1818-35c2-a4d2-0800a497cfbb | -13.04709 | -47.89691 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fcb212c-21cc-3ca3-abba-4933950f7565 | -13.66547 | -44.30564 | 2025-10-07 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60be6ba0-9501-398b-9646-07f49cb55808 | -13.70561 | -48.08046 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e239065d-bc8f-3f4c-96eb-c3893b66e4c5 | -14.28829 | -47.41688 | 2025-10-07 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6a9b28e-e646-3f06-b9f0-c704021cd20a | -15.39027 | -48.00271 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2c9c86-9c39-38f7-af99-6fc4ff0f7737 | -13.29132 | -48.05463 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84ad3d5b-a697-3cde-88f0-4d895fe2fadb | -13.09875 | -47.99152 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d3abbd8-4cd3-3d6c-8434-d2cede409740 | -16.06289 | -50.92064 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b94410af-c7fd-3971-b5d3-3bb2581b647a | -13.67649 | -47.95026 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 063d7417-4ad7-34ec-8950-9f570133bf14 | -13.58868 | -48.68693 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 111991d7-ac89-37d4-a801-b7ee3d8f964a | -12.60641 | -50.56164 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2857250c-7625-3442-a014-04df501071be | -17.34975 | -46.83186 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa2a90a9-4abb-35c5-8a64-0b456e5b9528 | -11.9429 | -46.44754 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bbc0096f-ac72-3052-a9ba-11a4cd35e71c | -16.01665 | -50.97243 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e53fe523-1fef-3883-b213-e928c7224d01 | -15.58052 | -52.56582 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4f36e65-919b-3d25-87f2-bfe015af4d42 | -15.65756 | -51.33057 | 2025-10-07 04:38:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f440b4e-72d1-3586-b7dc-d8b6bafe9a0d | -15.2221 | -49.31127 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1119dbdb-57af-3764-9841-8e12dc822ed1 | -10.74639 | -50.48469 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e87dffd-bb5a-32e7-a82a-c5976123afdc | -16.10462 | -48.94178 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d79dbfba-3f55-3921-8856-453b000d838b | -14.76768 | -46.04106 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a45cd4cd-899b-3e54-b4f8-6eb69b8ad9df | -17.984 | -44.99974 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6375f0fc-4e21-375c-9dad-dd91bad4704b | -15.37768 | -47.99266 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd490713-1a46-34f9-b5c9-024a766744bc | -11.80984 | -51.57228 | 2025-10-07 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 479c342a-d329-39b6-b08f-3fce71165bcb | -13.65734 | -48.73138 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ef91ab2-8d8f-3360-8dda-ce15902f7d30 | -18.66916 | -44.03702 | 2025-10-07 04:38:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8e71d88-e2c4-3a8e-8757-2bcd84d8dbe6 | -15.63854 | -47.61903 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a771d611-b9f1-3524-a240-8a6b7c1e4f08 | -14.52129 | -46.92662 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b6a17c-daf8-3c09-9d82-858349e69bd1 | -13.2885 | -47.57193 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99ad304-1715-3132-98e3-5349566c5feb | -13.28098 | -48.46863 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 390c09b8-c0c3-3a1e-8779-bb98c1465d58 | -14.66775 | -48.40098 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 815eab2e-4a56-39f9-9434-5dda642abf57 | -14.29177 | -47.41743 | 2025-10-07 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f31b7dfd-a06a-3dc7-a203-dc344fed4bc3 | -12.34049 | -50.26748 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8ee7163-1b1f-3300-b949-0da0143fc8a4 | -13.28514 | -47.16927 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddf5ecc1-e995-3504-9656-31a8f7f25334 | -13.27524 | -47.16383 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 905b6300-4dcb-3888-9eb1-3f46dfb0114e | -14.36409 | -47.72976 | 2025-10-07 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffdf9701-4255-31ed-b51e-06b2027eb18f | -15.16605 | -48.01117 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11851d65-d93f-3d68-9c03-76db59346464 | -13.23285 | -51.68303 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 60a63448-af65-36c5-998e-bb9b54dd7b72 | -18.51406 | -43.90593 | 2025-10-07 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f911905-8d7c-34d5-841d-3b3a0028e2de | -10.39708 | -51.59818 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57cad8e5-cb0b-36fa-a4fa-ec15779762a3 | -15.32245 | -46.30841 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d1b8a74-8e4a-35c9-a47a-bb5cef5e846d | -12.73073 | -47.9374 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a105c41-fda4-3a38-b0bd-962db158376c | -15.3877 | -48.00913 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 546dcec8-ba24-3c61-a254-b1509691ff51 | -13.37252 | -47.56586 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f260c2d7-a27f-3f56-88ef-a5d1d623fec5 | -10.74239 | -50.48781 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7cb3c5b-3a97-331f-bab2-bfb96556aaae | -12.99192 | -46.7895 | 2025-10-07 04:38:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5637e07a-a99b-379e-8984-4c18d5b5cfbe | -10.81105 | -48.59779 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 279604a4-1395-3e58-a40e-c1386ba88b40 | -10.40454 | -50.31163 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30107f8b-4a14-3e39-b52d-4b723c095b0b | -12.99728 | -51.09982 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 865f265f-c44f-31a7-8c2f-bf312f8b3043 | -16.02334 | -50.97363 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5ef5274-5568-37eb-9288-3755fe1cef15 | -14.70995 | -43.9564 | 2025-10-07 04:38:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 517fb7e9-d048-33e0-800c-ab939a9f5c8c | -15.4831 | -47.9371 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4065df24-6612-3114-b5a3-a5e61bc538ae | -11.946 | -46.42695 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17cf7c19-17f8-3afc-9027-4d86a6756f2c | -9.25616 | -59.02314 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98a410ab-8011-3035-8d5d-d59dd973ceb0 | -13.22775 | -47.80997 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 38f1d95c-c5dc-3638-a3f2-e3a44157372f | -13.57997 | -48.15208 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b0287ef-a645-3f4e-9afa-914bb9b54e98 | -15.29494 | -46.32973 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc3f2412-bd8f-3ffb-82f8-9a86af99f44d | -10.38259 | -50.29669 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0973b499-5411-34af-816c-02538883d0be | -13.23968 | -48.45832 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a67e0569-dae1-32e4-9d8b-32628e2cd272 | -14.70633 | -48.37683 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00b52ae0-4f2b-38c8-8c68-4312f631f215 | -12.72734 | -47.93687 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 103ccb55-0f7a-352e-866f-58fa43530522 | -12.41084 | -47.49693 | 2025-10-07 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d3f5f10-74f4-3095-9694-dda78b8e445a | -17.1716 | -43.45362 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ddfd639-613f-36a3-864b-2b72c8ce6542 | -11.02881 | -50.91885 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0d90a5da-dd34-3346-95e8-0ad5ed46da6a | -13.3773 | -47.53426 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 376482e4-2f9b-39cc-81a3-0e73a7185e48 | -11.13131 | -47.77284 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9136b94a-1fe0-389f-b910-35bda545264f | -14.29042 | -47.41822 | 2025-10-07 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 785b6547-f9d5-3c34-81a4-5205f6c7bbb7 | -10.45662 | -51.24343 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 692530cf-2f81-3f3b-b636-f9ee37192942 | -15.49922 | -47.92392 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dd5e633-620c-3705-a3af-b1ffffc284f2 | -13.13167 | -48.00728 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2a68e1e-c159-39de-a31d-0211dd18059a | -16.04853 | -50.96683 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eec4ad2a-7ca9-37f9-b0c9-c725f1a6d90f | -9.61836 | -57.19719 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41854b9f-8912-36f9-98c5-cb6c201b256e | -13.36907 | -47.56535 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e555d7ef-649e-38c7-a7c1-5cc723183ccc | -12.06547 | -51.20158 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5abf0dd6-9b95-3a12-951c-da5c0aed249a | -13.66714 | -44.05865 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14053034-ba26-358d-8ceb-6800256cfabf | -12.40544 | -50.27094 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0e672bc-411c-38aa-9ffa-2bea54a2dbd2 | -9.91033 | -60.19181 | 2025-10-07 04:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc184ad6-75d5-3d4e-b13b-c53e7138789a | -16.28351 | -50.98107 | 2025-10-07 04:38:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e8f03f3-2cad-360e-8a07-122d04289610 | -10.87731 | -51.03014 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8341ba1a-199c-3282-91ea-58c85e542147 | -10.74865 | -49.7165 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b4148c-3671-39e5-bea3-a5086f355324 | -12.18886 | -47.78647 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61e7d41-a220-3c07-be75-33bbb61c24cc | -10.60065 | -54.3666 | 2025-10-07 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 846db6a5-17b6-3da8-bdd6-aaad9dd7345b | -15.97165 | -50.83826 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0e1d666-41d0-33b5-8caf-bc53b1f38a2d | -15.61633 | -52.56787 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4449244-37d0-3ef1-b371-cd2e6f17375b | -15.59175 | -52.56361 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a84b6e09-09e9-3873-811a-ba9f3c31ab04 | -11.84758 | -45.0573 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 593dd530-9569-34ee-875a-5133bd35ea26 | -9.5834 | -54.94687 | 2025-10-07 04:38:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dca638bc-91f6-3bc0-9685-e8ca7461c1db | -15.98986 | -50.93842 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7ae80cc-39d4-313c-8ba8-9091f7828a1c | -10.80982 | -56.23781 | 2025-10-07 04:38:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40153e50-4c31-3dab-8422-3d21a5966888 | -10.4339 | -50.32404 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| b519fa73-897b-39a0-abb7-d6e74186730e | -14.77011 | -46.05082 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fbc46d8a-1811-3263-a37d-b55c37cffc7f | -13.0829 | -47.86725 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README61.md)
