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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37921428-177d-3ace-a042-188f0a5ec118 | -8.5581 | -46.2611 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| cf9fd85d-e6bc-3e90-a69c-409c6b4ea07f | -8.5207 | -46.2425 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c3e5fdf0-0934-3581-9692-4dbdb9f001f1 | -15.0585 | -42.3178 | 2025-10-07 03:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 25c35894-a843-3944-9f24-c76f1eb64729 | -15.0579 | -42.3424 | 2025-10-07 03:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 0c440a82-1f21-336c-879f-e4c53dc35c28 | -22.0279 | -49.7274 | 2025-10-07 03:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.4 |
| 45a0a4c0-da61-3d3a-8fa6-d880ec9fb20e | -10.8731 | -51.0289 | 2025-10-07 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 783e4c3e-b246-370f-b873-a801dae95191 | -13.5072 | -43.6594 | 2025-10-07 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e5749667-f76d-30ee-aa1a-851bf14d5b88 | -5.4937 | -43.0761 | 2025-10-07 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 8402275f-1540-33dd-94d9-ce4e152a13b4 | -8.5393 | -46.2631 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| cc36a111-be51-39e2-940a-75ef8eec9515 | -5.5125 | -43.0747 | 2025-10-07 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6232cc21-3103-3a1d-b98c-2f8910f1b2b9 | -8.5204 | -46.265 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| be4dfa64-29ce-37af-93b4-02a66feababa | -10.7291 | -50.4912 | 2025-10-07 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 961e3c7c-ca53-3e1a-82d7-f95e17c6a752 | -8.501 | -46.3117 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 65e103ed-f7f7-3c32-b2dd-7401134f82d3 | -4.6875 | -45.828 | 2025-10-07 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 778bc5ee-caa3-321e-9b61-4d3cddf41543 | -10.4288 | -50.3305 | 2025-10-07 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ee157f60-dad5-39e7-8e11-5ecc2830a3d2 | -4.706 | -45.8493 | 2025-10-07 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 99a33e60-4bdc-3e4f-9bc3-7f3ce98f122f | -5.494 | -43.0526 | 2025-10-07 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5c0fe5ad-fe46-3239-9da8-66d53b284ec9 | -6.454 | -44.5978 | 2025-10-07 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 95b4d102-42bc-3657-b611-b48d0d78918d | -10.4102 | -50.311 | 2025-10-07 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| a480e507-7e16-3d5f-919f-6d1c54b99670 | -10.4291 | -50.3091 | 2025-10-07 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6ae8186e-6496-33e1-b5c0-fd692437472c | -8.5584 | -46.2387 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b6bd8a78-d982-32e4-a418-3fe1f6a3fcff | -10.748 | -50.4892 | 2025-10-07 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c89839b2-2d0a-301b-83cd-5521188846e3 | -10.8731 | -51.0289 | 2025-10-07 03:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 50ff2845-f440-3142-95db-b6a84ada3573 | -15.0585 | -42.3178 | 2025-10-07 03:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 10170990-5243-3b22-b790-4511d63fe89a | -5.4937 | -43.0761 | 2025-10-07 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 61a1bd84-b684-36d6-9b2e-194d597c5d1d | -10.7291 | -50.4912 | 2025-10-07 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 48912b92-ef59-3e7c-b1a2-822595dff2df | -15.0579 | -42.3424 | 2025-10-07 03:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 62bdc24e-c114-3453-a52e-79b96cc85624 | -4.706 | -45.8493 | 2025-10-07 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e96ecfa8-2ba8-305e-a35a-7360747867cc | -13.5072 | -43.6594 | 2025-10-07 03:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 08eccdb1-e486-32dd-a750-740d73110ab8 | -22.0077 | -49.709 | 2025-10-07 03:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 9b006aa1-715d-35a6-a92a-bb1bcdf61476 | -4.6875 | -45.828 | 2025-10-07 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 9f8c3cc6-a043-3505-9e7f-7b911609ce0b | -5.5125 | -43.0747 | 2025-10-07 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4279a9c4-5e52-3822-9cd9-67c5947d1f36 | -13.5067 | -43.6832 | 2025-10-07 03:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 16a44ef5-6fcc-39d8-9055-aa7207f11db5 | -4.6873 | -45.8504 | 2025-10-07 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 145.6 |
| a01329e5-5b95-32c7-bf4c-8740db26feb8 | -22.0071 | -49.7321 | 2025-10-07 03:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| de2512d3-827c-39a3-a3ac-58c35877eaa3 | -6.4543 | -44.5749 | 2025-10-07 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f8569a06-a8b5-3174-aa25-c8692aefb5f8 | -15.0579 | -42.3424 | 2025-10-07 04:00:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 58b3540a-2683-3f06-9249-5b5c7a90f57a | -13.5405 | -43.0077 | 2025-10-07 04:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 65.4 |
| e8bda9dc-aa5e-3cd1-ad30-02e6e4ec3261 | -22.0071 | -49.7321 | 2025-10-07 04:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.1 |
| 942555ff-9a27-35d6-adb8-205c7b54c647 | -10.8731 | -51.0289 | 2025-10-07 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7adaa71d-4107-3c33-a29c-86ea602b6626 | -18.157 | -53.37 | 2025-10-07 04:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ee4360d0-9d4b-3443-a94e-ea32719edc56 | -10.8921 | -51.0269 | 2025-10-07 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| bbb9cdff-6f14-35b7-ba67-a4e0e903ce27 | -4.6873 | -45.8504 | 2025-10-07 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 3b50ced4-3d2d-3a9e-ac08-aa31f5e76a9c | -8.5207 | -46.2425 | 2025-10-07 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cef372d0-8873-385d-9f9d-3b721b95f3e1 | -3.0827 | -47.0088 | 2025-10-07 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| ba9a88cd-5bcc-36e0-8436-80007b38aa0a | -5.5125 | -43.0747 | 2025-10-07 04:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a39fce8e-6e40-35ee-9f10-9cfb4d0e8846 | -8.5395 | -46.2406 | 2025-10-07 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 23f81823-b242-34dd-b84f-2a325000a473 | -8.5393 | -46.2631 | 2025-10-07 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| aa9df042-606b-3c25-bf9e-328e11ce2890 | -5.4937 | -43.0761 | 2025-10-07 04:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 05d258cc-528c-3611-b155-525f971a74c3 | -3.1012 | -47.0301 | 2025-10-07 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 07ece94a-994a-3253-883c-4e8bceb782b3 | -13.541 | -42.9835 | 2025-10-07 04:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 858f2f6e-4020-3ce4-8dc9-45ea8d51c034 | -8.5204 | -46.265 | 2025-10-07 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cb199617-7a44-3305-9b42-8a70bf8e1d56 | -8.5584 | -46.2387 | 2025-10-07 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 75086a9f-4ce9-300c-ba7f-f75c62aa835b | -13.5072 | -43.6594 | 2025-10-07 04:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 95667a94-f1ae-3c25-9a6b-78d470d815ef | -22.5468 | -44.4405 | 2025-10-07 04:00:00 | GOES-19 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| 16e4a31f-622e-314c-b698-ab7e289fd902 | -11.0259 | -50.928 | 2025-10-07 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| fd139838-1508-3c5e-8726-710f22fe583b | -22.0077 | -49.709 | 2025-10-07 04:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 29fee398-048b-3deb-875a-3dc6cec756b0 | -3.1013 | -47.0082 | 2025-10-07 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| bbd19207-d5b1-38ae-93b9-b32918c70929 | -3.0826 | -47.0308 | 2025-10-07 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 62c6b014-cdd7-3fd6-b8fe-3bfd52d0fd5e | -4.6875 | -45.828 | 2025-10-07 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a5367607-0824-3fe7-899d-ac03f040b5b1 | -4.14439 | -47.65948 | 2025-10-07 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 232c4dfb-1bae-30bb-ad8f-9326e3b8b37e | -3.08557 | -50.58027 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f9297dd-fd13-31d6-996f-01b0f77df5a3 | -3.09774 | -47.0195 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 668e9b11-2edf-320e-ac9b-1b35f88ee77a | -3.98174 | -40.39631 | 2025-10-07 04:06:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f3bcece-9d3c-3882-b6c4-20837ac2a53b | -3.09046 | -50.58511 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab19ff73-d8ec-358a-8618-67199458c359 | -3.27539 | -43.53445 | 2025-10-07 04:06:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1afd593-8189-3b34-9f74-ba4a02c099b8 | -4.06099 | -44.50984 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b953838-4e95-3709-88eb-103ed5d52d06 | -4.14888 | -47.6601 | 2025-10-07 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cb44b89-a541-3157-882b-e7b25a65791a | -4.86248 | -42.78627 | 2025-10-07 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f3f640e-7da4-3edb-aa85-e8424842b1ed | -3.20078 | -51.01998 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0daff383-0399-3606-82f8-4b0d521554df | -1.09342 | -53.6868 | 2025-10-07 04:06:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36308de9-cf5e-3373-bcf2-6b67fe394de7 | -1.09948 | -53.69325 | 2025-10-07 04:06:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c217e4-9c8e-3487-9c80-be689809babd | -4.09473 | -40.12951 | 2025-10-07 04:06:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17f36375-87f0-3e22-af71-6bc2c84d460d | -3.10026 | -47.02427 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fea17ae4-8135-38ae-be11-5bc5c5640da8 | -4.64626 | -43.19939 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9761a9bc-6788-39d4-a4f9-e9246b8e8199 | -5.0928 | -42.61969 | 2025-10-07 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2228f394-f60b-39f7-ac71-3b0ecf8d4c58 | -5.42082 | -41.07448 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a53b7ca2-8355-390a-af96-623b0cfdbe43 | -2.2494 | -47.87069 | 2025-10-07 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f3e8af8-7190-352e-ab77-f206f0c24722 | -3.1453 | -44.41753 | 2025-10-07 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a911a17-932c-30b7-946d-d1477f7226bd | -4.86528 | -42.7904 | 2025-10-07 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c73fd9bd-429f-34c9-9d44-732ac623ecd6 | -2.8912 | -50.73004 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4a28cb0-e5b1-33ac-93be-50cbcf717af2 | -4.93354 | -43.42483 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d295e06-5d07-3c58-9bf1-067747026720 | -5.41423 | -41.07346 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de9a8d5c-41d8-32eb-ad78-b6a1a5682ce3 | -3.09844 | -47.01531 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 839c9cbb-1b77-3525-a5d2-ef5385904e12 | -2.24551 | -47.86506 | 2025-10-07 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfcf5428-817e-30f9-96b3-355c02741e2a | -4.45099 | -43.23475 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b06bffe7-fffc-310f-8850-38ead36dc9bf | -3.1973 | -51.0182 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e67710f-bd53-32bd-a9a9-181e3e1004a5 | -5.39138 | -40.9819 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 644874f1-477e-3ab0-b472-1f98559eac12 | -3.11955 | -40.99253 | 2025-10-07 04:06:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 648c6c72-1741-320d-8a6a-95b7dff0a97e | -1.61315 | -46.66686 | 2025-10-07 04:06:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 441d4c27-8bbf-31f8-b415-fedd4a8ad416 | -3.09177 | -50.57732 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af2e3814-a2cc-3eef-b7fa-8778c787fcfa | -5.83172 | -35.47851 | 2025-10-07 04:06:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3d9b875-ab78-36b6-889a-b5d955773d80 | -4.06466 | -44.51042 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c27cf5d3-ed83-35d8-857c-ec7cb1a51ef6 | -5.37881 | -40.99756 | 2025-10-07 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ab3d2403-7e02-31f8-b8d4-06d9c5473e47 | -5.30051 | -41.5625 | 2025-10-07 04:06:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 115c3756-e1b8-33c4-9b22-f91e732cd09b | -4.34414 | -46.46806 | 2025-10-07 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9f9952f-a4b7-3eca-8d1e-4b45acb9a188 | -3.1446 | -44.42191 | 2025-10-07 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59c3f915-db10-38f2-9ab7-99234762db6e | -5.41369 | -41.0769 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e132a13d-cc50-3d80-92ef-3d6daf92f68a | -3.09704 | -47.02369 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 48e02992-2738-3ae1-b6f5-0f2ed0ca6b9d | -4.5146 | -40.93146 | 2025-10-07 04:06:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
