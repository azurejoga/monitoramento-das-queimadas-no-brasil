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
| 01480cf9-f7cb-3e07-9678-7f48c7e2ed46 | -3.0849 | -45.777401 | 2024-11-15 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b44f6817-80c9-31a3-a17d-bf28582fecc4 | -2.3328 | -46.2813 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdda5b51-13aa-3964-8aea-054afe96a908 | -2.9908 | -45.862701 | 2024-11-15 00:08:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af115525-0abe-3ae2-b8ab-7aefb72f0c5d | -2.6177 | -46.814999 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5af9e2-5e61-3fb5-bdf5-c30ceb53220f | -2.7841 | -45.9515 | 2024-11-15 00:08:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38342d92-9f81-3001-b4b2-8b4d1656082d | -2.828 | -46.651001 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e54e644-8498-3e61-9675-d5ef080bb2c0 | -4.6553 | -44.197601 | 2024-11-15 00:08:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dc1885f-aa43-31ea-98df-592018a49c1d | -3.0954 | -45.961498 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f34b07bc-6a7c-3095-ac8f-679417a060f0 | -10.4598 | -36.949402 | 2024-11-15 00:08:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a6b3742-28a3-3ea1-b742-dc06faaed17d | -1.6886 | -48.456001 | 2024-11-15 00:08:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ed581d-a48a-32f9-a9aa-958dc52e65a3 | -3.236 | -44.302502 | 2024-11-15 00:08:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1350a148-1503-3b84-9ee4-462c16a6bf81 | -3.2888 | -45.539001 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd48f1a1-2b1a-3183-9372-d04f2e45d3f4 | -3.7094 | -41.6814 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e425a32c-09cf-3ce9-8efd-4bf3ca113b30 | -1.9795 | -46.359299 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533eda0f-61ee-3e0c-9b12-483bd0818eb2 | -2.3946 | -47.702499 | 2024-11-15 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1237727-e0b9-3084-be67-f909d090cbe3 | -2.8166 | -46.646198 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a40003-eac8-3dba-b045-ce1f313d4912 | -1.8567 | -46.2715 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e142143-d6eb-3cdc-88ef-20dab0d37ade | -2.4901 | -45.1506 | 2024-11-15 00:08:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc81eb7-7399-3d86-ad9e-6f17b6ec3199 | -6.2218 | -41.048698 | 2024-11-15 00:08:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3bb480d-ad8d-3cac-ba61-53818cb4e0d2 | -2.9466 | -45.164001 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f506ef3e-a188-3fe1-b522-a4b263b5d145 | -4.3072 | -45.714901 | 2024-11-15 00:08:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cda556c8-1943-31c0-9b10-9c7c4c8999e5 | -2.6617 | -46.8274 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aebbac0-bd2f-3011-8698-d3f118b950f4 | -3.2438 | -46.530102 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68c507b3-adaa-31b0-8d6d-384bcff65eff | -2.6164 | -46.168201 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e61fea23-efab-3366-a404-4331bb91de26 | -21.7995 | -49.769199 | 2024-11-15 00:08:00 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 496d475b-ff11-3ec4-9452-21635a04baf0 | -3.1084 | -45.973099 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a30f6e0-14e6-357f-8b10-e008a35d5fd5 | -4.3068 | -45.621498 | 2024-11-15 00:08:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d08fe866-df40-3789-8a36-5f2ac58cf98e | -3.888 | -42.5494 | 2024-11-15 00:08:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a5c74c53-6a21-3535-80fe-e1b545243c3f | -6.1563 | -41.165901 | 2024-11-15 00:08:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20e917c1-935e-3685-9221-694f3cd94e33 | -10.4501 | -36.951801 | 2024-11-15 00:08:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca42f5fc-d3e6-30bf-b32a-8be5ffed3dbc | -3.7834 | -43.8983 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8581b377-51c0-35f0-b0dd-9363d18fc4d8 | -1.9014 | -46.470299 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500727d0-a09e-3cee-96b6-55017849052a | -4.8322 | -44.6147 | 2024-11-15 00:08:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87f7dfdd-2870-3fb6-8ff8-8347ea18e4b5 | -1.705 | -46.147301 | 2024-11-15 00:08:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 058ec4b2-6f1c-3a3f-a515-98b0e8dfa2a8 | -2.2842 | -47.899101 | 2024-11-15 00:08:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e27a87-a2a7-3ce1-bc81-83b9eb09a7fc | -2.4211 | -46.261799 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f84d07f8-6579-338f-8070-fedaad084644 | -7.4688 | -35.273399 | 2024-11-15 00:08:00 | METOP-B | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8d45e86-cfb7-333b-a445-3f564aec247d | -1.9104 | -45.4585 | 2024-11-15 00:08:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a07a197a-880d-364f-9581-28a093c574a8 | -2.6275 | -46.812801 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17cce35b-7111-35fe-aacb-58888574dc0e | -3.176 | -45.0844 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc40c18a-d5dd-3199-81ec-6698aa7d9aa5 | -7.4738 | -35.2934 | 2024-11-15 00:08:00 | METOP-B | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aab25d0e-8b6c-3e36-84ce-af28d8b0601a | -2.6338 | -45.970402 | 2024-11-15 00:08:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f81d20c8-2bf4-314d-b5aa-b27032460b03 | -3.2421 | -45.377701 | 2024-11-15 00:08:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d2722ee-b8ac-3ec1-92c5-7e2323b46e92 | -3.0834 | -45.770599 | 2024-11-15 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b14380b-7529-35c5-9cd8-70bbd620e138 | -3.7965 | -43.910301 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20bbb772-b1a6-386a-a54d-1732ebccbdd2 | -1.9089 | -45.451698 | 2024-11-15 00:08:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60dd75a5-a04c-380e-9a54-cbf5e072c179 | -1.9284 | -46.269901 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87870b1a-a83a-35f9-8116-3ecc6f60dd3d | -2.3457 | -47.2094 | 2024-11-15 00:08:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73210b14-720a-37d0-be68-4cefb119472a | -2.6667 | -46.804199 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4fa51f9-7cc3-3248-80c2-8768b70d754d | -4.1872 | -40.674 | 2024-11-15 00:08:00 | METOP-B | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e20888d9-e099-3f7c-9cc6-1d2650f1894c | -2.631 | -46.186501 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae98c812-e412-322e-aed5-f030713d304f | -1.9063 | -46.766701 | 2024-11-15 00:08:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f41758a-037d-33b9-9d76-4ce9e18e7725 | -4.7277 | -43.246201 | 2024-11-15 00:08:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 209a7bd1-4e69-3a15-b66e-a0e4eba0624f | -2.6263 | -46.166 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac350698-11a9-3a6f-962d-b81b28b435c2 | -4.197 | -40.6717 | 2024-11-15 00:08:00 | METOP-B | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f2875476-12dd-316b-9562-3bbb05601ca3 | -2.3299 | -46.8638 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0ed2c3-871d-3dd6-86c3-8d470503557c | -2.0921 | -46.356098 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41921811-4340-37a6-b737-3c5ed462c206 | -3.335 | -45.378502 | 2024-11-15 00:08:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4dd146f-d15b-3027-9e29-2eef3ede603b | -3.067 | -45.058399 | 2024-11-15 00:08:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b89b6f6-a06f-3062-b644-4710ca0e2fad | -2.0711 | -46.2169 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfbcf4d4-2f76-3ef6-bb57-7e7713f81dce | -1.8533 | -47.813801 | 2024-11-15 00:08:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df5df9e-ad6d-30c2-9f37-2dfd6d6d8e27 | -1.8582 | -46.278301 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afab28c4-b11b-3811-88f4-9b73a1b2e36d | -3.0932 | -45.768501 | 2024-11-15 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e34c587-5f7f-3bc6-825c-276b48e49ad4 | -3.7016 | -41.692299 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d180da8-92f0-34b0-bf3c-d03be5f89b50 | -6.0365 | -41.806198 | 2024-11-15 00:08:00 | METOP-B | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46deed65-7db4-30ff-b3a6-9f8b3c780ee2 | -2.5303 | -45.556999 | 2024-11-15 00:08:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96a87acf-1a12-35b4-9005-ee30c8f0266d | -3.3044 | -46.066399 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4d68658-1d33-3dd5-ad7f-da806f4e4ed9 | -2.3343 | -47.204399 | 2024-11-15 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4dc08f3-924f-3a71-a909-5fe3fe2eb407 | -2.4227 | -46.2686 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26b81523-99e4-3cae-a2c2-a24cdd228e5a | -10.4564 | -36.9356 | 2024-11-15 00:08:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a831657d-86d5-3355-a4e0-8d7e973dbb8e | -1.957 | -47.9552 | 2024-11-15 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3237c1-9afd-372f-b78b-d21bfdb3b6e2 | -2.3359 | -47.211498 | 2024-11-15 00:08:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3318a5-2f43-3653-b5ff-74c2b2f67d70 | -2.3441 | -47.202301 | 2024-11-15 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a0849b-1e2b-365f-b1cf-d9f1a13c7bd0 | -4.6569 | -44.204498 | 2024-11-15 00:08:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca7ef7f7-f314-35f3-93ef-71bd30ef780e | -2.6475 | -46.168499 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 832fcc81-cf2b-3dd1-bd44-ed8045cbcc9f | -3.7932 | -43.896099 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a761b21e-fd6b-36f2-a7f8-23e411fc1c7e | -1.9652 | -47.945499 | 2024-11-15 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f147f862-fe2d-3ffd-94a5-172b7df362bd | -4.1931 | -44.249802 | 2024-11-15 00:08:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cc0d89f-b204-3bc3-a28d-f84d7cd3e98d | -3.2838 | -44.467602 | 2024-11-15 00:08:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6d7f231-20aa-3b20-b615-3aa600904531 | -3.2848 | -45.475498 | 2024-11-15 00:08:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e19dc3fc-883f-3fdb-b5c0-55c3cf151a22 | -2.6619 | -46.186901 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 172748fb-249c-32fb-90bd-d73d8ef525b9 | -2.6797 | -46.816101 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 469cbc14-4ea4-3180-9c64-1ada733a633f | -2.6537 | -46.1959 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37a723ca-7d83-3eff-ae21-654c72839a2b | -2.9456 | -45.114101 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc896bb-ae1a-3977-8f37-e9bc41c8f5f2 | -3.5592 | -41.8797 | 2024-11-15 00:08:00 | METOP-B | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ebd86f62-c2de-3ba8-848e-88f669e8a689 | -2.7955 | -46.6436 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b9d8ed-ba63-3942-a0b8-93b5206d0749 | -3.2946 | -45.473301 | 2024-11-15 00:08:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfb9329b-e176-363a-b3f1-9ac76eedbeec | -1.4725 | -45.755699 | 2024-11-15 00:08:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7337ce18-caae-3a98-ab92-32f30db7d18a | -3.785 | -43.905399 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 776a9743-8cf7-39bc-996d-2b09a08c0389 | -2.6459 | -46.161701 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c42a4dc-3754-34e6-a6ae-64b2bdeddf61 | -2.673 | -46.832298 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c3f092-1ebe-3e89-819b-351076aa25b0 | -2.6699 | -46.818298 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf6c77bd-7eac-3ca3-b583-40f1ae7572d1 | -3.7114 | -41.690102 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acd5c57d-d43f-3856-97e0-25da0836f9df | -1.3858 | -47.108799 | 2024-11-15 00:08:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b78fe46b-3091-3293-9ed5-4f5977b649ef | -1.9635 | -47.938 | 2024-11-15 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a9bfe0-fb41-3538-83c9-af44a4b1de2d | -2.7131 | -44.769299 | 2024-11-15 00:08:00 | METOP-B | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4fa4d6d-1f66-3268-a120-4d45c87e54c7 | -3.5572 | -41.871101 | 2024-11-15 00:08:00 | METOP-B | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9377c56b-7822-3c91-854c-a9a7a7654c77 | -2.629 | -46.819801 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da660d5d-700f-3220-8981-611b930402c2 | -2.8539 | -45.3923 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7cec01c0-3e6a-339c-960b-9faecd5c6b02 | -3.2797 | -45.7271 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
