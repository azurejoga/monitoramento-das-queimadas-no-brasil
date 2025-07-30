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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66aa4405-d5d2-37ce-9bcf-bd46d1abe23d | -11.4776 | -45.1099 | 2025-07-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 957173a2-2373-332d-a253-ab68dcb02698 | -9.154 | -49.8356 | 2025-07-30 00:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8c9381d3-68f4-3efb-91a1-9d34be790e53 | -10.0782 | -46.9678 | 2025-07-30 00:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4749207c-1631-3bfc-84a8-3e2868e6e41d | -2.9108 | -48.254 | 2025-07-30 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 9557b9e4-b638-349c-a4d7-cf131c74c54a | -10.6169 | -45.2512 | 2025-07-30 00:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8570ad9d-e5f6-3dca-af99-c3ebd975c106 | -6.5258 | -56.2121 | 2025-07-30 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 8dd38bf4-8d9d-3ca9-a13d-a757aef4aa40 | -6.5074 | -56.213 | 2025-07-30 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 11dd5590-7383-360c-a9f5-dd90368f044d | -8.5211 | -43.3063 | 2025-07-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cc2f3a7e-1532-3e99-a9d1-4f4b2f7ecaf8 | -4.8397 | -42.911 | 2025-07-30 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 06bd09f0-f9ca-37a1-8dce-c17b26ef7d2d | -10.0972 | -46.9656 | 2025-07-30 00:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 686da141-feb7-3916-b01f-bb8c5ff782f3 | -6.5075 | -56.1932 | 2025-07-30 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ad5c2432-bf02-3799-a945-616247922389 | -10.6172 | -45.2282 | 2025-07-30 00:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| fa3ef0df-3c1a-378d-a42b-f4f2d9bfcf2a | -9.1538 | -49.857 | 2025-07-30 00:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 10f0cbc4-49b4-34a5-9465-733660a156e6 | -6.6328 | -59.9841 | 2025-07-30 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 7e5ff872-0676-3c98-a91f-28047dfeca13 | -12.4733 | -47.2846 | 2025-07-30 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 436d1a38-ca5d-3ff5-a0d6-960e321b8e2e | -7.8568 | -46.7304 | 2025-07-30 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f1c26e5b-c5d7-3c76-b3a1-a738498d0c3e | -6.6143 | -59.9848 | 2025-07-30 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 038f954f-13c8-34cd-a582-3013d02ef3ab | -11.4584 | -45.1126 | 2025-07-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 5303efdd-a3ab-3b21-9779-6451bc253a4f | -9.6334 | -48.533401 | 2025-07-30 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adc52730-082e-331c-83f6-f6b7a9f48c35 | -10.526 | -42.542301 | 2025-07-30 00:02:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0bf04fd8-7e4a-31d1-8e38-c049b75b3b0e | -10.9298 | -44.192799 | 2025-07-30 00:02:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaa20453-8a16-3765-a073-ac009820c075 | -4.3771 | -49.024502 | 2025-07-30 00:02:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73805d38-86c5-32c4-a63b-2ea1261cf1f1 | -4.8886 | -44.948799 | 2025-07-30 00:02:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 672dd4cf-5afa-32a6-b2fc-3e61227ea793 | -9.0453 | -45.0686 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80201f80-0496-37b9-b477-103254a14dab | -7.39 | -48.1562 | 2025-07-30 00:02:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28f746c8-881e-31dd-8190-7d94f696762f | -11.4696 | -45.0984 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6212f3-44a4-390a-86c4-8b2bb59e1482 | -11.4629 | -45.114799 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce3d1cb-c13a-37f6-9e53-8a965be9846a | -4.6476 | -43.116798 | 2025-07-30 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 355630b6-72e2-3905-96cf-148647bed9f7 | -10.6224 | -45.2211 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f50cf726-9d6f-35d2-b957-cae0b847c40b | -7.2188 | -43.0937 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db1513b3-3806-38d1-a882-e779c9e99134 | -6.0332 | -47.541401 | 2025-07-30 00:02:00 | METOP-B | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7d9f1c2-bc82-343f-ba6a-cac43f8745ce | -8.9586 | -46.7304 | 2025-07-30 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 584a3d6e-5e44-338f-8f3c-48f62f0a1596 | -10.6239 | -45.228199 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 968fae29-05db-38c2-914b-cfd58e465262 | -15.7194 | -41.934898 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c13b0f23-0760-3f68-9c99-fc7a04668f7c | -8.0321 | -47.6632 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96bff700-1e69-30a2-986c-9478c2ee9592 | -9.8292 | -41.489799 | 2025-07-30 00:02:00 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 759eef49-f266-3345-873f-54c9b29344d5 | -9.5984 | -46.319199 | 2025-07-30 00:02:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba4d57f2-6b4a-3db7-b94b-e9927f934170 | -9.4187 | -40.355099 | 2025-07-30 00:02:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0300b7ea-d96a-364c-9bda-b3e9669dc146 | -5.2445 | -45.202099 | 2025-07-30 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9afd388-ff74-3bfb-8c0d-0e3c03f1cd05 | -8.6357 | -45.494801 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 555473b2-687a-3544-99ab-1e9f48c2e4bc | -7.1454 | -44.038898 | 2025-07-30 00:02:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f84d7ee3-3868-3427-af4f-693088908aa3 | -10.6141 | -45.2304 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72ee08ab-f0b6-36b4-9ed2-5ae64c921ff9 | -3.8759 | -41.017101 | 2025-07-30 00:02:00 | METOP-B | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9bb7f6b7-2a7e-3ce1-91ed-a2be27277b62 | -15.7096 | -41.937199 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90b12374-f978-363f-aea3-c690eb99cdf1 | -2.9079 | -48.239899 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efdbabb-8c64-3539-9310-caa2072c840b | -17.4881 | -46.729801 | 2025-07-30 00:02:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d1ea49b-1f00-3975-9b12-394072039547 | -9.2423 | -50.027199 | 2025-07-30 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ff857e-ba6c-3fbf-b770-c20a8f7fde47 | -18.7889 | -47.606998 | 2025-07-30 00:02:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ef91c5a1-5a6b-3030-b4f7-9c86ba86cb2e | -11.921 | -44.531898 | 2025-07-30 00:02:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b4639cf-1614-388a-bbc6-ba53fac78c85 | -10.4132 | -47.239799 | 2025-07-30 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 424c36bd-5b4f-33ad-95d9-37d12e96b22b | -4.3851 | -49.014 | 2025-07-30 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d377a1-184e-3189-a432-89e1b49b57d3 | -6.4613 | -44.567699 | 2025-07-30 00:02:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 423a532c-0655-38c4-b7fa-0e5f1b3ca2c5 | -18.572399 | -44.4174 | 2025-07-30 00:02:00 | METOP-B | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7c9102b6-2fb4-3a9f-b9ed-e6f20cb671c1 | -3.9903 | -43.216 | 2025-07-30 00:02:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77b9f332-9a6e-3c46-8a5e-5ec5cb869f97 | -8.8934 | -47.328098 | 2025-07-30 00:02:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03355e42-5e7a-3327-aa8c-62523f391089 | -12.818 | -45.4394 | 2025-07-30 00:02:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc53dcc6-84c2-3240-9e9f-2587a6ee537c | -13.5381 | -45.6381 | 2025-07-30 00:02:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1ac68a1-d45d-3da9-b22d-ce582365b489 | -3.8148 | -41.553799 | 2025-07-30 00:02:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8aa2de1b-06a4-3aa0-a042-f86e93e26446 | -13.0913 | -47.311401 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 927ccaeb-e17f-3d3a-a4aa-d3705f118e23 | -3.9921 | -43.223801 | 2025-07-30 00:02:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1616bbf3-06c8-3a7c-a791-ec1e1c42c169 | -8.5149 | -43.307201 | 2025-07-30 00:02:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e340289e-0244-37ef-9486-13a21f1e9e1f | -12.4774 | -47.262699 | 2025-07-30 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aaeb8374-57ed-30b0-bd96-bf4bb8f83fbe | -8.5133 | -43.299999 | 2025-07-30 00:02:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e9d13ede-7657-3ae6-9065-72f3e246e4be | -9.2676 | -50.197399 | 2025-07-30 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1f0bec-2c7c-387b-a175-d4b99cef00ef | -11.5416 | -44.258598 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 991b8f11-5b5d-3c1e-b42d-46fd90871982 | -14.4833 | -47.872101 | 2025-07-30 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1c089cb-4db2-3699-8775-dc9e5b6d1bd2 | -3.1848 | -48.790699 | 2025-07-30 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf36712-7e1b-37f9-a3c9-2bd85c22d55c | -7.1073 | -44.371399 | 2025-07-30 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9ed37e4-7968-3bea-8ca8-7963df95430e | -6.9501 | -44.223301 | 2025-07-30 00:02:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec018f8-2a1e-33c2-8ecf-36072fdd9e9d | -6.3976 | -44.742001 | 2025-07-30 00:02:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06f253d2-8db1-388a-bb58-ec73b3ebc82c | -7.8578 | -46.724098 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee32cd0b-712c-3c21-beb7-a5c082c89ecf | -13.0956 | -47.2831 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c182b07c-2e32-3d79-bcbf-eb380756887f | -12.5849 | -49.779499 | 2025-07-30 00:02:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a586204-eb7e-3a81-8481-b951443e01ea | -11.3269 | -48.907299 | 2025-07-30 00:02:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6ae0e7-dc76-3350-bc50-e7e5d671c6df | -17.496 | -46.7183 | 2025-07-30 00:02:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc2825a8-2c04-35ad-b0f0-d42f718d7b89 | -17.051001 | -43.773399 | 2025-07-30 00:02:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdaf9627-6c75-343a-92a0-775b9858e976 | -7.2205 | -43.101101 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87b75f7e-b557-3aeb-a709-464c2c7db593 | -4.9 | -44.953499 | 2025-07-30 00:02:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 030b0262-3741-3b5e-9d93-ee54647d0ada | -8.0387 | -46.892601 | 2025-07-30 00:02:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd46fab-51c4-3247-83d2-a6b18b5443de | -11.8088 | -44.2565 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 063d0708-465b-3e7c-a600-7cabc49222df | -8.0403 | -46.900002 | 2025-07-30 00:02:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f35a3c7-a05c-3040-be85-c7d7cc167023 | -11.8186 | -44.254299 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5de8903f-b4cd-3cda-93b9-6d46b663455c | -6.529 | -56.1441 | 2025-07-30 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55596219-09f1-3005-9e1d-af4b96768857 | -9.4261 | -40.343201 | 2025-07-30 00:02:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a388dc31-99c6-3a4a-b3f3-9d9f77b81cf4 | -10.9786 | -47.391499 | 2025-07-30 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84f25a85-d7a9-36d3-9024-ae8b0a6e0bbe | -9.6353 | -48.5425 | 2025-07-30 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb0308a-3596-36fd-a8f9-8478263a7db9 | -5.2476 | -45.215801 | 2025-07-30 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 939974e4-a5aa-3228-9895-41e7d0a08a2b | -4.8452 | -42.989601 | 2025-07-30 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 721ecf91-5196-3a42-89d5-fe6f1141b19f | -2.9177 | -48.237701 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1af5a722-addd-3da3-9dfa-502441a0f2aa | -8.8917 | -47.320202 | 2025-07-30 00:02:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92b85b74-fa67-3605-9371-926218ed2f72 | -7.9397 | -44.0882 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34b34940-1bb4-3322-a04a-5474e06c068a | -5.8345 | -44.029099 | 2025-07-30 00:02:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12ca46f0-811c-3c91-8e17-95d17a6522df | -8.6263 | -45.871498 | 2025-07-30 00:02:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e473af20-472b-31f6-9a32-c33961c94231 | -12.4854 | -47.251999 | 2025-07-30 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 736370cb-d868-39e4-9d3c-549011489086 | -13.543 | -44.141899 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8eadb246-ab2e-3a9a-bf4a-80a53d14a6d9 | -7.1552 | -44.036701 | 2025-07-30 00:02:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd3a568-9fee-321e-9768-9976f3c76b47 | -10.6255 | -45.235199 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1829e228-c48a-3c2b-a390-7ecd302bb707 | -3.817 | -41.563301 | 2025-07-30 00:02:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c5c0195-d389-3537-a5f9-ce657943c352 | -6.5194 | -56.146 | 2025-07-30 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a75e973e-75a3-3679-ad46-4aeac5e2028d | -15.7161 | -41.9203 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
