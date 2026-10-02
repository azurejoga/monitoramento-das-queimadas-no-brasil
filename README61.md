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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da836817-9b1e-38e2-b5ad-b157e2626374 | -7.34004 | -55.57677 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3344a217-0059-30d3-93ac-990400444c01 | -6.24231 | -53.14922 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6741a156-d7bb-347d-b48b-eccebe2df000 | -7.57067 | -55.02065 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 126e8c2c-bd54-3b01-963b-7ff4cab94783 | -3.02126 | -53.89114 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8ec32d7-6b9f-30ad-8611-e39fed941de7 | -3.14285 | -53.74551 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd9fdf5d-8f60-3bb3-bca6-bd764f3a57c1 | -2.92814 | -54.15829 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02b48b35-922b-38db-8510-5ce1a244a86a | -3.58162 | -53.45936 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0779fe7f-dfa6-3ddb-af87-0dbeb87f87e3 | -6.5277 | -55.05378 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 757f06f2-f034-3a50-8da2-fd32f24d2154 | -6.40183 | -55.24745 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b751fb8-c057-3c7a-a465-fec6c9934fa8 | -6.52673 | -55.38274 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2065b562-5a8b-3b56-bd5d-144faa09b6fc | -6.13882 | -53.28902 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d20d7c58-f363-3f82-8fd0-36958590d78a | -4.07739 | -50.32717 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c5e0265-a31e-3b1f-bb4a-3f5684448a8e | -7.74169 | -54.79605 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dc6ecda-9306-3b18-a4ec-952f6676365b | -3.29005 | -53.8457 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 800469b1-d857-30f1-a1ba-82150188ed32 | -7.55307 | -55.025 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd8cb3f-6950-3d35-82f1-c5434c6a0e6e | -8.1841 | -54.79528 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3e29668-cb0c-3d96-9de2-515ec69c1317 | -3.53879 | -55.53145 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d5638fa-1374-3d6f-95d9-9f26df70d043 | -6.20479 | -53.25947 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d2bae9d-2f38-3b60-ac9a-1223ddb549e3 | -3.13189 | -53.75084 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c91be359-3941-331d-ad93-e2c7b80be952 | -2.93475 | -54.15931 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26770ea9-65a0-308d-9dad-5820846e9be1 | -3.13626 | -53.74449 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 43961662-43bd-338b-887c-cc20bc2f1106 | -6.24785 | -53.13548 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73337ff3-2265-3502-b210-2f6109f1c718 | -2.85372 | -54.13622 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc0126e8-5320-3898-a7b0-4cb09d223f3f | -4.29366 | -49.09236 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e7d386e-eda6-3d7e-8d7e-8a7763622fde | -9.52804 | -45.34065 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 940317cf-eb69-3bcf-a181-913d8bb48d92 | -4.3178 | -50.78809 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0d474c6-fb57-34d0-b47c-69bd31fb24f4 | -3.12539 | -50.28321 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e9f09c4-65b5-357f-bcfe-afef677998e9 | -1.4617 | -48.90681 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d7772f2-9440-3548-8043-539a6e1e7a70 | -7.54923 | -55.02794 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd3e2d5-da60-316f-b04a-d69b502dbdc4 | -5.92564 | -53.48169 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30f38ccd-4e20-3361-8386-573267fd0305 | -6.76068 | -55.08674 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb14eabe-567b-389b-8a82-43b64ee1fbf0 | -3.03162 | -53.86814 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 423df54e-e16e-31ae-83f7-55e954a54a17 | -9.52325 | -45.33265 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ba9ca06-9fd5-3369-b672-c72c1b7100db | -5.76033 | -45.13515 | 2026-10-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5b652c-c37b-3907-b946-6d6eb9680e7d | -6.39139 | -56.4115 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f1a820c-72a2-3824-9871-9c067444add5 | -6.3216 | -54.78285 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a44d346-fd5f-3fbd-b392-e85fbd4c73ef | -4.861 | -56.03066 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ea51f70-f3f2-3e77-a3ed-480fbb69db30 | -4.30468 | -50.77758 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44f05ac3-5c9e-366e-aa76-d41bf8878574 | -5.87432 | -50.16283 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 09b8483f-25af-3956-b749-f901f219e283 | -6.00073 | -53.54679 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b42deaec-181c-34de-8f48-4aa196ae0f41 | -8.23745 | -54.7831 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5034e5da-2c0a-329d-9be1-7e92552e66c4 | -6.72301 | -44.27286 | 2026-10-02 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22ec5281-5dd9-3c1f-8bda-4042c8466c70 | -4.00059 | -48.39771 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5d56dba-70eb-3a52-b2ff-52d40ffd7cb1 | -3.17054 | -54.08717 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78e5d702-4de6-3e11-8bae-2ee00e6954b4 | -6.34649 | -55.33927 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 578586de-c789-3343-bf79-3180d524a3f5 | -2.9919 | -54.77113 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb0eacf-548c-383f-b737-78326a3d4adb | -6.34815 | -55.32875 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33e2391a-ed7f-3d45-b660-cdfe469564c3 | -6.25065 | -53.13955 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f7ed68e-7c9a-3d6f-8713-5ccbea078808 | -3.57354 | -51.47818 | 2026-10-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38cd4f8d-6851-3318-8001-372276eb3b19 | -8.2636 | -54.70212 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be74ce13-0adf-3bfe-b385-f9d36cc67ad1 | -7.27654 | -55.59195 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ab994ac-9f77-3be4-935c-bfd903c598aa | -1.60371 | -55.13214 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bc64315-dfc9-3b1d-b167-7d669ec345ff | -6.90615 | -52.50565 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 337fdcb5-a090-3bf9-85eb-33d3f2310ab5 | -6.27447 | -55.25606 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d55e5749-8b6e-3ff5-971a-e17397ae99e3 | -7.44133 | -55.5394 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1714f2d9-dc13-3d46-937e-c360aa33ddc9 | -8.01541 | -47.43658 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6a49c827-aa7f-3d1a-9e4b-c709d070e895 | -6.07943 | -53.30093 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1787453a-e6a3-36b6-9cd0-21dd14546492 | -1.26837 | -54.56401 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42aa52cd-c754-3334-8fab-49a35bff8450 | -3.28515 | -53.85548 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2237701d-0c06-3110-9ae8-2d11b9ac2490 | -6.40879 | -56.41367 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d0440d8-55dd-3f7c-83ba-9eedf654e4cf | -7.40143 | -55.21018 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c0cbb71a-7a6a-36bf-b49d-128aee631631 | -4.45532 | -47.92238 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b9f3beec-67f8-3316-a6a3-2d9820315c2e | -4.26335 | -50.75853 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30dd6edb-ee48-36a4-ac11-85b261f7139c | -7.72357 | -54.80383 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc3573e-ea2f-354e-963f-4f9f9a5ee8a7 | -6.26271 | -55.4376 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 374713e2-16e8-3424-a997-84c109ee540b | -3.27075 | -54.27577 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1534fa60-fe3f-3ff2-af44-2ec042579682 | -3.0185 | -53.8872 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72805c45-db25-346d-9c28-7b80bbea029d | -2.90931 | -54.12714 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e71118e-ec46-377c-a811-e534ee6a3201 | -5.12145 | -56.02647 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97859f29-01be-39ef-8e1c-9b7c8458c376 | -4.06398 | -51.09657 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76d4f65e-9395-3368-8b88-00d941949cf5 | -7.20957 | -46.54958 | 2026-10-02 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f3eea5-667a-3d28-800e-6cf6e3a46131 | -8.06747 | -55.34529 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c359162-9af9-37b1-b026-16064b00165a | -7.62738 | -55.07229 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d62fc81a-e2e5-3538-8d61-2bd20ea1ebb4 | -8.96787 | -44.1731 | 2026-10-02 04:57:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c135b8be-f2bd-398b-890f-a23ea2e04a60 | -7.68278 | -54.76202 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d75029d-8436-352c-b32d-68595d66f809 | -5.83407 | -53.54611 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3adb744-0d33-3893-bcbc-f4f5b9b927a5 | -4.2646 | -50.75018 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| adc7917b-9080-358e-9c38-df002a066d5d | -4.17025 | -56.30764 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd0884d9-d850-371d-b10e-c552005c4a8a | -6.4091 | -56.41047 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01243910-fe0f-3ba1-8cc5-e371069e0702 | -2.90001 | -54.14336 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83b4d23d-0b99-3803-a7f5-67bf7028ce35 | -4.04446 | -54.22495 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 508d1951-7607-3b2d-982b-aae230615170 | -5.99079 | -53.54522 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b922c4-51c7-3975-a6bf-1b4a7e7cce4e | -6.19648 | -52.80846 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a64c6d26-a6e8-3877-a925-85fcb5f7e429 | -5.87424 | -53.50602 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70af43ae-a280-335c-8f39-fb320b84d05b | -7.4633 | -54.98895 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d1c6836-a123-310f-8565-c8bec6a35b48 | -2.90223 | -54.15076 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a3c05c-3263-3a0f-a723-0806c72f90d6 | -3.29546 | -50.32101 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1666fd1-8370-3e3b-bffe-782df3fea16d | -6.90796 | -43.6829 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 495747ee-82cf-38e4-a36e-a1819ab493bf | -6.76013 | -55.09023 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d887414-8876-3816-b5d9-09bef493ad17 | -1.26223 | -54.55942 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d9d3104c-eb9b-3960-8b2f-b77cc275c0aa | -6.02292 | -55.3416 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a1679e5-f371-33d3-9b8f-cbef277e8151 | -6.25994 | -55.43355 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daa46ea7-7207-3749-8552-19f3f87339f1 | -3.30164 | -53.85802 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11aaebf1-67db-3fcd-b509-050cb2ff7636 | -4.36393 | -47.77522 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93e7a2fe-92a0-3a08-a83c-65f8b0fd1260 | -4.26162 | -50.74545 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b8ed4c2e-9b05-3563-8711-42e493bb6429 | -7.83488 | -55.11631 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b0ab763-5042-3dac-928b-d73ae6bf2104 | -7.27932 | -55.59597 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a07f32bf-ea97-3625-abd2-b3f1dd7f85a2 | -6.23952 | -53.1451 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e660036b-595f-3450-891c-bfdc8a19b59c | -3.03768 | -53.87259 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab2fd88d-efec-3aa0-b1ba-a9ab71213338 | -3.14063 | -53.73814 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README62.md)
