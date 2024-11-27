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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7cc460f-fe08-346c-8db4-7b359d046ef7 | -3.04709 | -48.50214 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3cad54f-3f98-3630-9f5f-d6acec9aba3f | -4.54486 | -46.78898 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcba3878-eb31-3420-99eb-8626c675557c | -3.8894 | -43.15327 | 2024-11-27 04:18:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80c44ed8-652f-3b1f-aeaa-63e9bfc7da5d | -3.75018 | -51.59494 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a063511-a663-3dd6-852c-4fbda0af2700 | -1.94673 | -45.72384 | 2024-11-27 04:18:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 667fbc2f-db38-3af1-ba72-a0f9cd1ad6f4 | -4.73139 | -46.57063 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7586207a-c4ae-37c4-8650-1a3ddc6ba35a | -2.31093 | -47.37081 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d13a87e-6c8f-3492-aada-a1ff75779e0e | -3.22169 | -53.93677 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0400725-3e4d-3eec-96d0-5314627d3c72 | -2.58859 | -47.47272 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee3cc9cd-e63a-3340-9638-7cda14e3a890 | -3.31334 | -46.66011 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac69fe8a-e9cc-3801-9b95-679fa0d977a1 | -1.55934 | -52.78775 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaaa18c5-7c46-3a50-bc86-e11497387f21 | -2.53059 | -47.32474 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6395689f-203f-32c1-806e-71c90645f280 | -3.0494 | -48.51287 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7eda2d99-4ad9-34d9-a86c-6294f4280ea4 | -4.81443 | -46.84145 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86b1db1-f29e-37dc-8191-417a9a33ad8c | -3.24696 | -50.61944 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d247551-4774-3cd1-8eea-9a127ada9e3e | -4.17854 | -48.63094 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe0e51a-4473-3e4d-97fd-212532733a00 | -3.27502 | -50.64753 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f87e48-e2fd-30b2-9eb1-e65b59891173 | -1.71092 | -46.12536 | 2024-11-27 04:18:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d46bcad1-46fd-381f-a036-8487fc7c0c47 | -2.54362 | -45.39031 | 2024-11-27 04:18:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4aeea89-9323-349c-a034-78990e40d7ae | -4.49638 | -46.59751 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de11d171-b18f-3c17-b1f7-ffdaff46e1b6 | -2.12857 | -46.42697 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d43a936-4d60-3198-979f-67d7917b1afd | -2.10959 | -52.7774 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d72437b-1ebb-36c6-a0d4-316dc1c9176e | -3.78516 | -50.13656 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9f5101-74b2-3484-875b-834dd09d49e9 | -3.23707 | -50.67911 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ec5de53-0a9d-3bc7-819f-d32c11ace990 | -3.3466 | -46.61222 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7e8f041-51fd-38b4-8aa3-1344227bae53 | -2.58771 | -50.64023 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f20a6a9-b180-3364-9bac-7ba149a952f7 | -3.09072 | -51.02968 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6519bc6-e99a-357c-a277-36fb24e74bef | -3.68632 | -45.4302 | 2024-11-27 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b21cbd6d-5a47-35d5-9ec0-2802e0f24757 | -2.61514 | -51.80366 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d4d6b2-16b2-3864-88b1-dbc712ba5b22 | -4.48174 | -45.9192 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39da5ae6-6971-33e9-ac95-c797d9cccfe1 | -4.02897 | -46.95303 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 866a8d39-9c77-361c-963d-fbd560b6ab2c | -2.2605 | -53.7529 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c10ed2b-f675-336a-a538-e54de4cca0dd | -2.42838 | -48.54673 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27a5eb9a-2e92-3353-9151-1d30459d462a | -2.83202 | -46.83473 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88fa67e5-eba5-3245-b27e-a352e7a02949 | -3.59097 | -50.38618 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28e3d276-80a8-301b-872d-e8b1fc89ecaf | -2.00721 | -48.47968 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2977e1d-37de-3de6-9277-e02a59762836 | -2.85612 | -48.09653 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1e7407-e016-34e9-8806-e7c092ca6ce8 | -4.90476 | -38.73723 | 2024-11-27 04:18:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37498712-9c5c-33dc-9c98-f011ffeafff4 | -3.94298 | -47.98266 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ea68463-489d-3b38-ae14-f693862154ee | -1.56887 | -47.81471 | 2024-11-27 04:18:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c3d72c-13d8-37bc-80bd-23d70810da6a | -3.59606 | -50.35577 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5b97661-d84c-38c9-8d39-825794f54006 | -4.08804 | -40.46887 | 2024-11-27 04:18:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddeee305-61e7-3b14-9ad2-088d2615d41e | 0.3344 | -49.71831 | 2024-11-27 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abc2fc19-5657-3b06-b5d0-70b33afba131 | -1.20188 | -51.75072 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a67f192f-72e4-3255-bc42-4747778741ab | -3.11024 | -53.26073 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 040457f7-70dc-3193-8ab6-a19aef75732b | -1.72734 | -52.04012 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0cbb970-ccb1-3e4c-81c8-d176c156f17c | -2.82808 | -46.81299 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a152836c-0c1b-3709-8e93-a415a46dc0ca | -3.86238 | -40.44509 | 2024-11-27 04:18:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 267602b8-4065-3964-be63-a0cbf65654b2 | -3.65215 | -44.47192 | 2024-11-27 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3d9e80-7cf5-3bb9-8c09-05688c44b90e | -1.42966 | -45.96382 | 2024-11-27 04:18:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9e4652e-133e-33f4-9deb-c7fe0271055e | -3.90683 | -50.59538 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6202d3df-d348-372b-b0ee-9454a796ed4c | -2.99645 | -45.46411 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3741712-e0d8-3c14-a4e5-3aa51d57deb2 | -2.87176 | -49.11933 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ccbdb9-7d0a-3fdb-b9ec-be7659bd779e | -3.87317 | -50.14969 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c11740a-2b90-3a25-a426-868a00bc74ec | -3.08474 | -53.2838 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0309e512-65fa-312c-a01b-131812fdd16a | -3.64571 | -41.52929 | 2024-11-27 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bfdbac0c-9365-30f3-a649-78203247b69d | -3.0344 | -48.50528 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a14d28c-499c-331e-87c8-dce43f8eb9b8 | -3.26846 | -44.54329 | 2024-11-27 04:18:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6b2f59a-567b-3700-825a-00d813ee46fb | -3.28977 | -51.15753 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35d4a0a3-40b4-3813-8104-0f0ac0f568a5 | -2.94072 | -49.12624 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3da43399-52dd-3d1b-b2f6-e1e278ab6d7b | -5.02443 | -47.01573 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b93213bb-4898-3e19-a797-5d3eec6f8ffe | -2.11218 | -46.46126 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27b2904e-c232-3d19-bf39-7da8f5421956 | -4.22703 | -50.20859 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1ee2907-f207-3be5-b19f-416aa4ae0e54 | -3.99426 | -50.55402 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f40ead7e-36b0-34a3-9269-903798f63b28 | -4.32215 | -45.89064 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9f4dace-74ad-3b71-9430-fc13e9cb3e2e | -1.54173 | -45.69366 | 2024-11-27 04:18:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7411b55-922b-3bed-89c6-04a5c0e6b35b | -2.58311 | -50.63953 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a2e20a8-5bf8-3fe8-b154-9e7950c5fc9b | -3.71939 | -50.18161 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee547d5e-fcdf-30f5-b758-533fecf724b7 | -3.4367 | -40.83356 | 2024-11-27 04:18:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fbd68273-9854-3f0a-aa9b-6e973df0c5ff | -1.31308 | -51.7386 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b287e1e3-ce36-367f-a7bf-9cac0177f6c6 | -3.18843 | -50.82962 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f4f4fe-5751-31e7-83e5-523fb5fc954d | -3.44851 | -49.50284 | 2024-11-27 04:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0784ae-e088-3288-a7c2-2335fca390a8 | -3.46477 | -50.25748 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23f2060d-a7e6-3f47-98ec-565e03491e2f | -4.83453 | -45.83188 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a699044b-e259-36bd-b164-afcce3a30e7e | -2.80662 | -52.91651 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c47b0b1-9872-38b6-8882-28b48f23725c | -3.4685 | -50.26245 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79514a74-edf5-3607-974a-72ca194d30cd | -1.94909 | -46.26238 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8011f800-4f3f-396d-8960-e1bed4b71fec | -3.27043 | -50.6185 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d946540-86c0-3e4e-a37f-c74e3ce05286 | -1.70686 | -46.24209 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d17254be-8533-3a47-b949-374ad6392d73 | -2.55035 | -46.40412 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b6da20-724b-3545-91fa-eb52d399ffec | -1.8346 | -47.90836 | 2024-11-27 04:18:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f563d3-657f-3688-b0ca-70e58643b30c | -2.73657 | -54.13597 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8115377-3ebf-3e22-a345-206109e96fae | -3.81325 | -46.60554 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 983e24fe-98f1-3cdc-975a-7888061f3330 | -1.51661 | -46.07676 | 2024-11-27 04:18:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1805b196-517d-346d-89a7-2a5b0829d4b6 | -3.03937 | -51.77711 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33b4682c-852a-3c53-baea-b8c28b30d67b | -2.85004 | -46.83754 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99ec1608-ac44-395f-909a-1ba200d63b3d | -2.78861 | -49.20507 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0795a27-2a7a-3588-a6a9-25deaa652ce1 | -3.97705 | -48.08089 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac6ff359-5fb0-35f1-95aa-6e2da295912b | -4.7244 | -46.56952 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b39a2789-eef0-3d71-9897-9676add70836 | -2.59813 | -53.96919 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ce0ec3f-7fbb-36a6-92d8-8c787e26e932 | -3.23943 | -53.93573 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4805b297-739b-3fe4-a6de-012cf3632aa2 | -2.80124 | -52.91578 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0c50ee23-b5ba-3787-b48b-fcbcadf7efb7 | -3.97342 | -46.73021 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7f790f7-102d-3953-82be-a56197a7851e | -3.84881 | -51.38719 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2a1762d-f5f5-3646-993e-c31e1c413199 | -2.93768 | -54.7909 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a7b1e43-162a-3375-a640-a494a18557fd | -4.59262 | -46.11763 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b2247b-6673-3aa9-9713-689629dc68a1 | -5.02681 | -43.60158 | 2024-11-27 04:18:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4909e82-e50b-3c87-bc50-f86bfdd78b8d | -4.01672 | -46.44081 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 27d0c0ff-630d-3c3a-bbb3-2c76c86d8506 | -5.22317 | -44.91122 | 2024-11-27 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8316c5-3732-3c31-9f3e-fc1d70b2f12a | -2.5491 | -46.41198 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
