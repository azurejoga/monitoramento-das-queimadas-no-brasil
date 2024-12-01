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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83d1272c-cee3-35d6-9d57-8496f36cb55c | -2.89634 | -55.22762 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7da406d-d370-3719-9b81-b942af094ba4 | -2.41481 | -54.01167 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a20fe99-2bd0-344f-83a6-84c3024a118d | -4.17421 | -54.93827 | 2024-12-01 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daa1011a-e48b-31a4-8f40-381103f915aa | -2.98217 | -53.89698 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 475614b5-66b2-350b-b7c3-999025401d36 | -1.30093 | -55.74407 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebe057ed-5ff0-34d8-b343-cb6ab95cc30d | -2.77737 | -54.05046 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a26c9fc6-216b-356d-b273-f0ac9898a020 | -2.46319 | -53.95223 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1272c597-37c0-3096-88a0-ee760743c6a6 | -4.45579 | -56.18307 | 2024-12-01 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e9c3ea1-ed5b-3625-9c6b-4bf101606dda | -2.27103 | -53.46631 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74ec6c8f-421c-3eda-aee8-26339dee0de4 | -2.63488 | -46.88046 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0d450b5-5bcf-3c74-8a2d-87c6e6852e81 | -3.06314 | -53.8162 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a912f7c-72ad-3c11-98f8-e57debed3633 | -1.72419 | -52.4882 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dbb3fa2-95c8-38ec-92e0-19f205405414 | -1.61934 | -53.88392 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f338773a-8c49-3bbc-8f28-3a26f3e90f0d | -2.35303 | -53.91693 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5b79234-0f8d-31ea-b919-bf4da5ad4905 | -4.55767 | -43.30459 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdf53e0b-f53c-398f-897d-a5b26c5af1a2 | -2.46072 | -53.71015 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4085d22a-1d1c-3c67-be8e-ae90ccfd5ee7 | -2.03026 | -53.50068 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b479fff0-d4a6-38af-9565-0c4141a85b54 | -3.23868 | -53.63691 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4dab9a1f-b62f-33b5-9f7b-34b295c84e6a | -2.60007 | -54.35723 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea3a414c-7011-374c-8970-4044f61d25ee | -1.46294 | -54.36887 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4c3bc82-9457-37e0-83f3-03bc791a4c22 | -3.65851 | -50.71056 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1abbe38-207d-335a-9cd3-e3baf2058e76 | -4.47416 | -50.7677 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 245793b8-fbd7-3bb3-9ee4-4589d65bb5fa | -1.40057 | -55.21685 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afd48338-2192-3768-b133-8b4cd5072a06 | -2.86267 | -54.03848 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51dd2392-6267-3620-a492-d42ce1c144c9 | -3.03761 | -54.04903 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0c83aa9-5722-34a9-b0ad-536b84700464 | -3.46509 | -50.53347 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09bcbb4d-3127-30d5-953e-dd42b3f0c43c | -2.44078 | -53.62981 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5794cf5c-724d-3e30-80e8-51abbf18d78c | -1.89033 | -50.65143 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 388680e2-8424-3a3a-9490-d2e77d9461e3 | -2.55706 | -54.34338 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a36d8cc1-4d53-3b4e-84fa-57b242ca5662 | -3.69036 | -51.80748 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d43101aa-bf0f-36f4-93ea-693e07f80495 | -2.83754 | -54.10943 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5096801-4b3a-3e56-9e4a-36e1df356292 | -2.79828 | -54.05368 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fe35c2f-b2a3-3f0f-91cc-944911491a84 | -2.79996 | -53.05292 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad19c77f-ef8c-380d-ad37-1f9155543d7e | -0.1415 | -60.8668 | 2024-12-01 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7965c93-f250-33ff-80c7-1f3a0e96515d | -2.52845 | -54.07189 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f89abf7-d76d-3cca-9ea9-fa52b6ebec4a | -2.89197 | -53.98752 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe52d14-29fc-3509-842c-b803fe887b57 | -1.43619 | -54.92359 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5c2f49-c9c4-3631-b0a7-a9d9df993410 | -2.03126 | -52.08171 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 111f7642-9288-38c7-b66b-a61bad1c71ee | -2.95974 | -53.8979 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e1f6f3e-f1ab-38f3-b1c0-502017d2cfea | -2.89907 | -53.96473 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01d70cca-bd18-3e51-859a-a57451895403 | -3.69333 | -51.81477 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16da0359-11dd-392f-9e35-435eb001500f | -3.03183 | -54.04023 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ec062b8-6f71-30a9-bf9f-c7e4db6a4552 | -2.57573 | -51.88435 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a851aca-ad07-30cb-aec7-b566067b70be | -3.11193 | -54.26776 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cf66494-871f-3333-b2e0-36588d245fa6 | -2.8845 | -53.33154 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0bd53e-2054-326a-833b-f5aa0107c009 | -1.38042 | -53.64901 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423ebd83-9dab-33d1-b570-8d1ae2ea8927 | -3.0615 | -53.27119 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5c85885-8bb5-3ab8-8473-31e64931558a | -2.91119 | -54.11682 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9697e2b-0ed3-3221-9efb-603eb6f2749c | -3.73023 | -54.22903 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e539b319-7312-3bf4-b270-4e268ed5a4eb | -3.69163 | -51.33849 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e781776-74f2-313f-b5db-798183933117 | -1.76249 | -53.63979 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a17e3c0d-ace5-39c7-b4bc-3575dad42a5c | -3.53046 | -53.79018 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97ae4d35-20a2-35c1-bbd5-b4d7de60bbed | -2.25173 | -53.63491 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f679755b-3c47-3acb-90b1-62951c641538 | -4.41235 | -50.69716 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54a74fa9-a4c8-3ae8-b43d-e29d932a2b6e | -1.93435 | -53.44236 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eab602ed-c3d7-35f9-bdd3-96e9c4ad0975 | -3.30469 | -53.86825 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0917871a-479d-3df1-a76a-33880632abff | -3.24942 | -50.61678 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e09fca5-2b5e-3e92-a1cd-cbe4cd6c62d1 | -1.70726 | -52.767 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c626639d-5e68-3d8e-89b5-e9e4ed5e1443 | -2.63425 | -54.20447 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3288d46-caf9-331c-a76b-8abd437c18bc | -3.52724 | -62.77188 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4961f488-aebd-39c3-97a2-21a22e1c3611 | -4.11013 | -48.88933 | 2024-12-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fa375f3-12c4-39b4-9fc5-ef919a8e9abc | -3.14754 | -53.24901 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf6ed5fe-3c36-3976-987f-a8f7e240ef88 | -3.41181 | -51.97655 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 22111b53-d178-3be2-96b0-f0b6d034421f | -3.77327 | -51.6769 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 273b7385-37f2-3213-a64f-60865ec9ad96 | -2.92158 | -54.27008 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a3a7b6-9d92-3efd-8a97-eb401e4d1246 | -3.69385 | -51.81137 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0d0d49b-bda9-3dec-91d1-e41b75fe4390 | -2.82314 | -54.07716 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 896a87b3-5c6f-332c-8202-25406f45690f | -3.12596 | -53.09775 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f639b92-c123-361e-97e1-82be919532c6 | -2.98224 | -53.87289 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1eb6971-7bdf-309c-883c-a8e1922d2e63 | -2.73924 | -54.97335 | 2024-12-01 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 83be3a5b-29f4-3a03-98f3-45d0ce65c7db | -2.60351 | -54.35777 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0744a583-8256-366c-b72f-58523bd996c3 | -2.61241 | -54.08101 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e53b3a7a-e9a2-3f63-a58c-118b8f9f132f | -0.14038 | -60.86628 | 2024-12-01 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f89fd827-45a2-3d1a-b2e1-cdac5b956284 | -2.44501 | -54.00061 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f384f2d-eb9a-32d0-b5ad-8f01ceb5c662 | -3.08475 | -51.07786 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd77d9bf-3d2b-351c-b85d-b16705e75539 | -4.07733 | -50.0266 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b65ff927-8e53-329c-b3fd-b25837822852 | -3.78758 | -58.97697 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7941edcc-59ca-3de2-9c07-87a7ac96bf80 | -3.32804 | -50.19107 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1279869d-f63b-32a9-b387-9f92aefd284b | -2.81459 | -53.05518 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f2fbf7c5-b23b-33c9-88ed-da2fdd80ca7b | -3.7671 | -54.44186 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76b0be5-1f51-3fda-817b-13d9a8058ada | -2.85156 | -54.06438 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28d69eec-3b37-3f15-962b-c03367092583 | -2.63078 | -54.20396 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66c647fa-5803-3e7c-a79e-2459b6ccebfe | -1.44284 | -54.51867 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9218fdc6-ece5-37f5-a6ab-8587aa783828 | -3.26195 | -53.62804 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 76488f70-f525-329c-a0ed-de9b856f104a | -3.02942 | -54.05568 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88219c70-4f75-36c5-9a95-3a562c1a2b86 | -2.86407 | -53.32019 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eb4cda9-9a78-3b44-b01b-4bd36a4bb98b | -3.66842 | -52.29788 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5d10239-9a92-3c69-b738-0f6f3dad0b7b | -3.69392 | -51.34202 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4919978-1627-352d-9172-c2ceeac38684 | -2.76145 | -54.1304 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb4ab49-e75b-36ff-b48b-648f6d70cbda | -1.59918 | -52.29623 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4783144e-3c24-3efe-9f04-ed1d20cbe972 | -1.45411 | -54.96256 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04eba92d-24aa-39ca-94e2-f94d6d3d3157 | -2.04471 | -54.70572 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f73ff52-b4ac-3f56-b8a6-6808954861bb | -2.83676 | -54.03588 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 113da3ed-788d-34ac-b306-c368fd4bb33f | -6.19 | -44.42662 | 2024-12-01 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 034478cd-b139-3540-ac35-6f7db310645e | -4.62226 | -48.02999 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c46c7404-b86d-34fe-a347-6bf6aaffa8aa | -3.99079 | -46.65625 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32814729-0793-3ea0-b056-74d7fa2000d3 | -3.79451 | -58.97808 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ac4c3c0-2edd-3211-afa8-835b9e8f3d1f | -1.43107 | -55.19651 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bce1a858-38bc-3587-89a1-aa2b134c1bf6 | -2.84577 | -54.0556 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20113113-a5b0-377e-a61e-5c364cef9d2c | -3.08693 | -51.07885 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README87.md)
