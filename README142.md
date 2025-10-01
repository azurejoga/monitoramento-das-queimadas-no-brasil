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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d59d559-f4f6-3762-92fe-5608fd12af18 | -10.82646 | -46.63904 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a111042f-992b-3429-aad1-2ab3ea7ecf23 | -12.77341 | -42.44046 | 2025-10-01 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c1e6a189-eaf3-37f3-814b-240b684ce204 | -11.13596 | -43.37901 | 2025-10-01 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a5f8e210-5c9c-38d6-a9f8-3ad22d60d1de | -14.28256 | -41.16795 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| eeeee673-8110-3931-9a37-5e1e805a01dd | -12.55421 | -41.83196 | 2025-10-01 12:00:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 12553284-6aa8-3803-b4b9-afe7fe3e90b5 | -11.27061 | -47.20659 | 2025-10-01 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ecc2ee9c-1f63-304e-a55c-2f9d384234bd | -8.52879 | -47.27672 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7ad58291-1f5e-3dd7-84c1-4a13d8370bde | -11.4559 | -45.02152 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| dcbfbf91-f012-3860-afdf-b26aeeceaa89 | -7.87587 | -45.28208 | 2025-10-01 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 02797852-6ada-3ef4-88f3-e8fd4600653c | -12.48004 | -50.23466 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3f3eeb2b-2696-329e-a4af-b00427472b42 | -10.84184 | -45.38131 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9dd460f0-6b96-329c-82c9-b16092bea104 | -9.27093 | -45.68365 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f58d1411-f0f8-3fa4-85cc-ea4b40b31b10 | -11.4102 | -41.71348 | 2025-10-01 12:00:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| bb40e7bd-e47b-3cfe-bb38-0a46522e6651 | -12.80649 | -46.89024 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 77644d6b-55c1-35ae-9123-a5357a8c5f1a | -12.37459 | -50.21641 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f97c3a55-c958-3fb2-a25e-ccb9ffbdf4bf | -10.11034 | -50.32352 | 2025-10-01 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5e058bd6-c23e-3726-837c-67003a4cebca | -9.80683 | -47.86038 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| aba88da9-3a32-39a5-894f-e45212e7f908 | -9.44409 | -45.47801 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4bc6a8e5-9ea3-3917-932c-05ea8cb9ddd5 | -13.33126 | -47.82857 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| eb36044f-941a-3426-9b84-deb14244db8f | -10.95016 | -46.55789 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ffdd371d-4bac-3409-a6f9-d21ee98f4496 | -8.64942 | -44.84921 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| da04c24f-3f24-3cd2-880f-5b963e602d38 | -11.19009 | -47.20101 | 2025-10-01 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e2a9ccbc-0007-337b-9c08-49c600c39a31 | -14.21194 | -46.08988 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 23b224f5-16fb-31da-986d-16eb370824bc | -9.8265 | -48.25961 | 2025-10-01 12:00:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e7ef07e0-6ec1-363c-8f27-d7ff25ce95e9 | -13.66958 | -48.08585 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6a527f16-a42f-397b-87b8-62d218d6cd7f | -9.99571 | -46.16934 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a143ad0b-0682-3002-9ae9-ecbcdec27bb2 | -13.0841 | -47.07431 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 66099480-0755-3129-a3e6-c9acde669962 | -7.86771 | -45.26971 | 2025-10-01 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 48905f0e-69fc-3b53-8662-221711861d85 | -13.62689 | -47.64854 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ba057733-3135-3f15-93e1-400b936d872f | -14.22371 | -43.51812 | 2025-10-01 12:00:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 36ae51d0-adc1-30ee-9d43-78e51c984a14 | -7.61761 | -46.6013 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 7e7d3b65-d45c-32e3-a199-99efe8a4cc1d | -14.09323 | -43.90925 | 2025-10-01 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 29d7ccea-7b56-3f77-bb2b-5b799e919ba1 | -13.31023 | -47.21033 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 830e499a-6533-3cf0-9632-8efc28783a41 | -11.42389 | -43.50105 | 2025-10-01 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3da41d85-ba5d-3e26-9dbb-c08eca6e5072 | -9.82377 | -48.27695 | 2025-10-01 12:00:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 78914446-8c00-38e1-bef0-6c4358be45d4 | -11.83551 | -44.95358 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a4b4545f-78f4-317f-b8fd-db45ff3c1ed7 | -11.94028 | -47.0529 | 2025-10-01 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4d6b011d-0ced-3662-9558-8c9c0b52d988 | -14.21084 | -44.93388 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f7db5752-2cdc-371c-8f73-b53153e6fd4c | -12.66639 | -46.86337 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a4c6741e-795e-357d-b5ae-1730fb9d7834 | -13.32659 | -47.85706 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2dbb475e-2493-3203-8493-337dfd8418b3 | -10.92492 | -46.46146 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a301680d-45dc-364d-97e1-9c8bbba8489d | -10.83234 | -45.37994 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| bf9331cd-a820-3439-92d2-1d91e391b77a | -14.31484 | -45.22534 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e57033fd-f477-34d7-aac2-534ab0b0ee64 | -13.8834 | -40.71663 | 2025-10-01 12:00:00 | TERRA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| db090e85-6769-3198-8a51-6e5f93658ad9 | -14.35457 | -43.82766 | 2025-10-01 12:00:00 | TERRA_M-T | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 045f977c-a2d3-3f32-90cc-5d73492e1492 | -13.45907 | -47.23658 | 2025-10-01 12:00:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7e18020d-de5d-3fd4-ac80-8b9a7db91406 | -9.99387 | -46.18107 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2fe35ded-c2cb-3707-a25a-fb1591ef41fd | -13.32889 | -47.84306 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| bd2bcf40-9c65-378f-b425-a3785f56d9b1 | -12.37831 | -50.19495 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9b0e5136-99d3-334f-8ca8-222d7d28fedc | -12.27474 | -44.11448 | 2025-10-01 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38038ec1-7738-305a-b2df-3524924752aa | -14.18983 | -46.10755 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f1b2b599-6802-3bfd-a7aa-3aa3614f62c9 | -13.78078 | -48.03829 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| af3e9d6c-fb1e-3cc9-81cc-5dc19a18ece0 | -12.83334 | -47.04056 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 287f1178-4684-3117-9a06-da614621afd1 | -14.06554 | -45.04128 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51014aeb-707d-3ab7-8db4-72c327708ae6 | -12.76197 | -46.90898 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 48c76799-6fb6-3a50-8ff8-8387a8754437 | -11.81161 | -46.62658 | 2025-10-01 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6115b111-aa75-3370-b339-1b73136fc1a8 | -8.89756 | -46.66492 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 89d14f3e-aff4-38ca-a822-5e48cd21fe43 | -13.81825 | -47.50079 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8f8144a6-1bf8-3057-9ce2-00f9af292c96 | -11.86193 | -45.02775 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d91eecc1-6b4e-3420-a9a3-98f58d6fe9e0 | -11.83886 | -48.06092 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 1db79274-2c53-3ad2-9981-18617726b63a | -12.01796 | -42.50764 | 2025-10-01 12:00:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 81d82125-39db-3553-aa29-ac61e90bd74c | -11.9256 | -47.88437 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9cfab9fa-e454-3a03-a051-47dc96251b5e | -11.77895 | -40.89547 | 2025-10-01 12:00:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 2610decb-337b-3c84-836e-2808ce9e8af2 | -13.01628 | -45.20509 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 607f06fc-4ec1-388e-9400-dc66df1a8cdd | -11.61295 | -45.03152 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1722d6b1-5b50-302c-bdb4-3de03d9778c7 | -8.90354 | -46.6252 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| ce135039-f5ee-31e7-951c-7938eed2c769 | -11.91744 | -48.00351 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| a66f30bf-063e-30cc-bc61-cec722f37934 | -11.20679 | -47.19662 | 2025-10-01 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7b667eed-e0bb-3898-b81e-42c98bff57c7 | -12.65297 | -46.94784 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f7d46834-d159-35d7-bbe7-d1fedb9e127d | -13.37777 | -48.1069 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 1fa64943-4f14-3f48-9991-f6179b2af845 | -13.17645 | -47.78067 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 5007bdb4-b25d-3319-a542-527a48ffe5d1 | -10.80206 | -46.66076 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| cdb89108-bba8-330d-97fa-12b8e9816db2 | -12.63127 | -41.67236 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 5fc17bb7-f83f-3dcc-a9be-a6a903bf3966 | -8.50409 | -47.28794 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f6369cdb-bc8e-379d-acce-2259cb6a308d | -12.00272 | -46.58482 | 2025-10-01 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4670a6f3-9698-3b65-a662-956ea9b0fb07 | -8.53624 | -44.69401 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| ce428913-4cad-3292-94fa-c4c37e896adf | -10.08881 | -50.19771 | 2025-10-01 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 6c3c5846-b291-3302-98ba-64822b9902be | -14.51472 | -41.75167 | 2025-10-01 12:00:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 34ba4f37-a6ad-34d5-b67d-398a502209f0 | -12.13401 | -42.65961 | 2025-10-01 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 70.2 |
| a9539a61-4f5b-3811-a348-21bc1aced8d5 | -13.0148 | -45.21486 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| edf2f539-f457-3080-85a3-369720d9f8a4 | -14.36023 | -45.90768 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9cda906e-d8e5-3141-b252-c3d8788c1d15 | -13.7046 | -48.64374 | 2025-10-01 12:00:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c2ec67f2-f07b-3184-959c-dd928847fdce | -10.62768 | -48.58875 | 2025-10-01 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a5174b24-cb05-3351-8c9f-706c8ea7591d | -9.13078 | -47.62302 | 2025-10-01 12:00:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f6555e7c-fe2c-3cc2-9437-128de407378e | -8.53772 | -44.68399 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 28fc10b0-ca22-3b0e-8394-42400b161441 | -11.76513 | -46.85717 | 2025-10-01 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4576031-765c-31df-b91c-083e1c8641a4 | -9.93056 | -43.68187 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17488e02-fbdb-35b7-b727-539662339684 | -7.62031 | -46.60786 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 913a6e1d-4bab-3213-825e-4f01c55052ca | -14.18822 | -46.11799 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| aeab57c1-5a34-33ef-8c45-101bee03dc94 | -9.61618 | -45.77302 | 2025-10-01 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b5c5c6fd-c716-3838-8625-c74d794fb617 | -12.77409 | -50.56826 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6351dd74-71e8-3a88-afd1-cd64f4678e38 | -8.67911 | -47.71317 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1d73a215-5a47-3bb5-97b9-fe86a03ef94e | -9.94349 | -43.65588 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7d3d8ce2-ebbb-3636-8a60-bbc401b95507 | -12.27608 | -44.10533 | 2025-10-01 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d3d05aa7-7544-34d2-a39a-e8f595dc0385 | -11.84496 | -45.01534 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 4b848d19-20ff-3d2e-82d4-8f31731db23f | -12.76665 | -50.55975 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f70bc78a-357b-3ee4-9971-6581de2f3c43 | -13.02398 | -45.21629 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4677ad54-830d-3a58-901b-e30ec68f18b1 | -11.44846 | -45.02383 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 244c2209-441c-39a4-8651-69231314e290 | -13.21977 | -48.50809 | 2025-10-01 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4d2183e9-317a-39f3-b528-222195adcdb5 | -11.46335 | -44.97257 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README143.md)
