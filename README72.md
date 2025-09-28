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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b46ef5a-9973-33be-8eb4-88b86aa04fb9 | -10.92342 | -42.84638 | 2025-09-28 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18adc229-b860-37e2-afbf-4bb1c6de7857 | -11.71919 | -44.42001 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc314b45-acd2-3e98-b147-662c817735be | -7.34976 | -42.10473 | 2025-09-28 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6fbf5810-119f-37eb-89b7-b1b9855b8e2a | -8.28835 | -45.4521 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93693d31-07dd-372e-8d3b-312c0c628c5e | -7.53615 | -46.09737 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27ad314a-42dc-38fd-b563-1a649abf47bd | -5.93121 | -43.34108 | 2025-09-28 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 788ccce5-b2ee-390d-9095-1a5e1c24b19e | -6.68816 | -42.74249 | 2025-09-28 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c35ff5cb-bea7-3aef-aaee-6589d23b6cd0 | -8.50098 | -44.72823 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b72ba4f3-c3bc-344c-8f70-58d0c42c3340 | -8.84401 | -47.76967 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1e55b2b-9900-3b82-b121-0996d9cb95d3 | -6.6111 | -45.08469 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2cd49d4-1cd7-3e97-9182-4a9804c636d5 | -12.68385 | -46.87402 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc004b85-27df-3c7b-930f-f912cc674b09 | -11.97895 | -47.08391 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c627efd7-cc2f-3ccb-b9eb-5fed203e3527 | -11.42742 | -46.6377 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c87d412b-4f30-3ea2-972e-cbd7c966f10e | -7.1705 | -45.50318 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3d2f284-6745-38a5-8bb0-f7b484310240 | -11.9557 | -47.89908 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79015b5a-4573-376a-aff7-724558a62033 | -7.44451 | -46.97884 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1140d9a-4110-3cc0-9518-104a44d6c7e3 | -11.3717 | -44.96473 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f275b691-9fc1-35ec-8354-5f877313d586 | -11.77685 | -43.76751 | 2025-09-28 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7433ce32-13ba-33da-8cf0-8e4ec0964654 | -8.92078 | -46.1012 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b522e84b-bd9d-348e-8c0b-f70e16d53734 | -7.24844 | -44.76633 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9558b9d4-13d6-3ad2-b8f2-9d1c0a3e7b18 | -9.07368 | -45.53376 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81682508-cf6f-3a25-99bd-2f0eb4abeaec | -6.293 | -43.26958 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e9be18a-accf-3be8-a8c6-573696c85cd8 | -7.75159 | -46.97078 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 617b505a-db31-3b2c-bfc2-802c68b7f453 | -9.21606 | -46.77346 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4788e45-4121-3f6d-8b6a-23fe8db5523a | -12.90387 | -45.15096 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6904b9db-01ca-36ae-a1c5-239bb17ede78 | -10.11754 | -45.76089 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e63d61e-8522-3992-9088-ee92f62f0dce | -6.40064 | -43.95388 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc6b67ef-eacf-3dc6-a742-2867e9f9ab9e | -9.43886 | -43.70353 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9e5b1bea-8aa9-32b1-b951-dde4c59fabb8 | -6.60783 | -44.10906 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d636657-a9fc-3ef8-b3a1-de82a8a84a93 | -6.31066 | -43.46046 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ad66e02-73b6-34d6-a886-a77d12fe89c8 | -10.94445 | -47.78423 | 2025-09-28 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fbc3b90-4fe7-3d9d-a58b-5d268826dec9 | -8.85932 | -46.60285 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b88b4f0f-34bb-3fb8-a07d-3b2444de8e6d | -6.42713 | -43.07979 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 979df2d9-e214-3fde-bf48-926c59df90b5 | -8.64855 | -43.989 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aef931e-05da-3320-836c-f20833595533 | -7.54885 | -46.10293 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33a68d3f-2e5a-3773-bfac-dd5e9da3ad1e | -11.43469 | -43.50949 | 2025-09-28 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479fc8c9-dfe2-3ccf-b0f2-e35b93b56b50 | -12.00892 | -47.96918 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e29110af-38a4-3395-9ab5-e658a2ce71aa | -7.73888 | -47.00803 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccf2e4ba-6df0-3ce3-ac24-33e3caeb8444 | -11.64253 | -48.58208 | 2025-09-28 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 188c9bc3-823d-3af6-9eca-cdebf224b18b | -8.83166 | -45.99705 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc8a9c91-2c4d-3fea-9f3b-c7a2a32b8e3c | -5.82053 | -44.44519 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13ea5b55-451e-3ccc-bb1f-d5e9b846171f | -12.94965 | -46.38099 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 930f321c-9358-3b08-9cb7-cf5f65ba3059 | -11.40433 | -46.93773 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965dd3d3-785e-3255-a277-c024c4744951 | -9.41137 | -54.69741 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ebbeaf5-9757-39c2-a8cc-30adc19249af | -9.54301 | -47.77334 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8269713-5973-34b4-aef3-4a93dde1485a | -11.37111 | -45.01672 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2f8ae7e-9b53-352d-9ea3-456d67c087fb | -11.36823 | -44.96416 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed9481c1-2139-3e65-9c7d-3341e9f99d83 | -7.75215 | -46.98872 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2d2ab32-7155-36e4-abf6-6603a4533e29 | -9.21937 | -46.77399 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1ad101b-fe31-3334-bb75-e8d44c97ef22 | -6.64981 | -43.87287 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 684b90d1-5ce9-3341-9faa-4781bbe6ee8f | -12.67885 | -46.88422 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d8987551-c395-39f2-8b0a-be989927ad2c | -7.75159 | -47.01363 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74c4a9d5-ef3a-3d43-8205-6525dd8f2654 | -9.03687 | -48.92296 | 2025-09-28 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a85f273-fee2-3f8a-820a-c160115f1332 | -13.29891 | -44.15778 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac182631-f433-3d05-86ba-6e4881d05361 | -7.23037 | -44.771 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c95d46d1-0947-3864-8c49-b566a6393a29 | -8.17217 | -46.39341 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7be06492-9225-3b21-8fbd-4f911775aa0d | -9.57112 | -45.44699 | 2025-09-28 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 999188c9-a446-3cd2-bc10-23435b7b6513 | -7.92944 | -42.6742 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b50455fa-104a-3376-84d5-a5ef641c9722 | -7.16608 | -45.50968 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49218e62-ff41-31ac-bbe4-82239260d199 | -8.2917 | -45.45262 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d71278aa-bea6-3ff2-8517-bbf9d56f7208 | -10.30146 | -45.4054 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaba384-35f7-3749-9241-bb904e201ffb | -7.75546 | -46.96782 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ae90f18-c2d8-3e7c-932e-f5351e110ddf | -10.76687 | -49.02912 | 2025-09-28 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd62c4ca-b4d7-3892-b314-66229558ee19 | -8.47515 | -47.80124 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7181577-facb-3f55-8b48-98b4a07b1830 | -8.72021 | -47.98388 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be8d8c74-4b94-3a9e-83a7-69e76360fe80 | -6.99208 | -43.78302 | 2025-09-28 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 288ef60b-6d03-3a74-bbcb-59e05a0e4968 | -9.31542 | -45.67682 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d5b3a56-f135-3158-bbe2-8a46a84e43ff | -10.11124 | -45.66752 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adf42900-2cd8-3edd-aa6f-2ba8251d3c19 | -9.96325 | -43.61808 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a2cc24b-9ef3-3b13-ba98-b7f5543502fc | -8.64501 | -48.91953 | 2025-09-28 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77d73821-0276-38ad-88a8-0005913a3eb6 | -11.363 | -44.99961 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7af75fbc-563c-361f-b25c-f4d5afb568df | -10.91141 | -45.74167 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b55d13b-787c-357c-9182-43a05070a620 | -11.44128 | -44.97523 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a538929-86c9-35bd-b65e-2dfd8f5325bb | -8.47907 | -47.79823 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 228a97b4-3c56-32ed-82fb-7d2a994bd750 | -12.25563 | -44.09663 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b6ae89f-817e-30b8-98d6-ebac63940ac6 | -6.43317 | -43.50982 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8454b15a-52de-3956-a687-99aa4a4ebe4a | -11.7198 | -44.41587 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e521012-aabf-3177-b287-61c41633ee8c | -6.76201 | -41.75466 | 2025-09-28 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24227283-da93-3aff-8b8a-ce52e6ce41f1 | -6.06822 | -43.76854 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 893572a8-9f23-3043-aaa3-4f9e1bd3f563 | -10.95567 | -49.60379 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1045ec1-5a13-3f8c-90ed-9282a9a44b49 | -7.75932 | -45.73566 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dfa9e45-48a7-3ddd-b488-5c7dbe6b31bd | -6.49478 | -44.24925 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3235686-89e2-3632-8f7d-062dcf1ac3bc | -6.54185 | -43.82175 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75b9c9b4-5310-3e53-b1e0-2e544baf4b21 | -12.9378 | -45.11542 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b036745c-a650-388f-9d5f-30d6e0c31573 | -10.41154 | -48.14421 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50c4e03d-9c5c-34f3-9c24-a3b6226429cf | -9.04904 | -45.51519 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148778bd-f882-3e2d-a606-54eee3cba1af | -12.40562 | -47.50296 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d02e990f-00b4-322c-978a-ae0c6966c3e9 | -7.74551 | -47.00908 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6af6e41-352f-3963-bb2f-f5375ee39c4c | -6.95479 | -45.30081 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49489e0b-243a-32d1-9484-b1b0c27a66e4 | -11.39112 | -46.97884 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45e62d9b-eab2-39b6-8df0-14355525c70c | -11.98502 | -47.06683 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 194b39a0-53b1-33fc-93c3-29d7baa17728 | -7.82163 | -48.80013 | 2025-09-28 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63be2f24-efb3-3c28-b5e5-54014f96f7bb | -9.44913 | -50.89714 | 2025-09-28 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0925f93-8140-3ed9-ac88-09e96002e4f2 | -11.14807 | -54.31476 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9492165d-f290-3f7f-8682-00912aca9a8e | -6.39659 | -43.95715 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf35ade-2dee-3e18-a084-0f8980973608 | -6.58122 | -43.41744 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 496424f9-0ec9-32bd-94af-5f6c31cd9aff | -9.11324 | -45.86802 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11ae3cbc-9bc4-36ef-a961-7f71fd45befc | -11.97134 | -46.58927 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bb38afc-bd98-3d3a-9ede-7ac20d4f9583 | -10.97417 | -54.10332 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ad7f55f-b18e-3b3f-a651-c5e4e9a8ad4c | -6.40351 | -43.95823 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README73.md)
