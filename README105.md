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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d5a3a87-6f73-316b-ab0c-bd495515f03f | -1.7236 | -52.46404 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e367848f-e01c-3f61-9501-2877a14622ef | -3.3456 | -49.93909 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3093279-d23e-36a7-994d-c1fe91211bd8 | -2.40537 | -50.30695 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8da75e0-3973-30d2-878c-c8bb62dc1814 | -3.24016 | -53.39756 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e7d123-f5f8-35bb-a532-6b893f0a65fb | -4.07801 | -54.97432 | 2024-11-09 05:20:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a1146d8-cfa6-3eb1-8d26-1faf3fdd6374 | -3.35684 | -53.39276 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b61e0fe7-efdc-344a-8a01-9653556fc57a | -2.98233 | -50.30322 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4485490e-1c1f-30f3-9656-05f456df2a79 | -3.03328 | -53.27 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b213d66d-4c66-3efb-ae3d-192e74687a4e | -1.5191 | -52.17374 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ecd6645-4249-3d1a-bab2-034d85251953 | -4.11654 | -48.50422 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d5ece57-5d05-3508-8b95-dc0b36610a20 | -2.8375 | -52.90791 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63966456-551d-3d40-bd5b-4db38ff8952b | -2.57796 | -49.13941 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e72c883-c631-3183-99c5-f9ddf358b72e | -3.70785 | -53.75239 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba5dd8b7-3736-3370-9f1c-820d02831e73 | -3.17543 | -51.31618 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 834a2d2a-1a0f-3ccb-b05b-886455e958a4 | -1.51365 | -52.17798 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3021d22b-2b2d-372c-bda5-c97589457565 | -2.87137 | -50.33015 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30f54b8a-2073-3eb4-b4d4-90354c62808b | -3.53039 | -50.33276 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d966d2-3885-3c71-b9e5-8c3f70c71984 | 0.62512 | -60.09351 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9acfa0-42e6-3f72-9c95-806200dbf8bf | -3.02951 | -50.36096 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 268d1e4f-5450-3eed-b6d7-b74a6c333fe2 | -2.29203 | -48.55823 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1dc7071-74a6-3ce5-9f50-58ee98c9f205 | -3.63035 | -50.18632 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1551679e-c4b7-37cc-a68d-852b38c13dd2 | -2.81091 | -52.96047 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8751943-1077-3cc8-a80f-2373e222416a | -3.11925 | -50.1404 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db87e87e-51c3-3f5b-a907-b452df69c520 | -3.08357 | -50.5677 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35f94d7f-15ce-34ab-935a-434a1dcaa292 | -3.33652 | -50.07981 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14892d94-6520-3a67-a917-2c10085f0936 | -3.83736 | -50.03418 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1948ab46-68c7-3293-82b5-f7eb23ddc783 | -2.30487 | -53.81785 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 922ad82c-7788-30a8-a419-45e4f600bc21 | -3.70721 | -53.7566 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 070f972e-703f-32fc-b174-d8e7777f8931 | -3.08692 | -51.22403 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f9ab34b-4984-3162-b29f-41a3cb8ecf43 | -3.83254 | -50.04588 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd9a3ae2-a00f-3fc5-9c8a-6785e3cf53e2 | -2.69198 | -51.70539 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd46d933-b706-33ea-8307-9e5d7f1cb1c1 | -2.36282 | -52.69986 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53e73bf4-97b2-3d75-9205-6a0431fbdc59 | -1.55618 | -52.27533 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4af75aee-42f8-3701-9cbd-cc97de3a3411 | -1.18619 | -53.66805 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c1bb6d4-c1c2-362f-bf2c-1732a0f02378 | -1.33056 | -54.60051 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 610e25b4-775e-3ffd-9cf8-6b19e5bb3db0 | -3.64096 | -50.19159 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b178567-05b2-3b33-a54c-f8f90ab15efa | -2.86644 | -50.32579 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d92f257-924d-3c98-8250-51ea68b7769e | -3.17031 | -51.31545 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7d22667-c332-30d5-b838-30490c81174b | -3.01747 | -51.043 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d70c0c4-59c0-344f-911e-69166a67d6ad | -2.60212 | -48.19407 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4918a0a-d54b-3469-b3ee-89812e951460 | -3.23625 | -50.26267 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5439546-8ae5-305f-b2b0-623379abcacf | -3.24792 | -53.40085 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beefdcc4-78ec-31a7-9fee-2fa260d08674 | -3.08306 | -50.57107 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bdabd7b-a26d-3698-85b7-001f1c14a859 | -3.03829 | -50.37653 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19e1a5c1-a98e-3a51-8675-e86b04373295 | -3.02587 | -51.23101 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f4cc5a5-c37f-364f-880c-2d600eb6de04 | -3.04223 | -50.3598 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4110ba7a-54a8-344b-bfbb-927ec53f8b03 | -3.36193 | -53.38903 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ce7e7b6-8c45-3e3a-ad81-7ac70711032a | -2.22477 | -46.55045 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7d021a-0747-333d-8111-58b3a4f9f59b | -3.6541 | -50.76191 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 008a7c56-87d2-31bf-8081-14c63e84923b | -4.06879 | -50.01292 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39ad8bbd-3a34-3617-bd53-99c337ffe929 | -2.5841 | -51.92453 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f81f90c-7b26-3b25-a122-7fafd13865a0 | -1.4172 | -54.76855 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48eca37c-7e1b-348a-96ee-2b41db312be6 | -2.57735 | -49.14358 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| afd2101f-3d95-3c2a-ba9f-ed4246a50fd3 | -3.21706 | -50.39111 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30f5c314-12ca-35d2-9d13-55a2dd97b1e6 | -3.07671 | -50.57677 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce7e9d4c-5cd9-32dc-8f53-2545a2ac02c1 | -3.17215 | -53.85378 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66ff4608-d07f-3302-99e8-ebb98c6d160c | -2.21924 | -53.73331 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e186b265-a58c-3e38-b4b4-9978cd38fd84 | -3.15111 | -51.1239 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf58618-78d7-3c21-8fee-b030d8bbcc3c | -3.04666 | -50.36763 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e861e9-3c56-353a-bf1a-e13a52558bdf | -3.08257 | -50.57436 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e9b139c-9135-3e45-87ba-540e08f67761 | -2.99643 | -49.23838 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8c1ee0bb-2e68-319f-b4ca-71557b26a4df | -1.40734 | -54.55187 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f36d65f9-5790-3ea4-a042-924d8193a32d | -2.61536 | -51.74511 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36fb39c9-9a41-376c-ab58-6fddad4418b2 | -3.39967 | -51.5985 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b7b2cf-a12b-3d32-b88a-6ace9fba8c91 | -3.09282 | -51.11392 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30d226ea-48f8-388a-bb03-53ac4abd8928 | -3.65406 | -50.14081 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac706ea5-1837-346a-b53b-2e11dad88752 | -3.0398 | -50.32993 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b15f088-ea9d-32b3-8ec5-fdfb44ddc463 | -2.81375 | -51.81043 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26c51e88-bcaa-3466-8f57-2293949871cb | -3.3014 | -50.08612 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f0867d-1251-3bc6-aad5-909dbbe7b68b | -2.97155 | -53.86839 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08bae6d1-2208-3132-af52-f0159daef717 | -2.97791 | -50.29528 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e355b69-2129-3917-9bf7-fab53a2d17de | -1.14468 | -53.65716 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a86c0e00-c6ba-3a14-885d-e2a3e8b2daae | -2.18719 | -53.62949 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd7805fb-6b56-3282-ab2d-8c3e80c68f97 | -2.39888 | -50.31308 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6faa8fac-a113-3ecd-87c6-47211a586598 | -4.40058 | -50.97332 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ad6ce6b-c13f-315c-a297-33d07ce9dea5 | -1.45936 | -52.56472 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fed8b763-0c80-3521-a112-23ccc12f870e | -3.50139 | -51.1463 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a58c21b-62e5-3b9b-b63e-60f8fc6bcb22 | 0.61854 | -60.09121 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1011316f-05ae-360a-ae14-b2888ac1d017 | -1.15678 | -52.00832 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 715eb74b-def9-3409-8b48-84f80dd83cc6 | -3.05347 | -51.34265 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f785fdd-1352-3d5f-95ea-0fbce9ef1894 | -3.29453 | -53.11597 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f67aba94-5825-3ebf-964a-86a5e13d8ff6 | -3.04121 | -50.36683 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f2a498b-aac3-35d2-882a-d0ba09fc3baf | -2.88543 | -51.74881 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a352069c-641a-3b73-9a77-65239189d665 | -3.15516 | -54.47979 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4e6f713-b7bb-3c0e-82b1-bdb334332c47 | -4.72701 | -48.96389 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f7b67bc-b78c-32bd-91f3-4609ca95dd0f | 1.32141 | -50.73399 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb46d5c-3710-37ce-b363-0478a246529a | -3.97113 | -48.17284 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b3cfb083-1d71-3cc0-b4aa-c6d0cfe7d583 | -2.96631 | -49.28577 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfc35be0-5f68-3d3e-b259-e07109c3af30 | -3.58853 | -50.24054 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3902f2e-ea61-3572-b147-0ea8dc2d8290 | -1.14911 | -53.65588 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e538a882-3999-3195-865c-ac93c7557d9d | -2.46195 | -53.69363 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 655a8f31-6878-3641-8a46-d183b310e7c4 | -1.5144 | -52.17301 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51a9dea8-3d4b-3e03-bfcf-e68490410c12 | -1.68992 | -51.92033 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a6958a9-463e-39aa-af79-c7ac32f3ea06 | -4.20922 | -48.68857 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f496a5e4-4df9-3b9c-b620-b28cc534aeb0 | -1.46718 | -55.65229 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbcc439b-7a9b-3d04-86a1-ba265d4a1010 | -4.49448 | -48.49637 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46ed4f8e-e9c8-387e-a707-800fc879e4d2 | -3.40355 | -50.01352 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f56638e1-bd23-34eb-b0de-f75b77a9ab7b | -3.51099 | -51.67266 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f73165d-f846-3538-bd26-fbbf0003bb2c | -1.15363 | -51.99754 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f32bc1a7-1b16-3dcf-b9bc-787cc47b7476 | -3.09349 | -53.32454 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README106.md)
