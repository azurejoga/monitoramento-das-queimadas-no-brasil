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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08045cd8-a4a9-32c4-9a85-eb1b33e40b06 | -13.56635 | -49.04423 | 2026-07-29 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 769cb31b-1e20-3b17-bae2-a8fec3b3d1e7 | -18.53445 | -56.80862 | 2026-07-29 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| efbb6550-4c73-366b-a4d0-6993cca2abd7 | -13.04152 | -46.79652 | 2026-07-29 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9baaef96-294d-39f0-922f-129269c4a39a | -15.4028 | -55.9188 | 2026-07-29 04:34:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eec1040a-6d83-3d75-8f0c-f602df286339 | -19.51512 | -43.5776 | 2026-07-29 04:34:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27f87742-4c96-30c4-a329-a5df27dca42d | -14.20692 | -43.97977 | 2026-07-29 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5138e7b-25c3-3eb7-837b-f006de39d18e | -18.54165 | -56.82078 | 2026-07-29 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7adfaa59-cb84-3813-bb55-fd6b2d619795 | -14.01973 | -53.96642 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| facbb6a9-13c8-3ab7-8f12-ecc5baf37bec | -14.0072 | -53.96408 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af0cd9d9-a588-3560-b0a1-5ce3f1b496fa | -15.43724 | -41.37952 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fb32b992-9208-3a5d-8854-4d5c2784b177 | -14.03502 | -53.9775 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49538789-8fa3-39a9-abce-b539360f205d | -14.00374 | -53.95932 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f8a37e-7cb2-318c-8bb2-f5e468dc427f | -14.03615 | -53.97623 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bae5c2ed-2686-3b50-8261-e692828e8814 | -14.22148 | -44.65943 | 2026-07-29 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f90645cf-05ee-3a8c-9db1-c6f98cfb389c | -15.33115 | -43.02338 | 2026-07-29 04:34:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 644f7e85-8a70-3e0c-9a10-d93fb832aa12 | -14.03542 | -53.98017 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25bad734-1119-3af5-aeb4-b608a530e0d4 | -15.87026 | -43.60036 | 2026-07-29 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df9f2d06-327e-37ec-9b5c-56d3ff510c2a | -14.01137 | -53.96486 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fbe683c-29be-3da9-8b50-499edbb795f4 | -12.32653 | -54.09187 | 2026-07-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c5a0f32-3412-3540-b4ee-df25a4a86359 | -14.1903 | -51.90885 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b70404b-b97e-36a4-a635-ebc7e1702921 | -13.98917 | -53.94447 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60fa7a51-222b-3a9a-8082-05be8bcac365 | -13.31917 | -43.58916 | 2026-07-29 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b36730a-76f2-3e87-b473-721b19844907 | -13.31724 | -43.59148 | 2026-07-29 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdd065c3-99f6-369b-8958-f218d24cc028 | -15.44767 | -41.3752 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 68084a15-0a03-34fe-aa4d-c1acf4f6a71b | -14.06538 | -53.98177 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff3c58d1-f976-3795-ad52-2b3f8c845b22 | -14.19306 | -51.90771 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65c9d2df-67b6-3433-8873-63326db36604 | -18.53703 | -56.81977 | 2026-07-29 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2069ad3e-a21a-3d9d-8ee8-ada4b0556fb2 | -15.10545 | -49.65833 | 2026-07-29 04:34:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1239ec9e-8a7e-38b3-a67e-3d805f9dd48c | -15.44243 | -41.37949 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 299c8bf7-b636-37a8-b4a1-7f4a9d360c45 | -20.01488 | -44.23695 | 2026-07-29 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f4f0a0f-03b7-335a-8cf5-0277f3f27a23 | -14.18569 | -51.90637 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca4e9b39-209b-3d1e-93aa-2ccde8dbc198 | -14.06609 | -53.9779 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa10b415-edf2-370d-9630-6526a44650aa | -14.72931 | -47.13984 | 2026-07-29 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecd992c2-d54b-32d0-a432-6e7f1365ed40 | -14.72092 | -47.1497 | 2026-07-29 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c36a3b33-ac7f-36a2-ac0d-7cc1fa573d92 | -16.14989 | -48.6115 | 2026-07-29 04:34:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfea76bf-e37f-3dad-8f3f-5afe51e2ee70 | -13.98845 | -53.94842 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d86f28f1-38bf-3804-8dfb-78af62f51596 | -14.05575 | -53.96372 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49254b0a-2407-3754-aced-1030e5fce10c | -15.44705 | -41.37999 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ec987f84-fd1b-3233-b0f2-8a9ef039edca | -12.44935 | -47.89023 | 2026-07-29 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48004f75-3caf-3e32-a6f1-c417b55b0756 | -17.72242 | -48.63079 | 2026-07-29 04:34:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5740c7ad-a874-3d40-90b0-8fbd1874812a | -25.17141 | -52.07857 | 2026-07-29 04:36:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2916ec3-d704-324f-b384-0fdbeecebdc4 | -20.30527 | -50.60495 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 9149f3c1-0725-3665-b480-c88ac8a43238 | -20.7925 | -57.87307 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d5ca73ab-2940-3cbe-b10b-db67e038c4c5 | -21.35056 | -44.81684 | 2026-07-29 04:36:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c76e7766-363c-3e6d-aa1d-3e293d333429 | -23.45686 | -46.43797 | 2026-07-29 04:36:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 27ad7344-a4cf-3c0b-8b1c-8ff2f13cc8f7 | -20.59657 | -57.26741 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 778b9c76-c120-3b7a-bbd6-9ee213b0b83b | -20.60509 | -57.24853 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83cc2099-9b1a-3f85-b43f-6ec5d6a4af87 | -20.77938 | -57.86417 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a3e0d7d-6b69-37dd-b24b-daef0fefa370 | -21.29263 | -49.08676 | 2026-07-29 04:36:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59ebe0fb-63de-3918-acac-c05ada48f44f | -23.49202 | -46.22897 | 2026-07-29 04:36:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 741143f4-da50-3c6a-bdd8-ea2f98e20086 | -22.87284 | -43.7542 | 2026-07-29 04:36:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7b1713cc-6229-3022-bcaf-d1f7d1fe4d5b | -21.02243 | -44.57465 | 2026-07-29 04:36:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 818c4372-4b7c-3d11-8060-288d27a404d6 | -23.84661 | -52.85664 | 2026-07-29 04:36:00 | NOAA-20 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7300cf9e-c643-3589-bd15-2b5439f1beec | -20.90844 | -57.48087 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fe81eedf-d8ba-3898-aa1a-e23195b74de0 | -20.78411 | -57.8653 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7914a5fa-97dd-3a25-9c43-99b3d984e537 | -20.62079 | -57.28595 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c109c944-428a-3fc7-a789-87a133f90cfc | -20.9099 | -57.4972 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e252ca29-cb3c-3d27-9cc1-aa21147c7929 | -20.6051 | -57.24592 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bdfe08c-14fb-3a2b-af54-e05f8cadf5bf | -20.59805 | -57.23384 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 083680bc-12f9-363d-8bcc-2622409c833c | -21.02196 | -44.57835 | 2026-07-29 04:36:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c667a188-6849-397e-95e2-4f0a5082d8bc | -21.35246 | -44.81814 | 2026-07-29 04:36:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1abbedb6-ca16-321c-85e5-711ef1541ae2 | -22.47582 | -43.51864 | 2026-07-29 04:36:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54b612fd-92be-34e9-9fb8-98e4008d2d87 | -20.30589 | -50.60123 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 10eb2c21-125e-3a2b-8ee8-1b455b5994b0 | -20.30799 | -50.60929 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 700692e7-1a87-3349-ab75-873c4b38aeba | -20.30466 | -50.60867 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a96c0f55-2331-34b9-8bee-e2edb23fb546 | -20.31255 | -50.60246 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 500398f2-a7e1-324e-a603-d835e4a1ef73 | -20.59855 | -57.25457 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ed00de7-c6e0-39c1-a1b9-4c925f5436b0 | -20.30344 | -50.61613 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a1b7e911-cc1c-39a1-bdf9-79697ecff674 | -20.30738 | -50.61301 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9b9b40e4-a312-3b18-9d16-7f4354661944 | -20.59958 | -57.25226 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f20542d-57e8-335d-b9b6-a91537bcc63b | -21.44687 | -43.79192 | 2026-07-29 04:36:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b29cdd2b-5f12-3174-ab92-a5bf6cd8597a | -20.30921 | -50.60184 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3bcbf427-6832-302a-b2d3-9c6b8ea489d4 | -20.79245 | -57.87297 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a3d21bf9-2648-3caf-a0da-ed9dc20a2c92 | -20.30133 | -50.60807 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ccc062b4-974e-3a03-98f0-57bbe42d6211 | -20.90384 | -57.47979 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b3e7b282-ace1-38b3-be06-5d00c741ace6 | -21.18101 | -49.54937 | 2026-07-29 04:36:00 | NOAA-20 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4556c631-ff2a-312b-a12b-e198ea4b8259 | -23.0997 | -52.67948 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 46571a2d-5deb-393f-84be-51528ccb481e | -23.09627 | -52.67875 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 010d4d9a-51cd-347d-beb4-557b9cc454e8 | -21.19892 | -47.88129 | 2026-07-29 04:36:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b1b23ee-6d93-36f7-a072-5841b9fb8c5b | -20.59098 | -57.27147 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 393203cc-120b-333c-a164-80399cc5d681 | -20.5954 | -57.26979 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7b5662f-d0f3-3782-b918-5ed9fdfebca2 | -21.08104 | -44.00929 | 2026-07-29 04:36:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2aef5b32-dcc3-3b33-89a4-0fde60783dc2 | -20.58978 | -57.27384 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff85dcf2-d0ff-3c4b-b050-d0c1acc3c536 | -20.30072 | -50.61179 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5a6db249-4367-3898-b424-ed321ff0b329 | -23.09746 | -52.68028 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 88823bf5-677d-35e8-a670-c08e0ea39509 | -20.59699 | -57.24128 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe8a6165-6b64-31d7-97ac-f5d2c7d3780a | -22.87667 | -43.75248 | 2026-07-29 04:36:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 41ef5e66-8280-36cf-b175-9034d3a8ee41 | -20.59797 | -57.23639 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1296218c-1f88-312e-9e5f-d60320d85ee2 | -20.30861 | -50.60557 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| d736fd2b-3cb3-3aa5-9f38-f00f180743f4 | -21.4474 | -43.78762 | 2026-07-29 04:36:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cb7703b7-956e-3cfb-8d49-c5e3218b88d9 | -21.35719 | -43.75522 | 2026-07-29 04:36:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a3a34ad5-1cbf-3402-abb0-a3f02ea27eba | -23.099 | -52.68355 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 41c0e259-3f82-3acc-8016-c9759ac56e22 | -20.60206 | -57.26068 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f54951a-4f7a-38ff-81fe-5b0e7eb771c2 | -25.75389 | -49.71342 | 2026-07-29 04:36:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d2c9c93e-f691-3764-a10a-fed2676ee412 | -20.60153 | -57.24242 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f3bb9fe-501e-3946-894f-b53953288b97 | -20.08299 | -49.91999 | 2026-07-29 04:36:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aa6be6e-00ae-3caa-8dc1-3543c4d60bfa | -23.8459 | -52.86071 | 2026-07-29 04:36:00 | NOAA-20 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 370ed5dd-e19c-3e44-ae8f-6211a9402159 | -20.60308 | -57.25577 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4ba4d6c-fbf1-3d62-9e30-6b75b6d9532b | -23.02734 | -52.65332 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f0505123-bec8-321f-b519-50b952758126 | -20.79722 | -57.8742 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README14.md)
