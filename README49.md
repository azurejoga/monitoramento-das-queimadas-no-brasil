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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea24744-6cb9-319e-92a1-f9e82caa2811 | -2.24402 | -53.6205 | 2025-11-17 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b13a454-4293-3097-9185-983d6c406291 | -3.18642 | -50.65625 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14c1f20b-7b57-38ca-b1e4-3c196ba0b014 | -3.29857 | -50.08059 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69416f5d-48e7-35e2-aeb4-9d33f30627da | -3.79618 | -51.09641 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb69fe2d-0088-3698-8f54-f75b9601bd3e | 0.7627 | -59.54023 | 2025-11-17 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| becb66a2-6d4a-3b56-8865-71dcd70c666d | -2.43191 | -52.12559 | 2025-11-17 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16c21b3b-67d5-3a91-bf0f-a8aebc19fe7d | -2.5105 | -47.82392 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bcd6db60-88b8-3a08-870d-1637fb8f995d | -2.47772 | -50.2389 | 2025-11-17 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 317aea07-a546-38fa-a7f8-c8b6fce5c3d6 | -3.3579 | -50.1835 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0aacab0f-37f5-33ac-8862-62139ee74586 | -2.47167 | -50.23798 | 2025-11-17 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d8bbdd0-3aff-39c5-86e8-71b06f27a42a | -3.46152 | -50.11996 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30a3dba3-6ca1-3780-aee5-96edc92287ff | -3.1871 | -50.65178 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e6cca21b-2412-3bf6-b2d7-03b14e3d41b3 | -3.75461 | -50.43036 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87e3c89f-779a-365c-938c-1c7f888be577 | -3.51265 | -54.37193 | 2025-11-17 05:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d041008-c90c-3c56-837c-02f0799fae98 | -4.17368 | -54.5933 | 2025-11-17 05:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cfd7cf9-7a0d-3c2e-aacb-16314dd9c05b | -2.5845 | -51.83329 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9934638-2adb-3f1e-bece-a70e41a15dda | -3.22873 | -50.51182 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a864c7f-3a86-366e-a1ef-56af46accc5a | -3.40102 | -50.18859 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d59f5a0-9c83-334d-b80a-445ad04eeb4b | -10.66042 | -49.37242 | 2025-11-17 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9e5f437f-d030-3794-9267-c1e98054d350 | -4.39298 | -49.65981 | 2025-11-17 05:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 228b4bbf-24c4-378a-96a5-17210f321cc4 | -9.85424 | -59.96458 | 2025-11-17 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 024018c8-3bb3-3375-8e89-ea94f43cac7b | -3.50732 | -54.37584 | 2025-11-17 05:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9af7cc62-5362-34fb-808e-19fe7494f2cf | -2.93975 | -51.76051 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8521f3fc-5ca9-3987-a3ba-698b1f66e7fb | -2.24882 | -53.62123 | 2025-11-17 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4424449-a103-3104-ab22-905119a9d615 | -2.58592 | -51.82977 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf7c275-5d5e-3c76-851b-bf9c05e6476f | -5.12871 | -55.9753 | 2025-11-17 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b98df1-0c15-343d-b85e-187f7b746189 | -2.35055 | -57.13465 | 2025-11-17 05:29:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ade2b010-8d54-3137-9779-55f64846e9e9 | -3.40034 | -50.19326 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f86d8e31-d187-3581-9fe7-2397897e9c21 | -3.23451 | -50.50079 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd976ad0-be18-316d-b29a-620002bd6329 | -4.01363 | -48.8137 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 225d60c1-b06f-3fe8-9782-323b9e93f995 | -1.30195 | -55.71514 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a84abb7-b76e-3219-852d-7b728a0e06f1 | -3.23913 | -50.51075 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b907350-ab22-3ff7-b69b-aadc2eecdfec | -1.93913 | -56.82317 | 2025-11-17 05:29:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371f0ad1-365c-3af8-bad7-34d302411382 | -3.74887 | -51.81555 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73df32a8-f1f0-37a4-bf05-c87dd3e4b236 | -2.51749 | -47.8251 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 61c4ae68-6c66-3a0d-a8c8-7bae2c350f38 | -3.24054 | -50.50159 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1f3726d-a594-347a-a8b6-427d4fb74729 | -3.65216 | -50.2284 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d5e694a-6326-337b-8479-21faf0bd249d | -1.97838 | -51.99803 | 2025-11-17 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a301755-8905-3459-8179-729ba9be5f7b | -2.50452 | -47.81602 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12bd0695-d260-3056-bf67-c9b700b17a54 | -2.67232 | -51.88618 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9833e9d5-33c9-3468-8aa9-3e6fbc2d6051 | -3.35733 | -50.18663 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7ef5dc5-ac64-3a92-9e8a-5e19905ee9d3 | -3.38353 | -50.13867 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d9b450a-0642-314d-83e5-93c7dbd68f84 | -1.62762 | -55.70843 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f7e9a33-1eee-314a-971f-010b1ba915d0 | -3.23983 | -50.50622 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9445aada-e029-3246-8638-591fde164779 | -2.51148 | -47.81742 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3a88cb9b-443a-3da1-8ca3-34ccd2936c85 | -4.01692 | -48.81017 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c649525d-0927-31df-8115-abd601e6a312 | -3.39545 | -50.18461 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6466b1e7-f6a1-3ce1-9199-d857dec0310d | -3.01205 | -51.3472 | 2025-11-17 05:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1464ed9f-d03c-3bd1-a567-2d62729376bc | -4.09789 | -48.03165 | 2025-11-17 05:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5eb411c7-a312-3e10-bdde-5fbbad6ab6d2 | -1.19353 | -55.82204 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb7fce03-eebc-3b3a-97ab-9abff3a1c857 | -3.29788 | -50.07775 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eb74878-d199-3cb1-9adc-fa9c3379485c | -4.09338 | -48.03019 | 2025-11-17 05:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d20fed5f-6ee4-3e49-ab4d-75a35348edb3 | -2.89263 | -53.28827 | 2025-11-17 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d05b8988-86e9-3330-aa21-1b335d9bbc36 | -2.89177 | -53.2939 | 2025-11-17 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af9a3907-214d-3757-81e0-d86b9672ba78 | -3.00695 | -51.34246 | 2025-11-17 05:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06764558-7fee-3fdb-8afc-8a3aa19c4aba | -3.35718 | -50.18835 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e43f404-65c1-33fd-8aea-933b49c78a55 | -1.05669 | -57.40514 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73e26e29-64c2-36ef-9b78-5c79ab6b6d97 | -3.30476 | -50.08144 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f01b5f-9cdc-3f72-9ee4-17092890bb98 | -3.22917 | -50.49548 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f931d8c0-ac5e-3cbe-af7b-46e7fcca3203 | -3.22938 | -50.5073 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e44c25a7-c8d9-3f73-b09d-d50fc9febeb3 | -3.0835 | -51.2585 | 2025-11-17 05:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f41692-622d-3b2a-80e1-ba9d1f1d3d42 | -4.55014 | -48.47689 | 2025-11-17 05:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 804cb389-eed9-34b4-b530-a8c6e6c9a602 | -3.30541 | -53.85292 | 2025-11-17 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5926845-643e-3e73-b7bc-dec25478f607 | -3.14772 | -50.20766 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26435eca-4c1a-3ede-8f7b-206cd01dd848 | -2.94473 | -51.76574 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 773b2a6b-d5fe-31bf-9582-dc82f31c6a43 | -3.38426 | -50.13386 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406e41db-a162-3687-9b8b-64afea5c8658 | -9.48808 | -59.46004 | 2025-11-17 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f2bd972-b307-3521-8dd2-bf6162a3f2cd | -1.97787 | -52.00139 | 2025-11-17 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eccd06a-62ea-3413-b73b-5df58ef38cca | -2.43243 | -52.12225 | 2025-11-17 05:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b12a5fbf-f209-32d0-89ed-e41bfff73c38 | -5.12314 | -56.0428 | 2025-11-17 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 642a4cbe-3712-3b45-bb04-c060e1b5c22c | -2.58997 | -51.83408 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee1a48b-16a9-3bd0-b410-b7d1972e0602 | -2.47099 | -50.24253 | 2025-11-17 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad19336f-ae3d-33e3-9ef3-c55570bcef8d | -4.54949 | -48.47699 | 2025-11-17 05:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 791602be-a465-31ed-a153-c6b2bd984d38 | -5.12562 | -55.96661 | 2025-11-17 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4931293c-41e1-38ed-b10d-b9cacbb2d19f | -9.57894 | -49.12199 | 2025-11-17 05:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d9cd2f0-9809-3a3d-8cdf-e0793aacd02a | -4.01016 | -48.80927 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f7d0d07-8204-379f-abce-07dad7ba467b | -4.01453 | -48.80766 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce724098-54c1-3cf6-bb02-acd1cca6f6f9 | -1.52785 | -55.5173 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b295067-05b4-368e-ae5a-885a7a2a1901 | -3.80207 | -51.09692 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf5ab4c0-bf2d-3026-8335-911eb94c3682 | -3.75343 | -50.43149 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09c61c32-4e31-3e65-97ed-022aff5c1884 | -3.2421 | -50.50436 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98ae8ccc-e7d6-3e49-87cb-b6dfcf6aad05 | -3.5998 | -55.54086 | 2025-11-17 05:29:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1380db7e-ef35-3b03-81b2-851ed8a71b49 | -3.83542 | -49.81287 | 2025-11-17 05:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0b52f0f2-0a85-32cb-901b-fbbe57ed4a5e | -2.50352 | -47.82271 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4e0d8b0-c5c4-31da-a9a0-415fa0d98e08 | -9.57617 | -49.11786 | 2025-11-17 05:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e679b86-1a84-3917-b436-23f755412aa7 | -10.664 | -49.38077 | 2025-11-17 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce090116-55df-3f77-a78c-530577d4c768 | -3.23608 | -50.50352 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1412f22-4a77-37cf-82d0-db651eda5890 | -2.75865 | -48.42467 | 2025-11-17 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 805fffbe-92e8-3253-820f-b80b8fbd2de9 | -3.18047 | -50.6554 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d55bee8-8660-3be9-b6db-97b5085a6fb8 | -2.88853 | -53.28191 | 2025-11-17 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c32f0101-0e2d-31e1-b521-8ea46d5eae4e | -3.51497 | -57.78975 | 2025-11-17 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f408929b-4b2f-356b-ad4f-1f5b8fc54ccd | -3.33089 | -50.28039 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3336779a-b328-3690-a3cd-3a5bfcf8226b | -10.91258 | -49.41817 | 2025-11-17 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5e514d4-ca46-34a4-83aa-eb1cd7821bfd | -3.30548 | -50.07673 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3a91438-ab5d-3e4c-abb3-56186878cc3d | -3.75409 | -50.42708 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c591ac7-4c11-3144-965d-1a5cdf57313d | -2.59088 | -51.83409 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfeb1c8b-61e4-3e02-ad38-4afa71d6c719 | -3.30406 | -50.07867 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 401def4c-7201-3c1d-ab53-61058d6f92c4 | -10.65962 | -49.37919 | 2025-11-17 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 20b9c696-41f0-30f2-bcc0-6bac2edce207 | -3.41072 | -50.12188 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a81d6c3-1b23-3ce2-94c4-6e5918ef246f | -2.8935 | -53.28264 | 2025-11-17 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README50.md)
