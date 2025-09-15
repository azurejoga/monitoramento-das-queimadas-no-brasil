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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b22c8819-f9c1-3c03-8ea0-3736f39d1cd4 | -21.11893 | -45.95697 | 2025-09-15 04:53:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 884ebac7-86df-39c3-8f60-ac69fd130b53 | -22.99441 | -49.94558 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7686d78-f75b-3e9f-a59d-5fb64bfde12e | -22.50667 | -52.97897 | 2025-09-15 04:53:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| dbbe6060-f554-3815-8095-15d146082998 | -20.08503 | -46.88603 | 2025-09-15 04:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f267ff87-bc56-38ba-b077-ceb464541e6c | -18.97944 | -48.58962 | 2025-09-15 04:53:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 11f3a7e2-d33b-3627-8e3c-3d20198c4ea1 | -23.60095 | -47.38511 | 2025-09-15 04:53:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56a8a4e8-99c8-3d9e-9551-2b435f4b55f4 | -22.98928 | -49.94027 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 513df35d-fa67-3d54-b931-23bfbcbbc29e | -23.19896 | -49.63484 | 2025-09-15 04:53:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a004516-d9a3-3509-a6ec-9b3123dc9325 | -20.90565 | -55.16986 | 2025-09-15 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 720f0b16-beb6-341b-a580-662c46bfdd89 | -23.45876 | -50.80122 | 2025-09-15 04:53:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c664f076-746d-3b3d-ad61-13186ff1c4ea | -22.0429 | -56.07903 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a1130d4-612c-303c-90c4-5b0f5772b503 | -18.95634 | -48.21279 | 2025-09-15 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 505698c1-b59b-37f8-ade3-a3d79fc90261 | -23.15258 | -48.96593 | 2025-09-15 04:53:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d58f4a4-5e24-3877-949e-5d6b8998669e | -23.14534 | -49.635 | 2025-09-15 04:53:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba48054b-a491-3203-bdea-09bcb851ab50 | -18.89736 | -50.15897 | 2025-09-15 04:53:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d15314ff-d66f-39d5-bbbb-915007ec1b60 | -22.17575 | -49.61457 | 2025-09-15 04:53:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da43147e-4b03-3032-969c-cfa4e50a0334 | -23.46718 | -47.28753 | 2025-09-15 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 98fafe38-0bed-3d6e-9fbe-6bae349df62c | -18.46612 | -49.57307 | 2025-09-15 04:53:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8049b884-ed9f-33d9-9239-328f8193d0a0 | -20.86256 | -46.21509 | 2025-09-15 04:53:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9480905e-0762-3433-b947-753e4b86ce10 | -18.58286 | -48.15231 | 2025-09-15 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a48da42-2640-3c98-a972-59d1575bb6e8 | -18.89798 | -50.15437 | 2025-09-15 04:53:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dce033f-fadb-37a5-b46f-447c3719cd48 | -20.51739 | -55.64012 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cb3310f-bc1f-32cb-8918-665baf7fac34 | -20.82558 | -56.86384 | 2025-09-15 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a986aee-8ee5-33c2-b63a-95de2bc3843a | -23.60177 | -47.3865 | 2025-09-15 04:53:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef550fa1-c8d2-35f4-bbb8-a7317caeeb98 | -20.52751 | -46.86389 | 2025-09-15 04:53:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b85d6d4c-ea31-33d9-9f80-831e894ba938 | -22.29719 | -47.94884 | 2025-09-15 04:53:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 244554fb-bb1d-31a7-bb55-551a83f468f2 | -20.32818 | -58.08745 | 2025-09-15 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6f763708-6695-3a12-bd0a-33cdf6e22107 | -20.23226 | -46.17542 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fcc9cca3-af24-39ba-ad9e-95be6cbe2ef5 | -20.90899 | -55.17048 | 2025-09-15 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d634656-7b8a-3a89-b4c3-f663f5171855 | -20.85998 | -46.21542 | 2025-09-15 04:53:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7cea628-932a-35d1-b111-1a19760a144d | -22.27149 | -56.04967 | 2025-09-15 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36af7d4a-25ce-3265-b533-57c318a6a675 | -22.20143 | -48.35379 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac88fba-1783-3cd7-8aaa-b7f45a6bfc98 | -21.7599 | -45.52653 | 2025-09-15 04:53:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 12663b3c-e702-3707-8cff-0115714e7f98 | -21.11964 | -45.95164 | 2025-09-15 04:53:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 67e17387-a9de-363f-9ac2-9835269e4640 | -22.27213 | -56.04579 | 2025-09-15 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a6ab975-ffe2-3a5e-902d-d0685214c805 | -18.59497 | -47.20974 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d69346aa-7e8a-38cf-926c-745787e653c6 | -18.97871 | -48.58455 | 2025-09-15 04:53:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 70c37607-1699-3bc4-a271-d3956a2c8ffa | -21.26329 | -45.63213 | 2025-09-15 04:53:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 64a1c29d-8f47-35fc-8c79-483a3506f5bb | -23.24499 | -47.11032 | 2025-09-15 04:53:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 07729601-785d-33d5-8987-8d486d272124 | -23.47268 | -47.36843 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| cae221cd-17a3-321a-910c-9211580dae92 | -22.66705 | -53.11755 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7be0dfea-ad06-315b-b891-c75912a067e8 | -21.37138 | -49.75043 | 2025-09-15 04:53:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b4fb1281-1dbd-3b14-86fe-f66da5854350 | -21.92376 | -46.5603 | 2025-09-15 04:53:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e2876d81-006e-3096-b49a-08381a90fdd5 | -23.4719 | -47.28816 | 2025-09-15 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 94edb75f-1c54-37a5-84fb-ba3709da193e | -23.47737 | -47.3691 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ae28ca13-6efa-3150-b9ac-86b9b93091cc | -23.47134 | -47.2933 | 2025-09-15 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90196533-77ed-3ec9-ab83-f63c572238b6 | -20.23716 | -46.17574 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9f65129-d95c-390d-a55f-8c9dc7879f9e | -20.88771 | -55.17426 | 2025-09-15 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e25406f3-e8fe-3dc5-aa38-c93c69a9610a | -18.61729 | -50.39628 | 2025-09-15 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 57b250f9-2894-3bc3-bae3-681b1225f0bf | -18.59553 | -47.20527 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9658daf4-36c2-3109-bbd7-15faecd6cc70 | -22.17175 | -49.61392 | 2025-09-15 04:53:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8832464c-09c5-3fab-9ddf-2541aae30be5 | -18.37143 | -49.27294 | 2025-09-15 04:53:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e74f60-439f-3edc-aba3-7a778d1a5e7d | -23.48263 | -47.36459 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bc0b6cad-ef2e-3495-8a79-ce6f35d2315b | -18.13912 | -49.19314 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0a6e0bbb-0fc3-3055-b9c1-e836ab8a0407 | -21.75957 | -45.52975 | 2025-09-15 04:53:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 34f249c3-97c9-3166-90c3-9482d605abc6 | -18.97825 | -48.58828 | 2025-09-15 04:53:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 951e7977-fc2f-3544-9ceb-e410619ba92c | -21.77229 | -54.59628 | 2025-09-15 04:53:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e81ec610-89d2-38ed-9303-59ce704d7bbf | -22.0524 | -56.08485 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b48a80a2-d79d-331b-b4bf-bbfcc30c9bbd | -20.04611 | -46.16123 | 2025-09-15 04:53:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76795dbb-67d7-3207-a5c6-df95d110b796 | -18.62929 | -47.32588 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ec9bc01f-5a14-3759-99be-f1573f46f3fb | -21.11958 | -45.95116 | 2025-09-15 04:53:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7032adc4-325f-303c-aacb-2ab00a1cbb16 | -18.97993 | -48.5859 | 2025-09-15 04:53:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9bbdf001-6e71-3c46-ac49-95f61a1f5f4b | -23.14084 | -49.63812 | 2025-09-15 04:53:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0fa01187-c3f6-3e41-abe7-f212909996d6 | -18.48007 | -46.94387 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04859eb0-a751-3d7d-bedd-d1288db199c5 | -20.23656 | -46.18123 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6e81733-9580-309d-8b9e-04c667c24add | -18.47101 | -46.94289 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e65511c-1555-38fe-80b1-1af5f9c44455 | -26.08079 | -52.17534 | 2025-09-15 04:55:00 | NPP-375D | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0d22d35-6cd6-3c5d-8e1a-526e3dc6794e | -3.55594 | -53.52843 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d5d102c-8b16-3ae5-be0d-95ee58b3eb51 | 4.3062 | -60.97302 | 2025-09-15 05:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ca7229-7244-3a3c-a44a-392c9e923796 | -3.0739 | -48.82115 | 2025-09-15 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74bde1d3-34ed-3895-b2ab-34b6ab7780f8 | -4.17543 | -48.56824 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32d57242-ab9e-322e-bd46-f7a12162db87 | -2.29535 | -48.57422 | 2025-09-15 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70ac6ae6-d9f3-3056-9198-0fa0f1d09d82 | -5.47059 | -44.68874 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e77fc34-18a5-3ddd-954a-38ff899bbe83 | -2.26141 | -47.88371 | 2025-09-15 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5fc7385-9f28-3345-b06f-f3a432bfbb8e | -5.47188 | -44.69252 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3057690a-5f6e-3c75-b39a-c908e3a73549 | -2.12455 | -56.86489 | 2025-09-15 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d686a8-b130-3c32-87f1-cac7c74c020e | -3.38624 | -50.15062 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 851d6396-366d-3358-9ce5-cc28c680edc1 | -4.17498 | -48.5712 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c7a603b-f9ea-3cfe-954e-c5ac686f3d5c | -3.65229 | -54.05733 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 40e60aa6-c51a-3f90-b6cd-e83c9ebb2f6a | -4.17912 | -48.57792 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aae127fc-73aa-30d0-9bec-2c9ec92840d9 | -3.96514 | -52.1962 | 2025-09-15 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b6385b-173b-3b50-8c20-6cae08c39f97 | -4.11087 | -51.09013 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bca4fa2-710c-3b9c-8f0d-053f816a0d1e | -3.21951 | -47.12871 | 2025-09-15 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6371e3f8-b3a2-3da8-b2d9-0ff1c5c35d80 | -3.59401 | -47.5158 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce24c022-0483-3a74-8e78-ed5ed7cc4a11 | -1.89379 | -54.61644 | 2025-09-15 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068208ab-d1c3-392a-8665-1e694c69b422 | -1.89436 | -54.6128 | 2025-09-15 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7e63402-e2d8-3fa9-947d-e5d0abdcbcaf | -4.1747 | -48.56609 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d8d786b-5bbe-316b-81e4-de0fca859e66 | -3.73673 | -55.94434 | 2025-09-15 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3da54f97-505e-3f81-b90d-cc02b25c3a23 | 4.30557 | -60.96886 | 2025-09-15 05:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad2decf-2ae4-3e68-a5a7-04357b0d5867 | -4.1895 | -50.42577 | 2025-09-15 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7836746-af4b-3f33-ac6f-16d5972b9ff7 | -4.18045 | -48.56913 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c0e1535-da22-3d29-bb63-a3a0d093cf23 | -3.64814 | -54.06075 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d3a4a39-7765-336a-b93f-65d1b8604ccf | -5.47641 | -44.69558 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fab41d4-eb92-3f9d-97af-d4b20314cbf6 | -4.17931 | -48.56994 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b9a0bb-a270-3ddf-b752-f56417d44f58 | -3.59682 | -47.51717 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3694e9c0-f77e-3533-8d7f-adaae4030e76 | -3.85644 | -51.33948 | 2025-09-15 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1305c7-40ae-3940-aa5f-6ebe8710bb24 | -3.52911 | -52.86257 | 2025-09-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe5c30d-ff73-3168-b09a-08347585fb1a | -1.23481 | -54.10254 | 2025-09-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46075563-13e4-3149-a63f-6694cc8b208f | -3.96465 | -52.19863 | 2025-09-15 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32d64d81-eceb-3893-ad35-7506e93cddd4 | -4.17428 | -48.56905 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
