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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c78594f-79c8-3267-b148-636298d159a5 | -9.27777 | -59.74586 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4687ce11-207d-3d1f-95c9-5fbd26167ca4 | -11.42859 | -55.18906 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac9542a-81a1-3dd1-8c03-be75370e9f5a | -9.33874 | -55.21883 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db34511a-0237-3b63-886b-a1d4a7ee3a73 | -11.67929 | -52.15528 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e2a1031-78a3-310c-aaef-15cb368daf55 | -7.60578 | -61.61213 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a146902b-13a7-302a-83e3-c901e786141c | -14.85105 | -60.04076 | 2025-09-02 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a412341-a7d8-3c92-86b3-525abbabd017 | -16.85503 | -49.57162 | 2025-09-02 05:08:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2be42e9-caec-3f2c-89f0-c73e4889268f | -21.46337 | -47.42381 | 2025-09-02 05:08:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8209875a-2f4b-343a-8d81-43155a4aeae4 | -17.71038 | -46.89343 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 68412952-18da-3472-a1e6-1daa2802ede3 | -18.36873 | -46.02475 | 2025-09-02 05:08:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f1c4e235-a0f7-30a4-8c42-f84d6395b549 | -15.64184 | -56.01803 | 2025-09-02 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 87a54b89-632a-332b-9dee-82e990804f7e | -17.29135 | -49.20382 | 2025-09-02 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fa11d5c-2953-3d6e-b516-79625667a860 | -15.57083 | -48.3898 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a08707d6-335e-3a76-83f6-63f509989eb6 | -22.6743 | -47.29812 | 2025-09-02 05:08:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8d57aaa-d6ce-38a3-8f05-a6c2704eba3b | -21.6317 | -51.99318 | 2025-09-02 05:08:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 75690a43-83d2-301a-81e3-f52926d7c240 | -15.56096 | -48.3295 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb9e71a3-1ffb-38b8-9776-c85597ecd153 | -20.69393 | -46.3086 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0bc0e039-f5c1-357d-b4d1-0b4fe4bdc54f | -22.10902 | -46.96779 | 2025-09-02 05:08:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017f0191-7d2d-3554-8d3d-3c338fd50f8a | -15.55946 | -48.34301 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfa2fa3f-5b40-3f50-a5d1-049e4529376f | -14.85042 | -60.04464 | 2025-09-02 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f19212-af21-3c20-9bea-e8fbc77d0f1e | -15.55404 | -48.342 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c16f769-ad32-3884-98ce-2cba6d7c2117 | -16.59727 | -48.97914 | 2025-09-02 05:08:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c5d41fd-1f76-3a14-850e-ec1f82c14579 | -16.59198 | -48.97836 | 2025-09-02 05:08:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e69c1ddb-c0de-359c-b743-6e6f7d38c4f6 | -15.57634 | -48.38987 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c98a9349-07d3-3d12-b9d9-6a42cdd68458 | -14.31864 | -60.34212 | 2025-09-02 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3df1adf4-050b-37a4-aa26-b29b9312dfa1 | -20.4853 | -49.69208 | 2025-09-02 05:08:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3894edb6-c253-32ec-bd7e-de611c47b25c | -17.89605 | -47.16325 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b55f6b80-c741-3373-a30d-bed5d1cff447 | -17.28642 | -49.19995 | 2025-09-02 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0dfc714-d273-3851-a1ef-43cf41307646 | -19.81705 | -45.00245 | 2025-09-02 05:08:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11e5068f-ee15-3f83-89a2-7c8092c54e98 | -22.52859 | -46.80928 | 2025-09-02 05:08:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 83bf0742-ff4f-32d8-8aaf-a322cecf06bd | -15.67059 | -56.4424 | 2025-09-02 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc11614a-5851-3bc4-a913-93a7cfb5c906 | -20.69925 | -46.31282 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a46e91e0-9dad-3b91-8454-81690cb58739 | -16.29782 | -52.94269 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 006d3de3-244f-3482-9747-5262fd537b88 | -17.88399 | -47.16143 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09455746-b8e6-345d-b7fc-1002a5c65f9c | -15.97417 | -48.23779 | 2025-09-02 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b5c2d4-1717-3d0b-8e97-74817eeaa93d | -18.0454 | -47.7461 | 2025-09-02 05:08:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94faa9fc-7ae6-3000-9cec-f34d0080f867 | -16.29832 | -52.93879 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 765822a1-f056-3fdf-bbb5-a56ca3959fbc | -19.9659 | -45.5002 | 2025-09-02 05:08:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1abcb73e-6916-391b-9ef5-61128c95d91c | -20.70625 | -46.30774 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5745a0b8-9f3c-3135-8025-e9a6e3dafb3c | -22.68063 | -47.29851 | 2025-09-02 05:08:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b57651a-3ac0-301f-8e99-42caf75fc713 | -17.61726 | -46.64348 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdaffef3-fa59-3f9d-b34a-c5b7910d4cad | -19.5351 | -47.61172 | 2025-09-02 05:08:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43a78779-a2f1-3078-a5d5-9e7e56d58ae3 | -16.29237 | -52.95282 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0dabbb33-7fba-38c2-9c5d-31f102cccc64 | -14.59916 | -54.57704 | 2025-09-02 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ae4fdf1-d0b2-3bcb-b0f1-285d0983a1c3 | -18.04583 | -47.74171 | 2025-09-02 05:08:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d530b300-3b73-3009-b87f-df028116c5c2 | -16.06093 | -57.79414 | 2025-09-02 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a39abaf-fbdf-3bb3-805e-0e0a1063c22f | -16.28879 | -52.94855 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ab767886-94cf-3d3a-8c9a-c0714428732e | -16.85981 | -49.5752 | 2025-09-02 05:08:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8277cf42-4e6a-3355-b31f-a3b2094ab910 | -16.30137 | -52.94714 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3e93103c-0201-3910-aa3c-e13523cf3f2a | -14.60276 | -54.57764 | 2025-09-02 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a8fec80-4f0d-3513-8207-c5ee0401b28a | -16.85945 | -49.57832 | 2025-09-02 05:08:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb441836-9e9f-32af-8c24-5d05459ae7ca | -20.70013 | -46.3134 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5afe3e3b-5ae5-367e-af26-d8139b5ac5e3 | -16.28571 | -52.94049 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5e303c9-7c1a-35ca-9db7-6b26e2785cba | -15.56567 | -48.33696 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1aa6991-fd61-3567-8b77-24d32add26e9 | -19.82407 | -45.00293 | 2025-09-02 05:08:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 524c73e4-b9bb-3a89-ba6a-d1bd7db0ff3e | -18.07274 | -45.95375 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fc31c95-5280-31a0-8f5e-a0284b5e5876 | -18.09029 | -50.47756 | 2025-09-02 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b39c708-bb2e-3d30-95b3-aa0ed0b4887e | -17.61675 | -46.64851 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e42b0d0e-006b-3ea7-bb33-09c63e7a3af4 | -18.08541 | -50.47675 | 2025-09-02 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a7f3b7c-e00f-3111-934a-26c29e630849 | -16.28522 | -52.9442 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ec6aa7-7790-3544-82e8-a928745e06ca | -15.56603 | -48.33374 | 2025-09-02 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82393fa1-7c6e-33ed-8a61-95e5e2ed19a3 | -20.70095 | -46.30379 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97b015f7-7685-3ae1-9ab8-c09cca570a01 | -14.84354 | -60.04343 | 2025-09-02 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c986cc6-9251-3370-a11a-b12b2f821c4a | -20.48647 | -49.69236 | 2025-09-02 05:08:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ca0a9e7-2541-3d1a-962a-ae1a2a258141 | -16.30043 | -52.95437 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e18d8d2b-c5d5-316c-9c3c-f412f5ecb167 | -21.63225 | -51.98804 | 2025-09-02 05:08:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb93648e-e604-3b87-afbf-1dc224135c15 | -20.70798 | -46.29875 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2693d3a-472a-307b-873a-7246b8748ce3 | -17.70199 | -49.0966 | 2025-09-02 05:08:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad36a5e-a43f-3351-95c6-888278d53067 | -14.56819 | -59.72895 | 2025-09-02 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47de7fa9-cf79-3d57-ba72-7ad41d154ea6 | -20.70701 | -46.29818 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c24ff55-a9d7-3e05-ab43-5b9d8bcc41e9 | -19.82253 | -45.0064 | 2025-09-02 05:08:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67c36599-a2e8-329f-8066-17500d29bf90 | -21.63322 | -51.99243 | 2025-09-02 05:08:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2e963395-a84f-3707-a426-044909552f15 | -20.42295 | -46.40963 | 2025-09-02 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 057f4213-0128-3d2d-b8d1-c8fedb13665f | -21.46377 | -47.41887 | 2025-09-02 05:08:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 53447ea0-e900-3892-b55e-1bb7f6981c5f | -20.70717 | -46.30835 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef10e2c4-5c0d-3952-be05-bb66edeba872 | -20.70054 | -46.30854 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c42d137-c5ef-374f-8ccf-cfc653bb6853 | -16.06037 | -57.79772 | 2025-09-02 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6a878a28-229a-371a-bf90-36359d265839 | -16.86017 | -49.57207 | 2025-09-02 05:08:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db884875-2867-332b-b260-fd14b3c63f37 | -17.89475 | -47.1769 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a04c82ce-5733-375e-b2d8-1dd040c21445 | -17.71083 | -46.88872 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1843a6cd-f827-3533-a565-1cbf846acc47 | -20.70001 | -46.30309 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a00b3025-d399-3081-ae6b-2787401f0dc3 | -14.604 | -54.56902 | 2025-09-02 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f8c9a12-70ca-30dc-a69c-03b353f0b114 | -17.89002 | -47.16232 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9b0f5f8-6e4a-3b57-be91-421d9af061e1 | -16.2964 | -52.9536 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9df024ee-293c-3333-b043-a3d49d3fe240 | -18.07222 | -45.95983 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8e30313-88b7-3d44-b46c-54c7de2c08f3 | -17.8952 | -47.17213 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c97f41f5-4911-39c6-9c4b-5d59c316dba6 | -16.5969 | -48.98241 | 2025-09-02 05:08:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51be2190-389f-3c54-97bc-ab23519bb570 | -22.52885 | -46.80884 | 2025-09-02 05:08:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b0aabda-b4cb-3142-89b0-3341cdaf2501 | -17.28606 | -49.20329 | 2025-09-02 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0484c536-3c3f-31c5-a0ce-c460174b367d | -22.52928 | -46.8028 | 2025-09-02 05:08:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ced9af88-6e6f-3adb-9a5f-66bed2a4ccc4 | -18.97528 | -49.48795 | 2025-09-02 05:08:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3f7288d-ccc3-3fad-8c14-67b6404fe70b | -14.66685 | -54.90905 | 2025-09-02 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad563068-6c2c-3a9c-adae-e679ecfba63b | -17.70471 | -46.88781 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 99e5542c-49d0-36f3-9794-e33bf5d6a30f | -17.17278 | -46.08884 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35e6e3f7-d594-3339-8f76-e2581e5c0435 | -17.17317 | -46.08471 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2244bc77-6ae3-3867-973a-5353d2f23827 | -18.55006 | -47.46026 | 2025-09-02 05:08:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7b262df-7bda-384e-953b-23f2ef4dc749 | -16.29023 | -52.93742 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7102f7e1-d347-3bd8-83ac-46d3e68e5826 | -17.7043 | -46.89223 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 83796130-fcc8-3f4a-9630-6701e1cde25c | -17.61578 | -46.64552 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dc40ab9-c3ca-30ed-9837-151152fe3d61 | -20.6935 | -46.31366 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README72.md)
