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
| dcd347cc-4dd7-3c82-aa92-d2968d18039f | -19.7041 | -56.8436 | 2026-01-26 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 163.7 |
| 94b74be2-10db-3dc3-a5a9-cc97f782390f | -19.7242 | -56.8408 | 2026-01-26 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 126.1 |
| e38ac9ab-e5f6-35c6-8293-d0d7dc5d25dd | -5.17829 | -35.85674 | 2026-01-26 03:36:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 91b8d4e7-35c7-3d95-8c84-0d13211983f6 | -3.26209 | -42.54984 | 2026-01-26 03:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a283ce39-84d3-3808-89bd-8bba4caedff7 | -3.26149 | -42.55343 | 2026-01-26 03:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1bd00b0-8653-3ca6-a216-7c0d254c5717 | -5.17766 | -35.86062 | 2026-01-26 03:36:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| afc6c11e-e3f8-3a10-85cd-53c33433d11d | -5.37918 | -35.41901 | 2026-01-26 03:36:00 | NOAA-20 | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48a04f09-5dc5-3896-9a54-92a0bc947314 | -2.75226 | -42.79184 | 2026-01-26 03:36:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2368e86e-79ef-3266-9962-e6810d8db171 | -2.75787 | -42.7928 | 2026-01-26 03:36:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e3445a-490c-3a1c-8155-e9fd8f72fd4c | -4.89425 | -40.71476 | 2026-01-26 03:36:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9bdb6798-8d29-372a-a961-4d01071c93fc | -5.47647 | -37.68356 | 2026-01-26 03:36:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13dd3edf-7813-3e15-8653-92c0f4765af1 | -5.20871 | -35.56041 | 2026-01-26 03:36:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02c51644-767f-3470-8b29-22bae590c144 | -5.74436 | -35.56738 | 2026-01-26 03:36:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5acf1135-4fa2-3a88-a053-31d253ef7af3 | -4.89631 | -40.71251 | 2026-01-26 03:36:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 32b91b41-dee2-31fa-9ec9-0cad38403b3d | -10.00579 | -36.47816 | 2026-01-26 03:38:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e5cfe7e-0827-3d81-8fb7-b0e589f9414c | -6.37259 | -37.37439 | 2026-01-26 03:38:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c418eddd-4c3d-33f8-bc85-ec1ddd337564 | -9.96647 | -36.78358 | 2026-01-26 03:38:00 | NOAA-20 | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5c2a680-ecf8-3da2-bea1-b4b43d5b89f1 | -8.54512 | -37.15966 | 2026-01-26 03:38:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 07065a41-52cf-3462-a68b-13c78b5385ee | -12.08632 | -43.77194 | 2026-01-26 03:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b89eca01-df28-3833-aa01-a114d803a53f | -10.00298 | -36.47381 | 2026-01-26 03:38:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84fb8121-e685-3cd1-851a-32b8dbfcd41f | -6.73824 | -35.21002 | 2026-01-26 03:38:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d01c0fc-40f4-3bb9-a251-c697c2c69103 | -9.59248 | -36.61983 | 2026-01-26 03:38:00 | NOAA-20 | COITÉ DO NÓIA | ALAGOAS | Brasil | 2702009 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 708b0530-700c-32b3-8346-4ff52e78185d | -10.00237 | -36.47759 | 2026-01-26 03:38:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6be3836d-0999-3afe-b658-a1debd3a7c9e | -6.37186 | -37.3788 | 2026-01-26 03:38:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09691008-fb83-357f-8ec0-e12dd64cdaa4 | -6.72707 | -37.67331 | 2026-01-26 03:38:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a75840f8-1ca6-3c7f-82b4-634b0c50a27e | -8.17128 | -34.98035 | 2026-01-26 03:38:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8caa9a16-6735-3635-93d5-30e27f2a4efe | -6.74161 | -35.21059 | 2026-01-26 03:38:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c2996a1-3e83-3166-8790-75d38ef83f68 | -9.96301 | -36.783 | 2026-01-26 03:38:00 | NOAA-20 | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e62dcc82-0656-376e-a946-3233ce8fb4a6 | -19.7242 | -56.8408 | 2026-01-26 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 618a8212-12ba-38dd-afe0-1e7c879580a2 | -19.7041 | -56.8436 | 2026-01-26 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| a9df2e6d-b271-3482-b276-d874cfa747e3 | -13.25029 | -41.33197 | 2026-01-26 03:40:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20796ac4-36e2-3cef-b466-363daa0013ad | -17.99877 | -44.51847 | 2026-01-26 03:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cbd2232-ffa6-308a-8430-f072e4bc3d91 | -22.48293 | -47.00791 | 2026-01-26 03:42:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6317945-90fe-3de9-b94f-55126a242b56 | -22.32311 | -47.13765 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd9a2d08-4bd8-3449-8827-c2aa4f77b976 | -22.32254 | -47.14019 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08548bf-ede2-3de3-8def-d527ae684412 | -21.67066 | -49.75814 | 2026-01-26 03:42:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7a9f15d9-bbf0-345f-bf8a-b7590602dead | -21.67182 | -49.75325 | 2026-01-26 03:42:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e691ff1c-9469-339b-b819-cce879b61089 | -22.32326 | -47.13683 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bcd9d45-d221-30dd-a6e1-9436916ebf49 | -22.31719 | -47.13969 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ba18796-2488-3c67-bca3-c857ef8d940d | -25.2047 | -51.39248 | 2026-01-26 03:42:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c7f884ed-920d-31bc-8e9f-337914a9f7aa | -22.31736 | -47.13885 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd8f3d9c-8916-3760-8b30-96b425352a7c | -22.31795 | -47.13628 | 2026-01-26 03:42:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6beb92b-4a53-32f6-8c93-bf4e26a9c55f | -19.7041 | -56.8436 | 2026-01-26 04:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| a40bc8d8-0850-33e2-94cb-d1211571fb48 | -19.7242 | -56.8408 | 2026-01-26 04:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 12e5595b-cd33-3d64-a030-237c22ea7ee7 | -2.47008 | -45.06625 | 2026-01-26 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ad1b5a-c568-33ea-9c1b-49980829aaf1 | -2.23516 | -45.39114 | 2026-01-26 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698e2307-43cb-3914-af13-94166f8aaf04 | -2.23186 | -45.39064 | 2026-01-26 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d549b27-6ec8-378e-93c6-88005f249b9f | -3.26186 | -42.55028 | 2026-01-26 04:25:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76a166fe-1f55-3e1d-8a01-b479c58956a7 | -5.17784 | -35.86013 | 2026-01-26 04:25:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b2c5a284-ae7a-348b-8b4d-23252b58a047 | -4.89464 | -40.71344 | 2026-01-26 04:25:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4b44681d-834c-3437-a353-de2dedeb2189 | -5.17841 | -35.85614 | 2026-01-26 04:25:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7cd579ba-92b3-3ac5-9c15-6fa80eb857d3 | -2.75792 | -42.79119 | 2026-01-26 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81ce44be-84da-3c25-8faa-f3ac46916acd | -3.26609 | -42.54671 | 2026-01-26 04:25:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 239954ce-3ed1-36bb-8c53-8ccea5e3bda7 | -2.47339 | -45.06676 | 2026-01-26 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d7372cb-2860-3b78-84b7-381076e4c7a6 | -2.49213 | -44.5981 | 2026-01-26 04:25:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03d4866f-9aba-3aa3-9c4b-c51d239dd1ad | -5.44099 | -46.21778 | 2026-01-26 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4993f318-3397-3438-9866-7f9a8ab4c005 | -6.19968 | -39.28365 | 2026-01-26 04:27:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd7505fb-549e-32bc-b833-fbc26c9f48b7 | -9.96954 | -36.78169 | 2026-01-26 04:27:00 | NOAA-21 | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b53ee97-6bfc-36f4-8101-e89267051504 | -6.20362 | -39.28901 | 2026-01-26 04:27:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e7e6d6c-d454-3999-884f-ae7f7ed99cba | -6.19899 | -39.28838 | 2026-01-26 04:27:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c057f30-f03a-36a1-9a3c-bfcb1babd7db | -6.30068 | -44.5188 | 2026-01-26 04:27:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a405e3d0-0e98-3502-a4f5-ddabe4432187 | -11.07369 | -45.37276 | 2026-01-26 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fb4f5cc-c3ba-307f-8201-6b28fa2250a1 | -6.20431 | -39.28429 | 2026-01-26 04:27:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 783ec9ea-0a32-3320-8dfe-1933f4805113 | -11.0736 | -45.37182 | 2026-01-26 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 556f198e-045e-34f4-856d-a25edcdc74de | -12.09182 | -43.77159 | 2026-01-26 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1324e659-fbdb-3b32-8073-8708ba96b074 | -12.44879 | -39.24923 | 2026-01-26 04:27:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9411ce58-c97d-34c0-8d1e-c8390fb6cd30 | -12.08807 | -43.77098 | 2026-01-26 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a6a950a-a636-39da-9eaa-f7c64316c474 | -10.00608 | -36.4768 | 2026-01-26 04:27:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae623a5b-06fc-3076-8f77-f44f22c50080 | -12.44723 | -39.24904 | 2026-01-26 04:27:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 706b4c74-d28f-3564-90bb-0d0d091974d9 | -8.76482 | -40.67692 | 2026-01-26 04:27:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10213ae5-46ae-3023-a7fc-21f10e41d9f6 | -19.63443 | -57.34963 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 795a785f-ceda-34e5-a28c-de0e1521d1d9 | -20.32011 | -57.81231 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c0a3bca8-54e7-3086-8d41-958983e308cf | -19.66349 | -56.85061 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 197cc6f0-141a-3907-ad04-22c1a3be4cd6 | -18.84433 | -57.73416 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| dd866f0a-9556-3a22-96e6-0467f6af2301 | -20.30721 | -57.82663 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7a674a61-1093-3120-8ac7-250d48fe141f | -21.67388 | -49.75067 | 2026-01-26 04:31:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 20b4cff9-40de-3325-a7e1-7eccfb972ac6 | -20.91726 | -56.38155 | 2026-01-26 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 908d0363-5abd-312c-8a34-ca463865dcfa | -19.71823 | -56.83968 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 96529160-14de-34c8-b5e7-9207f20f4ffc | -20.31536 | -57.81123 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d7333a1f-644b-33cd-93aa-e3fd873589db | -19.66777 | -57.32961 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 3a24ec0f-1f25-3608-97f0-c39ffc1bc05f | -19.66114 | -57.2899 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 835f4755-73ae-35df-a8bf-6ea78cc24105 | -19.63911 | -57.35067 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b8e07e05-71ea-394b-9819-7066a1bf4ed2 | -18.8291 | -57.72293 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0f0ccfa8-95f2-334f-ade0-8ee5e6e71ddd | -19.61786 | -57.33496 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 78c1685d-b513-3f0b-9770-9d446de33f79 | -18.84625 | -57.73876 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 0321ccd3-b45a-38cd-ac11-41632f84bcdd | -19.70014 | -56.83573 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 19d3e9cc-4e67-394a-9898-a99773e1d68e | -19.69562 | -56.83474 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8cab43e2-5f81-384f-9a90-40dad6f36c2a | -21.92441 | -54.7004 | 2026-01-26 04:31:00 | NOAA-21 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a2e85d5a-8b00-3604-bf12-0730a29eac50 | -18.80342 | -57.69928 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8deb980c-a740-362d-98d4-cb6eeb3e3484 | -19.71332 | -56.86408 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09b3e5d9-4d93-38fc-bb88-9b0536b5fa3c | -19.70353 | -56.83904 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f51637a0-f379-3cea-bcde-f7f8f6051c0d | -22.3183 | -47.13599 | 2026-01-26 04:31:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54e1ac10-07a4-3c96-910f-09041d80ca7d | -18.83026 | -57.71721 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8291f1a7-5d12-3cb2-8f1d-957e4b9cd8f4 | -19.62254 | -57.336 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9eed2a19-6525-37c2-b050-dcfece6172fa | -18.8492 | -57.73523 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| b0319847-0d95-388b-8543-5087c9e579d0 | -25.47371 | -52.75385 | 2026-01-26 04:31:00 | NOAA-21 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7498e9bf-ceed-3ed1-bf7e-6edf5f111c6f | -19.72178 | -56.84554 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a068525e-fef9-3bce-9f87-1791e130f9ad | -21.82161 | -48.61743 | 2026-01-26 04:31:00 | NOAA-21 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8284500a-bffa-33da-8a76-c7e760c90eee | -19.71725 | -56.84455 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 1685a775-6d3e-33fa-8942-1f41f4cc1032 | -18.82053 | -57.71506 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |


[Clique aqui para ver as próximas entradas](README4.md)
