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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54965935-cc15-3217-9267-db5ff7e0d4a4 | -13.19309 | -45.28603 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 142e12d2-54c3-3254-84ce-f01f91a859a7 | -13.37037 | -46.97762 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 714291a4-c997-3f37-a443-e96669065041 | -13.6566 | -46.91922 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea8116e-d70f-397a-ba94-efd355d7da12 | -14.00287 | -46.32986 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75426971-67ba-3935-abcb-533013023dfb | -12.70296 | -48.14433 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 130631e8-4afa-3205-9f3e-36ea79a1e4d8 | -13.59605 | -46.89123 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43c67c76-072e-305a-8ad4-e3d79d442046 | -12.43239 | -63.91459 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2c3431-1aa1-3361-9058-a5f6a4cdc2a9 | -11.30154 | -63.25836 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22c14c14-67b8-34ce-833c-96949f1c7ca8 | -13.37371 | -47.01655 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 479a62c3-cf74-307d-bd4b-300e402257dd | -12.82974 | -48.12128 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 30ae297d-577c-3e7e-9e0a-14156b73555d | -13.41657 | -46.95028 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ad33007-bca0-35a1-bc28-7110de08fcaa | -13.58079 | -46.90616 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fa56111-0dba-3864-98ae-7718a97f66cd | -14.00269 | -44.57527 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e22187fb-138d-39e2-9c10-bb3731eade60 | -14.02457 | -44.56079 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9799bab5-4502-39de-a6a6-d04f5ed7cbdd | -14.00136 | -44.58631 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8d5a892-45c5-35bd-befa-67962d9b7d78 | -12.91957 | -46.36205 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5a81e81-9a61-362c-81b8-fc20bef148ce | -12.61813 | -57.01511 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 817f842a-7e20-3e45-98de-4d33a7af248c | -14.59349 | -54.49086 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b53a45f-01da-3c22-b343-a8c2c951e385 | -14.00563 | -44.59253 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e95bd5bc-7c9e-3de3-b286-e793935e82fa | -14.45791 | -52.0134 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2d86604-7c55-341a-be54-d2168dafe548 | -13.35907 | -54.3877 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b00ce72-2ada-333a-bbf3-dd2622963c64 | -14.31717 | -51.86797 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9d08b93-0f16-39cf-9c91-29d532a4955f | -12.84145 | -48.09409 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33f87d6a-f878-3c01-b0db-cf4374267c44 | -14.84089 | -46.74218 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47457ac-61f9-38b8-86bf-c6961276f760 | -16.41031 | -45.6498 | 2025-08-30 04:51:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 542de4ab-1ccd-3e65-afbe-06d6452db18b | -12.51998 | -53.81487 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2aa4307-6fc7-3db4-ac3e-cbee6cc291e4 | -11.29979 | -63.26062 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b70a0df4-c1a1-3246-8d07-2cfc6d6750be | -14.00763 | -44.57597 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2b5b645-795c-3cd3-bbd4-26a8522c56e6 | -15.18823 | -53.78523 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f371ec9-553d-3323-aa00-8dc2e9d2db16 | -14.85381 | -46.77788 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f9ace1f-1226-3866-ad34-a44422bc54c5 | -18.13167 | -53.83073 | 2025-08-30 04:51:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36927108-628c-33ce-a7d2-2ba405bc62f2 | -13.37321 | -47.02035 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be708352-fe6d-36b2-bd37-a11f7b58a896 | -13.35969 | -54.38393 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28defbeb-a036-3d3a-a571-31bfd4bba368 | -12.84502 | -48.1522 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a4509cc-af4b-3a78-996a-700e05d67862 | -13.45975 | -46.94612 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fb86a0a-e69d-3bb2-9315-793abfead9ad | -13.58187 | -46.89832 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6234fc18-80af-3bff-94e2-fd140053d55d | -13.36638 | -47.00782 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c3ec6d2-bc58-3e6c-940c-7d079c5eaeff | -13.19246 | -45.29097 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f1b442-4546-3b86-86ea-0d014a657c29 | -13.36369 | -47.01624 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbea9f45-4d93-33c9-acc9-d5bac8dd016d | -13.39086 | -47.01515 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbac20fe-f2ab-3fd2-a7f3-9c3ab493c4b3 | -12.88837 | -48.1602 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68af1fd4-5c99-3581-9351-8f457fc656b2 | -14.35102 | -53.33425 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae4d1b1e-85ea-3bbf-9d23-cca83f9b6c47 | -15.0337 | -57.18742 | 2025-08-30 04:51:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acd4eaf1-4777-3a77-ad46-9c8f4195ea8e | -12.42628 | -63.91325 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c536eba-0d80-3f21-95a4-43e9d3b2c980 | -13.36803 | -47.0274 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e2b1817-e7f9-36ab-b3eb-b03e070f00f2 | -12.84887 | -48.15271 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daf2ff32-5cdf-3c18-80df-a0618b1d9fae | -12.85133 | -48.16297 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 512f5996-ef13-3d7a-b12c-2636bdd9a37f | -11.35731 | -63.26066 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0a9e8ba-35cc-3b31-ba7e-732a79c814fa | -13.50684 | -46.94726 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ddcbfa-e288-32d0-b7ca-351fd35b8e8e | -13.59555 | -46.89237 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d56f4f55-8ac8-37c4-8a99-c38c828edb2a | -13.46134 | -46.96556 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d95e9a-2812-3445-bb68-4a6b7f6d1f27 | -13.51481 | -46.95147 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a80e4e37-10ca-315e-b63c-b1b09e80dcfa | -14.00102 | -44.54467 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5609166c-eb2f-3ca9-a2f6-7ff765e2e2a5 | -15.22051 | -53.79818 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d817b2-b56d-39a1-adae-3acc5d5d5840 | -18.91756 | -56.25143 | 2025-08-30 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| aa0cc776-56d0-31a7-a0d4-4dec05faf775 | -13.1672 | -50.58596 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c88cc8be-ddfe-358a-897d-b26d18ba6153 | -14.02016 | -44.55271 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 26702790-6caa-3e08-92c8-319ea392a1a1 | -13.50318 | -46.94272 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 184956d3-77e0-310d-a853-4e6853530023 | -9.75911 | -65.09152 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f10610-e609-3c4c-b7d6-0f500dde4d07 | -12.94386 | -48.12877 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30a60b8e-dace-3294-9fcc-542e2ba19aac | -15.7654 | -47.76425 | 2025-08-30 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90e5a0e6-d5e0-3d45-87d6-cc15e8932939 | -13.37255 | -46.98309 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b16099a2-0836-3f04-95f8-91d81018b4bc | -13.96255 | -46.33468 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f873dd33-0313-35b4-bf13-ea9262639394 | -14.25636 | -45.24036 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| deac7464-7d0a-394c-a1d4-69f8bb649c49 | -14.83652 | -46.77571 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12cc53d0-052c-384b-9a5f-85ddf2ce8796 | -14.85436 | -46.77373 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c95973c9-5db6-344e-a04a-9a6dc1116bc7 | -12.92406 | -46.35207 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2927e4e7-3842-3ae0-89e7-e2c69a7e9446 | -13.4953 | -46.84014 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae0821e6-b8c6-3a19-a17a-03a7ed496f9c | -15.23824 | -48.25771 | 2025-08-30 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b73fb3e-7f8a-3111-9f80-4f3263e30eaa | -12.652 | -48.18839 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ce2a26e-5b51-3372-92db-308683a12921 | -14.00239 | -44.57337 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f87b6b04-cabc-3488-ace7-d7280701abaf | -13.47022 | -46.96296 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d45c96b-4007-3389-8bab-ba5b6e4cccd2 | -14.49859 | -52.04911 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3e55e4b-3ffc-3f55-86cf-7c97379078a8 | -13.97305 | -46.32305 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bedeecec-8d74-3bae-8c79-0365df455974 | -13.54908 | -46.95044 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 995a37ea-dff8-314b-ab1f-443161c57611 | -14.00179 | -44.54087 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3baf743-4b5a-368c-b990-6a26e477b010 | -11.39623 | -63.25876 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 898fa9b4-5959-3f6d-bd05-fd2dcae7b327 | -13.47067 | -46.95963 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3937cb0f-5fcc-3497-80a5-6538c4259dc5 | -15.63872 | -58.0821 | 2025-08-30 04:51:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f28ce71-60eb-3ea6-89cc-9bb73a79e43d | -12.83423 | -48.11737 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca138f8d-f5f8-3237-9746-048de76ab77a | -11.39684 | -63.24994 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d772c2fd-9819-3180-ba82-df4acb691027 | -14.35426 | -53.09971 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1298a331-5648-39cf-b665-5aa37008cced | -13.51229 | -46.84148 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a59a735-332c-3bae-b6ae-e1928ca6ea97 | -15.21441 | -53.79341 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18f1be8b-4874-3c71-aa44-a2fbe6fa4602 | -12.93362 | -48.11763 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b44d371-235d-3f94-be37-dd4d65382b28 | -13.37873 | -46.97866 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1789310-6aa3-3522-a59c-b718634c2b17 | -13.63285 | -48.18415 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83108176-df56-384e-9234-81832eb9d3b7 | -14.00734 | -44.57407 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6d073cc-5ec4-3c1a-b86f-cc6bdf3204b6 | -13.37249 | -46.99381 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71ce5c0f-9c75-3302-8696-290d6d8fe904 | -13.36786 | -47.01675 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae12f876-34e3-333b-8ec6-0afe611f2355 | -15.31037 | -46.08938 | 2025-08-30 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 060f18ed-3c86-3ff6-8904-854773e684da | -14.04006 | -44.51651 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47195224-2225-31c5-a96d-54a7e8af138c | -13.46089 | -46.96882 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3384323-3efc-37d7-912b-5a9687a9f4f7 | -14.009 | -44.56467 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7601f42-3541-32be-8a2e-0eb345a515a3 | -15.58702 | -56.02117 | 2025-08-30 04:51:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ee10305-8a0b-36c6-bd16-23156090ab45 | -13.73286 | -45.5328 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f49fef96-fb44-3cf0-85ce-3e159f55575e | -13.3722 | -47.02792 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91fbcd29-c28a-37b3-99d8-2822038cd796 | -13.42067 | -46.95144 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7a78d23-b8a8-3d8a-9961-875347924d40 | -13.58133 | -46.90224 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f088650-0fb6-3e20-97d7-733cc81faf64 | -14.00592 | -44.58511 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
