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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2006f3a9-0486-352a-9f9c-5ef42631be23 | -7.01963 | -44.60426 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 832be112-569d-3491-8921-75b7b1dbf37c | -6.44835 | -45.72746 | 2025-06-08 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b502e78-b2d6-342f-96e7-c72fa38209bd | -7.0237 | -44.57962 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5d880a7-c72b-3f99-8498-1e71fa8e55c5 | -7.1864 | -42.81579 | 2025-06-08 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88029848-5a6e-3da4-a3f8-f4045eb8f0b8 | -6.87819 | -47.23668 | 2025-06-08 04:02:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f7706d8-826d-3e2d-9fc3-1376828ea59f | -7.0284 | -44.57542 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29b0a72a-f982-3fae-945c-377f8ce26083 | -6.88284 | -47.23753 | 2025-06-08 04:02:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56c2f2fc-6715-36dc-af94-e7178ea73ca6 | -5.63935 | -43.71902 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdfcee1d-de66-3ed7-a46a-b44af4b4e199 | -7.02127 | -44.59434 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ceea0ab-3138-33db-bf34-a0ba348a3103 | -2.91927 | -48.23569 | 2025-06-08 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41dee7f7-36ba-38e6-a1cb-a9b564e8574b | -7.01737 | -44.5937 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70b38ff9-c3fe-32e7-bb37-9997d2c0be0f | -3.25592 | -47.53706 | 2025-06-08 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b934ac-f651-370b-882e-c4e14a590ad3 | -7.2299 | -35.78352 | 2025-06-08 04:02:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 618a9421-63d6-39c6-9dfe-1e4f8d42ca1b | -7.73658 | -44.16854 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96e21950-0ca0-3868-97ed-b9b43490f6fe | -5.77574 | -43.61843 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3b6e432-5f96-3d4c-8982-3e0590d009c4 | -6.49564 | -47.49401 | 2025-06-08 04:02:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37d2b4b7-71c7-3d8e-a983-80c68dd3da1c | -6.54022 | -45.69825 | 2025-06-08 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5ba489c-49ce-3ee5-9e96-e7da20a68536 | -6.43112 | -43.53228 | 2025-06-08 04:02:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13f865ed-6f03-3a27-88ba-a20aa93ac110 | -3.04413 | -49.43862 | 2025-06-08 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f5dff3-52eb-3245-874d-605ae59b5906 | -7.73584 | -44.17304 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d4cfd610-3485-3ebd-87db-9a5cd5a0e536 | -5.46996 | -44.70164 | 2025-06-08 04:02:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45148ffc-684c-37fe-a046-455e408a3e4d | -7.18705 | -42.81181 | 2025-06-08 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19f0ccba-ed47-3259-84d0-3bb2e8f62b37 | -5.64238 | -43.72424 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc02703a-32d0-329c-b81f-890f79ae6e60 | -7.01493 | -44.60844 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87d46f8f-aa5c-31eb-bba1-a6f61765beb5 | -6.44768 | -45.73141 | 2025-06-08 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56ec6504-a577-3bf1-985e-27f70d90caaa | -4.42164 | -47.66541 | 2025-06-08 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c58b9baa-0035-364d-8e63-585a0b476f68 | -6.87653 | -47.24633 | 2025-06-08 04:02:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76f3b072-91d9-332b-b13a-c67d1d267a64 | -5.86751 | -42.87004 | 2025-06-08 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5f766b97-17b8-3ac1-9d55-4c41b591256f | -7.02452 | -44.5747 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3826abc4-1efa-35d9-907e-48b9dbcee38f | -6.20341 | -43.32498 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c5c004d-76c6-3d7e-a7bd-d8ef7aa8d44c | -4.33286 | -40.1891 | 2025-06-08 04:02:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a1acb52-d437-3cb9-b618-db967789ccb2 | -5.775 | -43.62295 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 526b9f06-6f92-3cce-933f-0a973e58b991 | -6.44903 | -45.72353 | 2025-06-08 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22bdbc30-7415-32a0-81ab-55c40ee731e7 | -3.25541 | -47.54012 | 2025-06-08 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19f6f08c-2806-37d7-bb74-9c83e361879a | -7.01882 | -44.60917 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ce1c5e1-fdb3-385b-a6d4-39fce0039606 | -6.49652 | -47.48894 | 2025-06-08 04:02:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 062c7f92-2227-3ab6-9df9-406460ef34ed | -5.6386 | -43.72363 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0b69636-3994-3aad-a0a8-c698a8ea1789 | -8.07384 | -34.97543 | 2025-06-08 04:02:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c4a9331b-9ec3-3d6b-82ef-f1b66dcd5c37 | -3.04987 | -49.43964 | 2025-06-08 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4020c779-9f1d-3014-afcf-91cf08a64b90 | -7.72831 | -44.17176 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d4e5909-c13d-373d-a81c-7955ce54835d | -7.11875 | -43.70152 | 2025-06-08 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fedc6c9f-9102-3669-b45d-4c288fce58dc | -5.77949 | -43.61903 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a009db5b-7b4a-3bb8-b63a-df4b181b9550 | -5.57282 | -45.2047 | 2025-06-08 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76b60799-140f-357f-8ba5-38a51dbe2a8c | -4.46904 | -41.60887 | 2025-06-08 04:02:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f166cb8-a757-3898-9f1f-bed64d0b4be2 | -4.6042 | -38.53179 | 2025-06-08 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2781e4dd-fb12-344e-b95f-349e60f23a88 | -3.25039 | -47.53904 | 2025-06-08 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d3311e9-4733-34f6-9344-ee71e9075cb2 | -7.02045 | -44.5993 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9b84aab-a6ca-35d1-b640-76e94703e049 | -7.72529 | -44.16657 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f2a1748-8a65-3208-9247-5fae27a0b6d6 | -4.48614 | -43.77324 | 2025-06-08 04:02:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13f21a54-2086-32bd-ac23-f240d584bfae | -3.05055 | -49.43559 | 2025-06-08 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0a5429-baeb-377d-ba84-297a1f9dd8b9 | -7.73959 | -44.17376 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8efcdafa-bd80-3be3-b224-8e232d139f96 | -7.74111 | -44.18806 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| adeecd9f-c37f-38de-af63-a86efe9eb4b8 | -6.19902 | -43.32871 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2359a467-d620-3926-afb8-1efbfdbceb1a | -7.01574 | -44.60353 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce776bb1-6ecf-3088-97a9-96fa496dcee8 | -7.11506 | -43.70089 | 2025-06-08 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c96c362a-4a92-32d0-ba13-89ce98ec14dc | -7.73282 | -44.16788 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04feb045-c884-3e6c-9f77-b7e5faef76fe | -6.447 | -45.73537 | 2025-06-08 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1a41a07-ae95-3774-96d1-075ccf3a8059 | -4.60756 | -38.53231 | 2025-06-08 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 7d7e4b50-785e-30b6-91d4-97dd56a3b4e1 | -4.48999 | -43.77386 | 2025-06-08 04:02:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74192591-6b95-3394-b6ac-cc7858e331c2 | -7.73433 | -44.18217 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fe8c7a9-4888-36b2-be63-aa379821c8d5 | -9.40632 | -48.44418 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 04c290e3-a02c-36f7-8823-ce02302e2fd1 | -7.81928 | -46.49626 | 2025-06-08 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a8823c7-88bc-36fe-bc0d-febb48f07779 | -10.64532 | -44.48993 | 2025-06-08 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c075e4b-06d3-3d9e-a2ad-7115460bfff7 | -9.40727 | -48.4388 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4031de17-ef8f-33a1-ad99-76581c0b0db4 | -13.06705 | -49.24347 | 2025-06-08 04:04:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a25f8b3-3712-3f2f-9dd8-4319be8ecd2b | -13.33267 | -45.46973 | 2025-06-08 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e5a9bcf-2ae9-3d63-9f26-5585f0987f8a | -10.64313 | -44.48058 | 2025-06-08 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85b5a8d2-1a1d-3531-bf9a-c2493f5b489f | -13.54108 | -44.14426 | 2025-06-08 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34bda28a-5cef-3fd7-abaf-d4ca06ced396 | -13.41842 | -43.75342 | 2025-06-08 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa4ea0c-09e3-36ca-a92d-956e1cf0c0bf | -7.86616 | -47.89679 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c78bc8ea-e74e-3464-a351-200d53b75b73 | -9.40518 | -48.43999 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c66088e-a9ff-3a14-8f6c-4ee06ac617bc | -12.07628 | -45.79375 | 2025-06-08 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 258ca9b3-7a90-3f54-b3c5-1f7d9aca8f84 | -9.43938 | -40.34839 | 2025-06-08 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e242c30-aaef-3de6-8db1-6d36b4afeccf | -9.07042 | -47.14455 | 2025-06-08 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 864b80f6-2954-37d8-837c-d9ec26506853 | -10.64901 | -44.49056 | 2025-06-08 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc53d53-bab8-3568-b333-6849790fc24d | -14.87801 | -48.10383 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b6985f8-c1b9-35c8-941d-8934c9131fa1 | -11.80083 | -48.09031 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 80d61b1b-0a43-349e-9a63-20f1de55b142 | -9.58784 | -48.73058 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65afc2f9-5244-373e-b687-7ef3df2cb1c7 | -11.05987 | -44.27401 | 2025-06-08 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 978e6a96-a51d-3aac-8c32-051491b1b42a | -12.54244 | -45.4077 | 2025-06-08 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17bcd6a8-72a1-303a-a3d5-034e8d092c98 | -8.6914 | -47.14138 | 2025-06-08 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1edee7a-7896-3899-847f-2c6319d8289e | -13.48845 | -47.80977 | 2025-06-08 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c96f5c2-846e-35cf-b4d1-35767d1a5fb4 | -12.54165 | -45.41236 | 2025-06-08 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66cf00bf-6c0e-32a1-9442-d07d90b38299 | -14.42789 | -50.64842 | 2025-06-08 04:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2eb80c4-3069-33d2-a00b-4bfc0778e756 | -12.98493 | -47.11715 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a3d11a-61f4-3da4-9f1e-24101c6cb323 | -9.39582 | -40.53872 | 2025-06-08 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4920bec0-12a1-3e89-aa8e-acdb2fbf053c | -15.52616 | -42.61956 | 2025-06-08 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 908ef680-948f-356b-bab4-e05b8ff69ce3 | -11.11938 | -54.64508 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75bdf889-baa5-3429-94fb-4506e3c40182 | -12.94759 | -46.75584 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c450536-db7f-34d1-85f4-c2fb4521a28f | -12.06983 | -45.76192 | 2025-06-08 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea5b5e3-b569-31c2-ac35-77c1719672c8 | -9.06042 | -47.90962 | 2025-06-08 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bfe36c5-241f-3a3b-b201-6cdabb6e1a61 | -12.54086 | -45.41703 | 2025-06-08 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f7b0ea9-cdc0-30d7-bebb-e2105c83a7bf | -9.07564 | -47.14098 | 2025-06-08 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 404fc3b7-8105-3764-9510-0b98ae9f0066 | -13.37193 | -54.25393 | 2025-06-08 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09d6b72f-eb15-393e-bd1a-ca08c41d4c09 | -12.97338 | -46.75279 | 2025-06-08 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec1fd36f-ad60-355c-92a6-0201566dee1f | -9.40419 | -48.44537 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 435d3699-4398-3f0c-8599-e0d42be03291 | -7.87004 | -47.90293 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9194b71-1544-378d-9112-47b44919afe3 | -9.41117 | -48.44504 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dedbac09-1871-35cc-92a9-9b2ac49cadf6 | -11.12077 | -54.63845 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 58ff30fa-feab-3be4-9412-3ec9c68cb4da | -9.38592 | -48.41836 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
