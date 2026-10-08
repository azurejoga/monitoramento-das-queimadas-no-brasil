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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dbce972-41fc-33a0-afef-ee00b511d43d | -9.4935 | -64.3706 | 2026-10-08 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 403aa0d6-f124-3d81-809a-df7c315a420d | -8.7225 | -45.204 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 14cc63e6-40e7-3f10-a929-c4142343cc80 | -3.8383 | -55.9774 | 2026-10-08 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 45ce0211-349e-326d-a444-be5bcf8b6c14 | -3.1298 | -53.7834 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c18b3d8e-fab1-366e-8e15-b470c67fea82 | -2.499 | -56.0675 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 41185c78-c144-36b1-ba06-999b0af4a6ca | -2.4805 | -56.1072 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4edd1463-bb40-318c-a2fc-5dc3ad4bbd3c | -4.4507 | -47.9112 | 2026-10-08 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3fc04f4d-23e4-391c-8cf8-271d2552c86c | -10.434 | -47.2601 | 2026-10-08 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 83d7d2ad-57c4-33d4-945a-e003b79bcaa8 | -2.4032 | -57.8848 | 2026-10-08 02:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 287546fc-dc1f-3555-95a1-85e3f22e045e | -6.9535 | -45.2619 | 2026-10-08 02:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 440b643b-03d4-3ba3-af08-f91e7ed720a5 | -3.0374 | -53.9268 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1d81e1ec-f033-38ec-aadb-552c70f7b703 | -5.6932 | -53.487 | 2026-10-08 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| dff8f423-9415-3062-847a-4b2cd08b01ba | -6.6315 | -43.7533 | 2026-10-08 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 243a2db5-acb7-33e9-9ed1-02790e7430e9 | -7.0065 | -59.1223 | 2026-10-08 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e65f5a63-ab99-3c22-ab25-d669c6d2d639 | -5.7376 | -45.1533 | 2026-10-08 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5f83afc8-94e9-3d9e-b1d9-026670572764 | -8.742 | -45.1563 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| ce01ce33-b19e-35f1-a972-fcb5e4466e49 | -6.6505 | -43.7284 | 2026-10-08 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f266b419-e97d-3440-b1c0-14ca41cef5bf | -5.7117 | -53.4862 | 2026-10-08 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| efedfd56-ecef-3d5a-aa15-54a75202e878 | -2.517 | -56.1656 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5eca285b-9b0e-34c8-b623-132612133daf | -10.4151 | -47.2623 | 2026-10-08 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1316519e-9642-34c0-a468-3ca98cec934b | -2.4988 | -56.1266 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| df2cb9b5-215c-318a-8376-4bcd41a065bf | -8.7231 | -45.1583 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| f444a73f-0bd2-381f-b8ea-6ca76a649fca | -5.372 | -44.1751 | 2026-10-08 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e01ca572-fa4f-3f79-b69d-e5adb5660253 | -3.1285 | -54.1657 | 2026-10-08 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3827b567-256c-3895-8923-82d82c1430f6 | -16.8642 | -40.5709 | 2026-10-08 02:10:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| 9c33dac9-13d2-3d24-bf9d-e2d6ed155e87 | -2.4988 | -56.1462 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f9945a6c-5b91-354b-a595-3cb0344f47ff | -8.7417 | -45.1791 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 462461ed-db2a-348d-af3a-9c1faad35208 | -3.1101 | -54.1661 | 2026-10-08 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 89ce2e12-41b5-3fe8-9b19-debb70d835e2 | -8.7234 | -45.1355 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b9fddba2-f0e7-3aed-ae1c-ef3028f611f6 | -3.073 | -54.2874 | 2026-10-08 02:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5159a94f-f4f6-3a60-91a4-06a7636a8f6a | -3.478 | -59.5779 | 2026-10-08 02:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 305f7971-14bd-3182-9b5a-50a5418affe7 | -2.7796 | -54.0937 | 2026-10-08 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d361f9f0-c0c7-3314-99b8-bf8d648e372e | -3.0741 | -53.946 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 3f028abe-c43b-39ca-bdbb-4c51eb4614e6 | -2.4805 | -56.1269 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 19cb7eba-ac49-35fc-98c4-68ff91199cd1 | -2.572 | -56.1646 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| def61fe6-e1bc-3c51-bae5-ab8d7cb67d34 | -10.4337 | -47.2824 | 2026-10-08 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4cb00cb8-0a69-36b3-9df7-a27dd9110d9f | -3.5515 | -59.4807 | 2026-10-08 02:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 47ceef4b-6a61-3fca-9d72-01f089d482fc | -3.1697 | -58.6437 | 2026-10-08 02:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 3b6fa77a-6187-3c44-9e12-0035dce079c9 | -9.4749 | -64.3713 | 2026-10-08 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2c4dc7b5-3c0a-3bbf-8cf8-c4353832fa2e | -3.11 | -54.1862 | 2026-10-08 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0309c809-486f-31a2-a3f9-379c029dbaa6 | -2.4987 | -56.1659 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3e8bae3a-73d3-3435-abf6-641b4d483a8a | -8.6107 | -67.0301 | 2026-10-08 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9a25f327-5fd4-3b83-bc09-c42d01c39932 | -2.7797 | -54.0736 | 2026-10-08 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 86259dd6-888c-3a59-8ce5-671fdf2765eb | -5.7116 | -53.5065 | 2026-10-08 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 05fb6a39-4b0c-330e-bb0f-6cb80e5bc1c8 | -8.73 | -45.15 | 2026-10-08 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab6e398-ed07-3d92-975b-8e94ce83c0eb | -3.02 | -54.05 | 2026-10-08 02:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd0d143-beda-3c8b-ad33-0abeffd3d077 | -3.02 | -54.11 | 2026-10-08 02:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f62e7902-c3af-36e4-8c44-0dfe923ec5e5 | -8.73 | -45.2 | 2026-10-08 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca9fd8ab-be7e-3fd9-a479-f6f5ed0bdb31 | -3.0 | -54.04 | 2026-10-08 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc16090d-ab94-3318-b94b-4e8514926005 | -8.7 | -45.19 | 2026-10-08 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7055de1-5991-3adf-b368-81b60f6d3377 | -3.0 | -54.11 | 2026-10-08 02:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a80f7f-7404-3805-b30b-7651a24802e8 | -5.7117 | -53.4862 | 2026-10-08 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c803f5f2-6228-3522-be6f-fa81fe344d22 | -5.7116 | -53.5065 | 2026-10-08 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0049ed9a-91e4-35d2-ba6a-cc99038c22e5 | -6.1431 | -47.9214 | 2026-10-08 02:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 99e0971b-dcd3-3be0-8c5e-373c39013dbf | -6.6505 | -43.7284 | 2026-10-08 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a77727ec-30da-3974-a88f-4a07baf58b02 | -2.4987 | -56.1659 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b2f67c0f-f900-3f2a-bf38-b4f7dd1e1653 | -4.3473 | -43.779 | 2026-10-08 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c005abea-51ae-3fee-b9d0-9dcecd7bf192 | -6.1615 | -47.9419 | 2026-10-08 02:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2dcac8df-dad6-37f4-aef8-866cfa5d0e78 | -8.5184 | -66.9954 | 2026-10-08 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fc618e6b-5a52-30e4-aabb-fe61846563fa | -3.5698 | -59.4803 | 2026-10-08 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| b8ea0e4f-80c7-3f56-b45e-2f871a9aeb1c | -8.7231 | -45.1583 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 32579075-fc6a-35bb-9519-2fd280dd41cd | -3.019 | -53.9272 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5f7f54fa-bf93-3336-b61c-fe914f33dedd | -5.7376 | -45.1533 | 2026-10-08 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8a880b16-580c-3128-bc12-ea8160bb89e3 | -2.7797 | -54.0736 | 2026-10-08 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e8ad0af6-e502-3a88-a196-5b37311ce9ac | -6.988 | -59.123 | 2026-10-08 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d02cc1a5-3573-3ab8-aa7e-6ac7962432e8 | -4.3471 | -43.8021 | 2026-10-08 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 81faf628-40ed-3e40-acef-2780af9e552c | -5.6932 | -53.487 | 2026-10-08 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| e418f113-7391-3d52-8fb7-f969648b27ca | -9.4749 | -64.3713 | 2026-10-08 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 876b3d5e-71ec-383d-b013-71060c4d51fd | -3.478 | -59.5779 | 2026-10-08 02:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e86d6772-2583-33e4-b711-e8b132115a2d | -3.0741 | -53.946 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1431eb0e-b39d-3a4e-990e-3503d1e5c1f0 | -2.3848 | -57.9044 | 2026-10-08 02:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 04b6453d-1072-352d-9ae5-018bfc3621b7 | -3.0374 | -53.9268 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 42585dce-61f8-3d03-9c56-551de89b4796 | -8.7423 | -45.1334 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 20c580b5-93e0-378a-a956-50b8a2230d99 | -3.1115 | -53.7637 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 716b9dbc-829d-3b71-87d0-b8e36a1f9498 | -3.11 | -54.1862 | 2026-10-08 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4d53f3b9-9728-3765-a9d2-093def59ebf1 | -2.8575 | -59.1107 | 2026-10-08 02:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 598cd2e0-0d74-3cef-be32-70757766e1e6 | -4.1176 | -59.8888 | 2026-10-08 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b7ff679a-97ab-3852-8e11-5fc5b1121d93 | -3.0925 | -53.9455 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f96a3fa1-b855-398d-8b8e-7e0f4dee924c | -9.4936 | -64.3518 | 2026-10-08 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 23fe4937-5f40-3624-8a36-c278c48f6fea | -2.572 | -56.1646 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d418cfdf-1927-3a25-866e-fe0830602645 | -3.8567 | -55.9769 | 2026-10-08 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 458044dc-1e52-3f90-89e3-d601915cd323 | -10.4151 | -47.2623 | 2026-10-08 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c3c822e9-cb14-33c9-82e3-dfe0310bff7c | -3.1114 | -53.7839 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 3de5f986-1575-3a2b-a109-f90ba143cc27 | -7.0065 | -59.1223 | 2026-10-08 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| aedf1cc2-8414-310e-b457-ca87dc6a402e | -8.7228 | -45.1812 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 0e19f6e1-bdda-3344-bd4e-438e1c974d1b | -2.4805 | -56.1269 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b7aa954e-9585-3c70-ac62-630dea2736bd | -2.572 | -56.1842 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 64a31f9d-ab1e-3135-a053-d74ed23c9c2b | -2.3849 | -57.885 | 2026-10-08 02:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 73a5ae3c-8bb4-39ae-b871-749c210362fb | -6.6319 | -43.7068 | 2026-10-08 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0f8ee308-d941-3cfe-8c94-02e5a92ce501 | -3.1285 | -54.1657 | 2026-10-08 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b6d69e6f-9dc6-3d76-aff1-be13d5ed0326 | -3.1101 | -54.1661 | 2026-10-08 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 0ecf90a6-83bf-3f77-86a0-8f4652a5e481 | -1.5306 | -54.5558 | 2026-10-08 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b4cae6b1-589d-3ad9-8376-67be85d57a63 | -3.1114 | -53.8041 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a3fad833-9790-3216-a1c8-ddb3d1bcf3f2 | -2.4805 | -56.1072 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9d8a04cf-e5ec-3a7c-b529-6cb90dc56695 | -8.742 | -45.1563 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 221.6 |
| e8329ae3-93d8-3bac-bffa-7011a2bbceb8 | -6.1617 | -47.9201 | 2026-10-08 02:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3eb087fc-c66c-30bd-9be6-5ef4fe0b7502 | -10.4337 | -47.2824 | 2026-10-08 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3f2dadc5-46bc-3c31-9736-68f639071c4b | -8.537 | -66.9764 | 2026-10-08 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| eaf0b945-d089-30be-aa6e-51fbfc280764 | -3.0913 | -54.287 | 2026-10-08 02:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6a47e499-1225-381a-9214-f53d272602d0 | -2.4988 | -56.1266 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |


[Clique aqui para ver as próximas entradas](README51.md)
