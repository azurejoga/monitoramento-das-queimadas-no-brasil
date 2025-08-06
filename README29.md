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
| b244284d-d845-38c8-a7fd-edbb124dfe0d | -8.9023 | -60.55324 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0ba1e3c5-e1a8-3e08-8471-c981f0578dd1 | -8.90384 | -60.5856 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 688d2e18-c12d-3979-a4b1-f66166874972 | -8.9163 | -60.57915 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 77c01b50-9b68-3c73-bb91-6a75d98b7bed | -9.47404 | -57.85162 | 2025-08-06 06:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7be7c638-9206-39c1-b413-fc0afcbe666b | -8.92 | -60.74938 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88248471-db8e-319f-b240-90ab3d232c4f | -8.91425 | -60.55083 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3ead98c6-89e6-373f-9df7-494c271dcf11 | -8.91987 | -60.59586 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa4428ee-8bf1-3606-8739-3fe6b8ddfc35 | -8.91852 | -60.76094 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a989da13-991f-315c-bc98-bb491575fac4 | -8.90075 | -60.56499 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8d7f578a-c169-3b9d-b05b-177462e6cc56 | -8.92147 | -60.58387 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6616f91-93bb-3816-8536-1707836eab58 | -8.91951 | -60.75322 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c494acec-864f-36f5-b5a2-2cdaa895cf3c | -8.90795 | -60.59836 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 612112bc-39ad-3774-8a35-59c0722bd3bf | -8.9132 | -60.55875 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 612e080d-9afc-3bdd-b079-1607e5319930 | -8.90697 | -60.56191 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9a116ba2-141e-3cd1-b0bf-69d78447070d | -8.91682 | -60.57519 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 697c77f8-be68-392a-a4d4-aafacc74dcff | -8.92409 | -60.56425 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74de3edf-7a66-3794-9e03-187642c6ccd9 | -8.90279 | -60.59356 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3ae5f367-40a8-387e-9f65-8af321ae890b | -12.43617 | -63.69984 | 2025-08-06 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42750ff9-09f9-365e-a33c-694b4a55aa1f | -9.18513 | -60.83452 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6acd19-29ac-31a9-b9c7-cde56002c280 | -8.91112 | -60.57442 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f0e820a-32e0-3613-a96e-360f0987894e | -8.91803 | -60.76481 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4202b9f-13e6-33b4-8bbb-d40db7ef4d68 | -8.90436 | -60.58163 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6eaded5b-e716-3b5b-a053-7ead6816aadc | -8.91252 | -60.73695 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dde70745-05a7-3b93-bcdf-d7b750c40b71 | -8.91417 | -60.59517 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cff1dc60-ba9d-3200-bd55-e355a6a22abf | -8.90178 | -60.55717 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 324cd4cd-db36-395b-bc52-400b5a9b316d | -8.91786 | -60.56737 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4358f9d5-8840-3fea-b42c-f164eac6d96b | -8.91483 | -60.74495 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50718414-7b74-3923-9e58-1d3c24dac51b | -8.90127 | -60.56109 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 98419694-098b-31c7-a3cf-caa571dfd5dc | -8.91561 | -60.75667 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 464e25e4-2d36-3571-af32-ee4f5c4a3298 | -8.92253 | -60.57594 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67a34484-9335-35df-8b79-9bbbe6728a61 | -8.91509 | -60.76053 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12c786ee-580d-37f8-9c3c-e6b1d9e5a790 | -8.91201 | -60.74078 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 405e0299-c0c7-37d9-b038-87b2ac81ccbb | -8.92357 | -60.56814 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8885bc45-8cff-3b38-b400-f5c5fed81f91 | -8.92517 | -60.57209 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eedf206-7419-32a5-ae23-4243bfbdb609 | -9.70263 | -61.29854 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2544a0d-32c6-358e-9fba-d06f3e5a2db8 | -8.91754 | -60.76866 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650369d8-72ce-3fae-8568-2ce7807937e0 | -8.90646 | -60.56578 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 901ae6fb-cbe3-3cb6-bb95-7488b57f25b7 | -8.91434 | -60.74878 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c301210f-8ace-3269-bd7b-fdc9f10d7bd5 | -8.91405 | -60.76817 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fedb6f1d-5e1e-3889-b231-47d9cd6b0b66 | -8.9158 | -60.73729 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a33d6b7b-eba5-3348-a8fc-ac1854f4600d | -8.92216 | -60.59594 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ef75cd1-496e-3df0-b924-53c9d580fd52 | -8.91007 | -60.58239 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 11a868bb-b038-3a31-8792-7002a2a6f016 | -8.91524 | -60.5871 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 7a930145-5fc6-342d-86e1-74fa2e1bafb5 | -8.90543 | -60.57359 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2e31d6f9-d7f5-3e33-8858-67616da5f136 | -8.921 | -60.54377 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8abf00e4-bbf0-345b-be92-6ad13a657192 | -8.91881 | -60.60383 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fce95197-fb4a-3433-b358-085298a6e048 | -8.92503 | -60.60064 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4988fd17-a785-3af9-8ac4-95db8f49fc07 | -8.92049 | -60.74558 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0bf56ce-b7d0-3c0d-be3f-12f01437ff50 | -8.90853 | -60.55006 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2b9ea680-e3b1-35ab-bc41-6677ca9e5c20 | -8.92267 | -60.59194 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3f37ff8-20c1-32ca-a59c-46b9b5a697c3 | -8.91577 | -60.58313 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18e0d339-87fd-36eb-a0c1-4c6af06e3d19 | -8.92166 | -60.59995 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04621761-bfda-3a73-a9e4-7478b67e7f3f | -8.91261 | -60.60692 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f15f2d2d-f6c9-3572-8fd5-5a9fe116ca7b | -8.92317 | -60.58794 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1fbc8cf-a3b6-3043-b1c8-f40adbf30510 | -8.90749 | -60.55797 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0f0ed1c9-294f-3bcd-914f-4fabf6693e80 | -8.91239 | -60.76412 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df37aa3-7a45-3579-b42c-c8c53ed72dae | -8.92041 | -60.59187 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aba0fa39-3b55-3f8d-8160-010a4f4a5eff | -9.70217 | -61.30216 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5db0c792-aa39-38d8-931b-9bd0ef304567 | -8.90957 | -60.54224 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 986eb171-ab24-3382-a003-befb38720740 | -9.4665 | -57.85704 | 2025-08-06 06:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7a1dceb-78e6-3b01-96ae-552e02239084 | -8.90801 | -60.554 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| da0ed81d-5a24-397b-a602-9f545ed7665d | -8.90905 | -60.54613 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 031245d7-4928-3ae3-9433-4895b7558b15 | -8.92305 | -60.57204 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57694deb-8fb3-388f-9924-f824369f0615 | -8.91312 | -60.60304 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7b0d20c1-be8f-3d3d-bcce-6e425ae4fbcc | -8.90742 | -60.60231 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 501fe98a-439d-3a1b-b86c-47154546a963 | -9.70737 | -61.3007 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cab8a58-7312-3997-b86c-ae5d58875d6b | -8.92566 | -60.56818 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d595df-7d20-398a-b339-ac56a18e806e | -8.91944 | -60.55553 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e9ccbfb-487a-354c-a957-301fcdcf2599 | -9.70187 | -61.29998 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c2c74c9-d6ac-36ab-8fd9-7507a0495387 | -8.91891 | -60.55952 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0310cb5-712b-3194-b948-1b4498f5ddaa | -8.90023 | -60.56893 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fef93030-0f83-353a-83ef-89841ece485a | -8.91934 | -60.59986 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| feb307bf-5dfc-346b-ac36-cbf3dcccdf08 | -8.91996 | -60.55161 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 579d295e-97f6-3d3e-841a-bc3e4b5409a7 | -8.91287 | -60.76029 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b45114b-e227-31e3-a426-d4739be7f15a | -9.70785 | -61.2971 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7169690-4a4a-375c-9ce3-65536725196d | -8.92115 | -60.60394 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3833f15b-2398-33e1-9490-3410ea09c972 | -8.90595 | -60.56963 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5f061e71-8aa9-33e2-8dfe-665c0b863e0d | -8.90954 | -60.58633 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| d32a2343-cbb4-3e9c-9f49-d47878bb69b7 | -8.91528 | -60.54302 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4eb72ceb-efe6-3800-8440-b1aae2567d68 | -8.91267 | -60.56273 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 166fe6f5-5274-3a04-a8b7-1998cac7972c | -8.92367 | -60.58393 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1a7d0d1-59a9-3f3e-900c-055cc84f849a | -8.91457 | -60.76437 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 838907ea-482a-3177-9c0c-a710d2a34fc7 | -9.51046 | -63.52738 | 2025-08-06 06:01:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 252a5e39-4230-3062-ac37-721edc74cfaf | -9.1795 | -60.83382 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42d001db-0706-37d8-aa5e-fd4dc2cda5e7 | -9.46485 | -57.8551 | 2025-08-06 06:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d158fe68-b1fc-3ebf-8d1a-d29c2ccb6aa5 | -9.70813 | -61.29927 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c67b44a-3925-36a6-9b83-6bdc8310cc1e | -8.92201 | -60.57986 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9000ed0d-c5a6-3989-bd21-eae75281dff5 | -12.44103 | -63.70044 | 2025-08-06 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c3d86c8-1d10-3539-aa57-675f1f8c2298 | -8.9245 | -60.6046 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70e031e5-b77a-3ce6-bea4-ce6050aaa694 | -8.91664 | -60.74901 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d275a545-00f5-3d15-a381-76c4d7b6c139 | -8.91059 | -60.57842 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0dcf6db3-efcd-32dd-8043-2613045b5a8b | -8.92048 | -60.5477 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 144e0cff-b66a-33e0-9ec0-81830a170634 | -9.46722 | -57.85088 | 2025-08-06 06:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2fc42b0-9ef1-3cfa-ae8c-731768d1c912 | -8.91216 | -60.56659 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2560497-c4c5-3375-a79f-0f6e4852e59f | -9.70859 | -61.29565 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c96d4b60-93b7-3c68-b4d5-044a429e51f9 | -8.91819 | -60.73755 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0f413e7b-2c64-301f-ace8-d6500058404e | -8.91373 | -60.55474 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7106e3c1-51d3-30fd-ad45-a21ede35c976 | -8.90489 | -60.57764 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4868961a-4d86-363f-9b7b-c398b8e7a9ea | -8.92461 | -60.56032 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 591cb15b-2461-32e4-9544-a8a20b5b81d6 | -9.18564 | -60.83068 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)
