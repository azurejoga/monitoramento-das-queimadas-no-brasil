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

## Dados Diários - Página 250

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90450c22-f514-31b5-bc83-a33577ec7ae9 | -15.91035 | -38.95407 | 2026-10-09 15:20:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 1c83dbc6-06d1-374c-9559-aa9a2669c3b8 | -15.91008 | -38.95683 | 2026-10-09 15:20:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| d8aa9878-1d54-321a-8830-c04f3cb037b9 | -15.47579 | -40.49343 | 2026-10-09 15:20:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 17fd896c-cf45-3129-b18c-6aef2e92487e | -16.23077 | -40.14748 | 2026-10-09 15:20:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5fc73bbd-0b5b-3399-87af-dedfe2f3acb5 | -16.12635 | -39.00702 | 2026-10-09 15:20:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a766cf9b-52e5-3473-8219-e674a211d9ce | -16.13184 | -39.00669 | 2026-10-09 15:20:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 7cf9077d-54de-3bab-9ad3-a60d48cc7c1e | -15.9186 | -38.97002 | 2026-10-09 15:20:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| c4328689-9cbc-398e-8398-08a1429803b5 | -15.91769 | -38.9673 | 2026-10-09 15:20:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| d47805c8-6930-3fcb-b804-199f657c256d | -8.65362 | -37.70182 | 2026-10-09 15:22:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b1513efb-f12f-3eb0-9894-70caa14628ef | -11.88311 | -38.75022 | 2026-10-09 15:22:00 | NOAA-21 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 61e51c54-9674-3e40-a70a-2693956aad5c | -13.74435 | -40.83546 | 2026-10-09 15:22:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 761a2150-91a5-3a5e-87a7-fc652bec64f9 | -15.07883 | -40.44429 | 2026-10-09 15:22:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 6665d7f7-c92b-3218-b47f-7f956c8aaafa | -10.0565 | -39.51503 | 2026-10-09 15:22:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdb640f6-3268-30e6-8470-9d993b97010e | -7.59736 | -37.87674 | 2026-10-09 15:22:00 | NOAA-21 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cc618be6-c532-314d-aef7-16af19c2741d | -13.55854 | -40.88948 | 2026-10-09 15:22:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| bd079c5f-187c-3346-a6c6-aba8de7a2023 | -13.58277 | -40.01127 | 2026-10-09 15:22:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| baa9264b-c5db-3784-8097-64eced424902 | -9.25171 | -37.76095 | 2026-10-09 15:22:00 | NOAA-21 | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2ae73a2c-2d91-3380-a47d-94e1bb9a8ec2 | -14.77788 | -40.74097 | 2026-10-09 15:22:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a2cad4fb-2841-3f94-800c-91d279ad1c5e | -13.00804 | -39.73631 | 2026-10-09 15:22:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 2c3af674-4de1-31f8-adb8-8ed487376cfc | -9.11319 | -36.86584 | 2026-10-09 15:22:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 92125c6e-1ecc-3c13-8770-79862ec0d205 | -8.67516 | -41.18937 | 2026-10-09 15:22:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 886f7869-8fd8-37d6-8894-da67893ef0d4 | -10.07851 | -39.40487 | 2026-10-09 15:22:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9b8a938e-1b66-3524-abf1-9ba64f6079ee | -7.43085 | -36.98508 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e4db2d28-21d2-30f2-8ded-c26d7c6e2e66 | -7.66083 | -36.90628 | 2026-10-09 15:22:00 | NOAA-21 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e06964b3-6b38-32be-99b4-a3fc8f8b0814 | -7.96825 | -38.73046 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 49c45dcc-3954-3ce1-b298-a33d33fe52e4 | -7.59667 | -37.87684 | 2026-10-09 15:22:00 | NOAA-21 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 325b5cac-d442-3823-aae6-28b6f20562f4 | -10.86769 | -39.42743 | 2026-10-09 15:22:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| cfab66b0-23d3-3ed3-92b9-43e313ce2713 | -7.79226 | -41.08821 | 2026-10-09 15:22:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6ee108a7-7670-3131-8a3a-3ff860e6d25d | -7.84142 | -35.24884 | 2026-10-09 15:22:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e318e287-4541-3ca2-9924-85d688c2eb39 | -15.08053 | -40.44082 | 2026-10-09 15:22:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 859f2004-cf8a-3bf9-9066-9192ca248ae4 | -11.08143 | -37.22133 | 2026-10-09 15:22:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| bbad144b-3779-3f80-8fad-18ee751b182e | -11.79481 | -40.92658 | 2026-10-09 15:22:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e0cab92f-2260-35a5-aee3-a5405ad4026a | -14.34158 | -40.45775 | 2026-10-09 15:22:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 6a1e443a-1cb2-3e46-9b2c-fe8f6f6e4e5c | -12.35 | -39.554 | 2026-10-09 15:22:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ac0e206a-6304-372a-a47d-70f8626a5c50 | -10.61971 | -38.88108 | 2026-10-09 15:22:00 | NOAA-21 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3f50a5c2-f561-3bc2-bec0-7d640d479a77 | -8.84933 | -36.5273 | 2026-10-09 15:22:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e7e3a604-19ac-3bff-8580-c70d704d2a4f | -10.89285 | -41.29512 | 2026-10-09 15:22:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 83118339-5426-3ec3-b7cb-d2f8d1613bca | -10.87404 | -39.42675 | 2026-10-09 15:22:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 136efb35-f1e6-384f-a667-c2573c737975 | -12.28762 | -38.74772 | 2026-10-09 15:22:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 7092a0df-da9f-3723-9c27-48f3da8e2751 | -10.80898 | -39.36599 | 2026-10-09 15:22:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| bbba4015-8248-3543-9c3f-4c49de89345c | -13.28508 | -40.32558 | 2026-10-09 15:22:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2b495ea0-cce1-33df-a132-6197b9f41e1c | -10.99561 | -39.61165 | 2026-10-09 15:22:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 933c697a-2b02-30bf-9def-953e997cb503 | -14.34015 | -40.45919 | 2026-10-09 15:22:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 3cc5e484-3026-3998-bfe7-7288626a00ac | -7.80366 | -38.73831 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 676c06e3-a56b-3769-a89d-67a6c13ee90c | -7.8056 | -37.66478 | 2026-10-09 15:22:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5f58996f-5791-3d6b-a009-b6055af05e2a | -10.63731 | -40.03788 | 2026-10-09 15:22:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| bf6976ac-8d28-318b-8a9a-7e0386154d91 | -12.29229 | -40.2833 | 2026-10-09 15:22:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f8ee83d2-3071-38ac-aa10-9311186b140c | -12.22526 | -40.69533 | 2026-10-09 15:22:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 130c4e18-3ffa-3db1-ac52-754000f8b311 | -10.99773 | -39.61528 | 2026-10-09 15:22:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 16b78cc5-edd3-3d27-8464-18b2db934c41 | -12.82121 | -39.22428 | 2026-10-09 15:22:00 | NOAA-21 | CONCEIÇÃO DO ALMEIDA | BAHIA | Brasil | 2908309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 2b3019ca-e3e7-30b9-ad2c-6f119fd19e51 | -13.33312 | -40.3827 | 2026-10-09 15:22:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| b80afc38-8d58-349f-9479-ef79ba1068f8 | -7.72002 | -37.65982 | 2026-10-09 15:22:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| aead090e-bec3-3609-a8c2-791104c2ee0b | -13.33292 | -40.38014 | 2026-10-09 15:22:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 9b22978f-afaf-3944-87b9-b0aa9324184c | -13.00342 | -39.73614 | 2026-10-09 15:22:00 | NOAA-21 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| f59eec3b-703e-3a27-a263-7a276ec0719a | -12.03494 | -40.04418 | 2026-10-09 15:22:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f5c8b1ae-dc81-39e1-94cf-8f7f5fbff791 | -13.7451 | -40.84275 | 2026-10-09 15:22:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 161aec01-9363-3f6e-a0e8-d72cba60b226 | -7.28733 | -35.87323 | 2026-10-09 15:22:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 674e9a80-8263-3c16-be22-f42c5f33e76e | -7.81755 | -38.85122 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f42ad31e-186f-35c3-9165-37c5282e8e47 | -14.49086 | -40.82857 | 2026-10-09 15:22:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 5b5b66af-2a84-3057-8070-cf0a50cd3214 | -8.5044 | -35.40829 | 2026-10-09 15:22:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2245d421-5547-306f-a0a8-9f48b664018d | -12.23482 | -38.99422 | 2026-10-09 15:22:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| ddf5f6a8-c809-337a-94a9-3e9cdbc0298a | -8.15024 | -40.50532 | 2026-10-09 15:22:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d0928ac5-3d15-3d05-b691-45554302860e | -10.83331 | -40.30508 | 2026-10-09 15:22:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c4ce17bb-2936-31be-804f-272602605272 | -12.1902 | -39.77014 | 2026-10-09 15:22:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 67946387-ebf2-322a-94b4-884eda5d214a | -13.74902 | -40.84447 | 2026-10-09 15:22:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 9c205095-6216-3e0a-b0b2-283ae9e1ba4b | -14.56222 | -40.67048 | 2026-10-09 15:22:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cf1ed0c4-027f-3fab-8ae6-18104670444e | -7.28803 | -35.87828 | 2026-10-09 15:22:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 15d70a2c-84ae-317e-8361-fa693369572a | -15.10261 | -39.58406 | 2026-10-09 15:22:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c5d5d079-be8e-3db7-ba41-2f1f938f491e | -14.49404 | -40.82624 | 2026-10-09 15:22:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 706c819d-362c-360a-9f73-497843f20f8d | -12.18853 | -39.76664 | 2026-10-09 15:22:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 430b6b70-7163-3064-9e98-3c78c2f57359 | -9.25218 | -37.7646 | 2026-10-09 15:22:00 | NOAA-21 | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8b94ca7d-e6fa-3772-a56d-40988a1d4172 | -7.43359 | -35.08342 | 2026-10-09 15:22:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 36e3bcd8-cb2c-340b-a4b6-a9c5780da053 | -7.80321 | -38.73827 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| f81f9940-b9e7-39bb-8d61-cee0220d0c0a | -12.28856 | -38.74863 | 2026-10-09 15:22:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| d2ecdd59-c612-31b4-a554-7e38dc7b519c | -11.65189 | -38.9004 | 2026-10-09 15:22:00 | NOAA-21 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9162fe71-8222-3fec-8c29-0a843e2b5322 | -10.87465 | -39.43177 | 2026-10-09 15:22:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 80.3 |
| a071844b-cf2f-3511-b13b-5e20b953046e | -8.67616 | -41.18884 | 2026-10-09 15:22:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4c5f59c0-ac55-3504-a704-61b671678621 | -13.00068 | -39.73006 | 2026-10-09 15:22:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 4e77e70b-4d96-3eee-bbac-699d053460ee | -13.74832 | -40.83719 | 2026-10-09 15:22:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 0a33db52-e3f5-3e3c-a32f-9fe00acac5a7 | -12.03083 | -40.0416 | 2026-10-09 15:22:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d16375f2-8816-355d-999d-463e4f677ba5 | -9.0021 | -41.15546 | 2026-10-09 15:22:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 84ab734c-d56d-36dd-8656-a90298ac2a17 | -7.72094 | -37.79222 | 2026-10-09 15:22:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f7d7d537-2dbe-3be3-80f1-62bda78299f9 | -8.52224 | -36.52388 | 2026-10-09 15:22:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7d72679f-ec23-3866-8aba-5b11d22b7181 | -7.83161 | -39.08257 | 2026-10-09 15:22:00 | NOAA-21 | PENAFORTE | CEARÁ | Brasil | 2310605 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5f160fe5-8393-3fd1-8e7c-52cccc9ee749 | -13.00277 | -39.73032 | 2026-10-09 15:22:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 0bc99d12-9b0e-3806-84d5-65acf17efe62 | -11.97917 | -39.48388 | 2026-10-09 15:22:00 | NOAA-21 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e48a799f-04e9-3b2f-9102-c5614419add1 | -10.87056 | -39.42866 | 2026-10-09 15:22:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 159.3 |
| fb76c902-6cc3-3761-911e-bb9b67e3646e | -11.47749 | -39.77301 | 2026-10-09 15:22:00 | NOAA-21 | GAVIÃO | BAHIA | Brasil | 2911253 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 63425463-aaa8-30be-be81-763b57e6cd2b | -10.70405 | -41.2536 | 2026-10-09 15:22:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0180ca44-1ea1-3fb8-bec0-667c4c26cbe4 | -14.08962 | -40.38883 | 2026-10-09 15:22:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2acaee25-c15e-34b7-bfe4-8c297d3f7271 | -7.97893 | -37.74671 | 2026-10-09 15:22:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8acb4cb5-b335-34a9-afb0-815ab9457cb2 | -7.67987 | -37.40018 | 2026-10-09 15:22:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ac7f8a14-f801-3d32-bb0c-36f31d25c907 | -14.56573 | -40.67271 | 2026-10-09 15:22:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| eda0bf0b-9030-38aa-959c-eb141dea4542 | -10.6368 | -40.03959 | 2026-10-09 15:22:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 3707267a-7fdd-378f-ac6f-6a0f0bc56ea0 | -10.62058 | -38.88403 | 2026-10-09 15:22:00 | NOAA-21 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 40447185-1e63-3cc8-bd0e-0e0a6ce4dc3c | -13.55921 | -40.89631 | 2026-10-09 15:22:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 92da5002-388e-30a9-8ab3-7fbbbf7d9ca5 | -14.34228 | -40.46462 | 2026-10-09 15:22:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| e03fe07e-67ff-3067-81d8-5caa633582b7 | -11.48401 | -39.77219 | 2026-10-09 15:22:00 | NOAA-21 | GAVIÃO | BAHIA | Brasil | 2911253 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 17b7b999-8ac7-316b-b425-1e75437f889c | -11.2845 | -41.12848 | 2026-10-09 15:22:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1ef6fa55-9de7-3d95-a7ef-313b03313f26 | -7.79594 | -41.08535 | 2026-10-09 15:22:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |


[Clique aqui para ver as próximas entradas](README251.md)
