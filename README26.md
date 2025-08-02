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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e55d676-b481-3233-be49-4911fd6fa945 | -8.0132 | -43.1278 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 49ed5965-a8b1-3527-827a-667dcc68fc89 | -14.1672 | -45.4673 | 2025-08-02 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 96454482-c8ea-301d-a22e-75d6765880d3 | -12.6784 | -44.5085 | 2025-08-02 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 4ebe2f0e-721c-3abe-8811-e4ceb46f8ccc | -8.0513 | -43.1001 | 2025-08-02 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| a86297dd-e513-33f6-b571-3c1411b4beb4 | -8.0132 | -43.1278 | 2025-08-02 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 41ea5377-c053-36b7-bbf3-b0bab5b42861 | -10.4764 | -46.9654 | 2025-08-02 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 96ef0cd2-644c-3801-b64b-f829f6e1f5d9 | -8.0321 | -43.1257 | 2025-08-02 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 442.0 |
| c966b64f-1b5c-3403-8d01-b4ae6caed1bc | -14.1672 | -45.4673 | 2025-08-02 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e185d7d9-43c3-3b18-8915-7138d836bc91 | -10.4574 | -46.9677 | 2025-08-02 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2653e01c-9542-34c4-9e53-60cd6eda365e | -8.0318 | -43.1493 | 2025-08-02 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 9eb01b33-d089-36cc-bfc4-18c02579d89b | -12.6784 | -44.5085 | 2025-08-02 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 78c112b3-b378-3536-8a52-bf12d8435c3a | -8.0324 | -43.1022 | 2025-08-02 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 244.8 |
| 01dc3d1e-1c62-3135-99b0-5dddfac4b1ea | -11.9403 | -44.9264 | 2025-08-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f1078328-9495-3fc3-80c7-748872697ec8 | -8.0132 | -43.1278 | 2025-08-02 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 287.6 |
| e11d1507-6b84-3273-88df-3f19b83de94f | -8.0321 | -43.1257 | 2025-08-02 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 535.1 |
| 08645fc5-ace5-355d-95fd-e78dd7e2f24f | -8.0513 | -43.1001 | 2025-08-02 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 10baf9a2-5f2b-39c3-a3bb-1b015055d9f6 | -8.0318 | -43.1493 | 2025-08-02 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 024f0872-c91d-3c01-9d58-e6cb95abc036 | -12.6784 | -44.5085 | 2025-08-02 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 3bfbde12-9b11-3c96-8097-b7e94e67ba47 | -12.678 | -44.532 | 2025-08-02 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0093e010-de27-3bc9-8119-0c52d186850a | -8.0324 | -43.1022 | 2025-08-02 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.0 |
| ad3971b8-505d-3d36-b4c9-6ca7efe4213d | -6.5287 | -42.8036 | 2025-08-02 13:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 71d78b4f-a0be-3f5a-9287-281340e4fe04 | -11.9403 | -44.9264 | 2025-08-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f1939278-602c-341a-b49e-180cc2babf01 | -12.6586 | -44.5351 | 2025-08-02 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d79dfa8b-1ddc-31ab-ab9f-552cbd93f809 | -12.6784 | -44.5085 | 2025-08-02 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| d320137c-9499-36f6-ae75-ee64ba058891 | -8.0513 | -43.1001 | 2025-08-02 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 977e722c-c7f4-3c3d-ba38-8f592dc7b340 | -12.678 | -44.532 | 2025-08-02 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ddb294d9-7366-3792-907c-6d4504f48d73 | -8.0324 | -43.1022 | 2025-08-02 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 231.5 |
| c0a13a94-2171-36e0-9479-4b7830a923ed | -8.0318 | -43.1493 | 2025-08-02 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| c9aea114-24f1-3315-a139-96f8a819a05f | -12.6595 | -44.4882 | 2025-08-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 4532ea02-1da6-32d3-bac4-02ee28a3da33 | -8.0132 | -43.1278 | 2025-08-02 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 382.2 |
| c35844af-38dc-3775-919e-2fd7f74c05c6 | -12.6402 | -44.4913 | 2025-08-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 286eb189-12be-34fe-8abc-28daea25984c | -8.0321 | -43.1257 | 2025-08-02 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 629.8 |
| 7ef516cc-8587-321e-a9a0-017dd3dac54f | -10.4574 | -46.9677 | 2025-08-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2355ed13-234d-3483-816a-39efc1ca05ff | -10.4764 | -46.9654 | 2025-08-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 99bd52c9-c24f-3d15-9eaa-e0a2bf40c099 | -8.0324 | -43.1022 | 2025-08-02 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 196.2 |
| b0e2d5bc-fe32-36a8-8a6f-910e3695b605 | -12.6789 | -44.4851 | 2025-08-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 33c0adbc-dbdc-3083-ae10-d1effc483f6b | -10.4577 | -46.9453 | 2025-08-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7345410c-08bc-3b7b-8d35-54114561733a | -8.0513 | -43.1001 | 2025-08-02 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| e4661f82-5cee-30d5-b1ba-3ddb7c26372b | -12.678 | -44.532 | 2025-08-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| fae983f1-6df9-3daa-9ca1-8e894837606c | -8.0318 | -43.1493 | 2025-08-02 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 42611dfa-4028-3c76-bcae-45312318fe0c | -12.6586 | -44.5351 | 2025-08-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 65b6596d-91cb-3226-8e86-fce2f00c851d | -12.6789 | -44.4851 | 2025-08-02 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| b4132a99-ef27-31fe-a667-cd53965490ea | -11.5102 | -44.3401 | 2025-08-02 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| d5b2dc1b-f140-3260-8663-8dc496b037a1 | -8.0321 | -43.1257 | 2025-08-02 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 836.1 |
| ffb7bc26-b11d-310d-950c-0848e41a6ed0 | -11.5106 | -44.3167 | 2025-08-02 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 0965b80d-1aee-3206-8c4e-64aad02dab03 | -14.1872 | -45.4406 | 2025-08-02 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 27ba7e94-6e44-30da-ad3a-bc6a2e2c7858 | -12.678 | -44.532 | 2025-08-02 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 381b86f8-e565-3a34-8775-822e27dcb74a | -8.0513 | -43.1001 | 2025-08-02 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| 4e4af999-e4d8-37fb-91c2-58070f7464ae | -14.1682 | -45.4208 | 2025-08-02 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d8e6f375-6406-3677-81a1-b51b3a23bc13 | -12.6402 | -44.4913 | 2025-08-02 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 9f128f0c-d682-3357-a3c9-b0a8d8712944 | -12.6586 | -44.5351 | 2025-08-02 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5b07311a-7b7d-330e-aa6d-e5f5b2e2ba5a | -8.0324 | -43.1022 | 2025-08-02 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 359.3 |
| cc8febe7-232a-352a-9e0a-8ae4a10cfe3a | -8.0318 | -43.1493 | 2025-08-02 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 213.9 |
| c4b1d71f-178c-3f5e-bda5-9c5ac5684659 | -12.6595 | -44.4882 | 2025-08-02 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 200.1 |
| c67f001b-55c1-3568-afa3-8b758274e506 | -12.6402 | -44.4913 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 86281fbd-cb9c-3556-bea3-49181dbedc22 | -12.6595 | -44.4882 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 303.7 |
| 6ab7df91-aafd-330b-a4e5-9f185fe5bb29 | -11.5102 | -44.3401 | 2025-08-02 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0061060a-02d8-3135-b19a-686b4c5865db | -14.1872 | -45.4406 | 2025-08-02 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 211.1 |
| a6780f6e-0af3-3718-853c-b79bff9fbfb2 | -8.0324 | -43.1022 | 2025-08-02 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 259.1 |
| b01dee37-3f35-3f82-a039-e4d9255d142c | -12.678 | -44.532 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 85601895-ca4f-3950-af62-46ec094828f2 | -6.5287 | -42.8036 | 2025-08-02 14:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| fd7d8494-feb1-321e-83ad-6b44e7a67f71 | -12.6789 | -44.4851 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 36034e4e-2f9c-3c45-8514-6fb5de2e9bea | -9.1937 | -45.2886 | 2025-08-02 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ff38932d-74b8-382f-9c07-a8ae86526c1a | -12.6586 | -44.5351 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| afe325d2-dcd7-39ca-9901-0438a532a947 | -11.5106 | -44.3167 | 2025-08-02 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1d276de6-6228-32d0-990b-0e004560d7da | -11.5294 | -44.3372 | 2025-08-02 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8d43ca3c-c616-3fca-872c-e4261596def8 | -8.0318 | -43.1493 | 2025-08-02 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 489fda6e-1cfc-3eb0-a077-9d59367ce35e | -8.0513 | -43.1001 | 2025-08-02 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| ffa0219d-1af0-3158-8af1-708dc085ea0c | -14.1682 | -45.4208 | 2025-08-02 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 16cae6b6-127b-3135-b0f5-7177aa138605 | -12.6398 | -44.5148 | 2025-08-02 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 802cac96-b94a-37b1-9414-d4d3df1e59ad | -9.1937 | -45.2886 | 2025-08-02 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5c77a2c2-a743-33a3-bd04-b0dc50bf38ab | -12.6698 | -48.1038 | 2025-08-02 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| fa759286-ac99-35cf-9231-1fd893f6da73 | -8.0324 | -43.1022 | 2025-08-02 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 258.0 |
| c70b550e-c26b-361c-9ef7-ff24e1d02d8f | -11.5106 | -44.3167 | 2025-08-02 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c88d3ac8-0740-3d4b-b543-9dc33eeaa195 | -14.1682 | -45.4208 | 2025-08-02 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| de29a2a6-3a0a-35cb-9a07-23a9772b666d | -12.6398 | -44.5148 | 2025-08-02 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5f14d944-b301-3b90-830f-1fc39a5be789 | -12.6789 | -44.4851 | 2025-08-02 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 93d8459f-0da3-3bb3-9f4d-2711810b20de | -6.7997 | -43.8312 | 2025-08-02 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 0445b77d-6b27-36cb-832c-f5e6df99b5b6 | -12.6402 | -44.4913 | 2025-08-02 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 7a7d01dd-f1dc-317b-bde0-e72352bf4b33 | -11.9403 | -44.9264 | 2025-08-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f8b98ad6-581c-34ed-9ce2-46650647043b | -8.0513 | -43.1001 | 2025-08-02 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.1 |
| b4ff6d14-0ccf-353f-9e7a-50b097c3492a | -11.5102 | -44.3401 | 2025-08-02 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 8b12a008-42d4-3593-a70b-5f4e28608580 | -11.5111 | -44.2933 | 2025-08-02 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2f6fd9ee-9652-3537-8250-71a9d6e5eb23 | -12.6586 | -44.5351 | 2025-08-02 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| ca1932ac-0c8b-3a3c-9a33-24a6a6533bb9 | -11.5294 | -44.3372 | 2025-08-02 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3bddfe20-8f0f-3ff9-901a-18bdfd59836d | -8.0318 | -43.1493 | 2025-08-02 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.7 |
| 9ac6a4ce-a0cb-3924-861b-3eda25a8c825 | -12.6595 | -44.4882 | 2025-08-02 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 458.7 |
| 2038566e-046f-3d1d-b8cf-d45da23c3c68 | -14.1872 | -45.4406 | 2025-08-02 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 5ba7d535-6e1d-325a-96a7-f2a7d7d988e0 | -14.1872 | -45.4406 | 2025-08-02 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 53fbb85e-8d38-3e5c-833f-a55a8224722d | -12.6402 | -44.4913 | 2025-08-02 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 326.2 |
| e5652909-cfa0-30f3-8313-2556a7a25d8b | -11.5106 | -44.3167 | 2025-08-02 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 4292f6a0-30b3-333f-bbd9-0cca6f1a91b5 | -8.0132 | -43.1278 | 2025-08-02 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 491.3 |
| 1c589f23-e791-39cc-847e-16157b4aa76f | -8.0318 | -43.1493 | 2025-08-02 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 216.0 |
| 5b86e8f1-c60e-3658-b773-1b4fe40b2445 | -11.5111 | -44.2933 | 2025-08-02 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f92f4dca-ff1f-38f9-9448-64a5c5a1a5cb | -14.1682 | -45.4208 | 2025-08-02 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| a4644194-71d1-34c6-bc91-8a5409954697 | -12.6586 | -44.5351 | 2025-08-02 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| f86349ec-390f-35fc-a5c5-f9fe429eacd6 | -6.7997 | -43.8312 | 2025-08-02 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| bc2044f7-6872-3946-bbe1-bfbc7fec83b8 | -12.6698 | -48.1038 | 2025-08-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8fbc305b-4d2e-3b71-9830-a79eabc9503f | -11.5294 | -44.3372 | 2025-08-02 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7fea6c13-771a-3531-b72a-078e29ec0c8e | -11.9403 | -44.9264 | 2025-08-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |


[Clique aqui para ver as próximas entradas](README27.md)
