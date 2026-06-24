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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6b69e85-e1af-339e-9b27-0a9e172be9a5 | -8.33434 | -50.49342 | 2026-06-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d7a7be2-148b-3e87-a2b1-66cabfb55e61 | -11.46674 | -46.72731 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 699bbd70-e6cf-370d-9d6c-7201039bc608 | -12.84367 | -44.36447 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 13895ada-c999-36fc-940d-2489ca8d2894 | -11.23492 | -43.34755 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ab703d29-b36a-36a8-86e3-77a7e19a1846 | -12.84511 | -44.35414 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5212aaeb-a8c5-3a44-bdb5-cd1cfe23b35a | -12.87132 | -44.36845 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41de733d-a033-3632-9f2e-90d1f68e2fd0 | -12.8383 | -44.37416 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 75b9298a-874f-366e-bdf6-b6180691ef75 | -11.30003 | -43.32132 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5285b4cd-e9c5-360d-9ec0-aa0c52b30be7 | -7.59864 | -46.47834 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e928746-0d52-3f57-a58f-29f14b02b4b1 | -10.69741 | -49.61337 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f64f48-0c5b-3860-894f-bef7572c4689 | -12.78762 | -44.45059 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b5b3380-13c3-3408-8c85-d6f53fe34695 | -12.54638 | -54.60186 | 2026-06-24 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bc3d3c1-9a71-3f45-8046-ec3d73a6fa07 | -7.92453 | -48.28854 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71acf2a6-3cf8-3a9e-9515-d3e6c4a07f05 | -12.81685 | -43.89807 | 2026-06-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62a3241f-ca4f-36e9-ab2b-cce0f96a40ad | -10.84121 | -48.76654 | 2026-06-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fe1d5e4-0cf9-341d-8ffd-79f851bd6278 | -9.80309 | -48.92069 | 2026-06-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afe03648-cec2-300f-b59a-583e1e27f6ec | -8.68631 | -47.85684 | 2026-06-24 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cd2060c2-5844-32b2-97a4-8834b2da18e9 | -7.9141 | -48.29044 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f8f20c2-7bb0-36d9-92fe-2263c4a6a640 | -12.77977 | -44.44948 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b34630ea-90f1-32de-a1f8-02565e4a6524 | -9.17747 | -58.06158 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab7beeb-b776-3242-ab17-f2fa50af03c6 | -11.91671 | -44.17261 | 2026-06-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5aa3531-4103-3fd0-9b84-fb706211aff4 | -11.8495 | -48.18419 | 2026-06-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54057004-088f-3951-93df-cb919ebbaae1 | -13.07257 | -53.35215 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5669aee7-6776-3591-b5ae-5450c9b5e7b9 | -12.84296 | -44.36962 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 53ccf4bb-f805-3026-811d-cdf3e67992df | -8.88407 | -48.50578 | 2026-06-24 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7faf6b95-2de9-3fdc-90ab-ea6d396339a5 | -13.18262 | -43.40414 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 36937e66-2c11-32b8-b071-c571532e7c28 | -15.01489 | -42.37056 | 2026-06-24 04:34:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86d61272-470c-36b6-9cda-a1ed18bc5546 | -12.19846 | -47.96929 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25312165-95ee-3f15-849e-e2d02e8a4e3f | -11.27813 | -55.79544 | 2026-06-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82dfa9c8-40a1-31d2-a30d-c6f828966f2f | -11.89056 | -47.60008 | 2026-06-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2385356-c739-3bf6-aa2b-d5206cccee6d | -11.51461 | -56.12973 | 2026-06-24 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d5e5d4-cf68-37dd-abd5-ff1804a5dac3 | -13.11514 | -53.53423 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 671fe3f4-53f9-33a1-9a9a-c16049889793 | -12.79155 | -44.45113 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c74685-e8ea-3010-a286-bfc755580565 | -12.84834 | -44.35989 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 70688635-e71b-3110-a68e-258e0670bd08 | -10.90384 | -54.12689 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f89bd09-15e8-35db-b496-3935409c3f4f | -13.77388 | -53.07489 | 2026-06-24 04:34:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86aeb167-6309-39f7-a388-294dc40bc32b | -12.2018 | -47.9698 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0de63c90-ead5-3143-9ad8-59d0a8956c6d | -9.51402 | -48.06955 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b34337a8-b4be-3322-9f5d-869644d7d80a | -9.18295 | -58.06255 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a75a3061-6c5b-37ee-a2c3-3fa2b726b8ac | -9.13953 | -47.9818 | 2026-06-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c621956-1cbd-30cf-b9fb-e8bccc8751c8 | -12.87025 | -44.37057 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d8fa16a-e720-3289-8d7c-d026c4950393 | -11.30781 | -43.32618 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f95bb4f0-bb8e-3709-b5a9-b507f3a66eed | -12.78116 | -44.43924 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 709c127c-61e2-3b2e-a4ea-1d2795ef9cd6 | -8.53233 | -47.09004 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59efd463-c80c-3870-a809-eca39f1aaebb | -12.83973 | -44.36388 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| f37f2fa7-88ca-3265-8447-ef8547ae11fa | -8.07854 | -46.38723 | 2026-06-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe7a93c7-7221-33ac-8359-2e54d11db8c0 | -11.50275 | -46.69786 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c421cf9-26fe-37a6-9cb7-b16dbc366d59 | -12.77907 | -44.45459 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fc08d62-0e20-351c-aba6-46dc473612c1 | -12.84762 | -44.36506 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 849aa7a7-8f1f-35cd-8a70-55d620b91019 | -11.41815 | -54.43873 | 2026-06-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 199c4e4e-258a-3585-978b-190d95dd104f | -9.43931 | -48.87293 | 2026-06-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfab484f-2ca2-3850-a583-f0f627b37a5e | -9.59912 | -48.0223 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7b12b7-a300-3c31-9ea8-4fbae0c01a1c | -11.54468 | -48.26591 | 2026-06-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e050be7-37d6-3daf-8305-bb9650f421af | -7.9174 | -48.29096 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 931babd2-fca4-31b6-be90-f6ffdd01c7b9 | -11.96603 | -49.23203 | 2026-06-24 04:34:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47b1cbc-0c7e-3383-ba3a-f43ecf6d9874 | -9.80364 | -48.9172 | 2026-06-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03be7640-cc22-3d53-b8dd-6debaee2f1b9 | -11.30324 | -54.7165 | 2026-06-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffea1a06-9ec1-37ab-b53f-a89cadeeaa5c | -12.78439 | -44.44492 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f15255d2-b4c0-3283-ac09-c33839a0304a | -8.07516 | -46.38667 | 2026-06-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f657bbd6-d90c-3317-9cb4-7fbebe5bb910 | -10.7013 | -49.61035 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5527cd02-8712-3974-a52d-9281c7da22ed | -9.51739 | -48.09148 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f1150e4-c880-36cd-92ee-b30cdf11586c | -12.85157 | -44.36562 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 792bd55a-6964-3b46-b3fa-606d61f66f01 | -11.48567 | -46.74195 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec972829-3a4f-39e9-8c3d-5686200b5994 | -11.29636 | -43.31733 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2028695-fdd7-308f-bb06-b4ee2e4ef65e | -10.12511 | -52.11467 | 2026-06-24 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ff325da-33f6-3763-810c-6776fae0762e | -9.36595 | -50.54404 | 2026-06-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3388d52f-90de-3a53-9060-3860bd402856 | -8.6071 | -46.00033 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 794563fd-ea12-3268-b84a-64c9ca9fe2e5 | -11.26219 | -43.36313 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d2c5a0c-566e-304d-a347-6dfd212e4275 | -7.91453 | -48.24451 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 104363f9-47de-3416-aa43-0d188a737341 | -11.47993 | -46.73324 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2faee1c7-40a4-3de7-bc33-f6e527dadad8 | -8.98531 | -47.7468 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 442672eb-4de3-3494-a68a-e56ff02e1257 | -13.40059 | -44.12452 | 2026-06-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9db5e708-b06f-3f1e-9ea7-726121611738 | -12.06662 | -45.57743 | 2026-06-24 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4428f7a-4bb0-3299-95f4-8e496db274bc | -17.28852 | -47.04229 | 2026-06-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8397b121-4b0f-3b33-bd68-0edcc11b75a3 | -15.36537 | -47.36194 | 2026-06-24 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a451e40b-7941-31e7-a82d-1dca20b724fc | -15.88896 | -47.61687 | 2026-06-24 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b91074ec-5d25-31e8-839b-8496e6d66ce2 | -15.36322 | -47.36231 | 2026-06-24 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9cf0de0e-d413-3bb3-98ab-2eabd409f268 | -15.75868 | -43.22765 | 2026-06-24 04:36:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b6d8a124-ab7b-3409-9d11-bd55ca764a68 | -20.61946 | -42.27374 | 2026-06-24 04:36:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 068b83d5-459e-3ccd-a678-2e8406a7d7b9 | -17.79314 | -44.57228 | 2026-06-24 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05e9fec-36c0-3d7d-bb10-29c8c690f26d | -17.61646 | -46.69354 | 2026-06-24 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a869ed55-8ebc-32b5-b9de-b2e1e0e05c50 | -17.6128 | -46.69297 | 2026-06-24 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f9e77e0-8be9-37be-915d-5e1c1f83403d | -17.61584 | -46.69804 | 2026-06-24 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0ef9566-d633-3056-8403-3571ef25c4b7 | -15.7581 | -43.2323 | 2026-06-24 04:36:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 235c64b1-31f3-3ec7-a592-d9b2cbfda74c | -17.28911 | -47.03797 | 2026-06-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d24f515-34c6-3180-ac4d-fa6419206660 | -17.79681 | -44.57674 | 2026-06-24 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6c0241d-ac26-3b22-a777-da2d93f751be | -17.6 | -46.67725 | 2026-06-24 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1dbd7ea-2cc7-3f65-aae8-4b06e290ef48 | -17.79828 | -44.57656 | 2026-06-24 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9512adb-e3a0-3eb8-83a6-05cf498cff4e | -17.28552 | -47.03743 | 2026-06-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca32b0b4-38a3-38bc-97f8-c3f1c198376d | -17.61217 | -46.69747 | 2026-06-24 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8385fe3-c0ff-38f4-9a1d-636bf3f2d4d4 | -17.79458 | -44.57209 | 2026-06-24 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 593e0d94-276c-335b-9c7e-47041860bfac | -16.07048 | -44.45972 | 2026-06-24 04:36:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a8b8d8a-41b9-3064-af4a-205e9f5e5fc3 | -17.28493 | -47.04174 | 2026-06-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ba2a9fc-c122-3561-93fa-6676919b80b0 | -12.8552 | -44.3389 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| bfa34c4d-c5e2-3e39-8f8d-cec3812e4590 | -13.0635 | -53.3546 | 2026-06-24 04:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 953174fb-873a-3a82-9e05-258653848a3b | -12.8349 | -44.3892 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| eeaaf093-0102-3745-8b08-e21f7988a1e8 | -12.8548 | -44.3625 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 252.2 |
| 3e83a19e-1e84-3c8c-9ba7-16fe61ec67c5 | -12.8354 | -44.3657 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 366.1 |
| 4ebbd080-49b2-3f09-8d54-e0b7ddcbda0d | -12.8359 | -44.3422 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 219.3 |
| f5c633df-59fa-3eb2-b812-8425c7669f43 | -12.8543 | -44.386 | 2026-06-24 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |


[Clique aqui para ver as próximas entradas](README15.md)
