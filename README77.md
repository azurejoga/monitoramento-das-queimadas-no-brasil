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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e3b5d0d-cac7-3e68-8c1c-cc57229bcc90 | -7.603 | -61.3415 | 2026-08-28 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 37e84191-6adf-31c6-b466-2ed4695579e6 | -9.2284 | -51.5219 | 2026-08-28 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| c346c0a7-2dc1-3ecc-b458-592a4544c736 | -10.9556 | -50.5311 | 2026-08-28 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| a21a6beb-3021-389c-a6df-73c2abc79cb0 | -13.3789 | -51.5275 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 0f8810f3-a2a1-3208-a694-122950244075 | -10.7598 | -54.0179 | 2026-08-28 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 15fccfd5-b7d7-3bda-a207-02a25adf86e6 | -13.4191 | -51.4159 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 400.5 |
| 308f8130-33ad-3d03-aace-5c6423158d33 | -10.7839 | -50.6346 | 2026-08-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f4e596e0-1958-3cb0-b6eb-df0147087f67 | -8.948 | -62.3894 | 2026-08-28 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| afc2ecbb-1f19-325d-8421-dee9ffa8521c | -8.5969 | -54.7755 | 2026-08-28 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 196.8 |
| cbaf621b-921a-3a45-b635-5f26189ba5ef | -10.4981 | -64.5005 | 2026-08-28 14:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7e384d69-20f0-3ffc-a9c3-9111e46cb06a | -6.5323 | -55.2378 | 2026-08-28 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a584a12b-e704-38de-85af-2c12e30a3ea7 | -9.9708 | -53.9419 | 2026-08-28 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 173.7 |
| f2f45327-0697-3bd0-adcd-fadab6619a43 | -11.8239 | -47.2178 | 2026-08-28 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 3a07ea46-283a-3a40-9c3a-ceab122e9d0e | -8.0913 | -47.571 | 2026-08-28 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2536b67b-38c0-3032-93ca-70a8ff9f629d | -12.2281 | -50.5578 | 2026-08-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 196.7 |
| f11337ec-65b4-3f0d-b0ac-51ede84d514d | -8.5968 | -54.7957 | 2026-08-28 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b34a24b9-7abf-378d-b58b-418582c55ec7 | -11.7786 | -47.6474 | 2026-08-28 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1a57b49b-77ff-3981-be59-936e9b78d1dc | -6.1657 | -57.7793 | 2026-08-28 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 1c7b71b4-ef24-359a-b7c6-2883a92deaba | -6.5865 | -55.4346 | 2026-08-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 43859c5f-62c4-33da-b194-85c29415e430 | -13.8378 | -54.0573 | 2026-08-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7fde226b-913b-3752-8259-53ba437ba9be | -11.063 | -47.1161 | 2026-08-28 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0f95b8d6-17f6-3701-b0b1-d1140d508e45 | -10.498 | -64.5193 | 2026-08-28 14:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 78b4d8cb-1005-3410-bd98-83e496e9016a | -13.4132 | -51.7784 | 2026-08-28 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fdde7683-b10e-3778-92b2-c5cb75dfa8c5 | -12.0733 | -47.1614 | 2026-08-28 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8044a283-9474-334a-a0ec-96cd10581c15 | -10.9589 | -50.2958 | 2026-08-28 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0b3febbe-e2ef-3ba5-9a55-b431f82a438e | -9.2284 | -51.5219 | 2026-08-28 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 8326c7fe-2f57-3a78-93d5-95e18b8ed07d | -14.1784 | -48.7703 | 2026-08-28 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ea86ec98-634f-3337-b6e0-d2a20554348f | -12.3041 | -50.5701 | 2026-08-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 4c01e554-9962-331f-ac95-5e100073cfaa | -11.6773 | -50.4724 | 2026-08-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4860a88f-8fd8-3f03-affe-1b7e962303b0 | -6.2692 | -53.1526 | 2026-08-28 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b869210c-7351-3293-b61b-668f1775e5e4 | -10.3202 | -49.9782 | 2026-08-28 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e871925e-eaa3-3bda-9932-fe09674e821a | -9.9708 | -53.9419 | 2026-08-28 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 5fde432f-d156-3aa3-85a2-cfd7c57bd7fc | -11.843 | -47.2152 | 2026-08-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e2a99fe8-00ca-3704-8978-967fabf7cc11 | -8.5783 | -54.7768 | 2026-08-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 783c3f5b-0809-34a0-b468-0a47796b7b83 | -13.3789 | -51.5275 | 2026-08-28 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 4f1fffed-7832-312b-9d77-9326b16fff3d | -14.9209 | -52.6029 | 2026-08-28 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 917dd1e9-7b32-365a-a977-58796c08f685 | -13.3358 | -54.3407 | 2026-08-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9f280b3c-bfd3-3efe-9949-5f68af3ea7a3 | -7.5846 | -61.3232 | 2026-08-28 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 49b6da88-27eb-33bc-98d1-d7c7c03b2983 | -12.285 | -50.5724 | 2026-08-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5822b656-baf6-3e97-83e6-3cb7df4f9dd4 | -12.3038 | -50.5915 | 2026-08-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ce81a422-fdd8-3203-b96d-dd6648ad74c1 | -10.7596 | -54.0384 | 2026-08-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| e6582915-cea5-3410-b864-8e0cdc717d9f | -11.2109 | -51.2476 | 2026-08-28 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 417e52fa-f063-3d5e-8022-bed1ee6e1b0d | -14.9981 | -52.6138 | 2026-08-28 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 74164a57-5842-3b95-9c53-0718e21e3410 | -10.8992 | -46.6442 | 2026-08-28 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f0eb7f5d-a6ec-3b35-bfc3-9c60558b0280 | -11.7786 | -47.6474 | 2026-08-28 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5697aac1-a8ed-303d-a175-354a6aaac813 | -8.948 | -62.3894 | 2026-08-28 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0d4dc431-a1e7-3796-8815-869ae15d2eb1 | -14.9985 | -52.5925 | 2026-08-28 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| d4f2b8da-cec0-3d25-b4af-40c1f0a8ac1b | -8.5968 | -54.7957 | 2026-08-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| f01fc3f5-01db-359d-a3d3-ffdd6b80eecb | -13.3985 | -51.5037 | 2026-08-28 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 91022a10-3aa5-3aac-9a52-44bd86ff6d9c | -7.1266 | -43.1714 | 2026-08-28 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 57ae3a86-0546-387d-a3cc-aac1375cfd2b | -11.8243 | -47.1954 | 2026-08-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 615e0eb9-0334-3085-9be3-e8034cbd8f37 | -11.006 | -49.6461 | 2026-08-28 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| de3398c0-b668-31e8-afe2-38d011015963 | -10.7407 | -54.0401 | 2026-08-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| afd14be8-4cf5-35fa-bf99-9a1b9cd0aa56 | -9.4758 | -48.1822 | 2026-08-28 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2016ade1-0ceb-33c8-a105-52d5d9d49504 | -14.2989 | -51.7072 | 2026-08-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 397fdd4b-a057-31b6-9344-11e2589725c1 | -8.5969 | -54.7755 | 2026-08-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 206.0 |
| c95e994e-a5a5-365f-ab93-9586b9d0a14e | -10.7598 | -54.0179 | 2026-08-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 57568d0e-b39e-30df-8574-50e23f7bed6d | -7.6214 | -61.3408 | 2026-08-28 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 04e09ff0-c9d6-3d88-82f8-872e578f1d6f | -8.0913 | -47.571 | 2026-08-28 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3a19e83c-8215-3f31-9f95-acc760092a35 | -6.857 | -59.4371 | 2026-08-28 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| dfe84803-6de1-300d-83b4-466b6870688b | -11.2493 | -45.0501 | 2026-08-28 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6e95adb5-5052-3982-9258-1dbb231b3540 | -14.3182 | -51.7046 | 2026-08-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 178.2 |
| ced25058-036c-3c88-a7bf-6d770d9687a3 | -13.3254 | -46.9333 | 2026-08-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c265cfa9-3a53-3d8f-baea-ddfab838f121 | -10.8996 | -46.6216 | 2026-08-28 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 84e44faf-3563-3700-9825-0c5f09f0ee2a | -6.605 | -55.4337 | 2026-08-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 317.3 |
| f05111b2-ea72-3c72-8231-f61bf31de59e | -6.2693 | -53.1322 | 2026-08-28 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| fbc1ea45-08f9-3c10-b562-d16a15f6a4d9 | -6.1656 | -57.7988 | 2026-08-28 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 255323fd-77cb-3158-bb25-166861cf2237 | -10.4981 | -64.5005 | 2026-08-28 14:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 32beac4f-2239-304c-83c5-eb5ca093d932 | -6.1472 | -57.7995 | 2026-08-28 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 45849c2f-2e23-3509-acf6-f3d708795ee3 | -8.9478 | -62.4084 | 2026-08-28 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 635d676b-48f8-378d-a660-56d564e02df7 | -14.3376 | -51.702 | 2026-08-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d53d7dd6-0be7-3a77-9d5b-ae6250da9855 | -9.2282 | -51.5428 | 2026-08-28 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 3c9c7ce0-93d4-3f4f-9bb1-e31aa8e55547 | -14.8821 | -52.608 | 2026-08-28 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0d434201-3435-35df-b510-7578bd903338 | -6.5863 | -55.4546 | 2026-08-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 4b12d17a-fd13-3280-8124-0dadda699594 | -11.8239 | -47.2178 | 2026-08-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b7ca3e6b-c4ac-3877-b3b9-600c3dcaa098 | -13.3597 | -51.5299 | 2026-08-28 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 04c089d6-49dd-3aad-a77a-75f7d5549551 | -6.1657 | -57.7793 | 2026-08-28 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| aeb07ac1-b2f9-3cbb-9075-34e0b8bcae0f | -10.9187 | -46.6192 | 2026-08-28 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2ec48d98-ac8e-3f05-914b-b0b62b57df39 | -7.603 | -61.3415 | 2026-08-28 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 66a176ae-14ac-3e9c-9369-1afdcef8e351 | -13.44 | -51.44 | 2026-08-28 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8279aaf1-be1d-3257-a2c4-ff555b5f4743 | -8.1 | -45.84 | 2026-08-28 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffb20e75-dd2b-3630-8c8c-bacaf61c6387 | -8.1 | -45.79 | 2026-08-28 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f53dbdb1-8ae5-32b8-aff6-875c11fac373 | -8.07 | -45.83 | 2026-08-28 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab42c03b-4fde-3273-857e-4dfefda0e638 | -10.8992 | -46.6442 | 2026-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a8ace433-abb4-3b76-83eb-b114ce89d5a4 | -11.8239 | -47.2178 | 2026-08-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 7e6bd2e8-8209-3b9c-b1e8-c5dead13d2bd | -11.006 | -49.6461 | 2026-08-28 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 326e1dd7-d46b-3fa0-9a6a-1f6f6b4e33b5 | -11.7786 | -47.6474 | 2026-08-28 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b0ec8794-e46f-373b-9f44-ebd3735dc238 | -12.3038 | -50.5915 | 2026-08-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 4f793037-6a75-3e2e-a480-881c556aac48 | -14.6024 | -53.1508 | 2026-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4ef95bd6-419c-3ece-b41e-2d08dba57d17 | -10.4981 | -64.5005 | 2026-08-28 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| bef9199a-a2cd-3f3e-b414-0c1ac3bf1192 | -14.3376 | -51.702 | 2026-08-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 81ee65e1-9ccf-3c8a-b463-a5fdf031bc8a | -13.8752 | -54.1153 | 2026-08-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 13836428-210d-3f7f-b736-1ffd0d23b2cb | -6.2693 | -53.1322 | 2026-08-28 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 2f3a11d4-9eb5-33d8-8098-0d138b566d40 | -8.9478 | -62.4084 | 2026-08-28 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| bd528568-f2bc-3a90-b4d5-d472501e387e | -10.498 | -64.5193 | 2026-08-28 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d985a787-1f5a-3c31-a8b0-7406a1db92ef | -14.3182 | -51.7046 | 2026-08-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 0e8a5888-7421-3796-916d-29a3c71f096a | -9.2282 | -51.5428 | 2026-08-28 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 37666b32-fc91-332a-b134-f1d3ec139087 | -11.843 | -47.2152 | 2026-08-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 609b4db1-b92a-3d03-9448-90644a725d37 | -10.8025 | -50.6539 | 2026-08-28 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 30ee44b2-244a-32bd-8a90-eb3c0a79642e | -10.9589 | -50.2958 | 2026-08-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |


[Clique aqui para ver as próximas entradas](README78.md)
