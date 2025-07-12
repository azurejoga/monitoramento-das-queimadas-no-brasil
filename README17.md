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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a622d5d-f25c-30f2-b40a-300b874d349c | -11.86596 | -52.25532 | 2025-07-12 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77258df3-fea6-3382-8dab-2bb3ef33aed9 | -5.8412 | -48.3964 | 2025-07-12 05:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 2738a277-b65b-386e-b31d-607663bdfc6c | -10.8986 | -49.204 | 2025-07-12 05:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 680f6bd5-210b-34aa-b447-4e542573547d | -20.70612 | -56.66211 | 2025-07-12 05:10:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cb2c076-22ba-3ccd-b38e-04bf932eaafa | -18.66252 | -55.72525 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 04f25641-dd86-361e-b029-fb611e36c017 | -19.02286 | -57.62252 | 2025-07-12 05:10:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a7ea32ba-b9bd-3dc9-93f8-52e99815eae3 | -20.13659 | -50.73081 | 2025-07-12 05:10:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c7486163-c7a8-339c-b59b-e8ada60f637a | -19.09118 | -56.04166 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 136c3688-8794-3acd-bc20-4e71c089e949 | -20.14086 | -50.73727 | 2025-07-12 05:10:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fb3c6a57-e581-3b95-b781-cc6381551e9a | -18.66191 | -55.72947 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 47a77bd8-242f-3c5c-8106-1bdc798bffce | -18.94962 | -54.32841 | 2025-07-12 05:10:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f549c9ba-0769-376e-992c-0f63796c1f29 | -18.95346 | -54.32904 | 2025-07-12 05:10:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4218c9a0-178f-3ab7-a664-5f084f177fde | -20.14151 | -50.73141 | 2025-07-12 05:10:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5078b78b-f8e0-3647-83f2-35d055e622b2 | -20.70525 | -56.66341 | 2025-07-12 05:10:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb57f62d-a138-376d-966c-4eb8461cedda | -18.95279 | -54.33402 | 2025-07-12 05:10:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddcf550b-9abb-3b7e-9fb6-a3a11225d633 | -18.42657 | -53.03087 | 2025-07-12 05:10:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3b61eb5-9329-394d-a1bc-3ac5d5222b35 | -19.09059 | -56.04581 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e8275a1-e80b-30a0-9b19-e58e17b0f675 | -17.69168 | -54.00856 | 2025-07-12 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3819d384-d47b-3f84-9d3a-125777accd47 | -18.4267 | -54.55954 | 2025-07-12 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c530873e-2cec-3f33-9aec-a6ce8f9a73a2 | -18.42606 | -54.56429 | 2025-07-12 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eedfc55-347e-3b43-9620-65fd04951139 | -19.09471 | -56.04222 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0a99399c-2bb7-3024-903f-d096d7dd11f9 | -19.08765 | -56.0411 | 2025-07-12 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c20ee1b9-5ead-3161-82ce-bfb9f266327f | -21.4413 | -54.57727 | 2025-07-12 05:10:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2b52434-7419-3fcb-9d5c-b5449bcede72 | -5.8412 | -48.3964 | 2025-07-12 05:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| a7878c5f-3657-3664-acb7-0eb7298bc608 | -10.8986 | -49.204 | 2025-07-12 05:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8d3ea208-41e7-3e2a-a5b3-c9948c286448 | -5.8598 | -48.3953 | 2025-07-12 05:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 345ee115-bc8b-3bc1-801b-81159cda4b35 | -5.83833 | -48.37837 | 2025-07-12 05:23:00 | AQUA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 9e6ab46e-29ba-3080-af30-5d4f9469696f | -6.25101 | -43.36659 | 2025-07-12 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cc34c57f-dbda-3591-b418-0f0f379350e8 | -11.73084 | -47.46738 | 2025-07-12 05:23:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fb9f762e-f187-361b-adc1-674666574346 | -10.90502 | -49.2005 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c1b2dbc3-0c7a-33ee-a7e9-8d81281e2e3b | -10.89013 | -49.19795 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6200e755-3991-3559-9359-073d0b678861 | -7.98402 | -46.40705 | 2025-07-12 05:23:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2b3dd409-bd2a-3421-a5d1-337392115b58 | -10.88992 | -49.19259 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9e91144d-4dd9-3feb-af6f-9fcbdeeaf4b2 | -7.07872 | -43.50924 | 2025-07-12 05:23:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 94a898da-08f8-3604-86ce-070f343dcca4 | -10.56788 | -49.11242 | 2025-07-12 05:23:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 715ec2de-eab6-3e4d-bf68-494dfe961cd3 | -6.27191 | -43.41445 | 2025-07-12 05:23:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6afc5e80-9cc0-3c87-b539-e36194ffd553 | -10.84301 | -49.11702 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b3fa1eb1-126a-3ecf-80fe-50d881a87247 | -5.83307 | -48.40953 | 2025-07-12 05:23:00 | AQUA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 137b07d4-c811-32db-8ab3-98aeef50e5e7 | -11.4174 | -46.39306 | 2025-07-12 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 861b4911-5879-3254-a7e9-6a868ffdf014 | -6.71324 | -44.32678 | 2025-07-12 05:23:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f3dea631-6cf7-391f-a9e2-766617f9b15a | -10.56761 | -49.10715 | 2025-07-12 05:23:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6b86d52b-1718-3b72-b604-b8e9a1fa24e6 | -7.98324 | -46.41376 | 2025-07-12 05:23:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| bc94344a-0ae1-3d19-8fa2-c5db8031c254 | -10.90478 | -49.19533 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 77a17e4f-37a8-3370-8cb6-463abb046542 | -5.84371 | -48.37201 | 2025-07-12 05:23:00 | AQUA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b107100c-8b78-31a2-b3c5-41225d9234a1 | -10.84607 | -49.09587 | 2025-07-12 05:23:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ba979f5d-9a50-3c61-8045-5a526acb5e61 | -6.61003 | -43.88213 | 2025-07-12 05:23:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 834d652f-ee39-362e-b06b-1fa2e5666322 | -5.83872 | -48.40303 | 2025-07-12 05:23:00 | AQUA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 383e6b51-0452-34f2-abf4-33efe6f65999 | -5.84973 | -48.40053 | 2025-07-12 05:27:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1d7950aa-bf1e-366a-813c-d4cb3423962d | -7.08214 | -49.60642 | 2025-07-12 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edb954eb-7aa4-3ad7-872f-d32494d4d5cf | -6.63155 | -56.27598 | 2025-07-12 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c873f1-888e-396a-8288-fbdc9776caa6 | -8.47147 | -49.61768 | 2025-07-12 05:27:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 755448b0-f545-3853-81bf-60972d00c81e | -8.4707 | -49.62402 | 2025-07-12 05:27:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 38c5d25d-691f-32ec-8f2d-1b43d790adeb | -8.04338 | -50.10401 | 2025-07-12 05:27:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a025577-8a5d-372b-9fcf-e080e2be7ba7 | -6.62979 | -56.28832 | 2025-07-12 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85997102-7f18-3085-b53d-f84386471f3e | -5.84356 | -48.39256 | 2025-07-12 05:27:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1cfef93c-71bd-3460-9012-e1405ee3d3b8 | -8.01225 | -50.10201 | 2025-07-12 05:27:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e069eba-b815-3306-a79a-b9d0f99a64fc | -6.62725 | -56.2753 | 2025-07-12 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a7f2df1-42aa-30c1-ad89-afc64d8b386a | -8.0099 | -50.10234 | 2025-07-12 05:27:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8195f89f-e02e-35da-ac7f-137a49e605da | -8.47086 | -49.61741 | 2025-07-12 05:27:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d2da9a2-e13c-3370-9e27-e8f723373810 | -4.11922 | -54.91611 | 2025-07-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce01ce4-743e-3e15-9b0d-122c8a4bf5e2 | -3.87086 | -54.2356 | 2025-07-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ad90bc6-de4c-3fef-8bdf-80942c149176 | -6.42733 | -48.53265 | 2025-07-12 05:27:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8b3f3b9-71ba-36eb-8386-54da6026bcb1 | -7.08137 | -49.61248 | 2025-07-12 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7be6353-5958-3257-80f7-bfc4937a335c | -5.14798 | -60.37566 | 2025-07-12 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60083695-53a6-340e-8018-9c521a3493e5 | -8.47005 | -49.62371 | 2025-07-12 05:27:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2b3f423-92d3-3185-b637-07b57098dd57 | -4.1155 | -54.91303 | 2025-07-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1ebcb7c-5424-3427-96f5-7dfea83fe9f1 | -5.8507 | -48.39344 | 2025-07-12 05:27:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| ca986656-3ff3-36cf-8c34-3f7fce71bad7 | -5.14404 | -60.37875 | 2025-07-12 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f915a4a-2601-362b-a9e9-c21f55bdec56 | -7.08559 | -49.61097 | 2025-07-12 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c77ebff-a1c4-395e-9df7-cc4e92244f19 | -6.63037 | -56.28422 | 2025-07-12 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1386caea-6fe0-3ccc-9e75-baeee33eb523 | -3.87163 | -54.23051 | 2025-07-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d79b953b-a62e-3a0d-ad04-a6c6eaca896e | -5.14854 | -60.37203 | 2025-07-12 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8118e883-8945-3c23-ae47-f0c0e8301f8b | -5.84262 | -48.39949 | 2025-07-12 05:27:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 4dabbe40-3231-346b-bc33-7b1137b8b33d | -9.96813 | -64.95143 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0494b1a5-23d4-38f1-8512-faa540e4b505 | -10.31856 | -67.34918 | 2025-07-12 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2af0658-b549-3363-9ade-7da8569a60ce | -11.86637 | -58.70982 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6445ac3c-46e1-333d-a036-d97a329c4ca5 | -7.92589 | -61.55592 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a5a437c-772b-31c3-b3e9-cbb2ef60bbc7 | -9.0244 | -61.22692 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cd2a061-1dea-32f5-874a-2543e02e8211 | -8.80395 | -67.26915 | 2025-07-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc838003-16c4-3728-b3ad-dd98775083f4 | -7.90519 | -61.51276 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46935329-b329-321f-af23-701f2bda14be | -9.78809 | -62.48553 | 2025-07-12 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56d08a6d-567f-3852-83fe-f95d0cc24440 | -7.78252 | -61.36674 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0523fc1-9e6d-3473-8a5c-ee3eec034053 | -7.92923 | -61.55644 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 038b1e83-24f5-3b9b-b810-4d6d835a8834 | -9.01535 | -61.21798 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 149dfcc0-9f1a-3bc7-9c16-a903ea52290f | -7.91866 | -61.55841 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4ff351c-2749-3881-b067-35235c0f9111 | -10.67003 | -49.50242 | 2025-07-12 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6cbafe25-ebee-3847-848f-738e208c5497 | -8.64476 | -64.17017 | 2025-07-12 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b94a70c-45fd-3474-875b-9578907275c7 | -12.493 | -51.27512 | 2025-07-12 05:29:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05aa4b58-c976-37bd-b870-d54e8cb825b1 | -11.8636 | -58.70805 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ccc2a61a-49a0-3fb4-848c-e0dc59698871 | -8.52362 | -54.77385 | 2025-07-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c93d5048-cf49-364d-9993-8fb6c4f4b3e4 | -8.53103 | -54.77125 | 2025-07-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80adc620-04d6-303a-8ed6-492e296c7722 | -13.64445 | -53.93565 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7feecb19-6c1b-3690-b0c9-4ae9c2ff75ec | -10.6727 | -49.50166 | 2025-07-12 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f1e37d9-3ce0-32ad-8693-44b681189fe0 | -9.49464 | -63.465 | 2025-07-12 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfd03f52-87ba-3384-aef9-beb7503afede | -10.09512 | -60.4949 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8f3d1db-919d-303e-8e90-aa0eed6fe623 | -11.86711 | -52.25402 | 2025-07-12 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed986a3-45aa-3a3b-bebb-b2823078463d | -10.09864 | -60.49541 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d29e56-bd67-3e34-8d59-e0c178e1c5da | -7.91697 | -61.54726 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4acb6d9-8b1d-33ea-bec4-b5a2ec2fa870 | -9.02385 | -61.23058 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 573fbec2-8491-3277-b110-dcd8dcac5677 | -9.34589 | -63.56632 | 2025-07-12 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
