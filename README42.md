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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b8acbac-beb7-335a-b5e4-be32a1aa9b96 | -4.94817 | -42.98675 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 092c4393-b175-35ed-94d7-ff4da18a27fc | -4.94761 | -42.99025 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1dc7f6d6-67dd-395e-8834-a6291628da8e | -4.94704 | -42.99375 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92b1e9f7-79d2-3e4b-998d-a1e1deb5268d | -4.87294 | -43.0686 | 2024-10-10 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93a5b484-2ed7-3983-a9ab-e068dacae850 | -6.25875 | -42.51137 | 2024-10-10 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9dd7f81-8ef3-3b04-970a-e987037cf3d3 | -6.25797 | -42.51603 | 2024-10-10 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3eee7ced-6400-3f81-9953-2e8100678b32 | -6.25418 | -42.51528 | 2024-10-10 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7311c391-38ad-358d-b0e2-3a17c2841324 | -6.2534 | -42.51997 | 2024-10-10 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51b214c6-bdfa-335c-9f6e-4e4192364d12 | -6.24959 | -42.51933 | 2024-10-10 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94034504-b538-3082-bf7f-1887ecc6d4f6 | -6.14482 | -42.47077 | 2024-10-10 03:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f252d58f-e3d8-3610-8dfe-f5f2586e655d | -6.0829 | -42.37644 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8244381e-4bc1-386a-9359-eed6d31fcb2f | -6.07912 | -42.37577 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d646e58c-1564-3fdf-8d17-c868be1f3b0d | -6.03483 | -42.71574 | 2024-10-10 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cda7fb7b-8724-3f82-b5a9-2a19edebd232 | -6.00466 | -42.89849 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9f4e26cb-f0b9-3228-8ac1-280926c33b65 | -6.00379 | -42.90375 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 772ddfdb-19c1-3760-a7fa-29df3b959c6a | -6.00075 | -42.89782 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d1c5bdf1-1397-33ce-858c-5ac9af7ceeb2 | -5.99988 | -42.90306 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b0189c6a-78f4-3933-afe3-3cf4cd3eae05 | -5.99597 | -42.90237 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0aa7cec8-ebf4-3b82-aef4-4ae5c7502661 | -5.99206 | -42.90167 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d029760f-7772-3250-b9af-511f2d4a929a | -5.88234 | -41.9577 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 907e416f-55d8-3253-9b50-6137a33847eb | -5.88113 | -41.95557 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| caa2bf3f-481f-35ce-b9c4-8f80de7849a0 | -5.88038 | -41.96003 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ad7429f-0d93-31d4-8025-a5293dec496b | -5.87863 | -41.95706 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d1c4fad9-3067-3a2f-806a-e7ea9734da52 | -5.87742 | -41.95494 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f752b9de-eaaa-31ba-9459-ed3f971ddfd4 | -5.87493 | -41.95644 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd447777-1608-390a-a3d3-65558a08cf61 | -5.86752 | -41.95515 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 448183ff-3d28-392c-ae96-d20f60ab5b8b | -5.86679 | -41.95962 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2feef80b-9043-3b20-925f-955588e50475 | -5.86309 | -41.95895 | 2024-10-10 03:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26b4843f-6fc5-3ec9-8d6f-910b1e8a85a6 | -5.8214 | -42.40544 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a91dbe1a-c5c1-354f-b505-ad1471d2f6d9 | -5.82061 | -42.41015 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60e26772-9e4c-3d01-b7ea-d0be91f7f6e4 | -5.81681 | -42.4095 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0fb9c8bb-803a-37cd-b43a-8e7e48d344ea | -5.75507 | -43.19267 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ec006799-95dc-39d6-8865-b79c45885ae8 | -5.75106 | -43.19205 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5e94d4a2-817b-3cec-a316-d8bc8210f700 | -6.37403 | -42.9796 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be756944-1e0d-3799-a5ee-4af5ae929c71 | -6.32641 | -43.4558 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2f3d5c-a87d-30ed-9439-5da169a6a432 | -6.29232 | -43.46088 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6197d313-ff15-305f-9895-97aaab85fc46 | -6.28848 | -43.43468 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c006ae38-2bca-3c64-8eea-b3e4d4cc58c4 | -6.28757 | -43.43465 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c537867d-8cc8-3866-940c-cae636af6ed2 | -6.26794 | -43.42788 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce488f34-fdd5-3272-bc52-c4c33daa5ece | -6.26389 | -43.42731 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbac28b4-30c6-3391-ac5c-c10192b94194 | -5.99471 | -43.46303 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7e6b05cc-3269-34c8-8d51-63d294b748bd | -5.81536 | -43.23577 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d8d992c-38d6-3c38-8a2d-3a5c55727e58 | -5.66107 | -43.07779 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1912b7e3-ca58-3573-8900-7af260049948 | -5.56558 | -42.99792 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2797bd60-e33b-36eb-8bbd-3f683579c450 | -5.54845 | -42.92915 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d7e5145-3060-3501-906b-dd326cd29440 | -5.54334 | -42.74213 | 2024-10-10 03:55:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d5faa8e3-ae5a-3236-8826-62573b1989ee | -5.54257 | -42.74402 | 2024-10-10 03:55:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d5c52ec-7aed-3a17-8789-61fe44a9946e | -5.54052 | -42.92799 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 85466e3b-bd22-3c70-9ba0-fab40329aa8a | -5.52322 | -42.79 | 2024-10-10 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6344440-7b2e-3c76-a01a-69b160a84ccd | -5.51929 | -42.7894 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08188498-c757-3364-9f9e-24ee76dfc9dd | -5.51019 | -42.79519 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 913fe6c8-e0bd-31f8-aa96-89e50fbe594c | -5.50627 | -42.79456 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 738632aa-632e-3e74-859d-097a68518379 | -5.50234 | -42.79393 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6cb991f6-c148-336d-894c-6d5c8f0af8de | -5.50152 | -42.79901 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41e18ce8-1297-39f2-ab13-b6eda90715a3 | -5.49759 | -42.7984 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8a1600b-537b-39fc-8053-4919a403d167 | -5.49138 | -42.78708 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13bd2d1a-9e56-3a7a-b73d-c18b0fb1cf0d | -5.48829 | -42.78138 | 2024-10-10 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1cd96b30-b51f-3c67-a4b9-adb166d0d28b | -5.19164 | -42.52797 | 2024-10-10 03:55:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bcf8e130-4343-3874-9c7b-9bd504ddea65 | -5.58227 | -43.25462 | 2024-10-10 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8851f83f-01be-3d55-bfc7-3f18f20390d5 | -5.13568 | -42.89338 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60afa8c9-f42b-3262-9421-aa50297c5851 | -5.07058 | -42.87553 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c3d52c-92a4-3bea-add2-46296ba6df09 | -4.98525 | -43.02158 | 2024-10-10 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 508c2274-91ee-3507-9f5f-28a1af3f69b2 | -6.4887 | -42.17376 | 2024-10-10 03:55:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af0e0044-efe7-3de5-8dd5-a8542adb339b | -6.48496 | -42.17326 | 2024-10-10 03:55:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2526ef59-abd7-3e40-b99d-0c01bd117088 | -6.42286 | -42.01799 | 2024-10-10 03:55:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 72581464-a3b0-3117-9426-5dbf7bac437c | -6.4209 | -42.01474 | 2024-10-10 03:55:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c030f3ad-3d44-3d6b-9ddb-7e580294672d | -6.44263 | -42.92965 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a8bb669-4f92-33a0-af02-2410671d9334 | -6.42043 | -43.13761 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd799ed3-541d-3070-8e53-1ba67976a229 | -7.82975 | -42.46128 | 2024-10-10 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 663d0cde-de16-3778-b8de-ce20a357f1b2 | -7.82903 | -42.46568 | 2024-10-10 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 011912ad-c083-3583-b548-10f2138b523d | -7.82529 | -42.46515 | 2024-10-10 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0cc309f5-2b1f-37bd-a9ed-7676215bc26c | -7.80286 | -43.82892 | 2024-10-10 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af7a8e92-5e65-3ccf-8dfa-e6458b6033f4 | -7.7993 | -43.08584 | 2024-10-10 03:55:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d4924c9b-2f3c-38e1-87b0-640b20b4cd2a | -7.79846 | -43.09081 | 2024-10-10 03:55:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f4e456e-af52-32dc-a25a-e6463e5b5819 | -7.79544 | -43.08523 | 2024-10-10 03:55:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4c448f5a-c427-368b-8743-413249640c22 | -7.7946 | -43.09021 | 2024-10-10 03:55:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8d9b14ca-3c88-35a7-9d17-acc0d1e4a8e2 | -7.79293 | -43.10004 | 2024-10-10 03:55:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4a1678de-df8e-388b-a2b6-6002455f16ea | -7.73137 | -43.80494 | 2024-10-10 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dbe2e792-56a1-3d4a-841e-d2a0a649a596 | -7.73044 | -43.03674 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53fda893-105b-38ac-a6e9-19919950e24a | -7.72674 | -43.80778 | 2024-10-10 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f3de125-34b7-31b7-a4cb-c1cad3509e1a | -7.72659 | -43.03612 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f84fb77-0a4f-3077-9668-f0a5438938de | -7.72578 | -43.04097 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 64a0c889-40eb-3f99-91bd-ce7438969213 | -7.69073 | -42.99056 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| a1a82f0b-6954-3239-ae69-ee9dd728d3e2 | -7.6899 | -42.99545 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 594c330f-cc74-3d90-b084-f1ab72331f74 | -7.68689 | -42.98992 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 935c31e8-1c4a-3c1a-ad17-14aefe78293a | -7.68606 | -42.99482 | 2024-10-10 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e45b214a-c53d-3346-9e66-2ef0dc63ff1f | -7.67345 | -42.49266 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1de01b73-4ed4-3b82-a218-218d777bb878 | -7.67269 | -42.49721 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bff52f10-5478-3dcd-b664-e77bc16c648d | -7.66972 | -42.49204 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b3e264c-392e-3482-a919-a9ab78b7a1e9 | -7.66675 | -42.48688 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 73e50cfa-6628-3777-b258-0da37b9b1d0c | -7.66659 | -42.53358 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 271c234b-0dd6-3789-aa49-64b743d1ec34 | -7.6639 | -42.4128 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b608f676-1022-3719-9186-76e5bedab3a5 | -7.66285 | -42.53294 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da64aa83-3340-3bf2-8218-b7230b7ff735 | -7.66267 | -42.40905 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1db6687a-cc65-3ee3-967d-72b738aa333e | -7.66195 | -42.41349 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3ccbdb4e-5f0d-397e-903b-a54c57504720 | -7.66054 | -42.54671 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43f38135-e426-3e49-9887-4e439c0bd1bd | -7.66019 | -42.41217 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2ecdfcba-106a-3c48-9270-c600eeed4fa5 | -7.65679 | -42.54609 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f99d8d6-321d-338b-8200-57b2e6f789ec | -7.65426 | -42.40204 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 181e03f0-3a87-357e-ab3b-442791364941 | -7.65382 | -42.54088 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
