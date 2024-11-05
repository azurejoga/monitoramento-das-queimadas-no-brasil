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
| f1b5da1a-483f-3cd4-9600-0a99cb78e0cf | -2.65147 | -48.56539 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d3f3c9b4-b009-3585-92f0-309bfd945979 | -4.59823 | -46.86985 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52f34132-de00-39be-b79e-e081ca2abcb9 | -3.55749 | -53.14963 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69e0e699-1212-3ce0-8feb-eebb626ea9fb | -3.90251 | -46.44174 | 2024-11-05 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a992d2f0-0146-3f5f-a4ad-ede83252cbfc | -4.91613 | -44.36573 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1220fd6-4fae-3043-ac08-22eec77e52c7 | -4.25726 | -50.72736 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8ac0716-fc81-3019-bd88-1edfd57f05e3 | -3.54576 | -47.38856 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 851a7c6a-f22d-3142-bd0c-c838bfbe4850 | -2.81231 | -52.94135 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7fb0c90-bec9-35ba-9123-4dcd545e875c | -4.26441 | -50.7285 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a735ab75-0555-3064-8d59-92b0055a2cd3 | -4.60658 | -48.91066 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088d1336-db62-369c-9d96-b78fbc8b9d03 | -4.50549 | -45.64775 | 2024-11-05 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61589ec3-6c49-394e-a072-1ed82cd48b9c | -3.5383 | -47.37882 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 771364b4-b345-3ace-92fa-5f7a978339bd | -2.64697 | -48.56821 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1acd5c2a-5360-3b75-b40b-c9f36de31798 | -2.38745 | -50.60412 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c50275b-6b13-30c8-920f-3ec9668bf6e7 | -3.34277 | -50.25256 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731a241d-b363-3b15-8974-4013cfc98ddc | -3.55695 | -53.15307 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d6b942-1e40-3407-8969-83e07fc00c22 | -4.26925 | -50.72088 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f5524f-1aec-3425-8c6e-959a667deb4d | -4.07654 | -48.31258 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d313d19-68a1-3553-88f8-080cbcf51bd7 | -3.11957 | -51.10895 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41d92f90-4cb7-3e43-972a-30765ebb9975 | -2.6157 | -51.30494 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8198db00-c712-34ea-a929-f5b2cb138b3b | -3.08981 | -54.50108 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 481b6cf3-732a-3499-8439-49f572ee9fe4 | -2.28619 | -50.67422 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a64f0878-792a-3e28-8a67-12a988df830b | -2.75539 | -53.21777 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933e7025-5587-3067-89aa-dae4cc4abf29 | -4.77306 | -43.6465 | 2024-11-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aebd726-b795-3cea-baab-21f62388998e | -3.06471 | -49.56609 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8357cb99-1510-379b-a210-0bf4510421bd | -2.64927 | -46.76958 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a34a7b1e-13b0-3b8e-a64f-ab1efbc42ad8 | -2.91022 | -48.59745 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72710fab-41f1-3fad-ad00-771003fbaf08 | -3.40979 | -54.51949 | 2024-11-05 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f00a9d0-4964-3bc0-8cbf-96c208d05a23 | -3.03123 | -53.25771 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38a3e6fc-fe8d-395f-8fb2-4247e425aa72 | -2.90264 | -48.62074 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c8ab97-83e0-3724-a186-25dfae928189 | -5.81156 | -44.13515 | 2024-11-05 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1340f145-005b-34d3-9b05-eea2e375d14b | -1.86446 | -50.79921 | 2024-11-05 04:55:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb86e98c-2af7-3d2b-8a11-6f7305b080bd | -2.78613 | -51.6069 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58db120b-8527-3729-b774-b5ccd52e4c25 | -5.22739 | -47.47519 | 2024-11-05 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5abcadbc-3c71-319a-918c-7c8e193a3daf | -3.54638 | -47.38441 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 1d8066f0-b091-303a-8229-97cfba8ad947 | -4.60147 | -46.87971 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffef360c-078e-3ba2-9ab2-a68854133702 | -5.37295 | -46.45626 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291cd309-81dd-30fa-9b4d-c996380f89e6 | -5.69085 | -45.83332 | 2024-11-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c721dab-bd61-3727-a0aa-42cd9cc08182 | -3.29145 | -50.02864 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 697aa1e5-a508-3e07-9463-1041937acff8 | -4.219 | -47.39733 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a5d3c3-25ce-34c4-a3c3-c0b6503bd49a | -3.09496 | -50.26024 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1269f334-5b7e-3f53-89c1-a2068455ee59 | -3.06514 | -49.56901 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6c5ffa6-8a97-3593-b2c1-644ac2c81bcc | -3.21836 | -53.10346 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4a9fbc9-6c57-3aba-a472-4d5f1c7e0d95 | -3.85537 | -52.14029 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e978377-ab4b-341d-bc27-405ac7124bec | -3.29579 | -50.0249 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e867d7-d6a2-39bb-a4cc-b17489af8722 | -5.29814 | -46.26174 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a74d0a5-5f40-3f3a-b527-df26add11503 | -2.21553 | -50.68393 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f127cb-c397-3058-bf0e-f4db67eb3ec1 | -2.60539 | -51.30338 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ab69dee-7ab4-38a6-b4ea-4c82abf80ad0 | -3.03346 | -53.2651 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1c31dabc-f29f-3d0c-b643-6858bf9d8231 | -3.08203 | -54.50706 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cea4a92-b6d1-3f40-bdd0-c3c0e5c759d0 | -4.63051 | -45.66956 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc825a2c-94ac-34d8-bacd-c3048476828b | -2.927 | -48.62097 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deec0f6e-1ca0-340b-a370-fdf8066a35bd | -3.55011 | -47.38927 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 12e744d5-054f-3967-813b-3aa59c96f175 | -2.65942 | -48.56658 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d705fea8-f51e-374e-9d2e-d9ddc535271c | -2.77933 | -51.60585 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da2935b-a663-30ee-8de3-4a5c117c49a2 | -3.54266 | -47.37949 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97856193-cb6c-3009-a690-b36564d156a3 | -2.81285 | -52.9379 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a4f7e61-74f4-3683-959f-47ec5e4c7c74 | -2.9748 | -53.26996 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88e55359-725f-3b93-8e81-a234443750b0 | -2.62062 | -51.72683 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b15d77f1-16b8-3f73-a0a3-e33e3efdc486 | -3.04559 | -53.27402 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa3ff4b8-ae56-38cd-80fc-c2e496ea608a | -4.3657 | -47.23108 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12000652-6e83-3cab-913f-8435e26587a1 | -3.12305 | -51.10947 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94d17ff4-3806-3890-9613-c7db5b705aa0 | -5.21994 | -46.72516 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf94f98a-865d-3a96-ba57-8885997a846d | -2.21464 | -51.67646 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ef74650-b1ed-345a-9076-048baf44d762 | -3.08537 | -54.50758 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a27f1593-9211-3647-9187-bbc9b7d4e091 | -4.23331 | -48.54097 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fac2f3a-34e4-3956-b9c6-ad6455a1c264 | -4.24614 | -50.3633 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd528116-e227-3f5d-b81a-449b7cad2baf | -3.07758 | -54.51357 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a6b220b-1ef7-3bce-8120-a826aa94aa9b | -3.21384 | -53.06749 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94aab485-cebc-3a42-a472-256db2bf9e91 | -4.38657 | -43.11879 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852c31f9-ad91-3212-b799-d75f6477ae45 | -3.96326 | -48.15056 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dc549dc-6a49-301f-a10d-7c96b35f78bc | -5.44519 | -48.20869 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a324ed0-e550-3aa5-b78d-194f55dc032c | -2.64993 | -46.76514 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 571bb021-54af-360a-8f53-6f56a8629ca1 | -2.65201 | -48.56196 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 594613c1-bbcf-3c24-ac9c-5653ebecb268 | -3.88142 | -52.3157 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 079e32cd-5abf-31b7-b07b-f5ceec3f9436 | -3.30541 | -47.01512 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c545f98-235a-365a-a991-08434171f4a1 | -5.23883 | -48.14325 | 2024-11-05 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d6bb7bd-b992-31e2-a58c-453d52ee0f75 | -6.09949 | -43.95721 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 175d6b03-ace4-35ef-a318-2177c46e38b1 | -2.65028 | -48.57309 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5096094c-33c4-3908-9eb5-30ac956aa4be | -3.08944 | -50.27218 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 432dcb3b-0ffe-3ff1-b28d-185bf8b31bb9 | -2.86714 | -49.39331 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df7351e-f091-3a7b-bfbb-57f2801cd1f3 | -2.40161 | -50.30744 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63297df4-328f-3246-8cdb-6f06a2acf986 | -4.26084 | -50.72794 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45fb8f33-1d20-37b1-a2f0-1be4d8cf7ed2 | -2.6685 | -48.5084 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa7378c4-6686-3386-9a7f-b0eb58d35433 | -3.97045 | -48.15939 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c19e424-5c31-3ab8-b67c-d08459c8ded1 | -3.75048 | -46.14576 | 2024-11-05 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c648b7-fed4-3fc0-94fb-7ae50cde1d37 | -3.02703 | -53.26048 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd6dd1a2-ecc8-329b-8b46-0f2e6291731c | -2.17688 | -48.85438 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b21fed29-1589-38fc-91b7-ae70086a0ebc | -3.0307 | -53.26115 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 931322b7-1d21-3145-a76d-dc05b6f35c40 | -2.42595 | -50.40134 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e398cefc-cdfb-3a2b-a43c-9f1bdd05dda1 | -5.1988 | -48.23816 | 2024-11-05 04:55:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28ec8bc-b614-3809-a2ac-dc0717e775a7 | -2.2496 | -50.53598 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a1758b5-f6f5-34cd-a547-e31a46c427ba | -2.63888 | -48.03019 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93f5ea2f-7b7e-3f26-8100-6cb31287bfd4 | -3.64103 | -51.78791 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff17248d-2bcb-30ee-85e9-13ad0fbb81df | -3.55571 | -47.38168 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a665add5-80a9-358a-8608-909ae3e99ce1 | -2.90977 | -49.41865 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5512c33-4755-3032-bab6-55621ddce9bf | -3.11897 | -51.11279 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5528615f-dc11-3cbd-827b-62361d42e02f | -3.11994 | -53.12366 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ead0b994-8a3d-3ff0-9843-c0ed389a7ff7 | -2.10516 | -51.09455 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e481587-2c8c-3c18-9cfb-ccd8a04f1ac2 | -4.23277 | -48.54461 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
