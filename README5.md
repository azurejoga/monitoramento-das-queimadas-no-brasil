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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9309b2e4-3ccb-3728-bd99-52772a7c797a | -13.05272 | -53.71735 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94fedb06-df83-38fd-9cff-45a5fdb07354 | -21.24055 | -44.16551 | 2025-05-16 04:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5a7e93e-10bc-3891-b031-aced43074f96 | -12.29474 | -52.47277 | 2025-05-16 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72cb2f4e-aa1c-3025-8b00-0a30320f2eec | -13.59052 | -47.38069 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2dcf447-7e59-3b50-8abb-8b2e94bd2db6 | -13.59895 | -47.3772 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976b73dd-f89f-3072-be8b-65527dd1603d | -13.03987 | -53.71804 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f1edf37-c932-36fc-9e8c-644ddc58ca6d | -20.41852 | -43.55355 | 2025-05-16 04:10:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e83a99b-aa70-33e3-b078-873d553f283c | -19.15871 | -47.81776 | 2025-05-16 04:10:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca86511f-6c08-3b05-916d-bd36ccce2035 | -13.39194 | -48.44867 | 2025-05-16 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03504c4e-df8f-3867-b91c-2b9e783afbbf | -19.06665 | -53.45717 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27fd0529-fae0-36e8-84ea-2b2538aa236a | -13.95908 | -56.79401 | 2025-05-16 04:10:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4baf8d7-4a61-31eb-bdb8-42ae258c0af4 | -13.2797 | -45.41668 | 2025-05-16 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d529819d-5373-3df1-bb14-4f8d1ca9324c | -17.2528 | -48.11289 | 2025-05-16 04:10:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90d5fbc5-0269-381c-82c1-b148657f2d9c | -19.26068 | -48.7292 | 2025-05-16 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82d317ea-583b-33af-8761-85e6366c6acc | -14.01322 | -55.14238 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ce2a039-f343-35a2-9de3-ace7b623cd86 | -14.18441 | -45.47649 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 186daf28-c6bc-3023-81bf-8c7820af9827 | -19.06325 | -53.45694 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5639a064-a687-34f3-8e83-785fc092510c | -16.681 | -43.88354 | 2025-05-16 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 907ce3a6-bcc3-394d-be72-0ef976c90eb0 | -14.87038 | -51.98173 | 2025-05-16 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 848c35b4-8c8b-3e2d-a5c8-3cc93cc356ec | -14.01526 | -55.13257 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 155ba55f-2bf9-3726-aeb3-b4eb66d69807 | -17.80096 | -44.35677 | 2025-05-16 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac387109-8569-31df-895a-c9fb6c947070 | -13.57179 | -52.86908 | 2025-05-16 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad697018-f9bf-3a22-973e-1f9df8e8a231 | -17.66566 | -46.68062 | 2025-05-16 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90fffbc1-8542-3916-9910-9d9e4bfe524d | -14.16723 | -45.47352 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df683250-d8dd-3674-b29d-be5a59f6198d | -17.05822 | -45.91882 | 2025-05-16 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b5839328-47c6-3993-9c1d-281a5e09dd37 | -17.05482 | -45.91821 | 2025-05-16 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2b40f9a-4d91-39db-8123-54885b72ada2 | -17.97237 | -45.24144 | 2025-05-16 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d7ffd34-5ee7-3cd0-9542-9b222ac1180a | -19.06392 | -53.4537 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca8e32f7-ca13-37a3-ab2a-6257505a171f | -19.43971 | -44.33924 | 2025-05-16 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb7d6416-6513-320b-b264-b802b7d11cda | -14.47217 | -56.325 | 2025-05-16 04:10:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a8932c8-eb15-371d-96c3-e3de7a711ce5 | -12.8714 | -55.05883 | 2025-05-16 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dc0e4a2-4bf1-383e-b320-eacd11ddaaba | -18.75694 | -47.61615 | 2025-05-16 04:10:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bc268e7-c491-3ac1-a969-c05e9269e583 | -19.05886 | -53.45261 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3fa6f6c-3d93-37c4-8623-d03576c5803c | -14.17131 | -45.47025 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9331e6ab-c57f-3cce-b460-b985ad77455e | -17.88538 | -43.99031 | 2025-05-16 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ab02ca7-0f8e-3852-9933-4a0348a453ce | -13.04701 | -53.71601 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93eb1bca-c13d-31d3-a767-e64694866ece | -19.06733 | -53.45396 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5e14d035-f91e-3151-a29b-b691fe191281 | -14.02558 | -55.14479 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee7333b0-bf57-36de-be04-3677c5653032 | -14.18034 | -45.47975 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6929bcd-e889-34a4-82af-013802a1baf0 | -13.67527 | -53.94295 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efe8f3a8-3b8e-3380-94b8-71d9fcbc7105 | -14.33178 | -47.50795 | 2025-05-16 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| faed45c1-9a34-3b5e-a022-d3645bad67f5 | -21.18051 | -43.97929 | 2025-05-16 04:10:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d52e337c-908d-372d-879c-59a50f8d26fa | -21.23723 | -44.16492 | 2025-05-16 04:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 859873d6-0a15-3055-8dfd-31b7d0a24b23 | -19.53135 | -43.92008 | 2025-05-16 04:10:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 674781b5-edad-3341-af85-0d7d11cb3a27 | -13.38787 | -48.44797 | 2025-05-16 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1bdb842-4115-3d8a-8e9b-d9b45d593c54 | -15.26735 | -51.4611 | 2025-05-16 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0dfdcdbb-0401-36d6-8333-101c10bba5f9 | -17.25388 | -48.11083 | 2025-05-16 04:10:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ab1b8a3-59a3-33a0-a464-1215e8001cf7 | -14.18314 | -45.4842 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7dd09dc-f1ba-35af-89bb-797976733b53 | -19.04869 | -45.38824 | 2025-05-16 04:10:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f1e544f-3ea5-3448-819d-fad677e7d7e6 | -14.16787 | -45.46965 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d94ab272-6e6b-30de-9e8b-6a333e28ab15 | -14.17195 | -45.4664 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f46639a-9f77-3421-a5ce-f5fc5d178e8f | -19.11494 | -52.71091 | 2025-05-16 04:10:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b1728c2-54cc-3aab-9b55-d0838e9b9c80 | -14.33556 | -47.50863 | 2025-05-16 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1eb4128f-174b-322f-9a35-b718a9fb6574 | -13.05212 | -53.71656 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fd4d642-38e4-35b4-8267-f253e0710a80 | -13.67684 | -47.96626 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98fd30dc-2201-309d-b64f-2346c0e1ed0c | -14.18098 | -45.47589 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9da8a22-4b32-35cd-831d-a3d76b9d4167 | -20.7654 | -46.77111 | 2025-05-16 04:10:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23b736bc-20d0-37d1-b066-2da8eaa9de31 | -13.67492 | -47.16311 | 2025-05-16 04:10:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7c668b5-824a-34bf-80ae-aea204243ed7 | -14.01725 | -55.12302 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 372de9b6-473e-391e-b289-fa4b5fece56e | -20.57975 | -44.57529 | 2025-05-16 04:10:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a888e5d-af0e-3216-afec-0487455d9440 | -13.04618 | -53.7201 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cfdc0cb-7809-3236-b6d5-294736f2b6e4 | -17.25302 | -48.11559 | 2025-05-16 04:10:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b823efef-487e-3741-915a-e635faeae2ff | -15.00301 | -48.81789 | 2025-05-16 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dc25483-a6e1-3b93-af50-bbb296bce1da | -17.59564 | -43.19912 | 2025-05-16 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 035c034c-1ef2-3774-9c42-0a977de86b6e | -17.061 | -45.92326 | 2025-05-16 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a2b73c9-7422-3f68-8f05-2140e1990a1c | -12.87461 | -55.05704 | 2025-05-16 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de850e8b-268b-336c-a4ee-31305a6b0075 | -13.67119 | -47.97554 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 141ad6d1-be51-3694-9da2-36e2520c1e81 | -14.17283 | -45.48243 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b4608f-7c8e-3122-b37e-ffd8fc12fec0 | -13.05189 | -53.72145 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b9ec42-0299-3603-ad2c-57917018a5dc | -13.0464 | -53.71523 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90ce197e-5555-34a7-8cbe-839bdda5bc8e | -14.47346 | -56.31908 | 2025-05-16 04:10:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ef54127-d742-37e9-aa06-d474b0dc8898 | -21.23666 | -44.16866 | 2025-05-16 04:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 00461af3-b448-3262-b52f-a3b4b76c5457 | -13.5711 | -52.87254 | 2025-05-16 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c955c7c2-4d5b-381f-9dff-2e07c59ae58e | -14.17754 | -45.4753 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebd2fa8d-a213-3b1b-9e3f-2d913fb5bdc7 | -13.67635 | -47.96818 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d077220-d075-3b01-9d90-fb4c4f68bdb7 | -14.17538 | -45.467 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72c6a241-741a-32c1-a172-58746dd4ed18 | -11.91836 | -54.40899 | 2025-05-16 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5aa18e90-2f63-3e01-884a-789021272a19 | -14.01941 | -55.14353 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de1896c8-89e1-3143-b1dd-b475492a0297 | -19.0582 | -53.45582 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5151b39f-e77e-3f76-b0a3-56e345db24de | -16.93967 | -53.45071 | 2025-05-16 04:10:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31a7b147-8909-3b34-bbf1-2dea6b373051 | -13.9577 | -56.80037 | 2025-05-16 04:10:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fbb490e-f332-34bb-a68f-06dba74c136b | -13.0456 | -53.71932 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f99fb165-fb75-3a81-b9e2-d77ab8164020 | -14.87536 | -51.98275 | 2025-05-16 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd58311c-1a76-3b45-bfaa-f6b29b7e86c9 | -12.87359 | -55.06209 | 2025-05-16 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fe9d109-e02c-3b1a-a135-d5b365463f57 | -22.6994 | -43.34805 | 2025-05-16 04:12:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e206096-26a9-3e80-9a0a-fb9ad900b3c1 | -23.07681 | -50.3451 | 2025-05-16 04:12:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 518d5227-1468-3b06-9aa9-6ef878df8d5a | -20.18991 | -55.03974 | 2025-05-16 04:12:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9cc952b-5098-3f97-980d-8b56477f292e | -22.0432 | -56.64848 | 2025-05-16 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64e6a7bc-ad95-38fa-96fa-ac1d54006787 | -20.45328 | -50.0106 | 2025-05-16 04:12:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1ec7f60-969d-3b26-9836-b71073cc0deb | -23.52156 | -46.9752 | 2025-05-16 04:12:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99f56ecb-f03d-3599-afd6-0fd628fa7d1b | -22.78762 | -43.75652 | 2025-05-16 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2bf790f4-f669-3b45-bd95-5cf21845cece | -23.29164 | -51.59578 | 2025-05-16 04:12:00 | NOAA-21 | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46081c62-20d3-3bb1-81d7-8700a60f79d8 | -23.29081 | -51.59998 | 2025-05-16 04:12:00 | NOAA-21 | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5939f6e9-54ec-3649-b52b-ed7936104add | -22.91905 | -47.17105 | 2025-05-16 04:12:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 385e798d-0118-3910-8168-77a5f7ccb5e8 | -23.63163 | -46.42808 | 2025-05-16 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e9d78b0-5f1a-3395-ab8c-53a4651cffc6 | -25.19164 | -49.32816 | 2025-05-16 04:12:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b63cd6ab-7756-3017-b5f7-614b3108be9f | -20.18905 | -55.04362 | 2025-05-16 04:12:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6801581-0f7d-3030-80a3-42644f84e162 | -23.07564 | -50.34755 | 2025-05-16 04:12:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 424ebac7-d594-3f45-842d-3ac5b5f1c921 | -20.99722 | -51.7943 | 2025-05-16 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b630fb24-1678-3e3d-8335-cd224aedf17a | -20.47849 | -53.6756 | 2025-05-16 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
