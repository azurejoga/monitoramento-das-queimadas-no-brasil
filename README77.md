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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14ea9abf-0187-3d2c-9999-21f8f3bc8fd5 | -8.01371 | -70.06929 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a51a48b-1b34-36b7-997b-72e6f32cd751 | -8.91167 | -66.95586 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eebda29-9116-311c-8cfe-4032e799cc58 | -9.99438 | -67.56593 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b678c40-310c-356b-b8ff-7bc99f9cf1e9 | -4.29032 | -59.95373 | 2026-08-31 05:55:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70f2e425-5db7-3e84-8af7-a1f144796f73 | -3.16599 | -60.13335 | 2026-08-31 05:55:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40335dc7-22a7-305b-b4d6-425066373261 | -9.84727 | -64.98656 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0599747a-0c5c-3e4b-a1b6-cf2587d42103 | -9.88673 | -60.278 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0adaa1a2-76c6-3a5d-87d7-cb124fee0f54 | -3.79499 | -59.34602 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db412614-944a-316e-94b8-33f1565dc1e2 | -8.55706 | -70.05077 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36c724ec-69f6-3241-93f3-0789e9baa90d | -9.13313 | -68.17892 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18b00e81-0b68-30d6-b0d3-586411a9576e | -8.93321 | -67.36059 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e7184bf-0978-348a-a5fa-15c2837b14ef | -7.44258 | -73.0723 | 2026-08-31 05:55:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb3458eb-35eb-3c82-87bf-a69a9c623e09 | -9.01814 | -65.39697 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 153c7d4a-387a-3c35-838b-5b601cc01c92 | -8.9424 | -62.37339 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1d549cf-7763-3521-b4f5-42bfdf82a796 | -8.86597 | -67.46411 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9964bf79-3bd0-3533-b1e1-7f649ee8cdef | -9.79249 | -60.17867 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8369ad93-02d1-3a70-9475-91151e955055 | -11.49239 | -60.59073 | 2026-08-31 05:55:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efa2eef1-d1a7-3b45-b8a5-7e0796ae7e52 | -4.96435 | -55.84842 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f23aa80b-b313-3efe-8fc6-5003629e31e1 | -9.85857 | -64.98412 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cebd433e-bbc5-34d6-8c98-1afc7af6c4ba | -9.86067 | -64.98739 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33b7ecce-faac-3dff-bd83-293ab8fab542 | -9.04341 | -65.43121 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b640d24-9377-3dce-a86b-8f6645bab492 | -8.09376 | -69.90958 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddf9894-cc7a-38f9-ab51-d036ec58a7a6 | -8.01436 | -70.06535 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c4fcfc-d5ed-3f6c-8669-cc34d2fc80e7 | -10.10601 | -68.40492 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92967b11-90c3-3915-a9e1-46f49e05cb22 | -9.88691 | -60.27436 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25b1779b-6ef8-3769-a85c-5cb02b215dfa | -9.93507 | -60.52693 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2030b713-893a-3392-b433-395ad1c67007 | -8.25723 | -62.75408 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f0b1a8b-41bc-30b9-94cd-261857540325 | -10.18657 | -69.33711 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f598576-68c1-3c3b-ad51-a5c6bdfbd2d1 | -3.62781 | -60.5618 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ae870e8-38b8-38d0-9f79-dc584d6b3fb6 | -4.8453 | -55.83393 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e69897b1-8626-344b-8325-56bf3bef7806 | -8.96953 | -62.38859 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f1dbe6-f36d-3103-9f71-a37d79b700d9 | -8.79255 | -62.49387 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ffd5c5-679b-3883-a3c7-aae10c8e0275 | -7.72403 | -70.08974 | 2026-08-31 05:55:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d2427ed-6285-3c54-a976-20a168ca632a | -8.52281 | -67.18475 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbd9a716-eb1a-36c1-b4bc-3aec82f64ab4 | -11.47705 | -58.51116 | 2026-08-31 05:55:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56613c8a-8675-347b-af1b-00b891420857 | -9.05381 | -65.40919 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9d7149-9846-3314-b37f-aa89f1e98db8 | -8.48541 | -70.24187 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 716d3e50-6237-301e-8cb8-f251ec571ea2 | -9.88978 | -64.98766 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc080033-cdd0-366d-bb11-01910b1a6b81 | -8.01658 | -70.07383 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa67c81d-5610-349b-bf01-61295e69138d | -9.79732 | -60.1793 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42094300-5157-35e4-be54-026a0f863d06 | -9.05612 | -65.41743 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3d2561-e35e-3120-aac0-c45330b0f72b | -9.02855 | -65.39856 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 498c6177-2698-3d2e-bdc6-fbb999d5d781 | -15.9149 | -56.22593 | 2026-08-31 05:55:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 90341c1e-94a2-3ad2-b8c6-daa9d2d63b80 | -9.00473 | -65.43813 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e79098fc-7444-337b-8f77-0a980dacc6af | -9.09473 | -65.4901 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1245e31-6d78-33a2-99cd-420561ffbc91 | -11.0269 | -57.23997 | 2026-08-31 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f579663e-8184-39a4-8921-e24ce77a3abc | -4.96559 | -55.83962 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d889195-19cd-39be-9604-836f734ccd66 | -9.48601 | -66.6284 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300f9dcd-279b-36af-84c8-e6e45eddbd99 | -8.94315 | -62.37495 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71e8fa60-7143-303c-af22-ab789b06298e | -4.84794 | -55.83321 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42570f39-ca1e-387c-9bba-10a7fe829c09 | -9.04456 | -65.44708 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebac3760-87ab-3fcd-a44a-12a77adef163 | -4.16055 | -60.69802 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ccbd702-82a2-3db9-9812-f881f1006731 | -9.36487 | -60.31411 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 735ab9ac-8462-3e86-b3fc-ee3891797c6e | -8.91276 | -66.94884 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d06416c5-ff05-3a9b-b764-2fab89e85e6e | -9.9419 | -60.51237 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a54e70b2-90dd-3f76-8e16-8f72ada25a78 | -4.85928 | -55.83967 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdd47589-9bc4-3b05-9a6e-479293908b2d | -3.62046 | -60.55246 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dad80d9-b9bf-3d31-97ef-c55e4d51c8b1 | -3.62534 | -60.54909 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc3531fb-678e-3040-b26f-296d604b31b4 | -8.35258 | -70.1027 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d19b98-54f4-3920-92fa-a9be6c474eea | -9.46369 | -68.23594 | 2026-08-31 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53eb36b3-8567-35c3-a423-78aeddaaf2dc | -4.58597 | -55.93927 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9846d310-228d-3cff-815d-0d02b4856d76 | -8.0481 | -72.42941 | 2026-08-31 05:55:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cbfe3fc-a71d-391d-85c1-7aee4e22176d | -3.60904 | -59.07476 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d596ac87-d531-3c98-b122-284af5243cd6 | -10.48456 | -59.6074 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46888039-6c02-39fd-bdde-73609793f4c5 | -9.79804 | -60.17861 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 496befed-aeaa-3147-8588-3263e4242b5a | -10.37309 | -69.50597 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f81394c-b4f5-37b9-9d4b-fdc4bbbc8a82 | -4.96371 | -55.85293 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e91f18e8-b229-3fbd-844e-c801c2f752a7 | -3.76074 | -59.334 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc7ccdaf-4d26-3889-91ed-804df25128b0 | -8.59851 | -70.21516 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64273640-a811-35e0-9678-d7ca3ae1ef84 | -9.78642 | -59.44611 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f567b8a0-8a98-35a2-bdb6-f3bfdf641195 | -8.60448 | -70.20298 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e488148-8228-3905-91e7-5f6cdb1d3b2d | -9.30742 | -56.80331 | 2026-08-31 05:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f83c661-9c8d-3a60-bd77-c8e390af6d5c | -8.94143 | -62.06754 | 2026-08-31 05:55:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 762dfe78-a1f3-37e1-9ab6-ad901cd9fbd1 | -8.70328 | -63.96758 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dd654ac-1fbd-3da6-a294-8d17f5331daa | -9.85083 | -64.98711 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68c7d9ba-0c28-3542-ac43-b68dd38636c1 | -9.79322 | -60.17797 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd25f86f-9cbe-3f32-b9b2-f68462395d3c | -8.93266 | -67.36407 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fee0d75-30ca-3588-bace-168de4d0b0a0 | -9.79248 | -60.18325 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8104a24-7f00-3abe-b611-edca0c1e265c | -4.95893 | -55.84334 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a436b790-baed-367c-9d0e-619c9dd9772b | -10.37646 | -69.50652 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcc6552f-c8d4-343a-a510-d4cf294966e6 | -4.1514 | -60.70075 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52f5403e-e855-3f36-a172-3a4e2e923809 | -9.09186 | -65.48573 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f846066-72c0-3ddf-ab19-9d5f0fb403ac | -8.9644 | -62.39531 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a889397-d271-3d61-b0dc-01f856c0c98d | -8.80013 | -62.49866 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c30eb3f1-170a-3fc3-b7b9-89acc5537ffb | -8.94292 | -62.3697 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b06c194-6ab6-363e-b40a-7b9542e224f3 | -10.90842 | -61.67755 | 2026-08-31 05:55:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ccdcc0b-f5ab-3f0f-a029-3f8faf4a5f76 | -8.67173 | -66.51318 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 249367e2-f275-3a54-8bc6-d86142ae6981 | -9.15924 | -59.37214 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0375e0f-7d20-32d5-97c4-8d7554160bca | -8.63091 | -66.53941 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d054884-367d-3b87-858a-93e17613d8d2 | -8.78406 | -71.02962 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8ef26f1-22b9-3f19-a385-39246e1b16d9 | -9.00126 | -65.4376 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c4679b7-d78f-380a-8c09-8a056ef58808 | -9.15884 | -59.37514 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 307701a3-55a1-3eb8-95af-ddc9e21e395e | -9.46425 | -68.23244 | 2026-08-31 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c463514-7ea0-3590-af77-2047076baf96 | -9.89101 | -60.28031 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13e31f55-f6b2-3ceb-abdb-82a4ca7cc382 | -15.68014 | -56.27348 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a3eabe-2541-3904-99ad-f2b08e816a51 | -9.00849 | -70.56326 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c1c085-8a7c-368a-bb21-cfda7c6dd0cf | -9.3696 | -60.31485 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b688379-5a2e-3c96-a44f-c1a68f49750f | -4.15687 | -60.69339 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6d3b063-b79d-3882-89d2-606cb7daa50b | -8.94088 | -62.07138 | 2026-08-31 05:55:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c08c74e-5f37-3d32-ae71-0729e3a202c0 | -10.47833 | -59.61541 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README78.md)
