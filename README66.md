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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e142f4f3-6ce6-3bff-bc3c-f330d38149cf | -6.83674 | -46.04432 | 2026-09-21 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a386f561-6c9b-3fa3-bd81-150f91c43836 | -5.81589 | -53.52131 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c69178-d702-39e6-816f-27df5bfc38a1 | -2.87548 | -57.79711 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 60d09ac3-66d9-33d5-91ba-030c1b91f2c2 | -6.11272 | -57.7469 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa81502c-2944-38cf-8b21-306b4fb05f73 | -5.75877 | -57.58972 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2761d52f-60a9-3984-9de4-9772872e31ab | -3.40299 | -61.29764 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d56839a-8744-3acc-b4c4-cfc634940283 | -5.60644 | -44.84136 | 2026-09-21 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 161eb9c8-f6a1-3fdb-9df3-6677c5c5662e | -1.36287 | -49.30703 | 2026-09-21 05:04:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbb44f71-35ad-3830-9412-2b012d6080b3 | -4.3022 | -56.26272 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 04ceefbe-cba0-3cd9-913f-5a0601f3f7c1 | -3.17561 | -58.58754 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd217e6-e856-37a1-97eb-2e01940d73f1 | -3.68565 | -60.59404 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e23206c4-1146-3af8-8c0d-deac8ac22cb4 | -3.48273 | -54.71528 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6a49c8e-ca3d-3143-9b1c-7170cc63b46d | -6.18861 | -57.77821 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b870c73-8a52-3e7e-bf97-204ee8588f5f | -7.38311 | -46.03781 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df5e4c60-88f5-300c-ab38-11553069d23d | -5.83854 | -53.48944 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d308cad6-1dc8-3f0d-b8bf-5d78a161df09 | -3.73881 | -51.81845 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083669fe-768d-326c-b03a-e7166a44ab62 | -3.7527 | -58.3285 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a36e8a7-b4d8-3e35-84dd-5fce8d7a78c0 | -2.87013 | -57.80833 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9373a239-bced-3c91-88b2-f1ca1be48463 | -4.3461 | -55.65768 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 916fca98-5731-34cf-bd57-8ded03a76a25 | -2.17227 | -48.32111 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 830b38b6-4b9e-32f7-8565-a86dab5515be | -5.83958 | -53.47347 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ebe80b2-f32d-3e70-af36-3d4f7f9fda0e | -3.06373 | -61.2752 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee897454-26b6-34c0-8bd7-02ac4d7092bd | -3.4433 | -50.5994 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f4a77e5-e3e3-3981-9249-69d8078cb990 | -5.89151 | -53.64575 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb8a3d2d-5e6b-3411-9eca-911c581ff3c9 | -2.45399 | -50.37321 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9ba4e5-eb51-3ea0-8d4a-9a126f489eb9 | -5.97991 | -57.78688 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ee7751-2371-3b47-ade1-548c730f37a0 | -3.18988 | -57.8726 | 2026-09-21 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b561517c-7243-38fe-bab6-4a52b72ef6e5 | -6.51185 | -55.22588 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7257934c-8090-3d7c-b433-70d69723c65e | -6.9295 | -55.62631 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85e4dc76-d295-3dae-9a29-73096d3b6d5e | -5.85867 | -53.48837 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 757deaed-5ee5-3a62-a646-c589112385a9 | -6.77176 | -55.63316 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4fdb00-b55d-3963-8b23-8bef7660a9ce | -6.10024 | -57.62846 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b98c8f91-8e40-3126-bb2b-df02a48b0982 | -3.75864 | -59.41954 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d922bc2-ac85-3db7-98fa-f744bbff8bcc | -2.79261 | -59.89396 | 2026-09-21 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66ef2cbf-1a17-3a3e-8f95-2bf8828fe29a | -5.01333 | -56.09086 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db91419c-38ef-30b3-a1c6-59ec8df4489b | -5.37258 | -55.90395 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c68f616-7ca8-3867-9e28-1c3908a96e55 | -3.33236 | -59.81795 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae7e2a3c-d816-3a6e-9c55-edf28dc3097b | -5.01555 | -56.09829 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 694747a2-ce3c-3cce-9a82-06d7918a3114 | -7.41162 | -44.77661 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4e1823d4-3b71-3f08-9b42-67992d35dc68 | -5.21243 | -56.07655 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a3ee535-d669-3e96-b480-fb287abc989d | -5.84368 | -53.51733 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 973dbb35-14db-39bd-98ad-6dfd2de5dd13 | -6.13685 | -59.93993 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a761b137-f47c-38c9-be1c-24614f71c2ba | -5.38471 | -55.9129 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8886c3f-6f18-33cb-91af-c77f3668e09c | -5.8354 | -57.54558 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d92ad18e-fe33-3621-9deb-cefb37905f9f | -7.34453 | -44.46557 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3120c83-708a-3e95-98fe-cd02c331239c | -5.84485 | -53.53318 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 517978c7-15d3-315e-98fc-72cf86b592a4 | -3.33397 | -59.8081 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d53b8aa0-fc13-3aa3-b62c-089227b933c2 | -3.75789 | -59.42414 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| efa66dcb-3e3f-3167-b6ef-8b8715941aa8 | -5.89093 | -53.64952 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75926343-671c-35ce-8fb2-917083861476 | -4.87847 | -55.88608 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 554926f4-a752-3dea-9afd-0e6cdb867da5 | -5.98607 | -57.70464 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008d0c2d-2ccb-385c-9a37-75c4200f4e93 | -6.28898 | -57.74479 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 69d7dd16-81fa-3bcc-8f91-f6ccb44fa416 | -5.83913 | -53.4856 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b1734a-05f0-32b8-8363-4a2a10ed0083 | -6.10717 | -55.64211 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c603ac-0463-3a37-aa52-ba8c4b99100b | -2.94953 | -51.0403 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f98b40b-e591-3ee5-9034-9bf7f9755576 | -5.76615 | -57.58714 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d881d0d1-8ed2-3ec4-aacc-9ee8de17a3c5 | -5.85061 | -53.51838 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd47b334-5cbf-34c2-a00e-b01ebec0724a | -6.1232 | -59.95192 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7e5c32b-c60e-33e3-9071-da153de44ee8 | -3.10929 | -60.72248 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f28c4d9-3b50-317a-bd5a-c7f476453177 | -3.48053 | -59.60046 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b76bdae5-3b2f-3de9-b726-b200414f4ca8 | -3.69963 | -60.63729 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1cc94c0-2270-3252-9c4d-406ccec1df49 | -4.35044 | -55.49998 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1d32baf-1948-388b-8cc6-0d26afef2ba9 | -3.3302 | -58.13342 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38b54b1f-640c-35f6-b35a-95508237ae4c | -3.66437 | -58.86355 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2683d852-f9b8-3fce-ba72-b656cb396a5f | -3.82259 | -58.88165 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 379e1c9c-8cdf-3439-a948-5284289c4b07 | -3.48208 | -59.59092 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f207c813-004e-3178-9807-8f1efe6ae305 | -3.00659 | -54.16745 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 440aa12c-f5bd-3924-956d-e9e053c06bc1 | -5.76896 | -57.59134 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2e28470-c99c-353f-9fdd-6ff5c015b27b | -6.33741 | -59.95009 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a79c54b-a7ae-3e18-86c6-074642a4ea7d | -5.81877 | -53.5257 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3882bea-0378-3203-8f3d-d8e00dc181f6 | -3.06439 | -61.27109 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce3797bb-bdcd-3640-9c5a-4d78bd63278b | -6.53931 | -44.92702 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b506e24e-3919-365d-848a-a3816ad9fc01 | -6.08478 | -55.54673 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ec53e8f-6dd6-37bc-a2a8-cc5cd05a4272 | -6.66141 | -50.93714 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e944fc99-5bcc-324f-bd08-97b0c2abf80d | -1.20067 | -54.16549 | 2026-09-21 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50c96539-de47-36d1-8789-92ef526c020e | -6.12422 | -55.6412 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ed4d4b-1975-315d-8a72-32c47a3bb352 | -5.76218 | -57.45205 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9832e707-2999-3f1d-be73-55c5f2a4fc80 | -4.40766 | -55.24129 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c19a6fa-3910-3c5b-b16c-6c46e00c9e06 | -6.20165 | -57.78406 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 74c5915b-1f8e-3d44-843d-dbbf7399692b | -6.92628 | -55.64711 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 217e92eb-704e-3de8-8ea9-5870fafb0a9b | -2.96605 | -54.16478 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807b3635-b277-3906-b985-e5ecc9f50811 | -5.42 | -60.22751 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12b6fd49-9cc2-341e-b267-32adc1c2fb99 | -3.31195 | -57.86275 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d485b04-f0b7-3539-9a49-ed0577a3a242 | -6.68287 | -51.59855 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28013455-5f1a-3fc6-9eb0-78178294e792 | -6.19601 | -57.7756 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dad41ee0-56ce-32a2-bdbb-18391da61daa | -6.83135 | -55.53581 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| b64fc5ae-ddf3-36f5-8c18-da1f20da467e | -3.4497 | -50.61076 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fabf0efa-66ed-3b13-ae5b-1ba0490a3425 | -6.62273 | -51.43174 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e394a725-9f82-3764-b0e4-6e1a8eea1db0 | -2.82092 | -50.46749 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71797f4c-6df7-3216-9071-d1898f39e4a5 | -7.08526 | -46.28537 | 2026-09-21 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e68695d-7275-3334-b491-9e0fdd0646ec | -2.91734 | -57.78754 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d5bde69-1dbb-3f7e-b488-81f8ed08cfae | -1.32785 | -54.66026 | 2026-09-21 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10b178c8-461c-3ea5-8841-6786b98ca17c | -5.83169 | -52.05301 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d69bf9be-ff12-38f5-b4c2-b021fc6e6d90 | -3.87917 | -59.56495 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b71e83b9-3b2c-34f6-91ed-da243eb4c5b7 | -3.69383 | -60.56937 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af53c333-fca9-378b-b303-118af02eeb6f | -1.50919 | -57.74766 | 2026-09-21 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d5add92-f997-3fd3-9d2c-8793e2d16b37 | -7.03469 | -55.62832 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a956ff7-2412-3e07-a655-fc6ef60788cd | -3.39933 | -61.29292 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91348fbd-920e-3642-95b1-b260b5fa74f9 | -7.71144 | -49.38555 | 2026-09-21 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3b68116-e49f-3bbd-a541-f208cf32d609 | -2.74088 | -54.58576 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README67.md)
