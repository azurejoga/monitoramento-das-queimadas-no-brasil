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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbf01cf7-efd5-34e5-acdc-6d7a88951320 | -16.17556 | -48.72009 | 2025-08-09 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dceb9ac4-8d32-378e-8440-8d9a44f46850 | -22.18627 | -47.09394 | 2025-08-09 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5d622c9-c8e4-3ad5-bd34-e8dbb5e035cb | -16.09179 | -49.32297 | 2025-08-09 04:44:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e39936a-ed8f-30b1-b199-93f920fda331 | -14.53214 | -52.11969 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ddadb29-35fb-393a-b8ed-7c70265bd34f | -19.60037 | -42.69028 | 2025-08-09 04:44:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 6ea1d35f-7671-374f-a328-1d3ff85f5e06 | -14.39643 | -56.34714 | 2025-08-09 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44807f9-f30f-3639-a408-3115102e1692 | -16.79376 | -47.51565 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7aaf6dfe-67c4-37db-8d56-10610a83f7ab | -20.47747 | -53.67581 | 2025-08-09 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae0dc50-5409-30a4-9a8e-fff1ecb5d5ff | -17.512 | -50.29286 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8969278-5eb8-31b0-8616-8a93df70db99 | -19.73736 | -42.06867 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 7d13ee4e-0d32-3a45-af72-089159e3bdb5 | -16.43356 | -54.68719 | 2025-08-09 04:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f81b835b-750e-3960-874f-6b0dd8b3d5c9 | -19.73352 | -42.07073 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 4b83f8f9-1fa2-3a66-8e0e-463f8f80bb98 | -19.7396 | -42.06705 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| afd777a3-cd80-33a0-aefb-93dde3f2350d | -17.52393 | -50.28313 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb2bf1b-c872-393a-8f8a-e6d8815c2230 | -18.60832 | -48.25761 | 2025-08-09 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e6248fd-3fc6-3e92-8f99-d3e6bb7be042 | -14.96394 | -49.55552 | 2025-08-09 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63a705ea-5500-3d4b-a263-804d72b9faeb | -17.51598 | -50.28962 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9967e953-40c4-38b6-99a0-a4b08324eae5 | -22.18207 | -47.09322 | 2025-08-09 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7f92e44-6eb5-3e3b-899c-2a9a6a0b1892 | -19.7392 | -42.07117 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 297dd772-dd47-3582-b34a-43c99cd2b08e | -16.78995 | -47.51502 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 796576e9-a2e7-3d5d-abb4-dafb590d3185 | -17.51372 | -50.28145 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10884593-ef18-3ab1-8ea2-04b00d1ee2e5 | -21.17601 | -48.02697 | 2025-08-09 04:44:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9daffc69-9ecc-33b1-9eb6-c8615c5cf373 | -21.38224 | -44.12815 | 2025-08-09 04:44:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 07fb22e0-a279-3129-b8be-602462dcd1aa | -20.50884 | -54.90525 | 2025-08-09 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e42c4647-0556-3908-8c27-92f2bfe88f2a | -19.5896 | -42.68811 | 2025-08-09 04:44:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b89c4c8c-25ee-3518-90c5-f7af22b795e1 | -21.17864 | -48.0295 | 2025-08-09 04:44:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09881bda-c436-3c9c-b9d8-8b1a01008887 | -16.9601 | -51.05295 | 2025-08-09 04:44:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26d36ba4-5c47-3ea2-b09a-6e322d520602 | -17.75503 | -48.45106 | 2025-08-09 04:44:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb1508b6-e3f5-3e46-a4ca-a2f60896ec97 | -16.98377 | -49.29625 | 2025-08-09 04:44:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2126b2e8-be7e-347e-b79f-ccf1456e6e59 | -14.3672 | -51.11484 | 2025-08-09 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cd23228-ebd0-3889-8577-2135845a35d8 | -19.81132 | -47.07004 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| cfe07c66-b9e3-384a-a63c-287a164d9913 | -15.91472 | -48.95907 | 2025-08-09 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7570320-9dbc-311c-b72d-0a14adf97eed | -19.85941 | -41.43159 | 2025-08-09 04:44:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d1fd4ed-72b6-335e-a31e-49e408b8d59f | -16.98318 | -49.30029 | 2025-08-09 04:44:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35bd3c94-1aba-338d-beac-3479d67459f9 | -19.73394 | -42.06635 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b2b6acff-eed6-3e53-b8a5-5cfa56cc6543 | -19.59541 | -42.68501 | 2025-08-09 04:44:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3e747599-cf75-35d7-a80e-d65e240cf5ee | -14.96736 | -49.55607 | 2025-08-09 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a4b5f86-e74b-339e-93b6-d0f1816fa9cd | -19.59505 | -42.6886 | 2025-08-09 04:44:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2bd23eeb-1eb6-39b9-8a21-fedd832d4585 | -17.78904 | -50.11606 | 2025-08-09 04:44:00 | NPP-375D | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59bf3b31-f4b6-3bca-85d2-1cddf50b8e9f | -23.12899 | -48.77664 | 2025-08-09 04:46:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bbcd5bd-42c8-31c0-803d-1cd7b9168589 | -21.61003 | -54.33087 | 2025-08-09 04:46:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63e32e48-51c9-37a3-a059-df8f3855785c | -8.9399 | -60.7481 | 2025-08-09 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a4b4fffc-17f4-39aa-a72e-960b709d71b3 | -7.0801 | -59.1578 | 2025-08-09 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 429367d7-5278-3142-adca-5f237a8ed488 | -8.9215 | -60.7297 | 2025-08-09 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c7a332fa-14dc-3f36-be17-71bfc1da95d9 | -8.9213 | -60.7489 | 2025-08-09 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c71240fe-333a-3f2e-baba-ef2d12e17b66 | -19.8124 | -47.0634 | 2025-08-09 04:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| b9dd5edf-4a2a-3002-8534-2147c3730cb8 | -7.0801 | -59.1578 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 4223ced6-2608-3713-b887-50babbea96c7 | -7.08 | -59.1771 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.1 |
| bf6905b3-e8c3-38f8-ab04-c9bf72b5eae6 | -8.9213 | -60.7489 | 2025-08-09 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 182fc73c-8ea3-3f7b-bb16-fd554f18dfb0 | -7.0616 | -59.1586 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 094fe5a0-dd57-3554-8317-51378fede2cd | -7.0615 | -59.1779 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| dc96684b-f285-3d26-8d21-52f9e3e78d39 | -8.9399 | -60.7481 | 2025-08-09 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9c69ff7f-977a-3576-9b41-f133fbc9b0ff | -19.8124 | -47.0634 | 2025-08-09 05:00:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a4eebbf0-8b32-31b6-a2e3-aa5b4dba90d2 | -7.0984 | -59.1763 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3e3100de-e9f5-31d6-a4f8-3840aca57d12 | -19.7396 | -42.0522 | 2025-08-09 05:00:00 | GOES-19 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| 8b63b0dc-d5af-3565-a167-2319e61d234c | -8.9401 | -60.7288 | 2025-08-09 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b7363d19-125d-3fed-9178-0705999a181f | -7.0986 | -59.157 | 2025-08-09 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 480ed0aa-75be-3eb2-9941-b52ec0be468f | -19.7388 | -42.0778 | 2025-08-09 05:00:00 | GOES-19 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| d0869ece-be73-3302-9f14-9767c38dfd0c | -19.7602 | -42.0464 | 2025-08-09 05:00:00 | GOES-19 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 8f27c1d0-c555-3edc-a17b-1bef8c1a7177 | -19.7593 | -42.0719 | 2025-08-09 05:00:00 | GOES-19 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| dbb64056-309a-3c4e-9c9f-05dba3bf1624 | -4.17204 | -48.57536 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f84c31e4-2cc6-34cb-9539-18601599feba | -4.47895 | -48.1085 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07aeffa0-e7f3-3040-9efa-507162996b0b | -3.82352 | -41.56348 | 2025-08-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d203f1a8-0624-3688-b9aa-ab759b71d573 | -5.2163 | -46.07347 | 2025-08-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3978da19-fffc-3640-ad59-d1f0166ad767 | -3.96358 | -47.88618 | 2025-08-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93ea64d7-bb56-3aa1-9490-c0c88aec9096 | -4.3399 | -49.35777 | 2025-08-09 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1936d742-93ab-3d59-b93f-a1f0eae343e9 | -4.17136 | -48.58006 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ff82e5c-b3f9-3811-b920-5a848b1a0488 | -3.98736 | -47.88995 | 2025-08-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90c6a028-6919-319a-9304-03f67a75fa13 | -3.42455 | -49.04235 | 2025-08-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5fcab339-d017-3b64-98b2-5bb88b7800c9 | -5.83805 | -42.95465 | 2025-08-09 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 441c5bda-d5aa-36c2-8f32-255ae1008ef4 | -3.84182 | -47.75012 | 2025-08-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 73d95471-07f9-3565-98ad-e39cab44af65 | -4.69955 | -48.58499 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d559795e-55e2-3fae-937e-519fb6f7d2f9 | -5.21072 | -46.07329 | 2025-08-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7f83309-6406-3b6d-a996-6e0963e2bfb2 | -3.81966 | -41.56681 | 2025-08-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39f4c3fe-6767-3736-a6a0-4792d409d2a0 | -3.85746 | -54.08178 | 2025-08-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98d18c6c-8bc3-385d-b4f4-1d54eb995936 | -4.3025 | -48.07431 | 2025-08-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e3c65ee-102c-3b6a-aeb6-dae2f6bc4bbc | -4.14972 | -48.21616 | 2025-08-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f549ff5a-144c-3145-9c1f-67fe64e16f83 | -3.84105 | -47.75522 | 2025-08-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88ec58f8-1a57-3a04-940c-5afdc7637fc7 | -4.34052 | -49.35368 | 2025-08-09 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fd5b555-4c7f-3282-b91d-64008143f400 | -5.2168 | -46.0699 | 2025-08-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e96fb05-79e4-3dad-a45e-3a3acaed7e5e | -5.27403 | -44.94923 | 2025-08-09 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d763f579-7e1c-329a-8212-fa051f93b7fc | -5.21579 | -46.07705 | 2025-08-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5fef24ea-c539-3e95-be2e-b8500cdb5cc4 | -3.82254 | -41.57044 | 2025-08-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75429f5c-d770-32cd-b344-8cbfdc9b114b | -5.27462 | -44.94505 | 2025-08-09 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78eae3cd-2d50-3b1f-905a-2b8a29124a26 | -4.47348 | -48.11288 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e0363e9-eb45-3c3e-b5d7-1dc0f6b9a1d6 | -4.17089 | -48.57702 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ca0e194-18b5-349a-8e2e-ca7657109da3 | -3.96432 | -47.88111 | 2025-08-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3695b97d-33db-3905-b1b9-5144f26e07e1 | -3.81864 | -41.57371 | 2025-08-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c4d5047-02fb-355d-9bda-fcdcb72d67bc | -4.81839 | -47.31853 | 2025-08-09 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a38269d-2f24-36c4-a8af-16526b779e08 | -3.42956 | -49.03876 | 2025-08-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8892e42-1c11-3604-b178-3b2ce69792fe | -4.47276 | -48.11789 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6f834f8-ed87-3db8-b98e-655be050b1fc | -4.29531 | -48.05764 | 2025-08-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 99a3ce04-7754-309e-bcfc-f59b85c54aa5 | -4.29457 | -48.06265 | 2025-08-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9e6a8a6-a456-3459-89bd-beea00182412 | -4.47821 | -48.11359 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 825b2ca4-b78e-3930-8d32-7d1e7bdc631e | -4.29778 | -48.07359 | 2025-08-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3d41ea-e0d1-335c-974d-181bfa1dc174 | -3.18092 | -48.81002 | 2025-08-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87dd4b84-6435-34ab-9cb3-eb949e1f82b6 | -5.27345 | -44.95336 | 2025-08-09 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81dff966-9c9a-3abd-9807-8adf124b11bf | -4.87215 | -47.75743 | 2025-08-09 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f871f6b-4fab-3c8e-b4ea-fa55a561a8f3 | -4.47748 | -48.11857 | 2025-08-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1c92c59-bae3-31bc-b1b2-38d385abfad2 | -3.42891 | -49.04301 | 2025-08-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README24.md)
