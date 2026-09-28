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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c2b078f-35a4-3835-b455-43af4e0d2d07 | -15.10356 | -53.89538 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7739235d-85ec-370f-88f3-2c398cb23aad | -16.46584 | -41.24677 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 08e72256-b82f-396c-8599-2ef70370fe56 | -15.91383 | -40.98708 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 5b1aed1d-954d-36bc-8769-5dc60025df93 | -15.1041 | -53.89894 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 61f65536-9240-3e54-8cfa-e3f9ad830224 | -12.24006 | -45.05237 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2c252c1-2dd2-3d54-9733-7b27142c24bb | -18.75373 | -46.2231 | 2026-09-28 17:07:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 73bdc7e1-155b-3a4b-8899-290364766200 | -13.67874 | -41.01496 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| cf3a0ef7-914a-3902-9d05-16eebcccbf7d | -15.40848 | -47.93642 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5305b43e-f038-3568-a8a8-f9aec33eb7ea | -14.204 | -44.93843 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7bba9351-94b9-347f-b22a-c2df03185b5a | -14.71875 | -45.57226 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| a197cc02-eede-30c6-81cc-aa3a6da7f75a | -15.0886 | -48.32819 | 2026-09-28 17:07:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2beb9e5b-9d0a-3d06-8311-7524fd2995d7 | -18.78055 | -48.75636 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 0dbbe519-3861-311a-8a3d-3aeaabff9d72 | -16.62925 | -48.47115 | 2026-09-28 17:07:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ab73f7cb-5dd5-378c-a03e-789d60d8572c | -14.49403 | -45.24056 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| af62d89d-09c1-3ad6-8906-1a81f0fa2d6a | -13.17943 | -48.55293 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 747da2da-b8e1-320f-b7b6-3b94422db1a8 | -13.92945 | -47.84879 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e34d3a37-b863-3a3e-ae59-6bf9cd641d5b | -12.96262 | -51.06458 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1c6237e7-aa61-3ae0-8cda-7478338b0c78 | -11.29758 | -43.55671 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 0f2fd538-5ac8-36eb-8927-c21e126d31c8 | -12.7105 | -46.97689 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80f425a2-1ee7-3cf2-a677-5fedef7dbfc7 | -13.96256 | -40.46075 | 2026-09-28 17:07:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e901b393-2dbd-3199-a22f-978dbbebb909 | -12.9682 | -51.07631 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a42938ff-c202-380f-97fb-4c4ab7c7d04c | -15.03368 | -49.5904 | 2026-09-28 17:07:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c090cf31-3a82-3c59-8bd7-24beefd3b659 | -14.32512 | -44.82339 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c2dea2c9-6e61-30f1-ace4-e86a8cba8f86 | -17.1772 | -51.74215 | 2026-09-28 17:07:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b44ccee5-b0d0-370f-bf73-579e2c3248f3 | -13.94782 | -49.13736 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a9fe582-197c-349e-8375-6c54397ad38a | -14.61555 | -49.10318 | 2026-09-28 17:07:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cde86908-4a3b-3173-a99c-3afba9c5edaf | -11.71066 | -43.45789 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| fd117571-4427-3a3a-8ed2-6d7e514a6223 | -13.96948 | -54.01035 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b170b6b6-128f-3081-8241-8f6b8889723b | -14.71633 | -41.86354 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| f5caf015-af13-30e2-9ff0-bba83dce5073 | -14.53214 | -41.16201 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 89c0c3f4-be8c-3fcb-acd6-e56507234385 | -18.02609 | -47.63496 | 2026-09-28 17:07:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33602740-5e7a-3b01-9bdb-743647d30812 | -17.3045 | -44.52296 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 8d0a62f5-474f-34a5-b1d6-689f2dfddd19 | -14.79906 | -42.83596 | 2026-09-28 17:07:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0bfa04e7-2e47-3b3e-8871-10ede1833866 | -12.86788 | -44.81712 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 868532e8-7569-315d-bf22-79018084996f | -16.54763 | -50.51659 | 2026-09-28 17:07:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 597450d0-cb08-346e-8641-02daa5becf73 | -11.69821 | -43.48691 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d9fd467b-b81b-3c5e-96b6-8b317490fc71 | -13.90025 | -53.66632 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fe75266f-e330-35f7-bec4-981804e083bd | -13.25928 | -48.48343 | 2026-09-28 17:07:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7b5d013-fdf7-36e9-8860-2f2ab58831cf | -16.35524 | -42.57051 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 845e0c34-bb8a-318b-add4-c1ae2f3f6bf2 | -12.70045 | -46.97345 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 74b86df9-e368-3c3f-9bff-37a0a73dddff | -14.31812 | -44.82929 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ad9bc31e-eb65-31e2-bc68-69670fa916cd | -14.44527 | -47.76029 | 2026-09-28 17:07:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| a158a236-89ff-3520-8e8c-2271cfc3dc39 | -13.10432 | -48.2029 | 2026-09-28 17:07:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec48c352-3612-3716-b531-80e91bc6f436 | -16.68085 | -51.32345 | 2026-09-28 17:07:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a6d632d4-2016-32d6-b005-a5ad5d82dabf | -16.99593 | -45.47026 | 2026-09-28 17:07:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ee3c195-f2c1-3b76-8819-658843aa1e3c | -13.0413 | -47.00147 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 779fab84-5bc8-38a4-8faf-3a326cb0e7be | -14.64049 | -52.1146 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 73be67fe-98f4-33b0-af9c-998ed809c4de | -13.41184 | -51.34313 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b7096a72-c70e-3db3-9de6-336cae561f0c | -13.14896 | -48.54719 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e413edba-e75b-31cb-bf01-30dd7393bf21 | -13.5584 | -46.36787 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22cddf4f-d45f-3c55-9052-83b77bd03a28 | -18.43638 | -43.95921 | 2026-09-28 17:07:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a004e81b-ac68-37f1-8d17-3610a4584517 | -11.8955 | -47.01569 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 564a1eb3-2b6d-3642-a610-588711439f03 | -14.53512 | -48.3045 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ce856269-2d56-30e6-ad62-5c7d2381c8bc | -17.25817 | -48.28268 | 2026-09-28 17:07:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 66049191-883b-3672-b6d6-0586c887528f | -12.68637 | -47.36929 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| acdd2f1c-ac16-3fae-b0be-adcb7fa44176 | -14.45155 | -40.75296 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 78d8a198-0be9-3fee-ace8-86c24e3d2bed | -15.7832 | -48.16113 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c66d099f-bf6f-3b79-a37b-94c0f9a05c4f | -15.05285 | -54.60259 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7fed8be7-34e9-3ec7-bf86-381e2c267c3e | -18.68188 | -48.61879 | 2026-09-28 17:07:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf22b019-35d0-349a-9345-ff5efd8ad0bb | -18.09739 | -44.3913 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 78353a7c-dce0-3355-bcf6-bfc1d50c27ea | -17.82763 | -44.38818 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 174cd9ff-0585-3df4-9c00-6a054288b462 | -11.39053 | -43.41678 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 74bd9225-ba10-3957-a34a-6eca4e6760ec | -11.32112 | -42.21361 | 2026-09-28 17:07:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 780ba6f9-c7ae-3c07-9c47-8fcd6c7fb322 | -16.25783 | -41.67891 | 2026-09-28 17:07:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| aa389f47-10dc-3f60-b82e-7173bbce60d2 | -14.70823 | -44.65286 | 2026-09-28 17:07:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a075e5b1-e898-3fa1-92f1-0e0ea06d7121 | -17.3296 | -53.95535 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aa0019ec-72fa-3df1-9e90-0c683232e24b | -15.00332 | -47.85601 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc48a7ba-22c1-353b-958c-7fc1a337d581 | -12.51559 | -49.97362 | 2026-09-28 17:07:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d1fe910d-0de3-394b-8292-8b101de07a2e | -11.38298 | -43.40932 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e0c03a3f-ecad-31fe-80af-b5bdec09e4fb | -15.87684 | -42.51051 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ac361e6-1ff6-362d-abc7-043d6753cc6b | -11.70882 | -44.50876 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6da46f01-4011-3227-9d4c-38383ac0c8ee | -12.90161 | -52.04923 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1d6d40ef-0f34-3dee-b1ef-24fb8bd5d3ab | -20.90307 | -57.831 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f72c6034-edb2-39d6-b345-6f10ec351aa6 | -16.06762 | -47.92004 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 46a10714-7ff2-3642-9bef-8493390df5ed | -14.31694 | -44.82305 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cb2257f0-6662-3d9e-b4c4-70de2bdf6532 | -13.3139 | -43.96104 | 2026-09-28 17:07:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 613bfb07-fc0d-3a5c-a3c0-2801d386a753 | -12.82566 | -49.67138 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| bdc638ce-bb65-3107-ba74-e56afd691f38 | -15.75617 | -42.28016 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 565e5685-5fa6-3d99-bf3e-b48fc5b569f3 | -11.67632 | -43.52717 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2a5bcad4-4b17-3ad7-a3b0-e8f7198e6f78 | -14.33682 | -41.38735 | 2026-09-28 17:07:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 0c851769-5872-3fb1-86b9-af95a3d99fef | -15.94291 | -54.96352 | 2026-09-28 17:07:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 773b6b6e-c830-343e-8aff-c4dd3eb409d6 | -12.67873 | -47.35221 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 618e0999-dce6-37f3-bd19-9aef6f45cff4 | -14.32026 | -44.81259 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9fe6f346-db7d-372f-a485-f31851783577 | -13.89024 | -48.11737 | 2026-09-28 17:07:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2ff1d175-e24a-3b26-88b1-e91be9f09c8e | -14.72472 | -41.59819 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 156.0 |
| 506a9fce-0236-3401-a756-bc778b8c0d35 | -11.90095 | -47.01964 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e9f67b1a-f236-3c89-aefa-687a48b18cda | -16.11592 | -41.60942 | 2026-09-28 17:07:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 46fc03d4-e4e1-3064-83b4-19e350744085 | -16.54695 | -50.51256 | 2026-09-28 17:07:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7dbd79b8-b6a6-30a6-b8a9-13282dab7dcb | -15.23155 | -50.49154 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d9f7f23-46c0-3f16-8057-d264f193c0ed | -18.395 | -43.43387 | 2026-09-28 17:07:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 746c5245-1a08-3722-8f78-48b4618cc1ef | -15.07626 | -54.59904 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| cbfe6afa-e970-32e1-aef0-075f7674dcfd | -15.06611 | -54.62293 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 70bf6027-dc96-3616-9e00-db12b86908f7 | -18.12866 | -47.55342 | 2026-09-28 17:07:00 | NOAA-21 | DAVINÓPOLIS | GOIÁS | Brasil | 5206909 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96f579d2-74cf-3651-8302-ff7208a87195 | -12.65122 | -47.35257 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 2957b498-3b9d-35f0-a86f-7bd9b8aec8ea | -14.31871 | -44.83241 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 4cdbc657-6df0-3304-abe4-45d22f2de4fa | -25.27113 | -54.2151 | 2026-09-28 17:07:00 | NOAA-21 | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d35d71c8-1af6-3bad-9a80-0659852ab743 | -12.68326 | -45.01587 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1c8a5c31-72ae-3788-ac71-b61dcd38c914 | -15.73836 | -46.02763 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 5dc90208-a048-3576-bd7e-9543cea41edd | -18.55795 | -48.39955 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0c573fc2-87f3-3e4e-ba16-d69c6bbe42cd | -20.83636 | -57.78689 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README138.md)
