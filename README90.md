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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 573bf9d1-b2f4-3a37-93c4-6e446d989321 | -9.71415 | -52.84417 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66ee1aa7-ec7d-374f-952d-6cf5bd4593f3 | -9.71207 | -52.82514 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2f5f47f-a2b9-3bac-9619-d28ff4ed5432 | -9.71145 | -52.82973 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da1e8bc7-0e85-3c10-8851-cb246d4487de | -9.71084 | -52.8343 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e83d9d1-d3c8-3912-a82c-ccd36b673c1b | -9.71023 | -52.83882 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5ba4dbd-d50f-3d3a-9a09-74f829883276 | -9.63968 | -53.16148 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de51a6da-7d34-3155-a7c1-caf86a66332b | -10.64658 | -53.71056 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06e2723e-e26a-349e-a688-aac57c86c4b3 | -10.63821 | -53.67532 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a9c2c9f-6cf1-3928-af11-ddf4bf080a4b | -10.62576 | -53.66913 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4517873-481a-32cc-a9e9-556d9966e848 | -10.91165 | -52.35919 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7288b63-b820-3871-8c32-fd572a0fe64f | -10.89939 | -52.34152 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b770bbe1-2e7c-39dd-ae2f-44c82ba58180 | -10.89531 | -52.33548 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7923149d-1b5e-3e4d-840b-81b8cf018759 | -10.89461 | -52.34082 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a533da3-6dbe-317a-b497-35a1665bfb9f | -10.89391 | -52.34607 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699876b6-afed-3605-a9be-16de3e6a6f03 | -10.88984 | -52.34004 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f11c0ba-d5b1-3c8f-91f3-a6a5ca0a91b2 | -10.70743 | -53.04028 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cff68f8f-968b-3f92-a39a-7bda413f77a2 | -10.7068 | -53.04494 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d55575ae-b7b6-3d86-9b80-cbcc396a5e93 | -10.70413 | -53.03041 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a72e2e45-2011-3c2c-9d56-4d3cf52e4275 | -10.70288 | -53.03968 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e06c31c-f66f-35b9-86f5-9c0599c9435d | -10.70225 | -53.04432 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 152e6d01-579f-3de6-aa79-41093e4b6ae9 | -10.70161 | -53.04898 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d69ccbe-6173-3a97-84ea-7a25c643d273 | -10.7002 | -53.02518 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf623c95-8e7d-3a92-b609-45bd4181458d | -10.69957 | -53.02986 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8542ab74-37ea-37d8-9aa1-d4e7caa92f82 | -10.69706 | -53.0484 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50f140e4-c11d-3c47-a6b6-1f3d9ca7ab0c | -10.69627 | -53.01991 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8a7019b-8368-3800-9641-b4ed9e2e4e77 | -10.69564 | -53.02461 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a0a7136-aa33-3d69-bf69-8d34bc793904 | -10.69501 | -53.02929 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c52b5572-fd1b-3fc9-a273-f22b2af57049 | -10.69438 | -53.03392 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d03a75b-e410-3efa-9a5a-9cdc1eb91202 | -10.69251 | -53.0478 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e4bc91-b548-3803-9256-f6432af1f8d0 | -10.69108 | -53.02398 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1fe3e55-f3df-304f-bf73-bfae85a44c78 | -10.69046 | -53.02865 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4673b58c-aa7e-37d8-ad0d-c723f1b467c8 | -10.68983 | -53.03328 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b28130fa-e0a9-33dc-bc00-990dcdc8fb17 | -10.68528 | -53.03262 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e84f5c9b-7ae7-3211-8338-bdeb1c0cec4f | -10.60709 | -52.88369 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86d18668-0531-3a4d-8790-41bb2dcd94a1 | -10.60645 | -52.88851 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1cff90a-b95e-3c3e-bda8-90a8f6013958 | -10.2719 | -52.17551 | 2024-10-11 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f561bc7-434c-3c62-9c24-6a9562fb09d4 | -10.23088 | -52.76 | 2024-10-11 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7590ba41-799b-3c4b-ac30-c5e3ad9b8b35 | -10.23022 | -52.76479 | 2024-10-11 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65539827-68a3-3b4a-be84-6fcb83044279 | -10.22169 | -52.68981 | 2024-10-11 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b127c5d7-4e09-36ac-92ba-5dfde2b89143 | -10.22104 | -52.6946 | 2024-10-11 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d474f08-175b-3aaa-ac5b-762772410a96 | -10.2118 | -52.69321 | 2024-10-11 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 373aad87-56ae-3350-a319-a3426d47698f | -10.05453 | -52.08387 | 2024-10-11 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63aa4107-9d39-3a32-a140-c33bc2bf2169 | -10.04971 | -52.0832 | 2024-10-11 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada41b96-1209-3914-8177-f8ef49d9263f | -10.02768 | -52.10173 | 2024-10-11 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29a2007c-ec91-3659-80b0-62633331210c | -11.54071 | -53.84763 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de86d27a-c18f-3a2c-9c5f-0366c688d018 | -11.54013 | -53.85196 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b8ee4c2-bfcd-3fef-8cf2-a56595ed999b | -11.53955 | -53.85624 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d70685-81a2-3e1c-8f30-3e7a4b9cc546 | -11.53635 | -53.84699 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98343a6d-76f7-3b87-9211-c9a42e27b884 | -11.53577 | -53.85132 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53758ce7-e415-3a9a-8d9c-b4127826e94f | -11.5352 | -53.85561 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1bc2cce-4cfa-330c-9415-13bd47e7ee69 | -11.53463 | -53.85985 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e98bffe5-e7fe-3e67-91dd-2aa42a77a205 | -11.53142 | -53.85065 | 2024-10-11 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08eef7cc-b65d-3719-89bc-3bc849948c86 | -6.37931 | -53.63186 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a135fe7-9549-3761-8c3d-e9693df85273 | -6.1974 | -53.36527 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26f79ed3-5189-3357-bd5c-d47c10cc3bc6 | -6.19322 | -53.36477 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e943f00b-9f1a-37df-95a9-419f377b9b9f | -6.08605 | -52.88255 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 284e54ba-f65d-3adb-bd78-48cc5ce96e93 | -6.07753 | -52.88081 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbcb2aa0-c7a5-3408-af90-9383e6bd1ff5 | -6.00999 | -52.84292 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e02fb5d6-a3a5-3c11-bba9-2addf7794181 | -6.00943 | -52.84666 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20600322-2faf-3fe5-8c44-2f97aa34abb9 | -5.95071 | -53.74438 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59da62f4-9767-397e-b839-2f8d939bd2ff | -5.91772 | -53.43346 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a53635be-0b9c-3b19-8070-26fc43df104a | -5.91716 | -53.4372 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3c4d08-07e6-3f67-a72c-96806a28d2c8 | -5.81328 | -53.88522 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e890bb4a-a7c6-3d94-8a13-4be5e98036bd | -5.78389 | -53.83442 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdfc1c5c-9cb2-377f-936b-46b96c4d751c | -5.78339 | -53.83789 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f20629-c5db-333b-a442-03a3ac24d10a | -5.64402 | -53.86853 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74bc710e-c2aa-3ac6-bc8b-27b74bb440a9 | -9.17084 | -54.67372 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48bf0fe9-1dd1-35bb-afff-33282f67bcbb | -9.16787 | -54.66607 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ab1fdcc-7317-3d17-8e1e-878a42327f9a | -9.16736 | -54.66965 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af57e2b-d872-3c02-bfad-26912229f28b | -9.026 | -54.52957 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e500631-850a-3488-8192-2b89151941cc | -9.02551 | -54.5331 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6477dd9d-12f9-3c76-910e-c9a733164fa0 | -9.02198 | -54.52901 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a97a7e-38fa-3746-876f-37d4d4b05cac | -9.01489 | -54.50979 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 452a0c6c-4d46-3aea-8382-3e390c4e6c2b | -9.01438 | -54.51334 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1474fd46-e0e4-3248-8fc4-27578734a1c9 | -8.90406 | -54.74323 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69eea7bd-94a8-3f9a-950f-f8c30e101d6e | -8.89307 | -54.57525 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6c7f899-48dd-3ff3-b49d-f804c4a3f2bf | -8.88804 | -54.58181 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 838421c7-f0ec-30ce-ab26-f348d717a1b5 | -8.88753 | -54.5853 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50a96c58-7d51-30f7-9422-9f55aedab55b | -8.86286 | -54.69902 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35932a76-11bc-33aa-ae67-ca4002fdb690 | -8.85964 | -54.69333 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e7a421b-e9f6-3e7a-ad6b-8a719bc232e9 | -8.76382 | -54.74548 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 524f8dff-eda5-30e9-bb54-396895325248 | -8.76324 | -54.74663 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c115544f-791c-337b-bb96-9dd0bb2590c6 | -8.71904 | -54.83217 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67d00c2b-0748-397b-b7fb-a6fb05b083f8 | -8.70202 | -54.8391 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4f1a51c-3f05-3344-9c25-1fa8a7ce30d2 | -8.7013 | -54.84411 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4879a174-7db9-3a1d-afb5-3804e38ebf57 | -8.61654 | -54.59672 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71cdd19e-7cca-3b40-8c44-7f8643328dde | -8.61604 | -54.60022 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c812624-1809-39d0-b5c0-640deac84d4f | -8.61542 | -54.60458 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99ba512c-33cf-3e44-ac9a-256f7f002a46 | -8.34162 | -54.75339 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e552d15e-9263-3436-9b61-d47469603e61 | -9.4987 | -54.53539 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082aa52e-b7e6-3f8b-aa45-3332335f94d1 | -9.49466 | -54.5348 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e211c91a-4908-3668-9a68-5f09bc7f9f22 | -10.36216 | -54.1649 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b472f19-31e4-3fb2-9c4a-f61a882e3139 | -10.3104 | -53.70578 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e7902a8-37a8-39f7-aa9f-64c7e63bd103 | -10.27257 | -54.25734 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35d795c2-b3a9-3a73-93bd-b44e9c16b066 | -10.27205 | -54.26117 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0edde0c9-73d8-3be8-9f81-19f606829bdf | -11.61701 | -55.02241 | 2024-10-11 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1aeb9c7-045b-3e35-ad7d-9b2ffb44ad0c | -11.61347 | -55.01823 | 2024-10-11 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b83cae-7aa5-3a4f-b614-510d1c27379b | -11.61297 | -55.02185 | 2024-10-11 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63eb98c-b503-35f8-b7fa-c6e120323777 | -11.60437 | -54.69002 | 2024-10-11 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f25fd679-6f0b-350d-9f50-23287fe9915c | -11.60386 | -54.69376 | 2024-10-11 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README91.md)
