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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 015b81b1-7827-34f6-84f6-5bd5840e44dc | -18.65927 | -57.25045 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 74aa0b96-a1db-3564-93c8-c8026ea25934 | -18.65651 | -57.24601 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 44baf5c2-2816-3425-ac99-e199d6774a83 | -18.65588 | -57.24984 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b0d3f288-be3b-38cb-931c-0694f894f841 | -18.65312 | -57.24539 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 29c4df3f-ff2b-3a14-af67-dc518855eaac | -18.65248 | -57.24922 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c50c9af2-dd82-3427-b426-8b25d15b9d7d | -18.64973 | -57.24477 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 8409aa7e-c06f-3ece-93b0-1d1cf5987b34 | -18.6493 | -57.26841 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7c9eb14f-219a-37e5-a169-5612549810f3 | -18.64909 | -57.2486 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5d1b2645-0852-343d-ad46-4583d0fa9482 | -18.64846 | -57.25244 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 8f1065d3-6e4b-3060-9fe5-74e82a15eddb | -18.6457 | -57.24799 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2778e323-7ce2-3d6a-8958-bd5f05c894da | -18.64507 | -57.25182 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 67827fe6-fc0f-32ee-a148-536685303798 | -18.64443 | -57.25566 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 277c024c-9eb1-339d-9216-3fca6f43d0cd | -18.64168 | -57.25121 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d1a5f52f-ce6b-3a98-bc95-25a8133184a4 | -18.64104 | -57.25504 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 24d0b918-1b98-3052-9f9b-d0b2db133736 | -18.63701 | -57.25826 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ecd49a1c-c74a-37da-9cab-a76ad2d506b6 | -18.63362 | -57.25764 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| bc62008c-bbbd-32d0-bdfa-915ca8409f29 | -18.63298 | -57.26147 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4ec18cf8-194e-371f-aa05-9e37ea49a3ef | -18.63234 | -57.26531 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 9aef257d-69a2-3def-999b-921001ea19c4 | -18.6317 | -57.26915 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| defc6a5d-504b-3e89-9e70-38abfa0cd4f4 | -18.62895 | -57.26469 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 29a5a8c3-55a9-31b6-8379-9272191817e3 | -18.62831 | -57.26853 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 683dd6d1-6a35-35b9-8f8d-9dd01c082a07 | -19.14016 | -57.51092 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 149c307e-7bb0-31f9-b479-6cc14f5376c1 | -19.13608 | -57.51432 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e9217a2a-daf0-3a4a-9739-aee9b4a1ca43 | -19.115 | -57.51447 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 94a72723-11bb-3e36-8a96-6b25abc78896 | -19.11468 | -57.47463 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a1f2fe7-c94f-34eb-8d3b-1e3bfb750d34 | -19.11227 | -57.50982 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b3838d72-161a-3686-8c7b-f09eacb72abf | -19.11159 | -57.51386 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1259fca3-0596-308c-b408-946ec90196e2 | -19.11128 | -57.47397 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ff92213b-1b4b-31e6-89a3-ea9dd6fde51d | -19.11092 | -57.51785 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 998a4380-8ef1-3ff8-9b5a-da94c3962276 | -19.10887 | -57.50922 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1960db15-9d1d-3538-99ca-1526f9f14380 | -19.10819 | -57.51324 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e7f12c5-5bd1-36e8-b191-2a0052bfa216 | -19.10788 | -57.47337 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 36e814f6-cb20-3142-abbb-60ac624116eb | -19.10725 | -57.47712 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 74225498-75f0-3f02-b162-906ecd6c463b | -19.02294 | -57.62277 | 2024-10-07 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9d6c56b5-496e-38a9-b2ba-1f75b1a45c83 | -18.72945 | -57.29495 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c1473ae9-1853-35db-bbe7-189fb3404dc4 | -18.72881 | -57.2988 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d39d5d2b-00fc-380d-b79e-3eb9fdba5d55 | -18.7267 | -57.29049 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01ffa751-6baa-3560-8df2-010d48f7a1a3 | -18.72606 | -57.29433 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cf0e712b-21f6-3f6e-9330-cdb630f39c60 | -18.72541 | -57.29818 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| d13f6747-60f0-31e5-ae3d-bab54fed4356 | -18.72477 | -57.30202 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 1930d8c0-b614-328e-8aa2-534292e9365a | -18.72413 | -57.30587 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 12df2b1e-d731-34cb-8ec3-d52ac254f08a | -18.72395 | -57.28603 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4b112e2b-5fab-39b2-8fba-e55ebede9242 | -18.7233 | -57.28987 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a552e85b-31ec-3dd1-b78f-be8cab12a543 | -18.72266 | -57.29371 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| db06b456-d6b8-316b-884c-194f3c74d6a7 | -18.72202 | -57.29755 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 5a0180d0-3659-3ffa-9334-ae52b486e701 | -18.72138 | -57.3014 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| a2da3819-d572-3bab-9c96-adb4e28c8b83 | -18.72074 | -57.30524 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| fc2e10d7-e35f-3e52-8a6f-5385cb22aa20 | -18.72055 | -57.28541 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5b273fb5-6de3-35b5-b091-a8ae42a14db1 | -18.71991 | -57.28925 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9b97958e-1947-3844-a69e-28944340fa14 | -18.71927 | -57.29309 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 59b755d1-30dc-3273-acd8-cb555b11d9d6 | -18.71863 | -57.29693 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 744460ba-f5a3-3a83-a08a-7fefa46a49f2 | -18.71799 | -57.30078 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 45ce3406-ef12-3407-8e77-846839c7a2eb | -18.71734 | -57.30463 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 971158eb-e838-31ef-bbd4-00b83e000a70 | -18.71652 | -57.28863 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c65afbe7-d078-3920-b426-65a8a1d84851 | -18.71588 | -57.29247 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d213b94b-4e12-3dc7-9bc4-775b3f44319a | -18.71523 | -57.29631 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aa4baeb5-1abc-3ec2-8560-ce95f3da15a4 | -18.71313 | -57.28801 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 34076c5e-9be6-323b-821e-fe70e2c6f95a | -18.71248 | -57.29185 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d4c16453-3af4-39be-88a4-c5439f26e550 | -18.71184 | -57.2957 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 468c18e4-cbdd-3caa-bba6-353ba56a2bb4 | -18.7112 | -57.29954 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 062e8f05-47e6-3b6c-a5c7-144929c80f26 | -18.70973 | -57.28739 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b6638320-e051-34dd-93cf-c465d99df9e0 | -18.70909 | -57.29123 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fd2da729-cc0f-33b1-afbe-2715e3637f6f | -18.70845 | -57.29508 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 880c04c8-8b47-333b-bedd-faa4e3b74e2c | -18.70763 | -57.2791 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 74fe9216-ae24-3591-a88a-4e825c787e42 | -18.69698 | -57.3009 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c17c4fd4-6988-3e70-8cff-7c9c82df9c43 | -18.64208 | -57.29083 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3608bbae-444f-3711-bba7-f950433e2e8b | -18.63106 | -57.27299 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87770198-4e8b-30c0-9381-e5c2e3fad811 | -15.66959 | -59.44525 | 2024-10-07 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 583aa543-7e52-3e83-b1c4-b809de75b1c5 | -15.66865 | -59.45057 | 2024-10-07 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d7b7c1a-12cd-35c1-8d7b-d1e7c546896e | -15.66476 | -59.44988 | 2024-10-07 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bae925b-24e3-3809-aca1-6b8236895b76 | -17.63422 | -46.98034 | 2024-10-07 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 413cef67-57d6-329b-ab09-6045b046c468 | -17.63197 | -46.98049 | 2024-10-07 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8463de61-ff23-308b-a7dd-e13f9cb8ee9d | -17.61082 | -46.94789 | 2024-10-07 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6fb60395-555b-3b3e-ba9c-e34d95f61cab | -18.30762 | -47.13849 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0d3ddf0-6c7c-3336-a742-8776e400e2a5 | -18.30343 | -47.13136 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50dcff1c-c9b5-3fe9-979b-0371f8d4b71b | -18.30268 | -47.1381 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f81f49c-64a3-3060-91fb-3720e971d516 | -18.30202 | -47.14397 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5856eb4-3832-3825-b62a-4a4753689e31 | -18.30139 | -47.14954 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a6ba00a7-5134-3ca6-b750-a95b7e8a7b96 | -18.29778 | -47.13741 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0b5bab4-6aa4-3681-8b1f-b9fe1570ec76 | -18.29712 | -47.14328 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 935395b6-a8b9-36da-ada0-0b7ed7a143e7 | -18.2965 | -47.14877 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 09696164-ce00-3092-a442-72afb824ccfb | -18.24563 | -46.40533 | 2024-10-07 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d1204a-65e2-3fc9-9441-17dce58080a5 | -18.24118 | -46.39815 | 2024-10-07 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30bf3d95-c08e-312b-acb3-6fb947ef8719 | -18.24083 | -46.40142 | 2024-10-07 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c72a686-3041-31e7-b0ba-b59ce28ee4a5 | -19.19712 | -46.57622 | 2024-10-07 04:55:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9064a8d-2728-36cd-81f3-ee316ef47d15 | -19.1968 | -46.57923 | 2024-10-07 04:55:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a649e179-1198-34c4-8fd3-a67123f68133 | -19.19198 | -46.57542 | 2024-10-07 04:55:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f16b87f-44eb-3e1f-9757-4d589737570f | -18.59395 | -47.3099 | 2024-10-07 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4d758514-f05b-3513-b38f-a1df27e9deb5 | -20.47327 | -47.66332 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7298e5d7-4e0d-35bb-84ff-2fbea1eb9223 | -20.46899 | -47.65713 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ced0571-bb41-3903-a17e-0951f9a802ee | -20.46659 | -47.6795 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2256d8a9-13b1-3b24-b8f5-5b7464d2847f | -20.46289 | -47.66795 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e593e82a-56fb-310e-9429-8724020f6df2 | -20.46171 | -47.67904 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 71753bc2-feaa-351c-a5ab-5c6cd02d495d | -20.45197 | -47.67773 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 56b58bc1-961d-3f50-8037-9e464951b0b0 | -20.44777 | -47.68835 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ed9a8067-4436-3f46-b6fa-7f69eb30a0ea | -20.44651 | -47.68259 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7cad257a-ff3f-3562-8192-1b357c8a4355 | -20.44518 | -47.71113 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| abd984f1-6a8c-3b7b-bf52-1741f57294a3 | -20.44035 | -47.71031 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d9355e37-a853-3ea8-a0ad-352a61f7343a | -20.43987 | -47.6988 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7b5c8132-2e0d-3a5e-ad97-1fd707e48903 | -20.43807 | -47.68676 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |


[Clique aqui para ver as próximas entradas](README89.md)
