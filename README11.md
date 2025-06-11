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
| a111eab7-e781-3c5e-86d7-8c3405f4100f | -11.77963 | -47.39997 | 2025-06-11 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64fdaf04-82d8-32d2-8af6-fb3ae3b3a86b | -12.78251 | -48.72795 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf3f5041-e7b8-3a79-8770-033795b335d8 | -12.26172 | -57.60939 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a08e113a-b91b-319d-8f6a-1881a5e13d22 | -10.87847 | -54.75028 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e40165d0-94d4-3ffb-9a07-d2065980a94a | -12.52344 | -57.2253 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f7bbfd5f-b646-3462-bb41-efd5493865f9 | -10.70588 | -49.51681 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1cbb7668-eb41-3754-9921-ae57f45e75fd | -11.37774 | -56.56137 | 2025-06-11 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df66059d-bd73-339e-adc6-77326a2559a8 | -6.54886 | -54.98492 | 2025-06-11 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc66031e-0e8c-3fff-9142-28e7b986b4c9 | -11.13621 | -53.94413 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 103156f5-9e1b-335f-a915-d6f7383ac4e1 | -9.70178 | -49.47894 | 2025-06-11 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b10dccf-0784-3667-a207-cd9c46c6b66c | -9.38195 | -48.41212 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e7211d-e7e3-3bfe-9479-8b105098f85a | -14.25253 | -45.48937 | 2025-06-11 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b18993b-55a0-338d-a1a6-73b9f7fccf3b | -11.37945 | -56.5501 | 2025-06-11 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 284a67de-f65d-30d1-a6fd-787c96129752 | -10.29862 | -57.13794 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78b7ed98-6e1f-3465-b03c-b983e4eeb9a5 | -10.07805 | -52.74952 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a317b5f-c055-3eff-b5f2-bff42c3c7721 | -9.34768 | -50.26316 | 2025-06-11 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c8a05b-c3f3-397d-8b7e-8a2593acd070 | -14.04413 | -55.13685 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1888cdcf-0c63-39cd-9a50-2956bf18ddac | -12.26507 | -57.60992 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0fbb210-ce53-3f03-972b-d4b2fcce6802 | -12.52288 | -57.22899 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a7841f4-7c8e-3ce3-b4af-5f72adccdcb0 | -10.69549 | -49.51535 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 563c249d-1551-3454-bd1e-272e9f3c0ddb | -11.1417 | -53.92794 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1acbc75-13d1-365c-950e-331722651bb1 | -10.36431 | -57.23909 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e37e01-765a-3f90-9c8f-62127b727ca4 | -8.28331 | -47.44828 | 2025-06-11 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d1cf5d6-7aaf-311f-b68f-1a5b9584cc2a | -11.14098 | -53.93285 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 395fedca-30db-3766-ac1d-076ab4681b41 | -13.08972 | -47.43592 | 2025-06-11 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc01f511-caf6-31f4-806b-a7a0e0b23bd8 | -13.79137 | -54.31105 | 2025-06-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f1a1c67-17f3-34cd-92c0-9a1aac6fb0fd | -10.23619 | -52.23687 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a76780f-61e5-39ca-8139-a2a8e6da25a5 | -10.65348 | -49.42533 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd31be45-6490-3136-82e7-b4fdb002a60d | -10.05124 | -48.66642 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87b2028c-565e-3259-9b13-7c149b99c6f7 | -12.52173 | -57.21369 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c80e852-8101-3ff5-a03d-105dfc30c678 | -10.36363 | -57.50788 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5541449a-e072-39ed-b71b-2508ac25554a | -12.25838 | -57.60886 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 077f85a5-5b5d-3a3f-9c69-1a5869edd50d | -10.34756 | -57.50172 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f1d371-c829-3548-bd89-5044cac0e58f | -12.3481 | -57.42698 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b340588c-fe32-31bc-8ad7-acf0a01c87d9 | -10.94514 | -55.30717 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03cfc2d6-c496-305d-9904-dc4fefe7059c | -12.78294 | -48.72417 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0167d831-4fc4-36f8-9381-93401b180b32 | -10.29473 | -57.14099 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01611138-2a40-38bb-ba82-6ff0ee8c9591 | -10.30197 | -57.13846 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c739ce-8ea7-3353-8174-6e0af2ecb5ca | -10.6963 | -49.509 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d385c70d-f430-3cfa-8e66-79bc61289926 | -10.70109 | -49.51293 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8d54e0e8-07f2-3224-a769-03824c004f9d | -11.14242 | -53.92301 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1caa787e-f488-39e2-aa1f-6e7df75893e6 | -7.89321 | -61.47476 | 2025-06-11 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc65aed7-f15e-3151-b0d3-4e1eb0ab2087 | -11.36748 | -56.55977 | 2025-06-11 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7927bf11-024c-31f2-ab07-5c830debe677 | -12.03997 | -54.68232 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094a0578-f94b-34f5-917f-2436ce3b062a | -10.36486 | -57.23553 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 897d4853-8d40-316b-9bd5-fc57fdaff6fb | -13.89546 | -48.73401 | 2025-06-11 05:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62dd8849-ee71-37b8-bba2-ce5121075b24 | -8.96222 | -47.96921 | 2025-06-11 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4049c219-76ff-36c4-9312-ad830e875b1f | -11.8337 | -60.91948 | 2025-06-11 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d072efb-6af7-3a8e-afcd-7a7a1d7db759 | -7.8691 | -47.88446 | 2025-06-11 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b951ad2-208f-3b69-ae87-78a107da75cc | -11.04869 | -55.03998 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 711564eb-9eae-3d2a-bc5a-fb67932b5464 | -10.8426 | -53.78189 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebb55b52-5840-3e63-ba48-7d5231c55234 | -10.51181 | -53.63514 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c09e83c9-6c2f-320d-a58c-aad0c5576d7a | -10.12245 | -58.20192 | 2025-06-11 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d71982f-677e-3390-b3cb-46ccc0c38c52 | -14.03659 | -55.13583 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c07f6f12-7950-3853-adec-4579e2a7aacd | -9.36291 | -57.43626 | 2025-06-11 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e8b2733-ae6a-3d2b-aded-0112cfa2e692 | -12.2938 | -50.107 | 2025-06-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f95c3b60-6958-38c8-b8e5-97a089f36598 | -10.87488 | -54.32542 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4ea485f-f34b-36f3-a851-88fafa90ee78 | -10.70069 | -49.51609 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8b2c65ca-21bf-37d8-b8f3-76d4c649844c | -12.52228 | -57.21001 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17485a70-920c-3698-b1fd-1c90bd2c40d1 | -9.24115 | -63.28611 | 2025-06-11 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d38fc6b2-6901-3584-9ade-b88a57cf550c | -10.87504 | -54.32297 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01eb4b1-212b-306d-8d27-40a60a0adcf4 | -12.19869 | -54.26571 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c45c4ea-88a5-3e85-8ff3-1a1788886832 | -11.77907 | -47.40452 | 2025-06-11 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91082025-1cf1-3c97-b36c-6f709b0785cc | -13.47051 | -56.8578 | 2025-06-11 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68420eba-aa34-3c6c-bb29-035e927b1197 | -10.50409 | -53.57722 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 196b6371-5e36-3c52-a34e-488a43fed9da | -12.26117 | -57.61298 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696ae184-10a0-3ccf-82fd-d9e6aed34da6 | -13.78817 | -54.30529 | 2025-06-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fe8f358-52d3-31f2-be1e-eec5aa807eac | -10.29807 | -57.14152 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 764629f3-cab6-3366-9b57-eedb271cc8c6 | -10.94285 | -55.30969 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940a8acc-d1d7-3952-ada7-4936360f480e | -11.83077 | -51.28529 | 2025-06-11 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57570148-95fc-3deb-9501-f5a370f22271 | -12.52117 | -57.21738 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fcb531f1-57a5-3e88-aebf-3f32d0b54b8c | -11.87874 | -56.41367 | 2025-06-11 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b705b6b0-053d-33ab-b9ad-274e1818a9fb | -10.94326 | -55.3197 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2856d887-e503-36fc-a6ce-368d2334ea71 | -11.13962 | -53.91949 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb417621-8ad4-3ca2-8edc-4b5eff202e56 | -12.78816 | -48.72855 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1cdfd9-465e-3d2d-9bb8-7dd7c05ff44e | -10.94388 | -55.31554 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 585254ff-8d91-3bac-a327-d87e47184123 | -11.88622 | -56.41089 | 2025-06-11 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f68ea40-0dda-3708-8c9d-cb70c84e77a9 | -12.52232 | -57.23267 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b1ded5e-03f3-319e-8588-56036e54171c | -9.84829 | -47.88023 | 2025-06-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72915ac2-d0be-38a0-adca-ca538d4ed7a8 | -10.87192 | -54.31772 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb5482d2-b476-3889-8894-98a5bf9076e8 | -11.13956 | -53.94265 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 112be0e5-1807-3a8b-944a-c70657b099ad | -9.78194 | -57.42664 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0716e2a-1c79-3a8d-95a6-30cd27a5b334 | -10.6474 | -49.43114 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e542257-be4b-324b-8687-7c64f6c9b22e | -12.52395 | -57.19895 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53f29b2-3823-3a89-9f6d-6fe7560f7331 | -8.28482 | -47.44392 | 2025-06-11 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdcd876b-0c34-3771-bcee-7c7fd3223677 | -14.24483 | -45.49565 | 2025-06-11 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d432ac5-6848-321f-8136-660b05782f50 | -13.09364 | -52.2893 | 2025-06-11 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d21e7b-0805-30e4-8c35-173492f9ffef | -9.77862 | -57.42611 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8d00f29-bfed-349c-b132-23553f4f5702 | -12.34418 | -57.43008 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b58ad667-fcaf-3932-94c9-0813a72dca1f | -11.88276 | -56.41035 | 2025-06-11 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6213dd2-362f-3271-8ae4-33c6a8c06bba | -10.19244 | -49.59788 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455a603f-1f39-3481-a4e4-6cb59d309172 | -10.3686 | -57.49782 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fa804b9-5690-3b11-999c-653a035874fe | -11.04932 | -55.03568 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d190c2cf-d3e6-3c3b-840d-4f79e37d306c | -10.36418 | -57.50435 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9371f0f3-9b34-3bb2-93a0-20361ad96c50 | -10.50788 | -53.63457 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f613ca5c-5f43-39ec-9b19-021efca8928f | -9.78581 | -57.42365 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22e47251-7031-3757-aebf-3963f8c92be6 | -9.36568 | -57.44028 | 2025-06-11 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8bc989c7-41e1-3c7b-85b7-97d0b227d8a1 | -9.77916 | -57.42259 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed3e678-78a1-354c-9357-042bdaf0c431 | -14.03038 | -55.12536 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b5002d-9617-3ad7-8654-16980e4fbf3d | -11.33792 | -45.21844 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
