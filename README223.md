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

## Dados Diários - Página 223

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba432c2b-9e98-387a-9d29-0018665a0349 | -5.95985 | -55.3393 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3df2ebb-009d-31fb-bbcf-ffcdbf15877d | -12.21733 | -57.09933 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3472a656-ffbd-33af-b56b-f8df658bf87b | -6.15738 | -53.3123 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70c17329-d57b-35e5-9b58-dab9377ba9a8 | -6.11007 | -55.72212 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3741604-f10c-3248-af9f-acfe94b11356 | -6.38921 | -55.26725 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b5556521-3ceb-3714-9b4c-ee1313db38a0 | -5.68929 | -53.49416 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9264f2-2d9f-33c1-a200-98de3aa5ca0a | -6.45602 | -55.49006 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc41f737-e3e6-31da-87c1-620d1a69fd34 | -10.3719 | -61.22341 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0abd38-a351-3347-a650-a455521c0104 | -4.51685 | -61.12442 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 385e880a-749d-3109-b079-c73e295ee7cc | -6.49443 | -55.31357 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8113b7d-0153-3a15-a5b2-b996446d998f | -10.38504 | -68.90503 | 2026-10-09 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7236381-cd40-3eed-b71b-bac1e156c922 | -4.12545 | -59.89801 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec8d2111-ef46-38db-92eb-d7f85b31d71d | -12.76879 | -61.45369 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d2b0b2d-8438-3e61-adc9-5eb3fba72cb0 | -10.37131 | -61.22701 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d7d651f-1b68-3a65-9e77-33274d7817c2 | -5.22876 | -60.2411 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 318257c7-477c-3354-819a-bc27d55a78f9 | -6.44568 | -55.05025 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5232ccc3-09e8-3a10-aae9-c179e09e89d5 | -5.69928 | -53.45649 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4e01d3b-01c0-32fd-bd93-d2817d2381e3 | -14.88086 | -50.29544 | 2026-10-09 05:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d6a783e-69bf-3c3e-80af-f258da5dd9cf | -17.82989 | -52.34362 | 2026-10-09 05:25:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1bbf55-f80a-3c21-88de-972c9e6a19a1 | -5.70195 | -53.44823 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b4cafd7-292e-312c-ab0f-c1f1a079b8b4 | -5.69274 | -53.47148 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51e1a4ab-2092-3e2d-99b9-45d97b7178b1 | -5.69698 | -53.48265 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9fed72f-2bfb-3c12-9d93-a4f1cbf1f6cc | -11.75457 | -61.0629 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16b409fc-6bc8-35c0-877c-154dbff8f7b3 | -7.61425 | -46.53962 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d739416-11b9-3d43-a646-13f74a4e061a | -4.11126 | -60.71118 | 2026-10-09 05:25:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1277b075-2bb5-3a57-9e53-0e7ab57e182f | -6.88913 | -45.88974 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b112d1-f838-36f3-be62-0ee216dc0d4c | -5.70885 | -53.48866 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a00d3f73-4b07-3a8d-b0b2-c8e227667a22 | -3.84941 | -61.19365 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88d2262d-f9f8-3a17-95ce-38c03bf84bb0 | -7.18548 | -52.62524 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9956083-5bbb-3036-b5e8-ac614e06ab1f | -5.85574 | -53.45615 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1464b5f4-befe-3dda-8d30-2ac9d024ebfb | -6.87233 | -45.91422 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e426a2ce-e862-3481-a3f8-6cca575eb467 | -7.51298 | -47.32991 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5bbb8ec-f2c0-30d2-89b8-da6d3647c0c2 | -6.44332 | -55.04029 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b584492-f215-365e-9f6b-431c5c8ecd68 | -6.45589 | -53.6946 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 061b5b1d-73d2-37a8-81e6-1a9d45180438 | -10.61077 | -60.48196 | 2026-10-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3049a18a-f2ce-33f7-b118-9fcd6e0b0302 | -6.87863 | -45.91612 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7f1d8eb5-5436-35bf-9ac9-b2ecae849376 | -12.20934 | -57.12898 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 047aab6b-1df9-3aa2-8027-57652bae6070 | -4.12937 | -59.89499 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf81a8fe-d3e6-3229-8fcf-7a7de1e5bd4f | -5.71242 | -53.4933 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b605ceba-b98c-3f87-b129-7db55272608a | -7.6188 | -46.53804 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93faf5ab-8a76-3a88-af34-5f1378df02dd | -7.25145 | -48.06272 | 2026-10-09 05:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17f3cc12-c1bb-36eb-8be1-bce898a215df | -12.21617 | -57.08147 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| c327b06b-559f-303a-b3b6-5628d876bf74 | -6.36065 | -55.15094 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe54d74-6db3-3049-81ee-69a12da8cbcc | -6.00407 | -53.49969 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d12cc11f-bcf7-365a-9e92-6cfcaa5c8044 | -5.71655 | -53.4941 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0e385740-5123-3d98-be97-11e58a13e95d | -6.39364 | -55.2634 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c420f18-9298-3964-bc40-7bd1ec52c8e6 | -5.88933 | -57.72662 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd8f2253-3e07-3e8e-89df-d3a7fed3488f | -5.70462 | -53.44934 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e56f7c7a-3585-316a-8cf5-6a927a978d20 | -4.72926 | -55.66147 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9420d2f-3089-3736-af4a-49551391df1a | -6.48832 | -55.30338 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac628de4-d080-3473-9d4e-a87cf76b7daa | -5.09231 | -56.19878 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e4e5ca8-f363-361f-8eca-c39e8a5f1f28 | -6.19843 | -52.86483 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9436d56b-efde-3568-9372-a5a8de11850d | -6.04884 | -59.9174 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aec0fa7-e9c0-30b7-8b27-7c16b6924935 | -5.70352 | -53.48443 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 89525b5a-d0e9-371a-8b8f-38dd23cf88a5 | -6.21432 | -52.88285 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41d67e2d-5d81-3e4b-996e-8e1d08913acb | -4.74844 | -55.65643 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e22e226d-faf7-33cd-92af-1ee04255d984 | -11.38618 | -55.09292 | 2026-10-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7dec502-0fc3-347d-95ff-f6add383fd48 | -5.95985 | -55.33929 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dce3e074-daa9-38f8-8fbb-15d7c74566a8 | -12.23919 | -57.10262 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10210b06-0fcd-396b-881c-a0e72ffac15e | -5.26264 | -60.18052 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4706813f-193b-3d56-a185-6b757278c589 | -5.69816 | -49.08702 | 2026-10-09 05:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91d26cc1-4d60-382c-9834-5f014e5f6d1a | -4.06429 | -59.83747 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa66caca-90f1-3741-a628-e4c2a4f5c51c | -5.95036 | -55.35155 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00551fbe-e72f-39c2-b9f4-ad26da2932e1 | -6.87247 | -45.90909 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d046365b-966d-3fbd-9807-138fd5862322 | -5.69987 | -53.45261 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eb51634-936b-3914-961f-a6b87f2a89cc | -17.40766 | -52.02076 | 2026-10-09 05:25:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03a90996-e9ef-35e3-95ae-9f81244a3835 | -5.31146 | -55.92852 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6fcfaaa-bc2f-3a31-9900-9aee744218e5 | -5.81654 | -53.86131 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31dfc130-baa8-3b4d-9b47-925ff5e1487d | -11.74954 | -61.07297 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff95e728-54d7-3d69-b72e-1da38b4e7900 | -5.96243 | -55.37165 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9bc3583f-ba99-3954-81c6-e1b1f23c9128 | -6.24282 | -52.83955 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bcd3f8d-2417-309c-ba48-a3cc69f60da8 | -5.92414 | -51.83826 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1dee4c4-2096-387d-a08f-6b7a7f79a449 | -7.02781 | -55.68238 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59493e30-fb62-3742-81f6-af452c16596f | -4.07303 | -59.83867 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2556982c-a91f-3661-ab7d-815f5f9e2226 | -5.92636 | -51.82325 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 923b4347-0973-33f4-bf0c-9050437ba637 | -5.95642 | -55.36146 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77122b4f-fb9f-3e75-bf83-26a5d45a7211 | -6.87426 | -45.89999 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 474dccf5-09fc-3c27-b065-e7fe15540c8c | -6.48288 | -55.28878 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae46c35-7682-31ac-8d26-bd765be03994 | -6.87834 | -45.92204 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7d3b963b-4823-35d1-9b59-2d9080420894 | -5.7017 | -53.46852 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3983df39-b895-3491-8bd9-8576acc99fa3 | -4.13216 | -59.89908 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f3a4dc-35e2-34c1-9c05-50544f864d7a | -4.11987 | -59.88983 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae410ede-5dfc-3e15-b633-a48d68e88ca2 | -6.18406 | -52.87149 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6fade0a-9f24-3759-8eac-27143572e8ed | -5.96356 | -55.33988 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14ef526c-cbab-3327-af73-b74a8dbdb25e | -10.36593 | -61.22637 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1e143ad-0586-30cc-83ee-6117fee5d42b | -6.00049 | -53.49512 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 259a5c1e-f11b-303b-8c79-83c82d542cb9 | -6.44639 | -55.04561 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6969c0c3-dcf9-34ce-bfb8-d56567304eec | -5.23682 | -60.19104 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d851153-851a-3775-bd60-05bfacecbe00 | -12.22264 | -57.13982 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58cbd190-40ad-36ae-9caf-ccfcf712b412 | -4.99139 | -56.99268 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eb9bbe7-8864-36b3-a599-79319bf99ed6 | -12.23065 | -57.11021 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a907e788-36e6-34c9-9b8e-28327ca6ea25 | -11.97217 | -57.62045 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0c8bdeb-4495-3a49-82ec-e2b7e4529886 | -10.6767 | -58.73756 | 2026-10-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e41cd042-6b30-330b-8a74-4c27660a2eff | -6.50211 | -55.38804 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6ba52f9-2a35-3992-a704-d70c406ba23a | -5.25928 | -60.17999 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbda0140-6feb-3db6-8519-6afdf6c99d22 | -6.22736 | -52.79086 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f2dbd35-d5e4-30c3-b1b2-8d762daf8706 | -5.70585 | -53.48001 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21b1aaac-5e9b-3520-9bba-23e1c7b7cfd8 | -6.31581 | -54.80677 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6018ab7b-f2e1-37ff-aff4-8709f25ef352 | -5.22006 | -60.04591 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 551fae47-d6b1-3000-a0ff-894aed91aeac | -6.11202 | -55.70948 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README224.md)
