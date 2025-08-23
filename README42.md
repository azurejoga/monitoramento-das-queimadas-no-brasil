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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2862678-d5df-3df7-8399-047cc5cacff8 | -6.43914 | -53.38583 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e86a536a-752b-38f7-b62f-4fa8539f36a1 | -8.30519 | -47.26194 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 817b909a-35b9-3a31-93ca-75a44332d6a1 | -7.80885 | -63.55483 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 116f5747-20fb-3d23-8171-768abc66a059 | -6.78352 | -44.32349 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d558e672-f6db-313e-9349-e843ea64a1fa | -8.84891 | -49.86225 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b40785c0-095f-33a5-b5be-119d0bb195c6 | -9.61164 | -55.35808 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b5bd54c-0623-3d14-bbcd-3034969b1dc0 | -9.18729 | -59.63211 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97a9631c-fec9-30ec-bd05-715a257c2e45 | -4.06908 | -49.45583 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 256d9678-ce43-3030-87a1-205186fb8325 | -6.47678 | -55.884 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6414fd2-ab7f-3b2c-a4f4-efccdc9c8793 | -6.94203 | -59.64321 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dddff42-30a2-32f8-b84c-af32ec9073de | -6.56374 | -60.0613 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcd57a7e-5307-3784-a05b-1c88b1925159 | -4.23397 | -54.92375 | 2025-08-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70281a32-2d61-3d27-8014-f22aed439223 | -6.43804 | -53.39277 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8a8cdae-40a4-3029-b556-f1e6e57a42d0 | -6.92838 | -62.89252 | 2025-08-23 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3bd5d7e-838f-3992-a02f-3ed0c42d5d7c | -9.53073 | -48.13247 | 2025-08-23 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cf1e85b-e364-3123-bd00-ecc9f0945e4f | -9.60763 | -55.36126 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec678c5-61e2-36c5-b676-23f5696d1d87 | -9.18518 | -59.64455 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cb2d4fb-9303-358b-b2d4-cec413399be3 | -6.60723 | -44.56916 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1cc60d53-a3ce-3318-aeac-ac64872ef6fc | -6.25537 | -53.68626 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9cfc37b-a090-39b9-9464-3d2fa9398e9f | -10.74447 | -48.25053 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43c8ec8f-a0f6-39ce-b816-3b7e081e49b7 | -9.18154 | -59.63974 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6590d06e-c649-30da-a67e-3fe0e5eee6d3 | -7.07123 | -44.61402 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f0253ad-e800-3711-9637-8a027884094a | -8.52975 | -48.83446 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64125010-bbd7-3fab-b208-37317acdfe5d | -6.73021 | -51.97916 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2a4297f-b6ee-3c39-adb0-9189c7495da7 | -7.18519 | -48.42817 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7edab1cc-2e79-3e96-97df-85cd1a4a665d | -9.21303 | -59.47056 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f919e632-502f-33e8-a742-6b74d623b2d0 | -7.03852 | -44.66643 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8bec072-eae0-32f3-a4d9-1e964f692268 | -8.9966 | -56.34087 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04abbc08-f3f0-3c94-8df3-ff82bd55a39d | -5.88304 | -57.75256 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b2f2934-9959-35b7-9e5f-ed08c222c6b0 | -10.47531 | -46.82128 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eaba0c6-a19f-3766-8a2a-db3a9beca85e | -7.10353 | -59.77601 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7d3c4697-2e37-31a9-92d5-694b2e2fb6d2 | -9.20665 | -59.4568 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95b0608f-397d-3b04-8fd6-c2f44c6c1e48 | -2.85616 | -54.89663 | 2025-08-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36337f84-9cf7-3017-81ac-917fd92b38a1 | -3.28127 | -48.80966 | 2025-08-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5030f0f6-2e9e-378d-b018-3650e3eccb74 | -6.57599 | -59.87865 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ebe5f9d-1d88-3379-99bd-37ccb4f160dd | -9.16991 | -59.60339 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6227959a-5419-3579-9f02-0f1420d77541 | -8.65611 | -51.27386 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f85958-5167-353f-9449-5100dcba632f | -3.78163 | -55.96345 | 2025-08-23 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febab778-342c-3cd1-9158-c5474df64a5d | -11.13831 | -44.74649 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 315b186e-dd11-3f2a-8b4b-761957ea3aed | -6.61267 | -44.56693 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5abaf91a-c15a-3eae-8254-57c60c3e9609 | -9.19015 | -59.6153 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5a32b56c-ca49-3ac0-aa75-c63dbb9f46b8 | -5.23902 | -56.06243 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f09184a9-6077-3c9d-8f13-3c1490a3dbda | -6.62549 | -58.54261 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5274679-6bd7-33f0-a109-962be962997f | -4.07256 | -49.45514 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056e72ba-f460-3070-85b8-244cbffecb95 | -9.21465 | -59.47087 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da020fea-22f9-3b12-9ccb-371a937dcc2c | -8.53331 | -48.86493 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8a859ba-b307-3d19-9f03-80b7556af324 | -6.45847 | -53.39242 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d907b9-4ca1-3a7b-8e0d-7640f578ff9f | -9.55365 | -47.93895 | 2025-08-23 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d438be9-a34e-3bbe-a1bd-466cf4e9fa07 | -4.08116 | -48.03922 | 2025-08-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83e1388f-38dc-3169-87d4-3749a790c0a1 | -6.05267 | -44.36569 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2045f569-b099-3c5c-bae2-d808fe9546dd | -8.30038 | -47.26522 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72e90f0b-1b47-32cd-862c-28e4bddf8480 | -7.62244 | -44.37006 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b13e69b8-2941-3633-81fa-e5b96d180162 | -6.05776 | -53.88246 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 042287b5-b6f4-3988-8966-d61fbe5eabde | -5.87722 | -57.76278 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2168671f-78b3-3edb-adf6-c155f4588cda | -5.74842 | -57.6106 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b07b88f-27d1-35a2-af0f-000f8c340182 | -6.39393 | -45.51149 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 546b7a47-edfc-31c4-9109-95e6368b5758 | -7.15048 | -44.67207 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e9d9b5-405a-3b98-9104-b57d8e1e9ae2 | -10.70728 | -48.21355 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ddba30-c0b9-3b63-98d3-d3270ef46e88 | -9.17566 | -59.65579 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f401f9d-c8be-3c24-898c-98c652dda9b3 | -9.16197 | -59.59774 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ed9d0aa-2b76-350c-8b93-21a3b6286f5c | -6.06223 | -53.87589 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e8c175-8093-3be3-9626-908bd1dacdde | -7.03926 | -44.66093 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2268d4e-7a2d-3b73-bbff-9f0af5c2fe55 | -6.39108 | -45.5135 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a9ab1222-8e72-30d1-806f-e7a9c6022c65 | -5.88937 | -53.63526 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51c2c243-9018-3c42-8472-51977255fc2b | -9.20981 | -59.61424 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0181bce0-81ea-39ee-b2eb-2b07bbc2f179 | -9.18744 | -59.6147 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3e0579e3-86bf-32c8-bccb-59a5b5664893 | -8.61746 | -62.63128 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57aa0865-9584-3a74-a3cb-411a2ef4fb54 | -4.32718 | -55.13345 | 2025-08-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dabe923-aa7c-37e9-9133-83d60b49af5b | -5.74437 | -52.32742 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 490b060b-bb71-3e43-bbb8-37bfc2605d5d | -6.60486 | -57.64161 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5a84e9f-7a63-36de-b826-1de76164ece3 | -8.84964 | -52.0533 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e499aa-3f1b-3b45-b632-0972144252d0 | -6.11864 | -44.40349 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95a69010-65d7-3a09-84b9-bab62485623c | -4.14804 | -46.45871 | 2025-08-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8261a22-62e8-3855-a711-49b8785bdfcd | -9.20321 | -59.46035 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c919b8b6-1673-3274-bcd7-24f8616d2eea | -5.79723 | -59.22351 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 564d50c1-b630-3e86-a146-f60e95ec278d | -7.61122 | -44.37499 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a5a53e9-e560-3217-ba6d-07b1007de5ed | -7.31389 | -59.61404 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf9602b6-27d4-33d3-a6f5-d1cc03015dd9 | -3.84176 | -47.41214 | 2025-08-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61966608-8d40-3929-8889-8048e2f64154 | -9.17135 | -59.59499 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea7a7330-925e-33aa-a6c1-e04fa8cc7061 | -9.61043 | -55.36554 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cbd010a-3112-35f3-b4eb-e9edd93e1654 | -9.16846 | -59.58587 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dd3423b-7400-3e59-b82b-0dbb1a6385c6 | -6.06167 | -53.87944 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98af61d3-3764-3274-8b78-aa576050777c | -5.75416 | -57.60081 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 932bc96a-a0d8-3cdb-9740-d8f8ab3d9199 | -9.19962 | -59.45551 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9dbd4a87-d42d-3f7d-853a-5e6a812ec3b9 | -9.1917 | -59.64101 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5085da3a-e63f-3cff-82b2-93e4f5fa982d | -9.16134 | -59.6795 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 853ef3ee-d94d-3738-a17f-6d8419c54a0a | -6.71528 | -43.19522 | 2025-08-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 11e758a6-f26c-32ae-a91f-902965a12378 | -8.85258 | -49.86282 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7d8a561-2d5a-3154-be46-9770f3fc75fc | -6.45516 | -53.3919 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211140bd-6dc9-3202-87b0-2a22489cf4e6 | -7.64617 | -46.2851 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca91f565-44bd-3535-b995-836f72881498 | -10.75078 | -48.25063 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cf4ad2e-b683-30f3-9807-57100d8b526c | -5.88126 | -57.76338 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 81fd75a1-db17-34f9-a4de-98ffa08c97f5 | -9.19188 | -59.58974 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 799beee1-4b9d-39cb-9197-19a95f345375 | -7.31451 | -44.5548 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31458702-76fa-3ecb-b855-207f5b1720ab | -7.84578 | -46.97203 | 2025-08-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f69aff4-4a36-3583-8a66-56ff7f03b72c | -7.65135 | -46.2812 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c74e7c9d-1f9f-3d29-949b-d9b53d1c12f7 | -9.47855 | -57.82472 | 2025-08-23 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edb13fe9-0b38-3f1a-a952-525f702daed0 | -6.06501 | -53.87997 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482534e2-7f8d-3bcb-9afe-90a394d878de | -6.87928 | -59.81697 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1f0582b-7a3a-3e6b-a7e8-ad6bf38ea144 | -8.84955 | -49.85793 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README43.md)
