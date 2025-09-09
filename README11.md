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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f4d5ca8-7e1a-3429-99e5-93171a88a18d | -8.04377 | -48.64062 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8572dd3e-bc56-3a58-a038-a3753cc904a3 | -10.75043 | -47.74009 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 012b9345-d19f-3463-9501-30796243ec78 | -7.78773 | -46.08158 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335617ef-7eb4-3ee9-968b-8893cbfaf1c9 | -5.89226 | -43.95631 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918f80e0-abcc-3bbf-abc2-2e955d068d7c | -11.3704 | -43.52988 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b7d263e-00d5-3e67-b3c7-0eda0c8041db | -6.58881 | -44.01273 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b622c1ba-79f5-32b7-8030-1bc954b69d04 | -8.03864 | -48.64128 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b87fe33-f914-3e1c-a643-8ddfde8eb244 | -8.2032 | -44.83206 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2535414a-cf92-38bd-89b1-37634fe2c49e | -7.33675 | -49.56572 | 2025-09-09 03:42:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13ca79e7-e424-3acf-96b8-c4cd950f24f4 | -9.70166 | -46.81495 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 535d6362-8221-3afd-a242-e7902e634790 | -5.85478 | -44.19866 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fb3af3b-8fc2-3816-a0a2-b69956d19d45 | -6.8665 | -45.59807 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30bdec00-6129-34d2-96a4-32f849352b9b | -8.33777 | -45.06839 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd7d9cbf-a89e-33d4-9a41-32a26e91c0db | -6.88228 | -45.53492 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f580a7-3e5b-3205-b8bb-176a0453e0ad | -9.78873 | -46.23807 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 550b2a1f-5ab2-3509-a378-6036f5c2b56c | -6.83214 | -44.88949 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 077b261f-232e-3d5a-8030-7a91902c4726 | -6.43634 | -44.05225 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ab4203a-3f0e-3a2e-89e5-cd2bae7fb7a8 | -9.70251 | -46.81054 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fde4c92-6e43-364c-9862-f54a85bcadc6 | -8.37247 | -45.03033 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9cb4c10-cb96-3aac-a11d-7f6e9a1bb24f | -6.03772 | -45.01795 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f54b374-e2bb-364c-979f-7b3faa023020 | -5.79621 | -45.67032 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5eb466-8d85-374b-a2f0-071f79e73c07 | -8.03067 | -45.50834 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 545deca2-9193-3039-bf77-397a7495a631 | -5.57893 | -45.04557 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 56113a9b-3656-320c-a14f-de44e3d7c5d0 | -8.97018 | -44.94216 | 2025-09-09 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea955902-f5c9-3f91-87e1-26d1fc44a73e | -10.9673 | -45.11048 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6baa7c32-859c-3834-83ea-65fe0bc9bdaa | -6.1962 | -43.37137 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ede497e-4685-39a1-8a6e-0b494fc1ae05 | -6.56078 | -43.14481 | 2025-09-09 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53c3cb30-36ca-35c8-aa7d-be921df44b46 | -11.41613 | -43.58662 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46fd7fca-17d2-3d48-9ede-ada51e19d000 | -7.32394 | -35.13581 | 2025-09-09 03:42:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c31bd6e1-09c3-3281-84d8-d1152ffe1a64 | -6.82601 | -43.62291 | 2025-09-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb43deab-08d9-342a-aaeb-23486aba80b1 | -7.72203 | -44.74006 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6fcb4f5-abca-3344-8004-e209ae80512c | -6.2051 | -43.31887 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b9069b17-d559-3b38-bb7f-06ee89056812 | -6.87619 | -47.91246 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e41b3347-bae3-3a75-86f6-a59212bf1dff | -7.19433 | -44.89191 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e6beff8-a6f1-3efc-b9a9-8d5b48cb8efe | -6.92238 | -45.51847 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6d95c0c-1b44-333d-a708-06c0750b1d7e | -8.35686 | -42.23769 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0a0de27-0cef-37ef-afb3-8c1bf3fadfd9 | -6.86168 | -47.91719 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54a6d54c-09b7-36e6-bef2-0fa25fcb181b | -7.86997 | -46.2513 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a15e548-fe9a-39cc-ad9c-504929866cbc | -6.2279 | -43.51492 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f9414b4-7621-3272-a1fd-c4e5e85dfeb4 | -7.10745 | -43.89225 | 2025-09-09 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e36d678-935a-3165-8ab6-835012e34979 | -6.40388 | -44.45343 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 714b890f-f960-361e-84e3-9c9b2483abaf | -11.02919 | -45.93758 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5103989-641d-3c43-b3b4-7269182bbfd9 | -5.71441 | -43.89336 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce6740b-41aa-3d86-8ddc-430be8fb7025 | -11.43575 | -43.61056 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0046787-9368-3ae9-afa0-aa7f6e2358ae | -5.93586 | -44.89608 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adf24f32-b3f0-395a-91e8-f0a71a4454eb | -9.1533 | -45.576 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9b7394b-dd37-3608-b26e-0888056ffadc | -6.08515 | -43.3583 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465d2ded-8687-320e-a444-7b216c6ec1f9 | -9.72103 | -46.80952 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04c05920-b504-344b-8811-8e14007f1e90 | -6.2194 | -43.50404 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d76e38fd-e30c-385a-bad4-71553fe30fb3 | -10.16903 | -46.21785 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc9e02f7-0d55-3330-84b7-ab8d0e0080c7 | -11.39746 | -43.5579 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf5ca48-115b-39e9-9042-26fac3a9288e | -6.27429 | -44.48373 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0174982a-080f-389f-862d-c5eb1eea97b1 | -6.58938 | -44.00943 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9380dd06-83b6-3a54-8d03-e8e8bdac226d | -8.48009 | -48.27005 | 2025-09-09 03:42:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b99cb809-31f8-37e3-ba2e-b7898bda0de5 | -6.34324 | -43.78905 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8ab3b82-b508-3549-8eff-c16b04d4234b | -10.96693 | -46.81121 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 151f3cf0-56af-31d5-894a-0cc19cd6881b | -8.97081 | -44.93875 | 2025-09-09 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2934fe9-e171-3f7e-98b0-4fd528ba67dd | -8.47985 | -47.3154 | 2025-09-09 03:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f0bf9b3a-dd3e-32ef-954c-dba9767e638d | -8.33239 | -45.0673 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efda653f-53dc-31e4-872b-9f5de4386960 | -8.19285 | -44.76701 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77020e5f-01f6-301b-91b9-2496a55a47f4 | -6.34379 | -43.78594 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1a2ac50-926e-3363-aaa0-dfa2441feacd | -10.27626 | -48.8125 | 2025-09-09 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 474503eb-5478-3335-b2b7-404682bfbc1f | -6.25132 | -43.49959 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668d2291-7246-3d6f-880d-9c1ab593ccc7 | -8.04535 | -48.64279 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ad98f88-1e84-390a-8a0d-f4c8ecb699bc | -10.96601 | -45.11152 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9fbab206-faa7-3a82-995c-f5efb7920b19 | -9.09375 | -45.71586 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76ec8b96-62db-3b8d-b135-d9ea39570a4b | -7.80146 | -45.20893 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5537c04d-ad54-35e0-8f4f-3f73d60688f8 | -5.57326 | -45.04472 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f432c5b6-96cd-38ae-bb2e-ffef9909dcf2 | -9.84748 | -47.79203 | 2025-09-09 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6e6b5a2-d88e-3cd2-8a98-dada4ebb8654 | -10.17313 | -46.22699 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8a8856b-6904-359a-90bf-a109ff1c5efb | -10.33493 | -47.72925 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16f329a2-475f-3f7f-b287-7242dff31624 | -6.20787 | -43.39281 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67e132ca-587b-3697-b741-0c29ba8b84e6 | -5.79694 | -45.66611 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44950a95-98ba-322b-88a7-6f574145676d | -6.34585 | -43.79095 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29adea12-0972-3e26-ae80-211790efece3 | -9.35883 | -46.51167 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb6c6fca-2f9f-3931-b29d-10e41dd1cd54 | -8.02979 | -44.02916 | 2025-09-09 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9bd21d2-2571-3729-be42-f459aa8262bb | -11.02989 | -45.93382 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e01e6948-6e19-3dc8-96e4-4a6288923afa | -5.81075 | -45.65024 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e78018c8-4112-333b-b423-9aae7e8f3022 | -6.37069 | -42.57628 | 2025-09-09 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e526699-0e21-3ed7-b394-6ea274acbdb8 | -5.97941 | -43.70263 | 2025-09-09 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 156b9eb9-60e5-30dd-8cc9-524f5b706cd0 | -10.97889 | -45.10587 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 78c553ca-2f09-3f6d-b9fd-914eb1e8c9ee | -11.44339 | -43.64812 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cb16821-c561-3f0e-be72-20d1c783c64c | -5.92182 | -45.76405 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bca16c0-5a6f-3504-b2b9-7b602d8de797 | -5.58625 | -44.26196 | 2025-09-09 03:42:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09325069-d824-30a6-b2ae-4d18c277fbb5 | -10.97067 | -45.12086 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4dc07ba0-d1b8-39b1-830e-94c8c9b9989c | -7.78694 | -46.08578 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5622e685-4723-3d97-9de1-412fec77db59 | -11.3676 | -45.59567 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aac7c76b-a48f-3170-9e90-814a29ed2e65 | -6.36982 | -42.5813 | 2025-09-09 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d4dbb76-1dd7-3e1d-a482-a85cd1819d75 | -10.74213 | -46.33441 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8522aaa2-91b5-38eb-8626-ed458798df67 | -5.94029 | -44.89716 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96bbca33-9339-3319-b1e0-2a515352a885 | -9.72358 | -46.79618 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bb076a0-b92d-3dab-95bd-f4addb409312 | -11.36954 | -43.53473 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b350e22-def5-3ac8-96d2-33d94be9c395 | -8.0443 | -48.64819 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ed836c5-dbc9-3c8f-affb-4c8c8fc9c47d | -10.18432 | -46.22954 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 767b9219-a575-3d55-8ad4-c864e3cd60dc | -8.04952 | -48.64724 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f74d9727-6c47-33b1-9f09-354e40a8cc1e | -11.36963 | -43.52747 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2348f4f-41c5-3ed2-845c-f670f7284d7b | -6.20635 | -45.0319 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41278166-9aed-3cce-a448-fc4b68b7853b | -6.87838 | -45.53387 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71507cd0-ebab-30b5-992a-4c1b5c458eb1 | -6.09861 | -44.1323 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b66c9294-3a81-3d1f-b459-cb104d620dc4 | -11.44095 | -43.64954 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README12.md)
