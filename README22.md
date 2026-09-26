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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f7b7c1-f615-3e68-a1e6-40cf7f0cc8f1 | -1.14483 | -54.09418 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 262acc02-8ed9-3255-bd5b-a8f5ebe446d2 | -1.14272 | -54.10083 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e85423a3-4696-31c0-a1ce-040a25966da2 | 1.59067 | -56.06717 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 135df21e-a7cb-3aa8-8539-6716d202b4aa | -2.46946 | -57.93509 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 960a9e5f-c6ba-31bb-9990-114a072bd41b | -0.49472 | -49.14499 | 2026-09-26 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055c5343-c660-3f4a-8639-0144b548d2cf | -2.1553 | -53.70935 | 2026-09-26 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc9d236a-6b34-3c3d-a552-8a085c4a9f3a | 1.58627 | -55.82243 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50313719-b842-33df-a445-89ee3efeed0c | -3.40737 | -51.8711 | 2026-09-26 05:10:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eebd833-d8b4-31f2-a1a8-13021d784319 | -3.2096 | -53.41164 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fd9045e-088e-3c62-bbc8-62b694d5d29e | -5.73747 | -45.06744 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8062d86d-766d-34fc-b2c9-905cab64fbae | -2.06816 | -56.86852 | 2026-09-26 05:10:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcc80b2d-2231-3033-b960-5a6b500a1d96 | -1.90859 | -52.0873 | 2026-09-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b06d611f-dc04-3428-bd20-165f66c942bb | -2.97258 | -51.05341 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6334218-e109-32b3-bef5-8cc411fbb5dc | -1.31633 | -54.56976 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39f1b25e-6a70-3d95-93ab-c425a249ebc8 | 1.58573 | -55.81901 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39dc468-6413-3f6a-990f-35c88bba2ac7 | -5.6849 | -45.87103 | 2026-09-26 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a6800cc-e798-3489-89ba-37a0135d01f7 | -3.23038 | -54.32958 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1829635-8046-33d3-95ff-bc8f5ce28d54 | -2.91927 | -54.1609 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b38116fd-80cd-37af-aff7-e38b479f90d1 | -2.9785 | -54.1498 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59242ddd-a4b7-3cfe-91fe-421fae3b8100 | -3.10257 | -54.52259 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c70140-4089-3c23-9820-d37cda670b60 | -2.91575 | -54.16036 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bc910ef-f1ec-3d9d-9fd8-2eb7914ebfef | -3.20293 | -53.40618 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22ab232a-a55a-38b2-b7ab-992880d8f6f2 | -3.76562 | -54.81752 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97107766-0a8a-37d7-b172-fa7cf201701c | -1.26854 | -55.84356 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af374553-2f1f-3847-94e7-3c25e4327ab0 | -1.1385 | -54.08935 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c172933b-8894-347c-80f0-82b2a198a2d6 | 0.17918 | -51.11149 | 2026-09-26 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94676b3c-8601-38e4-ac42-73d256c9a515 | -3.84255 | -51.36853 | 2026-09-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eb7ffda-c7fe-390d-96be-5e6264567c37 | -1.54439 | -55.27328 | 2026-09-26 05:10:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c68382-c2a7-389b-bacc-a70f7feb2d95 | -0.50012 | -49.1409 | 2026-09-26 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77fd3d6-c285-3b55-8371-8a023f27df87 | -1.14137 | -54.09366 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d935c69-ec3e-35ca-8f01-547b36b1d5af | -2.97317 | -51.04952 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e76f6b9a-4966-3a1e-a26a-d8be76d20ce0 | -3.4522 | -50.07954 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e777004b-fedf-3710-a587-6f8e6effc6d6 | -2.92278 | -54.16144 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ce6ab7-53b7-3c28-9ebf-0a9b16f21a54 | -2.89636 | -54.19339 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc06cca-77a0-3bb3-bc50-36ce123b36f6 | 1.61076 | -55.87124 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b893154-219d-3b71-a4da-e3d9c6723d9c | -1.30004 | -54.22197 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a06207b0-1f68-397a-97db-502084b2dae5 | -3.8592 | -54.08039 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b52d8b2e-3406-355b-a3ba-926ad1f173e3 | -3.16383 | -54.60176 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6bd3313-fca4-3744-a309-30965a164941 | -3.84091 | -55.9046 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb4bc3d-95a0-38ad-b22e-f5c47f7eb1ea | -1.14077 | -54.09746 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 610a8a3b-7665-33a4-8370-57a13ccc183f | 1.01079 | -60.1116 | 2026-09-26 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cebcd5c8-37e2-3a75-b909-ea7b787480ed | 1.60702 | -55.84728 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1045d9dc-e826-36ba-b528-56fff36f2efc | -1.14196 | -54.08987 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c812d94e-e607-35aa-92b7-1d48e7203d97 | -1.34633 | -55.47588 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f807a5b4-77b6-3762-b9d2-aba3cff9ae71 | -4.48614 | -56.0869 | 2026-09-26 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 842e3512-a590-3ee0-8a72-e412c28a1b99 | -3.33945 | -53.54319 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c48dcf-1356-3c17-8714-f04e6d4290d3 | -3.49854 | -50.7383 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0ab435-c411-3db5-8e98-dfe45167bb08 | -5.06675 | -56.07178 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 736a8847-dc2d-3eef-827e-090bbcff4460 | -1.90471 | -52.08666 | 2026-09-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd79bb60-2488-3b96-bd18-93e01585e5e2 | -2.66951 | -56.46071 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b963c188-35bb-3362-a410-3c9dcdb6fb3b | -2.71956 | -57.53302 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee5808f-32a6-362d-b68d-aba973f7d721 | 1.6097 | -55.86439 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb64710a-3f80-3f7b-9830-b2dc5a31a5bd | -3.98765 | -48.4325 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea0f380e-343b-34d4-a3e8-7829f7347f6c | -2.83897 | -51.36155 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 868cf58c-2734-34e1-a3e5-ebe23f8c4054 | -1.4854 | -55.84939 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae474949-1074-343a-9f20-1c26408ad044 | -3.72984 | -49.03801 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc8ad748-af64-39f1-b168-0bcbda4cf598 | -4.46275 | -47.92192 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7398ed97-ff82-3f74-86f5-54467095092c | -2.71108 | -59.76682 | 2026-09-26 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee4c8f73-a982-3860-afbb-50d38548fdb3 | -2.90365 | -54.09815 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 91e4fc62-5c59-33b9-832e-66461f113815 | -1.14734 | -54.09376 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c13237-0e71-32a6-af28-ec7ad51499b6 | -3.20559 | -53.41287 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b45cabb-d9ba-39f2-8cee-baf0a22a7419 | -3.0408 | -54.69482 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a79c502-2108-3650-bba7-2131cb0dfdb3 | -3.30796 | -54.69279 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13091c6f-8dc9-358f-84b4-eed71a8f0685 | -2.72288 | -57.53353 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d8829b-bc07-35ea-af9d-8ea1e5cca2b7 | -2.60359 | -57.97045 | 2026-09-26 05:10:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9024bea2-b222-3cdb-8cdd-d3b3b5b09f6a | 1.60863 | -55.85754 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f4d32bd-40c3-3eb4-859d-8347fd65fe3f | -3.07096 | -54.40417 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a338724-53b2-3c80-9f0f-c816242588ab | -5.06784 | -56.06471 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b1979d2-2c6d-34de-96b2-86aa161e852a | -5.77905 | -45.10131 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c32a99e-859b-3091-9325-5385088b7aef | -3.98294 | -48.42873 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6944d4f-9371-3092-bcab-b6d327411efb | -2.1541 | -51.97699 | 2026-09-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51be535b-0c21-3e54-8651-5e04c771119a | -3.27433 | -50.14452 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c1002f9-1464-34da-bc7b-be6a025e20fe | -3.3051 | -54.6885 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 834a6f46-3383-3303-b376-29be5e96a58a | -3.83648 | -55.91112 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a1f4ebc-2e0e-3be9-afcb-49d70ef3c5f6 | -3.04138 | -54.69107 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ea789b7-f799-3bf1-819a-614325e6d8f1 | -3.44627 | -50.08814 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171de414-ac6a-335d-bf3e-a112eda39002 | -2.97375 | -51.04562 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc54ecd6-2b52-3cdc-a399-d1a51d8eddad | -3.84036 | -55.90812 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0898d09f-e581-3139-add3-0cfac65a6ec9 | -3.26982 | -50.1438 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f3440354-f731-3a16-9b3b-2e1ba1612927 | -1.1433 | -54.09703 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef0c4fe5-aa95-3230-bc8c-2f214b3f0ae3 | -2.99669 | -50.47372 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9dee62a-759a-340e-bc23-3445f6caeadb | -2.99735 | -50.46942 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 096d1ad2-bdea-31f1-bcf1-62835ffb05f5 | -3.30854 | -54.68905 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28d43261-7698-3dba-8ca8-13cabd1dba95 | -5.07064 | -56.06876 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 565d1580-4c88-3b53-91f9-c6d693910866 | -1.84013 | -54.7233 | 2026-09-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e3d6a4ad-e8e5-3065-a6c1-5ced9afc5ccc | -5.7744 | -45.09055 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b1e6924-4292-3181-bd2e-4608e94e2c47 | 1.59014 | -56.06374 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4b359e4-b3a9-354e-a449-fe0ee14eb151 | -5.77835 | -45.10667 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa992bcc-824d-323e-9840-ac84a62a7828 | -4.30207 | -49.13029 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa79e60f-c552-32f1-ba4e-2bd208a73bb4 | -2.41421 | -57.89394 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 118fcc35-8caa-3adf-b3de-93ff0d672ec7 | -3.71736 | -54.65221 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd28aa73-731c-334a-9daa-a8b0bb42c546 | -4.11489 | -51.08035 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f67bb33-00e7-35a7-89ae-18e774456ea3 | -2.97499 | -54.14922 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5120b182-41c6-30de-88cd-431c7eadfb68 | -3.23387 | -54.33012 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9ee085-6b57-304d-a977-5980c24c8eac | -1.15138 | -54.09048 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d239acd0-5dbb-34f8-86bf-2d92e980e0d8 | -2.46823 | -50.3624 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28e7bc06-8ef3-3d38-b57b-8b12e938b6d2 | -3.20992 | -53.40912 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5176e72e-9ae6-30dd-b683-07bc0cbc6f43 | -4.97645 | -56.19174 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b36c3c60-4a94-3514-9222-f5fcf314494f | -2.4131 | -57.90101 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 879e2cf8-8441-3f2a-9946-9a2a6e0ecd6b | -3.20594 | -53.41108 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
