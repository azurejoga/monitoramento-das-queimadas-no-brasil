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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61134c90-d0eb-32ed-980b-a6d53653b6f2 | -8.32978 | -44.14824 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89173059-1b4c-39a3-922b-f4c725646512 | -12.2341 | -50.79063 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f59768e-9356-336e-83f8-22263ca3c63c | -11.28317 | -51.28119 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88739afb-10e4-33e0-89c2-b9b4c1251cfc | -8.33348 | -44.15292 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6e247897-8f8f-3210-8e7e-3f873648fbac | -12.19548 | -50.75546 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e4475ca-a702-3c3f-9c73-3922001446f1 | -11.27872 | -51.28769 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a67e7d24-e905-3d21-a9b5-0851e86852fd | -12.2021 | -50.75653 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e03c34a7-bca0-31f6-b8f8-6de8590f4ba2 | -11.16962 | -50.02375 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9486d204-45f3-3078-a96c-ce9d12067221 | -12.22862 | -50.73917 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0153d62f-19e2-3a9d-bc4c-01241bf770cb | -12.19492 | -50.75898 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c24de69c-87e4-39f0-8785-82006ef1c9a5 | -12.20817 | -50.76114 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 713d5dbd-9e25-3fd6-8147-a3cc57a66950 | -8.27349 | -54.74869 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8014a6fa-a78c-36c6-8f11-71f19ec19dd8 | -11.27152 | -51.29012 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 956a598f-219e-3228-92c2-7beb0a059ed6 | -11.28367 | -51.29935 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f1be83e-0dde-3e3c-8509-71051ea51719 | -12.22195 | -50.8031 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e28538-7a8c-3768-b867-17caeb042cb9 | -12.22968 | -50.79713 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1d5d1d5-b319-3b2d-912f-eb6c28685a75 | -8.24732 | -54.69154 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23a3f12-e62e-34d9-9e79-1bd10f6f055d | -9.00896 | -49.64127 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c757c0fb-27e9-3014-8e95-727e2208123d | -12.22417 | -50.78902 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4c2b1eb-d451-31ea-99ea-f93134efe30e | -6.71752 | -55.07509 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdd6f073-90fa-3396-acf2-36676c9a4ac3 | -6.31051 | -57.75521 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 920a24b6-ec31-3f84-9aba-02e9cb8def09 | -11.27703 | -51.29827 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0258de8-cfab-3a1c-8e7a-9d15054b15a6 | -12.19656 | -50.79174 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7f4fcaad-c336-3a31-8540-74d520dc453a | -8.25207 | -54.68721 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3ae692fd-075e-3d83-a3aa-4f3e8f6df046 | -6.67613 | -55.05364 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 332bee40-c6b2-3496-9974-41f3974f1cae | -12.20377 | -50.74597 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a620ea42-d880-3fe6-96c1-d77adda99fd1 | -12.21482 | -50.74054 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7ae4312d-ab1e-3bce-aedc-9cb017412095 | -9.20003 | -60.86845 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d3a48f-4f64-3448-afbf-6aee5f8624f2 | -10.90526 | -53.94893 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f6c863-6924-327d-943c-6b05703cb893 | -9.20074 | -60.86388 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcf7c984-feb1-3f34-a80d-c23659378d2b | -8.61056 | -55.21328 | 2026-09-25 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f13987-0327-3849-8ff5-2961be9bb4cd | -8.79408 | -49.99302 | 2026-09-25 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf428441-d8b8-3468-8e6a-7ffda6e28d14 | -12.20928 | -50.75409 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc2a1014-cc9e-3e92-9c09-39948fd18a27 | -12.23466 | -50.78711 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c54fe1f-1c9d-3a07-8c52-e9dfb1308d8b | -12.21426 | -50.74406 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 089df4b9-802f-3074-aa03-022553d55ae1 | -10.90598 | -53.94467 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e24333cd-9c63-3d22-b7ad-16b3ddf42df9 | -9.02472 | -60.55738 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3efb99fe-a650-3ff2-bc73-7d8e9c235681 | -9.92963 | -60.71921 | 2026-09-25 04:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c76a99c5-79bf-364b-b921-cd92b7825bc5 | -9.14805 | -59.47507 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cf385d4-4046-33e5-a2fe-6880e8d64502 | -12.20984 | -50.75057 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 373b7ee2-2e39-399d-87b8-7705437f3427 | -10.57457 | -51.2915 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccd9da0a-32b1-3ff9-8382-599edd4f5acb | -11.15075 | -50.64013 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b379703b-db3f-312c-9a54-2887138687c6 | -8.33257 | -49.51591 | 2026-09-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87c2536b-1ab0-30d9-97bf-f798ff6188f8 | -10.62087 | -53.98708 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90cead47-1c0d-36f6-9fee-1786040de8b6 | -10.94814 | -54.09307 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53f8b52c-1b15-31f2-b184-1c5e1437f6e6 | -12.21645 | -50.77332 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6f9bf970-d09e-380d-aa77-71045179a80b | -12.20486 | -50.7606 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4c06a1a-8fe6-3dce-850b-438bd7ef3308 | -9.53132 | -49.27472 | 2026-09-25 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2567391-ea7e-307f-8b0c-5d66862d1752 | -11.28197 | -51.30994 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bc0e06c-3036-39a8-9404-5fcceb629237 | -12.23523 | -50.76193 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d15f2a7c-7dd2-32fa-9bb9-285ec6d9a286 | -7.38882 | -44.77339 | 2026-09-25 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0faa7dea-35c3-33fe-b0c5-dc606702556f | -12.21315 | -50.75111 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b652de1c-b4de-31d3-8b68-cc49257400db | -12.24019 | -50.77357 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4a8555d-d143-36e5-8444-a4f78c2e35bd | -12.21204 | -50.75816 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7ebfc3b-9b92-3782-839e-0f82b4d73de2 | -9.01724 | -49.63179 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb8508d-fb6f-39fc-8246-74d63d10ec54 | -8.78212 | -45.83168 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 837764c9-74e3-31e6-84f2-77f7eac299c4 | -12.20209 | -50.7782 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a966283b-cb6f-3e02-bdf8-533972de039c | -10.56436 | -59.48488 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8a4ff2b-674e-3f4a-a15e-9ffaceef1313 | -9.16034 | -59.47742 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32ceb702-fa52-3884-a531-9160eeaee818 | -11.28699 | -51.2999 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c296b6c1-62cb-3a31-8db2-62a8abef97ef | -9.42076 | -60.46522 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60ab5bf6-ab78-3ff8-a22e-c1a3858d6a67 | -9.19425 | -60.86726 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be854bf8-ce8d-36c1-8be8-8df4857bd706 | -9.15565 | -59.47301 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 953e2c3e-1f9d-3099-8829-ab436da6fc26 | -9.15928 | -59.41557 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e10115e2-641f-3528-a2c9-bd72cb3c9a64 | -12.2054 | -50.77874 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d87147bb-de37-31b0-a847-b5c0f1ecb766 | -6.19736 | -57.78601 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8951e873-02eb-3028-bc47-0ca537beaadd | -10.55858 | -59.48705 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| badb5deb-fef7-3fe9-8b55-4e497e5191f4 | -6.44627 | -57.77637 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b3ea9bd-3c99-3427-a550-155f0b1ebb38 | -7.12368 | -41.72969 | 2026-09-25 04:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cf4e8975-2a5e-36ee-b584-c172b30231e5 | -10.56261 | -59.48815 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1bb662f-4d28-32e5-8adf-f1ac6d45ece6 | -10.62379 | -53.99203 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5af0c4f5-3376-39f9-b713-bf6ecd97f01c | -12.20542 | -50.75708 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33bf3114-c26d-372f-b143-d98db6504f28 | -12.19878 | -50.77766 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2f76484-6f32-3321-bff3-53a51130c8a3 | -11.71385 | -50.5585 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 985cb645-89c4-3dda-9c28-8b1edb9704cf | -11.1502 | -50.64363 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a87ef3b6-4bad-3863-be3e-ef531c278138 | -12.21591 | -50.75517 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e90f6ccd-5fb1-357e-86e9-a654bf57f463 | -7.38832 | -44.7768 | 2026-09-25 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f939367b-34b5-30a8-8b3d-d0d0b9631234 | -9.02398 | -60.56134 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638d1928-779a-396b-9ffc-156afc754240 | -9.15504 | -59.47639 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5024a4e3-83fd-3791-9c5b-5f862e8ee681 | -12.24186 | -50.76301 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53b43f4c-12f0-3b3b-8ac6-7df844563722 | -13.06598 | -43.28044 | 2026-09-25 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8362bc1-bde0-33a1-a0a6-383fa4f864e9 | -9.26591 | -57.18267 | 2026-09-25 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc74b293-c134-3c7d-840e-dc23afb9c2ed | -11.28536 | -51.28878 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 73d94282-9b64-3819-9602-db7228300af4 | -6.6837 | -55.05041 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f84f3719-6743-3982-a68b-695dbb53158f | -8.33405 | -44.14891 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 268946a3-93da-37ce-aaa7-17ffd8429789 | -11.48329 | -44.21185 | 2026-09-25 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7896f5a-3b18-3c98-bda3-b353f90cc27f | -8.33832 | -44.14958 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ad668c4d-7268-3a47-b2f2-94eb623dfa75 | -10.28404 | -49.95479 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ea3d86-b0dc-356e-a227-8df869df0342 | -12.20045 | -50.74543 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1afb3cdb-8cf0-386f-bbbd-7d75b6c2af60 | -12.21149 | -50.76168 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d261e938-5a31-3257-869c-a33fbcda65e6 | -9.1526 | -59.48994 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb1b38a-0c5b-3da6-93c0-38d292420824 | -12.22141 | -50.78496 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da394379-f058-3469-bec8-2df9408ca546 | -9.41439 | -60.46801 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff3f797-c16f-346f-a5a6-44e451c6f09e | -10.28072 | -49.95426 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 760b8e09-c9ca-3aec-8e0d-b50e88b4f99b | -12.19216 | -50.75492 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 75a7212f-2d7f-3bfe-8192-6d7f8042ac41 | -6.68243 | -55.05778 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fcfebd-61cc-3fa9-bad8-a5ec5ba55828 | -12.23522 | -50.7836 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cbeb033-1216-3fdb-84f1-f922937581c8 | -11.2826 | -51.28471 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9c73e01-2725-3c03-83b7-bf91f27b7b92 | -6.31547 | -57.7561 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1128eb92-7133-39c1-b14c-288d8c8a5445 | -10.56376 | -59.48804 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
