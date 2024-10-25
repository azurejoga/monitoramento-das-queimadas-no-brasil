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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 692e1cba-614c-30aa-bb49-19ee2536cc73 | -10.7924 | -53.85952 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 67bf91c4-c89e-30f9-ae1a-bc6764afee0b | -10.78854 | -53.86005 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 81487937-5e46-388d-bf32-358783e14a75 | -10.78719 | -53.85036 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f12522a0-fef5-3cc1-9753-fcd32488706a | -10.78469 | -53.8606 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4e26621e-a46d-39ab-a322-ae03ef3354b7 | -10.78401 | -53.85574 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 20642af2-42ac-3572-80d0-2009665eebba | -10.78334 | -53.85091 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d04a7104-d5f6-37fc-b58d-b868e3b956ca | -10.67907 | -55.2318 | 2024-10-25 16:50:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e135c39-ced2-3a14-9f0c-80100f58ddc6 | -11.89892 | -54.25271 | 2024-10-25 16:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 46bc5312-2c69-37f0-85af-95bfe3ba3099 | -11.57588 | -53.9942 | 2024-10-25 16:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4a7907f5-e342-3d2a-922d-cf4133b9e940 | -11.38145 | -54.35869 | 2024-10-25 16:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0b69c68c-1959-30b7-9ff9-6a17003ae0b0 | -11.36116 | -55.20157 | 2024-10-25 16:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 6a45f9ee-ec1f-3adc-9d5a-24cd51798917 | -11.36105 | -55.2017 | 2024-10-25 16:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 11862f8f-0261-3ac9-a0e8-226ffcd64aab | -11.36064 | -55.19759 | 2024-10-25 16:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ecd4fe87-bb7f-3286-bc63-ec70b42866f7 | -11.3605 | -55.19772 | 2024-10-25 16:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| d9ae5804-71bc-3ca7-b4c1-733b3229f6b7 | -11.35155 | -55.41716 | 2024-10-25 16:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 5fec9503-563a-317a-9f8d-b30036a77299 | -10.95983 | -54.08506 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 20611d6f-185f-3447-9f95-6f154037e63a | -10.95912 | -54.08003 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 07f3b201-4af0-3b5d-a6a1-cd335649bca6 | -13.64277 | -54.52203 | 2024-10-25 16:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b0b2fd30-922e-3aca-8121-a2eb471235ac | -12.72948 | -54.98609 | 2024-10-25 16:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 02c65922-61fb-3243-a594-a51411170e2f | -12.61849 | -55.22223 | 2024-10-25 16:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 384ccd6f-8e87-3384-8294-4e9491d3cee4 | -16.55781 | -56.24294 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 5abe4860-9974-359a-9c40-25d30b7f54df | -16.55548 | -56.24589 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| be745324-3e01-349b-9abf-83678e4fa667 | -16.55479 | -56.24026 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 592bce2a-fe1c-3fd3-bfcc-5332322b490d | -15.79939 | -55.75621 | 2024-10-25 16:50:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b71709c7-2d44-3d02-9252-9476136dfc9c | -15.79471 | -55.75678 | 2024-10-25 16:50:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2179c700-bca5-36aa-afb6-99fb94d98f91 | -15.66623 | -55.97921 | 2024-10-25 16:50:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| c1bf2bad-e8c6-36b0-94d5-2d2785467660 | -17.886 | -56.87337 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6364132c-5933-3b43-a116-87e310b09196 | -17.56679 | -56.74568 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d84d6fe3-1fc3-3760-8efd-c9caf0f3e733 | -17.56124 | -56.71526 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 43072aec-95c6-386f-97ad-fffc5b399dbc | -17.55804 | -56.71487 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 9b59d353-0a14-33ca-975f-5f4b61b0c917 | -17.55612 | -56.71584 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 214aa79e-ea61-3901-b02b-68fb0b3a1f4d | -17.55364 | -56.72168 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b2d04441-fe87-3245-b56e-b782d96e7743 | -17.55167 | -56.72269 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cd3912a5-8c96-3f8e-8e43-d3e101c42cc4 | -16.7292 | -55.91424 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 55a90c24-a9a9-353e-82b7-7fe816641558 | -16.5676 | -56.24182 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| dfa8035f-097f-3b94-b620-3773f514440c | -16.56335 | -56.24802 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 3fce38e5-c08f-304a-b7b1-5e0960113cbf | -16.5627 | -56.24238 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 8babfb56-5e87-3073-9839-9bf4f90f1bbd | -17.23144 | -56.67315 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 82a706b5-99e0-3e4a-85e5-232e3e9e0467 | -17.23057 | -56.69713 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 29eefc46-4d54-37cc-ac7e-4d45cd3c0e20 | -17.22904 | -56.69843 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 5719b135-b46d-3a4c-8368-2c25ffde0a7b | -17.2287 | -56.69534 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 80356772-4ae6-3e76-aff2-eea17b745cb4 | -17.22806 | -56.67554 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 5bb35f3c-e164-3a6f-8c71-00b824fadcb2 | -17.22771 | -56.67247 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| fd77222f-cb94-37e6-a7f0-2f3e4e34423a | -17.22669 | -56.67681 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| c642f7fc-a19f-3354-9d9c-1768b219cbaa | -17.22635 | -56.67373 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| fe9f9420-d484-3e3c-b7ee-f4265c28bf26 | -17.22602 | -56.67065 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 687471c6-d33b-374f-a291-12b9ee1591d6 | -17.22584 | -56.7008 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 9286ceab-73e7-30fc-8c0e-8a3e355d808b | -17.22548 | -56.69771 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 06fc74ef-88c4-3471-bbb8-d4f4f50fa14c | -17.22334 | -56.6792 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 95edb126-b921-379b-9098-8e0903a6f704 | -17.21566 | -56.70194 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a2eb5518-720f-366c-8bc7-2740b86d78d8 | -17.21246 | -56.67419 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d0a67231-d423-3011-8d57-7570ea3b693d | -17.21211 | -56.67112 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 6202858d-f5d7-374b-8255-5132b5a092e7 | -17.21175 | -56.66806 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 791ae004-70cd-3649-9b40-8d4802a412b1 | -17.2114 | -56.665 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 7743d57a-f944-3693-a501-a71d047eb86f | -17.08052 | -56.18228 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 1204f20c-c2ee-3805-aed1-8329cef1e8f4 | -17.03664 | -56.01149 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| aff0e1df-1d94-36f4-bbb9-a5c4e0f8b2e0 | -17.02505 | -55.98768 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 88047e62-99c6-3cc9-9ad6-e579384fbe41 | -17.01732 | -56.00529 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| e4bab0da-841f-3329-b0a9-606cf60f482a | -17.01667 | -55.99978 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 73e58513-6e1c-34e8-9988-87a46ff7a2f0 | -17.01247 | -56.00586 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| eda4f378-15b6-350e-88ce-fda2e5b1eef8 | -17.01057 | -56.5559 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d355a5ae-b505-3b98-a557-6bd8c516dbb5 | -17.01022 | -56.5529 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 081db097-77ee-3685-aff5-e471e45deded | -17.01021 | -56.55509 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 96c2d5f1-0921-3995-8b73-62ef0ea21b12 | -17.00987 | -56.55208 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a624067f-4b31-3a4b-93e5-5492240afd44 | -16.98165 | -56.61406 | 2024-10-25 16:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| b73011ec-2001-3a8e-ac4a-e6842f612a14 | -18.33739 | -56.2391 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.2 |
| c28a603c-215f-3970-8ff5-641c66ccc8cd | -18.33672 | -56.23312 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 3b7883bc-3268-3fd1-85ae-2ea99bd01554 | -18.33238 | -56.23967 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.5 |
| f0d1032f-1d6f-368c-8f58-23ca1a25f202 | -18.33228 | -56.14078 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| b9f7100f-c05a-358b-9031-39a9fb028e2d | -18.33164 | -56.13488 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f83bc545-f985-350b-bc48-8430478ea560 | -18.33088 | -56.13762 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 2b15592d-37d9-35cc-b768-265470f67ebd | -18.32738 | -56.24023 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 3aa21059-2a97-3830-b80e-41e63ceb2884 | -18.32266 | -56.19849 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.0 |
| 6364b58f-08f0-3de0-8f78-fe437da4952d | -18.31863 | -56.16293 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 126dd034-15e5-3a2d-bd80-97f684c4f595 | -18.31565 | -56.18124 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| c957d745-876f-3acf-bcee-b5b5754f529e | -18.31499 | -56.17532 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| e5c4135e-c862-3d70-af5e-603db185c1b9 | -18.31432 | -56.16941 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| dc1fbfda-1a36-3b3e-820d-1dbc6da6a5a7 | -18.31301 | -56.24793 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.6 |
| 65465f51-df68-3123-9906-859782cceb8b | -18.27736 | -56.01965 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 20407596-e9c3-32ed-ad31-6c9dc8cd37e9 | -18.27243 | -56.0202 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| accbd2fc-9069-3912-a57c-08625a30ead8 | -18.27178 | -56.01442 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 3ada6478-2f10-3260-ae41-ded607e75c0c | -18.27113 | -56.00866 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 1d80711c-2110-3877-b40b-c90a48d0ec51 | -18.26749 | -56.02076 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| d8f05b97-b5c8-33e7-b9a9-96e68e098f1a | -18.26685 | -56.015 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 4f4e9857-d05d-3942-84a1-5654c024d82d | -18.26556 | -56.00345 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| e1b798bd-c8d6-3647-8d39-713dd9897b03 | -18.26256 | -56.02134 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 6bd291ca-04a5-36d9-bc34-e8f5ff5b3e99 | -18.26192 | -56.01557 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 30cb87e8-b67a-3d0f-9cf5-454e32b22ca2 | -18.26127 | -56.0098 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| bca1e2a1-fec3-3302-b265-e8a59562bdb9 | -18.25891 | -56.0335 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| a12eac49-b638-3602-bd38-01b3f6ccd6c9 | -18.25763 | -56.02193 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| af862beb-90be-35bb-be1c-bd5cc4a06f9d | -18.25699 | -56.01616 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 42e79295-7494-3ea6-9a4b-71641fb72211 | -18.25333 | -56.02829 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 2b350408-9868-3d8a-a5e5-fee78611d726 | -18.25269 | -56.0225 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| e740da99-793e-3cd0-9c4f-3fb5e0695e41 | -18.21576 | -56.61304 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| bbce38d1-a7c3-3489-85ce-586d8e89fa98 | -18.21542 | -56.60989 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 3b7a50d1-1a1c-3197-b8f6-c8ee0f770492 | -18.21063 | -56.61361 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 0f6ebfad-7534-35c0-8cf1-8bcc6970fba9 | -12.02732 | -57.08544 | 2024-10-25 16:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 9d936047-a2b4-334f-a059-237ca61dd00f | -12.02661 | -57.08001 | 2024-10-25 16:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a0774f7d-f830-3b0c-9790-b8452a6a2542 | -12.02622 | -57.08788 | 2024-10-25 16:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 56e99f61-1ddd-3fad-b223-71c4d458f0a8 | -12.02555 | -57.08242 | 2024-10-25 16:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |


[Clique aqui para ver as próximas entradas](README134.md)
