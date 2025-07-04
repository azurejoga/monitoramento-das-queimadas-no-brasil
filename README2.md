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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccad3aa3-4b7c-3d7b-87de-69d32412e903 | -6.2945 | -43.6659 | 2025-07-04 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 48000055-5335-3a69-ba30-ca4123db2867 | -6.6112 | -43.8941 | 2025-07-04 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2dd5b441-51d8-3ffe-bd2e-6189fd74bb28 | -6.6115 | -43.8709 | 2025-07-04 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 865250f0-9bd6-3fd0-897c-4549512fa9ff | -18.4486 | -54.6674 | 2025-07-04 00:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d248cb53-9023-32a6-96f9-ebb43571b832 | -17.9386 | -50.6021 | 2025-07-04 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a5d7077a-f380-33fb-af07-e037f4f27d27 | -11.9128 | -45.3919 | 2025-07-04 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 8ee25772-aacf-3472-abe2-8ec2139065bf | -17.959 | -50.5764 | 2025-07-04 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b69fbe85-b211-3dba-a4ed-0dc6bd24ff37 | -7.2405 | -43.0899 | 2025-07-04 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 4570c9cf-04cb-3075-9a12-b38a3758cbff | -17.9784 | -50.595 | 2025-07-04 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8ec75fe7-c242-396a-9e32-dd13009f5b1e | -11.9132 | -45.3688 | 2025-07-04 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8b9844de-7a25-3253-8388-66fcaf8f4598 | -10.5586 | -49.1337 | 2025-07-04 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 18223dc4-162a-3701-a823-2d01484f70e6 | -6.2755 | -43.6907 | 2025-07-04 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 3dc6224e-2367-31f6-9074-873ff8757440 | -11.932 | -45.389 | 2025-07-04 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| d0af8764-2801-35b1-8a92-d7bff2220347 | -12.424 | -43.7274 | 2025-07-04 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f641139f-26fc-3dc4-b24b-edfcd26a3b9b | -6.2755 | -43.6907 | 2025-07-04 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| a24a0165-bd88-3d06-aff1-36103e26661c | -6.2943 | -43.6891 | 2025-07-04 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 42764f49-c4f1-30d1-b905-4ec8cb9033ee | -6.6112 | -43.8941 | 2025-07-04 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2f833ceb-e8dc-3b2a-80d8-18af973202d2 | -10.5586 | -49.1337 | 2025-07-04 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9793a298-f7a7-3d38-aaaa-11fba37fc8b0 | -11.9128 | -45.3919 | 2025-07-04 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 1adf5ef2-c0b2-33de-85f0-6b8cd2a2973d | -18.4486 | -54.6674 | 2025-07-04 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 78aecab8-7806-3540-a997-de6aff482379 | -6.2945 | -43.6659 | 2025-07-04 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 4840f340-7830-3ae3-90cb-017d29e9590b | -6.2757 | -43.6675 | 2025-07-04 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| fd3da15e-25d5-39dc-961d-a5ddf5faf491 | -17.9585 | -50.5985 | 2025-07-04 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 276.0 |
| 4d098e42-7953-3a48-9250-2ebc89cf2e1a | -17.9386 | -50.6021 | 2025-07-04 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8a628506-a3ba-3037-870b-198b045232a1 | -11.932 | -45.389 | 2025-07-04 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| f8e1b741-a6aa-3f5d-8866-2bfe631e86b0 | -7.2219 | -43.0682 | 2025-07-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| bc1058de-6084-3f77-9bc8-6de579db6a0e | -11.9132 | -45.3688 | 2025-07-04 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 54d4256f-b8ba-31f7-b0fb-de5beca15a84 | -7.2214 | -43.1153 | 2025-07-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| e5f4b536-479d-336c-aeac-ab8dc7320ff4 | -11.9324 | -45.366 | 2025-07-04 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c2af3c39-f58b-391d-913c-9ae8065d4bcc | -6.6115 | -43.8709 | 2025-07-04 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 26e187b2-a694-3ca3-8053-7fd4e843f747 | -17.959 | -50.5764 | 2025-07-04 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 68a810d3-b97e-3f0e-b1e1-ce483e1d2470 | -7.2217 | -43.0917 | 2025-07-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 294.4 |
| cc8d4bb0-b3e5-37a5-bd6e-271801896c79 | -7.2405 | -43.0899 | 2025-07-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| c3f30d75-7530-34ce-8761-e6568affb4b8 | -11.9324 | -45.366 | 2025-07-04 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9c3f0816-2b10-32b0-9cc8-eb594b406a1c | -6.2945 | -43.6659 | 2025-07-04 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c85d5f2c-32ce-3637-a51b-7feb47399eca | -17.9391 | -50.5799 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 8516d0db-b5d6-3eae-81fb-806dad13a74c | -7.2214 | -43.1153 | 2025-07-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 666c66e2-1389-3088-a3b1-3aa807326fa2 | -17.9585 | -50.5985 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 502.8 |
| 5ff6d5b3-ae4c-323d-b324-4b734b3bb11c | -6.2757 | -43.6675 | 2025-07-04 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fe70a79c-d475-32bc-824f-4b94732722cd | -6.6112 | -43.8941 | 2025-07-04 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9fc72ae5-5b8f-3623-93e4-467ea60fd738 | -7.2217 | -43.0917 | 2025-07-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 355.8 |
| 7ecc1afd-cb61-3ff6-957a-38667d85b0a8 | -7.2405 | -43.0899 | 2025-07-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| beab051f-1b9d-3ac4-8ca9-db594d868a4e | -17.9784 | -50.595 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d9e3a8f0-37e3-36b0-b894-931c8e8b7870 | -11.9132 | -45.3688 | 2025-07-04 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 49745bd3-f3a9-3316-8c7e-4a927a784b4d | -17.9386 | -50.6021 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| b67b9581-5ad5-3652-ada7-e0145b888741 | -7.2219 | -43.0682 | 2025-07-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 778d0a2b-d61e-3798-b62f-c34dab7835eb | -11.9128 | -45.3919 | 2025-07-04 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 21d4f86b-b295-3072-8cdc-cc3d6a8ddac8 | -6.2755 | -43.6907 | 2025-07-04 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f79378fb-8290-311d-9cae-db0cc081a2a4 | -17.959 | -50.5764 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 38281a54-5067-3343-804f-374179f60f88 | -10.5586 | -49.1337 | 2025-07-04 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 14323eaf-1114-3fe4-8134-8eec3bb4efb5 | -11.932 | -45.389 | 2025-07-04 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 54e1010e-939c-307e-83eb-014a97181979 | -17.958 | -50.6207 | 2025-07-04 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3d6f5f5e-8d20-338e-9ac8-5efcbf89e710 | -6.6115 | -43.8709 | 2025-07-04 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 58fd8150-2784-30b7-8cb1-190b5cd80f50 | -18.4486 | -54.6674 | 2025-07-04 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d089c260-5048-3ca7-8316-48f35c380c8c | -17.9585 | -50.5985 | 2025-07-04 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 389.0 |
| 74eacced-a206-3fd4-b082-a8c6d51f673d | -10.5586 | -49.1337 | 2025-07-04 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0540416f-5ff2-3846-9d27-5e1bb1692dd5 | -11.932 | -45.389 | 2025-07-04 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 86f9a411-4dcd-3fd3-b041-bfd8a3a152de | -6.2757 | -43.6675 | 2025-07-04 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 3d1c3ec7-b7b9-3d5a-a8f6-df9c659c238a | -7.2217 | -43.0917 | 2025-07-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 324.8 |
| 2cb94a20-3462-3416-b0cc-9f7ba07b0da0 | -11.9324 | -45.366 | 2025-07-04 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3dbcd91e-15ba-3145-acab-b44579985e23 | -6.2755 | -43.6907 | 2025-07-04 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 9566ec4a-d012-34fc-a879-bc9a8948ac01 | -18.4486 | -54.6674 | 2025-07-04 00:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f5a6614e-eaf0-3608-947a-d93bd0fe29db | -17.959 | -50.5764 | 2025-07-04 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 1a016d16-b797-34a0-b001-644950e66506 | -7.2405 | -43.0899 | 2025-07-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 906ddffc-49d3-3942-a62a-5104d8a7ba0c | -11.9128 | -45.3919 | 2025-07-04 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 68172987-57f9-3379-bbdd-b934f7a98178 | -7.2219 | -43.0682 | 2025-07-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 80f38684-c7ff-306a-ba1c-64bcd01ce866 | -7.2214 | -43.1153 | 2025-07-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 05b68474-d60a-3d57-abc4-11c44b5ae522 | -6.6112 | -43.8941 | 2025-07-04 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2d90978a-0a47-30a0-a989-ab1cba647f1b | -6.9908 | -43.5349 | 2025-07-04 00:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 233bc800-94cd-3961-a37f-8236f5a95ad1 | -17.958 | -50.6207 | 2025-07-04 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| d0ea4607-14ed-3cc7-aec1-6490e7747e08 | -17.9386 | -50.6021 | 2025-07-04 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 894ff604-7406-3877-8552-97000bbd750e | -11.9324 | -45.366 | 2025-07-04 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 00b8f038-c2a3-38fd-831d-7df6f4f0c8b7 | -17.9386 | -50.6021 | 2025-07-04 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4c8ecb6b-811c-36c8-84dd-22b88b88915f | -7.2214 | -43.1153 | 2025-07-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 9139c786-5140-3515-b9df-4f3a93635f58 | -7.2217 | -43.0917 | 2025-07-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 259.6 |
| 2e52f4ac-d232-3641-95f7-00a22a46f91f | -18.4486 | -54.6674 | 2025-07-04 00:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1c4652eb-fe96-3d47-810b-feba8051ddb0 | -6.2755 | -43.6907 | 2025-07-04 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ed7e6a6c-4dc0-39b2-a1e5-e8d278ce414c | -7.2219 | -43.0682 | 2025-07-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 937cbd05-3be1-3256-808f-5516ecaaa145 | -10.5586 | -49.1337 | 2025-07-04 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5eef923b-edfb-3842-83a8-52af90e35ff6 | -11.932 | -45.389 | 2025-07-04 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| b1f3c686-16d7-318a-b206-d11af4b9e18d | -7.2405 | -43.0899 | 2025-07-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 50e84acb-ab44-3cd4-acd1-95db8f5fad63 | -11.9128 | -45.3919 | 2025-07-04 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9f06f33c-d12f-34cd-8a57-2d64b1c17e3f | -17.9585 | -50.5985 | 2025-07-04 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 62dd0a18-e37f-3675-b12d-8853f72f163f | -6.2757 | -43.6675 | 2025-07-04 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4e55e155-35c5-38f7-be68-f84cae828e32 | -6.6112 | -43.8941 | 2025-07-04 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a6aeb870-2cc9-3ee0-be14-ed152f0c5666 | -7.2217 | -43.0917 | 2025-07-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 300.1 |
| 34906f99-a3b6-3a98-840d-bb71038f8c65 | -7.2214 | -43.1153 | 2025-07-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 8a3e29d1-7d34-351b-adff-45382cc7ced9 | -11.9324 | -45.366 | 2025-07-04 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f7a7ff3f-1ed7-3ea3-8479-9459ae6b7dcc | -6.2755 | -43.6907 | 2025-07-04 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 683a5870-44db-3686-a9a0-ebe6078772cf | -18.4486 | -54.6674 | 2025-07-04 01:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5ef70a8b-ff88-3174-9870-91ee9640cd1f | -11.9128 | -45.3919 | 2025-07-04 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 79445e10-4dd3-3b61-963c-754d027a19be | -6.6115 | -43.8709 | 2025-07-04 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 93dd8e30-d91f-3d5d-9edc-6700858a7cfb | -11.932 | -45.389 | 2025-07-04 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 1eedfb7e-fae2-39b0-afad-558036eb9261 | -6.2757 | -43.6675 | 2025-07-04 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 6f4cf52b-f71c-3fc0-b41c-e7ed50888b8e | -10.5586 | -49.1337 | 2025-07-04 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0fe0993d-dcf9-3bff-84f1-ef5bd24a1ce9 | -17.9585 | -50.5985 | 2025-07-04 01:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7c4cf33c-c796-343b-afce-862b52c167c6 | -6.6112 | -43.8941 | 2025-07-04 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4424fbf7-edb8-32bd-abff-e277e128df80 | -7.2219 | -43.0682 | 2025-07-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 71138a0e-7d7b-3dd8-8ff7-f7e7ce9a4fa3 | -7.2405 | -43.0899 | 2025-07-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| d60d5414-8bca-34db-a35d-51769b56f297 | -12.424 | -43.7274 | 2025-07-04 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |


[Clique aqui para ver as próximas entradas](README3.md)
