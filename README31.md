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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f941a7-f48a-31c2-94af-eb34dbc3130c | -2.28355 | -46.64462 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18b78713-73a8-30b4-95c3-ff3875811a2f | -2.28288 | -46.6487 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0040d549-349e-3324-91d5-b45fc05dff8a | -2.28272 | -46.75893 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaf1996d-f29a-37fb-8620-e4f1dd5d353d | -2.28015 | -46.13226 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05322ef3-0e05-3cf7-8120-4b899d2fc291 | -2.27857 | -46.648 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b53f0f9-f852-36d3-a3b1-39fe9478d48c | -2.27844 | -46.11641 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f656fcc0-2841-3afe-9049-07da285acf12 | -2.26764 | -46.76936 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0196fb2-441b-3bd2-bdc4-a4efb32c751c | -2.2607 | -46.30656 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e674c6-e3b9-388d-950f-62522b182957 | -2.55291 | -47.3219 | 2024-10-28 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5688bee-30b5-3419-bba0-efeff3eba7e5 | -2.54842 | -47.32114 | 2024-10-28 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e5fdbe6-7a2a-3bf5-9541-d6e0cc34a884 | -2.54466 | -47.31583 | 2024-10-28 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac439c1-b323-30af-9eb9-08bbd78c8be9 | -2.54113 | -47.36651 | 2024-10-28 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4d05b0-47ff-3329-a15b-10163408fd71 | -3.96385 | -46.21267 | 2024-10-28 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1749990-0dc9-3be8-9ab6-4045ff2ea7fb | -3.95977 | -46.21204 | 2024-10-28 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f23793-bb6b-3b12-8137-c00a186ef41f | -3.95915 | -46.21576 | 2024-10-28 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e5e84e-34ff-39b3-be3c-dc4e80e4640f | -3.95752 | -46.40366 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 783593c0-c8a6-307a-9e9d-96492f8bb4a4 | -3.95695 | -46.40715 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9ade018a-c21c-3c34-a8c4-7eadc09bcb1c | -3.95452 | -46.42185 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8de516fb-25e0-39a3-a636-1e340c0ac7af | -3.95339 | -46.40296 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0915f32-0ea8-3bfd-9b38-dfcac6fe1a33 | -3.95281 | -46.40651 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 57c58455-42b0-31a7-85c6-aaa9bcf6b3bc | -3.95223 | -46.41 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fa622fb3-e75e-3485-bb4f-b46f8fe1ae9f | -3.95102 | -46.41735 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e975152-ce94-3f4c-8146-9e62642cfe6b | -3.9504 | -46.4211 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff64ce5-d111-3119-8f63-838710927591 | -3.91169 | -46.44924 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3ce06a7-57b1-3a92-a0c2-df56f66d7609 | -3.90967 | -46.44902 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97b900b1-c5ae-3521-bebe-151ee7ba951d | -3.90551 | -46.44841 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf932284-4a09-337f-85c0-d5795b635b33 | -3.83291 | -46.47534 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e0f61f-f84d-3ac4-9083-cfe131d9ff50 | -3.83226 | -46.47927 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57efe139-565b-3635-a5cc-3d362c6823e7 | -3.83163 | -46.4831 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 841960f6-eb00-3a78-94ec-b2170cb1d8a7 | -3.82396 | -46.4778 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0fb8fa-82d7-37e8-bab0-bc4e6e939de9 | -3.82043 | -46.47334 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f3aa6d2-ff39-3050-ace8-43595ab9ad73 | -3.81979 | -46.4772 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42e229a5-b538-3f91-928c-35bff22f227c | -3.81914 | -46.48109 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55e25ed0-23e1-394e-bbc4-fcba55e7d324 | -3.64678 | -47.4881 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 979e0772-6db6-3965-8aa6-32e9a526e08c | -3.64399 | -47.48974 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f2970f-b5fb-3b89-800b-4cfda3db4add | -3.61722 | -47.26132 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5bd6af1f-00d3-3b34-a92d-b67ef7af85d9 | -3.61651 | -47.26564 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e032865-ab1c-3d4e-a231-c4183c1ba9f6 | -3.61298 | -47.28712 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8b62118-7f06-3a9e-8f09-f220e7eac21d | -3.61284 | -47.26047 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e8144f0b-519d-3b2e-8b89-721fb0c84377 | -3.61213 | -47.26477 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fccef6f2-fb3a-34f1-b87c-d3a5f56f01ab | -3.61092 | -47.29967 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8e70f19-18a3-3678-b385-35b015726061 | -3.60846 | -47.25958 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e01ec4f-a3d7-3e25-a3be-e7dd2d516141 | -3.60721 | -47.29465 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e055ab0-1ccc-3bf3-9c2b-540813bd8bda | -3.6065 | -47.29898 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 432c8932-c1e9-3b7c-82ef-6ecb41129d1a | -3.60279 | -47.29397 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65819ee1-c978-3d36-b438-b8e9af260a49 | -3.59171 | -47.27879 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 588997ae-ae0a-32f1-a8b2-a90d82fa8186 | -3.591 | -47.28309 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 771f6fb1-1b33-3db0-89d6-40e0fe791c8c | -3.58732 | -47.27792 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce2a314c-4fcf-3957-a81d-b855a2a53d53 | -3.58661 | -47.28222 | 2024-10-28 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e799957a-76cb-3176-8d14-3c60b2dc69d6 | -3.81341 | -46.94009 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6c6d94b-9191-36be-9a21-8fa7e773ef8f | -3.81272 | -46.94436 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce4a8f40-e501-38e3-862c-3ad6486bb9c7 | -3.8098 | -46.93515 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33f361c-0e51-3092-8ac5-e6a658de8a77 | -3.80617 | -46.93034 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a448336-a9d7-3d8a-a7bb-eca2a46064d4 | -2.04189 | -48.03137 | 2024-10-28 04:04:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 554f6fe9-c03a-3551-9723-542d61c2c858 | -2.04186 | -48.02967 | 2024-10-28 04:04:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17078c69-1556-3bdd-8a1c-ecc782e6a2e5 | -1.97351 | -48.43236 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4361b187-1123-3cfb-a3f1-1687d8715cf3 | -1.97263 | -48.43793 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 088e1d7b-4cc8-3d84-8dfb-ac41245122e4 | -1.97042 | -48.43318 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe0dfb56-9908-3e1c-a8ec-e99a99c588e6 | -1.9695 | -48.43871 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 119dfbc7-ef8c-3e97-bdfb-b62fb24735f8 | -1.9614 | -47.95353 | 2024-10-28 04:04:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e578d07b-7006-3d52-80ca-671c143a5c3c | -1.94827 | -47.91508 | 2024-10-28 04:04:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa26c22a-32f5-345d-86bc-0d216283e644 | -1.78291 | -47.84237 | 2024-10-28 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13f63720-b306-3a8e-b09c-771113e3f79a | -1.77819 | -47.8416 | 2024-10-28 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3b61a9e-3514-32ba-9347-3abb819730fa | -1.52785 | -47.2061 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa977e5e-8bc7-3c38-82cd-096e161ca82b | -1.52468 | -47.20298 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9651eb23-b12a-3ab6-86c6-2d2b0d5b59fe | -1.52394 | -47.20754 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 089a614c-df52-340d-89da-7485fed76e75 | -1.52333 | -47.20527 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e394ae6-7ee6-3519-b517-7b8b393e9766 | -1.52261 | -47.20985 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f44854f-74ac-36e1-90fb-3831520d039d | -1.09102 | -47.23827 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fe29264-dc08-31e5-9192-b1fed044ddec | -1.09066 | -47.24097 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a26e348-753f-31bd-9e40-ff6d79dc28be | -1.09026 | -47.24295 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 137f1741-1090-39ad-91dc-e322f7786c3d | -1.08721 | -47.23283 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76c00916-a9fc-36fb-b865-4902a88140f7 | -1.08681 | -47.23552 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 498ad3c3-9774-344e-98d4-450756360614 | -1.08644 | -47.23752 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68b0cc34-8f23-3e80-a4b9-838877109ccd | -1.08264 | -47.23206 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab28cd2-3c90-350f-ad83-224c0c82e6df | -1.08224 | -47.23471 | 2024-10-28 04:04:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dffde8f6-b951-3371-b271-8fc7674ef30b | -1.05777 | -48.2611 | 2024-10-28 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 431ec9a5-91d0-39cb-ae28-d80e746b830f | -3.45578 | -47.66988 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b9ea8e6-7e02-3d2f-9837-934f770088ab | -3.10632 | -48.60806 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7bd4bc0-a860-3230-8ffa-f1098e73cca8 | -3.10145 | -48.60727 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c842455d-4d4f-3ea4-b039-97f5e9dc3333 | -3.0106 | -48.76119 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3eaa3d7-6d83-3404-842d-96918b1c7567 | -3.00942 | -48.7598 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5bda603-3b7e-345d-9add-76c19b5031f6 | -3.0085 | -48.0983 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9057903-d91c-33b7-9780-df6209ff3a16 | -3.00724 | -48.09559 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53e66ab7-8f49-30cc-b296-92409ff45b85 | -2.95672 | -48.9601 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 497f4461-344a-3623-a31b-b6e82fa2adf7 | -2.95623 | -48.96301 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56f3a3cd-7090-3274-8f3a-d4a59b28a94c | -2.92064 | -48.96188 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4acc6ca2-9684-3dcb-acb4-ffc2be1f8dd7 | -2.81512 | -48.43875 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63b9de9a-5ceb-3ae2-bb8f-594f269847b0 | -2.81426 | -48.4441 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d165ac5a-8cd7-3c7c-8c24-42afd4e0a324 | -2.77391 | -48.69453 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d4fdffd-dee1-3054-bddc-c16ee2395ad5 | -2.76899 | -48.69371 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b13ffde-4ec7-3cf9-aff6-eb6a34505b51 | -2.7654 | -48.71589 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5dffb76-3990-3088-8e81-99ce1b33a966 | -2.76047 | -48.71507 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 067a4480-e4f1-327c-a88a-e069d58cc7fe | -2.68587 | -48.64576 | 2024-10-28 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c39e1d-9c7d-329f-ba5a-7f7c0b1c838d | -2.61892 | -48.3168 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e5b54cf-57f0-3266-8b69-15d59648aa02 | -2.53065 | -47.37408 | 2024-10-28 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a157de28-8602-36ea-afdc-f5a032e19bc7 | -2.52411 | -47.44349 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f57f795-8df0-30b4-bbf1-95b71c1caee9 | -2.52336 | -47.44812 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a348ef56-978a-380d-8337-b80308e4dfda | -2.52262 | -47.45274 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ab499af-259c-3029-a750-993bb561987b | -2.51958 | -47.4427 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README32.md)
