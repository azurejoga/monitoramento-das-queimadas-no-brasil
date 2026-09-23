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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30a904ad-f2ec-3136-ad91-32c9bf647dfa | -7.14199 | -48.42871 | 2026-09-23 04:27:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34766518-8f34-3ec2-8cd1-3c535aebf665 | -8.94447 | -50.91346 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eecad20f-17ec-3d79-9425-eafdf44ca280 | -14.61156 | -45.64819 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0378be14-2361-3469-b473-8b2363197a5a | -8.3173 | -46.87785 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d5950aeb-bd37-3acc-a31e-1c149c3b8454 | -10.69306 | -48.72357 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c9b5c8d-1226-3e76-805f-fcb3fa1f50bb | -14.60868 | -45.61857 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cb68ce2-b370-3e75-ba7b-b101de976b84 | -10.51112 | -44.85685 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e463b142-f8ac-3e7f-a1ab-1a44e8dc416e | -8.86577 | -50.18891 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 693e3f2f-ab63-3024-bd9f-edea84a21ce7 | -8.15005 | -49.55101 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9de5b869-885f-3927-bbf2-f9fba3d554b6 | -10.00511 | -45.20586 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 196ed132-1e2f-305a-95d5-9ae0e977e193 | -13.44997 | -46.25602 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08eced62-4846-3e96-a29e-6e820a2a776e | -9.56985 | -47.95724 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a93d042-9df6-3c92-8849-e2ea8a075045 | -14.62157 | -45.62889 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc17df0c-959e-3643-b23f-2ad15b4edf93 | -13.44712 | -46.25177 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a390bdbf-cb37-3f11-9acc-8cae16be45b6 | -8.35915 | -45.61479 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a8a612e-4397-3b12-880d-9de45133d0d5 | -11.8384 | -46.88854 | 2026-09-23 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c0545a9-21b4-3581-9ced-320c53d2cbd4 | -7.09598 | -52.75751 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 82a246a5-cec0-3479-af83-5ce4b7f59e7f | -8.49243 | -57.61297 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 52486a5f-a4d8-35c5-a6eb-f0d2b3377b9b | -14.64221 | -45.61439 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be056ad6-015c-3c83-be1e-b82719db826c | -12.7334 | -50.88566 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a08f914a-7b26-3bd5-9ada-ad6d5f9e2ece | -13.05434 | -48.73016 | 2026-09-23 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4077def0-93ef-37c6-b870-1dd86542c504 | -10.2549 | -49.97449 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f45797e7-761f-38f1-8fff-51c45ab7f9bb | -8.18034 | -54.82158 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6285dc3c-a512-3b1b-a01d-8f6139f8a087 | -14.59457 | -45.64146 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beba66e9-d451-3664-ba4d-d601454abd7d | -6.68034 | -55.06096 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8923c71-96ba-32c3-aa24-ae2d10b7790b | -12.41522 | -46.98336 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e532185-5193-3d30-b158-f5b71e09ed55 | -5.92487 | -59.91606 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1834689d-d181-3b9d-a41b-3d49e8f9b0d6 | -9.34956 | -50.09593 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3179842c-db50-3821-b8db-905ebae96c5a | -10.50919 | -44.86167 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d22660-37ea-3c63-90f0-127b57443194 | -14.63342 | -45.62559 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 31dd3b17-7009-36a0-937a-86f1233f19ac | -8.81337 | -44.27126 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 39c38420-91e8-3155-9afa-bd137782b1db | -6.18051 | -52.79087 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4771cb0b-3ae7-32b8-883b-26a00bcf5f9b | -14.62449 | -45.63353 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18c04efb-4191-3250-af31-d1ca949f76fc | -9.92301 | -48.47714 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca4cc149-3035-3cd9-8c2e-bf21c4020076 | -6.8889 | -55.33284 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ceccdc73-e8a4-3037-b8c4-4971b70b1e84 | -8.49167 | -57.61714 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01f00e7e-bc44-3efc-bdce-a4e59a067c94 | -6.42372 | -59.98014 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57308009-906a-3866-9199-42df4d7ad354 | -6.30502 | -57.74807 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d332c859-3368-39af-9e74-980afb9693b9 | -8.11343 | -48.23688 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5f89b63-35a7-3702-897a-ee2f8cd5699f | -6.66719 | -50.88631 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbab717c-5537-3493-8ea7-ee2d25cd3689 | -6.6679 | -58.57329 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 872b96ed-261c-3cc7-ba44-ff25ef42a6dd | -8.38361 | -45.5895 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24b7679d-650d-3101-a039-184ae11b1aee | -7.1682 | -44.51693 | 2026-09-23 04:27:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9940da73-4c54-3fb1-b43f-8428ce6a7501 | -9.60594 | -43.94717 | 2026-09-23 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8a50df0f-510c-38c6-851d-f251d3db2a34 | -8.90455 | -45.93952 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c95aafad-d24b-3b97-b1ab-95664b95a826 | -12.76534 | -50.86995 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb68bd5-2f25-340f-8571-a4824f0fcc8a | -6.30466 | -57.75298 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9aee5752-3c5b-3f50-92fa-a57154741430 | -7.41707 | -44.72546 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| dd856c9c-fb25-3eb3-b64c-0dbef99abbb7 | -6.08621 | -57.62814 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f581894-fa50-3e39-8527-190075a350af | -11.78313 | -47.44651 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1837744b-3d41-316b-bd82-a61d803ebf32 | -9.57765 | -46.53611 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b16bc7d-78ae-3feb-a6fc-e3442562f621 | -10.9079 | -51.51901 | 2026-09-23 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0883a466-82fb-3005-9e77-4615279ef458 | -12.8136 | -50.86556 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01ed77b2-5531-32f8-b15c-c1dea0c98114 | -10.2628 | -49.97549 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 833519c3-c7c7-3517-8d22-0abad45b9cce | -11.45666 | -47.62003 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be37bfa-25e4-3bbe-b0a7-b5e87e396cc8 | -6.64533 | -50.9225 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51d9aef3-ca43-3217-b1ae-2033552eea48 | -10.45634 | -50.36263 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f9de32b-bd61-38fa-87c6-9928a5f0c1c5 | -11.29388 | -44.03476 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1744b160-deda-38f9-8cd1-11375b923ce7 | -7.10102 | -52.75401 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d489637f-a325-351c-9893-2cde8973cf81 | -11.96543 | -50.0825 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e228acf-c817-3a53-8a7c-ac91473cf24a | -14.59752 | -45.62114 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b88b1fc-d8aa-36e1-be76-5ec9c2dee1dc | -11.88851 | -45.77931 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1e7c3a8-e3aa-37bf-a860-e6d6437ff62a | -11.28106 | -44.04829 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b86bef39-547b-323a-929f-0a320edd3a0d | -10.26565 | -49.98004 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a643ab88-db99-3cfa-a062-82fd25c7b365 | -6.66816 | -55.07092 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35aa270e-5b5f-3d63-9600-69343bd46fe3 | -7.9385 | -45.6555 | 2026-09-23 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96e14249-e9ca-3695-ad7c-4a618a05e54e | -8.90224 | -45.90995 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 716b521e-98e9-355d-8884-0b04c21dada4 | -8.19861 | -54.71807 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7f8c9f33-1f83-3ab2-a7a8-eb392b4a4779 | -10.00679 | -45.1947 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dee77f41-c3c3-3cd7-87cb-429a9b5bebf4 | -7.14314 | -45.7208 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efdcdd68-b3ef-3dca-abef-7c95ccf8b005 | -10.87166 | -50.1552 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f6bc04d-d575-373b-ab8b-f1b34bbbe0cf | -11.67882 | -50.19624 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50828359-2b33-3668-8507-a4bd41567b0a | -13.02419 | -48.6413 | 2026-09-23 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f1c8d1c-a21d-3072-bae2-72ba1a356d7f | -12.71973 | -50.88461 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| acb50828-acbf-374a-951b-a1fcf1bfd2fe | -6.67235 | -58.55946 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08f966e3-095f-3b30-b495-72ca6f6b5ec7 | -6.67299 | -50.94715 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be4e1279-74fe-3c1c-b808-6a78628bddee | -11.93685 | -38.2882 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1e62217e-298f-3af1-886e-d658f4433f3f | -7.61883 | -50.42073 | 2026-09-23 04:27:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 952cf496-0791-3fea-b403-518d773a4baa | -11.7035 | -50.22073 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b61227f9-440d-39fb-a227-d61074b1be56 | -6.68123 | -55.07456 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c5afb6-3fbc-3eed-a155-8f4f893adaf1 | -14.62562 | -45.65033 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| de2e8754-2081-3a01-b89f-3d80ee4e57c5 | -5.74315 | -53.46696 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 630f9855-1cd2-3b57-b154-8e7b11431ce0 | -12.12995 | -47.37991 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45b5160e-39c0-32fd-a5dd-a8abff34b063 | -12.71617 | -50.884 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d129b099-18c2-3cae-a9b9-7b57387c5ed8 | -6.93226 | -46.55553 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ff42cff-a72a-37fb-8a99-f75811c701d7 | -6.34487 | -57.77422 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ec8bc03-9257-386f-9225-5130d510c452 | -12.06936 | -50.3614 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b4bc148-4bfb-3bf1-8b7c-dce6eb3f7601 | -6.45559 | -54.98823 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b747c449-6ad0-31f9-a4ce-f48c9e11bb2c | -6.6625 | -58.56676 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 344e1d32-3f24-3b57-b873-e8694c63c2c6 | -11.66474 | -43.48553 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7485975f-8f26-33c1-9227-ea1a9a62fcd6 | -8.25298 | -50.86458 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60ce5666-6113-3bae-a5af-f78aaed2dddf | -11.88965 | -45.77178 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70f032fb-8f8e-3662-9848-0e94415f0a9d | -10.96002 | -50.60879 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 141f2d0b-ccd1-39a5-aa8b-10d2a94d4e56 | -9.9292 | -48.45976 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 798c14d0-c34c-3859-ab61-25d551323730 | -6.67985 | -55.06387 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09af4c7a-f0fc-3354-9fe4-0f8584bd5fe0 | -14.70798 | -45.58278 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cec5cb2c-ecb8-3d35-b2ec-6e3f44413299 | -6.31196 | -57.7444 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c54cd0f-5f1e-379f-8216-7cb76282039c | -8.38198 | -45.60017 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acabd95b-1594-3385-ac8a-91d5fc484a64 | -7.39448 | -55.21636 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44385a28-a83c-34df-bf7d-ed2dfcc66988 | -10.25969 | -49.96714 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README70.md)
