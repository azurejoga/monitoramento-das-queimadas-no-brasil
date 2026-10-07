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

## Dados Diários - Página 224

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c975cf-d9ea-31a7-bb1f-6113ab926117 | -3.98414 | -56.21984 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 8e8d7362-0e6c-3e44-af3e-4fecdb6a82d0 | -3.22002 | -53.88725 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a0f83314-abbd-35d5-a0de-b1e3dd39f103 | -3.35799 | -50.46964 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5097a78-f7f6-3dde-a4fa-02fc4fc816c7 | -3.65008 | -55.46198 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a5ea6cac-ac5f-382a-ba7c-a555d384dae3 | -2.39111 | -56.13076 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 616bf3c4-b29a-38d9-9c73-e238a30046bb | -2.77448 | -54.1127 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e2a3f7d0-ef5f-3243-9f54-cf155a9f039b | 3.21719 | -51.29243 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fc1e248-d538-3997-b725-6a0c55a1230e | -3.84909 | -55.98203 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| d478e342-62e3-3556-b82c-94b85f15c183 | -2.425 | -49.75716 | 2026-10-07 16:39:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c0233ed2-c75a-30b6-9028-855aed1f9c2a | -3.05482 | -53.91864 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4ce22864-aa03-36c4-a72f-86f616fdd8a1 | -1.52395 | -54.80509 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 97e99774-edba-3ff5-9fca-c577a35493bb | -3.84837 | -55.97712 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 095fa5e2-8658-3a45-94f7-4980c3c7f89e | -3.9834 | -56.21484 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 97f95227-a91f-3734-95c7-1f7642755145 | -2.94924 | -57.19818 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4f2b45d1-1a9b-3541-b4bd-fc6c2f04a7ed | -3.2096 | -53.87159 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c35bffb4-f9e9-3d4e-a7bd-65ecb78162af | -3.23499 | -57.87828 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 05ccec91-ce2b-3d5a-aa64-d58d8199ab43 | -1.61004 | -55.55691 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 049c868c-6880-3b5d-b264-b503cf5a0d63 | -3.28207 | -54.05073 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 800e08f5-714d-3c6f-a2e9-bd5d87400cee | -1.80683 | -57.11511 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fe2a6996-07d0-3630-8d1d-2c89c7ee377d | -3.09323 | -54.29551 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 900aa31c-f3f6-35de-847d-bcd6d001c100 | -3.13792 | -51.02647 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 39639d42-cb21-3391-9ed7-c0c54ac35bc4 | 3.37095 | -51.34518 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 38a7a707-5b95-3305-a776-abd0284d9d1b | -3.10923 | -54.97551 | 2026-10-07 16:39:00 | NPP-375 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62d7cded-c213-3591-8194-c4a5382e3d56 | -1.16702 | -47.5694 | 2026-10-07 16:39:00 | NPP-375 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 705fbe3b-2d53-316e-80cd-bcda33fc6687 | -2.76208 | -57.67348 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 6d1b539c-683e-3bb2-92b3-e266baaeb8ad | 1.7061 | -55.61691 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| af586454-c8e5-3d82-a89b-330cbddaaa95 | 1.76192 | -55.58826 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 706c5470-a770-32f8-9d8a-d8892887ae3a | -1.42381 | -55.42332 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4265d413-bf3c-3e39-b964-8693d7c18d59 | -4.76632 | -55.72314 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| add9074e-a9c5-3d72-a7db-e214b0e7c76d | -3.53891 | -50.09309 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d2c59da4-ba5f-3438-a1c3-b583e8600601 | -1.55732 | -55.70966 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c046294-e20d-3d36-9271-798cc728907c | -3.54874 | -54.49831 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b202ddfd-93da-3944-bf25-95cb0506651c | -2.44877 | -56.54919 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c8c8837d-9fe5-32e2-b990-e31579ba928b | -3.54402 | -54.64141 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a857c66d-3c2c-3059-847c-8c82bb6b2468 | -2.69872 | -56.56455 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfd18619-8b6c-38f7-a4dc-9d98f9669cbc | -3.63324 | -55.28028 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 33b5afc9-c17f-3b5d-8b18-2392adb237d9 | -3.61497 | -55.27904 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c0a57590-fdf6-37d2-8027-4776c00e1f5f | -4.57151 | -55.99631 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 67dfa639-2380-3dd0-ab46-0a694faae421 | -3.06358 | -54.20639 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a653f8fc-fdcf-345e-be80-8802bb852323 | -3.32347 | -50.17847 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5c912445-d894-3ab2-a3fd-02a52a8f202c | -3.22319 | -54.29904 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a650834b-ae1d-3443-954a-4b3a956dc993 | -3.27816 | -54.06186 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 412d77f2-9082-379d-a250-9801d72a6faf | 1.53464 | -56.02093 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4e32e8d-4b1b-3753-b18d-540ebdafc6af | -3.61558 | -55.28316 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ee7c5822-d85d-3d48-aca2-005f8cad4b58 | -3.07069 | -54.25573 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1ebf0450-e642-389e-83ff-183dff4801a4 | -1.80507 | -57.103 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 0cc9cd72-a4dd-3008-842e-64c58f7c9b81 | -4.0019 | -56.25309 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2164766c-3a51-3b50-b7ab-d1372b88942b | -1.48108 | -54.49136 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2b48fcdc-9c64-34c1-a0d5-5e4806395e49 | -1.75117 | -55.12062 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0c5fb342-fce8-3856-98d5-cf4d8cf3b3fa | -1.75708 | -56.19128 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8e66731c-4ab1-302d-9ee0-518b507614d9 | -3.44431 | -50.61895 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 78af9e84-8525-3e0c-ae9c-921b491fb089 | -3.04405 | -54.26513 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2d36c722-1303-3acf-ab18-c5bdf629d0df | -3.64029 | -54.51143 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dba158de-b4e5-37f3-8dc2-c16c1d4ff4f1 | -2.96123 | -44.31644 | 2026-10-07 16:39:00 | NPP-375 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e52f58e2-3bfd-3cfd-bdcd-aefe3145e585 | -3.2722 | -54.02076 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 93bea884-8774-3940-8776-c4263e68c257 | -3.64891 | -55.45367 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ce4f8f41-6ae7-36ab-ab2a-85294ade8033 | -3.26877 | -54.03519 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e8c25a5f-fdbe-38f2-a836-b1b4cc860ac7 | -1.83688 | -54.94138 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4958b395-2519-3f4a-bc7b-959aef63cdbd | -3.27766 | -54.0584 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 16a20aba-9f05-3e5e-80bc-d0a042a04b49 | -0.89091 | -46.8606 | 2026-10-07 16:39:00 | NPP-375 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 88392f45-546b-3839-9c89-afbc541e3411 | -3.78773 | -50.87757 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 734e3f4e-5665-3b2c-85ee-5c3e3ddd331f | 3.37151 | -51.34167 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08836d65-953b-3398-88fc-252e13ee7014 | -2.65049 | -56.82612 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 825e3490-f24c-3b17-8dff-f0672f22b11d | -3.30089 | -49.12242 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ced9cb9d-d835-3eac-a120-e646590c3428 | -1.0933 | -48.05526 | 2026-10-07 16:39:00 | NPP-375 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ade4845a-8102-3dd8-902e-f5c34a5c9831 | -3.40988 | -58.02295 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0066ab15-a77a-311a-a649-f589d8e84770 | -3.22811 | -53.88567 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16ce97b6-302d-30d3-b28d-a490d4c8291b | -3.05196 | -53.16929 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5e776fcb-e728-32bb-a28b-0f58d5eded9d | -3.29142 | -54.03902 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f8a90241-2cce-3ccd-81bc-9a140de6d3a9 | -3.20731 | -44.37966 | 2026-10-07 16:39:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4adfe815-879f-3f2f-b54a-d042399f12cf | 1.75579 | -55.59107 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7c706b34-7937-3b18-932a-1f704a7275fe | -3.08058 | -54.24684 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 785ee4a2-4dfc-35ea-aba3-9a92f6e17930 | -3.54819 | -54.65545 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2ac0abb3-dd3e-3c5b-a765-784907444025 | -3.73269 | -51.20573 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6846a9a1-9e25-3a1b-b87d-264e6ad71ff7 | -3.97093 | -55.83759 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 734cec2c-aec5-343b-81de-e49e29a33cfb | -2.51017 | -56.25322 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 59a64203-71fb-3e61-9e77-b0d0980cf4c2 | -3.28951 | -54.06381 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 058b8e1d-ad2b-3d9b-8690-93135d578d7c | -3.5429 | -54.63393 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25fffae7-0730-3f69-a5b4-b278a91825a4 | -4.57434 | -55.99417 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1367bdda-bd9d-3b8e-a1d3-98f702c40cea | -2.24594 | -55.05814 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25715635-f725-39c9-9f4c-7b78703b7b76 | -3.07971 | -54.27947 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0bf3f8e2-2802-3aa8-a9d8-6666aa33bf37 | -3.45025 | -51.08445 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 27fc2263-cb59-3fcd-845b-5cfd1530b9e8 | -3.00593 | -54.76397 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89eadc39-1c89-36ca-9eb6-f227445cd1b8 | -1.99708 | -54.10008 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cea56a04-8632-3b0c-81c4-6c3474ebd90c | -2.92313 | -58.37876 | 2026-10-07 16:39:00 | NPP-375 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9cb8697-9f59-3491-b5f0-00b15a73a917 | -3.48307 | -54.61919 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1babf4f3-4978-3846-bc6b-a363e7a90d03 | -3.05452 | -57.41078 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f2fb3de5-b0e9-3af0-b940-47d1cc5719f2 | -1.87716 | -53.97371 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b441f690-fe47-39ed-9f41-429d0450b32e | -3.54626 | -54.6564 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0222ebbd-3fd2-3e81-a465-cb03a055abb0 | -3.01771 | -54.05268 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 253deb64-e619-3bbb-a4a0-1a0d7527dbe5 | -3.28842 | -54.01855 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cbef3bd5-5059-38a0-bdfd-330d237dafa3 | -3.41081 | -58.0295 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a35b4c7e-fbe9-3701-b730-7cbcad4b59a5 | -3.10163 | -54.27623 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| dbe6865f-95b0-310a-ac1f-19bfdbc573ca | -3.10173 | -53.76618 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 835a1aa3-f69f-39b9-b56a-84dbe9f563c5 | -1.33067 | -55.43204 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c121d116-9896-300c-ac68-8ec2cb94af91 | -2.80083 | -48.89501 | 2026-10-07 16:39:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f7c4dd98-86b0-37ee-b041-d06a342e54d4 | -2.78944 | -54.0654 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a4381454-e83b-3c70-ac07-888eda268b16 | -1.28188 | -55.85423 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| fc904a8d-d0e6-3f81-b847-21c6148102c4 | -3.00938 | -54.7484 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6b634426-29dd-3bbf-a326-24a4cf9ab56c | 2.42797 | -51.74261 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README225.md)
