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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e7e525c-de91-3392-91eb-14e620ea477c | -6.17507 | -43.32163 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a1b53383-599f-3e3f-afa2-7a7ae066c458 | -11.33655 | -43.62887 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f916ad-eb47-3e2b-834f-60ee3c55ebf6 | -6.57556 | -43.69589 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c089fd68-fc85-388d-aec4-801e59a09ca2 | -8.97239 | -46.73442 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31249538-26e8-3ceb-bb51-30a4969f2119 | -6.44947 | -42.39925 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9fed8056-196e-347d-b7ae-6e2d5c9af985 | -6.22983 | -42.41174 | 2025-08-31 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8258f90f-f0f8-37bd-b61a-99dd593dafab | -6.82945 | -43.33528 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 08808d6f-8a2f-3b04-b13b-be7fb5f03318 | -7.58293 | -42.711 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e79e4f5-e145-33c1-892e-a1c26407b39e | -10.14046 | -48.47257 | 2025-08-31 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56967fac-dc60-3f64-ada5-29cb153a04c2 | -6.71306 | -42.242 | 2025-08-31 04:02:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7db45865-77f5-3b71-bf0b-f52ed7beb715 | -7.37974 | -43.40123 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08a808d8-f250-39a5-9c11-b381eaf4f407 | -11.34286 | -43.63389 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 48462fca-931d-3c50-a2ae-9cb560ed54a9 | -6.16492 | -44.12951 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8e18f6c-8059-3e45-9139-2632c739e403 | -7.32679 | -44.36533 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28af1b40-e0b6-3ead-919f-fba01a28cc02 | -6.18392 | -43.33599 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33cf40a9-1dbc-3f11-9513-6d3619de65f9 | -9.59871 | -40.35506 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6366c7fa-a465-3a75-a943-4fa73914c7a6 | -3.80136 | -47.56987 | 2025-08-31 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b0b6323-fac9-321e-b952-c1acc8eac3e6 | -6.29963 | -43.52611 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 856a2b62-cf3f-3d7b-9250-f18b186cd2a6 | -9.54244 | -45.84387 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b41d29bb-7f9d-3c74-80aa-e1b6eb728b02 | -6.33342 | -42.52247 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11542c35-504b-33bd-a247-21e6d7bcf84f | -6.48986 | -43.55613 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ef71693-c0c0-34a7-8d7e-bc4da4b4f017 | -6.18398 | -43.56691 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c1add0-ce37-30a4-9145-61ca10a56971 | -9.68183 | -48.30177 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 836e6ff0-01a6-3a50-ae80-823ba54aab0b | -8.39146 | -48.26889 | 2025-08-31 04:02:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9c8085d-d2ee-322c-b5c7-f3f2816eb7ec | -11.36439 | -43.58946 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62cdde3c-be3b-3276-8375-c2d35cee98b8 | -6.17651 | -44.12926 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 728cfe3c-f5a3-3fbe-9f89-a31b07110eaf | -9.59432 | -40.36152 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 39e31527-5cab-3a79-8237-46c4b3e9823c | -4.27469 | -48.63717 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df7792b6-6f97-3635-8944-d9fab2f3ba36 | -4.15438 | -46.78216 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a300473-c87e-3294-a2b0-1dc75b740a64 | -6.95797 | -42.01043 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a048a8aa-38ab-3cb4-b89d-c3e0b4e26c87 | -8.84217 | -47.49077 | 2025-08-31 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 498c3fef-d159-3ce9-aaec-f8a8ac971e8a | -7.23326 | -44.22364 | 2025-08-31 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02884784-e7cb-356d-aafd-6f06905b33e4 | -11.06396 | -44.61677 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8e7af8-9898-30b8-840d-daf7e1ea0b82 | -11.29977 | -43.57071 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de5d63b4-51ec-3e31-8b31-4f5e65511909 | -6.45043 | -43.95451 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d9776e9-f74c-395c-a387-5dfbb7198459 | -11.30164 | -43.66723 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5c12021-961c-3f52-a5b3-686a5842236c | -8.29907 | -44.92419 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43b096dc-d1d1-3523-995b-89f1c9bdd3ea | -5.79992 | -43.86927 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3beffa24-8861-33f9-903b-58721da6849a | -11.29347 | -43.56571 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b454060-aa4c-32d4-b4fe-c8184938e1d5 | -6.18102 | -43.56201 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8316a7c1-102e-352c-a33d-b04dc9b6bb4d | -10.03902 | -46.02458 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c6c2028-37fb-35ea-abe2-e5a754b2bec0 | -9.68466 | -47.04125 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2abe9aa3-b2bd-30f6-a1ae-30bea19e1be2 | -6.17508 | -43.99477 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6006b6c4-0215-32b1-b79f-d5586ac33841 | -6.53658 | -42.96747 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba11c3e9-c365-39a8-9904-d43dbbb064cd | -9.01262 | -40.07962 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c5ff407-307e-3b87-a6d1-674e09f267af | -10.03647 | -48.08281 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffa4387d-2fcd-33a7-a66a-8ff4671f0cbc | -5.2516 | -44.45339 | 2025-08-31 04:02:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97a739b2-bcc4-35e4-9eb1-fdb0c380ec7b | -6.88736 | -44.43391 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea534cd-8ed5-3ecf-9016-2229e3a9074f | -6.44886 | -42.4031 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45f931f4-88f2-3b0c-91ba-5786643316a9 | -9.26023 | -47.06535 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27cca6ce-1333-3183-9571-8d465ba99717 | -10.93804 | -46.83939 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a3526c-dced-33b3-9983-4e2fc0111f70 | -8.86401 | -45.75146 | 2025-08-31 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 30589023-9b27-34f7-bb5d-fb0eacfcfb28 | -7.16442 | -45.15977 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f99cfe5d-e64a-3332-b2ef-dcf23fe5162e | -6.43735 | -45.6116 | 2025-08-31 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c0e272f-fe8d-361c-9acc-214bf928ec62 | -11.29631 | -43.57012 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 240a8b8f-2a34-3acf-82a5-b1a4f7e3b2a5 | -6.32813 | -43.53546 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e6fd8b2-dc36-3992-a3cc-c65dd5070c3b | -6.77172 | -43.76298 | 2025-08-31 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 350f9826-0ae1-3607-9804-6bf518b5d17b | -4.73649 | -44.45073 | 2025-08-31 04:02:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c480f00-8b5d-3e15-8c0a-c028fbfcb0fb | -6.85923 | -44.44501 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a79f959-ce66-37da-88e2-1a9016d81e2e | -4.74045 | -44.45133 | 2025-08-31 04:02:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 996eb841-24bd-35a7-a3ab-b37c0eab4e5f | -8.10024 | -46.26746 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce3f26a-1886-3068-ab1e-97dabd6db139 | -5.48243 | -44.39814 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3062fd6e-f3b2-3d46-8606-ab80b55a566b | -3.8063 | -47.5707 | 2025-08-31 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0cd90f9-18e8-3e51-a74b-a46c5fe773b7 | -11.36376 | -43.59334 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4015e207-6be3-399c-91a8-7d466f09e62b | -6.95379 | -42.00951 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3874e14-a11c-31a9-9a84-e5d9d85bc10c | -6.71221 | -51.42267 | 2025-08-31 04:02:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 107c260a-8076-3dc5-8f92-cae4aa896c0c | -6.16986 | -44.00317 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a49839a-ef30-3c28-96e3-076d4b7e92c9 | -7.74382 | -50.26449 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 07281145-974b-3da8-b14d-de3deb681f00 | -7.40264 | -43.39641 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60bba2e5-5148-36a8-8f56-147e45f5205e | -9.4494 | -40.68052 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a92cf9a-6dd2-34b9-9e2a-e0e42f3a2b92 | -6.71247 | -42.24569 | 2025-08-31 04:02:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f940d89d-52da-31cd-a066-ffba2d720187 | -11.31863 | -43.69438 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ec543b-f717-3d8b-96b1-d0f1061bfa56 | -5.80743 | -43.87044 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 563531e3-af2a-3ffc-9ffa-7a932b3c5569 | -6.16815 | -44.13267 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 365a05c1-d20b-340b-ba3c-bec96aa3a6f4 | -5.7973 | -42.55904 | 2025-08-31 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91e0fcbf-3b73-3adb-9c96-d17889e06561 | -7.97138 | -46.41401 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e80c9da-4710-31a0-b36e-c559a77460a2 | -7.58456 | -42.72309 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 218e6153-59b2-34c2-8c2e-4748acf08357 | -6.17628 | -44.13149 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e369040e-669b-3f72-9251-360a922a36ac | -11.33719 | -43.62496 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62465af2-963c-313a-ac6c-ee2172b3b5ae | -11.34705 | -43.58654 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbeeb76c-5ea8-3780-ba5c-f140278caa02 | -5.83862 | -42.52584 | 2025-08-31 04:02:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8fc0b047-e3a8-3f45-85cd-6e0653a3f03b | -11.32793 | -43.65958 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51ec07b5-5e39-35f5-a714-8c1c8c9fcc3f | -8.49622 | -44.74091 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9b549b0-bb02-31a1-91b7-29835fbd07d9 | -8.19563 | -42.30568 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef0a48c0-3be2-31c9-8676-38caf846eeed | -7.0947 | -49.92566 | 2025-08-31 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be272fff-7ac8-356b-bf57-2dc93ef52ca3 | -5.4646 | -42.57345 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9681d4d-9a35-3acd-98c0-8e3d63ff0213 | -6.17895 | -43.34378 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ac8590b-ec5b-3683-8745-480f41f0f47b | -4.30525 | -48.09802 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb12b7a2-d8ca-33c6-9752-48dfe7630e30 | -7.97412 | -46.41758 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f94353c1-afe7-3403-a054-26bb206f4f97 | -6.33277 | -42.52642 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f098a460-19df-3d67-9f5a-f115c36a9a46 | -11.34051 | -43.51796 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 580756ca-0950-3253-ad95-bbf7db576f14 | -9.51286 | -45.4014 | 2025-08-31 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c19f045-0640-348b-b011-259a36c1dead | -5.98883 | -43.36158 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9d17d099-366a-3c6f-b787-e2feb35222b2 | -8.00348 | -44.05436 | 2025-08-31 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3c20c47-5207-3309-8cec-fe3f6cf1de21 | -7.66204 | -42.65261 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6bfeed0d-23c3-3858-b828-4b2133f4ca8b | -6.52433 | -42.95325 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d3e9837-bcbb-36f1-aa41-7b020acffd14 | -6.96247 | -44.31177 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed6a858-09d1-37a6-b44f-f2bcc0cc98dd | -11.36123 | -43.60884 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd472a06-1479-3b7f-b097-529cbd027ebd | -8.49923 | -44.74626 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 114ed88b-b95e-39a5-938e-40643739336c | -7.63678 | -46.5577 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README22.md)
