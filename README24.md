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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bf554d4-e9d2-3c22-8843-e77ac972afae | -2.90874 | -48.23212 | 2025-07-03 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 002722ba-d760-3781-a8c5-44892a21c825 | -9.16957 | -48.77245 | 2025-07-03 06:05:00 | AQUA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6fe03aae-dd5b-33b5-8ad8-a75a7c2ef835 | -10.29751 | -57.12142 | 2025-07-03 06:08:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 01abf690-7d40-3100-a977-46670542a8ca | -11.64124 | -48.07167 | 2025-07-03 06:08:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8f40d0f2-ef5d-35cc-a3f3-48f83f95c796 | -13.43179 | -47.81209 | 2025-07-03 06:08:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cf0869b7-4a3a-3747-bbd9-ab28d513a9a8 | -12.42558 | -50.02331 | 2025-07-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49912fc3-0ab0-3f6b-b147-db0e0684a779 | -18.21014 | -51.349 | 2025-07-03 06:08:00 | AQUA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dd746499-13e1-3c51-91b9-e6c7e1920522 | -12.57129 | -48.88373 | 2025-07-03 06:08:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6a0c67a-a58b-3c86-9918-e2aa319c58e8 | -6.9605 | -42.8816 | 2025-07-03 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 193.7 |
| d91d1a83-26ae-38a5-92be-8d4b25309e74 | -6.9416 | -42.8834 | 2025-07-03 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 1b9b2cef-811b-33df-ab13-737eeb30c1f7 | -18.65916 | -55.73895 | 2025-07-03 06:10:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7d928078-4bde-35a5-81e6-bcfba459e953 | -18.64989 | -55.73731 | 2025-07-03 06:10:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 22fa9a12-4915-3fa9-bc37-a70fda904140 | -9.63183 | -61.4654 | 2025-07-03 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a68ef6a1-8b86-37d4-b1eb-1c3e39ea9ae2 | -11.78312 | -64.98446 | 2025-07-03 06:16:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0db3d654-77a2-376e-a90c-92894e6895c4 | -9.51516 | -65.5863 | 2025-07-03 06:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3c6b9cc-e1d2-36d2-aaaf-bd0d67bb3628 | -9.22336 | -67.9066 | 2025-07-03 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65821e34-3da4-3562-a55a-97edbac7cdeb | -9.51476 | -65.58925 | 2025-07-03 06:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d1ceb5e-0436-3189-9f70-015e03f0868b | -9.09016 | -62.66927 | 2025-07-03 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7237a21a-0099-3c0a-b686-833bab19615b | -9.63254 | -61.45959 | 2025-07-03 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cdfeb6b5-8bd6-31b2-bf72-7a67526a14db | -11.78355 | -64.98089 | 2025-07-03 06:16:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2f597d94-1d0e-3415-9d5d-30a856662e79 | -9.63112 | -61.4712 | 2025-07-03 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b6b30505-ce68-3930-89b6-45bb220b61c7 | -6.9602 | -42.9052 | 2025-07-03 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| ddc35e3c-aae4-3a21-9433-8a69c8d07e7f | -6.9605 | -42.8816 | 2025-07-03 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.7 |
| 2c8d30af-53e6-37df-aaa9-f7fa5caadbbf | -6.9605 | -42.8816 | 2025-07-03 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 5accc840-a319-345b-957a-ee43c4cc2a96 | -6.9605 | -42.8816 | 2025-07-03 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 170.4 |
| f3e64fbc-f699-3e7f-8d4e-88abc5354a4a | -5.9938 | -43.7366 | 2025-07-03 06:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 84d1acda-9b11-390a-b8cd-9130c675d596 | -6.9605 | -42.8816 | 2025-07-03 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 38e0e0a7-65ab-35fc-879c-cb8e332f6f99 | -6.9605 | -42.8816 | 2025-07-03 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 3972e9d1-f0c9-38a0-af7a-a1ba81ded061 | -5.9938 | -43.7366 | 2025-07-03 07:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 90aaa422-3bc8-3d79-b04a-506c16121f75 | -6.9605 | -42.8816 | 2025-07-03 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| c7f774a4-474f-3a38-92ad-1a18612c2ff9 | -6.9605 | -42.8816 | 2025-07-03 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| bbab67eb-9328-310d-a8d0-c3528fdb7ef8 | -6.9605 | -42.8816 | 2025-07-03 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 44967a2a-d5fc-3707-9398-7b840d8422d0 | -6.9605 | -42.8816 | 2025-07-03 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| b76d1059-f970-362b-8591-bc7a5dd40886 | -6.9605 | -42.8816 | 2025-07-03 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| a85e0984-d48e-363b-9c21-0d39624e9f53 | -6.9605 | -42.8816 | 2025-07-03 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 7637d1fd-7765-3b68-8282-9439977a507f | -6.9605 | -42.8816 | 2025-07-03 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| db4f3168-b569-3e16-82a4-ee749e3bc381 | -6.9605 | -42.8816 | 2025-07-03 08:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| e5887b50-dc53-3f34-9871-5bcd6e15ec86 | -9.858 | -46.4788 | 2025-07-03 10:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| f8893e51-67d8-3e07-8052-fc027b1d36b5 | -9.858 | -46.4788 | 2025-07-03 10:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 9b6ceefb-9df5-36f0-ac56-42065e007259 | -9.8391 | -46.481 | 2025-07-03 10:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| c0527664-2eed-3d18-88e7-7f838adbb968 | -9.8577 | -46.5013 | 2025-07-03 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5695a2a9-b246-30b2-9b3f-92ff334bdf8d | -9.8577 | -46.5013 | 2025-07-03 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 199.2 |
| fd536db6-b785-3f0b-8aa2-03d0bd299d29 | -9.858 | -46.4788 | 2025-07-03 10:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 5c0dd0d3-13fa-3728-b720-a6f1c9e7b828 | -4.00637 | -43.23412 | 2025-07-03 11:47:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a74ada03-498e-3140-9e8f-5549675ce1bd | -7.69907 | -37.10914 | 2025-07-03 11:49:00 | TERRA_M-M | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cd19ef88-529a-379b-b4ce-048da40c8962 | -7.33891 | -46.7039 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 63fcc3b8-7b6f-3082-9be4-04e243f9b3f4 | -5.85075 | -43.6424 | 2025-07-03 11:49:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 2898c431-316c-38f9-80e1-7fd571eb2a0a | -12.85986 | -44.47475 | 2025-07-03 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6ff00528-c59b-37a3-a191-a494e73807f1 | -6.68323 | -43.17778 | 2025-07-03 11:49:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 2db9ceff-91db-3fa2-9f10-6a293f83d2af | -7.33405 | -46.73418 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f9c223c0-f38d-347f-871c-eec94b416295 | -15.36547 | -42.04623 | 2025-07-03 11:49:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 1d01a057-fec2-33a5-8635-8d76c20a935a | -8.99285 | -41.00343 | 2025-07-03 11:49:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c2912905-770a-38d7-890b-86e61aa60d37 | -7.86248 | -47.88356 | 2025-07-03 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e1ca38b4-67bb-35c7-aca2-ad991ac1a9df | -9.85194 | -46.50419 | 2025-07-03 11:49:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 971d12fb-9e13-3dc2-b47d-3570670eed9a | -12.86022 | -44.48528 | 2025-07-03 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 12bfbbe7-e356-3bcc-839b-65cbcf55eabb | -6.30357 | -37.70832 | 2025-07-03 11:49:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 82139ced-5857-3269-9574-163df97b025a | -7.23065 | -43.05838 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 9a8dfb56-ef64-36e1-b2fb-e908d3f6f92d | -6.84693 | -42.7832 | 2025-07-03 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 085975f6-5ac5-37b7-be21-8b4fc8ed004e | -7.20803 | -40.23881 | 2025-07-03 11:49:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 21.0 |
| eaad893d-000e-367e-8a53-f47651231e36 | -15.73986 | -41.15447 | 2025-07-03 11:49:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 37bc04f0-cab7-31bd-8625-2edf6394ea8b | -12.85718 | -44.49071 | 2025-07-03 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fcefada0-0b3c-39c3-bbe9-622e13ce1842 | -6.29467 | -43.66639 | 2025-07-03 11:49:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 82444965-9a93-3db1-b1f9-efdc2ade634a | -7.22827 | -43.07372 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 29102419-3871-3683-8c5a-ee64e384a267 | -11.54508 | -47.86323 | 2025-07-03 11:49:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 8577511f-df1d-39f0-b39c-821a480cf3d2 | -10.64904 | -44.47885 | 2025-07-03 11:49:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c25918a9-578a-38c4-8261-dcc13f9d7b33 | -9.85405 | -46.47072 | 2025-07-03 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e6b0ca22-758b-3fc0-b2dc-058fb3047586 | -15.25206 | -42.52877 | 2025-07-03 11:49:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 71966c9e-629a-3ee5-83c3-f7d0cffbc266 | -11.28646 | -46.23174 | 2025-07-03 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c2ef5cf4-40d1-302a-8c2a-a895976e3ac3 | -6.94747 | -42.88053 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4b64da7b-085f-3fe7-8e1d-d9d4aa0e1825 | -11.14291 | -43.32875 | 2025-07-03 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| dddb2f8b-c986-3adb-a8d5-a099bb5f55ae | -11.65671 | -44.59349 | 2025-07-03 11:49:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f9809605-0e6d-3e37-b663-cc5d9b0814cf | -6.95965 | -42.87369 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| bd2f93a3-bcfb-368d-8348-b12fbba8a8e5 | -6.9542 | -42.83563 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 09fc65b5-b59e-3556-ac06-3efdda52b6ee | -6.9554 | -42.82722 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| da55c345-5e1d-3fc3-b58a-2c72aa1439e7 | -9.84156 | -44.68579 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 888a2d5f-a593-351e-abc1-dad75e40eeb5 | -6.30231 | -37.71712 | 2025-07-03 11:49:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7150c822-7fe9-321d-9821-26887ae53068 | -6.9573 | -42.88864 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.3 |
| ca48b2bf-652d-3677-86dc-79f05a99fe7f | -11.54352 | -47.88896 | 2025-07-03 11:49:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| a42bfa5d-970a-349c-9490-00ac14603b7b | -11.65029 | -44.59931 | 2025-07-03 11:49:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| eb2ca59a-5eaf-3fbc-8c00-327e0a1764d4 | -6.68565 | -43.162 | 2025-07-03 11:49:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 765bd2cc-2313-3326-926d-ec82956907ef | -10.99601 | -45.19857 | 2025-07-03 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a9ed4da3-c956-3613-b339-e93207a045e5 | -6.97093 | -42.87544 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 73ce473e-b446-398c-a2b5-dd814edf05ec | -7.61917 | -45.73734 | 2025-07-03 11:49:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 94409629-72e0-3b01-83d8-4e6abfb9cd55 | -11.85347 | -44.85921 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 5763984d-92b9-3f72-bb44-98cde4d8b55d | -11.14514 | -43.3148 | 2025-07-03 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 7fb3b598-45f8-32f4-8152-e778d50f46f6 | -6.29187 | -43.68425 | 2025-07-03 11:49:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| cd94a897-8976-3ad6-935d-75130eaebef6 | -10.65414 | -44.48551 | 2025-07-03 11:49:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 892cdd4d-e450-38e7-a6a9-04c814a60108 | -7.33604 | -46.70944 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 4a54183d-f30d-3e31-8b32-29db5b779ef2 | -11.85626 | -44.84208 | 2025-07-03 11:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 81fc6432-d985-3d0f-b686-51722a2728a0 | -7.18853 | -43.99711 | 2025-07-03 11:49:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1878aee9-5df6-3529-b201-976b6b37f557 | -9.85637 | -46.47844 | 2025-07-03 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 54353cbd-efb5-3508-9618-3c9cc806ce9b | -6.9686 | -42.89043 | 2025-07-03 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9411e134-b610-3816-9acd-6bb4bf09447e | -17.47565 | -40.01366 | 2025-07-03 11:51:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 15469321-dda0-38fd-b0a1-cb99a8f8a69a | -16.59255 | -41.13174 | 2025-07-03 11:51:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 9bf04fbd-dcc0-3d7a-a6d0-2fadae0c99b3 | -16.59116 | -41.14109 | 2025-07-03 11:51:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.5 |
| 38d13e31-f01e-39ac-9008-65ee475ca76b | -19.65187 | -44.23738 | 2025-07-03 11:51:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 484d526b-3544-384f-93f6-33ff0f0b80bf | -18.55939 | -40.56284 | 2025-07-03 11:51:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 69170d1f-37de-3159-b380-2e06cd947691 | -9.8465 | -44.6834 | 2025-07-03 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5dfeba16-7a78-3b42-bc85-e79ad315e13a | -11.546 | -47.8772 | 2025-07-03 12:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 5f6eda3d-d881-3d92-b83f-abde53e02e32 | -9.8465 | -44.6834 | 2025-07-03 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README25.md)
