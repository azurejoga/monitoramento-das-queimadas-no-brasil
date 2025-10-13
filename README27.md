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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd262388-e45e-3bf0-9ab6-6f77b306ed8d | -3.06711 | -49.40813 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ce88aa15-eccc-310b-bbd5-ccfbd1d62e01 | -2.70443 | -54.65292 | 2025-10-13 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e355f55-5d7e-32a5-8ab2-daa47e9308c5 | -7.48746 | -44.60733 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea8f236-ff0b-3c2b-b2df-d3f91223cef5 | -10.81408 | -43.98874 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 85537d87-4164-3ce6-9a0b-255e549470a7 | -4.66587 | -45.70137 | 2025-10-13 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb5c4ecb-b8c4-358f-acca-8677bd628584 | -7.69466 | -42.37425 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b95b7ce-5278-3428-b055-6910f07e21d3 | -7.75042 | -44.20135 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 350de135-1b99-3b39-97ed-136f5e451b76 | -8.23349 | -43.35627 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0699d16-d7d4-3f5b-8975-e8e1613c551c | -7.35372 | -44.09551 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 526e11a0-a87c-3acf-ba6d-895b41c628de | -3.26262 | -50.1306 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaed67ae-eefa-32c7-af09-94a3e17cef14 | -5.74341 | -40.76792 | 2025-10-13 04:44:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 361e80e8-158c-3a08-b2e2-c593dddd5f48 | -4.22686 | -50.62869 | 2025-10-13 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8423fd96-8079-32d1-be79-65f3da753914 | -7.51459 | -42.16438 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee86e931-a20a-37a4-be31-a76f866dfa5a | -7.45969 | -43.88387 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1182bbec-62bf-3cd7-8ab7-8adfeb0fcd82 | -7.21701 | -39.90355 | 2025-10-13 04:44:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ac4ba92-d1bb-33a9-8c4f-5fd7bb5378a3 | -5.56962 | -45.27836 | 2025-10-13 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ceee26f-c64d-321c-82e6-2579e917c1ac | -7.54349 | -46.09602 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 097c485b-7dbf-3918-b7b3-fdbc47ccdd02 | -6.42555 | -42.55155 | 2025-10-13 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d21ebb9-5d55-3597-8386-f925ce81e754 | -10.79803 | -43.95987 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48659d6d-523f-3956-a3f8-1d9ec038c8da | -2.88436 | -50.73896 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64929c38-9316-3ca1-909f-c579d7f2d096 | -5.18259 | -49.88784 | 2025-10-13 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e13a6b-f6fc-377a-8067-3d275a97f327 | -8.45331 | -46.12669 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b8f8f0c0-99d2-3885-813a-f3722df16f13 | -8.32889 | -46.24259 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c48ffec4-a143-3584-ac78-780a8352b75c | -4.01454 | -47.35138 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 36b6f947-314c-3cbd-beb5-310e070eb60d | -5.57017 | -45.27464 | 2025-10-13 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b948f103-a825-3d12-8df6-c7236575cd59 | -4.84659 | -43.20426 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31ee00a7-1ada-32b2-9d03-1bd715121d99 | -4.66548 | -46.28708 | 2025-10-13 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a832bb24-294d-318e-8fb2-af63802ef579 | -3.06988 | -49.41211 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d250a22-ba4f-353c-9733-a16437f2dfcb | -4.47442 | -44.93729 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 22b5a148-7001-363c-8f87-d244ca9f743e | -3.09456 | -50.3756 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ffafe81-8c57-331b-a5fc-f53be22d7a7d | -8.21693 | -43.33155 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a299f28-a0af-379c-8fe5-0d68d159d657 | -6.6483 | -41.38448 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ab5d0d26-9c88-322f-879d-6f13a551dc0c | -5.10525 | -46.13771 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b31b98e-414a-3816-bcde-44c7652c0e5d | -7.15641 | -42.1975 | 2025-10-13 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8ad733f-5adf-3cd8-9876-ddf5a746878b | -7.64634 | -42.57541 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64f7c8c1-9428-38e5-b1d3-76aff77ab22b | -7.69984 | -42.37511 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ca86eb1-9f76-3426-9b31-47616264069a | -5.92915 | -40.88704 | 2025-10-13 04:44:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de4ad14f-6802-3138-bd00-92cc8127449b | -3.25824 | -50.13695 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a22d3df-157c-36f9-8f84-e17c8e19c9d1 | -7.48897 | -42.76249 | 2025-10-13 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21ad99e6-3a3f-3248-908b-e339437471ee | -5.10946 | -43.2065 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02cbb048-3186-3dc6-9240-1a1a5cbbffa8 | -7.55465 | -43.83871 | 2025-10-13 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 242e89e5-ecfc-337f-b45f-76fb468cd9df | -3.27998 | -52.96003 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 524a87ca-6c0b-3a4b-b083-5e24af666911 | -3.38504 | -50.2804 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ffed563-eba8-3996-91cf-e87a5c265824 | -7.68813 | -42.57532 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7120a65b-25a9-3278-9ba1-d57a7951ece2 | -5.88291 | -41.38769 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0236c078-cab2-3958-94d9-7d6e6aa58fdd | -7.54401 | -46.09248 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 796e863d-ed1e-39a6-b523-4e0c5abf46fc | -4.48272 | -44.93854 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74ac2391-bc14-3f2e-8bae-84c2d5e05b66 | -10.80642 | -43.97159 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 134e7961-7e49-3fbf-82c1-daa5e6f6fa0b | -3.66289 | -50.9506 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d7b204-565b-3fa8-8c60-c758c0a871f4 | -7.15727 | -42.19727 | 2025-10-13 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5522cf5-3b0b-39ad-aa61-0f280098fa23 | -7.33385 | -43.86506 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac3eb964-b6c4-340c-adb9-841d8cacb9a8 | -4.28953 | -48.57829 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a21508bb-2b9b-30ab-a565-6e6a775f7412 | -7.35627 | -45.19848 | 2025-10-13 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 370043d0-43e1-3599-9359-0b7cec030027 | -3.83827 | -50.0134 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2262c188-6383-3ce4-89a7-a9d66491d0be | -10.80504 | -43.98209 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 85b19be8-521b-3200-8d05-be4fe82aa248 | -10.80291 | -43.96047 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a363f1ed-110e-3ee7-b821-58b09c34390e | -7.67778 | -42.38159 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c43cbda0-a425-30bb-815d-2a5de8646429 | -7.80316 | -42.44233 | 2025-10-13 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 801de8e6-90af-3fbd-8e3a-d6815d81e054 | -7.51063 | -42.15406 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7d0cf90-86d2-3808-a1a7-b48958e7ac87 | -7.13988 | -42.51658 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1917f7af-ffb5-3265-bdd2-78a57f673963 | -7.91769 | -47.21282 | 2025-10-13 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a9e2234-5507-3931-891b-23006d4f5fe2 | -3.76995 | -52.3595 | 2025-10-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 859ed37e-4fd0-3b4a-9a8a-fe04d0a48099 | -10.78972 | -43.94747 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b9f12b67-2598-3f35-a807-892f8f0e5a31 | -2.60604 | -51.91604 | 2025-10-13 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1097804c-a1cd-3751-9835-59a71d1cab7d | -3.29067 | -53.00693 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5d146eb-af38-305c-a93d-8c5c5b8fbad0 | -3.06813 | -49.37986 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349cfcc0-412a-3fa9-be4f-8e9d079245cf | -3.73545 | -50.25476 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bba4323-8b85-37f8-acf2-108a5a3eddb9 | -3.41089 | -51.22997 | 2025-10-13 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fe72cbd-2f88-33a1-ac4b-1abff78dca3a | -5.91743 | -45.43067 | 2025-10-13 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b42a499e-2e10-3b22-b7af-87f17e9fb40f | -3.25101 | -50.0307 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c628ea63-5d43-344e-aecd-e2aff7319ba3 | -7.54454 | -46.08895 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 75fc9ce2-2ed7-35ef-b2d5-0fc00d86caed | -7.2164 | -39.90808 | 2025-10-13 04:44:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca2e8717-d647-38db-b332-dac3cbfc58ea | -5.5743 | -45.27523 | 2025-10-13 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e243e995-c9d7-3a33-8f05-33e80aca7b05 | -8.54139 | -44.58922 | 2025-10-13 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dc77f23b-fe06-3814-8c5e-6aad748eeda0 | -8.21985 | -43.38274 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0992b742-6984-37b7-a319-57478424c8f2 | -4.47499 | -44.93354 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cc92df69-e22d-3cef-9a05-aa1f930de557 | -10.78689 | -43.96923 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c394b0d0-85ef-3857-9af7-c768c898af16 | -6.21722 | -41.56839 | 2025-10-13 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ddb9e2e6-5a2c-3a30-bde5-abb8a8774cb9 | -7.83528 | -44.52753 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efaa321b-a6db-396a-be6e-7602a7e5e3e6 | -3.84158 | -50.01391 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c12b37-4ebc-3456-9eae-5c9398404801 | -6.72897 | -42.07709 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2874171f-b6b7-3265-adfb-68a6987ecedc | -3.57109 | -53.0191 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b022425-adaf-3c34-b0dd-22611caae1a8 | -4.01253 | -47.34767 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31eabcc5-fc76-3096-8e90-b8dbc65cb17e | -10.79177 | -43.96982 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a91e623-699b-3c9b-920b-26bc932ef320 | -7.68948 | -42.37339 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d592e8e-698f-309e-acbf-6879f0946f4d | -4.22631 | -50.63213 | 2025-10-13 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4a785c-b948-3241-8547-8196a668cd33 | -2.98949 | -50.2886 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e58d59f9-df2c-3e20-8041-d22deadc74d2 | -6.4796 | -42.06144 | 2025-10-13 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 13cccf11-7f80-31f6-8687-062c5a066101 | -10.81965 | -43.98403 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23388999-57fb-36ab-866c-f237fd65e4f0 | -7.32291 | -44.75334 | 2025-10-13 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baf50956-6c54-359e-a22a-9932c87ff7c8 | -4.30363 | -48.10363 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d92803e-9bc8-3249-b34b-fd0459af886f | -4.61826 | -45.77613 | 2025-10-13 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5893c3cf-7675-3092-95d7-8af9230d9042 | -4.88626 | -37.49817 | 2025-10-13 04:44:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1db3401d-ce9c-3d05-8f14-22cab0cfab1c | -6.29293 | -46.7267 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07cc638a-1aea-33e2-9129-869c3959dfcd | -7.49443 | -42.15493 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdfe4199-400d-3c7c-8c1b-7e5606310635 | -4.28272 | -48.57724 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| feca0eba-843a-382c-9569-9f366252e70c | -6.67228 | -46.02813 | 2025-10-13 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d084e5f4-d46b-3976-9537-bf9654fbb80f | -5.53639 | -46.48894 | 2025-10-13 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75d61129-bffe-3a35-9b4c-863e4cf5f85e | -10.03769 | -43.81059 | 2025-10-13 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7a83a337-f59b-387c-a364-1d22d14d63b6 | -3.81405 | -50.74689 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
