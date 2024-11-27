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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3738a60-9d42-3387-92aa-d66f9cad8193 | -3.8132 | -45.914101 | 2024-11-27 00:21:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b87c3890-f0a7-3c10-a8b2-6131fa6bab0a | -5.9545 | -45.363499 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0f300f8-6a9d-341d-a72e-2c6551d837b7 | -2.8086 | -46.8428 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ca0aab-8775-31ee-9587-9a0666164e92 | -2.5664 | -53.9506 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1dd4ff-d391-3963-ab72-80e7f2ba65c4 | -1.631 | -52.694 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2982e635-c408-358f-8708-714103fdc949 | -3.4174 | -50.274799 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba48a5b6-5e26-3bae-a708-1ed8fb3acd1f | 1.3922 | -50.603001 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfbc065-f0c5-31ce-9afe-f2b19ddd64d6 | -8.0404 | -47.077801 | 2024-11-27 00:21:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9624d5c2-b886-32a9-878d-cad69de1a735 | -3.7341 | -52.388 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913f6764-ce21-38aa-b4cc-cc91dd85eb41 | -5.3305 | -42.131901 | 2024-11-27 00:21:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3cfb822-54e0-3e17-95a8-c633ba2fd8c8 | -5.4739 | -46.2481 | 2024-11-27 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a28dbd1d-af0d-3db6-b62c-ad6ce7157e2a | -3.925 | -46.909302 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2d5a5c6-7c57-3489-95f0-43e9569ab607 | -2.0646 | -46.5606 | 2024-11-27 00:21:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6406795d-ea87-39ad-b96b-3f268c0b6d53 | -7.4662 | -34.856998 | 2024-11-27 00:21:00 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49c4544c-ff40-3afc-b8ce-c1f091e025c3 | -3.2117 | -50.133701 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9b444f-713b-3468-af0e-29d9fd991b53 | -2.3288 | -45.730999 | 2024-11-27 00:21:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91c0e555-06c8-31cb-8069-af702a6b2d65 | -3.9423 | -48.0839 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8727ebe2-948f-36d1-99e7-f7bf60de78e9 | -3.8026 | -44.3279 | 2024-11-27 00:21:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fa7873c-046d-3a01-aa92-c55e73454075 | -1.6439 | -52.436199 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25196a95-fe93-3f6c-9a26-d17ae07e38e5 | -8.1136 | -44.479 | 2024-11-27 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0a42fe2-ed4d-3c08-8a8a-9d21c2069867 | -5.9643 | -45.361301 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e250ac72-4677-357c-9abb-8abd929d8e80 | -5.7333 | -46.258099 | 2024-11-27 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de11e684-a240-3252-b938-d4e7eb2a98e9 | -2.2936 | -46.118698 | 2024-11-27 00:21:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd29af32-357e-3ea8-b55e-be5585ce825b | 1.3869 | -50.6259 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7abf57de-8166-3a36-950b-b03a6030fd0d | -3.0086 | -48.4995 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae341e3-822d-3a7f-a68b-20a8927edffa | -6.6689 | -43.060699 | 2024-11-27 00:21:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb8cc9e-9132-3be7-b2aa-0703992bc1ef | -5.9562 | -45.370899 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8db7779-6dca-33c4-91c5-a3aa46685ebc | -2.6624 | -45.656898 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66cb7e20-5974-3b2f-a9fa-8c021b3f9f01 | -7.6696 | -42.9716 | 2024-11-27 00:21:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe27c93f-86bb-36c3-b081-2f4f0e0643bc | -5.2902 | -43.076302 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60449de9-877d-312a-aa91-792976b9c9d4 | -3.5583 | -41.965302 | 2024-11-27 00:21:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57b14834-9756-3e2f-b466-d438f7aec8c9 | -2.8344 | -46.820499 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 428bab54-1103-3ba4-a98e-488fb9f3083c | -2.8576 | -45.3825 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f40cc499-323a-329c-a781-c4945a63c3f0 | -4.6728 | -44.979599 | 2024-11-27 00:21:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b57ba54-cb53-3476-be9f-eaa70e674af9 | -5.2341 | -40.608101 | 2024-11-27 00:21:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1baf11fc-1c4b-32e1-8028-9afe02dc3e20 | -5.3662 | -42.958302 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| cdeade12-6fc4-3871-97b6-aa89bb8b34d9 | -2.5251 | -46.410999 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f536c6d4-0073-3035-8632-ee64dee1a05c | -2.7846 | -48.5998 | 2024-11-27 00:21:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 571a58d6-7dcb-3261-81da-b3570da84cc5 | -10.1404 | -36.523201 | 2024-11-27 00:21:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 064f40b1-4561-3737-9183-2d726a913e88 | -3.3617 | -50.3004 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c5d77a-602e-39a7-84fc-d0228f6699de | -4.1903 | -47.219601 | 2024-11-27 00:21:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4334a4bf-ca3b-3a03-9af4-a6f3f9b5d032 | -3.3387 | -50.106201 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256cb49a-db61-36a3-aa9d-be619b295e25 | -1.8717 | -50.598801 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a2d16a-3e4f-3c1e-9b9e-3c33d7641d3e | -2.2597 | -47.916698 | 2024-11-27 00:21:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4a2e3e-8d9a-3c5e-9fd7-8a1b09ff4f0e | -6.6705 | -43.067501 | 2024-11-27 00:21:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74d44dc3-d5fa-3467-88cb-047c99c7c813 | -2.6641 | -45.664101 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7c91f2-0fc8-3c2f-a449-0889cd7bae71 | -2.5062 | -47.325298 | 2024-11-27 00:21:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b48f72f-3d8e-3988-a76b-969509b5b541 | -4.2824 | -48.1805 | 2024-11-27 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1efe5b-45e7-39b0-8de6-c0aeb2476db4 | -2.7771 | -54.120602 | 2024-11-27 00:21:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd34d8df-7898-379f-9831-845a1441f9c6 | -2.9034 | -48.625401 | 2024-11-27 00:21:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf76defc-1094-33be-9ff2-63faf6a28927 | -5.6964 | -39.197102 | 2024-11-27 00:21:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e1a2da21-345f-3bd0-8756-4967c0a62c19 | -5.6253 | -46.6493 | 2024-11-27 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9b5e017-832e-3848-8029-ab509814685d | -5.6986 | -39.206501 | 2024-11-27 00:21:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 590e1f7e-9723-359d-93a2-ae63c94ce538 | -5.3678 | -42.965099 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 1df80b11-71c7-33df-b56c-9557d7dae4cb | -1.6515 | -46.917801 | 2024-11-27 00:21:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ee9f3a-6d41-3e02-a789-a5c0b6bfce1b | -4.6269 | -43.827999 | 2024-11-27 00:21:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0289f92-9d39-3de5-922e-5112275cc86b | -6.1652 | -44.426201 | 2024-11-27 00:21:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 712469b1-e6d6-3887-820a-9aa890784530 | -4.1231 | -43.790298 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5051d9a8-7a2a-3396-a89e-9efaa8e80c08 | -7.125 | -40.263302 | 2024-11-27 00:21:00 | METOP-C | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f3b2238f-cbf6-3766-970c-a03336847eae | -2.2577 | -47.907902 | 2024-11-27 00:21:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715ac02f-9bc0-3bea-82e4-d34fd2c301c4 | -1.8279 | -46.652901 | 2024-11-27 00:21:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e93bddb5-0a8c-3831-8f19-9339e06a10e9 | -1.3975 | -47.475498 | 2024-11-27 00:21:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56124479-8b6e-32c5-8ea2-34c7d6d780e4 | -4.2783 | -48.070499 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88398781-5b14-3233-b14e-529935817192 | 1.3949 | -50.591599 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5670e80b-ef9c-3bea-b430-640872e88ba3 | -6.0693 | -39.4207 | 2024-11-27 00:21:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bceba247-39e1-321f-9a70-9c1bbc10a8aa | 1.3842 | -50.637299 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 30dbe0b6-b575-3d3d-ae9d-ca0412a75734 | -3.6847 | -47.668701 | 2024-11-27 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5c3449e-167f-3fc7-ab73-1d8b38db769e | -1.122 | -53.6833 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795e1090-b138-350d-8dbf-f76a8aa57aaf | -3.0689 | -41.145199 | 2024-11-27 00:21:00 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1b00965a-0534-3a9b-83bd-9c8a0961a1c9 | -2.8326 | -46.812599 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6141544f-fabf-30de-b75e-f498749c79ef | -2.9799 | -45.466801 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 963ebfa6-dcb4-336d-be2e-2002c398a1d9 | -3.3415 | -50.118599 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a234a7f-52b3-36b8-801a-b55ecbb56ad2 | -3.0129 | -48.519001 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540f3cb3-9718-37c7-9964-fc3902637bc4 | -4.2095 | -41.9254 | 2024-11-27 00:21:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8fc5a2fc-64b1-358d-bb51-159381600b0a | -2.9892 | -48.596199 | 2024-11-27 00:21:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63d7803-8821-3592-ab8e-0f01add1ad19 | -1.7859 | -45.926701 | 2024-11-27 00:21:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd69a112-5754-3949-af74-4e6e186765ea | -6.3278 | -35.121101 | 2024-11-27 00:21:00 | METOP-C | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33fee62c-2fd3-335b-bcb6-a3fab3171afb | -3.2513 | -45.436501 | 2024-11-27 00:21:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35fc3b22-3f20-3cd0-b49f-41759b61d5e2 | -3.5566 | -41.958 | 2024-11-27 00:21:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ce7fd901-8b6e-3b00-b821-d5c6971a54bf | -3.8907 | -42.4207 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab486f10-cc2b-3c8f-947a-b919aa88d583 | -3.014 | -53.2701 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e1cd55-79e5-3332-9ab7-69a739664b27 | -3.9097 | -46.887001 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3220a28b-50cd-3015-9736-a33b4caa92bd | -3.9886 | -47.648998 | 2024-11-27 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6b0c47b-defc-3e00-b2c9-699ba716d885 | -1.9234 | -45.716301 | 2024-11-27 00:21:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b13ae11a-d236-3151-a227-f3bdbfd86767 | -4.3824 | -44.112202 | 2024-11-27 00:21:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89028186-ae52-393a-9cbd-e6982b03412b | -2.7148 | -45.660301 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4211e15d-0c17-3809-88be-74c07a164196 | -10.1269 | -36.176601 | 2024-11-27 00:21:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33390da7-a708-3a71-b7d1-80b46e9de46a | -3.3547 | -46.299198 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76807717-b3bc-31c1-9310-ac72c0767888 | -4.1309 | -43.824299 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0fdb179-999f-3d01-8b74-27301d154fa7 | -8.1103 | -44.4645 | 2024-11-27 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d515ad3-1529-34c4-8cde-2e1a92a69a23 | -3.0751 | -48.02 | 2024-11-27 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6eb61d3-7676-37aa-8689-8cb322ff9b14 | -2.5081 | -47.3335 | 2024-11-27 00:21:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a33d206-7a03-3b17-b51f-783d887eec9c | -3.4203 | -50.287701 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 386479a7-aca0-360d-ba30-0c5fd724cbc6 | -3.0183 | -48.497299 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f9eaf3-44c8-3183-a0b5-a207ea290220 | -2.8308 | -46.804699 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a624e784-19e4-3664-85b3-04487e0d2a61 | -5.9626 | -45.353901 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06dbeb21-48ab-384f-b976-6a626517d19b | -2.7996 | -46.803299 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6669e83c-f202-32ba-8940-e4f8cbf1e089 | -6.8707 | -34.987099 | 2024-11-27 00:21:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e89d620-3cae-3d2a-86eb-6f9e60da96f7 | -1.417 | -47.1092 | 2024-11-27 00:21:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6b8783d-d3f8-3750-8666-0bd1401f5434 | -6.8071 | -44.394299 | 2024-11-27 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
