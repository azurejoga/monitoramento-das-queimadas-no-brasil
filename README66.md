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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37edc35a-48c3-3949-8315-08f21d787eb0 | -8.61751 | -54.99408 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 954fef1c-8e73-3da6-83a0-6d3511e6fd89 | -5.63975 | -50.31797 | 2025-10-06 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1477d404-e551-3eac-bc26-c291b3f96fee | -11.13664 | -47.16553 | 2025-10-06 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82705143-0f5c-39db-97e2-51ddc12d453d | -10.43503 | -50.36414 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d305081-6635-3cc7-ad8b-376adee96f68 | -8.55896 | -46.25674 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8cb9a5c-0ba7-36d6-840e-7695a86eb3b3 | -12.24776 | -49.20387 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 951f020f-4a21-3276-abd9-ef7f17fce5e9 | -9.61476 | -57.20533 | 2025-10-06 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da6e22dc-0f8a-39c2-bbfd-c27a9a3e0d61 | -8.44067 | -70.12688 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7484c02b-615d-3228-85ed-cdf2fc23b65c | -10.49935 | -51.50157 | 2025-10-06 05:16:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 687d1462-7cef-3c5c-bb5e-201824dc8db6 | -10.42438 | -50.34524 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580404d3-0359-345a-956a-d9f5545e894f | -8.44148 | -70.12251 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8ec6cc0-b032-3154-9294-a840cf29816f | -7.98919 | -45.47919 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8b053f00-a90a-3357-bce6-f5dc5fd879e4 | -7.99792 | -45.48914 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 479784d9-9490-3bbe-8440-abe89045298a | -8.62651 | -54.62463 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb75a192-53bc-3f25-ae79-dc57cda07cff | -8.88301 | -47.61937 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 735fdabd-bfcb-354c-a3e3-61fa087b2803 | -8.61641 | -46.29568 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 203fe5c3-be4e-364f-92e4-a56a31c6a4f0 | -11.15575 | -47.93608 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f49f1607-8cab-3788-be51-f8ab49be960b | -10.47345 | -50.44993 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e52bb198-c0fe-3ba0-8eb9-10effbbd27b7 | -9.15487 | -58.31344 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b7ef9d9-d8a9-3a52-9609-4191ddbca48d | -6.37055 | -58.207 | 2025-10-06 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9aa64560-03d3-390d-8424-6e1fe25a94e3 | -9.30804 | -54.53691 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b907631-df25-3406-b307-03b7e5afb178 | -10.37373 | -48.15238 | 2025-10-06 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 187430f2-8d93-3208-9826-a6b8fe6d7bf0 | -8.61158 | -46.28882 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 34b46924-dcd2-3cf4-b759-8112511b768d | -8.55974 | -46.25048 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f64b620-8a06-31d5-b057-18f30a8d9af5 | -12.57061 | -48.1485 | 2025-10-06 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b4d16a79-eb72-3ebe-988f-355159f65a0d | -6.5543 | -47.86499 | 2025-10-06 05:16:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fcc21e30-d042-3314-b7a9-c364356e866d | -11.94961 | -51.47489 | 2025-10-06 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4483ffa-9f4b-3828-ba63-f02a00f61515 | -8.43986 | -70.13123 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ada4bf4f-c189-3a29-889d-b37cbe6e1683 | -6.55489 | -47.86066 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8c277777-4fbb-33f7-a9d9-0dd4e1401091 | -6.56149 | -47.8574 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 04f66243-daa8-38c9-a68a-3908b7526ac9 | -10.43546 | -50.36068 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f66b350-03d8-3f7a-869d-e007d8517efb | -9.4825 | -54.59833 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58832c92-37c0-3cab-af8d-86851bf44df7 | -11.5147 | -54.45481 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b81e6dd-06d7-3dcc-a0fe-439643831a69 | -9.23026 | -51.82595 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a835c9b-0e74-316b-8e45-13a3add7fdbb | -8.87669 | -47.61856 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb6373b-9cf4-374a-b32f-86c51caedd6b | -8.47499 | -54.70314 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49dc353b-24b7-36d3-aea2-5f1756272ed8 | -11.51002 | -54.45808 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dadd818e-a0ef-39af-af2b-e008f91f06d9 | -5.32732 | -47.28469 | 2025-10-06 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a1c508c0-59ea-399d-82ee-36c76742b202 | -9.24595 | -60.28083 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3fced9-4b80-3dee-90bd-5b34b55dce6e | -11.75149 | -51.51423 | 2025-10-06 05:16:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6f34bc6-8c8a-3430-aff8-d58238a42b6f | -9.07771 | -59.02647 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8440539-706a-3158-81fe-b32eaf06168d | -8.63505 | -46.32315 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5e4c07fa-7a85-3a42-97f8-d04d9b844cc3 | -10.32318 | -50.27509 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e6dc5a7-1b3d-3d70-8115-be13d30fba63 | -8.74052 | -50.66364 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3e3f7fc-13d6-32a6-aee2-7d54c5a25195 | -8.88258 | -62.32459 | 2025-10-06 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c090db64-4eef-3f01-89b3-aa053f2797df | -8.62825 | -46.32219 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d04a82ea-3e00-3166-8434-282dd8af3730 | -10.2359 | -52.69972 | 2025-10-06 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e33f7147-90cd-33f8-8443-7dccee578573 | -11.50329 | -54.47652 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c0e8ba6-5d5b-3b47-a350-cbdcd35645bc | -10.76437 | -49.70266 | 2025-10-06 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bc403a8-a9c7-32e2-ba6b-deb1b00dfbef | -9.3403 | -54.52395 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2a109d5-93c7-344c-9bc7-6429ec8b3592 | -9.67789 | -49.95919 | 2025-10-06 05:16:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 67600033-2d18-3557-be8f-1b244a4ea365 | -9.45497 | -56.65265 | 2025-10-06 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c2beebd-1275-3755-9f79-8a0014a7ef45 | -7.72205 | -46.25877 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4635dbf0-2670-3222-88fc-d267b777f33e | -8.62483 | -54.97049 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04f1ff87-9306-3e4f-8190-7c3522943946 | -7.72281 | -46.25296 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94419869-fa4a-3d3c-a5d7-348df40f3060 | -10.59248 | -54.35247 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 218e52e9-28db-3f89-ad73-4c4fa6e20e38 | -11.44094 | -55.05101 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c28b1c-45b7-36c2-acda-d25577e7f4c8 | -9.02379 | -50.58999 | 2025-10-06 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37da3074-c374-3d3e-badf-cb76536ee7d4 | -11.14036 | -47.16796 | 2025-10-06 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcaaa5cb-bbf1-3b46-8190-19b4180cfa5e | -8.62166 | -54.96516 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| efcd0734-bdc7-3b99-b041-560ad412a44b | -9.19618 | -63.15507 | 2025-10-06 05:16:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6034834e-01e7-3523-8c84-cef5864e9712 | -8.61255 | -54.97374 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b16ec315-1883-3a85-9aed-fd0e9a63ebe7 | -12.26483 | -49.1853 | 2025-10-06 05:16:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a4d7dd-f375-364b-a3f4-95059fc1cbd7 | -8.61935 | -46.32645 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a9f8ad-e4b6-34c3-bb7a-0cd410d10554 | -9.3277 | -54.51443 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 159dfa4d-8377-3729-8a97-14e30d387786 | -9.91416 | -58.56331 | 2025-10-06 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 232d0caa-8930-35ca-8f7e-147aa198ac3d | -10.4739 | -50.44643 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edcda440-9438-3b2c-9fd3-12c664f65fa4 | -10.42098 | -50.34461 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7e931e9-cd9d-3cc4-adcb-3903735ea221 | -10.47434 | -50.44298 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7465444f-978d-3fd6-93a6-01862bbfae3f | -8.62072 | -46.32725 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44799f5e-0c46-3086-88e3-c3cd41d0492b | -10.41402 | -50.34035 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b164908-88ac-3fc0-8a30-e18c9470eec2 | -6.55666 | -47.84774 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 83538921-2f43-334c-bc74-7b79df4c19d3 | -9.32718 | -54.51797 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54b44a59-f109-3de1-a6c5-0cd2278049aa | -8.56336 | -46.33181 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2ac0ac2c-b96b-3ea6-918c-c437079e1a79 | -8.47427 | -54.70812 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4dcfbdb2-3d33-3179-bcdb-9b0cbee54987 | -9.15069 | -59.53437 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f9c1711-7694-326b-9d45-1b6591451f8d | -10.04683 | -49.2057 | 2025-10-06 05:16:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3f505a5-04ec-39d6-90ed-e99947d1a670 | -8.61848 | -54.95978 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfbd66a2-baa2-3c92-ae94-3914dbfd6897 | -11.41796 | -55.07006 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbf90a7e-17fb-3f66-9fe8-31e533bbed08 | -9.34431 | -54.52452 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42f313f0-f644-3312-b11f-3a92dd7ff2a6 | -10.04633 | -49.20972 | 2025-10-06 05:16:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4616c1c3-1d0f-3508-9645-2898c97a4f07 | -8.45247 | -70.12909 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82b15db4-afa6-38a4-a5bc-19cb4c072bc7 | -8.17311 | -47.67301 | 2025-10-06 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b225bcb7-6a18-3229-bebe-7d897b6cfce4 | -8.15292 | -54.84996 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2957c77-7dff-3f31-90dd-bce1cb72f4c6 | -6.55548 | -47.85633 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 895cdccf-6a6a-3f09-a171-90e35c986f54 | -8.61868 | -46.2781 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b932254-26ec-3c46-aa09-a097bfa944c7 | -9.02811 | -50.67783 | 2025-10-06 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5c44077-a055-368c-9ad4-dc94811bfd51 | -5.24102 | -49.8696 | 2025-10-06 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 543d50ba-6569-3433-b9c1-9cec5962fac7 | -8.61718 | -46.28965 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0f1a098-cf9c-329b-b544-148c216465fb | -7.21457 | -45.88976 | 2025-10-06 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a491ec49-df56-37ef-8f0c-33daecf9678b | -7.35937 | -64.66148 | 2025-10-06 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a49357d-b591-31fd-b3a5-ee071000c04b | -8.48046 | -55.17306 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 077f4b4d-7d22-3cc8-baa2-28d63217530e | -8.60964 | -46.29439 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d172954a-1a60-3979-b6dc-f66a3f51235e | -10.7587 | -49.70193 | 2025-10-06 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 100982ba-b365-31a5-baa3-f3588d6d9d68 | -8.61081 | -46.2951 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48e3bed2-2e05-3c30-b68a-147e173718b5 | -11.02268 | -46.53251 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bd3438ca-e85d-3954-9ff9-32d9051ad68f | -9.66691 | -49.95774 | 2025-10-06 05:16:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 812a1c5a-2046-3a47-bdf4-90494ad873c5 | -7.03551 | -49.30484 | 2025-10-06 05:16:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3866d3e-8e65-3c63-a6a9-49cf4b9b5c14 | -7.9963 | -45.48002 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fb92b46c-5b92-344e-a7f4-cb3d9214cbac | -5.24057 | -49.87267 | 2025-10-06 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README67.md)
