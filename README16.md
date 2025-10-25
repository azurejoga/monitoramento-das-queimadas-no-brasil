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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07102fb8-7566-31f7-96fe-ff76954bc43e | -6.3598 | -44.27297 | 2025-10-25 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ee13c94-5de8-333a-99b6-66b3d1a455d3 | -6.25685 | -47.02987 | 2025-10-25 03:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f2f1bed-17ca-323f-87f9-00707d94dbe1 | -4.55407 | -46.68563 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9097303a-bd19-3835-9abd-051d4c4d4881 | -5.68362 | -42.76482 | 2025-10-25 03:57:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56fa8a15-4f06-3006-a143-307508b5b6a8 | -6.79185 | -46.46465 | 2025-10-25 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d356c39e-15d1-3049-a7eb-52f2f504c04c | -3.83269 | -50.19473 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a5e34ae-312b-38c6-ad83-1604f02e9647 | -8.60389 | -44.81771 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1d738a5-d6d8-3513-925e-a413a57bdd43 | -6.10579 | -45.85094 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da98be48-4dc8-3415-bc92-d56b23e04600 | -6.80002 | -45.4243 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff82c8a7-51b2-370c-89a0-c53acdc080b2 | -5.54556 | -41.38817 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de482597-fecb-35d8-a68d-535845c67e2f | -7.2563 | -46.33096 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 740a4f62-fa77-3e8d-be16-2521978ced83 | -6.13681 | -42.45338 | 2025-10-25 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4b90242a-f65c-3c01-a977-5de6baa615f1 | -4.82637 | -50.92851 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95be8572-52ea-3e9e-b913-8cfcade10633 | -2.86195 | -50.71686 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359f471c-1da7-3ac3-beec-9d0af89e5804 | -3.43615 | -50.26425 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 430ca0f9-6bc4-349c-8b6a-9ad72c62b87d | -4.99846 | -47.76519 | 2025-10-25 03:57:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b57db740-f31d-3350-a26e-a10d4d0fbd83 | -7.98983 | -47.38302 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e561bfcd-6e33-3209-abb8-544cb85e478c | -4.22687 | -48.61261 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e1c19e3-892b-3504-81ca-148be7c08be5 | -6.89705 | -46.36584 | 2025-10-25 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d090ea26-6b7c-38e4-a122-94b66abaa67e | -5.41436 | -46.00627 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 616b90a6-1ec8-306d-a729-4963fabc9482 | -7.14899 | -44.12492 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 858f211c-9b5f-3c88-b721-243ab86bf243 | -6.49856 | -43.90764 | 2025-10-25 03:57:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 779e1db7-97c1-35c9-a68c-d6d9f77c96f3 | -5.93261 | -43.36493 | 2025-10-25 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| de435c56-2e98-3282-97f3-4cd694acbc37 | -7.64723 | -44.57318 | 2025-10-25 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf896b39-3545-3468-97e6-0c9619be09fc | -4.28854 | -48.26689 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bce477a7-f55d-31e0-a95d-fb78656ced82 | -6.79542 | -45.4236 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be4820a0-11d6-325b-bb7c-9dc5a2f5ca6f | -6.43275 | -42.0265 | 2025-10-25 03:57:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af4bc02a-9839-3eaf-b7bb-fc1a33f69909 | -5.45618 | -45.41146 | 2025-10-25 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa07d24d-d6a0-3820-a06b-b4def753d870 | -5.44537 | -40.88585 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 003ca30e-5e00-385a-b63d-a7905a1b0e4f | -5.81927 | -40.80617 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44d9aba0-14a2-30fd-845f-2e0bc9b377cf | -5.69783 | -49.3224 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11b35c52-17c2-34a9-b4f3-be41892f375e | -6.2201 | -42.54417 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1abbae2e-b6c2-3228-bff1-8eeb9857e9c3 | -5.70417 | -49.31647 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecc65f39-da31-3c8d-abb8-bfe69ab5ea95 | -4.25571 | -44.58519 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3a01fd1-b233-3c9d-8c71-24e90cf3e8eb | -2.81714 | -49.14651 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b28dfa-b6df-34af-905c-46ffdde07156 | -6.59449 | -42.07365 | 2025-10-25 03:57:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1368a8b3-a487-3450-892d-352e82c6b40d | -7.5856 | -43.57718 | 2025-10-25 03:57:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2475796a-9e31-3af6-a791-ae6f76ec7cc0 | -6.21864 | -42.54116 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7f9d6c7-99fb-3038-a968-43789b59101a | -5.47555 | -40.87922 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0887bc17-1ccd-3bf7-9ffe-a1cc9ba6d9be | -6.60252 | -42.6573 | 2025-10-25 03:57:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8eb1c9ce-ddd6-38f1-b2f3-1642ceecf12e | -2.72969 | -49.16702 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3182b123-2899-3bad-aead-a11d8f4afc25 | -4.60801 | -47.02453 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906235cc-3e8c-3225-b088-57678f93f76a | -6.90916 | -45.1721 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5ce9561-a3f8-3eb1-b2cc-f82204bfd922 | -8.59747 | -44.82936 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6bb8b00-4d22-31c2-82b5-23d50cb55be9 | -5.93185 | -43.52105 | 2025-10-25 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 516522fd-04a8-31a2-b0fe-dd2d14af697f | -6.95854 | -37.51464 | 2025-10-25 03:57:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47412d41-608b-3053-817c-67b2fcb25641 | -6.92421 | -45.16546 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc0ff396-1052-3b74-83b6-429a3d6570a4 | -6.54486 | -41.57735 | 2025-10-25 03:57:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5438001a-cdf1-37c4-a37c-55ec7c5568a8 | -6.91445 | -45.16827 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe11f6e6-f949-3d6b-8a1b-9e4efa048dce | -2.893 | -49.1728 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1bd5a6c-1457-3930-9fa0-5b713bec18ef | -6.06805 | -42.15123 | 2025-10-25 03:57:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b226a373-c1ea-37d2-a253-ef52ba787902 | -4.25268 | -44.57534 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 956f2657-b957-39cb-9795-214c3248998b | -4.83198 | -50.93618 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e61bad0f-0b30-35e0-afed-22429b9e9769 | -6.8079 | -42.39532 | 2025-10-25 03:57:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5cb5b428-a1e3-3412-97fb-57c0b2d00ea6 | -4.60019 | -49.59059 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b5a5aeb6-b83e-3c4e-82d5-050f1976be3a | -6.28971 | -39.53874 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6a7a72e4-da37-361f-a10e-aea5d1f23f8c | -2.72342 | -49.16591 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 875b756a-bd7d-3d88-ae5d-9dcf1dea69eb | -5.64794 | -45.97285 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77176fb8-06dd-3d61-a3cf-ff139c2d1139 | -3.11691 | -49.10936 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b32b248-c901-365f-95d0-535b602c2d2c | -6.81303 | -45.43123 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc13cb88-4873-30d0-8d11-53c586d95e3d | -2.71969 | -48.34822 | 2025-10-25 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 964fd9d3-ff06-3612-bcf3-bf6df8b77ec6 | -3.98712 | -50.52037 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94007e07-ca5d-3727-97c1-86836b03b78f | -6.9663 | -43.49904 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aacf0c08-b8cf-30a9-b705-9285b8e4b4dd | -3.40676 | -39.1692 | 2025-10-25 03:57:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6216c511-1ee2-3444-a848-29618756c2c0 | -5.41616 | -46.00817 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf6df64-58df-381e-b9d0-99c2a79568ee | -5.54122 | -46.52871 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ce109c4-eda2-361b-a0de-f51e51dc5097 | -6.73806 | -44.15211 | 2025-10-25 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 883657fb-3862-3b52-836e-71809268f721 | -6.55224 | -43.23261 | 2025-10-25 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8af5848a-cd87-36ba-aa42-52f1e6186048 | -8.14475 | -41.50587 | 2025-10-25 03:57:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20efbd6a-f64e-3ae4-95be-ee9d3ec2ea27 | -7.03352 | -43.93808 | 2025-10-25 03:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39f0a747-4eee-3cea-9d04-5ec6c6dbecc7 | -7.14879 | -44.12783 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b053dc61-6686-3217-ae24-9cc07d9d9b83 | -9.15081 | -45.82959 | 2025-10-25 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c0c8460-9af9-32c0-9c49-b9bb8053e873 | -2.86774 | -50.72443 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1510233-6d22-3bb7-9c09-0b15fdc38287 | -2.80459 | -49.14445 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ddce2888-4098-31fd-be59-1b3a628d7ec0 | -4.00063 | -41.02262 | 2025-10-25 03:57:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| def3e27d-33f7-3265-99b5-241e549924f7 | -1.30221 | -49.35118 | 2025-10-25 03:57:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04a2c6b2-3822-361f-b06d-5685cb77cb19 | -3.83169 | -50.20031 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d32fea4a-8bae-3532-8cb4-8a05e99aa30f | -6.80801 | -45.42907 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fec0d2e2-0ab4-39c4-8758-c23a779a621a | -6.22474 | -42.5399 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 962f58c9-6f1a-3aea-a67f-d5ac56eaa2f9 | -5.46849 | -40.87787 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f17b1a4b-d01d-3cad-80f3-0ba9fdca9dbb | -6.75899 | -44.20781 | 2025-10-25 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a0fb1bb-3e13-363b-aac2-2affd32d7da0 | -7.79496 | -45.39758 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d004f93-c762-36bd-b330-5c3b804b47b3 | -6.31788 | -41.8718 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b98a226f-9870-3492-857e-82661c94d0df | -6.41992 | -46.1852 | 2025-10-25 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2d9ee24-0bdf-3957-a567-044f64a76aaa | -4.86908 | -47.5311 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f1c7a82-47a7-3b0f-b035-965c76b868d9 | -7.16026 | -45.8404 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d79c8fa3-9841-31e5-8c54-68042d8740ce | -7.79046 | -45.39675 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d5d1154-d8f5-3171-8348-57ba9067e975 | -7.15435 | -44.12058 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c1a9166-c147-37cc-a1a2-d5779ea0ab43 | -3.82509 | -50.19925 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36decb4b-fffe-38e8-8fa0-b219dff8b83e | -6.0674 | -42.1532 | 2025-10-25 03:57:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60f92be8-d65b-3d54-84a9-13c27bba080c | -4.25119 | -44.58442 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a96d0a0-6669-3c79-8831-5f51a815d4c9 | -6.09189 | -39.19489 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc555818-a362-34a8-9ad4-30384e5f26a4 | -3.40138 | -42.4799 | 2025-10-25 03:57:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09f1d91a-faca-35ce-848a-07475ebbf40a | -3.99035 | -50.52299 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3eeed8a-bfad-3a47-99e6-c2674e4888dd | -8.13664 | -47.04224 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69306736-bd85-3b7e-90a3-a36acb6a5393 | -7.78546 | -45.39304 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc606786-83ef-3fbb-8b2d-b6e3363d8a14 | -6.9651 | -43.50611 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 513fb7ce-4cab-3bb9-b317-1c3d0c341102 | -9.67849 | -37.09006 | 2025-10-25 03:57:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 339c388e-66a7-3e21-98bf-92baaa7cf52c | -7.85053 | -40.90215 | 2025-10-25 03:57:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d84f489c-efe1-31ab-a969-47abdd03d7e1 | -5.64308 | -45.972 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
