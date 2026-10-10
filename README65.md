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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d3e409-06ec-3da9-aaaf-8622ba81ef42 | -4.0948 | -54.01764 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd3ba042-fd84-3039-94ac-9dec5c09cc11 | -3.3189 | -54.04177 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f76d73e-11d3-383c-af1c-304d95d1dded | -3.87808 | -52.25853 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8e3ff47-2ce9-3052-9817-f270e9c6b194 | -2.81896 | -51.95591 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc451503-4ed3-3e8b-a470-8d2c82fb29e0 | -1.04764 | -47.55218 | 2026-10-10 04:44:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b71095d5-83fb-39b8-90c2-0896e85cb12f | -2.39814 | -51.3079 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8747b758-1fd2-389a-9c4e-0afd5c31f2c0 | -3.11211 | -51.03078 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 787af144-d7e2-33ec-a471-1043a4e0359d | -3.43799 | -54.53843 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0315e61b-a70f-38eb-bf3d-787482788545 | -2.39025 | -57.89643 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e467d5b-d68d-3d83-8743-b3ab879c0526 | -1.64278 | -54.40458 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a94f474-4f8d-3082-b141-ab9898d2adce | -2.98618 | -54.76337 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54a60c77-feb7-37ef-939e-ee06d1eb9fcd | 1.73403 | -55.57276 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce6a052-c083-3929-a4ba-b6543aa42def | -2.46941 | -56.0599 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a39556f-3548-30b1-9ec0-dc6516cfc822 | -3.26611 | -50.38649 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed355591-41a1-3518-882d-a5c9109e20d2 | -3.34829 | -50.47669 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36322c2c-ed2e-3583-9d18-19478b6d2a30 | -4.8179 | -56.08512 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c4e1815-85cf-32da-8529-5b7f5312ac6e | -4.99831 | -45.77075 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d9bb5e2-ecca-3e1d-a7a8-c7e5538ac67a | -3.17588 | -50.59345 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1b90ce-285b-31ec-8678-f4904469db96 | -1.74247 | -47.16749 | 2026-10-10 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ea7c0cc-ff52-397a-91c9-93aea189ea52 | -6.06674 | -44.6718 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee45191d-04d6-369a-bb0e-90017583a5c6 | -3.25857 | -50.43354 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc848847-2acf-3e5a-819d-1e53974a264a | -3.12212 | -54.17446 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e23c4dd-95b1-3e93-a80c-a17e7edca491 | -2.73577 | -51.5458 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460f3524-41b9-3e7c-ad92-79a5e9550802 | -2.57717 | -48.24985 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c5b8374-3863-379b-9f0f-8e39793a784a | -3.49469 | -54.19446 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91f1abf0-4898-3128-ab73-2262a453352d | -4.41251 | -49.77909 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4fd52e9-e623-3142-a6b0-cc70d63a659a | -7.06221 | -40.95346 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e03a9071-218e-3de0-856c-3413dccbdaeb | -3.50187 | -49.58797 | 2026-10-10 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf6d84be-73fa-3d76-9612-7c246193afeb | -3.28552 | -53.872 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 011ede84-2d9e-30d7-9344-c70d3b76c999 | -2.7358 | -54.14165 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c973473b-300f-332d-b320-dfb971c25cab | -5.59592 | -47.27199 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e851fe13-71b7-35ca-a730-df60950c9b83 | -3.25028 | -54.02562 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db239984-2a9d-3f23-9650-7825ebf6a80d | -3.58338 | -54.72008 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 832fb2aa-fc98-357d-94fc-e49ad93bafc5 | -6.05844 | -44.65356 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a588e0e2-c26f-3bf8-a36b-0f1beebccea2 | -4.82362 | -56.08301 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8f29321-412c-3b6f-bab9-72f19f8a2191 | 0.47413 | -50.79159 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 04e6577a-31f3-38fd-8a07-437d4a3ba047 | -6.83081 | -44.881 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 786e5990-5ea6-3918-9e88-90f4692ff413 | -5.41624 | -48.16566 | 2026-10-10 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7338075b-30b3-3d82-9adc-8c79f4ef81a6 | -3.74073 | -58.50274 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2e177741-5f33-3ef2-a7d9-7c9a5442acad | -3.363 | -50.47906 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb5c6974-c7ad-306d-858e-5cf2e21672af | -3.16176 | -50.58668 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 738aac4f-7e5f-3ac4-a95b-0ab7453f3463 | -3.98904 | -54.45769 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 307947b9-6e89-3d7b-af34-a6c70ac508ca | 0.36419 | -50.94753 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f39a4eae-6bb0-356d-83a5-89e87f592f81 | -5.89287 | -43.4075 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 058b0490-5a87-388b-ac36-626947e65ba2 | -3.24962 | -50.41887 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d3dfff3-a97b-35fc-bc06-9cc1aef16cb3 | -2.56228 | -57.42234 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8235c97b-a1f8-31ce-acc4-de71b85ceb50 | -3.20522 | -50.55338 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5757adb-7425-3a79-a210-f5f77fc6c5ee | -6.4183 | -44.07605 | 2026-10-10 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09592c7f-a1ef-3007-92a4-8a1fc2dfb8d7 | -5.04402 | -49.35098 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05dde884-aadb-3f4b-b37b-1e684c273317 | -2.50408 | -56.0642 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b073e43a-7999-3101-9a4a-a215e4426d88 | -3.25628 | -50.42436 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 586080f3-8589-3340-8562-4a4e9892d08b | -1.56087 | -51.69893 | 2026-10-10 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48a91b8c-b0d8-38e8-8dcb-679ba490245d | -6.49716 | -44.36255 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c8075e4-7853-3c39-9944-33cbf81434c3 | -3.40253 | -54.18691 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d2227cb-e14f-38e4-9937-c4476a48695e | -5.69654 | -49.05086 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 029d0f1b-3230-38b5-b5ee-bd610eb8c995 | -3.90222 | -55.81549 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df8d1637-4b6c-33f3-bf48-4c00c7846d02 | -3.86804 | -55.9851 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c99ca9b-a1ac-3b9d-88f9-0cedafcb1031 | -3.26166 | -54.18648 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a72567bc-8678-3cc5-8191-d6fcc26436a6 | -3.53936 | -54.74527 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2b397062-94c9-369f-b9a0-263a316e7fce | -6.21005 | -45.42784 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fed41159-db84-3740-ac11-f9479b337098 | -3.26176 | -50.39017 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eecf6f2-7e36-3cac-9c6b-21f954c9c583 | -3.15805 | -50.58609 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9e78d62-2a05-3a42-b538-e64eb24d4cab | -3.90714 | -58.94762 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adc9f7de-a8c7-3267-bd45-f8beaa56a0ce | -2.56952 | -57.41501 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ceb2aa49-5515-3db6-b7fd-32daadf993d1 | -1.28144 | -55.7517 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6f01d70-c46b-32f4-9b4b-60fe10112d8c | -1.87865 | -54.68972 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f75912dd-63bd-3a7c-ab1a-10835976aa5b | -3.41909 | -48.33762 | 2026-10-10 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a906b9df-ea12-386f-ba82-f1f602419a59 | -4.12028 | -54.03433 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 988ddf6d-1036-316c-96cb-3942bbd01623 | -2.7311 | -54.14087 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 925595bf-96b2-3c93-8c1c-b56abb095c27 | -3.60971 | -49.5014 | 2026-10-10 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e38531-b6b7-3f55-8710-0e5d1affd9de | -3.87792 | -55.99031 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f946511a-9cda-317d-aa3a-7a649a0eae3f | -6.87428 | -45.04065 | 2026-10-10 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 611de58c-0a43-3227-870c-a0f22b6af410 | -2.39118 | -57.89451 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b254a7f-4509-3500-adfd-49a1ebd25211 | -4.51661 | -54.89779 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ba8ffdf-d4b3-3c5d-bf67-31d416d68d85 | -5.60038 | -47.28691 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb38c8da-5c18-30fa-94c9-c528b34f6721 | -2.481 | -56.16888 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ce21990-f84b-3531-ac28-83f9ee7965c5 | -3.84266 | -55.78999 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa86ba0c-fe8c-378e-872a-f6995d1cd5c5 | 0.47807 | -50.79097 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5eb3be06-cac6-3ab7-84cc-1882f339943d | -2.84009 | -49.88388 | 2026-10-10 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4087b258-ec06-30bf-95ca-753fb0abc10d | -3.28095 | -53.87125 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be156ac5-6874-3b1b-8f81-5918cedebe45 | -1.10982 | -54.16459 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7cbe0e1-b329-38fc-bd42-e1b27d13ba91 | 0.47018 | -50.79222 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e8cee6-b134-3bdd-a519-c54c992f6b4b | -3.91227 | -55.82239 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c6c89a1-6826-37dc-8519-cd4f6f3beb56 | -3.87683 | -55.84012 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1b20bef-0c46-3203-a066-a22e785f093d | -3.22337 | -49.43473 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 79d380b8-1305-3836-a313-a3a337f8f0c0 | -1.9246 | -57.04292 | 2026-10-10 04:44:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a38d7d51-5406-3658-b433-4b442d58eac6 | -3.1011 | -53.94169 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad5665c0-b623-3d14-8227-66927c77948e | -4.40963 | -49.77463 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac21e6e1-dc48-3f21-8e54-87267f9cd229 | -5.88445 | -43.411 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f913d760-9779-3785-82b9-a2c563d7152a | -7.08296 | -43.93557 | 2026-10-10 04:44:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c53d0f77-306f-3c2c-95b1-42b0ac7250c6 | -1.18857 | -55.66292 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5caaafc3-1b40-37e0-bbd3-ccd07b81f40a | -7.22771 | -44.17634 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c48b8212-8179-30e1-b519-0163e6f82562 | -3.21987 | -49.43416 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ce0bcc5c-9376-3ea9-980c-ddc765570485 | -1.20405 | -54.21381 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3a19c97-9829-3119-a826-73f6ae5328d4 | -3.1083 | -51.03019 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d9554f0-44a4-3978-98a6-5158a3f30d63 | -3.87382 | -55.98283 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 613464d7-2e72-364f-a5b9-02275955cf1a | -5.74439 | -45.13021 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 870f3f99-52b2-3cca-a101-8701c5bd61c0 | -3.28009 | -50.39311 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 661fa524-ef7a-3e36-b48f-e6a66022d51a | -1.15305 | -54.22144 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60b3ac1f-8a5a-3aeb-989b-4bf02410b7fe | -4.72423 | -55.65965 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README66.md)
