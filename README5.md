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
| 2293eced-defa-3b30-af81-706a9a8cffc5 | -20.19803 | -46.88535 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e6b5e47-cd5c-312e-9eb4-0401506b9071 | -23.32828 | -50.12592 | 2026-04-23 04:32:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 854eac41-fd67-35f1-8bb8-0e4017657afb | -20.20027 | -46.89333 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 971b46e1-1e9e-3253-a926-f4e89e553536 | -21.70652 | -48.42792 | 2026-04-23 04:32:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8b929fc-831b-356b-8864-14a5f0a43a16 | -20.18624 | -46.89483 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af718cc-091b-34f3-b7b1-62a6c6ef2839 | -20.20308 | -46.89753 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68e7aead-8bec-3023-aa75-0c6de4d82fbe | -20.23992 | -46.76839 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8985b18b-75ac-33cc-b994-4032dbdfabe2 | -18.30998 | -52.89703 | 2026-04-23 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f89b4bcf-dc42-35a6-abb6-9afc3dfa982c | -16.4256 | -54.92268 | 2026-04-23 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f5f14cd-48e7-3e32-b58a-fed3b7659f2b | -20.17096 | -46.95015 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad1ca301-6d02-3b9a-a2e8-b89b22027fd8 | -20.16089 | -46.94839 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49928406-9ebb-32ec-ba5c-85da1e87fd40 | -20.1693 | -46.93837 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9294895e-6a27-3493-86ad-211f6935ecf3 | -18.41858 | -54.54842 | 2026-04-23 04:32:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8e4e327-a9f3-3fdb-98e2-ad947418b07f | -18.27432 | -52.88614 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55fb275b-3e90-3575-b625-62db9a670c37 | -21.33791 | -47.07148 | 2026-04-23 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f6df5d04-e619-31ec-a9a5-196378ecf457 | -20.17603 | -46.93943 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50567093-ea3c-3240-9010-579a6517d821 | -20.20251 | -46.90131 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9a02fccf-a47e-3040-9339-f14aa4ea9024 | -20.24265 | -46.79603 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c35fe1c-4fdf-3d44-a667-579494084930 | -20.23477 | -46.80241 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c575942-2a31-3229-bfe7-8078c0ece6d3 | -20.20852 | -46.74726 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8035889-969e-337b-a479-3c840823ef75 | -20.18938 | -46.73645 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9cd67f4-e8fc-39bd-b532-2008d04e3ede | -20.17376 | -46.95443 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8084e9b2-57c1-36ba-890b-1064c9ddcdbb | -21.33396 | -47.07474 | 2026-04-23 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f19d516e-5550-31bd-836e-57405d4b72b0 | -23.0381 | -48.43606 | 2026-04-23 04:32:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d2dd76c-d662-3dbb-900b-f34a4589a0d3 | -18.28311 | -52.88399 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce062a8-5e62-3272-a291-d449fb7782f1 | -19.6879 | -51.34005 | 2026-04-23 04:32:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76cc739-13b8-3535-945b-37d8388a3531 | -20.1777 | -46.95119 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d018ca6-ae2d-3cd7-bb0e-b9b5ec429976 | -17.4832 | -51.08859 | 2026-04-23 04:32:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36619dcb-ca81-320b-98c8-6ee1bb1c82c3 | -20.19519 | -46.90403 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb836151-ce6c-3281-beef-9a382607f1b1 | -21.05311 | -48.6666 | 2026-04-23 04:32:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fe1778c-c2a8-31cd-9bc4-40dc906336ca | -20.20348 | -46.73476 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c36fe81-e4ff-3d6d-ad64-4669be8cbed1 | -20.17433 | -46.95068 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8eaf3a2-6b06-37c7-867b-5e707ea5f2f3 | -17.89887 | -42.8588 | 2026-04-23 04:32:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6be4223-6072-33ba-bdc2-61105bbc01b7 | -20.19127 | -46.90717 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f75f701-4365-35e3-a0b3-a1084888ce69 | -19.44276 | -56.59039 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e39ead72-7b0f-3636-8757-fda64eee02b8 | -20.198 | -46.90825 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1c8827-7649-3424-a598-ce095a02da29 | -18.49419 | -51.66351 | 2026-04-23 04:32:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f42347-5984-35f5-91d1-625d2be0e004 | -22.96706 | -52.69676 | 2026-04-23 04:32:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 93a74d6b-25ad-3294-92b5-f3dc6f99cd07 | -20.20193 | -46.90506 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eaca9e52-2728-3549-b5fa-a3804873a348 | -18.49343 | -51.66537 | 2026-04-23 04:32:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe9214a5-7b28-346f-b82a-7bdf9d7ddf76 | -20.24211 | -46.77673 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd13d86d-0857-30ea-9b4c-a58b7973f666 | -20.19409 | -46.88857 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61bb5615-96bc-3a89-97a7-76caca023697 | -20.17941 | -46.93993 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a294717b-1304-34db-a054-b0fc9adebf8e | -21.39665 | -48.67014 | 2026-04-23 04:32:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8258d3e9-8757-3bc2-9a3d-5ca25143d27b | -20.19466 | -46.8848 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15ac3dc0-fbea-34ff-8ec9-cc3e877235f2 | -21.05251 | -48.67031 | 2026-04-23 04:32:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c938acd2-398e-3e53-b079-65b35a1ceb27 | -20.24772 | -46.78534 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc37f8db-5af2-37ab-8e9c-9b585c9d2cc6 | -18.26958 | -52.88905 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a1b531-e7b7-3d22-b470-9efe42053881 | -20.2001 | -46.73421 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ddbb9e7-fd24-3ceb-9709-06a7c245700f | -21.33338 | -47.07857 | 2026-04-23 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a8e9640-caae-369c-83ae-a0965c6e6d73 | -20.23308 | -46.7907 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd9fff62-ec0c-3f08-bc73-c54484ead248 | -18.49982 | -55.50307 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4118aaf0-20d8-34a6-95bf-baf4ee7b1d5c | -20.1997 | -46.89707 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ae5ae58-a96c-3dad-91c4-cf5a52fa5ff8 | -19.44896 | -56.61088 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f0fb4cf7-60ab-33cd-bfac-3ac158de26c7 | -20.19913 | -46.90082 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fe8baad-bd42-345f-931b-28643f1abe38 | -20.18567 | -46.89857 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8b895d7-f064-3edc-ba25-060b0e48588b | -22.78661 | -47.04726 | 2026-04-23 04:32:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 494f84bb-a0f5-3946-aa80-c35ddc38ebeb | -16.43248 | -54.91277 | 2026-04-23 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db5de082-1864-332d-8855-fe285728e582 | -20.19856 | -46.90455 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc60387-2cb8-38a0-82a4-f0f7208ea202 | -18.48334 | -51.68095 | 2026-04-23 04:32:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06393806-c877-3bf2-9c12-173d96dd4d4f | -20.23195 | -46.79815 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c829e72c-17de-3e7d-bced-0eecbab5089f | -20.23589 | -46.79501 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73e9b367-eb21-350c-ba42-022e79252591 | -17.16483 | -46.83438 | 2026-04-23 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81e17f32-a23f-3e07-aee9-8d2f30a49033 | -20.19074 | -46.88794 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4e1183b-1bac-3592-9c7b-25580cff9e25 | -20.23932 | -46.7723 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a8fbb65-6d00-3a63-8719-43790b951632 | -17.16816 | -46.83495 | 2026-04-23 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b16b23f-af63-36be-821f-5b5b08c3335c | -20.24829 | -46.7816 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc36654b-a203-3ffe-8ce4-76d804a0630f | -18.27836 | -52.8869 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63b3e273-e8f2-36c2-b440-899bb394a277 | -19.90872 | -49.88279 | 2026-04-23 04:32:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a8e7e066-5f78-35ee-8cad-a4cd1faeb8ba | -20.18196 | -46.80888 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d07b7ae-e833-3a91-b33e-dfe210e41916 | -16.42668 | -54.91713 | 2026-04-23 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55f6ab9a-04cc-395c-af12-fbfc34f1c3bd | -20.2387 | -46.79922 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fbb9544-91d2-3c45-a37e-9ae9a768486a | -20.19071 | -46.91084 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4a1f35f-7a53-3cb0-97ab-9402c9d75042 | -20.17267 | -46.93892 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a9e1385-d5e8-3a3d-b095-3cb82cf5c721 | -18.85781 | -50.12346 | 2026-04-23 04:32:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 249b8d1a-a394-3e8d-9864-80eec0045ba2 | -22.11153 | -48.45335 | 2026-04-23 04:32:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 41dad311-46b2-3093-9771-3d0fe9701e8c | -22.96624 | -52.69408 | 2026-04-23 04:32:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 16342ad2-2709-33e9-ac8a-21817965be4c | -20.20571 | -46.7429 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fbc1523-c026-3d49-b4e6-cb1be5c7361a | -18.28645 | -52.88848 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 590f113a-e280-342a-88f7-d1efc5b2cbb6 | -21.04978 | -48.666 | 2026-04-23 04:32:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 324426be-a12d-375e-9c88-8746fe6cf3c2 | -18.28241 | -52.88768 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99357f4d-6873-30eb-a25b-d0034be8b110 | -20.19745 | -46.88912 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6461afe-c0fa-3481-9fb9-0a2e2412a380 | -20.16482 | -46.94524 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 553d5729-e4a0-35f3-aec8-7c0526f79680 | -18.50531 | -55.50019 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b033c057-15ea-3125-b8a0-3c36c3a97477 | -20.2449 | -46.78112 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8b9b70d-f176-3e63-b126-2f1e9dde8f92 | -21.04918 | -48.6697 | 2026-04-23 04:32:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fcc6d3c5-412c-338b-9b56-8546dcbeb6ca | -18.27362 | -52.88982 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6750069c-f10e-3088-a371-991e2bc5b6dc | -21.27567 | -54.41735 | 2026-04-23 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f84435f-a1f4-3328-8c4f-a774bfbe9362 | -18.14062 | -54.23632 | 2026-04-23 04:32:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1fc0dd-3a55-3c8a-9c91-cc31fcd0da35 | -20.24209 | -46.79972 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74ce816e-ec0a-3108-9b94-900742c87d21 | -20.18455 | -46.90602 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d37fdbc-3b91-3ff5-a62e-2ceb6934e795 | -17.48689 | -51.08926 | 2026-04-23 04:32:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 106e48c4-d756-3a35-a4fb-e9c53ee61725 | -20.20628 | -46.73911 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7f5de18-b4d8-35fd-8795-86da1baafcfb | -21.39938 | -48.67447 | 2026-04-23 04:32:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f170dfb-0238-3652-8c18-064d6721b17c | -20.19463 | -46.90771 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b6e1026-ae98-3b32-9d89-81920f33d441 | -18.41412 | -54.54742 | 2026-04-23 04:32:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0499727c-8da6-386e-93a4-3faf2d56dcd2 | -22.10761 | -48.45647 | 2026-04-23 04:32:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 72d1a9a5-d064-3f8c-87b6-38b1d8c7fa46 | -20.17827 | -46.94742 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e6e517-9ff7-3145-b87a-36c9ce98b8ec | -21.70319 | -48.42732 | 2026-04-23 04:32:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17c60b46-d830-3f21-a0c3-84bca832d58d | -18.30191 | -52.89538 | 2026-04-23 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
