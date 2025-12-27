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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5423f4de-49e8-3f75-84e2-279a99c5734f | -10.62013 | -36.95784 | 2025-12-27 11:36:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| cbd9b7af-0c6a-3a5a-9147-31c4b9f30f01 | -8.75306 | -37.28978 | 2025-12-27 11:36:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 59ef8d06-b29b-302d-b426-e6374bbfe493 | -9.6075 | -41.72254 | 2025-12-27 11:36:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f2dfd0e0-b824-32fc-9116-4a438e8fb653 | -7.59532 | -37.13931 | 2025-12-27 11:36:00 | TERRA_M-M | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 34206157-dce7-3e26-b677-5026065587af | -5.88415 | -39.68898 | 2025-12-27 11:36:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 618a8ad9-f627-345b-b27c-ff1076d39342 | -5.32088 | -39.18573 | 2025-12-27 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 769703a8-663c-3477-b299-aa86b0a8ac6c | -5.96833 | -38.20644 | 2025-12-27 11:36:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f61353d7-f338-3991-a1f6-a2b013bd7fbf | -5.32219 | -39.17674 | 2025-12-27 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cf2c973f-98e4-3c28-8806-743e9867c01b | -6.68732 | -38.08541 | 2025-12-27 11:36:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 18c581a9-bea7-36dc-8a5b-9285c298cddd | -7.65686 | -37.48666 | 2025-12-27 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 9c9417e3-d387-3338-84cc-3f38b941ecef | -8.52844 | -36.84902 | 2025-12-27 11:36:00 | TERRA_M-M | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d76220c9-b577-31d7-ba5e-62fae8785c85 | -7.53646 | -39.23891 | 2025-12-27 11:36:00 | TERRA_M-M | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 826250f3-9196-36ef-9974-8fbd60f0d1cc | -9.18017 | -37.85856 | 2025-12-27 11:36:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ff142054-9329-314d-ade8-5d93f8ca640b | -6.03144 | -38.03201 | 2025-12-27 11:36:00 | TERRA_M-M | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 3d60f426-7d85-335f-b04a-1beee6449452 | -6.55183 | -35.16178 | 2025-12-27 11:36:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 0ecc8ad1-72ff-37eb-b6ad-21940b467049 | -7.65008 | -37.46975 | 2025-12-27 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| ab65d56a-783a-3ea3-acc6-13af684bef1b | -8.2669 | -37.99821 | 2025-12-27 11:36:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e03f074b-3dd3-3027-9d94-3e46e4e4ba88 | -7.65405 | -37.44179 | 2025-12-27 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0a111df4-1fcb-3aab-8c32-1e6ad1321b5a | -5.26397 | -39.31862 | 2025-12-27 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 5da73c9c-6030-365d-b699-59eb6edb193b | -7.65815 | -37.47733 | 2025-12-27 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 143.2 |
| 30f89034-0de0-3390-be3f-5952f8a1be8e | -7.64876 | -37.47906 | 2025-12-27 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 05d38f13-2384-3855-8b4c-32ae25595635 | -7.85904 | -38.01836 | 2025-12-27 11:36:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| dfd30f1e-feeb-3c7b-b95a-a6f631291f1a | -18.12435 | -42.87323 | 2025-12-27 11:38:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| ca2413f4-8f9a-3291-ae27-aa4261357171 | -17.80857 | -39.70929 | 2025-12-27 11:38:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 71bbebff-0373-3358-acd8-6f7e25734eab | -18.1163 | -42.87551 | 2025-12-27 11:38:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| dade847b-7d8e-3223-afb4-93d6cfc4ceea | -17.80989 | -39.69963 | 2025-12-27 11:38:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| e81cf442-929e-3d49-bd8f-f740b5755635 | -18.12282 | -42.88317 | 2025-12-27 11:38:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0f84924c-fc34-3e84-aeca-d1ecdce358d5 | -18.14493 | -40.20912 | 2025-12-27 11:38:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3d35bae8-a746-3729-9661-66de7bfbdb0d | -15.20764 | -42.62442 | 2025-12-27 11:38:00 | TERRA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 14f177db-5f9e-3326-9060-2819dbd5f88b | -0.1012 | -51.2738 | 2025-12-27 11:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 82e20ad5-33f2-355e-8dcb-76e73329bee5 | -0.0828 | -51.2738 | 2025-12-27 11:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 212.6 |
| 2c573b8d-89d0-3a2d-b607-d053f6d30541 | -19.32686 | -43.5157 | 2025-12-27 11:40:00 | TERRA_M-M | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a625773f-dba3-3352-8432-3d880841887b | -20.99957 | -42.96864 | 2025-12-27 11:40:00 | TERRA_M-M | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| e00f8cdc-a007-3080-bdf5-aff8dd901b42 | -20.99058 | -42.96712 | 2025-12-27 11:40:00 | TERRA_M-M | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8efc8612-6fc6-33ed-9487-0726d4c763cd | -20.89121 | -43.25769 | 2025-12-27 11:40:00 | TERRA_M-M | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b4293d10-3d03-3f46-b4b4-9d9d432b6431 | -20.89149 | -41.5621 | 2025-12-27 11:40:00 | TERRA_M-M | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 59fe3d92-3a62-3840-b4ae-a074b6732d94 | -0.1012 | -51.2738 | 2025-12-27 11:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3f407b60-a40e-3517-8a08-26e88c8a81f0 | -0.0828 | -51.2738 | 2025-12-27 12:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 262.6 |
| cde5099b-d4b9-3e7c-8941-44a51bf514c8 | -0.1012 | -51.2738 | 2025-12-27 12:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 00c8789f-819f-3d50-b786-240eead53055 | -0.1012 | -51.2738 | 2025-12-27 12:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 27485682-550c-3955-b600-8fa619b65afc | -0.0828 | -51.2738 | 2025-12-27 12:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 245.5 |
| d321e3d7-eab0-352f-9d93-6d5e138e6cd5 | -0.0828 | -51.2738 | 2025-12-27 12:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 157.2 |
| cf7040a9-e930-381c-8e9d-4483ab61d134 | -0.0828 | -51.2738 | 2025-12-27 12:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 229.7 |
| cde78b9a-fdc9-308f-a799-f6da8b780404 | -0.1012 | -51.2738 | 2025-12-27 12:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a98d5498-a21d-3a38-ace0-2385eb7bcbdf | -3.7701 | -43.5554 | 2025-12-27 12:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| e1931c48-3fdf-3a44-8b00-a5472bf16b9f | -3.9069 | -42.5672 | 2025-12-27 12:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 73f2879c-9a1f-3631-85df-da36ed7d0116 | -0.1012 | -51.2738 | 2025-12-27 12:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2989ddff-63fb-3c2d-863e-04c7ad24aead | -3.9071 | -42.5436 | 2025-12-27 12:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| bda6632a-5fd8-3165-ad7a-e90d22825a1f | -3.9069 | -42.5672 | 2025-12-27 12:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 3ff4a067-d29b-3ed0-bbe6-6a15bfd1acea | -3.7701 | -43.5554 | 2025-12-27 12:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| c87e42a4-148e-3e79-9480-153bf928a89b | -0.1012 | -51.2738 | 2025-12-27 12:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 97.7 |
| df22bd8e-a8a2-385b-aee6-ae7af316c284 | -0.0828 | -51.2738 | 2025-12-27 12:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 182.4 |
| e7dea913-28ca-38c1-b4dc-ecef12876c17 | -0.1012 | -51.2738 | 2025-12-27 13:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ad4bf1d4-d5b8-384d-b7d4-3d5068fbc851 | -3.9069 | -42.5672 | 2025-12-27 13:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| dfe2a49d-6d3a-36c6-aabd-71b612af0ffd | -3.9069 | -42.5672 | 2025-12-27 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 07142154-dd1d-3066-82ac-667c060334eb | -10.4889 | -44.9235 | 2025-12-27 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e0acf157-bffb-3159-a9d1-0d3c332b81f8 | -3.9071 | -42.5436 | 2025-12-27 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 466ddf96-c180-316a-83e9-8fd032095a53 | -0.1012 | -51.2738 | 2025-12-27 13:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a82734ea-d768-3a2b-a9a5-eb438853400b | -3.6398 | -43.5155 | 2025-12-27 13:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| eeb3cac9-4e24-3248-9476-f95c4f4a175e | -6.4365 | -37.5237 | 2025-12-27 13:30:00 | GOES-19 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 39a925c9-29eb-37c7-8663-5370218288fc | -6.1716 | -37.4739 | 2025-12-27 13:40:00 | GOES-19 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 98.1 |
| a4320d96-90a4-3f47-b646-dd279d013a81 | -6.4365 | -37.5237 | 2025-12-27 13:40:00 | GOES-19 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 94.5 |
| e62351d2-9d2b-3de3-b25f-81b89f8e8e32 | -5.4691 | -37.6726 | 2025-12-27 14:00:00 | GOES-19 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 47a4eab4-76a2-31b3-a8c7-53000079ddc7 | -5.3937 | -37.6535 | 2025-12-27 14:00:00 | GOES-19 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 7c2dce90-9021-3fe6-ba8d-3f1a8dde27a8 | -5.4694 | -37.6466 | 2025-12-27 14:10:00 | GOES-19 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 87.2 |
| c24ab666-feb8-3279-bbaa-3400e6d152e0 | -3.6398 | -43.5155 | 2025-12-27 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 7d454101-eb2f-37cf-8108-4fa6bc4052f9 | -0.1012 | -51.2738 | 2025-12-27 14:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 2238a433-0084-32c2-92ab-a0ed3f12c31d | -0.1012 | -51.2738 | 2025-12-27 14:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 156d276c-11f0-34c6-8c19-a171a01a2b45 | -0.1012 | -51.2945 | 2025-12-27 14:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 78.9 |


