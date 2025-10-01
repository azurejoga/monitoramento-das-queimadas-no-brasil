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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 114b5c86-f822-3a9e-99e7-3fdebfefcbd7 | -14.90507 | -48.12595 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50935c38-a12f-3f12-80c3-e832c862bb0c | -13.79215 | -51.23753 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5394dc7f-f6ac-35fa-a0ee-cc2c47231844 | -17.86054 | -47.14952 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ae47c3f-6ea9-3464-ac91-27237cb09ef8 | -13.97897 | -45.0673 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 457e01d1-3e37-3c3d-9b01-e0c9e2ced3cd | -17.90253 | -57.57888 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6eaad4cd-c3af-3a3c-aea7-c0520c8e9b3b | -14.35248 | -45.93261 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 15a6f0c8-52d9-3246-baa0-04804f1a8254 | -12.82254 | -56.55491 | 2025-10-01 05:12:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f3d3637-622c-3588-9829-47c035eb71b9 | -14.43962 | -46.3642 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c185f794-6406-34a9-9cfa-fb7eb916a319 | -14.5042 | -48.48885 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc21b057-2e47-3914-8dbf-6042e041104d | -14.7016 | -48.13173 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9167a59a-b614-3f6a-8064-2976b9f9cafa | -14.49727 | -48.44552 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68c93dc3-5bb6-37c2-a92f-33de734db3e2 | -13.94401 | -48.12271 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa614356-5cb2-3239-b82e-5f97321d83b9 | -13.70262 | -48.65021 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e17c94f9-54d7-34af-9dee-0320f3e590db | -13.76166 | -47.96476 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d61ff000-3008-3e6d-b193-0839a203cd3f | -13.98736 | -44.90897 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 433a6575-68e1-3cf0-b6ed-b41e1d2f6111 | -15.33913 | -46.28173 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20fef370-7c38-3e5e-8e94-73f9035c09fd | -18.96845 | -47.87564 | 2025-10-01 05:12:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 246ebdbb-40a0-3734-ac85-3aa1fc24a967 | -14.75416 | -45.76393 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08f47698-242f-3073-ae8e-23ce883858a7 | -13.77506 | -48.32393 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 709ad5bb-2723-3d49-aecf-4870beff896f | -13.78323 | -51.23092 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27c9a371-bae6-3df5-adc5-77f09f35d333 | -14.05673 | -45.04847 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 42f550f8-e2fa-3e48-bb00-a5ddeb1cdec7 | -13.82396 | -47.50635 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9b41fe5-ea03-3b28-b457-9d6fd5f8acb2 | -14.89644 | -48.1173 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 216ca087-7b8f-392c-9a49-bfe69dc53f0f | -15.85522 | -59.59611 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f690ab-5ede-3bb9-9af1-310399c3c285 | -13.80674 | -47.49373 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33d65360-c544-3416-bcdc-0a3778b281d7 | -14.90053 | -47.21489 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca814f64-6549-322d-8ad8-589c2524865b | -15.47994 | -48.54691 | 2025-10-01 05:12:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa3a6827-4530-30ac-9b57-c119c80699b3 | -14.17413 | -46.11792 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be4ec507-779e-3da9-9ad5-286e09910cac | -15.23998 | -49.72467 | 2025-10-01 05:12:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaea7db0-bae4-3b4c-bb2c-3ea6a67848d9 | -15.33644 | -46.28072 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dc2367d2-5f07-3c14-a468-0a9568f508cc | -13.66764 | -48.07338 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55dd3ad3-9043-3231-87e6-ed1bc0e66866 | -13.76533 | -47.95692 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3410e2fb-ab5d-3504-8ca2-2f961329dfd7 | -15.24041 | -48.75107 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a6577c67-5665-31b9-8fb2-a208a5602b88 | -14.98379 | -50.75897 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28c4c45a-9b77-3042-9954-c98faf99cc31 | -14.14805 | -49.20543 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e4b260-239a-3fd0-bb32-153a7784afa7 | -15.31289 | -46.41065 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 237cc6a1-81f3-34b6-a202-cfae42550851 | -16.37332 | -47.0477 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f873e9ba-6e52-3df7-a4c7-f114cd98c6a2 | -15.61155 | -46.91187 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 711499ca-f6f8-3ca6-9f38-58956610cd6c | -13.78735 | -51.23689 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a58bf7a5-532c-3d35-acb8-934de2106042 | -13.9399 | -48.12234 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5bb473c5-71b7-3e69-88a3-6e150d599ddd | -13.98339 | -44.92065 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de083661-aaf2-31df-aa78-7cc834609e06 | -14.68497 | -48.23048 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac73ecf3-db30-3620-9949-dd90bd0ac645 | -17.3988 | -47.17035 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fa6e149-fef0-3642-bff7-040587264383 | -14.88727 | -48.12253 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33717312-010e-3549-9667-47405e91449b | -15.31607 | -46.41012 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d70dfeb8-c03a-369c-b3cd-dc3ea0c6749f | -14.9212 | -47.81728 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 597a404f-c715-37cc-a3f7-6b60003155be | -14.81506 | -59.70797 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9533e453-dbbd-3f55-9621-5ef3a69d5e3f | -14.81117 | -59.711 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 936f4060-c612-377b-98ac-da4e1a413795 | -13.69774 | -48.64221 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02ec7507-da84-3615-b213-3a293b84cc76 | -14.51001 | -48.48964 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e66189b-e5f2-3269-826d-e473cc510caa | -13.82421 | -47.50488 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 336fcc8c-c5dd-3e05-87db-3d8c60d70941 | -14.35121 | -45.94486 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 04cbab84-1375-3d80-83f9-a795ca8285ad | -13.78933 | -47.98752 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b96646c-dd4e-3b75-a8f4-9cb346dae7ca | -14.51779 | -53.12577 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4addf4e-7393-31ff-97b3-c492f0441c3d | -15.16193 | -49.08859 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36d936dd-1a1c-3e2e-9744-28944d7990de | -13.7695 | -51.22369 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 442645b3-1e56-3165-8201-ff0a62499c6f | -14.70802 | -48.12825 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14972007-b2aa-3721-b672-9d5e3204eca3 | -16.37926 | -47.05229 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eef8f34e-4ce2-3afd-931b-60989ada9de3 | -16.06168 | -51.01375 | 2025-10-01 05:12:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c22fc14-9982-3867-a360-bc6d57770640 | -13.71357 | -48.65553 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3173bc3-87d0-3416-9495-cc57a2593515 | -17.89849 | -57.58229 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 9f50845c-fc75-38e2-b79d-08304d655191 | -14.75279 | -45.77695 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12a55773-ee0e-3799-a5b3-eeef90d5c1cf | -15.0063 | -56.03815 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662646b3-9264-3aca-bdd6-97a438389ec4 | -15.92433 | -48.14304 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c15311f-6bdf-3b38-a58c-b923d776ab37 | -15.48825 | -45.9003 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 80c8a9e1-fd87-3ad0-81bf-c515d4437de2 | -14.50021 | -48.41927 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d92b90d-afb5-3acd-9820-b3e94b228d5b | -15.27676 | -56.79031 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 390918a5-1d28-332a-96d8-f6082495d095 | -13.81784 | -47.5055 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 811bc32d-d537-326a-a422-85367cd78e46 | -18.712 | -49.17132 | 2025-10-01 05:12:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75a3eba2-1828-3e7d-b6e2-c7f355199e1d | -14.7135 | -48.1335 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68e88bb8-ff9c-37e0-949d-1e8e994c47b9 | -13.29129 | -50.6597 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbcc89b6-07a2-3b17-a4b4-08a538343a7a | -15.16061 | -49.1003 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a52c6476-eb03-3242-b4c6-9aa96c0c604e | -13.66462 | -48.04679 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01e1374a-9096-35f3-adc0-3c0e460f1ce3 | -15.84476 | -59.59791 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c920266-5581-35e5-b6bb-375f9811f339 | -13.76537 | -48.40807 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6240ccd-129b-3af2-aa35-cc9ff755a7c5 | -14.7082 | -49.14479 | 2025-10-01 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12d25ea1-bd50-3f48-82cc-975bad5bed99 | -14.89471 | -48.13375 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5703b07-dfa6-308a-876e-b78a2a6f5e40 | -14.79335 | -60.19888 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45cb703f-1f3c-361c-b320-4b4bf49bd6c7 | -15.24164 | -48.74014 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fcb6b7d-cf9e-3ac8-a502-94b61c710cdd | -15.25749 | -56.84837 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0cf8482-5dcc-3bf7-9834-fae81bca0bce | -13.72134 | -54.71877 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86fcde6e-0179-3202-a3b0-58f6e572a0be | -14.68008 | -48.24201 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0e4f36-245a-337f-8f1c-67dec6e25332 | -15.49331 | -45.91987 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e707d77-bf84-30a8-9d41-d5ef8f8bbb95 | -16.02527 | -50.88898 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e255b06a-c510-3296-b05b-faa7a60cfba6 | -15.30229 | -56.79291 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17165330-e3a2-31e4-a56d-34fea9f175a6 | -15.29198 | -56.78421 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3e5bbbe-05b4-383a-b866-83cf5e2d4349 | -16.7639 | -51.34601 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80c03978-07d1-323e-b237-87928a85d52d | -13.94652 | -48.11698 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb317d2c-08d7-3eaa-8101-fb54532efb61 | -14.02168 | -46.31807 | 2025-10-01 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84b12e89-fe5f-3f3c-bd3c-bab6f8b6272e | -13.9444 | -48.11919 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 108342e1-11e9-37b2-96a4-a7e371e44131 | -15.17404 | -49.08268 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac1ffdd1-6a7e-3698-a0c9-8d34f7bcc24a | -15.23464 | -48.7503 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da4e5341-7ae8-34dd-98cd-35155687d908 | -14.81621 | -59.70076 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1a3f50e-0f29-3184-a1b3-2e700df36c13 | -13.77773 | -47.9833 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a6f6f722-1c8d-3c45-9485-f2b92a7f179c | -14.0277 | -46.32475 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83948d55-216a-3828-a5c5-ce4ca1f7c3f8 | -13.67452 | -48.06557 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a8a2233-df25-379a-8f60-533eb50dac68 | -14.96354 | -46.88329 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c14c2347-d39e-3d86-90f4-446f626f6d52 | -15.87872 | -54.23588 | 2025-10-01 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93efe27e-8127-36d4-b434-43318fa69c79 | -17.41163 | -47.17122 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbd17521-911c-397a-8328-ccde525e3ea6 | -14.69782 | -48.22281 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README131.md)
