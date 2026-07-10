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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d6cea5c-0997-33ee-bb70-80709ee5da4a | -9.55447 | -48.67864 | 2026-07-10 03:47:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebbac52c-c80e-3ed0-9334-a551eaf82678 | -4.15722 | -43.08901 | 2026-07-10 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e5ec863-72d5-3c1e-9fed-9aaad243b1aa | -5.46774 | -45.42919 | 2026-07-10 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8287b39-e074-3263-92cc-52fbdf8a3a69 | -12.37437 | -47.89281 | 2026-07-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51d738a0-05da-3ce8-8902-c1cb52bc5fe1 | -12.36843 | -47.89147 | 2026-07-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7be80be4-8a00-3975-9cd3-27d11d261581 | -6.00341 | -39.20077 | 2026-07-10 03:47:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d37e5a5f-4e17-3965-9a79-e819075f5a0f | -10.1203 | -50.18987 | 2026-07-10 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c8392e59-60c4-348c-a83e-978e9c49a7e4 | -11.47003 | -47.60646 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fafaf79-ebef-3320-937e-becb9fe3b8c1 | -6.41917 | -43.71984 | 2026-07-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcfe3d5f-7b63-39c3-8efb-379c79d7f3cb | -10.12173 | -50.18291 | 2026-07-10 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 637b475a-6244-3b3f-860f-bd77747a82da | -4.34254 | -47.76703 | 2026-07-10 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efc29265-bfd9-3023-9e36-cdf1041ac3c7 | -11.45989 | -47.60767 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3188430b-a846-3772-ad36-edcf803d5a3b | -11.87576 | -47.67403 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e416e441-15d8-33f0-b296-05566e3419e0 | -10.82924 | -49.38099 | 2026-07-10 03:47:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a671e09-229f-389b-8f31-159c44f7285b | -6.94074 | -43.70946 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 883b81a0-3eae-3d6e-ad89-9a0597880f33 | -11.87664 | -47.66954 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4fc129d-4c17-326a-995b-e3613cd2fd05 | -4.15673 | -43.09194 | 2026-07-10 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1c8a066-4608-3d20-92e8-2acd8e5b27c4 | -10.12877 | -50.18453 | 2026-07-10 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b6063747-730f-39cc-8f4f-a9fca53db935 | -16.828 | -46.31636 | 2026-07-10 03:49:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5beac96b-38a6-3046-9f4c-870de5019b4e | -22.32092 | -41.79611 | 2026-07-10 03:49:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3acfe77f-3368-3fae-a6e6-8425e250c6ec | -16.52674 | -47.73825 | 2026-07-10 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5eff644-166a-308b-82b6-f71a98819c26 | -15.17249 | -42.50613 | 2026-07-10 03:49:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dba3524d-f8ae-32e5-88f6-874346596585 | -8.0023 | -46.62114 | 2026-07-10 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8974cfc-b522-39fa-a2e9-ecd79615ee11 | -18.02046 | -41.83089 | 2026-07-10 03:49:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d805be23-dc46-3d33-a5b0-7382bc18f894 | -7.99867 | -46.62274 | 2026-07-10 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d456db-e254-3a91-b243-ce1013b6ce06 | -8.50785 | -48.06478 | 2026-07-10 03:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b40af61-8bd8-3774-bfc5-b2cfb547e799 | -16.52681 | -47.73796 | 2026-07-10 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd41873d-8e65-32be-a6f2-eb9f00c308a3 | -19.59856 | -47.60378 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 343e28c6-2f6c-316a-b157-d5e0c99bb40f | -19.5921 | -47.60908 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a797c59a-fcac-34c2-a551-2614ad6d25bc | -8.50138 | -48.06369 | 2026-07-10 03:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 659309d4-3838-37c3-bbca-bacd02d4d050 | -8.1109 | -47.09951 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6461fe3-f730-30c3-b016-637452d38045 | -20.70326 | -50.52317 | 2026-07-10 03:49:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 93a3ce11-0e6d-39ba-ab77-405ac0782532 | -16.44946 | -43.14762 | 2026-07-10 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bfd08ec-624d-3c49-9d6b-6429e4f88369 | -8.03502 | -47.42561 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d66c65a-c964-328f-91e9-553ee2c14e6b | -14.72819 | -48.20047 | 2026-07-10 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77966770-064c-36f9-9f7b-828521ed8b5c | -18.07804 | -43.27797 | 2026-07-10 03:49:00 | NOAA-20 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89082672-658e-349e-a9bb-1c600a150bf2 | -8.71897 | -47.83222 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e450aaf6-7267-32a0-a91c-d9a71e843590 | -19.36573 | -40.86222 | 2026-07-10 03:49:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89ff337a-343c-3986-8879-ff94f3b5bcc7 | -8.03695 | -47.42963 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ff4ae0f-25eb-3f0a-b0ab-f7f0562a2f80 | -8.50033 | -48.06914 | 2026-07-10 03:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37e8f699-4fa8-3dbd-860a-005147d16e22 | -8.04026 | -47.43198 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25396109-848f-3a97-a5e8-695273e7dc85 | -19.59141 | -47.61243 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc663c0f-33ba-30e2-9836-e9caffa2b7a0 | -18.17396 | -42.69828 | 2026-07-10 03:49:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 58d69e95-54a4-3b24-919a-16a90c02724c | -18.02415 | -41.83166 | 2026-07-10 03:49:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bede9181-3c3d-3823-a989-a22049f70886 | -8.03595 | -47.42081 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c73d7233-0908-352e-85d2-51aaaed10b66 | -18.17785 | -42.69891 | 2026-07-10 03:49:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| b3bc7e58-3d56-31ef-bbb4-fd6db857ab2b | -19.95172 | -44.09171 | 2026-07-10 03:49:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f400d98a-1359-3af7-b220-d160ddf76eee | -8.71798 | -47.83745 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46899d67-b7c4-31dd-8012-53b7d49ad2c5 | -8.12905 | -47.8716 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f370509e-82c3-3174-97f7-853cdfbfe737 | -19.6005 | -47.60371 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b386bfdc-65bf-3559-adfe-11f463dfae97 | -14.8435 | -42.7715 | 2026-07-10 03:49:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28635848-8e70-37d9-9f45-9352b296d844 | -8.72184 | -47.83036 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4084424-57f4-3c88-8f95-c0b7dae64c26 | -8.71982 | -47.84068 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a3c6378-19fb-3b5d-87ec-ace1414a68dd | -19.59401 | -47.60897 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef00dff0-cef1-3392-a86c-a90fcc7e08c9 | -8.82475 | -48.33354 | 2026-07-10 03:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c393fb39-b043-38a5-88be-cc6a16dd1990 | -20.665 | -48.6764 | 2026-07-10 03:49:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f411861-0d7e-3e69-bad1-b28cac76caf6 | -14.7343 | -48.20035 | 2026-07-10 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca1f1ede-f20a-3320-9d41-54e2cd3247e8 | -19.36646 | -40.85807 | 2026-07-10 03:49:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ca526425-3099-3d76-8789-d0c34487eae6 | -19.66315 | -47.6116 | 2026-07-10 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c72a115-8377-311c-9ff9-c8bedce2ae5e | -19.33037 | -44.00648 | 2026-07-10 03:49:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1228d77e-b8c4-3f93-b6e4-ff60176085b4 | -19.66447 | -47.60528 | 2026-07-10 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d2df5698-8b10-36e0-aa96-963b347cd56b | -19.66007 | -47.60076 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 964f2ad9-8a02-3b7f-91e5-1517d56c5388 | -19.5998 | -47.60699 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15033439-c6e1-3bb5-98fb-7d1434d24b58 | -16.82861 | -46.31337 | 2026-07-10 03:49:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7d73a2a-9de0-32de-9c53-c65afd6ba8f5 | -8.72338 | -47.84359 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5880190b-93e4-3e45-9b1f-6f349fea6096 | -19.59329 | -47.6123 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 148ffa2e-1437-3d17-823a-72d241220423 | -20.96584 | -43.81065 | 2026-07-10 03:49:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8fe90820-b54c-3562-afde-b87e4561637f | -15.54216 | -47.38721 | 2026-07-10 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128750c3-b955-3701-bb6f-d5d3914c12ea | -19.5965 | -47.61374 | 2026-07-10 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd624be6-29da-3c9c-bea5-96469b32c038 | -8.00463 | -46.62377 | 2026-07-10 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65774cca-8fce-3314-82f6-c4d5163c2bd4 | -19.66516 | -47.60203 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 80c4e2f7-191c-3958-8cfb-bf8449cad046 | -8.00151 | -46.62553 | 2026-07-10 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89da987d-48a6-37ee-ac9c-93f1f0071545 | -14.7292 | -48.19562 | 2026-07-10 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e5c1c36-c21c-3688-9a94-397fa63fad11 | -19.66381 | -47.60844 | 2026-07-10 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3e829857-d881-3f51-824d-bce33efe6100 | -8.13545 | -47.87285 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bffbb3e7-813e-3248-91d3-4aa48406b600 | -8.72082 | -47.83556 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa64c4da-6388-3b5b-87ce-6c979cab3fe9 | -19.59787 | -47.60711 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bc7f09b-3afb-3800-a637-c2d827d742f0 | -8.72531 | -47.83334 | 2026-07-10 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6464f864-d763-30ca-92eb-7f38fd96548a | -8.0316 | -47.4236 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d30d9171-1751-3d78-9c5f-0c0283cdddb5 | -8.83129 | -48.33467 | 2026-07-10 03:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20fc96b2-b7d8-31a0-ba55-5e2838ad4222 | -19.65973 | -47.57703 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6299603-78a4-38a0-bb7a-78e276d378f1 | -15.53674 | -47.38586 | 2026-07-10 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd264c7f-d0f8-3231-8251-111c1f285c75 | -19.59718 | -47.61047 | 2026-07-10 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67423d7c-abd4-3d4f-9079-a6021b5211d5 | -19.94766 | -44.09073 | 2026-07-10 03:49:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| df2af4b5-2f8c-3a98-9897-bbe3cbb3968c | -8.10998 | -47.10448 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 767a2373-3333-3f27-9809-b8c32e663115 | -8.03785 | -47.42477 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f64abdc0-1420-35b2-b4f2-5b5849349e3d | -8.12801 | -47.87707 | 2026-07-10 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5264eeeb-3763-374c-9c8d-ddcf7d6742c0 | -23.56133 | -47.51186 | 2026-07-10 03:51:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2df3bcbe-d9e9-3d08-ac07-d20df7bd29a2 | -23.56291 | -47.50859 | 2026-07-10 03:51:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e1f7dadb-7fc1-302f-adf6-678a7d66dd25 | -21.45055 | -48.68369 | 2026-07-10 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a477a3f-63c4-3dd0-9643-0e38ca0d13cf | -21.73987 | -47.71837 | 2026-07-10 03:51:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ae62bcf-f51f-3a92-be0a-5adb3bf5e80f | -21.74032 | -47.71856 | 2026-07-10 03:51:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7dd680d-94d2-319e-82c4-0de92df0bdf5 | -23.4267 | -46.75801 | 2026-07-10 03:51:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc14ef4a-d80a-3341-be34-852532289461 | -10.1286 | -50.1902 | 2026-07-10 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| fd587548-d376-375a-9424-b04884c66322 | -5.46851 | -45.43105 | 2026-07-10 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0ba5a45-2ade-3219-840d-413b6a31bec0 | -6.93807 | -43.71039 | 2026-07-10 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31a0abdc-5208-3d5d-a501-f1cdeffb5b2f | -6.67253 | -47.52245 | 2026-07-10 04:32:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e49956e7-e9c0-30ab-a76f-24eebff9b9bf | -2.77098 | -48.5766 | 2026-07-10 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a47a9c7-3a56-3d67-95b0-6146d8511abf | -3.20724 | -49.06309 | 2026-07-10 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7952e778-62e3-3a88-8c89-138505e06f9f | -5.46909 | -45.4273 | 2026-07-10 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README6.md)
