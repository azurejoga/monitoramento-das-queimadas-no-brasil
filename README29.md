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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c3ff7b6-128a-3eed-b120-aa4702fdeb58 | -10.9374 | -54.08955 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a3474f-f84f-3ff6-b09d-f2915bd3c656 | -12.50956 | -45.92117 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 052cbf9c-5e8c-36d9-80d8-98acf1d1a028 | -15.03919 | -48.56093 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebbe3421-f9d5-3d86-b1c0-26083161f115 | -12.3867 | -51.41399 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3e7a4879-58ae-3dba-9213-96b3c46f5ad5 | -11.97711 | -52.46867 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1772539c-41dc-3b73-af07-9c762ca8502a | -10.69854 | -54.17477 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15463b5f-c7fe-3ed2-bd8d-5ac40a8ebcc1 | -12.32863 | -47.96154 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e50dc96a-7576-391d-8b2d-f867ec9f32cd | -13.74254 | -43.75557 | 2026-09-16 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a51b3321-7db6-37ec-8677-1cbacac7fc99 | -17.54576 | -49.42503 | 2026-09-16 04:17:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49b6f347-5da3-3476-a31b-f8196a4db61c | -11.97646 | -52.47211 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0c78434-4302-3e2b-90d0-5811972dffec | -15.28859 | -42.79778 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acfca37c-fead-30a8-982b-fcfff501fbe4 | -13.65223 | -47.90445 | 2026-09-16 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ee935c1-43ee-3481-8b95-70a4cbca5a20 | -13.7498 | -48.7909 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62f60e9a-0350-3f59-8854-8363b59958dc | -16.95648 | -49.71027 | 2026-09-16 04:17:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34450be5-bb8c-33f9-9588-fb4db27664c8 | -17.04023 | -41.28643 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| f3b09b60-2f19-3c87-9563-ee2ba81adda2 | -13.22793 | -51.63491 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 98146c34-f2cc-33cc-b550-552d6fe35105 | -15.53949 | -53.86065 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cc4e7ef-d594-3754-9aad-aaded0d0dc93 | -12.51607 | -47.15388 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1088ad44-ca42-3815-bb67-77fa03ddfcfd | -10.99153 | -48.31604 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee363e9f-42f6-311f-86a8-30fc05566239 | -17.59221 | -52.49834 | 2026-09-16 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7784cbb-7ea5-3c67-96cc-4a4d9690929a | -15.28689 | -42.8087 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0a39c101-d07c-3a6c-b756-c9d6e913f983 | -11.31946 | -47.23838 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36b31600-7760-33e4-ab53-c04b8fb9dff0 | -13.5541 | -43.53122 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a04938fd-591a-3d68-b057-aae7733f9c0f | -15.53402 | -53.85944 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88de375d-1866-39c8-8d5c-d4b5f96d10bf | -11.98431 | -52.47446 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9aec597-09fe-38b1-a662-14f4fdb151d0 | -11.3145 | -47.23534 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b123c675-22fc-3987-9583-438359a8f3be | -11.19336 | -46.3036 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99861c4b-d0a3-3d8b-9faf-a8847732eee0 | -14.13132 | -44.38123 | 2026-09-16 04:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce2d4bb0-786b-37d3-97fb-b7b14dec045d | -11.88589 | -43.82635 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b2d431c-0ad2-33a6-abd3-1b6b91ac6a2f | -17.03674 | -41.29158 | 2026-09-16 04:17:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6559d686-0f0f-398c-aa30-e92706e27cf9 | -10.91007 | -48.36523 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 439f6c83-56c3-3a28-be41-2a4e5f5ec0ff | -12.38689 | -51.41588 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b0bc78a-7f71-36ae-b1fc-bc6e7c0fb136 | -15.03523 | -48.56033 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 822ca056-47b0-3906-ae01-68c8bd4d8a3e | -12.32467 | -47.9608 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d2a8854-9b5f-3c1f-9a1c-9b3b787e2637 | -15.28523 | -42.79732 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d91efc68-ee4c-33e8-919e-b21094303fd5 | -12.62126 | -50.78765 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6fe4a7dd-b338-384d-9065-fb3a4dbcec13 | -18.22953 | -41.24827 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 08edc137-9683-327c-9305-a6b0317e2644 | -12.54519 | -47.09961 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8a1a2951-4632-34aa-8405-d9aa8b4ddb77 | -18.22236 | -41.24691 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 681f1d02-95e1-38f6-8162-8731b4241149 | -11.21638 | -49.95282 | 2026-09-16 04:17:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84e6b5a9-507d-3303-9675-95da7cbb2cd1 | -13.7685 | -48.82693 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e560dfa0-c7b0-3360-a030-ccf5ec168641 | -18.22313 | -48.15654 | 2026-09-16 04:17:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eef3a1ba-66e5-3b4f-9d3f-9a1dd9c1f7a2 | -12.71602 | -43.20516 | 2026-09-16 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45d04410-4e42-367e-8dbc-51d3c34b66ac | -11.34609 | -47.31361 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56cc36f8-5c4a-348b-99f0-cab96a15b6fc | -15.49861 | -53.80976 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf2c4ac-144f-3ea9-8408-1a6f988d6fed | -14.60488 | -42.14558 | 2026-09-16 04:17:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 57a225fc-76e0-3061-a197-62b025ac207d | -13.75107 | -48.78725 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c684222-6116-35a2-9212-4564a54890ea | -12.62599 | -50.78859 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e79def8d-6fff-342b-8c19-e84096786350 | -15.28299 | -42.81184 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d215048c-eea0-3574-bbf9-1202ac0424da | -11.97896 | -52.47339 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d5b792c-c397-364a-a736-d9a786b5c6ac | -15.88965 | -40.22285 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| eb1f7b93-8aba-3cab-92ae-ffd8b3fdd2c9 | -11.31369 | -47.24014 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dac0e556-67c5-312e-affb-3e8d8784229a | -14.66216 | -47.99065 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f1daab8-a934-38cb-9155-895bde23d756 | -13.3469 | -46.30812 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1bb58ab-02e8-306e-81f7-a7fa74148fb0 | -11.19237 | -55.02946 | 2026-09-16 04:17:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d80a0b19-b8cf-39b9-b497-09a80923bde9 | -15.49332 | -53.80798 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e809b70-513a-3133-b225-9d3e3dd61d8e | -11.34224 | -47.31282 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59e8112a-994f-3eea-ab3f-0e9f3dc30cf9 | -12.54062 | -47.10356 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af3f0c43-755e-3692-bbd6-6d9a1204fb34 | -15.29409 | -42.78419 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e926faec-bd56-36fd-a9e3-989cf55a1080 | -14.22842 | -48.51228 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d83cfa9e-766b-3817-84e9-1ee8bce89441 | -12.52992 | -47.11802 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fa5ac51-35f1-3b45-b8cd-d053d51cca45 | -11.88531 | -43.82991 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f6dce79-6e49-3ef7-8563-537ed2666b7c | -12.85192 | -44.39227 | 2026-09-16 04:17:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b07c865a-5916-38c3-a5db-528705bbee12 | -11.53807 | -46.85492 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a943fb-0b64-336e-a902-875d8549e597 | -10.69193 | -54.17653 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d07d4bec-cbb7-3c8a-a82e-cc3cb9fee0eb | -15.27014 | -42.80634 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da918072-ed22-3362-a125-1aa203a17ece | -9.93641 | -53.99161 | 2026-09-16 04:17:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70754767-911d-3a0c-a845-eeb4bd31b4d3 | -11.89313 | -43.82389 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 39166d6c-62c7-36d7-b07f-d9a9182035b0 | -15.2457 | -49.1081 | 2026-09-16 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9235c0c9-77df-37f4-9ea6-e64c8c9c90a5 | -12.83007 | -39.76498 | 2026-09-16 04:17:00 | NOAA-20 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14da0fa4-b19e-3594-85f6-ee9c902ecc01 | -13.55472 | -43.50591 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 23d22a3d-cfec-326e-baab-91b98648d246 | -14.13648 | -44.01091 | 2026-09-16 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2197f17b-dcbe-3b8a-8a3b-489d651efdb6 | -15.2707 | -42.80273 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75a9f3af-bb6c-34c4-b122-6dc77022475a | -17.03379 | -41.28691 | 2026-09-16 04:17:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9f92312-2c3b-3adc-b111-4e33ceae2337 | -10.6976 | -54.17949 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 593e310d-7fba-3e87-98f5-ffb2594f0352 | -12.71306 | -45.61679 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46075a9b-d4e9-3546-a39c-22454ee34a7b | -11.19128 | -55.03483 | 2026-09-16 04:17:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d16005c3-f87e-36f7-89d1-42a65b5f6d35 | -13.55741 | -43.53197 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 530dbe9f-e860-394b-a901-784445473e35 | -15.03823 | -48.56631 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b63c568e-c155-37f2-8504-7278c979e5e6 | -12.32558 | -47.95567 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15a22212-a295-38c2-84cd-97a70f6d1017 | -11.97816 | -44.93017 | 2026-09-16 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 515112d7-b2fb-39da-b926-c27a7b8528f3 | -12.52023 | -47.10667 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81bb26d5-5245-3def-a17f-078f9c0200a8 | -14.12798 | -44.38067 | 2026-09-16 04:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 183ad928-d9db-32b3-94e1-d0725055dc39 | -10.90521 | -48.3684 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4052df0-9109-3847-877b-f17e5a86cfdc | -11.88704 | -43.81922 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65a32423-c6ba-3ac8-9fb6-4a16785c7511 | -21.06721 | -48.5638 | 2026-09-16 04:17:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7f68a7d-c2e7-34bf-8ec6-a949cfa5b909 | -12.47271 | -41.41471 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 235e6636-0c84-3526-a42d-c155a288f719 | -10.86889 | -50.81519 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a4714b1-b5ed-3fa1-ae7b-535659bd0a01 | -11.48541 | -45.79869 | 2026-09-16 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8032b20e-b12d-3450-8b57-3d5e4ef1afdf | -11.44328 | -49.76989 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af824790-58dd-393f-9473-ebfe02e8e9b5 | -12.82987 | -39.76635 | 2026-09-16 04:17:00 | NOAA-20 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42a7a860-267e-3793-b487-d124402d1b56 | -10.86736 | -50.81363 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b7bda90-3fe3-3689-816e-5f0af7abe685 | -11.41426 | -51.42979 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34bf0b09-4d51-3690-8edf-31a1e21e4c74 | -15.50277 | -53.84576 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 308e8613-0a66-336a-9b4d-7358b293f904 | -11.88807 | -43.83403 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bfd9704-e4e0-3cbf-b4ff-b73630536829 | -15.24503 | -49.11174 | 2026-09-16 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 649000c4-c64d-3722-a509-cb8c2b3e1f01 | -15.89381 | -40.23564 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 600a4736-80e0-316a-b6b6-d4e6a831acd5 | -17.0403 | -41.2921 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a61e4b17-80b0-3ed2-86a0-2d8d636e0dc6 | -12.53071 | -47.11334 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1361cf66-a8a9-3bf4-a4d2-724a1f84e50e | -15.63712 | -39.80276 | 2026-09-16 04:17:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
