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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a587c276-a076-3f62-849c-860f05c855b9 | -18.45759 | -53.5183 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 207abfae-4198-376b-9bc8-05ce90f7dd78 | -18.45755 | -53.49488 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5fa3131-5da5-3034-9926-21bcbe33a63f | -18.45699 | -53.49867 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46bc32aa-0d6f-3f81-8722-5008f939ddcd | -18.45644 | -53.50243 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 062a75c3-00c4-307c-8b4d-780911844af5 | -18.45588 | -53.50622 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a008040b-d6b5-3bc3-9453-fadf0878b582 | -18.45532 | -53.51004 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52dc8b65-bf0f-3a6e-a508-2864fae6893d | -18.45475 | -53.51387 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27cbc31d-61c9-3b37-84c0-481bbd401ef8 | -18.45358 | -53.4981 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 059cbf83-818a-3037-8e7f-055034843c4b | -18.45303 | -53.50186 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ca9a5a1d-af19-35ca-a8de-245e50a5a76b | -18.45191 | -53.50948 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a4bdd3e-7f8a-3f52-a512-4d249abb4f00 | -18.45017 | -53.49756 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf78181f-1d29-396a-ae7b-4260ac3dafd3 | -18.44906 | -53.50508 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 974d3afa-26df-323d-adfa-ede049e5b69c | -18.44565 | -53.50454 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 840d83e4-c532-3b4f-952b-4bbde38d34ed | -18.20732 | -53.50673 | 2024-10-07 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8b8721a-5b53-30a6-ad2f-0f8dcfa5fa26 | -18.20391 | -53.50616 | 2024-10-07 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13d910e0-20ac-379f-a2bd-6590b185dc14 | -18.20051 | -53.5056 | 2024-10-07 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3dd980f-ab8c-3a09-b68d-d4cd4dda7439 | -18.19995 | -53.50946 | 2024-10-07 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc5b2021-b58c-3d67-81d1-c96558fb36ed | -18.19711 | -53.50505 | 2024-10-07 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad4fc9a0-1fa8-3ec4-ad13-37eb3f397aa3 | -18.78445 | -53.77021 | 2024-10-07 04:55:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdbf525f-5b2a-3bf9-9d7e-a3b0008a099b | -20.47886 | -53.67569 | 2024-10-07 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c86f430d-d8a3-3607-86bd-7d3565f817be | -22.90058 | -53.68976 | 2024-10-07 04:55:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38423abb-4cc9-3af2-9930-a4772ce167a6 | -16.49479 | -53.95069 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5051f34-ebff-377a-a7d0-3f4fc0ee2151 | -16.49424 | -53.95435 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bea756a-f3c8-3771-bd3c-d59c3e24a895 | -16.49368 | -53.95801 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c627fb90-6419-3ca7-947a-7e8f4eeca173 | -16.4898 | -53.96114 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1e8fa590-4ded-3e92-8aa3-ccea1c576679 | -16.48925 | -53.96478 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5034a94-32a2-39e7-b26a-0d76a9964ad4 | -16.48757 | -53.95328 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28cca0e4-0edf-3df4-9ac1-2e595767c87a | -16.48702 | -53.95694 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36a50cbf-8320-351e-9343-51c43e71f162 | -16.48647 | -53.96061 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70d236ce-801d-3d76-8432-28723644ff8c | -16.48591 | -53.96425 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6df5e60e-ec4e-3ddf-8569-572300275254 | -16.48368 | -53.95641 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a410305-1b7c-3762-b7e3-3f2ba0681ec9 | -16.48313 | -53.96007 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ac5d85c-a26c-31e7-b3ba-50f1a057cedb | -16.48258 | -53.96372 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80de314e-b2a9-3d46-a8cc-03e07aed66b8 | -16.4802 | -53.96005 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1029265c-5f55-3aa8-b6f0-84da4b9e4ee9 | -16.47967 | -53.94125 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71cb5f5c-829d-34cb-bf2d-f3da581f70e4 | -16.4791 | -53.94491 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e39ba2de-dbce-3b72-84b6-7b22e0e93dbc | -16.47188 | -53.96981 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 391628a5-8658-3388-a81b-3fb0fa0230dc | -16.4691 | -53.96564 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97827f56-0813-3a48-8f19-605ef109d6aa | -16.46855 | -53.96927 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 694e9816-252e-30b1-aa83-ce56f05184c2 | -16.46632 | -53.96151 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3529de2-3962-30ff-92dd-bb9f7f3e209f | -16.46576 | -53.96514 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e4b9f55-d78e-3c30-9605-549e89406e25 | -16.46521 | -53.96875 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b212de2-05dd-319c-a2f9-712cb143e7b0 | -16.46466 | -53.97237 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f97c59-04d8-327f-8d1e-e4821d34e621 | -16.4641 | -53.93135 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf32a9a-9a55-3706-b347-584399c5800f | -16.46298 | -53.96099 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 253ee02e-6591-3913-b7f5-2c2f36effbe5 | -16.46188 | -53.96821 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4610d448-7d13-3cce-b3ea-ffd7e019e973 | -16.46133 | -53.97183 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd90841f-32eb-33e0-914a-f6e480444307 | -16.46132 | -53.92714 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4fffd55e-26a8-3132-abc4-1d9d9856eb9a | -16.46076 | -53.9308 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c84758c7-6a70-3e8a-a1a8-2cc9a33e9f21 | -16.4591 | -53.96404 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fc85525-da85-3a6f-9510-59a423118b80 | -16.45855 | -53.96765 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e97def54-3e90-3661-852c-436ce83d7f47 | -16.45799 | -53.92659 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bcc4e2e-49b4-3adb-a312-2336391913f2 | -16.45743 | -53.93024 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c831aa9-a5d7-3013-a8eb-fa544f21ecac | -16.45578 | -53.96346 | 2024-10-07 04:55:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7fa9e6e-e728-3ed1-a15e-e4a62c82f3cc | -17.32986 | -55.04017 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a6111728-8010-3324-97bf-2c51e0970355 | -17.32712 | -55.03601 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6203bc59-e9a1-3670-8593-451a73fa7abd | -17.32656 | -55.03961 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8d351017-5362-3497-9132-d46d8796fe2b | -17.326 | -55.04321 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ea75bfea-c046-3456-9e6b-e145071c9fd3 | -17.32381 | -55.03545 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 19337940-81b7-3c77-af33-2a3d72ff7fd6 | -17.32325 | -55.03905 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 887f27d9-03f4-30a5-b1fa-b40974c10809 | -17.32269 | -55.04264 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 520ba7ab-b0d9-3d04-98a5-af14fc62c2a9 | -17.32051 | -55.03489 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 487da8c4-117f-35f6-b1b1-b83c72c7b79a | -17.21802 | -55.12469 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01f3d6a6-56d1-3847-935d-9898e1b0302b | -17.18086 | -53.93005 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb403803-6861-3ac3-8f18-e894c8018785 | -17.17863 | -53.92213 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad137738-ecc8-352f-81d6-b804013c1f4a | -17.17752 | -53.92949 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7044e89-8010-3503-b622-6d5a3e6f73cf | -17.17473 | -53.92525 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32f18753-fffd-395b-b155-9ca47997b192 | -17.16805 | -53.92412 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c67d816-3b5e-307b-89d0-a8c2a7d9f1da | -17.16249 | -53.93827 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a703d89-a1c2-3dd9-921b-87f325d953c5 | -17.15302 | -53.93293 | 2024-10-07 04:55:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e56e03e0-19fe-3f1f-8a73-9536ada8a6d5 | -17.02971 | -55.0669 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4cfaee50-75d1-3990-acc0-47c02c29be97 | -17.02915 | -55.07049 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7eda00fe-65c5-3e66-a60e-b9a0f5ad4f9b | -17.02802 | -55.07767 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6fd888b-b420-3eae-ba41-cbbe7f5feda4 | -17.02641 | -55.06634 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 655eafa9-fcec-3318-83ef-266a42163728 | -17.02584 | -55.06993 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cfe8527e-5252-37aa-8732-05c4d04c15d6 | -17.02528 | -55.07352 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4128db6d-f551-3e99-876e-cabc7a14d906 | -17.02472 | -55.07711 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6bf750dd-3f89-3686-90f7-09d03cf0a3bd | -17.02367 | -55.06219 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff2d69e6-a418-3a14-9ae8-468d09bef4f2 | -17.0231 | -55.06578 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6b308d5-4dad-3b64-b44a-c14fed87b2d2 | -17.02254 | -55.06937 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 002831d4-1734-377d-9784-60cc03d4969b | -17.02197 | -55.07296 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4ba53be-6d8b-384b-9f46-00b332efbb86 | -17.02141 | -55.07655 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fca5855-de1c-3ad0-bcd9-8f5ee4142208 | -17.02093 | -55.05804 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63c48ce1-8dce-30dc-a70c-dd4acf5b9cdc | -17.02085 | -55.08014 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d72fe30-3829-357a-8bcb-65f50feb1ef5 | -17.02036 | -55.06163 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1604b49-5d5b-3c82-812e-23f6848f2227 | -17.01769 | -55.03538 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 864153a6-71aa-32fc-8899-351049ce928a | -17.01762 | -55.05748 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07649ea4-f360-3c1c-8059-75f09f505c93 | -17.01698 | -55.08317 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00d4538f-67e0-384b-8d0e-900860f3b6da | -17.01642 | -55.08675 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c729e0b0-f3d7-3103-971f-bb3257e97cfa | -17.01585 | -55.09034 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d7df6c4-2aba-364f-9b7f-af22ecc4a11b | -17.01529 | -55.09393 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d9e1b7cb-0976-37e7-817b-157b5118a753 | -17.01488 | -55.05333 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8aa18c8-8cf9-3be1-b1f7-7c8c70e882c9 | -17.01439 | -55.03483 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6b434d9-abab-3a7f-8df0-bb9d24446771 | -17.01432 | -55.05693 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 072f9ce5-4bda-3a3c-b2e3-96596a0a4c90 | -17.01255 | -55.08978 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3dabe0a-4c23-3870-87d4-424b3b322d9f | -17.01214 | -55.04918 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbf8ed1c-d8d7-37cb-95b7-b072bd33fcb2 | -17.01199 | -55.09337 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a005e21-5c5e-3f83-80b3-215e642023d4 | -17.01165 | -55.03068 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49674612-b212-323a-b621-32964ebb7676 | -17.01158 | -55.05278 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eccffcfb-32c1-3790-bd26-f08dd122fbbc | -17.00891 | -55.02653 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README94.md)
