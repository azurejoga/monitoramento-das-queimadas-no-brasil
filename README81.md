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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865d7937-de44-3b81-b1ec-64cb842bdd92 | -9.3461 | -45.7261 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9ebd1ad-7c2e-3d46-a264-ff92506b3465 | -13.55401 | -47.24949 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d25875a-ab6e-3e35-acd2-e4ece1fd3e0b | -8.5526 | -44.79717 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4215ec8-d787-3577-acaf-d21562ffc3f5 | -9.76704 | -46.21161 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dffc9e5f-84de-3edb-bdb7-02cb94ee0964 | -10.01537 | -48.27323 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4cdfbae-959f-328d-ba2b-5a36495b1b65 | -12.92281 | -47.80777 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68ec47b2-b0d1-3692-9948-b633c7405260 | -12.52942 | -45.9813 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2794a762-64b9-3044-97b2-40cbe8b69e05 | -12.07373 | -47.9959 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cd0d16d-fc61-37e8-a604-b2b01270d7d7 | -12.93736 | -46.37956 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9803e3cd-f88c-33d7-bb6f-9852c993fab7 | -14.3037 | -43.86183 | 2025-10-04 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f90c8c0-f772-384b-a8d6-b77ef8f4be88 | -15.29696 | -46.2922 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d4c416b-285c-3da3-a4df-e232419cadd8 | -13.13195 | -47.81391 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d33e1a1e-da23-3de3-9375-bdb4a3f40200 | -14.74438 | -48.08385 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc39164b-533b-300c-b578-0717bd110dfa | -9.94821 | -43.7333 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 526aec31-ce9a-394e-a51d-2969970b9ea7 | -14.23802 | -46.08227 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdf0e463-6344-32c4-ac23-a7ffe8b75b70 | -13.73811 | -47.95751 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9039be96-0f9f-30a8-a17e-8299945c0ac0 | -11.48089 | -45.03077 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc25f73c-9528-3b6e-8f25-d9e32814df78 | -11.70075 | -47.51305 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ecb2538-9f32-3e28-a5d5-1c8f9748fcfa | -13.6709 | -47.30945 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f2ec443-d2a0-3606-81a8-ff2fd54d957a | -11.14514 | -43.37476 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69ffcafb-7286-3344-91e0-a640d31f1710 | -14.88428 | -48.27727 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4b40826-bfdd-3fe0-b73d-8b81faa203b5 | -13.10739 | -47.89196 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc23b862-ceb0-3218-af6b-0253b9684380 | -14.8661 | -48.11747 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fad7b887-dcb3-3a04-acae-079c4338c888 | -9.35148 | -45.80136 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dc14cc8-d0ff-37f9-95dd-18b61727dcf5 | -10.81831 | -46.58323 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77464d2e-dc28-3f8e-bc7f-8d0577811966 | -9.34583 | -45.79261 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49bc6a45-0a04-3798-864c-176fc33b59d1 | -13.13415 | -47.82284 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbdcb1a3-2a97-38d4-b83b-82b150a0245d | -9.75375 | -43.60965 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aab02f3a-4ded-3f77-84eb-b2eb38e5f007 | -9.33605 | -45.65831 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7e9a880-5ef4-3bda-9695-0b487448d88a | -11.92124 | -46.36708 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c4ccc6f-94ca-399b-8386-312c30650da1 | -10.7421 | -44.70268 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 171e6bf2-28ba-3fcf-a0f6-4605f5615f57 | -13.38553 | -47.28014 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d60e30-fdc8-3316-98a8-2345e4747d52 | -12.68943 | -47.56415 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab32639e-4629-3d4c-9d77-f947741253eb | -11.0868 | -47.88605 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c9df6dc-f51c-38a2-ac29-29ea32654bcd | -12.36311 | -54.17048 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 167af164-5f36-3880-b458-dbb1229d9ab9 | -13.25438 | -47.24097 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 488a54e7-72f6-3694-bc11-18bde2737893 | -14.24236 | -46.10952 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2c33ac1-84ce-3f01-bb27-db28c01c9372 | -14.93021 | -46.91424 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b35d0f0-f170-3113-af3a-962270b3540d | -11.11228 | -47.87984 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33a74352-bc47-350e-9375-9fb076ea1004 | -10.01926 | -48.27384 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89729a8b-bab3-3c70-9965-0ef8429e39ab | -8.81647 | -44.82087 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| feb5c321-990c-3dfc-b98e-9d9cea6a0625 | -12.08153 | -45.16645 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4423d16e-6f28-3903-942d-c463968d1bb8 | -9.90673 | -43.73803 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a8bb659-c5ea-3798-93d5-d446163db703 | -8.53275 | -47.21594 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23951e9f-dd57-3d78-b88f-62ae30b64c40 | -14.60343 | -46.7262 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a9f4f41-f150-3faa-9ebd-b923d871707f | -11.91004 | -46.34943 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbb17f6d-3531-3295-8c9b-9d064ef2dbdf | -9.95152 | -43.73383 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d8a6d46-aa0c-3bfe-987b-cf3892616d28 | -13.59461 | -48.17915 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf4c94d7-5daf-311e-80a7-81b109e893c1 | -8.55318 | -44.79355 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4efce9c1-0590-32d0-9703-d4473468dab0 | -13.98918 | -48.19844 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ad0fbd6-38db-3461-a92e-c4a548bf70d5 | -15.32669 | -46.38449 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29eaefaa-8ade-3086-a81d-553d3abb9766 | -12.65002 | -46.994 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d40a8c-9548-3ed2-91ad-d4557d30ae98 | -13.74328 | -47.92749 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60b05c52-4079-3eb2-b2c1-ee61d63150e5 | -8.39513 | -44.0162 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5e0f9b9-5d19-3eeb-9490-96c7e7b8fe79 | -13.30538 | -48.13859 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65306757-3255-3169-af59-d8ae20ea7975 | -11.45245 | -44.95699 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d13b64-9397-3096-a662-2a6d4bc16071 | -9.33202 | -54.51352 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ecf8ca9-b4f1-3bfc-b4d1-bf831231f0d2 | -13.99721 | -48.19553 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe7ab847-f72a-3769-93b5-8b8c4f2dc2e4 | -11.91842 | -46.36276 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eed2c598-a38e-3a06-9c1a-1a9eb8e8340f | -12.08042 | -47.99037 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d423f11-0c58-3667-9345-9cf86e7ae784 | -13.28704 | -46.98067 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6276e236-744d-3adf-ba93-eff111b93bd5 | -12.38007 | -54.46589 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6aebc4a-c76a-3d47-bda8-8db41a160015 | -9.33078 | -45.75487 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 857a06eb-6286-3be9-8aa1-32ba702aec52 | -12.71088 | -48.5676 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b615d229-3561-3a64-8f9b-8c7b0283f09f | -12.93176 | -46.37098 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72fcea0c-c6a8-397a-9578-cb0360578f26 | -11.91625 | -46.35457 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99985c25-0ef5-3817-9860-585bc0156e35 | -12.0364 | -45.19188 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d1cf18-6707-3c7d-9fb4-f3e9516efa17 | -14.44807 | -46.10704 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe37120-ef62-310d-82a3-018bfe52a222 | -14.2145 | -46.07845 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3491edca-aede-3f09-a06a-3cc40b7ebb9b | -13.74613 | -47.93253 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52411e85-9848-30ac-962a-c4418e573cb4 | -11.52575 | -47.30256 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74283ac2-dba7-3de8-bf86-7f1c187cde8c | -11.73607 | -54.72406 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4389fcec-4f4f-3ea7-95e5-6c8af933d0d4 | -14.02279 | -47.97926 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4cb8160-9f18-378d-aef9-ced57a6b6e23 | -8.61213 | -54.9758 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5dbcb36-a872-3837-8a68-76df05539ea5 | -13.72885 | -47.92484 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e6bb1d5-23c0-3b03-a83c-789484f098b2 | -14.72599 | -50.04028 | 2025-10-04 04:14:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 204cd9b4-e21a-3966-97bc-9dc0cd971d71 | -14.85008 | -48.28066 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b21e7675-6a11-309a-b088-ec90e8d64d1e | -11.12896 | -47.84996 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84c39281-5bb1-3b93-8ef4-b5f88b6fa258 | -13.28916 | -47.18388 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cebdbb00-ac36-326e-a97b-5d2d8b6ca008 | -12.03134 | -45.20203 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 211629d6-1de6-3ca5-a425-b060bca1a679 | -14.66397 | -48.31326 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 46d4904d-5895-3ea6-af93-36f55b8db14a | -10.61374 | -48.72953 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fe9639d-7b66-3bd4-8397-cc6e887c2202 | -9.93581 | -43.5747 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae462e52-3535-358f-acc9-2f72b653bc3f | -13.32912 | -48.08797 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3119eb7-19fe-3bd6-bcad-8a8b44532610 | -13.70468 | -47.34647 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9888079f-d913-313b-84c8-b729714ee92f | -15.75365 | -43.67168 | 2025-10-04 04:14:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f591821c-5bfe-3586-93a3-7983d0a11a90 | -10.32629 | -50.33735 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83295621-2161-38f4-bd97-738c9d04b539 | -13.68782 | -48.02971 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a4a10c-62da-3c1b-ae6a-43b0593251da | -10.27648 | -44.34204 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb31bd49-dd07-3036-88d8-8a475807ef0a | -14.74565 | -48.14178 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ca1ec4a-2503-3960-9286-3655eaf6fbc0 | -13.76682 | -48.05148 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb65be3-398f-34e4-940f-81cbef1943ab | -11.11131 | -47.90028 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 279490d6-3813-320e-8269-c60a9ae8f465 | -11.11784 | -44.90219 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3830380-5727-361b-adf4-0c49e63ceab5 | -9.93192 | -50.23768 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15cf3b0b-358d-3221-ab99-f3a121f52a9a | -13.39158 | -47.2886 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86b7ba21-dde5-3e38-976b-8abe54475dd7 | -8.5504 | -44.78936 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30d4e890-4f89-3b7f-a751-fb91003c1624 | -14.28729 | -47.4196 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9b86b0-8639-3774-b16f-85f59fd9332d | -14.88766 | -48.30087 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 983e5d67-7db5-3595-869a-42140e8a2687 | -8.19453 | -47.00227 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ed7c557-18cd-3244-9de1-792efb6749a7 | -13.57544 | -48.18074 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README82.md)
