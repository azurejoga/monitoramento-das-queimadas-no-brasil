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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c13d9e6-9e47-3e21-9c36-9e191efbd745 | -2.35121 | -50.11346 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6e6b20-35ce-30b4-a073-ffb040e56290 | -3.06822 | -48.03399 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5403cd32-dae6-38db-8dad-6f4c123b8e10 | -1.18934 | -49.04884 | 2025-12-04 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28357b93-a9c1-3593-81e5-70400229b993 | -2.88046 | -46.80268 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25ceed0f-a2a7-321d-82df-70e5f65971d4 | -3.84985 | -47.83475 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f9bf7da-306a-32e5-8916-614b747e47be | -2.43161 | -49.0213 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cba3896a-22a5-3b6a-89bf-82c47b393e4d | -2.38039 | -49.39108 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea1d27d7-bda5-3ed7-954e-2b574ce7d8ff | -2.92246 | -48.22945 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 042c782f-4fbc-319f-ba71-2605ef2ac07f | -2.6345 | -48.03978 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc9cc60-5490-3d1b-91b3-8bbcb6af3a23 | -4.25752 | -44.15121 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddb5901c-e9f1-3739-9277-7300285658f2 | -4.39902 | -45.83673 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1451b98-687d-3697-8a32-a37692e70e9f | -2.60807 | -49.25475 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 455b9b66-f1d2-3231-8915-433e49b928ca | -3.17615 | -48.6128 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68196a7b-7ceb-3ee4-85d2-8ffe64d8e9f7 | -4.52863 | -44.23246 | 2025-12-04 04:48:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3b230a8-30a0-30e0-94d6-78aca6e72648 | -1.98239 | -47.96598 | 2025-12-04 04:48:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de612d15-95e3-365d-a853-b520477f810d | -2.14321 | -47.88176 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8379c15-3842-3b0c-ae6c-615698e8ce7f | -3.40983 | -44.98721 | 2025-12-04 04:48:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ff9d22c-8843-3bc9-a24d-0aac2c6a08b4 | -3.14181 | -49.41312 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 220a5e88-656b-350f-8914-f0466eb81c40 | -4.52256 | -44.66125 | 2025-12-04 04:48:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81cdef25-dcd0-3f19-b17e-a9247c06198b | -3.0458 | -48.41954 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4533f7de-a14c-3011-b01c-96dfcbc3d52a | -4.07382 | -43.6911 | 2025-12-04 04:48:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51073371-8af6-35a0-99d8-99e5d6da9ff0 | -2.43106 | -50.29174 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f69af7-b66f-38c2-a5bd-e2a316e6f360 | -3.91108 | -47.71233 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2c84d5c-2ba6-3fdb-9de7-7d5e2e121fe8 | -2.64833 | -51.62535 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 571b8c5a-4bdb-35d0-9be4-17c5f3a8e16d | -2.58005 | -49.09545 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03f31f52-56dc-356c-a88d-3cb3e2e0225d | -4.5544 | -45.80214 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d34334dd-ba38-33ca-9db3-bbec7084b045 | -2.38708 | -48.65979 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b59109aa-6510-30c6-8b4c-2fa9dcebb963 | -2.43051 | -50.29518 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72e875a-1b0f-3b80-a20a-a0987c145631 | -4.51812 | -42.78502 | 2025-12-04 04:48:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81e54e8a-691e-3685-b69e-1394aa43cfc5 | -2.63995 | -48.53895 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19859903-32e9-31cc-b125-0c334e29b52b | -4.21557 | -44.2514 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 882d2bea-7c9e-3ee5-9ff3-6c02b534721b | -2.58061 | -49.09192 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bf08bd1-98d0-36c2-b21d-a00ff35a0407 | -4.49034 | -45.28189 | 2025-12-04 04:48:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7f05e8-7a61-3a8b-9436-ca992c6cafff | -2.63629 | -48.02842 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a2dbb65-1f27-37e3-935c-f84abf5c5bfa | -4.38899 | -46.67037 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 649abe1f-6379-3bf2-9687-1ad2cd3ab083 | -5.01808 | -41.00704 | 2025-12-04 04:48:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be496107-edae-3ea4-937a-2dc16c0c528b | -3.72562 | -45.57981 | 2025-12-04 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 169710a2-8076-3a9c-8234-79f52da14b8e | -2.4844 | -47.82985 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adfee56b-85c5-35cb-81f2-230091baec49 | -4.38821 | -43.13396 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c2a21c1b-2496-341c-98d6-9a925db29a18 | -2.53246 | -49.46164 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7add142e-a9c0-3089-b254-831981b188b9 | -1.16408 | -48.86179 | 2025-12-04 04:48:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed442f06-fd7f-30b7-8192-19b384cc4773 | -3.21768 | -48.61546 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 536de7b8-3f48-3e73-8989-c62d246e4dd2 | -2.42719 | -50.29466 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1747e722-0af8-3808-a880-61c513868afe | -2.38761 | -49.38863 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca1f8d46-e348-33bb-9048-6f44a12acf0d | -0.1846 | -49.06681 | 2025-12-04 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 024a3107-0e1c-3caf-9741-1bee0de7aa90 | -4.21114 | -44.25076 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25964be4-72d6-322c-ae50-52226357ccb5 | 0.41089 | -50.75547 | 2025-12-04 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a10dcb-f46d-337a-9fde-52f048789ef4 | -2.50967 | -48.47746 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 578a105f-6fbf-3c49-b0a4-b7367d84ab08 | -4.12051 | -47.29215 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9edb7dbd-be72-3447-a75e-a51358fe106c | -1.18433 | -49.03732 | 2025-12-04 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb262d7-e59a-3c54-b768-069634851e47 | -4.39982 | -45.83162 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae7fedfa-feed-3c5c-9598-87a6744f8f3a | -3.51955 | -47.20088 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5746641-7c6d-3a64-b0b1-0fd00e1261ac | -2.13974 | -47.8812 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 396cdfdd-93a7-33da-8a97-c7bc101a921e | -3.22068 | -48.61919 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6f58738-7337-3744-9042-0872ea7fba8f | -2.48569 | -49.41151 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d1303a0-cafc-3061-bd31-e053be10dac0 | -2.57397 | -48.22274 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 046e6804-3cff-34e4-9a0a-f5eca2730a46 | -1.35631 | -53.22289 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90e1570a-15d6-3990-8449-76d9d2e2537b | -2.6357 | -48.03221 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ac991c2-7e35-337b-bc95-472df5f52f15 | 0.41145 | -50.75901 | 2025-12-04 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 403e0688-a87f-3ceb-8d94-e40501bbe180 | -2.4216 | -48.59479 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e3c15dc-8013-30f0-ae5b-52f41f5f121e | -4.5011 | -45.76556 | 2025-12-04 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4150c79-e1d9-3eb3-b333-19d53e4311c6 | -3.22648 | -46.8544 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 287c8644-69f0-3f66-b61e-18a72bd850fd | -2.35561 | -50.10709 | 2025-12-04 04:48:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e2394a-0e61-3577-998e-69f387b72630 | -2.5319 | -49.46512 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61bed491-53b0-3113-be54-b4a884ee52ec | -5.02376 | -41.00733 | 2025-12-04 04:48:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f54fbe89-2976-34b9-97d4-4ba7ab4a19d8 | -2.35893 | -50.10761 | 2025-12-04 04:48:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 877dbe02-d815-3235-92f2-8f07ddbf26cd | -4.0345 | -46.97329 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a097c00d-f989-3f3a-923b-71a5c253315f | -2.50655 | -47.82539 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4279a762-9de1-3b0b-8231-3812e4f17b43 | -2.32783 | -49.08147 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| be735d7b-4b24-3094-a26a-eb01e9e98e87 | -0.8386 | -52.35041 | 2025-12-04 04:48:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f18d3865-82e2-361e-87e8-c5bfdccfcd8c | -1.87573 | -50.96078 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95b363a0-9ae3-3242-8088-1fe759e4078a | -3.38474 | -47.27563 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce874eb-9d4b-33f6-b1f4-4fe56c2b716e | -2.62531 | -49.23225 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08bbe7c0-fc65-3255-b1f1-f18a92a8ae9a | -1.42321 | -53.01147 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d355ac-93e7-3d43-a6bd-510af24caa8e | -1.09525 | -54.11038 | 2025-12-04 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07022b19-3a9c-36d3-baa9-75dacd351f5d | -2.64553 | -51.62124 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 013ad24f-a363-30b7-828d-621eecda2f9c | -2.59284 | -46.8076 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 292666de-159e-35f2-a2af-79cbcebbbe12 | -4.39207 | -46.13676 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a744b357-2f37-3b57-bf47-9af76a0e7b6a | -1.69244 | -46.14938 | 2025-12-04 04:48:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9e5b50d-8144-3ed0-a73b-dd1b8c9a55f0 | 0.33219 | -49.76594 | 2025-12-04 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f4850c2-5060-3e98-a339-62ee368225bb | -4.50006 | -45.77235 | 2025-12-04 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3caa1b2-8b5f-3f4a-accc-ab10ddf078ff | -4.83582 | -43.1992 | 2025-12-04 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99cabffd-69f4-3448-826e-46873c206bfa | -3.84693 | -47.83025 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e9815d1-4fdc-3ef7-932a-f4d696eafc3a | -4.21226 | -44.25213 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a4fd887-aa50-39c4-8277-5d95b73a955c | 0.83454 | -50.22568 | 2025-12-04 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6538840-747e-3de4-9f36-2b18468915b9 | -4.05186 | -46.60755 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd1cfdcd-8a46-3d9c-b7d2-d599269460c9 | -2.73859 | -49.33248 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32bfedb-8352-3fe1-b133-50b4b0987609 | -4.40696 | -43.13388 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5a78b7e1-386a-3e01-97bd-9dcb1880fb70 | -1.95783 | -48.45718 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a685d98-4cfd-3531-b0e8-e677aed1ecfb | -4.39736 | -43.13247 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d190ea70-a131-30ce-9b95-9dea305eda65 | -2.61086 | -49.25878 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13977e5c-e8eb-319a-a842-974ea92c4335 | -2.62915 | -49.18598 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7b8ae2b-31d1-3edf-abaf-57ac39e951e4 | -2.44555 | -46.31576 | 2025-12-04 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b368af7-e0fb-3b7f-9279-0b6aa717e279 | -3.38379 | -49.25182 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d79bca6c-c70f-335e-8db2-c9e8ca02ce9d | -2.53697 | -45.37316 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ccb81216-99b3-3897-866f-f4f687217738 | -4.11622 | -47.29578 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd999b8-3f64-378b-bb81-c4b42c3d36ef | -3.56729 | -47.18023 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d004845b-a5b0-345f-97d2-f10aec3ebb4d | -1.87769 | -50.96079 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d196c56d-ad95-3dd9-81ed-a0d31e7c52fc | -2.35947 | -50.10417 | 2025-12-04 04:48:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cbae0f3-df4f-33ca-aa6d-a2c61baf1b3b | -3.22125 | -48.61552 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README17.md)
