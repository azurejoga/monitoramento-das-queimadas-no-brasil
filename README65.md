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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62996c7c-2fb7-3d47-aeb2-3cb44b6d6b0e | -5.19445 | -48.22577 | 2024-10-10 04:17:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddfaf541-f48c-3232-a050-cb5b619cdaee | -5.74854 | -49.24984 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0372eeaa-be65-3db2-a2a5-85f0d34a6fec | -5.66605 | -48.97128 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9c69a6-4ae5-3c50-a456-b23c19416aeb | -5.66211 | -48.97065 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88fcccb-b4fe-380c-ac8f-ac74343c3f32 | -5.59621 | -49.03558 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb9edb97-422c-31b6-90b0-f2aafee7be8d | -5.45688 | -48.92782 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ed6e009-ee24-3222-834b-f81500d02a83 | -5.45294 | -48.92716 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e2f07462-02b9-315a-be5e-d63a918f5753 | -3.65806 | -49.51041 | 2024-10-10 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4e1674c-7bd2-3ee8-8cbf-aaba1aefcc95 | -2.48143 | -49.28905 | 2024-10-10 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89cc3cc5-58cc-360e-a4ee-9ac5dc2f3c82 | -2.47534 | -50.24206 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f965b66-5238-3d89-b5ba-9d97e41eea2a | -2.47462 | -50.24654 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aec1bbb1-cad8-3c7d-8411-e8d80b0dc4d1 | -2.4739 | -50.25103 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ae322e3-58ca-3118-8824-d3f7de5cd6b4 | -2.47083 | -50.24133 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb2c38ae-199b-3fe9-8414-5995ba7a11cb | -2.47011 | -50.24583 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f2afe6c-10d0-3143-9238-a898acb30e50 | -2.4348 | -49.60303 | 2024-10-10 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f65bb5-37d8-36db-943b-802fea8df478 | -2.43049 | -49.60233 | 2024-10-10 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f13eb70e-45d0-35b9-b73a-745be12a5118 | -2.42239 | -49.09212 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f387462b-80d8-3617-bed8-e989e3c1ee7a | -2.39798 | -48.9542 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afc0a53e-036a-3375-a0f7-282938c05109 | -2.35564 | -48.99683 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a597dad9-13ac-307a-98e3-cd678462755d | -2.35149 | -48.99617 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6c45266-fa09-32d3-964d-d42018e1649c | -2.31036 | -49.67669 | 2024-10-10 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96996861-d3b3-3f44-8ef8-0ab2cddd66a2 | -3.53757 | -49.18354 | 2024-10-10 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecff3321-c6d6-311b-be5c-ccc994a9e25a | -3.53594 | -49.18277 | 2024-10-10 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfa74ef4-5fdd-370b-9df6-ad8832fa3e51 | -3.50993 | -50.39088 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f70d93b-7fbe-3f1f-885c-963eb6ed1c64 | -3.50194 | -50.27266 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a49a1dc9-504c-34cc-98b4-bd157282d70c | -3.40759 | -50.33125 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58ae25b2-3f51-3495-97c1-52a948901cec | -3.40313 | -50.33051 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32bc98c2-79a0-32d4-bdb1-89cd7374fe5b | -3.37493 | -49.49828 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad98825-0c36-32e6-a5a9-53f55456395f | -3.34132 | -50.13117 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd3fd721-706e-3147-b92d-c8a2dc7efcc3 | -3.3383 | -50.12189 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5711639f-f52d-3da3-a7dd-47254f962d63 | -3.33761 | -50.12613 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f787bede-3b4a-3735-9388-194b821e39c2 | -3.3339 | -50.12116 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc991a31-8d9f-3fda-8417-95bbd9b7a74e | -3.3284 | -50.0721 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f3caa05-bf4c-38a5-bbc1-fb5027b12119 | -3.29315 | -50.17597 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccb9538a-0cbe-321a-a3a3-405747030d49 | -3.27597 | -49.09982 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2709b3de-3d3b-3697-a218-fc260eebbe87 | -3.27248 | -50.16372 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77dc0bc4-53de-3746-97d7-35b0b6470fa0 | -3.27186 | -49.09915 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f0098bd-b198-304b-8b12-a9334dd5a37e | -3.26906 | -50.1655 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 167e383f-6cce-3a5f-b37a-992f3c58fa11 | -3.26805 | -50.16299 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c244d84-5c67-3198-af8e-ad68c343e30f | -3.26302 | -49.10152 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d319eb54-9088-3fac-920e-78ac71488530 | -3.26242 | -49.10518 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4702f475-7ca3-3592-98fa-e79de97e12c4 | -3.2583 | -49.10453 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cde668b-ccc0-3ce1-adaa-49dec774c996 | -3.24048 | -49.55812 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91b376df-0c38-3fb0-b2b8-040fcc82f578 | -3.23985 | -49.56205 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2f3bd5d-c93d-31a5-b3c2-54d2a196805c | -3.12169 | -50.42147 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ccdc05f-3e13-34a0-85a5-687719b0ac27 | -3.06768 | -50.48812 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b92530f2-1690-3cf0-bdd5-e913f49e650b | -3.06461 | -49.52219 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b2dca04-b339-36c9-843a-400f4168e595 | -3.06397 | -49.5261 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e887cd6e-189a-3c3f-9834-866ba4fadf12 | -2.9905 | -49.5272 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f9214d3-ac82-3147-9555-a4242f2eeb1b | -2.98986 | -49.53113 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6332cbe1-96ec-3669-8ddb-60e45dc40070 | -2.98561 | -49.53045 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cda2bb9-f22c-3d4b-aec2-e096b0484992 | -2.98199 | -49.52588 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7007bf6c-c182-392e-bba4-df20a306dbcd | -2.98135 | -49.5298 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b61bc95-a6b2-3669-8b81-b84cb1776a6e | -2.96862 | -49.29014 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 356f18ea-48f4-3b2f-95b7-4a31322fbe5d | -2.96802 | -49.29394 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e37fe39-16d0-3d9d-8b38-b112eb1c8bf8 | -2.96383 | -49.29328 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e721d78-ed49-3dc1-b1c8-3a44c02d5ee2 | -2.9557 | -49.21027 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ddd0c10-a05a-308b-87cc-40fb39541e58 | -2.95336 | -49.19827 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23dc27a9-620a-3f4b-b12f-2fbf49eff90c | -2.95275 | -49.20204 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1b2a3ed-ed0e-3cdf-ab6d-bc8cacb10fac | -2.95153 | -49.20958 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62c905ef-0e6d-3882-9c0e-31fd1a8f6e38 | -2.94859 | -49.20137 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c86ce28e-d9f6-3227-8aff-27f87c26fa15 | -2.94798 | -49.20514 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83f97903-d3ff-3159-8cab-e73ce9bcaf3f | -2.94737 | -49.20891 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32b3e3dd-c065-33d0-bdef-d721f52ab005 | -2.94676 | -49.21268 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5ffc5e80-a4d9-3af5-96ad-cd7ee18c434e | -2.89981 | -50.3956 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aca9dd70-5c0a-3b96-9c0f-41ce04316916 | -2.89908 | -50.40014 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3145be11-3185-3a82-9402-f89c441532ad | -2.89529 | -50.39485 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39ad338f-7b87-3199-8613-18e7757922d1 | -2.89456 | -50.39939 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f462173a-8c8c-3503-87eb-529960cfca7f | -2.89077 | -50.39409 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5be1336d-1888-31d6-9327-c9a5cf7fbea3 | -2.79455 | -49.59469 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf5ac1d-0eb6-351e-9faf-1a2dd7e9a5eb | -2.77813 | -49.24036 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b56c158-1bda-36dd-af90-f583563a46a3 | -2.77791 | -49.24319 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6f9f088f-6495-30e7-aabd-18a5320ff9eb | -2.77752 | -49.24422 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed5bd304-d70b-3463-bd4f-6cb0dc48d552 | -2.77435 | -49.23872 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd4c00fd-b12d-372e-8acc-12c1acc6ae0a | -2.77393 | -49.23972 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18de8f8e-622d-33ce-b522-d4fbb6af432a | -2.77372 | -49.24255 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28bb1adf-522a-363f-8d77-0e4fb2d80636 | -2.77333 | -49.24355 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5505a322-a320-34f2-81f8-05769036e5a9 | -2.77309 | -49.24637 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a1ef635-1223-3d6a-9f3d-e5d9a13f12f8 | -2.77016 | -49.23806 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92029854-9f1a-3a6a-bad8-3263cd3a8cb4 | -2.76975 | -49.23905 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be860813-ab46-3de2-9812-ffd9908cfd91 | -2.76953 | -49.24187 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d7c3381-fc3f-3a2a-9328-493df637ad0a | -2.76914 | -49.24287 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 735ba975-5a25-379b-8b98-a7ce16582502 | -2.75162 | -49.53452 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c655a240-b4e8-3768-946d-0b919ad3f2bb | -2.74931 | -49.52189 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93651a5-0c8e-326c-bf84-4ed6680a985f | -2.73688 | -49.95399 | 2024-10-10 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3ac87d-d6c0-3173-baaa-e6607168e9c5 | -2.72534 | -49.53429 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b8b722-2125-3a64-b883-e29865714a40 | -2.72521 | -49.54805 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a258a6a3-42fc-3f6d-9f3e-5f5b71ed671c | -2.72335 | -49.54628 | 2024-10-10 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b674f50-4cd0-3248-b96b-bec7d0f251a9 | -2.71336 | -49.13695 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa182169-6561-393f-9154-b20cc097e5c9 | -2.7092 | -49.13627 | 2024-10-10 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 970a49bc-ea9d-32eb-9b5f-d88c3dcfe8a0 | -2.60619 | -49.79215 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c091f7fd-4716-3b8c-a671-8bc059a80a2f | -2.60552 | -49.79629 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c23cd19d-fdb2-3611-9cf7-8597c8919271 | -2.60184 | -49.79144 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77a78eb7-b169-3442-8389-7abbd1df63ee | -2.60116 | -49.79557 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12b92697-0674-340c-abf0-5b0c9f58a7ef | -2.60047 | -49.79974 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68f94f1b-3c29-31b1-8fae-d2fb3b9bd857 | -4.95093 | -49.76249 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd449363-6f70-3d5b-9d9a-b790054a9207 | -4.92198 | -50.56468 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d027cf02-6882-35c3-b5ff-8640d71da83b | -4.87281 | -50.54091 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c055b697-351f-3c2a-a491-4bce51637bd9 | -4.87208 | -50.54527 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f8bd66f2-19f1-394e-851a-e7da815b0434 | -4.83018 | -50.79549 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
