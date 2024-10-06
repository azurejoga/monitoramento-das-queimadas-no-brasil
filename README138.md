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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5c54e77-0f33-3725-a536-d1f66e242182 | -8.83237 | -63.031 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aea242b-8993-38c8-83bc-6495d1080fe0 | -8.80501 | -63.07434 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2eccdeb-826a-3b7f-a638-a65599009d22 | -8.79196 | -63.22541 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05b8155e-e2c3-30e3-a785-7b07b17aa09f | -8.78861 | -63.22489 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 295c614a-6d0b-3f70-b312-f40d8fe1d606 | -8.78806 | -63.22844 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfb5a538-5648-3412-897f-c9f28178294c | -8.78526 | -63.22436 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 084dde05-f706-3d8b-8bb0-70d013a26cc2 | -8.78471 | -63.22791 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f279bc40-1331-30f5-bc13-c4e6506c2707 | -8.58211 | -63.09485 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d3043d-ab83-3158-bce7-7e5848be77b6 | -8.58155 | -63.09841 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf1eb7c-a65d-3d1c-a9d6-5a0b59723393 | -8.57875 | -63.09432 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34331deb-082a-3593-a718-d88660af4c83 | -8.5782 | -63.09788 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba02b310-8149-3098-a7bd-99c18be93509 | -8.50523 | -64.01811 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1111ce-0543-3576-b4be-055c7c8ae3cb | -8.50469 | -64.02161 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a50d559-d740-37bd-85b9-8a1dc47568b0 | -8.48917 | -64.06214 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19e3414b-d8d2-3d7b-8695-2fe64a523867 | -8.48862 | -64.06563 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f830d868-dc21-34cc-9bfe-01a3edc08353 | -8.4853 | -64.0651 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 825f80e5-6afe-3201-ba6c-4deaee254c08 | -8.48198 | -64.06458 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1029c423-7b0b-3aa7-b965-27a6f468133a | -8.33734 | -64.01303 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4286878a-29c7-3134-8dd9-19b0733b3192 | -8.3224 | -64.02138 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76e83f23-cd68-3ede-a32c-c497f455fbe4 | -8.31521 | -64.02381 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95db2732-9e41-3d65-8b9c-9f308012c4c3 | -8.31188 | -64.02328 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8cbfc04-76b0-3698-a037-b494f0923217 | -8.26643 | -64.03712 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76a1d8b6-2679-360f-8e17-835537e7ec80 | -8.2631 | -64.0366 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4436df00-9cc2-3b6d-8620-4cc2d3915995 | -8.33402 | -64.0125 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d125d60-fd8e-3205-8753-346b6229082b | -8.33292 | -64.01948 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5628587-b8ff-34a6-a3c8-6fd3151bc126 | -8.3296 | -64.01894 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043ab60b-41e8-396d-8607-0a57274ce1ac | -8.31908 | -64.02085 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f494d68-5bf3-300c-b46d-ad83fc977e39 | -8.31853 | -64.02434 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3aa7e347-937d-3549-9425-eca19607ee5f | -8.31575 | -64.02032 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6882556-df75-3ae2-a2e4-278751881fa9 | -7.51246 | -64.67735 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cf3c087-4c71-3e66-a7e5-9562a819d6fa | -7.37813 | -64.66686 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12703d55-f5b3-3d7c-bdde-739d53519cee | -7.37422 | -64.66985 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 483d02d5-ed99-334e-8ad6-b0e9d11cd80d | -7.372 | -64.66227 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2448806c-e221-3a03-aca8-d7d5cdf2ffd0 | -7.37144 | -64.66579 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f6dde87-2579-3307-a8d8-33a41eb48db3 | -7.37088 | -64.66933 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65b47dc2-64e7-3820-be99-73cf5f693fc7 | -7.37032 | -64.67284 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7af230ae-e521-308c-a8aa-08bca0e59ec0 | -7.35412 | -64.68836 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04328695-39c1-3cc6-95d1-cf0f8f302fb5 | -7.37535 | -64.6628 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71531002-f04b-3dc6-a382-332bca9fceb5 | -7.37478 | -64.66633 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eb3890a-5312-3b24-a8ea-bacadf756a56 | -7.37366 | -64.67339 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50db219f-adbb-366a-a83e-cd05706d0768 | -7.3681 | -64.66526 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38d15919-688c-34f8-bfd5-88ebd53fafcc | -7.32961 | -64.66996 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f18c56e5-35e3-3b26-8d6e-0b060da048f4 | -7.29443 | -64.66466 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb2f2374-c678-36bb-9634-b97b25547769 | -7.29164 | -64.66059 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e5f4ff-21d8-34a8-857a-ed10839beabf | -6.82068 | -64.32291 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9763edee-4185-3728-a50d-6b91e4ee9552 | -6.81735 | -64.32239 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abc38d7c-c72b-3a92-9d15-a0cb70dd5582 | -6.81679 | -64.32588 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6891a6bf-32db-3468-8728-cd638d64b36b | -6.81401 | -64.32185 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d170ced8-9372-3a3e-b4f9-6b85e2918ab6 | -8.65855 | -64.29625 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7257cd00-7461-3996-aa88-2f82cf1d9641 | -8.65577 | -64.29223 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73be0321-9ceb-321f-b6f3-26b46f9b2678 | -8.65522 | -64.29572 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3ff79fc-cebf-3086-af98-65ba2a7c1280 | -8.65467 | -64.29921 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a414fa4-dedc-3a70-be69-0a45545cd0e8 | -7.47038 | -72.68741 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81f0496f-db75-3b46-9a16-968557695801 | -7.46575 | -72.68307 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c0afb70-b19e-37f3-afd2-6b4538d0978f | -7.4652 | -72.68624 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03e14af0-af87-3dd3-a5a7-862326ecf715 | -7.46464 | -72.68941 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c98cd77a-1885-3007-86e7-49c7046563f2 | -7.46 | -72.6852 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 021f9be7-a3b0-33d2-a12e-a97d9b589b53 | -7.35066 | -72.90267 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c25c917-df1d-3cf2-95ca-00d09ab36e53 | -7.34535 | -72.90176 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 031b7902-03a3-3e71-ab09-b5e765c64c64 | -18.88422 | -57.69202 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 18b0fbbf-85de-3e0a-bee8-9ac1993c76ac | -18.8804 | -57.72653 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d891ceda-87f0-38fc-a544-803806d40e5d | -18.87909 | -57.6914 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 00198f9c-ecd2-3b5f-8757-ab02109ac334 | -18.71939 | -57.35888 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4a29d8b7-6948-3c53-b25b-c8ea632ef776 | -18.71903 | -57.36217 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 90f01be5-13e7-3e4e-a314-0c9bd9a7f2c7 | -18.7138 | -57.36153 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5452de82-35ff-3e97-8e30-0715f31d15e2 | -18.65523 | -57.26365 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d608747f-ec3c-3ddc-91f7-4de1fd82898a | -18.65108 | -57.26217 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 10a45224-b4f6-3a4e-b90c-309fbb47039d | -18.65071 | -57.2655 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| b5d6503c-55cb-3ede-bd07-ce1bf0aec6e3 | -18.65033 | -57.26882 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 538a9282-3147-340b-b975-2ccab4bdc956 | -18.64997 | -57.263 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 5e496c0f-eb10-3502-a91f-010b895c3c3d | -18.64962 | -57.26633 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 4aed1aad-a194-3315-bedb-8e154bae1984 | -18.64927 | -57.26967 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 84c035d7-6c89-35b5-abc2-10544515f464 | -18.64508 | -57.26818 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 99717496-e859-348f-a0bb-19361f78bfcc | -18.64471 | -57.27151 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 78fea30c-e069-30d8-acad-629884c0a990 | -18.64401 | -57.26902 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 6849b7c8-ecbb-3b89-a9bc-17b779008707 | -18.64367 | -57.27235 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 385934d8-cca7-3a7a-afa3-42a777797ef8 | -18.63945 | -57.27089 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 0a703155-8583-338f-8e7c-91bff4d889d5 | -18.63908 | -57.27421 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 1d46bc8e-df3f-3ab5-91df-90480dd73940 | -18.63871 | -57.27754 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d30ad2c8-d0b4-3aa3-9c9c-7d940880cbda | -19.69584 | -56.49012 | 2024-10-06 05:38:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 15997422-d4db-383f-856b-5996de8fd1d5 | -19.69546 | -56.494 | 2024-10-06 05:38:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6b98a4df-a867-3c9e-81fa-f022e5db53be | -19.5825 | -56.5297 | 2024-10-06 05:38:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ab827624-67b1-3f27-abe0-daf52f6ba64b | -19.14203 | -57.51544 | 2024-10-06 05:38:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6c809b0a-10b9-32c8-bab1-905b6742291f | -19.13651 | -57.51763 | 2024-10-06 05:38:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8f3c590e-1e7c-3f98-8456-499afbe4eba9 | -17.84948 | -57.684 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 23d8a131-6784-3f3d-bf30-227958c6f40d | -17.84888 | -57.67815 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bb2c5803-2242-3e18-ac8a-0bf6883ae580 | -17.84823 | -57.68417 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5ee9d883-87dc-33d8-8d08-79638f949ff8 | -17.84758 | -57.69022 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 99f0e5f0-f4bc-3f73-ba36-c87d0c187086 | -17.8451 | -57.67741 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 657dc5c8-a517-3b8a-8a8b-27b5ae5e5399 | -17.84441 | -57.6834 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9d268f46-acf5-38ed-bdc1-990b7cbbd77c | -17.84372 | -57.68943 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fe9f7e5b-3ed3-39c0-b240-3c4f39a297cd | -17.83935 | -57.68279 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5651dc62-a6ad-34cc-ab78-c8f3d5621118 | -18.89027 | -54.54229 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f69ceb26-01e9-3630-8a61-446b12344d16 | -18.88987 | -54.54659 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4533b09c-bf76-3195-bd15-bb5ed76e4d2e | -18.87744 | -54.54431 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c561cdad-310a-3956-a20a-52bc0b3898b7 | -18.877 | -54.549 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15201845-4aa6-3c0a-9957-70c4f8596753 | -18.87114 | -54.54409 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa3238ee-3336-3020-bea9-ba647b1390de | -18.87074 | -54.54838 | 2024-10-06 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 071979cb-0857-3974-a065-65509d4efcd7 | -20.78185 | -54.82457 | 2024-10-06 05:38:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 804588e8-5861-3dc1-b546-05a9de60a9e4 | -20.78143 | -54.82922 | 2024-10-06 05:38:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README139.md)
