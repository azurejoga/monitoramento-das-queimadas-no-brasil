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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3fe3fa6-7b19-3509-93d1-4d9249f1153e | -12.77254 | -47.37494 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6620daa1-fcef-3eef-a147-3c454b54abee | -6.77059 | -45.47871 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30eba0d7-de4d-37b9-9595-1d280c71d336 | -17.00699 | -49.15186 | 2025-10-24 04:19:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe22c7b5-6b40-3738-8fec-5ced52e42e66 | -12.77117 | -47.38308 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 55497973-3382-30fb-9525-37eff37b76b4 | -15.83364 | -49.10098 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b866848c-6b60-386c-bd68-38d41a63d662 | -7.62656 | -42.20809 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4addfd5b-9290-37c2-83f5-91573f9d82cc | -6.92042 | -42.23405 | 2025-10-24 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42bf625d-3a56-31dd-98bd-af66e10a846b | -13.53878 | -47.54535 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f9293e-b5be-3218-9e8d-dc5398dd15cb | -14.27392 | -48.06575 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4811e6f8-58a1-3472-968f-ed0618941392 | -8.34546 | -46.17729 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c65eb89-d876-3d83-9e57-3292c64a5098 | -17.04296 | -42.72847 | 2025-10-24 04:19:00 | NPP-375D | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 47c9ead8-e853-3531-bc84-9fc10a3827dd | -6.78165 | -45.47656 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 459cfffa-a4cd-3d3f-ac01-dd01afbb253d | -6.7722 | -45.49072 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 8cd98729-7f2e-33ef-8ccb-5f1dd3a04bde | -8.47147 | -45.65469 | 2025-10-24 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 181d4d63-afa2-3348-b9d6-fbacb9ec5c53 | -13.12475 | -48.57977 | 2025-10-24 04:19:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04794bb8-0a59-3b63-a012-a4353e4b6d30 | -14.56633 | -44.81687 | 2025-10-24 04:19:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ce7972b-1498-329b-b109-6ab8824361fa | -7.27525 | -50.0069 | 2025-10-24 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0853267-a5b6-3101-bdfd-d44b89fac525 | -14.76184 | -49.29722 | 2025-10-24 04:19:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a353bb25-c9a2-362a-97ca-2360c3aea41a | -6.27649 | -47.01749 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7538fa0-1d34-3913-baa6-bf84d338a213 | -7.63941 | -42.16971 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaf77022-f1c2-3cd0-ad41-012f1f9c649a | -13.28451 | -47.48775 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c481f2-b364-3d6c-b5aa-a996d55beb57 | -8.61967 | -44.80854 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 008719a3-c382-338e-ad8d-1932ee8cea7f | -14.43453 | -50.95515 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4125ff4a-928b-35c0-b872-a30b80d1e8f2 | -12.81914 | -48.6707 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea07ac76-e5a4-3977-affa-c5ff2aaf2111 | -14.42531 | -50.95755 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50cdd11d-2591-3abb-98d2-9b83bb3ea295 | -8.20658 | -46.98182 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3f192d2f-ede7-3b22-9529-8734a73e72f2 | -15.87096 | -45.25634 | 2025-10-24 04:19:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69022e96-4bb7-371a-949c-4766dd70371b | -15.13056 | -49.55645 | 2025-10-24 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f5ed56b-8c84-384d-90ea-37e039885358 | -13.36594 | -50.46788 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b53d480a-6ece-3751-947a-9b3f5216df05 | -6.74743 | -48.06034 | 2025-10-24 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a51e80af-589c-3f68-883f-d9c7a994d0b8 | -12.80808 | -48.66118 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26d172ae-cfb7-3559-95c0-1590a084dab5 | -12.82956 | -47.25128 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb9852e-5c3f-31f2-bd08-ac0927a45d44 | -19.60013 | -43.68831 | 2025-10-24 04:19:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73e0b344-a2c3-3641-9b7d-adadd8392fec | -17.37287 | -52.01809 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6428de1e-cb9e-3010-8d5a-bc470d68bf31 | -7.49211 | -42.57676 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a65d4fb5-9398-3809-b4ca-f1bf7910f27b | -13.33402 | -47.96703 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 954d5769-568b-30db-80d0-430db062b714 | -8.46574 | -45.56055 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9715e1-e88a-323c-b344-818692b87198 | -6.80239 | -45.43673 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cadab9b5-ccb2-3ae2-a870-20fef7e4bd3a | -16.37172 | -51.54929 | 2025-10-24 04:19:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1be19eff-4f2a-3698-b160-98bfa92a7e0e | -13.35579 | -47.97059 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1621ce03-6eee-3ede-b839-1054dbfc8a38 | -19.65117 | -43.63337 | 2025-10-24 04:19:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1bd5bc88-4c88-3ba3-9137-6ce98ef51011 | -13.92293 | -50.25824 | 2025-10-24 04:19:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 445f8c52-c3b1-3543-99bc-f86982a2dc8c | -7.28924 | -46.27659 | 2025-10-24 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c2a1cec2-f0b5-30c3-88ec-b2e8c8b7b9c1 | -7.33645 | -49.04576 | 2025-10-24 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b43664c9-c81c-3c48-896d-b532780e3358 | -7.8508 | -49.65399 | 2025-10-24 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37c85269-42e5-34a1-aaca-49301ff7621a | -16.31494 | -46.57217 | 2025-10-24 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78dc2c51-7837-33a8-994c-827adf5d471c | -8.03844 | -39.86691 | 2025-10-24 04:19:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 88c14a12-1b73-327d-b88a-aa086ec58396 | -20.20722 | -45.807 | 2025-10-24 04:19:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4bb71890-7bdf-3ef9-b143-9ca5a9f7a58d | -11.32597 | -54.26361 | 2025-10-24 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4675d63d-ceb2-3448-976d-2ce1eb8d5a04 | -13.65022 | -46.80902 | 2025-10-24 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ea7c73-89b9-353a-aebc-6faf1262c7be | -7.63048 | -42.20502 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1c681c78-99d8-35ed-9608-2ff684131052 | -8.02585 | -45.15169 | 2025-10-24 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ece7fa55-e2aa-3ea3-96c3-a09900c41dab | -6.74749 | -46.54812 | 2025-10-24 04:19:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bde2f94-4a85-3b8c-aa95-fb2791ac03c6 | -17.66123 | -46.64948 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a453e96-1d4b-3f35-b754-9087f1e28d72 | -18.00145 | -51.22002 | 2025-10-24 04:19:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6b338a8-80cc-3388-b8a0-75fbc1bc8a0a | -13.28583 | -47.47989 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5abb3a-a051-39ae-9980-b099bf0e3f64 | -12.82187 | -50.94394 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93f4263a-d7ed-3820-be06-d7ff02de0365 | -8.19266 | -44.43711 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3015a442-cdff-3687-97a1-ede6b4696a53 | -6.85933 | -46.9303 | 2025-10-24 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d40baf2-b90e-3bb6-8cb3-880b1da286d9 | -7.63104 | -42.20142 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24478fc1-d337-3af5-8c40-5ed1dd2e157f | -6.77532 | -45.47162 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6adf7b1-639b-3f0d-bcd8-82b57dc5fb44 | -6.97739 | -45.28591 | 2025-10-24 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 690c6881-a9a8-365d-b49d-852b99b6022b | -7.38678 | -46.54187 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e10e93ea-e183-3080-b786-537e497e508c | -7.14823 | -42.54447 | 2025-10-24 04:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b93a3cda-807a-3745-baf1-7dfa98b01c8a | -11.48489 | -54.0233 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1625bc1-8165-3493-92b6-72ffbef0d102 | -20.40866 | -44.06349 | 2025-10-24 04:19:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11ffa54a-be11-3565-a43a-750451a95c4a | -19.02477 | -46.18611 | 2025-10-24 04:19:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5b019eb-207e-3153-9ade-959a44a06cf4 | -13.3601 | -47.9671 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 882045c1-6406-33c2-b03a-311e8fce0d02 | -13.02758 | -48.58302 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b818ff42-f7ae-342d-8458-32ad4cce9f3c | -8.34152 | -46.20164 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c7895be-16f4-3ccc-8b22-a874b58454f8 | -16.95462 | -53.22281 | 2025-10-24 04:19:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80cf1c37-8ae3-3ed2-92ff-2c4907606b0d | -14.74895 | -46.6096 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eb9e353-a353-3726-b8f1-7ee30cd12c7e | -18.01179 | -47.6392 | 2025-10-24 04:19:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8537b6fc-c429-3115-a5c9-2a5a0130aaf1 | -16.87252 | -49.21176 | 2025-10-24 04:19:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de8c05b4-0415-322b-9fae-194ea690bfc0 | -7.78546 | -45.40597 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 689e16d8-003d-389b-92c3-8f81166eb1c7 | -11.48627 | -54.01603 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97ec9c6c-3e63-3237-9c4f-93a923239b1d | -6.94307 | -44.01659 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91281fdf-31cb-3b9d-8417-f37c6e22c9ef | -16.12639 | -54.00288 | 2025-10-24 04:19:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6945932a-9148-3d3d-933d-9b651340a099 | -17.0394 | -42.72785 | 2025-10-24 04:19:00 | NPP-375D | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 429f85e5-cc06-3bc1-921a-deaa3d08631c | -7.7265 | -42.3734 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bdf3be40-fb02-39e5-838e-12e7a3f610a4 | -7.64297 | -42.30224 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 870bdbfd-6ffa-3645-bdac-e5fcd416a3f8 | -17.60219 | -46.63151 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58b29d10-8ce9-33c7-bcb1-4d1398055efc | -7.39956 | -43.91347 | 2025-10-24 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1a28162-93f8-31d7-8f7b-e3e3fd575717 | -18.60551 | -51.7884 | 2025-10-24 04:19:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6655d6cd-4999-36fb-8221-2490477f1e46 | -15.83737 | -49.10156 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e13572d-304e-3e5c-80c4-8851dfab5ce8 | -15.13085 | -47.9348 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d11a7d1f-4156-3bb3-b76e-5757531dc509 | -13.21318 | -47.73443 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac27569-1975-3919-ae37-1bb6a1d91cdd | -12.66371 | -48.62584 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8985f0f2-3bc6-341d-8f78-b05c442d024f | -13.28091 | -47.48746 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3efa336-8d61-38d4-b9a1-ea06f3531f0e | -15.612 | -45.92503 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc3c6ad2-5b1b-386f-911d-7ff4ea9a2be1 | -17.75661 | -50.96746 | 2025-10-24 04:19:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1505e88-6f78-3f7b-b48d-ca234fa9eec5 | -12.81536 | -48.67001 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c2cb5d-063c-3673-a458-3cea79a41a92 | -6.79045 | -46.46803 | 2025-10-24 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa885a51-1358-331f-83f1-93b99c8337a4 | -8.12695 | -41.08238 | 2025-10-24 04:19:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1fd0cfe8-7244-3736-925b-8d1c01b62b24 | -13.34494 | -47.96861 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 705bab8f-9f2e-389a-830a-a6a26ef19476 | -15.3603 | -48.09668 | 2025-10-24 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d33bd653-6270-3e0d-911a-014cabc24f95 | -7.62485 | -42.19681 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0f3aabd-d00f-32ba-acfe-a8c30c232090 | -15.56064 | -45.94585 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f78e50a-830e-3ad1-93f7-74cd82f919d9 | -7.68724 | -42.23953 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3e0fa4d-9472-32fb-b764-1927e8cce4d8 | -12.81401 | -48.62772 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
