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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88189fd0-1306-3b5d-8266-a3e3955378f7 | -15.15135 | -43.57607 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 4eaa396b-b0cb-3dbb-b799-92a63dc4993d | -15.86013 | -41.27449 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 6c6fc026-24b7-3c74-acdd-f8746a35aaef | -12.87896 | -44.81828 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b4175c91-e437-35a9-8072-8e8eabc7e48e | -15.15484 | -43.6207 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 6bfa8266-348b-3299-8cc9-4bb7abb26af1 | -15.82683 | -42.56322 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f92b14f3-ebea-3510-a83f-9f422e2c490e | -12.96058 | -51.05222 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e0081b22-2fbe-31d2-b4f2-b39b81463fec | -14.49295 | -45.23486 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2788b803-3be4-301a-b023-b1a53ceb1ccd | -11.27837 | -43.55142 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8e3c70e7-9628-3d8c-8286-1d2ee09ddddd | -16.8869 | -46.89925 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e39c97b3-8dbf-3778-bf4b-0d4421b6e8ab | -12.68588 | -46.97104 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 91789fd6-22e9-3f66-8d6e-c8cb9b15c0be | -11.38213 | -43.40495 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c4448ebb-12a9-344b-b081-d3a56e8aad2a | -14.08439 | -46.32342 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ddb12fd1-53a6-35bf-add0-b279d10c6bc0 | -12.18152 | -40.73253 | 2026-09-28 17:07:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 01aa021a-96c1-372c-9b1b-f9e279d4d33c | -12.75309 | -50.68723 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1fb1c4a2-c869-34e0-bc71-2d6e8b5f7c03 | -13.15467 | -48.55233 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c3d17238-4ba1-3329-956c-f33c657650db | -11.70484 | -43.4591 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ea9ad21a-ee5f-374b-a750-22472fe4ed98 | -14.64497 | -41.76514 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 67d35eb2-330c-3f15-a8ca-c31a0f753857 | -14.42812 | -47.04916 | 2026-09-28 17:07:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d09b772e-613f-349e-b532-1487b3b8b718 | -15.39838 | -47.90336 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 88df1542-5365-371a-9097-d81094a0493a | -13.15551 | -48.56033 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08c35289-ee1b-307b-ac0d-86d7d6248be5 | -15.94386 | -42.33954 | 2026-09-28 17:07:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a61a4f95-c575-3311-9622-752a5b911046 | -15.13641 | -43.62052 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 26.6 |
| cde5bcbf-ee92-3bda-a618-b023ae387ec4 | -17.40847 | -42.2411 | 2026-09-28 17:07:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8a426ac7-9d65-38d2-b0a7-642129e1e98f | -12.67792 | -47.34773 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 43576a83-7525-366d-9b76-2da7579a22d8 | -13.14943 | -48.54636 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1cfa6949-b89d-3a2d-a822-2a75847e4d44 | -13.15123 | -48.53635 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e96dca9f-9ee5-3dee-9493-7cbc8b763800 | -15.46663 | -46.14566 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| b0bf2aa1-fa85-3439-9d83-a61b7f12c254 | -12.90222 | -52.05303 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f0872bb-c0d9-3194-a437-121dd92a222f | -13.96586 | -40.45658 | 2026-09-28 17:07:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 01c954dd-36d8-30b2-8d47-05deb2af2ab4 | -15.22383 | -46.18994 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 232a9218-f951-38fc-b5fb-4beae98b3864 | -11.83157 | -45.01268 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 045e6273-c436-3648-b757-18f021a3e1d4 | -12.66546 | -46.98817 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fee29844-cdf8-3460-9672-08ad9ebbad14 | -14.64172 | -41.93268 | 2026-09-28 17:07:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 19abdea8-0b6b-3316-99ba-7f1fccdc14e8 | -15.07399 | -54.60683 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c9e039cb-f663-3fc3-b110-5211bb9225d7 | -15.94293 | -42.33507 | 2026-09-28 17:07:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 02e96681-34f9-3579-8e01-f5186897ee34 | -13.47016 | -48.58691 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a1f1f80-4aaf-3404-913d-ba4a62b2d2bc | -12.96466 | -51.07693 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b11aea17-e3e2-30d3-b7f2-177b4f9bce9e | -12.86076 | -44.80826 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 85eb436e-1e94-370a-9ad5-216e927659bc | -16.17473 | -40.76989 | 2026-09-28 17:07:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 67b65dec-3076-3fc6-bda8-12bbaa172e29 | -13.19746 | -48.5359 | 2026-09-28 17:07:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2289055-484b-3fe5-9344-47bc0b827c79 | -18.08914 | -44.37548 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2d52f874-ddbd-39e8-b0c9-5fe8f50d236c | -12.31578 | -46.41131 | 2026-09-28 17:07:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cb2eeece-1343-3ef8-8b9f-bff902f7aca6 | -16.35378 | -42.57418 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9caabdd5-99f3-3c4c-b158-437640b75b49 | -12.87642 | -44.80487 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf240549-789e-3866-af1a-983acd79f61d | -11.38467 | -43.41801 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d87967d0-2233-3197-9d61-3bd77cb6b934 | -14.32066 | -44.82764 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 200e3f73-b05b-3446-a652-8f31c5bea1f7 | -17.57712 | -44.38579 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c2ede8a9-3b16-33fb-87f9-176697ef6d37 | -18.79148 | -46.468 | 2026-09-28 17:07:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b522159c-3662-3e75-86a7-216785883a71 | -13.40901 | -43.44952 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d4bdee7c-50b7-35cc-9478-13a982b42975 | -15.45577 | -41.44645 | 2026-09-28 17:07:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| dad48278-ea62-3b51-829c-3640f346f50e | -13.17188 | -48.55778 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c94a412-c8d4-3c69-ad3c-29095036da9a | -15.16721 | -43.57615 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 69eff41e-833f-3691-a06b-9f29ea28fd30 | -11.38812 | -43.43574 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0264b79a-3f9b-34be-bd8d-3652db895501 | -17.86078 | -43.03472 | 2026-09-28 17:07:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d1e5eee-a1ea-39b4-b854-705b868bfcb0 | -13.93016 | -47.8527 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 15ac8856-c8fd-3573-9385-243919be5484 | -16.79746 | -40.77659 | 2026-09-28 17:07:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 7cf95663-ee8f-3f42-aaaf-e85d846bb66a | -15.14937 | -43.629 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4fc70276-fada-302d-80df-25892fdaa81f | -15.53431 | -40.54026 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 75dd9549-6ce6-31b4-8365-4d37e5edec51 | -18.82948 | -43.61803 | 2026-09-28 17:07:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 14ec27f5-b761-399c-8bb2-97a47058ff49 | -11.37788 | -43.38313 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c19c6bb7-29ea-3b54-8f4d-f132ee4a9031 | -13.62265 | -42.26856 | 2026-09-28 17:07:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| a9ab85ad-221a-3a3e-beaa-6a75e8cfe614 | -12.7014 | -47.32468 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| adb18e83-e872-37ca-8aec-91fbdeef3ab7 | -18.12467 | -47.55427 | 2026-09-28 17:07:00 | NOAA-21 | DAVINÓPOLIS | GOIÁS | Brasil | 5206909 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 05f21b20-fa9b-3309-9bec-d34edd774f1c | -13.72054 | -48.82467 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a03b9913-b92c-3d6f-8602-3ae9c18a37be | -13.92102 | -47.8503 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 72ecd265-0118-3e0b-a0cc-2cf4c9a6ce3b | -13.82277 | -44.25628 | 2026-09-28 17:07:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0489c06c-e6e9-3610-91b8-faa5eb76b8c1 | -13.8931 | -53.66385 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 377ec75d-7be9-3f03-bd71-e0226877771f | -14.85472 | -46.80177 | 2026-09-28 17:07:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6db7a2b3-449b-3a95-aeb3-8398efa6339d | -13.99979 | -43.76356 | 2026-09-28 17:07:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 19a01e6d-7bab-3dd0-a832-7464de7043a9 | -14.08998 | -46.32765 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c7e8c094-93a6-3f1d-9e6e-26f1dca54e28 | -11.6033 | -44.13877 | 2026-09-28 17:07:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 69e08b89-ab1e-3af7-a8bd-f0b59492de1f | -14.52152 | -48.30022 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f61e5f4-dc8e-34db-8da8-ea5d52964f57 | -15.0981 | -53.88164 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 18bd0229-9a14-3c54-885e-f50bb131b6c4 | -24.67105 | -49.60694 | 2026-09-28 17:07:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7a4656af-bc11-3824-aa07-296a048e2a64 | -15.21574 | -46.17257 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 717e7de7-3d76-38b5-b544-f6c5cd5fd623 | -11.69904 | -43.49113 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1b666687-5c73-30fc-8524-56f907423eb6 | -16.17237 | -40.77004 | 2026-09-28 17:07:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d40456e6-b483-3e25-ba69-590f6e468c30 | -15.06568 | -54.59693 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 93a2b460-dba5-3097-bb42-eb8e19fa919b | -15.13427 | -43.6098 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 18.8 |
| a055eca3-5600-3bd6-a7a5-6fe22fdce2ad | -15.0374 | -49.58969 | 2026-09-28 17:07:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ad7c2185-d6b9-35c7-96fd-0c717f30193e | -19.24453 | -46.62135 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7afd4e54-fc5b-3a2b-8a59-a6428dfd58bb | -17.57436 | -46.91528 | 2026-09-28 17:07:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6f8931b-e6cb-345b-a804-4b734a726528 | -15.16066 | -43.60035 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c6f79f07-705d-3244-80e2-c6f4f4ac7c43 | -15.18895 | -46.17936 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3f996c64-29b6-3135-ab73-5398a855219f | -18.39314 | -43.43136 | 2026-09-28 17:07:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a03791ac-f907-3395-abe3-720a53946e74 | -15.71916 | -42.62492 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 3b08d84e-6eb0-3bfa-bb98-25986adf99bd | -13.15423 | -48.55316 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ced58632-c4e5-35e9-b09a-65e7e8f2e944 | -14.50943 | -52.48738 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 83d6b21f-d57f-3481-bccf-1d9a3f410406 | -15.05619 | -54.60208 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c8239c41-716d-34b8-a718-708e1ef45179 | -15.11551 | -44.09164 | 2026-09-28 17:07:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 06252bcb-7738-381b-b6c4-33165da2b151 | -11.89506 | -47.01778 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| aa7a7c7b-f913-36d1-81b6-fa07297ed871 | -12.4374 | -44.14607 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a5676bea-e0b3-3052-a9ad-5a2c4749aa09 | -11.6333 | -43.49179 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 00ecc48c-5d4d-36de-aa84-061c9301f065 | -13.44924 | -46.3143 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 087bf556-08b3-3f4e-9a0a-64baa0a31808 | -17.89263 | -44.53417 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e17c425-75c3-3a95-9179-865222ab258f | -13.17473 | -48.55013 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cba84483-cf28-36bc-9664-2b7173f51fed | -11.39138 | -43.42114 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 877b877f-01bc-3145-9f3a-f015110e9437 | -18.46176 | -46.43427 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83261851-8f59-3359-a39f-13384d7568cd | -16.8868 | -46.90424 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0bf0c1b0-649c-3249-bc3d-926319adde38 | -15.5847 | -47.91545 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.2 |


[Clique aqui para ver as próximas entradas](README137.md)
