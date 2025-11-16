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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcfc6c74-02a7-30fc-837d-1820dbf745e2 | -6.11334 | -41.51938 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64ae1dcf-88c6-3748-ad2a-09a7df704111 | -12.39846 | -47.56141 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb460d05-12f1-3828-99f4-6ecf676600cf | -6.07475 | -42.87249 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 4aa482fb-5499-3720-b405-b1a5307e09d8 | -8.26244 | -40.98158 | 2025-11-16 04:08:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0fb6926e-3255-33a0-916e-fefb7f9285c2 | -5.64386 | -47.74525 | 2025-11-16 04:08:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9a13a869-3312-3efb-b756-77371d11294a | -11.96269 | -44.3462 | 2025-11-16 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3335371-bd63-3bd5-bcf3-76551dfa0760 | -11.81054 | -44.20773 | 2025-11-16 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4fea0b1a-516b-3793-bf52-26a3b7949a7e | -8.58764 | -46.05772 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2894bc10-4e4c-3ff9-97c5-0fb2dcd46181 | -7.12964 | -41.66665 | 2025-11-16 04:08:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d47488f8-f28d-33e4-a583-417dca25af94 | -7.05179 | -39.62461 | 2025-11-16 04:08:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03ca64a8-5707-31e3-8762-0b5424f4097f | -8.06503 | -45.65772 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad27bffd-e8f3-3dfc-8619-09e0451d5a50 | -12.21712 | -49.55038 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 237de7c4-0acd-39c3-8377-c2026cd8ecf5 | -8.2114 | -42.85639 | 2025-11-16 04:08:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 66898a90-14d1-33c4-94d5-c140e59b99a2 | -12.40304 | -47.55947 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12ba2f7f-c11f-3006-868e-d18cdb100c31 | -6.30393 | -43.79867 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c4e52f31-f96d-342c-a1cb-d61c8576bb6a | -11.16365 | -47.45734 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cda3f33e-1d07-38ec-8d84-4a35f6d528b7 | -6.10511 | -40.37887 | 2025-11-16 04:08:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5dbf80ca-c831-3a4f-851b-f4bc0519743b | -12.65542 | -46.74749 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ce96fbd-4816-35c3-8a0c-4dfa0342f3a3 | -7.3479 | -43.33767 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10c6e922-e727-3c68-a762-49ad60260324 | -5.99732 | -41.90806 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 083e698f-c7d9-3efc-89b0-58f75e371bcf | -8.21887 | -45.98731 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc602ffa-4a16-3aac-9fc1-f5947d062981 | -5.6066 | -46.37051 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d29c970-b407-3ffc-940e-3c1c00f3a44f | -12.00816 | -49.27945 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 68d974cc-dea7-3378-981c-417b48a32ae7 | -5.83088 | -43.82411 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfd2a3d1-231f-3bc0-87d7-ddb890ecd613 | -10.93187 | -48.69561 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecafd806-5185-3e2d-b076-397abafb7c82 | -5.72413 | -42.91608 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ab5070a-f5bc-3d8a-bbfb-f8bc69555c17 | -10.54624 | -47.99973 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b372dae8-d7b4-32aa-bb51-8a697f78220c | -9.15111 | -48.0546 | 2025-11-16 04:08:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31fa9de4-e121-3a40-9c1b-a36111717b00 | -12.40873 | -47.5501 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd981fd9-68c7-3427-a80c-3145f0f01980 | -6.36124 | -46.15952 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6862606-8935-39ce-a958-800a51330cff | -11.79015 | -45.53376 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0baff7c8-79c6-3684-8149-929ea0dce977 | -10.00418 | -44.77777 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb5839a4-aaf1-3b3a-b32d-b7620ca5470a | -11.80575 | -45.54891 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b5302a2-7684-3ca0-8953-e8dcb5b38bec | -9.74289 | -43.94784 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9af4239-a713-39c2-90fb-28b0f234c496 | -9.85844 | -44.16798 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28eaec46-1543-3045-a06b-c8a03a00b52a | -6.13105 | -48.04731 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a242603f-2b83-3df1-a2e8-03075f0047d8 | -10.73065 | -45.16567 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 550aa60b-235d-33eb-88d5-a51f6be2cef1 | -12.52649 | -43.35326 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0f4b8ce-8cee-37db-8ac8-128d3729e8a5 | -6.55029 | -43.47109 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6f42c51-5027-3332-9165-1b61c0c391ef | -11.70642 | -48.86548 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23be16f3-1948-3047-98bd-e56d7e13bd7f | -11.08491 | -44.82175 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae1ef2b8-517f-3f79-94be-97c2729db40f | -5.4235 | -44.63411 | 2025-11-16 04:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c23dcc65-277f-309e-90d6-5818d86ef154 | -10.167 | -44.49216 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04b46efc-5708-3b95-a7b8-8c3fba3efd26 | -6.39177 | -46.00199 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa336cb-c712-308a-9818-4750ba6c8888 | -12.68545 | -46.79485 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48e5d84b-1c61-3106-9f05-f959f87b5fc1 | -6.95267 | -39.56308 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce5ed846-5313-3ba5-8a5e-d2ba079b92da | -7.19559 | -39.21158 | 2025-11-16 04:08:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf935731-b7f9-350e-99ca-e3bb4cc43453 | -11.36053 | -49.7966 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f25d048-ceff-3ab9-beb8-ade2aa8e8e42 | -7.41021 | -40.06926 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 341e0546-d786-3148-94ba-7f585e2ffef6 | -11.16058 | -47.45155 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf565d2-7b76-38b0-96a1-07148940854f | -11.30355 | -48.51375 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c664f75-1208-3e5a-b83a-ad6ff72ba201 | -9.95033 | -44.92977 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96768ebe-d8fb-3f3e-8a59-241fbcf5aac6 | -12.39759 | -47.56646 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 414122c5-7943-3109-996d-1660d4db3e6a | -5.96221 | -43.75025 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed9f26b5-c8e2-3b32-827c-7fabecc66df3 | -11.70789 | -48.85721 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3139537a-abe3-39f8-b711-6eda8cde3282 | -7.11088 | -42.72718 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 433dcc97-38dd-33b3-98bf-5599bc4e1963 | -6.32731 | -46.3363 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 614e65c0-d5b1-38cf-b690-887b6373480d | -5.96567 | -43.75084 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 303f740d-8ba9-3510-9cf1-84a055d80380 | -10.05087 | -46.76676 | 2025-11-16 04:08:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc385d2d-1120-3e38-a234-998e67cf7a48 | -10.24761 | -45.06214 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb1e9549-ef33-3571-b83c-bfeae4544f65 | -11.80154 | -45.55235 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a98620ef-fa9c-3c99-b44c-60759d0b37d7 | -6.08457 | -41.61366 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 588bba22-b45b-34ef-bf29-676ee6a8320a | -12.29176 | -47.00275 | 2025-11-16 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84f45df0-1e00-3c69-89c0-949755b24743 | -7.2627 | -48.02679 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6ffab44-f0a3-3056-a7ad-8e18edaff243 | -6.62108 | -41.46534 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bce5d92d-30e0-3fad-8c98-1f8618bce68c | -6.60367 | -41.2963 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e43b413-c0a6-3950-ae30-c5c04d1bd5dd | -9.05854 | -44.75055 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b5fb8500-caac-3dcc-b185-1d1fa4e9b07f | -10.70214 | -44.52386 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ee696d7-b155-3b0f-b0db-4d4f3c1f8246 | -6.46461 | -42.00355 | 2025-11-16 04:08:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1084c693-77ee-3c7e-8412-d29080ac8a58 | -9.10863 | -40.46309 | 2025-11-16 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01ff33af-787e-3086-afef-8a68206991b5 | -5.60601 | -46.37408 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a5e0346-8d0d-3d0e-a7cf-8c85b5b6d1f1 | -10.2511 | -45.06287 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0255db9c-6324-3ec5-b7d7-dd48011584d7 | -6.51161 | -47.63103 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d618d86-3ec1-34a0-a52b-9ed4507a8576 | -6.72631 | -42.94273 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 8c89ee88-4b8b-3cec-a00d-3287f3ecddbc | -6.85784 | -42.84253 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 01940f92-0cb3-3e17-893d-057f2358e6c6 | -10.9155 | -44.84491 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 458a72bc-d589-35aa-aaa9-d7597f5d342e | -13.06389 | -43.24253 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea631e36-2aec-311a-baff-12319fcd66ee | -10.16109 | -44.50666 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 367633b7-6ea8-3735-beb1-53c7d6ee71f5 | -4.30929 | -50.87219 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cae9b4f-d0f8-38c8-ba45-f31f9d82035f | -6.85449 | -42.84203 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5b014cd2-6cdb-3c70-a50c-5e04055b32f4 | -6.87948 | -41.59482 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d27170f8-2148-3c37-acb1-21677fe21db6 | -10.66628 | -49.3581 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c1a06172-ad0d-328a-b75f-a0eecebfca54 | -6.78109 | -43.54208 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdd07cad-158a-365b-b002-89e641969cec | -12.0628 | -48.22179 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b31d7d96-d350-3b96-9c16-ee35c7f6f7be | -9.06269 | -44.7472 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2fc0cff-217e-366b-ab32-159d90494f36 | -10.6639 | -44.80035 | 2025-11-16 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8324e5e3-6c5a-3ef5-b1fd-235a77ecb6ed | -7.91786 | -47.1033 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c79529d-ebb4-336d-814b-c234a4118026 | -12.06818 | -48.21512 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96c3b4af-fb65-3212-adab-5c4793aaf055 | -11.71144 | -48.8622 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2fbd92f2-bde9-3641-879e-59daefe33eb6 | -6.67831 | -42.04856 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0375444f-86f7-3d6b-92c7-8ce076666ace | -5.49109 | -48.00214 | 2025-11-16 04:08:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d31b853a-780b-37cd-adfd-e6cc164e4fa6 | -9.66028 | -43.9001 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d9b480e-7068-321e-b833-69efc4108701 | -6.00725 | -41.90963 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8c08a23-8d80-3524-bfc5-5cd8f35175b3 | -6.29614 | -41.84529 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06ac9653-c5d4-3ffe-9a18-72b38dc54572 | -8.32108 | -45.40783 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21c15c12-8fab-3dc5-9f97-0eb58e0249f9 | -10.31734 | -44.57879 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bcb986f-4de1-3b41-a687-bd9e4a1e3631 | -5.9896 | -41.91393 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 069997be-453a-3e40-bc04-a6134bdf5c60 | -6.70345 | -44.14685 | 2025-11-16 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f60bb423-0189-37d3-8a61-7571ee5fefcb | -4.81109 | -48.34304 | 2025-11-16 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e12a477a-b7c7-306c-9829-9d87a39606ce | -11.05118 | -45.15657 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
