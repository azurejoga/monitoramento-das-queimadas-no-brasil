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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a160d91-3c2a-32af-b4f3-7931bdf1dd65 | -9.61123 | -49.68133 | 2024-10-24 04:57:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7178a358-b90f-3db5-a5cc-bca12d10cbba | -9.61072 | -49.68488 | 2024-10-24 04:57:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23ee7c93-cb6c-33a9-b3fb-c3161cc94cc2 | -9.57048 | -49.64582 | 2024-10-24 04:57:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4283e1f-ba59-34d7-8b62-faab78a45f30 | -10.89044 | -49.2709 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97feea65-9b27-3f41-9346-92b90ff157c5 | -10.88901 | -49.2691 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51ff7820-74f5-3d82-afee-375245ed7306 | -10.87391 | -49.53967 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b828231a-4b18-311f-8a22-9c02db8dc6eb | -10.87026 | -49.53514 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67e1ce70-51f3-38c6-b450-fd7058f55c13 | -10.86973 | -49.53902 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 058bb3ea-2f24-3a68-8732-2ee0574e083f | -10.45572 | -49.36493 | 2024-10-24 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3442cb77-6dce-3a38-be1b-fbb363d2063c | -12.16782 | -49.68033 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3fede1f-36b2-32bf-89c0-4d7b7b980499 | -12.1636 | -49.67973 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c1e6067-3ced-3405-8006-b3c7893485b5 | -11.73158 | -49.85811 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b0fc715-b5d6-37a2-9321-a27e2a700ca6 | -11.73105 | -49.8619 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558e8f64-1ddf-3be0-85ae-092ccdad37b6 | -11.72953 | -49.84233 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ded9a30-e034-3675-8cd3-a06d4e0120af | -11.729 | -49.84614 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e142feaf-66a4-3537-9a52-2daa70686267 | -11.72538 | -49.84174 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3360f451-dee4-3725-9955-772725145363 | -11.59385 | -49.89626 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e17d393-cab4-3ada-874d-80dc24a33d6f | -11.57332 | -49.35396 | 2024-10-24 04:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baecf1e7-b586-3dc9-b08c-b1a8888e0dc1 | -11.49794 | -49.87188 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac52ab5f-f4d2-31e6-938f-28b8a9201411 | -11.49742 | -49.87564 | 2024-10-24 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d75c3260-a6de-339e-a171-d14084089c93 | -11.25249 | -49.94103 | 2024-10-24 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f889db7f-379a-339d-8a9f-566c87b1a534 | -11.25199 | -49.94471 | 2024-10-24 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e00f116-64ae-3bd4-8070-1bb14c33642f | -11.25148 | -49.94839 | 2024-10-24 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24fc5831-478b-3cea-ba24-14700c2cb3d1 | -10.98557 | -49.2008 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de708427-ad63-3550-9c81-bdd4a7bd6c52 | -10.9752 | -49.30588 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13aac9ea-de78-3aa4-a52a-49b7aee0c706 | -10.97151 | -49.30121 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b409a3d-21f8-3936-b841-8ce538ecdbb8 | -10.97095 | -49.30521 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50e27da7-7e67-3487-9808-f9a034a1dd8c | -10.96271 | -49.42527 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b47fb22e-3244-329b-8be8-80a958f69c48 | -13.54809 | -49.88615 | 2024-10-24 04:57:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35fe3cae-dae9-394e-9a18-b5c8d1d0ed39 | -12.90735 | -50.199 | 2024-10-24 04:57:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef641894-024b-3d83-b544-02d99b172a8f | -14.26884 | -51.1292 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef8c9001-d816-3aa8-8bb5-83eeee4282a9 | -14.26812 | -51.13435 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b2faba6-c318-3294-ba38-9660fc0b7279 | -14.26489 | -51.12854 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 69ce0ef0-3fc3-34bd-9159-6d4654a441e0 | -14.26418 | -51.13369 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ec898a5-d5f1-3e3c-b2f8-1e836739e0aa | -14.26166 | -51.12274 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7837c49d-0637-3501-b5c1-23a989b71b02 | -14.26094 | -51.1279 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 73a85b11-3ef4-3f64-99e6-27ab2f035229 | -14.26022 | -51.13305 | 2024-10-24 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2639915-90f6-353b-8a20-d4d43567cb47 | -7.56925 | -50.70852 | 2024-10-24 04:57:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd515c4b-a223-3630-8a86-fb1bdbb537f5 | -7.56741 | -50.71033 | 2024-10-24 04:57:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89be60a7-f6f4-3b8d-8ccf-4a75a6d2ca02 | -7.56674 | -50.71476 | 2024-10-24 04:57:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73039f0f-558a-33ac-b6e1-163c8f289aad | -7.56489 | -50.71235 | 2024-10-24 04:57:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f9478a4-13c9-30d7-bf66-85428516f396 | -8.06287 | -51.00299 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 522b4af2-fbf9-3597-895e-da6575338a01 | -8.06286 | -50.99208 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43d2a8e8-6af5-38c5-a6f0-13a6c026e59f | -8.06223 | -50.9964 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dd41743-a5bb-3026-b1fd-132f98ea37e3 | -8.0616 | -51.00071 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f88a6962-7dc8-3571-9a40-b7a81a3d6cf2 | -8.0605 | -50.99384 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 422c06f9-f4cb-37bc-ba94-114534afa957 | -8.05984 | -50.99814 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 924e74be-df6e-3606-b587-1742ef24c54c | -9.29465 | -50.77683 | 2024-10-24 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3058c111-a856-3df4-8113-41d9938bc037 | -9.18322 | -50.54405 | 2024-10-24 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 381d95b3-e339-3a84-8f57-f5dc07a3348a | -9.17938 | -50.54348 | 2024-10-24 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73de536c-8d11-360b-be47-8469b5be377f | -8.3268 | -50.89457 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1320ae41-687c-3bcf-ab4b-bb89325e1fbc | -7.99166 | -50.68956 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370ffe07-0425-3771-a816-31a056fa5566 | -7.9911 | -50.68713 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a790a9fb-c10b-30be-a636-a562a1cb204e | -7.99101 | -50.69405 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66cce085-ecff-30af-ada3-306f42b698ca | -7.99042 | -50.69161 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65b54b01-113d-3a99-8f85-6eca1ba3ffe8 | -7.98974 | -50.69609 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d06b35b7-3ffb-3f12-bf3d-9e0b3798311b | -7.98735 | -50.68657 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1101ceea-87ad-3a7f-a50b-bd6dfecfdfa7 | -7.98667 | -50.69106 | 2024-10-24 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158f01cd-a857-36f4-9a98-698156685468 | -9.99579 | -51.45753 | 2024-10-24 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 578796eb-434a-357e-80e8-dc63f2dce513 | -9.85944 | -51.18622 | 2024-10-24 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e84b40fe-23c3-3810-a58b-269dc65001d4 | -9.37824 | -51.88504 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab35a70d-61f6-3043-8e36-ebdc5e55ff54 | -9.37468 | -51.88445 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c00d4dff-0ad3-38a6-8cb4-bf754aa26820 | -9.3711 | -51.88388 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dcf18d4-b038-3631-b21f-5dee554d0f1e | -9.37049 | -51.88805 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa852546-ee8f-3bf1-8cf7-2d87e9127e2a | -10.51487 | -51.84701 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3b52ef5-2241-3dc3-aeaa-79ae28abf592 | -10.51424 | -51.8512 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77732038-5ae8-330d-a3ed-44811f8735da | -10.47621 | -51.9574 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c71b8ba6-3636-3b5a-b7fb-5239d2d7edba | -10.36816 | -51.39333 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ea4625f-b9ef-3e83-b789-a2ba894d6190 | -10.34184 | -52.00996 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1819d03-196e-3530-a058-89d7a0a10638 | -10.33825 | -52.00942 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fb541d-4587-3e8f-b2d0-7d2a72457913 | -10.33764 | -52.01356 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bc64b90-3f1e-379b-9344-121a5313ca36 | -10.30789 | -51.89012 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da83e7c0-911d-3958-a2b4-ee9d389ef647 | -10.30367 | -51.89377 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc03ce2-a8ca-3547-a814-d5e0f6f86e5f | -10.15971 | -51.55396 | 2024-10-24 04:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ee75f02-d18e-36b0-8670-0f5803cac20e | -10.09815 | -51.13017 | 2024-10-24 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ddcb602-4080-391f-8f41-fb987e744e41 | -10.0944 | -51.1296 | 2024-10-24 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8d7bfba-21b9-3a14-a731-c0365a2756c2 | -12.35948 | -51.22548 | 2024-10-24 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 400d2ea5-e993-30fb-b1e7-146ff481e71a | -11.44359 | -51.48601 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd65f329-0a11-30bf-bd1f-aa56c53e66c0 | -11.44275 | -51.48773 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc8ffd7f-2fbc-35db-9aae-dceaca48adf9 | -11.09917 | -51.55585 | 2024-10-24 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5a3002d-e878-3c4b-a21f-4db379f5562f | -11.09772 | -51.55314 | 2024-10-24 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1be55aef-38c1-3821-b955-d588a12766a6 | -11.09402 | -51.55258 | 2024-10-24 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff7acbe6-0d1e-3a39-9dc9-215a9146f6d2 | -12.46811 | -51.33214 | 2024-10-24 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 656a7264-e205-3587-b93f-84d617329604 | -12.46429 | -51.33158 | 2024-10-24 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fdd463e-2492-3e38-b808-6655358e0f89 | -12.46362 | -51.33635 | 2024-10-24 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6605a036-36a2-364e-8059-aa34898ee86b | -9.32727 | -52.848 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f75b5a8-aa6c-396d-8a40-59e3ff325958 | -9.96537 | -52.24422 | 2024-10-24 04:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8320609f-1e4f-3bfc-8f97-14343314bb23 | -10.26998 | -52.17507 | 2024-10-24 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7825d4e2-1146-3299-9ba7-edcacab31e84 | -10.26642 | -52.17452 | 2024-10-24 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4ad9f8-ac05-37ba-83c9-d0de88da1358 | -10.26286 | -52.17398 | 2024-10-24 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0bec2c1-86d1-38fa-ba90-7d25c350eee8 | -10.99254 | -52.88247 | 2024-10-24 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d1ae29-43e9-33cc-8c18-9fdb1d21a784 | -10.99195 | -52.88634 | 2024-10-24 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 757e5472-5d59-364c-984d-da38c78d34f3 | -13.75795 | -54.06474 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5009e57d-3688-3bc9-9607-3ad330b1d7cb | -13.75553 | -54.05744 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9158ad5e-f35f-3ddf-98fa-255677d7c7c5 | -13.7551 | -54.06044 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c99c7f2f-aa82-3e39-b837-0a7cc0576d41 | -13.75496 | -54.06121 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d3ec014-72d2-3e33-a54a-02ab83b94f51 | -13.75212 | -54.05691 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d8d63f2-4e5f-3d7a-a306-8cd31c72d1a7 | -13.7487 | -54.05638 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff29c02-4851-3de9-a6d5-2cbfd730c60c | -13.74813 | -54.06013 | 2024-10-24 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da9dc50-f017-3095-97c4-e817cbb7e776 | -9.60515 | -55.05085 | 2024-10-24 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README79.md)
