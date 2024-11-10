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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5921b7d-c8f3-338d-9de9-d40e3db48289 | -8.5594 | -37.80092 | 2024-11-10 12:04:00 | TERRA_M-T | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 57e3de8a-78fd-3395-8e4e-89622a0e90c9 | -8.68171 | -40.7365 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 4233e407-6090-3a4e-b576-43ec0dca288a | -10.11847 | -40.73363 | 2024-11-10 12:04:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| f86cdbec-a4d0-30c7-8841-354cd076fd26 | -6.14355 | -42.60412 | 2024-11-10 12:04:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 5626e6b9-3f37-3d95-8a59-f58781c70979 | -6.34193 | -38.33454 | 2024-11-10 12:04:00 | TERRA_M-T | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a46ec320-f475-3f8f-afe7-3e0094c50442 | -8.80477 | -41.41175 | 2024-11-10 12:04:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 1c79d952-1d40-3345-abad-67339b452124 | -10.38462 | -37.29181 | 2024-11-10 12:04:00 | TERRA_M-T | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| b006c41d-1934-3aff-9e4e-08c232c3133d | -8.39887 | -44.14839 | 2024-11-10 12:04:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 819.0 |
| 435a90ee-a8a1-3451-a05d-9e6beec20170 | -8.68279 | -40.74325 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b9d30ebe-fa92-351c-ae90-3013e6a2b506 | -9.25449 | -41.22174 | 2024-11-10 12:04:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 76ff8138-dced-3736-bf59-e1abc66368f0 | -10.94576 | -40.81927 | 2024-11-10 12:04:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 6dc15976-76ea-3e1f-8b6f-c7a1f5399c19 | -10.93084 | -40.05764 | 2024-11-10 12:04:00 | TERRA_M-T | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 191ab91d-4d25-3036-8336-433aeef6653c | -8.74131 | -40.8199 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.9 |
| c30beb26-8d79-3b59-9018-89909d7df20f | -8.68451 | -40.73215 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 02cc297c-ee2b-3107-a464-cacdd9fb6ccb | -7.73006 | -37.54568 | 2024-11-10 12:04:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 3e9f4667-6d74-3273-8ace-79bd65aeacad | -7.73955 | -37.80611 | 2024-11-10 12:04:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 034a7236-7202-3ed0-b4a8-6a322f2f4cdf | -9.25355 | -41.22728 | 2024-11-10 12:04:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 137e9a35-159f-314d-aa69-6bfc14ec5985 | -8.06098 | -38.69155 | 2024-11-10 12:04:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3f3d2bad-ae06-3b61-b97d-6a82561d9b83 | -5.57755 | -43.97281 | 2024-11-10 12:04:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 701b526e-1870-3b1c-8f19-93a79c16fb70 | -6.14607 | -42.58779 | 2024-11-10 12:04:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 663.8 |
| 3ef0fddf-3a74-34b7-b616-97ecca5d92f2 | -7.35366 | -39.16869 | 2024-11-10 12:04:00 | TERRA_M-T | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 367fb38b-9a76-3320-995d-624ce6e53f6c | -7.72878 | -37.55453 | 2024-11-10 12:04:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 99380f45-4182-394f-a439-d40bf19fcd79 | -7.68259 | -37.36087 | 2024-11-10 12:04:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 6561ec9d-1b93-3069-a1d1-35ba7d73de0e | -7.43256 | -39.76606 | 2024-11-10 12:04:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d8e80461-2709-383d-8092-191f4a73fd4b | -8.05964 | -38.70066 | 2024-11-10 12:04:00 | TERRA_M-T | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bfad4214-aa81-3ae6-830e-03f94027de4b | -8.15484 | -37.67313 | 2024-11-10 12:04:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2fcabc4c-3bf3-3a13-9563-7c242a5d2845 | -8.90538 | -40.47309 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ce786ede-1dfc-361c-aea8-74e2cdf5a091 | -8.68337 | -40.72533 | 2024-11-10 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 782171b6-ff7b-3538-a16e-dffc4aba9354 | -6.15778 | -42.58952 | 2024-11-10 12:04:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 9a7fb408-0040-3df0-9430-276df7c87e0f | -1.476 | -54.3166 | 2024-11-10 12:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8df284aa-48ad-362c-828c-d920900d5029 | -3.1983 | -50.2867 | 2024-11-10 12:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 70d28855-d626-3c27-9430-a76b700a0829 | -17.5872 | -57.5328 | 2024-11-10 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 7e9afa1b-0162-3ef0-99c1-827bd4ace837 | -2.0656 | -46.3339 | 2024-11-10 12:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 14064485-0fa8-327c-8834-900e01e7afcd | -23.9095 | -54.0606 | 2024-11-10 12:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 187.4 |
| d36a13d6-f5a5-3cd8-a464-70687de9f98e | -23.9089 | -54.083 | 2024-11-10 12:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 209.3 |
| 8de6b218-7471-3299-828f-b4d71cdb9854 | -1.5299 | -54.9941 | 2024-11-10 12:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| ed3de635-4257-30ba-a7cf-fee907790e2e | -17.2933 | -57.4857 | 2024-11-10 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| f140b0a1-7c88-30c7-9ef3-9268bea8044c | -17.6073 | -57.5099 | 2024-11-10 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 258.1 |
| b62519c2-b75e-3ccf-9dd4-93cc6ff0b552 | -1.5116 | -54.9944 | 2024-11-10 12:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 7390d104-fe5a-35f7-8c1d-809e9878c20b | -1.476 | -54.2965 | 2024-11-10 12:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 51af1176-b66d-3817-af4c-1e34c3169cad | -17.627 | -57.5075 | 2024-11-10 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 184.0 |
| 12bcd2fe-9e7b-32cd-8da3-39b01df99dad | -17.5872 | -57.5328 | 2024-11-10 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| dcab65fa-733a-38e9-9a30-f1b7e5e8f029 | -17.6073 | -57.5099 | 2024-11-10 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 257.4 |
| 290c6bd7-77e8-33e8-ac67-adf9ab56f1b3 | -1.5299 | -54.9941 | 2024-11-10 12:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9064986d-26eb-3931-b61a-8e2877b729a9 | -4.4349 | -44.6229 | 2024-11-10 12:20:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 198225e2-7e88-313e-bf92-09c63cb73ff3 | -1.476 | -54.2965 | 2024-11-10 12:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ecef78ec-b8fc-38ac-8c49-20625267dddb | -17.2933 | -57.4857 | 2024-11-10 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.0 |
| aebabd1f-e24c-3390-be32-e17e4c902bfc | -17.627 | -57.5075 | 2024-11-10 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.9 |
| 4e937927-a2e1-3746-8bc2-efff039722c0 | -2.0656 | -46.3339 | 2024-11-10 12:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d15d2ce6-2301-3425-af6c-11c1a3a68987 | -2.0655 | -46.356 | 2024-11-10 12:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 9a63f1e0-d354-3aa5-a1d0-167e27a53f8b | -23.9089 | -54.083 | 2024-11-10 12:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 130.7 |
| 881ed759-f290-3307-9920-3b31b771150a | -1.476 | -54.3166 | 2024-11-10 12:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4460a439-86b0-32a2-a2dc-bfad5252ec1b | -3.9485 | -48.1508 | 2024-11-10 12:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 48ff0fb1-8ad5-3e49-a352-4949b9b812be | -1.5116 | -54.9944 | 2024-11-10 12:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 9c4bb99b-2dd1-3e67-85d9-472d93daa2df | -3.4409 | -42.3786 | 2024-11-10 12:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 109.1 |
| e5894bf2-1713-30cd-b72c-00424e6ce82c | -2.931 | -52.7753 | 2024-11-10 12:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5f8ee203-a245-333b-b212-2a02d9bca317 | -23.9095 | -54.0606 | 2024-11-10 12:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.1 |
| 5886600d-e325-3761-8a16-23cdb7f65a75 | -1.5116 | -54.9944 | 2024-11-10 12:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 2fcd73b7-f366-3eff-9e75-822ca71755b6 | -2.0655 | -46.356 | 2024-11-10 12:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 81baa87c-c4e9-3314-baf2-e4322fd1df4e | -1.5299 | -54.9941 | 2024-11-10 12:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| ded07bef-e43f-31df-af76-42fcf0fa79a1 | -23.9095 | -54.0606 | 2024-11-10 12:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 167.8 |
| 4e8babb0-e80f-32c8-93c1-7097d775090e | -1.476 | -54.3166 | 2024-11-10 12:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8777011d-8f91-3c9c-976f-d12a52a1266a | -1.476 | -54.2965 | 2024-11-10 12:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d9e877ce-3718-31c0-9dee-eae7ddbf6d7d | -3.4015 | -50.2801 | 2024-11-10 12:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| dc241d2a-7a32-3e07-9a3c-18e26162a5b0 | -2.6388 | -46.7597 | 2024-11-10 12:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c0d1fdd2-074d-30ba-b74f-c8f574c28cea | -17.5872 | -57.5328 | 2024-11-10 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 2498b859-3392-3443-8771-feab751535ef | -3.4409 | -42.3786 | 2024-11-10 12:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 12928f8a-f592-30a5-be32-6e72a4a80f3c | -17.2933 | -57.4857 | 2024-11-10 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| a1aa5c45-35f7-3084-8304-aa520738d069 | -17.6073 | -57.5099 | 2024-11-10 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 264.1 |
| 5c2eda6f-b759-37bf-9d9b-de1ed0e77f3e | -2.0656 | -46.3339 | 2024-11-10 12:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e697c098-bf88-3a7b-a5c4-2779e296b2e2 | -4.4349 | -44.6229 | 2024-11-10 12:30:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 08c2c3c7-2561-345e-b4f6-7b2fa6c04a8c | -23.9089 | -54.083 | 2024-11-10 12:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| 4d528e3a-de7d-326b-b6d6-b0afad2e6f0b | -4.3979 | -41.8987 | 2024-11-10 12:40:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| c1dc8e32-2653-3e05-9434-1a460e7018e1 | -4.4349 | -44.6229 | 2024-11-10 12:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 604263cc-f81f-35ee-9d1d-0a02c5565207 | -23.9095 | -54.0606 | 2024-11-10 12:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 146.0 |
| 07ac69a7-28a4-3d91-bcba-5280e6911e99 | -6.1366 | -42.5544 | 2024-11-10 12:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 2736bf5c-5c2a-3a78-8a18-76749c90ef36 | -3.1239 | -50.4358 | 2024-11-10 12:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| b3f6a421-444c-3b60-a8ff-a62e91192e29 | -4.0913 | -49.1323 | 2024-11-10 12:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5d488eca-540c-310f-aecf-b76e9834801d | -2.6388 | -46.7597 | 2024-11-10 12:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 65114ebd-10f8-3e3b-ac12-a1f60ce0c468 | -2.0953 | -48.8338 | 2024-11-10 12:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a5ab3d78-cfd4-390c-b9c8-869e95eb5328 | -3.9953 | -46.4203 | 2024-11-10 12:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2edb0d89-051f-34c0-b974-1c6c15d9dc38 | -1.476 | -54.2965 | 2024-11-10 12:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| ac1e6771-b8d5-3206-b12d-e7cb0dfa5441 | -2.0655 | -46.356 | 2024-11-10 12:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 280a89f4-59e4-3c2c-b8f2-59cb6bae69e7 | -3.8877 | -49.1194 | 2024-11-10 12:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8391d23a-6919-35e6-8358-e509d38dabc6 | -2.0664 | -46.0899 | 2024-11-10 12:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9501f085-50ad-35f6-baa8-bbb2eceae7fb | -6.1363 | -42.578 | 2024-11-10 12:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 457.2 |
| 5f513a91-ce52-37b4-8e4f-17ded4ce7645 | -23.9089 | -54.083 | 2024-11-10 12:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 134.1 |
| 8a8b6b57-28d1-334e-a73d-116ca3ed4ef4 | -17.6073 | -57.5099 | 2024-11-10 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 280.4 |
| 2580ab02-3e3f-3e31-967f-f99cfa0774a8 | -3.4015 | -50.2801 | 2024-11-10 12:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 266.0 |
| 03eeba0c-d23a-32e5-83c5-8f0056ff831a | -17.6069 | -57.5304 | 2024-11-10 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 240.0 |
| eb179661-4de9-32d1-8d90-0fcb230f8298 | -4.1099 | -49.1315 | 2024-11-10 12:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e1d1b4d6-3f3a-3068-a046-2ea317d71d9b | -2.0954 | -48.8125 | 2024-11-10 12:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 85bcbe2e-3b26-3bfe-8646-5613e4de9fb1 | -1.476 | -54.3166 | 2024-11-10 12:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 1eac2505-0220-3d3e-aa19-ef1e27ad0c90 | -1.5116 | -54.9944 | 2024-11-10 12:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| f98ae319-3cfe-3f87-bf08-fbc866512aa0 | -17.5872 | -57.5328 | 2024-11-10 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| ffba2e59-0a1e-33fa-9478-470f003820d8 | -4.1246 | -43.5833 | 2024-11-10 12:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f7e63946-04d5-32a0-b21d-e65024977a1b | -17.2933 | -57.4857 | 2024-11-10 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| ca752105-ad41-3715-a7f8-2e288f50942d | -1.5299 | -54.9941 | 2024-11-10 12:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 2f200c8f-d9fe-3afe-a6ff-a48ecff9e463 | -2.0656 | -46.3339 | 2024-11-10 12:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 70c672a5-1702-3613-a354-c761f29e275c | -17.6073 | -57.5099 | 2024-11-10 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 335.1 |


[Clique aqui para ver as próximas entradas](README127.md)
