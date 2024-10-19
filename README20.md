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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dcf5e71-8a50-309b-9081-cfcfed73a72b | -2.46302 | -50.25001 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b884707d-a748-3f08-ac01-6b78160f5bd3 | -2.45904 | -50.24939 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a1fca63-d463-33a9-9912-86038cf76c3c | -2.45848 | -50.25281 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22112f43-f827-39f8-a891-c97e6feace63 | -2.428 | -50.27526 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26b8c445-6c11-388c-9c31-e8f987a9e5ad | -2.41836 | -50.2844 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2947fd49-30c4-38c8-a5f3-edd36ed13b17 | -2.41781 | -50.28786 | 2024-10-19 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d146b58c-714c-3c56-b4fa-74dc2f02b88b | -5.0266 | -50.45178 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 239ec077-81f2-3d06-aafa-ba17afab20fb | -4.95305 | -50.8724 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c0c3bf7-03c5-3254-87ac-6beb7826440f | -4.95115 | -50.87105 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e931f142-27bf-3560-a4af-6c42ac009835 | -4.49768 | -50.14061 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22972123-e490-364b-bb6c-0b1209ce1ffd | -4.4969 | -50.14543 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9871b8ca-4744-3af9-90ff-58aa4ef1aff1 | -4.48454 | -50.19742 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dc68ae5-e134-3007-9ac6-f0969c068a53 | -4.46706 | -50.3546 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f47a2aa2-5d61-375c-8aa1-447dfb60c926 | -4.44839 | -50.15249 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c76e9019-f275-3bb4-9260-f57810214539 | -4.41358 | -50.53528 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4286b4-95f4-39be-9533-fe30368b7bc2 | -4.41046 | -50.52965 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a38a246-479d-3994-8367-cb0ca903a3a3 | -4.40964 | -50.53468 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 17fb9bf1-f6fd-390e-bda3-219e4f9f2d19 | -4.40569 | -50.53405 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4b04589e-66b9-32c4-b652-4b93d9f9be29 | -4.36562 | -50.80339 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8344d13-4195-36e6-8bbd-2ee724f4b273 | -4.32715 | -50.81166 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d296256-8028-3071-a38a-5ad339d0c510 | -4.32313 | -50.81102 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fed4ae9-6dec-301e-92e9-0c2655cea60b | -4.12873 | -50.7463 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c11e5ba1-de57-395c-9ce7-d97d465803e4 | -4.12816 | -50.74977 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7136bb94-6101-323c-b06e-d68b2247d452 | -4.09625 | -50.75898 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fba7755-a3cc-3e35-bd53-64458db3673c | -4.88233 | -49.75461 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c620517-6ded-3029-8233-d1f8eb17674a | -4.59813 | -49.51783 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99dc0683-9ba7-30aa-9829-c83f3ea42253 | -4.55658 | -49.65702 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b440227-d0f0-3a1f-a4d3-0a3d84ed013b | -4.55213 | -49.66082 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf3014a8-f828-3e7a-8d96-0c3c9cc97528 | -4.09569 | -50.76247 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c5ba16-4bd9-36b0-9566-44ef23748c64 | -3.87438 | -50.2622 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 871b2200-c71b-3451-a5a0-d82e3bae65d3 | -3.86248 | -50.48194 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c74a0ad5-0f9d-370c-a2cc-8f2b80ba3eb5 | -3.85582 | -50.07618 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05bab5c1-65cb-35d9-bcfd-fc68395b3348 | -3.85196 | -50.07558 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0eaf379-8250-3752-8da7-38ec71f876f8 | -3.85118 | -50.08041 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 869fa7dc-1639-3ab8-8995-56325220a00f | -3.84962 | -50.68612 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 733a04f3-3005-3bfc-88ca-a96a510e1e14 | -3.70504 | -49.83184 | 2024-10-19 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8496156c-7339-3d91-b857-ff1d2311ce02 | -3.70457 | -49.82953 | 2024-10-19 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 475dea2e-720e-3513-9670-77d78e936fea | -3.70122 | -49.83125 | 2024-10-19 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e1a3cf1a-ca63-39f3-8792-8fde66064ea6 | -3.60363 | -50.58465 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0cb52f91-eee0-3c57-a260-9efaee870ede | -3.60307 | -50.58808 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 90eea951-af5e-37d2-b60c-a3bcfc593f66 | -3.59964 | -50.58395 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ebea23d-c63d-3e60-a2fa-f48b0549334c | -3.57504 | -50.57266 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b437bc41-9b85-36cd-b895-a8eaff2e65ad | -3.59907 | -50.58738 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec7b7fe2-34a8-3251-85d5-3ee59482aa57 | -4.68278 | -50.65885 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78509fde-f7e7-3041-a189-d6ace7057926 | -4.55285 | -49.65639 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3dea8bd-8059-3d6a-9fc5-3d0bcd034e30 | -4.4246 | -50.54215 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 602b8f7f-d94a-3479-a1ec-ea97b5f1bc2d | -4.40652 | -50.52902 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc43d0d0-880d-3e3c-856e-3359a0cbd695 | -4.40185 | -49.74923 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0961a24-a55e-3503-bebc-fe3ca70e37b5 | -4.39809 | -49.74865 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2ff7cd6-0acc-359f-a628-e5b0024c8a59 | -4.38971 | -50.80724 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d908c8a-aebe-32c8-b12b-3ab9a26f2961 | -4.38915 | -50.8107 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00f4109b-35e8-3f21-a0df-2d650b568356 | -4.36963 | -50.80406 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbf96efb-893b-3457-8a50-60fe91fc92e5 | -4.33599 | -50.68475 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 894cb925-d6e7-3d49-8207-1802df922a51 | -4.32372 | -50.80753 | 2024-10-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2433a527-9167-3134-b297-451571cfb660 | -5.58011 | -51.04888 | 2024-10-19 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e07a7682-0e11-36ad-9e04-5b59e91afd5e | -5.03108 | -50.45553 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4bd40cbb-b735-396b-a5f3-8a1cb1bdcebc | -5.03049 | -50.45239 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa67807c-9f0a-3e55-9b14-eeca3d86aef5 | -5.02971 | -50.4573 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6ecdff2-7b32-3d8c-9eb7-3885d309efe7 | -5.02719 | -50.45491 | 2024-10-19 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dcf6c31-bf9c-38ef-98c2-15b76e34b94e | 1.72846 | -50.99431 | 2024-10-19 04:25:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa624134-c974-3aca-b7a9-367ec98b65fc | 0.23667 | -51.00076 | 2024-10-19 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aff0b969-8689-3a33-b6c8-0b69cf19e4bb | 0.00533 | -51.22256 | 2024-10-19 04:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1092687-07af-38ca-b6c1-22f477aa280a | 0.00091 | -51.22324 | 2024-10-19 04:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 547f6013-34a2-37ed-98bc-622694dc2c10 | -2.1715 | -50.52483 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027938c3-70b5-37be-9d91-e0ff14d8254b | -2.16367 | -50.69994 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c55ab911-7cf2-3d84-91d0-f661eadbe198 | -2.13548 | -50.83417 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f7096c-8abb-38a0-bd3c-7ef0f655100f | -2.1332 | -50.83344 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69666ff0-e2bb-38de-ab21-f2e7efd5bcb0 | -2.13194 | -50.69513 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c798de27-1031-347f-afc4-0f5ceba27651 | -2.10452 | -50.84098 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb548cbf-6cb2-3976-8706-47e688fef0d5 | -2.10015 | -51.43795 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20b2ba1f-bbf5-3563-b46b-a6d6e438aea7 | -1.86053 | -51.35907 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2a4fde3-8830-3bde-9261-96e2e64e784b | -1.33712 | -50.57123 | 2024-10-19 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a128b0e-94a1-3f1f-adda-aa57812b7908 | -3.28087 | -50.66549 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbdf5e4-6684-3f13-b4a9-6537f657a609 | -3.27741 | -50.66131 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb85a59a-c2ea-38fa-9ab0-95aaedddeb93 | -3.27682 | -50.66489 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16c52c5b-b1e2-3380-b4de-23f9318db092 | -3.27336 | -50.66071 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 70964fb4-0f5a-3d16-ae43-cd342e00999e | -3.27277 | -50.66428 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8cf25c0c-47c0-30b2-b5e8-2cfcc9d0a7cd | -3.26873 | -50.66366 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6fce2de-f821-3e79-8eb1-b0287be401a4 | -2.89807 | -50.70729 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b03a1b10-5ce7-3e99-84e3-0712ed66cf7d | -2.89327 | -51.67619 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d98d93c3-9c92-3b18-85b2-4f129f07a5b5 | -2.89189 | -51.68457 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0da1a974-cd6b-3cde-b91f-94a0bc252aad | -2.8793 | -51.65266 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e21e483-51cb-34ea-b757-8d5e0a0baba3 | -2.87684 | -51.61388 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78558b72-0242-36df-bf42-f6518129518f | -2.87615 | -51.61798 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18040b88-5819-327a-b2f0-eb11a1e74a79 | -2.87511 | -51.6139 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07eecc9b-6970-3d18-b7c5-33296341aa24 | -2.87445 | -51.61801 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da6d24fa-89b5-3e80-a55e-7bd5648b204b | -2.87249 | -51.61323 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9d3a3c9-daf0-3519-a712-8bbf5391f09e | -2.87148 | -51.67279 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec5f3dc2-a796-3365-8357-fc5d7abf114d | -2.87079 | -51.67696 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df7ca26e-9970-3643-8bc9-3f279f42c754 | -2.87076 | -51.61325 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e18c169-e2b9-303f-b91b-4186183406ff | -2.87019 | -51.67294 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa28111e-2bf1-3a88-a269-bb77de509dd0 | -2.86953 | -51.67712 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5876ddee-868d-359f-a1f9-2c048450ab79 | -2.86713 | -51.67212 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38c5f19b-dd37-3f7e-b005-e4fbb320f0c7 | -2.86679 | -51.39054 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 434399f5-abb5-3308-949c-7bb35f51b629 | -2.86612 | -51.39465 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe45afc5-da58-370d-9393-3250a008dbc9 | -2.86237 | -51.28344 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b21e5d27-84d8-339e-89c5-48abb28653de | -2.86173 | -51.28741 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e07a90-1806-307b-9060-cbf30e870353 | -2.84149 | -51.30455 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffb57d5f-2f40-3807-b9e8-4cac8b36aff8 | -2.83789 | -51.2999 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a56c21f4-ffbb-37dc-a89b-38f627be1e51 | -2.83724 | -51.30388 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README21.md)
