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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3740d36e-8d9b-3ee9-8b1b-51028c5fa63e | -10.9709 | -61.09 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 246c5492-45f8-3164-93cc-10ab2691614b | -10.96306 | -61.13387 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0778901f-47cc-3efd-8eea-5c266b01b579 | -10.95883 | -61.13313 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa54b059-d7c5-3dea-8355-30760d67d6a6 | -10.95541 | -61.10366 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e16c247e-3b57-3064-98c2-e4f293793046 | -10.95534 | -61.12829 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e98efd73-1af9-34a3-a7c6-1c14d61af3b3 | -10.95472 | -61.10752 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45149737-bf96-32e9-816a-99b6dbf8dae4 | -10.95122 | -61.1028 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab1a8ea0-41a8-34a6-b855-98226c907be2 | -10.95112 | -61.12757 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b553059-09a3-3084-af8b-10aac275af2a | -10.95051 | -61.10674 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c14567f2-1720-3cd3-993e-a6f797fcaee0 | -10.93078 | -60.82328 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce27e119-7ec3-3f9b-bc4d-05f27e8163d3 | -10.92095 | -60.95231 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 07d00a03-504f-36b2-a184-de65e27ab397 | -10.92027 | -60.95617 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6ad1bf6a-47c0-33fa-bf7e-ab2685aee80d | -10.9168 | -60.95144 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e174c73b-d903-3749-8688-13ef4ea5ac23 | -10.91612 | -60.95526 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 562ba3d0-f8c2-3880-a96d-8d81605f1912 | -10.90901 | -60.92233 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcd4a423-8913-3fff-bf5e-8b024ae020ac | -10.90547 | -60.89381 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f59c8196-b08c-3c6c-9f58-8af1a6a42d7e | -10.90199 | -60.88924 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5251cc0-ea72-3695-a640-b0d7db6b573f | -10.9013 | -60.89309 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01f62772-d6ce-3f61-962f-ae841442f7bf | -10.89714 | -60.8924 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0027e439-588d-3363-ba65-aca5d60f2822 | -10.82189 | -61.41287 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5eb6c77-bba2-3e4a-b763-ce5d60b9cb37 | -10.81758 | -61.41206 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fcf3fdc-412e-36e8-a75d-5a2ea18e6f9e | -10.81683 | -61.41624 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0470979-4a30-3f32-b566-b692a42e2946 | -10.81608 | -61.42043 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81a53216-ed90-3899-a14f-db5ed8d5f619 | -10.81178 | -61.41962 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44ad93ab-0a19-3881-a4b7-77c9c6fdbc68 | -13.51923 | -61.74816 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0f16dc2-a5fc-3aba-92c5-9aaba9fe2190 | -13.35581 | -60.57399 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc623b66-43ad-3a66-a946-cb0e7f27a734 | -13.35484 | -60.57943 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5f18edc-6aca-3aa0-8479-e85414455e5c | -13.35094 | -60.5786 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb4b2ee-4238-36de-a0b7-4cd8dd587544 | -13.34998 | -60.584 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dd53d7d-ffbe-3ab1-8f23-8de7147fa349 | -13.34803 | -60.57224 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51dc52d0-fefe-314f-9214-16be18e520ed | -13.34703 | -60.57782 | 2024-10-12 04:59:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7aca6eb-4c3a-3dcb-bce1-5a169a580611 | -13.08481 | -60.48572 | 2024-10-12 04:59:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75769a8-7829-3917-824a-da5631b551bb | -12.83429 | -60.83755 | 2024-10-12 04:59:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc73c94a-a890-33e2-919d-842ad993f93f | -7.98099 | -61.21551 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3056e1e-2c9a-355c-a9fe-18e47fd48ed4 | -7.98023 | -61.21999 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ed1f69-2898-3042-baf0-e3561f5b77ae | -7.97943 | -61.21358 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 868aaf85-7634-3371-bf80-e9b5be56d4b0 | -7.97864 | -61.21804 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a260273d-3f5d-3d43-adba-97bc2c9ca268 | -7.9324 | -61.55609 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6722046-d93a-3bc4-999c-f0fbd42e9c23 | -7.92782 | -61.55532 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0078c7c1-21fe-3fde-9d3d-c8a3a8b02fb7 | -7.92742 | -61.55747 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 244e9def-8241-342f-bb2a-c0bf856d671e | -7.92614 | -61.26643 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1c76d3aa-37ca-38d7-800c-1b03f3fa0fb0 | -7.9073 | -61.51012 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44fca6c2-3eb0-3296-b084-11a153a2ea78 | -7.90546 | -61.46642 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d82e4b9c-c77c-3973-84ce-ee8cd4a8bf66 | -7.90465 | -61.47106 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cc0385b-d23f-34f2-8755-a0a5b8bd3f46 | -7.83801 | -61.50293 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40987f2e-9d47-3d63-beb0-13bf11efde09 | -7.83735 | -61.50392 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c533c70c-1715-3e12-b20e-0ac87c92c164 | -7.82965 | -61.22245 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 441b9f32-031d-3652-b148-4c12e98b2f71 | -7.82887 | -61.22694 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 722248ef-fb7e-364a-9027-1257c2665f9e | -7.82633 | -61.16189 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c151a195-44a6-32a0-bef1-4942617bcbe5 | -7.82555 | -61.16634 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27935faa-1a5d-3fe6-a756-576faec96447 | -7.82109 | -61.16559 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99098b61-a035-3964-956a-ea1b99adc3a7 | -7.74324 | -61.22817 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd339b08-0dd4-3772-b67e-c8b5c7b8abd0 | -7.64954 | -61.19539 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b16bf3f-76e5-3392-9037-ae8c2182ede6 | -7.64877 | -61.1999 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9572398e-2cfd-349c-8246-99a8f3a9b030 | -7.59307 | -61.22777 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39b1e6d9-a39a-302d-9f24-1fd4e5f82b7a | -7.59228 | -61.23234 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a29d6ba-b836-305f-9248-f6f28eb48b65 | -7.58858 | -61.22698 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7096b1d-9473-31dc-a22d-047dc2ed3168 | -7.58778 | -61.23154 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f793633d-f048-311d-b3ab-0fff53858187 | -7.89021 | -61.6642 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3187995d-ca00-3d4e-9120-a1ab2c36660e | -7.82341 | -61.69249 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ce6e2d6-66f4-3b6e-aa4b-0faa213cadeb | -7.81978 | -61.63231 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa4ad0a9-9680-3b52-86d7-f44b01d3134c | -7.81893 | -61.6371 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbd27f89-955b-3dda-8380-dc0fe40d0785 | -7.81808 | -61.64193 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e7204c2-d3b5-3a83-951b-41b3bc306934 | -7.81466 | -61.63768 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bc86454-5783-3ecc-9b9a-ff5490f78a37 | -7.81432 | -61.63632 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c959935-30e1-3b25-b00f-50b483426ed7 | -7.80923 | -61.64169 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8ad20d1-365d-3c96-b9cb-19aa82646d75 | -7.80885 | -61.64034 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8e4e11b-ad0c-3942-b7e3-3fb5c1badab1 | -7.79756 | -62.39231 | 2024-10-12 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5853014a-3ef7-3fe7-b6ae-84c7240eee6e | -9.19747 | -61.69761 | 2024-10-12 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c991ba6d-45b4-3d5f-96da-a074b7c1716e | -9.12896 | -61.29987 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93296b54-8314-33af-8920-9b927164deb4 | -9.10502 | -61.25536 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa757323-0f6a-3610-b223-06c8a7147856 | -9.09321 | -61.169 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8ca367-1b49-3adb-b560-6132170a28c5 | -9.08884 | -61.16827 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c5de4e-f622-3fa6-af05-7c40c52ab5f2 | -9.0888 | -61.16521 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17d8c906-17c4-3425-a69c-7e0365f2f0e7 | -8.07603 | -61.81635 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23fdbf63-1c5e-3986-92e0-edc98f6f57be | -7.97996 | -61.7723 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a0ac275-ead3-3ff6-980e-d852c9975919 | -8.23378 | -61.18618 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bc4361b-49d8-3528-907d-d4d66a0b7b50 | -8.233 | -61.1906 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54b363df-7bab-31a4-9c08-fafc2909767f | -8.23222 | -61.19501 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1148147e-071e-3bdc-92d6-981dbf8ce0e1 | -8.23167 | -61.17216 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab9db16e-60a5-34de-aa44-84db5b92719d | -8.23144 | -61.19943 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4c098a-c01f-33e9-9191-830b71a96b96 | -8.2309 | -61.17654 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a060b8-0c62-3546-9df2-93f2f9684e63 | -8.23013 | -61.18094 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3ffee8e-6d85-3f8f-85cf-ace11f1a3162 | -8.22934 | -61.18538 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fb1682a-f462-3149-93a7-ef5827f0d28f | -8.22856 | -61.1898 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48c70ede-8273-381d-bbc5-fa0415b8a1d3 | -8.22778 | -61.19422 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f096548b-0611-31e5-9c0d-328b5e757007 | -8.227 | -61.19865 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28e9f844-08f6-3215-984b-82446ca8730e | -8.22491 | -61.18461 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4de735a2-1803-31b7-a4ae-307618e5cd27 | -8.22412 | -61.18903 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ae2e56d-9a0d-3924-a2f6-f0675bfc4cdb | -8.22399 | -61.50666 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1af483b1-d857-3799-b199-d35aff2c2431 | -8.22334 | -61.19346 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d61e486b-b8e5-3750-80e9-cc7cee8cf089 | -8.22046 | -61.18385 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcbf962c-941a-3528-94c8-36a2d6949622 | -8.21968 | -61.18828 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a80fac0-e582-361d-9633-31b3eaff8752 | -8.2189 | -61.19272 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12fe877e-1129-3288-9272-0f980362b607 | -8.21631 | -61.18828 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82657018-0f50-38ad-8d62-826fc215894e | -8.21556 | -61.19272 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a91986d7-5ba6-37c7-8bb5-f51804e7c640 | -8.21523 | -61.18755 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ba404cd9-ab0f-3856-8ee1-a0aa6700ded0 | -8.15654 | -61.26943 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8ed347e-5ba4-3312-b71d-ab14aa775e84 | -8.06783 | -61.26113 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d163229a-2325-3867-a566-0bc4dd5c05b6 | -8.06706 | -61.26565 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README84.md)
