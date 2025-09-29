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
| 50e2a1e6-d845-3014-9644-1d853a8664ab | -8.29586 | -45.47693 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab0bc009-4fd7-3202-9904-2d41a77fe504 | -6.61772 | -45.90307 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6bdd62f-c136-3939-8b18-9dea0addeaa5 | -6.61792 | -44.94326 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 182677fa-443c-34c1-bac6-0afaa8682835 | -9.28419 | -45.69299 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7cf0246e-1bc9-30b0-96ab-5fd89cbd963c | -8.71867 | -50.04461 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3a7582f-1b5b-3d53-b2a3-47a69c0f0fc0 | -11.99798 | -47.11304 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffd66904-7643-3ecb-b120-db82244ac221 | -7.24254 | -43.01435 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 095f9976-ba16-35d7-9fb4-585ad4e66967 | -10.54399 | -43.63362 | 2025-09-29 03:47:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 416d9453-7b91-30b0-9f63-cb601bc8aeec | -11.7119 | -44.43766 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b45bcce-e393-3f50-9b0a-368205c3846f | -8.2471 | -45.4916 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aef50c16-f898-3ab4-aaf1-6e2fcb87970d | -15.41539 | -48.22993 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2f61244-48f8-39e7-a54a-01da53fd8db6 | -6.47034 | -42.92126 | 2025-09-29 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6db561a1-bcf4-3293-90d1-14dc5f808144 | -17.07503 | -48.57448 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea33e2b3-a189-3905-8c82-c03838c4160b | -8.66294 | -49.43089 | 2025-09-29 03:47:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d8d43cc-faca-3fdb-b947-985648d133da | -11.98026 | -46.58488 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10159de3-6c95-3e18-a8fb-c7073ede7f05 | -6.2803 | -42.48594 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cef4612b-e7b4-3f88-a4a4-6fc573716cb3 | -19.96805 | -41.74195 | 2025-09-29 03:47:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 380b81db-2eec-37b8-861d-fc9b812f54b9 | -12.17816 | -43.56261 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 340339df-097a-30e9-b86c-81e46fa3b421 | -11.76022 | -47.55935 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ffc659d-040c-3bd9-a00c-487d8f75ae78 | -6.91084 | -44.00207 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c0cc4fc-4c10-3ce3-b723-dc306ea281c4 | -6.31713 | -43.45089 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92e471a7-5cee-3488-a071-a46715b3883f | -8.6673 | -49.43197 | 2025-09-29 03:47:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dd8e186-95f6-31e2-8d83-e9a191c6442e | -9.30702 | -45.72455 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55f2a961-887d-38bd-9f47-723865e7bd0f | -11.71679 | -44.43861 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d353219-e482-39a2-9e56-6f2ca9b3f8d0 | -7.29934 | -42.82903 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| feb64188-71a2-3699-ba15-5610e6d32338 | -9.04683 | -46.70519 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f70134ea-aaa5-3385-aad3-2bbd6b270b0c | -6.62087 | -44.95854 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 281579f1-7255-3cfe-a60d-366b5b52785c | -12.00163 | -46.6105 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4874bfc8-8727-3225-88ad-5a6538d44a2c | -17.75511 | -48.76635 | 2025-09-29 03:47:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 570c00dd-1acf-3eee-99f7-71fe13049ebe | -7.5627 | -42.40539 | 2025-09-29 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f41d988-a063-3b0d-ba64-e5c9e60023e9 | -10.53834 | -43.63776 | 2025-09-29 03:47:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eab2dc6b-e442-3be5-bab0-2289dcd75469 | -6.2195 | -44.20274 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4ce9a1c-f1cc-3592-81b8-c89c18ab6875 | -8.71571 | -50.05964 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 476d0277-7311-3221-969f-cb6bcbed678b | -8.16142 | -46.39639 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7114fa3-8de9-3d4f-8f07-ee7347bd5480 | -7.28797 | -42.83567 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1cf1fcf-8307-3f6d-8ce4-6e7dd0458141 | -12.285 | -44.10056 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 684ea78e-4338-356e-b878-e29f4529fbe3 | -6.62239 | -45.89724 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93fa602d-d3c0-3559-9427-c354456d44ba | -9.05431 | -46.71039 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c657e6a5-8604-34b6-a352-958ea574f606 | -10.48558 | -49.36713 | 2025-09-29 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f8a1592-cb58-3d01-8154-ea3d20678132 | -6.82473 | -44.83181 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bb076a84-e00d-3982-b559-da5480198e78 | -7.82587 | -45.14116 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5610e1fd-d9a8-3972-96ed-211944c304a9 | -15.87122 | -46.21801 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0da19ff-b6ef-3d0a-895f-74249aefe237 | -8.26659 | -45.47963 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea36a105-3a1c-31fc-bcc9-7f9aae6846cc | -7.86183 | -41.05595 | 2025-09-29 03:47:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80ae6d48-5e19-3289-955b-212ab2557791 | -7.76755 | -45.73034 | 2025-09-29 03:47:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7d7b4f5-f1bf-3d50-a71a-f3e5767c30a0 | -15.32579 | -47.90824 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b5dd118-cad2-3b4d-955d-2253e473964c | -15.2737 | -47.87103 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f7d2a51-ddd0-33c3-aadf-a53c01933b52 | -12.8717 | -45.15984 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e73b221-1b18-32de-9449-bf5d1f3d0f10 | -12.65902 | -46.90984 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a23bae4f-8787-3f5b-b218-4ae95a6eae4b | -8.14697 | -46.40796 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6c64acd0-c4de-39b0-a762-26f601c88f46 | -6.30484 | -43.46208 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86f006d0-ecb5-375d-b016-fc59d02e56bd | -11.36372 | -45.06313 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 750e4456-163c-3802-8374-c10684068403 | -7.51388 | -44.29942 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9da0f433-cfd0-35d8-b405-d809724e42c9 | -16.49161 | -46.03547 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f981547d-9e4d-3501-b2fb-8dc429e16aaf | -6.11448 | -41.82681 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e852d408-a8e0-3b3a-a2e8-51ef3b71867c | -15.615 | -46.25655 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f43fc80-0a2c-3094-854e-a09bbbd0d5d4 | -8.27301 | -45.50743 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 654b3670-272b-33cf-9c3f-8aad65e62717 | -7.58193 | -44.80706 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b782afe0-b7fd-316d-a703-cac97d48e931 | -6.57836 | -45.0982 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee459cd1-6065-3027-adc2-80cfb05d0866 | -6.11687 | -43.47768 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7106b90f-4925-3290-b123-47a0452ca0c4 | -11.43971 | -45.03663 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8360df34-4f2b-332f-bccc-466f3c80386e | -20.04667 | -41.33949 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 87266935-5dff-3a05-9742-0b0889e6b0a2 | -17.74931 | -48.76521 | 2025-09-29 03:47:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0ed444a5-5cd2-3b45-bcab-885b101e3549 | -6.85487 | -47.36127 | 2025-09-29 03:47:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7876437-2577-3d7e-9dc7-2995d693bdf4 | -17.08406 | -48.56516 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24e5217f-c117-3523-bb20-99383421d485 | -6.83076 | -44.82958 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19e923ea-5902-34ca-b6cc-8bc745c2f0a5 | -6.91193 | -43.99598 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd57e48b-a684-3f50-8bd6-8b9bb044b6a5 | -6.06685 | -42.47998 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c88963eb-c581-31ad-8a9c-7cf8783d959d | -16.55043 | -45.30899 | 2025-09-29 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f8c7cd6-bced-31e8-9e6d-dbadf6061f95 | -12.66696 | -46.90905 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d197d1-7825-39bb-9c7c-83a992dbc56a | -6.3951 | -42.90503 | 2025-09-29 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d4ec9379-f3b7-3613-92de-65ea1b6489c8 | -11.40403 | -44.90469 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a58a25f7-2b8b-35d3-9640-43ec35d38193 | -10.82878 | -45.40926 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1f33133-29cf-3cdd-b7b1-8ba0a1ec5a77 | -15.28322 | -49.50896 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c44a81b0-a611-3f8f-a747-e84d3c810bc8 | -9.5491 | -47.76873 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 077356ef-87c0-3e5e-94bf-e1ba01104a82 | -10.82642 | -45.39288 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ed7705-c51a-3b8d-ac7f-7919eaf46170 | -8.16418 | -46.3963 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc68d09d-f95a-3bf7-8ace-fe0c38a687ef | -10.40255 | -48.12016 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4999f7d1-a048-3ec8-be0f-5f313b57c3b2 | -6.31169 | -43.44672 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b03527cd-75bc-319f-a669-7b7db8a75abf | -6.46412 | -44.21975 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73841e9f-c926-34c1-881d-20483e01e74e | -10.80937 | -46.68246 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b93d8ce-eb58-3872-b0e9-1a0cc8d5258e | -11.73053 | -45.23414 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b64aecc6-ac41-3c85-9a9b-0eb8f21fd47b | -6.83021 | -44.83204 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b79b9005-bce8-3665-ac48-f73cfe0dfd02 | -19.47063 | -44.34232 | 2025-09-29 03:47:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f05c42d-7acd-33cb-a5f5-ad1d0aa8fe50 | -6.46351 | -44.22324 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cce7bd2-3739-338c-9cbb-0571b4e6a210 | -7.22802 | -44.78842 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a33f03cd-eef3-3a98-986b-f70ac5ad1f17 | -16.24879 | -42.21269 | 2025-09-29 03:47:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 133ec9bd-9870-391e-8831-fc25b18cfdfd | -12.85711 | -45.18164 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83eae1ff-2e74-3bd9-b4e3-082f3cfcbd45 | -9.51259 | -47.68936 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc50649b-9473-3baa-858a-f6886f00be4d | -15.86713 | -46.21201 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc8842e2-5394-31c3-9274-d47cde294a84 | -15.29 | -46.41936 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8335dfc7-0323-3fb2-85d5-dda93dc6ee3d | -7.50923 | -44.29528 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3e53656-345c-3ed9-979f-eabb87825a29 | -9.7774 | -46.93951 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1ea47f1-5cb4-38a0-bd01-9b764235f91f | -7.82534 | -44.80389 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf8fe98d-e7b9-3002-83c6-45442375fca6 | -11.6962 | -44.4403 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d18abddf-a269-32e9-bd61-fc9440e604f6 | -15.5252 | -47.92963 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7988cf16-9ebc-3272-a0f0-16a114f1b654 | -11.65807 | -45.33152 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19fee2dc-fd0f-3fee-8d75-77b9cdfaf9c3 | -12.58004 | -41.28285 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dabd21bf-8e39-30fd-9103-2974427ea73a | -6.26764 | -43.6482 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e880051-738e-3282-96c7-85d72c99ea79 | -12.17446 | -43.55698 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
