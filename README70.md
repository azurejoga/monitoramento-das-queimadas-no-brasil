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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19de017d-1c5f-378a-a942-56953b8ed5e6 | -4.89649 | -44.64171 | 2024-10-29 05:01:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d20052-eb4b-3999-a4f0-248d73991702 | -4.89588 | -44.64609 | 2024-10-29 05:01:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3270d749-7a4c-3907-88d6-3a88cacd1be7 | -3.65506 | -44.18727 | 2024-10-29 05:01:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f4919e0-31cd-3438-8904-4157e19cccb4 | -3.65439 | -44.19177 | 2024-10-29 05:01:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42d8a7f7-7ce4-3662-8b1b-2d2ca35fda7a | -6.45698 | -44.67353 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e529e1b9-f09c-3004-8732-73c836750a71 | -6.45685 | -44.67217 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17b1614c-96e5-3599-8140-224cb51324cd | -6.45633 | -44.67837 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f640e330-da2d-33cc-8ef4-8d4e5834f818 | -6.45616 | -44.67707 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 165751ac-175c-3e43-b422-0737158b3c42 | -6.45554 | -44.68152 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9ac307d6-a96a-3b0f-bd46-3e2ba8042e33 | -6.45099 | -44.67199 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ed75b9a-b261-3dc2-a710-5aa7056c09e8 | -6.45034 | -44.67694 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b1634d73-11bd-3985-813a-4a76e16a5e9d | -6.45018 | -44.67558 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 59e5934c-a88d-3d76-908f-d440312e01fd | -6.44952 | -44.68027 | 2024-10-29 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 18292e9e-a3f7-32b3-97ef-02eaecaeea5a | -5.81496 | -44.13148 | 2024-10-29 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe298172-8cf8-3005-9068-a3bd6cde03c1 | -5.81431 | -44.13628 | 2024-10-29 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a62ea985-0c55-376e-af71-9898af48678c | -5.80812 | -44.1351 | 2024-10-29 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d4b0cc8-ba23-39f4-88c2-b494ea0cb47a | -3.13339 | -45.22744 | 2024-10-29 05:01:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf5887ae-e3d5-3f8e-8c04-ef1b1e4ecc53 | -3.13284 | -45.23111 | 2024-10-29 05:01:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11e3f8bd-adad-325a-a87e-bfdb6947202e | -2.2433 | -45.61363 | 2024-10-29 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35cad50c-3415-364f-bde7-57d52f8fc070 | -2.24279 | -45.61699 | 2024-10-29 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31a4c2e1-04a9-3af5-9ecb-4d35ad09ad07 | -4.90624 | -45.76101 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ddc06fb-c50b-3b66-b49c-e14c01718446 | -4.90593 | -45.75996 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6bf4df4c-f534-3348-a854-68e5b213e070 | -4.86021 | -45.76686 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef13157-3243-367e-ae5f-b1505c7f20e8 | -4.27441 | -46.09647 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef41a57a-7a66-3ed5-9db8-5f9929861e85 | -4.2735 | -46.10276 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68562b03-6390-3941-a0f6-232890da812b | -4.27303 | -46.10599 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b6ef076-6f87-355b-aac1-88a6b4f6e7bb | -4.26908 | -46.0955 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d076341-9649-3373-815a-47e4bca215f9 | -4.26861 | -46.0987 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59a37ca5-f0fc-3d9f-8579-4f607b52a930 | -4.27395 | -46.09961 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a909bcbf-d230-3eb4-a466-b1ef9754438c | -4.26815 | -46.10192 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47aae6b6-349d-36cc-aa5e-cf0c5084dcb0 | -4.26767 | -46.10521 | 2024-10-29 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 890f605a-7524-3dec-b224-61208fbc8145 | -5.53498 | -46.26927 | 2024-10-29 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c8c2cc5-0d4a-3b2c-8cee-c7913d9bdca7 | -5.52962 | -46.26822 | 2024-10-29 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eb61aba-12d5-3a9f-908c-4c68fc9fe059 | -5.3655 | -45.65226 | 2024-10-29 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d29b3ef6-993b-37aa-bf00-9f780923348c | -5.36493 | -45.65617 | 2024-10-29 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5895686-9cca-350f-8d13-cb945d26f19f | -5.291 | -46.33102 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdeb844c-6d97-3eed-b98a-5d818fa91aab | -5.29055 | -46.33416 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb9f010-585b-3470-9f04-f7288faa775c | -5.26644 | -46.25316 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 448acbd6-963f-3ede-8d80-1ba5b0602c9f | -5.26363 | -46.25241 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c492ca-f2fb-3225-9bec-ef57bb000534 | -5.10215 | -45.96115 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5ca1646-a57a-32ac-9fc8-24e802812427 | -5.10166 | -45.96467 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d3af6b2-c93d-38e5-903b-af2239fc792f | -5.10131 | -45.96172 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94718a5f-a291-3a3c-a949-0bcc09abec86 | -5.10079 | -45.96524 | 2024-10-29 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf0f7090-1f53-3501-83aa-cf9d304ab6fe | -2.07996 | -46.50871 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78db1315-e9df-3a26-b05d-701e898aa996 | -2.07953 | -46.51152 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b98b07a-50eb-3ee7-9a4c-5364c1a8f14f | -2.07909 | -46.5144 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd8d410-23c1-369a-a6fe-b33a8552c441 | -2.07448 | -46.5108 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad69d34f-8b11-313b-ba41-1495d5825451 | -1.91288 | -46.6012 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d99bccb3-1004-3ea2-9f61-19073efd19c3 | -1.91223 | -46.60162 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668a07e8-6e16-399e-a3dc-5b269e16a0e1 | -1.16337 | -46.53127 | 2024-10-29 05:01:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bdc613a-6a39-3d70-b12a-a412b1489dbe | -1.16265 | -46.53017 | 2024-10-29 05:01:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a87a853-a2dc-3b79-b271-7687ed472f63 | -1.11336 | -46.83052 | 2024-10-29 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86584c6a-340b-383b-acbd-3c802c2fc96c | -1.11256 | -46.83583 | 2024-10-29 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07912f1c-fd92-304f-abe3-1d23e1e74933 | -1.11041 | -46.82872 | 2024-10-29 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2795751a-d121-3b10-8ba9-7dbc15e7b412 | -1.10957 | -46.83401 | 2024-10-29 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99d97b9f-e391-3e93-847a-398a5b06488e | -1.10851 | -46.82972 | 2024-10-29 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35313203-f6fc-318a-bf1d-7a2bec36efa5 | -3.30871 | -47.19572 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ade8501b-f255-3b76-a391-1cb3d911db3f | -3.30665 | -47.19879 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8062773-3c99-354f-9596-911f03e74d63 | -3.25425 | -46.87139 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| dde22720-68a8-3d85-b094-f6ae93158f2f | -3.25404 | -46.87214 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6a390ba9-0afa-382d-8467-76bdf6cde502 | -3.25337 | -46.87714 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c166daa2-d439-3030-aa7f-7cd2e82ea835 | -3.24987 | -46.86561 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 22f9fe0c-17e7-317b-8112-cc3f84440ea8 | -3.24924 | -46.87062 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5575e8bf-8b5b-359d-a7b9-59e3baf5ef02 | -3.24836 | -46.87641 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 07df0e20-41f7-3a2e-ab98-7664e9e94af0 | -3.16712 | -46.60683 | 2024-10-29 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a6ddcb-b6ca-3e85-8939-802d955b4035 | -3.16667 | -46.60981 | 2024-10-29 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bef4616-aafd-3040-8cf7-8df457ef0031 | -2.95873 | -47.36185 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86b2bca3-1bd2-344c-bf06-2408b8832376 | -2.95971 | -47.36063 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7d3e78d-1b68-3789-bee6-75fceb057319 | -2.9549 | -47.35987 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 635d7b35-31af-3ee4-abbb-df93f45f9429 | -3.2532 | -46.8779 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e67826b8-eac0-3b42-8937-3cb4dd697723 | -3.25012 | -46.86488 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ac1d09f8-bba9-3f38-ad52-e518af910b01 | -3.24903 | -46.87136 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2d0bf766-b119-3663-8713-9d76b42d3548 | -3.2482 | -46.87716 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| feed30c0-739b-3d90-8370-a61e4856afbb | -2.71971 | -46.69799 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1186cb8c-28e2-3a1f-8fed-e6f09a660272 | -2.71884 | -46.70375 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 028f948f-ecfa-341c-bd55-c538b3974db9 | -2.71643 | -46.68577 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7248441e-bf41-347d-b193-d9502b71fe1d | -2.71556 | -46.69152 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85157ac8-6dd9-30c9-ab49-f05e281d3b11 | -2.71469 | -46.69726 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 719015cd-a4ec-312b-86aa-1937742aa396 | -2.71381 | -46.703 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e5aec838-0d9c-3494-97d1-a20675a0a4d0 | -2.60088 | -46.14312 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10cb657f-c2f3-37e6-ab42-c88a77d2d0d4 | -2.60039 | -46.14629 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7977ada-4d1d-3ef7-8ac4-b95d736886bd | -2.44637 | -46.13816 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f12b751c-d8aa-350d-8183-188b1813bb08 | -2.42613 | -46.71505 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bd5e535-347f-3a1b-ac3e-9f623a353bb4 | -2.42611 | -46.71426 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fb2c3c2-9667-36ee-bebc-367746b9c077 | -2.42113 | -46.7143 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 620665db-d485-3ab7-890f-69c7b2e23d5a | -2.4211 | -46.71354 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 066c6bae-b9df-3f37-996a-660cfa573039 | -2.42029 | -46.71996 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a072c33f-c67a-3aeb-a3b8-783fe2351644 | -2.42023 | -46.71917 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9279a015-ff12-39b1-8993-5f6c2a5d5e11 | -2.41612 | -46.71358 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 013a93cb-5c26-302f-bbbf-6b883cb16920 | -2.4161 | -46.71283 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 398b6a7d-9181-32b6-9d00-fc9d97f6fbbe | -2.41285 | -46.7008 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ef317ee-d7fb-3766-98bc-8304b7462bd7 | -2.41278 | -46.7015 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a7a385-acc7-380a-bc5a-cc11b0496fe2 | -2.33467 | -46.64764 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aac81dca-a0f4-30bb-b537-5cc9b0e09b2a | -2.33459 | -46.64244 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8da4e0-40f0-36da-8aa1-dd05bce9997d | -2.33375 | -46.64812 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f4e33cd-1163-3329-97c9-00961eab8ca5 | -2.32575 | -46.50562 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4696b150-1c3f-363d-973c-aae60839e548 | -2.3253 | -46.50855 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6464d1b1-6bf4-3a05-8ff0-c3857247eb18 | -2.32484 | -46.5115 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fd987b-1a10-37df-937c-5ad9b795279d | -2.32068 | -46.50491 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 057ea654-8028-3178-bce9-13e1408c0492 | -2.32023 | -46.50786 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README71.md)
