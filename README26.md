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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7f1514c-e3cc-3960-b67a-db155f8168b2 | -10.5776 | -49.1316 | 2025-07-09 08:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f525482f-47b2-38ef-a65b-1fa920f07220 | -11.4397 | -45.0923 | 2025-07-09 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d3f241ec-bed7-31b1-b0e5-2baba4f90a57 | -8.5214 | -43.2828 | 2025-07-09 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 16861889-4f72-33e7-b1fb-0873b3196442 | -8.5025 | -43.285 | 2025-07-09 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| b63deefd-c20c-3823-b179-679a08db96ef | -8.5214 | -43.2828 | 2025-07-09 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| c2db3d13-f11d-3098-86a0-40b06b533ee5 | -8.5025 | -43.285 | 2025-07-09 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| e2b55de8-fc8d-3f8e-a919-cdb9b5bcf154 | -11.4397 | -45.0923 | 2025-07-09 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 15a9b566-1b2a-3ddd-a1f3-6c8f68b36623 | -10.5776 | -49.1316 | 2025-07-09 08:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 87d651d1-5859-3435-acdc-312752dae024 | -11.4393 | -45.1154 | 2025-07-09 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| ad1e517c-d50b-34ed-a2c5-49b9b871d582 | -8.5214 | -43.2828 | 2025-07-09 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| e2922344-2a72-3828-96ad-5927ea4a43c0 | -11.4393 | -45.1154 | 2025-07-09 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d72fc350-1db9-3808-99a1-b737f30d1088 | -8.5025 | -43.285 | 2025-07-09 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 6b49c163-deb3-37c9-acfd-2ade2e24da6a | -11.4393 | -45.1154 | 2025-07-09 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 76969920-c65b-306c-8ac3-19cff0cd25fd | -8.5214 | -43.2828 | 2025-07-09 08:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| da5ac26b-a56d-3626-95c7-af9bb6ea2b15 | -10.5776 | -49.1316 | 2025-07-09 08:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 31c0c9bd-ba11-325e-8f9d-2dd07a67fedf | -8.5025 | -43.285 | 2025-07-09 08:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| e4837702-218e-3f9c-9fc1-df63fd28c724 | -10.5776 | -49.1316 | 2025-07-09 08:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 326880b9-9e84-3f85-9ebf-506ce47acd6e | -11.4393 | -45.1154 | 2025-07-09 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 27e8bc23-9b9d-30f0-8d54-9c8bbcee9f1f | -10.5779 | -49.1098 | 2025-07-09 08:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 90b9e766-041a-348f-8df8-5adba1bb798f | -10.5776 | -49.1316 | 2025-07-09 08:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0f3b7311-8bef-390b-a372-1b9a1c657e7b | -8.5025 | -43.285 | 2025-07-09 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 8e17f847-6f8d-386a-810d-5a4079dcdbf9 | -8.5025 | -43.285 | 2025-07-09 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| a1a06483-8147-38aa-9ade-062f8a5e5b54 | -8.5025 | -43.285 | 2025-07-09 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.2 |
| 32015391-9f82-3b2a-b1b9-c571b66a678b | -8.5214 | -43.2828 | 2025-07-09 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 1f4e2a76-6c88-34e9-bef3-1fff14991db4 | -8.5028 | -43.2614 | 2025-07-09 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| f97497ea-1d11-3e5f-9a99-27949bcfe08b | -8.5214 | -43.2828 | 2025-07-09 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 8af658b4-a2ba-3daf-b637-a90c082e6847 | -8.5025 | -43.285 | 2025-07-09 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 237.3 |
| 299886dc-7150-3f77-abc5-79c330c1b779 | -8.5214 | -43.2828 | 2025-07-09 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| ec59057c-2caf-36ed-b096-6f368d6db9d4 | -8.5025 | -43.285 | 2025-07-09 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 230.3 |
| 6cba68ed-dc96-302b-bf05-620911ffbde1 | -8.5028 | -43.2614 | 2025-07-09 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 56ac4483-af19-3301-8eda-0ceb59e02498 | -8.5028 | -43.2614 | 2025-07-09 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 1fa7224b-4f2b-3c2b-a628-17b0bced7372 | -8.5025 | -43.285 | 2025-07-09 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 258.6 |
| e3bcd29a-dab3-3135-a105-98b65ff628a9 | -8.5214 | -43.2828 | 2025-07-09 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| af8d3a93-3dae-3a22-8e2d-05ed299c9f4e | -8.5025 | -43.285 | 2025-07-09 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 171.8 |
| 75b66adb-e2df-3bcc-a1d3-6f96071247bd | -8.5214 | -43.2828 | 2025-07-09 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 211.3 |
| 47727a45-70d4-30a0-b820-b1cf3c4b960c | -8.5028 | -43.2614 | 2025-07-09 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 115c2b42-fdef-3ac2-b62f-791c8d5a6b83 | -8.5025 | -43.285 | 2025-07-09 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 218.1 |
| 2b0c2b33-df63-3592-92dd-0e1cdfe2977c | -8.5214 | -43.2828 | 2025-07-09 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| a04336cd-ce90-3199-9226-c32a54002dd5 | -8.5214 | -43.2828 | 2025-07-09 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 824d13fa-8cf9-3b23-b452-d7976da6e558 | -8.5025 | -43.285 | 2025-07-09 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 217.2 |
| 7f6bd1dd-9da0-3e1b-a768-6c7392d1dc3a | -8.5025 | -43.285 | 2025-07-09 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 1182f84c-48cd-37df-9cf0-4f1dc15ea567 | -8.5214 | -43.2828 | 2025-07-09 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 20b77f08-fc8b-3f8e-a772-0fdb749e5bb8 | -8.5025 | -43.285 | 2025-07-09 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| d50699b4-3042-387d-b3ff-8514ca64d270 | -8.3802 | -43.9527 | 2025-07-09 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d3fcec97-ed3d-3b69-8b2d-331039aa3c45 | -8.5214 | -43.2828 | 2025-07-09 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 9ad72b29-c85e-328b-8efc-2c98a89b0885 | -8.5025 | -43.285 | 2025-07-09 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 693309b5-e984-3e20-ae20-6f6ab7f5e1e6 | -8.3802 | -43.9527 | 2025-07-09 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 815a1aab-2ec9-36ba-b763-86a6bd3c1e00 | -8.3802 | -43.9527 | 2025-07-09 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 65fc486e-5bd4-3862-97ab-b2d249cc6bc8 | -8.5025 | -43.285 | 2025-07-09 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 6ee24737-7bbc-3153-a078-37c12dc0133e | -8.5214 | -43.2828 | 2025-07-09 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 743d7c1a-7879-393d-8afd-c240cf470a03 | -8.3802 | -43.9527 | 2025-07-09 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9f5b05e7-8e8e-34fb-b04d-c84ecaf73ce4 | -3.04105 | -49.43504 | 2025-07-09 12:27:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59b73c5b-ca6b-3417-a25c-daa4c50c511f | -3.45332 | -48.88853 | 2025-07-09 12:27:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1b4c55ad-2db6-37af-b6b5-04993563e2be | -2.45146 | -47.32663 | 2025-07-09 12:27:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0ba1875-59e3-33f5-90e9-cec9e5a6fa3f | -8.17165 | -47.66175 | 2025-07-09 12:29:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d11818f4-210e-3842-8e4f-3a1796c4b28a | -6.80167 | -44.75144 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1f9d87f8-bf18-3d43-81ce-0c88db1074b1 | -8.39585 | -44.04139 | 2025-07-09 12:29:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7ff61c13-925e-3e3b-8d49-6955a8bf25c5 | -8.50742 | -43.26575 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| a11e94a2-98f6-37f5-9811-ad4316fef774 | -7.08423 | -44.39946 | 2025-07-09 12:29:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 3a894bd0-cef7-3492-9da7-ae6b47a3f15f | -9.2282 | -48.59956 | 2025-07-09 12:29:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8d41adf7-a247-38df-99dd-68f87116ef1f | -7.94114 | -44.86281 | 2025-07-09 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ec3b0936-23ea-3db3-8df2-e5d7cb2a401c | -11.68292 | -43.78315 | 2025-07-09 12:29:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| acd796bb-6699-373d-ad32-0d689cc4cec1 | -10.6793 | -47.19603 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3eab5f05-e614-3fbc-bcbf-5f2fb55d46ae | -13.38272 | -47.89271 | 2025-07-09 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5f7558f4-3b30-3f93-acc9-4680b313162b | -10.57163 | -49.13057 | 2025-07-09 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b3e21fc5-60f1-3eef-8ea5-c804d92a75ba | -14.80272 | -43.89966 | 2025-07-09 12:29:00 | TERRA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1418ec3a-48fd-3a5b-b394-775eb2f7e747 | -8.0687 | -43.11373 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 21de97a6-6f7b-3d63-8fcf-af176224f6dc | -8.33647 | -48.44669 | 2025-07-09 12:29:00 | TERRA_M-T | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 92440600-835d-36f7-8fa8-4507f7f1dbbb | -6.67676 | -47.40198 | 2025-07-09 12:29:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2624b06f-9261-364a-80d7-a9fcdf4f73b3 | -14.51715 | -39.85213 | 2025-07-09 12:29:00 | TERRA_M-T | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.3 |
| 247fab7b-c673-35be-bdb4-d752d8d0b5c2 | -8.14253 | -49.5817 | 2025-07-09 12:29:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e7744617-1690-37d0-a187-921572d6528d | -10.24891 | -47.30736 | 2025-07-09 12:29:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d60748d6-dd30-357e-bae4-d708c21b1e14 | -9.22948 | -48.5907 | 2025-07-09 12:29:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a74e3d4d-46f3-3889-8302-1f17c9909852 | -13.02155 | -46.28509 | 2025-07-09 12:29:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dc8c934c-af9f-3ea4-b802-17add96cd3ba | -10.46425 | -47.94423 | 2025-07-09 12:29:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b591fd53-35ba-3336-b9db-26f54a1bb21e | -15.61044 | -43.94678 | 2025-07-09 12:29:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 866ea8c8-e360-3cd6-b795-3b6491309596 | -6.39826 | -43.68021 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 10d764ca-674f-3db2-b83f-0f1d327d3c86 | -10.65366 | -44.48918 | 2025-07-09 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| be264833-1824-34ce-99f7-84f26989c45c | -11.95067 | -46.35929 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 5ac4ad5e-b516-3c06-9158-af0fc6d382d8 | -6.40017 | -43.6664 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fcf51a66-e793-34d4-bc2c-7a066daaad4e | -10.68848 | -47.19726 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 543bf26b-44fc-3c83-a52a-2466df290d4d | -10.68712 | -47.207 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aef8dba0-9aec-39e1-922b-8a28aa550218 | -8.14119 | -49.59086 | 2025-07-09 12:29:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c3dcfdc3-3e71-381f-9617-7d9593a4e99e | -7.28992 | -44.60873 | 2025-07-09 12:29:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e066a370-1617-3e93-b0a7-4c54c2c0bfab | -8.06661 | -43.12988 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 48d4b08c-d24b-346f-a3e0-beaacea94541 | -12.87091 | -49.18073 | 2025-07-09 12:29:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| af5dfb10-7d1f-3dab-85fd-7341d47cd1a0 | -7.66083 | -44.37139 | 2025-07-09 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04ec2611-8458-38a2-9363-170c21e1d7d8 | -11.94922 | -46.37034 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5b6fbe24-0604-34e2-8a53-e3c7f1f20c3a | -12.6624 | -45.27828 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 361741c7-5864-35d3-865a-dd38401f19f2 | -5.58408 | -43.58429 | 2025-07-09 12:29:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a10e02da-9173-358c-b95a-e157ae0c752f | -12.86963 | -49.18972 | 2025-07-09 12:29:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 41184322-8098-31fa-8127-ffaba5de6679 | -5.7893 | -43.61646 | 2025-07-09 12:29:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 32699bd0-1a4f-35e8-906b-963df2c406ef | -8.37413 | -43.93164 | 2025-07-09 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 0d60e66a-77c0-3c90-8c5b-9e5aaf3f4e9a | -8.51694 | -43.28347 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 9659b25d-dc0c-3673-b6a4-e5f13a5a700d | -7.22629 | -46.90827 | 2025-07-09 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12718a2d-7f3d-3fb1-a995-92eb8b65b79f | -6.1793 | -48.04673 | 2025-07-09 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 97b00759-1cc3-3e02-bdff-1d468a03d302 | -6.86187 | -47.85401 | 2025-07-09 12:29:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 274611a0-fe34-3af6-8b32-0e403bb5b44f | -6.57394 | -48.24389 | 2025-07-09 12:29:00 | TERRA_M-T | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5086d59b-f228-34fd-aeac-cede6233b228 | -9.12218 | -47.58871 | 2025-07-09 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7c4cfa69-0677-3e16-9a5d-3c222bccd74f | -10.57292 | -49.12165 | 2025-07-09 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README27.md)
