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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 293ca50f-7761-3586-9f94-171a5b56eacb | -12.2817 | -50.635399 | 2024-09-29 00:47:09 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6715f63c-7053-3376-ae8a-7729366dba5a | -11.5609 | -47.453201 | 2024-09-29 00:47:09 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fef4c2c8-7387-30ec-b87b-89b22e704b65 | -10.8605 | -44.608501 | 2024-09-29 00:47:10 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dfb0fbb-bc33-3de6-962b-6eb83d93bba9 | -11.1021 | -45.5471 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e635a4ef-6342-3f0e-be9e-7d646cd9c44c | -11.1038 | -45.554501 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4da1fef1-e1d5-3718-bfd2-b4c6de831882 | -11.1056 | -45.562 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8763a6ca-0467-322a-a165-48e63609e66a | -11.0818 | -45.5047 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d407cde-7d90-3f62-9951-734f3ada04ac | -11.0836 | -45.512199 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58c1fc47-4c80-3ecf-8391-66ae8a30d9bb | -11.0853 | -45.5196 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 623766bd-a36d-3ad5-aec4-aeab42f5c031 | -11.0871 | -45.5271 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d83a9b9d-a2f9-3f85-9f9c-76164507d6c4 | -11.0958 | -45.564301 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce969bf8-2bf4-37f8-9ac5-f99fae57d5ce | -11.0975 | -45.571701 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72a666c2-bcec-3321-abff-dbbf75622db7 | -11.0738 | -45.514599 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2986b36a-8322-3343-9188-a78acfc5ed0f | -11.0755 | -45.521999 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1c6321e-ec8a-3b4d-afe0-626ef3b5db06 | -11.0981 | -45.6185 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fec8597f-8642-38a2-9780-9bcd7f69a85e | -11.0998 | -45.6259 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce04efe-b4a9-32c5-bbe2-04995b975e70 | -11.1015 | -45.633301 | 2024-09-29 00:47:10 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a6da971-7c58-3603-8326-764472ca1013 | -12.2327 | -50.646 | 2024-09-29 00:47:10 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94945cbb-6abd-3c5e-be40-839af30fc5b9 | -12.2345 | -50.654701 | 2024-09-29 00:47:10 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c487617f-57eb-3dd2-8f49-85e0e6cb7dc9 | -11.445 | -47.260101 | 2024-09-29 00:47:11 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2efb2503-2920-3bdb-ac8e-aaf3c4d4d477 | -13.4904 | -57.231998 | 2024-09-29 00:47:11 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e553ab91-1c02-312d-9570-9968fe1b4eb3 | -12.8021 | -53.986698 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f01a72ab-0af5-3ae3-9d6b-5ceef0f34a10 | -12.7895 | -53.974499 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81841cb5-90fc-3666-b902-5006bdad5fbc | -12.7924 | -53.988701 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 281c94bf-ae36-3270-b85e-832527315ab1 | -12.7952 | -54.002899 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3da875-5cf9-3236-937d-d0f7c2b6cb70 | -12.7798 | -53.976501 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2df694e5-0710-3842-974b-7b5807c65470 | -12.7826 | -53.9907 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40651f22-94cf-3798-93bc-e6840e8eee8b | -12.7855 | -54.004902 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa6a413a-092c-3520-9438-977460953c7d | -12.77 | -53.9785 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0087fb0a-973a-3b3a-a590-bec3280f1e31 | -12.7729 | -53.992599 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa3a1737-868a-3173-9d43-9b8447c0fdca | -12.7757 | -54.006802 | 2024-09-29 00:47:12 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8eff5d0-fc72-3b15-85e5-182a128ee23e | -10.6557 | -44.485298 | 2024-09-29 00:47:13 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d043b04b-82d4-34e0-b7d9-05463952c1f3 | -10.6576 | -44.4935 | 2024-09-29 00:47:13 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e12fbde1-4615-332f-9f60-61414a57463d | -10.6596 | -44.501701 | 2024-09-29 00:47:13 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84a5e7c4-2a56-3fa1-8df9-313c7d1bae51 | -10.8935 | -45.494099 | 2024-09-29 00:47:13 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcd23e7d-55b0-3b60-959e-77d1f8ef7c8b | -11.5832 | -48.423302 | 2024-09-29 00:47:13 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85304c45-56bf-392e-89b2-9ce70e7184bb | -11.5848 | -48.4305 | 2024-09-29 00:47:13 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da22bb24-759e-3e0b-aa71-31e5432916c1 | -12.7631 | -53.994598 | 2024-09-29 00:47:13 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be94c80a-77fc-394f-8dde-fe60f4f3887d | -12.766 | -54.008801 | 2024-09-29 00:47:13 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7cf242-2407-32b6-8456-3a1a086190b5 | -12.5588 | -53.485401 | 2024-09-29 00:47:14 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c83713f-60ee-341c-a6cc-608b35f7bfbd | -12.5615 | -53.498402 | 2024-09-29 00:47:14 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15a27649-d584-34eb-be16-e6e375e6d84a | -12.5641 | -53.511398 | 2024-09-29 00:47:14 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 309976d0-3926-31cd-b0a5-ad7e8582f869 | -12.5491 | -53.4874 | 2024-09-29 00:47:14 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3e474fb-64a4-3e7d-a8cd-3affc8a4831d | -12.5517 | -53.500401 | 2024-09-29 00:47:14 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 399f85cf-ce18-3fe1-86ea-88579f2a311e | -10.8565 | -45.999599 | 2024-09-29 00:47:15 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c879df5-e2b0-3950-a158-2852b0ef6096 | -10.8582 | -46.006802 | 2024-09-29 00:47:15 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0782640-9eb6-39f6-b8b8-d51c14424ae5 | -10.8467 | -46.0019 | 2024-09-29 00:47:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 861a1b52-0fb2-39b4-b1a9-c680376d5be6 | -10.8484 | -46.009102 | 2024-09-29 00:47:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5556376f-f67b-35b4-9c9e-9cd14107bd15 | -10.2565 | -43.5508 | 2024-09-29 00:47:16 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f50e950-4590-38bc-a86e-8147ef22791d | -10.2587 | -43.560001 | 2024-09-29 00:47:16 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3010893d-d7d6-3beb-816d-b62d46f8e415 | -10.2489 | -43.562401 | 2024-09-29 00:47:16 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10149b3a-79c5-3fe2-9727-29d5e348bf94 | -10.2512 | -43.571602 | 2024-09-29 00:47:16 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 088e6e62-821e-31a8-9215-deb4a2f66d08 | -10.2534 | -43.580799 | 2024-09-29 00:47:16 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e12bbf1a-c4cb-35b5-9c84-91683d8babec | -10.2414 | -43.574001 | 2024-09-29 00:47:16 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43119aaf-2232-38fb-91d0-ec600d508144 | -10.9134 | -46.379398 | 2024-09-29 00:47:16 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81a08863-f0f4-387f-80ce-0f8415a5f7e5 | -10.9151 | -46.386501 | 2024-09-29 00:47:16 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07505edd-8a30-30ef-80c6-ef4200640868 | -10.8971 | -46.353199 | 2024-09-29 00:47:16 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 587d8b03-dbce-3696-a524-effc28a2dccb | -11.6858 | -49.964001 | 2024-09-29 00:47:16 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69f05279-f234-3da5-8e75-e29d070b3588 | -10.6852 | -45.840099 | 2024-09-29 00:47:18 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 858a2f91-b249-3ea2-9ecc-7604f8be9e84 | -10.6869 | -45.847401 | 2024-09-29 00:47:18 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee6f14a7-a59d-39dd-8b12-ea497754b0aa | -10.7862 | -46.5434 | 2024-09-29 00:47:19 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad69d7b5-1ae3-326c-8cd3-90e9ba82f495 | -10.7878 | -46.550499 | 2024-09-29 00:47:19 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7bbaad-b4d6-3e94-ae7b-0c5151e9a0f4 | -10.7829 | -46.574001 | 2024-09-29 00:47:19 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80864f1d-ec8b-34aa-8b0a-b5976d0b76e9 | -10.551 | -46.017601 | 2024-09-29 00:47:20 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6552ef84-2712-346e-a83a-fe8313630843 | -10.5527 | -46.024899 | 2024-09-29 00:47:20 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a49cd09-8cab-3b3b-bd5e-26de66f5d470 | -10.5544 | -46.0322 | 2024-09-29 00:47:20 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc90f5cd-7650-3c32-932a-faf385790da0 | -10.543 | -46.027199 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4074e4a3-76f5-3266-a4df-7fc328fa8421 | -10.5301 | -46.060799 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c12e964f-ac0e-3110-864b-229ac5c9b105 | -10.5318 | -46.068001 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 619791ef-7519-3400-b181-1815610bd91b | -10.5335 | -46.075298 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e02e10f-79c3-3588-b4d7-bf951555c2f0 | -10.517 | -46.048599 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8ab2bd6-d2a0-399e-a14f-7a5cc9450624 | -10.5187 | -46.055901 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74b8430e-7366-3876-99e1-eacc7e84a597 | -10.5203 | -46.063099 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87b679ed-532c-3239-9b56-d955193b0650 | -10.522 | -46.070301 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21768054-6c8b-3af4-88f5-980660b38b99 | -10.5105 | -46.065399 | 2024-09-29 00:47:21 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 015dfbc6-2356-3a70-8692-4327506229f5 | -9.9548 | -44.015499 | 2024-09-29 00:47:22 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 685c12eb-56b1-3247-b205-b66fe5f4fce3 | -9.9569 | -44.0243 | 2024-09-29 00:47:22 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2163e133-5b19-376a-94af-5aed6a013856 | -9.9451 | -44.017799 | 2024-09-29 00:47:23 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e39ce1f5-9c2e-336b-98f9-c9c4fbe06d65 | -9.9472 | -44.0266 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1294260-4ce9-3d1f-825a-bc2c52327a4e | -9.9493 | -44.0354 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ccb33a1-a3e7-394b-a6cd-523595a524a6 | -10.154 | -44.896198 | 2024-09-29 00:47:23 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa2c8ac2-19bf-3546-b1fa-e0a9731a41a5 | -10.1559 | -44.904202 | 2024-09-29 00:47:23 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| affdd639-f991-38fd-b46a-413d2559bfe6 | -10.1578 | -44.912102 | 2024-09-29 00:47:23 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2feb9ea8-5861-357d-bf4a-f4a2383bd774 | -9.9374 | -44.028999 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f516f14d-9822-34ba-98ab-3796567846c4 | -9.9395 | -44.0378 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03b27b95-2b72-33f6-a3be-48d5f3d37cc0 | -10.1461 | -44.906502 | 2024-09-29 00:47:23 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3e33693-0033-3ac3-900e-5386a8e391a8 | -10.148 | -44.914398 | 2024-09-29 00:47:23 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec2ae275-f359-3c87-bfa8-d1f3eb8ce5e2 | -9.9123 | -44.0536 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95532ae5-f6dd-34cd-9135-57d9fa6af70c | -9.9144 | -44.062401 | 2024-09-29 00:47:23 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab45c1b-1ca9-30d2-be76-a1f7844a1340 | -10.4856 | -46.3139 | 2024-09-29 00:47:23 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73176977-46ca-3ab8-a0e4-64d4ccb219d1 | -9.0337 | -40.5522 | 2024-09-29 00:47:24 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f4a09f8c-35bb-32ad-bc36-b85455e49f5a | -9.0374 | -40.567001 | 2024-09-29 00:47:24 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d0c6a423-5f45-3591-b357-8d31450bd39e | -10.3576 | -46.162102 | 2024-09-29 00:47:24 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31b21fe1-64c7-3e64-8862-3c2eb69ce66c | -10.3592 | -46.1693 | 2024-09-29 00:47:24 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a991c517-bbc3-306c-8fdf-2878ed565278 | -10.6591 | -47.929901 | 2024-09-29 00:47:26 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56150c2e-a8fe-3a2c-8eb7-638f1ef93427 | -10.7481 | -48.738701 | 2024-09-29 00:47:27 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37f35a64-c1ed-3058-8d83-f6339b45250d | -10.7383 | -48.740898 | 2024-09-29 00:47:27 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e634998d-9294-3610-b63b-68f68e5e5867 | -10.7399 | -48.748001 | 2024-09-29 00:47:27 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce2ff801-bb1e-3029-a8f0-91f5d4c54f45 | -10.7285 | -48.743099 | 2024-09-29 00:47:28 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b40a6a82-2254-35fc-8321-b665bdc932b0 | -10.7301 | -48.750198 | 2024-09-29 00:47:28 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
