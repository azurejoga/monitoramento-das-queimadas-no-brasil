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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d601c4b-ab3e-3f48-af0a-cd65e1dfbfe6 | -6.2418 | -43.2976 | 2025-09-06 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f27ee6a4-ce5c-34e5-8d56-ff1a2e86b92e | -15.3064 | -52.7208 | 2025-09-06 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 457213d2-65fd-3013-b425-c76431e13ba5 | -15.3067 | -52.6995 | 2025-09-06 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 6ddf6dac-b8df-3ec9-a480-2ebae850709f | -16.307 | -58.1055 | 2025-09-06 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 395b2d4e-5131-3275-9a23-7336477d6901 | -13.8407 | -46.2598 | 2025-09-06 13:50:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 99b994b6-7a4b-351c-8f72-03fde707443c | -6.2127 | -42.4532 | 2025-09-06 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| bfee651b-ef47-35fc-9cc2-e70b48dae9ae | -5.7183 | -45.2226 | 2025-09-06 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4875a489-7868-387f-ab74-3ede82920ffe | -9.7031 | -51.0802 | 2025-09-06 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| f19dff94-77af-3890-bc85-085bdf61d8e8 | -11.7576 | -47.7612 | 2025-09-06 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 06fd617b-2a97-35c7-afdc-98003b13df5d | -10.6128 | -44.3284 | 2025-09-06 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| d7c24661-ebd2-36fd-89a1-b1253412bece | -16.9246 | -45.7317 | 2025-09-06 13:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| db5da7ec-08eb-3621-bdbf-1dbc8c9cac41 | -6.1577 | -44.2317 | 2025-09-06 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 798a3420-e85c-3bf2-bc56-43ac6c623de8 | -6.2421 | -43.2743 | 2025-09-06 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ffe3e80d-2376-320b-920a-e220619cc13f | -11.3567 | -50.3161 | 2025-09-06 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 10616fb7-85db-39c4-af52-b238ebd08477 | -11.0245 | -45.9502 | 2025-09-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f7ddf4c2-4585-3ec1-9ea5-f4a76f1d89dc | -6.4021 | -46.0944 | 2025-09-06 13:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4cadcca6-7b5d-3c00-82b7-e268d00970f9 | -7.0129 | -44.9613 | 2025-09-06 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 1d19528a-c552-3df1-9e33-bdf5efc7ce36 | -9.6843 | -51.0819 | 2025-09-06 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 248.4 |
| bf30d184-4ec1-33c2-ae39-93fffd9d1ba4 | -6.1944 | -53.2585 | 2025-09-06 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| e03a5d82-8021-31a1-b0fb-07e133527c08 | -11.2651 | -46.3938 | 2025-09-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 58d43cde-2fba-3bcb-9c07-4f447a7017b9 | -6.2036 | -43.3709 | 2025-09-06 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 62a5019a-a59e-3185-9f60-8b5b3f7c3479 | -6.7419 | -51.975 | 2025-09-06 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fe5a3dfb-5cc0-374c-9d88-2806fb83b1e0 | -7.6881 | -50.2991 | 2025-09-06 13:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3e038194-25a3-34eb-a559-9e23e6841058 | -9.0948 | -47.0316 | 2025-09-06 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d39092e1-7beb-3890-8d9e-e91c3a79e27f | -10.2187 | -50.5223 | 2025-09-06 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 50d2d006-0228-3ee4-b6cb-86cf025d6670 | -11.6532 | -47.1512 | 2025-09-06 13:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6b48b8f9-6929-3a33-a4fd-c53272817ed3 | -8.5372 | -51.3488 | 2025-09-06 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d58eb8d8-00a0-3920-9b9f-3a7ed816f37f | -5.7298 | -43.9189 | 2025-09-06 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| c80c6c31-dcf0-3b1a-ada6-c85013511e15 | -15.7377 | -53.5928 | 2025-09-06 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| bf959a8a-2709-3cb6-8b81-a0eee7af58b9 | -6.2296 | -42.641 | 2025-09-06 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 67c94eef-f14e-360b-90c0-87415437b400 | -10.314 | -46.4022 | 2025-09-06 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5ba2db9e-47dc-3fe3-872e-fe32b63966f3 | -12.8028 | -48.1739 | 2025-09-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 28254cec-3009-393e-a445-5e0611256464 | -13.0044 | -54.8282 | 2025-09-06 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7bb68735-8cbd-303a-b7fd-e54c3e7cb327 | -8.1179 | -45.3125 | 2025-09-06 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| eff1be22-18ad-3aa4-a750-4c894efe7ada | -10.5937 | -44.331 | 2025-09-06 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| bab6e1ed-2532-3c3a-b2a1-1dc4f630865d | -13.8006 | -52.7454 | 2025-09-06 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| cd919495-0d15-3406-989d-d1ff83048806 | -4.4568 | -44.1413 | 2025-09-06 13:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4ff9c1ff-102d-30a7-9a53-b0086fccd41e | -6.2038 | -43.3475 | 2025-09-06 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3eb8d2d4-35b2-3562-9700-5c165fabe460 | -6.1945 | -53.2381 | 2025-09-06 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| ff75f793-b7b0-3029-a948-671f9f4111d7 | -7.7015 | -43.9312 | 2025-09-06 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 02e9726e-d5ea-37f9-b796-fc14168ce217 | -15.0639 | -50.087 | 2025-09-06 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 09bbaefc-e14c-31ec-962b-8849928d7e65 | -6.8281 | -52.8143 | 2025-09-06 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5fdfda4f-403f-362b-a0cf-152d04f7b3c5 | -15.0635 | -50.1089 | 2025-09-06 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 79210d34-abd2-3137-91dd-181ad22c0eb4 | -16.924 | -45.7552 | 2025-09-06 13:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 129.0 |
| f1bafcfa-85fa-3c24-a984-9b87c8188eb8 | -6.8095 | -52.8154 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2a737878-600c-3a7a-b8de-7fffac2949f0 | -7.6505 | -46.7268 | 2025-09-06 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| a5c82c78-8733-3547-8143-a7d6531b1860 | -9.0951 | -47.0093 | 2025-09-06 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 30b82e6c-6b0c-3682-9f61-bb7b273f6480 | -6.9942 | -44.9629 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 538bbd26-f8dd-3eb0-8e7a-923dff28f6a9 | -6.2127 | -42.4532 | 2025-09-06 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| c7f6c9f4-9441-3f27-a84a-1566f021f987 | -16.924 | -45.7552 | 2025-09-06 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 345d8870-0361-314f-8597-049af3c5a863 | -7.6881 | -50.2991 | 2025-09-06 14:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ebdbbe25-bd40-3685-87ca-91862d1ed8ea | -15.3258 | -52.7182 | 2025-09-06 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c3266571-a53d-3f91-b06d-2d2e95044fe3 | -6.5138 | -42.4266 | 2025-09-06 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 135b8b56-48f1-3df2-bd9c-132a007243d1 | -6.2203 | -43.5791 | 2025-09-06 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 49ed7996-b63b-3b32-a481-6b447a852344 | -12.8636 | -47.9877 | 2025-09-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f1d6b6ce-3ed8-38e6-9e7d-42430e3a7a32 | -8.4226 | -45.0535 | 2025-09-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 5eef052c-e94b-3eff-bde1-d20aeb802049 | -14.1061 | -51.7113 | 2025-09-06 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f10baff8-33cb-3cbc-90ab-5fe64f6aec87 | -11.0245 | -45.9502 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| acf37fff-e2f7-3c8e-928f-402223dff9f9 | -10.3327 | -46.4225 | 2025-09-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 52cb5e51-0965-38c1-9e9a-4075b12ff845 | -6.6954 | -44.829 | 2025-09-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5b59ed63-d6b3-3c37-bd3c-b563e8e18126 | -6.2857 | -53.4369 | 2025-09-06 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b9c31f69-9e5f-3e8d-b39c-fa8235ea6980 | -6.2205 | -43.5558 | 2025-09-06 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0f525385-74a9-355d-9b4b-f59b58347270 | -7.3838 | -50.9116 | 2025-09-06 14:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1d614912-e73d-396e-b741-524daa63d3ef | -7.0129 | -44.9613 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 3ccfac60-5e56-3421-8b4d-3f8b47fe23e0 | -10.314 | -46.4022 | 2025-09-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c14636ca-ad0d-3965-95a6-258597d27028 | -11.2302 | -46.1949 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 9b16a483-1801-3030-afbb-a24fa67ebd96 | -16.9246 | -45.7317 | 2025-09-06 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 609f7afa-07e9-3714-bed1-9cff7e6af579 | -5.8877 | -45.0972 | 2025-09-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 294a472b-6b11-30db-ad30-c35e09844abe | -6.1679 | -43.1869 | 2025-09-06 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 63.8 |
| fb2507f4-f2e1-39c0-806f-debf765fb9e3 | -20.2016 | -44.872 | 2025-09-06 14:00:00 | GOES-19 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c09bd999-32eb-3173-a285-2be5b8014a90 | -6.2296 | -42.641 | 2025-09-06 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| a5e481c9-f7db-38e2-917d-0aa5e5e17ab3 | -13.8006 | -52.7454 | 2025-09-06 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3b49dd02-4ab6-3f48-b3fa-56ce419f9550 | -8.3427 | -46.9515 | 2025-09-06 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 30606be3-31c5-3031-ad85-d02ab3198780 | -16.307 | -58.1055 | 2025-09-06 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 9da35873-346e-394a-8ec8-1f2145c706ba | -5.7183 | -45.2226 | 2025-09-06 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a5e2097c-c397-3564-a77f-7d66f4775535 | -6.7419 | -51.975 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 2fbc85f0-5b6f-3913-96fc-33c163ed6f6e | -9.6843 | -51.0819 | 2025-09-06 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 215.8 |
| 41e2c26c-3210-3c7b-a518-0af56165c050 | -10.5937 | -44.331 | 2025-09-06 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 1afe48bc-c19b-39ef-bd4f-e6f7db6115e1 | -11.2651 | -46.3938 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 0bd4ff2d-1993-3152-af08-905676775cad | -12.1316 | -50.6335 | 2025-09-06 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| f934583f-a419-3562-b10e-5b4fd55f1e8f | -6.2421 | -43.2743 | 2025-09-06 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 190f52a9-2fc4-3898-9254-548bcd2c8ab5 | -11.0242 | -45.9729 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 481e6670-27a1-3cef-b870-68203db29489 | -8.4418 | -45.0286 | 2025-09-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 8eee57e8-98be-3e8c-8be5-0bcf8498ad6f | -6.2299 | -42.6173 | 2025-09-06 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 9fc58a4c-b142-320b-b21b-33dad77e1709 | -15.7182 | -53.5954 | 2025-09-06 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 73e574d8-3377-3e7f-842c-44cc1136e5f3 | -10.3324 | -46.445 | 2025-09-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 90124c8c-ad9d-3606-a40c-492c62d945ba | -15.7377 | -53.5928 | 2025-09-06 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4febe52e-3a85-3448-b446-b25e0c7befd8 | -15.3064 | -52.7208 | 2025-09-06 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 3fdde253-2fc6-3135-809c-735a58d81be3 | -15.7381 | -53.5717 | 2025-09-06 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 15a550fb-8b3c-3881-9cad-3be9dea24dd4 | -8.0223 | -45.4354 | 2025-09-06 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b790de55-940a-3048-8a54-da9e244dafd3 | -4.4568 | -44.1413 | 2025-09-06 14:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 3caabcf2-e687-3d89-a98b-a1724c338395 | -15.3067 | -52.6995 | 2025-09-06 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 9fe0c0c9-1ba5-36e4-8910-07e3a0b1e3a6 | -10.6128 | -44.3284 | 2025-09-06 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 1a8d849f-90f0-3a1d-a84b-d02f0479fda6 | -11.319 | -50.2989 | 2025-09-06 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 77f18bca-3c54-3858-bc3d-1773e801c6ae | -5.7298 | -43.9189 | 2025-09-06 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 3d4b4ae7-8124-3ab9-83d1-ae5ead25b788 | -6.3058 | -44.4265 | 2025-09-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b1d917d9-db76-325a-9a13-905bc9047f1b | -6.4021 | -46.0944 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cdda8699-5fb9-3211-9210-ee4a9eab7522 | -11.3567 | -50.3161 | 2025-09-06 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| a515fa99-7021-31dd-9afe-ba3adb1eec8f | -8.1179 | -45.3125 | 2025-09-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d945ab77-791f-3299-9298-8e16f143e747 | -6.5141 | -42.4028 | 2025-09-06 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |


[Clique aqui para ver as próximas entradas](README95.md)
