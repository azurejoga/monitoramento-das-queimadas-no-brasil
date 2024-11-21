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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6293689-ee88-364c-ab3d-4a9c404acc39 | -2.17813 | -52.12481 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 041aa0e6-ae8b-3157-9570-0961718e4d23 | -0.82319 | -52.83512 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fafcd984-91c3-3a64-8de4-2eb07eecd188 | -0.81544 | -51.60745 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 226693bb-58a6-35c5-9e4a-4432387d3a6b | -1.52693 | -51.51538 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 000c7385-339d-3db9-9f15-19792b0d5deb | -1.76723 | -50.85257 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b0de4d9-87e5-354f-8e25-671de149b699 | -3.59068 | -43.63014 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fac622d-0839-3825-8c4f-e645e68d8e46 | -1.1977 | -53.67164 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6845faff-56cb-3d1b-9add-e85ddcc7f04d | -2.68715 | -46.25097 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8efc819e-ce01-38b0-abcc-b788fcbdd2bd | -1.49187 | -51.13682 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 775b4a16-f03d-3029-a427-3d82a08eb131 | -0.83377 | -52.87539 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b913ef0-cc67-339e-a222-4e3569a993d7 | -0.33777 | -51.55912 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31be03e6-a507-349c-a7c9-9872260a23e1 | -0.90484 | -51.72987 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef2e5a0-76b9-360c-a130-079b17ee44df | -2.26241 | -50.45582 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c114a1f-1af6-329c-a609-1abe560256ab | -2.54437 | -48.17995 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d2fbae-9f02-3d11-bb54-12bb920838d0 | -1.19248 | -51.97582 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 327c5ddc-0ce7-3284-a939-5d6e40cb278c | -1.41996 | -52.81941 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 477d491c-674e-337b-8e0c-c0de1102f1bd | -1.72832 | -52.80424 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87c30378-0860-3891-8e33-df7dadd13bbb | -2.6925 | -46.24683 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5853f65f-dc4c-3fef-8a79-c22ba6b1b794 | -1.64714 | -52.6715 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94c9938c-059d-36b0-88f7-cd03b9d10f58 | -1.25179 | -51.75069 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b1ebed4-12d8-3e10-ae30-77872b178691 | -2.94134 | -48.33387 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8de468ec-2177-34e8-bd47-96ee051923be | -1.49712 | -52.54644 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42868b91-6857-3420-9ddc-084a5de4f1d7 | 0.4002 | -50.79822 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af344293-d1c2-3968-896d-a8c3d4200cd2 | -2.14011 | -49.54726 | 2024-11-21 04:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62c9f20d-0f67-3039-a56c-b50c5dd36fc9 | -2.61983 | -48.06631 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5fdcb84-075e-353b-823c-642e28f0c1df | -1.42966 | -46.01718 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f61ff07-4210-3a69-92bf-de8e0041a2fa | -2.40603 | -48.61336 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dad91c6c-0f91-3e8a-beb9-666c3ee4bbfc | -1.26979 | -55.39888 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83c0652d-2ec9-33a0-b322-7b2859d878be | -2.60515 | -48.24761 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04a3f303-486e-3736-90f5-718a2cc70b6e | -0.92542 | -51.64248 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a998d7f2-01c3-3d7f-94de-2fd2b0501939 | -1.1272 | -53.40604 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f3d654c2-7146-343e-8c75-db1e3a273e84 | -1.42922 | -46.01504 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ace6b8-88cf-3e16-b1dd-9227c37dd1dc | -1.12048 | -53.73058 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cac62aca-ba76-3904-9200-f1aca63f46ff | -2.61921 | -48.07347 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0395027-6717-3ce2-82a4-1af6d4126569 | -2.84733 | -49.1581 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f216e26e-2b5e-3424-92b2-14286cad5b54 | -2.20045 | -53.66998 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95217ed4-b6ba-3e85-b721-0759c73faf9a | 0.15573 | -51.24312 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad05a7ce-96b7-35d7-a73b-d88ae787fee4 | -2.20154 | -53.6631 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91b50874-d94e-3090-924b-695b2da7875c | -1.34367 | -55.47364 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 911fd5df-6e67-3f89-b0e2-c8ec04e2ecaa | -0.92023 | -52.54081 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb37eb7-43f1-3966-9d7c-b918a3200848 | -1.7313 | -52.69904 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 116a952b-8057-358a-909c-0e72ae072d69 | -2.4332 | -50.2872 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b962c94d-e852-364c-891a-f51db39f48c3 | -1.51083 | -55.54212 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e8085e-accf-3b5d-b590-2f3e991b0f47 | -2.61978 | -48.06985 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96aadb8c-3a26-388d-aa34-58672d3b0d81 | -2.20394 | -49.21227 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33ff1820-91d9-346f-bf36-4b741948d3d2 | -1.37278 | -46.50925 | 2024-11-21 04:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d504e20c-81e0-3139-80f8-27eed4f9b231 | -1.47978 | -54.44897 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8422ee39-5947-3577-a404-696e9c00bb40 | -2.84432 | -46.67611 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42963056-0c04-3d56-8a27-d3337df48a42 | -0.94054 | -51.72092 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98555be9-a5ca-3f05-af85-81a6fff6df18 | -0.80112 | -51.78608 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6972a1ba-d1e1-36b9-bfb6-2b1933b0377f | -2.94774 | -48.06937 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b7c4f8c-c107-3dec-9679-98c74f435746 | -1.51432 | -51.15152 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14a48a03-0d01-3fe8-8dc2-a9f36bf12bf3 | -1.50442 | -54.40166 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22348923-b010-3ef9-a7d3-322a22d0d24d | -1.06558 | -53.6472 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76910e15-905d-3e77-94e4-0c49a9099f59 | -0.95114 | -51.71895 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ce31bb6-c92c-303b-ae39-2e9160a6797e | -0.9015 | -51.72935 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6410e6e-4bcc-3652-9049-aa3604ae051c | -1.33942 | -52.92289 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed435e0a-ebcd-3d1b-ab00-2fbaf05eafdc | -2.71781 | -49.34531 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ebd9b8e-b222-3dbc-8695-1c4faf03344b | -2.94719 | -48.07302 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21753424-188b-3168-bf4e-ee983026533f | 0.29588 | -50.84783 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3653248-4d09-357d-aeb3-abc930933073 | -2.90202 | -48.32061 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe69e5c-d0fc-30c2-9af9-b04c30707de1 | -0.88921 | -51.72022 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 837059ed-2758-3d87-a30d-49278d5b33e9 | -1.73584 | -52.38846 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 466c87f7-3c9f-3e4b-b100-6e32ef3c5653 | -2.56985 | -49.19796 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21892e40-b59b-3e2e-8db7-70c87e221837 | -2.22509 | -50.39353 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9690554c-0188-35fd-9b62-a948ed052da7 | -2.94995 | -48.33157 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd5e9d48-a523-38c1-a3dc-d174d147e20f | -1.53384 | -52.2255 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa259715-0a25-3a5b-a90c-fa97ac68104e | -2.01945 | -50.74071 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aea470e-9ec5-314b-9a70-4e366a171449 | -1.07977 | -53.19111 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e55d6c0b-daae-3957-af95-af01fd82e5d6 | -1.82837 | -55.61744 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 597eb5fd-a281-3381-bebc-93ec45aab90d | -0.93492 | -51.64758 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e58be82c-6e76-3be6-b5bc-fa4626c0deac | -1.20984 | -53.70206 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d820018b-7572-3e53-b2dc-c53d6a6fda13 | -1.10097 | -52.34274 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 221ac39f-bcc9-3fe6-b9a8-fbdecfd03c49 | -0.77714 | -51.76435 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33f0e056-21ab-3931-86a3-25e9632ff8c2 | -1.56633 | -52.01949 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 077b7ca2-0db5-3bf2-b62e-8414ee325472 | -1.19439 | -53.67111 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c759b47d-fa4b-34f3-94e1-3a6760bf747c | -1.04896 | -51.74515 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a157b4e8-a610-3ebd-b2a6-c0ade5e003ea | -2.20262 | -53.65622 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 71b11975-4ff8-3f08-afb7-ece248009bb2 | -2.24266 | -46.85461 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21e5affd-24b7-34f4-9e50-5216daceb7e0 | -1.54992 | -53.44051 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50405236-e6ba-3066-9662-cdc6ff6aa9d1 | -0.27116 | -51.39248 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51a86e8-a6e9-3442-acfb-1f15b1d90730 | -2.14311 | -53.77375 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49a6d480-74fd-31b6-8601-f8ba17d9dad0 | -0.96398 | -51.72455 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbb019ed-6fad-330f-943a-db59dc4e138a | -1.15094 | -53.51593 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 063ee0e6-8970-3e45-a1e3-d141dcbf1b13 | -0.90708 | -51.73745 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34eed1d6-ee73-3c87-9a49-f74a149f4100 | -2.67351 | -48.2869 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d73ea17-b1ea-33d5-b7ca-43376fc20221 | -1.2962 | -52.22397 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f1231e-901a-34d8-8611-18e75084f8e3 | -2.26363 | -50.44786 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d38cc0d-0ac2-34b0-afce-940fba2e9f29 | -1.04453 | -51.81669 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36e6dd89-8b2c-3226-a096-ec794df90095 | -1.78591 | -53.60511 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883c3c9d-54f7-3676-90c7-1ed0a42fb2cf | -1.21493 | -51.74499 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642d46d5-fbc1-3b11-a328-bc871f02e992 | -1.12103 | -53.72712 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5428feb-d5ea-3dab-a7e9-064189e417cd | -2.92816 | -48.33909 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7f43623-97f3-3dcd-86a9-2bd813a62538 | -2.0153 | -54.52108 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bfd3167-2add-33e5-93b0-f571a08cacc1 | -2.14002 | -53.64253 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e11c6615-e352-37b4-aed9-40ba89a7e45c | -2.68321 | -46.24552 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ba3c16d-d54b-3486-961e-a335c34b0ab6 | -0.31712 | -51.40689 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffc0ee36-7312-3384-9c39-4666ee1a406f | -0.81265 | -51.60338 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4056ea47-9c96-30b7-88bb-d2992ee8c0b4 | -1.34409 | -51.39098 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163e7c30-2821-333f-8e43-2b9535e4efdf | -1.2671 | -47.6671 | 2024-11-21 04:53:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
