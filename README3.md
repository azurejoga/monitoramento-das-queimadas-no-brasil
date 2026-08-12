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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed4dd201-ea49-349c-ad6c-3481fb9ac45a | -8.35769 | -46.00012 | 2026-08-12 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| bdd56e70-9dfb-3568-9b9f-d7e1daa29418 | -8.07085 | -46.52174 | 2026-08-12 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7b23db0c-5684-3c2b-8421-ee6e13d87eae | -6.24353 | -55.62216 | 2026-08-12 00:33:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e23a93c4-7bfa-33e9-bcf3-f8f5ef6473d7 | -8.97572 | -60.5358 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 2f251891-4135-34c7-b38d-24ffc9f58b99 | -9.47705 | -60.51026 | 2026-08-12 00:33:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 169334cc-c360-371d-b110-929be0268e2f | -5.73527 | -49.14256 | 2026-08-12 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4eab6422-601c-3a9b-a4b7-b9cb8027511d | -9.14114 | -46.39875 | 2026-08-12 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 106b1f3f-9c96-318e-bf94-82c2e30886ec | -7.41576 | -60.00574 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| f1bc35d1-cdf8-31bc-a812-170adc37eb82 | -5.72148 | -49.1447 | 2026-08-12 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c11ac8ba-1143-3eef-91df-7b70c6e05e1a | -5.72934 | -49.14901 | 2026-08-12 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 6079923f-eea6-3410-be38-bd9e55ddb18c | -6.60157 | -59.01485 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1bab9879-f759-3d05-a0d4-409d98bbadd2 | -6.59053 | -59.0055 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2c3a52d0-6943-32b9-af37-3a4f5738b0a5 | -8.9553 | -60.55339 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4353ba1c-3bfd-3923-bfa8-ccc5e425f8d1 | -6.61942 | -59.0015 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f923c5fa-26da-3783-91ed-abb2130b5ffd | -6.84624 | -59.10125 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 59007af1-3793-3a95-94b4-8e9439c5cf15 | -9.03236 | -47.47998 | 2026-08-12 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b7102408-0eb5-3590-9658-986634179abb | -8.95156 | -60.52411 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 9023b33c-c671-309c-9772-f89c4d0c026d | -8.97775 | -60.5448 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a07694d2-7d78-3569-a1a1-85610cde6896 | -8.96081 | -60.50807 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d210c72a-6290-3a60-9225-50dee5280fc3 | -10.43708 | -54.36597 | 2026-08-12 00:33:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03cbd54c-afe4-3a5a-8775-0e288635e334 | -8.07802 | -46.51507 | 2026-08-12 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 70f4de31-be60-3278-ad08-2bf0ff65fec3 | -9.12517 | -46.40175 | 2026-08-12 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 13289f8c-80e5-3702-b047-021ae512f5b4 | -6.60016 | -59.00416 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5c1f8ec0-3c3d-393d-b915-b6cffd418902 | -8.95343 | -60.53877 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 4126aa9c-70d9-35b1-9b0b-0d2c4c7386d8 | -9.13543 | -46.36531 | 2026-08-12 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| d03cdc5f-e742-334b-83d7-ced9241138bb | -6.60979 | -59.00283 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1d36b379-21dd-3b8b-b551-a79b75eddd89 | -8.94043 | -60.52555 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8066aa83-8a63-3574-8fc3-b0c987af07b1 | -7.41411 | -59.99322 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 148a6f1b-0a81-385d-94b3-2f7c998f30df | -8.90134 | -60.57553 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 11dd610e-c7c1-3d44-8b10-dd43ee97c618 | -8.35333 | -46.00594 | 2026-08-12 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 451f987a-9dd6-3f73-abd8-89998c9824a5 | -8.94969 | -60.50949 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fdfd72ed-19b6-3cbd-921f-4c86f3aa20fe | -7.40369 | -59.99458 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| cacc3b5b-7d19-334b-a5f4-b966bf4e7aa6 | -10.94129 | -57.10954 | 2026-08-12 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d27c598b-ac58-35a1-80c2-81afe1b72bce | -8.89743 | -60.55241 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 842428fc-5cbf-3082-9d52-fdd38740e5b2 | -6.59193 | -59.01618 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ba5ed4d6-0be4-33f1-845e-9ee8dad14a24 | -9.12774 | -46.37173 | 2026-08-12 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 569db3fe-ee5a-31e2-b4fa-8904ba016d3f | -8.95718 | -60.5681 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a035fbef-b8bb-32f8-a4bd-d142bafb67b1 | -8.98686 | -60.5343 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5f8fbeae-8f05-34cd-9417-34c9e14b60d7 | -10.94255 | -57.11914 | 2026-08-12 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a893fdbd-2d91-3c74-be41-5fe0d7f24881 | -9.13327 | -46.40546 | 2026-08-12 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| b399bbcf-770d-3d8c-b731-451aee7bac20 | -8.89936 | -60.56712 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 0b3a8d3c-aa95-3a8c-a573-381277451909 | -8.96458 | -60.53728 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ee6d8b0f-c137-3b1d-b21b-dc29925fc791 | -8.34717 | -45.96796 | 2026-08-12 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a69cf9db-17dd-36ca-a137-4343d921965a | -8.97595 | -60.5301 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f12c13d4-6e7a-3d78-9259-1870c22a6a37 | -7.40533 | -60.00719 | 2026-08-12 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b07d3bb8-d746-3a72-adbb-be5cc7e0eb50 | -9.76038 | -60.76705 | 2026-08-12 00:33:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| cac54fe4-b964-3db7-903f-82fbb4881ad7 | -9.03214 | -47.47329 | 2026-08-12 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 6e4bc570-371e-3406-9fc9-1d0c8036f68a | -8.98335 | -60.59465 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 22f3fb69-c24d-3200-8c26-77e82f0699d7 | -8.89952 | -60.56081 | 2026-08-12 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| da51e39e-8a6c-3674-a4d7-a4b6ccb6c6e8 | -8.35132 | -45.96238 | 2026-08-12 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0c7ef2bb-5355-3f43-9502-e777175dd3e0 | -3.15075 | -54.60981 | 2026-08-12 00:35:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c092886-a09b-34b1-b124-ecfe3acd1b2e | -1.82645 | -54.50893 | 2026-08-12 00:35:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2999cb8b-3bd8-366c-9474-2e02e1d675f8 | 0.18477 | -60.49211 | 2026-08-12 00:35:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 92601568-bb98-3e95-966b-e4cde7b7dfa8 | 2.68325 | -60.41838 | 2026-08-12 00:35:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bca3efe-16ce-3c64-8a3a-2b0986172dd8 | -1.82492 | -54.4982 | 2026-08-12 00:35:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a2a1bf32-4506-3390-b6c9-7d530cf26dd1 | -8.9414 | -60.5367 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 34c4c244-912c-3a6c-ac20-cc319ecea14f | -11.4873 | -44.553 | 2026-08-12 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 06027c70-bf7f-3403-b86b-fe132a690ef1 | -11.4677 | -44.5791 | 2026-08-12 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 222a8c7e-8568-3ec1-a179-641031bacb86 | -13.8986 | -53.8426 | 2026-08-12 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 18866ec8-245c-30a3-9ef6-ee3b315d992d | -11.9531 | -46.3672 | 2026-08-12 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f04205af-76f6-3e8c-a87d-85c77c4728be | -11.8285 | -51.8359 | 2026-08-12 00:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b384840b-33fc-3e1e-af8c-6e132b19c16d | -8.9601 | -60.5165 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 84552d32-1cc2-3558-9b10-4a2d1da79bff | -11.8282 | -51.857 | 2026-08-12 00:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 17eb8670-5aab-30a2-8ff6-aacbfcb5b470 | -11.9535 | -46.3444 | 2026-08-12 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| c58b829d-b512-3fb0-aaf8-a36afa5743f6 | -8.9598 | -60.555 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| d84d4d2d-3da8-31d6-9f3d-72310a28f788 | -11.4686 | -44.5325 | 2026-08-12 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 381bb2b0-4d54-35d6-b128-0f850fc6a601 | -9.1408 | -46.402 | 2026-08-12 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 26203e06-9df4-35d3-b11f-3cbf9052a7a2 | -14.554 | -50.402 | 2026-08-12 00:40:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 6dffe587-c822-3a76-ae03-42c4628ff6d4 | -11.9719 | -46.3871 | 2026-08-12 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 85b662e0-d617-3860-9008-e1c7db2deffc | -8.9602 | -60.4973 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 22d8343b-5751-38ec-918c-29bbf9cf4be8 | -8.9415 | -60.5174 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4c1580ce-bdb8-3dd1-870f-b0704cf231cd | -11.449 | -44.5587 | 2026-08-12 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ed47ab0b-ab19-3e4c-95a6-04fd91f41ff9 | -9.1411 | -46.3796 | 2026-08-12 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 153c91e3-fe0f-3d6c-b3d3-2fa950cc14d0 | -15.5765 | -53.9292 | 2026-08-12 00:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 923898eb-e204-3100-ab28-936787303d2f | -13.8989 | -53.8217 | 2026-08-12 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4c6b10d4-f329-3e9c-a3e4-43c118e75139 | -8.96 | -60.5358 | 2026-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| db7b091c-d435-369e-a56f-ee31e29a4bc0 | -11.4681 | -44.5558 | 2026-08-12 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 0b983986-7eca-3095-a004-1eacdf39a88c | -14.344 | -54.8689 | 2026-08-12 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2d589e24-93d0-36af-acb6-80d6f7456f26 | -9.1222 | -46.3816 | 2026-08-12 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c011a737-7e74-352d-8d55-e5b8fec4699d | -8.96 | -60.5358 | 2026-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 851ca728-8cfa-38e2-a99a-108622408a63 | -11.8285 | -51.8359 | 2026-08-12 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 0e9258fd-954e-33ba-832a-b36fc9d82ac0 | -13.8989 | -53.8217 | 2026-08-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5789f8ba-add9-35db-82a6-57f7158e5473 | -11.8279 | -51.8781 | 2026-08-12 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a8071277-d726-3aa3-ae85-d3467fc83323 | -11.9535 | -46.3444 | 2026-08-12 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2540098b-2c11-3a04-a5e2-de9a872cf92b | -11.8282 | -51.857 | 2026-08-12 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| e6218068-a64e-3349-b1e5-e41439d11112 | -11.8473 | -51.8549 | 2026-08-12 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 84ba51b8-9a8c-3f67-a8c6-96d39acaf90e | -9.1411 | -46.3796 | 2026-08-12 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 4a423339-7bd7-3676-a4aa-64bb8daf5cab | -8.9601 | -60.5165 | 2026-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 023c72bc-8745-3c81-a425-f09f099ddd1e | -11.4677 | -44.5791 | 2026-08-12 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 799dd266-b968-32fa-8186-5aa5912266fc | -8.9598 | -60.555 | 2026-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 60d147d9-f8d2-3be9-b8fc-348e7f150614 | -11.4686 | -44.5325 | 2026-08-12 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 688605f9-a7e6-320a-a431-d00652da95cb | -14.554 | -50.402 | 2026-08-12 00:50:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e259f9db-5dc7-3ca6-a7b1-c4773e23c372 | -9.1219 | -46.404 | 2026-08-12 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0249cb17-6a63-3a9a-b6d5-0f9e8c709fac | -8.9414 | -60.5367 | 2026-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 54bb6d2b-8369-3973-8628-90026c48b3e4 | -14.3633 | -54.8668 | 2026-08-12 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| fdf7cfa2-7476-3aa2-87cb-d63c493a7cd3 | -11.4873 | -44.553 | 2026-08-12 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 32ebaa6b-a1d8-34ee-a0da-23a6c6d5c9f9 | -9.1408 | -46.402 | 2026-08-12 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4377a617-bb32-30a4-8d02-8b617d6f29bf | -14.363 | -54.8874 | 2026-08-12 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e1ec9d0e-7d61-3ec2-9dcc-08cb0fb58769 | -8.3544 | -45.9897 | 2026-08-12 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9d4e05d6-6eb8-3d13-8099-72e6b01bdbea | -8.9415 | -60.5174 | 2026-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |


[Clique aqui para ver as próximas entradas](README4.md)
