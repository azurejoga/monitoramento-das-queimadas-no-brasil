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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09f56eb2-1a23-33c8-b932-a03e46fe8fd9 | -12.7015 | -48.83799 | 2025-10-23 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71a85af3-dd67-36c5-a2e4-98d82c4914c4 | -12.01293 | -46.74597 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ad4e0a5-9dc3-3eb7-9e64-8efaac4156e0 | -12.00302 | -46.7824 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 859dc11d-dceb-3bda-8826-1add4776e976 | -11.99321 | -46.77809 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99b5e88a-0639-3214-83a4-d8d5910ab1c9 | -11.9987 | -46.77571 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c7ec721-c428-341d-8639-962ead7d3205 | -13.12387 | -48.24721 | 2025-10-23 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5875c825-9889-3123-88e0-6f6ad1688682 | -12.00263 | -46.78538 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b3ffd36e-32ef-31c0-98b6-8cf1d705bf3a | -12.13031 | -46.72626 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c0183fb-fcd3-342a-8321-4403df52e8ee | -11.02809 | -51.64387 | 2025-10-23 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83da0294-af77-37c8-8360-a61747e7689a | -9.9769 | -47.07181 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a60137c-fdfe-3162-9bc4-cbcb9ad70f75 | -11.74399 | -51.191 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd7477e7-e603-3b7c-a948-5fa414a36d11 | -10.5256 | -50.23589 | 2025-10-23 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78d2f6df-5585-3fbb-b421-a7a05b591d8b | -11.99282 | -46.7811 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56b109ed-a262-348a-840f-16de4c807e9a | -10.34915 | -62.84454 | 2025-10-23 04:57:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f233e967-c42c-3d55-a669-f6f087b01658 | -10.38836 | -47.10522 | 2025-10-23 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df395706-365b-385c-a421-807dd1a8b2f8 | -9.97205 | -47.0711 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d923e5d3-4f62-328e-9011-819ca8c6c939 | -11.99244 | -46.78407 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7186e89f-5573-3641-b17b-1c29cb2dbdfb | -11.97174 | -63.92065 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b7e57e-b47b-3ecd-b8eb-db81a0a5c1b7 | -9.23368 | -45.6045 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42d7c20c-cccb-37d4-8a45-102272822cbf | -9.72274 | -64.97287 | 2025-10-23 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae96539a-197a-33c2-b83e-822c343efbd4 | -10.9073 | -50.11497 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f55a5d9-734b-3a24-b30b-967bbd6e6924 | -12.9022 | -48.48993 | 2025-10-23 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8636f5cb-3768-3de9-a5e3-3c7dc7abf3f8 | -13.90048 | -48.37663 | 2025-10-23 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e698da2-86b8-3ea0-bee6-6ef7b41c8431 | -11.35577 | -49.79091 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7894c1e-f3fb-3359-8dc8-69f7457013e5 | -13.04002 | -47.23385 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb54ae61-baf9-3653-9511-686c1fb420a6 | -12.10052 | -64.29859 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34681d5e-4ce1-3f8c-97dc-da32aee7b51a | -12.09446 | -63.62369 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcb278cd-e26d-36e1-bc38-63f2266580c1 | -13.37247 | -46.64346 | 2025-10-23 04:57:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e846b6c6-15cf-3096-ac05-a7591a2737c7 | -13.45952 | -48.82832 | 2025-10-23 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f30d5be-bce8-3e52-b152-34d0ea40ee17 | -11.35884 | -49.79902 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 46b4f86c-abca-3bc9-8d53-d185b972a0ac | -11.9987 | -46.7757 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 140fdaaa-c09d-30e7-999e-14f86c6b0213 | -14.20715 | -44.52296 | 2025-10-23 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5981b3a-bbba-30f6-8bb7-76e175280e78 | -12.01845 | -46.74346 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 584c4029-af82-3137-93df-9e7555120adc | -10.48737 | -51.86994 | 2025-10-23 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9660f56c-98f1-36b0-bed5-d84d9d79acdf | -13.36763 | -46.63952 | 2025-10-23 04:57:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8026b859-56d5-3115-86f2-3dc4e207eea0 | -12.69832 | -61.06384 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b47dbc50-f2dd-3e9b-9434-3e9a7caf7caa | -12.80285 | -60.66633 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed41076f-80d0-38d2-9619-91e826b2f944 | -11.99831 | -46.77874 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79a2aa3e-f9fd-32d4-98b2-aec3dd47b81d | -12.78376 | -48.57513 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e0eb96e-84aa-321d-bba6-6b8c6eb60ed0 | -12.02173 | -46.74213 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8cc465e-1ad8-3fa1-a350-63b8611245c7 | -8.35096 | -46.1822 | 2025-10-23 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b87f59b4-377a-35b5-b3ea-aa4cfb0448f3 | -12.24524 | -49.59266 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 393027f1-e624-322f-9ade-da4c43384d47 | -12.52115 | -48.58103 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12151844-5339-30f1-bbc3-772ad7db704c | -12.25 | -49.58933 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55fcf9d6-e5f5-3b8b-8da3-925703fb1187 | -12.69763 | -61.06769 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17ed4e62-f9ef-3239-99f5-ae8349156be4 | -10.24988 | -47.99815 | 2025-10-23 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa951372-e6ec-32c0-b743-04e03aacad4b | -13.05201 | -47.21966 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c249ff2b-6fc7-3ec3-b369-f7659f287a21 | -13.79154 | -52.7721 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 797cd4c9-3a8d-35a0-929e-c6d4090889c9 | -9.72198 | -64.9769 | 2025-10-23 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995eb0c1-72f8-3278-b6b9-f60de94909b5 | -14.87002 | -59.63673 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f40d9c60-5c00-3aa8-85a2-380c5bde208f | -17.60793 | -46.62461 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 7ba7f12c-45c6-3e61-bb03-fd13e10c3f38 | -16.49872 | -49.74225 | 2025-10-23 04:59:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03867104-e652-33cb-88f6-01a487feca1a | -19.95852 | -45.60341 | 2025-10-23 04:59:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 813d29e5-8470-3d7d-8783-87a5716e296e | -17.61512 | -46.60971 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d9afe0-0bdf-3bcb-8b76-3091fb19d203 | -17.61157 | -46.59 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f50498a-dac0-3da9-8c42-daf6a84cd78a | -21.84204 | -43.71276 | 2025-10-23 04:59:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a2b5656-6a72-3d42-9851-c933d4be84e0 | -19.26455 | -49.35307 | 2025-10-23 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5b73fd03-9ac3-3bb0-a3ce-ee5488cdc483 | -18.71905 | -46.83232 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed68de78-dc3d-39dc-87a9-6fa0e2dfc7e0 | -14.8713 | -59.63418 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30ecd3e9-bdee-3e55-992a-f35e7546b3ac | -17.61078 | -46.59756 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ad4efd7-7415-375e-b139-0e6f54d616c1 | -15.54895 | -59.58017 | 2025-10-23 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0112a218-e76a-3599-8365-2057284f02c3 | -16.47868 | -46.47566 | 2025-10-23 04:59:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422fa123-239b-30a1-b7f7-1888b58e903a | -16.47829 | -46.47915 | 2025-10-23 04:59:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dbf6ae9-f6da-37fd-babe-7233f85f5481 | -16.51747 | -51.40365 | 2025-10-23 04:59:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f9843ab-50fe-39d7-80f5-49fc261b8dc2 | -17.65024 | -46.64874 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f4a11dd-35fb-3dd1-b653-7f001db975c1 | -14.7883 | -59.24255 | 2025-10-23 04:59:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8c8b533-6147-3f48-9474-c185c82fde0f | -17.60997 | -46.6052 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8d3ebe0-4026-3a05-b90e-7e3a2b0e00f9 | -17.14903 | -53.311 | 2025-10-23 04:59:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ac8e2ea-5cf9-3d17-9df9-00a15e3c6565 | -17.60833 | -46.6208 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 17acdf8f-98c4-3121-88a7-74a701d60692 | -17.61471 | -46.61362 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a040a556-cd94-3db6-9425-b005d1d78c66 | -18.23468 | -47.41852 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c365262-70de-32fd-92a5-4ae48a4fa188 | -18.7256 | -46.82999 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b5e0aae-6efc-32bf-bb61-0c2d09b517de | -21.84213 | -43.71388 | 2025-10-23 04:59:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 90211033-7bf2-3880-855b-ccc32e53d3d6 | -17.7975 | -47.62319 | 2025-10-23 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9c94e18-7c1f-3770-8846-f805f2711942 | -18.72461 | -46.83279 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff3eab26-335d-3a51-9562-78cb8daeeb57 | -17.61791 | -46.5832 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 239eecee-ff90-38d6-a3a8-1cd785916ae2 | -17.20842 | -47.6554 | 2025-10-23 04:59:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea681f3-7846-32d7-8c74-0c6572b1e480 | -17.79307 | -47.62278 | 2025-10-23 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 997e7556-44fc-3bdd-b354-a7225c67f562 | -18.22974 | -47.4143 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f4b2e7d-990c-3e07-b81d-76bc5afe54ff | -15.67159 | -53.3484 | 2025-10-23 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81bd74ed-f5ac-3645-8488-ee765e31e857 | -19.26394 | -49.35832 | 2025-10-23 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 36ed750c-2d93-3b74-8235-dceb96496784 | -20.49298 | -45.98132 | 2025-10-23 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 311e6bbf-cb58-3dec-a3dd-62eaf64c6e4e | -15.9166 | -48.32216 | 2025-10-23 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e8d57f9-b575-3321-8779-2c0865a59e98 | -15.36232 | -50.55955 | 2025-10-23 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79ea1b26-74fc-3082-acf0-2e93fcdf9303 | -17.61117 | -46.59378 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b000330a-9e62-3557-b49e-8da5663ccf76 | -17.60522 | -46.5969 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b124938-169d-3a47-bfbd-367662055927 | -19.95805 | -45.60851 | 2025-10-23 04:59:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02aed71f-ae67-318e-b787-64a87a1c83fa | -20.70071 | -55.43641 | 2025-10-23 04:59:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c34cef39-aa54-3011-b0a5-20520d573893 | -17.60401 | -46.60854 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 01e4c884-359b-3df1-a2df-9565fd838390 | -14.8757 | -59.6306 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7910764-89e4-349a-8bf0-68492ecbf39f | -17.61308 | -46.62901 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d244f8e9-3e34-3509-8192-6a56c7cbdd2a | -18.14063 | -52.51188 | 2025-10-23 04:59:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6aed44-ee1e-37b9-a080-77b379bc08c3 | -17.61038 | -46.60136 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c32d950f-6718-31f1-9e4d-cd9f27ca3bb6 | -16.88221 | -52.87955 | 2025-10-23 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4b55cc2-e5fb-3147-9587-7f7b7b3d191c | -15.63069 | -55.84674 | 2025-10-23 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07c14f5b-b138-33d9-89dc-17c63d95bfe9 | -15.90094 | -56.75763 | 2025-10-23 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36d0779c-c302-34b3-b5d1-71f04a2e21b1 | -14.87444 | -59.63316 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cdb4d5a-e85b-3ccf-abec-cd51a73daf6c | -17.6068 | -46.58183 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cd29926d-81a8-3645-8369-e467a49a8d0e | -15.60955 | -55.93857 | 2025-10-23 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ec5c44-0ef3-3118-8550-9f0a8fa23601 | -15.84014 | -54.86285 | 2025-10-23 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README35.md)
