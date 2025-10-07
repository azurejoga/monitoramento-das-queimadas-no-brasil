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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fb1e8d5-8c1b-3c95-9df5-86fe9e63d2a1 | -9.33766 | -54.52011 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0e9a84-460a-3e45-ad03-74d670d422c8 | -9.18548 | -47.83517 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e4a8d339-8d2e-3c8a-ae61-9560f72fd362 | -5.39087 | -40.98539 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 24f2807b-8a59-32e2-bd82-f615a7010869 | -7.46734 | -42.61707 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d37f0e4b-0f36-3706-8dfb-8cbacb4a0de9 | -8.18451 | -50.30033 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aed3fe4d-d8ea-3a5f-be59-8be9892a4a1a | -5.59552 | -43.10691 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| abb7ded9-5dfc-3eef-bc4b-e209352e2ecc | -10.18574 | -45.53498 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0e8fabb-8845-3859-b832-70916e041c59 | -5.83387 | -44.98068 | 2025-10-07 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bb5da1e-3d8a-32f5-86da-2bfd8c238189 | -10.27029 | -44.37697 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05d0b939-2ed0-3607-94d1-6829c7512178 | -8.53238 | -54.86042 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 306797f0-9f81-38fd-9b9a-0621b671a9fa | -5.79823 | -45.21512 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e74d35b1-2e15-3778-9a90-0278f210ef06 | -8.16748 | -50.16616 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5851e557-0843-3030-8761-42927045f5ef | -8.17211 | -50.15936 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b469b46-1ed1-3f87-a674-d138af8e62d8 | -7.78543 | -42.61352 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c0d84375-9768-3c70-8d29-bb004590b097 | -8.17068 | -43.33184 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ef6e202-23fc-38f2-9f9c-a406236e8a8f | -8.53117 | -54.85852 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 746e58ea-34f6-3805-aa53-56312cd80e46 | -5.65566 | -43.18447 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e10fd89-3f85-3a17-8d75-b9dbaee2ac73 | -7.70544 | -42.3911 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 051e572c-14a7-317f-afd6-f670895ce7f9 | -9.18438 | -47.84223 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38bdcf81-7335-3ba6-92dc-8a20421c651c | -5.2469 | -46.55276 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 813c6ea2-b2f0-334d-aade-cf7b876856c7 | -10.25792 | -44.38007 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec264290-cc34-3a7b-a9cd-3d6c4a37f189 | -9.78501 | -48.28314 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab96a355-4226-39db-9882-398deca3a447 | -4.69207 | -48.62266 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4557a451-5a0c-3e12-9c14-dbd6d3028502 | -7.03041 | -42.75477 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33ba145a-088d-38a5-b5af-d1435e09e823 | -8.20228 | -44.17861 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23d7305f-9208-369f-bb99-5c0193d1c838 | -6.64983 | -41.97228 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e17c1b8-6013-3207-923f-dd6bea87e829 | -6.28238 | -42.9436 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1a46f73-b799-339f-ab8d-e710101d6660 | -5.49215 | -43.47409 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03d17374-bd86-3527-b28a-fc1731dd2bbb | -6.72569 | -42.82992 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8def6e03-adb4-3d9c-b61b-3d8fca30773b | -7.67935 | -50.20901 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f509fc5b-e5a5-3f9d-9eba-c96a902308a7 | -9.05807 | -51.35646 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b627a7eb-de80-3e8d-a5ce-f63cc070f8d0 | -5.21434 | -43.67566 | 2025-10-07 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32d8dca1-ef39-3a77-8280-610de7517843 | -9.69029 | -48.39418 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13b888bc-8345-3a62-8c9b-38ec0731e390 | -9.09425 | -44.39989 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24e8760b-f3cb-3f8e-b0b7-7ce0c8b64c79 | -5.6518 | -43.1874 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8dca946b-3e75-39d2-a153-1d5158593655 | -4.68803 | -45.8414 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 214fd1cb-768c-3a5a-b36f-e60e7d29e7ad | -8.87492 | -47.68131 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34eceb03-0043-31b2-9638-257b6b46cd50 | -10.15822 | -45.42313 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86798d28-a17d-3ec9-9012-1c27e79b2e28 | -10.39417 | -45.37924 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f49ac35a-529d-3f7a-ad18-61dec211f94a | -5.75948 | -43.39743 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| adb5538b-0759-31a1-bfad-0cd6bca1637d | -8.20405 | -44.19335 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c382a53a-501f-3cf1-be30-c91310e2a354 | -8.20131 | -44.21225 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b986c8f0-0df8-3f7d-b412-491a1daae019 | -8.95932 | -50.79541 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d76b51e-2b12-3e62-b028-0b16f91531a7 | -8.87541 | -46.7741 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8de33db-4dc8-358a-9d11-824244cf261b | -9.03176 | -50.59105 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6104d9a8-655f-3107-8ee6-c7c0f48babc9 | -6.71022 | -42.85003 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 720aba99-1553-3e11-9ab1-1eddade3625d | -8.26915 | -43.82601 | 2025-10-07 04:36:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 665bd9d2-1f78-3ee9-bfe7-bd254e747db8 | -9.92002 | -49.96018 | 2025-10-07 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0efe14fb-28b5-3f46-bc20-e2975b62475f | -7.80033 | -44.14233 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c65c9418-8cd2-34b8-a2b7-fc77521199a2 | -4.69087 | -45.84554 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f8595185-48ea-3f85-8827-c423fc1f97da | -6.4542 | -42.79431 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 934a04fb-8a55-3857-9f64-6a7991c1930a | -8.48536 | -46.29477 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8418bc95-99a5-3c4a-86de-8097872cf525 | -5.49769 | -43.07014 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bae886c5-5b07-38e1-bc70-b018593052a8 | -4.68834 | -49.49734 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c92c684-fd1a-312b-8059-14150da9e038 | -6.5283 | -55.04103 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 741c2049-ae87-3220-b05d-674674f57a09 | -8.49917 | -46.32011 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8cdcad9-8af8-3a17-80e5-f24ea0c47142 | -8.48941 | -46.29145 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74bf370d-53f8-3690-a121-0ef0f6b5cf87 | -7.68935 | -42.41272 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2a4b3073-b4bc-3de0-8401-d1ffa3fcb1a2 | -6.66969 | -46.53653 | 2025-10-07 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18c3ef28-4dec-31fb-a3f6-8e4eee73be9b | -8.61957 | -54.96748 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e098ca-ff81-34e4-943d-e48deeea56f0 | -9.51655 | -51.35836 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ff54c84-291d-3268-aec8-fefba1a7e9fa | -7.02379 | -42.29424 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f614dc67-f001-366a-b74c-687a035fbabf | -5.39021 | -40.98981 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0a23a367-4117-30d6-b327-92de1baf340a | -5.25732 | -49.86398 | 2025-10-07 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdcfebc9-df98-34fe-b31b-d88f74310552 | -6.29094 | -42.94146 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2368a5d1-fd24-33cb-9a0d-9b5da0db3550 | -8.20062 | -44.21696 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c944829e-c17c-3a52-a160-d1e2032f8c17 | -4.2254 | -47.20957 | 2025-10-07 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6eee9463-c6b4-3c01-b461-e1858e932ff7 | -10.41187 | -45.38675 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 125ea97d-aa4a-3369-a605-7d4c89a2e98f | -7.67885 | -42.57942 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ddddfaa8-2a3a-3a51-b279-08939d4de279 | -9.32236 | -49.80796 | 2025-10-07 04:36:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1b75934-5ae3-34e0-9e20-6d1622ec9eb9 | -6.98556 | -42.86729 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6535f29b-3d2d-3c15-b87b-5df126a3e8ff | -5.73979 | -42.53247 | 2025-10-07 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8187c85f-cee8-3f98-92ae-38b233385013 | -8.17966 | -43.35485 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 481d3d4b-c3ca-38b8-9e7c-c552996a4fc9 | -5.59701 | -44.42839 | 2025-10-07 04:36:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f18a16cc-1f49-3732-b671-3dda0e1594b4 | -10.4021 | -45.37636 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b13801ec-1cc3-3dee-85f4-ae37d0824c3e | -8.61785 | -44.93088 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f77e4dc9-2eef-38ef-9e7d-ae46c8048320 | -6.72515 | -42.83353 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1d5517b-7a74-37f6-bce3-c474fcce5c7d | -5.4231 | -46.00066 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee88ea7b-5c0e-390f-a093-cf9f4ef80ffc | -9.13488 | -50.69759 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbec6bfd-d423-3cdb-aa38-40c1d77a3a7c | -6.72106 | -42.833 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 543f25df-c8dd-3cca-a370-c08460f25f59 | -9.57906 | -50.8046 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01bb598-d87f-350f-bf9d-2c138f9292df | -5.59477 | -43.11195 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ed41166-3844-38f8-a41b-d40e76deed2b | -4.6886 | -45.83775 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 90e863da-4dfd-37e2-a9cb-b7a8f6d00ffd | -8.19857 | -44.23109 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 13bcab22-f88d-32bc-af3a-486ec4d0936e | -8.41364 | -46.80592 | 2025-10-07 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce896f68-99f7-30ef-a671-5241aeb754c8 | -7.517 | -49.91087 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bb83c28-6b07-36fe-8ee8-b6a2ce89b181 | -7.68457 | -42.59966 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9c471bd-2123-3e53-b3e0-7f3c111ad193 | -4.68746 | -45.84503 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 627e704b-f8ec-3024-a4b8-18f75101d753 | -3.81343 | -51.07355 | 2025-10-07 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1bf520-a35c-3b54-b408-b866629b872c | -5.85077 | -44.30198 | 2025-10-07 04:36:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c376ec8b-1541-3db6-94a2-5e7d2fd0effb | -9.01396 | -47.83326 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 743656bd-d046-35e2-881e-c8f6d8aa84a7 | -7.47571 | -42.61836 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0daf8e38-71ca-31e6-98a6-a4744ba795f4 | -7.69785 | -42.41407 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6d7bcb3-358e-3b73-a3a2-6a90e7653058 | -5.48433 | -43.07845 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 512e36bd-26c3-37e5-8346-10a9262ead0c | -8.30491 | -47.59254 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc45f79-e797-3167-b17a-cdfda5c1dbb0 | -3.94772 | -55.7837 | 2025-10-07 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffd5ea3d-781b-3cf1-9af0-1a4ca72f807a | -5.33849 | -43.38459 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5c8066e-dde6-397d-9596-7e34617b053e | -6.69738 | -42.85236 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0a3caa5-eadf-32b1-9482-b9451a0f9515 | -9.18493 | -47.8387 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dbb8f42-ab5d-3c4b-95ef-a3bcbf014a45 | -7.68361 | -42.57614 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README56.md)
