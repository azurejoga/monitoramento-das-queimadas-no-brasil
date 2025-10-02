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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e802945-47aa-3760-896c-c49b90def7ae | -19.69427 | -43.98585 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e111241-a9a3-3306-be05-a799805792d2 | -14.30202 | -45.96737 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1519991-e0ed-3dad-a7c1-2bbae9bbab91 | -14.89584 | -47.1808 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135b1672-c65e-3e43-a1a4-8f2132ed0c0a | -13.15176 | -47.79034 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5e2a4d62-0787-34fc-a1bf-8ebbe96eb7b4 | -12.81804 | -47.02505 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f1707881-287e-3bd7-8af6-1385ff655326 | -12.94158 | -46.94613 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a8d57e6-91fc-3fdd-8d16-95c7613fa320 | -15.14387 | -48.38831 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 660bbfc2-362c-33bc-9380-3b2fa736b9f4 | -16.02055 | -50.86966 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7832ff1f-7935-38ec-885a-1dd36d654e3c | -14.58333 | -48.31755 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb6295ed-371b-367e-958a-815daa35131a | -15.25913 | -49.27922 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9eb0c444-0499-3c49-b1c0-05dc93d1dab9 | -14.63985 | -48.13285 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2e0123d-34ce-327c-b13b-204bb8400209 | -14.21843 | -44.9344 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ac286d9-c67f-3acd-ae00-91c943b76af3 | -13.08485 | -47.07545 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56f67ecb-c3bd-3406-a5c6-9170359ed25c | -13.80871 | -47.54336 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 03210331-cf81-3504-bd5b-0f64998fd6f3 | -14.59431 | -46.71406 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 384ed7ce-924c-3ac2-96aa-05045ef0c4e3 | -15.24337 | -48.72468 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a50e3a7-4f87-3c14-989c-0c4fc0ed7b69 | -13.41128 | -43.49871 | 2025-10-02 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f7e6c1c-e1fe-3f2e-a75b-9c11bbaa58cf | -18.50393 | -44.04099 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8b426469-80e7-35c6-8ffa-98627953f277 | -17.32534 | -49.38455 | 2025-10-02 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1b4ab48-234e-31b3-acb7-761d8a449bf9 | -12.07592 | -47.8365 | 2025-10-02 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ac2ca7f-065b-36e7-95a3-ea96aac795df | -14.3668 | -45.96147 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26faf34f-6277-3df2-a401-51cfe6566e5a | -11.87432 | -51.2308 | 2025-10-02 04:32:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd4f9bad-dae6-3f50-a80f-4625a1d4ea35 | -13.07645 | -46.99676 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d30cf3aa-3690-310a-a566-d330c9f79638 | -18.73305 | -46.8856 | 2025-10-02 04:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acc6aa2d-8362-3546-a949-9e3d2fabafdf | -13.24069 | -48.50532 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fcdc072-6170-38b5-afe8-14b40af90918 | -15.9298 | -43.30169 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31c456a7-189a-378f-a827-327da94526d2 | -12.01721 | -52.51441 | 2025-10-02 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9de7b115-0eef-3064-b6cd-e4969f87bfd9 | -15.22557 | -48.72901 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2db70d-7566-351a-8d3e-a54d4528d2f0 | -14.3533 | -47.12882 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0209bf5-bbb2-3e0b-883e-4f2c5ad545c7 | -13.94595 | -48.09148 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64bb3461-95e5-3b5f-ad7d-06741f3bcea3 | -14.30898 | -45.99214 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f899542-6193-3fec-9dd2-7f5b660008cf | -12.57134 | -49.89929 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42174c68-ad88-347a-8169-bc2d6494af30 | -14.4406 | -46.34522 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 552882d3-7dc2-3d44-a3dd-de84349ba02e | -14.20077 | -46.0872 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c1b3999-1a51-3a43-8e3e-889bf0971644 | -12.75172 | -46.90826 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69751460-108e-31da-b69a-f76455a11792 | -19.94916 | -43.6705 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| be2d500e-6689-3cc5-9cdc-086c57d478c8 | -13.29696 | -47.21214 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 969281f9-21e5-38f0-9377-96cde4475478 | -13.5353 | -47.27927 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f56a2cd5-ce39-3f80-bee3-68a7fc280edd | -13.29976 | -50.68133 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4aacc34a-23bf-3e83-a423-6702414540f6 | -12.70669 | -48.58633 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af6a56a4-5467-3b2a-b970-92cc2a239938 | -12.80028 | -46.86078 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21fcfd7-56f5-3dfc-92c3-b991802f9d8a | -19.71565 | -45.90698 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 524a1419-e09d-32bd-89de-3b03aed3aaaf | -13.80477 | -47.53133 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afa6e4da-5f0b-3f88-94ba-cd0f1629c3fe | -13.7584 | -47.95155 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bf22afb-054f-33f3-9fe9-007d07fc0a16 | -13.74942 | -48.00848 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec81c241-64bd-33fc-8c2c-4dd87e1ad696 | -15.26558 | -49.31388 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 068da64d-2bcd-3d3a-9522-b2610d4a6727 | -13.85506 | -51.24882 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a0d26b2-9bad-3093-92e5-94333bfd65bd | -12.80419 | -46.85768 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ef6b39b-e340-3ba6-b8cf-3db20d786487 | -13.66302 | -48.08493 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a2fa32-f129-38b0-a3b8-a972ee29c3bc | -16.00754 | -50.90411 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d784c9d4-2955-3359-89e7-ecfc8cbb75de | -13.05803 | -47.00487 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0482072-20bd-3e60-9f13-980685ad8ed5 | -14.64374 | -48.12984 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 601cfa72-92ec-3776-b44b-98617f99e5d3 | -13.30319 | -47.57877 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fbff47a-d9bf-3b52-9bef-a73736140b31 | -13.3876 | -46.94633 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d95e85c-bbf5-3e55-9e76-7b700829e0ce | -14.70478 | -49.61912 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2295fe69-f08a-328e-aad5-29d0d8a948a0 | -14.48016 | -48.41353 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77bdc586-c660-3599-b271-8731ca19a5c5 | -18.61237 | -50.69945 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e17a0d9-a1cc-3a37-a138-edb3e55e4fd1 | -11.929 | -47.88517 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 544c2759-f0ec-36f1-8756-5df73718df8c | -12.70888 | -48.59409 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ade5ee0-91d9-3134-b79f-eeca9cd3a9f9 | -13.21062 | -48.50795 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1f60893-d3da-3933-9815-13f9a1ca8fdd | -14.46855 | -48.40062 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 708d7afb-d168-3b46-90a9-89024072aea5 | -13.76057 | -47.98112 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7d07d8a-f054-3a12-a646-77c4f9582b93 | -13.69509 | -48.62849 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da919828-7678-3b17-97f9-df660ce36e16 | -12.17685 | -47.81635 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920ee07f-de13-3554-9f2a-8e73d99d1083 | -12.87715 | -47.01986 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43c07393-a461-3f1a-83ac-020afca540cb | -13.2208 | -47.3496 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3083556-1748-3f32-a438-3d7fc46fafce | -13.30639 | -48.70377 | 2025-10-02 04:32:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0707d5c1-3a23-3d76-b374-d53e908d2c45 | -12.71167 | -46.89128 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a86a02-d6cc-38be-8477-7a49c9d60d8d | -13.67474 | -48.05404 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b3effd-168a-3c36-9bbb-6e421cb48c07 | -12.80418 | -46.90208 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3bb2ee2-58da-36c8-9592-5f63371b3f59 | -15.21772 | -47.1752 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b926254-4760-31b7-8d22-4b94ba506a3f | -13.28029 | -47.25323 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b6b7048-7c43-3357-8cf1-7d96904dbc9c | -15.1625 | -48.00934 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5a0e280e-9b0c-3300-98be-5a4c0e73672d | -18.18618 | -53.28481 | 2025-10-02 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d314013-0384-3dfa-b626-822422f8a8c2 | -12.80084 | -46.85713 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39e51eac-44fa-389b-8d90-cb1bf01b76f6 | -12.8582 | -47.03151 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ecd211d-eef6-3a4c-a0f5-91afb50e9b33 | -13.42591 | -47.79177 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 60388a28-883e-3cc6-8261-c8d6f0673351 | -13.6897 | -48.06747 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f6a8cdd-77e6-3642-b40b-99fbfbcce1f2 | -12.18667 | -47.90501 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 261aa533-7dac-3c70-b97a-5b129967366c | -14.41726 | -46.13069 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5706434e-e13c-312d-8fc6-0ced31f9dac8 | -13.5286 | -47.2562 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2295bc5-7271-34a3-a28f-a5e0cf854b9b | -12.85485 | -47.03099 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efe5c4da-18a9-3e1d-b54c-1a44acf9e5a7 | -13.17559 | -47.81242 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51e0c8c8-5f04-33e7-89d4-9a9df4a64f03 | -14.34181 | -43.84349 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ed95a50-2a9f-306c-b96e-dd4628241515 | -14.79324 | -42.83036 | 2025-10-02 04:32:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb4cfde5-9ae1-3bfe-9218-e20e7fb1d468 | -19.25521 | -46.22805 | 2025-10-02 04:32:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bdc9d67-c5a2-3535-8ae0-68cf9933c473 | -12.82418 | -47.02974 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fea6d393-5ec3-377f-a0d7-74800bf58a3a | -15.26196 | -46.39896 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c51a65f8-f57c-37ed-b0ae-2c42d2273432 | -13.01754 | -45.21506 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbbcd799-f353-3486-acaa-d3c2c379df75 | -13.3739 | -43.76105 | 2025-10-02 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd80cc3e-754d-3033-bfad-e75e9b093e09 | -13.3231 | -47.20919 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48e287fb-a1e5-3a2e-9824-05e5f9e62eb8 | -14.88427 | -48.33753 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4251b347-684c-3b44-af57-5f5dba7f1bdc | -19.02375 | -49.74519 | 2025-10-02 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1057270-1718-321c-96c9-c8174ea0a4e4 | -15.22442 | -48.7362 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e652ac18-bcf1-3f60-a488-3c21e7e55357 | -12.93348 | -45.10437 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff70ee75-4d33-3d24-8732-bacb213a404b | -14.58829 | -48.32936 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d3039b53-67d3-366e-bb11-7b783aac66f0 | -12.69459 | -48.55483 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40aecd09-a612-3e7d-b86f-16df38429fc0 | -14.47797 | -48.40586 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4d8460c-6e5a-3cf3-a5c2-41265f1544ff | -14.79714 | -44.88525 | 2025-10-02 04:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d630ccbc-785e-34c4-9e29-8b510fccf36e | -14.43435 | -46.36358 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README94.md)
