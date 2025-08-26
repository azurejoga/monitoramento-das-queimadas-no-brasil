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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a091e27-6ac1-3daf-b65d-0044f895b030 | -14.24033 | -53.04927 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a87a782-86cf-3f10-a21c-a33287daa327 | -11.1513 | -44.75238 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f487e5b-c67a-309e-b953-f155b3f24043 | -15.11726 | -48.64963 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35067db8-7d46-3954-9536-9734c2cca53d | -11.54924 | -52.13286 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5b67fd2-83f8-38e8-8e0f-ee5304eacfc4 | -8.55972 | -62.63637 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb57cac4-c516-3efa-be05-c661917b5f54 | -14.71096 | -55.94707 | 2025-08-26 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1297ecb9-4d57-3858-b5a1-f69858b3140e | -8.59309 | -62.63581 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4eb3f35-d152-30da-95bc-e44e4e2d2760 | -13.39468 | -51.79276 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d4fe852-b939-3ca3-8cd2-ae43b98f344d | -12.75294 | -48.09311 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c2343fc-dbe1-3bcf-8383-7e2b3ffefe69 | -14.44217 | -56.46022 | 2025-08-26 04:46:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f32b05-e994-3a9b-964a-4ffe4d5f5643 | -7.61655 | -61.03868 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 313ab25c-2d84-3abe-ba2a-3deb14bac184 | -15.04446 | -48.51135 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019d0f00-31ce-3e28-88a2-1eedc588701a | -15.06436 | -48.5393 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f297d4-00ce-3150-b81b-723e2d213279 | -13.42477 | -47.02691 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7fee49-7dc8-3024-8a9d-5885c2b0267f | -11.64188 | -44.86907 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab236c64-04ef-3968-a9bb-683afa16edf4 | -7.53891 | -61.3811 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eabe9bf9-355f-3f8d-a846-84fcb0716d76 | -12.78306 | -48.13232 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8d650a76-319e-373b-becb-bdc793d3c2e9 | -9.18767 | -60.80705 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5145854b-b1a9-3ab1-b769-9e83f8f5c33f | -8.33025 | -50.57155 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bf6f12d-d02b-3cfb-b969-5b9cd5319040 | -8.8771 | -62.46881 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e30a1ae-7ac5-398c-87a3-7d96f73242dc | -9.62101 | -57.37485 | 2025-08-26 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 226b8b78-1bd8-3ffd-b9e6-0f1f2350254e | -13.44197 | -46.87008 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 753adae7-7e72-381f-8fd5-5965f7ce88de | -13.35372 | -54.39291 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b9e3d9-7d37-3d4c-94a6-485a1adfd3c6 | -12.75923 | -48.10488 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aafcc88-9fe2-3e92-b617-810d55bcfdc0 | -16.03612 | -48.08331 | 2025-08-26 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f05490ad-35d4-3fcd-acbe-31b165a34948 | -10.60175 | -54.89346 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16691328-a810-38e3-b69a-a8269a3c4607 | -10.88957 | -55.7796 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| befbcd9e-2dd7-391a-b419-ac55ac10f06e | -10.54366 | -46.78429 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47969033-8eb0-38e4-b721-2ad84908d8d7 | -10.762 | -47.06128 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e10fbc6b-ddcc-323a-8253-617d9c03d139 | -12.78169 | -48.14209 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07c00a48-646e-3bfc-a55a-7bd08cd627f5 | -15.0551 | -48.7014 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a3d5f97-26b8-341b-852a-dd11d3a27928 | -10.52345 | -57.97644 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 282f3c65-2121-3fbc-abf4-8129ccd25140 | -8.84596 | -62.4405 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e71b4444-5f86-3153-b104-a98608b1ef05 | -7.47153 | -61.3369 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7e570e-44ee-3ead-9076-7f137d0a45dd | -11.5382 | -52.11668 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2a80cfaf-e921-33ef-b7cb-b4c005d51e2c | -11.56083 | -52.12393 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a406d173-c85e-39bb-b75c-4d8d0ebecbe6 | -13.61486 | -48.15862 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fe73634-b6a2-368f-96c6-98497bc5ad78 | -15.1071 | -48.63752 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88050dbe-9e10-3ef9-a986-3d2eb41e7087 | -9.08514 | -65.72691 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09f9fd6-ae8a-35a7-8a8a-c03fea293149 | -9.92721 | -54.71845 | 2025-08-26 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db35c6e-5446-3ebe-ac4e-fad481f526bb | -12.75823 | -48.10343 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8190e7d7-6422-344c-bf73-0029ec8eec6c | -9.15137 | -59.55626 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3e48d80-35fd-3ed9-88bc-9f4830cd0082 | -10.42112 | -64.3828 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d9e19e6-53eb-3969-b3f0-6ee0b7d03702 | -8.11769 | -61.46623 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 247ecc52-3cac-3789-bab3-ff103d9d643d | -15.20428 | -53.79982 | 2025-08-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5deaf2a-8504-34fc-8c0b-fe64fbfd8591 | -11.62724 | -46.40892 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea85316-61a7-38f3-ae8f-77da4f8dcaa3 | -11.03452 | -49.14639 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8a11e78-2de9-3530-85d7-37e6978abfa8 | -11.63702 | -46.20753 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afac00e7-4b5a-329c-9534-429cde5d4c61 | -9.04696 | -65.73307 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49b17d6b-b1e4-3a02-8aa3-561072889911 | -15.03579 | -48.68637 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea16f96b-6fe8-3d58-b855-20a854f7de24 | -14.97346 | -52.87888 | 2025-08-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5dd6195-948d-3094-9adf-3eecbb9eb5e6 | -9.17279 | -59.5117 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31ac9b84-789a-3e6e-928a-1d64be088d11 | -11.54689 | -51.88763 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b077cbcf-79de-3d7e-be60-e7c2b7fd45f8 | -15.0887 | -48.56974 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669ab944-cd74-3594-9f38-235d3798014c | -9.16282 | -59.51953 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 371d34cd-2bc7-358b-87c1-d6b710e67ba7 | -8.8435 | -62.45332 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d3d95c93-ece6-33cf-bcf8-ff97cef589e5 | -10.64591 | -51.59272 | 2025-08-26 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e20e20-3d00-3c4f-8904-42bab7b8082b | -6.91061 | -59.36209 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fc55da2-ad49-32bb-aff6-d2cdacdc609a | -9.18721 | -59.54198 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e1c27a3-de69-3170-ba01-d9f4b3ed84f9 | -13.44073 | -47.00391 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 693abdd3-fcba-3200-b455-b2ab51a30b76 | -8.85216 | -62.45044 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2e609c8d-e21d-307f-9642-566ca189c75e | -8.57166 | -63.92628 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c7c1850-fae8-3e68-bf5d-38307106fa00 | -13.58511 | -48.19796 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 36308e33-50e2-3f68-91e1-86187c332b9d | -8.10249 | -62.88547 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| daf04fe4-42d4-30f7-a732-df061f8e2c20 | -13.60574 | -48.16718 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31348df0-3df2-3c30-8085-7d03ff639065 | -14.53041 | -53.10503 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c983e45f-c4a8-3ee3-87cd-098726b3b81e | -9.16376 | -59.51414 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8683f794-30a7-345a-b161-ae08658cfc55 | -13.64528 | -45.70378 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d19f97-2a28-3e3d-9576-15158a7f9c24 | -11.53268 | -52.13018 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 829de992-e3f8-39a2-9585-50ca72d09cae | -6.782 | -59.6789 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e0e5a2d-7c15-377a-93e6-27fbe236f3f7 | -9.30021 | -48.42439 | 2025-08-26 04:46:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d1e5e4e-f6d7-3b2b-9ef7-8db41115b4c6 | -14.71754 | -45.38005 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35ba7619-a7f1-3cda-9030-07999c66e4e1 | -8.54013 | -62.64184 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ad4db54-dc33-3c74-adf4-f25ddd24b6f0 | -6.81959 | -58.96817 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0317f418-2a39-3cfa-be08-e3d891463e18 | -11.26053 | -44.99403 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23f1b1af-c51c-3dfe-94f2-43f1a85faf4e | -11.30572 | -55.1063 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 41b056be-1e67-3293-8b56-96c02747807c | -8.99898 | -65.4082 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c8e8b9c9-81e8-34f6-8adb-c478372bcd0c | -13.65179 | -46.87887 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 501c8464-3339-3f8e-bbb6-9d95a0259952 | -8.86933 | -52.04873 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2389c31b-6dab-3595-9657-4d0954accb17 | -7.3565 | -59.66334 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a43d5a1-f15b-3c52-b570-0634231fbad7 | -9.16953 | -59.50966 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73f26d90-2a36-3771-b84a-2330a9e17822 | -8.86698 | -62.45795 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0386fff0-1bec-377f-bb33-9ecbf2aac505 | -11.158 | -44.76259 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 87d83d0b-d010-3719-9cb9-3d56d50e09a6 | -9.18011 | -59.50607 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e0df133-576d-3bda-a98e-dbfcf025582f | -11.62249 | -46.2178 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d34f1814-3af5-3491-b618-325ad5e2824c | -13.43968 | -47.01151 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4ccc6ea-177c-3c94-9e9f-cd52dd137a21 | -9.1539 | -59.45734 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a0ba4ac-da1a-36d5-b3f0-dc507c671908 | -8.90301 | -62.46058 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 966e00c5-c38b-3b6a-9b13-7c78d5574f42 | -11.55255 | -52.1118 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1800525e-bf1a-38c2-8e66-0477dbadf3ce | -13.60618 | -48.19327 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6be9facb-b162-350c-a84f-f9d54ef6f714 | -13.61163 | -48.15305 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 992776e5-a253-3d38-b87b-758c89d9b5fa | -12.75913 | -48.13422 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 339fc283-290d-3c8e-939b-70aedaac3c04 | -11.52496 | -52.13613 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 62ef2765-343e-3a4d-887d-9b27fd8c3b5c | -9.92367 | -54.71782 | 2025-08-26 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb5898a-07d6-3a53-9ef8-9ef5cf1eec37 | -8.85769 | -62.44281 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 31855f40-b6d5-3aa5-b435-bc0a9b120207 | -13.39079 | -51.79581 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28a895ba-9f42-3007-9666-a3a142c0aa96 | -9.16158 | -60.772 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f800c62-44a0-3e8a-b9fb-812340be9aad | -11.15659 | -44.77296 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 556adbb2-f148-3f93-93be-a060fe0557b3 | -9.16389 | -59.54181 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e89281c1-a908-3abd-8769-1bbb6a109c6d | -13.41084 | -46.87732 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README70.md)
