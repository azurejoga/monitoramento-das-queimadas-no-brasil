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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b78432-16f3-3f35-bdb5-08a5ae9f3b96 | -2.61692 | -54.22513 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab800402-1117-3523-bb26-2944a6d43bca | -6.0327 | -42.52102 | 2024-12-11 04:33:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0087d4a3-503a-3bf9-b083-ae93185c293c | -2.61461 | -54.23902 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 807b4a59-4c53-3e33-8cb2-f05e55985cc0 | -3.34273 | -53.06749 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70b41144-c686-3374-9288-0239479a7f57 | -6.96278 | -42.98949 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8a573651-790a-3e05-a6c7-01410f09ed8c | -1.47005 | -55.3923 | 2024-12-11 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb45c644-0671-32a9-a65b-1341fe09bfca | -6.95818 | -42.99247 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8ba1bb66-e414-3331-892e-fe0a2eb238bd | -1.46956 | -55.39528 | 2024-12-11 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dcf51df-a583-3f9a-9659-259ac29700ee | -6.95162 | -42.98032 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db702cee-9af0-336a-8e4a-de34e763598b | -9.33295 | -40.32907 | 2024-12-11 04:33:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6aabf593-f10e-3020-8258-3ef37ff6e3ff | -6.12916 | -42.5421 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 5bda13ad-d8b2-3e0f-a282-522315259c67 | -6.9014 | -43.51414 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bf0ef38a-9ea6-3a42-866a-680fb3b7cd2d | -6.96846 | -42.97922 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c692843-fbf6-3a77-952e-1e50c3659f69 | -6.90676 | -43.5047 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c824a33-4e68-3af3-b87b-47da632a22e2 | -3.34151 | -53.07516 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8dae5f-2c21-38e2-b9da-0676c740087d | -5.29022 | -44.91232 | 2024-12-11 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2296a946-39d3-3794-b570-3c30be4493c1 | -6.12087 | -42.54081 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a03a81dc-06f0-3366-ac53-736d8cf32a2a | -9.17877 | -43.25045 | 2024-12-11 04:33:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 911cf818-3323-3ea7-a29b-8b3d4ff5c6d1 | -5.84687 | -44.7812 | 2024-12-11 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a3c1596-3489-311c-b3ac-c97abd10348b | -6.978 | -42.99929 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 814344ca-6c41-3ef1-9aab-d2d8fac84f25 | -6.95623 | -42.97729 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ede893a-9860-33d3-b644-c19a6681db9b | -2.34328 | -53.59032 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c5bda47-387f-3ef8-b7e2-0b7a8c80c6c7 | -6.9688 | -43.00525 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29fd6e19-637e-3eb0-b4d5-a960d88d4931 | -6.91142 | -43.50021 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ecf93ac-e0b7-3e6c-9ea2-6953016b1b23 | -2.78961 | -52.86646 | 2024-12-11 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84c29573-c372-3eab-94a9-785454f5626b | -5.0075 | -41.87054 | 2024-12-11 04:33:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35f0bd21-4b43-3bf0-bf7a-104ae16cffa4 | -6.12611 | -42.53384 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65f2b1a9-9326-3120-ab8f-3f46de3e83af | -6.969 | -42.97553 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be1a3e05-bd38-3ee3-ad22-7e758b03f33f | -6.12971 | -42.53827 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b5445675-fe9f-382f-8c89-643da2be06b1 | -2.36068 | -53.79598 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 966616c2-35a4-37fa-8b07-ec93c40d1d57 | -2.25147 | -53.8719 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4457c5-ccf6-3224-aaa8-a44e2a57ae07 | -3.09631 | -53.73516 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 479a1ae2-546c-31f5-8a14-100eea0869e1 | -6.90211 | -43.50911 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0e8e07ae-dcff-3c90-885b-e292aa7cab6b | -6.96438 | -42.97857 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 770cd266-f64f-347f-928d-bcb6aeb6fb6d | -6.94702 | -42.98331 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf01bde7-9822-3869-8485-ca5e849b9295 | -6.95305 | -42.99909 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 943af0d3-1ee6-3ade-99db-2390079dd007 | -2.61456 | -54.24151 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24226a9f-6d83-3c28-8647-aef79d507aa1 | -6.90115 | -43.5179 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 751fe6dd-cc63-3ada-b040-b66d683fbb87 | -6.16662 | -44.42316 | 2024-12-11 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a9b6b9e-f294-30c8-90ac-aa736ffba392 | -6.95109 | -42.98395 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69d3c3a0-8bc0-3049-9662-311bf8d0eac0 | -2.30015 | -54.00174 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff544b11-dbe4-329e-aa4d-0801f1fbab6b | -6.90282 | -43.5041 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 28e1aac8-ca79-3696-8782-583d3d0692ac | -2.78544 | -52.86572 | 2024-12-11 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05d87e09-06bf-3202-a372-cf4111a817da | -6.16729 | -44.41864 | 2024-12-11 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c235da-930d-3b60-8cea-d814b7b40889 | -3.3312 | -53.24511 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b8e5d540-91af-3032-85b7-fa631b4b0059 | -6.96632 | -42.99375 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 120ffc8d-b6b1-3a6b-b4b0-baf0b5a254e3 | -10.20095 | -45.18188 | 2024-12-11 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 321c8af3-a1b8-3888-a841-d1832b273b4f | -6.97307 | -42.97617 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 958b090a-4455-3df5-9e78-df618bdf256b | -4.54991 | -48.00366 | 2024-12-11 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69bc8e93-6e7e-3ed8-825c-7630017e2946 | -6.89721 | -43.51731 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 0c38e7f8-b938-3bad-8383-118471223fd9 | -5.34308 | -42.11952 | 2024-12-11 04:33:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd206212-2c64-32dc-91d3-9ba855daf580 | -6.90927 | -43.51535 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 65b0049d-e6e5-3a70-9279-ec67200ed060 | -6.97661 | -42.98045 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3f7e001c-64f5-339e-8f92-4ff55bc9359e | -6.12141 | -42.53703 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba1653d7-88bf-3b13-b7ed-68e02c07417b | -10.59346 | -44.98041 | 2024-12-11 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e8df312-0c8e-35e9-a766-be5290f4f399 | -10.59334 | -44.98223 | 2024-12-11 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba78fce7-5763-37df-af58-694cbb6ce203 | -6.10181 | -44.04908 | 2024-12-11 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eaa1f58-b2a0-3412-9157-fe0673dfc828 | -6.91203 | -43.49892 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 60f73e07-2e31-3cdb-b375-bdadd5352bd5 | -6.19205 | -43.45786 | 2024-12-11 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0049e78-7db4-3a53-b267-7553311b3f16 | -3.3361 | -53.24187 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f036a129-8cf2-38a8-aa4b-0c92e3982b17 | -6.97199 | -42.98352 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47c2d0f8-765d-370c-8680-7be71c59d81f | -11.04363 | -41.98487 | 2024-12-11 04:33:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 788637c8-2111-3b4b-85d3-177d0d4c004e | -2.60997 | -54.2407 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0acb6d59-4031-3d0d-871a-e3a6edae19a5 | -6.96473 | -43.0046 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d29d3beb-5902-3b69-884d-74ec03e8ad99 | -5.3033 | -43.28103 | 2024-12-11 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e150e13c-f5b3-3c4a-8f2b-8974acfa9454 | -6.94182 | -43.54081 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b02a608-d87a-38f6-ba85-e3925cbfceca | -6.89871 | -43.50723 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| e2ae6358-c325-3641-9cd0-1332fa08bfd3 | -10.75498 | -44.9319 | 2024-12-11 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b54ae2dd-95c2-3d18-9a4e-f65f0ad5b6a0 | -6.96492 | -42.97488 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76c97464-6ad5-3cda-8b9c-f35f5c421941 | -2.8171 | -53.07266 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3cf424f-2788-3691-ad1c-76e6bad69db1 | -6.95924 | -42.98522 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0108f3f6-9552-3f0c-8bf3-64b9e6414dd1 | -5.42552 | -39.52973 | 2024-12-11 04:33:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15210486-c6f2-367c-bd0e-562862077993 | -2.96627 | -53.72955 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ee94bde-1d7a-376a-8a24-8282cb097e08 | -5.42656 | -39.52979 | 2024-12-11 04:33:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 546a8900-642e-3c62-a396-d1b07309b55c | -2.80138 | -54.19102 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e007d43-4042-37e9-9c48-cd4b8cddd75f | -8.32238 | -43.51822 | 2024-12-11 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e5fb9f62-b6e5-34b4-a396-934b6771617d | -6.96084 | -42.97425 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40cd478b-0e4b-366b-ba45-6afcb0692802 | -3.86131 | -40.80484 | 2024-12-11 04:33:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20473936-f256-32a6-9ee2-306b81d31378 | -5.9493 | -38.32817 | 2024-12-11 04:33:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 642983a0-92db-3a0a-a749-dae2c3c12061 | -12.71562 | -54.97315 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccd706de-c5c8-37bf-9800-42e77b0eeded | -12.53184 | -58.36158 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71ec5864-5a21-3543-b2c4-992f96ae809c | -12.24834 | -54.29337 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00f7447f-b68b-3e3d-92e9-9c61f654ed83 | -12.55478 | -58.35309 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c726d4bc-bfdd-3537-95ca-93d717bcc1ba | -12.53367 | -58.35217 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a60bdbfc-24ad-3608-aa19-825705325f64 | -12.41874 | -43.80104 | 2024-12-11 04:36:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| def0425f-b1ec-38ec-af59-3b1d21d3e7a1 | -12.55085 | -58.34583 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7ae9a213-5d9a-3ea3-8d56-d9ad1b2f1ee1 | -12.53564 | -57.72321 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78216a58-963b-38e3-8729-b5c91f9aadb0 | -12.53847 | -57.72795 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5507afa9-e2f3-392c-943b-d5af4f630007 | -11.11985 | -54.6487 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ad4529e-f33b-3d4e-9179-84a636406d5f | -15.0226 | -57.62188 | 2024-12-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e20e004-0bd6-3200-a8e8-dd98c7a00f02 | -11.46993 | -44.95565 | 2024-12-11 04:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 306161c0-9ac4-3dbf-9ea1-6597f4a5bb25 | -12.54515 | -58.34782 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3bdc3660-2e27-353b-b998-ec16dbf94670 | -12.70805 | -43.89825 | 2024-12-11 04:36:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0036734c-4ada-317c-b109-0fa249f270ed | -12.54695 | -58.3385 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59295c2a-dd22-3ab0-b0c9-53ff4268df55 | -9.72122 | -54.89088 | 2024-12-11 04:36:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 368a15ca-4e67-39ed-add4-1907a7b99e64 | -12.54225 | -57.74207 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0043eccf-756a-35f0-ab52-2ccc0c5dbfb9 | -12.54575 | -58.34473 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bd0df48-35ac-35ae-82a3-5be88efdc7cb | -11.8008 | -43.80417 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f79de1-81ca-300c-ab2b-6a63ed83c9ae | -12.56326 | -58.36438 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db8154c7-0e2b-3e26-88aa-33ff1e5c042f | -12.54153 | -58.36659 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
