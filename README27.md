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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf873038-3708-3dd8-bd05-6ce6a74b5678 | -6.39549 | -44.25477 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed0db7d7-d755-3b2b-80a7-50d68fb1d6ae | -5.64836 | -43.37067 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04a8734a-611a-3d44-bbc8-92715c5687d1 | -5.98198 | -44.14837 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7af531be-0198-3941-a851-a8e49666a7f8 | -6.63183 | -35.07088 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d533a5e5-0da1-3016-ad3e-f65c54ebad44 | -2.44439 | -47.32669 | 2025-08-20 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2c7742-90ea-3fdf-886d-94012c830c3b | -5.80451 | -46.55133 | 2025-08-20 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7df517e-1dee-3389-8400-de8af1da268c | -7.64164 | -45.27726 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d861a0f8-b9f8-3f97-b4fe-dd839d56cd03 | -8.82198 | -52.06273 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d2e91ed-0ec5-3073-9fb2-4ce2290b1c8b | -6.18847 | -55.46204 | 2025-08-20 04:34:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72421d9f-d15b-3420-b553-4618132e67c9 | -5.97656 | -44.14506 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8925511-6c7d-39bb-be3a-f9f673decaf8 | -6.437 | -45.50566 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2363c1b0-bdce-38cb-b940-bbca125b59de | -3.83758 | -47.41796 | 2025-08-20 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5108b6dc-290c-3e5b-8681-5cfd0bd35d58 | -6.1515 | -57.71329 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43bed24e-4785-35d6-ae47-5a7df27b1655 | -7.64404 | -45.26108 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4aa6cd5-cac7-35a0-8306-485afd9ecd8c | -3.97002 | -42.50616 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9be8d051-31cd-396a-bb3b-60b9f0156b24 | -6.3685 | -44.74756 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53367dfb-41aa-39ba-baa9-383864be5dcd | -5.35962 | -41.21632 | 2025-08-20 04:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0597d8d9-b3f2-31fb-8dc2-c7b244295ce2 | -7.39217 | -44.27429 | 2025-08-20 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91dab31f-d57c-3a0a-a267-48f09b56750c | -5.60978 | -43.47001 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3508199a-ecb5-3912-a54c-309994f9f667 | -7.63389 | -45.26065 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6eb5c81-4040-3ffa-afd5-b7158e97b253 | -8.83235 | -52.04846 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30dc7a78-47e7-3a9c-8129-b1230cf1c6c4 | -7.59441 | -44.39087 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9296fc3e-d0ba-39e9-b88c-12c25ca2c7b2 | -5.99764 | -42.85136 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7606191e-ad8d-3c9d-bdb4-95749e2b8999 | -6.02771 | -44.39103 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3557df05-36d4-3c0d-9d8e-d26d9175ec3a | -7.97192 | -55.30562 | 2025-08-20 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc4175fd-69e7-3d4c-9d99-ddfad969158c | -8.01732 | -47.66927 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c599ff9f-b475-3efa-912f-e93183fa0776 | -8.17111 | -47.35572 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 439aa0b2-c331-36bd-b005-daea7ca4c4ca | -7.65881 | -45.25943 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 959a311c-29e2-3928-883e-5ea7e327c435 | -6.45372 | -44.55619 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dff1a11-8ce8-3412-9135-ec44ea1f152e | -8.41512 | -45.68678 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81a3d3a7-7586-3788-8c6b-5710722c5c25 | -2.97087 | -49.29736 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfd39060-3899-31fd-9481-053fd79e97e3 | -6.31955 | -43.61287 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea754a88-0371-3112-9027-02f4056331c6 | -7.64932 | -45.27437 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f4df45-f489-33ad-8264-50ee4331febe | -5.5945 | -46.28994 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2baf308-c5c6-31fb-90ca-a20a907097c1 | -8.80439 | -45.33034 | 2025-08-20 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2081ddb7-1c38-30ac-9698-7ea67d87a496 | -8.17276 | -47.34517 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c3e524d-0f0b-31eb-84a7-abbbe35b63f8 | -8.21495 | -47.30898 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54dbeff3-69d1-3be2-ae14-49022dc7203b | -5.68453 | -46.47116 | 2025-08-20 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6cabbd4-72ec-37a3-9b56-36286d40b8ce | -3.98694 | -47.88661 | 2025-08-20 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 268c67d6-df03-3658-9031-effe052c2130 | -6.00609 | -42.8218 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1cc7978a-8d18-3072-8556-271e2f25f9c5 | -6.02836 | -44.3868 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e916631c-2370-3a5c-9470-84b2ab9116dd | -6.53086 | -45.47352 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac746b70-e25d-321e-96a5-225a873cd4e7 | -5.86344 | -43.43827 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caae2de1-ea09-3155-a55c-ae90c455b71d | -9.45279 | -48.36615 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94abb154-3a91-3539-b74a-153423eaa343 | -5.31712 | -44.48632 | 2025-08-20 04:34:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 231187eb-2c70-32ff-84f8-3b8981fc4a3e | -6.02408 | -44.39042 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75fa7719-2c6a-3453-a135-80bcff89fb20 | -4.43029 | -47.75676 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 406b0640-7e6b-36ce-b8da-a46a78341296 | -6.37573 | -45.0569 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cefb3251-0572-37db-a7b9-5fe0dbc10469 | -4.31105 | -48.099 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac842ee3-256b-3b34-8d3c-ef3326403e55 | -4.09631 | -48.74414 | 2025-08-20 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0429ad9c-ff0c-3319-a19a-ad366fdb50b6 | -7.29164 | -43.6804 | 2025-08-20 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a63fb88-cfbc-313d-b0f9-e24b36f8ed9d | -9.37341 | -48.29229 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff684860-b0d9-3830-8714-a0477286992a | -6.91899 | -52.85585 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6caa90b3-9708-32db-aaac-dea199719d9a | -7.21177 | -46.25528 | 2025-08-20 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8faf9cd4-568c-33cf-a1f4-61075b224bdb | -7.64142 | -45.28253 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 957ed7b3-a2dd-30f2-bdc8-d834cdcc77f6 | -6.44914 | -45.49591 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dc0ef2f-858d-3dbc-95ac-819c8ab17ad2 | -7.22804 | -44.70108 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a0debf-b6e9-3299-bcf9-c1a7ee26a088 | -6.5055 | -43.43462 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc1e32a9-f117-31de-a89f-31123b689f35 | -5.54081 | -45.37758 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09490ac7-f517-3835-b775-42b88ab7687e | -6.07256 | -44.39178 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24859d04-4a0e-344e-9ebc-dc30491a7df9 | -2.54673 | -47.70345 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ec4892-2019-3ea2-bb73-288015539545 | -6.02198 | -44.35548 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1874effa-7548-3df5-9328-879adc093ba0 | -8.14361 | -49.51483 | 2025-08-20 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14594891-c676-3bfd-81f5-c770fb4e6420 | -6.02263 | -44.35123 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22e905ec-16c7-3532-b874-863e33a03458 | -7.58011 | -45.42316 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b447fe2f-068b-39c6-97f1-80919d44d30e | -7.64458 | -45.28183 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7df69888-2536-3729-b526-e288f1d1200c | -5.06122 | -43.72755 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19b18d33-a9fa-30bb-8b25-ecdaf87d10bb | -7.83347 | -47.67241 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6e67bf6-44af-3fe0-82ee-3ea58c7ce30e | -5.11646 | -43.21642 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07a0879f-a713-3665-9cc7-35d89ad5d754 | -8.22218 | -47.30654 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdb1256d-2ccc-3590-a118-137fb6d4ca70 | -6.71087 | -44.3271 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95e0a74e-d90d-3fff-a961-eccb1173364b | -3.98267 | -43.2444 | 2025-08-20 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10c470dd-a675-3395-92e4-e81df117bcac | -4.31328 | -48.10654 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d5fcc87-3080-304c-ba6a-b904e88ed643 | -4.00452 | -47.09096 | 2025-08-20 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43795249-8abb-3809-aa59-6ae0c2b4c8fa | -4.95351 | -43.08698 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6f75a59-3ed7-336b-b9fb-84546633a107 | -2.35362 | -47.46902 | 2025-08-20 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f57410c8-0027-3851-b2da-29a5d966396e | -7.63726 | -45.28596 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddd0ea97-d971-33d7-bab2-f89e92b61515 | -6.54609 | -43.0056 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1904ffd8-52a1-3f44-98b7-240ab853bf8a | -8.80836 | -45.43784 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b28853cc-d0c5-3d71-974d-8cde2c90f808 | -6.55082 | -43.0011 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5444c103-dd0f-32a8-9da6-1046109c64ff | -6.13326 | -57.70782 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105d4f08-5562-3a89-8f8a-47296266d9ed | -8.02785 | -47.66736 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbb4ec05-ff91-3675-988f-e8ee08238254 | -6.01235 | -44.19691 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6206c74-c60b-3438-a821-ae9924473639 | -6.72126 | -44.33309 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8928e3c3-2809-3dde-917f-4dbd4d1c54b4 | -7.64223 | -45.27322 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbf297e0-09e6-310c-a924-3b47b57335a9 | -5.68844 | -46.46814 | 2025-08-20 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02a4613a-dca7-3940-9c03-005a7671c568 | -7.58634 | -44.39419 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ec94836-d5d7-3d14-820a-7ac8bd90fab7 | -7.64159 | -45.25782 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f825b91-ca69-37c3-8367-0cbd718320f6 | -4.16954 | -42.02612 | 2025-08-20 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 32570036-fd96-3aef-b060-0332747d8634 | -6.9594 | -42.87387 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 113058fc-f816-3dea-89bc-7266d3bc0306 | -2.91592 | -48.30183 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 919f20c0-1ae5-3245-9482-150991741ca6 | -8.02675 | -47.67434 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d3101f20-1a00-311b-9db7-45279cba462c | -6.02562 | -44.35608 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d73ab60a-6832-33b9-98f1-12097a8dbaac | -7.22836 | -44.25785 | 2025-08-20 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e991c8c1-6298-3e99-b204-ce8c4631b04b | -5.78829 | -43.89149 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 366bd2d2-aa67-385f-b795-dd027ddf444a | -7.64872 | -45.27839 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdc655c-983f-3935-9421-df735fa9c60c | -8.21392 | -44.4226 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ede31d65-9f78-3583-87b5-41820b2e3f2b | -6.45434 | -44.55201 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efeb750b-17a0-3d20-919e-bd86e99f06da | -9.15048 | -44.38673 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5f0ced0-05ec-37e6-982b-3d1267d66e6e | -8.30215 | -47.61755 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README28.md)
