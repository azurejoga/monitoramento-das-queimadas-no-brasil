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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89409c06-dcbe-3526-9d27-940bc11816a3 | -12.86082 | -44.61631 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4733c266-c893-30f3-9552-b2f845233dc9 | -12.86039 | -44.61972 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0948792a-9fe8-3f10-a91c-b2117c40293c | -12.61339 | -44.78688 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 686cec9b-984f-36c7-8b74-0cb13c593456 | -12.60976 | -44.78637 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e05b4e1-15ae-363b-8b53-3987120bd222 | -12.60847 | -44.78278 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a7e714-90d8-3813-bee6-064d089a151b | -12.60807 | -44.78616 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48dba4b4-4fd8-3004-a15c-c13cd2d85f69 | -12.57751 | -44.74083 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a34b116a-197d-3499-9ce9-bb6bfa0e43a1 | -12.57709 | -44.74427 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57ab4439-a272-318f-89c5-c6a6dcd0a733 | -11.44005 | -45.29136 | 2024-10-15 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7541f85-1157-39d0-8c5a-37f5de5f74a0 | -11.43967 | -45.29427 | 2024-10-15 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d73c926-a99d-3237-a1d9-5beecec84cb0 | -13.92359 | -45.82259 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa8d43ef-a23c-3dc2-b122-de7498ef74ce | -13.92323 | -45.8256 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f15542e3-022c-3245-97b1-41a32517f036 | -13.92286 | -45.82862 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 705c6f06-b219-39a8-a863-ff460c69100b | -13.92249 | -45.83162 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f5290f8-2305-3e95-8786-f83ebf52c97f | -13.92213 | -45.83462 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139b224e-8fa6-3c4c-a08f-82d920ba324f | -13.91927 | -45.81589 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9134c25d-94d3-3e27-afaa-3d9790b387d9 | -13.9189 | -45.8189 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44d2013d-be9d-3687-8e40-745973354f81 | -13.91854 | -45.82192 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 52de28ab-6328-3996-a582-50323be1449f | -13.91817 | -45.82494 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| dbccce73-efd8-3a6e-b20b-350fc3dc447e | -13.91781 | -45.82795 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e901ce2d-b15f-325e-8271-a4b1d3aef07e | -13.91744 | -45.83096 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8127725e-5f7c-336b-b6fc-ede07596e316 | -13.91708 | -45.83397 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fd530a17-c28f-34c6-ae1b-0cf33ddd5404 | -13.91671 | -45.83699 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a351946-fc43-39a4-abb0-766d3ae48bc1 | -13.91634 | -45.84001 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2c5bd6-7be6-3408-88c4-0acf5677660e | -13.91458 | -45.8122 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72a32036-3aee-3401-b72c-68a24a7259bb | -13.91421 | -45.81522 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 310408e9-fa19-33e3-bce6-cb7bdb4ecb26 | -13.91385 | -45.81823 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0039dbe-0f9b-3a65-87d0-6d4575983cfb | -13.91348 | -45.82125 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 2b93670d-edda-3940-8703-15ef730126ce | -13.91312 | -45.82427 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1225ef7b-f6e7-3ecb-b50c-eeec00dc5909 | -13.91239 | -45.83032 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f6e74d1e-746d-3974-aabb-6425b62680f0 | -13.91202 | -45.83333 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6155dfdf-4067-3739-a19b-1ca0fa45c799 | -13.91166 | -45.83635 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4fa12bb5-4ad6-3f5d-9314-ad1ad1948b3c | -13.91129 | -45.83937 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7437e33-30c8-38a5-8224-6522329ba664 | -13.91093 | -45.84238 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8938fbdc-a66c-368b-bf6b-b38c85f5ec42 | -13.90916 | -45.81456 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cbaeb2d-6cdc-3947-984d-c4c258994596 | -13.90879 | -45.81757 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97238468-cd7d-383c-8d73-871d3072fe89 | -13.90843 | -45.8206 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae1476c3-03f1-31da-9fd4-385c7d2b9c90 | -13.90806 | -45.82362 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e062a145-93bd-3e3d-8387-991ed9b850c2 | -13.9077 | -45.82666 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95098f07-3c07-30b5-83ca-f4720ccc1d03 | -13.90733 | -45.82968 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b341859-84ed-358c-b6be-c6c24ed8cfb4 | -13.90697 | -45.8327 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a58b057-b383-30b3-9fbb-8965d3a1729c | -13.90661 | -45.83571 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4274f67-8ec0-3f9b-8215-0d9087a8418a | -13.90624 | -45.83873 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 22160d73-33cc-3be3-a6d4-6030f3f7189e | -13.90588 | -45.84173 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26130588-fccf-3958-afa3-11f560fc0832 | -13.90373 | -45.81693 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 878fae32-4ce7-352c-9a22-10fbe9b2925c | -13.90337 | -45.81996 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c660f52a-acb4-3e32-a7c5-0d1b088b3ed8 | -13.90228 | -45.82903 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eef79b3e-246d-3904-980b-3343899721a2 | -13.90192 | -45.83205 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a3a8178-2313-3020-8226-42d97301c0df | -13.90156 | -45.83507 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ea4e816-5ede-301b-9d08-d99e7ae347dc | -13.90119 | -45.83807 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b69bc08-dc19-374b-851f-9a0576716169 | -13.90083 | -45.84108 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b18b386c-5937-3970-ae54-04b4e85bdcb0 | -13.90047 | -45.84407 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e04566fe-5653-324a-9210-ae61a7f0b4a0 | -13.90011 | -45.84707 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c73ef51-211b-34c6-b0ef-72eb4c5380a9 | -13.89867 | -45.8163 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7c3c91-cb98-3fc1-ad71-45c8639f10d6 | -13.89831 | -45.81932 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88a9a63c-d48a-37b2-b6b3-ddcc828f0b68 | -13.89795 | -45.82235 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18a4fe2-f114-3afc-8852-fa66cbbb3d85 | -13.89759 | -45.82537 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d752964b-4f38-3e86-be9e-3742a0910ab0 | -13.89723 | -45.82839 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bcaf123d-b7c1-395b-93e9-b6e46cea4e09 | -13.89614 | -45.83743 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c7e65764-8ad4-3324-8066-a003af7e75d3 | -13.89578 | -45.84042 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6c3a0f70-a032-3a00-aa6e-fc786ab5eb1f | -12.90029 | -46.92978 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89d1827-934d-3dd7-8e44-c2f5a80611ee | -12.89972 | -46.93426 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de9c892d-28c2-341c-b25b-44044596920d | -12.89147 | -46.93069 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83cc8625-575f-3c5e-b067-03a71d98db6a | -12.89106 | -46.92842 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d52b5a0-3d93-34c2-9a92-4cfa54324587 | -12.89048 | -46.93298 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 130de2c3-b21f-3a05-b699-6d0c6fa4f4aa | -12.88686 | -46.92998 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c694d37e-c8ad-302c-87a9-0bbb7be0ed41 | -12.88586 | -46.93233 | 2024-10-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2509a0f-5456-3beb-94cc-949942800d45 | -14.11523 | -46.98345 | 2024-10-15 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757fae52-60d1-3c3f-b192-e427bea99d71 | -11.10189 | -47.7014 | 2024-10-15 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70e16de6-4def-31b6-96a3-1936cb8336da | -12.10103 | -50.25411 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7584ff0e-9d07-3439-8cf6-1788060b9578 | -12.10038 | -50.25855 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f88eb79-10bc-35b2-b1da-ad9153918f23 | -12.09604 | -50.26244 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 435cc4ab-fbcf-3633-aefa-994587e81708 | -12.09432 | -50.31902 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d66f96b-71d5-3295-8df9-81279e41b10f | -12.09129 | -50.3205 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8b41f1e-24f1-3c49-95d7-05a0a038007d | -12.09064 | -50.32491 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6b68d2f-6f78-346f-97cc-5bf48c088269 | -12.09002 | -50.32288 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68f80e89-ff71-39a7-8ab0-26385e3c7d73 | -12.08696 | -50.32437 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ec895a-4119-3f4b-be5e-eec87c1e083e | -12.07997 | -50.26913 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4ffeee5-7578-3ec7-90a2-f3774e958537 | -12.0796 | -50.32327 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 858ebcdb-6ddd-3c57-a898-f05684a48787 | -12.07933 | -50.27356 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5950f604-cea1-3a46-99d5-70f2c5ce54b9 | -12.07628 | -50.26859 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72065eef-9d6d-3063-a5f5-9aa1884e0389 | -12.07592 | -50.32272 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46f55219-240e-3f96-a645-d2678cedd4c3 | -12.07289 | -50.31777 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00a99913-fe8b-317d-9c6f-a823bf597f12 | -12.07049 | -50.3084 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 061d4855-92b7-366d-b4a2-0a56f3fa0986 | -12.06985 | -50.31281 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77ab5eb6-7097-368c-a0c7-86c7f726bba8 | -11.6048 | -49.86823 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c5f76c3-257d-30c7-9461-0447e46df9eb | -11.60105 | -49.86768 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e515bc6-edff-3239-8991-23635e451fd8 | -11.59264 | -49.89923 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b232a6d-053d-3708-9f31-b9e05bec5748 | -11.58694 | -49.83274 | 2024-10-15 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c4e78c-9f52-3856-9c98-d216f98774a0 | -11.15002 | -49.7025 | 2024-10-15 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84d6909f-6f8d-3438-af75-ccf98c61ca72 | -10.66609 | -51.82349 | 2024-10-15 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9ab8356-1e0f-3e52-9b7a-f39fea316518 | -10.66553 | -51.82719 | 2024-10-15 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25c1a633-a711-3ecd-b6ee-bee66911ff17 | -10.66497 | -51.83088 | 2024-10-15 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc70cc84-f930-3a1d-a482-c3c768d6bc06 | -12.0791 | -51.06079 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02bdea7e-a42e-31b2-87aa-ad4a3183f084 | -12.0785 | -51.06486 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45692fd2-5959-37d8-9e68-52420ec26f07 | -12.0779 | -51.06892 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eee6f90c-ceea-3b3e-9dea-ff575447be6a | -12.07729 | -51.07299 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e555b9c-8c1b-3d69-ba0d-1749a2218801 | -12.07669 | -51.07706 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4de1168-d900-31d9-b6d0-c9fcf9bde457 | -12.05064 | -51.1063 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea340204-7021-3624-ad93-b243342de380 | -12.0471 | -51.10576 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README68.md)
