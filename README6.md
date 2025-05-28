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
| dd26e797-f468-3351-8dfc-bd5ad6a614eb | -5.64781 | -43.58634 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ae3ede-c822-3d9a-82f7-98635072344b | -7.18208 | -45.10334 | 2025-05-28 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0eb578-70a0-342e-9a48-4c4f5b036253 | -6.63645 | -47.34435 | 2025-05-28 04:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04f3b115-b58e-33ce-a686-f4fef8910e9c | -7.18637 | -43.11475 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7b659b3-105f-3a70-af88-922c22034980 | -6.03126 | -44.04892 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30566a9b-50bd-3c25-aeb6-652e0fb6de33 | -6.62136 | -48.0238 | 2025-05-28 04:08:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7ea2c31-80dd-33c5-8c1e-648166b3f45d | -7.18299 | -43.1142 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a04ac1fd-0ff3-3242-a041-27790e2e5062 | -7.33894 | -43.68459 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9158c4b9-4842-325f-a8bc-91d13a51ebcb | -7.1943 | -43.10864 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ee98a65b-9d84-3ba2-b3b2-83d269691257 | -7.2174 | -43.11605 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfeec60c-2a67-3447-bf6f-1c1618be4586 | -6.33125 | -43.37302 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffeb0ea6-055b-394b-a955-3235562b1a73 | -6.33587 | -43.36613 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79a5028b-c8d1-32a3-87be-4c221005c9f9 | -6.31977 | -43.37883 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 451831c8-6611-383a-8ddc-38a045a48c48 | -6.21461 | -48.48654 | 2025-05-28 04:08:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 950a6f12-7b64-30fd-b7c6-55393c1db118 | -5.7808 | -43.61802 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b98a2c4-6c7e-3986-bc3b-bc1de35b0d03 | -7.61138 | -43.40218 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7ce876c-5991-37fd-8103-e5dcc6849880 | -6.21574 | -43.35099 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2ec4cd14-3f26-3149-87d1-a08df618da04 | -7.36481 | -43.67727 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6c4aeba-8211-38c3-ad04-8d099cb175a5 | -7.19091 | -43.10809 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3fcfd93b-5eb2-3e9d-999f-45041f4f9580 | -5.97165 | -43.75317 | 2025-05-28 04:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e841b0d0-6899-398a-b79f-89d05e11b8d7 | -7.20329 | -43.11749 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 44b84545-d81f-3d12-bcc3-c4ae2bdf5579 | -5.65068 | -43.59071 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 183babe9-b025-3010-9a5b-6d8727dfa5b2 | -7.21798 | -43.11245 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d9dabeb-8e36-35a2-a4dd-127fad6a6a1f | -7.19366 | -43.24234 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dce3a504-7d1b-370f-b044-b339955f045c | -4.90256 | -42.23319 | 2025-05-28 04:08:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6ff66b39-dab7-3716-91ed-077bb9e8d760 | -7.22136 | -43.11298 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| feefe6f2-c9e0-3118-857f-cb1c6d9d5727 | -7.34643 | -43.68193 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed87dd89-5af8-31c3-92b3-940a97afc35d | -7.20667 | -43.11803 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fd784124-5fce-39ee-a9c9-f6b024ae3aed | -7.07958 | -46.05032 | 2025-05-28 04:08:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 468fecb9-a144-3d9f-96d4-4842ba3f1128 | -7.20725 | -43.11443 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7af1bab6-8214-3e80-94cf-954499a0696b | -6.20947 | -43.34624 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d9e0ad6f-f378-38cd-b6ed-c7752a8436e6 | -7.60857 | -43.39796 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e53326b-da2f-378d-b80b-e1055d819614 | -6.31753 | -43.37083 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2458bfc-b96f-327a-8694-d55b92fa7423 | -7.61079 | -43.40583 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23d48515-d415-386e-a3b3-049982cc371a | -6.20888 | -43.34993 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f9c9a444-5c07-3a14-8e19-1c09dcbc3b06 | -3.13042 | -40.98888 | 2025-05-28 04:08:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 95a066a3-3a9a-3704-8b45-c331a14a32e9 | -4.41575 | -42.13821 | 2025-05-28 04:08:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aecc64ec-1170-325a-b8b8-f17b3dc20cee | -6.33185 | -43.36929 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e816ecb5-1108-3064-b8ba-6676de2a444d | -7.56761 | -43.32777 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74073426-fd16-3d1d-a907-cf0db26b7d53 | -5.7617 | -43.48331 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a329eae-84a5-3058-8597-223872c78aaf | -6.61691 | -48.02311 | 2025-05-28 04:08:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e8198d-f8b0-3ebd-ae00-a5e6df72c350 | -5.78142 | -43.61421 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eed86af-90ac-3250-8f18-41fcfa3b56dd | -7.61302 | -43.41367 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c8162b6-3e5b-3fe3-adfa-0187e5e6055f | -6.50891 | -43.63808 | 2025-05-28 04:08:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b52ab14b-6894-3c0e-b5e8-d56684cce4b2 | -4.48524 | -47.79258 | 2025-05-28 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f56e5c0-a32e-3d0a-b814-4d4ffd4a4c2b | -5.6472 | -43.59015 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31cfd433-1d49-3f41-bdd3-eb8e9feb948e | -7.19488 | -43.10504 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5074fe6c-61fc-3c85-9912-a77fbc9a8c8b | -6.32782 | -43.37246 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919d334f-b930-30d6-afca-02f34e18e596 | -6.12 | -43.94727 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 931b0ac8-4e33-3e94-93a3-0ec956022baf | -7.60915 | -43.39432 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637cf174-7c89-3fd9-a0e7-09584d980129 | -6.05725 | -44.04493 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d908341-717d-3433-a742-572ca2077b99 | -6.75202 | -44.63447 | 2025-05-28 04:08:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56e95a22-b410-371a-84c8-968c86aad989 | -7.56466 | -43.34596 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7ff2a6-9aa9-3b35-9d33-614809e39b9b | -7.38945 | -43.73423 | 2025-05-28 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f2f514-71a5-3ecb-8644-6164f853c89c | -6.83469 | -43.41087 | 2025-05-28 04:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ea09ad25-65c7-350d-a010-8704e066d556 | -7.55683 | -43.32979 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1e7f0fb-98ff-322b-b4b3-b866952fe5e2 | -4.65988 | -48.15067 | 2025-05-28 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 305e43b5-dec7-3a5c-a25c-199cd5486caf | -6.20545 | -43.3494 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92dc8bdf-7a82-3a8b-ac76-7f0b8be666f8 | -6.32037 | -43.3751 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9c23a53-96dc-3565-a838-3d003a201a48 | -6.31634 | -43.37828 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a3112ac-ec04-3d64-8e85-4ce820b3035b | -7.19372 | -43.11225 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ebcfaf0a-d91b-310b-bb5f-bbbfae107c1b | -7.19932 | -43.12055 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4794c76e-c4d8-3136-b6ca-2bd4e76ebf65 | -7.18357 | -43.11059 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 739993f8-2113-33a6-bb51-213d95a82bf9 | -6.03062 | -44.05284 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4c5d2a3-2eda-332e-9809-63e8702b34cf | -7.18695 | -43.11115 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fd658cf2-10bf-3d31-9219-986609bd9ab0 | -7.08345 | -46.05095 | 2025-05-28 04:08:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 35fbfae7-76ad-3066-821c-cee009b5648e | -6.33527 | -43.36985 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3571155-492a-32a1-90d0-395ed26c8b95 | -4.17011 | -42.0308 | 2025-05-28 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| afce3dab-d967-39a7-80ed-6ad808039e44 | -6.6292 | -43.21254 | 2025-05-28 04:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1180e76f-42a9-345c-8c98-436a5efedbc5 | -7.34238 | -43.68513 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1cc725e5-e24e-3385-b15d-f57f4c1f7e73 | -6.32096 | -43.37137 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2451691e-dc9d-3674-8126-f41a92b52bcc | -4.42082 | -42.10641 | 2025-05-28 04:08:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bef477ba-ea8b-37cd-b33a-6a241e7d0789 | -7.3188 | -43.41901 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc5bc82-b1af-30f2-9643-1f837feb0fba | -6.21231 | -43.35047 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 403b9870-ff59-3a30-93a7-b5b055a60a70 | -7.1999 | -43.11695 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6e2c9c2c-391f-38ef-a6cc-aec6a605c05a | -4.51339 | -43.68837 | 2025-05-28 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 049cf98c-5ea6-3857-b791-ca1a6de5200b | -7.08732 | -46.05158 | 2025-05-28 04:08:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f6cd1963-44cf-3660-9f3c-c85972292755 | -7.23981 | -43.47466 | 2025-05-28 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3bad8a2-9d21-3a33-a9df-f36e94b642cb | -5.76862 | -43.48438 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e86e76b-2047-3041-a142-7cd6551c0a81 | -5.77208 | -43.48492 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36478908-d896-3f1c-a4dd-3c7ec5517a07 | -7.56068 | -43.34903 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8135631-7723-3a9c-9b44-2ddb8e9d20e4 | -6.3238 | -43.37564 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59c26982-50bf-3030-8fec-fb39510c7076 | -6.1235 | -43.94785 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d264760-c4f8-3897-b00e-5b507bef64df | -7.18968 | -43.24545 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22014854-916f-32e4-b0ec-8f837eec7ea4 | -6.64828 | -41.99549 | 2025-05-28 04:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91ea6ed1-0923-3779-8801-b6ed03d4dcdc | -4.60127 | -47.25647 | 2025-05-28 04:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf1a776-b65c-3a22-b38a-d18cc7dee71d | -7.35047 | -43.67875 | 2025-05-28 04:08:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 271dcb20-2519-3644-81a5-5b6cbf96358b | -5.77147 | -43.4887 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4158673c-da4c-3b59-a3a2-5341d7ec5e9d | -6.11937 | -43.95114 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aad34d9-fef2-3486-b509-d020cd382e6a | -6.21291 | -43.34678 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cf2acfca-4202-38ee-8fd9-bf6ba2f3e9dc | -4.43128 | -46.10968 | 2025-05-28 04:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f8c5cae-463f-3708-baa2-ab96ff1cbd2c | -5.78427 | -43.61858 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b90004-070a-3377-a75d-1eee1e542e75 | -6.12226 | -43.95558 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a46275ee-f089-3a6f-9cce-5e0bbc596d92 | -6.32439 | -43.37192 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c51453ec-b625-338b-ae9f-f0952dbfe99e | -5.7623 | -43.47954 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3a11f71-8c94-3e42-b9a1-21138c0e1ca8 | -5.96817 | -43.75259 | 2025-05-28 04:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7945addc-525a-3b7f-808f-ba9740d63880 | -3.81323 | -48.99194 | 2025-05-28 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b0e02de-69c7-3cd4-baab-a4de51f89336 | -7.35416 | -43.72158 | 2025-05-28 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd131d27-3415-3bee-9327-345fd2a0f3ca | -7.21402 | -43.11551 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3f3ce33-6e0d-3b1f-ada0-9a3858094d9a | -7.19033 | -43.11169 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |


[Clique aqui para ver as próximas entradas](README7.md)
