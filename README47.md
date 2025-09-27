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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3e80a1a-c91d-32c2-b5bb-14dff89524b6 | -7.60431 | -43.05474 | 2025-09-27 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d599081e-fe08-3026-8891-6857d490ef01 | -4.64602 | -50.96433 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8c4c4cd-d04b-3d60-955a-55e7b0f35d69 | -6.54155 | -43.8266 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6bf95af-062e-3a00-9678-d6d71b0d822c | -9.97787 | -43.57364 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e761bb5a-6fdf-3b2b-9f67-c4c02dd64dea | -5.28018 | -45.03361 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae96a82d-0f96-3e75-bf5f-165f026900fa | -6.31739 | -43.38559 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8250a089-7346-335e-8965-5d9aa012cca1 | -7.28846 | -42.97525 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| faf3adb5-8743-3231-af10-02c97528ae41 | -6.19653 | -44.24075 | 2025-09-27 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e39c8656-fd06-3f04-91ec-620f46da13ba | -8.86028 | -46.61422 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab95152b-9965-3d58-8eb3-29a76f60dbd1 | -7.35306 | -42.09607 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a7b081d9-fe10-3cc5-af57-a1de34f943e0 | -7.86536 | -45.29506 | 2025-09-27 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d8152d0-ca29-3344-969c-0462d7cde751 | -6.2554 | -42.47601 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 105f94e3-d4b5-39c2-a519-b47c5ee12368 | -6.31622 | -43.39263 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbda3a59-e76e-3eb2-8749-a372cc2cfeb5 | -2.49392 | -49.27253 | 2025-09-27 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dcb10ad-b23d-3230-b524-566876408ded | -5.08662 | -44.85516 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327d2976-4b6f-351c-bb44-314214e2cbf5 | -8.73535 | -48.85963 | 2025-09-27 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c1364e-d938-36d8-95fe-9837a1208349 | -7.61231 | -43.82695 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e1e5db0-529f-377b-aaeb-4e371377ba29 | -6.06841 | -44.87573 | 2025-09-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b8ce600-a3b4-3699-b61f-1dc868b56b35 | -4.70427 | -40.41903 | 2025-09-27 04:44:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d5e5f48-fb12-3e4f-87f9-7c8d69324060 | -2.26533 | -47.85952 | 2025-09-27 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e23e090-1750-3c7d-945e-683b1de609e4 | -6.42814 | -46.16434 | 2025-09-27 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75246789-ab7b-3ad1-ac37-04915108df1d | -6.99096 | -42.3908 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bd44fe1-0315-3e6a-a09b-026f6e7e05fa | -7.34728 | -42.09867 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5420a487-7249-3ba7-aac8-6e24feb17e3c | -4.48112 | -47.67139 | 2025-09-27 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d04b762-9dd5-3075-b0bc-c0dd9be91943 | -6.23995 | -44.13088 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02141485-32e0-3833-85dc-6683a5dc8359 | -6.55153 | -43.84516 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 42471374-1e30-3702-91a5-e5d2c109a3d2 | -6.69731 | -42.74902 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6358684c-03f9-3f3b-8015-7ef004e4873e | -5.76369 | -42.81174 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53185a4f-1280-30ed-9556-ae1a53bca1a1 | -8.82492 | -46.26032 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d08cc475-c128-349b-9ac6-d003d215a581 | -6.76121 | -45.62897 | 2025-09-27 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a061435-9bb4-309b-b444-fe03d1f8d1cb | -8.72915 | -46.68681 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb0a0a30-b3ad-3de9-ad6b-21c7a53f085d | -6.53621 | -43.83067 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc5fe174-b43b-35d2-abc7-e4e9e533b843 | -5.25764 | -46.16667 | 2025-09-27 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0129b778-4eaf-339b-a776-f8828e9aad4b | -4.64933 | -50.96485 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5bd81c5-78be-36ab-a218-f56a0ec29c41 | -6.70231 | -42.74992 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05ac38ec-f20b-31ad-b8f3-e998e161df93 | -4.59281 | -50.65583 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47e9d2d5-578d-33bd-af78-1f7e52c1449c | -8.49478 | -47.85417 | 2025-09-27 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e9fb20-71df-3274-9345-2f5fcefec1bb | -4.64878 | -50.96831 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4ce4ae8-599b-3ee7-aeef-752797df8e42 | -5.57411 | -51.6459 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 273d46bb-bc35-38f1-b5bd-c350063bac63 | -8.26989 | -44.93391 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6179c68d-ab7e-3321-b752-64bf3f45386a | -2.45105 | -49.0257 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ded7d8-9617-3c60-8749-3d616c1cdbd1 | -7.94027 | -45.20109 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f0193c-adac-389c-9130-87eb1ee97b14 | -4.37239 | -48.20666 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5fadadc-a3d4-3b38-be9c-8ff1996235b5 | -9.11116 | -45.87982 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 694a07d5-bbdf-3fe8-b490-b88b9ee2f6cf | -9.11224 | -45.87221 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 175ecaa2-e2fd-3934-9de9-678e0ac2c591 | -7.64352 | -46.77504 | 2025-09-27 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 064818da-01bf-3cbd-99bd-1f394572ba5b | -8.82032 | -46.2634 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08301aaf-e619-3c52-9b22-90f690e71be8 | -2.83377 | -54.56002 | 2025-09-27 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8cf34d8-9aba-3ec6-bb16-2483fb4a125a | -7.28806 | -42.9781 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 35173783-267f-360b-8207-708eadc1da35 | -7.05141 | -43.027 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a61142c5-780e-3b36-9433-6fe48595cd3b | -2.49446 | -49.26905 | 2025-09-27 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 460d6362-6c23-380f-977b-dae158fb4b5e | -4.00794 | -46.965 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14cf18b8-4ff3-33b2-a50e-e57c40e234de | -3.3356 | -50.24935 | 2025-09-27 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e922c1b3-ab36-36fb-9255-656b2e833017 | -4.38336 | -41.92243 | 2025-09-27 04:44:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e05cafbf-827c-3235-893e-0e3d7b3bfb5b | -4.45063 | -40.97858 | 2025-09-27 04:44:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| acb3f090-a862-3b8f-91a6-ce1c26ddea0c | -6.70903 | -42.73892 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c420d35c-d0c9-3175-8417-4111f142d1cf | -5.7308 | -42.64682 | 2025-09-27 04:44:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e938bf6-a75e-3257-82b9-a934e549e83a | -6.06451 | -43.20737 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7bcfb5fa-01fe-3211-97a2-6e87146c715d | -9.05014 | -45.51453 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8812a142-7899-34a4-97c1-92fba4d0aa0e | -5.08238 | -44.85451 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 02fb9c60-8c62-37b3-8369-09419f4cbd70 | -3.82212 | -40.35287 | 2025-09-27 04:44:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e81f294-74d8-3fca-879b-89f5dc8df48f | -4.68318 | -46.44675 | 2025-09-27 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bbbd93b-fbc4-35a6-9001-0d9c0bf15218 | -8.72518 | -46.68624 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa082307-4c1e-3314-8723-9b21d7ea83b8 | -4.57435 | -44.07423 | 2025-09-27 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a910cfb4-e2a8-3f00-b836-d8f2527658c8 | -7.80748 | -46.96022 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afdeb066-54d9-3644-8b8f-c9dc4a036f98 | -4.61295 | -43.10471 | 2025-09-27 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 862ee4f7-d373-3ad2-8def-2de2c3443fc4 | -2.30471 | -48.14381 | 2025-09-27 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a8b8166-f79c-37f0-9c88-bf72e2a875f3 | -6.70189 | -42.75284 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33084495-9872-3972-b810-d2b88dd780c8 | -5.97402 | -44.12928 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8677416b-f35d-36d9-9261-55c130e1839a | -7.87885 | -44.01933 | 2025-09-27 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21e74a8-e95c-33a9-8c61-7e0458a84b9d | -3.69997 | -49.01214 | 2025-09-27 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d9e435-309e-3295-967a-24917fc6455b | -1.62554 | -55.16489 | 2025-09-27 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c4835f6-1497-38c8-9b69-3aa39608d8a3 | -9.9952 | -44.17361 | 2025-09-27 04:44:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97f1d0bb-4906-318f-ba20-ddf308578291 | -5.94162 | -44.88375 | 2025-09-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61f611ba-b90d-3570-9488-13c89e72ec5d | -6.76536 | -45.6295 | 2025-09-27 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f59a8a01-57e6-38a8-929a-3dea1ec91238 | -3.58322 | -49.08495 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e85407d1-3a8a-38b2-9cbe-e1b4756455d9 | -3.33175 | -50.25227 | 2025-09-27 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0f43bc1-d256-366a-b25e-4ae5050090dd | -4.59226 | -50.65928 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4cf6f763-51c5-3041-9f5b-32bf14acb249 | -3.15795 | -48.60548 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 705fe7a2-8b84-399d-b08e-367f7cf43b58 | -5.08117 | -44.86256 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 02a6d5bd-2e7a-311f-8300-01f7d6f29a1e | -9.18591 | -46.64404 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 85926c4e-2aba-32a0-b1ea-318ee7a0a927 | -5.8016 | -42.82872 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6aa40a17-3df0-3e59-a2ea-c9a6fee32b9f | -6.80948 | -44.47359 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 169ffe7c-48ee-3ac0-bea3-37ef1b989057 | -9.1117 | -45.87603 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95f88f16-11c9-3289-9e76-16bd8bfad3cf | -8.8306 | -46.22006 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 732f1bf3-8717-3081-8035-7e2b36b8e839 | -5.5493 | -45.05545 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e37480de-40ff-3a87-b36e-f44681ae811f | -6.24003 | -44.09796 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 726645d3-74b4-3d4f-8c87-69f3e9d55bc2 | -9.96751 | -43.61345 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b187a723-ef83-3f87-bbf9-0dc089d78302 | -4.45014 | -40.98199 | 2025-09-27 04:44:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 850661f6-90d7-3d9e-83a2-9def52343050 | -4.48006 | -47.6746 | 2025-09-27 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b50bf12-7c6d-3baf-a5b8-1d7fca5c54db | -4.60819 | -43.10403 | 2025-09-27 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5bc5a72-5af6-3da4-9659-3d8bf6d86bba | -1.83813 | -52.07784 | 2025-09-27 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17abac03-a5d2-3dc1-8f84-2b3cc358e0d9 | -7.75887 | -46.88859 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c49545c-91a3-3801-927d-41946974ca98 | -4.26542 | -48.55544 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba56b798-1e00-3f1a-b8c0-c3072222a5f4 | -6.99055 | -42.39385 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea98893c-53f0-3ff2-8c9d-03756c446b95 | -2.14282 | -53.64655 | 2025-09-27 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61638fce-c08b-3f9e-9f46-758d466a9fac | -4.71606 | -50.95057 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 552e057c-b388-3d90-bee4-faab07c9f5d0 | -6.32175 | -43.388 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02878d38-f5bd-3e92-9989-9c7062865a81 | -5.80973 | -42.80739 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bb633cba-f5a9-30ce-b264-11b9390ec239 | -8.83525 | -46.21677 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README48.md)
