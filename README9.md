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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f8f8535-1773-31fc-9d77-7251458c2726 | -12.48428 | -43.72794 | 2026-06-23 04:06:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f3afc764-bd62-3bdd-a1a6-383eb1625cf5 | -11.30232 | -54.72285 | 2026-06-23 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f272fe01-0e3a-361f-ae5a-87524e063fbf | -10.65837 | -47.22732 | 2026-06-23 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1005e972-9917-3b8c-a2d3-7115012566d3 | -11.90839 | -43.40572 | 2026-06-23 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e67c8c1-3314-3ffb-b480-868345c28c7f | -10.56574 | -46.2292 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7518c8c7-bb34-3aed-97e5-f7acee9a711e | -11.57617 | -47.43773 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9e1d7b9-f7e0-30be-a017-d9fb5753e526 | -10.5589 | -46.22044 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d4670a8-d388-3069-a583-5f664bded00c | -10.12098 | -52.2034 | 2026-06-23 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ca92e6d-7b00-37e8-8cc4-ea9026982874 | -9.22142 | -45.32625 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7f2383f-2d8c-3d45-8298-6c539ea1d68f | -11.97323 | -47.11502 | 2026-06-23 04:06:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f9b683-1408-393f-bfdc-85681031f0b9 | -12.48146 | -43.72345 | 2026-06-23 04:06:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c9cf016-f2d7-3b2a-a042-022b59d8289f | -11.58049 | -47.4386 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa3928df-d306-327e-aa22-9d02832bf8e0 | -9.12503 | -50.93361 | 2026-06-23 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 636408ff-afe7-3f42-adbb-5200e3d56132 | -12.86083 | -44.36242 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ed4e3f2-df37-33a8-8ca1-e1bcb57b7031 | -9.45798 | -49.8316 | 2026-06-23 04:06:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d3f63c9-281b-3df8-a586-e7adb302b276 | -7.13246 | -45.8778 | 2026-06-23 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7331ae7-1f04-3499-abfe-b2a323a2e20b | -12.65148 | -47.67501 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78e8af6f-e99e-311e-bc37-849c2244b649 | -9.49693 | -40.86462 | 2026-06-23 04:06:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8f2d75e-f728-32e2-a91d-b12803d11380 | -10.90834 | -54.13866 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b91ba7-ad7d-3fa6-8d86-6561b3637f31 | -11.30259 | -54.71936 | 2026-06-23 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7764d5f7-8847-3edd-a31d-ba5ef421dd81 | -11.05219 | -52.4642 | 2026-06-23 04:06:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6cf9a21-5dd7-36ff-a58f-9672fbaab9dd | -11.89362 | -43.83597 | 2026-06-23 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70f10a76-9177-3c47-95ff-ec24ba76c06c | -11.30946 | -54.72079 | 2026-06-23 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ff03c1e-be96-3282-8f7f-fe6e45269469 | -11.80086 | -52.52693 | 2026-06-23 04:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11bc4990-b775-34cb-85dd-422beb7653f0 | -9.82528 | -48.22339 | 2026-06-23 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b3f2080-92ab-3e62-8b7c-866ba54b8115 | -12.87006 | -44.37251 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef3509ba-9b16-36d4-95e1-bcd08aafc934 | -8.87282 | -46.93985 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69e85f07-010d-30bd-898e-eebd19409eac | -11.97744 | -47.11582 | 2026-06-23 04:06:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39d7c6e3-3404-3aed-a44b-707534ae17f9 | -10.77514 | -54.11579 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf34b995-f69a-3fc6-82ae-1b037c9bba63 | -9.36857 | -50.53667 | 2026-06-23 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e4560f6-7111-31ed-88e3-cb53bb67d725 | -9.06409 | -44.75049 | 2026-06-23 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f481f0bd-024e-3367-83ce-9d5a0d22d11f | -12.92685 | -43.61878 | 2026-06-23 04:06:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d8d5c75-8c57-33b3-aa31-ccfe86a6768d | -12.86153 | -44.35832 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cbe92d20-a8a9-3972-8e02-08eb51c10161 | -8.08159 | -46.39256 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bbc3ddc-9979-393a-bea2-06642d6f99c1 | -9.44816 | -50.842 | 2026-06-23 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983b4522-6410-3f3a-adb0-60320595cc3c | -11.04517 | -52.4678 | 2026-06-23 04:06:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd72b912-6a96-3ea8-b0b6-b2cb49d67326 | -12.85798 | -44.35769 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c298487f-25e4-3a4f-8810-2a9ddc26d823 | -12.03498 | -47.80389 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e1aea53-0971-3052-922e-60529cfd80e4 | -8.08649 | -46.3897 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da263ef4-8770-3655-a376-e693dca49f59 | -9.74 | -47.88186 | 2026-06-23 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d657579c-bfc1-3edd-a87c-2a9fd5468842 | -10.40225 | -49.44374 | 2026-06-23 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 356c2b5e-a472-31a8-974b-e6fcf1201b9c | -8.3572 | -50.50261 | 2026-06-23 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a111aa-fa3f-384c-8655-24e3a58852c6 | -12.86367 | -44.36714 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 950ce742-1ff4-3ae1-9297-f47ddb6e0a61 | -12.6601 | -47.67667 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90966e8e-107e-371a-833f-eb17ee858e50 | -10.12191 | -52.19868 | 2026-06-23 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2be7f5c-9c71-303f-9a08-3d69f62f3e76 | -10.88413 | -49.54766 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5db90f28-faaf-30e4-8c4f-ce82c0e91b48 | -12.02614 | -47.80252 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9403ec9-c9ce-36f3-ac66-acc6d929e234 | -12.50172 | -48.2714 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b9c68ff-d462-3097-be7b-0111feb87a3c | -8.31575 | -45.3933 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bc4ce37-c9e0-3fb4-9cff-a4eb2cedcbc6 | -11.81457 | -47.34563 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 247a74ce-ae95-3efb-95be-349c1dbb0aed | -6.93639 | -51.93986 | 2026-06-23 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd218e18-755e-3c42-a134-1a090f9e439e | -6.93285 | -51.94058 | 2026-06-23 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f3c92cd-145f-350c-a4e3-1af2df1637dc | -7.72033 | -44.17107 | 2026-06-23 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3b7c5d3-c70c-3ab0-8235-509470b0c227 | -11.81104 | -47.34067 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02a7581c-ef4e-3d66-ad9a-174812c7b47e | -7.91586 | -48.25296 | 2026-06-23 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d64c58a9-cd8a-3f11-888b-598523974d1e | -10.40339 | -49.44634 | 2026-06-23 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6f25522-8f96-334a-a3ce-8a0a3d0f0b91 | -7.91193 | -48.24667 | 2026-06-23 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abaa3bad-84ae-3d48-8813-1bb983aac958 | -10.56637 | -46.22561 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a91cb366-ac28-3142-8858-0404a3d22706 | -11.83717 | -47.07412 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1189be9c-62ff-3c20-9f46-508ce4d9d7fc | -12.50257 | -48.2668 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 074e12e4-5d24-332b-8e8c-017bc0d0c79d | -12.86652 | -44.37188 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfc800d6-9090-37df-ab36-ea7fd763f198 | -14.06488 | -39.48986 | 2026-06-23 04:06:00 | NOAA-20 | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8969a22f-9ea1-3107-a70d-62dd94eb5118 | -11.27523 | -44.52598 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53bd2c2e-79b5-387b-94d9-bd6cdd8b7172 | -11.61204 | -43.11962 | 2026-06-23 04:06:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7f4ae1d9-fe72-3a20-bbea-a21fb6812db1 | -7.36075 | -47.02291 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd88332b-b21c-376f-b6f6-667c2733a547 | -8.32284 | -47.55538 | 2026-06-23 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c314dce-b2b7-3fd4-9eb3-075f43ebc217 | -10.11131 | -47.55185 | 2026-06-23 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25bb4381-72d5-33ab-9c4b-72cb7db48d55 | -8.08583 | -46.39355 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ce367c4-4457-3792-8f6a-fb1ef7b6980c | -11.5711 | -47.44106 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2acb24c-de61-386b-a280-c48d673ff509 | -11.28009 | -43.34218 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dc3ffdc9-189f-3bed-9685-41e63c1a25a6 | -12.85444 | -44.35706 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 491f4d05-9a6f-336d-a868-3de7d1572fc9 | -10.56979 | -46.22997 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72adb318-8c54-3ba7-9eb6-c1aa31f18597 | -11.81606 | -47.33731 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 940fab7b-8fd1-3c37-861a-c0d647cc5a08 | -11.29236 | -43.33243 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4c70b0b7-4f13-3e0c-ba33-014a5c34a657 | -10.974 | -48.15432 | 2026-06-23 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9c1d564-b5e7-3ca6-94a6-c3933e45e0bb | -7.72117 | -44.56129 | 2026-06-23 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db9f71a-da66-32f3-ada2-a29951b305d6 | -12.87499 | -44.36496 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03fa8ce2-df1f-3f76-a74f-40375caa4121 | -8.07928 | -46.38035 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f71c790-e86d-36c9-acb0-37e5bb8f034b | -11.27159 | -44.52533 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d706b18-66c7-37c6-99c5-5f94885f9f4d | -7.90943 | -48.24837 | 2026-06-23 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76fd5f1a-3006-3685-a58b-74cbd3910537 | -12.01149 | -40.11362 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 911aadd8-c61d-3f32-ba1a-0511f45e04bc | -9.45696 | -49.83154 | 2026-06-23 04:06:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 751f1622-cdda-3b20-bacf-c133547ffece | -9.57652 | -49.1171 | 2026-06-23 04:06:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b043e696-6f30-368e-b47b-8888753e5790 | -12.5155 | -48.29781 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| eb9e5afd-2331-32f7-9bbb-16399b3aea41 | -12.12348 | -38.67079 | 2026-06-23 04:06:00 | NOAA-20 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c23f8d5-cb02-3378-82a5-a30a3bdb06cc | -10.9701 | -48.15205 | 2026-06-23 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a5d2685-4bee-3976-83fb-2470996bc547 | -11.80675 | -47.33989 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 719edd4c-9146-30ab-b1a5-181955de254c | -12.48493 | -43.72405 | 2026-06-23 04:06:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0035dbd-4cc9-371e-9e8a-a6597566908a | -7.9143 | -48.24923 | 2026-06-23 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e016e350-473e-3496-b465-c1b649b56da6 | -10.56232 | -46.22481 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd6b2f9e-b2a3-3513-a503-b2330b463d17 | -12.85659 | -44.36589 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f434eeb5-9d83-3a8b-852c-046b068bfbd0 | -8.86252 | -46.9471 | 2026-06-23 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1994adf-bdbb-3c41-ad09-c3ac5ae4b34a | -12.86861 | -44.35958 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 98798bb1-9b5b-3620-8523-ebecaa95986e | -9.21751 | -45.32553 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdf85976-0170-3431-8e97-3ad423983085 | -8.86331 | -46.94257 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a21d2252-24fb-3ac2-b891-1b81700de71d | -12.85729 | -44.36179 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 652c25c5-f521-3b95-a701-bec31594e1e2 | -11.80601 | -47.34402 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8131401d-f122-39b6-800e-6c876e79c4db | -11.28354 | -43.34278 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4014c13c-78be-3b5b-aab3-acb288f09db2 | -10.97489 | -48.14948 | 2026-06-23 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4bfc0308-d830-364b-af07-7487597b9f63 | -13.89551 | -43.78977 | 2026-06-23 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
