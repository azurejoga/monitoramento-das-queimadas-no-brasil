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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1955578-24ee-3538-b83f-524259967d2d | -5.65229 | -42.77722 | 2025-10-11 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 850b8aca-a3e8-304d-b448-1913cfab61ad | -3.55474 | -44.42514 | 2025-10-11 04:32:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9645e25-9a29-3a86-85c5-8a3f7df8631e | -8.0075 | -44.44852 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e1a0d91-67f7-33f9-924b-dd0ec652be42 | -3.12057 | -49.10026 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 869c6785-7e03-3e62-afce-b2c22ca3f5ed | -7.53166 | -44.2932 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9696229a-d125-3b58-9027-1442bd6be6fd | -7.34707 | -43.85694 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a819bfee-e984-31d4-bfba-f1420596182a | -3.39146 | -50.14997 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50454d9-f9b3-3d99-96eb-a779ae91f5ac | -8.53148 | -44.59838 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b954db7-62ad-393a-9020-301609731b9e | -8.4074 | -45.08879 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a79596cf-d778-3615-bec8-1276a773e910 | -7.66841 | -42.5732 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| db2b9ee5-73a4-33ba-b6ed-1039cd349a49 | -7.14487 | -44.12817 | 2025-10-11 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fca4b9c9-f727-3a17-b93b-4987071bfa10 | -5.11866 | -45.68772 | 2025-10-11 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41b9c4e1-c950-3e37-8e47-30d869519ac6 | -3.72898 | -48.35809 | 2025-10-11 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddff8ce2-0435-3297-8d25-7e8c3f59eb1e | -7.47078 | -46.73217 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c7e8b3b-b05c-385e-9192-a6aefac1e005 | -5.59177 | -41.09954 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b01b0d1b-2096-3951-8dc2-5db25e85fd5a | -7.98871 | -44.47297 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37eae19d-6a34-347f-bbc1-c5616000246f | -7.14659 | -44.14265 | 2025-10-11 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e88f0f0d-cb0e-302a-bb49-97b635787245 | -8.20381 | -43.32473 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 8166be08-f8a6-3d38-b480-f7ac2ab9e823 | -4.89067 | -45.95605 | 2025-10-11 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ebd0cd8-67b1-38f8-9c49-2f59982462b4 | -4.42734 | -47.59936 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d9c954f5-56c8-3b42-b0f2-e0ca9c49eca0 | -4.53306 | -38.46421 | 2025-10-11 04:32:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| efd4cd28-356e-3893-9275-62522357d5cc | -8.11562 | -47.22477 | 2025-10-11 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f84be2f8-cac0-3e57-9c9f-316551301920 | -8.21941 | -43.37318 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86049256-8def-3b1d-9ff3-9115adca40cd | -7.86245 | -44.46464 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25a432a2-822c-3e1c-b12f-ce8426426d50 | -5.48162 | -43.40637 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d6d12662-4814-3752-8d5a-1c105eb87c3b | -7.79551 | -42.60111 | 2025-10-11 04:32:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ddd7ea12-cc3a-35bf-8185-5a7ef7b6399d | -5.61579 | -42.57032 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 64047693-88ec-36a5-9ed4-362a1d2da2b7 | -5.74507 | -43.37417 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c876ccdb-5823-3ea0-901d-6894d3052aea | -4.98539 | -48.42041 | 2025-10-11 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7592d11-e364-3299-aae2-685cc7c9680e | -8.53519 | -44.59896 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5906705e-2f28-395d-aff6-90e8305faf06 | -6.83193 | -42.7983 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b9aae0f-cc47-32d0-9832-f34d0ab871ff | -7.2585 | -44.09164 | 2025-10-11 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c5bce5f-d8d8-3c47-90ae-7903a1374337 | -6.04645 | -42.50443 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e38cea59-c0e3-3253-9c16-d7a1ba6c2956 | -5.8586 | -42.84698 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| de242ef3-613e-3203-b5a7-0be4a3b901e7 | -5.36645 | -48.35603 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f32f44-841c-3b78-947b-bc00a2981613 | -8.56723 | -44.61318 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c97c35c9-1a57-3b1d-9f3c-6512aff6795a | -6.31585 | -45.79866 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16095dd9-e81b-31d9-9df8-74b25093cef2 | -6.19067 | -39.69354 | 2025-10-11 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8724b80-f727-30f4-a9c0-f226c89065f9 | -6.7577 | -42.82117 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 45e5d58a-f843-3c89-8e3f-d70c26bbe89c | -5.90975 | -46.24744 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 603bce61-561f-3fab-8ea4-cc9c4f864c70 | -5.87417 | -42.82447 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a1a1600-9edb-3f06-8243-ad026573824b | -6.91833 | -43.58313 | 2025-10-11 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e4b63b2-859d-34d4-b5b0-8c592bc4e637 | -7.21569 | -39.90556 | 2025-10-11 04:32:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4ec526d1-d5d6-368c-a830-50d58012b614 | -7.40229 | -45.92085 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9610b699-243d-3558-b710-cbbda0aa0afa | -8.2122 | -43.35098 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b32a899c-1265-33db-850c-1b4e4596e3bd | -5.87918 | -45.29865 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ec5b3c1-d1bc-31bf-97c8-a26fc97b8b05 | -4.19675 | -46.8064 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c6da4a0-f0fa-3dce-b078-9c37c6937e70 | -6.64044 | -43.97465 | 2025-10-11 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cba77828-3c1e-3b0b-80a1-f95cd1e2060d | -7.79784 | -44.18956 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0b3354b-edec-342f-a0de-e61dff3a1491 | -6.66658 | -41.37655 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5398ce5f-0a6f-35c4-9e3b-99fbf5e60abb | -4.65805 | -43.41917 | 2025-10-11 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b6fff3c-edd6-3581-8155-1876c319cf51 | -2.80627 | -49.13196 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f83b235c-2759-360a-a646-1aaeda7d2304 | -7.57451 | -44.94914 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 898b32ec-5ac2-3980-9219-1b68fe45f393 | -6.87734 | -42.3956 | 2025-10-11 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 82790e92-241e-3dfd-9112-adab9137a376 | -7.35158 | -43.85284 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 960ce275-3265-34b0-9bd5-7e01cbe88f71 | -7.86354 | -44.4832 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc0af314-31da-3590-85c3-7f913f7caca4 | -7.70603 | -42.37524 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1aafcb97-4d39-3333-b0e3-2841ce02e1f8 | -5.83562 | -49.02464 | 2025-10-11 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bf2e604-aacb-35b8-8437-45cab5a1d1c8 | -7.80241 | -42.42826 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3eb2cd61-355b-34e6-af89-e7baf3f91663 | -6.75368 | -42.82042 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ed712068-2b43-3d4a-bd1c-0f68e6e32f6c | -3.33402 | -44.09676 | 2025-10-11 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f86f474-8d9b-39bc-bd45-78fe65545e3f | -7.78128 | -42.9686 | 2025-10-11 04:32:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f29149eb-c30f-3351-b627-a8e9c48bbd69 | -4.91011 | -48.55205 | 2025-10-11 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc39ff43-f78c-3b3d-9872-f5a4f05d78d4 | -5.86207 | -42.85106 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| c1a4369e-620b-33f5-84ad-ed5aadcfe222 | -8.21567 | -43.35509 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5b6e5fae-85f5-37d2-8a11-fdf9ffd910df | -6.16866 | -42.55185 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c38ca9ce-b663-34d3-a76a-dcd78cc82a11 | -7.32539 | -47.82195 | 2025-10-11 04:32:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4940af74-5bf8-3b5d-8cae-6ef903fc2e04 | -7.79666 | -44.1176 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76f119dd-30a3-3af4-9aa2-96b60439cf69 | -2.26986 | -47.85333 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6a0fe34-fa04-3c88-a09a-42afcc6228bf | -6.75419 | -42.81694 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 829242d0-95a1-3f96-b6d6-54ce7c27a7bd | -6.10595 | -42.55298 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 283d17d5-f99e-3ede-94d8-aef71f539611 | -7.58115 | -47.20679 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dc4afb6-7b31-37d4-b2b8-bad733dcc5bc | -7.38225 | -45.17468 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe03f4ef-cacb-3f25-8790-970d01295829 | -6.81022 | -42.97591 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 78b6b977-a13b-3d1f-8430-8cb24a1f2a3a | -7.85934 | -47.10168 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad644e7b-df1a-394d-8db3-c9c0044b9425 | -2.54703 | -47.80095 | 2025-10-11 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54a30f7c-6462-3101-8f2c-74dd5c54e8ff | -3.983 | -46.27792 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 257ebeb7-d032-3fa4-8894-904ed9c04066 | -8.05214 | -44.11784 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12c7ae9d-2de9-30e7-b1b5-020e19912b78 | -5.6838 | -47.90042 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c667e6d-8622-37f5-b118-711969a84f08 | -2.94618 | -49.33802 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab819f4e-2757-37c4-b937-ee3522499543 | -8.2199 | -43.36969 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42e10536-f2fb-3ec3-967b-22059b966e85 | -7.12189 | -45.91847 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b74f62b8-bafb-31cc-92bc-f1d06bb2c184 | -3.77517 | -49.13742 | 2025-10-11 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbdc0b9d-60bb-337a-be65-8c9a03cd221a | -3.81309 | -50.21356 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6f50d22-c637-3230-85a1-a589b0720891 | -4.40532 | -43.47239 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4144fc4a-121f-3552-a1a6-4d75bd54cae9 | -5.18852 | -37.65702 | 2025-10-11 04:32:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98617275-e990-3712-98e2-3260d064f33e | -7.65841 | -42.58346 | 2025-10-11 04:32:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1be2f386-69d6-3dd4-9fd8-a3ae34f5b572 | -2.26377 | -47.84882 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9639b17-d1d4-3525-a1ee-c6a247057202 | -7.21607 | -39.90272 | 2025-10-11 04:32:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7078f0cb-9115-31ca-9948-42bd1323b84a | -7.40866 | -45.92176 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44341721-9681-3edb-ba33-e4f3fa2e73de | -7.48891 | -43.0582 | 2025-10-11 04:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83e5b913-2926-36f8-935e-9d34a44b8602 | -7.46099 | -46.86227 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ce351013-1803-350d-9395-cd17d6f0f893 | -2.26709 | -47.84934 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0be68dd2-21b9-3140-92af-7f7504c976e6 | -7.5296 | -44.29546 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1003409c-dddd-350a-9015-7ac248c988b8 | -5.72534 | -44.51588 | 2025-10-11 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9afcea1-a956-3721-b571-efcff39d7581 | -6.22446 | -41.57926 | 2025-10-11 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 212dd8f1-1a6f-36c6-a01a-1c972aab38e4 | -5.40303 | -40.9765 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa28e83b-bbe1-3ec3-bfc8-8be7cb114a6c | -7.66313 | -42.58027 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2ddce7a9-58e7-3615-b7f2-fe2f375b1126 | -7.2153 | -39.90838 | 2025-10-11 04:32:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ca6374ea-f768-3ad5-b2af-81db069d0abd | -7.66898 | -42.5693 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README19.md)
