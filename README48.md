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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c108c4bc-f295-3c83-9813-c9f5072b52a4 | -8.50247 | -45.64116 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 906d3157-903f-3c6b-bcf0-3180f0b0a293 | -8.4997 | -45.63711 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f241639c-43e1-30d9-a90e-a1784f2679b5 | -8.49914 | -45.64064 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d6271f4-b10e-32a1-8973-faf543fd90a2 | -8.49692 | -45.63308 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd0fa5c2-1250-37a0-9436-3df0a012b3b2 | -8.49637 | -45.63659 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b22128fd-4863-3dc4-a405-9adad1d54400 | -13.66401 | -44.30886 | 2024-10-26 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bc610d8-12d1-369a-970a-d881663c0200 | -13.65485 | -44.29949 | 2024-10-26 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 086f29f0-6725-3f51-b260-2035e7dbe073 | -12.46682 | -43.79001 | 2024-10-26 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4db90059-3d85-325b-83a8-7b9a0e94eccd | -12.2277 | -44.63115 | 2024-10-26 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c28e497-287b-326d-aba8-ce7d56a932ed | -13.33269 | -46.37569 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1df7dcac-b726-3f17-8fd4-07882a7f7420 | -13.33213 | -46.37924 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78a1dd79-3bc8-3fe0-ba69-cfbb2497103b | -12.48511 | -45.24699 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f48c0643-7ee0-3eb0-ba32-76080c60cc8a | -12.48455 | -45.25056 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b7d0cb4-5734-3321-bcbc-391e2d03f049 | -12.48177 | -45.24646 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37d5153b-f21e-3a5f-b146-42ba7e1d62a8 | -12.48122 | -45.25002 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0bf4fd2-a94a-376e-adec-dc4bb5f9a5a0 | -12.48066 | -45.25359 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 159191da-380e-3eea-9191-3e8bb7a2a16a | -12.47733 | -45.25305 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daba3386-a4cd-3afb-9c1f-c41775d8faea | -12.47399 | -45.25251 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8953859b-7cbe-3a90-8e8e-2bbca80251a8 | -12.26481 | -45.65885 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fffdc6f7-3dfd-36b5-9e83-1f632f195896 | -12.26426 | -45.66238 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5df85e2-177e-3e10-b8c3-8462b29cba9f | -12.2637 | -45.66591 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9b0233b9-0eb7-3110-8be8-ccb36a390f13 | -12.26149 | -45.65831 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 58140991-2a1d-3f8c-9dfa-f2ca6de7ed07 | -12.26093 | -45.66185 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b50cf4c-757f-3676-9572-994273488d41 | -12.26038 | -45.66538 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1e6aa981-a6a0-3245-8c32-e1b667b85c46 | -12.25816 | -45.65778 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3989cf6-9565-3901-bfe1-8b228f7150cb | -12.25761 | -45.66131 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 333a0d9a-017b-3cb1-9572-84e904dbb9a4 | -12.25706 | -45.66484 | 2024-10-26 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 734250b9-f10f-3156-a7e9-0baeac8baee6 | -12.10123 | -45.71175 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dadcc72-7346-344d-9d82-f443ba011a36 | -12.09901 | -45.70416 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 529044e6-0981-3327-9875-ef41e442dd9d | -12.09791 | -45.71121 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65a6f80a-351d-380d-a77c-45dbc4776de4 | -12.09735 | -45.71474 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 556fd050-b18e-32e6-a254-1e33789debce | -12.07687 | -45.71504 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39592846-b8b1-30cc-87d3-cc2215f9b736 | -13.94812 | -38.94614 | 2024-10-26 04:19:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 66909e13-d288-37ea-b36e-87a2dd1e24b5 | -8.89 | -36.23555 | 2024-10-26 04:19:00 | NPP-375D | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a613c9b1-3e5c-3194-b2c6-1819b8182c36 | -8.88956 | -36.23889 | 2024-10-26 04:19:00 | NPP-375D | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 756475b8-ba8d-37f0-bd91-1cd853eb7e26 | -9.70775 | -36.5334 | 2024-10-26 04:19:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6f4513b-5524-33d8-b018-da3b57944c14 | -9.70734 | -36.53648 | 2024-10-26 04:19:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 956bc843-e62c-3aaf-88cd-2dd881186694 | -11.20844 | -39.909 | 2024-10-26 04:19:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fb64eed-bf20-3824-95c9-66659190841c | -7.01985 | -40.05313 | 2024-10-26 04:19:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9927e5ec-88ce-347c-acc8-14e50d8cb31f | -7.01784 | -40.05129 | 2024-10-26 04:19:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 600b2043-d43b-3ba6-9a6c-286d96ead16a | -6.975 | -39.2487 | 2024-10-26 04:19:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da4d3da7-bdac-3a48-af33-10f97849886e | -6.9672 | -39.24377 | 2024-10-26 04:19:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4797f889-fe6b-32d3-8331-8562a15cf165 | -6.9006 | -40.00505 | 2024-10-26 04:19:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40f79139-6a1c-3953-b9a5-912cd2192c6c | -8.81418 | -40.26781 | 2024-10-26 04:19:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 88f25474-2f1e-3d8c-a9cf-bba8cf5f32c2 | -8.81282 | -40.26604 | 2024-10-26 04:19:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ad2473a-af9c-3608-a0fa-2e34a46050e9 | -8.20582 | -39.83323 | 2024-10-26 04:19:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af254fdd-4330-3dde-8c56-c90c8934079a | -10.84258 | -40.41935 | 2024-10-26 04:19:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c910f70-2cfd-3401-b6d9-275276d3a3a1 | -12.16368 | -40.87328 | 2024-10-26 04:19:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91a3cde0-0377-3d04-8a56-fec619c04c2f | -12.94031 | -40.64064 | 2024-10-26 04:19:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7effaebf-27e1-30b9-a7aa-f77a29b17e77 | -13.92733 | -41.45359 | 2024-10-26 04:19:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3190735c-ee2a-3159-a04f-85ca6d0f01fd | -7.25601 | -41.227 | 2024-10-26 04:19:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8eeffbf-bf2f-3ec3-8e0d-ec889bf73841 | -7.0029 | -41.29873 | 2024-10-26 04:19:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9979f3a6-4708-3e15-ab95-d163406651bf | -6.95439 | -41.32189 | 2024-10-26 04:19:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe9ce942-de96-352e-a0bc-d5f44fd9f048 | -6.68681 | -40.89025 | 2024-10-26 04:19:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41303a5d-bc40-3f8f-8f4c-3a22183295f2 | -6.68615 | -40.89479 | 2024-10-26 04:19:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| df4aada4-40d8-30c3-868e-27fe80cd0bb5 | -6.68482 | -41.23497 | 2024-10-26 04:19:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2e1cdc6-005d-3e16-991a-c20d6a3d5917 | -6.55193 | -41.71639 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1dbc40e7-53c3-3925-b248-2441374ec015 | -6.55124 | -41.7071 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| afdfab29-9879-32a6-bc0b-cc8762f0740b | -6.55063 | -41.71118 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 448347fe-b9c6-383b-97f0-90aac355305e | -6.55003 | -41.71528 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 17882dc5-bdb5-3069-938c-773831b52463 | -6.5496 | -41.70771 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 54ed060e-522c-37de-8734-bbd85c120b0d | -6.54897 | -41.71179 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4369e09b-afcd-387d-a083-7c21bab1e7e0 | -6.54834 | -41.71589 | 2024-10-26 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 344fb42f-c275-3099-8aa2-ab26b097cb8d | -6.48222 | -41.52114 | 2024-10-26 04:19:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb331d03-7c5a-3f11-b46e-2bac167a9a0e | -7.76624 | -41.24383 | 2024-10-26 04:19:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8cb3628-f9a0-3c37-abf4-e0deed79faca | -7.76252 | -41.24326 | 2024-10-26 04:19:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a0d3d0e7-b482-3b2e-ac49-0450a4a70f08 | -10.19804 | -42.45215 | 2024-10-26 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abee7397-9942-31af-bee6-46c934423313 | -11.88795 | -43.05931 | 2024-10-26 04:19:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ab9cc84e-8f86-30bf-99d1-a6e913c7b8eb | -11.88735 | -43.06338 | 2024-10-26 04:19:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 197cb063-ca27-3bfa-97ab-616ea4e44174 | -11.88439 | -43.05878 | 2024-10-26 04:19:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5c85c343-32d9-30d1-9e3f-d17bb8d96839 | -13.5039 | -43.01435 | 2024-10-26 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae678bad-31ff-3339-b18c-b9615b1f087c | -13.50329 | -43.01862 | 2024-10-26 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d6e1197-32e6-33ee-9b62-480d23907c0f | -12.92296 | -42.44797 | 2024-10-26 04:19:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb670d82-c5d6-3414-b034-2b40364e20c7 | -12.92188 | -42.44562 | 2024-10-26 04:19:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca2d01c7-c451-3214-bd6e-e6e97180a0e0 | -13.0573 | -43.34879 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20b36016-6c81-3693-be54-ea65dab4a10f | -13.0567 | -43.35286 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af5c12e5-a36f-34c3-9da2-720ca13653a6 | -12.65699 | -43.30921 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 865ed009-c185-3a7b-8330-3b5aa747e28e | -13.81307 | -43.34477 | 2024-10-26 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b738898-ab92-3f3d-8ae8-f56f7e79f396 | -6.50906 | -42.34632 | 2024-10-26 04:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f91c8473-c12b-323c-9059-1bd19363397b | -6.50558 | -42.34579 | 2024-10-26 04:19:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8aa30a1b-5376-3815-949d-48d7a7bb355c | -6.5021 | -42.34526 | 2024-10-26 04:19:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 58621400-9d13-3e07-829d-e6a24bbc05be | -7.79975 | -43.16669 | 2024-10-26 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e84c073-ad9c-3491-ab34-86cf8804fe7b | -7.68495 | -42.64271 | 2024-10-26 04:19:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b9cc8be2-8913-3d82-a194-c37d0fdb69fd | -7.68147 | -42.64217 | 2024-10-26 04:19:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3687ebcc-d9cc-3ed0-8ae1-8227a22990b1 | -7.61182 | -42.29461 | 2024-10-26 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a3eb1b8a-3810-35a5-a67e-f9bf25144d4d | -7.6083 | -42.29405 | 2024-10-26 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6c568760-be73-3918-8a78-7e5c11690037 | -9.18176 | -43.24749 | 2024-10-26 04:19:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4141b30c-47da-3fc9-823f-9733c99ce5e6 | -9.16044 | -43.15513 | 2024-10-26 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58cea1f6-9f3e-3c82-bc19-45f3722b010d | -9.15698 | -43.15463 | 2024-10-26 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ff6c7be-cf07-35b8-9065-fe05c825d6a6 | -9.10319 | -43.19395 | 2024-10-26 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74288b0b-b033-3f42-993d-b82639969625 | -9.60884 | -42.92588 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 652c9aad-aa18-3f5f-94f5-4a63e4ac51ae | -9.60877 | -42.92305 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 333efb98-42e7-318c-b486-8dab437fe77d | -9.60827 | -42.92976 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea055470-9ae3-3e0b-9f38-cd2a774c9a96 | -9.60759 | -42.9308 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5167ee7f-fb8e-3eb1-b510-f15bcbc77e87 | -9.60646 | -42.91472 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7e28f29-a1c7-3f2f-bce2-eaf3911af3f9 | -9.60586 | -42.91867 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21835c2b-2c4b-39a6-9032-42c6bb939171 | -9.60526 | -42.92259 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98d1cf55-ba8f-3d3b-bb04-368ecbf71f56 | -9.60409 | -42.9303 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63e53f9a-dca6-309c-bc8b-143ab921284a | -9.60351 | -42.93414 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbcfb01e-a05c-3ee5-b349-bb7d4c0b0c04 | -9.60001 | -42.9336 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README49.md)
