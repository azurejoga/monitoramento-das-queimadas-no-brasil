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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03fdeb27-4335-35e5-90b2-e49d05473cdb | -5.66596 | -44.50439 | 2024-11-21 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b13a6c40-84ae-38a4-8be4-43f56ae2dbb0 | -4.57824 | -48.01352 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af7ef6c5-2100-3f08-8f5d-5bda5cabb375 | -3.28788 | -53.85137 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3836968e-7616-38ec-bab2-7e269d84efac | -5.92917 | -44.72547 | 2024-11-21 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94791b04-f9b9-3c30-a3d2-e738a1359677 | -3.28439 | -53.82068 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a7ddae6-d382-3e11-a86c-e291c48774d9 | -3.29366 | -53.8507 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d1660b9-8d91-3c7f-95ae-b89bcf8bb6c3 | -4.35271 | -45.89001 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04e7097e-ff10-308c-872c-16715452f9ac | -3.74893 | -52.67156 | 2024-11-21 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf7f4574-12d2-392b-ab2e-7a7c45b5080a | -3.56987 | -54.68374 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7aaa9e15-bc7c-34e0-af6b-bb4e2e5cd3e9 | -3.28824 | -53.82591 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec8364f1-7059-3ab0-a454-68d28a796dbe | -5.55166 | -46.39097 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bf95931-591b-3ce6-9165-7f9d2153d23e | -4.22298 | -47.18036 | 2024-11-21 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740959ad-db3d-31b7-84f5-da7214510bae | -6.0658 | -44.1501 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2ed7cdd-2cc5-3db5-9379-0c087797c737 | -4.09111 | -51.07185 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f69a32-ce47-3d1b-bfd5-ad34d2c84657 | -4.39506 | -45.59269 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9f1341e-2331-34f3-9f15-611efe89bde6 | -6.2033 | -46.21987 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2276a5dc-fbb9-3ced-b409-29d7151b27fc | -5.24211 | -42.63579 | 2024-11-21 04:31:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d814c495-0b5b-31f1-a7ef-d71052d1a8b3 | -6.8673 | -48.66714 | 2024-11-21 04:31:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3152f96-f762-3047-a318-e6a252888135 | -4.58325 | -48.02506 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a96f2781-9d34-311e-9f37-b4a2f5c43f05 | -3.27607 | -53.84317 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7521522f-3757-3266-be09-60aeae01ea41 | -3.26914 | -53.82793 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22483f03-2022-3568-a54e-c23f50ff1075 | -3.71324 | -51.84245 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8354c30-f401-3505-a621-09054a024753 | -3.27299 | -53.83318 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 340c0530-47c4-3c08-9a87-54842c0853c0 | -4.09061 | -54.04515 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9b1995c-d651-3ba3-aad8-f9fac5109b5c | -6.19954 | -44.37231 | 2024-11-21 04:31:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fc0fea9-3342-3ef0-8cec-38effd4bc877 | -4.34495 | -46.14028 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c49b18f8-010b-3783-971f-fae5bf015738 | -3.28263 | -53.82681 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a0a192b-1798-341c-9e26-9b3b6d1ed05c | -3.52092 | -53.80249 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed690a04-7acf-3215-a6f1-ad1983be1733 | -5.24655 | -45.88473 | 2024-11-21 04:31:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c342347b-b79d-317f-ae72-350b28728743 | -3.33951 | -53.30915 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8d1809a-7d34-341b-89cc-7b122b5467f2 | -10.71642 | -49.48481 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed3b7285-2c85-38b5-9365-03f0525735b6 | -6.21289 | -46.22506 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fae51ab1-0ead-31ed-8a77-cf33e4bf3149 | -5.43577 | -42.83573 | 2024-11-21 04:31:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 12063d1d-f5c1-3bfe-8985-f9fa33118427 | -3.2795 | -53.84529 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fd5847c-7dea-3934-bc13-0c6b2c4b3c23 | -7.39223 | -42.77533 | 2024-11-21 04:31:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7b49b8ba-910f-38a1-a54b-0eaa4f64ea8d | -5.42796 | -45.34032 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a437392-609a-36c3-8f3b-06dc634a44a7 | -5.4451 | -46.35638 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb1d115-1f35-39cf-bc2e-d089c5a729ce | -3.51643 | -53.80142 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f1624a-7bd0-3f55-b6b5-648a876c076f | -4.56991 | -48.02295 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88c91d12-77bb-3c0c-b2e1-8b86e719fe86 | -3.82556 | -52.25434 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ac473d-c800-3591-8e5e-458e32858202 | -4.3914 | -49.93756 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef36415-61e0-3d87-ab0e-61a8b22e5624 | -9.40681 | -43.3178 | 2024-11-21 04:31:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07a1c13a-6dc5-3601-aa6e-81eb2abdd9a1 | -4.62881 | -45.56768 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72d3f572-62a5-3b3d-b2f5-635c5fea400a | -3.1884 | -54.76781 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59470106-926e-370b-ae4b-dd3a40b7a784 | -4.79568 | -45.79861 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e76da7a-fa2d-302a-8978-8e2823a80589 | -5.59938 | -46.5357 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee87ed6e-7376-3740-9b54-aa4e13838d66 | -4.17654 | -53.5763 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 627c0224-5ecb-32ba-b776-4c287d7c090e | -3.46878 | -51.64404 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9593add1-4ad1-36e9-b471-3ea2976cdbe8 | -4.00421 | -49.92433 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25a903a4-9b66-3c30-b01b-480f1130206a | -4.01037 | -49.0099 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d326f0f-e634-3bdd-9d1f-423f0e49b8df | -4.10993 | -51.05135 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b408bb25-4961-3dc5-a077-4031395e7548 | -4.09037 | -51.07636 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a94ccb34-fa48-34e0-83b8-8614275ce9d9 | -5.35815 | -46.8682 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ee419f3-5a90-364e-97f6-0c76e21d5f33 | -6.30029 | -45.33601 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6410be6f-452c-36c4-b9ec-5091e4810bf0 | -3.96093 | -49.698 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b58c7027-a6a6-3fcf-add9-f1f95ab47e99 | -9.13068 | -43.10596 | 2024-11-21 04:31:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bce4c964-037a-3d4e-a849-c87d112984a2 | -3.73189 | -50.44179 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1370da5a-f338-3285-9621-c812170d24bc | -5.53821 | -46.36697 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fdb02b2-2c3b-3249-847c-7faffd9f7dca | -3.64589 | -52.35915 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf540b45-0844-38ff-a5ce-ed9b0b89bb0e | -4.5523 | -48.0094 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e17f7720-868b-3c42-a2a5-e81ea70a7a4c | -4.95377 | -47.80147 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c231001f-f34e-3d76-b846-f98fc6ef96ea | -3.56902 | -54.68895 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd7a9441-2b9e-34a9-a702-17007d6277ae | -4.13577 | -47.73353 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc4eb831-3acf-3481-8494-42f10897c1be | -4.63549 | -49.54813 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecca399d-2ebd-3720-a978-ba20d4bba22e | -4.81596 | -45.75716 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75ae4546-4050-30f1-8bce-ce512adbc55d | -3.3947 | -53.71422 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d3c66a3-a2d8-3704-9571-75b81895ffc2 | -3.19852 | -54.32359 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c1a091e-7098-3fd8-862d-57f0836bd9cb | -3.46208 | -54.56218 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50703ca2-54fc-3980-a047-cdb9502570b6 | -3.75942 | -55.5762 | 2024-11-21 04:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a33421d-b44c-3219-af31-07ca9acbf9a5 | -4.60911 | -48.47622 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e09b5dd-9f2a-3441-a4d2-1d7af6437dd2 | -3.51117 | -53.80509 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ab32b9-01c6-3729-9ad7-99bdf7ce7d06 | -5.18178 | -46.16996 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1068f364-3b01-375e-9f5a-655fe498b35a | -4.69809 | -49.62472 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b3d736-0a86-3167-a60c-272aeee85ff8 | -4.55398 | -48.02041 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4242aac7-57a8-3920-be8f-a614885561ac | -3.52018 | -53.80715 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef8241da-1341-3ea5-ad59-3dad08e689eb | -6.86748 | -44.75639 | 2024-11-21 04:31:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dee2f10-d61d-3fd8-b9c7-c9090fda1eb7 | -3.04727 | -54.41185 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52267bd-24f4-35f9-8095-dd738a282651 | -5.56452 | -46.35281 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c2ee4ad-4524-385d-b9cc-ebfee3bdfedc | -7.47038 | -47.18246 | 2024-11-21 04:31:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8761a8f0-ae92-3cc1-a1ae-e3ca7b829b71 | -6.63667 | -35.04136 | 2024-11-21 04:31:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f293a691-e7ad-3e53-822b-6a0e0e818858 | -3.74775 | -51.6012 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b191dc8-f1c5-36bb-ba7a-2ee41fb700cb | -4.29635 | -49.74582 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24ff8a37-46dd-31ab-a6c2-3d3b9de0beed | -9.13015 | -43.1097 | 2024-11-21 04:31:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7235bebf-c212-3e75-b719-d2d4dbcdd6a7 | -4.74306 | -45.39605 | 2024-11-21 04:31:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16abe357-b59e-30c3-a3a1-c741a6fad4f4 | -3.39501 | -54.55069 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ea2422-97dd-35b3-9dc5-b9a9a9875dc5 | -4.1019 | -50.31855 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fb4ed1f-ec29-3f4a-a545-512ddf18c7a1 | -3.28341 | -53.82219 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f1b45c3-3999-326e-b5c2-1bc550fdc3be | -3.59944 | -51.55531 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f2d001-6ac8-3a81-b080-c0037a4356b9 | -6.20668 | -46.22039 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3fe5fe16-e654-3ef6-bea5-4267ea6b4c4b | -3.05768 | -54.40816 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 166deaab-3d90-32e8-bf53-9f8eecbf39d1 | -10.66041 | -48.10828 | 2024-11-21 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 190c58c8-82bd-3b0c-8689-8e2373f7a05e | -4.60189 | -47.0304 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 523a6ae5-9b74-381a-9239-bb671cbe90a0 | -4.91259 | -46.83776 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 669532d1-9185-3529-b95b-c3029a2f192f | -4.83961 | -49.3522 | 2024-11-21 04:31:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3fa9662-58a0-3afe-8ba1-0c63232ed9cd | -4.49711 | -46.10195 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 214cbc51-f4b9-3868-b58b-e7e10aa5a197 | -3.10237 | -53.98717 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00b5eed-e425-33b0-8e53-4d2c597fae1c | -5.43143 | -45.34084 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48825107-ef83-3e28-91bd-ec7e4a816591 | -4.3483 | -46.14082 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf2f38dc-e646-3696-b320-de62a43e41bc | -3.80731 | -52.36636 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 47fb730f-7d92-3b52-ad83-15f6d0c97287 | -6.11481 | -46.00142 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README47.md)
