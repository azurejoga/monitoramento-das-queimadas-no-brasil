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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33be0166-235d-3560-a5e7-7cc6fbf2dfe9 | -13.33828 | -54.38512 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 029dbf48-1de5-314d-bbc8-541914dfb4a3 | -12.36111 | -47.4254 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2b97740-0afe-3603-b7cf-b6bbe55526d5 | -12.7761 | -44.46008 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 195ba479-d9c1-39b4-ba79-372758df3514 | -12.79628 | -44.45878 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc310926-44e6-38fe-912f-e9360d704867 | -13.33124 | -54.38336 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f33c7e4-0c82-3ec6-9941-8554d0e97151 | -13.2942 | -44.61607 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86f69161-eacc-3664-9c09-656438f4c4bf | -17.53358 | -54.01424 | 2026-07-08 04:08:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 313fe2da-a35a-35d7-8fa1-9fae826c9c05 | -12.45369 | -49.58666 | 2026-07-08 04:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32c463b4-5132-3dc5-a222-ec6bd6839cb8 | -12.78084 | -44.45587 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 3015104a-87c5-338d-950e-b684d8a6469b | -13.53883 | -52.93666 | 2026-07-08 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37ef8d26-bd29-3d6f-9a0c-e5a59d8c60db | -13.28793 | -54.41079 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 018eed24-3f13-3f79-95ef-0d9a1eac28ba | -19.67526 | -43.13838 | 2026-07-08 04:08:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c1d463c4-b549-37cd-81c9-2dd0fea3754d | -11.96589 | -46.95212 | 2026-07-08 04:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bb74596-61a0-3dc2-b3dd-06c4f5b0874d | -13.27634 | -45.17879 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecdbbb47-417d-32dd-9060-2c67fc1b85d3 | -13.29333 | -54.41996 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 943ca841-1c42-3395-83fb-3e103c6319bc | -17.28041 | -50.01961 | 2026-07-08 04:08:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b91e33-e18e-34ac-b418-f530d41ea032 | -14.60451 | -52.06736 | 2026-07-08 04:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01aef8d3-6ab9-3968-b549-aa2e257ed72d | -12.78119 | -44.47628 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cde1161-04c7-361e-9687-a5e027331b93 | -15.16748 | -43.82528 | 2026-07-08 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60ac210f-b1fb-39d5-b8b6-c45b51f29091 | -12.35028 | -47.42653 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b095ad7e-0364-3095-b3a7-cd09a96438c8 | -13.27359 | -45.17091 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8e91d8c-0e40-374f-a8b2-038bed7e8241 | -13.53762 | -49.30704 | 2026-07-08 04:08:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15915dc1-df11-31ca-8c9f-67e1eaf171e6 | -20.0718 | -41.30653 | 2026-07-08 04:08:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6a412ee4-b58d-351e-9b62-04bc7809b693 | -14.48763 | -46.72958 | 2026-07-08 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a22146f6-4808-3c6f-ab1a-768ade18f5c2 | -12.84772 | -44.39248 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e60c6ac5-5087-3800-991b-b7255ed54bb7 | -12.36207 | -47.42033 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 002a5055-805e-339d-9c64-75f70262a5d6 | -13.82471 | -44.055 | 2026-07-08 04:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0702db1-db35-3962-a8fb-a000bdb2864a | -13.28373 | -45.18382 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc860daa-881a-3cd3-ac89-7b99cedcba0e | -12.74501 | -44.45266 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c7dcae9c-4253-3212-9366-d2b4e6378d86 | -11.64466 | -46.36385 | 2026-07-08 04:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b19da5e-4fe8-3f88-a8c7-7004b0e32932 | -12.63498 | -44.64699 | 2026-07-08 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b7cf402-0198-3735-9b0f-fde8360b242d | -13.29049 | -54.41927 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b97b01f-e87c-35bc-bd8a-d4602988b923 | -13.33991 | -54.37775 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0e3ede3-30ca-32c8-b593-8278bcd72aa4 | -15.16387 | -43.82461 | 2026-07-08 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f78ed5ca-18b7-3fb0-93bc-b17f1808bcdd | -12.50085 | -48.25681 | 2026-07-08 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 316b2b87-634d-3efc-81d7-ef58b0395ca7 | -16.65965 | -47.53032 | 2026-07-08 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5d475eb-ba76-3fe3-a1dd-99528894a7bd | -12.35591 | -47.42241 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4eba8f7-e31a-3739-9912-61bbff5aff60 | -13.47354 | -49.9154 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c77ccdd0-4309-31e4-b9bc-086ff7473f17 | -13.28161 | -45.17236 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f3d2c2d-e692-3b92-a04c-8449544f882e | -17.54135 | -54.00989 | 2026-07-08 04:08:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08171b06-37b8-3054-ac59-3bb04580b804 | -14.14029 | -52.88787 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 010cbfc6-42fe-3d6a-9e93-baa8e96c244b | -13.2831 | -45.18742 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2a233a2-3f80-3ffd-8225-4249c716f5c6 | -13.44139 | -43.8547 | 2026-07-08 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a933135-54c8-3d70-b7f6-87950b05746d | -14.72989 | -47.14928 | 2026-07-08 04:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c85c1878-4c84-37ee-aaab-c8871fe85300 | -14.73432 | -47.15018 | 2026-07-08 04:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fcff5ce-aebd-33ed-80e1-64031ad4a7f0 | -13.27422 | -45.16732 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf76ff6b-df20-3fca-99d5-7ea52d092b98 | -12.77996 | -44.46078 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 265b01ef-2110-3fd9-9270-8906f1e6f355 | -15.76878 | -43.23688 | 2026-07-08 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9494538f-c4fe-343c-a045-41f349715838 | -12.78506 | -44.47699 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d4fb840-3313-3d9e-8a14-6eae360ee2a7 | -12.74888 | -44.45337 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 237b87bc-004b-394c-bc69-4bcbc418b3e5 | -12.75507 | -44.53288 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cef769a-2fb4-357c-838b-9bb31873c615 | -12.13462 | -48.26218 | 2026-07-08 04:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c30840b9-39e8-3854-9f3c-8cf801fbf098 | -17.27912 | -50.02584 | 2026-07-08 04:08:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb933b72-1e7f-37ba-9d79-358420205ec5 | -19.09442 | -40.08503 | 2026-07-08 04:08:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| afcb9339-024c-3e48-b589-cfa64303bc8e | -13.27823 | -45.16805 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28484329-6bd9-3912-84bb-7db14197847c | -12.35121 | -47.42145 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1850c82-6cd2-3a73-8e8d-ad2d63741258 | -13.32812 | -54.3827 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6544199d-a242-38ad-802b-13fe2c8ea07b | -18.37101 | -39.95746 | 2026-07-08 04:08:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d76c5d92-b089-32c7-aecd-040e70851743 | -13.95269 | -45.2239 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae98dd74-937b-3ff9-9c78-baae413ae171 | -13.47934 | -49.91546 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8637fa05-5de3-38b4-983b-452481aee010 | -13.95554 | -45.20816 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 948d5556-d042-37c3-b7d7-e85eb8604fd7 | -16.65933 | -47.52819 | 2026-07-08 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94b6dbea-e234-3a2a-992a-7cc381ea863d | -12.64373 | -44.6401 | 2026-07-08 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb496c9d-08e3-39a5-a514-8cd59c52cc4f | -14.14088 | -52.88787 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a254be59-d853-399e-8c50-4296cc903eee | -13.28957 | -54.40341 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 878bbec8-1a6d-3e32-80d1-8c3e6b78e2dd | -13.28035 | -45.1795 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a364a039-120b-34b2-b16c-d32770764cc6 | -13.53644 | -52.9478 | 2026-07-08 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb189000-d9fb-30c7-aa51-ea9d1ff5a9a6 | -13.47896 | -49.91661 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92dd3300-14e5-3e27-8c20-c4941f4dc962 | -12.7847 | -44.45659 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 9e3484e7-35ce-3f8b-b89a-ee254b764b98 | -13.28775 | -45.18455 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 785aeea3-624c-36a6-8868-3434dd51f551 | -12.79242 | -44.45805 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7d28a2f4-a528-30d9-b0d3-8e03b961492b | -14.80872 | -43.56398 | 2026-07-08 04:08:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13f6f0ed-a87f-3958-aa3f-239163e91185 | -13.14974 | -44.95547 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf2a2c7c-f434-38ea-aa1b-7f649adabf8a | -14.52466 | -41.11028 | 2026-07-08 04:08:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c3bd8688-f3c5-3367-9df4-ce7bc0f48c02 | -13.52179 | -43.992 | 2026-07-08 04:08:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aacd89c1-25fe-32ad-a308-a2736ab2f277 | -13.28436 | -45.18024 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43b4f24f-2193-3af3-83e6-a67e1c14c5b5 | -15.1631 | -43.8261 | 2026-07-08 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 677ae7f1-92c4-37ec-b6b2-2c24f989800e | -12.76316 | -44.53277 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a90ad220-646e-36e3-be73-4408e1883401 | -14.59838 | -52.06626 | 2026-07-08 04:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6605a4da-4c42-3788-aad6-047ac3fa48bd | -19.08764 | -40.08391 | 2026-07-08 04:08:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b421cebb-1523-3dac-b571-8444f13d1458 | -12.75189 | -44.459 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c4c11d25-1a71-35ca-ad0e-dd46100932cf | -13.29457 | -44.6181 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 995fc85a-0fa9-34a8-8deb-b97b1fff5896 | -12.75984 | -44.52865 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 381c6963-753a-3f17-a5d5-8a80de9f4b59 | -13.52987 | -52.9466 | 2026-07-08 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1961f5dc-4f20-33b5-989a-1a3944fdfdef | -12.77594 | -44.45835 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 96dbf464-544d-34b3-83c2-01976c055230 | -19.09103 | -40.08447 | 2026-07-08 04:08:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 58d726fb-56a6-3990-b934-c4b495cadc3b | -13.28562 | -45.17309 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca83f46-549b-3285-b179-c69fd65ce338 | -13.47825 | -49.92022 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 206acfb4-3961-3a48-92e2-ad555106e674 | -13.47966 | -49.913 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12fae321-d8d5-307a-8898-1a0d66000e7f | -14.14145 | -52.88257 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b3834bd8-d275-3ea2-bfb2-5a5fd5b4dbe3 | -13.44217 | -43.85023 | 2026-07-08 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fec65a62-900f-3c68-b65a-4677e6222f96 | -12.12963 | -48.26114 | 2026-07-08 04:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37778f72-137b-35f1-98ee-d7ae9aeb9edc | -13.27697 | -45.17521 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 476e7ec0-7da4-3cb3-86e5-0d2f2c6f1dd1 | -11.66357 | -46.37566 | 2026-07-08 04:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8294cc4-9919-3b86-bbd9-3fb68a3a8910 | -14.73074 | -47.14477 | 2026-07-08 04:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 887c8b8f-5bdf-3f96-8993-5b289aad0499 | -13.32655 | -54.39 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a8daacd-60e5-3614-a8a7-186c89356c2c | -15.81006 | -41.89906 | 2026-07-08 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1cedd85-0351-31d1-a915-b95076b570e7 | -12.35737 | -47.41937 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe7fd82c-4760-33f3-b14f-dfad8531d866 | -18.7426 | -46.91472 | 2026-07-08 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b651a933-f3e8-3681-bb1e-d23d5a7fc822 | -13.27793 | -54.40851 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
