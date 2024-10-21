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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f7c36fb-caf5-3f66-9225-6e7da47ccfa3 | -3.09038 | -54.17239 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 2e949572-bcd8-3174-ab2b-88fa3c652f48 | -3.08814 | -54.18717 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b5e5dae-f4d3-38f3-b687-c59f3f533410 | -3.0879 | -54.43576 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1febbdd5-aa61-3623-9130-8938fe2d30ac | -4.30783 | -55.41397 | 2024-10-21 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ea29396-1690-301b-b019-ab86c01a7354 | -4.30347 | -55.41327 | 2024-10-21 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acbe2a67-9cc4-3398-ab7e-27c9f35c6516 | -3.62567 | -54.67219 | 2024-10-21 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6617cd2f-c5a4-34b3-9e3e-a048da56d003 | -3.55107 | -55.44101 | 2024-10-21 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b8385d1-86b9-3b9c-81ca-e514637a8448 | -3.47964 | -55.38798 | 2024-10-21 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc1964b3-4f2a-3302-818a-2afd8e15cd79 | -3.47702 | -55.38967 | 2024-10-21 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ec4b29b-b7b7-372e-861d-2edbcc249b5d | -3.47533 | -55.38727 | 2024-10-21 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb6da85-6032-3d1e-847d-90831b079109 | -4.73224 | -56.07717 | 2024-10-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f7b0650-e87e-39fa-89b8-ed16a1613a2f | -4.73168 | -56.08094 | 2024-10-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3ce6aa-d4ff-3f53-870a-cbb8bb475611 | -3.95218 | -56.16969 | 2024-10-21 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf09a45-9c0a-3195-8cb6-bb6156b16dd3 | -2.98159 | -59.20851 | 2024-10-21 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e53fb7a-64f7-3436-b44a-ff7c3258501c | -5.31409 | -60.12328 | 2024-10-21 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9988064c-6551-3e57-8ac8-66a246543527 | -2.95416 | -60.01375 | 2024-10-21 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ec36cf3-e770-31e5-9019-cb4d30732293 | -7.86385 | -63.78072 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b21ebc-f9a1-3497-81e3-b9a0f5e7aa99 | -7.86049 | -63.78018 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2485f29-922b-3307-9806-a70b0ff0e3b6 | -7.76902 | -63.33225 | 2024-10-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f4a3f10-1473-393d-aecf-099a65b3d902 | -7.88513 | -63.77678 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 662027ae-24c7-3afb-b1ef-cff89b3013a8 | -7.88177 | -63.77624 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a6c4c35b-6b1d-34a4-ba7c-8545a15216b5 | -7.8812 | -63.77982 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7b7e8b2e-78da-3041-b14d-109e74784761 | -7.87842 | -63.7757 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e84cae4-bc33-3ce7-a1ab-9f20f74a707f | -7.87784 | -63.77928 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 178dbcbe-0c01-3819-a20b-4fa71f8774de | -7.87506 | -63.77517 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fd7eda8-9eda-3a6a-8d71-004cf84166a2 | -7.87449 | -63.77875 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f51a3614-f31e-302e-8ee7-9e606aa140a6 | -7.87171 | -63.77463 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5828742b-84ca-3f22-aaa2-7e9d44ddafe3 | -7.87113 | -63.77821 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34836a0e-a11b-3a0d-ab96-780a3f29abdf | -7.87056 | -63.7818 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed10c8b2-e1b3-35f5-aa0d-ddf070474907 | -6.97539 | -63.94984 | 2024-10-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79222c5f-813c-32bd-8ddd-cb3fb3372979 | -9.37506 | -66.48555 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f10f464f-4a5f-3db9-94ff-644a9f0226e4 | -9.3743 | -66.49 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ad594b2-f906-33d5-b539-1a1360e9a9dd | -9.37136 | -66.48492 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 362ae4c6-2b64-34ba-a35e-e3891c3f4d6a | -9.37061 | -66.48938 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5100f244-2b39-33e5-be9e-b105253d659c | -9.36767 | -66.48431 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 570c7dc5-299a-31ca-8108-9a7aec390e40 | -9.36691 | -66.48875 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b15c8b97-4e54-3256-a0f8-ac1b10f35003 | -9.36321 | -66.48812 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84cd6759-779a-3983-81f8-d205c47a48e9 | -9.34852 | -65.90918 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b031a1-9f44-387a-a616-b8e99ba69411 | -9.34647 | -65.90994 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 824964aa-25c3-388a-b4da-b587119668e9 | -15.30924 | -53.31759 | 2024-10-21 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 148c97ae-c95c-3765-9155-f436a2c802d0 | -15.30875 | -53.322 | 2024-10-21 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44cda902-b6fa-35aa-b287-08f0465e0d94 | -15.30828 | -53.31804 | 2024-10-21 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e64b3313-33ee-38ba-86fa-ac9da62a328f | -15.30782 | -53.32244 | 2024-10-21 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6422c3ea-fddc-3643-b002-49a59fe6279d | -11.8696 | -56.88276 | 2024-10-21 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20207153-9545-3ef6-bfba-3aee472247d4 | -11.86637 | -56.87335 | 2024-10-21 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a248b55-4dc8-3a8a-af2f-10d1f1f594d7 | -11.86577 | -56.8778 | 2024-10-21 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a310fa8d-933a-3da4-8f13-4e84123f8b5d | -11.86518 | -56.88218 | 2024-10-21 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b029a78-1ce6-3a6d-bc22-088a31211d56 | -15.62113 | -57.86007 | 2024-10-21 05:31:00 | NOAA-21 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6401ca6a-c754-3f4f-aec2-5651367fd11c | -11.81691 | -57.36645 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6cb63f2-5244-3709-b718-8d1f439d351b | -11.81264 | -57.36584 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98530520-9d7a-378a-b52f-47635fbb2cba | -15.53536 | -58.01393 | 2024-10-21 05:31:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d24a53d9-2964-3450-a335-7afe8791d089 | -9.45706 | -59.22882 | 2024-10-21 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eae81a1-47ce-3636-87a5-bb9759f6b452 | -10.83433 | -58.60639 | 2024-10-21 05:31:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ba1abcb-dd44-3ac6-bcb6-827f9b52ade3 | -15.66907 | -59.75356 | 2024-10-21 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4d0ecc-10f3-3cfe-bd6e-bcef58c4b783 | -12.18025 | -60.68311 | 2024-10-21 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 128710d4-714b-3053-9490-be9c59548a70 | -12.17966 | -60.68715 | 2024-10-21 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17036d99-aac8-39e8-8106-d473b5f70a44 | -12.17673 | -60.68254 | 2024-10-21 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23365038-80da-36a5-b66f-5bb7c75b9aa5 | -11.50793 | -60.72967 | 2024-10-21 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 602609a4-14dd-3954-9d0f-a2aee30eef4c | -11.50734 | -60.73367 | 2024-10-21 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 991c88a6-4e39-3e73-8052-9b2618acd240 | -12.2784 | -61.53301 | 2024-10-21 05:31:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96aecc74-90d8-3255-a45b-8a6adca9665d | -9.17591 | -62.65547 | 2024-10-21 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5be0229-70a1-326b-8ad4-b7d9df0bdc46 | -9.17536 | -62.65895 | 2024-10-21 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0435baab-3d8c-3a20-ac1e-93dd04d94833 | -9.15632 | -61.97338 | 2024-10-21 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1137627-7ad0-3465-96b6-426298d40170 | -9.37944 | -62.35629 | 2024-10-21 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b02793f-6b24-362e-833a-d2f3479d54cf | -10.5328 | -62.61567 | 2024-10-21 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f58a366c-06b9-38de-8911-2452df968df2 | -10.53226 | -62.61917 | 2024-10-21 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b29a43bb-6d6e-3cd5-9ae0-90dd6c18bed7 | -10.5295 | -62.61514 | 2024-10-21 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe7fe045-b58d-3489-b836-1faabe55e7f6 | -10.52895 | -62.61864 | 2024-10-21 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3574958-e8ff-3b76-9809-b8970ddb40a4 | -12.17433 | -63.3216 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d600a74-689f-34fc-805a-5b6a8b61b200 | -12.00202 | -63.11783 | 2024-10-21 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 956e76a4-0b3a-3ffb-9204-646614894d58 | -12.00147 | -63.12134 | 2024-10-21 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dad184d-7198-39c9-ae5e-412640bcbd6a | -12.16679 | -62.15773 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20d2be7-8349-3296-b539-f616acadfb2f | -12.16344 | -62.15719 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e413dbe4-92db-3912-bdd2-bd5d5309439e | -11.94451 | -63.1799 | 2024-10-21 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 477dbd9d-14b1-3c21-99f9-014e4c33ffb6 | -11.94121 | -63.17937 | 2024-10-21 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac13c36f-45bf-3cc1-879f-d149c8c1f758 | -12.5506 | -63.28545 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b63ed33-3d9a-3dd0-b56d-62c775a701a7 | -12.54785 | -63.28139 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f08e411-ecb5-3ee1-9e59-11074f8d7409 | -12.5473 | -63.28491 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b94c12f-8f4c-332e-ba37-5dc5a70d770a | -12.54675 | -63.28843 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ee936791-40fe-3e4e-819e-2e94341dc7de | -12.5462 | -63.29195 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26644c3b-ddb3-36bf-bed9-2ab7d3912444 | -12.54565 | -63.29547 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b580c6b9-2b3b-3b96-bd76-a6be7521079c | -12.54564 | -63.27383 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f297423d-6d88-33ab-adb2-c9715e00ed65 | -12.54509 | -63.27734 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb66f650-5e5c-3a8e-bc6f-0b46fb844608 | -12.54455 | -63.28086 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75b19d64-8e5b-3f05-88cf-138c0949671b | -12.544 | -63.28438 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 246cd837-1c41-3b65-a6ca-96f0e60f9065 | -12.54345 | -63.2879 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bcaaf9c-0069-38fd-8b86-ef498f062244 | -12.54234 | -63.2733 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45537e79-6312-3c40-8298-b86c5a21cd05 | -12.5418 | -63.29845 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b21e293-42ed-3256-9816-5cd0f7c3f68f | -12.54179 | -63.27681 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28e4c3eb-0055-3f15-8244-c5aa4016dba1 | -12.54124 | -63.28033 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e1fe693-b302-39a7-93d5-10279b8fe197 | -12.53958 | -63.26925 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbc0d0c4-44ae-3d74-ad01-736e9b45719d | -12.53897 | -63.18623 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 412c3755-942e-3543-a8c6-1fe53f093691 | -12.53792 | -63.25816 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daf842b8-0631-35a4-abf7-38f44c2de5c8 | -12.5374 | -63.30495 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b5b9a09-a8cc-370e-a854-8c96b57e8d86 | -12.53732 | -63.19679 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11070761-64a5-3352-9797-0268cb72e423 | -12.53685 | -63.30846 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9a05a50-57e7-3725-8ffd-d4cdb27ea6a2 | -12.53576 | -63.33712 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34eb6b17-0e08-3434-b3e4-be06cf395c15 | -12.53566 | -63.1857 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df5b63b-f8c5-337d-99d4-91d53a973cf6 | -12.53462 | -63.25762 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed38be3c-7444-3b83-8841-796d8ddff257 | -12.53457 | -63.19273 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
