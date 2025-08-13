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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1ed13df-a274-355f-9899-fd77c6439f63 | -13.43648 | -44.50187 | 2025-08-13 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d63cd01-8278-3e90-930b-409e9758745d | -5.852 | -59.90538 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41f7996e-e44c-3302-ab8e-b02928244fb4 | -9.16928 | -59.67102 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5606af1d-04f5-38ff-81b4-630414c1b0cf | -6.87624 | -59.14261 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ce3181d2-82c1-3a33-bf56-6c383bd7fce6 | -9.84469 | -47.82262 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| df4d5faa-2cc4-3add-a2ee-1f059b0f7f91 | -6.88886 | -59.1343 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 69b15039-8fe3-3029-8388-7659bf0960a8 | -9.29466 | -50.2767 | 2025-08-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83ddbc2a-0919-3fce-9fb1-29eef4a25aa4 | -7.25241 | -59.99665 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1058b02c-74fe-339f-a91c-3de8d0973cd0 | -5.84198 | -59.92574 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c11882d-94b6-3846-9406-8b08846c667a | -6.61557 | -43.88906 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f6d07e9-2a08-3235-ac9d-e81729537065 | -6.8864 | -59.14803 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 2f3aaf8d-f293-38ae-871f-c1f0960d89a8 | -7.08195 | -60.01995 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d18a7fb5-4145-36d5-a347-b0959895af6b | -9.94631 | -48.34336 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea9a2e5d-9594-3b35-bc17-41c9e923c60a | -5.88805 | -57.74481 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e94c4937-b316-35fe-9652-71eaabb6fc3c | -8.56587 | -54.66542 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 413f2e04-1c99-3231-b192-44f54bfeb7e1 | -10.35277 | -49.9226 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2552fe7-e805-39be-a21e-0967048871bc | -6.61245 | -43.88055 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9d5cc499-a734-3c8f-934c-072b8e5c0ef7 | -11.91148 | -52.53333 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261f39c3-4b24-3694-b170-e5ed53eb6a6d | -7.45775 | -59.89069 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1222e683-80f7-3dd4-87aa-9c16b002b27d | -5.03506 | -50.86313 | 2025-08-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2064f206-3a6c-3e27-8f65-49e063740c31 | -10.34259 | -50.81711 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3828f740-a1e2-3a42-9fb6-f2223bf62a51 | -9.71142 | -49.47507 | 2025-08-13 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c73ddb6-0cef-3d8c-86dd-abc76764ff4f | -7.09774 | -60.03023 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f0c71c33-77b8-3be2-a273-e7e467cc2c51 | -7.06302 | -44.36209 | 2025-08-13 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89243b7a-5afe-3b13-8f13-640970a6b9b1 | -9.94577 | -48.34317 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b195d702-2e2c-38fc-8f82-bd93a56e83cf | -12.52802 | -46.97685 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eeb8d8b0-cdb9-36b2-a18c-87bde9ebfe84 | -7.07543 | -59.20525 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 365238ee-a145-3e13-9994-48df307c6578 | -7.09271 | -60.02547 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73bd4797-fc37-3d37-989a-9c6a3de8faea | -10.53319 | -42.54686 | 2025-08-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7ebcad49-8e1c-3f0c-b701-bdd29eabac2b | -12.49226 | -46.95705 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe857c87-a69d-339a-ade6-6cf831d43a37 | -9.31339 | -48.92789 | 2025-08-13 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6c41b5d-d79d-3f25-af69-559494a64a98 | -7.06751 | -59.207 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dac28f02-7a02-3ae3-bbc4-795b4c0fedb5 | -12.48716 | -46.9658 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 74f8cd07-7b8d-3929-a3e8-098f2f044825 | -9.06186 | -60.65612 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2bb239f6-473f-3944-9422-9a512a3bceb7 | -12.52734 | -46.98151 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c321f3ba-7ccf-3863-9569-d46a835cfe2f | -8.56622 | -54.7112 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edfcdfd7-f510-3646-bedb-e567da3f8819 | -6.8804 | -59.15043 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| bd3dd8a2-4295-38c6-848a-4bf6197383c1 | -12.50981 | -46.96927 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b103f5eb-7738-3370-832a-1307fbf98d79 | -12.30612 | -50.01295 | 2025-08-13 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 649f4da6-5644-3748-bb90-bb8d5263de93 | -6.10346 | -59.93656 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a2f0ca1-b2b0-36a0-8182-ab17766c3a2a | -8.93498 | -60.72807 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bed1db1e-64ed-375c-8ddf-d0247abbb24e | -10.18265 | -49.50549 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 288b311d-62cc-311b-b032-05caa6d0426a | -9.27598 | -60.76645 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de2b353-8d51-3692-8d61-7da916618e81 | -7.07606 | -59.20176 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ec989f-4173-35db-a7cc-bc57f9a404ff | -9.50752 | -62.37416 | 2025-08-13 04:40:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcec89cc-83b7-3389-a169-aa4be9a9964b | -7.06213 | -59.2059 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55c4c224-6699-38d0-84ad-2d091a17a008 | -5.84918 | -59.91856 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3caefbb1-c00b-36d0-b405-48d9ad40a4ef | -10.31268 | -48.11105 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c9fc4cc-2eed-3655-b920-31d4ce756e52 | -10.47642 | -61.32713 | 2025-08-13 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d89eb354-3be1-31fb-aa79-719dd827d81c | -7.45587 | -60.63658 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4111a9df-d65e-38cb-8040-9c5bfcced037 | -6.09694 | -59.93983 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec2bd5c5-8c97-35bd-81c7-d9469c7bc1e7 | -6.09114 | -59.93903 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f773753-1e93-3d0d-a4e6-8e52059443c1 | -10.00756 | -59.21241 | 2025-08-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 052120b1-2f3a-39b8-9bbf-cb758965cdb7 | -7.2517 | -60.00065 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08c4145c-4e21-3ee6-ad48-a90061354813 | -7.06941 | -59.20773 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad4f506-87ef-3de0-834f-7538f3c65f13 | -6.86609 | -59.1372 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c047eefa-2148-340c-ada2-8a02c5178000 | -6.8978 | -59.14651 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7e699bfc-0b8d-3455-a3c2-3e9c8a454e71 | -11.69584 | -50.13893 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df5a8354-1dbe-3d44-8725-f56d19959691 | -6.88409 | -59.12992 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6f357041-572f-32fd-af7e-3126542adc48 | -7.0735 | -59.20455 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e71e166-e117-3791-91d7-efc3729a84ff | -5.85353 | -59.92776 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ba9fe0-92c7-3336-8de4-5dbddb0bfc3c | -11.68783 | -51.58092 | 2025-08-13 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9237aa9-6370-3e69-89a4-4bc82062de01 | -7.06403 | -59.20664 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d772ceab-579f-379a-b4ea-09c894ed021f | -7.08769 | -60.02072 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c223faff-4dda-3803-8495-9fd9bcca500d | -6.61612 | -43.88512 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f8c48877-b28b-342c-84fa-581d671d490c | -5.88851 | -57.74212 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc04793c-2832-3f30-9fb8-06c1e08317f6 | -12.21597 | -45.47199 | 2025-08-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23d3ddde-89da-32c7-a6d5-fd65f158e11f | -11.90308 | -52.53601 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69dc802b-87d9-3208-b74d-d9c968a95bf0 | -7.06813 | -59.20346 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 463938b2-754f-3f7b-bf0e-5ecb129f0a3f | -6.89425 | -59.13527 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| fed9e37d-a197-34af-b640-96ec00669c29 | -10.3641 | -50.8098 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbdb930b-24f7-35cd-81a4-8d70d5f26ed9 | -12.52779 | -46.9796 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2a317c0b-b7dd-3bc4-a457-e65d40a29a5c | -6.90754 | -59.12312 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 257d99b9-1b9d-331b-9225-bfbe1024d975 | -8.10821 | -55.57167 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4fe2bd0b-ae3c-3064-8be9-41e00af95342 | -9.38217 | -61.53215 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12101793-ab44-32af-bac6-f013a027acc6 | -11.91426 | -52.53759 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe8d8d6-b042-36f5-8984-48d8b183b949 | -12.54484 | -46.96787 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c629b3b-8258-3fe2-865a-b5847b68e044 | -11.90749 | -52.53645 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a9c4e8-db67-361f-ad61-e63477a64c53 | -7.25438 | -60.00019 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c17287f-e455-317c-90b0-a17be84ec2fd | -11.68092 | -50.14745 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e568d4a3-f778-333e-a5e4-f60f6fdddfc3 | -6.64322 | -43.21732 | 2025-08-13 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| faf83804-ea7a-36b7-96a0-66b7de5f80b8 | -5.89302 | -57.74585 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bd0b6a7a-fe8c-31ce-8e8c-c9bf4d783403 | -9.66235 | -48.15383 | 2025-08-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c4c569-3e82-3445-8950-49d5fc86955f | -11.73997 | -47.59369 | 2025-08-13 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18a163c2-c3bb-357c-82f5-abb11d8cbf36 | -9.98911 | -47.8471 | 2025-08-13 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f740afbd-ca62-3776-9a01-a80d4367fbf7 | -11.70609 | -51.59479 | 2025-08-13 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16572551-2256-3db0-81b7-b33e03345443 | -6.89011 | -59.12734 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ca4e801-5e00-32b8-a191-eb723a74134c | -9.77761 | -48.3683 | 2025-08-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 916b594f-ab55-3b9a-8fbe-f25666b7b36c | -7.07069 | -59.20068 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24c2f928-421f-3d59-929a-191102182acd | -8.57711 | -54.71814 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab930640-4798-3d16-93de-7fc646db87f6 | -6.9701 | -59.28375 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd329a7d-f81e-31df-8dd3-15ce07fffb5d | -11.31667 | -55.22404 | 2025-08-13 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c44ebf94-58d2-36de-a811-e01e27bd7ca9 | -7.45517 | -60.63076 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85623ab3-d575-3d9c-8cac-046155a7f5d7 | -12.58883 | -46.98438 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58a5aa38-9270-3c01-9a6f-056163902f62 | -7.07005 | -59.20421 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c806c21d-e248-316d-902c-2f4926e63451 | -12.69094 | -46.97329 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e145561e-f937-3ff2-a9c2-d5f6224d82c2 | -6.87501 | -59.14945 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e760f142-f45e-3a5a-8ab3-e0d10288cc93 | -12.58455 | -47.0691 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4929fcd8-9a4f-313e-bb6c-d99d2875212f | -9.18005 | -59.67286 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 422a9e54-c666-343d-bd6c-fe26faec721d | -10.96632 | -49.57605 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README19.md)
