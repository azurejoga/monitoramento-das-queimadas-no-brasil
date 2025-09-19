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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1a875cf-dcc8-3768-98bc-edc0e13fc2bc | -17.09032 | -43.34266 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9f015eb7-0ea5-346a-ac7f-60e59a802c3e | -14.83554 | -60.23863 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1296dcc6-7861-373d-95c9-82bc6695b379 | -17.45955 | -44.79707 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b4feec1-fa77-34e9-8e65-afe4d025c6fa | -12.91851 | -50.5661 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83fcfd1f-5c42-333e-bc89-957a7e405e5b | -15.41862 | -58.77723 | 2025-09-19 04:49:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0b7acfd-5ef6-3410-8ca3-503884f8f654 | -17.46106 | -44.78292 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1deb5cc4-4fa1-36ce-918c-ca8f0aacbc97 | -15.33224 | -59.40791 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b51bb29e-e454-3d7f-b64a-10ff6ec709e5 | -15.8196 | -59.46019 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8018861-bab7-3500-8213-b949e3b891aa | -15.79519 | -59.40634 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55865677-d21a-3f9b-bfbb-d140ab38c6c2 | -15.79807 | -43.81116 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7eda5828-0143-3e9a-acba-5955d8f1a24c | -14.83464 | -60.24335 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cecb274-72cb-3e3a-9d2f-2d1471d61be7 | -17.21657 | -45.94516 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a54b9f-8c0a-394d-b1f7-c6ffcb2115fc | -17.45739 | -44.79592 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241b672b-6670-3741-9253-f353cf5b8cab | -14.75878 | -60.19234 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b550421c-e472-3c55-86be-fab65098bd21 | -16.69032 | -54.9576 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6361f4bf-0387-3392-9458-0b816f96dc56 | -16.68573 | -54.96453 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49e33abc-2ed6-3c0d-816f-1ed6410883aa | -18.63102 | -43.91121 | 2025-09-19 04:49:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aeda3c99-6347-35b6-8960-78f629eca650 | -11.8214 | -57.63325 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70d98a0e-914e-3d9f-becf-90325dc8725d | -12.93394 | -50.55677 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae5259c1-f72b-38f6-97eb-2033c64c5290 | -15.79945 | -59.40704 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b8467a7-553f-349b-8c33-a9e83713cd8c | -17.09278 | -43.33821 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35d46d31-4b52-33bd-99da-b85136e31100 | -17.22546 | -45.95182 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0edc1e13-13ae-31cc-a5d3-9ee8b3080105 | -12.92994 | -50.56006 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df61981d-0e99-3f79-8978-6e8c400e3a40 | -14.26161 | -44.70116 | 2025-09-19 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad1ec45c-c9fb-3951-83fe-6b37f2f34d24 | -13.95973 | -44.54037 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d941875-7aef-3968-960a-ded3b88a78d1 | -13.96337 | -44.5471 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd3a8a7e-3c2d-34fd-8204-347e796a8649 | -15.80026 | -59.40261 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 931d2503-8203-338e-a528-9fb4a190940d | -15.81596 | -59.46096 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89ffb4d6-be81-3d40-970b-52f9d3f85902 | -12.87904 | -50.54826 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dc0a7bc-8567-309d-a12f-afc554aeb938 | -12.92536 | -50.54372 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f47ce650-ccc4-3483-b52d-1fa7d0dbcb01 | -17.06417 | -45.91221 | 2025-09-19 04:49:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cff3d3ff-de9b-346e-8649-26f29b137393 | -15.00195 | -55.32582 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 224cfd3b-722c-324b-ad90-70dfe446e00a | -17.08547 | -43.33432 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e488ce93-9b0f-3353-b194-17cec9105ba5 | -16.6897 | -54.96139 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ddb1891-92a9-3789-acfb-273639bdf817 | -15.79847 | -43.80762 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 860593c6-06fd-3af4-a1fa-56d2d37b6194 | -18.95885 | -42.07673 | 2025-09-19 04:49:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a1fe12ee-2b9e-38f0-a2e5-f0f5bb728b8d | -15.78133 | -59.38638 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 111ef855-fc76-3ce0-a24e-b388adf31b6b | -15.70481 | -41.75356 | 2025-09-19 04:49:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e664b48f-6351-371c-8d5c-ca51ebe74564 | -18.63069 | -43.91254 | 2025-09-19 04:49:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c22608-9af1-332b-af49-1f85e6b27353 | -17.46141 | -44.77958 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 878ecbe0-776a-3049-b4d2-e58cc071bae0 | -14.75953 | -60.18837 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 828915c9-8644-3da8-a9fb-483b81bc0278 | -17.08678 | -43.34103 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab829f53-a1b6-3e17-8ce2-1c6019ea523d | -16.69397 | -54.97765 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf4b74f-6795-3873-bcb4-1b75f395bde9 | -15.00216 | -55.34602 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2362929-3b32-3387-a56b-4690c97bc094 | -17.22071 | -45.9512 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1429209-a25f-304f-9f5b-0dc095bdb7d6 | -17.08638 | -43.34471 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1eaa068-6073-3550-badd-6af86162b27d | -17.08718 | -43.33732 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2c58351b-5fdd-33f8-bbe0-2be8cc3c76b5 | -17.08585 | -43.33052 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a522ba8e-2da3-337a-bb3e-0051b7e72580 | -17.457 | -44.79934 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e431289d-d203-39bb-bd31-39a8f49a1ffb | -17.09916 | -55.51029 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a624c263-4313-3bfd-b619-5a3e11bfe416 | -14.82726 | -60.23256 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24ec9372-fcd1-3923-90df-267bc89a16ed | -15.78706 | -59.3791 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32107161-77e6-3828-8b4b-b3e6d72e5220 | -15.78207 | -59.38238 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecef57b3-6ae3-3c2f-bafb-1d6d10e9624a | -17.0907 | -43.33889 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bdce8115-120f-3f7e-838e-5dc3052c116c | -14.2599 | -44.70659 | 2025-09-19 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d211e74c-f893-3aac-9b39-dd8ed8d72b0c | -13.95837 | -44.54648 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd24d520-df94-30ba-8365-0569be82d133 | -19.00844 | -47.89203 | 2025-09-19 04:49:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf462b4d-97fb-3cde-b796-84f5a5222936 | -17.16176 | -44.78639 | 2025-09-19 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0218b5f1-528b-3f5b-9a34-ac65a1ad6cb7 | -12.92537 | -50.56716 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4fe5994-2ee3-38f4-9e5c-49557a0539e9 | -11.8099 | -57.62754 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71cb3618-b5bc-3862-bdac-476ec0b03add | -17.093 | -55.50526 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ff3aa499-edc2-3da4-9e10-6140aa339eef | -15.02761 | -55.33807 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c73185b0-97dc-3739-ad93-446cd68ea389 | -13.95909 | -44.5407 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4163ed6d-e2f6-3f33-8412-c65a49b3c3ec | -16.68696 | -54.95698 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9da6a15a-46d4-300d-b218-79a3c23a3d3b | -17.16655 | -44.79015 | 2025-09-19 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5393532c-6ecf-3a79-a8b7-f758f294a782 | -16.69457 | -54.97392 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be2a422-b3a1-335d-8f00-3f9ca76df28a | -15.03512 | -55.33547 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fef2344-129b-3d51-b94b-436b0ca4120d | -16.51518 | -43.55193 | 2025-09-19 04:49:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c05967c2-acb1-39a7-9f04-ceec965b3be8 | -15.8153 | -59.45962 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d61e05f0-c996-3761-a544-3c59aa1be40d | -19.12836 | -46.62453 | 2025-09-19 04:49:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc1a68e0-e47b-3926-8ee6-3ddb6c25cbca | -15.78053 | -59.3907 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 338da5f2-0c53-3b7c-a706-65a0918b1107 | -17.16621 | -44.79326 | 2025-09-19 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a594046f-3b0b-358b-9756-aafdabd6fa58 | -14.82912 | -60.24756 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc946f47-e43d-3f13-bdf3-bda44ba0aae7 | -17.22961 | -45.95766 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02f9ba3e-974b-3a0d-a524-4398a80d0090 | -15.78746 | -59.40066 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc3935b0-a755-3825-a08e-582fc2ac73a3 | -14.82641 | -60.237 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4ef5393-145c-389c-970d-c1611516d7fe | -17.088 | -43.32982 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfdcd71-c403-330c-b65f-3fa986c8231a | -15.28268 | -56.83368 | 2025-09-19 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86792a82-33fc-3ebd-9626-083cc81bfa26 | -15.0056 | -55.34665 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d681588-25f9-311e-9e4b-a47529a0104b | -17.09364 | -55.50143 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 79492ff8-009e-37d4-b797-89e63e78d780 | -17.2048 | -45.95391 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c1055fe-b48d-3c5b-83df-85e587e9eaae | -16.68847 | -54.96896 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aabaaacb-71c8-3f4b-ae3b-01efa5ed5d15 | -15.3365 | -59.40881 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e972aa1-107e-3722-95bd-dff307e79a65 | -17.0964 | -55.50586 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 68819e3a-5384-3df4-925a-63d372e5d2a1 | -17.46622 | -44.78349 | 2025-09-19 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15a89842-c6bc-34d2-ba41-093e8a10ef5f | -17.16109 | -44.79258 | 2025-09-19 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21170925-4461-3ab6-8f2a-f1ae33d87774 | -15.27826 | -56.83744 | 2025-09-19 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df0351f3-64bb-3dbb-9665-4ea4e1acf5f4 | -11.81394 | -57.62827 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33abec32-0fd0-3c2a-9e1a-390e967b8537 | -17.20006 | -45.95325 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0fdbf7f-06cb-3ed2-b605-015aef121ae2 | -15.79866 | -59.41135 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f98db294-61d2-3e11-9bac-ba6e12082a9f | -13.96405 | -44.5468 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30cebed-23d0-3b91-94d0-075d74e440c8 | -15.01352 | -55.32002 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 206e3e6c-4517-31cd-bb92-8fa8064415b4 | -17.09236 | -55.50908 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 00bb5489-30fe-3d05-aa5b-fa72db136e80 | -11.81735 | -57.63258 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1073a945-453c-324f-b9ab-09b79a9b36ed | -17.09576 | -55.50969 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9a26da41-b84b-3306-9bcd-59a678b56ed3 | -15.279 | -56.83311 | 2025-09-19 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c8bfde1-af85-37a8-a68f-8c67943747a4 | -19.00792 | -47.89625 | 2025-09-19 04:49:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 928d3ec9-c952-387c-8f65-2e8a779185a1 | -15.00282 | -55.34201 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad0b6ff5-2159-3efa-8c05-7b7ccc699f6c | -16.68908 | -54.96518 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63d0d91f-c366-3f84-ba6c-87f2d14d34d8 | -14.18648 | -51.39149 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
