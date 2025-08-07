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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bb84c2c-3f10-322f-9a9f-d1e08bc623cb | -9.70697 | -61.29789 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c61a4ec7-993f-3445-ac0b-f8c6123eccaa | -9.94288 | -60.4695 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 056e1525-79bd-3d02-a635-246686961270 | -8.92122 | -60.75877 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a2c89616-ebe6-324b-adde-5106a13972b3 | -9.71159 | -61.29108 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 297ac15d-845d-3f8d-8fa8-6ba6fcd6580f | -11.67888 | -61.16719 | 2025-08-07 05:21:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e85cec4b-7ce3-3cf6-a416-ec6f1b29fac0 | -9.71098 | -61.29477 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 191da639-e5c4-36e6-a2c9-d3032d01fbff | -8.91899 | -60.57049 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7402416f-1ad8-336d-908e-8e2f745e51f9 | -8.92285 | -60.58947 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fee13c5-d601-3957-851e-e98cddcd80d9 | -8.91277 | -60.58783 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bed10ebf-357b-3fd7-9963-70f9c32bb48b | -8.91272 | -60.73905 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60793652-8e3e-3a18-8e47-ab5eedcb82e4 | -8.90392 | -60.55703 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef04e6d-0786-333e-ae59-3f835a9609ef | -8.9218 | -60.75517 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9a77f5e9-8c48-3e88-bccf-50bfeaa46116 | -8.90998 | -60.5837 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15e6b8fd-3505-3443-8258-27b039bc757b | -9.93498 | -60.4973 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33a63d94-f0e5-352f-9f26-1cea01a80c3d | -12.51771 | -47.15061 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efe08f69-142e-3119-a976-8f477e447e30 | -12.5334 | -47.14547 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78bcc7e9-834c-3661-a86f-446f40a5ab5e | -8.92071 | -60.55974 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539e9569-8842-37d9-bd89-8b698e8f6cc4 | -8.92522 | -60.55314 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72bd222a-e31f-3c24-8b86-afd85802877f | -8.92298 | -60.74794 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 15ddc227-b169-3855-9597-e30e831b57c5 | -8.91506 | -60.75406 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6af1f99d-3fe0-3c3a-9870-3cd8c904e0dd | -12.34349 | -46.06425 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ba134aa-8696-32c0-8427-b38d4a17aae1 | -8.91015 | -60.53968 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b766bee-2fe1-307b-8e37-96067f9cfdf7 | -10.63826 | -55.3122 | 2025-08-07 05:21:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7c1f07e-13fd-3952-be57-fbddefb49e97 | -8.90719 | -60.57958 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2dbc22c-e684-312e-a229-d48ed78e1fe1 | -9.93384 | -60.50438 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1f8529c-bb2c-37ce-8495-3ec048b1b1c9 | -7.40981 | -60.01025 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4bdbf1e5-565c-3c3a-8f6e-caa86cf9ba45 | -8.9094 | -60.58728 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a41483-46e0-38ce-8237-7216f7eb642b | -8.91682 | -60.74322 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7a2d8467-4d37-3d12-b92e-aa6026379568 | -9.93832 | -60.49785 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce8f3277-2575-3ba4-bb9b-ab6ac1b90ee7 | -11.77881 | -62.67976 | 2025-08-07 05:21:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefb8244-b49b-31cc-8215-3381df37f0b9 | -14.39124 | -51.04809 | 2025-08-07 05:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a2b7981-1c6a-3dc9-b832-a34cd7796dbe | -8.92022 | -60.54131 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6345ca67-4059-307e-97b3-de58c30fa8ab | -9.93441 | -60.50084 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f6015ed-6298-377d-bdc4-71295d35e72e | -8.91383 | -60.60268 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4467d0-4bd1-3dee-8d4a-d0fe8a3bda87 | -9.93946 | -60.49075 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 751f2b65-3d24-3529-8c47-2a6c24054741 | -8.91457 | -60.55508 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a9c6d74-2396-3896-a1cb-9f9a81b3da59 | -9.93257 | -60.47899 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64d604b0-9d71-30c8-bb4c-f1d178033ed9 | -8.91785 | -60.75821 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a1e0da2-ff32-3b70-93a3-061da325bcfc | -9.93221 | -60.4932 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e27ee60e-d6e2-3ba9-9759-6ef127b1a9fb | -14.35699 | -51.09604 | 2025-08-07 05:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96d1661d-9c1c-3e12-abc9-8d32b5e8e88e | -8.92292 | -60.56746 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5d79ee1-2652-39d3-bb71-ede6170b1ffb | -14.38576 | -51.04732 | 2025-08-07 05:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc96351-63fe-3c89-8d3c-99950aee2ae5 | -8.91949 | -60.58891 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb490549-7763-389c-bb46-0a462e3cf663 | -10.05557 | -64.99663 | 2025-08-07 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eb00ac4-fe02-3a2a-a2a7-dc59f5badfd4 | -12.51161 | -47.14342 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa794e58-458f-3205-a5c9-40db4d6250ab | -8.90547 | -60.59031 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 674739a6-ef03-3c48-a67b-d19dbc248b96 | -8.90507 | -60.54987 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| aee11ed6-b22b-3f2e-9456-08d769da72d0 | -7.40862 | -60.00674 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 341ceee9-8bb7-3b94-b960-c58cf9b76bb6 | -8.92449 | -60.60074 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 663cb1bd-f1b3-3bb8-8f35-405032f8289c | -8.90317 | -60.60462 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41105d4c-8206-3278-a05c-b5958b96ba7f | -9.94052 | -60.50548 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c57ce7e-397a-39a3-8502-93023808e9f5 | -8.90653 | -60.60516 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de85877b-888a-3bb3-a3da-4d43d0b307be | -8.92137 | -60.73656 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 897730aa-a187-3d72-a7ce-40222d46fcf6 | -8.91961 | -60.74739 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5a0a91bb-c5b4-3bd8-b38e-8f78dfed8b10 | -7.4075 | -60.01381 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8f714c50-0881-36c6-9fd4-21a96cb65d66 | -12.70399 | -46.38879 | 2025-08-07 05:21:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d0e2599-798b-3f1b-ac93-b48b74280a4e | -9.93621 | -60.4684 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ab02e1c-cd84-3759-bf61-207facecea0b | -10.83579 | -54.01582 | 2025-08-07 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 135beb75-6887-38cc-97e0-0a2d0d232a04 | -9.9354 | -60.46127 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d80bc5b1-558a-39aa-a9a5-fe848fa29dc7 | -9.92928 | -60.45663 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e19235d-1797-3a74-b1d3-7af550f8f866 | -8.91285 | -60.56581 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a20998d0-35e5-3b11-8104-cc23135f7268 | -8.9049 | -60.59388 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b685bee5-0df9-3da7-83d1-1f599e5f311a | -8.91667 | -60.736 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df9fcd8-5f6f-32e2-8090-ce85a5be6ce3 | -8.918 | -60.73601 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0adca428-ec56-39b0-8dae-1af251d020e5 | -8.91121 | -60.55454 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a8cce4c-bd33-3090-904f-875314013e3b | -9.93718 | -60.50493 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12e4b94d-e2f1-3a8c-8889-bbece6286a62 | -9.60343 | -63.46044 | 2025-08-07 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d202f8f-aa11-3896-bc1d-b41119cc7809 | -9.93278 | -60.48966 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37976baa-2b88-3cf4-91dd-800e9d7203a0 | -13.72487 | -53.86694 | 2025-08-07 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 622a4259-bdd6-3944-a8b5-6e6fe2deb4a7 | -8.9217 | -60.59662 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b10151-d065-3d53-a3d6-7e0a026790f6 | -8.90891 | -60.56886 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8029a500-434c-3082-8a36-2bf5ebba475f | -12.34428 | -46.0568 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94e412ee-f61f-3937-9928-13627986c9ef | -8.92415 | -60.74072 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c2478cea-3c03-3218-957d-7ee30d7d4a6a | -9.92872 | -60.46017 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 087a5c58-62b5-388e-a0b1-b5e3d77d6afb | -8.91842 | -60.57407 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02376e6-18e0-392e-902b-2f7de093a08b | -12.32977 | -46.05501 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07fc5ccf-49f7-323c-ac93-e3b61479577a | -8.90777 | -60.576 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d61328ac-5e92-39df-9d4e-0694beb80c23 | -13.05917 | -56.85678 | 2025-08-07 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d61ab3-00e0-340f-a5db-21cf8a2fc4be | -8.91436 | -60.75043 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7fc9830-a2ba-3266-8ff6-a5e78c5b7c09 | -8.91334 | -60.58425 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a3ea8a4-43ff-3ecc-a95e-0342e02a0908 | -8.90564 | -60.5463 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14bdd95a-07ff-39be-9a72-991ab9292570 | -7.436 | -60.01806 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bac49789-388a-310a-9150-0274dfabf237 | -8.9212 | -60.5782 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9717455-cafe-3bbd-90d9-5f9aaf219550 | -7.41372 | -60.00725 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78f58f27-dc00-3665-80ef-93b81eb3a955 | -12.71904 | -46.38349 | 2025-08-07 05:21:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5130b33-b1af-3caa-a076-5be312d8b9ca | -10.09758 | -63.18932 | 2025-08-07 05:21:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62e9c2ea-1335-3193-a8d6-ee2c0c4d24b3 | -8.90958 | -60.54325 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd894a5c-dfa5-395f-8cf4-6284fdceeb18 | -9.94402 | -60.46241 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b75ce6d1-676d-3822-a619-1d676329af73 | -8.91293 | -60.54379 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa682af4-560c-3255-8b94-08d8fc836944 | -9.93149 | -60.46426 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19745337-05f2-304c-ac27-bf91b95997ca | -9.93792 | -60.45778 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 608e7644-92b4-3755-b4e7-e92cfd93268a | -9.93555 | -60.49376 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35060779-2d54-3793-81ab-a05de7425ce0 | -9.94125 | -60.45833 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b6f6abb-c335-35a1-8f0b-9e617b613f93 | -8.91555 | -60.59194 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adfba81a-5de0-30b5-8c92-4ae973efa000 | -9.92975 | -60.49671 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67c5c1af-5acd-3050-9fb8-ff65365de87e | -14.50611 | -52.77376 | 2025-08-07 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf1a7b3d-8482-325f-9b5e-982ef8e7a910 | -8.91162 | -60.59497 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7be76ea-c986-373e-b411-8c4eeab86088 | -9.46924 | -57.84808 | 2025-08-07 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6425ab8d-f7d3-3cc0-a85f-9e9164ecd921 | -8.91621 | -60.56636 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd1d501-af0a-38df-94e6-0f6f208353e5 | -8.92113 | -60.6002 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
