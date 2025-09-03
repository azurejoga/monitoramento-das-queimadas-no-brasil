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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1969c077-45ed-3b0b-9585-7cefdc7ad052 | -12.93161 | -57.00396 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af7ec0c2-ae7b-3976-b12e-c363a54f6f35 | -11.05406 | -45.40317 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18fad350-f0ca-3474-9132-add98f2c16fa | -9.42095 | -48.36171 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a4bc7b4-2e5f-39ea-b734-d98f486ce64a | -8.0568 | -52.351 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90b1a8c4-7f5e-359e-909e-d0541d7facd6 | -9.333 | -55.22939 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dca1c2b6-d004-33c5-8d2a-ee02f7a3a2a3 | -10.0063 | -46.90391 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d6fd60b-0946-351e-b9d1-eb1c694e23f4 | -9.64795 | -48.07184 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd5c6ee-21cb-3671-bd77-0c372489f87f | -11.59119 | -52.13313 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 0016c6c3-f6d4-3523-a491-a5d270c04eb4 | -11.27416 | -48.94594 | 2025-09-03 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9509e9f-f114-3046-8fd5-ba7ee30c83fc | -15.10423 | -48.12473 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7507d756-5264-3a17-8897-1c4a3afce9f3 | -9.72965 | -49.00264 | 2025-09-03 05:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1cea086-7068-3625-99cf-b87fe755edfe | -10.12362 | -47.43809 | 2025-09-03 05:14:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| caa47953-7c8f-3c96-ab29-ad973e66480e | -8.06216 | -52.37169 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1720b8c-a7b0-3f2a-9866-f76580e46333 | -11.60213 | -52.08582 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 568f4f9e-3209-32c5-bc7b-c6942f200e3b | -8.37295 | -48.29159 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a448e06-c0e5-3dc6-8321-14e3e4557ed4 | -14.83046 | -48.36322 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2d410f7-9ccc-356c-92fd-697a2095fc8e | -10.94771 | -50.77387 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d61fa3e3-faa0-3f67-ac34-866914f7dc90 | -11.61719 | -52.07465 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab1c5e5-0a4d-3ac3-b420-e733860e4692 | -11.21649 | -55.07327 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b550cc8-b0d5-3578-a8d2-9559fcf0c104 | -13.0168 | -56.87284 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5161ee7-419b-356a-aa1a-445103333774 | -11.80643 | -50.62942 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45b96a7c-efff-31b6-916b-ce4889d001a9 | -11.59973 | -52.10342 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55645307-9bf0-31ed-9373-3c894d37adc6 | -11.91855 | -46.66425 | 2025-09-03 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1ff15fd-2b33-358d-89da-2f887fa9de45 | -9.75018 | -46.91117 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a16c8aef-10d8-349b-9355-86909b323828 | -12.943 | -56.97494 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8d6e8b4-ef06-38bd-9ae3-f69df08be18e | -10.49121 | -53.65619 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fae9bf8c-6070-3fa5-a0bd-2411204d79b3 | -9.61101 | -55.38745 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f38c55ac-c282-3bee-9621-04d3f01cf06d | -13.1024 | -57.14139 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7818ca5b-eb34-38bb-8559-437a01987a99 | -12.62941 | -56.99661 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 771759ca-2498-347a-bf01-4531efd5d06f | -10.48225 | -53.6344 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85f75c71-3026-327b-9857-8aa4a7e7ae3f | -7.70885 | -50.25606 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a719362-c5ec-3212-b938-f53a89588e29 | -10.4685 | -53.62547 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fe59fba9-5344-34b3-8991-0e9996137b41 | -11.42038 | -55.17794 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe3b5b44-3b7d-34c1-b2ab-c9cd404fc6a1 | -10.14816 | -46.27339 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 791226a2-3944-3bb0-bace-37d9b9d23a33 | -14.54831 | -51.9449 | 2025-09-03 05:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e21825e-0213-367b-9492-b3d69db302c6 | -8.87467 | -45.82714 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ef3a3d5-d52e-3481-8da8-4e59261b83c6 | -12.91352 | -48.09463 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 347f59b6-cf22-30ca-a6fc-b9ee12a80718 | -12.91725 | -56.93607 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49dfa24c-6f88-3307-85d1-aae42fc854a1 | -10.4569 | -54.77695 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 324d1f22-7931-3ccc-bf2f-9044f1bb8a2b | -8.08727 | -47.60166 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d737eb3e-b43b-3043-8189-f1628642c89b | -7.08882 | -63.06628 | 2025-09-03 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab89e09-b823-3e47-becc-7836501f041d | -9.32945 | -55.22886 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34005641-635a-3f0f-a44b-7cf357fce9ea | -12.60663 | -57.0084 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10ad76dc-cbb6-329c-b734-8285abe01ce8 | -11.86246 | -51.46145 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08c00bda-70e5-3ea5-b398-508689058973 | -11.0375 | -45.06337 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c58afbd-6ee2-3eb2-b759-d7055e203dff | -14.5743 | -54.55209 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db143ed3-fcfc-3de6-a132-48d724dbd598 | -11.59413 | -52.11152 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 40a996fb-d135-3f21-9dd2-bc676bf9ad4b | -11.64861 | -52.04343 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ed3f11-bd87-3266-b69d-56ffe5cdae0e | -12.95157 | -48.07603 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b09e11f4-7114-305c-abfd-fb04d4c3212c | -9.63394 | -47.04327 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f23ea37f-13fe-35d2-8c0b-c7b8898544e7 | -12.89328 | -56.95546 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8b696a3-19ae-346f-925d-3c941bb0624f | -12.89059 | -48.08609 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08486dcd-12ec-3025-a0e9-1f79333bcef4 | -14.35214 | -52.80634 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5030b875-0324-3d8f-8b3d-3d8820697fe7 | -11.12192 | -45.12007 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6678047d-6ef9-3442-a0e0-d704f86939ea | -14.8397 | -46.69633 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92030262-13ba-31f9-9ba5-da1c4d8d45cf | -15.00003 | -50.05265 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3223969-5d73-3ce2-8c11-4f6c2e22c389 | -7.70333 | -50.26084 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d6257a0c-b6d9-3b77-a612-9ee56e22df7c | -8.43846 | -45.08843 | 2025-09-03 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 620fe54b-5255-35fb-a25b-f468836f60a1 | -10.98975 | -46.82681 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f6cfb8a-ed6e-3824-922d-054dd439f3e7 | -7.71311 | -50.29353 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bca28f51-ec6e-36b3-9105-c80beee273ce | -14.81049 | -48.21591 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f256bd2-4b90-340c-8010-111f9f025082 | -10.43548 | -54.7691 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ebcf6f-c9fc-376e-9fa3-3f6488146e0a | -11.82963 | -51.56931 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9aa95107-1ccb-3584-840a-5b2c07ed5f68 | -10.94701 | -50.77909 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f5260d-bb37-3765-a76e-5c3f99b60655 | -12.94872 | -56.98356 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 455ef2f9-c6ac-34c3-b23d-7c503476064c | -10.48941 | -53.64058 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26a65ce8-cd36-3e0c-8571-766474615ef4 | -11.06344 | -52.07705 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ef8f74-b299-3fc3-8592-8311a17c5bdd | -14.40744 | -51.7079 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46f4f921-8594-3ac3-bf99-a1ee018fb748 | -10.95872 | -50.76476 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2c71eb6-7321-3a0b-85c9-60600f44d06e | -12.94244 | -56.97871 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 234a5ad1-373e-3da9-9ea3-8e4468706ecb | -8.06326 | -52.36427 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87e65f7b-f299-3c42-8a83-12742e47b990 | -11.66186 | -57.35281 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7459f16-f84d-3108-9ed9-94a2e9f0ff8c | -11.86366 | -52.4305 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a0ab270-b458-30ed-b101-60886b8d1066 | -8.36653 | -48.2979 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 473429e1-cfd3-3ebb-a900-1f4269e0891f | -11.59178 | -52.1288 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 119490c6-c0b1-3286-a8a8-682fbcc39bf0 | -12.49618 | -53.83572 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8620e7e6-2c3b-3c9f-8c77-ce58c3764491 | -11.59502 | -52.13803 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b0ca74b0-aa31-3bd2-8c24-d8e67b385c0e | -11.58471 | -52.11465 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cae6ef41-460c-3488-b15c-916d8d5350db | -6.44086 | -58.126 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb7bcd3-ddca-3f10-ba45-36c7d925aa43 | -10.47797 | -50.3489 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e08b9aa4-85a6-3139-b629-a513a9659761 | -12.97378 | -54.76903 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d641304-2212-3d5d-a222-dc95e2b5b70c | -8.35922 | -48.31086 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2102b04-5f44-379a-a72c-ae0740cdbbae | -11.65849 | -57.35228 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e5dfb9-b78b-3948-adfc-a5fd571c7883 | -13.90314 | -48.1185 | 2025-09-03 05:14:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5aaccb0d-9e7e-3afd-ad18-aba54e129916 | -11.9244 | -46.66953 | 2025-09-03 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72f065e1-a622-3296-ae7a-2a1b6c148921 | -11.53011 | -54.40927 | 2025-09-03 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 118578c7-a144-3b76-9027-a6f3111b97e0 | -14.57498 | -54.5471 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6d4b399-84bb-3a60-88ab-2560898bf846 | -13.49626 | -46.81833 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8382466d-dd2b-394a-b11f-5b94228d7892 | -13.45724 | -46.92744 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6511aaab-555d-3a4a-b549-60347ecca609 | -12.8646 | -48.02331 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47bd15b5-d283-3ca0-bf9a-29ba73b8e004 | -12.95044 | -56.99537 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 755aca08-2731-35f2-a558-f07a8264eb1a | -12.88997 | -48.0387 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af3bdf89-1486-3fea-b267-2ec1ac6822af | -7.69312 | -50.26468 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e9bf0f7-c53b-3cd2-ba46-1e5a6bf0cb41 | -12.92077 | -57.00612 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5fd460b-9a2c-3a4c-950e-e544691f88bd | -12.84546 | -48.03305 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 552b139f-06ce-3580-b5a7-329c692ab65c | -10.88509 | -55.74782 | 2025-09-03 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fff143a8-e622-3cbd-bf02-dc7b2f470e01 | -13.09669 | -57.13287 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef0ee36-a84b-3c1e-bf6a-914d88ce34b0 | -11.59427 | -46.76923 | 2025-09-03 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c5646a-a3c4-3128-b47e-226d5a8286b6 | -8.34964 | -52.52342 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2184797-abb3-39b6-b530-95dd911ca787 | -9.64486 | -47.8565 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README96.md)
