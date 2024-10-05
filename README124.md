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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c234360-0dff-3bed-8614-afb874952628 | -18.69559 | -57.28666 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| adee324d-0eb3-349a-b5ee-15439869cf1b | -18.69163 | -57.28584 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5255ccf2-c37e-337c-9e1a-f50a45779cb6 | -18.68774 | -57.30737 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 568d4595-8620-3a82-b7c6-36acd0ba8c90 | -18.68768 | -57.28503 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 24665e59-d058-36dc-aab8-c108a2730302 | -18.68565 | -57.28672 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f42e01b8-103f-3766-90bd-a1f907a3284e | -18.68371 | -57.27519 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 1f07182a-182b-376f-8205-39c73460beb9 | -18.68068 | -57.29128 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a996277-beda-3cf0-a138-8aee27848552 | -18.67185 | -57.28177 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2de33a46-955b-36b7-9969-40e7ac0cb914 | -18.66888 | -57.27559 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 2405480b-a2d7-3c7d-a6cf-9939cd68bec0 | -18.66692 | -57.28633 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 6dfe5a9f-f137-3973-892b-a978d15ea58f | -18.659 | -57.2847 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| aad610b8-f918-3dfc-8547-3e65c132baed | -19.11155 | -57.47472 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a6f6628d-c772-3c74-9a32-f2359f5c3be4 | -19.02018 | -57.62385 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2b055644-ee15-3688-8038-433304ea9544 | -18.88492 | -57.69773 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ce37f67-ca19-3064-8e2d-983b6a891d6f | -18.69663 | -57.30361 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 28ab1ec8-8594-364d-8ff9-ac453478f2de | -18.6955 | -57.29988 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 1087e076-b3b1-3513-8e46-321d02c310bb | -18.69456 | -57.28298 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f8740173-5ae2-364b-9c53-cf60ae6b8b6d | -18.69261 | -57.28047 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 46c41755-c4a7-339c-b559-542e2ba2b609 | -18.68865 | -57.27965 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 384265cb-361f-338d-adb7-d5b318e6d3ac | -18.68666 | -57.28135 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8b74710c-8cdc-3c0c-9dd9-dce0c992346d | -18.68469 | -57.27884 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| fc4e7fe0-06de-32c4-8e15-8f869a405e64 | -18.6827 | -57.28055 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ad1a662f-2a6b-3785-a5ef-4c32a9919717 | -18.67483 | -57.28796 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fb98d3fb-af87-3602-b05b-3171f1711835 | -18.66989 | -57.29253 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d8c8668f-09f2-3baf-b395-5eed531b53ec | -18.66198 | -57.2909 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 46e0a472-ffdd-38d2-b223-1df8a9dbafdf | -15.1079 | -58.36095 | 2024-10-05 04:40:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f75acbd-3231-3d04-86be-8b54901c5f16 | -15.105 | -58.35763 | 2024-10-05 04:40:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 024c045f-642b-3c2b-9fd4-2947629b0b7b | -15.10421 | -58.36177 | 2024-10-05 04:40:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b3b7c3e-ccf7-3855-853f-303ff0fc506e | -15.10347 | -58.35962 | 2024-10-05 04:40:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c3f7451-5a1a-3ccc-a742-22499370685f | -14.88678 | -58.03237 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea1bf15e-61e9-3519-82b6-00eba92f4ddc | -14.86613 | -58.02012 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e85ac2f4-d61e-3a69-b433-63083ab81be7 | -14.86534 | -58.02426 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4b7df0-91ec-37e4-a65c-955096bb3105 | -14.86456 | -58.02841 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b42032-f8cf-36d8-adec-c895efdb861b | -14.80742 | -58.57794 | 2024-10-05 04:40:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 279ca5b3-aca8-343b-bb98-d2a643901930 | -15.38719 | -58.14265 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76cc26e3-ec3f-3bf6-b9d6-9ea950a168e3 | -15.38288 | -58.14122 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9953ed7-5f62-33eb-a0bd-207ddfda963c | -15.38024 | -58.13792 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a090bc96-8a30-36a0-80db-6caf2b0bd338 | -15.37937 | -58.13559 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcf76602-2d00-3d9d-8906-0b1d7a3f8735 | -15.36964 | -58.13847 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec5baa45-c781-351b-84d6-fe49af5a1132 | -15.36528 | -58.14445 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d70ebbf-e57a-3362-93bb-2e130d66197f | -15.36434 | -58.1422 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a761e1c-0c3a-3fae-8cb4-f13883838817 | -15.3635 | -58.14653 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ad8033-2a94-3065-ab2d-d31b07c78c1d | -15.3458 | -58.1506 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b74450c0-ae95-3d05-a317-9edaecd525c0 | -15.26891 | -58.19247 | 2024-10-05 04:40:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c94b971-4dd1-340c-8f18-b23fc317dfe0 | -16.54655 | -58.20171 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e381a436-ea4d-3300-83ef-559406d073cc | -16.54332 | -58.21913 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4a17ee43-9e9e-3572-a446-d7d051b07997 | -16.53979 | -58.21381 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e2b2e129-eaa9-3fef-90df-3a7dd1658f6e | -16.53897 | -58.2182 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a60902ee-62bf-3af2-adaf-377e0bafe418 | -16.53815 | -58.22258 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 362f2de7-2b07-370c-ae0b-96a09b53a135 | -16.53734 | -58.22696 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8a6ae866-1e1a-3730-af17-c1da9ad5954c | -16.53652 | -58.23137 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 94b32815-def2-3112-befd-58f75ea178f2 | -16.53544 | -58.21291 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6e9b206d-b0a0-3c56-a542-afc5a0011b5e | -16.53462 | -58.2173 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5d42fbc1-72fb-3704-9576-a0b890ec74f5 | -15.17562 | -59.44332 | 2024-10-05 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c4f5fed-489f-3238-957f-5be20e08cd0b | -15.17457 | -59.44878 | 2024-10-05 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83138ab0-f7c1-3c43-a12d-3904eb6fbaae | -14.78376 | -59.43066 | 2024-10-05 04:40:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277b6c41-79d4-3128-b0b2-c48b9baf845e | -14.7789 | -59.42966 | 2024-10-05 04:40:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13364248-63d9-3545-a49a-8328bf43cf05 | -15.48815 | -59.80803 | 2024-10-05 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a03aa0-7076-30be-bcac-1939f897068d | -15.48702 | -59.80828 | 2024-10-05 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 078044bf-0e87-31c3-9468-3255ec7466d0 | -15.48585 | -59.81953 | 2024-10-05 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82b93324-a275-3f28-94ef-06ba5fcb3865 | -12.90647 | -62.44976 | 2024-10-05 04:40:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1c2f6f1-08e0-3282-8409-7c1712d99478 | -12.90547 | -62.45459 | 2024-10-05 04:40:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a3f564-2c40-3974-a778-c3a4dcfb9d12 | -12.70611 | -62.94374 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94b93773-ee6a-3ce4-a34e-3be7dd0e04c9 | -12.63596 | -63.10207 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 58ff3edd-5ae7-301c-b1ec-771453a8f881 | -12.6342 | -63.1033 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89dd7404-7997-31af-9f05-ba4a5e18f7d0 | -12.63372 | -63.1127 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c9fbaf4-502e-349c-8a3c-13cc1004eb2d | -12.63202 | -63.11395 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95f8a26b-8303-39d8-b5a7-8538117d6b50 | -12.64055 | -63.10466 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37bb54db-56b7-387a-ab57-a7a72da970e5 | -12.63528 | -63.09797 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17d25d1b-1c08-360f-a4d8-8246d1e971cd | -12.63092 | -63.11932 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce3c4d6e-d7c6-3226-9e9f-26b592de0417 | -15.57344 | -57.45703 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ae9467c-c346-3a50-a3b9-c75b00054d0d | -15.5727 | -57.46108 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd5508f6-29ec-3b42-a2f6-ee4fd9d3583b | -15.57196 | -57.46513 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c073499-bb65-327c-a2f4-af9ce2b3da98 | -15.57121 | -57.46917 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6aa5adf-c055-388b-bf62-2ae2498c68c4 | -15.56923 | -57.45618 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78ea6b78-7cbc-354e-bf44-01935bde4c56 | -15.56848 | -57.46022 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c759304d-dfb0-3b77-b7ea-4ce904918a47 | -15.56774 | -57.46426 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1401f6b0-391e-34e5-b1d2-1fc91e317e0a | -15.567 | -57.46829 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86f4d189-3663-37a7-864d-4a2f93d101f9 | -15.56501 | -57.45533 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecee63ed-e380-37cb-9111-de88b929dcc1 | -15.56427 | -57.45936 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93135d91-4f28-36c9-a83c-7bb917d1edb5 | -15.5608 | -57.45448 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fd8e4b2-9a36-3450-a02b-e9c54109cdaa | -15.56006 | -57.4585 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4a42179-7406-3a10-9825-522de1a9692d | -17.83877 | -57.69007 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 37679209-c4f5-337c-830d-5db0a22071a9 | -17.19277 | -57.39493 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4aa71564-27bc-37e1-b214-d139dfd6ca89 | -17.17519 | -57.37559 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 57813b99-a267-3e9f-9c2e-082f2cac1fe2 | -17.17253 | -57.36717 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bb681814-ab7a-3b3f-aad9-f263fa6f6a28 | -17.16846 | -57.36634 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b36508da-0b6a-3c7b-803a-d684fb51626c | -17.16775 | -57.37013 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ec73b053-7528-3d22-af37-4a56e919ce17 | -17.16543 | -57.40517 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 4f3a8b1c-bd62-3f1a-a6b0-d45f0655dc7c | -17.16247 | -56.96708 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f4c0a98a-da66-3fc2-b041-ab2a8c6c9ec5 | -17.16154 | -57.38069 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5c40c6fb-7b5c-35cc-8627-c5af9f31e7c6 | -17.16134 | -57.40435 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5a848123-e3cb-36d8-922e-0b586adfd529 | -17.16101 | -57.36091 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7030283-cd11-3c1e-b4da-262168161478 | -17.1603 | -57.3647 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79ac65da-b846-3e88-9428-139de434f7bd | -17.15959 | -57.36849 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ffa2b16f-7647-3750-80dc-70449296f33f | -17.15849 | -56.9663 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 10be03c8-edb3-3b96-994f-064a7b0b54c3 | -17.15745 | -57.37987 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 080e7cd8-c257-3920-94c9-05c2cfab4ffd | -17.15726 | -57.40353 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 923f7e86-1ac9-39b6-80a1-6dfd40fc8c02 | -17.15654 | -57.40734 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 5e78ec4d-0f34-3c9b-8d3a-32d5ce8bdcce | -17.15317 | -57.40271 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README125.md)
