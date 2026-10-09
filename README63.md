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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2ea0aa1-8748-3b40-b139-bf1f19478548 | -12.81488 | -44.64853 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29b7d12-2838-347f-b0f2-6ffb5319c533 | -8.90272 | -45.21599 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ee3b7a9c-5bdb-357f-a432-cc335386ad84 | -6.88054 | -45.91153 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 568a958b-9132-3d0a-8423-d4d04712d5d5 | -7.51041 | -47.33225 | 2026-10-09 03:45:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 131416d6-d890-3651-a8c0-920df7c9e2e8 | -11.2193 | -45.32461 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01376c19-e864-3b5e-88d2-3af6f27dd936 | -11.06684 | -44.08291 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee4ceeb5-1970-32c9-a338-50629ca0aff1 | -11.26443 | -46.26649 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9714670e-cb23-3667-a9aa-b08b48f97897 | -13.35032 | -39.27166 | 2026-10-09 03:45:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 012d368c-e2d7-34eb-b593-2a4215cdf606 | -11.25614 | -46.27143 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 860960d8-2728-3cad-9b82-7833a0debb6f | -13.6352 | -44.42199 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4f03e1d-0d8c-30a3-8702-a31c474114fc | -11.18105 | -45.3079 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b021d17b-727b-377c-9066-0895ca8e50fc | -11.2532 | -45.2509 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4ad4149-6326-3aa3-9aa3-da3d8356a403 | -13.49758 | -44.37273 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df20640d-7eb0-34bb-9f4e-ae834ddbf2ea | -13.81505 | -44.19224 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3aa9564-6264-3b5f-98ba-028b9c7118b1 | -11.00402 | -45.41587 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 32432671-d25f-3cfc-9265-05f83a336398 | -12.8142 | -44.65197 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bc76200-639e-310f-af43-4ef67e90923c | -11.30289 | -44.83165 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8e24612-061e-3cda-988f-bb79e821f21d | -10.86605 | -45.5399 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c757ffcb-8f79-3ace-9bb7-574ebb9b88cd | -11.65725 | -43.68117 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ffccdb6-419c-36ee-bad5-3f37259e3704 | -11.19722 | -45.31616 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e340e1a7-3fd1-39cc-9095-112120013710 | -7.40841 | -44.76915 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c3bdb1a-5b71-37fa-8a17-7f0c89b7c491 | -9.11894 | -45.8315 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624ffd86-bfa4-3990-b43c-a55c028e1b4b | -8.98328 | -45.91061 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 02afcf92-2a02-3b42-8813-f28080f68c99 | -11.0559 | -44.06063 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f36224-4d4f-33b2-b956-930a0aca1c4f | -12.00008 | -43.47442 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 371c16fc-26a5-340e-81f2-551c845e1cfd | -8.9671 | -45.13449 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67f0e1b1-1672-3bf0-b857-e4bb992c176d | -11.19805 | -45.3119 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02cd0260-757a-3b50-8abb-fe8c46a95108 | -14.43951 | -43.93002 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81583685-f5f0-38df-8a00-0fc0966118b5 | -11.99747 | -43.48825 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c438a112-478a-3b5d-9fb0-5f57312a8e51 | -7.41431 | -44.77018 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48cffb52-7c12-352f-8bdf-169781b775be | -14.15162 | -46.34182 | 2026-10-09 03:45:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c807eda-2750-3010-a348-6feb59ba9213 | -7.3119 | -43.97899 | 2026-10-09 03:45:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87b1684f-ce83-36ae-a096-e31553e08477 | -10.00663 | -36.01375 | 2026-10-09 03:45:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bed46432-4749-3d23-912c-e9cfff32dd39 | -11.08779 | -44.05949 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bce78ac3-f5a9-3c66-933c-fbdf6142d2a0 | -11.6294 | -41.83318 | 2026-10-09 03:45:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d5bf22c-e479-3728-b1ba-edbc1e1ae386 | -9.02879 | -44.38725 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 302583c0-6cc9-3ae2-85a4-59bc007d607f | -8.7438 | -45.14395 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 89e58fe8-c73d-3a14-a24e-f05df863a5ab | -10.92564 | -45.3858 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f730be88-99b9-3f1a-a4d0-1746a81eff39 | -10.99784 | -45.41523 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcaeb0a8-3bb1-37ee-9aa9-4ef917ab9539 | -8.91119 | -45.23561 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9df400d1-d3ee-3136-ac88-3faa3202d9f0 | -13.75287 | -43.62567 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3da0628-f436-37ee-b906-b5a565d437ce | -8.96883 | -45.15747 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a7d2e6b-cefc-38e5-9fb1-0b689395fe77 | -11.76343 | -44.95354 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7753ac6b-cda6-313d-ae02-2354855ef5db | -9.90689 | -44.78997 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc4683f3-4c3e-336a-b67d-34946a75ad7d | -7.41509 | -44.76595 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37bb3e93-2b48-3f82-a64f-08575762fb2c | -13.24926 | -42.24899 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 4695aba0-f17f-3dc9-8f87-97d2eb826387 | -13.78567 | -41.02462 | 2026-10-09 03:45:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8b0bd76e-6dbb-3337-861e-aaf59f171bc5 | -12.01017 | -43.47584 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20b2bc92-550a-3ded-aa3b-f90a495591ba | -11.05886 | -44.06749 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe2c3873-48f1-31f3-af49-da0b1993c026 | -10.85864 | -45.54697 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 983bfb6d-4f9f-3bda-85ca-4610e3809b8f | -11.01219 | -45.43502 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b8bfa4a-2697-3d8d-9c83-57b72d955fd7 | -11.76003 | -45.47935 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85734439-e601-3b71-980e-244055f80bf4 | -9.29371 | -47.47437 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e8d2a80-1703-3315-a122-250cbe0c1f47 | -8.91209 | -45.17792 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc333449-26a1-3c8b-a71b-c414329f8488 | -7.3803 | -44.03581 | 2026-10-09 03:45:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 573d68aa-a676-319d-ab81-2bf50346649b | -10.3107 | -46.60125 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bacf1904-3efc-39b6-93ca-96c0179e5582 | -8.72537 | -45.14449 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbed5a1f-6c6b-3430-ba34-1164755bb9a9 | -12.02106 | -43.44535 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c8d6f11-3532-3422-abcf-e4cce0cc34c2 | -11.11372 | -44.0097 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aae65a8-59b6-3f65-b527-109b144b138e | -8.90695 | -45.22582 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e7b11592-3689-38c3-bdfe-0cdb69387c37 | -13.78979 | -41.02538 | 2026-10-09 03:45:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 17540705-fa62-329a-85a5-3dcfabd16bc0 | -11.61715 | -43.69748 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aa5a019-4d99-3ed5-9af9-71990821250b | -8.96722 | -45.16603 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0978c3e2-9708-3b98-aae3-d4184592c3eb | -11.61596 | -43.70373 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a94151ca-e835-3161-8a7b-b8b62985914b | -12.00952 | -43.45176 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e1e4688-505a-391f-b36d-f7fb57d38ef2 | -8.96308 | -45.15568 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a19c62d1-9d55-3c9f-adbc-f8da6508e555 | -11.58307 | -43.65441 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96bff2e2-0537-32bc-95d7-0d4c215c8e88 | -13.25103 | -42.25789 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| d2eac3d9-ba2a-35ba-99fa-3276938b6dff | -11.82735 | -43.59405 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12076d11-8b60-3132-adca-27ed47cedfe0 | -11.20911 | -45.25521 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a2705f7-8bb6-3d0a-bc03-68f22cde5403 | -14.43841 | -43.93575 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef6d1801-4a47-3f2e-b8cb-b44d5888b850 | -13.36261 | -43.88813 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ba3d70-32f3-380d-be06-d63c6045c437 | -8.98427 | -45.90556 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9004b59e-92a5-3704-a186-8e74be9da8f0 | -11.77991 | -45.58868 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d04a0a5-0132-3bbd-9700-fe4a7c828f95 | -9.27051 | -45.63854 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9746ee63-b98b-3625-a4d3-c8b02f69cd66 | -9.46823 | -40.34232 | 2026-10-09 03:45:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 530a8e21-ba60-36ab-8f89-c91c44211a3f | -12.01119 | -43.47043 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c875c7f-cd6f-3e53-9e66-1b7b8ead35e2 | -13.15916 | -43.28498 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9b4a7ecf-d5ab-3ad9-8544-32826ae5c475 | -10.59376 | -46.41978 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e57a67c-dee5-34d2-b39e-bd11ca12f51c | -10.30444 | -46.59996 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e85622fe-df63-35d2-8c20-228cc51b0992 | -14.95417 | -41.42765 | 2026-10-09 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffff8c44-7a18-387e-b767-98c897989c8e | -11.19562 | -45.32436 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fa7f580-b5b8-35c3-94c9-999418311c94 | -13.88579 | -43.82632 | 2026-10-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ea0e989-8615-350a-bc1b-3b738e7644fd | -11.76689 | -43.53379 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ef2fb1-0efa-3237-897f-516f7d7766a6 | -11.76161 | -45.47147 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fcbc2d4-c803-37c4-93fe-933cd0db3072 | -14.43423 | -43.93599 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5cf8e90-8917-311d-9174-ebede147f5a9 | -11.86468 | -43.56286 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2eb02940-697f-3742-bed9-138aaed585de | -10.31384 | -46.26587 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b2365f7-d62c-39e0-ab70-5a5cae07f5ec | -11.05311 | -44.04628 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a06efee-c059-351e-8cea-1e5c6a8d4419 | -11.60849 | -43.71514 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3769c19f-f912-36bb-9822-4e80d714d608 | -10.91012 | -45.52582 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddddf0c1-259a-3f54-ac54-14f545062f7a | -12.00228 | -43.46274 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c1fafb9-a1ed-3d61-a0a8-3b8ef04a350f | -8.7337 | -45.13281 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e7f899ca-b4b3-3950-8ffb-30b41fddb8e4 | -9.8684 | -44.86865 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b9d079f-556b-39b4-863d-173ff99bd93f | -11.6047 | -43.67944 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 121e39f1-7221-3d82-9820-471af0925275 | -11.62159 | -43.70196 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8b34ffd-53fd-3468-ba9a-1bba37a9ff78 | -7.4771 | -42.85644 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3181efc-b53c-31f6-a627-e51c70263de6 | -12.01012 | -43.44855 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 675c4880-07bb-3b49-965d-2dc6760fa031 | -11.00813 | -45.42534 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a59dc020-fa52-39a2-8eef-f57fd2409570 | -7.51207 | -45.76805 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README64.md)
