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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecec08a9-e86b-3b23-a28c-466048c40857 | -11.96362 | -44.21281 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad861974-25c2-3f92-aa90-d01e19a1793b | -11.75348 | -44.59662 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8cfe75db-6e3d-34a9-bb6c-2b3e0b8ba40a | -8.53635 | -35.75198 | 2025-12-29 03:42:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c36b143-e52b-3d46-9b99-0fc8eff656cd | -11.54237 | -46.30312 | 2025-12-29 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf7425f4-6882-306f-9356-a4ffbd264643 | -11.75417 | -44.59305 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 249e80c3-ca4c-3071-830c-b3a46604fa1b | -11.96427 | -44.20945 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4cf8fa0-b05c-3b37-8753-72155ddc76cc | -11.96791 | -44.16186 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0c35692-0707-3f85-9953-a36c47c56183 | -8.53697 | -35.7482 | 2025-12-29 03:42:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f48e2574-72ab-37fb-bac0-c9390b21fd00 | -12.21099 | -38.98168 | 2025-12-29 03:42:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c05ea594-a3cf-3650-a85a-036d635f7f95 | -11.54144 | -46.30779 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6e6b5c1-b84c-3496-a7f3-19d1660219e4 | -11.75487 | -44.58948 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f10b7b14-0cee-38d2-9bd3-551380686d8d | -9.38231 | -36.90675 | 2025-12-29 03:42:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13602160-f005-3ac0-85a5-4e4ffb1eccf8 | -8.79643 | -36.95509 | 2025-12-29 03:42:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1135b928-fd67-3db8-8326-6a8c80898bfb | -11.54751 | -46.30909 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a659da68-39f3-36e4-84fa-6cbd2e74c8e6 | -10.62093 | -37.12651 | 2025-12-29 03:42:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 177aef83-0e9f-3c8d-9cf3-2443a31ea61e | -11.55355 | -46.3105 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b89e4b8-55a7-3478-bd9e-2c83d9316666 | -19.33764 | -40.90192 | 2025-12-29 03:44:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| bcca3af6-40dc-399a-a46c-09c0b7d3c614 | -17.61395 | -46.66454 | 2025-12-29 03:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ae19cab-eb6d-366b-945e-df483bcd36e8 | -13.7105 | -45.51555 | 2025-12-29 03:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f9f7a31-4cbd-393f-a226-da5e3fd9d433 | -13.47573 | -44.01561 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 09a79235-7aa9-3a42-9c60-4f4c5330044f | -19.33861 | -40.89642 | 2025-12-29 03:44:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 2c28e4c7-75ba-3125-9aa6-fbc52ee40901 | -15.84789 | -42.63224 | 2025-12-29 03:44:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4a557a4-0487-3e58-89d7-93af4cd2a197 | -13.47514 | -44.01863 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e78082a2-cfad-301e-bb2b-2d2e5169e838 | -15.96551 | -43.28009 | 2025-12-29 03:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 892bea0e-87b4-37c2-a419-805a741f5e59 | -20.50405 | -41.72011 | 2025-12-29 03:44:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ba9a600b-b03d-3c3e-b97f-52e5b532f22f | -14.15296 | -44.25741 | 2025-12-29 03:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1ff9b5e-c3a5-32b3-b8b1-e7e0a0f9afc9 | -20.18034 | -40.22028 | 2025-12-29 03:44:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7c0bd8d9-198a-3b91-b562-bd46e9160afe | -20.38897 | -40.56079 | 2025-12-29 03:44:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 90d0a31f-4994-3db0-9ef6-12f040850f6d | -15.13113 | -45.29194 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24fbda07-0adc-3276-a289-3d492ac5fbf7 | -15.1258 | -45.29073 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d74227ef-57e2-3939-a341-a25a6e56bdc3 | -15.96778 | -43.28278 | 2025-12-29 03:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 03eb2f88-fdf3-3c9c-86e1-2357da060148 | -13.47123 | -44.01166 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9e9497c3-f230-330a-8839-7e36da527169 | -20.93371 | -41.50811 | 2025-12-29 03:44:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 48320c18-0bcd-325a-aa99-07205fe3ddee | -19.33489 | -40.89535 | 2025-12-29 03:44:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 63ef7f02-f496-32cf-800c-0ee5e026d63b | -13.47632 | -44.01259 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b2e09d1b-47a3-39cd-8714-2b10c2db9ccd | -13.65538 | -43.72748 | 2025-12-29 03:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fd79dbc-a4c7-3e08-87bc-735597e18d2c | -13.47183 | -44.0086 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b0fd643-2ebd-35c8-a792-6a5a73b24b38 | -15.96459 | -43.28494 | 2025-12-29 03:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 50264953-9a46-32c2-8b12-44b03081aeac | -17.29119 | -41.82505 | 2025-12-29 03:44:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3d1192ac-2619-37d4-8a4d-3351b535002a | -19.4243 | -40.466 | 2025-12-29 03:44:00 | NPP-375D | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2384047c-1009-3cd9-bfea-a9cbfad10a1c | -13.47063 | -44.01469 | 2025-12-29 03:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8a9280e1-3818-31e9-bc09-f11797cfd493 | -13.70417 | -45.51813 | 2025-12-29 03:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46048db1-b5c0-3b7c-b532-13a8c055fad7 | -13.52641 | -43.51388 | 2025-12-29 03:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21b3944-8a59-33e4-b102-c7fe050c544d | -15.96318 | -43.28172 | 2025-12-29 03:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51dd4204-d66b-336c-b654-99d3353481db | -14.37347 | -47.36173 | 2025-12-29 03:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc20df01-7dc0-3c60-9e1a-3ddb860baa72 | -13.5215 | -43.51289 | 2025-12-29 03:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34caa902-1532-3328-989d-bb6117b464e6 | -15.13044 | -45.29542 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f49df92-4cba-3004-b68e-edaab50e14ed | -17.61477 | -46.66067 | 2025-12-29 03:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cd5ff54-12d9-3f53-bb0b-4fdf17969276 | -15.4918 | -39.001 | 2025-12-29 03:44:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4015107f-189b-3534-ac9c-bbf04bb2d9b5 | -14.37156 | -47.36203 | 2025-12-29 03:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3026fee-a46d-3e02-abc2-e1638930844d | -14.37058 | -47.36658 | 2025-12-29 03:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bfaec42-cdf7-337d-b285-f16d0ca51434 | -14.37772 | -47.36335 | 2025-12-29 03:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07a9338d-eb4a-392f-8edc-b4c8f7a72258 | -18.73745 | -48.02457 | 2025-12-29 03:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 44826b81-0311-3dae-97f8-85d3a2755305 | -12.66217 | -46.76607 | 2025-12-29 03:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4924bdf2-43f1-30ca-98fe-9df416d9b04e | -15.13718 | -45.28956 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 990d1454-a7fa-3961-b509-9e20f540c187 | -20.18111 | -40.21589 | 2025-12-29 03:44:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48ab9275-ae06-34f7-8e2f-0ba716d2f89d | -19.33393 | -40.90077 | 2025-12-29 03:44:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f9dd44af-7967-3534-bd52-a59219f60d44 | -16.98162 | -40.70592 | 2025-12-29 03:44:00 | NPP-375D | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1c9a6ea-38a3-37f7-b3c3-3a96229bf2d3 | -20.39265 | -40.56139 | 2025-12-29 03:44:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3e022c62-2295-341e-8cb7-30969cec33ab | -18.73644 | -48.02909 | 2025-12-29 03:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e492ea30-11d2-3fe0-b457-cd68fd0f2a36 | -14.37253 | -47.36625 | 2025-12-29 03:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d507980b-0c43-3eb2-9ebb-0d0d0501a81d | -20.16224 | -40.95089 | 2025-12-29 03:44:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c77b08c-2954-317c-b6bd-a95c30939d0a | -19.33578 | -40.89035 | 2025-12-29 03:44:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fec3636f-5ceb-3bc4-9b2f-0c593672b32d | -17.29604 | -41.82194 | 2025-12-29 03:44:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 559e9fc4-a2f8-34b8-be1e-4ffe74aa9465 | -20.50458 | -41.71872 | 2025-12-29 03:44:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43cee8a0-8a2d-35d8-8746-dbe470cd1f5c | -19.42252 | -40.46732 | 2025-12-29 03:44:00 | NPP-375D | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b689a661-7b77-3100-8724-2e28e5da73a5 | -12.6683 | -46.76733 | 2025-12-29 03:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea741a9-0884-3bfa-a1ef-2bd1a8863ea2 | -18.73055 | -48.02768 | 2025-12-29 03:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a41a0fd2-7f24-34db-9fd0-18d60f47b60f | -20.21151 | -40.21289 | 2025-12-29 03:44:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 533bdc24-10df-33ab-b1a5-557e78e7be3e | -17.29531 | -41.82584 | 2025-12-29 03:44:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3835693a-edb4-3b81-be02-b4dfa9917835 | -20.50497 | -41.71523 | 2025-12-29 03:44:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c05df4d0-4759-340f-8887-469829e6ee17 | -15.13356 | -45.29219 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c6fdf96-7887-3934-be86-8d5735dc3470 | -20.38978 | -40.56226 | 2025-12-29 03:44:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| a06cbd64-e0b8-3c39-ac37-e3a37adbc881 | -13.70494 | -45.51435 | 2025-12-29 03:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 865103e5-3031-376d-91a7-6c1044bd8065 | -15.13182 | -45.28847 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9def1798-a966-3681-a7fd-9eef63eaee25 | -15.13428 | -45.28873 | 2025-12-29 03:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de082791-019c-3ecd-8e24-386222cdfe2e | -17.60923 | -46.65937 | 2025-12-29 03:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21079d72-296d-3c0c-9e9f-c80f8f6c1dde | -22.52055 | -44.31252 | 2025-12-29 03:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39840563-3a35-3084-af76-ac682800c485 | -23.0367 | -45.32576 | 2025-12-29 03:46:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5be6e240-3939-3745-83a8-14b5bb844cf8 | -23.0357 | -45.33056 | 2025-12-29 03:46:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b731b802-f6b4-328a-af70-0159790cb48d | -22.02901 | -42.30994 | 2025-12-29 03:46:00 | NPP-375D | MACUCO | RIO DE JANEIRO | Brasil | 3302452 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 479fdf56-dcb0-3370-9a36-ae8a4bd6fa0e | -22.524 | -44.31799 | 2025-12-29 03:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ef2716f3-c0f5-38fc-b8b7-b575902a7311 | -22.52492 | -44.3135 | 2025-12-29 03:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c3778d15-08b6-3199-8479-1c089d151545 | -22.05521 | -44.4341 | 2025-12-29 03:46:00 | NPP-375D | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2dd822d3-85e6-376d-9009-0fd99db731bb | -2.86295 | -40.18462 | 2025-12-29 03:59:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c084673-b715-356f-833e-26aa517a91bf | -3.91284 | -40.88445 | 2025-12-29 04:01:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 75e14853-be62-3dde-853b-f86e908a588e | -7.0669 | -47.3972 | 2025-12-29 04:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ac93f1-9361-339d-9de1-6d4b4a8cc75d | -8.81038 | -38.93712 | 2025-12-29 04:01:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 51d73b2b-d85f-34af-a72c-eb1d438e78dc | -6.00086 | -43.44842 | 2025-12-29 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1a33185-6551-3884-99f5-918d85bb6e04 | -2.44985 | -47.79797 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a2e9e30-a864-3b85-b2ee-e74719240355 | -7.01221 | -40.28434 | 2025-12-29 04:01:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 87665b15-5bf2-3d72-9b73-c29cb9fd3e47 | -8.54012 | -35.74763 | 2025-12-29 04:01:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2f3988ef-3454-3ee6-9f6c-3331d7565925 | -3.21342 | -43.45464 | 2025-12-29 04:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6b8b4aa-77b6-3708-adf2-786ca322058b | -5.85726 | -40.34873 | 2025-12-29 04:01:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3eb117a-c84b-32a7-bde6-4d50c16c0e88 | -5.61588 | -40.62701 | 2025-12-29 04:01:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 59af0dc3-39d2-39dc-a9d0-1ecc90455169 | -2.45239 | -47.78224 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3e2be56-c01a-3d33-9742-5afe6bd0235c | -6.51815 | -41.27599 | 2025-12-29 04:01:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15b99931-a147-37d6-95ce-10a2b5203c39 | -10.77036 | -37.14085 | 2025-12-29 04:01:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d5b1dc3d-3748-3367-a0ee-189c9d83ed07 | -5.99739 | -43.45035 | 2025-12-29 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7864dd7-307d-30df-9b18-6636869819d2 | -5.24713 | -38.22105 | 2025-12-29 04:01:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
