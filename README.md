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
| 32a8b763-e3e3-3b7a-8a34-682aef2ccfda | -6.1538 | -44.6446 | 2026-09-10 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d6cfb062-257f-31d0-a041-e1e93eeb47b6 | -4.3587 | -47.7853 | 2026-09-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 43d0a180-d45c-3a83-bbc8-95f5c435e5d9 | 0.2483 | -51.4804 | 2026-09-10 00:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d8c952a7-8dc7-34d0-80d2-d14191079c63 | -7.4979 | -45.2587 | 2026-09-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c1f2e3ce-0ce3-36d8-aaaf-c8182e671a3e | -5.7571 | -45.0613 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| c0ff29e4-aed7-3f55-ab90-f0a55f056bfb | -2.9391 | -50.4832 | 2026-09-10 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 56b61e83-4975-39fe-be34-26c9b6025f4b | -5.1148 | -46.0041 | 2026-09-10 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0db743e1-ce1a-3e68-9512-6387fbaf1593 | -2.7332 | -57.6077 | 2026-09-10 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 770d82cd-31f8-333d-851b-73d5dd7af2f0 | -5.7567 | -45.1067 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |
| d1b79531-be3b-3da6-bf43-27368ca321ae | -13.4453 | -43.8366 | 2026-09-10 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cf7600f1-90b9-3d2c-bde4-40fcbd54ab89 | -8.744 | -62.379 | 2026-09-10 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 3da553fa-05c8-3da2-a852-2b74b8111732 | -2.7331 | -57.6271 | 2026-09-10 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 601136c0-f64b-3044-b1a7-449f52e2a198 | -7.4976 | -45.2814 | 2026-09-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3174f0bf-17d0-3c8a-8555-1ab0fd983910 | -5.7569 | -45.084 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 707.4 |
| df670c9b-ef60-38b2-99f8-fc5146cc5020 | -11.2103 | -49.9462 | 2026-09-10 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 75557b62-d94d-3e5a-bb46-1888fec304a5 | -19.8228 | -58.0359 | 2026-09-10 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| dc1b2a7e-c075-35d5-adee-3b2514ab6314 | -6.1726 | -44.6432 | 2026-09-10 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ad2ea22e-6f83-3425-9cbc-0905d583a7ec | -5.7758 | -45.0599 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| a2956679-15cd-394f-9420-0bc1352de44b | 0.2667 | -51.4803 | 2026-09-10 00:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2eb09c80-8eee-3480-85c4-18b40a39d055 | -5.7754 | -45.1053 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 7e0b92f7-5afd-3a72-8d4c-2c60f9fb09c9 | -5.7756 | -45.0826 | 2026-09-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 432.2 |
| 98452a5a-3a4a-3c16-bdca-cd2cde6097eb | -7.9837 | -43.9719 | 2026-09-10 00:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dfc18817-44bb-3361-8d20-91360359ce64 | -6.7196 | -45.4519 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9f3a8d-fd3b-3859-b392-b55b6f5eabf9 | -12.3504 | -48.2001 | 2026-09-10 00:05:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 467a5709-abca-3b4b-99b5-b9be9d509288 | -7.0424 | -42.706001 | 2026-09-10 00:05:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87d24fc6-0f0d-3eed-a7d5-51e52b1a29c4 | -7.5691 | -48.358398 | 2026-09-10 00:05:00 | METOP-B | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cd06cacb-ef7c-34ac-8307-0425b0535d20 | -7.4809 | -45.266499 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 800a1245-0ebe-3e92-ae51-20cf929838dc | -7.4847 | -45.282799 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 400ccec1-54f2-3e5a-a286-5f972ed7488e | -7.9754 | -43.942902 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 10799984-a2a6-37c9-81ae-d100d2523dcc | -19.8202 | -58.014 | 2026-09-10 00:05:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf3191ab-a43f-32a2-b60d-55fc82da0ee2 | -5.6568 | -44.297699 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 051f891a-9247-386e-bf49-545a10209e75 | -9.6832 | -43.443401 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c9daf6c0-c803-3dc7-90b0-67d05d3e14a7 | -5.1035 | -46.940102 | 2026-09-10 00:05:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cef8d981-89ad-3dcc-8f5f-9d1a0e27cd71 | -5.1751 | -45.459599 | 2026-09-10 00:05:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aed273d0-4867-30d4-ad02-d9db6d523d5e | -10.2321 | -45.208199 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0be6a3-40a6-3506-9f7c-6d9751dcacaf | -11.1883 | -42.785999 | 2026-09-10 00:05:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a916d3e0-f91e-31f2-ad2a-c2585f05b485 | -9.6883 | -45.221199 | 2026-09-10 00:05:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff9cf27a-f724-360a-b99a-db8faff66860 | -12.8482 | -44.341702 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17e28f67-7926-3a6f-a173-33cf873b4611 | 0.2947 | -51.444698 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 61b58b7c-4028-3adc-b6a7-0ec385936bd6 | -5.1142 | -45.999401 | 2026-09-10 00:05:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 050ef3f2-cc52-325a-829c-d814099f6dd9 | -6.1656 | -44.622501 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3d64284-f219-37b8-a523-8a22f279c07d | -7.9799 | -43.9618 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a414af6-76f4-38d8-89ca-29d1962056d2 | -6.4685 | -46.284401 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48a71b9e-678e-347f-96ec-5790c0d21a1d | -7.9767 | -43.992298 | 2026-09-10 00:05:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 750d940c-19b8-3d97-a97f-b64e99eb111d | -10.904 | -47.8466 | 2026-09-10 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b510a3c9-a7ce-3430-943f-93f4fbd476d7 | -12.8385 | -44.344101 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d62c100a-09a0-32f8-ba3b-55ae6e054adb | -7.5103 | -45.259701 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79f4740f-4dca-3b56-871c-961a220fafd0 | -3.244 | -47.236401 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62160033-ab0a-3e09-889d-ee86ec47cf62 | 0.2636 | -51.445202 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8455b2d2-e0fc-32fb-9c2b-0810aefb9522 | -7.9852 | -43.940601 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6defba-c7cf-3bfb-a64f-27e453e910bc | -13.4321 | -43.836899 | 2026-09-10 00:05:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 272796dc-c4b3-3f7d-a582-991f554d3c0b | -7.4828 | -45.2747 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2744ea2f-7968-374e-b7fa-29cdb87e518b | -10.9138 | -47.844398 | 2026-09-10 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2cdd8f2-e043-3518-a21d-fff5d50f2c64 | 0.2604 | -51.459499 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c841e426-f0c3-3390-a965-3d3e0d571fb2 | -2.8918 | -48.2701 | 2026-09-10 00:05:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78830932-39ee-32b8-96da-aaaec44b3174 | -7.2011 | -43.633801 | 2026-09-10 00:05:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4eaa2e0d-1d35-3420-905a-62bc567f0f8c | -6.2681 | -46.354198 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 852e4536-71e8-39d6-bb31-0a9b1c0b3039 | -5.3795 | -46.300999 | 2026-09-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab7913e1-e3f3-3447-9090-81c32146ef9b | -5.6001 | -44.848999 | 2026-09-10 00:05:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06d92876-0a6a-3669-adeb-987c56938a9b | 1.0108 | -51.103298 | 2026-09-10 00:05:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0805be72-4eea-3a16-a7d1-dd759c4c5398 | -3.542 | -48.183201 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b71c59d7-4c10-3afd-8c82-ed97c1f61585 | -12.8328 | -44.32 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03a26892-efc1-3a12-909c-50b02ad641e8 | -6.7146 | -46.323101 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84b8ea20-1240-368c-a38b-cd5ed576e9d3 | -12.817 | -44.340801 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5efb0446-2365-397c-ab92-379aac987306 | -12.6486 | -47.0821 | 2026-09-10 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d4d0154-842b-3df7-9dfe-317ae168df4c | -6.4993 | -47.591099 | 2026-09-10 00:05:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d022b1b0-3fab-38e7-8e7e-c953d913f953 | -6.7177 | -45.443802 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00d34182-94b5-38dc-abec-cade49072dbd | -7.5122 | -45.267899 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4842728-4683-3245-8e49-7c4e81699486 | -10.5516 | -47.101101 | 2026-09-10 00:05:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 281ef69e-deb6-359b-8d3b-284eb03baad8 | -5.7692 | -45.0886 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54f663c0-65f6-3c83-9247-f5c19dddd486 | -8.9751 | -44.993999 | 2026-09-10 00:05:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c022726-c529-332b-8fb9-9a609ba12a01 | -11.855 | -44.863998 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44daf5e9-a947-3ed1-92cc-df1828506090 | -7.9492 | -43.7883 | 2026-09-10 00:05:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 503f9f66-47d2-3015-b324-fa579efecda2 | 0.2588 | -51.466599 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ece534f7-222a-3131-8bf3-c678e937d866 | -7.5753 | -45.6735 | 2026-09-10 00:05:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b92c1913-a369-34b3-ae27-30f12cc33c06 | -3.5518 | -48.181 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42960fda-b87e-3af3-bc50-d0831665520a | -15.3291 | -47.245499 | 2026-09-10 00:05:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b4ed672-7c7e-31d0-b468-9b5698b9fedc | -7.0202 | -45.103699 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78542d18-68dd-3bf0-b045-47b54f414f07 | -7.5084 | -45.251598 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c911a70c-11ec-3b2e-aca7-97bb310d0986 | -15.7826 | -43.5513 | 2026-09-10 00:05:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2949f6de-5d26-346a-a650-7ab46e473f4a | -8.32 | -45.1049 | 2026-09-10 00:05:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fb9abb3d-3db9-3ff3-b086-b7bee45e00dd | -10.234 | -45.216 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b007e829-8bc6-3f0a-afce-e249f0242df5 | -2.7166 | -57.589901 | 2026-09-10 00:05:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 532c7ef2-893b-3c33-b10a-70828f0ba682 | -12.6502 | -47.0891 | 2026-09-10 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1639b5fd-d207-3047-98b9-c02a7916a934 | -7.4907 | -45.264301 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa7b6a81-f813-33ef-b834-1216e749fc84 | -12.8403 | -44.3521 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cad2b2e0-329b-3fd5-84d1-efd5a86f5a28 | -6.0894 | -47.284801 | 2026-09-10 00:05:00 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5073514-153a-38cc-bc4a-d5f3ae3db81f | -9.1674 | -45.244202 | 2026-09-10 00:05:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cafabaca-2ea2-3c06-92a3-127878b1de23 | -12.8561 | -44.331299 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e339a177-c65e-3d00-999f-26a7e8688d16 | -9.3292 | -45.630699 | 2026-09-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5e9a11-7335-3795-bd57-7fceb1a8749d | -8.977 | -45.002102 | 2026-09-10 00:05:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 931ffa6d-1612-3481-b5a1-ae3f738d0b92 | -6.091 | -47.291901 | 2026-09-10 00:05:00 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5311b38e-c155-3fbb-a8a6-6f7b09907e19 | -12.4027 | -43.4156 | 2026-09-10 00:05:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8ca1c8-1f93-38f0-99bf-333dd5a6ce70 | -12.8207 | -44.3568 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc4f6937-9202-3ac5-835a-63c0cfff3443 | -2.9488 | -50.482201 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6838412-e9fc-312d-a29d-f17457b74efe | -10.4623 | -44.955399 | 2026-09-10 00:05:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81b95b31-0fdf-3305-be3f-b2fc8626546e | -7.9865 | -43.989899 | 2026-09-10 00:05:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88fc6f54-d47b-3e14-86fd-d193dfc0f4eb | -9.1693 | -45.252102 | 2026-09-10 00:05:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7aca7a21-59a7-3312-aa0f-cb8d435d31f9 | -5.9209 | -44.943001 | 2026-09-10 00:05:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4a691f8-b96b-3490-a8f0-69a5f5d516f3 | -8.9395 | -44.4007 | 2026-09-10 00:05:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
