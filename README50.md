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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e966efa6-b79c-35e7-b421-36f9d8384948 | -17.6098 | -52.68429 | 2025-08-31 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b132ca-bcb6-3d9e-ac42-471c22efc360 | -16.97653 | -49.30512 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f6d8b7-303f-3717-b247-b43cac3257e0 | -16.53623 | -55.05233 | 2025-08-31 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b861a80d-8645-3788-a4ee-68b4d6e70aee | -14.58974 | -54.54822 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa3ca8c0-7ffc-3e64-b0c7-6b079d91f69b | -22.18013 | -46.63814 | 2025-08-31 04:32:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2897006a-b5ca-3da3-b55e-94c72029f058 | -18.12041 | -44.98594 | 2025-08-31 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18abdb2a-fd52-33ee-9004-d3ce4e43eb48 | -20.25863 | -46.0194 | 2025-08-31 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 835a1c71-63f4-3db4-8cf3-009eae281fb6 | -16.40818 | -45.65332 | 2025-08-31 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ed75e44-86a5-396f-8214-68636b719c03 | -15.68721 | -52.75021 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c86b411-b125-3190-b67d-8a2d1545aa4d | -14.80059 | -59.71763 | 2025-08-31 04:32:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c469ae6e-0c64-3318-b316-1334e21180bf | -17.20251 | -46.0747 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77cf4080-e2c7-316b-a32d-44ccf891e645 | -17.15878 | -46.08141 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f72bcd91-57e8-3b1e-8457-0765aac0ec45 | -16.45943 | -46.86929 | 2025-08-31 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7115dd89-f278-36a1-b452-b3bf2a7d7901 | -16.41175 | -45.65386 | 2025-08-31 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f52de66-3a92-3d13-8a9c-6fab0e652e0d | -17.14821 | -46.07973 | 2025-08-31 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074bce07-a234-30f5-a59e-476ef4877053 | -16.22462 | -52.69197 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ae86cfd-6f92-3c45-b334-9ef668b63871 | -16.98086 | -49.32091 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9628f93c-a7bf-3528-a2f3-8ab6eeb2ca5a | -16.21457 | -52.66038 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6f71dabd-9e1b-3dc9-9d64-7c966f533b77 | -15.71519 | -48.96049 | 2025-08-31 04:32:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5368bcc4-16c0-3a01-a8bd-52fc2729f7e1 | -21.13166 | -47.85815 | 2025-08-31 04:32:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7cc05ea-b86f-301e-8e70-83c27c8ff516 | -17.14997 | -46.06772 | 2025-08-31 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b46871f-8890-33f2-b6ae-2598f7db4870 | -18.66316 | -49.09653 | 2025-08-31 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4949d537-4b02-3e8f-a240-ac29bf90bddb | -16.99839 | -49.33173 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e4b42d5-aa77-300f-8fec-59070a614fd0 | -18.6637 | -49.09293 | 2025-08-31 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 24b748fd-f694-3e1f-a787-bff5b489c4df | -16.76896 | -50.29957 | 2025-08-31 04:32:00 | NPP-375D | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d63813c0-fba3-39e3-8753-97c7bcd99904 | -16.33536 | -51.59851 | 2025-08-31 04:32:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e40ae3b-bac8-37a5-aac0-73ee219f7044 | -17.15906 | -46.07612 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56e62966-bfbb-3c00-8d71-3e13095aed5d | -22.17537 | -46.61885 | 2025-08-31 04:32:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b195b61-1e88-3d7e-aef7-cc060a0d0eed | -18.05779 | -45.94165 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1854b94d-36c3-3ef3-92dd-9c261a6fbb73 | -18.05362 | -45.94531 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4aede9b-8c86-3091-8b87-2cc8fc8e2fee | -16.76833 | -50.30337 | 2025-08-31 04:32:00 | NPP-375D | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8e7544-795d-3cc6-9ee6-685c43e30bf7 | -16.21876 | -52.68077 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b350c2f-ebcb-30c0-8731-21218f971d0a | -16.21838 | -52.66108 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| aa4c5b6f-51fe-381f-bfe6-395e516e8b4d | -17.14586 | -46.07115 | 2025-08-31 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6a32404-b1d5-3d3b-87bb-9882caeb99bf | -15.71186 | -48.95991 | 2025-08-31 04:32:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c9f0919-c9ae-3406-8d23-8efb0529fed5 | -16.37148 | -43.03633 | 2025-08-31 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfdbd657-f918-322d-a90c-7b3087611385 | -16.98027 | -49.32458 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29566e2a-32fa-39ee-ad9a-6298641b6821 | -15.30142 | -52.79549 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7083932-f72c-3efb-ad8e-69deba26323f | -22.62199 | -47.94144 | 2025-08-31 04:32:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2b75c33-e892-3171-b75d-cd99dac74e10 | -18.92726 | -48.18158 | 2025-08-31 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4f47736-b515-3e78-9247-c4dc9d58b17a | -16.22599 | -52.66247 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26e88eb7-fa68-3ba5-a716-9862bf47f4bb | -16.2217 | -52.6863 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4f9e27c-5596-392e-97ca-86a3bef108d6 | -18.06791 | -45.94757 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0baae8d-3e67-31bf-9578-3d96db2206fb | -18.05659 | -45.95015 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c7f93fa-40ac-338e-90b4-bc8cd6da251b | -21.6335 | -49.84229 | 2025-08-31 04:32:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41fd23c3-6018-329d-bed1-109b4b30fc37 | -15.2338 | -56.07515 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be97eaee-5a78-3213-b3c6-687cc68daa0c | -18.71022 | -52.92427 | 2025-08-31 04:32:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ba7a518-222c-31f5-9104-907104fc3203 | -16.69444 | -49.32812 | 2025-08-31 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d3b63a3-fe68-32b7-9583-b409baa6ecde | -15.22061 | -56.066 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1f288c1-95ec-3fe2-a874-6cfbc2805a1a | -19.05949 | -49.34842 | 2025-08-31 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9b35bb0-b335-3aee-b799-7f96c8c9c7fb | -18.65983 | -49.09595 | 2025-08-31 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93ec8189-615d-3185-b8c9-862f7b08dd2f | -16.22344 | -52.67663 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9afa65ff-00b4-3575-8635-491054c2cb65 | -14.59057 | -54.54377 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bb35ed9-ac7b-3c0c-854f-0663465a3f30 | -21.43513 | -54.15674 | 2025-08-31 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e3f355b1-efff-3afd-8e87-46104fee857a | -18.06434 | -45.947 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b89fd4b6-c33a-3f46-a8e7-d01251c347fc | -15.29661 | -52.80005 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c97481b-ef0b-335d-b347-fa4cf4710691 | -14.60336 | -54.52403 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aa5a1fa-e652-3dea-90ce-787bad1417cf | -15.71419 | -48.94538 | 2025-08-31 04:32:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fb57c48-8518-339d-8026-c654ca088f50 | -16.53707 | -55.04797 | 2025-08-31 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| efbe7e2f-b7da-3487-bd2c-b16c32218113 | -16.97536 | -49.31246 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b9b7008-958b-3c0d-ada6-30b046bf4b1a | -17.60909 | -52.68681 | 2025-08-31 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d794bef9-bbd4-3b2b-a1ec-af75b5564b63 | -16.23528 | -52.65454 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c498544-dbb7-327e-9294-09717cd23791 | -14.58067 | -54.52396 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51b4cf26-6f1d-39ce-884b-b18663f2cfd7 | -16.22258 | -52.68143 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f221117-6213-3efa-bbfc-f4d75299ffae | -15.21211 | -56.0584 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d2b1a673-1531-3972-84e1-b16a13a5d027 | -20.55486 | -56.25991 | 2025-08-31 04:32:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a51f480b-df47-3f6b-9741-e40146e80680 | -14.59329 | -54.55353 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 781a127d-5903-335a-b249-cbd4a3313495 | -22.03965 | -47.93372 | 2025-08-31 04:32:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c04ecd0e-6efb-3122-abd3-217965f32337 | -16.33176 | -51.59783 | 2025-08-31 04:32:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f281c100-d099-33d8-8395-c686bb51efcc | -20.47844 | -53.67586 | 2025-08-31 04:32:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 961bff91-a469-3ebc-81e8-16e715396c64 | -17.62255 | -44.25555 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33f4e0bb-628b-304b-ba3c-2ac6b21384bd | -18.05956 | -45.955 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c9ca682-5272-3b85-8f20-8c1827a19076 | -15.6881 | -52.74525 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1d26b14-ba74-382a-9399-acf4d9b1cca3 | -17.20604 | -46.07524 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 032dfb24-800f-3681-a9e1-19df277217ed | -17.62185 | -44.26063 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a18dc35-2e04-3f3a-b046-70ed7401f194 | -15.71795 | -48.96468 | 2025-08-31 04:32:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08e5f8ad-951f-30ed-86be-3788964b41d8 | -17.20411 | -46.9923 | 2025-08-31 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6755aad-02ae-3ff8-9fe3-7e4e39fdb318 | -18.5846 | -48.69818 | 2025-08-31 04:32:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1644471-2b6f-34b3-bd5b-1a878c471d8e | -16.97594 | -49.30878 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cfad1ef-938a-3eae-b770-360ec04093b7 | -18.06374 | -45.95129 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc2a3795-7962-39a8-87d6-254dde2c913f | -22.62141 | -47.94544 | 2025-08-31 04:32:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2d95fc07-447c-3d4f-8bad-22732e7f79b0 | -18.43772 | -47.24262 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2788e416-f042-3bf9-b3f7-7bcda74bb0f8 | -16.22552 | -52.68701 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8bf8d4a-0d1d-350a-92ff-d9afdf3a170c | -16.22048 | -52.67126 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e1b8c84-25e4-3aca-b874-3076b287f4aa | -22.21409 | -45.86832 | 2025-08-31 04:32:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1387207e-7109-3b76-a1a1-e20f2f54136c | -17.61935 | -44.24994 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 674b31cf-da2c-3b42-ba4a-d133ca7e267d | -23.02151 | -46.46754 | 2025-08-31 04:32:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20d198e3-8088-38ab-a0ec-f313912812c0 | -17.14764 | -46.08363 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee04f930-a5cd-38e8-a9a1-4e987a53322b | -22.14229 | -46.93954 | 2025-08-31 04:32:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f331a082-bdcd-370c-a7ef-2e7c4d27ec42 | -17.48117 | -46.99948 | 2025-08-31 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8502cfc3-5a32-313d-b16c-23a6c0db2516 | -21.43605 | -54.15174 | 2025-08-31 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc939511-0237-3a06-8ace-e0ba79e7b541 | -17.61547 | -44.24934 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13551007-0f61-3116-9c11-820bd754e334 | -18.12417 | -44.9865 | 2025-08-31 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a662c040-45d5-38b5-804f-54aeca314d56 | -16.98203 | -49.31358 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65f66d8a-0785-3d6c-87f5-cc30774f4f97 | -22.61854 | -47.94087 | 2025-08-31 04:32:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c96953d-f960-30a3-84f2-b8c41e3fe213 | -16.22639 | -52.68213 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 353c31c6-b7c2-3aa6-9f81-82ac9fe7b895 | -22.61796 | -47.94487 | 2025-08-31 04:32:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 69204824-97cf-3f50-a203-3aca6d501615 | -14.60809 | -54.54734 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d08fc7c5-a6a3-33fa-bdaf-dc116dc8791b | -16.21963 | -52.67598 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe2e9a0f-9bdb-3c47-9824-a90a67aee160 | -14.60376 | -54.54619 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README51.md)
