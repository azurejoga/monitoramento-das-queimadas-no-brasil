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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb660f74-0296-3f3f-b17a-fdbf68bc096a | -5.97947 | -43.61395 | 2025-10-01 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 281412f4-c304-3427-87c7-afe0100f9a9d | -6.28516 | -43.91763 | 2025-10-01 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8c621008-f205-307e-812b-ff12a80b4a57 | -5.86045 | -43.40765 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cd9aa3c-414f-312c-9c3e-d34002e8e8f2 | -7.41382 | -45.41069 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4197332-4e1b-32fa-8ad8-f736549ca057 | -7.0207 | -44.46739 | 2025-10-01 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 316eaa25-92c4-37fd-a2c5-a01928099483 | -8.67901 | -40.9496 | 2025-10-01 03:28:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 279007cd-ae94-3932-9957-67339e187f77 | -6.23163 | -45.33872 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61d55bd5-ae3d-3440-a1bd-f0f98b90f9be | -5.41363 | -41.32952 | 2025-10-01 03:28:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 099bf504-f7af-348f-82f2-990466f6f29c | -7.62741 | -45.45119 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8faa08ab-54c5-37de-8d5a-88a441915fd2 | -3.89151 | -42.52183 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43b45a96-d5d0-3696-813d-4b1dc712e954 | -6.51573 | -42.49505 | 2025-10-01 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| efcf213a-7570-39cd-bdac-46229f7bfd6f | -7.79776 | -42.51275 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 13f08a90-ec54-38b8-94f8-1b63deda3271 | -3.92958 | -41.58107 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb10ca23-3576-307f-96bb-5a7dc4057c58 | -5.63646 | -43.92127 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fd97ebf8-4716-3569-9011-7f3756159b6a | -3.93455 | -41.59267 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ca767b8e-d5ba-3089-b41f-97577bcaf0a3 | -6.08968 | -42.47384 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6be5c79a-f1b2-3e17-a235-be60547a91ec | -6.42968 | -43.07782 | 2025-10-01 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05f92eeb-4a72-3683-8793-7d9ea8db25a9 | -5.85424 | -43.40635 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 54c15f8d-5372-3b52-bab2-06009ef9d5e9 | -3.86711 | -40.33595 | 2025-10-01 03:28:00 | NOAA-20 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e46a569-c011-3e82-8d16-faaab888a77c | -6.08385 | -42.43882 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6dd80089-2210-3355-96bb-7661ad1ce0bf | -6.46188 | -43.94177 | 2025-10-01 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07c3b496-2789-3089-9ddf-509cc26a87d6 | -6.08969 | -42.43988 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 037b21bc-216b-382b-abe7-343b4be52fdf | -5.47703 | -43.07994 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af27c895-eb37-3c4a-b098-a4c887db699b | -6.43052 | -43.07316 | 2025-10-01 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f90e722a-e23f-3144-b57f-b2ee545f2af7 | -4.62752 | -43.5438 | 2025-10-01 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f050720-2b12-3b62-9835-0a0484ae983b | -6.42679 | -40.6223 | 2025-10-01 03:28:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1a36bbb-b1a8-393e-b4cb-babf2d52c510 | -3.34447 | -43.2001 | 2025-10-01 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37a7ef8a-7d25-3924-a453-633ab399a6ac | -7.41401 | -45.41257 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f351ba7-3b4d-3c48-a816-c56c99da5150 | -3.93317 | -41.6006 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 96941a2f-c5d0-32bc-b32d-755fcf1f9d44 | -5.97991 | -42.65861 | 2025-10-01 03:28:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2150b850-55f6-3a0a-aad4-6adef7bfa396 | -6.79998 | -44.74599 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b2f62f1-1660-3591-85ec-10e05d61b0a9 | -6.70847 | -44.5671 | 2025-10-01 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc9708a3-b2aa-35d5-977c-9fd66c39271f | -5.72726 | -42.88299 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ea924c96-0522-35d3-b089-a4d578d3320b | -5.64184 | -43.92706 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e78ccbe8-33b0-3153-8254-290212748968 | -5.84888 | -43.4003 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44e9612c-b719-3882-8727-c54861c9c710 | -6.46095 | -43.94686 | 2025-10-01 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3f53741-e5a2-3a46-a633-f1f0963c336c | -6.67405 | -42.8097 | 2025-10-01 03:28:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| df96af9f-57fd-386f-b911-503604695531 | -6.21183 | -44.24904 | 2025-10-01 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ceb7fab1-1fbb-390b-9ef3-cbc42fee5b1c | -6.79508 | -44.75333 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b255dd27-5449-39b4-82a8-3b0257694ecf | -5.47113 | -43.07483 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1446f8b-268b-366e-94b7-a8b0440ad4a8 | -7.09304 | -45.56275 | 2025-10-01 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff96b9d2-f7de-39af-a331-b4af473a1003 | -4.62114 | -43.54252 | 2025-10-01 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d5bd345-6663-375e-8917-0c24c0f8faba | -3.88627 | -42.51954 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ef29bce-3b62-35f7-a3d8-71749641614b | -2.98181 | -39.93032 | 2025-10-01 03:28:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b29ee0e1-cd5a-39e2-b3c1-c44de9c7cfc6 | -6.83104 | -42.99284 | 2025-10-01 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d6e7ac5-0c7c-3395-a259-081a3ad7b967 | -4.99017 | -38.85694 | 2025-10-01 03:28:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ff8b6261-2a6f-3f36-995b-14ca3e3a9981 | -8.67692 | -40.95092 | 2025-10-01 03:28:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0597b24-17f0-3942-add7-4f94fa371746 | -7.78566 | -42.51435 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 46e7dbfb-dc65-3ad1-9372-1b036baecdc0 | -5.85512 | -43.40137 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 945c8ab2-ffd8-3e3d-8aa6-11325f0a6218 | -5.61282 | -43.23521 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fb2f9b6-8676-358a-b8f8-a3f0ed5a6c57 | -6.64707 | -42.03598 | 2025-10-01 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f0e1127-d669-3835-b140-8f0b247f33c9 | -6.29147 | -43.91927 | 2025-10-01 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e979c6e4-b830-3d7c-9eec-f72fca687bf3 | -6.67481 | -42.80549 | 2025-10-01 03:28:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5f9d98c8-4a2a-3f29-b14d-717ffeb90a6a | -4.91835 | -43.30735 | 2025-10-01 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5512586-b579-335f-8317-f5774cee1245 | -6.20623 | -44.24277 | 2025-10-01 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a8fc723-e624-3669-ba36-7f396754856f | -5.18602 | -37.66092 | 2025-10-01 03:28:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4044fb1b-9dc6-3fbe-bd1b-d18baae809d1 | -7.95459 | -41.40883 | 2025-10-01 03:28:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d80ae908-e9ad-3b27-ad03-a5840ad0c183 | -5.94406 | -45.87228 | 2025-10-01 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 205b63c3-cd59-3e4c-915d-de1cf2599398 | -6.08306 | -42.47704 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 310d29ea-a809-3830-98c4-45037f85189c | -6.9857 | -42.80104 | 2025-10-01 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73260dfe-5c22-3aa9-802c-bc40613cc998 | -4.96102 | -42.03698 | 2025-10-01 03:28:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20788864-a1a4-31ca-81bd-70024fdf4ca2 | -5.33377 | -43.74368 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5489c52d-74dd-3ab6-9ad7-5a4f6743ac74 | -5.72132 | -42.88135 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 594fa989-6d8a-3199-b29b-05d78fbdf237 | -6.63748 | -42.04228 | 2025-10-01 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 69caebff-5306-3814-9234-b4b0895e5fc0 | -6.06467 | -42.68294 | 2025-10-01 03:28:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53cb88d1-9226-398e-966d-294812af1123 | -6.46282 | -43.93666 | 2025-10-01 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08f2dbb7-28c3-3f7b-8c2a-833c94858edb | -3.34587 | -43.2004 | 2025-10-01 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64fc3da3-0eff-3d10-aaaf-97a0a45fa1fc | -5.84799 | -43.40534 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bf58df32-d7c8-37b4-b997-1b56948e33d4 | -6.78937 | -44.74694 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e832a37a-00dc-3038-abf6-f54b223fe3bf | -3.88019 | -42.5185 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd8a18b7-b3d5-3224-b6fb-49c4a27e1628 | -5.98067 | -42.65429 | 2025-10-01 03:28:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7ea605f-d4d6-3390-8633-341f2ab6ae39 | -5.6361 | -43.9258 | 2025-10-01 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 1f046ebf-e1c6-333a-8c92-fb064ffcfcb6 | -3.1013 | -47.0082 | 2025-10-01 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 424f89b4-da33-39f3-9ee7-e2e44eab9023 | -20.6302 | -46.2287 | 2025-10-01 03:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5441ae1b-f745-3fd0-9f80-de21b9716e23 | -20.6309 | -46.2046 | 2025-10-01 03:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 47d45206-ff98-3637-a4d1-7ac610c9275a | -14.3519 | -45.9206 | 2025-10-01 03:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 57649b07-4ddb-3872-8752-dbd51c9ff919 | -12.2536 | -47.806 | 2025-10-01 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a366e330-c7d3-3832-b1b3-ce5f64f7c1c3 | -3.0827 | -47.0088 | 2025-10-01 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 58b5adb1-3606-3372-b1d6-d9d68b9df952 | -3.0826 | -47.0308 | 2025-10-01 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c502e787-94bf-3121-b8d1-3b258780563a | -14.8021 | -45.7946 | 2025-10-01 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0644ab7a-5f34-38e8-9288-ca7d79c25c9a | -5.6363 | -43.9027 | 2025-10-01 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 0af43f53-2050-3470-9af7-948ce29f667a | -11.3826 | -45.0774 | 2025-10-01 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1a328dac-2b67-36b1-9181-97aaa25c6a69 | -3.1012 | -47.0301 | 2025-10-01 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 47843d03-9f02-3039-86aa-e8fc0fb3a4fc | -20.6508 | -46.2235 | 2025-10-01 03:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 23079518-85f9-3be9-a613-3f3a1f891885 | -11.4588 | -45.0895 | 2025-10-01 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f9ba9073-c243-3311-849d-e28259c208f5 | -20.6515 | -46.1995 | 2025-10-01 03:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d2045ce0-c65f-3f49-912a-05aa5dbb2f22 | -15.181 | -49.0788 | 2025-10-01 03:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 24a04ea8-1c42-3fe7-9fa3-aff8062e84be | -13.9396 | -48.1182 | 2025-10-01 03:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1b46c970-c00a-39a6-bf17-a54ee2f32357 | -11.8434 | -44.9872 | 2025-10-01 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 18a79dda-cef2-3d00-85c2-983746641900 | -14.1926 | -46.1091 | 2025-10-01 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8eac0049-a8c0-3e31-8b04-d8d080b3efa3 | -11.478 | -45.0868 | 2025-10-01 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 95b5bfbb-51c0-366c-b8a8-236daf7a1a29 | -14.02039 | -46.32384 | 2025-10-01 03:30:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94b9d1c7-65b3-335c-b081-6bf8e8154846 | -12.88261 | -46.77037 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de54accc-7a2e-309d-b5db-71e23f994e76 | -13.65105 | -48.03523 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49ee8f50-9547-3781-b597-92900e248c2d | -13.56165 | -47.28188 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48c92d85-5854-3246-b9e7-e78aa25e263f | -13.53814 | -47.25751 | 2025-10-01 03:30:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ffbc4f3-e106-338f-bde1-dcba1470495b | -8.55146 | -44.72744 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a6bd0d6-bb01-31e8-8291-904c129744ad | -12.76906 | -46.86975 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca697544-a98d-3974-8bea-a7a45da43cee | -13.76201 | -47.98256 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3498b96a-108d-3b9c-9714-025a69baba18 | -11.84157 | -44.97599 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README15.md)
