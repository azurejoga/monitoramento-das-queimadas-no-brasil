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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21f149b2-8cb0-3297-9b79-57bb2463425e | 0.67998 | -59.80602 | 2024-11-03 05:31:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7b437f9-5bf6-3989-9039-274c02f8483c | 0.39281 | -62.68034 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98947f60-bdd0-335c-a938-87e56b5cc4f2 | 0.39227 | -62.6769 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aeced86-c0ae-3e04-bfcc-59157a825791 | -3.30012 | -50.03215 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db84ba54-5e4b-3129-9cde-1ee2f759224e | -3.29524 | -50.02695 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 488e8c14-bc4e-33c6-a1b7-346f7a2ef2ec | -3.29435 | -50.03323 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aea8675d-2b44-3ea5-ab18-224f09e39862 | -3.29422 | -50.02487 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 599b749d-1f83-341d-aab8-e1d97a5e87b5 | -3.2933 | -50.03109 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21fa8bd8-7efe-3f94-a014-4ad1706758d1 | -3.29237 | -50.03736 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce706c74-ec53-3497-a7e7-64a96152521e | -3.11085 | -50.27092 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 828c0c50-deeb-355d-bd69-f37e34b13b76 | -3.10998 | -50.27687 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5338963a-5287-3fe4-987e-3a230f55bc52 | -3.10911 | -50.28285 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b4583131-3cdb-34d6-b6ba-2448cb52a0b8 | -3.10823 | -50.28888 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dbe633aa-92d3-398d-aa3e-e98771baec8a | -3.10735 | -50.2949 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2ed9310f-c514-39fd-9483-6d7030f37630 | -3.10649 | -50.30077 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9d74155-2b11-3316-8bed-b3f820a419bc | -3.10564 | -50.30662 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13df0599-7fc7-3645-a9da-fa907c83d10b | -3.10413 | -50.26992 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09ef640b-6aa1-34ab-aa3d-6b379ee69210 | -3.10326 | -50.2759 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bb258ff-cbf1-3e55-9f2b-b4cf399bc3bf | -3.10238 | -50.28192 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c624c706-e362-3b1c-9d2b-5cd96ff9e44e | -3.1015 | -50.28797 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d2ef7fd8-eec1-3f8b-abce-221c140526a6 | -3.10128 | -50.26738 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02480dc2-9aae-31d4-840b-0ba421165798 | -3.10063 | -50.29398 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38e33dfd-ec0a-30b8-b69c-a60c4883343c | -3.10037 | -50.27331 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1deb5775-1e88-3b7b-8900-b92659c8b9c7 | -3.09978 | -50.29981 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a768c40-9a09-3e2b-ad97-377c08cf0a5b | -3.09945 | -50.27938 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d1fd7e6-53cb-37fc-91c7-803b10d31a4b | -3.09893 | -50.30563 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 109310ff-4bc6-31c0-8ed5-c10b4b3ed681 | -3.09853 | -50.28539 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5c72220-e0d5-3d4e-a0b7-2734c1436ca6 | -3.09762 | -50.29139 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 270dfccb-606a-3af6-9f29-5111bd079878 | -3.09673 | -50.29726 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee2b4c4-aa20-36b5-8161-863d73223721 | -3.09585 | -50.30303 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57b74a81-009b-328d-9877-53092eb3597e | -3.09565 | -50.28104 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 344c3164-87f7-3676-aa1c-8905433b9609 | -3.09478 | -50.28704 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64100e43-90d3-3a07-8b61-fadec423f4bb | -2.98817 | -49.52483 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87b06765-d138-3824-9fa8-88c4203bbeca | -2.98715 | -49.5316 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd31f623-9f8f-333e-8fcb-528cd77ea5cf | -2.98648 | -49.52631 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 92da8d1e-5c21-3898-82ef-2d1e4c4452b2 | -2.9822 | -49.51695 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aaa0eab7-74de-3bd3-9953-42157c556a35 | -2.98119 | -49.52364 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e51e6d9e-fff8-3e34-ac47-77139d12bbac | -2.98048 | -49.5183 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd52d5a2-3c3c-3181-89a1-db0a293bdfad | -2.90995 | -51.46794 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21a6b272-85c8-3f2c-89d0-b8f8e7810a86 | -2.90518 | -49.42353 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d645274c-9ffa-360a-9ec6-7ae8e4394a4d | -2.90495 | -51.46909 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59ee1fcb-3ca4-347a-8375-5ce027c3b9f2 | -2.90373 | -51.46694 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4dec2f2-0b0c-3697-a99a-26651671e592 | -2.90281 | -49.42308 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f715614-1a8d-3590-b0c5-110acbed99e1 | -2.9022 | -51.77806 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d5c0f25-c675-3f7b-a20d-8428dd8d87ef | -2.9015 | -51.78277 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c1a0de5-1727-3046-b271-83731f4d8563 | -2.89814 | -49.42251 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d315dd94-12ad-3858-91f7-9373b9498679 | -2.88911 | -49.4346 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ebbbf91-a3fe-3b01-8873-675cf4003908 | -2.88804 | -51.747 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5829c5b0-23a9-3b53-a719-5e07af46c834 | -2.88737 | -51.75157 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070c3eca-eeb7-353c-9059-9d61d3488e2b | -2.88192 | -49.46804 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dff97617-6871-38b7-807c-7f7091468f8e | -2.88191 | -51.74617 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93abfe96-e568-392b-b4bb-d1abbdc0c255 | -2.88122 | -51.7509 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0714467-c270-3af3-b441-bb74c77a0115 | -2.84907 | -49.49727 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2935127-90b7-359a-8355-6aea786cc4c1 | -2.84488 | -49.49008 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d23a887-816f-3f2c-888c-fecb3a74452e | -2.84389 | -49.49672 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c87ed28f-2cee-3305-8773-fc3d4f9eb8a1 | -2.84302 | -49.48952 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4e0c931-4832-379f-8257-7287b3d0de68 | -2.84206 | -49.49622 | 2024-11-03 05:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c5d4608-a666-3f84-9204-0e7adca144f7 | -2.83383 | -52.87679 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c89bad3-fa62-33ea-baa2-e7b4126a6ee2 | -2.82965 | -51.80545 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 526d6379-268b-3026-8ad3-e1031f4789f5 | -2.82898 | -51.8101 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6710afa0-eb1d-3e6b-b50e-2e9452a6b3e9 | -2.8285 | -51.80683 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaad505d-2e8a-3b45-b78b-c9a33e74fe37 | -2.8278 | -51.81147 | 2024-11-03 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| badb56c4-3d22-354b-9614-1e741a509682 | -2.8182 | -49.15578 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 203ee1fe-7656-3541-b880-352044619b78 | -2.80205 | -51.60635 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8bfdc1bb-000f-3867-870d-ca04becf4128 | -2.79659 | -51.60064 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b9eb5b4-ae2f-36bb-a993-3454cbcb7fa1 | -2.79589 | -51.60543 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23c41d1f-3be3-3586-8786-e1f755bbece8 | -2.79519 | -51.61016 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed9b04d0-4324-3963-be9c-250f5f001129 | -2.7904 | -51.60482 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af11953a-776d-3092-a0ec-31e3ad1b6adf | -2.78973 | -51.60444 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 30fb8efe-1c88-3910-b679-5be883f1fb46 | -2.78966 | -51.60962 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 26bcf2e5-037b-39eb-951b-b9c9b51537ee | -2.78903 | -51.60926 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67d7e996-82ba-37a1-9f7d-6672256f92db | -2.78893 | -51.61439 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 249a15ef-b35e-39a5-aef7-5e2405ffc824 | -2.78832 | -51.61405 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7a791e5d-f36e-32ff-8e48-697c7ed34163 | -2.78424 | -51.6039 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 270e371a-8713-3570-9b7a-eda7bd9dcf10 | -2.78351 | -51.60868 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14e56ee1-5ae6-3280-8107-ec7112a2e852 | -2.78287 | -51.6083 | 2024-11-03 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e634bb19-4218-36ec-956d-60b12903bf8b | -2.75275 | -54.42337 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6380f6d-a798-3f6f-acfe-8372e808b1a3 | -2.75229 | -54.42638 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a3fe9ce1-047e-3c3c-bb04-c106ceb50174 | -2.75184 | -54.42938 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 36efa0e8-6257-3eb8-b190-653cc152472c | -2.75138 | -54.43239 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3836e4b8-8128-3153-9b72-e5a14af5d537 | -2.75033 | -53.2159 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5796d7fa-fc0d-35ac-a6fd-0d4bdd504251 | -2.74979 | -53.21939 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5f9fe43-5530-3e75-ab02-1b3315524df0 | -2.74955 | -53.21523 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6f36e0c-48c4-3060-9d43-a72a68d665ae | -2.74924 | -53.22292 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2ebb02e-9cd8-3e47-a423-3952a4b065cf | -2.74904 | -53.21874 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 326a025a-46ce-385d-904b-c4f161fdc3ef | -2.74852 | -53.22226 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7b4492d-c95c-336c-9465-da08f3e1356a | -2.74767 | -54.4224 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9674a32-c6c7-3ed0-8c2d-fdade850aab6 | -2.74721 | -54.42539 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c90fa22f-b085-3008-afa3-93f9f5db360c | -2.74676 | -54.42838 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0efd6eff-cf7d-3b60-838e-6d3b2293bb99 | -2.74629 | -54.43148 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4e5dd540-1588-3eca-856a-f2384ebee8cb | -2.7448 | -53.21491 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b18aa863-2e7c-30d5-a652-c82762e6a725 | -2.74426 | -53.21843 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c44c7623-0895-3297-9a93-385fd4f25bc7 | -2.74403 | -53.21421 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e44e2a8-5a5e-3883-a0f4-9e426f758e08 | -2.74351 | -53.21775 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d98e79c4-845e-38d8-85e3-88540cd9193b | -2.74299 | -53.22132 | 2024-11-03 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0254c470-32cc-3b80-8729-1e6b22d20619 | -2.74166 | -54.42756 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf6d30bf-7964-3a72-8ccb-9e6675552aaf | -2.74119 | -54.43066 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba9e6fc-4e7b-3ac1-b91f-6e6db9b57228 | -2.73845 | -51.74142 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a4cc559-ed16-311a-8e77-950c51fc0566 | -2.72717 | -49.85552 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 29046e36-5762-3edd-8791-20f6b4483370 | -2.72643 | -49.85334 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README85.md)
