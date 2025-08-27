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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44601dd1-3c1e-398f-81cb-f7eb54aaa94e | -10.2639 | -64.476601 | 2025-08-27 01:11:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ecf09e3-1b4a-38b3-be90-2f5bdf82fd6b | -6.6282 | -58.545101 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0c1bcc-b1a0-389a-89c6-6b3764c94eca | -6.823 | -58.9566 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e67f7f64-9e9b-322d-a76b-c235524b27e6 | -9.1713 | -59.500702 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 710e9068-6911-3d1c-b319-63c36e24529b | -8.9468 | -65.901703 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67f2761b-2244-3d99-92b0-55cf063c4849 | -19.5595 | -47.535198 | 2025-08-27 01:11:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 04de1451-fbd2-3f76-88b9-e5218157721e | -10.5212 | -57.972198 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f29d047-d561-3172-a832-3eef8bcf4b24 | -7.3461 | -59.647099 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61e4897a-060f-34e8-8764-8cdac9b9ace6 | -9.1987 | -59.532398 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb3fcffb-abb0-3945-97ad-242b16251062 | -9.1836 | -60.7925 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc9f14c-2641-3459-a359-1696b8b6f8cf | -6.6774 | -58.8568 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90b6fe45-78a7-339e-8eab-031887240c9b | -9.1365 | -50.7738 | 2025-08-27 01:11:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9126274d-dad9-38b3-95f0-84e8aa13fbd0 | -9.2853 | -56.8974 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c83f8dbe-c93e-322b-8671-9e1a1ceb9ffe | -6.8266 | -58.9725 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8976c3d6-87ca-3a23-a903-c46e6eb42bf1 | -6.7117 | -58.550701 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72912392-bc2f-33af-b8d3-c406b371d03e | -6.7867 | -59.625301 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54802682-7b36-3a88-8087-f3c3b328794c | -9.0909 | -49.574402 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2ac9674-52f3-3f61-b0e9-de75d83f9a82 | -6.8772 | -59.8951 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74d77437-a860-3fb6-98f7-d52510dba2ca | -9.134 | -50.763401 | 2025-08-27 01:11:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06d5182-4806-3d26-b7c1-d5ec8914ab2c | -6.2424 | -59.996399 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5af9f70d-7639-377c-b942-cdd2a0bd1151 | -9.7937 | -64.2519 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fcc36cf3-076d-3151-a409-5ec3a0bb42dc | -21.101 | -48.835899 | 2025-08-27 01:11:00 | METOP-C | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 295efe06-8ebe-3faa-bbac-da722e000490 | -9.5702 | -55.3783 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32406c79-07bd-3dc5-89fc-37481228b7e6 | -6.7746 | -59.663502 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 330ce640-122a-39c5-a6c0-80d3db5ed58c | -9.1654 | -59.567902 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 032fb6d0-1aff-3fbb-a81d-21f16666f2b6 | -21.1084 | -48.8237 | 2025-08-27 01:11:00 | METOP-C | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5588d74-0db8-35f4-b2b4-f4e0d2b83619 | -9.1957 | -60.800999 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0d970b-f4d0-3c8c-a394-3a699fde31e2 | -9.6192 | -55.3671 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 411cccca-74df-34d0-bb59-5378a08af60d | -7.1812 | -59.737499 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af66b471-9167-3cbe-ac8c-1fca4b0c9562 | -9.1948 | -59.5144 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac550025-4c27-3abf-b4a7-f60c7101a638 | -9.1755 | -60.850101 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4433b7da-8c96-37ce-b229-fccaf0c33262 | -9.5996 | -55.371498 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 204560c5-d31b-37d7-9dcd-4dbf9bc6c68d | -9.1712 | -59.547699 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 603980e4-27a4-37f2-84e8-7ef8ac9e0e68 | -6.2482 | -60.022701 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9835f28b-6961-360c-aed1-9ae858e38a7f | -6.8328 | -58.954498 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59ce183a-c1df-3d6f-a97c-5f6cb57469f9 | -9.1037 | -49.584301 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98a0abaf-19fb-371f-be52-56080971f522 | -21.5833 | -47.479301 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0d4e60d9-2163-3483-8f59-91ffb96f4f78 | -9.9248 | -54.719501 | 2025-08-27 01:11:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1a3567-5192-31f7-a61a-2aa9692c20ab | -8.9612 | -65.972801 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce46e0fb-9e35-3a2d-bfd4-a7b60b252859 | -9.7959 | -64.212898 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 626cc827-63f4-3920-bb8c-c23a25fc3e9f | -5.4528 | -60.140999 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2f27221-4d13-3d77-b953-63c40caed279 | -9.4157 | -60.4911 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13f0c564-4f79-3d13-8584-935d821445b8 | -21.593 | -47.476501 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec57ff60-ca92-3cf8-85e3-437f3df59bc4 | -5.7613 | -53.771801 | 2025-08-27 01:11:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92659367-c242-326b-8a37-6a96791f78b1 | -8.8794 | -60.757401 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 623b724e-1947-3758-b9bd-5d3b7e192e71 | -8.9419 | -65.9272 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dea7c08-5ca0-3705-9ef8-ffbe86f574c6 | -9.0629 | -66.027496 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85bd98ba-886b-3ac2-8a53-68ea5de3d146 | -7.7352 | -50.276299 | 2025-08-27 01:11:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78f4690a-21cb-33be-b367-d8c8876bb7cf | -5.355 | -60.393398 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a68c1d7-124f-3a4c-aeeb-b63c73e227a3 | -9.1693 | -59.5387 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad882d1-7fea-3ff4-9b96-ced9efdbbceb | -9.167 | -60.7626 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15991142-4e3d-385a-a24c-c6c53aceb035 | -4.0958 | -55.7985 | 2025-08-27 01:11:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df4d79e1-5f99-38bd-acd8-41c27740cfc7 | -7.738 | -50.287998 | 2025-08-27 01:11:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afcfca38-db83-32b4-9070-b78727437c11 | -9.4103 | -60.513802 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b57a34af-de5e-33ee-b87f-231b1538c3a5 | -10.2736 | -64.474701 | 2025-08-27 01:11:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 767a387c-1655-321c-86a3-ddd7f70a37bb | -8.8817 | -60.768002 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0445f43-2487-3a45-bedc-56047fb7c35e | -20.685101 | -49.257198 | 2025-08-27 01:11:00 | METOP-C | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6fdd85d-7bb5-3867-9e3a-acce21623cb9 | -9.6177 | -55.360199 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28a030c4-ddf2-3274-8829-2d9a9aebd01d | -5.353 | -60.384499 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 931b55b9-a55a-3860-a758-79446340389f | -7.2788 | -46.9828 | 2025-08-27 01:11:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac36b78-8cb8-33f1-8be7-ebe79fb030c3 | -9.1733 | -59.462799 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 093d8f31-43f5-3056-8ed7-45433a2455bb | -6.6872 | -58.854698 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5f9eeb-c1a3-3f1e-844f-73024043a109 | -6.6554 | -53.183601 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 048c5baa-3eb5-3204-aca6-7d2c93f1d301 | -6.7648 | -59.665699 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a245653c-8411-394b-9bac-7a59146be654 | -9.1673 | -59.529701 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0f5a2ce-3262-360e-bafd-47eb55103d95 | -9.1831 | -59.460701 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2d67dbe-9fe1-34ff-ab34-aca048e9b820 | -8.0727 | -61.5242 | 2025-08-27 01:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4522f52-ddfe-3d63-a1b2-a056bd5f1d38 | -6.9174 | -52.849998 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a431a96-d020-3751-90f8-48e0b48fc6ee | -8.9129 | -65.884003 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0c70294-e5e5-373e-86c6-fb9b11c853e6 | -4.9661 | -55.813999 | 2025-08-27 01:11:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff7caf6-4c7b-3eed-84f9-c0fe0c9c9c9b | -8.536 | -62.644402 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5417cac6-46c9-3686-9c30-6c34021f4f4a | -8.8915 | -60.7659 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00ccbdfc-a28b-3121-813c-9157c80f0623 | -6.7002 | -58.5452 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd735e3e-68db-3656-aa67-b63ee3ddab52 | -6.8213 | -58.9487 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3401b66a-189f-3a5e-b93f-e85fe5f937e1 | -9.191 | -59.449699 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d30edaee-cc64-328d-8e07-5094a73d671c | -9.5883 | -55.366901 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06c0520e-1478-33c3-b267-724ab92406de | -7.6271 | -61.024502 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5f2349f-5a9d-3ba0-b663-e85728a29a32 | -6.9194 | -52.858501 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36eb2ff9-f521-31f0-bdf2-fdf876d574a5 | -9.1536 | -59.561001 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc7d3558-e6af-3dd4-9b0e-4ad0304a6fb6 | -21.5902 | -47.4655 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0d031405-f027-3d4a-ba92-ed203e9df0d4 | -9.0781 | -49.564499 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9e315e6-4288-3b2f-b9ed-2f843143fde8 | -6.6255 | -53.319401 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 679dc4f9-758c-3207-b9c5-7d86feed9f76 | -6.5785 | -47.385899 | 2025-08-27 01:11:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b74ecf8-1321-3f4d-b2b5-ad97e9c6c3ad | -7.7484 | -61.064602 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49f95c13-448a-36cc-b057-fd6342150921 | -8.3494 | -62.917999 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a47222db-ffc4-3b93-aaa3-53a46ea7c067 | -8.9467 | -65.950897 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3485763-6322-388d-a93d-bd3014cb1ae4 | -7.2736 | -57.660301 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf38d38-51e8-308c-9733-7c899fb34deb | -6.3551 | -55.797501 | 2025-08-27 01:11:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d98d46-43dc-3d8c-8037-6d83bc9eb292 | -9.5867 | -55.360001 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbfdae9b-6ebd-35cc-95f9-95941ccdba09 | -9.6275 | -55.357899 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccb7bd9-ddbc-30dd-b726-b00c41c8bf50 | -21.107901 | -48.864201 | 2025-08-27 01:11:00 | METOP-C | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3db1e67c-9a31-32ad-bb99-9bcbc4c0b206 | -21.5861 | -47.490299 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 30a04c6b-1b3b-3b07-9811-2f92c7ae9447 | -10.4092 | -57.696201 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c37665fd-4989-3d69-be62-03e77077090a | -9.1634 | -59.5588 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b28841ae-a9c3-3a7d-95fb-f4f752675a85 | -6.8426 | -58.952301 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4d5b591-9b7e-38ed-b94f-e372daf17cfa | -9.2884 | -56.911598 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77c3129a-03b0-39bf-bb38-ba79b704016a | -9.4059 | -60.493198 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61531173-03c9-3935-9157-6d61f405ee6e | -9.4224 | -60.522099 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e67f694-b276-3442-8e52-9b9a489491a7 | -6.7019 | -58.552799 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0949ae5e-9ef9-360b-891c-e48abb03b5c7 | -3.7363 | -48.943001 | 2025-08-27 01:11:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
