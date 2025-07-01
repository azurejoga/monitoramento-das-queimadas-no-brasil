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
| 77478b78-6a77-3a57-bfe9-2221f089fa2a | -7.2025 | -43.1171 | 2025-07-01 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 3a1b8707-89e4-3669-97a1-2d4efcaf7d04 | -10.1207 | -52.3409 | 2025-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 9d35ca7f-4527-3730-a349-d3ac37edff15 | -10.1393 | -52.3601 | 2025-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 57fb19a0-707c-3eab-81ed-d098cf1bc0d7 | -4.3197 | -48.0908 | 2025-07-01 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 014d98b6-59f3-38e8-bb16-d6ae15aec45d | -12.6319 | -54.2087 | 2025-07-01 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9bb963e5-e37c-3471-b32c-c92e9893fcca | -7.2214 | -43.1153 | 2025-07-01 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 933e077a-ae0a-383e-b690-f77b5bb11387 | -7.2217 | -43.0917 | 2025-07-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 5fbd8a32-74ff-3df2-be41-cfd1a95a8776 | -6.4814 | -43.743 | 2025-07-01 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ac184054-8e2d-3ef5-a1c0-1f5879062594 | -4.3197 | -48.0908 | 2025-07-01 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 73fb941f-baac-34ad-a3a0-b194b336e45a | -7.2025 | -43.1171 | 2025-07-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 2cba694d-1597-38c2-b2d5-ed49e982183c | -6.2943 | -43.6891 | 2025-07-01 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| c1f630e9-db98-367b-9b1a-797f7cd4046b | -10.1393 | -52.3601 | 2025-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| be270e5a-2e7c-33f1-836e-d82e115ac5e9 | -7.2028 | -43.0936 | 2025-07-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 705b8bd2-a0db-3209-99ce-ddd33fd91958 | -7.7755 | -44.0396 | 2025-07-01 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 964f4109-d001-382d-9a48-63e79d8aa2bd | -7.7758 | -44.0164 | 2025-07-01 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 0e911157-9466-3da7-bf89-3b926b04c131 | -6.2224 | -43.3693 | 2025-07-01 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 26b6d9c9-d96b-3a2c-ac75-bb447a8766ee | -7.6239 | -45.7447 | 2025-07-01 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a5c0c052-a415-3799-8a8b-03e6639b85c5 | -10.1395 | -52.3392 | 2025-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b6c1e579-632d-32b4-905c-831d87ebb31e | -6.2226 | -43.3459 | 2025-07-01 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 09443553-bbe3-3b30-b208-a311fbfd9d92 | -10.0784 | -52.7393 | 2025-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3914c83a-0849-3c62-8ac0-e2cd70450f2d | -10.1205 | -52.3618 | 2025-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6f2ff012-8cb8-37fd-8b9f-8fe6c167ca43 | -6.2945 | -43.6659 | 2025-07-01 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2e43fe3b-0014-387c-aeb0-277d59b72401 | -10.8832 | -56.4367 | 2025-07-01 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a142ea01-60ef-3b8b-94ff-d60b456a33e0 | -7.2214 | -43.1153 | 2025-07-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 241fbf64-3f01-313e-b2bd-989e2b4200fd | -10.883 | -56.4567 | 2025-07-01 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| a7da3f8f-47a5-3605-9772-1a7de8fcf2c3 | -10.1207 | -52.3409 | 2025-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 6f751128-d330-3379-a3dc-29b72de7c70b | -7.7947 | -44.0145 | 2025-07-01 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9e5de06c-8001-35ce-8bfd-0329fcee918f | -10.883 | -56.4567 | 2025-07-01 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| c20b28b4-ae3b-34f2-910e-f11777345b3e | -10.8832 | -56.4367 | 2025-07-01 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9c7dac24-c13e-35cc-861a-537ac6286ad8 | -7.7755 | -44.0396 | 2025-07-01 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 9f5d3e3b-63ab-3d38-8373-d86215335d54 | -7.6239 | -45.7447 | 2025-07-01 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 442bba3b-89dd-3765-8e29-2205d356aec3 | -4.3197 | -48.0908 | 2025-07-01 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 35e356fa-ce2a-398a-ada1-ad67b9c4b62a | -7.7761 | -43.9932 | 2025-07-01 01:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5b3be02d-1e13-356d-a388-5ee5dfafedb4 | -7.2028 | -43.0936 | 2025-07-01 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| acd69a74-7cf6-32db-9a56-ca15c9d2d69a | -10.0784 | -52.7393 | 2025-07-01 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 96e18931-5a84-3683-b152-e121e8bb9cfa | -10.1207 | -52.3409 | 2025-07-01 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b69994c4-e189-3aa3-86e2-e33c0641661d | -7.7947 | -44.0145 | 2025-07-01 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| feb4abe6-4fa7-340a-ac46-b6fa96c3071a | -6.2226 | -43.3459 | 2025-07-01 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 519f4f02-5f3f-3afd-90a4-e4016bd572c4 | -6.2943 | -43.6891 | 2025-07-01 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b4bdb69b-5a58-3899-8fcd-6aa5113215d5 | -10.1395 | -52.3392 | 2025-07-01 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f0a2b1c5-b7ce-33fb-8cc5-af6aced29f89 | -7.6051 | -45.7464 | 2025-07-01 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d28dcd46-7a45-3610-9993-17534059e9ba | -6.4814 | -43.743 | 2025-07-01 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 3a1ba74b-e2b4-3d41-8ca2-d1b70a59d3e1 | -6.2945 | -43.6659 | 2025-07-01 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 02588488-0613-3a89-94d6-40b2589adb43 | -7.7758 | -44.0164 | 2025-07-01 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 00dad9a0-5797-32c4-a12d-58cede98e97e | -7.2217 | -43.0917 | 2025-07-01 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| d78e0590-b30a-383b-bc8b-b73a7259c39f | -7.2214 | -43.1153 | 2025-07-01 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 5c9b6939-de6f-318d-8603-667a27d79625 | -10.8832 | -56.4367 | 2025-07-01 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| d43a579d-58e8-3e38-8670-fa2dcf835f75 | -7.2028 | -43.0936 | 2025-07-01 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 71982f51-a70a-30a5-b05a-0cfc391713e7 | -7.2214 | -43.1153 | 2025-07-01 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 9ad77dff-aeda-395e-95d4-ffc2e8660dff | -7.6239 | -45.7447 | 2025-07-01 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 10578ca9-2b91-3166-b7ed-2ed8655cf176 | -10.883 | -56.4567 | 2025-07-01 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 89f76d15-e7c1-36e8-b539-8ab5330af91c | -10.1207 | -52.3409 | 2025-07-01 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 35d06c55-bd0c-3531-a402-2b35d3d4848e | -10.1395 | -52.3392 | 2025-07-01 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b5efa047-5a68-34ae-8483-d108ceeab636 | -6.4814 | -43.743 | 2025-07-01 01:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e34d3d8c-002e-365a-bc1a-ef28becb84c2 | -10.0784 | -52.7393 | 2025-07-01 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 70a1e238-5e5c-3ceb-8045-f7e33cfad6fe | -4.3197 | -48.0908 | 2025-07-01 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 340cf9c7-3de4-3575-af85-eb7c6594afb3 | -7.2217 | -43.0917 | 2025-07-01 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 418ea9e6-2710-3e00-84bd-004e764eca3d | -6.2943 | -43.6891 | 2025-07-01 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 3cf5c208-6a0c-359a-8559-039bc6e1d5af | -6.2945 | -43.6659 | 2025-07-01 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 69da0abc-9c64-3706-96d2-46df635c7c08 | -9.9847 | -48.2378 | 2025-07-01 01:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 64143c2d-463e-36fb-9dc1-77805e5a2d41 | -4.3197 | -48.0908 | 2025-07-01 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 293623a3-8a16-3b5e-a8c9-7ffe21a5e0dc | -6.2945 | -43.6659 | 2025-07-01 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0e0033f0-fcd1-3e2f-8eca-5eb5a72a4c34 | -7.6239 | -45.7447 | 2025-07-01 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e5b90046-60ed-3d90-9d87-a3ef5d653e99 | -6.2943 | -43.6891 | 2025-07-01 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 5726c9da-6202-3f62-a505-be36bbe21332 | -10.1395 | -52.3392 | 2025-07-01 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3f78f515-9469-3e30-8745-70fd493c2ab7 | -7.2028 | -43.0936 | 2025-07-01 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 58d04f71-1fb7-3634-b3cf-e96650ab7feb | -7.2217 | -43.0917 | 2025-07-01 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 8f5e1a97-5c98-3ffb-abeb-452b9dab863c | -6.4814 | -43.743 | 2025-07-01 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f263838a-e16d-3fc9-9db3-baf9418372bb | -10.8832 | -56.4367 | 2025-07-01 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 147e7b8f-a223-300c-ab84-d20165b2248c | -10.0784 | -52.7393 | 2025-07-01 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d4b3917b-4978-382c-87f9-1141f0af693f | -10.1207 | -52.3409 | 2025-07-01 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d3b45de3-068c-398f-bcdd-7c4a1f5d4834 | -10.883 | -56.4567 | 2025-07-01 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2e89aac9-ee01-33b9-87de-45498fff0460 | -21.13778 | -48.60009 | 2025-07-01 01:20:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| b3872847-6a19-3517-9511-8ee62966dbc4 | -10.30123 | -57.14356 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 80def35b-dde1-33f0-a3c4-d733c9b76cdb | -11.12591 | -55.45456 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 244fd92d-b520-39d5-b2c3-0f97d40b4db1 | -10.08764 | -52.75883 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| dd653c69-924a-3dae-ad03-89fc2d44cd38 | -12.10047 | -54.57511 | 2025-07-01 01:22:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2385a395-0250-34c8-99ef-03ef2f5b70d2 | -9.08384 | -59.48993 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3022633e-d1f5-3017-ba36-f44ad1f88466 | -12.01575 | -47.77381 | 2025-07-01 01:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4c7e09de-8393-31e8-a0f4-a09f4c6d023d | -10.30898 | -57.13245 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 072e62ce-f84c-35bb-937e-5fa473244d84 | -12.62816 | -54.23061 | 2025-07-01 01:22:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9658e4de-79af-3d27-9080-3b37d9a3df45 | -10.28087 | -52.8347 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| b616243b-9f57-3f2c-9ad2-ca318a3b5ec0 | -10.29982 | -57.13388 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8c288c12-5c57-3158-a913-473c561266c2 | -12.63669 | -54.21565 | 2025-07-01 01:22:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 802bf2ae-09ae-35c3-855f-3f7615bb3d1d | -11.19364 | -55.91515 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a3cea389-66d7-39f8-b451-1cbcd4b25414 | -9.7092 | -56.18718 | 2025-07-01 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 51407c52-1054-3256-b3ff-39b19ad2692d | -11.07368 | -55.37896 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c0b52af3-3add-3781-9c97-881136ce831e | -11.57464 | -54.57152 | 2025-07-01 01:22:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 116dc1cc-82df-3f1a-aebd-42469784c582 | -9.04569 | -63.98804 | 2025-07-01 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f4bedef5-c62d-35a4-b0af-7abbbefc6853 | -10.87448 | -56.4538 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 0c985967-a2ab-392d-a3dd-75fc2b625abc | -9.24211 | -58.76784 | 2025-07-01 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd8cf34b-6968-30b0-aac4-f09c00ad20aa | -10.12549 | -52.34437 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| b48f11a9-6a0f-3e4d-b065-427072876b85 | -10.8824 | -56.44204 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 15cf6426-040b-3372-91de-44e950ba69e6 | -8.68573 | -63.77774 | 2025-07-01 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c95639b0-6f6b-3bfb-9826-df8fc94d7b45 | -9.24086 | -58.75892 | 2025-07-01 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f46c8fbf-d887-34a6-bbc7-cb3f6d24be49 | -10.8839 | -56.45235 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b998d9e8-3f73-3bf4-b809-fd9506916a53 | -10.29841 | -57.12418 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 49f42137-c902-3ac3-9dff-deb092a1882a | -9.09146 | -59.47976 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 841d8042-151f-3513-911f-a943048231bc | -12.97714 | -54.69237 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 22a2750b-2f0a-3906-9330-2c01399c4496 | -12.10605 | -54.56773 | 2025-07-01 01:22:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README3.md)
