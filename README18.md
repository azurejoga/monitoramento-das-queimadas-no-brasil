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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1ac462d-9fbc-3f0f-95d1-61295c71adc1 | -2.69536 | -46.60086 | 2024-12-18 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b3b4e8e-fe2f-3859-bc81-4c0943eb5e33 | -4.00519 | -43.75457 | 2024-12-18 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b30c1af-7b8f-36ea-9ddd-c492f9679743 | -3.64876 | -53.46238 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd7e2b9a-d57e-3976-9f79-851daf5041f4 | -4.11992 | -43.56559 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f2557b2-2caa-3795-8de3-2cc1bd0d1cd4 | -4.02982 | -46.91056 | 2024-12-18 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea55d45-61c2-3916-b4c6-f07aba0c1ff3 | -3.34621 | -53.84093 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33019388-89c3-3a55-ad07-f256b2ba88b7 | -1.42587 | -55.45187 | 2024-12-18 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7fa837-6e25-3763-8ff4-3627329c5cca | -4.93472 | -45.0941 | 2024-12-18 04:48:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05d9729c-6ee7-352e-81c6-3fa03eec4015 | -5.94518 | -43.77052 | 2024-12-18 04:48:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d1abb77-1d56-33a2-a591-b9ff1fea65a1 | -2.09001 | -45.28749 | 2024-12-18 04:48:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c109efb-fdf6-3997-929b-b4bb5312ec9c | -1.70429 | -45.78531 | 2024-12-18 04:48:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3faf2f14-36d0-378e-a02f-947d8b8e2afd | -4.04295 | -46.68113 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed889fde-90c2-36f8-a67e-f73fc3128b1d | -2.57081 | -47.94723 | 2024-12-18 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bdbad94-cdfe-3625-a575-24a655d3b3c1 | -3.06455 | -40.0509 | 2024-12-18 04:48:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82f3b623-1b81-359f-8975-5b3a44c01bc0 | -4.26296 | -48.56839 | 2024-12-18 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad43903b-4901-363c-98e6-97e53ff6bdc3 | -1.62471 | -45.8523 | 2024-12-18 04:48:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c5d1ae4-2a05-357a-9637-51a67ffd72c4 | -6.08375 | -43.97277 | 2024-12-18 04:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 618e64cd-3cb9-32aa-a479-ea2fd0af4d32 | -3.58124 | -54.55315 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77f1e502-4382-371e-bc26-4f9f7c42d57a | -4.1505 | -43.56986 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 186b9589-3826-3a23-93b2-a71316c94cb5 | -2.36421 | -48.49257 | 2024-12-18 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90b4bc13-82bc-3105-9c2c-a50a21750414 | -3.14692 | -44.4573 | 2024-12-18 04:48:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35c85dd-89b0-315c-8d53-285d6e967520 | -4.57207 | -45.88352 | 2024-12-18 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b6d2e86-cb39-336a-8627-c13994df0c36 | -4.03349 | -46.80194 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f10e7e0e-3181-3624-8d8c-6914ae2868a0 | -6.00019 | -41.57675 | 2024-12-18 04:48:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67b26416-9af8-3d18-bcfd-60b2ecd10ace | -1.40455 | -46.67955 | 2024-12-18 04:48:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53063f27-5f59-322b-bbc8-d7cf190cd2a5 | -4.5392 | -43.29797 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33ee8bf9-8c14-350b-848c-6b2117395e43 | -4.01402 | -46.93365 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65163cdd-f3ee-3ea6-9366-f4d76fdd9a68 | -4.5407 | -43.29296 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c44c4b60-c98a-3be3-863c-74c7e5c011fb | -4.97721 | -43.71725 | 2024-12-18 04:48:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05568e78-d7d5-3023-ac46-ab33e3aa4e61 | -3.61525 | -52.50151 | 2024-12-18 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25667c73-6126-327f-a41e-b55775f476cb | -4.52538 | -45.86748 | 2024-12-18 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fabb150a-c81f-395d-9fa8-51be41ed20a9 | -3.24004 | -46.87306 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f98b0740-8080-3ebb-9ae9-e7f958d390fe | -3.35023 | -53.83774 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3477b70c-8a26-33d7-a454-56f430352798 | -1.44717 | -45.74067 | 2024-12-18 04:48:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cef70ec-3f41-34ef-8772-14b787dc1baf | -2.79875 | -46.71397 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f5f7ed-8371-3c71-a155-c3ca717db304 | -3.49987 | -53.953 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 72f95a3c-24f1-3719-bce3-140231011e61 | -3.2435 | -46.87717 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d5a73383-8fa9-36c1-94c6-4411569ce241 | -1.70008 | -45.78466 | 2024-12-18 04:48:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449874a8-602c-3f19-a077-62408f865a1a | -1.04325 | -46.60211 | 2024-12-18 04:48:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3b9f5ae-87a9-3464-99a9-73b807c69fbc | -4.11948 | -43.56863 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a18d68e1-65e3-3b07-b6c2-8c1bfe0a6b4f | -6.0578 | -44.04717 | 2024-12-18 04:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ddb03e-73ea-3e52-bd5b-a1141204bc1d | -4.00561 | -43.75173 | 2024-12-18 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fef036b5-0000-35a1-8718-ad4fef3cfba0 | -5.71514 | -43.46966 | 2024-12-18 04:48:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50be4cdd-a9a2-392f-8dc4-e266d965611e | -3.63619 | -54.75459 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43519e0c-df9a-3773-93d5-26d833ea7869 | -1.42514 | -55.45651 | 2024-12-18 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f52a7d1-e9a0-35df-b116-2cb0054186ef | -3.57761 | -54.55361 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d38f7d-701b-3036-8178-5cd85d2c15d9 | -4.06211 | -46.91568 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcab8186-e204-3790-a3d1-86269ac38969 | -1.53995 | -53.73177 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f14b75a3-3013-3066-973a-0a9b3d3aaca8 | -1.79438 | -47.06059 | 2024-12-18 04:48:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59dfafd2-dac0-3356-8ef5-58b80f81cceb | -4.5398 | -43.29935 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1336cd14-e262-3a85-8742-e57e3d248039 | -4.5449 | -43.29548 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afb42256-e5f0-3654-90fc-60d59be48542 | -5.99427 | -41.57546 | 2024-12-18 04:48:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f421e8f-9006-37e7-bb87-9ce2f94016d4 | -2.05384 | -46.65668 | 2024-12-18 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a418c58f-c6e4-351a-a9f3-ae1086ff1b8b | -3.0653 | -40.04588 | 2024-12-18 04:48:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3fb29e60-a8c8-3ee2-a4a7-d9382f8f8e70 | -2.35236 | -48.48785 | 2024-12-18 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc03b061-548e-372e-82d3-da356d708e15 | -4.57643 | -45.88424 | 2024-12-18 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c280417b-b184-33a2-98e4-b0241431f2da | -2.13826 | -46.46337 | 2024-12-18 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74365d49-b2c1-357c-b369-334b593e8a75 | -3.77864 | -43.00354 | 2024-12-18 04:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d6fa233-8049-3685-a9ab-caf896d41350 | -2.24411 | -53.56133 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ad47c76-4fae-3eed-9e1e-f70300b4c671 | -4.54443 | -43.29867 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ff282c8-20c5-33b4-ba43-c1a352dd18bc | -2.01635 | -54.35288 | 2024-12-18 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7735b082-f3cf-3e15-bb8d-c86995e29fa8 | -4.04705 | -46.68171 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb51de53-f7ed-39ad-84dd-2f3f4a55b346 | -3.24295 | -46.8807 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 90d48cc3-9697-3d53-96fd-00ad49eb5228 | -4.54593 | -43.29367 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8964dffd-fadc-3302-8912-fe78918b567c | -4.15005 | -43.57286 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12963252-9bb6-3475-a2fb-25787a6e749c | -2.40928 | -47.71128 | 2024-12-18 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6939cd96-8d5b-36c2-8d53-cd15b9a65f37 | -5.62975 | -44.83791 | 2024-12-18 04:48:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6686cfa-2ebd-357d-821a-c1255c5f23cb | -2.07977 | -54.22798 | 2024-12-18 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c0c9a20-afcb-3072-a447-57aea38fbca3 | -3.50272 | -53.95731 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7289eed2-3e45-3f12-b306-5f47b6b47350 | -5.68301 | -46.50415 | 2024-12-18 04:48:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 699b300d-418f-34ce-b494-6dcbc818e443 | -4.54548 | -43.29688 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b332634-0a8c-33d9-96d3-6d2605d9dc66 | -3.53084 | -54.73468 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de1c4e7-ee81-3052-9d1b-ba5691ff7ded | -4.97209 | -43.7166 | 2024-12-18 04:48:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6276abf2-dfe6-308d-a55e-0640000c6838 | -4.15094 | -43.56688 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4725f90e-5116-32bf-ade6-8032daade96d | -1.42894 | -55.4571 | 2024-12-18 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1abf1338-0055-3a0e-b3e1-db16006991f2 | -3.86505 | -47.03159 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c5d33c5-aa4e-3c0b-b5d3-10f35fa78cd9 | -6.08332 | -43.97583 | 2024-12-18 04:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbdfff8e-40cb-38b0-ba12-43c454fc5b00 | -0.88732 | -50.64778 | 2024-12-18 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e652918b-455e-3379-8bfe-9ee201506e6d | -4.53968 | -43.29479 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dae09e94-f640-3550-add2-2a35b6686ef6 | -3.24404 | -46.87367 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ceb70be-7644-33d4-b5fc-ee1d076a0aa9 | -2.92365 | -45.24686 | 2024-12-18 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce66d23a-6c21-3782-9d70-4996a6aa859e | -3.0246 | -45.23364 | 2024-12-18 04:48:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c6a03a7-0cc9-3014-a291-f63b8c1c170b | -4.54015 | -43.29158 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c66f075c-a6fb-3cff-a554-991495a00ddd | -4.97165 | -43.71964 | 2024-12-18 04:48:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bff8b7f8-fdf6-342a-94c6-c1ab50afd8c6 | -0.75335 | -47.7558 | 2024-12-18 04:48:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 091a5d89-ae22-30eb-a8bd-1badbeedf089 | -4.39333 | -44.10409 | 2024-12-18 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a055c3b8-0717-3b84-a1f4-0ea1f6066269 | -4.54025 | -43.29618 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c0dcd29-839d-300e-b2ca-b89722555ec5 | -3.86263 | -54.20261 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adce584e-b176-3d87-80aa-3d48e10ceb5a | -1.3786 | -45.96277 | 2024-12-18 04:48:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4765d94-a96a-321b-b627-132c48bfbc34 | -5.68434 | -46.50125 | 2024-12-18 04:48:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c4ef917-7cf2-3970-b14c-791b162248e1 | -5.1104 | -43.31572 | 2024-12-18 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4cf8b136-94fa-3295-ae5d-6057fdbd6943 | -2.0833 | -54.22853 | 2024-12-18 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f904fcd7-ce26-3134-a0bd-d0437232e456 | -2.34908 | -47.4222 | 2024-12-18 04:48:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46df5fe3-d331-39f8-9c8d-3d55709dc9ca | -3.24443 | -42.41766 | 2024-12-18 04:48:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ab094e6-8ff3-3ff0-96e0-724d5fed645f | -2.22651 | -53.53939 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fae2019-e055-3c4d-becc-7c68eb62b349 | -2.79734 | -47.42718 | 2024-12-18 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9d1ab2f-0c74-3457-a6cc-e0ac6e7574a3 | -4.12037 | -43.56255 | 2024-12-18 04:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb531ea8-bb68-3cd9-98ab-abe1da2c1d5c | -3.23895 | -46.88012 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 571441b0-6cee-3c60-8d11-281303105962 | -5.21423 | -44.90522 | 2024-12-18 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e32348a2-2ce3-3d87-a36e-3c6faad70cbe | -3.77671 | -47.97981 | 2024-12-18 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
