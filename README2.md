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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04eda000-05c6-350c-a057-bffa50b705ab | 3.51771 | -60.30545 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 154b1bb8-313d-332e-82f4-853cb44e443f | 3.03025 | -60.0704 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1ad321d-5617-359d-8c3c-00e9071848dc | 1.49208 | -59.92978 | 2026-02-26 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfbd0474-b0b3-34cb-a1a0-05c41364f9b1 | 4.27402 | -61.32622 | 2026-02-26 04:44:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b77ca8c-f369-3d10-bcc5-fb08325ba8f1 | 4.07316 | -59.89944 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac848c8-fb37-30ad-a9de-01e9bf1e9baa | 2.57462 | -60.55144 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d40719a1-dbf8-3ed7-8d12-134a75504d58 | 2.5757 | -60.55121 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| beae5c48-ad79-3ab1-8a10-34c3719fcd31 | 4.07389 | -59.89475 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 152c414a-0a91-3a75-898b-b5e6d40f1da7 | 3.12897 | -59.97515 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11bdc132-548e-3f31-b331-74745324980b | 1.74064 | -61.13456 | 2026-02-26 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6cb3ac4-bf19-384e-9d26-9bd77e9861e7 | 3.04576 | -60.0377 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff29deb-c8f0-3899-9397-32f0b753b818 | 3.02955 | -60.06584 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| deb655b9-c30a-39a5-9b62-83eb200d3a4a | 3.0451 | -60.03315 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7445487a-f9e8-3ebb-ba4c-513d82391317 | 3.51701 | -60.30058 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ece383fc-e1ce-36f4-b0de-5c1970bfb892 | 2.56841 | -60.55228 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ce4c6b7-fd99-31f8-8b14-19ce6a9fe1b7 | 1.94302 | -60.3578 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5957e97b-84db-33b0-bee0-a7ca853b4c16 | 3.135 | -59.97429 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdf5f15c-3107-3c37-8fa6-ff29fa37336e | 3.48262 | -60.28086 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e29b5c-502a-3174-8a09-45b3a0dcd98e | 4.07451 | -59.89918 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f795b5-2163-3fe2-bd0f-59fb32e61976 | 3.03157 | -60.06769 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd2bd3b5-427d-381e-b481-0a87fbd99ae3 | 3.13097 | -59.97453 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6b308b4-f71d-369d-ae63-7651ea76ee6b | 1.74143 | -61.13979 | 2026-02-26 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41d8e1e2-26e1-3846-ae22-2c3e6239aaf7 | 2.07076 | -60.21011 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc065956-0585-380f-849a-738721610e6f | 4.07252 | -59.89508 | 2026-02-26 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a2d5683-1bd9-3681-a0b9-91c45e4600d1 | 3.137 | -59.97366 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0de59f6-855c-3cf3-93d1-56af15502361 | 2.56948 | -60.55202 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 487f4b1b-7e67-3cef-a781-5f5e5cf44789 | 1.94373 | -60.36245 | 2026-02-26 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5533f12-38e8-3b11-ad75-daae38a38395 | 4.27687 | -61.32953 | 2026-02-26 04:44:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ace5290e-95bc-38cb-abda-735836566c17 | 2.07299 | -60.21159 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3934e1ab-250c-3896-8f6e-726697566e44 | 3.03091 | -60.06312 | 2026-02-26 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1e52ade-0357-3e6b-a0ca-f82382eb978e | -10.68669 | -59.37405 | 2026-02-26 04:48:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1df13926-44a7-3c39-bf39-1accac256997 | -11.83143 | -58.03561 | 2026-02-26 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab23519e-0f98-3dab-b3c9-3c29f1f504dd | -11.83557 | -58.03639 | 2026-02-26 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0be678f4-6c30-331e-9745-2b92ee9d30bb | -19.56951 | -56.24173 | 2026-02-26 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f87dea28-c239-3631-a3f7-1a0e74f47083 | -20.84511 | -51.73909 | 2026-02-26 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5187058-6efd-340d-a863-0f589cdb1d89 | -22.8854 | -53.43337 | 2026-02-26 04:53:00 | NOAA-21 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2caf9be9-922d-3980-a98c-428379602d4f | -23.76529 | -54.58341 | 2026-02-26 04:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 6acd502d-f620-36e6-b69c-3cecad7678e3 | -27.82852 | -50.30562 | 2026-02-26 04:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b4f2ccf4-85a9-3306-9822-12e0e3e0cb5d | 2.57974 | -59.93816 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65972512-5d72-38dc-b881-8426b3629ff7 | 3.51436 | -60.30405 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950df378-e2cc-3ee5-bed1-3611e975ffef | 3.51273 | -60.29325 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea84ffcc-2e8f-34ae-80f1-7be734b98a9e | 3.13656 | -59.97136 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf396054-b324-3d2c-b750-a3902976c1ab | 4.15188 | -61.02064 | 2026-02-26 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f17f59b1-a6e9-37ff-84bf-17d7298ff518 | 3.13259 | -59.97197 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bdcb01-0bd2-35c1-9646-c79b9ed3289d | 3.48612 | -60.28265 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d8aa74a-0db5-3f35-b3ff-51740d5ae10c | 1.83325 | -60.61375 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce784bb-f4d8-3f9d-954d-a9d075599650 | 3.50702 | -60.2831 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fa8cac8-f635-34af-8239-d0f635a0d685 | 4.01877 | -60.10329 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1bc3302-3079-317c-a8fb-d9641a352e55 | 2.92053 | -61.01484 | 2026-02-26 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f613d26-7aeb-3c6f-9026-164a9940b5ec | 3.48205 | -60.28329 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a579665-0c9e-3530-8c1b-5ea98da0d828 | 3.13336 | -59.97705 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18084cca-83e5-37c9-a2fd-a9ada86941e1 | 3.80751 | -61.75059 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0babf7ff-dba6-3d81-baf9-c297372a83eb | 3.11939 | -60.26912 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf76700-3ff4-314f-a713-80bfaf739b70 | 3.11884 | -60.26559 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e25456-06e2-376e-853b-3ecd811eec13 | 1.94259 | -60.84207 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bad093c-a395-3803-9b62-2d21f006625e | 3.64111 | -60.91196 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 954c1613-bca4-3222-a607-94567b76ec32 | 2.0708 | -60.21212 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88ff4dfe-8675-36e5-a300-5ce0bdcea2b7 | 2.07477 | -60.21148 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f456edd-da38-3486-90c2-e0675ece67bb | 3.51844 | -60.30342 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2259c63-3fd8-3af2-b77e-fd31df613783 | 3.03106 | -60.0686 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b73f7d2-9065-3035-ab29-63d2b3dfe95e | 4.2732 | -61.32819 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c693e4f-3cc1-3715-b068-c1175dd7d749 | 4.27421 | -61.32691 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b9bd9ab-f51f-34cd-a94a-91431ff0fb8e | 3.80817 | -61.75506 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 814db6b7-e11c-31c9-b903-e7617b73712b | 3.11534 | -60.26974 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d813e5a-8cc0-3686-95ba-f8deb51c85ed | 2.56996 | -60.55301 | 2026-02-26 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7f12118-3c61-305a-bdce-79f6f4ffacda | 2.92319 | -61.22993 | 2026-02-26 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63597433-6d4a-311e-8a10-e42f4ed9fb6a | 1.93433 | -60.84338 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad5b32d-56c5-3d36-9655-c5a1ab500d3e | 2.90844 | -61.21982 | 2026-02-26 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7cdca02-8f68-3ef3-bd4b-fd0ac1595410 | 1.9402 | -60.8418 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a984e0b-280b-3717-8df8-3aa684e4c627 | 3.51491 | -60.30766 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b124961a-a0f9-3e99-b969-30895f2fdff5 | 3.12288 | -60.26497 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2f1060c-a152-3a29-b87a-0c4dce965283 | 1.48454 | -59.93395 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19e2487a-9d3e-3028-8d21-525c12bffc07 | 4.27762 | -61.32755 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3a926f-2df4-34cf-a859-33f67558cd77 | 4.27863 | -61.32627 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f65c763b-fa57-3b3a-8062-fb32a67b7658 | 1.93846 | -60.84273 | 2026-02-26 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9266e2c-2968-38bd-bdf8-33b55ae0df9d | 4.07498 | -59.89842 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49d97c1e-ae1b-3f2a-ac6b-f6bc1270cefa | 3.12939 | -59.97766 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90b88e0e-da1f-3a3f-8c83-6e6be3d4df7c | 3.0463 | -60.03479 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaaa9d98-c42f-3fc7-b991-0013178a2fe4 | 2.91765 | -61.22254 | 2026-02-26 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 873ed8c5-7ca9-3afb-9226-b1125f7f7170 | 4.05653 | -60.81234 | 2026-02-26 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b287c4d-d0b7-390b-8a49-1d15f402835d | 2.92257 | -61.22591 | 2026-02-26 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3269312e-544b-375d-80c5-6c9844950cc8 | 3.03028 | -60.06346 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f643436a-67cd-39b2-8e6c-56470f555293 | 3.51789 | -60.29982 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36d443ac-773d-36cf-9adf-d58f6d0986f9 | 3.51163 | -60.28606 | 2026-02-26 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba6cd5fd-28a1-3108-812f-fcc85da52fa3 | 2.57405 | -60.55239 | 2026-02-26 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5449804a-29f8-3513-a319-9243f90aee1a | 3.05981 | -60.04317 | 2026-02-26 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19097854-2305-3e16-bf82-6806cf321473 | 4.27929 | -61.33054 | 2026-02-26 05:14:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7778bf9-e51a-3b8e-9f5d-96dbf8206e32 | 5.04705 | -60.5006 | 2026-02-26 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a84fa35-de9b-359f-a30a-bea7ab030161 | -4.70445 | -55.97143 | 2026-02-26 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f6c4e3f-9ec9-3103-8c7c-9b58926e876f | -11.83724 | -58.03783 | 2026-02-26 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 047871e8-f0af-3ac9-94b4-54c351d038e4 | -10.67276 | -59.36417 | 2026-02-26 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e1244a8-8659-30e9-a21e-d10bc1bc31a0 | -11.83391 | -58.03729 | 2026-02-26 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59bf9c58-e458-35a0-9cda-21049c309e4c | -11.83446 | -58.03374 | 2026-02-26 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef1d5946-5d1f-3532-a46b-5793254c0ef6 | -10.68502 | -59.37348 | 2026-02-26 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| def39f0a-7715-37b9-b4d8-851caf640353 | -10.68838 | -59.37402 | 2026-02-26 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dee5148-6336-3325-92c6-567f5e54f795 | -9.72245 | -60.2034 | 2026-02-26 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f31ecc1b-aff9-3d0d-80ba-b4cad7b56cfe | -23.76248 | -54.58294 | 2026-02-26 05:22:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 084fe531-f57a-3b15-90d7-8af54372d9a7 | -23.76195 | -54.58759 | 2026-02-26 05:22:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2e77b393-0354-3d73-8e96-3e8ec9ca2e85 | -23.76694 | -54.58364 | 2026-02-26 05:22:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0132cdcf-fd62-304b-bd64-3f3a1cac8b9c | 1.4864 | -59.9308 | 2026-02-26 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.6 |


[Clique aqui para ver as próximas entradas](README3.md)
