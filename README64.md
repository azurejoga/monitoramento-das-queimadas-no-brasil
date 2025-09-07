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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93dcad13-4a65-3a80-8ca1-c346092bc93a | -20.85374 | -54.98306 | 2025-09-07 04:23:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95a8f39-68a1-38dc-9b62-d4b93dc4c598 | -24.14392 | -49.50998 | 2025-09-07 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e8920bb-3a87-38fb-8d56-303e41db3c1d | -22.17203 | -47.31138 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1f8234b-ae33-366f-ad4b-8fe1dc36c772 | -22.16704 | -47.29881 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d13ee95-7dc4-3a11-ba67-75f10ed3f86f | -22.14417 | -49.12005 | 2025-09-07 04:23:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c96f3a0b-0fbb-313e-ac28-a6f89272185a | -23.49065 | -51.08943 | 2025-09-07 04:23:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9b8cc83c-7710-301c-9237-da7541c92120 | -21.67642 | -45.08598 | 2025-09-07 04:23:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a0b2435-0f55-3846-bed2-9dc241d03114 | -22.7059 | -46.91806 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4e626f1d-0cfc-3119-a043-87ca9bddfaa5 | -21.89499 | -46.49245 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f3010083-a272-3004-bc28-9b6b6eb90979 | -23.55693 | -50.14201 | 2025-09-07 04:23:00 | NOAA-20 | CONSELHEIRO MAIRINCK | PARANÁ | Brasil | 4106100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 27793c5c-c64d-3875-a7fa-16e683e97cf1 | -23.2057 | -50.82524 | 2025-09-07 04:23:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c99c3f0a-6ed5-33a8-9262-c2e983fed810 | -22.16811 | -47.31456 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 538ca546-7ab1-33e4-9c97-4acdc0fd763b | -22.69517 | -46.92013 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 242bffdf-2f92-363c-8e50-b3fd1e81d43c | -21.70843 | -45.3833 | 2025-09-07 04:23:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e6f4efdd-dbdc-328a-ae0f-6fe025421a9b | -19.88145 | -57.90059 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 4433ecb3-e607-3247-aa52-fb40ea39da9b | -21.83422 | -46.45403 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 662aa5fc-0511-3bc2-b9cf-029b7bec12b8 | -22.77753 | -51.3018 | 2025-09-07 04:23:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 583cae7e-c0b9-3a53-90ad-a3c74bf8e61f | -22.16982 | -47.3032 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 972352a7-c36b-3909-bd4a-4db2ec288aa2 | -22.69896 | -53.24446 | 2025-09-07 04:23:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5bc41a34-70d1-37a7-9f26-9e7bebb85544 | -23.94465 | -51.12968 | 2025-09-07 04:23:00 | NOAA-20 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1097029c-adb8-38d3-8934-d9800e804a8c | -21.2084 | -44.33736 | 2025-09-07 04:23:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cc282e7-2301-392c-860d-3381f5775378 | -21.48481 | -45.56273 | 2025-09-07 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 93a8e18e-0eeb-3442-bef9-8a417b694e19 | -21.86712 | -46.49201 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a3cd4513-2b27-3903-97d5-2e803132985e | -22.70078 | -46.92916 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f0c93c13-e221-3b26-8f45-1a38572da92e | -19.87687 | -57.89563 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 6a40e19c-4684-3e6d-9740-82174d92fa4f | -19.87072 | -57.89794 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 56b0cf46-be7c-3a24-88b5-8cc825ea81da | -22.1726 | -47.30759 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8fa6a80-9898-3a49-89fe-fd0e4edc5a29 | -22.41833 | -47.43513 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c611b364-1eee-3fdf-80c8-69cb88b4a94f | -22.41775 | -47.43893 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fe2903d9-ee8c-3e37-8405-a992b9b03812 | -21.50167 | -48.65495 | 2025-09-07 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 666e8ada-ff1d-354e-8988-71958062a165 | -21.7123 | -44.51711 | 2025-09-07 04:23:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 07d72f94-cfb2-3828-8a9e-ec24735cc336 | -22.16313 | -47.302 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b222fe35-7698-3a8f-a8a8-c98458160c71 | -23.01741 | -44.93322 | 2025-09-07 04:23:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 419d3c53-501f-3365-8b61-cebd885e9c7a | -21.48422 | -45.56688 | 2025-09-07 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 281b39b0-9295-3702-a15f-874d6894ffe4 | -22.69798 | -46.92466 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dd60bfe2-21b9-3a09-a894-21642d3f503a | -22.698 | -53.24963 | 2025-09-07 04:23:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f89d550f-2ce0-3484-b864-e4e7796a209e | -22.70252 | -46.91743 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fd237d04-2c06-307d-a4ee-6c9ae8c81bb2 | -21.48129 | -45.56217 | 2025-09-07 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| d9d77e30-3293-326b-85c6-ba45fc1f614c | -19.86615 | -57.89298 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 41e747cd-2455-3ebf-bf6e-2aec47081c58 | -22.17317 | -47.3038 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 00cded74-019c-3070-a357-7751f2d6f11b | -22.41717 | -47.44276 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2ec9a1c-9b76-3596-93a0-ad722ec4125e | -22.42167 | -47.43573 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0c0b151b-04b9-3216-852e-e0bc937be809 | -22.16925 | -47.30699 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b51c552c-bd3b-30da-a6bb-65299046acc8 | -22.16533 | -47.31018 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c627886-bd70-30b6-acc4-e414fcfe25c3 | -21.70861 | -44.5165 | 2025-09-07 04:23:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3917d23e-a821-37bf-be78-0581c470d880 | -22.41499 | -47.43454 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 32ecc827-060d-3bdf-99e8-030ee0caa459 | -20.48925 | -54.56969 | 2025-09-07 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b3d7e85-c2cf-3749-818b-cef186e7a097 | -21.42735 | -44.1713 | 2025-09-07 04:23:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 26b4e397-93d5-3268-a362-b5bdc5ab28ab | -22.33013 | -49.37825 | 2025-09-07 04:23:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 643a2e0f-6dd3-34f1-8551-ea5a0c115179 | -20.79858 | -49.32519 | 2025-09-07 04:23:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 97f099df-4565-3846-ac36-17090df9e46e | -19.8868 | -57.90194 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ecf66af3-230c-3b19-b838-9566f6440f78 | -24.14664 | -49.51439 | 2025-09-07 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace9f9f2-769f-3e30-8ae8-a9045d96c7bb | -22.42051 | -47.44336 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32267d3b-cb8e-3e33-be13-9dc4246acb9e | -22.45394 | -49.34239 | 2025-09-07 04:23:00 | NOAA-20 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb4619a9-8650-39dd-bb4c-7f8cc213f726 | -21.46919 | -43.91346 | 2025-09-07 04:23:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96feae26-2e49-329f-9993-abd4af0afd76 | -22.16647 | -47.3026 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f9f465cc-6829-397c-8dc4-5c3cf681510d | -20.79522 | -49.32458 | 2025-09-07 04:23:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f92adaf0-98a0-3fac-bdea-8e17db4c38a6 | -22.16868 | -47.31078 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c72a24bc-2314-3c93-aac5-618c6764fad1 | -22.4265 | -47.43916 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94b29eb2-65ef-3a6e-81c2-e2aab72093e1 | -22.77678 | -51.30605 | 2025-09-07 04:23:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 60df699c-786b-3fa5-a793-fe20b1d33d45 | -21.86312 | -46.49547 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7398add-3c41-35c1-9d6e-0f3a7ac357ec | -22.69575 | -46.9162 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 04a1d118-0acc-3d7c-ba5c-7f468e04b320 | -21.92433 | -45.41127 | 2025-09-07 04:23:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 486c478f-43cc-3120-be9a-308a16b3d25f | -22.69459 | -46.92405 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bf28ccd5-84c7-33da-9c0e-d6bd1bf9e532 | -22.17039 | -47.29941 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65c17b7e-84b1-349f-9dbd-eed90c3eef6e | -22.69855 | -46.92075 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6f426671-64bb-3fba-b6cf-2498df8c6c61 | -22.41383 | -47.44215 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 65609622-ff1c-3f87-97e7-0ab06f5bcd30 | -22.1659 | -47.30639 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c09e964f-c99d-348b-932f-c3b5a17d25e1 | -21.48774 | -45.56742 | 2025-09-07 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e7281a30-bc60-3e03-a6b5-b029010b64e8 | -22.17652 | -47.30441 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec2a8b61-1b70-3b06-ba9a-038aa4df55c7 | -19.86536 | -57.89662 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| f97a60de-a951-3fdd-a828-d6e4980d73ec | -24.14332 | -49.51374 | 2025-09-07 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb9418a-94e5-3a0a-8e96-06c9ccdbdc8a | -22.45333 | -49.34617 | 2025-09-07 04:23:00 | NOAA-20 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 885eaa82-596a-3b7e-9511-661d8cdf65b2 | -22.69914 | -46.91682 | 2025-09-07 04:23:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b88b8c15-b9bd-3566-b5d4-cee34786c38f | -24.14121 | -49.50555 | 2025-09-07 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e091f98-aa6e-3799-af48-c9722fed45ca | -20.79992 | -49.38015 | 2025-09-07 04:23:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c63f8c-427a-33f2-b2cc-d8a170ca9b6f | -20.50101 | -49.80772 | 2025-09-07 04:23:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d3953e8b-8680-3bc9-a85d-a8b5d56f3974 | -22.17595 | -47.30819 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9c400510-2b1b-362b-81cb-3598e12911a1 | -21.70783 | -45.3876 | 2025-09-07 04:23:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 62b50d1c-935a-3d4a-9baa-ca78799b9965 | -23.0168 | -44.93783 | 2025-09-07 04:23:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7283e11e-704f-3173-802e-8ee11d72e618 | -21.20904 | -44.33264 | 2025-09-07 04:23:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d184fa62-20ad-36ba-bfc2-08fbbf39241f | -21.71292 | -44.51251 | 2025-09-07 04:23:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 793661ed-b3de-3d43-8229-1cad64b06385 | -21.2909 | -48.61331 | 2025-09-07 04:23:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9b55003-edfd-3818-92d4-a969ab0cba93 | -22.16256 | -47.30579 | 2025-09-07 04:23:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d0dae23-57f8-3bfa-b225-c05d7bc6a77a | -22.56269 | -46.91816 | 2025-09-07 04:23:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a42a6383-4a6d-353e-83ea-15227daba533 | -21.86654 | -46.49597 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de0dfdd3-24c9-3e27-ba82-1ce3980bdfdd | -19.87151 | -57.89431 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| a742dac1-2dc8-3b8c-b93e-2f797c806ffb | -8.14765 | -44.87717 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9421371b-0d4f-3a4b-ae6a-718fa32b4188 | -7.68335 | -50.31214 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07000217-3ac0-339e-873c-8ab48bc5c43f | -7.75561 | -48.82119 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43049446-a30a-3043-992f-21226e30413a | -6.82384 | -52.80621 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2cdbb46d-dba3-3380-a22a-cbcb3adc3cb3 | -6.23289 | -53.57508 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea899a1-37a9-39b7-b3fe-59098fe813d0 | -2.82051 | -49.20092 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae26693-ce5a-33dd-b011-805cbee32cf8 | -6.81914 | -52.81073 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98ca3ec6-0097-3c22-ba1b-449806a8f20a | -3.59317 | -47.51997 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0fa655f7-7500-35d5-9cb5-6b6711475bd4 | -3.59651 | -47.5116 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e300b110-4bbf-3002-a853-0b891cf723cc | -7.76208 | -50.72005 | 2025-09-07 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59a96d69-bb5d-38f1-810e-1bed0b76aa5b | -2.82126 | -49.19577 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5597b023-7202-3e61-85d9-467042734b10 | -7.81394 | -45.42706 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d59c6b2-f371-33d1-a037-27d6f0eff6e1 | -3.25058 | -50.80382 | 2025-09-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README65.md)
