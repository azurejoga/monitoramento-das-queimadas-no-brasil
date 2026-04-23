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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e650e3b3-4b90-3839-a606-de70c45d5705 | -11.7917 | -43.6163 | 2026-04-23 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b275f619-386d-3ba0-8b85-c2b315a7a97a | -11.772 | -43.643 | 2026-04-23 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8b9d1546-cea1-30de-9920-1cf61114c4e5 | -11.7917 | -43.6163 | 2026-04-23 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5a385d10-b003-3340-bd74-95451108d865 | -11.772 | -43.643 | 2026-04-23 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2d1dc0bc-09ab-338a-8c25-b6719ad705cc | -21.33401 | -47.07594 | 2026-04-23 00:13:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 51c2aeee-12ae-372b-a0e3-40cf461178ee | -20.23705 | -46.80469 | 2026-04-23 00:13:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bb9d661c-99ae-371e-b50a-f3cd0b205398 | -21.70446 | -48.43316 | 2026-04-23 00:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 36da0c1d-c888-368c-a298-590d7d914a10 | -20.20149 | -46.74341 | 2026-04-23 00:13:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0314eb3c-ab20-39e3-843a-e6b2b5a550d1 | -20.23575 | -46.79536 | 2026-04-23 00:13:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0efefed4-8de9-3278-bbf1-15dd7d425f36 | -20.6307 | -42.50056 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 89019751-b9ea-3a90-b87b-ba4a587298d3 | -21.70446 | -48.43317 | 2026-04-23 00:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2ea93214-df9f-3f22-aa2a-e0d9987b1863 | -20.20149 | -46.74343 | 2026-04-23 00:13:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae31ee62-d4e9-3307-868b-a7588ff0d55d | -18.27697 | -52.89061 | 2026-04-23 00:13:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 40281227-be3f-39fd-819b-80ee5e12db21 | -21.33529 | -47.08539 | 2026-04-23 00:13:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45220a3a-0c87-3ae2-a07b-b6ca527d2603 | -20.62415 | -42.49295 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 78833ee5-7f97-32d9-b1cb-757da66a6247 | -21.70317 | -48.42291 | 2026-04-23 00:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efeaf869-054c-3e59-b03b-867543bd091e | -20.20018 | -46.73407 | 2026-04-23 00:13:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bfc3c0d2-5b12-31e8-b807-63a5dea5bcf0 | -20.20019 | -46.73405 | 2026-04-23 00:13:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfac80b5-4d51-3690-b815-2f767b04f447 | -21.70317 | -48.4229 | 2026-04-23 00:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcd474bc-a85f-333d-b2a4-749318fb3e1c | -20.62415 | -42.49294 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 658bf2d0-92cb-30b3-b3ca-c5c8d13b13a1 | -21.39547 | -48.67148 | 2026-04-23 00:13:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 93efb50e-cd7e-36cd-a8ee-a45d784d92ed | -21.39679 | -48.68189 | 2026-04-23 00:13:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 23633cbd-7e2b-3499-949b-510ba412e67d | -20.38878 | -42.81804 | 2026-04-23 00:13:00 | TERRA_M-M | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 3d5ab628-e3f6-3d08-8ac3-a8c21df9add8 | -21.39548 | -48.67147 | 2026-04-23 00:13:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 801e984b-2e80-3b2a-9799-a699c2d4dede | -20.23575 | -46.79538 | 2026-04-23 00:13:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 948ed5bf-6901-3e40-a72c-ff1c37e1f89d | -20.38878 | -42.81806 | 2026-04-23 00:13:00 | TERRA_M-M | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 3285ba19-00e7-3d12-9adf-f6568a8245e0 | -21.39679 | -48.68187 | 2026-04-23 00:13:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ff2df86-3f59-3244-ae22-fe80da5edd18 | -21.3353 | -47.08537 | 2026-04-23 00:13:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b20f655-143e-3411-9c4c-0eed91db2e4c | -17.16431 | -46.83575 | 2026-04-23 00:13:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e2b5d323-2542-3663-9134-96b498bc5d3c | -21.05636 | -48.67167 | 2026-04-23 00:13:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| a172d9db-864d-398e-a905-44bc76ce919f | -18.27697 | -52.89062 | 2026-04-23 00:13:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 044fb5e2-4d41-315d-80f7-137067be894b | -20.6307 | -42.50055 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 762ad10a-5e9a-3f75-8896-bcb107089d83 | -21.33402 | -47.07592 | 2026-04-23 00:13:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 69193de4-fe12-3c23-a297-35dbd80f8d24 | -20.62814 | -42.48535 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 1c0b731c-b7d7-3606-905a-3ff419522348 | -20.62814 | -42.48536 | 2026-04-23 00:13:00 | TERRA_M-M | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 89d9d47c-5565-3fa1-80e8-a70348318cda | -17.16431 | -46.83574 | 2026-04-23 00:13:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d905638f-ea3c-3f8d-bafe-72100f489b66 | -20.23705 | -46.8047 | 2026-04-23 00:13:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d657e014-3b13-3f3d-aae1-d95d1541c4c9 | -21.05636 | -48.67168 | 2026-04-23 00:13:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| b54f9d9b-275c-38f4-8133-db9a289352ee | -17.48502 | -51.08854 | 2026-04-23 00:16:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 65683f1b-37bc-3c4e-9aaf-db7eb79fc262 | -15.18627 | -43.98326 | 2026-04-23 00:16:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c5cf7603-0055-3080-b0b8-bb8f5f7b4ac8 | -15.15372 | -41.29302 | 2026-04-23 00:16:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 75bc0ad9-3566-37e8-bb76-0a38ae250904 | -15.15372 | -41.29304 | 2026-04-23 00:16:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 606dbb3c-6981-36df-a383-f333a84fc0d7 | -13.38284 | -45.32341 | 2026-04-23 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8080e7de-2832-3f6d-b53f-251f394d1d0c | -15.18627 | -43.98324 | 2026-04-23 00:16:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9422692a-75b9-3a6a-9dc3-233ad5ef5889 | -17.48503 | -51.08852 | 2026-04-23 00:16:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| c8ff437f-759b-3dde-830a-67e23fdebc24 | -13.38284 | -45.32339 | 2026-04-23 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1bb68456-7095-3ce5-b3b9-6ba5c8d986c8 | -13.373 | -45.32499 | 2026-04-23 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e716a35-f60b-3b66-b189-3474bd79bbf2 | -13.0254 | -43.59542 | 2026-04-23 00:16:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| aa904f25-e04e-344d-a2ac-7cb66cff304d | -13.0254 | -43.59544 | 2026-04-23 00:16:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d9cb9fec-5564-3b65-8042-1ed8211a2082 | -13.373 | -45.325 | 2026-04-23 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 898aefb6-be2c-360f-94aa-1a2b97eb2c9a | -17.48653 | -51.10089 | 2026-04-23 00:16:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f22058ae-6887-3d73-b928-76c7518fa9de | -17.48653 | -51.10088 | 2026-04-23 00:16:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e27b5c63-f76f-3432-8445-08a91e206899 | -11.78166 | -43.67005 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 9da6d209-feba-3439-ae53-1af94fef62b4 | -11.79703 | -43.62806 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ac4e0c5b-9efc-3005-91e0-2fab5c1b05d4 | -11.77919 | -43.65393 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 74e772ab-76a2-3236-84f4-4579c50c9d7f | -11.78558 | -43.62995 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e8073aa7-ec33-3b3e-9321-92bce7e2bf77 | -11.7767 | -43.64772 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 7a70f4bd-986a-3f85-9044-6ada0d7a62cc | -12.28318 | -44.61886 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 1b8b121f-25ae-3709-9361-fdd29fb3a963 | -12.56521 | -45.47506 | 2026-04-23 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 228b6993-8261-39ea-933a-dee2dbbcdd96 | -11.76784 | -43.66547 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5a3abd3c-1ac2-3381-b677-429f703bdce9 | -12.28515 | -44.63192 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d67ebd39-9248-33ce-84f0-11714c03eb4d | -11.76784 | -43.66549 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8ec37df9-1196-3c55-b58f-6e9669c1d27a | -12.28318 | -44.61885 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 1650e62d-9c31-307d-a7bb-a9dedb4f0374 | -11.78305 | -43.61415 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 130f817b-c6d4-39ba-807a-0d2c43a75a95 | -11.76777 | -43.65578 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f4a0d6bc-f222-32a4-b9e8-42c525e07313 | -11.77925 | -43.66356 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| cbb02c4e-26e5-3ffb-86ef-7c244d0f02e0 | -11.78166 | -43.67004 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 70a5d6e3-dd80-37e6-9366-828d703458fb | -12.27268 | -44.62066 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 07ef2d7d-40f2-3177-bbde-3ab630d978f9 | -12.58492 | -45.47185 | 2026-04-23 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7317184f-02d4-31bf-bfd0-73d2c0c1174c | -11.7767 | -43.64774 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a58ad1d2-d268-3811-86cc-0a78cafd6335 | -11.79703 | -43.62807 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f34be6d7-1efa-3ac6-b995-e9d167620f9d | -11.76532 | -43.63992 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 47cc3a51-0dd3-33d4-97a8-40e996c75e16 | -11.76527 | -43.64959 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2b7c3778-79aa-3c71-9537-2d810e30f44f | -11.76532 | -43.63991 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 26274491-22ba-394d-bb70-f2566701ae04 | -12.58493 | -45.47183 | 2026-04-23 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ff5e34ed-02a1-3c07-9c8a-2608188e1e70 | -11.76527 | -43.64957 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 70d48da6-21e5-3500-b4d1-b15419ca7aaa | -12.27268 | -44.62067 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bbc159eb-20cb-35f0-be89-9f1746d56c4f | -12.28515 | -44.63194 | 2026-04-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fc3ad2f9-b9de-3c79-9b50-d420f490aaff | -12.56521 | -45.47507 | 2026-04-23 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ab72605-9522-3da7-a624-36d265cb5f68 | -11.78306 | -43.61413 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ce0d06b7-cb7a-3ef5-adb8-0ca4d21b53cf | -11.7792 | -43.65392 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 211db2b3-72f7-3122-ab94-4728bde28c56 | -11.76776 | -43.65579 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e7af5b94-5b45-3b7a-9af2-94dbd6bf09e9 | -11.78558 | -43.62993 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 681ccd06-a42e-3ba7-b5c2-ed4ba586eefd | -11.77925 | -43.66358 | 2026-04-23 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0d52831e-511c-3cec-9230-37ec64ec4886 | -6.5631 | -51.1126 | 2026-04-23 00:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a77a064-4487-351e-8a24-da570eed4c91 | -11.772 | -43.643 | 2026-04-23 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b91f4e1a-2a1b-36ce-afb4-8f83c4c177f9 | -11.7917 | -43.6163 | 2026-04-23 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1b4e97d3-6f3c-38df-be8e-f142ffe1465b | -11.772 | -43.643 | 2026-04-23 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a89b14ea-da6c-3398-98e4-d22acebb493e | -11.7917 | -43.6163 | 2026-04-23 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6a1bf911-85e6-3c5f-900d-6179388ea938 | -11.7917 | -43.6163 | 2026-04-23 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9b6e4bb7-7488-3fed-9e5c-66f09c88b264 | -11.772 | -43.643 | 2026-04-23 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6980350c-4d6f-3224-9e49-e5feaa919cdb | -11.772 | -43.643 | 2026-04-23 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 81dfca44-d238-3412-8339-94355e5b474c | -11.7917 | -43.6163 | 2026-04-23 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8a8b8ab6-ce93-3f3e-96f6-b6c6ae413949 | -11.7917 | -43.6163 | 2026-04-23 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a5c1005a-74e8-3c1d-9c9f-93a1774fb94a | -11.7917 | -43.6163 | 2026-04-23 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 78a71ddf-12a5-31ef-b24d-a5f708a361f9 | -11.772 | -43.643 | 2026-04-23 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 13026f9a-f5fd-3312-9043-80debf2ac06f | -11.7917 | -43.6163 | 2026-04-23 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 61b9f3f3-0681-3d06-9fbd-9bfdaa9bb624 | -11.7917 | -43.6163 | 2026-04-23 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| dd14dd4f-2a18-380f-9b5f-ea10d3257371 | -21.2708 | -48.842 | 2026-04-23 02:50:00 | GOES-19 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| a68248b5-ce23-35ce-b7ab-51f00d3d2e93 | -15.1525 | -41.29512 | 2026-04-23 03:10:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
