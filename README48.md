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
| 6cf82783-ffe4-38bb-bd45-283f946b4919 | -15.7714 | -43.96528 | 2026-10-10 04:10:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fa2b0c9-5653-3b33-88ac-f41b3e7a913f | -11.20036 | -49.93814 | 2026-10-10 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cca2b66b-4db7-36fb-8b33-98e87a55552a | -14.74691 | -48.21695 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71394560-7a02-39ef-afb1-9a9c378af4ce | -12.23757 | -44.79217 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 228dc708-14b2-3d74-a633-a5ff7c3b2493 | -14.32477 | -44.67048 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7081ddae-9f84-336a-8fa8-716dd6da3c23 | -13.48594 | -44.44501 | 2026-10-10 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8405c8c9-5e5e-305e-8e07-9eff916522ff | -17.97153 | -44.34202 | 2026-10-10 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2e60f8e-cf28-3ece-a11c-341a4650cb98 | -11.94921 | -43.47155 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d33d7d-6cad-30e6-a5c8-215706f97c79 | -12.85354 | -44.16574 | 2026-10-10 04:10:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4588b3d-0d83-36e9-b3fc-dc7e887d1e32 | -11.59987 | -43.74355 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d2cc4023-31ba-3581-bc5f-0accb8008b0f | -11.00348 | -45.396 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3a26d1-c103-3ccd-97a4-7e96a6812011 | -11.6865 | -47.30355 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e44e2d1-496c-3b37-8868-4192ebf79e8e | -11.08117 | -44.11382 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da859c33-6b17-3646-90cb-f48db573eb26 | -11.85504 | -43.59357 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 781cc571-14d3-3f32-9f60-49ecded27f23 | -14.45463 | -43.94297 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5f40c5c-cc85-39e6-835d-fab5eddf323e | -11.36614 | -54.02446 | 2026-10-10 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae1eec2-4bef-31c9-a4ac-68639417385b | -10.43612 | -47.30807 | 2026-10-10 04:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8769d5d-124c-38a4-8957-53730c11d9b5 | -11.6585 | -43.69562 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95be1fd8-cbd1-38aa-87fd-4e8431f2351d | -11.77416 | -45.509 | 2026-10-10 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f07711d-b4b7-324e-83c9-aaf01a94c6b1 | -12.22905 | -44.69567 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfc1c521-b671-3462-9696-7e5f592bf8ad | -12.53786 | -47.19138 | 2026-10-10 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c2bf6f2-a468-3bde-825d-5dfc2800d778 | -14.32711 | -44.65603 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7e1181c-642b-363d-8660-66a48474c8d2 | -14.4618 | -43.94052 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ddd6e952-2beb-3e92-b597-6d46105297b8 | -11.99201 | -43.50425 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8596f6ed-070c-3ee0-aa3e-41bcb4bbed7e | -18.18776 | -42.73999 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 97eb3651-7775-3072-82fb-80d5301c3ead | -11.8689 | -48.03313 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea5cbcba-8977-3b8c-87a7-5de1411ebaa1 | -13.37646 | -43.89516 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf7d37c7-e59c-356e-af6a-a84e856e70c5 | -11.0918 | -44.11185 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f34d3c23-1427-360a-9773-60ff462811e0 | -13.38751 | -43.8897 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2ee912d-8e4d-3be4-8822-38a8542cce79 | -17.10376 | -41.57529 | 2026-10-10 04:10:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b31bfa4a-28cd-368a-a249-8714d8933a8c | -15.74034 | -41.90396 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80fa0cc7-fc2e-3c27-8d2f-dd00cac40031 | -12.06231 | -45.80611 | 2026-10-10 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc8437b1-caa3-3c1f-a798-1d47ebd3514b | -14.43806 | -43.96207 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4ed384-bfc9-34d7-8d62-9462804e0a7d | -11.20057 | -44.8763 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3137763b-ecfe-3103-9b09-705a1d886ca1 | -11.65857 | -43.67383 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 870793d3-a549-3cc1-886f-4aeed56781c3 | -10.98493 | -45.20359 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38283d21-dd68-3f23-b8ba-60607f86fe03 | -11.94481 | -43.47801 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db54a860-94d9-3823-a69e-a68e43b18d66 | -15.57667 | -44.5303 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 051e45ce-1f7a-327e-b08c-31cc1056d32e | -11.86215 | -48.02453 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0908daff-8d15-34d4-a40f-e4f868eeb262 | -12.05654 | -43.41747 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd191fdf-d7d3-31e7-b53b-01fd39180f28 | -11.67772 | -46.78421 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 207884b5-5039-3e77-8396-eb41e3b9bb31 | -14.33799 | -55.02938 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bf5838f-0b15-3781-86ba-9a13df700285 | -10.89521 | -44.83017 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 27e67f11-0f3f-319f-afa8-66c7d0d8d8a3 | -14.4375 | -43.96561 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8af854-6167-3f3f-82f8-a484d06ad44b | -16.56924 | -46.80118 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f7bccaa-7c1c-3d08-83f7-2cb5b335e231 | -15.9886 | -47.3501 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da4580c7-c4d0-3cc7-9aab-9743b46ef2b8 | -12.04226 | -43.37915 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8b29ece-ca71-3db6-ad39-c8ce3809782f | -12.04199 | -48.52939 | 2026-10-10 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bbe36c5-86ac-38ac-8afe-33c46cd1ac38 | -15.56629 | -44.51009 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eda9a789-e1ca-3990-adbd-766aa9ebc777 | -11.20214 | -45.29478 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ba02b1d-fe8d-3754-8df4-e81648e7596d | -9.9619 | -55.33652 | 2026-10-10 04:10:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3964eb84-bf27-3779-84c5-9d076efc8238 | -14.97715 | -47.54414 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9d6fef6-d776-386f-89ac-b6a451c15d5f | -15.7305 | -41.8515 | 2026-10-10 04:10:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc6e7209-36de-3ba4-a59d-8c0a90e95e7c | -10.89802 | -44.83393 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 255ab1eb-6414-3f7b-8f51-99e10432b837 | -11.99874 | -43.44038 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 362b4509-7385-344e-962e-3f7e3fd3c890 | -11.59994 | -43.72168 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc7dff1-9d2f-331c-85f9-312915390018 | -14.33482 | -55.01435 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08ce5eb4-5099-3037-8fe7-4954657cb8ec | -15.65639 | -48.14093 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4427be76-6977-3488-a6c3-659ff8862c9a | -15.90336 | -46.00091 | 2026-10-10 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0989048b-6921-358d-904f-de7ebec5e945 | -12.45392 | -46.53212 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20019799-193f-3a46-a2a8-8ffdf4f3076b | -15.38155 | -41.93928 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4d2e6b06-e3bb-37a8-b49f-03de0f2a5b07 | -11.95582 | -43.47265 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 673714de-3a99-371a-839e-7892e5ae5f2a | -15.7409 | -41.90014 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4a86f31-b206-3de3-9e4f-f6bdb6c92896 | -11.46938 | -43.38633 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1562b5e6-7428-31d3-9b44-c266899e0b00 | -16.12591 | -43.74271 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbcdd6dd-d139-3e7a-bcbf-d50ccc758103 | -13.1046 | -46.35246 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1a17835-c45d-373d-aac0-084260f07927 | -11.03368 | -44.02467 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d289b61f-8454-3bb4-948f-23c25406040e | -11.22512 | -44.83334 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ea28315-5b4f-3c1c-a72b-2b2191ebcaaf | -13.77586 | -48.1343 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b02ad7e-3bab-3fee-9f3e-e7d7f6d59c8e | -11.27735 | -45.18348 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81d60ba4-1ee2-3805-ac80-cc7082ced191 | -11.86466 | -43.57711 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87acc3fa-a68b-37fa-b81d-69a9bfc79d3b | -12.22966 | -44.69199 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3bcfeff-957f-3818-a610-9cc149750f56 | -14.23969 | -47.30534 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9348d7fe-d979-340e-8c29-a05a761da3a6 | -10.90144 | -44.83454 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 981668d1-f92d-34da-bdc7-369ffc743f5a | -13.68142 | -44.28932 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc2de3c3-3c67-3a06-abe9-c966c07ecc83 | -16.04697 | -44.82446 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb8c565-9d79-3e6f-8f60-26bf8f829cb4 | -16.76361 | -47.07072 | 2026-10-10 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fb2940f-7568-3e46-8d64-895d8d685b0e | -14.71708 | -48.22765 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2f581e94-661e-36c8-8eb1-411fa92a32ca | -12.11933 | -43.31966 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 262baccc-4eaa-339e-89c3-8132db1bfc7d | -13.37702 | -43.89161 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6789e485-76df-3947-bbfd-bf8e5fb7683b | -12.05765 | -43.41045 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54e025f7-63c6-3db0-83ca-05837e67a5ee | -11.18646 | -45.32478 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29c4c642-1605-3ae4-b3ef-9c65852b3c85 | -12.23267 | -44.67359 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d556337c-8c8e-3e54-9992-fddeca0408ab | -13.37758 | -43.88807 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4daa33f6-8265-3d7c-bd7c-a967581b5063 | -13.67705 | -49.1111 | 2026-10-10 04:10:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63ff452e-961e-3e3b-b60d-0cfe895a1c68 | -11.2905 | -45.20442 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a28c27b-5457-3e36-a604-debd7be09c6f | -13.15162 | -46.33482 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 415cfb73-c2ad-3ba6-bff7-7523d1f7175a | -14.57813 | -43.82927 | 2026-10-10 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a7d49f5-c6b6-36a6-9b5b-55c799126713 | -14.44752 | -43.92359 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b577d32-722c-319d-9452-43079d0fc526 | -12.29885 | -47.04314 | 2026-10-10 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5faf4b24-3cf5-360d-bae0-681e9a21f93b | -11.51751 | -48.73159 | 2026-10-10 04:10:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4180b32b-e31f-3eca-9116-f67d6fb81054 | -11.85513 | -43.52842 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf07aff-dcca-3a0b-a7db-de4f4ce1c696 | -11.97123 | -43.48241 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2c766fc-e6ed-3b71-83f9-faeec35f4165 | -13.52641 | -47.42176 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d26fefc0-6ca4-3a56-8140-4c724d76293a | -11.01139 | -45.41368 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1f2d307-2ca3-3d00-9acb-81c00a81e1ed | -13.64947 | -49.40596 | 2026-10-10 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28b7aa40-e872-3e54-a5e2-b4a142c039c2 | -16.81996 | -42.30152 | 2026-10-10 04:10:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77932759-eeac-3c50-9957-5396a14651df | -13.84861 | -44.35038 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0100c24-bed4-391e-b695-b54037f5c69c | -11.20423 | -44.85366 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c69e568-3a57-3317-9cf8-7e3128970e82 | -14.45794 | -43.94352 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README49.md)
