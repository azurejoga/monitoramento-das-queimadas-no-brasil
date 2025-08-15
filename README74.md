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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1920febf-5cc0-38d4-8c29-442c1c97811d | -14.12061 | -44.66583 | 2025-08-15 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f1e204e-1608-34c0-935b-0ce062e58a98 | -8.83364 | -45.55542 | 2025-08-15 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7d9a893a-86bc-3e3b-82ab-9dc5cf6ee12e | -8.72967 | -44.01981 | 2025-08-15 12:14:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a2942dad-0640-3c04-bb7b-3cd7f18faf30 | -8.30267 | -49.02364 | 2025-08-15 12:14:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 1958812b-e1b1-3be6-bcae-be4f163617f3 | -7.44955 | -49.24775 | 2025-08-15 12:14:00 | TERRA_M-T | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d9eec219-a91e-3ca0-9275-d5124900f473 | -7.43174 | -44.59767 | 2025-08-15 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a1160542-140b-3a3c-a5dd-e78e63d3a4de | -7.0221 | -44.29901 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 136bfdbb-1cf0-36bc-85bc-8f2ab1921ac0 | -12.78778 | -45.96768 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7fff1e02-7df7-3533-8e41-da2460d07f38 | -11.89961 | -47.06728 | 2025-08-15 12:14:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36600508-2cb4-329f-a1b7-029dd654fe04 | -13.65409 | -46.9357 | 2025-08-15 12:14:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccce87e0-b6ea-3528-a1c9-2e788b4e1e26 | -13.32287 | -45.24177 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 991b31d5-40af-3c43-b90f-a84a21a3ebb0 | -5.70039 | -43.6652 | 2025-08-15 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| db4796e8-b436-3841-b54b-a9bc1825d91b | -12.83146 | -44.46255 | 2025-08-15 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c481414c-12fa-321a-8d5a-2adf1ab8771a | -7.42288 | -44.59641 | 2025-08-15 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2e12642d-7235-35f0-93b8-e6c86fe00033 | -6.97295 | -42.87551 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| de17af54-c030-3bb1-9b81-be87a0291460 | -6.87168 | -42.8035 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| afa1f66f-00a8-37ac-ae4f-6adc2e0b8332 | -6.96495 | -42.8641 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 3c7795df-eb92-3e15-b573-9df6d7eabe63 | -5.27019 | -43.581 | 2025-08-15 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 2161b057-1932-3ce6-a919-1ca1bb18246b | -14.16433 | -45.34955 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 93c74fa4-a34a-35e4-83f6-77340cae8249 | -7.6132 | -45.20218 | 2025-08-15 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7c1d5f31-5b44-3aa3-be71-a77ec4b29258 | -13.5206 | -42.39351 | 2025-08-15 12:14:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 94f86a01-2470-370a-926c-ce44ab580216 | -13.40543 | -49.13268 | 2025-08-15 12:14:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| accc5109-f5ea-3f12-92a0-42a691c597bf | -13.30535 | -45.23325 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7566cbf1-5f74-3777-98e4-2614aeae2095 | -14.59612 | -41.8285 | 2025-08-15 12:14:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 773eb1ff-23df-3333-b19c-05690abbf7f4 | -7.61447 | -45.19335 | 2025-08-15 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 42b42267-08cc-391d-b48a-25f51b1ddeea | -6.9487 | -44.5475 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8408e3d1-25b4-32bc-80bb-fb791b0b9d27 | -7.58648 | -46.08364 | 2025-08-15 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a25bca1b-2986-3759-b552-25e0bc8e2c2b | -11.4071 | -47.58953 | 2025-08-15 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2ff0fe39-9e07-3b79-ba44-6be1979804d1 | -7.03272 | -43.8297 | 2025-08-15 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 117c751f-4f0a-3c64-b2ef-6d61642cc912 | -10.65344 | -48.93259 | 2025-08-15 12:14:00 | TERRA_M-T | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 18f61947-1368-37e6-b795-491402fc98f4 | -10.37065 | -48.29155 | 2025-08-15 12:14:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 039fcf4a-173b-3e5a-81f4-561e36ece436 | -12.58832 | -46.96159 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 09a6e311-7b8a-34bd-a9aa-45948bc35440 | -9.62308 | -48.22394 | 2025-08-15 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b57a68de-ae52-3122-813b-4576fc05b6ed | -7.09876 | -46.32444 | 2025-08-15 12:14:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf58c683-1537-38a4-a7f3-2d1ebe9c27fe | -12.31827 | -50.04812 | 2025-08-15 12:14:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ad265dc7-0743-3119-a275-35661a144649 | -13.41582 | -45.89819 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bea298e4-2d0f-39c7-b70e-e3fc1339c629 | -9.19096 | -45.32355 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| c8288ce6-64f4-3bd6-9580-fc9d9a384c78 | -14.24017 | -44.5816 | 2025-08-15 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3f9d983c-e960-3c05-beb3-8a9f1663a7d7 | -13.33316 | -45.23366 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 357.9 |
| cfcb3a66-89ce-3557-b0cb-140aef716786 | -7.3775 | -44.83742 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bfdf1de6-8174-3a34-b77a-80b463527e75 | -13.30666 | -45.22386 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ec91c68b-0bce-333d-8f53-ae5874974068 | -6.96354 | -42.87427 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 51feb8e2-c276-3ccd-9152-75a6ef36c694 | -12.49575 | -47.02555 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 72aab336-b2ad-347a-996e-9b097a864c5a | -15.14588 | -45.64401 | 2025-08-15 12:14:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bbcf3bfb-2a09-36ab-98f7-55fb4faa022b | -7.29149 | -41.5933 | 2025-08-15 12:14:00 | TERRA_M-T | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 65d1d103-d66d-3c3d-b420-50e71fbb49c2 | -5.69141 | -43.66397 | 2025-08-15 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d7438a2f-4cf4-3127-a3ca-6848d3f5d9e7 | -7.40262 | -44.86547 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 85536f8f-4175-3dc0-9cc2-4b6369a395e8 | -19.12029 | -44.46533 | 2025-08-15 12:17:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c52357b5-6cbe-316f-87c7-081a472a1dc2 | -16.00286 | -48.0905 | 2025-08-15 12:17:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53e8e98e-ea62-3cea-b53f-027d95f28310 | -22.96134 | -48.83005 | 2025-08-15 12:17:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0857f4b-82ac-3c60-989e-c1e4787e9a0d | -22.96272 | -48.8205 | 2025-08-15 12:17:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 670842bf-11b0-38a8-ab3c-6823f9cee45b | -16.28432 | -52.02579 | 2025-08-15 12:17:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 90ede879-9371-30fb-ba90-3c8c10a9aa66 | -17.93762 | -44.38285 | 2025-08-15 12:17:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0e3a79ce-79bb-38c1-ac43-19838dfd5a6e | -19.12004 | -44.47121 | 2025-08-15 12:17:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6c466973-cbe1-3ca3-9fba-e0487400e950 | -16.00146 | -48.09996 | 2025-08-15 12:17:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fae4761c-aa4a-34c2-ad67-d9f2ddb17d35 | -21.43392 | -45.11724 | 2025-08-15 12:17:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8eccbe6e-2216-3155-8c01-bc8b56a5be6d | -20.95979 | -45.55614 | 2025-08-15 12:17:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2ec76a1d-9b59-3332-a5a8-9427604e3b21 | -15.40249 | -55.77821 | 2025-08-15 12:17:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a0c28079-aff0-388b-be8b-d8c3045b3d93 | -20.69492 | -48.99338 | 2025-08-15 12:17:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c68c60f0-7d10-3983-84d7-92d944e880e5 | -17.97006 | -45.52296 | 2025-08-15 12:17:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 789ec79d-cf67-37be-a674-16f23cb32a71 | -20.6935 | -49.00293 | 2025-08-15 12:17:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a1b6b1ff-ec47-3474-921a-e02e66903a67 | -16.47688 | -51.9799 | 2025-08-15 12:17:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2d7ab4ed-3f87-3daf-90ae-c61315b0bb07 | -16.0635 | -48.05822 | 2025-08-15 12:17:00 | TERRA_M-T | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 953039c7-e6aa-34c2-9132-e502746c3c91 | -19.52662 | -43.98692 | 2025-08-15 12:17:00 | TERRA_M-T | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 83ada98e-9cc8-3334-a58b-db6e7d686326 | -19.14536 | -46.48461 | 2025-08-15 12:17:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50b3421a-b58c-33dd-84de-2c12f74de3b7 | -14.57442 | -52.03594 | 2025-08-15 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b5a304d7-2dd1-3d3b-a221-483f40ac6462 | -19.83248 | -44.63536 | 2025-08-15 12:17:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| a145a401-5686-33bc-b7c9-196fcfdcfaa9 | -21.56852 | -45.09396 | 2025-08-15 12:17:00 | TERRA_M-T | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 12913f23-2061-3efe-99b7-89c4180b831e | -19.34772 | -49.17722 | 2025-08-15 12:17:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1341efae-177c-3840-8001-79e625a75473 | -14.56028 | -52.04995 | 2025-08-15 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 800a0db9-19d6-300f-a366-2d2d43fdc592 | -16.0621 | -48.06757 | 2025-08-15 12:17:00 | TERRA_M-T | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f8c215f8-5c5f-3c60-946a-b2e073dfcb33 | -16.2818 | -52.04071 | 2025-08-15 12:17:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 71cca09c-5bc5-3101-9341-456f3459ae72 | -17.6483 | -44.48827 | 2025-08-15 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d25f2ce7-7fc3-3660-8e8e-edead18f04d3 | -20.95839 | -45.56709 | 2025-08-15 12:17:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c83f4b39-1c9e-38ee-88de-bbbff06261e1 | -19.64806 | -46.09502 | 2025-08-15 12:17:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e201c195-1a11-3b12-9513-b6ad29b7ef0b | -16.04242 | -43.81802 | 2025-08-15 12:17:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c00e2fd0-4e77-378f-96ae-4c88d167f3f5 | -16.37695 | -50.90823 | 2025-08-15 12:17:00 | TERRA_M-T | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 034d2dca-2851-37b6-aac0-cd5670c3c84d | -15.4055 | -55.77172 | 2025-08-15 12:17:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c5613330-c908-3887-b95e-dad914ce1c98 | -16.379 | -50.89562 | 2025-08-15 12:17:00 | TERRA_M-T | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 205326cd-5715-3b45-bb4e-664f3d78e588 | -18.73758 | -46.90568 | 2025-08-15 12:17:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 36.9 |
| fe58b0fb-b42e-3532-a072-f418123f93a9 | -14.5718 | -52.05192 | 2025-08-15 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ab483a13-a9d7-367f-8ead-b9578038a186 | -16.04088 | -43.82998 | 2025-08-15 12:17:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fca336d3-9e77-378c-8cb9-65952459f4a5 | -19.52828 | -43.97355 | 2025-08-15 12:17:00 | TERRA_M-T | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f20b5e90-c1c7-3468-aa64-9aa49d53a04e | -20.15281 | -48.91569 | 2025-08-15 12:17:00 | TERRA_M-T | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5bc26651-37fb-36a2-bfbb-e48e14a0a051 | -20.15423 | -48.90614 | 2025-08-15 12:17:00 | TERRA_M-T | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b4145363-9526-3407-92b0-e2346bea4131 | -21.28595 | -45.94878 | 2025-08-15 12:17:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9a253aea-1a8c-33ff-9863-b26ff1c31641 | -18.73627 | -46.91507 | 2025-08-15 12:17:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3f2a7ad7-c493-3719-98a6-578a9ac9180b | -19.65932 | -49.37413 | 2025-08-15 12:17:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| db4bc6bb-6e48-38e2-9e64-14bceaeaf807 | -19.11874 | -44.47737 | 2025-08-15 12:17:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c41f8b09-c89f-3a57-9023-2fb280bccd1d | -17.96079 | -45.52167 | 2025-08-15 12:17:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 000a6d53-f095-33f2-960a-cfede19194ab | -25.7142 | -52.2442 | 2025-08-15 12:19:00 | TERRA_M-T | CANDÓI | PARANÁ | Brasil | 4104428 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| bc8482f9-f51e-3bc0-b891-b4f76ee07d95 | -30.90914 | -52.02183 | 2025-08-15 12:19:00 | TERRA_M-T | CAMAQUÃ | RIO GRANDE DO SUL | Brasil | 4303509 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| 326f3368-8952-36ba-ac55-fbfed63be2e6 | -13.3198 | -45.2409 | 2025-08-15 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 360.1 |
| e04af7c9-76f9-342a-ad39-ed94495eeda2 | -13.3397 | -45.2145 | 2025-08-15 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 251.1 |
| 0a8370c5-e4ef-3502-a8b5-8ef3f29592c1 | -6.8673 | -42.7961 | 2025-08-15 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 418.5 |
| 3d7af621-194a-3bdd-8779-01a7fa0327bc | -5.2647 | -43.582 | 2025-08-15 12:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 282ee5f5-b2e4-39eb-994a-509b28838c04 | -13.3392 | -45.2377 | 2025-08-15 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 3970cf2d-c519-36a7-ad3f-65254f60a281 | -13.8937 | -45.561 | 2025-08-15 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4a906a28-cbd1-36f4-84aa-c81143b31e35 | -7.4085 | -44.8571 | 2025-08-15 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 1577fedd-d653-3e7f-a048-7f8eebec28d0 | -13.3009 | -45.2209 | 2025-08-15 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |


[Clique aqui para ver as próximas entradas](README75.md)
