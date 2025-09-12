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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93f21f6a-d8c3-368f-900a-8ba441f32385 | -11.14911 | -45.29042 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e2dcb06-730e-33ee-8d7f-3bf898595c68 | -11.42413 | -43.53751 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a7f2a96d-7878-3d30-9569-127fd8b2f11d | -6.6348 | -49.78514 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d3629f-a017-38e9-844b-a4e8270b545d | -8.48454 | -47.27188 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f274a5e-d9e0-3205-8606-4724c0d10b19 | -10.14022 | -46.30756 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e68d287e-418a-33c9-8674-d5e57bfa80bc | -9.04783 | -47.06237 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 811487cc-c859-3fcf-8f39-a9b8c9990df2 | -11.40995 | -45.5988 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32df1b6e-b10e-31b8-a5ad-29970fee3a3c | -8.62431 | -53.11972 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 326b5c0a-370b-37e6-93e3-189a591da05d | -10.07905 | -48.17719 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72eeea1f-5e87-3da4-9b92-3f53d05b18a4 | -8.17145 | -46.09185 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fd11eff-d057-3020-8329-26867b124520 | -8.0401 | -52.33147 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d0439bb-11fa-3746-aa31-0cdb82036ce3 | -6.08408 | -44.82685 | 2025-09-12 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4f8a746-6f03-3abd-8006-9b84884d1132 | -11.68545 | -46.60902 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7846e207-f7df-3a1c-89a5-e307cd9977f9 | -11.67769 | -46.61505 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcf5bc74-4c67-3363-9d4c-3d3a555291a3 | -9.09409 | -46.94139 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4891c2d9-cf50-334f-a52b-c7397684e090 | -9.34928 | -46.5926 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9633519f-8057-35f3-9861-189cb00da35d | -11.69985 | -46.5602 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e2f0513-186e-336a-963e-cdab474f050c | -5.22541 | -46.05966 | 2025-09-12 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3647baa1-3ff9-36d0-8155-ab22e61771b9 | -12.08466 | -47.59551 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e9ea6c32-67cf-390d-9952-c6baac28bb10 | -9.45507 | -46.41589 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f383299-ec32-366f-998d-132bad1b3cd9 | -11.48386 | -49.26522 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc8cd17c-5a60-319e-89c5-dc40381effa5 | -11.51741 | -50.38318 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa8e5701-3bbd-3bab-a3d9-290d3cb8779f | -11.53436 | -50.40636 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 14beea77-0a8a-3e2f-ba15-7b0a5d1108eb | -11.84348 | -47.09855 | 2025-09-12 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 678fb8c5-f429-3f3c-8bd6-3138f09b60e8 | -7.73014 | -50.74961 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83e349ac-72b0-355a-88bc-f86f6f5cb1a5 | -9.59509 | -55.00335 | 2025-09-12 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ca50dbe-b663-346b-8a77-2bac62c3a5a3 | -7.55567 | -44.39031 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61c9e459-5e9c-3404-9d40-0520642a8f3f | -9.03624 | -47.11409 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e1403ea8-498a-34d9-b936-225272b0d9b5 | -6.47733 | -45.15765 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 258b321b-9311-3718-925c-d8733927fe7d | -6.29502 | -44.23428 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69cac88b-7565-3cd5-9d7f-8c9f7c378c1d | -8.05954 | -52.32188 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13668045-6a5b-3ee1-ad83-27c4f7b5c912 | -8.02775 | -44.80414 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23d5eb81-f343-32e1-a2c0-6585da8d9b98 | -6.30428 | -42.22371 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 93052819-2539-3d9f-93a6-da52888a304a | -7.69812 | -44.69445 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48079020-a11b-357e-a5ef-43c48ce63500 | -10.68217 | -48.65232 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fea434dd-3b12-3873-bb55-7e917b560cef | -11.67432 | -46.59265 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9ebfd30-d0d3-390a-8713-8561f923ce77 | -5.2887 | -48.12481 | 2025-09-12 04:25:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf19f934-07a6-3e82-aead-be6c70410b30 | -11.86206 | -46.7608 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db8aecde-1d5c-3f9c-8c83-cc7c673594ee | -6.20158 | -42.49623 | 2025-09-12 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48c35cb0-5340-3969-aea0-fb2b12319be9 | -11.69708 | -46.57804 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7b31e3e-0dc1-31a8-b55b-01273e554975 | -9.44789 | -46.41833 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84c7d509-fb30-33e7-975d-5327e050a91f | -8.07762 | -50.17233 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fab08906-4f67-31e4-bbcc-b2220ed12517 | -12.13547 | -44.83715 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c44dc46-adb7-34db-b80f-5ade6710404f | -6.67647 | -44.13976 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b295a448-ca7b-3300-acd3-6d981391a778 | -7.27693 | -45.16019 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5c3c5d7-fb2f-3e82-8b1f-de7e874bb404 | -9.01231 | -46.11969 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 374e5e36-e4b6-31f5-b7f7-03931a3c1110 | -11.67099 | -46.59211 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22923e28-4629-3c63-9640-1e9fbf4e9fe5 | -9.90972 | -47.77171 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70617aee-ae76-3cda-a7e2-981204856199 | -6.48294 | -43.8808 | 2025-09-12 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdaf476f-95e6-3152-94da-f87159b6e188 | -6.67251 | -44.57845 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba018823-de23-3d99-9a4b-b33d13610832 | -9.68393 | -46.77477 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 748ed76f-3793-364d-aa0f-0c6a3412dcdb | -9.889 | -46.46342 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fe1d1b9-e7f3-3e67-8ea3-6a05829138f9 | -7.07844 | -44.14867 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e04bce0-87ad-36b5-a522-eed7f9608e0d | -6.30736 | -42.22889 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bfe4ec43-6798-3c51-881b-f01f1ab62851 | -10.70647 | -48.63037 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e32f3e97-5acc-3c3d-87fa-98219fff4b30 | -11.75462 | -48.26203 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ac7af79-5029-36a9-ae7a-72712667691d | -11.66766 | -46.59156 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dc71f1e-cec0-3155-8715-a33f421dd15a | -10.41177 | -49.17119 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bf0dd74-0e20-3829-bbbf-7e640edbe346 | -5.40176 | -45.93219 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b6c60b2-be64-3403-8a98-cdb57e3d2014 | -12.08411 | -47.59903 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 641e0c4c-ae77-39f8-a460-7d5205696a70 | -11.68878 | -46.60955 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5fd6f8f-b659-3796-80d6-fd8a1bf7b515 | -10.84866 | -48.16777 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7292b700-a1b7-3aa5-b12f-6f3cc81a4b55 | -10.53588 | -51.53389 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 708d7c65-0d7a-3cc1-accf-49a76662dbf2 | -10.54059 | -51.52944 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aa87dc67-5f4b-3788-9be1-98967672088c | -5.75661 | -52.37857 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea472e83-a9b9-3e3d-937e-c37ea8dc0db2 | -11.69211 | -46.61008 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daee5d69-e37a-3719-9925-8aec61673567 | -9.67856 | -47.54003 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bcd4928-e1ac-32e8-bafb-47b7222dedfc | -10.70529 | -48.63771 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32b1bff-814e-35a3-91ed-2ccc654cf4d7 | -10.13961 | -47.90699 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 665b2767-c6b8-37c9-b9d2-1679a0e34fd9 | -6.21749 | -44.53272 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04340f31-e484-3e15-ba7d-372c91ab7e31 | -10.48394 | -49.3743 | 2025-09-12 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87a6f7c8-0655-3a6c-9c82-be2c21f0fc12 | -3.82306 | -54.11556 | 2025-09-12 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e408278-dee0-3c4a-8b82-77e66b7db835 | -6.10685 | -45.94091 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 684e6d12-8ddf-3390-b562-9377e4df31fd | -6.63846 | -49.78576 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e43230b8-6d2a-3115-b4b5-70304fac0050 | -10.35945 | -57.48964 | 2025-09-12 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4171becd-7316-3e91-ad75-3ee7667e7fa0 | -6.53411 | -44.77036 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a728dc10-fe59-3377-a925-57e465802bf1 | -10.57138 | -49.43885 | 2025-09-12 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8290958-3075-3c19-b09c-9f01faeee3c2 | -7.49298 | -54.95215 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aec56db-7a53-3d06-ad75-8b8e578a695b | -7.14915 | -44.34889 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb94dba1-e598-36ad-96ec-d94f5eaf6b69 | -5.49395 | -42.68032 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f4e855b4-7b5a-39da-9df6-fe3640d2b1d2 | -9.73612 | -45.42447 | 2025-09-12 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 442a2ef3-2e62-3405-be0d-8d53fd2b1a45 | -9.69404 | -47.54972 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e2135a3-271d-3e2c-b431-a9da77aac2f9 | -11.69376 | -46.59943 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 033c607f-44ec-3ed8-87b2-b5150dc6fe2a | -9.89038 | -51.89138 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 928ef842-0c33-3e73-8c6b-21ab6963736c | -8.95555 | -46.09243 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05b46296-7ea5-3df6-a1a3-9c026587d58b | -7.65504 | -50.27387 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 956f16f6-45aa-3769-ba76-9a829af5e493 | -12.5624 | -44.67931 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 448488f0-5588-39dd-b21b-890744e00b7e | -6.30499 | -42.2191 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 889b8cd5-efd8-3157-964d-1eb251c65198 | -11.08908 | -48.40878 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d33ce68-9dfb-36d7-a9a7-11ddd6328219 | -12.08522 | -47.59199 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 70e689b7-39eb-36b3-bc5c-cb6aaf016dd3 | -12.10427 | -44.87755 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecaeafb7-50a6-3d72-80d1-e1b3e8b72fd4 | -9.06658 | -47.11537 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0607429-f118-3fcd-b9d4-defebd09de75 | -12.5404 | -44.69004 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 329dcca4-db59-36ea-a983-3be7c0129515 | -5.65747 | -45.94793 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 581ff416-7f30-31d1-96ee-4fcd7ab0257a | -6.82371 | -52.79515 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2f0d33e-df55-3b6b-a6e7-a79058188dbe | -10.67821 | -48.65539 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b42388ff-ee3d-3ad9-b6f7-7d6a28ae3b0a | -11.20564 | -48.4021 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92c31098-0485-3964-926b-e00dbdf4c391 | -9.03734 | -47.0857 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a39f4b4b-4b72-3527-a9fb-91eabce773ac | -8.87945 | -49.54532 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbb39efd-a3d2-3f50-9df0-3572b82c5a36 | -7.75682 | -50.92155 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README73.md)
