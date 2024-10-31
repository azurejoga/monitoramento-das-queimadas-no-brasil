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
| 65cd5063-9d61-32e0-86c5-5b860a501e8d | -4.6201 | -44.2924 | 2024-10-31 00:30:43 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cced47e1-5463-344b-a8e3-7c3461cdebeb | -4.6318 | -44.298801 | 2024-10-31 00:30:43 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16871aae-6db3-3cf1-8105-3902cc32e556 | -4.6221 | -44.301102 | 2024-10-31 00:30:43 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9709964-ced8-355f-be65-b85efc39c2a0 | -4.4103 | -43.609402 | 2024-10-31 00:30:44 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a8868c-8806-37dc-926e-5013209b384d | -4.4184 | -43.777199 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e407d26f-1c28-33b4-b0d0-b070e0bc2f77 | -4.4206 | -43.786499 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a682af45-3caf-3c53-bdd7-92a5bf69bfca | -4.4086 | -43.7794 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 602a40b6-8c78-3eb9-8127-f6e69528f840 | -4.4108 | -43.7887 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0122455e-a08d-32f8-b004-e8f5b5236def | -4.2922 | -43.410999 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dc905d9-d9c9-30fe-af64-489bfb1ce5f9 | -4.2945 | -43.420799 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4674a41d-a6f7-396d-9cec-e19493b8edb9 | -4.2824 | -43.4133 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2358bf84-7683-3710-9070-9d0ac88d3da4 | -4.2847 | -43.4231 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 928a5d97-8702-3c12-bafd-01bb9d1f7310 | -4.287 | -43.432999 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4063e659-3681-3ff9-a8df-f902e1fff84d | -4.2968 | -43.430698 | 2024-10-31 00:30:45 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00ddf8fe-aa9f-3b1e-a403-6c4b0f377803 | -4.8496 | -45.830002 | 2024-10-31 00:30:45 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61eac64b-7ad1-3f30-a5f7-9f34145dd7c2 | -4.8513 | -45.837399 | 2024-10-31 00:30:45 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f754e09d-0454-3161-af28-8d14e19c9ff6 | -4.275 | -43.425301 | 2024-10-31 00:30:46 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3afc5334-624e-3654-b838-5c948107f993 | -4.2773 | -43.4352 | 2024-10-31 00:30:46 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5f0f32c-bcda-3726-bc5e-c1a1f2b90f36 | -4.2796 | -43.445099 | 2024-10-31 00:30:46 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9150b90b-e6c3-3ae0-83c5-27a7da3d4bfd | -4.4866 | -44.830799 | 2024-10-31 00:30:47 | METOP-B | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 770cdfbe-e2d5-3aea-bbc2-8299fd59d731 | -4.9012 | -46.6894 | 2024-10-31 00:30:48 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a17fe11e-44e6-3008-afd5-d35c8e88c096 | -4.9028 | -46.696499 | 2024-10-31 00:30:48 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0fc28cc-fea7-336a-b606-b75da01ea5a8 | -4.3981 | -45.703701 | 2024-10-31 00:30:52 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9adf4ba3-25b9-37c0-9e20-98a4cb78fb74 | -4.3998 | -45.7113 | 2024-10-31 00:30:52 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8b4cb5-246e-33a4-94f1-d9e68c211c4c | -4.4324 | -45.853901 | 2024-10-31 00:30:52 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba1f696-1720-3eb7-b403-09f026981cdb | -3.422 | -41.621201 | 2024-10-31 00:30:53 | METOP-B | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 098499bf-46b7-3265-a4c9-a31f67117208 | -3.4251 | -41.634499 | 2024-10-31 00:30:53 | METOP-B | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8eedb092-41b8-3511-b07f-a182bc5f6390 | -3.4122 | -41.623402 | 2024-10-31 00:30:53 | METOP-B | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b55301c0-d204-37ba-b853-95fe175218a0 | -4.5197 | -46.4627 | 2024-10-31 00:30:53 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26fc052b-4837-3baf-915a-9fb14d87553e | -4.3047 | -45.700901 | 2024-10-31 00:30:54 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aec851cb-2283-3bfd-b54c-97a2528f049e | -3.9946 | -45.7869 | 2024-10-31 00:30:59 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72033283-3f21-3ece-8f65-f277307b04aa | -3.6409 | -44.469799 | 2024-10-31 00:31:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee2ceb11-b75a-357c-837e-52a0aa442efb | -3.6291 | -44.4632 | 2024-10-31 00:31:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72f7e78c-edeb-3582-a836-1a3bd96d9fb7 | -3.6311 | -44.472 | 2024-10-31 00:31:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0732ca23-04f0-39be-a0d1-8356b7fadba5 | -3.3892 | -44.226299 | 2024-10-31 00:31:03 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0e1404-8ddc-3a34-8b15-b9605d680912 | -4.3673 | -48.570202 | 2024-10-31 00:31:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da8b89ed-4b9e-3a0d-ad14-140e0aba2882 | -4.3688 | -48.577 | 2024-10-31 00:31:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 496f3bc2-f183-395d-ae9a-3ab686ddc2ca | -4.3704 | -48.5839 | 2024-10-31 00:31:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820d5f8b-3d12-3d40-9d48-2f8d28dc07f0 | -3.4232 | -45.226501 | 2024-10-31 00:31:06 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65c0d5df-775e-3124-8206-3cfeef1ced10 | -3.425 | -45.2346 | 2024-10-31 00:31:06 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 323bf5e0-43c8-3944-87b1-0773c0000caa | -3.9885 | -48.122898 | 2024-10-31 00:31:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 284c5f31-5211-3095-98eb-e3d5102dcf1a | -3.3136 | -45.3778 | 2024-10-31 00:31:08 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3380e1c0-18e2-3217-a450-18638831ab50 | -3.3154 | -45.385799 | 2024-10-31 00:31:08 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eca77da6-e6f5-3972-b924-309ba0d787a1 | -3.3172 | -45.393799 | 2024-10-31 00:31:08 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7a5f893-a9c9-3970-b740-51404d34fb4c | -3.9644 | -48.335999 | 2024-10-31 00:31:09 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90b73305-2b45-30ea-b79c-79bb158e79d5 | -3.9659 | -48.3428 | 2024-10-31 00:31:09 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a7e900-ad4c-34d3-abe0-1715b3fb280b | -3.953 | -48.331402 | 2024-10-31 00:31:09 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db65a9e0-eb77-31e3-9645-6922ed2ffd64 | -3.9546 | -48.3382 | 2024-10-31 00:31:09 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 209e10e0-5ab4-32e5-82b4-b1809ab722d7 | -4.1506 | -49.3036 | 2024-10-31 00:31:09 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c68a4f8-f2e6-3ab3-871c-a45037fbaeb4 | -4.1521 | -49.3106 | 2024-10-31 00:31:09 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ada64ce-cac4-312f-ae92-48efebccdae3 | -3.2593 | -45.8167 | 2024-10-31 00:31:11 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e734234-6d9c-3253-b5fc-44675e67b30a | -3.2674 | -45.8069 | 2024-10-31 00:31:11 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b932a3b3-afe2-3338-bc9f-345dce3d18b0 | -3.2691 | -45.814499 | 2024-10-31 00:31:11 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69cf2fd0-9ebc-37fb-84ce-4f49a553201a | -3.2709 | -45.822201 | 2024-10-31 00:31:11 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14c55a18-27f1-3ccc-beb2-38c50002d987 | -3.2824 | -45.963299 | 2024-10-31 00:31:11 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e45be17-a273-379d-a352-45ae1933027b | -3.1241 | -45.495701 | 2024-10-31 00:31:12 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba23c12-64c2-3311-b8a7-add4a656306d | -3.1259 | -45.503601 | 2024-10-31 00:31:12 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed816eb4-af6d-3326-aef4-1bf11ba770d5 | -2.9621 | -45.598598 | 2024-10-31 00:31:15 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95979e73-6e96-3bd6-9270-a64111241023 | -2.9639 | -45.6064 | 2024-10-31 00:31:15 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc7bfa0-fabc-33af-aa45-27d254f18c4b | -2.9435 | -45.652199 | 2024-10-31 00:31:15 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5dc517d-12ad-383c-bd29-8293ecce7723 | -2.9453 | -45.66 | 2024-10-31 00:31:15 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 308bdb4a-a60b-3636-b38e-a882588fd087 | -2.8378 | -45.459999 | 2024-10-31 00:31:16 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7954e7e3-abe0-38bd-8be5-f9cf69b4d462 | -2.8396 | -45.467999 | 2024-10-31 00:31:16 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c92b528-4bfe-375b-b21b-4339acdfa9bc | -2.8414 | -45.476002 | 2024-10-31 00:31:16 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 410d819f-9d35-3fbf-ad06-216f1bff62bb | -2.897 | -45.809502 | 2024-10-31 00:31:17 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 108769ef-88dc-3198-8836-eeddf15c638f | -2.8987 | -45.8172 | 2024-10-31 00:31:17 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4610d51a-648f-30ef-a399-57297afd93e3 | -2.9005 | -45.824902 | 2024-10-31 00:31:17 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd84729-54c3-37d1-9a0d-ed7c18bd2242 | -3.2697 | -48.454201 | 2024-10-31 00:31:20 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bf6277-59fb-3939-a12f-48c5e74a434f | -3.2712 | -48.460999 | 2024-10-31 00:31:20 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b006248e-2262-398e-a2dd-0036489fc058 | -2.7431 | -46.672699 | 2024-10-31 00:31:22 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d322406-eb86-3bd2-9f85-0f3b13f2b7a6 | -2.748 | -46.694302 | 2024-10-31 00:31:22 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cb5765-20ba-3472-9af1-fbd14d79b150 | -3.0017 | -47.905201 | 2024-10-31 00:31:23 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a4d422-4795-35ce-8d4f-a016228ef5ab | -3.0032 | -47.912102 | 2024-10-31 00:31:23 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4760d4-b39c-3f4c-bf0d-20b7778d3711 | -2.2528 | -45.379398 | 2024-10-31 00:31:26 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acbf3c33-532d-3725-9095-da3a4f20f7ed | -2.3442 | -46.006302 | 2024-10-31 00:31:26 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea5f8bc-32f3-34b7-99dd-379390b71d97 | -2.9333 | -48.607498 | 2024-10-31 00:31:26 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8509f25-b01c-3e0d-a655-89696cddec96 | -2.6342 | -47.3288 | 2024-10-31 00:31:27 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e96d7bc-71dc-36a5-9c5c-884fe506a752 | -2.6357 | -47.3358 | 2024-10-31 00:31:27 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cec3476-c995-3307-8a9f-28882a3e63f8 | -2.4487 | -46.693001 | 2024-10-31 00:31:27 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4785ed2-e5d3-3781-bfc1-e0bf8c3eb1de | -2.4504 | -46.700199 | 2024-10-31 00:31:27 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce90eef7-b012-3fd1-a23e-abfa4b88a732 | -2.2977 | -46.481602 | 2024-10-31 00:31:29 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 098432e5-911a-3753-82d7-bfe95c132f52 | -2.2994 | -46.488899 | 2024-10-31 00:31:29 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49196c62-5f61-32c0-92ce-39518f52d50e | -2.7211 | -48.6259 | 2024-10-31 00:31:30 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2523143d-ee65-3be7-9cd3-d34d6960bff5 | -2.2624 | -46.688999 | 2024-10-31 00:31:30 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5345b56d-b6bf-340a-9b1d-d772fd852d66 | -2.2509 | -46.683899 | 2024-10-31 00:31:30 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99b674f0-2f97-3aa2-97b2-1c0a172f2438 | -2.2526 | -46.6912 | 2024-10-31 00:31:30 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab541f3e-8f2f-3816-b3fb-4f226ad1c6ff | -3.1849 | -51.109001 | 2024-10-31 00:31:31 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15c608f2-f32a-3054-b65a-5c4f1c7a173f | -3.1867 | -51.117001 | 2024-10-31 00:31:31 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adeaa1d0-ce7e-301f-a42a-c2cf8f83b265 | -3.22 | -51.313099 | 2024-10-31 00:31:32 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e800e4f-62f5-34a0-a117-dc5e10eacf3f | -3.2102 | -51.315201 | 2024-10-31 00:31:32 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65138d8d-d9e8-3f19-9cf0-5a26baab5bb4 | -3.2121 | -51.323399 | 2024-10-31 00:31:32 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821cf0e6-1bec-3954-9895-26902c72ffac | -2.5459 | -48.442902 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34721966-a7be-3c68-8c49-3d86a2e0b220 | -2.5474 | -48.449699 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35d78c58-577a-349f-8436-6b67b88158dc | -2.5489 | -48.456501 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e6148f1-4b06-33fe-bbe8-44132c641684 | -2.5505 | -48.463402 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fabf7629-b1af-3dca-8358-3a4654b7e3b5 | -2.5376 | -48.4519 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab61505c-74c9-3bee-abc0-8e22c9e95f96 | -2.5391 | -48.458698 | 2024-10-31 00:31:32 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a60b56cc-bbc2-3f19-9dad-c479176e2b59 | -2.3683 | -48.661098 | 2024-10-31 00:31:36 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294e775c-8858-3cab-9ec7-d491a12188cb | -2.3699 | -48.6679 | 2024-10-31 00:31:36 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de9fcfad-3920-3ba4-916b-94361e1e0de4 | -2.1939 | -47.933899 | 2024-10-31 00:31:36 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
