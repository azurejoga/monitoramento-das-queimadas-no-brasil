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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa40a26-4496-3e6a-82b4-5cc484ecc0b4 | -18.1121 | -49.121 | 2024-10-01 11:56:47 | GOES-16 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| eabb69b6-242e-3429-a024-c95a06cda932 | -18.1127 | -49.0983 | 2024-10-01 11:56:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 180b5b3d-fc11-3216-b728-6f49e5b1b573 | -18.9096 | -49.1902 | 2024-10-01 11:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 174.3 |
| e0faed8e-46eb-38d5-9b61-e86f2a3e51e3 | -18.9091 | -49.2129 | 2024-10-01 11:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 1290d7e3-7487-32c2-bd14-5b32fa9b9f1c | -18.6977 | -57.3123 | 2024-10-01 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 58a2394f-2292-39ca-a323-f65c03ccb801 | -18.6973 | -57.333 | 2024-10-01 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 56c02fef-a5fa-363d-b040-54c60dd8b541 | -21.3834 | -48.4915 | 2024-10-01 11:57:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 306a2367-78fd-35ec-bb26-008efdb1a759 | -21.3841 | -48.4681 | 2024-10-01 11:57:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 0473a639-7eba-32cd-a87d-4ce45c079648 | -21.6078 | -47.854 | 2024-10-01 11:57:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 290.6 |
| 88e8cf5b-fb8a-3c81-bfb9-dc6c2f275320 | -21.5677 | -47.8169 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5e8ac18a-0b20-3da2-98f8-824606f68acf | -21.5885 | -47.8118 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 889.2 |
| b6953caf-f18d-3a0d-b566-76571a06b915 | -21.5864 | -47.8827 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 333.4 |
| f0a1208c-72e4-3c50-9a32-884b99a0bfb1 | -21.6085 | -47.8304 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 317.5 |
| 8ae3564d-06f5-3197-b3d3-a26cb6f7bccc | -21.5892 | -47.7882 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 361.1 |
| c3952461-fcc3-3fe8-acf0-ea66dfb5a11e | -21.5878 | -47.8355 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 264.8 |
| 5905437a-5098-3069-a22e-1756b83cc75d | -21.5871 | -47.8591 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 322.5 |
| 5272d32f-9365-3b03-b1b8-9dc46d852c0e | -21.6099 | -47.7831 | 2024-10-01 11:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 299.4 |
| 4ac834f9-da0e-3ee0-8bab-82aa10448502 | -22.3713 | -49.3011 | 2024-10-01 11:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.3 |
| 800410ee-a003-3584-a62f-ea8c3b65058a | -22.3707 | -49.3244 | 2024-10-01 11:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 161.0 |
| 4b746cab-3992-3734-99c8-8d1d12c5b680 | -10.996 | -46.5418 | 2024-10-01 12:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 93192925-bf65-372a-8629-ffa1d733ae7d | -11.258 | -45.6682 | 2024-10-01 12:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| b3c2e046-556f-301e-b824-e81310777e97 | -12.9433 | -51.2192 | 2024-10-01 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0402dce6-1017-3161-ac63-1c7004856336 | -12.9201 | -51.4776 | 2024-10-01 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| eb67fd0b-97a0-366f-b60e-461cf53b358d | -12.9205 | -51.4563 | 2024-10-01 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 221.5 |
| e5e86b82-41d3-36ff-85b0-f4a1fb898610 | -12.9396 | -51.454 | 2024-10-01 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 899b2cc3-ac92-3181-bd78-9c5dc9b64289 | -12.9625 | -51.2169 | 2024-10-01 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 23e85737-a90a-3063-8415-27ac4710c107 | -16.4935 | -57.3531 | 2024-10-01 12:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 6dcd511d-f0c0-3674-98b1-bb21e7590703 | -16.4536 | -57.4188 | 2024-10-01 12:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 53f12ac9-7763-3f5a-9a20-2cce9cf350ad | -16.474 | -57.3553 | 2024-10-01 12:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| f0318103-c992-3aab-aabb-a4620264f7bd | -16.6515 | -57.233 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 21b68549-c024-37d4-88e4-97b61804c1f2 | -16.6117 | -57.2784 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 89b3f70c-fa09-3569-a04b-72a10bf2541a | -16.6316 | -57.2557 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 8dbec826-6cff-3b57-affc-93ea9b0b26c8 | -16.7724 | -55.798 | 2024-10-01 12:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| b9931dae-23cc-38d4-9503-7239a69b5682 | -16.7461 | -57.4265 | 2024-10-01 12:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| f2a194cb-75d6-3d42-9178-0ea1f7cdcec5 | -16.6319 | -57.2352 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 2f3e67a5-59fd-3c8e-99a3-ecf2ea36da46 | -16.612 | -57.2579 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 9f78b796-fc77-3e6f-a02d-8f203948e7b1 | -16.6512 | -57.2535 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| ce8627c9-c79e-34cf-8e9f-0f7f8f86d19f | -16.7471 | -57.3651 | 2024-10-01 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| bd2f4529-2a1e-3e16-a511-328f69b1e4cb | -16.8787 | -57.6971 | 2024-10-01 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 42dbeb7a-83df-31e4-82ba-ef64e19444f4 | -16.8488 | -55.9128 | 2024-10-01 12:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 83ebfd79-a8c8-31da-bf47-ef478e54cd79 | -16.8292 | -55.9152 | 2024-10-01 12:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 3599bff0-b9e8-3475-97d9-06b281df035d | -16.8484 | -55.9335 | 2024-10-01 12:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 1e4554aa-d72d-3ecd-8cae-74a289d4ca25 | -16.8481 | -55.9543 | 2024-10-01 12:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 4276d3f5-5a61-3a44-b197-207a094da40b | -17.1377 | -56.2076 | 2024-10-01 12:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| d1e75c1b-afd2-37a2-b486-eab09b6ea60f | -17.1767 | -56.2234 | 2024-10-01 12:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| e3941373-370e-3fc2-9038-b9bc51007987 | -17.1577 | -56.1844 | 2024-10-01 12:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| c0a4623d-e47b-37b5-b372-5bdc8276b939 | -17.1574 | -56.2052 | 2024-10-01 12:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 512a67f4-3f8c-3176-a70b-e93205c902ce | -17.1581 | -56.1637 | 2024-10-01 12:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 57212853-ea9e-3aac-be10-58426e71cee3 | -17.705 | -53.2046 | 2024-10-01 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 696e1d01-8bcd-321b-a98e-3d5bb8b5e461 | -18.1121 | -49.121 | 2024-10-01 12:06:47 | GOES-16 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 8c042a3f-e458-3ee2-90f6-631c1a26b96d | -18.1127 | -49.0983 | 2024-10-01 12:06:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 70b2fdbc-cd0d-3c79-aa71-fede13ebb67b | -18.9096 | -49.1902 | 2024-10-01 12:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 215.0 |
| 67409cc6-3a19-3763-8cce-5592e47a9e7e | -18.9091 | -49.2129 | 2024-10-01 12:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.2 |
| 4a5341c1-36a2-3665-b6ba-140620a986d4 | -18.7176 | -57.3097 | 2024-10-01 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 30d8541b-066c-3417-a633-91641091fe15 | -18.6977 | -57.3123 | 2024-10-01 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 69799c19-1754-3875-9172-2fd653217933 | -18.6973 | -57.333 | 2024-10-01 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 453bd4a8-5a5f-39c2-99a3-33c326cbc8fd | -21.3841 | -48.4681 | 2024-10-01 12:07:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 00608d67-0fd5-3517-b7e8-2474fb7eccbc | -21.3834 | -48.4915 | 2024-10-01 12:07:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 124.7 |
| bb5d05d2-798c-3a0b-b9c6-b375a093d270 | -21.5885 | -47.8118 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 647.8 |
| e2e908b2-d259-307c-b81c-77a1802b476b | -21.5864 | -47.8827 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 305.0 |
| b63cc222-a3b1-3f1c-ac87-64d40769d2fa | -21.6085 | -47.8304 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 437.2 |
| 072c93da-c761-3d16-8575-0f8681f99921 | -21.6099 | -47.7831 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 183.2 |
| e490f911-bea5-344a-8416-bf6e9474bbfb | -21.5871 | -47.8591 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 275.6 |
| b4d22dc2-8756-3dfd-9e17-4761800dd697 | -21.5878 | -47.8355 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 296.7 |
| 5c76b087-3074-3ffd-bd59-a299dbab3632 | -21.5892 | -47.7882 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 35bcbb50-d472-3313-ae4a-09b9a21ed9df | -21.6078 | -47.854 | 2024-10-01 12:07:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 267.8 |
| 9f4d033c-974a-3415-b6cc-7148bcadbf92 | -21.5677 | -47.8169 | 2024-10-01 12:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b3b034dd-8c4f-39b4-a014-6fa8e01fc661 | -22.3713 | -49.3011 | 2024-10-01 12:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.0 |
| a60d0ab1-e40f-3ee6-b0a6-8b29417948f8 | -22.3707 | -49.3244 | 2024-10-01 12:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 195.7 |
| 68fca120-77ed-33b6-87c5-404a4692c013 | -10.052 | -50.2833 | 2024-10-01 12:16:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 037a1d61-0379-3089-9c2a-8634270c5545 | -10.9964 | -46.5192 | 2024-10-01 12:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 9404f35a-0027-305d-911a-12f941c47358 | -10.996 | -46.5418 | 2024-10-01 12:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 36647f66-a1a7-3ba8-ad07-9dbc02b5cece | -11.258 | -45.6682 | 2024-10-01 12:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 471e0f75-6aca-3fee-9e66-6273f0b85bcd | -11.2584 | -45.6453 | 2024-10-01 12:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 29467e01-b185-3c2b-ad67-e1cf67a2dbb8 | -12.1406 | -50.0524 | 2024-10-01 12:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 28386a64-a9d0-3c50-a30e-b4ebb009f80b | -12.9205 | -51.4563 | 2024-10-01 12:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bda88aed-3e9b-37b9-b00d-c866aacc659e | -13.2116 | -51.2073 | 2024-10-01 12:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| e7423790-5b51-37b5-9f93-85eb3f500d4a | -16.4536 | -57.4188 | 2024-10-01 12:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 1fe53a3f-8bbf-375c-9896-074ea954ea32 | -16.4935 | -57.3531 | 2024-10-01 12:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| f21c2fde-ff95-34d8-95e3-41d091e47f25 | -16.474 | -57.3553 | 2024-10-01 12:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| c33e58b1-61ac-366f-bffe-b2d51b8e19b9 | -16.7724 | -55.798 | 2024-10-01 12:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| e0431c5c-ebef-3e9b-aac4-fe998cc8aa8f | -16.7471 | -57.3651 | 2024-10-01 12:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 45a3d1b9-c9d0-39d1-85a0-86206137f56d | -16.7461 | -57.4265 | 2024-10-01 12:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 0927c1ca-c574-3c7e-84a7-0d42b9a31e98 | -16.8787 | -57.6971 | 2024-10-01 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 6d479186-0bdf-3cbc-87d8-43e46592c4a1 | -17.0895 | -56.7503 | 2024-10-01 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 84aa1027-c01c-370e-a477-28a8a1d76a37 | -17.0898 | -56.7297 | 2024-10-01 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 88a7559e-cfda-3e6e-961f-0c91956e5a4b | -17.0699 | -56.7527 | 2024-10-01 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 06ba938d-b892-3909-bd4a-46ad14d1a277 | -17.705 | -53.2046 | 2024-10-01 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f6750948-6add-3027-a7fb-e728d723c626 | -17.7248 | -53.2016 | 2024-10-01 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 23eb1102-10e3-3b53-9c3a-eb0908cb85fd | -18.1121 | -49.121 | 2024-10-01 12:16:47 | GOES-16 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 934ec539-64df-386d-8581-81e059acbc66 | -18.1127 | -49.0983 | 2024-10-01 12:16:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 139.1 |
| c23302c6-e680-3537-a396-28ccbcec2138 | -18.6973 | -57.333 | 2024-10-01 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| d885c488-7eec-3dc3-a4b0-64e674b0497c | -18.9091 | -49.2129 | 2024-10-01 12:16:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.1 |
| e31eed67-ae8d-3b87-a399-4f830edefcc4 | -18.9096 | -49.1902 | 2024-10-01 12:16:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 210.0 |
| f5f137b2-a50e-3794-a04a-332baa8ffbfa | -18.6977 | -57.3123 | 2024-10-01 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 773e8d4e-f7e6-3ffa-ad07-55d8f954cc0c | -21.3841 | -48.4681 | 2024-10-01 12:17:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 93efab6d-bdd1-3030-8612-0c8f682e864c | -21.3834 | -48.4915 | 2024-10-01 12:17:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 744213d3-927c-38a3-be33-6071e8e47c70 | -21.5864 | -47.8827 | 2024-10-01 12:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 294.7 |
| 0721ee88-4824-3965-bd6b-e3d6749432dc | -22.3707 | -49.3244 | 2024-10-01 12:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 237.4 |
| 1e8e46f3-5eed-33fe-9d6f-d7545ea8cac6 | -22.3713 | -49.3011 | 2024-10-01 12:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 202.0 |


[Clique aqui para ver as próximas entradas](README163.md)
