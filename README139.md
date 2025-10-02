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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b62af21-0134-3ea1-adea-9c50bb0b9eb9 | -11.17251 | -47.27092 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 858efea6-951b-3566-b4ef-417a1434e951 | -11.05439 | -47.80625 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 287c992e-e17f-3a78-967b-cd2010ed85d7 | -11.43277 | -43.88718 | 2025-10-02 05:55:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e26153ff-c744-3879-b816-df65d36ef9f8 | -9.85913 | -44.60024 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a33fc8f4-0b0f-3c81-b2a8-9ddf2927340d | -10.98609 | -46.61342 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6728514-48f5-300d-846e-50f2db33e1f1 | -10.6523 | -48.49063 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99b88f5d-ef07-3401-8947-8640e6b57bbc | -9.41555 | -47.58194 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a0d03b33-ba3e-3b9e-b651-8cbd3f5518b7 | -10.16871 | -45.45638 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b467f36-50e0-39db-b932-016b9da29e61 | -9.40804 | -47.57145 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d86b49a5-0a1d-378a-8454-61583c2c302d | -10.26436 | -50.31219 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f8f7308f-aba7-3f2c-b155-a3d36f632111 | -9.32542 | -45.67297 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 110974cb-0e95-3119-821c-59bcb27a8009 | -6.32281 | -43.03572 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 11e49d6f-9a82-342e-b91b-5f2b5843d38c | -6.69346 | -42.81135 | 2025-10-02 05:55:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a424405c-8430-3da8-961c-c07ef5602acc | -6.72578 | -44.13937 | 2025-10-02 05:55:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| cf0e1303-c5c1-3c6c-9438-503d7a9ea850 | -9.93502 | -43.76247 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| a7019b3b-46ec-3252-8720-146c78a7f3fb | -7.77543 | -42.53359 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| b51fea9c-c01a-3980-ad19-557fac7892cb | -10.70424 | -48.5776 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 716a80b6-2429-3a19-a5cb-c823859d5152 | -12.79729 | -46.85643 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b2a4c4b8-14f3-36fe-b386-66afcccbef0e | -13.78003 | -48.00046 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c15665a-e163-3b2f-ac03-1fc925c030a8 | -13.16218 | -47.81331 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 51233367-e83a-31c1-91e6-8d80b74c2a52 | -12.89926 | -47.16882 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 730b4597-bec6-3dc6-a8b7-c3079967604e | -14.58865 | -48.33315 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| feda6379-cfb3-3a7b-bb75-cbe38966af4e | -13.31013 | -47.19262 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 50a4746f-2e0c-3369-9bfd-25eddffea80d | -14.30715 | -45.99647 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8ff4cf09-a681-348b-8c14-2daff34b0f1f | -15.25832 | -49.31269 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d4bc4fca-5d77-3120-b162-eb0e76f6ded7 | -12.95233 | -46.36769 | 2025-10-02 05:57:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 03f7ed31-23e5-36d5-ba82-0942a5454b1c | -17.94419 | -46.80501 | 2025-10-02 05:57:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93e86177-0159-35fe-8c0f-878b955b40e9 | -12.5842 | -49.89242 | 2025-10-02 05:57:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a50abaf-c08f-31f6-9751-519302ad0518 | -15.31637 | -46.29306 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc822826-9259-359d-b967-dc2e5d6d07d7 | -14.46686 | -48.40186 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23efe2b2-0ec7-3b57-ab98-db03569c851c | -13.56488 | -47.27841 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e83bb444-d96e-367d-89bc-f96ec4559e80 | -13.45852 | -47.25537 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d8605ae-4ee8-36ad-bfe9-8999cb973bfe | -11.86564 | -45.01732 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8b84aa24-c860-3822-9796-646b6a8cceaf | -12.4761 | -47.26554 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ae3df019-99ee-3d78-b7a8-7e201aab2622 | -13.14472 | -47.85069 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a8d6ee3a-4851-337f-a2b1-069832e6b95b | -15.34735 | -46.26498 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 395ccbfd-e34a-3037-81c4-29335a25d8cd | -14.30991 | -45.97727 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 95d4b428-8f33-3e5a-82c1-e4e8025dce5a | -14.31466 | -45.87932 | 2025-10-02 05:57:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3f94179-51df-3801-a5cc-96d564ee4044 | -12.68427 | -48.56929 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7ba2782d-95ef-3c92-aefd-d254259b89b0 | -12.27555 | -45.37725 | 2025-10-02 05:57:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| df33a5e6-7d00-313e-a92e-0342a05662d2 | -13.17239 | -47.8056 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fa6c3fc6-4240-3f0c-acbc-52a338475fbe | -14.59116 | -46.70747 | 2025-10-02 05:57:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6b6d7843-9eae-3c4c-a4b5-e10c1300fe86 | -13.30316 | -46.9984 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d60b08fc-9453-367f-b60b-baf659bed507 | -13.75035 | -48.00756 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 584dccde-7319-3b02-85c3-7536d34a645c | -13.95033 | -48.09551 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9eb84117-15ec-33b3-a97c-111e1b172531 | -13.31676 | -47.81607 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ea3d6c45-f797-3b24-9550-8a22715f4590 | -16.01626 | -50.8616 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 490bb2cb-c3b8-3010-91f7-beada84085ce | -11.58655 | -47.65034 | 2025-10-02 05:57:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54b54a25-a87f-3d28-ab61-cdbe710e1543 | -11.26672 | -47.80524 | 2025-10-02 05:57:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 707ae420-341a-3d46-87eb-92d6b1a1c623 | -11.10768 | -51.0651 | 2025-10-02 05:57:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 0c72f0a2-fdc5-3bc8-a234-6fb35701e502 | -14.69829 | -48.21717 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb46ed40-e1e1-3ece-9839-8debafa10c14 | -15.25434 | -47.89905 | 2025-10-02 05:57:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 108f106e-265a-3c43-8cfb-fc05bc257321 | -11.79951 | -44.9708 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be1511bb-e625-3161-a8ec-076066743bd9 | -13.18394 | -47.78905 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8eb0c8d7-d7bf-31dd-93ab-fa31ccbce1dd | -12.94435 | -48.44066 | 2025-10-02 05:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c356f076-3432-39f6-b9a7-7261ac313cb8 | -12.90806 | -47.17017 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9aceabb5-3396-3a4d-a43e-d06ddd2f12f4 | -11.91295 | -47.87445 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 05619adf-b77c-3bf6-b4d2-20b5c94821c8 | -16.1377 | -46.67382 | 2025-10-02 05:57:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 14f368f0-31ee-3e49-9ab1-3df8a2f32235 | -12.70231 | -48.57188 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ff59ef54-f692-35dd-8eff-6552c23d82d3 | -15.99474 | -50.91001 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b5fef6e7-bcca-3cdc-bbcd-81de29593ea3 | -15.6055 | -46.9082 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0b7c767a-c849-339f-9c9e-f35eb0b32f6c | -13.52361 | -47.25367 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0d7159f-98ff-391e-9cd9-a79e5c350cb2 | -17.08556 | -48.55594 | 2025-10-02 05:57:00 | AQUA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 89aad410-1da5-3966-a32d-5d8bfaf6ba0f | -12.20267 | -47.78997 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0c4e04b-05b6-3b33-a6b0-73c24025a38f | -11.2714 | -47.83406 | 2025-10-02 05:57:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6557d18-ee7f-3d34-892c-eb285dc5e4af | -14.89312 | -48.09265 | 2025-10-02 05:57:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9028872-61c3-3624-b192-344beb008000 | -13.00715 | -45.22198 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7fe91fdd-94c2-362b-9b1b-7eecee05b67b | -15.31778 | -46.28335 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 17097959-58b3-3bfa-9167-9c90132bea1c | -14.08333 | -46.65575 | 2025-10-02 05:57:00 | AQUA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e12839f-36c5-385d-b1b4-0fc6165baaa3 | -14.90105 | -48.33622 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d930953d-a272-3198-afcb-40f994b18ad5 | -13.42244 | -47.79225 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| af018005-89e4-3fc8-88ce-cdde198128ee | -14.69271 | -48.25358 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28c72fbb-cd28-33a3-99ae-cc6fdf0c133e | -15.22354 | -50.11102 | 2025-10-02 05:57:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8a5b3949-a704-3cb9-855d-7f01b1a7bf5f | -13.4062 | -47.78049 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| adfd4884-6eee-39d4-a361-37db34374303 | -15.9972 | -50.91609 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2d4f00d3-b3e1-319f-a29e-66e1845373a7 | -14.47147 | -48.43081 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3773dbf8-4a26-3f79-83bd-e1a79567f832 | -14.31623 | -45.99781 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 394951e8-540a-33f8-b396-a70c4693a61d | -11.81942 | -45.01059 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 93d1b1ea-2d72-37df-8707-4aade59882a9 | -17.18472 | -47.02406 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f5431424-a8c0-35fc-8166-c497c3b79e6e | -14.47289 | -48.42161 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| e1211ea4-2f1d-3da4-a96c-b8c44aaf2074 | -14.90245 | -48.32709 | 2025-10-02 05:57:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b3d2e70b-1821-3830-bb6c-b2aaeb25b21f | -13.21299 | -48.49301 | 2025-10-02 05:57:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dc282bcc-6ca6-3039-9625-73a409cb705c | -13.16356 | -47.80431 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7309838d-8c7d-3a55-8dd0-4da047ecc017 | -14.69968 | -48.20808 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2d9f6e4c-3ac8-351a-b5d2-0c6da64dbbb1 | -14.5812 | -48.32264 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9e999b2a-d4a2-3656-b593-9c936abfd72d | -11.86423 | -45.02717 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d502a251-a7d9-38f4-ad6e-1d826dbf6dc6 | -12.85446 | -47.02782 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea5a06d4-5a33-344c-9895-74261ba86c78 | -11.19858 | -47.76941 | 2025-10-02 05:57:00 | AQUA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52a5f806-7f52-3263-9622-289194225024 | -15.54622 | -48.17441 | 2025-10-02 05:57:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e4921089-b3c2-323f-94c6-0c108a97ccf3 | -14.2067 | -46.12135 | 2025-10-02 05:57:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e33be0d2-8f71-3eb8-92a2-d41cf11cc77c | -16.36501 | -47.07405 | 2025-10-02 05:57:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 10fc25ce-19d5-3a34-9b81-8e5347cef6dc | -13.28314 | -47.25269 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6d8d0716-ef89-3482-854f-159b1a0da6bc | -13.96384 | -48.12538 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c0ba63f2-958e-350b-91f5-74c593748f3e | -14.89222 | -48.33484 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0799eff2-f5d7-30bd-8beb-619e58bfdb14 | -13.32638 | -47.20428 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d95affe-0ad7-3764-8719-25cd6c25d54d | -13.21265 | -48.43597 | 2025-10-02 05:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 458dc2ce-3f75-35eb-a895-fe08f4aaef61 | -13.22092 | -47.34742 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c0abc64d-d9cf-33d1-a444-3152bec1e1c5 | -13.56623 | -47.2694 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8d13d92-be94-329a-aef6-3f723d4d9ee7 | -11.82712 | -48.07654 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fa46ffc7-fb5c-3e89-9947-72408c93b7ba | -14.48319 | -48.41374 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README140.md)
