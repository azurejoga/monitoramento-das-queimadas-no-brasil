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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1483ce10-b2fd-3c5c-8b8b-79061166f228 | 3.11372 | -60.70819 | 2026-08-29 06:10:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4256229-0e7e-38e1-939a-c502b14f89a3 | -5.88994 | -57.75445 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b2b00a68-246d-397e-88e2-5b58c725f3de | -3.61377 | -60.5401 | 2026-08-29 06:12:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89fa5481-2467-321d-8657-1897abcfc987 | -5.88388 | -57.76433 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae35c6f6-8e21-3b39-ae45-a379d2d146d3 | -6.16266 | -57.7926 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7f67980-728e-3c47-87d7-d2450ad7737d | -5.88919 | -57.76003 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a2a1d5a-ba41-3dc1-a7ae-8f87267a1431 | -6.9439 | -58.94995 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808152e6-fe89-3eba-ac53-31721a9429f8 | -6.94264 | -58.95933 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac1fdcf5-efdc-34f5-87ea-304f7e3956d8 | -6.74972 | -58.72664 | 2026-08-29 06:12:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fa9901-1a3a-32c7-b52c-ba7006548d49 | -6.84384 | -59.94897 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e192e1d2-aee2-34a7-a7d0-45ddca9dc329 | -6.82015 | -59.94945 | 2026-08-29 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e36e63d6-9612-3bdf-8ec3-9383b1461181 | -5.89113 | -57.76039 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fa71526c-3112-3923-829d-b78e97df2742 | -6.16346 | -57.78677 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0201e6a-673a-3b29-bbb5-332bc5004511 | -6.93644 | -58.95856 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17ebd552-1414-3726-a828-f863a479e12c | -5.88782 | -57.77029 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bec136f7-9852-3527-a6ef-e77391389073 | -5.88535 | -57.75379 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c127dc05-706c-3390-ad16-5928962f2ca7 | -6.1774 | -57.78289 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88e67241-8ce0-3ed0-9743-8a0fb461037e | -6.75039 | -58.72166 | 2026-08-29 06:12:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1cf4b21-b589-3d84-ab81-03450bbf11fb | -3.20457 | -61.14299 | 2026-08-29 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 704d8dfa-ffb6-31cb-a407-bfce2754cacf | -6.93707 | -58.95386 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27b0f85-c1a4-34cb-9670-94d719b59d64 | -3.93807 | -59.32974 | 2026-08-29 06:12:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c40e202-7123-3cb8-8007-9e2e79742cc0 | -5.88461 | -57.75911 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 394242cf-853a-32b6-a8bd-90ccb220929c | -6.8877 | -59.41153 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebafa2cc-7c90-3c8b-98d6-dbbdcfa4a286 | -6.16188 | -57.79832 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60a845eb-2abe-387a-8d75-c24a477366ea | -6.17083 | -57.78194 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3ba5b14-baa1-3e37-871d-d113d9c9a029 | -6.95565 | -58.95628 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85df6036-b240-3b3e-8f03-677720dccf19 | -6.8823 | -59.40625 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56545b31-d6e4-3c9e-aec0-5f87a8449f1b | -6.94452 | -58.94533 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5228edcd-b5fb-3379-9891-8fceee1f3346 | -6.82535 | -59.95457 | 2026-08-29 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b096983-cfe6-3578-a630-1fb14a651e31 | -5.88315 | -57.76955 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5b50aaa-7554-3f59-b3c5-63c1cc16e380 | -5.89194 | -57.75456 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa679062-25c1-3131-9cf4-598e88635123 | -5.89038 | -57.76569 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 419d1003-1120-3ada-91ff-41479f475be4 | -6.94328 | -58.95456 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8393491b-a0ba-338a-9aa1-3eb3f324e203 | -5.88236 | -57.77522 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c9ccc98-0a5a-3291-8517-2278e2fbb2e9 | -6.94947 | -58.95541 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1fe3fd7-e6dd-3a82-9686-653c0b2b8cec | -5.89277 | -57.74865 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 46686dc1-04ac-3263-8689-ef449322523d | -6.82592 | -59.95045 | 2026-08-29 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59900060-3104-3872-8b09-1f2ef998bb67 | -6.15383 | -57.80824 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23b2266a-999c-3e71-8fc1-083c1afb2504 | -5.88967 | -57.77076 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae6d4d07-07c1-3461-9ca6-ec1abab51fc5 | -4.1584 | -60.69206 | 2026-08-29 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b80c4c-9e12-3353-ada2-b4cb50e3a5b1 | -6.81778 | -59.45671 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d9e561b-a7cc-3458-b1a8-84687fe48591 | -5.89855 | -57.75523 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 778bb473-1b03-343d-8328-656bbce7e163 | -5.89656 | -57.75492 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eebf9b38-218d-336d-bb77-936bf8f9f658 | -3.93748 | -59.33379 | 2026-08-29 06:12:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 954a4a04-0f96-3e05-bc2f-77da948ca5cd | -6.8444 | -59.94501 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2e5a397-0c1a-36c7-b45d-fca7b7fb7ee1 | -6.15457 | -57.80283 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc03ff2f-aaf1-36ed-a527-9bfdce03f553 | -5.99298 | -57.68766 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2c1a1d9-0b8f-383c-937a-a1cd0ca91211 | -5.88269 | -57.7586 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c751b097-02c9-3d7c-8494-44dc02bd55a6 | -5.98635 | -57.687 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf4312f4-81de-3646-8b99-2bec90082d72 | -6.15533 | -57.79724 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5610b3fc-7415-3f1a-ad1b-617d3ec97393 | -5.89572 | -57.76126 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be4068e1-f312-3a6d-93fd-56144cdb0d1a | -6.15611 | -57.79156 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd5e80d3-1e47-362b-9205-437aa3034eb3 | -6.83805 | -59.94817 | 2026-08-29 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 186c4514-b79b-33b3-94c4-a2b08cf024e0 | -6.84496 | -59.94092 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21dc573b-50a4-3e7c-a0f8-1ff8e09562bc | -5.99377 | -57.68203 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c25a269-94e0-3971-9dc6-381fe578e114 | -6.15688 | -57.7859 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bae310da-0c9e-3d85-a951-d6b03ae43d10 | -6.95009 | -58.95076 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91900f7f-f2a8-31c8-8939-4c36bef4bc83 | -5.98796 | -57.67536 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15abf53d-68a4-3060-8e52-87ad9f057276 | -4.15358 | -60.68802 | 2026-08-29 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 366f8878-2982-3441-bee8-a947e252a73a | -5.88052 | -57.77497 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34942e95-3f65-3b7c-933b-dc6785d19101 | -5.88849 | -57.76526 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6a80b12-c196-3445-b6d9-8971705ea816 | -5.98714 | -57.68129 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c1d38c4-760c-3e46-8020-cf7acf4d6ae2 | -6.93089 | -58.95296 | 2026-08-29 06:12:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f26548df-d7c3-34f9-ad81-5498b9c72d91 | -5.98555 | -57.69278 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdfd6d17-31f6-314a-8870-c80b71e5c1aa | -3.61329 | -60.54341 | 2026-08-29 06:12:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef6053a-2d65-36b8-8e06-f8ba6722e856 | -5.88128 | -57.76921 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 296f6503-ab06-31c9-b667-a8b4725c3c2a | -6.17003 | -57.78779 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5aca691e-3d8e-3d71-97b4-fbadf724623e | -5.89072 | -57.74855 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d5da2e57-3543-3b77-9611-cdd5fbfeea85 | -2.75233 | -60.23835 | 2026-08-29 06:12:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f92cf8-576f-3a8c-900a-8b58088d1045 | -5.98138 | -57.67423 | 2026-08-29 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b39ddc75-1cda-31fb-aa42-309cee40c8fb | -9.93645 | -60.43982 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d69bee5f-7892-37eb-92bb-5611073c9d8e | -8.89922 | -71.39558 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1011c5af-5694-3b05-8bfe-439aa5d65d9a | -8.34982 | -70.85133 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ca1e78a-f041-3517-8fe3-b3e95ca9a1b7 | -9.86592 | -60.3002 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461dd1af-5cf6-3bad-8866-bbc9fc258af7 | -9.99862 | -66.87001 | 2026-08-29 06:14:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79e7094b-0952-36e6-980c-6b225b05f81a | -11.02683 | -57.243 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c3d6805-d738-34fa-980b-315fa646d8a3 | -9.86731 | -65.03745 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62484ed5-9b5a-37b6-bf3e-91d86a54edb6 | -8.94785 | -62.41055 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07313b14-51ef-3350-9fd8-b9d1ecb1964b | -9.13607 | -61.01549 | 2026-08-29 06:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f33f9b3a-822a-3efd-b45e-04b28397d217 | -8.59654 | -70.2151 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21ffd09-aeae-3e2f-a6ca-284d8873a053 | -10.48448 | -64.49281 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9aeda05b-88a2-34de-b16f-503ec07082c7 | -9.93752 | -60.43143 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ef917c-01fb-3b97-8a6a-ea21f6534423 | -8.65299 | -70.75376 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cfb6c778-b5db-3fa2-9fce-5001faf4bcc3 | -9.34937 | -67.80058 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e41ff723-c811-32d9-878f-d9b9c7123328 | -8.59877 | -70.21592 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e08563-f357-3027-a780-6b70e5f7fdef | -11.04464 | -57.21614 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 039e769c-8070-3612-8ebf-8830eb962d96 | -10.46716 | -64.48572 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e538f6cb-0506-3a43-8518-ca20e09b2771 | -9.42961 | -67.41416 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07bff328-14b3-36a8-adb7-2e027eb30315 | -11.03025 | -57.21413 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 097e3875-4e72-3e18-a3c6-1d92a483233d | -9.42467 | -70.57984 | 2026-08-29 06:14:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd9cbed2-9368-3121-83b9-9c24323e0062 | -9.33808 | -68.88833 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4c4c36-a4a8-3bac-8879-73b01bf0cce8 | -9.91938 | -60.4336 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c72ee3-49d3-383c-9409-d04b52170e08 | -7.58094 | -61.33862 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab46f41b-9eeb-3cc9-961c-956c776f3f89 | -8.3781 | -70.1414 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29c47dbd-5239-357b-a0b5-3ae9a6647b8c | -8.95919 | -62.40313 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4693a8e-7747-3df4-ae9b-b8415b16a33b | -9.09461 | -65.47648 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f566747c-474c-3e0e-be36-7628e51b2b69 | -8.24895 | -70.09946 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 041d709e-7b53-3cd9-ac38-b3ef76b0ceb2 | -11.03486 | -57.25046 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1edd92c-e95c-368d-97e0-967d99066343 | -9.43263 | -67.41908 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef326bf2-a6ad-3962-99dc-5e1cfe7d3c8b | -10.47552 | -64.49149 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README69.md)
