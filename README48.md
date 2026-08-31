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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6075eeba-7ab6-3ef7-b53a-444fba083cf1 | -10.74873 | -54.03305 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29393a7a-e717-3eae-8b92-b5e2981f4219 | -9.47059 | -51.58487 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bedffa04-db43-332a-95f4-4099f7e448cf | -14.22697 | -52.85267 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09455b2c-f5f2-3a28-aa6d-cc0a16ea3e2a | -9.20619 | -59.41845 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d58008b-ec1e-3bb2-b581-68ca2cf55acc | -9.01498 | -65.39934 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd77f8c-e3bd-31e4-8da0-3ab685e73e1d | -9.84085 | -64.97835 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1b25605-e09d-35dd-b5f7-b26337e13ea1 | -10.0579 | -48.69337 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 545614aa-239e-3d6c-b2ef-f4c5f7ca8f18 | -10.74755 | -54.01807 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2929a09f-fa99-3d8f-bda4-728e76f052be | -8.80095 | -62.48803 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab962eff-4420-354f-9dc9-a192ed0981f6 | -8.6251 | -54.69627 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0ddaecf-4f6f-334d-b92d-3e52a86a0cdc | -12.10059 | -45.03923 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c470c9b5-8d7d-3333-aaaf-a6ff6f282140 | -10.75506 | -44.8798 | 2026-08-31 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 11754c26-77a3-38ee-93a7-838ea3b496c2 | -11.34167 | -45.20909 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6206df55-2282-3853-9f3e-4ce1ef4cd8e0 | -9.93807 | -60.50893 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31af3749-a34b-31d4-9bbb-c4283b80adc1 | -11.49561 | -60.57507 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf092e59-f1cf-39a5-b822-b755aa401efa | -8.79525 | -62.49239 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 191a011e-9dc4-3e25-9b42-9dcd729c1a51 | -11.67841 | -47.60895 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc24c42b-3589-3f72-b70c-e9ae9a9b2259 | -7.44252 | -61.42188 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f18147c6-59a3-3238-bc81-2d812cf86c91 | -10.83113 | -45.31114 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 105f0744-0675-318d-a3d6-2b2a9c85da56 | -11.07934 | -51.52209 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2459db7e-9367-346a-9db5-4b8aec77297f | -12.78356 | -46.46103 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d859fe6-4b91-3af5-b46a-94a2ac2d22c3 | -10.82228 | -50.68977 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e34021a-bcf9-37cd-af30-345cf428d451 | -10.7431 | -54.02477 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc10655f-559c-3efa-baa3-44c0d8d49fd5 | -15.09367 | -48.10956 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| eee14af1-6a3f-31f3-80b2-0d1fcf556b94 | -10.47933 | -59.61553 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 112c4347-c5b0-3ae8-8f6c-81042c454ff3 | -11.49502 | -60.57851 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26f9ea7d-7933-31df-84ac-9a655b27f6d1 | -12.92715 | -45.86151 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a861f8b-69d7-363d-97f5-cecbdc99a1da | -10.74709 | -54.04389 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 40c6c7fe-2bc4-3239-b567-dc60448e935f | -9.16557 | -59.36824 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 59574dc8-fb22-3f8d-85d5-b5a2dbf467e5 | -10.48017 | -59.61068 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41d460d3-3831-3325-bcc9-f8c6ab7cb412 | -14.58464 | -54.12368 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64d22fc6-7c3a-31b2-b37c-f3095c0de6ab | -11.93242 | -45.06346 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfb20bef-e8cf-35fb-8fda-2de6f806a009 | -14.39465 | -52.54092 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b32141-ad87-3543-9192-dda4093a205e | -11.02817 | -57.23645 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1af88b01-a486-3468-991f-9191caefddc4 | -12.08905 | -44.98592 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a113a3b2-217e-3187-98ac-ca86ec41881d | -7.57731 | -61.34131 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d64a71c6-35df-32ba-bedf-ec653271bd0d | -14.40328 | -52.53321 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ac9ce7d-9963-3c7b-aa78-1efe53b54eee | -12.39497 | -46.45753 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 667f53c7-1fa5-30dc-aecb-6613a1f93b3e | -10.7835 | -50.70976 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96dda504-915b-33e6-a1a0-567e0d220048 | -8.58475 | -66.97188 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36cc1b76-dce0-3f65-b060-6b87c9667c79 | -12.95092 | -45.94869 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 02550512-ae54-3b18-8c83-89078f492c15 | -10.79958 | -50.50377 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46b64358-97ff-339c-88fa-ea285477d9ae | -9.93308 | -60.48903 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d42963-f91d-38df-8095-ab6559ffd7ae | -9.85675 | -64.98507 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21f5a8e7-2fd2-3bd0-a971-16fe0106a1b2 | -15.66563 | -45.91313 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc148c7a-e660-33fe-a90f-b6c1665f553a | -7.58258 | -61.33752 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 923d36fe-7fa7-3503-b2ea-811627f766c4 | -11.93222 | -45.06398 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62b9d367-fe0c-322c-9a25-74b677a40273 | -10.48623 | -59.60914 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 406be8f7-3f70-36a3-9f83-7093080fe354 | -11.37691 | -45.17317 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b340c8e4-1052-3930-8d07-b8e0afd090a0 | -11.34186 | -45.15947 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82c8bc90-d46c-3f15-9ca4-3f16e4a8fb06 | -9.17341 | -59.63197 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f33b42fb-59ee-3764-b75b-f8e8b2e38c22 | -11.34844 | -45.20104 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8958210f-1cd2-345e-acd5-ddec85741294 | -12.78897 | -46.46124 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 682ccc27-6558-3e58-a77d-c28db5607060 | -12.91636 | -45.90617 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b0bc0666-1c34-3993-867d-bd61a984c369 | -11.32712 | -45.18535 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f45f3ec-16e3-322e-b645-cefb4d4ab120 | -14.5886 | -54.09686 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88173a6e-c8d7-3b51-bd9d-0cbdba372240 | -8.62023 | -54.72749 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015b9175-20ab-37cb-96d7-e859bbaa30a5 | -15.08871 | -48.10899 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a6d233b-7360-3b4e-bcab-a94cffe23225 | -11.18523 | -55.11116 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2cf784a-80e1-38bd-9b76-d686b9e83011 | -14.40825 | -52.52479 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ee5ea1f2-5fa3-35fd-af7b-ab8317fe4521 | -11.22084 | -45.32726 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32bc8261-e34a-372b-b15b-44f87b217245 | -10.15866 | -45.73484 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b906dddb-8ea7-3830-a849-ee1c66c4da29 | -15.6661 | -45.90863 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f37a262-ca6c-3c8c-83a2-ec998e1cc856 | -8.91519 | -66.95355 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38400969-64eb-37f3-b1e8-fb0f0b41d1f5 | -15.09087 | -48.10333 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 482bc04e-87cc-3ad5-8b8b-a4c367cbb098 | -9.93461 | -60.50452 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2932726-e074-3f72-b3cf-2385cd2ee048 | -8.61572 | -54.69124 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e949f4da-e83b-32c3-aeee-3da3105f4d50 | -9.04835 | -65.44343 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316f9c72-d724-322c-bab6-6eedcaea6824 | -11.88406 | -45.82043 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e175061-5ad3-37a5-948f-393c4655cc2d | -9.19052 | -51.55708 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10353219-e490-3c14-83cb-b075032c1a82 | -7.92004 | -61.33444 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3e377ac-eaec-3954-b02a-c83e7e0cfa09 | -11.17802 | -55.09204 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f26b6dc-c0b6-3126-b85d-61b60816a17b | -8.67853 | -62.81657 | 2026-08-31 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4689597b-b29d-33bb-9426-577a9620a2f7 | -9.84638 | -64.97932 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec26fba-b144-35e7-8fad-8ab25f5d61d8 | -10.81472 | -50.65769 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be694723-a79a-3625-a2dc-decfa5e9b549 | -11.37738 | -45.16912 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fff43002-1a2d-37af-836b-c0feac9ef59a | -11.22545 | -45.09792 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e29986e-a70f-3aff-a7d0-7d0e0c8e4441 | -7.50723 | -63.6526 | 2026-08-31 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae051e79-498d-3140-a34e-660a95348482 | -14.60926 | -54.09998 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a4db74d-1e54-3683-8f79-07165c575431 | -11.37168 | -45.21835 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3703524a-51f3-34f8-a62d-e546c6dd40e9 | -14.12927 | -52.80482 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95edb717-269d-3fe2-a590-65bd8d50716c | -11.17857 | -55.08854 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99284df5-2f0e-362d-95b8-6a1957d8b707 | -13.48043 | -57.05747 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23228ac1-7029-3e68-a26a-541aaf088917 | -12.39539 | -46.45415 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26f68841-10b5-3401-b70e-f1e862791766 | -11.1797 | -55.1031 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fe28a93-07e3-3afc-8c87-e229ed8aaa8b | -8.59111 | -66.97318 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dfc7b98-6ee5-3da7-b149-6603ce220d2a | -9.0092 | -60.59417 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a1e3c8-25fa-30b0-b970-05412bdf085f | -11.07161 | -51.46947 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36b18c38-b49a-3d69-a967-d8793d513d75 | -13.38953 | -51.80506 | 2026-08-31 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0eb5a009-7eaa-3292-9b30-6376e2024866 | -10.75028 | -53.99998 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b10d4082-dbd8-3687-9c51-6e7d44ee86af | -9.93679 | -60.5163 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6acb0404-a494-3c0f-99ca-11ef311346f9 | -9.13892 | -60.52985 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 755cbe6b-8bf5-3b4b-a3d0-cff5733dcdd4 | -13.93587 | -54.41626 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca57f47a-eae1-3c89-9de4-e05c2d17c25e | -14.40697 | -52.53374 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9726ec2e-444f-3e64-b134-cf2be8169587 | -13.6432 | -51.83905 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44f3431d-61ae-3a87-a5d9-360d0bb287cd | -8.67552 | -66.51397 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca4c8ec3-6182-34b2-a865-e906916c9acf | -9.722 | -65.00195 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 937ae440-c043-3c6c-96ed-e82460a89e1a | -9.89319 | -60.28334 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4e2b7d4-98e9-35d3-942f-457ac8b01491 | -9.07025 | -60.42128 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cf1ddca-4b1d-3145-ab46-40d63d3c86cd | -10.48157 | -59.61338 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README49.md)
