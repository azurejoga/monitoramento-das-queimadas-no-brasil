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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e21104a-d6ef-3d8e-a3e0-7bdcdeaf9506 | -3.83583 | -43.98392 | 2025-10-11 04:32:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06614e76-2aab-3a02-a19b-a6df96a57c1e | -6.43518 | -45.82051 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3d9b06f-6c4c-3a64-98b6-d7d46635d81d | -4.07437 | -48.04472 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf274ae7-b143-3622-8ccc-22c58c8f021e | -7.70568 | -42.37677 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93deb94a-acc2-3115-a36d-1f4af921a96f | -7.62704 | -47.50398 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 873a7b44-fbcd-3c4e-8848-d3a0617e2852 | -3.5169 | -49.70316 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e786b4e-a377-3a03-b212-a3d533078d0e | -5.41299 | -40.98833 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 029e11fc-737e-35f5-b134-31b4b78159e6 | -3.50685 | -49.72149 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ca77e86-4bcd-3565-a79f-a867a80f8a1b | -5.94411 | -42.26521 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a98c85b-02e0-3193-b6c3-71761c70b8e3 | -7.75048 | -44.21822 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6748f19-1ff5-357e-b1bd-300adb29a258 | -7.75492 | -44.2142 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb85650-2a01-33a5-bbf4-669c080bd237 | -7.36451 | -38.75821 | 2025-10-11 04:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 395a5068-3a7f-3959-ab2c-99707ea9c97b | -3.16128 | -49.17507 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 562c1247-2c08-3c09-bb0c-d0e2664b7e77 | -5.94193 | -42.28015 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a12950fa-0de7-3c1c-b052-23b92f96de95 | -3.51034 | -49.72206 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a15d7c9-00b6-3830-8938-0cbb177213ab | -3.77947 | -44.11206 | 2025-10-11 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f088fbdb-c0a7-3c79-bd48-00dfea79bf6e | -8.20679 | -43.33229 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f426359b-2890-334d-a939-205afa80983a | -7.46434 | -46.86279 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| efabb083-411c-3ee4-8723-4284276fd0d9 | -5.1016 | -42.61649 | 2025-10-11 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f3fff70-d422-349a-bf8d-c9e4f3e6a5e4 | -8.19633 | -43.32005 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 154fe7c8-5637-3f78-8f02-528b75f4c5ce | -5.47397 | -43.40521 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28ccf400-4a83-39ca-a2f1-f0a9611fc7ce | -6.43402 | -45.82803 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea0c20d5-c458-3166-9f39-47f73f6f376a | -6.66211 | -41.37598 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c14a03f-245b-319a-a9af-e631d809ce0f | -7.46154 | -46.85872 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b5d7c394-ba48-3ba7-b284-26fe5f453080 | -6.27198 | -39.95224 | 2025-10-11 04:32:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d2cd751c-d567-3ce0-9092-bcdde84e4b47 | -7.74649 | -44.69564 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2462018-d34f-3b0a-98c2-6e3bb402d0a4 | -7.05041 | -41.49614 | 2025-10-11 04:32:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae6f4f90-e3fb-3b9e-870b-1451b394cb95 | -5.86505 | -42.8585 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0ff9f6b7-b600-3a1f-a031-f09c65c4b895 | -6.4346 | -45.82427 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b593edfc-4fb6-3627-8d82-2ec623fb6996 | -3.38984 | -50.13736 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| facd17ec-290d-3170-afe4-5e22894502f3 | -6.05107 | -42.50147 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f9a8a43-a059-3907-86d9-e7c82ff4b228 | -3.11998 | -49.10396 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d6d8a47-b807-3e42-84bc-31df9838b370 | -4.42168 | -43.47209 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd73f1dd-7902-3061-bb78-7a2650aa5d25 | -8.67999 | -40.42048 | 2025-10-11 04:32:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f0a40f96-9dd0-3697-98f0-b509fe4fc2b4 | -5.63458 | -50.39954 | 2025-10-11 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9725a64d-0ba1-3be0-be17-2fd8ddf4a752 | -7.4951 | -42.75929 | 2025-10-11 04:32:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6daee17-31ac-3f07-b374-b7e7eff6aaf2 | -7.85855 | -44.49148 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5696af4-7579-317f-a8e8-f1cf98441d81 | -7.77809 | -42.41431 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3ff2c13-d3ce-3e4c-a437-88ca8510fe51 | -5.21818 | -45.65763 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3273444-4bee-37aa-864f-b5abff66371a | -7.12246 | -45.91472 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc85562d-907c-3ce6-8d49-11a8a2f706f0 | -7.67276 | -42.39568 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad6b2762-1497-3735-bac1-6293d9549ee6 | -7.86311 | -44.46007 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbf538e0-71e6-3968-87c7-b2d0b0d9e508 | -5.58538 | -41.11203 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2ffaa697-651c-38df-8bf9-6ef9b69b292d | -6.04994 | -43.37712 | 2025-10-11 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4a3516e2-2991-3e9a-9b5e-a32bf4603b08 | -5.41136 | -40.98219 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2446ea4e-8ce7-35c2-8b9b-72bf1c1e3bd0 | -4.47922 | -42.86231 | 2025-10-11 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d42904d0-597c-3d2f-aece-54143d19a07f | -6.25242 | -47.22072 | 2025-10-11 04:32:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17641a1f-d307-3938-a3cc-6b449dac1dfc | -7.65786 | -42.5872 | 2025-10-11 04:32:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7ff28d91-b690-3bdd-9ba2-61b07a2e1272 | -6.19025 | -39.69655 | 2025-10-11 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fef31665-c80c-3e24-8a63-3918a651f004 | -6.15996 | -42.55424 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5de41020-7f67-3b7a-a911-eb06a6cc09d9 | -3.521 | -49.69986 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd135c4-829e-311b-a85f-9f5cc42b48bd | -5.32941 | -43.0898 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 39c61b1f-9bd0-3cbf-8fdc-0304c2d05a15 | -5.84395 | -43.41173 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 02cb0d7c-43be-35c8-9f42-a45973dd74a7 | -7.22282 | -45.32001 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7016e57d-0ec1-39ef-8b22-6fbb03317d69 | -7.35539 | -43.85346 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd08e64f-524e-31a4-875a-e55548d2e52d | -3.7423 | -44.40691 | 2025-10-11 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15574ad8-b6f4-3523-a842-135be1d2f733 | -7.40177 | -45.9207 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5c2a90f-fc59-35b2-a383-d239bd9a8c35 | -5.3856 | -45.54946 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a79c504c-75b8-35d8-aaf7-2e9f875b8580 | -7.41267 | -45.91849 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c46c80d-07cd-3206-bd09-703bca3a3dab | -8.14933 | -43.33485 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1141dd8-9215-383d-8878-7885d365430f | -7.67314 | -42.56997 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec0e9655-a2a9-3585-bd54-3944d2afae3c | -5.24152 | -50.94281 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11e60f18-0bce-3ddf-9b4b-a49e6dbe8dc5 | -5.21932 | -45.65025 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22b286a9-7326-31dd-8ee8-ea05f1734274 | -7.5479 | -44.28641 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5ac3d9-e2b7-3307-acb4-73e9e046b5b2 | -5.2366 | -49.86606 | 2025-10-11 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6fb1ebf-c218-3d15-9cf6-f06a9e13590d | -5.1875 | -44.93472 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad540631-f948-37e3-b7d3-cb5fcfb4f3cd | -1.40854 | -46.70648 | 2025-10-11 04:32:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a50f67-c679-3189-892c-21e6d8974500 | -6.18389 | -39.7058 | 2025-10-11 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d84c084a-231e-34b1-a14e-87c0519044d0 | -4.41415 | -43.47096 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a174ca6b-e3b3-3a2a-9d25-9a5f8561bbea | -5.24533 | -43.00458 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42eef024-d06c-381b-8bad-9d5f769e744a | -5.39919 | -40.97137 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8fb091b-0504-3ef9-8a8f-29b098e6aafb | -6.32215 | -43.90144 | 2025-10-11 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 269d6c75-3c8d-3822-8693-c1d93d8fcfc1 | -8.14984 | -43.3313 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7d84f417-6796-3974-85fa-0b73c4799e54 | -0.75636 | -47.75969 | 2025-10-11 04:32:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f2c7de4-f9e1-362e-afa9-5f4b6ca8a0a1 | -5.30871 | -44.87576 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc92736b-1bad-3a52-8cef-aba81111c694 | -4.7582 | -40.57572 | 2025-10-11 04:32:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e983a371-4761-39aa-bbb8-405feb0b36d1 | -3.85165 | -50.50124 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 305c9804-0087-3884-9aab-ac0b41470993 | -8.21641 | -43.36559 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed6f1657-1bca-3b05-8d19-925bcc91df82 | -5.42226 | -41.33565 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15efaa2c-cd24-3967-b7f4-2cc730b1e9bb | -3.26339 | -50.04507 | 2025-10-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f454442e-a034-365b-b081-44916afc35ed | -6.03421 | -42.50245 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f43e882-ab25-3753-8d6b-c3c4693a380d | -5.22331 | -45.76028 | 2025-10-11 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09ea1ad4-9f59-362b-87be-211e0663928c | -5.83619 | -49.02108 | 2025-10-11 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e6d54a6-a247-353d-a518-d87037c32dca | -5.3659 | -48.3595 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0e90485-aa6e-373c-a894-0985dbb9fc82 | -3.12956 | -40.99621 | 2025-10-11 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e145161a-cfec-39ae-ab09-fdb01e8bbf0d | -5.32551 | -43.08281 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7a4c053-b0f6-3a88-8069-97f1bdb449c1 | -7.40234 | -45.91691 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c3ca6b-81e0-3dea-b1ef-92f2d34a14a9 | -5.63096 | -42.69958 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14634953-d78c-319a-b346-ebd52a3c89c7 | -2.59569 | -48.11941 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c359e1c-08f2-387c-8c20-b8982efdbe66 | -4.05257 | -48.89399 | 2025-10-11 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baededb4-7d1b-303f-a264-fb5e1d95884b | -7.55163 | -44.28695 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223c8242-feb9-3518-9ae5-17664b76dcb4 | -6.71364 | -42.20923 | 2025-10-11 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 41147b1c-3daa-3de8-b7e5-2ead5cf5a5bb | -4.42616 | -47.75743 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9976ec47-df30-317b-8a78-c64fc63860ac | -7.67538 | -43.99492 | 2025-10-11 04:32:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da90c1fc-b400-3add-b2d6-d8baa104c193 | -5.4316 | -41.36366 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 538c5e99-8045-322f-94f1-c068f650b770 | -6.63461 | -43.8561 | 2025-10-11 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ca024ea-45c6-368e-bc87-9426197bb1bc | -6.53584 | -44.35683 | 2025-10-11 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d12177f-0b92-39ba-b10f-3054f47d5c1a | -5.4778 | -43.40579 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 30d0d051-664c-3992-b375-4feb2dce24e0 | -4.13893 | -47.65564 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18393467-f5fc-38fe-b369-e1160c19f25b | -6.16909 | -41.73484 | 2025-10-11 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
