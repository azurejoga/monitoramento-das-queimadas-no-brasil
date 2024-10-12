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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ffb0b75-27a3-3fb5-a0ba-40e14807e82b | -4.99898 | -49.75498 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7241fa33-a0be-3eec-8669-3ff0c5ffbc68 | -4.51973 | -50.42509 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b8e82d3-b715-3c53-86e5-fd1badaa420b | -4.51421 | -50.42427 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2fc6699-f649-371b-b6a5-768bb36918e6 | -4.16986 | -49.77312 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b532d1cb-fdab-3507-a52c-8e79d4335a41 | -4.16927 | -49.77304 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41297f0c-e164-3a65-898e-43d67ba6874c | -4.16412 | -49.77228 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d50ada4-a430-36bd-9be0-702b919a4225 | -4.16353 | -49.77221 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23eef7fd-2d83-34ff-a060-b0032313db37 | -3.69445 | -50.1194 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 18d2655b-d18a-32d5-ac12-506b69408507 | -3.57874 | -50.56581 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 280ef899-90a2-3783-992e-b34ae7380484 | -3.57823 | -50.56923 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56ef002a-bcae-3f81-9d3a-bc2235fac049 | -3.57333 | -50.56509 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03b99800-38fb-3a85-8215-f28ac08f7b03 | -3.57282 | -50.56853 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d338791-8cec-3290-99ea-87fd89143cae | -4.83061 | -50.79921 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c04b0f8-8f77-34f3-97f0-b93a20c5dbd6 | -4.38084 | -50.8053 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b26f111-f20e-3f13-b604-d79c8ed0e001 | -4.38034 | -50.8087 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 574095d6-1e32-3bec-a327-0549cd7fa620 | -4.37547 | -50.80447 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8874e48f-a338-3f92-91f5-83986c216dc6 | -4.37498 | -50.80784 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1def9e4e-9ba8-3dda-85aa-fb2f6c6cd2c0 | -5.20716 | -50.16336 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0698bc6b-acd6-31e4-8beb-aa8e7edc2fe9 | -5.20662 | -50.16715 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b62ab2a5-38e0-3e3b-b9b9-eadb787d1660 | -5.20147 | -50.16261 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb696416-6e00-35b0-a2c8-dfefd0ff52ff | -6.13415 | -51.14128 | 2024-10-12 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98d81679-b5ac-31f4-9924-a5a2802899cc | -3.56426 | -51.51327 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8c63357-8cfa-36e2-86d4-54118db9f1fc | -3.56382 | -51.51617 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb4afe0a-46a0-39c6-9627-c5fc27e6f505 | -3.46726 | -51.55124 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31f632b8-784f-329c-910a-b39294033a80 | -3.46637 | -51.55704 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea41cab9-a967-3e58-97c8-14fe738be453 | -3.46574 | -51.55184 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7db4c1f7-8ff0-352f-a681-ee791bc8092a | -3.46532 | -51.55476 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 29992895-5d16-393b-8bd7-d87fc6f17e67 | -3.46135 | -51.55624 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 81980a15-a90e-33cf-b41e-12982a775a93 | -3.46029 | -51.55396 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d4a62d34-4782-3693-8f32-4537136ecd98 | -4.27824 | -50.95987 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89378de9-f169-327a-b310-7652fda5eba0 | -4.27775 | -50.96318 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5268f2af-6eaa-3ba4-b855-e3c1d7946231 | -4.27344 | -50.95566 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cb7744c-afd2-36b2-864f-2c7162a7fc57 | -4.27295 | -50.95897 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5ae009e-7063-310a-9c1c-efe2e23a96d3 | -4.27246 | -50.96228 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f046a8a-3d89-3df1-8758-c19a02a173c9 | -4.26813 | -50.95486 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 859156f6-a4a4-3139-9892-2a6a4ef61096 | -4.26764 | -50.95818 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83699700-ed6d-3bf7-b3cd-0811d9766904 | -4.26716 | -50.9615 | 2024-10-12 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec3ace6a-3922-3680-9bf7-db443c4b996d | -4.08752 | -51.02314 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4024b469-e726-3cc9-856e-1b001283514b | -4.0866 | -51.02926 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ae5267a-5855-3e3f-909f-ad96fe2995a5 | -4.08614 | -51.02913 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34ca937c-fab2-3d33-aa83-85c840b87581 | -4.02884 | -51.20028 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bd2a811-9fc5-3722-99fa-46fb2e7f7912 | -4.0262 | -51.00092 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ae48fdd-f23c-3e06-bde8-3eba8e627d14 | -4.02575 | -51.00402 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9f3bdf0-c996-35d6-80a1-42440e0c9a79 | -4.0241 | -51.19641 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64d68f62-1e57-3b4b-81a1-06d3e42360e4 | -4.02363 | -51.19958 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e896276-c8d0-3c42-bb0a-0576593ec784 | -4.02096 | -50.99995 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b521f0d-2415-3d6b-8551-a67d5cf8047b | -4.02054 | -51.0028 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d41c151c-dd29-3e71-88d5-6bb2da9f730c | -3.92393 | -51.22445 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d83dfc8-cd9a-30fb-ac98-505a9211ed55 | -3.92346 | -51.22758 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 617c996d-59d7-335e-b426-2a6d2c3c846d | -3.923 | -51.23069 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 764f0707-db5a-3ce3-83b3-d718e9c3d8ac | -3.91829 | -51.22677 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cec9fb6-5073-39c8-980f-e3f560145ccf | -3.91782 | -51.22989 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01f72287-8460-3593-98e3-d5107d151aa9 | -3.82873 | -51.40618 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 910aef9b-8979-3062-87ca-471090f3deef | -3.82405 | -51.40247 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2a37e84-2157-33c2-b61c-e5d33a3c6de0 | -3.82362 | -51.40545 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b7f7d2-8fcc-393a-b44f-abf4240a0b90 | -3.81648 | -52.25655 | 2024-10-12 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed048728-4776-360b-9b9d-9282e3380057 | -3.79303 | -51.31136 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c669f161-3950-3abd-8583-e7bf9fa6e13e | -3.79257 | -51.31448 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebd92f29-d9b7-3070-ba78-4547cc3e1504 | -3.78926 | -51.30138 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44e0f636-a239-3851-8066-2b7907a104b4 | -3.78881 | -51.30441 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29611725-6fc8-3a1b-ba47-4ec74da24b29 | -3.78835 | -51.30754 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba33afad-ab37-31c2-b1ce-9dc235419810 | -3.78787 | -51.3107 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 886e74f4-99a2-3c85-b6a4-d6217ab037dd | -3.78741 | -51.31381 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae3d198-948c-36cd-8ef3-d6b01dbbc6b3 | -3.78696 | -51.31684 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 129b7335-6c52-376e-82ed-e3a119e1ee94 | -3.78651 | -51.31985 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d153f585-9951-3bf5-ad87-50402bdbb96c | -3.78607 | -51.32283 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 655b5382-9480-33ef-9d9e-d3a85f6f872b | -3.78562 | -51.32581 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d7624b91-e5f7-33f1-ae3b-0ac87d34272b | -3.7841 | -51.30072 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dea3b241-fdd1-3e60-b9f7-1dff528437d7 | -3.78366 | -51.30372 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 968f848f-3499-3798-ae81-7fae9c1fab71 | -3.78318 | -51.3069 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3766b5b4-7452-32eb-b76a-8198f0172de0 | -3.7827 | -51.31014 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30cd471c-d5f0-3486-80a8-6259501323b1 | -3.78223 | -51.31329 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2f38835-c1b4-3a97-8dc1-4daac3668535 | -3.7818 | -51.31623 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 95969115-4f2e-3948-b62c-bb801e443077 | -3.78136 | -51.31916 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 845f70ce-d240-30fe-b333-a79248e2a508 | -3.78092 | -51.32209 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2e9c5349-5b37-3108-886d-dc5ce19f78f2 | -3.78048 | -51.32505 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| bf164fab-f519-3379-8a7a-9399d8a83fc6 | -3.7785 | -51.30303 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64cc2575-a0ff-3ed0-9170-31c2c843d911 | -3.77804 | -51.30615 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fc37aa6-015d-390c-b068-9f7551ae071f | -3.77756 | -51.30935 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81c33e11-5af2-3fcc-8c5d-2f50ef31900f | -3.77665 | -51.31547 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb7619b-22b6-3b65-b5f5-36e97883158b | -3.77621 | -51.31847 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f118f64-0545-3952-926c-4358689a01ff | -3.77576 | -51.32148 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f475d557-e974-32cb-aadc-e311867fec9d | -3.68508 | -51.07068 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcd76c43-ab19-38c7-a2ae-5ca3dedaf1c1 | -3.68462 | -51.07382 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d481623-3b68-3cba-b35e-c543fc3ee3fd | -3.67988 | -51.06981 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78f28ea0-6817-35e7-8e2c-fcb9c317276f | -3.67941 | -51.07299 | 2024-10-12 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e2aee78-4234-3d25-be27-86e1d83dc9f3 | -3.64703 | -52.11976 | 2024-10-12 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f3ba5a5-d7c9-32b0-8770-672f8b8dbf8e | -8.85375 | -53.01278 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af82e378-ae14-34d5-b2f2-92d16a6a1c5d | -13.2866 | -53.75586 | 2024-10-12 05:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c194d7f-513c-3215-a99e-865a7b946ca9 | -13.28159 | -53.75534 | 2024-10-12 05:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 326f9f9a-8cd2-3a81-9f76-96519f950f1a | -13.27658 | -53.75478 | 2024-10-12 05:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d61a13-5dff-39b5-b645-4d0933c9c4a1 | -14.80559 | -54.62059 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9105b368-1a7d-3963-97e9-9f80619fcd25 | -14.80424 | -54.62217 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be8fecfa-e9b8-3852-9ab6-b2d35f672523 | -14.8008 | -54.61982 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39455e8e-3124-3408-8104-ef358d8a2578 | -14.79945 | -54.62138 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef13fd0d-4e86-366a-bb88-62f34ed00769 | -14.79526 | -54.58639 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c5a24b3-fc77-34dd-89ac-7e126bb3d4b2 | -14.79429 | -54.58266 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 360eba33-cb1d-347c-91cd-de2a312c6a88 | -14.79367 | -54.5878 | 2024-10-12 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 505e1573-aac0-340c-bdc1-0ccb0b8ba74a | -14.45142 | -53.64244 | 2024-10-12 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41c86777-8fc1-329d-ac60-4193ab7c36a0 | -3.48494 | -52.82751 | 2024-10-12 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README101.md)
