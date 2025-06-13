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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d74198f-68ad-35d8-89cc-5656657ba304 | -9.79212 | -36.99104 | 2025-06-13 03:45:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f3be20a-4766-32f5-87e4-c2ce89a0f8ce | -10.65607 | -44.49167 | 2025-06-13 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4bcafa7-f77e-3000-a472-f035e2c0d4a1 | -12.76911 | -44.414 | 2025-06-13 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5776bf1f-4908-3b1e-960d-299331bc4532 | -9.67265 | -48.77016 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e99f05b-7d2e-3a40-9136-10d242e26d02 | -10.69916 | -49.49663 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 741d9e27-23fb-3fc6-b96a-bdb9c3b72a7a | -9.38902 | -48.42889 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87ebd030-dfce-3947-ae8b-70dec11dd327 | -9.88131 | -46.27692 | 2025-06-13 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ddbc2b43-5357-334b-a29c-de5ad97d03f4 | -9.66718 | -48.76315 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c28fdd31-6445-3b40-a7d7-db7cc04d49c9 | -9.40852 | -48.43241 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa5163b7-e779-310d-85b8-dd4a1fbeecfd | -10.69572 | -49.50398 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a4bb1312-15de-3388-998e-d43690e35210 | -10.64766 | -49.42918 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| aaa0e240-1e2f-32e9-89ce-8953206b51a9 | -9.41023 | -48.42498 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06dde5cd-6ade-3a85-8b83-473a106c4e8c | -11.79834 | -43.78889 | 2025-06-13 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f502d52b-fdaa-3f6e-8d19-93e2e0909f41 | -9.791 | -36.99814 | 2025-06-13 03:45:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 60d07f80-5be3-3cab-852f-d00b0c2beb83 | -10.69821 | -49.4915 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c6f65c42-6989-3d1b-9e36-68359891f418 | -9.40376 | -48.42366 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9bfbe2a9-1556-3814-89c7-0fb9def499ed | -11.5735 | -47.4372 | 2025-06-13 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 067cb23c-4821-34e8-9d3a-b208e7e711d9 | -8.95738 | -47.2733 | 2025-06-13 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6126f4-b49a-340d-9a65-58dd4059fbcf | -9.36385 | -40.41929 | 2025-06-13 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b22c863-d719-3db4-a67e-735596ef68ed | -9.4107 | -48.42141 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a281fc0-0c66-31c3-9605-b1960ba5d155 | -9.40269 | -48.42922 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0db66242-75bf-3ab8-9b93-6ac1d62abc49 | -9.40313 | -48.42561 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 76812737-1cf2-3df6-b4ff-f171be002de9 | -8.96795 | -47.97105 | 2025-06-13 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef3325ea-c9c6-37c4-834d-8cc1c62140be | -8.5938 | -45.86559 | 2025-06-13 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5838600f-fda1-3c60-be5f-9cb9d6c3bf00 | -9.40917 | -48.4305 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e418bbb-125a-3153-a6ee-f0862dd7c033 | -10.18273 | -49.49801 | 2025-06-13 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68894f7a-416e-3539-aaba-04eed162d0a4 | -9.39726 | -48.42248 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ece88ca0-5468-383f-91d9-c69f6c8b615a | -10.65112 | -44.49076 | 2025-06-13 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e403a498-da9f-3b34-bcdd-db3177b2df67 | -9.84705 | -44.70901 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9098b608-310b-31ca-85f9-f0ae2fb7fd23 | -10.65215 | -44.4851 | 2025-06-13 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 028393d3-db28-32c9-be0c-0f1657b37e49 | -10.18144 | -49.50439 | 2025-06-13 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5af4f0e9-a01d-3ee5-b9e3-14841c694ebf | -12.29289 | -50.10763 | 2025-06-13 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c309bf1-da39-312f-9919-d24fd737b611 | -12.2839 | -50.11167 | 2025-06-13 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54438510-0f99-319b-aba1-6ae8cca53c68 | -10.58332 | -37.13123 | 2025-06-13 03:45:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4885178-cf86-356f-ac5d-db92e9d65b4c | -12.28522 | -50.1053 | 2025-06-13 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bec8da5a-8fdb-3992-b1ef-e0c54c70f7e4 | -12.05675 | -48.07518 | 2025-06-13 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dac9ed4c-2212-34d1-9c77-a2dd64e72c64 | -17.65629 | -47.45804 | 2025-06-13 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c46a8bcb-c20e-32c6-a96b-983e7e41b6d6 | -15.36345 | -47.87627 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02994c9c-6423-30f3-83db-c7cfa1b36dde | -21.3497 | -48.67092 | 2025-06-13 03:47:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e77983d5-2f85-34a5-beab-e85e77b4f184 | -21.34894 | -48.67439 | 2025-06-13 03:47:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4f18d4d-1205-354a-a95b-e7840b5c0af8 | -15.36262 | -47.88024 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf25025f-89cb-3ff6-b77a-215d2ab8dc2f | -25.45876 | -49.61162 | 2025-06-13 03:47:00 | NOAA-21 | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e80c9f14-a136-318b-aa84-e0de01f99f2f | -19.7165 | -40.35326 | 2025-06-13 03:47:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a56ee9f1-c1d4-30b1-90c1-6b181664686f | -17.21235 | -44.79914 | 2025-06-13 03:47:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ca6a40f-e975-3635-9eda-474cc1ca9127 | -15.36096 | -47.87668 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34887018-0b92-344e-ba61-9cecaf87793b | -21.45975 | -48.51639 | 2025-06-13 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66813f41-2a2f-33f8-a301-c0b7d5db0307 | -21.34446 | -48.66946 | 2025-06-13 03:47:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e938c58-3ec0-3393-914d-d8e12ee8f16c | -28.58704 | -49.44257 | 2025-06-13 03:47:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 37116a26-ad82-3cd8-a4bf-12c2143e8147 | -15.36015 | -47.88066 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e04d439c-baed-372c-82ee-deb559fa9150 | -22.62992 | -47.35736 | 2025-06-13 03:47:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1de2cdcb-1296-3fcd-bb4e-d207e9aa7ab4 | -15.36422 | -47.87259 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833d57f5-d662-341b-9dd3-6330640b1710 | -20.10707 | -44.58327 | 2025-06-13 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76f8e3f3-4745-37ff-8814-369e8da7c208 | -21.46051 | -48.51293 | 2025-06-13 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0e209cc-5312-387e-afb0-b7d4c5076b70 | -15.36243 | -47.86937 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9451026-f580-3efe-95a3-045cb5a46c0f | -15.37074 | -47.86958 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff3b5a8c-6220-34f2-a801-74aa8cbed95a | -21.35007 | -48.59289 | 2025-06-13 03:47:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2cf4083e-b025-370f-a46b-020ca1cf4bd3 | -22.53845 | -48.8138 | 2025-06-13 03:47:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5510279e-fbe6-3f86-9a2f-988d5aaace15 | -15.07888 | -48.94661 | 2025-06-13 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e36c0793-c022-3028-b809-3bbccb46afac | -15.36499 | -47.86892 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 650678a8-c167-346e-bd57-f457ca4eecd9 | -21.34369 | -48.67299 | 2025-06-13 03:47:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef3ad7bf-aff7-379a-8d37-54e1889ebfc6 | -22.85662 | -42.97918 | 2025-06-13 03:47:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a974b46-a8c5-3b0e-aa17-1e3344343289 | -15.37148 | -47.86606 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1d5a4f7-6402-3607-b95d-14f0454dec9a | -21.34929 | -48.59647 | 2025-06-13 03:47:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 048f4f50-9976-3beb-86b2-e2d672d5df30 | -18.82345 | -47.92907 | 2025-06-13 03:47:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b98cabeb-8556-39b5-925a-0046f98b80b2 | -17.66157 | -47.45918 | 2025-06-13 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62757465-d48b-3e71-af6e-b679164e3f03 | -21.18026 | -43.98137 | 2025-06-13 03:47:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f5c0559-d72f-3cbe-b949-d4a2b49f2830 | -15.38687 | -47.87703 | 2025-06-13 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1427c475-13f8-3ae1-9c39-a2e91d19a7b2 | -22.85508 | -42.98234 | 2025-06-13 03:47:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f13662c8-2a5b-312e-a09f-d0c0164fd4a4 | -17.66224 | -47.45594 | 2025-06-13 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae29216d-476e-33ff-a8a6-45620391c8c9 | -15.93045 | -46.76565 | 2025-06-13 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec5d0cb4-108a-3be4-bc95-df74d7399be5 | -20.18031 | -40.25323 | 2025-06-13 03:47:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8a80d50-9d11-3054-99f1-524d8731046f | -17.65697 | -47.45477 | 2025-06-13 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1199a5b1-5306-3dbd-b155-781dd7d25a67 | -16.50199 | -45.0386 | 2025-06-13 03:47:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb87042d-36dc-35f4-bcd7-06cb63df6383 | -22.77013 | -49.31631 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b89d601b-795e-392e-a58b-452bff8225af | -22.77094 | -49.31275 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3ec8028-fbb5-3e96-819e-b8e903c847d3 | -22.77283 | -49.31729 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a41eeba9-a4ac-37a6-8fa1-eea8e149a00f | -22.76931 | -49.3199 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d568e36-15b3-36b7-a3eb-0047a642a982 | -22.77362 | -49.31372 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c8de45b-5da7-3eff-8309-779b3c6322ab | -25.19119 | -49.32882 | 2025-06-13 03:49:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 346d2301-0d37-3a47-81d6-5b88c3609bc9 | -22.77203 | -49.32092 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be200297-84a6-3651-a563-a5ea4e29f52e | -22.76752 | -49.31588 | 2025-06-13 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0281ddcb-9c19-3f56-a6a7-56c961a75d2d | -25.19187 | -49.32573 | 2025-06-13 03:49:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b8174dd-1dd7-395c-89f4-51477a9b6bcd | -13.9059 | -54.6291 | 2025-06-13 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d0ce6488-27e6-3f8a-8ce0-1d2e8401861a | -10.6492 | -49.4267 | 2025-06-13 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fb788c4c-403f-3423-a657-79d785816123 | -13.8867 | -54.6312 | 2025-06-13 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| fa74479b-dbd4-3f17-ae17-398e689cb554 | -11.5647 | -54.5794 | 2025-06-13 03:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a52d31ea-2e3b-3548-a1cf-874a225ac3cf | -13.8867 | -54.6312 | 2025-06-13 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e907480f-a84d-3639-9f73-5fc35b973e25 | -13.9059 | -54.6291 | 2025-06-13 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e0963afb-7002-3928-86c2-1594a1c4b5ce | -10.6492 | -49.4267 | 2025-06-13 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fcd629b3-68c4-30cc-b632-65c3376f7d74 | -10.9355 | -56.8322 | 2025-06-13 04:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e5d3f28b-a5cc-33be-af51-2ad53a01bc56 | -5.64541 | -43.60284 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 872dcd7f-f7fe-34b1-af03-061c69260cbe | -4.18989 | -38.37158 | 2025-06-13 04:08:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e8484da1-8822-39cd-a8cd-1fd5e872f953 | -5.64826 | -43.60722 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81ef03ad-575c-3b4e-9727-fb566731308f | -5.90092 | -43.45236 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c62c126-d3f4-3b6d-9f86-eaed94d570df | -6.95108 | -42.89485 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 36004c3c-2955-325d-8edf-5427fee3c03e | -4.19051 | -38.3676 | 2025-06-13 04:08:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4131ff41-c2d4-37f2-b1ef-e77de72187d8 | -6.94828 | -42.89073 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| fd5b2b2c-91cb-3ea0-99a0-94531944b9a1 | -4.89342 | -37.52565 | 2025-06-13 04:08:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 35ed1939-0a99-3621-8534-3afa77a998e2 | -6.94714 | -42.8979 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 8a47a3c8-8884-32a7-8a51-d06d3318ba50 | -6.95051 | -42.89844 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |


[Clique aqui para ver as próximas entradas](README9.md)
