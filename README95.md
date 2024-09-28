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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 563293a5-0358-30ea-a72a-3d27ef70ee54 | -16.49057 | -57.37534 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3773f464-a8eb-3400-8e5c-ae22b410be79 | -16.48712 | -57.3748 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d733f627-7ebb-32ca-bde2-b8cfac15b26d | -16.48597 | -57.38262 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c63af55c-2f0b-3c32-a92f-4bdd37c72cac | -16.48367 | -57.37426 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4357e038-8e4e-3cc0-83e4-27a786cefde8 | -16.4831 | -57.37817 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a2bd534c-5b93-3a7a-b3f4-89ac455e78d1 | -16.48252 | -57.38208 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a0d3ce23-ab8f-33dc-ba9f-5c68f665692f | -16.48022 | -57.37372 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 800bd7ee-b2b6-389d-b32b-c007b7f1afad | -16.47964 | -57.37762 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8440c856-8ddc-3839-bd3a-55b9165427c7 | -16.47676 | -57.37317 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 82647f02-5bcf-3cd3-8e8c-1c818e93e2b9 | -16.47619 | -57.37709 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 58841159-098f-3121-bee1-c76b5092eebe | -16.47331 | -57.37263 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 444ae807-3b5d-35b3-99f1-e1bfb6e4d194 | -16.47274 | -57.37654 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e78d9e80-56fd-306a-a801-835843ebd9a4 | -16.12177 | -57.53027 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dd1894ea-d91c-38f6-b85e-c03f60f7ef25 | -16.1189 | -57.52603 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bc5e6c69-ab3a-30c7-99b6-500e8629fbb1 | -16.99891 | -57.95978 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e93898d6-2fa0-3cff-a46d-3179c79eb437 | -16.99551 | -57.95924 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 30c23e38-8bd3-394a-9ef9-1f465578e222 | -16.96373 | -57.93605 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 175652bb-599b-3c52-9960-e89a86618a62 | -16.96317 | -57.93985 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f00c6162-d443-36ba-a11a-6fd3016b05e4 | -16.93714 | -57.99783 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4fd135c4-cf35-3c5a-955a-32344ff6c0b6 | -16.93375 | -57.99728 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fc3bfd99-597e-3588-96b9-cdd5b7542e96 | -16.93037 | -58.01999 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 40843571-0dfd-3c60-a3ec-549fd6584fea | -16.93035 | -57.99674 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d1363dfb-b680-3441-bb17-169bdcf4a37d | -16.92981 | -58.02378 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d48ba017-0fd6-368d-a2dc-bf0ac6be7f9a | -16.92696 | -57.9962 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 94400f2a-bcc2-33c7-803f-1d79b5db7464 | -16.92356 | -57.99565 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3223b38e-2148-3ec0-bccf-326b744d9052 | -16.92073 | -57.99132 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a2894d6c-e186-3c89-8ede-311f73930a1a | -16.92017 | -57.99511 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8be25710-4d92-337a-846c-6238d19f7ccc | -16.91677 | -57.99456 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7cd8bf7c-50b9-38fa-b5cf-41f47a30c4db | -16.91338 | -57.99401 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9ae7341d-bca0-3fbb-993c-033e84ee008d | -16.90998 | -57.99348 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| df51c89d-d4f9-39ec-a7f0-8a68106d02e3 | -16.90659 | -57.99293 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1c4a3292-0e63-31b8-9d3a-bb77b3508bd3 | -16.90544 | -57.97723 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bf0911ee-1c04-3e24-b3aa-d2b15d6983ff | -16.90487 | -57.98103 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 875b3eac-0878-353a-a89e-6d35f8db3db9 | -16.90372 | -57.96532 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 056b4fba-1355-31f2-9734-7988ed93608e | -16.90316 | -57.9691 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 611ea142-2dbd-3c94-9465-b3cd27d12d7c | -16.9026 | -57.9729 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| db4e5118-37fc-38e6-8b38-381f2515181d | -16.90204 | -57.97669 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 86146c4e-8dbb-366f-beb6-ec9d93b8d8c5 | -16.902 | -57.95339 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e7d905bd-8b6d-34ad-831a-2d0decc19a29 | -16.90148 | -57.98048 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7a0d3918-c276-3ae9-92cd-c4eaf64c1618 | -16.90144 | -57.95718 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5ac21191-f6a6-3126-8885-40be87692b6e | -16.90088 | -57.96097 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| efff0d06-eef5-364f-ba71-1a59b61774da | -16.90032 | -57.96477 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f2302eaa-9ece-3654-95a0-eb51205f2946 | -16.87639 | -57.72281 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 095d8547-b195-346c-8ac3-b4e6e701b542 | -16.87462 | -58.03841 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c0cc0a70-746a-32f8-926c-b458eefc926e | -16.87349 | -58.04596 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9f88c3e6-3a7f-3a2e-b505-07d916fba987 | -16.87067 | -58.04164 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6d682665-5206-3c95-a684-c357e60842e7 | -16.86898 | -58.02979 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 86220337-ce8a-3801-94e2-4dffc969a0af | -16.86841 | -58.03356 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b2a3bc58-15fd-3636-857e-8c82e5952492 | -16.83879 | -57.74047 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aef6db61-daf6-3273-ab62-74bfc828fe17 | -16.83537 | -57.73993 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cfcc6ff4-0cb3-3ef7-8bf1-8bdedf816bbf | -16.83195 | -57.73938 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 02e30cc1-b2d7-37e3-9459-e39028335fe7 | -16.78808 | -57.49144 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6f44e326-5e76-34fb-a00a-6b0262ccffaa | -16.73083 | -57.47899 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 93722b33-79b0-34dd-aaea-e3448a903a1e | -16.67165 | -57.4497 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 36580cd7-f5f3-3df4-885e-8a45e07a794d | -16.67108 | -57.4536 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 713c312d-c437-3d39-afef-f3231221a0c4 | -16.6682 | -57.44915 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e6e5d78c-12f4-3e11-80e7-2e16568ce463 | -16.66763 | -57.45306 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e65bbe02-2152-3948-934c-95b8cd9f35f4 | -23.56623 | -47.35172 | 2024-09-28 05:14:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 18244782-5f59-37f1-b1d0-0e6e20549845 | -23.56579 | -47.35802 | 2024-09-28 05:14:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e796fb8a-bc15-3fa8-a118-484ad8b3a453 | -24.24148 | -50.74075 | 2024-09-28 05:14:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55a48fdf-a75c-3e5c-80eb-1259a19f3b88 | -23.69506 | -55.25456 | 2024-09-28 05:14:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 96a478b0-bb4d-3835-9d99-5c3803cb1ee9 | -6.3171 | -43.4154 | 2024-09-28 05:21:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| c840146e-455a-34dc-8aa9-3b3a7d42397f | -6.31535 | -43.42791 | 2024-09-28 05:21:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fdb6aba5-875e-3a44-b2b4-01d0d74934be | -6.17093 | -43.44589 | 2024-09-28 05:21:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 38ade8a3-b40b-3e6c-858a-9a9e33c2c063 | -5.88685 | -42.78131 | 2024-09-28 05:21:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0f2d7628-8474-3ee8-a62a-420a3566cc44 | -7.2651 | -44.93591 | 2024-09-28 05:21:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e81319c-6a45-335a-a78a-25004994be64 | -7.14442 | -45.43819 | 2024-09-28 05:21:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 92ced60d-9912-3627-9c83-7d4d45b53fe2 | -7.02172 | -45.33895 | 2024-09-28 05:21:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f0a378eb-762d-31fb-84ba-f7fffc841354 | -7.0203 | -45.34866 | 2024-09-28 05:21:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e79c7279-6a23-3d2c-b54a-a423e41b5f1a | -6.68949 | -44.5511 | 2024-09-28 05:21:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c8e57ade-4f22-351e-aa7f-0b5841acabca | -6.58903 | -44.17061 | 2024-09-28 05:21:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 59616f34-c58c-360d-abb3-9cee6890843e | -6.57955 | -45.71003 | 2024-09-28 05:21:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e80a9528-9261-3f8a-96f7-58635d531a66 | -6.57916 | -44.16936 | 2024-09-28 05:21:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| af9499b1-ed49-3767-aee2-84d9c698b29f | -6.57759 | -44.18044 | 2024-09-28 05:21:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8d82310f-3ec6-3d45-9c37-7a8aeba124e3 | -6.3915 | -44.77735 | 2024-09-28 05:21:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1f82f7ea-a5bf-3deb-91e5-cca1218486bc | -6.17908 | -45.42785 | 2024-09-28 05:21:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd894a87-39cb-350c-bc4e-3fde25081122 | -6.16993 | -45.4265 | 2024-09-28 05:21:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9e40de13-3c10-31b7-ae89-8a53286336ca | -6.16853 | -45.43603 | 2024-09-28 05:21:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f45f2e70-5a9f-3666-a6c3-6d46ceccedd5 | -6.07796 | -47.65694 | 2024-09-28 05:21:00 | AQUA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8ad3e82e-0aeb-32b4-8f65-7d54c70dfac5 | -5.93686 | -49.18996 | 2024-09-28 05:21:00 | AQUA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6749f209-5f8e-3385-9fbc-846d4a7ae4d0 | -5.56307 | -46.283 | 2024-09-28 05:21:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d7cb47d-6f5f-3d13-8ea1-4c07c402ac27 | -5.55321 | -44.66804 | 2024-09-28 05:21:00 | AQUA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a3fd28b5-9956-3f2f-a7b1-e182fb319355 | -5.33881 | -46.60984 | 2024-09-28 05:21:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 407b3be1-cdc6-3cd8-8e26-928914054929 | -4.90844 | -48.60938 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 399e7caf-f140-3e63-9f6c-856a82caccb7 | -4.58363 | -48.01087 | 2024-09-28 05:21:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5bd59fe3-4156-3f22-961c-8abaa3e12110 | -4.57461 | -48.00954 | 2024-09-28 05:21:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3b0cae64-8c6c-3f8c-8841-15bab7d42296 | -3.91443 | -46.43797 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fed25261-159d-3bdd-8064-cdc6cb599430 | -3.91312 | -46.44676 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1f13022-0f2f-3156-8372-e84a1072ff2b | -3.9118 | -46.45556 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 134.2 |
| dd0ce3a7-e623-3fc6-b773-bd6da875f4da | -3.91048 | -46.46436 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 108.7 |
| a0e0b3a3-4273-3427-984b-60ce116b5559 | -3.90296 | -46.45427 | 2024-09-28 05:21:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1ebb56f0-0627-3ff6-b680-e4c431635390 | -3.57606 | -50.54972 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0e66afe9-e620-3bfd-ae63-d3495df34bf2 | -3.57414 | -50.56253 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c8263193-f9db-3681-aa71-6d2c93afcb85 | -3.56895 | -50.5552 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0b67c5ce-728b-3ebd-b516-e310e5b2c91f | -3.56691 | -50.56809 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 54603f3e-8084-318b-86c1-e3f8f308cf0b | -3.56159 | -50.57378 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7e55c183-910c-3296-8856-d725771a373a | -3.55923 | -50.3766 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b4c76bab-8961-3066-ad02-63b635f90b0a | -3.46432 | -47.65892 | 2024-09-28 05:21:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 720219bc-d506-3b69-a8b9-f28a2d53d291 | -1.16892 | -46.71347 | 2024-09-28 05:21:00 | AQUA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e967dfd9-c348-393b-97f9-f3a5e72c1173 | -3.46294 | -47.66801 | 2024-09-28 05:21:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README96.md)
