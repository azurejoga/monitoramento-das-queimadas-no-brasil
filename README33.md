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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84b936fe-dda0-36ac-a0da-db7b3682f63c | -3.77728 | -61.7615 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46590a7-16b0-3b6f-b4cc-8caefa0108f6 | -3.77176 | -61.7666 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c3fa201-eb30-3c7a-92d8-4b80bb481c39 | -2.58728 | -59.40509 | 2026-09-05 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c85d4c80-5712-3fb4-baf5-075e115dc661 | -5.34473 | -56.03085 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3a45f795-ce7b-320d-be3a-d6ba647e6ccd | -2.59236 | -59.40589 | 2026-09-05 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1cc2d92-111d-318c-9403-41153e0fa4c9 | -4.66819 | -55.63702 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea429a50-ab40-3920-8b00-687938055f93 | -6.69216 | -59.98495 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94137b00-9722-361d-92e1-1d79e7117d35 | -5.3449 | -56.03983 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e3d2a84a-dcae-3e58-a3e6-439e19a16cc7 | -5.16935 | -56.0597 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33f985bd-0c36-3a2e-9746-370744cd57fb | -6.66658 | -59.94016 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9580f046-4851-384a-b1b0-7849da3b28e0 | -5.21346 | -60.03302 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 688e4f59-8da7-363a-8a4d-4c69f793e6e6 | -5.14581 | -55.95017 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c713ae-b4f1-3ad4-bdee-ba2f60ead399 | -3.78256 | -59.71893 | 2026-09-05 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19d65d1-b34b-3987-a765-f05d56eccd16 | -5.30774 | -56.01738 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9cbf71c-6843-3e0c-96d6-4ba6ccd847f7 | -5.15003 | -55.95605 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61ffb5f6-fad4-355a-bbfb-09482dbb9af2 | -6.66614 | -59.94334 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a398d85c-9b3e-3eeb-b542-dd20eec4a2be | -3.77491 | -61.77579 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d6ca2a1-e42c-3b34-9851-9412c4b9c3f6 | -6.58447 | -59.915 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db5903a2-71ad-3b9b-aa13-940dcb5b97d4 | -3.93401 | -59.34228 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c439df87-58ec-39e1-9f45-0e4ec33e0f77 | -3.03935 | -59.36248 | 2026-09-05 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6ad1b21-27a8-3dc7-a84c-e20c504d7620 | -5.34397 | -56.03647 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ad13ab88-a60f-35f7-b4a1-2248360ad221 | -1.77542 | -56.24302 | 2026-09-05 05:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01865f79-36ea-394e-85f9-e095550f43d1 | -5.33991 | -56.02763 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8da71c0f-a7ac-39e3-8520-6a012bb647bd | -5.15081 | -55.95027 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c7dcd29-669d-3338-93fa-b5511dd9337b | -5.33233 | -60.13241 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 969551cb-5217-314f-8b11-a0266f7631eb | -5.34626 | -56.01953 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff215ba0-3df6-31c4-a1ef-005f82bcb678 | -5.17012 | -56.05416 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d86dd8f9-4ebb-3dfd-95d2-e4c3bc15ba30 | -5.34981 | -56.04295 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2def24a9-3b1a-3984-84fe-591447684b94 | -4.6824 | -55.63315 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11ef976f-63e4-3f67-b432-5685c1e62f0f | -3.77091 | -61.77364 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9148eb1d-0a77-384f-a674-bcbed402de63 | -6.67181 | -59.94084 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fc09bd7-14fa-3352-af1e-f4e9ec9fe814 | -5.76561 | -59.18294 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9df51fee-40d7-3b7c-af2a-6a052b903b4f | -6.02726 | -60.17213 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d6095c9-b828-3818-b8dc-e8c164bc5eaa | -3.19788 | -61.23055 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 166661ea-c85d-3340-8449-ccc518bb95cc | -6.67048 | -59.95032 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8802a40-b8d6-30d9-bbf0-fbf6b5ac90a6 | -5.76342 | -59.1838 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d4d25b7-8b06-387f-bccc-9a9b73fb2197 | -3.9336 | -59.34163 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 349be9cf-a7df-37dd-a137-4444fe8c9f54 | -5.33738 | -56.03554 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 36c3c392-4ecb-31b9-be25-c061c8d4ee02 | -3.75967 | -61.75888 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b132e039-17c0-3ab5-b188-4f83816b8329 | -6.58968 | -59.91578 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597d7ec5-d3ca-3609-845a-7743bcc93d2f | -4.41448 | -59.87284 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d975d8a-7ea9-3cd4-967a-923285c0afa2 | -5.16858 | -56.06525 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89008c8e-0c79-3400-900d-3c2e587b6e87 | -5.30115 | -56.01648 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00a818fc-5122-3c62-abaa-e90610a881df | -6.2021 | -57.76815 | 2026-09-05 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b7fa0e7-58b3-316d-bde5-d86f55c94446 | -5.33911 | -56.03329 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16eaf3bb-0f3e-395e-b92d-827989e3c56d | -5.83592 | -60.25529 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23060d1d-94ef-3056-ba64-325e1476964a | -3.14174 | -60.64501 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d10e5532-10b0-3ac7-9f9f-77dfd6a1d07f | -5.84138 | -60.25307 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22f0896d-1d40-3697-89d0-0de8b235c020 | -5.5565 | -60.17344 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17234f17-09c5-3934-ae67-1c1e1d333cde | -3.13779 | -60.63929 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 72ebd603-c004-314f-b737-c2e656b90b1a | -2.91546 | -60.99417 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43895128-a38a-3904-8399-f3fe1f36db3e | -3.14569 | -60.65075 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0c1a8e5-693d-39c4-8f1c-57f1fbb5584f | -5.33173 | -56.03796 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ec10133-0f32-3ffa-9198-3d46e9704fe9 | -3.77596 | -61.77005 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72e3a4e5-0f05-3669-af1a-52ccc6e52902 | -6.65617 | -59.9385 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f10becdd-db47-3d3a-a30b-d686dd934ac3 | -5.15242 | -55.95104 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0957ebd1-a383-3fe3-842c-02b63af0a2e0 | -5.846 | -60.25684 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f1cdaa7-c34e-39ca-b517-7d755067ffad | -5.33149 | -60.13828 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9e77007-dcdb-3559-a889-001d8d8ab186 | -4.67915 | -55.63095 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a26c57eb-5d20-34b5-9c3f-60ae5baf3ba0 | -5.25203 | -59.9807 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd241800-e22c-3c61-ab92-0c125296ff02 | -6.65917 | -59.95514 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3dbe573-d528-3633-86ab-f242286ecb25 | -6.12805 | -59.92465 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6d080a-63b9-3fe8-b1dc-1fb051841617 | -5.47072 | -60.06057 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9fc5cd-65d2-3a7d-82e4-c74d5bd8e812 | -6.67092 | -59.9472 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c98e5a1-4722-3752-9b84-2eab82c95bde | -3.75902 | -61.76316 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca902443-419c-3d05-a44b-97fa024719c6 | -5.14343 | -55.95509 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313e86db-81c0-3b55-a3a3-037f537a4d1f | -6.13324 | -59.92538 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c732bcc-735f-3fdf-b405-c565b3ccd41b | -6.65052 | -59.94084 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fa2d68c4-c23b-3989-8b0c-5b7c6e7cb7b2 | -5.16945 | -56.0657 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4146af0-6ad9-32b8-af0c-c8d4ff2ff56c | -6.65573 | -59.94167 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d78e42a-ad69-371b-a0d7-407367a540b1 | -6.15178 | -59.94364 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54755e55-4e37-399c-857c-ac48b1f172f5 | -2.91409 | -61.00188 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 957a191b-d536-34ea-8adb-1e633d6f95c8 | -5.3473 | -56.02294 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3894985f-a6fa-37ac-b166-4fb00edc5980 | -4.19606 | -59.93352 | 2026-09-05 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9497a10e-e57f-3d87-9f51-7e858464feae | -6.59536 | -59.91329 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d24d925-10dc-34c4-919e-426f6ccbfbe5 | -6.68395 | -59.96796 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a46fea1f-ec5c-3986-91e2-7beb3f78caf8 | -6.12849 | -59.92154 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 454be6a5-9421-3c5d-8c53-83d762073fba | -5.17107 | -56.05458 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cf35b1e-2488-39e5-97d7-4f4b2b7dd454 | -6.64876 | -59.95354 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ba115cab-a210-31ce-ad6f-20534f79cbd4 | -6.5949 | -59.91654 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6ec36dd-2c80-3019-82d5-d98c6111b369 | -3.1472 | -60.64081 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a96307e-7560-36aa-aec3-5b0bd38bf642 | -6.65484 | -59.94804 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 543376f9-5917-3c63-bfd2-f49b33bbe52f | -3.77156 | -61.76938 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75dabc5e-56d1-3413-8ca9-dfa0577c1f87 | -6.65829 | -59.96149 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 902f99c9-79fc-3039-9e65-6c09edf283d2 | -5.30854 | -56.01171 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b513add-56f0-3d48-841b-c3b5566167ad | -6.65961 | -59.95199 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70023c13-b84a-3192-8a7e-4c473de21c7e | -6.6835 | -59.97111 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f603250e-7212-3ce3-bb7f-217ee789877b | -4.41491 | -59.86991 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24dbc5d1-2fe8-357e-8231-bfc5408ef265 | -3.79019 | -55.88087 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0df0914f-fab5-3878-aefa-c7a2db8500d6 | -3.82909 | -60.7673 | 2026-09-05 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7ffaa2de-1ced-3d7d-aa00-c64ea5ed62e8 | -5.46182 | -60.05021 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39d73e5-711a-3db9-a634-24493069db2f | -3.77301 | -61.75802 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ecf559-583b-37f1-8444-0a6750b9ba27 | -6.68262 | -59.97739 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b7c507-3a11-3e42-b0ad-5584dce0ddec | -6.6492 | -59.95037 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1f8d1ac1-4ffc-364f-b528-562fed2f32f6 | -6.66439 | -59.95583 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87fddb1d-9cc3-3f2b-aeac-bf7df47da69a | -6.59014 | -59.91258 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5099b566-b332-3fea-a9fb-c1981cffdada | -6.66395 | -59.95899 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c0277ef-0385-3748-99b4-cff8adf8c05b | -5.31277 | -56.02954 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e231c12d-f986-34b3-aac7-444cdeb7ec64 | -5.35058 | -56.03727 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e10813ba-bb4a-3fbe-b9fd-282f04d7a0f5 | -3.72086 | -59.36988 | 2026-09-05 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
