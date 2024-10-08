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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb4ed9d3-8a5a-3829-8084-6f164ff48531 | -22.8041 | -46.720798 | 2024-10-08 00:03:10 | METOP-B | TUIUTI | SÃO PAULO | Brasil | 3554953 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c092fb2-469b-39c7-a2c3-dda2aea80d7c | -22.7943 | -46.722599 | 2024-10-08 00:03:10 | METOP-B | TUIUTI | SÃO PAULO | Brasil | 3554953 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c76beb9-f384-308d-be59-de4c35267c0b | -22.572701 | -47.088799 | 2024-10-08 00:03:15 | METOP-B | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d2587890-ed21-3dc3-9f93-dff6a13c2ebc | -22.652599 | -47.664299 | 2024-10-08 00:03:15 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74fe8960-b3c4-3ce5-b25f-019c45e99f3b | -22.6429 | -47.666 | 2024-10-08 00:03:15 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 092e7aad-64de-3353-9c9c-ba007794f28b | -21.5497 | -42.314499 | 2024-10-08 00:03:18 | METOP-B | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07fafe55-f834-3768-ab79-a27e0b084cfb | -21.5516 | -42.324402 | 2024-10-08 00:03:18 | METOP-B | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8148be7-c316-3cba-a8ea-623869c33a81 | -21.553499 | -42.334301 | 2024-10-08 00:03:18 | METOP-B | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bbd4412a-79be-3c47-b28e-1b99ab28bb92 | -21.3183 | -41.381001 | 2024-10-08 00:03:19 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd4acde5-0c01-32be-a703-3a21e44cc4d6 | -22.0194 | -45.486599 | 2024-10-08 00:03:19 | METOP-B | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 709d43f9-485a-3e94-80a8-fc21ab6a8cf9 | -21.1908 | -42.0881 | 2024-10-08 00:03:23 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c0528a2-1b36-3d6f-b4ad-56f078d89210 | -21.192699 | -42.097698 | 2024-10-08 00:03:23 | METOP-B | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d474b38-43f3-3bc5-bfac-6d03c173c93f | -21.1945 | -42.107201 | 2024-10-08 00:03:23 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a9c7185-2ad5-3ea5-a755-8f76501e5ec0 | -21.816799 | -45.655701 | 2024-10-08 00:03:23 | METOP-B | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bec86d66-49c9-3c43-bb51-9086fcb137e1 | -20.929001 | -41.1675 | 2024-10-08 00:03:24 | METOP-B | ATÍLIO VIVACQUA | ESPÍRITO SANTO | Brasil | 3200706 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9298382-b6b0-3076-9da5-81a23365e5db | -21.168301 | -42.1828 | 2024-10-08 00:03:24 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd4f494c-85d9-3653-988e-70526fdf9c5b | -20.39 | -43.97 | 2024-10-08 00:03:25 | MSG-03 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5da835df-579c-395c-9b47-86900d621178 | -20.37 | -48.86 | 2024-10-08 00:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d50ebbac-2f58-35ca-8a65-d4e78553dfce | -20.37 | -48.8 | 2024-10-08 00:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b7e71fc6-6416-36bc-80e3-1eb200b5b57a | -20.4 | -48.87 | 2024-10-08 00:03:28 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3e2e5176-7af4-302e-a034-456c407fe171 | -20.4 | -48.82 | 2024-10-08 00:03:28 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 48c8754d-fd20-378b-b7aa-578963551575 | -20.43 | -48.84 | 2024-10-08 00:03:28 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1636de97-b9de-35b2-a82d-2c4e16d642ae | -21.003401 | -43.028198 | 2024-10-08 00:03:29 | METOP-B | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d66af531-1850-3d4a-a3ad-eb322d260ddc | -21.0054 | -43.038799 | 2024-10-08 00:03:29 | METOP-B | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e915791-9f02-3aad-9efc-56dedc22940e | -21.842501 | -48.348701 | 2024-10-08 00:03:30 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f2e416a-26fb-39ae-b0f9-4210f44273c8 | -21.846201 | -48.3727 | 2024-10-08 00:03:30 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc5ea62-77af-309d-99d8-ba536e3637f4 | -18.93 | -50.26 | 2024-10-08 00:03:36 | MSG-03 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3128e3-b937-3fcb-8c7e-ae3e19678db7 | -20.3211 | -41.9655 | 2024-10-08 00:03:37 | METOP-B | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c36d7456-85cc-333b-9039-4be473c31d76 | -21.08 | -47.192402 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf0c954-3e53-316f-a1f3-5a048d6ee2e5 | -21.067101 | -47.174599 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82912fb8-e10e-3a04-87fc-122cdef024e2 | -21.070299 | -47.194199 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1cdd668-02ad-3178-b804-ecba1778e60c | -21.073601 | -47.213799 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 37e85e59-ed76-3cb8-bace-73659d65b966 | -21.0574 | -47.176399 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 95e64352-7185-34c7-bc6f-9947ad88c9f9 | -21.0606 | -47.1959 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6447ed37-b34a-32cb-bb78-4aa8ecdeb1f6 | -21.0639 | -47.215599 | 2024-10-08 00:03:40 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 26548a31-dd5d-3073-ab46-57a1561cba2c | -20.3864 | -43.91 | 2024-10-08 00:03:42 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fadab61f-101e-3915-b163-de595e9bd95a | -20.388599 | -43.921799 | 2024-10-08 00:03:42 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1060cf43-fd18-3f81-86ba-132a9072cd84 | -20.3929 | -43.945301 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bf1a189-ee42-3a67-a2d8-efe8f47c4266 | -20.376699 | -43.911999 | 2024-10-08 00:03:42 | METOP-B | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34c27e96-7e9c-3225-9684-8a238c204b87 | -20.378901 | -43.923698 | 2024-10-08 00:03:42 | METOP-B | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ff01a31-7c98-3f01-808f-adba162b0f4c | -20.381001 | -43.935501 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0d245b7-ae74-3dcc-8e0b-256b644fc511 | -20.3832 | -43.9473 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f46e30f1-91dc-3f72-bce1-78554cedfe7c | -20.366899 | -43.913898 | 2024-10-08 00:03:42 | METOP-B | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3dc481f-69d2-3a0a-9eb8-93774ab8d0e0 | -20.369101 | -43.925701 | 2024-10-08 00:03:42 | METOP-B | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 235fdf21-a94e-3a3d-b132-47ae56c49bfb | -20.371201 | -43.9375 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7be19a41-2430-3b04-ba74-94a6b0400f62 | -20.3734 | -43.949299 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3735b6ef-ed51-3a94-a743-2330250af132 | -20.359301 | -43.9277 | 2024-10-08 00:03:42 | METOP-B | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a33822f8-95a9-3b33-a147-80615cd699fb | -20.361401 | -43.939499 | 2024-10-08 00:03:42 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61636ee8-1931-37df-ae37-486c00a27f01 | -20.765499 | -46.329601 | 2024-10-08 00:03:43 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5957252e-fce0-3f66-8228-bdba355cfc19 | -20.7684 | -46.346699 | 2024-10-08 00:03:43 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a863a27-c302-373a-94d9-cadab7e54b25 | -20.7558 | -46.331402 | 2024-10-08 00:03:43 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4b69a4b1-f79a-3f36-9351-b20832cb316b | -20.758699 | -46.348499 | 2024-10-08 00:03:43 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 05bfe400-b466-3907-a8ab-696b6b8d5c63 | -19.9147 | -41.819099 | 2024-10-08 00:03:43 | METOP-B | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 190c1fc4-8af6-3a8a-b6d3-a725116bc054 | -19.9165 | -41.827999 | 2024-10-08 00:03:43 | METOP-B | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95783612-a40b-3b10-9d2b-fba5e015ec7c | -19.807899 | -41.8983 | 2024-10-08 00:03:45 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b9110b8-52f2-3159-8c79-14c903e752bf | -19.8097 | -41.9072 | 2024-10-08 00:03:45 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9029ca60-f7a0-3b62-8606-ee09be72c63c | -19.8976 | -42.616699 | 2024-10-08 00:03:46 | METOP-B | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2ffabdf-47fc-3b06-8722-d4f44d1f3e9c | -19.8995 | -42.6264 | 2024-10-08 00:03:46 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d22c41e1-851d-3f3c-b706-76816eb1f52f | -20.1304 | -43.841702 | 2024-10-08 00:03:46 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 962d04d7-e835-3360-878a-7fbcd1891a3e | -20.1325 | -43.853199 | 2024-10-08 00:03:46 | METOP-B | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 268106cb-d8e5-37ff-a7ad-17c47772318c | -20.226999 | -44.420601 | 2024-10-08 00:03:46 | METOP-B | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e447109-e0a0-36ff-b936-10541cd45256 | -19.423401 | -41.153 | 2024-10-08 00:03:49 | METOP-B | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3b6b3ff-3d8d-3cfb-a614-458c39b181f7 | -19.4119 | -41.146999 | 2024-10-08 00:03:49 | METOP-B | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9275ecb6-faa4-3a4d-8cdf-073ab44c6fd9 | -19.413601 | -41.155201 | 2024-10-08 00:03:49 | METOP-B | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 08a6d2f0-811c-3897-b3bc-00b9648c958c | -19.415199 | -41.163502 | 2024-10-08 00:03:49 | METOP-B | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc612426-c15f-3825-9f29-725f96da9601 | -19.823601 | -43.774502 | 2024-10-08 00:03:51 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66ec9187-872d-3353-a455-c20db9d358b5 | -19.825701 | -43.785801 | 2024-10-08 00:03:51 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 568c1223-67fe-36c8-a191-ab3836f8e5be | -19.8223 | -43.821899 | 2024-10-08 00:03:51 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10012318-71e7-30fe-9923-def2972f739a | -19.8244 | -43.833199 | 2024-10-08 00:03:51 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 28a70cae-d830-3247-8bb7-bdeb659a4d1f | -20.4363 | -47.5966 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14326c96-190b-3d85-aa72-53060adc2d50 | -20.4265 | -47.598301 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e4272c89-8a69-3878-b5ad-bba3c3591042 | -20.4298 | -47.618698 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 461b7fa2-1e40-3c2c-bf9d-62226d4f994d | -20.433201 | -47.639198 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcc5ea7-8960-3f5e-b97a-bce5d49a7232 | -20.4168 | -47.600101 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 072a6326-05e4-37ed-90c7-7acf6536485b | -20.420099 | -47.620499 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 36dd521b-dd40-3db3-bc74-2fcd80631fe3 | -20.4235 | -47.640999 | 2024-10-08 00:03:52 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a4d8ce4e-0ca9-3fc5-9673-79e23976e323 | -20.4216 | -48.741299 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1cc302-2419-303f-9156-0c1ebea49703 | -20.4254 | -48.765598 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90bca6e0-c856-3e4f-90fd-ba9a87f6fa06 | -20.408001 | -48.7187 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cad5dbda-e766-3792-9926-4262359c50ae | -20.4119 | -48.743 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 047d6db4-9c4f-38fc-ba07-8b1d63c31714 | -20.415701 | -48.7673 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 72c2ed11-951f-3467-b2f9-79eddc3d15d0 | -20.3983 | -48.720402 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 49a085a0-3359-331d-8fe6-89fe1c755790 | -20.402201 | -48.744598 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c417ffa-900c-33cc-9deb-e24ec90a69d1 | -20.406 | -48.768902 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 31140e36-5dee-3469-b00b-117cbbe60ce8 | -20.409901 | -48.793301 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dca0ff15-8bf8-39bb-a777-b8744d75f6f5 | -20.388599 | -48.722099 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64124e84-f9af-3fd2-adfe-578f1dc19b86 | -20.396299 | -48.770599 | 2024-10-08 00:03:55 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e78c002-ebcd-3dc9-8c89-c8ab62102dac | -20.379 | -48.723701 | 2024-10-08 00:03:56 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a444043b-684c-3e00-84f1-8043b1fcf982 | -20.3829 | -48.747898 | 2024-10-08 00:03:56 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fe10c78c-cf2c-3917-8f27-50b5d6daf13c | -20.3867 | -48.772202 | 2024-10-08 00:03:56 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b8b31089-5f57-30b5-8749-4241b25898b1 | -20.369301 | -48.725399 | 2024-10-08 00:03:56 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 93e3e353-5c49-33fa-a952-112e835946b2 | -20.373199 | -48.749599 | 2024-10-08 00:03:56 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb32a25-eca2-3868-9156-921e9729822a | -20.377001 | -48.773899 | 2024-10-08 00:03:56 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8785b5f8-0453-3b96-a572-ffaf8c204dc5 | -20.3596 | -48.7271 | 2024-10-08 00:03:56 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9009a8a9-dba3-3eb3-b89b-ed483f42fce0 | -20.363501 | -48.751301 | 2024-10-08 00:03:56 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4e916481-fdd0-33d1-8ec3-c95e0fae9632 | -20.3673 | -48.7756 | 2024-10-08 00:03:56 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b320941b-2728-3f59-b54b-06d7b60e575a | -18.2584 | -39.8895 | 2024-10-08 00:04:03 | METOP-B | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9aa896e1-7f30-3c21-9f34-335494f8340d | -18.259899 | -39.8969 | 2024-10-08 00:04:03 | METOP-B | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87502e23-80a4-3ac3-a177-60e81a3581e4 | -18.557501 | -42.385799 | 2024-10-08 00:04:07 | METOP-B | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81cfc9c6-da98-38cf-8f02-376c148224ea | -18.559299 | -42.394901 | 2024-10-08 00:04:07 | METOP-B | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
