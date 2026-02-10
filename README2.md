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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f4c20f-bda9-3a4f-adbf-84707c3ec160 | -17.61491 | -40.35724 | 2026-02-10 03:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c9f551c8-d879-3287-8c47-b91fdfc8e7a8 | -16.2958 | -40.77468 | 2026-02-10 03:38:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d958b18b-10ab-3e5a-9ccd-14fc62a52516 | -12.67898 | -38.79899 | 2026-02-10 03:38:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec485f58-1c71-3717-93b3-4de592ae55ef | -17.61078 | -40.3564 | 2026-02-10 03:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d77e648f-1cf8-319c-8539-79ad74d146d4 | -16.89726 | -39.77488 | 2026-02-10 03:38:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 049910ef-54da-32a8-9c94-a37b40bc967f | -12.15202 | -38.06639 | 2026-02-10 03:38:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25db518d-904e-3b4f-b4eb-7d3261803ac7 | -16.89824 | -39.14992 | 2026-02-10 03:38:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6e3c0307-8661-3b2a-8734-247c3ccfd9cb | -17.61226 | -40.34862 | 2026-02-10 03:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 29aa7928-6e50-31eb-9d6b-0afd3374be3a | -16.29145 | -40.77383 | 2026-02-10 03:38:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| ff3c6bd3-b257-389e-b27f-0e054ff91626 | -12.67833 | -38.80254 | 2026-02-10 03:38:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61f1cf54-6401-3693-aa48-b41369357445 | -12.68305 | -38.79971 | 2026-02-10 03:38:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4e3dac2-7536-3ad7-81e7-c51f8b721207 | -17.61152 | -40.35248 | 2026-02-10 03:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 05849659-2cb6-308f-b997-8a0d2e2e813a | 1.121 | -60.5034 | 2026-02-10 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 43180621-fee4-3259-b5d8-07e428c7661a | -19.3865 | -40.20398 | 2026-02-10 03:40:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5926ae9a-3cd2-328d-9b10-413a64db129b | 1.121 | -60.5034 | 2026-02-10 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3a2bdaf1-8743-3f29-a1be-766925d0314b | -7.86229 | -35.00876 | 2026-02-10 03:55:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4cf14af0-2337-3ddf-b585-52c4bef16aad | -5.45058 | -38.39234 | 2026-02-10 03:55:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ea02f39-83bd-31ae-a031-df42dff6c53e | -2.98685 | -40.38369 | 2026-02-10 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa22dd14-fffe-3fd0-81a9-3f84c32382ab | -7.71262 | -37.44142 | 2026-02-10 03:55:00 | NOAA-20 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e4efdd91-c54f-3469-bee2-0f7a7cbcce58 | -2.51501 | -47.8179 | 2026-02-10 03:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a31f967-85d8-30ad-829d-37c7787bca6c | -7.78063 | -37.56909 | 2026-02-10 03:55:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 593eb23b-e62e-3cd2-a375-398598bdc367 | -15.88336 | -43.68565 | 2026-02-10 03:57:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a382598-1ca7-3a42-b51a-831dd6fc2b32 | -12.08197 | -38.09316 | 2026-02-10 03:57:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c11ae2f-6033-386b-b70a-da82899b27a7 | -12.23813 | -41.14783 | 2026-02-10 03:57:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bff896fb-1f38-30b6-8143-382847ff162f | -11.52091 | -41.56748 | 2026-02-10 03:57:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73db87f2-d7f9-3804-9880-608d5a6b4d1a | -12.47205 | -43.73437 | 2026-02-10 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 338d869f-e913-3b36-b021-202bf0cdb262 | -12.03164 | -45.34124 | 2026-02-10 03:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e815302-9cc4-300d-a561-734d44aad036 | -16.29071 | -40.7737 | 2026-02-10 03:57:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 33833b30-2215-3fab-aae4-4b005a48b459 | -12.68074 | -38.80018 | 2026-02-10 03:57:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8f086eb3-6a78-326f-be1a-ae86e84eec3c | -10.11795 | -42.16746 | 2026-02-10 03:57:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89de8616-1559-32dd-bcd1-04e548cb39f8 | -11.01779 | -45.07174 | 2026-02-10 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05fcc5e-a378-3a33-9275-da2d09f90add | -12.08253 | -38.08945 | 2026-02-10 03:57:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 210cdf7b-9b32-34ba-9ad8-2704ad7ed890 | -11.23894 | -49.45407 | 2026-02-10 03:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6e83323-a144-3177-aa31-c1015e978e38 | -10.18106 | -47.77633 | 2026-02-10 03:57:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf028ed9-8a65-3269-8c7d-13d3200520b9 | -15.51613 | -39.51288 | 2026-02-10 03:57:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8442a176-4380-348d-88bf-45d6087f3118 | -12.1522 | -38.06604 | 2026-02-10 03:57:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad0a4cf2-c785-3c30-8b18-563237205c71 | -15.54387 | -41.36525 | 2026-02-10 03:57:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8e5910f3-0c2f-363a-a6fc-e0b6911c8ea4 | -15.06613 | -38.99744 | 2026-02-10 03:57:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2bc55c23-c1b8-3541-9189-df8b4c9e3eb4 | -15.66431 | -39.16315 | 2026-02-10 03:57:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d2ef334-4e9b-3e4d-918a-543fa4ddec28 | -16.29402 | -40.77426 | 2026-02-10 03:57:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7588c630-37f9-3b2c-b580-1baa33a769dd | -10.25785 | -36.41677 | 2026-02-10 03:57:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 359fbe27-63a2-38b2-a879-1373c653d147 | -11.15801 | -49.25435 | 2026-02-10 03:57:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 965d8fb7-10bc-36e2-8b40-31f62c41b156 | -10.11768 | -42.16657 | 2026-02-10 03:57:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5f61fcc-2b48-3dae-91e6-481246fdd4e0 | -10.18051 | -47.77932 | 2026-02-10 03:57:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 660d4069-5403-31b8-82cf-d4dd18a2316e | -11.04432 | -41.98465 | 2026-02-10 03:57:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9c1a0c59-424a-30b0-8d8b-2f035d2a6fc1 | -12.47041 | -43.73586 | 2026-02-10 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f581d996-eeb5-336f-8cb1-d97575a56e1e | -11.01714 | -45.07547 | 2026-02-10 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cdb029f-e8a7-3e8e-88cd-20023e039b6e | -16.89749 | -39.77504 | 2026-02-10 03:57:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81118024-225f-3a6e-9176-b8f3d0a4fdc9 | -11.15871 | -49.25074 | 2026-02-10 03:57:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ed1f4fc-9212-35bc-9745-a5dca3a2c473 | -11.8569 | -38.46459 | 2026-02-10 03:57:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c68f4a83-9dbb-3934-b41d-5169e1bde807 | -14.93179 | -39.56088 | 2026-02-10 03:57:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 33165a78-e8c0-377a-bba8-7a2034b0ebad | -12.31462 | -37.91795 | 2026-02-10 03:57:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57adfedc-2d1f-3c04-9c1c-6266d6f55e48 | -16.89817 | -39.14642 | 2026-02-10 03:57:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a69961b-ea34-38b4-9a53-4be90fbb7f0f | -12.03232 | -45.33743 | 2026-02-10 03:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0081f73d-f293-3f44-9fb4-25463170a88f | -16.8976 | -39.15024 | 2026-02-10 03:57:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c284497a-5328-39a6-85c8-f4b1741d5fcb | -13.42605 | -38.91726 | 2026-02-10 03:57:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c817ba0d-4424-3a86-b26c-9bbc9415f88b | -15.06951 | -38.99799 | 2026-02-10 03:57:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87e21d6d-716f-36f6-93ca-62e5b57c920e | -16.89784 | -41.10075 | 2026-02-10 03:57:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e379b78d-df30-3a6b-9cbd-8da712c5e57e | -13.4294 | -38.9178 | 2026-02-10 03:57:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1f22445c-6fd2-318b-94ae-296317eb4055 | -12.86957 | -38.34274 | 2026-02-10 03:57:00 | NOAA-20 | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 014a2ecc-42d1-3b96-9b33-90e731fcb011 | -11.62108 | -37.61983 | 2026-02-10 03:57:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 772ca63a-ea36-394e-891e-35c2f2557efd | -12.46833 | -43.7337 | 2026-02-10 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf958fab-6038-34fa-bb46-1646e8ba96f5 | -17.61289 | -40.34894 | 2026-02-10 03:59:00 | NOAA-20 | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42929104-c07a-3533-a6d4-b60f12139f9f | -17.61232 | -40.3526 | 2026-02-10 03:59:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bfec0acd-d54b-3ed6-a6af-2c6d5c6e4875 | -17.61176 | -40.35624 | 2026-02-10 03:59:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7169c4f5-0da6-32e9-8d26-2df708fa0a95 | -17.61565 | -40.35316 | 2026-02-10 03:59:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 357944d4-edc7-3f6d-8e9e-ddc4da3d5620 | -17.609 | -40.35204 | 2026-02-10 03:59:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ca1f4615-61a0-3ecf-8d18-8d6f1c0827c0 | -17.61509 | -40.35679 | 2026-02-10 03:59:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f01be18b-d1f9-3b00-9276-955869c29e3b | 1.121 | -60.5034 | 2026-02-10 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ebaec165-5ea8-34d6-bc49-c055194f36e4 | -22.52137 | -50.91004 | 2026-02-10 04:01:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6b6035f6-8ee7-3a9d-b2ed-366588835310 | -22.52745 | -50.90542 | 2026-02-10 04:01:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d725247d-3809-32d1-a6fd-8a9971dbf197 | -27.09819 | -50.5287 | 2026-02-10 04:01:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dacd7ce4-6f1c-30a6-92e8-ad1f4f54c0be | -26.62841 | -53.69241 | 2026-02-10 04:01:00 | NOAA-20 | PARAÍSO | SANTA CATARINA | Brasil | 4212239 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12e34906-0e6b-3634-830a-aed234c59b95 | 1.121 | -60.5034 | 2026-02-10 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f7f5d3c0-0da8-34e2-9c1c-5db3e9ec789e | 1.121 | -60.5034 | 2026-02-10 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9a071fcb-61a3-3e7b-ba43-e250accf10e7 | 1.121 | -60.5034 | 2026-02-10 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2b049fb2-b1b7-365a-8ca7-dc0485843a8f | 1.121 | -60.5034 | 2026-02-10 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9b9a5216-b7a1-38fe-ad64-2812e24ce86b | 4.41389 | -60.72917 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d931ab5-312a-3687-bde8-a6f4089917e4 | 0.96273 | -60.52089 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 18bfa18b-353c-32ff-ad35-608ded081dc0 | 4.42015 | -60.72718 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12426e3d-8ef6-34f2-b43a-742127743ea6 | 1.11306 | -60.5099 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0a4d2e32-fed6-37b0-a2df-9cebbff59768 | 4.41315 | -60.72402 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd4c8610-fdfc-3265-b5d2-8a3c0caba29b | 4.41239 | -60.71872 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a9fc4f1-3383-31bd-a5e8-bb8a34ca0981 | 1.11828 | -60.51421 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0d0847ef-0424-3736-b002-7f5db5c68e59 | 1.11151 | -60.51058 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 68e78661-e2c0-328b-aa06-294ee4fa755d | 0.95067 | -60.52278 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd0a99e4-cc2e-3dea-ac6c-dfa4335a9072 | 1.11756 | -60.50969 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0b14172f-fe6c-3446-a7d7-e82ebb8944fa | 0.95669 | -60.52182 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fe22496-22d2-30b0-8e44-747f2e7f9fb4 | 1.11978 | -60.51351 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a08e32b5-ee26-35ff-b3cb-7d12fed34bb3 | 0.77809 | -60.66887 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31ade25e-8b7e-3b80-9fd1-9599d8e1a6dc | 4.39515 | -60.68938 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49b46792-000b-3cf4-b802-6fd5356ae310 | 0.78417 | -60.66795 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f61f85b-4fb3-3f41-bc9f-5c4a56765473 | 2.48306 | -60.55575 | 2026-02-10 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a8d11c2-3317-3a4c-aefd-849f017e6151 | 1.11389 | -59.19912 | 2026-02-10 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ab6deda-eba4-367a-8f6d-f354854e645b | 0.79097 | -60.67162 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 667a5c52-0c37-3a3b-bc10-93abe753eebc | 0.79025 | -60.66704 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c34729ee-9b75-39ce-9422-ff42a3a5bf7d | 0.95739 | -60.52634 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ed161ef4-e62c-3009-8b82-b006d8a7226c | 1.11374 | -60.51442 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae4721dd-4032-3ff4-ba80-8522926d7c97 | 4.38893 | -60.69162 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a919899e-2fb9-3e19-9343-2c7db871a4ac | 1.1191 | -60.50897 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.2 |


[Clique aqui para ver as próximas entradas](README3.md)
