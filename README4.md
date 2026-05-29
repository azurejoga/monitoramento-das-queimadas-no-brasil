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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3d91286-ad30-3e3f-a213-1a10653d0703 | -11.99539 | -47.15498 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 65774d26-f2af-343e-bd86-c231ca943ff7 | -11.2945 | -46.77024 | 2026-05-29 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb5b8a51-1739-3469-8e4c-a5a830137105 | -10.82595 | -46.88851 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c9c31bc-c9b8-3b63-9f63-55931353dbf4 | -8.20888 | -46.20436 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24cdf400-0687-38b0-8465-e73296346c51 | -10.52135 | -48.10716 | 2026-05-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d85e533-87c4-33cf-9ddd-1995848ca74e | -11.16381 | -46.79961 | 2026-05-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeef55d4-c328-3f93-86e9-c106c76128ad | -9.21411 | -48.59752 | 2026-05-29 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5333fe11-6a5e-3de2-afd2-1eebab57eb7a | -12.45691 | -46.52398 | 2026-05-29 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f12a135-8d82-3ad1-be35-6fa413b14d38 | -10.90964 | -54.12006 | 2026-05-29 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc63cf3c-b03e-3c71-8235-61dba42d49b8 | -13.18655 | -52.70655 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f7074e9-8e0f-35cc-a998-1e7713539a14 | -14.44316 | -48.90721 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25b5c42b-e14c-3cc8-8e32-12aeaf2e3827 | -11.60097 | -47.44284 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e01d57b4-500b-3039-b731-6157ffa4a56d | -8.89205 | -51.85566 | 2026-05-29 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5a0122b-8589-38c2-869b-b6bd0e1b4c7c | -15.78378 | -43.85698 | 2026-05-29 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d91c53f4-86e3-34ed-97c5-94f02ffb58b6 | -10.66099 | -49.7273 | 2026-05-29 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcc808a2-5aa4-3f4b-990d-30b12fe41deb | -11.82991 | -48.21181 | 2026-05-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1224346a-d5df-3780-a88c-1828c52b8b30 | -11.94414 | -43.40415 | 2026-05-29 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57eed562-a750-302c-85b0-b3e62aaa39fe | -11.79443 | -40.08011 | 2026-05-29 04:21:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1d81ded-a48e-3fbe-8894-0ee7fce3667b | -11.56252 | -54.5774 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9acba40b-8899-30aa-b836-19152467f2bd | -8.71907 | -54.99088 | 2026-05-29 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43580445-2695-30c0-bd44-a07d321c8e00 | -11.60157 | -47.43915 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5185cc8c-1197-33c7-a64e-2411871221de | -12.36532 | -54.16603 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c022d74e-f689-3787-8b53-602969fc991d | -13.64175 | -55.75561 | 2026-05-29 04:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb7356ed-bd18-3f00-b17f-f58a1fbc8ce4 | -9.24048 | -40.55837 | 2026-05-29 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ad73483-8aa0-306e-8ca5-8eb1df47cbae | -11.4633 | -46.69515 | 2026-05-29 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95ad4abc-907e-3685-885f-dbc2faa39324 | -8.68722 | -48.308 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8922ba8-60e5-3d88-b3b0-83e8d26c1aa1 | -12.31748 | -47.89779 | 2026-05-29 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca00015-1792-3fe7-8707-9d592109dec4 | -11.63059 | -56.86425 | 2026-05-29 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb2f0bb3-27a3-3997-9dae-7db2622f7790 | -10.66178 | -49.72258 | 2026-05-29 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 432d3b6c-0930-3904-a736-388f0b862bb9 | -13.18215 | -52.70573 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f530370-bd5c-3266-90d2-b0d71abae192 | -11.29804 | -54.03171 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43111470-49b8-3781-a946-80117e1e7845 | -13.11702 | -51.72408 | 2026-05-29 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8a450e5-bd87-3d73-8c3d-f330e152861b | -11.33599 | -51.40166 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 021eefcb-8f59-34a6-84b4-cf59977fd4b9 | -8.49076 | -46.46267 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41b9f05e-a001-3275-8983-47c2f753b22a | -15.24881 | -47.4605 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a29ea0ac-d64d-3e63-bfdd-7ad24388ae90 | -14.41726 | -44.58677 | 2026-05-29 04:21:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f243d00-4bcb-3251-a35f-ae628e1fecfe | -13.18649 | -52.70591 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3489cb50-8269-37b2-941a-501c72fb81b6 | -8.72157 | -47.83094 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cff87458-2120-3aa7-ad88-38fc48bd757c | -8.68654 | -48.31219 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea1eb016-d8c3-3150-8b43-7f311756fb86 | -8.85051 | -46.70981 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8af138d9-2c08-3a2f-b090-a6c5f02ae45f | -13.18134 | -52.71023 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e8cffe6-247c-3d95-875d-8ad26a3037cb | -13.55634 | -46.65057 | 2026-05-29 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d050068-b57e-367a-88e8-8d5a92583ca4 | -10.72298 | -49.03514 | 2026-05-29 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8f16388-ff59-3bc6-a3bb-9a64087009b9 | -10.1045 | -46.5687 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59d1f5cf-6618-33c2-baf6-5efc9f617907 | -10.66105 | -49.72492 | 2026-05-29 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e7dcb53-a0a3-36c6-a843-25eca3f89fbf | -11.44928 | -55.11223 | 2026-05-29 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24d62b5e-0f1a-33ad-88bf-3c620db32945 | -10.48143 | -48.90803 | 2026-05-29 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d958603b-cabf-3606-bc8b-5985bf79cdee | -8.71208 | -47.80075 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c079464a-bea9-3735-833c-13a199fdbd99 | -11.89789 | -47.60585 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4a1e8d-cf92-3e6a-b6cb-fe3bdc22945e | -12.20921 | -47.50154 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 632eae81-a927-32dd-b531-7653f6a69662 | -8.72575 | -47.82751 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 495b04a6-1067-32e7-a644-ea082481d41d | -11.63145 | -56.85981 | 2026-05-29 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb2b773f-fef0-3a91-b75f-852a25df44ab | -12.0097 | -45.35683 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc0c4545-c0a3-3ad2-aeb3-9a8b17cbe82a | -8.84656 | -46.71289 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3762b7b8-01a5-3274-844b-a7073ad2d22e | -8.87769 | -48.4975 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39248952-3f7b-3c8d-a147-293ffd688e92 | -8.68791 | -48.30381 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3561a5e-4816-3d0b-9270-a35720f53598 | -11.56133 | -54.58368 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f834ec4e-6764-313d-bb31-d24df2c2e521 | -10.13161 | -52.40237 | 2026-05-29 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a5d40677-075b-34a9-81ed-c66dcbd7e530 | -11.04767 | -49.60331 | 2026-05-29 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fe2c549-5b8d-362e-825d-fded12780eab | -8.70856 | -47.80019 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95b36aa9-a777-3ae1-8a3b-276018cc100e | -8.84993 | -46.71345 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4026de4c-6d4d-3471-9394-61d35055d2b5 | -10.98642 | -45.09302 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f9a605-0b08-31c8-a4a9-8b12d38d5c0c | -12.2655 | -48.80365 | 2026-05-29 04:21:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71042e05-8288-333f-b384-76aa83913e56 | -12.36408 | -54.16423 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb3efd4-b962-37a4-b6d2-79d52f765f74 | -8.71841 | -54.99448 | 2026-05-29 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0db5b1a-08b7-339e-a8db-87e7d4744aa1 | -12.36423 | -54.17168 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35dc1eea-2ff1-345d-9fc8-1f68429d5733 | -10.97832 | -48.15387 | 2026-05-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fbeac85-360a-3db0-bbb3-e50c52aef8af | -13.63641 | -55.75455 | 2026-05-29 04:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae784c17-2edb-33bf-b54f-ef14a29e1746 | -11.62811 | -56.86245 | 2026-05-29 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02a51d67-c605-3870-8898-ad5aa731cd11 | -11.30355 | -54.0297 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1947b49b-5035-3dee-b5cc-4044d9937f46 | -11.59361 | -47.44538 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 59eb0036-3c55-3134-881e-98fb758dc40f | -8.68362 | -48.30742 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dcb609aa-bbbb-3bbe-a769-144d132d4a7b | -10.82536 | -46.89215 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6095a5-5703-3a8a-ac64-6709ae88dc63 | -11.96739 | -47.37096 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87cb47a8-b051-3081-b884-1956ba23c947 | -11.59819 | -47.43858 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c16e4a40-4cb9-3ff2-97fd-1607e42eb6c6 | -10.98311 | -45.09249 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9302f6c1-82b0-388c-a550-86629b6e1d78 | -8.59535 | -45.93624 | 2026-05-29 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98b94012-f364-3663-9f01-6d892d73188b | -9.22708 | -47.51398 | 2026-05-29 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5a40666-2888-34e1-a9c0-033993c54e92 | -10.71933 | -49.03452 | 2026-05-29 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47cf30bc-090e-31cf-a8b5-6f94c7700007 | -11.47062 | -52.91959 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7f28cbf-b954-3d0f-b5e3-8d8203b68d6d | -15.42072 | -42.02158 | 2026-05-29 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d0a95bde-b6f5-3795-90c4-1899a8025045 | -11.94472 | -43.40023 | 2026-05-29 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d4e4494-d94d-3668-a4de-bd24b3f8be61 | -11.97017 | -47.37518 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c45e959a-cc5b-330b-98e0-00b084cffe7d | -13.18209 | -52.7051 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95801f12-0003-3b23-bcf3-f6d827f88f73 | -11.59022 | -47.44482 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f925a523-ed7e-3cd0-b76a-aba20ea728a8 | -10.13616 | -52.40316 | 2026-05-29 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc888cb0-3cc5-369c-9dd6-89833a55c9b5 | -12.45579 | -46.53106 | 2026-05-29 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce23fcfd-cd81-37d0-baeb-9a73d8fa71dd | -11.29858 | -54.02877 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca6e3243-ba8d-3495-a852-6521a4f324c5 | -11.84655 | -43.96826 | 2026-05-29 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d75cc831-a13e-3a26-8bfa-a6bd69b34acb | -8.71274 | -47.79679 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eeda147d-723f-36d7-a204-ce2ea9a91735 | -11.16047 | -46.79908 | 2026-05-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7f2430a-4910-3c55-b540-73f0d33b2694 | -8.22436 | -49.67241 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c39813bd-a713-3a60-9541-ae2480ecec2c | -12.37002 | -54.15963 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 794071cb-9261-3c61-80b1-8e22b1cd5a77 | -10.14398 | -48.07992 | 2026-05-29 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95220850-44fc-30e2-a507-f3d87d6d32c5 | -11.58962 | -47.44851 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7e76f712-3eb1-3df3-9299-109708fc9042 | -14.44382 | -48.90327 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60655b53-ccfe-33b2-b55f-e834a23cf849 | -10.82142 | -46.89526 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddae7ac-6eca-3216-9cd6-e3a430532ede | -11.58624 | -47.44063 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eed2cba1-cae7-3088-b385-285aad2ff1a9 | -10.86538 | -44.64002 | 2026-05-29 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc5fa76-5182-3640-b29b-8dfea5d6313e | -11.78399 | -52.5156 | 2026-05-29 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
