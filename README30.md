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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 805cc0bf-0129-3e1f-923a-5e0b9997988a | -18.40316 | -45.20178 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff49ac77-17c4-3e40-9f24-999ef39ddfbc | -18.25318 | -45.46045 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e810e2c9-154e-3768-bf60-60669ac34db5 | -18.02306 | -44.94452 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90131af6-a4d1-3b83-93d7-6108592d8069 | -17.28316 | -42.64808 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 39fe527e-5e75-3678-b390-314cce258dc5 | -17.99868 | -44.98603 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee46f895-270c-369f-be5e-32d490615865 | -22.30299 | -49.92897 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48e6cfa0-1527-31f8-aa45-bbab5c7165d4 | -18.04639 | -43.14957 | 2025-10-08 03:51:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a3cffaee-e7a8-33c0-be87-aad1909351c4 | -15.99474 | -50.97084 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 265c74c5-2afb-310a-95f4-3cf617abb7b1 | -16.33908 | -47.04995 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8253e92-d2d9-3bce-80ae-e62c2025a2ac | -20.30053 | -48.51696 | 2025-10-08 03:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 582281f0-acfe-3c37-824b-0634ac07d701 | -16.71877 | -47.60086 | 2025-10-08 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 482d6f64-3a86-3d8d-baa6-2701e4a47d7f | -18.82945 | -41.75317 | 2025-10-08 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ab57545-f65c-3309-97db-31e9ed1d6762 | -18.46092 | -42.52648 | 2025-10-08 03:51:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 825b2fbe-d3e9-3cad-82bf-959290af10ff | -17.9671 | -48.55415 | 2025-10-08 03:51:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ffc448b-07a7-3fdd-b0f3-cbb1f4cdec94 | -18.54959 | -43.24222 | 2025-10-08 03:51:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb9a76fc-d7fa-330a-9712-8f9178aaa015 | -18.10142 | -44.70278 | 2025-10-08 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec2766de-ea34-3c4d-9ac7-058f4e601dd8 | -18.41874 | -45.20908 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d0657e2-3a9d-38d7-99f4-2369c07614f0 | -19.30591 | -43.76066 | 2025-10-08 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2a26c01-fe71-3bf5-b4e7-ec17f9904e15 | -16.15816 | -45.12596 | 2025-10-08 03:51:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec463d4e-3c93-3641-85bf-f247675642ce | -17.98313 | -44.97899 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed8a104d-7aac-3048-97ff-b76aa73ae854 | -22.39294 | -50.01931 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| adc0bc10-9f0c-3657-a560-df6db1979d05 | -21.04325 | -45.67567 | 2025-10-08 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f15a5d2e-c148-366b-9f88-b04b41586534 | -17.96774 | -48.55107 | 2025-10-08 03:51:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b74bcd65-873e-338d-95f1-b94f9b4ad88d | -17.24313 | -46.93984 | 2025-10-08 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0f1ae79-9ea0-386e-87cf-f18d31c9ddeb | -16.1317 | -47.90682 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0ba3d26-1d99-34c6-af19-41d9ee999126 | -20.40584 | -43.6714 | 2025-10-08 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 09d8ca4b-a18d-3e56-a50e-0ba516d1612b | -20.18825 | -43.93864 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 612b3278-cfc0-31a8-b49a-d37588572ce6 | -16.13299 | -47.91064 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 047ffa30-962c-3519-a455-d4e8d4e873c0 | -19.39625 | -44.39109 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ec4d68f-f306-319a-b94c-a2538c287680 | -17.38414 | -45.05988 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a7543f4-cf0a-312d-a5ab-ca8503dd74e9 | -18.41058 | -45.2074 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dc144379-41be-3058-b0ee-c6e0c37faaeb | -19.5809 | -44.73399 | 2025-10-08 03:51:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 54d7d39a-268b-3bc5-a89f-072b64bedfb7 | -17.27159 | -42.65049 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 123a9681-f3b8-3cd5-93b9-dc8736ee6aa0 | -18.35628 | -42.39377 | 2025-10-08 03:51:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b29a148-8557-3f5b-8353-8e8d1e2efed6 | -18.2992 | -45.44549 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5aa16b28-32f7-355e-b484-74cd0e7fdc46 | -20.49894 | -45.94753 | 2025-10-08 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be1e46e5-fbdc-3fe9-abc1-e3b2c3db3b71 | -15.20184 | -49.76094 | 2025-10-08 03:51:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6394054d-5b92-380a-a383-74091dd2d23b | -16.66808 | -43.9351 | 2025-10-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 646789a2-1eda-36a7-934d-d3429c5a48e4 | -16.7618 | -43.97598 | 2025-10-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deecc616-1f51-38a2-9465-89d0f714a935 | -21.72635 | -46.99581 | 2025-10-08 03:51:00 | NOAA-21 | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 73ddd9bc-a575-3135-8e7f-34be49d90cbf | -17.38003 | -45.05896 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8eb9fed2-fa3e-38b3-9d4a-6782e8e16860 | -17.51264 | -45.00199 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e85945-cf5c-3a60-9bb8-a24ce9ef9dbc | -16.72 | -47.59487 | 2025-10-08 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 27c0d338-3841-3ae4-97fa-9a3e38f99794 | -19.77187 | -44.10201 | 2025-10-08 03:51:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31851a85-deb8-3ec2-8eb1-f87c69fd1915 | -16.18744 | -43.66598 | 2025-10-08 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8ec34d3-118d-33fb-9e67-e9109094a93a | -17.35939 | -45.05502 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49edf153-7ebb-39ea-8b50-71445a545c02 | -16.59388 | -42.89068 | 2025-10-08 03:51:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 018c6274-e288-3512-848c-e3d7a53566c7 | -21.16083 | -45.62678 | 2025-10-08 03:51:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9eb56b4-f40f-372e-b5a5-dd05e6505c99 | -20.29081 | -48.51479 | 2025-10-08 03:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c494d28f-7b07-3b04-89f2-4e0f927f17a9 | -19.71687 | -43.90639 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ab7e927-9e4f-32ed-846d-223cce9642d5 | -18.03237 | -44.96208 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b6b5625-5076-30a8-9710-ef57bc454dd8 | -15.35504 | -47.3289 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8f61a8c-2863-30a7-8d54-39cd1ed42fc7 | -17.55798 | -46.06703 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb9ec79e-8d97-3886-9856-516de708a926 | -18.45289 | -42.91169 | 2025-10-08 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4800ba4e-a8c8-3c9c-aca7-41d8258e4c4c | -17.13707 | -43.46035 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 447a3754-ca7b-32ad-814c-94fdd281a1eb | -20.20881 | -43.90933 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 29943c12-5148-31d6-b791-43663fea425b | -15.38875 | -46.28102 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9c2d4a4-63bb-30d7-ad1f-4633501f2a3c | -15.37095 | -47.32652 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b6cb99e-d979-38dc-8923-2d82fa94ea7a | -19.33437 | -46.04462 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5294e9da-0c98-38b0-88dd-1adba9106402 | -19.30881 | -43.76599 | 2025-10-08 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 41309a9b-2f40-3bae-b4f4-8daa6c8facfa | -15.37161 | -47.32306 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f99371f-adcd-364e-8f53-408dc397e261 | -21.90017 | -44.89175 | 2025-10-08 03:51:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 561e3587-bf5e-3efc-92a1-65980aa93f8d | -20.39453 | -43.06725 | 2025-10-08 03:51:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3601b31e-8785-371c-af42-d9883a8caa5d | -22.3981 | -50.02033 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6bebc2b-cfd6-331f-9ea2-49e684184d38 | -17.48714 | -43.33235 | 2025-10-08 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 804957cf-77fe-3b6e-862c-566402c4a566 | -20.265 | -43.63723 | 2025-10-08 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 82ec607c-1af4-3b7e-b15f-8ffcfc137df5 | -16.71861 | -47.59324 | 2025-10-08 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2f11aae-be15-31e7-a8ae-ea1cdbadd593 | -16.13613 | -47.91099 | 2025-10-08 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b2cb3ba-4aaa-38da-bafe-8faeeb8f1dda | -19.33517 | -46.04056 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49a59029-81c6-3fab-a424-10683cebede1 | -17.29038 | -42.64931 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 786b4668-809c-3e6e-a41f-9a127fcb9e63 | -17.28743 | -46.91133 | 2025-10-08 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acd30c64-b1d4-3f53-8961-b0c3cc2cbcd9 | -15.79854 | -46.24559 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a14764b-8fb2-3348-85ae-38ca472ffebe | -19.9755 | -43.21152 | 2025-10-08 03:51:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 75715bb8-1609-31b8-bc71-4fc4a5d0ba38 | -18.05156 | -44.46872 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ad0bb6a-7442-35f6-85ff-90eadd1ac31b | -23.14797 | -47.66862 | 2025-10-08 03:53:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7698945f-f709-37cf-81b0-2776361fedb2 | -11.1642 | -54.9007 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d8c3f046-4139-3e9e-bd02-d52100f5c590 | -11.1455 | -54.882 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| af04c96b-62b7-392b-83d8-8126369595f6 | -17.8417 | -57.6254 | 2025-10-08 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| e4acd24b-e079-31a1-9085-e3535a57fe83 | -11.7466 | -50.9342 | 2025-10-08 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 6557af89-151a-36bd-8336-719cd92fcc00 | -5.1414 | -44.967 | 2025-10-08 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1102df17-91f5-31b2-a978-d8448327a45f | -11.1646 | -54.86 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f01b8129-f1bf-3a40-b1c3-1e7cbfa06aca | -11.1833 | -54.8787 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| b9e46021-6348-3c26-83af-3ed741b5f528 | -11.7275 | -50.9363 | 2025-10-08 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c1b1744d-9922-327a-aefb-89492f4b4d03 | -11.183 | -54.8991 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 73d787b7-0cce-37b4-b9c6-30a39d8016e3 | -11.7272 | -50.9577 | 2025-10-08 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9e356b47-040d-3d73-84c7-11bedaa62046 | -7.017 | -42.8762 | 2025-10-08 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 3ec0c6f4-2f6e-3443-a162-7c6e325d1c52 | -7.0167 | -42.8998 | 2025-10-08 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| da06ebd6-bf17-36a9-bae5-d114db513070 | -11.1644 | -54.8804 | 2025-10-08 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d9aa3119-47c3-3525-b479-6b6bb48b9c51 | -17.8413 | -57.6459 | 2025-10-08 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| ae94858d-8759-36eb-bb3f-fdb285a51bba | -5.1414 | -44.967 | 2025-10-08 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3b8cbeed-d0ea-3cc3-8f86-05df60b3256b | -11.7272 | -50.9577 | 2025-10-08 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9d295b6d-31ba-37a3-a483-5ee7831a520b | -11.7466 | -50.9342 | 2025-10-08 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 87ab3382-041d-3f10-862d-409e93ce8d22 | -17.8413 | -57.6459 | 2025-10-08 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 3dfa79e5-c91a-30c9-bfa9-81092644b2fd | -11.7462 | -50.9555 | 2025-10-08 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 77f81beb-c7ec-3451-909c-3f84b1482dad | -11.7275 | -50.9363 | 2025-10-08 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6da6bd59-bd87-3f80-9f62-d541f780b7a1 | -7.017 | -42.8762 | 2025-10-08 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 3c8e5dfc-fd0d-3cd2-bbd1-ed158d548c5d | -10.24361 | -52.69756 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbb9f19e-5efd-35ef-b015-21bf49842930 | -11.26114 | -47.61983 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdbe73a8-7f42-3b1b-ab59-b7b2e6a499ad | -13.23556 | -47.79029 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15d7206b-0829-3d0c-83c6-873816c92313 | -11.73209 | -50.96031 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
