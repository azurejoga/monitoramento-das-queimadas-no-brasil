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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 462bbd8b-2102-3475-906d-875021fd2f9d | -6.16381 | -52.63422 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bdae5c0-96c2-3418-bd08-5e65035547fe | -8.45177 | -54.73817 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ca22c29-17b3-3d77-a8fc-7d287113a5b0 | -6.13831 | -62.5272 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31426ebc-d173-3a5d-93e9-c40ba9d47a2a | -3.6591 | -58.92089 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b131baa-8373-3bf5-8c29-6b166a32d8f8 | -6.31908 | -54.75309 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1ae8447-eb6d-3150-aa9a-cc2ec72dc695 | -6.94227 | -56.45657 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91d3f881-29d1-37ba-9092-15fe7ecf8e24 | -6.69069 | -59.95107 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 575c82a4-aa30-3844-ab40-c470c7ca7afd | -6.19551 | -55.2823 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd2725d5-2e6b-36f6-96c7-2e1ebed7707b | -5.75743 | -53.40326 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e839df48-e0c5-3024-9fc5-7637c4155123 | -6.26141 | -55.42856 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b530151-b164-30fd-bb23-658d62a7b79d | -8.44647 | -54.6983 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51baee5e-ac42-3bb8-9295-a2f13b07d4a3 | -8.47738 | -54.71597 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| f1c65d13-6513-306a-8a4a-5f7d91d8ddca | -3.61787 | -60.55174 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccd6716e-4f54-3f48-9c1a-d651e9cf5ab3 | -8.43805 | -54.70364 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2418b36d-7b42-32f1-adc1-f1021902c6c3 | -1.50961 | -54.96154 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97d68e1f-4110-346a-b858-2fd45ed6d879 | -6.81331 | -59.56446 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b132108-5b56-31c0-b1c5-162696da0721 | -6.31553 | -54.75255 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73fdb765-dac9-3960-ab23-6cfbc4034045 | -2.93189 | -54.15611 | 2026-09-02 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea50555a-1e92-348b-a501-910820bd06b8 | -6.81927 | -59.44008 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3290d5c-c1da-3a8c-aaab-d6f2394fc09d | -4.23813 | -62.23354 | 2026-09-02 05:16:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98974237-f494-3b0b-9839-476ab6b668a7 | -8.44509 | -54.73076 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e667f4fe-2ddd-358c-93b0-595e9e1cf1e0 | -8.44598 | -54.70052 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ac58d8b-1792-3c1b-8eac-eb43003e7d1b | -4.97311 | -55.85005 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34ab86fb-7b4a-3d37-90da-a439271f9670 | -3.63588 | -60.54826 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057a416c-ed14-3af0-a8cd-3d65168ba65d | -3.19744 | -61.13856 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0874d3af-2471-3be6-885e-3cd01c403958 | -8.45115 | -54.74241 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f3b3f0b-5427-3cb9-b9c3-271bf1cd7aec | -6.61519 | -47.63938 | 2026-09-02 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c656b3b-c767-3271-bb85-b1a29d70bbdc | -5.86794 | -57.77945 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b171064-5640-351e-8458-26529fcb27a7 | -6.58134 | -44.7883 | 2026-09-02 05:16:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d96ede38-6ff8-3bda-a2f8-5dd6e37afd59 | -6.22833 | -55.61835 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a59d367-e03c-39de-8a8d-93988afd0210 | -4.35503 | -55.02925 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 114e42d8-1e83-3a50-8669-b55ea34d5503 | -5.9741 | -53.58168 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6832281c-4738-328f-9d1c-142301152a65 | -5.88503 | -57.75733 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b65f50e-f219-332c-a68c-e1f8cc1fded2 | -7.30067 | -60.62722 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b96f9d-bf25-3078-8b48-bded8b3fb98c | -8.46219 | -54.71798 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f37e6081-75c6-35c2-8754-2b8a5b244f03 | -8.11422 | -54.94842 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cb33246-6a7f-3112-9ec9-246d748e5339 | -6.25797 | -55.42798 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c310d1cd-bc93-345d-a854-37ca6c6813b8 | -5.94414 | -57.6856 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f94cd7c-13d8-31a7-abaa-b25dd99dbd2e | -7.31903 | -61.14465 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e36587-069b-3f4b-90ba-906b0e819e2f | -8.475 | -54.70697 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b8675e64-d7b3-3cb3-a2c0-6ca2fb6ab205 | -5.98771 | -57.68896 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70cde655-0ebf-39f9-9d53-a42b7753c659 | -5.2476 | -55.91365 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ceaf485-8296-303e-9d4a-753960926a6f | -5.97479 | -53.57712 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c208f16d-16f3-39e9-8466-5a7fe8f9178f | -6.04727 | -53.83734 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eccf37c-870f-3a3b-8191-14531146ee87 | -3.23853 | -47.25467 | 2026-09-02 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 39027b8c-8af4-32d3-bb2a-9a35258c8ba6 | -6.24933 | -55.43822 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77a28065-32de-3df5-a013-5a6233df278e | -3.62192 | -60.56394 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 707e7646-3ec8-35cc-8903-002efbeefe5d | -6.11736 | -57.68473 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f94b4a-482a-393b-ace9-6ed8935e1da4 | -6.1306 | -57.68683 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 287dfa52-79cc-3644-8289-cb265cf8c0b5 | -6.09753 | -57.70285 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd3d12c5-c088-3ae5-8066-f3896828f80c | -8.44399 | -54.71523 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a82e520-7d9c-3de4-b6e5-6f18737f71c4 | -6.56852 | -55.61643 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da36cb12-5792-3b9c-9979-91f5789f8592 | -6.94172 | -56.46012 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 529e4ffb-dd2f-337f-97c9-9428d853232f | -7.258 | -61.105 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6460127-2bf1-361f-9691-5cc9d9ac1b37 | -5.95628 | -57.69461 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90472748-0934-3a3e-92e2-38b3fcbd512a | -6.25394 | -55.43119 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ac9f753-0366-3121-80f3-f3acf62eeecc | -7.65095 | -45.87945 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 239b685e-0ed3-3ee5-a932-385b544c5a99 | -5.24816 | -55.91006 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99e887b3-5d45-3fc4-a66e-a082ac6500fd | -7.56679 | -61.3684 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f29f607-a7a3-316f-b38d-34131aebc9d6 | -6.55348 | -55.13854 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bc41293-2e97-3272-b4a7-02c9566e6dd1 | -4.97367 | -55.84646 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78492293-7882-3758-9dc0-305f8e2f012c | -3.12477 | -61.23342 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68010555-1cc6-3874-b746-9ae16caf6a47 | -7.66453 | -45.87558 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca6bc443-9e1e-35ab-8acd-a877f1efbb8d | -4.97199 | -55.85723 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c2bb96c-88da-31dd-880b-a3e71e11c02a | -7.53892 | -60.72225 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77a1417c-8a7e-3982-b5e4-30ebf9ff88e2 | -3.13723 | -61.18096 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c96e317e-db97-3d84-bd78-c868e7271448 | -1.35473 | -55.38549 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c9407a-3506-3317-8692-9f802b485832 | -6.0775 | -53.66388 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b598d443-bef0-343c-8fab-8a4b08f21c63 | -8.45604 | -54.73448 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 051bf483-daac-37b3-8538-8b2a33545199 | -3.89465 | -55.42308 | 2026-09-02 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 440556d6-2ff4-3b58-9a0a-d763bbb85078 | -2.74663 | -60.23789 | 2026-09-02 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00211335-18a8-38ec-96fe-e375da0b4287 | -6.94161 | -59.63815 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ee31f9-7855-3020-af15-fab08769e499 | -6.75156 | -59.64233 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7af23c2-f463-3a30-b056-be989f738aaf | -7.35614 | -60.57833 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8275624-dd20-312b-86bc-91813bd4f3fe | -6.81868 | -59.44375 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0855f864-316a-3ef3-bb3f-b7a847abc2ae | -7.20598 | -60.67491 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85f4dec2-2764-3b8b-93c6-298287725a03 | -8.47676 | -54.72019 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3fe8489f-048c-3e22-9345-77b872bd1df8 | -6.87849 | -59.40029 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ce4e18a-ad68-339c-a5a2-d350b9cbb7e6 | 0.01176 | -60.60133 | 2026-09-02 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d09ee591-18cb-3430-8e80-39e8f69aa033 | -7.3628 | -60.6043 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aadbf93a-eff1-3102-898d-a8ee0ee7c9be | -7.20531 | -60.67899 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 431f6cdf-b07a-325c-9d5f-54f383dadbca | -8.45315 | -54.70356 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ca8114-412b-3ca6-811a-eec7327329b7 | -6.11686 | -53.86851 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70e2b4d1-4da9-3dd1-b1d0-6b25e87ba1c5 | -8.45377 | -54.69933 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd80186-2e70-3810-8f2d-cb7b0279725f | -8.27778 | -54.94687 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13f034d1-4e9c-3101-8368-84eb54fa95b4 | -8.45553 | -54.71268 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f8d1bd78-0229-35ba-a773-733ffff4d47b | -6.81587 | -59.43952 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab4177c-e590-32f0-ab3b-110c4a7c1af8 | -8.45478 | -54.74297 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df1fbb4-7737-3f06-b8a5-51a24185d3c8 | -8.45616 | -54.7084 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b183ae1b-183b-3d30-bb5d-9e50816a6ba8 | -4.10126 | -60.66128 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff17161-084e-3d05-a178-f008b9dd80ba | -3.37206 | -59.38997 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 843509b2-d5b9-35ff-9cec-12016ca3fc75 | -6.25621 | -55.43931 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| da701afe-629b-3453-810a-24edc96ec5c6 | -5.96235 | -57.69911 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ac8cab-7818-3ca8-b2f4-490bda2fefa5 | -6.25276 | -55.43877 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55a8ce54-85d6-3a65-843f-c88a22af8086 | -4.51838 | -48.74978 | 2026-09-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65b6caf4-9766-3f24-8a22-68bfbd732e84 | -6.1061 | -55.82193 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 853cc376-8088-302a-978d-70a00624996b | -5.58082 | -60.20114 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c523f4f-2939-3d27-aa1e-e52ba0823bc6 | -7.3049 | -60.62373 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e26146-699f-3029-8637-ae69f6c12ca9 | -6.25453 | -55.42741 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23e80709-d955-3cc4-a0f9-ee0008b6ea66 | -5.97341 | -53.58624 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README49.md)
