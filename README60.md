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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecfc19ba-a963-3e08-9469-f2ccc854f310 | -14.75041 | -54.67383 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57e9ec2a-412c-3825-a3ee-435b56704fc8 | -11.79568 | -45.01669 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6044d965-ab3f-31a1-8a9f-d2ee02f9e81c | -11.80537 | -46.83863 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39043d91-657b-3c0f-81d3-67d29e3e7948 | -15.42248 | -50.20237 | 2025-10-05 03:55:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3dec1ac-ffa0-36c2-ab5f-1b123fa7c184 | -10.83761 | -47.19173 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee917f75-a523-3599-8343-37725804fec4 | -10.68356 | -49.27687 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d52f4677-a23b-3e05-9a0e-169825fb6916 | -15.52444 | -46.87548 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01888dcd-1625-3aff-949c-896e59749549 | -14.74663 | -54.65759 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58f2a882-cb95-3411-80d7-78598c82bcfc | -14.31492 | -47.69188 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64635e6c-3ba5-3c14-aadf-43722959f3b6 | -14.88048 | -48.14414 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3776da02-ff05-3752-92ae-d947c88fe8a8 | -17.01829 | -43.45646 | 2025-10-05 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9a41b310-f061-3006-a7e5-a6718533e7c1 | -14.446 | -46.09869 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbcc0221-07d9-32a3-9551-c2f0c1ba0f56 | -12.39622 | -44.83229 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 213c8764-aff4-3aa0-9abc-4a42aa83cf30 | -10.79536 | -51.00983 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| adfd3d48-a11e-327e-9078-ee2ffdfec1d7 | -12.81464 | -46.8502 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2266072b-3727-39b4-8f9c-6d3bb75174cd | -11.52865 | -47.2338 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f01751-a65a-3b7c-929c-badd0d9ecfa3 | -13.31571 | -48.08255 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eecbfbff-a5aa-3357-af27-11961840cfdc | -16.38012 | -52.16642 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7011aad8-95eb-3df8-ba13-13a92f674cc8 | -12.11984 | -50.9119 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13d3fc3a-02d3-34cd-be77-8803ca901545 | -16.34839 | -51.48203 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b49a132b-ae7a-3671-995a-774b94b8811d | -15.96586 | -43.32785 | 2025-10-05 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c45f11da-2dd9-3080-92c3-affbdeb7a3cd | -14.27063 | -45.87088 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 718807ab-8106-3387-9767-76c452ff8617 | -13.57199 | -48.17205 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33970069-3dde-3a62-808a-53fc700acacf | -10.94282 | -47.07184 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7c71133a-2176-352f-b0dd-5834f9385e3b | -13.24435 | -48.47526 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cffd278-4da7-37d5-9a93-8890fd38447e | -15.54937 | -46.83945 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c53191e2-e25e-32ad-a84e-8d0195d3d3a6 | -15.29049 | -47.33556 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad5ce1b4-5979-36e7-87e1-9af90c0e2d3e | -12.91534 | -47.30958 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9b55899-3953-3528-83a1-ef83f0acbf71 | -15.68956 | -46.27455 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c06bca2-32f9-396c-877f-fd0023482902 | -11.83278 | -45.05933 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65c8d7ba-dfc9-392f-988c-eb1e3a0de798 | -13.97049 | -48.11996 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 287d0814-7053-3556-abdb-cfc3c7e92f4a | -11.13017 | -47.89935 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21f6442e-524a-3215-bc92-b5452f64c8f3 | -14.16498 | -44.68308 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac2b9c2f-e543-3db3-9c21-d438ad2114bb | -15.55186 | -46.85033 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d17761bd-8649-386c-a309-b8a1cf870253 | -13.30402 | -48.11625 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15aded2e-7139-341d-999e-dabe7db6d261 | -13.81901 | -43.1708 | 2025-10-05 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42c69193-45d6-3df7-9c21-862dfa7af63a | -11.11454 | -47.20779 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35b259bc-a8d3-35b4-aa35-54d932488552 | -14.6741 | -49.61237 | 2025-10-05 03:55:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63e05526-a529-30dc-9d36-56328aa4a499 | -13.3519 | -47.58952 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46773cf5-0bb3-3cc4-b1b5-75dd53ea2885 | -10.032 | -50.40958 | 2025-10-05 03:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b67434e3-15a2-337b-80c2-19e89d86d435 | -13.03514 | -44.93372 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2afc309c-b8c0-3d46-b376-aa527880a95e | -13.28892 | -47.58364 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96c1e6f0-89b7-3314-9af5-04ee6857c96a | -11.46077 | -51.52174 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df1b9680-f636-3990-a06f-fafe1e5391b7 | -15.13705 | -45.74481 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecfb4f94-05ad-341a-8dab-8ec6903afe2d | -15.58107 | -52.49974 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cd49f87-6bd8-3a15-9554-ea867f6082fd | -15.30191 | -47.95866 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2335bf5b-c5ed-39a2-9cb3-f1e263b0fc9b | -11.48248 | -44.96919 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e54b1d81-687e-34ff-8788-fc5bbed48dc3 | -11.68821 | -45.28307 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac0e705f-07e0-35b7-b68f-5ace84b8a8f4 | -11.40821 | -47.16524 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 935e7a31-e616-339f-b502-d1b7a6f59eab | -11.70868 | -47.51073 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94bd871d-0a95-3b48-9697-dd9962dd57be | -12.97581 | -51.04304 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 602a4171-6005-34d2-a85a-0d2f95ae7127 | -11.49948 | -44.97877 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c311e7d7-f850-35c3-bf75-0cd1d8dd1a5d | -13.56704 | -48.17114 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9726ffb4-9fd4-3d37-8db6-eabcb12c752a | -16.01316 | -50.95964 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d408969-fd2c-36cb-a98b-8032a38e79d9 | -11.05968 | -47.77959 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b868700-32d5-3ed7-93a6-24ad40072493 | -10.5727 | -48.71557 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19855b83-e0c5-31db-873e-5d13766da448 | -14.87841 | -48.15489 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9291fc6b-9073-3524-9c73-4a9b02f176e4 | -16.38621 | -52.16283 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 999bd41f-d0e9-34d0-9138-8bffe5469eb6 | -13.73353 | -51.28069 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e95daff-b03f-348c-9124-583a04f6084d | -13.34448 | -47.78805 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f89b090d-52b0-384f-aafa-3c4c7a450887 | -11.50153 | -44.9912 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eec787ff-328d-3bc0-ac14-e0c2fc6199dc | -11.71222 | -45.34424 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f1c21e4-7ec3-3d30-95a6-56352751763d | -11.90898 | -46.23394 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1403b28-3d9d-3220-9913-fdaf8069334a | -16.38735 | -52.16225 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68b6a62d-211d-3a60-a08e-94538397500e | -11.75568 | -44.74 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 138d1620-fac7-342a-a01d-f38a0a8beeea | -11.54491 | -47.69283 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee3b15f3-9e4d-3547-9dee-7b7b92b1dd38 | -14.87793 | -48.26193 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 937f9b35-8c56-3327-8024-e5e1af5aa9ae | -15.98156 | -50.91426 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 291a17eb-4e4d-34c6-9874-f30b26cb56bc | -14.95257 | -46.85224 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5d2113c-5bcf-359c-883b-934f60fd13c5 | -13.22956 | -47.82193 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3317f76e-e5e8-383e-9927-8cf673c668c0 | -15.13639 | -45.72495 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b32a03b2-0703-3d27-971d-f6c486886e02 | -12.12112 | -49.42916 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 472a2548-0723-35a9-8822-94cca677880d | -17.11443 | -48.92772 | 2025-10-05 03:55:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24ded84f-29df-3edc-9012-804a79255280 | -13.48397 | -47.23338 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9df8cf53-c700-3d45-a125-797b7b861823 | -14.60785 | -46.7356 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f2aca95-5c76-3809-bcf6-53903c9ea20f | -10.3551 | -48.16756 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35767763-5033-389d-88a4-ff2a148fa628 | -12.10398 | -50.89202 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5550e47c-06bb-332d-817f-1d0ee1060365 | -13.10738 | -47.86878 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d23bc5e-dc2d-30ba-8216-25267343026f | -13.29749 | -48.09712 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a765fd90-070a-39d3-9b0b-466e023e011c | -11.91178 | -46.24382 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36785897-a74d-35ce-b459-46c968a2ea13 | -11.80077 | -46.83743 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12f685d3-e969-372e-beba-96b94c690a27 | -15.98517 | -46.60167 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b950c8b-4361-322c-be88-559aca7fb78f | -11.4835 | -44.9724 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb3fd9b-9b01-3038-b21d-36fdbff7b44a | -11.91019 | -46.24116 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a58d3ca7-a5f1-3f72-979c-9cf9e608945a | -15.75096 | -46.27305 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a31ee4-f09d-34a6-ac74-54d76c84d926 | -12.89833 | -47.32226 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56104e10-07ee-350a-b30b-5782a9b0fcb4 | -11.8267 | -45.06933 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7002b9dc-d5d7-3859-bda4-0d877a482932 | -12.11476 | -50.90598 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 997c3c2c-86ca-3056-9981-31765bcaf0cc | -16.39446 | -52.15364 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1835902e-91ea-39f1-ad9d-a2dd51d1f579 | -13.08133 | -47.89928 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fcd63de-703f-39ce-a7df-481d74c00c16 | -15.38614 | -47.95354 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 665435c4-56de-3db5-9d19-9300a0d3a4f3 | -15.54374 | -46.82132 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35d62e23-d28b-3352-b58f-6c81c8464e33 | -11.10771 | -47.87909 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4008e9db-27e1-387c-a6f2-ccfb43702da8 | -11.06984 | -47.6964 | 2025-10-05 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c6573cf-786f-32ac-9f64-a88d30fefa1c | -11.70964 | -44.30554 | 2025-10-05 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd7b6e9e-7ba2-31ab-9d0b-1d30f5f9c4b9 | -13.3791 | -47.54999 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| de970f68-4854-3abd-96fe-b2de59c6c535 | -10.6816 | -49.27541 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8645be65-25f6-396a-baf4-f2fa02efcfb5 | -15.9805 | -50.90704 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62e0a3f7-a3c8-3b4b-b9d1-d4a5ebf1ba4b | -14.73926 | -54.65707 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b07607d-19dd-30a5-b4e8-654df0a9057d | -12.57119 | -48.16484 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README61.md)
