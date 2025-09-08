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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f51b42b-5732-304b-9c10-680450d16086 | -18.03956 | -47.08649 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5d7659e-a5d9-3150-bd77-9c613aece2ae | -16.91208 | -45.82273 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 940c12d6-4f20-3a38-bbae-791c1ad1ea44 | -16.9101 | -45.833 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| df3c1705-7310-399c-909b-7bdd7261fc8c | -15.22886 | -52.35393 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d6a207-b1c8-3af7-86fc-e5b7b2bcb146 | -16.94085 | -45.85115 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50944cf4-6b5b-3e0c-8491-e9b668c62499 | -17.69762 | -43.53503 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3da792d0-b190-35b9-899f-26f149c3b612 | -16.91026 | -45.81026 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dee38447-1bde-312f-a4b0-a0366c24223c | -16.30017 | -45.69164 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb507118-c3e0-3822-b040-4964abeeac89 | -17.61678 | -44.83305 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| facad039-065e-3b10-989e-93ebc0c2d9cc | -17.62697 | -44.1843 | 2025-09-08 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a60cf1c-1976-35ce-a061-8641ad222f6b | -15.82856 | -52.29018 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64b378c-ab36-3ca3-9edd-fa7a37192512 | -16.89971 | -45.76276 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f1757f8-df1c-3c7c-b46d-9f5dcf88e516 | -16.63972 | -49.15673 | 2025-09-08 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9c3a8ad-dd19-31cb-b75d-5bf70cfc7e89 | -19.40096 | -44.51148 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 341cdbbf-2fdb-3da1-b25c-9cf51cb15e3a | -22.27853 | -45.73793 | 2025-09-08 04:04:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26269636-fa05-3c1d-a00a-5630fe2c2b05 | -17.58017 | -49.79829 | 2025-09-08 04:04:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 331ffdf3-2843-34c5-bda8-da2796aaccb1 | -15.83327 | -52.29528 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af64231e-bc72-38f7-9d67-ddeb7cbb65da | -16.29158 | -49.56005 | 2025-09-08 04:04:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0e507cc-1349-35fe-ae62-378f28d3cb10 | -15.83161 | -52.30329 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8fe3760-8c11-38f4-b107-41a3c37cb768 | -16.94339 | -45.81535 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5db081e7-7cb2-3ec0-aa8e-827fe09564d9 | -18.0398 | -44.33993 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dfb4552-926f-31b3-9692-f725192f0e5e | -16.91157 | -45.80446 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffb2dff1-ebde-376e-b5bb-c0458b01dcf2 | -15.91711 | -49.07108 | 2025-09-08 04:04:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 615efab2-8ad2-38ca-978f-3b1c07ee543f | -16.9154 | -45.84638 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e2c3419-7078-3ab6-bb9a-fac23ce86ba3 | -15.24329 | -52.38438 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51fa3b6f-181b-3e72-acc1-4c4fc0aed527 | -16.63771 | -49.15394 | 2025-09-08 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38f4f767-9e9f-377e-832b-40f1a485253c | -19.21164 | -43.73533 | 2025-09-08 04:04:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0201f431-4a3c-32c6-8e7e-da2dac2971ff | -16.54082 | -45.10288 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36c388d9-0437-3f94-b727-1722555bf9ea | -19.50864 | -42.56936 | 2025-09-08 04:04:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 90bee9bd-6d10-37dc-b48a-deb205dafdbd | -16.54364 | -45.10766 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 755ff628-962d-3c41-b0fb-40935418fee9 | -19.638 | -46.57977 | 2025-09-08 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79ca7f8d-f3af-33fa-b3f7-309dad2b6879 | -15.25524 | -52.38327 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0d93fd4-e8c3-3dc9-b26f-1e76da9396b2 | -17.96458 | -45.28836 | 2025-09-08 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7d1112-966c-3fbe-a8d3-020986dc2c58 | -19.9242 | -46.17543 | 2025-09-08 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0980a070-733b-341b-858c-eca22854889c | -17.58415 | -49.80109 | 2025-09-08 04:04:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f008f40-b724-37f0-9822-403944867d12 | -16.33505 | -52.92364 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 206ca99a-6a6e-33bb-8bd3-a0e88d06b582 | -16.34941 | -52.94014 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1724ebc-fe0b-3c1c-8a8a-884764333f03 | -15.76412 | -53.56542 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ac50de3-e24d-3150-9173-ac4f0ed35308 | -16.52317 | -45.0996 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7328fdb-b00c-3719-a3c3-3ea1304bb2b5 | -16.95188 | -45.76699 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b0bb29b-a328-3c96-b71e-b1492264d055 | -19.35921 | -46.28721 | 2025-09-08 04:04:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ef093a8-a353-3881-a25d-95a736305459 | -16.29003 | -45.68521 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc400f56-da7b-30b0-b81a-b0a43e2f5503 | -17.64201 | -44.78004 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fd38616-49ef-3814-92c6-eae41c472863 | -18.41025 | -43.89809 | 2025-09-08 04:04:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0cbcae6-5379-3e49-8fea-adb5479e9ab0 | -17.15514 | -44.44145 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 81e85f89-ac24-301e-aded-a4f921699e0e | -17.1483 | -44.44018 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cdc406b-f22c-3ca1-81ab-19939c431883 | -16.89895 | -45.76714 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c207a464-fb47-3904-ad80-369f762b2b6c | -17.24234 | -46.69452 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13f0184c-1308-30da-8f22-388f5211789f | -19.64761 | -45.97143 | 2025-09-08 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abacb516-43ea-32ff-9d3c-415f9066f889 | -18.95612 | -46.79734 | 2025-09-08 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fa1c2a3-e4c7-3d3b-8b9a-031605fd92b5 | -20.74582 | -43.22936 | 2025-09-08 04:04:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 056973a4-6706-3cd0-9f6e-2d49da5799b4 | -16.91052 | -45.83154 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 27a5549f-fb7a-3ae0-ac22-38f56e052301 | -17.97312 | -47.8172 | 2025-09-08 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb66ae4-0b7f-34ca-a20c-741883b29c07 | -16.3294 | -52.92227 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3e16b07-3e79-36ba-b5d9-6640f4bc51f4 | -16.34208 | -52.94661 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba5be177-b0d6-3473-8d34-e2ee7a8ca0dd | -19.00374 | -46.90195 | 2025-09-08 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11473e78-04b8-3625-a161-2c666caaa54c | -15.24422 | -52.36472 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bb269e5-053a-37a3-a215-60ca3db3ae3a | -17.71362 | -44.48277 | 2025-09-08 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1bc62b3-2da6-3ea3-a1dd-898521bcb6ff | -19.4519 | -47.88594 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5759d101-8bdd-3f5d-adae-c554ea9adb8a | -16.77606 | -43.87046 | 2025-09-08 04:04:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd8d8388-0651-36a5-88b6-95004d8196e1 | -17.83803 | -44.24487 | 2025-09-08 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2508cfac-288f-3f22-bb9e-20097e154618 | -18.02581 | -47.11853 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a8de1fd6-e53b-364a-8bdf-9ddc8ffae452 | -19.35391 | -44.52252 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9aa89967-8218-3638-87fe-66434eb115bd | -16.43852 | -49.28727 | 2025-09-08 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dc0ac93-4e1a-3c88-946a-c9e8f566b4cb | -22.69249 | -46.92748 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| fd36e3f6-dc87-370a-96b2-203025e94a2b | -15.82742 | -52.26793 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e14cb93e-b5f9-3272-8661-34002993f261 | -17.65525 | -44.18191 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c40da88-5e3c-3ac0-8152-971b921de007 | -16.16048 | -47.91916 | 2025-09-08 04:04:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b23a94b-19db-3460-a278-ec8c24af3083 | -15.26008 | -52.38819 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ead7ece4-2eee-3494-8d2d-de66efa6a2a2 | -19.4621 | -43.80201 | 2025-09-08 04:04:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e882970-3277-3323-8496-b71d96d9b8fb | -15.25365 | -52.39092 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8709b035-3418-3053-ab12-327bd6a37426 | -20.68241 | -46.32778 | 2025-09-08 04:04:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3053173-253f-3f34-be1b-754d521d9b86 | -19.52818 | -47.88707 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10a3a5db-a846-3ed6-b4e8-0dfe6472551a | -16.34854 | -52.94425 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74957cf7-31a0-341d-b123-4456e8aaa4c3 | -15.73641 | -53.53957 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1e1e052-2ddb-33ba-b5df-50fade96826c | -16.28639 | -45.68453 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0dbc580-4049-38cd-930e-81744819f478 | -17.71087 | -44.4782 | 2025-09-08 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa796b93-674d-38e5-b39b-85de17935e67 | -16.63859 | -49.1492 | 2025-09-08 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 597a5fbc-aafe-397a-afbd-f48506be40d7 | -17.85728 | -44.33839 | 2025-09-08 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a450a793-6c9f-3263-9935-24b4a1364cee | -19.59592 | -43.689 | 2025-09-08 04:04:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c06b3f06-da8f-39a7-ac62-7a35a7c2e1dd | -19.52037 | -47.88546 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c281e82-48e5-3fca-aded-b1478959d2b3 | -20.92839 | -45.26915 | 2025-09-08 04:04:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f562239c-7ad0-35f9-9dbf-dc9a9131a07f | -20.85061 | -54.98169 | 2025-09-08 04:04:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cff63b-b382-3e5f-b367-ef17d91df944 | -16.91162 | -45.82415 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5420b94f-09c1-325c-afe8-ccc2c347ddf1 | -19.37797 | -44.50333 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b63d689e-50a5-34b7-811a-81c92d434c36 | -18.85091 | -44.84118 | 2025-09-08 04:04:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b02a7980-f57e-3a47-ba0c-e49a81cfd566 | -21.54887 | -45.75237 | 2025-09-08 04:04:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76cee64e-2195-37c3-8479-482dc9a68d64 | -18.78733 | -44.40538 | 2025-09-08 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe1e1bf0-4d57-3ee1-88b7-64a8f4bcebc6 | -15.68334 | -53.55412 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdbce9dc-c78c-3b6d-b61b-aa22c90f0957 | -19.69533 | -49.28379 | 2025-09-08 04:04:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40c6ad5d-7829-3766-aefd-8879a39586f8 | -16.95266 | -45.76259 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f96d6bc-4a5f-3d0b-a8d7-75837980233f | -18.16125 | -50.67499 | 2025-09-08 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 645f7dd5-dd4b-35ac-a36f-51ddfa4d6cc8 | -17.76771 | -48.62276 | 2025-09-08 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb4dd993-b0b8-30ff-9e30-17dea399f993 | -16.05113 | -48.15758 | 2025-09-08 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d91a3039-4bbe-3ea4-af0a-bef91164d3d5 | -16.28354 | -45.67945 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caa255ad-b7c5-3750-8e88-9e29b56aef15 | -18.15537 | -50.67956 | 2025-09-08 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec9abeb1-64fe-3283-9ffc-618e00e7fd55 | -15.23193 | -52.35474 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60b2959b-1ff2-3b31-b65e-2eaafd796300 | -23.18444 | -47.24948 | 2025-09-08 04:04:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee23eb20-7122-307a-af4f-c01fa3cadc85 | -17.1524 | -44.43682 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eff3ecc5-1f18-3472-a271-b1b9ec482aee | -16.64064 | -49.15199 | 2025-09-08 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README47.md)
