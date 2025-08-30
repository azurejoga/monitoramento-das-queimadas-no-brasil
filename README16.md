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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cadc0b91-0bfb-3cca-a610-240c0d43e33f | -13.18991 | -45.28681 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d15476b-5b15-38cc-a069-9de3d5fe8e1a | -13.35687 | -46.8847 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1e5e525-7334-387b-9649-2423d7f3024a | -13.39979 | -46.95811 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77688f2d-71df-3af1-b4a7-6c600ae4fe27 | -14.62327 | -48.08586 | 2025-08-30 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74eb4530-b8e2-3a7e-a6fd-d9224532bb85 | -14.00137 | -44.5989 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 58abce98-8358-3860-a7f9-e6294419c6fc | -14.00887 | -44.58971 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 386cc51c-af8d-3c93-b3b5-7f001773f2b2 | -13.38265 | -46.96135 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ab72d601-88d6-320c-8fc7-ff3bcd9d536a | -13.38922 | -47.00691 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7b5e7eaa-d47b-35e4-a00f-efd2af205039 | -14.03592 | -44.51674 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c8dcd9e-0c39-3b59-ab71-91373e92a411 | -14.00221 | -44.59279 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d126c14b-8ab8-3ebb-b661-2a823d5e1021 | -13.62784 | -48.18387 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea5b557a-0b05-3b09-b233-813e36e91a2d | -13.19642 | -45.28897 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bce5c4f5-24ec-3943-9d1b-14ce36e5c45c | -13.36775 | -47.00849 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 648dd5f4-db98-35a7-a364-03c8e7bc265a | -13.6272 | -48.19704 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04236cd3-83e2-3b39-bab2-c56e059ccfa0 | -14.0573 | -43.56697 | 2025-08-30 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c9f80a9-cd51-3807-8f08-3e466c95bd3f | -15.07568 | -48.6357 | 2025-08-30 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4285e355-1b3b-3733-934f-4ea739e19e55 | -14.01766 | -44.54712 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2981764-ca58-31cc-a604-2bdfb1deafcb | -12.93971 | -46.1512 | 2025-08-30 03:32:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5ae0edb-3a01-31e9-bfa2-9539be05ac07 | -14.02374 | -44.48862 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02263d18-6340-3d9e-9a21-4a9affd7a5fc | -13.47011 | -46.96799 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 422f07cc-f8ef-3ce5-9361-fdc30cdc3285 | -14.04083 | -44.52198 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ef146b6-e311-3517-9600-095b29236ed3 | -13.38644 | -47.01976 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f010d34b-5ac4-306e-afe7-9b75f500fabe | -14.00392 | -44.58611 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 63aee821-8e3b-3110-8261-db0b2aefcd5e | -13.41481 | -46.95357 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a4d24e7-e659-37a9-91a7-e36d7fd07a80 | -16.4095 | -45.65317 | 2025-08-30 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10c534d8-53b5-34d3-8b84-07c263eeee2d | -13.99902 | -44.58055 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c033de5b-6c6d-3761-9aa1-fa4d9e4fab1d | -14.03427 | -44.52476 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7a5d491-1dc6-30dc-80b3-fa0d47ca1ce9 | -13.39075 | -46.99989 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b8243281-19fd-39fe-b3eb-0401b8a1cb1b | -13.3609 | -46.99786 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5f5ceeb-9148-35cf-b650-d1d163967d01 | -13.40378 | -46.96089 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8df7c6c6-94a6-3039-afb5-31a36411e793 | -13.43694 | -46.94849 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1faa7865-24c4-33bf-9504-3ec0763bba0f | -13.1974 | -45.28416 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 913d3932-675b-3a07-8495-d7bf0e96d807 | -13.3896 | -46.97272 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1f224733-6eef-3efd-a0a7-f111083e921f | -13.97313 | -46.32709 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c03f2f69-43d1-3d0c-85bb-d6b63836a5c2 | -13.39631 | -46.84529 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e5abfb-9489-372c-a08d-f734747a1ebe | -13.99912 | -44.57859 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b217e18-2b44-32f1-a097-8f56b5726e60 | -20.08481 | -48.2777 | 2025-08-30 03:32:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf0a3fb-2034-339e-a58a-36f1290c9988 | -13.96511 | -46.33667 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ef9911e-f87a-3a1b-afda-5d060f86b3c6 | -13.50408 | -46.94083 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91dc7e0b-5999-32bd-bddc-791a4188582a | -13.36229 | -46.99127 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e388f3d-ac4d-35a9-92de-601c90bd82d9 | -13.39673 | -46.9611 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3679af2d-7124-30f2-9c6a-096d9d91ab77 | -13.75924 | -43.77542 | 2025-08-30 03:32:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8355adc-8517-3bd9-beb9-355f6cc7fab7 | -13.36493 | -47.01204 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0bda262-09a2-3be9-ba93-23befe76ad6f | -13.98054 | -46.32721 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04b58188-f3e1-371c-b179-893b3dbb58fe | -14.03031 | -44.48578 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0369c423-ebda-368d-812f-50d551198090 | -13.37443 | -47.01019 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a58b64c4-0eda-373f-a212-1dab2b2d8b10 | -13.99324 | -44.57934 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de9e8dae-5be6-328f-890f-e4c06855cbc6 | -15.07718 | -48.63925 | 2025-08-30 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dae3e4a-f037-3900-9a96-4b09a95c0be8 | -14.84201 | -46.7414 | 2025-08-30 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9d3a087-016d-3c2f-97a6-d31f924c79c5 | -14.00265 | -44.56155 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b3b504e-955b-3730-b06a-65d0c1749388 | -14.00091 | -44.56997 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a5506a9-8b72-34df-9a55-25e53a9e4fc0 | -13.38775 | -47.00393 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5eaa689b-ce79-3437-ac13-2c1688c917a3 | -18.79843 | -40.16011 | 2025-08-30 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d220ebb-bab4-3dc0-80ee-ffd3ad41eabf | -13.37979 | -46.97496 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c9217e36-8e53-3ca5-9e9c-a45bfbe07baa | -13.48051 | -46.84264 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e38aecb-9f5d-311b-ab4c-bdce91eeed32 | -13.6797 | -46.88513 | 2025-08-30 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8b442d-2627-3bec-9836-8796c2f20ed8 | -14.0016 | -44.5676 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d282e786-c7c5-38c8-a549-717158490cf9 | -17.70178 | -47.28854 | 2025-08-30 03:32:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 780b3724-9cdf-3a81-a7a7-1c67a8d9b2b4 | -14.03674 | -44.51272 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6be7c605-9842-3884-8c57-2b365e7902cb | -13.37188 | -46.97916 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30730e40-d4d4-350b-b394-3a0b269fad27 | -12.92341 | -46.35783 | 2025-08-30 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e71f8e6a-57be-30f8-a94e-b610211edd83 | -14.61478 | -48.08078 | 2025-08-30 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 715b5a1d-ff37-3bea-aeb7-571f893aa45d | -13.75373 | -43.77423 | 2025-08-30 03:32:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275b8e61-c758-3966-a3cc-94900ad4b841 | -13.98165 | -46.32205 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71fc4f13-687d-3899-a1a9-f8a6376d2dff | -14.00756 | -44.56692 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc74587e-5faa-3812-9bb5-99c3ee910a30 | -13.57516 | -46.90289 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2968749-842e-32e6-b623-78c87e3cd02d | -14.04007 | -44.49651 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b24c02fa-4f69-379d-9c23-729f356a01be | -13.50544 | -46.83838 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47c086e7-857d-373b-ab72-c01bc38ff80f | -13.36236 | -47.0242 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99dfae27-f93f-3c98-b641-da3405c72e19 | -22.68599 | -46.8471 | 2025-08-30 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68d4a101-98f7-3b54-8840-77afb59b7779 | -22.84552 | -47.49469 | 2025-08-30 03:34:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b811df8-7ed2-3e9e-899c-4a000c41b638 | -22.84448 | -47.49914 | 2025-08-30 03:34:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 863dc61e-0905-3c7e-94b6-bd43045bf549 | -22.68486 | -46.85202 | 2025-08-30 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15789d2d-b10c-3839-85e7-1fd9cb4f4d63 | -29.02306 | -52.37127 | 2025-08-30 03:36:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 47b998dc-1210-3cf5-8fcf-a6eb1b66c766 | -29.02977 | -52.37277 | 2025-08-30 03:36:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad43fcde-113d-3623-b101-93f9e524a455 | -6.5263 | -44.8659 | 2025-08-30 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a75dbd1c-bcd2-36b2-8e9b-773619640e54 | -9.4497 | -62.3485 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.6 |
| b32aca5b-46fe-3144-a6e9-87bb4ad5cf71 | -9.4683 | -62.3476 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b49f5830-a79f-3056-8793-08bb10760f3b | -9.4247 | -60.5509 | 2025-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 68057ba7-c174-34f8-96f0-f33757d66c75 | -9.4435 | -60.5307 | 2025-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5d061c08-0e64-3497-b519-ff6097b1fe91 | -9.4498 | -62.3294 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 7aa507b7-8aef-305e-a864-e2a42aef2397 | -9.0613 | -65.4542 | 2025-08-30 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 495f6364-257e-34a4-b509-7aea16e084e5 | -6.7814 | -43.7865 | 2025-08-30 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5ab693a3-bc2a-31ac-8bcf-650547e3470b | -9.4684 | -62.3286 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 80eaedae-7353-3fea-aac3-3245326d8378 | -9.4433 | -60.5499 | 2025-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 202c8ba6-c7e0-387a-8529-7072b0e8120d | -9.462 | -60.549 | 2025-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1bd6ddce-68b1-3509-bb46-7815b84fb599 | -6.1853 | -43.3257 | 2025-08-30 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 343.3 |
| 62e73a47-2cec-311c-a7df-ad07dadea83a | -9.4432 | -60.5692 | 2025-08-30 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 3bd8aeb1-7f1b-32d7-b60c-407a074b7963 | -8.9126 | -62.1058 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6d62edf5-c814-3cd1-9923-25a8684e7797 | -9.0614 | -65.4355 | 2025-08-30 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6685e5a9-2712-3ef7-9af9-94f7951cf932 | -6.185 | -43.3491 | 2025-08-30 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3e517e1c-c463-31b3-a6ad-bffac5d67665 | -9.4312 | -62.3303 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e61f895c-6e55-312b-a577-25aa0dac7cf1 | -9.4311 | -62.3493 | 2025-08-30 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d573985f-bf1f-3a49-8d25-dad4835ceadf | -9.1155 | -65.7699 | 2025-08-30 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0cf1544a-b125-3f3d-9171-362194ac7275 | -6.1665 | -43.3273 | 2025-08-30 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| b556017e-889a-3ee7-867c-0cb357205943 | -6.1665 | -43.3273 | 2025-08-30 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| e8346966-18d6-3dd8-8392-8a501a5e4fba | -9.4432 | -60.5692 | 2025-08-30 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0583e6cd-d7a6-3175-a2e9-cda8605b0547 | -6.1853 | -43.3257 | 2025-08-30 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 349.7 |
| 045567b8-20a4-3201-8318-749110d1883b | -9.0613 | -65.4542 | 2025-08-30 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8823bded-af75-340f-a75a-5eeb85340d7b | -9.462 | -60.549 | 2025-08-30 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |


[Clique aqui para ver as próximas entradas](README17.md)
