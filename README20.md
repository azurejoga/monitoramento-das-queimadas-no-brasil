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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce36aa08-87ed-34f6-9389-bece5f45c728 | -9.4257 | -60.416 | 2026-08-20 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e3b5752a-4dd1-3562-8b89-ede6e6000928 | -9.2071 | -59.771 | 2026-08-20 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2ea3dcd9-f89b-37e1-b615-aecd6f40a24a | -9.4256 | -60.4353 | 2026-08-20 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4308e5fc-10a9-36b6-b09e-a8b5c830a02e | -7.3413 | -45.8377 | 2026-08-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 60fe3c96-250d-3f81-b45a-c32d85f26d32 | -17.3365 | -43.6383 | 2026-08-20 02:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 075c5fcd-e27b-3695-b974-f14f4f8ba8fd | -17.3372 | -43.6139 | 2026-08-20 02:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 172.8 |
| f07d6bb2-7c6e-3b27-a0d6-3c0f66152e5e | -9.2258 | -59.77 | 2026-08-20 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1b0dc123-4c74-3866-8815-0b23b64b42f8 | -11.2191 | -55.0382 | 2026-08-20 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 362a285b-5d52-3441-9acc-e87db21529c5 | -7.9751 | -44.6648 | 2026-08-20 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 745ebbee-fb5f-3f57-b60a-d358922476d8 | -7.3415 | -45.8152 | 2026-08-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 17797f92-b7fd-3e1b-a8fd-768873c439d8 | -9.12 | -61.6011 | 2026-08-20 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 172e07f5-c779-32b9-9396-e26c83061a27 | -8.654 | -54.6505 | 2026-08-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ba44e758-8537-3aec-b73d-429ffad9d378 | -11.1939 | -53.9993 | 2026-08-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 72aecf45-3321-3b19-b163-68c4c53a96e5 | -6.7123 | -58.9412 | 2026-08-20 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 31a20da2-2ba4-3398-afdd-5759d056ee25 | -7.34 | -45.85 | 2026-08-20 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf3ae3f-caa9-3b6e-aa22-5d963001c47a | -11.8083 | -44.8072 | 2026-08-20 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d9a0edbb-4aa5-37bb-9191-9a444c007842 | -7.3413 | -45.8377 | 2026-08-20 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 30bafd2f-b794-3c48-8efd-cdc5135d4998 | -9.2071 | -59.771 | 2026-08-20 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e9cb78dc-c4c6-3c20-8168-bd4572df6e8d | -11.1936 | -54.0199 | 2026-08-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 71b45d8b-1e7f-347b-a6b5-c760fc3dda37 | -17.3365 | -43.6383 | 2026-08-20 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 512f7732-4815-3883-b8ca-d0c745484afb | -9.12 | -61.6011 | 2026-08-20 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 30ba3dec-edd9-360d-bf52-673967d6dfae | -17.3372 | -43.6139 | 2026-08-20 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 976e16e8-94c7-333c-86d1-6a0b4af9f2e2 | -8.654 | -54.6505 | 2026-08-20 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 12311e7d-5a35-31ac-b754-d591d0056a80 | -9.2256 | -59.7894 | 2026-08-20 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4aea6d4d-473f-3a70-b8eb-0269efde7a54 | -7.3415 | -45.8152 | 2026-08-20 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 0225c602-f914-3914-9862-47ec210c82e2 | -6.3863 | -54.9451 | 2026-08-20 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f21b31eb-f7fe-3303-acab-47fe0ee6c3b1 | -9.4069 | -60.4362 | 2026-08-20 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e0a81bc0-935c-35fd-97ac-6d9a0c53ce17 | -11.8377 | -58.8445 | 2026-08-20 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8a518453-2aac-3170-a861-4a7647806a44 | -6.6938 | -58.942 | 2026-08-20 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fcc144b4-8562-3c97-8b5f-38d721ceb131 | -8.6727 | -54.6492 | 2026-08-20 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 19941250-fa5c-3d84-ab9a-5ff8d7710941 | -9.4256 | -60.4353 | 2026-08-20 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 389add72-cad1-3fc5-a64d-3f9cb45e6dba | -11.2189 | -55.0585 | 2026-08-20 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6a228e8e-afa1-3622-a897-4f8a2db2b046 | -9.2258 | -59.77 | 2026-08-20 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 105dfaf4-84c3-38a1-8142-02665668be18 | -9.4257 | -60.416 | 2026-08-20 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| bbd3c6fd-f148-34b6-aca4-c145ac95e78f | -11.2191 | -55.0382 | 2026-08-20 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a329bb20-7cf9-33fa-b8fa-fe7650698add | -11.1939 | -53.9993 | 2026-08-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 13e3cb35-eb93-3117-86ed-b001c583bf67 | -7.36 | -45.8361 | 2026-08-20 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 055f6532-a0ec-3a17-b57f-f697f50f0bc4 | -7.3603 | -45.8136 | 2026-08-20 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 88827069-36c4-39c5-88e1-66ecb8eb0186 | -11.2 | -55.0601 | 2026-08-20 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4527821e-22a3-318b-bc80-71b496e1622a | -9.4256 | -60.4353 | 2026-08-20 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b4d345d1-edf0-3bb1-bb90-e9963f5e2df1 | -8.6727 | -54.6492 | 2026-08-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 4d04c083-d4fa-3a59-87ba-8026538b080e | -9.207 | -59.7903 | 2026-08-20 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5c77ba91-1389-37fc-aa67-5e7ae3aae2a1 | -7.3415 | -45.8152 | 2026-08-20 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c4738b97-de1f-3f28-be0b-97e1e74d4d0b | -6.6938 | -58.942 | 2026-08-20 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 67e6ec48-a633-3b11-aab3-dbc05a64d6df | -9.4257 | -60.416 | 2026-08-20 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c77268c6-e920-30b3-85eb-74e334c68dc1 | -11.2 | -55.0601 | 2026-08-20 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9a8d1a48-52f4-3836-9295-53dcdd2114ba | -17.3372 | -43.6139 | 2026-08-20 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 163.2 |
| d65d6f03-1769-350b-a757-bcf593225470 | -7.3413 | -45.8377 | 2026-08-20 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 834682c2-f841-359b-82df-a0ff810d39d2 | -17.3365 | -43.6383 | 2026-08-20 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e6f44506-57d8-3c62-b7e3-c74a29e115a1 | -11.1936 | -54.0199 | 2026-08-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4f4b09f6-cf6a-3628-a533-c9a439cba0c9 | -8.654 | -54.6505 | 2026-08-20 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 93cce69c-f08b-3d11-9107-987755cf61ce | -9.2258 | -59.77 | 2026-08-20 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7d61373d-30ff-335d-8135-356b354f9792 | -7.36 | -45.8361 | 2026-08-20 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6cd644e6-23a4-31ba-991b-4255e9489810 | -9.12 | -61.6011 | 2026-08-20 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c8b44a4e-19aa-37d4-99ca-79ce14534364 | -11.1939 | -53.9993 | 2026-08-20 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c61cc7fd-6d2a-3611-9376-350db003d0b3 | -9.2071 | -59.771 | 2026-08-20 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3d2de5f0-5a43-3f65-b24a-889ac7792914 | -9.4069 | -60.4362 | 2026-08-20 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f7c452e1-c776-3075-9a3e-45c04885db97 | -11.2191 | -55.0382 | 2026-08-20 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| b73435eb-c8b8-3a0f-94c2-e07d21c30612 | -7.3603 | -45.8136 | 2026-08-20 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9c9769cb-b9dd-3073-8030-6ede721d7830 | -11.8083 | -44.8072 | 2026-08-20 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ffe4563f-cd1c-3799-8abc-d0d8c5dbba34 | -11.2189 | -55.0585 | 2026-08-20 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5651cc09-e4f1-3c27-923b-8e99ef02143b | -7.3413 | -45.8377 | 2026-08-20 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 90a42771-327a-3769-b681-20c36102aee4 | -9.4256 | -60.4353 | 2026-08-20 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a907bc98-5fe5-33b1-b0dd-1210cc38ae1a | -11.2191 | -55.0382 | 2026-08-20 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| fd762560-880e-38a6-9500-03fcaf916ca7 | -9.2258 | -59.77 | 2026-08-20 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c9b5d68f-71c8-3ded-8e48-f00e096a16c5 | -12.4914 | -54.7569 | 2026-08-20 02:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2b2b2f1f-a5db-3de6-b05b-5f06f4eb1737 | -8.6727 | -54.6492 | 2026-08-20 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 978ec735-fa3e-3d37-95d2-26dc45af2961 | -11.2 | -55.0601 | 2026-08-20 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 39cecfa3-e6c3-36ab-968e-e8575dbfb773 | -11.1936 | -54.0199 | 2026-08-20 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 603d4d24-b75a-3a36-a7cc-64d5f6d67463 | -17.3372 | -43.6139 | 2026-08-20 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 167.9 |
| dc407f8b-2a1c-316a-8e7b-793f217839f5 | -9.207 | -59.7903 | 2026-08-20 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| c25fbe7d-ba51-319f-ad7d-5e928e251c7c | -6.6938 | -58.942 | 2026-08-20 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bccd0215-aea5-38db-be90-e0d988b3c23e | -7.3415 | -45.8152 | 2026-08-20 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 4c4eaf7c-b129-3d83-8047-d5efd9c8ce70 | -9.4257 | -60.416 | 2026-08-20 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 530bf2c1-94eb-3cc5-a26a-655c7e04f963 | -7.36 | -45.8361 | 2026-08-20 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| a783a1b1-4182-3c5a-8788-9dd03f29c25b | -17.3365 | -43.6383 | 2026-08-20 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 2109f82c-9e22-3f0e-b5d6-af6a8b53eddd | -9.12 | -61.6011 | 2026-08-20 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7df2cde7-e465-32c5-93b1-601563e5c125 | -8.654 | -54.6505 | 2026-08-20 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e70dc94a-9564-37eb-ac7b-3013abf3a575 | -7.3603 | -45.8136 | 2026-08-20 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b0d1b898-c3ce-3c1e-96d7-4b05d4bc7568 | -9.2071 | -59.771 | 2026-08-20 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9796390f-1c23-3e30-a874-776f1c17f894 | -12.4916 | -54.7364 | 2026-08-20 02:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 99df7755-861a-304a-ac65-2d941e1502cc | -11.2189 | -55.0585 | 2026-08-20 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 780a3f5a-fdc3-3d7f-a3a6-fb26408d4757 | -11.8377 | -58.8445 | 2026-08-20 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b69549c7-8643-3deb-af6b-6a9d0d6efeb3 | -8.6725 | -54.6695 | 2026-08-20 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 027c213a-cc44-3ce1-8a12-3280b8b4155c | -8.6727 | -54.6492 | 2026-08-20 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 33dcdcbe-4c21-33d0-9322-0bd111d082fc | -7.3415 | -45.8152 | 2026-08-20 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 7dda2312-551f-3ebb-be5f-45b359b9f002 | -14.3339 | -51.9157 | 2026-08-20 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1d705d06-4625-3997-b1e1-f325892bc7e8 | -11.2 | -55.0601 | 2026-08-20 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 8d877835-7770-3857-8d27-9573c9c017aa | -14.3149 | -51.8969 | 2026-08-20 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b9e57284-f647-3bff-9678-9c27f73dce03 | -7.3413 | -45.8377 | 2026-08-20 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b0103098-48d6-3d9d-bcee-a7d16fd23144 | -11.1936 | -54.0199 | 2026-08-20 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e2030824-853a-3067-9aab-9dd592527674 | -14.2952 | -51.9208 | 2026-08-20 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a8a99a71-ff03-3253-bfdc-5ca5daab2e4c | -14.3146 | -51.9183 | 2026-08-20 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 7142a8f2-ff93-38d7-b4a3-1a7ffb6826cd | -11.2189 | -55.0585 | 2026-08-20 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9cfe9781-d88d-3a4a-9773-1e44b6772e84 | -9.12 | -61.6011 | 2026-08-20 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 474cac32-a399-36fd-b463-ccee6def6652 | -11.2191 | -55.0382 | 2026-08-20 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 6d6ff6d5-36ab-35d0-9eca-73334b1d1857 | -18.0285 | -44.6113 | 2026-08-20 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 53a971d9-a8fd-387b-b62d-329e2ddaf602 | -17.3365 | -43.6383 | 2026-08-20 02:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e35970ff-060e-316c-a8c8-421ef550e68a | -9.2071 | -59.771 | 2026-08-20 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a9ddac63-f0d9-3d6d-ae04-b71382bad143 | -9.4257 | -60.416 | 2026-08-20 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |


[Clique aqui para ver as próximas entradas](README21.md)
