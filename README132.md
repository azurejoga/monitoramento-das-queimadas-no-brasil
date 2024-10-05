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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f2102b-965f-3d8f-8eb6-28899e97f031 | -1.16045 | -53.78664 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b8c95ea-c759-3227-9808-9a12b06e952f | -1.12862 | -53.63375 | 2024-10-05 05:27:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a652bfc-5442-30b9-a62e-e6fe742afb54 | -3.06909 | -54.77785 | 2024-10-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1efe33cb-1b0f-3af5-8174-1c0ce6ddc7d1 | -3.06462 | -54.77712 | 2024-10-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddb8a838-cb42-37a2-ad7c-2abf309fc9e3 | -2.97415 | -53.7265 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e60e0570-6a49-3998-bd8e-650acdff6f83 | -2.97387 | -53.72701 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23e224dc-321b-364e-9f0f-1bf59c8cb08b | -2.96935 | -53.72577 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecb941e9-a7fc-3663-a93c-eb573833bb92 | -2.95251 | -53.70706 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21db5a59-b44b-383a-8930-438b1b5743b5 | -2.95172 | -53.71231 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a481ed99-1dc5-305e-88b6-766e10c2435d | -2.81841 | -54.71417 | 2024-10-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95d54a80-0a33-35ed-87fe-d4b1b8bff468 | -2.72683 | -53.97727 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb6e7729-fca4-3399-b80e-ba7afbb0ef8b | -2.72492 | -53.97596 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6f430e3-c657-3a72-b8b8-ff3ae9e03661 | -2.60328 | -54.21347 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed36821c-ea44-3402-8a42-2b03fe6d7b78 | -2.31792 | -53.85723 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79086d5f-09e4-32ea-8c9b-60449ea11642 | -2.31718 | -53.86229 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ff85b4-76fc-39cc-a253-67c26b6b6fbe | -2.3154 | -53.86106 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fab5472-4fb7-3069-920d-d1e9b4ed446b | -2.18676 | -55.1311 | 2024-10-05 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 867cd56a-74bf-3f25-b9d6-46d21174a141 | -1.82698 | -55.18773 | 2024-10-05 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4d2f9f0-69c3-3c6c-a95b-696895ce4d6f | -1.63168 | -55.04819 | 2024-10-05 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2760fb35-9e47-35e7-8974-61caa8cb570d | -1.50671 | -55.10101 | 2024-10-05 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43a2f86b-dd98-346f-a3e0-9396ea7e55eb | -1.20553 | -56.21252 | 2024-10-05 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 621c34f2-0129-3e1d-8c70-c4fb90dc95c9 | -1.20447 | -56.21481 | 2024-10-05 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1731b974-e632-3655-9a1a-ebbbc3277836 | -2.53188 | -58.04571 | 2024-10-05 05:27:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5648a1a9-5889-301b-b2cb-9fdcd1628e36 | -2.9016 | -59.22897 | 2024-10-05 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251cad23-52bc-3d1e-9637-9adc1d68c8b1 | 1.08041 | -60.42387 | 2024-10-05 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec1cee7a-708f-3753-b7b8-42bfd74797c8 | 2.67174 | -61.32519 | 2024-10-05 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1454684-1bbf-3a04-8546-7e911266d747 | 2.6684 | -61.3257 | 2024-10-05 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 335610a2-0bfa-3a01-91dc-65f924516244 | 2.60128 | -61.28602 | 2024-10-05 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6616f6d-7d6f-3867-ba82-4624270980db | 2.60073 | -61.2825 | 2024-10-05 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bd2c901b-7a60-3277-8b17-e36a54725130 | 1.32752 | -60.71778 | 2024-10-05 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0781e766-93a1-3cb3-9f60-f0d478a0a673 | -6.27513 | -62.47964 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 288b9ea9-bdcf-3020-9249-4540d6d3d44d | -7.86982 | -63.45724 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aeb58f4-c6c1-3876-b529-771c9db4eb49 | -7.83053 | -63.40401 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76c3f6db-baae-32ab-bb07-78b85dbbafbb | -7.58561 | -63.36089 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5bf3f58-e474-3e23-9e4a-438b2d85e318 | -7.52255 | -63.26437 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3da36986-7314-3df9-a3ee-6963f1721a09 | -7.50405 | -63.35878 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ddde8b2-16cb-3aa9-8474-8adb4eba1e8b | -6.98267 | -62.91256 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93f5cddd-1567-387f-9b51-bdab72369a53 | -6.98212 | -62.91603 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5130345-1e25-3474-a9d9-091edc599623 | -6.97936 | -62.91203 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f8e625-116e-3fee-90a2-fe1e5837a645 | -6.97881 | -62.91552 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1efafb03-2355-3003-8c15-b29688fd6de7 | -8.6363 | -63.15321 | 2024-10-05 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3f1fe36-1742-351c-8e38-25e83e6516bc | -7.68783 | -64.97669 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e75e51-cc0f-3d1c-ae98-5121ce4d5bd5 | -7.68718 | -64.9806 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e8110e-8a0c-3794-9ac2-de83c36975dc | -7.68369 | -64.98003 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cef9a5c-b881-3d86-b4cf-01d70eed4c00 | -7.68304 | -64.98395 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26552acb-d355-30b4-97ec-ebe942d90314 | -7.67954 | -64.98338 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a83b1c6a-2734-312f-9419-f7bd4f5d7033 | -7.67255 | -64.98225 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 237f4906-4989-3c99-9964-e49bc10be34c | -7.6662 | -64.9772 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c591e8e5-a4fe-3e65-87e0-e1c9ba90dc71 | -7.66334 | -64.97272 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 420badb1-04ba-39b9-8c05-18b7784978c7 | -7.66215 | -64.97322 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3808fb07-bcec-329e-8a9e-91fa20461557 | -7.51571 | -64.67588 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5ffe131-44f9-313a-9b6f-174884d488f2 | -7.45463 | -64.44777 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b54f9ebe-b96d-342a-a00b-b7c80d26e4ec | -7.45402 | -64.45152 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a24d3f73-8a13-37a3-997f-1d000faae76f | -7.4512 | -64.44721 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71686513-103c-3598-9d4d-6cca8c8cd76c | -7.45059 | -64.45097 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 970c95da-f581-3fdc-abdd-43c395a294d0 | -7.35599 | -64.68988 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d006b5fd-e630-31b0-b15c-4e0e8232afdb | -7.33075 | -64.67004 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aa7a290-b771-30a8-b038-4a8e4e7ed81d | -7.33012 | -64.67388 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f9ef609-7407-320c-9193-3082d3001d1f | -7.29326 | -64.66006 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeedde79-28a2-334f-b5b2-acad74c1d8ac | -7.28979 | -64.6595 | 2024-10-05 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24748c2b-6004-3066-b8c9-dbc4f81be7e9 | -6.81811 | -64.31998 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe6b95a-528c-38fb-9013-c28084bebc72 | -6.8175 | -64.32374 | 2024-10-05 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3b268f1-0488-33cb-89a0-4f8b3e22650d | -7.74204 | -49.2194 | 2024-10-05 05:29:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90c49771-1787-3e92-9864-92d0986e9a5e | -10.32861 | -50.50967 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35fb80f3-2810-37f7-8ed4-0a9f29b67670 | -10.32793 | -50.51536 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11dd6b1d-6d18-3490-828d-d180dbb1f770 | -10.32725 | -50.52105 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d41f836d-e19b-3b7c-be80-90a8a781a905 | -10.32657 | -50.52671 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4fd31a9f-f099-3910-8b77-ce7d1826d320 | -10.32589 | -50.53238 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed2e4be9-7aa2-3202-a652-96000af7bc62 | -10.32271 | -50.50307 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fd0812c-c9c2-37a0-8cb7-f5c22f5b8da5 | -10.32203 | -50.50877 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2f980ef7-0d3f-38da-80bf-c2fb0522dbb8 | -5.65151 | -49.7174 | 2024-10-05 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a046775-ba72-3834-b855-5eddbaa856f8 | -10.45447 | -50.72684 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41092b17-3446-3e77-980b-662f06508470 | -10.45376 | -50.73264 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96b16793-9459-3333-aada-52ccabd6ea6b | -10.44869 | -50.72007 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a8528be4-1c88-3c89-8657-76a3a5929501 | -10.448 | -50.72575 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a94c17ed-fde5-38b0-aa5c-5405b14dabb3 | -10.44731 | -50.73143 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c2eb5aa-ef31-34c9-8ea9-efa23125ae75 | -10.4422 | -50.71915 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2ccf2229-7b99-3f47-adf9-1018db823744 | -10.44151 | -50.72476 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf9dbe4d-9848-32af-9cee-ca63178d1318 | -10.44083 | -50.73038 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28383ce4-ad7c-305f-a1e7-ec02a2552c85 | -10.43678 | -50.76368 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3c1a2b6e-5d99-349c-baf8-fa85dbeff5c0 | -10.43502 | -50.72384 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 354baa5e-287e-3c28-b8a7-11a630493419 | -10.43435 | -50.72942 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fd96aad4-6823-3ee9-b042-d3ba05f9e5c9 | -10.43367 | -50.73501 | 2024-10-05 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 88e260d7-f7a1-3a44-9563-1480daa84402 | -8.63894 | -53.17607 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74c3819-d3ef-33fb-adeb-1fc786a4e7f4 | -9.85 | -52.06501 | 2024-10-05 05:29:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114ad7c3-8639-352f-919c-c894316f3e1b | -9.84942 | -52.06951 | 2024-10-05 05:29:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa40cee7-50ee-3f5e-9f49-55ba75ac006e | -6.1497 | -53.41943 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3725cd9-5a2d-31b9-a8e4-8993681255b2 | -6.14927 | -53.4226 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fa13447-5438-35b8-ad61-23b28c62a3c2 | -5.90276 | -53.4456 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0809616c-906b-315a-8f75-6d628f80941d | -5.89811 | -53.4415 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51553601-d6f3-3944-b9c2-d69609398ddc | -5.89769 | -53.44444 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e6d39c1-5bcc-3953-adbf-cdc81466fb5e | -8.9074 | -54.45791 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 118f1f85-093c-30e1-916c-3629bee37778 | -8.90685 | -54.45793 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e84d2b2d-399c-378e-912b-1e6d5f91cdcd | -8.90241 | -54.45713 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b0b318-35e6-3fa1-9a19-2207da2c746a | -8.90186 | -54.45716 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 288a9e84-2c3e-31ce-a0e1-0328b78eed27 | -9.65719 | -53.59016 | 2024-10-05 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ab8e1b5-9946-3cb5-8232-4c32faaa11dc | -3.87615 | -54.22827 | 2024-10-05 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8158cb21-2c8f-3cdb-82ac-949084d1674e | -3.8745 | -54.22682 | 2024-10-05 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c2ada89-9022-32ce-9972-6a42abef43fb | -3.87375 | -54.2318 | 2024-10-05 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52ea52f0-4e3c-3666-83ec-5f35f7941d0d | -3.87073 | -54.23256 | 2024-10-05 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README133.md)
