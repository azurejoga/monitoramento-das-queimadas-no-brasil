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
| 1f87c8d1-2615-3d21-a3d0-e05a0f53af91 | -6.51256 | -44.60819 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a01a3e6-1d21-3b01-a61b-de41f0a645ee | -2.44397 | -47.33229 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc8b9c2-4f0b-3793-addd-f592472520aa | -5.65693 | -43.71295 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e196d2fd-af43-3acc-97f5-35602a1a048c | -3.03802 | -49.4236 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11913bd0-57c5-3da3-a204-16f4ddc3966b | -2.58504 | -51.92218 | 2025-07-19 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65b75ddd-f692-3e0f-aa1a-fd5477727523 | -7.48369 | -47.49723 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a8383aa-92e6-318d-b4da-1404d5b98fb7 | -2.44839 | -47.3259 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 664c64ed-1c0e-387b-b75d-a3f66e92a5c0 | -2.91148 | -48.24726 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8da7bc57-d464-33da-a1d8-dfdb2c935a62 | -8.7422 | -47.73456 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01726193-4ac9-3b1c-be7a-cf4845c6098a | -7.95248 | -43.95291 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 820dafc0-9a2a-3b17-9a95-8232869d6749 | -9.6055 | -43.86291 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f69cbdd6-21c1-370e-ab81-886164e4c11b | -2.44065 | -47.33177 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9bcb0b4-5ce4-3d8d-ba21-fefccf9030a5 | -3.59064 | -48.93996 | 2025-07-19 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1750794-f3c1-357f-8a05-64845bfff4a0 | -6.89159 | -45.24333 | 2025-07-19 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4c7b587-dcd3-3b87-9e8e-42c0ffb4fd99 | -2.90476 | -48.2462 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0da41c2e-69ce-3b06-8cc8-f9d847f68d86 | -7.48647 | -47.50126 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64385207-f27e-3ce2-b3df-a18a399c6610 | -8.53621 | -47.84182 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6143d431-2c9a-31a1-b88a-dca5c81c005f | -3.11686 | -47.0143 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25279abb-da2f-34de-bd61-d826b6b004be | -8.54841 | -47.85091 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 359a5f38-31fc-3eb7-a0ec-fe4b29063999 | -6.13353 | -47.30705 | 2025-07-19 04:34:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4acd720c-6967-33b2-9c0a-9b7886140683 | -8.53288 | -47.84129 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f04e4398-c11f-3fd9-a122-ad74fbda941f | -6.7529 | -45.51561 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0630536-6d7e-3bb7-b0ec-b31678332d14 | -6.78678 | -42.99563 | 2025-07-19 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b79a2954-ea5d-36cf-a632-54c6996140a3 | -2.44452 | -47.32883 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f7a6c98-4d77-3f71-a677-0989e813d5e6 | -6.91758 | -44.83458 | 2025-07-19 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e95dd399-f224-3a08-ae15-915082a411d0 | -4.1262 | -47.6538 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 999645d0-e3a9-3d5b-a265-a4e1afb259ac | -4.25139 | -48.54465 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dad6de4c-e530-38ce-af25-586254d079da | -3.03391 | -49.42688 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620636c4-f15c-37f2-996e-28fdfb27218a | -4.48295 | -46.07508 | 2025-07-19 04:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 974e6ccb-7643-3c25-bafb-60b52093226b | -5.65177 | -43.72152 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7642bfc1-d947-3f89-815b-f927f13e341a | -3.1279 | -47.00896 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e0de952d-e38d-35ec-ba37-838ead422ce8 | -3.29043 | -42.53451 | 2025-07-19 04:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad7acf3-9899-3442-b6d4-31602919476b | -4.77744 | -45.35074 | 2025-07-19 04:34:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52fc402a-27e4-36d3-9548-f39dc35bb53e | -7.11296 | -44.38009 | 2025-07-19 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0ed42bc-8f58-33de-adc7-e3e3c95de2c3 | -7.48427 | -43.9371 | 2025-07-19 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20359ac3-f77a-399c-8b7c-8f65100230e1 | -6.15583 | -47.76501 | 2025-07-19 04:34:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 044c61cf-65ed-38a8-af81-33fd754a8266 | -5.80042 | -43.63276 | 2025-07-19 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c80fb6e-8e71-3c05-a420-6819f0e5ac21 | -7.57993 | -49.40501 | 2025-07-19 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de86784-4f80-38b7-bca2-537fca51aeea | -8.74275 | -47.73105 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b4b1c7e-b891-3c11-b58e-1363aff2c054 | -7.48314 | -47.50073 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 886924fd-6df0-3059-b460-7ece73153b05 | -7.63074 | -44.29816 | 2025-07-19 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b998529b-37fa-308a-ba16-9da1460b7fc2 | -2.91654 | -48.23713 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02c356e4-4933-3dcc-b821-0d4af11f9792 | -8.06948 | -50.07536 | 2025-07-19 04:34:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 525044da-c56a-3ab1-9a2c-8f96eb4ffccd | -7.48925 | -47.50528 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b2d7cb9e-2472-3ff2-8186-20c7ef4da25c | -7.5805 | -49.40142 | 2025-07-19 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 126cecf3-aa35-3a93-aedb-691d4f426882 | -2.90532 | -48.24265 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e801b47c-6398-3d5e-afe3-f8c3f29f2bba | -3.82709 | -47.74457 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49476461-217a-3302-85fe-282742c446f6 | -3.39884 | -47.4787 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbaf0e61-5c5e-3952-b1ef-a85b3b52dc80 | -3.39056 | -47.48802 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6b954bd-a4ff-35b7-9e42-48b61528d58b | -8.14631 | -43.43176 | 2025-07-19 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6e26b46-6af2-31ce-8453-b2c063aa13d4 | -3.83042 | -47.74509 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e1cc1b8-ccad-3d06-a292-4994595882ff | -5.88572 | -45.1987 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e7ec562-9194-3898-b924-10e74dbf73e2 | -4.53402 | -48.02357 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bad3c795-ef68-32df-980f-39f7cd386e5a | -7.63008 | -44.3026 | 2025-07-19 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4dbbfe8-a0e1-36b7-aae6-de068fc8be56 | -7.4898 | -47.50178 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e134a4c7-5748-3e36-bcb3-b47af424bcf8 | -4.25476 | -48.54517 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04913d87-88a5-3da8-befc-955fb0440d6b | -9.51593 | -45.43026 | 2025-07-19 04:34:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dd373df-87e6-3214-b18e-91a241405b63 | -6.72505 | -44.85005 | 2025-07-19 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b26158a5-8013-3635-8e5d-e45c358aff46 | -3.38724 | -47.4875 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaaa5ad2-66fb-38f6-b372-b56962e4ace4 | -7.4881 | -43.93762 | 2025-07-19 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dd5e386-9ab3-300a-b7fc-c740d103b9e4 | -3.97786 | -48.41787 | 2025-07-19 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ac85a2b-05bc-3668-aa0b-a7a99a47d7a5 | -9.59042 | -43.85538 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f847dd5d-d93d-3d4b-aed1-fe892e70d436 | -3.67992 | -43.05085 | 2025-07-19 04:34:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7927c88-b0bf-3032-925e-d5c5d7bf8cf7 | -8.41573 | -46.87142 | 2025-07-19 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07376791-1a6f-3a47-86c4-35d36f9300ba | -7.17512 | -44.09686 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea5fdd1-0608-3a21-ad08-156d7c8512a2 | -8.39331 | -44.02939 | 2025-07-19 04:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 858e891d-ada3-328a-b5ba-0b588960001e | -5.88221 | -45.19818 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c733c5-3f65-33da-8f7b-74b66ffeff91 | -9.60227 | -43.85724 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 984c14bc-5c8c-3e94-8dec-603850cb08a1 | -4.81846 | -47.32026 | 2025-07-19 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddd3a676-a427-3eed-92fc-3760856e16e7 | -3.03329 | -49.43072 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db07c4e7-1465-30dd-a3b0-8c73e92afb74 | -4.25419 | -48.54874 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a753478b-d70a-3e3d-81dd-10912af4a22a | -3.46815 | -50.25444 | 2025-07-19 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cee65a3b-b790-3263-9d1c-bf941f74245d | -9.59101 | -43.85902 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ab6b303-5194-31bc-b77e-9c4b13827d36 | -5.18451 | -44.95702 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d042fb60-fe31-3171-9554-e1ad8d10dfd2 | -4.55953 | -48.01331 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63b28b27-e7b1-385e-8581-5bd8102f4ac0 | -5.91762 | -43.46455 | 2025-07-19 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47117b2c-1951-3895-98c1-204db8d0e19c | -3.95456 | -49.44297 | 2025-07-19 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ab2b094-9b9f-3228-972f-797f933e1114 | -9.45354 | -46.88349 | 2025-07-19 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 037b1a9f-02da-3861-a403-158f0214e16c | -2.58449 | -51.9257 | 2025-07-19 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8104ba89-a2a4-307d-bc60-9127424fbcd6 | -3.11355 | -47.01378 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d36e3f94-c863-3287-b4da-0f70f24baedc | -3.14062 | -47.01448 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0c00414-034d-3e7f-8d09-375fc907d8bd | -3.3619 | -49.16642 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0b533a6-3606-36fc-bab2-d2b01d165638 | -7.70902 | -47.2878 | 2025-07-19 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f487da6c-f725-3ea3-a545-73751bbb9a60 | -3.29507 | -50.75278 | 2025-07-19 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 357c3b5b-b806-30ea-914e-b5711dd6a55e | -7.48881 | -43.93284 | 2025-07-19 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 037d31e6-969c-332a-b9c4-3b3083ed22ff | -5.84859 | -46.72475 | 2025-07-19 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 861287e7-7c4f-3c6b-b093-018c081ae684 | -6.16813 | -48.05084 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 643263f0-30ec-3406-8985-65a8de39b556 | -5.18511 | -44.95309 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 543ede32-ce2d-3886-bdb1-260792de402c | -8.01377 | -43.67466 | 2025-07-19 04:34:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80d6eca6-9682-3874-8b31-88b4afd50881 | -8.53233 | -47.84479 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c29b3a44-a1ea-32aa-abcf-0a6e1a606dda | -2.92356 | -49.07274 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e155a191-61f3-30c8-84f5-3c5b22901043 | -7.17888 | -44.09748 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da18cdd9-374a-347a-8da5-622e62daeb16 | -8.32536 | -47.49992 | 2025-07-19 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b6fa5f8-b0d6-3a19-8b2e-87dd5ba96c7f | -7.18314 | -44.09563 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b890b0e6-fd88-343a-97a0-90a279b875b3 | -4.10581 | -48.20653 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c548f70-a5f0-3962-bbe9-aa6a5ff3974f | -5.84804 | -46.72828 | 2025-07-19 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89138812-5f45-36e5-bc18-1d9054ebe313 | -3.51562 | -47.21085 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 038a897f-b753-3214-b50e-2b6326da1bd6 | -4.54567 | -48.01469 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a266b04-1e2b-3f9e-8289-04621e3477d7 | -2.44784 | -47.32935 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44c722b5-4245-3c4a-a219-e2ce97afbefc | -6.97641 | -42.80576 | 2025-07-19 04:34:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
