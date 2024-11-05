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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be0ee45b-f63a-325b-b9fe-cc17f351dfec | -3.5631 | -47.3847 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 8ce3d135-6780-331c-b66e-8d7d762c66ec | -3.5632 | -47.3629 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b3a593d1-87d1-3243-b601-6faa3903c56f | -5.6944 | -45.8323 | 2024-11-05 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 381509ad-ca67-31d3-9322-1b1eed1056cf | -3.4612 | -45.5299 | 2024-11-05 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a1e951cb-8235-34f7-8da2-8cd49d2ac7ef | -11.8639 | -43.8644 | 2024-11-05 01:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cdc048a4-8c02-3e07-afa1-03c7c5a9c282 | -3.967 | -48.15 | 2024-11-05 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 20e62d24-abe3-393c-89c8-89d2665af7dd | -4.408 | -43.1018 | 2024-11-05 01:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 038b57be-6d24-3ceb-914a-e637818c3b7e | -3.5446 | -47.3855 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 202.3 |
| e2c97cd7-ef84-313e-94fd-6fd5c0f87cf5 | -3.5447 | -47.3636 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e4e902e6-29b8-368f-bd64-7fb92be2a1ef | -3.4798 | -45.5291 | 2024-11-05 01:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 008d5cb0-fba6-3139-b8b6-bb3d4390bdc6 | -6.1041 | -43.9593 | 2024-11-05 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5aaf490a-c0dc-3535-a784-163b0c320718 | -6.1229 | -43.9578 | 2024-11-05 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 841e2fc5-5fad-3ad0-b519-4f8466e7d19c | -3.0906 | -54.5073 | 2024-11-05 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 662a8f2b-e41e-3e8d-aa04-3e5e1985cbf7 | -2.8065 | -51.4855 | 2024-11-05 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 36d2e7d6-e10a-3152-9259-5e9192ad6018 | -4.4268 | -43.1007 | 2024-11-05 01:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4a218f90-3e42-352d-a346-0ac668226f58 | -3.53 | -47.4 | 2024-11-05 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a933d6-0b71-3380-b77c-e0e55d331454 | -4.2459 | -48.0293 | 2024-11-05 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 2b4297e8-b964-3e33-a577-7f36ac7e9c88 | -4.0667 | -46.9246 | 2024-11-05 01:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f3ac7bf1-8d55-36cb-962d-42b1a67a6c9f | -3.5632 | -47.3629 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 87381c18-83d6-39f9-ab11-7d40a7fbc6b1 | -3.0906 | -54.5073 | 2024-11-05 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b5026b7d-40f3-3cc6-b161-4d05c6c09ba6 | -4.7477 | -45.2175 | 2024-11-05 01:10:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c46179cd-7dcb-33e3-8b23-9eb6b410eb35 | -3.5446 | -47.3855 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 300.3 |
| 6af499da-f37a-3885-b0dd-c7f79ea916dd | -3.5631 | -47.3847 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 242.3 |
| b443d872-d282-39b7-8823-cf9eab3b22d7 | -4.408 | -43.1018 | 2024-11-05 01:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b4b80d3d-3f5b-3686-b794-e18ff0e6bc2c | -4.4079 | -43.1252 | 2024-11-05 01:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2bfb6d2d-4f2c-3d29-9513-ec4058033b8f | -4.7479 | -45.1949 | 2024-11-05 01:10:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a2d76d51-a639-3003-9f9e-a0db6d93e586 | -6.1041 | -43.9593 | 2024-11-05 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 23c04b5f-22f1-36ab-b36f-940878106a4f | -3.967 | -48.15 | 2024-11-05 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 6af6cd63-d0da-379e-8041-1c8a94e96602 | -3.5447 | -47.3636 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 4cb80c13-beae-3452-8cbc-17f240670e4b | -3.5444 | -47.4073 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c53486c0-da38-3226-b031-1963c57c84df | -3.9669 | -48.1716 | 2024-11-05 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1de7013d-2ee6-3605-a2de-7ac691b12376 | -11.8639 | -43.8644 | 2024-11-05 01:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5cd623b5-dd4e-33c3-aa54-7ee9d51e5a7c | -4.606 | -46.8758 | 2024-11-05 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c4d2e974-0fe8-3395-ba45-3b978c38f453 | -6.1229 | -43.9578 | 2024-11-05 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| f047bd7d-6f1a-3732-8841-f79d3f480f35 | -5.6944 | -45.8323 | 2024-11-05 01:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d3ed9978-ffa6-3157-9e3f-fff4d4af6136 | -3.563 | -47.4066 | 2024-11-05 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 78457082-f356-3bdc-96dd-20bd7795fe3b | -12.14025 | -48.00824 | 2024-11-05 01:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e5cb07ff-901b-3963-86c7-e573670809cc | -11.85705 | -43.85771 | 2024-11-05 01:13:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 03fd37fc-1a70-3a93-b261-0f83f81e7635 | -12.15085 | -48.00637 | 2024-11-05 01:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c5f38b90-083f-3df6-9f52-615930fbf4d7 | -11.86179 | -43.88557 | 2024-11-05 01:13:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 72f505ff-5642-34f0-a8f4-fa43d188b1b1 | -11.98545 | -42.91036 | 2024-11-05 01:13:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| de0fef83-b043-3168-ac23-2ac9b5ee32b4 | -12.14231 | -48.02143 | 2024-11-05 01:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a86ad157-4461-33bc-a926-65ad0f9f2489 | -10.36503 | -45.08134 | 2024-11-05 01:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7ab3453b-30c6-32d8-86a4-e5075d7904f1 | -11.86138 | -43.87889 | 2024-11-05 01:13:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2d4accc7-9f12-3bf7-a818-3722503d5650 | -3.042 | -53.271599 | 2024-11-05 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5373eb-5d2e-33d7-a581-03cc52609362 | -3.5554 | -47.406399 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4930bdbd-315d-3a99-aa8c-ba6d9eb26c6c | -5.6902 | -45.854301 | 2024-11-05 01:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c94ca18-c566-3569-9026-cf3100aa5352 | -4.0521 | -46.935699 | 2024-11-05 01:15:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4e08beb-6e2e-3703-9ab0-dbf1b0bea730 | -3.0857 | -54.515499 | 2024-11-05 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d588a576-b681-3677-8251-493ea4e59c6c | -2.1239 | -54.634998 | 2024-11-05 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dca05e5c-6990-3f68-a784-b578d7eac0b8 | -3.0838 | -54.507 | 2024-11-05 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 772143ca-40b8-3255-b321-eeae3ed6ac41 | -4.2364 | -48.557098 | 2024-11-05 01:15:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d75f40-ccce-3b56-aa50-6435329c008b | -3.0818 | -54.498501 | 2024-11-05 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 937206a8-07f3-38ce-88ff-0b6beca0067c | -3.5458 | -47.408699 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 394b84de-19ee-3587-a9ae-a9a00a2084f5 | 3.5047 | -51.250099 | 2024-11-05 01:15:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf669c0-517b-3049-a5ee-4342ff0270ab | -2.1259 | -54.6437 | 2024-11-05 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d717c244-47cb-35af-80ca-3fb531d18be6 | -3.0299 | -53.263699 | 2024-11-05 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6d3bf6-f879-3113-864a-ca68dd00ba08 | -3.565 | -47.403999 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0df01c9b-5e43-3279-883e-c6aa9afd0046 | -3.2186 | -53.1026 | 2024-11-05 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0dcedc-0551-3ff4-bdef-c89170e4d509 | -3.0396 | -53.261501 | 2024-11-05 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82057225-36d0-300c-a5c0-1f411d87d296 | -2.652 | -48.566002 | 2024-11-05 01:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0528174f-f4c3-3516-9a47-bcb6ed950b98 | -3.975 | -48.158699 | 2024-11-05 01:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0874587-b5be-3c66-8e60-d2f09a9df25d | -2.6571 | -48.5872 | 2024-11-05 01:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64677f36-4917-3c8d-a6cb-4f150ba38817 | 3.5008 | -51.2673 | 2024-11-05 01:15:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 45eca7ac-5479-37a9-be51-9949239a521a | -3.559 | -47.379299 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c05403b6-8f20-387d-8e34-b2be2d08bd73 | -3.0936 | -54.504799 | 2024-11-05 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e7ea7d-631d-3ecb-b9dc-e1565074e4d4 | -12.1377 | -48.001598 | 2024-11-05 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e8c0a6a-5fc3-3e28-b9a5-636bfc778cf1 | -5.6828 | -45.8251 | 2024-11-05 01:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d8d5cbc-6934-33af-ac8f-b9368bd4f97a | -3.5397 | -47.383999 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee87564-63a7-3184-8149-bfc022ef74a4 | -2.8067 | -51.4884 | 2024-11-05 01:15:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b76c98b-80fe-32e2-a4c4-ee09bb6f5f67 | -3.5493 | -47.381599 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2a4503f-37c7-3a3b-a399-7df81d7a88cd | -3.9653 | -48.160999 | 2024-11-05 01:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2676f6e0-a9c0-3d5d-bce8-aaf255afb21b | -5.6998 | -45.851799 | 2024-11-05 01:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b146bb08-0bd0-3b82-b6a0-5f4c7b8c397b | -12.1418 | -48.017799 | 2024-11-05 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45bef1a2-06ea-38a6-b399-f8af34f3a39d | -12.1473 | -47.9991 | 2024-11-05 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24ec62f5-aa7a-3402-bd31-4c6be68fdbcc | -4.2315 | -48.537102 | 2024-11-05 01:15:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 360d48c9-b866-301c-9cb5-de40386f4f70 | -3.5432 | -47.3568 | 2024-11-05 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265dff03-3038-3337-9177-72695fd3e20f | -3.0916 | -54.496201 | 2024-11-05 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5601d4-1eed-3bfb-b8a2-3261aa3ddf36 | -12.1515 | -48.015301 | 2024-11-05 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 927064ce-08eb-3602-800b-5379ba836d10 | -5.47431 | -48.61296 | 2024-11-05 01:15:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| c07b8320-88fa-30a3-9b7b-6a5861def0e7 | -3.55681 | -47.41829 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d99ee731-9d68-37b4-b3b7-0096d7769874 | -3.4761 | -50.37433 | 2024-11-05 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 082ef08e-302b-3e1b-aff8-7283846bff65 | -3.55369 | -47.39768 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 349.0 |
| 8cddc7ff-25e9-345c-845c-9d84cab9c325 | -4.06203 | -46.93993 | 2024-11-05 01:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c19aa7a3-0632-3078-9987-04f0aab65be1 | -3.70445 | -47.61401 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 04948cc8-50b5-3801-bdbb-dd1f3035534d | -5.21925 | -47.47638 | 2024-11-05 01:15:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| fe202822-267d-3f60-853f-f499773b574e | -5.69538 | -45.82092 | 2024-11-05 01:15:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7f5090b8-107d-3354-963f-7f0316257ca1 | -3.95549 | -48.15002 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 35c3cb0a-1d61-376c-997e-51625546bd06 | -3.55313 | -47.38274 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 329.2 |
| e1b2f307-a160-3d29-8fc2-a6f24d4349c8 | -4.04865 | -46.94208 | 2024-11-05 01:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 002326c5-6468-3a0a-80d2-e9ba21b659f2 | -4.60109 | -46.86449 | 2024-11-05 01:15:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| dda7b6e6-73e8-38ec-b3fa-09d4625aacd5 | -3.543 | -47.40484 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 15e4f2b9-dc23-327e-9f7c-645510e19081 | -3.96767 | -48.14837 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 3708e2cc-1435-3afb-8b4f-1cd9a6d499fc | -5.47454 | -48.62199 | 2024-11-05 01:15:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a7680197-1f63-3cb8-855e-cce21da617b0 | -3.97026 | -48.16582 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ab0e6ace-570a-3b24-aabd-59cffd28f8f5 | -5.69212 | -45.827 | 2024-11-05 01:15:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3c1ba206-90e1-3cdf-8771-7d838e69fb24 | -4.1121 | -47.96879 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 84679692-320d-3b8b-aa41-68d40a68efb5 | -4.74514 | -45.22326 | 2024-11-05 01:15:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b60dcf4b-ac69-320f-8a84-1f9cb0c4ab3a | -3.47784 | -50.38646 | 2024-11-05 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d246765c-2c1d-3fc4-b34a-7342e49304f9 | -5.83372 | -43.66082 | 2024-11-05 01:15:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |


[Clique aqui para ver as próximas entradas](README9.md)
