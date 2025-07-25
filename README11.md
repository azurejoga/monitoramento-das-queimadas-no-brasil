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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7593aff-6f5b-386d-a679-f780a5ae82a9 | -14.21226 | -43.95257 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a61427b-193a-323e-9ed9-0da55005aec2 | -12.70256 | -46.98112 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b3c277e1-79e2-3647-842b-142782737786 | -19.19265 | -44.15606 | 2025-07-25 03:57:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df296951-c886-3774-a4f8-9176b1dc2a3e | -18.2271 | -54.54773 | 2025-07-25 03:57:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff55d453-07de-3bd1-bb18-1b65f7e68bc6 | -19.41434 | -44.96358 | 2025-07-25 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e496647e-3720-3246-92f9-6f3f1baad51e | -14.95546 | -46.98346 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e893096-e687-36d9-a398-1d3aecb3520e | -16.82044 | -47.5967 | 2025-07-25 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 938c4f7d-00f2-3c51-b6f7-9a6ae3fdfe58 | -12.69794 | -46.98069 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cfa971a-26bc-3d62-9099-0dd1a87d608e | -16.51135 | -50.85102 | 2025-07-25 03:57:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5342f64a-00ef-3eff-92c8-21cc72d2f262 | -16.61623 | -43.35785 | 2025-07-25 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3dcf9ba-349e-3cd7-b8cc-2dbad8bd0191 | -14.94297 | -46.97769 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2699f294-f701-3c0a-b577-544f89f7fbb1 | -13.7154 | -45.67587 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 923d01cc-8c34-3233-b7ff-04ac109aea6f | -18.22524 | -54.54822 | 2025-07-25 03:57:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 771a9a1b-4624-3786-b172-66f3da818cd9 | -13.71685 | -45.69168 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df24904e-f7c6-39d1-9f2f-b34d64aaa10d | -13.70787 | -45.67057 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a0abc3-384e-3fa1-ae07-9bf9acf2dbe7 | -18.42021 | -54.56159 | 2025-07-25 03:57:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43f9b69b-ecc4-3e5c-b79b-53e361b3ddae | -13.70931 | -45.6864 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bd10ac3-0c23-3905-b84d-a0f15f59a200 | -13.7072 | -45.67433 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3517dcee-dffd-3438-bc16-7f001b19485a | -19.67844 | -43.88431 | 2025-07-25 03:57:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70e2907-5c9a-3ea7-ad06-aad21ba5e964 | -15.59936 | -46.51912 | 2025-07-25 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 287208d5-787c-3b0c-b2bc-513e7bb3138b | -16.51062 | -50.85459 | 2025-07-25 03:57:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 95f085e3-386d-3ba9-9126-bd3c68d8c4b5 | -13.70654 | -45.6781 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e271743-1809-3269-b4d3-71fb154ae21c | -14.21885 | -43.95835 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e0a940e-ef03-3d50-856f-4d2b50a76439 | -12.71104 | -47.79588 | 2025-07-25 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fe3c2b7-cb44-3fac-ae59-24cfcc23dcfd | -13.71883 | -45.6804 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd14102d-e30f-3137-a26f-ab197113fe80 | -20.39232 | -42.39725 | 2025-07-25 03:57:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 692a95a6-5af1-30c4-b111-61ec1a7c9371 | -19.41167 | -44.9615 | 2025-07-25 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9c8338c-bbff-3aca-8a5f-374169e1ec9b | -19.42862 | -44.81632 | 2025-07-25 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75bf7230-cccc-37a2-9b8f-63aa02c30d3b | -7.9256 | -44.0937 | 2025-07-25 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 991fde15-1f9c-3c0b-9d75-0a8517178b14 | -7.2597 | -43.0645 | 2025-07-25 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 3da7caff-3a9a-39fd-be12-10314df6cefd | -11.4584 | -45.1126 | 2025-07-25 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| def7044e-11b1-3a74-b940-8bcb84f864f8 | -23.20733 | -49.41024 | 2025-07-25 04:00:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db99923a-f561-307d-9a29-f8aec81f5756 | -22.28913 | -52.01023 | 2025-07-25 04:00:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fbbc5e87-8710-372d-af5d-4f2fd8d335b8 | -21.47236 | -44.96312 | 2025-07-25 04:00:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a84c5287-a9bb-35bf-ae3c-5407745b668c | -20.22607 | -50.91375 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5284d2ef-df20-365b-88b2-8c5baf2cf343 | -20.68193 | -46.30558 | 2025-07-25 04:00:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 429db4ba-0d5d-348f-9ba6-681734cbd3d5 | -20.47785 | -50.90811 | 2025-07-25 04:00:00 | NOAA-21 | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 871b9f38-d51c-3803-9b02-c992421f17db | -20.68572 | -46.30646 | 2025-07-25 04:00:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 095fa801-432e-393a-a4f3-8552150a8cd2 | -20.68099 | -46.31082 | 2025-07-25 04:00:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbb75f61-5a22-3da4-88c0-58e1e81e4ac4 | -23.70804 | -47.47907 | 2025-07-25 04:00:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cb50537-4390-3cfb-a068-e12ff62f2b66 | -21.35889 | -46.7203 | 2025-07-25 04:00:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fccbe2b7-ddd6-35ba-a386-d0f6c4f31329 | -20.2279 | -50.91827 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 98bbc6ea-2ae5-3f2d-8897-05891e58d50a | -21.5499 | -47.96441 | 2025-07-25 04:00:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 611efdc5-8ba7-3071-aaa5-9b52c1f950cf | -20.90565 | -45.26371 | 2025-07-25 04:00:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fc2e046c-c96a-317d-b190-076c9924f684 | -20.22856 | -50.91507 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9fb63faf-06fc-3df2-8877-145ee07afdec | -20.22284 | -50.91695 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 13933c5f-83ca-389f-a25b-5733b703b9c2 | -20.22351 | -50.91373 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7fb6bb75-96d1-37ae-8a26-3c4fa0bd6ab0 | -20.60536 | -46.31432 | 2025-07-25 04:00:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f6ebe91-b47e-3c9f-ace2-b929ae2549fb | -20.22538 | -50.91695 | 2025-07-25 04:00:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f7a31b93-83de-3ee8-85c1-6255af77f717 | -11.4584 | -45.1126 | 2025-07-25 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ac38ad3f-7396-347b-a906-e5f4416f2b8e | -7.2597 | -43.0645 | 2025-07-25 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| f61d4b2f-9a93-3dbe-ae4c-5cff3f5120a7 | -2.86128 | -46.77422 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b7c1491-96d5-37a5-8a3b-af14eb2860bf | -3.47288 | -42.85435 | 2025-07-25 04:19:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e786c493-48cc-3c0c-90e1-e3cc401914dc | -4.68811 | -40.57742 | 2025-07-25 04:19:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebbb686d-f8d4-38ea-9059-e2150c7ec4bb | -3.81513 | -43.02642 | 2025-07-25 04:19:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b1a239c-8da0-3f6e-8caa-efaa7aef6a11 | -3.82554 | -41.55559 | 2025-07-25 04:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 67ebf9ca-1dab-3bf0-9c6f-7e79a8863c8b | -3.12196 | -47.00931 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e66f0801-e7bb-38d1-81c3-21c8fceb55de | -2.90789 | -48.24812 | 2025-07-25 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 3f1ac02b-3aef-3c2b-9cc4-d98686e86865 | -3.17902 | -49.45735 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e8228a7-e369-3268-a8f7-ad22f335bf25 | -3.04592 | -47.38403 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55c6651b-8415-3b91-88c1-12c5d4fdcee6 | -3.1761 | -49.44896 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbce3f37-0110-3b8b-b913-0bef2737ef42 | -3.18028 | -49.44965 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19fa2b63-651a-35a0-b148-7c1c471eba4d | -3.04664 | -47.37963 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c99e175-eab4-388f-893a-45b0f488e171 | -3.45752 | -42.99644 | 2025-07-25 04:19:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb4de314-d330-346a-80c5-4d40b4df458e | -3.32491 | -48.71455 | 2025-07-25 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 664d5bae-8f57-3be3-8515-456572e088aa | -3.12129 | -47.01343 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e72ee9a-d25d-3f72-8c1a-dd5f0aecc925 | -3.20141 | -49.16601 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d4d1141-b4c7-37ce-828a-5673d5b8ed8e | -3.17484 | -49.45663 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13953db6-4fc2-326d-9eb3-f3560dc8d00b | -3.04224 | -47.38341 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c2eda96-784f-3326-a9cd-15c09590554d | -2.39152 | -47.62755 | 2025-07-25 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 507be648-56a4-3b2f-8b1e-ecfcf0467a09 | -2.90856 | -48.2449 | 2025-07-25 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8722ad7d-37e0-3667-bd99-a87d898af1f0 | -3.04434 | -47.38144 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebb2d49b-0ff2-3fa1-878e-59faa390e5b8 | -3.82493 | -41.55949 | 2025-07-25 04:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2c109d50-f3f7-3cf5-9e78-a19e70a3343b | -2.9937 | -49.32292 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7138d88-2910-3a00-be58-d4640181e1b5 | -3.04296 | -47.37902 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1e4c88a-2c54-31b6-8097-ad7443506d78 | -3.35528 | -42.86884 | 2025-07-25 04:19:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d807e9fb-bb39-395b-9806-4e389f21c9f5 | -3.17066 | -49.45593 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d29f2ed4-a023-3444-9d16-8e6995b44eb8 | -3.04364 | -47.38584 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 781e9e63-c833-3196-83ca-2e48d9fb5ee4 | -3.17966 | -49.45348 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b4bb8f-4f5a-33cc-bba2-a7d509b6e848 | -3.20081 | -49.16967 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc0ce5aa-af06-32ad-aa43-737d46f5edb1 | -3.05033 | -47.38023 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd8529a1-55fc-33f2-80f6-7ef1f6f364c5 | -2.91245 | -48.24552 | 2025-07-25 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 943bcfdc-2f30-3599-a958-a97690e633d7 | -3.17129 | -49.45209 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44d7f5ae-690c-3d6b-aa73-2978963d57ed | -3.17421 | -49.46049 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4029d1dd-2da8-35f2-846e-20c0abd6baa6 | -3.58324 | -47.52419 | 2025-07-25 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea49c688-b594-36e1-8854-72c0cd7d6486 | -3.82663 | -41.57168 | 2025-07-25 04:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef3ddc59-7801-313e-8e6b-261e82a4eb3c | -3.18384 | -49.4542 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2756051-cf4d-3456-97e5-ede6908dc5ea | -4.45114 | -38.44593 | 2025-07-25 04:19:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7486923-6077-36f1-bb79-a6d949c474ec | -3.04241 | -40.81647 | 2025-07-25 04:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e0ede47-b408-353c-a6f1-f3773a2c9709 | -3.05472 | -47.37647 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d28ff02-e5f9-335c-868a-5eb13c56c97b | -3.39613 | -46.90363 | 2025-07-25 04:19:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b9bdf1-e7fe-3ed9-866f-77d8a6ca03db | -3.04961 | -47.38464 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 67dd9eec-fcf4-3ad5-b86a-24cc96a7d2a0 | -3.32807 | -48.72029 | 2025-07-25 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4923c420-9cb7-3bde-862c-76311ca4a5e5 | -3.32326 | -48.72477 | 2025-07-25 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4806be61-bf8a-3318-8191-52c8b6291d45 | -3.99614 | -44.32389 | 2025-07-25 04:19:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f7a26ba-9a35-320f-bd77-18debbf4e84b | -2.90776 | -48.24977 | 2025-07-25 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dbc399b9-2313-3810-8e4d-4aa3c6750e19 | -3.82602 | -41.57556 | 2025-07-25 04:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e11ec68-e75b-386a-9181-0297ec8d490e | -3.04065 | -47.38083 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b68d4f10-f9a1-3203-967f-38b7d9acbf01 | -3.17548 | -49.45278 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c8364ac-f88c-3912-8013-bd735bd873e0 | -3.05401 | -47.38084 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
