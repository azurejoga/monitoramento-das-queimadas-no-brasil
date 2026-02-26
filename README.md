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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee6d24e-fdee-36b4-ad21-4a03abae28d4 | 1.5046 | -59.9306 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 07133176-401d-3c9d-b7b8-b9be0e02b1a7 | 1.5046 | -59.9497 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 091ab9cb-3608-37e8-802e-3d0b9f6592ea | 1.4864 | -59.9498 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.8 |
| eaae6667-6996-3db3-9e0a-62dca660bac1 | -10.1424 | -36.2761 | 2026-02-26 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.1 |
| 953b7de0-fca2-3669-9e6c-22a8a01adc8a | 1.4681 | -59.9309 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0064762b-0f0a-31fa-9fb4-138f7cb3dac4 | 1.4681 | -59.95 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3d928f49-0cfc-32b0-b761-ccb788e1970d | 1.4864 | -59.9308 | 2026-02-26 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 199.4 |
| 1ba4b15a-ba5e-3561-8376-039d2802ad4d | 1.4864 | -59.9498 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 2ba0ef7c-ea53-3bf2-975c-e2c55096194d | 1.4864 | -59.9308 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| cb886cc2-bbaa-3470-8069-a70cfb632b56 | 1.4681 | -59.9309 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1678cb50-fae4-384c-846b-c5572e171e17 | 1.5046 | -59.9306 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6bfbf610-6a85-3895-8af4-7df63b155beb | 1.5046 | -59.9497 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| f4e540a7-07ec-3c20-8dd4-4f50831fa22c | 1.4681 | -59.95 | 2026-02-26 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1d67046b-f146-3098-9d01-cd5f75dd0409 | -9.8013 | -35.9855 | 2026-02-26 00:40:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 186.9 |
| 3a1689a2-92b9-3b24-a18c-70d0bfaf3353 | -9.782 | -35.9889 | 2026-02-26 00:40:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 123.0 |
| 86b56e57-d5cb-3088-ba72-7bd49fb9f731 | -9.8008 | -36.0127 | 2026-02-26 00:40:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 130.1 |
| c927e9bc-e493-37dc-b155-7648f06ffee3 | -9.7815 | -36.0161 | 2026-02-26 00:40:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| c341d114-ce75-331f-9f84-034a4aeeba80 | -9.782 | -35.9889 | 2026-02-26 01:00:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 152.8 |
| 1ef2c216-0ae4-33af-b246-979e321fc340 | -9.7815 | -36.0161 | 2026-02-26 01:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 39df5be3-b6c9-3656-a5a5-c51d2586e280 | -10.1424 | -36.2761 | 2026-02-26 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| d8cc2777-0f9f-3dd6-92f0-b6d28f554e55 | -9.8008 | -36.0127 | 2026-02-26 01:00:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| ab7d07d7-f584-318b-95bb-67cb6c928494 | -9.8013 | -35.9855 | 2026-02-26 01:00:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 198.4 |
| 3c4f21ee-0ff0-3d3c-b7ca-a0fa4bc6ff9c | -10.6863 | -37.0602 | 2026-02-26 01:10:00 | GOES-19 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| f661d0a5-bbe8-3db2-85b4-55f5cd21ad7c | -10.6669 | -37.0637 | 2026-02-26 01:10:00 | GOES-19 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| e88b38f8-eea4-3256-a804-70b6e3202f8e | 1.4864 | -59.9308 | 2026-02-26 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c3efa32b-355b-3aac-a28c-6cc43d4482a5 | 1.5046 | -59.9306 | 2026-02-26 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 146a745d-41c8-3402-88d4-8bd3b891c00e | 2.57205 | -60.5462 | 2026-02-26 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5088dd15-dc14-34c5-afb2-c26cc5ca9e9a | 2.58079 | -60.55299 | 2026-02-26 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8e9ed9b7-df81-3774-a56f-e3c9bcfd9aee | 1.12324 | -60.51287 | 2026-02-26 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| da476a2f-afd8-33f4-9856-68d8a57abdb8 | 1.4864 | -59.9308 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 228.9 |
| ba897d32-7470-385f-a444-bb5890475c00 | 1.5046 | -59.9497 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 9055a623-4af5-31e6-8587-0bcd041a8c09 | 1.4864 | -59.9498 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.3 |
| d77adde0-c647-3d68-8619-61d689f0b435 | 1.4681 | -59.9309 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f375f9cc-92c4-395c-913a-bb2117e33cfd | -10.1613 | -36.2997 | 2026-02-26 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| f45cec9d-aec0-37ac-a396-7af686cc7072 | 1.5046 | -59.9306 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 744f5422-2894-3566-a4c6-244b5d01b083 | 1.4681 | -59.95 | 2026-02-26 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 46232855-e175-3015-96e0-f2a1a143dce7 | 1.4681 | -59.9309 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9bc4d6f5-5142-3809-a62f-a382eafd2773 | 1.4864 | -59.9498 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1274e771-388f-3097-b1b3-cc77af36ad3d | 1.5046 | -59.9306 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a44a4dd7-208c-3b92-b912-688c2bf50783 | 3.4588 | -59.9221 | 2026-02-26 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 86b79c15-6bdc-3538-a8cd-f913f7c2f2c9 | 1.5046 | -59.9497 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.0 |
| f6831aac-d0b2-37a6-b31c-b4926bbeec78 | 1.4681 | -59.95 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 90fcf3a0-ec78-385d-8e8f-6da0c1bfe2f2 | 1.4864 | -59.9308 | 2026-02-26 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 0983ceb1-4a1d-37f4-8eb2-41d8a54d7033 | 3.4587 | -59.9412 | 2026-02-26 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 391269b5-8693-37dc-8a6b-a79bc91a98a3 | 3.4588 | -59.9221 | 2026-02-26 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f26c750f-b163-3725-bf53-9b8110cfabf4 | 1.4681 | -59.95 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 23b6c247-cf25-3176-bc99-0a1dfe97efd9 | 1.4864 | -59.9308 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 0fadc5c5-0a63-3267-adb0-593f2b734f68 | 1.5046 | -59.9497 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 91ae6bda-a1c7-3dd5-b735-453552404a0f | 1.5046 | -59.9306 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a6c5f9ea-c667-33c5-814d-c84c19d319d5 | 1.4681 | -59.9309 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 58df5200-4799-3200-a207-14467f64acff | 1.4864 | -59.9498 | 2026-02-26 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 7519594d-3da3-3fd2-bbf6-9f1c7ddd268d | 1.5046 | -59.9497 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 56034e63-899a-309b-b9ba-c31717e90646 | 1.4864 | -59.9308 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ca326535-f7c7-3366-bf49-831661eb3b91 | 1.4681 | -59.9309 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 4a9bd3e7-689f-30e1-9826-b786fc0d66e8 | -9.4054 | -35.5373 | 2026-02-26 02:50:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 4518f652-2cf9-348f-9037-cb14696e9387 | -9.4247 | -35.5339 | 2026-02-26 02:50:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 151.5 |
| 75eb2105-ecff-314c-a07e-1f31e3684ad8 | 1.4864 | -59.9498 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f82ce49b-409d-3470-909c-d937b2f2ad2e | 1.4681 | -59.95 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cbfe7c8d-18a4-347c-8e73-52a0ca2d129d | 1.5046 | -59.9306 | 2026-02-26 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| daa4d93e-4e24-3f73-876a-c5f66d892540 | -9.4247 | -35.5339 | 2026-02-26 03:00:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.9 |
| 1bfbd5cb-aec8-32cb-b0e9-7c566c117120 | -9.42672 | -35.5327 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 07115d1c-296e-3795-8d3c-6273067d1646 | -9.91282 | -36.04103 | 2026-02-26 03:06:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 3d44c658-f69d-395c-936a-8d1d8fe2ac56 | -9.41445 | -35.54042 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31cf68ed-cb58-300a-be06-6e4776b8ba97 | -9.42209 | -35.52844 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99af0bcc-24e4-3303-813d-4ea752276f8c | -9.41968 | -35.54145 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 001a8b68-2a42-31cd-990f-4d9b5ee95278 | -9.91217 | -36.04453 | 2026-02-26 03:06:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| dfe27371-9503-3341-85a9-6689033e823d | -9.41625 | -35.53067 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63c9e186-cdfa-36bd-b994-6fb3f478c574 | -9.41566 | -35.5339 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2c7923fd-d7ab-3d68-b827-477d786db3ef | -9.42612 | -35.53596 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| a7cd842d-e539-3246-a77e-fad35485f88b | -9.42552 | -35.53921 | 2026-02-26 03:06:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 6baf7a13-c9da-3b95-a5dc-5a4e3f6370f0 | -9.42149 | -35.5317 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 04c68b15-7921-3b89-88d3-fb3e81adaae4 | -9.41506 | -35.53714 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d944c411-f2da-3f6a-a530-4c9a247e3539 | -9.42029 | -35.53817 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| eca9b799-47f0-36f7-a281-faf4c434c3ab | -8.62496 | -35.06163 | 2026-02-26 03:06:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9cdafc61-8933-3f03-9190-ddbf9489be43 | -9.41908 | -35.54473 | 2026-02-26 03:06:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| acf7228c-80bd-3fe1-8be3-f10872bf4754 | -9.42089 | -35.53493 | 2026-02-26 03:06:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 34dbac52-11d3-35be-a150-bf960944d49d | -9.4054 | -35.5373 | 2026-02-26 03:20:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| 6f4e6077-aef6-3019-87b2-9da63ffabb8d | -9.4247 | -35.5339 | 2026-02-26 03:20:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 180.6 |
| b41ce1ef-7cf0-3b5a-8ca6-c1be2ae6a439 | -9.7399 | -36.1856 | 2026-02-26 03:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| b8bb7319-99f3-3b4a-a67c-f9c97033e4b8 | -9.73493 | -36.18644 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 0fa9d007-15d8-3ef4-ba8e-398ea66c1dbc | -7.20747 | -35.78062 | 2026-02-26 03:36:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c02a0f4e-4d46-3e3d-9385-7f8f202e3fc0 | -9.73053 | -36.19022 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 7fbd5bac-18eb-33c9-8b3e-fec00d83c2ed | -5.10181 | -39.46935 | 2026-02-26 03:36:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7bfda49-8fcd-328c-9e6f-d8699676ca60 | -9.72686 | -36.18965 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c32b498f-2447-3040-b5d8-45b84a94cd54 | -7.21116 | -35.78124 | 2026-02-26 03:36:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae5a668f-0f2c-3b82-89ef-c92e891b0c50 | -9.42584 | -35.53422 | 2026-02-26 03:36:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 19c4c99f-f21f-3596-9546-f24d52c40dfd | -9.42229 | -35.53361 | 2026-02-26 03:36:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 86b76641-984d-3db0-ab26-bcf122999075 | -9.72759 | -36.18535 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bfe19420-d134-3f8c-ab1e-f211bd310af5 | -9.73126 | -36.18592 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 0fb56f29-42a8-3c44-b46e-adf0ee092e2c | -9.73861 | -36.18699 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 80b77d48-cbc2-313d-aaae-508efc6069d1 | -9.41873 | -35.53299 | 2026-02-26 03:36:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a254e7c-3843-32c1-85a3-b2c04e51d2ec | -4.6757 | -38.40753 | 2026-02-26 03:36:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e112d9e1-7ccd-3865-b035-1b2362576325 | -9.73788 | -36.19128 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| f023455d-eefd-3b8d-8698-20c8af6f1ad2 | -9.73421 | -36.19074 | 2026-02-26 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 2d6ca2cf-a071-3415-8ec3-8ea094e22099 | -5.10666 | -39.47021 | 2026-02-26 03:36:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 728b9cc6-bdea-314e-addc-d494dbb5a0c7 | -5.1033 | -39.46727 | 2026-02-26 03:55:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d8a0ace-498e-3655-8a39-7bacc39c3a5c | -9.0291 | -35.44007 | 2026-02-26 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a4d374e8-e677-3ef2-b885-ea7d90593648 | -8.40503 | -35.24091 | 2026-02-26 03:55:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cb1b55d-a03a-3a09-848e-8b08f97a8ff6 | -7.20986 | -35.78179 | 2026-02-26 03:55:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f41dfeec-5939-34d8-a162-489e14edb4d3 | 3.03971 | -60.03857 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README2.md)
