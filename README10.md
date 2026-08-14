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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ca3e420-eaf5-371f-a94c-f38b94ec0ceb | -19.95562 | -45.54895 | 2026-08-14 03:40:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81db139d-8d0a-3d79-b2b1-4e5dccb73a7e | -21.40482 | -41.1562 | 2026-08-14 03:40:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0a6be225-bee9-34b2-ae64-98812c7a75d7 | -20.31503 | -42.23121 | 2026-08-14 03:40:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4e833195-94f7-36da-8a4a-309fbc027dae | -14.93779 | -46.62412 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| f3446a45-b96e-3518-ab91-db04311f73b4 | -20.26176 | -46.71144 | 2026-08-14 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 040e69e1-4cb6-3d87-b64b-7286982ed7d9 | -21.40735 | -41.15409 | 2026-08-14 03:40:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 805f9bb8-e9ec-3a69-8567-d22994f7ea3b | -18.41774 | -45.19559 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c2746ca-08d7-3863-8427-95a51908d0cd | -18.54983 | -48.18208 | 2026-08-14 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54290d4b-56ab-38c0-bb27-e7d761270919 | -18.4232 | -45.19431 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac7de39b-3c48-352e-8ba7-c835d5d479a0 | -21.49792 | -48.63573 | 2026-08-14 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1bdfc34-b146-3ab9-a88b-a6083a8b9124 | -18.28985 | -46.08305 | 2026-08-14 03:40:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2931aa36-be82-3590-a861-6fe7a0aac19e | -14.93673 | -46.62926 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 28fefb92-680e-3541-924a-f1c61f713a7c | -18.48875 | -43.40071 | 2026-08-14 03:40:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc9343b9-020e-3f7b-8784-a632b9684b16 | -21.38295 | -48.63412 | 2026-08-14 03:40:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5f8312-aaba-36a3-ab60-b265e7f8104f | -20.32625 | -42.01474 | 2026-08-14 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8eda36c-82f5-32ed-a377-aa566d7e3f82 | -19.95067 | -45.54783 | 2026-08-14 03:40:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 381660e2-1426-3e15-9a62-671175bc2448 | -21.40652 | -41.15881 | 2026-08-14 03:40:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5514b029-56b2-3eb8-a489-629bf6c3bdc9 | -20.96109 | -47.20273 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a031ef3-11ef-3d99-bd29-72bbc5f08ec7 | -18.41716 | -45.19847 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f959d720-45f8-3d09-84f7-6d6d6c4f41e1 | -16.72041 | -46.40564 | 2026-08-14 03:40:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57f756cf-7daf-3fa3-b248-beee1b18f75c | -14.93868 | -46.61985 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8c714ae-a975-3549-8f5f-7d89e0eaf650 | -21.74814 | -44.03069 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 944bb1d9-c533-32a7-9eee-b259e7812eeb | -21.73739 | -42.40835 | 2026-08-14 03:40:00 | NOAA-21 | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7140d3c7-28ad-30e3-b944-7833c546fc91 | -14.95872 | -46.61105 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef49262a-96f3-3298-87b2-0e0d16242aef | -19.87113 | -43.24225 | 2026-08-14 03:40:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5cdeee5e-2fe9-3934-a1a5-f0d56d9f3cb2 | -18.55106 | -48.18538 | 2026-08-14 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ae7681c-65d4-3775-945e-9356c60c02bb | -18.54881 | -48.1867 | 2026-08-14 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f91c6378-2dac-3e78-b702-638bdd23e8e0 | -20.97059 | -47.41663 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afeba2bb-0928-3191-b32b-e484bbeb16fa | -20.36335 | -41.50082 | 2026-08-14 03:40:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7985903d-b0f4-33f4-be53-992418ab911f | -20.32123 | -42.01966 | 2026-08-14 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09e4af10-4220-39e6-be22-5fc6daabc447 | -16.34455 | -42.88013 | 2026-08-14 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf92ba89-c4f6-3bab-8a88-a4a453822ece | -21.78111 | -44.04747 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6a88f98d-9739-33fd-9bdd-abe3191a5112 | -14.95414 | -46.60381 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db59b243-11eb-381e-b623-2c25d1c40a46 | -21.76213 | -44.02887 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2472a4da-3f70-32d9-a90b-8e6e176215c9 | -14.95785 | -46.61526 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d25c4d1-cb17-3950-92de-086752523e0b | -14.73222 | -47.14968 | 2026-08-14 03:40:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31fda498-f63a-3f08-94e0-a7d6537e40d9 | -18.4264 | -45.20428 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b782a193-3959-3d54-add0-eed39155ad94 | -18.53873 | -48.20399 | 2026-08-14 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1755aa4-37fb-3115-b0f4-3aea2088abd7 | -14.7262 | -47.14838 | 2026-08-14 03:40:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 761189a5-8b0f-3dc0-9ca4-6fe592425c45 | -14.72521 | -47.15309 | 2026-08-14 03:40:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2941144-f7dd-3b2c-a32c-1b9404e27837 | -18.4134 | -45.19129 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c3af05d-6a74-33a1-99b6-13918183ffa0 | -19.96057 | -45.55006 | 2026-08-14 03:40:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3021966a-db63-340b-a744-4512e89bc249 | -20.32523 | -42.02023 | 2026-08-14 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48494bc7-f25b-388f-917f-fa154afc31ae | -22.91868 | -49.20967 | 2026-08-14 03:42:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc0b7ec7-1fe9-31c7-83a4-1228404d03bb | -23.31017 | -47.5431 | 2026-08-14 03:42:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42495ac4-e89d-3d4d-adb1-f9c7f3a3e583 | -23.21185 | -45.95041 | 2026-08-14 03:42:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 77de4491-2de9-3775-a0c8-194f72df6554 | -23.31098 | -47.53951 | 2026-08-14 03:42:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc205b0a-cfaa-3e60-83b5-9491b9f78ce4 | -23.29662 | -46.6877 | 2026-08-14 03:42:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a290642-36e0-306c-9f98-e2c1c282047b | -23.21099 | -45.95198 | 2026-08-14 03:42:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af14f2b3-e7b8-3bff-8fef-13b176c1e951 | -22.92028 | -49.20919 | 2026-08-14 03:42:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e3dd60a-46fc-308e-bfd3-6f5973f17ce7 | -4.5057 | -42.5325 | 2026-08-14 03:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 3fceb937-d72e-3087-8d7b-7fe4c9187383 | -6.6195 | -59.0416 | 2026-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1661149f-01f5-31f2-a44f-f803b5d3954f | -13.2221 | -54.2704 | 2026-08-14 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 51fadf2c-5544-30ba-b145-b79da6b2cb7e | -13.2413 | -54.2683 | 2026-08-14 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| d49dbe6d-5ed5-33f0-a6fd-f72321a6e404 | -11.4885 | -54.6273 | 2026-08-14 03:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5774a3af-f4e3-34fa-a06e-0a7f893469de | -13.2801 | -54.2228 | 2026-08-14 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 10de7a09-bd22-359d-95bc-d636fd24de96 | -4.5057 | -42.5325 | 2026-08-14 04:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 3ed09d58-ecdd-30a7-b26b-d9589975d5af | -6.6195 | -59.0416 | 2026-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| bc3101b6-ebe6-38fc-b3b9-b867adc17df8 | -14.2945 | -51.9635 | 2026-08-14 04:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5f3ad5a9-d399-33db-9ac0-ed2e43e844d3 | -11.4885 | -54.6273 | 2026-08-14 04:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c34cfe6a-1a54-3d8a-8281-8e35b1f35157 | -13.2413 | -54.2683 | 2026-08-14 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a3a636fa-93d0-34d1-b489-036ac5e5da16 | -11.4885 | -54.6273 | 2026-08-14 04:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ee38c83e-542c-38b0-a44f-3c9001c154dd | -6.6195 | -59.0416 | 2026-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 489ef7f4-73c2-36e2-82d4-5ec74f007755 | -6.85782 | -42.90253 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9ca6f12-fdc9-3d77-846c-4a39162d4a61 | -6.92215 | -43.64 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a975ff13-32f2-3b9a-89b2-9c5c826bc4e0 | -6.90809 | -43.63943 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3306e03c-b65e-37f2-9cb4-02d55c306051 | -6.9799 | -41.4679 | 2026-08-14 04:12:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82a17600-af71-3b88-afbf-0bb5676864a9 | -6.77856 | -42.65908 | 2026-08-14 04:12:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a6457221-ea4d-38ea-a213-7ad99ae3bca2 | -2.79691 | -49.58152 | 2026-08-14 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97968ebd-af5a-34ba-8394-279a84f7ed31 | -3.84829 | -49.04161 | 2026-08-14 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7353ef5-f318-31e9-80fb-fc187c3c9348 | -4.49295 | -42.54483 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 57ec0614-d2f6-37b0-8fd9-dede42e5431b | -4.25297 | -48.54359 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc35448b-d04c-393a-9abc-d36e9ad70b33 | -5.73344 | -44.50476 | 2026-08-14 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 007077e4-95cf-3fe8-9e86-3c7b8d247bda | -6.10962 | -44.03074 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb9eb667-f5e4-3d51-b0a3-2b9162ae96f0 | -6.88671 | -41.95617 | 2026-08-14 04:12:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0855a7f-fe44-3d5f-961a-907c07d82b22 | -6.91847 | -43.6394 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3aa876e9-a623-324d-9ea9-2ab0c64b5896 | -6.11038 | -44.02625 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88238797-926c-34d2-ba1e-bb3dec03a0b6 | -3.84846 | -49.04075 | 2026-08-14 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9411e573-c2ba-396b-8670-e5d2ab0f4134 | -6.4149 | -39.25799 | 2026-08-14 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| efd52891-9b9c-3f87-a295-0dc6d96c8e5e | -6.11341 | -44.03139 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0f0af70-7b11-3211-ab7a-c3cef63ee247 | -6.91544 | -43.64063 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4379e94-04a6-3a18-8b06-31011fa16776 | -6.26888 | -43.27877 | 2026-08-14 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4982f523-ab09-3e69-a7ca-c39b779dcf25 | -4.49515 | -42.54145 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 23f380a3-1cf1-3179-b34e-3ba6d4c5ac38 | -6.9197 | -45.73067 | 2026-08-14 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8249149f-f058-391d-90ea-373528300473 | -6.91247 | -43.63567 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c7d42fd-afad-3424-b009-1a0f97d1e6eb | -4.41069 | -42.14499 | 2026-08-14 04:12:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94380c5c-5181-37d4-bd69-441473194fc4 | -6.80915 | -44.88167 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1b9d6b3-496e-3645-a803-964681dc3688 | -5.5588 | -44.11149 | 2026-08-14 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e461740-aab7-37ad-b34f-756d12df7d9d | -4.25241 | -48.54692 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ec6788-f242-3257-8a34-b085f3f596e1 | -6.20717 | -47.13309 | 2026-08-14 04:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d78261b-4c02-3239-9a31-5ca496c9b20d | -2.6442 | -47.98739 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec6d8ec6-8869-31d0-8026-ae35e3e237b1 | -4.21697 | -46.43663 | 2026-08-14 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2de1d30-a7a0-340e-835b-e5c0176a9b35 | -5.80307 | -43.63966 | 2026-08-14 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74f47c97-e8de-3415-b0f9-8e8c497c94fa | -7.99402 | -38.32937 | 2026-08-14 04:12:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db51d191-106a-3fbf-98a8-9fd53280f202 | -7.02823 | -41.44649 | 2026-08-14 04:12:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 493036ee-9974-3c30-8af7-2d234f78df51 | -5.30361 | -43.06422 | 2026-08-14 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8d1bd90-ba0a-30df-ba5f-0ba6939dc224 | -4.5001 | -42.54597 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 260d279f-2120-34c6-8f3b-037a3695f9ab | -6.88052 | -41.95112 | 2026-08-14 04:12:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 513ac4fc-6427-3d1e-b5a2-ac56e98c62d4 | -4.50434 | -42.54248 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 590352f0-96e7-3239-be3a-ef59fa325d3f | -6.8574 | -42.92722 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
