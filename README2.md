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
| 22997a5d-104a-347e-9e93-360a6e83d300 | -18.5472 | -56.8343 | 2026-07-21 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 92e1efc2-6094-3297-b343-a71e6df48b85 | -18.548 | -56.7927 | 2026-07-21 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 774b13bb-f39d-3e2b-83e0-9f0793dc407e | -18.5476 | -56.8135 | 2026-07-21 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 358.6 |
| 0c95d3bb-15f1-3ea3-a429-8ed81d02ba04 | -10.5048 | -50.3013 | 2026-07-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| db50d1f9-6120-37de-ab67-dd7fbdc594e9 | -8.7497 | -49.0782 | 2026-07-21 01:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b703427e-7b3a-3bcc-b17b-036ea8e6ba49 | -18.5675 | -56.8109 | 2026-07-21 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 78a83a0b-ad73-306d-91eb-ec3e5607e211 | -17.5947 | -47.4956 | 2026-07-21 01:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ad3367d7-4b8e-3d81-abf6-54a64d0361a3 | -8.7522 | -49.061699 | 2026-07-21 01:23:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9106638b-fab4-3c62-b004-66971bb2a9b8 | -10.8538 | -50.419498 | 2026-07-21 01:23:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74bfa4f1-6e58-316c-a45a-0b37fa693a83 | -17.586901 | -47.4837 | 2026-07-21 01:23:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44626662-62cd-370e-aea7-94fa31a42400 | -20.8745 | -57.492699 | 2026-07-21 01:23:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9536e2ce-107f-3db3-8026-2cbad768a48a | -18.5452 | -56.814301 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 90863d8a-8aff-3b01-9a78-70e85d805efd | -7.6865 | -55.360401 | 2026-07-21 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b56a997-bf49-3339-9a38-12310575c2c4 | -17.865499 | -50.5028 | 2026-07-21 01:23:00 | METOP-C | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5798e7-06ea-3ad6-b0e0-6fcc91b48735 | -10.8203 | -50.409599 | 2026-07-21 01:23:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 735ac942-1149-3a90-8cbc-0933e85c99d9 | -18.546801 | -56.821499 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44e81175-e530-3516-bbb7-491812408903 | -20.892401 | -57.480598 | 2026-07-21 01:23:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c57da2d-ac0d-3830-a3e7-a9af8f368727 | -18.555 | -56.811901 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3f66c4a-3144-351d-a2cd-e023f9595258 | -10.5137 | -50.3009 | 2026-07-21 01:23:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d19f9d3e-9710-316f-b690-0226c920c338 | -10.5188 | -50.2803 | 2026-07-21 01:23:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| beb64ef2-7c30-37c4-987b-b9073bc9f370 | -10.8106 | -50.412102 | 2026-07-21 01:23:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a68c8744-c34a-3ab6-aaee-2434d80e93fe | -8.7619 | -49.0592 | 2026-07-21 01:23:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49880342-0630-389b-b041-031095b1b79c | -9.4901 | -63.311001 | 2026-07-21 01:23:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29260ca0-b080-3109-9552-a0e70406c330 | -7.6887 | -55.369801 | 2026-07-21 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af6976a-d7c5-3f3d-a5ef-037f932fa752 | -11.5991 | -58.511299 | 2026-07-21 01:23:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f71cbc0-c748-3c1f-8cbe-81ff61af2124 | -10.5091 | -50.282902 | 2026-07-21 01:23:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1d5ead8-4a61-3fae-81db-f53e340f666d | -9.4978 | -63.2994 | 2026-07-21 01:23:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a703c623-04e1-384d-b7b8-d576de5d96de | -9.488 | -63.301498 | 2026-07-21 01:23:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42bb7e77-c06d-3ce3-a42b-b5e9d460e3f9 | -18.5436 | -56.807098 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 48b11cae-77f7-3035-88e4-7c9a6ec95673 | -10.5234 | -50.298302 | 2026-07-21 01:23:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dd3b32e-d9e4-353c-9966-b14c38c3e702 | -20.876101 | -57.500099 | 2026-07-21 01:23:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1e86485-85cc-366a-8cd5-749b5a378e1c | -9.4999 | -63.308899 | 2026-07-21 01:23:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87730c14-6ea9-3958-8a94-c7df70aa9648 | -8.7679 | -49.0825 | 2026-07-21 01:23:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa717c7e-aa1e-3e05-96e4-96789f894155 | -9.0935 | -50.592098 | 2026-07-21 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de4cfb1f-7249-312d-a12c-1adef9909bcb | -12.142 | -48.248901 | 2026-07-21 01:23:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db1638b6-d1a9-3359-92c5-ad69977a3120 | -12.9891 | -62.1469 | 2026-07-21 01:23:00 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bedb5965-f870-35f5-b6df-6eb1f18e62ea | -8.7582 | -49.084999 | 2026-07-21 01:23:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1c4c83-a527-3823-9721-1371ee056e1a | -11.6285 | -58.2775 | 2026-07-21 01:23:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 517cd12c-ee95-3829-b03a-3b621aa9a4d3 | -19.1931 | -47.350201 | 2026-07-21 01:23:00 | METOP-C | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddcd138-0139-30e3-9216-0f593193e4d5 | -9.1016 | -59.406898 | 2026-07-21 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6a3619-236c-3d50-8c15-130895ae972d | -10.7436 | -50.3923 | 2026-07-21 01:23:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 633cd134-d581-3444-b142-88058c2d46cb | -11.5975 | -58.504398 | 2026-07-21 01:23:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55f635b3-3de1-38e8-ab63-69d5c4aae0c1 | -18.5534 | -56.804699 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e182f2f7-8e2a-3b4c-8e5c-547aa94e75cd | -18.556601 | -56.819099 | 2026-07-21 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51a74c01-c323-378c-a1f9-a8212410d058 | -9.1 | -59.400002 | 2026-07-21 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e68c98f4-b248-336b-a684-37f916094786 | -13.3221 | -45.1246 | 2026-07-21 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d6ba7e3e-447f-3a6f-bf76-6abb2d5042fa | -18.5472 | -56.8343 | 2026-07-21 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.2 |
| 9eafe9a6-2fa4-3166-855c-1794bc1fa173 | -18.548 | -56.7927 | 2026-07-21 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| d09832b2-41a0-3488-a7f8-a4d8c3877219 | -13.3023 | -45.1511 | 2026-07-21 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 047ccc72-f9d9-3000-af37-0ce3369f6be2 | -18.5476 | -56.8135 | 2026-07-21 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 403.1 |
| f1cedf24-c1ac-3ced-9879-545c5b39c684 | -8.7497 | -49.0782 | 2026-07-21 01:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8475e19c-d4a9-30ba-a805-ba2abf9db4b8 | -13.3028 | -45.1278 | 2026-07-21 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4005dce3-4559-3359-a20c-01f6abc0b222 | -18.5675 | -56.8109 | 2026-07-21 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.1 |
| 00eb0fbe-d50a-3d0e-8c5c-bac2cdb4d5a3 | -13.3217 | -45.1479 | 2026-07-21 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1d34e841-6e09-3114-9193-4c41d6281ccf | -18.5476 | -56.8135 | 2026-07-21 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 372.9 |
| dfa722b2-2967-3fe8-a9fe-a1ef6036843a | -18.5472 | -56.8343 | 2026-07-21 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.6 |
| 9047208f-0ecf-314c-8807-c5086784308b | -8.7685 | -49.0765 | 2026-07-21 01:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e0533353-4a2f-3d3b-bd24-0720e2150c81 | -13.3217 | -45.1479 | 2026-07-21 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7841f295-7958-361a-80ff-66e24155263b | -13.3023 | -45.1511 | 2026-07-21 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 56eec517-6ea8-3cba-8435-176aa49ec6bc | -18.548 | -56.7927 | 2026-07-21 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 35889f34-0338-3bff-a39b-03dfd00285fa | -19.6142 | -47.6443 | 2026-07-21 01:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b2da11cb-3ffb-3738-86c3-07214507b3e9 | -19.6148 | -47.621 | 2026-07-21 01:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 991c0a6b-065a-3b9f-9196-5356747ac0e7 | -18.5675 | -56.8109 | 2026-07-21 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| cbff326b-0b5f-3870-ad48-21f312dc49a3 | -13.3028 | -45.1278 | 2026-07-21 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| e2b3680a-343d-3c4b-814e-280818b95c24 | -8.7497 | -49.0782 | 2026-07-21 01:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9e578c39-93e1-3dea-8ec9-5c0fe442308c | -13.3221 | -45.1246 | 2026-07-21 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| ade7b11b-0173-3527-b8b6-2e3f4e23c5ee | -18.5671 | -56.8317 | 2026-07-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 73df3382-8128-3610-a922-98dfc728e265 | -13.3221 | -45.1246 | 2026-07-21 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 759791f2-c710-3985-ae45-d2747402d0af | -18.5675 | -56.8109 | 2026-07-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 205.0 |
| 191ac064-42d2-3ef0-87eb-ed5e9ef38e39 | -18.548 | -56.7927 | 2026-07-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 8fd88289-9b41-32c9-b739-d30f5704f94a | -18.5476 | -56.8135 | 2026-07-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 387.6 |
| d975d204-bd3f-38fa-9896-3987b929a626 | -8.7497 | -49.0782 | 2026-07-21 01:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4cfbd9bf-2996-3b58-b839-4eb4eb98468c | -13.3217 | -45.1479 | 2026-07-21 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 572831e5-90d7-3fae-94c8-e41a90c6c631 | -18.5472 | -56.8343 | 2026-07-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.7 |
| 2cf84a6f-e39a-3cc3-843b-063778f08e63 | -19.6142 | -47.6443 | 2026-07-21 01:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| a371013a-90ee-3833-ae60-9679141637e0 | -13.3028 | -45.1278 | 2026-07-21 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 9569cebe-1a28-3142-8870-1653005adebb | -13.3023 | -45.1511 | 2026-07-21 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 375e8044-fa92-3825-92dd-bd65fd8f93ba | -18.5472 | -56.8343 | 2026-07-21 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.8 |
| 111fabcf-0e73-34ba-81f9-c1db4e8b8688 | -18.5277 | -56.8161 | 2026-07-21 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| a8d2fed7-6eea-325e-a09d-65cd439c493d | -18.5675 | -56.8109 | 2026-07-21 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 244.8 |
| 289cee7a-92c5-3ced-8f4e-7d3eb3b69d94 | -18.5671 | -56.8317 | 2026-07-21 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 668959c5-5492-3d6c-9df1-b52bf8b76cdf | -13.3221 | -45.1246 | 2026-07-21 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 140e0746-16e9-370f-9d03-c629af4f4fbc | -13.3028 | -45.1278 | 2026-07-21 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 68c26994-3d1c-3452-8857-26d5abd59944 | -18.5476 | -56.8135 | 2026-07-21 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 411.7 |
| 353e113b-430d-3075-9902-c6cdd1e26847 | -13.3217 | -45.1479 | 2026-07-21 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 3d1980a7-5b23-3ecc-8275-d426ff6a7292 | -8.7497 | -49.0782 | 2026-07-21 02:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9c073d78-54dd-369e-b73c-8012004b9588 | -13.3023 | -45.1511 | 2026-07-21 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 71e7b59e-38f6-3f3c-ac43-127fb646112b | -13.3221 | -45.1246 | 2026-07-21 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 279.6 |
| da90d797-86ba-3b03-b19d-86c4dc289d68 | -18.5675 | -56.8109 | 2026-07-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.0 |
| e7e96988-7002-324c-b10d-774046c3d30c | -18.5476 | -56.8135 | 2026-07-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 425.7 |
| fe7848e6-39c1-3c7e-9eaf-c6aeda9bf883 | -8.7497 | -49.0782 | 2026-07-21 02:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| bf558a3d-3766-3e81-bb22-cb109724bf6e | -13.3028 | -45.1278 | 2026-07-21 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 244.1 |
| fa365bc5-6681-3b9a-acfd-8d50fb958d26 | -13.3023 | -45.1511 | 2026-07-21 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 9cc9e902-026e-32a7-8b00-e6bf6e5c156c | -18.548 | -56.7927 | 2026-07-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 88889038-03fd-32cf-8f5b-42553c39bda8 | -18.5472 | -56.8343 | 2026-07-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 221.9 |
| 3561dc07-6c0e-3176-9bdf-759d34311ef2 | -13.3217 | -45.1479 | 2026-07-21 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 7af52b9c-7a41-3df3-bd75-9c1b8455a353 | -18.5671 | -56.8317 | 2026-07-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 9ea8d416-e137-332b-bf86-4494ae2d9631 | -13.33 | -45.15 | 2026-07-21 02:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5756859-d57e-3fd6-bd27-57265bbda646 | -13.3 | -45.14 | 2026-07-21 02:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5db8da2d-4911-35d3-8dca-28cc79f79a86 | -18.5675 | -56.8109 | 2026-07-21 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.6 |


[Clique aqui para ver as próximas entradas](README3.md)
