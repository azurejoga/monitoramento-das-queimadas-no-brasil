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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 374d7bef-cf55-36e3-86ba-d6e99c930e26 | -3.2768 | -53.8199 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e9c4eb5c-2fab-3bfc-b81e-b98e4bd922d7 | -4.2575 | -46.1188 | 2024-11-21 03:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8ec9c961-0591-3410-8f30-baf8105c1c26 | -2.0259 | -54.5289 | 2024-11-21 03:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 0e40e929-29e9-3cef-8041-6e16c707b7f2 | -4.2388 | -46.1197 | 2024-11-21 03:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 798e181d-335e-3424-99ee-b98831e79980 | -3.2952 | -53.8194 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b537b406-5e18-3519-959a-98efcd659478 | -3.2766 | -53.8602 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 3f286ef4-5b8e-38b3-a3b1-028629398eff | -3.2951 | -53.8395 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1a23be64-3604-39f2-998e-74bcfac45a45 | -4.2575 | -46.1188 | 2024-11-21 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| e9041ae6-6dcd-306f-8f31-d57cf553135e | -3.2767 | -53.84 | 2024-11-21 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9e843a61-ee4a-3a69-bd13-35b7109b6fa7 | -9.9731 | -36.0634 | 2024-11-21 04:00:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| fedee656-8b3a-39b2-b9f3-e5fe40be216e | -2.7676 | -52.1045 | 2024-11-21 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 0e63960e-5c15-3aa7-b169-03b75521ed07 | -3.295 | -53.8597 | 2024-11-21 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| a7e56b9d-6337-3894-8f7f-165b878b0e23 | -4.58 | -48.0132 | 2024-11-21 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6d11d2c6-84be-3646-8903-e7b642b72c79 | -4.5799 | -48.0349 | 2024-11-21 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a7eb512f-a393-3139-b160-96ef57f5e17f | -2.0259 | -54.5289 | 2024-11-21 04:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 88547588-f522-3650-ae01-f3ce2290a524 | -3.2768 | -53.8199 | 2024-11-21 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6410a8c6-6d85-3ea3-8d9d-6bad101f5cbd | -4.2388 | -46.1197 | 2024-11-21 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 5048fe10-a8d5-39c1-9566-92c7b57fe4ae | -3.2951 | -53.8395 | 2024-11-21 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 672f70ee-879e-38f4-b397-3400770d4221 | -3.2952 | -53.8194 | 2024-11-21 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 489297c2-2b27-3384-ace9-d987f7e5748f | -2.17963 | -52.12605 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f3fed54-186e-353d-896a-a8c0a9663895 | -4.49213 | -47.11096 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09df0a0d-7f35-3341-81e4-0c7c090c0897 | -0.88515 | -51.72392 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddc763bb-7a67-3f8f-9c6e-e20833d4e782 | -3.42562 | -49.2379 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1519f62-bd3b-34b0-8a92-4229a5357173 | -6.93839 | -41.20146 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0759f7b3-964d-3aa0-8a53-e7e3ab6b632d | -3.37812 | -52.45334 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9315b365-dc57-3b88-a7cf-19468c29c541 | -2.91788 | -46.83788 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4ce8d1f-9c34-313a-8dbe-6494c4e1cfdb | -2.24644 | -48.16395 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 289e9954-94ae-3656-bf65-13bd2e9e625a | -6.16619 | -42.07553 | 2024-11-21 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70feb731-33ee-3e74-84b5-fbb54fb6ff15 | -4.82072 | -45.75679 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b4ab8d7-261c-3ead-a90c-a9a321f81e45 | -4.72546 | -44.42822 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0789fe13-a481-3d18-9caa-4e085ec89e2d | -1.44844 | -47.11976 | 2024-11-21 04:08:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d7825f-97db-3d99-b345-3c5cd7d2a70a | -3.64658 | -52.35967 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbafa6d0-d9d6-3b06-bfa7-2dd0f9c12e9c | -6.12467 | -42.5142 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 48848788-3567-3d77-9ff6-3dd6ec82ae53 | -3.80814 | -52.37094 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33d52475-f9da-3b2a-b49d-d83ebeb7a70b | -3.64082 | -50.21555 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee1d8a68-b3b1-3609-ac52-ddb7cc777a94 | -3.30146 | -50.36511 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b8eebfe1-affb-320c-945f-f39383a6cbb2 | -3.27509 | -53.83516 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8de0417-3156-3137-b81d-5ecf63c0dc08 | -2.02201 | -51.17492 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e3903b-6ef7-3d1d-b86d-e6a42db68aba | -6.61511 | -42.381 | 2024-11-21 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f298f25f-323f-3f41-b780-e6ac49298c0f | -2.84446 | -46.67756 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37a885d-9ba6-3c67-a496-86582e6f579c | -6.06628 | -44.14965 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07b17651-ab9c-35bb-80a8-ec1f4b1caf4b | -2.63092 | -48.06524 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 260ade8c-4da4-3364-9783-8b5411b71722 | -3.06995 | -51.36764 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e8c4f6-46d5-376f-9cc3-ddd023e87b90 | -5.49804 | -43.95528 | 2024-11-21 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d834e3a-eb63-391d-9f33-8a3d05bcd2f8 | -4.6276 | -45.57217 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83b002aa-f102-3c80-bde4-f48594da6f7e | -4.15778 | -42.02131 | 2024-11-21 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 4469cf2f-6c70-3d3e-b69c-7ec63f35db36 | -2.6812 | -46.2441 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f79479-5054-3a3f-a800-3b5cb0bf1a4f | -4.53333 | -48.45987 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d64bf93-797a-3608-b2ea-1329987f9b3b | -3.41755 | -49.22491 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27f1e9fc-7ee5-33e1-b9d6-08bbd6d1f334 | -3.34552 | -51.64405 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1f8da5-8981-31aa-aee4-035e10fe4a64 | -1.18743 | -53.72392 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 01c0352e-a56e-38ad-a6e3-311e00a8eb9c | -5.86593 | -39.94958 | 2024-11-21 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb6cf9dd-7ba8-3dc4-9194-131dd5ed0e08 | -4.1611 | -42.02183 | 2024-11-21 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| a909eab3-5677-36f7-b3f5-8391e9e81684 | -1.40954 | -52.10563 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 910a4a37-4d8b-38e2-b347-dffbee1b391f | -3.64552 | -51.45641 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 621702ed-0c64-37bc-8c61-28ddcf711e0c | -5.72335 | -43.51004 | 2024-11-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2983759f-0564-39fd-95ce-d6d9b2374350 | -4.06864 | -46.83285 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94babca7-5c5b-309b-890d-b74891a70b34 | -3.81211 | -52.34735 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c474a1d6-6aa3-3ed0-baca-65586cc722a5 | -3.4703 | -50.00666 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f4bb1e3d-36ac-338f-9013-584195c4087d | -3.39763 | -50.25187 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25dc10da-6b7d-3cfc-b59b-11d3852fc9a4 | -4.48865 | -44.75389 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5772ea26-412a-3c6f-961a-9e16262383fe | -3.19938 | -54.32888 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70c37cb0-50c2-38c7-8a1a-f4a77b338e06 | -1.60149 | -46.86708 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 509455b0-b08f-3fd7-9fa1-6699a5a2cc31 | -1.79295 | -47.19667 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 249d36e2-ba40-385d-88f9-88847f34cb5c | -1.23522 | -47.35541 | 2024-11-21 04:08:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7f24562-85cc-3859-8383-67e7f070e923 | -5.07604 | -47.94117 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b35077d-3e6e-39d7-a747-3aa2a6302ecf | -2.38656 | -48.92617 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72ba1a82-7884-3839-959c-a8973068f237 | -1.74909 | -52.06279 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde30df9-fa2d-3b78-a1bc-72f9a768d049 | -0.41942 | -51.56531 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd39a0ec-40c2-3e28-8a48-63b81e129bb9 | -3.04317 | -49.46507 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec5825d0-9105-39da-9aba-32068fa7bc34 | -5.62469 | -43.95495 | 2024-11-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddec6203-81cf-3ddd-a044-7126bfa974b0 | -2.6369 | -46.21081 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45412e8f-a8f6-339c-b25a-f74ed19f418d | -3.30382 | -50.36875 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5524c04f-7c45-3d01-a22c-c86f067d334d | -4.38891 | -47.77774 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7030cb40-ca33-3ae6-a881-89a7e41c7289 | -4.15832 | -42.01783 | 2024-11-21 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7f68bc7b-7be1-33da-ad22-070f29cfcb9f | -3.49508 | -50.44777 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bbab8ae4-20f3-300d-9b6c-5e84344280c3 | -2.5881 | -51.71659 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b325bae-cad1-33b7-9329-517109e4fe67 | -1.26797 | -51.6104 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0fe22d55-93b7-39d1-a8c3-2739812b1bec | -4.47326 | -42.9574 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 648597ba-1874-3f1e-9c85-f2777a68b366 | -5.70925 | -39.06385 | 2024-11-21 04:08:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76cdb69b-71a3-3f24-bb82-7e021785e458 | -4.29949 | -50.14479 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5e152d1-a7a6-3fdb-aeea-50d989a978f8 | -2.15073 | -53.77613 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dcd400c8-55a6-3627-a693-01f156301c80 | -3.81037 | -51.26646 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e618f846-f68a-35bd-934a-15c7584a1824 | -3.48743 | -51.47521 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd697ce3-5eeb-3357-acb2-61156f860c5b | -4.24581 | -46.10378 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 077b0a24-ffec-3071-a435-20f9b0b510f5 | -2.93079 | -48.334 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3f0a193-d503-37ed-b242-049f281f193a | -4.81688 | -45.75602 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a086e36-d730-32c6-89ab-e5a8ae702c0e | -3.77576 | -50.70452 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce52310-a5ec-3115-a94f-9387d7b8dafc | -3.5384 | -50.53384 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 574e27a1-4379-31d8-ac50-b5892208d5f1 | -3.51119 | -53.80088 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2c6174-b44d-327e-8a6b-82555d6f54e9 | -4.39615 | -45.59561 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4500ebf0-cb2d-3d30-98fb-8f12ae1fb3e0 | -2.67777 | -46.16491 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c991cbeb-3d19-332f-b90c-a9b8fd704495 | -5.55618 | -46.18906 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 144d5f22-927f-3fe1-8a05-5150e400e18d | -0.07107 | -51.50196 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69859404-9512-35f7-ad69-8e7c810848d5 | -1.99014 | -53.14207 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a458c644-cb4b-36d2-94a6-43fc4b984b47 | -3.9296 | -51.1796 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f97bf53b-e7ed-3875-8e01-ef8ec29b7709 | -2.67342 | -48.28776 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b424c225-a4e5-3cb2-835a-10c3e73aaf5b | -5.71691 | -44.81036 | 2024-11-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 91e9e24d-b880-3e05-875a-467b3f70b36d | -1.89803 | -53.33167 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a60a5f8b-ed4f-310b-bcfd-b51170d721ea | -1.04543 | -51.74405 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README12.md)
