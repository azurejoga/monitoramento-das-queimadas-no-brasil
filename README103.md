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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6831798d-b051-37db-b12a-7161fd22cbe5 | -16.04563 | -50.99346 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c206def1-4c77-3ad6-b92a-f7937bd8f3e2 | -21.49735 | -46.02535 | 2025-10-07 04:59:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dd892ca4-1658-360a-a4c0-e91bbb2fceba | -17.24852 | -46.93059 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3aa5cea-0f2a-30fc-abc6-96355ec61703 | -15.03757 | -56.03379 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc43ba8b-50fa-373c-bbb7-1ddea4fa2c22 | -21.61192 | -43.99776 | 2025-10-07 04:59:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d745d1af-b863-3d45-823e-7002018cd706 | -16.11562 | -48.9376 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ea55962-69ad-35ab-b2b3-2a1afe84d13d | -16.03316 | -51.02535 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc988966-e678-3205-a9df-9dad55c3b1c5 | -21.90646 | -44.89277 | 2025-10-07 04:59:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 258a660e-5162-3634-8ffe-10b363621be5 | -15.01046 | -56.05484 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57459001-95ec-30f5-a038-be6ec778683a | -19.63653 | -55.73922 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e027ed77-e6d3-306e-b3ab-4a2e0fb712d2 | -20.05538 | -49.54398 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 64288a58-5dcd-3397-ba79-d86e6bd3f35c | -17.56149 | -50.44757 | 2025-10-07 04:59:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb0ed981-b962-320b-9322-49398ff32168 | -15.55894 | -52.44245 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 610569ca-682a-3155-92ff-212792f1033c | -16.29875 | -50.99025 | 2025-10-07 04:59:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3dd12eea-0b2a-3575-be55-25e1e863e188 | -15.99975 | -59.52802 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fce90d1d-7d1b-3e81-ad39-bc5ce0824493 | -22.01442 | -49.72255 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3f50fc96-e19d-3b41-ac0d-8709383afb2f | -21.51503 | -45.60283 | 2025-10-07 04:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7fb44240-1c36-3db5-9bea-d18d898fec70 | -15.22528 | -56.77604 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30534fa0-3c69-3af9-9e3e-5b859e33d320 | -18.6041 | -46.8016 | 2025-10-07 04:59:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7814f956-49f1-36e3-99ae-505986762c1e | -15.60735 | -52.57225 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a23898dc-8c6e-3405-aead-ecb0673c4a40 | -17.9803 | -44.98838 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dd4239f-ebd5-37b9-9971-9c1a8b675bf7 | -20.07837 | -49.59501 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 87c8dc34-ba7a-3dc5-b56a-432327702c5f | -15.5804 | -52.57686 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09b483f5-4112-32fe-bb93-f9da98eb9cb1 | -22.09083 | -44.79324 | 2025-10-07 04:59:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0bd2d4d7-b4bd-3a9d-ba26-a7ee6f3fa74e | -15.22354 | -56.78684 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a6501d-2a7c-300e-9d37-9075f0219752 | -16.00987 | -50.8277 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 407d4d31-598d-3e8f-8391-6891ed135496 | -15.68754 | -53.62785 | 2025-10-07 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| babae355-7b6c-38bd-97f6-0c72c6728ddc | -16.31572 | -47.91439 | 2025-10-07 04:59:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6fb7ab92-9f6e-3a8b-a9b1-5062f5b29984 | -19.04086 | -48.13591 | 2025-10-07 04:59:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db8a387-4a7f-3c5d-b256-8b1b3ba99027 | -16.00776 | -50.9662 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48c6e1b7-a990-32d2-89e5-640f053f8618 | -15.99668 | -50.95622 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c03ca4db-5603-3020-8f6e-f67a6a1e8452 | -15.19335 | -56.82595 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d17f3797-cb7e-3563-9bb8-fbd6c49eb5af | -18.11453 | -53.3494 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4f2659c2-8eec-3023-8c79-4ce17cda9f53 | -21.74056 | -44.42214 | 2025-10-07 04:59:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 449b3422-6b23-3c71-b1a3-1998130d4981 | -15.19781 | -56.81947 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23f3b1e1-e5df-3ede-8192-3fb8eeb27233 | -17.25322 | -46.93751 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0057e8e4-9ece-3434-8af0-6f9e45504159 | -22.00425 | -49.72681 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1c41026e-5e45-346f-b2b8-b8303d52765b | -15.03538 | -56.02612 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ada3f791-0816-353d-9345-1ace634a57d6 | -21.61827 | -44.00387 | 2025-10-07 04:59:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5e743f37-d25b-3e81-b9fc-896f705818e5 | -15.29846 | -56.9328 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24329e7c-3177-324e-b752-a73a55bd5d6e | -15.18279 | -56.82791 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ecdca50-c741-3f13-876c-cc12a3b3bc8a | -19.95555 | -44.63649 | 2025-10-07 04:59:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59968e47-aa5a-39fa-9b49-0088810f90ef | -15.59449 | -52.55664 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52ffbe09-92ac-3d66-a801-123f19353142 | -17.17314 | -43.45443 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fe48ff9-b313-353b-b1fe-95579bf9ae12 | -21.74099 | -44.41659 | 2025-10-07 04:59:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 062fa7ab-8a81-3dcc-bc8d-21174ec71859 | -16.01906 | -51.03843 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc3edb56-8a21-3a3e-a12e-24e9f27b5b2b | -17.56149 | -46.07663 | 2025-10-07 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a643ea-8a49-3a68-a0ff-9454a71897fc | -18.92481 | -49.48541 | 2025-10-07 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e0327a2-4c14-3d79-a6e8-af002de1e994 | -17.08857 | -43.38299 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8663a869-f43b-363d-a9e8-974eb8dd44de | -22.01259 | -49.73932 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 850095db-d779-38e5-8eb3-b7be17643c45 | -15.99552 | -50.84114 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82c92880-ec65-3b7b-afa9-8079ca180bd6 | -22.0132 | -49.73371 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 25087df3-53f4-3bc5-b717-fc7b563c4730 | -16.04655 | -50.95499 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78f66de6-0b64-34d3-acab-5ad77375984c | -15.03151 | -56.02913 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54e85740-e186-3a01-826f-62b48d7feb76 | -17.16945 | -43.45457 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 261cbb37-9a34-3e37-90a1-58adb70fbd03 | -16.01813 | -51.04546 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 699b2b5f-3942-3721-8e86-324acbf45699 | -20.2119 | -43.92389 | 2025-10-07 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ac1bec6e-7083-354c-b22c-94cc58ad7d88 | -16.0186 | -51.04193 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f139438f-75e2-3a7b-815e-d090ba83d748 | -15.58101 | -52.57246 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68da5df6-f325-3d75-a8ea-63caaa3dda89 | -15.24534 | -56.75737 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aecc3401-8dd0-375c-97bc-494289fc8bf6 | -16.3952 | -53.32528 | 2025-10-07 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee5bf935-7016-366a-bed4-f41a8261338e | -15.6 | -52.57099 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3c654c37-a971-3f61-a8cf-df8e1c8ccd83 | -18.78212 | -44.62175 | 2025-10-07 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03798919-03b5-39b5-adc6-4f215d36eed4 | -17.09153 | -43.38508 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e3b5604-2652-3adc-9714-1e47d6d53a01 | -16.01409 | -51.04482 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 246e4960-2468-3d06-9ed4-a2cb3b1a3fa7 | -22.09048 | -44.7979 | 2025-10-07 04:59:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 808cecb2-d5bc-3bd3-99b7-447b47b682f7 | -16.0208 | -51.05661 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8924de36-0e7b-3202-a5f9-36c3dd820f99 | -20.11248 | -44.41282 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 87a22d57-d45c-3c51-b498-712365296b30 | -21.48166 | -46.72095 | 2025-10-07 04:59:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ee01081c-ed87-331f-be92-d0b5f8d896f5 | -15.61533 | -52.56894 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0520d346-4b29-3c14-ba68-4a7bceb4ef43 | -21.1921 | -45.61704 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b08f6a3-1c2f-3798-8230-a5d99e4dee14 | -19.63756 | -55.77817 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2794d6a0-7b15-3629-bd60-7447c1a661f2 | -19.80791 | -46.05585 | 2025-10-07 04:59:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b393cc7e-f3be-33db-a3d9-9ece7ef93c49 | -15.20562 | -56.8134 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e2b5a64-a987-3548-9a04-866b0ef1466d | -21.49175 | -46.01987 | 2025-10-07 04:59:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d5a78e36-255e-3f73-afb7-5bd8ef2fe2d3 | -20.32062 | -45.11813 | 2025-10-07 04:59:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c145b130-baba-3e8c-b4a6-3ba7385349b4 | -17.09099 | -43.39104 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3553c5a6-f79e-3ca9-b58d-a5a97555b5c2 | -16.3396 | -47.05651 | 2025-10-07 04:59:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1419ea47-c156-36ba-89c6-7d005543cb93 | -15.0059 | -56.10523 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72d855b9-d9f5-3c5c-a26b-1827e1464bbf | -21.76919 | -47.78171 | 2025-10-07 04:59:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54173c08-94e2-3b7a-94dc-037f56b1d59a | -16.00779 | -50.96606 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7269240c-a88c-3ecd-a4ea-9453338c6f8f | -22.55076 | -44.44989 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c2ad1488-f94d-39d1-832c-b57be4a5c97c | -15.99254 | -59.54141 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25025820-37ef-3a6f-879b-a44a00ad5e68 | -15.96639 | -50.84032 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8f69a9f-c63a-301e-a2cc-201f1e21fa88 | -16.0636 | -50.92022 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25f8482c-58fc-3110-bb74-0ab725dfba4d | -21.6735 | -51.15285 | 2025-10-07 04:59:00 | NOAA-20 | ADAMANTINA | SÃO PAULO | Brasil | 3500105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f47eb1a5-2f4e-3122-a944-5a40777057eb | -15.60921 | -52.55894 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d705752-d3b6-32c7-ab79-4cfa2c55c074 | -22.02397 | -49.72405 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9340e928-acfe-37bd-a384-7417d1e697b7 | -22.01919 | -49.72333 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| cc726183-26e7-308a-a7d3-be2a29336446 | -22.00965 | -49.72184 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7956013b-ebb0-3b91-ae16-b8a2e6e40cf6 | -20.58715 | -46.30861 | 2025-10-07 04:59:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 057ac246-3ac9-3351-b560-97edbadfe30b | -16.00069 | -50.95721 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6662c61a-03ce-3d23-9058-38e25dd13782 | -19.04597 | -48.13665 | 2025-10-07 04:59:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 409f213c-dda8-32df-97cc-d4c6b18cf5e9 | -20.09733 | -44.20358 | 2025-10-07 04:59:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c3cda2f7-e77c-3c3f-b52f-e6279c18d926 | -16.3958 | -53.32106 | 2025-10-07 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff02123f-0f13-37f6-a2dd-375de42ba8e4 | -16.34705 | -48.13221 | 2025-10-07 04:59:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f0a56bd-8ce4-37a4-b101-a6749a96e139 | -15.57794 | -52.56745 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1086c854-7eea-3149-9fcb-70d34412bfc2 | -16.02909 | -51.02486 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce8cd5fb-a67f-3442-9293-7a14ed0922e6 | -18.11756 | -53.35433 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 76e23b91-2312-3ebd-a393-aae2acd8b800 | -22.79341 | -54.66904 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README104.md)
