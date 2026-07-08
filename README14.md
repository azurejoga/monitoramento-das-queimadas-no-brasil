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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84eb2599-c130-3bf0-ba10-e3ece0969a89 | -4.04365 | -47.15538 | 2026-07-08 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a31f995b-277c-327b-b361-642dbaa45186 | -4.82029 | -46.81366 | 2026-07-08 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a3de76b-66c4-35f6-9bc6-946b0cfa8b22 | -6.90773 | -44.90483 | 2026-07-08 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bff849d0-f2b2-3726-bdf6-bbed6e0a0b4a | -8.1277 | -47.10239 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f37af0b-87ed-33aa-9718-2cdf2d37da5b | -6.49112 | -43.61726 | 2026-07-08 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1576b63-0edf-38b2-85c5-31d159123e6b | -5.66242 | -44.31422 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 43bed169-8aae-3a90-8d56-027a214ba28c | -4.34261 | -47.76472 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b444830a-df40-331f-ad30-2082a04205a2 | -5.79801 | -43.79818 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c94065d9-58a7-3b34-88b8-8fd3a8cb3ba6 | -5.80079 | -43.8022 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3281211-ac62-33aa-8b1c-ba11493bfa57 | -6.85821 | -38.35041 | 2026-07-08 04:23:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c77a20f4-e37e-3ebc-99ec-b9719be83646 | -5.46909 | -45.42482 | 2026-07-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba45c9c8-2c58-366b-8998-80e396b87538 | -6.92116 | -43.71255 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88859ca6-aafa-3711-ab25-05b5095b677f | -3.51008 | -48.04057 | 2026-07-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0e325d82-6686-38b4-bc1f-c0c41698c90f | -4.26239 | -48.61437 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61932f9-2b39-3510-999b-8f893db787d5 | -6.90279 | -43.70622 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d305f7f-109c-3d4b-af31-8dc847832afa | -5.50606 | -44.07725 | 2026-07-08 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d13c4bb-5c21-3bc6-a4c8-c15ec1352b17 | -7.01453 | -42.78695 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9f66cd8-80fe-319b-a415-dee7bd2d502e | -5.79856 | -43.79469 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 934948c4-79f9-318a-807a-d89fce8b6219 | -5.33439 | -44.7109 | 2026-07-08 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 563876d1-7d41-3f5d-8d45-57d953ff5d61 | -5.80024 | -43.80569 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10ee1d2e-b7f2-3281-9b7d-006ea92dd5ef | -4.28807 | -48.35809 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44acef6d-2b60-3604-b535-09cec107bcc0 | -6.47814 | -42.92505 | 2026-07-08 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c640bf8-37a6-3a7a-a75a-0b9a40e8aa58 | -8.12367 | -47.10558 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9187fab4-be3b-3754-b5f5-9ac5621425e0 | -5.65966 | -44.31025 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89bc916d-c9c7-31b7-9cf7-22983d6a0a52 | -6.93566 | -43.70751 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fd1c4f0-f2f7-3f3c-85ca-7b9b3c6d32cf | -6.92671 | -43.69881 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23625771-d543-333c-80aa-416854d7f201 | -7.25721 | -45.10228 | 2026-07-08 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e56bbeda-c1b4-322e-9ec0-89b967e2b4a6 | -2.98454 | -48.59184 | 2026-07-08 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b61c852-3136-36c5-9986-4fbe26e67672 | -5.30828 | -47.24421 | 2026-07-08 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddfb5ee0-2013-3761-b90e-695829a11556 | -7.05617 | -46.9585 | 2026-07-08 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c37dd0a-2315-329d-9f7b-11d5e0b9cef9 | -6.93901 | -43.70803 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89937b09-8143-39a9-b414-3d864e3e157c | -6.93062 | -43.69576 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09e21279-c732-3311-af8e-b43b21262aea | -7.89776 | -48.25592 | 2026-07-08 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 377a6aa2-01d0-3fed-a29f-79643137a369 | -4.5735 | -48.02996 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c304b18-9104-38b3-9f0d-44ea47d45435 | -6.90442 | -44.9043 | 2026-07-08 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2affc461-95f6-3c72-8c97-4b1068df5f5c | -4.34557 | -47.76957 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e952235b-2f2b-3a82-8988-7dbe99b7b976 | -4.25854 | -48.6138 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f85b51e-6745-3df3-9d7d-dcb2432d0321 | -2.98117 | -54.60441 | 2026-07-08 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a7622f-0ded-35c1-923f-85f28e2dbb94 | -6.84499 | -50.6501 | 2026-07-08 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de4f8ca-1b72-3da1-9ede-7bf7be5acb2e | -6.92226 | -43.70543 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 052ff901-b97b-3f52-ab61-55db592b17f4 | -2.98373 | -48.59679 | 2026-07-08 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f18277-5293-3218-9f81-bfcbe2d462dc | -5.80521 | -43.79573 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1520bc04-8301-39b5-b6e7-7d5d89a070e3 | -8.07088 | -45.58425 | 2026-07-08 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22daf8d9-cece-34fa-a600-bf2dca1a09be | -6.91336 | -43.71862 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 552453b5-7e58-3e52-85ad-9d2ca829ebbf | -6.94402 | -43.69784 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c14607ae-f412-38ac-b643-82da442f85ba | -5.98211 | -43.61826 | 2026-07-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b9db08b-d04f-30d8-8c99-bcd423f9505f | -5.5022 | -44.0802 | 2026-07-08 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 831f4170-7681-3b99-befe-68c8b034ec78 | -5.47852 | -44.10133 | 2026-07-08 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eba22554-52d8-3263-9677-f275c2331502 | -6.94682 | -43.70193 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4fec056-8f51-30e1-94fa-7dcdf6411f8b | -6.64946 | -43.91349 | 2026-07-08 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f2dd884-d4ed-3e18-9ed9-6c9571ebf3b2 | -6.91556 | -43.70439 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cccbc9fc-4e76-3566-a7cb-052505ef6a0e | -5.30475 | -47.24366 | 2026-07-08 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7708fd39-a950-3fb0-9fa9-34238fa09f30 | -5.6613 | -44.29988 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a59abef-80ab-3c65-9a87-c81446acc54b | -4.41012 | -47.60193 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f94a76a-c252-3108-980f-e782775e5938 | -3.51084 | -48.03594 | 2026-07-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4006022e-597c-3584-90ad-53f249ab6cf6 | -5.47957 | -44.07309 | 2026-07-08 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfb68687-1459-31fc-8987-6fe300844750 | -6.91836 | -43.70847 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c623e9f5-a091-3250-a7a4-b6cd8c2614fa | -2.98046 | -54.6086 | 2026-07-08 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d094640e-14e1-3c0f-b254-260192978c11 | -6.42648 | -55.80239 | 2026-07-08 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7340ec9f-e0fb-37ed-ba8a-f58d49073137 | -6.91446 | -43.71151 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd6173dd-d5ad-3b7d-bc20-2965797a5c45 | -6.42729 | -55.79797 | 2026-07-08 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08ad1c76-ab18-31df-859f-1a5f1fe24b21 | -5.79691 | -43.80517 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 778f15db-bed8-311d-ada0-c3129c41f783 | -5.65912 | -44.31371 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a109b7a-50e2-3123-b35b-eec869e234eb | -7.01108 | -42.78641 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8468954-21f0-352a-9611-ac39e2b43b1d | -6.93007 | -43.69933 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5af10b9-6b31-3b45-b118-34dcf1d573f0 | -6.5945 | -51.69238 | 2026-07-08 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df90f7dd-f939-3cdc-8b18-eccab443e68c | -7.08775 | -41.349 | 2026-07-08 04:23:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd2c828f-6338-3fbe-86dd-6ac9f8747796 | -6.64668 | -43.90945 | 2026-07-08 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0711f9a5-bfa4-3c2a-adb6-0561411d9534 | -7.66005 | -40.11084 | 2026-07-08 04:23:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6577b04-faa7-3fb2-9c22-f3b05c76e055 | -5.81095 | -44.49363 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4e8ac3b-d86f-35d6-9cda-47b9a2942e66 | -5.66682 | -44.30783 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 65b81b46-744a-3ff1-8a37-cb6d4c55ee6a | -8.12025 | -47.10503 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5edd52c6-0958-3f4c-a802-64c7dc4ff469 | -2.98389 | -48.59432 | 2026-07-08 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bd9185c-ccae-3a47-bd7a-422de71c483a | -6.91221 | -43.70387 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6846796e-7496-3a6c-b52e-8ef55358160e | -6.91781 | -43.71203 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a829abc-96a7-324d-8777-737cdfe73d3e | -4.26315 | -48.60962 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 941c4d6a-f112-3e21-8642-c14a7329f35d | -7.01166 | -42.78264 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85cabfc0-5406-320b-b580-01bc0b66a20d | -3.65624 | -48.9612 | 2026-07-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21446ec2-81e6-33ee-849e-4d61368ef9c7 | -5.3417 | -45.3511 | 2026-07-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2b60e5a-a52c-36e6-ae6c-61c5207708d4 | -3.66021 | -48.96181 | 2026-07-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bddb40d3-a63d-3fa7-9f65-7e8a5c83c29d | -6.91891 | -43.70491 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 275296b8-7384-3b71-a9ed-a5f3aee27e84 | -7.00996 | -42.77079 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2989d040-2575-34cf-9917-32037eeaf1f1 | -6.93368 | -46.15068 | 2026-07-08 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d61162f2-d6fe-3928-8bcf-0ee7b50112ff | -6.90335 | -43.70267 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36461891-dafb-3ddf-b779-0e0dac2296ff | -5.66351 | -44.30732 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8e9e00bd-7b87-3e0b-979d-844e6657262b | -5.79746 | -43.80168 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 757bf75e-be3f-3bc8-88db-57af6b6173fb | -5.30525 | -43.05735 | 2026-07-08 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4fba6cc-963e-3824-8cac-55043b7ac912 | -6.92281 | -43.70186 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a5a4f34-a156-3ad6-9760-1dbdc0367ec8 | -4.07534 | -47.70425 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f30c1074-b90b-3293-8c52-0f6768cf2be9 | -5.83111 | -43.47864 | 2026-07-08 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f222476c-1ae0-37bb-a3fa-28b79bfccaee | -5.66736 | -44.30438 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aa3abe66-ab58-3aa2-8698-282bcadeca3b | -6.91611 | -43.70082 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce6759a-0b54-329b-92e3-d6e8bb455734 | -6.92951 | -43.7029 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd0488ea-fcdd-343f-9103-f913ab4264cc | -6.93231 | -43.70699 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a42bae79-9832-3e42-8ea6-9ec790eab050 | -5.66406 | -44.30386 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4bb7f59b-df06-375b-abed-efcdee1a14a4 | -6.91501 | -43.70795 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 268c61df-5c69-38bf-82f8-2b2a12ddc260 | -6.02724 | -46.72659 | 2026-07-08 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c84b984c-7e77-3138-ba2c-7c4129758cdf | -6.91946 | -43.70134 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23bebe93-288b-3d0e-a9d7-fa3120553bf4 | -5.04062 | -44.46349 | 2026-07-08 04:23:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8524d505-0837-35fc-b844-9d841f07a859 | -5.62565 | -47.10088 | 2026-07-08 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
