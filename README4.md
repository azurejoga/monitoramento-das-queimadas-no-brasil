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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f4977ec-d118-3b02-97e4-94f1e4696cbd | -3.2096 | -50.9105 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f011892f-9715-36d5-a03d-fab29b60113b | -3.1644 | -46.592899 | 2025-11-18 00:11:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20b15450-b475-379f-9ebf-d49e07aa8c30 | -3.4734 | -49.980598 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60fab3ed-057c-3225-a057-11a56e431f43 | -12.8482 | -41.456902 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc9a17c1-1965-3619-bff8-02e3647d56b1 | -7.8275 | -47.146999 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3d08e3c-3807-3646-854f-333d4d9d0fdf | -10.8373 | -46.736801 | 2025-11-18 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 124fe7bf-3ce0-36f9-99ef-6c2795ee4c9a | -3.2705 | -52.4636 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91a4beef-d178-3b59-b823-0e665bd92d39 | -3.0647 | -45.402 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0f4aef-b1a9-335f-bfc6-f38b0b5da5c1 | -11.8437 | -47.5881 | 2025-11-18 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 291a7271-06da-37eb-abf8-f5b10c266c8a | -13.8569 | -43.870201 | 2025-11-18 00:11:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93da916a-aac4-35c8-b1ad-0fb42a6d6c9e | -5.4732 | -44.688099 | 2025-11-18 00:11:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1f165b2-21b7-3292-9148-28cd40a8f11c | -5.3863 | -50.4734 | 2025-11-18 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfdc2e7e-40d7-31a9-b35c-58cef76721d3 | -8.2112 | -45.018902 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60664181-ac3e-33d1-8084-4290b64d9eb7 | -2.8519 | -49.601799 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbefbc0-09a0-3044-ac7a-75f329a50353 | -3.5295 | -49.091599 | 2025-11-18 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87c4d4e1-618d-3c92-bfd9-aef0491af301 | -3.24 | -50.497398 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90ae15f0-6e9e-3460-90ba-e84f5bace0df | -3.0815 | -51.255501 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f451bc05-6216-317d-acd0-c10aa53ab6b4 | -2.9259 | -47.845001 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0136cec4-a59e-3e65-9514-cd6ab9127b4a | -3.7501 | -50.933399 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d867e494-5cfb-3f10-b778-046ad8bac566 | 0.2691 | -51.059101 | 2025-11-18 00:11:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f481a48f-fded-3c6d-ab5b-a53b5e9bdbf4 | -8.9362 | -49.830898 | 2025-11-18 00:11:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5ff5048-597a-3851-8db9-16b18d240fd9 | -9.7286 | -48.904499 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f056154-8815-3e1c-89fb-68800692e82e | -12.6991 | -46.7645 | 2025-11-18 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcc23271-1b08-391b-8da7-edc530dfa027 | -9.0413 | -48.546398 | 2025-11-18 00:11:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 81daf5c6-39ee-30d6-9c39-6f835b57ba4b | -2.6029 | -45.3195 | 2025-11-18 00:11:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd29307-21a7-36e9-ad97-b22e453e80b9 | -3.3637 | -50.1786 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcb558e6-4675-3708-b7f2-88d2c9a26506 | -11.8449 | -49.222801 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e962b8e4-466a-365c-bd33-7c39954e2297 | -1.7632 | -47.175999 | 2025-11-18 00:11:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32cece9a-1737-300d-8425-5a2e3c3438d7 | -7.4013 | -42.739201 | 2025-11-18 00:11:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| daf0eeae-ed85-3409-8fe1-cd27253f53ec | -3.5122 | -50.334599 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e55cfcca-c37f-33ba-975e-f3643255af6f | -10.3813 | -49.906601 | 2025-11-18 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0887a0b-f150-35dd-8022-5930efb68f8a | -11.713 | -48.854801 | 2025-11-18 00:11:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 189c805d-de11-339c-87e4-550ff309d81f | -2.8602 | -45.230701 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4667fc9f-aa57-33a2-85c8-4ea9f230ee60 | -10.5741 | -48.449001 | 2025-11-18 00:11:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99d6b674-a819-353f-9342-8883cef9c943 | -3.5115 | -51.3368 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8626f8-09bd-37b7-a133-6b39d614fbdb | -3.4224 | -50.347301 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e397d4a8-59fd-3b19-aa1f-8da815869f51 | -3.6596 | -51.7677 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbdb0ea-86b1-3030-b236-136423762d4c | -5.4034 | -43.040501 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 055cab5b-528e-3cc7-9042-334e4c3c3add | -2.0156 | -46.928398 | 2025-11-18 00:11:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d51caa-bb55-3e8e-b4cf-4aa83ffa2571 | -3.3524 | -50.173901 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba1ec90-34de-392c-b8e9-bd3d77319fb0 | -2.8504 | -45.232899 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91e25ad6-7be1-345d-8f8b-72d0652d86f2 | -7.2995 | -45.752899 | 2025-11-18 00:11:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24b91370-3c1d-337b-97e5-72cf5b4ca779 | -9.0322 | -47.456402 | 2025-11-18 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c581fe5-4649-3afb-b1a0-e26c9dcc8bc7 | -12.8414 | -41.471199 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 309a5d91-9943-3f61-83d1-7294f44b3a2f | -6.9435 | -49.659599 | 2025-11-18 00:11:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3de6b8-f6c2-38ee-bf3b-10ede05fcc32 | -3.1746 | -48.0308 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5633eb1-1cae-3271-94ed-91fe89add23f | -9.4009 | -48.450699 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4beefb-b3b5-325c-81e4-cbce5870f554 | -12.7331 | -45.423801 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48c6a06a-f602-37c7-96ee-6ece9e6cd194 | -3.5311 | -49.0984 | 2025-11-18 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e22f9e-22b7-3a77-91eb-5c280bc9132d | -3.142 | -49.881599 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3c7c12b-6bf4-3092-a759-a9f13c2b8aa0 | -3.1435 | -49.888401 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee50a2f4-beb1-3ef1-be3b-94edac93b4ad | -8.7821 | -44.3764 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad8bda48-53a8-3bed-b607-4e38b5cce9df | -4.6444 | -46.5313 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb37dbe-812a-3753-853f-59dc5a9de6b4 | -3.19 | -50.640701 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d110e2c-3e20-3d04-97cd-695a8aec7c95 | -4.174 | -50.209499 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adbbbd29-bc06-3058-90f0-568fe7393473 | -10.3562 | -48.9044 | 2025-11-18 00:11:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b841c4ea-1bb0-3649-98ef-90c0d1c9fca1 | -15.4717 | -43.183201 | 2025-11-18 00:11:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 39afc564-150b-3665-bd9c-90863c01471f | -3.2501 | -50.678902 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6749370c-4835-3b82-857c-1eb389d6d121 | -8.0573 | -46.845001 | 2025-11-18 00:11:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00ccc891-4fff-3b84-b0de-918bc49aa89c | -4.4162 | -45.900799 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c88dc6a-4252-3dc8-8e06-39a8aeccde0e | -4.4951 | -46.688301 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 094d6c79-dcf2-3824-9514-9efd8eedbe94 | -6.4387 | -43.800301 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86b8691d-277f-3b9f-8a24-a21ea64a006d | -5.5682 | -51.1959 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45919657-bd9b-3a95-ae71-dbaa3b79e00b | -6.1516 | -46.094398 | 2025-11-18 00:11:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2af2c397-5bf8-3f7a-b93d-90c884a70a70 | -7.148 | -49.102699 | 2025-11-18 00:11:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| af59b490-e6d5-3f29-be2f-42ca0e211190 | -13.324 | -43.497898 | 2025-11-18 00:11:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36a16ebc-d7fa-37df-bd39-8494a60fc35b | -11.9295 | -44.809299 | 2025-11-18 00:11:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55c70ea5-0e11-37de-8a57-0e2a6daba630 | -12.2379 | -49.376999 | 2025-11-18 00:11:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16222db3-3999-376a-a913-9d60f1385a14 | -12.7314 | -45.416302 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b84d212c-236f-3277-ace1-77609badd296 | -3.8015 | -50.110199 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d2d302-a0c2-3471-8433-719a944d4540 | -3.1633 | -50.158001 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1961d9e4-1da1-3773-a719-3ba7ef8df46c | -6.2216 | -48.0592 | 2025-11-18 00:11:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be897e58-f282-3cfd-87b0-f1983bb5ba01 | -9.0479 | -45.419601 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee814399-eb42-3169-88f6-a75453b2c413 | -0.8873 | -51.979698 | 2025-11-18 00:11:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 29a72228-d836-3ea8-87fc-233c0cde2446 | -10.8507 | -44.262199 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8584fddb-0e12-3a44-accb-880e15177df4 | -4.0128 | -47.415699 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc377783-b7f8-3bec-8296-3eabf08102f4 | -13.829 | -41.784901 | 2025-11-18 00:11:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b01a08d3-4150-35d4-b6ce-c5308f85af22 | -3.1452 | -51.310101 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13e574e-9312-3ce0-98d9-dfe2efcf6d9c | -11.5728 | -48.127102 | 2025-11-18 00:11:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6c21e0d-f842-3d59-aab4-39dbe6351aa4 | -2.5138 | -47.800098 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e1a420-ddfb-3f50-9d0a-d6b1c932d93e | -3.1337 | -49.890598 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0739854d-576d-3aea-ace9-0df8f1d361dd | -4.5189 | -50.323601 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f026ae6f-282e-30ce-b139-7163a4fbb1f2 | -2.4916 | -49.330799 | 2025-11-18 00:11:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e05a6d5-757c-366b-a6a8-0b0d2684c867 | -8.8666 | -47.317699 | 2025-11-18 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 624d233f-25a8-37ca-b941-c9c031d68f23 | -3.4852 | -55.409901 | 2025-11-18 00:11:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6332547-92bf-3895-8dc4-00746a4b29d2 | -5.4131 | -43.0382 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5097c4f7-cb37-3c8d-a7f6-4039d8767663 | -12.0064 | -49.256599 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f805eb2-15e2-3ade-80e2-b33c2ba3c801 | -4.1643 | -44.244801 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53fbbd91-4300-304f-9974-53ee0df75af4 | -6.4411 | -43.810699 | 2025-11-18 00:11:00 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae87c2f8-49ee-306f-92b4-b962fd0c9f41 | -3.8933 | -47.928799 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec8295f8-bfe3-3e60-84ae-5beee8e30c93 | -11.9257 | -44.793301 | 2025-11-18 00:11:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed0b085-7626-3666-9ad0-5b53223aecc4 | -7.6962 | -46.8442 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c22687a3-bee2-3cb1-8b8d-33b100d534ed | -4.1911 | -44.227402 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99544d3f-5891-376d-9ff1-a2c6b8132b53 | -3.2391 | -43.018799 | 2025-11-18 00:11:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c67075d9-83d8-3f93-baf9-92b357209edb | -8.5435 | -46.046299 | 2025-11-18 00:11:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9a73ae8-a584-3b7a-8aeb-26a3853b1482 | -13.3219 | -43.488998 | 2025-11-18 00:11:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4d788a6-fc33-31aa-a634-3e337743cfc9 | -5.471 | -44.6786 | 2025-11-18 00:11:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4c6d39f-fcc7-3d7b-aa68-52a244bbd42c | -10.0903 | -44.7593 | 2025-11-18 00:11:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6db647-26c2-3dd2-a492-f40697df08ab | -4.1568 | -46.8302 | 2025-11-18 00:11:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 415fbfa5-e197-3763-b035-1db8f102fe03 | -9.7266 | -49.127399 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
