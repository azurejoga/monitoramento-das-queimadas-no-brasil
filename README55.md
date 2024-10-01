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
| ed53d00c-8ebe-3710-a22e-975a6454f304 | -21.56842 | -47.79529 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aae96f32-a1e5-3bdb-89ae-da139437f4be | -21.56792 | -47.82136 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b856f91-6562-39d2-b17d-35a522ca2176 | -21.56744 | -47.80013 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab32e5a7-57b5-3a20-8f84-04c1ea6389d3 | -21.56686 | -47.82656 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1658fa5-15fb-3ee4-a66e-91b735ea8469 | -21.56644 | -47.805 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de262bc6-25e9-3036-b57a-61fb6c198eae | -21.56579 | -47.83183 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 079618ac-44d7-3741-96b6-11a933df0305 | -21.56542 | -47.81001 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d81f481-68bf-36a5-9fc4-adb4fdf08d38 | -21.56472 | -47.83712 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 918a2910-85f9-3458-9056-48696f552593 | -21.56439 | -47.81509 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8c68608-9e02-3551-b9a6-7453ea0a909a | -21.56334 | -47.82021 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99f5c6b0-50b4-3d36-9b2f-bc4e9588200a | -21.56229 | -47.8254 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 210d5555-6faf-3a8f-a671-b3d63949e61c | -21.56183 | -47.80406 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6360b3c-feb6-332d-816f-e04e9b23fc2a | -21.56122 | -47.83064 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3e825c5-5d56-3347-b69a-565fd42da326 | -21.56082 | -47.80902 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a475a6d-b98c-31bf-9e2a-4ad273dfdcf7 | -21.56014 | -47.83595 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebec870c-6605-31da-85cb-263e55d75447 | -21.5598 | -47.81403 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd2a2ee9-f327-3e80-882e-c946710e9790 | -21.55913 | -47.84092 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7c741d9-640d-3629-854c-2dd0696427d1 | -21.55771 | -47.82426 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 917a40de-8bd8-3abc-8773-d9d79142347e | -21.55664 | -47.82951 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a06a52-e77d-3536-891e-eb096b47e4ab | -21.55313 | -47.8231 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf91ccc-1e2d-393c-ad80-e4fa55129270 | -21.55206 | -47.82833 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 255c4ec7-90f6-3a72-80a1-68299b2de880 | -21.61107 | -47.87001 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fd6d16c-5741-3d7f-ba5e-6fe32966c048 | -21.60852 | -47.85872 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f09d551-6e26-3b1f-8564-757cd6e11f99 | -21.6075 | -47.8638 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 771337ed-d0c9-3f51-81c1-86a9f613862b | -21.60669 | -47.85971 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf062ff8-def6-391f-ae2e-a6f0629ac5be | -21.60648 | -47.86891 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 446f58a2-55ae-39ca-9622-ec8c1428034c | -21.60563 | -47.86479 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9753e3ae-2689-3f04-bd74-129fd6f8527e | -21.60315 | -47.85355 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e5b9465d-1951-3abc-a349-9efd11f916d5 | -21.60137 | -47.84634 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72d0191e-2092-3030-af35-d0d6129567ce | -21.60035 | -47.85143 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 051dc3c6-2f31-314a-86fa-14f74f48b6d9 | -21.59961 | -47.84739 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c00b18b9-95ba-3f1b-a53a-9dd7b6b7e873 | -21.59933 | -47.85651 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fec067d4-014f-34c8-a19e-5b06a478cf4c | -21.59856 | -47.85246 | 2024-10-01 03:51:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4a2351b2-b290-3488-bb1e-5109290e75d9 | -21.5983 | -47.86161 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6eba2245-a427-3ded-a800-f91b193257e0 | -21.59678 | -47.84524 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d2f1e32-de2d-33b6-83f5-c86e1e0a684d | -21.59643 | -47.86264 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6de956e-be23-3d25-9918-fbf2fcb5b988 | -21.59576 | -47.85032 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97a89322-6065-3eda-b182-145ccf336cd2 | -21.59473 | -47.85542 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66265e1c-5a1d-35e9-a4b4-35e115f69dc4 | -21.5937 | -47.86053 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65c1bb13-0e65-3921-b56f-2550817cde1f | -21.59267 | -47.86565 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df5c7a14-dba2-305c-8851-200e668216bb | -21.59164 | -47.87077 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c74d3cd-ccb9-3dc0-85ae-1fd3fcee3238 | -21.59116 | -47.84922 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 545a5098-7980-36fc-8801-ce99729b9cc6 | -21.59013 | -47.85433 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 5cea5cd7-1f4f-37cb-a0fc-1ed0f9a1e99a | -21.5891 | -47.85945 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 7dd43ec8-12c8-3ebc-a85c-813577929ae2 | -21.58807 | -47.86457 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 95f618b5-6fd1-34dc-b5bc-c702054a2749 | -21.58704 | -47.86967 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 918f37a2-095c-3eac-90a5-e715f311fe2f | -21.58657 | -47.84809 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9575216a-2520-3f02-8f45-a556d8605f51 | -21.58554 | -47.85321 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 1c65a273-6403-3ac9-8649-75da6f71bb91 | -21.58451 | -47.85834 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 5deeb974-6aa5-334b-8737-83330bab6681 | -21.58347 | -47.86346 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 847b2eea-79d8-3ad2-badf-4c2d1dc82407 | -21.58244 | -47.86857 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56f61db3-72a8-3c22-a05d-703aa04a8855 | -21.58201 | -47.84684 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08247c05-5984-3cee-bc49-f277a03a61b1 | -21.58141 | -47.87368 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5221ee3a-3007-3920-b121-6b25149dd67d | -21.58096 | -47.85202 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 97dd57d6-3b72-3134-943d-85f2d0bb9855 | -21.57992 | -47.85719 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6d35cdc2-4d76-329f-9c50-4fb5ee19a0f8 | -21.57888 | -47.86232 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| effb15c3-16ad-3489-8b1a-447e0a129d2a | -21.57785 | -47.86742 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a1da0f6-7809-3205-a045-b3040402459c | -21.57745 | -47.84557 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5ddc244-a266-3a90-9e93-b1e83de3a7de | -21.57681 | -47.87253 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 918c5a53-166a-363c-8d17-3974e1581392 | -21.5764 | -47.85072 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c9516cac-ba34-3b9f-b78d-0db9e5462cc9 | -21.57536 | -47.85587 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 73d5ef86-8960-3da4-8006-4e58df498b39 | -21.57433 | -47.86097 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c91f22c8-8d6a-383e-806d-2ecfa5cbaa1d | -21.57328 | -47.86614 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2419f9cd-95e3-38a4-9e0b-b157a35a172c | -21.57267 | -47.89298 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d28aba84-7e32-36b5-b51f-2fbf3c8e2067 | -21.57223 | -47.87135 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac260d72-facf-3c8c-a79b-1680476b0c93 | -21.57163 | -47.89809 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f78841c0-3279-3c77-8035-44e127f35519 | -21.57082 | -47.8545 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1ad6812-39ca-3c5f-89e9-94e3bc093b48 | -21.57016 | -47.88155 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8f24d33-aab0-3fc4-b642-8c47f610a04b | -21.56978 | -47.85963 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee17afee-297f-3838-b2a8-ec6b11eddcfc | -21.56912 | -47.88666 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b1868b-4dc0-3370-8abf-af8425c0641d | -21.56872 | -47.86486 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32ff1c77-387d-3aae-b3ca-ea40a85fac8c | -21.56809 | -47.89173 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 742b3d41-500f-39de-a607-f69544835b17 | -21.56764 | -47.87014 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5538e3b-f8fa-3465-aff9-6b3ca45bf9c4 | -21.56627 | -47.85319 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fc79fe0-cdad-3f8b-8ee1-7ffc71b185d1 | -21.56558 | -47.88033 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa5bbe4d-86dd-315f-9659-aa9c731f372b | -21.56522 | -47.85835 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76512700-c6c1-3fc6-883a-1cd1449f7d94 | -21.56415 | -47.86361 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd87c664-1635-3309-af95-340182dabca4 | -21.56065 | -47.8571 | 2024-10-01 03:51:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2f548ec-c12f-3032-b25b-dae85cbe6bb5 | -21.38076 | -48.47341 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7048fa49-1ec7-32e2-b1d6-d75726711c70 | -21.37957 | -48.47924 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9abdc2fb-042f-3434-bc83-cc24b12cedaf | -21.37821 | -48.47483 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b381fc00-1cee-3826-b996-6389ff5e4811 | -21.377 | -48.48059 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f634b01-d8a6-38fb-b38f-90cc0a488cdb | -21.3758 | -48.48624 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bfd2c73-28f6-37fd-b484-7bc9286a340f | -21.37486 | -48.47766 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1209d847-c432-3dc2-ab8a-b6d83e96e647 | -21.3737 | -48.48336 | 2024-10-01 03:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9e3eb6c-b345-35b6-bf87-67740f38a7d0 | -21.70017 | -54.80313 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df33e38a-bf4c-3a39-b78c-24946e7a533a | -21.69507 | -54.79434 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a7ae7be-8ad2-3434-9f5c-cc616a0c4029 | -21.69337 | -54.80107 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 049fd2f5-4531-3e60-a7c9-0c83e2f8d800 | -21.65039 | -54.85469 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97a7d0b9-5905-3b26-b110-d253ffd74d0d | -21.6454 | -54.85485 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96d02275-b63e-3b32-a4ea-d76d839c545f | -21.64358 | -54.85257 | 2024-10-01 03:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b971446-a325-3630-b0a2-801a837fb501 | -22.6753 | -47.04979 | 2024-10-01 03:51:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a05a639-161e-38c9-9164-d3bc884f94ca | -22.67527 | -48.35318 | 2024-10-01 03:51:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d02e6d4-9b63-3c0a-a01e-57cb361571dc | -22.67104 | -47.04866 | 2024-10-01 03:51:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d1d55c4-1dcb-328b-af65-1928058b6822 | -22.56095 | -47.93641 | 2024-10-01 03:51:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 488c9260-fbe2-3d4e-b67c-6b6a4ea0a9ef | -22.53929 | -48.8149 | 2024-10-01 03:51:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fba5048d-84d2-3d96-b2df-d0629dce3e8b | -22.12221 | -48.56109 | 2024-10-01 03:51:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5709937-d69c-3e4b-a689-ab221e8ea440 | -22.11985 | -48.55296 | 2024-10-01 03:51:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 301693d8-3d89-3a52-bb95-77108544d3ca | -22.11868 | -48.55871 | 2024-10-01 03:51:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cbcab2d-5a07-3c39-8ce4-bf92e3861108 | -22.11864 | -48.55438 | 2024-10-01 03:51:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
