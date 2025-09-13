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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aefa7354-43ac-32bd-9ab1-2e0225143c72 | -16.6071 | -49.47331 | 2025-09-13 03:47:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1db4505c-df86-3a74-9d2d-1a2b44049925 | -11.82525 | -50.55979 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 1cf26f9b-4c4a-349e-b87a-05eac0374f29 | -13.47779 | -48.45398 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b936b38-230d-3dd6-8648-56b867e02afd | -13.35047 | -44.44333 | 2025-09-13 03:47:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5422750b-11a0-37f1-b567-3381b32fc4b7 | -13.47867 | -48.44979 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abd81d32-afb5-31d9-8e77-ae618f6efe2e | -7.77826 | -43.93637 | 2025-09-13 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4efbdaa-8a33-3dd8-a3b0-4653e325a140 | -12.90289 | -47.96 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ac0d0c8-dfeb-3510-97f0-353b652acfc5 | -18.06439 | -45.45029 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3cdf8c00-8839-31cd-ab14-806a29800014 | -14.28373 | -46.07755 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21ed2f91-2e31-3c4c-b447-99ce070c6bc1 | -11.78179 | -43.76273 | 2025-09-13 03:47:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc5610d8-3d82-3d2c-a331-39a7c75f0f0d | -12.94938 | -47.98087 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84155451-32db-30ed-8759-a69e1e8b832c | -10.77448 | -50.52636 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf82e243-6c64-3519-be01-361713398d1f | -10.32666 | -48.81387 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7763c8df-0a35-3361-ad37-a6ca01a57116 | -11.86304 | -46.75928 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bb77f14-23af-3c6d-a946-8f149886c3c2 | -16.64519 | -49.78189 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b7127e4-76ca-3fdb-a561-061a957c5812 | -16.5669 | -49.22711 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95eff194-15ca-36a2-a847-132a54425696 | -14.2242 | -41.97615 | 2025-09-13 03:47:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 188c3b3e-0a2e-3194-853d-752e04e7a61b | -14.17416 | -46.24804 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d97f2e65-3cf3-3f83-a20d-228eb2d64af2 | -16.55388 | -49.22836 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1554874-b8cb-3b39-b233-846587755948 | -10.36398 | -45.43468 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b063d35-a311-3c17-8ea8-ca3661d57edd | -14.17604 | -46.26628 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3315039b-4dee-38a8-b4e2-3a924dbc9fad | -11.84504 | -50.5718 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 14760c6e-50d0-3ac9-a326-a52c5f658b92 | -14.20776 | -46.27295 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 293d11e4-ba81-342f-810b-1df22225739a | -10.89174 | -45.57841 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4551aaa6-30a3-31c8-bc64-e8de7ef44e28 | -17.13865 | -48.51623 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ff4c9a2c-849f-35af-99b5-55d05fbf4eb8 | -14.20057 | -46.25357 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 06137d21-d8db-3284-abbb-6ff9db8b6bd5 | -18.39084 | -44.09887 | 2025-09-13 03:47:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 460d19e2-d703-3aeb-a005-52a9551728b8 | -17.12303 | -48.48172 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e55c3ccc-8a80-3345-8123-03f73b4ce17d | -11.71025 | -46.56271 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e0538c5-1677-3f06-b25c-2aa39ebe1114 | -11.40638 | -50.74039 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38acc1c4-2c13-3115-b9f3-d832e7b70077 | -14.17884 | -46.27997 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7f70865f-eaa7-3567-9d79-4f5d873d5e28 | -19.61778 | -46.6969 | 2025-09-13 03:47:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89b601eb-9010-3124-bce7-1d6a862ffc9c | -14.21206 | -46.25109 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5804c7d6-77c5-3f06-bea8-dbc5a4d881a6 | -11.73222 | -44.21408 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ca87d24-3113-3842-b719-7bd09ace31e3 | -20.44425 | -46.44576 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34cab086-e16a-3b51-a4f8-70c3c1072407 | -9.29124 | -43.26154 | 2025-09-13 03:47:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b08058c3-127a-37f9-ae69-e25ba07e0c7d | -19.25096 | -51.43007 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04bddb83-4128-3594-9508-fdfed0446617 | -7.56936 | -42.65091 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3c92a9a3-1b67-32d1-83db-d32a39dcddbc | -20.55969 | -41.01642 | 2025-09-13 03:47:00 | NPP-375D | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a129c47-af84-3f5c-9c9c-5ab46a17bba1 | -17.30225 | -48.73885 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6459c296-41a2-379f-844b-63c1f20c6814 | -10.10191 | -45.50458 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 471054e3-b875-30f4-a79e-26205a15039a | -14.20288 | -46.24187 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d52446b8-2598-3e7e-9183-13c8a25c23eb | -7.9481 | -46.91077 | 2025-09-13 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47e3b504-e9ac-321d-9c75-d34f94ab98d9 | -12.10204 | -44.89913 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d956f65-3e1e-3cf7-a4b2-83fbef911a71 | -20.02124 | -47.64556 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4b9e8e1-760e-3e0e-8ebf-758a176a7e73 | -17.13523 | -48.50965 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b81184cd-a0ef-3b5a-b283-47c2f2bc090c | -16.25131 | -50.0755 | 2025-09-13 03:47:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71a22c75-3fa2-3c1d-94bc-9c617c7f12df | -14.28116 | -46.06328 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a3359de-5879-3d48-9879-c377a6c9a7ca | -7.56468 | -42.65008 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 18797bf4-e8a1-3a0e-a2e1-5bfeae8dc3c0 | -17.12797 | -48.48684 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4377ae31-047c-3d31-a7e0-7ba900acdb17 | -10.77979 | -50.54279 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c7ff7205-4618-3580-8946-3a1e902dbd79 | -11.70504 | -46.54968 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f53099e-f6ba-38c5-bffe-b9769223831f | -11.7012 | -46.54925 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c373e94b-8897-3973-9997-be243768c11d | -11.49289 | -43.70193 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 608f13a2-4a89-35b1-bbbd-1bf015788e80 | -13.29416 | -43.76527 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3387e59-ec22-3fba-8620-531cda093b7a | -11.74028 | -46.61895 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7a181a1-a776-3b26-8552-54751670e896 | -16.41603 | -49.24757 | 2025-09-13 03:47:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e2352b9-d2ae-3ff1-9946-ba6abd5ed01c | -11.43751 | -45.62878 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a21b1269-725d-3076-b309-982d2a7779d0 | -9.71622 | -48.32041 | 2025-09-13 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43a0c593-d16a-39a3-adf7-0de04cee15ff | -14.28184 | -46.05991 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a60e4fd-cc3b-3317-bebc-fdb8f9e36610 | -17.54222 | -44.54799 | 2025-09-13 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a05311bf-ba36-3392-8d03-63040371cdc9 | -8.46731 | -47.25517 | 2025-09-13 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efe57829-99ab-3e57-bba3-db26b7a8a211 | -17.28693 | -46.10163 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1863bf56-63bb-3f73-a3a0-62f887a5484c | -12.13033 | -44.83086 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80f66dd0-ac27-37e1-abca-dbbf0de42987 | -11.84545 | -50.58274 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 40d3d295-27af-38d9-a75b-1f2cc4941bdc | -8.66558 | -40.18159 | 2025-09-13 03:47:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5dc41cc-13aa-3338-9e57-507bd3aeaba1 | -20.44313 | -46.45124 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22fa8785-1be3-32b1-9653-45bd14f1f4aa | -17.54133 | -44.55254 | 2025-09-13 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd2e5904-82e3-338b-812a-cee43247a491 | -17.83887 | -50.40891 | 2025-09-13 03:47:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ad2b11-0ddd-3928-9939-e4b1b6afc611 | -18.35146 | -47.02214 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ade0b11e-27e1-34b4-a66e-a34149593ced | -12.09197 | -44.89726 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b84ed1bc-d2b2-37a2-b38a-4681b4876ce4 | -12.00182 | -47.76084 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73fe4b57-765f-3a48-be5b-e98404edae68 | -14.21412 | -46.2968 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ace40c06-fa4f-3b6f-b9fa-be4f1dfda0c9 | -14.2903 | -46.07182 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ab43362-01bf-337b-816f-bb636b396a2c | -8.48093 | -45.14915 | 2025-09-13 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b84e9e6-5f19-3d50-a7eb-bf1c8f42a755 | -14.22545 | -46.28529 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 512a5d9c-0690-37fb-97a6-f3e4f90bc5bd | -17.28444 | -47.24951 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be40c798-58da-3bfa-98df-4c893af6c121 | -11.70682 | -46.55043 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cd227c7-5fb5-3a62-85cb-0f00034263a9 | -13.89294 | -48.25606 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5aa951da-5b06-3eae-a14a-f4d7e2f0e26d | -12.84384 | -47.94189 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad5ddde9-ccf2-3502-a324-bf8d1682c876 | -12.90883 | -47.96165 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8cb94916-559c-37b7-9ac2-79945dd693ed | -12.44443 | -44.74604 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46673c98-62f1-3d01-a6e2-95b7856d9ee6 | -11.83495 | -50.58443 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9597b5eb-5ebe-3ef0-9c95-b783978b86e6 | -10.79217 | -44.7852 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f75671f-3c22-305d-9cbe-f04b56d7d350 | -12.93803 | -47.97503 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3cc68de-3d88-31b1-8501-de2a0fb6850c | -14.22075 | -46.29103 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e9d92106-a77a-38ad-b9ed-bc0a6f7c3f53 | -10.23577 | -48.64437 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73a3f41d-e9aa-3560-8e88-52eb8806c786 | -20.42772 | -46.45365 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff74d666-a708-3796-98d4-d5889dc025de | -14.21546 | -46.28993 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45317b50-3887-334e-adbc-a0428d086e2f | -11.37738 | -43.50348 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d54f5730-9c6b-37a2-b516-92985d24b6a7 | -14.28314 | -45.0387 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02baeecd-0e68-32ee-b866-1f03eac60740 | -16.52573 | -51.75924 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8da8835-dea7-38be-8b9f-45a72881f74b | -11.84916 | -50.58768 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 72cb4fac-3e9b-373b-9ad6-2dafb62a6eb5 | -12.10464 | -44.85735 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61070bd6-10d3-3692-be6a-494f76389cbe | -20.09633 | -46.90613 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf33adb9-fb7c-309d-abcc-11619226f655 | -7.5498 | -43.953 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c57d2e54-eb0c-3e4a-990d-8972b95ebe90 | -11.12552 | -50.70396 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4a3b703f-b1c7-3c0b-8c4a-9393cf04bc9f | -10.76116 | -50.55435 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b56effc1-9f6a-31bc-9eab-383846b4ac8d | -11.86103 | -46.76522 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1caaf63c-4970-3b83-afa7-bec991b8d6d2 | -12.12834 | -47.59764 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README26.md)
