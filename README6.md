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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a702ae7-5e52-3f41-8be5-248bffd5eac5 | -2.6391 | -48.561298 | 2024-11-03 00:25:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d91ff6d1-2d0c-3fde-9cfc-78c6b37e9d02 | -2.5404 | -48.169399 | 2024-11-03 00:25:57 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd51af6a-6236-3828-a18e-81832293c6be | -2.6268 | -48.552399 | 2024-11-03 00:25:57 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df77564e-231d-321d-9fb4-e9300bb443aa | -2.6293 | -48.5634 | 2024-11-03 00:25:57 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b3cf30-8b18-3f81-83fa-56b4e3400881 | -2.6318 | -48.574402 | 2024-11-03 00:25:57 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53050950-02ac-3958-af54-f537564108c4 | -2.6343 | -48.5854 | 2024-11-03 00:25:57 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a1def71-4571-36e0-b4c5-ce2d0dbf352f | -2.8367 | -49.4842 | 2024-11-03 00:25:57 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 276dd753-88ad-3f92-affc-ea40a064edb8 | -2.0742 | -46.3414 | 2024-11-03 00:25:57 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc52be1-c367-3ed5-9d06-a487cb298118 | -2.0761 | -46.349499 | 2024-11-03 00:25:57 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7cdc9d0-8812-3571-931e-d802ba3706a9 | -2.7066 | -49.315399 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0983adb2-b2b2-3ec1-9065-c6ae8ae31ffc | -2.0681 | -46.359798 | 2024-11-03 00:25:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2593a33-58a2-3a49-8ed9-7d505df4d7cd | -2.07 | -46.367901 | 2024-11-03 00:25:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e3836e-672e-328a-9981-b3c88047b108 | -3.1157 | -51.094398 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf9d8c1-3f9b-398a-a676-4cb6d06b43b6 | -3.1194 | -51.111 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e1dc71-a937-3300-a5e9-5c295df7fbd1 | -2.701 | -49.290699 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03afb393-02dd-3a00-8d1d-ec09483e76ef | -2.7093 | -49.327702 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 909e85d8-d832-366d-9ca1-b319a5e1ee52 | -2.7121 | -49.340099 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33d1a9f9-4f52-390c-9066-ad287cffc159 | -3.1059 | -51.0965 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00946ada-c53e-3f56-af48-2f0ec1ad343d | -3.1097 | -51.113098 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0fceeea-d03d-3f31-992e-a8be455a39d5 | -2.6968 | -49.317501 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596cab72-2c5d-3a1b-8345-e2c29152178b | -2.6995 | -49.3298 | 2024-11-03 00:25:58 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5678975b-9a41-37e1-891b-fafae304b5b1 | -3.0962 | -51.098598 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b69f95-1f90-32e3-baec-26e222bab61f | -3.1 | -51.1152 | 2024-11-03 00:25:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72073ba-0f0b-3b27-ab8f-4bc65573947b | -2.6254 | -49.091599 | 2024-11-03 00:25:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2006ea78-3446-3c02-907e-a37413189d71 | -1.997 | -46.590302 | 2024-11-03 00:26:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed75182b-dc27-31a2-8e71-6270fa74870b | -1.9989 | -46.598598 | 2024-11-03 00:26:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccaef27-452e-3804-b5ec-759dea48f528 | -2.7217 | -49.837898 | 2024-11-03 00:26:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d2b2750-aa71-3137-89fd-ce41a640fca9 | -2.7247 | -49.851299 | 2024-11-03 00:26:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46d3e50-fd93-3c00-83d6-28a1569e0e26 | -2.7149 | -49.853401 | 2024-11-03 00:26:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f15c39e-6bcb-335e-baf8-08d2b5e018c8 | -1.8317 | -46.045399 | 2024-11-03 00:26:00 | METOP-C | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b525e09b-746b-38ea-a0dd-27f438a1f83a | -1.8334 | -46.0532 | 2024-11-03 00:26:00 | METOP-C | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79dcff53-f9f5-3d02-8b85-f925a4e82602 | -2.0785 | -47.129398 | 2024-11-03 00:26:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfcd4d3-2214-3aa1-80a5-f54915d0c94e | -2.0667 | -47.122601 | 2024-11-03 00:26:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4abcad5e-09e3-3063-82c5-acaa12133ce8 | -2.0687 | -47.1315 | 2024-11-03 00:26:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f247d961-47f1-3e95-88ee-136723bc6e89 | -2.5325 | -49.225201 | 2024-11-03 00:26:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ce7506-8d18-3c91-a09c-1bd12d62dc4c | -2.4876 | -49.072102 | 2024-11-03 00:26:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb98d54-3c7f-398b-a6f0-dc1700fd43f8 | -2.406 | -48.846802 | 2024-11-03 00:26:01 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6547c51d-d32e-34ab-ae04-7027e1884080 | -2.4086 | -48.8582 | 2024-11-03 00:26:01 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05f47b2-6e11-36d1-90ee-46e2bcc1ef85 | -2.4112 | -48.869598 | 2024-11-03 00:26:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dabaabde-7e54-3273-bc11-57b596e02b6e | -2.3988 | -48.860298 | 2024-11-03 00:26:01 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a221fb-8858-3dbf-979a-8df1f969c35b | -3.2613 | -52.708 | 2024-11-03 00:26:01 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2c156e-cc89-38db-bbc4-79d1d274e929 | -3.2661 | -52.729698 | 2024-11-03 00:26:01 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc6d99d0-cc26-3b89-8263-5103f81945a7 | -2.2515 | -48.254398 | 2024-11-03 00:26:02 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1d8b9a-bcc0-30ea-a431-57d2e448181d | -2.2539 | -48.264801 | 2024-11-03 00:26:02 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ca58da-bfb4-30a2-8d39-a32b4079f390 | -3.2516 | -52.710098 | 2024-11-03 00:26:02 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa9a136-8fad-3ef7-8b29-e39238f3c6c5 | -3.2564 | -52.7318 | 2024-11-03 00:26:02 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1bc035e-b03b-3467-ad3e-0be407444995 | -2.1988 | -48.1581 | 2024-11-03 00:26:02 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c388250e-e52a-31e5-9708-e91631157227 | -2.8982 | -51.444599 | 2024-11-03 00:26:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc68e24e-5be1-35f5-8825-4adfe531b7a6 | -2.9021 | -51.462101 | 2024-11-03 00:26:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202fc4f5-0c37-363e-8bd7-a259fbef0715 | -2.8884 | -51.446701 | 2024-11-03 00:26:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca0927d-f459-3b69-a567-c261afe1b557 | -2.8923 | -51.464199 | 2024-11-03 00:26:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a75b651-afce-31ec-8a6d-5b44cb8abf49 | -2.2806 | -48.791302 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3514d30a-ed14-30d0-8ee9-047302039184 | -2.2832 | -48.802601 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0385fb-bbb7-3c62-ad1f-5b6e1586b726 | -2.2857 | -48.813801 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25fe3d98-5a6c-3434-97a7-ac19c49cb06f | -2.2708 | -48.7934 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99506667-7745-33de-abcb-87b11a787ca4 | -2.2734 | -48.804699 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70c1249-a3c4-3f84-9e19-c9c726a92b27 | -2.2759 | -48.815899 | 2024-11-03 00:26:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff86953b-5fcd-3891-9738-36f8649e607f | -2.8705 | -51.730999 | 2024-11-03 00:26:04 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a7d7bcc-3d22-37b1-a62b-881e43292b19 | -3.2387 | -53.383202 | 2024-11-03 00:26:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b45e2e93-99e5-366c-81ec-36a986c8d8f6 | -3.2441 | -53.407398 | 2024-11-03 00:26:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 725cf8b8-5412-32f3-8884-4b7b26970714 | -3.229 | -53.3853 | 2024-11-03 00:26:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c373aa59-8c65-3ad0-a241-f848e4eb383a | -2.7857 | -51.579601 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78dd4749-e954-33b7-886e-b4fd7450a4b9 | -2.7897 | -51.597401 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b9c89a-ff9d-3616-9251-e5cccead008a | -1.9539 | -47.938801 | 2024-11-03 00:26:05 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc617271-b52b-3afb-8a8b-db350569d1c8 | -1.9561 | -47.948601 | 2024-11-03 00:26:05 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fefa734e-de18-37a1-aafa-591ae292be72 | -1.9583 | -47.9585 | 2024-11-03 00:26:05 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069a6635-d6fa-3aad-b70a-bf6442b2fad2 | -2.7759 | -51.581699 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d400f5f0-6a2e-3051-afa5-72ed49d35992 | -2.7799 | -51.599499 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae2f2f3-c754-3af3-a490-2819dd0917b3 | -2.7839 | -51.617298 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b98ab666-6e25-3634-ab53-325714f10740 | -2.7702 | -51.601601 | 2024-11-03 00:26:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc043237-6e64-37bc-80ce-ca5a224597c4 | -2.1928 | -49.173901 | 2024-11-03 00:26:06 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5fdcae-ab1e-3be7-ac4c-d468dbee2686 | -10.8426 | -49.1453 | 2024-11-03 00:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3a560281-4a8a-3531-91c2-f9ede4d7973b | -10.8616 | -49.1431 | 2024-11-03 00:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fe3621d6-a9a4-39df-918c-49eb11301e3c | -3.0222 | -53.230701 | 2024-11-03 00:26:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01e00ab5-dea3-31b3-84b1-794e3f544ea6 | -3.0275 | -53.254101 | 2024-11-03 00:26:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 682340cf-607f-37d1-ae99-2c4289658feb | -1.6485 | -47.364899 | 2024-11-03 00:26:08 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 895a15ef-24f0-3bc0-8616-fe041d158345 | -2.7886 | -52.457001 | 2024-11-03 00:26:08 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5cfeea4-7e7d-3d4d-94f3-b2d772c26f39 | -3.1105 | -54.219601 | 2024-11-03 00:26:09 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8850eaf7-1e00-3d39-ad6e-a0d963baa372 | -3.1166 | -54.247101 | 2024-11-03 00:26:09 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d25dd1-c1b5-3a1e-b1b3-bb400f0d2956 | -11.2819 | -56.144 | 2024-11-03 00:26:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6fac3d4e-8f0b-3f53-a330-11745b821520 | -3.0573 | -54.116901 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5c3ca1-8d5d-31b5-9c9e-bcaf6b015164 | -3.0633 | -54.143902 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9d66c3-b24e-3c98-9dbd-4ae92902f8cc | -3.0477 | -54.118999 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47906f1c-375c-3d63-b7d7-241093663f29 | -3.0537 | -54.146 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8650d75b-1038-3d01-b6d6-76d52c434eb7 | -1.4806 | -47.215 | 2024-11-03 00:26:10 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8150771f-bd0e-35d8-8dd5-1189678d0262 | -3.038 | -54.121101 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c3afb2-046c-3a78-b3d0-b4ee33407b7a | -3.044 | -54.148102 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fba23b86-772d-3577-9667-8424fc07da1a | -3.1009 | -54.221699 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6865c6db-fd50-3c26-a4cc-4e5fd041220e | -3.107 | -54.249199 | 2024-11-03 00:26:10 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2063cda-70e9-3a19-a2ac-d532616be06a | -3.073 | -54.141899 | 2024-11-03 00:26:10 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afbfc76f-3051-3c57-9a24-1e92da701f49 | -3.0308 | -54.179401 | 2024-11-03 00:26:11 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1eaae1-aa49-30d3-b820-80e441073ae0 | -3.0211 | -54.181499 | 2024-11-03 00:26:11 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98639a05-dddb-3548-9471-9d12097c008e | -1.3665 | -47.436699 | 2024-11-03 00:26:13 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 836eae53-b7b5-337e-b993-31a9e87b07a9 | -1.3686 | -47.445702 | 2024-11-03 00:26:13 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 932d0a67-0801-3f46-9a8d-3cf45de2a31f | -2.7492 | -54.413502 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecab2d48-f30f-3f75-b988-e63af4ec1c01 | -2.7332 | -54.3876 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3359c93-98fb-3cef-bb64-aaabc9b86a3b | -2.7395 | -54.4156 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb0985fe-6a4a-3959-9a9f-dbc51299c822 | -2.7457 | -54.4436 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba50c97-f00f-3235-90cc-7a9bae5001d8 | -2.7236 | -54.389702 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ed05eb-0fd4-39db-8fb7-734b5deea344 | -2.7299 | -54.417599 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
