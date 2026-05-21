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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48905d4e-e05b-327f-ac7b-fd3c24ac0146 | -9.73691 | -37.24463 | 2026-05-21 03:32:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7d074fc-64ff-3a57-99d6-48c4ae615e89 | -12.2322 | -44.26149 | 2026-05-21 03:32:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f20a9a5-b2d1-35c1-a257-b8b8ddb2ed2f | -10.65251 | -42.30413 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 507a9980-e22d-3264-9b97-1c12c8e5b062 | -14.90346 | -47.75401 | 2026-05-21 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 694bed13-6d1a-3b75-ac2b-d74d5a01fa88 | -10.65108 | -42.29761 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 864965e2-cf63-3016-bc3c-6ec64c1e8daa | -14.63289 | -48.03516 | 2026-05-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09fdc17f-0f39-33dc-8430-0a54fe2105cd | -9.30273 | -45.49386 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 5b370b2d-2077-3768-b3d6-d298ac54a452 | -9.29929 | -45.49266 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 4042674c-6fc9-371c-b586-03ebac1ff0f5 | -8.54836 | -45.985 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 35b999ac-6d51-3300-8ac0-7c8dc8d8cfd1 | -9.62041 | -40.34626 | 2026-05-21 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 17df2187-bb28-3579-ae76-d70a37b80c9b | -8.62662 | -45.9854 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38c1f968-4740-3020-a8a9-675e7d85cd8d | -15.06986 | -42.37788 | 2026-05-21 03:32:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c342a0b1-5a98-3a80-a8cf-f5a59f085ed8 | -14.01609 | -47.50703 | 2026-05-21 03:32:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2efb7e4-6921-30be-8434-0a8c81ec1010 | -9.29492 | -45.47943 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| af929e95-1686-3408-9f54-e2fbd7573135 | -15.07044 | -42.37484 | 2026-05-21 03:32:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66a4168c-53df-3448-ba0f-e88193bae798 | -9.29843 | -45.4807 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 7e569938-d152-3695-bd61-d7a18b52d263 | -10.65314 | -42.30068 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a090fa6-d158-3fde-addc-6fac858550cd | -10.64715 | -42.30311 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06fddadd-ee62-3766-b6a0-9412cbbf7af0 | -9.30592 | -45.49413 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c7111b95-5994-3088-878b-af419e8e33d8 | -9.3039 | -45.488 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 7bdc727d-c0f5-3d82-830b-c2399c836b58 | -14.62646 | -48.03101 | 2026-05-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 915c32c4-b955-3bfe-b66e-659173f69772 | -8.55336 | -45.99208 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0ad7ccd7-80e3-3016-a56a-29c05c09bd60 | -10.64441 | -42.30349 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49600e35-7ca8-3351-8667-3f68906d9891 | -9.29379 | -45.48532 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 499a626a-e250-3019-bf97-9db64af36d8e | -9.2961 | -45.49243 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 0ad8a318-518d-3098-92c9-387b9f919227 | -11.99711 | -45.14156 | 2026-05-21 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbc9da44-4643-3257-84f6-8210cd8ad1c2 | -8.6171 | -45.9974 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71d44a4f-196b-315f-bbef-b6a357cdd1e4 | -10.65187 | -42.30758 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24228ee8-3bf7-38a7-9289-71a4b5d2d14a | -10.64779 | -42.29966 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2f7c26d-cb7b-3568-b8fe-3d889d3da48d | -8.56152 | -45.98725 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c5b32b86-f868-3ce5-8550-48903c932fac | -9.32894 | -40.21129 | 2026-05-21 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 249fde83-f502-3c98-b4cd-9221b405cd04 | -9.30705 | -45.48825 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ce3947bb-48bf-32d0-9fab-baa043fefddb | -8.56217 | -45.98805 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bce99604-7838-3b82-87e1-aee077ae9b55 | -10.64243 | -42.29866 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d2b0f2a-e9b0-3469-a8fc-28b4d30d656f | -14.63219 | -48.02607 | 2026-05-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca73e2f3-5d67-3f6f-9444-816a1656dce1 | -16.35589 | -43.87585 | 2026-05-21 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69310d2c-e5b0-33f0-9544-c557509d4dcb | -16.35496 | -43.88037 | 2026-05-21 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00a1b398-9a8f-3153-8057-1413c57b6ccb | -18.90684 | -41.94067 | 2026-05-21 03:34:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ebe4c0f8-4a9c-3f53-a77b-4303260efba6 | -27.6109 | -49.94277 | 2026-05-21 03:36:00 | NOAA-21 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a527d9c-dcf3-36f3-8fcd-95ee8681f850 | -27.61064 | -49.94461 | 2026-05-21 03:36:00 | NOAA-21 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 05948b0a-fcbb-3fbe-90b4-b632b3c9796f | -9.3045 | -45.4809 | 2026-05-21 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 9455c146-3368-3622-bc44-f76a317cfc5a | -9.3041 | -45.5036 | 2026-05-21 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 8c9183b2-159c-3f5d-bdd0-23bdec276996 | -9.3045 | -45.4809 | 2026-05-21 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| cbbc58c7-9c7e-3b2a-8ac0-2083d9ca17db | -9.3041 | -45.5036 | 2026-05-21 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 58a58d90-b55d-355f-80d4-f96b323c2a30 | -9.3045 | -45.4809 | 2026-05-21 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| acacb7c1-5d1d-35f3-aaf2-549529351778 | -3.61547 | -41.81818 | 2026-05-21 04:02:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 966706cc-81c9-3d7a-9224-251396fe082b | -6.39267 | -44.16619 | 2026-05-21 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 803d3360-73e1-3796-aeeb-f89bec2b301d | -9.31112 | -45.49374 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59f907e6-39be-3090-bf68-6382bf2d4220 | -9.30312 | -45.48783 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 222e478e-5961-33fc-b2b6-da490bfcfa49 | -9.62199 | -40.34482 | 2026-05-21 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d0f4f69-d563-319b-abbb-4469dc2d7aa6 | -4.36231 | -37.89654 | 2026-05-21 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7016f313-6994-3e44-a187-bf59bf38c8b0 | -6.29857 | -43.63685 | 2026-05-21 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4899efc1-5c40-39ac-b10f-4a3a87cd5ae3 | -4.47577 | -37.82219 | 2026-05-21 04:04:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b69c72a-5422-3711-9169-67348500d638 | -8.54963 | -45.98419 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 297cda9f-a45e-3315-8bfd-7ad7cd80244e | -5.75102 | -43.40848 | 2026-05-21 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae5fb42e-6738-37e4-9ff5-a808a4eb1deb | -10.65036 | -42.30497 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49eed01c-a69b-3894-9466-b2b344b1d837 | -5.02429 | -37.04293 | 2026-05-21 04:04:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1a257c63-31b4-35e3-8740-8e06f26d892e | -8.32681 | -48.01023 | 2026-05-21 04:04:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0cc8368-170a-3946-b33f-e741a91af451 | -9.30749 | -45.48867 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f04ed40b-5de0-310b-a70c-4178ea0c53f1 | -10.65391 | -42.30558 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 203a4328-e0ea-3a0e-8f6c-c96ea51bc695 | -7.05423 | -45.06364 | 2026-05-21 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a78fc91b-a4ad-3e85-bf9a-d7a62b2a5a33 | -8.60619 | -45.95279 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cab879f-3c89-3c04-aa87-861a56223c98 | -9.71471 | -50.41648 | 2026-05-21 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0171210b-7117-3b32-b782-92e2ce980831 | -9.29513 | -45.48193 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 867eb81d-6cd0-36c9-8da1-e4c773bae024 | -10.09295 | -46.54396 | 2026-05-21 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0702f930-d494-3996-8b4d-a962e2760ef3 | -4.36564 | -37.89706 | 2026-05-21 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5b13152c-8f42-36b9-9be8-c57468e3e0f7 | -10.64495 | -42.30108 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7577389-307e-31fa-b8e6-47713ed979ed | -8.61693 | -45.99815 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 526cd73c-867a-34e9-9177-ddac8a42cd9f | -9.71381 | -50.42103 | 2026-05-21 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe8ac2e0-d69c-314f-a629-7b4789bf8303 | -5.34591 | -42.68867 | 2026-05-21 04:04:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 244094a8-e67b-37c0-abcc-439f927b2e4a | -6.39203 | -44.17003 | 2026-05-21 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 976bbc90-0d0d-38d8-870b-3b8e7dab7f52 | -8.61234 | -45.99734 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1554877-54ac-364f-a987-16ff2daf59d4 | -9.2995 | -45.48276 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99dffcbf-5bd1-32a9-9ea7-7f7573415a32 | -10.64393 | -42.29969 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac152715-f83d-3859-a6f0-08955ff7fdb7 | -7.04983 | -45.06282 | 2026-05-21 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 462520a7-690a-3bf7-a0a3-468b93224cdd | -10.64562 | -42.29702 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2704face-288f-33c8-ab91-66880db86816 | -5.95284 | -43.49366 | 2026-05-21 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c71d82b9-570b-3522-bc42-315af6bd5153 | -8.32097 | -48.01244 | 2026-05-21 04:04:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73a69e02-4981-30a7-b0c5-c469214223ba | -5.94879 | -43.49298 | 2026-05-21 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2423918d-9723-3b5a-ac89-732df51fff0a | -7.82563 | -42.06035 | 2026-05-21 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3570ab7e-345a-308b-a7ca-bd41d68aa956 | -6.39687 | -44.16693 | 2026-05-21 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 204b14f7-bc8d-3882-9641-600a46dd417f | -9.06052 | -47.63668 | 2026-05-21 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62a47ade-d974-3a23-a11b-31c1686b3687 | -10.64429 | -42.30515 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6161c2d3-2750-38e6-9ff2-7cc8732b5fa5 | -10.64324 | -42.30375 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a7c5997-b47c-300c-8904-7bd836989cf2 | -9.29076 | -45.48109 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5f5bda9-8830-3efd-b1dc-b1e72e93e4bf | -9.29801 | -45.49123 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 85e53f73-7a3a-372f-b453-ac40371dc426 | -8.55797 | -45.99059 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 588ce525-09e0-3f8e-b358-da79c0e19192 | -9.29876 | -45.48699 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2fdf22e9-acba-3875-bb76-bce716253933 | -8.55339 | -45.98967 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8f10189d-4c42-35da-9365-c60e59fe666a | -8.60194 | -45.95511 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f40b9e46-58fc-3d23-8512-c43b0410e94c | -4.47741 | -37.8118 | 2026-05-21 04:04:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b1d344a-a543-3ec5-ac39-82542ed5d4e8 | -4.65729 | -42.42104 | 2026-05-21 04:04:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b147bf15-ebed-35b9-9daf-c0274da7bfc9 | -5.75507 | -43.40911 | 2026-05-21 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa2ea89b-3d6f-30d3-b993-10bfe2f9fc22 | -6.30264 | -43.63754 | 2026-05-21 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ded5c3da-1c1c-353b-8095-5aef97c5d17f | -9.93545 | -48.01231 | 2026-05-21 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a796839-9737-38e9-817e-4379a0fe046b | -9.62257 | -40.34124 | 2026-05-21 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 509d6d90-b0cf-3d39-bd86-924ec9370726 | -9.93489 | -48.01534 | 2026-05-21 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ce2358-1f67-3776-8f63-90e4ca36fa0c | -10.64818 | -42.29625 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 654d8593-3239-3f1a-9a20-d6e64c129bce | -5.30512 | -43.06086 | 2026-05-21 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29e388fd-b993-3609-8b61-b641a8d9ec35 | -9.29439 | -45.48616 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README4.md)
