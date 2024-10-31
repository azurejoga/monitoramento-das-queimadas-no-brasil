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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 453e981e-fc62-3912-9d9b-28e35f4fd7d1 | -4.53256 | -45.97829 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f42a3f06-2955-3fde-b7f8-91b69d799056 | -4.52979 | -45.97432 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea11f4a8-6b3d-32f3-8796-7589d423eba2 | -4.52924 | -45.97778 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f41cfae8-6627-3ff1-bea2-c2ca5fa3730e | -1.94395 | -47.03702 | 2024-10-31 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b6adbc-a397-3d08-8095-cc2af45b568f | -1.78545 | -46.91006 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1a1adcd-4696-3792-949d-22effb8cb6ad | -1.78486 | -46.91373 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5b7a006-c8fd-34a0-8319-9f0b6191ca29 | -1.73612 | -46.71614 | 2024-10-31 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4635971f-2a9e-31ed-bdb2-0c766094d436 | -1.60289 | -47.14086 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4f8950d6-b106-3e29-9caf-8316572c3566 | -1.59944 | -47.14033 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86c176e4-12c9-3c42-84cc-7b438d3d325d | -1.59599 | -47.1398 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 927659f2-b58a-3d5e-8d9d-5bbd1f9f0fcc | -1.32487 | -46.60081 | 2024-10-31 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78a1137c-12b7-3531-9a58-ae730e14eb61 | -1.25349 | -46.60849 | 2024-10-31 04:23:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4da4f706-f1d7-3390-846d-3edb25ace39b | -1.25009 | -46.60796 | 2024-10-31 04:23:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e03822e4-11b9-3719-ba13-19470d7ff3ba | -2.3532 | -46.49905 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 43e4b1c9-3a91-3579-8f8b-4989f1355f20 | -2.34309 | -46.4756 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40dbaea2-611f-30bd-a556-4b5719d4c715 | -2.33917 | -46.47863 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8806b419-cb79-3745-8df3-bfa4847b9890 | -2.33807 | -46.59524 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99cc6cd0-ee89-3f45-8037-ae9bdf0de95f | -2.33692 | -46.471 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c91f4d0a-32dd-3760-875b-e345efa34f24 | -2.33526 | -46.61311 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d840cf-8cb6-3798-8f96-01ffdc277752 | -2.32178 | -46.50138 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b1744e-353d-31fc-a06a-381582982892 | -2.29066 | -46.74223 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849d7f2a-71be-3af9-bd6d-f6adbaddf09d | -2.28784 | -46.73809 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75bd5050-c825-3b6b-9e30-db200e87459f | -2.28445 | -46.73756 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e67ca92-9859-3e36-bde1-a7667bc5a38c | -2.28388 | -46.74117 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95795eac-43c8-38b5-b8fa-e2ab83ae6066 | -2.27745 | -46.49807 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f7bb960-de40-38c2-856b-073bb5d132d5 | -2.27465 | -46.494 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9216a746-7603-3599-82de-106b59faf106 | -2.27408 | -46.49755 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ab2594-d722-32c2-9589-d6a42e16ff21 | -2.27249 | -46.79118 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c06c7174-efd0-307a-b680-929adbbf70a6 | -2.27192 | -46.79479 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d700b9f2-540e-351d-8b26-bbc818f83af4 | -2.27128 | -46.49348 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b38ecf9-6834-3ba2-b025-f8e05bc8a712 | -2.27071 | -46.49703 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50a4dec7-4920-3792-b7bc-68049ccdf05e | -2.26983 | -46.6984 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a0716ee-90b8-3b35-b889-7a81ab359acc | -2.26645 | -46.69788 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c666a171-ac7c-3a01-8ea8-eebd32f9d0fe | -2.26153 | -46.30724 | 2024-10-31 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1158059e-f5b4-389d-9cf5-e33c6809f880 | -2.23203 | -46.69617 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1fba22d-1bc2-3130-a40b-f99520dd9b9a | -2.23145 | -46.69978 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd8a929e-ad73-371e-83fb-9f04b98f47dd | -2.22806 | -46.69925 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1d329e-af79-3438-8bcc-093b805a0e19 | -2.22804 | -46.69596 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b1df873-dc34-3923-80d5-618d13a6af07 | -2.22748 | -46.69957 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce43351b-fbbe-37fa-a4a0-5f06adcb86bb | -2.21455 | -46.51776 | 2024-10-31 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95f264e5-e836-3f86-82db-6a9248d00f83 | -3.30352 | -46.19701 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70145234-f9ed-3912-a17a-1aaa1d125b73 | -2.93083 | -46.77932 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dcc83f9-6e7f-30fe-8688-e15ef8d4bab3 | -2.92745 | -46.77879 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57568b25-68e1-31c2-93eb-bc224c887163 | -2.84409 | -46.68844 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 619dd1e5-65f5-3dca-b256-4e171ac7fc9c | -2.84353 | -46.69201 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 789d0683-831e-313f-9720-1d1ca4559570 | -2.84128 | -46.68434 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96c65aff-1151-3c64-8524-f4b86db58faa | -2.84072 | -46.68791 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02850ccc-b489-3b98-bb44-d07a26086de9 | -2.84015 | -46.69149 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab2a3c2e-1084-3f82-a893-387c0a7115df | -2.83959 | -46.69506 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8735b1ea-e0f9-3646-81de-6be98bc9b478 | -2.83735 | -46.68738 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f514818-f875-3712-8105-396b4b4b58ca | -2.83678 | -46.69096 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f249f65f-d932-3abf-b9bd-46ba7463d158 | -2.83622 | -46.69454 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1498076-2867-380a-b307-5c72f5f61e1e | -2.705 | -46.04646 | 2024-10-31 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76438d5e-9f98-3646-9370-559fe9c78650 | -2.56588 | -46.11044 | 2024-10-31 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74725caf-fade-3e54-a1e9-65a28f2edfb2 | -2.5495 | -47.36173 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ec4f9d2-71a3-31e3-b9ac-2ce2ae3ca69f | -2.45302 | -46.90849 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ef8be5e-fb1d-3a8e-9c78-3a0f8736b135 | -2.44963 | -46.90793 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93ac8d8-8ae4-3947-807f-e9df33592bf0 | -2.44904 | -46.91158 | 2024-10-31 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c283be4-572d-31c6-aeea-add89677b881 | -2.42588 | -46.7043 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39c707ee-2228-335f-b43d-4990e6df6bbc | -2.4225 | -46.70376 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd5e44ad-1c59-3cc0-8700-0397b8a52b5c | -2.42193 | -46.70736 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9bf871-803b-357d-a575-1b31dfb0ac5d | -2.41968 | -46.69963 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 992fba2c-88b0-3dcc-b675-7cc9f3cc9077 | -2.41911 | -46.70322 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5a08c3-9592-37c7-877e-c77ebdd43701 | -2.41855 | -46.70682 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc5398e2-a174-3e57-a223-2e39090df02f | -2.4163 | -46.6991 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b5bd668-9911-3743-b14d-3b610e93ffe4 | -2.4146 | -46.70988 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b1e3e67-b4a7-3de7-8acc-7ebf2de1b080 | -2.41292 | -46.69856 | 2024-10-31 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3de99d48-bacb-38ca-b2bd-1c1104817470 | -2.61089 | -47.34376 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e75af3f9-3e51-3b7c-a8d7-3f8086c5fb44 | -2.52781 | -47.32001 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55ac6f78-5715-3815-ab60-22fa32a57fdb | -2.48269 | -47.27083 | 2024-10-31 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f6e224-57e5-3cba-8b9a-78ad8d8df0f7 | -4.50069 | -47.10111 | 2024-10-31 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c4e6370-e927-3e36-a717-524d22148c18 | -4.35075 | -47.31799 | 2024-10-31 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf1c153-2cf4-3b9a-a6ab-a9d6c9611961 | -4.13382 | -47.12435 | 2024-10-31 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3cb11a-232c-3be3-a870-31d13d2dd91f | -4.13044 | -47.12379 | 2024-10-31 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e670a73-a02f-33db-9746-0c2dcfd30304 | -4.62155 | -46.51165 | 2024-10-31 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8591fc-d2e4-38f4-8389-50fc6b333748 | -4.53984 | -46.57401 | 2024-10-31 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246cc680-bc92-3f9d-9f2d-2207a66a405b | -4.53929 | -46.5775 | 2024-10-31 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fddc9e47-2bb3-3f4c-832e-fffbf967bf1f | -4.5365 | -46.57348 | 2024-10-31 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3062751c-d798-3be7-84c8-2874bc10440a | -4.49845 | -46.47444 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dba02c0-932c-3fda-833b-5d5aeea62f8c | -4.4979 | -46.47794 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea50e4a0-15ad-37fb-84a9-2e55c68cd4ea | -4.49511 | -46.47393 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e887e50-0af8-334d-aa22-0849bc6ef18f | -4.46787 | -46.45173 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7a707d0-8471-37f6-8af0-9b647d0d3a45 | -4.33404 | -46.7871 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecdc00fb-3851-3c2b-9659-57fcee414f3f | -4.2168 | -46.44061 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b73ec763-4694-3770-b906-69a242d7c2ce | -4.19869 | -46.71806 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9a491f0-a0ec-3940-a505-9e7fe324fb0f | -4.1948 | -46.69938 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ea419b1-4e23-3132-8003-4e16d5e0355b | -4.19424 | -46.7029 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5956fd8-ba7d-3d2c-8c79-f66f1359b39b | -4.19367 | -46.70643 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 901e81a2-a836-36e8-997e-8a8c7738383c | -4.10277 | -46.59857 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c83ffe83-9b6d-34fb-a0ea-6193233ff709 | -4.09998 | -46.59452 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a249a41-61a0-33f8-853d-9044234b6c02 | -4.09942 | -46.59803 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91690bc-305c-3ff0-8103-958757b88d6d | -4.06411 | -46.28806 | 2024-10-31 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff1ddc11-d288-36e2-9446-1cea92bbf23f | -3.98768 | -46.43356 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62b3b0e-6cf1-3f4b-b01f-febd4ec6f97e | -3.95816 | -46.40384 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a6425f-65bb-36e1-ad73-54146e5fba5c | -3.90423 | -46.44187 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4900c1f-55d0-3d35-85be-ca6fde882351 | -3.90368 | -46.44537 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 193d567d-75eb-3e76-8fec-4c16aed3a28b | -3.8853 | -46.43833 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c3d5289-d574-3319-87c1-ebca368dedba | -3.87812 | -46.48395 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c468c41-f27f-354a-af6e-9a5d42a20710 | -3.87292 | -46.6385 | 2024-10-31 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9d37b1d-6416-37ff-af3e-3dff1e764d63 | -2.17143 | -47.95202 | 2024-10-31 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
