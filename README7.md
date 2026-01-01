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
| b9fe07eb-5fe4-37bf-a24b-8aa3f33e08d1 | -19.37176 | -54.59908 | 2026-01-01 05:40:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c70b1a1-53d1-318f-ad40-ddf77f4f9333 | -19.37461 | -54.60388 | 2026-01-01 05:40:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f51ecdc1-222a-3cc2-86e1-80c531e0ded2 | -19.37506 | -54.59845 | 2026-01-01 05:40:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88cb1c58-db9a-3abc-9835-9027cc9562c3 | -17.70551 | -53.27423 | 2026-01-01 05:40:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f862679c-fbf7-3e99-8c37-2430635d64ea | -9.5821 | -44.6007 | 2026-01-01 05:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 4251486c-d02d-3dee-a12d-837027481c45 | 0.682 | -59.55802 | 2026-01-01 06:03:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e65fb4d3-06d4-3d0b-b8ac-ae8e6be2aecb | -6.5631 | -51.1126 | 2026-01-01 06:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 4ab5eb74-6884-3881-b70d-129669571bcf | -3.86337 | -54.22908 | 2026-01-01 06:56:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 88c005b6-7f92-3c8b-a8b6-924f84523247 | -14.64078 | -55.8218 | 2026-01-01 06:58:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 01652ca2-1ead-3604-b9f6-0cc91ced872a | -19.36553 | -54.60342 | 2026-01-01 07:01:00 | AQUA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 26.7 |
| be4576c6-5d05-34d9-b964-d2f14c833d9b | -19.36809 | -54.58116 | 2026-01-01 07:01:00 | AQUA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 90021da4-e42b-3af2-9e2f-c46fbfc83335 | -19.36589 | -54.58627 | 2026-01-01 07:01:00 | AQUA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3d46f6cf-36ec-3771-92c9-75a8d1793f03 | -5.2256 | -37.72982 | 2026-01-01 11:34:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 83b3c957-4e7a-310f-9576-5643e1ad4969 | -6.20692 | -37.44024 | 2026-01-01 11:34:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 82c30a07-5666-3193-b8c8-29cfb6c0542b | -4.65915 | -37.69555 | 2026-01-01 11:34:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 14138d6d-969d-3e8b-9a25-32d9821ced4f | -5.17259 | -37.06448 | 2026-01-01 11:34:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 65d9b7aa-14f0-3fe2-b8f8-01946a192fa9 | -2.33569 | -44.89494 | 2026-01-01 11:34:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 9e56cefc-8f4c-36b4-8a25-a6c4f945c866 | -5.17391 | -37.05524 | 2026-01-01 11:34:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 10b2b229-35bc-3f43-8675-04f3ba259bd0 | -6.20562 | -37.44939 | 2026-01-01 11:34:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 896170c4-0a1d-3096-ae00-93da2263d0eb | -9.26059 | -41.00688 | 2026-01-01 11:36:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 201c2081-58c2-348b-8300-a42f0901660c | -11.4037 | -39.53385 | 2026-01-01 11:36:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d56fa143-77e0-3ae9-90ce-ca6690b407f0 | -10.70555 | -39.44791 | 2026-01-01 11:36:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2406a68e-826b-3f74-8e76-a44539837e6b | -9.26979 | -41.00822 | 2026-01-01 11:36:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d070d196-10eb-31f7-b21c-262186a93a75 | -9.19298 | -37.76388 | 2026-01-01 11:36:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d43fa3c2-8671-3102-b147-f6254d976edc | -12.42275 | -38.70941 | 2026-01-01 11:36:00 | TERRA_M-M | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 125a3761-2622-38e8-8e21-7eaf1c0fc1fa | -9.23188 | -36.74842 | 2026-01-01 11:36:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 004655c7-d140-3a40-a661-2b243798a6c3 | -11.41255 | -39.53512 | 2026-01-01 11:36:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 34.9 |
| a312eb48-a5f9-3452-897e-d0d4e3f6e924 | -11.39517 | -39.90739 | 2026-01-01 11:36:00 | TERRA_M-M | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6f0f8b53-de65-3ac7-ba35-f1a11c22b3c0 | -10.38113 | -40.16589 | 2026-01-01 11:36:00 | TERRA_M-M | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f673cfbc-a6d9-392a-900d-fa2c94f92d6a | -16.7357 | -39.87243 | 2026-01-01 11:38:00 | TERRA_M-M | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 664865b2-23f3-316b-975c-e9f9f13b46b3 | -16.73437 | -39.88198 | 2026-01-01 11:38:00 | TERRA_M-M | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| ef60c716-db1f-3927-bfea-a9759f3efb00 | -22.26653 | -42.75994 | 2026-01-01 11:40:00 | TERRA_M-M | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 1469c339-ce7e-37ff-b2e4-255d459e4cc6 | -2.7678 | -42.5725 | 2026-01-01 13:50:00 | GOES-19 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |


