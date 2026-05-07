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
| 26cf8098-f0fb-3a63-92f4-97d0720dcbb8 | -10.5701 | -47.0433 | 2026-05-07 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 583efe67-4684-312f-8677-9e08ca83f006 | -10.5697 | -47.0657 | 2026-05-07 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| bbd3169c-5dc7-373e-8614-5fc8f0927565 | -14.1507 | -45.331 | 2026-05-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 33838be0-63b0-390b-91fa-d4c3e24a1829 | -14.1507 | -45.331 | 2026-05-07 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b7f8710d-7376-3ada-a702-2d026ad276d0 | -10.7774 | -49.7362 | 2026-05-07 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 30a07b58-fa68-3b53-aed3-10d3a8696e8e | -10.5701 | -47.0433 | 2026-05-07 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 333.4 |
| cb4dc075-9776-339f-91c6-8e07ec0bfc70 | -12.3508 | -50.0266 | 2026-05-07 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| bc01ec0a-2e04-3fbc-83c0-266d73635dc5 | -13.9924 | -56.6437 | 2026-05-07 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2d2fd600-0136-3ea9-a58f-032c2b18f8f7 | -10.5697 | -47.0657 | 2026-05-07 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 225.4 |
| a26553bd-6ab6-364d-93ef-22d6cd226a4f | -12.3512 | -50.005 | 2026-05-07 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 70540611-bfa2-365b-9ce5-f10195167f4c | -10.5511 | -47.0456 | 2026-05-07 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1e597e48-2da1-3759-9cdb-305626c91cfd | -14.1312 | -45.3344 | 2026-05-07 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 57e26215-ff69-3495-9c80-ac9a58ff6471 | -9.4655 | -46.1415 | 2026-05-07 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| deeab339-0492-3b26-94af-27b49e5e23b5 | -8.7841 | -44.8315 | 2026-05-07 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2e60d974-590d-34aa-81ea-ae45bfbd8aa3 | -10.5888 | -47.0634 | 2026-05-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 92bb800f-dfbc-3128-a681-87fe1bbb6ebb | -12.3512 | -50.005 | 2026-05-07 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4dc36b9b-b981-3090-812d-d5f329833537 | -8.7841 | -44.8315 | 2026-05-07 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0e506956-4410-3bfc-a90e-e77623f4f213 | -14.1312 | -45.3344 | 2026-05-07 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4d8ce34d-b4f8-32f8-aed9-eeab2502488b | -13.1882 | -52.6922 | 2026-05-07 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 863fce86-0078-321f-94b3-cc2794cb16f7 | -12.3508 | -50.0266 | 2026-05-07 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 869ed3a5-8117-39e8-9808-7ffb3e5d61f6 | -10.5701 | -47.0433 | 2026-05-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 78799d30-1396-31e5-b5d2-1dd1a2b26f4d | -14.1307 | -45.3577 | 2026-05-07 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| dae7d706-19e3-32e7-9ab4-e24023e43820 | -10.7954 | -49.7987 | 2026-05-07 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 12682d18-ea81-3ec9-b4c8-c729f5dad70f | -10.5511 | -47.0456 | 2026-05-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| a8aeba02-f06c-3f7d-94ad-59e297e99ebe | -10.5507 | -47.068 | 2026-05-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| be6d86da-7772-3aeb-9e1a-f198a42b29b0 | -14.1312 | -45.3344 | 2026-05-07 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 4d1edabc-fd28-365e-956c-ff15b361f360 | -10.5888 | -47.0634 | 2026-05-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 82c47e74-d797-3eb7-baa1-8cc61556476a | -12.3508 | -50.0266 | 2026-05-07 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 221fcb4d-609e-3af1-a91f-f88a5309c064 | -13.1882 | -52.6922 | 2026-05-07 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 00c19e28-e63f-3615-97a9-0feb8ffdd5f8 | -10.5701 | -47.0433 | 2026-05-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 078e0a56-59d0-3615-96d4-05471f777b76 | -12.3512 | -50.005 | 2026-05-07 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 62edbdf0-2f3d-3c4a-a321-06d0088df0c4 | -10.5697 | -47.0657 | 2026-05-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 379.2 |
| 1be61b96-58aa-3ad7-a808-cec22ee56279 | -14.1507 | -45.331 | 2026-05-07 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fb1f4332-42b7-3120-b903-5160c62b6c20 | -13.9924 | -56.6437 | 2026-05-07 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 15691db4-aa9b-3d43-ac10-15e089fd34dc | -12.3512 | -50.005 | 2026-05-07 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 31b2a974-ed65-3cba-a5b4-90ca22f54405 | -10.5511 | -47.0456 | 2026-05-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ef30a104-6cbf-3f2c-b728-d0fe24274299 | -10.5507 | -47.068 | 2026-05-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c8b66670-4195-3383-9f13-8aa0f0308bf7 | -13.1882 | -52.6922 | 2026-05-07 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| dbd95b80-bd9e-372f-aad3-1203e7a308d5 | -12.3508 | -50.0266 | 2026-05-07 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d3a2ed46-ab3a-3454-82ee-812413b525ae | -10.5701 | -47.0433 | 2026-05-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 317.2 |
| bd08cc28-9db9-3fd8-896b-b3a2f58ced81 | -14.1312 | -45.3344 | 2026-05-07 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 2de297c9-372f-3beb-95b0-8b68141e5cdc | -10.7954 | -49.7987 | 2026-05-07 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9876e932-92cd-3704-bb19-6876c23da7ca | -10.5701 | -47.0433 | 2026-05-07 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| e5a7b97e-80a8-3f4a-a87d-89d59fd1033f | -12.3512 | -50.005 | 2026-05-07 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 99cc51dd-6f61-383e-99c2-87107d027c33 | -12.3508 | -50.0266 | 2026-05-07 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 169ac0cc-8da4-39c7-870a-cc629cc1aec0 | -12.7819 | -59.0096 | 2026-05-07 14:40:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b3abc8df-6197-368f-bc3e-7e79ca9a84a6 | -13.1882 | -52.6922 | 2026-05-07 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 886bdbff-68aa-3280-a044-59923e27845e | -14.1312 | -45.3344 | 2026-05-07 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 922cba12-f92a-3737-a105-2685b8b879f6 | -10.5697 | -47.0657 | 2026-05-07 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 229.5 |
| ef152e1f-9122-3d95-bc4c-1e7250dc1ef2 | -14.1307 | -45.3577 | 2026-05-07 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1c917960-f786-345f-b002-3fc9e439c18d | -12.3512 | -50.005 | 2026-05-07 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 328e82c9-fd5b-3a86-ab6e-b1087977505e | -10.5697 | -47.0657 | 2026-05-07 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 357.3 |
| bc81adc1-ecdc-3065-a1a4-32d72b26548b | -10.5701 | -47.0433 | 2026-05-07 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| c8b7371e-e5c9-32b6-8280-ae1bd66b5901 | -12.3508 | -50.0266 | 2026-05-07 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 56e75d59-31d6-3928-80d2-d0ec90bb1c2c | -12.7819 | -59.0096 | 2026-05-07 14:50:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a7f48cd1-845e-33f9-8ebf-4bd3babbe561 | -16.1655 | -58.4842 | 2026-05-07 14:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 4412a12f-a137-345e-9c75-3ab9fab76c35 | -10.5507 | -47.068 | 2026-05-07 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| eb18dc27-7fb5-3ce5-b229-4800126b2b71 | -13.1882 | -52.6922 | 2026-05-07 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| aa3de002-7616-3d92-88fc-2d3336fe1f8f | -14.1312 | -45.3344 | 2026-05-07 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b6c45645-08cc-3c5d-8099-21d7f38715e1 | -10.9273 | -49.8488 | 2026-05-07 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 21bed83e-69bc-32c2-87c3-71d32ac5d0fb | -13.169 | -52.6944 | 2026-05-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 62ca4ebc-6a4b-3753-bbb7-3f89c4159792 | -14.4001 | -44.5846 | 2026-05-07 15:00:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 18c4c565-6cef-3828-b38c-529425168830 | -16.1655 | -58.4842 | 2026-05-07 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 190daee5-2a2f-380a-84a8-acbbc630da24 | -12.3508 | -50.0266 | 2026-05-07 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2e4ecc32-79cb-331d-a0bc-e2d05e886aec | -10.5132 | -49.6786 | 2026-05-07 15:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 40e59dfb-2668-3484-b414-9b3b48426e7c | -13.1885 | -52.6711 | 2026-05-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ebdc8c6e-e2ca-3322-afbe-4146f3814138 | -10.927 | -49.8703 | 2026-05-07 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0e17834e-b00a-361e-affd-5a015a98870e | -12.3512 | -50.005 | 2026-05-07 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2af735c5-fc11-3bb7-8498-380c462f645b | -14.1312 | -45.3344 | 2026-05-07 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f7bfa137-e2db-3c5b-b3ab-64a9043e9a65 | -14.1307 | -45.3577 | 2026-05-07 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 03aa507d-f10b-3195-8ec3-325d48139c7f | -12.7819 | -59.0096 | 2026-05-07 15:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| df541b76-7c79-394e-8034-91bc2ddf1acf | -13.1878 | -52.7132 | 2026-05-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4186527f-d806-3beb-b9c3-c3add094e3b4 | -13.1882 | -52.6922 | 2026-05-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 275.2 |
| 2adfe387-c2c5-38ec-99b4-12e59ba0b17c | -16.4159 | -54.9288 | 2026-05-07 15:10:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 880e3cf1-07dd-3570-aaa5-292f76eef250 | -13.1885 | -52.6711 | 2026-05-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a8803e39-61cb-3e85-bb2a-8e797d04da83 | -10.5132 | -49.6786 | 2026-05-07 15:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 89bfc320-eb2c-3d73-be96-353c3ac06e8f | -12.7819 | -59.0096 | 2026-05-07 15:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 927a8b38-698e-374b-8720-10f959a69684 | -12.3508 | -50.0266 | 2026-05-07 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| bb951140-7ad7-33a0-a7b4-bd96cd3dfca9 | -14.1312 | -45.3344 | 2026-05-07 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0ce62a01-c842-355a-a168-66dfaabefdd9 | -13.1882 | -52.6922 | 2026-05-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 348.5 |
| 2f85aba1-7e90-3ee0-af79-0c82ca2f6c28 | -14.4001 | -44.5846 | 2026-05-07 15:10:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b19c9201-54d6-353e-ac85-d03cbe9c217c | -10.5701 | -47.0433 | 2026-05-07 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 531127c8-5b59-3e74-9ad7-bf1d4c98a2e4 | -13.169 | -52.6944 | 2026-05-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| c72652b4-e800-3cd8-8b25-c95c0e44d1c1 | -13.1878 | -52.7132 | 2026-05-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| e1add3a5-b2f6-36df-b082-eb90740640cd | -10.5697 | -47.0657 | 2026-05-07 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 179.1 |
| c4ecdff0-a112-3db3-893f-8d2d5716cdf4 | -16.4163 | -54.9079 | 2026-05-07 15:20:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 19f3a213-1293-35ae-a48c-e38e678286d0 | -13.1885 | -52.6711 | 2026-05-07 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 4681a86e-59f1-30b4-9772-7dc6498f0801 | -14.1312 | -45.3344 | 2026-05-07 15:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 60f224ea-a568-307c-9ee9-7e95940feed9 | -12.3512 | -50.005 | 2026-05-07 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2ee60f97-6eca-302e-9dfe-b3abc815454f | -16.4359 | -54.9053 | 2026-05-07 15:20:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 28f41e8b-b867-35d5-b4be-0f320c155534 | -13.1878 | -52.7132 | 2026-05-07 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e6dd12cd-4be4-3da1-92f3-41e06164a1a1 | -14.4001 | -44.5846 | 2026-05-07 15:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 96e023ce-8bf0-33c8-8167-aad96750ecc3 | -13.169 | -52.6944 | 2026-05-07 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 40d23b78-af60-3686-9de6-afa77aa0e8d6 | -16.4159 | -54.9288 | 2026-05-07 15:20:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7994fd85-9560-3087-b34f-7048b17591fe | -13.1882 | -52.6922 | 2026-05-07 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 385.2 |
| 8049a17a-29ca-3111-9c4d-b3cab895179b | -12.7819 | -59.0096 | 2026-05-07 15:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| dc5dc942-7b04-3129-9b34-6693d67e1a10 | -10.5701 | -47.0433 | 2026-05-07 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 82fdacb2-6bbb-3420-8c9a-80dfc865fbe8 | -12.3508 | -50.0266 | 2026-05-07 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |


