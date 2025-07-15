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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8585b29-673f-3911-862d-3dbade45f480 | -3.58356 | -47.51397 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c7f9bc6-581a-3581-8ec2-6760e83dd9ca | -4.22696 | -47.76748 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73d713a0-dbfc-3599-a31c-4f3d137f5f16 | -3.38229 | -47.47555 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b45be70a-f25b-3890-a4f9-51a2b9eef0a8 | -4.68984 | -43.25117 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be3f934-fc7f-38a9-8851-1f437c57d48a | -3.58469 | -47.52822 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a55ba2b8-79c3-3bfd-a1fd-af909eeb0a88 | -6.28763 | -43.41632 | 2025-07-15 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab98ab56-46a9-32cc-84e2-b93bcf566982 | -6.4679 | -45.35477 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b79c041-b5c2-3543-82f7-2b6f633eab5d | -4.77617 | -45.34268 | 2025-07-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b2aee79-edf9-3126-8638-7993fff3edd5 | -6.28771 | -43.41743 | 2025-07-15 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67ce1516-b630-3d00-b86f-8a2524002ef2 | -7.20037 | -43.10436 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 845d51d2-62a4-3842-94f7-94e35e376496 | -7.89248 | -44.49591 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90390f16-cb24-3df2-b646-a67a5b6385ba | -5.53369 | -43.89483 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07754adb-d879-37a2-9851-b89f3e4ad30b | -5.77956 | -45.10204 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7db44e89-1d33-321d-9754-b697d401fbcf | -5.21111 | -42.50269 | 2025-07-15 04:32:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81c4e827-6f8c-33ab-9bd6-fa9b0c5f7dc5 | -3.75468 | -47.11861 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 343fa900-f869-3350-8dba-6e8e18f89815 | -7.09308 | -49.17094 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac99e50f-e592-3867-8cf4-de775a677302 | -5.78834 | -45.11556 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f77a1bef-287c-330d-ad21-60165fe29dd8 | -7.27874 | -44.04091 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4565c30d-ee3e-310a-b0d5-1cf7707e1d3a | -5.18363 | -37.63842 | 2025-07-15 04:32:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f9d33611-c55f-374a-8bda-aaef51b21df4 | -3.38283 | -47.47211 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e581dc9-7af7-316b-bee9-bc45de775477 | -7.66549 | -44.41108 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75d1ad1d-6367-3646-b1f0-f7cd0a658cd8 | -7.09122 | -44.39228 | 2025-07-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0deaeb1-d07f-34f6-bc29-728473bc3a9c | -7.41407 | -44.40723 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1547a5f0-49c8-3246-aebf-3ac3d3d30250 | -8.22982 | -44.92127 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1945c4ed-dff2-38a7-a898-445b94c8349f | -8.88068 | -46.8903 | 2025-07-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72ce9059-304f-3a96-8efc-eee69b433892 | -9.34398 | -46.1056 | 2025-07-15 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 612555ab-5616-34a0-a6a6-f64313e77812 | -8.22249 | -44.92012 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d25363fb-315a-31e0-9223-6ec78fb2d89e | -4.6182 | -43.32197 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffc134be-7ccc-3b84-bfaa-2912d5c49df1 | -6.16795 | -45.87698 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d0f303-76f8-35f0-bebc-ab069ab8cb78 | -3.38061 | -47.46472 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74d6cec2-d4d8-390e-9af6-ad856d3ba3fe | -3.58193 | -47.52428 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2184bbea-b4bc-34bd-8101-43f37ec479d3 | -4.03353 | -48.06547 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f16d3a2-645c-3203-af36-e1798fc6cd60 | -5.32625 | -43.73219 | 2025-07-15 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0500fe1-a3af-3a53-8046-91c336a41939 | -6.36505 | -44.74573 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 684de3c1-0dee-36be-b407-395aac93bde7 | -3.78681 | -47.08847 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0eb5d2-44f7-308a-88ad-ea367d0b1d44 | -7.6442 | -44.41927 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a13b3b-1e4c-39ad-a32b-4f235a93bf4c | -5.7011 | -44.24418 | 2025-07-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0b19960-f462-3ffb-aa2a-0fb7486a42b7 | -9.44039 | -48.40287 | 2025-07-15 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0898b6ab-6745-377f-ac59-0989c2af342a | -6.87722 | -42.7587 | 2025-07-15 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0210ca65-2144-3202-a750-63a7e3b7f59c | -6.29233 | -44.2324 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58f12aa-0203-3238-967e-a3c70c3bbf66 | -7.08171 | -45.64674 | 2025-07-15 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63aab4d2-80e6-37c2-bdce-4677ff8a49e3 | -6.7224 | -44.32998 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebc90852-0207-34f3-b3a2-168374208f59 | -6.85037 | -44.77687 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83954d85-f78b-33ae-8aef-e59b17a91217 | -9.81033 | -47.74885 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c78644cb-8314-3f52-8490-1a494279550c | -7.09563 | -44.38832 | 2025-07-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 084e9dc3-3b46-306e-9ca1-a59f9a57335c | -7.15858 | -42.96631 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e20af4c0-3cf6-3e7a-b830-e8c5623fe920 | -9.79419 | -47.74268 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50b09cf8-22f4-3728-8f45-59c043116716 | -5.33103 | -43.75172 | 2025-07-15 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd0c5a51-7a38-3df1-8544-a29793a4edd3 | -6.71229 | -47.79962 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d20e0256-4f5c-3b4b-979c-d58c49a04228 | -4.03794 | -48.05907 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9d8bd1f-455f-3e26-bb48-e7027e1981a1 | -7.09916 | -43.51073 | 2025-07-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adbff6df-9201-38ba-b450-12456bfc4fc8 | -5.69741 | -44.24364 | 2025-07-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3ecfb40-337f-34ea-8d70-a357210bea69 | -7.43093 | -48.09091 | 2025-07-15 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea67694a-25ed-3c4e-b221-8307c9a169b4 | -6.70899 | -47.7991 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 550eefb4-2ecb-3bc2-93ca-bdc4663ad9ab | -3.58301 | -47.5174 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3977866a-19aa-3473-87d2-916c9cab1937 | -6.84957 | -44.77792 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0260b27-ba7f-340e-953e-bf740084ff9a | -9.61864 | -49.10273 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4d6e983-0802-3f1a-9b81-7cc104820da0 | -9.90456 | -48.32274 | 2025-07-15 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6a5c6c7-a2a8-39d4-80d9-c3443d55b7d0 | -3.3945 | -46.90355 | 2025-07-15 04:32:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fcf62cdd-03ab-3be1-b31d-74d162aba872 | -7.28443 | -44.03558 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bbcce7f-ffa3-3dcf-a940-a188c1bad4bb | -7.09975 | -49.17201 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ec8e395-98f2-32da-9c4b-2cc03581ab75 | -8.23635 | -44.9242 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 259eb2a4-2ec5-3fc1-91dd-ca71ffba1c0d | -4.60282 | -43.31969 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fc7d291-0829-3b91-a6c4-40bc637c486d | -8.05102 | -50.08689 | 2025-07-15 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cda8aa9-b522-3e40-b3b5-0606032a86d0 | -9.94951 | -48.16487 | 2025-07-15 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75fb2d3a-be51-3dd0-a6ce-f8cb209aa2cd | -3.58139 | -47.52771 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7eecd3b-1f22-322e-9147-8b9e004e593d | -3.51576 | -48.43813 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b00209f-eaba-3c7b-bef5-ca9197732037 | -2.92189 | -48.24095 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fce2b867-a054-329d-8f99-cbf224761d71 | -4.48696 | -48.86647 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 679dbf24-c5f2-32c6-bddd-2f9428a97412 | -2.91856 | -48.24043 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ce08c07b-b977-38d6-8846-015e0a22bcd4 | -9.97925 | -48.08294 | 2025-07-15 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f53c73a-33f5-310d-a35b-74d792642c70 | -2.91467 | -48.24341 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5960dbfb-e699-388d-a930-c5a9daad861a | -7.89689 | -44.49196 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d131fc5-b43a-38be-8808-6628808b84e1 | -5.63183 | -45.33345 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f529c499-0408-31e1-b9d1-22ac060f2062 | -9.43822 | -40.31836 | 2025-07-15 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92c90bbc-d674-3f6d-8663-4fac4f6c2a3e | -6.14402 | -44.08152 | 2025-07-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f4c06c-c2bb-3c9c-b35f-de9e60432dbe | -6.84051 | -47.84849 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01756b23-752a-3ad9-b7b2-6f7c76e498e4 | -5.7837 | -45.09861 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 845290c3-226a-3ad9-8dbc-25f3b5d4fdeb | -9.90787 | -48.32329 | 2025-07-15 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06ff7ae1-1b41-3339-8c90-8faf61cca2d4 | -5.78724 | -45.09917 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcf60179-fcf1-3456-a264-90fca89acf12 | -7.09189 | -44.38784 | 2025-07-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1935546d-5af5-3be6-b4a9-34c1749d57c5 | -6.70752 | -44.32774 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72cddf24-751b-3a96-8c55-008b6f2dd739 | -6.70845 | -47.80256 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a1f943b-996d-3a6b-808d-c67d8539d3bb | -5.78078 | -45.09409 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c6f0d1e8-cd9a-3f5a-bf1d-3ba53ebe374f | -8.57282 | -45.54239 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50562e19-8358-3a1f-866d-82e1493377c9 | -5.18584 | -37.63768 | 2025-07-15 04:32:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 741d94a2-07c5-3af7-93ee-be5b7bf018d4 | -4.21771 | -47.30766 | 2025-07-15 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06797d53-c616-3acc-ab15-232980c9153a | -7.19634 | -43.10375 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0f2caafa-ac3c-36fc-ac1f-a3411a4e7f4c | -10.2761 | -47.61224 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc007e21-41c6-3df1-ab87-e4d845da4aae | -3.36185 | -49.16499 | 2025-07-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dab0f90c-f136-3f79-affb-b4396d6d42eb | -6.12791 | -42.96121 | 2025-07-15 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e9049c7c-b223-3b26-bf1f-29825ac7b21a | -3.21724 | -48.9707 | 2025-07-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 637f96ef-ab25-3bee-b79b-6b60d72c35a0 | -6.7329 | -44.33614 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a72e8d54-968f-3881-a2a0-49efda11c48f | -4.00749 | -49.47017 | 2025-07-15 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d944f54-f233-3b82-ae51-f3cbc3246a2a | -2.92244 | -48.23743 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f45560b-980c-35ba-b3df-a3fc256b1bb6 | -6.72918 | -44.33558 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86bd71cd-b385-32a5-9b85-57bf01ffc987 | -3.40158 | -49.54971 | 2025-07-15 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7838509f-a9ea-3e01-b43c-ce7963aaf36a | -7.09195 | -49.17802 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8d47b8b-3337-3ea2-80cd-8086e16647d1 | -4.77964 | -45.3432 | 2025-07-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c7d1dc5-3e6e-3da9-a595-27e325c25a09 | -9.80475 | -47.74069 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
