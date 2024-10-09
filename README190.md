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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7079598-2b3b-31bd-86d3-657b419ee3e7 | -21.57766 | -46.98884 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01092979-d0a8-306a-84a2-1b88c6f8fe27 | -21.57675 | -47.9037 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28bd6a8b-f11f-3a0e-b69c-62b91b99ca81 | -21.57632 | -47.90833 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2e36ce7-f9d4-3eeb-ac78-65cff991304a | -21.57611 | -46.97678 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d09a1a55-5c72-3795-b71d-9e396e214df0 | -21.57572 | -46.98162 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ac8505c-a937-3ad8-bb83-38262c0198e8 | -21.57549 | -47.88449 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e32e3c2-98e3-36ea-834a-6139f8eaddb6 | -21.57535 | -46.98624 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89b45786-034b-34fc-85d8-e31c3ebb58aa | -21.5751 | -47.88911 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb8b00bb-9792-3843-a01b-854f45dcaadd | -21.57394 | -47.90297 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dee86710-92a7-3add-9326-f6cc2a202abe | -21.57354 | -47.90764 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1889cf96-3fde-3779-bc73-2f4501cd5730 | -21.57178 | -46.98365 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b2ffd5a-1547-3639-885b-ad2d18dabc78 | -21.57135 | -46.98848 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdbf8139-f7db-327b-b7c7-8786bbe00c07 | -21.56944 | -46.98092 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c51437d1-029e-362f-bf26-665a41e3376c | -21.56905 | -46.98575 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 501c9cd1-2967-3681-880a-5b50c636ebe5 | -21.56592 | -46.978 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b41732eb-a26b-32b9-a546-8f5c62634968 | -21.56548 | -46.98312 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92d70252-384a-3a99-b0a8-5aea021a6715 | -21.56504 | -46.98825 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b6d955f-e55e-3294-a378-b38389e2c37b | -21.56359 | -46.97479 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c57ed6cb-d752-35fa-94b5-d7b3edb9389e | -21.56316 | -46.98013 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76d9ddf1-0db8-339a-a3f2-5e61b72b44d7 | -21.56274 | -46.9854 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c19265c-de9f-36c7-896e-945d1c2e5e86 | -21.56233 | -46.99056 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21d70ced-bf1e-3486-9c3c-ee3491671aa2 | -21.55964 | -46.9774 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0fc482ea-4264-3014-9297-4de69cd038d3 | -21.55918 | -46.98272 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d11849bf-72ec-3a46-89a6-f9725b023001 | -21.55873 | -46.98789 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2acc86a0-aa48-30cf-bf48-431536ac3f4c | -21.55684 | -46.97989 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bea8ab56-2b5c-3f20-95d5-8b940d6c40d0 | -21.55644 | -46.985 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46b2d4f0-32d0-39fb-a039-72cb39b3a3ac | -21.29748 | -47.21401 | 2024-10-09 05:06:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 993abd53-5121-39aa-9540-c506e6c5f59a | -21.29707 | -47.21881 | 2024-10-09 05:06:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2a8fb448-df6b-36b7-8a21-5556eadcf631 | -21.29126 | -47.21379 | 2024-10-09 05:06:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0bb833bc-9fc9-32e1-a59e-a35e66892018 | -22.82408 | -48.43267 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7db9bb6f-683a-3431-8b75-b985dc700716 | -22.82368 | -48.43703 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 56f6d9e4-d722-3722-aac1-d1d61a87144d | -22.82317 | -48.4347 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 84b84c89-d878-3b3f-996a-ca6bab1a2d23 | -22.81788 | -48.43603 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc5e1372-c054-3675-89aa-a88d58e2388c | -22.81736 | -48.43374 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2360d76b-7466-39af-86fe-5921a078ad5d | -22.817 | -48.43802 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d5038d51-0417-343f-894b-9d93ae563c98 | -22.81209 | -48.43501 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab49ef87-67cc-3422-83fe-e4a057bd6c1d | -22.81155 | -48.4328 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8422b466-48c7-3b45-bb6a-61534b2e47de | -22.8112 | -48.43688 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b80fe68-6927-3e45-9fec-780476013fea | -22.81093 | -48.44783 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e371e4-a70c-3e6f-b457-d85c8f3b2a11 | -22.81047 | -48.4457 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c05bcd3-0fa9-31b9-a169-756090117ba6 | -22.81014 | -48.44961 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29977021-77df-3e81-bd8a-74a60e1e057f | -22.80628 | -48.43412 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fa560b6-fb4f-3ac2-b4b7-94f93b5bf0ce | -22.80572 | -48.43203 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cefa9cac-ad3a-3900-996c-2a279325078a | -22.8054 | -48.43588 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79e106cf-1b50-3d53-a4c3-e5260e670023 | -22.80511 | -48.44714 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5117dc28-3c2a-3c42-ba62-a65c0b84985b | -22.80477 | -48.45087 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1468317c-2934-3236-9d52-7dc5877dabd9 | -22.80465 | -48.44493 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27beb53b-2ce3-338c-8b8d-8bac24237b1f | -22.80431 | -48.44892 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc720d57-68cc-3573-aa08-7967ba0729d1 | -22.80082 | -48.42926 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24464ea4-9dba-3937-86c9-15df34a10033 | -22.80047 | -48.43324 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e51f2b4-564f-3b28-bde5-ce2e84ea989a | -22.80012 | -48.43717 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86b2e7fc-bfde-3a7d-9266-7f030e74a366 | -22.79991 | -48.43111 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 764442e9-194e-3d00-8ae9-126cac3818d2 | -22.79959 | -48.43493 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7579d8e6-81b9-37f4-b515-e0d3fdd80e9a | -22.79926 | -48.44673 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ad8464-9d56-3036-83a6-eae5e027c2dd | -22.79846 | -48.44859 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9f3c42f-8ce8-353c-9480-7f00d9746b35 | -22.79504 | -48.4281 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e51461a-edab-37e8-9409-41bd3aff01e4 | -22.79467 | -48.43222 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d5f2e84-3ee2-33cf-8a26-732dbb152beb | -22.79432 | -48.43618 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4482ea85-d629-3de1-8a10-7c523aab9bf2 | -22.79411 | -48.42997 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 315309da-caaf-3c4c-b80d-97acc8fab203 | -22.79379 | -48.43392 | 2024-10-09 05:06:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0599e2c2-dcc8-31bb-9a74-7572bcadaa17 | -20.76775 | -48.57656 | 2024-10-09 05:06:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eea3fc9e-9768-3cbc-b1da-43853fae7303 | -20.76206 | -48.57621 | 2024-10-09 05:06:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 319a7d70-fbea-3bd9-9fb3-d12952c6f894 | -20.61607 | -49.359 | 2024-10-09 05:06:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e1714da-2f23-3025-bf15-fcd3fcd5938f | -20.61571 | -49.36251 | 2024-10-09 05:06:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a41ddd8-15d9-350e-aac9-b5357ed34f6b | -20.61532 | -49.36618 | 2024-10-09 05:06:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29e4e5a7-0c8b-3365-b739-5f620af70ec0 | -20.61341 | -49.35825 | 2024-10-09 05:06:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d57e118-f0fa-33a8-8be0-d0b627b70507 | -20.61308 | -49.36175 | 2024-10-09 05:06:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3bb785e-6a94-3af7-ab0d-7b915f0102e0 | -20.61272 | -49.3654 | 2024-10-09 05:06:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67222896-a53c-356c-a8f8-ca82ea0361e1 | -20.6107 | -49.35842 | 2024-10-09 05:06:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9e4348b-46fa-3d4b-84ea-6e629b622747 | -20.61033 | -49.36192 | 2024-10-09 05:06:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33ceb3cb-da29-3e51-9c1d-a8c46ad8daf6 | -20.6077 | -49.36113 | 2024-10-09 05:06:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b09f737f-12ce-3483-b846-b74000e6888f | -20.59492 | -49.35336 | 2024-10-09 05:06:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4705a6c3-5733-380c-a209-fff1da69b477 | -20.58953 | -49.35288 | 2024-10-09 05:06:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a35711c-0837-38ef-858b-23dc28d298cd | -20.57486 | -49.33686 | 2024-10-09 05:06:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae57ec75-daa1-3088-8ff4-5dd81c2cb00b | -20.57019 | -49.32932 | 2024-10-09 05:06:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d18c2a47-4b17-3906-ab40-0b0968b7a148 | -20.36785 | -48.72609 | 2024-10-09 05:06:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52c5d02b-7e60-3852-a2df-b9703c3a6597 | -20.36711 | -48.73385 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ffc83c0-bb72-3887-8854-bb4010d6d9eb | -20.36673 | -48.73776 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37f39183-b0b4-3147-8af3-d24b35eb5156 | -20.3619 | -48.72932 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d670bc0b-05df-3967-9d47-1b5bee2af23a | -20.34016 | -48.73178 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a68d995-5ad5-34d1-b618-22bc9fde049b | -20.33917 | -48.73137 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68cada68-03cf-34c5-85e6-98aa75d57289 | -20.33497 | -48.72729 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea102169-5df5-3287-a238-dce6c6c4deb2 | -20.33459 | -48.73111 | 2024-10-09 05:06:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e60be43-d25a-3580-bdc9-b8270ef17439 | -20.12711 | -48.85188 | 2024-10-09 05:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b4dfa7-b844-3761-ba0a-33b51a7c1353 | -20.10771 | -48.82312 | 2024-10-09 05:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c42e2b5e-13b8-3a37-8337-b04541800d48 | -20.10732 | -48.82698 | 2024-10-09 05:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e7c4189-94ed-34a5-aa19-9217fe5073c9 | -20.08555 | -48.82122 | 2024-10-09 05:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2739f86-b0e6-3dd4-9f6f-4fe8fad5ac5b | -20.08517 | -48.82499 | 2024-10-09 05:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ab54be4b-3470-33e0-9d2c-d3fb621fc5ba | -20.02113 | -48.22658 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f1e2f22-723d-3d7c-9fc0-ec313238af50 | -20.02072 | -48.23086 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf655db7-3253-3255-8aa0-4021c03439a5 | -20.0203 | -48.23518 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4153a10f-f299-36c0-ac61-efb4a9c7eaf6 | -20.01989 | -48.23949 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28e29e4f-b07e-3e0b-a263-09483da1cdf7 | -20.01538 | -48.22611 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43420df7-bf55-3640-a6a0-94f790b2cdb6 | -20.01455 | -48.23484 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa15145f-3adc-3b6d-a2ea-fe6493c2899f | -19.77703 | -48.2656 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25245db4-5595-35d8-b805-d6ce46c4a54e | -19.77664 | -48.26971 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bee30972-333a-3cb2-b79b-ca8d344a7607 | -19.77478 | -48.26589 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8a6a7e8-3b98-3dac-bc90-f66667578580 | -19.77436 | -48.27 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 576fa479-e1ca-372a-9c47-c172df3a222f | -19.77092 | -48.26927 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ece599b-0246-3092-9695-a909c7f3f367 | -19.76864 | -48.26956 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README191.md)
