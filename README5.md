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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68207b5c-b13d-3de8-a283-af9712d19a1f | 3.31096 | -60.52832 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 390ba45d-f5cd-3fc8-bd3c-b72b7145d7d1 | 4.04321 | -60.66728 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1fb4d2e-eff9-3428-a628-d08f8b3202ba | 3.61152 | -60.39431 | 2025-01-10 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acb66cf4-1a3c-3216-81ec-70f0627c5136 | 3.16415 | -60.63563 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1926c0b0-135e-3434-a1c5-3510a8908743 | 2.62426 | -61.44987 | 2025-01-10 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf217628-8bf4-35eb-8a81-4e7392944b88 | 4.02346 | -60.61964 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e328e2e3-791e-37ae-8355-cf4a0dcf5b02 | 4.04264 | -60.66343 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15604a24-bca8-3a9d-ac28-3f28974a3186 | 3.48061 | -60.16415 | 2025-01-10 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd15563-c700-3bdd-a54f-b4c75a0f9eb7 | 4.13524 | -61.0265 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b648030b-a69a-3847-bff4-6a305318892a | 2.57269 | -60.69026 | 2025-01-10 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7332f779-5070-3eec-bd0b-a0947cc1d68e | 4.66087 | -60.16719 | 2025-01-10 05:08:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3472740-9de5-37eb-9522-8e7166a22251 | 4.849 | -60.53085 | 2025-01-10 05:08:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314bd7b0-bfcd-340c-b686-28836e5aeb17 | 3.30852 | -60.53983 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8975b52-36ef-3864-9433-4717d72aa332 | 2.55987 | -60.68841 | 2025-01-10 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e73530-f77a-370b-b4de-819a91a34649 | 3.71279 | -60.26507 | 2025-01-10 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c68c254d-e37b-34eb-989e-dcb1b69cdf0d | 3.71333 | -60.26864 | 2025-01-10 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8a2e9de-d6ad-3e03-bdd6-0d1a914dfb8a | 4.13951 | -61.02586 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 89ea1128-606f-3dcf-8b77-27c9f98ac471 | 4.16155 | -60.67793 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d758ac9c-3971-3783-8c0d-7fe2403baf42 | 3.61504 | -60.39011 | 2025-01-10 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a2ed81-c410-3e57-8f43-ce837809d506 | 3.30388 | -60.53679 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d8ea6a81-f6cf-3250-9b35-acceffe37541 | 4.13891 | -61.02181 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4dc7e5cf-6483-39d3-8217-6e621bf949e8 | 2.43752 | -60.6511 | 2025-01-10 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57705a09-263c-3323-a8b5-8b7b6f862396 | 4.13343 | -61.01437 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb1fefd1-8d7f-39e3-b114-8ebb9f7b3f64 | 4.13584 | -61.03055 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21267226-02d4-3506-b1c4-b4a07bedd33d | 4.15849 | -60.6862 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b0517a-af3f-3cbf-9f81-c7809f46d1f7 | 4.16267 | -60.68557 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d117e132-d39c-306c-ba00-1ff66316d02d | 4.16211 | -60.68176 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d02973ef-3b15-3898-9260-f8b401bdb93e | 4.14012 | -61.02992 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c53068d0-c280-3999-9567-d1531aa1bc4a | 3.30443 | -60.54043 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a9a38d9-afb2-3dbe-b176-f329c992db1b | 2.5686 | -60.69086 | 2025-01-10 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f4eefe1-13a7-3d27-a6bf-7921b1cbaeeb | 1.80249 | -61.20992 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d989cd4-f04d-360f-bc36-1a86016d016f | -2.75169 | -54.69532 | 2025-01-10 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13b2e4a0-ce48-3cc9-b811-fb404f91fb06 | 1.30873 | -60.41216 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05c47a55-fc00-3749-8e2e-8e347c586260 | 0.78541 | -60.10334 | 2025-01-10 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c38643b3-171a-353a-9597-558f2906a422 | 1.93448 | -60.40836 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 58dc5ab6-d910-3f0b-bbc6-301b74806439 | 1.34704 | -60.03128 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b767f0e3-c588-348b-9fe5-c5b9906d8706 | 0.61308 | -60.61668 | 2025-01-10 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47f728c0-c754-3a1f-bb49-0b4da7a14efa | 1.34318 | -60.03182 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c1a844a-5318-3c0c-895b-cd3bd482d2d0 | 1.92654 | -60.40963 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97b1f563-9c9b-360c-8752-de0b0011a58b | -3.72759 | -53.77482 | 2025-01-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04cbb42d-8a27-3bf7-9efa-721356d50b07 | 1.94455 | -60.86288 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a9af309-3d56-3b89-bf24-d0c2a6948c20 | 1.94865 | -60.86226 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c631148e-a84e-341d-911f-3b10bba311da | -3.73244 | -53.76708 | 2025-01-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a48a413c-be0f-3465-b0cb-d13f1a0474ba | -2.87435 | -54.16863 | 2025-01-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58da43cb-d15d-3f3e-b492-6cb4fc2da38a | -3.10003 | -54.59911 | 2025-01-10 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 039944b9-ba62-3d86-bf03-ad227a1d9e4b | -2.87376 | -54.17253 | 2025-01-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb7e186-39a6-396e-9f4d-33fb0e1b7065 | -2.79771 | -54.16943 | 2025-01-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8a8111f-4276-30bf-a6ba-d5c696fa414e | 1.94511 | -60.86654 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0da75182-dbba-3633-83f3-5420580c9c8a | 1.93051 | -60.40902 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7bd596ca-0ed3-332a-8b80-bc259739950f | 1.93103 | -60.41242 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5585b8e5-266f-324c-b5fb-ae8efd7db685 | 1.38419 | -60.79758 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1180b71-471b-3811-87d1-337b3ed6aff5 | 0.97862 | -60.38234 | 2025-01-10 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d5e4f53-a51e-3220-9e2f-d3d858c0ec85 | 0.78447 | -60.10595 | 2025-01-10 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49871834-c8eb-3395-9aa9-cc3e338872ec | 1.93 | -60.40562 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 06f00143-81fe-35c9-a5ad-b480710e59d5 | 0.61782 | -60.62115 | 2025-01-10 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52c2e6e3-4468-3650-85fc-9948e6aeeb38 | 0.61387 | -60.62174 | 2025-01-10 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fc11399-cdc8-36b5-9215-b71cf0643b67 | 1.30796 | -60.40715 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18f76431-9c76-3eee-8610-6b2a6a62fea9 | 1.935 | -60.41179 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3e789c41-adcf-3aba-8f98-aa1a8d7c45b8 | 1.92705 | -60.41304 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca5d442e-c13b-37f7-969f-f22547411936 | -2.8187 | -54.71646 | 2025-01-10 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee416c7c-e0f6-3ee1-a484-090b2dcfd61b | 1.17563 | -60.38308 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76a28005-89b9-3176-9cbe-af2d6d81e6a6 | 1.944 | -60.85924 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80f4f1a9-43b6-3a88-8c4b-94f8af57965c | 0.97939 | -60.38736 | 2025-01-10 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11274de0-819d-3a6c-b11d-084965156285 | 1.92439 | -60.41375 | 2025-01-10 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b603404-9d20-3186-b079-8a0524d1d699 | 1.94046 | -60.86351 | 2025-01-10 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1220f241-e006-3768-af01-8eb7ed22451c | -2.66431 | -54.83229 | 2025-01-10 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73d9c3e-232f-3eb6-a007-dfc642bca3e8 | -2.66487 | -54.82864 | 2025-01-10 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f09e4b-7b90-34c5-aef7-41120982f6f2 | -2.85208 | -54.00268 | 2025-01-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 796b1cd4-a312-3185-878f-b655e2d52be2 | -7.73499 | -55.19807 | 2025-01-10 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86ff0b48-0d80-3cce-aebb-055a4968540b | -17.6616 | -54.17007 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11b1d3f0-6b2a-3f9d-a254-27c6e2c58396 | -17.31653 | -53.72326 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca5ac0a7-9174-3689-a439-119efc8c7cff | -20.30347 | -55.69282 | 2025-01-10 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bbfbccc-381e-3ecc-87b4-c13d1acef38b | -18.60767 | -55.49697 | 2025-01-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bfec4ed9-1f49-3ab3-b812-bf831ad25c8a | -17.66529 | -54.17464 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a7a1623-2234-3c33-93a8-b94a67fd82d4 | -17.65739 | -54.16949 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b574cc36-58f9-38dc-8863-52d087ae9843 | -17.65268 | -54.17292 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d033745-ae81-3acf-ba34-3f991073ba9f | -18.21738 | -54.13381 | 2025-01-10 05:14:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a6f89cd-b0c7-3321-b084-ba236517bcb0 | -17.65791 | -54.16545 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc3152bf-8a43-305f-9e52-4b0b4b007e69 | -19.15878 | -54.83608 | 2025-01-10 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79dd74f0-5b34-3125-bc31-e72255fd3312 | -19.32108 | -54.96078 | 2025-01-10 05:14:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c508f00-8009-34bd-ab39-e04ac2fdea45 | -17.31601 | -53.72758 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 858ac9c1-fe8c-3a0a-b4ba-72ed2cbf546f | -17.65688 | -54.17353 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fdb127c-034f-35a7-9086-077fb902aa30 | -17.66108 | -54.1741 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 395c65fd-910a-3492-9086-2259fcbc1fb2 | -17.31981 | -53.73236 | 2025-01-10 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e66080b0-9314-31a0-95b0-81917c95b520 | -21.30474 | -52.06548 | 2025-01-10 05:16:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10acc45a-d5b8-3218-995b-eba4437aa3ad | -21.5669 | -54.20049 | 2025-01-10 05:16:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db5c21a0-233d-32b1-ac8c-033d123e05cd | -20.9779 | -49.77592 | 2025-01-10 05:16:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 71690dac-6d20-338e-b9c0-c8a506b64b47 | -22.60099 | -54.88718 | 2025-01-10 05:16:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| db8b9d69-2abb-37dc-b8db-2970b845eb24 | -22.49008 | -55.71807 | 2025-01-10 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f4e5129-e119-3bab-aee9-e5e60fa04374 | -21.30442 | -52.06865 | 2025-01-10 05:16:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6513e369-d756-3a2b-bdce-d1b4bf243225 | -20.98335 | -49.78095 | 2025-01-10 05:16:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b45adc5f-584e-3fa3-831d-d78a67202eef | -23.35497 | -48.53461 | 2025-01-10 05:16:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87da8432-5070-30c9-b6e7-3e6dd6ab8f84 | -21.31146 | -56.02757 | 2025-01-10 05:16:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 781cb4ff-c1e5-3035-a584-6cf4f1e9400d | -21.30507 | -52.0623 | 2025-01-10 05:16:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50c71c94-d104-3de0-bae5-1112392896de | -21.56196 | -54.20447 | 2025-01-10 05:16:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1579282a-d263-3364-8ce1-44a81a0e7f95 | -23.35538 | -48.52869 | 2025-01-10 05:16:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d819b8f9-854d-3d98-ac3e-ee2f1a9690ae | -23.10564 | -52.0992 | 2025-01-10 05:16:00 | NOAA-21 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4d4e1672-3b35-3646-bb07-57f4697a3c27 | -20.98373 | -49.77667 | 2025-01-10 05:16:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 927d6039-7e97-3cb1-8b34-018f2b7d3b5d | -21.20275 | -56.91495 | 2025-01-10 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce5b92c3-adbd-3537-8e73-df141a044d3a | -23.35423 | -48.52997 | 2025-01-10 05:16:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README6.md)
