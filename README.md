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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a9d356e-26c2-3827-82bf-37705ecdfd9e | -9.9548 | -36.0125 | 2026-02-03 00:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 81361c1b-4722-35e6-a3e7-3347dbe47130 | -10.2177 | -36.3703 | 2026-02-03 00:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 1c408bff-8262-3cee-a8a7-4be427eebf82 | -10.1984 | -36.3738 | 2026-02-03 00:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 4adb7408-8386-3bcb-8a05-a90d2ede5c9a | -6.4089 | -35.0706 | 2026-02-03 00:40:00 | GOES-19 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| c8edd152-db8e-3340-a610-cd7e4c1e6a44 | -1.57611 | -53.99096 | 2026-02-03 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 06cda0a8-43f8-3ed7-8780-cc55b3dfa633 | 0.53783 | -60.47163 | 2026-02-03 01:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e2d8fa5-7a2f-3bb3-82fa-f667e96accca | 4.36435 | -60.35666 | 2026-02-03 01:11:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24feace0-cc09-3e4f-89ba-25de245d947d | 3.42355 | -60.65289 | 2026-02-03 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27c2b504-e3ee-3930-aec5-70eb8c57ad97 | 4.36027 | -60.95558 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 87649326-3770-3c10-b98f-092d0f4ded25 | 4.35893 | -60.96537 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3b77cd3b-1509-3584-ba73-5b915cca27b2 | 3.40889 | -60.76152 | 2026-02-03 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cfe8e6d3-4231-38ba-8ab1-8747ffffdfbd | 4.17584 | -60.95662 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6fb6336b-1245-371b-a9ed-96ed785a6af3 | 3.4049 | -60.72092 | 2026-02-03 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8543aede-cf47-3288-a89c-1114109dc87a | 4.08011 | -60.70496 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2a2e555b-1234-3078-9eaa-f3492e4ac24a | 3.89771 | -60.96882 | 2026-02-03 01:11:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac832b52-01d0-35a1-a9b5-8cb041f9e22c | 4.36678 | -60.97681 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dd7f63a5-0fee-32ac-8fa0-6f68c185dde4 | 4.07874 | -60.71507 | 2026-02-03 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2b0044ba-383e-347f-b9a0-fa1f4772d324 | -10.1984 | -36.3738 | 2026-02-03 01:40:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.7 |
| f755ba85-f059-37d1-92f0-bd4f8d62a456 | -10.1791 | -36.3773 | 2026-02-03 01:40:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 172.7 |
| a12e589c-a4e9-3e09-9b92-70d2af16012e | -6.98402 | -35.05516 | 2026-02-03 02:47:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 068bd825-aca8-3a1c-8815-8eb467feded4 | -6.98978 | -35.06344 | 2026-02-03 02:47:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 152d749e-065d-3e3d-b614-a09cee15bdf5 | -6.98529 | -35.04853 | 2026-02-03 02:47:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| e79f2afc-849a-3548-be25-db68d26cc8b7 | -6.99107 | -35.05669 | 2026-02-03 02:47:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| cf6f87ea-87d6-3202-b270-7a26940089ee | -6.99236 | -35.04998 | 2026-02-03 02:47:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 385ca9d9-b7de-3484-bbb2-e9fa07fca25b | -8.30526 | -35.35342 | 2026-02-03 02:49:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3bcca827-f592-3b73-a69b-51594ed6dc73 | -8.36339 | -35.39367 | 2026-02-03 02:49:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 50da8b49-2b71-3fe2-9e57-65aff6b522e3 | -8.36191 | -35.40129 | 2026-02-03 02:49:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8a5ce4c-a8b5-3cb0-9a9f-f1a545398b94 | -4.7899 | -40.54877 | 2026-02-03 03:36:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab496058-84d8-3c8d-bb81-b85d701c4ccb | -5.09338 | -37.55124 | 2026-02-03 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 34904d6d-9a6a-3280-ae42-810e25bf76b4 | -4.66515 | -40.56189 | 2026-02-03 03:36:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f59a7d26-9d04-3f79-992b-bcc60c5512f5 | -5.09324 | -37.55282 | 2026-02-03 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81c7c21f-79bd-3a6c-bc1c-43f9ff3ed3d5 | -5.88998 | -39.29795 | 2026-02-03 03:36:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1bdf67ed-d5cf-30bb-95e8-4011a291bdda | -3.27665 | -42.38304 | 2026-02-03 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea0796ea-b4c7-3bee-a364-c7692c191615 | -4.56491 | -40.02579 | 2026-02-03 03:36:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99b2cec7-4cb1-3af0-9886-b3f5a7b96567 | -6.05256 | -35.42929 | 2026-02-03 03:36:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fadf060e-c91d-315f-9d7f-238b17d48890 | -5.88752 | -39.29383 | 2026-02-03 03:36:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a91f69e8-85db-3f2f-a13b-e34ec978420c | -5.55776 | -39.54612 | 2026-02-03 03:36:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d3cfcbf-7c8c-3955-9e41-1250b6a83460 | -3.2707 | -42.38549 | 2026-02-03 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b3dd230-ae88-30d9-9f95-9dc09b84ab05 | -5.23463 | -40.86929 | 2026-02-03 03:36:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| abbc299c-ce03-3f2f-9617-68b4a806cca2 | -4.39037 | -37.94792 | 2026-02-03 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7382fd53-a3b3-350b-9de9-610e82ee9ae4 | -3.27128 | -42.382 | 2026-02-03 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d38c20d-2798-3e1f-8f38-8bce9c288d30 | -5.11253 | -40.50634 | 2026-02-03 03:36:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aec66769-48c1-3a33-a8d8-c1ff1aed443a | -4.36582 | -37.90005 | 2026-02-03 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d4097c8-906f-33fb-b5b7-297f9b3cb220 | -6.58793 | -34.99695 | 2026-02-03 03:36:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f104496-3183-37a4-b3d2-148d9f7102c3 | -8.8375 | -35.72584 | 2026-02-03 03:38:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d88ccbee-13ac-3801-b29e-63b97b2f1c55 | -13.53337 | -39.85272 | 2026-02-03 03:38:00 | NOAA-21 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dddccff7-2bf4-3754-a2d6-81715af33487 | -8.30502 | -35.34908 | 2026-02-03 03:38:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b5e38ae8-02e1-3e30-94b1-7467b02ea64b | -7.05383 | -35.93547 | 2026-02-03 03:38:00 | NOAA-21 | AREIAL | PARAÍBA | Brasil | 2501203 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b2f29d95-24db-3e00-8260-e6fee52fca4f | -8.84087 | -35.72635 | 2026-02-03 03:38:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4849ae67-665d-3286-829a-5551ce4fe159 | -6.06254 | -43.73992 | 2026-02-03 03:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b973067b-8bb8-301c-b0cb-a0367440dfd2 | -8.55381 | -35.70552 | 2026-02-03 03:38:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f41d754-a955-3fa4-a9c5-e7d0b805673b | -10.11349 | -36.1905 | 2026-02-03 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ae0d3c48-2e05-3642-9a4e-de02ea0a84b6 | -10.11408 | -36.18684 | 2026-02-03 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3d94f78e-5d25-3f06-a40b-cbdb45582a65 | -7.05323 | -35.93921 | 2026-02-03 03:38:00 | NOAA-21 | AREIAL | PARAÍBA | Brasil | 2501203 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 507e5eea-de00-34fe-b375-49d614cd0389 | -7.49615 | -35.14964 | 2026-02-03 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 817d3333-dc48-33dd-ba9e-256d910e4ec6 | -10.0933 | -36.29275 | 2026-02-03 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 8a9797b5-2409-35f3-a887-50588e54867d | -7.49672 | -35.14608 | 2026-02-03 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 818e4b52-500d-35ea-8254-32013ea160dc | -5.96191 | -43.53534 | 2026-02-03 03:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 633af778-b2f6-3a0f-96e5-8faf6e83062a | -7.49282 | -35.1491 | 2026-02-03 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ff7b3224-1438-3f6d-8395-dc482b3d1f22 | -11.55129 | -37.84104 | 2026-02-03 03:38:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 00473706-84f6-3618-b762-212eed8f9584 | -12.50791 | -41.5956 | 2026-02-03 03:38:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| faf4a991-91d7-3b76-9bd5-be5e578c7300 | -7.05666 | -35.93976 | 2026-02-03 03:38:00 | NOAA-21 | AREIAL | PARAÍBA | Brasil | 2501203 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 005cb9c7-c22b-355f-81a1-b29c79b13d36 | -9.42343 | -36.10468 | 2026-02-03 03:38:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3946191d-7114-3afc-82d3-607db2336b4b | -5.97959 | -43.5655 | 2026-02-03 03:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bebf0ce-b2fc-32c1-9f9f-d2ad5cf06723 | -6.58626 | -37.49973 | 2026-02-03 03:38:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4aa16d0c-5b0c-3dfb-8274-36d12472e87b | -10.0961 | -36.29693 | 2026-02-03 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 437b6fde-6c43-30e7-b8f7-703299da3e7f | -13.38883 | -40.05161 | 2026-02-03 03:38:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 401894e3-3be4-3eb3-ac30-fa8fe88d7d3e | -11.77047 | -37.6157 | 2026-02-03 03:38:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80a129a3-7f51-36e6-a13c-f4f21e39126e | -5.98027 | -43.56163 | 2026-02-03 03:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb081403-fae2-34c9-995a-79da27de8268 | -10.79912 | -44.48589 | 2026-02-03 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7864ecc-1227-3f43-a3f9-868a85dca300 | -11.14025 | -38.36987 | 2026-02-03 03:38:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a5ad7c7-f90f-3c34-bdbc-3fab4942652b | -9.51939 | -35.99251 | 2026-02-03 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a62ddf6-824b-319b-83c8-e394dac46298 | -8.67603 | -36.27182 | 2026-02-03 03:38:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2431480a-2382-3cfe-9621-92475e694cf1 | -7.86727 | -35.27533 | 2026-02-03 03:38:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 007ec289-abf2-3cec-9661-fd08cdeb46ba | -10.79982 | -44.4822 | 2026-02-03 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ca7550d-12e0-3dc1-ada6-ca37da324079 | -9.51602 | -35.99196 | 2026-02-03 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cb71fb2-e5fd-3186-ae80-42528d281c23 | -6.06322 | -43.73608 | 2026-02-03 03:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb298c2c-f4a8-383a-b64e-2fa92f646b27 | -8.36395 | -35.38769 | 2026-02-03 03:38:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 832d7737-c859-34c5-9d56-7259fb31a965 | -8.36338 | -35.39129 | 2026-02-03 03:38:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 37161bbb-3232-309d-8cb7-b1df50c1f313 | -11.18779 | -40.28184 | 2026-02-03 03:38:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7510a492-3cc8-395e-b085-b81108664d66 | -13.36203 | -39.90306 | 2026-02-03 03:38:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e76b17dc-e09a-375f-b8ab-6454ba5787ee | -10.18011 | -39.05239 | 2026-02-03 03:38:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3b5889ec-3295-3d88-9450-d3ab9abaea05 | -13.3581 | -39.90271 | 2026-02-03 03:38:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0b868eeb-4156-3596-89ad-303515eb7008 | -10.09669 | -36.2933 | 2026-02-03 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 948623b9-a087-305f-b977-bafa3e34f87a | -19.0507 | -40.57091 | 2026-02-03 03:40:00 | NOAA-21 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc495a1e-e6b1-33d8-9ef8-b93117e6b6ee | -17.66822 | -39.20451 | 2026-02-03 03:40:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31c01e95-1129-3a65-9ace-bd77b8a9e5fd | -17.66786 | -39.20744 | 2026-02-03 03:40:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7e1af7ad-f544-3279-8088-ba26e99edfcf | -27.65067 | -51.03759 | 2026-02-03 03:44:00 | NOAA-21 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 39bdca98-8306-3bb4-802e-abb47311a297 | -28.17078 | -50.77057 | 2026-02-03 03:44:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ddadaa1d-d352-321a-b279-03e5cd2ca51d | -28.17179 | -50.76651 | 2026-02-03 03:44:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2f8349d1-e760-3d42-84a0-e77ea49cfea7 | -26.5159 | -52.19401 | 2026-02-03 03:44:00 | NOAA-21 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 801fb1c1-b15e-3b2a-acfc-c0c55e53ef6d | -2.50278 | -47.81927 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e2abf732-bcf0-328f-8075-6beef9bd08fc | -5.46835 | -39.12096 | 2026-02-03 04:06:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3aec0aaf-1250-31d5-8d28-1be8fdd5724f | -4.92432 | -44.05124 | 2026-02-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16ebef12-370f-3609-a558-de20269cc384 | -5.09168 | -37.55307 | 2026-02-03 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1593f37-490e-34d9-9a62-7d2e520ab1e7 | -2.85089 | -46.71897 | 2026-02-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6069d5c-961a-338d-990b-3ebb3db9f30a | -2.40388 | -44.86631 | 2026-02-03 04:06:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79190df2-ae87-3ec3-8de5-cdaabac62e96 | -4.7916 | -40.55062 | 2026-02-03 04:06:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 61ab3722-6a18-3cb3-bd8e-d7c6a89dc2cd | -4.92045 | -44.05056 | 2026-02-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe37b4c9-fe96-3b30-9c32-603e44ee5c24 | -2.50314 | -47.81919 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README2.md)
