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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475ddff1-30e2-31de-b55d-62aaec4f394f | -9.89114 | -67.3415 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57172335-ae5b-3216-9bbf-287b7776efde | -9.88846 | -67.34267 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0cb4f8f-3324-3c79-9e7a-48337cc79df2 | -9.88404 | -67.34003 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a6d060-875f-3c7e-896d-21656dbfe74c | -9.88258 | -67.34711 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f658a1f8-a075-38ca-833d-03e021a26660 | -9.88137 | -67.34119 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b326232e-e3b2-3e21-a712-8d9ba22c41ab | -9.47028 | -66.58361 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d89d3ce8-8633-3ab3-81bd-04848d5f7a8e | -9.42529 | -67.23668 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47125d4e-88cf-301c-966c-245d4f753dfb | -9.4182 | -67.23508 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 163916f5-45a2-300d-8943-9f69d2aeae00 | -9.09793 | -67.50643 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72f9b0ff-4f08-3698-8726-acd85dd94421 | -9.09706 | -67.50652 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 821c5b43-6cef-3625-affa-441b25823a07 | -9.09643 | -67.5138 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fdb26cc8-a983-371e-81cc-846b90f5f1d4 | -9.0956 | -67.51392 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 385c961c-62fe-39ce-8045-0e9a7bcd9553 | -9.0949 | -67.52125 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4839d00a-b836-37c0-bf4d-2be62d42feda | -9.09412 | -67.52139 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb367312-3e8a-3c0b-9a18-5724558990e3 | -9.04484 | -67.50321 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15e61efa-fe2a-3a43-bee6-d322806ca2c9 | -9.03757 | -67.50178 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c0923d-4d14-36c2-b7cb-3a8aca033922 | -8.98899 | -67.4068 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f629d8e9-dc9b-32cc-908a-9d7d5d733e08 | -8.98797 | -67.40877 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 214765c0-9bcf-3e6e-949d-77d9aa5fdf1e | -8.98747 | -67.4142 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a3e170bb-3fcd-312d-a5d9-a2a5501a95b7 | -8.98649 | -67.41624 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff067719-01aa-3e8e-a037-0e0ad4c1e81d | -8.98073 | -67.40734 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06ffa8ec-f67e-3591-8904-91c838ceaf42 | -8.98023 | -67.41276 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5719bc54-2c91-3d9b-bef7-45af8098ad54 | -9.42364 | -67.6203 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b9b7058-5bfc-3b84-88be-15057cdd4f0a | -9.42312 | -67.6232 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2087ccbf-0016-3e3e-ba50-9060f7942743 | -9.41638 | -67.61878 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ea1602-1bfd-3ba1-b80a-6a3e5b6ca256 | -9.41586 | -67.62165 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7b28a8-195a-39dc-a95e-650ed29f235a | -9.36345 | -67.39545 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf1215f3-7a0c-3527-aff8-2d35545c3b57 | -9.36143 | -67.39569 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa15b092-f806-3115-a2ad-354c2e32c246 | -9.35627 | -67.39398 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1f18ed6-5afe-3be3-bfaf-41420d88a043 | -9.35425 | -67.3942 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ec66e52-60f6-3d50-8926-d12eea1e793a | -9.62895 | -67.47279 | 2024-10-03 04:51:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 634e104f-56f5-324f-aec9-5978951c4462 | -9.62822 | -67.47072 | 2024-10-03 04:51:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 31cf6324-568d-331a-998e-94afcdb15cf4 | -9.62673 | -67.4782 | 2024-10-03 04:51:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4db16d0-0238-317a-bedc-c55476a000d3 | -10.53034 | -67.85583 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b835078-2722-38c2-b183-22dec49223d3 | -10.52316 | -67.85408 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad073828-f8f3-3680-bc08-bc5c69eaf1ad | -10.50661 | -67.89681 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8bdf8ee6-b95f-3e53-8d0a-ca4d319d2168 | -10.50622 | -67.89367 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cd6d569-45b4-3e02-8232-b89a45ea2ca6 | -10.50471 | -67.90109 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca06b0ba-8bca-36f5-9b16-bce12b9c1d34 | -10.49936 | -67.89531 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78aed1d4-92ba-3b43-bcc6-d22552b304ef | -10.49747 | -67.89949 | 2024-10-03 04:51:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17c9e265-58eb-3003-9bad-1b726358fe96 | -10.11265 | -67.73721 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de66a49a-9bc5-3f8c-97e2-336f89fb4234 | -10.10824 | -67.72772 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708e59e8-4fee-32c2-bd94-7cafd63d0a6b | -10.10694 | -67.72819 | 2024-10-03 04:51:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22be6ee6-8544-3221-ae5e-7dd4cdbbea6b | -10.10668 | -67.73516 | 2024-10-03 04:51:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d92dd14-e23d-3a96-a2f7-7d625d03baa6 | -10.10543 | -67.73561 | 2024-10-03 04:51:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8afb3bd9-49c2-3f15-be1d-18eb3c94a69e | -16.33851 | -42.30121 | 2024-10-03 04:51:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a312c5d1-2c68-39e3-b957-fe1132b17180 | -16.33261 | -42.29412 | 2024-10-03 04:51:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63c8ac40-da46-3aaf-96b1-187b65dff541 | -16.33204 | -42.2999 | 2024-10-03 04:51:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f61505f8-504c-3eab-84ee-81272db67c17 | -15.23832 | -43.33442 | 2024-10-03 04:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f26bb1d4-e8da-34df-ab17-4aac73e49ece | -15.23757 | -43.33451 | 2024-10-03 04:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4fdbd829-f723-3145-bc25-6e241ef62536 | -15.23226 | -43.33369 | 2024-10-03 04:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5104537-3555-3e02-91df-8d86778f82bb | -15.23151 | -43.33381 | 2024-10-03 04:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61043a04-c86c-30f6-8640-0d3c1bdc5c11 | -9.25591 | -43.49704 | 2024-10-03 04:51:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f6368ae2-1219-3e9b-b64e-76e0aacbfa23 | -9.49996 | -43.16826 | 2024-10-03 04:51:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23658b5f-039d-3730-b186-469c72eeb5ce | -11.84331 | -43.82718 | 2024-10-03 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91228d4a-17ef-399a-aa1f-591dcdaafdc1 | -11.84284 | -43.83099 | 2024-10-03 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cac2a35e-462c-3369-85e1-993ddcedc8d8 | -11.83768 | -43.82645 | 2024-10-03 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab08da5-d743-3de3-8049-fd851657161a | -11.83722 | -43.83025 | 2024-10-03 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960af06c-70dc-33b6-8771-8453158d1176 | -11.27859 | -43.39397 | 2024-10-03 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d108db45-4575-3335-be73-06e48f036e8b | -11.27809 | -43.39794 | 2024-10-03 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ab1d571-2553-3e07-980e-39d720391fb0 | -11.27285 | -43.39321 | 2024-10-03 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92fc5d17-90d8-3c19-a2af-675243dec7ef | -13.30976 | -43.70969 | 2024-10-03 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7860580-60cb-327e-992e-d7e9469c509f | -13.30929 | -43.71378 | 2024-10-03 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbbe1b9c-c85e-351f-9433-052e07d80bf8 | -12.99535 | -44.72174 | 2024-10-03 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e809527-81cb-3cdd-ba90-8fde8b4ab69a | -12.99037 | -44.71764 | 2024-10-03 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e3e4bc5-2744-366e-98f4-30b9e4e430ac | -12.98996 | -44.72107 | 2024-10-03 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80944ab5-715e-343e-8a4e-a871b4704e7d | -14.5148 | -45.23837 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7237a2f-2a4d-3ea3-9c1d-35168e08a9ff | -14.5144 | -45.2417 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdf3e1c3-9767-332d-b78b-f5d0f6cb75a7 | -14.51065 | -45.22778 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a000ec7b-41cc-3f11-b5b6-4450ab44cf86 | -14.51026 | -45.23105 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 177e87f8-4359-31dd-9619-244fa4c4c0dd | -14.50988 | -45.23434 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e92b0dee-3e85-3ae7-8c7a-7c32024af128 | -8.85586 | -45.51044 | 2024-10-03 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab701b25-675b-39e6-b0dc-50cca2e84877 | -8.85514 | -45.51567 | 2024-10-03 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb645bad-fd6e-355e-be99-58d3054255af | -8.85105 | -45.50977 | 2024-10-03 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d287714e-896a-3f41-a5ae-074a6339dc77 | -8.85033 | -45.515 | 2024-10-03 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0944f6f7-34aa-3653-aee1-84bc3700ad70 | -10.6648 | -44.49759 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16569ccd-3a2b-3cc0-b01e-738b12a90036 | -10.65951 | -44.49688 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918ec2f3-245a-3ac9-b2d0-3287498adc11 | -10.65909 | -44.50018 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81cced9f-5e45-344e-9e51-8cb34aa8b3eb | -10.87931 | -45.96069 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4706fe16-cd53-30f4-a99b-08d498f74df5 | -12.26889 | -45.96711 | 2024-10-03 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75824ec-a8b2-382e-b8fc-1f6d90d8f202 | -12.26693 | -45.96457 | 2024-10-03 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e5c0b95-9bd8-3863-a90d-6c7d70382c36 | -12.2662 | -45.97004 | 2024-10-03 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6fe5bad-2fb8-31fb-94ea-2b0db03e4852 | -13.18351 | -45.45161 | 2024-10-03 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c599f71-7e7f-3e39-af16-3e4678443b84 | -13.18126 | -45.45124 | 2024-10-03 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a480bbe9-ffc2-30e2-86bf-f6f9f911732c | -13.17874 | -45.44786 | 2024-10-03 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6dc1c68-ced4-3815-b467-2ac963923627 | -13.17651 | -45.44752 | 2024-10-03 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8a6245b-d674-3c28-9d08-40728f246d60 | -14.1994 | -46.46326 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7540935-57b1-34d1-bd09-0760b51dd55b | -14.19874 | -46.46844 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a3fb594-2fce-3151-9ee3-085e5efc1c91 | -14.19516 | -46.45764 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b78f022d-fcc1-343c-8fb5-cae07610e511 | -14.1945 | -46.46283 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52e04d4b-9865-36f6-a733-d2b0e0cdbc65 | -14.19387 | -46.46791 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72e4e66d-09b8-378e-b111-fee594ff5638 | -14.19322 | -46.47301 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3289535-4075-30de-8e68-c4803ca6f0af | -15.73556 | -46.87469 | 2024-10-03 04:51:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f86ad14-3891-32ef-99c4-7b46ed91d397 | -9.10411 | -46.90388 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15601502-e15f-3956-84e9-04c635980e5a | -8.72773 | -47.10352 | 2024-10-03 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5620216c-e10e-3fde-bdb8-627df48acd0b | -8.72343 | -47.10287 | 2024-10-03 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f94dce8b-f2cf-31b0-ba54-5c177f1d867b | -8.62996 | -46.53116 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7e3cb8c-e168-30dd-a559-ae480559d5db | -8.62615 | -46.5259 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c199502-2673-3210-b7fa-e2c7f4638b81 | -8.62168 | -46.5252 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2784718c-cde7-3c17-ac1d-3d49b041d34b | -8.60762 | -46.52789 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README122.md)
