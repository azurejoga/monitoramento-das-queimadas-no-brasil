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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e15fa0-b0a9-3443-9ccb-a257bd800e91 | -19.1441 | -57.78431 | 2025-08-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f9c651f8-59a5-3fdd-bade-94fe7db50e45 | -19.14342 | -57.78793 | 2025-08-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1dfdcb96-2d04-3375-a10b-d41ee1e969b4 | -22.82449 | -53.27152 | 2025-08-29 04:44:00 | NOAA-21 | PORTO RICO | PARANÁ | Brasil | 4120200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dfbc9103-4ee0-3f15-97a4-14a9592c6883 | -19.9166 | -44.61935 | 2025-08-29 04:44:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95757a00-3906-361d-9d57-1d73a617084f | -21.02718 | -44.79823 | 2025-08-29 04:44:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9f4411c-0ef2-3791-9596-b7d7d530a231 | -24.173 | -49.56944 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d80ab85c-da39-3916-88be-f099051337c6 | -18.98139 | -52.94636 | 2025-08-29 04:44:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f643c535-5d9e-3996-a797-d448169a9a17 | -24.17235 | -49.5745 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae87d786-48f3-34f3-a1ec-2faefcded375 | -20.49661 | -42.24387 | 2025-08-29 04:44:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 53bf19be-785a-320d-a85d-40ecfc8351ac | -20.02717 | -45.55363 | 2025-08-29 04:44:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e89fcf5-8faa-31fa-b371-dd03f8f82123 | -21.01383 | -45.06864 | 2025-08-29 04:44:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 72754716-4384-3b54-8e30-65de17694d47 | -18.97808 | -52.94577 | 2025-08-29 04:44:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b264fbd3-0fe4-3ff9-a167-5cf13d0ad406 | -20.47836 | -53.67415 | 2025-08-29 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c32c5b1-203c-3d27-aeac-b2f38e3c7827 | -20.97765 | -43.84105 | 2025-08-29 04:44:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 88c22587-eeed-39cf-a298-1875f54cd09c | -24.16987 | -49.56378 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4823acf-22cd-3274-bc0e-9c1669968772 | -20.49623 | -42.24791 | 2025-08-29 04:44:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 80e05240-344a-39ca-93ab-cd259030ceb6 | -18.97865 | -52.94213 | 2025-08-29 04:44:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3163f059-00c1-343e-a5ef-5253abacfbdd | -24.16858 | -49.57399 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 9cbec032-9875-33b2-ade3-7f3adbb04469 | -28.70255 | -55.58267 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 3221005b-5a8a-3307-91e5-71bbdfe3d637 | -29.77855 | -51.1772 | 2025-08-29 04:46:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 091444c9-388e-32af-8cf0-a253855b925d | -28.69924 | -55.58199 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 1f8527c8-5a31-35cb-93ec-06db8866ff68 | -28.73155 | -55.65794 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| 2efd0d37-11b5-3519-8dd6-03c2af5df06a | -28.73473 | -55.63818 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 8740c3bd-2934-391d-8238-b77224f4d211 | -28.70192 | -55.58661 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 4917924a-dadd-35e9-97a4-fa4d627a7fc7 | -28.70128 | -55.59055 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 38df099c-a9c0-31e3-ad2f-83b3a1b3d240 | -28.7355 | -55.65467 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e444decd-540e-3ebf-ae88-4f7c72d7b845 | -28.73805 | -55.63887 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| a41dcbb0-c3bc-3b9d-ae43-f83a27d5ab83 | -28.73614 | -55.65072 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ebc03424-0f87-338c-b1cf-978783faa68f | -28.7341 | -55.64214 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 7d03a4a3-ba8b-3448-8627-30ede3852cbd | -28.3009 | -55.6253 | 2025-08-29 04:46:00 | NOAA-21 | GARRUCHOS | RIO GRANDE DO SUL | Brasil | 4308656 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 4dfa049f-6c1c-3768-8676-63fe3d73eb21 | -28.70065 | -55.5945 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 383d3f22-bd67-3e2c-8de8-7af2f448f4bd | -28.73219 | -55.65399 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| f66c8663-f611-3302-98f5-4bd335763dc0 | -28.29758 | -55.62461 | 2025-08-29 04:46:00 | NOAA-21 | GARRUCHOS | RIO GRANDE DO SUL | Brasil | 4308656 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| bf1afa61-a026-308c-862f-db4ee186fc53 | -28.73346 | -55.64609 | 2025-08-29 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 183befec-7324-36db-955b-6ce834528c91 | -13.5391 | -46.8548 | 2025-08-29 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 49be4c9d-1118-325d-9c01-cf7013a5155d | -8.1758 | -61.3755 | 2025-08-29 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 31a1b04c-a664-33f5-b894-45d7b97b4bcc | -9.7728 | -64.2657 | 2025-08-29 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ac0e21a7-782a-3eae-9878-373e7a0281a1 | -9.7916 | -64.2461 | 2025-08-29 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 00147104-d1e9-398c-923b-9100abbe89c1 | -12.7067 | -48.1873 | 2025-08-29 04:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 258d34db-f48a-3204-8efa-95ffb9d7bc01 | -9.1155 | -65.7699 | 2025-08-29 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 368a4400-75d6-311d-a63e-abfb7e603a45 | -10.9709 | -46.9266 | 2025-08-29 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 102d345e-14b1-39d8-ba33-597168277828 | -9.462 | -60.549 | 2025-08-29 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| fe1abad8-4a01-32d5-8566-b8b50596218f | -13.4212 | -46.9637 | 2025-08-29 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 54c176b4-5da8-3d93-8b18-4f13b109c0d8 | -13.4019 | -46.9667 | 2025-08-29 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0b0faebd-e85b-3b60-8d47-e82166140e58 | -10.9712 | -46.9042 | 2025-08-29 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| d5643548-6660-3c91-ad30-5bdde702a25e | -12.6878 | -48.1677 | 2025-08-29 04:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| dc298f84-b476-33ce-81cb-1cb9aa25a133 | -13.4208 | -46.9864 | 2025-08-29 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7643d206-a06e-3263-8b6f-31f4519777d6 | -10.9903 | -46.9018 | 2025-08-29 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 148294e3-43e2-3354-8b57-1bf012c2242a | -9.1156 | -65.7513 | 2025-08-29 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 97dd5d8f-d328-3420-a025-3fae0f6ad343 | -9.773 | -64.2469 | 2025-08-29 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b73c511a-8fde-3b3e-8aec-13b60974c713 | -13.5386 | -46.8775 | 2025-08-29 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 56a3a10c-4dab-3c6c-8d63-4553a8f8aede | -9.9328 | -59.9247 | 2025-08-29 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1b0d2ad5-6148-3c65-96d3-ab2e29808699 | -9.4433 | -60.5499 | 2025-08-29 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 485c665f-b125-31d0-b08e-7b41b7d53609 | -12.6875 | -48.1899 | 2025-08-29 04:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 540601d7-7b53-3252-a6c0-c41ccd968a46 | -3.7694 | -54.8086 | 2025-08-29 04:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 915e7859-092a-3c2a-9b9b-4917a1f34c45 | -9.4433 | -60.5499 | 2025-08-29 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a178e353-fad0-3ce3-ada0-8d189629ece0 | -12.6875 | -48.1899 | 2025-08-29 05:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| dacb6483-2070-3149-9849-f1473741bf79 | -12.7067 | -48.1873 | 2025-08-29 05:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7f0ed5be-cbb5-331d-97c8-356f31f17ae9 | -9.9328 | -59.9247 | 2025-08-29 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f316f806-c901-3798-8dfb-0f4372f91518 | -13.4212 | -46.9637 | 2025-08-29 05:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a02a633c-5b04-3a9d-a18a-a3a63c5770a1 | -9.7728 | -64.2657 | 2025-08-29 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8eff67b5-ba6c-32df-b95f-ed26bebe39c7 | -9.7322 | -64.9067 | 2025-08-29 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| adb40732-f9f3-3a76-b9fb-877fb35f0b6d | -9.462 | -60.549 | 2025-08-29 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| b507b448-a1cc-3e9b-82bd-be1a53b30869 | -9.773 | -64.2469 | 2025-08-29 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5ebc256d-2641-338d-954a-29be17484015 | -13.4208 | -46.9864 | 2025-08-29 05:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8b07a7a6-d60e-3578-a82e-79da55d1b353 | -9.7916 | -64.2461 | 2025-08-29 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3c2c4634-93c4-3ae2-98b4-18f88d2dfdd8 | -11.876 | -46.4007 | 2025-08-29 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 23c327a9-f157-361c-a616-433c8b20aa7e | -8.1758 | -61.3755 | 2025-08-29 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cc2c82b4-9c06-367e-aac6-161b035e72bb | -10.9712 | -46.9042 | 2025-08-29 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 72f7ce62-32e7-326b-b318-d1a676f6f6df | -9.1154 | -65.7886 | 2025-08-29 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a110ae1e-7ab5-36d6-a9ef-618f0c98283f | -9.1155 | -65.7699 | 2025-08-29 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f5e0c973-48aa-3aff-bb9a-9b92aa9d3627 | -9.4618 | -60.5682 | 2025-08-29 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f8c435b7-a3ea-39c7-8420-741448ed419f | -3.4254 | -49.0517 | 2025-08-29 05:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e514a057-a199-37e6-bbfe-c12be76ccb58 | -10.9903 | -46.9018 | 2025-08-29 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d139abae-ad99-373a-a746-f17a021e53c7 | -3.5125 | -47.20878 | 2025-08-29 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b1deb2-16c6-31d0-8eb3-8ed77cd289ae | -3.97741 | -43.24467 | 2025-08-29 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| abdecaa6-0a50-3a5e-b27c-8f2d642d25cd | -3.97817 | -43.23936 | 2025-08-29 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655a66f8-835c-3611-a5fb-08179c6a81a7 | -2.44699 | -47.3301 | 2025-08-29 05:04:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae7aaca-b7e6-34c3-bada-d4feafe1a42e | -3.97538 | -43.24895 | 2025-08-29 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0df7b015-265e-3418-8923-74ca0e8d121b | -0.75187 | -47.75194 | 2025-08-29 05:04:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f4c51e4-3891-33b5-a63c-2bc1fde7ab78 | -2.98226 | -48.60405 | 2025-08-29 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69e1363-0fb3-36f7-aa06-c485d01322d4 | -3.17106 | -48.8075 | 2025-08-29 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8baf27a-8193-356e-bbc0-1a3409fcfaa7 | -3.04667 | -49.43162 | 2025-08-29 05:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e295d6e5-8edc-36ba-a84c-a86fc20509e6 | -3.04363 | -49.42337 | 2025-08-29 05:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4278b722-29ed-3e99-b436-0fa7b3a7dbb9 | -2.4422 | -47.32935 | 2025-08-29 05:04:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ef69ec4-ddd4-3871-ac3d-a29900aa5128 | -3.38317 | -47.49239 | 2025-08-29 05:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d8ed3bd-1533-37b7-85f2-cbf04ab0d817 | -0.7564 | -47.75264 | 2025-08-29 05:04:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbe90574-5f1e-392f-852e-b2cfd68b87fd | -1.74775 | -54.51603 | 2025-08-29 05:04:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab248c5d-9daf-3378-8e54-42ec27db82cc | -3.97102 | -43.2435 | 2025-08-29 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 348b4a29-7a5f-3a8b-9cca-85632e61151f | -2.7435 | -48.70155 | 2025-08-29 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37978062-a634-3f8b-933a-91a3c9de7303 | -3.97617 | -43.24369 | 2025-08-29 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05f20b58-8d55-3ba3-8657-1e59aeb4be12 | -2.91882 | -48.30987 | 2025-08-29 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50fef90c-352e-3df8-98ff-515f63e910f8 | -2.98669 | -48.60467 | 2025-08-29 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2de63241-b35c-3591-bbb4-56ee1ec98e67 | -7.74387 | -50.27326 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f79c412-0174-31ee-bb63-1797b5326742 | -9.49763 | -45.39178 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 087a13c0-912c-3333-beda-d0f878edc3ad | -6.43193 | -44.57063 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 010addcb-5962-3f83-995a-17d505ad9baa | -5.69982 | -45.96016 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06a7dbd9-b2f5-34f7-9a10-3468aa9a06f5 | -6.71306 | -49.46694 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afc0b7bc-b3a5-3988-8112-b2855ed51636 | -7.73208 | -50.30119 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c267be77-caa7-3c15-a290-e9cb435b56b4 | -3.81839 | -53.73798 | 2025-08-29 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README59.md)
