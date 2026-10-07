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

## Dados Diários - Página 216

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea7a0b62-5575-3c36-a94e-716a76278fdd | -7.09712 | -45.23398 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1ccc2c17-63fd-3f22-910e-fdc630022fc7 | -4.36575 | -43.90856 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04e0c3c0-886a-3fa5-868f-1eb7ba317af8 | -15.96878 | -40.6968 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8bb2039d-5db4-3e77-9842-6bc1396a48fe | -8.46366 | -48.69132 | 2026-10-07 16:37:00 | NPP-375 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea6cd549-21ae-3522-94c1-75904b55c32a | -6.20526 | -49.38148 | 2026-10-07 16:37:00 | NPP-375 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9b9f82b-15d0-3e7f-a541-2fd6813aa4c1 | -4.96856 | -40.56124 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9b20c1b1-0d37-3fd2-b8ed-7e2e560338a6 | -7.04657 | -44.32484 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dd83cd81-8166-33d1-bf54-b0ab2d043c4b | -14.7792 | -41.60019 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 86.0 |
| d4894826-5c6d-3610-99dd-1670b8a852aa | -9.95098 | -43.5553 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 6383f7de-2595-308f-b610-cf5dc8735f08 | -3.95094 | -42.46988 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ea93e60-6dce-38b2-99f1-3fde564abd04 | -6.65294 | -47.90976 | 2026-10-07 16:37:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 467a932e-9547-39bd-bcfb-7f376e0a7a65 | -6.83834 | -39.55816 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| dcc83d53-c244-3054-adaa-8d618e7aec92 | -3.53027 | -39.50353 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 78cf8d6b-c1b9-3a01-aaa8-39807fa44a3f | -6.05258 | -53.48307 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 184a18a3-b53f-3da1-ad40-82fff60cca33 | -8.5428 | -54.58618 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8b84245-a2d8-3998-ba25-e4c1362d4496 | -4.45036 | -45.72231 | 2026-10-07 16:37:00 | NPP-375 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a6a5ca-7b5b-35a1-85a4-ce702bab7062 | -5.94543 | -46.361 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a22bf883-9adc-38ef-b660-c18347cc78c1 | -5.7569 | -42.04144 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| c137dad2-5241-3e7e-842b-77ed333d9568 | -6.24564 | -44.34856 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b3cd194-0fa1-3f03-8cc1-b030dae4ed4b | -6.69432 | -44.92113 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 62e87adf-86f6-3b48-b49a-a9107c5d01e2 | -6.9405 | -45.27971 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5bee9760-67c1-33e0-8eb2-b794af174301 | -16.64619 | -45.50808 | 2026-10-07 16:37:00 | NPP-375 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6fea0043-fe19-36e0-a202-560457aefe46 | -6.6785 | -44.9523 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40c330ee-e4b0-3e32-9cbd-ec508bd79f36 | -9.12814 | -45.10827 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 619b672f-a2e5-3550-969b-c10013d9d00a | -7.0995 | -45.31829 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1bdc2bb-ba11-35c7-83eb-ea52d8f08b7d | -6.34262 | -38.86825 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c792656a-cce5-3e28-8956-fb05e0b6803d | -7.60009 | -47.02507 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e52fa60b-6813-383d-86f2-1a01b2cec7a5 | -7.26115 | -39.71606 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| f06866e9-4d97-31af-aa02-81522099d6e3 | -6.20313 | -42.92715 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2c2f232a-8c66-3101-99f0-10480f307610 | -7.39658 | -46.21468 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8b0e3860-f4d4-36fa-ac18-8528d3abc27b | -6.58385 | -53.03659 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 883fe9da-eb39-3786-9401-e5335005b884 | -5.01814 | -49.94031 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6fd2837f-31c7-3188-9ee3-2951ff7e8f22 | -6.17442 | -35.42284 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3d3e7a34-1ebc-38aa-9425-00722b6d4591 | -8.21763 | -46.34333 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 6f6d8e1a-8cd6-3d0a-bc5d-1f79beec5263 | -2.97348 | -41.41476 | 2026-10-07 16:37:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fd83153e-af2e-3114-bce0-841b3382d7c2 | -6.94281 | -45.27209 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 463f0264-d119-3857-a222-e601ea4215a4 | -5.64376 | -42.78466 | 2026-10-07 16:37:00 | NPP-375 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 082dda02-9763-3c2e-91ef-5c2d580bb1c2 | -11.11201 | -47.59092 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77ab9543-7f1e-3cf5-b376-02322aa5a391 | -3.87657 | -44.11111 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 75db24f7-63e9-39d3-ad24-5c5b589ba48a | -5.97882 | -53.56244 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8a24f34-4fc6-3156-994c-9eaafda948d7 | -11.3503 | -51.87844 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| be368ddf-e45f-366d-a1df-53d41a1c6307 | -5.47447 | -41.21746 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 7362ec69-984e-3da7-adf9-9e9d6c4b988a | -5.36963 | -44.16843 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb65b262-6cb5-3733-874f-0d8732f9ba04 | -6.14859 | -52.89934 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3e464972-8817-3869-a355-6283b27c85d4 | -17.02066 | -45.91592 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| baaa4d9d-3e1c-3150-a430-d5aa10121c65 | -6.40578 | -52.71146 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d73c71e1-905b-3ea7-9e6f-ce349688174c | -15.80534 | -47.84647 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 58969362-94a7-3475-a2aa-94b79994b319 | -9.80062 | -44.77757 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4218ffc-3f76-33cb-81bf-37892f19989f | -8.35015 | -49.77543 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6f0939d-2365-3ea5-aea4-337a04de727a | -3.94525 | -41.54805 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 9c4a3c53-b177-3cff-b7d8-4164345568aa | -10.97634 | -45.4049 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2ff6241f-d868-37bc-bf37-a62094c8d5ce | -6.44246 | -52.67193 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 94e788fb-659e-3c03-a9b9-d75b8aee2f2e | -6.31943 | -43.48657 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6a889714-1783-30cd-912b-6b1ba988caac | -4.572 | -43.88621 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8b778a7-0f80-366b-990e-e82e0d6b1954 | -8.72418 | -48.06612 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d04ff37b-7e04-3b3e-9d27-ecad79e702e2 | -5.50523 | -42.83606 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| e21dfb19-8c68-332f-9daf-ffa59deab076 | -9.03656 | -44.36327 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 97aac22b-f1e5-368e-ba9a-103de9fe86e6 | -6.82861 | -45.00196 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 50302417-36fb-3005-adc7-661c6278feb8 | -6.1056 | -55.68491 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 7eb7a98b-9606-3ea6-9e6a-90fb57790a36 | -5.738 | -41.72067 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a613d33e-9543-3fd3-9d19-ba6dd92784b5 | -9.5508 | -43.0822 | 2026-10-07 16:37:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 08d22725-1ccc-3cd5-b35b-fcfd791d2d48 | -7.54212 | -35.26976 | 2026-10-07 16:37:00 | NPP-375 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8927471f-c31d-35fa-b84c-1d1ea79265ad | -6.64695 | -43.78791 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5436cef9-dd81-3e71-bda8-7fe63ef44bfc | -8.16864 | -47.6399 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92f39548-690c-3f26-8c61-d520f00b34d9 | -6.05567 | -47.32361 | 2026-10-07 16:37:00 | NPP-375 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ad25d8af-0676-3705-a630-3306b7fda508 | -3.95905 | -42.47639 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f94e4ed-7f70-36b7-872a-9fcab871a688 | -10.35881 | -48.23288 | 2026-10-07 16:37:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 736f6656-fec1-3e86-b859-6243f551e56a | -7.59937 | -47.0202 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d79c08a6-f8a7-3068-bbbd-511349d87c33 | -5.69244 | -45.28716 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7bae1cfa-b486-30eb-9cb5-34edf9f9a40d | -6.44719 | -52.66815 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4b92b7cb-4b82-333b-81b8-aa668abe9f61 | -6.19957 | -51.43877 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f583d2b-0679-364c-824e-dbd59632b519 | -7.21308 | -44.2878 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70e0f93b-9561-30b0-8471-be36ce628950 | -10.37732 | -46.25533 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| f375239e-3295-3017-b3c9-0d887725a835 | -5.49 | -42.82735 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 07010fc2-4668-3c76-a098-cf5e6f96ce33 | -16.63343 | -51.08792 | 2026-10-07 16:37:00 | NPP-375 | AMORINÓPOLIS | GOIÁS | Brasil | 5200902 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 86669459-0889-34ae-9b80-a1837ae352c4 | -5.23842 | -50.909 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3bbb71f3-9b01-3002-a549-bf1662374b66 | -9.91646 | -44.80807 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 03d9a9d1-8aa8-31b4-91c2-8cce33eb1712 | -15.69714 | -41.0523 | 2026-10-07 16:37:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 51a0fa5c-f4ae-3986-b2b3-74fe81774140 | -5.73319 | -45.15761 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| ca4eccc1-559d-3a56-b4c9-c3639cd588a1 | -9.93182 | -46.94988 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c474492d-ed26-3b03-9758-f641d27337bc | -6.35113 | -44.86356 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a85e2c5-3bc9-3a1e-9a92-ef3ef77cca1e | -6.3548 | -55.13821 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4831ab27-9626-3148-bd1e-12ecb04f6d02 | -3.55665 | -39.13744 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 151d7178-04f1-3b5d-9b9c-6bc8184399bb | -8.16936 | -44.41661 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 475c4fbe-5238-33d1-b242-4b3b45280f3b | -6.99009 | -43.29384 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 58ba564a-d440-3c72-88bc-3feb601b6217 | -8.74205 | -44.20738 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82f09107-bfae-3f08-af25-c29650073a24 | -3.22606 | -42.81361 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0643ca9f-fd3c-3174-a8f1-b8718b3e8c12 | -9.86524 | -46.3067 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d795805e-baa8-3eb9-86a5-902ee06d7065 | -6.48536 | -52.82678 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c5d9fe60-4190-32fb-aa8f-6d60938ad061 | -17.02815 | -45.92726 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e785cf86-9382-32bc-96a2-aecb9dcbe218 | -5.46599 | -45.79434 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d5fa5739-3f95-3df7-aabd-e0222b085f09 | -5.7281 | -45.16921 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 72bc656a-8afd-36e9-95c6-8194746be0fc | -6.45908 | -43.97388 | 2026-10-07 16:37:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2cdabaae-3c24-3908-a540-b315af2d17b0 | -6.91769 | -41.24143 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d481051b-509a-3342-b782-5d6558c0e834 | -5.85055 | -42.65507 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 38ce521a-c082-3a59-ba7f-69328b6e43e2 | -7.17506 | -47.79436 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ffc674fa-72f6-301a-a2a3-9ef431fb0ed3 | -9.44468 | -45.83187 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 79766fac-e76b-37ae-95f1-685fbc6c632d | -4.28224 | -46.47937 | 2026-10-07 16:37:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50834d7a-d2e0-31f6-9730-b0bd27223147 | -8.54223 | -54.58165 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 315163fd-db4f-3b9c-a5d0-45a945b64a5d | -7.07151 | -35.29469 | 2026-10-07 16:37:00 | NPP-375 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README217.md)
