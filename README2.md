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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17225a14-cb06-3f0a-9a62-53cba8a97018 | -4.7258 | -43.2533 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f805b2c4-82a6-30b1-86a4-7f84ed530f0e | -4.6607 | -45.683899 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea7fda02-aa26-3114-b482-e2b12fb40e4d | -3.9873 | -43.7169 | 2024-11-23 00:00:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbaf66f0-34a7-314b-9979-70e970c1c9fd | -2.7013 | -46.258999 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b196e443-75fa-3df6-b1b2-bf7ddbbca766 | -4.3373 | -45.3326 | 2024-11-23 00:00:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| daabc0b5-2abb-3b6c-ab77-0640c99f5129 | -2.8561 | -45.307201 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9aa4123-68ab-38a6-9df3-832057eacd0a | -3.1358 | -44.270401 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45388d06-15ab-30fe-84d5-352ca85624b0 | -2.4345 | -46.529099 | 2024-11-23 00:00:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9270a6db-3b6f-3367-9222-4b4142a1b95a | -3.84 | -43.9305 | 2024-11-23 00:00:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a41c96c0-4d06-3ad8-87be-39e204f03db4 | -4.2521 | -48.6936 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e654389d-b01a-31b0-9a8a-ba8b441e195d | -4.6985 | -45.855 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f788296-cd0d-3108-8f0d-fe8e7844daf8 | -5.949 | -39.6805 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d326f495-5eb0-3d14-917d-b634a3e4263c | -2.8203 | -45.1483 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4ada5bd-0efa-3a78-bf8c-d4c0a61ad971 | -4.497 | -44.713501 | 2024-11-23 00:00:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d076edf-ef00-3c22-8920-e97633f267a9 | -4.421 | -44.095699 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4efc222d-b46a-39c7-b8ce-56159fb18e82 | -2.4443 | -46.526901 | 2024-11-23 00:00:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff7a017-d42f-3e80-8e0d-118560fa7fd9 | -6.5652 | -39.761398 | 2024-11-23 00:00:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 15ea2b9f-55b2-3b47-a1cb-0bcff54a0902 | -10.6812 | -37.0532 | 2024-11-23 00:00:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df9fb371-dfb7-3371-8a4b-0b5669c8b791 | -2.1754 | -45.3367 | 2024-11-23 00:00:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83ec4105-ef4c-35e6-bce6-91b0998c6d2b | -4.195 | -46.8144 | 2024-11-23 00:00:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bba609b7-aeec-3b87-9899-eb3cdad3cc6c | -5.8627 | -39.663502 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c89c87c4-3034-3902-98f8-9e2a81b08b60 | -4.6955 | -45.841702 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 966f2dd6-e129-3f2b-b739-af15f4c76ce4 | -4.5284 | -42.922199 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb7861c5-203b-3318-a340-660e4c77f0b9 | -7.6937 | -42.984901 | 2024-11-23 00:00:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a53d5b61-63f1-37ce-86bd-5e43f0ad0e6c | -7.3175 | -34.946999 | 2024-11-23 00:00:00 | METOP-C | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f41e718f-ec65-3b3b-9d70-a753bc1935fc | -5.9474 | -39.673599 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e591bf4c-9dee-30c2-8dc0-310b5c11754b | -5.601 | -37.9813 | 2024-11-23 00:00:00 | METOP-C | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 488e9d9b-341d-30cd-8c93-8f430eb96be6 | -4.1089 | -42.474499 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e79660e-6a00-3739-baa3-eb0ef5085239 | -5.1104 | -45.823002 | 2024-11-23 00:00:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cceae85-1fd2-37e2-80c9-c50598d45d6f | -4.0103 | -44.324501 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3162de92-ef85-3cee-8b31-0a8dda8ffa94 | -9.8157 | -39.145 | 2024-11-23 00:00:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 55b20caa-6ab0-3a99-bb6e-16312e505d5e | -4.6037 | -46.491501 | 2024-11-23 00:00:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c27d997c-d465-3eca-bdf7-a8e5ec0a8e13 | -2.6984 | -46.2458 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e613c278-513e-3597-8a19-9b2de6ff903f | -7.6034 | -38.976898 | 2024-11-23 00:00:00 | METOP-C | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3ee642a7-0592-3a6b-b753-e6ffcd362195 | -9.7377 | -37.034401 | 2024-11-23 00:00:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c2d1ac09-10ab-319f-8e09-336562139492 | -10.4754 | -37.145199 | 2024-11-23 00:00:00 | METOP-C | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98784e7c-03ed-3cc1-b63c-5cd7f3e73922 | -6.5051 | -47.0373 | 2024-11-23 00:00:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d688dc7-435a-39f8-b619-3c8c21ce8850 | -2.4474 | -46.540699 | 2024-11-23 00:00:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5d6627-3bd3-379e-904c-c96e81c72f2c | -3.1456 | -44.2682 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43fa0983-69aa-3246-8f1f-57ed47b87931 | -5.2283 | -45.102798 | 2024-11-23 00:00:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38a1b774-c82b-35ae-8775-5108c8c3ccee | -3.6711 | -47.121799 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0855fb8b-431b-3bbf-b7f3-02b51fb70c3c | -3.163 | -45.7155 | 2024-11-23 00:00:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3e481f-4a5a-33d3-8b17-ec3312dc758b | -7.1362 | -39.053001 | 2024-11-23 00:00:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 56fa0a80-e5d1-3bf1-9796-cd68cc6cb9ac | -3.6221 | -45.707298 | 2024-11-23 00:00:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43c2bb71-5f47-36a4-828c-e9bd4ab61517 | -3.0137 | -45.141399 | 2024-11-23 00:00:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c71e3b63-b5cc-3fbd-94b0-82f592fb930b | -5.1058 | -43.1609 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07683f92-6b8f-32ac-9c43-4fc59fe01ea4 | -4.655 | -45.658001 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 094dc49f-a665-3641-a95a-5da99d9fac44 | -3.9399 | -47.967701 | 2024-11-23 00:00:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d71d78b6-29df-374d-b587-e8342b6d63b7 | -6.5668 | -39.768299 | 2024-11-23 00:00:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 23aa4a0f-f4ce-33b4-9f9f-785b3039cf93 | -2.8587 | -45.318699 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbbd7fe-2cb2-349d-8817-7b37674251de | -4.025 | -46.184101 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e66c8d5-5439-3dc2-ac59-ac68cdfca5e9 | -2.6563 | -46.2411 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9e917c7-76d6-3903-9e74-eb0891aa0d72 | -5.1134 | -45.836498 | 2024-11-23 00:00:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3087455b-1319-3448-a749-dfcf7a0f4af6 | -6.1434 | -46.6791 | 2024-11-23 00:00:00 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da5ec590-2b29-3864-980f-53d69199b047 | -5.2254 | -44.903702 | 2024-11-23 00:00:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03a04d96-75f4-33ec-a95f-f6c8f57a41d3 | -3.5994 | -41.677799 | 2024-11-23 00:00:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| babb817c-b949-3928-bb0c-0a0df03507ef | -3.6193 | -45.694801 | 2024-11-23 00:00:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bac3874-5dfb-331b-a72f-1a21e26b2ba8 | -6.2206 | -39.4244 | 2024-11-23 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 62f6ef72-b258-336e-99fd-6743d0f5bbb3 | -5.8642 | -39.670399 | 2024-11-23 00:00:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7a2cd688-c080-3ff3-85f6-6f825f9547d7 | -4.2605 | -46.278999 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39b254ef-ff36-3dbb-8629-e88c407ed28e | -2.9478 | -45.167599 | 2024-11-23 00:00:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2874ee62-7e09-321c-9970-2b49fc5918ec | -9.7279 | -37.036701 | 2024-11-23 00:00:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 58eae9ae-1e69-32e7-9136-67a72db894d2 | -8.1569 | -38.238098 | 2024-11-23 00:00:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6f6d8c48-19cf-3c07-b075-ba35b375bcb1 | -10.4953 | -36.694099 | 2024-11-23 00:00:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43bb8261-f542-39d0-b16d-a90b912a0d91 | -3.8444 | -43.950001 | 2024-11-23 00:00:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55de2ada-1d37-36b4-8016-76bd04c30f39 | -4.7052 | -45.8396 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81abde23-7bab-3251-80d4-a281b11cf214 | -4.5638 | -48.028599 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc806fc-c593-32fc-9c74-c8f4ef69fd1c | -3.852 | -43.938099 | 2024-11-23 00:00:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a35cf00a-141e-317d-97ad-13ccf47d523b | -10.6796 | -37.0462 | 2024-11-23 00:00:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8767d38-614e-3df5-96a5-d01014bf02e6 | -3.4615 | -48.2444 | 2024-11-23 00:00:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c21f79-417a-3442-a42d-d0fe87db0424 | -2.734 | -47.5425 | 2024-11-23 00:00:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21cfe1fd-06d3-32e6-8ee8-61e2a95a64f8 | -4.3264 | -41.7957 | 2024-11-23 00:00:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 844c40dc-19d8-3d28-8b13-4d3e95ed265a | -4.2735 | -46.291 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5ad6966-fe7a-3fd3-a22d-c71a08ef4330 | -4.5947 | -45.431801 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c339c9e0-e1f8-3867-8b01-891cb2e88fb5 | -9.9408 | -36.351601 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7d380eb-6167-365f-a7e3-fb02ebaecdd7 | -4.5092 | -44.722599 | 2024-11-23 00:00:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee8af65-3f2f-3ed8-92ca-baa2de395b30 | -3.9456 | -47.947498 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac7f96c-c2e7-37cd-9c95-6bafc1aab45d | -3.7762 | -45.204201 | 2024-11-23 00:00:00 | METOP-C | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37ce1c66-3f42-3ee3-a88f-ce93ee8ff30e | -4.418 | -44.1283 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a779fcf4-4ff1-3d2f-a452-ef0b2ab0bf59 | -7.6133 | -42.9921 | 2024-11-23 00:00:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eacff643-1ed3-33cf-952b-08ecd8f87b4d | -5.5994 | -37.9743 | 2024-11-23 00:00:00 | METOP-C | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| a070ec97-4681-34ec-9721-11b17653a4eb | -3.0111 | -45.1301 | 2024-11-23 00:00:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10f65d50-e621-3291-8898-8d0c91ba6ab1 | -5.738 | -46.265598 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa15b51-38e7-3546-bf3e-0e2edd0e93ee | -3.8422 | -43.940201 | 2024-11-23 00:00:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c434641e-f8ac-38a1-9ba6-ab6b91668acb | -6.1399 | -46.663101 | 2024-11-23 00:00:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1f78aa-1306-3483-8626-bdb45d244cdf | -5.2887 | -44.865601 | 2024-11-23 00:00:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07d35569-1ba5-3aee-b31d-3dc60f1bb824 | -3.1435 | -44.395401 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93ecd15f-82ff-3ccd-a73b-01b2803ac004 | -3.7365 | -49.993999 | 2024-11-23 00:00:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff559bc-b10b-3e1a-a09e-785d18a50f25 | -6.4954 | -47.039299 | 2024-11-23 00:00:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7c09341-8bd6-351f-81fb-87921baa69b9 | -7.1378 | -39.059898 | 2024-11-23 00:00:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| aaab7e45-c6eb-373b-895d-434b66940d31 | -2.8105 | -45.150398 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd8f427f-3ebb-3bf9-a25a-4038c6f6d077 | -5.1195 | -47.030602 | 2024-11-23 00:00:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afce34ff-2c5f-3fb1-96bf-9bf042b33c5e | -6.9416 | -42.782001 | 2024-11-23 00:00:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5aa75bb1-a229-34e5-b20c-ac2b512c7771 | -3.29 | -45.687901 | 2024-11-23 00:00:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 209e9cdc-f94d-317e-a904-1404be8b249c | -4.4112 | -44.097801 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 744d8263-1d94-3488-8063-3d949375f7f5 | -3.1653 | -44.401299 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fac11244-3090-3981-9b82-7ca545834a49 | -4.2475 | -48.673 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e906c098-ddc5-3220-8447-62e40546cb4d | -7.605 | -38.983799 | 2024-11-23 00:00:00 | METOP-C | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e5f776ee-0992-3b36-a482-a3b6e012f5db | -3.7517 | -50.017101 | 2024-11-23 00:00:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3d9494-555f-306b-a635-4c86a5597f0a | -4.5245 | -42.9049 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
