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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2ebb78-0473-3a52-b232-d5f7e65e6b73 | -13.73776 | -48.41984 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec8cf566-39e0-3d6f-a289-aa2844542377 | -10.29236 | -47.18696 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1ff5879-b751-33b9-93af-683dbc04148e | -13.86032 | -48.51675 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84449d2a-e950-3fc2-a0ff-cd4edce2ed4b | -14.64062 | -48.39531 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a36b98b6-efc5-3844-b80a-fc777bf76918 | -11.73552 | -49.3283 | 2025-10-28 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a85a8b-103b-3f77-973c-f2d9a073e036 | -12.31681 | -47.4523 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4197301-22fc-3762-930d-31b241085bbd | -14.14877 | -44.2459 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4804ad5-2d9a-3f24-aa4f-47ebac4eedb3 | -10.28848 | -47.23802 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ec4c457-c8ea-394c-b0ef-f4c68c37a94b | -8.63651 | -45.28488 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d42dd07e-6063-3fb9-83aa-5aa1c70b8f41 | -14.42371 | -49.41832 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcc81320-16b9-30a5-90b3-289b409bf105 | -7.92802 | -49.73676 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc6c72fa-a392-331d-a785-bc612875f80d | -10.84235 | -47.88943 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca2e546e-f238-33ee-b1b1-b03306056edb | -10.67821 | -47.26948 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d1e6bd8-10a7-30ef-a538-2dee81096188 | -11.10328 | -44.01833 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc749476-5e88-3895-ac31-62ca3bb4f7e0 | -9.95749 | -47.11122 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b824ee3-ffe4-3da1-adee-1c32e966da85 | -11.1338 | -47.04926 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 023d52cc-d74a-3e26-8a51-e332c650010d | -10.2347 | -47.6465 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56fc2395-83f6-398a-b666-1dee85b35580 | -13.94516 | -48.40194 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c80aed54-311b-33a6-82db-db229fe536fb | -13.62719 | -46.46295 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 255f33b6-b5d3-3232-8380-6ee89c0c31d1 | -10.33673 | -47.78037 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f39ca296-98b4-3be0-adc7-4f85d04580a1 | -11.79904 | -52.49426 | 2025-10-28 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 621729df-e1a1-3133-ad88-2ca77deba582 | -9.47666 | -47.777 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3f21be9-e74c-319f-b55f-63a7345ff02a | -8.63376 | -44.7935 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeb8ed08-8af6-36f0-872b-568765c73e03 | -13.42793 | -47.37832 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fe85edd-0bc0-309c-b2b0-5f924098e1bb | -8.63803 | -44.78635 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ab8872b-ea64-34e7-ae33-a6cceaf00943 | -9.29199 | -45.21679 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916dbd64-af17-3397-af4c-d0998b18d053 | -9.56518 | -46.9718 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 427aa11f-c19a-37e8-98d8-bdfe1269d431 | -10.34735 | -48.04706 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bac94834-12e4-3065-a4a6-baa627cd9853 | -13.68701 | -48.35096 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d936238-3851-3ce6-89f5-a116d1945e6f | -13.43169 | -47.37865 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a772d5a2-89e5-328a-98cf-082d38d2904b | -11.14437 | -49.73093 | 2025-10-28 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a538678-b592-32a1-8e15-3b879c409d9e | -10.56182 | -49.81018 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82fa7673-7737-312b-a6a5-85a8ba679e11 | -9.51839 | -40.3118 | 2025-10-28 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d5b8a8d-f616-3d03-b6dc-c5b96ac80d84 | -8.14141 | -47.75065 | 2025-10-28 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e226416-1872-365a-a0e6-4351d93989f3 | -15.19624 | -47.20943 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39b2e635-33f5-3159-acf1-fde4d932deee | -10.97592 | -47.81393 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939aba06-1fad-3428-b557-a8e1b7eb9373 | -15.17809 | -47.21384 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3bc038a-9cf0-3be2-9a99-7f9d762be349 | -11.84605 | -49.81188 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dfbd388-df24-379f-9c99-8fb0ec83f8fd | -12.08352 | -45.64611 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce29f9a-776c-352f-9e82-feb8452549dd | -15.1567 | -46.6036 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c0c6972-dd64-304e-a94d-5f51b4cbace3 | -12.64928 | -44.26276 | 2025-10-28 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb132215-5a87-3b16-b39d-95ca2dc81ba3 | -9.02652 | -47.89338 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66ab42c7-853e-3f4d-b4f9-4eceaefaf8e0 | -13.24554 | -47.96371 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 57764884-5ff4-3dc8-ba9a-5bb6bb5ff2a4 | -13.03813 | -45.85488 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e5c741-bed8-3ff4-acd8-27d1a3a2bf75 | -13.78786 | -48.49839 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3eb2cad-298f-3707-86fb-86336e9fac80 | -9.04716 | -46.92843 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf9f77dc-b00e-3dc5-890b-b9e015a2abcd | -10.76435 | -44.74834 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f3d337e-59a9-32d9-936a-54920160614e | -10.92556 | -50.27279 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319c8e90-6541-386c-886d-650408f3706e | -10.87691 | -48.62949 | 2025-10-28 04:44:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0d88953-fbc3-3957-b750-5a3ecd692393 | -14.42654 | -49.42284 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 041e91b9-86d6-3024-b2a2-35ef5eacda69 | -12.95814 | -44.61991 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1955f34-54b5-3e83-9669-baa9f7f08287 | -13.55586 | -49.57838 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a8b6da-6981-3984-b726-c39a7b505a63 | -13.32052 | -47.43881 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cd58c5f-6e97-37f7-be40-ca5ee64c68e2 | -11.19246 | -44.63142 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc280f7-69b7-3294-a827-dca08acd2112 | -9.88535 | -44.88626 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81482680-d0de-3f58-a6d5-d132eab7c6b3 | -10.33261 | -47.78375 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ad175405-3a88-37f5-abb1-ea7e730f6e50 | -9.97053 | -47.17324 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdafbc38-944d-34c1-b16f-175f82daa41a | -13.66546 | -47.63214 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3686f8dd-3d2f-343c-82b7-ff8609e5ddf1 | -11.7344 | -49.33562 | 2025-10-28 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e5d5d41-2748-348d-aa67-7032d6ff35d7 | -14.53652 | -47.98529 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a83efc0-0194-3c46-9cdd-221e881e3d31 | -10.88551 | -48.63768 | 2025-10-28 04:44:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0d3505a-1477-3629-96cd-06df8976094b | -8.62961 | -47.70934 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d067deb3-12f6-3526-92a3-71a46368b066 | -10.92611 | -50.26927 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6a31853-3037-3342-b179-3ea652d83e68 | -9.0684 | -45.10454 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2723aa84-7ba8-36a8-9db0-bf5eeb8ee378 | -10.60074 | -48.03625 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c0e278e-6dbe-3477-9040-9946a0905bde | -12.20676 | -46.50811 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f8d760f-aaeb-3bab-8cf0-10f84d5cc57e | -15.79287 | -45.20022 | 2025-10-28 04:44:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45aa207b-03db-332a-86df-cfba6f16817f | -9.26401 | -46.27378 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93ea0772-2dbc-3a05-b94e-151abee38a5b | -13.65681 | -47.63993 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9be1bfc2-9d11-3923-b784-96d64ab96f14 | -10.58292 | -49.76277 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d0570b-7cac-3c58-8032-8f8ba397750b | -10.06754 | -48.1997 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 126576dd-2e4f-3fce-9e3f-ce1b6c0a84fd | -14.45756 | -47.77645 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668a5879-2b97-3ebb-b70f-876f07513e58 | -14.65372 | -48.40607 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc36f036-5302-3e7f-bd7f-bef6b3b247be | -10.86046 | -48.96492 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20cada81-7591-355f-b09f-1c09671c0c81 | -10.69046 | -48.0129 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4192e636-07f5-3406-b314-c8a894de8948 | -10.62857 | -42.32268 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b89025dd-9a80-3ce0-9478-f865f2b481c3 | -10.91794 | -47.8136 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47798bb8-5070-3c1f-80ae-764371d55409 | -9.97603 | -47.16122 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a2d08c0-0e10-3be3-9330-352791695ea7 | -10.86114 | -47.90853 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54628821-bf3a-3856-8961-acbf9226ed6b | -10.99548 | -50.36301 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69e83eb1-c908-36a4-97c1-bf8c868b20fb | -14.08623 | -44.15553 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c97df1c-0274-328f-a254-00a905f7dbbe | -9.61281 | -47.80762 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97bbf9a9-f3ac-3dbf-8f0a-96f0e2179d22 | -9.48645 | -46.85267 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53651dbe-d2ef-3fc8-ae1a-7e1e929cbc73 | -13.79142 | -48.49882 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a87478-e2f0-3c1d-b1e1-253533529a90 | -10.97049 | -47.82592 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5261a2d2-7a0a-363c-b630-da034dac58b0 | -12.52922 | -47.55074 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55914420-e955-38ba-b4c0-bdfdbd070dda | -13.53274 | -47.16063 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 411a3c17-5fb4-329a-a8e9-67131f55ff9d | -10.55878 | -48.9975 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec907453-6517-3dc4-98b7-d1daeb1ce011 | -11.07754 | -48.3356 | 2025-10-28 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21a666f8-2cad-32ab-b308-81f3697baca1 | -13.73601 | -48.4319 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b58b75e9-96f4-3738-b81d-67d1b910364d | -13.22945 | -47.07545 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dbb286d-5290-37cd-89fc-769973543fc8 | -13.4465 | -44.1039 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97eb6ca8-e2bc-37ef-8712-a9cee691d8b1 | -9.13713 | -51.30449 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e8ea1578-6d04-3df8-8776-38fdd9e8c86c | -12.54927 | -44.93665 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ec46395-1c2f-327f-9604-739d91a517c7 | -10.54178 | -49.78524 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e91425b0-0e7d-3a6d-836b-43d1bd038207 | -10.64723 | -48.01424 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e409b7-ea46-3e30-a6f9-647b7cd363f6 | -14.94284 | -43.44043 | 2025-10-28 04:44:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57b5ab0a-c7ee-308d-9d4d-daa54ee32b83 | -13.31683 | -47.43809 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc9af0a-af98-34e8-9dd4-0cdfa2721223 | -14.05319 | -44.40473 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fced69cb-ae83-3b5a-8f12-223790d5ce87 | -10.29648 | -47.2091 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
