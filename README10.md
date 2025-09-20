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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 120caa3c-a40f-3143-8fa3-669af68cbfd8 | -6.46887 | -45.98563 | 2025-09-20 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e235013-705f-329a-8223-f9967e704688 | -6.96123 | -42.43891 | 2025-09-20 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0441d7c-baca-3415-af0c-047cdbbb7445 | -7.33123 | -44.56253 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd496f34-ead9-3f98-ab14-4e068955fa4e | -4.35339 | -48.72541 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e849b6dc-08fa-3482-a441-d02725cfa3c2 | -4.94448 | -49.92214 | 2025-09-20 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba4364d-1be2-34aa-bb24-4127eecd891c | -5.19624 | -45.48529 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6664ff2-0718-397f-924f-8d113613e851 | -5.82913 | -46.35791 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c76a1ec5-bdd8-392c-9aea-fc1c1251df8d | -4.67252 | -43.63927 | 2025-09-20 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0d26ded-7964-3f9c-a3db-826a6b056812 | -7.43739 | -42.62595 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44bb14c2-f937-3810-989d-f91e55437869 | -2.79927 | -47.14443 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8c5845-4246-36a1-affe-07221711d498 | -5.10694 | -43.20498 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 393c01c4-b2b9-39ff-b2f7-0839d991da5e | -6.81109 | -47.85605 | 2025-09-20 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26b1c0da-1e28-30ca-a034-0d95c3e8a4b3 | -6.46505 | -45.68323 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01d11d7-e5e5-3d5c-a3b9-554ea48dd85f | -6.86323 | -45.46209 | 2025-09-20 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e26b3958-debc-39fa-8b71-0c7b97e353e8 | -2.79533 | -47.14754 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd052e41-697f-34c1-8fb0-80b18915880a | -5.31453 | -45.1179 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 476cca92-9c88-3235-ab7a-c98ed4a605cf | -8.81594 | -43.0467 | 2025-09-20 04:25:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bb0b620-502b-3d5a-beb6-c490a7442fa4 | -7.59738 | -45.50718 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315be2c0-1df2-3e3d-a7c1-fe326e8c7d94 | -4.48216 | -38.53394 | 2025-09-20 04:25:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ef2d39d-d4a2-321f-a609-bda288da4497 | -8.14379 | -43.62217 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec87f422-e005-372c-8919-6c1c3cc07ef0 | -2.84962 | -43.68016 | 2025-09-20 04:25:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e28ce13-fe8a-3a56-a7db-c200492d2968 | -2.96211 | -48.59932 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 955ac6d2-416b-3844-8254-c7b3d597a087 | -7.51301 | -43.6722 | 2025-09-20 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9371329-0f48-3885-b52a-a2b577052a89 | -8.84238 | -43.02278 | 2025-09-20 04:25:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dff0415-5e57-3602-b1ac-7c1f3c1c1436 | -4.15882 | -47.83459 | 2025-09-20 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffaef2d0-9e89-3037-99c6-0199e17a4506 | -6.21428 | -42.63909 | 2025-09-20 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03de45c0-d025-3962-9dd5-4bdeb65e4f90 | -6.64663 | -43.41866 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 040aa46d-3b95-3e88-a946-c078698d2195 | -5.11466 | -43.20201 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17c830ba-893a-36c0-96e5-f29b700304af | -7.44442 | -45.19835 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a7306a3-e0d8-3a47-a0fa-59507c1a50d0 | -6.40375 | -43.32166 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fea79d86-ef20-346a-987d-db4604c9f3ee | -2.83628 | -48.66031 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3230d587-c0b7-38bb-a6fb-d33cf87d3a87 | -5.10339 | -43.20448 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83955ef7-78a0-3640-ae3d-66cfa27d7a79 | -3.74048 | -53.80683 | 2025-09-20 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a39a48af-b2c3-3ed0-8e61-0791d25b9637 | -3.98648 | -51.06085 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b341525e-8e3a-30d9-a563-ceaf56cd7e03 | -4.66082 | -46.03919 | 2025-09-20 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa07cd9f-65fc-3917-813d-8e2c22341f12 | -7.31405 | -45.16007 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d90ef1d-99f1-36b7-9233-d5a5d06ec496 | -2.43229 | -49.33525 | 2025-09-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| dcde1465-301a-3097-bcb4-e8c4960ce180 | -5.89502 | -45.71866 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96cf33d0-7d2b-31f2-96fc-72eb5d628179 | -8.61606 | -41.16431 | 2025-09-20 04:25:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8efab69b-2d92-30db-bf57-f86a48b7b253 | -6.39304 | -43.31976 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6fa8470-23ed-3ffd-9d62-adaa47caa48f | -4.20632 | -46.43983 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5982e149-baf5-3d92-a5e6-b37386a690b8 | -5.82942 | -43.88065 | 2025-09-20 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51399c8b-912c-304e-b36e-d2b28b183b40 | -5.59279 | -44.09329 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f44a3eed-f469-324d-b65a-24188d22bb7d | -7.09038 | -47.33927 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81aa4b56-f52c-34f8-97d8-ceacdcbc5f85 | -7.23187 | -46.61221 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 465a475e-13d4-3cd9-9db6-79417e3d3417 | -6.19682 | -41.22459 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| eb8c0d44-9571-33e1-871e-d19df40cf773 | -6.81052 | -47.85965 | 2025-09-20 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b12af137-307f-3be5-ad69-7ea85045c14d | -7.08707 | -47.33873 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c23f57f-d9c3-3836-aaba-6e056b1b34e9 | -5.7176 | -49.87519 | 2025-09-20 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f2f01c-af7a-33f1-a203-ba774ea498e7 | -5.99837 | -46.64616 | 2025-09-20 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30144a79-2bcd-3dc0-823b-08d4422e9763 | -7.57067 | -45.50306 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e99f334-5ec2-3189-af8c-870664b146f9 | -1.68701 | -48.19949 | 2025-09-20 04:25:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8400db-9ede-3f21-9a13-9021fdfa3e7f | -7.24203 | -46.33096 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467c0bc4-14c9-3750-911c-792bd6afcb74 | -7.25267 | -45.49353 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 860a5f07-ffaf-3cf7-ae84-78a702a12ec1 | -5.89029 | -45.63985 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60164880-145d-36f4-9920-2a09e3c2b59a | -5.16512 | -45.42363 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cfad2ed-0d29-3694-be57-b3633d25dbd7 | -5.74279 | -42.58524 | 2025-09-20 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eacd505b-4d32-3c12-ac88-27f23ca68175 | -5.16843 | -45.42414 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f2ea564-9b09-3c7f-9e59-e3c6fd66878f | -5.81556 | -49.84876 | 2025-09-20 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f0733b9-0d82-300a-a2f9-a10c48550146 | -7.49017 | -44.99035 | 2025-09-20 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db677504-809c-36ec-b4ac-114985da91fa | -5.76318 | -42.77475 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da4b0606-2cfe-3077-ae87-f35cc1c5ad65 | -3.3508 | -48.39107 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df75b066-7e5b-3139-8927-a230b76ebdaf | -2.92325 | -48.95906 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34fde56b-7bb2-3cdc-9f68-2098382c1cab | -4.27335 | -48.63569 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c994d98-2058-3b0b-84af-ad45c0394404 | -4.63623 | -50.99871 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd36759-fef6-3d4f-88a8-941ddb2d7400 | -4.35899 | -46.2905 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 440a940d-581f-3807-b3dd-fbb1df7d7fc7 | -4.36283 | -46.28757 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc26b33-d420-373b-84b8-b8f978210932 | -5.6346 | -45.94982 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3d3231f-319f-38c7-aae6-517568819b22 | -6.19347 | -45.1057 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8bd7e95-89a2-31c0-a17e-24144733e29c | -5.43095 | -45.81575 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b6e149f-9438-3d28-91cc-acf2e2bce9a7 | -5.51966 | -43.85763 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 032e79d6-46f6-347c-ac0e-a662fa55d5f6 | -7.59677 | -45.48896 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d26dfce5-bfae-3a3a-a27b-c9da74dc7e5e | -7.08652 | -47.34223 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a768b9e-0707-3145-8554-d1f247af0bb9 | -6.1066 | -47.85123 | 2025-09-20 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19c4be8f-4354-32c1-a85c-d576e137f65b | -5.85585 | -43.8128 | 2025-09-20 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccb6f914-d492-3699-a925-c47b43c0c25f | -5.60594 | -52.15034 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab786eb-1daf-3ccf-b20d-bd09f1815722 | -3.92455 | -47.53855 | 2025-09-20 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f88ec87f-a7b8-3013-bd88-fd17fb416986 | -5.74284 | -45.07579 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1809972-0c36-3877-a798-85a714d3c761 | -5.04151 | -43.08871 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29e863af-152c-3141-a8a4-191f6204aac3 | -5.04355 | -47.90387 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 466dce03-96c9-334f-804c-d1ea104add6e | -5.30732 | -45.58039 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15602c23-cb92-34a5-91b2-84ed26345331 | -6.36657 | -42.89484 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 199be67c-172c-3a43-a561-009f0d865109 | -4.66858 | -49.33189 | 2025-09-20 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8902475-dea2-3db3-8a62-fd805cbce9ed | -5.19347 | -45.48131 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53a01840-bcf2-395e-bfcd-e008f060cb22 | -4.87359 | -46.82915 | 2025-09-20 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ed885cb-6c14-39be-abb6-f3558eacc144 | -6.20087 | -41.22514 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d1e3f8f-9040-3865-9208-72ebe6faf76a | -5.3112 | -45.11739 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02317d4d-00a4-39d8-9a32-1666db8248dc | -8.49091 | -44.73106 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c26073-10c7-385d-b1ac-90d79ff9c046 | -5.83715 | -46.28513 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0152f7b-2093-36fd-864d-c8381ab5a005 | -5.0404 | -45.57027 | 2025-09-20 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b49c08-28d8-35d5-8abb-4e521c57738a | -4.27999 | -46.36287 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e542058e-e6ee-3daf-b7bf-ecff17980e18 | -7.38193 | -47.04376 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 329f133e-91a7-3882-891d-bdb2b31a3bb0 | -4.15941 | -47.83091 | 2025-09-20 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29a3a548-0b19-30bd-9311-8237d8fc9092 | -5.20766 | -42.30466 | 2025-09-20 04:25:00 | NOAA-21 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b0743f55-4805-38e7-bc8c-ba3d744f117c | -5.1105 | -43.20549 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0956b5a0-8557-3a50-a76f-e07a3f79df70 | -7.61 | -44.45701 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 205ab169-2517-3ceb-8628-2f95155c60b2 | -7.23463 | -46.61618 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b96ce34-01f9-3d43-9433-f87835dc2e59 | -5.0891 | -41.14192 | 2025-09-20 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 47dfe88e-657a-327a-a2ec-d3fe14dc1cf2 | -5.79691 | -43.64922 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5de4a92-650b-3a45-a8c8-dd5b15e2040b | -7.57844 | -45.49697 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
