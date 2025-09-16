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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ee11500-84c1-3606-93b0-274f4bacad3a | -8.22528 | -49.49487 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 105a696a-501d-30c9-96e0-e4d6c38eb6aa | -12.66298 | -47.71741 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db283ef0-cff9-3c01-a058-71cfe3ffd6d1 | -10.71457 | -44.73936 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47808fb1-8e6a-3947-97db-bd078e3ef022 | -9.05668 | -44.85172 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebc31f6a-b53e-31c6-a9fc-aef290bf16dc | -9.06878 | -44.83847 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 849b2da7-b12a-31e9-ae47-0a04689bf70b | -9.09534 | -44.86228 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1acc9c4d-0202-3853-bc5b-d9e3373506bd | -10.04879 | -44.34946 | 2025-09-16 04:51:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d812b2c5-c40f-3d35-b876-a3d60734da4f | -12.17814 | -44.10327 | 2025-09-16 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67b7cdf-7b70-30e6-84e0-8a7b04f26b9f | -10.07835 | -48.71246 | 2025-09-16 04:51:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e012af6-d53e-3308-bcbf-9ffb87f4b74e | -10.71998 | -46.50861 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| eb866c28-ac14-35c8-8065-3377d1a66143 | -10.07415 | -48.17976 | 2025-09-16 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31f041ec-ef17-32cb-b831-b2c86dc3eb7f | -11.11983 | -45.12064 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79ed3ac9-b7dd-38d0-ba45-ea8abcf5a8d3 | -10.71077 | -46.5072 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8f9e48d5-fb0a-3e97-b648-d444199c85f8 | -12.69288 | -47.99883 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51c3e294-2c8c-3165-9d4d-87801cc258e7 | -8.41099 | -47.85233 | 2025-09-16 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be91e4ac-940c-3d19-a3a5-b52d6f34d7b8 | -10.71141 | -46.50239 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d68986b1-ba75-3124-b48b-fa6fd4a1287c | -14.84919 | -45.51173 | 2025-09-16 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dbbedf9-0cff-32bb-ac19-f1cb883e810e | -12.10669 | -44.82696 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39b785cf-6bcd-368e-a6c5-cbd6d88c0f3e | -10.47771 | -45.16483 | 2025-09-16 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9218a12-2e12-353c-9af3-9e6a935f690b | -12.96022 | -47.98492 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 010e0324-44a0-3494-a805-53c53c69f98d | -11.12866 | -45.33177 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68a4fbdf-72af-3b48-9982-16189a6e0f20 | -8.98041 | -46.24857 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2afd9d75-e3c3-334c-b314-7d147c8308e0 | -14.91326 | -51.66383 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 465b95e2-96a5-3e57-b431-ab981ce2fe1e | -9.1019 | -44.85148 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82feeca4-9110-3d7c-8454-d5e6739955e2 | -14.91569 | -51.64727 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5be7ce27-1b0f-3081-bfb1-d6278328c8b1 | -9.10041 | -44.86281 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b4894c1e-250e-33f4-a600-9d793f6eecb2 | -12.62718 | -45.75933 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| accbf5e0-7904-35ff-9228-31228ded8f9b | -12.64799 | -47.95526 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 566b1870-90b9-31f7-b595-1b9cf04c11d8 | -8.87743 | -46.18368 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89a69d57-ae96-303d-a431-31ef6e888525 | -8.0327 | -49.83421 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b1c1c24-6a96-3c8b-8da8-cd54709b3104 | -9.05604 | -47.01684 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4211d9ca-65ed-3026-8ef8-12ac7a972fbf | -11.32949 | -43.48335 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c16bd6dc-512c-3aaa-aeac-fcdcf4ec4384 | -12.82767 | -47.22697 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc58861d-332f-35a9-872e-0eaef1992cf2 | -11.13333 | -45.33526 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4929d809-7bff-3879-be66-4d593945313b | -14.83034 | -51.66517 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b2dc5a0-173d-3fe5-9e21-2f8a2d87c827 | -14.38637 | -52.90169 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24982e8a-29be-36c7-9a50-ceed63bf7969 | -12.64312 | -47.95882 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d11ccb94-469d-33be-bad7-a43ea2cd87ea | -10.71663 | -44.76501 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e05164aa-3790-3684-b5ab-fd7e183cfcd5 | -12.9748 | -47.95977 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51f3bf02-b1e7-3b94-a52e-480a19c91be1 | -14.82973 | -51.6693 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ea9741f-c053-3abe-9731-a44fe4476d96 | -9.23436 | -65.32865 | 2025-09-16 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 553f8362-96d9-3a70-b5ef-eb654567e55c | -14.81769 | -48.12014 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a7e9d2-2b63-3a03-9d2c-3314a1274197 | -13.21472 | -47.30384 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e680b486-8f46-38c2-a149-354067300579 | -14.64665 | -52.09996 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fedeaab6-bb5a-32f5-a71e-0155bb08ede4 | -10.76536 | -44.71548 | 2025-09-16 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 116213b2-7143-374f-86f0-18f3197d7ccc | -10.71745 | -44.74997 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| baad3b77-aa10-3a0e-a0a9-75b141651483 | -10.11039 | -45.66482 | 2025-09-16 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0199153-d634-358e-b614-58ab5219a12e | -7.87584 | -55.38325 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bece4d42-76a7-3825-8f90-0474866ad6e1 | -9.05241 | -44.84525 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfb50e6a-d583-3a9a-bd90-0705e74c6e2f | -13.20403 | -47.27958 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d232ef3e-fc69-388b-87e9-52e9e967e7d8 | -13.74368 | -48.76802 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b790d13f-1d4d-36f2-a54c-16ff4df7ac91 | -11.12829 | -45.33461 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 895b728a-af9d-3972-a2e8-e601e44f6580 | -14.51302 | -47.32681 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f365d514-86fb-3d95-bdae-101e4ca7f63a | -8.8953 | -46.15668 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f45374a1-c2e3-36d2-94eb-0714fdd4eafa | -12.85601 | -47.15804 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cf18fa2-69bc-3fe3-8ce8-93865bbe957d | -11.1253 | -45.35747 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5bfacea-616e-3ddb-a94b-6d15bdc6c0c9 | -12.63074 | -45.77155 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 984599a4-8e40-3032-a0f4-2e55652fb7e4 | -10.37261 | -61.2575 | 2025-09-16 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f2b176b-5c86-30a9-9713-d303def23149 | -12.26714 | -53.92381 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24bd4081-42f2-36d9-8af3-ee73b204b275 | -11.7267 | -46.48526 | 2025-09-16 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc04014b-99f4-3761-8521-c5696c422e49 | -8.97913 | -46.25766 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| db25ef5f-2ece-32fa-9755-1af0ea6e8564 | -10.4218 | -50.64246 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a131daf3-1079-32e6-91e3-4d1ed5cd7845 | -8.64776 | -62.66932 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e446e182-b7d6-3d51-add8-2cb5b329e605 | -10.71538 | -46.50786 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 82295ad3-dbfb-307f-9117-8417732a33a7 | -8.60809 | -46.40529 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7734380-9457-399a-b3ec-9493cd02a75a | -10.72124 | -46.49915 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| f86df86d-993f-35b2-8603-fb6bad9761a5 | -8.58355 | -46.3499 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 447bdfeb-ce2c-31f8-8c7a-389e403ec4a0 | -12.79581 | -47.18857 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80f9fbc9-8618-3c93-b23f-52165ab47eff | -12.96274 | -47.9835 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38977ab1-ec32-3280-9f5e-178239bb9a25 | -8.70392 | -49.41459 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 595f1e08-9ef4-3ff8-9ccb-e18b924fc557 | -12.11576 | -44.84049 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a1a8f8a-17be-3354-ac6f-eb7579e7d1bd | -10.76494 | -44.71868 | 2025-09-16 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b75c0e4-114b-38b2-b93c-faaa83ff8cfb | -12.7658 | -47.96189 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa4b9974-a41c-348c-85c2-3094b65c5a2a | -8.60237 | -46.41336 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b4da44-31e9-3c93-b908-919d0b4f7df5 | -10.71541 | -44.76526 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88f14b73-c078-3a99-a31f-d383fd8f7645 | -12.79392 | -44.74667 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eb9f3d7-6dca-3dbf-b8d8-133bb021e514 | -13.00019 | -47.94812 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a2ed72f-4c40-3989-bd38-3aebd2fba8a3 | -12.8219 | -47.23561 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b51fc59a-e78f-3d88-876e-f7c2f1770b5f | -9.15614 | -46.97621 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26891941-6779-32a6-a989-36b657afd3c4 | -12.62647 | -45.76509 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62feb108-a58d-32ec-b3bb-dfa209f58550 | -13.19108 | -47.30839 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0780da36-5c95-371a-a0d5-8f8822d22b54 | -14.80546 | -51.66138 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fd839e3-0c04-3085-ad9c-647ec3643c18 | -11.4294 | -46.92999 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e7ebfe8-2c50-3ea8-9fdc-69c945669f12 | -8.12247 | -50.16884 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbe8edb0-eeab-3e8e-ad6c-d60c83cc82d8 | -8.67302 | -46.37965 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa9058e3-d5f6-302d-b9a2-e84d0b03fc86 | -8.43809 | -55.6203 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75b785c4-ed61-31d9-aca7-6743f6e03be5 | -14.45783 | -47.286 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdc31b16-b690-313f-bd29-e35b676c0387 | -12.75914 | -47.96253 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 308f210c-6834-3a29-8ed2-b42cc7899805 | -14.81654 | -48.12914 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee15e97b-d34d-3d31-8173-6a97997e2f77 | -11.27626 | -50.79856 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e050a67b-d40a-3ee8-8e0d-0549bc4a5cad | -13.18774 | -47.29847 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 602f12d8-8b8c-3661-8882-95f2f4d93f47 | -11.4748 | -43.58807 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aa58f56-e3e1-30b0-bfae-b87982d4ee9a | -10.71266 | -46.49287 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e5bed1d8-9cbc-3668-840c-b2acd6ae5827 | -9.73524 | -48.1103 | 2025-09-16 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d8ffd44-b962-36cf-91e2-45d85f0ca40e | -12.65514 | -47.93533 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94b5e196-1005-3213-aa2f-682453fb926b | -12.7911 | -47.25967 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a4f65c2-f495-39ec-bf20-64d9aa9cc193 | -8.42984 | -47.21173 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5e9ceb6-9075-3254-a0c4-096e70fff476 | -9.6357 | -58.9473 | 2025-09-16 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf43bb05-85aa-3272-8c63-e7fc6ce8501d | -12.65802 | -47.7211 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a055e129-c5c4-37b9-9c33-5a52ea292eca | -9.09728 | -44.85572 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README71.md)
