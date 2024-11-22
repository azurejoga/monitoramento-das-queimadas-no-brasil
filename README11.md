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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb5c51cd-34d4-3740-970a-5c3578f14d13 | -3.4778 | -45.9096 | 2024-11-22 02:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c10faa9b-d26d-30cf-86a4-0f69441b9030 | -1.1857 | -51.948 | 2024-11-22 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 088a670c-d6d6-32ec-a130-32918196993c | -1.2041 | -51.9683 | 2024-11-22 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3695ecaf-7b58-3eb1-8095-b955c0c2417f | -2.5013 | -48.9949 | 2024-11-22 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 57997c12-7ec8-3c1a-bd0b-f03cdbe71c03 | -3.774 | -46.1196 | 2024-11-22 02:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 66ba62ef-107a-3e21-b337-072db22790a1 | -3.1831 | -54.3247 | 2024-11-22 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3fff43d1-ed8e-3fd8-81af-18457cc33565 | -2.9984 | -45.1207 | 2024-11-22 02:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| cdf31922-f320-32dd-b3a8-0a3dffbaf1b9 | -3.3266 | -50.5132 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 22b6fb46-f504-351a-990a-ab443578466f | -3.3635 | -50.512 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ba0e4342-984b-3c44-ba2c-a0f0483e898d | -3.3267 | -50.4923 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| be3f3d1b-151e-377a-9b6a-48314fff6bf2 | -3.5159 | -53.8132 | 2024-11-22 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1e40d6e2-c079-3f67-a4aa-6b6a531a08c0 | -3.516 | -53.793 | 2024-11-22 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 3cb54ae4-7ef5-3d3f-b385-2df2fd62dbb2 | -1.1287 | -53.3951 | 2024-11-22 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| fbe1a192-ee6b-3a31-bc23-cffd90572776 | -1.7366 | -52.3916 | 2024-11-22 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f3e8ebf1-81dd-39db-b575-0c8aba2dd422 | -3.3452 | -50.4917 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3c3dbd43-a7ba-330e-a3c7-651ece7f5cf1 | -1.1287 | -53.4153 | 2024-11-22 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1c9582e9-4cd0-3ab3-9de2-008b828022f4 | -3.8355 | -52.2576 | 2024-11-22 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ecfdd4a8-307f-3cb1-b646-432026ffefa7 | -1.1857 | -51.948 | 2024-11-22 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 65b3095f-44dc-3ca0-842e-1710e4463860 | -3.6181 | -44.0473 | 2024-11-22 02:20:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d2ad1c2e-f3ce-3350-99d6-48b77138d2d6 | -3.2768 | -53.8199 | 2024-11-22 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| cb89137d-41e3-31ea-9b00-779fd8a49bb4 | -3.3636 | -50.4911 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5c6dea40-421c-3163-8a9c-7dcdb008db1b | -3.7554 | -46.1204 | 2024-11-22 02:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 213.4 |
| a3d6d6f4-0df7-358d-ac8d-e5b31312b183 | -3.4592 | -45.9104 | 2024-11-22 02:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a01814a3-b1dc-370e-a5d2-e5a267b6324c | -3.3451 | -50.5126 | 2024-11-22 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 20912296-de01-3adf-a9b4-fa8b4af97b1f | -1.2041 | -51.9478 | 2024-11-22 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 8e675d4e-1927-3c52-97cf-3a5e469ddc45 | -3.2569 | -54.2426 | 2024-11-22 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| c0a67ac1-51d1-361e-8589-177b7b174468 | -3.7554 | -46.1204 | 2024-11-22 02:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 9177ae19-4222-3bcb-b51e-c1c1aef190de | -3.2386 | -54.223 | 2024-11-22 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 5e1465ec-2779-3cd8-b88a-64f38be4d630 | -3.5995 | -44.0481 | 2024-11-22 02:30:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cbb34b8b-7b17-3546-810d-bcc2a700450d | -13.2549 | -50.9022 | 2024-11-22 02:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c2093a50-14d2-3373-8f00-a18b931a8d2f | -3.516 | -53.793 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f91c7c22-0b23-3922-ab5f-ae07767552fe | -3.3451 | -50.5126 | 2024-11-22 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| a0ed777e-976b-3709-b202-8201ac3f72a2 | -3.3635 | -50.512 | 2024-11-22 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 71da77e0-f044-3daf-87f2-8f9a7b6d8829 | -3.2385 | -54.2431 | 2024-11-22 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 336.2 |
| 48d0a829-1430-38ae-b978-ad3711f47d6b | -3.6367 | -44.0464 | 2024-11-22 02:30:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2d027542-3e47-3561-a2f9-f6a6e33528f9 | -13.2357 | -50.9046 | 2024-11-22 02:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b378450c-f9e2-39f4-aecd-e3896ccf81ff | -3.4975 | -53.8137 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5aa1dbd2-9012-3331-ac2b-525437fc42b4 | -1.1857 | -51.948 | 2024-11-22 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 45f96b36-6908-3553-ac07-99d74ff7ee2e | -3.5159 | -53.8132 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0dfb19fa-f807-34f9-89ef-4b98e205bdd4 | -3.331 | -54.08 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2b2806d0-6abf-3c80-91e1-6457fbda8dfe | -3.8355 | -52.2576 | 2024-11-22 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b5f597ca-97b0-35a8-a45f-934814f5641d | -3.2384 | -54.2632 | 2024-11-22 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| eb2b6ff1-7af6-3f7c-906e-a1e75d87ebcd | -1.1287 | -53.4153 | 2024-11-22 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7681b843-de71-32b1-9cf6-717a2bf5db64 | -3.774 | -46.1196 | 2024-11-22 02:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d8809df9-1558-3324-9c68-04ef4052666e | -3.3309 | -54.1001 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 5eaedd95-93e2-35f4-b466-924f1b583d55 | -3.4976 | -53.7935 | 2024-11-22 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c499d771-3dd8-35bb-a75e-9e2b8dccd14b | -3.6182 | -44.0243 | 2024-11-22 02:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| de0c077a-8751-3d32-89ee-281ddd82ea74 | -1.2041 | -51.9683 | 2024-11-22 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 0eef8801-21fe-314b-b6e2-5265dbca9632 | -1.2041 | -51.9478 | 2024-11-22 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 8a76935b-4ec2-3636-877d-6ba2f57a0566 | -3.618 | -44.0702 | 2024-11-22 02:30:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ac757409-c0d1-305d-959d-976e104c18aa | -3.6181 | -44.0473 | 2024-11-22 02:30:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 84b487e2-d96f-3c63-9002-3ecb8fac5d82 | -1.1287 | -53.3951 | 2024-11-22 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 2333d32a-10b1-3040-bbee-23ba8bb99ae5 | -3.2201 | -54.2436 | 2024-11-22 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 8a8959a8-155c-3b98-ba53-252c94d0a084 | -3.3452 | -50.4917 | 2024-11-22 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b6be4b00-fbd1-39ce-8231-e778ad45abfc | -3.22 | -54.2636 | 2024-11-22 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 92da5a15-15e9-3169-8a51-b30fee3c435b | -3.774 | -46.1196 | 2024-11-22 02:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 355cee81-1935-3ba3-ace4-695f865dc6b5 | -3.516 | -53.793 | 2024-11-22 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 53e71f6d-aa3c-3647-9298-c44202b5d5a7 | -2.3549 | -48.5493 | 2024-11-22 02:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 333a7736-664d-3467-beb6-67df08edf1d8 | -2.9983 | -45.1433 | 2024-11-22 02:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 59cd6544-20b3-3de3-9e20-2323c2fdf789 | -2.9984 | -45.1207 | 2024-11-22 02:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| dbf7a2c2-a510-3e19-97a9-c248371a64e0 | -3.3309 | -54.1001 | 2024-11-22 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 221c3237-f82e-3bea-940b-dd67041272f1 | -3.6181 | -44.0473 | 2024-11-22 02:40:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 402915fb-9922-3e2b-ad60-27b8a3760176 | -1.2041 | -51.9683 | 2024-11-22 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| de159321-a069-3ba8-953e-458c77204799 | -1.1287 | -53.4153 | 2024-11-22 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| aab1e02e-a486-34bc-bfbf-8370249b2314 | -3.5159 | -53.8132 | 2024-11-22 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8f6a2495-0868-3c71-b61b-18b56dcea95a | -1.1287 | -53.3951 | 2024-11-22 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 419f9dc9-dce3-3cb2-937b-af0c4e30ecda | -3.3452 | -50.4917 | 2024-11-22 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3b20cd6c-9b31-3a66-8c2b-f757483bd2bf | -3.4592 | -45.9104 | 2024-11-22 02:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0423c1cb-e026-3f77-900e-22cb1b3899f1 | -1.2041 | -51.9478 | 2024-11-22 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7030a2c9-e71e-3314-b8a9-20ab63d6b816 | -3.3451 | -50.5126 | 2024-11-22 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 49bc9bc0-a2aa-3011-873a-58fbe8297de2 | -1.1857 | -51.948 | 2024-11-22 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5d122971-9ad3-324c-8bb8-8d06e33852cc | -3.7554 | -46.1204 | 2024-11-22 02:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 128.9 |
| af4aeaa8-33ae-3996-ab60-619cab55c4ce | -3.4975 | -53.8137 | 2024-11-22 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8637c9f9-467f-31b9-9d05-ec3b03a8c478 | -3.4976 | -53.7935 | 2024-11-22 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c6c58b18-132a-3f4f-9fb9-3978659f5ebd | -1.1287 | -53.3951 | 2024-11-22 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 76fc8bb5-5b2e-3c6b-9a5a-fe429a795491 | -1.2041 | -51.9683 | 2024-11-22 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b3bd473a-dd17-3454-aeb4-e36afc523e13 | -3.774 | -46.1196 | 2024-11-22 02:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 54b43383-6afe-35b9-be0d-2dfcab50cbbe | -3.8355 | -52.2576 | 2024-11-22 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| aa723814-a946-32ef-a9c2-af9e6cc39f32 | -1.1287 | -53.4153 | 2024-11-22 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2fe5ccab-220f-337b-9695-17feb81d1195 | -3.4975 | -53.8137 | 2024-11-22 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| ece946ac-51b9-30d6-963a-8f1a5799698f | -13.2549 | -50.9022 | 2024-11-22 02:50:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| be81f6da-39b5-3d02-bee0-30f1bb29d978 | -2.9984 | -45.1207 | 2024-11-22 02:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d3fe23d7-5d85-3fe2-aa1f-3376ac34e86d | -1.2041 | -51.9478 | 2024-11-22 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f5b009c7-99ec-3cd7-8365-0c229575dcc8 | -2.3549 | -48.5493 | 2024-11-22 02:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 91f9da45-e960-3e09-a642-65456db686ff | -3.516 | -53.793 | 2024-11-22 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 0e5d6f16-e3dd-38bd-a7d1-f381eaff8aff | -1.7366 | -52.3916 | 2024-11-22 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5edb98ab-6040-3cec-8cc3-374d0bf7ff98 | -2.9798 | -45.1214 | 2024-11-22 02:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ca0710de-c8c2-3003-ba58-d03f33a9c987 | -3.4592 | -45.9104 | 2024-11-22 02:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e9f3cc85-0ddb-3251-991b-fc8af711ff38 | -3.3451 | -50.5126 | 2024-11-22 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| eddbe9f9-24aa-382b-80e5-23fdd221808c | -1.1857 | -51.948 | 2024-11-22 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1bba35bd-ed03-34dc-a64d-f4858fa137df | -3.5159 | -53.8132 | 2024-11-22 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e692f121-8fb8-3b7b-b10e-fdb87c85593e | -3.7554 | -46.1204 | 2024-11-22 02:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| d30af10c-4cda-3fcc-9dde-d0c86035613f | -3.2768 | -53.8199 | 2024-11-22 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1d0cd085-e8bb-38c6-84c4-fed5a4e742f7 | -6.19239 | -37.44067 | 2024-11-22 02:55:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a115f89c-4f37-3cd0-b5a0-d7cd630335f5 | -6.91627 | -37.11397 | 2024-11-22 02:55:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1a2e0b4-396e-33c3-8682-8b11edfde573 | -8.84555 | -35.71316 | 2024-11-22 02:55:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0f175210-360d-3980-9c6a-7aee7af4c4a2 | -8.83955 | -35.71203 | 2024-11-22 02:55:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 000743af-4864-3093-a581-b6ca13ef4363 | -8.36789 | -35.35902 | 2024-11-22 02:55:00 | NOAA-20 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f8812e91-6cc5-3a1b-948f-69605325d042 | -7.78191 | -34.93996 | 2024-11-22 02:55:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 57a54511-1c92-3869-8750-c4bf3e1f78db | -6.92086 | -37.11452 | 2024-11-22 02:55:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
