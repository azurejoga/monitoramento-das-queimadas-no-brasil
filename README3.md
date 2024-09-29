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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b62dbb2-2de1-3049-97ad-fe7aca37e0db | -15.6093 | -57.4491 | 2024-09-29 00:46:36 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5849839c-f739-3541-b30c-e3cd7ac4c3b9 | -13.3388 | -46.341202 | 2024-09-29 00:46:37 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24365da8-f31c-3390-9483-89d330514962 | -13.329 | -46.343399 | 2024-09-29 00:46:37 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 07c03104-3c0b-35f2-b215-0fd6545a5c7d | -13.3306 | -46.350498 | 2024-09-29 00:46:37 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af20962e-07b2-3cc1-b9b7-db7e96dcabb1 | -15.5851 | -57.425598 | 2024-09-29 00:46:37 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b469adb5-2820-384a-8343-c59574fc5c6a | -15.5899 | -57.452499 | 2024-09-29 00:46:37 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| faf73289-01f3-32ec-b8e0-63af6ec9d808 | -15.5802 | -57.4543 | 2024-09-29 00:46:37 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2da7c8ee-4851-353b-a4f9-2dbc12c552b8 | -13.2557 | -46.338299 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95ec0224-9dac-3dd9-a33f-6606e7dbdfe0 | -13.2573 | -46.345402 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 78fa2242-9941-3f21-a64f-05747f187681 | -13.2589 | -46.352402 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 046396e8-88da-387e-905c-c6cf3b2a31e8 | -13.2427 | -46.3265 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 032d7800-be13-334d-9862-41f8ea4cbce8 | -13.2443 | -46.333599 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c2bdcaf1-a8e0-33b5-b015-96bde0cf578e | -13.2459 | -46.340599 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75c46427-38c1-3772-a957-00512b16b1b0 | -13.2475 | -46.347698 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd55f2b-0694-317b-b5e9-302d2eea84cb | -13.2296 | -46.314701 | 2024-09-29 00:46:38 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 819f937c-60a5-3068-ba49-c3eb831494c5 | -13.2313 | -46.3218 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 298452a7-272b-3bce-a8a4-9635b92d8f85 | -13.2329 | -46.3288 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48710963-fdfa-3395-a645-e59c7e6bbff9 | -13.2345 | -46.335899 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0bc22b1-9287-35c5-8f05-a722f278ce5a | -13.2361 | -46.342899 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 598a554c-c4c4-3dad-8431-0d8f50fc74d5 | -13.2377 | -46.349998 | 2024-09-29 00:46:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3c8e474-da7a-3aa1-b23e-78fd6e8da232 | -12.585 | -43.8228 | 2024-09-29 00:46:39 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2962ddb-ea1d-39cc-819f-dce7a8f01ca7 | -12.587 | -43.8312 | 2024-09-29 00:46:39 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c718bb47-0158-30c5-bffc-209459bc6c3c | -12.5891 | -43.839699 | 2024-09-29 00:46:39 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4be9e3b-18d0-364d-9d28-a62b2f3c89d2 | -12.8174 | -44.802601 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 612bc0f0-4e2a-34b0-aaef-eaeff9ce9be8 | -12.8192 | -44.810299 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a76c9054-4aed-31ce-b105-6da899d06feb | -12.821 | -44.817902 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c302e4c6-0069-3a82-b0a9-eae3b5649fe6 | -12.5773 | -43.833599 | 2024-09-29 00:46:39 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03e66079-4abd-3389-a56c-bf2755098c79 | -12.8076 | -44.805 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e032f57f-73c9-31c8-8277-ab9538e24874 | -12.8094 | -44.812599 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4732f98a-838a-32ae-8884-ef36815f001e | -12.8112 | -44.820301 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ed8db62-749f-3bd3-af4c-640675e5a419 | -12.813 | -44.827999 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8eb591-cd8a-39b3-88eb-8cd944153811 | -12.8148 | -44.835602 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d3c486f-1c18-3de1-bb94-efdd089aa8a9 | -12.8166 | -44.8433 | 2024-09-29 00:46:39 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 137865c0-3c53-357c-979c-18418327524c | -12.796 | -44.799702 | 2024-09-29 00:46:40 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee828c4a-e8d9-3067-8828-ba746b58612c | -12.7978 | -44.8074 | 2024-09-29 00:46:40 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9e227ee-fb2e-31f1-b935-355e82999272 | -12.7996 | -44.814999 | 2024-09-29 00:46:40 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6180587a-ef8c-303f-8266-45617e32627f | -12.8014 | -44.822701 | 2024-09-29 00:46:40 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11ec6193-2aea-3235-af51-608868e43b5d | -12.805 | -44.838001 | 2024-09-29 00:46:40 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9da7cfd-6b48-3779-9230-139f49e8676c | -13.4492 | -48.351299 | 2024-09-29 00:46:42 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19bd296d-a48d-34df-bcc9-39dfd2cb4664 | -13.4509 | -48.3587 | 2024-09-29 00:46:42 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f92812f-8cc1-3422-b0ae-58dd7ce95ee2 | -13.4667 | -48.571602 | 2024-09-29 00:46:43 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8df7d037-ff27-3a59-a23b-0224aabead56 | -13.1764 | -48.512798 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 038e95b0-278a-3f89-99f8-f1bb68205c42 | -13.178 | -48.520199 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4dfec88-1ad0-38d0-9516-5766698a91a6 | -13.1618 | -48.493 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df1f1f9a-df8a-3d8b-a645-06f8abac8e6c | -13.1634 | -48.500301 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9b1dcf8-199b-3999-add6-a5abbfe957dd | -13.165 | -48.507702 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1475d246-db56-3e3a-b1f0-bf17cd048124 | -13.152 | -48.495201 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9cac6e-87b0-309b-8b47-2afa4edd7da5 | -13.1536 | -48.502499 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f124ba64-3c35-3423-a261-89a83d7770ba | -13.1552 | -48.509899 | 2024-09-29 00:46:47 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d45e3ca-2b3b-3ace-b582-a87be32aff42 | -13.1796 | -48.527599 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b305cb82-51cd-31f6-9b49-0aa3a69d6649 | -13.1812 | -48.534901 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb22be4e-8ecc-3b4e-9f43-e86da82de91e | -13.1698 | -48.5298 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20c608e0-baa4-3835-a763-a1e6a0161388 | -13.1714 | -48.537102 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79a0b393-c532-3a5e-98ca-69b177f0cfda | -13.1731 | -48.544498 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66745612-d4a6-3ba8-81a1-1c31c49f5f78 | -13.1633 | -48.5467 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcae8765-2d1b-3618-a3ea-7a66e9d2d260 | -13.1649 | -48.5541 | 2024-09-29 00:46:47 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 815065ae-d278-3e05-92a6-c6a088e3241e | -13.031 | -48.599602 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af59709f-4db1-310e-916a-ba61e0a9f625 | -13.0326 | -48.606998 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d97d5d1-6062-3ae1-90b7-3cf3e9b4b27a | -13.0343 | -48.614399 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3782b56b-3cac-3357-a6dd-8afa10e16a14 | -13.0228 | -48.6092 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50d75297-f2ae-3aa5-a2fd-6db89a78dee1 | -13.0245 | -48.6166 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64d854b0-2a44-3efe-8e91-701202e087b7 | -13.0261 | -48.623901 | 2024-09-29 00:46:50 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16b1f874-a914-3dc8-ba3d-fa30fdbdd094 | -11.8782 | -43.806301 | 2024-09-29 00:46:51 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6670e1db-a240-3697-b117-1b3e662867c2 | -11.8803 | -43.814899 | 2024-09-29 00:46:51 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b17d3b7-9026-33bb-a3c0-3885d034ae78 | -12.9626 | -48.5224 | 2024-09-29 00:46:51 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8e19ba-7eb0-3ee9-ad3d-8b79949ac269 | -12.7458 | -48.4715 | 2024-09-29 00:46:54 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97702fe6-7e48-32a6-b174-89907ab10456 | -12.7474 | -48.478802 | 2024-09-29 00:46:54 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53eef118-246d-3372-8650-faf3a74070f4 | -12.749 | -48.486099 | 2024-09-29 00:46:54 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bd76daa-2433-3974-b75c-2d53621ca768 | -12.0324 | -45.730301 | 2024-09-29 00:46:55 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1348ce99-b506-314a-bb42-9a398541fc99 | -12.0341 | -45.737499 | 2024-09-29 00:46:55 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c577e2e-162c-325e-b72f-6c1c18cd8084 | -11.7732 | -44.667801 | 2024-09-29 00:46:56 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29a1cef3-20ed-3214-aa7b-9ae01b183964 | -13.2449 | -51.272202 | 2024-09-29 00:46:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51b9fe59-deca-3d35-98cd-33d55a0a56de | -11.9163 | -45.541599 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eff8fae0-f6b8-3a4e-8d55-1c2a2d61e03a | -11.918 | -45.549 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01ca3454-06ed-3937-913c-323900b41c09 | -11.9197 | -45.556301 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a4f30af-9c0c-32ad-8517-0be8eb12361f | -11.9082 | -45.5513 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90cefb2c-838b-3fe4-88c4-d13965f4ebef | -11.9099 | -45.558601 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3727df21-8616-38c3-933c-340e86f9dd8a | -11.8985 | -45.5536 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5d1a0ea-f839-3222-a7c3-884b66ced6c1 | -11.9002 | -45.560902 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3ede5f-444f-384b-a425-8cffca48a6d4 | -11.9019 | -45.568298 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f0d12cc-7781-3133-95ad-c2196887c45b | -11.8887 | -45.555901 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1abc8085-6b9d-3af7-ae15-f02efa7410ba | -11.8904 | -45.563202 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 438e7d25-85a0-39b5-9a70-a2860f11d5c1 | -11.8772 | -45.5509 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f458180d-2597-3a5e-8408-b728b125b253 | -11.8789 | -45.558201 | 2024-09-29 00:46:57 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2b6772-4aa6-3fd3-8297-0bbc7a08ca09 | -12.4819 | -48.394001 | 2024-09-29 00:46:58 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a401a48d-ffc3-3895-9d56-4b631af92d8d | -11.7604 | -45.492901 | 2024-09-29 00:46:59 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e0b3bc2-e2a6-3285-a073-cb0950c91feb | -12.4877 | -48.606201 | 2024-09-29 00:46:59 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2da133b2-e024-3362-89af-aebbcbc8dfbb | -12.8584 | -51.135101 | 2024-09-29 00:47:01 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e614b20-3a5f-3f16-ba81-48f7adc04142 | -12.8604 | -51.1446 | 2024-09-29 00:47:01 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a21e9be2-7699-32a6-8a6b-05ecdb0a6072 | -11.6983 | -46.338299 | 2024-09-29 00:47:03 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9035475-7d18-3c2c-95a8-b1eef0a55b54 | -11.6999 | -46.345299 | 2024-09-29 00:47:03 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42480c38-a821-3ab5-a6ec-ad1ed210ad66 | -12.5455 | -50.623901 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f62fb24e-59ea-350c-b85c-67624700f4fd | -12.5473 | -50.632702 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec21aeda-7dfa-3c0b-9244-0fb5791e04f6 | -12.5492 | -50.641499 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d2b6965-7410-37c7-8f7b-bc79ad3f1a65 | -12.524 | -50.6194 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c5f95ba-be8f-3980-b43d-df1a5a4d70fb | -12.5259 | -50.628201 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 450d593b-59bf-3872-bd13-0f2c95d77f37 | -12.5277 | -50.637001 | 2024-09-29 00:47:05 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| feb43d92-fe24-314a-9538-eb48f1b61954 | -11.7911 | -47.6059 | 2024-09-29 00:47:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb91d8f9-9029-30ae-8696-4f7fc8cd750e | -11.2949 | -46.1549 | 2024-09-29 00:47:09 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc79902-a079-39c4-b0d5-1a0631607856 | -12.2798 | -50.626701 | 2024-09-29 00:47:09 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
