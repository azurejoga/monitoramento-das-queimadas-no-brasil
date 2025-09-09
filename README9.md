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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a7b98bd-c63a-393c-9480-e9aa4c125693 | -6.39623 | -44.43413 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 25873033-97c7-3e0f-99a5-0062194d17e7 | -5.57675 | -45.04231 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7d6a5d25-3531-3c56-99d4-95285943867f | -7.86841 | -46.25967 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c5ab786-cc55-3256-bf21-e6259429d562 | -9.85264 | -47.79877 | 2025-09-09 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff9fd68d-5ff4-312c-aee5-f60fbbb5dc6f | -11.37346 | -45.5937 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f003bee9-7842-3a17-85f0-99a8fd91446b | -7.08074 | -45.2079 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb21b0ad-c003-3708-9b09-e5a83b52b6f2 | -11.36579 | -43.52898 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3358cc69-1394-3e9d-a1ae-93b22e43aecf | -7.08829 | -45.19796 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dae2474-1804-3437-a685-2d6f145a6b3f | -6.48799 | -41.76365 | 2025-09-09 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9d349e9e-2816-390d-b3db-910528099a09 | -8.39693 | -49.1069 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 317565bf-d505-3971-8d53-86b77a629255 | -9.49629 | -48.28189 | 2025-09-09 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c442404-04ed-3b13-b298-39505931d57d | -8.35932 | -45.0416 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5b9ad79-04dd-30c1-a06a-f279b7b45544 | -6.69647 | -43.5424 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33afadc3-371c-33b6-ade0-26937363de73 | -7.57535 | -44.66127 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e2a710-12ae-3acf-bbd7-92c4ffce6ca1 | -5.81499 | -44.12151 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f3b8b95-9bd6-3cd0-aa83-23b085f0de45 | -5.3621 | -44.80608 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4d9a9c7-84cd-3cd9-8018-74d199e6f539 | -6.67103 | -44.55365 | 2025-09-09 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 721f6574-e491-3c0b-9a29-bb44dac5a237 | -5.58565 | -44.26545 | 2025-09-09 03:42:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a93f35ff-5e72-3344-8d12-515f60504206 | -5.67971 | -43.90709 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2574ad0d-fbd4-3caf-a92e-c15147307be0 | -6.08512 | -43.36024 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27de9c28-53b1-3302-8315-bac6b5ea65bd | -10.28819 | -48.82122 | 2025-09-09 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95efd947-3ddd-3e82-aca7-d5759c9cbe6d | -5.83577 | -44.21308 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89151ca7-fc3f-354a-9d89-7a5dc286f2db | -7.86919 | -46.25549 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e2e5d5c-01f0-3b9d-af66-289801d215ff | -5.67561 | -43.89983 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67042b5f-4d4b-31cc-b2de-ad0feff19975 | -7.82018 | -45.41736 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c00705fc-5f3e-3214-9240-343096044f3b | -5.94142 | -44.897 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15285549-ae14-35e6-85a7-cb280ca48550 | -10.33299 | -47.73927 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97a3c622-9b97-39a5-91b4-905f5e222463 | -5.54948 | -45.17675 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 451b5feb-a5f8-3bec-b653-3244ef54da24 | -6.43467 | -44.06171 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 573832de-0b29-3094-8d1e-cea3cf312173 | -6.05926 | -43.12397 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f30c0738-876d-36fd-8117-427ca846ab3c | -8.39746 | -49.10212 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49475b20-7ce5-3d5f-bb6e-400329e690f2 | -7.28455 | -44.56846 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6683b801-8fe9-3e3d-9b77-7bd7c3868a67 | -5.88674 | -43.95548 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63e1ac04-118d-3935-ab4f-4483a5b1ffde | -6.5598 | -43.15033 | 2025-09-09 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd36b88-4963-32db-a0e3-9300330420ec | -11.13267 | -46.35183 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18a05623-82b1-30cb-91a7-6c4c2432de0b | -6.20738 | -43.39559 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 439e8503-2b92-373e-b63a-098548d62511 | -9.13569 | -45.58073 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b36e23e-b2d6-347b-be65-b0fac677d133 | -6.40276 | -44.42832 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b80c1d2f-5296-385b-9aa0-a112dc2b356c | -5.81183 | -43.98352 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e39dfc2a-e7ed-3014-b8d6-8f126acc9c8b | -8.23178 | -49.54952 | 2025-09-09 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 058aaf53-4219-3fb3-9842-4d61a3ec9379 | -11.435 | -43.64131 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b3b1423-3a09-3128-897d-15f627b271ec | -10.9637 | -45.12408 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e53daaa3-7668-36f9-bc7c-1e51243a0960 | -5.87772 | -43.97747 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ed429c3-f266-3634-b745-cc42999656ea | -7.0213 | -44.94227 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4f115c4-8d37-3109-bdac-b53ab2fa87f3 | -10.96318 | -45.0978 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| df4b9975-d30e-3858-ac7d-67e47a5e47c5 | -11.36784 | -43.53712 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bfc1262-1d5a-335e-a4b8-40e3a3ad33d1 | -7.19495 | -44.88846 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06db63d7-51c5-3b77-a729-36d7ea3b7bfe | -11.41809 | -43.60217 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d81d82a-c4e8-3d8d-a504-dd48fc382fb6 | -11.41241 | -43.58075 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17732a98-3168-3552-a848-10a759b9ada0 | -11.37886 | -43.52924 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34c4b4ce-8a0b-3ce1-a5d5-0c732ef6d848 | -8.37486 | -45.017 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9b09dbb-5478-317c-9408-b46b49d2b2fd | -7.08208 | -45.20056 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92081cc2-2bcb-3d4c-9825-7e025d6b1953 | -9.82271 | -46.03101 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b831dad8-eb39-3892-baf3-752dd8b8742f | -6.20915 | -43.29837 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c64fa1ba-0b4b-3d5a-b769-eee2572afd06 | -8.03157 | -44.02785 | 2025-09-09 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af34ff58-31a7-31c5-9b6d-5cc971d144e9 | -8.05931 | -48.63242 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 03d8adbb-b714-31be-b555-55dd66aa5f42 | -6.47814 | -38.828 | 2025-09-09 03:42:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 340c21da-901b-3e5c-ba05-b3e3df9bb71a | -8.06415 | -48.65426 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e1e1a3a-46da-3be9-9f0a-d6127e0c5745 | -7.82583 | -45.41794 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a4964dc-5b93-39a8-b0c3-9e26b65cf789 | -5.3565 | -44.80526 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce3c83e2-3765-3fca-bc23-2ff002db9012 | -8.0542 | -48.63337 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 301153eb-2320-30b6-a68b-2c3aec0af8cd | -8.05308 | -48.63908 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1d4f437-fe51-3b31-a1b4-b723acc7b41c | -5.68383 | -43.9143 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0d71c78-6577-3662-9319-f4a400f3ff77 | -8.04743 | -48.65837 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e778d1b-46fd-3546-a8f2-ccd6e1b3c785 | -10.97765 | -45.11233 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| becc2a69-ff6d-3c8d-8655-fbf768d228d8 | -8.06268 | -45.52269 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0565779c-bc22-3ef1-bbc1-7e85e9d515e0 | -7.18518 | -44.91179 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b44d237a-eb8e-383f-a136-c851dc3b18cf | -11.15326 | -45.26913 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2fd97c2-e6fc-3330-a2d6-c307a32bf015 | -11.39463 | -43.54731 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7095b6f7-7e4c-318a-b0d8-fa1659ae4293 | -10.95493 | -46.80964 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53beb7fd-a338-3b40-bea3-3c3b0e7c84fb | -5.82084 | -44.11916 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9224252d-0aba-3f59-9146-20c9d498eed4 | -6.83104 | -43.62383 | 2025-09-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be856fe0-d0df-36a9-b83b-a94dbaddc7ca | -8.04854 | -48.65245 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 41b64f83-2f66-3f4d-bcd4-abff41fb3979 | -8.37465 | -45.03048 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 126ee5f1-f776-34f9-889d-568609f3a888 | -8.11397 | -44.86839 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86e95283-ff93-3189-9a4f-61831eaa31e7 | -5.67913 | -43.90894 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88e1a81b-d0e5-364e-91fb-2f21aa47ead7 | -5.68606 | -43.90163 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b16f7e86-9fb0-34bc-a884-2eba9a83fa35 | -9.14867 | -45.57193 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77898c3e-e83c-3e87-9311-ccba9bc408a8 | -10.97247 | -45.11143 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 33733aa6-c9d1-376c-9a7d-28678188539b | -5.84417 | -44.19669 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77c930b-e5ef-36f1-b402-37c6b2605051 | -11.41462 | -43.64767 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bc3a4bb-7822-345a-9239-c57d4ff8bf4a | -6.16726 | -43.39003 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 734eb9cf-0d36-347d-99a5-f31f0a4f86a7 | -11.40867 | -43.57503 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 601d5c1b-74d9-3e9d-a9bb-b9148654e9f2 | -6.38603 | -42.60007 | 2025-09-09 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4217140-68ba-3c1c-b3de-d67b97c08edd | -6.42881 | -44.06444 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b7f722c-ef44-3fa7-acf2-c5539f47c86f | -5.72271 | -45.40918 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48c1e889-1578-3b22-b26d-c9758a5d025d | -9.72521 | -46.78767 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7ed19a3-b2d2-3e7c-ad92-9e63708134fc | -6.42934 | -44.06147 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbeaf0cd-874c-3f39-b0f9-00b862e36ad5 | -6.22736 | -43.51802 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f03f0f5-bce7-3f3d-b186-4963e8636977 | -7.08854 | -44.14798 | 2025-09-09 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85aa8dc-58a5-3ad5-9ba9-4398d6070f6c | -6.30864 | -43.82285 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8806ab4-e664-3d97-989e-545c5b7aebba | -11.42076 | -43.58749 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a0dfe93-d1ac-3427-a89e-4b249b76fa60 | -6.18754 | -45.8103 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e16acbc3-b8f3-3c9a-909e-79fd89d10fa1 | -11.3909 | -43.54158 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd7eb0fe-c07d-3145-9462-d4d61baf8931 | -10.96259 | -45.10102 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 511bed2c-f6ad-3cf5-8b39-3e34c70ce627 | -5.67966 | -43.90579 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d88f5ac9-b342-3c1a-abaa-1c598d14051d | -11.4266 | -43.63463 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40ff47dc-5935-3d23-a09c-e1fea9b4d85c | -6.19894 | -41.0256 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6bdc1220-9aba-3993-a707-d89adf81ccb7 | -6.81863 | -44.90182 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60efb019-5335-3085-8797-e9f7e430c388 | -6.431 | -44.0521 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README10.md)
