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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c529444-cb07-349f-b1aa-77ef7baa36fe | -9.71496 | -54.81893 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56ed740e-fc1a-3c52-ab45-645198a955bc | -4.17769 | -51.24715 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98387c43-1b14-353b-970d-c1525934cc1a | -11.32165 | -47.35917 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75d531e5-25f7-3b82-916e-2a6eda28452e | -9.60859 | -45.377 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 887eb792-2a96-32a5-93d6-c4a108d6ecac | -4.25838 | -48.53972 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 452c88ae-7cb6-3e71-aba6-05d4d8d1db9d | -2.8997 | -57.79601 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bb9dd347-6c69-364b-b669-1a42abf8961d | -5.8903 | -52.0849 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67d962dc-121e-3316-974c-4cb4fc311155 | -10.53737 | -46.7469 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4e311d05-20c1-334c-b0a1-484cdaf832ab | -6.66666 | -50.89785 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 442cfe3a-fd6d-3927-9c84-3d7ad20d1305 | -9.24971 | -57.137 | 2026-09-19 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58fcc0a6-3480-305a-b43e-b59253f8e7aa | -9.80221 | -48.32684 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a661bbb6-3593-31e7-9d9a-772290dca569 | -2.9759 | -54.76351 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77708867-71b7-3a04-aaf0-76ee0d4111d8 | -8.16564 | -54.8129 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f9ad007-b93a-3219-b1de-decad24aa01c | -11.0793 | -48.31106 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 105c10a6-ba85-3249-aed1-fd3de3d06a32 | -4.56487 | -54.90807 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e9b49c3-34db-3110-9683-227c222cd0dd | -7.04303 | -55.44136 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6139999a-ca4f-3bd9-a8d2-6c1791682183 | -4.32045 | -60.88398 | 2026-09-19 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d6aa19f-cfad-3bff-87bc-922f1f3afe24 | -7.06897 | -47.53996 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9a205bed-2373-39e9-b731-65a57138d298 | -10.48885 | -46.29746 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86da687f-eef9-3dc3-a6d3-29d82ff135cd | -7.76208 | -46.73853 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c067e74-0b29-39b1-917d-64b7d128fa17 | -5.88248 | -52.04802 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8741e63-cfd1-36ac-a54c-e7f2c821e7ad | -6.67236 | -50.90631 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09da3a60-0c72-31ee-9016-132dc7243c7e | -5.83444 | -52.02948 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0262d04e-413b-394b-bd69-89c00779f431 | -5.93099 | -53.52216 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6aa2bceb-3928-3de6-b254-1e385bbbf525 | -8.63662 | -47.53668 | 2026-09-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f6c55b9-2684-3343-8086-13906f839f65 | -6.99509 | -49.76601 | 2026-09-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8555eb8a-2340-3dee-bd51-265373623205 | -6.98759 | -42.18301 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 16bba660-cfcd-3794-8511-9c5096b09378 | -4.54996 | -54.9334 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1c25f12-ee28-36b3-a148-2670da6c0ce6 | -5.8908 | -49.78898 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bc7e587-a33f-39a4-b9b5-30c12c96cb31 | -6.66209 | -50.90466 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f1cb75e-beea-34d9-b01d-9e3ab1a5d0f2 | -3.73068 | -54.64552 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9858850-e96b-39e8-8282-acd32276dc61 | -9.65365 | -49.14477 | 2026-09-19 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11342275-0293-3743-b9b3-feefa071aca8 | -6.00408 | -51.79461 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cea8d8d-5dc4-304a-a02c-e600896e9445 | -4.55732 | -42.9781 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82073cc9-271f-37e3-bbe4-de41f1dc0cd3 | -5.86935 | -52.11 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0220ab01-91e0-307e-b152-3af1ae3c632f | -11.08572 | -48.27401 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a1e328b-c2d8-33e4-9950-16c3f32ee4f4 | -8.87964 | -50.7839 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e68281-8d0a-3f6d-a7eb-12704e2b758b | -6.33127 | -55.27774 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7cc5a738-1d74-3516-b24a-cf7c73e70fc7 | -9.25064 | -45.92946 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63ec1d1f-6772-3bb8-93a6-db74db9c15a2 | -3.49575 | -49.51035 | 2026-09-19 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d68b7f9c-3d9f-3802-9b6d-b913bcab8066 | -5.3832 | -55.88372 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d96a5d62-6a94-347b-870b-efca13279be0 | -3.36081 | -50.46312 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b8db6a5-2d70-3325-a650-7424c6576fea | -10.32413 | -53.58112 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d16788fb-a59d-34e2-826c-24cdd78c1601 | -4.55088 | -54.90576 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68788d96-4a6e-3450-a79e-1e7b0d6f1006 | -8.61236 | -54.61422 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf17ba7-5efb-3011-8e2f-afb4cd4a37c7 | -7.06588 | -47.53233 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 54da7909-7c46-3294-974e-26a20ae6cdc7 | -7.79317 | -44.84755 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c87715e8-5372-379b-91b1-648d5438c00f | -9.66711 | -54.31493 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a9a6f0c-95c7-327d-992c-d74fa2c0ecfb | -6.02448 | -51.76829 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff099081-0287-34a5-8cea-eb79f51cee42 | -9.34551 | -50.18326 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 676b2851-5370-3b38-b96f-a326aba62f1f | -8.6628 | -45.45657 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c592066-1aa3-3599-80b3-47158bf5db1b | -6.80131 | -59.16281 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b281fecd-3bb2-33ba-919c-0a5ba5744d3e | -5.7477 | -57.58035 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c94af6d4-5ff5-3096-8bd4-91bdaa2a8591 | -6.09022 | -55.55188 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b968502f-21bc-347f-b46e-f535d46f3edc | -8.89651 | -62.44545 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a883e7f5-475f-3201-a657-7c60a229cec3 | -5.89341 | -49.78823 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f5e4605-065a-3bb6-a681-aeff3a283830 | -8.164 | -54.73789 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1869bd07-30ef-32ed-a5d3-8cd9ec32f16e | -7.60226 | -45.42488 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7bbb7313-1905-349e-a90f-c8f42c68bd0f | -8.45436 | -47.66283 | 2026-09-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a06d1d95-a5c2-369f-934f-175ca2deae98 | -5.25681 | -50.97472 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa4088e0-fa46-3279-8bfd-33d34e1b8434 | -10.12943 | -45.56317 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bab67ab4-a25c-3058-81fb-dba256a9b8a7 | -11.08151 | -48.27367 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d0acd54-109c-3128-bef2-9c5672a20b79 | -9.03856 | -48.75413 | 2026-09-19 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 234b4fbb-be4b-3c07-bcb8-90c7c0d6d01a | -4.56329 | -42.97528 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5f3327c-9d35-34a8-942b-21af16c60100 | -4.215 | -56.3306 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3b80a91-ee42-3616-8bae-9006e1c2b270 | -5.88985 | -49.78767 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 534ab0f6-aefe-3f9c-8015-86257e2b547a | -9.72006 | -54.80872 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| debff168-698c-373f-8cd2-0add5fbabab3 | -7.60635 | -45.431 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bafd6b10-7920-354d-8ad6-2c19dd2c4793 | -8.46818 | -47.01062 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35b2faf5-9a42-3ba0-956b-52ffd7040d3c | -8.98949 | -50.16895 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2242f61c-ab1f-3f6b-8595-2130036a7407 | -10.58915 | -46.60495 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2979f0f6-3c2d-3bc0-98f4-60ca5ffbc612 | -10.48411 | -46.29681 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35fa19a-26c8-34f9-98c3-b08e1ef85f87 | -7.1984 | -47.87154 | 2026-09-19 04:57:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bf7a087-b7a3-37d5-9e6c-a5fec0889243 | -5.75712 | -57.45231 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5269798-06db-3351-a2b5-bd537bf660da | -9.70373 | -54.82449 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4989199-8e95-36b6-8eed-8669acf0bd21 | -3.84826 | -50.01241 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ac35772c-f83b-34ad-b443-51058a66291c | -9.8925 | -46.54542 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccc12fd1-adb1-3670-b513-4a561e655839 | -7.05127 | -47.48784 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 702cf250-2a0e-3669-ae72-7f8c8895ed84 | -7.57961 | -57.69229 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b4e33d9-066f-3943-a5d4-7ea4d9b3694c | -6.66151 | -50.90838 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 652c17c7-c4bb-3306-98c5-80189e4def57 | -10.70099 | -50.25419 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 429c792d-0ba8-30a9-b891-da0bfec1cdf3 | -7.40145 | -49.84748 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2c9b341-3d1e-3fd7-95e1-803a7f2bae28 | -5.33092 | -48.98613 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f31017ff-05bc-3604-ae55-9404b86c72e5 | -8.89057 | -62.4455 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24ecbe9f-9fce-3b85-a4ba-d3c263dd340a | -7.02409 | -47.44115 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36a3d8b7-2b46-362b-a3dc-890d9abecacc | -7.55957 | -61.3361 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd63a660-87d3-3bf3-8ba7-6fabd0180882 | -4.81405 | -56.08604 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95300dc4-8a18-3739-afa5-d94560ad3091 | -8.84332 | -50.44917 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01e9b59-6e60-3b21-bc2a-e2924897a162 | -10.497 | -46.27197 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a106d3c3-bba6-393a-bfd9-0a87097eef46 | -5.86642 | -52.04195 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab098be5-c8d0-3670-9eac-5929538e8ebd | -4.88046 | -56.07465 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5858fcd1-b2ba-322c-95b2-eec7bddcff91 | -9.55608 | -46.57939 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3bfecb6-9438-3d0e-ab5c-50ff84b19740 | -10.17726 | -48.52132 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95c84e24-82a8-3a31-854a-18773f237d32 | -6.80567 | -59.16355 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0bb5a19-6af7-38cd-911b-9839cbf942dd | -10.4825 | -46.30138 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1aaf08bc-ff38-3152-aee2-f7e1921a08dc | -9.0076 | -44.91606 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a9c3d58-262e-395f-a28c-da8cda4c0fbb | -9.24522 | -45.93217 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c23b1ca-e67f-3815-a38b-e9a42a4f4382 | -9.25155 | -46.20911 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3955d305-9ded-3a57-a307-8db3d47e9fde | -8.77097 | -48.6654 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c9796fe-e926-3998-9b1a-ab114dad98a7 | -9.0469 | -48.72464 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README79.md)
