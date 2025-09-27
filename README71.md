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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60b530d8-d01e-36fc-a0e8-352bd704b73a | -8.6631 | -43.991 | 2025-09-27 14:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 76b49fa2-6b8f-3056-aba7-2516aa1a6210 | -7.1571 | -45.5158 | 2025-09-27 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| d1bb73f3-15f9-39ce-9913-a417f68abd6c | -9.3343 | -48.9364 | 2025-09-27 14:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3bade9d8-18d0-3ed0-914d-59be97b12567 | -8.1619 | -46.3451 | 2025-09-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fef00ae5-8a01-370c-a4d0-29b29e4294d0 | -10.1845 | -50.2487 | 2025-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0bbaef89-cc1c-3382-abc4-a31f40cc1ef3 | -12.2829 | -44.0568 | 2025-09-27 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| d0b61fb6-3a21-3f84-b90b-ec56e4df9b54 | -7.7794 | -46.9371 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 414.2 |
| 5b5af3e6-8282-3d57-a377-43eab3cbb4fa | -9.4269 | -47.5943 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bbb5fd4f-54c9-333f-bde3-6440628ec29f | -10.8051 | -45.3866 | 2025-09-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| ae139587-9a0b-304e-94e3-fdb768ec7094 | -10.8242 | -45.3841 | 2025-09-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 51a9b3c9-694b-3e2e-8a45-6a14c072f6b3 | -20.7346 | -57.7664 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 978f7b60-4373-32ee-a22d-88e1c880f1a0 | -10.407 | -47.8169 | 2025-09-27 14:40:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c298d15d-5d87-3f7e-b823-48e23d18e931 | -10.4215 | -48.1234 | 2025-09-27 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| c0dd2e48-8b16-3e3a-b5fd-66ef470b0502 | -8.4827 | -47.8202 | 2025-09-27 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 3dd2bd7c-008f-3226-aeb6-9ca827cdf7f6 | -12.6495 | -51.6797 | 2025-09-27 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 346.7 |
| 84cd9069-70a2-35c9-aaea-459ec02beca6 | -7.3661 | -47.0173 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 9e2c5816-370f-34ab-b432-73d2b74b55bd | -9.3517 | -47.5801 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9f33e4e9-3ef5-37d3-af2d-281abc21ccb9 | -12.5481 | -48.4962 | 2025-09-27 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 39fc69fb-6a6d-3823-af9b-7fd03c0370a8 | -9.3514 | -47.6022 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 179960dd-b36b-3629-9029-3690db2dff2f | -17.1936 | -56.3868 | 2025-09-27 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 854f83a6-5608-30e3-82e0-28baa5e9efaf | -9.8971 | -47.7421 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e1d746e9-6e54-3b26-9186-dd7d20768792 | -8.4825 | -47.8421 | 2025-09-27 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 56368f5e-005c-37b3-9420-a83093aef069 | -8.1805 | -46.3657 | 2025-09-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 5e0f6ce3-c442-3adf-8fa8-2114e3450e83 | -8.6328 | -44.848 | 2025-09-27 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 83e95e7a-e249-3594-b045-1ea00832e497 | -18.3247 | -57.0913 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 215.8 |
| f1e34972-e3ab-35e8-891d-17f32a208a65 | -12.2636 | -44.0599 | 2025-09-27 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| f41dfeb1-bee2-3f31-b11e-557b57754d05 | -12.6498 | -48.1509 | 2025-09-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 619ce9cd-3c3c-3011-a6d3-c0abdea4d50b | -7.7558 | -47.3809 | 2025-09-27 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| cc9b043c-c3aa-3524-b73f-ee5eb65cf59b | -10.2037 | -50.2254 | 2025-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f5ca114b-18e9-3d4d-8721-ac780b4b56f4 | -8.8415 | -46.2095 | 2025-09-27 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 01ede70d-477c-3e3b-9b14-277b5d38726d | -9.6159 | -47.5741 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 48977f35-35db-3a77-bb0f-9ef79f3da4a1 | -11.4233 | -44.9331 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5e6ec52f-7805-3e92-919e-539cd5ee479f | -9.671 | -46.3207 | 2025-09-27 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 18f2acc9-30f8-3456-902c-b4245c3c4396 | -11.3834 | -45.0312 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cc9e835b-f09c-3577-baf2-f01a6b8b9881 | -9.3702 | -47.6002 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 44e36d80-5f3f-3904-8a05-91ef5495c77d | -20.7342 | -57.7873 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 275b28bd-4e73-305e-91fa-885d99d8638e | -18.3045 | -57.1145 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| f890b850-7331-3375-bb80-8dfbbf460f8f | -14.8454 | -45.6013 | 2025-09-27 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 0317e698-3415-3c5b-8ee6-c6b774c2d782 | -13.6316 | -48.0758 | 2025-09-27 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1feb07cd-81d5-340c-8df6-e11400cce6b6 | -9.8784 | -47.7221 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 4ddd0a9f-5482-35fb-adf3-e27b7515801b | -5.1887 | -43.7263 | 2025-09-27 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 933351bb-d4c0-34e8-83b0-3be8915491bd | -7.3659 | -47.0394 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| ca802698-c0c2-3e02-a6c0-d44bf9ffb1c7 | -9.0419 | -46.7478 | 2025-09-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6556515c-dfbe-3251-8261-b836b8ffa2d4 | -10.4025 | -48.1256 | 2025-09-27 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b82996c2-c15c-3460-86d7-79393ffa167d | -11.6814 | -44.4078 | 2025-09-27 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 0379a6ae-e406-328f-810d-1b9de90a2b43 | -8.6442 | -43.9931 | 2025-09-27 14:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9346da10-5ae3-34c5-9f8b-52c5b2c736bf | -4.7619 | -43.29 | 2025-09-27 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0a501d78-7bf9-37fa-b9b2-876e5cd5734a | -9.0233 | -46.7275 | 2025-09-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| f3c5e459-976d-34d1-ab30-b49a6fde8ee2 | -11.385 | -44.9386 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b64cf809-b41a-3638-8467-d14dd555c51c | -18.3049 | -57.0938 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 294.4 |
| 0e7fba6c-4537-3658-8a40-e65f5b408ad3 | -12.6499 | -51.6584 | 2025-09-27 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e4a3d4e0-464b-3fe7-9534-dcd5cb95b78a | -10.9374 | -44.3065 | 2025-09-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d8cb7470-20b7-3192-8bc2-863f2108773d | -12.8839 | -62.1256 | 2025-09-27 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |


