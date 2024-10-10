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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffaec428-3227-37e1-a613-598e3b104a5a | -5.1979 | -44.608799 | 2024-10-10 00:20:51 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c735c76c-43cf-3733-be70-3a7942f95d0b | -5.1997 | -44.616798 | 2024-10-10 00:20:51 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0ab346-69ad-3d63-86bc-c60034732a26 | -5.2525 | -44.852299 | 2024-10-10 00:20:51 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9712ad3-4cf2-39ef-89a5-359e3420368e | -5.3002 | -45.203098 | 2024-10-10 00:20:51 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5f8427-a933-351c-af8a-34ac498bc2bd | -5.7705 | -47.419601 | 2024-10-10 00:20:52 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c93383f-349c-3e1c-9c52-5dc9fd29f961 | -5.7731 | -47.4314 | 2024-10-10 00:20:52 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 036d393c-cbe4-30ee-91c2-2dfe5b28b694 | -5.7581 | -47.409901 | 2024-10-10 00:20:52 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36666a3c-482f-38c1-824f-ef03d88538d2 | -5.7607 | -47.4217 | 2024-10-10 00:20:52 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d9d7a9b-f885-3b2c-b383-b0fead9dbd91 | -5.7633 | -47.433498 | 2024-10-10 00:20:52 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2be53068-e22b-3986-a9cb-12fbf9977046 | -5.1692 | -44.801701 | 2024-10-10 00:20:52 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdbb1614-bc98-3962-8615-9c632762b947 | -5.5051 | -46.308601 | 2024-10-10 00:20:52 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 449eeaed-c8f4-382d-abd1-3238459e1dc6 | -5.5073 | -46.318501 | 2024-10-10 00:20:52 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab15b290-f172-3f3d-98bb-a9274c50dcad | -5.1576 | -44.795799 | 2024-10-10 00:20:52 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fa4918a-2cca-3ff3-b93f-b8d17a7fcae3 | -5.1594 | -44.803902 | 2024-10-10 00:20:52 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 008c0b77-69d7-39aa-9cdf-4c20dbbf5c9c | -5.1613 | -44.812099 | 2024-10-10 00:20:52 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b326caaa-6f30-350d-b8aa-251767cf57f7 | -5.4615 | -46.204201 | 2024-10-10 00:20:52 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf674772-bf34-35bd-968b-d78212c888dd | -5.1209 | -44.907101 | 2024-10-10 00:20:53 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c69ad18b-9828-3e73-a18a-ec4a15ffa478 | -5.1283 | -44.940201 | 2024-10-10 00:20:53 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6e6b1f-109d-3300-ab79-7be4d49fa538 | -4.7072 | -43.075001 | 2024-10-10 00:20:53 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f42749b-13ab-3fc8-8789-5280af77e3b2 | -4.8749 | -43.678101 | 2024-10-10 00:20:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c5a779-894a-3389-a39f-1ef6c7d8479c | -5.2391 | -45.481499 | 2024-10-10 00:20:53 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8152245-2c11-35f9-8727-6754c0e6abd0 | -5.2411 | -45.490398 | 2024-10-10 00:20:53 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5be9f083-4162-3bee-8991-55bf7a92eb50 | -5.57 | -47.019699 | 2024-10-10 00:20:53 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf37372e-992a-3203-854b-27e9f0372ef9 | -5.3318 | -45.989601 | 2024-10-10 00:20:54 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6bdc301-c29a-3ec9-b9d8-ccdc174ce69d | -5.3198 | -45.982399 | 2024-10-10 00:20:54 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01213cc0-18ac-35f5-9541-26fc7fd7e39f | -5.322 | -45.991798 | 2024-10-10 00:20:54 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cddb97a2-28d6-3223-a6bc-b077a9345838 | -5.3241 | -46.001301 | 2024-10-10 00:20:54 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 503feb8a-5372-3a4a-9eea-03f2818addf9 | -5.4669 | -46.692001 | 2024-10-10 00:20:54 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd048a6-8427-3b61-a920-2efdf1ec5859 | -5.4692 | -46.702499 | 2024-10-10 00:20:54 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e0e56fc-5da8-3d61-8354-e6079aa6f0d4 | -3.9717 | -40.4081 | 2024-10-10 00:20:55 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8fce0e5d-8f0b-3cbc-b6c0-dbf2b0da5a14 | -3.9733 | -40.415298 | 2024-10-10 00:20:55 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 13379080-74d4-3f43-9b22-c78c76b5c66c | -5.0719 | -45.101398 | 2024-10-10 00:20:55 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d2120b6-206e-3196-af7b-fc09991dd63b | -5.0738 | -45.109901 | 2024-10-10 00:20:55 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e21be77-78db-37bd-ab2d-e2244b2902c1 | -5.1297 | -45.589401 | 2024-10-10 00:20:55 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f17d5688-e51a-385a-a0a0-cbe44246e7af | -4.4036 | -42.6017 | 2024-10-10 00:20:56 | METOP-C | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2e464f-2696-3a6d-8dcb-5ea7969b603d | -5.0804 | -45.4146 | 2024-10-10 00:20:56 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa24b36-1be4-37cd-804f-53de87f9af2d | -4.1768 | -41.925701 | 2024-10-10 00:20:57 | METOP-C | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51bf158a-eb17-3b53-a011-32c7a7d9817a | -4.1784 | -41.932598 | 2024-10-10 00:20:57 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf4e3b3f-ba9d-3b0d-85dd-60e5e1bdaa9e | -4.1799 | -41.9394 | 2024-10-10 00:20:57 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 28c63846-eb31-3ba0-a0ce-911b2bafe871 | -5.2851 | -46.611198 | 2024-10-10 00:20:57 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03a6b568-0be9-3bdf-8cad-6ae892f7e5bc | -5.2874 | -46.621601 | 2024-10-10 00:20:57 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dba6bd19-40c3-3fc3-9dbb-23f0fa7530e4 | -5.1886 | -46.222301 | 2024-10-10 00:20:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 637fe478-72e7-3542-b4f0-7b83fc80317d | -5.1907 | -46.231998 | 2024-10-10 00:20:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 754dab91-6297-3c91-8644-5a5a1effe671 | -5.273 | -46.603001 | 2024-10-10 00:20:57 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 285488e2-8888-3343-8248-9427ee549ca8 | -5.2753 | -46.6133 | 2024-10-10 00:20:57 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1da98010-7251-3e56-82a6-e29b929b94c6 | -5.2776 | -46.623699 | 2024-10-10 00:20:57 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef77244-e65e-3890-8a9d-83c29c5396a6 | -4.8927 | -45.035301 | 2024-10-10 00:20:57 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eae3d8d-6d3b-3607-ab77-d6dad7e39c92 | -4.5874 | -43.772499 | 2024-10-10 00:20:58 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d72ab0bf-a3e8-31a0-85ee-41ddcf903519 | -4.589 | -43.7798 | 2024-10-10 00:20:58 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94cbb840-f751-37fc-9643-26ee8d620ae2 | -4.1686 | -41.9347 | 2024-10-10 00:20:58 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0491b998-f883-37a8-a6ba-59cdca0e1cb2 | -4.3702 | -42.907398 | 2024-10-10 00:20:58 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1209fd1-e578-3375-9866-a91936729026 | -4.3734 | -42.921299 | 2024-10-10 00:20:58 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86181e3b-cc27-3be7-a6e6-9c602f533cb1 | -4.362 | -42.9165 | 2024-10-10 00:20:58 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06423abb-04b8-304e-afa7-15d97b7e27cf | -4.3718 | -42.914398 | 2024-10-10 00:20:58 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0d12adbb-7d7d-3c21-8236-853f13bb9b9b | -4.982 | -45.801899 | 2024-10-10 00:20:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6e0dc9f-9238-39c1-b91d-5a256ad66a32 | -4.9722 | -45.804001 | 2024-10-10 00:20:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0778969-c9f4-34a3-a716-50d3dbc7c5ed | -5.0215 | -46.116901 | 2024-10-10 00:20:59 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d18bc4aa-c886-34ca-9adf-e49246288317 | -5.0236 | -46.126499 | 2024-10-10 00:20:59 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e98f20d1-871d-37f6-9cab-7e1cd05e7d9b | -4.6676 | -44.5835 | 2024-10-10 00:20:59 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c5f93a7-ed8f-348e-b518-e73004c8a2dc | -4.6694 | -44.5914 | 2024-10-10 00:20:59 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32247d40-8b28-30fc-82a1-d15baff233d6 | -5.3579 | -47.683498 | 2024-10-10 00:20:59 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b6a1fe0-b918-3cf3-a79f-2283158fc197 | -3.8196 | -41.0448 | 2024-10-10 00:21:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e440cbad-8c57-3d41-98d0-0dc56a4c6fdb | -3.8212 | -41.0518 | 2024-10-10 00:21:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 13abf014-5ff5-3405-b5c9-4b73b61cec4e | -3.8904 | -41.486698 | 2024-10-10 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11813cc0-9dd5-3f62-8d1d-d39a77f63361 | -3.892 | -41.4935 | 2024-10-10 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2acfc4eb-0130-39e6-a055-23020554a167 | -5.368 | -47.822601 | 2024-10-10 00:21:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16cab5b2-368a-3af0-98d3-a9f9f894d482 | -5.3708 | -47.834999 | 2024-10-10 00:21:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a02887ac-144e-3c89-8b18-5a3269775d82 | -5.6811 | -49.256001 | 2024-10-10 00:21:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12029696-ec24-326f-87ba-4062dad04ff9 | -5.3583 | -47.824699 | 2024-10-10 00:21:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b84851c4-2898-372e-a6f2-24b421dc94d4 | -5.361 | -47.837101 | 2024-10-10 00:21:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae8d1624-d2f7-3599-a622-c89d0e13caff | -4.8004 | -45.357399 | 2024-10-10 00:21:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9fa6a6-8107-3e77-b760-cad7c057363c | -3.8822 | -41.4958 | 2024-10-10 00:21:01 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 528d06f7-71ab-3d7c-b6dd-267799d1d876 | -3.8724 | -41.498001 | 2024-10-10 00:21:01 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 985a8312-be5a-3c37-95d4-e6e6a92ab0d4 | -4.4192 | -43.848202 | 2024-10-10 00:21:01 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4941107-488a-394f-883b-cfb0ab2be148 | -4.4209 | -43.855598 | 2024-10-10 00:21:01 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a7def6b-6b99-3728-a0cc-b9851047bc3c | -4.3369 | -43.530602 | 2024-10-10 00:21:01 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7cf9893-8129-3c20-9797-7a969e64c033 | -4.2089 | -43.148899 | 2024-10-10 00:21:01 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0121e4d-61eb-3c9c-9418-4d5bd9e2e965 | -4.2105 | -43.155899 | 2024-10-10 00:21:01 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19e8447d-a849-3184-b01b-f4c4d710d9a9 | -4.7593 | -45.357399 | 2024-10-10 00:21:01 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d15ef0bd-183d-31ae-a1f1-ec24491f6dfa | -4.7612 | -45.366001 | 2024-10-10 00:21:01 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af9f8b23-de60-3eef-90ab-8cb46b6220bc | -4.8145 | -45.695702 | 2024-10-10 00:21:01 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| deb6d2f6-c81a-3cf7-bbab-7613680c3cff | -4.8166 | -45.7047 | 2024-10-10 00:21:01 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 637049cd-529b-38ec-92ed-ef124263b9da | -4.8186 | -45.713699 | 2024-10-10 00:21:01 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3a69f56-bb12-3cf3-be2b-10bf19cb0939 | -5.3829 | -48.262699 | 2024-10-10 00:21:01 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd6a021-872d-38a4-98e1-7bdcea642ef1 | -5.2136 | -47.539001 | 2024-10-10 00:21:01 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 916da002-b6f7-3381-adb1-c4c972709533 | -6.3185 | -52.712799 | 2024-10-10 00:21:01 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f618187-423c-349e-bbe1-27be848d5ec1 | -4.8383 | -45.939602 | 2024-10-10 00:21:01 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a49f8ca2-de96-3df1-abc8-523f660a4a07 | -4.8403 | -45.948799 | 2024-10-10 00:21:01 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 921b078e-8c38-3fe6-baa2-06cfc41bc978 | -6.3088 | -52.714802 | 2024-10-10 00:21:01 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 735e9169-1b29-3ecc-b533-4d59ab43fbd0 | -4.8285 | -45.9417 | 2024-10-10 00:21:02 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f223302-a3c5-37ef-9ca0-d9d26ee3a88b | -4.2895 | -43.548698 | 2024-10-10 00:21:02 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83f50fed-cebe-3502-8b13-85cd9267b654 | -4.2911 | -43.555901 | 2024-10-10 00:21:02 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2c809a-7a4d-37a7-9f78-a092df9ae29a | -4.7976 | -45.803799 | 2024-10-10 00:21:02 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad7a7419-da5c-3e48-8004-84e261d1f48f | -4.7997 | -45.812901 | 2024-10-10 00:21:02 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8910ff60-d2ae-3c86-8a4b-e13f4fef0b1e | -4.8305 | -45.950901 | 2024-10-10 00:21:02 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| deac484d-3f9e-3df8-9561-e62a1564d846 | -4.7899 | -45.815102 | 2024-10-10 00:21:02 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55151f8b-2261-3225-b93c-4eec353659c6 | -4.0726 | -43.002899 | 2024-10-10 00:21:03 | METOP-C | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90fd5d87-cf40-3ea0-bafb-1d25aed5995f | -4.0742 | -43.009899 | 2024-10-10 00:21:03 | METOP-C | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6be12d42-af32-3db6-b249-b27132debe48 | -5.3839 | -48.921001 | 2024-10-10 00:21:03 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e174531-7309-3370-ab3f-33e76af48403 | -4.6479 | -45.685101 | 2024-10-10 00:21:04 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
