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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1660836-5ec3-30d3-856e-30b679fb865a | -6.57604 | -43.69751 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6021da46-4daf-3d83-bcdd-f588a35fa00b | -11.07275 | -44.63157 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae6e14e9-906f-3229-afaf-37b4a3999232 | -9.69298 | -48.29354 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc1f3116-c8b7-3685-99eb-01ff2e4975d7 | -5.13722 | -45.03419 | 2025-08-31 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a406e00c-5400-3a31-a648-3783dcdb37db | -11.02521 | -46.88282 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66879251-9583-3cdb-a194-bd0af796ea53 | -11.83468 | -37.5724 | 2025-08-31 04:02:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9796d1a3-3f24-3ec0-a312-80894adc8f22 | -11.30925 | -43.66447 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3957b215-01db-3adf-93c1-3fdfa5f2813d | -6.46196 | -42.42436 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f0c9e779-d562-3b90-9131-73f0a819b089 | -7.62151 | -42.66161 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbe386bc-29d7-307c-bb04-9035f9c41b9a | -7.2278 | -44.06913 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83a7d204-5ac9-362d-96bd-e3a6118370b6 | -8.46459 | -43.62794 | 2025-08-31 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2640eca-fd8f-342c-839a-dfbaf5b105d9 | -7.75462 | -45.45782 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e08bf4e-07e2-31c9-835e-9c9139226bcf | -7.77127 | -45.45708 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 556735a9-c1c8-3eb5-bebc-79e899d4f3d3 | -6.53368 | -42.96291 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74acafd7-2f63-3d00-b664-51be9cdb3664 | -7.96987 | -46.41674 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 664fa452-606c-3b61-a649-a45b1766899e | -8.55264 | -51.30192 | 2025-08-31 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3984c525-6962-329d-a5dd-6ed60442ba39 | -6.17949 | -44.13468 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0cb4e9-8d03-318b-80ad-74a118f3b57e | -11.35868 | -43.62445 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57d44bd6-42f7-3344-99e0-b2e04cc992e0 | -8.46102 | -43.62732 | 2025-08-31 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc136ca3-220d-37c5-b9e1-86a1af413b58 | -10.60908 | -44.32391 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9645f559-8817-3efe-8312-af63288ebf89 | -8.29668 | -46.3129 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7904e1b0-4cf6-3e50-a489-9357518b8ad4 | -6.28729 | -43.53263 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9987a976-4ca3-36c8-b9b6-d22398f5cf60 | -11.064 | -44.63903 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87adc274-83c6-3f30-a9e1-0a9ce60a6a75 | -6.44971 | -43.95887 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ee43ed1-487e-34a2-b27d-e7bbc1a1d803 | -6.48882 | -44.07262 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32554190-794d-37c3-990c-9feb8d03cb74 | -6.77092 | -44.64401 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b28f4c91-3d17-32f2-9480-1216809f7acd | -6.30833 | -43.51886 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b99536e3-a018-3ef0-9ecc-dcaed6898350 | -6.17962 | -43.33958 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99b4f32c-96d7-3824-80cf-46b043c0efcd | -6.12627 | -44.05685 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd9cbe21-f24d-3a21-90f3-3d309a84d643 | -7.97481 | -46.41365 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7888e39-5aa9-3549-87c5-6727097ad784 | -11.3644 | -43.54577 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 229cb52d-a754-3da0-b837-73baef5d3513 | -11.36249 | -43.60109 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4dd62ca3-1f76-3a4c-b373-2ccbff4625d7 | -11.21365 | -45.04539 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83137325-5e8f-3889-bb14-7a8efe7866f0 | -6.15659 | -44.13292 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07dffd12-4a62-39c3-a499-acacde8cc944 | -6.0082 | -43.42598 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c79fd688-1dad-3e41-8534-303fc6d35508 | -10.03566 | -48.08736 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 39f8ed48-c306-3a5b-a893-303f5b449965 | -4.07102 | -47.95742 | 2025-08-31 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42b70cf2-e289-35b7-9584-2f65335c9c80 | -11.36817 | -43.56626 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f552ad7e-8a01-3c27-bcb7-5bff7073168e | -6.25048 | -42.40726 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45c48dd0-264a-3f0c-b2be-79fd67461516 | -7.33184 | -44.09871 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84d93977-6589-3da4-bed3-bb2b3dc381b8 | -11.31993 | -43.68652 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 426e7713-b762-377a-8e61-80c2cd1d8425 | -6.48915 | -43.56053 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cf8305c-2051-3b55-b2bb-951e9ca3c689 | -11.34761 | -43.62668 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1682b4ff-a60c-3288-96b0-1fca5022c96b | -5.84914 | -42.52748 | 2025-08-31 04:02:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ee12f99-1251-3aa0-8827-bce837ed00d8 | -6.33563 | -53.4374 | 2025-08-31 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8da221c-c813-36da-9184-9d0d4480b7a7 | -6.94353 | -44.05452 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1c67f7a-1e92-36af-88b9-3298148b8aaf | -6.00969 | -40.22874 | 2025-08-31 04:02:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1f5a086-7f05-3fbc-ad96-e0b21435a7d7 | -11.21071 | -45.04006 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd13a1fd-0929-37db-8426-61ab6d4a9d4e | -9.60256 | -40.35209 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c53de363-df9c-34ce-ac7b-8549c9ecffb5 | -7.65228 | -42.64713 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 113518ae-f15f-39c5-aeef-b134babdd911 | -6.4249 | -43.96152 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b54c7f-a2d0-309c-899d-38c06da6fed4 | -6.95857 | -42.00674 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5979701e-0416-3ca1-8bd2-45b4b1b20acd | -9.25643 | -47.05704 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d77deb41-b557-3eff-8f4b-709875e9b180 | -10.66708 | -46.26591 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 406593c9-05eb-3478-bdfd-29255ecb5cc5 | -9.58824 | -40.35698 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9e2066b6-5b1c-3a4e-935c-990e86aab90f | -5.88777 | -42.96367 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 17af4c9d-46a7-36f1-8e11-50e165aa46a4 | -7.10292 | -44.30882 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee18bc7b-e96c-362d-b720-a1a6f9f86b8e | -8.01085 | -44.05555 | 2025-08-31 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44502275-66c7-3a45-b872-c192c60d1d3f | -10.99815 | -46.93915 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4166b53-3944-3736-921f-120e9ba1b286 | -7.40121 | -45.92462 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aba3e6b-d1bc-3630-85fd-782e4173f8df | -6.1301 | -42.94656 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c7c7ebe4-3055-3d66-a6b5-a98446d0bcb7 | -6.94575 | -44.05594 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a034ee3-528a-3f28-8dc1-f97f176d4755 | -7.7753 | -45.4577 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8fee401-e164-3c83-aa1a-3807f0279f3b | -5.83167 | -40.99144 | 2025-08-31 04:02:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3b210ff-6dfc-3aa6-b6ae-f4e180ea9113 | -10.93193 | -46.84281 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfb85d75-181e-34b2-abf0-dce3b24b0f84 | -8.96338 | -50.01205 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee318d37-28f6-35ac-b80d-1746db5ef1ce | -6.88824 | -44.43565 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2aefadf-121f-390e-bb5c-1754b207300b | -7.39799 | -45.92764 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 466f1312-aa8a-3047-aacd-e6909feb8afb | -5.83449 | -42.52917 | 2025-08-31 04:02:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 760e2418-0aa9-3832-9c78-d250ac1e21d3 | -4.51169 | -42.90938 | 2025-08-31 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b607930d-9a3d-3171-a4d7-7071fa36d4c7 | -10.03494 | -46.02423 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3feedc29-7744-383f-8f6b-7ed1b8564ba2 | -5.58585 | -46.32637 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eee4e84-bc13-3db6-ba11-dfa6dbddeed0 | -6.88748 | -44.44033 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c946106-89fe-32d1-925c-2d5ba327c882 | -6.71304 | -51.41807 | 2025-08-31 04:02:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| ba68c98f-23bb-34e1-aabc-ac3d9bc72680 | -11.28746 | -43.64487 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48a33aa8-5ff1-3299-b5f7-59dd9bcf2f6d | -11.36377 | -43.54964 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bbe362f-1fa3-386e-b11d-013c21c9608f | -10.42119 | -50.85942 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7038d302-a3c1-3377-8d33-cc44737655e9 | -7.38114 | -43.40205 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f929e81-eae4-3411-ab85-7259cced167d | -6.25129 | -43.38454 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b21286ee-76b3-3bc9-8193-d85b35a91c39 | -6.97247 | -40.94335 | 2025-08-31 04:02:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| bcb50b8e-cc3c-321c-9f5f-d6c4f1f9c98e | -6.24385 | -41.81822 | 2025-08-31 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa0676d2-0c8b-3d76-827c-be19b2294074 | -6.24766 | -43.3839 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d49546bb-36b3-3452-8f70-82d37c6fe8bc | -5.73677 | -44.11256 | 2025-08-31 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 190c330e-f03e-3a81-8d85-8ac3bb03556b | -5.90947 | -45.54521 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2079889e-2937-3dff-a6ca-d9749c5a6466 | -7.54238 | -45.3529 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eddc9c1-74e5-3821-898f-a10b61555bab | -4.14325 | -46.45098 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de86bf8b-7d96-3f5b-bc53-be616a657be9 | -8.46749 | -43.63264 | 2025-08-31 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51d1d151-9424-346a-a1ae-f2c161c63857 | -6.53644 | -44.44804 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f16f76d-3158-3edd-84ec-d63b3cfc29f8 | -5.79025 | -42.55811 | 2025-08-31 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70a642aa-b635-39ef-84a9-46ce0289a30b | -6.58698 | -39.64784 | 2025-08-31 04:02:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9eb52488-1c6b-3b47-8750-ee320fba4572 | -11.07929 | -44.61481 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd9c644c-b456-399a-9b68-7cfd37d182de | -9.59486 | -40.35802 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 6dcbf030-a8ad-34ac-93dc-49751b5d581e | -7.44682 | -44.8162 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 064850f8-be5f-3b1e-a486-0f3b1a9a54d6 | -6.28952 | -43.54187 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83a42e00-7bac-3ccb-9659-daf36af06267 | -9.25497 | -47.06557 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8c52177d-6498-3c7e-91d3-88737cfe68c5 | -8.29602 | -46.31685 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b037fd0-2dc8-359b-bbc3-d621bc926296 | -6.28658 | -43.53691 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77fc5e8d-4776-354e-b781-366d0c68a7f9 | -7.42268 | -42.04654 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9976b8d4-11a5-32e6-ac6a-f359e815eb72 | -6.28222 | -43.54058 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f310a4b-318c-3b76-bc66-215fa25c4fd2 | -6.91669 | -44.37595 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
