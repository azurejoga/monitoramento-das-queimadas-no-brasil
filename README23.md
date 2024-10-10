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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12d7e4fb-6ad7-3cfe-a912-3789305d378b | -8.6123 | -54.580799 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7625789b-b262-3054-8a5f-1723a30dd0a3 | -8.6139 | -54.587898 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c065810b-c9f1-3fe1-ab63-b0596d97fbca | -8.6155 | -54.5951 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1e09a3-4f03-3def-ae85-9617139d0776 | -9.8624 | -60.288101 | 2024-10-10 01:06:04 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d84366ef-650c-3475-afe3-7ac4ba9828a4 | -9.8645 | -60.298302 | 2024-10-10 01:06:04 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1961f8af-500c-3130-a41a-da9eba4fe605 | -8.6025 | -54.583099 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 683cada9-2f11-3974-bc55-7467eb76677a | -8.6041 | -54.590199 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5987791-2c3a-3a3b-b16d-8fb535742fb5 | -8.6057 | -54.597301 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471d032d-a8d0-3c39-9ced-c97ad2657ff5 | -9.8548 | -60.3004 | 2024-10-10 01:06:04 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 428ea5d3-9549-3521-9833-c37a5d17f6c6 | -10.3707 | -61.2513 | 2024-10-10 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 77a0605f-e51f-36f0-a6c3-30125457c049 | -10.3708 | -61.232 | 2024-10-10 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 394125a6-ba2c-30d3-ac24-208e5b5cd37c | -9.4403 | -58.927502 | 2024-10-10 01:06:06 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1c66bf9-37c2-3cc0-96d0-f992a92951a5 | -9.4421 | -58.935902 | 2024-10-10 01:06:06 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7159d21a-396d-3ecc-b8c5-cb18dd639cf5 | -10.6258 | -55.8953 | 2024-10-10 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 899f18aa-235a-3fdf-9eb7-229b0276a9ca | -7.1461 | -49.434601 | 2024-10-10 01:06:08 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cca308b3-136b-315c-b7f7-dd02940aabca | -8.4854 | -55.157299 | 2024-10-10 01:06:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 079bfb8a-c2ec-37af-8f82-0eaf7c9fc1e5 | -7.1364 | -49.437 | 2024-10-10 01:06:08 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8a28149-ac80-3fc7-b299-15b9707b40f1 | -11.0252 | -57.2436 | 2024-10-10 01:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| acd4befc-a890-336c-8dfb-e25d2345005a | -11.0254 | -57.2237 | 2024-10-10 01:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 258.9 |
| 5f62a423-c968-3ee1-b84e-aa6155f2156c | -11.0256 | -57.2038 | 2024-10-10 01:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 272.9 |
| d5976bdb-d02c-33b6-ac81-72874e01a0e8 | -11.0443 | -57.2222 | 2024-10-10 01:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 8338b1b4-db4b-3b92-af37-1dc735cc7583 | -11.0445 | -57.2023 | 2024-10-10 01:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 7e5608cb-d775-3bc6-9d1f-875dbf3d1732 | -8.4372 | -55.445499 | 2024-10-10 01:06:10 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fdcf0d-c726-32c9-9994-d06576161374 | -8.4387 | -55.4524 | 2024-10-10 01:06:10 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 435f758a-2560-3489-ba0b-7a9c14827b65 | -8.4403 | -55.459301 | 2024-10-10 01:06:10 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0cb211-57ca-320d-9e3d-58035b8fe40f | -8.4305 | -55.461498 | 2024-10-10 01:06:10 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1683e75-fe63-3e20-a079-30bb13a7e252 | -9.1836 | -58.8778 | 2024-10-10 01:06:10 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bea5569e-eb2d-3f94-8abf-73778df1d766 | -6.5678 | -47.692402 | 2024-10-10 01:06:10 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b45e014-d133-3391-8145-6acc1260dbba | -11.277 | -60.4067 | 2024-10-10 01:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9da9d016-79ba-31fd-b4a5-33987ddb29b0 | -8.2878 | -55.377399 | 2024-10-10 01:06:12 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988bbcf3-49be-394b-ac20-f27678bad12c | -5.8889 | -45.366699 | 2024-10-10 01:06:12 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2529abbf-3221-387c-95bf-f24778c85292 | -5.8957 | -45.393799 | 2024-10-10 01:06:12 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78bfe63f-f81d-39fa-b48a-ec95dcdbafda | -5.9024 | -45.420799 | 2024-10-10 01:06:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45ecfa81-5b0a-3098-adc1-418bdf3da614 | -8.2764 | -55.3727 | 2024-10-10 01:06:12 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0e6544-58b2-364f-a445-7f7899909f4b | -8.278 | -55.3797 | 2024-10-10 01:06:12 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c33f43e-eac4-38b3-93b3-7009e167e1bc | -5.8793 | -45.369202 | 2024-10-10 01:06:12 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc31db21-3fc3-37f7-8b47-139f8d04d78c | -5.8861 | -45.396301 | 2024-10-10 01:06:12 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8399ddf9-5c3f-3d37-801b-f47ea272b332 | -5.8928 | -45.423302 | 2024-10-10 01:06:12 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44827941-21f1-338e-adeb-9d1508049edb | -8.2157 | -55.240501 | 2024-10-10 01:06:12 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf97590d-d04e-3fda-83dd-ae71b3da33a8 | -9.2086 | -59.760201 | 2024-10-10 01:06:12 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50ab86a4-3c01-3e8d-84b7-30601259ba60 | -8.1364 | -55.163399 | 2024-10-10 01:06:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd95bd63-0760-3314-99b8-75654bb7392f | -8.138 | -55.1703 | 2024-10-10 01:06:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eefd847-c24d-3ad5-b99f-bafb7ac9f49c | -11.8188 | -58.8459 | 2024-10-10 01:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f9217770-36db-3164-990f-e94c5c2431c4 | -9.3845 | -61.029499 | 2024-10-10 01:06:14 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48acde2c-ba8a-3d80-8da7-831ecb92c142 | -5.4618 | -44.234699 | 2024-10-10 01:06:14 | METOP-B | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 240b6bf9-5785-3ec2-9bff-e1550b91b2da | -5.4701 | -44.267601 | 2024-10-10 01:06:14 | METOP-B | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9591f1de-2783-3b55-8882-add4cc513445 | -9.2446 | -60.460999 | 2024-10-10 01:06:14 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 454164ce-3c59-37c3-bfcc-dfaa47fd92ec | -6.0323 | -46.559898 | 2024-10-10 01:06:14 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ccd6f04-5911-3759-866a-474918798c12 | -6.0378 | -46.582199 | 2024-10-10 01:06:14 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7c8c928-890e-3e8b-ba2e-c04205b90759 | -12.2888 | -43.7495 | 2024-10-10 01:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 311ca0e1-ae68-3d71-abf7-2d65617b6360 | -12.2893 | -43.7258 | 2024-10-10 01:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 6b25993c-d080-393f-963a-d468762309af | -6.0282 | -46.584599 | 2024-10-10 01:06:15 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53e69822-5518-36f9-90ed-a9ad2d171c76 | -7.9574 | -54.737999 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4354d259-2a81-3c23-b2e3-61ce26e19394 | -7.9476 | -54.7402 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77c2d75-6ebe-3a1d-bd76-1758b84c7ea4 | -7.9508 | -54.754398 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c52a82fa-3c9f-3c3e-b1e0-6f3ed272963d | -7.9524 | -54.761501 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14d297f5-b1fa-3f6a-9327-d275851421bb | -7.954 | -54.7686 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a972cd-3591-3b1d-9d58-6e81e93e6163 | -7.9556 | -54.7757 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e844d0c9-05f9-3910-ba1b-7d52fb40964c | -7.9653 | -54.818199 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f15da64-0a6f-3098-b529-2ffaaaa9ca20 | -7.9669 | -54.825298 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b68a05-a926-383c-94bf-c4b330473527 | -7.9426 | -54.763802 | 2024-10-10 01:06:15 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61c879e-fd83-3bdf-ae8c-cfe000fc52a4 | -12.4177 | -54.5797 | 2024-10-10 01:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b49bafb0-4a03-3bea-b23c-fd157afb6d0b | -12.418 | -54.5592 | 2024-10-10 01:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d86aac3e-1cca-3193-9612-6c20303dd73a | -7.8186 | -54.7173 | 2024-10-10 01:06:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef0a587-57be-303c-8c5a-2e43c33a8534 | -7.8557 | -54.880402 | 2024-10-10 01:06:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9474dea2-fcb4-3977-bba8-a937b2d66f73 | -7.8573 | -54.887402 | 2024-10-10 01:06:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be313fd4-84e5-3020-9168-d68e170791bc | -7.8589 | -54.894501 | 2024-10-10 01:06:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b702f642-9d1d-33b2-9ec2-1fc947a3b6b8 | -7.8475 | -54.889702 | 2024-10-10 01:06:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b4868b-f14a-36e6-8524-9070b3e71608 | -12.9255 | -51.1361 | 2024-10-10 01:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8ce70c77-6d35-3a4d-a63e-6bf333d9bd56 | -9.1264 | -61.259201 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01c85daa-8a3e-36f3-b66a-3debd398feea | -9.1142 | -61.249901 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 049e1f75-9165-37f5-bf93-350f62530c2d | -9.1166 | -61.261299 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2c5ef5-ac2e-3d74-a2f0-3cb5f60e9e67 | -9.119 | -61.272598 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 397b1997-510e-3654-92cc-bbf2740f9159 | -9.0785 | -61.128399 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebaa2279-de3c-310e-bb96-983eaa3d4a23 | -9.0809 | -61.1395 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce1a9cdd-51e9-3936-b420-8b7c35dd82fc | -9.0832 | -61.1507 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9400e5-d89f-33ae-a7b7-cc90c1c8a8ae | -9.1044 | -61.2519 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4b31fc0-8a85-3c88-9ad2-10ec1ce2d19b | -9.1068 | -61.263302 | 2024-10-10 01:06:19 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd260d21-247b-3f43-a29c-13f680ca5fc4 | -5.6924 | -46.4268 | 2024-10-10 01:06:19 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 023c4d65-4272-390f-bed2-a8ae9750ca9e | -5.6827 | -46.429199 | 2024-10-10 01:06:20 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62770633-8a7f-3661-bbb1-ec76a4072051 | -7.6763 | -54.817001 | 2024-10-10 01:06:20 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e84e3580-2a14-306f-ab6e-cdd69bf0e3e9 | -7.6779 | -54.8241 | 2024-10-10 01:06:20 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a6734a-4f55-3949-aff7-755405c0c326 | -9.0893 | -61.3745 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a87bbc4e-33e2-32dc-883b-81ee866a68b9 | -9.0771 | -61.365002 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67386c76-3d96-3ce4-9c90-f35493091de7 | -9.0795 | -61.376499 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0fa403c-75ea-3440-b508-8e0559d83be0 | -9.0819 | -61.3881 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 644ce3b8-c4b3-3877-a962-429d461e2dd5 | -9.0673 | -61.3671 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff529f5-ef45-3aaa-9ac9-f96bbaa51085 | -9.0697 | -61.378601 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76948f09-dfd3-3e95-8cfc-aa2e2ff47906 | -5.2192 | -44.7691 | 2024-10-10 01:06:20 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad145bc-479d-3b8e-9167-e3256b2dce84 | -9.0551 | -61.357601 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd1bb9ed-ba8e-33c4-9b6e-23114860336d | -9.0575 | -61.369099 | 2024-10-10 01:06:20 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37b0e880-d84d-332e-8c86-1a8253196daa | -13.1845 | -51.7004 | 2024-10-10 01:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ef2c927b-15ec-39c6-9cc7-76fafc5398e8 | -5.2096 | -44.7715 | 2024-10-10 01:06:21 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5707278a-8c33-39a8-8eb3-7a0a3bf53960 | -8.3605 | -58.159599 | 2024-10-10 01:06:21 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 851b0c28-f2f5-3ddc-8dc6-2d47044bf5ff | -5.8268 | -47.390701 | 2024-10-10 01:06:21 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f3898f2-b8c3-35ef-835a-af8a42e90101 | -5.8317 | -47.4104 | 2024-10-10 01:06:21 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4dfec7d7-eac6-36da-8d75-d6098e586ffa | -5.8172 | -47.393101 | 2024-10-10 01:06:21 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b969f0e-3f63-3b6b-b956-b2c210e88e84 | -5.8221 | -47.4128 | 2024-10-10 01:06:21 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5708b9f8-ce54-3db0-83a8-f830c650f14f | -5.1823 | -44.9072 | 2024-10-10 01:06:22 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc83c0cd-b6c5-394a-91b6-5ac7a809c047 | -9.0209 | -61.584301 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
