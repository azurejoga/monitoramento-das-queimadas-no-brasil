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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19bbc56f-ed44-3732-9c9c-07eecdac8003 | -4.91107 | -44.32291 | 2025-11-11 04:50:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e8270b2-8ba1-34e5-a288-2d3df21f00a2 | -4.20675 | -49.7751 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ebfefc-198f-39b9-b8d0-0b41aeb1c57a | -7.27352 | -42.16412 | 2025-11-11 04:50:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9f69324b-7703-382f-ac81-0273ddd7f415 | -4.71869 | -46.45485 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 8a987e71-9438-3fad-9caf-ecb961ea4a72 | -4.25489 | -48.58085 | 2025-11-11 04:50:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f155c995-d613-3eb4-89c8-1974a3286d80 | -3.88689 | -47.18191 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a233e51d-1c91-3e76-9f30-b9c217110f4f | -3.21214 | -43.32742 | 2025-11-11 04:50:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0091c3d-a97f-3dc5-af4f-9c570d1e472e | -1.48475 | -45.61874 | 2025-11-11 04:50:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d64819a-7505-35e8-95e2-9286f04eb6dc | -3.41581 | -44.10106 | 2025-11-11 04:50:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a10e76fb-7a7b-3a5b-b2e8-e7a5f27317ad | -2.47847 | -48.85459 | 2025-11-11 04:50:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 298a85f4-5c43-3ba3-920c-907d0720559b | -2.87674 | -45.4277 | 2025-11-11 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891aa015-ddd0-3391-97c6-3019644524f8 | -4.31755 | -50.76991 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85d2d1dd-684f-366d-b5d5-b81f4e775404 | -3.81194 | -46.00617 | 2025-11-11 04:50:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2ab86542-5f74-320b-aeaf-de2a083afaf8 | -13.46368 | -44.03423 | 2025-11-11 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179ec468-e429-3e11-8c07-a39310e14ceb | -20.10872 | -54.66192 | 2025-11-11 04:53:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd01a43b-d487-3634-a8e7-5c3f434cff49 | -12.01164 | -43.85083 | 2025-11-11 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa03fdc5-1fd6-37e0-9804-d5ddb16f0e03 | -20.79226 | -48.35265 | 2025-11-11 04:53:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29bf2640-decc-3779-96aa-d02131a607f8 | -17.80789 | -51.73479 | 2025-11-11 04:53:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43c0906-8e40-3bfc-8420-3fafbeffd26f | -9.89099 | -47.86581 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e5bd8cb-965d-350a-8dcf-823df76954d3 | -12.33385 | -43.65702 | 2025-11-11 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10d0be1c-5503-33b6-af29-9d72d18dd815 | -17.8073 | -51.73906 | 2025-11-11 04:53:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cf89b4c-e2c9-3188-b2be-fa87d541a1fb | -9.91673 | -47.8619 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ea704ec-a0ca-35ae-91a4-2f33aad59365 | -18.24707 | -51.27251 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 82a0d9e8-9bf3-3d00-84b0-0841722255ca | -18.39642 | -54.99286 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 100cc28f-fc90-344d-bbc4-2baee4c5ac02 | -18.39536 | -54.9778 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37a0da54-0516-3e8e-b86b-30c6f2280ac6 | -9.67365 | -43.9062 | 2025-11-11 04:53:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0281a432-97c7-38f8-87e2-567d33fb1f6f | -17.56017 | -54.01831 | 2025-11-11 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 424008b0-4426-3cce-a12f-beb45dfa8591 | -10.85048 | -44.94234 | 2025-11-11 04:53:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c933b9a-f696-331e-9434-ae426a12db27 | -9.67318 | -43.90985 | 2025-11-11 04:53:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29e9cfdd-bd25-3c44-ae75-2b30a56ee2ca | -7.48923 | -47.15524 | 2025-11-11 04:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02116e53-7700-3bf8-b28a-45611f51d042 | -7.48869 | -47.15905 | 2025-11-11 04:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ebac0a8-3801-33db-9849-f8f6bc99cadc | -20.29613 | -54.08877 | 2025-11-11 04:53:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22b4092e-253d-3496-a4fb-7b8a967181ac | -20.02673 | -54.84235 | 2025-11-11 04:53:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7c728bf-39af-3292-8483-f0fee1e90288 | -19.59419 | -51.08601 | 2025-11-11 04:53:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f7669e9-a217-3d47-ae1b-002d42cc1f72 | -18.47864 | -53.40153 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4d0f7575-690b-3ef7-a4cf-ff10f21714a3 | -18.47879 | -53.39863 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4d1c5dcd-5527-3035-8731-b93b4d127fb6 | -17.56351 | -54.01886 | 2025-11-11 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31ec4197-13b0-3829-ba40-22d82c0d64bb | -11.90812 | -43.82692 | 2025-11-11 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6d18054-f302-3fe2-9466-5b6c4ed8d9a1 | -11.04712 | -45.3999 | 2025-11-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e22d3a10-1a2a-38cc-9c75-23250d463883 | -18.39367 | -54.98867 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6943cb78-d323-316b-9179-d30dc623cf10 | -11.03376 | -44.64775 | 2025-11-11 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2d01e57-8276-3e13-8397-d5bb2eef19b7 | -10.92619 | -44.61089 | 2025-11-11 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d4677f9-150d-326b-a793-12c5f7b160ff | -20.10928 | -54.65821 | 2025-11-11 04:53:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 180f41be-71a0-3fde-899e-952f69470e6b | -19.31345 | -50.50172 | 2025-11-11 04:53:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fd32590-1b0d-3906-b9cd-2c3d27b44c1e | -18.39205 | -54.97723 | 2025-11-11 04:53:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a46ecb4-9503-37fc-bac6-52afd8257552 | -19.31483 | -50.50077 | 2025-11-11 04:53:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f25326ca-e1bf-334a-8c6d-1004100cd7ee | -20.80941 | -49.83848 | 2025-11-11 04:53:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1dc29448-7285-3f35-88c9-281c8c26e250 | -18.39198 | -54.99955 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e9124579-f294-3e8b-8bab-886defbae0a3 | -18.47919 | -53.39771 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2f459223-5056-352f-a5d2-db1fde305c68 | -18.4826 | -53.39828 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1eceacc7-1f68-3f8d-b1b9-f00255092b1a | -18.33105 | -54.29076 | 2025-11-11 04:53:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a5ba8a4-6eb4-3c70-a1d7-9c3d0a1d7713 | -17.80368 | -51.73845 | 2025-11-11 04:53:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dd0b88d-0558-369b-bfca-a48c90dd433f | -12.0172 | -43.85163 | 2025-11-11 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea79915a-3707-3d0c-a95c-23b45f46d590 | -9.89563 | -47.86262 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aed866f4-9400-3801-99af-4c409db8baeb | -18.47482 | -53.40186 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bf882c3c-5bb7-3715-a8c9-cd5f0ba9e473 | -18.39311 | -54.9923 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 28b8c52f-ee68-3c3d-9059-084a3168c716 | -9.8951 | -47.86644 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2620f58-2e1e-3ebb-89f1-5bbb5d3b2548 | -18.39149 | -54.98086 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9100551-5480-321a-b8cc-d079940b8307 | -11.90857 | -43.82317 | 2025-11-11 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96c5a7e9-18af-3fd2-95de-efd8a15969dc | -18.39424 | -54.98505 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5478a588-fe07-3d0f-806d-8cc03c5a29de | -11.57458 | -44.85449 | 2025-11-11 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6db6f5d3-8f32-3594-a88a-78729e936e93 | -18.39698 | -54.98923 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c7c55fc-a0af-3e02-a362-c4eb57de00af | -20.74425 | -49.77131 | 2025-11-11 04:53:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a180f4c-2893-36f2-a4b6-c3bdde7dd603 | -18.47808 | -53.40535 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4875807-ab17-3376-9fa1-152c162aad31 | -9.86813 | -48.14705 | 2025-11-11 04:53:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1287580-9f10-3380-9e9e-ae61225a61bb | -9.88688 | -47.86517 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6a2df3-46ce-3f39-a631-d1ee5fd85221 | -12.33671 | -43.65849 | 2025-11-11 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ced9fc9-3461-3844-b080-38eb85e7b30a | -10.92097 | -44.61018 | 2025-11-11 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd18ce65-0f6e-3f8b-a798-5473bb6f1bb1 | -18.33439 | -54.29131 | 2025-11-11 04:53:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0a31ba0-32bf-326e-901a-3a9f77c5bbc9 | -18.38868 | -54.99899 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ce0a470d-2d04-32c6-8d66-ec100f2b913c | -11.57975 | -44.85523 | 2025-11-11 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02d6aa6c-67a2-37ba-b667-a5663711010c | -11.04488 | -45.4054 | 2025-11-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fa757d95-baca-320b-bdcb-51736fecfb41 | -17.13157 | -55.7434 | 2025-11-11 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d8c4ac64-21c5-3c85-a59d-0ce94d806092 | -11.04641 | -45.40556 | 2025-11-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19b8b6d0-b720-3f44-9672-1f0ea9333a93 | -18.39255 | -54.99592 | 2025-11-11 04:53:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 940fecbd-032a-3136-a83d-b166e318a775 | -11.04563 | -45.39977 | 2025-11-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88386633-ab7f-3b13-9581-ee647c88a438 | -20.79632 | -48.35847 | 2025-11-11 04:53:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77608a09-64e5-39c5-b647-39da45cdb6fc | -9.89152 | -47.86199 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01b2f6ad-829e-3168-94d0-7ae12585b6c4 | -12.33104 | -43.65776 | 2025-11-11 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11d22c8d-888d-359e-9583-cb681778f594 | -18.47766 | -53.40626 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cc035f7-a13f-367e-8a2d-89dd832c2ac4 | -18.24644 | -51.27724 | 2025-11-11 04:53:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3b497b2-c09c-32ae-a3cb-d2395d610491 | -18.47822 | -53.40245 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bde68e07-b2a6-38e0-b047-43ed8ed68a1b | -18.48205 | -53.40207 | 2025-11-11 04:53:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2e7dd7c9-1a2b-3e8b-a88a-2903fcd947bc | -11.04984 | -45.406 | 2025-11-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ab8e0dca-e406-3428-b414-d25c0b32ac39 | -11.90767 | -43.83065 | 2025-11-11 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 789f092a-e075-34b7-a2ee-96ba0679b6fd | -26.61628 | -52.98441 | 2025-11-11 04:55:00 | NOAA-21 | SALTINHO | SANTA CATARINA | Brasil | 4215356 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 774a1ae5-277f-3ae0-af77-2c220f4dc236 | -23.02716 | -47.49056 | 2025-11-11 04:55:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 282f86f7-70fa-3fcf-a68e-ea1094eba5b7 | -19.78697 | -58.02658 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f264349c-fb58-3237-a0c3-f17e86c1f366 | -19.75164 | -58.02406 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 541a1dc8-0641-3b31-9f29-d8859b14209a | -22.13439 | -56.31424 | 2025-11-11 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd53593b-3bad-3477-b4e5-cd6099758c63 | -19.7939 | -58.02789 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| f5d93212-0435-3d46-9f04-f58cebb8d137 | -19.81946 | -58.03582 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 328b9040-1fc0-3220-be53-20e01cfc9cea | -21.42373 | -47.68097 | 2025-11-11 04:55:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 96c93595-bac6-3ba7-942b-0e8099eddaec | -19.81877 | -58.03985 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| faccb322-3042-3d21-be09-ad05cc9646e4 | -22.66267 | -54.8774 | 2025-11-11 04:55:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 29496d2c-43c1-35a7-b18c-571f58fc5adf | -19.76478 | -58.00988 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7400073f-b38e-3322-84e8-e0dfef63102b | -19.79458 | -58.02384 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f0a6e5ad-8f2b-3a96-9013-5ffe6d01b2ca | -19.81469 | -58.03182 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 4da6fe21-3761-369c-a2c1-4b240c6b8bce | -15.55254 | -55.23196 | 2025-11-11 04:55:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fbaeaf1-4144-3afc-bcd5-04a9a3f23163 | -15.00932 | -55.68709 | 2025-11-11 04:55:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
