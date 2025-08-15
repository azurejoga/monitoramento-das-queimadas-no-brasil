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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 142e946f-3f2f-36df-89b3-cc42603f314a | -11.7414 | -64.883797 | 2025-08-15 01:10:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cfb653d-33fe-3a46-bd2c-2d4b765c5207 | -9.2221 | -59.659599 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20014ca5-e5da-325f-b064-f125dda81041 | -9.5046 | -60.528198 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7818f8e4-ac96-3c24-a120-e396a73feff3 | -5.4517 | -60.118301 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b83596a-2ac7-3e67-9d83-27d04e087825 | -7.6229 | -63.5159 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30a35b8b-eb4f-3528-ae28-38a3a429d76e | -7.0893 | -59.223701 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc497d2c-54d9-352e-ae8d-16d65436dd4a | -10.8653 | -61.989101 | 2025-08-15 01:10:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b190a67d-7aea-30dd-99bf-56797b63b37e | -5.4457 | -60.1371 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04d4b747-55e4-328d-9617-7f0049b3aca9 | -6.09 | -59.936699 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5eded3-bb88-3037-8120-0ff371a410f8 | -9.1848 | -59.6768 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e40e9e71-5dbf-3fac-9971-c40e777ea752 | -13.0659 | -57.1334 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfbbbd17-a559-3f6e-ba25-0f310aa2fa86 | -7.6115 | -63.5112 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f204541-5508-3f90-8f39-165420d3fc4b | -8.9064 | -60.572498 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbcb37bf-35b0-33e0-b994-77683efa4fe4 | -6.7067 | -58.820202 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f96cc07-27e2-32a7-bfaa-c0224c8a782a | -6.4832 | -62.931099 | 2025-08-15 01:10:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d25bf05f-4ac2-31ac-8ef3-7ecc6ea83142 | -6.9016 | -59.125599 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47cc933b-d696-32d1-8440-bafe60ae8a77 | -10.0487 | -59.354099 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9e8ae56-9885-3d13-8838-c8a97ea9a559 | -11.4052 | -58.534302 | 2025-08-15 01:10:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dddd962d-9cec-3fe2-a3a9-813c4c8d9e9d | -7.9559 | -61.740398 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1314f8ac-578f-3c53-ad6f-a22f3cb45917 | -9.1811 | -59.660702 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc826a8-b972-3ca6-b1b8-0e5963654a22 | -7.6131 | -63.518101 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4216e15a-64cc-3f2e-a3d3-5bbc1b803f8d | -7.0795 | -59.226002 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a33895c3-9c11-3c97-92f2-d2c06bdea80a | -7.3175 | -60.6124 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7768ae-b919-3b89-a623-b6e4757b1d2c | -8.117 | -61.178902 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6c9b755-3078-3788-bcb4-4f2d16e749f4 | -7.2844 | -64.683601 | 2025-08-15 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adda69c6-6f43-3efd-ad06-7727767aafad | -6.6556 | -58.822102 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71cdb313-807f-326f-9634-ab9598dc012c | -7.5308 | -61.320099 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 399e87a1-3e68-3ae3-99b9-1c53ff74fcf8 | -7.0754 | -59.208199 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 158b3d59-b3b7-367e-9b40-9ee16a08a944 | -6.8785 | -59.825298 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5f994a-bba9-3df2-a6ef-03a609609d1e | -6.6729 | -58.808102 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5f0462-ccb3-342f-a88e-2ca403ee902d | -8.5615 | -63.852402 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f32ba398-7a3b-3515-aaf8-8b3f2600306f | -7.9607 | -61.761501 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdb1a3a6-0d6a-33ec-880a-59621deb4979 | -16.2967 | -52.917702 | 2025-08-15 01:10:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5348bb7-82f2-3d8f-8d07-ecc8e3d9c565 | -7.0775 | -59.217098 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8e2d3a7-7cc1-3e26-863d-9c4bd92e60f0 | -8.5724 | -63.902199 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be729927-0c4c-3fa2-a368-9ede27ada75d | -7.0559 | -59.2127 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbe3cb8f-9526-362c-8cbd-243907607b41 | -6.9497 | -59.999802 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0a19a14-159f-3508-b4ac-1bb43d9fa220 | -15.6594 | -49.780499 | 2025-08-15 01:10:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7549d5-1e73-3d74-966d-001fa2db351d | -5.4555 | -60.134899 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e238ffd-c5a4-3f92-b73d-d68846973280 | -9.1536 | -59.675598 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea3fa0d-a254-3eb5-b9de-947584a066e2 | -9.9159 | -60.432899 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8295c6ff-275f-3dd5-87db-9f7ede5d99dd | -9.7959 | -61.492001 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7332f6e5-abe2-32ce-85b6-28179268793f | -9.3935 | -60.5383 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68c32797-36ca-38ed-af23-858c14cd04ff | -6.0763 | -59.922199 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc43507-ba7c-3fff-8228-be601bbfa5fb | -9.1867 | -59.684799 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f34eed08-48a7-3726-804f-36f584d1471c | -6.9409 | -59.516399 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 521a2338-e143-3714-9789-264736d5b9ba | -7.0733 | -59.199299 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c69ef181-cdf0-39df-898f-782cc65bf98c | -8.5611 | -63.897202 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9568994d-1142-3f36-8942-22ac3a1c650f | -9.5097 | -60.550499 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2e05fa6-ceec-3f9f-a939-ec8d841c5b10 | -5.7378 | -59.8843 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfa1b26f-1ae1-36e5-af71-90e6706aa323 | -6.9311 | -59.5187 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 324b6315-ec9f-3011-b9fb-9307ab483bbd | -7.6213 | -63.508999 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 771ab560-0871-300c-8c1a-1807f1f113a2 | -6.9484 | -60.128201 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31e624a6-928f-3f36-89a4-9bf86c3265b2 | -7.095 | -59.203602 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6379c9d2-2b84-32d2-8a80-8183d215a5fe | -9.926 | -60.477501 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a021ebe-be30-30d1-a043-eea25664d19d | -9.5461 | -63.560299 | 2025-08-15 01:10:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd98ca1d-e2c2-3222-bc55-6a4ff381fad7 | -9.3952 | -60.545799 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f031cf3b-e3a8-3c07-bc00-0993efb53bb3 | -8.6701 | -62.441299 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a9541dea-4df2-382a-a4ea-f43679b6d6d5 | -7.1546 | -59.6376 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9ccd1d-316d-349a-9156-5ea1535ad183 | -9.6363 | -63.082802 | 2025-08-15 01:10:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb81fe9-7895-3e80-b1fa-65811be07c52 | -7.9591 | -61.754501 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58b17e46-9e35-32b2-9480-56f538e77a33 | -15.6446 | -49.727001 | 2025-08-15 01:10:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9987f7-5607-3f90-9d97-5817bf108902 | -9.3495 | -62.578701 | 2025-08-15 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2cca065e-8bb3-3d07-b67b-01dbc54cffa8 | -15.6425 | -49.756699 | 2025-08-15 01:10:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aaa2aea8-96b6-385d-b592-9415a8a598d7 | -7.9445 | -61.7356 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdca0060-2527-3d38-831d-620fb6fc3dde | -7.5308 | -61.365601 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 237047f1-0cd7-37f7-978b-58dc121ef1cb | -6.9351 | -59.5359 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aadd78c7-8d57-31af-95c9-fe47ac8e702e | -7.436 | -60.007198 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2a7234a-ba67-3ac7-beaa-d9edd38e75be | -9.2142 | -59.669899 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9514677-bedf-318a-89a1-10e2f3935316 | -5.7358 | -59.875801 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51dbd043-94f4-3e5e-ae42-4c6e4ff2330c | -7.5878 | -63.450901 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19ff132e-851c-3b99-afc6-5909500587b9 | -9.2049 | -59.629601 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1238764-cda2-39ba-a683-09d218cf6d7d | -7.8118 | -61.332001 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc87d3a-e3ad-37ed-b38c-df1b15bc3a42 | -6.9503 | -60.136299 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10bb245c-0416-3ab0-9329-9f89e3c32a47 | -7.8804 | -61.8167 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 475e3ef9-df08-3c99-bbdd-54e2e0ff7165 | -6.0742 | -59.957901 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04bedf02-e7c9-3a45-8de5-38daaf72a6a4 | -9.1988 | -59.647999 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f58d0a5d-a869-3f0c-a5a7-a210ae806191 | -13.1267 | -57.128601 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6878e751-6191-385e-a014-102217a94aa0 | -7.5603 | -61.4044 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1259a7bf-9d0c-31a9-bb36-f62d755bd58a | -9.1596 | -59.6572 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45b8ca86-b64a-3d24-be70-63cecc086048 | -10.3644 | -64.439697 | 2025-08-15 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77b8a45d-f6da-3cc6-b079-77e3e854005f | -6.6511 | -58.8032 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7c163d5-b4d0-3d32-bc11-67ff626e3ef3 | -7.0873 | -59.214802 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af0fbd25-039f-3a9f-b603-9a4e3ae6bf30 | -7.5341 | -61.334599 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63a60903-faa3-30f6-979f-91f86006ff99 | -7.1193 | -59.618999 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a208b89c-e4da-3daa-b140-5673d7f3ea6c | -7.9543 | -61.733398 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05d94106-a3b8-36b6-9da4-722bda83050c | -6.7262 | -58.815601 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27ae4324-50a9-300f-962c-e2aac3ba8786 | -13.117 | -57.131001 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e15113d1-b2a9-3d78-b41b-2284710b0250 | -6.6631 | -58.810398 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd332dff-fa3e-3d46-89a7-315c6878e57e | -9.0828 | -60.7579 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f03b3d89-1c1a-3011-807e-b5b5947d9107 | -9.5029 | -60.520802 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eaa32155-2e0a-370b-8bb7-554ee7af9095 | -7.3406 | -60.6231 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52f78fbe-785a-3b33-beae-046ab7d46389 | -6.4931 | -62.928902 | 2025-08-15 01:10:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85901803-6e30-348d-86eb-01bc10a28619 | -9.9061 | -60.4352 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e45746f-e350-3094-a04a-b4da90625dbf | -6.6871 | -58.824799 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a438a3c-de66-37e6-834b-a9ff20b364bf | -6.9253 | -59.139198 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3df29700-2dbf-3d63-a65a-b9d107b8437d | -11.3482 | -55.425301 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba9bff9-0320-3d92-9b65-783cf5e561d0 | -6.9041 | -59.624199 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5629e59-d791-39b6-8610-01ef23dc4a17 | -7.9493 | -61.756699 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2529b02-baed-3223-a94c-8cd966248cb6 | -8.1056 | -61.173801 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
