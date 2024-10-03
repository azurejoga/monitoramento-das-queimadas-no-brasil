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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fd13f7e-7922-3cfe-b312-0ad672e022f4 | -19.88969 | -42.1046 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 9ef99e67-1245-3ce9-9d5d-292a5fab2c35 | -19.88919 | -42.10901 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 688d2230-3162-33e7-84c3-ed536b168bad | -19.88869 | -42.11339 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 9656322b-4122-3321-87e8-bd3bf6fb6f7d | -19.88509 | -42.10405 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b52fe19e-559b-37ec-aac6-ea96e7526295 | -19.8846 | -42.10841 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 793f0ad4-7f27-3c85-8443-2439dbf87fe0 | -19.88411 | -42.11269 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 4dc142fe-1bca-3032-ac44-46596d092fe4 | -19.85944 | -42.37006 | 2024-10-03 04:29:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4bdecab-1000-30ef-a214-16728c87a8d3 | -19.85894 | -42.37438 | 2024-10-03 04:29:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44326666-eb95-332d-9545-bb0f55682ef0 | -19.85491 | -42.36965 | 2024-10-03 04:29:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ecea7c1c-7e04-3811-920d-1d857e843f60 | -19.8544 | -42.37401 | 2024-10-03 04:29:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| adbf9bcb-9e02-3954-9cc8-1816686a706a | -19.72068 | -42.42525 | 2024-10-03 04:29:00 | NOAA-21 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d0a233e-dd14-362b-93af-4966eb3dd33a | -19.71887 | -42.42265 | 2024-10-03 04:29:00 | NOAA-21 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9db44b29-c23b-3b31-9a77-9a1f648c7c05 | -19.69234 | -42.03858 | 2024-10-03 04:29:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cdbe9adf-3a64-3aec-90bc-5cca61bfe715 | -19.68835 | -42.0326 | 2024-10-03 04:29:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f0443a2b-54c1-3f0b-ad6a-925efe848bf1 | -19.68778 | -42.03757 | 2024-10-03 04:29:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c3700470-7f3a-38b4-85f0-9305fae9ab1f | -19.6832 | -42.03679 | 2024-10-03 04:29:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 20175192-fc7d-3fa6-bbe0-01d7e8c3de98 | -19.52594 | -42.88633 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 10a6d781-8c47-3192-8f41-bf044872b98a | -19.52052 | -42.89454 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 867d5ffc-b1c4-3f80-9b27-87b7f06692c5 | -19.50574 | -42.87096 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 845dca72-a6d8-3c7e-b2df-513075352ca0 | -19.50402 | -42.88523 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 042418f7-3f35-3092-a9c6-b2bec7a2af30 | -19.50352 | -42.88937 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 50f47925-91a0-3a0e-8cf0-873d2c342e3b | -19.50076 | -42.87573 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 67fca7da-e828-37c2-8e35-252c3f463ac8 | -19.50016 | -42.88076 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c709c4b3-4a8b-3dc2-9c41-ba3fc995715e | -19.49638 | -42.87548 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8f7a3b76-66b3-3651-b803-a8ba30ce3856 | -20.55068 | -43.36726 | 2024-10-03 04:29:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 60d1c0fa-0c39-390d-a76d-bf12ccd28b85 | -20.54968 | -43.37546 | 2024-10-03 04:29:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 66b3dacb-42c3-3fa5-a10e-36d3d8a9c133 | -20.54693 | -43.36248 | 2024-10-03 04:29:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0d1be410-5289-3cea-a530-32e24f41e38e | -20.54642 | -43.36661 | 2024-10-03 04:29:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9ca81dde-c382-3b98-b6c3-eb1021137944 | -20.54217 | -43.36594 | 2024-10-03 04:29:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b60b51b-416a-3528-8d77-b398697d1d75 | -20.4791 | -43.17995 | 2024-10-03 04:29:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 35af604f-4d1d-3daa-9090-a7922b3fa4f0 | -20.47429 | -43.18345 | 2024-10-03 04:29:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d14142c5-71c5-3c1d-adb4-6c4e75475d80 | -20.41581 | -43.55408 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1c849ca2-e93e-3dc7-bfbe-2f55b8824e52 | -20.37555 | -43.25506 | 2024-10-03 04:29:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e135ea97-dd5c-35ac-ae6e-b705900d0316 | -20.37428 | -43.25238 | 2024-10-03 04:29:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c0836f22-6dd8-3785-80cc-86e77f59be31 | -20.28631 | -43.52447 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| abeb5e14-c8cc-337e-a23e-24ed006194e0 | -20.28256 | -43.52016 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e24d18f4-32b8-31e1-bccb-e220b52fc66b | -20.28206 | -43.52425 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a9948e97-37ca-3d1a-9c2c-f01f18a4d94a | -20.27835 | -43.51962 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b664d733-447c-3413-9a8b-17685938207c | -20.27783 | -43.52392 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d67871a8-4525-37b4-8156-558643ccbb0d | -20.09656 | -43.28079 | 2024-10-03 04:29:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 696ef6b5-f0ec-3f2d-8e76-f9763e58c391 | -20.07379 | -43.217 | 2024-10-03 04:29:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 356d0791-86d4-3426-967d-53db3b828d93 | -20.0695 | -43.21648 | 2024-10-03 04:29:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7a30aef8-bf42-3d3b-bd0d-ad95376781d3 | -20.06523 | -43.21584 | 2024-10-03 04:29:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| db0234c1-c970-32b8-a58d-071b9162f47f | -19.992 | -43.14734 | 2024-10-03 04:29:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 643b435f-b125-37a9-b9e3-f42b9aa6089e | -19.98772 | -43.14664 | 2024-10-03 04:29:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 287d44fd-637b-3a00-84c0-c90f606da147 | -19.87401 | -43.16376 | 2024-10-03 04:29:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c269dcf9-5aec-39a4-b62d-e16ec233a78b | -19.8697 | -43.16339 | 2024-10-03 04:29:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 480d7754-1db4-39c1-b4c5-36778eecbdfa | -19.44316 | -43.06393 | 2024-10-03 04:29:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d0554a1e-8022-3cba-b7e3-bc3c0878a844 | -21.66116 | -43.52594 | 2024-10-03 04:29:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c7dea643-e26a-3c70-9d9e-f6af5e16f41b | -21.65639 | -43.52955 | 2024-10-03 04:29:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37e0805f-c17c-32c8-9671-8699148617de | -21.46006 | -43.70233 | 2024-10-03 04:29:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0c333ad9-c752-3d58-be9a-991ee89518d2 | -21.33683 | -43.4342 | 2024-10-03 04:29:00 | NOAA-21 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55901220-5ca5-3248-9e06-bd7869c9a4fe | -21.14578 | -43.30612 | 2024-10-03 04:29:00 | NOAA-21 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04f006be-f18f-3ce7-9035-1b2c71861562 | -20.95672 | -43.31144 | 2024-10-03 04:29:00 | NOAA-21 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c351617b-81a9-3bd5-8336-d98d2a65ce44 | -20.93195 | -43.37316 | 2024-10-03 04:29:00 | NOAA-21 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a9c70622-78f7-3a59-894a-0416bac78651 | -21.79244 | -42.48862 | 2024-10-03 04:29:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 89a74e5e-a0c0-3d7a-ad04-0d63f3795b18 | -21.79185 | -42.49397 | 2024-10-03 04:29:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0a91665e-404f-307f-b749-fd3a1dde62f2 | -21.61478 | -42.79469 | 2024-10-03 04:29:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4700618e-5f32-3457-aad4-1e5f2b60aebb | -21.61275 | -42.7917 | 2024-10-03 04:29:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 65835285-e189-3098-bf0a-6ffdd70b5e00 | -21.61089 | -42.78857 | 2024-10-03 04:29:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fa73e76-98e3-34e8-a9b7-6b2956aab128 | -21.00257 | -42.60373 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79c0ca53-c66a-3495-a114-9b20646e514b | -15.7735 | -43.57845 | 2024-10-03 04:29:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b5a2c6c-149b-3b3c-b4fe-07b5a63ed371 | -15.66069 | -43.9154 | 2024-10-03 04:29:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0007edcc-d85f-311e-ac76-c71ac2ded7bc | -15.659 | -43.91383 | 2024-10-03 04:29:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24fe005d-047f-3f8e-a39a-1fe4865df935 | -16.22355 | -43.62381 | 2024-10-03 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0290417-7f30-3932-b268-3f809dd28137 | -16.22295 | -43.62051 | 2024-10-03 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26042dbf-e001-3594-ad7c-84d085163aef | -17.92337 | -43.51496 | 2024-10-03 04:29:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6198af-d883-3f81-8a88-60a497933c65 | -17.59455 | -43.19618 | 2024-10-03 04:29:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3ba3a04-44f1-3f81-b8d9-d80d4d91a27b | -17.59205 | -44.27689 | 2024-10-03 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ecd1cac-2788-34ee-aab7-809ce6bc46c0 | -17.26235 | -43.59277 | 2024-10-03 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c2edf2d-af63-3e91-bbe7-a24150747ed7 | -17.25797 | -43.18234 | 2024-10-03 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8987cf79-a00d-32e9-af2b-8b1d647bb4bf | -17.2567 | -43.18151 | 2024-10-03 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c914546-ca7e-31e4-b7be-79c0d7828acb | -17.25574 | -43.18919 | 2024-10-03 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b627331-d5a9-3c93-8aaf-7d6ddf034854 | -16.68008 | -43.88543 | 2024-10-03 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0c722e0-5555-30df-8161-43399825875e | -19.13564 | -44.64172 | 2024-10-03 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0ea1fca-9efc-3ab9-bd6e-09e9ca0b287c | -19.0689 | -44.41543 | 2024-10-03 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b192501b-4ccb-3fc4-adac-ac8a11a814a3 | -19.06636 | -44.40411 | 2024-10-03 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06277559-81fa-3e0c-bd98-0747d7baae35 | -18.60048 | -43.92556 | 2024-10-03 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7cbf58e-4032-37ce-9a49-308d11b96fb9 | -18.60001 | -43.92919 | 2024-10-03 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93126b48-ab2f-372a-9fbd-d1debc492e48 | -18.59955 | -43.93282 | 2024-10-03 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4601e73b-0666-3b4a-8ce4-f4eaa63e38c3 | -18.59909 | -43.93642 | 2024-10-03 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81368ac7-f8d7-3957-b89b-344d58f07088 | -18.59862 | -43.9401 | 2024-10-03 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9af0eb42-432b-3bd4-9775-6cb89599ced4 | -18.38372 | -44.0293 | 2024-10-03 04:29:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1896faef-592c-359f-ab6e-401b1ef796c7 | -18.34498 | -44.02712 | 2024-10-03 04:29:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83906fbd-4f69-316f-a44c-d0f84a099cac | -18.34405 | -44.02311 | 2024-10-03 04:29:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ec28df8-5f47-3c2a-892c-e69fa80140d2 | -18.7674 | -43.38764 | 2024-10-03 04:29:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 4a22c375-76ce-30e9-843c-64df0285642e | -18.76325 | -43.38692 | 2024-10-03 04:29:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 445309a3-ec74-34c0-9aed-96d41ec5cee9 | -18.54129 | -43.25806 | 2024-10-03 04:29:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 51a1350c-39a7-3298-a328-7ae3f7664a01 | -18.31612 | -43.23456 | 2024-10-03 04:29:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a58c03ed-b8d6-303a-8f68-d8df12d82008 | -18.31195 | -43.23391 | 2024-10-03 04:29:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7a4f8436-ed2a-37c6-a858-1cb6766b112f | -18.31141 | -43.23815 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| afb2eacf-79a5-3fb0-9910-7ef035be4466 | -18.31091 | -43.24202 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c52bbb5-c57e-396a-b28c-ad69b266e13e | -19.46047 | -44.13509 | 2024-10-03 04:29:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2bcdf9d-a8ac-3d6a-933f-0baea010930f | -19.27501 | -43.76798 | 2024-10-03 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd5182b0-f5bb-3af7-9ab5-a09b056bf6a2 | -19.27454 | -43.77172 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3c203c7d-d7f8-330f-94b2-edac1e9c41ae | -19.27405 | -43.77559 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 70001f24-d0a2-3975-be56-6871b3a277a7 | -19.27309 | -43.78328 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91a4aa5e-67e7-3acf-9a10-afc8e4aa3d86 | -19.27092 | -43.76741 | 2024-10-03 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5a7ef80b-408a-32ed-8cc3-1b8404834ed9 | -19.27045 | -43.77116 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 75cca9af-ba03-3820-b926-e3b79e237efd | -19.26948 | -43.77893 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README102.md)
