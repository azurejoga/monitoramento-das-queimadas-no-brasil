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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15b5f016-14c2-31d9-b11a-3e56df33353d | -9.2092 | -59.4997 | 2025-08-25 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 4e4be423-e388-34cb-bf9a-9fe98f7cce68 | -9.324 | -48.2633 | 2025-08-25 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 226.2 |
| cbd4079b-a211-3ac1-a50c-9d5b8ac1bc8b | -10.5874 | -47.1527 | 2025-08-25 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 91622f09-af95-3213-8b0f-8cdd34f5bc6c | -14.9247 | -45.5403 | 2025-08-25 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| cebdafb0-a735-33c0-9f28-d0be1b82fc03 | -6.1961 | -44.1365 | 2025-08-25 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 569ce309-3e3e-3621-9379-d75c758b6ad7 | -6.3733 | -45.1963 | 2025-08-25 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 602dfd2d-5e60-38cc-9cfa-17916f9b0ca3 | -8.8919 | -62.4487 | 2025-08-25 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.9 |
| b72a4b89-1a5f-37e6-8fc9-9ec9d3f86d50 | -8.9689 | -65.4198 | 2025-08-25 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 07e0070a-8fe3-37db-8b55-595bffd42ee2 | -5.6441 | -45.1599 | 2025-08-25 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 78d526cb-2784-39a1-8dc4-8a498e64340f | -12.3078 | -49.1421 | 2025-08-25 13:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 19fb43fa-cec0-39bb-92b5-723710bdf1d0 | -5.6817 | -45.1347 | 2025-08-25 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| aa4bbd5e-e340-3d79-91ab-7b6a78596501 | -8.5759 | -62.6133 | 2025-08-25 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e1985913-1f5d-31ef-a06a-607fed91ce3f | -14.9247 | -45.5403 | 2025-08-25 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| a7ed188f-dd19-36b6-88c9-01015316c3c7 | -5.6817 | -45.1347 | 2025-08-25 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 228.2 |
| e3b158a1-4e32-3bf6-9a53-1b036324e94f | -14.2159 | -58.6117 | 2025-08-25 13:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 03a1d890-b7fd-30c6-9825-5f2cf090b084 | -12.6937 | -47.8339 | 2025-08-25 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| df045839-9354-3342-a441-2727826fa798 | -18.0633 | -47.8594 | 2025-08-25 13:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 80b1ded5-1e5a-32fe-8e90-b542b962ca5f | -3.4541 | -43.3618 | 2025-08-25 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a7c883f9-be66-3e29-93b0-07cc9cb800cf | -9.2092 | -59.4997 | 2025-08-25 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8798dac8-810e-3a84-95f3-1343ef047779 | -11.6089 | -46.3699 | 2025-08-25 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 1cb35b69-9678-3fca-bd47-ed69dfb405e1 | -8.6313 | -62.649 | 2025-08-25 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b7cd49d7-408c-347e-a4fa-6a77d9f8258f | -8.5758 | -62.6323 | 2025-08-25 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 271ae88d-b1f6-3a47-b788-38b84244ef32 | -12.3078 | -49.1421 | 2025-08-25 13:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d6ab5940-6060-33ba-b3a0-82225c6f56c2 | -9.1812 | -60.7939 | 2025-08-25 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2ff414d2-6d6c-3572-9b5e-b4e68aa38b76 | -8.8919 | -62.4487 | 2025-08-25 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 728698f8-e38c-35ae-b1bb-076bee3297a5 | -9.1906 | -59.5007 | 2025-08-25 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 80b52d86-1e29-311e-b335-160d880181dc | -8.8734 | -62.4495 | 2025-08-25 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 4c52e98d-c2b7-38ae-b91b-121f64bb6c0e | -8.8735 | -62.4305 | 2025-08-25 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 1b51ff74-a418-38c7-9aeb-0f349d5edea4 | -6.8201 | -59.4386 | 2025-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 70f3fae4-bd7d-3e7c-a6e4-fa40e17ab222 | -9.1722 | -59.4629 | 2025-08-25 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9058fe36-2068-30f7-8eef-80d7bb1617d1 | -10.5364 | -46.7568 | 2025-08-25 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 0134f5a7-d6d0-3e8e-94cd-6d207bcbb444 | -11.6093 | -46.3472 | 2025-08-25 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 90dd8fc5-775c-3a48-b244-260b428683bc | -14.2157 | -58.6316 | 2025-08-25 13:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 211.4 |
| d68b1d1d-bf68-3a50-a911-10bf3d996bc7 | -7.605 | -47.4599 | 2025-08-25 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 54f3bc64-4541-3e6e-bc27-05ae2e29ee40 | -9.324 | -48.2633 | 2025-08-25 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| b006b6b2-0c92-3fff-bc3b-0d2062f0b415 | -14.9051 | -45.5439 | 2025-08-25 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| fc21e6d0-0bec-3f71-a292-db2687718839 | -9.1718 | -59.5211 | 2025-08-25 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b6794683-ab66-3e11-baff-81529800d962 | -5.663 | -45.136 | 2025-08-25 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8ebf3890-2322-30d8-ab48-9ebc05857746 | -3.4542 | -43.3386 | 2025-08-25 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1a34f730-1645-3c3a-82d1-4a45a0cc6e15 | -8.5943 | -62.6315 | 2025-08-25 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 18222440-24ea-3d8f-a549-25c91f2867b7 | -14.2752 | -51.966 | 2025-08-25 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8211047c-72a2-38b0-a580-30df704957f5 | -7.5862 | -47.4615 | 2025-08-25 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7ac1b243-ff7c-3ec2-9705-05ee780bf4d3 | -10.8167 | -48.3192 | 2025-08-25 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| ba634f17-f12e-38e9-b35b-e42f5f704393 | -8.8735 | -62.4305 | 2025-08-25 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 761b403b-8878-3eeb-beea-3fa27526da09 | -8.855 | -62.4313 | 2025-08-25 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7377d23e-df25-3e69-a7d0-4bdd7a33914a | -11.6089 | -46.3699 | 2025-08-25 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 46a19c56-ed3f-3f1f-89c8-e89692225402 | -14.4362 | -56.4564 | 2025-08-25 13:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a0febf78-26a5-3c1d-92e6-7473a4f566f4 | -8.5758 | -62.6323 | 2025-08-25 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 224.0 |
| c59be2e0-f9b6-3326-aef1-6be5d12315cb | -14.2157 | -58.6316 | 2025-08-25 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 35383d96-c2ca-3522-ab21-9376cac70514 | -7.5862 | -47.4615 | 2025-08-25 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 6064f9c2-d646-3107-a3eb-f886839ab617 | -8.5943 | -62.6315 | 2025-08-25 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 6aaada64-b772-39f3-9076-292c402dcb13 | -6.8201 | -59.4386 | 2025-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4bb30299-126c-320a-878d-903b3f3d2753 | -8.5759 | -62.6133 | 2025-08-25 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a1ba4950-7c95-3e9e-beca-6b72a23cb7f4 | -9.324 | -48.2633 | 2025-08-25 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 82d72eed-d690-3969-8ce7-b8083cb33fe7 | -5.6817 | -45.1347 | 2025-08-25 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c53ce5ef-c231-3b63-bacf-6ed2c5fb67f2 | -14.2159 | -58.6117 | 2025-08-25 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6cc0c66d-aa4f-366c-af07-b287824091da | -8.6313 | -62.649 | 2025-08-25 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7535233c-e832-314c-a7e8-006234b5da04 | -12.7655 | -48.1126 | 2025-08-25 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9592b3ba-b1a0-399c-b586-5b8c8156b2fa | -6.5216 | -45.343 | 2025-08-25 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 3bd3726d-964a-3ebc-8b55-1e625daab6e1 | -7.605 | -47.4599 | 2025-08-25 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 55f8af3d-3f49-396c-9804-29a0e16833cb | -12.6745 | -47.8366 | 2025-08-25 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b8abe4cc-36e9-3011-af73-a13343a52024 | -14.9247 | -45.5403 | 2025-08-25 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |
| 14745ac3-4952-3401-bf11-7126ad40d40b | -12.6937 | -47.8339 | 2025-08-25 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 5cbd5e88-3b18-37d4-ae63-a696f10bed54 | -9.5702 | -48.1724 | 2025-08-25 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a546a85a-9f7b-3cb2-a3ea-f997f2cdafed | -8.7584 | -49.9566 | 2025-08-25 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| be2c671f-5e94-334d-badd-2d05deca685c | -14.5076 | -51.914 | 2025-08-25 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 83c20e40-5b64-36fb-8d48-21e002779878 | -8.8734 | -62.4495 | 2025-08-25 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 0411616a-405a-3ef0-826c-6b084ca7cfbc | -12.952 | -46.3104 | 2025-08-25 13:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ebfa33a4-f5ca-3ca6-bc97-125f9cae725d | -11.6097 | -46.3245 | 2025-08-25 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a80eda45-fad2-3948-85cb-7ebecbe3beac | -11.6093 | -46.3472 | 2025-08-25 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 197.4 |
| af0b033e-7153-3110-a03f-a5f703819ee0 | -14.5072 | -51.9354 | 2025-08-25 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 68d7a0bd-2850-3162-afe8-06f95fa42f1e | -6.9061 | -44.4217 | 2025-08-25 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0b4a01bb-47fa-31c6-b5b8-4884f70feab7 | -14.9051 | -45.5439 | 2025-08-25 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 306a1ecd-2e90-3912-8b3e-92285b4b32ec | -11.2096 | -46.2882 | 2025-08-25 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| beaea9de-e58e-365d-ac82-9265dfd51890 | -10.5874 | -47.1527 | 2025-08-25 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 5ad19612-fa56-395d-b2df-a252b201565d | -8.8919 | -62.4487 | 2025-08-25 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 84be277b-801b-3a07-b0df-621fe7468bd9 | -7.605 | -47.4599 | 2025-08-25 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 70e09f8b-e0d2-3f47-a0fb-d756940c3f0c | -8.8919 | -62.4487 | 2025-08-25 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 61f17573-4bb8-3778-8e96-e0a695af2323 | -14.2752 | -51.966 | 2025-08-25 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 94d6be1d-e218-3a0b-bc98-36d50eaf6b21 | -8.8735 | -62.4305 | 2025-08-25 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 12d72292-6e8f-3933-8385-5db1282fd005 | -6.9061 | -44.4217 | 2025-08-25 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 2971c89e-f9ec-30e6-aa2a-7db1dd266d39 | -9.1812 | -60.7939 | 2025-08-25 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 03a5cde7-beee-345b-a5bc-0c7ed168b29b | -6.5216 | -45.343 | 2025-08-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4aa10d00-dc83-39d9-a915-80c2a8daa84f | -12.6745 | -47.8366 | 2025-08-25 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4cdb8bc1-8b78-3010-a757-9427bdfae978 | -9.324 | -48.2633 | 2025-08-25 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 54303757-cd33-34ef-9ea8-5ac48b3cdfcc | -8.5758 | -62.6323 | 2025-08-25 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 170.7 |
| f269121a-45fb-37ca-b7b5-a7f8d1b5f03a | -14.4362 | -56.4564 | 2025-08-25 13:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 75c337e3-0c5c-3034-829e-caf6e037b87b | -7.5862 | -47.4615 | 2025-08-25 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3cf41765-2e1a-3368-bca1-acebc3f8a9c5 | -11.2697 | -44.9781 | 2025-08-25 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 982ca22d-c1ba-35dc-b7d8-025aac88fa25 | -6.8201 | -59.4386 | 2025-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4056ec6e-4643-3bc9-ab15-d8c373fb4d62 | -14.5072 | -51.9354 | 2025-08-25 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| fdb1d42b-a526-33f8-902c-9c5d4d7ccaa8 | -8.8734 | -62.4495 | 2025-08-25 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| e77b3224-c3d1-3234-8c94-d6015158d900 | -11.6093 | -46.3472 | 2025-08-25 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9587d58e-1fb3-3e57-a80b-f088729c7f15 | -8.5944 | -62.6126 | 2025-08-25 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0cb80c5c-e35c-35f7-9151-5fe1038e9793 | -8.6313 | -62.649 | 2025-08-25 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 3023c904-02cc-3d55-bfde-8a08b29066a5 | -14.7722 | -45.3822 | 2025-08-25 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| cef0edd6-f49f-35e5-b39d-8487fc444352 | -8.9105 | -62.4479 | 2025-08-25 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 81c72a76-ed0e-39b5-a848-4e409bfd807a | -8.5759 | -62.6133 | 2025-08-25 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8fc1308c-1fa8-33a5-888b-c6728ce09281 | -10.8167 | -48.3192 | 2025-08-25 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9b0ef210-5d9b-3cbb-a7d9-47319f787720 | -5.6817 | -45.1347 | 2025-08-25 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |


[Clique aqui para ver as próximas entradas](README97.md)
