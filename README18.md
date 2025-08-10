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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5a3f4aa-8dd3-3877-b042-3c93f3d39b46 | -12.53296 | -45.67372 | 2025-08-10 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddd83e90-de11-301e-a13b-dcdafbd57f7a | -15.16117 | -48.12795 | 2025-08-10 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07fa965c-6ff5-3a44-b736-f4842539750d | -12.60539 | -47.12946 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fad8ab8d-834d-3bf7-854e-7e28a05a6ec0 | -14.74045 | -45.16132 | 2025-08-10 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef8b9cec-9082-3aab-9c15-dce36979b62b | -11.43694 | -50.58697 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b57fbd8-1ec4-3246-af17-d3bd48885f78 | -13.63558 | -48.99622 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a704927a-b20a-34c9-ab0a-f893252e857d | -12.71296 | -46.37674 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf53ada-2f51-3ec8-bbcd-3b4dc3969c17 | -11.43297 | -50.58625 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02914fe3-ed90-3f82-bfe7-e357ed6943cf | -12.69166 | -48.20128 | 2025-08-10 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb091d3b-8ef6-3196-99d0-a735619d6807 | -13.61166 | -46.93432 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a6213d6-c5e5-3a49-a330-37a19f99186c | -13.06112 | -56.84557 | 2025-08-10 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a903a48b-2227-3690-9270-41ac1fa16257 | -14.58596 | -47.15237 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f058633e-3f1c-3dc0-9452-0cd42367ccba | -14.11969 | -45.40826 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5191dbe2-2ebb-3e64-9d96-f094b614c81e | -14.29766 | -51.98471 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb45c6ab-95ff-30c0-a093-5f5ea93f32ca | -11.92381 | -44.85456 | 2025-08-10 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21ab491e-46a3-311c-9069-d40e7e567e3e | -11.66009 | -48.32123 | 2025-08-10 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb1f4794-7ad9-3ef1-811e-9f29009c4b7b | -14.10797 | -45.39525 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c749e974-7f2f-31f4-89a6-2b8ce3e0c8d2 | -15.08898 | -46.54208 | 2025-08-10 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 268ee98b-1510-3391-b850-a262e31bbc98 | -11.93102 | -44.80788 | 2025-08-10 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe76485-8f18-3c7a-ac1f-3ee57df5e551 | -12.57615 | -47.15093 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 783de66f-1383-3a02-9c2b-e51628c6f96c | -15.20516 | -43.45744 | 2025-08-10 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ac128c1-839c-3e91-812c-f2dbbff0652b | -12.55645 | -47.08054 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 920626db-8a39-34c6-918d-cf4eb6efe48a | -14.09618 | -46.57189 | 2025-08-10 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01caf0e3-94d2-3e41-bbef-9a62aa72a218 | -11.42412 | -50.59002 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c9c24dc2-fd28-33a2-b27c-d836293d3b3d | -16.30226 | -52.92447 | 2025-08-10 04:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4af4c41-f1a8-3489-9519-ac2ddafe2d10 | -13.11034 | -46.89886 | 2025-08-10 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b51f0a-6feb-33d8-a027-0c6230763da8 | -11.48937 | -50.28159 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd33c3da-5308-31b1-8aee-b31a423d1ba5 | -16.30307 | -52.92008 | 2025-08-10 04:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b055cc-0856-3824-a0ba-0680a903eb52 | -12.70963 | -46.3762 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e5078a0-0712-3dde-954f-58159cb805e5 | -14.37812 | -51.11429 | 2025-08-10 04:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 110b89af-9b8a-3d24-883e-ba588c040259 | -12.57599 | -41.27899 | 2025-08-10 04:23:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f54fff33-a8d4-3978-a394-3ece4458308f | -11.37366 | -50.52743 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 844d1761-cb89-3557-92c0-9fa5c6815189 | -16.3718 | -42.53042 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483c5cb8-e24d-303f-9619-b407c20e48ff | -11.1092 | -50.48441 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1984945d-4c9b-3009-85ef-b2001f992cd8 | -14.03792 | -46.34356 | 2025-08-10 04:23:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8e2ed72-cc90-3c48-90af-346fcc758a8d | -11.72484 | -48.34464 | 2025-08-10 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bccd324-359e-39e3-b63f-1e3875207ecf | -12.57673 | -47.14731 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a42f472e-3cb6-35dc-a1ce-bbb3f0fc71ad | -13.60107 | -46.93623 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faadf8c3-6030-3f2f-94d4-c3bac5518618 | -14.44725 | -47.85731 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3800730-9326-3d31-8095-6dbdab467659 | -18.24679 | -42.57809 | 2025-08-10 04:23:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2381f72-a099-3ffa-935a-5189b4135e64 | -12.71408 | -46.36966 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 509e3dd4-2e25-3c42-b61b-7bd5d8ef67c5 | -14.701 | -48.56461 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4834faba-38ce-3f3a-8265-3efab6aa90a3 | -14.08784 | -46.58145 | 2025-08-10 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dcf746b-aaa0-360d-a850-0bee22652f3f | -16.08248 | -43.63436 | 2025-08-10 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07107cdd-6cb7-3fcc-80eb-627908d942e2 | -16.3833 | -42.53244 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2cf1f3a6-2f45-3bac-98ec-612b8d552633 | -12.55308 | -47.08006 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c12a3e01-2b62-30bf-9d78-7b221136abeb | -17.63279 | -44.64851 | 2025-08-10 04:23:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82a2044b-8ad1-3a7a-856b-676cdc8514b1 | -12.58257 | -47.11105 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f67f697b-8c1f-37b5-865a-77f62dfb673f | -22.52409 | -46.81311 | 2025-08-10 04:25:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 84576138-702c-3993-894a-d751c2f2aec6 | -20.19308 | -49.12381 | 2025-08-10 04:25:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c9bd92d-9e35-3654-85c0-33b1d2c3356d | -19.57476 | -47.22508 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35fab237-0c6c-356b-9d4c-32c427f834e7 | -19.57143 | -47.2245 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7b34b30-5a3c-389f-b11e-00f5bf9b9242 | -22.51845 | -46.80412 | 2025-08-10 04:25:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0c03d25-09a3-3a54-9efc-d5329b022a17 | -18.17301 | -46.99649 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fed934d-8a6b-322b-b630-1be91d348307 | -21.48314 | -47.75128 | 2025-08-10 04:25:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b69ed289-b5af-374d-a01e-57726e207140 | -22.83972 | -47.24191 | 2025-08-10 04:25:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41d7a1d0-1d81-3c40-a1f1-b6585cfd202d | -22.52185 | -46.8047 | 2025-08-10 04:25:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 18e310bb-6a87-3af9-926a-1786b56aeb11 | -18.17138 | -46.98502 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e9dfb3c-ffdf-392b-b41d-831f8adccc0b | -19.75458 | -48.01228 | 2025-08-10 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5054122f-26cb-3561-abb8-aa8fa684f5b5 | -22.79545 | -51.74168 | 2025-08-10 04:25:00 | NPP-375D | CAFEARA | PARANÁ | Brasil | 4103404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21777541-6500-3168-a601-57ff5bf5484d | -19.83504 | -45.92221 | 2025-08-10 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28d02aef-c36f-3b7b-a194-bc1708855d80 | -22.68498 | -50.47304 | 2025-08-10 04:25:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14374b16-8292-386d-94bf-e9741e136420 | -22.68405 | -47.3727 | 2025-08-10 04:25:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c9e87b7-5aa9-30d0-808d-ff4eff4c45bc | -21.6335 | -49.84157 | 2025-08-10 04:25:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05bd4e00-3b4d-3f06-9609-3611764ab547 | -18.17577 | -47.0007 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da341368-31e3-3128-8ad6-aa3b30c59829 | -22.90903 | -45.50155 | 2025-08-10 04:25:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1eaa6f3c-aa5b-3fae-b731-f41113098d59 | -19.57086 | -47.22817 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b40ee47-7be9-32a6-80c2-43a491a1e3df | -21.44717 | -47.02256 | 2025-08-10 04:25:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb9984df-d1dc-3fcf-88eb-dfa46bd4c783 | -20.17443 | -43.71785 | 2025-08-10 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fd8f8c7e-abf3-3f89-b499-25ea43e7cf4f | -19.88544 | -44.4199 | 2025-08-10 04:25:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7489ad85-223c-30e8-9b89-84a5fce06d78 | -19.57694 | -47.23301 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 676634d0-d436-3653-873b-387dcf087dcb | -18.17414 | -46.98923 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1054f9a6-b671-3465-b663-7c47730cabcd | -23.3972 | -47.00795 | 2025-08-10 04:25:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a7939ed-3d1c-3e15-a223-63ac3a1557bb | -21.17187 | -48.65084 | 2025-08-10 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b956b731-d9f7-3e0c-8b26-5584f122bd49 | -19.57419 | -47.22875 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e16adad9-48e0-36f6-8711-a38d9ab1b4d6 | -23.17752 | -46.7249 | 2025-08-10 04:25:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0bf1c431-a06c-386f-9e82-68338afa8d12 | -23.19565 | -46.76862 | 2025-08-10 04:25:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 567bf914-f630-3337-8391-6edb42e20220 | -19.40271 | -43.35564 | 2025-08-10 04:25:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 602093c1-e7a2-32f2-a409-73d5abe37898 | -23.59046 | -48.06688 | 2025-08-10 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88dc2f09-d6a1-36bb-b840-a13c7671d598 | -18.53728 | -45.00926 | 2025-08-10 04:25:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87cbca06-0f1b-3c1e-a0f2-c1e97c69a547 | -19.84815 | -45.92833 | 2025-08-10 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4584b1d8-39e8-38ab-bc3d-b70a4aa32330 | -22.69493 | -47.02346 | 2025-08-10 04:25:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5344293-c716-3590-85ca-af72671d5873 | -19.8533 | -42.30106 | 2025-08-10 04:25:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f3a4682-2d43-30bf-acb9-b4e7583bd01e | -22.90843 | -45.50589 | 2025-08-10 04:25:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 36b2a6c0-3e07-3c16-a5d2-81556fa2cd31 | -20.65854 | -44.73273 | 2025-08-10 04:25:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f31f64a-e4d0-33cc-9e5a-56abfe45008b | -22.72014 | -47.394 | 2025-08-10 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 65c9af9c-687d-3b28-b2d9-aa855f9e235a | -19.83961 | -45.91499 | 2025-08-10 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f4f18d6-7a63-36e3-a804-a952f06ab0ee | -19.20104 | -42.01643 | 2025-08-10 04:25:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 725d5c75-0f18-346e-ab25-3ba1184072cf | -18.17082 | -46.98866 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b726e19b-a41f-38a0-982f-52caf930e44f | -22.96668 | -49.24966 | 2025-08-10 04:25:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a2d5551-b113-34fd-8974-f0c5b81a76c7 | -19.08091 | -43.54568 | 2025-08-10 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42921951-1107-3ccc-905f-4a029077c408 | -18.16749 | -46.98809 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 46e11639-c0b7-3615-ae43-7451ffd55ff0 | -19.40493 | -43.35804 | 2025-08-10 04:25:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56769c02-9e8a-35f0-a5c7-366cd8a5bec0 | -20.94248 | -46.69803 | 2025-08-10 04:25:00 | NPP-375D | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8dfb14a-0e69-30eb-b2a2-44bc217e9780 | -20.47803 | -53.67544 | 2025-08-10 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ec8bc26-661a-3bb6-a8bc-e44aa1795844 | -22.90298 | -48.72651 | 2025-08-10 04:25:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 927fa835-8567-325b-854f-4777c36cff5c | -19.08529 | -43.54169 | 2025-08-10 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 825367b6-109d-3259-af02-f5d9f852c73e | -18.17244 | -47.00012 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37f06f39-3c5f-301d-bc17-2d06b89d90ba | -24.6775 | -51.04631 | 2025-08-10 04:25:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54a0d1a3-ce3c-31e4-b589-43831c428a3b | -18.16806 | -46.98444 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README19.md)
