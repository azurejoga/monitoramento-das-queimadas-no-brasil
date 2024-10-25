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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c3fb5c7-1443-3201-a9e7-438886964997 | -17.06739 | -57.47807 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef218826-de89-364f-b3c5-adf226126938 | -17.06665 | -57.48196 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a96a0641-c150-37d6-b653-75b7970315ef | -17.06639 | -57.47821 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 402c47c4-14b3-3695-916d-4885040e0595 | -17.06509 | -57.46181 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0f152e0d-4104-3dd1-a65d-31751187e5d2 | -17.06439 | -57.46569 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 72671bd2-c8a9-36a7-a839-b3a3a8d3b624 | -17.06367 | -57.46959 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 08a19571-4ccd-3191-a9e3-cb596b5c11b1 | -17.06225 | -57.47736 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7dbfa39c-cbbc-3840-ab8d-e93084876cd5 | -17.06154 | -57.48125 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 050c4dd5-1d01-3cec-a6a6-b449169fd9e8 | -17.06096 | -57.46096 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 14886eb8-4b27-3a62-8609-332780e0007c | -17.06038 | -57.44072 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dff111cd-c087-317a-b6be-1b3b7d3b2a33 | -17.05812 | -57.47653 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bd4f8dd2-18b6-38ab-891e-edd6ffe94a3e | -17.05696 | -57.436 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3eca06b9-968a-3fb5-8cef-4e3e24360496 | -17.05412 | -57.45152 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e0e2f099-149e-3af5-8b3b-520e79d036f2 | -17.05398 | -57.47568 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5b033b83-6015-3671-b8e0-65b126456bf7 | -17.05341 | -57.4554 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 522710b8-a6ee-339c-9989-63b12fac59ee | -17.0507 | -57.4468 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 616818c6-7fba-3097-b620-a655bb34dd88 | -17.04999 | -57.45068 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7208beaf-b5f5-3e64-8abe-156d28c8a200 | -17.048 | -57.43821 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2d86a872-d831-3374-80a8-962685b4a6e3 | -17.04729 | -57.44208 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0ca00559-0890-37da-896d-f2756be72ce0 | -17.04657 | -57.44595 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f106ee8b-fcb0-3b91-9d0b-c9fb421952cc | -17.0457 | -57.474 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ccb4b8ec-8ae5-339f-b2b5-0e94bb77c4c4 | -17.04515 | -57.45371 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 63e9042f-b186-3402-a614-f9173dbafe34 | -17.04274 | -57.39708 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 771a785d-3aac-3018-8b9f-6c0eb9a7866d | -17.04244 | -57.44512 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a719f130-dc8e-3626-becb-536c0d724896 | -17.0418 | -56.85415 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 92363e93-ad2f-3a8a-943d-ecdf973dbb22 | -17.0403 | -57.45677 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 83fd9153-7c46-3c7f-94ba-2666d27482ad | -17.03831 | -57.44429 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 72293274-b23f-3d66-8919-64663de8b0d2 | -17.03759 | -57.44816 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 14194967-c703-3321-8a53-b723b045494c | -17.03545 | -57.45981 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1f661222-9904-3984-af26-6275d1677ae4 | -17.03401 | -57.46758 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 48d72795-7ee2-315d-b9f9-92fda96b6918 | -17.03329 | -57.47147 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d319633c-b834-36c5-aec6-eb24ba6df0fb | -17.03257 | -57.47536 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 080f9a69-cd65-3d6f-9b4a-085f77c82ebf | -17.03203 | -57.45509 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4ec735dd-69c8-3083-973a-3339dd5ed142 | -17.03131 | -57.45897 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 657a44b9-5e14-32e8-99e5-e702316e2c7d | -17.0306 | -57.46285 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a1f734a7-01d5-3d03-9c4c-462277190c60 | -17.02988 | -57.46674 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6c01a2e2-9329-329a-9918-13bad424b329 | -17.02718 | -57.45813 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6874ab0b-3c34-3ee8-a0b7-26941941f2f7 | -17.02501 | -57.37755 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4d89bb7c-fb16-3eea-8bc0-32b6226507e3 | -17.02018 | -57.38056 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 63bc1bdd-0002-33d6-ad47-7732ebcf0149 | -17.01593 | -56.86013 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b5e5f132-b4fe-36a6-bbb7-8a8ec6d11639 | -17.01391 | -56.8486 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 36856f57-15c1-3d74-9f5b-e113329f37db | -17.01071 | -57.36272 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ea2e67b3-e84f-3493-92a3-904b8fabaaab | -17.01052 | -57.38657 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0077accf-b98e-30e0-887f-b07ac6f38fa1 | -17.00784 | -57.37806 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fcc1b999-8c89-31f0-a063-030b6d6275ee | -17.00053 | -57.34874 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e0668454-fdd3-3286-8981-302a713daacb | -16.99909 | -57.3564 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 458fc13f-50ec-3bd9-acb7-9bcfcdd78330 | -16.99642 | -57.34792 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 0f848f00-4c07-3345-b988-f9009600f34c | -16.99571 | -57.35174 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 2da88f5f-5382-36da-b119-677d62d9e625 | -16.99477 | -57.37941 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3cf83d4f-2dd1-3427-aa65-d5e2b59aae27 | -16.98509 | -57.38543 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| de016c08-5afa-3353-b2d2-80dcbc7c655f | -16.96511 | -56.82223 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7dadd649-ab17-3e48-846f-8c50f1f9991e | -16.89534 | -56.74628 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aa757274-4285-3562-85c1-d44a82e65497 | -16.89436 | -56.75159 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 55962e3b-25fb-3467-afc6-cba8323900ef | -16.89039 | -56.7508 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b722e057-509f-3735-891b-f03671db5562 | -16.88923 | -57.27169 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 781385b5-236a-362e-afdb-ff7d3ac32b3e | -16.88345 | -57.26761 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 97f8389d-ccfb-36e9-967c-726fdf2383c0 | -16.88276 | -57.27141 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1114dbc2-5562-31be-93d3-b6cf687e8281 | -16.87936 | -57.26678 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 22137d21-8b10-3891-95e4-1646b74f26df | -16.87047 | -57.26894 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e18bd855-6b9b-3440-be32-2fe41accc5e3 | -16.86978 | -57.27275 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d9f7960a-c985-31ce-b632-920d70e787b6 | -16.83406 | -56.68863 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3cc1adbe-ea9c-3844-ac0d-4aedb5366fc7 | -16.83309 | -56.69393 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0519aab7-213d-35a8-82fe-d54529fdd7eb | -16.83202 | -56.67731 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 329530d8-ce18-31ab-a40f-50d983567995 | -16.8271 | -56.6818 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 788c7168-a127-3c0a-b02e-961f3b4e05c6 | -16.79267 | -57.41282 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 50def155-1485-3e4b-909c-43b168e81767 | -16.7107 | -57.454 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 18c500f0-1600-332a-9699-1f5f59f5d55a | -16.70799 | -57.44532 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3cd966ca-9bd8-3bb5-a034-b9eae758793c | -16.70727 | -57.44924 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0cf372c0-ea91-38fe-ab39-2fbed2dd4f5b | -17.04196 | -57.5178 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 73920a1b-b857-300f-85d1-acf0a58c6bed | -17.04123 | -57.52172 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5a22ff82-76cc-3146-a2f8-9ac6ee8ff835 | -17.03366 | -57.51611 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 79c4294b-3a4b-33c4-945c-f873e9832c8b | -17.0324 | -57.49961 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 07c10cc9-921f-3c34-a924-18666c4cbc93 | -17.03168 | -57.50351 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ded32312-440f-304c-9f8c-f2f7b143c124 | -17.03149 | -57.52788 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 40da70d7-50a3-3e0c-a123-052d0b4a746b | -17.02806 | -57.5231 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 65c7c272-3b43-334a-b661-22ddbdfaff4c | -17.02753 | -57.50267 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 86a64bad-c7e4-3360-9fb4-e29e75ed602c | -17.02734 | -57.52703 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9d06e909-53f3-376b-b176-fc71e6da6701 | -17.02411 | -57.49792 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 43543cea-dfa8-3c47-bb0d-062ad8fd28a7 | -17.02338 | -57.50183 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| abe03bd2-5105-3174-8f11-9dde022d4f4a | -17.02266 | -57.50574 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 555bc975-f5ae-3189-be82-9b93460ec14c | -16.9753 | -57.52866 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.3 |
| eecdc43b-e1d4-3f99-a927-68a88a9bdbb8 | -16.97456 | -57.53258 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.3 |
| f7d625ac-a53a-34f0-9f5c-254cdbcd87a2 | -16.97114 | -57.52781 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 9a27f6c5-68ee-3fd7-a443-afdacef95acc | -16.96699 | -57.52697 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 3af79d6e-3d56-3186-b5b1-fc56744014b3 | -16.96505 | -57.51438 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 160a5512-98e1-3903-9154-c87ebcd2820b | -16.94649 | -57.54022 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 413bb20c-7ccd-384a-84fb-3969740d5e60 | -16.94577 | -57.54416 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b2636a45-97fb-3f5d-8d37-e63bf93aa1f6 | -16.94305 | -57.53544 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c364f715-57d1-39e2-b5a5-70af2b28982b | -16.94233 | -57.53938 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 01d8c683-d9ea-30b4-af18-e7c86017185b | -16.94161 | -57.54331 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4214c15e-d0dd-3b40-9594-7be2d889e8b7 | -16.93817 | -57.53852 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 15c2e03a-f4f6-3ef6-8050-f45dcdf10010 | -16.93545 | -57.5298 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| fc546878-2cc7-3af6-81b3-5f6b74fbd130 | -16.93473 | -57.53374 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 2989dbbd-50cc-3a42-8257-4fa6e64cc142 | -16.93346 | -57.51715 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 62a70ff1-9fa5-3368-beb2-5fbb1965d648 | -16.93274 | -57.52107 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| baab8f6a-e06d-3f91-9a4e-046b5990ce9d | -16.9313 | -57.52895 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6db1a2cd-dd7b-3710-801b-3add6bd729be | -16.93057 | -57.53289 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 566c4b2c-ac23-3f1c-a3b7-621c308acaa9 | -16.92939 | -57.68135 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 49c36422-702e-37ca-9d31-94a09d3ff7d3 | -16.92931 | -57.68009 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aa1c57f8-3da4-35d3-8358-47ef0fa0f62a | -16.92931 | -57.5163 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README77.md)
