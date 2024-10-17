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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0729d609-377b-3e07-850b-517dd68cf1f7 | -3.93353 | -42.41698 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 175fc9f5-4b0a-3e09-abb5-924f045ad889 | -3.93323 | -42.41025 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 385b0f83-d000-3308-8d09-8e1157d3cae0 | -3.93283 | -42.42128 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf6e3a0a-6ce4-3d83-bb12-943d4dd88bc7 | -3.9325 | -42.41454 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d760b2c-22e5-3b4b-a1a9-00b5355a6e9a | -3.93214 | -42.42559 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 81e5e5c0-68c6-3124-a706-77d5802ed5a6 | -3.93178 | -42.41882 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f685969-b82d-3865-8406-102c876a7412 | -3.93119 | -42.40335 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 70176f31-5501-3817-91b9-8e9acf284bf1 | -3.93105 | -42.42311 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbc295e5-7cc9-37d9-8b76-cd8e2c4ddc1c | -3.9305 | -42.40765 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7feed2eb-d85f-350e-bbaf-a57c398c161f | -3.93032 | -42.4274 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 715672b6-fa9b-3a87-b4db-941f3393d41f | -3.9298 | -42.41195 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96087745-569a-3642-9da5-580bd96f54b8 | -3.92911 | -42.41625 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 78a50c77-9eab-3f56-b9a7-d234cbb21429 | -3.92841 | -42.42055 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 61a6ab11-71bc-38ef-b51b-d50504f69b3c | -3.92772 | -42.42485 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e0aee59-4d80-377b-803b-cbd924dcecf8 | -3.92702 | -42.42916 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b8fe20c-a953-33e9-abcb-336b5ccb278c | -3.92678 | -42.40261 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3df6425-e5f7-319d-87db-02e2aae48425 | -3.92632 | -42.43348 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77e34dc5-13a8-3f05-8d5f-ed85e6b51072 | -3.92608 | -42.40691 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3009110e-10c5-34bb-8cac-8dbb066d98de | -3.92539 | -42.41121 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47e805d8-83b7-3361-b639-41f78a1c408e | -3.92469 | -42.41551 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 42db55ae-62d3-367a-ae19-3c85530e1306 | -3.92399 | -42.41982 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4220d5cb-8a2b-3162-9c01-dde76a7c5268 | -3.92329 | -42.42412 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c877354c-98aa-3fe2-93a8-453f8575b389 | -3.92306 | -42.39757 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b183721-141c-3c1f-8ec4-a45510931c7c | -3.9226 | -42.42843 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4e22b27-4773-3830-8773-9bd28db09dec | -3.92237 | -42.40187 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b4867526-1757-31c1-8607-550c8669fa75 | -3.9219 | -42.43274 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab7f0f10-349f-34b7-9d73-aceea84f4822 | -3.92167 | -42.40617 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| bd05f2b7-cb50-33e0-8137-ddc615d6f003 | -3.92097 | -42.41047 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b58eb9bc-59ef-3203-b266-50c217bbedb6 | -3.92027 | -42.41478 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e72b9487-4189-3f83-beb3-9f875c56a5c9 | -3.91957 | -42.41908 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7aaf6b48-4468-36cd-87cc-601465704277 | -3.91887 | -42.42338 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 47aefa4f-e36b-32a6-93c0-312da997db40 | -3.91865 | -42.39684 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b2330a7-557d-3c9e-bd04-c40c1f90f363 | -3.91817 | -42.42768 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 07eb4d17-449a-3da7-8b76-4274781b3f75 | -3.91795 | -42.40114 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4d6006ca-8653-3e77-9831-7ac7d1eaf5c0 | -3.91747 | -42.43199 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9fbe98b-4f40-354b-a4eb-71fd21da65b8 | -3.91725 | -42.40545 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e9f9331f-44e9-3aa0-9872-0f90c91bcff7 | -3.91677 | -42.43631 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10f1e5f6-19e1-38cd-8743-b95d49f9b79b | -3.91655 | -42.40975 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| dee821fe-a1fc-3dcc-b6b9-be29cd675da0 | -3.91585 | -42.41404 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e2e9d0cd-f174-3aad-b3b7-4046ee320300 | -3.91515 | -42.41833 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d68f6463-837d-3bf4-b956-3f1fdb7182f6 | -3.91445 | -42.42263 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 55d5dd60-246c-37e5-a50b-ae9eef4382a6 | -3.91375 | -42.42694 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f6971ca6-4c28-33dd-8011-ec696a3f9eb1 | -3.91353 | -42.40042 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b05526df-2326-3100-a456-8c8b7c594a48 | -3.91305 | -42.43125 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd4056a1-15e4-354b-9ceb-2cee20f8a6aa | -3.91283 | -42.40473 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eab75e4f-0141-3c5c-af50-a3a8fb42998e | -3.91213 | -42.40902 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0d69653f-2ba8-309a-9df6-1e23757710e4 | -3.91143 | -42.41331 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8bf1a4f2-6225-35b3-ba68-166b21845a02 | -3.91073 | -42.4176 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0cb4b857-6a77-37b3-ab3b-cbfcf833e48a | -3.91003 | -42.42189 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 37ee5c25-a28d-3d2d-84e8-e3dd529492a8 | -3.90933 | -42.4262 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d724b20b-8474-3688-be50-9fb54a99a5ff | -3.90862 | -42.43052 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5bbb384-2be6-31fe-a3ad-4b58b71ec5b0 | -3.90791 | -42.43487 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4fe17dc-093d-30cc-a6a8-405674268187 | -3.90701 | -42.41258 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d730ae1b-cbd6-3f48-9dfb-aa9424395c0b | -3.90631 | -42.41687 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 89e1939b-a215-3ced-8076-f06a0d4d1ea2 | -3.90259 | -42.41185 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a1f6404-2f30-39d2-8906-ba116e03dd2e | -3.90188 | -42.41616 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83fde3f0-9a86-35a1-bdfe-c81a355a969d | -3.90118 | -42.42046 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca1a58fe-d152-34b5-bbbd-957c8e602a89 | -3.66134 | -42.26524 | 2024-10-17 03:47:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ec6e233-3a52-39f4-930c-88bac6d1cfaf | -5.07636 | -42.56679 | 2024-10-17 03:47:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d18b0c0-16bd-3c3b-8f2c-2c1463c39492 | -5.07199 | -42.566 | 2024-10-17 03:47:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f0766ec-27e2-3c4d-bd21-67028a54ab40 | -9.29985 | -43.27224 | 2024-10-17 03:47:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 56e9a650-2727-392e-8f38-b6a32b08e234 | -9.29799 | -43.26879 | 2024-10-17 03:47:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1657cd65-f3a7-3663-97af-b4172e4a34df | -9.2973 | -43.27286 | 2024-10-17 03:47:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1f467a0-2354-3a77-99c0-eea988ca48f6 | -3.51852 | -43.23456 | 2024-10-17 03:47:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc1057b2-6add-385d-827a-4b9fe9894da9 | -3.5177 | -43.2395 | 2024-10-17 03:47:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e2d4edd-ec02-31fc-af7c-8c29abe8f71c | -5.02755 | -43.66035 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d51657d-bd7e-371b-8d5e-623219c97e37 | -5.02673 | -43.66535 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8865c5a-72c0-3f57-91be-95334111345d | -5.02307 | -43.66091 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6237a104-55e8-3d40-9c86-2a863dee1a04 | -5.02283 | -43.65952 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc59b7e2-8578-3c96-8140-cc6dd307dcbe | -5.0222 | -43.66589 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d4334d9-7d19-37e5-8e48-a3ef971a6fca | -5.02201 | -43.6645 | 2024-10-17 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bf2028d-1539-303e-a9a7-2a219a8dd0a0 | -4.13345 | -43.08798 | 2024-10-17 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ddf4361-e498-358f-87a0-b07efa8f40d3 | -4.12885 | -43.08716 | 2024-10-17 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b4c9ea5-3220-3604-aa76-3ac1c40ee6d1 | -4.12807 | -43.09194 | 2024-10-17 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 947774aa-7d5c-3839-a459-b68bd6347158 | -4.04683 | -43.23651 | 2024-10-17 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d4d274-8641-32c4-a6f3-1a7c46cec133 | -4.04602 | -43.24131 | 2024-10-17 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 645d5a29-bcb1-3f0d-a424-fc75edd0e526 | -4.04135 | -43.24051 | 2024-10-17 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7c5f8c7-71cd-3e9b-9414-e01af71f580c | -3.85849 | -43.24669 | 2024-10-17 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40d06920-2917-39a3-978a-df90355850e2 | -7.86524 | -45.34948 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4b8cef5-aed7-37dd-a8de-f49946f94d48 | -7.8647 | -45.35243 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8e6c22e7-50cd-36c6-9a15-5a48e33122eb | -7.86363 | -45.35833 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3b1ec51-82dc-3e28-a0df-ac3720dc6bf8 | -7.8631 | -45.36129 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5334db51-b293-304e-a695-deb13f9372e4 | -7.86255 | -45.36429 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65e35e29-6c7e-35a4-a58a-c72a2b414794 | -7.86034 | -45.35677 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b8d0c8-838e-3e9a-be62-f0d10a36a7b2 | -7.8593 | -45.36272 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c264d033-5fec-3429-8f20-99fdce093414 | -8.50752 | -45.45973 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ee29891-722a-3c1f-86dc-a03771647a9e | -8.50251 | -45.45867 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87a22706-6003-35d3-840c-5a6be5f25a40 | -8.19081 | -44.10981 | 2024-10-17 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7f6b52f-aa38-3f23-8169-773c6554f1a8 | -8.1883 | -44.10794 | 2024-10-17 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5486625-b5ec-3f8e-9f62-3cb3b951b68d | -8.18752 | -44.11253 | 2024-10-17 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a197c3f-f13a-3fe5-82e7-76cea2272974 | -8.18614 | -44.10929 | 2024-10-17 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a118f2c6-4333-333a-ad42-411a093ada3d | -8.18365 | -44.10732 | 2024-10-17 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5855b6af-5fb9-3bd0-ad00-ce0ced449551 | -7.86922 | -45.3563 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0d2548e-075d-30f9-b616-4b129db70ab9 | -7.86868 | -45.35927 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 312e085c-8756-3dfa-a674-abe94ceecfbe | -7.86815 | -45.36224 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d67e75fe-ed80-349c-a520-824616dd4e4a | -7.86085 | -45.35381 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54891300-5c67-3ea4-ad1d-d1a93f53ce46 | -7.87029 | -45.35041 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 15c42e55-ab42-31ce-a5f3-31b5067609a1 | -7.8676 | -45.36527 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86b968df-d069-304f-97b7-405f893f2675 | -7.8748 | -45.35431 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2fa7dd65-3479-3829-9b9f-9e99d58d2397 | -7.87427 | -45.35725 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README20.md)
