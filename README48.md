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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78da200e-d312-3a07-842f-ab4d1dca1c4b | -2.03554 | -46.37331 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8d10bf3-6f70-397e-b382-0bf6dd6b269f | -2.23009 | -48.36945 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10ccad3-2108-3f53-a5f9-45baa0886d40 | -3.66236 | -50.6066 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb445403-59dd-3b10-a421-ba9ab3a50f17 | -3.13293 | -45.89713 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c469d9-4471-3c6b-9b84-0b15438253d7 | -1.47321 | -51.1338 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21659fd3-bd54-39b2-8131-94ee30ededf3 | -2.64546 | -46.55689 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c965b0ae-c816-3e03-93b6-e2f57499776b | -2.60692 | -46.2604 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5adcf4ab-f4f8-3c3c-8d7b-f62a061d801f | -3.94264 | -46.40707 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b8aa1b-edcd-3473-a7eb-05345f804846 | -4.80943 | -44.48172 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9c340460-205b-316e-8912-c704efd84ca6 | -3.53089 | -50.2534 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1b50f768-8a00-3404-a165-8ec64f1cb0ab | -6.94752 | -42.76077 | 2024-11-17 04:29:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| adf216e9-8c74-314a-860d-c723aa4814b7 | -3.68988 | -50.11386 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 91005041-5902-3fef-a60a-f07878037659 | -3.93967 | -46.70914 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00f09df2-aab2-3017-93a1-4971cec92d27 | -2.15809 | -48.95391 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6326047d-c1c7-3ec0-8d3a-4300f2bf2433 | -3.9914 | -46.40028 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0786646c-5ebc-3dc9-9ab3-1e7843b7b778 | -3.897 | -46.48238 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c4fcc07-a887-3be3-9469-840004cb0227 | -2.62326 | -48.56654 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 039e90db-7834-3cc8-93ea-6e696e13118d | -2.64709 | -46.15627 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1ee440b-d04f-3ff7-83be-56d008f97e0e | -2.15447 | -50.69999 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0eb5dc57-4cdf-395c-858c-286527c77298 | -1.49376 | -47.3979 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50446095-60ad-3961-8ab4-7be627ecb4ed | -2.37467 | -48.91479 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c37f6ed5-d3b8-3cd4-8465-0c80fba8aba7 | -4.54026 | -45.2562 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be830e04-4297-3698-9e70-a5d50205aa18 | -1.32667 | -51.8648 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 407933a8-a96d-3717-b2f8-69693f3ecde9 | -3.57708 | -45.68367 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43308efc-6fbc-39e0-97d0-7e714284f427 | -2.69827 | -49.28766 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b2da242-2391-3dc0-889b-18cf39a94b10 | -2.59296 | -47.55954 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89e2518d-b9a7-32b8-bf74-d3965b722bf0 | -2.58138 | -47.56834 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1176378e-ec09-3961-8fea-c09a76e34e48 | -3.94147 | -49.00592 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3d54c64-d11e-330d-b952-0ca079e5e68d | -2.84519 | -42.88581 | 2024-11-17 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b81958f-83de-37d1-9e52-bc2a72993308 | -2.67531 | -46.21438 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ce5057f-a09b-346c-951a-809675f95104 | -2.53675 | -46.21041 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c780455-1d9b-368f-85a7-94317f8601f8 | -2.94422 | -48.32721 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a30112-b89d-32b2-9522-705296b62868 | -3.51947 | -50.25579 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 714901ab-960d-38f1-9cb2-6d491e41473b | -3.81391 | -51.37824 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fb76a6-8a96-37e7-81eb-b1b23eb5f774 | -2.14501 | -46.82372 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385ee211-1b0b-3943-b938-5f44c6aef260 | -2.47146 | -45.67214 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88753661-919b-3889-950d-e50e8287809e | -5.27249 | -44.90901 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 063dcdfb-b5a1-334b-b98e-213836588341 | -4.2037 | -45.62298 | 2024-11-17 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f7bc5e-abcb-3206-9711-bc30e0d150f8 | -4.54157 | -45.25279 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 683d8cdc-4b46-3a43-9656-1fa9e8636396 | -4.12654 | -46.94727 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b697028c-cab3-3927-8dd8-dbe0d38d2318 | -2.65538 | -46.21131 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91eeb58f-975e-39af-ba79-49975dd37c4f | -2.62441 | -48.55933 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ac5c4f62-d254-3d04-a59f-7fa625c43835 | -4.55342 | -48.0133 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e6bca6-0d05-3a33-bae8-73f6ffdeb6af | -3.97442 | -46.70388 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4c9953-fb20-3f28-8de7-a38fcd192494 | -1.20386 | -51.77187 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69a20a7d-aca6-389d-bece-8f69ec9bcdfe | -2.63639 | -46.83019 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca494b96-d32f-37fe-9829-0ce509b2c889 | -2.62264 | -46.83157 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce1a2983-0632-3865-8e74-7208a48c5e8f | -2.65596 | -46.16477 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 875590d0-e84d-3f7f-a3a6-4ab5091b8757 | -2.24622 | -46.84952 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 010bc9be-80e8-37ba-a0a6-7eeb7b1eafcd | -3.091 | -51.31796 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bdd5c0a-448b-338d-880d-07e7e656cbb3 | -4.47279 | -48.11406 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1f8a031-0d24-3245-aba8-eab071277737 | -2.81051 | -52.91731 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 158ab0eb-85e3-336f-a9fc-fc4a613db427 | -2.12854 | -49.50238 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb2edd1-52c2-33e8-a812-514833ad24c3 | -2.15841 | -50.70737 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa1b8d6e-7888-357b-87da-cfde907d6d11 | -6.87408 | -41.92743 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d50dc846-7a9c-3e2a-b307-f17a0aa78cd3 | -0.9002 | -51.95056 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e82a90a1-39ca-3b61-b8f5-999a37006648 | -2.74644 | -46.08624 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07159462-b7d5-3aeb-9463-3f9f37f0e281 | -3.04317 | -47.97894 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d1022ed-e044-3cbb-ade2-b5b6ebe34430 | -3.15434 | -46.60444 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c46bbc-7c02-3687-8e8f-ed3472723f3c | -4.688 | -49.62711 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb64d2ad-3fd6-3887-92e5-27f44edfab9c | -4.29055 | -48.62146 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0684f05-03f4-34ca-a4c2-42da0fbda0f0 | -2.51257 | -46.27772 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a08f291-ad91-373b-9766-67f235556065 | -1.48218 | -55.35044 | 2024-11-17 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5ccc4d58-b52e-3fcd-af99-3fe115c1928f | -1.4943 | -47.39444 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c8139ca-17fc-33d9-b9aa-10714eab2f18 | -3.09733 | -45.97113 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b804f53b-34d2-3a17-a4ba-be1915b83dcd | -0.79858 | -51.48826 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 996b9ef8-36dc-3c84-b527-87f0647e0def | -3.86366 | -46.43442 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0d6c6a0-5240-329e-8403-d00a586d6137 | -1.214 | -53.5628 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1333b85-d8bb-38d8-aee6-73720e92d1f9 | -2.08462 | -48.53543 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02346665-42c7-3bd0-b18b-ff37a79d07ce | -3.73866 | -44.53104 | 2024-11-17 04:29:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c04a9a82-c4bf-3e76-820d-909c8dfe8e39 | -4.55783 | -48.00689 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 7620a2d5-b8b1-38eb-ae69-6519f3679c14 | -3.11237 | -45.98427 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57250cfc-5ee1-3f15-9514-d7abec56e03e | -2.29909 | -49.13002 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b54088d5-a1da-3ebd-bb99-13028eac0d86 | -2.22425 | -46.83603 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 624fdd57-db75-3986-a0b9-dd91abe5e760 | -2.58801 | -47.56937 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8482f2f3-b072-38ab-a449-028c10846b3e | -2.16424 | -48.76101 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3795e9d1-2db9-36e5-9dca-35347e8967cf | -3.53367 | -50.24866 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78bd1868-53d3-3fba-8b90-5865c737a71d | -2.18982 | -48.26443 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50203ea-77d4-362c-849a-f67ab989aa0c | -2.29682 | -49.12191 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca17ac49-02be-3539-97c8-8a53665d4c7b | -2.67701 | -47.88889 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1376a373-1700-3626-826d-78ff8444e440 | -3.3516 | -46.42982 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdbaf06f-6382-3ad6-b212-85846cbde9f4 | -2.65381 | -46.20007 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e477ee8-fc87-3f33-a60a-470bc5748837 | -4.10651 | -46.88052 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64d8f4b5-faf6-3708-89cf-156c53fadb1d | -2.1201 | -50.69913 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 301665b0-2661-3136-9449-adb77ad1b75e | -3.69803 | -47.68359 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ca3c5cc-ee80-3d72-a728-ac0db26bc750 | -3.53299 | -50.25281 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36bf9a95-4a69-3e92-8b4d-22f72ad200c9 | -2.19519 | -49.5405 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6240e09b-e4ce-31b3-8441-6c159419cc7e | -2.13144 | -49.50686 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41c5c9eb-ae2d-3c3e-834e-e1a5ba19324b | -2.71146 | -46.07008 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bcdc219-8119-3afb-918d-5e61c737a961 | -4.24863 | -49.19263 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cdaef93-6542-39f3-afa6-3d4dc8d6163e | -2.07445 | -48.53383 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edb269f6-d483-3cb6-a11e-b94a645ae9aa | -2.17504 | -48.51245 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78210bb-bb91-3908-8284-6d35694412a7 | -2.16681 | -49.25786 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda49b5f-07cc-3506-84c3-d58931682000 | -3.25177 | -46.52398 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d86279-70e6-3a3c-a6a5-48c0ae3082ae | -3.51587 | -50.25525 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c6b79c1-9fea-33cb-bff1-6b3bea39fcf7 | -3.78483 | -46.67825 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed26f480-19f3-3db1-9c5d-4ac8e8d057b2 | -2.26644 | -46.58938 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 641e3cbf-1db3-3b7a-b271-d3bf6ae76b0f | -2.62168 | -46.18799 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 290528a4-c0a3-3f8f-9b5b-a2de97a7a56b | -1.13347 | -51.68764 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e8b42f9-726b-3823-aa30-94ee730e4a2e | -4.39399 | -45.27703 | 2024-11-17 04:29:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README49.md)
