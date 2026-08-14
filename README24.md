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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa6c0c1c-d096-3352-9768-5315217b66d7 | -12.02589 | -46.41106 | 2026-08-14 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7333abd-d2f8-3e4a-9200-774321f690a4 | -14.47151 | -45.67886 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 404e0939-1526-3dbb-92d3-28fcd65b4fa8 | -14.30463 | -51.97016 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea9ffb48-d720-3f6e-a648-c99088dde656 | -14.7227 | -52.88859 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f56e8db-b801-3dea-90dc-b1ab16f9fd3d | -15.10073 | -50.43392 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68ef9fb4-c52c-349a-82d5-c94ba5a610d2 | -13.28478 | -54.22579 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcbfe415-98e9-350c-86dd-5c61066d89dc | -15.5171 | -52.99851 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d9f9970-e6db-330c-9701-bc7c7bae38da | -11.59341 | -54.67917 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7996f46b-8f8a-329c-b1ae-a10af0f9d982 | -14.71412 | -52.89194 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34bc1267-a7a5-397d-82db-595e7ac147e3 | -11.06505 | -50.94299 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ab39fc1-74cb-3792-a039-170f24c01cd5 | -14.71973 | -52.88293 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 736183ec-0a5e-3694-a08c-7dac7d8f47c4 | -14.47678 | -45.69204 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adfca9f4-5025-3883-b7fa-be5a80ded403 | -13.89849 | -53.84963 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d33f57e-5575-38fa-9af7-b9ee049f0bba | -11.47455 | -44.55786 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 527b103d-fcc8-3f91-935b-8246c53e43ad | -13.68186 | -46.2715 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a77a44a8-47c4-3d23-8a9f-f0236eb881bd | -13.92031 | -53.96592 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 947f8dfe-234f-3fe3-8000-9205c740c703 | -14.44102 | -51.87159 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1943369c-3377-3260-be49-d63d23a5a7e5 | -15.17058 | -50.05293 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c63a0c0-1e30-31db-a33b-fbf2e3172584 | -10.82123 | -50.32363 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd468d7d-78a7-34c0-acb6-b1b7f2d733ef | -16.90965 | -54.15313 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea338505-49fc-3264-9aa8-f90dc5d97c3a | -13.81265 | -53.81714 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d6d20c3-5fe2-3114-b386-eb24d7cc5290 | -12.34838 | -53.14393 | 2026-08-14 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b674f1ad-7452-32f7-9201-6e3d8a9289c4 | -14.32263 | -51.98896 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 264ed107-467f-3e82-87b7-c2f5fb8d007a | -14.47737 | -45.68801 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18ba5e76-7d5d-36ef-992d-2d16da45d07e | -14.94155 | -46.61783 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6737cdcb-b344-3264-b45d-57041f463f9d | -14.4803 | -45.69259 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3122e17a-a956-3eba-9ee8-c34e8ed0a985 | -15.14093 | -41.56171 | 2026-08-14 04:34:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c64d7bff-79af-34e2-b6d3-ec77422b23a7 | -10.96912 | -50.54052 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ef3a6e9-b8ef-3034-ac76-ae2276f37e36 | -14.43262 | -51.85784 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb391636-ea36-3d03-84bd-a30fcb02f851 | -13.56553 | -46.25358 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4fe75ce5-146a-3736-88a3-3e6c275e0afa | -13.55927 | -46.24879 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9fa7a666-c8f2-3cc5-8ce6-4dcd4541c732 | -12.03294 | -47.82323 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53a23bd7-7666-3370-a454-4306ff0f540f | -15.09604 | -50.44098 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4292425d-073f-3f43-a1de-609d6e58ad0e | -14.45513 | -45.69281 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb1f1ff9-93a2-372b-a5fa-16f0f05cd190 | -13.87822 | -53.76186 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58908522-eb4c-3c80-944d-d17cbb22ce47 | -13.67725 | -46.2557 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 329fbdba-f958-3959-b2f5-077017bf236f | -13.75542 | -53.41826 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dac1fef2-c6b2-3bb2-a9a2-cab24330c973 | -10.70116 | -50.4769 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3332633a-8622-32ee-ae14-48e65eb535dd | -14.44285 | -51.86426 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab010b3-56c3-362b-96e2-44b4954669b4 | -11.49327 | -54.63257 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbce1346-5659-34c2-aa7f-8e1077b35d9a | -14.35412 | -53.69449 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a3c653d-4065-3f82-a369-cfd6a7dd72d1 | -13.6494 | -46.25505 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5681b379-00bd-342e-9564-de0e479c00a9 | -14.71797 | -52.89272 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aed3e958-a1cf-3710-a126-1c28e83e04ce | -18.42203 | -45.19272 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a2f6a28-0a8e-37fe-a649-9ab6f160b582 | -8.8879 | -60.56045 | 2026-08-14 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c23e1682-ba84-3334-9e68-270a30507106 | -14.94778 | -46.62276 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff52e90b-77e7-304d-84cd-ef8af6c9fe3e | -14.94382 | -46.62591 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cce9819c-cbe9-3b2d-af20-3a9a1c9dc5bd | -12.73083 | -48.4337 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9a531eb-ae1b-35b8-aba7-cffd875cf63c | -9.9838 | -53.95066 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d6c462f3-953d-3966-a4ad-6d1baa38be7d | -14.97 | -46.61434 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f006c365-45c3-30e2-91a3-2a7c1ad14004 | -11.99868 | -53.45483 | 2026-08-14 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 266a82fb-5286-33a9-be97-41cf27f34636 | -13.679 | -46.26727 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8abea43-fb23-3201-bd2e-d65da14a4038 | -12.76006 | -44.55333 | 2026-08-14 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 227de9e6-2b82-3cdd-b4f4-4e21540a17e7 | -14.05535 | -53.61043 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3d6bda33-cedc-3892-ac51-e8b48e42123d | -14.72092 | -52.89847 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9b287bc-d5ee-340f-8161-63b871f9e2f3 | -12.51653 | -55.79324 | 2026-08-14 04:34:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac4245a6-cd91-3144-b0c9-e81660470ac3 | -14.97533 | -46.60309 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5e1e7ab-d53c-3125-8eba-3d356b01141d | -14.4539 | -45.6979 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cbad83c-4722-34d7-8e68-8aaef9fc0d27 | -18.16526 | -43.98214 | 2026-08-14 04:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f2df991-8c9b-3045-8ebc-0e3791cccf40 | -12.00969 | -46.40439 | 2026-08-14 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cc8f28a-d094-3667-a559-be69cd52a866 | -13.59685 | -46.23135 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89c3d4da-e400-3586-8aab-d151eefc7ce8 | -14.08522 | -53.63165 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bae0814-b4b2-383b-959a-2027336a2a18 | -14.45396 | -45.70088 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46bbe9e1-fd0c-350e-b08c-568404a69fa8 | -11.48083 | -45.09354 | 2026-08-14 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c34767e-0ddb-3153-82db-feffa13b6722 | -13.75812 | -53.42645 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a96aa7a1-111c-3d23-b056-5d97bad34d7b | -13.25046 | -54.20789 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9d03178-a920-315b-bd53-10ae957a6166 | -11.49846 | -54.60426 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3f7b468-cea4-32f3-81f6-6c7229da3dd5 | -14.47093 | -45.6829 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45ceab0c-ef7d-3833-ba93-835a472a8e70 | -9.97167 | -53.96681 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 640bc304-0519-3547-8dc7-1a66810b07c5 | -16.54391 | -39.66645 | 2026-08-14 04:34:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b4104452-7b02-3abc-8169-789f1a702235 | -14.24017 | -45.40988 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28c3f102-2706-3309-ac16-a604c94e315e | -11.86975 | -51.93873 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff707e3-1439-38bf-b675-e0ff843e7e5d | -13.28125 | -54.22087 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1d746cf-acd5-306b-9449-11b23bb16e2d | -13.82454 | -53.79891 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47cfb470-0793-3f44-9b1e-d464605a83fd | -14.71885 | -52.88779 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaf19de0-a7c0-302d-ad27-053c7f4d8733 | -11.79859 | -51.87918 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bb61d23-fc86-3d4b-beed-ef298d9fa927 | -14.4426 | -51.86269 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5d54ed4-4461-340b-a46a-e0979e84e05d | -18.89279 | -43.76223 | 2026-08-14 04:34:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 982ea588-0eca-39cb-9c9d-65224583873a | -14.29415 | -45.26569 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 653f769f-efb5-334a-a846-8d163ade80bf | -14.36268 | -53.02751 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7061f4-1dbe-3d45-ad2c-b65089d550b3 | -14.19771 | -46.21272 | 2026-08-14 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3f1552d-011e-3040-8527-214a19acf5e6 | -12.02026 | -47.81755 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1354ff72-3576-3ed8-94fe-73c8d1b12683 | -14.46333 | -51.91682 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3060a527-8531-376a-9c83-261840c7802a | -15.63316 | -48.89606 | 2026-08-14 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d359dbd-d113-3922-a762-4d74f7a76e5b | -14.44626 | -51.86335 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65aa3d7b-5371-3615-8bd4-a09c43a4d8a5 | -12.49515 | -43.77363 | 2026-08-14 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 092175f1-6736-3cc5-b2cd-f6a87a3d5390 | -11.31394 | -45.22123 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 863030e1-c87e-3660-86dd-be5c968d31e8 | -15.16382 | -50.05175 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7535b1a2-c2de-33dd-969c-aad77389cb04 | -14.44133 | -51.87317 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e812b9-fc9c-3526-933c-578e0ed919a5 | -14.95121 | -46.62317 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12096efd-063d-3b37-9718-8da6d337b2c0 | -14.44748 | -45.69279 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb391adb-ed58-3b8a-bcd2-bb147f863f66 | -13.23559 | -54.2657 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e137bf73-edf4-3bc4-a201-623985e8c51b | -13.38897 | -42.38478 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a115cdb0-6065-32a3-a10c-0953eec543a6 | -14.3271 | -51.98522 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b58a88-2b2a-326c-abbe-fdf6ae9b4e82 | -12.80388 | -56.22017 | 2026-08-14 04:34:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffd0386e-72cf-376e-ae4f-ff9330c0d369 | -14.3017 | -51.9651 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47a9b5d9-c7e2-3576-96b2-e86b38f85799 | -13.68582 | -46.26842 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b396ac29-a66f-39c3-b251-954e52493b3d | -14.34036 | -53.30889 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f712149c-9a32-3635-9747-abd78f6834af | -11.61919 | -55.17969 | 2026-08-14 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57832abf-4f99-3066-a888-8fcad29007da | -14.28997 | -45.26928 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
