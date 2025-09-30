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
| 9dd4b623-9121-3499-ba16-46dbb4cba3e7 | -14.51279 | -48.44148 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c877a568-2d4a-3bd8-ba3f-fcbfc7d9cac0 | -14.52057 | -48.44468 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fddd1aaf-ef01-372a-a847-8c400f59c5ec | -14.71474 | -48.25257 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6311aa9-f558-321d-9086-60a39a3d4426 | -14.52694 | -48.48337 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05f4edae-dbcd-3d95-8a3e-ead1ed2e757a | -17.90865 | -57.58604 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7051b8bc-99bb-369c-b5e7-1b43d6150a8a | -14.54314 | -48.48359 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3879c5e-d86c-350b-8717-35cfb8154f5e | -13.81216 | -47.95847 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4edf30ab-2f7c-3a5f-985a-9dc67ff448ae | -14.54577 | -48.26011 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98b17da7-7c61-3d73-98f2-862669976794 | -14.3852 | -47.14302 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94148bf7-26a6-3f31-8c05-52357c8e89f9 | -13.78044 | -47.94532 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02f7c470-cfb2-3481-a57c-ab983ab88a51 | -15.92747 | -46.20823 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b8ce68d-c5d1-33ef-974f-d414c566f7f3 | -14.39105 | -47.14336 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ed4dd87-3a4b-340a-a287-6775207597de | -14.54811 | -48.48729 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27c81c09-e0c0-3f74-9224-4ac04d7b6b4f | -14.68911 | -48.14061 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3377d2c6-5215-3ef1-b437-76602fea4518 | -17.39254 | -47.13134 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 907dff0d-14b0-332e-8c39-6256c77f98f2 | -13.75137 | -54.73971 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a67cb12-a6d9-324b-bd84-3774f5832db7 | -13.73492 | -48.67492 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 324797db-0453-3b9d-b15b-481610097da9 | -17.3916 | -47.12952 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cab37b3-1823-3207-a1ae-66489fa37f24 | -15.03504 | -46.9895 | 2025-09-30 05:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 101fb846-a524-3b22-a5bb-bd64f306a5e7 | -21.22249 | -47.13129 | 2025-09-30 05:10:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da3a7142-5db7-389d-8d02-098f669d06e9 | -20.28676 | -46.23542 | 2025-09-30 05:10:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 121d5a24-565d-3a72-88ce-6befe499ff80 | -14.51897 | -48.43528 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5a1895f-2e30-3469-9ae6-dd723e1e7fde | -14.65164 | -46.96672 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2a38d17-9d3d-34c4-b2e8-22f196275796 | -13.62623 | -48.02995 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0759d79f-eaa3-3ab5-a6ca-e33806c3a9bb | -15.05512 | -46.97029 | 2025-09-30 05:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1e635ae-18c7-3e2f-94d0-a4e09839e6a5 | -15.71931 | -47.59002 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 85c39f40-0a00-3ec7-a217-22665c1bc071 | -15.91678 | -59.50252 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e61a6c5-d71c-3ece-8ef2-348d311b36a7 | -13.78808 | -47.97427 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45aef3a6-6448-327d-9bf1-c8763b0d2b9e | -20.063 | -46.79794 | 2025-09-30 05:10:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 079fffd5-8b9a-33b4-b158-67e6c65dada8 | -14.79195 | -48.30723 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1a29548-679c-3740-911b-5bf29b4174f7 | -14.51226 | -48.42247 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c26d748-585e-3a5d-933f-228841856800 | -17.91873 | -57.58757 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ed066730-463a-3995-b021-0e2ab511c5d8 | -20.62434 | -46.18591 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 96facbd8-4be7-3b65-91af-21c191648ff6 | -14.51335 | -48.46035 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1d9fae9-45d0-333a-899d-2840de43a126 | -13.84345 | -47.50761 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b62f003d-ea46-3143-94b9-c5829b86f432 | -15.2736 | -49.25551 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05ca7179-62a9-32fd-8779-ac4dc100c037 | -15.7196 | -59.51151 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a480b50-17af-3a95-be00-637080255e18 | -13.79853 | -47.97953 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 789ee988-a5c9-3df6-b5bf-82314d399a92 | -13.75589 | -47.91807 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 033cfdba-ee96-3f65-92cf-9e30b4460e5c | -13.74499 | -47.91622 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5590aee-4230-3103-a1c9-f4163b909e5b | -15.28437 | -49.27072 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e0e9ec7-d96d-351b-bcf8-1fccbaefd10b | -14.54764 | -48.25591 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f335275e-754f-3648-bc5f-8c9efa3a628b | -14.52185 | -48.386 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4f1de30-e743-316d-b0cf-39cc2744f7b9 | -19.86127 | -44.55688 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ccb23226-98da-3ac8-bdd4-912c7c1785df | -16.4229 | -47.03981 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e08071e-cd53-3eaf-8ba2-94095856ede6 | -14.51615 | -48.38829 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 726f13cf-dcb8-3d06-a68a-aba1ef1d66c2 | -14.51007 | -48.46384 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b25034bd-0150-3f6f-8d90-30a2180d19cd | -16.0062 | -59.51045 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 413bb797-938b-3a72-ad3e-00ee673375a2 | -13.85175 | -47.95929 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69d4b733-d8f6-3bef-8d6c-db8d18ff7e3c | -14.57399 | -48.21785 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3011bb7d-9e53-3c96-8298-6b0fb75653d3 | -13.78575 | -47.94741 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75f96245-19b5-3441-a741-9fe49d89f235 | -17.092 | -48.56604 | 2025-09-30 05:10:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02241b55-8ec6-31c8-b0e9-40b369838069 | -16.41156 | -52.17206 | 2025-09-30 05:10:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 132736ce-04b8-3119-9022-78bf365db5b2 | -15.26919 | -49.24914 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e95922a7-df7f-3e9b-8323-85b62d18a15a | -15.4893 | -48.55365 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 816f9af6-def3-3367-baeb-19fc9523a0cc | -15.85803 | -46.22812 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 154dd2ce-5177-3fa5-afca-63527c1bc880 | -14.54084 | -48.25549 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b323067-7d0f-37af-8d59-8400530efe05 | -19.71065 | -45.88374 | 2025-09-30 05:10:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f04d698-242d-33db-8112-d6848dab9f88 | -14.52482 | -48.47606 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a612dfa-1f1b-3836-bccb-0d130544de5d | -14.52525 | -48.38383 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3cd43d0-fb16-3a15-9f10-6686bae3d5f4 | -14.69864 | -48.24908 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dab62f25-51bb-39ae-9968-41423e1d053a | -14.72333 | -45.22209 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a558705-75f9-3629-804b-9196bc2cd733 | -14.51462 | -48.40179 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d4230f-bc33-3805-8c66-075a93328367 | -15.47492 | -47.93836 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0441aeb9-8082-3382-b201-f7107607ecfb | -13.71748 | -48.6448 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f08bce7-dbe3-389a-976a-46d2cbdba7eb | -14.54151 | -48.26147 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac5c8864-8769-3e91-aba8-9f7c80bf1639 | -15.9264 | -48.12869 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34bb0034-4da3-3134-bf98-c6161242cadb | -15.465 | -47.9257 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57521a08-2fae-3129-a17b-04a23d6c570c | -18.32578 | -57.10455 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 17a3cdf2-cd6c-3c2a-87c3-a797950f9851 | -14.70948 | -48.15612 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 42f968ef-ad32-3ff6-ad06-d817bb81a65b | -14.50969 | -48.46701 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b56e3198-75b1-3b38-9596-07496dbf5ef2 | -15.17455 | -52.29725 | 2025-09-30 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d93762c-b3d0-30d3-9a40-dbb40e2ae10f | -14.70934 | -48.25168 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 225c8cca-ebee-3934-9aac-915c910dcb16 | -13.60172 | -48.036 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ebb6b05-74d4-3432-a89d-11d366929f96 | -18.90905 | -48.06848 | 2025-09-30 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 318d8122-79b6-38f1-bda9-15402acf3f41 | -14.51658 | -48.45491 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4c38dc8-71a6-359c-a1ac-9ef8ab1a901f | -14.6933 | -48.24767 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93917b97-e8a2-3486-9073-6427b11861e8 | -15.80842 | -59.52278 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3408f5a0-4afb-39e8-9ec9-41083c23f62a | -14.51061 | -48.43702 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4abea7fe-79bc-389b-97ab-e3c2c17321c2 | -13.72856 | -48.68351 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9bc8f64a-b1cc-3145-94eb-80d90bfa0fc4 | -18.90856 | -48.0683 | 2025-09-30 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 788a48df-a97e-3ec1-82c8-9118ebe2522d | -16.42594 | -47.01097 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d089823-d85d-31e8-96be-4e1d2b570147 | -13.73063 | -54.73229 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0715e55d-b412-3735-88c7-3f013ab55b94 | -14.51204 | -48.44765 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 315cdda0-de88-3083-b6bf-34a312a25927 | -15.84596 | -54.02999 | 2025-09-30 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80c9c714-83af-31b0-be04-615cb81a8a16 | -17.39549 | -47.15065 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82698d73-1517-339b-86db-ae29b11410d2 | -14.71055 | -48.14693 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 624ff4a3-de04-37fd-88e9-587dc5474559 | -14.58244 | -48.28695 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d73087f4-4dfc-34c9-bd0c-b928970f71e6 | -13.23336 | -50.93089 | 2025-09-30 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9abe6c64-2df1-398e-b76d-6b086275b0c5 | -14.53179 | -48.48812 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db562bd2-158d-3a29-9225-6295fb04db31 | -14.51424 | -48.40505 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5891f57c-a2c9-3e99-8711-9ef8ee82bef7 | -20.61851 | -46.17624 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aee7e09e-90e6-3af8-b231-ca77d277b047 | -14.51262 | -48.46672 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73d9f3cd-0035-30cc-9300-a2cb40a40610 | -13.80951 | -47.88815 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6451a043-1e91-359d-9d5d-1f288b5a5858 | -13.22774 | -50.93908 | 2025-09-30 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce27f1eb-35ac-311c-a368-5fa02e3a9393 | -14.708 | -48.16881 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bda332c-b21a-3c3c-b060-04ee720b53fc | -15.32988 | -43.80503 | 2025-09-30 05:10:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7938c982-9091-3a25-a476-f7cf81dcf79c | -14.81354 | -48.75813 | 2025-09-30 05:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6a62a11-781a-3c6b-b111-97f7c844aaad | -14.56703 | -48.46442 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f24f029-8080-334c-a96b-2294a88aef5b | -18.46747 | -44.02495 | 2025-09-30 05:10:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README102.md)
