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
| 999f79ea-6c49-3ce4-b8ae-5d2f8efc3308 | -13.01617 | -56.85516 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35c4ad8e-9bf3-3d3b-8b27-e5b569098bc4 | -12.99632 | -56.85867 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 064900a6-0dbf-38e8-9dc7-82545cc2c41d | -13.2167 | -50.76581 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc46e872-d60b-3ed2-b221-568eeda6857a | -12.98957 | -56.85252 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f5b25cb-468f-36bb-997c-83a5360c94ee | -15.49922 | -48.52604 | 2025-08-18 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb741288-b1a0-3b08-9d80-d9d39d7bfca0 | -12.99954 | -56.83981 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36c04fc7-f4e4-3da4-b9b6-73d89a398a24 | -17.39188 | -42.62667 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 76c9d0d4-8029-3896-bdfd-9cf4a6b45003 | -14.97516 | -54.77396 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f2d7d47-8283-3170-847f-32dc5aab2d45 | -12.49246 | -45.5663 | 2025-08-18 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b305c08-006f-3be5-99a3-390072d435be | -13.2186 | -50.7781 | 2025-08-18 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 13ca7c60-4927-3661-a6a3-265850b010bc | -13.2193 | -50.7351 | 2025-08-18 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 623849e2-5236-3434-a9f4-42bfdafe78c4 | -17.0838 | -49.8899 | 2025-08-18 04:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 55e457ca-ecfb-3f01-9837-450f9a4b4b2f | -13.219 | -50.7566 | 2025-08-18 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| c79143a8-bee0-3239-aa92-0c40addb4187 | -13.2382 | -50.7541 | 2025-08-18 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 707b574c-5584-3311-add5-69ba7d120ccb | -17.1036 | -49.8865 | 2025-08-18 04:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| f9af4230-be5a-3deb-bf51-10971fccc587 | -13.2385 | -50.7326 | 2025-08-18 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 59f1e8a7-6551-390a-a248-ed181dbdee3a | -17.0842 | -49.8677 | 2025-08-18 04:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 23318cc2-de71-3c4f-98ff-664591f0e15c | -17.104 | -49.8642 | 2025-08-18 04:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 66fe052d-86aa-3d5a-9948-a877c5fb150d | -19.43621 | -43.72972 | 2025-08-18 04:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb92ae84-b5c8-3daa-8b9a-abe846f74635 | -22.20356 | -56.04683 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 576af6c0-072e-3057-aad0-96400363dc24 | -19.1467 | -47.03884 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37435f04-ef80-3717-9e9a-bc678fa6c8f2 | -19.15125 | -47.03949 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79f05ba9-7b0b-3f92-97bd-3729c184b69e | -18.90071 | -44.76814 | 2025-08-18 04:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08f49d35-ab03-3998-904f-a7ea655ae5bb | -20.87275 | -54.96497 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b02b71-ac63-3d61-9221-5b964d777dd8 | -20.3321 | -41.61511 | 2025-08-18 04:51:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| eaecb1b1-748a-3eb5-ac0e-d781a4f84041 | -22.3325 | -47.72321 | 2025-08-18 04:51:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e17ab49-db2c-3815-964f-b2df702bb896 | -20.42878 | -43.68118 | 2025-08-18 04:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f98672d9-c8d5-3477-8b8e-750616a074c4 | -20.04568 | -45.46274 | 2025-08-18 04:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e6a6376-d5e3-339c-9456-df7cdcfaffbb | -20.20916 | -47.03226 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48fd8a15-e962-3a6d-aaa1-e55eb452519d | -19.14207 | -47.03118 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81b7ec06-7e3e-394d-8d32-6b8bdb976a1a | -19.14432 | -47.01908 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad516196-a64f-3a71-9d2d-40bc4bb8c6ff | -18.90038 | -44.77132 | 2025-08-18 04:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf513a1b-5773-371b-a720-e9aa73b39a98 | -18.61979 | -49.1958 | 2025-08-18 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d08d074-841d-32d8-b6b3-130da507afdd | -22.27321 | -55.95042 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fa30bc-9e19-3f8f-9cf9-aacde5b6eaa9 | -20.40875 | -54.69429 | 2025-08-18 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8b882be-0049-3186-8cad-2bdef29b18cb | -23.0863 | -54.18722 | 2025-08-18 04:51:00 | NOAA-21 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 531b4fa2-ec8a-3987-9783-b59c9643964b | -21.82074 | -48.1421 | 2025-08-18 04:51:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07a3a5d2-46cc-3901-80b6-36bce23229ca | -19.14618 | -47.04347 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2166de79-4a6f-36af-a0c2-b9d031b64840 | -20.35028 | -45.30754 | 2025-08-18 04:51:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cd774bf0-6ea5-3601-9724-01208efac6c3 | -20.01084 | -46.43475 | 2025-08-18 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cd9dec3-0e43-3c65-afb9-570b609469db | -19.14322 | -47.02164 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 812941c6-f51f-36f0-91b5-6462a10d339c | -20.20881 | -47.02904 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b541aa4c-dfe9-32df-82e0-a50af7dc84d6 | -20.86611 | -54.9638 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76d240a-7ff4-3d93-b97f-693d1da8ee7d | -20.04604 | -45.4595 | 2025-08-18 04:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94d6b45f-73f1-3fbe-97eb-281ae20b0118 | -20.28626 | -42.54005 | 2025-08-18 04:51:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e209b1d-49e2-3dc2-be59-206f80e8a149 | -22.08139 | -45.05659 | 2025-08-18 04:51:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| abb74ec1-7bb4-3d2d-bbd6-c0ce95503375 | -19.14269 | -47.03349 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2fa7d8f9-0e59-39e6-897c-dc22e192e479 | -23.30454 | -46.89014 | 2025-08-18 04:51:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 736cb710-0622-36f3-bd99-1366784cbfea | -20.00218 | -46.15356 | 2025-08-18 04:51:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a2ac29a-5a69-3133-9a52-6ed546da066a | -20.20824 | -47.03425 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a9dbc6c-e880-3040-87c1-83bba05a51ca | -20.86221 | -54.96692 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa98c777-4d9d-3096-ae9c-0fa4e8ff1dae | -19.84687 | -51.20225 | 2025-08-18 04:51:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c30f21a-3660-3c53-bd33-6b95d5c39e53 | -23.07418 | -45.60716 | 2025-08-18 04:51:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5838ada4-6593-37d4-8dec-50dd3cec604e | -22.20146 | -56.03859 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 41638768-65b3-3040-9599-f211b86c9e1d | -19.38028 | -49.05709 | 2025-08-18 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8514ea4-9462-340b-9fe9-fa20b4af951f | -20.8628 | -54.96321 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74d7ef1a-fdf1-3c37-9589-ef480763e448 | -19.53618 | -45.61539 | 2025-08-18 04:51:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd14d1d2-54b9-3e63-aba3-bfd4595b5e75 | -22.20022 | -56.0462 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54a49800-23b5-3cfa-a242-51120c82b4af | -19.15581 | -47.04002 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d6baa9f-d2d6-35d4-be04-b85e0f5842cd | -24.38488 | -49.0922 | 2025-08-18 04:51:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 002a75e4-1d32-357e-bcf9-565a1f9f29a5 | -20.21751 | -47.03516 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 860f11e7-1711-3478-bf83-1b2a95d59b3e | -20.47817 | -53.67468 | 2025-08-18 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06fa3dda-1b76-30d1-898e-59bfff22ebad | -22.33193 | -47.72828 | 2025-08-18 04:51:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31fae53f-f852-3885-8380-ad767e0b2ad6 | -20.33222 | -41.61359 | 2025-08-18 04:51:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 013eb02e-891c-30e3-9601-98cab59f3123 | -19.53597 | -46.12247 | 2025-08-18 04:51:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9a74baf-01bf-3e57-b87c-da4dc608b0ec | -23.30618 | -46.89016 | 2025-08-18 04:51:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| baa0d52a-dfef-3083-bfd2-ad7e9d58eb70 | -24.28267 | -50.25974 | 2025-08-18 04:51:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29300c5e-d404-36e7-97b5-f172d45e561c | -20.21317 | -47.03803 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec2879e3-f58c-3f1d-96d2-b3082f42aed1 | -22.21539 | -56.19823 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 252dc6c5-0358-3cbc-bf26-3654e2b6ad49 | -19.14722 | -47.03428 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79ab5792-44d4-38d1-a05e-cccb4eccc204 | -20.4066 | -54.68636 | 2025-08-18 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9c1a89f-71c6-3db7-a119-42fff29aa6ac | -20.86884 | -54.96809 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe9ce3c7-a3da-3510-ad04-6e5092a16d70 | -21.79605 | -46.5787 | 2025-08-18 04:51:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cfa5d9a7-7b7c-3dcb-847b-57ec97ead3b8 | -20.04535 | -45.46583 | 2025-08-18 04:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 079eb392-5758-376a-8fd4-aaed4dac892f | -20.42313 | -43.67933 | 2025-08-18 04:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 5262a29c-583f-3aa8-b104-1ddd32d2bce8 | -18.61585 | -49.19522 | 2025-08-18 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc87e898-0eab-3de0-bed4-b16b89a7e940 | -19.15231 | -47.0302 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8301ddb7-71d5-3329-8338-bf806875585d | -22.07602 | -45.05585 | 2025-08-18 04:51:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c97ac231-92f7-3f51-829a-71266ae51db8 | -20.26089 | -50.65689 | 2025-08-18 04:51:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 67e6c6ea-70f3-309d-b040-6fae7da640a5 | -19.1569 | -47.03052 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b72f535-1702-3b1a-9abf-ddae474c822d | -22.20084 | -56.0424 | 2025-08-18 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd156aaf-dd73-39f7-9bff-d27755253459 | -22.14218 | -50.02691 | 2025-08-18 04:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2cec83b0-d1be-3358-a89c-70094710346d | -20.93123 | -56.89138 | 2025-08-18 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30683fc3-90bd-3e4b-b38a-09ca5e4962ca | -21.42726 | -43.8821 | 2025-08-18 04:51:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ccc82417-0ef0-3d6b-a5cf-3d49eff46cf5 | -20.20977 | -47.02703 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0278532d-5907-3b89-908c-2e7ee7bd377a | -20.55859 | -54.58511 | 2025-08-18 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10d55dad-4047-38d6-b78d-44416513e6eb | -20.40933 | -54.69061 | 2025-08-18 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55ddf2d9-2f3f-312c-a6db-5238771d2cd1 | -19.14321 | -47.0289 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59477300-f6cf-38a7-8caa-34146e3e3384 | -20.22275 | -47.03017 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 187f1c23-f434-379e-833a-b4bb6bb28d0c | -23.50645 | -48.31358 | 2025-08-18 04:51:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| da00aefe-b0bb-3aee-b2fd-a7e76bd0e852 | -19.13129 | -47.00533 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0997e5b4-06aa-330e-8528-efaee8ee48ed | -20.21695 | -47.04028 | 2025-08-18 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e733dfa8-508b-312c-afc8-a6b7073f80c2 | -20.87156 | -54.97237 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33b503c6-fe6d-31b3-a954-0083673827b1 | -23.38162 | -45.43919 | 2025-08-18 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ada8d74-acc4-3516-a56e-880226bbd654 | -20.87215 | -54.96867 | 2025-08-18 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ac8ef0e-19f2-3444-9b0f-6f89dfc6c50c | -19.13173 | -47.00768 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1090c75b-7a8a-35f1-8ed2-622295103168 | -20.40602 | -54.69003 | 2025-08-18 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49bf8551-77ab-3209-8c1a-4cfbb1d5199c | -19.15635 | -47.03533 | 2025-08-18 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b96f54c-a651-317f-ab2c-3b6d886a74e7 | -20.5165 | -47.35783 | 2025-08-18 04:51:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d4011b-1af4-3e9d-a9f0-0e04a85eb150 | -21.11712 | -44.23132 | 2025-08-18 04:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
