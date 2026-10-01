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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f0fa3f6-806f-3133-9224-c3bdb5e373db | -1.63798 | -55.12622 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d786ad0d-5ef0-3a5c-b272-45b35850bbd3 | -4.25695 | -50.7456 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 67b6d73d-680d-357c-b184-5cd778efc139 | 1.71011 | -55.91927 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2200c02-3d0e-3e04-a551-3ef5d0967453 | -3.57507 | -51.4777 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71f6ec45-5494-31dc-a53d-946943bfc81b | -4.30444 | -50.76398 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aa8be7ee-6e73-30bb-bcde-b011bfcc07fa | -2.96659 | -51.02802 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b359b852-ba9a-38a4-ab3a-1d19f9bf16d8 | -3.80517 | -51.02708 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9d63be81-a28a-3b3b-a968-54e61592e955 | -4.0435 | -54.23318 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0327c2a8-f21a-344d-946d-9b5f7de19572 | -3.22643 | -54.31395 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b0cd12f-7fc1-3253-960b-c3b51e9b6975 | -3.59695 | -54.55423 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbdbaa3c-28b5-3029-a283-37c1b7174a5b | -4.29058 | -50.79009 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c3f5db99-74aa-3d09-a4d7-fb5a9b4a432d | -2.93528 | -54.19107 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b1f4d9e-3e52-371e-b181-6d0326663115 | 0.49828 | -60.5985 | 2026-10-01 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f95a7a2-550a-3441-bb32-4782ea167995 | -3.5969 | -61.71771 | 2026-10-01 05:16:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67f4f3d5-fb73-3502-8384-9e9c5794e33b | -4.44737 | -50.66124 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b04ce60-1c4b-3f6e-b432-8949969b86d5 | -1.08634 | -54.10749 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e265162c-e3cf-301a-90a5-4c131124510b | -3.17024 | -54.10069 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 828719fd-1704-3fb1-b8cb-7ff239c208d1 | -3.09203 | -50.26016 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 484962c8-02ae-3515-97c2-4163d241fb4c | -1.75711 | -55.64135 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f03bcea-3c1f-3ea9-bc85-4305cb4f496d | -4.06469 | -55.37151 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9228b38-aad8-36b3-a522-0ae604746a6d | -3.95709 | -48.12473 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9afda073-e627-3cf0-809a-812a2299c1b8 | 1.8538 | -55.55803 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc43451-0b7c-3ed9-a41c-c738ad723d4b | -4.28728 | -50.77842 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 64fde3a7-d26e-39a8-988d-e3d697fd5425 | -4.29381 | -50.76808 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 297.8 |
| c25846e8-e9ad-3d68-a033-88408791cbaa | -4.14601 | -48.91171 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c29e376-fb24-3189-bce2-37529e776f3a | -4.25776 | -50.73995 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 872fbcab-2a90-3e7e-93be-65d3077cf359 | -1.75552 | -55.64006 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6871374-1f09-3eaa-a054-6ffd734deca5 | -2.99489 | -51.03241 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 144f15f7-bbea-3932-bd8f-81993a08a2a2 | -4.38989 | -54.8251 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c1f419-8127-38ef-8bf2-3f2ccfab7dbf | 1.87143 | -55.62592 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9750f5c-6549-3c72-aabc-d27ae04a59e0 | -3.48932 | -59.5324 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf4341c-9c92-343a-859d-189791734fc3 | -3.68852 | -60.54029 | 2026-10-01 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b17da236-df54-3e59-80f0-51299883b96b | -3.80164 | -50.60381 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b608cac-3620-3d83-a129-81050fe1082e | -3.37954 | -50.95607 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9affb4e8-938a-3b41-bb63-5207c472129e | -3.24849 | -50.81284 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a08e475-826b-33aa-959e-11fff0abf792 | -3.49318 | -54.72548 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eabd522-3217-3120-aea4-5fe6257a67e2 | -3.87685 | -51.97602 | 2026-10-01 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c92a849-e54b-3e38-b58e-9fdd49b4fca5 | -3.10808 | -50.28886 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4ba8e57-3d88-3346-ba94-d436f720ac44 | -2.46067 | -56.07631 | 2026-10-01 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c553fc7-d965-38d5-b7d2-910059e9eff8 | -3.14426 | -53.74558 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a7ef5ee-4b23-30a9-901b-cc4023649dfa | -2.78845 | -51.65889 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c578bdc2-83da-3ba1-b7ea-38145c76039e | -3.25018 | -50.12507 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1985810b-bf52-3cca-9d03-ffd3257e85f9 | -3.24936 | -50.81069 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12526ac3-8c65-31da-b32c-242fc55ca4e8 | -3.04237 | -57.51465 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d82ad5-4387-3083-8c97-c5097b609c34 | -3.16238 | -54.0748 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3a2fd9af-32ed-3cfc-9c07-598bbe1348af | -2.99399 | -54.90322 | 2026-10-01 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cad2df30-3020-3210-b94f-deb5ed96bad3 | -4.28973 | -50.76168 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b68c69b-e51f-3e03-9624-333fd0ca3a39 | -2.54773 | -57.54437 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0241f0-ffac-3ec1-a759-856c0d632852 | -1.32567 | -56.58634 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0121a6e-eda8-3b42-b9b3-fdd3019e4076 | -2.89589 | -54.14176 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6813fc5-5dea-3e58-bda8-3087a84dec46 | -3.27112 | -50.70023 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9f11fb3-c061-38b2-a0dd-7899a985f485 | -3.4785 | -49.92252 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a72028e-18bc-30c0-8cbd-5242727de3b9 | -2.64846 | -56.54396 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5519bdf8-7d3e-35fe-b57e-b8a13c433d5c | -3.48988 | -59.52889 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfabad64-45e4-35d8-94c5-7d4bc63faa69 | -3.18321 | -57.83513 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 426a1ebe-f6e4-3e26-bae9-2da91856dd7c | -4.53882 | -50.77187 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5627912f-c210-3252-b162-fafa4e2a3870 | -4.27009 | -50.75884 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b91ce7aa-2938-3ae1-8845-72c5f0420216 | -3.82882 | -55.79711 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef0f4675-d8bb-3240-82a5-0f938ba58ed4 | -3.14819 | -53.74619 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fef438d-6115-33fd-8cdb-4aca9ffb86a2 | -2.91896 | -58.30756 | 2026-10-01 05:16:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3232d79-47f7-3c53-b4bb-3d2c5cb907b9 | -3.76416 | -52.19039 | 2026-10-01 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 019c90e2-d2fb-3dc9-a3d8-0e9071bf7001 | -4.04032 | -54.22789 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9fd789d-274d-3ba4-9dbc-a7d272474963 | -3.12269 | -50.26249 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48addbe-ce11-38fe-8db9-665e59feb805 | -3.71361 | -54.22345 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15438bb6-0e21-3a9d-8a3f-feb3189e32c1 | -2.98103 | -57.90929 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f181fd3-1c4f-3736-9e30-a434e436af80 | -3.73297 | -54.65263 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| babdb133-cdb3-3290-aa3b-6c17d9fda8d0 | -3.16164 | -54.07962 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 37fcda9f-46e5-3e22-8af6-bb42eb121dc3 | -4.04227 | -54.23038 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b83368f-298e-36d0-8b30-5af9194926c9 | -3.70752 | -59.68206 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fcd9af7-aa19-39e2-b28d-f3e9e4e3612d | -4.63303 | -50.62117 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c85407d-eeb7-37c7-a8c2-4afec9be633b | -3.4241 | -54.54216 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e19f2882-0e03-3a42-b952-dbbf1547aeb0 | -1.37162 | -54.63721 | 2026-10-01 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5938d6-9cfd-345f-858e-92a66d1fe76c | -2.41939 | -49.29578 | 2026-10-01 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 969dac6a-ca1b-3ce2-a79a-166076b9961f | -1.90998 | -45.80986 | 2026-10-01 05:16:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f9fce7d-4c00-3a7b-b92c-586dcc6d1cfe | -3.82822 | -55.80107 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd5d3158-f1a7-39f7-a200-00f8a6436db6 | -4.63887 | -50.61602 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a4cfa13-39c8-31b5-bcd8-cc4341b1d04a | -4.25871 | -50.76822 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5b03595c-501c-3a2b-8a2d-3f82682f9508 | -3.85236 | -55.80883 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16d2049b-696b-3803-b419-59b5f0247948 | -4.26679 | -50.74695 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 699d2fb3-bf97-3ddf-8bf5-8dba6e34aa68 | -3.18353 | -54.10447 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5450ce5e-97c7-3a4a-befd-40e7e38c88ba | -4.05884 | -51.10162 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b37e0c9b-c6f9-3508-9528-d79a4a2b0fa8 | -3.76868 | -58.83845 | 2026-10-01 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 736181c6-9417-3b86-a707-66598a98ea47 | -2.98677 | -51.03242 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f7f7000-0ce3-3165-8be3-5697a695c0f4 | -4.06904 | -51.09719 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e4c1df8-bd42-37ab-bd6c-a8b7426bbe99 | -3.27031 | -50.70554 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ad65f95-e8ed-3b1b-a008-a4085de0010f | -2.92887 | -54.15646 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3954e48-eaa1-34fc-87c6-55c774660c9e | -4.15979 | -48.89508 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9503d9b0-f4eb-366d-b8e8-4be464584839 | -3.58808 | -53.99849 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32858f8d-9033-3192-a66d-4f834540e9d9 | -3.2999 | -53.85818 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5232f1f-91f7-35dd-a786-755db4f5fc67 | -4.63551 | -50.60411 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 52ddf2f2-391a-39bf-8f64-9670f361be38 | -2.50382 | -56.90925 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 29f42d5c-97e4-3e99-b0ea-d4a526eacae3 | -3.48505 | -54.7288 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2cfbc9a-1f40-3486-8530-ff2c657cb251 | -4.26282 | -50.77447 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd1f5357-1ebb-33f1-a426-67fa4b1a6bca | 1.87652 | -55.63626 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f975973-6544-3e4d-ae07-02a5916dc364 | -3.87809 | -50.66582 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f670135e-e38c-3485-9718-e62a0636b4da | -4.28808 | -50.77294 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 297.8 |
| bdcbdf6a-60f8-3002-9db0-0656c31bff8d | -3.59757 | -61.71355 | 2026-10-01 05:16:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b2f1764-767e-3eeb-b37f-2a4e707badb2 | -2.91884 | -54.14529 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83014f88-3ebe-35aa-ba89-3062c91487e5 | -4.83366 | -50.68641 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add1abee-09bc-3e05-b50c-2b2fb405ad2f | -4.2497 | -50.76117 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README76.md)
