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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c43e376-06c8-38ae-8cb2-edfb8badab20 | -5.6522 | -60.2342 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef576f5-00a0-3548-b48e-3abb30769acf | -13.2467 | -61.7337 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 070b5700-2b2f-31c2-98c4-8881c4733b20 | -6.6648 | -59.927601 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e50378b6-3c94-3a5b-ac29-80fa1bcc8802 | -8.5277 | -63.8773 | 2026-09-07 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91ef1c5d-dd01-36d5-a54a-12309301a456 | -4.281 | -59.9715 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f68afcf-d794-3e67-8c42-320ce0ffbfe0 | -5.3739 | -56.030998 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf85b2f7-e795-344b-ba98-94760a702a2e | -3.3867 | -59.4077 | 2026-09-07 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea8ef17-1b58-3b18-b3c8-3b5468c2b551 | -3.8255 | -60.767601 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 039b2812-efba-3d88-9dd7-7eb566c8803f | -5.1507 | -55.959099 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4effcf52-5f34-3852-ae66-fc0e45e554f5 | -3.6126 | -60.5606 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44e8d0f3-6410-3326-9137-24de8b08678b | -5.2726 | -60.154202 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d769c1a-f012-30b5-8f7c-9563072fdbbf | -3.7091 | -58.932201 | 2026-09-07 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| affb22c6-4915-3746-8454-013f48b5a36c | -13.2369 | -61.735901 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f59db7e-e794-3155-af47-e317338aac86 | -3.1404 | -60.659698 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a97a19df-1cad-3f70-a985-37f95a82c465 | -6.6617 | -59.958599 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41890aab-13a6-325f-b337-bb3acdddc0f4 | -5.3003 | -60.140301 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c67e26ac-859f-3773-a41a-1b72eb4055e9 | -5.302 | -60.147499 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9f726d-cc5a-35a8-86f3-99a9d0bd1157 | -5.2855 | -60.1208 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ffcc8d2-554f-34a8-8a50-fda67ff0c317 | 3.9706 | -60.564301 | 2026-09-07 01:29:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c23ad0de-3496-3540-b570-3b7e0f219651 | -6.6877 | -59.9375 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcc45b00-482d-356f-92e2-28951288456b | -5.9963 | -57.6908 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a054bf-7026-3785-9efb-8da974f6c472 | -4.6788 | -59.596298 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 696c8cbf-639a-3c20-8430-480ad82201e5 | -6.6763 | -59.932499 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b37181e-6b97-30fc-b9ba-6db0bb4ef54f | -3.142 | -60.666801 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0bdddf7-a6f7-35d6-90db-e0e0b4e0c561 | -4.1001 | -60.6609 | 2026-09-07 01:29:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03e2d2d7-1ff6-3e49-a828-0902214400d0 | -5.6539 | -60.241299 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eee115be-ee9b-323d-8367-860ec7658324 | -13.2173 | -61.740299 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 015d47a5-6717-36d9-98bc-dde0f2027e60 | -3.3893 | -61.3367 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a677658-bd99-3609-938a-54d426aa60e6 | -6.6746 | -59.9254 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20451a50-479d-3c77-bec1-843a0ac3c0a1 | -13.2434 | -61.765598 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18d16099-c56c-361c-9b12-e6e07d3d1af2 | -3.8369 | -60.772499 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2c652e5-6c44-3edf-8369-29f61aa69c53 | -3.1437 | -60.674 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 305cdf4d-a340-3e27-9a0d-a678cd067126 | -7.0689 | -56.476398 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29dbcb31-56a4-3751-8a47-ae1145ef56b2 | -3.8353 | -60.7654 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 056aa8af-1481-3429-b444-865c2dffa4fc | -13.263 | -61.7612 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7618fce-d52b-39a1-b5db-28330e5bbbdc | -13.2385 | -61.743301 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8340f962-f60a-39e2-b19f-611eeb4974f9 | -4.2972 | -59.952202 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc5e72f-2ccd-32cb-9060-2aae6333aff7 | -5.2987 | -60.133099 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14e5b031-ec13-3a3a-9c86-5809eed34bbd | -8.7596 | -62.4216 | 2026-09-07 01:29:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1f060bd-b98b-3440-8591-4fd1d5fe77dc | -5.2872 | -60.127998 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2345d54c-2040-31d2-a67c-9c7bebe58970 | -8.5196 | -63.887402 | 2026-09-07 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51e6f2cc-a605-3928-8c7a-3c38b87d569c | -3.0828 | -61.528999 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24fe0819-9d2d-34c2-8f56-21ec254c7f16 | -6.6844 | -59.923199 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0b82f1-7f76-3731-b70d-85268cfa33b0 | -3.1387 | -60.6525 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a98cd359-4d43-31aa-8694-e891a9f1b54c | -6.66 | -59.951401 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9e40db2-eba9-3aeb-94d9-2487d2c756d5 | -4.4081 | -60.074799 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2676b49-c0d6-3c40-b85f-55689a458fd3 | -13.2255 | -61.730701 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4fc75e-513b-392b-ada5-43537a13082c | -3.155 | -60.633598 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64fe0521-ad30-39ab-8377-916b296167a0 | -7.6186 | -57.6115 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4903adde-9cc4-301c-9bb5-60367be28991 | -13.2663 | -61.729301 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46a39850-f36c-3cd5-a8dd-fc57fcfe0223 | -6.6665 | -59.9347 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47b0131f-4d21-3005-a202-34b61d15e694 | -13.2271 | -61.738098 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2975c857-aab9-3d9e-96dd-199d3aa0f2f6 | -5.3711 | -56.019299 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdac44e0-4b77-365e-afe6-812e09bb1281 | -6.6502 | -59.953602 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94637da4-1406-3c88-a497-9c759350cf23 | -7.0664 | -56.466099 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b98052-8702-3a11-98f6-7689f9cff7b6 | -6.1396 | -57.686001 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df33483c-1e9f-3955-bd07-4a63902d10c8 | -3.7647 | -61.758301 | 2026-09-07 01:29:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76b5f0b0-f062-3dfb-8b2e-ee2f9c3adb53 | -4.6805 | -59.603901 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee21fb0e-40ef-3efc-b97a-cb7c99e350ce | -6.0002 | -57.7079 | 2026-09-07 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f7e697c4-1652-3fca-be15-4b925161348c | -2.9645 | -48.7036 | 2026-09-07 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 0b37a2b5-8496-30f5-8026-e1cf332a5a0a | -2.6203 | -46.7602 | 2026-09-07 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0bc0c354-3985-306d-88cf-05495a26a4f8 | -2.6388 | -46.7597 | 2026-09-07 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 3486ccb7-4036-3b75-aa5b-ca3418cff903 | -9.7522 | -43.3907 | 2026-09-07 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 94baf297-4db0-3505-98c5-6803d66aa1a4 | -9.7328 | -43.4168 | 2026-09-07 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ad767967-9814-350f-8339-172610ed8950 | -6.6514 | -59.945 | 2026-09-07 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c4d3d148-d996-3ca7-bbe0-6147fa5b414f | -3.6215 | -60.566 | 2026-09-07 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 87859810-ca66-32a8-a34d-068438f3dd54 | -2.8655 | -50.4434 | 2026-09-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 70415419-346d-361c-a087-90bbe8e3b498 | -6.6699 | -59.9251 | 2026-09-07 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b002ee7a-ae28-306a-b908-01774ec69688 | -3.1462 | -60.6506 | 2026-09-07 01:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 839d56d4-3608-3e48-8297-983a8fe1d437 | -6.0004 | -57.6884 | 2026-09-07 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e3e6393a-ac30-362f-b530-653c53e269b2 | -6.6884 | -59.9244 | 2026-09-07 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 79cf494e-d4f6-35b9-9802-9c6b72d60331 | -13.2477 | -61.7342 | 2026-09-07 01:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5d556295-1155-3ec1-84c2-ef7cc1a782c3 | -3.1461 | -60.6696 | 2026-09-07 01:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e5761f45-5b57-37da-8efe-bb6fc55e0595 | -13.2287 | -61.7355 | 2026-09-07 01:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0a5dee23-838b-39b5-ba8d-e77a93cbfef1 | -2.6387 | -46.7817 | 2026-09-07 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 8d3492be-01bc-3ac8-af51-c5ca55576dff | -2.8839 | -50.4428 | 2026-09-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 0d0609bb-1c62-3082-a17d-992ad3197df4 | -9.7332 | -43.3932 | 2026-09-07 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 102.7 |
| a014e53a-484f-3f57-aa38-3a96b0a398db | -9.7519 | -43.4143 | 2026-09-07 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ef141e6f-af2e-32e2-ab8e-2c9bf43b6ad6 | -2.6202 | -46.7822 | 2026-09-07 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4906923a-a071-33c1-8853-7d96755ce3be | -6.6698 | -59.9443 | 2026-09-07 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c8b9fce7-749f-324b-ad3f-4d2f8f01d13a | -6.6513 | -59.9642 | 2026-09-07 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| b7f664e3-b3a3-39cd-8e88-9e9a27d26ecb | -6.0002 | -57.7079 | 2026-09-07 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 16af0557-ad85-3443-ae6c-3e20bf32d313 | -2.6203 | -46.7602 | 2026-09-07 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a947770d-6b07-3b95-9ed8-b9ece288f415 | -2.8839 | -50.4428 | 2026-09-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 019f8fec-ebab-3957-8827-75512852719c | -3.6215 | -60.566 | 2026-09-07 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| db8e3ce6-fa86-357c-bcc6-6148ffe0695a | -2.9645 | -48.7036 | 2026-09-07 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 893961dd-f708-3683-9f1a-944e845f497b | -6.6699 | -59.9251 | 2026-09-07 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 074700ae-a0ee-3cfe-978d-420a099ef9ea | -5.9819 | -57.6892 | 2026-09-07 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a4847807-1efe-315e-b9f2-e6a8d6747770 | -3.1461 | -60.6696 | 2026-09-07 01:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c6dde5ee-02f6-360c-b797-9868d1fa840e | -2.6387 | -46.7817 | 2026-09-07 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 4d1da04e-4c9f-331c-ab29-65413b725f7f | -6.0004 | -57.6884 | 2026-09-07 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f45a7662-fd69-3af8-aa44-66066d483ba2 | -2.6202 | -46.7822 | 2026-09-07 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 02f28b2d-c317-3396-854d-3fdc3fba6745 | -2.8655 | -50.4434 | 2026-09-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 0b61555f-6f39-353d-9ad4-d1d6ad643952 | -6.6698 | -59.9443 | 2026-09-07 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 91d6821a-680f-3207-9019-152b7503dde2 | -13.2477 | -61.7342 | 2026-09-07 01:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0e1a0373-96bc-307d-b56f-c397f47b35e7 | -6.6513 | -59.9642 | 2026-09-07 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e734af28-e4b1-3de5-882d-fa99efb48504 | -9.4777 | -40.2867 | 2026-09-07 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 3ad70043-8e23-38c9-bde8-1d092c02e49d | -6.6514 | -59.945 | 2026-09-07 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9a0aa855-d363-3c00-80bf-1dd78a4c3e52 | -9.7332 | -43.3932 | 2026-09-07 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 67.8 |
| d3d2d15d-1390-394d-b65d-bf249ca5e11a | -9.4968 | -40.2839 | 2026-09-07 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.6 |


[Clique aqui para ver as próximas entradas](README7.md)
