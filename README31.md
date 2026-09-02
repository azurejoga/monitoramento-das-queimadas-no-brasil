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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a36622f4-802e-3e04-b407-d9729459c3ba | -1.59128 | -50.43997 | 2026-09-02 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af7c21f-fc07-3533-92e9-cf32caed6c27 | -2.16271 | -47.48398 | 2026-09-02 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a58f8f6-87d0-34ec-a295-ec0a53b3251b | -3.12442 | -61.23361 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae109525-b9d4-31b8-b316-b88505253ff4 | -5.24731 | -55.91302 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 391a3775-4ee9-32d5-8430-2bbf3fe4d404 | -5.25195 | -55.91016 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49879498-2381-33bd-a2f9-673d214f5b32 | -4.11446 | -51.02663 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd7ef779-cb91-39be-9f83-0084229e8855 | -7.233 | -42.77026 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e548387-8cbb-3b40-8630-c6943e92910e | -4.26773 | -55.15459 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5a8cf320-669e-3786-a414-e6b34cba19e1 | -4.12111 | -51.02769 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e43cdd41-d6ec-3bfd-8338-dcfb089ba50c | -4.36882 | -47.77764 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f1f7456b-80a1-31f7-9cd0-9df9c9da0a1c | -3.44808 | -47.27313 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37e30ca-b05b-3ffe-a34e-7aeb52ebd70e | -3.76171 | -59.41667 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7140d5e-f5bb-3829-a190-c600bdff010e | -4.49781 | -45.9081 | 2026-09-02 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5cd9b6ae-0077-3d1f-b7b6-5b3aafd757fc | -5.25606 | -55.88552 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af4c3dd-ee30-3374-adba-2d0b4d00547f | -3.79932 | -59.29185 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a3d172-f57f-3c58-87ac-da2febef6b68 | -4.35648 | -55.02862 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3923d577-7faa-388e-9e56-39163860121d | -3.79878 | -59.29503 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 266237ee-f500-33f0-8bfd-45609230a85d | -4.36525 | -47.77709 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4f51d0d1-affd-3867-a78f-d30c3918681d | -6.84274 | -41.68167 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84ded3d6-7c91-3eb4-8c7e-103770b9fa8c | -3.5751 | -58.74773 | 2026-09-02 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69aa87e-4120-3312-9a24-b8a3ac1e03f9 | -3.23877 | -47.25326 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 24e3f325-021d-3f46-92e5-6fe347b5daa8 | -2.82709 | -48.65546 | 2026-09-02 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e16e844-0bc5-367c-ba4f-cd643479306b | -3.0611 | -48.74359 | 2026-09-02 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4864ed0e-dab5-3de3-a1db-0ba81b51d48c | -3.85667 | -44.05716 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63c0f4b4-fcd9-386a-93aa-ddc75a001517 | -3.65372 | -58.91665 | 2026-09-02 04:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4df313-8438-3a42-aefc-13490d5cf79d | -1.39434 | -48.15281 | 2026-09-02 04:55:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37a97b58-3c01-3aea-bed3-125f6083453a | -1.01725 | -53.72844 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78c8c5db-504b-3388-a334-a2124919a49e | -4.27164 | -55.15526 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| defa32aa-ccad-3593-ae09-16d47db93468 | -6.61733 | -47.63995 | 2026-09-02 04:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c837afbb-f524-3186-acd3-b63f3746c7a7 | -6.14162 | -44.45686 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f051a0e-68e6-3739-b351-e641fe082c47 | -3.61618 | -60.56371 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed991028-624b-3dd8-a5ac-08bba0e35f5f | -2.33457 | -48.90427 | 2026-09-02 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28414515-4203-3cf5-b0b7-241620ec04d9 | -3.44785 | -47.27036 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1aad2f6-94e4-3734-89e7-3b9d2e20d061 | -4.69622 | -56.05377 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c662ed86-562f-3bb3-8939-a9fc2e5254ca | -4.80016 | -55.97574 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9353b4c4-ddbb-3f41-a87c-a35194531cb5 | -5.89596 | -52.10273 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425d53b9-7f8c-3cbb-9165-97eca4bca306 | -3.14515 | -60.64365 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 705fc46f-d84e-3d8a-ba06-d05f16c217bb | -4.4818 | -54.97202 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e58a38b5-3dd8-312b-8efd-23a5031232e4 | -1.09487 | -48.05811 | 2026-09-02 04:55:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abaea418-48fe-38ca-b331-4ce82ff071d0 | -1.96226 | -48.38186 | 2026-09-02 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 928235db-9fac-3feb-882d-8c5c3b9a6706 | -4.16579 | -47.83508 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0526b3-4b10-37ff-90aa-d97d80aa1487 | -7.23038 | -42.75095 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ab4002e-f401-3234-9a8b-6f19d53a3435 | -5.39839 | -45.62909 | 2026-09-02 04:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ca21ec43-a8c3-3e58-b5c4-5431c1427859 | -3.52666 | -50.52942 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d056cd7-e1c7-31a3-aaa5-3cc076d68bf0 | -3.83029 | -59.39536 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcdf9a33-7870-386f-88f7-e73500b38f5e | -3.62188 | -60.56468 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f0b978f-2e80-3adf-803a-12c309af75d2 | -7.23127 | -42.77163 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 939260fd-9175-3403-a0c3-ed44aadb7e35 | -4.96263 | -55.85096 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31d4be57-9095-3a79-9fe4-efd697134c9c | -3.12515 | -61.22923 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81dc21ec-8485-322d-9abc-2ada70e388ea | -6.8367 | -41.68388 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60e584bb-081c-3d2a-a8fb-ba39aad5ba81 | -1.46609 | -52.96583 | 2026-09-02 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10808025-8847-3ac3-84d0-94e0cd704019 | -2.021 | -52.11005 | 2026-09-02 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12f47fe6-21f7-3713-b056-dae678ad6fe3 | -4.97478 | -55.8531 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81d09a3e-ba66-3327-9765-c60aabaddd63 | -1.58741 | -50.44291 | 2026-09-02 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4964f57a-fc62-307f-b395-cd18a95cd54c | -6.42928 | -48.52978 | 2026-09-02 04:55:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 458da5c4-6fe1-3691-b568-1e26fc8cf3cd | -6.91139 | -45.71247 | 2026-09-02 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 674c58de-541e-395a-b371-ffc3155bf054 | -4.22132 | -56.08088 | 2026-09-02 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba6c64bf-0c53-3959-a685-fa306087f92f | -2.40044 | -48.17174 | 2026-09-02 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e72e6c6-984a-3ffc-9165-5dc34103da97 | -4.91358 | -48.99438 | 2026-09-02 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86303a4b-59e6-371d-a1e9-b99acdd8929b | -6.80737 | -46.20394 | 2026-09-02 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 091cfda7-d494-36e1-9ae4-3b192766ac69 | -1.01795 | -53.72397 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9fdbfb3-d9e6-35d2-bf08-2c07c31b583a | -6.58274 | -44.78425 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e31d69b-d434-3f7f-97e9-d011be9e1343 | -5.0257 | -43.60223 | 2026-09-02 04:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09bb83a5-b9de-3409-9d94-6e7c3c14b7ab | -4.36587 | -47.77303 | 2026-09-02 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e57d8643-d968-3c8e-8508-e743286c17e9 | -3.15094 | -60.64454 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50d60f99-7e31-3f39-b54c-e9e490cf27b3 | -4.96668 | -55.85167 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d65173c-c3d0-3fc2-b869-6df07fb050ae | -3.46466 | -59.65956 | 2026-09-02 04:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c43b1c7e-f757-3b18-bab9-34535f872285 | -3.65831 | -58.92051 | 2026-09-02 04:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 720dd74a-429c-3b7a-8f66-4352772a3827 | -7.23259 | -42.7733 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3a76204e-e74f-3a98-9b9a-e841f1cfcebc | -3.24004 | -47.24496 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b2c1460a-95bf-3dfc-a686-4de8eab3443b | -3.75215 | -59.31917 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924d4f15-e607-3c57-bc6c-34e451b38203 | -3.11771 | -61.23692 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4535f736-be0d-302d-b253-b59473d07f29 | -5.24907 | -55.90244 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec547ca2-97c1-33af-8d7c-aae0ba094eb5 | -5.25136 | -55.9137 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63fff7aa-441d-3813-bc4b-37d44128d322 | -3.84774 | -44.05577 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f042814-cd21-3103-aa46-30afe1622801 | -6.57387 | -44.78302 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58f27a8b-2b4f-3e8f-ba8e-c631cc34ab98 | -3.78116 | -51.35183 | 2026-09-02 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d67c0ad0-e05a-371d-b4f8-85794e927a72 | -3.36724 | -59.40324 | 2026-09-02 04:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 967cea09-2705-3b35-9a0d-12324af8c5f0 | -3.11342 | -61.23854 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9202881c-9a70-3031-b449-a1b74ab3679d | -5.80296 | -52.05119 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 234b28aa-423e-3358-87d8-8e21292787ca | -4.35261 | -55.02792 | 2026-09-02 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26547218-48a1-347e-a163-4e05fe1fd2b1 | -4.9661 | -55.85522 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 36ed5931-1d14-3b84-a40e-750ffaa735da | -4.54349 | -54.9157 | 2026-09-02 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7edded8d-7764-3401-84ea-63c1f93fedcc | -5.93515 | -50.2113 | 2026-09-02 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c12991f-1c24-3c48-a020-dc3bb82ae713 | -3.8522 | -44.05651 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8b25507-6822-33e5-a9ad-155ceb4b0ebd | -3.36138 | -59.40565 | 2026-09-02 04:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89ce1be5-5144-3588-aa16-617df29aa84b | -5.25547 | -55.88903 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42b8a8a-71a7-39a5-8abc-ba6aab399df1 | -6.30096 | -47.46764 | 2026-09-02 04:55:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5877f0fc-8bd1-3165-a84d-54df97aa86a9 | -3.55281 | -59.03576 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 602e8a9b-7a3e-3a45-8814-4bed680c5085 | -6.57328 | -44.78706 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c7e7a30-14bc-30ae-af02-4aa39a1ca0ed | -3.06052 | -48.74723 | 2026-09-02 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b400879-8584-3af2-bf8b-283f677b6be1 | -5.6416 | -43.55576 | 2026-09-02 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b95d7d64-29fa-3d9f-8980-cb82b1d79867 | -3.12018 | -61.23515 | 2026-09-02 04:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96210225-72d9-323c-b1b0-1666d2290817 | -2.5008 | -48.13308 | 2026-09-02 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48972ec4-47a7-30a2-8409-eec27379a3ff | -2.50425 | -48.13363 | 2026-09-02 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 831df4a9-6bfb-3f41-8d38-ce24bcde18e4 | -1.46967 | -52.96642 | 2026-09-02 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c4bd7b-0021-325f-aaad-4618e3e20c4c | -1.2591 | -55.73963 | 2026-09-02 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fc9bbb0-846a-327f-aa37-3a26e5809a05 | -4.12056 | -51.03116 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ca006b8-73e9-36dd-9a11-bb7ea43537a5 | -1.02136 | -53.72663 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1da1af-df3e-370d-8159-a3bb8cc767dd | -1.51405 | -54.96048 | 2026-09-02 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
