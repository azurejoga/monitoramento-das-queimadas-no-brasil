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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd65977b-7765-3c27-825b-a4d2ad077f6a | -13.10916 | -46.348 | 2024-10-06 05:53:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 0316b0cc-662d-39c1-95db-c95b6d2c0cd2 | -9.71335 | -64.60959 | 2024-10-06 05:53:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 009e4114-998c-333e-8559-269c5eb1aa4a | -14.56563 | -48.79737 | 2024-10-06 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4a847cbe-b046-3a82-a628-568654c3663a | -20.4731 | -51.30461 | 2024-10-06 05:55:00 | AQUA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 327.6 |
| 5abde81b-8755-3c3f-aab0-88bf48b760e2 | -20.46343 | -51.28606 | 2024-10-06 05:55:00 | AQUA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| 646b83fd-7f4b-3b4e-915b-b7aa678e7e2c | -20.46146 | -51.3031 | 2024-10-06 05:55:00 | AQUA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 81d6bfd2-c34b-3099-b7bc-c07c3eccca13 | -20.54473 | -47.47795 | 2024-10-06 05:55:00 | AQUA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8833bdd7-05c0-3311-a382-4ee5c4f6cd20 | -20.54165 | -47.50982 | 2024-10-06 05:55:00 | AQUA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 61139121-015c-3e0b-a8e6-8d0c29ff6a6d | -25.03869 | -54.07632 | 2024-10-06 05:55:00 | AQUA_M-M | RAMILÂNDIA | PARANÁ | Brasil | 4121257 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| cd36c437-97f8-3f28-9c4c-c71853e7adbd | -25.037 | -54.08964 | 2024-10-06 05:55:00 | AQUA_M-M | RAMILÂNDIA | PARANÁ | Brasil | 4121257 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 5aee8150-4fe5-38c1-87a1-b9765e2310bc | -25.0352 | -54.08254 | 2024-10-06 05:55:00 | AQUA_M-M | RAMILÂNDIA | PARANÁ | Brasil | 4121257 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 04ffdb0c-d849-3ecb-8aff-c2c7a948ad4d | -21.42435 | -57.25045 | 2024-10-06 05:55:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ed68a68e-a6a0-3814-9d8e-64e2d9b85d44 | -20.61064 | -49.36921 | 2024-10-06 05:55:00 | AQUA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e56c58ac-f86d-3703-a51c-adb587da644e | -20.59708 | -49.3676 | 2024-10-06 05:55:00 | AQUA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2649ca38-4c4c-3b61-9152-41f5c646af26 | -20.59461 | -49.39117 | 2024-10-06 05:55:00 | AQUA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e093c165-2c96-3d17-9239-b9ca6e266936 | -20.54051 | -47.48225 | 2024-10-06 05:55:00 | AQUA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ca84635e-f9e2-35c0-ac74-0230981cd377 | -20.53766 | -47.5141 | 2024-10-06 05:55:00 | AQUA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 5971c811-44b0-365e-b4b1-29b57a0f6015 | -20.47705 | -51.27071 | 2024-10-06 05:55:00 | AQUA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| e8679f55-d9be-3428-8f9c-746741ec5f24 | -20.47507 | -51.28772 | 2024-10-06 05:55:00 | AQUA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 358.7 |
| 0d122f7e-d87c-3743-9192-90e02ca80146 | -5.1115 | -56.26201 | 2024-10-06 05:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbe70162-22cc-3de1-ab27-a9b44d0502de | -5.11056 | -56.26868 | 2024-10-06 05:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb190bfb-a625-3e43-85a7-f4d4f4972ae0 | -3.52993 | -59.39864 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 363b169b-41ea-3b30-a90c-1a76fcd585d4 | -3.52429 | -59.39778 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 773a9ab6-111a-3af1-b89b-773cb4d48ec6 | -3.39569 | -59.58584 | 2024-10-06 05:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac0e04c-f0e4-3ffb-bb27-d2f5d66bcdbf | -2.62154 | -59.3779 | 2024-10-06 05:57:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ba68fa8-0ea2-3c64-8f68-18d9cda12c36 | -2.62098 | -59.3816 | 2024-10-06 05:57:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6837492a-6bdc-3730-a073-cc96633694bf | -4.29041 | -60.01983 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ea6e940-8db1-3dfd-bab8-17c2f65108dd | -4.28494 | -60.01902 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f16643-a5a8-319e-bf4a-8855b57dbe66 | -4.28409 | -60.01829 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 100529af-e561-3ef7-b869-60a41fdc8c70 | -4.28356 | -60.02185 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeb7ba6d-700a-34fc-a190-d37a6dd70296 | -4.27946 | -60.0182 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cec96c4f-d88c-36ef-87c5-7f5d83ee6d4a | -4.27861 | -60.01749 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bbf0f63-aa2b-3845-8588-a105c6c27a5f | -4.27808 | -60.02104 | 2024-10-06 05:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f892aa84-b5db-365f-8917-b1428a18594f | -4.90294 | -65.3284 | 2024-10-06 05:57:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33001e24-fe5c-3019-8c96-9bf783004028 | -6.96517 | -59.07308 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a0ae6ec-60a1-372b-b457-3a6e72e9f094 | -6.96216 | -59.06232 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 585dc6bf-81b0-3a25-b817-f1fa28055b41 | -6.96157 | -59.06681 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e49c7aa-bc3f-312c-b052-e7f01ccdcc96 | -6.96099 | -59.07129 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ab90515-b6a6-3bbd-b6ac-7d64c6c22e71 | -6.96098 | -59.05882 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 416e4987-5360-30ad-97a9-ef0b4a05e8da | -6.9604 | -59.07578 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5758af0e-5a45-3680-94be-acdd10b93ce1 | -6.96035 | -59.06332 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52ce8681-b06c-30aa-adac-395c04464a99 | -6.95974 | -59.06779 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4bd51d49-556d-32f5-82c8-8f196b4b69fe | -6.95912 | -59.07227 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e0abc156-5392-3942-b4c1-975826b08445 | -6.95851 | -59.07675 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5abb7270-6df2-3482-9e6b-7928be4884e2 | -6.95669 | -59.05698 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d8d66aa3-e0e3-3afc-b657-ca9d118742c2 | -6.9561 | -59.06152 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9f4bbd11-383a-3975-9896-4d712a3a5cec | -6.95551 | -59.06603 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5645527c-8d76-369d-abb8-f1366f4e19de | -6.95493 | -59.0705 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff5c4bc9-2d49-385e-bbd9-282a616cabfd | -6.95492 | -59.05802 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e3f1268-a53d-3555-b436-8739e666fbe7 | -6.95435 | -59.07497 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 01e1a8ec-811d-36e0-89d2-adf9dd07a0d1 | -6.9543 | -59.06255 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2cd3561f-1886-31e0-a52a-8a0d784d7f4a | -6.95368 | -59.06703 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2c00c56e-8eaf-3141-8d4c-c5633fcd073a | -6.95307 | -59.07149 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2923f786-1ce6-3c04-923a-66cc7a9ba168 | -6.95245 | -59.07596 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4a7ddfe-690a-33cd-aa58-e29972602771 | -6.95006 | -59.06061 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 77afcca2-bdef-3c7f-8b5a-cc6e0eebcf15 | -6.94947 | -59.06514 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b034e92-5dd9-3e49-b092-11801868aa67 | -6.94888 | -59.06967 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47cf68d2-03eb-3d4e-8e98-dd94477667a1 | -6.94826 | -59.06161 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c6b3e53d-9267-310a-9d14-cbee7d65bea5 | -6.94764 | -59.06614 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03343d8b-151c-32c3-9c60-8a2802ddc7b5 | -6.9416 | -59.06521 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 226c7308-512d-31e9-99ef-d815bd094457 | -9.89011 | -59.49726 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf00c3f9-41d1-3280-a6ae-23ffe8f1cb6a | -9.88955 | -59.50185 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de4bdcdb-0f9f-31b2-b48e-e74d55829577 | -9.88943 | -59.49886 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bf9e499-11b6-30df-8dde-5848ff3c5c75 | -9.88899 | -59.50653 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d09b0a02-fc9a-35a8-9a6b-589e3c1f9c25 | -9.88885 | -59.50344 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5116418e-9b24-3559-8f05-0c3ee203aea8 | -9.87789 | -59.49544 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba8d8b4e-fef1-36f8-9832-6c85b03194c4 | -9.87733 | -59.50015 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c64aa3d-dead-3b59-a6f0-36bcedca6841 | -10.21982 | -59.40418 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb67e0e0-03c5-393b-9d23-2013d0799a26 | -10.21925 | -59.40866 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2db6adfb-c77e-3851-b6dc-2aa4e1016e58 | -10.21863 | -59.40569 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6990d73a-7c16-39a0-8cc5-68a330f72c53 | -10.21363 | -59.40343 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8644f89c-897a-34fe-9b1f-317238500609 | -10.21306 | -59.40791 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e25ee9ae-7722-3993-a698-67655731d9c7 | -10.21245 | -59.40492 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2f1d859-a843-387c-86e8-e825f7fddd4f | -10.21192 | -59.40936 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d14db292-e085-3d08-af79-d11dd48995fd | -11.70981 | -58.84475 | 2024-10-06 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6933a7a-50e0-3cf8-bec7-f27b7f344bc1 | -11.70336 | -58.84337 | 2024-10-06 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01f092c4-ceac-3c75-8f55-403967b0eea2 | -7.15666 | -59.38572 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12d88cbd-4b15-3708-a843-cecb31fe5a86 | -7.15356 | -59.3818 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f175e43-1d1d-3f4c-9c18-b60a5241965d | -7.15293 | -59.38628 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1746e89-bf89-3b22-85b0-6fcc38159046 | -7.15127 | -59.38073 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1b1d560-351b-3ebf-8b6d-daddbc0d6349 | -7.15067 | -59.38522 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7363aa30-c489-374b-8624-f43e598ad2c6 | -7.0322 | -59.4029 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f26a6ed8-1f6f-3b71-bcd8-475005fbae47 | -7.0316 | -59.4072 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df12d288-4c6f-3294-97a3-659cf8487c0f | -7.03101 | -59.4115 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8d56a5d-0ade-36a3-b3ad-a0328ea317cf | -7.03007 | -59.40051 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d89e5a0-bbf9-3ada-91f0-f40543987d14 | -7.02949 | -59.40486 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93df6b39-a336-37e2-a024-d938d20749b6 | -7.02893 | -59.40916 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e57d2055-cd93-3835-a86d-8a5d290da63e | -7.02836 | -59.41346 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33cdc4dd-73dd-374d-adc5-a164a614f9a2 | -7.02628 | -59.40205 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab46309a-a86b-32b5-be4d-c316209b995e | -7.02568 | -59.40635 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33a51ce7-4f8c-3b97-93ea-58b507f17d77 | -7.02509 | -59.41064 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee003ad1-a01f-322c-831d-f41fdb6a03be | -7.02358 | -59.40396 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e3253a9-128c-3e2c-96da-0a8ddc6b5fb2 | -7.02301 | -59.40827 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f4315f9-2067-3831-a8c6-dea55d6d6de9 | -7.01977 | -59.40546 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcea79ac-61c8-38e9-b0f0-fe858b12687a | -7.01977 | -59.36163 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fbd85b3-3d11-344d-baf9-6a56c6dc25e3 | -7.01765 | -59.4031 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aaee57e6-2439-329f-b1dd-5ad744cdffc0 | -7.01735 | -59.35907 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6478feab-2b09-3f43-9f79-e01e7ff2efca | -7.01709 | -59.40739 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52184975-9be1-3b77-a15b-78ab8a248dc0 | -7.01678 | -59.36342 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86459c71-0a79-3189-89a6-f382bd754e68 | -7.01443 | -59.40041 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README152.md)
