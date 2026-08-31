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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eae2402b-74ea-3c46-925f-90e1b555d146 | -5.95814 | -57.68476 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9a19d7a-26ab-341a-ade4-f8d268051704 | -7.3332 | -55.14926 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9852f26-1f8b-31b0-afb9-fca0fa9b1af0 | -4.95752 | -55.8477 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11eb46f7-9099-3569-b47c-3de35694b6ac | -7.2884 | -52.36448 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00676f0e-872d-3014-a51d-a24e05368adb | -6.08737 | -57.90884 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5278e02-cf05-3616-aed2-782fee33396a | -7.64087 | -46.71928 | 2026-08-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d90b4ed9-6bc0-3878-96e2-b865e6ded20b | -5.89015 | -57.75861 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c265e15-f2f0-3f85-9d3c-06d4be6a7e9e | -5.25045 | -55.90488 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 91069e2e-7ab4-3dc1-951b-79642463e800 | -7.06018 | -52.71663 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80db77dc-6ca7-379f-9478-7c8ebcd3a023 | -3.6327 | -60.56192 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c92181f-8167-3180-9028-40bcefa00c19 | -6.53366 | -55.10748 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba0c9ee2-0d0e-3d5c-af4c-fd7de1d18f99 | -6.21048 | -53.58328 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea05db4-335a-30f8-9270-a3c0686e3a16 | -3.11433 | -61.23108 | 2026-08-31 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c144863-8df7-3e66-8245-abfef6bf8894 | -7.29798 | -60.58837 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fce67d70-91ac-3a77-8747-c3c1ffc83900 | -6.2183 | -55.42472 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab91b82-3b34-3e69-b60c-60480390f27c | -1.59666 | -54.40359 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14658c29-efd0-3703-bf52-5d5607601bbf | -4.585 | -55.93825 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6f1cbaa-7349-3637-ae2e-9389aff1058c | -6.62634 | -53.17592 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b747677e-fe3e-39b2-82a4-4e689978feb9 | -6.91835 | -55.70768 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 383bfa18-2a09-335a-8271-6119fb26895d | -6.8685 | -59.4727 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82ffbfbc-be7c-36ee-8e13-9a98b21fdcb5 | -5.49139 | -57.13811 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a6645d9-f379-37b9-a862-3ead9fc8881c | -8.1773 | -48.81105 | 2026-08-31 04:57:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 707717e6-1d0b-37bc-aaf6-614a4029fa11 | -8.75465 | -45.38071 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc2a29d-16e9-346c-b191-4fa2b24becd3 | -5.60513 | -44.00032 | 2026-08-31 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38d4a5f1-cefe-38ad-bdd3-f8ee39b82bbd | -7.97921 | -44.28405 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c7d8148-9185-391b-878c-af8f349cb7f1 | -7.52912 | -55.59 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89742406-edc2-3a14-bddf-4d26d46eb7c6 | -4.9655 | -55.84143 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48ca96c6-6b2f-33ea-9184-a2a4be68c312 | -1.62403 | -55.17094 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2176c470-d96e-3a80-9784-a368151f004a | -7.28709 | -52.53767 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f44b81a-423b-3cbe-a994-060af30d845e | -3.86408 | -49.10878 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 83c825d1-2491-3a55-9594-ebf0ccda5ca0 | -2.74829 | -60.23759 | 2026-08-31 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75bcf696-7de4-392a-9d47-32e438b4a75c | -7.41488 | -44.24965 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38f6d03d-e0ac-3323-b867-b54629a6bee2 | -9.42296 | -45.65702 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 323a0208-1527-34a4-be50-ccd6a328d768 | -7.92398 | -44.25317 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bc948d11-d8c7-383d-83aa-e6537c682561 | -6.93301 | -55.63702 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8ca42d49-46de-38cd-9f6d-98563cc20a35 | -6.39421 | -45.50129 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a02adf51-2bcb-3849-a9a1-575e1bcefe9c | -4.28877 | -59.94966 | 2026-08-31 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 404adaa9-a238-33af-9c6a-9cea3cfdf00c | -6.12531 | -57.6707 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5702ee15-f0bd-35de-a115-5406887cd13f | -6.9474 | -55.71961 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc9076a-fbfb-3d1b-8481-30cf81085ee6 | -5.59084 | -42.32618 | 2026-08-31 04:57:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4c414dfb-6ac1-30a6-827c-4218c5f51d4c | -7.48702 | -55.31676 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71eb5c1a-2122-370e-b931-6f4d108bb28d | -4.64768 | -55.85287 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34eeca5b-27ee-3102-a676-6ccdbcf7f742 | -6.75411 | -52.44729 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 601bc7ff-21ba-360d-a1aa-db72e51a8148 | -6.0894 | -57.91203 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f854898a-7b6a-36da-a261-2c36d7b96b04 | -5.87491 | -57.78311 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8924e0d3-30fa-3b67-969a-ef9e58e7db40 | -7.56973 | -55.56799 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67011828-ed97-318b-9754-585f589c84cb | -8.21144 | -54.95058 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4ed3b9-7035-3fd4-9649-f1470960c3a1 | -7.97388 | -44.27775 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a48c3ed7-1310-39bd-a09c-cdaddd000b96 | -6.2562 | -55.42341 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcd5aa75-2032-3a1b-ba59-f55ae7acb42d | -5.9414 | -57.69526 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6deff2c-ef07-3812-afec-41b3512cd09d | -5.49073 | -57.14222 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d20f551-c758-3bff-bb13-a8e0456c83c6 | -6.86045 | -59.47144 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ad3f59-a501-3a75-a08e-99707ecefaf2 | -4.85751 | -55.83571 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b61a48c-746a-3558-9e23-ca1741f2e509 | -6.93914 | -55.64162 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4105ba50-987a-34a6-bb65-4dc302fbd827 | -4.66685 | -55.93159 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b4acd2c-e97f-309d-a104-844a0551502b | -4.14709 | -60.69818 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb78a2e6-ba73-381f-b612-f5abb01323e1 | -7.11555 | -42.75902 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b73181e9-cb7a-324f-ac44-8540aba7c368 | -5.31082 | -55.85429 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed563e7b-9b39-387a-a62f-9792021aa146 | -4.86092 | -55.83623 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f23949-e975-3a8b-b491-18eb25ff0c7c | -8.74591 | -46.45406 | 2026-08-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4fad42d-27fd-36dc-a044-99cc345a77f1 | -3.16577 | -60.13417 | 2026-08-31 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06344423-0760-313a-ae0b-8519b5b0f7ce | -5.87681 | -52.15376 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca96f06b-8877-37a3-9eaf-5f2d06522034 | -5.98353 | -55.72886 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e22eb6e-d626-312e-b591-574b96901e7a | -5.97646 | -57.68757 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe5b6e9c-49d8-3e78-9a8e-b867eced0715 | -8.38294 | -44.99903 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c08c02a-ece1-3d8b-a241-fbb9a02d00b2 | -1.60055 | -54.4006 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55b11a1b-d578-3046-97a2-d4caa1cc7902 | -7.52411 | -55.31907 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 464691fd-4dd6-3461-88fd-2956ad56f8a6 | -5.59361 | -42.32579 | 2026-08-31 04:57:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 90f3ed8d-7cfe-3948-8d70-32d1da34c1e3 | -6.11518 | -53.56157 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc6e39e-5190-3057-a76e-18a9b880d5af | -6.90754 | -59.48637 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a25d79e4-3c65-3d11-b1d5-3b2230ccbb4b | -6.25174 | -55.42997 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f33f8d2b-2fdb-3435-8235-be6088b2ea21 | -6.60903 | -58.60088 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 32d2df35-3885-3154-b23b-52fcd6f0ccea | -3.62436 | -60.55581 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0c89b8f-9be5-38b1-993c-a86ac77cf91f | -6.93244 | -55.64057 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c124e6c9-c9a9-33cb-8b31-c409d75c8b15 | -6.80365 | -59.45814 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d298cef3-197e-3b76-bdc2-990a55456d17 | -3.19039 | -60.15157 | 2026-08-31 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac1fc847-e728-3fcd-b5f9-66e914ee5f55 | -8.04762 | -54.01327 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d9820f4-2966-3e9e-80e4-88a498d929e1 | -8.38317 | -45.76555 | 2026-08-31 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc154dda-7489-3bb2-86a9-9a6a7ef8fcbd | -7.52688 | -55.3231 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13ce655a-9e1e-358a-b29a-ffe04fcc0701 | -6.86785 | -44.43567 | 2026-08-31 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 314dc756-ebad-3036-843a-bab68ba3c475 | -1.62119 | -55.16673 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0602771-8621-3079-bef7-7df8a1359640 | -5.88458 | -57.76582 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c9f78fe-1173-31fc-85d8-bc6f2178f6b3 | -3.97426 | -55.65008 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13b06fb9-ed6d-34cb-a973-a4c1f466d3ee | -6.16016 | -57.78042 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01836e59-35e3-33eb-9e83-f2a3595d5226 | -7.06747 | -59.70887 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38fe6db8-248f-33ca-9dd3-7ce7335da8dd | -5.8934 | -57.75817 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c330769-e531-3a2d-be78-a2e6bd161da9 | -5.24938 | -55.88966 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9ecc06a3-9183-34ca-a421-2ab46249679a | -3.86801 | -49.11197 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c5c106d2-698a-3b76-a89b-8be0bd451da5 | -1.59386 | -54.39954 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 164f6984-c88b-3ac9-a8b2-6ca09a176d31 | -6.93858 | -55.64518 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10f887b9-ba93-38b4-9468-2c298ff29a8e | -3.79732 | -59.61186 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96e6eec-7991-356d-8868-b2c0049f04bc | -3.88748 | -59.40155 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4c2d157-4f27-3eaf-87aa-b71481d7ec68 | -6.76128 | -56.33859 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cf306c4-95e7-3a51-9fda-acfac08e98c7 | -7.51802 | -55.33603 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94492945-86b6-312f-ac98-d7358091a269 | -6.11189 | -57.70787 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a38b013b-8479-3a98-af5f-1d3d91bc4b16 | -8.23023 | -49.04861 | 2026-08-31 04:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eaeeeda-2d4d-38ca-9e7f-30537ec7ffac | -5.96985 | -53.57842 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb9cafd6-399a-3268-a8cf-dce3e1febc91 | -3.22866 | -46.36901 | 2026-08-31 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5f6a0e4-0314-3a5f-96a8-777a51f7809d | -4.15242 | -60.69427 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fdf59b3-0456-39e7-9cce-6424a06057c5 | -7.97717 | -52.08232 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
