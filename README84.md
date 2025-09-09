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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 184e3c2c-5bef-3e31-8c35-bcb0ff4518e0 | -7.5611 | -44.6597 | 2025-09-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 94d2fcb7-b47c-3ea6-b11a-db609b79fe27 | -5.8395 | -44.2103 | 2025-09-09 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7d8f3b62-fb08-3f24-a259-e58577f1fd98 | -6.2036 | -43.3709 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 895a5feb-7127-33fd-9b1b-30d8ae3766b6 | -5.7168 | -45.4035 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0821afb3-12a5-3e4e-9b79-bada445362ac | -12.5098 | -45.2786 | 2025-09-09 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 12a214b9-7933-3e07-ad4d-371c58fe3f18 | -5.9563 | -45.7915 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 4eeb3836-64b3-3ef8-b2a2-d06f2683898a | -12.2178 | -53.9005 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c7c54c21-7dc6-380a-8f68-71e9b1a9176c | -11.2196 | -54.9975 | 2025-09-09 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 730782c1-1182-3c4e-94a8-f2ad0fac1194 | -12.1991 | -53.8817 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 382.6 |
| 9c50913a-8fd9-3a33-943e-ff83d47206d6 | -5.9378 | -45.7704 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 32f74e01-8ceb-34bf-9f16-fd3cb7c0d0a2 | -12.967 | -54.7705 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 653e5bdd-0d76-3065-8120-4d3bf894d3b1 | -14.9266 | -55.8319 | 2025-09-09 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5dcacb65-192c-3e51-b105-b4ce812aaaa0 | -8.4119 | -49.0869 | 2025-09-09 14:20:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e881e176-679d-3344-94b5-13f0f2f5ec10 | -11.4482 | -49.2704 | 2025-09-09 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 3756b0da-41d2-3212-97e2-91641130b0a6 | -6.2758 | -45.6105 | 2025-09-09 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ec51dbcb-ea9a-34bc-9621-caba4774b61a | -6.1899 | -41.0154 | 2025-09-09 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 155.4 |
| c7756155-e094-3d83-943b-d663f5f5939e | -6.199 | -45.8186 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| da46b540-c2b4-3b13-8da9-f8fe53526b8a | -11.4469 | -43.5988 | 2025-09-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 46536b7b-53f0-3b71-a12c-c1a57a1b3843 | -6.8449 | -44.8847 | 2025-09-09 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| dfd7db3a-5753-3aba-832a-6fec92b9b694 | -7.789 | -46.0891 | 2025-09-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 6bae135d-bf61-3395-b8ac-da8c024854f8 | -12.529 | -45.2756 | 2025-09-09 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 81b8188e-2de2-38b7-9425-c8ced97b3c09 | -7.3405 | -49.56 | 2025-09-09 14:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e436bbb9-6af5-3e37-9da4-a7e32d445aa1 | -17.2967 | -46.7032 | 2025-09-09 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6368756d-5baa-33e3-be30-3b4e4fdd151a | -5.6418 | -45.4312 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 43ec5d29-589a-362e-88f3-d4ec5f7c4d2d | -12.1988 | -53.9024 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 256.9 |
| 7e4cbc67-1753-3434-ad1c-8b9b44ad525d | -11.7706 | -50.5901 | 2025-09-09 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 490bc9ee-c681-3e34-afae-0976f16e95c0 | -5.5506 | -45.1664 | 2025-09-09 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2849ed17-52e5-3bd6-9848-8a3b5256c784 | -5.6738 | -43.9 | 2025-09-09 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| baf9f4d9-0e53-316c-b787-906e9980df21 | -6.1992 | -45.7961 | 2025-09-09 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 46f60ce4-7725-3840-8f88-8ae81fe94d8b | -5.589 | -42.9048 | 2025-09-09 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 803.3 |
| c3dabc60-dfd3-34e0-a097-c5b1b63cf5b6 | -13.1367 | -54.9171 | 2025-09-09 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 4cbb990b-854c-396b-b3d7-0f07f9308f14 | -19.9545 | -49.2928 | 2025-09-09 14:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 194.4 |
| 09c7b987-4bf7-39eb-beed-9ccca403f3ad | -11.3552 | -50.4233 | 2025-09-09 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 6ecd34b7-f5b1-3421-8814-ec8042065593 | -7.789 | -46.0891 | 2025-09-09 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 97ee90ef-8081-3dd9-8aa2-e21122dccce3 | -7.5611 | -44.6597 | 2025-09-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5470b40d-d498-32bf-99c6-31b8ed8523bf | -7.8624 | -46.2392 | 2025-09-09 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d1e1fed6-606a-3131-8d7f-603b5a24ccbc | -5.8582 | -44.2088 | 2025-09-09 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fa3ad6ed-7707-3ffa-8b00-f6bd1c2778a1 | -5.6738 | -43.9 | 2025-09-09 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 9b153552-16a7-3fc0-bda3-616ab36def4e | -9.0232 | -49.7834 | 2025-09-09 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4ee37e1a-493e-3041-9b88-9120ccdc3f5e | -9.7857 | -46.24 | 2025-09-09 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 7d374bd7-05dd-3779-93b7-a6430265b0d4 | -11.4672 | -49.2681 | 2025-09-09 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f09b9095-b2fa-3c08-a4e2-857475cb46eb | -6.1899 | -41.0154 | 2025-09-09 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 1e3bc4ed-789d-3000-bce0-84f55dd5ebbd | -6.2038 | -43.3475 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e935de8c-9ab1-38dd-a2c9-036681ac7cef | -8.0606 | -48.6423 | 2025-09-09 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 230.0 |
| fc773367-dd88-3498-9df6-29790968b786 | -14.2757 | -44.9357 | 2025-09-09 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| af000689-7129-305c-9da1-fdbf5bb66e45 | -11.3202 | -46.5218 | 2025-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 90869ffd-0833-3b93-bd8d-bcec1e806314 | -10.2793 | -48.8168 | 2025-09-09 14:30:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8de77e6b-b9de-3103-8d4f-f6323f099d45 | -14.3231 | -47.3171 | 2025-09-09 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 139da60e-7148-3a7e-b303-cf78a3c9a873 | -12.2178 | -53.9005 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| bc79d842-8366-35ae-b09a-9af2959c6760 | -14.4664 | -53.2099 | 2025-09-09 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 38c68809-ab9d-3800-a60f-bd41f52216eb | -6.3572 | -43.0303 | 2025-09-09 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 461a3772-fd64-3895-a286-136575d31dc2 | -13.9723 | -54.0419 | 2025-09-09 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| af0bb30b-401b-3607-b7a3-276123edd5e5 | -12.6343 | -56.9725 | 2025-09-09 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 53d06b81-d2ed-3965-81b7-3bf5c0b31e38 | -13.9534 | -54.0233 | 2025-09-09 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 3d04e83d-8626-3966-b861-49d3836865f3 | -11.4482 | -49.2704 | 2025-09-09 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 2636855e-72b2-34f8-8df6-79fcd78bdaec | -5.5506 | -45.1664 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e8dc1bc0-d28f-34af-a945-43ae7f70f21e | -6.199 | -45.8186 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 75fe3f20-4a17-3769-9d1d-467fca2341e1 | -12.9482 | -54.7519 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 358.9 |
| 753b99e4-25b9-30f0-9f09-221ceda98c88 | -17.2956 | -46.7497 | 2025-09-09 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 29da07ec-7010-3461-b619-30fe6576f337 | -7.881 | -46.2598 | 2025-09-09 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 0f51fb6d-18ad-3fbb-afd9-e9b474714768 | -5.0438 | -43.1314 | 2025-09-09 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| c139f7f9-353c-3b0e-a075-523c5bbe2a5c | -6.8449 | -44.8847 | 2025-09-09 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9d02a21d-eadc-3729-a88a-50b88f33304e | -10.2982 | -48.8148 | 2025-09-09 14:30:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 82617c4a-a7ba-34bb-ba7f-4596be1772cc | -11.3549 | -50.4447 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 5fdaf848-23c0-3655-8afc-31442871f2b7 | -9.0931 | -45.7314 | 2025-09-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2a595833-f753-349c-bd24-2f8bc63e8eca | -8.3929 | -49.1101 | 2025-09-09 14:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 01cdacde-2088-3733-9ab9-37f31c6c360f | -5.589 | -42.9048 | 2025-09-09 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 194.9 |
| c1f9310b-25c9-3665-962a-0465f12ddf3d | -15.8201 | -52.2659 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b9f69abf-1991-3c8b-9eec-2be89c0ae089 | -5.6925 | -43.8986 | 2025-09-09 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 9498f4ec-bb47-3db5-a1be-efbac549aede | -9.3395 | -65.4451 | 2025-09-09 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f8240a57-2f74-35fe-9672-36b804e75e1f | -5.8406 | -44.0951 | 2025-09-09 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6d5800d5-16e7-30e4-aae6-e4ff92843c1d | -11.8156 | -51.4148 | 2025-09-09 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e10bea04-c4ae-3600-ab19-02486dd6ec3a | -15.5409 | -48.6419 | 2025-09-09 14:30:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 693f7d0a-b277-3e76-93a2-55d580fe34f8 | -14.2752 | -44.9592 | 2025-09-09 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 7407c7e4-09be-3b1b-801f-994abce95376 | -6.2407 | -43.4144 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7bbe7319-416a-3c8c-aa38-8577f31f7312 | -14.5601 | -52.2262 | 2025-09-09 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9d3997b9-a49c-3c84-84d0-acb9f668cc53 | -6.1803 | -45.82 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fd539ae5-a5b4-3365-96e2-79c8cd8872cb | -9.7203 | -46.8526 | 2025-09-09 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d950b48c-bd11-38ab-b502-c9f5c6896cd6 | -11.3011 | -46.5244 | 2025-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 305.3 |
| bd956e1e-050f-3a11-b506-f0ee847db095 | -12.18 | -53.8836 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 599ca0a1-7033-31ac-bfb1-8ead94599dcd | -5.8152 | -44.8298 | 2025-09-09 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9cb4db7a-e83f-382f-9f57-2f30ec642bf0 | -11.3552 | -50.4233 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 1cb17b9f-9fe2-3ef3-a5bb-6062f414251e | -11.3172 | -50.4275 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8e149619-e2c2-3e4f-9fb2-e45e5ce08dde | -14.4471 | -53.2124 | 2025-09-09 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d7fc3c70-7c18-3423-80fe-5b356e1c162b | -12.948 | -54.7724 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 0ff1823a-4157-3592-b819-1455eccb6ed2 | -5.2265 | -43.6774 | 2025-09-09 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1aba2691-43da-3ab4-8990-7afcf1a63808 | -5.3669 | -44.793 | 2025-09-09 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 85e588e2-eff5-3b1b-8442-d8885facea9f | -6.4096 | -45.3067 | 2025-09-09 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ccca0fd3-b27f-338e-adaf-e5d3d5873ece | -5.9563 | -45.7915 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 6b5562cc-f4de-3f7c-a6cb-7c9e6fd80d0b | -9.7014 | -46.8547 | 2025-09-09 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| aed1b37b-fa6f-391b-83a6-cba10efbcc44 | -5.6601 | -45.4751 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 102014c0-714e-3d5f-ad80-f89d690e4738 | -14.9073 | -55.834 | 2025-09-09 14:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 83382e88-d1b9-390c-a159-51fe8c74344e | -13.0165 | -48.0326 | 2025-09-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a366e6c6-7b30-30cc-95e9-1af8b0ba9fef | -5.5504 | -45.1891 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ffdd9105-0691-3ddc-b50c-9fe5e9b6d4a1 | -15.8205 | -52.2444 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| e21599b3-e1e3-3adf-b232-dc3cb99a899d | -9.3394 | -65.4638 | 2025-09-09 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 2d90eab3-42ea-3dde-8329-00cda2d24252 | -8.4612 | -51.4595 | 2025-09-09 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 98e68e68-5bf3-34f8-a1ff-354e510530f7 | -14.432 | -52.9619 | 2025-09-09 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| a04d2469-3c24-3a48-b331-e94da38dac93 | -17.2962 | -46.7265 | 2025-09-09 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b6dc867d-f641-3d9e-8cdb-bf1a5a03bf49 | -5.9899 | -46.2141 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |


[Clique aqui para ver as próximas entradas](README85.md)
