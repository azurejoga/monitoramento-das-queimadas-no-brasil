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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ffdb1e4-3339-3b72-a41e-aa4ae252bb87 | -11.37962 | -54.04741 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca8378d7-7cd1-35f4-84b2-2a81751a8be2 | -12.62614 | -47.26173 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672eac8f-932e-3559-b9a6-a677b28b7f0b | -9.16154 | -45.60436 | 2026-09-29 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c8f2abf-dcf6-35db-b2b9-e36151209d42 | -10.71633 | -44.43599 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94b2179c-53ab-3807-bbac-3ca679e4057b | -9.95694 | -50.15703 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae3ad343-ce4c-3770-8499-629a92edf3f5 | -16.06294 | -47.91573 | 2026-09-29 04:17:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7d5599c-22cd-3f54-8a42-9ea9c08ba272 | -11.5018 | -47.40063 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0cd7ad95-ddbc-35b0-aeaa-2f9db42a0f71 | -11.39964 | -47.44747 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f141e968-a73b-3c31-bd6c-bf1a9cc84860 | -11.37171 | -43.36311 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3476ea6c-655b-3274-ad4e-f33fd67c24e7 | -15.08407 | -48.33501 | 2026-09-29 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f7694ef-5002-31bf-8bcf-9c349679762e | -11.3997 | -43.42607 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 476c0517-c7d8-3f42-9c20-9c6a5ccc7517 | -11.5487 | -54.49684 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92ab2ea2-5c69-3a02-aa2a-4371f7c9143c | -10.26918 | -44.63961 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10313ced-c355-36f7-9832-ca735e04c009 | -9.85814 | -44.95846 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e573abe9-b60f-334e-ba22-081a13a47d15 | -11.08519 | -47.50438 | 2026-09-29 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6738ee98-db26-3164-844a-880661412e85 | -11.34608 | -47.33365 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c9f7452-53a7-314b-8de4-4c0266c30a57 | -9.96407 | -50.16669 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e9e3aaf-1973-3ce1-a128-e284d865eef4 | -11.35148 | -54.03839 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef48ad45-a17d-3c2a-9e2b-09dee110fcd0 | -19.76062 | -48.93506 | 2026-09-29 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4523384-c68d-38d4-bb84-92db6ab32db7 | -14.5198 | -52.48516 | 2026-09-29 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c233f9c4-64ef-3690-937d-702383926023 | -11.86501 | -50.47003 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6984689-7e9c-33b2-be06-6b1b3ab04957 | -12.05994 | -46.49543 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| efd0298c-bf4c-3ed0-ae60-ae49de50500d | -10.81291 | -48.73227 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77a435e1-5c60-3717-8d49-f904389310c6 | -11.9058 | -50.61124 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a350d8e0-aa07-3cf7-aefc-efcc88df5a62 | -15.16919 | -46.16814 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821a2ebc-fd14-3e3e-a5e3-237f626270f3 | -9.07287 | -49.8661 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad896b70-4d84-34b9-b75f-3256476625ce | -9.79475 | -44.82133 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e95cfd2-0341-3974-bffe-b6c5bfa5efef | -11.40938 | -48.97353 | 2026-09-29 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8da3a95e-ade5-3cf6-bd51-f837836d1589 | -19.44169 | -47.56274 | 2026-09-29 04:17:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72df4642-1b88-3c18-8088-d761cff2b3cb | -11.3989 | -47.45185 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf87ee4a-8425-3fcf-a2d4-6189e432ab26 | -10.80909 | -48.73136 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e60f112-82ad-3260-a6be-26900a453355 | -15.46225 | -46.14398 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e8195e1-efd2-3fbc-8189-c8e0d9024c2e | -9.09141 | -49.88597 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0458286-610d-32c9-9791-f87a80ed4a62 | -12.04396 | -50.93606 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ecd5d12a-5a70-370b-8f2d-e7deb18cdb14 | -12.0284 | -50.97301 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c2288cf4-f168-358d-968e-4f4ed7d32d34 | -11.37391 | -47.44782 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0e752c7-b57a-3f06-8217-86bf9dc6d8d0 | -19.98792 | -41.33955 | 2026-09-29 04:17:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e83edf6-449b-3a10-b9cf-0a255a3e7b84 | -20.91513 | -47.4659 | 2026-09-29 04:17:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cb56878-9d17-31fe-bfa0-cec3c8de7bfd | -11.17359 | -44.79709 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f43b17f5-597c-3aa9-8dfd-51a1d6b1d152 | -12.03429 | -50.96522 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6e85b797-1741-30f2-b5b8-9274ec626d22 | -9.76654 | -44.82766 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d96355a7-f59c-3ae1-8574-d1b5c4c39fe6 | -12.01301 | -50.98352 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93d9aa7b-2a34-3891-982a-b4f3bfb532dc | -11.41588 | -43.45418 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2440ffa8-bbaf-3f87-be42-cda1a0200c0f | -12.07151 | -46.47015 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d64a0b7-b96a-3682-b2b0-79c88005bda6 | -15.22324 | -46.16973 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6c3740b-089b-3c60-8c5d-2e0b99f1e228 | -11.43695 | -43.45018 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fcd4bb6-5ca9-3885-a7e8-55fd8470a52f | -13.16103 | -48.56436 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb756c00-40be-3c9f-a1e2-7bbca67d51b1 | -12.02045 | -50.96712 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 572c47e6-340e-307f-b3f2-fab0e0a4c46d | -12.63444 | -47.25502 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1409efc-ecde-3646-9455-c62023a1577d | -14.51136 | -52.48508 | 2026-09-29 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53f11595-f6a1-3b4d-9527-d8d27cd14fee | -20.35459 | -40.97896 | 2026-09-29 04:17:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6fc24bca-2062-3683-be8f-c3a45dab1738 | -11.71531 | -44.50797 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b14b042-fbd6-3ebe-8ac2-ec5096ce2246 | -9.68269 | -49.30693 | 2026-09-29 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8163c3b7-26a2-3ec8-90cb-dc5e14f00311 | -14.10561 | -54.29721 | 2026-09-29 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 551516d5-84ac-3772-8a61-46d68b7455e4 | -10.48424 | -45.23808 | 2026-09-29 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d20c5e9-6445-3e30-a1dc-90dade47949f | -9.828 | -48.20407 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00455da9-16dd-3bb6-9c61-684f0bcbb7cc | -11.18664 | -46.1827 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf580d57-e93a-3df0-a793-fc8881fd9615 | -11.63014 | -41.8345 | 2026-09-29 04:17:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5f6436e-fdcf-3327-b53d-80c17f87f8c5 | -9.82866 | -48.20164 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87417cc8-fb8f-3fd2-8e1e-b3c91d14cd95 | -11.42139 | -43.44042 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c9121b-5ae2-3741-a887-068550037296 | -11.3818 | -43.38667 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54017cf5-0298-384d-a463-3cfa237581b4 | -11.61567 | -46.78212 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bd8830d-1521-32a5-ae93-cfac228aa737 | -15.73258 | -46.02765 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2bcdc3-b29f-3afd-9fe6-c7b7c7640503 | -11.90916 | -50.6109 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b345d7d5-6418-3fd3-a4d5-8047482470e3 | -11.43144 | -43.46392 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28caca02-ef35-3b57-8cf7-c51d50cc0c90 | -14.0699 | -46.33224 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5142037-ded8-3e9f-9dab-572a055acfcb | -11.64836 | -43.51217 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12a17b19-dfc4-3753-becf-1816b06dbe48 | -11.95823 | -50.93805 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e37f982f-b618-3377-b3eb-1e6659c62d85 | -12.32943 | -46.95124 | 2026-09-29 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 493087c1-f50d-306e-8500-197318d0e4a9 | -12.03375 | -50.943 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce6ec77f-d481-37c3-b050-fafec9be6224 | -12.04168 | -46.5001 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca80b3de-3415-37e2-b4d3-8c63e3c9c6d3 | -12.01506 | -50.99726 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 300cae31-463b-3e19-98a7-8e60cfd6513b | -12.73502 | -47.26287 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b969a664-6e73-3135-985b-4a418d758391 | -11.38017 | -43.3974 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d33eddae-b5a3-3417-92d4-bf473b7cb34a | -11.38391 | -47.45376 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae4fffc1-980a-35b9-b02a-d2a8c9b883fc | -11.17634 | -44.80112 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0383d11-c731-36e0-8849-b7013d9f2477 | -10.82603 | -48.72492 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bafbb9fc-26c8-3aef-b364-0d86a48b788e | -10.52098 | -45.3682 | 2026-09-29 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6db6a3-a3e6-3faf-b4c1-276dacf99086 | -21.2303 | -44.33537 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3c0afb0-e04e-307f-b39c-63f06a93c03f | -15.45619 | -46.13925 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 240d63c7-236c-3648-871b-fc72fd424766 | -14.51544 | -48.29935 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb24089e-d71a-3cae-a107-e5456b7bf1ca | -12.3173 | -46.40729 | 2026-09-29 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ecf31a5f-cc77-3f5c-87d4-d28f571d535a | -12.69406 | -47.3786 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ab6aa0e-b76c-35e4-87ce-8057ff0ba348 | -11.41636 | -43.42868 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4d587c6-d10f-3a98-8da1-4f5f6608db90 | -12.03827 | -46.49956 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fdef4e3-e7f2-38a5-bdf9-0f04c8313bc4 | -11.35486 | -54.05016 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f426a26-21ff-30b5-8bb6-c8ec8a45be76 | -11.17525 | -44.78659 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 60e842a5-3604-3c6b-8423-fe881a4b20d6 | -11.86078 | -50.46927 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 58d08350-3e1e-3e81-8417-bd54074a8284 | -10.92717 | -43.89004 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05e29a6e-36a2-3766-be51-38dbb27f9df7 | -10.21856 | -50.00624 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aaadc03a-766d-3242-afff-8532ccc3bd52 | -12.00684 | -44.92902 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39913c74-cc8e-37b5-afbd-bdc1823d00ee | -10.90782 | -43.86186 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 065845ce-7f50-3a68-b011-8c864a1ac029 | -15.09567 | -53.86961 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6082410-6fef-3a9b-9e79-514f26c3e767 | -11.39698 | -43.44392 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61dbe2a-e7a4-308d-845b-bf8642274206 | -9.95483 | -50.14405 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00488e96-01e7-3fac-8aa5-0fc16c295740 | -15.71734 | -42.23974 | 2026-09-29 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af963199-e696-32dd-99f6-2c9240d1aa48 | -11.38642 | -54.04127 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c93f297d-e989-3e69-afee-2de849cedd92 | -14.12495 | -46.28928 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bf8379da-697e-361e-bc5e-747900b5971b | -11.0956 | -47.11454 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 43967a61-4ba4-3115-b82d-aae191fec372 | -13.43942 | -43.82293 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
