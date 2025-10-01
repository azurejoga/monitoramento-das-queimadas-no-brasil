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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2037a82-1bc8-34d7-bddb-55d4ac6c70f7 | -2.24584 | -47.88622 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 441dfbe5-156d-3c70-802f-f02e7c6736c6 | -2.25095 | -47.88695 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fd4e368-38aa-384d-880b-857b23c67082 | -4.03659 | -54.1342 | 2025-10-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69771d7c-c589-3652-93a0-51058e16d51c | -5.85512 | -43.40632 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0db303ec-bddd-32ef-85d0-374f7017fc2a | 1.29066 | -51.24483 | 2025-10-01 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87890fff-1336-326e-934e-7fe3e795d21f | -1.62634 | -47.05306 | 2025-10-01 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22676bde-fa88-3731-b430-0ea841690c43 | -3.04971 | -51.10427 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 849a0286-60c2-35e7-8146-338fe3e242cf | -4.26004 | -48.55228 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf1fcfa-616b-390d-931c-a44d500ac85b | -4.25457 | -48.55452 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e680a8-baef-38b7-9331-c86260912f27 | -3.91488 | -54.56373 | 2025-10-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e63e66d-fda6-3f94-b049-99e19588fdf7 | -1.62382 | -47.05472 | 2025-10-01 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 22948022-5421-3748-8ed0-9cb56c0aaeb8 | -5.64401 | -43.91825 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d2960448-4d5d-39de-8b75-cdbe1e4f4412 | -3.27089 | -52.50892 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7cb4f8-109e-3044-8047-28deaacd951d | -3.68694 | -49.04796 | 2025-10-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31adc2b2-b285-3960-b43e-f4ea77a78565 | -3.51367 | -49.4472 | 2025-10-01 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10569847-830a-3da6-9b08-9744db45f038 | -3.51678 | -49.44534 | 2025-10-01 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6318a04b-0ce7-3b10-81e6-80efc4445858 | -3.78006 | -51.29449 | 2025-10-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6ef0792-b74d-32ff-aa69-c9a556e826c6 | -2.30459 | -48.14677 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25fdf3e9-536d-32c8-9839-0865cac3c438 | -3.46378 | -50.08751 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ecd6859-8a35-3775-8c50-b990300ae715 | -4.31238 | -48.09164 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62420783-22c4-3460-bebc-20d48fc9ad79 | -3.54012 | -51.1571 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 281b7c5f-04c1-3a71-92ff-d7f1279b46ec | -4.36884 | -55.89059 | 2025-10-01 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cf23c4b-dc26-3475-921c-0cbe6f7e97df | -4.31284 | -48.08853 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af216270-d760-3305-bd9c-d9e43f8f7aba | -0.09694 | -51.27765 | 2025-10-01 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0fb18ef-5f0b-34f1-9100-f0eb3c9607b5 | -3.24353 | -52.89235 | 2025-10-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 378aa79c-6cb3-33c9-9522-8aef0c06d7d2 | -4.80512 | -50.73603 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe98cfc9-1c3b-3143-b70d-131d06084bd6 | -2.14578 | -47.50971 | 2025-10-01 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8c9e45b-4937-3ed8-9c61-c1b2ae0d3047 | -3.67578 | -52.132 | 2025-10-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e0b6fde-52e2-33b5-9bb5-ce692966200e | -0.90043 | -47.54539 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9db2292-b51c-3a49-a877-789a67fcee9c | -3.0521 | -51.10461 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff51df61-927e-31f3-a522-f99fec1546c3 | -3.45328 | -53.8354 | 2025-10-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cedd25c1-88e2-3d0b-a14a-ae5835744c04 | -3.09376 | -47.0256 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6def9c82-440b-34cc-b7af-4390240086e9 | -11.82819 | -44.95105 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2180baf9-97e0-3767-80d6-5680fc64e572 | -10.6455 | -48.52499 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e8d0c04-c905-3f46-a02a-3635d5f6745b | -11.80003 | -47.59781 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dff09d64-96a6-3843-bae2-cbb3eb7e46fd | -7.81649 | -47.06579 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd7c0b90-1e78-3bca-9c80-f83d60e7371e | -8.55285 | -44.72716 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab3c7eca-d3e8-3a82-9c82-2fc3590af08f | -7.82877 | -47.0629 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab4bc7b8-6a5c-3db1-9530-2e45b052290e | -11.76323 | -46.86739 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8eb443ed-5628-3245-a25e-4430e0177c63 | -13.30876 | -47.22848 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88f140be-ed05-3eee-bdd6-8b72b0a2bc96 | -9.85247 | -44.61063 | 2025-10-01 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f90262-51c5-3557-95d8-3ba741b6fa9f | -13.32129 | -47.33628 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6cff0a4e-e9e6-3fc0-b70b-50482b9000cf | -13.29519 | -47.23713 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb1e3e9c-6c36-3b91-802a-871d2360fc2e | -11.45519 | -44.97414 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa97028d-bc6c-3f54-9a8d-c8bf43944d1f | -9.81776 | -47.86019 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c927f08-1b01-3366-a9a0-58ec9ff82203 | -13.21431 | -47.34292 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76c7a682-faa8-367c-a580-63853f3c1701 | -7.63241 | -45.44843 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a9fcd8-bfd4-391e-9457-baed202373db | -12.98031 | -48.41893 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1dbab38-4f94-38c6-826d-e30e6652ba1d | -10.06506 | -48.19611 | 2025-10-01 05:10:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235d75c7-ab38-35ac-8ad1-c68b95c574fc | -13.22375 | -48.45177 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0acf39f-379b-375a-8b9f-4c68c2e2030d | -11.83768 | -48.05688 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1148c3a7-9770-31de-902d-f0775200dc52 | -9.58409 | -54.59932 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9206c5e-6c72-3c2c-b313-3471e7e9ca35 | -12.37122 | -50.20292 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2fec65-8dd8-3c66-a247-e3b951d8a1b1 | -13.2421 | -47.31793 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b97aa46-d91e-3bc2-88df-ea383593eb09 | -11.56967 | -50.18053 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdd88922-a721-3fe7-b4f6-14297460cee2 | -13.32699 | -47.82224 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1a2f658-0d92-373f-8099-3d9693f48448 | -8.16472 | -46.24988 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff16edc2-c067-3400-8d1a-bc222f08316f | -13.32678 | -47.87596 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdd88e8f-128d-3669-8497-075191b9bf36 | -12.24449 | -47.80863 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 317b3f48-03c3-3350-b853-b2af404ad281 | -12.86156 | -46.94433 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cc586be-ea36-37b9-91b5-17a723df2411 | -8.21992 | -55.20202 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da29179d-1c19-3a80-bbba-c493daa6d75e | -11.12082 | -49.78629 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e4b71a2-0d66-380c-9484-2b2b3b0bd971 | -12.3716 | -50.19994 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67295b22-36e0-32cc-b92d-fd53d2d5e26d | -11.84001 | -44.97206 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4acb587-2532-30b8-a6cf-5bb3778c02cf | -7.47416 | -46.47438 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de9c1f28-37ce-335c-a1d6-9a1292591abf | -8.14932 | -46.27192 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4fef300-a790-3601-b3e4-574026715e3d | -10.73618 | -45.37177 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f74817ff-2e57-3123-aea4-210467762dff | -11.14485 | -54.11874 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b269622-1f02-3049-97cf-4eac4a699dd9 | -13.32604 | -47.83037 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2af193b-1a08-3100-8e1c-c3b2c77cde54 | -13.37872 | -48.0837 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06e9a344-bf97-31d6-a0d5-7dc25aa17e06 | -11.83747 | -48.05349 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99beac50-6522-3f35-9b37-1efdad074b6a | -11.46185 | -45.09758 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6a104f5-89a0-333c-8099-6592b055d7d7 | -11.18266 | -47.20738 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8d6ebb-204c-38a1-a353-b8a84effe316 | -8.14871 | -46.27667 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9f72b0f-c394-38ca-936e-e2510ace4773 | -11.08544 | -47.83636 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c8e7720-c350-34d3-94b3-ee916160dc4a | -12.7993 | -46.8982 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b59ce84-5415-39ab-9dec-4ac4acf50851 | -11.39318 | -44.90649 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b5bc22e-bff8-35c3-9637-2504118de330 | -11.84326 | -48.05415 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40881567-f5ac-3827-8f57-08a9b9c4ab83 | -10.77757 | -45.36868 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5f98a49-81b4-3e64-ae7d-14efb88a0370 | -11.67288 | -46.96118 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 78382074-5f8f-31fb-8d99-d4e426397f22 | -11.76264 | -46.87254 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f680018-d489-3605-ab1c-32d598ebca8c | -11.92045 | -48.00474 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a033de99-6af7-3e8f-aa85-ef3a5b368a40 | -12.77426 | -46.89387 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e88596a0-de42-3700-b639-1f3a9dafc3d7 | -10.10123 | -50.22226 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0466b46a-79df-3d17-9f53-3e6785d24070 | -9.85859 | -44.60846 | 2025-10-01 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0009fa61-fc38-3b3e-9158-05343eadd161 | -8.57911 | -44.74865 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7e56a62-9c0f-379f-a3ad-8a4eb6529998 | -13.34384 | -47.80592 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32c495b-2f2f-33d8-8e33-dddf0c3eed75 | -11.12043 | -49.78932 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf0880f8-404d-3e79-9997-8e1c519e935f | -10.10843 | -50.31738 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3a0a35d-9e4f-3434-ae4b-c199034b449e | -7.62656 | -46.68204 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce18af62-52ae-3910-a7a5-711b180b6a8c | -11.80594 | -46.63204 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9e9f0b9d-5c3a-38e4-8d3e-4c0f1ffcf0a3 | -10.03717 | -52.09483 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f067e32f-ff6c-3be3-87fa-c2bc118ad912 | -8.88554 | -46.61449 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00c1cde4-ff01-31b4-8c2c-25bf4c15f89e | -11.46647 | -44.99124 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fc52dfc-b693-3fd3-97af-3d7c51dd77c8 | -7.47365 | -46.46745 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f62b354-e59d-3eed-b190-d3afda84cef8 | -9.89645 | -45.94123 | 2025-10-01 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e39aeeac-fa8f-3870-bfd9-b9296065d944 | -13.32981 | -48.14655 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2980020-e1fe-30a0-ae7b-6d019f530907 | -12.82833 | -47.03066 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eddacd5f-f14b-315e-bcf6-0a544d66746e | -12.80307 | -46.89669 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e7ff562-e1d7-3268-9d7c-7f7e3023a59b | -11.39397 | -44.89979 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README121.md)
