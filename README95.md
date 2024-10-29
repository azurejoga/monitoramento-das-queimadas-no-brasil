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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89035a8e-39a9-3d52-82a1-ca2d77068112 | -1.20656 | -55.90488 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1e05c7cc-d89f-32b8-9f27-a78beb3b8897 | -1.20292 | -55.87518 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcec9f62-0da2-3741-aa06-70b7b40f1ecc | -1.19865 | -55.92896 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f224e926-79d8-35e6-aa5e-8a94f588adec | -1.19809 | -55.93254 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca8af949-360a-3a31-93fd-2f500914d7ba | -1.79687 | -55.67261 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dec9674-fe31-3722-bc2d-1defe210d41c | -1.76868 | -55.55238 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86647855-db13-3d17-b2ba-f8423c5c5465 | -1.76738 | -55.69878 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fded2f55-df6b-3eab-87fa-ce5f7ba5ded4 | -1.76356 | -55.64118 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8d499ce-de40-3611-b687-24429f3ed24b | -1.75888 | -55.2248 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12e6b3fe-2ef5-3bee-a2ca-ed3a5aa5c9c5 | -1.75825 | -55.22881 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b681b924-1ecc-39e5-8f17-fce72e2b8d3f | -1.75595 | -55.66304 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99cbd047-422c-38b2-af1e-64c2e80d30af | -1.74048 | -55.25882 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4ffc6ae-f97c-30c3-b1c0-893637a17c68 | -1.73694 | -54.99647 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa0612df-8c34-368e-bf94-8f1eceb15b6e | -1.63044 | -55.46962 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8492212-a43e-3a6f-bdd5-1e98638562de | -1.62931 | -55.46973 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e13002d-452b-3327-8284-d627924fd757 | -1.59679 | -55.8865 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f39044-f4af-3c1e-9054-860f98928177 | -1.59624 | -55.8901 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed56dfa8-b615-37e8-bc13-cf52872b453e | -1.53788 | -55.47933 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9328b674-e292-3069-afcf-d126c50429e3 | -1.48203 | -55.84672 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceef5140-b242-369b-be86-7f8f40e8c8cc | -1.42764 | -55.07069 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb1f99cb-9727-381b-9169-bf9e9c512cba | -1.40088 | -55.38187 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 042ac51a-e354-3938-9863-ab7e1aa7f7df | -1.40074 | -55.99562 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87221a4c-d228-39f9-85d9-222919973b47 | -1.40028 | -55.38572 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0efe0051-2519-33a9-a4af-cf5b99eb7d77 | -1.39671 | -55.995 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b5f560-c84f-3a91-974d-917aee4b46ba | -1.37647 | -55.85752 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1fd1cb5-10fa-3657-9a96-9db3fa63ee31 | -1.37592 | -55.86111 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 325d603e-0293-3c66-b671-fd6332d4d675 | -1.37537 | -55.86469 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a451dab-739d-3310-96de-2ae858171fa6 | -1.37186 | -55.86045 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a409d4e4-af1c-32f6-a9d6-a01d4dc04517 | -1.37131 | -55.86403 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2f3614-2d0a-3fd7-b4a2-2b457a553888 | -1.3678 | -55.85979 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22ba4c13-4ba6-3bee-8f41-ffd3c77e3bd8 | -1.36726 | -55.86337 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 825efcd1-3386-385d-bb0d-335f25c8c657 | -1.36081 | -55.69131 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 256e093a-e34c-3959-90e7-cf620cc5dbe2 | -1.34227 | -55.14974 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 69022796-5d35-3fd2-b14f-40ce7b7d1db6 | -1.34165 | -55.15368 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7aa7d8f0-1c07-366c-8255-d8cde8979008 | -1.33799 | -55.14919 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7395a1c2-bdf9-31b2-bcd5-f3fe1b8e4c46 | -1.3256 | -55.45315 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e99a062-e2e3-3bf9-8300-7e050bf3e473 | -1.32503 | -55.4569 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2e4ec7-7278-3041-b371-58585f4c0b90 | -1.31816 | -55.82991 | 2024-10-29 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae0970a-0b58-3c9f-aa82-e518cae18f3d | -1.30119 | -55.72346 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed4d1fb-3f09-3854-b631-d6fc1bf591db | -1.29709 | -55.72285 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f311c3f5-2d02-34f1-9826-fa900b39c5a6 | -1.29654 | -55.72649 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7120aea-2e9b-32ee-8bb0-56f69ee5f513 | -1.29598 | -55.73014 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ddaae7-9c7f-3296-8eab-45271dd99296 | -1.29541 | -55.73383 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8cc9e1-079f-3dcc-bb33-b2a2b38b4c36 | -1.29355 | -55.71861 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 845d0557-1608-3f91-aa01-94f8b687495f | -1.29299 | -55.72226 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 963b3274-87a8-3897-af89-9b51d77c1ef1 | -1.29263 | -55.752 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12fba4d-557f-37e8-b2a4-5e674e845d78 | -1.29244 | -55.72589 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4fde6a3-1c4b-3181-8978-555d0c88d196 | -1.29188 | -55.72953 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3d9b86c-1496-3987-9f27-c620c8452e76 | -1.29132 | -55.73321 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef69708a-d067-36c9-8b8d-114cad836263 | -1.28853 | -55.7514 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 870d9965-a3d2-3cf0-865a-419b051208b0 | -1.28778 | -55.72894 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ee3165a-2b22-3baa-b6a1-6605b1e8871a | -1.28001 | -55.77979 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23162fe4-2e79-350b-add2-ef1d0fe03835 | -1.25974 | -55.91241 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e49e78f3-9856-3a7f-b24e-6165c5eb0e4d | -1.2592 | -55.91592 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974d2d4d-a76e-37ae-a76d-6827e19d102b | -1.25463 | -55.91879 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9d69280-46e3-3d0e-a476-ccfc2ca07808 | -1.25004 | -55.86723 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 304afb0c-a4d9-3806-9e9b-86ea0d33259e | -2.13215 | -55.89539 | 2024-10-29 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57482dc6-48d5-3add-918b-74daabf1329f | -2.12395 | -55.89413 | 2024-10-29 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2376f91-ead4-3cff-a579-a73a50164bfc | -2.02616 | -55.77034 | 2024-10-29 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 176e5bd5-fdc7-3733-9341-bcdec4e649c6 | -1.99848 | -55.71368 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42c94930-e7fc-36bf-9d1b-20124f8c642c | -2.46622 | -55.6274 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0dc9c83-b567-3f72-8bce-1e0916c0e117 | -2.27965 | -56.42987 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e30d5ca-e750-35e6-894f-c91af450347f | -2.27887 | -56.43498 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5584799-7d6e-3e62-b5c8-c54769d1fa41 | -2.06081 | -56.86973 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 784a4b66-bd78-3163-a146-be7a05d7ea9e | -2.05912 | -56.86691 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2acea70c-99a6-3d54-acf5-ab142c9989bd | -2.05837 | -56.87163 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce04496-4433-3560-aec9-29cf355123aa | -2.05696 | -56.86916 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea887bf0-17cb-3bc2-bfd4-1475a9396c93 | -2.05527 | -56.86633 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e9a5f5e-c0dd-33cd-b3ab-3cd34d2ebfa2 | -2.05141 | -56.86582 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c314e01-5e7c-3424-a6cf-c4370f8ae6b2 | -2.82952 | -57.67172 | 2024-10-29 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb6a99ed-27da-3211-8cc9-f87f5128e494 | -2.691 | -58.0873 | 2024-10-29 05:25:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16acf46f-03c1-3bb1-8ad6-52b150c3d370 | -2.68738 | -58.0868 | 2024-10-29 05:25:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30abf75e-986e-3a81-931f-8736600e9011 | -2.55978 | -58.11539 | 2024-10-29 05:25:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d77fcb-3825-380e-abd9-d8da0783e286 | -2.55681 | -58.11069 | 2024-10-29 05:25:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 764e72ea-23cb-3dac-b0fa-e05a55dd8c53 | -2.55617 | -58.11484 | 2024-10-29 05:25:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d499f4-b146-31cf-8d44-ed69412f00dc | -2.46705 | -57.52924 | 2024-10-29 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 409a8a03-9cea-3cc3-9471-e81f4b25703b | -3.03154 | -56.94053 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a14b4577-7c6c-3338-8f5f-3a9cdcf1d06c | -3.02825 | -56.94213 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe1a4044-a193-38c8-bd90-71d677179c5d | -3.02765 | -56.93995 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b17874-5dba-36ca-bfeb-f117811d075f | -2.34343 | -57.15351 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a41806ea-8a03-3c80-b567-71713b68f9f4 | -2.34339 | -57.15032 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51d16a2e-c447-3c31-ba4b-a0021580d7f8 | -2.3427 | -57.15815 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64a2fa7b-8a0c-352e-97ef-6808f1e130da | -2.34269 | -57.15498 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8668aa17-a160-3ba6-893b-56d86f12cd26 | -2.33964 | -57.1529 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 554b29f0-1673-37a0-b929-d92fea30ae50 | -2.33891 | -57.15754 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5baf51f-7e37-34b5-aab8-938684afe5bc | -2.3389 | -57.15434 | 2024-10-29 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1138ee94-3213-313d-a92f-24b5d304e322 | -2.32445 | -57.15063 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 370874d9-771d-33f1-b6d4-92ea7318b81b | -2.32065 | -57.15005 | 2024-10-29 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b15b0a2a-965a-3ec0-943e-d533cc2ab4e4 | -2.9794 | -59.21193 | 2024-10-29 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd29ae4-4053-33e3-94e5-ece525b89608 | -2.86764 | -58.37261 | 2024-10-29 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2c909c-c8ca-3965-8a21-cfa3963476aa | 2.557 | -59.97465 | 2024-10-29 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26eeb268-116f-37bd-90e5-e30286da2bb2 | 2.55316 | -59.97173 | 2024-10-29 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ba9511-77bd-3376-89af-2e81609850e7 | 1.10316 | -59.70145 | 2024-10-29 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c12e711-4595-3194-a725-c9db99326a69 | 0.76293 | -59.50492 | 2024-10-29 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc39562a-e1b4-363b-871a-b1c188553775 | -1.7918 | -60.91517 | 2024-10-29 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10649d87-ce98-30b2-821b-de47f15bb929 | -1.71737 | -60.13252 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51f5f3df-9e66-3747-9aa8-7d143cff24bd | -1.71683 | -60.13601 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ad5e6fd-0c81-3745-8fdf-af0fe8644d3f | -1.66996 | -59.96011 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 957be077-3947-36a6-b142-fb4b2764ca87 | -1.6251 | -60.07172 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a2719dd-4be0-3664-8621-6236f2c0f00f | -1.624 | -60.07871 | 2024-10-29 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README96.md)
