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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 135347a6-c5f4-3c66-8e05-697f5d2b7f0f | -12.34875 | -53.15286 | 2026-08-09 00:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 436e714d-acd6-3eab-9bca-c7d5e551a42e | -12.3293 | -53.15549 | 2026-08-09 00:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 41a960ea-2d3b-3305-8a9d-0e34f1c93fd3 | -7.68668 | -49.51966 | 2026-08-09 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a634b876-d0d9-3408-9086-27e2fa366c3c | -11.0579 | -50.56538 | 2026-08-09 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4b3d2578-af82-3bb4-9969-c068592798b2 | -6.77841 | -46.46586 | 2026-08-09 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8e50450d-7db1-3da5-b338-5e9e94ed6ea8 | -11.04679 | -44.26834 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 0a227aff-1648-3c1b-bc55-79ad3aaf391a | -11.03826 | -44.28295 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 2d168f14-4e6c-3e89-a50b-2ecd7028095f | -12.11087 | -47.22398 | 2026-08-09 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e161ab7-9829-335d-b897-a05c21d8b360 | -2.96352 | -49.25581 | 2026-08-09 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| a24d9eeb-da7c-3b63-93ed-a5bcd366193a | -3.59259 | -53.30886 | 2026-08-09 00:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 44c1e75f-f754-34b0-9989-1d57636a62e0 | -6.94344 | -51.9291 | 2026-08-09 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7625824c-99ab-3aae-9e77-b8d876182688 | -5.73262 | -49.14319 | 2026-08-09 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a8bd3dd0-7326-3303-9772-7cc6d18461c3 | -1.8349 | -54.66493 | 2026-08-09 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f2770ccc-a5a7-3b33-aafc-994fe1c6b2c2 | -2.35022 | -47.64265 | 2026-08-09 00:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cf82ba07-337f-31ac-9ad7-92891126e0cf | -6.69388 | -51.92789 | 2026-08-09 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5d9d4bc4-48f7-392e-9a69-1a259350f3eb | -6.1334 | -57.70977 | 2026-08-09 00:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 3ab43bf2-812d-3585-af1b-d0b5ba920ddf | -2.9651 | -49.26688 | 2026-08-09 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ebdf8d08-7579-3371-874f-076e3c602627 | -6.50639 | -51.43027 | 2026-08-09 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3446f617-eadb-30bc-a74b-9006815af22a | -6.4188 | -55.78115 | 2026-08-09 00:13:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e8b3c8c9-ea79-3a69-902b-e200aae24983 | -6.41534 | -55.78792 | 2026-08-09 00:13:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| d65eb393-c8c3-3ddd-835e-60aa5901f684 | -4.46047 | -47.91821 | 2026-08-09 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c80ee64-39e1-3246-9f96-9f12c64124b7 | -5.73112 | -49.13271 | 2026-08-09 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 933af326-d673-39a2-a4fc-29e501080a6d | -4.10189 | -49.2743 | 2026-08-09 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 20a15b52-bfed-3467-8673-6dbc61bd7e8a | -6.14999 | -57.72037 | 2026-08-09 00:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 94eb2f58-fbb7-3b6e-ab65-fd156be22913 | -6.71117 | -58.94506 | 2026-08-09 00:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 16364c4b-b81c-3cd1-8be8-d72e8ef46c44 | -4.52259 | -48.05292 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 405165d3-44a4-3bc6-a47f-38d7c219fb07 | -5.88655 | -46.50355 | 2026-08-09 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 8a33a739-fe85-3c5b-a4cf-97cde7ca9f0b | -6.42051 | -55.79461 | 2026-08-09 00:13:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| a3cb7a0e-08ef-3e87-9233-d72c9652bf6f | -4.26685 | -48.1988 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 8bf8d64e-b801-37ce-bc4c-2b1d40acb736 | -4.26509 | -48.18629 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 0577d2f0-e72f-39ed-8504-c7e1cce60a60 | -6.71638 | -58.93913 | 2026-08-09 00:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 00f22420-edb5-3734-9fa2-d188372d754f | -6.13746 | -57.72193 | 2026-08-09 00:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| f6ea3963-301c-3ecd-83de-6efd0a9ef993 | -6.94223 | -51.92024 | 2026-08-09 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f1853b0-66b6-3537-9fff-b94c22a4f173 | -6.87836 | -58.93667 | 2026-08-09 00:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 2a60c369-a37c-3529-8709-790d068c667f | -4.27742 | -48.56745 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| eb953a71-cb80-332a-ac10-55b7d567240c | -7.31499 | -55.11346 | 2026-08-09 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 57317345-8dce-39a8-9be8-d9a1cc9a4e15 | -5.02841 | -56.1314 | 2026-08-09 00:13:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4675aad3-005a-320f-a357-b2741f824f39 | -6.83634 | -58.94207 | 2026-08-09 00:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6ff5d2e2-2477-34cb-a942-1d3d59347e0e | -6.60781 | -56.37163 | 2026-08-09 00:13:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 446dc7d5-2a34-3762-a762-9ac0a72a04d5 | -4.27328 | -48.19148 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4bc7003c-e4ed-3f95-ae8f-9178545485bd | -4.10037 | -49.26358 | 2026-08-09 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 68e0f365-f333-350e-892b-341caec9395b | -5.87791 | -46.5111 | 2026-08-09 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 51c583d6-6b27-3560-bd6a-5788ccf1cc9c | -5.36731 | -49.16741 | 2026-08-09 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 657688b2-9417-3893-b0ec-025ba93ebcf9 | -4.11154 | -49.27284 | 2026-08-09 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f38c8966-de6d-3ff2-8d8e-310aca9699b3 | -4.30086 | -55.73048 | 2026-08-09 00:13:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4d798c49-a5e1-398c-8518-d81efdc56a3c | -5.87565 | -46.4954 | 2026-08-09 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2939217c-cdaf-32e0-8716-308586881a6b | -6.13589 | -57.72849 | 2026-08-09 00:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 79f4eda9-7660-3355-acad-02d57eed0dca | -4.27573 | -48.55562 | 2026-08-09 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5e726219-f769-394d-aa58-117000fdc631 | -5.02665 | -56.11793 | 2026-08-09 00:13:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| df45b1a7-e631-3bb7-911e-bdca2ced1144 | -11.0334 | -44.2696 | 2026-08-09 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 75f351bc-22dc-3970-8a5c-80b18d9af40b | -18.4154 | -50.6269 | 2026-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 631be839-885b-363b-843f-453ade494711 | -8.6856 | -62.874 | 2026-08-09 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4a3778bb-01fa-314d-bd5b-44a774498a85 | -11.0526 | -44.2668 | 2026-08-09 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e4840782-697f-3a35-9d35-4d4154982d6e | -18.4354 | -50.6233 | 2026-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| b8465af7-7a4b-370f-a65f-1089d3ea2319 | -18.4359 | -50.601 | 2026-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 113.6 |
| eb9448f5-961a-3a13-8511-ec9ce5eb880f | -14.3485 | -53.3504 | 2026-08-09 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5d791863-be0a-3281-a44d-15d2f75e3cbf | -6.1476 | -57.7215 | 2026-08-09 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8e910fa1-0cc9-344f-b8c0-f8cfecefb5ec | -18.6327 | -49.8742 | 2026-08-09 00:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| e79986c4-df04-390b-9bfb-29733b934f73 | -18.4159 | -50.6047 | 2026-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 811c4230-6f86-3772-9d05-d70ae773e80f | -18.6528 | -49.8703 | 2026-08-09 00:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| bb7574f6-49a9-3a7f-90ce-6b2d641735d1 | -6.1292 | -57.7223 | 2026-08-09 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 17760286-67aa-3873-9982-adec9895f022 | -18.4359 | -50.601 | 2026-08-09 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| e48b695c-9f71-3e57-8ae3-acd382deb543 | -18.4354 | -50.6233 | 2026-08-09 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 179635a7-4dbf-3d4e-aa75-010f9e14bb56 | -4.109 | -49.2807 | 2026-08-09 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 43035470-7991-3234-b180-2fdec2ef6f4f | -18.4159 | -50.6047 | 2026-08-09 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b7533f0d-6872-3dc7-a515-3e2d87c9d524 | -8.6856 | -62.874 | 2026-08-09 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c9d30b14-c954-3793-a773-6370150b6da9 | -11.0526 | -44.2668 | 2026-08-09 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3e671749-8393-3856-957c-5b26d753e15f | -11.0334 | -44.2696 | 2026-08-09 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 2d75eecd-2c12-35c1-baf1-85237c933128 | -18.4154 | -50.6269 | 2026-08-09 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4b3ff40a-69c9-3a2b-9bfd-cf440a3a902a | -6.1476 | -57.7215 | 2026-08-09 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| dcda65fb-d96c-3f99-964a-250dba61dd2e | -18.4154 | -50.6269 | 2026-08-09 00:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f20405cb-71db-301f-a194-386704f88b10 | -18.4159 | -50.6047 | 2026-08-09 00:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 7361a1e6-4b40-346e-821a-60debc4c3bba | -6.1476 | -57.7215 | 2026-08-09 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 82317e5a-9043-384b-82f6-2e1c610d6dce | -18.4359 | -50.601 | 2026-08-09 00:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| 67caafb1-6b7a-3274-afb4-60e86076779d | -13.9541 | -58.1162 | 2026-08-09 00:40:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d1227a3e-caf7-3fb2-8c6e-8982d4d9e81d | -11.0526 | -44.2668 | 2026-08-09 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 6f314bf8-f3bd-3505-843b-3645f6d4c080 | -4.109 | -49.2807 | 2026-08-09 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a8de6fe6-17cd-31fa-b740-cf60029f6f55 | -6.1292 | -57.7223 | 2026-08-09 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 678301ef-4cf0-3f95-a313-1dc932750d62 | -18.4154 | -50.6269 | 2026-08-09 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 452.9 |
| 5cd73daf-6a65-3889-bc6b-95338e81fe5d | -18.4164 | -50.5824 | 2026-08-09 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| df38337f-1890-3e39-ab13-ad3e63491346 | -18.6528 | -49.8703 | 2026-08-09 00:50:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| f6e36995-e1af-3d8c-b3b1-369ba0df469e | -18.4354 | -50.6233 | 2026-08-09 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 175.3 |
| cec200a6-749e-33b4-a1b4-f39d633ca6ef | -18.6327 | -49.8742 | 2026-08-09 00:50:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| a5031b48-560a-348c-97d3-31f5e11c09ef | -18.4359 | -50.601 | 2026-08-09 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 205.6 |
| d9c893af-fbd9-3714-927a-6e6c5240c2f6 | -6.1476 | -57.7215 | 2026-08-09 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 798b5556-665e-32e3-8a65-4badd66fdeaf | -6.1292 | -57.7223 | 2026-08-09 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6606c618-a10b-3340-88f9-b82deeffb574 | -18.4159 | -50.6047 | 2026-08-09 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 482.1 |
| ef05f122-bbc6-3531-80d4-841878e85f02 | -18.4159 | -50.6047 | 2026-08-09 01:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 42482a67-3dfe-3894-b2b2-2259eb95cf1c | -6.1292 | -57.7223 | 2026-08-09 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1a297f95-0c8d-3cff-850c-b2f42936744c | -6.1476 | -57.7215 | 2026-08-09 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 49069353-bb7b-3bf5-a4d6-7a11a329b99c | -13.9541 | -58.1162 | 2026-08-09 01:00:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f034ff96-7c90-33aa-9b62-b7d08d69825f | -13.9733 | -58.1144 | 2026-08-09 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 789163a8-e4c0-3c67-af2a-6478ccd0dbad | -21.986 | -56.0051 | 2026-08-09 01:06:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b98102ff-99dc-393c-86fe-ecebaa174d7b | -13.945 | -58.117699 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc009421-083f-337d-8a9a-5da891b54459 | -6.1374 | -57.7005 | 2026-08-09 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 152efb28-36f8-38a2-ad84-d34eafb8c782 | -11.4147 | -61.4767 | 2026-08-09 01:06:00 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7cac6d-86f1-3153-8793-e761abf4d3ec | -6.8163 | -56.417198 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3cd9c63-069d-35d1-9663-dae554a1b56f | -13.9331 | -58.111 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6650518-96de-3f19-8160-295119734ea0 | -9.3329 | -63.437099 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb5b960e-8b24-38c8-8eaf-ccdd76822825 | -13.9504 | -58.096901 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
