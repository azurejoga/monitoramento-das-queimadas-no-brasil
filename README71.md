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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae91d3ea-7b64-3e7b-8d78-797303cd3d9c | -3.00464 | -54.23032 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88384316-c702-3285-a508-8d28f4f64531 | -3.17597 | -54.09759 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce26313e-6cd4-3959-9bb6-706318e674bd | -4.26551 | -50.78217 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 992e4f9d-a3f8-3a18-bb75-12b6ecdca13b | -5.86003 | -53.47641 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9909c9d9-5a7f-3bad-ae27-f24a2faf1c8f | -2.50263 | -56.90911 | 2026-10-02 05:33:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e00f0845-44cf-3f73-8767-5636a9624be4 | -4.27237 | -50.77329 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4477b6c-c574-322f-9b1d-823de06c2179 | -4.27679 | -50.78064 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc947fa4-f7b5-3db7-bd93-d6b34374860a | -4.29747 | -49.09521 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a59a2495-d893-376b-8f99-0b5ad1318658 | -4.29208 | -49.08991 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1c55d62-058a-3012-b77c-f15b05857616 | -4.25824 | -50.75682 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65f9e0da-9f49-3a16-8fcc-7fdf32375e57 | -3.17471 | -54.07731 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6044c9a6-c96b-316d-88de-370413601f69 | -3.8834 | -51.89841 | 2026-10-02 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb987543-b6ac-3ed3-afe2-c83eaf24a007 | -3.18446 | -54.09868 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10957900-b379-3e80-afc1-5b39c5449a94 | -4.42543 | -54.84841 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69930c3f-9f90-38bb-ac59-ae347cd27cee | -3.04651 | -53.87867 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91213e90-ff8a-357f-b4a1-a495dc4275ec | -1.90933 | -55.0462 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd9c0d0d-7306-3d26-86f7-4bfceb38ece2 | -4.45274 | -54.9109 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 801bb130-42b1-3ec5-b11a-afbd65f1465e | -3.17352 | -54.08521 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93e454de-bb0f-3ca1-997a-0ef8e38e975b | -4.27062 | -50.74799 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4032c95-08ce-3c38-ade0-739f75d1724b | -3.93668 | -56.05421 | 2026-10-02 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9fa84d-b200-3e68-abe8-c1e1ade22664 | -4.29351 | -50.77961 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fb29ee2-2d4e-392d-a1d6-758baedbbc8c | -0.24606 | -48.48822 | 2026-10-02 05:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48596826-78dd-3ca8-8ed6-159de1a35b8e | -2.90249 | -54.14184 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a432518-23de-364d-a889-958c7f77acaf | -3.28687 | -53.85955 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3670e65-dbcf-3cb1-b4c2-6d249d00d0c6 | -4.45694 | -47.91853 | 2026-10-02 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| d0f31e0f-4cbc-3af7-a2eb-c2e343da26c9 | -3.16505 | -54.0839 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 249870b8-cc6e-3fd7-8687-3d04a1df0304 | -4.26113 | -50.77452 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c4266f-67ff-3b89-b209-bcbfd95275f8 | -3.1808 | -54.09426 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf3aa569-5ea3-322a-8e1e-469c9f5c60a1 | -3.011 | -53.88159 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17e72a1d-22f9-3d1b-87c5-9199ee9fb87e | -2.88244 | -54.87878 | 2026-10-02 05:33:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa3530e9-ae42-3d51-be34-18d60c04b4bd | -2.9912 | -51.04658 | 2026-10-02 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2f71f48-aef5-3de0-931b-5ab8659c79d4 | -4.27287 | -50.76994 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e15c7c26-80c3-3c64-825f-a13d7ec9848d | -3.16751 | -54.09629 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c35bad6f-583c-304d-afb6-9591139f49af | -5.11989 | -56.02209 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4afc5607-39de-330e-831c-d9783a5108bb | -4.04202 | -54.2341 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb29165a-524b-324d-acee-33f55d7a320b | -4.27161 | -50.74137 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7bff7cd-6e21-3d63-a285-8dc65610a02e | -3.28595 | -53.85054 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 231fe688-ab68-3079-8594-dc29fe6939ca | -3.46966 | -54.62406 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf9a0ca-a441-3321-912b-9a00d5a983da | -4.45616 | -47.92393 | 2026-10-02 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 924a0c47-c452-3556-afc9-4c43a5f73c83 | -3.16623 | -54.07607 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bad60bd6-033e-3e18-be3a-d6f69b944efc | -3.01161 | -53.87757 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c748946-995b-3e8e-b1dc-06b183879a00 | -2.93442 | -54.15728 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b30019-0962-3652-84c9-63f239bbb33b | -2.89291 | -54.14813 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6b85bfb-79b3-33a8-b101-3a1bb6ebca4b | -3.00244 | -53.88028 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51e33619-a602-3aef-8ba3-106f9c8cad17 | -4.31111 | -50.78163 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 725de35d-e6ac-3f7b-be52-0496d1631c71 | -5.00763 | -56.28291 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e379404-bba2-3097-b97a-13661b6380e0 | -4.27913 | -50.77353 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38576a3-04e3-3651-a634-44caf733ee2e | -4.2665 | -50.77553 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 420c026b-cc8e-3615-80b0-53fc13004701 | -3.28775 | -53.83841 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f1693c2e-f260-36a6-8c69-22025627e7f2 | -3.03488 | -53.8688 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b8b52f2-78e1-33a6-970a-9484ee7c3047 | -3.14811 | -53.74825 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 905cb2fe-459f-39a4-a10a-733ab9150439 | -3.29206 | -53.83908 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de69e13d-7e73-3066-9337-7ebf81215f69 | -0.40112 | -51.83896 | 2026-10-02 05:33:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f82fd3f0-1b60-3ab8-a087-3fb96693e677 | 2.8855 | -60.28492 | 2026-10-02 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce275ee-d4dc-338a-a91f-c00a33156072 | -3.5882 | -54.52527 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dde0e5f-4e0c-3d10-bf8c-f50a3371a25e | -4.16779 | -56.3054 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a639ec3-736b-3d4d-adb1-19a8b853f13f | -5.67441 | -50.09361 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df9c6b6-256e-3890-9d5e-b6ec5f8a0658 | -3.68657 | -55.48795 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3e28c3d-f4ea-3f94-ba82-003af1dc2bc7 | -3.28079 | -53.84204 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1e5bb109-9a5a-39f1-92e7-3e6ad334369b | -3.01039 | -53.8856 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 579f53fd-47dc-3411-aa01-ec6c77b6b36c | -3.00611 | -53.88494 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5778a608-a76f-3498-82b0-42c1240d1bc7 | -2.85631 | -54.13474 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28a33368-55f7-36d3-96f9-671d77be7e9f | -4.06553 | -51.11324 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1a2dcb2-b8e3-338a-b159-d6b9124f6660 | -1.60547 | -55.12716 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9673fc88-75fa-3061-a1ec-8416f3199728 | -5.8956 | -53.49005 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30214de3-fa64-3779-8673-a83ae7420fd5 | -3.29826 | -53.85662 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 302e5add-d9b6-3652-8ba9-21515f2ffa72 | -3.29893 | -57.85223 | 2026-10-02 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6562d4bf-02cb-39db-be09-cbb323c3b91b | -1.60765 | -54.75379 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b28bc32-277f-3e1d-b619-080417e6ffa5 | -2.90907 | -54.09969 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599ee217-8391-3298-bc96-176d5376ec67 | -4.30518 | -50.7844 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a9ccdb-b6cd-325e-a561-83e4d50cc33c | -4.2747 | -50.76588 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4909cbe-3926-3fd1-8318-4d3832b920a8 | -4.27935 | -50.76359 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd69b298-2fe5-34d0-b90d-c973e9c36c04 | -5.13996 | -49.86764 | 2026-10-02 05:33:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| facf3443-b783-3df6-8a94-27a1a61eb223 | -4.27371 | -50.77285 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f15a5ff6-06f1-3819-a86c-5b1e511441de | -4.29537 | -50.77583 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dec4018e-c7c9-3194-ae97-5bf8a7ed298c | -3.17538 | -54.10149 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b866aafa-7410-32a2-bf24-a0f7ef45efec | -3.28572 | -53.8387 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 89761c54-db02-3bda-8bb4-575880fab2a8 | -5.89415 | -53.49979 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d6e347d-c031-3c4a-9f6b-66bdf722b389 | -4.45773 | -47.91313 | 2026-10-02 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46a13767-0c3f-32c1-a4c2-642323552a2c | -3.18021 | -54.09819 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| df5927c0-14d8-31c5-bdd8-542fa3180c11 | -1.63491 | -55.14154 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 980766ab-bf96-3100-aae3-93b1015a135c | -3.8519 | -55.8096 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f60e9b76-149a-39b8-9e09-c72e570a33be | -4.2831 | -50.78439 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e94fdd-58d2-33e2-a640-5d22fb48221c | -3.17046 | -54.07675 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8339fa48-77be-3a17-948c-e95f501567ae | -2.93229 | -54.19974 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03baa0f5-644e-329e-b6c3-9a09a6e4ada5 | -4.28269 | -50.7781 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58cef9a-611a-310b-8dea-6af5652ceabf | -1.46553 | -48.90686 | 2026-10-02 05:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4918de9d-eb62-3360-be5e-e23c563dfc0d | -4.26163 | -50.77119 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 392aabb2-2d40-3b47-8655-7e023d2cfbfe | -4.27963 | -50.77009 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1b166ba-4888-3045-ac50-e9938bda51f5 | -4.25926 | -50.74998 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f611c339-3d47-3828-8e13-f60f8b357dae | -4.27717 | -50.74854 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40d4908a-86dd-343b-a5c3-0f84fd303235 | -1.63877 | -55.14216 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83e825c-a37d-30cd-a416-cbbddc26b068 | -3.61803 | -51.79847 | 2026-10-02 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1888ae3-c02b-31c0-a3dc-73cc3ffbec34 | -5.86459 | -53.47734 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5492d8b4-9c83-3077-98c7-3a8b32aaf041 | -4.28811 | -50.77882 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ce1ff34-91cd-32bb-88b2-c3ec217fca58 | -4.28914 | -50.77202 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f336e5a-5198-39ac-9b2c-7a3eee671777 | -3.30257 | -53.85729 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97d295f4-84c0-329d-99d8-a9781646351a | -4.28321 | -50.77469 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86806d19-af0f-3270-abf1-58080e1bd210 | -3.22573 | -54.31205 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8afb1d8-47bd-3706-8165-41f4b5c60479 | -4.275 | -50.7557 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README72.md)
