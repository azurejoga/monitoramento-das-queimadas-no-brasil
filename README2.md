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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78602d2a-1bf3-3e1a-afbf-25b54cdf49a3 | -22.3967 | -48.7314 | 2024-10-31 00:26:10 | METOP-B | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aee483fc-6b1a-3c9d-832a-014e64f2b69e | -22.398701 | -48.742199 | 2024-10-31 00:26:10 | METOP-B | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63fbbb18-23b2-3ddd-a9db-59592fdc2adc | -22.343 | -48.225399 | 2024-10-31 00:26:10 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c540e9bd-e894-3442-9b6e-9035e67bb84f | -12.4438 | -43.7005 | 2024-10-31 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b2311953-7f3e-3300-a171-c3312b3b776b | -12.424 | -43.7274 | 2024-10-31 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 2d7a9fa9-d043-3cca-a701-16e7d9d5a32a | -12.4428 | -43.7479 | 2024-10-31 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d72de0b3-2095-3f96-a1c5-5186e56b54fc | -12.4433 | -43.7242 | 2024-10-31 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| e3c14e2e-2a8f-3bfe-a3b6-98a0a2b69d96 | -12.305 | -63.5805 | 2024-10-31 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 026a935b-88e5-3497-a3f4-8019f2a49dda | -21.9795 | -49.055901 | 2024-10-31 00:26:18 | METOP-B | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62e6267b-9ab4-3b7e-87ff-e771f3290fac | -21.969801 | -49.057899 | 2024-10-31 00:26:18 | METOP-B | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f3b3cd4-b01d-3f59-8b12-78a6383d8b6c | -20.984301 | -47.156898 | 2024-10-31 00:26:28 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb2c87e4-4c34-3f4b-8d2b-58d079092ba9 | -19.9641 | -46.066502 | 2024-10-31 00:26:41 | METOP-B | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22e75871-5395-370a-9c44-b83bfb861904 | -19.9657 | -46.0742 | 2024-10-31 00:26:41 | METOP-B | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7b305b51-f831-3248-b064-6345dc3c64c9 | -17.7246 | -57.5574 | 2024-10-31 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 8f4e2954-fa19-3465-8f9b-344c22aa39cc | -20.355301 | -49.982498 | 2024-10-31 00:26:48 | METOP-B | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21aa906d-75d8-3af2-a41f-5cfe18ce7e87 | -20.3575 | -49.9944 | 2024-10-31 00:26:48 | METOP-B | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 068be7d2-33df-3ca0-83b3-de25f6987f96 | -20.3456 | -49.984501 | 2024-10-31 00:26:48 | METOP-B | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6077bfc8-17ca-32dd-91fd-57ff16d5e615 | -20.347799 | -49.996399 | 2024-10-31 00:26:48 | METOP-B | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0577103f-9264-3d5d-a93c-bc7bebd8e77c | -19.641199 | -56.6381 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49cc7b76-8c51-3833-8157-53bcbbae18e5 | -19.646 | -56.669701 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b5b39c11-4613-3518-bfeb-5d1f152a7ba4 | -19.6315 | -56.639702 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 861b3280-97a7-39af-bd8b-0e5472d63119 | -19.636299 | -56.671299 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b0548e8e-d80a-3650-bdb0-45ab20355c2e | -19.6411 | -56.702999 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cc371be-2697-3e7b-9bf7-de23f7e897e8 | -19.621901 | -56.641201 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 912751e9-dec8-33e5-9632-9d5823b91d02 | -19.626699 | -56.672798 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 341831a1-dfdd-3f5d-b8eb-216b5f755253 | -19.6315 | -56.704601 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cb18bf0b-27bf-3dc8-83d6-253b1108b5ec | -19.6605 | -56.634899 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6277922-2f99-3ffa-9a5e-6bc464955010 | -19.646099 | -56.605099 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1bf612b1-615f-304a-b761-4f45dd3d64e5 | -19.6509 | -56.636501 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed00fa70-52db-36ea-b3ba-07e5220316d8 | -19.655701 | -56.668098 | 2024-10-31 00:27:18 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eb51b012-618e-303d-8d42-61ce423dba74 | -19.607401 | -56.611401 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8582655c-0586-38ae-a400-9059c91c960e | -19.6122 | -56.642799 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 17fc17bd-9371-3dfa-92b0-326419936373 | -19.617001 | -56.6744 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| edecfe69-178c-3c5b-bb5b-5f63f900eeb4 | -19.621901 | -56.7061 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 48f81b9d-fb9b-3d6b-b1ca-290bc0197d55 | -19.597799 | -56.6129 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 29bcdcbc-af03-3c2e-89eb-0fe4660c82eb | -19.6026 | -56.644299 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 17b2ad68-f44e-3aa5-9e26-cb2fb5527073 | -19.607401 | -56.6759 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfae72d7-4f23-320b-893f-0a42c8f68105 | -19.612301 | -56.707699 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9e84ff2-9921-3b60-84fa-61cb0efba014 | -19.5882 | -56.614498 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 64cfe5a5-c6fe-313b-ba6f-27317f5dcdcc | -19.593 | -56.645901 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac9d5d42-87d9-31d0-94cd-678ea2968cb5 | -19.597799 | -56.677502 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5abc8b5-a3ae-33c3-ac7b-c232224b7d4c | -19.5833 | -56.647598 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 496dbbd2-6c24-39aa-99f5-97dd7466944d | -19.563999 | -56.6507 | 2024-10-31 00:27:19 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc36857c-e7ee-350a-978c-af60e78c50d6 | -19.535299 | -56.5275 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8d971f4-7ea5-3a4f-ac20-d9f6c19a05b8 | -19.549601 | -56.6208 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f1c36fd9-54fe-3025-808a-4ac8b6722de7 | -19.554399 | -56.652199 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2250b490-49c4-38b9-91fe-8a7ce9841e4f | -19.5256 | -56.529099 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 437e5c0f-8fe0-38da-a730-500f8b327372 | -19.5399 | -56.622398 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5d09edce-4d0c-3f0e-9829-54994d270541 | -19.544701 | -56.653801 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 815747da-814c-378c-b5aa-b6c32d56b55b | -19.530199 | -56.624001 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0a73ed4-c0a7-3827-9b4d-67d98054a316 | -19.535 | -56.655399 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1705e61a-d904-3344-b5ec-fb532c331c47 | -19.520599 | -56.625599 | 2024-10-31 00:27:20 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0088c13-fee2-382e-8428-c6b85b2f6f65 | -18.287001 | -55.909 | 2024-10-31 00:27:39 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 84aebd2a-1cd9-35a5-9123-b02a0ec6e527 | -18.277399 | -55.910599 | 2024-10-31 00:27:39 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2a5d9d0d-f6ea-33b5-b5f9-f8f6c735beb5 | -17.5961 | -52.369202 | 2024-10-31 00:27:40 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63d38304-5837-3ad8-9312-69b1dd4372a9 | -17.5989 | -52.384399 | 2024-10-31 00:27:40 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45c8c9ec-85db-3c9e-b8d6-e27da6464eef | -17.7558 | -57.4823 | 2024-10-31 00:27:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 062a7484-6fbd-3208-82c0-8550e908f832 | -17.746099 | -57.483898 | 2024-10-31 00:27:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f354a916-a3b7-3489-a6f5-df5bd08cef54 | -11.9066 | -40.946602 | 2024-10-31 00:28:33 | METOP-B | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c9fd3523-ec56-3ebb-9773-1165450228e8 | -12.4601 | -43.7104 | 2024-10-31 00:28:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7ab103c-3e31-368f-b810-2a3cab687ef9 | -12.4619 | -43.718201 | 2024-10-31 00:28:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0635adb-c0c1-3823-a1a1-5df59d616ee9 | -12.4637 | -43.725899 | 2024-10-31 00:28:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad24ba25-7f56-341a-b77a-87dd05464ab7 | -12.4503 | -43.7127 | 2024-10-31 00:28:35 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d7639b2-388d-35ca-a6d8-a97578279b01 | -12.4521 | -43.720501 | 2024-10-31 00:28:35 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98d33be4-8406-386b-af06-60fba35a0d37 | -12.3995 | -43.716499 | 2024-10-31 00:28:35 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 067c467e-bfcb-3d78-9747-0cf623350284 | -12.3636 | -43.6507 | 2024-10-31 00:28:36 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2ce84a7-3d08-3a27-b98c-d2d3f76b9483 | -12.3654 | -43.6586 | 2024-10-31 00:28:36 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21433ad4-82d6-3dcf-91d7-406de8cfc0f5 | -12.3672 | -43.6665 | 2024-10-31 00:28:36 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20aa891f-d19b-38f1-87dd-a51326a482b1 | -12.498 | -44.638 | 2024-10-31 00:28:37 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6613b183-0796-3139-bd39-3b2361760c07 | -10.5677 | -36.9673 | 2024-10-31 00:28:38 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dab85da2-3fb2-3a81-8971-22f87f9aa198 | -11.905 | -43.810101 | 2024-10-31 00:28:44 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27d1ae2d-be8c-3482-be87-13723eda227a | -11.9068 | -43.817902 | 2024-10-31 00:28:44 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2147a2b7-73a6-3aea-af26-31adc75e9c99 | -11.6811 | -43.9128 | 2024-10-31 00:28:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb34491-9463-3633-bcd8-43570be82ae6 | -11.6713 | -43.9151 | 2024-10-31 00:28:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bedf792b-c55c-3d7e-a8d2-5c7ee42a07a3 | -10.0948 | -42.216599 | 2024-10-31 00:29:07 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 36be7419-4cfb-3e6d-9e6c-beccad0f065a | -10.0971 | -42.226398 | 2024-10-31 00:29:07 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2813ee01-510c-3563-9ea1-2d9cc6c55cdb | -10.0328 | -44.820499 | 2024-10-31 00:29:18 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f8d8ffc-4964-329a-aab1-a2c399a8f413 | -9.7092 | -46.254299 | 2024-10-31 00:29:28 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 041f785e-06e5-3509-8097-92427c4132d5 | -9.6916 | -46.221699 | 2024-10-31 00:29:28 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdda53d-d23b-381b-847f-b8a4eb634cc3 | -9.6931 | -46.228699 | 2024-10-31 00:29:28 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcb8f31d-63cd-3e1a-80e3-2278fb2959be | -6.9952 | -35.126801 | 2024-10-31 00:29:29 | METOP-B | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0902d880-2bfc-312d-8442-1ca13a68447b | -6.9857 | -35.129299 | 2024-10-31 00:29:29 | METOP-B | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 986db663-4770-39c3-8885-92b9f8d8f355 | -8.0166 | -39.9333 | 2024-10-31 00:29:32 | METOP-B | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1a11c51d-485f-3fdb-a987-578c924bd94c | -8.0033 | -39.921001 | 2024-10-31 00:29:32 | METOP-B | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5700fc3e-14af-32a0-8eee-f75e2a625d56 | -8.0069 | -39.935699 | 2024-10-31 00:29:32 | METOP-B | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ac31d9a1-63e5-39c9-aacb-58d73cb065ad | -8.2173 | -40.929199 | 2024-10-31 00:29:32 | METOP-B | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0eb72d9-873c-3a33-a996-8431d6ab4f88 | -8.013 | -39.918598 | 2024-10-31 00:29:32 | METOP-B | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5f5f111e-7ec0-3fb5-adab-2d80c3ba7f48 | -7.6236 | -38.837002 | 2024-10-31 00:29:34 | METOP-B | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7b97e8a0-46c7-3ebd-aaec-28d00c460b69 | -7.9257 | -42.9496 | 2024-10-31 00:29:45 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48bd951e-2f0b-3586-9031-abdb22ecc402 | -7.9136 | -42.942402 | 2024-10-31 00:29:45 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a97bc2e9-2721-355e-a645-9b820acbf8ab | -7.9159 | -42.9519 | 2024-10-31 00:29:45 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3757218b-4681-35c8-a89b-1d52766533db | -8.2833 | -44.839298 | 2024-10-31 00:29:46 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06ed6f44-ea93-38bf-ba4b-eed161cdff5f | -8.2851 | -44.846901 | 2024-10-31 00:29:46 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 010cd345-95e7-3a61-8e88-8db2fa113d9a | -8.2868 | -44.8545 | 2024-10-31 00:29:46 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b94eb3c2-a5de-3bc6-9f9d-8d54c46bb6e9 | -7.0892 | -39.972 | 2024-10-31 00:29:47 | METOP-B | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 24f6fbb2-942f-3943-a7e8-a05f6ba5a859 | -6.9901 | -39.8181 | 2024-10-31 00:29:48 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9ea42a53-bfb5-3e39-a1b0-c193db44e59f | -6.9766 | -39.804901 | 2024-10-31 00:29:48 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2c5033f0-8af8-3f0e-baac-e145473c95be | -6.9804 | -39.820499 | 2024-10-31 00:29:48 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c72b7487-6270-39be-855d-740ca4cb1711 | -7.1049 | -42.617699 | 2024-10-31 00:29:57 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d98c575c-a7ca-3084-a440-22bd115ac34a | -7.9278 | -46.672798 | 2024-10-31 00:29:59 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
