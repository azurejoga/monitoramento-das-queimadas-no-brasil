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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ba3e752-2f0b-345a-90ee-2cca945e8b5d | -3.98001 | -41.52796 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e6060cef-d728-30d5-81c3-7289bf61f5e8 | -5.8776 | -42.32835 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9f7a9b90-95fd-3d10-9a25-c63f4ae86abe | -0.9627 | -51.64804 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 368538f0-4626-3822-a3ba-e4c8a1c5722b | -4.04141 | -46.85584 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc43817c-cdee-37f9-a38a-19de779302a8 | -2.67321 | -49.86865 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc97cd8f-b25a-32b4-ac35-9ccc2bffac84 | -3.25451 | -53.64178 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1aee845-a2fa-3bd5-aff1-a29edbc815ee | -3.93574 | -46.50018 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95493a5a-2c38-36b3-8cb5-f73a58587351 | -1.95155 | -53.33779 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6372140-73ce-37ff-a074-cb448e8848ba | -6.81982 | -46.77418 | 2024-11-30 04:40:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7e18d75-6e6d-3c3d-aebd-800ffffc5ef4 | -1.00726 | -51.72642 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e783a184-d8eb-3f9c-a998-ef084817fe10 | -1.05752 | -52.41617 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30cbd0f0-e69b-3916-874c-80dea7f4ad55 | -2.28767 | -50.52611 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7822ac54-0eeb-32fc-b94b-ddfb5bdc323c | -2.45943 | -55.27681 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fa48736-2b18-33dd-86b3-4d2d8965223d | -2.86032 | -53.99848 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68295459-0f9d-38da-881d-f6283c6e9ab5 | -2.06342 | -51.19107 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f69399a8-16e8-35ce-810c-3cf7843d3b7b | -1.06914 | -53.22137 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 45a052ea-30f5-3f90-a09c-9bb69d53c84d | -2.95752 | -50.57354 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 961bd045-fc64-3623-9e2d-89fb75b8f14d | -2.3918 | -48.55823 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c3a52e-80c3-3131-91d7-381d0d898891 | -2.82845 | -46.85347 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 985f7f69-9692-3fdd-8879-4b7ae56b5203 | -2.73426 | -54.13666 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b6118cd-bf1d-3c51-98a7-42f3a4e81337 | -2.66302 | -46.1317 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68b35d7b-e856-3c5d-8995-f672e16a6314 | -3.13306 | -51.0415 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f490820d-bc40-36f4-9d03-4a2ae2601345 | -2.82869 | -54.09275 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d57f6311-d846-35c0-91d1-2e68683b7e75 | -4.11318 | -48.53381 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db794d0-a8ee-34a0-b8b1-21b0f0d34786 | -3.95192 | -46.72934 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 045da678-dcfa-3446-bce1-613b48c09947 | -3.05434 | -53.28323 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78ff6cbe-e971-352c-8a59-264e0f4e2127 | -3.11745 | -53.27106 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da4c5e99-7500-369d-b9a0-96dff96927a2 | -2.88474 | -53.98036 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bda03646-34b5-35bf-bd8e-198462c45d78 | -2.38171 | -47.88077 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8815735-0071-3f3b-9334-53f8ae1d9aec | -2.83747 | -54.11643 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21de1b98-3edb-3f91-8479-434038393379 | -3.16282 | -49.02402 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d07d38f-6703-3508-85ae-73bcec0ae15d | -3.82423 | -46.90104 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 809bdf46-83dc-3dd8-b4b4-691bf45ce672 | -3.94302 | -46.90389 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8937541b-f79a-3db7-8c14-493844af84e2 | -3.86545 | -46.34493 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bf8685-1d54-3c82-834a-c3dae54232bf | -1.97571 | -52.89653 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aea1c2a2-fd69-355a-9d78-d0b091fa5c1b | -3.12411 | -45.98416 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82f15e9-5ec6-31f6-8115-84e8a004c9eb | -2.92872 | -48.01509 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbfd0bac-78d3-3aff-987a-351a58e129bf | -2.70593 | -46.30186 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 548a3bd9-a6f3-366b-9c0e-6ad34c8a5e05 | -1.66785 | -52.05457 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98ccb515-1da5-3bfe-98a9-3622ad1f8879 | -2.01756 | -51.20056 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b56b53-3c0b-39f4-9c8a-7b5b5268ff14 | -1.36541 | -46.89631 | 2024-11-30 04:40:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec30476b-47d9-3686-becd-2368b7990bcb | -2.9817 | -48.72453 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f9a0d7a-4561-3557-9ab6-1ea650d36ccc | -2.43148 | -48.17285 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c0bcf79-72c2-3d0e-9f8a-d9d84bb969ba | -2.24929 | -48.42715 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 796b1ca9-49cc-3ad4-b8ee-46627eb176bb | -3.34331 | -50.23989 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b49803-664d-3504-a0f3-eeb964308d3b | -2.80745 | -48.61955 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27f073fd-9810-39fb-8ec4-3badf6df62a7 | -3.27061 | -46.44421 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c448684f-248c-3724-974d-87a4ebf57604 | -2.92892 | -49.43108 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eae8438-4a37-39ae-87d5-8f65dbf6125b | -3.38718 | -50.11277 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b7a4533-04e8-3618-852a-6b7d6210813a | -3.94416 | -46.91954 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744072c1-8835-301c-a0ac-7093f9ccad6a | -3.09259 | -53.72235 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8a7211b-2138-39c8-a813-022394c238df | -1.10846 | -48.36803 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e6cf50-20fa-3f0c-96ed-579f687830c4 | -3.1983 | -48.57902 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6df75f19-691c-3d33-bed9-a1402316d4fc | -2.6619 | -48.7904 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2de8e521-706b-3f6d-bae8-c10e9cd17921 | -4.20394 | -50.68898 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f50213eb-3192-3b53-b6e8-17162117e119 | -3.94654 | -49.9496 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3d2a676-54ae-31f6-a4e1-644cb8933b76 | -2.01619 | -48.06587 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da53a8fe-60e4-3a8d-9a21-e54a253eaa89 | -2.4482 | -46.5196 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7223774-6f1a-3a45-8355-f9caa2923cd7 | -1.79422 | -46.62237 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b35dd1c8-4eca-3306-8f04-cb6930912bda | -3.60986 | -49.99325 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b00b996d-295c-3e05-b710-6cdc51deee3b | -3.45719 | -54.5645 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e211e557-07da-330e-aa16-151f66ef971a | -2.58154 | -49.99804 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b617a52-9334-3084-8ae2-6a246afa2bcc | -3.05735 | -48.52134 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaffa128-5f01-3c0a-b160-abd657588a9b | -2.91707 | -53.07011 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4de5fc7-a84f-3221-8d87-849a00b76e38 | -3.13149 | -53.68189 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39259028-3db2-3426-8209-5bd78dc25c88 | -1.37608 | -53.64848 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 10231103-79ef-39f0-a8bf-ffee39e15300 | -1.14791 | -48.33195 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5439c383-eec0-388e-8a0a-08dbe831c915 | -3.82662 | -46.54883 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93d7235a-0bf5-3270-9815-171bc501678c | -3.29728 | -43.54164 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5acc53bf-badc-37c7-9786-4e11a63081a2 | -4.11936 | -46.87077 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 994ed6b7-4b56-31b1-bf97-907506cac1f9 | -3.89465 | -46.67359 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6d4bf74-e3d7-3df8-84d6-907961a22c78 | -2.97015 | -48.03264 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6905aa72-73bd-304c-b7a8-e9e6dd5b61a3 | -2.44589 | -46.51147 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987a4def-b349-3be1-b353-eead7166ed78 | -1.49871 | -51.93911 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79ee6bde-06cf-3e7f-91fa-2b241b3dfdeb | -2.96961 | -48.03613 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13849f65-562f-39f6-9fbb-0626e88a2650 | -3.04841 | -48.49173 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c07dbed-90a5-3fbd-9aa1-0c38ea45aea6 | -1.93471 | -53.44367 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6df00232-374b-339b-8bad-f89b59c2ee09 | -1.58107 | -53.75087 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 754abc5a-27a1-3384-93a8-fa566d211b65 | -2.24586 | -50.48229 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf1b0ed1-cbcf-30b7-81dd-0b903e964595 | -4.89702 | -45.87664 | 2024-11-30 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23484ca0-9a50-33e2-91ee-dbba245e1059 | -3.10903 | -54.0385 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17465680-a276-3d8c-b20c-a26a8ce9be1b | -4.16969 | -48.63108 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e4efdd1-42e4-3747-b3aa-78ac836c9538 | -3.19867 | -51.42187 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 838928d9-5fe1-3528-a34b-1dc8b77c70be | -1.84817 | -47.65853 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e87cd25d-8997-3888-8e7b-87a2e669ee3f | -2.81044 | -50.32154 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4095d40-5dd1-3811-a05f-ef6d830037bb | -6.91132 | -43.54339 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e4ae439a-3781-3c82-ac95-d87055706f4a | -2.87035 | -48.1059 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cae23e4-5ac8-3279-8679-7cc4f23c3599 | -2.5715 | -49.99649 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 442545cf-d90e-3687-b4eb-dd30ed63c5df | -3.1551 | -53.83158 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a65dcee1-edc6-3e33-a53f-6aff137a2e80 | -3.2947 | -50.24326 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02a413f7-0603-3146-86f8-5e0920974089 | -1.73184 | -52.49878 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a18530e6-1fdb-3d77-8767-8e39f196684b | -3.04381 | -49.37115 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd49045d-e94c-3a96-902d-97ce944e9c2f | -2.9356 | -48.60469 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b803910c-4323-3936-a8cf-d6f00c4c028e | -3.49023 | -54.02789 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7115bd2c-1fec-3242-9820-b6b61d58498e | -4.04297 | -48.26297 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a85f0222-651a-348b-bc20-87add3e0544d | -3.86512 | -46.3476 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c9f093-67c6-304c-bcfd-66f5d919008c | -2.59952 | -53.98592 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c02d0efc-e490-305f-8bf1-bb3f4453f983 | -3.14543 | -53.84068 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0cdb214c-e8b8-3a63-be04-3ecfe6039ead | -1.69654 | -52.47217 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23ff8c01-345c-344b-8d0f-bfe82d181613 | -3.10498 | -48.58865 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
