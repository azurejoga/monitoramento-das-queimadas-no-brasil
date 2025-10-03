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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45c95270-f78f-3f62-813e-50206f736877 | -11.1444 | -43.3845 | 2025-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 952bb33c-2617-3624-85c2-0f15700e25b9 | -5.8655 | -43.4214 | 2025-10-03 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ca67cddb-50a1-3652-93c7-26253186bf6b | -6.0603 | -44.629 | 2025-10-03 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6310dca0-0ac7-39b5-980c-28c7d37319b3 | -9.9365 | -43.7657 | 2025-10-03 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 4cf9da6e-255e-3b1f-9856-8bf891467432 | -14.9538 | -46.8931 | 2025-10-03 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e833ef01-5e8c-3b33-a8fa-be4e3c524a4a | -18.6837 | -47.823 | 2025-10-03 00:30:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 61644da8-e125-3f68-9de2-0dac6439559e | -12.7673 | -44.8904 | 2025-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 10344989-1050-3616-b3e7-9fd6c644b69e | -9.9369 | -43.7422 | 2025-10-03 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 9a435bce-75a5-3a0d-b775-7e09b9fbb42e | -5.8657 | -43.3981 | 2025-10-03 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 28944920-937a-3017-8921-ae01a66e223e | -5.3849 | -47.2271 | 2025-10-03 00:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 124.9 |
| d2b50286-98c3-37b9-94b9-ca4284c37007 | -9.9182 | -43.7212 | 2025-10-03 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 9857676b-1644-3e98-8a62-4ad84ec0fcf6 | -7.756 | -42.5648 | 2025-10-03 00:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| b44c1fb1-ade7-3ac0-862a-4640630a6650 | -6.0418 | -44.6076 | 2025-10-03 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6790c5bc-c44d-36c7-a211-869508ac4838 | -10.1759 | -45.4906 | 2025-10-03 00:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7f9ee1db-27e0-34a9-bf82-ca580ece3a85 | -3.9331 | -47.5655 | 2025-10-03 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 1de92cfa-7988-30bd-9766-5a4d6de75e75 | -5.6176 | -43.9041 | 2025-10-03 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fab7a111-599a-32b3-978b-daaff2b4d682 | -17.5956 | -46.6648 | 2025-10-03 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7eba25b3-a7a6-3e05-a5f4-d5a002986e4d | -7.8951 | -43.5155 | 2025-10-03 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bab35291-b1a1-358f-b5a2-f36bafa2d4a9 | -12.6323 | -46.9697 | 2025-10-03 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 9cfb27e3-11dd-3cd2-94cf-8b57653a6331 | -4.6692 | -45.7842 | 2025-10-03 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 380.9 |
| cc906df6-e5a4-35a7-9b3d-4856f441661e | -14.7336 | -48.1269 | 2025-10-03 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a83cc9bd-6bcc-3233-a22b-709184cb84d9 | -6.0416 | -44.6304 | 2025-10-03 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 8719da9a-5187-3aa3-959d-8939dc3fcb7b | -13.1345 | -47.882 | 2025-10-03 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 57463168-b2f7-308c-bdd9-526a84fa7cd5 | -5.3851 | -47.2052 | 2025-10-03 00:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 180.4 |
| b93d89b2-fffb-37e7-8efb-552fbd993cf0 | -16.3356 | -49.9289 | 2025-10-03 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e0444eb5-2056-35a8-8646-698bb41de0d2 | -12.7475 | -44.9168 | 2025-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 8ccd7443-1d30-3c67-b97e-8815a1aa191a | -12.6327 | -46.9471 | 2025-10-03 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 101df9bf-81cc-33dc-8e57-2a3fde8f1bc2 | -7.8948 | -43.5389 | 2025-10-03 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 55993560-4e54-3e3a-9626-d278fb7fc26c | -13.7666 | -48.0777 | 2025-10-03 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6c7c0d9c-a145-3e68-aaa0-9f56e1920b0d | -6.2406 | -45.365 | 2025-10-03 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| eba20eab-7556-3362-9626-eaaae6ae1317 | -5.6174 | -43.9272 | 2025-10-03 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d52eb01f-d747-3ff1-84db-78b69f79998e | -4.7708 | -44.6033 | 2025-10-03 00:30:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e1014493-3de5-3484-a87f-97ab90c9a237 | -11.144 | -43.4082 | 2025-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 192.7 |
| 3fbc45ac-3fff-3c0b-92eb-4daa5b390d5b | -11.9163 | -46.2817 | 2025-10-03 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 38df8eef-f5da-302d-b8a8-7cc7a229d523 | -7.2578 | -48.4699 | 2025-10-03 00:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 63c860c6-dd55-32fd-8ec7-e925c63e2a1a | -5.3665 | -47.2063 | 2025-10-03 00:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 1cda8034-77e0-3674-affc-b23f745ca20d | -8.6138 | -54.976 | 2025-10-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 143f338c-d0d2-344f-b3c2-3bb12da67cfa | -4.6505 | -45.7853 | 2025-10-03 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 281.7 |
| 2587afc8-18bf-3285-9179-0ac366e32ca3 | -12.6135 | -46.9499 | 2025-10-03 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0c6f60cf-108e-36b5-b6d0-e8d2fee38ed7 | -11.1631 | -43.4054 | 2025-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| d22d1096-7763-3c74-8b08-d726aafcf30c | -7.7749 | -42.5628 | 2025-10-03 00:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| a9f0964f-cf39-3255-bc7e-d9962d602a9f | -5.6361 | -43.9258 | 2025-10-03 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 126a9bd5-a6ff-3f1c-9006-185889840c79 | -7.7746 | -42.5865 | 2025-10-03 00:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 211.4 |
| eb360239-3ab3-3909-b2cd-157138181332 | -5.6363 | -43.9027 | 2025-10-03 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 268.6 |
| 5922e7d2-497b-31cf-b4f5-f099157154ec | -14.8966 | -46.8346 | 2025-10-03 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| d69c9b39-6166-38e1-bbff-ee36a8ce727d | -7.7743 | -42.6103 | 2025-10-03 00:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| c2c1c500-4b13-35ae-b30b-b66432570c6f | -4.7895 | -44.6022 | 2025-10-03 00:30:00 | GOES-19 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 292721e0-af13-3374-8756-a8eb9efb7b3c | -10.2569 | -36.3362 | 2025-10-03 00:30:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 01400f6a-8d9c-378c-b3a2-8cae3a6c8567 | -12.6131 | -46.9725 | 2025-10-03 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| bc62eccf-b81a-353a-9d9a-d4b56384da9a | -9.8772 | -47.8103 | 2025-10-03 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 57c07fd4-7215-3d82-afaa-6972b5a1609e | -7.7557 | -42.5885 | 2025-10-03 00:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 154.0 |
| 99a9881e-c722-3ac0-a45f-921c0c6e498c | -13.7769 | -47.5392 | 2025-10-03 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1fd9c860-6891-305d-a40e-a6ab10158981 | -5.3663 | -47.2283 | 2025-10-03 00:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ecf871f3-beb0-3e8f-bbe1-112ec6e4e314 | -4.6504 | -45.8077 | 2025-10-03 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 243.7 |
| ffb7dfcd-9835-3abd-8310-1222945b266d | -6.2408 | -45.3424 | 2025-10-03 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 47e403b1-0cec-3d85-a08c-d7cd46e2231a | -14.9342 | -46.8965 | 2025-10-03 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1c58b4e9-d2e4-38f4-bea5-88103826d221 | -10.2564 | -36.3633 | 2025-10-03 00:30:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| afea8329-c945-3d55-99ea-654ef21ad198 | -5.8469 | -43.3995 | 2025-10-03 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ae787468-e975-34a5-9684-a7922c7f58e2 | -8.6139 | -54.9558 | 2025-10-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 878e5a20-9561-3aad-86be-3a621df7f726 | -13.1349 | -47.8597 | 2025-10-03 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 98549de1-3e28-3921-98df-cf7452d058cb | -12.748 | -44.8935 | 2025-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 73841123-06d0-3d11-8bbe-21d11e45c09c | -6.0605 | -44.6061 | 2025-10-03 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a618905a-bec8-3f18-b4bc-2b8cf5195a97 | 1.5103 | -55.8259 | 2025-10-03 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 81cc1d46-fb66-324a-89dd-38760c39b900 | -7.7938 | -42.5607 | 2025-10-03 00:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 93f53190-c1b0-3da7-ab66-52cf5f519d22 | -7.9137 | -43.5369 | 2025-10-03 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0da405f6-efb4-3481-9cd7-8b2c174ec64a | -8.6324 | -54.9747 | 2025-10-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ef0bb139-ccc2-386f-8709-0c1b69ee5beb | -4.6505 | -45.7853 | 2025-10-03 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 283.1 |
| b41a9121-e32b-3f19-b246-189518c01792 | -7.7554 | -42.6123 | 2025-10-03 00:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 9a783ee4-70c1-34e2-bbbc-c350711ec69d | 1.5103 | -55.8259 | 2025-10-03 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4021f6c9-5160-33cf-b596-d038a34a1474 | -14.7531 | -48.1238 | 2025-10-03 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 09db7a8a-b830-3a60-b911-bd6ff3fe82f2 | -5.6176 | -43.9041 | 2025-10-03 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7d8a2aea-c8d5-3bca-857d-7cbe099a6a1d | -13.7769 | -47.5392 | 2025-10-03 00:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 57f9db7d-8d91-328c-ab83-88ebe7486696 | -6.0603 | -44.629 | 2025-10-03 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| ad5d35ab-f55c-3860-ae07-ba131d18db7e | -12.6327 | -46.9471 | 2025-10-03 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7198d6a3-d462-332c-851f-05a030afdfea | -5.8657 | -43.3981 | 2025-10-03 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e19b80cb-6a72-3417-92da-b2c2dc78be14 | -18.6837 | -47.823 | 2025-10-03 00:40:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 974c02ba-4a02-3ed1-b499-bab565484b9a | -7.7746 | -42.5865 | 2025-10-03 00:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 196.6 |
| 58299bdc-7fa0-3f4b-b604-759da83add5a | -7.7749 | -42.5628 | 2025-10-03 00:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 143.6 |
| c52cd068-7b0c-3168-aac7-1157abe64117 | -6.0416 | -44.6304 | 2025-10-03 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| fc25fd24-7805-3f36-b71d-cfd675cabd91 | -6.0605 | -44.6061 | 2025-10-03 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c4ba6a10-d3f1-3fb5-81c9-89393e3a041c | -17.595 | -46.6882 | 2025-10-03 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 28a1c2bb-e903-3502-b820-116289c72685 | -7.7938 | -42.5607 | 2025-10-03 00:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 8dff2693-621e-3014-abc3-046a6e03afd4 | -6.2408 | -45.3424 | 2025-10-03 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e97b8112-3f6d-36a7-a481-ae75b1eacba8 | -6.0418 | -44.6076 | 2025-10-03 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 586e4598-dd63-348c-b6c3-c83454870534 | -11.144 | -43.4082 | 2025-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 186.4 |
| 966c68dd-39fe-354b-8e7a-04a71395d35e | -5.3851 | -47.2052 | 2025-10-03 00:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 0bf9693d-4b32-3512-9dde-09fa7be1e233 | -8.6324 | -54.9747 | 2025-10-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 735963e8-51fe-39bf-b271-deb1304172bf | -7.8948 | -43.5389 | 2025-10-03 00:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bc60b5ad-4ba9-32ce-84a0-29c5f57a298b | -10.8739 | -47.0506 | 2025-10-03 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2cfae8d2-1b87-3a08-81d6-1b8bf03abf48 | -13.1345 | -47.882 | 2025-10-03 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| de56ae0a-f0a9-390c-b2d6-cfddf4fbbecb | -11.9163 | -46.2817 | 2025-10-03 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 481c1f47-aa8d-3e3e-94ea-f397b95cf6c8 | -5.6174 | -43.9272 | 2025-10-03 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ce17ca6c-f715-3e49-b1a4-015860e1ca6f | -14.0227 | -44.9576 | 2025-10-03 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 88b1ae40-7bbe-3ec4-8bc1-f109c8239dcb | -14.9342 | -46.8965 | 2025-10-03 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8070eee4-73bd-3ccf-ae14-e7790fe7949c | -4.6692 | -45.7842 | 2025-10-03 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 446.7 |
| 4f99177e-3ef9-38ab-91ff-01583ea08cff | -7.2578 | -48.4699 | 2025-10-03 00:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d9335ad9-174e-3915-8ed9-bfdac8d077a9 | -5.8469 | -43.3995 | 2025-10-03 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d97364af-c4c6-368e-9c4f-d8843cc2e1a9 | -5.3663 | -47.2283 | 2025-10-03 00:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8b675e32-1e7b-3e56-b8d5-290c4acae774 | -9.9175 | -43.7682 | 2025-10-03 00:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 2b9d3b09-584b-38c3-96d3-92a5f45487d5 | -12.6135 | -46.9499 | 2025-10-03 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |


[Clique aqui para ver as próximas entradas](README4.md)
