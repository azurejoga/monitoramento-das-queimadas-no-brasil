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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 465acba7-c1be-31f9-9df1-75433a3771ba | -16.995199 | -56.824402 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acc5ca43-aba1-395a-ae7c-806fd13e0db2 | -17.1089 | -57.361599 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1f9e6b4-35bc-3bf0-854a-41257663134f | -17.1106 | -57.369701 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cb3ee0c-3b31-3ccd-a938-97f3820fab9b | -17.1124 | -57.3778 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18cd57f2-f9b5-3539-afe0-6724bd815300 | -17.1141 | -57.385899 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba61e29d-6a73-3984-bb65-b4b2bf5dadea | -17.115801 | -57.394001 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91cf8c25-0018-3bc4-9b00-e9f24039557f | -17.1175 | -57.4021 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a0a6e7c-f2d5-3b89-90c7-d2adc5b348c6 | -17.1192 | -57.410301 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccfe5a95-5985-3940-9c3b-9d0b40c424ce | -17.120899 | -57.4184 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d72e66a-07a6-3e55-b13c-83c8ae73e3a6 | -17.122601 | -57.426498 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f72e3e33-d412-3de6-ac22-97d07b3b1fbd | -16.939501 | -56.612099 | 2024-10-07 01:20:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 865ab259-1eaa-3a5e-ae58-06f719c996b2 | -16.968901 | -56.749599 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3a7cbac-a3bb-320b-b844-7e1c3e8a7509 | -16.9706 | -56.757301 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d635e91-cc4a-3b9c-80dc-85455b70d476 | -16.9788 | -56.795799 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d49061a-c890-3377-ad21-65fc6f1fe496 | -16.9804 | -56.803501 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54fd9ccb-3987-35e1-ad5b-326ce02c38b0 | -17.0991 | -57.3638 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a21434fa-533d-3543-95dc-2adc2a548281 | -17.1008 | -57.371899 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88bae47c-b847-3d7c-9e30-a79253117dbf | -17.1026 | -57.380001 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf223b81-7760-3e3a-be51-3657b80527f6 | -17.1043 | -57.3881 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e29f37ab-afd9-35c9-89c7-cf3a4e323052 | -17.106001 | -57.396198 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10095da6-b4e6-3e17-b5ac-36e70cbb5c3a | -17.1077 | -57.404301 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e2cfac2-57d5-3959-898d-cb5a9b9d676b | -17.1094 | -57.412498 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e026b15-fc44-38a3-80d5-7d36c77eb135 | -17.111099 | -57.420601 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 435bd390-3ff6-355b-a4e9-fc429d2b66b1 | -16.9592 | -56.751801 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b895cad4-bc86-3da4-ad95-15c0af75c33b | -16.9608 | -56.759499 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9a5a79c-48d1-3559-853d-90dfc52276a7 | -16.9625 | -56.7672 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c78d158a-36f2-367f-8c3e-1d263e021c90 | -16.9641 | -56.774899 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa88c699-e9c3-3a7f-8933-c0ff47091db3 | -16.9657 | -56.7826 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 708418c4-5ba4-31ac-8703-7cf7dc7b9b04 | -16.9674 | -56.790298 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4ffc56a-fc07-311f-a272-f0b46117bb33 | -16.969 | -56.798 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 981c6b5e-ef8d-3483-ae08-8d4a891d5eb6 | -16.970699 | -56.805698 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7998bb25-a798-348e-91f0-644918023898 | -16.9723 | -56.8134 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36dc5d59-e393-39df-8754-05aba064e855 | -17.0928 | -57.382099 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8b3ca0e-8dc5-337e-bf6e-4087ce88e7be | -17.0945 | -57.390202 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40425213-ce46-3b88-8ff0-0517be1ea03c | -17.096201 | -57.3983 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3fe47d9-a871-335c-96c9-cb888941f3d0 | -17.0979 | -57.406502 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4409d534-f7c2-3ff3-b6e1-62bb62067f21 | -17.0996 | -57.4146 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 648b67b7-9048-30db-8ba0-dd517577cd5b | -17.101299 | -57.422699 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 611375d3-e80a-3dd1-8f05-18b500e76b49 | -16.6133 | -55.2113 | 2024-10-07 01:20:52 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b04fca85-e3d9-310b-b60b-b0740baf8738 | -16.9527 | -56.769402 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fb2b8fa-4069-3208-8248-f25620b39207 | -16.9543 | -56.7771 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 583b090f-869e-380c-b1c9-eb427baa11d0 | -16.9592 | -56.800201 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08ea9401-6470-3643-866e-e7eff4a38723 | -16.960899 | -56.807899 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61bfedd2-e1ec-3987-ab86-ee7e307ddc66 | -17.086399 | -57.400501 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7823bd0c-4473-36db-b9df-11addc322df4 | -17.0881 | -57.408699 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fc763d5-d773-3fd7-9c18-2e38659c04e6 | -17.0898 | -57.416801 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1eaf4ff0-a55a-3c24-9cec-63e3f43578cd | -17.091499 | -57.4249 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ec37a02-5148-3b38-a37b-28b585b6de90 | -17.076599 | -57.402699 | 2024-10-07 01:20:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 143974e6-bbbb-3bf2-8901-f2166e998c6b | -17.0783 | -57.4109 | 2024-10-07 01:20:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 945b89f9-74f2-345d-8a2d-f13ff97cb405 | -16.6373 | -55.552399 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf3bf4eb-266c-36bc-81a9-6bbb1af7d52c | -16.638901 | -55.559601 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e56cdba-092b-3cdc-a1b4-c6e2d3180a9b | -16.640499 | -55.566799 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16fadfdc-f3ee-3e8a-95e1-0e65edaf39ae | -16.6196 | -55.5187 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0222cae1-8e5a-32ee-b936-8fe8dcf09948 | -16.621201 | -55.525902 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9de06dfd-7976-39d6-81ee-a9fcac54b19f | -16.627501 | -55.554699 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 502bfdf6-c5e5-31e1-b861-e29881f8e43a | -16.629101 | -55.561901 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9d377bc-0518-37e3-bff6-c70fef105851 | -16.630699 | -55.569099 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f09052af-47c5-3d6c-845d-3a2b9b19379e | -16.632299 | -55.576302 | 2024-10-07 01:20:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d108fe77-65ea-3cd1-81bb-454537df7731 | -15.872 | -52.299999 | 2024-10-07 01:20:54 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97f14702-fdd3-32e4-9dd6-1c16eacaa375 | -16.613001 | -55.5354 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db6de8fa-ba9f-3779-b14f-968fad8c4071 | -16.6145 | -55.542599 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e188976-4e67-35c2-b9fb-746136cab5d4 | -16.617701 | -55.556999 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5149d0a8-8e36-377b-8958-5060fd25c963 | -16.619301 | -55.564201 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa585b9f-6d41-3cd3-9114-2b40197e82e6 | -16.620899 | -55.5714 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6687dabd-8847-37ed-8f40-960394521d22 | -16.622499 | -55.578602 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20d738ce-3683-3cab-b65a-4cb9485f0831 | -16.690701 | -55.889801 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0d2445b-7696-309b-8ccd-ea53f53f37b3 | -16.692301 | -55.897099 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69fc39e4-72f5-383d-8fa4-9803f833147e | -16.693899 | -55.904301 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd6011da-f548-3318-877d-947f32abe675 | -16.695499 | -55.911598 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7b5dcce-a491-3380-98d9-2a1027da79c8 | -16.8678 | -56.708302 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8302bd3f-5156-3a77-bcde-751c2250cfc3 | -16.8694 | -56.716 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0def968-bd65-3ea6-a16a-cffbb6cf7cbe | -16.871099 | -56.723598 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce202b6a-db6e-398b-8975-754ce150bed1 | -16.8727 | -56.7313 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28b1ebf6-f14f-3d33-92e4-4464af0c10fa | -16.607901 | -55.559299 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbc4b867-2c49-3f40-96ba-98d59405f009 | -16.609501 | -55.566399 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 079d0d44-7bff-3c5f-b692-146ab7514de3 | -16.611099 | -55.573601 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf150848-32b3-3586-ab22-5525e45fce1b | -16.6127 | -55.580799 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a962dc55-4e18-3d99-8576-2659ddc058b2 | -16.6777 | -55.877399 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 329cd440-6723-377f-89c2-8db9897fe493 | -16.690399 | -55.935699 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7643459-eb39-375f-821f-33ce8a5897d4 | -16.691999 | -55.943001 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2877fc6e-f258-3631-9a6c-67f0b50fcc70 | -16.6936 | -55.950298 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0f23bcc-bf1a-3268-b8cd-b095decdcf02 | -16.8564 | -56.7029 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2bab1b4-ac96-3047-a491-c29d655406dc | -16.858 | -56.710499 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b60fe1d-b2ba-3d63-b40e-66732c08a13f | -16.8596 | -56.718201 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cb97ae4-d5cd-3633-9dab-d1ab3da83312 | -16.8613 | -56.7258 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5cdb7e33-b86e-3f7a-9308-544ea7b0b56e | -16.8629 | -56.733501 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da0d0b76-bffe-3f49-a341-590ce1d643d7 | -16.601299 | -55.575901 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f5e85d1-7c58-39d5-83c8-edf196432e3f | -16.666401 | -55.872398 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2d10d88-9e5f-3348-a772-f9dff304df54 | -16.667999 | -55.8797 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f449e62-66d4-3fd4-9278-4aaf722b3963 | -16.6696 | -55.887001 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb810473-8c83-393d-a215-e6419332129d | -16.671101 | -55.894299 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8cb759f-bfa2-3bd0-b557-788958e9d011 | -16.682301 | -55.945301 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6997498-eae7-3ece-b6b0-bce7abcd8c45 | -16.683901 | -55.952599 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cac6bfa7-5df8-3bc5-a3bf-ba03741f5814 | -16.8466 | -56.705101 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e3119b3-3915-3348-8548-9bc947dc0b7a | -16.8482 | -56.7127 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a74bac07-fb96-399a-bd22-42e8d16cadf7 | -16.8498 | -56.720402 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63c34f24-b178-3b72-b35e-f4727a7b53a4 | -16.8515 | -56.728001 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1112e064-9a3b-344e-95b2-b990afe35945 | -16.8531 | -56.735699 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ac5cbe0-7964-3a11-a799-7f1b3721b4ec | -16.8547 | -56.743301 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e2cb7af-dab4-3f85-b354-cf43d1251adf | -16.658199 | -55.882 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README22.md)
