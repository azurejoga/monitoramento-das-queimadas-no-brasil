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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aad6d140-3529-35a6-be01-a3f9e5eda9d4 | -7.25534 | -43.06811 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| d0a98b32-d39f-3872-afd0-4462ba3fa4bd | -8.48178 | -49.55613 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 337854fe-7cfc-341e-b4a6-26248edd81f1 | -10.04533 | -59.09392 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87a430db-2453-323b-9a1c-8da6214387da | -8.03357 | -47.65435 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27520554-c49b-3d6f-8535-6455e2857f1f | -8.92872 | -63.89984 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143ac529-5f83-3678-b86f-1e2e8b20f8eb | -10.93416 | -60.71772 | 2025-07-24 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23d3c89-1e58-3978-ac24-905c21a8f6f5 | -10.67179 | -47.79551 | 2025-07-24 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 129aac12-0ad5-3b02-b6b0-d7eceaaf7138 | -6.96914 | -44.83087 | 2025-07-24 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cca6229c-57a6-367c-94e5-5d8456e1367a | -7.24839 | -43.07912 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5f628428-068a-3738-9a73-0288fd5688b6 | -7.45628 | -49.40198 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bc75a3c-3977-35e4-ab43-3db9150e7e27 | -7.23998 | -43.07886 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a79c80ac-103b-3061-8a8e-4814a1d550eb | -7.24597 | -43.08594 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7a459b7e-0b75-3280-891e-443793088064 | -8.29981 | -44.97252 | 2025-07-24 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 220dcd5c-1d42-3a1f-abd1-c2ad2cbb098e | -6.57936 | -49.51221 | 2025-07-24 05:04:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ffb1022-d81b-3197-826f-9c02cd00cb09 | -9.60376 | -63.46107 | 2025-07-24 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9429207a-944b-3d9a-99aa-ebe55983bbf5 | -8.92522 | -63.90108 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b2a81e-2b3a-34e8-aa62-d7e64a113a5e | -12.42246 | -45.38653 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ac16173-e70b-3b0d-a1ba-ffd408368cd9 | -10.00428 | -48.12548 | 2025-07-24 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b2a90fe-43a0-3631-9972-a1e24e77a2cd | -9.02158 | -61.2314 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9506b966-45ab-3664-9ed6-118fbd4feb93 | -5.9095 | -43.46677 | 2025-07-24 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61dd82a9-9e1e-340c-80b2-9b73ac0983cc | -8.09606 | -50.08768 | 2025-07-24 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d12e8bd-c9ad-35f3-80f9-22df1ad031c6 | -7.30642 | -49.57199 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f81e0fdb-5c3d-3bd2-9337-e0d2f80588e8 | -8.47725 | -49.55542 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2870ab59-df71-3632-86a9-2baf7cfa9456 | -6.25784 | -45.26921 | 2025-07-24 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddfb31f0-0f83-3e1d-9f9b-8a6e04c628f2 | -4.05244 | -56.24597 | 2025-07-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c0e6199-69bc-32d3-98f8-0ee786419a10 | -10.71525 | -48.85497 | 2025-07-24 05:04:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8920fb58-aa08-351f-bcfd-a1c47741da26 | -9.46044 | -63.14742 | 2025-07-24 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff2588a2-77a1-3b2e-99c3-0ec00cae8c0c | -9.52301 | -63.6241 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a389d1f-aff6-3c08-8259-4a36a96fe077 | -8.99025 | -64.52641 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11cbfdbf-045f-368e-8af7-02cee4c3d1bf | -9.35391 | -58.84011 | 2025-07-24 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b31a196-f917-3e17-857f-546172ec518b | -10.6231 | -45.23841 | 2025-07-24 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41dc95aa-5db9-3053-bc73-db268be119e1 | -9.37809 | -66.57989 | 2025-07-24 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc30b999-a24c-3c9c-a7ac-d402b280bc27 | -7.89376 | -45.54534 | 2025-07-24 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 506bd054-e381-3b74-8982-daf47ac56cb6 | -11.5212 | -54.68393 | 2025-07-24 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a988a3b-d4cd-39d7-a3e0-1b5f58c9c498 | -7.8458 | -56.49617 | 2025-07-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f8b02f2-5cf2-3943-ad9c-9df05b443a5f | -7.26286 | -43.07469 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 778227a4-bb6f-32f0-b2c4-c9bf5e212dfe | -9.13195 | -63.92077 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25939ed-28d8-3426-b1ad-13062886b929 | -9.73345 | -48.02228 | 2025-07-24 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d495af43-ec88-3cf9-8b03-fdfe299d8547 | -7.45564 | -49.40655 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa4401f-5bc7-3d1e-9eaa-20d9956c183f | -7.2485 | -43.06721 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 0a598306-1341-3c7b-b49d-7fa15bb3ebe4 | -7.45632 | -57.66248 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f12a174e-f7c2-3a8b-a193-543cdf58cc51 | -9.52705 | -63.62685 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 417df6f5-5db7-3e58-941d-b2daf5fdcfff | -10.05054 | -48.66476 | 2025-07-24 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52087115-3562-3419-a883-56689523bf57 | -11.3133 | -55.22275 | 2025-07-24 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 983ed0c4-f504-36aa-918e-2103138b6e22 | -7.45574 | -57.66613 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 238e361f-a0a5-3314-99e2-d2abcd0f1a89 | -8.47804 | -49.55714 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 569e7fba-0939-303e-aec1-260fa0d458ad | -7.25287 | -60.18493 | 2025-07-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cb3d59c-c8f6-3e78-90a3-e54fb08666c2 | -7.89261 | -45.55405 | 2025-07-24 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 439b56c4-bfad-3f0c-93bf-df4218fed297 | -7.26121 | -60.18155 | 2025-07-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a72b66-bde3-3ef7-bcdb-b4fa33a586ea | -6.63517 | -56.28896 | 2025-07-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba75224-9525-3c7a-a6b5-8e1d2b8c071b | -14.76996 | -48.27119 | 2025-07-24 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 967c1829-f273-3798-8a5d-0ef49371e845 | -16.63735 | -49.35133 | 2025-07-24 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d857e14a-86d7-39b8-8e13-0f26b19bcf72 | -11.79129 | -57.24226 | 2025-07-24 05:06:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 376b6f6a-d7c6-3665-842d-d9dd73d683e5 | -15.5869 | -56.02732 | 2025-07-24 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a7d0eb4-4193-3b9b-a81c-58a1091bd6cc | -13.64924 | -45.71934 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b4a0fd6-1f2a-3974-92fa-81f1fefba7fd | -12.50863 | -57.77485 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32fe7dd1-6cb6-329e-800d-e38680c96b90 | -12.58056 | -56.9738 | 2025-07-24 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db3302ef-a410-33fc-b53e-7df2dba2cfe2 | -18.11518 | -44.63761 | 2025-07-24 05:06:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 979b627b-bda0-3e3a-bc45-b602674d9caf | -13.74511 | -45.92712 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efb2db3f-33f1-3777-ba2b-e7dba0441e3b | -12.4987 | -57.7732 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a893a322-f948-369e-932a-4ce6b331a20f | -13.09772 | -52.14626 | 2025-07-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eaa17ed-315c-34db-9370-b75069dacc3b | -12.2716 | -63.79648 | 2025-07-24 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2a7a336-852b-3eba-a76e-0baa64f93a62 | -12.43874 | -63.6996 | 2025-07-24 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec4ffe63-ef76-3810-851e-3eeb7f97a885 | -14.36926 | -50.33043 | 2025-07-24 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdfae148-b9a4-36de-9214-aeb70471633d | -13.64871 | -45.7244 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf2671c8-8302-3d8a-9346-dd42c2c8f558 | -13.70459 | -45.67956 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93dff62c-94cc-3195-ab31-ceea69d060d6 | -15.13749 | -58.37823 | 2025-07-24 05:06:00 | NOAA-20 | ARAPUTANGA | MATO GROSSO | Brasil | 5101258 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d508581b-a8b1-3cdc-a441-1c7333887501 | -13.45333 | -60.97578 | 2025-07-24 05:06:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74ce51c2-db3d-30f6-af60-349616b1dce6 | -18.2672 | -51.13894 | 2025-07-24 05:06:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ba8b572-6f93-3079-ac94-8bc688c84edf | -13.6994 | -45.66843 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3fcf280-1875-3dbc-a368-3a9c6a7b4e42 | -13.70515 | -45.67439 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a65025db-2e54-3c75-8d58-52d0d2a51cbe | -17.56767 | -47.50968 | 2025-07-24 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea0a3a3e-558f-3ada-925f-791d677cd83b | -18.81636 | -50.6263 | 2025-07-24 05:06:00 | NOAA-20 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd182b09-3f8a-3ee0-b8bd-6c96efe6790d | -12.49483 | -57.77617 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fe9e7bb-9758-3fe9-994f-dcc74d182811 | -13.70403 | -45.6847 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf412f5e-1ce4-3732-b32d-545fa73fb0d7 | -13.7126 | -45.66478 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76942192-3329-375a-b0b6-2bc19d5e66c6 | -11.95159 | -58.76629 | 2025-07-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 29091fc0-0b44-3660-841c-92dc1490644e | -13.71033 | -45.6855 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa9f89f9-21aa-3427-b99d-972517d39e87 | -17.57355 | -47.5105 | 2025-07-24 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd7f83b0-4434-3e65-a51e-9d769d215b59 | -15.27325 | -47.13579 | 2025-07-24 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99cf3dd6-f13c-318f-b121-a081ec20b277 | -13.70347 | -45.68985 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65b2ff39-c4ff-36c5-960d-a8d346a14a4f | -11.94483 | -58.76514 | 2025-07-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2ee666a8-6e75-3fd4-b8b1-5062b6eef703 | -18.85482 | -47.96261 | 2025-07-24 05:06:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3458bc03-a337-3221-8bd0-44f6344632a5 | -11.79074 | -57.24577 | 2025-07-24 05:06:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afe27a88-6fad-3669-b3dc-c9cda1a56676 | -12.57725 | -56.97327 | 2025-07-24 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c71f397-1ebd-3e82-a9b8-34a4849880e3 | -11.96558 | -55.54135 | 2025-07-24 05:06:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1b918e2-b567-3c16-b570-1f173c06e97b | -13.21991 | -51.08129 | 2025-07-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ba5877-8367-3253-b501-89f209f0f793 | -11.94821 | -58.76572 | 2025-07-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f59d4ff-6e69-3477-9a3a-9eae5f6b750b | -12.50257 | -57.77022 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1e54fe8-a145-39d3-aec0-9bd141c8c06a | -12.58001 | -56.97733 | 2025-07-24 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e824da7-161b-3c73-a33d-38d961937b79 | -13.74691 | -45.92584 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f17722b6-894e-3513-b697-23df4b06ee41 | -13.69716 | -45.68909 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1ca365a-fa32-3960-8648-9cb3a9e47a04 | -13.69884 | -45.67361 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e9ca608-3866-3214-9fac-9565cbca3852 | -12.01756 | -62.80865 | 2025-07-24 05:06:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 388d970b-75a3-3a67-8423-f982e3243891 | -11.74737 | -58.34395 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b905a9b-affd-3766-8011-8fd8ce36460e | -13.70977 | -45.69063 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c85daa5f-c0ac-3a68-b591-1947195cea38 | -13.09364 | -52.14567 | 2025-07-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 429358b7-9c78-3bcb-b2da-7aa61f4d4dbd | -14.33876 | -52.10112 | 2025-07-24 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37bd22f6-5c34-3810-957b-f5cd999c63b5 | -12.57946 | -56.98085 | 2025-07-24 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9364805-265a-3a2c-af5e-75d122566f01 | -13.70571 | -45.66923 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README24.md)
