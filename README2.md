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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46279820-afc2-31dc-a08d-33f0e4232b15 | -3.10287 | -41.86751 | 2025-01-29 04:12:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc4948d5-0581-3bb8-953a-cf24552d3e02 | -4.51537 | -38.27224 | 2025-01-29 04:12:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3b86cf69-e69b-37a7-88fb-01346e100019 | -5.29806 | -35.98972 | 2025-01-29 04:12:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79e4ae8b-baf2-31ff-beb5-ee4eea813ba0 | -3.42084 | -43.16507 | 2025-01-29 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a392361-f1f4-3024-b8e0-8888142ee663 | -0.8278 | -47.45298 | 2025-01-29 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8744c9b-fd8b-35a0-8318-aacd8b4c6adf | -5.29623 | -35.99117 | 2025-01-29 04:12:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 838da3e7-cb09-39fb-9baf-587a9064e2fd | -3.6152 | -47.31202 | 2025-01-29 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac8fb6eb-b56d-3f46-98c3-8f86dfbf53f9 | -3.13354 | -40.04995 | 2025-01-29 04:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc6136e3-d457-3be4-aff2-2a4b7318df5b | -3.09957 | -41.867 | 2025-01-29 04:12:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3000c7dd-2ccc-3114-a99d-f71b7a0cd299 | -6.93615 | -43.53683 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d511e972-78de-34c8-8618-6575d4487e96 | -5.47449 | -42.91962 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a50dfc1-7497-388e-b425-86d51f36d68e | -3.31005 | -53.86282 | 2025-01-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90cc1118-1b6d-3bd2-9974-c90ee907da6b | -6.51108 | -47.60115 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc9db955-c977-3d7a-9993-3cfc5fde8945 | -6.94221 | -43.54132 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fc4d865-f5bd-33cf-bd93-cc151bf3adb1 | -6.94275 | -43.53786 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4dd44af-1f6e-3ff7-9c60-d1cdb473e98b | -5.46406 | -42.92152 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cc2c7210-e0e0-32d2-80ca-6360d9253f70 | -6.51189 | -47.59624 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fefe9415-0d13-3603-9c04-08b86d650aaa | -5.4679 | -42.9186 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5944a5df-683a-3fdf-a796-5f8d26fd6e3a | -9.1638 | -49.49826 | 2025-01-29 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404ead0f-46a3-3a67-bdaf-d48cfbefdea4 | -6.66252 | -47.60905 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3aec445-887f-3fc4-ba9c-44793132cf0c | -5.47395 | -42.92306 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb9b6195-64f9-3899-b444-832071ed8e53 | -6.9389 | -43.54081 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4e29bc3-738d-3869-9072-9be2cc730282 | -6.95044 | -43.53197 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ed2d8584-8898-3270-b7ee-ff3d5c0ccf47 | -11.59707 | -44.8654 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 080dbeea-183c-3e9c-b27f-2c2ad15c259c | -11.78029 | -44.71808 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 997d9938-346a-3567-89a3-120c43c588a7 | -6.94438 | -43.52748 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12deaabf-d130-3da3-bb31-2692b86f3f09 | -9.16792 | -49.49904 | 2025-01-29 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f749ecfd-2453-339d-a113-a4b6b0da05eb | -3.30875 | -53.86016 | 2025-01-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11594271-59c2-3e16-8134-6c024923cf85 | -7.95234 | -49.75931 | 2025-01-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8be036e-f25c-30a6-88c8-0baff4653efa | -5.47066 | -42.92255 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 26b6af46-9ecf-3de3-94c6-660dbaa72fcc | -7.94793 | -49.75861 | 2025-01-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 860da600-33a8-3447-9bff-ee65fbd5790c | -6.93339 | -43.53285 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 00bd0429-8d57-3788-918d-3c28d0b8304d | -3.31498 | -53.86116 | 2025-01-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625e18be-f267-39a8-83a2-d6ffe799b8b6 | -6.49702 | -47.4928 | 2025-01-29 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2900edd-1f06-3d0b-8bbc-083338622fe1 | -6.93999 | -43.53389 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 6824442f-2ea8-3fc6-acea-355239452f8a | -7.95083 | -49.76798 | 2025-01-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca98d59f-3ef5-37ac-b454-7b96d2d81190 | -5.47119 | -42.91911 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a97e1f9-76c2-3c8b-ae14-d28a7460f20f | -8.71436 | -44.00221 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b69505-c8fc-37a9-ba6b-8039eff73582 | -3.31918 | -54.91391 | 2025-01-29 04:14:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 17f8cedb-7862-375b-b704-807edfc62dac | -5.46736 | -42.92204 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5970f68a-1eb1-3512-8e2d-72774e04e37e | -5.024 | -45.96931 | 2025-01-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b2e5369-833a-348d-844f-c54e611795f8 | -6.94384 | -43.53094 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c052df77-afd2-3de0-a916-865f4547c628 | -9.16369 | -49.49833 | 2025-01-29 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75a8f418-321f-3c5d-ad20-904dd06961ca | -11.59763 | -44.86187 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c82b916-47c8-3aff-b146-89da51f72527 | -5.46352 | -42.92496 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 446c47da-f937-3a84-98e6-b1ace942717c | -10.2163 | -52.85648 | 2025-01-29 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba173760-04e7-31b5-848e-3e27cc26d1f3 | -6.94605 | -43.53838 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e144fd1-9ef7-3715-bcea-5d378e884040 | -11.26159 | -44.48932 | 2025-01-29 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d944d877-e64b-3d57-880b-68cf01b2d905 | -11.78085 | -44.71457 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6bb19c19-089d-3387-beca-79b23763d93a | -8.72428 | -44.00378 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5543f146-3473-3c86-a015-b93e8173dd00 | -8.84174 | -49.90445 | 2025-01-29 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2b9b338-8a21-3815-b8d1-3d5ab3223cfb | -11.26379 | -44.49685 | 2025-01-29 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccad5914-9312-3646-bcb9-27bb97c4f6b3 | -6.9499 | -43.53544 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9394450e-7547-3106-8c42-1a209a378687 | -5.13037 | -42.87942 | 2025-01-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63b4138d-d102-3386-a64a-60e9b10d09c2 | -8.72097 | -44.00325 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c19ee48-baaa-3ee6-97ee-147ddbc318b0 | -6.94768 | -43.528 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdc83293-9cb3-3495-90e3-a4682fd48f20 | -6.50169 | -47.48868 | 2025-01-29 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad41382a-199c-3bb8-b231-4e70c5805560 | -5.72186 | -43.51057 | 2025-01-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21178abb-4813-3e30-9b11-04b3f3ec86d5 | -6.94108 | -43.52697 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d637ee8a-f31a-3f07-bca3-ea7a4dbb4692 | -6.93945 | -43.53735 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaf4958f-6221-3fef-9d98-9b998f5cd261 | -6.93832 | -43.52299 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f5f50b7-86ab-3518-b3cb-0d7fd2872c82 | -6.65992 | -47.60579 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0723d75e-79d7-395d-a529-2e151871219c | -8.72042 | -44.00674 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43313972-181d-34cb-8530-292cc319787b | -6.50636 | -47.48451 | 2025-01-29 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0edaba79-96ed-356c-aaaf-c99721a4feed | -6.50797 | -47.59568 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c3ea1ac-bc75-382f-bb81-95850d73b431 | -8.71767 | -44.00273 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a767da6c-caf1-35ce-b8c8-c3573c79f120 | -5.46298 | -42.9284 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 838087e0-5c3b-3e34-9da6-8c075946bb6e | -6.94329 | -43.5344 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0493389d-375f-374f-810c-f9344cee0ae5 | -6.94053 | -43.53043 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2365c03b-a210-3d2c-a1ce-4c93d8f4cbf5 | -6.94551 | -43.54184 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb726ce4-adde-3819-a7a7-303713fd0cd8 | -6.95266 | -43.53941 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d48ca43-319d-3ba5-8d29-7bfff97fef86 | -6.94935 | -43.5389 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcc87663-e6ab-3985-8969-9b23839d0bad | -11.25829 | -44.48878 | 2025-01-29 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2656c19-fe86-3317-b4ef-2b1c69b4ce1e | -11.59044 | -44.86433 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a4a0d42-41b6-391d-87f3-ec4195fe9c67 | -5.83383 | -48.08387 | 2025-01-29 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a5c1342-ba4a-31b3-b14b-2a64f8566a38 | -6.49783 | -47.48795 | 2025-01-29 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e45a3fe-3375-3010-94db-73a53f0a15d0 | -6.93447 | -43.52594 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c839f89f-6e3e-364c-8bd4-e48f6a0c09ff | -6.93778 | -43.52645 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 873dd900-90bf-3e08-abe6-9ac1c653ba7b | -11.86407 | -46.94662 | 2025-01-29 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfaf27e4-d51a-3bb5-bd69-515622a3e2ef | -9.98291 | -48.08292 | 2025-01-29 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2470a9ac-41dd-3e93-8a42-6f436db9c097 | -6.94162 | -43.52351 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c796f2-603c-3da5-b635-6c69c0b1ecc2 | -9.16804 | -49.49898 | 2025-01-29 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3369e98-9cc4-39e9-ac35-d91764665050 | -11.79131 | -44.71266 | 2025-01-29 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c2e6ae4-909a-374e-b4d7-c84986540708 | -9.98754 | -48.0788 | 2025-01-29 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e04e904-3693-3a93-8d13-b8ba1fcc57cb | -6.6374 | -47.85917 | 2025-01-29 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fcec889-0047-3262-933b-5cf2cc2f1964 | -10.2111 | -52.85553 | 2025-01-29 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af077efb-1575-39de-9044-93ddd88170fb | -6.5158 | -47.59681 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5a90b07e-27c4-3608-b5e4-0609f3109d77 | -6.94881 | -43.54236 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 273a3a79-a26b-3048-8fc0-de3f92da6641 | -6.9532 | -43.53595 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 644cdf09-fb38-3aa4-8fd4-5269252740ce | -9.98372 | -48.07814 | 2025-01-29 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d7d7d70-10df-37a9-a2bd-a81660282642 | -8.3278 | -49.37505 | 2025-01-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6b054e7-88f5-337b-854b-1fb7851f40e2 | -11.32155 | -39.30714 | 2025-01-29 04:14:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1bf3a086-0e26-376e-9eb7-587b632dee66 | -5.46023 | -42.92445 | 2025-01-29 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0df3b3a9-d414-310b-8256-8b5c02c854cc | -6.32378 | -43.36142 | 2025-01-29 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c97b882c-1f3f-3548-8253-b52af5b59411 | -6.93393 | -43.52939 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d2004b33-027c-3c04-8cfa-4293744152d3 | -7.17911 | -44.99437 | 2025-01-29 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ff75834-97db-32f6-a1a5-d5bf5ab337c9 | -5.25968 | -45.60863 | 2025-01-29 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae99cd40-a81a-3127-bd39-a191b3bacbc7 | -6.51499 | -47.60172 | 2025-01-29 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bad2022a-9d33-3c7c-94cb-61b288bd989b | -7.95308 | -49.75504 | 2025-01-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d74b5f2-d8a9-31c7-91a0-cb9a4ad33f28 | -6.7206 | -47.62582 | 2025-01-29 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
