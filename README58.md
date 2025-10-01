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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 487070b1-b3ac-3399-ac1e-45b182aff53f | -13.33131 | -47.84082 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 476061ce-fef3-38db-8b29-6a7ffef16463 | -14.21578 | -46.10711 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab7fd352-5769-3ba6-8c20-ba4b3072a415 | -12.87654 | -46.77005 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87a0127d-585d-3d0a-a3b0-5fdddad6e701 | -16.40212 | -47.05118 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e13b47a-9acb-353e-97a1-f5d9d53c10ae | -13.20783 | -47.44748 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45508b98-3dbc-3ff4-94e2-e4a014caefbe | -11.82368 | -44.98973 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48b0dd99-bbc0-3bc2-80a7-de1bbd43f6eb | -14.71467 | -48.15366 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3dcc816-bdd5-359d-911f-6fe60fd22ac3 | -11.84435 | -48.05464 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f526776-b0e6-3c6b-9b16-fe4f725824eb | -15.10799 | -44.95195 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d5d85c-9184-3d32-8b67-9f51028efb82 | -12.77291 | -46.86554 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30de774f-1ad5-33b1-9e27-4fc83dc90450 | -11.45896 | -45.08514 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdb4f154-13b3-32af-a3d2-fbc29371bc93 | -12.8756 | -47.11908 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1014b7fb-d14e-3734-b434-f510a95092ad | -12.97189 | -48.42459 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de392829-9a64-3d22-9de9-6903a6c3c246 | -15.63202 | -46.24926 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17915aec-4395-39fe-8368-63a3822647e3 | -14.90776 | -51.67426 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b9856e12-dcb7-316f-8325-a65ac7e7cb9e | -11.82253 | -44.97494 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58580301-14f7-3c8c-b7da-f709395d4225 | -11.81756 | -44.98515 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a79f2150-2159-399e-a057-b11aa6911aa0 | -14.62312 | -46.98407 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7a6657-ed77-39f1-8e3e-d61c408602a5 | -16.40704 | -47.063 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e30c14bd-4e34-3dae-8dba-9f516f101c53 | -13.34741 | -47.80542 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4355eb0-f22e-39ce-8b10-e3c1c3ef2463 | -13.06819 | -47.06395 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b679f546-76f9-3e53-aeb0-e519e525c068 | -11.80114 | -46.61848 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ea962715-e062-3ad3-aeb5-bb9776819df0 | -10.9132 | -46.50883 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| dc7c939b-32bd-3ed4-a193-562a607e06f4 | -13.41269 | -48.16017 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 608ddf8f-b14d-3657-956c-329749526852 | -11.59543 | -45.03731 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0dd29cec-361e-3bbe-a37c-caff09578e2d | -16.38347 | -47.01872 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fb06a06-21e7-3179-9b5f-532a4449fdb5 | -14.5086 | -48.49122 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07dae3ad-db5b-3d46-9d4c-1be400757cfc | -15.3714 | -47.0724 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ff263eb-c2fd-35a8-8753-aeef86aa8eed | -15.2766 | -47.83612 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d89ad14-c816-3ddf-a02c-d1828a964cb2 | -14.99331 | -46.9656 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d64b924-65cc-3ce4-8508-986fec60a02c | -15.75318 | -43.69253 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1786752-ffcf-302e-9113-11ce11e574cc | -16.24433 | -44.05495 | 2025-10-01 04:21:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b3be342-c130-3921-abbc-25bb1b89808c | -15.9426 | -48.12156 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be2fe36d-418d-3246-a156-d98759e2b84a | -12.00648 | -46.59036 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 759b9725-2484-3599-adeb-392d48b20473 | -14.67995 | -45.28927 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f1944f0-a3a8-386b-9628-f48382651d90 | -15.15656 | -49.09888 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c21f5610-016a-3270-9d36-dc68c6a54f89 | -13.69861 | -48.64484 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb704ba2-7c0b-3c26-ae7b-43c4d03b98a5 | -18.33629 | -41.81084 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbca2767-2f5a-3d42-b831-5241e4286186 | -14.61108 | -45.02176 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d21d3e03-3a48-351a-bbf2-3026d57cdc69 | -15.15722 | -49.09496 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 803ed466-c688-39e0-8763-4b559641e147 | -13.70809 | -48.63044 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f64874a-d966-3803-97d4-548324d013c9 | -14.92483 | -47.82081 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efd1aad9-e6dd-32af-9828-37a05ce9060c | -14.49573 | -48.44244 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c87e9ed6-ec1a-3056-a647-314471a2c83d | -11.85253 | -45.00163 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c0923aa3-8fdb-384a-bc62-24d4cc713bbe | -11.81369 | -44.98819 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 111c2e14-4e34-3569-94f6-05805a284da0 | -16.2446 | -50.93419 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b59bf04c-596d-35f1-a14a-65778154f52d | -14.78762 | -46.97491 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aee280c6-6774-3ae7-8212-4586ee896868 | -15.48912 | -45.91653 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8def6cea-f047-3940-bb58-6fa19ba8e743 | -14.70546 | -48.12535 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1983724e-9e9a-3a9d-a1cf-4f52e53c21c5 | -16.86727 | -44.27488 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 068e0204-0428-3316-b604-beeaf9f95bfe | -13.97982 | -45.06757 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e071ce5-b922-3225-958a-d11ac3395eeb | -12.94481 | -48.42052 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd3eb8ef-e228-3d88-b60c-1e9f1802734e | -15.53248 | -45.22813 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eac1dc7-db66-3abe-afba-8d26f784e8ab | -17.38771 | -47.14302 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9acb02a9-750c-3d79-90e4-944c4d21e13b | -11.63707 | -47.49272 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bfe872e-d607-3124-9437-8ecddeeabbd8 | -14.68374 | -46.965 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 211555a7-af7a-37dc-a7f0-2a885203b23a | -14.90502 | -48.13255 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d4d6876-d593-3400-94d5-46f549f5607e | -11.75844 | -46.86565 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1358c08b-f78e-31cf-9e39-81d67a0a34f2 | -14.5986 | -48.21824 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92842581-a304-3d3b-89e8-cfd24d8ddf1d | -12.78346 | -47.73136 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f9a7e02-8cb1-3ea6-92fb-97f90e9116d1 | -11.85421 | -45.01284 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d7dc864-ef91-3018-b186-6cb89416aa08 | -13.76319 | -48.40465 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcf5c72a-5117-3313-bc08-618b77cbfcc7 | -17.39157 | -47.14 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2925d83f-bde5-3e34-bc3c-5d4af1f71eb8 | -14.55116 | -48.23289 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b083fc31-6135-3bf5-b2e3-67990891f20d | -14.56144 | -48.48866 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b1d5148-f54c-3dc5-b431-2de2e3352605 | -10.8309 | -47.95382 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd08d388-3803-3d89-bdcc-3f4e22f89511 | -15.29365 | -46.19448 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61e90b09-870a-3fb6-aab2-38e7b7d488b1 | -11.83252 | -44.97651 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bdbe3e1-82e9-30cb-b2ad-5b56ed2f0e74 | -12.8867 | -44.68443 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79b24acd-a031-3d09-b7a2-9330b8c7a9eb | -12.69941 | -48.56618 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a463ebdb-b75f-3b4f-a9cd-392cc25f61d3 | -11.84309 | -48.06225 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76ee969b-bfc6-38d7-b631-d0c576b177ba | -12.39474 | -44.76575 | 2025-10-01 04:21:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d738e49-63c3-3a91-9ad9-e75397af0ea2 | -13.41397 | -48.19515 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a8e067b-5425-3fbf-9be8-4c5dad992d9f | -11.16859 | -54.11722 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 18e20df0-eeb7-3ca9-9198-07c0c2e83936 | -14.21046 | -44.93283 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d71f6dfd-772f-3524-8fda-9e6b0b3ab602 | -12.46214 | -50.22242 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ee137a7-7838-31b5-88f9-34e40b7afe1b | -14.61336 | -45.02974 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03d1e098-ce1d-36af-a70d-853877d677ab | -10.98408 | -46.53476 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03d84465-3b09-392f-8cc0-2963acc73448 | -14.79204 | -46.96836 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c98a01c-4c48-35e9-9949-3c1ab0de818d | -15.15219 | -48.01657 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd8f9ff7-5b33-32bf-aa8e-8ef41aa491e3 | -13.13227 | -47.42743 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca14614b-ab44-3dbb-aaf5-5af384960aa8 | -12.28195 | -47.82644 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9156b17-f0b2-34df-b3f2-f503a0d10f54 | -14.41083 | -47.14156 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e0c52ea-9fe6-368f-99f4-06399a0cdc7d | -11.82423 | -44.98615 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbc29353-22f9-3da6-a0f0-2cfb1503d216 | -14.68472 | -45.18819 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26544bdb-020b-3841-9832-ce5f6757d1bb | -15.41548 | -47.05053 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 907af4e4-1c1c-383b-8d3b-9b593a38dee0 | -12.89844 | -47.08277 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38f6b70f-6389-3ebd-ac73-15fd99828eb7 | -11.27611 | -47.8098 | 2025-10-01 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 158e03b0-efeb-3807-b5e2-471fd50daa1c | -11.08109 | -47.81991 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d23414f-f62a-3c86-81be-126d99b26401 | -15.49077 | -45.90569 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0691e497-ca6d-3da3-89cb-67fe5b45cf07 | -15.26878 | -47.84222 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 435e8331-dd97-3dcc-9bc7-1a8ebfc06e9a | -13.36053 | -48.1592 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65d47c35-14e9-3cbb-a4bf-f7ced57ec0a4 | -14.50923 | -48.48742 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29af137a-4c42-3b7f-b722-3b5a78f1529e | -12.63989 | -44.22815 | 2025-10-01 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61314725-c006-3b0f-848b-0abf5643920e | -13.41729 | -48.15332 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eb7b8c0-6b36-3c8e-97cb-62b658f32535 | -14.98672 | -46.96449 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f45e5d04-28a8-3853-ad69-bc142791df4c | -12.85212 | -47.00967 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a3eed02-4ba1-36db-8b5a-312b57ec3f1c | -13.41336 | -48.19889 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da571c6-3569-3ec2-a39c-23c4d4540ce2 | -10.79832 | -45.3545 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b875ede8-d012-374d-9cf0-fd4f01121748 | -11.39536 | -44.90063 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README59.md)
