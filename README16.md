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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdec38a3-2e47-30ae-9526-3809567b08ee | -18.64536 | -53.31426 | 2025-05-24 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45179fa6-96d0-3f6a-a3c6-df4e6a79c60d | -21.60019 | -56.04182 | 2025-05-24 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 502d237d-3c21-3f99-8246-28d162587593 | -18.36132 | -55.17742 | 2025-05-24 05:01:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 96346c0f-12a9-3f36-a1b0-a100c497a1e6 | -20.94515 | -56.58814 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7a30de9f-3eb7-3c11-b984-1a65cab0c54a | -21.22139 | -48.61528 | 2025-05-24 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 63710bee-3f4d-30fc-aba6-6c710d9f011c | -20.60962 | -55.7053 | 2025-05-24 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fbdacbf-a656-3d33-b40b-18fd2db78815 | -20.94403 | -56.59562 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4a2556e-4915-3855-a6a2-d9ad4bae283c | -20.94792 | -56.59245 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4831d6e8-a0ac-344e-9314-561876df81ce | -21.60301 | -56.04628 | 2025-05-24 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3005390e-677e-3df1-b2a8-1cd8054790ba | -20.99582 | -51.79178 | 2025-05-24 05:01:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b48c86c-61aa-343e-be4e-1b8548e8e585 | -20.94181 | -56.58757 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8cc78596-11de-3907-9f69-d5e6879f6077 | -20.85399 | -53.74783 | 2025-05-24 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbe85208-104e-33c7-950c-cb7f496cec4d | -20.94069 | -56.59505 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 76924de0-44d7-342f-99b3-7ddefa1452be | -18.35849 | -55.17303 | 2025-05-24 05:01:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9d0d141f-9648-38e8-88b5-22e914dc013f | -21.6064 | -56.04686 | 2025-05-24 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7530fde-c481-3a85-8266-5d77dd0c79be | -21.96289 | -56.0789 | 2025-05-24 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0361e16a-52ce-3b60-bf4a-9931504e29d1 | -20.63968 | -55.71414 | 2025-05-24 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb7dcf67-6d4a-3fae-bd7a-d6d0e8eccd01 | -21.48053 | -57.11395 | 2025-05-24 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1baed931-a194-39e0-bd9c-cec42dba3e83 | -19.87308 | -54.3694 | 2025-05-24 05:01:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bb9273e-820a-3619-b255-885223520f19 | -19.10475 | -54.43914 | 2025-05-24 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27ea1949-b1f5-3e4e-be2e-9d08310c4f2c | -23.61413 | -49.00793 | 2025-05-24 05:01:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47675aab-6490-3548-be91-9e292fb18cec | -21.85827 | -56.38433 | 2025-05-24 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ebfeeb-cc78-3282-98fb-7eaf8e84c9d3 | -21.60358 | -56.0424 | 2025-05-24 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 641d64a9-a598-3975-b90f-42b2068c4f33 | -18.64167 | -53.3137 | 2025-05-24 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984150da-f2ed-3222-8c2e-e602630f639e | -18.59661 | -46.55182 | 2025-05-24 05:01:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c90204c4-c073-3ab9-a92a-82b0a0ed0d44 | -19.79783 | -53.83349 | 2025-05-24 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3104828a-d1e9-3bf6-b2f5-17c03d98a710 | -21.21658 | -48.61145 | 2025-05-24 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f884bfd-0846-3f2a-90a0-a616a17481f9 | -19.30277 | -55.00986 | 2025-05-24 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c30988a9-4faf-319b-8a80-216dfd2a2353 | -21.89668 | -56.26431 | 2025-05-24 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50249abc-3847-327f-940e-c4ddb12ff760 | -24.24299 | -50.74015 | 2025-05-24 05:01:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f2685a0f-d22f-3a79-825d-fadc5ac105a8 | -21.48109 | -57.11023 | 2025-05-24 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf88e75a-b130-31b5-b2be-8211bbe8ab5a | -20.94736 | -56.59619 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16bfa2bd-de49-396d-8326-9407f2a92bde | -19.88077 | -54.36637 | 2025-05-24 05:01:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19745f83-4c87-351a-8e5e-9a1ebafdd69b | -20.28093 | -50.74855 | 2025-05-24 05:01:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a86bb169-ec63-3aac-88f2-f8ec246e8e89 | -8.07 | -43.1216 | 2025-05-24 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 1a871142-f66e-3b35-8f6f-85fc80c88694 | -8.0889 | -43.1196 | 2025-05-24 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 4ae51ca7-ce72-30fc-9d02-c4ea1b240d9e | -8.07 | -43.1216 | 2025-05-24 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 83128934-0f9d-300e-8859-f186deaccdc9 | -8.75215 | -48.04196 | 2025-05-24 05:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75d0143f-f59a-3fe4-b6a5-376ab05a463e | -8.75291 | -48.03574 | 2025-05-24 05:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee64b954-789c-334f-b200-fdd82f84b651 | -10.02109 | -65.00548 | 2025-05-24 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff3dcf2-c77e-3280-a763-c337823dbd2b | -10.53461 | -55.72044 | 2025-05-24 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b39bf57-2a09-311f-9cab-0fe1a37a4bab | -9.92879 | -59.93046 | 2025-05-24 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfea605c-ac69-3115-9fe3-84c18605fdc7 | -4.28708 | -48.27201 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc77afbf-fa05-3e3a-b06c-b5f560c1e761 | -11.99175 | -57.21149 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fadc6346-d61a-3dff-ae1b-c800e6bd687c | -11.75838 | -54.22569 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7baa558-8fac-34d5-853f-e79db9923224 | -11.35571 | -55.13497 | 2025-05-24 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fda0123-1d5c-3219-a8fd-25268c0857fc | -9.99245 | -55.90988 | 2025-05-24 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e14f41bb-5157-3bd2-87ab-c36de8b94663 | -10.36897 | -57.50374 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5c80ed8-a6f8-3b53-b136-a1c458e8dcfd | -13.85447 | -59.72426 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a920877b-eb3f-314d-b90b-15be8293c738 | -11.42757 | -54.30351 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47bd2721-cd6e-3478-9072-baad4fd7be2b | -13.15584 | -56.81898 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c3a0e48-6ef7-3a0e-a76f-7b9daac426ff | -13.82626 | -59.69521 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af48fa03-692d-3ce4-bf68-4e4b60e253f8 | -13.97611 | -56.02197 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43624a8a-b3f3-315a-88f7-10334e9b481e | -13.78101 | -54.3049 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a159c7c-c053-384b-bf14-c566cbbe39dc | -10.37106 | -47.98775 | 2025-05-24 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f267732-f86b-335a-a43d-23c5ba943449 | -13.8428 | -59.65633 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f92e781-f9a1-339a-b325-22cd0cd43534 | -11.76255 | -54.22745 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0c8b2898-c1c2-31ed-8018-724336b15bbc | -11.3608 | -55.13113 | 2025-05-24 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a507676-5458-344c-918b-e0ed47416972 | -14.06923 | -57.10806 | 2025-05-24 05:25:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e2e96e1-6594-3c49-9a12-a77b63eb2ca0 | -11.42266 | -54.30401 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea2402ed-ee63-3442-b62d-9b03370c394d | -11.42283 | -54.30279 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b19cc869-0b6a-3380-a4cb-32307f71e01d | -13.15173 | -56.81837 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f25739db-1ee9-3400-acaf-3e4df19c14b9 | -13.86034 | -59.73335 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4178f185-044a-36bc-bfac-f7fe69b84225 | -12.14592 | -55.30698 | 2025-05-24 05:25:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f30041f-f869-3d7f-a954-aa90dcfe02a9 | -12.39347 | -49.97791 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc62ae6b-e75b-31af-9449-7afa4ecdfa17 | -11.75226 | -54.23152 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e9af741-c113-364d-bdf7-5ba0badf6cbf | -12.38586 | -49.9874 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9c9b133-2ed2-3533-be6e-ffbfc652ba7a | -12.10419 | -64.05818 | 2025-05-24 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4400ce13-e3b6-3382-8f68-0c33e77e9ec7 | -9.23882 | -63.28685 | 2025-05-24 05:25:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd9b8e3-8af9-3124-8937-d9b2e35f97c2 | -13.14401 | -56.81345 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9edb57af-afbe-30ca-ba6e-c80af02a54a7 | -9.493 | -63.33929 | 2025-05-24 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0760ed16-bbe9-388a-bd7b-9631c366054f | -10.76711 | -55.26457 | 2025-05-24 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca6c1856-1fba-31fe-a2a9-fd528f1a7d44 | -10.72318 | -52.47337 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dde41697-effb-3373-aca7-61d8d2df22ea | -13.37137 | -54.2635 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6e9b0b6b-d0b6-36b3-870e-84c856b408c0 | -12.37949 | -49.98644 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a271e5d-1210-3821-838f-4001159f8e0a | -14.01777 | -55.14143 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10d2e75d-c4e9-3517-8c5b-fb527e35c98f | -8.98473 | -63.88591 | 2025-05-24 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d2f32d5-c717-3f28-b16a-f3866dd2b1aa | -13.83277 | -59.65071 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d88ce5f0-530e-387b-9239-a362fe74e1bd | -12.37371 | -49.98859 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12df5714-95e8-38b7-b16c-abdb582d5c0e | -12.35297 | -49.93562 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6a70069-ade1-341c-8a75-3695d46a5ce5 | -13.47136 | -52.27896 | 2025-05-24 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3781c455-867a-37ce-9484-f574d529aaf0 | -11.29543 | -53.97842 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936189ed-a112-367b-9f5e-f723c3dda6d7 | -12.37889 | -49.99156 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83fe080d-2d11-3c36-9365-4d25673f3848 | -13.85741 | -59.7288 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b7a06f-9081-36b4-bc01-aee10ec3d86e | -11.74805 | -54.22974 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dccd0bd5-6927-3ded-aee2-04d9d5b2209e | -9.41609 | -58.30082 | 2025-05-24 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1f1b7f0-a465-3bf8-a1df-921530d785f7 | -12.3998 | -49.98711 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c3d5863-87f0-321e-9a8a-b766fa2c938c | -13.47479 | -52.28332 | 2025-05-24 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 941641d6-becb-3282-91af-310ba1b7c960 | -13.18873 | -53.57863 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06a82786-fa66-3393-942b-9b76b6fc3d2f | -10.7236 | -52.47 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ae509fc-5195-362c-b05b-5d6b6e026e05 | -10.68157 | -57.60485 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2af14788-7172-39f7-948e-8694217ac486 | -4.28639 | -48.27694 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 235fe3c3-9c90-3d87-bbcb-ea7aa0242566 | -12.38008 | -49.98951 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfdbaca8-b95c-36d7-b57e-2cecc48e03af | -10.36518 | -57.50317 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 528b999c-2590-3743-93c3-eb61e004c7c5 | -12.38066 | -49.98434 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7e1217a-a508-33b1-af37-18d2080635f0 | -10.68224 | -57.60017 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fded0ae-e0f6-3f2d-aa4a-42fdb2bb1fc5 | -12.67322 | -58.21721 | 2025-05-24 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecd2fc3e-9e13-34ab-a1b3-eecff43f4ab0 | -12.39987 | -49.97865 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6624582-6063-3419-8535-1a802eb715c6 | -14.06513 | -57.10754 | 2025-05-24 05:25:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 921f0f83-a777-361b-9fab-798edd8bf675 | -13.14914 | -56.80649 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README17.md)
