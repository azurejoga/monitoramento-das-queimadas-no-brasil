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
| 5275a134-1ea6-34db-a6e9-4e88755b6bc6 | -14.85294 | -46.79447 | 2025-03-05 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8e80211-c3c6-35d8-87c9-d3e55987c88d | -13.6203 | -44.43258 | 2025-03-05 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c13cfdab-3e2d-3d0c-9da8-839d7876f372 | -18.04001 | -39.92594 | 2025-03-05 04:08:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a0a7ec76-6473-39e7-a7c2-362c94f3d53b | -13.84962 | -41.39952 | 2025-03-05 04:08:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 24e95819-e681-3267-b8a8-9ce3577e3263 | -15.3791 | -43.7215 | 2025-03-05 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a946ad0f-8aea-3f1e-851d-8b1725b3de5d | -12.01015 | -43.79465 | 2025-03-05 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b96a80fa-9b78-3a23-bb90-06ef3ec88c26 | -16.7001 | -49.12653 | 2025-03-05 04:08:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6605f5a-0e9e-33a1-b186-f203fc2ab558 | -17.45573 | -47.00713 | 2025-03-05 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 653746ab-dc03-30c9-bdf1-3fe237265274 | -11.82888 | -43.81998 | 2025-03-05 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3c6fe03-7324-36d9-8280-8ebc95727232 | -14.08566 | -44.13895 | 2025-03-05 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89491ce6-5b07-3831-be3a-88c738f6078c | -15.0782 | -48.94473 | 2025-03-05 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b02aec9f-bd6d-3145-9e1a-28d30580c9d7 | -17.67491 | -42.74647 | 2025-03-05 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0eb8fba-48f9-397b-bd79-d75dd1dade55 | -17.79352 | -48.99754 | 2025-03-05 04:08:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ef1e8f9-1c14-38f7-a4a9-fac4497c68b9 | -17.4536 | -47.01965 | 2025-03-05 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c144a62-eb9f-303a-aaeb-a704293f2745 | -11.82496 | -43.82301 | 2025-03-05 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97bbc90e-8399-31fc-96ba-8288b363d7a8 | -16.82585 | -47.0959 | 2025-03-05 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1243dd3-6911-313d-97b4-8fcafaeb387b | -17.79256 | -49.00274 | 2025-03-05 04:08:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef1b33b-40ef-31aa-98c2-b3ed0c22c35a | -14.13481 | -41.69092 | 2025-03-05 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 243853f6-2cce-3fd9-baa8-ac594cfaa61a | -17.98075 | -47.22232 | 2025-03-05 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b3897dd-b663-345a-9558-b54c7dd2a43e | -16.68154 | -43.88438 | 2025-03-05 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b1128c0-ca31-389f-8194-aa5474e6c137 | -15.37636 | -43.71738 | 2025-03-05 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1ddf2848-eca9-34d7-a509-5e37175fa3a1 | -11.8283 | -43.82356 | 2025-03-05 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35f13bb9-9407-3166-a077-2ed93dcadf26 | -17.67547 | -42.74273 | 2025-03-05 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c6b5a8e-a232-384f-a4f2-c892f295c0ab | -14.90633 | -45.17745 | 2025-03-05 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d60591-d781-3bd9-8dd6-57a234dbd702 | -17.59599 | -43.19872 | 2025-03-05 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d4277e-e7dc-3c93-8c92-49e77f20e455 | -17.67603 | -42.739 | 2025-03-05 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fc58fe86-a7b5-3032-94f4-0ea6b975dc20 | -23.33763 | -46.7734 | 2025-03-05 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09a12e77-fc23-3989-b246-d4d2e7f3e27c | -23.58657 | -46.3951 | 2025-03-05 04:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 844d3b66-4483-3d1f-b6ae-4b30557aa0cf | -21.13469 | -44.91766 | 2025-03-05 04:10:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f7b31bc-12ec-3578-aea9-57cb4c048abb | -20.34663 | -40.36095 | 2025-03-05 04:10:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 46881818-abef-3da5-9ef2-cfd780f8fa9e | -20.91445 | -55.55392 | 2025-03-05 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dff5658-b465-305b-a911-1fb9da5fc185 | -22.90316 | -42.70326 | 2025-03-05 04:10:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b1869b5-ec3c-3d46-8a3c-a83098ea08ab | -22.96141 | -42.90372 | 2025-03-05 04:10:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dbd02435-91fe-3263-b0d5-5b2463e92a6f | -23.98312 | -48.91806 | 2025-03-05 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3abca7c1-4944-3d93-a5d6-4ce79e5d7570 | -20.00408 | -45.40353 | 2025-03-05 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d14c40d1-cc36-34ba-ad7e-e149814a480c | -22.87762 | -42.57768 | 2025-03-05 04:10:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 734c8402-2b96-3076-979e-ed5c0e9389c6 | -21.61669 | -48.47657 | 2025-03-05 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a33e0a46-d503-30d1-8761-d903711b990e | -25.09462 | -49.56484 | 2025-03-05 04:10:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c25c09aa-7bdd-307d-8959-5f278d14c71d | -25.10857 | -52.72461 | 2025-03-05 04:10:00 | NOAA-20 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d33495db-3501-3ebb-8ed7-9a2b1a448e06 | -20.91537 | -55.54985 | 2025-03-05 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7d7dd13-d62d-3d79-acf0-c2ba45414276 | -20.76319 | -46.76808 | 2025-03-05 04:10:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6142620-9ffa-36c7-ab9b-440150fa9889 | -22.79086 | -42.80682 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a61cfd1b-32e3-39ed-8ad1-e3e2186e0d41 | -25.61342 | -49.7155 | 2025-03-05 04:10:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ddd08573-9a22-33dd-a2f4-a6b037d1c2d1 | -23.1715 | -46.22886 | 2025-03-05 04:10:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b316b023-dc72-3dab-8632-ee5ef52cd6f6 | -20.0074 | -45.40415 | 2025-03-05 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1bc7998-7eed-3b5b-ab54-27d5aa2a1d01 | -23.40421 | -46.55713 | 2025-03-05 04:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc9176a4-d182-3094-b8ec-a9d9eb981cea | -22.77158 | -42.84191 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 406b1a57-b30a-3906-9fb3-c816db183fef | -21.09433 | -47.97901 | 2025-03-05 04:10:00 | NOAA-20 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42a7186b-c05f-37b7-be0f-56a6b313316a | -21.64958 | -46.42517 | 2025-03-05 04:10:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6474dc3b-9481-34ad-87ad-da697f64ab0e | -25.112 | -52.72992 | 2025-03-05 04:10:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7fd21a1-3ae0-33ba-a737-8d31dcb3f327 | -21.65021 | -46.42136 | 2025-03-05 04:10:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7d95a6d8-90e7-327e-82bb-b001c5cab01b | -22.84364 | -43.60026 | 2025-03-05 04:10:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0ed5ea5d-591a-366e-add6-f6f8e2063b86 | -20.91706 | -55.55045 | 2025-03-05 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db02adfe-e59c-314b-8f81-4ff2a7e87c44 | -22.88114 | -42.57825 | 2025-03-05 04:10:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db799205-3162-3704-9dc3-490ba4e4f2ca | -20.7307 | -42.70424 | 2025-03-05 04:10:00 | NOAA-20 | SÃO MIGUEL DO ANTA | MINAS GERAIS | Brasil | 3163805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 131f79e8-cbcf-39bb-8160-3c23f32f53d7 | -22.85647 | -42.98119 | 2025-03-05 04:10:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe68e50e-ada0-3e71-887d-37e061f8a296 | -25.10765 | -52.72918 | 2025-03-05 04:10:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6215ff78-edf8-3bd3-b730-d337023c4cec | -22.84418 | -43.59655 | 2025-03-05 04:10:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ecf7d6e6-fdf3-36d1-82d0-af8c3a187750 | -22.68306 | -42.85414 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 45cb64f6-52de-3930-9169-b397ca825f90 | -23.73155 | -47.42266 | 2025-03-05 04:10:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 843be2c7-109d-3ed3-a89a-e590f426692e | -19.63455 | -47.15779 | 2025-03-05 04:10:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9f7e945-aeb3-31ed-a691-a66a77ab3c4f | -21.91196 | -42.26347 | 2025-03-05 04:10:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 571a2602-3b65-3bd5-821c-a0e593f70328 | -23.27282 | -45.91854 | 2025-03-05 04:10:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a47325ae-4701-3f77-b7a4-a0408fa8a4cd | -20.29083 | -50.97644 | 2025-03-05 04:10:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 36ccc72c-32e7-3dbc-bdf9-2038ada03838 | -21.61308 | -48.47587 | 2025-03-05 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d121d05-f62e-34e5-84f8-1095573ba4a9 | -20.28156 | -50.97884 | 2025-03-05 04:10:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 611c7af4-4618-35d5-b873-023dcebbb9fd | -23.59154 | -47.43864 | 2025-03-05 04:10:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d4f0dbf-c946-3900-8fdb-1ecabee92cf5 | -22.67373 | -42.86954 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 829135c5-9720-3b4a-9a88-cf77b36a9957 | -22.77217 | -42.83776 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5db6e2c5-44a8-3224-bffa-f1878409d874 | -20.73128 | -42.70024 | 2025-03-05 04:10:00 | NOAA-20 | SÃO MIGUEL DO ANTA | MINAS GERAIS | Brasil | 3163805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 223d840a-c08b-3c48-918d-e61a9dbe6562 | -22.33066 | -45.90121 | 2025-03-05 04:10:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1af7638b-07cd-31ed-9adc-814fa191391a | -22.76868 | -42.83719 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6469fac0-8e08-38ec-9e79-ba3f26998c43 | -23.86731 | -46.92473 | 2025-03-05 04:10:00 | NOAA-20 | SÃO LOURENÇO DA SERRA | SÃO PAULO | Brasil | 3549953 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ea8687a-865d-35cc-828b-8cf4b251e9f2 | -19.37799 | -46.99947 | 2025-03-05 04:10:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38b071e5-602e-3e9f-b94b-545e1a04189c | -23.20092 | -46.40592 | 2025-03-05 04:10:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 66f117d5-8276-307a-b66b-540efc3bbf9f | -21.19631 | -44.93613 | 2025-03-05 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2b556196-0356-3982-9d42-032d8bce0a1a | -22.76879 | -49.32864 | 2025-03-05 04:10:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c936c7-44d6-3598-bd16-2dd438a04d80 | -22.91666 | -43.29023 | 2025-03-05 04:10:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3493440-7446-3839-8dec-f11d018a64e7 | -22.68017 | -42.84943 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8c46c5f0-193c-32c2-9d56-10eacf5984df | -25.21968 | -49.34909 | 2025-03-05 04:10:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39f45eba-e523-3553-a4ab-93ee25b69269 | -20.72972 | -45.24396 | 2025-03-05 04:10:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d498c4d6-bc35-3e86-8eb0-2b7f6859dd3a | -23.20154 | -46.40212 | 2025-03-05 04:10:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 3ba88d0c-2969-3d59-b209-b95657dba4b0 | -20.2866 | -50.97553 | 2025-03-05 04:10:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6fdb9424-6e31-3884-b448-3d59c83729fb | -20.91617 | -55.55451 | 2025-03-05 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd27f6b6-ce00-37b3-bd99-1fcf9f5dbc81 | -22.67491 | -42.86127 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f8633146-ca1d-3135-be44-dbae8323303d | -22.79145 | -42.80268 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d2655ae-cb89-324f-be19-e405fe073d95 | -20.28579 | -50.97976 | 2025-03-05 04:10:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| ef254e92-9517-3a1a-89be-c085df8bc84d | -22.67432 | -42.86541 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0af8b84c-24c4-3ec0-a654-5b19bc812ad0 | -22.67958 | -42.85357 | 2025-03-05 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 4fbf7065-fb64-31fb-90d8-adff160ae1cd | -22.75197 | -43.26753 | 2025-03-05 04:10:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8454515c-c7d0-34d9-914d-8e02b3a46b61 | -28.58401 | -49.44053 | 2025-03-05 04:12:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 075a98cb-1a3e-32f1-ad2d-9a4bd9a614da | -28.9827 | -52.19129 | 2025-03-05 04:12:00 | NOAA-20 | PUTINGA | RIO GRANDE DO SUL | Brasil | 4315206 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8ff3691-6a42-365c-89d0-d36f66c1d574 | -29.07887 | -49.60802 | 2025-03-05 04:12:00 | NOAA-20 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 36b18c68-2a59-341a-ab36-f9aa86921bd4 | -30.49453 | -51.83332 | 2025-03-05 04:12:00 | NOAA-20 | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 7.8 |
| 1a41990e-3435-3b71-bef3-4b1bb4e299fc | -29.77809 | -51.17476 | 2025-03-05 04:12:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| eca99a83-3b56-3330-a466-38ade12e06f8 | -27.70768 | -50.62477 | 2025-03-05 04:12:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a34a5b5e-6056-3dd3-89cd-44da574911b1 | -26.98779 | -52.2114 | 2025-03-05 04:12:00 | NOAA-20 | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c3a7331-87ba-3389-ab20-6cfe4456c802 | -27.70403 | -50.62386 | 2025-03-05 04:12:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2344e71f-ecc0-3d72-8392-1d0b1c279ecb | -26.9877 | -52.21255 | 2025-03-05 04:12:00 | NOAA-20 | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 84d4595f-3724-386d-b6f3-a21141dcb247 | 2.35067 | -61.00666 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README4.md)
