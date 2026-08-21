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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad0e68a-68bb-3f9b-b92d-2c1744b7e69a | -6.11922 | -59.91011 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e31b0c80-c424-3168-85f7-edee277a9eae | -6.89203 | -56.43088 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f62877-20c3-3c1b-8963-f04a61da010f | -3.2686 | -49.52423 | 2026-08-21 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fea0eca4-3776-3a78-ae36-e62d2bec486c | -3.38367 | -59.52718 | 2026-08-21 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 429b8d48-dc38-3f5a-803a-ade49942f857 | -12.51197 | -54.76616 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6633ca9-d7f9-351f-92d2-20368f66b970 | -8.45992 | -46.95354 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bab4b323-6dfd-34dc-ac90-e38a15079b38 | -9.2467 | -59.80999 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ecb20d-e8c0-33bd-aba8-6003b7b83d42 | -4.95214 | -56.26767 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f99b621a-3d01-3075-82dc-5f904f9bc437 | -7.44688 | -60.00336 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09199d1d-57bf-332a-82d1-208b270b7f93 | -14.1021 | -58.81575 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c24abeca-7705-3aff-9876-d73d22f9cd64 | -6.12974 | -59.91182 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3e8685f-eb20-3192-ae84-7154907cfa9b | -8.16736 | -54.9957 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c4bd3ce-ca51-3320-818e-3537424be913 | -6.87111 | -59.43667 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57757ff8-f3fa-3449-b699-4827738c40b1 | -8.40595 | -62.69601 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cab256d-f882-399c-9734-9cc1ae4427d3 | -6.00341 | -57.83858 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13feb6d0-74bc-3a73-b376-ae96e1492e10 | -14.30786 | -51.89776 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0d73dff7-ae54-39cf-85c8-7c19807a1add | -6.57842 | -58.95873 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d3a370-cf34-3e2a-9b40-021cc19d9cea | -6.0023 | -57.8669 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 456fd212-d06d-3cc9-9a7a-5247e3e217e5 | -9.46346 | -51.64227 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45df6753-fe20-3b89-8740-a2739eb63fc2 | -6.13738 | -59.90907 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d93ba24f-fe93-3eab-9d03-bb56cbc47910 | -6.94158 | -52.78159 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7e923df-97d8-3b09-b579-22c9609963fe | -6.00895 | -57.80383 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79041e18-df7b-3ac7-9c6c-64c84d99d1e2 | -6.42639 | -52.75808 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8035c629-ef41-37ef-9f30-3dc70f0d5f9e | -6.87394 | -43.73808 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9bff1da-ebd6-39b6-bc14-71af130600bb | -6.66382 | -56.35151 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9872a9aa-1174-3260-87bd-e1671ca4d022 | -14.45876 | -45.62773 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e652948-9e68-3e02-b24d-62ac73cc0991 | -8.18338 | -54.98653 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ac9771e-b255-310e-97ea-c7a2e4ba9766 | -4.45956 | -54.83876 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 407c491d-887a-36c6-baf0-fd4213affa3c | -4.11449 | -48.93476 | 2026-08-21 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 567426aa-eb1c-34b5-9a78-ca622ddf8ce0 | -6.83025 | -59.40722 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 430c7dda-2216-3874-bbbb-0547589e32a7 | -6.85622 | -59.44185 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2a2e8ed-dd0f-3e44-bc83-c1bba3572281 | -6.24249 | -55.42447 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4f9810e-6157-3d2e-be43-534c0dbf8a68 | -4.45361 | -55.38957 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52b0379-64ca-3291-8ab5-9facb59ec403 | -4.04527 | -50.29966 | 2026-08-21 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 673810f3-57ad-3e56-b154-49f99ddb5079 | -9.15858 | -59.55529 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 406af864-4d11-3902-ad25-483b5ca90075 | -6.88306 | -56.42216 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d4aab9e-4ee6-3907-a069-d19fb27a05a9 | -14.34218 | -51.89223 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 264844b4-548e-3b22-801f-71df3dbf8f91 | -6.84151 | -59.42426 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e80c979c-d939-30db-b5ab-5e7844a594b4 | -14.45238 | -45.62011 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 157272bb-cf3b-372f-9912-fff803984c1a | -6.89828 | -55.22015 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00a81958-e5cb-3211-9901-9e36633a9795 | -6.66101 | -56.3474 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4adb535d-044b-34f0-902d-30c391d34a0f | -6.24711 | -55.41748 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c13cb9e-8b48-35e8-b168-964710600b0d | -9.2229 | -59.78304 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 113fb00d-5faa-3a00-8e06-f6bd3092280c | -4.88964 | -56.28264 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f83d0aa-549c-3c99-8815-89c5b8eeb8ba | -10.66136 | -49.02256 | 2026-08-21 05:23:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e005370c-5b57-3c56-a20d-d61f7a36f801 | -8.52031 | -55.33495 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4598e3ce-ed92-3a00-a63c-26c308ff885a | -8.56742 | -54.65941 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0372cf1-974e-3d9a-ba46-abf25104c53a | -6.43213 | -54.94832 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9aa86b2-7251-3bdc-b836-3eb2fd274cf1 | -8.28565 | -62.89486 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 450bd181-f98e-35c9-baf3-f2be36f7f2cc | -6.88214 | -59.41189 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f387e3-2877-306a-920c-dcee37b3a9fc | -6.89224 | -59.43632 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fdceff7-83f3-3afc-8440-3679a83b2ad2 | -8.59106 | -54.75031 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f227797-2f65-3aaf-b2b9-ef1012439f3f | -4.95937 | -56.26523 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be7940c9-b69f-317c-b8ff-c8629dd01897 | -6.23508 | -55.40409 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3985f584-0264-3bd6-93de-54a131ffb297 | -6.57445 | -58.96179 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce757c3-94d8-3b9c-b9ce-7484fea147cb | -13.43794 | -51.79825 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2afa3d71-c8b2-3de9-9e43-8db54ddb8f41 | -8.55187 | -54.81333 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| facff461-d94f-30b4-9b0d-9deb9f18e872 | -4.95992 | -56.26171 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d7a6727-dbae-3344-bd10-1504ecf691c3 | -9.05573 | -60.43691 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d374b31-cc9a-31c4-9a80-0709f0f4f82e | -6.88702 | -59.44687 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff96f4c3-4723-3e2a-80e2-767a18ab769d | -3.93144 | -59.33356 | 2026-08-21 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f8af4b1-06e6-3965-b032-3955f688862c | -12.50816 | -54.76554 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 677c2b09-be6c-3751-a251-42a7e2faee74 | -7.77974 | -61.16647 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a045d103-6d92-3bf1-bc79-fb0f764f8656 | -6.23624 | -55.39664 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdec5817-9cee-37af-9c98-d64931e0a935 | -8.5817 | -54.78769 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fd141ad-8d90-30f3-a110-df9844b0361c | -8.11386 | -50.04265 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0766960d-b4ab-3900-8e66-1be871f0060d | -14.32541 | -51.91085 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15a741d4-6190-3a67-8c90-130ce37a23e5 | -9.17309 | -59.70311 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cef4bd08-c29d-304e-b589-b4af44e24c97 | -6.94692 | -56.38833 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1f9d9e3-dc55-31d6-bef1-3199b2b63d08 | -13.94977 | -53.86317 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac601c87-d202-3c66-9d7c-5849a81a9da1 | -6.43393 | -56.18776 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e566b9a6-8fb8-30e7-8a14-b3d09497b3d0 | -13.92974 | -53.85611 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c4a1395c-87da-3989-b106-fd8cc0214bae | -6.36718 | -58.33718 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9830bda-7043-3c67-9494-f941b0fbd0ea | -4.93671 | -55.78521 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75fc4dae-b9f4-3e22-bb82-3bb0f7a28604 | -5.81326 | -55.71518 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4fc81b0-9d21-334d-b8ba-e7ab5c280430 | -3.55393 | -59.03249 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7111ba18-f6e0-3926-a07a-1a267d183253 | -4.95548 | -56.2682 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8d24729-51b7-3b04-aba1-58de823fb0ec | -14.31793 | -51.89407 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| aaca1355-dfc5-3a75-b350-32e01c725efe | -6.23566 | -55.40036 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 318c8011-328b-3379-a814-4186aa738578 | -14.3085 | -51.89266 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8139aa55-755c-36e2-be1d-dc73ce382013 | -6.701 | -58.93363 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15887732-65ac-36df-854e-22fe25f6ea3e | -6.68971 | -58.93918 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b152731-d252-3d44-a6b7-92bbd7c54e3a | -5.81667 | -55.71571 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6646e128-1544-326e-b428-15f7650cda90 | -9.50589 | -51.67936 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbaf77fd-ea78-3958-8f21-0c94e750b77c | -14.07986 | -58.87061 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa13c6c7-d810-303a-8263-6c24aa0ae842 | -14.20973 | -52.88013 | 2026-08-21 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71ac9a8c-abc3-3def-8791-baaaddd7608c | -6.86649 | -59.44353 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b7e6da8-7833-35c5-be6c-3834adab7479 | -3.26788 | -49.52912 | 2026-08-21 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3df5de88-c2d0-32cb-b60b-ca854dcb6780 | -14.07598 | -58.87362 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1d856e9-a094-3f16-9506-3410fef01643 | -7.37194 | -59.95274 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01dca903-4f44-34bc-ae9d-7fba653f1ba3 | -6.64488 | -56.40701 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d01aea7-7f34-33ed-a65d-dec60ffd6282 | -13.93025 | -53.85233 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e372042d-000c-3137-a9c8-2dd02d4d4eaf | -7.77903 | -61.17078 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b2b1716-822b-3801-abf8-d6d397b856e9 | -6.84212 | -59.42056 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f33229a2-ae6f-3bee-a5d1-bf13137e247a | -8.71653 | -49.61932 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0587c70b-3c14-3a91-9cc8-ef1e4725132c | -6.83246 | -59.4152 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cd9076f-11ff-3437-8321-3e169698d8a9 | -15.4932 | -53.89864 | 2026-08-21 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2bd14c2-76c7-3dd5-84b8-31c6ef4e36f9 | -13.40963 | -54.36199 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ebde5e2-3211-3f60-bd15-c8eea643bced | -9.44802 | -51.62206 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acde1c83-bdcc-304a-a35c-ed386c4d30a7 | -6.54772 | -56.26078 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README67.md)
