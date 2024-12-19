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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59407a92-f975-3c94-a57a-411090a08387 | -21.04669 | -55.81262 | 2024-12-19 04:33:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75af6f6f-7b08-3c1e-b550-9eb0aefb1c35 | -20.47487 | -55.84444 | 2024-12-19 04:33:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ecccc6b-5775-397f-880f-892345db6314 | -22.54563 | -48.36914 | 2024-12-19 04:33:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3a1eae5-79fd-38f3-80d5-c04aa5ab8120 | -17.69906 | -54.08605 | 2024-12-19 04:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b1c9684-8d45-38ff-83ca-d7649e1c78cc | -18.73899 | -56.56367 | 2024-12-19 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3cce60e4-7d84-3f93-b2b0-15a0c90e69f7 | -18.73976 | -56.55964 | 2024-12-19 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ce1b45b2-c8e3-38f2-b619-8df318e6e8ad | -17.29976 | -53.77051 | 2024-12-19 04:33:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6770613b-4677-3d6c-b3f9-d06aec0542f6 | -19.98055 | -54.4215 | 2024-12-19 04:33:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 892ed670-67bd-3d73-85ea-4ddc506c3c46 | -19.36063 | -49.19575 | 2024-12-19 04:33:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 08a5fa67-c50e-3266-9b39-1b09802eef89 | -19.12627 | -53.45715 | 2024-12-19 04:33:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97f6d9da-70be-3b53-b709-91e5d7bfafe7 | -20.76301 | -46.77111 | 2024-12-19 04:33:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dbdb7494-2ec1-31dc-be4a-19b7727a2791 | -23.0464 | -49.89404 | 2024-12-19 04:33:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fe3d3c05-916f-3e2b-b3eb-802d30c3fc4b | -17.30055 | -53.76602 | 2024-12-19 04:33:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 382d18e5-7568-316e-a8f2-4d95bc56b97f | -20.77978 | -49.85555 | 2024-12-19 04:33:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4d1051a4-6c32-34ad-90af-c3abfe1ba9cc | -20.13497 | -52.04417 | 2024-12-19 04:33:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ed60168-3ce1-3b5a-84c9-498a8c59b076 | -17.94195 | -54.96892 | 2024-12-19 04:33:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fdae1c0-61d7-30b3-bc26-8ef2b4af02e7 | -21.59495 | -48.49192 | 2024-12-19 04:33:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98f5ecd0-d0ea-3fb0-aabc-c9ef92d4eda9 | -17.97199 | -54.00896 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8466c7d-9b1d-36e0-a0f0-3f61966358f5 | -19.06391 | -52.89113 | 2024-12-19 04:33:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f72ee0a4-555d-3a7c-99e5-01ded566a137 | -22.5412 | -48.81185 | 2024-12-19 04:33:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c12a255c-f318-3da0-aba4-61be978300c9 | -18.74316 | -56.56456 | 2024-12-19 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7a9422a0-0c30-39d1-904d-c070d9157ed0 | -17.97177 | -54.00716 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860cfeae-49dc-3321-ba75-1b1082c4014d | -21.30641 | -49.39224 | 2024-12-19 04:33:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eae6e85e-14b9-331d-b3d1-dce53ce5c231 | -21.33245 | -49.21459 | 2024-12-19 04:33:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 672af0c7-2dba-3cd4-a5c8-7bbbd4254809 | -20.25521 | -55.14013 | 2024-12-19 04:33:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 050e4cfb-e855-387b-aa7b-38676fc972f4 | -20.47511 | -55.8423 | 2024-12-19 04:33:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 638af397-6f59-3ba9-bc87-8fc4f0c46533 | -19.35667 | -49.19901 | 2024-12-19 04:33:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 186e7596-cc2f-38e3-8018-da828eca7063 | -23.33785 | -46.77061 | 2024-12-19 04:33:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1d07d649-5f35-3337-841f-c2c4f376a98d | -19.06459 | -52.88719 | 2024-12-19 04:33:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bab283e6-314d-36a9-83e7-0c65e621af82 | -17.97543 | -54.00784 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d4eb973-c5fe-36f5-9f51-372f14c94888 | -23.59191 | -47.44098 | 2024-12-19 04:33:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 502c7934-02a2-3913-9bb8-9423fa3b1522 | -19.06115 | -52.88652 | 2024-12-19 04:33:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83f47905-2597-3a20-b3aa-69c73875453c | -17.97356 | -53.99991 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caa89ec1-9693-3940-bdd0-5c04cf39463a | -20.71305 | -49.64679 | 2024-12-19 04:33:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7036d520-4041-3b79-a8bb-50ee36c3be1c | -21.79255 | -55.99632 | 2024-12-19 04:33:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a36ab2f6-19f6-3f59-bb88-284c0fdcf780 | -20.77921 | -49.85934 | 2024-12-19 04:33:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c21cdf3-03bd-33a3-a1b2-9edc374bcb88 | -22.25236 | -50.04176 | 2024-12-19 04:33:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b7f95323-59bf-3778-b13f-c0ff3baae5d2 | -18.73558 | -56.55876 | 2024-12-19 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5d342282-949d-30a5-af27-d78cafb6068a | -19.70363 | -49.86784 | 2024-12-19 04:33:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca96093b-39e5-3f77-b7b5-e5315a32871b | -20.78035 | -49.85176 | 2024-12-19 04:33:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55f5525c-bdbd-303d-9621-025c344ff481 | -20.77642 | -49.85499 | 2024-12-19 04:33:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 112f8bb2-9a8c-300c-95fd-2ac26730f281 | -20.47564 | -53.67675 | 2024-12-19 04:33:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2f5135d-40dc-31bd-a1c3-d15337796608 | -22.54922 | -48.36968 | 2024-12-19 04:33:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ded63868-b2af-35a5-a968-e5c5c157d676 | -19.34055 | -54.17227 | 2024-12-19 04:33:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b104708-c15a-3cf7-8b0f-39c65adf65be | -17.97258 | -54.00264 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e856e584-6ff3-3429-a8c4-4b149fd48a69 | -17.18304 | -48.83368 | 2024-12-19 04:33:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 593dc8cf-8629-35b7-8642-77f4eacf74ff | -20.91963 | -56.55002 | 2024-12-19 04:33:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8640a97b-b55a-382d-8267-72a7c372955e | -17.97644 | -54.0051 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b4e1dec-3549-3d74-83f1-5cadcf398f5a | -19.12556 | -53.4613 | 2024-12-19 04:33:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0cf10a2-02d9-39aa-b9ab-2d95f0853fda | -28.58583 | -49.44117 | 2024-12-19 04:36:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8383620d-9be5-304f-9d8b-cb6a98ecd412 | -23.98184 | -48.91855 | 2024-12-19 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be34ada7-1fc9-3982-98c9-3b974406b829 | -26.6209 | -52.7633 | 2024-12-19 04:36:00 | NOAA-20 | FORMOSA DO SUL | SANTA CATARINA | Brasil | 4205431 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 20d9270e-6742-3fd3-8c2a-a7ddc3413e75 | -28.45809 | -52.82621 | 2024-12-19 04:36:00 | NOAA-20 | NÃO-ME-TOQUE | RIO GRANDE DO SUL | Brasil | 4312658 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9197182d-3d12-3a7d-9600-f9d920495a08 | -24.58338 | -50.94611 | 2024-12-19 04:36:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0641fb0b-b1d8-3df8-a72e-09ca6ef451f4 | -24.24226 | -50.74163 | 2024-12-19 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a12e828e-540c-3167-90ad-8d8ea6397205 | -26.99775 | -52.24054 | 2024-12-19 04:36:00 | NOAA-20 | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91eca348-77b5-3d27-bf0f-e4045dd50fa0 | -29.89207 | -51.23703 | 2024-12-19 04:36:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 1c0f45e7-7fa1-3095-a4e4-89cd57031e1f | -29.86659 | -51.16616 | 2024-12-19 04:36:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 592ecae6-be61-39f8-816a-c27a79efc8f7 | -5.2108 | -43.3067 | 2024-12-19 05:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9a1957cf-a2e1-3b6d-9720-902e39f04dc7 | -5.2108 | -43.3067 | 2024-12-19 05:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f1d68ce9-01b4-3ac3-993e-64e94875ca95 | -5.2108 | -43.3067 | 2024-12-19 05:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c851c0b8-4f3f-3b4f-b362-add6576df476 | -1.25968 | -53.52928 | 2024-12-19 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7981c86f-5edd-3d8a-a29e-771286c44eee | 2.27785 | -61.2276 | 2024-12-19 05:22:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18a7b776-2861-3cb0-b1f9-e69fe8acf803 | -1.78775 | -46.81182 | 2024-12-19 05:22:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be422e46-65b0-31f5-b066-4e7a095424c8 | -1.27162 | -54.13504 | 2024-12-19 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 790bde54-e757-32ce-953a-a0ec925f1043 | -1.55579 | -53.77409 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3ffe749-655c-3c11-86e8-a45a3be897bf | -1.58378 | -53.79092 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d5c29bb-2a98-3925-a395-40c5a9128cb6 | -1.72578 | -52.55687 | 2024-12-19 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d7ff234-77fb-3cc5-a380-8f3eb2916262 | -1.55946 | -53.77866 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fbd5800-6798-3f7f-a21d-e82bde707232 | 2.28133 | -61.22707 | 2024-12-19 05:22:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c2ceb7a-dd3e-3959-bb90-df2e2910e311 | -1.56797 | -53.78015 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc30c46-97e3-3786-aa52-b8c1786cb926 | -1.56855 | -53.77631 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8864ba0-67b4-39e1-9e59-e2ed2947338d | -1.264 | -53.52995 | 2024-12-19 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd5a138d-882b-30d5-9427-457a73427791 | -1.5552 | -53.77796 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a599a15d-3037-3fd6-83e9-25fd4e67f689 | -1.54539 | -53.7272 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2ee9473-5d0e-3700-8e71-2946493a6194 | -1.72651 | -52.55201 | 2024-12-19 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9e5ee3c-0839-3521-9d3f-c3808ffc4ab4 | -1.56371 | -53.77941 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4bb8fb3-d199-3e75-b031-b34dc075e46b | -1.30204 | -53.45515 | 2024-12-19 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b13601-ed6d-33c6-997d-4846ef2a5184 | -1.27225 | -54.13092 | 2024-12-19 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4644a035-2057-3169-9b5e-395e6e60e565 | -1.56005 | -53.77481 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f937e7ff-e12b-3537-9b23-52384e769a50 | -1.27101 | -54.13908 | 2024-12-19 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3953c1c5-13a9-393f-ac6f-48893e76cb2f | -0.25475 | -51.50232 | 2024-12-19 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3edb0d1d-7286-358e-8257-4377a350cffe | -1.58437 | -53.78708 | 2024-12-19 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f1ad9cd-5b21-38f7-bab7-b374345ea9fe | -4.28026 | -55.74291 | 2024-12-19 05:22:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e1b92c0-939e-376b-8c8b-e19752fa531a | -13.89457 | -54.61137 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6401ed0-54f8-31f3-bfd6-82d834a4aed3 | -4.35255 | -48.47108 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03996595-2698-37cb-874b-5118492d5527 | -11.83642 | -58.45552 | 2024-12-19 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fc2bd01-5d0d-33d4-a516-3db0abfa3c44 | -15.16597 | -56.46234 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4169f03-ecc4-37db-9a4b-9e436d6071f8 | -12.2352 | -54.31389 | 2024-12-19 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1206db59-022d-3898-a0b1-eda3009926d8 | -13.48467 | -52.94763 | 2024-12-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09b67039-95db-30ee-ad5e-d8baef3beeba | -15.16977 | -56.46732 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ac2d01bd-0982-37b0-b61a-0592b2fc62f7 | -13.92353 | -54.60645 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9bb03bd4-53e9-3496-80bc-08723612e8e8 | -12.90858 | -55.04777 | 2024-12-19 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e90d9e7b-7899-30c7-9a31-10eb6e6893fd | -12.5596 | -57.82929 | 2024-12-19 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eefa2037-91dc-35f1-bada-4ecb8e82eb5c | -13.92284 | -54.61216 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ff670951-50ad-3706-a22b-44983674618f | -15.16433 | -56.46447 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| edb5ed7c-f82a-309c-934a-8cb80df0cb77 | -4.35059 | -48.46553 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 885ce7e2-903d-3092-9246-f1b3e487f93e | -4.32899 | -48.29849 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1ca8978-0e94-3e5f-abee-42bc48d7b0e8 | -13.89386 | -54.61693 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de9ff62d-8510-3f4b-bbb3-c4915c4130c4 | -10.50353 | -49.12486 | 2024-12-19 05:25:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README13.md)
