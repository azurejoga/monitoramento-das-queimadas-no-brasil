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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3a272ff-b123-3b08-96a3-df270ed7faa5 | -9.08504 | -47.94676 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fe35c6d9-c9ee-37ed-b353-3a7646f9c25b | -11.47561 | -47.62891 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29193db6-c350-3325-9c12-a540656ee71d | -12.17319 | -45.06065 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b3a18c-6e95-3d21-8f0b-ddeeebdcdb8d | -10.61077 | -47.40751 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da8fd547-8898-3181-a9de-f30ab1325ba2 | -10.89133 | -47.91189 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87be9f7a-ada3-37b5-9453-3201d5f7d1cd | -11.4737 | -44.15093 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26880c9-7667-3e6a-a913-bf11807f74b3 | -11.43031 | -44.1403 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cca6668e-79fc-3091-acf5-d83b994d8c1c | -11.73083 | -62.29752 | 2025-10-16 04:40:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6f27407-6ebe-33c3-8b04-0356566f6818 | -8.3925 | -46.25027 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7b59be0-ee97-331d-b1b2-89c2e2f4787c | -12.24385 | -49.38511 | 2025-10-16 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 702b9aed-473c-31a1-9958-7ad395afc6df | -8.46037 | -44.18043 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 477d12c3-0137-3090-a99d-7c309884e7eb | -11.47738 | -47.64168 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdac28e7-8cfd-3a2d-a86b-5765e29ef3f8 | -12.22584 | -43.30552 | 2025-10-16 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd288451-42d8-34e4-afbc-9390c58829b8 | -11.58974 | -44.08717 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0618e405-d36d-3fc3-968c-d459977529ec | -13.73533 | -44.23279 | 2025-10-16 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70e256a5-c7f4-3281-b5ef-51ad67af798a | -9.37495 | -46.9534 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e081513-7c5f-3a39-93d9-0134c12ea1d1 | -15.0291 | -47.31702 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91f026b6-6eda-33a8-92f0-8c7f8e6e39e5 | -10.13237 | -44.57396 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27e741b8-7abc-3752-979d-f31a8635bd03 | -12.22521 | -43.31063 | 2025-10-16 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 197acc4f-91c5-3a5f-8f45-8f50be095058 | -10.70013 | -44.43457 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 54d1b8f1-298e-3f31-b1fd-9156ea296a50 | -11.42883 | -44.11784 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de28377c-7f8d-3887-ac89-16714e07e093 | -11.44936 | -44.16515 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| bacca6a9-704b-3041-b30c-b409ee02885e | -11.83179 | -45.28232 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b006281-39b9-3f10-94e9-5b9879fea301 | -8.46572 | -46.18859 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 140b552a-29d4-3be3-9102-f1780108cfa2 | -13.19714 | -49.97375 | 2025-10-16 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 297a1ca3-75fb-3961-97be-f8b9e3db66e8 | -10.81173 | -47.93308 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba14378-8385-30b2-b71d-cb92d0b55657 | -10.12506 | -44.56522 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85582d65-1793-3014-b6ea-630cc43280a4 | -9.68827 | -44.53705 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82fe7843-88c9-3e97-870c-dc676eacb503 | -10.63792 | -44.41925 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2faa354e-c5b9-353c-9bba-d7a1857bb428 | -8.20142 | -47.01263 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c775edfe-6e13-3f0c-93a9-a6b7f0f565ba | -14.03475 | -50.56488 | 2025-10-16 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60ed133f-0472-3568-9485-1bd34f694c50 | -13.02276 | -49.17658 | 2025-10-16 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41ea3246-0d1b-35b5-bf29-fc481cc574ed | -9.25559 | -44.35953 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2cbd234-90e9-3f39-9cd5-8fc121aa2f38 | -15.73709 | -44.624 | 2025-10-16 04:40:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fced26a6-6709-3479-81a7-2a9e094ba579 | -8.47633 | -46.24429 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd75fe54-b7ae-3cf4-a4d5-1000104adaeb | -9.15911 | -46.86969 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 78a976b4-16cc-35a4-8033-ca16e8a9e798 | -8.70418 | -44.79012 | 2025-10-16 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c6d6cfd-3aaf-3337-b7eb-c6bffeca1950 | -11.46514 | -44.18069 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c66d2d7-01ac-35c2-90f6-c5e20a3860e4 | -10.88095 | -48.80215 | 2025-10-16 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4f041628-fbdc-3732-a1c7-acd84a500c7e | -10.13467 | -44.56578 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af5ad919-d4ed-3026-a0c4-3d7db70d0867 | -10.83489 | -43.99405 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c881cccf-cf46-3a8a-9609-8d64db01a3f8 | -15.88889 | -43.46397 | 2025-10-16 04:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| baabd6f9-c5be-3d93-8f63-8b8408641f26 | -12.73033 | -50.6436 | 2025-10-16 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e162361-1ab6-3fe2-8fc3-5afdabc76cad | -10.98453 | -43.72215 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c49434f9-1de9-30ea-8ebd-bc28660543cf | -10.83311 | -44.00701 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9a067fd2-6d2d-3a3a-8c79-033a186f9073 | -9.0647 | -46.89905 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c5a099f-001b-3464-b22e-9a861750bd4c | -11.75276 | -61.07144 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db2887a9-f80c-303a-b94d-340b61f6264a | -10.91366 | -47.58759 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cafb381-be7f-32ef-8207-7c0d3b6e7eee | -10.82432 | -43.93976 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e37002fa-17f1-3e3c-8849-a4931fcec8d7 | -10.95627 | -59.12148 | 2025-10-16 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c70493c4-9d51-3870-b2da-f441dcef1ef8 | -12.42233 | -48.69273 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2621243f-d1da-371f-b141-d05e6f9713c4 | -11.46076 | -44.18005 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 999e37b2-12c2-3f2b-958c-c19e7c3ff12c | -10.30457 | -43.99498 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6431de52-268d-3047-9276-78bb52419ef6 | -10.50864 | -43.36868 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06aa9ce6-e982-3b41-94e4-cf93254a2c3e | -10.83548 | -43.98975 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9589b6-e2fa-3c1b-8658-bc8e89c72d6d | -12.22401 | -43.30457 | 2025-10-16 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bab5645e-8a18-3246-930d-8023d2854324 | -9.15551 | -46.86916 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 16dd88d4-cd86-329e-b98b-fb12e264a632 | -14.43483 | -52.76936 | 2025-10-16 04:40:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d0d17fb-2117-3423-b484-c8540fa17c2c | -8.19435 | -47.01151 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 02c8daf2-b4a2-3295-852e-bb8337a78d60 | -9.22848 | -48.60242 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bd6a58b4-6150-35e8-b1d7-2c756a01a664 | -10.63848 | -44.41513 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04768a04-db5b-38db-82fb-7c07b199d3d2 | -10.05723 | -43.83514 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6b9e4ed2-fce7-3d03-b30f-c227dc5fe5e1 | -11.33424 | -45.27465 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8c2e156-af2d-3935-b528-96374fdb5d32 | -10.26844 | -51.04113 | 2025-10-16 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 909d6f3c-9b46-309c-92db-4f8a8ed5d7d5 | -10.16716 | -47.10606 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f893637-6cb5-3858-8b8c-c570d6829d31 | -11.59888 | -48.55102 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0172e11-dc02-3432-b92e-b1e5eb105388 | -10.81287 | -47.97308 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b5516ed-705a-31f5-a31c-42bbb383973a | -13.45263 | -47.95387 | 2025-10-16 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c608bda-6c62-3a44-ae56-d3bd0b10bbf5 | -11.47489 | -44.14222 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6075c465-260e-3599-a570-3c5219d922d8 | -10.61591 | -42.31735 | 2025-10-16 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ef795b1-f91b-3599-b93d-3ec1332c1647 | -12.7248 | -48.63605 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45ae1f3d-0601-351f-9391-75c80260d15f | -10.57595 | -50.90401 | 2025-10-16 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21a9510c-7239-3b42-a51c-421145218a82 | -8.55412 | -44.58485 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5552cf74-d49c-3cb5-96e6-240a0e2305b3 | -10.12451 | -44.56908 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a78f6e5-6670-3f3a-b6f9-c41c319f00d1 | -12.06349 | -51.20445 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 373e21d0-e13c-338e-874d-c5cabc245fe9 | -10.54239 | -47.97284 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48406e5c-a610-3b2c-a0c4-fba1eb41e063 | -10.99581 | -49.5429 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e09367-adc3-353f-89ba-d3999c8f948c | -14.0353 | -50.56132 | 2025-10-16 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e39f735-a999-3ef0-8806-3014a735268b | -12.67711 | -43.43683 | 2025-10-16 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6d0f44ce-1871-30c7-a4d2-b4353063f391 | -10.22256 | -43.90844 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d43675d2-7128-3345-9e0f-5f9eeb7c99bc | -9.1582 | -41.05675 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9cfca6ef-60d2-32fb-af8e-cf5042b8ad5b | -13.89012 | -48.45588 | 2025-10-16 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bd17b62-8460-3476-9b45-ac7786b04de1 | -10.64424 | -45.24357 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27191099-95c0-3237-80b4-0a74ca8116b3 | -11.57585 | -44.06069 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f44e4ef-5167-363f-930b-87e5a8525c61 | -9.95129 | -48.59344 | 2025-10-16 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00a01560-7180-3a0f-b60f-d6560c62db85 | -11.54651 | -49.91976 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b963729-648d-3eaf-b367-fb9af3bc8cb6 | -11.75845 | -61.07254 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 142275f6-855a-308a-b337-1e5ea6c85615 | -9.26816 | -44.36152 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d887583f-f95e-3097-86ac-76c916f5c193 | -11.06231 | -44.66095 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 204719d9-9f75-3d0f-a414-e0625ef798ee | -8.29127 | -44.96885 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85eb2e3b-9b13-3009-a6d9-c8beefeffb4b | -8.3919 | -46.25438 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8a46cf0e-3a40-36b4-a0e3-e110b4d832b9 | -11.79654 | -44.22135 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09645fd9-1249-3fbb-b413-51990c187a99 | -8.40605 | -46.26066 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5afae62-022f-339f-a11b-f9c2aa87f46a | -8.27076 | -45.91038 | 2025-10-16 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38edde5e-6be4-388c-b1a5-d616a31c2a87 | -8.29873 | -44.9734 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35bc71cb-e961-39a5-98dc-387a67379ada | -12.23658 | -49.3877 | 2025-10-16 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e4cd853-8da4-3484-ac93-626489a18563 | -10.66634 | -45.29104 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d4622e-0d97-3868-80b5-f75cdd43150c | -8.46459 | -44.18092 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4c060505-3b13-33c8-8485-684e4a04a7c5 | -10.05283 | -43.83454 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 905ab29c-5a94-39a2-9f23-d3b6423869d6 | -8.47264 | -46.24373 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README62.md)
