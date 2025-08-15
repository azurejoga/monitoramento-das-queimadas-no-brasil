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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c495713-a74c-3528-bcb4-8e5ccfae3a5a | -11.55125 | -47.32064 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abdbd052-2d7b-3c14-9fd3-71e5d0d6ec2f | -11.35181 | -55.40959 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08be51e2-fcad-315d-857d-665ede9bf4f8 | -12.58729 | -46.96207 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47de1946-4a0e-3f5a-8ade-7051fa08a4da | -11.35985 | -55.42364 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e96b0deb-c1b2-35db-ac9e-7831ae69d327 | -10.35175 | -50.81108 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d63afa8c-e3c6-3cae-97eb-25e4aa2e9cd7 | -13.15624 | -46.86993 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a89d64a-5de2-320a-a4b2-d8d10fdb25bc | -11.35321 | -55.40477 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c601fb3-88d5-3160-866e-35caa8b9311d | -9.5072 | -60.51991 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6d876885-864c-3b07-b5a1-926d285a313f | -15.63634 | -48.07857 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b171bbb-0aac-3f60-9705-20c43912a28c | -12.49702 | -47.02411 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8368e8c-fdf1-37eb-8a33-799beecc30af | -15.57695 | -47.32205 | 2025-08-15 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3724fa19-d602-33fb-bce1-8b314f6caf8d | -15.58365 | -47.32313 | 2025-08-15 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3670712c-2ecd-368f-b990-c09da3108465 | -11.19335 | -55.01226 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f83428-b5e9-32f8-8e9f-92ad027a8206 | -14.01865 | -52.03971 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c15a07f-c103-3dee-9291-f072e1acd9d9 | -9.20569 | -59.64622 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d031fa09-90f4-3c6d-9a11-157621bbd36c | -9.16411 | -59.68094 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a6dbeca-cb1f-3945-b826-bb36b8f6395f | -9.50352 | -60.55196 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| de48ca28-e5b3-38bb-a43f-dd561ed0e7fe | -9.39843 | -60.5436 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3df6dbc7-442a-3329-a6ba-ff19c66c1c65 | -11.93081 | -43.43941 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f8f5e96-d3fe-360f-897e-1d4f266a4173 | -11.35108 | -55.416 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5df996d6-dba5-30e4-a92f-e86b382ba976 | -14.06956 | -46.31802 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab57c6c1-a787-3fa6-8af4-dd30ca08666c | -9.50752 | -60.5317 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a6ce6b51-df91-3108-85b5-1fd401386365 | -10.96243 | -49.56996 | 2025-08-15 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6ffd1c7-a65f-3183-aff6-3084f0d8fd06 | -11.34829 | -55.40381 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be07bf6f-6f08-3fdd-8069-9758e34a7c16 | -15.92429 | -44.7976 | 2025-08-15 04:29:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e005ea24-b359-3782-9b30-035876bda3e8 | -9.14938 | -59.42209 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aeb17df-721f-37a8-9aab-9e90edac3fea | -9.50488 | -60.54511 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c949c0a3-19ac-302f-987b-d1e42b60810a | -9.1543 | -59.6604 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b79e0a85-271c-3383-82c5-7ba6da413b38 | -9.50585 | -60.52655 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9be1edaf-26a6-3a7c-8ffd-3710cfc895d3 | -13.12462 | -57.16393 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ae665c-2d32-3a6b-83f9-dd8369a6b7c1 | -9.50729 | -60.55512 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 896378db-f177-3c43-ada2-9aef6071cb77 | -15.17337 | -49.74358 | 2025-08-15 04:29:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e3f4410-0ba2-3e9b-ae1a-036f3b746db7 | -9.15189 | -59.67245 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dde53590-38c8-38a1-b1e7-9ba702269496 | -9.20881 | -59.66569 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 981df553-485d-3e6a-b079-fd1ff6b23b10 | -11.3487 | -55.42665 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dd9968d6-e6ce-36ce-9033-037dc861336b | -9.17064 | -59.66901 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b476358c-4bfa-36b2-9b47-c58925a3a53c | -13.88314 | -45.55469 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aafb2b6-f6df-37dc-8fce-93148a9eb586 | -15.25092 | -51.71811 | 2025-08-15 04:29:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34d87d5d-2552-386c-8205-e6de963e9880 | -12.59286 | -46.9702 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4752ee9-6c35-333e-b40a-b693647361b3 | -13.32068 | -45.21921 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fb42878-e867-3aff-be95-da525e722545 | -9.16843 | -59.69423 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a82bc30b-87e8-3ec6-8d4b-2186995f5673 | -11.77847 | -47.40036 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 154cd81e-f0af-3ecf-a49b-9b785adaddb7 | -11.4074 | -58.54491 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27bc19e8-c154-3604-982f-3a58d1439c05 | -15.40058 | -46.59922 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f48503-8ff5-34f9-ad82-e35e8fc7fe4e | -13.57741 | -46.9661 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 810cbe89-f232-3a78-8e7c-b8c5ba198d15 | -11.40618 | -58.54832 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0746437-47f1-317f-a649-030bc50b6afa | -10.00977 | -59.22448 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddcaf618-e296-3bb6-8e06-d6e2d05dd1f5 | -10.00944 | -58.42805 | 2025-08-15 04:29:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 337a5ed1-035d-3b09-b5be-d1c7b5167c21 | -15.65447 | -49.77214 | 2025-08-15 04:29:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebc74afb-5fe7-378f-99d3-fe82330c2fab | -13.1195 | -46.84956 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41da5151-e235-3919-a183-6d4eaea56fd9 | -13.31658 | -45.22265 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 413e6bca-35d1-3f90-bf89-1d1d3e4e5f55 | -12.42919 | -48.70151 | 2025-08-15 04:29:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e3741f-8d6e-3491-a8d5-6c53747b7e25 | -10.04967 | -59.36222 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e3f39e2-4894-35b4-a1c8-3d9648a2c048 | -13.89301 | -45.56022 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 645ee01a-6a4f-36f8-8148-403345a844f3 | -13.11203 | -57.143 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6797cba4-40d9-3bdd-9724-d3c8609a3d19 | -13.11739 | -57.14404 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a970464c-7ecc-3255-aecd-f3c3bc88ee10 | -16.37012 | -50.89601 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dba1cb7-3833-3ec5-b3a1-d84d8560a206 | -16.60146 | -47.04988 | 2025-08-15 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42071e7b-5755-34c3-8398-f24d992a8c7d | -10.04898 | -59.36375 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca35d54-c4cc-39d5-b887-086875b5ae48 | -9.19918 | -59.64406 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ab9bd37-1c00-3606-a862-50c8fda0a761 | -11.35384 | -55.42835 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 99abeb23-5b48-35eb-9898-c91447073a58 | -9.50059 | -60.53003 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 918ea7c8-1a43-3c7f-a137-5580a334fe22 | -12.75832 | -44.41006 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b84c08cf-ffb7-37ea-9512-67d85f5363db | -12.26443 | -48.78665 | 2025-08-15 04:29:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b732d806-0013-3e99-bada-99294dcaf16b | -11.20601 | -55.91579 | 2025-08-15 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f4aef7-bdd2-3b5d-98e7-c9200afd3683 | -13.32829 | -45.21631 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2d9d2ef-0267-3fdc-b977-ebbe756a001a | -12.7571 | -44.41856 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 94b79610-a036-338f-a98a-02ad8810fbd6 | -12.67009 | -44.95092 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfd19039-71d2-3bfc-b01f-4008fb136017 | -11.34505 | -55.4208 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 121899c1-9b4c-318a-917a-e5f21359e2fe | -9.38317 | -60.54709 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 988d1665-892c-32d1-baa5-33e16921dd63 | -9.18225 | -59.65955 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a3636fc-47ba-3ef8-ba27-0874ba717319 | -14.0171 | -52.04252 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2684b162-c4eb-329f-84d8-3349609bada3 | -11.35752 | -55.43438 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cc8d8b13-bc25-3eed-b33c-ab3ebcdf3b9c | -9.20335 | -59.65818 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf740e02-d727-3bdd-92e8-bcf9125e4141 | -11.35877 | -55.42935 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b70b6239-98d1-3ff7-a550-d607fcdfe37a | -15.17331 | -49.74436 | 2025-08-15 04:29:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8f6caf7-5c43-3323-94b3-becd8ae7e523 | -11.53853 | -47.25 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4725d5cc-d1ac-376b-869b-c0094b4c6c9c | -12.4199 | -43.48964 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab123e2f-aeb6-316a-8630-f516715cd2c6 | -9.20026 | -59.63861 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af975bfe-ac0a-3880-9a5b-b35f9a391424 | -16.37712 | -50.89714 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c1f5982-2321-344e-9984-a27e782fdb63 | -12.58138 | -46.94313 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b7740cdd-f58e-39b4-9075-76f4957197e2 | -9.16283 | -59.67356 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed246cff-ab54-3689-8c9a-94745f6b11c6 | -11.92279 | -43.44046 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddb658b2-5522-328b-b0fe-2bd64301b3c4 | -11.73981 | -43.37557 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1968f099-7737-32d1-94c5-5813b246c436 | -11.35078 | -55.41524 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ae9ae902-2690-30ad-ae15-06356d69d100 | -12.58784 | -46.95851 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b09a3117-ec96-30b0-b8e6-296b1e9d63b7 | -9.21116 | -59.65371 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2c4c96d-cb24-31bd-b44e-6f1ef49f4866 | -12.41923 | -43.49431 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0944a0d0-afc7-300b-96f3-f0fd4dd307de | -10.11843 | -57.76591 | 2025-08-15 04:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d53cc8-f028-3dae-ab96-7fe886d0e540 | -12.57749 | -46.94616 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d34d0df-e73e-349a-b61a-b667ca712f2b | -9.50868 | -60.54833 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fecdb66-4cd2-3c5d-959f-6490bb639285 | -12.57472 | -46.94204 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6486b98-c2e8-3538-b69e-ef74d19c44f3 | -9.16097 | -59.6618 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23bb1c39-4749-3463-b078-3d3e708d5450 | -11.34721 | -55.40945 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f3d3315f-507f-3bf4-b7f8-8ceb0a0a3fbd | -11.21111 | -55.91684 | 2025-08-15 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 272ac76f-c90b-352d-b29f-dc45359a1812 | -11.34613 | -55.41511 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 27f87c54-00d1-36f6-a55c-59f43f3b8f4d | -11.91901 | -43.4399 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af7083aa-d3b5-3cc7-9927-82164ae40e46 | -11.44987 | -47.33667 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e14e6a52-782b-37ee-9a55-5587eebc4181 | -13.05141 | -56.84482 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172d5a3d-a98a-358e-b942-63a397e855a3 | -15.8977 | -48.32774 | 2025-08-15 04:29:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |


[Clique aqui para ver as próximas entradas](README35.md)
