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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c7eb5ee-8fe0-3016-95d6-b3c08c8905fb | -13.23054 | -50.81199 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dac42e8-8650-3923-b3f1-bc42dfb0c19e | -14.65445 | -54.88817 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c1bffca-b3d4-3b01-b263-66c2fe3d986a | -14.95976 | -50.12421 | 2025-08-20 04:36:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c23cd331-00af-3b06-ac23-19d28ea4af10 | -13.33019 | -54.41846 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc7a6d55-fadb-30a7-aff7-019cf8d7aec3 | -13.34551 | -54.40268 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e84e0898-cbf0-3aa7-bf58-6d1c315bd2cf | -12.97339 | -56.85321 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d1f3efe-ee44-30d0-ab13-e0d5776a2e58 | -9.22829 | -60.33437 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c4ed8f9e-6854-3a0e-8358-db1ef5d12a94 | -9.9887 | -47.81763 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 411646b2-5502-31d5-beb2-514d98fff04b | -13.19677 | -50.74153 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfb31cb8-b92f-326b-a4fd-a2c4a7469e1d | -14.62879 | -54.89057 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0116f2c4-d7c5-395c-b07f-0c5f1be039d0 | -13.33291 | -54.42653 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c3627f9-40a4-3b8c-8324-5f237f5a04dc | -10.82248 | -43.27806 | 2025-08-20 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a126f871-3f0a-34fb-85d8-57a271be6fa4 | -9.22728 | -60.3396 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b168599a-e360-3a52-8d63-c57769b58e48 | -14.69224 | -49.05305 | 2025-08-20 04:36:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de68ffca-0d8a-3010-ace6-3502f9ed7c0e | -13.1889 | -46.90315 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf583189-6538-3ace-ad21-07ba0e0f9de7 | -9.23044 | -59.60254 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b073d84-17e3-3f66-8cb9-49d3ec9ada7e | -10.91337 | -57.50318 | 2025-08-20 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5539ee26-c87c-3b28-b5ce-0663a02fb8f1 | -9.23074 | -59.60122 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2836d25b-25a4-3a51-ab93-c094fdf59ecc | -13.35357 | -54.40415 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5427ba-4c45-322c-952a-e14d7e61ab99 | -15.75082 | -46.6259 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb5f09c-2118-32b0-b95a-3456cff51ded | -14.15475 | -45.28417 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 825bd18c-c472-3510-8cfe-20d73c70dccf | -13.58074 | -47.02787 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8983d992-049f-3974-8fc9-bac0baf0d629 | -13.03085 | -46.78347 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a0f8d98-bfaa-3b3d-b218-952abead9b02 | -12.4752 | -47.98133 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9c36d64-e831-32da-a122-c0d9e0536cca | -9.18739 | -59.63104 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 551ac91a-f104-3303-ba15-d7f3910d541a | -11.30695 | -44.92677 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72e186c7-de40-38e3-8ff7-377528b427f8 | -13.15275 | -54.91792 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cd379ec-8dc8-36fe-b5e3-edbacbb17c2e | -12.11108 | -47.90224 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a951eb3d-0b7a-36b2-ab4f-f591b045811c | -11.19159 | -45.0607 | 2025-08-20 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9dd3c51-1756-3e12-bad0-7dfc14550718 | -11.74709 | -55.84034 | 2025-08-20 04:36:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66068654-8635-379a-83df-3e92dc92963f | -11.44022 | -47.31335 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be7e0b8-17b7-37a8-89ef-4f647d7b2a1f | -12.9726 | -56.85442 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f82b19cc-e26c-3259-bbb4-5cfe03444e37 | -13.61568 | -46.8884 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6da9f9d0-a26e-3945-9544-51004fa858e9 | -11.44306 | -47.32093 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23e1e520-6068-3c00-a9ad-2b7e692aa461 | -11.132 | -46.98202 | 2025-08-20 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aeb7a29-ded2-3432-8197-4352bcfdf536 | -12.87106 | -46.0574 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae4501fb-a4a7-3fea-9edc-059c5476a739 | -15.19245 | -48.7488 | 2025-08-20 04:36:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1089bbd-c7f3-3eed-b3d6-4aa079fe6e22 | -12.95205 | -46.16704 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf2fa39b-9f2b-36ff-bbd0-8827f0e3aa82 | -14.70728 | -45.83935 | 2025-08-20 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a12606a-53aa-3923-8db4-9d687ef57768 | -9.19818 | -59.63884 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e961e2d-314f-3624-8019-d711d524e2f6 | -13.18594 | -46.89906 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ef7fce1-0db5-360e-8253-16725f2684ef | -12.96671 | -56.86279 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8617698-6ba6-3833-81d3-d73e30590d56 | -10.34411 | -44.90913 | 2025-08-20 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d6dfac-0beb-33ba-afdf-4b6417731e6f | -14.16307 | -45.28053 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be06d73-957b-38ff-8a3a-be933b24875f | -12.14487 | -48.01819 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aee48512-af9e-3888-8840-a995bb3ddde0 | -15.54575 | -42.27998 | 2025-08-20 04:36:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f648ba70-e50c-3d55-8e28-5e4e3bab512d | -13.34678 | -54.3956 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 709b8f28-be04-3828-81e0-8cda345148de | -9.18314 | -59.58696 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02850f92-e8be-305b-a71e-0e9c3c3fdef5 | -15.57613 | -50.31182 | 2025-08-20 04:36:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d527eb-e816-384f-a43b-985ccc0c8a17 | -12.95868 | -46.14679 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56bc99c7-cb8c-3a37-b8ed-d3efee17b396 | -11.44077 | -47.31302 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 641eebb3-a7f7-3514-bc6c-7dfa551a44ce | -13.19234 | -46.88004 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93d7353d-1a23-3aa0-a769-1c63e7abcaaf | -13.0336 | -46.78443 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b60ea6d-a535-314d-84a7-394fc390b113 | -12.90218 | -46.09674 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce157ecf-9554-3752-af3f-d9d8d0af25c8 | -14.55239 | -53.17815 | 2025-08-20 04:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb56b193-5c9f-3edf-8fe1-87d73f559ca7 | -13.62675 | -46.88631 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c3341ad-8c87-310a-9167-f1215d522ffc | -13.04074 | -46.78938 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a166321-7960-3731-9274-6d40c877860f | -15.54768 | -48.56824 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1c7fa43-784f-30ea-9cf5-410991bd3d36 | -12.51808 | -45.59695 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30e2901c-30c7-3a85-9bbc-8efc12092e39 | -16.11675 | -46.82138 | 2025-08-20 04:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fbb2eca-4f2e-3dbf-9477-896279393e69 | -9.18137 | -59.59626 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbd0991d-5b03-3cd6-88c1-4aa9f87377df | -13.04017 | -46.7933 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3275156e-974c-337a-9b4f-629e1d0365f2 | -13.03339 | -56.84547 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2672abd9-d5d9-3813-80c4-99df57e2323c | -12.63461 | -46.8822 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db26886a-9b17-3580-8f01-59fb9d45eb9d | -12.91369 | -46.10123 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53c504b7-2461-3029-a55b-1eb03b48d799 | -11.73954 | -48.18853 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb9cbb89-d3aa-34fb-9659-91bb4bf2e922 | -13.02793 | -46.80352 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b9d6db3-86b6-3d22-9dd1-3b8244591592 | -15.54486 | -48.56403 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3666403-ae20-308d-979b-12200426da40 | -13.41057 | -46.35807 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2f20529-8bf6-38b3-b1c9-51cb8f685167 | -12.14543 | -48.0146 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9101861-9170-3aa2-b833-723e818fb5a7 | -13.48636 | -47.05791 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82d9b8eb-b091-390e-9eb7-19073ea27f47 | -13.03057 | -46.80447 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc763c90-ba32-3679-b642-d32a0c1571ba | -9.19525 | -59.62279 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b8300ca-bbcc-3be5-a730-29c5945f8b9b | -12.97148 | -56.86364 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a52bf345-b3e4-3cbf-b059-47e9af6e34fa | -12.8992 | -46.09198 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c48dcfa-1081-35bd-a14d-d5bf86163eb6 | -9.24251 | -59.60518 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b789d27-9e36-3ed6-90e9-2325d97800b1 | -14.36263 | -52.00291 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94ea0b8b-112a-3315-9de9-4128a4fa3738 | -12.9781 | -56.87729 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 925fa1d7-7513-3539-b33e-f56647a821af | -13.86654 | -45.55915 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5546091b-50c1-3836-892a-6120d3f9c740 | -10.27823 | -46.77391 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 810b89ce-5b76-34bf-86b5-1153bfda33fb | -12.92018 | -46.09969 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8520d117-beae-3870-b7e9-bc01dd422185 | -15.4255 | -46.72247 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d9d867c-b594-32fc-ab07-84e93628de56 | -13.14228 | -54.92813 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 720c62f9-a620-3ffe-9361-167b6f6f5d97 | -11.31154 | -55.22412 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3984908-9b69-32c8-b968-8db828fc3cf4 | -14.74277 | -46.29682 | 2025-08-20 04:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daff9e0e-aa9c-35d5-b804-fcd9a4b71ae5 | -12.22288 | -53.60297 | 2025-08-20 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a73cf500-c5c2-3d08-8fe4-4a8563fa57fe | -13.18405 | -54.96012 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bedf4ae4-96b4-33fd-b838-9c7deee60567 | -15.42669 | -46.71404 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec191cdc-788f-3c4b-b26c-51d9a1a4fa87 | -12.65898 | -44.96071 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cab7e58b-bd13-305c-a525-99a029f076e6 | -13.1534 | -54.93828 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ca6c2a4-e3c2-393f-8b5c-9af9841a542d | -8.69001 | -62.10432 | 2025-08-20 04:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7451b4a7-106c-3d38-b397-3f9677280513 | -14.15925 | -45.27996 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 927c7c01-75ea-3d6a-8c99-c19c5a312500 | -12.94431 | -46.11894 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e005d97-4255-3bb8-a585-ea85782157bc | -13.02969 | -46.79144 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0ca198dd-47f6-3ff1-8955-d2b2e4bd2047 | -12.98009 | -56.8668 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35c4488a-fc1b-3b07-8171-396328250be1 | -10.24635 | -48.33483 | 2025-08-20 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 369b005c-78ef-39b6-8028-c7b00652d296 | -14.88846 | -48.09062 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9c93262-16b8-3fb2-a97f-dffe1acace32 | -11.57076 | -50.44632 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2701585f-e10f-316b-baa0-531278cdca83 | -13.03239 | -46.79243 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1d266cb-6620-3e1e-bafd-1c431b3e81d0 | -13.5895 | -47.55375 | 2025-08-20 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README33.md)
