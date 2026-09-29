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
| e2d13ca5-1271-36a2-a223-da4b6aacc125 | -7.38734 | -42.6476 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d09d5ae0-2891-35e8-b6df-f102054944a8 | -4.08782 | -45.91594 | 2026-09-29 15:48:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 835676c0-8b29-34d6-8fa7-77a2aea6d79f | -6.91007 | -43.6924 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 217d8f80-9847-33a5-a205-45f1282bad08 | -4.30599 | -41.76569 | 2026-09-29 15:48:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 56e9c34e-9246-3392-9277-f1e22a4da25a | -8.36409 | -44.18282 | 2026-09-29 15:48:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6e3b7974-7ec9-384f-9d63-25af79db9157 | -4.60672 | -40.38188 | 2026-09-29 15:48:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 48feb2b7-2b28-3270-8d5d-2f2952937fbc | -4.72389 | -44.34829 | 2026-09-29 15:48:00 | NPP-375 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eaa33c06-2a8c-37ee-882c-62211c998dd5 | -4.53928 | -40.69243 | 2026-09-29 15:48:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2e4baff7-4742-36b0-af6c-8f47d4aa07fd | -7.2713 | -45.33054 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 52eddc06-933e-31b8-9bc2-e2fe6ade18bb | -3.28921 | -42.66795 | 2026-09-29 15:48:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f8613535-3e77-3b47-89a7-28e12cc826f1 | -7.52958 | -44.55242 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 484d4ea4-c8a2-37f2-b2a0-c35fe2dd98cc | -7.05673 | -42.07433 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| eca0e961-44bf-3ed6-8715-d6c9561234a6 | -7.2672 | -43.38844 | 2026-09-29 15:48:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 195287f6-d8be-309d-a4b0-f7d1f4049451 | -7.06777 | -41.75135 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a76829d8-e1c0-312c-93eb-f571e8cdca5f | -8.32185 | -44.18195 | 2026-09-29 15:48:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 44230759-1a7a-30a3-831a-208a9a285d9c | -5.54964 | -44.98056 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 28900a0d-4218-3a6a-a6a5-f8debd0a47df | -6.9228 | -35.35469 | 2026-09-29 15:48:00 | NPP-375 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1ee2575a-898c-39af-bf06-9f892a20f059 | -8.02242 | -42.85616 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 12fde880-efe0-3cab-b3b0-c419d6b421d2 | -8.5572 | -44.04702 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4937369d-c41d-376a-b2fc-d5775772f1a3 | -7.07418 | -41.75469 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 9f171c7b-ea3a-3ad9-ac00-5994a265e2c5 | -6.95434 | -42.85819 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e630543f-5e4a-374b-a4ec-68863904b5b6 | -6.83846 | -38.26704 | 2026-09-29 15:48:00 | NPP-375 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3f6491dd-0276-3473-8eb7-bf1cb1cf5889 | -8.02428 | -42.87075 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 88797787-c6d1-3d70-87b2-51cb4e8025ef | -7.99854 | -44.50523 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2ab17b79-4dfd-3c4e-b901-b59f0a2e247b | -8.01789 | -42.8714 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 7d937278-f499-31e6-8faf-8350d3836f86 | -7.15136 | -45.3334 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 45df0842-9bf5-3d81-8cc4-bf84b929ee9d | -7.45866 | -40.2146 | 2026-09-29 15:48:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a400de1f-cea2-37f6-be12-34e31e28b073 | -7.69773 | -44.9306 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3700f511-2666-33ea-b4ed-660aeab12e90 | -6.02815 | -42.58309 | 2026-09-29 15:48:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 82f7be18-8f33-3c3e-aded-3b249d8b3a75 | -8.00029 | -44.50587 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c48c0ef0-5bff-333e-bf25-ba003dd9671f | -6.91078 | -43.698 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5f6ba625-78fb-3d2e-bbfa-807ca1be62e2 | -4.09504 | -45.91471 | 2026-09-29 15:48:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 68d09718-8b35-3898-9374-2598f16d3b21 | -7.38607 | -42.638 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| df5ee57e-8a4b-3565-9308-8411154600a2 | -7.7571 | -39.90117 | 2026-09-29 15:48:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 471a1858-351b-33bd-ba3a-97581416e4e9 | -6.90699 | -43.70087 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 68866214-af79-3e0d-b72f-1362f59f8c6b | -7.07894 | -41.74589 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6f45843c-6d73-3617-9a12-7d5524ddd5cf | -4.9308 | -45.46494 | 2026-09-29 15:48:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dc82419a-bebf-3afe-be8e-6f8a4bee40e9 | -6.02616 | -42.57498 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6974b1d7-ec99-3ab3-a13f-020ce4966560 | -6.02755 | -42.57853 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 634ef56f-cb85-309f-b1e0-10bbe50f15a5 | -6.95259 | -41.60073 | 2026-09-29 15:48:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f0ecf70f-7cfa-3ff5-9b95-9a2b1a59af14 | -7.39357 | -42.64681 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 07b28923-4298-3763-9100-8bbe69be9aab | -7.51567 | -44.55487 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a001a64b-58bf-3083-afdb-f1a3a2b5bb67 | -6.06096 | -35.35922 | 2026-09-29 15:48:00 | NPP-375 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 1632b381-600d-3160-9763-ca16cad72f0d | -6.01944 | -42.57114 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 76c66b43-eb73-3cf0-ac0f-35344e334712 | -6.76214 | -37.77808 | 2026-09-29 15:48:00 | NPP-375 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| cc20456d-edac-333a-b02b-79c250ff736d | -5.18552 | -37.07003 | 2026-09-29 15:48:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a7210cf3-c73c-3c61-b403-ef88fc6b7602 | -7.15169 | -45.33227 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 31bd6e1f-c220-30d0-b095-df7d1d434fb8 | -2.89626 | -42.36021 | 2026-09-29 15:48:00 | NPP-375 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94a15a6b-a67e-3ae7-b512-2dfa20b2fc3a | -7.69936 | -44.92579 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d30f5001-9a2c-34a5-ba43-151ab2e73002 | -7.2786 | -45.32965 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cdf5df2d-7eab-3219-8824-c1b8e822a78e | -8.73935 | -44.89531 | 2026-09-29 15:48:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fbf1a85b-6990-3a34-afed-b65a24a95f01 | -5.70329 | -45.24073 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b2df72d8-d22f-3541-ab3b-8d8678dea966 | -4.03432 | -42.05709 | 2026-09-29 15:48:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 67afe26b-6b37-37f8-974f-f1bc947c0b1a | -8.55718 | -44.05127 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 014d5080-4f94-360b-9bb9-28bb5b469de2 | -7.2701 | -45.33173 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 646cbb7f-80c3-3378-91f7-d5c353c193bf | -6.94453 | -42.86273 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| df4a04ad-fcba-3836-a365-3c041530bdc1 | -7.3942 | -42.65156 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 38d129b6-3c00-3211-886d-1141462914b8 | -6.47411 | -38.35661 | 2026-09-29 15:48:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 0f95eda6-3b0d-3676-8824-024c39cd054a | -7.34182 | -42.07501 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| aafd9761-1bdd-3327-93b0-1df01e8458c4 | -7.38671 | -42.64281 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 749f86be-3b2f-3624-84e4-bc5484d91c26 | -7.28594 | -45.32909 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f65b5541-7d2b-368d-b960-c098310baff0 | -6.02069 | -42.5802 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| fc6e5e9f-9f03-3527-9a2c-b8cb2e02bb1a | -6.0146 | -42.58097 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 588e6e6a-fa5c-3ff2-a66e-6487b7dae06e | -8.02493 | -42.87581 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4e9b15c8-634e-3ec5-bc15-a9754971c6c1 | -3.77763 | -41.60696 | 2026-09-29 15:48:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 5177771d-9357-3581-a266-2733805fc08a | -6.89531 | -43.71407 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ffe1d49d-eb7f-368d-9992-32e84e666302 | -6.94385 | -42.85776 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 8fee85cf-a430-3632-a380-549e0ecd1fd0 | -6.24955 | -41.59098 | 2026-09-29 15:48:00 | NPP-375 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5334d387-783e-3f02-8fde-b4f1da3e040f | -6.28709 | -39.41275 | 2026-09-29 15:48:00 | NPP-375 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e00c67c8-2d5a-39c9-8f06-af2a4b391eb9 | -8.45081 | -44.66235 | 2026-09-29 15:48:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4b0d0602-e942-3c29-a93d-eb286e9077b2 | -6.36778 | -35.1671 | 2026-09-29 15:48:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 39a80b7a-f149-3314-afdb-63d6465727d7 | -8.32109 | -44.17587 | 2026-09-29 15:48:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d9c8df81-fb92-3f72-b06f-6e88b5b6e6e1 | -7.33732 | -42.07429 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a818041e-93dd-3e97-8f5d-9184afb72dc3 | -7.0672 | -42.86829 | 2026-09-29 15:48:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a9d75988-7b3c-3d49-b597-33833e196b17 | -7.02942 | -44.62623 | 2026-09-29 15:48:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 29b3e398-3bd1-3c45-999a-fe461718ad47 | -7.3811 | -42.64829 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cdf7c3f9-0d47-3f40-a025-8e1ab86a0d10 | -7.02747 | -45.30395 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d310fc6c-ed12-334f-92cc-4825abd9ae0e | -7.55435 | -40.46652 | 2026-09-29 15:48:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6e13fbf2-d655-3d61-8985-e03d2d6e0127 | -7.51488 | -44.54861 | 2026-09-29 15:48:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44039087-e1d7-39fe-8a92-07487d308693 | -8.728 | -44.9226 | 2026-09-29 15:48:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| efa8a436-ebc6-3aa4-b81c-fdab09432495 | -7.05787 | -42.08297 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 05fccf27-5e10-3534-be82-07070bb3d291 | -5.13935 | -40.40657 | 2026-09-29 15:48:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bb79739f-a441-33bd-92d8-45d8780e8e3b | -7.07308 | -41.7466 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d26449b6-259e-342a-8a79-801ba8b24b47 | -7.38047 | -42.64349 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0f503d2d-e01a-3414-865c-5633c12ff493 | -8.03067 | -42.87017 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ac9755bc-4af7-3422-b5f1-528763f55cc6 | -7.0568 | -42.31021 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3f4706cd-68d9-3593-b392-49bd7404bcbf | -8.74112 | -44.90002 | 2026-09-29 15:48:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d2163065-0f84-3d8a-8193-38f9cccf32e2 | -7.42342 | -42.63328 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 136129e6-8030-3e48-8a62-b1532031e07f | -4.09423 | -45.91604 | 2026-09-29 15:48:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 38adf345-c4d2-3e2c-ab6d-59be7b738743 | -8.32263 | -44.18814 | 2026-09-29 15:48:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ab8f340d-aefc-385b-a466-4725ff572c96 | -8.01855 | -42.87653 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 01943db2-494b-3959-ba13-7a695e83ce64 | -4.71832 | -43.20072 | 2026-09-29 15:48:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 163952d1-eeb1-3a98-816b-c65d2517ad0f | -6.88799 | -43.70948 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3f6634e9-e7d3-36d7-808d-beee780f3aca | -2.92318 | -42.86743 | 2026-09-29 15:48:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4d33ba21-a26b-3fa5-83ac-ce75b4e655db | -3.40082 | -44.11698 | 2026-09-29 15:48:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ccde374-803b-3e44-9325-46dfc93a564f | -5.74133 | -45.20076 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d32feaa2-d096-3cac-8b6a-1195e07a1cd1 | -3.28502 | -42.67017 | 2026-09-29 15:48:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7ae1b036-6c6a-3e16-8407-908a3d938c72 | -8.55646 | -44.04086 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a4d679af-4365-3a25-8490-ac486c3e759a | -5.55112 | -44.98218 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 3701b150-9f83-3c50-91d2-d2216927fd71 | -7.02796 | -44.63117 | 2026-09-29 15:48:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README95.md)
