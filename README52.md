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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91ff97e0-3983-3b66-81fc-a0c4542ccad5 | -3.02546 | -53.87448 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdf1c71e-4f99-3580-b4d6-7c3cbd1e89eb | -5.74441 | -45.16244 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ff9cb20-dc08-3553-b9a3-26e80c8f4dbb | -6.01254 | -49.56464 | 2026-10-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 29be25f2-332c-3876-b922-f4f2ad25e077 | -4.2998 | -50.77178 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 350f3afe-92c7-3cb2-8e3c-b1d2d42cdcdd | -6.9268 | -44.56132 | 2026-10-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a60c2c58-0141-3cb4-a8f6-183b0812e584 | -4.2584 | -50.77559 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 475de4f9-230e-34e3-92af-f38f0be92501 | -1.90258 | -45.80821 | 2026-10-01 04:32:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfd8824b-77b0-3917-b958-65ed573c4a3b | -3.43728 | -50.66397 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d7e1a76-aa54-3cb0-b174-9f798cbbb890 | -3.10713 | -51.27143 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91a33cdd-c9d6-3d4c-b5bb-83c1cb9c7ef0 | -3.95674 | -48.13103 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52259380-b4af-3b6b-a65f-0c5e05554835 | -3.20336 | -50.91875 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb5ede6-6faa-33f9-a5f2-0721fd2abb9e | -3.95694 | -49.04727 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e1e996f-caf7-316b-9eb3-f693487bd8db | -2.35523 | -45.86943 | 2026-10-01 04:32:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f070e67-cd1d-3004-a57b-84a61e8ee822 | -3.79986 | -50.61241 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c295ae4d-05de-372c-8421-d874144eb055 | -3.69095 | -47.12474 | 2026-10-01 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4516dbd-c3de-3e4c-844e-b72d623920fc | -4.28562 | -50.75904 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7b9402f5-95c2-308e-947b-e5cfb5c2e27b | -4.88897 | -48.37201 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 16e124b5-fc9e-34c9-a768-591960fc7d50 | -4.03829 | -54.23564 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 525ef1bc-9c15-36d9-b1b1-af470857ab64 | -3.3733 | -50.95003 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84bc889b-cd40-3109-aae2-b348d1c3f343 | -4.25801 | -50.7632 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2f918b28-4a2a-35c5-b45b-528e0308358d | -6.23115 | -47.4514 | 2026-10-01 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5a55c46-26ef-3e92-a5bb-4362af231941 | -4.25563 | -50.74358 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b54f1591-ca90-3662-a136-4befcc541592 | -3.24919 | -50.81599 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cdb7d04d-0e43-32e2-9a01-ec323a11a55d | -6.1917 | -44.85699 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a73cfd31-1c44-34b9-b908-8ff18a1f1211 | -2.96763 | -51.03472 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c424ec6c-a371-3434-964e-07f695545903 | -4.27343 | -50.78325 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| ab51941c-be79-3605-a10c-9a510ded63f8 | -3.00381 | -50.47241 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7ce0594-0c88-30b7-bf69-08abb2a1a473 | -2.57815 | -50.78936 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cab73115-e89c-3e76-9499-d43bb495fbc6 | -3.1059 | -50.28434 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abefbb50-d111-39c0-9b27-ad11a62564d2 | -3.1051 | -50.28928 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 771a9205-ea2e-3990-8710-cb8510954892 | -2.36059 | -50.35143 | 2026-10-01 04:32:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d84f6ae-07e4-32eb-8848-807bd6ce12da | -4.27061 | -50.75135 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6b74227b-aaa6-3642-a9b9-c15fabe85a77 | -1.8128 | -57.10844 | 2026-10-01 04:32:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebfccb4-3aa6-3e02-8603-d845b8250528 | -4.26745 | -50.78054 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4dc82882-8bf5-3eca-9466-f8f1ab3796fe | -5.65736 | -51.36625 | 2026-10-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ddff757-f7ae-3eff-84ed-d8c3822ee632 | -1.32269 | -49.12922 | 2026-10-01 04:32:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3c02267-628d-36c1-829b-e6fe81f08ae7 | -3.11293 | -50.29058 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05110122-7793-39a6-97e5-234240e94b14 | -2.90377 | -54.14454 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88694114-f035-365c-af73-edcc872ea070 | -2.9025 | -54.089 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0fd43de-c0cc-34b4-8109-865ea9736902 | -2.89916 | -54.14068 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40632bdd-209f-33d4-929c-7dc96ec64877 | -2.50019 | -56.91416 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32124d1c-ba33-326f-8aa8-3995b14d8d48 | -3.16794 | -54.09404 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fa017a23-7fd2-3b4d-a38e-10e52ae1d976 | -4.01427 | -50.4566 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74ddbdf-fb1a-3f06-9a32-ee494e5a30b7 | -2.98059 | -51.03302 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45bae479-6235-3fb6-b82a-f593af688062 | -1.78806 | -47.94146 | 2026-10-01 04:32:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9a883e-4b6f-377c-bcac-a429a384d048 | -3.4797 | -54.73044 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4a3059e-ab5a-3fdf-a7c5-11c8cc47f9a1 | -3.00198 | -50.47392 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4ee6f65-f118-30ce-87d5-b395133a77d3 | -2.97767 | -51.025 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 377a0406-40c7-3327-8970-a7d4af3635de | -7.39546 | -42.66168 | 2026-10-01 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 381bf09b-454d-374b-8377-7ac052244246 | 1.78995 | -55.65815 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f785ef6f-b1cb-34be-8573-5615de1c996a | -4.2732 | -50.73593 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad178566-55e4-3e23-87a9-d784698e4374 | -1.42841 | -46.7993 | 2026-10-01 04:32:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7509b7-81a5-3fc2-992c-34662ca73547 | -7.32041 | -42.07642 | 2026-10-01 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5fdcaa0b-8b40-3d5b-8e1e-5cb90772b1e4 | -4.63121 | -50.61599 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b329e07e-eca1-3b8d-adde-1c5d02062496 | -2.89407 | -54.13983 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73c90c1a-14ab-39c4-b830-6057632426d1 | -5.74886 | -45.15586 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a78b74fe-193a-3aa0-9b6f-ab86e088429c | -1.4422 | -54.46014 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d40c928-4b5a-3d2f-8c2b-c1ca29df6767 | -4.12936 | -46.87152 | 2026-10-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30324426-9326-38b9-bc1d-ad9baabe1bf1 | -4.26444 | -50.74851 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 79a67fea-49a1-3d45-ad5f-962966e493df | -4.03881 | -54.23259 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2ef3693-b1d3-3864-aecd-816f6166e7ee | -2.501 | -56.90943 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df5759eb-08c2-3fa4-bec5-02d63b68837d | -1.95772 | -50.631 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aadcc6c3-8fa7-38e9-b75f-56c6ad91a5b1 | -2.89742 | -54.08811 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de2f0521-174c-39f0-9775-4b353cffa626 | -2.05399 | -56.87243 | 2026-10-01 04:32:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8416870-065f-33b2-b060-b781b73be036 | -3.97343 | -41.51684 | 2026-10-01 04:32:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0ffac36-c0a7-3b3e-8b68-5f2606e51847 | -4.31796 | -50.78522 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8af0fca-b76b-3a48-8a35-dc7dc1c78491 | -4.39028 | -54.82487 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a1448a4-685c-3603-9843-74d9c417c61a | -3.12003 | -50.27139 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5550f711-d0aa-344b-b008-077853734610 | -3.52567 | -49.26101 | 2026-10-01 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94b8b810-0fe0-3b17-b687-5cfc9abb90a4 | -6.85346 | -45.58106 | 2026-10-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85e050e8-0dc5-3e1a-83fc-898db02e75b1 | -3.13945 | -53.74644 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| efaa22d4-9305-3579-93cd-e3b8ad093ea5 | -4.53523 | -50.78354 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c946614c-7da9-3410-bc9f-10dff9133fc2 | -2.36538 | -50.34692 | 2026-10-01 04:32:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e46ae28c-ac29-34d0-9df0-86a71247b6d1 | -3.47829 | -49.92207 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 064ae0b9-67b5-3de4-8072-0bb16a42eec1 | -5.7567 | -45.17156 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce8feb3f-e9d7-3499-92f1-8f1dc9b3fd18 | -3.3739 | -50.94641 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f76d958f-5908-3501-954a-b8aa9a21fe7b | -3.23006 | -54.31786 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1e1066f-b791-3157-9063-18ad4ff968de | -4.2669 | -50.73317 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f93763e8-f687-3e27-b924-03f4ed92a5c3 | -4.27256 | -50.78845 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bd131536-6876-36bb-828a-f504b3bff09b | -4.04327 | -54.23683 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19438890-b017-32f1-8a3c-9769be4b8477 | -6.18832 | -44.85645 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4bb2e8e-e782-3d82-9447-5ca46b72a9a6 | -4.94971 | -49.41802 | 2026-10-01 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96009d7d-a3ae-3863-9b3c-1f0fce312df9 | -3.82276 | -50.6215 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 407ea021-4cf2-300d-87ec-4030e8c39394 | -4.27686 | -50.76272 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 665f9ea2-d937-3adf-ac9e-c9be8ee377a3 | -5.22144 | -46.02658 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d48723e-7dc6-3b4c-a92a-19b1dc59be33 | -4.38064 | -49.73815 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc31b465-5a02-3596-9259-ffae5451062b | -4.28166 | -50.75836 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e131333b-e9be-3767-a915-855d58bfaba2 | -5.36375 | -46.22263 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5511a7fb-b582-37bd-b8ec-c2d6dd059e00 | -3.80576 | -51.03421 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13676fb3-1943-37c2-bfb4-1950cbcd38c1 | -4.24461 | -50.74533 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f41730fb-2162-3099-a111-340db45527ad | -3.54763 | -51.54255 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b0e6e9d-accb-3c01-b728-d45a40641c7f | -3.00403 | -53.87969 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bb32b6-404f-3860-9f7d-711239a9f586 | -2.91009 | -51.30806 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d3b465e-1343-3b03-b053-beb8ec8cb37d | -1.90204 | -45.81165 | 2026-10-01 04:32:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17674ef5-232d-35a2-a011-09a7ec13ce5d | -2.37835 | -50.40619 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282213ac-e70e-349c-926c-91cc7ff3375d | -3.5755 | -54.32666 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705cf83b-873a-3503-9bb7-bbd7eac58ceb | -3.09265 | -50.26695 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eee9f9e4-25d2-3249-9bbb-f5b8c8988505 | -2.89867 | -54.14369 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 482b5965-87d6-3216-bd8a-e59d12b3cac5 | -4.30233 | -50.75647 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7a7d706-2bdf-3448-bfd7-24e1c3a37efe | -2.0532 | -56.87707 | 2026-10-01 04:32:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
