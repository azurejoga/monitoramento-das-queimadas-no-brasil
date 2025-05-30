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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20c6a67-71b1-3f3d-b18c-b25a5c3d643e | -8.51865 | -50.01665 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24343a16-0d56-31aa-96aa-f88c63d63457 | -6.30059 | -46.05556 | 2025-05-30 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3b12731-007a-30da-9426-66f648e72212 | -7.5828 | -45.95267 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af80f6a1-1645-332f-bf3c-5f648aeb2ca1 | -7.94689 | -46.20195 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67fd7cf6-d223-3304-a32e-63d5573073d7 | -9.3983 | -40.36836 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c4c7394-9274-384d-9402-c443079ed8a2 | -11.69491 | -46.21554 | 2025-05-30 03:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fafb4ec-337f-3c4a-81de-215b83d783d0 | -9.79463 | -47.75122 | 2025-05-30 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6deb7fb-2e07-3e55-964f-d4295f446119 | -9.60405 | -49.02323 | 2025-05-30 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f30878ce-f99b-334f-8567-d94ab569802e | -8.00299 | -45.68266 | 2025-05-30 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28de120c-cf2a-3083-9c45-643464f85706 | -9.85047 | -48.15364 | 2025-05-30 03:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62bdf485-2101-39f2-93fd-8df563653cf5 | -7.1942 | -43.11323 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6c7feab8-cae2-32e8-9414-c6af29a41993 | -7.96097 | -46.1769 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70fa0651-9b51-3043-aac7-cf9836f0bc6d | -7.00699 | -44.61811 | 2025-05-30 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cd1a3bc-f26d-3999-9de0-2d046edfd79e | -7.18807 | -43.10196 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00181354-ec71-33e9-a2e8-4b58a4b69ee2 | -9.3916 | -48.42234 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af47f522-a8c9-312b-bd4f-7d4a07a8d558 | -9.2579 | -48.874 | 2025-05-30 03:53:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 334b7163-858e-3d2c-a991-5cfd9b46c025 | -7.19029 | -43.11253 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e6cf0d2-082e-345d-b8ec-5fe8d69766be | -11.57213 | -47.45332 | 2025-05-30 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af4a3ac9-e09f-3bac-ae64-683220b93baf | -7.95733 | -46.17323 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5779dae0-cb63-3df5-a497-1898e1b81096 | -9.84639 | -48.14631 | 2025-05-30 03:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aaeb8a7-3045-33c9-bcdc-6a353bc09aeb | -6.83009 | -44.65305 | 2025-05-30 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6297e07a-dd8e-3ef2-a6ba-36d2c067d17c | -12.29634 | -42.01622 | 2025-05-30 03:53:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5fbaeaa3-26cf-3856-9a8a-94539981bea7 | -11.89431 | -47.44291 | 2025-05-30 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21660dd9-f51c-3996-b8df-4269846b2d6a | -7.53348 | -43.32167 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210c3eb6-29c0-3c3b-8f0d-92e1f5850097 | -8.79243 | -47.94176 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d873c627-3831-33e9-822e-c7b733d2aebd | -7.22551 | -43.26379 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10566cfc-81b8-3691-8fc3-2535c50f2c41 | -11.45024 | -49.09985 | 2025-05-30 03:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62113541-e998-3484-ba77-b4dba0ae2ce2 | -9.39447 | -48.4201 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e43037fa-ee8b-39d7-b151-7a7884f46e07 | -9.71807 | -48.31744 | 2025-05-30 03:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9d1dc5-a3d2-35b0-b056-59e977c5c9aa | -8.51779 | -50.02126 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc6959e6-216e-30ec-887d-714b06af3ec3 | -6.83078 | -44.64903 | 2025-05-30 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e0d2c3-66c0-3935-8b48-52449f1ca7ea | -7.70327 | -49.3902 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a2cb63b-2732-3750-a9c8-d299305ba99f | -6.75399 | -44.93372 | 2025-05-30 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85c7e786-71ae-3d39-aac3-81369f0da12e | -11.6913 | -46.21007 | 2025-05-30 03:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ec39bdb-3b5b-311f-8500-098dfa54c8f8 | -7.10458 | -44.3707 | 2025-05-30 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89e58459-2239-3580-b1d0-4aff3762bf02 | -9.39882 | -48.41317 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81e0db81-a320-3798-8376-43602c28912d | -7.58662 | -45.95849 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7786bd2e-d76f-3a61-8511-7bdaa7f8a962 | -7.61104 | -45.73892 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e990c115-c9fd-32fe-9d30-fb528d169f48 | -8.54767 | -46.42408 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9d3f6e0-599f-3c73-bba9-44b1ef7438af | -12.25688 | -44.60171 | 2025-05-30 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c8258d8-328a-3e6e-864a-c9041afa9211 | -11.89914 | -47.4438 | 2025-05-30 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0d7988a-8fa8-3ab3-a2ec-2989fbea7b6f | -7.18776 | -43.10511 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4798284a-f698-31d0-b965-49389c828657 | -7.24146 | -43.09558 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 47ca9dfe-7f85-3b9d-a0be-d31cfac5631b | -9.20136 | -49.4669 | 2025-05-30 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63cd9846-66e4-3c56-bbed-f016bd0b659a | -12.26355 | -44.5997 | 2025-05-30 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ca020be-676b-3a15-88f4-ea635338060a | -8.00213 | -45.68761 | 2025-05-30 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecf2d97b-422d-367b-b74e-6c535576e00f | -7.99835 | -45.68219 | 2025-05-30 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcfbcba7-0eb8-3e80-a3aa-3f0b9fd1097b | -12.25957 | -44.59896 | 2025-05-30 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0e4d4e3-9cdc-39dc-9e41-525cbc90a1c5 | -7.63261 | -46.11383 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97ab698e-7442-3952-b705-3856e019e4f4 | -11.69573 | -46.21103 | 2025-05-30 03:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 860cd7b4-d6cb-3a42-bd7d-44792b2d3d48 | -9.40284 | -40.36167 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 8b349613-5346-3696-b8d0-2c343770bd3a | -7.66865 | -49.37978 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 849e9fed-823b-3f72-9d1e-cf6622cf0ffd | -8.54746 | -46.42431 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c778428-c2d3-3f87-a7cf-d31b6cc3d372 | -9.25305 | -48.86918 | 2025-05-30 03:53:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e2a56a-cb47-3e7d-bc2d-f6c7a6a466ab | -9.39511 | -48.41673 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26b52ace-1e41-3e7d-9377-8555e49e6417 | -7.70242 | -49.3949 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 735fea9d-bd18-32b2-b03c-394c2cfa0a8a | -7.23171 | -43.27539 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65988136-bd95-319c-8ea0-86144a3d0950 | -7.95618 | -46.17635 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 377ffa73-d0d9-33f5-b8d3-5464e162eb5b | -11.69048 | -46.21458 | 2025-05-30 03:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 985c2044-4ac1-310b-ad50-3ceb609c26cd | -9.39284 | -48.41553 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab6a866c-3d73-30fc-b59b-4c90e5bfa30d | -7.57912 | -45.86455 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c1aeceb-6dfb-3fa3-8663-3bfe0c01734e | -7.24537 | -43.09624 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ee284912-cb3c-353e-8ce4-55988fd9965e | -7.2724 | -44.22649 | 2025-05-30 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f2403e5-0102-3cd7-a945-b93749264f53 | -7.61569 | -45.73959 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 552925c0-c6a7-35ac-8340-cbe83cf67c5e | -11.20376 | -47.82493 | 2025-05-30 03:53:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e061b82-8fc8-333d-b9b5-4c728b10151b | -9.60959 | -49.0244 | 2025-05-30 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eeb824e-7b18-36ee-a6b9-ff881f214b87 | -11.56044 | -47.46213 | 2025-05-30 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c618893b-d40b-352b-a064-cc2d2282c2b0 | -11.38924 | -39.06601 | 2025-05-30 03:53:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8550909-4686-3e1a-98b7-7b5b1117887b | -10.45503 | -47.94937 | 2025-05-30 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 704b9a48-3e86-3aa4-b163-e31030a693a1 | -7.23447 | -43.0893 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 891eed61-6bed-3e9b-a127-01fbfde974a8 | -6.82601 | -44.91394 | 2025-05-30 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f9affb8-6a58-39da-b812-86b045bb4adf | -9.19557 | -49.46591 | 2025-05-30 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56372140-46e2-35c5-981f-37bec8f9d1fc | -9.39345 | -48.41215 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959883bb-afd1-381e-8c64-7111096bf3a6 | -11.79106 | -44.2872 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f00e3068-5fb7-3137-84c4-770485ab6e3f | -7.6186 | -45.75014 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7898e49-fdc0-3ce8-b7da-551c4ec0588d | -9.39638 | -48.41002 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1011e25-6b00-36c7-ab2d-25d93de25eab | -8.19734 | -49.80983 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3c36563-aa65-3232-a607-408d5b266efa | -9.40562 | -40.36584 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1ab83663-bceb-367a-a224-49f82472f99e | -7.97234 | -45.94207 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7a1c666-2a12-3890-b0fd-5b0934588d42 | -9.39223 | -48.41891 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 200af6e6-a69a-317c-8917-2de7949d9279 | -11.20322 | -47.82787 | 2025-05-30 03:53:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32a23b55-9eb3-34d4-ac27-2489c50efe96 | -9.40503 | -40.36946 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f6e3108-c7b1-3541-98d9-34b96267983b | -7.63737 | -46.11463 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b93a049e-6dbe-3cf2-9f32-3af83cfb77a3 | -7.61948 | -45.74519 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 061e6b35-b1da-3887-b846-70b19965e0f9 | -7.24063 | -43.10055 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fb38e3e3-d66e-3b2d-860c-50123f4eb792 | -9.83259 | -40.56496 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e97c3c7a-461b-36f1-91ad-2665f1615145 | -9.84282 | -44.68503 | 2025-05-30 03:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3a9e4c7-715a-37e2-8aa7-e2bd0ee985f2 | -11.79195 | -44.28211 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 497e1e67-d593-3e43-804e-832aabf9d50d | -8.51175 | -50.02012 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cd07915-3854-3ef6-82ff-3be50a8ae9e1 | -7.63281 | -46.11635 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 905ccd9c-8439-3cdf-9ef4-5603fb296cae | -10.45742 | -47.9488 | 2025-05-30 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5477ac52-3672-37c7-b688-7622677d3ea1 | -12.25863 | -44.60424 | 2025-05-30 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ad2f801-1383-38c2-97f3-01c1ad8503c6 | -6.69363 | -44.16039 | 2025-05-30 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8504cc5d-008f-3a9c-8a91-380d78c43ee8 | -11.81122 | -44.26457 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be46a24a-5485-3df5-bfc1-eb684d885d4f | -7.95648 | -46.17797 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5046c614-0c20-3ef8-af65-51e0cb27cb14 | -8.51262 | -50.01546 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8b69083-4825-3d7c-bf62-ff4788098a91 | -7.58369 | -45.94765 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85535a64-f345-305b-8a07-cf7ae039f036 | -7.32575 | -43.71254 | 2025-05-30 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39254646-f9b1-31da-94c7-453483f19351 | -12.01776 | -49.51896 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 657ba5e7-588b-386e-b885-c4973054d294 | -14.84433 | -48.10139 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README6.md)
