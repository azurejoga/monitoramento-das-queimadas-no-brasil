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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 685dd26e-cb72-3c12-98f3-72b24b289782 | -1.07645 | -53.39582 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e24e92eb-c869-364c-a60c-2f875ac57c17 | 1.27641 | -55.90662 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fc29d2f-9db6-3e29-94bc-100848d145b7 | -1.09533 | -53.60239 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ac58083-a9ff-3770-9759-52111c1d80e8 | -1.51871 | -45.90761 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 502e68e9-0d4a-3d61-9fb7-10a1cb8b211f | 1.18172 | -55.95341 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e784f4f0-e876-3142-b61a-ac376b5961b1 | 1.17712 | -56.01046 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 618a7c94-c025-36ec-8162-3509f19ddc33 | -0.82174 | -51.59955 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 701f07ee-efb6-3c0c-8905-951772e08f05 | 2.73697 | -60.38671 | 2024-12-01 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0390f8bb-32c3-3e18-9117-0552a16e950b | -0.99656 | -51.71524 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bef87a0-776e-383d-b815-826dd01f3931 | -1.14141 | -53.67328 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7536953f-5025-3c1c-9eee-7f4e08db32db | -1.08124 | -53.38837 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eceb1ce2-d336-386a-912d-9c49989806e2 | 2.20235 | -55.78968 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d6b42b4-44e6-3adb-ba6b-cde38a68db85 | 0.07571 | -51.48795 | 2024-12-01 05:05:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0404eaad-6516-3b8d-b77c-c83898386a1b | -1.0835 | -53.39692 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fadb5a0-9350-3dd0-82ef-6a108d46dd58 | -1.09157 | -53.64964 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e4ef131-dd1b-3f52-99a6-135ea4b370d4 | -1.19459 | -51.75942 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 023eb917-2a6c-3277-b179-a68218d38d17 | 1.16681 | -55.96629 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1afe02c-0380-3c3f-b2aa-cf1ab01d53fb | 3.2683 | -60.07694 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6dbd3b3-d3dc-373c-b425-67da2c0010d4 | -1.07673 | -53.23263 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd836ac6-9985-344d-ade7-67efda36a452 | -1.04061 | -51.73671 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fee2c25-e481-35c7-bbaf-5114b1ce3f6e | -1.09951 | -53.38709 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcf3e5bb-5853-3592-8657-1d1f5d6de5d0 | -0.61157 | -51.70564 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54cc6b63-f2fb-35ff-a617-a41f894b2fb5 | -1.10578 | -52.30473 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5756fecd-dd81-38fe-946f-5d1099e63a87 | -1.15372 | -51.707 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8646982-1f24-3b02-a0da-eeb39e6afc68 | -1.24485 | -51.79165 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 498d34e0-5f08-343e-b91c-d8257524deb4 | -1.32122 | -51.66695 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 088eb8de-df8a-3de2-9852-1637c39dbe05 | 1.15951 | -56.00616 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4fee2d3-dc6f-3ba3-8c1a-348745221f24 | 0.63046 | -60.06285 | 2024-12-01 05:05:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbee3c6b-7c79-3f9a-b280-92c26701fcb5 | -0.60953 | -51.70673 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2974c222-a3a1-3d42-bb06-e1fef48e436b | -1.3145 | -51.73558 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e06a0f0c-992a-3b80-8054-e906e02bec05 | -0.59772 | -51.69378 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 40cefac4-a443-38a2-955d-0a639cc272c4 | -1.0738 | -53.22812 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d180c75-619c-3b83-86d2-c2ee3c10d0b7 | -1.09535 | -53.39055 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d2d1bf8-37b1-36f6-b263-6ce8c0b460fc | -1.11773 | -53.22661 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e654900a-4949-380a-9422-7af3f36f1bcd | -1.27815 | -51.73988 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d2c1ceb-a665-31bc-b22b-f63984107141 | -0.2503 | -51.60826 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dbc7812-265a-3753-bb82-b934dda00453 | -1.08576 | -52.43323 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cd411dd-da24-3b3c-b157-30a62286f87c | -1.08005 | -53.63177 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b3ac2a7-93a4-37fb-acd9-2f9acdf57f7e | -1.15561 | -51.70409 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a8f841eb-fc42-3459-b40a-7df74cacb5bc | 3.26535 | -60.08457 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1812f9d6-6e8f-3a0f-8a1a-6f05e1659704 | -1.20532 | -51.74136 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 319d848a-8e67-3eae-852a-6b6516f2c816 | -1.25249 | -51.74365 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47cf7339-ca21-3822-9d12-3c0c1986a4bb | -1.15217 | -51.69188 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8aaadde6-caa9-310c-bb49-8dc3189ba2f7 | -0.19098 | -51.54794 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d446888-85ae-3aef-917e-12c30a4d4fcf | -1.31997 | -51.75129 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b59d7aa7-fd81-398e-a57b-83500973f90e | -1.08703 | -53.39746 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ece570c-bff1-3a4e-a3f5-ea4284d4af31 | 0.93802 | -50.74096 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5efb9ce4-409c-3b9c-b73e-dcdc56c3ee20 | 0.85698 | -59.45001 | 2024-12-01 05:05:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8adda122-7b68-3ee9-81cd-45c7ecbe857c | -1.05426 | -53.2134 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 881884a8-4d3e-354d-88f5-6df489373b52 | -1.52326 | -45.91654 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83ab7089-1743-3c91-be07-84b9ef711438 | 1.67678 | -50.66685 | 2024-12-01 05:05:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faeeb2f4-6bb3-3b0c-856d-4a70324c717c | -1.07068 | -53.64622 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142112b5-e0a7-3708-9cda-eb5d6719c326 | 3.27472 | -60.06527 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6922a5cc-2fe1-3708-a109-7343131a57ed | -0.97786 | -53.72765 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b3a770-264f-3aff-9035-b7338025f377 | -0.8333 | -51.81411 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dda32625-01c3-3a96-a832-a493a8b8cf8e | 1.25509 | -50.69065 | 2024-12-01 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8937b035-6843-34ec-b7ae-c4b55ca0b21f | -1.31526 | -51.73073 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 823fb409-dfc0-3f02-8539-9886b37b908c | -0.76343 | -52.46087 | 2024-12-01 05:05:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4c753bd-3bca-352b-aac3-c8e08a5d1ccf | -1.21381 | -51.73773 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7595533-03c4-3933-8c89-8c8ea4c60230 | -0.94915 | -51.66357 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff28fc5f-6f21-3606-92b0-7bcff7c1bd3a | -1.14201 | -53.66945 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6722f57f-916c-387c-bcdf-371e8baf8a24 | 0.98523 | -50.24695 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4a6e1e8-e9d2-3ee3-a30a-9b28fd222af8 | -0.96225 | -51.65569 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06b6378c-43db-3adf-97c8-f5ea9da27815 | -1.23238 | -51.80665 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aea47e35-b4f9-391d-8e17-2e4e7b1ef342 | -0.10154 | -51.32845 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f5d035b-0c7b-3626-8edc-bb072e861627 | -0.19869 | -51.54914 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4592a1df-7e11-3f5c-ad3a-03d677322ea8 | -1.26745 | -51.758 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 229b779c-4617-3fef-a313-f6b9f56e3268 | -1.09412 | -53.61017 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a7445a-8db7-3934-842c-69f7784130ed | 1.44361 | -55.87001 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517f8243-b1cb-3530-8457-36e2887fff63 | -1.10292 | -53.59959 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5143a403-6cb4-3ad2-bdc6-786a2064dd9d | -0.29192 | -51.60754 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a469ecd-91b2-3df3-bd82-7618c1d799fd | 0.99397 | -50.27586 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a599086-7a40-3992-a535-52540601203e | 1.15208 | -55.98217 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a33f3ee-e701-36b6-aa4f-361554ed4a1f | -0.25137 | -55.91386 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faa77bab-8dc3-33a3-bc3d-16746ec99814 | -1.32046 | -51.67183 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c65909b-76e3-3bdb-8434-6aca115dfeb6 | -1.23165 | -51.81145 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02d81eb5-0dc6-38f3-a3d8-88e1828a07f4 | 2.73752 | -60.39031 | 2024-12-01 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2f3bbf7-92e8-3232-bc99-d1cad91d7a09 | -1.07368 | -53.62678 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8144af8-db58-3b69-a8c7-8f61dae9cd48 | -1.18787 | -52.12543 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fa621d4-2648-3d0a-b5e7-110d89bc27c7 | 1.1552 | -55.97865 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 999f7f63-721c-390a-a3c6-408a5c0a75c7 | -1.32359 | -51.67731 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6db8c6-8556-3d1d-aff3-6785e443f730 | -0.29029 | -51.60466 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6ec89d0-e9eb-3f29-ae66-9ec5eda78891 | -1.51755 | -45.91079 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 066dc33b-1bef-3a78-bc48-04fc40b49b05 | -1.19534 | -51.75461 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 11c6bee1-1cd5-322c-8813-86bc272a4c01 | -1.07597 | -53.63511 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f819aeeb-a7fb-36c9-9267-5b18f4a4af84 | 0.94764 | -50.75006 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e156007-229c-3059-ac1e-8886db9406f0 | 2.11779 | -55.8769 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cef5203-04f5-385a-a687-60e03dd5a64f | -1.23025 | -51.80903 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 901a9ecd-69f4-3b7c-99ad-8b9bf3a4bdfa | -1.14489 | -53.67384 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57b3ffbf-e39f-3514-bf1e-52fcd3f1d114 | -1.27889 | -51.73505 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56d2f2b6-1d7c-3361-bb3d-d0ce7330363c | -1.15056 | -53.61525 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efa8a4d7-30cd-3b79-8990-109f5ad259a6 | -1.08532 | -53.20105 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eee5f33e-d0cf-3581-b8be-eed323fde1d4 | 1.14433 | -55.99746 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2829e8d0-9966-3745-b2dc-f29b53a5091d | -1.00042 | -51.71584 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d79a8ee0-171c-367a-a83a-67f092de4f13 | -1.09352 | -53.61406 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a858fa9-407a-3b2c-b893-56ac3717844a | -1.06069 | -53.38123 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cdf6879-f4d2-3f64-9fdf-034997658c2d | -1.51692 | -45.91479 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6efbe45e-4180-3ffd-9329-205bd09b57ab | -0.58618 | -51.69204 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 904e8798-4997-31b5-a46a-4cb6acf78436 | -1.17855 | -53.41497 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09aa0c36-03a3-3389-ad1e-0bfa7f289b30 | 1.14487 | -56.00089 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README72.md)
