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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa12dbc6-2869-369a-b3cd-b24f898b374a | -3.3457 | -49.23138 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0510fb9e-d251-3e5f-ac3b-07e7d54af48a | -4.85537 | -42.47284 | 2025-12-04 04:48:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 470518d1-e62a-317d-9f2e-42c25026de74 | -2.38706 | -49.39212 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af99c347-9afd-3b7c-9c0a-1c604440fe63 | -2.14855 | -47.87841 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c615becd-b457-3716-94ba-eaade88b0655 | -2.68652 | -51.66814 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f24cf0d-9f5d-39d6-983c-691c46e14ffd | -2.54078 | -49.45222 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a7b9723d-973a-3208-a3e2-bb5c0ceef428 | -0.37397 | -52.04803 | 2025-12-04 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38c2152d-3ce3-3ed6-8d75-fc8f8c411b93 | -1.12314 | -53.4476 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0942fa04-0152-3bc4-9ed8-a7536f8b254e | -2.14034 | -47.87741 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0803d1cd-ae3e-3731-916a-67395ac23f12 | -2.73284 | -51.55076 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5eba252-3859-35e2-bd37-7b93c0db9d83 | -2.8641 | -45.24535 | 2025-12-04 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b109a2-648f-3b00-8794-988c8d71333e | -2.19431 | -46.46852 | 2025-12-04 04:48:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 967dc203-40d5-3cf3-95b1-6d2e56af6be7 | -2.41821 | -48.59426 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e30345-6398-36a5-b621-21768df0d99a | -3.32757 | -44.38328 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f95777a-3e63-36a1-98f3-2f55123bbfda | -4.43118 | -43.86234 | 2025-12-04 04:48:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d607870-c650-3905-850a-45dd550d5fbc | -1.6955 | -46.1545 | 2025-12-04 04:48:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b99e62d-65cf-3d0b-b12a-e67097ca9613 | -2.45473 | -49.22348 | 2025-12-04 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea741d48-4d38-3aa1-9ad9-1bfed187e810 | -2.36551 | -47.6868 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448f2f9d-ef44-3659-9fc5-a7e5b38c2c78 | -3.22052 | -48.61965 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b5a7170-ddea-3ea2-bfb7-b163c3302a11 | -3.389 | -47.27206 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa8198bd-d901-3285-a07b-17aa7817e289 | -3.04237 | -48.41901 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38d89dcb-df1a-3362-a2aa-29ba27553f47 | 0.40753 | -50.75599 | 2025-12-04 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f87fa6e3-1204-35c9-99e1-583b356cb151 | -0.55472 | -51.78145 | 2025-12-04 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd3b422a-c435-3a66-a860-cdb080f0d515 | -4.38457 | -46.672 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aad32d05-63ce-3542-b02a-f29cc10a7054 | -19.6241 | -56.8339 | 2025-12-04 04:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 7c2628b9-42bd-35bb-802c-29655bac3688 | -4.60002 | -45.99829 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e37003ac-f77c-3310-908d-03f71a29b22e | -5.2233 | -43.96353 | 2025-12-04 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74dcd760-7fcf-38e2-8111-856793998d13 | -4.70144 | -45.70281 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baaedc8d-bd53-3e66-9604-859736d650b9 | -5.36319 | -43.0329 | 2025-12-04 04:50:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 961cf844-a740-3e9d-90e5-e0606e8ce1fc | -4.78844 | -45.62069 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98571375-58bf-30de-aa7b-c2a63d08cc83 | -6.33441 | -41.40229 | 2025-12-04 04:50:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 364ab05d-6fa7-380d-ba48-35cefd7276d2 | -5.3443 | -42.12106 | 2025-12-04 04:50:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fef7223-d0b4-389e-b869-794f43419c04 | -4.60474 | -45.99376 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82c03a26-b40a-325c-8fdd-ead265515aff | -5.02639 | -43.96969 | 2025-12-04 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0135c2f-b895-3ae6-9c56-7a4b33086b63 | -6.42345 | -44.79721 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a97e68a-ff20-3544-82fd-0d06d4bb3fa3 | -4.7009 | -45.70635 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf596b4d-05c4-3e7d-8158-2f781d2bedb7 | -6.33855 | -41.40183 | 2025-12-04 04:50:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 080ae54c-598f-3ebf-b4db-4bd41c04e18e | -7.12735 | -44.7589 | 2025-12-04 04:50:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6313211c-be71-3cde-8b78-26ca59537825 | -4.60398 | -45.99887 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a76da29-65d7-35ae-af90-72297ed90898 | -5.85731 | -39.93187 | 2025-12-04 04:50:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b229ea54-ff11-3c8e-bddd-ec41732d84e9 | -5.18501 | -46.07022 | 2025-12-04 04:50:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c1a3124-7ce6-3c13-868b-2761f613f38d | -4.73422 | -45.70462 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea145379-dc80-3d60-9fcb-11257291eab4 | -4.73021 | -45.70384 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a693e134-67ed-3f56-82a0-57b18676beb9 | -4.69033 | -46.43583 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42b4af99-4fe2-3f5c-bc36-5dcbcfe850c8 | -5.98677 | -44.59514 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4aef213a-544c-3cc9-83cd-14ad9e52971c | -5.49362 | -50.98321 | 2025-12-04 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2539b572-2cb7-3272-b66b-038d852cfb3e | -5.99024 | -40.36992 | 2025-12-04 04:50:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 48c0d743-ff4c-3f4c-8638-38d642673598 | -6.58529 | -44.669 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd195bcc-de16-3e78-a19a-ffabcd46c11c | -5.99556 | -40.37505 | 2025-12-04 04:50:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8df8776-500e-32aa-8ac3-1f7b4211107e | -6.05657 | -43.74716 | 2025-12-04 04:50:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 167e4014-3a7e-3ae8-944a-cb61f2c5a4d4 | -5.03027 | -43.97509 | 2025-12-04 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ae9f4ff-bd6f-36f8-ab09-9c9a66e72771 | -4.60284 | -45.99191 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0152a9-a732-331e-948d-d0404edcf820 | -4.78478 | -46.13097 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e894fe3-7f55-3531-b3d6-2d65562947c8 | -6.49716 | -43.80021 | 2025-12-04 04:50:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c9cc9f4-ccb0-3c4c-a01e-524fd45e33a9 | -4.3711 | -49.18838 | 2025-12-04 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00831192-c9df-34d6-98e5-077a6e976114 | -7.21873 | -45.04887 | 2025-12-04 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8352f70f-a774-34f6-a8f1-fad038faa7f3 | -4.6068 | -45.99248 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80c3256b-3b10-38c3-8488-5a8a7f49b114 | -5.47851 | -45.40602 | 2025-12-04 04:50:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62c7b948-2bbe-30cf-9fa9-ced7a30fcfc3 | -4.92762 | -44.70821 | 2025-12-04 04:50:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d222c97-991e-3438-b970-07adf6ae8bce | -5.98756 | -44.59624 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87e1a331-c0c6-39e2-9f02-150eccffc9d4 | -4.66649 | -46.3046 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 911bd236-7e27-36ff-a85e-fcf6f0da9145 | -4.85564 | -44.88147 | 2025-12-04 04:50:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf9286d-3942-3a2d-9ee8-9de32ba964c5 | -5.79393 | -42.99017 | 2025-12-04 04:50:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 201a078c-0850-3831-a641-24210dda8392 | -4.81338 | -47.34133 | 2025-12-04 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49f228bc-b7a7-3dad-a384-12b98495ae02 | -5.00829 | -46.8539 | 2025-12-04 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a6a652e-cd42-3455-919e-88a50c15e278 | -3.84427 | -50.89989 | 2025-12-04 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14428264-6209-3c2a-8605-c9a259809a2f | -5.98232 | -44.59453 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b748398-3ca5-3d23-bf93-941e48a40022 | -5.00797 | -46.85608 | 2025-12-04 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dbcfc60-31ef-36ba-8ed4-60cb3bd0c208 | -5.77067 | -45.97566 | 2025-12-04 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a5b1b5c-065c-3c18-9f07-f9b8a5f8d9e9 | -4.90369 | -44.50535 | 2025-12-04 04:50:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ff33943-531f-34f6-828f-3c27dce4bd94 | -4.67037 | -46.30524 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83da6fd-d57e-3d86-962a-bed1bbc35ad7 | -4.03477 | -50.38169 | 2025-12-04 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd3f1d6e-771a-3717-aae6-620e6ab27541 | -5.02571 | -43.97435 | 2025-12-04 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebbef6a8-7c99-3e8a-9868-892b8d665a85 | -5.33908 | -42.1203 | 2025-12-04 04:50:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d35c76d8-ce03-3cb3-8dbe-8eceb278b275 | -4.69876 | -46.43227 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2585c7c-e433-341a-8ac7-c45d4c3050b8 | -5.9817 | -44.5989 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| caf6db08-f79a-3035-95d5-6e2d4aa058ec | -5.99497 | -40.37932 | 2025-12-04 04:50:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80090e1c-d35c-3913-8e2c-e7830fc04f1a | -6.42407 | -44.7929 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d44d5ff-6ceb-3e9c-8983-fe60b57b84bd | -6.00898 | -42.32647 | 2025-12-04 04:50:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 963abb69-fd7b-3012-8269-c11a64a0aaa3 | -7.21946 | -45.04677 | 2025-12-04 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8cc2a1a-0963-332f-b653-40090362723f | -5.41341 | -45.76146 | 2025-12-04 04:50:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f5fd9b2-400c-3091-89d7-7129cb7a83cf | -4.78083 | -46.13045 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 517fffc5-c238-33e9-9999-b3ed3ef19ef3 | -4.59187 | -46.05333 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90de7ca-b36c-36f8-9bb9-708d36a44e44 | -4.2532 | -49.2509 | 2025-12-04 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7472867-9adb-3db2-bfd1-d9ae05bde9a2 | -5.22289 | -43.96527 | 2025-12-04 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34fdb285-60cd-3d47-ad4c-682528248a9c | -6.42912 | -44.78912 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 060f3a3b-2654-3060-93e3-81fcd9e480c7 | -4.69738 | -45.7023 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ce67bc-9409-3196-8d73-5f9e1b0227bb | -6.4285 | -44.7934 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebf73b27-1d45-39dd-97f5-36be6feb03c8 | -5.97867 | -44.59502 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc8d6da5-e76b-307e-8dcf-c1801cfcc313 | -7.5923 | -45.89444 | 2025-12-04 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| defd3c1f-583d-3e91-a7ce-0aada6b7d387 | -5.57087 | -45.42231 | 2025-12-04 04:50:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c083aa3-e71e-3631-b716-e820eaf24616 | -5.98246 | -44.59999 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fcb2b6f-c615-371f-ade1-6de0caf4558e | -4.20197 | -50.6734 | 2025-12-04 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aacba37b-2013-39f3-a6ef-4f3b3d821a76 | -6.333 | -41.401 | 2025-12-04 04:50:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b466f96-9c57-3dbf-a349-c8ae5a13de84 | -5.34476 | -42.11789 | 2025-12-04 04:50:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42043074-5c8a-3026-bff3-4c8f1ec7d448 | -5.03094 | -43.97044 | 2025-12-04 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82e4dbea-97f2-3120-be6e-8b42201ed74c | -7.21936 | -45.04466 | 2025-12-04 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87b1f592-9117-36da-932b-34dd7841b72a | -4.60204 | -45.99704 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33ec5830-daa8-3d10-91bd-88c363691e67 | -4.45645 | -48.73042 | 2025-12-04 04:50:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f382e99-297a-3fb3-955c-7c4b6f324c3b | -5.55752 | -45.45534 | 2025-12-04 04:50:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
