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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b99fdd-4973-30c7-8703-b9721553ae52 | -13.60626 | -47.31477 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1668a1a6-cca3-37f9-b144-ab4817fd51c9 | -15.04637 | -47.1346 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0826e4f8-62a0-34e0-a5a5-871511125560 | -15.19626 | -56.02209 | 2025-09-27 04:25:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17daf55a-e4d3-347c-8ffd-164f4decb181 | -14.84804 | -45.61687 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b305f0d0-0fbc-32c0-b6d2-9c4e5fce24d5 | -19.1129 | -44.39167 | 2025-09-27 04:25:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9934036a-a980-33a3-ac79-1ec8a10ea87e | -13.50354 | -47.40954 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be281ea2-0de9-3901-8005-f12617c36632 | -15.04189 | -47.14122 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49df7929-e4e6-3adb-bde1-0c43ec7831d3 | -15.01227 | -54.99178 | 2025-09-27 04:25:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08ddd867-cb21-30c2-9c96-f60cc2c01cbe | -20.16647 | -46.20416 | 2025-09-27 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8957b7a7-5d99-3f76-a18d-0f1945a70340 | -20.29989 | -46.66242 | 2025-09-27 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54ba8871-73b4-3190-aecb-0f30faef7194 | -13.60013 | -47.31011 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 683512b4-23e9-3637-9b13-a2c41efe8d5f | -15.03339 | -46.9372 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4fdff5b-6a68-37bc-852a-481d58063920 | -13.79283 | -48.33562 | 2025-09-27 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0260d15-e406-33e6-bd83-470bf4562d23 | -14.0219 | -56.1039 | 2025-09-27 04:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4f78650-25c4-3822-910b-142f7867644f | -13.62896 | -48.07819 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fd91125-8f7a-3de1-9477-6f73fa16af12 | -17.50577 | -46.74103 | 2025-09-27 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59db3119-e91a-334f-90a5-70f53378dced | -13.50632 | -47.41371 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1cce206-310e-395b-82bc-3c9072f498fd | -20.32538 | -47.13685 | 2025-09-27 04:25:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebc2c4bf-4f95-345d-a338-8543993fee06 | -14.83739 | -45.64137 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7067bcf-563a-3e50-8ad1-d254ee0b738e | -19.40958 | -44.30841 | 2025-09-27 04:25:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecbb81ed-5247-3e9c-b6ed-4305848c3787 | -15.57171 | -51.71463 | 2025-09-27 04:25:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79cb25a8-1237-30a5-b14a-2fa2da0ae3a4 | -15.91078 | -57.50131 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 273876eb-f588-3fae-8954-775dc7bb55c5 | -15.57265 | -51.70934 | 2025-09-27 04:25:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 035b46d5-5727-3672-9dd3-7368473f79f9 | -15.90004 | -57.49011 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3444a562-b6ca-34e4-baa2-6f1fbdb72b7d | -19.63345 | -45.57272 | 2025-09-27 04:25:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df6812e-b7f2-37d0-8725-444640e01c9a | -16.00163 | -49.02622 | 2025-09-27 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d19b53d3-1f7e-37bb-9d4c-def9bdf32f71 | -13.60131 | -47.30281 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b36655fb-88bc-3e0e-9fac-d30199f849c3 | -18.36316 | -47.54585 | 2025-09-27 04:25:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac2a0c89-8fea-3d38-ab79-29eeb9cd1908 | -18.24906 | -45.01208 | 2025-09-27 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9f6300d-c732-3d03-b1aa-4e9fd3934e75 | -15.90033 | -57.49446 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79e924be-8d72-3ddd-a994-5c8850754697 | -15.19356 | -50.09929 | 2025-09-27 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0be339ec-fa16-3198-a1c4-301581a25a18 | -15.97205 | -50.87389 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f484142f-7014-334a-8a5c-ec362f04d158 | -14.06317 | -48.82227 | 2025-09-27 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed7ba097-160f-3e6b-9f57-6d068ee4bd4f | -17.09207 | -48.56425 | 2025-09-27 04:25:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 909a23cb-8a42-3df0-9f9c-49f74df8be8e | -14.94272 | -47.50174 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe19ecdb-54da-30c3-b54f-4b9c0bbd7699 | -14.83852 | -45.61159 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d90ceca-5082-3e69-9280-67a5f259f304 | -15.01184 | -49.53814 | 2025-09-27 04:25:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11b89c6-ee97-3846-8128-3ca99970c501 | -19.0498 | -48.13272 | 2025-09-27 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db408f27-068f-3fd3-bd69-f71107cb5797 | -12.48598 | -54.31536 | 2025-09-27 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3507cb9-1bf6-397b-aeb2-2b17b11b3a32 | -15.27768 | -46.4413 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93ff6472-8386-33ab-818e-c3c224a8f32e | -13.70466 | -47.89161 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ac0ba57-9103-376a-a015-106288bfc014 | -15.92475 | -59.48764 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 218b0d43-8878-3bf4-8b55-086cfe257723 | -14.84748 | -45.62053 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52ff0e3b-5724-3cfd-a75f-b103ea3f403a | -18.31895 | -57.12627 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9fd4f00e-e70a-31f8-a3f8-a1b9ff7264ee | -15.45085 | -47.09892 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4713cc0b-4901-3ad8-84a5-82b6ab9549e5 | -14.97263 | -46.76569 | 2025-09-27 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01cf61ab-1cfe-3e53-b9ec-0a8fed86a469 | -13.5069 | -47.41014 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed1c292c-7e5c-3729-a25a-9998ad3a2ed7 | -15.92604 | -59.4818 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f45eb87-0533-32cc-8a73-19c933278d1f | -13.70404 | -47.89536 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cb5932e-1423-3492-baa4-09d8d027c5c0 | -15.2721 | -46.45511 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb1b7960-cc2f-3181-9234-5da3a350df11 | -15.93639 | -57.49267 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5436c2a7-9d0c-3134-a160-16acfc446173 | -15.44753 | -47.09836 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6cb514b-07c1-3ca7-b20e-10f76305c2b1 | -17.18514 | -56.37586 | 2025-09-27 04:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5678eb50-0743-3b33-abcd-95d92eb78a0d | -14.83404 | -45.61834 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c55b84c6-d93d-3236-bdbd-0c978c956bb0 | -15.00898 | -49.23141 | 2025-09-27 04:25:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d729999a-c4c9-3611-9c45-2222668fe7d5 | -18.31438 | -57.12155 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2b12b94b-ec1e-3618-87ed-0e764497f8a7 | -13.70804 | -47.89224 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 600c1319-5e09-3ef1-b66b-c7a02a2c21ff | -20.9652 | -45.80699 | 2025-09-27 04:25:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf917436-42eb-327c-a0bf-035603aed364 | -15.20088 | -56.02639 | 2025-09-27 04:25:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a55e859a-9079-3473-ae8f-8a49c3af9796 | -19.30764 | -48.90692 | 2025-09-27 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0f2ab99-bba3-3532-8160-86f90fe7645b | -14.77993 | -60.18602 | 2025-09-27 04:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 454e627d-0522-35a4-86d5-b1eb7100932d | -15.89036 | -46.18983 | 2025-09-27 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5b3103c-4fb5-33ff-80e2-40ccb7093b6b | -13.83347 | -47.95956 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e9a84fa-9aed-3c2e-8041-f07a852db6b6 | -18.54613 | -44.77058 | 2025-09-27 04:25:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b5552d-311e-33ce-ba3d-9a18e798a13e | -20.32595 | -47.13313 | 2025-09-27 04:25:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89e3e043-f327-3e63-a6be-dfc91724d576 | -14.843 | -45.60481 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d9eb8aa-e920-3f74-90dc-0026b446fb91 | -15.02834 | -46.9474 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2297bb3-65c1-3aa4-bfca-2f8f5853fb45 | -20.43657 | -43.3694 | 2025-09-27 04:25:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b20f02de-0c69-3a9e-a6de-eaf371f2b79c | -14.57035 | -49.11157 | 2025-09-27 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 138aaa5b-c6f2-3104-89ca-5fb8af8d208e | -18.25401 | -47.00754 | 2025-09-27 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 399d6287-ce0c-337d-8844-4b6fd36719d6 | -20.31229 | -46.64909 | 2025-09-27 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d773648e-9a9e-3c20-a37b-8d5e28cc36d6 | -14.83292 | -45.62564 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d0e7c8bc-cff3-3597-92a6-149e3cb6e545 | -14.59371 | -48.24458 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bc435d0-ba93-3ece-a0a8-17fff43392be | -14.47949 | -47.7073 | 2025-09-27 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 830696da-8161-342a-9aac-d7e835c5bbb9 | -15.27993 | -46.42695 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68401195-0f76-304b-be6c-2bf672e57053 | -13.76779 | -47.80383 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b11f0a0-a7a0-3794-8bd5-8bb38cf5938f | -15.63857 | -47.82063 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 470bacad-cd7f-3e8b-b0f6-cafc39efb67d | -15.9419 | -57.4947 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd445b5a-f537-3855-accc-7587d2f59426 | -15.88979 | -46.1935 | 2025-09-27 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ef1199f-abc9-3547-8493-938af559ace9 | -16.81313 | -48.81377 | 2025-09-27 04:25:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97eba830-7f15-391c-a6fe-e73491711a81 | -13.75361 | -47.86948 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aa510de-435e-308e-83b0-b32994202367 | -16.75744 | -53.35668 | 2025-09-27 04:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 19ba9c79-c6f1-37a1-bb1d-824cadfc4f5f | -15.54015 | -44.33963 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa2bf816-d9f1-302f-95dc-41a897113578 | -15.90597 | -59.33186 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e341e755-a182-3785-a896-0d4725290e74 | -13.61414 | -47.30864 | 2025-09-27 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b974b9cd-bae8-31e7-87e2-73c3ef7cf1a7 | -16.76094 | -53.3618 | 2025-09-27 04:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6300bad0-de3a-359f-bc08-ee349ed05eec | -15.5503 | -47.91078 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3471c636-459d-3df3-a6fa-a218c6e72459 | -15.26018 | -51.47717 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 230dd505-94e3-3ad1-b197-d0dfb055fb41 | -15.28841 | -49.48159 | 2025-09-27 04:25:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80dd39f0-d58a-3e1e-bf0f-9941d9d3052e | -15.99979 | -48.7678 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ca5347b-d478-3fa1-a46e-acaee4aab70e | -13.72701 | -48.6695 | 2025-09-27 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8087e9ea-9298-382c-b966-c8367a7ba684 | -14.83796 | -45.61524 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3443e9ab-01cd-35e9-9cfd-d0e9fdbe70c3 | -14.83348 | -45.62199 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9a16a2e-6293-3d44-9ba8-2352e75b336a | -15.01882 | -46.96423 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84bd9cb6-25cd-3c9a-a60d-c1d7cbef90f8 | -15.27154 | -46.45869 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 896c0d08-7129-3d18-af4e-75c3ab7d52e6 | -16.12573 | -47.38962 | 2025-09-27 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b1d098a-f9d6-3a6e-a188-6638f1f2849a | -15.27544 | -46.45564 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 162d9098-61cc-3dea-9f36-168e7b59d079 | -13.37293 | -47.82746 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12fc232c-e903-35ca-a624-77ddc6c2ef2d | -18.31968 | -57.12278 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| baf96f10-a6a2-3e6a-90de-0f0df0646a16 | -15.92993 | -59.49458 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README40.md)
