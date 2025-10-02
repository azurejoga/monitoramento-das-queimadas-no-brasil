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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79a2589d-16c6-3df6-b72b-c362daddf2a9 | -15.35954 | -47.06592 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b21f8dc9-7d2d-371a-ae1d-57110bd0687b | -15.02511 | -55.27806 | 2025-10-02 04:32:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3feb7a5d-1ee3-383e-b3d6-6dfa77d26786 | -14.44747 | -46.34623 | 2025-10-02 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 902eeb58-fd5b-3bae-93d5-91c855a3b76f | -14.31243 | -45.92107 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da7e0920-3967-36fc-9eca-c71788c62600 | -17.56033 | -44.80341 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53d5231c-8c81-3156-98b8-f4c4500ff3f6 | -18.17863 | -53.2831 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb12ea35-c01f-3a80-9149-2a7c1ae52187 | -14.35581 | -45.96373 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e26db4c5-86a6-361c-903a-aa757be145e5 | -13.16283 | -47.80668 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36152c21-c493-389b-84c0-0de6ea4c2801 | -14.31877 | -45.87819 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0a510d2-02d3-3a88-add2-e56bcf73a54c | -15.18675 | -46.40723 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c083ab4-e952-3dae-ac6e-bd5943de9d80 | -13.36479 | -46.34244 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0766f1d2-6b95-3178-a39a-0fdd0cdd9c9b | -19.71879 | -45.88424 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 180ebe7d-9a8c-3523-9f4a-ee791767184d | -13.94262 | -48.09092 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a16f7641-80cd-3e5c-8692-399d26573c97 | -13.2953 | -47.24479 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34f60a7e-ada6-3063-9d72-d220151c1814 | -12.62794 | -44.85619 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c30ba275-7555-3537-b533-7f79cfbeb4c4 | -13.19831 | -47.84164 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6960d13-4c09-37e9-b42c-42cd71c67881 | -13.16006 | -47.80259 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47de7f41-c106-303b-b3ea-4c37a6ecb168 | -14.59375 | -46.71778 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d33620c-1723-3a69-9d11-2e3f7127fb76 | -14.20946 | -46.12343 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b0a0f7f4-642b-3c62-96ff-a62435c10645 | -12.6783 | -48.57056 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d7afbb0-10a1-3c3d-8a18-0274ef1ca5ed | -13.79219 | -47.9973 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81552d9b-ee1e-3237-92a4-dd237020fb28 | -13.5364 | -47.24994 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e58e4e81-5199-31df-a292-68082081c462 | -12.89655 | -46.9168 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1e99899-6f04-3f57-b5e1-259679acf3a0 | -16.13814 | -46.6847 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35fe6891-bc95-32be-83ea-994be7ec8ff6 | -12.65423 | -46.95184 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48314d3c-9601-3485-9a52-1b05a0fa6841 | -19.25946 | -47.34927 | 2025-10-02 04:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49e0edec-9662-30b0-9862-29f884ed7b0f | -12.68397 | -48.55676 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96cfc7c6-56fb-3c4a-9e99-624b6da1540b | -13.30736 | -47.83442 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7901a81e-69a5-38af-91ba-a56208063dfe | -14.04268 | -47.99793 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89c1b0fe-61af-30e8-8da3-8501f54d83b0 | -19.71816 | -45.88881 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2dbb0bd-20dd-34b0-8321-9c99e3f926fd | -13.469 | -47.2321 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a40a0bf-0f35-37df-9df6-be53be0286a5 | -12.81415 | -47.02808 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 517e5c55-c41e-339b-8b41-c752581dd42c | -14.65485 | -48.12436 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84c3f407-e0a1-3964-87fd-4c9db5e0beba | -15.41175 | -47.04737 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b09c7e68-8581-3e0d-a4b4-ae8fcdae3aa2 | -14.88766 | -48.3161 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff0532cf-d1dc-3ced-a801-8b9689df2364 | -14.42071 | -46.13123 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53777660-6f70-35fd-9abe-38a57443d4ae | -17.08763 | -47.11259 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cf9b5277-3be5-3f52-9143-f2dc509fee4b | -13.22867 | -46.43545 | 2025-10-02 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9777f06b-67de-3da2-ab34-36f6588a0d87 | -13.15723 | -47.84217 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2dc7915-5dec-314b-9f16-3510eb335f88 | -12.87648 | -46.93557 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e80a06d-6bad-39ac-a17d-1bdb5be83e87 | -11.8292 | -48.06893 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f25a52e-de96-3951-ac6d-2832dd6866e7 | -16.03761 | -50.91745 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3939531-8350-3e59-a56f-575686da4a7b | -14.40231 | -46.08877 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe090dac-53c0-3bf5-8920-af5832bd1612 | -18.50342 | -43.39695 | 2025-10-02 04:32:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 77da8099-0782-313c-9499-6c971a463779 | -15.23069 | -50.12089 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46cbfec6-5c00-3e1f-b8e8-559e7b409566 | -16.0408 | -50.87724 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 669e73c2-9ab6-334b-9ee9-547264665371 | -12.67379 | -48.5772 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3834603-509c-3be0-80e2-6fa3e172252e | -13.69567 | -48.6249 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb717ce3-ccd6-341c-b829-b374bb5f8a2b | -14.66207 | -48.12189 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae8617b-a050-37dc-b8e3-bf3e84968834 | -18.43121 | -46.53717 | 2025-10-02 04:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a153be-e84b-3c1d-b3f8-376baca07d39 | -12.94884 | -46.94358 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c1bbaf0-dd6a-3986-a3a4-ae0d3b46abea | -12.49689 | -50.25507 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5d8ab91-d014-315b-ad9a-6e8d2243016b | -14.61035 | -51.3351 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 291b5cc7-8a80-343a-b956-2e303ae3181d | -12.77537 | -44.91181 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb5580c-1e71-3ba2-96b4-ef7b4dc740de | -12.81032 | -46.90677 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d84e9ab-b773-38b6-8ba8-2bf20c9a93df | -13.24583 | -47.32069 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06d1053d-dfe6-300d-9025-b039dac31ddc | -19.59336 | -42.47561 | 2025-10-02 04:32:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7ac2f03e-2afd-3bff-996c-12b707ba3734 | -13.47342 | -47.24778 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8082d0-47b1-31b3-90a1-280e90a95d42 | -13.31312 | -47.19634 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01d3f9a4-5d3e-3a2b-8e02-98dc16424e15 | -14.86552 | -48.29085 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ba88716-3a3c-3afa-9f5a-c1105761d9e2 | -13.86542 | -47.95791 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38a767c0-9130-3349-addb-351e0e4c243f | -16.41067 | -47.05015 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03618088-9ed1-37e2-b184-dc5bf0a6757c | -14.37257 | -45.97031 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf4e2616-281b-3c9e-b5c7-045a6dc00ba1 | -13.05971 | -47.0162 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46baa44c-2586-35d6-b748-baa2a441ae62 | -12.58715 | -49.89003 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84276e58-d33b-3f91-82c3-ab0695ac1bd9 | -14.3393 | -47.1303 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ed19aef-1079-3c82-a70d-cdeb0014b5dc | -16.04475 | -50.85378 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b1e318c-e5e2-31dd-974e-54c563792f95 | -13.40226 | -47.55098 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31618111-ab47-382b-8d41-55c3d31bf148 | -13.24361 | -47.33496 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69593c6d-2bbb-3980-a81a-7f32a228a98c | -14.58496 | -48.32881 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8b391cdc-f5d2-3057-ae48-b16a061df366 | -13.95972 | -48.13391 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee8a8832-03f1-3d94-ac3c-9d0be06e58d8 | -13.18006 | -47.78407 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e149eb4-623a-3170-8815-be62f6e09a52 | -14.47244 | -48.39761 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 510d6b71-9ecd-36f5-ad99-9cf2f47fb0a7 | -12.66957 | -48.57251 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55219772-8196-3e4c-9a8e-76edbc3a2b89 | -12.79915 | -46.86806 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57e9031c-0c44-3133-bdc3-ba9720b96414 | -13.76278 | -47.98878 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe045c6a-ce3c-3f7a-978e-a4dec8b449bb | -15.74269 | -43.67704 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0607be2-bb9e-3498-8de5-3f67a8abea6a | -15.93386 | -43.30228 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daff2539-990b-30ef-aa6d-bca360418c83 | -16.36929 | -47.07062 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d461a235-a66a-3533-912c-75290f6e2709 | -15.25764 | -47.90369 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1553f6-0c88-30e1-b2ca-792b5768d9e3 | -12.866 | -47.02542 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a31fafd9-0a15-380b-81f0-6da1dc3079c5 | -12.82194 | -47.02204 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d6a7be7-3c6a-3086-9c2f-0eb8ce2743bc | -12.25922 | -47.80869 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53c05d3c-b54f-3ec4-b38d-0a6866777859 | -13.96029 | -48.13035 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3869be47-fc87-3c76-9e7c-c0ce0ef0313a | -11.85594 | -48.0515 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 381d3815-a80e-310c-be0a-177f5705363e | -12.70233 | -48.57075 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c762630-0ef7-3239-be38-6b9b34468a23 | -17.69305 | -46.84065 | 2025-10-02 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a072c7e7-a9c6-3ecc-8796-5292f8afec1e | -14.59091 | -46.71352 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af9933ed-e83a-3085-9aa2-61c6bc369590 | -13.22922 | -46.43177 | 2025-10-02 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34abb983-0655-3543-90fd-1b1ec91e22b3 | -13.37886 | -47.31323 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abbe8ebd-a0d9-3f32-b17e-639437ee2bb1 | -12.76954 | -46.8818 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 109e3ceb-95c7-3489-9def-8fd9f4a2851b | -14.90873 | -47.23156 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7d2f5d4-45bf-3785-a929-3fd419ffa829 | -19.69785 | -43.99035 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f81d6040-7c7e-3ae3-8d7b-0bd44a3c0cc9 | -13.23735 | -48.50475 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51ed493-d1e2-31d6-8874-2779a9403052 | -19.04791 | -48.13773 | 2025-10-02 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac5141fa-dffb-31f0-a3bb-aa52a99d708a | -18.17952 | -53.27821 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b63eba94-af3d-37a8-b491-c2773c3b654d | -14.49121 | -48.43005 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a92d9425-cd11-34bb-b11f-92f9b2c09385 | -19.52095 | -43.60539 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 603e96c7-6f2c-3d6e-b925-3bf80b35d0b3 | -14.46578 | -48.3965 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b378f652-43ea-358a-840c-965b21f77d12 | -13.68637 | -48.06692 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README97.md)
