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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf0fc2fe-dc79-33b6-b963-45897291249f | -3.90959 | -48.3619 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6699dce-1f69-3947-a743-52ff5f2e2228 | -3.90734 | -48.35328 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47596b19-465a-3b82-a943-6c516f9b0a2b | -3.90669 | -48.3573 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e28e7a-08e4-39f1-bdfe-2505595bbbc7 | -3.90604 | -48.36132 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a82ce69-6f95-32b7-a756-e31ebd7b45f9 | -3.90248 | -48.36075 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 67658e1c-de3b-360b-9a11-b46749228a4c | -3.90219 | -48.34005 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 085e7008-2919-3bdd-a5ba-6eebbad944f4 | -3.89864 | -48.33949 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1df78fc5-77df-33e0-a4d9-ad66a866663d | -2.20616 | -48.85791 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec692d78-f6d9-3ac7-aa4f-d22f0a364ecf | -2.20244 | -48.85733 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a6aff22-faaa-3900-bfde-f7b9787c5e9e | -2.19035 | -48.85269 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 942f6330-a6f7-372c-98a5-886acfe0ccd4 | -2.18126 | -48.83763 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebfe1f9b-8064-3065-9dee-6c2aba02c3c2 | -1.1501 | -49.16704 | 2024-10-15 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c5f388-22d3-3f32-a7c3-05e0709bab93 | -1.14936 | -49.17178 | 2024-10-15 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15b57c4-f40c-3bc1-be89-c01b8ce627b3 | -0.87484 | -48.70495 | 2024-10-15 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3ea9a71-f03f-3e49-86a6-d2ac885ce690 | -3.19323 | -50.45506 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d95e4ca-afd0-3420-a6f4-5178899d7901 | -3.18863 | -50.4578 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c71ddbb1-3eca-3fbd-8a49-54e0e54c576f | -3.17535 | -50.4628 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e09601-5bc2-3f5d-be11-bcb72aaf5c6e | -3.17072 | -50.46566 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1463fc5-b5a3-37a5-a9ea-fc9567ccf8f7 | -3.169 | -50.4763 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 265124ba-ee3a-35c5-a594-45a69319d2c5 | -3.16842 | -50.47985 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4bc3294-c0c3-3cc9-99e5-8518a99e9058 | -3.16609 | -50.46855 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f52998e-0133-3a81-be5c-607e2c7ac403 | -3.15913 | -50.46012 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b8ca902-33c1-3950-9c21-50b030afc5e3 | -3.0675 | -50.48968 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870c6a44-40ac-34bf-a954-da6e2298e3a2 | -3.06344 | -50.48902 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e4dc057-65ad-3698-8b9b-b65b6a23c49c | -2.77799 | -49.42966 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1f8dd85-d8ac-391d-b9a9-527cf10bbb0c | -2.77724 | -49.43432 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a20e46-d805-3661-94f4-dd960a2d7172 | -2.6839 | -49.05375 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78abbd69-23e7-33ee-9186-2b49fb150ffe | -2.68015 | -49.05316 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f412a6f2-183c-36cd-9da8-75a882c9e43d | -2.65909 | -49.51946 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29eecd8c-0d08-30be-a86a-7559f79df1b6 | -2.65601 | -49.5141 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 567e6797-0a3e-3a9d-a32a-98057e006459 | -2.65524 | -49.51884 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ce1cfbb-64c1-35fd-a8fa-50cbe0641376 | -2.65216 | -49.51348 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0853afe-b7f0-3fb6-a6c9-cec2d3bb8c49 | -2.65139 | -49.51822 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f014af07-3cd4-31f9-8838-de27f5bd06bc | -2.65062 | -49.52297 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4196734-9d22-3c2b-a520-64ba739a7b77 | -2.62915 | -49.27766 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4f4da83-053d-386f-9ad0-ba16410280ff | -2.62535 | -49.27706 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e6af530-9765-3be9-9be0-da464859fc5e | -2.61748 | -49.08451 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9135656e-af1f-3479-ad6f-6889c4f4c9bd | -2.61675 | -49.089 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8880edc9-2c91-3978-942a-57b21d6a215c | -2.61312 | -49.11153 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36425c17-6f90-3c0a-8ad2-bbeeb28b085e | -2.61008 | -49.10646 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cba00934-0b17-38da-b88c-649728efc9b6 | -2.60487 | -49.11486 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4106a7f-22d4-36f7-9340-df8eb7b09245 | -2.6011 | -49.11427 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d164c10-fd37-3b06-8d6b-2660f75722ab | -2.58164 | -49.13903 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82c7ca67-6624-3816-b245-de5fc1cd8063 | -2.57947 | -48.95628 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef053c44-0311-3333-9f2a-32f848d3708f | -2.57618 | -49.07794 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd15598f-b3c5-3cba-9217-e7796bc9ba69 | -2.57543 | -49.0792 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd4a75ef-2107-39b2-b654-4a96aa56c5b9 | -2.56364 | -48.93561 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca53dfc-e5c6-3a1e-9314-56b43a801a2f | -2.49958 | -49.07177 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 63e27607-851f-353a-bfd2-45e5377b2e27 | -2.49582 | -49.07117 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d993cc33-1637-3fa4-8d15-4b97a2a8cf64 | -2.49075 | -49.29513 | 2024-10-15 04:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f91a3b60-295d-322f-899d-2346b388fe61 | -2.47929 | -49.02945 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceb8f1e2-0785-3448-a82a-8c6177ff7f33 | -2.47916 | -49.03164 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 459d8140-ec25-32d7-bdb6-86c962440b32 | -2.47859 | -49.03394 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e6896f-67e8-38d1-ae74-a46519b07f06 | -2.47329 | -49.6275 | 2024-10-15 04:23:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1fc0631-160f-39c9-8c60-a80e809dd7cc | -2.46941 | -49.62689 | 2024-10-15 04:23:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c6be0c-6e6a-3a0b-87bd-5a8d489ae304 | -3.45755 | -50.31631 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cab9db51-3db8-3ea3-b5f6-970051f74878 | -3.42382 | -50.26136 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73cd7daa-9ad3-3bde-83a0-9ba70fb33873 | -3.37393 | -50.34084 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60287529-1f93-3936-aee3-a6a318d91208 | -3.37335 | -50.34435 | 2024-10-15 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b3b4dae-eafa-3dc3-9f49-78f6ee2013ea | -3.19728 | -50.45574 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc6a6e2b-db40-3163-844a-0eb9b86309a7 | -3.18458 | -50.45712 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3910a699-6923-38e3-a53a-5f28a34738c0 | -3.18402 | -50.46059 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84cd0aa0-a404-33cf-8835-cd91ec542f67 | -3.17997 | -50.45993 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d37f5038-1ad1-32a0-b479-07a81371a6d8 | -3.17592 | -50.45926 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89672614-2548-3dc8-8c25-afe7552b9f2a | -3.1742 | -50.46987 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1667e4f-fb4f-37e5-8750-2c741ce2ccde | -3.17129 | -50.46212 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ccf4ce-483a-388c-a874-3fb6a5d3cf5e | -3.17015 | -50.46921 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba3afd6b-154a-3444-ac46-c6eeeadbb9e4 | -3.16957 | -50.47275 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c817be9-643f-3916-8c9d-344477e170ad | -3.16667 | -50.465 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361f1a21-1756-3b82-b562-276cc6bdcaf3 | -3.16436 | -50.47919 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bcf80456-9aff-3063-8421-d9dbad569258 | -3.15508 | -50.45946 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 410c5f18-69a8-32fc-ae9e-f3bd1d255b21 | -3.1545 | -50.46301 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f91cac4d-3ad8-3b89-a4d6-c9ff530a2565 | -3.07157 | -50.49034 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16197c5-f493-35b0-9826-4eafdcd80405 | -3.06693 | -50.49325 | 2024-10-15 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 809d269f-f85e-384d-874f-ade3bb91f97e | -2.44342 | -50.2378 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 255d30a9-5a45-37e2-b590-282b2c45cbf4 | -2.43825 | -50.24414 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00cd4c9b-ef24-34af-8047-d1cbd97cd3f2 | -2.43648 | -50.22949 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce8166e2-fef8-3278-8895-09aa3bb8611c | -2.43591 | -50.233 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c37a513e-f3c1-3d75-a8bd-9af8fb89ba8a | -2.43534 | -50.23652 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e0b952e-d9b1-3d3f-8306-25bfae89091a | -2.43421 | -50.24351 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51fab3ef-7500-3c5d-9d2c-65f3b53c440d | -2.43187 | -50.23235 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f0927b5-1c30-3435-9b7e-d51bcbfd940c | -2.43995 | -50.23365 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba466f24-ec1e-3882-9637-d034e9e67688 | -2.43938 | -50.23716 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47c3fbfa-085e-3680-8602-6f7f81891b3d | -2.43882 | -50.24065 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c3fd95d-7d82-3edf-a63c-c437634741e8 | -2.43478 | -50.24001 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f3d5004-73c6-30ff-94a9-8b645fc3d234 | -2.4313 | -50.23587 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02680bf3-06bc-374e-907f-6d84697636b5 | -2.43073 | -50.23939 | 2024-10-15 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 869a4c9e-d891-3b65-a304-e8b01db70746 | -2.42328 | -48.94732 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f809e28-e6a4-3beb-bfeb-f2c912828424 | -2.41955 | -48.94672 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65f558d-1b91-38ed-878c-51bbaabe5174 | -2.41208 | -48.94553 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd728596-cbc8-3bff-ab7e-90639ce5786b | -2.41136 | -48.94998 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd33510-5b13-3c6b-ab2b-cccb4a0c9de8 | -2.39237 | -49.18758 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d51cd806-5d39-3138-a073-d47106520880 | -2.39163 | -49.19214 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 196adfa6-58a9-3736-ab9c-3cad9ec4639b | -2.39142 | -49.14522 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b25fe0bb-5e5e-3976-95b0-28a16f9f1d31 | -2.38858 | -49.18695 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 98426b81-5bd4-3876-8bd5-0adb552f7fe5 | -2.38785 | -49.19153 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 926679a6-6407-30f8-a29a-827d56497a21 | -2.38764 | -49.1446 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa4e9b7-b2e2-3297-bf84-09e0bf68c5ee | -2.38607 | -49.13038 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c54c5781-8fc8-3a7d-b8f7-616b91cf9fad | -2.38533 | -49.13491 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d34eae9c-d5a3-3ace-bdaa-973f85271814 | -2.38479 | -49.18637 | 2024-10-15 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
