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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 168ec1f9-d42a-3c25-8921-61900c6b6b3c | -8.51497 | -63.8736 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8924769-f267-31d8-8668-f1c5eca0abc9 | -10.70771 | -47.14619 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 175827c5-69a0-302f-9c7c-f10908135b9e | -6.35894 | -57.9677 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98c1abb7-d9a2-3999-9044-92ae9f9e1822 | -9.51275 | -60.51223 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2627b5e9-1bb7-352d-be68-d229eadae4a0 | -8.2109 | -61.41737 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7067a0bb-060b-3fae-a141-f7ab7826a638 | -9.23209 | -60.92577 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdec3ef8-8385-32b4-a1b2-012e1858e71e | -10.71641 | -47.12226 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6eac58b-4c9f-3a1d-b668-0c3b684d22d7 | -7.65692 | -63.51666 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25b2aac-eecc-3c37-95d8-d0bd125626db | -9.20237 | -59.50404 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b315bab-003f-37cd-a957-c4a08119ca68 | -12.93737 | -46.3092 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 529127fc-2958-3325-bb58-99645ee5633a | -9.10228 | -61.42966 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11a1de6d-4f08-3e75-a8fb-6ef522bef0a6 | -8.61276 | -62.60859 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1e4ee78-b4ec-37aa-adc9-12adbc92a2a2 | -8.9047 | -62.46044 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2479f76-066c-3dde-99a9-3c75def7f597 | -7.47176 | -45.01696 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 766bec87-0259-3e90-bfda-34a39788219b | -12.93694 | -46.31285 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d71150e-95e2-30c4-8c00-77bd54d26f11 | -5.74548 | -57.57613 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1cf8b76-5774-3060-ba65-43ede9825549 | -7.58404 | -45.23278 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da55269-4517-306a-b24b-c41b7f21267a | -9.07185 | -65.72005 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82b2ecf2-c206-306d-b755-7be833d0793e | -5.80518 | -59.21682 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1765e428-9047-39c6-912c-710845ec8b62 | -8.89899 | -62.46785 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82a5e4a0-6640-3ef5-b20a-cfc8cd26a033 | -11.20078 | -48.46581 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80c86984-b19f-318e-8540-8d43cbbea427 | -12.99226 | -45.22195 | 2025-08-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35929344-63c6-362b-9c76-a242a7b689f2 | -7.59356 | -46.24597 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b95f3b4e-bc56-34e4-a104-32c5f4aa9353 | -9.20302 | -60.78419 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7f50c1d-1e3a-3b26-b751-6a1e959b43f5 | -8.12364 | -62.87941 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2cabdccf-8a05-32c1-a7d5-6fa603b45753 | -6.93433 | -59.5557 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f5a7194-0d0e-33dd-b7b8-d6ebe98e64ee | -8.91035 | -62.42775 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 005655d5-f7fc-34a6-ac07-2515cb5e46cf | -10.41821 | -64.43652 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f34d042f-5b19-3068-955c-7a22826a3f6c | -9.51572 | -60.51748 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe00e784-7307-363f-b923-f6d44bf3a83f | -9.23292 | -60.9209 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db7837c6-e0b0-3588-bf4c-a2b18cd27b90 | -11.47493 | -55.47178 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ede8cba9-4160-3993-ab28-ce252f4394c2 | -7.28714 | -44.47385 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c3f9a16-d669-3873-89b0-2be58fe03f2a | -5.42456 | -60.16729 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fadb004-6224-3045-b643-61b82712a924 | -7.54699 | -63.86479 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cb3c2ec-ada9-3721-86da-3445bfd38bb3 | -8.90965 | -62.43183 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66b1c486-6967-32c0-b212-8bbcc7a24b1c | -9.00599 | -65.40183 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1be94aa-a035-36bf-b6d0-30e795f84682 | -5.75171 | -57.58091 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56833fed-e03c-3a0d-bfda-72646624dfe2 | -9.00256 | -65.3912 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93dfd566-2bf0-335f-af3c-82a542295283 | -9.21821 | -59.70643 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 950044a8-2b3b-374f-a6e2-ba3afb32e20b | -10.61151 | -55.05312 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b48354da-3339-3368-966b-7ea9e4d4ba5b | -9.18772 | -59.45926 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df4e6bdf-a5a9-324a-b525-728860578c6a | -9.57329 | -55.36871 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13a45746-107c-384d-9a3d-9494f834581c | -10.61095 | -55.05682 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 83c3bf4d-bb8c-3f89-8acf-946fd30a5270 | -7.49591 | -63.82181 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f51efa2-7ec0-354f-b9ec-3b79224304ab | -8.59571 | -62.5979 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a8e311e-3f6b-3892-8b9e-7c641405853a | -6.83427 | -58.95848 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5f69d846-9fa0-3020-a373-7ae7d7ac42fe | -7.52564 | -63.8172 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30be56cf-9fa1-37f6-b292-5c3a9386d3ed | -6.02871 | -44.22206 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8785240-32c7-3e18-88e5-6360e16d41f0 | -9.96257 | -60.1879 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7f3cc5d-66e6-3843-92b2-a05bfb2c5f66 | -9.25343 | -60.48352 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42ec3b3f-19b8-32ba-abf7-83afb2dcd906 | -7.65606 | -63.52168 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba7f4f6-3b35-3b13-a2f6-74769eacee83 | -8.07661 | -61.54341 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d8c67e-2045-39d4-88b9-b4ffd00654f8 | -7.55756 | -63.86125 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ecee74c-8822-37b9-833b-863e3782901c | -9.21116 | -60.92513 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9249a6ca-1dce-3291-b80b-1383a73936ee | -12.99018 | -45.22842 | 2025-08-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 954e2a4f-f566-335e-81f2-b18a2a92f828 | -12.75339 | -44.42327 | 2025-08-25 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02f2c949-006a-3f80-a699-e5791565dbaf | -8.90681 | -62.4482 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49db11f-c03b-3595-a990-5c8ed6120195 | -8.22709 | -61.42018 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20f2a412-a806-3ce7-ab06-c6b66ce6bd42 | -8.0705 | -49.67266 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f3bc45-5733-3fe6-8c56-1dd6ecfba60b | -7.9088 | -45.88825 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b1fa419-e05c-3e1e-b7b2-a7083a41f243 | -6.4975 | -49.9105 | 2025-08-25 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc64f096-f4fe-36e4-bca5-decb2a0b74ad | -6.79518 | -58.64651 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1d65fb1-023d-33b9-a2c2-1a726292cce1 | -9.17633 | -59.46158 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7350c353-5f47-3b6d-beb3-6bd46e494453 | -11.93221 | -46.72416 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0a8334e-d5dd-34ed-902e-d44ebdda0270 | -11.2726 | -44.97051 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d31dcc38-24c0-3270-9e4b-2b86214bc0c9 | -8.8747 | -62.45509 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5cbbba0d-21e3-354e-b4ec-3ea31907a4ea | -7.35577 | -57.63538 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4505896c-a566-34a2-be1f-d57c2449f377 | -9.01818 | -65.39419 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7a2836-699b-382c-a90b-c257b98e0376 | -12.73434 | -48.14234 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b278f7d4-285a-34d0-8e78-5c2c874b0ee2 | -4.70414 | -56.06335 | 2025-08-25 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce2545f-04d5-3aef-884c-4a22b6eebf2a | -9.17188 | -60.8282 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83e2a159-51fe-3a58-b96d-624ef9ee81c8 | -9.81471 | -64.26064 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acb9f8cc-96d0-3047-b1bb-970f5bdd80f6 | -8.10577 | -62.87623 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6f2a526b-fb3f-35ac-8454-d74e0310eefa | -10.88689 | -55.78918 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb67060e-6470-35f3-baa3-816c4512f767 | -6.83495 | -58.95439 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 85392467-b387-3355-b0bc-745928dd58f1 | -9.21388 | -59.71004 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5237a48a-c41d-3ef3-bd77-90b22d6bb179 | -9.51695 | -60.55563 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bfc28b5-b7f6-3e2d-ae58-23780cd787dc | -9.20685 | -60.78486 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47adac62-9951-378a-80b3-8aac7d1053c2 | -8.6063 | -62.59441 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bf7872c-9f5a-3137-a19e-d8addc6be7fe | -9.17174 | -59.62255 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c44d939a-3184-38ca-b006-9f6b32380345 | -5.43166 | -60.17152 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2c7b267f-14ea-3b64-8588-e077f8078631 | -6.7987 | -58.64712 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fc3601-c7bf-3bff-86b9-ea2441772c7b | -11.60736 | -46.23706 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb88e724-cc27-3f07-b132-0f0a507729da | -7.91508 | -45.88511 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc201e19-0ac3-358a-81e5-b5ae31bf18ae | -9.20688 | -59.61126 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f0527e-cfbb-3be0-b4ae-33ec54d3468b | -8.88396 | -62.40219 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b2d3c3-d625-3a06-bf8b-305697f05d40 | -6.79936 | -58.64314 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c72c587-5175-3f51-87ff-2c8cb23041d3 | -5.75051 | -57.58829 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4d89a7-55e6-347d-b496-2ea491dc6a60 | -10.41152 | -64.41894 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b898cb0-2499-3401-9abd-074fdc1bc589 | -12.9908 | -45.22312 | 2025-08-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 680b6728-a95a-3608-aa08-acd7e48c64f0 | -9.20605 | -60.78965 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce73ee23-805f-3394-95b5-8b557548dd0f | -9.81403 | -64.26351 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7665b7e6-c739-374a-b706-82af11c6f42f | -6.62715 | -58.54338 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eec12e12-75cc-3ffe-9cec-e026d609f4b5 | -8.22364 | -61.41594 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a32a09-47e3-3169-902f-aedf2a319fd2 | -8.59085 | -62.63086 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bb062c6-676e-3d38-84d5-c97af4c8581f | -9.57664 | -55.36924 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02440d3a-95a0-38df-8add-21564b07a5a6 | -9.64479 | -59.63702 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 713bfd6e-495b-3318-8a36-56b83b6053c8 | -9.52245 | -60.52337 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b45c0841-b9a6-3e10-858c-9a7c6e59a2cd | -9.19112 | -59.43879 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c1ebb8c-ddc8-3828-9501-e1c023fc2770 | -9.19044 | -59.62133 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README59.md)
