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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45ddf870-d3e7-33b4-b1b8-233ce2d01ad2 | -12.47407 | -45.33689 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 670e4b43-dd0c-3dfc-bcc9-6402b4abf9e4 | -18.04608 | -44.3741 | 2026-08-11 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bccc213e-f597-304f-97dd-418562c549f7 | -16.66356 | -43.63314 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7722d1e1-d0f6-352d-bd2e-75e835b4babd | -13.58152 | -46.2801 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 013add2e-016b-379e-9968-2bdbe80cf1ba | -12.45732 | -45.31515 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801392ae-4f5a-30bb-8a2d-b26e99a833d3 | -13.56781 | -46.26657 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 55d77b8d-2875-3e7f-b790-262b513da6f0 | -12.45847 | -45.30917 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e43b2f31-8879-324a-9ade-caaa5a39c0ba | -13.56111 | -46.30028 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ae664a5-21ef-3ceb-a133-350efd6d12ff | -15.01437 | -46.57825 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 041e40c7-f578-3217-9e08-ec42bd228f89 | -14.45441 | -45.67952 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c50c8edb-cf16-36cb-9e36-7d482a94c37c | -13.57304 | -46.26774 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ca4e8349-303e-3d76-bb48-8b03bf5b95bb | -15.02148 | -47.03749 | 2026-08-11 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b84fa57-b9fd-33e1-af64-ac026cb6977d | -17.89425 | -44.46013 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0035ba4c-6212-3692-9497-bbed1811b49f | -13.57171 | -46.27444 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e2394862-1d73-33ad-95c5-ed2a335f8ea3 | -14.27543 | -45.31672 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dc9829f-79e4-3d2c-ab51-215d73513b79 | -11.47909 | -46.62466 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 251a42ec-8f30-32ef-8f9a-56a29ed696fa | -12.48819 | -45.29028 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15811421-e184-3cb5-8d90-307c8d9133b9 | -12.47075 | -45.32691 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c1c86db1-31f4-3e0f-b788-de9c926b6da1 | -13.51762 | -44.13801 | 2026-08-11 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75b31e94-e4f6-38f8-a704-03504d58101b | -13.64666 | -46.25383 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ab5936-b0bf-37d5-851b-ce808eceb310 | -12.48763 | -45.29321 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df5f67e2-f427-3dd7-a754-2611bb191984 | -14.44448 | -45.67742 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3a8322e4-f0de-3688-913e-71d4bcca56ef | -15.87368 | -43.596 | 2026-08-11 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6169a5b1-b692-3a96-8611-bcae29321616 | -13.56972 | -46.28448 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fd8c9ef1-b142-35c3-8da8-d6a67c83e69d | -15.44021 | -41.38148 | 2026-08-11 03:49:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 03edcfa1-8f55-347e-82ab-f1afc7d816cb | -15.02349 | -47.03748 | 2026-08-11 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e3d6e78-59ee-3cc0-ac20-d098d0fbe455 | -14.45737 | -45.69078 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 603da5bb-22eb-3d42-8c1f-6c9631fc9240 | -18.04351 | -44.37687 | 2026-08-11 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 176144df-9887-385e-85d8-6af233ad9cf3 | -13.57237 | -46.2711 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b17ed70b-c497-3246-8359-702f8fc9f510 | -16.65927 | -43.63573 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ed3ff21d-a1cb-30ff-9ad1-4f44a4391a8c | -14.12071 | -45.61409 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17491d2-38b3-3dd8-af34-87c244e09250 | -12.48481 | -45.30798 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 21b6f5d7-b21e-3fa5-9ead-2ada0c40c9fc | -13.57563 | -46.28223 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4aa46b7-a73b-315f-8ffd-ac16fd8416b1 | -16.66344 | -43.63665 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| cd2a8a1d-3ef8-301b-89ae-a580f1c6a179 | -12.48197 | -45.32288 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22f5cddf-0263-3820-9e14-89546379247d | -12.49991 | -45.28344 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 47ecef4e-3cf6-3319-be6c-01967702a832 | -12.48083 | -45.32888 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dc6eb4bf-9e67-3601-b5b8-d4fb31f9add7 | -15.03576 | -46.58001 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70779691-234b-300a-876b-9826eaea5554 | -10.42077 | -46.66523 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e38f7291-99c6-3c9e-8775-9c70c2e216c6 | -14.45623 | -45.69662 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27e6410b-c69d-39cc-927d-dd83ef7a46c7 | -12.4719 | -45.32092 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6a6a1c76-fedd-3378-b358-6146722d7496 | -11.87744 | -40.96659 | 2026-08-11 03:49:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb6d3ecf-da8c-35f9-9f0d-1117508a2b8a | -13.07664 | -43.06113 | 2026-08-11 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99acc0d6-9d89-3926-ae4b-470746fce857 | -12.47854 | -45.3409 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 95c2d029-ada9-34d3-bbc1-4a3eeba305eb | -10.41691 | -46.68558 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 84000ab1-8913-3268-b3a4-1abf5296c336 | -10.42414 | -46.67865 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12e62309-1520-347d-98b5-fc67a2c26523 | -12.48425 | -45.31094 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 60463e08-23a2-3363-a3a6-adc1fb0096d7 | -12.45156 | -45.34509 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10a0c2f7-c6a1-364b-b8a3-1523f876d7eb | -12.4579 | -45.31215 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 170b0161-0198-3694-9bc6-eabd86706b7b | -16.66283 | -43.63716 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 407b998a-de5a-3e13-a2f4-c7b6d74af709 | -13.05793 | -43.06616 | 2026-08-11 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f0f93d4-b0bb-3339-be55-a30131102166 | -4.26905 | -48.18859 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 6acb5edb-fce9-39bd-acb7-30e1cde45e27 | -4.26739 | -48.19463 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 27051932-bc2c-3d6d-9b8a-df3fc54bb576 | -17.73065 | -46.21469 | 2026-08-11 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12c78f8a-6322-391b-b151-6dfecbfa5aa1 | -15.02275 | -47.04108 | 2026-08-11 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32874679-ad4a-3465-b810-7d85593606a8 | -14.12098 | -45.63904 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4a0475b3-d3a9-3c1a-b8b7-0ff2bfba7648 | -15.00898 | -46.57805 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b933cd77-cd1a-39f9-a3b5-db4ad2cf8929 | -14.47113 | -45.69978 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4bea984-85a6-3229-8ca3-a7760d074ae1 | -13.59199 | -46.25471 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f8ad477-3573-37a6-ae87-28f6f6de40c6 | -13.56892 | -46.31612 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b24ab8c-cd77-37a9-bda8-239bc4bd2ee2 | -4.2605 | -48.19333 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 722ffaef-fc67-3cf9-ae61-7b6d03c71e75 | -11.31366 | -45.22404 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54fe2f6f-af1c-38a7-81cf-02763f398f25 | -14.46731 | -45.69288 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f4a2b7a-42e6-3cfd-b07a-22aa40ce9fac | -13.55383 | -46.3093 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae63829c-31df-3fa9-b38f-6368cc33a8ae | -12.47247 | -45.31792 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8dc97196-ed10-36fe-88ea-a48e3e0aa25c | -17.72461 | -46.21959 | 2026-08-11 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1708370b-84df-30ad-8b80-69ee39e1081a | -10.88945 | -50.38057 | 2026-08-11 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56b5ac67-fc7a-34b5-9a33-a3fdfb12d7bc | -4.26105 | -48.19364 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 150207f8-0870-36f6-b513-aff643e634f5 | -14.45125 | -45.69557 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6c97a26-2c5b-334c-b820-54b273bf8277 | -15.43885 | -41.38373 | 2026-08-11 03:49:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3e1ae3e0-de67-3158-ad3b-99bd137bf1ff | -14.61552 | -47.66274 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f2ae0e0-a021-3efa-b046-52bb26c62801 | -18.02784 | -44.40013 | 2026-08-11 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b74ff79b-9cd7-3487-b57d-8dc270893759 | -10.4237 | -46.6809 | 2026-08-11 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| eaedf93e-3b63-3436-8c8a-6127db4153e5 | -13.5701 | -46.2584 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 7e23d8ec-c7ba-3c7a-bba2-1d7b3f224351 | -14.1249 | -45.6368 | 2026-08-11 03:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 032304c7-b2ca-3087-9763-f9de93a78917 | -8.9039 | -60.5769 | 2026-08-11 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| defe80d9-b89e-3043-a8f9-76c18d80c580 | -14.6268 | -47.6506 | 2026-08-11 03:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d5feed07-fbe7-380f-b01b-833e50cb135f | -14.4734 | -45.6914 | 2026-08-11 03:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bc6a64b5-8681-36f6-ba52-5315f5dd576d | -13.5502 | -46.2844 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 451807ea-d170-338d-9679-8fbb31a8e37a | -13.5696 | -46.2813 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 382.6 |
| 76ddbef7-551a-37a6-8220-cdc34c82241b | -13.589 | -46.2782 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 196.6 |
| c223c855-94d6-34c5-ae70-0162e94588fa | -4.2635 | -48.1799 | 2026-08-11 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 09a93660-04f9-319c-b7e3-d19513df7591 | -13.5691 | -46.3042 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 81b6781e-e13b-34b3-b98b-db117a80789c | -13.5894 | -46.2553 | 2026-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| e09402c8-1d2f-3d7f-a663-9218978d4cb4 | -4.2634 | -48.2016 | 2026-08-11 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 80c2c7e7-d7a3-3a26-a79b-a45be7d2fbd1 | -21.46822 | -48.61346 | 2026-08-11 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f4b8b1-0387-3da9-9c20-d2baa307b1ac | -22.18469 | -43.24119 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0342028a-13a4-3608-a598-cc695ac49ad7 | -20.39301 | -42.11164 | 2026-08-11 03:51:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f81cb5e-c0a7-3363-b4ce-1211e078ff42 | -19.00093 | -46.1774 | 2026-08-11 03:51:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60708d35-05b8-36d5-a1a0-9d7b332ee32d | -20.38487 | -49.30765 | 2026-08-11 03:51:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f7a20f9-01b6-35a1-9df7-7b52d8b0765a | -17.12984 | -51.68717 | 2026-08-11 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db8f063d-ff2c-3fb8-b54d-4fb40e674498 | -20.81705 | -44.5486 | 2026-08-11 03:51:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| da335d70-9b45-3ff9-a6e8-95a1cf38707a | -22.27629 | -42.85051 | 2026-08-11 03:51:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 04c2afbe-c92f-3d2c-97b8-7152a6ffa75b | -17.13422 | -51.66395 | 2026-08-11 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0fdabf0-a043-3018-a36f-fa1d34f729fc | -22.34654 | -43.04086 | 2026-08-11 03:51:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 21c500ac-7e92-3937-9bd8-7d9947c16bde | -20.38936 | -42.11112 | 2026-08-11 03:51:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a74d17f3-5817-3eb4-91b2-16a73e16a6ec | -19.25639 | -46.45727 | 2026-08-11 03:51:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efeb6f24-8e0c-32e7-b9a4-69e2af93919d | -21.4622 | -48.61579 | 2026-08-11 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41129318-8545-3e91-bf99-15b67693efa1 | -17.13562 | -51.65785 | 2026-08-11 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 689354f2-2fba-3d20-bd60-e08452f4466b | -19.25738 | -46.45628 | 2026-08-11 03:51:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
