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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58d2d782-953e-3da2-8346-db48a4d5c9f0 | -4.36574 | -48.50639 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c149ac36-2435-39d7-b4d4-0c01ceb0596d | -4.001 | -49.95851 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239c33db-823f-384f-ab8c-55030a47938a | -3.1143 | -53.24889 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58adab2a-34b6-30c4-bde3-358c32480d11 | -4.0037 | -47.92025 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8b8e64e-03c6-383e-a795-ae5814559eb2 | -5.18923 | -46.14243 | 2024-11-27 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c3589f-c218-3fcd-b5d9-89e1e10891bb | -5.43008 | -48.48219 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b709866-fb34-3df2-a8b7-a071315e43c7 | -1.30959 | -51.73921 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 045e2cd6-97c1-341f-a7c7-79d0a7d590ed | -3.23971 | -53.63802 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46866c4c-2722-3d05-8a24-f50db1fe995d | -3.28289 | -53.83366 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a22f5846-8e75-308e-adc8-ff1cae198828 | -2.53146 | -47.33007 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 197c820c-a9c8-36ff-8ef9-b5b3ac8c4d2f | -4.1647 | -48.71753 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f34b3741-eef4-3ec9-bc2a-5897834ec7df | -3.83319 | -46.53722 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2710a417-53c2-35ed-8dd1-66b1ea80eb45 | -3.74185 | -50.39733 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48273f32-1815-343e-a71a-6995218f451b | -1.61105 | -52.27097 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7075c6b3-ce54-33c9-bd06-660669a01e43 | -2.81729 | -54.11951 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d5bee37-157c-306a-811b-292629c97c81 | -3.83764 | -46.5332 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f12e870-185e-30e3-a8bf-bb99f6f07ffc | -3.84747 | -51.38617 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6af3720-dd66-3409-bba1-6666cacd57cc | -3.50297 | -53.8167 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02eef80f-8cc8-3f5d-9128-47824920e22d | -3.73138 | -54.26791 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86e1f2a1-cb8c-310e-979a-5dbbcc012a59 | -1.66074 | -52.71088 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa4bcd17-520f-3869-bad6-9ba8f82c041c | -3.2887 | -51.1158 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 069e415b-12eb-3789-9f1c-f61984b1c8ae | -5.58699 | -43.15929 | 2024-11-27 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 849eb63d-44a2-35f9-afe0-bf4489e695d0 | -4.72708 | -49.50383 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86191bfd-35fe-3ef4-a3e5-675f8a86bcdd | -4.1953 | -48.40853 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4515770-9f4e-312e-9a96-b223168dd6d8 | -2.55997 | -51.23486 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70677126-2dd7-3689-9562-5c789c06b623 | -2.83599 | -46.8422 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4edbc35-f1f0-3566-954a-1a6057d7a4f5 | -3.2363 | -50.15613 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31c1e6ad-70f0-32e5-b4c3-3a91b8655a29 | -3.65953 | -50.74757 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 188a1b54-01a1-3a88-89ba-1393a74b20d2 | -3.29436 | -50.54203 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07bcd22c-0db4-3e2c-9ffd-d3a617781d2f | -1.6304 | -52.42063 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a439eda-9e1b-3d3e-991b-342312f7fa2b | -4.21827 | -50.88868 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0f9e0137-05a0-3c35-818b-b0c112f12805 | -3.23053 | -49.43333 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2eb1348-0be3-30b6-b614-9e3fc228d985 | -4.04981 | -46.85013 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 550dccad-f3b7-3874-9b2c-07251d91a909 | -2.94855 | -51.75586 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edc7b53f-278c-3bfc-b140-5c8de2516ee8 | -2.68792 | -45.65923 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3052f145-14f4-35e2-a08b-032add01608f | -3.28926 | -51.15523 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab2153ad-4756-3ea6-bce2-54f9be0b67c7 | -3.32709 | -50.05416 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060c1c86-1836-3ce1-b8ef-6440399e58d8 | -0.48212 | -48.6363 | 2024-11-27 04:42:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14892c2c-3388-353c-86e1-8bffabaf2c55 | -2.71096 | -46.25496 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bdca2dc-3fcd-3f95-84ae-8580e6ea565d | -1.28565 | -51.73546 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a1c6ea-77fa-3047-a7b6-032cf3e63801 | -4.1384 | -43.84762 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed6aff3f-fbdb-3f35-a043-21772193918f | -1.48576 | -52.53496 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9da9b723-5c57-3199-b706-494d4140bcaa | -3.78952 | -50.13701 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 715a744c-8572-304d-b97b-0e89aef7392a | -1.53061 | -52.22726 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155bb85b-48a1-3c67-8daa-faaa5057722d | -3.41838 | -50.4455 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 290d2ced-2aef-32e4-a1bf-40267fd24885 | -3.13045 | -49.22534 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5633525e-e65d-3903-9328-60edf277de54 | -4.30586 | -48.18907 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638541fb-1ddb-3b97-840c-04e08fdb3420 | -3.27935 | -48.75428 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d068064e-fc44-3a0a-a633-b439576ede51 | -3.32797 | -51.63856 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3ac3faed-5d85-30e0-9fc7-f353cb08fd56 | -2.59966 | -53.97395 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10affec9-5780-3cb9-8f55-630a1df6254a | -4.37374 | -48.5 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6301cc72-24fb-32f9-88c6-4671a2d989e6 | -2.00578 | -48.5377 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f23d0b1-95e8-3b07-a43b-2d6d7d512dd0 | -1.36768 | -52.54967 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d3acf8-33ff-38c2-b379-f04ba61901f8 | -3.31068 | -50.26637 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a66595b1-ccb8-3da2-9e06-c488edd66fee | -2.18416 | -53.78322 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 154db73d-8170-35dc-a8e2-dbae8ed69a81 | -2.18486 | -53.77874 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 64d55afb-4300-3d7f-920f-e5dc6658f158 | -1.07937 | -53.37747 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ff3061c-ba8c-320a-b752-655f55dda1b7 | -2.803 | -54.13601 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| adb31da3-621f-31bc-af52-ca0dbdd9b71d | -3.49381 | -53.31741 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d2be272-a5c1-352d-883c-e56287f63899 | -2.57375 | -49.09609 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e30a360e-b314-3e48-9697-62d6cc092fb1 | -3.25724 | -53.2771 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e8aa0b-60c3-39a5-abf2-e151fcff471d | -2.7765 | -52.868 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6784370-c870-3ead-8cfc-3e3cb8f3e0dd | -1.39602 | -53.5535 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86416fb-5f4c-39b8-ae8e-589ba0354d82 | -3.1249 | -49.22061 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9df8609-0aea-3f16-8d41-a8ed8a72bc37 | -3.19127 | -50.82979 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03123f81-21d3-31f5-87a3-d120d1a94594 | -2.59945 | -51.82852 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ae0812f-f4b6-36a2-89df-d84075f8bc9c | -3.07267 | -51.25742 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9adac5f8-039a-3b72-8e06-bae1f746d175 | -3.27496 | -50.01777 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd0ccd0c-3271-3f84-870f-df1568f6832b | -3.6866 | -50.23014 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8be7d98d-5e1a-32a9-a6d7-4d6f3e57d3e2 | -1.18897 | -51.77043 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92c03c1-25a1-35ff-b56c-2c91360d4fbe | -4.3361 | -48.65342 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dec4cd9-afd9-31ed-9029-250d6310522f | -2.01728 | -51.1866 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a72f6b3-c0ea-3c5c-9da7-99a3aa50ac44 | -1.76592 | -52.29393 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1efe3aa7-8fde-3b78-8177-8c3be4d382ae | -4.13908 | -43.84312 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e42c71e-142f-3fbb-adb2-25a644ce9d77 | -3.67962 | -50.87805 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69729486-27e9-3a1b-ae4f-9ca17d7bf284 | -3.03713 | -48.51358 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76162784-968d-369c-879f-76c6f6867fec | -1.22942 | -51.80264 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fb2347b-9e49-3196-9877-1fe9a62268c4 | -2.28562 | -47.91368 | 2024-11-27 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caf9c5a7-1713-3bbc-b5e8-db6906a111d9 | -4.21995 | -50.89955 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec07732-27d1-36a8-9408-d5f56f026c15 | -1.66145 | -52.52411 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| affe94f6-ecef-3b07-b5f0-a8aff431ae57 | -1.24053 | -51.62277 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ad02f94-ae5d-3433-a6cb-219c3871ded2 | -3.96681 | -48.092 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f7922d-6072-3641-bfa0-1ab59b82bed2 | -1.15898 | -53.67857 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ec845e-5497-383a-a3cd-862a6650738a | -3.38725 | -50.10226 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bfc45c9-68ba-3732-9032-9b9f1a4d7d51 | -1.64116 | -48.20197 | 2024-11-27 04:42:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 916202a5-7522-328e-8fdd-6ffac3136133 | -2.81809 | -54.75787 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 232751dd-6637-3cf1-b201-cc441416b2b4 | -1.22883 | -51.80635 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a85eccf3-7f72-3cee-a953-2ad119ecb434 | -3.36053 | -50.18614 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b6257a-12b4-3011-a2cd-6f1d6a4031b4 | -1.35648 | -51.43943 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6281489f-fedb-3dd0-be34-3db2ebe65346 | -2.42529 | -48.54649 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4946b9e-a2a7-3bec-9840-1ce5d29c7de9 | -3.89155 | -50.07215 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fa8c1d1-ed30-3e7a-b1ed-7f6033674ec7 | -5.20031 | -48.18097 | 2024-11-27 04:42:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52eaee41-d6a3-3e15-9fe4-66a1451febe1 | -3.7158 | -47.13103 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb284caa-6ed5-3e2e-b8dc-896f40427a4f | -2.81846 | -46.83522 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bd97664-85bb-3050-adb5-c7e5dea189f3 | -1.58334 | -51.26854 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3315dc5e-8cbd-3b7d-adef-f7ad56f986de | -3.78345 | -50.13254 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8425b94e-ee58-342b-ac69-d3c3ef9cca74 | -3.45155 | -50.29927 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 67e461d3-41d9-3d2f-939a-d4ac91db8f12 | -3.49915 | -50.49337 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0e89fbf2-0786-36a4-abd9-db766d152314 | 0.94668 | -50.74659 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5d982a5-d581-35ce-92c3-b3661847d5ee | -3.28498 | -41.77648 | 2024-11-27 04:42:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README69.md)
