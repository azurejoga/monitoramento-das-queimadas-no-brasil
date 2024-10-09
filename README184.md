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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd3fd294-be1d-34be-9f72-1505d854080c | -12.93805 | -62.49997 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f357785c-3539-383a-a022-af334623fb36 | -12.93774 | -62.45472 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7198c732-e524-3c75-be4f-3cd3e0ffa7dd | -12.93401 | -62.4992 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b339338-ffe9-395f-9a32-9e1d38d58ce9 | -12.9337 | -62.45396 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dee91d7b-51c9-3086-9b1e-47c0ef06ac6a | -12.93336 | -62.50286 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cce6975c-196a-35f0-8179-98ef4ccc6633 | -12.92931 | -62.50208 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f9d671c-1b56-3a4f-817e-89966875bcbd | -12.92902 | -62.45685 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a604f1a3-fb34-31d6-a46c-328bf2724ed4 | -12.92642 | -62.47142 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab2f3ff4-ff4c-3907-8b9c-e9d2ab80a4d4 | -12.92577 | -62.47505 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03eb4970-dc1f-3bf1-ac47-8ef0c94f2238 | -12.92169 | -62.73521 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4cb26b5-c251-3ff1-b64b-0b2a4f7719dd | -12.92095 | -62.45532 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64729a94-356c-36a7-8652-1e2862381dbe | -12.92029 | -62.45897 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49b23438-d83e-3e40-9081-0237c9d0503f | -12.91825 | -62.73066 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce55037b-94bb-346c-96e4-6ab175941e0a | -12.91762 | -62.5913 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b4e772a-8f6e-3832-bff7-834e1162dcd0 | -12.91137 | -62.72155 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8a17daf-bc11-3db3-a983-085a12ca734b | -12.9107 | -62.72533 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 742602a5-d05f-3983-bc43-b4d92eae678d | -13.00441 | -62.7389 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87c0905f-ac36-3540-8c62-6677c4bf2753 | -12.99963 | -62.74191 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04e1d6e5-d5d9-3918-a0af-b0c2bc4145bd | -12.99484 | -62.74491 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 040bfb29-691e-3ff6-9791-bb6c691e7830 | -12.99006 | -62.7479 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d29ffe9-fe89-3877-8e65-b4f229b7fe83 | -12.98934 | -62.72825 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b0fb0a-c5a2-3a35-b30a-a434ce95ec02 | -12.97427 | -62.69431 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38148e28-dfce-33d1-869e-2581c758d896 | -12.97085 | -62.68979 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf447ebf-07d7-3364-a913-20556f758285 | -12.96676 | -62.68901 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f5d7007-fef3-376a-a364-e0253f35a9d0 | -12.91758 | -62.73445 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8ed989d-7214-352e-a044-c6659620d12d | -12.91481 | -62.72611 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c7ca01b-9c00-3341-91a2-54dcf36ae8f9 | -12.90659 | -62.72459 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9156d6d-89d4-3e44-9e5e-3b2cbae43ff1 | -12.90591 | -62.72837 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5808dff6-9cf5-3e83-aa2a-a877a89b07c5 | -12.88068 | -62.79822 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1acffbb2-5f36-3c72-a02c-7f0694ccb9dc | -12.8786 | -62.78601 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9281ac3c-97f5-39ef-925a-9c78113a0186 | -12.87791 | -62.78983 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bcaca725-c659-3a5e-a266-897e9977ee9c | -12.87518 | -62.80509 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b0ca874-fc21-3f68-a246-cbbf39cfafe7 | -12.87449 | -62.80893 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32e52549-b6e4-330f-adef-b2a305c81bdc | -12.87105 | -62.80432 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db04d2f9-f3f9-38f0-87b6-ae81046f729e | -12.86691 | -62.80355 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6ba7f58-460f-3d2a-9cc4-4309fc0c7e9d | -12.86209 | -62.80659 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c214988-c931-3450-b1e3-68ad6c8e1d4c | -12.86003 | -62.79436 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 002b6650-cc7f-3d22-8f25-4297fa87f3cc | -12.85521 | -62.7974 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a716972a-6a3b-3e95-a14d-f0451a8b2922 | -12.85382 | -62.80507 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8586c7d0-1226-3bdb-89e3-85089c8d88d5 | -12.84072 | -62.80659 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e5f37ad-7292-36f8-a84f-b14a8a0de854 | -12.7462 | -62.07699 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 177d1836-8631-3cfc-8e61-66068956c387 | -12.7439 | -62.07577 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9c122ea-0f72-3515-be15-ee51e6b8c4d6 | -12.72468 | -62.04531 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b04c22-3081-390d-a429-5c359d0faacf | -12.45663 | -63.00489 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad146f39-31aa-3e46-a692-4321e41ea535 | -12.45522 | -63.01292 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c133d96f-0ee7-3d00-8db8-c6da2637f042 | -12.451 | -63.01212 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd588325-585f-38b2-afd3-99feefe7a079 | -12.45029 | -63.01612 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8200d404-ebe3-3341-9adf-796403af05be | -12.44678 | -63.01132 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b6b5701-70e1-39c4-87a2-8077099ce5a1 | -12.44256 | -63.01052 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cd5b73b-4203-3c73-8641-70a2c8ad374f | -12.43058 | -63.02892 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7165da9-6578-386e-9eee-ca0602b9fc8c | -12.42213 | -63.02731 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b94ac09-5304-31a1-9e8b-55dc4cbc765a | -12.41862 | -63.02254 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f55defb-b12b-3aed-8ac7-ce8bd7e06189 | -12.41791 | -63.0265 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4492e8a2-07a5-33bf-a9bc-df6ba4b5447b | -12.41368 | -63.02571 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06832c90-00c4-36ba-8967-b5bea9c783f7 | -12.6995 | -62.96146 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a63cb67e-50f7-37f3-85ab-056d43be800d | -12.69881 | -62.96183 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f32e686-5d55-3ca4-bb8e-8627a5f63314 | -12.69878 | -62.96539 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c87622f-e4c3-332e-ae3a-f7dfd2652f94 | -12.69812 | -62.96577 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e417bdc-b2ca-35aa-ae0a-685fc62fb5de | -12.6946 | -62.9646 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd31a363-71a7-3846-8505-03642da3de8a | -12.69393 | -62.96498 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b80163ed-f22f-39a6-9aec-dfe8d3dcefcd | -12.69388 | -62.96854 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f3ae3865-a4a2-3c7d-89bc-ffe336660cd1 | -12.69324 | -62.96892 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 185fd956-f41f-35fc-ab02-5b92ae5637d5 | -12.69113 | -62.95988 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c24bcdd-3c90-3147-8dd2-657f2243fb65 | -12.69044 | -62.96024 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d1f202f-e920-330b-a297-7bf7cda74a13 | -12.69041 | -62.96381 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a00cde7-ab87-3aaa-92a3-bb1aaa0ac065 | -12.68974 | -62.96418 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e3be9d31-5d44-367c-b890-44ad03bf2cf1 | -12.68969 | -62.96775 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1b2fcd4b-ff3a-3a7f-83b7-18e7d3de06f3 | -12.68905 | -62.96814 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23c7cd42-5e7c-33fc-a70e-cf59671d3914 | -12.68694 | -62.95549 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9451dc2c-eb16-30ea-a9b1-6dbd801b791d | -12.68625 | -62.95944 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fed4da49-2d33-3591-9fcf-c6ae5c886e3c | -12.68556 | -62.96338 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00efed30-4ede-3bde-8176-2cd3a77626dc | -12.68345 | -63.07317 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e714b96f-0645-3d83-890d-230960ede5cd | -12.68272 | -63.07717 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e29ad81-0b6b-3b97-affc-d9ba6fe4d2a7 | -12.67723 | -63.08504 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cb5a23a-46c7-3615-a7ed-9e718d48a397 | -12.67704 | -63.08437 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1955f9ee-e76d-3051-8433-3f94d2933e68 | -12.67301 | -63.08424 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 570abec4-3c72-3bc3-a1d5-1a00ecfb6140 | -12.67282 | -63.08357 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5f7ba3f-8bfb-3944-8701-b58edcd64cf6 | -12.67208 | -63.0876 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9820b28b-e5d2-3a1b-897a-5ca9b8a8210a | -12.66879 | -63.08344 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c9a62c1-1739-39cf-9072-2126ca76cb4e | -12.6686 | -63.08279 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8596856a-600c-3987-81d6-aa060d29d17e | -12.66808 | -63.08747 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a540c000-5e47-3d0b-9d99-67de70f29a3a | -12.66786 | -63.0868 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8875623b-cd7a-3b48-a70c-f3d8e716aaf7 | -12.66737 | -63.0915 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 22202e24-e927-398d-b86e-c30dfb5991e1 | -12.66712 | -63.09082 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 45dfc6a1-b555-36c6-841b-4cf9d3c7ae13 | -12.66385 | -63.08667 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39d47f6b-24ef-3ded-a93c-77411f15f406 | -12.66315 | -63.0907 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c96580da-2ded-3e38-90e9-843351ea8de1 | -12.65892 | -63.08989 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f05d9ab-6437-3d4e-ba45-24fe44ad8f70 | -12.65399 | -63.09311 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d3e5442-b243-3d5b-825c-202c72d9953d | -12.65327 | -63.09713 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5045993-d067-3c7a-9ab5-e1e5b576a594 | -12.64976 | -63.09231 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 756f077a-2282-365b-932d-3f58e119a8b4 | -12.64905 | -63.09632 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0b85ab0-5ee2-3967-8d3b-24c3a4dc4652 | -12.63637 | -63.09393 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba85a36b-b721-3b15-acd6-b53a24008312 | -12.63053 | -63.1513 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7058baa6-bd51-39a6-bdca-0d7c3ab263ed | -12.62628 | -63.15052 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48e71f41-9b24-37f3-94ac-21f91e7ca08b | -12.88839 | -62.44959 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbc6e105-8590-3b6c-92d8-7de236fd1900 | -12.88499 | -62.44518 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 955c98e2-602e-3d13-b438-4e22d1974554 | -12.88273 | -62.78678 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2abbb61f-927b-3b55-9d29-cca4164289e2 | -12.88204 | -62.79059 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c6a14d3-e66f-39a3-9544-7b9ea069c902 | -12.88095 | -62.44441 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90ad489d-177b-3968-a41e-62125cc318ad | -12.88031 | -62.44806 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README185.md)
