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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 484981c9-082b-3539-b342-d54145c9cfca | -11.19369 | -54.81416 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145c1fe1-8123-335a-84e8-56a8725e6d6e | -8.54333 | -54.72929 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 115678e5-0868-3998-9496-cc8b974ffba1 | -8.5303 | -54.73412 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2b44563-4c94-3e54-b1e5-0a0b49ccb1e3 | -8.5369 | -54.72219 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 945644cb-ab7a-3b8a-9cc3-d0dbe4c728e2 | -14.45437 | -45.62738 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 886f28c8-9899-3587-b51c-decf17ca7a94 | -11.3805 | -46.39038 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc276d10-1caf-3e03-81ad-bcbeb41ca669 | -8.53615 | -54.72643 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69981449-fea1-3a86-b3fc-2126d00701f2 | -17.44059 | -47.16556 | 2026-08-19 04:42:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd8d73a2-f9c9-334f-9552-41dfa02ea261 | -16.52794 | -54.69063 | 2026-08-19 04:42:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00cbd325-85ca-3b55-97da-ae39279ad89d | -19.07964 | -57.35363 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ee986f78-2c72-38f8-84d5-93780370b1a7 | -22.98451 | -50.02494 | 2026-08-19 04:42:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 6e265e05-84a0-3e56-89e2-0a3ee639472d | -19.73966 | -57.95241 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2c8be6d1-45fa-302a-9790-21fdc4954d5c | -18.58311 | -41.3284 | 2026-08-19 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77b3fa57-7992-3f25-b2e0-6f960a432558 | -21.52701 | -52.00451 | 2026-08-19 04:42:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| db4a72d9-7ad5-3f43-bb9c-d16ca66b1d4e | -20.18473 | -44.59359 | 2026-08-19 04:42:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05c20b22-49d9-3b5d-90e4-09aefc2519c4 | -19.75629 | -57.96086 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 39bb85e8-01f5-335b-bf0b-c5aa00e2289b | -19.76506 | -57.96281 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6539f483-960e-3835-a4e5-270c0a93fac3 | -18.50998 | -51.58069 | 2026-08-19 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f10db1ee-7b40-3ef1-a472-9aee9f87a349 | -21.40214 | -48.71237 | 2026-08-19 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86e26c54-8efa-33e4-9d2e-cdac0547d6d1 | -18.86504 | -48.87638 | 2026-08-19 04:42:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27941e97-8fb0-3051-8e2c-f7e50945a541 | -17.99203 | -48.54281 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e93da461-f97d-338a-8893-02eb3c71cfa1 | -19.7318 | -57.94592 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6ab249c0-a559-3329-baea-418726a49304 | -19.7502 | -57.94531 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a12acb39-e99c-3dfa-924e-9b1f4a6b64fa | -17.95606 | -44.44545 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1480e5a1-3631-36d8-be5d-e3bc47cbc263 | -22.36514 | -46.91036 | 2026-08-19 04:42:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 893cb661-8b8a-33e3-a98e-1eafae72be77 | -17.5905 | -44.59564 | 2026-08-19 04:42:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7475db50-0f1b-362d-8699-bdeb1b3a7311 | -15.87679 | -55.55237 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa224e0d-a0a9-3f7b-b48c-b8c858cfb6b9 | -19.74582 | -57.94433 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a011d1e4-d314-3b5d-844d-b56be6daaf09 | -20.2991 | -46.48774 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c544c55-ca20-3d3a-a96d-0aefd8fe1d4f | -20.4146 | -44.08942 | 2026-08-19 04:42:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f937d16-ad90-33b9-84d9-826901df257d | -20.58088 | -45.93134 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42f86c9a-51ca-3ba1-98e8-d30bba02b6ee | -19.67768 | -45.90991 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 173162b0-8cf1-371f-a6c8-4e86520a707e | -16.24685 | -57.66701 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 296c38b1-3312-3c95-9c0a-f3ab0183ea05 | -19.46784 | -44.18006 | 2026-08-19 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a618b23f-2ded-3b00-b7a7-2af3fd0367b6 | -19.75807 | -57.95179 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 29a0eb03-311b-39fa-9b32-0ac6b2cff3e4 | -16.25915 | -57.67158 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9b182bbf-e534-32f5-a722-0a510da53803 | -20.88276 | -45.2913 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4119dbc2-5ff1-3ccc-b7f2-c4e2877498b7 | -16.24881 | -57.65666 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 156e7e59-fb83-3ca8-8741-c41c7f147869 | -15.87939 | -55.56118 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00a61f9b-ac15-393b-9e84-5790e27860b9 | -15.88607 | -55.57062 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78caae2f-d363-38a3-bd89-dd0e3bc82c6c | -17.2423 | -46.90603 | 2026-08-19 04:42:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a49e890f-c5a7-394c-a2e4-00cae9a94409 | -19.74753 | -57.9589 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 491ec0bf-e0cb-3b78-976c-576988716cb0 | -21.52973 | -52.00883 | 2026-08-19 04:42:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 4ede4c2b-6e61-3c8e-9ca0-e69f87fbdf73 | -19.76068 | -57.96183 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2ff9712d-bae4-3892-a258-a3a94825498e | -19.74671 | -57.93982 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ab00626c-966a-3c33-8182-5a5168cefe0d | -17.93918 | -44.42685 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 443bedec-6dc1-3da4-abdb-908fcba729ae | -17.59355 | -44.59895 | 2026-08-19 04:42:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e29c587a-6de2-3773-b1ca-d3efd9897524 | -23.29147 | -46.16552 | 2026-08-19 04:42:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ff71688-a7ca-3d9a-b1f0-3115be9d120e | -19.06089 | -57.35844 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d6d50ac9-87aa-3810-8e82-23ebee838f6d | -16.25202 | -57.65929 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6d502321-b1bd-3ddb-856d-c50583720915 | -20.40989 | -54.6516 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06707770-3170-3c26-b672-4a147e6f3348 | -17.58995 | -44.59983 | 2026-08-19 04:42:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 462d07c2-ce2c-3d56-8227-f7914c9e04af | -21.44456 | -48.51308 | 2026-08-19 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fadfd8f1-fed5-3327-969f-3998c81343a3 | -19.75458 | -57.94629 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 7cdfb107-28ff-343e-bdc8-f2d020775a86 | -20.48536 | -45.24369 | 2026-08-19 04:42:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 21b234c0-39f4-3297-af7c-9ae1bffee3c7 | -17.91912 | -44.34184 | 2026-08-19 04:42:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cfab374-0ff3-3f60-b379-cc5489b3f1ba | -15.87533 | -55.56049 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 806da770-d4cb-3294-a2d7-5e166b8f0ff3 | -19.66565 | -45.90773 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da1f7226-842a-3de3-b481-b6abffcdaebc | -20.19135 | -45.40123 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae9d2038-411b-3ad7-b7dd-153d296089b2 | -20.29403 | -46.46503 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 832d0855-23a9-3932-9dd9-e66cbe9e9509 | -20.29584 | -46.48201 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a2298f7-1573-36e6-afde-372ef6beaf53 | -17.93972 | -44.42269 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7d91c65-8c41-3d65-82ad-240bdf8f549e | -19.73447 | -57.93237 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 207ff8e2-cdc5-3fad-b753-683149e3d480 | -21.53033 | -52.00512 | 2026-08-19 04:42:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| d0441610-4440-30c0-9985-7b5079be78e1 | -20.28141 | -46.4699 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd1fc208-a5c6-365e-b478-0aec99dba191 | -21.04314 | -48.47467 | 2026-08-19 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17f46b25-8a1e-3663-8021-a635dd531b6f | -19.76771 | -57.94923 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 9cc2bac8-db2c-3e6e-a618-b03086fdb71d | -18.6748 | -52.65026 | 2026-08-19 04:42:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df48022f-d816-390a-9b2d-7851ada9818b | -18.81026 | -46.74884 | 2026-08-19 04:42:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a8aaaca-6d27-337c-abdf-96e98524c5fc | -17.32058 | -54.93355 | 2026-08-19 04:42:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a86a2ed6-96f8-32c2-9e80-a691d1dea046 | -19.66916 | -45.91224 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4790d849-6c78-3e84-b282-e06b2e585a55 | -19.07881 | -57.35789 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| db5a29ae-8e7a-3470-9c91-d91c39943fb8 | -20.58002 | -45.93822 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c6f712-3e42-32e5-8915-63f9e69db1dd | -16.26525 | -57.67067 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d75453ea-7443-30ff-97d4-a0eacc3da6a2 | -19.05235 | -57.35657 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 54f4a76e-2125-34d9-8e72-cb1421ff66fb | -21.44753 | -48.51797 | 2026-08-19 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c772edd2-3933-3236-aac4-df8e3756c73d | -22.36599 | -46.90899 | 2026-08-19 04:42:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbb6754e-a9dc-3021-b505-3f42799f8e82 | -15.373 | -58.23091 | 2026-08-19 04:42:00 | NOAA-20 | ARAPUTANGA | MATO GROSSO | Brasil | 5101258 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00e4ef5a-4c89-3e4e-a235-9ae97d85fbd8 | -19.56931 | -49.43539 | 2026-08-19 04:42:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 608cff7c-d21d-34e3-bc61-75f4d13d2f93 | -20.58689 | -45.91647 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e836155e-4d2e-3c31-83ba-c7083575e182 | -15.89527 | -55.54438 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e482802-7dd1-3c52-b0b3-2b2a21f74112 | -20.29005 | -46.46486 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4e8aa31-e2d3-3f76-95fd-903aeaaadc1a | -20.58412 | -45.93857 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cedf007-89e4-3764-826c-918776770cd2 | -19.67014 | -45.90477 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fff1cb7-8720-30ca-a95a-46772ecd10ce | -17.47475 | -48.87234 | 2026-08-19 04:42:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c68c825c-0a92-34bd-8fe4-182fc0902ac5 | -19.75895 | -57.94727 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| b463b095-54e7-3869-bade-c5fb06c6518c | -19.77121 | -57.95473 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| c9746224-4fa1-34db-bf7d-aaf624210c45 | -20.58635 | -45.92082 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04c35014-a9e5-3eda-97bf-f0b73ae65a5b | -20.29978 | -46.48249 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2033d4b-85ba-3ff6-9413-b19abaf6028a | -20.58229 | -45.92005 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40026632-c1b6-3c6a-b036-2dd5381232af | -19.05568 | -57.33956 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c4c5237e-1426-393b-baf6-8e6d49197dc5 | -15.88678 | -55.56662 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3905af79-fc35-3a1f-a758-ec19f0880bc2 | -20.88223 | -45.29566 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 00dd00ef-a3cd-3f42-b7a4-3eb8770b8758 | -19.74233 | -57.93884 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 65f8d0ca-370a-34e4-8661-a59684c480bd | -17.45293 | -47.85924 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178bea77-2c96-3fdd-a453-ab897435a35a | -20.58045 | -45.93474 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78533cb-8b49-3b99-9555-ecb7fdb2532f | -20.60372 | -45.91467 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 376d9c21-2eca-3e70-8af0-e4bbdd4ed8aa | -20.59096 | -45.91714 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 067c3e3b-8a82-3a56-91a3-0699eaa6f1d3 | -18.51273 | -48.18911 | 2026-08-19 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f373d685-3c17-39c0-90fc-15a4d7ed97f2 | -19.75191 | -57.95987 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README47.md)
