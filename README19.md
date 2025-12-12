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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0225f75-6268-3c9b-bc38-df4a2094e983 | -13.57819 | -49.77792 | 2025-12-12 04:23:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d60e354-7a28-3953-a67c-c592b1dd672a | -12.4098 | -58.04758 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| adc340a5-2556-3281-9a9b-97ca2fc8be08 | -12.38606 | -58.03735 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 639e7821-175b-3b0b-9c06-e23c6bafc5d4 | -19.58387 | -43.96609 | 2025-12-12 04:23:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2a236bd-0885-3d08-b48a-b75b81e992c7 | -12.19665 | -49.53904 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd7d3fdc-ca8d-3110-bfe1-0ec46461e068 | -12.38026 | -58.04334 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e1ca3d68-bb71-3157-a2c8-f88a2d3b9835 | -10.2374 | -52.21937 | 2025-12-12 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df1cf444-f873-3877-a352-2ac27e32591d | -8.09685 | -55.01381 | 2025-12-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1cf43c3-b7b4-31a8-b170-ef03c7c68821 | -20.53784 | -41.82883 | 2025-12-12 04:23:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d2e4b9d-d8c6-3133-ae74-967a13364470 | -11.32112 | -49.19518 | 2025-12-12 04:23:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e77bac49-e9ff-359a-b9f5-f3187bb94d83 | -12.5112 | -58.36414 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f843212-3a3b-39e8-b10f-528e4b8b5f94 | -12.41187 | -58.03752 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 11c06a4a-d38f-35fd-a99b-82ad25ff0b0f | -12.41703 | -58.04386 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 93100d13-53b8-3bb9-8f0a-dbcbf2228c52 | -12.62232 | -58.09452 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f7bc3d1-da58-3180-8ea4-0e614ab35440 | -12.42426 | -58.04007 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 132a174e-e05a-358f-bbdf-96bbfdbc8911 | -12.41083 | -58.04258 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b15b98f7-351c-3ba8-abc1-76cf9dc81885 | -20.47937 | -42.25924 | 2025-12-12 04:23:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 78319ea4-5180-3aff-9227-e565c585988a | -12.40607 | -58.04345 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1d75bb34-5a94-38a6-a3dc-912daa915bb6 | -12.38749 | -58.03951 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b24758d3-1dbb-3b19-9eb2-f5aa61b699a2 | -20.38358 | -41.3354 | 2025-12-12 04:23:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4111944-487b-321c-8106-0dfefb92b1f8 | -12.62338 | -58.08942 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09b96ce0-c76b-3c1d-92bc-7c49dea1ad61 | -11.46524 | -48.16392 | 2025-12-12 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0f4f6c9-f03b-3422-93fb-da19e60574cf | -11.89019 | -43.70449 | 2025-12-12 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec3bf3a0-1777-36fa-ad42-ae3dff0fd8c3 | -12.63161 | -58.08081 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6a32bfe-3597-3222-8ee3-67c2a736ed2d | -10.88551 | -54.14019 | 2025-12-12 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6882e1f2-024f-3e58-b4cb-1371e024a5b3 | -11.02383 | -50.53217 | 2025-12-12 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca1e4dfe-0095-3b4e-aa5b-69e4bb505c5c | -12.38647 | -58.04458 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 014b9400-077f-38b2-aa3a-e80bb5ba4a67 | -10.23664 | -52.22372 | 2025-12-12 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf79ac56-7006-3e67-9b15-0c57f89bc448 | -12.25594 | -38.24688 | 2025-12-12 04:23:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 100ced08-399e-36f4-8b6d-2d71120dba07 | -12.40361 | -58.04623 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 92903498-6a19-30aa-9f22-c2b4343bbb34 | -12.51446 | -58.34814 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17ad5fe0-d2cc-340f-9698-2c25cce53f7c | -12.51338 | -58.35346 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5f13f11-b9a5-3ba2-9616-ec55a5f1c62c | -11.87557 | -57.01854 | 2025-12-12 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62e0bb33-151f-3846-bfc6-4c34a99803df | -6.55883 | -56.14178 | 2025-12-12 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5814a11d-7584-36f3-856f-7c3a9c4de2e7 | -20.95951 | -48.76854 | 2025-12-12 04:23:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e883d8d-6a71-36eb-8e7f-28c7fc3290b4 | -12.39226 | -58.0386 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a08ccef8-436b-375b-9ffb-20879d371957 | -11.32015 | -49.19665 | 2025-12-12 04:23:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28f14376-fe09-3421-b7cc-422c2b960b42 | -12.38128 | -58.03827 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2165b46-011c-32b2-88cb-36def95d4004 | -12.39989 | -58.04207 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 92556fac-7d7c-3251-8c1a-43356845b53b | -6.55966 | -56.13723 | 2025-12-12 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f5bf4c7-1f99-3af7-ab4e-87ec7eb5378b | -12.20319 | -49.54471 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db51dc14-67b6-346f-9ddc-c0c2e2a1ceb8 | -12.39268 | -58.0458 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| adf509f7-4961-3dcf-b7cd-5970239a754c | -12.19955 | -49.54406 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e858b84a-b522-3880-a7cd-aa77e4ea5fe9 | -12.3788 | -58.04117 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ab704606-db18-352e-974d-4fa68b7e9d1f | -12.70278 | -48.79691 | 2025-12-12 04:23:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3693f34c-5cfe-36d4-945f-b98ce168d6ad | -11.31751 | -49.19451 | 2025-12-12 04:23:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e0b9401-1a15-3686-b4d4-2319b38d7103 | -12.40708 | -58.03838 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1de1a760-4761-3026-8ec8-fbb51eb56d62 | -12.506 | -58.35742 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc104983-7b17-396d-aaca-6985cb428d93 | -19.71517 | -49.20115 | 2025-12-12 04:23:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d4752d2-81dc-3e04-a5b1-30f4b8e68630 | -10.98826 | -54.00066 | 2025-12-12 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4d1fdfa-3dfa-331c-b8ce-21a2de902d0c | -21.33287 | -44.95063 | 2025-12-12 04:23:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| edb5f1c8-5bac-356d-9089-806605232d47 | -12.42323 | -58.0451 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9f73e23a-f407-3197-83cb-de33586efd14 | -19.86735 | -46.56019 | 2025-12-12 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee69856d-1cfc-3e10-8615-4d997cde76be | -11.3204 | -49.1994 | 2025-12-12 04:23:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09c0ff88-4064-3fda-8604-3f25492c0be0 | -20.77456 | -54.41833 | 2025-12-12 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010ab3cf-2288-32cd-9344-44ebaf8e03b2 | -12.43047 | -58.0413 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9427e8b3-8b8f-3dc9-9960-248aa3bafb55 | -20.54003 | -41.83176 | 2025-12-12 04:23:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18f1cb0f-2fcf-3e85-b1c8-309fdfcd62cd | -12.01 | -47.79539 | 2025-12-12 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d375237-dbf3-3636-920c-f0b4d733e6a3 | -10.73573 | -52.44448 | 2025-12-12 04:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 037d7154-0fad-33bf-aa20-0dc443d2757d | -12.4009 | -58.03703 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3321454b-87e6-3b52-81f4-ad0d535c732e | -12.39369 | -58.04076 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 03341f1c-be67-3b10-ba9e-adabcf0e0c99 | -12.20973 | -49.55037 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b19d1d33-5fd2-3c46-a6a9-b02aba45713b | -19.55951 | -49.50171 | 2025-12-12 04:23:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ea3a873-03b3-3749-91db-d321fd90538e | -19.30096 | -46.09126 | 2025-12-12 04:23:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73cb6a8a-1d58-3535-897f-b5fc81128969 | -11.02295 | -50.53722 | 2025-12-12 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 958bdeb6-ab35-35e6-beac-d9309251950c | -20.38403 | -41.33773 | 2025-12-12 04:23:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a41021d8-7800-3022-8b36-b9886467c837 | -18.6931 | -42.9637 | 2025-12-12 04:25:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3b9e5ce3-9399-32f3-ad3d-721e32b1ea09 | -14.90253 | -58.13285 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| adc54739-b4ac-3902-b17c-28445d97c8e9 | -14.91744 | -58.15089 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4846c81-a4b9-3638-8b2b-5ca4c66a88a8 | -14.91241 | -58.14518 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93b82953-885f-3b39-9331-9135fce7755d | -24.70651 | -47.79298 | 2025-12-12 04:25:00 | NOAA-20 | PARIQUERA-AÇU | SÃO PAULO | Brasil | 3536208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| de2f01a9-c50a-3731-9f00-6582d3418940 | -22.68371 | -46.88171 | 2025-12-12 04:25:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db7cd073-f975-358c-992e-2b3db2bca8ca | -23.61021 | -48.34597 | 2025-12-12 04:25:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c0e19eb9-2c0b-3357-b3a6-069fd1028e29 | -14.89756 | -58.12688 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7431c7f1-7e06-398b-9cf1-70c7db053d7d | -22.73083 | -49.34977 | 2025-12-12 04:25:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56f3c6e1-7df2-379a-859f-2d19af313ec2 | -23.49888 | -45.93686 | 2025-12-12 04:25:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb242e9a-19c7-33e4-ad75-101d9b173f0d | -15.97381 | -56.28101 | 2025-12-12 04:25:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3f7c6716-d788-3b74-8b46-28a4260b909e | -18.4522 | -44.49072 | 2025-12-12 04:25:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a35763e-8310-361f-b961-5bea3a42257d | -23.50242 | -45.93745 | 2025-12-12 04:25:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3b62fbb-eb49-342d-be51-2fb5c511892c | -14.90352 | -58.12813 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 23725865-483e-3651-a9d4-ec9b4a742c9b | -18.69244 | -42.96877 | 2025-12-12 04:25:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 298cd757-f6d7-3651-a619-b15354501118 | -14.8966 | -58.13144 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f81fb6ca-ac90-3c85-b0ca-d383fba35a8a | -23.3003 | -45.6506 | 2025-12-12 04:25:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3d37f0e0-16d0-3fb6-8693-25f158d009d8 | -16.09944 | -56.76318 | 2025-12-12 04:25:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc72cd2c-7609-3c39-ac1a-48a333f0fc52 | -22.95262 | -48.70737 | 2025-12-12 04:25:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 317fc17d-9fc4-33a4-a403-2190deffbc48 | -23.4059 | -46.42259 | 2025-12-12 04:25:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63918154-7468-3503-8c99-9b1428e81fa5 | -15.97315 | -56.28432 | 2025-12-12 04:25:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 58859bdd-54ab-393d-a4c7-c60edcb1eab9 | -25.72858 | -51.11051 | 2025-12-12 04:25:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 94c24b28-dfbd-30ef-8bed-49accfe7ccaf | -14.91144 | -58.14978 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91b00c5a-8e87-3eb4-8463-a89fab9f6749 | -23.30451 | -45.64651 | 2025-12-12 04:25:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 998fad50-1832-3f96-b1e2-9d9d4218174a | -14.90448 | -58.1236 | 2025-12-12 04:25:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6ca351f0-7d3d-317a-8ec6-7538d8f83ead | -23.30389 | -45.65105 | 2025-12-12 04:25:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 07c9fc83-952b-3433-9613-b3adb5a4e7c8 | -22.70123 | -43.35318 | 2025-12-12 04:25:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c4a00e3-dfa5-39fa-92b8-dfa347cf2b22 | -14.9134 | -58.1263 | 2025-12-12 04:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ff67d300-a925-36d7-be59-ae9f780e6a08 | -2.4183 | -51.9278 | 2025-12-12 04:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 5cfff6d3-7fce-39dd-b0d4-ad834467a727 | -12.4325 | -58.0276 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bcadc30a-d092-3fe4-8837-bd9c4ab27068 | -12.4323 | -58.0475 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b1d3b10d-36ec-33e6-96ab-a18de3130039 | -2.4367 | -51.9274 | 2025-12-12 04:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 1b30bfe9-9031-36d6-9786-8d54f6185f2e | -2.4923 | -51.8027 | 2025-12-12 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 93fc684a-d9f0-327c-b760-4a4f8b3e6dc1 | -2.3566 | -54.3631 | 2025-12-12 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |


[Clique aqui para ver as próximas entradas](README20.md)
