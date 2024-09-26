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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9bbfb6f-b7f5-3da2-b5c5-e5093b5e0dba | -1.8824 | -54.8843 | 2024-09-26 00:57:51 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37916ded-bdef-3978-8f7a-ea658ad2ab08 | -2.1728 | -56.128201 | 2024-09-26 00:57:51 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef7908b-175e-3818-9ec6-9433f896833f | -3.8215 | -54.1175 | 2024-09-26 00:57:53 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50415cad-4b99-3ce4-94c0-32b9cd29f808 | -3.8231 | -54.124298 | 2024-09-26 00:57:53 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e16edc23-927a-3ffb-983e-bf1bd50503fd | -3.5173 | -52.82 | 2024-09-26 00:57:53 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 238b9cd4-e7e2-36d5-b041-53670c48bea6 | -1.1136 | -52.1712 | 2024-09-26 00:57:53 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ed85d07a-b9ea-325f-bf2b-74235ad7669c | -1.1118 | -52.1633 | 2024-09-26 00:57:53 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| aa41d6c5-93d7-3c6c-b152-4386600b8fa4 | -3.4421 | -52.716 | 2024-09-26 00:57:54 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97664b64-1c7a-3cf1-8268-0c057542719c | -3.4437 | -52.723202 | 2024-09-26 00:57:54 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b52c9b50-5d15-39d2-89bd-82ab7b56d6aa | -1.5285 | -54.275299 | 2024-09-26 00:57:54 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40ec754f-5437-371c-bcf2-c59304156206 | -3.0057 | -51.076401 | 2024-09-26 00:57:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ff55a6-193a-3864-a125-3e39240809a7 | -3.0076 | -51.084801 | 2024-09-26 00:57:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507ea8ac-ed3c-3628-a1cd-b3b3c0314f61 | -3.4164 | -53.192799 | 2024-09-26 00:57:56 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 419b088b-2c79-333d-9ef8-4a701bd91a90 | -3.418 | -53.199799 | 2024-09-26 00:57:56 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e64252e-b33e-3d74-a117-9c0e06584fa6 | -3.325 | -53.198399 | 2024-09-26 00:57:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4156bbb7-3af6-3e29-90d5-cbc162772bf7 | -3.3282 | -53.212502 | 2024-09-26 00:57:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31ffda2-e9fa-3f85-892e-b7464f072c8c | -3.3152 | -53.2006 | 2024-09-26 00:57:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b68627-64e1-3345-9f04-f35c60bdbd11 | -3.3168 | -53.2076 | 2024-09-26 00:57:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12aab3a4-3624-3fb7-8908-ee4719cabda0 | -3.3184 | -53.214699 | 2024-09-26 00:57:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed85b5c5-c722-36f1-8b52-074f1e2f3e94 | -3.3893 | -53.709999 | 2024-09-26 00:57:59 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520fc1a4-0b98-3a4c-9973-9a986ea732d9 | -3.3909 | -53.716801 | 2024-09-26 00:57:59 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d36284-dbb5-339b-b198-6e5c237ef8f4 | -3.01 | -52.176399 | 2024-09-26 00:57:59 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 946de02d-559e-342a-baab-7107a1917364 | -3.0118 | -52.183998 | 2024-09-26 00:57:59 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fee1693-9466-347d-8be4-e39aa8933058 | -3.2558 | -53.302399 | 2024-09-26 00:57:59 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5d1a17-1b45-3f22-9e47-73e4e4dafb8f | -3.2574 | -53.309399 | 2024-09-26 00:57:59 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b543ff-b89a-32a9-a9b7-dde32bc41f6a | -3.259 | -53.316399 | 2024-09-26 00:57:59 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 285ea62d-4d34-3ae5-bfc8-0dc4d689dc2e | -1.3361 | -54.654999 | 2024-09-26 00:57:59 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523b291b-8e99-3242-8f21-4b1de1326253 | -1.3346 | -54.648201 | 2024-09-26 00:57:59 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ebb2a9-0649-338d-a288-5889e56690c5 | -1.041 | -53.350399 | 2024-09-26 00:57:59 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec80d602-d037-3be7-8176-31d6b50d042c | -1.0394 | -53.343201 | 2024-09-26 00:57:59 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcdc2966-22e3-3005-a574-1148dbfec7ad | -1.0525 | -53.355301 | 2024-09-26 00:57:59 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87f3249-fe2b-3a37-8510-ca00d66319ea | -1.0508 | -53.348202 | 2024-09-26 00:57:59 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e941b80-4b9e-32f5-992e-e5f25060f65e | -1.0492 | -53.341 | 2024-09-26 00:57:59 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd07119-7f23-3d1b-b78d-002e8d069d79 | -3.3512 | -53.769001 | 2024-09-26 00:58:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f9243d-b563-3463-9b30-56a1d016ee9b | -3.3527 | -53.775902 | 2024-09-26 00:58:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ae90a3-e5d6-3e6b-8db6-54c67acab433 | -3.3429 | -53.778099 | 2024-09-26 00:58:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cac164-aecf-36e0-ac77-34847dcb1209 | -3.312 | -54.919102 | 2024-09-26 00:58:04 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a77e090-7770-305a-89e2-1e11b1727afd | -2.9555 | -53.7052 | 2024-09-26 00:58:06 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 842c1288-d1f1-39e2-9628-67c1331645f0 | -2.3907 | -51.2686 | 2024-09-26 00:58:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f37d77f-504e-3d29-8ba0-0004ae55f2a7 | -2.3926 | -51.277 | 2024-09-26 00:58:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d623f1a3-e767-355c-9af2-17204420a9c1 | -2.8542 | -53.3036 | 2024-09-26 00:58:06 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79423173-a958-3ed4-8d80-61684bc8f9ab | -2.8558 | -53.310699 | 2024-09-26 00:58:06 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d2b1c1-a4bb-346d-ab29-bc8c8de4db2c | -3.7269 | -57.187599 | 2024-09-26 00:58:06 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6d0f697-85fa-323d-9f41-40766e84590d | -2.3828 | -51.279202 | 2024-09-26 00:58:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af8b3ca-bc84-392c-bfad-2ef1e81b9c81 | -4.2228 | -59.853901 | 2024-09-26 00:58:07 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83860d3a-e224-3fab-9ad5-57e8a5e97546 | -4.2254 | -59.865501 | 2024-09-26 00:58:07 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 942ee89d-a790-3f17-b920-b869987e02b1 | -2.8721 | -54.156399 | 2024-09-26 00:58:09 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ddd95aa-6507-32ad-9550-aaa2f8be2904 | -2.8736 | -54.1632 | 2024-09-26 00:58:09 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 386f5e1a-74fc-33bb-a792-59ad1dbe7d52 | -2.7717 | -54.7159 | 2024-09-26 00:58:12 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5c1e42d-e289-3e8d-8e0f-664ee9250711 | -2.7732 | -54.722698 | 2024-09-26 00:58:12 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32871cbe-205a-3c61-9608-815a0d8c0b92 | -2.7355 | -54.738201 | 2024-09-26 00:58:13 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7d56903-1798-3fe7-9ea0-e1ff59ae4eda | -2.6541 | -54.605999 | 2024-09-26 00:58:14 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a04289e-d192-38ea-addf-dacd4d5032af | -2.6557 | -54.612801 | 2024-09-26 00:58:14 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7a6f58c-3da6-360c-a326-852aa5b18b06 | -2.6572 | -54.619598 | 2024-09-26 00:58:14 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5968d2e-b84d-337a-a16b-44f1d4519045 | -17.65 | -40.24 | 2024-09-26 01:03:40 | MSG-03 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e16f427-7541-3bac-9e08-1f8a51cd0690 | -17.65 | -40.2 | 2024-09-26 01:03:40 | MSG-03 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfffe1f6-07c5-37a3-8c8f-69f74830f5ff | -14.44 | -45.26 | 2024-09-26 01:04:01 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 349bcbfb-62dc-30ab-b806-95388914dc2c | -14.44 | -45.21 | 2024-09-26 01:04:01 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7bc73c-e005-3e67-be9f-c9b5ec52b3e6 | -12.8 | -51.31 | 2024-09-26 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdbbf853-e48f-306c-a9d1-866d9a7b2655 | -12.8 | -51.25 | 2024-09-26 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a33e885d-03f3-3826-bf7d-aa7eb3c8b82c | -12.77 | -51.3 | 2024-09-26 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32466841-8e1f-3dbd-9790-1e1489f7a42a | -12.77 | -51.24 | 2024-09-26 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1a347a0-1caa-34db-b918-5a0d304da2e5 | -10.04 | -53.48 | 2024-09-26 01:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cde999c-9e19-33eb-9e9a-cd61f7f6acba | -7.37 | -55.57 | 2024-09-26 01:04:43 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece8117e-ade6-382a-9571-201940c5dcbe | -7.37 | -55.5 | 2024-09-26 01:04:43 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baa7baa-32c3-3736-8172-cae2bc11dc70 | -1.0369 | -53.3555 | 2024-09-26 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 32bc095b-18f6-3aa4-a708-b04fb49b6dde | -1.0553 | -53.3553 | 2024-09-26 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0931c8d9-a35d-3493-9e4d-83be4edf596b | -2.6601 | -57.5507 | 2024-09-26 01:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a63415b5-6628-3858-8e10-b29e23e7e180 | -2.6785 | -57.531 | 2024-09-26 01:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 596f0e7b-c63f-3ea6-867a-8e624e98b20d | -2.6968 | -57.5307 | 2024-09-26 01:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2cd33da5-c7b4-332c-8a1a-c89926890963 | -2.8795 | -51.6695 | 2024-09-26 01:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0f377b09-468e-31cc-ad89-5411b80c7315 | -3.3158 | -53.2122 | 2024-09-26 01:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 01b8ec3d-fb00-3875-a10d-fefe11064679 | -3.3342 | -53.2117 | 2024-09-26 01:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 6a6af951-5696-3ec6-a76a-301a107f5bce | -3.5488 | -50.38 | 2024-09-26 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 68c34354-784d-36b8-a50f-a58721eac27c | -3.5673 | -50.3794 | 2024-09-26 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| edd5c8f3-186d-3877-82ba-5c1f73ecb78a | -3.8008 | -41.5989 | 2024-09-26 01:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 46c29fbe-52ea-31c9-b880-67d8fdc985d5 | -3.801 | -41.575 | 2024-09-26 01:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| a9d8859e-a2bf-3f93-9fea-5c525b352ef8 | -3.9208 | -46.4459 | 2024-09-26 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| fcfe69cd-d6a3-3f97-ae24-21bc869658cf | -5.212 | -47.9577 | 2024-09-26 01:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0fe248aa-2e84-3461-b2f5-ad7f74630901 | -5.943 | -52.1241 | 2024-09-26 01:05:40 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ba3f9f10-8ca5-3eba-972a-f8b9f4218e2f | -6.5772 | -60.0437 | 2024-09-26 01:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ec164ac3-1e9e-3534-b4bf-7071f2074725 | -6.7839 | -59.3245 | 2024-09-26 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f6f90e60-ca61-3c4e-8bb2-21656300ed03 | -6.784 | -59.3052 | 2024-09-26 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2d63826c-1d70-3b4a-9aae-0718ff040348 | -6.8023 | -59.3237 | 2024-09-26 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f658314a-bd1f-3288-aafa-12e0365580a3 | -6.8024 | -59.3044 | 2024-09-26 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 4e92113b-6a37-38f7-8f77-20002e3fb8b1 | -6.9305 | -63.1241 | 2024-09-26 01:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9081f88a-a80b-3b8e-993e-5290b728dccf | -6.9306 | -63.1053 | 2024-09-26 01:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 194ef187-01f5-3ec3-b102-76a1c1ed1bc1 | -6.949 | -63.1048 | 2024-09-26 01:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5a6a635b-bb3e-30b0-8711-31f63c3dfed4 | -6.9681 | -62.9349 | 2024-09-26 01:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 43e2b9aa-41fe-3598-983a-945ffc3b2df0 | -6.9682 | -62.916 | 2024-09-26 01:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 21598bd9-7a87-3835-a18e-8c7f757aa282 | -7.2905 | -61.106 | 2024-09-26 01:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| a0688fbc-2812-319b-a284-d223366af622 | -7.2906 | -61.0869 | 2024-09-26 01:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1b378a2c-9914-34f2-9fc1-89d98f59349b | -7.797 | -54.7263 | 2024-09-26 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c9569615-cd80-3b64-bf52-5179c94b0bb0 | -7.8156 | -54.7252 | 2024-09-26 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 30581df3-c27e-386b-a1d7-8a5e06a0dae8 | -8.3153 | -55.0157 | 2024-09-26 01:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b92afdf4-aaf3-3d89-9f9d-18c69df8a9a9 | -8.3155 | -54.9956 | 2024-09-26 01:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 4ca18ea3-4e6c-377a-a809-318c79acc047 | -8.5542 | -63.1814 | 2024-09-26 01:05:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b9595451-99af-3952-b138-fc53ae42a4b1 | -8.7087 | -54.7881 | 2024-09-26 01:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1baa7f56-fc05-3082-bde7-47c2235b72d8 | -8.8098 | -58.2172 | 2024-09-26 01:05:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e2b264c7-6271-387a-bc3a-31e987ae8709 | -9.0657 | -61.3743 | 2024-09-26 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |


[Clique aqui para ver as próximas entradas](README31.md)
