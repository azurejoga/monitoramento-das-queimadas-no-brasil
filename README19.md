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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f50ab61-22a0-3bda-8473-77c48d4826ea | 3.85851 | -61.45181 | 2026-09-05 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ece842d7-1282-38e3-b122-174b278a313b | 2.45103 | -60.76256 | 2026-09-05 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f2509c6-2c0e-3b75-babc-2deb8c7df776 | 4.8838 | -60.29866 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2c4f5e4-eb8d-36b4-b026-cdb9e76e6e42 | 2.36806 | -50.7653 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a8b4dd2e-a147-31d0-a642-cf77fc9b0a40 | 4.8845 | -60.30063 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb7cfa16-1e3a-366f-b459-2685afd793ee | -5.14988 | -55.95724 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3348e74c-e7f6-3f5e-a08a-b5d4a6c9825f | -3.21214 | -57.85898 | 2026-09-05 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 988fee36-db63-3e6e-af04-ae2f40c0e77a | -7.46146 | -46.15115 | 2026-09-05 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c61ae8cc-2433-354f-b919-a6d10a467773 | -2.47058 | -54.88495 | 2026-09-05 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 029b9488-9ec5-3437-8650-976fd265262b | -3.80468 | -55.87975 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 744bc35f-a156-3a31-b206-73a687909635 | -5.34031 | -56.02302 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 089d1f9f-b9fe-3ed0-89fc-468a319ad054 | -4.67246 | -55.63871 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58468a8e-22b3-37ef-827c-ea8fbe306cc0 | -3.14282 | -60.64385 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0b4fc227-873a-3a79-a8b4-c15b1ec9efb8 | -5.337 | -56.0225 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcfa662c-f9b1-3cdc-8be8-0be6b97940f6 | -3.79806 | -55.87872 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76df42eb-3cce-3e3f-898f-b3ff04db74a1 | -4.67684 | -55.63234 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03444f88-a0f2-34ba-abdb-d821709ce011 | -4.6697 | -55.63476 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32e23a2a-d264-3616-b8f1-113a9ce0e173 | -5.353 | -56.02852 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b7c4d889-bc63-3808-a1ad-bc0863760e2f | -4.2943 | -59.95796 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a340ffc8-3cc0-3e1a-91d0-987f64524fd2 | -5.29317 | -56.01901 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d642d3d2-f1d2-35e8-b2d3-88056889a197 | -4.66532 | -55.64113 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dedd125-f24c-3881-bbcb-30ed86255065 | -2.76334 | -49.47663 | 2026-09-05 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e6ec1959-1488-3847-b5f5-75ec5418ce96 | -5.33315 | -56.02544 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ec93859-0a07-371e-a5e2-c6d811743231 | -6.56046 | -44.77362 | 2026-09-05 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5d864d5-a16d-3fe0-8fe3-ffa254cf77bb | -6.12718 | -57.70085 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cea4411e-347e-378b-b1c1-49046cc8a36c | -5.33334 | -60.1301 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f1a558-44a5-3b88-9aca-c683316ae8ab | -1.83336 | -50.6486 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f563e4f6-472b-35cd-b63b-b62f4120b917 | -3.22924 | -50.57819 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3caa5cec-b7f0-307e-b9d5-4c7af29072f9 | -5.31186 | -56.00778 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a026a245-cda2-3020-8d7d-ddbd2da12521 | -3.38068 | -61.33999 | 2026-09-05 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f43ab8-a3e7-3aa5-b9e6-34f9d45ccaaf | -5.30694 | -56.01762 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edea739c-afdf-3d54-8cc4-cd50390781d4 | -3.78274 | -59.71406 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d44d2aa9-7106-39f0-bd59-15bc8584bc38 | -5.29479 | -56.00866 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f0993cf-1119-3bf1-9424-17a59d670d4a | -2.80521 | -48.67682 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5815a82-977c-348f-97d4-f72547099faf | -3.0723 | -61.08481 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d86bcbe6-2406-3d87-9576-a2eec3782331 | -3.04034 | -59.36522 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77d8e778-3d7b-305e-8a90-55e5df60606e | -6.03544 | -60.16547 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e07bb6b5-5536-328a-a0d5-3eb24dce52f3 | -4.19828 | -59.92962 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cde3f258-24a0-39a6-820a-f143cc8adf5f | -3.79089 | -55.88116 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4caa350-cd6f-342e-8501-ac4d09f616c1 | -4.27908 | -54.77863 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 895fcc96-283a-3537-964d-5cbb29351db5 | -2.855 | -48.55828 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7ca4fdd-099d-39ad-af47-6d075e5afdf8 | -5.29202 | -56.00469 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f352704-d40f-374d-947b-174587167f8d | -3.76673 | -61.76141 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a0cde82-4c7b-3038-ba9d-1688e4e8ed3e | -5.66515 | -60.2414 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1611b1fe-0dd9-3ad6-a6cc-9d112b39969c | -3.46381 | -58.86536 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dcb5024-3048-30f4-9bcc-3692ce47bf23 | -5.76715 | -59.18444 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0d85ebd-e963-3acc-8290-70f3f34f75c3 | -5.30417 | -56.01365 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60d7dc78-e8e4-3249-8ada-8e28c241b003 | -4.67631 | -55.63578 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0367b0ab-9eaf-38b0-8b66-4f55e0a96c4f | -3.14637 | -60.64824 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 587a9c63-58cb-3652-aee2-9856b8a80e14 | -4.24318 | -62.23817 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 965b03bd-d7af-3c14-8fa9-c320ccf35cca | -5.83973 | -60.25213 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 544a0678-6201-3817-bdb8-de6c7f48c45b | -5.52574 | -60.20338 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c12d8eb-3dff-3fd4-9d51-3d88d4e086e4 | -5.17828 | -56.05719 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 853fa7bf-fb1b-3401-b3d4-164398895af8 | -4.43161 | -47.54078 | 2026-09-05 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8afce91-9da6-3534-8516-b0ed05cff223 | -4.66916 | -55.6382 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc5ff7f7-4852-3ec9-937b-c0390c3f9292 | -5.46659 | -60.05476 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89caa35-61ce-3c68-acdc-438438b50151 | -3.77186 | -61.75781 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a5c30e-f476-3eef-b5ff-45124978237b | -5.07725 | -56.28988 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 807fe5b7-2cae-39b1-922e-b17d1e027392 | -5.34969 | -56.02801 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ba91e04a-9ab1-3cd1-9105-62bd7ef7ccd7 | -3.78812 | -55.87718 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5949f30-cee6-3ad0-b24b-ab16289a42ee | -5.31909 | -56.02657 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb27fee-9954-3eba-97d8-9a1523d1e4da | -3.58713 | -51.47574 | 2026-09-05 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a320ea-904a-3c20-a440-c97552a1ce91 | -4.12992 | -56.34386 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e070ecda-8b9c-36df-9919-12c9aa2d3a18 | -3.77629 | -61.75851 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30aa1bcd-231e-365a-b676-236b59cbb05f | -3.62967 | -54.60301 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1122bcd4-686e-3391-9b7c-784168946664 | -5.15042 | -55.95379 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf497d11-1667-3f07-a94f-2f79315c6487 | -5.77002 | -45.06705 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 746866a5-c0a8-3ec8-b336-931e65d1ec98 | -3.42065 | -58.30565 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed6d5a80-5e72-36c5-acde-72ee0d9b44f7 | -1.6688 | -55.50903 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 844c141e-50d2-35e9-a057-e0df633bd411 | -3.25209 | -50.82472 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f77ec82-3dd7-341c-9886-630902c8d781 | -2.47411 | -49.41177 | 2026-09-05 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0f041f2-0378-3c26-9e0e-098ae998e343 | -2.90175 | -57.18536 | 2026-09-05 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a284f59e-a420-37c3-9058-bec7a6b018c0 | -4.43477 | -47.54086 | 2026-09-05 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 857ca7c5-c8b6-3928-b285-9129a8a2df9d | -3.62636 | -54.60249 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0904a193-3108-3c39-be31-2adad178269d | -5.30802 | -56.01071 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5643cec8-5a85-3429-b22a-a9cacba400f2 | -1.18327 | -53.8246 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55c91865-d514-3529-9f22-592c3ddf17bb | -3.77413 | -61.77149 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bcecd6b3-54ac-382c-b8f3-ebc7387666fc | -3.80137 | -55.87923 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dbaef66-5ae0-329c-9c78-9cfab0a36066 | -6.13108 | -59.88926 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3fe5bc-db96-38a9-945d-741e9725c25a | -3.78196 | -59.71888 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd8c02fe-5d91-353e-96db-c1657504f84f | -3.82719 | -60.76856 | 2026-09-05 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00af8e1b-eca1-30b9-be48-f990e5b98c08 | -5.43143 | -60.12329 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d03719c9-dfe2-30c0-8ac0-3ba03fa9550d | -3.83132 | -60.76918 | 2026-09-05 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d77caea6-8fb9-3446-8bee-218b538d6c52 | -4.919 | -55.80048 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7f486cff-042c-3b7b-a96a-5d997135cffd | -5.33592 | -56.0294 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7bc39ee2-a41c-383c-b462-6c3563f38115 | -5.30086 | -56.01314 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a8b99c2-2717-3f97-973f-1c4b1e65d75e | -5.33484 | -56.0363 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd0cef65-fb94-3529-9cf4-9f03a8ae77d8 | -5.29371 | -56.01556 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7c92e45-6315-3cc0-b49d-9bd165ab4f09 | -3.04106 | -59.36061 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e43c60e6-0334-3b16-8f82-0040c291e86b | -3.12246 | -57.69385 | 2026-09-05 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 303ed27d-c76e-37ed-97f2-b859fd709b80 | -3.76898 | -61.77515 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45a681cd-837d-38ab-9afc-5f3415e2f556 | -2.74879 | -60.23689 | 2026-09-05 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdef5993-c43f-3a5f-9f9f-ef9d09724340 | -6.14914 | -59.9444 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b700eb74-4b71-330c-98cd-6030ae919d70 | -5.31632 | -56.02261 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a916841-4d1f-33eb-a29e-9eaf27bcd096 | -5.29809 | -56.00917 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d58e7d4-db97-3c8a-a101-dac89a0d055b | -4.12507 | -49.4559 | 2026-09-05 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fae2586f-715a-3981-8afc-6d615c246ff4 | -3.13868 | -60.64322 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ddd549cf-5064-3302-be95-3391f577f9b5 | -3.44468 | -43.27201 | 2026-09-05 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad7c3599-a47a-38c6-9d86-5545539cd65d | -3.19984 | -61.22857 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac49bb92-557b-3127-8bb4-ab5b0abb3d7e | -3.23359 | -50.5752 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README20.md)
