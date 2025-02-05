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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80538d6f-a3e6-31c4-983c-ee9b9b4f693d | -11.97226 | -63.83643 | 2025-02-05 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b851390-3618-36f4-b5b5-7f9d0ebcefec | -16.09799 | -60.07565 | 2025-02-05 05:52:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2f14558-84b4-3a82-b037-31acf85c7607 | -16.10329 | -60.0764 | 2025-02-05 05:52:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 918d2447-d5f3-3410-8c0d-37b8cd0d9080 | -15.25795 | -60.23328 | 2025-02-05 05:52:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e8c7f20-1cbf-39e5-9278-a7f3e0b699bd | 3.58902 | -61.4295 | 2025-02-05 06:09:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7106faa5-8451-3f31-a732-90cb51d3ba63 | -7.93064 | -42.82336 | 2025-02-05 12:29:00 | TERRA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bba74259-9428-396a-a62c-c47263c3d801 | -7.92915 | -42.83435 | 2025-02-05 12:29:00 | TERRA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2967de8e-b2c6-3b03-a9d5-3cb84b81a217 | -5.97912 | -42.44594 | 2025-02-05 12:29:00 | TERRA_M-T | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e8585ead-f5f4-382b-87a0-fb99240d0240 | -6.1697 | -43.26191 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 77bbe246-73eb-3668-85fb-04a4ed56e4d6 | -11.46531 | -44.95766 | 2025-02-05 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 38450fc8-7fd2-34df-8131-3220bccb617e | -4.74232 | -43.25131 | 2025-02-05 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4bd83fdf-bee3-3281-8e5b-954e15582b28 | -5.95482 | -42.1769 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| ea45669d-d22b-31b0-a20d-c123596f51d1 | -11.02785 | -45.05471 | 2025-02-05 12:29:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ce795ffa-8693-379a-bf2f-36e5142d083d | -6.14452 | -42.57992 | 2025-02-05 12:29:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d15dc1ce-b331-3d6f-8ecd-d003034a17bd | -5.99077 | -42.64458 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d8139a12-9bfe-32a1-b676-00dca67c2882 | -11.57102 | -44.86103 | 2025-02-05 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| ad1a2694-b930-328d-8304-c654bd475457 | -6.95559 | -42.84365 | 2025-02-05 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| b7e1ddfd-abb5-37e4-a164-d7b2f0d877f6 | -11.57932 | -44.85878 | 2025-02-05 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6735481f-3b48-3ee0-9c00-eafa5e630799 | -5.95324 | -42.18814 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d9504f82-f4a8-3141-850b-fa67eb5fb5eb | -4.80877 | -42.98207 | 2025-02-05 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b082827c-ce55-3263-8050-01884555757f | -10.8557 | -44.76765 | 2025-02-05 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6ea3ccbd-1786-37d6-be5c-143bcf5e02a6 | -7.27345 | -43.7235 | 2025-02-05 12:29:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2080011d-a184-3ed1-88be-1f6235a0ef89 | -11.12384 | -43.36782 | 2025-02-05 12:29:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6ea77285-332f-3bd8-9ae1-c34369fa0894 | -6.17111 | -43.25195 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0186f92d-6117-3bc6-8cc6-b728290e093d | -11.47281 | -44.96468 | 2025-02-05 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0b44fa83-6d46-3c2e-8cd9-8d975aa31a1e | -10.85439 | -44.77722 | 2025-02-05 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 6ff41257-1ddb-30a9-ab0f-0bffedbb4c1e | -7.87029 | -43.12214 | 2025-02-05 12:29:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| e3c80b58-5d51-359e-b6fe-91881d031b75 | -10.60492 | -43.65705 | 2025-02-05 12:29:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5555b444-c874-3837-ba72-7ba3b6847a7b | -7.68776 | -42.87214 | 2025-02-05 12:29:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 2a792848-c4e1-34d6-9fef-0f82890420d7 | -6.84837 | -42.81196 | 2025-02-05 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c6926158-eb18-308b-9256-02cba9ecf9a8 | -4.73649 | -42.97626 | 2025-02-05 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 763b0a0f-0457-3a01-8ffa-65be373e77fb | -7.87173 | -43.1115 | 2025-02-05 12:29:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ca591495-3227-398e-9241-171df4a8f9e2 | -8.37354 | -43.95948 | 2025-02-05 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f6568a15-8ee1-315d-8da7-e957cb63e3d3 | -6.84689 | -42.82261 | 2025-02-05 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 074c2816-aea4-312b-b74f-134555eb0249 | -5.95435 | -43.28063 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6e2f9339-9223-3d80-b06d-51af216f589f | -6.35395 | -43.37597 | 2025-02-05 12:29:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 33192db2-59ac-3f86-b707-e95711c8ad9d | -11.57237 | -44.85139 | 2025-02-05 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0075382e-a2ab-353b-bc3c-115a42fd07f8 | -6.14858 | -43.79671 | 2025-02-05 12:29:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2ae01b05-06c3-31c4-ad71-a3d0fe3059f9 | -2.8544 | -41.75897 | 2025-02-05 12:29:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8b64166d-927b-3946-9725-28ce4932fb5e | -4.96247 | -43.71442 | 2025-02-05 12:29:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 44a41ec7-dfef-38b9-a50c-34bd188e3022 | -12.46026 | -45.34581 | 2025-02-05 12:31:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5584d33f-cfb5-3f68-b6dc-134729282151 | -14.21434 | -47.00435 | 2025-02-05 12:31:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04c6f82d-d729-3e79-9ca7-3b79b83750ba | -12.74265 | -44.83657 | 2025-02-05 12:31:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ea49d77-01d0-3d38-ad77-c5551197ed59 | -12.64703 | -43.81995 | 2025-02-05 12:31:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f57ff226-0670-3fde-93d4-ca9b042dbac6 | -19.58285 | -42.64153 | 2025-02-05 12:31:00 | TERRA_M-T | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| de20621c-6080-3386-9271-b0b4ddbf8cd0 | -13.44013 | -45.58128 | 2025-02-05 12:31:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 403a8f96-050d-3fa8-9459-eb807fb26e99 | -19.7904 | -42.14591 | 2025-02-05 12:31:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| df5b1cbb-a5fe-31c9-a10e-353862d8d65c | -14.21303 | -47.01343 | 2025-02-05 12:31:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 289313bd-29eb-3f9b-902c-0c0a10079901 | -12.64849 | -43.80883 | 2025-02-05 12:31:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| c2987020-3202-3ba9-93b4-1a97b9edccb7 | -12.65828 | -43.81015 | 2025-02-05 12:31:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 55729307-20e5-3203-9390-ebce3410a88d | -15.37568 | -43.92496 | 2025-02-05 12:31:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 25a72a5f-1263-3666-942f-9ed5f3bec8e0 | -19.79545 | -42.13431 | 2025-02-05 12:31:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 77780b99-b708-3dd1-8442-0d0f78e12456 | -15.93234 | -41.17698 | 2025-02-05 12:31:00 | TERRA_M-T | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| ca58f799-72a6-3c4d-9b17-51b46e22f78f | -12.3561 | -47.98361 | 2025-02-05 12:31:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 806cd258-66b9-3be3-aaba-6792bea63f3a | -21.13418 | -42.37825 | 2025-02-05 12:33:00 | TERRA_M-T | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 7d1ddd66-26da-366c-9f21-929e8c52e51c | -20.95737 | -43.79343 | 2025-02-05 12:33:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 4b08a1e8-e74b-3f8f-aa80-20c28427b832 | -20.07394 | -44.29654 | 2025-02-05 12:33:00 | TERRA_M-T | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7821db76-d246-3e21-af3b-632e3a3cd02d | -21.13119 | -42.37204 | 2025-02-05 12:33:00 | TERRA_M-T | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| e5cec179-a6eb-38a4-b4ad-b0f62d934d70 | -20.05818 | -43.97794 | 2025-02-05 12:33:00 | TERRA_M-T | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 4bab6a94-f6f3-3345-842b-b6ae03e2ccda | -21.13616 | -42.35902 | 2025-02-05 12:33:00 | TERRA_M-T | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 2facd74f-01ae-3e9e-9123-3cbed997cb3d | -20.9556 | -43.80842 | 2025-02-05 12:33:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f446c1de-d4c5-3faf-942b-89041361d6be | -19.888 | -43.65801 | 2025-02-05 12:33:00 | TERRA_M-T | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 4ee9c5f1-fd20-380c-88ef-0dcdd8055795 | -27.96867 | -51.63523 | 2025-02-05 12:36:00 | TERRA_M-T | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 5e16b6fe-fb14-3626-9bad-d605d564d8f0 | -29.40118 | -51.44128 | 2025-02-05 12:38:00 | TERRA_M-T | BARÃO | RIO GRANDE DO SUL | Brasil | 4301651 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e08b0313-7626-31a5-b91a-17d9bf315282 | -29.39223 | -51.43954 | 2025-02-05 12:38:00 | TERRA_M-T | BARÃO | RIO GRANDE DO SUL | Brasil | 4301651 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


