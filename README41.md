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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c511d9d-5e24-3bea-bdbc-6a8dc9443f6e | -2.95557 | -49.19916 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab5f61a-cf19-3097-be6a-6762c0d27450 | -2.95542 | -49.2127 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 610cf8ec-7a33-319b-94ff-6e97379e27aa | -2.94999 | -49.20666 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8e1a877-33cb-3844-81ea-c31e4dd1ced9 | -2.94931 | -49.19815 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ca48fed-06ed-36c7-b737-0d115520e300 | -2.94916 | -49.21165 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30415d3a-fded-3b20-8226-bdca8365544d | -2.77854 | -49.24557 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9189a11-f44d-32c3-8037-fc7b7fc4d312 | -2.7731 | -49.23949 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 327ce8e6-bf8e-3f63-a3af-f5f7d6a55359 | -2.77224 | -49.24461 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08d3b04c-14dc-34c2-a8ba-84466006710f | -2.60558 | -49.7956 | 2024-10-10 03:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdb0df78-1b85-3ba2-9f71-20cb399f2d56 | -2.60498 | -49.79689 | 2024-10-10 03:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26d9037e-bc48-31c7-9d19-e2f810081f01 | -2.59906 | -49.79453 | 2024-10-10 03:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5bc74277-6671-3c26-8e9f-cc213077150a | -2.59845 | -49.79582 | 2024-10-10 03:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 012f78c0-0535-3fa6-ae27-1ce9e1c76dd5 | -2.59813 | -49.80005 | 2024-10-10 03:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0056c536-fe0b-34f2-9d1d-005771039d33 | 0.44885 | -50.21298 | 2024-10-10 03:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e5a8220-1738-3c87-afe3-7b33b896651f | -3.23095 | -50.84993 | 2024-10-10 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 38cd05bf-3cd6-30c3-afd2-d8cef6a038af | -3.03188 | -51.10098 | 2024-10-10 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f47439e-d3e3-3595-a188-ae9df47be7df | -6.54589 | -42.5162 | 2024-10-10 03:55:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3be500b1-84d4-3b3e-a485-67944013cd87 | -7.79024 | -35.5512 | 2024-10-10 03:55:00 | NOAA-21 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20337df5-6f88-3291-adf4-de2c1affb3fc | -6.88394 | -35.49171 | 2024-10-10 03:55:00 | NOAA-21 | GUARABIRA | PARAÍBA | Brasil | 2506301 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28e796ff-b1f0-399e-b89d-75426c0e04f5 | -8.07234 | -34.97814 | 2024-10-10 03:55:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba5f9f14-175b-3455-b8b6-0833f00f24ae | -9.87861 | -35.98202 | 2024-10-10 03:55:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 516b9842-7b29-3137-8fdd-a55db80709be | -9.8119 | -36.53696 | 2024-10-10 03:55:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf514216-f012-3219-8452-ca4d3b7ca08e | -10.592 | -37.11055 | 2024-10-10 03:55:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 757785e7-1fe8-3952-ac07-5a6224000906 | -12.78183 | -38.49627 | 2024-10-10 03:55:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61ceec8c-7c9c-3e97-b1ef-5f635c3cb073 | -12.78128 | -38.4999 | 2024-10-10 03:55:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9cd1ac49-2ec1-3484-afc9-207cce30a669 | -7.94569 | -38.3501 | 2024-10-10 03:55:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ffb87865-3c32-3bf5-9e64-c4ec02368b35 | -6.4589 | -38.84608 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 322b8d66-2961-37a1-a51a-7cfc8d1930dc | -6.45559 | -38.84556 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db30cbff-2e8a-3468-9e1d-0a70c30d7cb4 | -6.45505 | -38.84902 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7341f5e2-82cb-344d-95c8-ee1d80d81150 | -6.45229 | -38.84504 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c807f21-da9d-3091-bcdd-9234c4f645d9 | -6.45174 | -38.8485 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b41523fd-91a8-35dc-ae34-1759050d543a | -6.44898 | -38.84451 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b3b434f-c023-30da-b98e-94f7c506bb33 | -6.44071 | -38.83255 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54755209-c26a-3531-be75-2bc3448b8589 | -6.43741 | -38.83203 | 2024-10-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddc60ead-5c17-3718-85d3-b1aae544433b | -12.13504 | -39.40767 | 2024-10-10 03:55:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18a880d1-b4dc-3970-9017-f59717f1a37c | -12.61541 | -39.62209 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d0e06c9-f1df-3268-b883-40d339e3c336 | -6.18948 | -39.49191 | 2024-10-10 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| afbb357f-c723-340b-b6bf-c174722bd572 | -6.18671 | -39.48783 | 2024-10-10 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb0594a0-b4b5-372f-a88f-44a6bc6f1d6b | -5.5943 | -39.44807 | 2024-10-10 03:55:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 627e0c86-66aa-383a-86b7-f4f9b95c0d39 | -7.67021 | -39.62345 | 2024-10-10 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffbd5114-e752-3ee3-9760-a1cf8446d813 | -7.06482 | -39.72549 | 2024-10-10 03:55:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2b055d0-a31c-37e7-910c-6189cb468d33 | -6.91732 | -40.47042 | 2024-10-10 03:55:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 933c2679-e1a3-3a68-a559-90ab3f8440b0 | -6.9076 | -39.55945 | 2024-10-10 03:55:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cdb51975-5ae9-3e49-8725-acc4aa9da807 | -6.54816 | -39.61457 | 2024-10-10 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5afedb2-1afe-3625-92b6-5f2a6bb790be | -8.6237 | -40.38934 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a8be98fa-b273-387f-a52e-526dbf5b11f2 | -8.61169 | -40.70776 | 2024-10-10 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 594b7f31-10c1-3b5c-a7a3-9c743ef8578e | -8.57563 | -40.43011 | 2024-10-10 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39c106af-9ba5-3791-8301-a32f604618c0 | -8.56945 | -40.66255 | 2024-10-10 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ebe66239-f90e-372a-9c41-ec854d946ac5 | -8.56605 | -40.662 | 2024-10-10 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6872176e-45af-36b7-966c-6823e3642086 | -9.446 | -40.5454 | 2024-10-10 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f860642-9899-3960-88cb-8829f1be7406 | -12.42265 | -40.58134 | 2024-10-10 03:55:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09859064-c1de-324a-87d2-1c80f29a5193 | -12.29865 | -40.90629 | 2024-10-10 03:55:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ba983df-125b-36d4-8320-053f03f4c2f2 | -6.37207 | -40.47347 | 2024-10-10 03:55:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62128f59-6a45-3146-bf40-b9fda282b67c | -6.30286 | -41.76843 | 2024-10-10 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 859b037b-a970-3c84-ad07-9ace2562097c | -6.29919 | -41.7679 | 2024-10-10 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0e64d151-803b-3599-a155-b64af9e27a75 | -5.60217 | -41.0099 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55188387-d500-36a1-83f4-c446268701ad | -5.60211 | -41.01092 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 306c7687-5e35-3d7a-9528-2c57cae35244 | -5.39617 | -41.25108 | 2024-10-10 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d42aa175-6657-370e-9656-cfbd97b52744 | -5.39325 | -41.24635 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 291fe865-ebe8-3059-8e1d-fd04cbf4f9fa | -5.19735 | -41.2943 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8085af9-8b31-341a-9a7e-966f072e3e11 | -5.196 | -41.30273 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f4dac02f-af36-3446-89f8-1782776e6ab8 | -5.19532 | -41.30695 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a353ae73-7a98-3db6-bcd5-c5f1ce41e015 | -5.19442 | -41.28951 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c870b717-a4b6-3f9a-ba3e-f807ec425c7d | -5.1917 | -41.30639 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69e35e8e-1253-3070-956f-88dbb8edc673 | -5.18876 | -41.30161 | 2024-10-10 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 993b796d-bd32-378f-9bd2-9919f48b4b85 | -7.36102 | -42.186 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a9884afd-7a16-39ae-9da7-6378dee4684a | -7.36031 | -42.1904 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a8851ca1-907f-3d76-9944-695a6c3c3599 | -7.99268 | -40.97176 | 2024-10-10 03:55:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 965fc7ca-5859-3f08-b9ac-ebf6afb1a938 | -7.09969 | -41.44481 | 2024-10-10 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 416794a5-2e33-3f6d-abf5-a486bd76ff4e | -7.09902 | -41.44887 | 2024-10-10 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7842ee1a-4759-36e3-896a-01b6aad0eeef | -6.48185 | -41.95924 | 2024-10-10 03:55:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 99142401-343f-342b-a4dc-ed54f5ee0162 | -6.48113 | -41.96364 | 2024-10-10 03:55:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8641934-22e0-375c-b881-71bdb144a267 | -6.42359 | -42.01364 | 2024-10-10 03:55:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4d939982-4282-309a-ba2e-0ec01151f4cf | -8.4094 | -41.95576 | 2024-10-10 03:55:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6a818aca-091b-38b9-89ec-efc6a302ceac | -8.1849 | -41.36038 | 2024-10-10 03:55:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4292fab6-f4e1-3968-9dd7-a1c07466ea55 | -8.1814 | -41.35981 | 2024-10-10 03:55:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7059a8a6-2b24-345f-85f6-18cb35930860 | -8.14893 | -42.32286 | 2024-10-10 03:55:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7cddaac8-5188-341a-b753-59de40231294 | -8.14231 | -42.31727 | 2024-10-10 03:55:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb62cb1f-0d8b-352c-b025-038b852cae85 | -8.14158 | -42.32167 | 2024-10-10 03:55:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 251aa1ef-1ef6-3078-816f-367375dcd47f | -8.07003 | -41.10187 | 2024-10-10 03:55:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90508c27-2d8d-32fc-9c82-22f73a206693 | -8.06656 | -41.10131 | 2024-10-10 03:55:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70356b08-fe9f-3211-aeff-bbdea36da702 | -10.79835 | -42.44873 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 365bb771-e926-37b8-a8e5-6782cb51f2c0 | -10.21506 | -42.45866 | 2024-10-10 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f796fae3-36ca-391c-8155-d7a6d7a3554a | -11.9563 | -41.77345 | 2024-10-10 03:55:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 814ac3e4-d517-3106-9dd1-95802a50224a | -11.82698 | -41.66217 | 2024-10-10 03:55:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7575be1a-1191-36ae-8b50-c5256935cfd4 | -11.7116 | -42.61139 | 2024-10-10 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 17681db7-cfe3-37ce-ace0-b5acb223281b | -11.08797 | -41.53716 | 2024-10-10 03:55:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80ff7754-ef3b-3b2e-aafc-b1009cdfda1f | -11.04347 | -42.0205 | 2024-10-10 03:55:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9a4b619f-f0a4-393f-8b67-13605911572d | -11.02861 | -42.89584 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc83957e-23b3-3ea8-b7c0-614377d47937 | -11.02788 | -42.9002 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8aaa6489-c50e-3b21-83e5-31d12f29c2c1 | -11.02495 | -42.89522 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0250304e-d5b5-3967-8c61-28e1af32ca5b | -11.01693 | -42.87592 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 578d39c2-81db-3524-a64c-325055d6b5a1 | -10.84637 | -42.86249 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81cbecc2-caeb-33c7-a0cf-e0e14c07eb74 | -10.84637 | -42.86179 | 2024-10-10 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8646d281-baf3-3042-a7a3-93e6971c74e1 | -4.95218 | -42.98738 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1832bff5-ec63-39d3-884b-ff8375d403cf | -4.95162 | -42.99088 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fece3ebc-4ce8-3f74-b4a2-e1d96d07d6f0 | -4.94982 | -42.98729 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 60e32925-e2bb-3fb8-a47e-69f5ea176957 | -4.94923 | -42.99078 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 48bd06e8-bf63-33d7-8810-611533027155 | -4.94873 | -42.98327 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f397613c-cb9c-3794-994f-8cde334f77ee | -4.94864 | -42.99428 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
