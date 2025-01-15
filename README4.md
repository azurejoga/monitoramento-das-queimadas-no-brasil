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
| b1c0dafe-82b3-3989-9d5b-115a234728cb | 4.0409 | -60.69794 | 2025-01-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5cbc80d5-db67-3ba0-99df-08ce62ad86ee | 1.93643 | -60.40864 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f322c76f-74b0-3de2-9c68-2853203cf7fa | 1.32424 | -60.03731 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb7b94f4-d1ab-32f2-afff-f9649455b69f | 1.31948 | -60.0299 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47a77d62-6cae-3e00-9075-176ae701a1de | 2.09709 | -61.81403 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea2e9b7d-7f02-38ac-8f4f-b07f13c60b6d | 2.52322 | -60.99235 | 2025-01-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 355f78a5-fb68-34cf-ab1d-53ec2a3376c0 | 1.17464 | -60.49934 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1834372b-801d-3be9-b58d-8bcdc3d0b695 | 1.17825 | -60.4988 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d56ac22-f753-3a87-a3c8-dde2a4ee4812 | 2.09395 | -61.84559 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbce5fc6-4205-3655-8d95-b06c9c351bd6 | 2.2895 | -60.21399 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fcde4ec-357a-3e38-bcd6-f5ec7c6851b2 | 1.32583 | -60.4395 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99611ef4-0077-3210-9432-71e3f8467bf0 | 2.09686 | -61.84305 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 553debbb-a712-315c-a8a8-12c2d6616d8e | 2.09232 | -61.81269 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67fa8645-c14b-342d-8b66-dcb8fef129cc | 0.45891 | -60.43812 | 2025-01-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9db76520-5452-3968-a6f3-fe48e0520b9d | 2.10005 | -61.83734 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 686e21e8-e361-3b3b-98a8-9bc1bed6c080 | -2.76846 | -54.04753 | 2025-01-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 356ccb13-832c-3fc3-8ab4-3f1671860a09 | 2.51944 | -60.99293 | 2025-01-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 05db67c0-f892-3583-bf32-bb41a2e20078 | -1.69134 | -55.68856 | 2025-01-15 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c2670a0-ce81-383a-8347-4e69a1d2e752 | 2.09627 | -61.80886 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2eac8eb4-c57b-346a-9ce7-b4a51a4287fb | 1.17335 | -60.491 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97574ddf-364e-3ec9-be55-3c2f7fbc27f1 | 0.72367 | -60.11679 | 2025-01-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 560c3cfb-9be8-383d-b38d-b6385824f35f | -2.77623 | -54.55885 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d2cb24-124a-3ae0-a01e-5ee41e946b81 | 1.01068 | -60.35504 | 2025-01-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fc7e640-3286-3b73-83d1-f10bc4a599b6 | -2.50471 | -54.12524 | 2025-01-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50c61950-e6ef-349a-ac79-9bbb179a9d00 | 2.10082 | -61.84241 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 710e6f04-ee7e-336e-9493-455153633d56 | 1.32301 | -60.02935 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bec8f658-903a-35d3-b18f-65fd1bd3f40e | 1.34836 | -60.02956 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0d9f88a-77c4-317f-8c2d-f364b283cc0c | 1.32777 | -60.03675 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1170306a-0388-306c-8238-3509fa0c2ebd | 0.63589 | -59.94575 | 2025-01-15 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 164e1dc4-99d1-31c9-a19d-31c7c4ef35c5 | 1.31962 | -60.42344 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 51104979-12a8-3550-b955-234edeaede63 | 1.32353 | -60.44834 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 873ffa14-2186-3b97-8c78-ff2e5b04ccc8 | 2.09238 | -61.83553 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a1df7e7-044c-3828-965e-284ec97023fe | 0.72305 | -60.11286 | 2025-01-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc02b5d1-7ed1-3cc3-b806-7e138d68c7a6 | 0.66548 | -59.59288 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43158a0e-d8f3-3391-a1f7-dc5f370c3303 | 0.72658 | -60.1123 | 2025-01-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 465e353b-87e9-3979-94fa-31c17384e245 | 1.01041 | -60.40125 | 2025-01-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8290aa30-f3b7-3f7a-8f42-ebaa9058cd5a | 2.10097 | -61.81652 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bce9ac62-a919-30ab-a4dc-c2227db3b8e5 | -2.85961 | -52.7919 | 2025-01-15 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b909cc-0ff8-3552-9e07-2ffae1ea8f5e | 1.32518 | -60.43534 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 164be089-cb47-3bbe-a770-d65c3a13b3a7 | -2.77991 | -54.55943 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf84dc49-33b2-3d9e-b816-0227ecd012d9 | 0.96348 | -59.47523 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2702f39-c5ba-3fca-af86-f0ed894c9c4f | 1.32222 | -60.44003 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60f5acf4-1d54-3d4b-bfcc-379ae6f38236 | -3.02609 | -54.5925 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad13cb3-9360-3201-90f5-07e0785ebaa3 | 2.09789 | -61.81914 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0e4501c-de1d-3d22-a68f-b3f07461b56b | 2.1002 | -61.81136 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2dea97de-cc1c-3624-988a-eda66fe34afc | 1.32071 | -60.03788 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37a67cf0-653c-3f07-aaaf-434581e143d4 | 2.28652 | -60.21865 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| c690ed3b-1ab4-351f-82fc-492204e52d22 | 0.71124 | -59.229 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff01d83b-6581-325c-a348-d631fb9c785f | 1.90154 | -60.57023 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6be7fade-4347-3b65-b542-ec72312b3871 | 0.7272 | -60.11625 | 2025-01-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a009586e-bb46-3b98-89f7-64fb16fd7468 | 0.96692 | -59.4747 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d1b9e8a-52de-3f8f-b91c-57a85cb7c336 | 2.10106 | -61.83927 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0ed484b7-496d-3c27-a2bd-cf0d4ec30ad4 | -3.1629 | -54.63008 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 146ab3d4-b108-3068-88d6-627d0022d779 | 2.09762 | -61.84811 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2b38047-bbd7-30c8-9c02-fda74647ead5 | 2.08896 | -61.84435 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9cbc248d-16be-3eae-a84b-9bb35ad3d99e | 1.17761 | -60.49463 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1963d69-d7ca-3e71-8d29-7fe629c68770 | -1.55449 | -54.4407 | 2025-01-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 529dbb12-a445-3b88-a2dd-c8b98ce0916c | 2.10027 | -61.83427 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6413e8eb-4cb4-3bb9-8977-605fdca99f51 | 1.3519 | -60.02905 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d2effda-5466-3197-a99e-3b6321efaaca | 2.28292 | -60.21922 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 34e83590-c908-38cb-a330-4a8aa65d5194 | 2.3438 | -60.23127 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9736dce3-7e50-3836-8de5-261209b9878d | -3.68947 | -53.42634 | 2025-01-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c61f921-d3ff-32eb-b255-1436ab7dc35d | 2.09235 | -61.8096 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cedd9f6a-a6c5-3f52-9027-029e34702538 | 2.10492 | -61.8159 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| cce85df8-9176-39bc-9632-506c8bbfe67c | 1.17632 | -60.4863 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43e2a8ea-b8ff-3e10-8488-bc102374c394 | 2.20782 | -60.24608 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdeb592e-a41e-3b8c-8880-67df18fc3c3b | 2.09711 | -61.83993 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c3898155-2c8d-3e70-a008-a5943a88fbd9 | 1.18057 | -60.48992 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce79c6a-c50c-333f-bfdc-bd80e4a226ef | 1.32009 | -60.03389 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46b1bba0-f7d3-3b02-b11f-57d61bad175d | 2.28229 | -60.21507 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 1f550045-cf9c-33a9-b9ee-0502357372bb | 1.17271 | -60.48684 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9224e8f9-780f-3bba-82fa-83e28492b39a | 0.64048 | -59.92917 | 2025-01-15 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba760275-0a31-37f8-a922-de56d644c498 | 2.08821 | -61.83929 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db3bf7cb-2601-32a1-af1e-150983a3ebe1 | 1.17696 | -60.49046 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad8e5ac1-2931-3dfc-843d-3b6bc651fef8 | 2.10569 | -61.82104 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a2c56692-e101-3a35-9ef7-927a90d2e16a | 1.01605 | -59.56713 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4f32c47-3bde-3b6c-bb2e-761de45f28ff | 2.1104 | -61.82545 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| abe425aa-7e97-38f6-a216-69a83f82b1da | 1.17528 | -60.5035 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3daed50e-071a-32b8-91e4-7cc61d703909 | 2.09394 | -61.81974 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7749e051-6a46-3551-8a0b-2ac14530be41 | 2.09315 | -61.81467 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4fda04b4-631f-3333-b8de-d0c299da43f7 | -2.83502 | -54.54517 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3a0d15b-3236-3817-b6e9-e6bef9b630ce | 1.12447 | -59.42781 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47318a12-0f51-3114-b748-709da481f411 | 2.21145 | -60.24569 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76f8e299-8c6b-3b7c-bb7e-fca905030a05 | 1.90109 | -60.56883 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71ce2dce-d259-3236-b813-4f50be73d1da | 0.96652 | -59.47449 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c378f37-6259-3957-859e-b6decc8f05ca | -3.16167 | -54.63208 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0f9f82c-2b4c-3b40-9c45-fbacc126f9cf | -2.77689 | -54.55448 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be57df96-83d7-31b8-a78e-7dc1a4adcd8c | 2.09317 | -61.84057 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d505f30-1076-3b34-9269-f1464c786972 | 2.09308 | -61.81777 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f20535b9-560b-35d1-91de-454fbe32c3a4 | -1.55474 | -54.43881 | 2025-01-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6e51f53-8365-3b56-b155-92b8efbb5a59 | 0.50651 | -59.33905 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aa0cb1e-3995-369f-a44c-27679f94cfde | -2.8732 | -53.97033 | 2025-01-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8adafe9e-fbcd-3774-a000-7a05a041504a | -1.6925 | -55.68575 | 2025-01-15 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5a00c87-1626-37ea-984b-2fa99bf6c270 | 1.32288 | -60.44418 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9696483-d9e3-3719-88aa-8438f368d335 | 0.79494 | -59.65877 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e942940c-fe97-392e-b9fc-395716d85ed0 | 1.04418 | -59.54351 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40885f06-26f3-3711-9687-32f863f29e57 | 2.52391 | -60.99694 | 2025-01-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c6e06fb-643f-35ba-a4d3-69f8f2631034 | 2.09216 | -61.83865 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65094090-7ae6-34ce-82f7-e849c8926137 | 2.28589 | -60.21453 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 2c00e3f7-f20c-3e96-999f-2f6dc9318db6 | 2.0979 | -61.84497 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README5.md)
