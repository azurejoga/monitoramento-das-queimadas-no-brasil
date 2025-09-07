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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54e2fa3e-90c7-350e-a0cd-51aa90560c3b | -11.40928 | -43.61687 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 208c4d5f-db6a-362d-8a17-3f5ce4a69878 | -17.36758 | -42.64632 | 2025-09-07 03:32:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ba2f116a-33ca-3119-8349-910bc80bd40f | -11.60045 | -47.17522 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 29e1745f-c57a-3e49-b476-f546660d606b | -13.83581 | -46.27401 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0505959d-e4c6-3228-bbb7-e715affbc2d6 | -15.01039 | -48.0032 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 211a61ae-a5ce-3262-98f5-1e8c18cfc3e6 | -15.73588 | -47.0291 | 2025-09-07 03:32:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73484535-c8d1-3f27-b9bb-7edc5a23dbdc | -13.83917 | -46.258 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7030775-a599-347f-9389-4bb7b5e158db | -11.61783 | -47.16756 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 059713b7-b83c-31ee-8e44-d257d97f9b89 | -11.60392 | -47.16474 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 2e700f35-9cfa-3fff-9b2a-23c71534f014 | -16.53909 | -45.09627 | 2025-09-07 03:32:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9cad307-3881-3509-95ba-fcc1836adc3f | -15.15225 | -48.17515 | 2025-09-07 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f9c93b7-5ede-390f-a2f4-416dc5c01f56 | -13.84035 | -46.26087 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8dbfa0f9-0884-3a4b-a19f-68f2e0d1358a | -11.40539 | -43.63686 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96f0d768-3156-3676-9db1-c5cccade6dd5 | -15.11711 | -48.07442 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b4093c91-2587-38cc-8a5c-8c4e123846af | -13.71478 | -46.88113 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd1d5565-8245-34dc-a5b7-6512a2323990 | -9.83505 | -46.54762 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2135235b-c5ab-3aae-91a0-91d755e764cc | -11.59694 | -47.16346 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f99608b1-fcd6-3b46-b4c4-ae80b94841e5 | -14.27102 | -44.97966 | 2025-09-07 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 126218ce-2f3e-372b-95cf-fd1c4e75150f | -11.40517 | -43.60792 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c305e5-0f49-30ff-ae31-ed767b61a47e | -14.84908 | -46.69135 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9009502a-2c01-3455-b806-c2dc6095a6d1 | -11.41082 | -43.60901 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 218bf84f-d2ca-3d96-b3b3-175f6f45c022 | -11.38504 | -43.54613 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e37fc7-7e18-38cc-8586-a933605fcca6 | -11.40694 | -43.62889 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5733a6bd-baa3-3c43-8dd5-1270ffee86dd | -11.60495 | -47.15419 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 4ddcb059-df6f-389e-89bf-75eec8d0cd35 | -15.09392 | -44.00828 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6715a1af-4140-3a97-ad2c-cc6054cc4e71 | -9.83442 | -46.54803 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d7e564c6-f283-3170-8ce7-d3bb3ab6f489 | -13.78714 | -43.16202 | 2025-09-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cdae83a3-2f66-3869-a07b-7a8c5a8001fe | -11.31602 | -46.54408 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3458e947-7a0d-3759-93cf-08361458a31c | -13.82234 | -46.27494 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6fd8a2eb-5248-3296-85ef-237b45c46d9a | -16.53824 | -45.10032 | 2025-09-07 03:32:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e92dca6-d412-3c84-acab-4aeba78ff557 | -13.6639 | -46.95774 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68d944e6-830c-3ea2-86c5-4f86b07e20cf | -13.73411 | -46.90744 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbd949f-a9b5-34fa-81f2-0685c76cb613 | -15.1824 | -47.9748 | 2025-09-07 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f2a7fa4-941d-30c0-a25c-45ce6337be4f | -15.25664 | -40.74815 | 2025-09-07 03:32:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f32f26bf-ca8b-3b95-995e-1b3c56c5cfab | -11.40071 | -43.57084 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3eb2ab4c-625a-3037-a495-dff4b8013084 | -13.91157 | -48.02654 | 2025-09-07 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c6e48a4c-6633-31d6-933d-a51afa61ae57 | -13.82521 | -43.86364 | 2025-09-07 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 320fdfcb-1cbf-3c4e-9c79-cbba34007c39 | -13.78648 | -43.16538 | 2025-09-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fae46fa0-b63a-3330-b467-26f4d070b97d | -11.40131 | -43.62766 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6aa2df5-fbd4-3845-8d87-82acc9d171bc | -13.71783 | -46.88702 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12c24393-2811-34ce-9f39-a99c0c3abb4f | -13.71603 | -46.8953 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54742929-d598-3813-bc8b-761b712062ea | -11.29787 | -46.5407 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72272e9b-a640-3226-9d73-22cc52b57530 | -15.36547 | -43.66572 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 810c62a2-5def-3c02-9fcd-b4fc4ddc0e4d | -11.32105 | -46.56427 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 95dbfcd2-1fc5-3a7d-ab37-37a54d767260 | -13.84766 | -46.24909 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a041d154-119c-3539-ac01-81f2a240b207 | -11.4021 | -43.62361 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b881d978-bbd9-386c-937c-0847bd0a6c52 | -11.60537 | -47.15773 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 983727bf-9c82-3149-85bd-dcec9b324c72 | -15.53809 | -42.65668 | 2025-09-07 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| dde0622f-ea81-3bfc-a5f4-45a03371b226 | -10.73712 | -44.35298 | 2025-09-07 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b21798b-0688-3f54-9a81-e0f8503f234f | -11.61972 | -47.15839 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8c7af73-4e46-36a6-a202-1dfb047d5954 | -16.28077 | -45.68452 | 2025-09-07 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c56cc5f4-33c7-31eb-bc26-616b90e38067 | -11.61062 | -47.16156 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e4588e6f-7e6b-3ec9-9fb0-4c9fb78df610 | -10.60815 | -44.33274 | 2025-09-07 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 82e03897-4198-37f2-aed7-e460f6a54bf6 | -13.71696 | -46.89105 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c2d3f52-574a-30c9-b8f0-0026cf3255fa | -10.34688 | -46.45827 | 2025-09-07 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1446a2f-c601-3ce8-8c2d-b0dc27233d18 | -13.18632 | -44.48485 | 2025-09-07 03:32:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3bd35069-3d2f-3ade-acf1-100cbb8e131f | -13.8251 | -43.86328 | 2025-09-07 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4662fb9-c02b-3578-8468-a9d76a53be52 | -15.36477 | -43.66914 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49a4ee14-e505-34da-91ac-0ce360b07f0d | -11.31046 | -46.53686 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b646a6d-de0d-36ee-978f-406e159d47c7 | -13.00913 | -45.22649 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c56b29d-74c5-32b6-bff0-3db0cb235240 | -11.60197 | -47.16809 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 79d073d6-cfe4-339e-9325-5baad930890a | -14.65826 | -46.82077 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37813eb1-56c3-36f5-a9ae-c93c3f6e0104 | -13.91654 | -48.03713 | 2025-09-07 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 098ab8d6-4f5a-385d-9b25-b970f049a306 | -11.39483 | -43.5561 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a2483f20-b3e5-3edc-8033-cfab9280a928 | -13.83585 | -46.28169 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 21a1a87b-28dd-3195-809d-afd32157aa1b | -15.0087 | -48.01072 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9af75a30-c2c9-38d9-ab32-5dd8e814bf45 | -14.85499 | -46.69077 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0d5b6c46-1550-3cf5-ae9d-942997371225 | -15.72896 | -47.02677 | 2025-09-07 03:32:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aad2f075-bb8b-38b3-af94-09897e102f3a | -15.11706 | -48.0738 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3820995a-74bb-365b-8a8d-b0332f8d7722 | -15.946 | -41.887 | 2025-09-07 03:32:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 654ab92d-602a-3d50-8766-cca37743d898 | -13.83361 | -46.28455 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b5434e35-2f2c-37d3-a542-41b6ee59c281 | -17.36389 | -42.63993 | 2025-09-07 03:32:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 86b85deb-88b5-3284-9acd-33502599291a | -11.23923 | -46.44039 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9328bf04-4a7f-3d5b-8cdd-1593a38061b0 | -11.31689 | -46.55058 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7fb28c79-89d8-3042-bf44-38e458841ff5 | -11.41158 | -43.60512 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af3459b1-f2d7-3dea-86e7-2fce7504d801 | -11.77303 | -47.56019 | 2025-09-07 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea010488-4000-388e-95e9-29bcf64fb274 | -14.56671 | -43.72506 | 2025-09-07 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b0b1d98-6a1c-3a35-a8d6-ae1e339170b4 | -15.10867 | -48.08002 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9555b2e2-2e84-3e4b-971a-29ccea8b4ab8 | -13.91927 | -48.03727 | 2025-09-07 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de900e1c-59f5-3aa6-b484-46671acaf1c3 | -13.83792 | -46.26395 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 626a1a74-8adb-347b-a029-646cf246459a | -13.72008 | -46.90841 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 894e4dc4-c3b2-3396-88c2-3ecaa8bcb32a | -15.09261 | -44.00786 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f3aba0-e085-3588-a690-ab3a9f3a909c | -13.71571 | -46.87674 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 985482f4-3347-39a4-b981-af04789a16e3 | -11.31257 | -46.53768 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 126374f2-bc3a-33a3-8d39-51d6d2356765 | -14.79271 | -48.10813 | 2025-09-07 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1916abcb-1423-394c-ae00-8cb6c532999a | -11.32032 | -46.55747 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 4f6df7a3-50dd-3ee3-911a-167af2545224 | -14.85383 | -46.69625 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24994383-a31d-322e-a60e-9a7ab2d32324 | -15.94408 | -41.88305 | 2025-09-07 03:32:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1862fe97-efc6-3b46-b59a-3eef6452ec87 | -11.41667 | -43.63922 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1bff22a-5268-3a9d-9445-4138aa77d9d3 | -11.60355 | -47.16075 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 9eb28dc1-34c3-3c51-bdd7-c802d4c69b15 | -13.00592 | -45.21099 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a0aec5c-146d-34d9-bb1b-ca2c4db18dde | -13.91426 | -48.02656 | 2025-09-07 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f627113-7f69-3fa3-96e6-98cf89b66a74 | -11.34522 | -43.51025 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c250933a-b42f-3d20-bf08-71f00e8f615e | -13.05249 | -47.12385 | 2025-09-07 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e897d63-b4ae-3e18-9621-2bc75f7e58e5 | -13.00975 | -45.22647 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e777ca9f-890e-3e9d-88ac-8c467762f5b4 | -16.29252 | -45.68708 | 2025-09-07 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4da6f3a5-7439-3b1b-9530-c968261f5706 | -14.79111 | -48.11525 | 2025-09-07 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0afc3ed2-7970-3a5c-8ef3-39ea71084899 | -11.30931 | -46.54252 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 094b850c-0e3b-3556-bcdf-6852466ac69d | -17.36282 | -42.64534 | 2025-09-07 03:32:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 1055610a-a959-3b06-b97d-690a6e956bf4 | -15.54198 | -42.66307 | 2025-09-07 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


[Clique aqui para ver as próximas entradas](README21.md)
