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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a09fbc6-8b55-3060-bdbd-2571466244ba | -14.5633 | -48.46262 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb9fec1a-7820-3276-877e-a9c9c281fde6 | -11.69687 | -44.31596 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6b86a18-bb9d-343f-99d6-57ea2b5d25cf | -7.04057 | -46.41299 | 2025-09-30 03:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8ca58c3-72d1-3ff8-b2d7-af89100f2b24 | -12.82839 | -46.99773 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93ed98ff-ed4a-3ab9-9539-7044e1c37beb | -15.22915 | -48.03247 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54d5a5b7-c65c-30b6-bcbd-b155f319858c | -11.70713 | -44.43239 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10be907e-ee10-3997-9953-f2028e0844cd | -7.29458 | -42.86642 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ab3e3f18-fe3b-3f05-a391-b0716e6350dc | -15.26628 | -49.50167 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7190a361-fcfa-3bae-bb76-ac165419ab44 | -6.88529 | -44.52217 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb6a9e9b-c06a-3db1-99e4-f86c0678b98c | -13.06418 | -47.07541 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a1417b-4acd-3755-95f3-55a176bc9435 | -16.7948 | -39.19836 | 2025-09-30 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f8aef9a-bb32-3910-9b18-b95b74f14608 | -14.7431 | -45.66759 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d98e2b05-e708-3512-98f0-4df57e3a1b68 | -6.86814 | -45.62633 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b13f8d0d-12d2-394c-8313-b2d4c5229fec | -6.78516 | -47.1665 | 2025-09-30 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dce03920-9ef4-374f-9119-30f12292fc9c | -12.05512 | -42.95842 | 2025-09-30 03:49:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47b17fe8-a3e9-3b2b-8096-5a63bbdc5b6f | -13.38192 | -48.06876 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68349400-9168-3e96-97ad-0d2251b69942 | -12.81683 | -47.00255 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 660997ed-7f1d-3888-8056-c9cfb731cedf | -7.301 | -42.85492 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb79cd81-5c78-3450-b6e3-275a0f54a3af | -13.8072 | -47.96167 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f380a8b-9cb1-3c1d-a99f-4d4661cedcd8 | -18.12506 | -47.78769 | 2025-09-30 03:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6b609097-3b95-32f6-9268-2c043126629c | -14.5462 | -48.26754 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4bce87-591a-3414-80a9-30aa80e27176 | -14.53085 | -48.4823 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8a65d15f-5c88-3ad9-92cb-c82ec76a888e | -13.23585 | -47.30714 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35e5ec3d-48d6-345b-83ad-454992deccf4 | -13.81694 | -47.49501 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 271ed087-ea96-3464-9487-ca34de696d74 | -17.41174 | -47.12952 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2220c41-f3f0-3618-8ee2-00df1fbcd791 | -6.78865 | -44.08575 | 2025-09-30 03:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd7b50e-0f8f-3cd0-93cc-0ec9392cc7f0 | -13.60998 | -48.03481 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b150695-e64b-35e8-bc50-9e47c706b095 | -7.04031 | -43.23529 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cde8d352-5b0a-3bcf-ad52-e2b91073e731 | -7.05206 | -45.1949 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b0032b6c-9f48-365b-bdf5-b065a4eba966 | -12.83303 | -46.98417 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e6e660d-d216-3c61-b991-16339406b14d | -14.5455 | -48.2623 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 043b8b55-4521-3d89-b98d-bd5129ea56f8 | -18.12248 | -42.19572 | 2025-09-30 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 459adbab-46f1-3e24-b407-a258106894d3 | -15.91791 | -46.19994 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf241d83-40fb-3690-b3d6-18b51b57db58 | -13.61598 | -48.03287 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b308bc6-3954-3f8e-8119-38a4a14297d4 | -13.36802 | -48.16587 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41cbd801-84c8-33c5-9c20-b8788f9b497b | -14.44244 | -46.35847 | 2025-09-30 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f975705b-0354-3792-a30f-4a781c58c20f | -7.01562 | -45.2243 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d960e28-60aa-3033-9dab-3dcb31068026 | -11.25902 | -47.22942 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d673f6f-ec6b-3afb-a8ae-ab8b1406c4d8 | -11.22413 | -47.20832 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa3209b5-2503-31b9-ab3a-3607e3e0c735 | -13.76977 | -48.32321 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2155a07-1b17-3286-9ca3-423ae8c64f63 | -15.67584 | -46.26092 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f0019b7-d63e-3993-8b7a-86abfc5fc8f8 | -13.59891 | -48.03391 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc7d4b96-4673-3ffc-afda-a8778477d90c | -14.78236 | -48.31149 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6e787de-bb20-3b7a-987a-f106cf8a6e8b | -6.70154 | -44.55479 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4114e604-0b58-38c5-80c1-8099d7479c7e | -7.35647 | -42.12549 | 2025-09-30 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63b10df3-44df-33d0-92f9-eb2f85ae03fa | -6.50785 | -45.21888 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e0097b9-0e9d-3b5d-9f6e-bcaada6ff92f | -14.78709 | -48.31586 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6311213e-a355-3617-b3de-0d62cdf85aa4 | -13.63181 | -48.04475 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 735f3e37-4afa-3410-8616-55cd0a4a5ae2 | -5.5213 | -43.87642 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 5b125c5c-bca7-3891-aef0-e0bb517e20c7 | -15.26982 | -47.85665 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4db2c1e3-6c64-34c2-bc7d-affab84ed6d5 | -13.64783 | -48.04911 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80da055f-8b2c-31a1-9401-9c223522596b | -13.63055 | -42.53243 | 2025-09-30 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 10d8f3aa-75a5-319a-a94b-d1b141502d0e | -15.11883 | -46.46264 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1491fb10-95a6-33cf-bfdd-1fa60f18f702 | -13.83544 | -47.48533 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57f3c12e-e3f6-3ead-8666-06578ebcfddc | -12.84593 | -46.97265 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e4fba08-3210-3bbd-85ce-c835367e762c | -12.74463 | -46.85394 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7e96d34-fe2f-3e3f-b632-fbda240a4223 | -14.71347 | -48.25359 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb9dc4f9-cf30-323d-a533-8e8a16233f24 | -14.78869 | -48.30793 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 873b4a00-f81d-359f-b01d-9118d0deaa56 | -6.50971 | -45.23831 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2894a31-4190-319d-a380-a4a4596ae191 | -5.82868 | -42.79396 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bbbc4adb-d13e-323f-a1fe-ec1bafa30bfc | -14.52665 | -48.47495 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5bd4c9e-b791-3738-aeb5-216f3246114a | -13.17378 | -40.24291 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0ab3f91-9a82-3cb3-8e94-d0749c5c8c7b | -4.95667 | -47.60008 | 2025-09-30 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f97ed34d-dcb0-3ab1-957c-0e2606e21fa6 | -14.44725 | -46.35923 | 2025-09-30 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c345fb44-c6ca-3014-b7ac-9b37fb0dced0 | -15.90425 | -46.22819 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 009195f1-b1db-3685-9332-c94d18a67c6d | -15.68049 | -46.26179 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee826946-13ea-3805-9d5d-5446db6eab82 | -15.37457 | -47.07986 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 0cafdbce-d723-3993-9767-8d6c4ac58bd7 | -13.84499 | -47.49171 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c0a9c9e-1d75-3a26-b501-05f180c414f2 | -6.29633 | -43.44661 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81a0cb6f-e371-3591-9a47-549fbdae0db7 | -13.60057 | -48.03214 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ade99943-83a6-3632-a05b-0d42cbaa1d1a | -15.24666 | -48.75056 | 2025-09-30 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7368b2f3-3b9d-3c93-bc2f-32607df5de6c | -14.53439 | -48.24284 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7030f5d8-8d2f-3df5-be20-1c481d5024de | -7.01202 | -44.46728 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f60615de-1a50-3039-98ac-c1dc90c6e0ae | -13.65695 | -48.05994 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7163eed0-7622-3ff4-88d7-b942f1ca69b2 | -5.8259 | -43.87062 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce2c3a98-42b3-3299-8615-055564b5501a | -13.61161 | -48.03318 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 913153b9-595c-30fd-8ff1-05d7c0e08987 | -11.19877 | -47.22472 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 349c20b0-bd88-3945-b0c7-201ff22e20f3 | -15.48416 | -48.56751 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c514236f-cd46-3a08-ab21-5f558dac29b2 | -11.75336 | -46.84317 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5eaa405-7846-3334-b054-eb05d41b1133 | -7.16548 | -41.70465 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d40ad1b-cacc-3bb3-bb64-d8c0d6bad857 | -6.04861 | -42.47119 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 089529f6-55f5-398c-abbc-2ab060abc039 | -12.85991 | -46.9011 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b61eec2-462c-372f-8a88-2009a7719c55 | -11.1543 | -54.1465 | 2025-09-30 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6e03c443-01b2-3baa-9879-85e467cda8b7 | -10.1855 | -44.8709 | 2025-09-30 03:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 764aeebe-c908-3cc1-9566-08fff478fb4d | -13.2161 | -50.9286 | 2025-09-30 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 840b10f2-6e00-3dff-bcef-dac66d73c5e2 | -11.2707 | -47.2236 | 2025-09-30 03:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 49344151-c52a-3f99-936e-55b90645eba5 | -13.2158 | -50.95 | 2025-09-30 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 244.1 |
| a9b51ca7-e24d-30ae-b1ae-4822e318f3db | -10.1851 | -44.8939 | 2025-09-30 03:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 217.1 |
| a20794cd-6d18-3766-a941-b780e34ad281 | -14.5137 | -48.4522 | 2025-09-30 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cd94e912-d07a-37e4-b0c5-dd795efedf9a | -5.3382 | -43.7391 | 2025-09-30 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| fb5b004b-46c3-36b4-b1f5-5da01a54e53f | -11.1735 | -54.1242 | 2025-09-30 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| ee6fb199-34a8-3e34-a395-12b28e16142c | -11.7519 | -44.7461 | 2025-09-30 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 48212173-3da1-31f4-ab25-2dd26d475d83 | -5.3195 | -43.7405 | 2025-09-30 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 0f7a4982-f744-3516-a685-93b0a17d975e | -10.2041 | -44.8915 | 2025-09-30 03:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| aa5ce1b0-e752-3665-8602-224e014d471c | -13.1966 | -50.9525 | 2025-09-30 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 85370f0f-382f-3fe6-9af0-753ddaa40fc5 | -10.1847 | -44.917 | 2025-09-30 03:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| cb9052b8-4305-3436-a726-fa2fcb4b892a | -4.8915 | -43.4678 | 2025-09-30 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 84fe8d81-5c3a-3963-832d-8592142f1574 | -11.1548 | -54.1054 | 2025-09-30 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0947630f-c4dd-3930-a4c0-131a4bd28cc5 | -13.235 | -50.9476 | 2025-09-30 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| be1c7dac-459a-340e-a552-73d4239a3680 | -11.2516 | -47.226 | 2025-09-30 03:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |


[Clique aqui para ver as próximas entradas](README44.md)
