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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c12140ed-6b9d-36e0-beac-63fe0582d6b6 | -6.12983 | -47.27686 | 2024-10-11 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bbc7ec06-e381-3867-a235-cda8927d8942 | -6.12426 | -47.2709 | 2024-10-11 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 768f4925-8490-3cc9-b588-4d621af94b64 | -6.12358 | -47.27586 | 2024-10-11 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 918f053d-9b0f-35ab-97a4-a88b551d3773 | -5.83896 | -47.43232 | 2024-10-11 05:16:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de4f46f5-0ee5-322c-af2e-b74da09a7ae8 | -5.64713 | -47.92767 | 2024-10-11 05:16:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f48f4e4-8bb9-3422-99b6-34b842003721 | -1.99993 | -47.25759 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a4c6541-7982-3b9f-ac11-550e7d689350 | -1.9963 | -47.25555 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec6d4625-55fa-369f-8ced-d3c287e545cb | -1.99402 | -47.25664 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0debc31d-97c1-3fb2-9e3e-4d34fc9cc8b1 | -1.9073 | -47.8865 | 2024-10-11 05:16:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83c23e76-250f-3669-b537-f6880671f3b6 | -2.80794 | -48.70451 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cc900c7c-a93f-3701-a85e-58ddab61b2ea | -2.80742 | -48.70801 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f6d21f68-06ae-3d32-83d3-771d1ac4019f | -2.80355 | -48.69663 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb990902-5439-30ee-bd22-d2552a3cce34 | -2.80302 | -48.70016 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23189883-c62e-320b-aca3-a3ea8ef77d75 | -2.75382 | -48.68316 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e777810-7211-3047-9cf6-151d351d335f | -2.75014 | -48.68105 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e32fb1cf-07dd-3b9b-8edc-357c1cc29104 | -2.74963 | -48.68457 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50191eb5-4921-34ab-a028-cdc00e17aa78 | -2.74837 | -48.68235 | 2024-10-11 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b30dedf-ee04-35ca-9b31-e1b8281dc71b | -3.4612 | -47.66343 | 2024-10-11 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a10abb4-8767-399c-877c-73a4a31e7c6e | -2.97287 | -48.00057 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74f04dd4-8d9a-3330-bd1a-a8a10f6f2efb | -2.97228 | -48.00461 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 936e0d40-3266-3b87-ac3e-5b6040a2b7e5 | -2.97149 | -47.99845 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e40eb58a-9905-37c5-80b0-983d0c169ef9 | -2.97088 | -48.00249 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 694895b3-2336-3fc3-9a19-172f1e42e86f | -2.96716 | -47.99962 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 859f3aed-25f0-3748-867e-13892e4b7c89 | -2.46112 | -47.84124 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa0a6b42-73ad-3d8d-9e53-b69babdb73fe | -2.4594 | -47.84181 | 2024-10-11 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a8d7ca-559b-3ada-a1d3-9f85303e7bd6 | -2.23796 | -48.02075 | 2024-10-11 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1ed8cf7-f4d2-3efb-a9ec-a8d8520b68c1 | -2.2374 | -48.02453 | 2024-10-11 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70163cde-73ae-32d3-8e27-f2f8eaddc881 | -2.18818 | -48.24065 | 2024-10-11 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3d8748b-ecbf-3443-9ca7-de36ad28ef84 | -4.97285 | -47.92882 | 2024-10-11 05:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a00d5f1-0c61-3a28-87e3-3050a33443d3 | -4.69737 | -48.62453 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aee0e044-8cc2-3d70-a7f2-30d9a60086d3 | -4.69418 | -48.62069 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01019911-ab2e-3cf4-81d6-2f34ce0341b8 | -4.31939 | -48.6347 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 024d74eb-8e9b-36ea-a16f-082a68adbfcc | -4.31886 | -48.6384 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cf680b4-f0e0-387a-b978-1a03ff4877b6 | -4.31831 | -48.64217 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab9dd923-1efb-3610-9f44-f069ece4c589 | -4.31381 | -48.6338 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d57d6516-705f-3143-8ac3-4360f8ae849e | -4.31327 | -48.63754 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 641608b4-3db1-3dad-8865-2f3c5bda30cc | -4.29198 | -48.62662 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 145e5040-e4eb-33f7-a668-4ee8503e899e | -4.29145 | -48.63035 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 333a2d62-a9de-3a84-97c2-453bdff4fd66 | -4.29092 | -48.63407 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c53f1acb-8c4c-3733-af11-b339a71a002f | -4.28533 | -48.6332 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53653a8b-ae42-347c-a1ba-b4f137edb91b | -4.25587 | -48.64779 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4014289f-051c-3c46-bbb4-460d79b3ee96 | -4.25533 | -48.65149 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05008905-46a1-3c92-b741-b5a6ad766e81 | -4.25483 | -48.64716 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba00463f-4155-346c-b762-f25b9b5fbe7b | -4.25431 | -48.65089 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5b0cc9c-1678-3a35-aade-7de5bc4d998e | -4.11065 | -49.06731 | 2024-10-11 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25531fe3-6499-343a-94c8-8757ebd225e7 | -4.10524 | -49.06644 | 2024-10-11 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72b0db0f-8f51-311f-9f93-8d9fd2b3c811 | -4.10476 | -49.06986 | 2024-10-11 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ff45ea3-f3eb-3c29-9902-640cd9f9fa8e | -3.92147 | -48.34447 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8365ff9e-61cc-3f8b-bda7-7bb70a21d9ca | -3.91633 | -48.33994 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa2a03cb-a373-3d97-8bc4-f4e4237a1e97 | -3.9158 | -48.34366 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ea25e8e-3882-3722-b32d-884aca4a1288 | -3.91525 | -48.34742 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6dbddade-5847-3ded-832d-0be2ce94bdda | -3.9147 | -48.35123 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07f22fbb-d5b4-3f37-aded-b27c7cc54f80 | -3.91415 | -48.35505 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 741f822c-b76b-3c65-bbd7-76f6df6481e0 | -3.91065 | -48.33919 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c85d36-431c-3c60-b17b-dee3bd8b66c5 | -3.91011 | -48.34296 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b2922ac-b008-36d7-a0f0-ed95b209e16e | -3.89607 | -48.36015 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6baee803-1265-3ea6-a011-69427c73cec9 | -3.81355 | -48.97393 | 2024-10-11 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e6b88da-3e1a-3803-bbf4-382952a1bd29 | -3.81305 | -48.97739 | 2024-10-11 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c3eea9-7357-3725-9551-c7b2868efda3 | -4.48385 | -48.11024 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 14343b0d-b064-3532-a3a7-139476026374 | -3.80558 | -47.79096 | 2024-10-11 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| accf5521-d849-33ae-a625-b69203d14c31 | -3.76587 | -48.10332 | 2024-10-11 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98b8f58d-720f-365e-a091-9932e856a99c | -4.27695 | -48.22662 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 815bf16f-1116-3374-9ad0-2c4b1a3a685f | -4.27122 | -48.22562 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5851ef9-2f48-3dda-b892-af64a97e8f3e | -4.27067 | -48.22943 | 2024-10-11 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52008f96-cc4f-386d-835f-fe4e1543c660 | -4.12 | -48.24941 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0af716c9-05c1-3ac8-bf94-553486727f92 | -4.11944 | -48.25335 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 473f8b9a-5b4d-3253-86d7-e5f56678b697 | -4.11889 | -48.25721 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f45f16d0-07a9-30a6-a9af-33d48ef6b07b | -4.11781 | -48.26482 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf008536-d640-31b4-baea-ad2b9d9c5956 | -4.11728 | -48.26857 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18163815-cfb2-3146-9fce-ad1bbfb35e31 | -4.11674 | -48.27238 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3145278b-818d-341a-b39b-c26edb6a1b79 | -4.11619 | -48.27623 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58b6f952-364b-360b-976d-dc2d1222b795 | -4.11603 | -48.23613 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01a0b079-de92-3c1a-847c-345047552c8c | -4.11543 | -48.24039 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 819b5514-1b32-3bff-afe6-dfe68637087c | -4.11427 | -48.24857 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2a6a7fdf-de69-3298-8b4d-761a60a44034 | -4.11372 | -48.25251 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0f844068-43ae-39d8-ae65-2859d74506c7 | -4.11365 | -48.23908 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a369f31c-2afc-3857-9b84-f511a1a60133 | -4.11317 | -48.2564 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8d84ca96-8f89-3707-b1d3-b6f2d7f01437 | -4.11304 | -48.24321 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 28d04658-da02-39e8-a2f5-08032d756391 | -4.11262 | -48.26023 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 85b40bd7-9b92-3cfb-bafd-c5e3248056b1 | -4.11244 | -48.24725 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c1d859f5-e5c4-3ac8-8ac6-e2d498140cf3 | -4.11209 | -48.26402 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa74d662-5163-38f8-adfc-63202d086b22 | -4.11185 | -48.25119 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 303481c8-2494-3bbc-827d-aba7efca97bb | -4.11156 | -48.26776 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7489dfc2-87c9-3181-b7fd-bb8a2bd09f27 | -4.11127 | -48.2551 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7b00ade1-b63f-388d-9adf-831449f9c62f | -4.11103 | -48.27152 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68c81da9-7e37-3ac8-814c-64bbbb1dab8b | -4.1107 | -48.2589 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2121e7b0-06fb-3735-8769-1e73a229397c | -4.11014 | -48.26268 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5fc78d9d-f257-3939-aa7b-6aa8330b3980 | -4.1097 | -48.23954 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5608fe00-b688-3af0-9c5f-f7bc90aeff52 | -4.10958 | -48.26643 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32b04a2c-93d0-3f25-9dd0-f6aeb41e6b8f | -4.10913 | -48.24364 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b3e4f599-f858-3880-aca8-f3f4484bab62 | -4.10903 | -48.27018 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31989d06-a9fb-3c0a-b154-200527d6ce38 | -4.10856 | -48.24767 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6ab8cf97-968a-3c6a-a773-8c9f606fe0ee | -4.10846 | -48.27397 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d06d1ed5-4f77-38c8-b8f3-2951628705f8 | -4.108 | -48.25161 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 48573ea1-60ce-32b7-84ce-76cd2fa8ce4a | -4.10794 | -48.23816 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4ef477f-6e21-398d-bf38-4030a74a7468 | -4.10746 | -48.2555 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3fcaaab2-9ab6-313f-8c24-8ffe2cb00817 | -4.10733 | -48.24226 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| d2fa0307-baf6-3428-adb6-8933808990bf | -4.10692 | -48.25928 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 947f967b-b145-3181-b951-8125f20291da | -4.10673 | -48.24633 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 06570518-79fd-3e3e-bb48-9ad1e4637874 | -4.10639 | -48.26306 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README76.md)
