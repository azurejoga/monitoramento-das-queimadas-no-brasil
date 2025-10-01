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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2793cbca-8d75-379d-b474-1bbc6a794e2f | -14.76006 | -45.75373 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3fafb869-9811-3ede-8096-2213f4d6ee3e | -15.11235 | -44.95244 | 2025-10-01 12:00:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9fb103a6-1cd6-372c-85cc-37b66e7874b4 | -14.36253 | -45.9353 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 34b20016-8865-326c-a8a3-cfc863b36b3a | -16.28649 | -45.24554 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8238df4-eb0e-30fb-9f97-e49015cddee2 | -17.86351 | -47.14321 | 2025-10-01 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b424183b-5163-34de-acb7-6260f9835acc | -14.67483 | -45.28642 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc33ebae-1973-31c3-b1ae-12955aba139c | -15.35064 | -47.84351 | 2025-10-01 12:00:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5a7534e4-d83c-39a1-a4c7-8f75dfc91943 | -14.3735 | -45.92641 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f11caddc-6253-3661-890f-f4d014d1b1a4 | -18.22983 | -43.39137 | 2025-10-01 12:00:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 812c4f14-cab8-3780-b184-0bdbf2610870 | -15.76775 | -43.7408 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d31e80e5-da51-35cc-a08b-e4dff64fceb0 | -14.34693 | -47.1379 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 78ee9033-742a-33e0-900c-bdbeee459cc2 | -14.68392 | -45.28783 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3b48ed78-a530-340f-a550-87f803693ec4 | -15.07145 | -45.04209 | 2025-10-01 12:00:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d1aa828-9196-37b8-b0ae-5a36f251da7c | -14.90019 | -47.20666 | 2025-10-01 12:00:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b4107aaa-732f-3245-9ce3-bebac002a4f9 | -14.04411 | -47.98745 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0d22ee57-8af8-3682-9ac4-ecb16132f509 | -15.49367 | -45.91015 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 86bc9d5c-80c9-39d2-a88c-e53ae465607e | -14.63439 | -46.81048 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 43494e7a-b507-394b-8cdc-2d337225aa23 | -15.23645 | -48.73206 | 2025-10-01 12:00:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a2a3b9e9-1df5-342f-9101-4e6be41bada2 | -16.69612 | -44.97018 | 2025-10-01 12:00:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e50e57ec-2f83-3bbd-af26-c7022e3e96dc | -14.81569 | -45.82404 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 960741c1-a1d7-3e12-ad5a-65e9e5df9398 | -14.75852 | -45.76374 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8ceea065-7f03-332e-a590-47db560addb6 | -16.40876 | -43.51276 | 2025-10-01 12:00:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8f066f47-003a-3c0c-9eb8-a9f0ae24296c | -14.68681 | -45.2686 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a6b7f3ef-0ae1-31c2-8335-e14162c2e6ba | -17.86833 | -47.13885 | 2025-10-01 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| cd4fac66-216e-3439-9226-67ebc394be21 | -14.63884 | -46.97598 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3e785951-0197-3bca-9267-a9e9954c3199 | -17.84557 | -46.16658 | 2025-10-01 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3970b81c-68a2-3721-a760-ca3a7e4e8a99 | -15.48598 | -45.89861 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b1f99a5e-a76e-32ed-bb18-2c827edee670 | -14.75096 | -45.76675 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6e327020-4a28-388c-b136-22ce1068ae5c | -15.63565 | -46.24845 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5295a9a5-1aeb-3e12-850a-4a72df16d277 | -15.39229 | -49.18575 | 2025-10-01 12:00:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e71d4b3f-f98c-3c08-bf06-29a85c5fe409 | -14.36412 | -45.92503 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 91192e32-6bae-353b-bf26-9a703f8dcea0 | -15.5844 | -41.81347 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 81b47f9e-eeaf-3369-8cca-79e6a241345e | -15.94215 | -46.24329 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f6a11a3d-dc65-36d4-a93b-298d3b6f387b | -16.90699 | -47.43186 | 2025-10-01 12:00:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a7b52172-b1dd-3c96-a555-08535869a359 | -15.59378 | -41.81466 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| b58a7e45-aa69-3a8d-899e-b55c5d742812 | -14.05713 | -47.97527 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| fb7cee06-796f-3011-bac2-19b60f6383e5 | -18.45652 | -40.48756 | 2025-10-01 12:00:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 225e8f53-6a65-3667-8626-f75756c06777 | -15.31517 | -46.40275 | 2025-10-01 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 438004be-2365-3aa3-b1fe-d513475771bb | -14.81722 | -45.81397 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ca3ae033-8201-3bfd-a68b-cccf958f2de8 | -14.88862 | -48.31253 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7b21467c-7d00-366c-9aa8-1c94f35c808d | -14.97142 | -46.88843 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f975f6e9-1ea8-324b-9ede-f01e5073a717 | -14.60716 | -47.31154 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 31f9ff1a-6931-3902-b3e0-6e45afca07c8 | -18.45733 | -40.56949 | 2025-10-01 12:00:00 | TERRA_M-T | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| c4528dd8-dcd7-3630-a369-d8a688a9689b | -14.89916 | -47.2126 | 2025-10-01 12:00:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 15195a6f-f8cd-3303-a5b3-01e9f274cf96 | -14.794 | -45.77954 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 702b8fc6-daef-3514-acf5-49f70411385f | -14.81264 | -45.84421 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 0d034d19-3c58-3096-8416-2078ebdf475e | -16.6384 | -46.92389 | 2025-10-01 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a70ee8b0-0615-3169-a82d-b8f12635e483 | -14.49834 | -48.44388 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b30b6dad-cc4d-35c7-8894-ed06d9b92a77 | -16.38721 | -47.0108 | 2025-10-01 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2e5c7c79-3c38-3156-a8a5-cb0441bf5ff0 | -15.93887 | -43.31189 | 2025-10-01 12:00:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| f112e6ff-fa44-36e2-abfa-fc1c4b7c1b2d | -14.51627 | -48.48296 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 058147b5-4e0f-3448-8818-f9c01cc50059 | -15.01731 | -42.45962 | 2025-10-01 12:00:00 | TERRA_M-T | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fc7e0a81-a2a6-3e2c-9414-10e35240d9ce | -18.06532 | -43.90952 | 2025-10-01 12:00:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d4d7c762-93ea-3fd9-964d-cccc8fbafd92 | -15.34596 | -46.26762 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbe689e1-1e95-3996-866e-315b04b4e42b | -15.85893 | -43.09515 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 58b04a22-7a1f-3da7-ab6f-8d095d58adc7 | -18.16888 | -46.10709 | 2025-10-01 12:00:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7ad59f2a-98a6-3a9c-b601-7ca04396e23a | -14.97502 | -46.86578 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e8ae7cb9-2359-3f4e-bb2f-104d46900e80 | -15.94373 | -46.23293 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e8c1b7c9-3a77-3f4a-b34b-20aeb92061c2 | -16.70366 | -44.98087 | 2025-10-01 12:00:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ba050109-b662-3a3b-bf41-8abf48c40cc4 | -15.4952 | -45.90016 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 235c4627-c929-3745-be44-bd887e01835a | -14.43864 | -46.35243 | 2025-10-01 12:00:00 | TERRA_M-T | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 31eb554d-9003-3e1e-8a7a-edc7ec1538c3 | -16.29546 | -45.24695 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 17d938a1-43fb-3d29-9e58-e6a539ea1177 | -17.86518 | -47.13242 | 2025-10-01 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 42e1cddd-6115-3f97-b7b3-cb984513660f | -18.16738 | -46.11697 | 2025-10-01 12:00:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 543d1d51-9f64-3e1b-b493-ea12379dd504 | -17.97113 | -45.01844 | 2025-10-01 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b613efcc-4239-3a83-9949-dc93f184014d | -14.36573 | -45.91467 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ed082d8e-1659-3e37-8a7e-3fe22e3046dc | -15.41719 | -47.05261 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b8d785fa-992c-3bdd-b88a-69fb3dca4df3 | -14.96162 | -46.88687 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fcef1739-16d3-3d80-b986-58d3a651bc41 | -14.80796 | -45.81243 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d1e429fb-e246-3ec9-964b-aa546cafc571 | -18.6065 | -43.26327 | 2025-10-01 12:00:00 | TERRA_M-T | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0c43f7f0-34a1-305c-8581-b7df1c147405 | -15.27971 | -46.41287 | 2025-10-01 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ce716899-653b-39ac-b660-b467e6de60c7 | -15.42706 | -47.05404 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 959e5c3e-01e8-3229-8b13-97d387fdce38 | -14.88639 | -48.32638 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 014951c0-d9f1-3581-a250-f101a717ceca | -15.39463 | -44.9768 | 2025-10-01 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 424dad71-24d9-3c2e-8e87-33f5a18d95e7 | -17.67351 | -47.26288 | 2025-10-01 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9f9a3319-d0b9-31b1-bd58-570df52296eb | -15.30328 | -45.03297 | 2025-10-01 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1a27d1cf-44eb-32d9-9c5a-eba914763118 | -15.61631 | -41.83455 | 2025-10-01 12:00:00 | TERRA_M-T | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| a47cc8da-19b6-39d5-b3b7-41666504ebff | -14.78779 | -45.75815 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2c773c1a-1c84-3f8a-9ca0-a14c477bf8a5 | -16.17618 | -46.52271 | 2025-10-01 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 02698c0b-3db0-33cf-8bee-cbd00256f5ba | -15.3365 | -46.26634 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c4fa2df2-1769-348f-acb5-a7272f2d3138 | -17.40208 | -47.16422 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3a8eff16-abb6-3b94-940d-01913c2ac1af | -14.79096 | -45.79945 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 09972e14-4896-37d1-9c23-4cdd08204e08 | -15.53333 | -45.22306 | 2025-10-01 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fe859cfe-f325-3a73-bcff-5e2007d25ff4 | -15.95149 | -46.24485 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 89060b5f-28d2-32d8-8438-253b22562adb | -14.80644 | -45.82247 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| a4617f7e-1569-39c6-8184-20161fffac09 | -17.41004 | -47.17636 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5fd90d5a-72db-3425-9bc0-5333d6d97635 | -14.05261 | -48.00287 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 769b500d-9735-36ee-adb8-f463a60f601b | -15.5029 | -45.9117 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9e5f6968-0731-3d9e-a5af-a57d33d3eb96 | -15.52288 | -43.58287 | 2025-10-01 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e447425-f941-39df-84f2-0be5f7769c1c | -15.49314 | -42.5479 | 2025-10-01 12:00:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 20fdf83b-2177-3809-9828-712a3d31606c | -14.35758 | -47.13338 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d93d32ff-1813-3018-b1e3-d1703ccda39c | -14.80174 | -45.79097 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 050cd384-5427-34d5-bbd2-fd6ed0d0d647 | -15.31226 | -45.03431 | 2025-10-01 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a32026cb-0794-3b15-94cc-cfa24b6f6d35 | -14.75697 | -45.77375 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7da9c422-357a-38c7-987f-24e83d04f06b | -15.17949 | -46.40091 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b3632767-193f-3d58-8339-0121d2fc39b6 | -14.9143 | -47.81742 | 2025-10-01 12:00:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 7fae238b-71f5-3640-9a3d-1117961e6efe | -14.80325 | -45.781 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 126747dc-9bdf-3fb3-8841-af448c19aa75 | -17.86661 | -47.1496 | 2025-10-01 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a5286a42-1fe3-374f-9eab-3ba71e99904e | -14.79552 | -45.76957 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9562629e-cfeb-34e6-94d5-5f92f3552da7 | -14.80948 | -45.80241 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |


[Clique aqui para ver as próximas entradas](README147.md)
