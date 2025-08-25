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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89f74684-e6cd-3c83-a847-238217ecf481 | -9.1507 | -59.48029 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5413553b-300c-35ee-9d88-770b083c9c21 | -8.65182 | -63.43389 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df2bf81-93ef-3d6a-bc85-671ab970a1b2 | -7.54172 | -63.85889 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aebc08d-60f6-3ab9-8683-dbf493d787a5 | -9.0035 | -65.38603 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 643e87ec-29da-308f-9b74-157285303665 | -10.41979 | -64.43571 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2cd3f0a-4ca4-370b-8cd8-ec7d30e132f2 | -8.98764 | -65.41595 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1c3a67a7-5d57-3b46-b964-1f4ecd5b9855 | -6.68699 | -58.85718 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdc1b0a5-4b20-3e81-b369-1e7e00bb7ac1 | -8.56726 | -63.92632 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 956fb1ec-4a25-35b0-91fc-1e0dead410bc | -8.89653 | -62.45362 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ada614e-728c-3265-ac9b-b58c0deb5d7c | -7.72832 | -67.06687 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57439462-9bfd-356c-a2b3-796b9858e27f | -9.01923 | -65.70853 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39940244-d87b-3084-8ffb-61236a4044c5 | -6.35911 | -57.96642 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 756dac26-6b6d-355e-b323-bff34d75cef0 | -8.5088 | -63.86935 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dae8eb6-3ffd-32ec-9877-a030c9037f71 | -7.9051 | -63.06269 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ae55d305-3db5-3d03-b842-42d62565d28e | -9.17376 | -60.8098 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03eba9a6-9800-3ba6-95a7-d799068fc0cf | -11.6972 | -60.17601 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9114e250-83c6-380f-82b4-8d42134806c5 | -8.12235 | -62.86558 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9291e5b-857f-30d3-9e8c-6ca9fb2dba77 | -9.16201 | -59.52327 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e1591a-2287-3306-bc44-91921fd578f7 | -8.59536 | -62.59652 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 325de702-ddfa-3f06-8a47-4bb47e5de12b | -8.99255 | -63.65068 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 016e7888-87e7-3082-93da-5c043482d5ba | -8.65633 | -63.42817 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45867889-540a-3d97-99de-c68683cd8deb | -9.18138 | -59.4561 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 325b972b-d102-3d82-bc09-7bad282f6e6a | -9.15867 | -59.46259 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3215415-6923-3f69-9c7b-7c07e86e47b1 | -8.88743 | -62.40828 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfe05a04-8e81-374c-82f5-09164778a8a2 | -6.83173 | -58.94584 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e08c9c0-0f11-3ce1-a71a-157c1ce93031 | -8.89323 | -62.46534 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 715db0a1-5e1a-33a4-9264-abe4c82f78e1 | -6.83072 | -58.9534 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f68c6aa-6f84-35b6-b287-c4366f3ef8c8 | -8.87839 | -62.43982 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc0c9b4b-1c06-3dcb-aa7a-8e3796b3b4b8 | -8.9144 | -62.42349 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1210e555-9231-3465-81e2-31e8d6042268 | -9.11709 | -67.91967 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eef12cb0-bb7b-353e-8dd7-db15fc3ac13b | -5.79286 | -59.22346 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff1e892a-fe7d-3e39-9dd7-a40cd05eb97d | -9.18647 | -59.4607 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e73246d-06b1-351b-ade5-e5ad42b811ad | -9.04607 | -65.73034 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a2735c45-5448-3f59-ab0d-e1d517f55f18 | -8.19573 | -61.40408 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b7963ee-5c4c-356a-9052-07bb3aeb5a22 | -8.10702 | -62.88032 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce6ba159-972d-3663-8b89-86bf94276c90 | -8.60872 | -62.59846 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91b53172-e77e-3405-b32d-5fcd714e1b45 | -8.90043 | -62.45885 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9db48deb-d815-3017-b32e-00c9d4b306db | -10.4629 | -59.13094 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92e24472-2d4b-3275-930a-25e3d7618349 | -7.54524 | -63.86303 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9faab12f-2714-3468-a72e-ee2cb0514c9a | -10.09009 | -67.95354 | 2025-08-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfcd24ce-ed7b-32d1-bfad-da43f5dbbd74 | -8.51645 | -63.8742 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53bc411a-618d-3de1-9356-4bf5b7529464 | -8.88421 | -62.46404 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d9eacc2-ca86-32c8-b086-86ba3ce59ee3 | -9.20464 | -60.92116 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4699094-4980-3d78-9f8c-727c2ceda6ae | -9.81302 | -64.25764 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93992cd0-4e73-313a-8cc2-8d8a9164bc04 | -7.66144 | -63.52034 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91833073-4428-3731-84cf-d0936e2b0c2e | -7.71945 | -66.91647 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f30a91d6-f995-37b1-99bc-5a0a3500fd73 | -9.1553 | -59.48837 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769a6cc9-b876-3fe7-9397-d7b15356c475 | -8.63367 | -62.64714 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3db1a68-344c-31f4-b1ac-e53c8d61bbbf | -9.81707 | -64.25823 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f5367d8-3244-32eb-9cf4-1876b74fb3fa | -6.93184 | -62.98005 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff4b0db-1250-39da-b01b-07682b765bde | -8.88678 | -62.44572 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f227df8-ea4a-378f-be0d-bfc785c372c5 | -9.19017 | -59.47636 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 466b3ba3-aa34-3b36-b4d5-1b1155506f34 | -9.17154 | -59.62106 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecd7512d-916a-3017-b593-5d74efe2d74e | -8.47523 | -63.93121 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f87e89-c015-321f-bced-39621245bb4a | -10.09935 | -57.76574 | 2025-08-25 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aeaa2d3-25ff-3af4-8ca9-0d4396a2789b | -9.07131 | -65.71204 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c973e5-a066-315e-8003-e62b1d876676 | -12.05919 | -63.15244 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 669c1446-43a1-3096-a827-ba2f33a2b808 | -9.19991 | -60.92236 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca500db3-2a74-3bb4-b34a-babc012d6e22 | -8.90166 | -62.44967 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a813c208-5041-3fd1-a034-01b4826449e2 | -8.12118 | -62.87394 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69d3ccf2-e53f-34d2-bed3-f685b10e4f28 | -7.57134 | -63.44188 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a76ec9-9a79-38aa-a4bd-7805f5efdd50 | -9.16941 | -59.59496 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27bd060-3b52-3bc1-8698-1063a054ddc0 | -9.15213 | -59.4693 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5651ce00-4f17-35af-b276-9e7ae19b33a8 | -9.17177 | -60.82479 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48f9affd-f4ec-366a-aa53-438993783d36 | -9.15432 | -59.49585 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdfa9756-6762-3d14-af59-c41b838d07ae | -8.10441 | -62.86716 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82fc9b9f-4373-3ca1-bfe6-775e938ddb4a | -8.61132 | -62.61243 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a3b0e06-5d28-3f6e-8401-fba925cf9504 | -9.04304 | -65.7254 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 176bd821-8104-3509-8fdb-b5190587647b | -8.12177 | -62.86976 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f71f736-2e89-3dc5-b030-ffc7fdf41254 | -6.84184 | -58.9551 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79cffee2-e08b-3e57-8c77-162555eec47c | -8.97951 | -65.41932 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0e41e8f0-d4be-3f1f-9eb7-1c5d8abaa509 | -8.1206 | -62.87811 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6bae2e84-2d94-3f83-bbc4-650ed290e6f9 | -9.2017 | -59.51932 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ef3bbf8-281c-3190-b95a-ba10723938ba | -8.89079 | -62.46213 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 039f5c70-cdf1-3009-b59c-6f6a62b497d7 | -9.01607 | -65.37861 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3201d838-cf31-3c93-9a52-b9331cfe724e | -8.13479 | -62.87167 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fdf001b-6f74-3337-b052-7be5423f3a84 | -9.20263 | -59.51198 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d45f122-c941-32a5-809b-758b8be49374 | -10.29833 | -64.50211 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b3f25d2-69bb-3df2-b100-b9bda2159f39 | -8.63491 | -62.63831 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84bb5ea-bf26-31ad-8671-b52f3e986fff | -9.20932 | -60.92476 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfb88464-e23d-31a2-96a0-f0797cb83579 | -9.19418 | -59.62283 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3407b44f-fae4-354b-8d2f-0363cc8a48fd | -9.19005 | -59.4821 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f414d91-13c5-375d-9989-33ee94d9ddc1 | -9.00858 | -65.3775 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f0d43369-7979-3f25-9240-71c40aa73721 | -9.19911 | -60.92827 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb763105-637a-333d-830b-903776f60d8c | -7.53114 | -63.81736 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e92777e-616b-3529-b472-4728d503ad58 | -9.2224 | -59.70742 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 622db1f4-f3f0-3966-91cb-7f1cd3e518da | -8.62282 | -62.62757 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80046e05-24f7-3afe-a73f-4c440f2e2539 | -9.21741 | -59.70298 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20328a36-bb37-3c5a-b0ae-8404dea79436 | -9.23569 | -60.91948 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb6a0308-b61b-3574-98dc-ca767766a766 | -9.15409 | -59.45425 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd63c4a8-37ba-3221-a5b7-7281ac5f530f | -9.00216 | -65.39509 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b9b964c-98a4-3319-b7e6-e3af5f916a37 | -9.19772 | -60.78547 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 094187ed-8e02-3a45-ae16-aae97ed83d7c | -10.41929 | -64.4393 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f705edf-284d-3cde-b729-6c880f569da3 | -9.18744 | -59.45911 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 31d80c15-8140-3408-802b-810e759f47a6 | -9.19896 | -59.4964 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fba93d5f-70bb-3719-b2dc-c48dc01c3090 | -9.21465 | -60.92733 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 204272df-9ca8-324c-914c-d0b1ffe3e773 | -13.06002 | -56.92229 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 492b2003-fb1e-348a-9989-6d367d9bb1a5 | -7.89969 | -63.0701 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| cf86363f-df75-3908-919d-a5c4dc4e86e2 | -6.81304 | -58.95832 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff8b1104-daa9-301f-afd8-4cdcb68e955f | -9.04542 | -65.7347 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README85.md)
