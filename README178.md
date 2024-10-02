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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4388b75-152d-3cd3-b7f7-1499c5f38e70 | -17.22831 | -56.19048 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f63c6a7d-854a-3911-8bfd-62fbf14572c4 | -17.2279 | -56.1942 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 1fe99faa-8401-3324-be38-fd7d4a8177ca | -17.22525 | -56.1674 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 237d985e-1c89-3d4b-92c4-f7ba31b04f64 | -17.22443 | -56.1749 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 52f018c6-e52d-37f4-8d79-37254cd47529 | -17.2232 | -56.18611 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8d34762f-e303-396f-943d-ed8b4d30f9d0 | -17.22238 | -56.19357 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aced3f9a-4b83-3de7-ab38-55fd17e9a4f9 | -17.22014 | -56.16299 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| faaeb551-e71a-3bf1-b29e-59c5fba997aa | -17.21891 | -56.17425 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a7577f32-66f7-30cb-9317-75686af26992 | -17.2185 | -56.17798 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a1d5ef7a-e4c3-34bb-aed3-d3a4adf22c55 | -17.21727 | -56.18922 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f8edf98a-05e8-3710-8adc-69408fac764f | -17.21461 | -56.16234 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f9aea46f-0465-3159-abea-4f7123be3d61 | -17.2142 | -56.16611 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 7acea6e0-a4a1-3c13-9070-d65983eece04 | -17.21379 | -56.16986 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 425eecc9-1c2f-3235-938d-f7dda7d79ce5 | -17.21338 | -56.1736 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d8ed1462-70f1-399a-ae53-fb8fe35e22ab | -17.20949 | -56.15794 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8409e848-0989-3d8a-8d1e-7e6d70c43bfb | -17.20909 | -56.16169 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f2631c19-a218-3f11-a830-248ac1c01203 | -17.20868 | -56.16545 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 8b9ba912-934e-3a2b-8cd6-6b5c3f37edbe | -17.20827 | -56.1692 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7fd5be5b-b54f-3784-8d00-98aa07666696 | -17.20437 | -56.15353 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f4226b1f-2fef-38af-a52f-ce8364e2701b | -17.20397 | -56.15729 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 15420cac-fccb-3a7c-80d8-394d392be76b | -17.20356 | -56.16104 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 917f0dcc-b57e-35bb-8f5a-9df56191c244 | -17.20316 | -56.1648 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 26088afd-a0e7-3bed-96bd-de968a2a82c7 | -17.20275 | -56.16856 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 94f15ae2-603e-3b68-9ee1-450b3dc370ae | -17.19763 | -56.16417 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fe19a6f4-454c-3a79-aec9-d9dbb7b1cec9 | -17.19722 | -56.16793 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ac70bbca-0c58-3f4d-b066-0899de50579e | -17.196 | -56.17923 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b2648d50-a25b-3e10-aad6-b5aefa7dccb5 | -17.21012 | -56.20355 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 07f452a2-9703-3d3a-9a9b-0d8ea7f6a1cc | -17.20809 | -56.22215 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| df4acec7-c24e-3edb-b16c-909c4ae321c4 | -17.20769 | -56.22585 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 92c2470c-7eaf-36b9-a989-611edc22c56b | -17.20688 | -56.23324 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 281bfbcc-8f58-30d5-b5f2-3d4d3fc0ef6e | -17.20647 | -56.23693 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b65ae165-3881-3037-815f-9ab99e03b18c | -17.20607 | -56.24062 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b4db360-7f9d-36e9-ae58-e495bb9fbd03 | -17.20567 | -56.24432 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 68b286ec-20e9-31df-8877-3f1853e0de67 | -17.20461 | -56.20287 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 065ac014-5f5b-3145-8483-4f68070539fc | -17.20364 | -56.26284 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 62a78763-fcc7-36fe-9c8e-608997a2b83d | -17.20259 | -56.22151 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| db69a2a9-6f8f-3469-985f-b8ca709aeb8f | -17.20218 | -56.22521 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 41b61111-4563-32a1-b76e-72d3886c392c | -17.20178 | -56.2289 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fae2a987-97dc-3718-83a5-cd7e743dbc9f | -17.20138 | -56.23259 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e4241320-03ec-34f9-a0cb-f16caf2ea25f | -17.20098 | -56.23628 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9c32eb62-2576-378e-946e-1b959b61e39e | -17.20057 | -56.23998 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16fc0e93-c6af-3bcd-8187-7bcec817d7e2 | -17.20017 | -56.24368 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a21a87f6-8ff6-3ceb-b3b0-a0b757977666 | -17.19977 | -56.24739 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e33e0765-d6fd-39ae-8169-8a9ecb443d87 | -17.19896 | -56.25478 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 93754081-5933-3a93-8f6a-b74ce1865fb8 | -17.19856 | -56.25848 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 827f3bb5-232d-3a0a-840c-22acffba5ed7 | -17.19815 | -56.26218 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 345563af-678b-3edb-8c13-d8076fcdba28 | -17.19748 | -56.21715 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7ac8e03a-b098-3b8a-9c62-10f3ccc2e80b | -17.19708 | -56.22086 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f43173b0-a451-3d42-90b6-7bef919fd337 | -17.19588 | -56.23192 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f360e02-bda6-32b1-99ce-efc5c53063ad | -17.19548 | -56.23563 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ebdab1f5-a653-3c6e-964f-0daf2c30373f | -17.19508 | -56.23933 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2513aa99-3197-3e6d-b09c-1576abdf01e7 | -17.19145 | -56.27268 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 267fefff-f042-3947-9247-5dd4bd0fa52f | -17.19049 | -56.17858 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 52714349-3779-36a5-ae49-81c32e5a54b0 | -17.19038 | -56.23126 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 83f2e157-df3d-3db7-8e0a-90d87e315322 | -17.19008 | -56.18232 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d03931bb-49af-37b5-9db4-91effed75e9a | -17.18998 | -56.23497 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 26c05df4-4961-3c5e-a901-474417970a32 | -17.18968 | -56.18605 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 44bc3253-8641-39fc-9223-f946fd7cd00f | -17.18888 | -56.19349 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 50969007-31c4-37a8-ae52-0c2e46be36ba | -17.18848 | -56.19722 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0029c036-ce19-3091-a177-73b353e95432 | -17.18457 | -56.18166 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| df8d3460-1fd0-3c06-a7d5-5598b0e69ca4 | -17.18417 | -56.18539 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3db1c70a-06ed-3356-88bb-933de1a7e280 | -17.17978 | -56.22627 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5d176758-25da-3e03-b4d7-de205a105622 | -17.17546 | -56.21457 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3b1c6e58-19b5-315a-922c-910b250631dd | -17.17467 | -56.22195 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8f7eb7bb-fc53-376d-a00f-d658e7d11f80 | -17.16996 | -56.21392 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dd437d13-61de-3718-bcde-2bf0233f6f06 | -17.16957 | -56.21761 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 13c3841f-65d6-38cb-811c-da2b4b134c7e | -17.16917 | -56.22129 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 98a11f45-3156-3fbf-8d9e-cb46f005554b | -17.16524 | -56.20584 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b2733a5-e599-3cb3-afbe-84fd1059c274 | -17.16485 | -56.20955 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 42f744f6-813d-3e05-84d2-ce0b9f62a2dc | -17.16446 | -56.21325 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7f1c55a9-14b1-3ae5-8131-dea94ee301fc | -16.89654 | -55.84399 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 713f2582-6847-3746-90c3-752323fe9315 | -16.89133 | -55.83943 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 62f33691-60a1-3048-91cd-18c5b269e36c | -16.89092 | -55.84332 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| ac6d57bd-8434-3662-b6d5-f2cc716dd3a7 | -16.89051 | -55.84721 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 6016f7c0-04db-301c-a887-76b50f90ca09 | -16.88009 | -55.83813 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| d74a1a8c-3487-3ae6-9176-3bc15b8cfb46 | -16.87968 | -55.84202 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0513db8f-15bc-336e-b9be-cc395afe6542 | -16.87927 | -55.84589 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 2d2f5cff-3ff8-32ce-a24c-96999de9f039 | -16.87886 | -55.84978 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 23f71f02-6750-36cb-9488-3ef95c0cded3 | -16.87845 | -55.85367 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| cadc88b2-6817-30ec-b104-aaddf4be1d8f | -16.87529 | -55.82961 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 641fdb8f-1052-3804-acd8-4bb83b30ac7b | -16.87488 | -55.83353 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 19c24ec1-ddc4-34c3-9911-b77ab4a4edc6 | -16.87447 | -55.83746 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9c477437-699a-3f33-826e-27170baa2ec9 | -16.87406 | -55.84136 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 43c3fc69-cb6f-36dc-bc06-bf8bb2ca6c5f | -16.87365 | -55.84525 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 08df974f-dcd4-367b-9a68-07119bab4312 | -16.87324 | -55.84915 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 20a5a5ac-71d5-3ea0-8291-b90ce294d905 | -16.87089 | -55.83815 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f95b86d1-40ee-3253-88c4-76fd44596e6a | -16.87045 | -55.84206 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| db36fe66-41fc-35f3-99f7-008246616239 | -16.87001 | -55.84595 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fe3ba252-1451-3b43-9d54-8fabfec32f02 | -16.86958 | -55.84984 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 78860d60-39a5-373d-9a3b-c6042577bfd5 | -16.86926 | -55.83287 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c9e12bfd-6292-3d1f-9eb7-c89beec15fa4 | -16.86885 | -55.83678 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4dcc0146-cbb7-361a-b83f-d5d6be471da6 | -16.86844 | -55.84069 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fe2a58a7-680c-3c3a-a957-f884516b2dec | -16.86803 | -55.84459 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 552d696a-1a5e-3825-9ba0-32753de11fe1 | -16.86763 | -55.84849 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| fbe250b6-7244-317b-8c5f-f0485eabc201 | -16.8657 | -55.8336 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e2c152e0-6a2b-3549-bdf4-9163784b3c70 | -16.86527 | -55.83751 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 491b66f3-72af-30eb-a25a-c8e6cbe34bed | -16.86483 | -55.8414 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b1c0f52-e208-3044-8f71-bae39b8ba6e6 | -16.8644 | -55.84529 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| acc8f6b5-c45f-3a55-992a-639509edef00 | -16.86397 | -55.84918 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2b8117cd-525c-3f40-92b6-aa5cc80f00da | -16.86364 | -55.8322 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README179.md)
