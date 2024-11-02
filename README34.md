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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 889668c2-ad8a-3bf7-8c81-09ea982f78fd | -2.1083 | -50.83094 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc25ca4d-dba0-35fd-9ff2-ac52454610c3 | -1.55212 | -51.61988 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3413ddae-0d00-36d6-b2ce-fbac1b0075f4 | -1.55155 | -51.62347 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f861a74-1b09-37fe-8e7d-81ca5765f0b6 | -2.32419 | -50.47415 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e2ed03-2ef6-3721-b931-b112c098fb3c | -2.32371 | -50.47704 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06b4163-7010-3792-8144-8ad354033745 | -2.31007 | -50.62308 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1beda6b-432c-3dd7-bbdc-262e533baa57 | -2.30271 | -50.66787 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df8a8f86-4133-3dfa-b4e2-9b0f4bdaa558 | -2.29761 | -50.66702 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbed3cbe-e694-3cca-a1c6-25b45e0a77f4 | -2.29253 | -50.6661 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a0b7a2e-6f36-3177-8d54-ea9356d31acc | -2.29203 | -50.66914 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb61ec0-c5e9-3225-85b3-1f614c7689cd | -2.29153 | -50.67216 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7298f7ee-760f-3324-b816-ae35013855ba | -2.29103 | -50.67516 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7aa396a0-33bf-3588-8307-9a18c8631890 | -2.26635 | -50.51771 | 2024-11-02 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 460dfa1d-140f-31d1-9343-9b58cbbab66b | 3.41807 | -51.25415 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330d191f-d520-3a53-a048-9cfaf5f82feb | 3.41797 | -51.25188 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264a7de3-2d92-3c1a-aea8-90fe846eac2d | 3.41627 | -51.2813 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f65eb9e-5d67-37b5-862b-44e35fdb192e | 3.41597 | -51.27946 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db01bf28-643b-3153-b0db-8bc530932f86 | 3.41568 | -51.27721 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69eaae5e-8c1e-3d41-a7a9-9be89cb50cd6 | 3.41535 | -51.27538 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cee7b18e-eeaf-3716-893b-b784f19f814f | 3.4151 | -51.27314 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87017961-0e4b-3381-bbe7-7f1a010750d4 | 3.41474 | -51.27132 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d44bbe8e-5137-3783-884a-0c0841c87c81 | 3.41452 | -51.26907 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329f65a3-07bd-328e-97c5-02e68a96d51c | 3.41413 | -51.26725 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23f7a57b-5bea-3ff9-aacb-6af6d74d5a7d | 3.41393 | -51.26499 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f0f5776-4993-32c0-8736-e09c5d573eb8 | -0.73615 | -51.70411 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| decf259c-9f19-30ff-b233-aa55aa3af0ec | -0.73554 | -51.70785 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4bec07f-1546-3a3f-b9a3-8227abec7c60 | -0.68194 | -51.69511 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 963cfb61-7c8f-3043-899d-dbcffe81d947 | -0.67812 | -51.68287 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad615e80-b75e-3b24-ad77-b8e1469ba6e8 | -0.67753 | -51.68663 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6f4106d-af4c-3e7f-9a96-f6f932999181 | -0.67693 | -51.6904 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dee55fdf-5b87-3e15-ac1c-54b65063fe2b | -0.67634 | -51.69416 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2efabd1-f223-3f50-afab-e28d67d4bb0c | -0.39901 | -51.83555 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7c92ef-5fcf-31d6-afc4-3567981c0b5e | -0.3984 | -51.83939 | 2024-11-02 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0b90df8-10ac-3ebe-ba1e-06bb88746d86 | -1.93075 | -52.67662 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 038a1f9b-14c0-31d5-a5d4-c0c2ca75ae4c | -1.93006 | -52.68092 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05bc8cf6-e857-3556-b339-f33265001fd5 | -1.92904 | -52.67883 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3904f9e7-38f5-3415-9aaf-161aaa1e7b7e | -1.88705 | -52.1355 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35d4bb78-4108-331f-9519-461a7ca40d47 | -1.88199 | -52.13081 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c6168d-b930-326b-bb47-450840ca0d69 | -1.88137 | -52.13463 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32969153-3b1e-3850-b449-1cbe956e5ecb | -1.8667 | -52.33416 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6a19d61-50bc-3d04-b379-4f10014588e7 | -1.86158 | -52.32937 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5234d857-6402-3ad6-9a5a-4955a6b24ea2 | -1.86095 | -52.33323 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fa746c7-e50b-3d4e-abd5-78e840cf2fcb | -1.8552 | -52.33235 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90632f47-cc99-3530-a6ef-2f215201d50f | -1.82223 | -52.28198 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1094f493-eb4a-3df9-83c0-525be8224db1 | -1.82158 | -52.28594 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6b103c7-f3b6-3d01-ae7b-bd818ea787b9 | -1.78402 | -52.1945 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630986b5-0669-3a01-9da8-519b0eac812b | -1.58907 | -52.17061 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7b9b386-ec00-3da1-a653-3122e346981a | -1.58845 | -52.17454 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 04165444-6359-3639-a6de-26a0a923b390 | -1.58712 | -52.14613 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83fbd262-3ea3-363d-a95b-f34b0b9fcbc2 | -1.5865 | -52.15003 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa0fdd7c-9205-385e-8244-33988176f740 | -1.58562 | -52.16682 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3802b206-d3ac-3a7f-85a0-b691ce3da415 | -1.58497 | -52.17074 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5f3eb501-a14e-3aa0-b54e-c64438499460 | -1.584 | -52.16572 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52a3530d-cf10-3eb8-87e2-abef1db2dc4b | -1.58337 | -52.16967 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2e84f9ea-ad9e-3b6f-9a3e-04825a65892c | -1.58058 | -52.16196 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b832bdd9-dc60-315c-b7eb-7db3b4cabe7c | -1.57992 | -52.1659 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6fc636aa-9005-3c39-8a5a-b6079259cecc | -1.57956 | -52.15691 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e37d29e1-0f58-363c-8c89-dc4b887f8990 | -1.57926 | -52.16985 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13b2ea70-99ac-3a23-8010-677994de006e | -1.57893 | -52.16083 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39515105-fc89-34b4-b265-84994fd695fb | -1.5783 | -52.16476 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 89a75ea5-3abb-36ab-9ab1-7a53d06caa70 | -1.57767 | -52.16873 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70fb15f4-6cd3-39b2-bf11-d552c7ce116b | -1.5775 | -52.14539 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ca2faa4-9a07-36b3-aaea-62216bb95568 | -1.57699 | -52.1364 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fa27600-3588-374a-862b-f217b17e59dc | -1.57685 | -52.14929 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67512f79-dee1-3ac8-b541-280a11328415 | -1.57574 | -52.1442 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 240a12e2-d526-3999-b3a3-cb785fc627b7 | -1.57554 | -52.15714 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 78832098-c64b-3efd-9cc0-7d3d5864810d | -1.57511 | -52.14812 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18f6be00-f1bc-3213-adbb-ce9a618486eb | -1.57488 | -52.16106 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f412ba71-2dc4-30fc-a18f-a6ab23ba5f76 | -1.57385 | -52.15601 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1705c1c9-cf60-3a7a-a5e2-5caa39f87340 | -1.57323 | -52.15993 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3180f9f-1d77-3a74-9cda-8dc6f85f267b | -1.5713 | -52.13544 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 992bdba9-4c70-3598-8984-09c812ed7934 | -1.56143 | -52.27655 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c26e1bf-f9c4-315e-82b7-b5bc39b760aa | -1.56123 | -52.19826 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25f660a6-7382-3737-bb27-5c86adffd20d | -1.56077 | -52.28054 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 707d414a-ad1a-3136-9238-5c99456fdd84 | -1.5606 | -52.2022 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c0b28ba-47e8-36bf-ac89-7e49455c5a26 | -1.55997 | -52.20613 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d4fd96e-8999-3ffa-b424-318e7b8e660e | -1.55996 | -52.27971 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 216826b5-b41a-3790-a305-1d435f7b820e | -1.55932 | -52.28371 | 2024-11-02 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31bd1307-04b8-3a89-8880-21e91ef084f2 | -1.55615 | -52.19334 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b94735c-f983-326d-b2ad-cc3b433234d9 | -1.55552 | -52.19729 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6237403-97e5-3ec7-883f-5e08b702b778 | -1.55488 | -52.20124 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5dbd3ac-f8b8-32de-b980-b72df86ed293 | -1.55486 | -52.09267 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0d2fcba-33af-3fc2-9717-de78c89e2784 | -1.55425 | -52.20518 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18ab22b2-e5e3-303f-906c-27e663e42e1e | -1.55423 | -52.09655 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11bcd024-44b4-34c2-837b-5ff7e11a6f39 | -1.53223 | -52.01759 | 2024-11-02 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b2069b5-34da-3f68-957a-d5cd3fd399c3 | -1.51035 | -53.14148 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75af10fe-cfbd-31e3-81b6-a1c0b183fd31 | -1.50962 | -53.14597 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d9b0747-146c-33ae-8d29-4fb38ac43b46 | -1.46627 | -52.34668 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45b39459-2c6e-3d4e-a8ee-e0c5876a7d43 | -1.46573 | -52.34694 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d808fd-65f1-3191-afc7-255ada60d3a5 | -1.45983 | -52.34976 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d45c3dc0-c15d-3548-86b9-9fcd9f3c5bf3 | -1.45931 | -52.35002 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd2ee8a0-2af2-31e8-baa6-23f7945fe9f5 | -1.45513 | -52.3781 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c67ab4f-cd70-3109-a080-83f4eef47d43 | -1.45482 | -52.37846 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac10729a-8495-347c-99f4-6cd25f50c22b | -1.44935 | -52.37714 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1605d5d-fff7-3deb-af4e-c14ab251672d | -1.44903 | -52.37749 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca6fbd4-5d30-3185-9c5d-52b64673c94e | -1.41598 | -52.21485 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d55b65c-bf5d-3626-9776-0d2962e8c654 | -1.41219 | -52.20199 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32d8216b-54e8-3f16-ba2d-afba7d46f517 | -1.4109 | -52.20993 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752600e8-b119-33de-a7c3-4d0d64d29052 | -1.41025 | -52.2139 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0626d03-0d07-3e96-8824-b2d7149d8c25 | -1.40647 | -52.20102 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
