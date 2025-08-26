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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b7fbeb7-e131-3804-a71e-4998ed22a299 | -7.18846 | -47.57351 | 2025-08-26 00:30:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b99685c8-4710-3720-8ddb-e1098d6d44ee | -5.7775 | -43.6143 | 2025-08-26 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 94841161-1fb6-3665-9337-0ebab141689b | -6.94284 | -44.17066 | 2025-08-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 01de3fc4-6d65-3ec2-aaa9-7748beb7fcdf | -6.57061 | -44.21622 | 2025-08-26 00:30:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| dca0ca2b-80e1-3043-b749-031c1547118c | -8.37709 | -48.03253 | 2025-08-26 00:30:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e675952-e16c-314d-9328-9eb48d5cacd0 | -7.75517 | -50.29719 | 2025-08-26 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 82acddbf-163d-309d-9836-97b89f5e1f67 | -9.93882 | -46.47329 | 2025-08-26 00:30:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f9a7956e-d06b-30ba-9dc8-3590ef39aa37 | -9.58107 | -48.63419 | 2025-08-26 00:30:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2ebc6974-7a50-30c6-b489-ebf11e2c3be5 | -7.74541 | -50.29821 | 2025-08-26 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 917176ee-2a72-342b-b885-42d0cc3f8fb2 | -7.86074 | -45.4102 | 2025-08-26 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6fbae16d-af0c-399b-877f-499e0dc4d191 | -8.06116 | -47.35178 | 2025-08-26 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec4bd04f-d923-3db0-a21f-0c6e483284e2 | -6.61099 | -47.33173 | 2025-08-26 00:30:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9442cad0-beab-3144-9c61-e6a33e1d7bf1 | -9.10663 | -46.06643 | 2025-08-26 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 17c56ff1-5ef1-3e11-87f2-9fb2d3f020c3 | -7.74395 | -50.28735 | 2025-08-26 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 87fcc8d4-dcec-3260-818f-b59557a71154 | -7.75868 | -50.30206 | 2025-08-26 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9d43a3f0-2035-33c8-9568-0b0fcf85fab6 | -8.70316 | -47.8672 | 2025-08-26 00:30:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 95619216-4ba7-3271-9e39-b6fe2ed31465 | -6.60523 | -49.70419 | 2025-08-26 00:30:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1aa7a2c4-9546-35e8-9c84-5430ae9a27ea | -7.8568 | -46.7425 | 2025-08-26 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a09d4916-1089-3bf6-ae66-184a23728439 | -6.56218 | -44.22955 | 2025-08-26 00:30:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a963a833-eaab-3257-89e3-3dde9a7660a7 | -7.63123 | -45.23068 | 2025-08-26 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2e08885c-da07-3d91-96a2-9422218db314 | -8.28763 | -46.33493 | 2025-08-26 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 05de2d6f-1f02-3946-b0b9-c10fc671569a | -8.3335 | -50.56842 | 2025-08-26 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 210.2 |
| 6eaa30d4-23c0-397d-958e-21e43bfee2e8 | -7.59156 | -46.23548 | 2025-08-26 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c46d75f-b00b-3aa4-a45b-5ac35ad8e193 | -8.12229 | -47.12908 | 2025-08-26 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 758c1923-07ce-39ac-959d-af71ddfc0bfc | -8.91111 | -49.90239 | 2025-08-26 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f4587e3-a163-3526-98c0-05fb4f9b76ed | -7.21109 | -45.31247 | 2025-08-26 00:30:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| a3ab7696-a84b-3797-bbdd-c3d6dc09435a | -6.94458 | -44.18254 | 2025-08-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56cc1873-b65e-35ed-b1f5-55b5375efac4 | -7.59563 | -47.51218 | 2025-08-26 00:30:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d9b6d27-6178-308c-8249-6562acd3490f | -8.22344 | -49.56489 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e2bf3edf-7b9d-3c26-8838-c16cfc34179b | -7.78259 | -49.4934 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 418b2599-9278-3724-82c1-49f2f8eb755a | -8.467 | -45.84538 | 2025-08-26 00:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b65f5337-8036-3c07-98ea-e9d82031236d | -6.56043 | -44.21777 | 2025-08-26 00:30:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a8b119fd-7788-39d9-b9cf-fdd74a19c536 | -8.22212 | -49.55485 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 58f02e1b-69e1-3fcc-a3b7-d900f2da7c42 | -8.12684 | -47.29128 | 2025-08-26 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf989867-f470-3449-bedf-2222fd5cc58c | -8.47765 | -43.67183 | 2025-08-26 00:30:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d1dc353e-11be-3550-b575-b7f4c7dafdc0 | -6.14468 | -44.38232 | 2025-08-26 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d097eb5b-8da9-3f4e-8fda-6b6b339698d2 | -6.76696 | -42.9872 | 2025-08-26 00:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 9ba6f0d4-35c9-38bd-adab-f49bfa18f0c0 | -7.7776 | -46.57581 | 2025-08-26 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0cb6dad-48d5-3152-bb29-f1609c598eba | -6.19373 | -44.16032 | 2025-08-26 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9eff24a9-f451-3d0e-b7cd-2905f15bef82 | -8.36253 | -49.55996 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3e12ef3c-3175-3ecc-8515-bab7d6215d04 | -8.33503 | -50.57987 | 2025-08-26 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f114d43d-6557-35b7-a440-f5717a1f60a8 | -8.28634 | -46.32579 | 2025-08-26 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a6b8042-3ded-3657-a04a-2b5111425299 | -8.37587 | -48.02356 | 2025-08-26 00:30:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 79e4496d-6382-3e47-8d53-77a0571ef7c4 | -6.1919 | -44.14795 | 2025-08-26 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 72dcd6d4-2ea0-3f60-aef5-ee834b37d138 | -7.53544 | -50.55104 | 2025-08-26 00:30:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b9e8f54a-f87e-3217-b63e-c83f8197530e | -7.85554 | -46.73352 | 2025-08-26 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d51f5f37-8fe1-3fbe-85ef-54da5b6a39b6 | -7.58436 | -47.49575 | 2025-08-26 00:30:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6b330bc-0cb5-306c-a2fa-a99a4595e271 | -7.65747 | -45.41129 | 2025-08-26 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e530a7a-f91e-3006-90b2-e50b37fe07a7 | -7.66396 | -45.39024 | 2025-08-26 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cec9e79e-add2-329b-a01e-93caead541cd | -8.32353 | -50.56977 | 2025-08-26 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 45fe38e7-6b33-3051-a843-34899e096c96 | -6.10314 | -43.16125 | 2025-08-26 00:30:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3e535889-aa5f-3a32-a3eb-98fd7ce5e998 | -7.52414 | -50.54123 | 2025-08-26 00:30:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 28063940-77e7-324e-abfa-eb40149fec62 | -5.79506 | -43.88308 | 2025-08-26 00:30:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 15342336-5a3a-3d58-8608-9afe5bef5851 | -7.90006 | -45.87897 | 2025-08-26 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d64194e-a2c1-3fb9-87d6-22ba28658a2f | -8.46565 | -45.83592 | 2025-08-26 00:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9ef1490d-0f41-3f7b-82fa-d14c6e2e47fd | -8.71202 | -47.86594 | 2025-08-26 00:30:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aba59fee-4dc9-37d4-83b7-e6646ba73b00 | -7.2156 | -44.42181 | 2025-08-26 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e1623a32-32b0-35cd-ab7b-0825e8670182 | -8.07248 | -49.66942 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 188e1ac9-bab3-30c3-9567-2e966d7e7005 | -8.21275 | -49.55615 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60976208-dc17-35c5-8306-b3bedebb3885 | -6.80628 | -44.99322 | 2025-08-26 00:30:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a8879fa6-583d-3b0d-9d80-822300d116a1 | -8.21408 | -49.56623 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89b01db0-c6d6-3deb-9ac8-2718e61bd6ea | -8.32506 | -50.58122 | 2025-08-26 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| bac87bba-e77c-3d05-b200-47802090bd75 | -9.05058 | -49.56226 | 2025-08-26 00:30:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 34b656c1-2054-3265-8965-82440ad21ad4 | -8.36389 | -49.57006 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 724024e0-99b8-38ff-80ba-3fbf25dc490f | -9.27059 | -56.89511 | 2025-08-26 00:30:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 7252c8f1-18d3-32e5-bc61-f5c797633fe9 | -2.64706 | -48.05425 | 2025-08-26 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 76dd2447-eb6c-3d7b-921c-75166d25b772 | -4.93796 | -47.55362 | 2025-08-26 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b7a846e6-f1ae-3335-8c31-19b299c6d33e | -4.78951 | -47.28111 | 2025-08-26 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 86924473-3be0-3798-974d-9cc722495b61 | -2.93544 | -53.69799 | 2025-08-26 00:33:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c89dc201-4fa0-3112-b503-c33da9f2b27f | -4.0753 | -48.04279 | 2025-08-26 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b91b29c5-1f50-304a-9517-443848e7940c | -3.9877 | -47.88171 | 2025-08-26 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 0ef73e3d-b054-32a8-b873-145bc3be0fef | -3.20036 | -49.1128 | 2025-08-26 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e034f0e2-6cd7-3be0-bcc8-7032719c9177 | -3.06364 | -40.04151 | 2025-08-26 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 08108cc4-0b8d-31f1-aa71-8192141e14aa | -4.97237 | -55.82165 | 2025-08-26 00:33:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f886dea9-d25f-3018-9767-29432d587267 | -3.17662 | -49.47801 | 2025-08-26 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 665eb543-8a95-3137-b8e0-f1971ffb50ca | -3.98892 | -47.89052 | 2025-08-26 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 6b62ac80-008d-3d60-813b-aad689b423a6 | -5.79016 | -46.13897 | 2025-08-26 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0683ba9c-24cc-35a9-8bc2-eb7889867c4e | -3.06578 | -40.04794 | 2025-08-26 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 83.9 |
| d7763ba4-6393-3ff8-aad6-2f73d0f5732a | -2.26079 | -47.86162 | 2025-08-26 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f5a7ab64-1f40-336d-b136-eeb727ce74c6 | -4.70042 | -56.05953 | 2025-08-26 00:33:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0393bc82-d579-3b1e-8b20-702fa034bd5b | -4.82121 | -47.31313 | 2025-08-26 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b36d1357-e278-358a-9fb2-5ac7e4c82bae | -5.64825 | -44.35241 | 2025-08-26 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 51daba0d-111a-3a69-9799-9f8c2fbf4ffa | -4.48382 | -47.66681 | 2025-08-26 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d045e648-33ba-3b37-be80-c352c5e80488 | -3.20158 | -49.12169 | 2025-08-26 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0eb8c37b-e50d-367f-8ea5-05fa3ba1d1fb | -3.25248 | -46.90693 | 2025-08-26 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5b9c2fe5-7e4f-35fc-936d-75d7cc8097e6 | -4.96178 | -48.19473 | 2025-08-26 00:33:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ccf8c099-8818-374e-b578-de15a0c3d0ae | -2.98678 | -49.30613 | 2025-08-26 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6bd0463e-9c6e-3278-8170-e0122a939c40 | -3.16768 | -49.47924 | 2025-08-26 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 781fb04f-b1d8-3c7c-8fab-9763dae3adc9 | -3.92521 | -47.6921 | 2025-08-26 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 88db2b15-4865-3889-98b5-1ab65bc103ff | -4.82246 | -47.32206 | 2025-08-26 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e480d27c-26f6-37ad-b5a7-72f408ef6c27 | -5.82996 | -46.35658 | 2025-08-26 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5a5153a7-ca37-34e1-8011-c0ccbb1b8d34 | -5.39696 | -45.15004 | 2025-08-26 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ad023502-7ba6-3849-ab8e-29d0f128091b | -5.6585 | -44.35096 | 2025-08-26 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ea24892f-94ca-35e6-bb03-cf6c68039b12 | -3.36538 | -44.19188 | 2025-08-26 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 265107b5-3225-3bf0-9719-4fdd96d48cfe | -4.78825 | -47.27212 | 2025-08-26 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa6b179e-3602-3753-b925-6932bf28cfb0 | -2.29308 | -47.88752 | 2025-08-26 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7336f22-8f69-3a79-a482-faa543dff60a | -4.01931 | -49.51006 | 2025-08-26 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 964fb69d-c788-3833-86ab-a2983f703948 | -4.01805 | -49.50089 | 2025-08-26 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b2eab15-8eb5-3ebd-8222-28f01a775a4c | -6.65091 | -53.18826 | 2025-08-26 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 24369413-ce06-3b0d-b0b7-0e2ad5a774cc | -2.25955 | -47.85268 | 2025-08-26 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README7.md)
