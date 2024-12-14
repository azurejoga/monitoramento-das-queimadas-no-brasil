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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e5a2475-932f-3593-88d0-ec4886a64f7b | -3.01816 | -51.39996 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 631550bc-75bc-3632-9c17-a68fa0c2e409 | -3.38309 | -51.50635 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6be8cfb8-d38c-3396-a48f-4fec1f22c50c | -2.82832 | -53.0774 | 2024-12-14 01:00:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9594177f-eec6-330e-995f-63cc884b9c28 | -1.9536 | -50.77114 | 2024-12-14 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f196ddc2-b0d4-34af-a7a0-22d81dfe4256 | -3.56549 | -43.65592 | 2024-12-14 01:00:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a3b41960-348b-3cd8-a5ad-cf0616f6345b | -2.65099 | -51.87522 | 2024-12-14 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1428965c-eb46-3c4c-94a6-417ba22e1ec5 | -1.742 | -52.02696 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d70850cb-482b-3b7c-8e5c-0d0c42f55ddb | -1.74074 | -52.01794 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 578b0d69-1f7d-3084-b4d6-da41ce986b0a | -1.71505 | -52.56036 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9e20a3d3-a44c-30a2-8de6-6c73dc305053 | -3.24585 | -51.37714 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1061763e-a46f-32d4-bb52-b91b4874017d | -3.38185 | -51.49739 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b72553a-6814-3060-89ab-ee3c3a8ba191 | -3.52189 | -50.32225 | 2024-12-14 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8246ce11-ac67-367d-8ff0-2a8c89285e4c | -1.72416 | -52.55909 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9f7dbd7e-77b5-3d53-a469-4b052612601f | -2.8411 | -53.05915 | 2024-12-14 01:00:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e10997fa-c804-37a5-a9c9-8cc08d14e252 | -3.43291 | -50.94109 | 2024-12-14 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ce66461a-36d8-3043-b7d8-7ded42e74f9c | -2.80808 | -53.06998 | 2024-12-14 01:00:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d7988099-93e6-3da5-88eb-67fba341852b | -1.70332 | -52.60975 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6228875e-4541-3bd2-9d09-e274b2d2ed49 | -3.02582 | -51.38978 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9331387c-8e6f-3867-ae47-80a01fd107b1 | -2.73675 | -51.82921 | 2024-12-14 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f81d6a62-a83e-3252-b38a-5bd289006193 | -2.8189 | -53.07872 | 2024-12-14 01:00:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7ca68901-d6fd-3eec-9afd-c2eef3850fce | -3.44618 | -51.10143 | 2024-12-14 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9558a55-c359-35b6-b604-29aef7609de7 | -2.58423 | -51.92154 | 2024-12-14 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6435dd4c-6056-380f-b7a4-7626a2ab414e | 0.65985 | -51.57651 | 2024-12-14 01:02:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5af2bb6e-2984-341f-87c6-3f73e4b17278 | 2.74655 | -60.38541 | 2024-12-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7064ec70-0d77-397c-8d37-c18481d827f5 | 1.18691 | -60.44586 | 2024-12-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.8 |
| ddf7dc75-27c3-37d1-91ce-a748097ecf70 | 2.74489 | -60.39164 | 2024-12-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 27.0 |
| f4b8a9f1-1f59-3bc3-91b4-f573fdf8f1ab | 1.18237 | -60.45041 | 2024-12-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c7d4216f-f984-3bf3-a86c-745726d05738 | -2.3095 | -45.5031 | 2024-12-14 01:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c30e8088-c331-3596-87be-e16f6c053a4f | -6.0472 | -44.0331 | 2024-12-14 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| bb3dae48-cd5d-3f5f-8235-338c3a6e2908 | -4.7252 | -43.1991 | 2024-12-14 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e3cf2369-83de-3ae8-a338-7c6bd53daa31 | -4.4081 | -45.8433 | 2024-12-14 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| cafc4c43-0e46-3031-88bb-9fb1573b2215 | -12.5682 | -57.7579 | 2024-12-14 01:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| a08003f9-899b-3eca-bb58-b28d54905f16 | -11.8295 | -57.8175 | 2024-12-14 01:10:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 71bae733-2434-3bfb-b95d-8ccafdff3bfb | -2.2909 | -45.5036 | 2024-12-14 01:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1900fd2a-02ac-33c2-9778-05ba505f093a | -4.4082 | -45.8209 | 2024-12-14 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 43830bea-590d-3fc0-8608-2820b49a1e1a | -13.1793 | -53.2791 | 2024-12-14 01:10:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 31f8c19d-b068-30ba-b00b-b3aaa7a4a980 | -4.1057 | -46.6142 | 2024-12-14 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e9eb3adf-fa8e-32f9-a934-e2e92025981e | -4.4081 | -45.8433 | 2024-12-14 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b933056e-1f00-3458-b92e-544a5848873d | -3.2504 | -46.8489 | 2024-12-14 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| dd3dd43d-1824-3dc5-9df1-73e23cc48304 | -12.5497 | -57.7196 | 2024-12-14 01:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| cef0dee6-480e-34f8-992a-babcac22e9bb | -3.2503 | -46.8709 | 2024-12-14 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| adfb9d9d-0d96-37de-8380-0783102c85a9 | -4.7252 | -43.1991 | 2024-12-14 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c79e68fb-48b8-3d36-bbd9-8abaf169d085 | -11.8295 | -57.8175 | 2024-12-14 01:20:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 499470e5-1936-3c37-b9c5-ea6000bd7cfc | -6.0472 | -44.0331 | 2024-12-14 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| fbb68d8d-c3f8-31e7-8e7b-170f061f6bc1 | -13.1793 | -53.2791 | 2024-12-14 01:20:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3208757b-1593-3a57-a2d5-8cdb95b9a78c | -4.4082 | -45.8209 | 2024-12-14 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7b1e6529-94b2-37cb-9bcb-4e3eeeb78a7b | -17.1682 | -53.4347 | 2024-12-14 01:30:00 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4a64ecf2-5e0f-3ccc-a0d9-1510bdfd9cae | -11.8295 | -57.8175 | 2024-12-14 01:30:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e03cec54-4705-3e4c-881a-f2cd24718065 | -9.9711 | -36.1719 | 2024-12-14 01:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| 5ba7680b-7fca-3ff2-996d-fce5f5a9786f | -3.2504 | -46.8489 | 2024-12-14 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fb4f5e57-cb13-321c-bc1d-81bcdc533a30 | -13.1793 | -53.2791 | 2024-12-14 01:30:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 61aec60f-5f29-3e0f-b3e6-86b134d80e0d | -12.5682 | -57.7579 | 2024-12-14 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 12cd1576-c177-3609-be62-6915c944575c | -12.5497 | -57.7196 | 2024-12-14 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 8d2defb3-86ad-32a6-a9d6-d4a9e77078db | -6.0472 | -44.0331 | 2024-12-14 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 39db39f7-866c-3165-aa5e-8bd56e6fe295 | -3.2504 | -46.8489 | 2024-12-14 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0ce55152-733a-37e3-a0fd-090618d1e70a | -13.1793 | -53.2791 | 2024-12-14 01:40:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 171af874-1c38-30d0-99f1-a4e7471249d7 | -12.5687 | -57.718 | 2024-12-14 01:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 5dd40932-9bc4-3318-bc44-4f11ed77f3af | -12.5682 | -57.7579 | 2024-12-14 01:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1130a0af-8dfc-38ca-a0a4-7deb7b257c4b | -17.1682 | -53.4347 | 2024-12-14 01:40:00 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2914b92c-927f-3649-b42f-5de62171999d | -6.0472 | -44.0331 | 2024-12-14 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 09522f5f-94c2-3d72-8fb0-56f0989051b5 | -12.5497 | -57.7196 | 2024-12-14 01:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5288463a-c84a-3226-b88e-cb61e1ca7ce5 | -11.8295 | -57.8175 | 2024-12-14 01:40:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 93eef4b5-b31e-3952-88c6-21526e8075e3 | -3.2503 | -46.8709 | 2024-12-14 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 43f46210-d6b6-3bb2-b6d0-66f7577482a6 | -17.1682 | -53.4347 | 2024-12-14 01:50:00 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 39ac2236-739a-376f-8246-8ed5eb565497 | -3.2504 | -46.8489 | 2024-12-14 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4fbfa6ce-e32f-3a60-9232-7ecd08416afc | -6.0472 | -44.0331 | 2024-12-14 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| cd4138a3-f481-3935-9086-c13fa37f2f49 | -12.5497 | -57.7196 | 2024-12-14 01:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4d13eb6d-bbf7-3b6f-9905-609583249c97 | -12.5682 | -57.7579 | 2024-12-14 01:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8f70b9e2-82de-375e-bc5c-1fdb4876e02e | -11.8295 | -57.8175 | 2024-12-14 01:50:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 831cce60-e64d-31e5-a9cc-529e8316ed00 | -12.5497 | -57.7196 | 2024-12-14 02:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 965abb11-9b5e-342f-bd7c-a084e17f2107 | -11.8295 | -57.8175 | 2024-12-14 02:00:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b142d996-e0b7-30b6-850e-023ce5f2d353 | -17.1682 | -53.4347 | 2024-12-14 02:00:00 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 142aa998-42cd-30e7-a041-d4577ffd41c7 | -6.0472 | -44.0331 | 2024-12-14 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 567409f7-718c-33cc-ae89-081045d96952 | -4.1057 | -46.6142 | 2024-12-14 02:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 84e812f2-448d-3aba-a389-12a270e50190 | -9.85 | -36.21 | 2024-12-14 02:00:00 | MSG-03 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62d551ff-4688-3f0d-8709-ef856d9fe73d | -13.1793 | -53.2791 | 2024-12-14 02:10:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 75b4e4c5-c2b0-3eb7-81fd-0165a820d54d | -12.5682 | -57.7579 | 2024-12-14 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 974406de-aa05-3cff-a831-7a3fc930bde1 | -6.0472 | -44.0331 | 2024-12-14 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e69bf54f-9a4e-329f-843f-1ccf5d429b69 | -12.5499 | -57.6996 | 2024-12-14 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| e7932386-ff82-389e-bfee-a705689d72a4 | -4.1057 | -46.6142 | 2024-12-14 02:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 665b7c0e-7acc-3f46-881c-df961f6089fb | -1.7178 | -52.5553 | 2024-12-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0927684e-b880-31a2-95bc-a5dfa73ef253 | -11.8295 | -57.8175 | 2024-12-14 02:10:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9fdb3015-3998-34be-9c15-ec958330ee43 | -12.5497 | -57.7196 | 2024-12-14 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1ad95b6a-2e72-327b-b609-323f1ed44108 | -12.5687 | -57.718 | 2024-12-14 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 3383cc0b-c595-3d79-9db6-6eb09fff11cc | -17.1682 | -53.4347 | 2024-12-14 02:10:00 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4e49e83a-fee8-3713-9eba-beed5e7a8dc6 | -11.8295 | -57.8175 | 2024-12-14 02:20:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f993497a-712f-3bfd-9a26-16b34b01b6bb | -12.5497 | -57.7196 | 2024-12-14 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b4b7d617-5b00-3231-adf0-d3a3c862c3cb | -12.5499 | -57.6996 | 2024-12-14 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5fd4403d-d34a-3383-ac8d-d22e7047da13 | -14.8449 | -53.6661 | 2024-12-14 02:20:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| bed086f4-2d60-38f9-9db9-8ea65f363b4f | -4.4081 | -45.8433 | 2024-12-14 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 408acc06-b86b-3264-b683-2ba2ee0bb0d9 | -12.5687 | -57.718 | 2024-12-14 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| c82c223e-5645-3a3e-bdc7-0c0159e59e2c | -6.0472 | -44.0331 | 2024-12-14 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| faa75bb8-7311-31ba-8e4d-798238a8ba79 | -4.4082 | -45.8209 | 2024-12-14 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e44d9fdc-8ecc-3b8a-9938-f3e4b2898b0c | -12.5682 | -57.7579 | 2024-12-14 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ca92a5d9-d030-3c87-80f5-329ea91c410a | -12.5682 | -57.7579 | 2024-12-14 02:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c31eb866-b605-31fd-916d-d0ca328c4ebf | -4.4269 | -45.8199 | 2024-12-14 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e5966559-91af-36a4-bd7a-19b5a152318f | -11.8295 | -57.8175 | 2024-12-14 02:30:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6f82f37f-f9f1-3345-a591-52ba380d500c | -1.7178 | -52.5553 | 2024-12-14 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 989ec237-231a-343c-a6fa-118d0effdb1a | -12.5687 | -57.718 | 2024-12-14 02:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 8da28743-ed82-3521-a510-2b29f6c9ee15 | -12.5497 | -57.7196 | 2024-12-14 02:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README3.md)
