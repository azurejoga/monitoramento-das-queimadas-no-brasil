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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e901844b-f316-3704-8f95-d1d817b47c64 | -7.71328 | -45.62429 | 2026-01-08 04:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4c27dd0-f17c-3b54-8a6b-cd1309197427 | -7.5623 | -45.62837 | 2026-01-08 04:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6cd7502-6638-34b4-bc73-5dd770fee853 | -8.81857 | -39.83127 | 2026-01-08 04:16:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1599a908-0ae5-3343-b0c1-12ce811b8add | -11.9572 | -44.20999 | 2026-01-08 04:16:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8086913a-bb50-3a59-88fd-107fbb65463f | -9.99047 | -44.74776 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9bb43be-2992-3589-9724-8b56fac607ab | -7.56496 | -46.48271 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a912379-6970-3dbd-8ad3-7d9fd85982de | -7.7139 | -45.62053 | 2026-01-08 04:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e16719e-fb3f-3ba7-b569-f7e6534191a7 | -8.69195 | -39.58815 | 2026-01-08 04:16:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3103f3fe-12f8-3a67-8990-679c87e0fd18 | -9.64144 | -42.95572 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb6862f0-c2ba-311b-93c7-3414aa0ed690 | -9.64868 | -42.95321 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb2b9265-becc-3e0f-97ea-781dcb6dd8b7 | -7.56562 | -46.47863 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8579735e-5a00-36bc-9550-e996a3ca9c98 | -9.9899 | -44.75129 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dba1c90-0dbc-3e06-8c0f-caeacbe1007e | -15.14736 | -45.27649 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f114d30-64f1-3e4f-87e8-62db3925b958 | -9.65111 | -42.95378 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e110e209-b63b-3c76-b4d7-1eaf4f1a379b | -8.37635 | -41.85568 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 41aea212-551e-372e-a4d9-8d3f04c0f796 | -9.98602 | -44.75426 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97be4eb3-2795-3a2d-9173-ec3898a666fa | -9.99103 | -44.74425 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07d1366d-53fa-3bfb-a82e-733077563c32 | -8.81866 | -39.82852 | 2026-01-08 04:16:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a83751ed-bc95-3fda-ac5d-3b31e888dbe5 | -15.14073 | -45.27538 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9a5123-254c-3ab8-be89-100c78c3ef6e | -7.56575 | -45.62893 | 2026-01-08 04:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ffb62a-c801-3a91-9621-b421a719dd98 | -9.64534 | -42.95268 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 35e761a9-fee8-3ad7-92ee-a42deb76f2c4 | -7.56393 | -46.48097 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fe2abed-f615-3b2a-90b6-4ae34b42c9d4 | -9.99435 | -44.74479 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 533977bc-109b-3028-beb5-17ff45a6c0f5 | -7.56461 | -46.47689 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fa056c8-8b54-3bf4-9716-ff1140fded00 | -12.17423 | -43.47268 | 2026-01-08 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62d905e8-a354-3892-ad53-cb08c057899f | -9.77609 | -36.56033 | 2026-01-08 04:16:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4a3cac52-4f10-3ac6-bd98-5e787a4aa6b7 | -9.98658 | -44.75075 | 2026-01-08 04:16:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b04a968f-6979-3629-8f8b-68cae3227a77 | -7.56919 | -45.62949 | 2026-01-08 04:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e29cc3f9-ff50-3979-bbc7-bbce6376d6cd | -8.81923 | -39.82666 | 2026-01-08 04:16:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 266d092f-1063-3e92-99ff-b26e70eebfcd | -11.8828 | -44.20885 | 2026-01-08 04:16:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5b191de-7251-3bd1-b5a0-9371e188e164 | -9.77134 | -36.55967 | 2026-01-08 04:16:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1882f105-27fc-3f3d-9f92-95a204ae5630 | -8.82243 | -39.8291 | 2026-01-08 04:16:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0421783c-a88d-3a1b-967f-04157f944557 | -15.14129 | -45.27182 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 969b01c2-31c1-3584-acbe-561e327d2b1c | -10.14107 | -36.20345 | 2026-01-08 04:16:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bf90e330-d5bd-3594-9c37-60d08195ba51 | -15.14792 | -45.27293 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6326562c-c907-321d-9ca4-df55c0f73c6a | -15.14405 | -45.27594 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41befb84-77cd-31cb-98c9-b6e540369679 | -8.37977 | -41.85621 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6380051e-193d-3be5-ac55-576a63b36a48 | -10.17795 | -39.05102 | 2026-01-08 04:16:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30ae5ee8-7afb-31b5-8ac4-c4318dde9c16 | -10.76952 | -45.01568 | 2026-01-08 04:16:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d79b6a4-cbbc-3533-a1a5-f8d48ee4ac91 | -7.5675 | -46.48156 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2215cfec-c8a6-35be-8c68-908004fe4c63 | -9.34258 | -40.46503 | 2026-01-08 04:16:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cfcc8cf0-164d-3b35-8cc0-9565598e798e | -9.4609 | -45.79383 | 2026-01-08 04:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af5aad33-62c9-3a48-95a4-3ecba5da86be | -13.37288 | -43.657 | 2026-01-08 04:16:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb610259-206d-308b-8891-49c6c030d9f1 | -9.65391 | -42.95785 | 2026-01-08 04:16:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 793d3d70-25f7-3885-b244-e9c014b4e748 | -17.87155 | -45.54669 | 2026-01-08 04:18:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcee695a-3939-3134-9437-6de1a538d0d0 | -17.31246 | -44.92799 | 2026-01-08 04:18:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e481b5a-3aa2-35ba-965b-4ffe70d6e056 | -20.7135 | -49.83206 | 2026-01-08 04:18:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27483e33-0606-3039-86f0-5502b7809571 | -20.71428 | -49.82771 | 2026-01-08 04:18:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f0602e55-9602-337b-9a9f-afe3a9bac2bf | -4.2913 | -43.7822 | 2026-01-08 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f219d16f-0a3c-3400-9816-baf486d19058 | -4.2728 | -43.7601 | 2026-01-08 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| d896366a-910e-32e0-ab73-5a7ddcd9eb77 | -4.2726 | -43.7832 | 2026-01-08 04:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 73f5b004-5f49-3272-9feb-aeb3ed9e9b17 | -4.2914 | -43.7591 | 2026-01-08 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6b75511a-6cc0-39bb-9824-f4f2d75db8f0 | -20.89442 | -52.34295 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6376fd9c-b1c4-3d57-a711-16364a1c7f61 | -27.09921 | -50.84029 | 2026-01-08 04:21:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3ebcc2f-4c25-3972-869a-b431fc2eeed7 | -23.61232 | -48.34924 | 2026-01-08 04:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a3740c6c-648a-3e38-bd67-ed4b9d3998c6 | -22.96 | -48.69967 | 2026-01-08 04:21:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5fb091e-0999-3da4-82af-5ecee7e5b5a6 | -24.34875 | -49.42392 | 2026-01-08 04:21:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 55377190-5eaa-3736-a658-b515068cae06 | -22.55679 | -49.87389 | 2026-01-08 04:21:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 63e07a67-1776-3703-8300-56a3e2ba3829 | -20.89236 | -52.33865 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1488a1fe-e3f4-30a2-9824-5734daa75fcc | -28.19469 | -48.70196 | 2026-01-08 04:21:00 | NOAA-20 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f9bd5451-23f4-3865-984e-619180531329 | -20.88605 | -52.34956 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f0de34d8-4eb7-3705-93d4-cc55996cd643 | -27.31434 | -51.04112 | 2026-01-08 04:21:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbd0cf6b-11b9-34c7-a8a1-7046dea86b02 | -21.61925 | -48.94537 | 2026-01-08 04:21:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f582233-553c-334c-af38-efa6bc605356 | -20.89494 | -52.34758 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a741627f-e2dc-3a27-9c11-b07a02ef48ce | -21.53414 | -57.53846 | 2026-01-08 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e507f28-2f69-31e5-867c-408a467ad169 | -22.82438 | -49.29467 | 2026-01-08 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f93e2a5a-832b-3322-907e-ec06a624e205 | -25.0367 | -49.40899 | 2026-01-08 04:21:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4450303-d432-3584-89f8-c411b9022dbd | -20.88829 | -52.3377 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3be633b-8103-3621-9fb6-7f7a41104b20 | -24.34535 | -49.42321 | 2026-01-08 04:21:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7534f57c-99e8-3a95-84dd-9f0f484ee1c3 | -24.88653 | -49.278 | 2026-01-08 04:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b90d221-0764-3b1b-accf-25f35673df92 | -20.88681 | -52.34558 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f01f8dd7-9060-362c-9566-680aacb84704 | -22.82369 | -49.29868 | 2026-01-08 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42b63089-186c-3a3c-bc20-a02a1563944d | -20.88755 | -52.34164 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0ebeb5ee-4b94-388b-aaf5-04cef6ae7fb8 | -24.88585 | -49.28201 | 2026-01-08 04:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97713ce8-5543-32a5-8418-375b5742caba | -23.5791 | -51.45013 | 2026-01-08 04:21:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d8eca27-f8b0-3abb-9caa-7bb944f597aa | -20.89087 | -52.34658 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e2d10bd5-73d4-3277-818d-ce3e1edad4bc | -20.89013 | -52.35055 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e1859ba7-d39b-348a-a26a-86d6a906fd04 | -20.89365 | -52.34692 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0bb28ae6-9ce2-3ff7-985f-2aae2c5eedff | -25.42618 | -49.36992 | 2026-01-08 04:21:00 | NOAA-20 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5d8740f6-e2f1-35e1-8038-8da9123f1b52 | -22.82507 | -49.29064 | 2026-01-08 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db79fd98-6a86-3fbb-850f-8f769b168632 | -20.89162 | -52.34261 | 2026-01-08 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ea2df3de-e744-31fa-b7d9-543b7f7677fe | -22.8278 | -49.29537 | 2026-01-08 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f06960b-323f-38c7-8cb8-8a5f3aa7bf96 | -26.84014 | -50.37125 | 2026-01-08 04:21:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46c9e64b-8070-3c8b-8533-efb659d3cc3a | -21.54051 | -57.53617 | 2026-01-08 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13309e29-c530-357f-9aa0-1de470f7b4eb | -23.57872 | -51.44803 | 2026-01-08 04:21:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8ea403b-9fa6-37ed-b347-68dd0d156947 | -24.34807 | -49.42794 | 2026-01-08 04:21:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ae937093-2506-307e-8c90-5a0ab572aef3 | -25.04822 | -49.40303 | 2026-01-08 04:21:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc1fa8e0-7120-329e-9843-041c0635f6c6 | -25.20502 | -52.39135 | 2026-01-08 04:21:00 | NOAA-20 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3caae8ba-c5d8-3af4-a362-81ed2e7d66d1 | -21.53974 | -57.53959 | 2026-01-08 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14542112-48c3-3710-b7e0-606c38ef8c50 | -21.61857 | -48.94939 | 2026-01-08 04:21:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2395acac-31bb-3bba-963f-640fe70afaa6 | -27.62402 | -48.64103 | 2026-01-08 04:21:00 | NOAA-20 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4c293d0d-0095-34c9-a256-c40c52769f05 | -21.61514 | -48.94873 | 2026-01-08 04:21:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c6caa97-ff31-37bb-a7ec-5f874698d4be | -20.73136 | -55.16562 | 2026-01-08 04:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a887cf64-d1fe-32f2-a2cb-7c8b948825b3 | -4.2726 | -43.7832 | 2026-01-08 04:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 47cd82f3-c2db-311e-8ffe-3401f862410a | -4.2728 | -43.7601 | 2026-01-08 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 06311e88-4e96-3cc4-b273-764d6fd9eff5 | -4.2914 | -43.7591 | 2026-01-08 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3d4747a5-cb5d-38b1-9fdb-5f2b37b912f5 | -4.2726 | -43.7832 | 2026-01-08 04:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ef673396-4839-3775-80a1-cd423a50ece0 | -4.2728 | -43.7601 | 2026-01-08 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 20e4b8e7-a440-3e18-a5f7-f4143028012e | -4.2913 | -43.7822 | 2026-01-08 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7bc824ca-63b9-30e6-9721-03726697c3a3 | -4.2914 | -43.7591 | 2026-01-08 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |


[Clique aqui para ver as próximas entradas](README7.md)
