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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f834e1d-d500-3204-ad1a-e2311af425cc | -19.88922 | -46.34064 | 2025-09-11 12:00:00 | TERRA_M-T | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7012b037-de3f-38e7-9b8d-92c836ce0f05 | -21.40919 | -45.38662 | 2025-09-11 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0f293a20-71b4-3a19-92a9-3a3c53618e00 | -14.30526 | -45.02004 | 2025-09-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75c28fcc-a049-338a-82a7-5d6516f64060 | -12.68858 | -45.27657 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 8584d65e-7611-39ab-9ff4-f2251bb51b09 | -19.43437 | -44.58125 | 2025-09-11 12:00:00 | TERRA_M-T | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 74b7b6b3-7de2-3466-a43a-5d3480e51154 | -20.08964 | -42.04231 | 2025-09-11 12:00:00 | TERRA_M-T | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 09315616-8a4d-3145-b04b-481620cce8de | -12.84548 | -47.95071 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b5df9c9d-0ad1-3767-8c9c-305f28228038 | -18.6417 | -46.91005 | 2025-09-11 12:00:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6ab35e96-4a51-3b98-9811-8995263b1189 | -22.70593 | -46.33081 | 2025-09-11 12:00:00 | TERRA_M-T | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1fd5e869-d54c-381e-b876-e531dbae202e | -21.65484 | -45.28874 | 2025-09-11 12:00:00 | TERRA_M-T | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| aee8c2fc-c5bb-374b-94ac-51c3522a43df | -14.41549 | -47.32313 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5b26e253-647d-35f3-b60c-46b31b26898f | -19.25335 | -48.00884 | 2025-09-11 12:00:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 50.3 |
| f6fdc34a-07a9-3624-89f9-a372a26b01af | -20.70165 | -41.71392 | 2025-09-11 12:00:00 | TERRA_M-T | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| db2de293-2eb9-3136-a863-27ad762e8f21 | -14.14598 | -45.39993 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 51862b8b-7518-3c54-9de8-ede489d19209 | -20.90739 | -45.28566 | 2025-09-11 12:00:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c6de3d70-df56-3350-913c-bbd62ba7eda3 | -20.93953 | -44.88135 | 2025-09-11 12:00:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| d87fe9d5-c353-3337-a41e-a477fac5fce1 | -17.83905 | -46.72944 | 2025-09-11 12:00:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9fc3f668-6b66-3c13-b1af-99135e6ec08e | -19.10248 | -40.4059 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| dd00aae6-7c11-3958-8d48-045a19bc93c9 | -15.10166 | -48.05404 | 2025-09-11 12:00:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ff2c5721-332f-305d-b08f-c5a8cbd6cbae | -14.13326 | -45.41951 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 1dec29e4-d26c-3d5a-9cc4-0aea6a52e1db | -12.83559 | -47.95739 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 941bb2a4-05ad-3d21-a523-ac84f168242c | -15.75876 | -48.0554 | 2025-09-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 15243826-db77-3ce9-a8d1-fca11ae31bd8 | -16.43417 | -45.68639 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77c62f68-3774-3738-abf0-5155024233fb | -20.71143 | -47.11146 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| d9c92019-7730-32dc-8a43-79688a3162bd | -13.25634 | -51.74627 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f4748162-62ab-39c7-b8de-013c21a41970 | -21.72973 | -46.25743 | 2025-09-11 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9b927d1c-16f6-3be3-93d5-24c9038bd5f3 | -12.67897 | -45.27505 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6290a085-89da-3798-b668-a1cbd5c64aa3 | -14.74634 | -46.29656 | 2025-09-11 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 19f3e6bc-4f34-3fbc-9d26-80c68713aeb7 | -15.68663 | -47.02605 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 312e3a37-f1b3-3f36-9b15-eab8914e3683 | -13.49365 | -51.8033 | 2025-09-11 12:00:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 51cf7581-356d-3fd2-8907-183d8e0f3064 | -20.46535 | -46.38211 | 2025-09-11 12:00:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cd6a089e-59e5-3a83-89a7-18a8ae66f432 | -19.94048 | -43.09589 | 2025-09-11 12:00:00 | TERRA_M-T | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 8c15cd76-fda1-3d5b-8e2d-7395e6443701 | -20.41065 | -42.20359 | 2025-09-11 12:00:00 | TERRA_M-T | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 3f93119d-22a1-322c-b50c-81bc34b536c2 | -21.41811 | -45.38813 | 2025-09-11 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 95129b5a-e41e-3057-97a8-0d1e1c11cfc3 | -19.48525 | -42.32116 | 2025-09-11 12:00:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| a762df22-32d8-3041-bd72-2ba012e777ce | -19.98227 | -47.63062 | 2025-09-11 12:00:00 | TERRA_M-T | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 065d686d-deee-35c7-9061-16dd41567e81 | -18.8455 | -46.85401 | 2025-09-11 12:00:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 44aff4f1-9a83-331a-835e-9bfe24ae43be | -20.44656 | -46.07473 | 2025-09-11 12:00:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4a07319-ee54-3cf1-87dd-96f46e90246e | -15.17114 | -43.40537 | 2025-09-11 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| bba7fce9-eab7-3aac-8e67-0de5dd54ae5b | -21.43958 | -48.9183 | 2025-09-11 12:00:00 | TERRA_M-T | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3aaa7683-72e4-3985-a265-548f59060206 | -13.4229 | -45.90422 | 2025-09-11 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ce818f8a-2058-366d-8c7f-b8e895a1948b | -13.42466 | -45.8928 | 2025-09-11 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| cdca02a0-e70a-3eb5-8849-7bef2e2db2f9 | -15.68862 | -47.01374 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a68bf9b6-fc49-37b3-aa8b-d25a9c9b6e4d | -14.30071 | -45.05031 | 2025-09-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| f92ab858-6535-37dc-bede-22547aa87c5b | -16.635 | -49.7659 | 2025-09-11 12:00:00 | TERRA_M-T | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8a2b76db-f8f8-3636-9915-e80d17349a48 | -15.22679 | -44.0371 | 2025-09-11 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9ed9fe8-4101-36e2-a1ee-bfe5b4c402c9 | -14.38244 | -47.29805 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7403c7b5-e663-3272-b8bc-296ff9a6d7b3 | -12.67569 | -45.29659 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 976d77b3-e8f1-37a8-a553-1e488ccbcf5c | -21.8418 | -46.0673 | 2025-09-11 12:00:00 | TERRA_M-T | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3d7dc8d1-a559-3248-81f8-f4837b70637f | -12.84311 | -47.96502 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 307.2 |
| f587e6af-84c5-307c-88ce-bd13f1a234e5 | -14.13809 | -45.38786 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0bddff3-0745-32ae-ac7d-53347f0eee91 | -17.56679 | -44.55381 | 2025-09-11 12:00:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3e48e737-4ea4-3744-897f-346395322958 | -12.92072 | -47.98239 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1548f659-817f-34ac-8563-10515eb7e731 | -14.13649 | -45.39838 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0d63b3af-ceec-3c43-bf31-da69281ee521 | -16.50753 | -41.41374 | 2025-09-11 12:00:00 | TERRA_M-T | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b8ca1d11-1a03-3d13-81f4-5a56f8e5291d | -21.67828 | -46.46828 | 2025-09-11 12:00:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b5f563eb-7905-3f5f-99ed-ae451d19291f | -20.46376 | -46.39243 | 2025-09-11 12:00:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6f922892-acdc-39dd-99ca-0bbf59289df9 | -14.14438 | -45.41048 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6318f7d9-d29b-33e9-9cce-f5d691f57d09 | -15.10539 | -48.102 | 2025-09-11 12:00:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d64a1f36-4240-35e9-bc33-369a5e1de784 | -13.04332 | -48.01418 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 66e452db-8fd0-34ef-a125-df3d33837f6c | -19.16852 | -40.78106 | 2025-09-11 12:00:00 | TERRA_M-T | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 5ae69696-d274-3d99-ab57-3d0a30ff7939 | -20.44814 | -46.06454 | 2025-09-11 12:00:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2ba1dd3a-c6a2-3aa1-ab62-ebffc165096c | -17.25956 | -46.0952 | 2025-09-11 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 228ba300-673b-3760-9958-5d5a03372790 | -14.74813 | -46.28503 | 2025-09-11 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 576901be-1e87-38d4-992d-42d0d534c172 | -13.97362 | -48.03917 | 2025-09-11 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| db4dc8ac-8ab1-3ecf-9b5d-ae4f73762149 | -20.15518 | -41.03428 | 2025-09-11 12:00:00 | TERRA_M-T | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| affdbfd1-73c9-33c3-b768-e1918320b645 | -19.2512 | -48.02193 | 2025-09-11 12:00:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| d298a68b-20df-3721-9e0f-ceb3f2ed5c69 | -12.53614 | -45.34647 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| bed04aea-7aa5-3377-ba95-0a824dfc5784 | -20.00133 | -47.6401 | 2025-09-11 12:00:00 | TERRA_M-T | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1298a1d6-c7fa-345c-adfb-3f59352dd252 | -21.32517 | -45.02372 | 2025-09-11 12:00:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| b66d0d89-0b1f-3d49-83a8-6c3b81d3d6f1 | -13.84424 | -47.35903 | 2025-09-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4b262c01-a47b-33d6-98b7-e42d902286d3 | -21.05357 | -46.79345 | 2025-09-11 12:00:00 | TERRA_M-T | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cc0d94ef-d802-3f04-a18e-81aec4f70e9f | -19.38666 | -44.41071 | 2025-09-11 12:00:00 | TERRA_M-T | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 374c2170-8957-37b8-9721-3d4d19ea121d | -14.14277 | -45.42103 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e78a3905-b559-3b47-9611-26ac4733c154 | -18.00774 | -44.44348 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 76af5363-4c74-3e72-b60b-8f0c0f0e2303 | -21.11195 | -45.08721 | 2025-09-11 12:00:00 | TERRA_M-T | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c87e65a7-c2d8-3483-8a29-5d12ec6a97f5 | -15.6846 | -47.03853 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 67cc2b8f-6cc9-3087-b596-3f7d889d40ff | -14.13488 | -45.40894 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7a846d0c-c992-32c0-bdef-f6fb040961b1 | -15.66199 | -47.04756 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bbffb7ce-bda0-3eb3-91a9-f6b6b6a1fca0 | -13.30366 | -43.75574 | 2025-09-11 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca6e15eb-4680-32ac-b60c-f54a56b9864d | -20.09102 | -42.03157 | 2025-09-11 12:00:00 | TERRA_M-T | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 10a8512e-ae83-3795-b009-ab2071f5c7ff | -13.28215 | -51.71231 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| e96ab3ea-6389-33ff-82db-f46336215979 | -14.40188 | -47.31414 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b91a2aa6-f0f4-39e0-94ae-a1b4e488b1ef | -20.07725 | -41.24301 | 2025-09-11 12:00:00 | TERRA_M-T | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ec4589f7-df57-340b-8bec-519c3df496a3 | -12.68695 | -45.28733 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b78aa395-8df1-3079-90f5-8eb463d7ce7d | -18.35008 | -49.32384 | 2025-09-11 12:00:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1be002c0-cf4b-32d2-abc1-a0af3aa0ec80 | -18.78971 | -42.0258 | 2025-09-11 12:00:00 | TERRA_M-T | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 2853b5a6-79fa-397f-8c9a-17f2d63cc498 | -17.93837 | -44.47408 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d118da81-f150-3c7d-b546-7cad3a0a992c | -15.76151 | -48.04728 | 2025-09-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b08f0c64-14e8-3283-8a20-b83c98820a3a | -12.61644 | -45.68389 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 502.0 |
| 4dff1070-cc1b-342f-a02d-d46348cbf11c | -18.3782 | -43.98756 | 2025-09-11 12:00:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f1e80235-8ffc-3266-8189-97f7262fbb2d | -22.7941 | -45.6231 | 2025-09-11 12:00:00 | TERRA_M-T | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 616bf4e3-41d4-3765-bdf2-7268f223e7e8 | -19.9665 | -44.15094 | 2025-09-11 12:00:00 | TERRA_M-T | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a2a4faf4-574b-3f1f-ac82-751a369f0ba7 | -15.22541 | -44.04639 | 2025-09-11 12:00:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 54b41e24-5d10-3892-bc10-648c5e2ca561 | -20.74313 | -46.54119 | 2025-09-11 12:00:00 | TERRA_M-T | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 28b40ef6-9cb6-3c19-9602-758e1ef45c03 | -21.72584 | -46.93608 | 2025-09-11 12:00:00 | TERRA_M-T | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 67a3cafc-cccb-3ab9-a2d0-14c086e7d327 | -13.27738 | -51.71864 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.2 |
| a71206a7-51cb-305c-a221-7a3e5cc5e324 | -18.63196 | -46.90836 | 2025-09-11 12:00:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 66e96156-93eb-31c2-97bc-45fcafdcc099 | -19.90876 | -44.23759 | 2025-09-11 12:00:00 | TERRA_M-T | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e1da594d-cee0-35c2-9bff-62faa95791ff | -20.84547 | -44.95656 | 2025-09-11 12:00:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |


[Clique aqui para ver as próximas entradas](README136.md)
