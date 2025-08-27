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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba77d109-add6-3fee-a221-617e8d7539cd | -6.18263 | -44.03246 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5b777fde-d740-3f61-982c-e946db008f49 | -9.13571 | -45.23636 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 66fa2c50-3cfb-332d-b6f3-6bbb4ec8d20b | -6.35109 | -43.6528 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 24054625-128e-3abb-b814-85c7f603850c | -7.70708 | -45.76639 | 2025-08-27 11:55:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ace27a6c-5ea8-3391-85e9-9d867ec8b9e5 | -6.7083 | -43.10279 | 2025-08-27 11:55:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45617dec-8551-3fb7-8d1d-0430fcce29c5 | -6.87059 | -43.61049 | 2025-08-27 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6acd5ffa-d155-3f64-b846-c66f31df0c7f | -7.1793 | -44.87308 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| bf532f7f-d23c-3329-850a-03667c5177dd | -6.45988 | -44.5751 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| dbd313c6-7816-3f55-bb0f-7ae84b210efc | -5.78366 | -43.61324 | 2025-08-27 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fed71e03-3797-34fc-8528-df03b74e212a | -6.4408 | -44.55946 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b954c6a3-30d1-3d32-ab29-67d01d7a238c | -7.0664 | -44.28811 | 2025-08-27 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8d2ce527-7d21-3d84-8612-201c1694cccb | -6.88996 | -44.42861 | 2025-08-27 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c4ff198d-50b6-37b6-be40-0f8f38ab8b98 | -6.43692 | -44.58509 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b157def0-ff3b-3ebe-b8e3-9d02083d197d | -7.43413 | -42.04819 | 2025-08-27 11:55:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 103ef47e-3c7a-3637-93c6-aba8e7dc350d | -7.53948 | -36.73734 | 2025-08-27 11:55:00 | TERRA_M-M | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3222bd23-95b6-36a0-9661-e531d1337b28 | -6.31855 | -44.82877 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 6d6fe12f-ff13-387a-a4cb-8d9ec37b32ee | -6.88359 | -43.59006 | 2025-08-27 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 9f615a18-6631-3885-a0ff-35d8d1331597 | -8.91648 | -46.65741 | 2025-08-27 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 47ca52c3-6846-3a4a-adeb-b5455e9bdda1 | -6.20306 | -44.16371 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b63b4a2d-deee-3e22-9ecc-40df42793a78 | -6.18357 | -44.167 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 392539f5-f0b3-3188-8b13-999e47f22976 | -8.09176 | -45.00723 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f6193916-1093-3f53-b4ca-1ee719fd8e69 | -7.64502 | -42.68253 | 2025-08-27 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d2a5aada-6043-37b0-a22c-db0cb58fbf35 | -5.49765 | -43.94951 | 2025-08-27 11:55:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3cf0784b-5193-3dd2-a923-14888f760613 | -7.12568 | -43.68881 | 2025-08-27 11:55:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8dfd4fda-ccbc-393e-a895-1d142e983110 | -6.36468 | -44.04777 | 2025-08-27 11:55:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f5b6fd94-aa20-3fb8-b1c0-fbf50dbb06eb | -6.37233 | -43.85878 | 2025-08-27 11:55:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cefa7187-fdac-39d0-be4b-947e68a0761f | -12.74896 | -48.19009 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2bc01188-148d-3af8-b245-0317acdac9da | -12.93324 | -46.3163 | 2025-08-27 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c51b0d42-d46d-39a9-8aa7-8c87dc33d164 | -13.7535 | -41.78604 | 2025-08-27 11:57:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 753ff75d-6647-3131-8aa4-2df62fe321fd | -15.19968 | -41.12469 | 2025-08-27 11:57:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 1e906aea-38be-317e-9dcd-1b3336a913cd | -13.53402 | -42.47066 | 2025-08-27 11:57:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c7f69f94-b2f8-36ca-a7a5-49ad9b653252 | -13.75221 | -41.79512 | 2025-08-27 11:57:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 95f09b32-bfa1-3b74-abf4-b872fe010a7d | -12.87067 | -48.10716 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a59827e7-aadc-314a-87ab-cd54eaaa2efd | -14.12184 | -42.10539 | 2025-08-27 11:57:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| fa561664-36c2-342b-adad-f7af1a766a92 | -17.44802 | -43.65556 | 2025-08-27 11:57:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 917d0828-4a5a-3116-b82d-71bfff890cb2 | -10.80239 | -43.59578 | 2025-08-27 11:57:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ab93aba5-28b2-3b16-9438-a1c2fe394964 | -11.58432 | -46.3953 | 2025-08-27 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 88a90f95-9f63-3967-8465-80884e35285f | -12.80359 | -48.10839 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6f236493-fe7f-3996-99bf-d5260dedbf97 | -12.6994 | -48.18065 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ef7171be-0d1f-3334-967c-30fb37fc9b43 | -12.7956 | -44.89298 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 65695f52-223d-3b8f-b49e-29d2786dbe83 | -13.07508 | -46.31007 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 64fd9cb3-0b58-3422-a1cd-6d25a1cea09e | -14.12144 | -45.41358 | 2025-08-27 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 126e6f7e-5db9-3ca5-954f-60f98c95c4c1 | -10.9825 | -41.82145 | 2025-08-27 11:57:00 | TERRA_M-M | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2fe97095-fee3-3414-b009-b37424e6a113 | -16.31353 | -45.11041 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a6d0df5e-99db-3a10-84e3-18d1b723d4f1 | -11.8182 | -46.80493 | 2025-08-27 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0a7a49a7-357b-3983-93cc-bdd8df31359b | -13.60392 | -48.21029 | 2025-08-27 11:57:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 5eac1dc8-f93d-3e39-b146-84fb68f3a26d | -13.52888 | -40.68803 | 2025-08-27 11:57:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7f135e6e-b05b-3206-9c69-9f39dc548c95 | -16.7434 | -47.59201 | 2025-08-27 11:57:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 164b5e7d-c7c3-37e3-b113-71eb79a6fa30 | -12.74572 | -48.21006 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| eefb61ef-a19f-38e2-9ce9-03547f024ac3 | -12.23285 | -41.52491 | 2025-08-27 11:57:00 | TERRA_M-M | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 53d18c28-87ec-3dd9-a02c-18f9130f5766 | -9.67668 | -43.71275 | 2025-08-27 11:57:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 3392aa9a-75f0-3e73-920a-770583936dba | -13.38956 | -46.92714 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b6bd5838-cdcd-3ba9-8777-5dd81f40485e | -16.11763 | -41.27418 | 2025-08-27 11:57:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 53451ba7-b62d-3963-adba-33a653735c90 | -10.86226 | -47.32182 | 2025-08-27 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 65bf1670-d4fd-3847-88d5-772e4ab5cff6 | -13.54348 | -46.90522 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2e73e37e-65b8-3f21-8827-ff4e74bcf05f | -11.80689 | -46.80289 | 2025-08-27 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| feae1fdb-5e16-305c-aac3-73a2618ebcd9 | -12.65725 | -45.3271 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| de228f58-19bc-3de9-b228-4b6ffb8c0c9c | -12.78803 | -48.12552 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 46b8d668-1c6d-337a-8f3a-3da1dcab489e | -12.23157 | -41.53392 | 2025-08-27 11:57:00 | TERRA_M-M | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| de2da589-365e-30cc-90f1-8b8e52113def | -10.9838 | -41.81251 | 2025-08-27 11:57:00 | TERRA_M-M | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| d462ba8b-af4f-3c2e-ae6a-19280da6fbfb | -11.8992 | -40.94716 | 2025-08-27 11:57:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 53a06173-b6d2-3002-b2ff-a0e4628100ed | -12.71171 | -48.18349 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| e7efe6f8-ed8e-322b-bb79-f7761f6a61fc | -9.09461 | -49.56811 | 2025-08-27 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3a52a1ea-fd0c-32d4-be1c-45c0e635dfc8 | -13.53533 | -42.46161 | 2025-08-27 11:57:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7ddf5fa5-b8b3-31fb-a4a9-62ae9dc9804d | -11.24302 | -44.99093 | 2025-08-27 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 238cac1d-c275-3ae4-96c1-cb004b1ce65e | -12.78153 | -48.1643 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| fa371c45-cb53-3101-8dc3-530655c371d2 | -11.32776 | -43.29739 | 2025-08-27 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| acccaca4-233b-300b-8b59-72d1513496a6 | -11.25301 | -44.99266 | 2025-08-27 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 89c1e8f2-068f-3d26-81de-c8315db340cd | -12.93098 | -46.33067 | 2025-08-27 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c224ee8f-34c3-36b1-9170-3f62a326e200 | -15.49811 | -43.54883 | 2025-08-27 11:57:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7506825e-2b65-30e3-97a7-fa5541cda965 | -16.79441 | -47.55667 | 2025-08-27 11:57:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0ace587e-da1a-3928-8e3a-f02cf202067f | -12.19291 | -47.1912 | 2025-08-27 11:57:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f2825e07-6748-3e3d-8e3b-48bb1db83555 | -15.61871 | -43.04495 | 2025-08-27 11:57:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5d015c9b-08d8-36eb-aa51-39987075cf33 | -15.6226 | -46.17004 | 2025-08-27 11:57:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 49104375-1d01-31a4-8dc5-7eeda18728cd | -10.69067 | -47.12981 | 2025-08-27 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| f955dd5d-4d2a-3a93-88b6-28f95544b8ef | -10.66518 | -47.17061 | 2025-08-27 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dbab0efd-fa28-3b54-8515-3b30a26cfcd5 | -14.09382 | -46.65593 | 2025-08-27 11:57:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 60f599ba-5d58-3796-accc-0943d8c3ac53 | -12.65912 | -45.3153 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4aec5f0e-ab8f-3c9f-975d-12cb0ac1493c | -14.13311 | -45.40374 | 2025-08-27 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| afc3aa4c-7a1c-3bd4-a848-c5556d7a4546 | -13.45185 | -46.97179 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3618c61d-50db-3495-8c7a-52ad6dbc1aa5 | -13.38018 | -42.45996 | 2025-08-27 11:57:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 77ce4e13-9d39-316d-aa02-e9306b6460c5 | -12.7425 | -48.07393 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e8df131a-a2fb-3aec-a223-84c4ac307185 | -11.32625 | -43.49517 | 2025-08-27 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a096cd8c-7952-3af8-bfae-4d09683f3b0c | -14.1313 | -45.41516 | 2025-08-27 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| b16f1415-3a09-3910-a10b-46528cc07408 | -14.39013 | -51.94473 | 2025-08-27 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3d8c8437-d664-38b9-aaab-a4c31a40674b | -13.92694 | -40.80761 | 2025-08-27 11:57:00 | TERRA_M-M | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 7b6a6107-604d-3912-82cd-1a098817f5bf | -13.45387 | -42.38776 | 2025-08-27 11:57:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d65babc7-60b7-374f-8da9-0afd4b3f97bf | -12.75034 | -48.19778 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5bb89baa-d80d-33bb-97a4-e805cdbde3f1 | -12.9225 | -46.31482 | 2025-08-27 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73ed1036-b447-3d37-9681-672f99d5b6d4 | -15.92933 | -44.79439 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a2e4ec28-6d3a-391a-ae99-0f99414eeaca | -9.95477 | -46.49494 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 884a12db-dc2b-36ed-ae25-934d63463c61 | -15.62066 | -46.18223 | 2025-08-27 11:57:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ac94145e-2803-36a9-989f-3ec2c0a9bcec | -13.40314 | -46.91349 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| bfb64633-dbf7-3fda-858f-355e1b53e8a4 | -14.12326 | -45.40215 | 2025-08-27 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f9703415-35b3-33cd-a6d3-31a8c2842892 | -13.45985 | -46.85262 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3d1e04d5-9ce1-30f7-aac8-6d2fee517292 | -12.74483 | -48.08101 | 2025-08-27 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 480fe9f9-d0bc-3e21-8bff-ac88c9b4be55 | -13.76263 | -42.10167 | 2025-08-27 11:57:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 66c96a23-5316-358c-b724-8461592a5aeb | -13.61937 | -48.19318 | 2025-08-27 11:57:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 5e1b01ed-d9f6-3b74-9173-318368a125e2 | -13.07277 | -46.32438 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9c012d4c-5679-39af-a343-86d100dbf403 | -14.63006 | -41.24738 | 2025-08-27 11:57:00 | TERRA_M-M | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README91.md)
