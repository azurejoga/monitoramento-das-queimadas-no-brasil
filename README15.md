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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adbd064c-4365-3535-8052-c03d62f6cd55 | -10.30774 | -57.14284 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d70815c-4533-320b-8a7b-b0cf784ba559 | -10.81478 | -56.61425 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5863c038-8113-3e4b-bf0b-c9844c0edbe4 | -11.90946 | -57.10719 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7ce7b08-60c0-3c56-81cf-63e9ee3fa589 | -12.18393 | -52.88449 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 18638964-c84d-3a89-8ad0-9328f6716ec3 | -11.93536 | -58.63371 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7d34b9a-393a-30f8-a610-e25d1bea2b66 | -12.17651 | -57.14774 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d429d66-ec0c-3651-85f9-478bd629500c | -12.20004 | -52.88184 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08c8694a-8f82-32ae-b12f-12b1e232e1fb | -12.09181 | -52.01171 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df78166d-aa5f-3c0c-b543-4a11c387faba | -12.19129 | -52.86834 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e66b6237-bcd8-3f97-b903-7da74a68a927 | -12.46132 | -58.4955 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b5274aa0-ea73-3a24-a2ee-cbb5e4ebed5b | -11.52709 | -54.79465 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9d06d064-28a2-3f57-88ad-bbe91719f142 | -11.92254 | -58.65898 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d76fc3e6-6578-39b9-90ff-facbaf15da5b | -11.93398 | -58.6348 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93a15389-97cc-3ca2-b3bf-fd99ea7b2a24 | -11.21437 | -54.32999 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97821ecc-0dba-3d00-8824-1adaae48358f | -11.66315 | -57.25935 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8480d6bb-ae4c-3050-8ce4-935f6e5603a5 | -12.19192 | -52.88867 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a29c1b28-611a-3344-843c-7598a5a3f1b6 | -12.17591 | -57.15146 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b77441e3-318d-3db9-96ba-e2c57f6a8c22 | -12.1777 | -57.1403 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0a0336-1324-3e20-8611-ec065555b557 | -12.18958 | -52.88022 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6207b54f-0709-32ff-a140-ebff10728892 | -12.18452 | -52.88054 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92a41f25-ea60-3825-aa23-2dbd6d9297f3 | -9.09115 | -59.39155 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc5525de-8664-3039-af80-70343937b5f6 | -12.77466 | -59.00303 | 2026-06-28 04:59:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2940714c-a04d-3147-8100-e8410cb0e9e6 | -11.21144 | -54.30445 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| c98e8348-2539-32e0-8755-6dcb619756aa | -12.20353 | -52.88239 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eda8e4d5-eaab-39f4-9296-dd4d47b8e3c2 | -12.62112 | -57.8891 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f3318d3-f16e-3340-8aa9-56b31bfce69f | -9.59067 | -56.92657 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24ef75c6-e38a-331c-abc7-adcdd3fc7a5f | -12.45846 | -58.49072 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ff60b5f-1529-3c5f-ba99-470080d3ec1f | -17.30418 | -42.6602 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fe607679-bf3c-3470-9d13-bcc2e6833dad | -12.58464 | -57.81575 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de9dfa62-df8d-396b-bf95-28cc1d5ad08b | -11.21706 | -54.31229 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81df7222-81c3-376f-bd2e-f7a3839d0b1d | -12.17311 | -57.14719 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a755ec7a-702a-3cd6-92c9-f07519dda88b | -10.78339 | -54.10253 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7191275-16d8-3fc9-80be-4b6c7bb9ec66 | -12.18309 | -57.15618 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 963d3f28-78b3-359d-85ce-6584983c9303 | -12.0942 | -52.0208 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66d3314f-948f-3e2a-904c-e1cc26a75746 | -9.08375 | -59.41097 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 67594ea8-3b26-34b2-823f-ee8c626f32a6 | -12.08392 | -52.01492 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6b7de4c-05e4-38be-b6ec-da6b17b591d8 | -12.05019 | -55.45693 | 2026-06-28 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01003d0a-caa9-368b-83de-e1b4b23cbd8a | -12.98904 | -57.77105 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 705ba2f5-99ec-3b35-ac84-9239e292e72f | -9.08339 | -59.41395 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 084065ec-591d-33cb-98ba-e213b2541767 | -11.5304 | -54.79517 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0fa257e-2eaf-3b03-9f5e-89943550cb79 | -11.94982 | -58.61429 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00046f28-c7fa-388e-b516-fde8db9670f0 | -11.92184 | -58.66325 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 909ec019-c6d2-3ff1-82cf-31b375d5130a | -11.87297 | -57.8191 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70a29990-931b-38b2-a083-c9c670b1e88e | -14.63673 | -54.46083 | 2026-06-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15f1028f-79e3-36f1-b175-b4734031cce0 | -13.89219 | -47.17582 | 2026-06-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc3454d0-2a16-3357-8e26-fb905f567e90 | -11.20945 | -53.82419 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a1aba50-dd87-3d28-b8d1-44b3679ff3aa | -9.08855 | -59.40657 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f209507d-b128-37e5-96bd-73ad47773f6a | -12.19267 | -52.87372 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e3370b0b-cb84-380d-b3b0-c94be4b053b3 | -11.94188 | -58.61731 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44219371-f364-3da5-8245-49e820444a2d | -12.17032 | -57.14291 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c97c7e-aa1e-3c28-b0c2-dc7523320e50 | -11.9108 | -57.14182 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 960b997a-016f-3071-8113-27b88c656db6 | -9.03302 | -61.32837 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 494da75c-e752-3428-9464-aecf420c9dac | -12.94428 | -56.64508 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba7780c-e88e-342b-b928-9e65393d00eb | -12.20061 | -52.87789 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daffae22-365b-3024-9333-deab5ee4c286 | -12.18742 | -52.88504 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a346e3f7-fe31-3246-8c6e-f60f17725426 | -12.19535 | -52.86492 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a26feb36-98d2-3b4c-a079-cb8cdf89c0e3 | -12.17251 | -57.15091 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c6f50f4-568c-34ba-ae91-ce43ccf6a070 | -12.18673 | -52.89998 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e09ad48a-46b7-3b42-a00e-9dd158ddc166 | -10.93807 | -56.85627 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4d9aad7-1a20-3e79-8d18-6652e315fc15 | -12.18507 | -52.90081 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0219752d-8a41-38ad-ad3e-a89807efc747 | -9.09292 | -59.40515 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 392e9fd6-ed43-3b3f-8ebc-deec5a3064b7 | -11.2176 | -54.30875 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eaba8052-8c87-358b-9a22-0a0e48b95672 | -13.29595 | -43.54968 | 2026-06-28 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1ba2ef7-a950-321b-814e-ded2784356d8 | -12.62739 | -57.89423 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6a6b357-c737-3773-b095-332b47125468 | -12.17371 | -57.14347 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ffd264-ea89-3505-8b32-66035ac4da42 | -12.1781 | -52.89974 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99c8ab2c-7129-3494-8878-91a30b3f7372 | -9.08816 | -59.40953 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b969ba9b-5ab1-3d83-98a8-f31fbb403ec2 | -12.60843 | -57.88786 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bceb7188-e5f3-3b36-86d9-52ea78316635 | -9.09065 | -59.39445 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 420fa0b6-c48d-38b9-addf-9ba410f6b0c0 | -12.6056 | -57.88336 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5627377b-d720-3b02-96e6-da708f659327 | -12.17092 | -59.75452 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e8cdeb7-cdc0-3cd2-b4ed-b1352902ace6 | -10.30333 | -57.12647 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0a61e941-2eea-3a0f-85be-ede4b4bd78b9 | -12.28665 | -57.55294 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bdeb40a-3904-3550-a60c-152289505136 | -12.46419 | -58.50029 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b33e0469-aca2-3db4-8686-dcc0908c0df9 | -11.60645 | -43.1103 | 2026-06-28 04:59:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8e810b76-eeba-3c9e-8677-f432af38fdf7 | -11.32212 | -54.46994 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9a23c8c-5a80-320b-a938-8ab432031a19 | -11.90365 | -57.1215 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c53cde-6acb-371b-8953-27e917577798 | -12.60725 | -57.88679 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c8b0dda-cac8-318c-86a2-3b808e34b1c4 | -12.20817 | -52.87499 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 98edb4fa-a23b-38ec-9b1a-bc3a502e7293 | -12.18709 | -57.15302 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a589713b-9b21-379e-8131-545e7b8b7145 | -13.29343 | -43.55076 | 2026-06-28 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd5ee9cc-f726-35ca-883b-d3f35277b7b2 | -9.09457 | -59.39513 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f45b6101-272b-3fd4-8273-3b609b83f358 | -12.98841 | -57.77489 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa47a574-cb05-3c9b-8541-a727ddd7f44e | -12.19249 | -52.88472 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92edbdfe-047b-36ca-8a92-9a11e6f82fe0 | -12.18334 | -52.88844 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 636ea55b-6519-3ef1-bdbb-8abaf7fe961e | -12.05073 | -55.45343 | 2026-06-28 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcdc2ef-6249-3d26-ab04-ddb2632c60af | -12.18209 | -57.15631 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a72f87-b3fc-39fa-9878-8fbcfaf3c727 | -12.45776 | -58.4949 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 986a98fa-b49a-3088-a32b-d6abc7fce762 | -12.98433 | -57.77815 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c941086-6217-338d-b95b-c886da8f328c | -16.04136 | -50.55852 | 2026-06-28 04:59:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daa5f0b6-06d8-3b56-ab17-24b3a394df30 | -11.22006 | -53.82215 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 55885d44-9a51-357d-a689-ffcc34d81058 | -12.18276 | -52.89239 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 581fef42-c060-3f0b-a314-c1af7e64ecab | -12.16594 | -57.12691 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504f7e11-63a4-370e-a33a-a03f8543ae47 | -12.19306 | -52.88076 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b617cce3-1636-3ba4-8b8d-f439525931f1 | -9.59875 | -56.9201 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fd661ee-c54e-351e-9cb8-52fd776ebb7c | -12.19662 | -52.90552 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce75f848-528e-3e55-8cc9-652082235677 | -12.23455 | -56.54986 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bc8c9cc-0298-394e-b35f-5c0784ce8e18 | -12.18965 | -52.90446 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d5ba596-01de-322b-91bb-db4e6f643e37 | -12.09567 | -52.01563 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bc4f117-99c9-32d7-9c5c-9fc81df3bf12 | -11.86319 | -57.81338 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
