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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 108a7bd5-9bd1-3dba-a65c-66f672f0b6f6 | -11.92354 | -51.06237 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a006a2da-ec7d-3899-a82f-45bb166595b7 | -17.56221 | -44.54777 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41c85f17-fd5a-36ac-a9b6-df8ca0de4afd | -15.78304 | -53.5781 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78c83d66-e1ec-3ae9-8a84-17b136421bf0 | -14.90357 | -50.11886 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0105ab9e-45d6-34bd-b23e-8dc7d6d23660 | -12.92282 | -54.7692 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab5da8af-a902-3ba8-af94-a4e2798ba5b7 | -16.03207 | -49.84233 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3355df27-ffee-3cd9-bef2-2eeacc373c3d | -19.64804 | -45.04556 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6cf1584-5815-3441-a810-738325016008 | -17.25233 | -46.08244 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b11b2fcb-644c-3d05-a029-f818f18d2e45 | -15.49021 | -49.48933 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c1b57df-d122-3ffc-a4cb-7d515ef91bba | -16.39501 | -46.8745 | 2025-09-10 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e51b7c4-51b5-33f1-9e94-17b9e1a70500 | -16.56981 | -49.73842 | 2025-09-10 04:44:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b30f091-a294-385a-8357-0bb5e23ddb7d | -15.02621 | -50.09266 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ba05a4f4-529f-32dd-a82b-0ac41f362b0f | -14.898 | -55.86128 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08e045a7-c069-3ec5-a844-5e68571b3311 | -15.10342 | -48.03146 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50cabf46-7dab-3c68-9536-70720b6b950c | -15.1344 | -52.3983 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48526c9f-3588-3a5c-a39f-ac58aee32fa7 | -15.75611 | -53.50617 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 868f0626-d240-3a4b-b635-4dfcd360f0ad | -15.47707 | -49.36439 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3179500-d870-3df8-ae72-165f599968a5 | -15.20565 | -46.24115 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16e42100-57f8-37a9-a8c1-ea74e3e3d247 | -12.9664 | -54.76293 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 122251b3-d2a6-322e-95a4-d0d4a54afbc4 | -15.03434 | -48.0983 | 2025-09-10 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da002177-ff87-329e-8f0c-9bbace82e983 | -13.90322 | -47.98213 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34cbe59e-c1e7-34cc-a4a3-2a6ad1cb7d73 | -18.03445 | -47.14956 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 748bd627-0fe0-3c21-be20-6fc469fb9683 | -15.13279 | -52.38699 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1356ffc6-b18b-3eb1-9af8-0a597c066bbf | -12.84714 | -52.94527 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c5903ca-5e7c-317a-921f-0500e2c03ecc | -13.90384 | -47.97778 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13936f40-c3db-3e49-81e5-cc9e89874c7e | -15.61139 | -52.75075 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67250662-b84a-3caf-845b-13c4f05c9bbd | -18.1424 | -51.72974 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c981508-b43a-3dce-9b5a-39c05a86749f | -16.28889 | -45.68688 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 911cc554-2e4f-336a-8ad3-eb35b534922a | -19.51956 | -45.01404 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51db8b4e-3fe8-376f-ac01-ab89c5d383d6 | -16.57327 | -49.22141 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e95378d3-9042-31f6-8aab-92167b347f8a | -17.55868 | -44.53714 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 010e4ec1-4ac4-32b7-ab08-5d4237a51c39 | -13.13146 | -54.9266 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6eb1c2f-d54c-3519-bc98-fc6a6b5b71e8 | -12.01089 | -50.98597 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1db6af72-2a1a-3e7d-8d07-634e62fa6305 | -15.23607 | -53.7579 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78978e9c-7d30-3de1-9e7d-4ad602bde40a | -14.75097 | -45.33264 | 2025-09-10 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2015f9ea-3445-34f6-8c8c-7c857af1f778 | -15.01213 | -48.01965 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff01916-d90e-383e-ac2d-d1a5ccbe2387 | -12.17974 | -50.6256 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07f8b9c6-4e1d-3020-b9bb-0aa40e910f2d | -17.33367 | -46.70915 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88439835-c02a-3fdc-a0bc-2b86550affb0 | -12.82642 | -52.9417 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e48212ee-0850-3073-bdef-d98134e0699e | -20.21913 | -40.36573 | 2025-09-10 04:44:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e731de15-2563-3b4f-99ad-2be4207d84ac | -12.61433 | -56.95955 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f7155d5-19be-3deb-bdd0-bbc5f29dc62d | -17.24804 | -46.08311 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b0c6fd9-9db8-3ab1-9d33-a0ae2363eec5 | -17.31354 | -46.73656 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2924c951-5c4d-3963-8602-1c5c59b179a3 | -13.34817 | -51.69505 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cb85feb-1197-3470-be96-4299401796f7 | -16.28514 | -45.68218 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 600caada-ebaa-3bba-91fe-1f3e23b030c6 | -13.94967 | -48.25771 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0103ac0d-7411-3eac-a245-3bdc3416cb41 | -12.99392 | -48.02032 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 584f499e-065e-3d65-8178-3875af553629 | -15.75012 | -53.52084 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c30eee0a-a1c8-35d2-a9a9-97661cedae36 | -15.02283 | -50.09211 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4c677081-083f-300c-b03c-9bf97c8392d7 | -13.94733 | -48.25908 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2137ecd-888b-38b1-9037-59ab02bc1176 | -12.17697 | -50.62153 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a258f295-a492-38f5-9ad7-5bdef2a7a7c4 | -13.12475 | -54.92053 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d32a785-9892-3af5-91bb-5a7c54adf970 | -14.24346 | -46.69265 | 2025-09-10 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1e0969b-d032-38b6-8441-7334c9f30fa1 | -15.10501 | -50.07841 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 903a0ca5-e2fe-3e3b-9951-14dc35c1462a | -16.58029 | -49.2226 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d6c7340-65cd-3eac-83c2-4dcb5569a31c | -14.88532 | -55.8623 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc3a8d9b-34c7-3ef9-b459-6e782c468dea | -16.32154 | -52.92103 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c0c0c6-9acf-3552-88e9-2b93bb3a8e1f | -12.60928 | -56.96289 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da54618-bc36-3c26-9950-3321c6ea4b8b | -16.73779 | -43.78771 | 2025-09-10 04:44:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 830c0fd4-70d1-3811-ae29-350cb237488c | -17.25227 | -46.08369 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 891ccb14-7154-3e99-a73c-cadec70fda62 | -15.80483 | -52.24681 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7ac89a1-dd84-30bb-aecb-8fba9a45ca11 | -15.13718 | -52.40242 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d5ee9ec0-3cfc-3bf4-966a-0f33d179bab9 | -15.94273 | -50.22865 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e3586d-2243-3ac5-b50d-3eb5bf6f4e2b | -15.80701 | -52.2546 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b7324a7-67dd-35ef-ae1a-8d9e3eee3966 | -13.17915 | -47.25792 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6781f3dd-223a-3c38-b278-f3396964e6f9 | -15.25344 | -53.78846 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 871d654e-d6ac-33cc-82e0-408741d070d0 | -15.96021 | -50.22775 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db321e76-ccad-3da6-b754-ca72242dcf8e | -15.80715 | -52.23235 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de27d8f7-d8b1-3cd4-b603-6cdbae18f404 | -14.32495 | -47.31234 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a009efc-4a24-33da-9770-7f0cfe77610b | -17.30612 | -46.76174 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ce1519-d193-3a5f-8708-c8ad5e672abb | -14.8971 | -55.86628 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 751e4283-0a38-342c-89b1-7b28b20905d2 | -13.43818 | -51.83125 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47b5e756-744c-30a6-b40c-8e8076e1c931 | -12.18171 | -50.62632 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f007c9f-4b95-3d98-a7d6-da79185e4159 | -15.85772 | -51.83004 | 2025-09-10 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91aaf156-f4d6-3318-92e7-454798114479 | -16.67355 | -49.39648 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd150ab0-00d3-3a07-bc7e-e7ff410c0b88 | -12.9945 | -48.01637 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08a0f4cc-533d-3b35-b249-d511396c3437 | -15.51787 | -48.37875 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a26481c6-7501-364f-b318-7ede0506e8c6 | -17.30852 | -46.74333 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f3971e5-bd97-320d-92d0-a3da4c9d27f7 | -18.69158 | -52.59399 | 2025-09-10 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2af9c956-a122-37cf-9f09-80625d5401c6 | -15.22886 | -48.24284 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06995428-e037-3a99-881c-2ab3f67fe685 | -16.88334 | -45.74908 | 2025-09-10 04:44:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0628fc02-04b9-381f-8d6b-2763af6643d2 | -18.34181 | -49.33954 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac8f33f-80cc-3ad6-8359-1b1b0a04d989 | -15.03498 | -48.09392 | 2025-09-10 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce56fe1-e1c0-32db-b60d-993b6104dfc3 | -17.30854 | -46.67945 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b3ff469-6c69-3c4a-b5ac-abf75fb0571f | -15.51427 | -48.37809 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d819836f-f992-37aa-82be-b599d114cea6 | -15.11012 | -50.0904 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1f18aff9-961b-3958-8f3b-5b3ef46d968b | -14.92833 | -50.11523 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb18b811-88a6-32d2-82c1-61270e19bf35 | -16.28086 | -45.68156 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a97880f8-e428-373a-a497-e484b449036a | -15.33265 | -52.89737 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b1d0b09-9857-3fcf-9a39-3f07f157fb4e | -13.00146 | -45.20575 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad8473b-59c9-36f7-b7b0-40b7e0c1a592 | -17.56396 | -44.53283 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 413896a8-977e-3fab-bee8-7cfd65037e92 | -18.44014 | -45.93588 | 2025-09-10 04:44:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6af15aed-38af-3494-97d5-09e10194246d | -14.38225 | -47.31514 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a0bb29-0540-3ae8-8a26-46cdd39f4ced | -17.20574 | -50.17126 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29a34426-60c0-33a1-af25-2f5a05a72be4 | -15.80933 | -52.24015 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b41411a8-9ee7-3279-96f2-d8b41c5aa5e3 | -15.08362 | -50.08236 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a290761-7e3d-3a4c-a37b-4e0914bd20dc | -13.90992 | -47.96114 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3774552f-dd52-3e1b-81da-38210a5ae903 | -19.28691 | -47.98288 | 2025-09-10 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 554d4ed8-fc58-3e16-9a97-fbd4d77355de | -13.05488 | -42.32419 | 2025-09-10 04:44:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aea3b4c1-eb4c-3f14-b2da-cb86b1cb2e89 | -15.95345 | -50.2266 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README79.md)
