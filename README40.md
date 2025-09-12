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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 731765fe-2bc4-3cc9-b7fc-4a263101275e | -11.09338 | -48.41128 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbd07525-0f1e-3e38-a941-ea8e8d6ef0bd | -5.83128 | -39.65062 | 2025-09-12 04:04:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba5b6b92-5932-36d9-85d5-bafdc3aecbf7 | -9.65864 | -43.53151 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e277bc62-720e-30fc-b50f-abca57fed796 | -5.4973 | -42.6837 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaebf5ab-1dba-3ac1-b900-39aad02b518d | -7.4721 | -45.30169 | 2025-09-12 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cea2b27-874c-305f-b9bb-8fdfc79fcb6f | -9.04038 | -47.05005 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f9f6240-3bb6-324a-b46e-de041e35f18a | -9.71404 | -46.88199 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c937e36-6588-3a5f-baf2-74ced2b964fe | -7.56615 | -44.37434 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b199bfbc-ca10-3272-923c-47c0fd7cd8c9 | -7.55527 | -44.39213 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17dd5484-431a-38cf-80bd-7c18f4baaa09 | -8.5209 | -47.65542 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecbbe7bf-6a94-332d-850a-4e5ed9af5098 | -3.68864 | -49.5764 | 2025-09-12 04:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf4197d5-2c4f-3289-b2ac-bc35a6feb128 | -6.82344 | -45.65314 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18834815-dfe4-3504-bee8-0c79f0d47c6d | -5.69662 | -49.19936 | 2025-09-12 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 202ef461-4b96-366e-abd5-ff2d48f0d62f | -10.67854 | -48.66594 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9a919c7-4cf2-3033-8c7d-7897b87c117f | -10.21063 | -46.21906 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d11ec3f2-c844-34b5-966e-2133fce71632 | -10.84811 | -48.16377 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e721faa-65e4-3661-9c1b-40ddfda2d65c | -10.55444 | -51.49036 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c724a7f1-07bd-35a7-b28e-52a12ed06e69 | -7.24145 | -44.4217 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1383a1bc-8b2f-3a46-95eb-8aae4aa23906 | -7.04424 | -44.69022 | 2025-09-12 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0458ca99-e4ba-3783-b63c-0e10fce834c5 | -11.0943 | -48.40624 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54f05a49-7008-331f-89f6-873d1dbd707a | -9.03512 | -47.10602 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb03affe-e1b2-3444-aa03-b08fbc4b22fd | -6.10541 | -45.9381 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d42b38ae-3e8d-3cae-bd58-5e690ff1c9fa | -6.12067 | -42.95961 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bdb276d-4d27-39ec-914d-d7ea2bad968b | -6.59936 | -41.44923 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 616abeb6-21fa-3607-8aed-6c967929ed55 | -6.31791 | -43.4397 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce432322-4a9c-386f-a05e-5299048f7fb9 | -10.21593 | -46.24699 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f03305d4-691b-3c1e-b37e-fe11dc69930c | -12.10695 | -44.86953 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ca75975-009d-34ed-a7e0-6e78979c5bf9 | -11.67777 | -46.56438 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4de06d1b-4e05-3a71-a257-477638b60074 | -10.33884 | -48.80527 | 2025-09-12 04:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af1d4a2e-487c-3fdd-ba0c-1fc1edca4c51 | -7.40024 | -44.36376 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40fb6d4c-0100-3988-9a98-5ec86754b6e2 | -7.29694 | -44.35917 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 059e4baa-b0ab-3484-9176-725d441c01ed | -8.4209 | -47.26387 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99fd246a-6bce-3abd-91d6-06dd8ad11b2f | -6.30678 | -42.22459 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 42806d03-68a3-3057-a0ba-afade2c5ef1c | -6.41825 | -44.50533 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11b96eee-0de6-3d9f-9eb9-fe0079ec28e3 | -7.44929 | -44.4015 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2bd3ace-bf67-3189-8cdc-7e174a45d293 | -11.67582 | -46.57564 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ee84aed-07b2-3c71-9b29-594b9d745bb2 | -6.8079 | -45.64256 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a534a3-a53b-3f78-92d2-cde3e4d1d8af | -6.15625 | -47.27847 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a973cd10-870a-3267-ab1c-ecaf7deb377a | -8.41082 | -44.76146 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07cf5f98-961c-35b4-8a88-a5c9e79920ae | -6.59833 | -44.31497 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c311f48-b064-3bf8-8e12-d5ed4e480413 | -6.10471 | -45.94226 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9ca5a29-e83a-3f65-ae0d-c593e394169b | -8.89337 | -49.93314 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e421632a-a2a8-3f70-9039-719e4402ad81 | -9.05604 | -40.52239 | 2025-09-12 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ec6d48c3-9190-364d-9544-2f762480f5c1 | -10.12439 | -47.91784 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b54f409-6dc0-384f-8b59-348321fd7133 | -11.67293 | -46.62531 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c844d9-e2d6-38de-bfc6-2005e8c69baa | -9.03354 | -47.115 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cd01d47-39d8-3c54-83bf-996a2eeb8627 | -9.67694 | -47.5378 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9fb8f0b6-d00b-3c9f-be64-c324b6d903e1 | -6.29611 | -44.58625 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce006f52-f604-343a-900f-9f64a6ed5d6a | -6.6792 | -44.14868 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 30414a43-1b2f-38bb-92f8-23e6186acf97 | -6.21303 | -43.37501 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1547fa9d-670f-3d46-8ca2-f4630110f9d5 | -8.17931 | -46.11952 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2711e442-c135-3112-b163-b77536349ad6 | -8.48924 | -47.27318 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85943344-e1da-3154-8c14-d05e287150b6 | -6.32609 | -53.45699 | 2025-09-12 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b5f392d-fcdd-334a-baa5-2a7178968f83 | -6.68775 | -44.13257 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cb8940f-ed11-3cf8-9286-0a28f5cc0204 | -8.00012 | -39.79655 | 2025-09-12 04:04:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 365a3e67-8355-36b6-8b32-b1211d02c38e | -5.73996 | -45.59722 | 2025-09-12 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b80792a0-3a5c-3eed-9104-e5c62a0ecde0 | -9.95874 | -51.6922 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45d68919-72b3-3231-88db-2ca69737ab69 | -7.15037 | -44.34451 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb032cee-2697-329d-abc6-bd9f5adc30d3 | -6.67779 | -44.14537 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e4b630b-0f1f-30bd-8dc1-94ecb822a442 | -11.68601 | -46.57646 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8852e199-581b-3848-a7a4-aab76da1ea6c | -6.40748 | -42.60173 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d0e815e5-ba94-3611-a961-4adc21ee4d66 | -11.66949 | -46.59701 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d6d1030-14f3-3fa0-bd5a-04d2b15a8ac2 | -10.84492 | -48.165 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bcf82c09-7b47-3b39-bab0-059ae1f5ee30 | -6.83554 | -47.87446 | 2025-09-12 04:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7fb5ad6-42e1-389c-b649-7e0cd33a8ea8 | -10.13209 | -47.9124 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3edb9e-85da-3342-b57d-8fafdf1e7cb6 | -10.19391 | -46.19242 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c06ee64-5a98-30dc-b673-c8ba0b790dff | -10.5597 | -43.66578 | 2025-09-12 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a64cca4-bb1e-341f-abb9-36f8abab2dd6 | -10.39599 | -50.5007 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85eeebb4-29a3-3ebe-aa87-3ebb6d16bee8 | -10.21217 | -46.23494 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13d25a48-885c-3b99-ba61-6cc7fe047d80 | -7.84421 | -43.88937 | 2025-09-12 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61eb1986-d222-3cd1-9f59-142b7f06f80a | -7.84792 | -43.89001 | 2025-09-12 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb9531ed-d181-34b6-9e1c-73e7e255ce35 | -6.6908 | -44.12667 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84b98207-14d5-3063-b90f-b5f8df5366d9 | -10.16758 | -46.1725 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac612682-a6ce-321d-907f-d479f3d2461f | -6.63735 | -49.78719 | 2025-09-12 04:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad37a49-3be2-3c8d-9f78-2c617023f36b | -9.78424 | -47.38162 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 178f8a1c-1b8d-35d5-bc43-7c7d2997a8ac | -7.30366 | -44.38957 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1403fdb9-5d13-3c33-b3a9-e27fd3e58194 | -11.6778 | -46.59833 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3056d3c-5379-3d80-9d39-1877f432d4ea | -10.44154 | -50.61667 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53e5fa53-1757-3cd9-b266-30f38a2cf51d | -6.41457 | -42.60291 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17c3e209-568f-3a03-a3b1-73e35fd57b8b | -4.93646 | -45.59371 | 2025-09-12 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d086c8c-456d-3b92-8ac9-af2920fb13fa | -9.68894 | -47.54955 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c92e864-fecb-3bef-8135-8aa57a257d7f | -9.01825 | -45.7452 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a652c8cb-22f3-37f9-93a2-9c1b10d56a93 | -5.40597 | -45.92934 | 2025-09-12 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9672aa8-3973-3b1e-8236-225e6384b7e0 | -7.44836 | -45.00303 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 677fee8e-4a0d-32dd-a8d3-9f11bab1e908 | -10.88578 | -45.59249 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 762ca1eb-b5c3-3ade-9596-81dada0cd19b | -10.37822 | -50.50463 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bdbf5fe-3676-3ed2-9d55-b9aae9595661 | -7.84784 | -45.3946 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41c6cf3f-8816-32d7-8ca8-d3f10efd3024 | -3.68362 | -49.10563 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f68292-dcdf-3ea7-8052-010e1616836a | -8.02384 | -45.40986 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 2ff8003e-8e12-3249-b8b9-c210c084f1b6 | -10.34945 | -50.53641 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5025992-c1ba-3f09-b337-5f80ab9fb629 | -3.68983 | -49.10293 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06495daf-ad58-3fa7-80e9-b0f7031a32d7 | -6.20107 | -42.49633 | 2025-09-12 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e78f7d37-0b0c-39e7-b971-a5038222a3d3 | -9.06583 | -47.03595 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d4cd89f-a8e3-3f8a-9a08-2462207d8574 | -5.51924 | -42.69048 | 2025-09-12 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 741a6c9b-f77f-3879-a0b4-df8f77c1850c | -8.18016 | -46.10613 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f133dbb0-00ef-3ddc-aeb9-eaafb685bcfd | -9.03539 | -47.07832 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 685ade53-5777-3cc3-86cb-9dc4467696eb | -11.14702 | -45.2399 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2fc57ee-c818-3df4-ba41-b31bb44f90a8 | -5.96474 | -44.72588 | 2025-09-12 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 520701cf-8edf-3c2d-97e6-3256f6936159 | -8.95963 | -46.07937 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a72c0ae-693a-3480-a80f-6807b5cb40e4 | -11.67424 | -46.54713 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README41.md)
