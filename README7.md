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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa92136b-2e15-30c0-8d25-4b43f933e8c6 | -2.01777 | -47.51096 | 2025-11-22 04:44:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa4334d-8a0e-321b-819b-d3bd5fd2f86b | -5.1117 | -40.72813 | 2025-11-22 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e62fbef0-162e-3eaa-b798-65eecc523079 | -1.44615 | -46.8497 | 2025-11-22 04:44:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e881f872-beb2-30cc-83af-66a278e9f173 | -5.57517 | -42.29904 | 2025-11-22 04:44:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5131eae-98a8-3093-8815-8eeb3dd637d2 | -3.17731 | -48.61624 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fc779dd-3f9e-37d6-af89-4d7a17f353f2 | -3.12702 | -44.37139 | 2025-11-22 04:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18aa5bfd-9cd4-3c17-8d9f-c41856bfdcee | -4.12022 | -50.07928 | 2025-11-22 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6ce3ff3-87d1-310c-a265-0adc4f999957 | -1.85511 | -47.47998 | 2025-11-22 04:44:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| c045eac5-718a-3632-b280-104a2a64102f | -3.83987 | -45.3469 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 68ad44a1-9aae-3f16-ac79-4cdbead29e41 | -2.92071 | -48.23294 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 233347fd-195c-335c-80c3-222e23d8ea94 | -3.29116 | -43.91819 | 2025-11-22 04:44:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 819d570c-acb4-3a94-9c7f-ef8406a856ce | -4.04277 | -42.51252 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c7c5ce76-309e-38ce-8e92-c1eef33dfcc6 | -2.93496 | -48.23138 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4894fb9b-0f85-3fce-ab52-32ff961ad673 | -3.83824 | -45.35755 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02d21fde-01a3-3463-be3a-04079c6b80fe | -3.84293 | -45.87809 | 2025-11-22 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7d2bcf8-3627-3c62-a5f0-4a5ddc363278 | -2.89913 | -45.11922 | 2025-11-22 04:44:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1525ab0-d2da-3be8-b293-e690aae35955 | -3.17504 | -48.60848 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| febf154e-000c-3c48-8fa6-bbf4cf923697 | -3.17787 | -48.61263 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2c4979f-6f92-3bee-bdda-f50f6885eb64 | -3.83637 | -46.05116 | 2025-11-22 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce93f0c-8f9c-38a3-8768-e21ffea6089d | -2.54448 | -45.95792 | 2025-11-22 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7181b0b-43dc-3e53-8c15-8c24a469d6c7 | -3.31084 | -44.38517 | 2025-11-22 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3944bb5e-bedb-3012-8fb3-4bc63f3daeef | -3.83476 | -45.35339 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 301f90c3-0a07-3d08-ab46-1217bbea0228 | -3.21684 | -52.45546 | 2025-11-22 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 035f8de4-bcd2-329e-9fe0-242c6ecab08d | -2.64218 | -47.38297 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b26baf16-dc2f-37bc-997c-67ef10c791a2 | -3.2448 | -44.32989 | 2025-11-22 04:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922316bb-be6b-3451-855e-21f044ecd4dc | -4.45248 | -50.69537 | 2025-11-22 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc4e27ac-fe51-39ef-852f-6903c6a7913d | -4.03214 | -42.5165 | 2025-11-22 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7bf30e0-be1e-33ed-9537-aadc6ff3d68d | -3.8353 | -45.34984 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1e689e0c-6b72-33fd-9b42-b17da8c8c77b | -2.69039 | -48.47215 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c99f9e1-b79b-3fea-b7e5-615f4023245f | -2.06815 | -46.56619 | 2025-11-22 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a1b34a8-a948-3213-977e-f8cae17b68da | -3.90818 | -46.13729 | 2025-11-22 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dd48204-d30d-3a0f-a1e2-e53e2556429a | -2.92869 | -48.22661 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 175d24a7-d065-3a94-93e7-eb1fe67ebaf3 | -2.92128 | -48.22924 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| bf75da54-bd6f-364c-ab98-49731a4de3b0 | -2.97488 | -47.76612 | 2025-11-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c90305dd-f8d1-3e25-85a9-de0d84e1417d | -4.11847 | -45.7306 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb4a2e99-b726-3246-8e0a-01cec047a798 | -2.81541 | -45.47849 | 2025-11-22 04:44:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caa9a19f-459e-3faf-bb3f-88b88f3b254e | -5.6731 | -55.75573 | 2025-11-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8828a69-3055-3576-aaff-37e73985ca0b | -6.22311 | -55.64084 | 2025-11-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4308bfad-b7a7-3f37-b2fd-8804ff8910fb | -6.62402 | -55.02191 | 2025-11-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ff70db-5a99-3014-8ca6-fd15739c621e | -12.03981 | -52.54618 | 2025-11-22 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00c7bf6f-d045-377f-9ab7-7af288b85038 | -12.106 | -52.49203 | 2025-11-22 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f6d86e7-6f1f-3688-8edc-ab930e5b7151 | -6.22393 | -55.6358 | 2025-11-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60d1c92d-0f5a-362f-9ecf-ca7d50e0e00d | -16.4668 | -46.42495 | 2025-11-22 04:48:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27051d74-9adf-3c8f-b16e-0dc3f4cc05cd | -17.1718 | -47.23608 | 2025-11-22 04:48:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0efd96bb-6992-3c78-b19e-6b9a2c0920d3 | -20.24882 | -49.33596 | 2025-11-22 04:48:00 | NOAA-21 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bb8897ee-9582-332e-ae74-d9a372ec8195 | -18.7586 | -45.28251 | 2025-11-22 04:48:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d310e974-c223-373d-88f5-ef39c1594c16 | -16.54833 | -52.36455 | 2025-11-22 04:48:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b5ae7dc-a840-3975-ab38-a41b04ecc6d2 | -18.14619 | -46.92387 | 2025-11-22 04:48:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62b39f37-416e-32c8-b4bf-cc54aab93938 | -16.60845 | -47.02088 | 2025-11-22 04:48:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ed3ef1-81dd-3894-83fb-81364ab6b114 | -15.52439 | -52.72592 | 2025-11-22 04:48:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1737cff-f1f6-3ab0-8839-e17aa458a057 | -16.46624 | -46.42959 | 2025-11-22 04:48:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3bff946-4a6d-369f-a7f6-a3424af24e8d | -16.55111 | -52.36876 | 2025-11-22 04:48:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76cc96b9-94d3-3671-be93-9a5b036a43ec | -21.07193 | -43.33287 | 2025-11-22 04:48:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 522277bc-a286-382c-ae85-04fa4182817c | -19.12045 | -46.96674 | 2025-11-22 04:48:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82b44cf0-7a9b-3da8-93d0-3a7337aa2b10 | -19.00595 | -51.48741 | 2025-11-22 04:48:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6335e36-1874-3d9c-a6a8-16568f290ee6 | -17.75209 | -53.80939 | 2025-11-22 04:48:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d842823c-622f-332f-8726-ea75e0653a69 | -20.39451 | -46.46719 | 2025-11-22 04:48:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d016f70-ce5d-31c5-a528-ac44d691eb3c | -20.60314 | -45.50204 | 2025-11-22 04:48:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1e8566b-ca5b-33a1-a4af-496228885a13 | -20.39104 | -46.46793 | 2025-11-22 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 022e5c92-44b3-335c-ac8b-fc0cdf00f1dd | -18.7591 | -45.27792 | 2025-11-22 04:48:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59327d91-1c42-3df8-b963-433d77ea1f49 | -20.40936 | -43.75751 | 2025-11-22 04:48:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 909c2cf1-3eb3-3ded-809c-a2b95f092952 | -17.07162 | -46.59621 | 2025-11-22 04:48:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6495828-6c3a-3e85-8125-bbc1dc41d5af | -20.3957 | -46.46931 | 2025-11-22 04:48:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d95a4a53-dfba-36ef-a248-658f96baed6a | -18.76361 | -45.28316 | 2025-11-22 04:48:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4942df4a-669e-3921-b09c-469de5a9b994 | -18.97718 | -41.02999 | 2025-11-22 04:48:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4b942c64-2cde-31e3-9dbd-e105a4a11ece | -15.15201 | -52.25435 | 2025-11-22 04:48:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd610893-3847-3df1-ba5b-dfedff69f0ac | -15.49119 | -52.8303 | 2025-11-22 04:48:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d34facc3-be44-3c02-8400-503a314565eb | -16.55166 | -52.36511 | 2025-11-22 04:48:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7dc3cb6-49fa-38f4-8793-606812b6134d | -20.25208 | -49.34173 | 2025-11-22 04:48:00 | NOAA-21 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| af73b4d8-9184-3a5d-8485-630828c1930f | -19.85375 | -46.3096 | 2025-11-22 04:48:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32306546-d512-386a-8749-efd41fddec78 | -17.56073 | -54.02919 | 2025-11-22 04:48:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a74ea57b-4280-3330-9b2f-0ecc673148b1 | -18.9767 | -41.03556 | 2025-11-22 04:48:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13bc6e78-7cce-32b6-a50e-a44a99ba646b | -20.25276 | -49.33654 | 2025-11-22 04:48:00 | NOAA-21 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 42014be9-ef51-3b52-a20b-96edb87d11f9 | -15.52108 | -52.72538 | 2025-11-22 04:48:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5359a413-e8c5-3688-9336-c7f911ab2872 | -21.51754 | -42.27007 | 2025-11-22 04:50:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2b04f0a4-ecd9-34df-ab33-e89eab0bf56f | -22.11564 | -54.95155 | 2025-11-22 04:50:00 | NOAA-21 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ddd6b9b1-adc4-3fa7-8314-5b5922733859 | -26.98057 | -52.09743 | 2025-11-22 04:50:00 | NOAA-21 | LINDÓIA DO SUL | SANTA CATARINA | Brasil | 4209854 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02341a95-8d62-373a-bb3a-18e343083412 | -22.92203 | -48.68037 | 2025-11-22 04:50:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7ff7a09-f7c6-3e48-9b0e-2dcf475b3157 | -24.37017 | -49.18406 | 2025-11-22 04:50:00 | NOAA-21 | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d0c154c1-59aa-3ab0-941d-63d9517fa225 | -21.52152 | -42.27032 | 2025-11-22 04:50:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3006dd66-6263-3938-9881-2a5ac07b02e5 | -24.37188 | -49.17798 | 2025-11-22 04:50:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63c8fccf-7432-32c5-9cf4-3a929bf57695 | -22.11369 | -47.01017 | 2025-11-22 04:50:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95e703c3-7371-32f0-9732-fb65b38cf9f4 | -20.8852 | -52.33567 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 299c6561-b5f0-36f1-b7ff-c1e7891b896f | -23.0495 | -46.57151 | 2025-11-22 04:50:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e488316-0c36-3bed-9d0b-0aec48944428 | -23.0476 | -46.5713 | 2025-11-22 04:50:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c266b821-6535-3beb-b4ad-06cbccde0d2b | -20.88749 | -52.3441 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c8c0b89-1016-3ca9-ae05-5f10e91cc20c | -20.88406 | -52.34356 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 264a58e9-0fec-335b-b8a5-d234f6c979e9 | -21.81183 | -45.88826 | 2025-11-22 04:50:00 | NOAA-21 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20a90722-e34d-31f9-af89-0270a198307c | -24.37433 | -49.18488 | 2025-11-22 04:50:00 | NOAA-21 | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de5915de-85c3-3f16-b4b7-fa44652ef248 | -24.37065 | -49.18 | 2025-11-22 04:50:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2919fb0b-ec74-3903-b91d-2cf23dec28f2 | -20.88863 | -52.33622 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| baba7e36-b0ff-3670-90cc-89c44192170a | -20.88463 | -52.33961 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc180eab-59e1-3574-bb3e-80ac7347d5d4 | -20.07469 | -55.38686 | 2025-11-22 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1331fed9-a81b-3840-9fca-907837f99d1c | -21.52195 | -42.26475 | 2025-11-22 04:50:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 03a36502-4991-35f0-81a7-056e88c946cd | -22.03728 | -47.19345 | 2025-11-22 04:50:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9f1c20b-4ef7-3492-8a3f-36fc6093357d | -23.23699 | -51.28586 | 2025-11-22 04:50:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d3783231-d981-3ced-b45f-46364cca5d99 | -24.37142 | -49.18209 | 2025-11-22 04:50:00 | NOAA-21 | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f4405a5b-4c7b-384a-b4f3-452b1fe53a1e | -19.95854 | -54.78111 | 2025-11-22 04:50:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 010318a7-a5be-3b76-b4fb-3b9e490b7a96 | -22.03783 | -47.1883 | 2025-11-22 04:50:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d92d1907-9897-30fd-8766-58559a2766d3 | -21.5238 | -42.27065 | 2025-11-22 04:50:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |


[Clique aqui para ver as próximas entradas](README8.md)
