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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2091242-489b-3b1f-b37c-0ba9ccff2ced | -20.12636 | -43.5288 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| def72542-62ef-32f4-85dc-3451d0e865a6 | -20.12531 | -43.53341 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| d5d949ab-4720-39fa-a21b-5b28eb1c0520 | -20.12287 | -43.51682 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b75a6abe-5788-35b2-9951-19b796053785 | -20.12165 | -43.52222 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f5c5e57-8b3f-33a1-8241-f2a62ee38e89 | -20.12057 | -43.52696 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66048fa8-caa0-3bd5-8fef-f23fff6a1200 | -20.11581 | -43.52061 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 94fb302b-1c2a-3266-8a58-261601d1f172 | -20.11484 | -43.52486 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c7216e3-cd7c-35f6-899c-af8d74b5db6b | -20.10998 | -43.51897 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 9ffbfdb3-d072-3e3d-acdd-7a4ef0f66303 | -20.10906 | -43.52302 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| f666965c-c0cd-3f79-ba7c-b77d2f674507 | -20.10816 | -43.52696 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 1242d5d5-a9e4-324c-a247-40014ca49ed5 | -20.10729 | -43.53075 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| e02d59bb-7921-3bb9-8806-1a352d61fac9 | -20.10586 | -44.91211 | 2024-10-04 03:19:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c833571a-f2d2-3137-8a12-4ae79b2b76d0 | -20.10459 | -44.91744 | 2024-10-04 03:19:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebf8c95-c956-3b44-8f6b-b0e9b882d601 | -20.06905 | -43.6046 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2c27384-15db-3df0-9b1b-650e71f75779 | -20.06592 | -43.60271 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 40c9ace6-f62f-3640-b7d8-153c83c722ae | -20.06481 | -43.60755 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d3a35238-2d89-36cf-b08c-1e49f3f8e8ed | -20.06234 | -43.60672 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cf292d3b-3f6c-340c-9250-a96dfe38fa01 | -20.00588 | -44.49784 | 2024-10-04 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a2ff3ec4-948d-340a-bfa0-ac481d0df3e0 | -19.99311 | -43.55439 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5868c88-ad3a-3606-957c-7fc1c4b93d32 | -19.9872 | -43.55299 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa4f3abb-9f44-316d-8bfe-ab33f894be1d | -19.98321 | -43.54319 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00b832c4-1a02-391b-90c8-0fbee5e44a30 | -19.98226 | -43.54735 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2a351937-cf0c-3d37-9c91-c116ed11a22c | -19.97998 | -43.54373 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c8b20563-f00d-310c-8170-aa7a0447e785 | -19.97725 | -43.54205 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 96817432-55cc-3788-9496-31a7fa34ad48 | -19.97618 | -43.54668 | 2024-10-04 03:19:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f188c203-48eb-3f14-80ed-67ee7cea5e32 | -19.89658 | -44.52796 | 2024-10-04 03:19:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7217263f-2b88-360e-a7f1-02749c28a6af | -19.8905 | -44.5257 | 2024-10-04 03:19:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| cfc61f62-e8d5-3f97-a0a4-5459d311f8bc | -19.87522 | -44.59108 | 2024-10-04 03:19:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66d53783-8fee-3331-9783-75c36ece586e | -19.87386 | -44.59688 | 2024-10-04 03:19:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 538fe607-d0d1-3f4e-9049-eebc866735d3 | -19.83743 | -44.23068 | 2024-10-04 03:19:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82b3cd6-d2db-3e9a-bd3b-72ff7e9b1275 | -19.83113 | -44.22979 | 2024-10-04 03:19:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50e0a4a9-8f82-3738-9707-72634a737749 | -19.82993 | -44.23494 | 2024-10-04 03:19:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d8e1a45-a32b-3849-bffb-d6fab0558a00 | -19.80471 | -43.6461 | 2024-10-04 03:19:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c99de65f-1083-3b04-91ab-94c2cced8451 | -19.79881 | -43.64442 | 2024-10-04 03:19:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb29d86f-a080-3f7b-8658-af6e55ad369d | -19.75618 | -43.69365 | 2024-10-04 03:19:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a814c12-3080-398c-9068-f23b42ff08ce | -20.23835 | -45.95081 | 2024-10-04 03:19:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818e6823-1dfd-323f-a984-f1334dbdef5a | -20.23686 | -45.95701 | 2024-10-04 03:19:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b09f7a79-a2d1-3ae1-ac15-877abb45e5ca | -19.7622 | -43.6949 | 2024-10-04 03:19:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 433bcbd9-3f72-3792-909b-19772ea34549 | -20.50041 | -41.81536 | 2024-10-04 03:19:00 | NOAA-20 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 255c6e87-b4cd-30c1-9b03-ee9d541bccbd | -20.4997 | -41.81862 | 2024-10-04 03:19:00 | NOAA-20 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0fe49cf5-ab0d-3237-a4e7-bec38b982e89 | -20.31579 | -41.97166 | 2024-10-04 03:19:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5980d2fb-28e1-3213-a0bf-4aa9b6689736 | -20.05189 | -41.26409 | 2024-10-04 03:19:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9771d84f-94f2-33b3-b15a-e3cf9e3cf316 | -20.0512 | -41.26732 | 2024-10-04 03:19:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c39e967b-a6c6-32f4-bb09-e5cb2cc07170 | -20.04677 | -41.26283 | 2024-10-04 03:19:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de2fa2e0-b613-3887-8a27-6028f78bcd00 | -3.2534 | -50.3689 | 2024-10-04 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| db993c3d-4a1b-37e2-a2c7-a2f5ab3bbb29 | -3.3665 | -42.3112 | 2024-10-04 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 021f4d1b-6116-39ae-937d-1405be7233bf | -3.3667 | -42.2875 | 2024-10-04 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 246.9 |
| a089dd27-6555-3a38-9b35-299aeeedbc5f | -3.3854 | -42.2866 | 2024-10-04 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c073a9c7-1ca3-3304-9a66-e86c8be6d128 | -3.2899 | -50.4725 | 2024-10-04 03:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7911a0eb-3422-3d9b-9f70-6f678e049009 | -3.2899 | -50.4516 | 2024-10-04 03:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| ad47217b-7ec1-3bd5-86b5-7978ede36475 | -3.3083 | -50.4719 | 2024-10-04 03:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 38f60087-be4e-39e0-a2a9-038b4d6bf674 | -3.3084 | -50.451 | 2024-10-04 03:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| dfc1c0a0-00ed-35d3-b337-e41c6292a106 | -4.0763 | -48.4902 | 2024-10-04 03:25:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 23663870-fa1e-3ec0-ad0f-1b08367f080b | -4.0765 | -48.4687 | 2024-10-04 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 62cc0068-a292-31c5-8358-9794241217c6 | -4.0949 | -48.4894 | 2024-10-04 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 218.4 |
| 43eaf11f-4068-39a9-ae97-aa4d6f57a4c7 | -4.095 | -48.4679 | 2024-10-04 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 0cde4136-f2b1-3108-a1c0-0e60a7d28626 | -4.5375 | -43.304 | 2024-10-04 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8d59dbf9-ce26-3ecd-92c3-09f3a98e688c | -4.6684 | -45.8961 | 2024-10-04 03:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c913c918-f938-322a-8026-8c23fd9ce19b | -4.6686 | -45.8738 | 2024-10-04 03:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 41274bc3-19f5-3be3-9801-a7ceb12ae80f | -4.687 | -45.8951 | 2024-10-04 03:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 160.3 |
| c5fe2c0d-f30e-3b42-a8c1-d40c44b93ec4 | -4.6872 | -45.8727 | 2024-10-04 03:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 273.1 |
| 94569a0d-5991-363d-9319-e04217805c84 | -5.8216 | -44.1196 | 2024-10-04 03:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8c28ba1d-9969-32ff-a75f-73e3eb4875c5 | -7.8539 | -45.3611 | 2024-10-04 03:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c6fbbc78-382e-382f-9def-2806df6461a6 | -7.8351 | -50.5416 | 2024-10-04 03:25:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0bf3be99-ed89-3f95-9d66-b13333e7397c | -9.0853 | -50.9036 | 2024-10-04 03:25:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b65b0749-c15e-3348-95b8-066e0c643ecc | -9.1041 | -50.902 | 2024-10-04 03:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a26fbd5d-bce1-3d0c-9180-be09ec9feb56 | -9.3115 | -50.8203 | 2024-10-04 03:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 419179b8-b337-39ec-9baa-5753fca06e38 | -9.3118 | -50.7991 | 2024-10-04 03:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 6999cd23-b460-3de5-9594-24d4991997c3 | -9.3303 | -50.8186 | 2024-10-04 03:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 63fc040f-6439-3967-98a3-a033dfc402a5 | -9.3306 | -50.7974 | 2024-10-04 03:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 077217bd-a4be-3677-a2f5-5d926cb75c0d | -9.845 | -68.9623 | 2024-10-04 03:26:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b0970140-cacc-3a69-b6f9-748755dda135 | -11.0723 | -46.5319 | 2024-10-04 03:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 12b2f540-482d-341d-8535-a219d84b5564 | -11.0914 | -46.5294 | 2024-10-04 03:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1bd56b74-b49a-3634-a848-f72a658dd018 | -11.0918 | -46.5069 | 2024-10-04 03:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fae7ef2e-2ad2-31a8-886b-ad152bc967a0 | -11.8242 | -56.6009 | 2024-10-04 03:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| aa4adaa8-7050-31a2-9a57-0b51eafe8ece | -11.8244 | -56.5808 | 2024-10-04 03:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 95b7d10f-1db4-31c3-a322-0358b73c26f3 | -12.5901 | -53.115 | 2024-10-04 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 1aec6827-2a7d-3769-b9c2-80ee1c782a62 | -12.5898 | -53.1359 | 2024-10-04 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 8609076a-9584-336a-b4c8-950670bbd234 | -13.1587 | -48.6764 | 2024-10-04 03:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3fbec3ce-c260-327a-8871-5c404b09fa54 | -13.1591 | -48.6543 | 2024-10-04 03:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 85d010e7-f029-3a9d-a7fc-44cc0ea9d627 | -13.0598 | -51.1195 | 2024-10-04 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2f1a5f2a-8cd9-3858-a4cf-4e92f501a135 | -13.0786 | -51.1385 | 2024-10-04 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0160dd3f-e5ae-3bd7-b842-eb8fd5e45bbc | -13.079 | -51.1171 | 2024-10-04 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ecac2cf9-4e98-3e90-8774-62cedcfa935c | -13.1166 | -51.1551 | 2024-10-04 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ad143c2f-d616-3567-8d1a-5a1322c3da22 | -16.4151 | -57.3823 | 2024-10-04 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 1f3badf6-2d8e-3e74-99d0-dc6897da2918 | -16.5935 | -57.1988 | 2024-10-04 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 26f54e37-67ec-3e4e-880b-498c265c2686 | -16.5938 | -57.1783 | 2024-10-04 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 375e9df3-b55b-3130-8511-d148aae9b8bc | -16.613 | -57.1965 | 2024-10-04 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| aea9682f-8c12-3d2f-8d93-64811acf3eae | -16.6133 | -57.176 | 2024-10-04 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| 5c946a73-2195-39e5-bcf4-93f4c5b44c50 | -16.6868 | -57.4741 | 2024-10-04 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 1c8c83ea-9ed1-3544-901d-74288c7858e3 | -16.6871 | -57.4536 | 2024-10-04 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| bb6ecd77-b22b-3898-a61a-45dd2158eb84 | -16.7455 | -57.4674 | 2024-10-04 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 0a0cdfa6-126c-3631-ab32-6f861a29275f | -16.7647 | -57.4856 | 2024-10-04 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 951fad38-fcc1-3ceb-bbea-36dd356cf735 | -16.765 | -57.4652 | 2024-10-04 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 6feadc3b-5837-3fc1-92cb-5e3b5a711656 | -16.7843 | -57.4834 | 2024-10-04 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 22f0c0d8-0cb4-3da5-80e2-3f52d8f66f97 | -16.8055 | -57.3788 | 2024-10-04 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| f16b856c-edd6-3671-9fdf-cc1339626c54 | -16.843 | -57.4767 | 2024-10-04 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| d6e1a4e2-8a11-3634-8ac1-e0057a9421cf | -16.9087 | -55.843 | 2024-10-04 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 556dbad2-b9cb-3218-9002-b2372295614c | -16.9283 | -55.8405 | 2024-10-04 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| e5901690-4e07-3b8a-ba5f-965f254e69ad | -16.9287 | -55.8197 | 2024-10-04 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |


[Clique aqui para ver as próximas entradas](README55.md)
