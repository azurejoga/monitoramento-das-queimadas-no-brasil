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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c2f601-8989-393c-b86d-e04e968841a2 | -19.73307 | -54.51241 | 2025-06-05 04:36:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66bc02e7-474b-3f83-8669-c257787143c7 | -18.84561 | -53.63137 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1987d24-18e1-3a57-961e-489c649427e5 | -18.8428 | -53.62355 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6ec440f1-3e24-3290-a9cf-bb473a5efe6b | -18.84209 | -53.62775 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6e547d94-4e1b-33b5-a8a8-50b3a78d1118 | -17.09413 | -43.80534 | 2025-06-05 04:36:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e578528f-ba92-37f0-a8cc-bd8fc708eb57 | -19.07828 | -53.45766 | 2025-06-05 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 198d1287-3a5c-3591-8be6-102b6cac7e63 | -18.84912 | -53.62906 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e80317d-e88e-316d-a078-9cb7abd86c2c | -18.83858 | -53.62711 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 532270a0-145f-3f27-b955-222459d94978 | -18.84781 | -53.61878 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c9e7c20-f71b-3926-8021-3ea2fbb7056d | -20.37746 | -55.04026 | 2025-06-05 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2472889f-575d-3b95-b7f3-1d9ea34985d4 | -20.19337 | -55.06091 | 2025-06-05 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b35c7bb-5267-3163-ae50-a3ec2f433d24 | -18.84488 | -53.63558 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4949953f-c6d0-371c-a26e-db6cb5dbb179 | -18.62984 | -47.64557 | 2025-06-05 04:36:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 850c5d8d-a220-3038-9fc1-93261c84a7f1 | -18.83506 | -53.62648 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 058779c8-a1a9-3a07-a938-a56f538aecf3 | -18.84422 | -53.61517 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dceed8a4-4e45-3ee3-abc3-a70a95d306ca | -18.85054 | -53.62064 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8f00d81-e692-39ba-a699-b55b595e857d | -20.99721 | -51.79174 | 2025-06-05 04:36:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c51916aa-51f8-3906-9709-4155edfa9377 | -18.84138 | -53.63196 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a07c6504-667c-3a34-961c-3c35c7e1dac6 | -18.63993 | -46.48891 | 2025-06-05 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f91955d-5d49-326c-98d8-ff79b7b232ad | -18.84983 | -53.62485 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14da897f-ff93-3222-9eaa-13a7665f3d4e | -18.84635 | -53.62717 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc1c1c2e-70a2-3266-830c-f6819921afa7 | -19.07759 | -53.46173 | 2025-06-05 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87734ed3-25ed-38dc-aefa-05421c019f0d | -19.49459 | -45.33484 | 2025-06-05 04:36:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccfd0518-8290-365a-8a5c-433e419ffbb7 | -19.39807 | -54.46925 | 2025-06-05 04:36:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a72cb4b-3176-3b77-9e63-9a55569d3b64 | -16.68097 | -43.88379 | 2025-06-05 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1deac863-2742-3648-b7cf-6b6c55773bb2 | -20.19253 | -55.06557 | 2025-06-05 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d21f0c4-dedd-3222-bfeb-6af02605e26f | -19.43783 | -54.77443 | 2025-06-05 04:36:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b6bf765-7609-3fae-807c-846bdd47c9bc | -19.43703 | -54.77894 | 2025-06-05 04:36:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17b7152f-8aa1-395a-bfd7-3c518c56b685 | -18.84774 | -53.6158 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b6e9349-0b8b-374e-baab-d628b8e300f9 | -15.11361 | -59.32814 | 2025-06-05 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c4f44d-e808-31b0-bfa4-664ad2b3aa87 | -18.84071 | -53.61454 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df76e283-88a0-3b99-8d2a-55d4fffb6e11 | -18.83649 | -53.61809 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9440c669-5ced-3c5d-b5b2-ddf26b5bcce4 | -22.6779 | -42.85484 | 2025-06-05 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 44f98f7b-fb6b-3d5f-98ab-8d15457adfc1 | -20.82229 | -54.95586 | 2025-06-05 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ddb09b7-6c3b-3493-aec4-88690557c57e | -21.79778 | -52.76196 | 2025-06-05 04:38:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aed3b7bf-69d3-3f67-84d1-ebbd6864da08 | -22.53985 | -48.81243 | 2025-06-05 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14cfef78-1f4f-3078-b1b6-449c9f1944c7 | -20.6943 | -56.66379 | 2025-06-05 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a642302e-e13a-3f27-83cc-3ceff396a3b9 | -21.8005 | -52.76639 | 2025-06-05 04:38:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1f31976-8ea0-314b-9caa-2583876dc84c | -21.7984 | -52.75816 | 2025-06-05 04:38:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a965879a-e506-3837-bf38-521198e31f66 | -21.80112 | -52.76258 | 2025-06-05 04:38:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d4df5f0-e5df-38c8-a258-d9d3d5993659 | -13.5155 | -56.5488 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 3fb050b9-442f-30a4-9f6e-afd5a6fc6648 | -13.5344 | -56.5672 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e5c70987-c37d-308a-964b-e5a9c701bd59 | -13.5152 | -56.569 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 3f64bc35-4af8-3198-b60d-f290cf7a967f | -13.515 | -56.5893 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3365a3ac-b7e1-3481-9ae7-31f8de2bf5b0 | -18.8479 | -53.6251 | 2025-06-05 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ec485532-a600-329a-a1c0-75f9d2428e69 | -13.5346 | -56.5469 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| caba6844-d78a-3821-99a4-d6c913129768 | -13.5341 | -56.5874 | 2025-06-05 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| fa2a5183-200f-3dc7-96fa-7f1d843a1ae3 | -13.5346 | -56.5469 | 2025-06-05 04:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b7637277-0aea-3de0-bd7c-e2527fd96c63 | -13.5344 | -56.5672 | 2025-06-05 04:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d86ea8fb-83ba-354d-abb0-3def3afe2003 | -13.5155 | -56.5488 | 2025-06-05 04:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 6f933588-3d2e-39e8-991f-2a671e819f74 | -18.8479 | -53.6251 | 2025-06-05 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d3d2610d-10eb-3aba-a77b-48790e9be41e | -13.5152 | -56.569 | 2025-06-05 04:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 84826ac0-1cd7-3fa9-ad0a-db758bb75f6f | -13.515 | -56.5893 | 2025-06-05 04:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 04627af4-e142-38b0-a028-fbd0a83c824b | -4.42324 | -47.66358 | 2025-06-05 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4178b01-b080-342f-8996-6a0a23f05b71 | -6.96899 | -42.90417 | 2025-06-05 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5dc55d19-baa6-300d-8b6c-a3fdcc45a797 | -4.81876 | -44.35224 | 2025-06-05 04:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6fe3883-bb94-34bf-aaa7-82e52cf64f2f | -4.58598 | -47.86217 | 2025-06-05 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749a6eea-085a-3dcc-a015-14f33a39b6e7 | -2.9235 | -48.2337 | 2025-06-05 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a73e2f44-c5fc-32ae-b281-cf5dff7db60a | -6.20644 | -48.56087 | 2025-06-05 04:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f80d0c-dbe4-3e9b-abe5-8c0e91f1becf | -5.19049 | -43.32124 | 2025-06-05 04:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9214450d-05d9-3bf9-88dc-308d10a61ae2 | -4.41889 | -47.66286 | 2025-06-05 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e237793e-85b4-3ef3-b08f-1b1e1e0ecfad | -6.742 | -44.9896 | 2025-06-05 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 926b9eb8-6743-30be-a6ba-9fba74a71446 | -2.91939 | -48.23306 | 2025-06-05 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f35ee5a8-4ccc-3569-9d70-147fa159fb49 | -6.20333 | -48.55276 | 2025-06-05 04:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d692611e-05da-3ba2-9f90-8186dc1a06cb | -4.80784 | -45.26084 | 2025-06-05 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 050e3824-7793-3fad-80ea-be9067e8daf3 | -6.96142 | -42.91319 | 2025-06-05 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 71c41b01-6eba-3671-833a-ac178f127042 | -6.29876 | -47.00953 | 2025-06-05 04:57:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad8227b7-cde3-3d8c-97d9-b4c4c3e2b94d | -5.77933 | -43.61378 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a6a4a6-f8df-3d88-b16a-903dbe63a5ac | -5.19114 | -43.31682 | 2025-06-05 04:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6962086a-cac6-33b1-bfd4-4a606c6a00fd | -6.74589 | -44.99105 | 2025-06-05 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a656a337-1589-3605-9cf2-6251601bfae5 | -6.21332 | -43.33425 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6b1d738-0f62-3672-b7b3-f2b82ea0406d | -6.20277 | -48.55653 | 2025-06-05 04:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f14abd-307a-3f09-bdf4-4af7e10aeccf | -5.77874 | -43.61791 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d139da5a-848e-355c-b745-33186f73e0d5 | -6.96833 | -42.90907 | 2025-06-05 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ac143b50-1463-344e-8fd7-c736f7b0b09a | -2.92294 | -48.23734 | 2025-06-05 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d01d183-2a40-3f2d-94c1-d13e5d6a69b9 | -6.96208 | -42.90827 | 2025-06-05 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| a464f993-c44f-35aa-83ab-0cca4b137f0f | -4.81257 | -45.26484 | 2025-06-05 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 270d391e-dfac-3396-9c3a-11cd5c84e0eb | -5.77719 | -43.61349 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5790ae2-7559-3ec9-8cf7-94bb65e1435b | -6.74153 | -44.99307 | 2025-06-05 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f109b3a-96bf-3273-9823-325d96ed876a | -4.79564 | -47.21418 | 2025-06-05 04:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f62801-0846-30c0-b8e7-a69a0348cad2 | -4.8074 | -45.26389 | 2025-06-05 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c204f08c-1215-3a9a-991d-3f1025c5e643 | -6.21271 | -43.33859 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc503b08-8fb9-322e-b2bb-6f709c4ca096 | -6.20732 | -43.33325 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 47df4d61-1308-360a-b14c-df9e8ad0f696 | -2.91883 | -48.2367 | 2025-06-05 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9390c3c-c527-3550-806e-0751ae15ffff | -6.20673 | -43.33751 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 102e0191-266e-3840-b6b4-97fc2084bc68 | -4.81944 | -44.35364 | 2025-06-05 04:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa508455-17e9-3588-ba3b-f94258ae9b11 | -6.20611 | -43.34191 | 2025-06-05 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 094f32e5-e722-32e9-b076-72d3ed28f735 | -4.81826 | -44.35579 | 2025-06-05 04:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b412f5-c13c-309f-add0-5d46ea1e821f | -6.22018 | -48.55556 | 2025-06-05 04:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790d89fb-93d2-31c3-a91a-88a4ad7d283e | -7.61361 | -45.74997 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaac6d67-8dfb-31fc-be5d-b65465a2ae17 | -9.22577 | -48.85905 | 2025-06-05 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff242c93-3653-3c8b-946d-5554d2a4a373 | -7.00784 | -44.60526 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2de825a6-7182-33e8-b249-13cb81f2667d | -6.98326 | -47.09093 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ca75a7e-bdc9-366b-a2ed-7a15021b5549 | -11.06832 | -55.04555 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8f41cb-ae4b-3ed5-8e3d-8f7c009a2467 | -9.35646 | -47.69314 | 2025-06-05 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0baf6a49-6e7e-3c69-9bc8-db5680e204a5 | -10.87542 | -46.86568 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e7b18ec-8e0b-3f65-8ff1-71c77b3887c8 | -7.21304 | -43.1306 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d447f11-6e35-36b2-9615-bafae507b327 | -8.73153 | -47.98447 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bd10a1f-0bd0-3fba-9210-a1137103cd85 | -10.6887 | -48.96925 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb91ee1-494b-3171-b01a-2534151a5cd6 | -7.61403 | -45.74684 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README13.md)
