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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd39f6a-7bd9-369f-8bed-4ecb92023d0b | -2.03962 | -48.03253 | 2024-10-15 04:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 688fc346-7838-309f-b76c-d264ad8f6d44 | -1.90955 | -47.88658 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cd922e6-3e39-3e14-98c3-292c39fc7fc6 | -1.87477 | -47.89036 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b4420b0-8e96-3e79-9212-54ad765aaded | -1.87144 | -47.8126 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6a1ebcb-a454-3a50-99ae-aca43eac5977 | -1.86365 | -47.83872 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53a886d2-2494-337b-beab-5343a88d26ee | -1.86297 | -47.84313 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f9f19b31-bccb-372c-ba11-cab99b5008c7 | -1.85925 | -47.84258 | 2024-10-15 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc671894-70fd-3160-b6f7-4dc71e3c03d8 | -1.58746 | -48.03394 | 2024-10-15 04:46:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7c2c342-103c-33e1-baf3-8839d5061444 | -1.47133 | -47.16866 | 2024-10-15 04:46:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dce73a64-f52f-3a74-9ba8-90fb253b95ff | -1.17042 | -48.09244 | 2024-10-15 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbbf8b0e-b7b3-3618-9da8-d627f500d315 | -0.97006 | -47.30294 | 2024-10-15 04:46:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13dbe8a6-9d57-37fc-8e02-222094f58179 | -2.85701 | -48.2433 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d28d09-86e9-394e-a6e1-e75e8f6ac60d | -2.79231 | -48.70426 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1b60d05-c768-3007-83eb-640f0aefd3f8 | -2.75344 | -48.69414 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a53bcfb-5e75-3e1e-aa79-044c1c3cbe43 | -3.05512 | -47.97033 | 2024-10-15 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca84cfea-a7ae-30cc-9e81-aff255058442 | -2.78668 | -48.08489 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa28bb5c-c8cf-387a-b3fe-0e1cb468a7d9 | -2.78601 | -48.08931 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89db18c9-b718-3e39-b2f6-5a59cf21ce00 | -2.78535 | -48.09371 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f88cd58d-d7f4-323e-b649-9d3313949df2 | -2.78436 | -48.08609 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c7fe3d0-3ada-3882-8052-81880747d037 | -2.78367 | -48.09049 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf6f3424-70d7-3503-8aa4-d3bbe5658aeb | -2.5847 | -47.47475 | 2024-10-15 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d64102c5-c4c4-39f9-951c-4bd8aafc9cea | -2.58397 | -47.47951 | 2024-10-15 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3c8ea3-395f-3517-836b-4212b0d5e038 | -2.46311 | -47.81483 | 2024-10-15 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eef924c0-ed28-3e89-8a16-cc523fcec551 | -2.39856 | -48.10947 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b6f4e4-490d-3f20-ad2d-bfd942a3c55e | -2.23763 | -48.01665 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86ff092f-f74c-3d0f-8005-3a8732119c22 | -2.23695 | -48.02102 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330ea984-5b77-39e1-9e58-40e99fdc8e74 | -2.51011 | -48.55359 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3141aeb2-1ca6-347e-847e-40b711949aad | -2.50948 | -48.55776 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1c6a5018-bc2e-3f58-94ae-ea9336cab473 | -2.50651 | -48.55301 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa338cb-c5d3-3894-a947-8c3466b7c42a | -2.50587 | -48.55718 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16442cc9-ad7e-37ce-abf8-da6515e34d9f | -2.50353 | -48.54829 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b8d4a43-119b-3a6b-8781-7650ab2fd9af | -2.5029 | -48.55245 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31533e20-eff1-397b-ae1e-3f48365ff8ea | -2.50227 | -48.55661 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 871615a0-6cd2-3f78-81d6-0cbf35162a1e | -2.50194 | -48.54902 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 940dd846-ee25-3886-adf0-87aac683644a | -2.50129 | -48.55317 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a00e663-c159-38cf-ae4b-267bbeae7ec8 | -2.50063 | -48.55734 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1b8c050-66bf-3649-89d0-efb5566d575d | -2.49866 | -48.55606 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28a75079-94b7-34dc-8207-d2a413a3b97b | -2.46107 | -48.59791 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65fd1bf1-e2b3-38ec-8067-024729223be7 | -2.44891 | -48.67585 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb6b1866-3f29-3d59-b2fb-78ee3b601d6a | -2.44828 | -48.67994 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2019dd9-16ba-32c4-a090-7ce07b1683c9 | -2.32927 | -48.55865 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7edb1acf-e072-3487-a6aa-5ea850893188 | -2.32863 | -48.56281 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00139bd1-0250-31b6-8c1a-2c756ae6a109 | -2.32544 | -48.58342 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7f28eefb-d76c-34a3-bd96-85b6029850f3 | -2.32537 | -48.86552 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38e21ce1-8a64-3a03-b520-684ed0b1a33a | -2.32185 | -48.58287 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2400fe4d-b03c-3459-951d-b7b4fd4735dd | -2.1954 | -48.35733 | 2024-10-15 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ee217e-337f-3a65-a6e3-f8cea1cee6cd | -2.17967 | -48.82345 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e1df612-aa8d-39d9-9649-bfaa1aa8741a | -2.17612 | -48.82292 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eb8c360-bf12-3b3e-ab78-e7c68347b0f2 | -2.15606 | -48.81165 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f442b45-2be9-399e-8b31-b64300e76843 | -2.15252 | -48.8111 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60121809-2be4-3f78-ba81-f9a784f330ac | -2.14836 | -48.81456 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4ab6a7-924c-38a8-b8ef-4066232cc861 | -2.14787 | -48.79402 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0314f9b0-d503-3853-b440-d74b6173a81b | -2.14481 | -48.81401 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fbc529b-5bc9-32fb-ab5e-09b85fff37bd | -2.09778 | -48.81601 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18c7a7a3-41e5-3cd8-bd65-cdeed6acb915 | -2.69643 | -48.70643 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b10d93f-e04b-3766-9b1b-9c68de7511a8 | -2.69507 | -48.63133 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 651e4fd0-5300-32c9-8700-17dc62d7315b | -2.69082 | -48.63492 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36691817-8b54-39ea-a664-2ff744adb62d | -2.68925 | -48.70535 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2333a6a8-9b7c-3ce7-a0fa-43da875a3012 | -2.68704 | -48.7059 | 2024-10-15 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 186b9132-3776-3482-aa2c-636e0120e7fb | -2.64814 | -48.43184 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efee5793-1c45-3422-b090-487b7024cba9 | -2.64451 | -48.43127 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95b46f38-fe46-3bb6-8ea2-f6cb5d172438 | -2.58647 | -48.29778 | 2024-10-15 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28f16cd3-91cd-3c42-931f-8a0dae7aa4e7 | -2.20306 | -48.8597 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb2d2199-d342-3ea2-91cc-1c2177ebaa81 | -2.19305 | -48.85411 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e95a823-e279-3506-b480-a9c7280dc433 | -2.18951 | -48.85355 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59224ccb-bbda-3bd7-b270-faab7d5a433e | -2.18074 | -48.83998 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5edcc848-0a33-3574-bb7b-9e46057fdfd2 | -2.17719 | -48.83944 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 565f80cf-a6b1-34db-9b9b-5e14c3deb446 | -2.05114 | -49.49268 | 2024-10-15 04:46:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dfae58a-2d03-3939-abe1-57750987c9d3 | -2.05056 | -49.49643 | 2024-10-15 04:46:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b968051e-6c59-3cc6-b289-7cc89c176e3d | -1.91095 | -49.51775 | 2024-10-15 04:46:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aba449a1-4e09-304a-ab7f-fde30522aff8 | -1.60674 | -49.71428 | 2024-10-15 04:46:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1028af1b-48e1-3b40-80a1-a5b90ed7a38e | -1.15199 | -49.17043 | 2024-10-15 04:46:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f8edffe-38f3-32ca-a6ee-fa68eec6e74e | -1.14853 | -49.1699 | 2024-10-15 04:46:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11679401-0a3f-30ac-b324-b9af4e6c22fe | -0.87385 | -48.7028 | 2024-10-15 04:46:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f5c086-3ccb-3a9b-be9a-ff59eca6f8d6 | -0.87324 | -48.70673 | 2024-10-15 04:46:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcde6d95-4c59-3367-91c9-6b4e991c50ec | -2.49854 | -50.39965 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9576f58d-bad8-3c0c-b824-dd9d5732f09a | -2.44759 | -50.37359 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e52a7565-884a-348e-91c5-a29ddd621297 | -2.43881 | -50.24051 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394bbd9c-6e02-3964-a3fb-5bdf6310349e | -2.43657 | -50.23283 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5d197ab-8ed7-37f9-a7a1-8dc7b1927aba | -2.436 | -50.23641 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44465833-9bff-3ebb-a3a4-d04e30479e71 | -2.43544 | -50.23999 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618488b8-305a-3acf-a329-48684278ef87 | -2.43488 | -50.24357 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee0e7f3-e541-349a-b414-4b03c60c4e82 | -2.4332 | -50.2323 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e3d0154-c5e4-38f7-a384-89fb77606522 | -2.43263 | -50.23589 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5fb305f-124d-3be0-9ebf-b4c7fa2381ec | -2.43207 | -50.23947 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65f66ad-6d36-3b0c-85f4-190566f2cb88 | -2.42926 | -50.23537 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b2a5c9-61ef-3155-a2f2-51c9d465d250 | -2.3879 | -50.41148 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4a3770-4712-3200-9eb9-fe723940b2d7 | -2.3851 | -50.40741 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| ce04cb74-1427-3042-8a1b-5b53aa844da5 | -2.38455 | -50.41096 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b30683e7-8e55-374f-bdbd-b45d1d3dfc9e | -2.38399 | -50.41451 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73f2d90e-b253-35fe-b1cf-9a6271686887 | -2.38006 | -50.39573 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a2d942e-1edd-3711-83d2-1efb07c99184 | -2.37381 | -50.3256 | 2024-10-15 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1479a10e-256b-3e3a-967f-cf9a858b9ecf | -2.7103 | -49.13519 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98fa2ee8-411e-3aff-9d10-65a6fd579540 | -2.68317 | -49.05453 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 708a8cc5-3385-36ce-ab64-2ef16fa1c318 | -2.67964 | -49.05399 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db9bc132-ca85-37c0-ba90-9235049bbf39 | -2.67551 | -49.05738 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e19e86-ba62-3b23-9522-56778a57c40e | -2.65758 | -49.51756 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e224423-0bab-32bc-972d-347b472bbd80 | -2.65699 | -49.52134 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d62c4d7-e5c3-33c8-94db-342afeb5650c | -2.65412 | -49.51703 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0957e614-2346-383f-a4e8-318a373ba88d | -2.65353 | -49.52081 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README54.md)
