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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93c22c30-9f89-3a17-bae1-1e75bfd41901 | -9.50333 | -55.97206 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e508cac5-5a90-31c8-9334-bae5917043a6 | -12.99819 | -46.75478 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed3e4e71-2810-3cc1-a130-b28cf39de9ae | -16.2829 | -45.68538 | 2025-09-13 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b239809-8e51-319b-9439-d778d509b7d2 | -10.52195 | -51.51434 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d883b626-f324-30c7-a08b-a16feab2e2f7 | -15.76965 | -52.23768 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2161bad6-9c06-3a19-b87f-96b0157f31e2 | -13.08745 | -48.26058 | 2025-09-13 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49d9d804-5dfe-3350-8579-28fd0f837c72 | -15.76902 | -52.2423 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d5a6df7-0445-38bf-9cb3-50d3408e5c10 | -13.15552 | -47.14056 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 644b078c-18cc-3f4b-b1fe-68fe6939f738 | -16.43296 | -49.04789 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b0c7094-67cc-3d63-a955-f5cbaac9b04e | -10.51202 | -51.53088 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b211f2bb-208e-3991-941b-196744ee625d | -11.70834 | -46.55233 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 71df9b09-0ccb-39b5-8206-dddf110fa83c | -14.28859 | -46.07189 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e449c28f-3481-37c2-a867-cd33ee665007 | -16.25127 | -50.06272 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42952220-e95f-3eaf-9505-7f8cd5ca17ef | -13.14851 | -47.13383 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e316f6-20d3-3dfa-9be0-26049a5995ab | -12.99515 | -46.73533 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8640cf3d-3e16-3269-ba8b-ead7db007a11 | -12.81319 | -47.96432 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79d7eed3-e708-36ea-96cb-3b9f88541893 | -11.38502 | -50.47018 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b72c0e67-1638-3111-9ea1-6401c22a0b06 | -11.31881 | -55.22494 | 2025-09-13 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83298a1f-0456-352c-b5bf-9547aac5b045 | -13.24009 | -51.72973 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c12aad4-45ce-39dd-96b3-80ac04d3915b | -12.11992 | -47.59531 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c56a4e28-ea1c-3e86-98a3-b30892f6dddc | -11.11157 | -51.41758 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99a52d44-b306-3f8d-9155-f5212c3489bb | -9.36687 | -59.48179 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17db2712-b674-308a-acea-6e1a5f70a500 | -10.0171 | -51.72739 | 2025-09-13 04:59:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 231b808e-cbe2-3221-ac3c-74fe32798a35 | -11.79032 | -50.54673 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7a3a63d-5def-33ba-9ce8-e7819eb5ca18 | -11.87347 | -50.57976 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9e5c11c5-2339-3f2a-9090-7aecbc899e65 | -12.09535 | -44.86325 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0fd8e48-0fae-3e5c-a8ab-9b0593d2b89a | -12.93328 | -54.74236 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76a8fbe3-bca5-34f1-988a-54fdefd6f01e | -15.70452 | -50.57736 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ffb9b31-3551-3f41-8a34-2e9248034639 | -9.88731 | -58.33614 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c21dc0-f98c-383c-b3c2-e4819d6dace5 | -15.86514 | -51.85533 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b31dc44-5597-3cb1-8d73-92a0fa5fca92 | -11.19426 | -55.08676 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c31a2783-5934-36e5-a55f-7a8d048f6859 | -10.51824 | -51.51367 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3390b824-f4ec-33ad-9cf5-99dbdafaca23 | -12.8159 | -47.93406 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3f6ce72-60b6-3349-8a2c-1407e9265c93 | -10.76497 | -50.55157 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63582238-837d-399f-b2c2-5243cfc2e834 | -14.21931 | -46.28573 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b924bff4-a9c4-33e7-a1b0-f7c3352d6826 | -10.09752 | -59.15729 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfb6f040-da0e-3581-afd6-a15d830071ea | -14.21296 | -46.24445 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48e2c341-2936-3a98-bc21-54f048abaa85 | -14.43198 | -47.3204 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 459b2af7-4bb9-3add-b252-b4468a6963b3 | -14.44267 | -47.31872 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 291f669d-0a62-364e-9a1e-f5dc24d44ec8 | -10.33595 | -54.32364 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 973c6c01-d4f0-3c8c-9138-1c661e7bb568 | -11.7629 | -51.51418 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98f0fba5-64f8-3791-8b16-1115451c618b | -12.91119 | -47.96065 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1fafe672-a109-3b3a-89fd-a271896b06a2 | -9.27263 | -59.4183 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 832c6b16-451e-36ad-9cd1-4bbbab9f56ff | -14.72332 | -59.71908 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddada345-3f7b-35c4-bb56-ef2c5a0be642 | -11.43273 | -45.61691 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| e8dcfb17-015a-38b0-ba1f-04dc0225d47e | -11.83389 | -50.5567 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a5186f-7ccf-340b-bf5f-c4d22ea753f3 | -10.5282 | -51.49697 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d68c8a7e-ce5c-3d55-b89b-151ce55518b7 | -15.165 | -50.14965 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf26be3a-ef39-302f-a464-d7696343f69c | -9.27585 | -59.39884 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 343831ac-f722-3660-bf79-455bb62a291f | -11.71404 | -46.54949 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a22985b9-d331-3ce6-8a99-c89291e83b81 | -15.05526 | -47.99911 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a59900dd-2b02-3c91-b8e4-826bd0cd4341 | -15.16993 | -52.49942 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f50e78f-fff8-3f41-ab5e-2b4ad2ddebd8 | -12.9283 | -54.75264 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6948a372-9158-37bb-b8e1-9a999b1f5d73 | -14.19568 | -46.24628 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e9c21be8-bf0b-30e5-8604-9dc856a2a4c1 | -16.56273 | -49.22335 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3bb49494-e127-3b43-bec8-cbc1eeafc945 | -13.14083 | -47.13225 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b835e963-877b-32a3-b546-139283374ba8 | -9.2781 | -59.4092 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6f693c7b-977d-38ac-915f-3fabe6591dfa | -12.07297 | -47.61079 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ca69bea-08d9-3943-9846-14ed61c735c2 | -14.46028 | -47.34742 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86352e88-5a7c-3b28-919d-4bf9488405d0 | -14.44496 | -47.34396 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b823073-d3ec-3413-aa4b-78bba4f45195 | -11.86692 | -50.56797 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 15802085-edc5-3af3-82ec-c05d9db7c08a | -10.18759 | -57.5343 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9daa9121-6228-3e3a-b32e-b0c7b413e923 | -9.25838 | -57.06738 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e4794d2-8374-3680-96e3-1b373db8c7c2 | -11.79784 | -50.55145 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7bb9c72-d226-319f-9648-8f091f03efdc | -9.83172 | -54.52887 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3c8c10c-9f69-3c6b-947b-f193bd6fadc0 | -11.33652 | -50.78625 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 614fc2a4-3bd2-31e4-a3ea-db055fb5ea30 | -15.05588 | -47.99368 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 201e1fce-580a-3486-8850-fb45aa3d32b6 | -14.20922 | -46.276 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b5f53cb-90b6-3a7a-8039-e35de5e5a6c5 | -13.92457 | -48.2732 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 41ffd8f6-66f1-3dce-a7e9-49a341fcc901 | -11.18213 | -55.07765 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e89aa5b8-4b93-3ecc-a81b-1226aea0e0fd | -11.86291 | -50.56738 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a8e2de85-e78d-354d-b411-d37db3a34238 | -9.27505 | -59.40368 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 591dc065-3a76-398d-9b01-4dea3886b62d | -15.55037 | -54.80157 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78b9a01d-3f36-326c-96de-69624435aa12 | -11.86947 | -50.57917 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3071d166-310f-3614-883e-eb0908e522ed | -9.2765 | -59.41893 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36300d24-67e8-354c-9ae6-406867404cb1 | -15.78296 | -52.25391 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a4c998d-c53d-315f-859f-f42baf0cc95f | -10.786 | -50.54107 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4271ac55-5bf4-3eed-a384-a1cb1735d608 | -16.26007 | -50.064 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 933d4af1-d3e8-31ea-ba35-8114ea101fe5 | -14.17651 | -46.26828 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 2a1b425a-c48b-37bc-b57c-f14341848e51 | -14.2189 | -46.28941 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe21dfbf-6564-3363-ab08-752e457f6c09 | -10.38077 | -50.48996 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cff24b93-50be-39ac-8a70-7827d55ad1dd | -10.15384 | -64.72899 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf21f350-f52b-3288-9096-b573c1b54d0f | -10.7267 | -48.61916 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1e093fb-52bc-363b-bea3-2be3f1b17954 | -15.70822 | -50.58193 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b2f5fb4d-268c-3091-a05f-e0a72062afee | -9.62646 | -64.18256 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c701e50b-2ee4-3b80-b525-7b0619e8fff6 | -9.26877 | -59.41764 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aaac09d8-e9a4-38f4-8817-57879fd84eef | -10.76942 | -50.52073 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e478db09-dc3d-3fcb-9496-758d878a23fd | -10.50389 | -51.53485 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af17a353-1887-3705-9644-3425c6f99d74 | -14.20509 | -46.26266 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c94e3b1f-2397-30e6-9ba9-284dab928c9e | -12.91039 | -47.96696 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 25a4361d-5e3f-30df-b117-2597501480f9 | -11.80234 | -50.54849 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ab5fa8f-458d-37d2-ab90-5cb09e6d4ed3 | -10.09298 | -59.16124 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7293ad20-93a1-3bb3-9c0f-7cf3841f31ae | -10.70864 | -54.44372 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73a75777-968a-3f72-a4b1-3415a87c5610 | -11.8445 | -50.58273 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37effc7a-60ec-38cc-af89-e6f5a9628119 | -15.77794 | -52.23391 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75458f9b-6d93-3383-b014-5da200d250e5 | -10.42353 | -60.46892 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48993657-4e80-3ebc-8c4c-1b58f616bf18 | -11.18399 | -51.42573 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5fa8aa1e-e114-3b96-a605-33dbbb773723 | -10.51447 | -51.54034 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95be8a00-2672-370f-8c63-b579dc2686b6 | -9.88646 | -58.33219 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8871799-8094-3755-9773-1cb8ffc642c7 | -12.58295 | -45.66997 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
