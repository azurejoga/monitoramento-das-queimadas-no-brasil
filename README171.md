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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aeea45fd-0b7d-3480-a4ad-87ac92ff1f58 | -7.8233 | -72.8236 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 75.3 |
| facb4222-48e3-3036-85e2-0d204b36885e | -5.5066 | -43.7503 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cff9767d-b3f7-3e4c-8f11-9300d9631cf5 | -9.6672 | -66.834 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4a7b1a28-8c64-3932-ae6d-8065360d7b98 | -9.1626 | -67.8498 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6966a8f1-33b3-3bc2-a950-22352ed1e83a | -7.8232 | -72.86 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 84.8 |
| c943b7da-dac5-3af5-b655-ce2b1e682d99 | -9.1075 | -67.7401 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| bb9dda8e-64e5-3e91-b8e9-202c319c6c04 | -8.6115 | -66.8076 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 8a8127f1-3e36-3d81-a75a-96850adb8720 | -7.2537 | -45.2582 | 2026-10-05 20:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 21a1c264-0f42-3048-8fd2-d1fe0731b477 | -5.8094 | -43.4025 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 457.5 |
| 708aa906-2971-3d43-9189-424b38802df4 | -9.1257 | -67.8137 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fb57d9be-051e-35f9-b103-c0906476e595 | -7.9152 | -72.9324 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a30d74e1-6cc5-361e-af24-b811a1516f07 | -8.8519 | -66.8012 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 23684ed8-74f4-3019-ae8a-0a7287e04b08 | -13.5197 | -61.1319 | 2026-10-05 20:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6c6f2f15-f784-3970-a087-d5bc1be6d63b | -9.1055 | -68.3135 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| fb343f51-89e4-3822-ad30-ab4befadcdbc | -6.4547 | -40.9178 | 2026-10-05 20:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| 7154fc5b-d2c5-3378-bb14-306c76f5feca | -5.5612 | -43.9313 | 2026-10-05 20:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| dc9e05ea-1718-3129-8db7-bc0f1358ebe5 | -2.5353 | -65.8819 | 2026-10-05 20:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 56a00ddd-c092-33d6-9db8-7e75803303af | -5.8096 | -43.3791 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4b3cef72-77d4-372d-8ef5-f94c4282c813 | -9.4435 | -67.1008 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| f8c821cc-8b1e-357b-9db5-16215b474d29 | -5.8282 | -43.401 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 262.3 |
| e37775b5-171b-34fb-9dc5-70a0be34d003 | -5.8092 | -43.4258 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 368.3 |
| 03372c52-2c27-3503-8b0a-9afcd326b57c | -5.5797 | -43.953 | 2026-10-05 20:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7c561eed-e71f-301e-88b7-5f3a37aa4cdf | -6.7199 | -44.2771 | 2026-10-05 20:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 1b260784-99b0-39ab-9bf4-d99f2db2b2e3 | -8.882 | -68.7981 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 7101ba94-d109-3f3a-b4a4-3fc180a08fe2 | -6.1894 | -44.8472 | 2026-10-05 20:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 152e57ab-8bb5-3fbe-9ad4-f5b5657d5fcd | -7.8232 | -72.8418 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e1a7beb3-da18-3293-8905-48302914fb75 | -8.6483 | -66.8437 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 5a0e348e-462a-331c-b51c-8e259f70d402 | -9.3431 | -64.7143 | 2026-10-05 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 129297e2-bd73-33ec-89de-4bd5924d92b5 | -8.9688 | -65.4385 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 6cbbaaad-a38c-3df4-8729-d507a829054d | -5.8321 | -45.0332 | 2026-10-05 20:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5607abf6-10b4-3479-8737-d93c160f36bf | -4.3668 | -43.6623 | 2026-10-05 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 0668751e-371e-3710-bd36-e51d5ec6399e | -9.6673 | -66.8154 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 288d11ab-4584-3203-a73d-a85d4209641a | -8.593 | -66.8081 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| b54d8c31-fbec-32be-9934-d8b733ca4a9e | -6.237 | -43.7866 | 2026-10-05 20:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 193.5 |
| b02ba4a9-c310-38fd-8eb5-7aaf3631e848 | -8.537 | -66.9764 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 69b16828-8a16-3886-b6c1-e529963493d8 | -9.0892 | -67.685 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 3d7e3aab-ab44-373c-8a9d-140b4a4489bf | -9.5424 | -65.7002 | 2026-10-05 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 54d29791-6665-3e1f-afa5-ef3a2003c3d1 | -9.1426 | -68.2941 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7ed68fbb-980d-38bc-96f6-7219a6c0ac40 | -9.1077 | -67.6845 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 0a7a2163-325d-3886-9756-940a2a0ea7d0 | -6.4356 | -40.944 | 2026-10-05 20:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| 53948fbd-86cc-33f1-b97e-f49cdc4ff388 | -9.1257 | -67.8322 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0446f3d9-97f0-34d0-9b3c-147263827067 | -7.8969 | -72.8049 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 8d093ba4-5775-3d89-a685-8099cbe33d96 | -9.96 | -43.481 | 2026-10-05 20:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b0cf95bc-27aa-3408-ace9-e75394a4a8a7 | -5.828 | -43.4243 | 2026-10-05 20:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 83b6bdfb-5dc4-3cb0-a4c0-36c7ed492f4b | -9.1074 | -67.7586 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 1f9fc463-7c3b-3ca7-b974-62b95f9e97c2 | -8.8265 | -64.2258 | 2026-10-05 20:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 8b5ab85e-5c6e-3282-83b0-86ec04975d74 | -5.3605 | -43.3194 | 2026-10-05 20:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| eed0da9c-3e82-3c58-a44b-41fdbf8ce238 | -7.2349 | -45.2599 | 2026-10-05 20:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d69ca891-45e6-3cc7-9468-71309d63db28 | -8.9293 | -72.8344 | 2026-10-05 20:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 15375a37-ae21-357b-acd4-607ace7c0c70 | -8.852 | -66.7827 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 2da95993-13b4-3e00-91c1-80de4e0aaa0e | -9.0892 | -67.6665 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1049cccb-f72b-31ac-8349-c171c3da72e7 | -5.8323 | -45.0105 | 2026-10-05 20:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 61ce3fdf-f623-34a8-a800-d096c639c279 | -6.17 | -39.3388 | 2026-10-05 20:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 295c4529-d165-304d-8cc4-1fbfa4deafd6 | -6.4545 | -40.9422 | 2026-10-05 20:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| aaaf2490-de7e-33de-b724-0d396c568f57 | 2.4769 | -50.8294 | 2026-10-05 20:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 003f797e-7733-3191-a86f-3326de299cff | -5.3418 | -43.3207 | 2026-10-05 20:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| ab168b9b-d96f-38ba-956d-6589d5d7fb94 | -8.9478 | -72.8526 | 2026-10-05 20:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 68b53d51-5070-3042-9c48-5f2f185692bb | -9.7126 | -65.0951 | 2026-10-05 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.3 |
| f1e0775b-3079-37b8-94ca-9131ef75dae2 | -6.8952 | -43.6833 | 2026-10-05 20:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 174a027c-9cf8-3ee5-8186-3420a358e2bb | -7.3825 | -72.4621 | 2026-10-05 20:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 52af81c8-7e26-306f-b7d0-52bba53f48a4 | -8.882 | -68.8166 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3b1fc44c-bcc5-3f7a-b7e4-2a456d8a6bd8 | -8.6483 | -66.8623 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 410f3482-f6dc-38b4-a916-f7c43de77c4e | -9.5425 | -65.6815 | 2026-10-05 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| a012222f-266f-31e5-89c7-5a504517f1ce | -7.8785 | -72.805 | 2026-10-05 20:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 3cb3eead-eb0d-3464-a2b9-131ac3a7eac6 | -7.3641 | -72.4622 | 2026-10-05 20:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 7d342cb3-6781-3d9e-86c0-6200b262e3c4 | -6.173 | -44.5974 | 2026-10-05 20:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ab67f8b5-9d47-3214-9f7d-2456228b701f | -9.1259 | -67.7581 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| da6522be-a7b8-3da8-bd03-cb7118949a1c | -6.2372 | -43.7634 | 2026-10-05 20:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e96f44fd-3a8a-3b5f-ba21-5eaff35c97ca | -10.2827 | -60.5432 | 2026-10-05 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| f635c4fe-6aa9-3796-8f86-44c67ca1ce3b | -10.2563 | -68.2673 | 2026-10-05 20:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 41757506-56dd-36ad-95d8-46e942f0bd21 | -9.7312 | -65.0944 | 2026-10-05 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 8a4ac9b1-7b09-37dc-9bef-6f3720cdf7df | -9.1055 | -68.3135 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 219.3 |
| 9882b6bf-61ca-3fc3-ad8e-76aea7927051 | -7.8049 | -72.8419 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 192.9 |
| c78163ed-b343-3072-adde-984007402b27 | -8.6483 | -66.8623 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 77afe55b-0236-385f-91f4-6db62eee1aed | -6.256 | -43.7619 | 2026-10-05 20:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 15b4ebd6-5ac0-351c-98ff-4e0c48827a2f | -10.534 | -68.7055 | 2026-10-05 20:30:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 51198f7f-0767-344f-80c3-511f64b1ee50 | -9.1072 | -67.8141 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 82f0f484-b0d3-38a7-b1bc-b644f7afab3e | -8.5971 | -72.7271 | 2026-10-05 20:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 0a870ee0-eb89-340b-99d7-bdb9d6e42b76 | -5.8282 | -43.401 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 482.8 |
| fb0c21b9-1681-34de-bc20-774aedf8faf2 | -9.5424 | -65.7002 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| c2340c64-c219-3153-8a25-e099112197fd | -6.8952 | -43.6833 | 2026-10-05 20:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| dea311ce-2559-35ce-abb8-f2321987b089 | -8.9687 | -65.4572 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3d056284-98fe-3894-a5f8-2110c19eba1a | -8.6115 | -66.8076 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b93b25b5-e981-3a2b-9ad0-acfc5c7cad5f | -8.8519 | -66.8012 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| ec657114-d926-36d3-be3b-4c2cd6a1c042 | -5.8094 | -43.4025 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 374.4 |
| b9e2be40-4f68-3909-a800-553e99edc851 | -6.6683 | -43.8196 | 2026-10-05 20:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9c229984-a835-312f-be3c-3d56082aa675 | -9.1428 | -68.2387 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 30d55852-2b67-3ded-86c2-4380a7d6c66b | -5.5612 | -43.9313 | 2026-10-05 20:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| eeba1a86-88f8-32f3-ae0a-7150f7ea9558 | -8.9873 | -65.4379 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 126.4 |
| b2bceae4-b9ad-32b1-8e53-c0ccd4ca2904 | -9.124 | -68.313 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 854d388e-27c0-3113-aff1-ec2426336ed6 | -7.8416 | -72.9328 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 539d674d-532d-34d9-be9a-5722c7ce30d2 | -6.4545 | -40.9422 | 2026-10-05 20:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 200.8 |
| cc136877-b5e4-3f5b-ba52-f142d02b67aa | -8.5184 | -66.9954 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 00e540e9-f13c-3c04-b293-bbb402707d8f | -8.9688 | -65.4385 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 0a238e38-4541-35e5-b4b0-00a99d107940 | -9.1074 | -67.7586 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b7e990e8-10a8-391f-92c9-67d2c4f9cc27 | -8.4169 | -70.1119 | 2026-10-05 20:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 331fdb73-87e3-3fd5-8260-f8d521567550 | -9.1078 | -67.666 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0e391f51-8ddb-3f55-8644-da77383f1026 | -7.2721 | -72.6631 | 2026-10-05 20:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 40bbeb22-b1a2-3823-aa74-b739adfe33d1 | -9.4435 | -67.1008 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1a1d0951-5072-39ff-b3d9-d3ae9a272a5c | -6.4547 | -40.9178 | 2026-10-05 20:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |


[Clique aqui para ver as próximas entradas](README172.md)
