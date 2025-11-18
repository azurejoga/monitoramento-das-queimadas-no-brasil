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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd4d209-57c5-303e-b7bf-92305fe181e3 | -5.39571 | -44.46399 | 2025-11-18 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0edfe092-bf8f-3e28-a627-678ae3ed2be2 | -9.04642 | -45.43641 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dff2ef22-adad-351a-a160-2f310cce2d48 | -10.51607 | -43.95391 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9cf3f43-2b11-30a8-b424-9b6ab48a17b2 | -3.33672 | -50.27612 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 519a8449-be8f-3931-95b2-d2c752151555 | -3.14744 | -51.32583 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74f9d1dc-7417-357f-8a5c-4216da1f77e7 | -8.47073 | -47.97755 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4273397e-9851-36c0-a2c3-4ac708f42a36 | -4.17793 | -44.24315 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f91d539-c0be-3b94-947a-c74f199f9a60 | -3.6671 | -50.21654 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa6d7536-d80b-3805-95b8-f42fcf254dc4 | -3.939 | -52.1795 | 2025-11-18 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43108f1e-66b2-3579-bc84-102c7591a353 | -4.17624 | -44.23232 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 75899076-44fc-3366-b6ae-2e28ec3bfdf6 | -3.65872 | -51.77954 | 2025-11-18 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d854409-cf13-31ce-8e84-6b6f6391702f | -9.39901 | -48.44931 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 980b13e6-9bd9-3fec-b347-3a99960641ba | -5.25843 | -44.88093 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b3db256-f637-3add-b4ef-1024ff712ee1 | -7.87088 | -45.68291 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab56c628-0ae8-364c-9184-9988ce3f6d3f | -9.50648 | -47.46537 | 2025-11-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dca85849-fb4a-320b-91a7-0be809562f6f | -3.59944 | -50.71902 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fefeb410-b35c-3b8e-88c5-c623ed88ba82 | -7.57383 | -46.28986 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a744852f-78c6-3a3b-86cb-3a24d918ea27 | -5.4676 | -40.96488 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e33cea72-1e41-354a-93aa-dba915cf7fc2 | -3.64632 | -50.8377 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d8b3500-bf8f-34e1-b3cb-7c77fdc16222 | -3.08332 | -51.26508 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cd6c2e1-5032-3bf3-b231-acbc1e8a36bd | -7.62883 | -42.58192 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6e7e494a-8fbe-3709-bfc0-8f29ea5a045e | -4.22814 | -46.34588 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2baa516b-280c-3a35-abb1-80b42bfe3921 | -3.67478 | -50.25228 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e74b8ef-7487-3545-9643-a4e0ac0b3eba | -7.02524 | -39.3658 | 2025-11-18 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2dae7c5d-866f-37fb-b58c-a98d323a689b | -4.4061 | -45.82954 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44106e0a-d20b-38bf-966b-e383b484f299 | -6.68017 | -43.77225 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38301491-edf4-3e28-860e-8848db547c24 | -7.22307 | -48.46703 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7072511a-1c0e-3508-a01d-9ff445960d2c | -6.09238 | -41.66313 | 2025-11-18 04:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1f2c6500-4fe1-3e0b-b253-f540bc25d9b7 | -4.40443 | -45.83314 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f875558-3468-3ded-86a9-f7318650fdfe | -11.39596 | -43.32082 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4c4d27b-1cc6-31f4-9193-f79206245de6 | -6.88028 | -44.60361 | 2025-11-18 04:21:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8fc65316-6c67-3015-93bd-86d3c1ce09f9 | -10.84364 | -44.87918 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 458a3f1f-c336-34cb-a5a2-3fa4f75da8f1 | -12.30359 | -40.21629 | 2025-11-18 04:21:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 068ae183-5d21-31b1-b516-f20c43e835f8 | -5.51145 | -44.3981 | 2025-11-18 04:21:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a2fcd5e-bb8a-3cf5-9e4d-73f6a3ca3b2e | -10.51213 | -43.95705 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ef84a9a-8a01-3f89-a7c0-83234c1bc848 | -6.2212 | -46.88185 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05d94374-2010-37df-9b3d-5e8a596f3551 | -6.11553 | -46.18785 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad2674d2-9c2f-3fc7-a7a4-7a2838b759e7 | -6.34724 | -41.748 | 2025-11-18 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4c795384-db49-3b4c-8893-76eadc17f7dc | -3.93853 | -52.18228 | 2025-11-18 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d62f6c7-f714-38e2-9265-6576ff644421 | -8.79724 | -44.39385 | 2025-11-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59006396-cb23-3f4c-bf6f-bdb3f95b3b2c | -3.19277 | -50.64944 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb350411-a855-33c3-8fb2-3ccf1f9dc332 | -4.17954 | -44.23283 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 78178534-0108-3fef-8707-5eb71f19b340 | -4.34093 | -50.6805 | 2025-11-18 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 755fcfad-84f6-3cd8-927a-2fcedaf94f58 | -10.54589 | -47.77036 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a352ccac-db10-3f45-b507-ccf98488f8ec | -6.71182 | -40.79227 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d62d6f94-4010-353c-a0fa-098c8753b982 | -7.06269 | -41.5857 | 2025-11-18 04:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85634a77-0163-3102-bd0a-80bbe60d61c7 | -6.94061 | -49.66392 | 2025-11-18 04:21:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2145439c-5929-354b-b097-14259fbf0e94 | -7.43778 | -45.19207 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f5c72e-843a-3200-ab42-e7cd6fc0b18c | -9.88 | -44.18562 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66cd297a-a472-3727-bab0-e461f519512f | -6.13361 | -44.35474 | 2025-11-18 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40cc1248-cd96-3033-9465-4f1ad3f62174 | -8.4073 | -44.03399 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6163d091-bc4d-3000-b6ce-b69af427a50b | -5.49685 | -41.38902 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cfdab305-4b97-363e-9b95-edf4e5db397e | -7.08071 | -52.61877 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1794ed3-3033-3574-8acf-a60818981c9d | -3.4994 | -50.44147 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b85ad12e-aea3-35ca-bb22-e1b9032cca89 | -7.54044 | -47.0465 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39deb5eb-e6da-336c-bae7-49d40b7fa319 | -4.02591 | -45.54807 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce8b9c11-009e-30dc-add5-deab52c00ffe | -3.75609 | -50.94376 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d771ca3c-ad55-3c92-b381-8d6c21fdae4e | -9.72116 | -49.13474 | 2025-11-18 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e06e09fa-2b05-32b6-8634-daceb895e685 | -4.6428 | -45.52684 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cabbd94-23e5-3ca8-af2d-a52c3cd805cb | -4.64 | -45.52282 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c54c84-dbf0-3314-af07-35d8a489625b | -9.6101 | -44.37018 | 2025-11-18 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 39e2cf91-4b37-3152-8e13-2abf0d60a49f | -8.0873 | -46.05363 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd5c1eb6-44cb-33db-a3cb-5597edf4703a | -9.39541 | -48.44872 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fab839c7-5d73-3164-bd9d-d858785abcb8 | -4.64325 | -45.65507 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 757704f2-3dcb-36bf-9e3a-0006d426aeb0 | -8.01016 | -46.5756 | 2025-11-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 561e0415-b20a-334f-86de-91668f5d2a46 | -3.08806 | -51.26584 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c97a081-0929-3118-a4b1-d6108db92170 | -8.54061 | -46.05024 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1baa0c13-557c-321a-8765-58e200d0d92e | -4.64335 | -45.52333 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23440efe-d964-3478-abb0-4947449cde13 | -5.96838 | -44.12743 | 2025-11-18 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4628fd3a-68a0-32d5-9990-43f110dca63e | -4.17516 | -44.2392 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aabef783-c520-34ac-988c-61cddc6bb24d | -11.39654 | -43.31691 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 632e46ad-e75b-33a5-8083-cfb571f9aa34 | -10.38596 | -47.50313 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6848fc2d-c456-3793-bd5b-f9d1bd290b5a | -10.50593 | -43.95233 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 337a502e-e6c7-3f58-a06f-5da42ebb8aad | -3.67215 | -50.21305 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48104dde-50d9-30a2-ae39-f00c0af50254 | -9.73282 | -43.9422 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4a61ee0d-108b-35e7-82eb-b4086c782b69 | -7.45471 | -46.88136 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 088d6098-4139-3b01-9110-9b2cf0b042c6 | -6.09005 | -41.65448 | 2025-11-18 04:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bf8d0d24-278f-3818-b832-4242efccaa7f | -7.48055 | -44.00475 | 2025-11-18 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aac2b9d-77f7-3502-8dbf-7d5f703dc6b0 | -10.3618 | -48.91762 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92153749-b259-3fc3-ba3d-d4760077b068 | -6.71048 | -40.79376 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 89590210-930a-30d9-9659-5f3bbdd6eea0 | -3.77908 | -50.1391 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75b9aae-ebfd-378f-a519-1aad1b73d7c5 | -11.43039 | -43.31692 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f82ab8da-1ebe-384f-81a0-a343a1b93b7b | -2.34125 | -55.79663 | 2025-11-18 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cd5ad22-446f-3f6c-8b61-e515f10570d6 | -11.57082 | -42.41693 | 2025-11-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| afe9f45a-48d4-3974-acb1-8e0549e7537c | -8.54395 | -46.05074 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c6da93f-5d95-321c-967b-ac9c94888452 | -4.4257 | -45.54449 | 2025-11-18 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40f17cc1-5ef8-32f6-bd0f-1d3bfb235514 | -5.95595 | -45.3553 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 501933a5-9f25-3af5-adaf-7aeae9080e2c | -5.87352 | -48.24513 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333f9e56-4ddf-3e71-8f3d-d7fe4836c9d6 | -6.20953 | -46.88792 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 536d3153-b958-3164-ae92-1b72098732f0 | -8.29945 | -44.00632 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 635a54fd-08f8-3272-9efe-9ab7c8501b5d | -3.83642 | -52.29876 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 060ac16f-e8a2-3dfc-b6d3-ea7bbdb118ed | -6.21363 | -46.88462 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53acdb99-ac83-3e2b-b4f3-6dc5a72385d7 | -8.57872 | -46.4922 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f19257f8-7026-362e-8560-5311d2e6bd4a | -4.14178 | -46.76461 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a77d7a2-2778-33e9-8b86-9cd3e99f850e | -3.2357 | -50.5031 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e87898-6241-342e-8cf7-100273be5b63 | -7.10438 | -46.5244 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 048b8b1a-ac27-3a61-98df-231ebebb889c | -9.39181 | -48.44813 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ff14a07b-8b76-319a-8756-7e5c1f224625 | -5.12958 | -46.13736 | 2025-11-18 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc370635-79fd-3319-8156-928a21f4a321 | -3.15528 | -51.48762 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 780a93e7-bc6c-3d63-b623-0c4dc3b102cd | -6.62003 | -41.4697 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README26.md)
