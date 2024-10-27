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
| f2b4fb25-61f4-38c5-9cba-672888fa5f2e | -7.002 | -35.63836 | 2024-10-27 00:09:00 | TERRA_M-M | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 22.4 |
| c41bda7f-faed-376a-8ad7-1eee38b4080b | -7.0007 | -35.62917 | 2024-10-27 00:09:00 | TERRA_M-M | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 18.1 |
| ac50d227-b7f3-3eaf-b650-2bb7315aa12e | -6.97249 | -39.24495 | 2024-10-27 00:09:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 62659eab-db39-342c-b977-8b6245cf4e69 | -6.96896 | -39.25129 | 2024-10-27 00:09:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fc6ccaa1-b745-3ab9-acdf-3ab95405a392 | -6.95453 | -41.33461 | 2024-10-27 00:09:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 6c49325f-4abe-3c05-8ca9-235469c62ae2 | -6.8626 | -38.4198 | 2024-10-27 00:09:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 122d82eb-9d75-36d5-a0b5-c5c3ad34d964 | -6.70904 | -37.49966 | 2024-10-27 00:09:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 674a478a-e1ef-335b-a2df-18562b5bd33c | -6.68991 | -40.8915 | 2024-10-27 00:09:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 2c55b0d6-06e9-37ad-840b-a2734fa75fcb | -6.68098 | -40.90588 | 2024-10-27 00:09:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| fac31e22-3cf5-3167-90ea-c12bf248f354 | -6.63594 | -43.70061 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aec6f6ff-ac99-3b59-905c-1d4d327df257 | -6.60202 | -42.06624 | 2024-10-27 00:09:00 | TERRA_M-M | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 68426045-cfcf-3c0d-8312-eb511d33d32c | -6.54808 | -40.51561 | 2024-10-27 00:09:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 7ee4084a-eb65-37c5-946c-2ccf70a27549 | -6.41939 | -39.55701 | 2024-10-27 00:09:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 880e6d38-73e8-3416-afbe-3ac552065d87 | -6.40901 | -39.70075 | 2024-10-27 00:09:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 9dec2a2c-5b81-3ad4-bbaf-4c5bf49d7527 | -6.40759 | -39.69012 | 2024-10-27 00:09:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| ffb6630c-e9b9-36ca-9311-12c68b2fee90 | -6.36084 | -39.65835 | 2024-10-27 00:09:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4b465251-48d0-370c-a371-313a4259b48d | -6.20719 | -39.73577 | 2024-10-27 00:09:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d0fe0baf-f19c-3ec3-86a6-83b34b63a19a | -5.97044 | -42.11954 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 717480b0-495c-3b83-b1b5-a080df65e925 | -5.96898 | -42.12939 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| eb47987b-0f50-38fe-8fd3-0396a28ae73e | -5.94004 | -38.13393 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| efe850bd-0836-32da-9dd1-4b2eaa8eef3f | -5.87511 | -39.21891 | 2024-10-27 00:09:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 071f640a-fa47-394d-aa02-68761208d891 | -5.87376 | -39.20884 | 2024-10-27 00:09:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| bde60a57-4d0a-313e-9254-e5c221c934eb | -5.71711 | -43.84143 | 2024-10-27 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 11148440-5216-3ed1-9eb5-92d2778dd390 | -5.68882 | -41.64668 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 5b99898a-c859-3e81-95a6-95c02d0ed274 | -5.68846 | -38.04776 | 2024-10-27 00:09:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e296d203-5ab3-3a65-baa7-3c51b97aefaf | -5.6872 | -38.0387 | 2024-10-27 00:09:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 11b1d571-f03b-32ea-8a87-c58f5712f593 | -5.65679 | -41.83569 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 61574f85-c908-3dec-8ee6-1ee2ab89ae98 | -5.6559 | -41.83018 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e8fc888f-4db0-38d9-be54-8f8b662333bb | -5.42056 | -43.37959 | 2024-10-27 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| db7ad74f-1c93-3c9f-a2ab-45cd09539d6f | -5.42045 | -43.37315 | 2024-10-27 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cb5726bf-c24f-3431-b571-e8830c6b8cf1 | -5.29818 | -42.94017 | 2024-10-27 00:09:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ccde483c-9c13-3899-ac8a-e9a860836588 | -5.26474 | -41.22165 | 2024-10-27 00:09:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 749408b7-8ba7-3f85-a610-c9d68b2a6c68 | -4.86346 | -39.01364 | 2024-10-27 00:09:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 568ac64c-d58c-3011-a17b-813cdeb9b8ef | -4.76647 | -43.36626 | 2024-10-27 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d6509582-9751-3ec5-a641-60d5e798aeb7 | -4.76403 | -43.3473 | 2024-10-27 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 99ed6692-52c7-318d-858c-5054fa554fe1 | -4.76284 | -43.35296 | 2024-10-27 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 96a3db1b-1d43-309c-961a-21bb736b77a2 | -4.5444 | -43.57004 | 2024-10-27 00:09:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 40ee5a6c-de47-3ec5-ab6b-35964823719b | -4.43039 | -42.52517 | 2024-10-27 00:09:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| ee23ca7b-1acf-3e51-8495-c6f09c0ec12a | -4.41872 | -42.52675 | 2024-10-27 00:09:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| c9bd7fd9-d7af-39f2-9b8c-7f9cbcca6d20 | -4.33809 | -39.14284 | 2024-10-27 00:09:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2fff8b9b-218e-3a4e-a0b3-1cd233e19e90 | -4.29214 | -40.60039 | 2024-10-27 00:09:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 17491a4d-d3df-3458-a71c-3f80ae67df39 | -3.91782 | -42.38549 | 2024-10-27 00:09:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e1714018-80b3-3de0-82a0-94d43c03c683 | -13.38311 | -45.13476 | 2024-10-27 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b6a1fdf4-ddc7-345d-922a-9d66e716fed4 | -13.37696 | -45.14052 | 2024-10-27 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 233618f2-9377-3f3d-ba79-115b6e4411c9 | -12.67567 | -39.31298 | 2024-10-27 00:09:00 | TERRA_M-M | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 94d19305-096b-3563-80cb-e052e7ee48c4 | -12.12404 | -40.36615 | 2024-10-27 00:09:00 | TERRA_M-M | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e56d541c-a201-3fd8-9737-16b6c295a520 | -10.60451 | -44.29577 | 2024-10-27 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 1d15884f-dec3-3295-81d5-3c9d3066d454 | -10.60186 | -44.27459 | 2024-10-27 00:09:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| afaa3e2b-1608-3879-b117-8949ee42f586 | -10.60147 | -44.26821 | 2024-10-27 00:09:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 18ef1393-dff2-3071-aeaf-429fe39c7f37 | -10.57207 | -44.27787 | 2024-10-27 00:09:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 920a99fb-f58b-3348-802e-47aaa5c2306e | -10.55756 | -44.28483 | 2024-10-27 00:09:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 38e05e75-4170-3da4-9c24-19268ef96c31 | -10.55719 | -44.27959 | 2024-10-27 00:09:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a2789a71-c29c-3316-82de-bef39bd915db | -10.53957 | -45.15776 | 2024-10-27 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d1951ce2-c0b5-3a30-9672-c783441d3031 | -10.53581 | -45.1256 | 2024-10-27 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 3d875b61-9112-3193-8b86-7be72cce2327 | -10.43968 | -44.57168 | 2024-10-27 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 8e7914d9-bbe3-3362-9ec5-7f7b2a6e031d | -10.17833 | -36.33223 | 2024-10-27 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 58293309-c655-345c-a9e8-6d5533dc0eef | -10.1661 | -36.17904 | 2024-10-27 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| bf20e8df-0767-348f-86d4-33bf3b0e9c34 | -10.15602 | -36.17139 | 2024-10-27 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 460b3922-27ec-38c0-a0f9-d3cc882c7f8a | -10.11497 | -36.47551 | 2024-10-27 00:09:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 19.4 |
| e57b25fe-6a7d-3d03-aade-a4f5d5612e95 | -10.11374 | -36.46655 | 2024-10-27 00:09:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 164.7 |
| bc4178c8-ec7d-3aac-9f7c-78d36f614148 | -7.2459 | -46.07846 | 2024-10-27 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| cffda847-fea3-320b-99ba-7d0ef26858ef | -7.24178 | -46.04463 | 2024-10-27 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| c055e579-493b-38c4-b14b-47d8c9b708a8 | -7.23437 | -46.05223 | 2024-10-27 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| f15fda3e-f046-3d6d-a90e-00401b4d11a3 | -7.22556 | -46.04657 | 2024-10-27 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ba567a89-69bd-3c21-8d6c-dc0e3a8417e1 | -6.86229 | -45.90858 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6c3710b8-a1c2-3d99-93c4-dae04d9ada3f | -6.8583 | -45.87617 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f4ec8a6f-36a5-37dc-b52b-fb1249c3e237 | -6.84909 | -45.88333 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 319eb04c-a118-3d62-a8e4-b04cc6a11165 | -6.8423 | -45.87752 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b302f8a4-4ca4-3dd1-a06a-a7117c62bcc1 | -6.8189 | -44.48147 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fb44d836-fe9b-3672-981f-9fcc722509a5 | -6.7245 | -44.68268 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cfd32ee5-212f-3359-92b9-8ffa32ab625a | -5.81949 | -44.13688 | 2024-10-27 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| c2dd681b-2c80-3190-8eec-b2bb7348c5fe | -5.80588 | -44.13897 | 2024-10-27 00:09:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f6ad5547-39ad-35bc-beaf-a8dd2bb7099d | -5.62206 | -44.84402 | 2024-10-27 00:09:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 933ff178-7a11-3708-9c80-4ee6f70fe470 | -5.6188 | -44.81835 | 2024-10-27 00:09:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3eb0d874-ff88-31fc-91e4-fb4e6b223e22 | -5.61629 | -44.82525 | 2024-10-27 00:09:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| dc3265ea-2e52-3036-81ff-d9452d3e01d9 | -5.01414 | -45.43381 | 2024-10-27 00:09:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e5243d1f-5760-30d2-8bdc-4773a2a38714 | -5.01335 | -45.42889 | 2024-10-27 00:09:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 3385bd81-b819-3f3c-b715-4ffd6de59ef8 | -4.84857 | -44.83772 | 2024-10-27 00:09:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7f8e159e-2048-3644-abff-b09736f20135 | -4.52798 | -46.01041 | 2024-10-27 00:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8b794aeb-9d8e-38c1-932f-e41f40931199 | -4.43154 | -45.96811 | 2024-10-27 00:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 461c7e34-cfd3-3a86-8613-1defd2956149 | -4.32443 | -44.36723 | 2024-10-27 00:09:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b40c8ec6-948c-3873-b176-77e8a18721be | -4.28168 | -45.52306 | 2024-10-27 00:09:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| bd0fe3fd-79e2-3468-983a-d4cc49914cf9 | -4.27791 | -44.32815 | 2024-10-27 00:09:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8f3b6336-32ee-30bd-85ed-d3db69048d3e | -4.27013 | -44.33564 | 2024-10-27 00:09:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 93f65d5c-0dff-39f9-b33b-6fa048d079fb | -4.2668 | -45.52499 | 2024-10-27 00:09:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| cfe99e1d-9cad-3721-b606-2b105ff94f5f | -4.25882 | -44.66346 | 2024-10-27 00:09:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7ae0efb9-bd73-3cc2-9c0b-73ad892b66a3 | -4.25568 | -44.63987 | 2024-10-27 00:09:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 70b4a480-c6f6-34bf-92fa-1bfa7025e3d8 | -4.12551 | -45.1439 | 2024-10-27 00:09:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 49fd7a2a-6fca-357d-b4ac-1caa4efad007 | -3.87271 | -44.76842 | 2024-10-27 00:09:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 8497033f-139f-3abe-8ffa-7b7d02ca5b3f | -3.86744 | -44.78778 | 2024-10-27 00:09:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a1cc8024-8ed2-36f2-8c1b-8f69079eb88f | -3.76161 | -45.37501 | 2024-10-27 00:09:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d173328d-0244-3612-89b9-08a6635a4f4d | -3.75998 | -45.3804 | 2024-10-27 00:09:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 7bf717c1-5683-3566-9987-81d5a52b4d4e | -3.75895 | -45.92417 | 2024-10-27 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dd86881e-e2ff-39d4-adf6-cf3d4c7cdfd0 | -3.75633 | -45.91766 | 2024-10-27 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 904fcf1c-4019-3bd4-adb7-a42e62f32252 | -3.75493 | -45.89516 | 2024-10-27 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a6ffac7f-bb27-341d-a509-ebf015ac5173 | -3.69198 | -44.35254 | 2024-10-27 00:09:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4c66d5a9-4ea7-3c8c-b742-2190f733a319 | -3.68678 | -45.96371 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 33a66b98-8ce9-31db-8d00-8d9c0e9db30d | -3.6829 | -45.93442 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7b2d3442-1ae0-32c5-a37b-8e90318a831e | -3.67042 | -45.94135 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1bbaf86d-e61b-367a-8d1a-e33102904b7d | -3.66766 | -45.93628 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |


[Clique aqui para ver as próximas entradas](README3.md)
