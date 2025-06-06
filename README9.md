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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d37c97b-d672-3881-991b-f320222cf7ef | -10.07719 | -52.74979 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35f0ff97-ddeb-3ef2-b9fd-17430a5c8f67 | -9.60506 | -49.0212 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f7b17cd-9053-388f-a66c-5ca93b5e6779 | -12.66097 | -58.22273 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c47f07ff-7b23-369f-8fb4-2fddc9842409 | -13.51414 | -56.5696 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 681647fe-fe87-3785-97e7-57f0904cbb03 | -12.83345 | -47.38625 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a5ecce-6ff9-3f7f-a0ac-e864c5518e12 | -10.86995 | -49.5449 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b5e83a-a965-3218-a695-d81aadb18000 | -12.52257 | -58.36131 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b3b282f-adbd-3869-abe6-cb467b267401 | -10.69862 | -57.64325 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 145fe71e-336d-3075-81ea-c3ea34829e7a | -12.05441 | -47.32407 | 2025-06-06 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68f672b2-c02f-3187-998c-7c8a60f3e2c5 | -15.08044 | -48.94463 | 2025-06-06 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc11436b-9faa-376e-ac16-13dc9cf4f775 | -13.07742 | -49.2474 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ba04b4-9aff-34c5-a383-59a849586ed5 | -9.70267 | -49.48653 | 2025-06-06 04:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94ec727d-cef2-3c46-b17c-4e3063449cb4 | -12.05377 | -47.32846 | 2025-06-06 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb62252-8f28-3916-a297-6e1f6a1263e2 | -9.2041 | -49.68953 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652b17cc-54cf-350e-8659-1c15717966b6 | -12.9601 | -46.77216 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a3b8a3d-de2b-3eee-8b83-6b17ea49ca49 | -12.53463 | -58.35473 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e6445b0-d3cc-391a-9dbb-9f8ce053968f | -14.2981 | -47.99224 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 035573fc-05da-3950-97fc-a6190878f587 | -12.38201 | -47.31819 | 2025-06-06 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cba1bc5-d823-375d-a19c-f90c11aba301 | -10.39643 | -47.11908 | 2025-06-06 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b20b57d7-5a1e-3d42-bde7-a9c37c509c7f | -10.46155 | -47.95411 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 566b4a30-08b9-34a8-905e-c70529548998 | -10.45864 | -47.9496 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f273c302-01cb-36f1-a8d2-6a18a0e66e71 | -14.92377 | -45.97024 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5193c5d6-8fe9-3bb7-8106-31ae30db58db | -14.22 | -45.49625 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6514fbd4-2927-3079-8a7f-24ad3cbf182f | -14.28773 | -47.98658 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e68264f3-fabb-3a1b-9e3e-59a2b6740a86 | -10.99466 | -59.15655 | 2025-06-06 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd639e5-0d9f-35f5-899c-a2815b7e3f45 | -13.64499 | -44.44688 | 2025-06-06 04:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29165718-1c20-3490-b1a9-3c78ddd2e5a1 | -14.74395 | -45.10625 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56ac27da-cb45-3e32-b848-8fc752f4c57c | -13.64135 | -52.18215 | 2025-06-06 04:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56797f77-c294-3d52-9cef-264f1bf37c82 | -10.30553 | -57.13712 | 2025-06-06 04:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5f85148-2a01-3f68-b87a-338e580e00cd | -14.30175 | -47.99278 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9b32c42-db5d-392a-8e61-364b64b89a23 | -10.33499 | -57.49302 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6c7050-bb87-3e61-b7d5-c0782e997725 | -12.27072 | -55.07677 | 2025-06-06 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e34cf7-1996-3d6e-b501-2ae9fc2f6568 | -10.68758 | -48.96444 | 2025-06-06 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d7bd8c5-2f93-3bb0-92fc-01b476c66160 | -13.51482 | -56.56586 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72c5af5d-9505-3cb0-842b-894a8fe5c71f | -10.49631 | -53.65593 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57b61093-60e8-3d12-a08a-79de9e36f129 | -12.83925 | -47.38573 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f27bc68-bbc2-3322-8a68-bc5c718989e1 | -12.15709 | -43.20847 | 2025-06-06 04:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aab02349-9c55-3f1e-bcc2-e66e15e272fb | -12.96712 | -46.778 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76c73c84-3a40-3b28-abf2-7cad42ff98fd | -12.40905 | -49.67725 | 2025-06-06 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9fc1087-b0d0-3954-acfb-0bffbba57337 | -10.30372 | -58.43803 | 2025-06-06 04:42:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd3b01c-22dc-31cc-aae9-31059fdc3f9e | -14.66767 | -53.1243 | 2025-06-06 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc4415a5-09b2-3f4f-ade9-4da9b1005908 | -11.13849 | -53.94679 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c38af4f3-ee88-3f9c-8efb-a0f9aee94734 | -9.54558 | -47.77376 | 2025-06-06 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09e00d2c-1d6a-308d-b92d-689e69c7b72f | -14.86141 | -48.33983 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ea7bd6-d83f-39a3-b5ff-fb4ccc002bb8 | -12.52264 | -57.2433 | 2025-06-06 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd08132-9c16-3779-a3c9-59c1d780f6b7 | -11.92298 | -54.82125 | 2025-06-06 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c529c470-f68e-34be-8245-6f923c31d16b | -11.37631 | -56.55159 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35b5af76-f7ca-3c14-9d67-51a3556cf3e0 | -13.99356 | -45.23988 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76194a00-fb8d-3555-955c-202cf00b066c | -10.49923 | -53.66079 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f2bea23-fe31-3c0b-9697-997b178af057 | -12.52894 | -58.35897 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f33ec62e-2c87-35e5-bb5d-dae31f0d3540 | -13.51619 | -56.55839 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5a37c6b-12e4-34b5-afbe-a520bc1b4ded | -10.30269 | -58.4436 | 2025-06-06 04:42:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad46db9d-c132-38fd-b5c1-01f4f3c36360 | -10.4956 | -53.66018 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24909164-e89f-31a4-8504-bb93b53605b8 | -11.07642 | -54.77343 | 2025-06-06 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20989fdf-67d8-3fd1-ba68-1f61fda9379b | -10.59458 | -52.8088 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df32cccd-4da4-33f4-8f51-2679257d6b63 | -12.82057 | -47.37075 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bafccca-1fd5-3ebd-a2be-a5fd1100022e | -14.74013 | -45.10143 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9691b6-86ec-3ae3-9cde-1a17823ec54b | -12.05313 | -47.33284 | 2025-06-06 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52aa0015-dc29-31d9-97ef-024985d0e2a8 | -12.95493 | -46.78112 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96c4a303-111b-34c4-9778-f7507ffa1453 | -13.52237 | -56.57106 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8869fe7f-30ff-356a-8f15-f5c156ad9451 | -10.29487 | -57.1445 | 2025-06-06 04:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f064b203-00d9-3733-91d8-d47c6c9f42d7 | -10.07369 | -52.74921 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e76f726d-37b3-355a-975a-b83020e33e64 | -13.93193 | -47.18521 | 2025-06-06 04:42:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c14fb49c-d546-35cc-b481-ae5549f9101b | -10.70322 | -57.6443 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b15f47d7-84f6-3d84-b8f5-610611af9a4c | -11.53707 | -56.45204 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2494c75-5c98-347b-b20c-b1d39fa6771f | -15.14665 | -45.51059 | 2025-06-06 04:42:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 506eb9c0-bfd4-3bc5-9ba0-36356583f6ef | -10.70825 | -48.78218 | 2025-06-06 04:42:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 212f9ff5-64e0-32a8-87c0-1f574582b88b | -10.46506 | -47.95465 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74452903-1443-3556-8bfa-ee59da9969af | -14.03957 | -55.13833 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 260deb61-59f6-3bd7-8b8f-bede4d57d2fc | -11.53214 | -56.45526 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 778719f8-85d9-3f19-ab37-abc73eb1539f | -13.8835 | -54.67731 | 2025-06-06 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0bf12fa5-5d9e-389c-954e-16a6a029bc73 | -14.29868 | -47.98819 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558a1de1-24b8-3e7b-ace9-0cad7857690a | -13.51826 | -56.57032 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ee82fd-ace4-3cdd-ace0-d0f523c62aed | -9.60898 | -49.01812 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9216a75-9e6f-3803-a32e-6091b6372e67 | -9.5148 | -47.69244 | 2025-06-06 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 973457e2-8425-3f47-923a-3f3c28d64133 | -9.39297 | -48.4245 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd666831-ac73-3e77-b5e3-6457555f1608 | -11.11483 | -54.66343 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b577382-a788-3dbc-aa05-42e31c6a0399 | -9.37756 | -48.41067 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f5dff8b-d43d-3130-9508-3ab85af69492 | -10.49268 | -53.65532 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ebf45095-ca26-3974-821a-b0c5bff7a0cd | -12.8341 | -47.3818 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 741244a8-e8de-37c8-bdfb-d6b29275e93c | -14.7407 | -45.09716 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6353ecb9-8c45-359d-ac62-cd6753468e05 | -12.95175 | -46.77584 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de71f50b-cdf2-3d44-9aa6-aa577e51a356 | -9.66637 | -48.59789 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcbc832c-a22f-3edd-bb15-02b9a0988ca6 | -12.83781 | -47.38234 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4a579ad-bfac-382e-bd52-17e6a86be226 | -11.71399 | -56.45416 | 2025-06-06 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 371b261d-87e6-3094-87e9-b7da7f690e1a | -11.53143 | -56.45927 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77772f74-52dd-3c63-9dd9-1b3845c5bb77 | -10.68424 | -57.59037 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a3599fa-cb63-3557-8d8d-acb3d600cb41 | -10.68762 | -57.65115 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 57ae7feb-8363-3182-b4e7-aab544a090c0 | -11.37983 | -56.55643 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac0272e-0dd2-30b3-bdbc-32564e1762de | -11.68967 | -54.55725 | 2025-06-06 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b108d641-6b78-3d32-b1a6-4e2bf9f4f4f5 | -13.07799 | -49.24364 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f7f0b1c-0164-3c50-86cf-7e521e9fb0ed | -10.70483 | -48.78164 | 2025-06-06 04:42:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e29cc431-2bbf-3fd1-b4f5-4283320ed24a | -12.26461 | -55.07777 | 2025-06-06 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c91286e-13c8-33eb-b827-5219d7a03ea0 | -14.22476 | -45.49288 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db5f22a5-45aa-3939-8658-a56e2a971162 | -14.23429 | -45.48612 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e6658bd-a33c-35ca-ba57-6c0507c73a24 | -14.02914 | -55.13165 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 474b62f3-ea02-3482-b92b-25b4be57d46a | -11.14287 | -53.94308 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ee60e6-1641-3122-9277-68d4bba3f245 | -12.24677 | -51.42852 | 2025-06-06 04:42:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7fd20636-6c6a-3e73-b857-ebe894147e0d | -12.83554 | -47.38519 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b8425f9-bb19-3e9f-99b7-954975e43519 | -14.66488 | -53.11996 | 2025-06-06 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README10.md)
