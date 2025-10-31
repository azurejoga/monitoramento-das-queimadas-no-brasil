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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6dacb0c-e4f2-38f0-a719-a260378269c9 | -8.10584 | -45.17674 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3844897c-798a-32e1-9d92-fe8b4c781235 | -8.05147 | -49.63702 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2029a9b-941d-3837-a56a-5770eee70a8a | -11.31418 | -51.4472 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc89ac6f-c970-359b-a824-9612f48dce89 | -10.75 | -47.83091 | 2025-10-31 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 477ea397-e52c-37f4-b5cd-01f324f59ebd | -8.09418 | -45.1402 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 767c0a0e-b1b4-35d9-854b-f41ddf5c770a | -7.61108 | -46.47825 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7887752-835c-3eb0-affd-db8ab9885316 | -7.6666 | -43.59631 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52a687cc-f3e4-3f79-a2ed-8fa16bac4f76 | -11.63999 | -44.04328 | 2025-10-31 04:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96a4431f-40bd-3216-8fb9-ac2735ffa71e | -11.12885 | -50.7434 | 2025-10-31 04:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a482538-8ac9-354f-a43f-eaeef99726ce | -7.87112 | -47.82455 | 2025-10-31 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c185d3c-5eb7-39a3-b77d-6800c161c3e5 | -10.93197 | -44.76383 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63dc101d-11f6-310a-82c9-6a197e620bda | -10.5338 | -53.70905 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92e2c7a2-cf42-3c9d-b645-3d7cee0aa0fa | -8.32457 | -47.92668 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d18e4850-7886-3802-b73e-4217d28ccea3 | -7.03237 | -47.62162 | 2025-10-31 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74149375-4658-32aa-8aa9-9ab9111acd77 | -8.62357 | -51.58677 | 2025-10-31 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b1202a-0e5b-38d1-aff9-7997b6629f47 | -5.20597 | -56.10011 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04f60248-554b-3107-95f2-d935cc59b742 | -11.17567 | -47.61619 | 2025-10-31 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08fd29bb-557b-3fb6-b83f-ebd00536bdc4 | -12.10959 | -47.11821 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 542fd4a4-dc2a-3140-a8f2-185c0f9c93e1 | -11.55812 | -47.07967 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0938741-c58f-33e9-b029-f033f5674249 | -12.94049 | -47.93412 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f38d370d-82f3-3c3e-a5bf-eac912e445d9 | -12.16076 | -48.00491 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b1949a0f-2296-39b8-8959-634a09b2ff3e | -7.31847 | -44.94881 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 938673ad-e910-33c8-a161-91232c2f0cf8 | -10.42294 | -44.32538 | 2025-10-31 04:57:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f787ae7d-15d1-37bf-9dae-64df4ea73734 | -12.27892 | -48.06883 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37272980-ee79-3ec5-aa40-e877dc23f923 | -14.08327 | -44.1608 | 2025-10-31 04:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa01b07f-097a-3494-a604-d608d1e3a9e0 | -10.92753 | -44.16151 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1300413-ea9b-3849-a67e-0b01283ff3d5 | -7.0834 | -44.94109 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ad86bd2-16e6-3813-a8e2-1d6890c7fe64 | -8.09867 | -45.14783 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82bc5c80-cea5-38a1-a9e7-e6f89898fe66 | -7.74117 | -46.74352 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3297cdf-8300-3829-ba20-c10e2f3ac5e9 | -8.09286 | -45.15038 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc7fd611-da48-3894-9134-9a866ab38183 | -9.86209 | -44.84908 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c1b7eb65-6302-3c79-abed-57a6abd97a05 | -7.64765 | -43.58659 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 286eab3b-d8d0-3c59-b98d-93c6f7ae697a | -7.07357 | -44.93272 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfaf770f-9b1c-34cc-8ec6-c6501cda35da | -8.33287 | -47.93231 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a18eba-c65c-3a67-9f1f-413ba8093784 | -9.86161 | -44.85293 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 858bb943-e1d5-3e41-8370-bc48a3dbb56b | -8.08344 | -45.13854 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff3e59d9-2913-30f3-906a-4df5ea2510f0 | -10.93404 | -44.15774 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 44b58b2c-b298-3df4-99b1-c4d79451936a | -8.95809 | -47.51786 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7da964b7-307a-3fed-aae3-dcc1e57b1701 | -8.09721 | -45.13812 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b313e9ee-8d9c-3f43-baae-ae178ef6ff3c | -7.80742 | -46.39263 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08fc455c-3edb-36d2-8b5f-2ecaf2926f44 | -12.93577 | -47.9331 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90460da5-7731-391e-883a-ced63c52f2b6 | -7.66057 | -43.59632 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a9b2bc13-86f3-301f-a9df-1e36fec20bc8 | -8.55608 | -47.78065 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b29e9b0-9c17-391b-86df-73afe50da63c | -6.51928 | -46.90609 | 2025-10-31 04:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d42a3c1-443f-3f11-8893-f861d70a3c6a | -7.87497 | -47.82958 | 2025-10-31 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 951dcf5b-a7ff-381b-a5f6-4d321d7c8d46 | -7.35086 | -44.9927 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 737f1937-072a-3f34-b9b0-f40913d46139 | -13.59616 | -47.34663 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17ca4b34-0979-3a7f-9a01-d55232a5280c | -8.31531 | -45.37719 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62f6de1d-268e-386f-8f63-9c2c4b233def | -12.29371 | -43.78136 | 2025-10-31 04:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c54e79dc-d4e0-33bf-b53e-10ee2bc8b596 | -10.42929 | -44.32202 | 2025-10-31 04:57:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae114056-4340-32eb-b53c-8c1dd92c0473 | -6.2246 | -49.05222 | 2025-10-31 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861c540d-219a-3257-ab38-8fa1ff52c5ca | -8.08881 | -45.13935 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53374d1a-e81d-3c0d-9803-55b6792eafc6 | -10.53836 | -44.78434 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 24c0d652-2c58-3272-ba51-de88e2e06fa5 | -7.9248 | -46.79406 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c140e7-4057-31b2-b45c-b0fb4a34935c | -7.88204 | -45.68961 | 2025-10-31 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 599f5fe3-c008-3514-8f56-7048bb8c56c4 | -8.16616 | -45.49323 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 782ff460-9300-3ffe-8d9e-a2ef85c58e38 | -7.62764 | -43.57199 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec6a91b8-5149-3e28-a721-c9f0501ff19f | -7.91633 | -45.70814 | 2025-10-31 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b0aec2-bf07-332a-8512-f968680d45b3 | -14.08248 | -44.16039 | 2025-10-31 04:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac4931ed-e48b-35cd-9362-e63135fc7735 | -8.31576 | -45.37374 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 183c57ee-1348-3386-ab1a-9c9e20bd96d1 | -17.13423 | -55.74868 | 2025-10-31 04:59:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 52470932-f853-3104-ac44-14de0f373387 | -13.24075 | -54.3628 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf45390e-df30-3dc7-b7b3-8de79cd78837 | -13.24241 | -54.35188 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e7df747b-ed7d-3fa8-9068-93b5310910f3 | -13.23516 | -54.35446 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b2a3b48a-7b58-381c-a481-f6addb8f8fb5 | -16.3309 | -56.54469 | 2025-10-31 04:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 9227261e-fc4a-36e2-a7da-00fbf5287127 | -13.24017 | -54.34406 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dea06c23-d9d4-3b37-9a82-8e1d6443e07c | -16.7655 | -53.83337 | 2025-10-31 04:59:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82a4be9e-3676-3af1-abb9-d6f59d4f9582 | -13.24856 | -54.35659 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 02c17d6c-b023-37a8-a76c-e2301e652255 | -13.34729 | -54.28601 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03438d8a-9812-3c65-9b8e-77e4995361ea | -16.36676 | -45.25077 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7013521c-d4dd-3d14-8682-fed765b0e1ee | -13.25246 | -54.35349 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4f90b3de-bd01-3638-be15-18681a15bb20 | -13.24911 | -54.35295 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ad0af26b-e403-366c-ad77-6be1dc62da60 | -13.23402 | -54.33935 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8ad2a4d-17ca-3177-acab-b8ea5b552d0e | -18.29075 | -54.28983 | 2025-10-31 04:59:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5e247b8-fb9f-3a42-a03a-9e9e5c71120c | -13.23906 | -54.35135 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 792b078b-80d2-378e-9bc2-ec6b8679bc62 | -15.00533 | -46.31507 | 2025-10-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0105ff08-1336-3dbc-97e0-2dfe1cf502f3 | -13.24631 | -54.34877 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d2626af-5448-3497-acca-1c57f38a0952 | -13.24966 | -54.34931 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d4599ed-24b6-3cbb-b99e-6ae700419827 | -15.01117 | -46.31238 | 2025-10-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6a5d3e8-8997-33c1-b44e-159e4b7bfcd3 | -13.2318 | -54.35394 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c420c016-fb3e-3a07-ba2e-9894c1c91c83 | -13.34784 | -54.28235 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5da2f88-59da-3596-9fa9-505637698835 | -14.74802 | -46.58586 | 2025-10-31 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ed6ca15-dec5-3588-954c-bddf6fd98eda | -13.23737 | -54.33987 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab78a098-88de-31d2-9bdb-a3cc1d52ca26 | -13.22455 | -54.35651 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcd2db28-4fee-3ecc-9ffd-f8421bd8c1c9 | -13.2441 | -54.36333 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93c1b04a-0132-3ae4-becc-711baf6cfe12 | -18.29018 | -54.29385 | 2025-10-31 04:59:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4f8c1a6-7903-35be-96ae-5cd3b63f390d | -12.61977 | -62.03341 | 2025-10-31 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef16011e-cf15-3ef3-90cd-575c91fd1547 | -18.28726 | -54.28928 | 2025-10-31 04:59:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99c738de-79f0-32e8-91c9-22d9adf6a6ca | -13.2307 | -54.36121 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1971362-1b9d-3bce-9977-02fd88aed9f1 | -13.24521 | -54.35606 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| d7541fc5-4170-3d90-a404-8c3468986991 | -13.23851 | -54.35499 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d04e7b98-3e60-326a-ab2c-de4b0a9df995 | -13.23571 | -54.35082 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1f2ed5e8-9044-3ab9-88b3-6e0c6910d7ab | -15.00454 | -46.3125 | 2025-10-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0990220d-889e-3e2e-970d-726bad5e38f2 | -12.14287 | -64.08911 | 2025-10-31 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 158637e9-4f0a-3b2f-82cc-e7f39eca5cd8 | -13.23125 | -54.35757 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c6a2f4-0f94-3037-b961-86241324dc2a | -13.22371 | -53.87028 | 2025-10-31 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfa9ef06-6e2a-31a9-a388-e4066845240b | -13.23796 | -54.35863 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5653ebe3-4293-3aff-a932-520d4e3a63f0 | -13.22956 | -54.34612 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69e016b1-ac4d-314f-add6-a83b3ef86165 | -13.24466 | -54.35969 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06858e38-bc44-30b4-9101-4185004dd090 | -13.22735 | -54.36068 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README40.md)
