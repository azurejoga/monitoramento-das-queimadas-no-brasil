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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da0543c0-0a8a-3806-a89d-f85dd7662919 | -4.0456 | -44.2555 | 2025-11-15 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 30879a9a-4044-3812-870b-eb476a5d9b88 | -7.3988 | -44.0536 | 2025-11-15 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2dfb413c-50e2-36dc-9cdb-e0a198c5781b | -12.6938 | -46.7576 | 2025-11-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0c769b50-c403-3c55-8899-60e1b393f07c | -4.4845 | -42.8631 | 2025-11-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 86572665-b817-328e-9a95-1278a1a180bf | -3.6252 | -42.8168 | 2025-11-15 14:20:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 86690046-43ec-359f-b855-988186389993 | -3.6511 | -44.7994 | 2025-11-15 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| b5be83ea-9f1f-3222-b4fa-9c5ddb223103 | -7.442 | -45.2184 | 2025-11-15 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 89e27add-b847-39ac-b6ed-f1fca24d6457 | -8.5792 | -46.0794 | 2025-11-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 8770e437-fbfd-3e47-8db7-643cacbe36a1 | -3.5359 | -45.4594 | 2025-11-15 14:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 324.4 |
| d7d56fc4-7510-3bd1-8ca6-93d592f059ab | -11.709 | -48.408 | 2025-11-15 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 8c91bc7d-be44-3b6c-aafb-6af2fac5185c | -7.6149 | -46.552 | 2025-11-15 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5facc8a7-5baa-3c32-8f7c-dacff0a0a2f4 | -6.0849 | -48.1859 | 2025-11-15 14:20:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f8969750-825d-3f51-bb49-1ff46f01a5be | -4.0067 | -47.6711 | 2025-11-15 14:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| cd32b629-79e4-31ad-8e45-8c78abbe196b | -3.59 | -42.4421 | 2025-11-15 14:20:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 194.6 |
| 997c5da6-90f0-3023-91e3-063764f607d1 | -11.9171 | -46.2362 | 2025-11-15 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 321.0 |
| 05f32fac-f920-3333-b409-e079479b3347 | -12.8727 | -46.4363 | 2025-11-15 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c041f1b3-9cf8-3361-9372-59d165b381d4 | -11.7017 | -48.8692 | 2025-11-15 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a67a6658-e667-3960-805f-d7a197da7322 | -4.1385 | -44.3194 | 2025-11-15 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7a3d92f7-1e19-3822-88f7-79f6fcb0370b | -11.9175 | -46.2135 | 2025-11-15 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 394f7c7f-351e-3ac8-a6f8-347825f907ea | -8.6808 | -45.5041 | 2025-11-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 600.5 |
| 372199ac-9cff-326c-bc41-275bfa49b5dd | -12.4109 | -47.5616 | 2025-11-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| a1863f1b-dd70-3edf-8308-f7265e2293ac | -8.5795 | -46.0568 | 2025-11-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 191.7 |
| f185f3eb-d794-3fe7-b5b3-3c6f258e1979 | -3.6835 | -42.4374 | 2025-11-15 14:30:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| a2c32901-e385-3fd2-a031-5cae4fc89a32 | -6.1608 | -48.0289 | 2025-11-15 14:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 511ca0b6-f6fd-3990-ae8d-fdf85d3f6890 | -4.0067 | -47.6711 | 2025-11-15 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a3758189-468a-36b6-b55e-aaa6cf10aa35 | -11.709 | -48.408 | 2025-11-15 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 406d8db7-f3d5-3710-880c-f630997be82d | -9.0009 | -44.1843 | 2025-11-15 14:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 954d2e38-b791-3577-ad66-dc2ed80b2641 | -11.7017 | -48.8692 | 2025-11-15 14:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| cc8edd9c-747e-3bd4-8a31-f87ad72c81c6 | -8.7355 | -45.657 | 2025-11-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4c21c4f0-ab94-322f-bf48-35d1fd71739c | -10.3232 | -44.576 | 2025-11-15 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 67c8ba58-8b85-3952-8808-a97bc2040b71 | -7.4417 | -45.2411 | 2025-11-15 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 06384560-f309-3727-ba31-eebb3166030c | -12.6741 | -46.7831 | 2025-11-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d5a1aed0-6ea5-3e8d-ab2c-2e662cd9a568 | -12.4106 | -47.584 | 2025-11-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f38611af-644b-3bdf-8b56-44622141d93d | -7.3868 | -48.6545 | 2025-11-15 14:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 72e25330-6035-3d04-8d59-7d906306973d | -10.5461 | -44.9159 | 2025-11-15 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 385.7 |
| 56aac54a-b523-339a-8133-0d652ce57336 | -7.3504 | -43.3604 | 2025-11-15 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| def952e7-f683-3f1f-a2c2-153bff2dc5b5 | -3.5667 | -43.2402 | 2025-11-15 14:30:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b0edf7f0-361d-3acd-ba52-fd31896f1090 | -11.3265 | -48.5214 | 2025-11-15 14:30:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3772bee5-a0ab-36c7-8132-d67c569896fa | -6.2944 | -41.8265 | 2025-11-15 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 626cb80f-9f59-3736-bfc8-76da5ee00c0f | -1.2934 | -53.7565 | 2025-11-15 14:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dfbf08f6-a115-3957-8382-6bcf8ab379e2 | -14.5621 | -45.1875 | 2025-11-15 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 9cff9c64-c429-36b8-8baa-78319c9c1df1 | -6.1421 | -48.0302 | 2025-11-15 14:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 385.7 |
| 5b065771-b97e-383d-bce9-8d43bde56ce4 | -11.9171 | -46.2362 | 2025-11-15 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| ede7efc7-6056-398b-88e3-9ec85d3ef661 | -12.3914 | -47.5867 | 2025-11-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 3e36311d-05fa-3711-b03d-25cf50075556 | -12.8534 | -46.4392 | 2025-11-15 14:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| ad9d23b2-1b4b-3e31-a756-98380b438bbc | -11.6755 | -44.7342 | 2025-11-15 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| e6552899-05f6-3dbc-a637-e807ed006623 | -4.1787 | -46.8313 | 2025-11-15 14:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 15ebed33-ada1-363b-ab48-5fc467ba543f | -3.2488 | -43.3942 | 2025-11-15 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6a82c917-dda6-3759-b76c-2ecf8adb23e2 | -7.0938 | -42.7509 | 2025-11-15 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| aacb42ec-62ac-3ec4-9684-ec454de6cf35 | -4.4845 | -42.8631 | 2025-11-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 90266230-451f-3bbd-b84d-28a374a556f0 | -10.5652 | -44.9134 | 2025-11-15 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 175.4 |
| c61ebc5e-d1f2-31e3-8700-e2f4a890a261 | -12.0748 | -48.2065 | 2025-11-15 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 53a97c3d-64f2-304d-8816-a67ab66286fc | -8.5604 | -46.0813 | 2025-11-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 314.9 |
| b45b2763-6c26-3c47-a66e-6395fd1b2bb7 | -8.6811 | -45.4814 | 2025-11-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ea6e3c75-c7ef-3fd8-960e-1cfcdcff8cc1 | -9.9377 | -44.9252 | 2025-11-15 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| dcac531e-370f-3632-bce2-f7c742f8c4d8 | -12.8538 | -46.4164 | 2025-11-15 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b7b27024-853a-3678-a4ec-eb1ca21055b3 | -7.442 | -45.2184 | 2025-11-15 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5704cdc3-4f9a-35d2-9770-b9e3bfa2e386 | -3.3552 | -40.9959 | 2025-11-15 14:30:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 96.6 |
| ae0d2fe4-2c7b-39a3-99ed-64ed78a4a3d8 | -3.6696 | -44.8212 | 2025-11-15 14:30:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 82b26903-7f21-3b86-86f9-f9129aaa9e2f | -12.3917 | -47.5643 | 2025-11-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 205.9 |
| c9e9bf3d-b2cc-3e4e-8b50-b04701f5ab41 | -9.0217 | -45.4217 | 2025-11-15 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 34fbbd22-d530-32d6-9595-7b1ddca430a7 | -9.9374 | -44.9482 | 2025-11-15 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bbec2061-0263-322a-b622-1b6383284e35 | -4.5033 | -42.862 | 2025-11-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fe0bddf4-8e10-3b01-8be4-b84090f3d99a | -3.59 | -42.4421 | 2025-11-15 14:30:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| bd7bc682-c919-3289-bfee-353c002e2d6a | -9.1384 | -45.1808 | 2025-11-15 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 68714e6e-d136-3946-867d-ff193dec2b5a | -8.5607 | -46.0588 | 2025-11-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 78b0422f-74fc-3dd3-bc2b-269de25b7cbe | -8.6623 | -45.4834 | 2025-11-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 287.9 |
| 5b78f767-2029-3c79-959b-2ce6a04778cc | -11.7094 | -48.386 | 2025-11-15 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 44cdaef6-9c83-3f24-9f5f-b81b41057ccb | -8.1967 | -45.0312 | 2025-11-15 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 44308d1f-62e1-3422-ab21-a779204402e3 | -10.5379 | -47.934 | 2025-11-15 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 78e15712-054a-33f1-801d-4cbcf2d7a28e | -11.7904 | -48.089 | 2025-11-15 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d6d23256-03ff-36d8-92b6-d8798da07fcc | -9.0025 | -45.4466 | 2025-11-15 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 446330bc-0146-3549-ad6f-9a04c72f64dc | -12.0557 | -48.209 | 2025-11-15 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5eb2a5e1-3338-39cf-a58b-fa0053d9191d | -9.2325 | -45.2157 | 2025-11-15 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| cd90829a-2bbe-38b8-8984-78519a718d15 | -6.1233 | -48.0532 | 2025-11-15 14:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 332.3 |
| c55b1ca7-1849-30fd-83d8-62fbc842fd8f | -8.5792 | -46.0794 | 2025-11-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 7bf75185-4c39-3b57-a43b-a86eebd11058 | -11.4977 | -48.5223 | 2025-11-15 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 703ea7cf-34f6-3fff-bc1c-26d374dbc285 | -9.8542 | -44.1729 | 2025-11-15 14:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b175467e-7320-381e-a7c3-ab2270e2201b | -9.9564 | -44.9459 | 2025-11-15 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4b30dab4-e7b8-3d39-abb7-f67b6ed09e29 | -12.4436 | -47.891 | 2025-11-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5a124162-f1b9-3939-92b9-f9859c6bd06a | -3.8083 | -43.4143 | 2025-11-15 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a943ef81-5baf-3e80-9d79-2ad97072c0aa | -9.9754 | -44.9435 | 2025-11-15 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| a3893637-452d-3817-9323-84cb2664cbb0 | -9.7549 | -45.7464 | 2025-11-15 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 215.0 |
| ec886c45-50c0-3a7a-b75c-bf77b635b9ab | -8.159 | -45.0351 | 2025-11-15 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 2584caae-1d3b-3a78-9603-b6a7fcfd53ed | -3.1305 | -41.0066 | 2025-11-15 14:30:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 8ed3c729-6d73-3da2-b463-612188b91826 | -9.736 | -45.7487 | 2025-11-15 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 5482f053-1ed7-3967-86f7-c429f2863ed6 | -6.4113 | -41.4552 | 2025-11-15 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 843434e4-e34a-3584-9561-0388713295f6 | -7.4224 | -45.2883 | 2025-11-15 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 59b6b8ac-bfbd-3f8a-92a0-72fd039380a2 | -6.1421 | -48.0302 | 2025-11-15 14:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 314.6 |
| d43ee78a-d543-368e-b182-9bf239ee0e5d | -11.709 | -48.408 | 2025-11-15 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a921e2a8-a5d9-3ed7-a953-ffd92ee30a81 | -9.0217 | -45.4217 | 2025-11-15 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 98d2a959-110a-3bc5-8944-a38d30e3a479 | -10.3037 | -44.6017 | 2025-11-15 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 1f59ea11-feb4-3c92-a278-184d51fd497a | -3.8083 | -43.4143 | 2025-11-15 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4af3edc9-f4b5-3b49-a2de-61a734e6c59e | -14.5621 | -45.1875 | 2025-11-15 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 328.6 |
| 334405f9-e8c7-3ac7-bdad-f29587c60228 | -8.6811 | -45.4814 | 2025-11-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 156fa84b-05c7-3ae2-95c4-82d2df5e3218 | -8.159 | -45.0351 | 2025-11-15 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 2f98839b-1131-3ad7-a21f-bd8afd41c694 | -11.9363 | -46.2335 | 2025-11-15 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 402c1391-947d-39d1-b299-5e0015353ef2 | -12.6938 | -46.7576 | 2025-11-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 428fed13-b170-3f09-89f0-9b9d676a975c | -7.442 | -45.2184 | 2025-11-15 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 59df9f5e-fb27-3cb1-88f9-85a31aca1037 | -8.5607 | -46.0588 | 2025-11-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 983.9 |


[Clique aqui para ver as próximas entradas](README65.md)
