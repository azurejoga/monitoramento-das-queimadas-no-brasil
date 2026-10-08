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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9a0848a-071c-35fd-b070-6a3fad7ff6c2 | -3.86044 | -58.64614 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc12a788-89fa-3875-a0cb-7d402e083d5f | -3.05206 | -53.16958 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3a4e595-7d36-30dd-83a5-e9ad00b67564 | -7.88937 | -54.99723 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5d0b54-b3b3-3778-a6e4-78fbe4b26649 | -4.31918 | -50.78061 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 507267ce-ede0-37ef-9cd0-5fef6d5288ae | -6.9295 | -43.65933 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1b6e2642-3bab-31d7-83e9-3b777e9c592d | -3.07496 | -54.25331 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 399a7ec3-f5f7-3c5d-a165-6cd2c937022f | -3.29273 | -54.0644 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eff4ad5-7994-30d3-9b28-13f9e53cd25c | -5.72874 | -45.15756 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99459f27-53e0-3e8c-bfd3-73e9bd12dce6 | -3.54964 | -59.49503 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c065d15-f8ff-3c4f-a70c-dd8d0400ee4f | -2.91389 | -54.11388 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e3738b9-c05b-3b74-83df-0965f77d5ed0 | -2.56932 | -56.15208 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f77e5224-7a10-3f57-b604-a4457ca08a27 | -2.50713 | -56.16199 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e6677f5-fc4e-3acb-92cf-482d20e2cc91 | -3.16584 | -54.73132 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d20d93b-a569-38b0-b7cc-5cd996d3052a | -3.27265 | -54.0273 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 64acc182-908f-3395-89eb-df8d6e8530e9 | -3.30602 | -54.70046 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 498481de-9f62-349e-8379-854bd4e5e68f | -4.30875 | -50.78251 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ebca5a1-fe64-32f2-a516-3af84771a659 | -3.67211 | -54.50315 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a68026bc-b228-3b93-b4ac-809acde0ddbe | -3.77815 | -59.25891 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19e1146-8806-3555-8b4b-b10d2880a503 | -3.00513 | -54.08143 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8c395a72-e729-359b-8c62-73a8add62d37 | -5.04818 | -49.76601 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc843ab-cdc5-381e-91ab-95940d4dfe99 | -10.76966 | -46.58037 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 820f4da1-408c-3165-a870-d337f4eb4b57 | -3.44502 | -59.82721 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85aa8006-9d5d-3e54-86cc-acddd5d3ec47 | -3.05414 | -54.26406 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc73a1fd-3de0-3a93-9788-a32a9ada8cfb | -8.28998 | -50.26678 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| df256fef-c30c-37bf-97a6-1f0eebd9a144 | -8.06215 | -55.29599 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41a535f8-4f2b-3d71-916d-52fb990adfd6 | -2.79499 | -54.08271 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95bf8e06-3c0c-3120-9694-70ba10fbfe12 | -8.08782 | -55.29398 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0acf495d-3441-3bc0-8b0f-1ac689e267c7 | -2.57528 | -56.16906 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5d49cad-1c95-3d9b-ae78-efefbe826217 | -5.48594 | -42.83952 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65fb0312-d993-3066-8dcd-7ebb64e7e8f2 | -6.29 | -43.65254 | 2026-10-08 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fcdbe4f7-966b-3dab-91fd-ebfd9520201b | -8.07397 | -55.29335 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b26b7eb-911e-3c69-83cf-d8a3cffc562c | -4.54144 | -54.98599 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4dd4c2af-8543-3e9b-bd68-3ec5caa7df1e | -3.09972 | -53.71999 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79cb433b-fa8c-3ef3-b27e-3a4e776248fb | -4.64641 | -46.33348 | 2026-10-08 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f2016b-1b37-3890-8552-91587207919e | -11.62743 | -43.69599 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aef23c89-08e4-3935-9cf5-b3ff09443f51 | -9.14666 | -45.82603 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94160ce2-4f5e-3ca0-94d9-767b783ef8ba | -8.07694 | -55.29841 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3bcb9d8-becb-3fa1-80fd-53f0f830c1a7 | -11.09998 | -44.0068 | 2026-10-08 04:46:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1b9a6ff-8fdd-3633-8ed7-bee2ea771842 | -7.14682 | -46.52398 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa59da5c-06e6-37a6-aab3-c4cad58306da | -6.09045 | -53.49871 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e24eb8bb-4dd0-3366-9f71-e19cb059b14e | -5.28406 | -48.10777 | 2026-10-08 04:46:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7142137-bcc6-3ad9-b20f-f399b708b1f5 | -11.63741 | -43.7 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4506ba86-15a6-34f4-bbe1-b736dde2c98a | -3.367 | -50.47276 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8483aaf-ac8b-3271-a8d5-df9ed2d9fa6e | -3.22764 | -54.37097 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e906a6b-6c74-3781-9160-14865659ba60 | -3.05135 | -57.4868 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff4fc925-8cce-3a3f-922c-e9ad991af936 | -5.82343 | -53.83658 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7159453d-a794-39de-be96-12d91b588671 | -3.30355 | -54.04398 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5110cf55-123b-3030-a7d8-3e3f69c50a00 | -2.99406 | -54.07972 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 9ca6f6eb-18f5-397d-95cd-85b3a326de04 | -3.08226 | -53.9502 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 85d60bb6-507e-3b54-a994-b0987f77531c | -6.92932 | -43.66447 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 25f87b04-937c-3a92-b6dc-f0b022158d54 | -2.75603 | -54.11278 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 039bdfa9-663b-3f6f-a2b6-1b47698b58d4 | -2.58326 | -56.14621 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bdae4cf-4eb1-341e-a2f4-91e2446d4a52 | -6.66667 | -55.08334 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 05af1e27-29b7-3ee5-8787-51cc5e60ba0d | -2.79199 | -54.07775 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f58dab29-ead9-38f4-8399-69753d3d9442 | -3.04046 | -54.14532 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1707b4cf-bb4d-3e4f-9b12-1aabd5565a08 | -3.00059 | -54.76557 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af6da9c0-bfaf-3e99-8d67-7e4caba3fe6b | -3.656 | -54.28265 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8c27cc6-275c-37ee-a9c6-7ea6327f9ebc | -5.71868 | -41.72079 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fae242c6-6efb-3e1a-9adb-60ad13a67f84 | -6.82174 | -39.54671 | 2026-10-08 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04397c19-4b49-39eb-9ec4-2e3ef91315c5 | -6.32867 | -43.35041 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38940c11-fa94-35dd-991d-8e831f810048 | -3.80208 | -47.49027 | 2026-10-08 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39917185-4594-3f0f-80aa-9460d175778c | -5.59358 | -47.2785 | 2026-10-08 04:46:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51543c8c-fd78-39fe-b0d2-746bb60594e6 | -3.70846 | -59.67403 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e93f9321-35ee-34d1-91dd-ade83e74e8ef | -2.76556 | -54.1007 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37540d1b-a5bb-3a0a-88f7-496b43c2abc2 | -8.04287 | -49.83863 | 2026-10-08 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbc4c34-fa77-3209-b288-b4be9c90cf9d | -6.81137 | -55.29377 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35dce4a4-e4c1-3b87-8a0f-4756b37a1a7c | -5.37273 | -55.88263 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ff84fe-09ba-35f8-9c99-3a05d5ca667e | -3.01874 | -54.04338 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab5d3fc8-bf83-37ba-8dd4-ce556a65d769 | -11.32358 | -46.66449 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 847ff185-20fe-3fca-90c3-860a916cba31 | -6.08902 | -55.7354 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4db138b-9555-3947-a0b1-a1d9601142bb | -6.22507 | -55.61976 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4227a05e-a998-3ea3-9f99-46c1bc057705 | -9.79029 | -47.8636 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 507d23ce-1f3f-3bd0-9a98-df76ea90d593 | -5.96455 | -55.36229 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 66b189bf-572b-3d9d-b7a5-5a1e1d1d8380 | -11.39627 | -47.54998 | 2026-10-08 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234a9bd4-82e9-30d0-89b2-3927e7161dd5 | -3.10782 | -54.19053 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2b7c1428-0186-31d9-b14b-2ef5ada236f8 | -7.40936 | -55.57908 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43ceffab-17d0-3fc6-b2c4-0ccff1cbbb14 | -2.47648 | -56.10905 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f4ce964-34ce-3647-b2eb-14e8641dd1dd | -3.53695 | -54.66631 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9ae5be5-d3a5-38d4-b74c-2b1b6a185b77 | -6.15457 | -39.43237 | 2026-10-08 04:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 666bf767-3ffa-3cbc-bc38-c2738c714ae1 | -3.66355 | -57.09383 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03a994e3-eb9e-3688-8813-41970a797496 | -2.76469 | -54.08248 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2287886-5689-3962-bd02-4867193b90a9 | -4.09386 | -52.06587 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dab12fe-3b7a-3087-a031-0dc2d9db906e | -3.28156 | -54.04051 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d04968-eb0f-349b-854c-648d37ed537e | -3.57849 | -54.64939 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e08116c3-4963-3116-be1e-98be16b75706 | -3.04348 | -54.15031 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44e4a6d4-1bd3-389e-8b05-fc5f289cfd23 | -3.05215 | -53.95119 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 03050c91-abf5-355b-9c42-3bd2f0c4384a | -3.09167 | -53.93843 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 19737b06-b11f-37cf-84af-835a88410e89 | -3.05159 | -53.90725 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 254772d9-43a3-36a9-bde5-80c335292ae2 | -4.60571 | -55.72016 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef957088-5ab0-336d-9589-176536ccb286 | -3.22987 | -54.29943 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bae3be8e-78c6-3358-9686-00cabb02e7b9 | -5.26564 | -45.40628 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2f5141d-b3b6-3088-92cb-97763b502504 | -11.10743 | -45.67624 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8872eeb-6ed7-3a82-88df-cfce3af4b15d | -3.58792 | -54.56621 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 80126697-c0d8-3527-9eca-315c5c044edb | -7.13888 | -46.52272 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec0b412f-acdd-3861-9594-10bd5bc9b494 | -4.08708 | -48.95884 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4abcd2a1-087f-3137-8ef8-a255db8d3fa3 | -5.24542 | -50.90896 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb749656-2f86-3819-9c99-6bfaf9f6b0d3 | -2.38962 | -56.13694 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b49e7ef-19b8-3f10-9ce5-81142175e061 | -3.70591 | -55.964 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4db7d0c5-9ccf-34cc-adb9-1da5d1a684de | -3.27999 | -54.02704 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd52f953-470b-36a6-b5e0-954aaf967689 | -7.466 | -42.8239 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README96.md)
