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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 119f01a6-e3b9-3869-be10-8785785b98ec | -6.63802 | -60.0 | 2025-08-06 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95e7b2bc-45b0-307e-8ce3-adf8206e6448 | -8.92367 | -60.56205 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1cf9988-3613-3c3b-ae0c-898cbf34d7f2 | -8.9169 | -60.55647 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e41c91b-de12-3aec-8756-e2a3e74dc3ff | -8.91708 | -60.75807 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7523b42e-497a-3859-a585-a9872466c108 | -9.47519 | -57.8488 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d5e8366-b837-37d0-9053-fd82e0ec54e3 | -7.5986 | -55.19614 | 2025-08-06 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c65589fb-891a-3321-b449-e33f8709bdc0 | -9.70706 | -61.29785 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d73a996e-5e97-351a-8f07-d46e62e0f1e2 | -8.91774 | -60.75373 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a429e142-329e-3221-af72-5ee436ba05db | -8.90489 | -60.58636 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d4b3c8d9-cd56-3054-8438-078c24a8c37b | -8.91624 | -60.56092 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7a0a0a5-e4eb-3ff3-993a-7c702d92db6c | -8.91734 | -60.57915 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2fa38ec0-2f6d-3eb8-8684-78d1d0f676ea | -9.46568 | -57.85197 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b648f1a3-5e1b-3819-90a3-22c5be7c8b39 | -6.95074 | -51.63282 | 2025-08-06 05:38:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 612fb021-7ee4-3a95-a657-f89e4661f814 | -8.9086 | -60.58692 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f859f334-bc07-351b-860d-78cdc183e7a0 | -8.91755 | -60.55203 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a918718-5ad6-368b-a99d-0aefb5aaec35 | -10.75576 | -60.74765 | 2025-08-06 05:38:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55814ae0-764e-3c3d-b122-529358cbe866 | -8.90686 | -60.57303 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c68b3d35-2d92-3a3c-be83-fa1a440ab29a | -8.90816 | -60.56422 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 82bf65c0-8cbe-31cc-b21a-a04f98f0abd1 | -6.27184 | -53.63455 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42a112d8-424e-34dc-80cc-6ff255b479f2 | -10.23296 | -56.76744 | 2025-08-06 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdea830f-9763-3ba1-90d3-4ee5523139b7 | -9.7113 | -61.2942 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33719c0d-28e5-3c00-b42c-15f4a6e67e5d | -8.90293 | -60.59969 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5e22529b-0fd9-3306-a3c9-3f0f6d7cbf02 | -9.69537 | -57.42507 | 2025-08-06 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc34f81-5f9e-3410-bd90-6836c8fab6d5 | -8.89988 | -60.59467 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e2efbb3-33f6-3a8b-b331-2dd60572f32e | -8.92105 | -60.57971 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98d8860d-5ad3-3af8-a97c-cd161827835f | -8.92192 | -60.54818 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4d81d20-d249-3d7a-a4c0-0700e9ca0a64 | -8.91904 | -60.74507 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a94c965f-1c31-38ea-bfe7-b0fb50b5f4b3 | -8.92258 | -60.54375 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f859173-5e6d-35e8-b643-8207ef804a9a | -8.90358 | -60.59524 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| db8c06ff-365a-3948-89ce-2892a0478ead | -8.91841 | -60.59748 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b0dd93b-ef66-354b-bdc9-29da61154cee | -9.93363 | -60.47557 | 2025-08-06 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e8b5c79-5cdc-3014-a697-5a1a44d8e3fe | -6.26624 | -53.63323 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c92041b1-0af0-38aa-900b-478bfb4c81c4 | -8.91077 | -60.54649 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 1bb87833-dc24-39b9-b3f2-8bad88ba2794 | -8.90203 | -60.55423 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| afebc480-056e-3daa-8503-e425a73349bf | -13.0728 | -56.8729 | 2025-08-06 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| da1535fc-48f3-3719-a57d-8c8a200a33aa | -8.9213 | -60.7489 | 2025-08-06 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 89a74956-d9e0-3062-a781-5a13d89de1d8 | -18.3847 | -52.11683 | 2025-08-06 05:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2e63c0b-95b8-32b4-9cc2-78da4123a4bc | -13.04963 | -56.87299 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 187fc1aa-3d32-38f7-8763-d615d5c19af1 | -13.06039 | -56.86851 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ef326849-5039-36ad-a8f3-f871ad4ec404 | -12.4405 | -63.70093 | 2025-08-06 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf295ad5-664a-3dba-95be-a0d347a9b185 | -13.07043 | -56.86972 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ab332387-38f0-3ccf-b14b-2f80b41a4409 | -18.39184 | -52.11796 | 2025-08-06 05:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e196bd15-da67-340f-b53b-ad38763ebb9a | -13.05965 | -56.8744 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e33ed1fd-6813-32ea-942e-b1b20eed71d4 | -13.07546 | -56.87029 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e58a25f6-2220-31f4-990c-171bcd6f86cc | -13.05611 | -56.8619 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d88e2779-27fd-36c2-983f-cd319b8031de | -17.83051 | -55.1003 | 2025-08-06 05:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7a58e53e-1bec-35b4-a6c9-327610d88496 | -13.05464 | -56.87373 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2672f4af-bd05-3c6f-af1c-0de782e9d5e7 | -18.389 | -52.11552 | 2025-08-06 05:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cee1eccd-4709-3391-bd21-2c2e3cf493c5 | -12.43713 | -63.70039 | 2025-08-06 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c99eaafd-4d53-3ced-96e3-ee20daa69ebe | -13.07621 | -56.8644 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f76fa00-ff80-3e47-a234-9307d0dd4232 | -13.0511 | -56.86116 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 185952f4-91dd-3659-b026-cdec7e9f92a0 | -13.05036 | -56.86709 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 423c63a1-542e-3eae-ab32-a04f85acb326 | -12.268 | -63.83051 | 2025-08-06 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5004b86-ddbe-343c-9221-b66f52125ea0 | -13.06541 | -56.86914 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fc20f948-84dc-35d2-91a2-9820d14eb755 | -17.83005 | -55.10485 | 2025-08-06 05:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dfeb234f-8eb1-3e5b-b81a-e87596ba88a2 | -13.06113 | -56.86258 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e7100a7c-121a-3d8e-98be-c76268d7a356 | -13.06467 | -56.87503 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d46ff5b9-8a9d-37c7-97b0-e899d120185c | -18.38526 | -52.10999 | 2025-08-06 05:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4148878-be61-3066-9f30-9a8418286fe5 | -13.05537 | -56.86783 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf2b83a6-e060-3a24-ac3a-ee9dee8c1ab6 | -13.06689 | -56.8573 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| da493152-14b7-3aec-b823-1fb710cb471c | -13.06615 | -56.86321 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a1f510e3-0e23-3838-8b86-193210b33575 | -13.07117 | -56.86383 | 2025-08-06 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2915d3a1-1790-3f15-9958-2d3372504941 | -8.9028 | -60.7498 | 2025-08-06 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0d65037d-66a5-3946-8c99-996d1c34abca | -8.9213 | -60.7489 | 2025-08-06 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 71439b72-a1fe-3236-9246-ad71cfec242d | -3.0566 | -59.9105 | 2025-08-06 05:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8b7c3064-849c-327b-aae5-2815c1b4335f | -13.0731 | -56.8527 | 2025-08-06 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 740d68b3-e8f3-381b-b74b-b930b54585d6 | -13.0728 | -56.8729 | 2025-08-06 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 4d7c1aa6-d630-373e-8791-8324aae1969a | -3.0384 | -59.9108 | 2025-08-06 05:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9a3db4ba-0836-365b-b4f3-07d91c486424 | -3.04366 | -59.9119 | 2025-08-06 05:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1a15af-b51b-33c3-b01b-60b0c89c6f6f | -3.04468 | -59.91082 | 2025-08-06 05:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb2e09f-b93c-34e1-b741-6904ad5ed6f3 | -3.04416 | -59.91441 | 2025-08-06 05:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30b8f79a-6ad1-3bee-9976-e6a075dde6d8 | -3.04311 | -59.91545 | 2025-08-06 05:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9be2ba7-3432-3ed4-873f-fc884506bf30 | -3.0384 | -59.9108 | 2025-08-06 06:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0c37112a-be1d-3457-bb99-154fd3e12ca9 | -8.9215 | -60.7297 | 2025-08-06 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 11fab665-51e1-32f7-a715-eb020881b75e | -8.9213 | -60.7489 | 2025-08-06 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8cd5e418-7af7-38fc-b47a-101f0850b02e | -3.0566 | -59.9105 | 2025-08-06 06:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f59455f0-845c-331c-86ee-25759471f693 | -8.91838 | -60.56348 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a543ede-35f2-3923-80d6-6685cf65e73a | -8.91531 | -60.74113 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 648b6a28-f3bc-3689-ab3f-b81684255dff | -9.93495 | -60.4782 | 2025-08-06 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08dfb2ef-dd0f-3166-8eb0-26d012295321 | -8.92146 | -60.73793 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f0d3a958-c688-351d-bea0-359be7a7b2f2 | -8.91364 | -60.59913 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 236b7d04-00cd-3b9e-b1f4-188f64c649b0 | -8.91476 | -60.54694 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4afa400b-33a0-3b30-8118-3ca9b37b7be0 | -8.91385 | -60.7526 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af3c1f38-64c7-3d0f-9523-a407891987aa | -8.92097 | -60.74174 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 09acb351-e845-3dec-b636-171d87232368 | -8.90901 | -60.59035 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e55dee62-ace5-3f03-9e45-f5489fa6f2dc | -8.91902 | -60.75708 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c5fa258-b18d-300d-bebc-9ea461a6a5bc | -8.90173 | -60.60156 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b19fbd2f-ecfe-3354-b2b1-1ec6d70c654f | -8.90226 | -60.59755 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e24632a5-cbe8-3597-8555-3479a2d1a473 | -8.91165 | -60.57045 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c856a3f2-28aa-34d0-be96-3aee850b74d7 | -8.90691 | -60.60622 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8797082f-8ac2-3665-8692-9709ff84624d | -8.91767 | -60.74138 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aa9ff197-e410-360d-8d23-50eaf9a5e5ae | -8.90331 | -60.58958 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 253ab8e0-4fc1-3fdf-ad25-0fce035a8036 | -8.91613 | -60.75283 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 87201b44-6a34-3f2e-b8ec-43bcefd73a9f | -8.91471 | -60.59112 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e315604e-8aaa-3ed1-aed5-a797c7beab02 | -9.18 | -60.82998 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b7777f-313d-383e-9bdd-133b4e7cfb9e | -10.22263 | -59.41524 | 2025-08-06 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a7ff4a4-5307-3b15-aff7-9c92a42d6e39 | -8.92468 | -60.57598 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4938f1f-b35a-3e44-a2d0-ca079d4fa0df | -9.46559 | -57.84906 | 2025-08-06 06:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d4c70d8-cf3d-3e32-99f7-bc617c052480 | -8.91716 | -60.7452 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 18d916aa-bee1-3e8e-ab59-89a6e2b70d98 | -8.90848 | -60.59438 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |


[Clique aqui para ver as próximas entradas](README29.md)
