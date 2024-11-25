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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d180773f-d8a8-36bd-b735-4cb9642bb626 | -2.90687 | -51.71042 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5ae14625-f883-36fa-b352-84815fb0a673 | -1.38228 | -52.32409 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 53f66e9c-7803-3b69-af0c-ca5c6b3c389f | -2.80292 | -54.12849 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c65b9cb-83d6-35c6-8a25-b1dac6e2e285 | -3.51171 | -53.82213 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 400868cd-65fb-30da-8dc6-5e28948a8b44 | -1.20314 | -51.75162 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94f505ff-d2ca-3a5d-b785-e28b80987fda | -2.83034 | -54.11701 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97bcbed1-c1e5-38c7-933a-298ef255053b | -1.11414 | -52.10995 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a15beb4-3800-38ad-a2c0-8cbbce8c3bdf | -4.28596 | -59.71484 | 2024-11-25 05:20:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ffa6c5-fb8b-3564-af86-154c9924a16f | -3.50487 | -53.80917 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eacec44-3221-34fb-87e3-8df90a493d7c | -1.67699 | -53.19901 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04cca0e0-31cb-39cb-98da-3b49a42ca0e9 | -3.54557 | -50.40135 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a0bd866-06c1-37cd-9471-5083533a1e54 | -2.18287 | -53.80114 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75e9889d-a357-3dcb-909d-280ac545d608 | -1.17541 | -54.12824 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 117d84d6-285a-34e6-bf5e-cc58451e5224 | -3.62106 | -55.30072 | 2024-11-25 05:20:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f9d3fd3-0019-36a4-91c5-bfc69edd3481 | -2.87961 | -53.99725 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ca756c7-c2f9-3e4c-beb3-93c6f750ceb4 | -2.93569 | -54.08089 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18919ba0-53a1-355a-81e8-3169e65f1a33 | -1.95876 | -53.32384 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f53b335-83e7-3eff-b2f4-ff716ca62dd7 | -3.08091 | -53.25959 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ea0e99-ba6b-3bed-a46b-f86b4d381747 | -0.92785 | -52.65353 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d399dd83-0402-3bac-8011-d5e8ed96dd00 | -2.79379 | -51.68079 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b1c0b76-b959-365c-8efb-0e175ac23950 | -3.53226 | -54.08288 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a44caf2d-a491-314c-bd3c-55e9666d03dd | -2.62042 | -54.25508 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14e3e3a0-94bb-3ba5-af0c-cb28ab07b3e9 | -2.80984 | -54.02765 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 794b26e0-0162-36f0-9c20-117b315068ff | -2.57663 | -53.96989 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6978d7a0-e1ac-3f27-8ced-ed2bd03d5ab0 | -2.88959 | -51.58427 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcae21d0-6286-362c-b6b5-03e4621c7108 | -3.74897 | -54.47334 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb33b4cb-5015-3db5-96ba-4e5d5ebe5a11 | -4.2648 | -48.69122 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc11360a-12e7-36e0-bd1b-37b98886b968 | -2.32783 | -53.87118 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acef4575-274b-3477-ba43-c1e2aaafe500 | -3.25013 | -54.22803 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8475022a-7cb1-3a73-b9b5-cacdf0ba299e | -2.81043 | -54.0238 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a836654-24a2-3e48-97d7-140d16d0fc37 | -1.46009 | -51.11985 | 2024-11-25 05:20:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c476a3a-8387-37ae-ba8d-987a01a5a0a7 | -3.5216 | -53.81513 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d1da49-fe45-3e19-9438-6bbd239fa063 | -1.08976 | -54.0365 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199816b1-c633-30d4-bb5a-5dd357e1656c | -0.33515 | -51.53497 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfea6f82-c79a-3358-be2e-418e121c39cd | -0.3635 | -51.41529 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6be0410-0517-3890-a871-e5d89e4554fd | -3.41771 | -53.28436 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b38f8ca7-e6bc-39f5-a26a-a0651a1459f5 | -3.04808 | -51.44928 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01a7fe63-4c8c-3d5e-b7eb-2894424ae853 | -2.79797 | -53.00776 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ea14b18-c0cb-396d-9fc3-86d75c9013d2 | -4.85084 | -50.80807 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394d3494-79e4-3ed2-8409-38f0e34917c8 | -2.7406 | -54.39682 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e6a3edc-cd85-320a-b111-67240017c58a | -4.25932 | -48.72877 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55433fea-2705-30ba-9681-551018e65ba3 | -0.57696 | -51.71295 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e5d043a-f5f0-31b4-8e3b-4dd8d678369b | -2.93989 | -54.08153 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c908bf-2344-3891-8626-441fc84dabe7 | -3.70546 | -54.39706 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5747b4f1-3e5c-3433-ae9c-ded5a116ca2d | -3.81182 | -51.99957 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96a44bbf-4f05-35ce-8bb0-511bc4c32442 | -1.73346 | -52.32206 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e58214b0-b612-381f-9bd2-6013aecb708a | -3.74253 | -54.67418 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b572396-3892-3774-8e21-db643315311f | -0.94826 | -51.72046 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ee07254-36c0-35b1-8963-5bb92d1dc646 | -1.46669 | -52.68844 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93f5d3ad-3a0a-3cd4-98fa-987d3a02e232 | -3.66753 | -51.72429 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a23dbd7-ed2e-34fe-93a3-746969f81651 | -1.97503 | -56.14005 | 2024-11-25 05:20:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a157e076-8835-30ec-b0c3-9e25b60d8f5b | -0.96343 | -51.71747 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fc924b1-baae-3147-bbe6-0d42801a61a3 | -1.19674 | -51.76128 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 848fd13a-a4b2-33e8-af6f-f3715e332fc5 | 1.70824 | -55.82423 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f03853e-590d-3bb0-af71-477b20ddc073 | -2.79298 | -51.68631 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd662bb6-6be0-344d-a906-d5fbb992ab17 | -3.5363 | -54.49401 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d33c146-1b3f-3c0f-9180-51c6b7c421f2 | -2.63711 | -54.28415 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f37d12-007f-3800-ba1c-655cb108fe56 | -3.71166 | -52.41634 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 074e6c20-80b8-3128-a85b-22d1c968acd2 | -0.95863 | -51.71675 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd47ce90-47af-3c6e-8bf0-6a7fadd5ecb6 | 1.94658 | -60.85975 | 2024-11-25 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063a3f1d-66ef-3823-9669-c8760be355a9 | -1.10708 | -53.39714 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0702dea2-abcb-320e-b76b-83d9ef44d6a0 | -1.19114 | -51.76576 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d5764fe-3733-3e3b-9065-44d6734491c0 | -3.22731 | -53.92579 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3517f37c-db2a-3fbb-9dbb-b4e94fcb882e | -4.84545 | -50.8071 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c9ff77e-ed79-3912-b8ef-5e261b958ee8 | -2.7626 | -54.05597 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26c536d3-efaf-3efc-a342-b7be3014cc5a | -3.2857 | -53.85773 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11acb8a9-a443-3cf8-8537-f461d766546e | -3.25665 | -54.21356 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a164f6-30c8-3bed-8321-6fc174bd74ac | -3.7069 | -52.41562 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40a38b6c-53c3-3d33-a669-2ad86afd6602 | -1.40967 | -54.4718 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660e0c9a-1ebf-3008-a196-77355608f9e5 | -3.80992 | -51.99717 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c81779b-1808-3d4d-8666-d9c99112ddff | -3.77815 | -51.87362 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c5e5602-b5aa-3c93-bdfe-4655059adf07 | -2.76448 | -54.07196 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 033fbfad-4ee1-3690-b672-22803becb117 | -1.18787 | -53.88622 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a38873eb-9d6e-3812-97a7-d0137b945ac5 | -2.33723 | -52.18121 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eb6ecff4-c229-3d46-9da9-b1eeb00ac331 | -2.57109 | -54.06261 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adcff167-dc44-3897-846a-a8946322e66f | -3.95532 | -52.22793 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82a190a8-f582-3a1c-ac96-29c6b4b0e732 | -0.98818 | -51.71605 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6021aa35-2a23-3ea2-b047-a0d8da26daf2 | -3.70785 | -51.79947 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6839098-6767-3c84-b419-8ed8dc51f033 | -2.85374 | -53.96672 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e0300d4-3f0d-3ba0-8fd7-cb5b017d0bd1 | -1.10891 | -53.39437 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 232f48ba-b005-35ba-bdee-7bccc00f2f5f | -1.88849 | -53.31745 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8d7cd2-d3ee-37cd-8982-14dd80219fc2 | -0.9734 | -52.80119 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5788ceba-dcd0-3bd7-99b0-711212d2a9b8 | -1.77813 | -52.73949 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40dc76ea-03c6-376e-a75e-ccc9fdcd2736 | -2.81656 | -54.09546 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b74ac4-ecab-3fe3-b82a-62ee56e42633 | -1.13426 | -53.61631 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d11a4f42-3356-3c39-b725-0111500fee22 | -0.95384 | -51.71603 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a3ca8cf-9da7-37c9-acb2-b6cc9af14a6b | -1.48278 | -52.52177 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be0f3926-7d97-37b8-916b-ebaa3b9623af | -0.88488 | -51.71964 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8491eb6f-0ec3-376b-8927-bef231f3d3f6 | 0.94655 | -50.7389 | 2024-11-25 05:20:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 918cc04b-e826-3426-b39f-4c340b79c23d | -3.27355 | -53.82246 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5f7577c-0fc5-30e5-b3cd-e1fa51e0ae65 | -1.99082 | -53.29013 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd9058c6-90b8-334b-b1c4-9c19c9c25516 | -3.26927 | -53.82175 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e99143-3e0d-35d3-99b3-4ed35aac1f58 | -3.62497 | -55.30133 | 2024-11-25 05:20:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d329b8e4-b1dd-34ae-90e7-4dc054c978fe | -1.24156 | -53.39701 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8af6bd2e-c73c-3b2a-a950-16e53a1d5b2e | -0.27956 | -51.60957 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6951e8aa-1435-310d-b6ba-7d549c6ce074 | -3.09707 | -53.73596 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c413ffba-70af-342e-80be-796e399a37dc | -3.0719 | -50.95677 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fc5481d-16f3-3cd3-96b7-1f25994c5809 | -2.63767 | -54.28046 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008fa998-0d85-3da3-931e-429726e17530 | -1.08675 | -53.64519 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3062f346-055e-3007-bc91-bf812ba54bc5 | -3.62034 | -55.30555 | 2024-11-25 05:20:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
