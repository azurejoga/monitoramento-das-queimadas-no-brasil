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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 879a9e5d-20c6-3e07-a1d4-aa6224d2c10f | -6.71194 | -42.80205 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bca65692-6a74-3fbb-b043-2aa1d6d58d6a | -5.77966 | -42.92035 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 56d6982d-e86b-3cc0-a424-5465f68a1933 | -5.6618 | -42.74263 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a64cf629-2919-3aeb-8241-54b785056eb6 | -4.69987 | -46.47876 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7784d223-1935-39de-ad4d-1c69c5e5078e | -5.51575 | -45.16511 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3612dfd3-90a6-3f5d-b8a5-40d05b3e55d7 | -6.99657 | -42.30891 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99eb746d-a0f4-35e4-a3ed-864e1b6b5f63 | -6.30673 | -46.3352 | 2025-10-04 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be7b79c1-0b88-3183-a4ee-3ca5bacf4698 | -5.23157 | -46.21909 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50a2a5d3-1a30-3824-936c-83b8d7dbd0f9 | -6.38794 | -43.60591 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c5c9914-71d9-3434-8320-bef1937663a5 | -7.78307 | -44.12686 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5563d6e9-b797-3a17-a0dc-93b36a1c5d7d | -6.65059 | -41.95583 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c59925a-1e74-3892-93d6-18a6abc37206 | -5.65682 | -42.73124 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| bf64d202-3024-359a-bee1-3fe01ffb9c3c | -2.248 | -47.87754 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eadbde09-8354-34ed-9ca7-b378bd06ab31 | -6.36764 | -43.90394 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5df867d9-42a7-384f-b2f1-6f53952e8b2e | -5.69684 | -49.31165 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a1b5639-ba3f-3184-a6a2-f27f33527f3f | -4.4271 | -43.24488 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48177dd1-60ea-3860-b726-cd38901bdd73 | -6.36934 | -43.89334 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51322911-1275-3ad8-9a5c-30c22c7dbdee | -5.8571 | -45.85252 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a999e729-8935-34d5-877b-d74a7b938c15 | -7.34422 | -39.17287 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a158684d-30f1-39b9-86a0-49384cf9f12a | -6.28134 | -44.04183 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acccba07-327b-3602-acd8-0febd8f712aa | -5.68901 | -42.84944 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6b094131-f75e-3f57-bbd1-b4742a7874b2 | -2.25161 | -47.88221 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb885af4-294e-3b62-b8cc-434e74749f5c | -7.31005 | -47.30637 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b32060eb-9878-30e8-9af0-917be3c1d17c | -5.61131 | -43.23361 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b06b34d5-ef8f-3086-82a9-8d8e7a650b58 | -7.78416 | -44.14139 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d855a788-9b84-3df5-9244-55b5e3cbb7bb | -2.81366 | -48.614 | 2025-10-04 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44550736-26f5-3def-a7fc-c570e4876d15 | -6.6673 | -44.19822 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fda4febd-29e3-3f6a-a68d-a716878c2c1d | -7.75498 | -42.53845 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2dd2695d-7afa-31b9-a508-de91b47b48f1 | -6.13725 | -43.81372 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d52426de-497d-3ed7-818b-0daf441f502a | -5.23299 | -42.89762 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1db03ee6-cc87-3b4f-bc1f-ef95c93a64b7 | -5.30959 | -43.10015 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6fd2b17-bade-344a-8c7a-4e9d85fecd04 | -4.43374 | -43.24593 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43380c55-6944-3b0d-a31e-bbd5c8dff815 | -5.73834 | -42.92445 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1e571d9e-00f1-3266-804d-e668084b003c | -5.75047 | -42.93344 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e23ff2c-af72-31ec-83ca-d9446b27a2d4 | -6.53035 | -43.37233 | 2025-10-04 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5df2036f-504a-325f-b9f0-7955fb602d97 | -7.78639 | -44.1274 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0efbd7d-9d8c-35e2-b410-50bd8e5e5d30 | -7.56424 | -42.63004 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1575f50f-60c4-398e-8d32-7657e71a7605 | -5.608 | -43.23307 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad6b6099-1388-3668-b953-0afb7740d4ab | -6.30452 | -44.4489 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 050f5b25-644b-36d8-91fb-3750cd47d325 | -5.17385 | -46.18481 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a212339b-3f42-3a51-98ae-f310c408fb59 | -5.65904 | -42.73867 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c61a5fb8-e138-3cd5-9ec1-15785c838706 | -5.45825 | -43.17002 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b10d1815-0ce6-38d6-b75b-00243948fafd | -5.23092 | -42.97508 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c76151ce-88bc-3c1a-945e-0d366317ae63 | -5.48334 | -44.10195 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f515735c-b3e7-3a3d-a2bd-b0386dd6c13e | -5.93369 | -42.89133 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7784f0e2-d9b8-3fc3-a0f1-61dbe655f639 | -6.278 | -44.04127 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7dbf0386-1d2c-3898-b8b1-d2bf784fc246 | -5.75654 | -42.93793 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bb9caeb7-1096-3acf-8deb-a358082c4969 | -7.56146 | -42.62602 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a46abb8f-3e0b-38de-b16d-09b8caaf3842 | -5.94924 | -42.87967 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c776881e-1f7d-38b6-9ada-8beaa1363805 | -6.55471 | -44.15843 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 322eae05-bace-3f19-97bb-7243795bdea8 | -5.96317 | -43.49935 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52ae1e76-a09b-3805-ad69-a569c6d681fb | -5.70672 | -42.88758 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 991df5a3-de9d-3314-926d-0f944a00e8c4 | -6.17661 | -44.28798 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 171eca13-16e9-317b-8a60-2075c0a692de | -5.98641 | -43.48159 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4104af65-95ef-3876-a08f-0f8137c65966 | -5.8367 | -42.88315 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fb030b19-c7ad-3771-9d4f-f97f346e45d9 | -6.77141 | -44.81769 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12595530-da09-3f2e-adbc-fc011f942767 | -6.24523 | -45.33703 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5731ddc-18ce-3b94-821b-795e9a405c62 | -5.87977 | -44.887 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7162a928-3f75-334f-8da6-eeaef26b4512 | -5.60855 | -43.22962 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93b11aa8-efdf-3b05-986e-c10bac4d5257 | -6.99273 | -42.33342 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b14ae787-32ae-325e-b2e3-e12f525d170e | -5.48671 | -44.10248 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5d61fdfc-574b-37a5-a33d-72e78b6e56b3 | -6.28634 | -44.05352 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 236f940e-6649-3c04-8622-8699d4470da9 | -5.74055 | -42.93187 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e72c6a8a-fb6a-36d6-8cf5-e8772c729eda | -6.98765 | -42.79943 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 684615ee-8cea-3f8a-b6fe-84cf1dff8106 | -3.68959 | -50.88947 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f711b19f-a8de-324e-b51b-8d196985cf03 | -5.78884 | -45.7836 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9668d50-7aa9-355f-b2d2-ce0b447d9cbd | -5.68571 | -42.84892 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 34ef55d7-be3f-377c-9680-eaae4950dc5f | -5.95157 | -42.95079 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 30fb3a06-39fb-35ee-af45-983d6bbdcd2d | -5.7788 | -45.77765 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4107b64-1c08-30e7-a826-3c0671dc3ac3 | -5.80737 | -42.72313 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a6c44ecb-5649-377d-b557-dda6116602ea | -7.89497 | -42.60017 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c166a1d3-75b8-3b34-9bab-4f3544d826e9 | -7.76103 | -42.52147 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27db1059-c051-39a0-be65-eb0be76be6d4 | -5.40929 | -41.32045 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d94ad06-4c34-3eb2-9148-bc93f73905b8 | -6.7114 | -42.80551 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c61bf462-5be4-3352-a730-71e826752fa5 | -5.46545 | -43.16764 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d824434-4a4f-3a32-92d0-58017e312088 | -5.97605 | -45.27268 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36056ba1-31bb-394f-b7fd-0bac1737ddf9 | -6.98996 | -42.3294 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59e52560-353c-3904-b26e-c446b0961ed4 | -5.63885 | -43.18834 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cfc929e4-71e8-3f76-9609-d812de1952ce | -5.45549 | -43.16604 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 994d8fd2-aec9-3e95-a288-dee84d149874 | -7.25223 | -40.59267 | 2025-10-04 04:12:00 | NOAA-20 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69bc0490-a962-3f46-9d7c-8b11ef61a95c | -5.93148 | -42.88391 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ef19dcdf-e486-3f60-9e37-dc47d284365e | -5.47604 | -44.10447 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56afb001-154c-3c30-888e-069e2b173860 | -2.25225 | -47.87827 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14dd5fe3-f4c0-3942-9ff8-b4905c31cfa4 | -7.64717 | -45.4748 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b27c98fe-642a-32e7-a689-172f8a5c2032 | -6.28239 | -43.62808 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47476a6d-3df7-3679-a580-7b80c8427d60 | -6.71321 | -42.16392 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 481c1375-47ec-3331-b30a-664e7515e702 | -7.78058 | -42.59272 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6d60f40d-887d-3cf1-b3b8-fc8e5f7d3e99 | -5.74164 | -42.92497 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 810d7caa-667c-3d41-9b28-976490ed016b | -7.71776 | -42.56135 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8ab5072-faef-354c-98af-246babada072 | -7.31325 | -47.28741 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 676d6617-b03c-37cd-bfa8-c0c3d9e7719b | -5.55944 | -43.26093 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa689635-ee7d-3662-805c-0cffe26c5cc1 | -6.46191 | -44.58533 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4e9e893-f360-39a2-8bd4-1b4a6965ebcc | -3.84699 | -41.58197 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 370e71ec-33b8-38bb-bd68-1841f570bacb | -5.6816 | -42.72453 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ac1ea18-95c4-3d6e-a53c-790e8d33d585 | -6.87961 | -47.23393 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e8b770e6-f7a9-38ee-8c6d-318de4fe045f | -6.64669 | -41.95892 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 998d5707-38ea-35d1-8276-701ce6a0b637 | -2.90104 | -50.73172 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aca3d7b8-c29b-32f0-8b12-a2cf30b258db | -7.3564 | -44.34829 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78c9d1bc-3110-3a2c-976f-44cd45012486 | -5.83358 | -42.87932 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84777820-a7b3-3f68-bc81-6d4f59935818 | -7.16331 | -44.99744 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README65.md)
