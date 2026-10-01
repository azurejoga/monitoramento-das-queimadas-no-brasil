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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b642204-09c8-3e2d-a805-963e64b04062 | -5.75119 | -45.1498 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fd315f6a-11fc-3ded-a069-a5bb9261f444 | -1.90043 | -45.82047 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75953d8a-6ebf-3bd3-b9cd-c496916dfab5 | -5.43851 | -43.73977 | 2026-10-01 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac9ff9e7-3d8d-321f-8553-7f421bc1929e | -14.14546 | -46.23542 | 2026-10-01 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74fbe7e5-a829-3634-b90a-0c48797f6e25 | -10.85001 | -48.70314 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 457ed408-b250-3d21-ae75-612f1b80659b | -12.40791 | -38.71683 | 2026-10-01 03:38:00 | NOAA-21 | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6080af1f-9888-35d0-98e6-78a0f9a29a89 | -11.45792 | -43.44312 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8aea11af-bd61-3224-973a-e640035dbac2 | -8.85248 | -44.39162 | 2026-10-01 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69f321f1-4d85-3e06-a8b0-01848143b001 | -8.62018 | -45.3748 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 923ff92b-7c0c-38b2-84a8-7f7b66897bff | -11.42221 | -43.41187 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bf261e4-6f0f-34a7-8c12-366b6ac90f64 | -11.6543 | -43.55381 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc83dcf-c318-327c-ba74-c4984878480e | -7.85184 | -45.82621 | 2026-10-01 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 82ae8e7e-7350-3464-b319-9a83fd09c94b | -11.61729 | -43.55613 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5059fc9-714c-30c7-855c-0b4c36d2c14f | -8.63529 | -45.29377 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f1a5a5-0e18-3fa4-b1e7-d8e15391b490 | -11.42333 | -43.40596 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9cb3056f-b49c-307f-8bb8-ce46adacd629 | -8.21038 | -45.47121 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea49d660-1d26-33db-86a9-ecf556d3cd62 | -7.50201 | -45.83334 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36a6b9c0-4ca2-3673-b46e-01909f034e98 | -11.83858 | -44.75017 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 403cb3f1-626b-31eb-a9ec-723123c2aaf3 | -7.60954 | -44.55492 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0e3d6a7-d8b4-3595-84f7-97483ef13234 | -8.13057 | -43.53177 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d575cf9-736c-36a0-a218-230cfd46b616 | -10.84357 | -48.69901 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78be105c-d18a-3b3d-82e4-e9452cf57f7d | -11.41832 | -43.40501 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 41973ee2-4b9b-337c-8121-7b54aeeb50ea | -11.17457 | -45.12372 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14e983ee-d3ed-38cd-874f-13810e95ee06 | -11.41664 | -43.41386 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3cd62ec-a345-3d33-909e-44be4485bef0 | -12.64521 | -47.63532 | 2026-10-01 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccf388c0-a077-326b-bc8e-3558a1dfdf43 | -12.2026 | -43.83203 | 2026-10-01 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 692dc31c-dca7-34e2-8640-307b02d35c61 | -11.31348 | -41.1785 | 2026-10-01 03:38:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7908c831-6f26-3edd-a702-bdf386b2040e | -11.45902 | -43.43719 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3988fee8-eb02-31d5-a673-b5f47d6dafbb | -8.21221 | -45.48837 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 835d8c40-98f1-3d8b-8638-fcfafa2437fd | -12.45176 | -44.18958 | 2026-10-01 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70ed21b2-5bdd-3692-97c8-1e19fe24a28f | -11.17602 | -45.11607 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ce3e939-cfb3-3df9-ac41-e08a379956ed | -14.14368 | -46.24409 | 2026-10-01 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7cf06a-dfdd-38b4-a170-12d8151fce36 | -11.43672 | -43.41758 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a947d48-9209-3d44-8c6b-a1f50909483d | -11.44173 | -43.41855 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6d51bc9a-a05b-38bd-ae6a-04e5d8ae81ba | -11.16961 | -45.11911 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdfc4371-7b4d-3777-a424-69b19d15ec4a | -12.4138 | -40.9207 | 2026-10-01 03:38:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea245032-6f8e-323d-a1d7-d251eac9fd9a | -11.71755 | -43.43699 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23adbe4b-1845-3358-923d-6f8d8cd57ffc | -12.86276 | -44.33837 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 413ff400-3d45-30c2-a882-2e463c000421 | -11.19106 | -45.11453 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1304f9f8-e9ba-38df-a376-902a309e0e49 | -10.85147 | -48.69604 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cd3e25f3-13c6-3e8d-a8f4-80bb53d2f784 | -11.4356 | -43.4235 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 179dd04d-ea13-3acf-b96a-22d18e9f9299 | -11.11608 | -44.59169 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3441c9b9-e67c-36f9-a10d-a84c7c61cbae | -12.5643 | -43.0691 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f8f42a28-2ab2-339c-8651-7d1ba1df1e47 | -11.44398 | -43.43424 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e50bed33-912b-35b9-b0c0-1ea42dbafeab | -14.37267 | -44.78346 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1c553e31-fe33-3935-9f66-829046d51b78 | -8.04023 | -42.85977 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72c2290d-9e0f-3cb5-9339-b4121da59918 | -11.45011 | -43.42929 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3235ca0e-3831-3ba9-b619-4d2a395a48e6 | -8.01846 | -47.46427 | 2026-10-01 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1a87b72a-152a-334f-b957-62afd11059b4 | -11.20426 | -45.19658 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac17a39-9495-33ad-bfe5-278fae47f0e8 | -10.25778 | -44.57999 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8dcd580-5c71-3060-9a9a-ed3f5309753b | -8.33391 | -44.15774 | 2026-10-01 03:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe403965-ed18-3c7d-8858-8795a0aaa750 | -8.38993 | -46.2862 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 424f363b-0f28-30cf-a49f-5422feee054f | -11.45737 | -43.44607 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4b9811f4-3acb-38e1-9557-a132caa74870 | -11.43783 | -43.41167 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 910fa9cc-57e4-30e8-93b9-a3ddd192d020 | -11.18547 | -45.11324 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fff299c-ebb6-30fe-8343-6818c2daf0d5 | -12.60579 | -42.17086 | 2026-10-01 03:38:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ccea8614-493c-3822-9d5a-c42d6e59a09c | -12.86281 | -44.3342 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8dfa2774-5c9c-3349-9726-1019c0afd133 | -11.42779 | -43.40984 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2efc47bf-b852-306f-a462-3f2230970ef0 | -9.75593 | -44.82139 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 288ecda3-5bf1-3cad-94b7-fb3de92e35ef | -11.40696 | -43.41259 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e49194bb-9741-311b-b0fe-fc6e876eaf6d | -9.20535 | -45.80611 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 22e15cd1-b91e-3127-af2f-b43b41f85dad | -11.67998 | -43.49996 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcede648-340a-3f9f-8f4f-fcf9d9ab09b6 | -11.83795 | -44.75343 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0c966519-9d67-361c-83b9-5ee524a79799 | -11.22427 | -45.18411 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85abb3e5-15f5-3fe7-b5f5-73b930921f97 | -15.45206 | -42.09868 | 2026-10-01 03:38:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6c7329e-2117-31f1-baa0-20a54e9a9ba3 | -13.5195 | -46.88699 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fbfacfcc-41d9-3337-a6fd-8bb5cf6b97f2 | -11.19187 | -45.18681 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83f7e749-a864-3ae3-bb89-ba85c0beb183 | -8.01839 | -42.89369 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 894db04c-504d-3776-a4af-b1f5775d5b73 | -11.19444 | -45.18678 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1057e13c-33ce-311b-b1e1-6cd5d4cf0734 | -12.1942 | -48.44033 | 2026-10-01 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 0fc1b834-e649-3e2f-bbb5-3d463d97c40c | -12.20557 | -43.83349 | 2026-10-01 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 275e3b8b-636d-35fd-8518-21d6b3652375 | -8.12721 | -43.53268 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7dbecf5-1c43-336d-9a92-22427eb062be | -15.5087 | -41.57221 | 2026-10-01 03:38:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bba9aa7c-9daf-3785-8264-fa1f649e4535 | -11.45345 | -43.43919 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4a923b2-23e2-3d62-a288-875ccc64220c | -11.44454 | -43.43127 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ca8f4bb-0cc4-31ca-a368-d311eb791774 | -11.1798 | -45.11241 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb9810c9-7f0e-3fe9-b250-357aa45b1dd8 | -11.42667 | -43.41574 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c62be80-6d17-3198-a2b6-bbeb8b1e0f21 | -11.65934 | -43.55476 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8526453d-596c-3168-9224-187758f0c03f | -11.1831 | -45.10949 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2311e591-4265-3726-85ce-5e99595f8ed4 | -9.8035 | -44.81776 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d1799d-fede-3ac1-b1ff-1a1ded75be21 | -11.39892 | -43.37149 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99cb5134-1bee-3b69-af1a-0c553b5a9a8e | -11.34442 | -43.35812 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d8d201-06e2-3eba-a026-e5ce3b17449a | -11.18242 | -45.1131 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 296158b0-72f4-3756-a182-99da155410a5 | -11.41776 | -43.40796 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a4a7165-8d45-3f26-95c4-37bcb46b0978 | -9.78159 | -44.80972 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4d44f8d-094d-3fa4-9a32-97d1a47edc09 | -12.50943 | -43.10022 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e1c13c05-0aff-30ff-bb9e-e9ed2143e180 | -14.85751 | -42.15125 | 2026-10-01 03:38:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22376da7-1d1d-3023-863a-7b045107ba54 | -11.4357 | -43.50623 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668656d2-d318-30d2-9e29-0611e85e2012 | -11.20338 | -45.14108 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 845f2a5d-d4dc-3be8-8794-c7e5ba998fe0 | -12.35556 | -46.37649 | 2026-10-01 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 813c5f71-490d-384a-ba53-7cf7129c7fdf | -8.33321 | -44.16161 | 2026-10-01 03:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1fe322f6-c8fd-30ad-83c1-303708e1560d | -11.449 | -43.43521 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| deda0b94-7cdf-3d82-84d8-72eaecba16e5 | -10.91628 | -43.8467 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46e5d881-f007-3e1e-8f17-d461617bb2b0 | -13.26078 | -42.46414 | 2026-10-01 03:38:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f5d54ba-c248-31dd-857a-9f9182170113 | -11.44674 | -43.4195 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ac0e3b16-6837-3899-a610-82fb831e7d15 | -13.88696 | -44.45946 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6818c22-9ef0-308a-8777-9b3bf4f715b8 | -10.45372 | -46.778 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d73262a0-8d97-32f9-bab7-a24d680ea031 | -14.36353 | -44.77495 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3259df6d-0bf2-3d88-ba9d-17aa81c7a0a3 | -13.51347 | -46.88578 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8349a809-6674-3253-9d5a-d2004423ea89 | -11.45235 | -43.44509 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README21.md)
