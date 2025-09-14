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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd8d78fc-110f-3129-b713-83d887419cc6 | -22.20062 | -48.35147 | 2025-09-14 03:51:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ae57f127-feec-3af4-9f0b-6d6dedb8640d | -18.37796 | -48.34127 | 2025-09-14 03:51:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b2c1cbe0-a3a7-323d-840d-3fc4b1e1fc1c | -24.4559 | -50.73951 | 2025-09-14 03:51:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd25e912-5ea2-3bee-a0d6-cb3bb793b198 | -22.04777 | -47.40928 | 2025-09-14 03:51:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f09e6015-1083-345e-a620-0f418c2b5f01 | -19.99639 | -46.90866 | 2025-09-14 03:51:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7ff952e-857b-36db-973b-9bd014cead49 | -23.87051 | -47.59008 | 2025-09-14 03:51:00 | NOAA-20 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5524f882-ea27-339f-ba7a-5ebec80d1ca2 | -17.8323 | -50.42255 | 2025-09-14 03:51:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13283ab6-7205-3d05-9860-fb6a2218bb1c | -17.36451 | -52.90831 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 931818db-6bad-313d-addc-5dc7c314b158 | -23.47778 | -50.85047 | 2025-09-14 03:51:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| da0e8a59-22af-30cb-a57c-e4a66b943596 | -18.98635 | -44.23178 | 2025-09-14 03:51:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2992a426-149a-3c96-bc83-29b4031419ea | -19.45776 | -43.68758 | 2025-09-14 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0facdd4-e57b-3b94-8d16-2d3d928eb33f | -18.59138 | -47.19894 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 116acf77-6608-3dcc-9b49-bb9481af4855 | -18.05949 | -50.74174 | 2025-09-14 03:51:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7616e3b7-716b-34c4-81af-9ac0cedf98d9 | -21.09457 | -47.17656 | 2025-09-14 03:51:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d8eb848-7708-3af8-ab71-ecb488f68557 | -23.15727 | -47.57729 | 2025-09-14 03:51:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 534e39bd-36cc-33c0-8385-06dcc7280fbd | -22.73358 | -49.89931 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1c42c0b0-0977-3503-9c39-833d32825a35 | -23.14638 | -50.40533 | 2025-09-14 03:51:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8cddb5f3-929d-349c-91d2-cc8943892823 | -20.47957 | -47.45987 | 2025-09-14 03:51:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7774449-a021-3227-a3b5-aa07ad14608b | -22.17672 | -49.61552 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c6fdb0f3-3a69-371f-81f9-74c886084d15 | -17.83321 | -50.41839 | 2025-09-14 03:51:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| addd7755-022b-3e8a-b2d3-b70a7a876fcd | -19.9973 | -46.90403 | 2025-09-14 03:51:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 170dfb15-2d96-3e98-8d38-6f8ba5935994 | -21.06561 | -47.85076 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d56bc61c-9fa7-30ec-b55d-d9b19655fcfa | -19.09258 | -44.49034 | 2025-09-14 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 49a3af3c-b7a7-3f29-8684-1c854e6703e2 | -22.72852 | -49.89807 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8ebaed1-fd44-35c9-8f8f-fc55500f3007 | -21.06101 | -47.84965 | 2025-09-14 03:51:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f567f723-a016-3857-91b1-2662f32ab612 | -22.05234 | -45.65575 | 2025-09-14 03:51:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1ee0f22f-8879-392c-a767-ea1e906656f8 | -19.0916 | -44.49556 | 2025-09-14 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06ffc83f-da5b-3e9e-8f23-825291a28252 | -20.08999 | -46.89424 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51aca4de-4c7d-3dfc-b187-18ab50f7df83 | -21.41881 | -46.60704 | 2025-09-14 03:51:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 38652971-5c34-3a13-b079-dd3961011a5c | -19.18117 | -42.66765 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35789702-ebbc-3e90-84c8-881a3fae5267 | -18.95469 | -46.31133 | 2025-09-14 03:51:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e65c9868-6f70-389d-96b9-8e08fb261457 | -22.798 | -47.80246 | 2025-09-14 03:51:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd35547f-02dc-37ee-9ff7-daa4bacfecc3 | -19.0955 | -44.49633 | 2025-09-14 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00dfce6b-2fa0-3ebd-a0a6-5d6dc0f442a3 | -18.16111 | -49.20288 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fff30bb7-3e5c-3ac3-8c06-19e5815c2827 | -22.04999 | -45.65694 | 2025-09-14 03:51:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 168d04da-111b-3f43-a11d-ea49ff2ff411 | -23.17402 | -47.56193 | 2025-09-14 03:51:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 621d7407-1446-3793-9131-9d379e272de7 | -23.47497 | -50.84851 | 2025-09-14 03:51:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89577e25-e32d-3cfd-9bc9-b757079e3383 | -22.28837 | -45.96532 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa854b81-e0a6-3dbe-a7ee-db9b3a39fd99 | -23.1731 | -47.56655 | 2025-09-14 03:51:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73a85766-d25c-3f57-b0da-8dac1283c6f4 | -18.14582 | -49.1962 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 800816cb-0a78-3482-aaad-1e399ddbae4a | -20.08552 | -46.89348 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 531348f5-f969-365a-ab1a-be59b8277e50 | -18.46921 | -46.93531 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a91c222-312a-329d-a927-811552b4a928 | -20.12564 | -46.8772 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81dd75be-1d1f-3194-bff8-ceaeaef9f5a1 | -18.90843 | -47.98122 | 2025-09-14 03:51:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bb31d8d8-212e-3ccc-aeb3-6d9fc4130fef | -18.60954 | -47.18087 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d05cffa-4467-3f54-b7ac-32f65115e679 | -20.12119 | -46.87643 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df2abbcc-0ecf-3087-91fc-a556c5b2d5a1 | -18.37734 | -48.34426 | 2025-09-14 03:51:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 220ed81e-4625-30f7-a9df-72f70467eeef | -19.67261 | -43.11075 | 2025-09-14 03:51:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b09a8e49-0b58-390e-8808-97e6a6dffeb7 | -22.7879 | -46.79658 | 2025-09-14 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9fe6e53-6792-3ff7-ac6e-b1dd8659ea19 | -21.76438 | -45.45856 | 2025-09-14 03:51:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72af5f0d-5dfe-321e-a012-b1491a45c2d9 | -19.71288 | -45.44703 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90f9267b-92f5-326c-bdc9-283628fe5aa7 | -20.44836 | -45.24017 | 2025-09-14 03:51:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86dc9dc2-b3c3-3de8-8bab-cddd02c76fc4 | -22.28033 | -45.96355 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 8803d2a4-109b-357b-8d0a-8ee773a604db | -19.70697 | -45.43367 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36e9f5ce-de53-371e-9081-1060a0f78c84 | -21.6296 | -46.81765 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a65acc6e-8e7a-3c38-8ed8-c69cb32432df | -22.27963 | -45.96723 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 7387c124-8062-3453-a09b-02e37ffa0c5c | -18.26354 | -46.94604 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a6baf8b-75b8-3373-9b3f-0743b390c0a3 | -22.7321 | -49.90606 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46a2f3e3-0e29-3ba6-accc-eb4b6ce9700e | -18.19436 | -47.91916 | 2025-09-14 03:51:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 220193aa-ae43-3038-a39b-6027877cdab2 | -23.7509 | -51.76332 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 6ad3d059-6c5e-3c0a-bb29-b77f2cb7727b | -18.15651 | -49.19826 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d0585ad1-cefb-3e01-84cc-898f54ef08a1 | -18.62457 | -47.17823 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27d86b83-2e08-3f37-a5f6-0acf424dc4fa | -21.64732 | -50.1958 | 2025-09-14 03:51:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44d64fd1-d5af-333a-b5be-e173f2129e9f | -20.60107 | -45.22651 | 2025-09-14 03:51:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3b52be8-d84a-30c7-8e2f-2f41299819b6 | -20.25171 | -47.8108 | 2025-09-14 03:51:00 | NOAA-20 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db2851ef-a0d9-3e58-95e8-5db99b0131b7 | -18.62704 | -47.19007 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 956b8dc0-84e6-3e53-9361-83f2e0720e28 | -22.79889 | -47.79808 | 2025-09-14 03:51:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4be63e0-dd9a-346b-a220-a752710e5895 | -22.73432 | -49.89596 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 25885cd0-0c79-3fcf-b5b6-aae5edcbf13e | -18.9121 | -48.01305 | 2025-09-14 03:51:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4b47971e-9772-354f-82f7-bd01edf8d935 | -18.16403 | -49.20311 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a17d4c27-b778-360f-a535-44f226345548 | -19.17336 | -42.67048 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 172ab0fb-4063-3a35-85b3-a4d5d25d46fb | -22.99027 | -46.46115 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b6bf205-b56a-32f0-b791-8a588d58cd51 | -23.65862 | -47.60015 | 2025-09-14 03:51:00 | NOAA-20 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e2100cb2-ffae-3dd0-8cb3-69211e679e6c | -20.08363 | -46.90294 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0600f82-c849-3ea0-9377-bb3a9f774e83 | -22.19475 | -49.60546 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2bd0a162-65d9-3533-ad0b-927eb1c6a3ae | -22.29738 | -47.95331 | 2025-09-14 03:51:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bee0bf1-48d6-361d-b664-45debbcdc1de | -18.14126 | -49.19135 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af92547a-ffcc-3233-97d7-72bf669689ce | -21.63052 | -46.813 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c44e50c8-e6a8-3b57-a1bb-06eef797e04a | -21.76834 | -45.45924 | 2025-09-14 03:51:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0d506c7f-fbe6-34cc-92db-f6f28badb7ee | -18.4681 | -46.94094 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bb57c48-4888-3a99-882c-14efadd9be4b | -22.49341 | -47.41337 | 2025-09-14 03:51:00 | NOAA-20 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e1c244fa-6df7-3443-b785-7e4309ae5690 | -21.21503 | -45.82604 | 2025-09-14 03:51:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81d89924-3d53-3541-94b3-36b2f8187aa2 | -23.74905 | -51.77129 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 3c45344c-e284-3b0a-90d6-e6bc20cde422 | -19.17556 | -42.65774 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e995ffca-e9a9-3c1e-8218-1c7d58a47567 | -21.92221 | -46.55409 | 2025-09-14 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e9022118-bd1e-36b7-86d3-3e75ba062a09 | -20.44767 | -45.24385 | 2025-09-14 03:51:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0212dd46-faad-3bf6-8636-dce45df665b9 | -19.70213 | -45.43679 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76fa4a5a-089c-3912-afa5-ca5a9f0e78f1 | -23.65951 | -47.5958 | 2025-09-14 03:51:00 | NOAA-20 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8d1b93fc-6c01-39b5-bc10-b997b5689cd5 | -18.15736 | -49.19414 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 63ecdf9e-236c-3f49-9d27-29300bd30c45 | -23.79189 | -49.94406 | 2025-09-14 03:51:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8149af65-aeef-3f53-b4fa-4d93686fa49a | -22.51987 | -52.99981 | 2025-09-14 03:51:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 80be1e22-ae91-321a-8ec3-12a08258d285 | -22.20532 | -48.35233 | 2025-09-14 03:51:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0db38d24-3c49-35d0-83ea-adc37c970ffb | -17.3836 | -52.92632 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c857841-d93d-3a05-9401-296139ea9ff3 | -19.1769 | -42.67121 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d9b1c0dd-7430-3500-9af2-3db8475b09a7 | -23.21943 | -49.36353 | 2025-09-14 03:51:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 74e1c118-9214-315e-ab82-69fdf0c88c97 | -19.45617 | -43.68388 | 2025-09-14 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26472993-13c6-3d7f-9c57-4a26e3bfaf3e | -19.62959 | -43.7314 | 2025-09-14 03:51:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5f4205b-f8cf-3e81-abb5-81c692c42a16 | -22.29631 | -47.95852 | 2025-09-14 03:51:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67874b83-8527-3130-b482-7f6dc1e88369 | -18.62922 | -47.17915 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 954d96f8-83f3-3efc-beb6-bd942194fa4f | -19.14736 | -44.84476 | 2025-09-14 03:51:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
