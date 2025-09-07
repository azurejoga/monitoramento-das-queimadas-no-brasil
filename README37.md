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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0ec0e4f-103f-3f5a-b257-b0463be8b5f7 | -17.40563 | -49.31046 | 2025-09-07 04:00:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0f85e7f4-8f68-3e31-8a39-0105e196ade3 | -19.34144 | -42.17138 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47a76557-4ad8-3054-ac93-c682f6234ab7 | -13.83945 | -46.27427 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 993d79d7-d72c-3bae-89e0-dc3c06b76613 | -16.94184 | -45.76356 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b21d6781-9f85-319e-815e-e07737beab92 | -17.95141 | -45.30094 | 2025-09-07 04:00:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1229438d-0e29-333b-8e5b-a3ff25f5f10d | -17.68154 | -44.50578 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e0be65-d0ac-3499-af8b-f341e99b6d2e | -16.28336 | -45.68511 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2df13a30-f7b1-3afc-ac9f-7a31a9f4cede | -15.5296 | -42.62615 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1f98ecb2-b92b-3908-b8d7-395008db2388 | -18.63397 | -42.77351 | 2025-09-07 04:00:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 486fa156-df14-3825-a90a-24525e30308c | -14.82398 | -48.19601 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa6d994-e6d5-307a-93f3-18fa621a4b9b | -17.70812 | -47.65314 | 2025-09-07 04:00:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32a7aaf5-65dc-319d-a5c7-8383be642a73 | -18.11655 | -44.49921 | 2025-09-07 04:00:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f838a915-bc28-3e2a-ac07-36a5a1406326 | -17.20736 | -46.86772 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abbf3943-92a3-3e70-aa16-28391906c99b | -13.5478 | -48.11267 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c25b496c-a914-3f48-82e1-e1106daec199 | -17.67513 | -43.53315 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cff6dfa-b014-3fed-b8db-d7f652649c75 | -19.07032 | -46.77555 | 2025-09-07 04:00:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a821f035-2cbf-3da4-bbd9-0be524592612 | -16.9398 | -45.76694 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f09b92a9-895f-3cd3-ae49-78917842a247 | -19.87926 | -45.02821 | 2025-09-07 04:00:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e806214-f851-35db-a96f-f48760909445 | -17.68776 | -43.54414 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 129235ba-4cb0-3eed-a5fd-e3a68eb8dd79 | -15.88473 | -52.19366 | 2025-09-07 04:00:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62234739-783f-3744-82c7-cee7f15617cf | -17.63418 | -44.26056 | 2025-09-07 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a5894cb-6c4c-3349-9f4e-c00a2af368d7 | -15.6947 | -45.04431 | 2025-09-07 04:00:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5afb775b-1c83-3855-98c7-6697bd410cda | -19.66881 | -44.88349 | 2025-09-07 04:00:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62801446-2d88-32bd-aefe-578373bf4957 | -18.03226 | -47.09637 | 2025-09-07 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63031e73-b2b5-3914-bee7-7c8fd53294d9 | -17.22123 | -46.7019 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c86c05d1-c591-3f05-b97e-1c61d58c7fa2 | -17.24369 | -46.69843 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9eb9711a-1267-3ffc-9b90-4afa7228eca8 | -15.18154 | -47.97232 | 2025-09-07 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8931e5e-5a95-3f2e-8bca-10c5e4173b0c | -16.94377 | -45.76785 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3846e9a5-9f4a-3d0a-99c3-8f5837103324 | -16.54169 | -45.09507 | 2025-09-07 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2625080d-e3ec-30b2-8d90-9feca831bed8 | -17.86472 | -44.33313 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6535e5e9-8d53-3bef-b122-9d4bd6cb46e2 | -17.6347 | -44.25799 | 2025-09-07 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 840edbb3-6a6e-3b77-8648-4d742fe8334f | -13.67043 | -46.95219 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1875d214-e40b-3695-8b0a-5b1edb7e5655 | -17.70351 | -49.10802 | 2025-09-07 04:00:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8fe0c3a-7f10-3892-9ecf-5a7f49a7a1a9 | -16.93486 | -45.77889 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e9648d6-2387-3918-867b-f8dff5649239 | -13.67001 | -46.95518 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b87fd5d4-34ef-3a07-9605-6c672faf8495 | -17.67092 | -43.53654 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb85e554-d12e-3096-b522-283a965c8e01 | -19.00981 | -46.61073 | 2025-09-07 04:00:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64865b71-0370-32a6-b70e-100b92936422 | -15.37341 | -46.42354 | 2025-09-07 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f394c7a-7290-3746-910e-8439bd97c54c | -14.27478 | -44.97733 | 2025-09-07 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bbe037d-a318-3050-9a9a-bcb194b9b33f | -16.53693 | -45.0993 | 2025-09-07 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 532f114c-b855-3014-b37f-9d527c0e2a0b | -16.9338 | -45.75439 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5330f7ec-3f66-3431-883e-ba38b701bf29 | -13.83753 | -46.26044 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13fe0174-2198-3439-a741-8539dfaa6f3c | -12.7804 | -52.96554 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76475f52-e93d-3989-bcc9-3f3bb1fe147d | -15.53893 | -42.66291 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 900c5bd0-3acd-357f-b553-62cb41392984 | -18.03374 | -47.08861 | 2025-09-07 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adde58ba-b443-3f82-a369-c9ef08d883be | -15.73125 | -47.02868 | 2025-09-07 04:00:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 19763b4d-9abf-3927-b108-55b3803fa04b | -15.00757 | -48.00779 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3829859f-ce56-3d99-95c6-ec327a2af70c | -16.94474 | -45.76241 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5df46676-c819-3463-aab9-d4e9be9583cc | -16.08942 | -41.81518 | 2025-09-07 04:00:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c547e25c-1a18-369c-a7f6-cc338d2e55d8 | -13.73956 | -46.90995 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b5baf88-b73e-3ac1-afc6-44cce59e01e1 | -18.07207 | -47.98999 | 2025-09-07 04:00:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65c4066f-b298-3689-9123-776702bb4780 | -15.53612 | -42.65842 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cec988e8-6fb3-3699-b627-05fc732d9238 | -19.48515 | -47.7496 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e30a251a-1afe-36e0-ae06-7e606af29263 | -18.38299 | -43.89529 | 2025-09-07 04:00:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 335665fb-de10-32e2-b14a-bfb9c7be275e | -19.41621 | -44.31998 | 2025-09-07 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a8392e-ccc8-3778-9130-154d7ea5f407 | -17.24295 | -46.70237 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e3a5884-15ed-30e0-825d-3753791d6133 | -13.71214 | -46.88119 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2575a96f-2a64-3736-be01-ea25f3364553 | -16.94083 | -45.76899 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0388d88-d6ed-3126-926d-8947db691316 | -15.73466 | -47.02721 | 2025-09-07 04:00:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7c264120-3920-37e5-8028-ff7a247e5f2b | -19.89871 | -41.43885 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6318bb8a-c4a6-3092-bdf2-140b98bf2018 | -19.88292 | -45.02896 | 2025-09-07 04:00:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32d733ca-e1b8-34b6-b44d-9e87db19dc1b | -15.36101 | -43.67242 | 2025-09-07 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 751e920b-400f-360e-acd9-36f9825aa9ff | -15.25735 | -40.74762 | 2025-09-07 04:00:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98734880-f414-3259-b99c-aa715fa4c488 | -15.11245 | -48.07434 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1be0571-b983-3cdf-9c67-9e440e74dd14 | -16.3371 | -52.94814 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6fe19f6-a643-3cdd-80c0-43ddf9fbe825 | -16.93889 | -45.75726 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd18571f-e4d1-375f-ba45-30864fbca767 | -17.68633 | -43.55243 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a231095e-bb10-3c2a-8957-eb8e4fa916ac | -13.9192 | -48.04357 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b688173e-c249-3e80-ad75-566df37e1316 | -13.84022 | -46.27013 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3397d1ec-4ffb-3094-8237-2d4c53397e4f | -16.93777 | -45.75521 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 179b9262-8b01-39b3-bd17-90e85de9571c | -14.48732 | -48.7657 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e7fb7c3-f952-364c-99db-b8bbf82d9420 | -16.34332 | -52.94997 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94d87ea4-463d-37f8-b8f3-ab5720ca0df5 | -13.83023 | -46.27554 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2bffee4-7ebe-386c-a968-77d6c3b8f130 | -19.36786 | -43.65552 | 2025-09-07 04:00:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab53b59d-1ac2-3758-a115-e57f42eff995 | -15.88953 | -52.20264 | 2025-09-07 04:00:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2a05aa4-792d-3e07-a6a9-f591e963ac67 | -14.496 | -53.24885 | 2025-09-07 04:00:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 271cbbe7-e73e-315d-a011-fa349e60e499 | -13.91883 | -48.03635 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 044d2705-34e9-33f3-9159-fe0e3ffdb911 | -13.91133 | -48.0225 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6417024e-df28-33b0-8d7a-819a6a4a31a0 | -17.2224 | -46.71877 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7f83c16-5126-366b-b75f-470fa790bf4c | -18.02159 | -44.90836 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b58611bd-812b-3b6a-babd-74a8eb21139d | -14.84952 | -46.69112 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fe54d810-46d4-3f0f-bb83-4c68a3fd44d7 | -14.74331 | -47.5052 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 342020d1-5c8b-3511-937f-4b4df9ac3b65 | -14.48842 | -48.76005 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ae8628-7475-3508-96b3-6ba3b37aaa3f | -18.01785 | -44.90762 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 525fe886-673c-3917-a26d-ba39535e64b5 | -16.92588 | -45.7827 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bc403147-14f5-39d7-b546-e77587b0f662 | -15.83532 | -52.27309 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86b72349-d55a-36e9-80ef-7f66243e6db9 | -18.03735 | -47.09282 | 2025-09-07 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab91bb28-908e-3237-9534-28f0a8dced09 | -13.83445 | -46.27701 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4932ad61-a974-3e72-b869-0ded9903668a | -15.84659 | -52.28024 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2cc46e1b-532e-30e0-8156-4648cfe3a5a3 | -17.66949 | -43.54484 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 258d5969-8aae-35ed-87d2-758b341667a6 | -17.7164 | -44.49158 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a3f7765-a7ff-3838-9aa5-14a8200f1a06 | -16.96672 | -45.83038 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fec13608-67a4-3291-8ad4-7f7f95b625a4 | -13.85282 | -46.25048 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78be4c03-46d4-39cd-a054-71a4de995d31 | -17.70841 | -49.10886 | 2025-09-07 04:00:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c8dfc2c-6883-37c1-89e5-4edb0e033005 | -15.8339 | -52.27956 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f59eebb9-4c9e-310b-968d-b7f95ef88892 | -13.55518 | -48.11012 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f98cf14a-cb06-3fb6-b394-1b5d44f0faa1 | -17.84862 | -41.52562 | 2025-09-07 04:00:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4e03738-1ccc-3258-9e7d-db2cfde5d567 | -19.48363 | -47.78111 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 153df573-df3c-3b3e-8966-dbef42b94177 | -20.42789 | -42.21355 | 2025-09-07 04:00:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 48aa7eb7-2a6e-3ee8-bea5-93ae5dae83b0 | -17.67447 | -43.51603 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README38.md)
