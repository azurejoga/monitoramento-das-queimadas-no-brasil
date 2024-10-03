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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c023c6c-6680-318d-9da3-e6fccee5cb50 | -13.1908 | -48.63299 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 507cf595-03e9-3dfe-a0bd-abf0d9401354 | -13.19034 | -48.65245 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ddf1857d-61c6-3488-86eb-e04c38bd5994 | -13.19033 | -48.62222 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6642f94-f045-365a-aed5-1bf39e09d993 | -13.1898 | -48.62605 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79400cc0-7cba-312a-a7a1-104fe04dfce2 | -13.18967 | -48.60948 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c430f08-8dc9-3b8f-b291-ff4dc07f441f | -13.18926 | -48.62986 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e849f90-f29d-3017-8326-db1dad91731f | -13.18837 | -48.65135 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23b3d2d4-f3ef-3c50-9a1a-21afdaafc5ce | -13.18833 | -48.60618 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801b7dd7-0716-3fb9-b927-3352cd4c288b | -13.1867 | -48.64831 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0808caf6-76ee-3c85-931b-a0b0a1a94283 | -13.1862 | -48.6519 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bcf182eb-2619-3d07-b165-235aed608d02 | -13.18422 | -48.6508 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2e8d0c3-e295-31d0-9a28-0c57d6dbd41a | -13.18419 | -48.6055 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49ab239e-8600-3ca7-89b7-5b977c2031bd | -13.18374 | -48.65442 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dde31b3-6550-3873-9960-6837c351159c | -13.18365 | -48.60944 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 646becd4-b88c-3f74-bdd2-99699582ca42 | -13.18205 | -48.65136 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb1f0b03-15bc-38f7-983a-efe7941d12b7 | -12.4938 | -48.60635 | 2024-10-03 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41840de4-c653-370b-ab4d-934f91bb52d2 | -12.49329 | -48.61007 | 2024-10-03 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7252d800-b4dd-3317-b0b3-0facc4253874 | -13.75583 | -48.31925 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c78d448-1f1e-377b-819d-f33d7d3424b2 | -13.75158 | -48.31854 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c1afa99-a8fd-34fe-904c-2e7a65da821f | -13.74682 | -48.32166 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 415860c6-4e3d-3447-894c-9d57c6ee76b1 | -13.7452 | -48.30148 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4a69f47-0977-3c35-b691-5c6e80b2668d | -13.72752 | -48.30363 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd1801f9-3a9c-3375-bfde-9d8fe8bb5ae0 | -13.72592 | -48.31555 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6e7a401-3ef7-3900-adc7-6826e2cb7b76 | -13.7388 | -48.31667 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e076087e-1b5b-3e6c-82e4-bbb0c1c63144 | -13.73452 | -48.31625 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cac4a370-79cf-37e8-84ee-a61323cc15b2 | -13.50573 | -48.61066 | 2024-10-03 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3e32508-6ac3-3cf8-b535-f7abf43dd6ca | -13.50519 | -48.61456 | 2024-10-03 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0b27eb9-79c0-3bfb-91cc-1d5f1412a566 | -13.50157 | -48.60997 | 2024-10-03 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc7f7e48-bda5-30ad-b106-90d214b9e5fe | -13.50104 | -48.61385 | 2024-10-03 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 485e9149-d847-32b2-85b0-9c14e59df79e | -13.49742 | -48.60931 | 2024-10-03 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ed949f-77ce-396d-b323-a9f86ad4465d | -13.22967 | -48.62666 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc695e7f-ce2a-328c-9729-8c1e6e34f5cf | -13.225 | -48.62995 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5b5b060-e353-3f7c-897a-8ab60ad38b59 | -13.2245 | -48.63364 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0c08122-8fea-3efe-a3a1-cf1ff9d6b9da | -13.21984 | -48.63692 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f370522-001d-375f-b441-a54f0f1a67ab | -13.21935 | -48.64056 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48c89458-c1b8-3eb9-b68a-264ba5821a7c | -13.21519 | -48.64007 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491f0f49-51de-3be8-8ece-e5d500a60eda | -13.21471 | -48.64366 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f98e465-3168-3610-9440-107863bc376a | -13.21056 | -48.64316 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3267194-2c53-3463-8d39-ab3e1a239bc5 | -13.20592 | -48.64629 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9233651b-c830-39f7-bac9-cca4a8b7f87f | -13.2058 | -48.51918 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b810987f-f174-363c-83bf-5e8d6a3eb5ba | -13.20452 | -48.52011 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15a0ccec-4404-3712-81aa-f5c8d775e6d5 | -13.20225 | -48.64211 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e98e12e-6344-32c3-a824-1fd77213fce5 | -13.20177 | -48.64579 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7d9df48-632f-3f69-a698-13e78b5cc13d | -13.20161 | -48.51869 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 744256a3-f68b-3ad5-8c4a-979eec5c5101 | -13.20091 | -48.51541 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9651118c-0563-3e50-b80b-fa636de3f943 | -13.26542 | -48.58157 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e828b6e1-fc4e-3235-9165-9b90700bfc21 | -13.26492 | -48.58526 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95306860-7f62-3e13-afe8-302ced566c9b | -13.26126 | -48.58096 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cb29f17-9451-3960-ae4e-abe72063d352 | -13.26076 | -48.58464 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6da52109-a591-367e-b84e-1bf5c5adddeb | -13.26026 | -48.58836 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a0519a6-c7ce-36d5-9c15-f5c7a2ac94ea | -13.2561 | -48.58772 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e6f2c30-d9e2-3f11-bcdb-a99d2cfb5983 | -13.25144 | -48.59086 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a96a1fa-55a8-3e69-8890-945295a19118 | -13.24728 | -48.59029 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40704fc8-02fc-3a96-8785-a6b1695eb802 | -13.24677 | -48.59402 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a44e30fd-1ea9-3c97-809c-ce27303ba89e | -13.24211 | -48.59716 | 2024-10-03 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c94ce17-af6f-3436-9f07-6eb30f9c55d6 | -13.75107 | -48.3223 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72f6ce48-0d6a-3f77-b44a-b3a043366622 | -13.73022 | -48.31588 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6fb92cc-63ba-32b5-96fb-d290c01476ed | -13.72698 | -48.30764 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5028ab0-49f2-3f80-8da3-272a4ba67e41 | -13.72163 | -48.31521 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 881752df-347c-31c2-9cd7-435d6acfc5bd | -15.07879 | -48.9441 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a3faf1-aed7-35b7-9662-e2c4f004d39a | -15.07816 | -48.94378 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 827c5833-634f-376a-a790-34ab2d6895c7 | -14.82863 | -48.76888 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91502391-479e-3991-84d8-82792c102e6e | -14.82809 | -48.77297 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fb98f37-3f8c-376e-a9d8-d4dfdc6611b5 | -14.82547 | -48.76036 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f118923-164b-300f-803d-5199f431129b | -14.82492 | -48.76455 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a617f7e-167b-3ce6-851c-7257c3308107 | -14.82438 | -48.76865 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d8dba2-1c46-3fab-9611-e70aebcb4dd6 | -14.82384 | -48.77278 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 470436d8-974c-3270-8469-16c260636dbb | -14.82123 | -48.76001 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47d03450-560b-355f-a569-300d5424df1b | -14.81744 | -48.78898 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a56c31fb-a07a-3e99-98ab-3516f61c309b | -14.81321 | -48.78864 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6e92cc1-b7e9-3547-afbe-01e0ccff229d | -14.81266 | -48.79281 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ea001c5-aa01-30eb-a744-70938b1ac186 | -14.80849 | -48.79206 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94941d73-30bd-3cea-9ffb-a09927af5167 | -14.80799 | -48.79588 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af8beecd-0299-36e1-b3f1-b8e88184070b | -14.80432 | -48.7913 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 82b97c19-688c-3374-8685-9947abcad204 | -14.80383 | -48.79504 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d5b66ff5-5a09-3fab-bc2e-14bed40e90c8 | -14.79965 | -48.79436 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1fd44763-2db7-33a8-9377-b2d7bacef6be | -14.79917 | -48.79798 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c235a526-c26a-3c1d-8cd3-eb1a2bfabf74 | -14.79546 | -48.79373 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 111534c2-602a-31a5-b448-da3cbd1558d2 | -14.79499 | -48.79736 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55110cdc-e329-3ddc-b7e7-efab13a66c21 | -14.79079 | -48.79679 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b69baa3-d45b-3431-a2bb-7de93a23f8e9 | -14.7866 | -48.79618 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e78add9b-f9a3-3aa4-9c6a-22e0a600675e | -14.78246 | -48.79516 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c1f25ff-45e5-3288-bd83-335e3fe39536 | -14.78209 | -48.79565 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2e146fe-a92a-319b-a37a-4551ab8e96a0 | -14.76857 | -48.80092 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08247c87-e25e-329c-8726-dd7834d91729 | -14.71757 | -48.76691 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1357617-8d91-3ff3-b07f-b857ea2a1ae9 | -14.71335 | -48.76652 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24000832-a5bf-3ef5-9958-d9ff5202d55a | -14.71139 | -48.74881 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b18ab27b-53f2-3520-a916-66a747d55436 | -14.70962 | -48.76242 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf2e699e-c01d-33da-88d9-39f8844243b7 | -14.70911 | -48.76632 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c59fa95-2fc9-38ff-80b1-6fc0466ee7cf | -14.70714 | -48.74864 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f6e73ec-4006-3067-9426-e1541ed62dd0 | -14.70652 | -48.75337 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7737632d-a1ac-37ab-aa17-faed82ea39b1 | -14.70536 | -48.76233 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fffe7424-bfa5-3642-96c8-c82738f8161f | -14.70486 | -48.76616 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b654eb7-9837-30d6-b258-1ea0067d3efe | -14.70291 | -48.74828 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 338f6313-e2a8-36e9-badb-d581fd927bd6 | -14.70065 | -48.76561 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a386eef1-1a53-3e36-ae67-b21a0798fa67 | -14.70018 | -48.76927 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67cd8101-f7c7-361c-a449-a4ddf294c288 | -14.69987 | -48.73869 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fef3e2fd-043e-3ba2-bc02-daba47460cc4 | -14.69931 | -48.74301 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 213698ec-570a-3fca-bb5c-67a28b2e2f14 | -14.69872 | -48.74757 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ef83246-4c27-3619-810f-6a0897c326ce | -14.69809 | -48.75247 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README125.md)
