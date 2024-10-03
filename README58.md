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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec90722e-8e21-3150-94d6-01b0d0983db5 | -20.14201 | -43.82238 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f651485a-1e86-392a-b11f-d5cfdb79b51f | -20.1415 | -43.85317 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 811fdec5-5bda-380a-bf41-bef2253abe02 | -20.13832 | -43.82032 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 11c6005d-1a5a-3ca4-a581-6b380bd261d7 | -20.01744 | -44.50832 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2d0638f8-2e47-3a96-ae60-fa8a3e4dedbe | -20.01599 | -44.51427 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2aa7bcd7-ac39-3c59-9c15-c4ab35ee0fa6 | -20.0111 | -44.50574 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8c0b1b63-867d-313b-a900-efb192021c32 | -20.01085 | -44.50569 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 462cf05e-f3ef-333c-be52-a4fb75af7cc1 | -20.00969 | -44.51168 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| f34241aa-98e0-3a98-a834-e3b25d2d9cfd | -20.00939 | -44.51161 | 2024-10-03 03:15:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 86477a79-d173-3976-bf2c-9e8439606952 | -19.75409 | -44.25755 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f70d35c4-e8a3-304b-927e-545be4ffcae5 | -19.75264 | -44.26352 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 37d3ef23-ef3a-321d-9b96-fa00fd885d43 | -19.74748 | -44.25519 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 34034584-e38a-38b0-8901-226e7a6b2d45 | -19.74716 | -44.25637 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af643193-945b-33e8-a334-0eac771c2eb1 | -19.74582 | -44.26207 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aae75ab9-84db-3aa5-9739-7d63cc8f2b86 | -19.74551 | -44.26334 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d582b01b-6879-3641-a5e6-61d46743bd38 | -19.74417 | -44.26885 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 680c41a5-4b9f-34c2-8fb9-b91e2541cf42 | -19.73869 | -44.26186 | 2024-10-03 03:15:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ffacbd65-f959-39ec-8d3a-955d66dd4b9a | -22.31326 | -44.06803 | 2024-10-03 03:15:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 787bfb55-a273-3cec-944a-519add1698d8 | -22.31164 | -44.07471 | 2024-10-03 03:15:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f2df6da2-07a0-3877-914a-fc2d5b53bd22 | -22.30009 | -44.06648 | 2024-10-03 03:15:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2830aaae-798b-3303-9347-0ce537243728 | -22.29874 | -44.07201 | 2024-10-03 03:15:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5339df56-cc48-3515-8639-29140e4b2664 | -22.11656 | -45.09686 | 2024-10-03 03:15:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a365391f-4646-301c-9ff7-427b7e5e5df7 | -21.56242 | -43.97458 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a396521e-4361-326f-92c7-032055caf7d1 | -21.45045 | -44.57613 | 2024-10-03 03:15:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e7f170c-ba6c-3f90-b1ca-eae005244345 | -21.44873 | -44.58317 | 2024-10-03 03:15:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67c5224f-aeea-3668-b525-c1b2e3ce9886 | -23.1491 | -45.13552 | 2024-10-03 03:15:00 | NPP-375D | LAGOINHA | SÃO PAULO | Brasil | 3526308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 234a5fe1-2d16-38ab-ad39-0b0b308cf6b0 | -22.62339 | -44.65737 | 2024-10-03 03:15:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7a4d9f99-b275-3825-9259-dae42cbff59e | -22.62206 | -44.66273 | 2024-10-03 03:15:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9996321e-a337-3658-8261-1e0390a10e7c | -19.72434 | -45.07576 | 2024-10-03 03:15:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3ae69e2-6941-3c2e-9f55-2c82bdb30865 | -19.72261 | -45.07265 | 2024-10-03 03:15:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23445138-fc63-39be-a158-912a0d0dc2b3 | -19.72066 | -45.08062 | 2024-10-03 03:15:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 945444d5-14d4-33e6-a2fe-941a65dc605c | -19.71743 | -45.07334 | 2024-10-03 03:15:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a01779e2-b19c-3936-a6be-75bcbcd2f06c | -17.85263 | -41.42763 | 2024-10-03 03:15:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 21c4d83c-706a-337a-b4d5-e618968422a4 | -19.43504 | -41.36308 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b027cf43-74e6-37f0-a56f-6d32535a8c7f | -19.43248 | -41.35221 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 833f5b23-2380-3945-9785-d7b18f059891 | -19.43176 | -41.35553 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c60575d9-0d66-35a9-a996-2fadae79b557 | -19.43109 | -41.35353 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1e5fe0d1-568a-397a-8d89-4b58935cc511 | -19.43034 | -41.35683 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e8004707-354a-3d51-b142-a5fa25b93270 | -19.24644 | -40.62739 | 2024-10-03 03:15:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b55a946e-ed48-3772-bd77-c9a02d9a0206 | -19.24553 | -40.63165 | 2024-10-03 03:15:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b56c24c2-de9a-3ebb-bc2a-c19528d59db5 | -18.91189 | -41.27843 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 91e5416f-482e-37d0-86d8-5aa46dde963b | -18.90179 | -41.21426 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2ee23240-a9fe-3d4b-8732-b66f0250262e | -18.89795 | -41.21165 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 625bbdc0-c7ca-3a2d-8373-e76c457de953 | -18.89697 | -41.20856 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0859c56f-fcf8-30e3-b0d8-c14faf96e9ac | -18.8961 | -41.21242 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 886f4ae5-1c24-3aef-8cd4-e4d6e6afa680 | -18.89218 | -41.21016 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e4ce38f1-98e0-3a5f-a2fb-96770442ee3d | -18.89132 | -41.21414 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 107f4997-ad55-3a4f-a3cf-01044c8c0b97 | -18.8904 | -41.21833 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b3eca1d4-e8e6-3d88-bd0e-c8d4052e003a | -18.89031 | -41.21104 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 52fe8974-961a-3c90-8056-10d4c68b5e33 | -18.8894 | -41.21507 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 2e2b57a5-a74c-35d4-af9b-a17cc8bee3a1 | -18.88847 | -41.2192 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6176e978-46ce-3187-b0ab-9a8d22e82c3f | -18.88748 | -41.2236 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 360c9c8c-7d35-314b-996c-a0617b9155e1 | -18.88567 | -41.21207 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| a55f5bcf-0007-3b3e-a1db-34b8336f0edb | -18.88481 | -41.21597 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6202c9a0-9391-3b4b-901a-a53722097645 | -18.8839 | -41.22017 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e57c6904-1fb0-3f1e-a0fd-05c53ceb4494 | -18.88355 | -41.24981 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83365008-9998-3f76-a991-ca8bacd13c0c | -18.88282 | -41.22513 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 36a09cac-bd4c-3afd-bc0b-1ba782403e32 | -18.88231 | -41.24659 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9794165e-43a1-3992-9f87-81acfda66134 | -18.88142 | -41.25053 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ddba5e1d-aded-3a52-852a-2bdf04f0c1b9 | -18.87849 | -41.21698 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3b819b53-8b3d-35c9-9b2f-e39f86921d74 | -18.8778 | -41.24812 | 2024-10-03 03:15:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fea5c8c6-f488-335d-8fbd-de2d8e0bc150 | -20.81749 | -41.62099 | 2024-10-03 03:15:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ad62baed-bbe3-391b-825d-30f08d1845c8 | -20.81638 | -41.62589 | 2024-10-03 03:15:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ef6caa2e-0413-3d78-8b8c-cadf86ca9c5e | -20.65479 | -41.99786 | 2024-10-03 03:15:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7059fcb8-b417-3f8c-832f-017ff0dd381f | -20.65308 | -42.00549 | 2024-10-03 03:15:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9cc43be3-ffc7-3ba5-b068-4783c771397a | -20.64851 | -41.99829 | 2024-10-03 03:15:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| de1d0d34-ec2d-3c4d-8de0-1801e7fc1ee9 | -20.64718 | -42.00417 | 2024-10-03 03:15:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b4fd7708-a10a-3723-9c51-f79fd61b2a8d | -20.43791 | -41.99834 | 2024-10-03 03:15:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1ea1892b-4a3e-3da6-94c0-9fd96bf506cf | -20.15355 | -41.87198 | 2024-10-03 03:15:00 | NPP-375D | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d0982cc2-f251-319b-95c3-bf5cea7a42c1 | -20.15112 | -41.86966 | 2024-10-03 03:15:00 | NPP-375D | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8296f0ee-8eab-3386-bbc8-21b6656575d6 | -19.89 | -41.40423 | 2024-10-03 03:15:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7bc6dde3-902d-3ec1-b4d1-be1a16b759eb | -19.88908 | -41.40837 | 2024-10-03 03:15:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 47c83285-c30e-3f47-bcdc-4892fbd93557 | -19.74615 | -41.67162 | 2024-10-03 03:15:00 | NPP-375D | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 438378e8-1551-38fb-b1d5-4d05a65f3e2b | -21.56054 | -41.24054 | 2024-10-03 03:15:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 15db9d69-b2b7-3eb4-85c9-e2a873e16296 | -21.55968 | -41.24439 | 2024-10-03 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 24481a78-0bc4-3e7a-8508-0c19c0f7ff79 | -21.55679 | -41.2313 | 2024-10-03 03:15:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bc3c32bc-575a-3831-a3bb-653bad6bf8b5 | -21.52779 | -42.05252 | 2024-10-03 03:15:00 | NPP-375D | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf533543-3c86-3d68-80c3-baf22141a3c1 | -21.52764 | -42.05817 | 2024-10-03 03:15:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 807e29f1-e3e5-3cbb-ad61-1565553c56f5 | -21.52348 | -42.0495 | 2024-10-03 03:15:00 | NPP-375D | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 71e2505d-eeee-3a39-b580-6b81cbfcfbc7 | -21.52259 | -42.0486 | 2024-10-03 03:15:00 | NPP-375D | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1bb6cd54-3992-37b0-89b4-673a9420677b | -21.49131 | -42.13734 | 2024-10-03 03:15:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a1eac77-39e8-30c1-8360-eb8a4ab3200d | -21.49029 | -42.14185 | 2024-10-03 03:15:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 548d1c2a-1240-36ab-9a8b-15816b7344ad | -21.48556 | -42.1356 | 2024-10-03 03:15:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dcdaf65c-361b-3bf6-9d2a-83b582b64efe | -21.31768 | -41.40707 | 2024-10-03 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4612fee3-4f01-3245-ac89-2bd89a38d864 | -21.31284 | -41.40232 | 2024-10-03 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ec9398f-5fd7-3367-a2be-77aa485b8a97 | -21.31194 | -41.40635 | 2024-10-03 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e7628a5-42b8-38ff-b177-fd4dfecf2917 | -17.3315 | -42.50452 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7036339b-8eed-362d-bab0-2807b0aa520e | -17.33066 | -42.50408 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a806802-1b7f-306e-8959-c8581da92a91 | -17.32943 | -42.50946 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3b7b48f2-987e-3f92-b5b8-cf18d37dc619 | -17.32512 | -42.50276 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1a6d9d03-cbfd-31e4-8224-684d4d485703 | -17.32428 | -42.50232 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 291ef061-7400-3c13-98bb-7770cc1e493f | -17.32387 | -42.50842 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1b504c9f-b376-3f3e-83df-50a4057881d0 | -17.32298 | -42.50799 | 2024-10-03 03:15:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2cfbd928-b14e-37fc-9d8d-331a55d1dcc3 | -17.61782 | -41.97526 | 2024-10-03 03:15:00 | NPP-375D | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16e317b5-ef17-353b-9aca-5d3471f84a7b | -17.61675 | -41.98005 | 2024-10-03 03:15:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07852b1f-69f9-3550-9b09-1e419fd4f3eb | -17.6106 | -41.97835 | 2024-10-03 03:15:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c4781d62-f14c-312a-9f10-70b93a755e33 | -19.50308 | -42.32232 | 2024-10-03 03:15:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d3e8d872-244f-377a-ba54-336556efa2b9 | -19.5015 | -42.32911 | 2024-10-03 03:15:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 756dcea9-7045-3e51-b56a-05928cff0c63 | -19.31332 | -42.60089 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 800828c3-aee0-3608-a5cc-ef22e8eb750f | -19.31189 | -42.60714 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |


[Clique aqui para ver as próximas entradas](README59.md)
