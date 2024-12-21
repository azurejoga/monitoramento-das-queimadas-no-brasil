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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d912a69a-44aa-3883-821c-20a6352ec5ef | -2.63433 | -48.03453 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b41cfafc-80b8-3d87-9d52-660fc94fdc47 | -2.07819 | -52.04511 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae8d460d-4e40-3321-b3de-ae46606f65b3 | -1.29282 | -53.11985 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bb3543c-1143-36a0-a8cd-3ae9375fd7e2 | -5.91301 | -43.47808 | 2024-12-21 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 762b9e8f-7e44-33aa-ad9d-3bf6efc72c00 | -2.08153 | -52.04738 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9326e8af-717d-334c-a04b-5c894bd7e1bd | -2.90272 | -54.50075 | 2024-12-21 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd127b9d-840d-3b80-b1a8-2a68e39b89d6 | -2.4438 | -47.48001 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a95d1bc5-00d7-3833-8915-9c220560da7c | -1.25533 | -53.4796 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1b1a391-698d-37a2-8a9f-8394d9973716 | -2.63203 | -48.04977 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 658376a9-8117-39d2-98c3-1dc3f0db4131 | -2.73426 | -47.73006 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9514ce6d-6980-316a-83f4-1aa28d851bc5 | -2.554 | -46.88269 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1a99d3a5-e1a3-3230-b512-71b6f965dbc1 | -2.76376 | -47.39471 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d20820c-4e3e-3a8e-aa2b-a09332e4dac2 | -1.25557 | -53.52482 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0768a461-d2fa-38d2-a38a-37b3a06ef2a9 | -2.50724 | -48.06039 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c04370-3f10-3cb1-8ceb-9e448db209fa | -2.05637 | -52.05674 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5b3f7f9-03c1-37e0-8de0-fdee230e0c67 | -11.97901 | -63.61098 | 2024-12-21 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42443b8c-0676-330f-8ff5-3db065c5a901 | -12.55449 | -57.75974 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7b27067-04d1-3db1-9a17-66370f5deeff | -12.55897 | -57.75301 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 177c10b8-1910-312f-800f-250d7cc02397 | -12.55505 | -57.75611 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84361869-974e-3dad-b2d2-f97babccb9b4 | -15.07796 | -48.94355 | 2024-12-21 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2920711-9454-3ae8-9f41-5cf8cee5b224 | -12.25381 | -60.50976 | 2024-12-21 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac40e596-d8ea-3e73-9d02-5031f102fc36 | -10.53479 | -59.45197 | 2024-12-21 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 199d878b-7fdc-375b-88e4-5a16cc55b7ca | -12.55841 | -57.75665 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0aa5b78b-21d5-3889-a099-efea319202ef | -12.55786 | -57.76027 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4671c29c-4901-35de-a855-a102f6435e96 | -12.5556 | -57.75248 | 2024-12-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9faca170-2b38-34e2-bb5c-ad6a44e0f756 | -14.84484 | -56.75131 | 2024-12-21 05:14:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb51d796-5d27-3121-bc2b-50c05fd0ada1 | -19.08554 | -57.71302 | 2024-12-21 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eb7a8993-ea93-3c6e-85d7-400cae69441f | -20.47661 | -55.84499 | 2024-12-21 05:14:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 491dacb7-dcd4-390c-a0e7-f8802af7a837 | -15.33053 | -60.01563 | 2024-12-21 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b437b2-6464-313d-8c57-1ad8cea23907 | -20.47514 | -55.84268 | 2024-12-21 05:14:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f82bde3a-dd93-3f8b-a910-73c624b20f82 | -18.60559 | -51.78895 | 2024-12-21 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e281f51f-142f-3a86-9c62-2f97b8a62fb9 | -15.16564 | -56.47035 | 2024-12-21 05:14:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dfac7c8-d0e4-33f4-87d0-ab0a80d249cb | -18.6041 | -51.7904 | 2024-12-21 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5fa2a97-3153-33b5-bfc3-71b61347c079 | -19.082 | -57.71247 | 2024-12-21 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 421f0539-f01f-3b84-9777-27e5460943db | -25.19695 | -49.32387 | 2024-12-21 05:16:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c986241d-24aa-30a4-863c-98e935d5a997 | 4.45431 | -61.0323 | 2024-12-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d72b3cc-f5e5-3029-8f8a-9ab8b2d24ed5 | 4.45707 | -61.02835 | 2024-12-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 393260e6-b335-3cb0-8e5d-632ba9673b49 | 4.45377 | -61.02887 | 2024-12-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3988756-6f38-3131-82d6-fcce18d3a4e1 | 4.45323 | -61.02542 | 2024-12-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17d805ba-2fae-34cf-94d9-7bc877710f48 | -3.06375 | -47.48163 | 2024-12-21 05:31:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa5f6149-fc7b-3f88-8d89-12aff15deddf | -1.56327 | -46.77217 | 2024-12-21 05:31:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 485793e2-9821-342d-82b5-d98036f3b029 | -3.79656 | -46.84315 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 29e91042-9154-36e4-a1de-06d6577dcabe | -2.43457 | -47.482 | 2024-12-21 05:31:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 44faf543-e89a-30ac-8258-f9ea2754c33d | -3.90222 | -46.99918 | 2024-12-21 05:31:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 618a316c-d959-39ec-a421-f860eccba8ce | -3.75414 | -47.18673 | 2024-12-21 05:31:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d8f4859-929f-3095-b164-10619c19de15 | -4.08765 | -46.81378 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b27ddd2-7ef3-3fa7-993d-e8f8cf8e4ce8 | -3.80743 | -46.70977 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e41fdc8b-3967-3b7c-99f1-7e495ff4c08f | -4.05572 | -47.08765 | 2024-12-21 05:31:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0178c4a0-cdf1-35d1-b16f-408b432eeb01 | -2.70243 | -46.13293 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e3097707-6ef7-3d79-ac1d-9c233e4fc551 | -3.91932 | -46.88495 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd645e55-3062-38a7-9e29-374d666affc6 | -3.9703 | -46.91682 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65a74399-3a23-35df-909d-a19524798024 | -2.55196 | -46.87978 | 2024-12-21 05:31:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44bf308d-6c83-352c-91b1-8051010389b0 | -3.94502 | -46.40921 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a969671d-a69e-31a8-99db-e218df489df3 | -3.91801 | -46.89375 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 11b86392-6e79-3c3b-86f8-30d5a019ac16 | -3.86262 | -46.58222 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2cd75dc-ce26-3e83-b68f-6a245dac947e | -3.79524 | -46.85194 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 77cf594d-201e-3309-a1b3-114d25d00ee2 | -3.83038 | -46.67699 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 40ba7703-2690-3130-90c8-2dc5d4c9f973 | -2.76335 | -47.39257 | 2024-12-21 05:31:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c5902dd-8a6e-31d7-90ae-132ad4404f57 | -5.91235 | -43.47353 | 2024-12-21 05:31:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ec527c85-825f-35e6-bd41-7a2e0c2caa37 | -1.87414 | -45.55471 | 2024-12-21 05:31:00 | AQUA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7799ed79-c247-31f1-9cbe-aff302a93fec | -4.06303 | -46.91821 | 2024-12-21 05:31:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5bc26f6e-3a5b-3d5c-8d79-f7b197faa167 | -2.7011 | -46.14185 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4c439946-fd04-3691-a505-887fa6af5db4 | -3.99769 | -46.55076 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33c98175-f8c8-347f-8150-9a080acc7aaa | -2.65057 | -46.10128 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 34828fcc-5a76-3414-8f7e-1a9857206780 | -2.6297 | -48.03154 | 2024-12-21 05:31:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c8c9bdea-e853-39ae-a3f4-245241509583 | -4.06435 | -46.90941 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd0d0368-495c-306d-8e2a-023ca90a7599 | -3.08134 | -46.56348 | 2024-12-21 05:31:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f789a76-78ff-3948-a57c-82460085b011 | -4.09648 | -46.81506 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 82cd1382-6d8a-384b-9253-212c7aa998ec | -4.10212 | -46.71672 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 094d3a0e-724b-32df-a28e-6833c59c06e8 | -2.87889 | -48.27371 | 2024-12-21 05:31:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bf6e8e61-dde9-30f6-8ac4-7ab0aef5b349 | -4.03419 | -46.79119 | 2024-12-21 05:31:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34d8eb4e-7583-37fa-8577-3e3213c0a173 | -1.25625 | -53.52301 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67d585ef-6ae6-3b2d-b300-6009e48c88d7 | -1.28875 | -53.11826 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d4ad0e-12d4-310e-9ecd-d17e5ecf5408 | -4.28022 | -55.743 | 2024-12-21 05:31:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d2456f7-072b-3b98-b0b3-8240019aa921 | -1.29416 | -53.11917 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee3814ab-dfdc-3980-b458-3b25ef06a7f9 | -2.05668 | -52.05519 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda67546-743d-37a3-aa22-e2b35c914099 | -1.29255 | -53.12929 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2e52914-682c-3d06-996b-140ec2171d9c | -1.29035 | -53.11848 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b133aca-8283-3ebc-9282-9eebe5f2298a | -2.07564 | -52.04943 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd0af253-d45a-3a6a-a164-4eb374be8e95 | -1.28933 | -53.12528 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4e9aa90-23c4-3437-bf0d-c12d6958f92f | -1.26203 | -53.52052 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08aa173b-22e3-31a6-971a-c45d52b95bac | -2.05604 | -52.05938 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9387713e-f8c8-328c-ae86-02b5d6d2767f | -1.2881 | -53.09661 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5be2b15-0751-3327-b3a6-81462c4c27e0 | -1.28882 | -53.12865 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7791a242-8e43-3b24-8875-a384ead258a7 | -1.34484 | -53.85418 | 2024-12-21 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4392b39f-a7f3-3314-ac4c-acc2a3653d7a | -1.26154 | -53.52371 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e271597-2f2b-3e0f-9aa9-2ee9ecd19e32 | -2.89913 | -54.50135 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8c55ac9-c5c0-3cc4-a60a-e855df46536a | -1.25578 | -53.52608 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9761545b-06fd-3d7e-a38c-a5342a884db8 | -0.35177 | -50.08265 | 2024-12-21 05:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a0e51c-1b95-32a5-a7ca-74447491e293 | -1.29308 | -53.12596 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45771c75-1e41-384b-8da7-49f294855fef | -0.35827 | -50.08368 | 2024-12-21 05:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ad2af96-cddb-3005-9f48-8108fe3b0caf | -2.07943 | -52.05238 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288d3a1f-1b8e-3112-b847-cdb80fa8a61a | -1.71087 | -52.574 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6511d79f-729b-3553-93ff-83a7a9b8cb33 | 2.6007 | -61.15063 | 2024-12-21 05:31:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bdb5f8a-f487-308b-8233-1e3521d52215 | -1.28984 | -53.12189 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2d7e479-ce27-3374-b195-479b7aa0cbee | -2.68205 | -54.03138 | 2024-12-21 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68efe4da-8014-36c5-81c8-9dfed9188b30 | -2.90466 | -54.49906 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f4cbeb-bce6-36bd-89bd-dcc771135299 | -1.29362 | -53.1226 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e837b664-23b1-3a82-9eb1-21376dda1170 | -2.90332 | -54.5007 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c628b9f0-5a5f-378a-8e23-dd7e208b1ce6 | -1.28756 | -53.10017 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
