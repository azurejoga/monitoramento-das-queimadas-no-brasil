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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e6ee757-6d09-30e3-a41a-12cf8de6fc29 | -9.05468 | -50.49194 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a099690b-dede-3372-bf05-adb2db7745e5 | -15.79643 | -52.25211 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a9cdaea-54d8-3a74-96db-09ba007b55b6 | -12.03873 | -47.5428 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6640749a-57ea-399a-89d9-41b759e3b769 | -14.35393 | -53.07659 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2706909a-9ba1-3d3d-bd22-d0ae74ad5a0a | -11.99656 | -47.59267 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a33658f5-5cb5-3e67-b832-8ee614ed17c7 | -11.80676 | -46.75655 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85291a94-410f-3001-b8f4-97fd37ce84f7 | -14.50429 | -53.94043 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f44cc6f-59d2-38c4-856f-7a6503ad71ed | -10.00293 | -51.72648 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b63828d6-714b-3c62-b418-8a0352058909 | -10.00072 | -51.71898 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e13ac07e-9261-3710-b033-2c42da4246b4 | -11.48327 | -43.69285 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39d78d79-ab30-335d-b634-d2579c4c7415 | -9.89323 | -51.8842 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 871d3b44-5b49-3f71-8383-9e181e1c2625 | -15.97911 | -42.98475 | 2025-09-11 04:46:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b51924b-ff22-3daa-959f-6e3dc41d013e | -8.6366 | -53.11214 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c49b2eb9-5910-3150-bcc9-ba475e73fe8b | -11.48796 | -43.67129 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46df997e-3e24-35c7-a8eb-6b85912c72e2 | -9.05749 | -50.49601 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6da3fe37-e7a3-3b18-86f6-81943996c348 | -11.71963 | -50.62607 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| b2e6804d-5de1-31bd-9a10-6f8e70e340a2 | -10.47396 | -51.86302 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb35c813-d841-3e0a-bc19-59d46e5d87df | -11.49022 | -43.67853 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b0a34b4-8c1d-3828-90e1-f58cd006a2ed | -12.23959 | -47.31093 | 2025-09-11 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f65b14a-9d05-3eae-98a3-c071b8008d5a | -9.52003 | -54.64325 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| caf23145-4f3c-34eb-aaf4-25d470d38976 | -9.07199 | -50.49096 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dc2dd4f-45ad-32c5-b095-100501d7a6f8 | -11.41043 | -43.54631 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11469496-a0c6-31bb-b5e4-970e0f444e32 | -10.40778 | -50.52288 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 799e11d8-8426-36bb-a863-72efffd3b1f4 | -12.9233 | -54.7836 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 710c235b-7da9-3660-848a-e1ddab497246 | -15.82054 | -52.22265 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91d9b899-a160-350b-8d4c-f73c161d647b | -9.10361 | -49.85223 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9999907-23f7-3a0b-8d4d-da14c301779c | -10.39148 | -50.51661 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 995fc107-158d-3774-b3ea-17f78e6df536 | -11.48326 | -43.66761 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 781cb497-6e4d-3077-8676-b9cd32278189 | -11.63071 | -46.76283 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbd973b6-755b-3175-84c8-c62ee474d490 | -15.8022 | -52.23065 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 892e612a-cd6d-31df-9763-2d7428abd36c | -13.27349 | -51.73439 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43bf6fd0-568e-37b0-a30e-50c06a81bd74 | -13.67242 | -44.2223 | 2025-09-11 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a01da5-5707-398c-bbf1-cfacf0078161 | -11.48955 | -43.65921 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77148ce5-6105-3d36-a11f-056536c517fb | -9.72164 | -48.08872 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f02b3db-a455-35ad-853e-b46ed723f834 | -11.15911 | -45.31296 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23130977-585e-36d3-b99f-ccb288bd747d | -15.10238 | -50.06536 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 544467f4-e6df-3741-8262-ec65f8fa61ce | -13.34884 | -44.00225 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfcb0852-f9bc-3aca-b590-6d72f2074e6c | -10.30826 | -48.79773 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 01ed7591-62ac-35fd-ab00-3669a73365c1 | -9.89048 | -51.88018 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d819e4f-2932-39e5-b5e9-5f1e3202747c | -9.05414 | -50.49545 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c14a68a9-db92-35bb-9363-6dd89c73f30e | -15.20065 | -44.04523 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0bd8013-0905-3bd1-a72b-a20a92ef785c | -11.37253 | -45.57801 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4ad2f77-f454-3382-b03b-dec46dcc1b39 | -13.24355 | -51.77781 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eb8f0bb-edaa-3fe5-a13c-903d407b0f79 | -10.00348 | -51.723 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f057807a-0232-3c2a-bae4-1e6a74fb52f8 | -9.56467 | -48.29842 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45de6e7b-07a2-36ba-b25f-a2068c861bc5 | -9.01594 | -49.76265 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c8f4c076-c287-31ef-a9b7-713e5eaee544 | -11.08656 | -51.33003 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f8fdfad8-d083-33df-ac06-5b5e580495dc | -11.7988 | -50.58537 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a396d95b-e01a-3864-a591-17067058a751 | -11.49195 | -43.641 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbda1e8f-230e-3054-beb1-30e28fe254fb | -9.71852 | -43.52065 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd89c97-5c8e-3e82-8f26-2823e7d8d6df | -13.13131 | -54.92649 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6749fb6-09dd-3afb-ad3b-61bfc69c6ab9 | -11.10748 | -48.41116 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0183cc73-ed57-3dc5-9473-ab8f12f6a86e | -13.13609 | -54.91924 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f2cf807-70fb-359b-b765-4184d899da55 | -9.02619 | -49.76423 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19d82353-29ad-34d7-b874-505a1f0ec67e | -11.47347 | -43.62352 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5accef99-3d81-364a-b64c-7bded4f73511 | -12.12844 | -44.86679 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aa8ac2c-682f-3d06-b5db-71543801a725 | -15.12963 | -52.41469 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a77d4f9-a1a2-3a43-98b6-639419093da9 | -14.78695 | -48.24357 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef4beefc-482f-361e-aac3-727f13176bf2 | -11.97122 | -51.11307 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c216608-a3d9-3fe2-907d-2ce2058ae818 | -15.14236 | -52.44263 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28688165-ff2b-38a3-93c7-2ab2ba065956 | -11.45221 | -43.5868 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f5996f7-8a9d-3aad-b8e2-ae39c1fdc081 | -12.0336 | -47.60999 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0709fbcc-eb54-38b3-9df9-c62edea9d360 | -12.9671 | -54.75537 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c35e08f4-7d91-3420-8edb-91190542b6af | -15.56806 | -54.75227 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 338e1dee-4035-3f80-abbf-6b35a2cab997 | -12.47002 | -53.82796 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a81bae-b2d1-349d-8f32-bfb66ed0174b | -12.96493 | -54.74706 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc89c93e-6a80-34fd-9248-75c6ad5ec0f3 | -11.50392 | -50.38408 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36de5aa6-fbf4-38be-ba9e-177577f4af6f | -15.79942 | -52.24887 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3c929d3-d74f-311f-8065-449ce65687d2 | -11.22227 | -54.99821 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a47aafd7-7145-3362-9f93-879077a52a84 | -12.84349 | -47.96484 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba197f7f-4c23-3e6e-bd47-10c7834f4707 | -12.9763 | -48.04791 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1011fb7f-51c6-3f3d-a0c1-4cf5215dc390 | -11.47034 | -43.64753 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18836c10-625c-3a3d-bfdd-82ed862fa8bf | -11.44237 | -43.5823 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63085c40-933b-320e-8057-7e3a372ce7ab | -15.47806 | -49.35981 | 2025-09-11 04:46:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d504caa-c590-3609-aea1-1c4e0328ec45 | -9.30362 | -46.76395 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14a86630-e37f-3f81-a2c3-578ff3178d35 | -12.51338 | -53.80529 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b678f5ae-2954-30e0-938c-588d0c848056 | -10.27454 | -48.82673 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c6c7148-7c0b-3dbe-a8e9-a270401d1849 | -14.92296 | -55.93885 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9566eb67-5ead-3b48-a489-400b45d42991 | -11.38912 | -43.52934 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e27016-9086-30b1-86a1-a536b5b5e284 | -11.72191 | -50.634 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| dfbb87b3-a4c0-3f91-9614-a049c3599b34 | -12.27347 | -53.9128 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ea994b-5e4b-3ae2-b991-a43d8be5307f | -9.05522 | -50.48843 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fc93adf-4eff-3751-96ef-6a401af919ea | -11.36039 | -46.56115 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6ab541f9-69e2-3346-80cc-2bb637e3e6d7 | -8.09045 | -54.74572 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfc45743-e534-318a-be7a-6f828c1092e0 | -16.29657 | -50.0605 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87e06e81-b734-3a24-94ef-819f6c8e3dae | -9.71886 | -48.34001 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05c901ce-dc34-3d46-ad62-22a9b9b6b47d | -15.59347 | -49.38917 | 2025-09-11 04:46:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e09ebdb-77bd-32a0-956e-971b0cbf311e | -9.02277 | -49.7637 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2ca46fe0-ae71-34da-ade3-92f255cfae58 | -14.88607 | -55.8766 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bb95edc7-48df-3314-b055-8a5cc4bbd712 | -14.52059 | -53.92454 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6263bfd-6740-304c-b06f-5bdbd4d08c50 | -15.11245 | -50.14651 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e6b98b-c078-3298-b0d1-9a548cff56e4 | -11.65751 | -46.90385 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d645c8f4-9652-3e5b-b2ba-85f28ef61796 | -15.11842 | -52.4017 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5cdb65a1-905c-35b6-ad3d-128634bd612e | -13.26022 | -51.75845 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b83368f7-0d93-3556-9ab8-5d6b44b10af0 | -11.46521 | -43.60703 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bbf7d0aa-5855-375b-88c0-ff782dc899f6 | -10.5694 | -52.03252 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d4d25de-c3ae-32e6-865e-df48ddfa2b60 | -10.31476 | -48.80354 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a620631-c7da-3f48-b59b-e81b1ddaf9aa | -13.64786 | -45.69962 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7dc33db-a21c-368d-8b17-0d75f65d8784 | -9.30312 | -46.76742 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c3ec33-0998-3b86-91ed-90f2c122321c | -9.07918 | -49.80667 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README102.md)
