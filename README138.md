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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbed76a5-e9a7-388f-854e-b5dca71c17d4 | -11.25593 | -60.50462 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f626d92b-4c79-35dc-89b9-9e66b6402566 | -11.25551 | -60.56296 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2333496-fe69-3ed6-b65d-ce80cafb534a | -11.25492 | -60.39973 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a25b89d-7a92-3a96-8c52-4a2a6766741d | -11.2517 | -60.56225 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfa50e7-97f4-3c7c-aaff-f117553ffafa | -11.25107 | -60.39904 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cc80006-2a3b-35aa-b872-476d74b89e45 | -11.24197 | -61.17871 | 2024-10-10 05:38:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8c1c6e6-385e-355e-bafe-164154d7cff2 | -11.23828 | -61.17818 | 2024-10-10 05:38:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8da18d5a-db0b-3ced-b9d7-7c57b2e8091d | -11.23435 | -60.4909 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fcd729a-bfd0-32db-8f90-2023ebce1726 | -11.23053 | -60.49018 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9305a43-9391-3f55-a2ed-7754ff46a478 | -11.22985 | -60.49506 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6365b6c9-2b73-37fd-a8d4-35018ec9f99c | -11.22918 | -60.49986 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e802e77-e12c-384c-8b64-20ff1517e102 | -11.22047 | -60.56237 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ce7d3ab-4e46-3c04-9263-543afece6cbb | -11.21721 | -60.23589 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44b2f9d-8f41-3917-90f2-7c9a5798e0bd | -11.18331 | -60.44631 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2132be90-f464-354f-90e4-13947b9cb9d0 | -11.16627 | -60.61996 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef51face-a5e2-3d20-80e4-717f108001dd | -11.16315 | -60.61458 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b0c1ba-f9bf-33de-9f11-46ca8c24438a | -11.16003 | -60.60928 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 755bc732-5f01-38db-93b2-c267d8d2804d | -11.14167 | -60.60167 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c61c6e8-5206-3eb5-8a49-20ebf7782f5c | -13.7448 | -60.60593 | 2024-10-10 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c89ac4d8-1c42-306f-a886-9b11b6dc704f | -13.74086 | -60.60535 | 2024-10-10 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3923f8a9-a438-317f-80be-33abd193d687 | -13.42815 | -61.91024 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 701ea18e-6095-346d-b3ef-d74ab6810a1f | -13.42754 | -61.91459 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d125b308-c7a6-33ea-9bbf-4f26f5686677 | -13.4257 | -61.92758 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b11ea5e-5d41-3ac4-930b-613bb7ab0bf0 | -13.42451 | -61.90969 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d1018a2-db88-3742-8faf-14021bb33ca5 | -13.4239 | -61.91403 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b4f4452-cec1-310d-b208-14fe26dfe1f8 | -13.42328 | -61.91837 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ba77638-878f-30ea-b756-d8c733b0dc44 | -13.42267 | -61.92271 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 989a26a1-1c77-3cf0-8b8c-5d133e908664 | -13.42206 | -61.92704 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 217b5acd-a718-33ec-90d3-8196967e2de8 | -13.42087 | -61.90913 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bba3807-2b98-3913-8d2e-88b4cf5f758c | -13.42026 | -61.91349 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffda4d46-7256-3edd-b72e-40ee5db515ac | -13.41964 | -61.91782 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cdec4ad-99cb-3c52-aa8c-63d5e41f99d1 | -13.41903 | -61.92216 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b581e4b4-bf79-3ce4-9535-febbafc5bda3 | -13.41842 | -61.92649 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ead218b-4365-3961-957a-c436bbb47970 | -13.41539 | -61.92161 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582b4fad-da2c-3f19-9d68-67cb742cde21 | -13.41297 | -61.91237 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8969ee71-1f01-3ed6-9d03-0f1035d0fd08 | -13.41236 | -61.91672 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d28e50-af33-3336-b17e-34f4a8f6c13c | -13.41175 | -61.92106 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa244a9d-4bc2-35e8-b77f-503ec56c6a75 | -13.40872 | -61.91616 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385d0c1e-c4ec-364e-98d2-84d744514e7b | -13.40266 | -61.90638 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6d36b929-5ba3-3e7f-b649-b9fe28f55f83 | -13.40192 | -61.90772 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e337aa8c-a091-30da-ad66-12a555e4cd9a | -13.40128 | -61.91205 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79c8aca5-13c1-303c-b84c-2f0fa18ff235 | -13.3891 | -61.91908 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0f79148-c07e-3343-a793-056f6d40723a | -13.38484 | -61.92286 | 2024-10-10 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4654bdc3-e25d-35bc-86b1-adf078749597 | -7.9346 | -61.2765 | 2024-10-10 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d078295-91cc-3dc7-8ce1-52767f611398 | -7.93107 | -61.27596 | 2024-10-10 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6e0930a-c7c4-3101-837a-c5e22df37fb3 | -7.9253 | -61.24221 | 2024-10-10 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8d624d9-23b0-36f0-ab8c-5077a47e502a | -7.91354 | -61.66243 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0ba3edc-6157-3fbb-b893-3392949ef1a7 | -7.82172 | -61.69275 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 359b2333-acda-3789-99f5-69f081cdf106 | -7.81825 | -61.69222 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eccdaf0e-7474-3057-9fd2-351418f3dbb4 | -7.79718 | -61.58275 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f244025-f42a-3138-a844-5a4d63f0c71b | -7.79659 | -61.5866 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae9bbc9-64b2-3232-8334-8ee06f604568 | -7.79429 | -61.57835 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c295ca8a-1aef-3cb2-b70f-ed8ef8744e98 | -7.78207 | -61.35174 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc55630f-77d0-3356-bec7-5b4abf668c53 | -7.77855 | -61.3512 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fd42257-68b1-301d-acc2-de23978716ae | -7.77589 | -61.19966 | 2024-10-10 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83e93cee-a5c0-320e-8738-87c2cd61e6d2 | -7.77503 | -61.35066 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42307d6d-03bf-3bb2-8793-1107136ae181 | -7.77235 | -61.19911 | 2024-10-10 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f145d0e4-f4f6-3403-aa12-414b2ea1d28d | -7.77152 | -61.35012 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec59e64a-211d-3b3b-a938-72e23829f489 | -8.23569 | -61.19917 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce1f75e2-f045-3dcf-afdc-ea046d90d854 | -8.23455 | -61.18233 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ca13dab-fa04-33e0-aa3f-2991a2f49c13 | -8.23273 | -61.19456 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd68d771-4b8d-3810-b687-31e814959d5a | -8.23213 | -61.19863 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99af406a-8236-3687-bf89-fbeffb4cd91a | -9.17851 | -61.57579 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc1de52d-89f1-366c-ac0a-3a2fed0f822d | -9.17498 | -61.57526 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f26577c6-a0f3-3dbf-b2f1-81855c34be84 | -9.17145 | -61.57472 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1442d5a-86f1-3f11-9bab-30ca93c6aba5 | -9.16791 | -61.57419 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cb01cd-3c01-331e-adc4-9b2e9326e340 | -9.16438 | -61.57366 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 486886f9-cc45-3384-9f51-337c0a6ea64e | -9.16145 | -61.56911 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5080f074-34ca-3ad9-aa8b-409c287cb220 | -9.16085 | -61.57312 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a95df647-adcf-35fe-99de-39e63fadd64e | -9.15732 | -61.57258 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ef8dbd6-c454-30a2-894b-50af41f851fd | -9.12421 | -61.28552 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8bb2460a-fb52-392e-abc2-31e811edf907 | -9.12359 | -61.28964 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e17403bc-0b22-377e-8036-2edd3aa9045f | -9.12186 | -61.27674 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c6b14ef5-e68a-3d19-b809-97a045bffd89 | -9.12124 | -61.28087 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 75b7b358-635b-36e7-b19b-ab2f0f3ebff3 | -9.12063 | -61.28498 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2cb8c5c6-0730-3b2c-b160-5ebca754a11e | -9.12001 | -61.28909 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2dfc21a8-1569-3d7d-9c49-d2bf11f05f70 | -9.11889 | -61.27205 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab6bd8c8-a27c-3857-9baf-bba0fab67065 | -9.11828 | -61.27619 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d1fe0a40-4673-3eb2-96db-979161a5fef4 | -9.11766 | -61.28032 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 17de7720-0ff2-30eb-9dfe-b6f754d1ac5c | -9.1147 | -61.27563 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f5686fc9-a8cd-31bd-923e-0a81984260ac | -9.10063 | -61.37 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5b21cee-b43e-3df6-a405-6a5b16eb5f71 | -9.09707 | -61.36945 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac98697a-f7a5-392b-9a87-34101e8a1686 | -9.08924 | -61.39755 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b66a9af-02a4-3100-8c45-d5a9cde89a76 | -9.08863 | -61.40164 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00a5025-2671-3669-977e-bbcd6cc99b5b | -9.08629 | -61.39291 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 322049db-fe37-34fe-9e58-bdc370b410c0 | -9.08568 | -61.39701 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7aa33ecf-d140-31f1-a781-6eda4e4a4ee8 | -9.08507 | -61.4011 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9e88dc9-fd44-3f1a-83f0-407f908f6076 | -9.08333 | -61.38829 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 020f3998-f52b-376b-b879-9564f199682c | -9.08273 | -61.39239 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10a02aa7-18a4-3961-8cda-4f8e80295a43 | -9.08212 | -61.39648 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d7f4b2c-0d04-35b9-a765-4a7a863d8f26 | -9.08151 | -61.40057 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eab7f283-07b0-31e2-8ffb-cf83a6562f4d | -9.07977 | -61.38776 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3046c86d-a7b4-3930-b8f1-953b60ef4051 | -9.07917 | -61.39186 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fc7dc3-caf0-30c1-b161-2cca0ca9062f | -9.07856 | -61.39594 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 304ee494-aa41-3651-943d-5d5d855f3c0a | -9.07795 | -61.40002 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21ca098c-c9f1-3fd2-90f7-33e9366fa9ea | -9.07561 | -61.3913 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4649b33-b652-363a-b412-0d65ceed3fc2 | -9.075 | -61.39539 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c474b59-f612-305b-8960-5cbd00a5365d | -9.0744 | -61.39946 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1e50772-43bd-3b4a-a4cb-756dd2e52ad6 | -9.0735 | -61.28201 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e68b3754-82de-3dff-8988-a94906e17141 | -9.07145 | -61.39484 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README139.md)
