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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b716eb87-8684-307b-97eb-40a7e3dd9fd8 | -11.14604 | -55.56168 | 2025-01-28 05:22:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2bbed32-f4a6-3ebd-8e0b-36df5083588d | -8.55146 | -61.66394 | 2025-01-28 05:22:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02c537a0-90a0-3f31-b225-e08b8016412d | -9.25897 | -60.31606 | 2025-01-28 05:22:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7976e271-6d97-3b85-aa2d-976fed94a4f4 | -6.26956 | -48.03394 | 2025-01-28 05:22:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 208b8da2-0c22-3b6d-ba52-9a24d749d85b | -10.6898 | -54.3573 | 2025-01-28 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6d4052-3a98-3dd5-9db8-be51391783f4 | -12.70614 | -54.91154 | 2025-01-28 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f024f11-990b-343a-ae85-696403b99d4d | -11.71101 | -62.28337 | 2025-01-28 05:25:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3c488f9f-20f2-37ce-8e1b-6089c57cfefe | -12.69815 | -54.90061 | 2025-01-28 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2801901-21ea-3d22-9e31-973015a799e1 | -12.69877 | -54.89582 | 2025-01-28 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49b58737-6427-32cf-ba9d-c978223b6f6d | 4.31863 | -60.85656 | 2025-01-28 06:09:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0904b9d5-3d0f-38d2-9ad2-5af9eceee60a | 4.32422 | -60.8557 | 2025-01-28 06:09:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a0ef845-d14b-3cad-93f0-defcf341e08d | -11.00063 | -38.38462 | 2025-01-28 12:06:00 | TERRA_M-T | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9c7cd86c-c726-317e-9d54-e695808b427a | -4.98801 | -40.29608 | 2025-01-28 12:06:00 | TERRA_M-T | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6541ad76-ddf5-307b-80b4-b6e2328ffb88 | -11.07688 | -37.34837 | 2025-01-28 12:06:00 | TERRA_M-T | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7519b2cd-67fd-36d2-892e-e2d1cd484bbb | -5.54286 | -37.98353 | 2025-01-28 12:06:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5458fdbc-ea45-384e-acba-78248c90c306 | -11.93368 | -39.10002 | 2025-01-28 12:06:00 | TERRA_M-T | TANQUINHO | BAHIA | Brasil | 2931103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 44e1e519-a471-3577-9b63-f65d3bac1bda | -5.54155 | -37.99275 | 2025-01-28 12:06:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 919cca7b-b726-3b1a-bc6f-a27875f2cc12 | -5.53895 | -38.01118 | 2025-01-28 12:06:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ebe2bd3c-7687-371a-af7a-888466369913 | -6.23161 | -35.64983 | 2025-01-28 12:06:00 | TERRA_M-T | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a83becd6-a746-313a-9fae-703253ba5ada | -9.80185 | -37.11509 | 2025-01-28 12:06:00 | TERRA_M-T | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 14.1 |
| dbd7c059-792f-31a2-8e69-a7cb2e190358 | -6.16855 | -43.25613 | 2025-01-28 12:06:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 1612ce92-3fed-3e71-9f52-9a51c2f63a11 | -4.98668 | -40.30524 | 2025-01-28 12:06:00 | TERRA_M-T | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3f7c4882-1822-39e4-9255-02cb82708e44 | -5.53765 | -38.0204 | 2025-01-28 12:06:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8da65df8-dd12-3d12-a6ad-fae031237a3c | -11.07538 | -37.35972 | 2025-01-28 12:06:00 | TERRA_M-T | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| e278f555-db6a-33db-b9a1-40b007000926 | -12.27369 | -38.83921 | 2025-01-28 12:06:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5c8d3e60-f907-3983-bb18-10a5fe1f45a7 | -11.15666 | -39.12952 | 2025-01-28 12:06:00 | TERRA_M-T | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7b42d664-d30d-32dc-be54-4b91e6389b88 | -11.06312 | -39.20543 | 2025-01-28 12:06:00 | TERRA_M-T | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 43d7c2ca-2e47-3fa5-8155-8720d8006b1e | -9.45139 | -38.41592 | 2025-01-28 12:06:00 | TERRA_M-T | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 11dd1f3b-15d4-3762-a7aa-4b489fc38a07 | -9.0328 | -44.98387 | 2025-01-28 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0a79f1c5-c216-3040-94e3-2703e38925f7 | -12.32452 | -38.74516 | 2025-01-28 12:06:00 | TERRA_M-T | CONCEIÇÃO DO JACUÍPE | BAHIA | Brasil | 2908507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5ee1d6b5-6749-3602-94f9-1a2bd042b92a | -11.99162 | -38.06656 | 2025-01-28 12:06:00 | TERRA_M-T | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 72d4b565-f4a5-31a4-b98d-e65c63c141d2 | -18.93397 | -41.04652 | 2025-01-28 12:08:00 | TERRA_M-T | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 8e546100-3ca7-3567-945f-fc9ba4ef0056 | -13.16043 | -42.29082 | 2025-01-28 12:08:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 260cbd78-fb5d-3fb0-861e-7c8e09524798 | -12.76897 | -44.82645 | 2025-01-28 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 10e9a973-c145-3561-bc6c-5dcc3a37b7a8 | -13.84324 | -39.39956 | 2025-01-28 12:08:00 | TERRA_M-T | PIRAÍ DO NORTE | BAHIA | Brasil | 2924678 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| f76593b4-4ec8-3913-aa35-ed3ebf80ba90 | -16.72732 | -39.43108 | 2025-01-28 12:08:00 | TERRA_M-T | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 31b01a7c-4d22-366c-a267-6c7823d94e5f | -15.98828 | -41.93919 | 2025-01-28 12:08:00 | TERRA_M-T | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 33f5056e-3428-369f-a057-0b6909fa7010 | -12.70552 | -40.22955 | 2025-01-28 12:08:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |


