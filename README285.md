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

## Dados Diários - Página 285

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73ef379-a7bd-3875-99d7-e02e54ec6ecd | -11.0566 | -44.0327 | 2026-10-09 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 7e47a662-c5aa-34cd-890b-98927d80d9bf | -13.1641 | -54.3178 | 2026-10-09 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 44fa2faf-d2c0-31d3-b7d8-d4454b5ed0a6 | -2.572 | -56.1646 | 2026-10-09 17:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3249f81c-e166-3352-9620-215c537f6652 | -9.9198 | -44.8585 | 2026-10-09 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 3fec6a11-7175-30bd-b3fc-876684ca51a4 | -13.1636 | -54.3591 | 2026-10-09 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 367.7 |
| 5a13132b-179d-3929-bce2-236260f56226 | -2.4623 | -56.0879 | 2026-10-09 17:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| bd31fa9b-b082-392f-ad24-0310f19cd652 | -9.9208 | -44.7893 | 2026-10-09 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 162.4 |
| b4703cb5-d4d0-3dc2-b1d1-e04c2b97688c | -2.4623 | -56.0682 | 2026-10-09 17:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 19794db3-e703-3803-9372-55bcc2f3df0b | -1.8757 | -56.3133 | 2026-10-09 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2efb9da7-e4cd-3a7f-a2f3-0f91ab286be1 | -10.2488 | -49.6636 | 2026-10-09 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f2439725-224f-36aa-9fe5-e86b51cd8b7b | -9.1015 | -45.1164 | 2026-10-09 17:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| e249f5ab-a3e4-3146-bc92-7d4817465213 | -15.0713 | -41.7982 | 2026-10-09 17:30:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 445.2 |
| 69de72dd-c5de-3399-b675-a43f0c301e77 | -10.9388 | -45.3687 | 2026-10-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 816c53eb-e21f-3365-b307-b57b5dcdf6a7 | 0.5246 | -50.8991 | 2026-10-09 17:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7b4f3d93-8b61-369d-9bc5-9aa535e646d0 | -10.4724 | -47.2333 | 2026-10-09 17:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 8424624f-7dd4-3cd1-9b6e-715f94b77649 | -10.9193 | -45.3942 | 2026-10-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| dd915413-4f88-329e-b155-af0c045852c6 | -12.8303 | -44.6239 | 2026-10-09 17:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1948496b-8915-3959-bfea-2094d987487b | -3.1697 | -58.6244 | 2026-10-09 17:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 332219dd-a217-3405-bb98-d89f130e1c18 | -13.1639 | -54.3385 | 2026-10-09 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 193.4 |
| cde48208-d87a-3ae2-b27d-905210f4c600 | -10.8313 | -47.3456 | 2026-10-09 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 96011376-aebb-38ee-8c32-a328116581ce | -10.2488 | -49.6636 | 2026-10-09 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 89122da6-a53d-34a6-a974-22937b47758e | -13.3671 | -43.8742 | 2026-10-09 17:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 9717324b-f5c7-310d-a703-db701d5b4412 | -7.0038 | -47.6843 | 2026-10-09 17:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b1fce9b7-2e68-3722-89f2-1f9237fe966b | -11.1145 | -44.0009 | 2026-10-09 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| c499e06a-fe5d-33ca-b33c-4d2cc511a415 | -13.1636 | -54.3591 | 2026-10-09 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 312.9 |
| 7419d53b-e9fe-3b4c-b9e1-d16b22854d5e | -2.0586 | -56.3892 | 2026-10-09 17:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8d30872f-7813-3f54-b81d-50aabc2091cc | -11.0562 | -44.0561 | 2026-10-09 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| f5bc2b55-8118-3eaf-bb24-3a6638631807 | -9.9398 | -43.5542 | 2026-10-09 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 677.0 |
| 52869fe0-9912-318a-aa61-e02788ada1d7 | -1.383 | -55.1944 | 2026-10-09 17:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 5fb27e57-47d6-3f05-a375-dd3700223d67 | -14.7822 | -41.5883 | 2026-10-09 17:40:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 138.5 |
| a27a29b7-b2a5-3634-8900-2a6f6f3c8375 | -12.214 | -44.6524 | 2026-10-09 17:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 776.5 |
| 2ff79723-8f6e-3130-8cd1-7f7ee1aba868 | -2.4623 | -56.0879 | 2026-10-09 17:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ecc8cf3d-9750-36e0-8521-2b9d279e280c | -15.3825 | -41.9277 | 2026-10-09 17:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1200.4 |
| 272dc139-99e3-3ead-b6ea-9c865f8b8cc5 | -10.8317 | -47.3233 | 2026-10-09 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 4da08500-d4f7-398e-b5d3-8c14dac53871 | -10.4724 | -47.2333 | 2026-10-09 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 867067d5-4cdb-32d6-b8b8-479088dfabac | -9.1012 | -45.1393 | 2026-10-09 17:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c545a2d8-4695-31b5-951e-8d89acb46439 | -3.4463 | -57.9618 | 2026-10-09 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d74b02d0-5136-3b3e-a40b-7b460b1dd7f5 | -9.7559 | -45.6783 | 2026-10-09 17:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| e99d2b7c-14c1-3887-a7ef-30c8cc9ed79c | -3.1879 | -58.6433 | 2026-10-09 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 2d225582-db06-3de2-9b32-e3d5ae1fb0a0 | -10.9388 | -45.3687 | 2026-10-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| b917e41c-78ec-3315-a0b6-a70d4f88f08d | -9.9198 | -44.8585 | 2026-10-09 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 686.3 |
| 5dd26f04-9ae0-3bad-b395-25ca8b3947b8 | -9.75 | -44.7875 | 2026-10-09 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 9e7574ad-64e4-3c51-85b5-adf9dad1a135 | -2.5492 | -58.0373 | 2026-10-09 17:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9a837671-c862-313b-be11-e633aae23e9a | -15.8531 | -42.0202 | 2026-10-09 17:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.7 |
| 105d2b5a-83a5-3409-8600-5b5133e2595d | -1.2175 | -55.6512 | 2026-10-09 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 304.0 |
| c9f959ed-238f-37ec-8f6b-c10540452ab5 | -15.0713 | -41.7982 | 2026-10-09 17:40:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 668.3 |
| 5fe18e8e-8d7f-34bd-a995-ce099eed4e92 | -2.0403 | -56.3895 | 2026-10-09 17:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f02e9671-4b99-3d73-97c5-adb3e391ba43 | -13.1639 | -54.3385 | 2026-10-09 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 6c2accf6-6fa5-3a96-87c7-46a9ece8f82c | -3.5893 | -59.0773 | 2026-10-09 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 32680d40-08d3-394a-81e2-3b2061ccc9cf | -15.3832 | -41.9029 | 2026-10-09 17:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 864.7 |
| a720cc2d-c1f8-35b3-b593-9cd045f05fb7 | -12.1939 | -44.7021 | 2026-10-09 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 171ab776-c96e-367b-b49c-97129866e2ca | -1.1809 | -55.6713 | 2026-10-09 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7ddb5b0c-ad71-3f75-9d92-9ad0f8c1363c | -12.1435 | -45.3576 | 2026-10-09 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 381c4907-c349-3de7-82ba-96a87e70b635 | -12.1436 | -43.2992 | 2026-10-09 17:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 551f33c8-f835-3cc4-a5ba-472c2511e417 | -15.0516 | -41.8024 | 2026-10-09 17:40:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 321.8 |
| 0fd2998f-340a-3d12-afeb-d56d18a8636b | -12.1952 | -44.6321 | 2026-10-09 17:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 428.8 |
| 3153c3b9-caf5-3182-a672-81ed21668534 | -1.8757 | -56.3133 | 2026-10-09 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 52461b7a-4115-325b-9dfd-36ffb50dbd28 | -2.5689 | -57.4163 | 2026-10-09 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 888f7312-41bc-3101-824c-3c1bafc4c4d8 | -3.5709 | -59.0969 | 2026-10-09 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 227728cb-e059-36ee-a2c8-5e2f77f0397c | -10.9197 | -45.3712 | 2026-10-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b0613cca-4e39-3d01-8452-2f738e494631 | -11.5683 | -45.3959 | 2026-10-09 17:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| faab96c7-0e2c-32b5-90c5-81e2b0216919 | -3.1697 | -58.6244 | 2026-10-09 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 29b6411c-f407-3959-b45a-4a76b818cb70 | -10.4914 | -47.231 | 2026-10-09 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 2b320131-51cc-395a-867a-12ca5a9e5535 | -2.8247 | -57.606 | 2026-10-09 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3772efbb-ab6b-37a3-9f18-7fd64920ca83 | -11.0566 | -44.0327 | 2026-10-09 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 1d6a0b28-d6a5-36bf-99bc-9862021edf4f | -14.4339 | -43.9396 | 2026-10-09 17:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 645.7 |
| ac1e0986-4218-3198-9269-4b6b2db8774f | -11.075 | -44.0768 | 2026-10-09 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 0f713347-08d3-300e-a2cd-c42a12dbab8b | -15.2535 | -42.3741 | 2026-10-09 17:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 273.7 |
| 214d69bc-c362-32b0-a0a5-72f7d0cca3e5 | -10.9193 | -45.3942 | 2026-10-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| fe606db7-8667-3f8d-bdcd-6bb18a5b10ff | -9.9018 | -44.7917 | 2026-10-09 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| d944683d-6b92-3818-96ae-c3313b439600 | -3.4278 | -58.0203 | 2026-10-09 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9afba41f-2cb7-3f27-afbf-ac3ed1e0166c | -2.4623 | -56.0682 | 2026-10-09 17:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 303e3f20-c1d2-3a83-a555-b6fda9795e72 | -11.0953 | -44.0037 | 2026-10-09 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 2e078068-86f9-3587-8c89-5db5c8cfee8d | -13.1641 | -54.3178 | 2026-10-09 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 16c0421e-a127-35a4-9ddb-c756d978e3df | -11.2068 | -45.3091 | 2026-10-09 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cee3ee62-823a-3bca-bc60-df8f6fb529da | -9.9398 | -43.5542 | 2026-10-09 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 5d159f5c-5dbf-3ada-905b-1e1c0b19861e | -2.5492 | -58.0373 | 2026-10-09 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a3f6bb48-945f-3b34-840e-ff049ad6d089 | -2.4623 | -56.0879 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 414363e1-2d3b-3311-96ca-708e1f266da8 | -9.1012 | -45.1393 | 2026-10-09 17:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 660d81d8-60a6-3ab3-af81-47f080c612c9 | -13.1641 | -54.3178 | 2026-10-09 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 29bcf5fa-2315-3ff9-8bc4-8b50de9b5fc8 | -3.4463 | -57.9618 | 2026-10-09 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7546ad50-95b3-3fc0-b78d-d127263e3481 | -1.7117 | -55.8629 | 2026-10-09 17:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 6e2232e8-6111-3ed2-bf0f-09d82bc742f6 | -12.1436 | -43.2992 | 2026-10-09 17:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 2ef9d92e-379f-3ea5-a352-cff6023ef665 | -9.9194 | -44.8815 | 2026-10-09 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 316.1 |
| 98a6286b-3953-3d14-bc31-af6e64361c09 | -12.2504 | -44.7631 | 2026-10-09 17:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1c0d81ca-2053-3b2b-8881-2ea9c24a7109 | -10.9575 | -45.389 | 2026-10-09 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 7d15b67c-5693-3037-87b2-7f1b0a796b60 | -9.1827 | -43.3923 | 2026-10-09 17:50:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| e40c4051-32e3-3743-8c48-b40c51bf285f | -12.2273 | -43.9481 | 2026-10-09 17:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| b78ad178-4b29-3a5d-b035-a706ac81e86e | -8.3014 | -45.7019 | 2026-10-09 17:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 67823a04-fe9c-3ff2-af4f-70efa0d4be45 | -14.4535 | -43.9359 | 2026-10-09 17:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 736.7 |
| d07e1110-9252-3a76-94ed-f5d8fcfcc96e | -11.0566 | -44.0327 | 2026-10-09 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 0c6dea21-7740-3281-9148-e63a6e78ccd4 | -14.0472 | -43.8222 | 2026-10-09 17:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| aa0ba937-1529-3cf8-b7fe-9fbf41517ad0 | -12.0453 | -43.4102 | 2026-10-09 17:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| dd3528f3-ba46-3121-8ca0-f7fdce127b05 | -13.1833 | -54.3158 | 2026-10-09 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| df3ede4c-aa59-32fb-8973-3cd6703311bd | -15.3832 | -41.9029 | 2026-10-09 17:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1042.3 |
| aa3ab452-1439-34a9-bf3f-0861724391cc | -15.2535 | -42.3741 | 2026-10-09 17:50:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 228.0 |
| 9800372c-b316-32c8-801f-d424389fc862 | -1.4301 | -49.0382 | 2026-10-09 17:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 746579fc-0c47-33fe-a477-75878ed74e60 | -3.571 | -59.0777 | 2026-10-09 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6fa01ae1-951d-35d2-bed7-992074fb75a9 | -8.3583 | -44.187 | 2026-10-09 17:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 98fb4be2-ac83-3f3d-b10e-4b427556b272 | -14.4339 | -43.9396 | 2026-10-09 17:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 488.7 |


[Clique aqui para ver as próximas entradas](README286.md)
