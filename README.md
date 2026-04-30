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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b39ed1-c62c-386d-b17a-278c710e134f | -11.0006 | -45.0847 | 2026-04-30 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 90c7f1b4-beee-3f9d-8c07-98293fe20345 | -10.9815 | -45.0874 | 2026-04-30 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9fa8bcc8-03c2-325e-96f6-12bc21e7d571 | -18.0836 | -53.0813 | 2026-04-30 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 139f7273-aa29-30da-bbed-a366e0a74069 | -18.1035 | -53.0781 | 2026-04-30 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| a292dba4-b1e8-3900-a095-0b563aea4bf0 | -11.0006 | -45.0847 | 2026-04-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 281f357d-cc62-3cc9-bbc9-d1377ba24712 | -18.1035 | -53.0781 | 2026-04-30 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 75abe38a-85bf-3af6-860f-fabbaff5a9af | -11.0006 | -45.0847 | 2026-04-30 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a1ba8986-eae4-3388-88c4-a905ab54b6b0 | -18.0836 | -53.0813 | 2026-04-30 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 0bfabbec-1223-36b0-8f6a-c2c86f1496ce | -11.0006 | -45.0847 | 2026-04-30 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7286444a-399c-3b4c-bb35-1f307c67b37d | -18.0836 | -53.0813 | 2026-04-30 00:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f70dac5c-3c7e-3125-b325-de39ad0855d7 | -11.0006 | -45.0847 | 2026-04-30 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3bae348e-6e4e-3a02-9e2b-18e633894dc4 | -12.0586 | -57.416801 | 2026-04-30 00:49:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98b17bfe-66dc-3e4b-b520-5b35c63f8d52 | -12.057 | -57.409801 | 2026-04-30 00:49:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cca4192a-3b0e-3090-b1c7-4c4bec771d1f | -17.2478 | -47.0825 | 2026-04-30 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4b1b2548-a894-3167-b90b-057078a81772 | -11.0006 | -45.0847 | 2026-04-30 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1d9b5399-2b8f-3b36-9eb9-590dd59b814f | -11.0006 | -45.0847 | 2026-04-30 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 94fd66d7-344d-3509-9cb1-3feb4aa938c1 | -11.0006 | -45.0847 | 2026-04-30 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| a6e789b3-70e8-3687-a5d6-174d296e2f9d | -11.0006 | -45.0847 | 2026-04-30 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 27a05771-1338-3ed4-bb11-a793b7379ff1 | -12.0507 | -57.412998 | 2026-04-30 01:20:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21e88630-3221-3544-89bd-ac1daf2a7470 | -12.062 | -57.417801 | 2026-04-30 01:20:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62dd51bb-0340-3bf4-8e37-a12c4bd6c207 | -18.0497 | -52.9991 | 2026-04-30 01:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7cca8c21-f702-380e-82c3-e634ad16dc18 | -12.0522 | -57.419998 | 2026-04-30 01:20:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c74e19ef-6aff-3eb0-8582-f320b541b712 | -12.0605 | -57.410801 | 2026-04-30 01:20:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f4a3b7-c1b6-3ae8-b9a6-73699873b3e4 | -18.0595 | -52.996601 | 2026-04-30 01:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2170f328-760e-3541-a5ad-57bc49a3fde2 | -18.030199 | -53.0042 | 2026-04-30 01:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d8aca7d-62a0-39bf-a6d0-4d140b2630c9 | -11.0006 | -45.0847 | 2026-04-30 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 394b2995-d7bb-3e6d-8300-3482d98f4cd5 | -11.0006 | -45.0847 | 2026-04-30 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 873f5163-3e86-3f7e-944a-5bea2f3e4cbd | -11.0006 | -45.0847 | 2026-04-30 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 69891bb2-6b01-3173-9bc9-bddff03c8c9d | -11.0006 | -45.0847 | 2026-04-30 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 078be271-82b6-3089-87a1-feccc69a773b | -11.0006 | -45.0847 | 2026-04-30 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e7c169ad-e156-3918-b551-a7891a975546 | -18.1035 | -53.0781 | 2026-04-30 02:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 47bee1bd-67ec-3829-bc61-0075dbc01ddf | -11.0006 | -45.0847 | 2026-04-30 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b80a8c5c-8207-34c1-bddd-335ef0569c56 | -11.0006 | -45.0847 | 2026-04-30 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 426a7b53-b6ce-3dd0-b5af-a1c838420319 | -10.9815 | -45.0874 | 2026-04-30 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| c5dd8ec4-dbac-382d-999e-d1964581a6f6 | -11.0006 | -45.0847 | 2026-04-30 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f158bd14-ea1e-3bce-bf58-db6228c72ed6 | -11.0006 | -45.0847 | 2026-04-30 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4b822471-d1c9-33aa-ba75-cb4f17a4f539 | -8.58105 | -39.42402 | 2026-04-30 03:23:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7e4e6687-7d37-3091-b956-53b325e29fd1 | -8.5816 | -39.42094 | 2026-04-30 03:23:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c6af2fc5-eba3-3fd3-996d-52e4806c9a46 | -13.20804 | -44.48933 | 2026-04-30 03:25:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fdb2e39-4ee2-3ff4-9ad8-0dd60717a6a9 | -10.99079 | -45.07594 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 17d07c30-d7a6-3def-8d03-a99fa6c8f438 | -10.99119 | -45.07892 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| da28e21d-0142-357e-994b-9c5e6c0e8d36 | -10.59434 | -44.32943 | 2026-04-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9d60d475-6860-3a76-8390-c6fcb6459047 | -10.98945 | -45.08236 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 088f1109-d87c-354c-af58-e174399210f0 | -10.59307 | -44.33559 | 2026-04-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 871ff56b-41d0-3c8b-ac44-1882f1e84ac5 | -10.96424 | -45.09903 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2131f4fc-876a-3d8b-bf38-99cb6cbcbfa1 | -10.99683 | -45.08669 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 1af7d16b-97f7-33ea-a595-ccf0e706e073 | -10.99777 | -45.07711 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2f30fe57-0974-3003-b455-6fb51d93587b | -10.98809 | -45.08885 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 893c1e8f-5b5f-339e-aa13-f764227e5b00 | -11.95089 | -43.38232 | 2026-04-30 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 790ee700-c597-3c10-89ab-4b8ef73ab176 | -10.98853 | -45.09203 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| db26da80-9269-3507-bc06-6448e35f1145 | -10.99642 | -45.08355 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b9ae5176-4bf7-35cc-ba3c-559ecb0c9036 | -11.41824 | -39.52793 | 2026-04-30 03:25:00 | NOAA-21 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a752a43-e9bc-355f-a719-a464455f2a6e | -10.5906 | -44.33328 | 2026-04-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| cdf6c61b-7c7d-3db9-af5d-80f831bb39f6 | -11.12823 | -45.13933 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 73018abc-52a2-3b6e-b1a5-ffbdfc70da66 | -11.13521 | -45.14053 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3b87f0d0-afc7-304c-9a2b-a7af9564a1dc | -10.58638 | -44.33426 | 2026-04-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 99f749bd-d6ea-350f-9c0e-889228d1ccd9 | -10.97127 | -45.10005 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b8c4c2-2ad9-3b2c-a8aa-7b7e52fea2a0 | -12.00554 | -38.66668 | 2026-04-30 03:25:00 | NOAA-21 | OURIÇANGAS | BAHIA | Brasil | 2923308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ef7b934-6f4d-32b0-be4d-c6a87b4d98c4 | -10.96618 | -45.09533 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cdb0d82-0e18-31f1-82fd-2b7175fc8b72 | -11.95195 | -43.37699 | 2026-04-30 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e6a9a0c-0bfb-3585-9f67-1fe8972c4153 | -11.41546 | -39.53003 | 2026-04-30 03:25:00 | NOAA-21 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08627e11-15e3-3146-8eea-c7132a0fce2b | -10.98987 | -45.08541 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0d530dec-28f0-30af-be55-01a328ca66a3 | -10.96477 | -45.10224 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cba717b-e94e-3265-969a-f4113fa15a5a | -10.58766 | -44.32805 | 2026-04-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f4c2dc2-4aa6-336d-9081-85561b17b1aa | -10.99815 | -45.08017 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 2383f8d5-0f66-30d1-9dd5-0b3ebb6ae31d | -10.99505 | -45.09013 | 2026-04-30 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e11d6cea-9f57-3835-8435-f086e0b8051c | -17.38801 | -42.62414 | 2026-04-30 03:28:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78fcfea1-62bf-31a6-b269-d0fb2d1f652d | -17.38727 | -42.6277 | 2026-04-30 03:28:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17dbc679-9c6f-3816-bdca-9313975aded5 | -17.38653 | -42.63126 | 2026-04-30 03:28:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6b9e585-ed51-3984-bd01-af12340b9f13 | -18.89359 | -39.92802 | 2026-04-30 03:28:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d0438e79-55e4-342a-8385-64d4e96b3972 | -11.0006 | -45.0847 | 2026-04-30 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b81832e9-70ab-3014-9a3b-e560a1e49b2a | -11.0006 | -45.0847 | 2026-04-30 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 239f3fe8-8ef8-3d49-9f0c-afdf8a2fc61a | -10.9815 | -45.0874 | 2026-04-30 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3a52b873-521d-3d6e-9285-ed98c82575d7 | -11.0006 | -45.0847 | 2026-04-30 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f03d6306-5a74-3760-858a-1cb85672a54d | -11.0006 | -45.0847 | 2026-04-30 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 345c6752-5112-3c2a-9bf3-eb895852d13e | -18.0456 | -53.0013 | 2026-04-30 04:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| da0e9f61-67a6-32f6-ab05-eccb6f91a99a | -11.0006 | -45.0847 | 2026-04-30 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 67a4eee1-dc76-31a2-bec4-5da740c3f346 | -18.0853 | -52.995 | 2026-04-30 04:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 659b849b-a989-303f-9023-34a8368c2ae3 | -18.0654 | -52.9982 | 2026-04-30 04:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f8c70d95-d44c-3b94-b9f7-1abc1917eb18 | -14.40447 | -44.5847 | 2026-04-30 04:17:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23c883e2-a16d-3055-a64b-6613106305bd | -8.69444 | -47.52457 | 2026-04-30 04:17:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d9192af-5e48-372a-857b-d6fc1adf6947 | -16.58622 | -46.96365 | 2026-04-30 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7fe1aa7-47d6-3596-b257-c678618f0214 | -6.43798 | -44.58249 | 2026-04-30 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eec9a31-94f0-3164-bc61-3cff996d2fde | -13.41354 | -43.75476 | 2026-04-30 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b8b417a-40e7-3772-95bc-ff907d79ab89 | -14.46621 | -46.98259 | 2026-04-30 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00333da5-8511-3647-aeab-d7bcaabf6482 | -17.38833 | -42.63047 | 2026-04-30 04:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8018b422-0b4c-3334-8441-96256ad447a7 | -13.3768 | -54.27094 | 2026-04-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f1c4de9-7fca-3a38-b60e-b3f2acd4fabc | -15.37391 | -52.22987 | 2026-04-30 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b9e9a51-5fb9-379c-b68d-31b57e5f89ef | -6.25124 | -42.57786 | 2026-04-30 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8960433a-13e2-3b35-b3da-c8a851f53893 | -13.37311 | -54.27169 | 2026-04-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c4f983d-da4c-3f78-8efc-4506e6aa0aeb | -9.64253 | -42.95038 | 2026-04-30 04:17:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6e4fd6f-5d99-3b38-bddc-42966c6b5033 | -9.45982 | -46.12374 | 2026-04-30 04:17:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30934ffa-dd75-3b58-9108-62660dedee8d | -9.46677 | -46.12493 | 2026-04-30 04:17:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f09eb224-afdb-3b01-bd30-b3bde87ec6bb | -11.01274 | -42.85031 | 2026-04-30 04:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e78a9d8-2b9e-3cc9-998b-46f73caf38e9 | -13.69671 | -55.6942 | 2026-04-30 04:17:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d8f6033-28ed-3d10-8a8a-8a1c9a05ce04 | -5.81361 | -44.49458 | 2026-04-30 04:17:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6718a2d-11a8-33a5-8948-5607bcd7a2c8 | -14.76319 | -46.58524 | 2026-04-30 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb2d4812-a3d2-38f0-813d-2a5b5fd827af | -13.54327 | -43.5718 | 2026-04-30 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1367cb6b-db42-386b-a2ca-435d39eea6df | -13.37919 | -54.26922 | 2026-04-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00816d07-3761-3b32-83c9-e6d9f65e6c9d | -13.37143 | -54.26981 | 2026-04-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
