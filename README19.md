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
| bed37b0f-a5cf-3de5-a35d-c03d4efd361c | -4.01722 | -38.25149 | 2024-11-14 03:46:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5511ac69-f368-3c47-8364-fc4c003071e7 | -2.47113 | -45.85305 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3eecaad2-02d5-33e0-9e76-6c8a1046b4fe | -4.22603 | -46.87969 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c839c29-21ad-3cd2-b3cb-9ac52b6cf09e | -3.77003 | -41.60587 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 48064db8-68d0-39ea-af90-548e0b1671c8 | -4.04215 | -45.72149 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c4b493b-e7af-3ddc-bef8-857860409efc | -5.22317 | -37.73154 | 2024-11-14 03:46:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c10bb947-df12-3c9a-a20e-0e63a5df0590 | -3.14767 | -45.48238 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41a6f43e-098e-337e-98c9-cbca21ca8798 | -3.25967 | -46.27912 | 2024-11-14 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da370a28-5539-348c-b307-d763c55cab9f | -2.64028 | -46.17512 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e73aeb54-89d8-3a4e-a7c1-af42a0040c54 | -4.16076 | -46.25141 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffd941d7-28c8-3798-a876-4440dd5a627e | -3.86841 | -43.94078 | 2024-11-14 03:46:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31d18945-1069-3a74-980d-a6e809815c17 | -5.94453 | -42.43573 | 2024-11-14 03:46:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47edede6-47e6-3955-9dd2-a2f8c7569265 | -2.26975 | -45.35283 | 2024-11-14 03:46:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4174ad52-9b66-3b63-9606-32d49dcd5e01 | -2.36572 | -46.50344 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f5f8584-53f8-3f62-93de-174bba80f003 | -2.3789 | -46.49679 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54512a08-bbc6-3cc7-9bb7-fe9e3e987ffe | -4.01781 | -38.24776 | 2024-11-14 03:46:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 601ce658-d609-377e-8463-452a3b3a349a | -7.22465 | -39.96409 | 2024-11-14 03:46:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 317f2cdd-78fc-3018-9175-d9ea61e597f7 | -3.32645 | -39.70059 | 2024-11-14 03:46:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e816a577-b4c2-3139-8c3e-e7e41bd8a125 | -5.08501 | -45.98299 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33bf08a-0b62-3a10-a562-02f931047628 | -4.22493 | -46.87867 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b31e29bf-f1a1-3e09-88ed-56c65e957033 | -5.35144 | -43.54721 | 2024-11-14 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47de89a9-dada-325f-ad08-0dcae7f0c8e7 | -5.34315 | -46.02787 | 2024-11-14 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65db6991-64b9-37d4-b19c-0907c975cc33 | -4.45522 | -44.93407 | 2024-11-14 03:46:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 488814e5-bcb8-3875-ad5f-664f018ae8c7 | -7.78979 | -37.59975 | 2024-11-14 03:46:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5890840a-b3cd-3f19-90f5-9cc5559c253a | -5.55713 | -45.36913 | 2024-11-14 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9a8d8885-9362-32ad-a59b-b0ea5a1623f8 | -3.01577 | -40.21113 | 2024-11-14 03:46:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d91b664c-685e-3b0c-8de6-4ff05dc01e68 | -4.92704 | -45.7141 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9109ab50-3bc3-33d6-895e-6037610a89d7 | -5.74865 | -35.27637 | 2024-11-14 03:46:00 | NOAA-20 | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 159f6f14-d197-368b-9bf2-bc3ca5a35800 | -6.92365 | -39.9354 | 2024-11-14 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da10813b-e852-3df9-98f5-7846fd87b9e5 | -6.05613 | -44.047 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32ea21c8-a654-331a-951d-e47697efdbee | -7.22823 | -39.96468 | 2024-11-14 03:46:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b26f1803-acb9-3f44-b571-7dda0ffa9acf | -5.34441 | -46.02595 | 2024-11-14 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d866db7-d19f-3807-b703-fbc86cccab85 | -1.93065 | -46.28508 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2293220-7b3c-3536-aeb1-a02d5d665741 | -2.65037 | -46.17918 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede7861f-c608-39c0-9194-85ece749cad8 | -3.1421 | -45.28222 | 2024-11-14 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10c4dd3a-a5cc-382e-9cf6-2d9b387b9d01 | -2.63826 | -46.18701 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe547a9-f318-30d3-b1ae-573f0308bba5 | -9.15654 | -50.54513 | 2024-11-14 03:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4888241-cc4d-3c1d-8820-4fb867287f6f | -4.44443 | -46.57781 | 2024-11-14 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42456457-ba0d-36b2-aa25-083be80f0150 | -5.56231 | -45.37016 | 2024-11-14 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 936b82b2-3039-3b0d-b3b0-d41e4cd48e0b | -2.63761 | -46.18503 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c28eff9-830b-3235-9d79-3c30be1166bc | -3.1101 | -45.88306 | 2024-11-14 03:46:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0a446e8-926f-31d0-8bad-ee5896c1d6c8 | -1.4444 | -47.78834 | 2024-11-14 03:46:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d03d095-73c1-3054-bb1c-9c11551d2909 | -2.47413 | -45.85358 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a55f8f9-ad2d-3e27-b680-4f198cd7270e | -2.63954 | -46.17313 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e504d0ce-8a75-383e-9c5e-61eb7f56bf96 | -2.64601 | -46.17614 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e28208f-5fd1-3ad5-bc77-830a9f1e6504 | -5.06927 | -45.51192 | 2024-11-14 03:46:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5a5bcdd-ce62-3517-9cd7-7986c6fa2c8a | -7.78703 | -37.59575 | 2024-11-14 03:46:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1233132b-758f-3774-98da-a64a266298f1 | -4.16009 | -46.25529 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1838a3b2-8f65-333b-9881-74674fa0b27c | -4.22674 | -46.87547 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ce73b04-8755-3698-8ec7-8ed10925ceae | -4.55264 | -48.01446 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 991d45e5-9806-3b3a-81c2-573b6b018e88 | -3.28487 | -45.37083 | 2024-11-14 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d8f4c304-f817-34d6-be55-d6eb0b155906 | -2.98754 | -45.87117 | 2024-11-14 03:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596aeb2a-8124-348f-b763-b7acf52e83ec | -6.52765 | -35.26658 | 2024-11-14 03:46:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34b74a55-97cb-3c01-85e0-6526716b236a | -5.19194 | -44.36442 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acf56ae9-b95a-3c32-84b1-79584d6d0f4b | -4.93853 | -40.54959 | 2024-11-14 03:46:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bccb3680-4f0b-3414-8da4-29ff53b2ad7a | -2.40695 | -45.34369 | 2024-11-14 03:46:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7b13b5c-e398-3630-9504-67fb8587e714 | -2.19716 | -46.36374 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc198e09-9e88-3145-8a7c-b2a2a844770e | -5.83986 | -42.33398 | 2024-11-14 03:46:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 28f7b7e0-362e-3148-8ff5-d80886e88e66 | -5.19287 | -44.35888 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd9fc97a-bdfc-3924-a3b9-187a249fc2d5 | -2.36999 | -46.50339 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74a08b4f-520b-3767-85fd-88157406c402 | -7.02881 | -35.24588 | 2024-11-14 03:46:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e68d7b9f-3e97-3002-b952-52ae5e9daa98 | -2.90044 | -46.86087 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce99a9df-9262-39ad-b315-34c82f0c0dd4 | -3.78017 | -41.5958 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d0a64b6-2166-35a2-ad09-87c04e570c91 | -3.77127 | -41.59828 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10e15069-0a83-3a6d-98e1-c3bc483e9ae3 | -4.56104 | -48.01966 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ac827ee-66f3-3980-a75f-329c7e7a7fdc | -3.28544 | -45.36742 | 2024-11-14 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aca33045-8787-3ec6-ab63-fbf26a689d31 | -4.15579 | -46.24654 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e6cdcca-6dda-3ed4-83cb-c6204a780af4 | -6.26874 | -44.55036 | 2024-11-14 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31a03fca-e912-3cc3-a77d-27c68c8ab237 | -4.15013 | -46.24571 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2cd46e16-5471-3b27-8e2f-5319877240e3 | -11.86961 | -38.35513 | 2024-11-14 03:46:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a845839b-6e1e-3ab5-81c3-84a738e63077 | -2.42055 | -46.27528 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dbf09054-48fb-3449-8494-40bd54575abd | -4.77638 | -45.73738 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad3f2a9-98d0-345d-95ef-9e78e78f1c1b | -4.59048 | -46.62882 | 2024-11-14 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c175e434-4693-3b0a-b29b-29f44b026943 | -4.36609 | -39.42834 | 2024-11-14 03:46:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a74d009d-f7aa-3320-84fe-9253ab819315 | -3.77189 | -41.5945 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1c82a02-17c1-321e-8a64-e7029a4f65cd | -5.32101 | -35.62667 | 2024-11-14 03:46:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c1c4bbb-3c43-38fd-8a19-a4fd2f504b69 | -2.64529 | -46.17414 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93c155ba-62dc-3f9f-869b-cd227b005594 | -2.89224 | -46.87301 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71416e4b-661e-3997-a31e-a85d1a511a9e | -3.88792 | -46.09583 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3b808bcc-2649-38a0-85de-37a8efc8fe74 | -4.5589 | -48.0156 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4686f1d6-a9b3-3f12-8aaf-c1f994e912fd | -4.05425 | -47.23684 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ca134e5-73c0-3fba-a849-4470b5ee4c0c | -12.34509 | -39.10281 | 2024-11-14 03:46:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a49e5c6a-f746-3163-afa4-c0ea4a6c8ab2 | -4.80145 | -39.60869 | 2024-11-14 03:46:00 | NOAA-20 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ce79a41-0f5c-3609-97e7-9662837e282a | -4.04824 | -47.23578 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2e9638a-29ab-32d4-9458-f321d57eb0b1 | -5.32156 | -35.62317 | 2024-11-14 03:46:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a10f7627-b886-39fe-8f3f-7b3299c045c1 | -2.67021 | -46.99398 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bfe1b7e0-d5fa-3b9b-ae72-345571f144c3 | -1.63244 | -46.10683 | 2024-11-14 03:46:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bac05b2-b9d3-35b0-bc4c-c9d9745b7056 | -4.51794 | -37.90081 | 2024-11-14 03:46:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1e0708a-8e0c-3cbb-be06-7478636a3411 | -7.13526 | -40.17214 | 2024-11-14 03:46:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e386d062-01ba-3126-846c-292ffe6d932b | -4.15441 | -46.25457 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d3e2a7f4-28fc-3fc8-aa02-9c5561139f68 | -2.37958 | -46.49258 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15cb680f-21cf-34c5-9bde-916c74e34ad2 | -4.36701 | -48.09356 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8d31284-91eb-3eea-a91d-fb35fca62aa5 | -4.14875 | -46.25371 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a493c7c9-3ee1-30a8-a7bd-ae63f33ca7fd | -2.66631 | -46.8326 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 971b6275-beec-3547-84c8-70d6695495e1 | -2.27582 | -45.35018 | 2024-11-14 03:46:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 2d60b743-29d3-31ab-8c20-7c82c49697c1 | -3.17032 | -45.44675 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d177e79-3ea2-366c-8ea6-d0f169795bc0 | -4.86381 | -44.48137 | 2024-11-14 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03d53adf-987a-385a-8ca7-3ace46486c57 | -2.64764 | -45.8036 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b984547-bbfc-36a9-a355-8e10c03929ab | -2.98194 | -45.87022 | 2024-11-14 03:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 975297cf-6d99-3e6e-9f72-2906ee1385fa | -5.1938 | -44.35328 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README20.md)
