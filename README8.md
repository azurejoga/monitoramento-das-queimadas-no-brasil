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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea87e1e9-0925-3faa-acee-d33736c672c3 | -13.3247 | -46.75328 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1be8cf6-3108-3f34-9e2d-da60af9abdb3 | -13.3154 | -46.75456 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 55107bcf-25ac-3c7a-be21-164b5c90a198 | -13.12448 | -46.77273 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65f4ee60-c510-36c6-bd1c-66dc4377f66d | -12.47457 | -47.49909 | 2024-10-01 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2be63770-5427-3214-912b-26c11c5892d2 | -14.0335 | -48.13483 | 2024-10-01 00:48:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c4fafd6c-3dc0-3e87-bead-e570552e8a82 | -13.7505 | -48.15421 | 2024-10-01 00:48:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a077e9bf-7b01-31b4-b37b-70cb0993b8b9 | -16.50889 | -48.06459 | 2024-10-01 00:48:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c31a72db-dca5-3333-9840-90448a6eba87 | -16.50733 | -48.05172 | 2024-10-01 00:48:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b779b25b-0e80-37a2-98fd-b7c4f5f4f55e | -15.7812 | -48.49963 | 2024-10-01 00:48:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3b649889-133e-33d7-b69f-22d80a3a8b08 | -15.28876 | -47.50404 | 2024-10-01 00:48:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ddcc4f75-7d5b-3c1a-bf69-3301ddcf7cdb | -15.28733 | -47.4929 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ae01a80c-2187-3a40-85d9-30317ef685bf | -15.28601 | -47.48246 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6c7e5a09-6621-3222-9faf-d4e736a94920 | -10.7805 | -48.75904 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 9d6e1d5c-19e8-3a66-91ad-394ab789a106 | -10.78027 | -48.76494 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c56ffe7-1b9c-345f-a01f-6fde3b52dd79 | -10.77892 | -48.74713 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c94cab60-f6c7-3c5e-b80f-a5732b216432 | -10.77876 | -48.75296 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 6f3faa5f-6911-3472-8dcd-0be5db3b8db6 | -10.77038 | -48.76044 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f0a34f88-5592-3995-be31-601652ddcd7d | -10.7688 | -48.74845 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d87c9a36-f2b5-3088-ac05-55ef90f3992b | -10.75168 | -48.77514 | 2024-10-01 00:48:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eb3f7e73-4435-3100-b8b9-769f869e9556 | -10.57506 | -48.05534 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 930a6e0b-2c6f-33a7-964e-d5837a59714b | -10.57354 | -48.04403 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9d101a53-4f81-37f6-a5b1-939b7476bc60 | -10.57209 | -48.03312 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a95f0908-d6ae-3e91-b442-25ad3c4e3f5a | -10.56396 | -48.04579 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0686f446-d7c0-3121-9b78-859ca916461b | -10.5625 | -48.03478 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| de936a37-6cc5-3164-ad62-bb4970025f63 | -10.5587 | -48.08027 | 2024-10-01 00:48:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cd4c9200-f465-3235-90da-18d8e8692e1b | -10.46544 | -48.22115 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b96cf175-de89-36a1-bda0-3cdfc11cc5d1 | -10.4571 | -48.23328 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e2dd3305-7b0f-30f0-8fa6-75dd460d8491 | -10.45567 | -48.22223 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 46b660e2-d59c-31a7-895e-da5f7d8849ac | -10.45423 | -48.21114 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 63fb9de7-f4b6-3765-9359-33a78c9f5663 | -10.45272 | -48.19947 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d601bf0-2d95-3103-b918-94d2d29a7fb6 | -10.4092 | -48.19014 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c0079be8-a639-35ac-92f6-321095192c7d | -11.44356 | -47.82197 | 2024-10-01 00:48:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3fb357f0-4f33-3088-ad06-b0d22c7749e1 | -13.45259 | -48.62309 | 2024-10-01 00:48:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 43532838-e4f4-3673-96bd-68654e379c55 | -13.2251 | -48.5808 | 2024-10-01 00:48:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 88cda790-ae09-3c03-8fe2-e693e4d06311 | -13.11705 | -48.22104 | 2024-10-01 00:48:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 16fc54d1-8577-3c73-8fd1-65b5ede04606 | -12.97467 | -48.54872 | 2024-10-01 00:48:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 685b0922-be7b-39f1-ad4f-e41336247c05 | -12.97307 | -48.53584 | 2024-10-01 00:48:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 57843ce0-bd8a-30eb-a327-1a0e8dd22f48 | -12.52655 | -47.98285 | 2024-10-01 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9a38271-b235-37f5-86ba-06d00058248d | -14.74206 | -48.77289 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7635b4dd-427f-37f2-9b68-0b3872f4112b | -14.74043 | -48.7593 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ca968b62-b86b-3347-b154-2618f293ce65 | -14.73894 | -48.74686 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 065c6214-b609-399f-9e56-92456cea157b | -14.72977 | -48.76147 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 140de309-31be-36fa-a0af-768466ad7e56 | -14.72821 | -48.74842 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1271ce25-27c6-3162-86d1-d3afbb2565a1 | -14.72639 | -48.76751 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d8ed3f5c-e3ea-3780-a228-1c88088564f6 | -14.72475 | -48.75439 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 24d9e4de-cad1-3d75-918a-60e3cfdb19de | -14.71744 | -48.74955 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 766fad2e-536c-32ac-8b7c-3c3e7c3b1a02 | -13.72284 | -49.42899 | 2024-10-01 00:48:00 | TERRA_M-M | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d9e2a2f3-71e8-3fcf-89d8-b374b0f47052 | -26.215599 | -52.354801 | 2024-10-01 00:48:01 | METOP-B | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99964480-11a8-35ac-be55-0c9a7613269d | -25.0194 | -54.054798 | 2024-10-01 00:48:26 | METOP-B | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d5694f8-b1fc-3d80-99cc-eaf044749d28 | -24.848801 | -54.005402 | 2024-10-01 00:48:29 | METOP-B | SÃO PEDRO DO IGUAÇU | PARANÁ | Brasil | 4125753 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 121de837-29fd-3056-abc8-7e08ff0b716c | -23.0665 | -45.371399 | 2024-10-01 00:48:29 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f07cc397-12cd-3cd4-952c-2323dd4a55f2 | -23.0686 | -45.380501 | 2024-10-01 00:48:29 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84aaba60-9b9b-34ba-814e-328cf2bef768 | -23.070801 | -45.389599 | 2024-10-01 00:48:29 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af326621-9948-38d2-98e9-22232c3322c3 | -23.058901 | -45.383202 | 2024-10-01 00:48:29 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f338edf-52b8-33ef-9ebf-2931acc5d732 | -23.0611 | -45.3923 | 2024-10-01 00:48:29 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3aa4ab1-2105-3bb1-bd97-0749eb5585a9 | -22.4804 | -43.533901 | 2024-10-01 00:48:31 | METOP-B | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c942699-65c0-36dc-a062-d73f4208c553 | -23.4149 | -47.504398 | 2024-10-01 00:48:31 | METOP-B | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f673f10a-aa84-3e53-8bcc-97122eb0abd3 | -22.499701 | -43.818001 | 2024-10-01 00:48:32 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6342e0fe-3cde-3d84-8d33-90c4359cb81e | -22.5243 | -44.2929 | 2024-10-01 00:48:33 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c893bb57-b8c7-3ae7-92ad-700fd3a63436 | -23.0986 | -46.5672 | 2024-10-01 00:48:33 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12603256-360a-31f9-a15e-e66f1705514a | -23.1005 | -46.575401 | 2024-10-01 00:48:33 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e03f3029-0fc4-3f1d-b5a6-f3b45a3ceb6e | -23.1024 | -46.5835 | 2024-10-01 00:48:33 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9282413-01f1-3706-ad93-1d6b5b623c2b | -23.0907 | -46.577999 | 2024-10-01 00:48:33 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b24ed0b-935a-3257-9228-f4bb26566b74 | -21.608999 | -41.1894 | 2024-10-01 00:48:35 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c74077b-b596-3b5f-8506-ddc6f75a396c | -22.7169 | -46.661098 | 2024-10-01 00:48:39 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a67e631f-ad14-37ae-b15f-bf07e1a817e1 | -22.7187 | -46.669201 | 2024-10-01 00:48:39 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8186dafd-3fa6-3b00-8e0b-4f46582b8dae | -22.376499 | -45.781799 | 2024-10-01 00:48:41 | METOP-B | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93c0c5b9-9434-31f2-ad5b-fe76c00502b9 | -22.373199 | -49.287201 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8d271a1-0c41-3665-93a4-c433658ce164 | -22.374701 | -49.294601 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8ff52f1-0c87-3cbc-b38e-613da9ad2ef7 | -22.376301 | -49.301998 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ae3d192-dc84-3683-8c0b-a3283842335c | -22.377899 | -49.309399 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4701b406-8bc0-3120-9d53-05b70c1ce660 | -22.3634 | -49.2896 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49a1bf8c-dfe1-34b2-96b0-269bd63a932d | -22.364901 | -49.297001 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 078fe059-4e7a-3e1b-b84e-75b2d3d54bbc | -22.366501 | -49.304401 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84594670-a9e4-3a24-8429-ae35a853c116 | -22.368099 | -49.311798 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ab10117-de3d-3faa-8939-adc95646e154 | -22.369699 | -49.319199 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ffb1debb-fdb3-3884-a057-a78039891e36 | -22.355101 | -49.2994 | 2024-10-01 00:48:54 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f9dff37-43be-3fc5-9825-fc8586642e80 | -22.356701 | -49.306801 | 2024-10-01 00:48:54 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d7ba2dd-ca93-35e7-84a8-783c638e0e88 | -22.358299 | -49.314201 | 2024-10-01 00:48:54 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37055b72-d548-3737-bf45-d061ba441ffb | -22.3599 | -49.321602 | 2024-10-01 00:48:54 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa112405-679a-3272-a2da-7354b11686f5 | -21.8484 | -47.155399 | 2024-10-01 00:48:55 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 152fd470-e995-309b-bde7-23d328473aee | -21.850201 | -47.163399 | 2024-10-01 00:48:55 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3bca6951-3d9d-3e9a-b376-87d09897ab35 | -22.118 | -48.539501 | 2024-10-01 00:48:56 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9923fbe6-af20-3539-ade3-dcaa9bd0228a | -22.119699 | -48.547001 | 2024-10-01 00:48:56 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ad2ebc92-2555-35ce-972a-9b6309b98a0b | -22.1213 | -48.554401 | 2024-10-01 00:48:56 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1b247b5c-b574-32cf-a946-837d4f7d457b | -21.5965 | -47.773499 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3dc13a4-b2f0-39b1-b0d9-727ea09c4ea9 | -21.598301 | -47.7812 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4b409eea-62b3-3a64-8b3f-5180bceefb6b | -21.6 | -47.788799 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fee11400-b0a9-3189-9473-75ef45f03b7d | -21.5781 | -47.737701 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4bb8b7-efcd-3f19-8d82-4443b0e9efc7 | -21.5867 | -47.776001 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06179ee3-1a55-35d9-afe7-c9d3542fde07 | -21.588499 | -47.783699 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1e978668-4d27-385e-9123-b7bba70cfa73 | -21.5902 | -47.791302 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4cc1fd47-bc2c-382a-8051-231dff5ef11f | -21.5919 | -47.799 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 18a13094-4900-37b0-96d9-48e7a3b671a8 | -21.5937 | -47.806599 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6f9223ff-445f-3ca6-a054-fcd5a1ae0cf3 | -21.5954 | -47.814301 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea1e3aea-9ec1-3b8e-bf89-ac69166d7889 | -21.597099 | -47.821899 | 2024-10-01 00:49:01 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 394dadd4-97ac-3ecd-a48e-d42c0f7884ce | -21.577 | -47.778599 | 2024-10-01 00:49:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6316ea-e1d3-35fc-8e16-9217c5e82035 | -21.5788 | -47.786301 | 2024-10-01 00:49:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0a13bdb-229a-3091-bebe-9edd48c166d1 | -21.5805 | -47.7939 | 2024-10-01 00:49:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bdc7109c-8bb0-33c5-8715-172367a041f6 | -21.582199 | -47.801601 | 2024-10-01 00:49:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
