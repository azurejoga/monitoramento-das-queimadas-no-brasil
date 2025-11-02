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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20684184-264c-3b8a-b9f7-223433177125 | -16.9496 | -49.7138 | 2025-11-02 00:00:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 29e66e18-b1a3-334a-97f7-ec98b8c7be96 | -4.6775 | -44.6089 | 2025-11-02 00:00:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| accfab61-0b1a-3470-a57e-0e14635f62f3 | -13.4976 | -61.4452 | 2025-11-02 00:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| d4812537-1919-3662-ad17-67e86eeb98fa | -16.9298 | -49.7172 | 2025-11-02 00:00:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 385934fe-f3f3-3fd2-92f4-6d8a9939f3b1 | -9.9631 | -44.507 | 2025-11-02 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e5bc81bf-de7a-397e-a7c8-cdb05b36171a | -4.6773 | -44.6317 | 2025-11-02 00:00:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 1747f2a2-bb38-3a94-9d08-c07ffc41e261 | -4.7257 | -45.6914 | 2025-11-02 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f39e03ea-32ca-3f7b-8297-74bd540d10a4 | -4.7071 | -45.6925 | 2025-11-02 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b74a6416-e542-35f8-a65c-6ebdedb6a9f2 | -3.017 | -49.4482 | 2025-11-02 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e5a212d5-9868-3744-8ae2-2ff056383631 | -4.5829 | -44.7966 | 2025-11-02 00:00:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 200c047a-495b-3014-899c-97db9da2f0f3 | -5.1354 | -43.3818 | 2025-11-02 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e8261460-27bc-3dcd-b4ed-b2a6bc0a6e8b | -12.3782 | -63.8821 | 2025-11-02 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 44d6d8d1-d019-3fb0-ada4-04a4c68fd3b1 | -1.9579 | -52.1012 | 2025-11-02 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 53358b95-0b8e-345b-bbd0-98d03c677240 | -16.9303 | -49.695 | 2025-11-02 00:10:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cf95e3d6-1301-3506-a5bd-28839308c467 | -1.9579 | -52.1012 | 2025-11-02 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2f4e75de-1103-324c-9ac0-7baab3f8bccf | -3.017 | -49.4482 | 2025-11-02 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4b41f71a-6a73-3d3e-a2a0-5839d7d82c74 | -12.4405 | -63.1331 | 2025-11-02 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5f18771f-72ab-3172-8792-cf845c7189e6 | -4.6775 | -44.6089 | 2025-11-02 00:10:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a3a13699-6608-37ec-b350-d93bc226f23d | -12.3782 | -63.8821 | 2025-11-02 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c96950e1-4a13-3633-a32f-b9697d615851 | -9.9631 | -44.507 | 2025-11-02 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bb28a365-342f-3807-bf61-e623d3e0e7cb | -10.9701 | -44.6271 | 2025-11-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 0d109632-f611-36e4-98e9-80af28b1bfa1 | -4.6773 | -44.6317 | 2025-11-02 00:10:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7b79bff2-59cc-34cb-997c-384ac7a08ead | -16.9298 | -49.7172 | 2025-11-02 00:10:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 0a36bfa5-ae9e-3fb4-9994-5e5c195c5524 | -3.6581 | -50.7112 | 2025-11-02 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 81a7ad11-51ec-3f9e-90a4-a0574ba2ea2d | -16.9496 | -49.7138 | 2025-11-02 00:10:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 1c78332b-53a5-3af2-8b36-5a47fa6d6dbc | -4.7257 | -45.6914 | 2025-11-02 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8a3d87e5-1dd8-329d-b5c4-70b0da248b87 | -3.017 | -49.4482 | 2025-11-02 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0bcecade-e7d6-3759-9615-9cb44dd0991b | -9.9631 | -44.507 | 2025-11-02 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a10cd8b8-bf39-3190-8a28-9c0e5663fadc | -12.8725 | -50.8647 | 2025-11-02 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| acf07cc7-0f38-3466-8f46-9d9520116580 | -12.8917 | -50.8623 | 2025-11-02 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5bc72545-d4cf-3f4a-b382-ab9b273abf2a | -4.7071 | -45.6925 | 2025-11-02 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7e6dd2d1-2f7c-3ba9-b4f7-bbc9f17581d6 | -3.5497 | -54.5752 | 2025-11-02 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d4f8dea9-f429-302f-baa9-167898fcd839 | -12.3782 | -63.8821 | 2025-11-02 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b589d30a-c086-32ba-b75b-6eb2b789460b | -16.9298 | -49.7172 | 2025-11-02 00:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8626f3ee-55c2-32ce-8f71-11add81b8f19 | -16.9496 | -49.7138 | 2025-11-02 00:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8f810364-9a3e-3422-954c-fea9a6039818 | -9.5152 | -40.331 | 2025-11-02 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| d0693648-cba1-35c3-aafc-e04d564aa337 | -9.5156 | -40.3061 | 2025-11-02 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.5 |
| f67388e9-3677-3eaa-8387-18952868899b | -12.8722 | -50.8862 | 2025-11-02 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8397c74e-e246-3fcf-9dda-2a67c5673510 | -3.6581 | -50.7112 | 2025-11-02 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 211689fe-b10b-36ad-bb7f-caed54994c50 | -4.6773 | -44.6317 | 2025-11-02 00:20:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 33b25a31-1a92-30a1-a153-ca74fe64abee | -4.6775 | -44.6089 | 2025-11-02 00:20:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 7b72d513-5ff6-3515-9230-59d3ebeb8153 | -14.0161 | -43.4703 | 2025-11-02 00:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 46b1dd7b-bb58-31c1-9763-a952bdb7149b | -4.7257 | -45.6914 | 2025-11-02 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7add6fef-e795-345f-af28-966076403be6 | -16.9298 | -49.7172 | 2025-11-02 00:30:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 59d052c5-0774-349d-a93e-687d6980aa51 | -16.9496 | -49.7138 | 2025-11-02 00:30:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2dea27b9-cd67-3623-9446-61336bc20722 | -4.7257 | -45.6914 | 2025-11-02 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 792b338d-f996-3ec9-81fb-182fb6e3efd7 | -4.6961 | -44.6078 | 2025-11-02 00:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d2f4676b-2368-3e09-8226-83d8a5bf7f7d | -3.6581 | -50.7112 | 2025-11-02 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fddef110-bf11-32ea-bc57-ad25e7c472cf | -12.4405 | -63.1331 | 2025-11-02 00:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 30573e15-4dbe-311d-9dee-649f08fd7224 | -13.4976 | -61.4452 | 2025-11-02 00:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 87d3ca4d-582e-3259-8150-1b29e3a4f3b3 | -9.9631 | -44.507 | 2025-11-02 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| d5882b66-11e4-31fd-8026-65c77a2395bc | -4.696 | -44.6306 | 2025-11-02 00:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 573288ef-5f4e-3e0d-a1d4-2d36f1fbeb08 | -12.8725 | -50.8647 | 2025-11-02 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 89a8b9b3-a0f2-3b36-8796-99cf57f1fd5a | -4.6773 | -44.6317 | 2025-11-02 00:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f331caf1-1789-3961-94a0-2daed994e504 | -4.6775 | -44.6089 | 2025-11-02 00:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 1cea90eb-9503-39be-8dee-05543d7bd91f | -3.017 | -49.4482 | 2025-11-02 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 72741363-418f-3024-8574-c08ea5e1e0a4 | -16.9496 | -49.7138 | 2025-11-02 00:40:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6f59c151-67d1-36bc-877a-9dcac69e7ac6 | -10.4321 | -44.9079 | 2025-11-02 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 896b59f3-e4db-333d-92c8-ae85ec3e458d | -3.6581 | -50.7112 | 2025-11-02 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b4eaa7a9-58f4-3227-8dbc-774301505353 | -9.5156 | -40.3061 | 2025-11-02 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.1 |
| c8400c68-7809-3b27-8289-c11ff22fc950 | -4.6773 | -44.6317 | 2025-11-02 00:40:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 503f8be5-8bca-3a29-a199-438ab1e0c4b6 | -10.413 | -44.9104 | 2025-11-02 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8cd24fae-ee4a-37b6-b870-6238bd332926 | -16.9298 | -49.7172 | 2025-11-02 00:40:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 95253313-ca83-3375-a0a4-a9b23ebb4d95 | -9.5152 | -40.331 | 2025-11-02 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.5 |
| e04816cd-deeb-33bd-9d8b-e1c8cbc9018b | -10.4324 | -44.8848 | 2025-11-02 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b7e496b0-06f6-3113-a7b1-a95b2e841720 | -6.8582 | -38.7119 | 2025-11-02 00:40:00 | GOES-19 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 96ac3cea-5f9d-365d-b444-ed59bd3a7974 | -9.5343 | -40.3282 | 2025-11-02 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 93d038c3-1453-38e7-94e6-e38d029f8b5d | -4.6775 | -44.6089 | 2025-11-02 00:40:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f45dd87f-005b-3013-b6e1-7518b2e25f22 | -14.0155 | -43.4943 | 2025-11-02 00:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b8821081-3394-382d-bf27-a33b7190d27b | -10.4134 | -44.8873 | 2025-11-02 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| da7a77d0-f7a1-3083-b579-25039e385dc2 | -14.0356 | -43.4666 | 2025-11-02 00:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e2132ad0-d809-3000-952e-b7dcfa1d8035 | -9.5347 | -40.3033 | 2025-11-02 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 153.4 |
| 529ab4a2-f035-30da-9e0b-b44f7c935d3f | -14.0161 | -43.4703 | 2025-11-02 00:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1f0245d9-641f-3133-b5dc-be4154a496ab | -4.7257 | -45.6914 | 2025-11-02 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 58e19700-0a2e-30b9-835a-b79a44ef87a9 | -18.5321 | -53.4824 | 2025-11-02 00:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ed8a4777-3f1d-3ae8-9963-79b5bccdf0c3 | -4.6775 | -44.6089 | 2025-11-02 00:50:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c89e9c95-dcd9-3421-a562-03a59e633511 | -4.7257 | -45.6914 | 2025-11-02 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 198cc481-f448-310f-9eac-5cdaa62a0f15 | -9.5152 | -40.331 | 2025-11-02 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.8 |
| dcae83d2-3f7a-3c47-8da7-4c445a4e4083 | -14.0356 | -43.4666 | 2025-11-02 00:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 76feaec5-899c-31a4-8299-85d60bfb027e | -18.5121 | -53.4856 | 2025-11-02 00:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 00aa7dc3-9ae0-3fa6-a3e7-5caec64d8236 | -17.4921 | -40.2778 | 2025-11-02 00:50:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.9 |
| 487759fe-29ce-395f-a9ff-9522f8047a5b | -14.0351 | -43.4906 | 2025-11-02 00:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| a4de4c03-7351-31eb-8649-fb3dcc406098 | -14.0155 | -43.4943 | 2025-11-02 00:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 2f9a1fca-59b2-3992-861d-6d82b924134b | -16.9298 | -49.7172 | 2025-11-02 00:50:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9e7d97b4-77d0-3802-8ce0-2a139f206390 | -13.8773 | -47.3436 | 2025-11-02 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 323c4402-a32e-37f0-9689-4ddd899dbca9 | -9.5347 | -40.3033 | 2025-11-02 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.5 |
| ea80b92a-28e1-3d93-8772-3c97010058d4 | -9.5343 | -40.3282 | 2025-11-02 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 53695fc1-72c1-30a9-b9b7-d6b018e9e07d | -17.4928 | -40.2519 | 2025-11-02 00:50:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 130.2 |
| 87f77445-3fe5-3cdf-891b-83be8e5763fb | -9.5156 | -40.3061 | 2025-11-02 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 129.6 |
| f2dbe269-6a05-3677-b3ee-cbe993e4bb14 | -14.0161 | -43.4703 | 2025-11-02 00:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| a083a444-ab88-396d-a2d7-cfb4e3a50003 | -4.6773 | -44.6317 | 2025-11-02 00:50:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 107f60b2-8fbd-37b2-87fc-5721024580b2 | -21.40893 | -49.24855 | 2025-11-02 00:50:00 | TERRA_M-M | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 3dbae01f-d006-3658-be4e-63634a232292 | -16.93898 | -49.71792 | 2025-11-02 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4a3260f4-e27e-3829-9fd7-0f982cb5880f | -16.93724 | -49.70666 | 2025-11-02 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7278492b-25dd-3d20-9ad2-41bdcee7993a | -16.92751 | -49.70838 | 2025-11-02 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4ba79a8b-de8a-3407-bb8b-14a4511a5c90 | -20.29662 | -54.08399 | 2025-11-02 00:50:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b85461b4-7c8c-34f6-8f53-690604180b0b | -18.44931 | -51.62695 | 2025-11-02 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38daac0f-a990-38fe-b5c7-54e6d7de2636 | -19.1012 | -50.46548 | 2025-11-02 00:50:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 21297f40-75df-3435-be15-48cbb4b5ce93 | -19.10888 | -50.45396 | 2025-11-02 00:50:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 21a64b03-d318-346c-977e-169afbe8c442 | -16.92923 | -49.71951 | 2025-11-02 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |


[Clique aqui para ver as próximas entradas](README2.md)
