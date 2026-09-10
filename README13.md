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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee48042c-4b98-34a1-afd4-324a1d76616d | -12.84929 | -44.34316 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 371.3 |
| 36b4227f-314e-3e62-ae07-7b2ed893eca8 | -12.83224 | -44.33664 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| f8ce8639-0ed1-3b75-a33c-75ec08e7dab1 | -9.778 | -43.45569 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e352d378-9dfb-3855-aa2d-1410f2e15300 | -12.84872 | -44.34426 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 367.7 |
| f6e83021-462b-3df1-b66c-c24467a5e373 | -12.84459 | -44.33475 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| c06a661c-c94d-3601-8c7a-461410cb61ce | -8.23857 | -44.75871 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2693c4df-67a1-3416-9a30-4afa5bc02bab | -9.68446 | -43.44282 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcdc7387-55d0-3c0e-a9c0-3916fd4c0187 | -12.85036 | -44.33592 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| bde9b079-b29d-3b66-928c-501ef46d7e6e | -10.07184 | -45.48364 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 787f6518-5915-3ae4-821b-49d78bbfb1ef | -12.82646 | -44.33552 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| dcb5452d-128e-332b-8939-a54192cead89 | -12.85448 | -44.34544 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| db51684b-26a2-3040-97a3-d38b0a92649b | -9.78389 | -43.45977 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 720c28f2-5364-34c2-b52b-6fbb179c91da | -10.55664 | -46.09054 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10d4f3de-df3b-3fce-9849-7bca060e802f | -12.64779 | -42.2963 | 2026-09-10 03:32:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9c31488d-a2e5-3959-864d-c61ba8706e38 | -9.68596 | -43.43787 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ad64fd4-f520-33a3-9faa-e937685b7e53 | -14.91425 | -44.67085 | 2026-09-10 03:32:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61ed97d8-cebb-363c-ae10-4d1aa36482ce | -12.65292 | -47.09072 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0fcdb2b-aded-35ab-8e18-d16586977db3 | -10.23802 | -45.18869 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d89813-147a-385b-a8e1-2469040ca423 | -12.84295 | -44.3431 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 367.7 |
| 2ffeaf1a-ba3b-3973-8ba9-9a0449aee58d | -12.63725 | -47.09315 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07e35b9c-c5fa-31c1-aa1e-8d4856d75554 | -12.85611 | -44.33714 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e7367889-f682-3989-bf82-fe6649ab3ca5 | -9.55177 | -46.65084 | 2026-09-10 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49794043-6988-31fb-865c-9527f9680cd9 | -9.68182 | -43.48938 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 264c0120-f902-3048-afce-75cdeeb85da1 | -12.85692 | -44.33298 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c5cd01d4-7d5f-32b6-b565-b4c6e2e01c0e | -9.78302 | -43.46079 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f896aa0-1f15-34fd-97a1-3e609877f9f9 | -10.06785 | -45.46952 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43f79d5c-16b4-3de0-81c5-381eba84d19d | -9.66145 | -40.63048 | 2026-09-10 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c2eaac14-f342-3cb0-93cb-e3f4972ef173 | -12.63928 | -47.08805 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd248168-6d25-33c5-983b-dfeed9b19ed6 | -15.78954 | -43.56574 | 2026-09-10 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b105e35e-a166-32ed-95ac-ae1e2790699a | -8.24171 | -44.74254 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| fd0ad70a-b348-3957-83f2-7c7e54b2e8c6 | -8.31804 | -45.11091 | 2026-09-10 03:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1788d9d0-afa9-3bc5-aa06-656566469f78 | -8.31695 | -45.11655 | 2026-09-10 03:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ebca5b3-93a1-3690-85d6-16bb073e65cc | -12.84182 | -44.35035 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| f4a82c1f-4846-3227-9313-d90461bdd26e | -9.72563 | -43.3862 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ae38d85-17b1-31d4-abd6-5f6fef86fe17 | -12.17096 | -38.59619 | 2026-09-10 03:32:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3ca8ecc-1fc9-3c06-96a0-c4cea72ea266 | -15.78435 | -43.56461 | 2026-09-10 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d752a8e-6a85-359f-ba3c-903a47c4f9ba | -12.84522 | -44.33369 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 78648892-f7fb-31ab-9269-90473840aa71 | -12.83057 | -44.34504 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 7c724d36-dabc-3a73-95bd-79200fb7ec76 | -12.85366 | -44.34961 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4270bfff-ce28-3d11-8aa0-5f3d97b0144c | -12.82481 | -44.34386 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 428dc6f2-9f3b-34e1-8268-8e0986257566 | -9.69273 | -43.46478 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5edb0c57-46d8-3581-b720-eaf6f8c63cd6 | -10.46508 | -44.94683 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bce16f6e-0ab3-3211-96da-026a65d803f4 | -11.87817 | -44.85175 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48dd7b55-1888-3320-84f2-803df304fe45 | -13.43822 | -43.83517 | 2026-09-10 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0ff9838d-25f4-3b15-ab6a-8b21630906f0 | -12.83553 | -44.35032 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6b996e25-f72f-307e-ba9c-3cffd19fa4ba | -8.94591 | -44.40857 | 2026-09-10 03:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85f49e7d-6326-3256-aba7-2bb8dff6d7e6 | -12.83636 | -44.34612 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6d100439-45c3-3935-bba3-782288af72d8 | -9.71103 | -43.40042 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e794865-a397-3695-a312-af7620aa2d81 | -11.86617 | -44.84883 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d258ecf7-9f8d-3694-ac18-aca16b5740df | -8.23852 | -44.75117 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| d91067ea-c27b-33ab-85c8-84e4959daa1c | -9.68379 | -43.48019 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a994d62-9d5d-38f4-ba7b-8aa369227610 | -12.84352 | -44.34201 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 371.3 |
| 87c4d2ae-b406-3120-8b58-953c029c7928 | -12.85183 | -44.33069 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c950ad39-bd9a-30bc-a8a5-2c6464ba4041 | -8.24067 | -44.74789 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 2013b3cf-53d1-3374-9e09-8df9047358fb | -12.85758 | -44.3319 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 837bbf51-5c8b-3070-b385-05e21af7aa0e | -9.69357 | -43.46044 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 940a2099-8213-3164-b16e-a009d8beaf57 | -12.86023 | -44.34666 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 50f45216-0b3d-3095-b4fa-749381ab0aca | -12.86104 | -44.34252 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 65138dc7-15dd-38a1-a19e-b00f9a7e23ef | -12.64407 | -47.09449 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b41d77bb-c8f8-3b25-aa98-d88dfc760ed6 | -10.06679 | -45.47502 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c186ae59-0f02-3bc3-b2e1-5d63b315faab | -9.7797 | -43.4506 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbf4fe11-00d8-3ce7-9c24-916835715621 | -12.8542 | -44.34848 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 214a4dab-8db9-370b-bda1-7513a1e8828b | -10.55887 | -46.09803 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7167ae06-7a35-3a41-a44d-56a4080afded | -9.7035 | -43.40425 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db6bd550-36e0-337f-8c1c-69c1c0830338 | -9.71603 | -43.4054 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2890ea2c-7523-3f9d-a954-8f31373f0eeb | -12.84541 | -44.33059 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e64411c3-d447-319b-8081-696b4d520d34 | -13.44389 | -43.83558 | 2026-09-10 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 32c69f1f-6295-3381-ba4a-78b705e77586 | -12.82975 | -44.34923 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 71534e67-2905-3c2e-83d8-85aa16de45d4 | -10.07931 | -45.47993 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6850b56-e18b-300e-b0bf-9e5664c08287 | -9.66175 | -40.62708 | 2026-09-10 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a61e6d75-044f-3864-ab84-4eea15207f9d | -9.77877 | -43.45158 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9c2e1be-7404-36b1-b83a-608b60ad4998 | -12.6386 | -47.08663 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31ac059e-83e8-3159-a30e-988e47b59d41 | -13.53734 | -43.30641 | 2026-09-10 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9383e8d8-4631-3af1-aa71-9906982b8fb6 | -12.85674 | -44.33604 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e22ed810-0d30-31ec-82e7-ce0295af95e4 | -8.23953 | -44.74576 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 379cb052-4ed5-3740-b130-749301d20456 | -9.71681 | -43.40127 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5488a381-a4a3-3c31-a0e2-d862ab23b517 | -8.98052 | -44.97789 | 2026-09-10 03:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85e9a892-78f2-38a8-8fe5-56231c114266 | -10.56205 | -46.09817 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6e9cc70-6c8f-3225-81af-b089291ef3d1 | -12.8616 | -44.61111 | 2026-09-10 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b784263-6257-3c15-88b2-9519f2635a7a | -12.17496 | -38.59699 | 2026-09-10 03:32:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 695c08b5-01d7-3d25-97bf-5e6e927f840c | -9.6985 | -43.46584 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b6cecb3-a94d-3d64-b831-dd913863a260 | -9.69034 | -43.47724 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0424a4b9-22a8-3394-9ba3-a342fe9e9090 | -12.86743 | -44.61243 | 2026-09-10 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b420b16-de64-3ac7-81cb-95aee56fa6cb | -9.71913 | -43.38914 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5165670e-4816-339c-a637-c8e33b498dec | -9.68518 | -43.44196 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 076c0af1-6fd7-35fb-aaa3-ec5a8add356c | -12.83306 | -44.33246 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ed3aede2-7f7b-396b-a179-dcb59bd6c7f3 | -9.68986 | -43.47819 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eceb5b7a-b456-3886-b2c5-72e7aed7ea22 | -12.84213 | -44.34727 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7df5157e-4db0-39ba-ac1e-91c22a3e4ff5 | -11.85463 | -44.8753 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6aae16f-0397-35ca-903f-0a4299f90539 | -11.19399 | -42.78736 | 2026-09-10 03:32:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f0ab6f26-6f98-3d80-baf7-8a0551ab3b09 | -12.8413 | -44.35146 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 499838ce-9a5e-37e2-8809-5046c926699e | -14.91343 | -44.67485 | 2026-09-10 03:32:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1435ec4-862f-3021-bbd9-4362b3195ddf | -11.43706 | -45.15444 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c7236f5-7e5c-3677-855a-8261bcfa5d92 | -15.71759 | -42.24763 | 2026-09-10 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e6c0db4-59d6-3b91-8ee6-11eab9e6a855 | -14.46891 | -47.05323 | 2026-09-10 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a824b7d8-924c-304c-b5d8-dc74d22a15ec | -11.32973 | -45.78485 | 2026-09-10 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 906e4b5b-f97a-3155-92a9-aa6a30af33d5 | -14.20311 | -41.60311 | 2026-09-10 03:32:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 56d71325-ed74-3e8d-abdb-7917fa5353d8 | -10.27433 | -45.20524 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d97b9c2a-e236-3733-abe5-2f32b7661385 | -12.83141 | -44.34083 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| f46b7820-a059-375f-a9b5-48d76afa067f | -10.06776 | -45.47039 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README14.md)
