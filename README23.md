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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e323f0a4-282b-3b09-bbc3-2dd072124c56 | -3.96642 | -47.88239 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 71eae86b-6b2b-3585-94f0-5b312dd03b7c | -7.28645 | -49.27203 | 2025-08-12 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 323a2c57-f141-3669-b310-c82f1d9379e4 | -8.52569 | -43.31171 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e101ad17-f887-3e21-9bbd-533583a32fb4 | -7.12247 | -44.6252 | 2025-08-12 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15dc4b74-99f5-3a7e-a6b3-9fd7f8a64b45 | -7.13204 | -60.13066 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3e3bdcca-6dc5-3a8f-825b-521c31c60a05 | -7.2176 | -46.22171 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e29ac76-ffed-34d6-937f-ba7f34d9591c | -3.839 | -47.74448 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3184ef62-20b2-3026-81eb-e3238e9153d2 | -8.51891 | -43.32589 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b50dff1a-0104-323c-9ba4-be909e718e03 | -8.56723 | -54.68642 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14f082f5-4cb9-33eb-9f44-509a5a5ab986 | -9.77342 | -48.75222 | 2025-08-12 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89d656a4-46a4-30b5-97d6-6d8bb68b8bcb | -7.21253 | -46.22114 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 043d8b21-adb3-3b7f-92ab-7cf26617778f | -3.65238 | -53.68726 | 2025-08-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb167a0d-f34d-31ef-a0c0-1eadd7527b99 | -5.84762 | -59.91341 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7521025-c863-3ba8-9c4a-7a1dc7480f3a | -9.91129 | -46.1823 | 2025-08-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef3ed54-4095-3eb1-b9c5-6f8050af40ba | -7.13621 | -60.13132 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bd2e932c-e5f0-34ca-9dd0-4c43982466c2 | -3.42964 | -49.04267 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8ae34a2e-2961-31b6-a307-a0f749c1ec49 | -8.79082 | -52.05835 | 2025-08-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12c8e501-1de0-3f5b-b57a-14097b9643cc | -5.10641 | -43.15423 | 2025-08-12 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2670faa6-4d24-3573-8a45-edc5917d880c | -8.56784 | -54.70431 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13dca16d-f972-3025-bcb1-cd2b0cfc4196 | -9.64527 | -48.13799 | 2025-08-12 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ecedeaf-eb1e-336b-aa26-d7bf48d03b1c | -8.57553 | -54.6984 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e63c865-f31b-3723-bfde-de618f6a69a4 | -6.9714 | -59.27804 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0f58df16-a52b-3243-9159-6c68337e899b | -8.56002 | -54.6675 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11248828-a556-3608-aead-140958368b59 | -3.97128 | -47.87919 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 0a2c4b1d-7f6a-3e0a-b101-8ad82d9432f1 | -3.43358 | -49.04327 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 46c11404-30d5-3867-87bb-e4c7c1f7270d | -9.3488 | -50.40772 | 2025-08-12 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07ebc8b4-9522-3855-a70e-8adfeeb92e17 | -6.69312 | -59.13653 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efb4c019-7500-3982-acf4-c57a246bff79 | -7.14647 | -60.1214 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0a98c787-00dd-3dc3-8939-7a03ec6cb0d1 | -8.56898 | -54.71873 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d060f128-132e-396c-a219-022c1e59bbc9 | -7.14102 | -60.12822 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cf7eddb8-adb5-3624-9d01-fd01e6aa17b1 | -8.51947 | -43.31079 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e1f3f902-3407-360d-8c32-a00a805ac468 | -7.14232 | -60.12066 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fbdef2ca-1882-347c-b05c-28f3ec07f7a3 | -7.21334 | -46.21521 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b47f01ef-43ca-3437-9224-8bb3f0439472 | -8.56291 | -54.71421 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adfcb5c8-5b84-3eed-be46-d9c3c9920d83 | -5.84697 | -59.91726 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9e95c8c-c240-3623-b2a2-aebfb3f7c5df | -6.9697 | -59.28817 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d103c28-6046-3c87-b0ae-3a9cfaa8b1b1 | -8.56339 | -54.68938 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f663f4f9-98be-38ae-a483-afb06a746de3 | -6.7286 | -43.57885 | 2025-08-12 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e823b951-7ce4-3109-895c-53cff571d82f | -6.96181 | -60.1313 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db61d80c-aa07-34f0-9912-b717742657d9 | -7.13399 | -60.11926 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5ed03383-89de-32c4-97a3-1fccda3769ce | -4.29511 | -48.06008 | 2025-08-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f76500d-d788-3d50-b7f9-ecf72ee28e80 | -7.21681 | -46.22753 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95133aaa-f3cc-3812-a7a9-37c62b483a76 | -8.5789 | -54.72028 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36bb6971-8047-3dd2-91bf-81ff8bd21ca7 | -6.10073 | -59.9305 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b722bfc-387e-3712-89ee-4961d834f6a2 | -6.7226 | -43.57814 | 2025-08-12 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a95e88f7-bdac-393c-93c5-56930a02c8cd | -3.43708 | -49.04514 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9419a889-46f4-37b2-aa4a-391b429b9fac | -8.55948 | -54.67097 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a0c29c4-deae-35a3-840d-7de64059e57f | -5.78414 | -43.60579 | 2025-08-12 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c784842-ee56-3f0f-b862-fc57a80ca401 | -7.21213 | -46.22409 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 540e59ec-6ab4-3be4-a82b-b0d7f4a0e31c | -8.56285 | -54.69285 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75250fd8-1e57-3d09-be98-1bb08a063bba | -7.06681 | -59.21348 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2bca0b0-32f3-3bd0-8a14-fd0fa5124974 | -9.72083 | -49.48261 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 63a8eb9f-4e90-3919-be57-d57625d5b474 | -4.31099 | -48.09912 | 2025-08-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 878ce967-fa40-3bcc-9535-947a8845512d | -8.56675 | -54.71126 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50077252-7d6c-3259-824d-04a72e2dad43 | -6.5839 | -44.57253 | 2025-08-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e825f1e-20d8-3996-8401-23bec5d1afd2 | -9.04641 | -45.0836 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 827cdbc3-6076-3af1-a81d-46ce5c711676 | -8.56567 | -54.7182 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e409d60-018d-3b78-aa8b-fb2e5e3e47b6 | -7.06447 | -59.20482 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1edebc4c-e4d8-3a4f-b757-5aa928a08596 | -5.83893 | -44.10741 | 2025-08-12 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c76c635-120d-3ed7-9a7f-87d78407a1a5 | -4.0703 | -47.97084 | 2025-08-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1291eac7-a6af-3ea0-b35c-4f6f3f216b1a | -7.08592 | -59.19599 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cc635c6-18f2-34aa-966d-79770091fcc1 | -9.71192 | -49.48521 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce17925-e1c3-301d-98b5-e4ff0dd67a9a | -8.56561 | -54.69685 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e0c90b2-f9d4-3810-a3f5-d9c6dfcede8d | -8.57331 | -54.69094 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fabca6f2-d137-3bb8-a032-da2478b51414 | -9.39264 | -48.23429 | 2025-08-12 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ce8d6e9-765d-3b6e-9a68-695c48c57774 | -3.0807 | -48.85457 | 2025-08-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f49f7e-7b60-3955-89ff-5069fde52e8a | -6.96745 | -59.27737 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e8037c0-115a-3ebf-9ce3-fd80e5b32229 | -8.56838 | -54.70084 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ee8e401-221e-37c3-8209-5a4acdea5c7b | -8.51887 | -43.31573 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3ed8e2ce-6a1f-3fbd-85db-12e83085f5c0 | -8.51955 | -43.32094 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d789a01-9977-34ba-ad94-550fd1c7c115 | -7.06774 | -59.18474 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4fa6fbc-5499-3c78-bb0a-6af1a5add28b | -9.77283 | -48.75654 | 2025-08-12 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6030639b-f87f-3d56-9567-f3260868d0fe | -4.29085 | -48.05952 | 2025-08-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5ff3161-cad0-3ea2-a1f6-d8dc7f87f7ff | -8.57006 | -54.71178 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1869c479-8781-375b-8c2d-69641de8ef1a | -9.2124 | -48.52344 | 2025-08-12 04:57:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77bd5782-8e05-3131-9384-ce461ae465b1 | -7.42335 | -43.96355 | 2025-08-12 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f01cb46e-3856-3257-856f-1a0892b852e1 | -8.57944 | -54.71681 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 089a7765-d476-3786-876e-9eed7dd7f06f | -6.5854 | -44.56139 | 2025-08-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25834954-8ba9-3d35-85c6-ba9339a15829 | -6.5859 | -44.55772 | 2025-08-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ce6caf-993a-3bb8-8eda-4b37e51b3262 | -4.32346 | -54.85167 | 2025-08-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a7c9f19-90d3-394c-b358-3eae8366dcf2 | -7.4251 | -60.03611 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a8cde9-40c9-3a7d-b1c9-1605f1f68166 | -9.71246 | -49.48137 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c5ae33e-414d-39b4-9d0e-e271ba78ce0f | -6.10138 | -59.92665 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0359c646-5aab-3aa5-bf69-bc6e8d391ffb | -7.03995 | -59.81592 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4e3dd54-762f-36db-89a4-3d4da9e0764e | -7.07807 | -59.19465 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 182670d6-f7de-3b0f-9bb7-840ea57b325d | -2.58635 | -51.92483 | 2025-08-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e9139e0-951d-39d7-8648-b8336d90bf43 | -8.56886 | -54.676 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea669df9-7048-3187-bb96-cf7a41a94d37 | -8.56278 | -54.67149 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166c542d-c39f-33b9-b8a5-0c246fae048f | -8.56237 | -54.71768 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d5a32b2-36a7-34a1-af36-b35800cf2ee3 | -6.10557 | -59.92729 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 658e899d-0f93-3442-82cf-f3c706260c94 | -4.17987 | -48.63592 | 2025-08-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9c96a19-040c-380b-92a4-d652efe0c08d | -7.14019 | -59.6407 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa416aa-25de-3634-b387-732621ae60b8 | -7.06365 | -59.20991 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87d4de82-91f1-3df8-b5c6-454ede45b49b | -6.21763 | -43.32842 | 2025-08-12 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb4322c8-9280-35c1-84a8-073c54598823 | -3.43436 | -49.0382 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2b0f96b0-dd27-301f-84fb-d95423f99bbf | -6.97846 | -59.28442 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03036391-6b83-3468-ad72-7c9463fd2713 | -6.09236 | -59.92921 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87847642-2b5e-30eb-ab64-4fb7cfa3e09c | -3.8367 | -47.74512 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a9319936-7543-340a-a16b-e21c501baae6 | -8.56513 | -54.72168 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6beaeca-3040-3a7c-a984-6d8a94b5d284 | -7.07159 | -59.20909 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README24.md)
