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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90630484-89de-3ba3-a46d-1042c11e1411 | -14.1309 | -46.2801 | 2026-09-29 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 238.1 |
| b26a1a72-6528-3c95-86f8-af8771f09272 | -12.2723 | -50.1657 | 2026-09-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5677a45b-9465-3d9d-a700-7157aadaba8c | -11.1583 | -44.7859 | 2026-09-29 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.5 |
| c95e8858-8767-3af0-89e8-a1b21a167906 | -12.7417 | -47.2909 | 2026-09-29 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1bf15954-10c4-3f8c-95da-a37b1a96fa3e | -10.7916 | -48.7377 | 2026-09-29 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 80caa03f-491c-33cf-8143-2389f38de257 | -8.9823 | -44.1633 | 2026-09-29 13:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 23ee90d5-cefa-3db3-af25-3f584aa4a7bd | -10.8109 | -48.7137 | 2026-09-29 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2d04d9a3-d546-306c-bd51-d60da436c16b | -13.1799 | -48.5631 | 2026-09-29 13:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 74fb5d7d-273c-3848-a7f8-0fc6eaf84a8c | -10.7913 | -48.7596 | 2026-09-29 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a852effd-d76b-3543-9f9c-a81642fb0b15 | -11.411 | -43.4625 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 28486a39-148d-3a9c-ab8e-6463f35ae4e0 | -14.4839 | -47.0414 | 2026-09-29 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d0a5e5d3-7d0d-3f21-bda7-1829158d2d8d | -7.3965 | -42.6498 | 2026-09-29 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 01f4e322-fd74-3ce4-aadb-736867053c11 | -8.9633 | -44.1655 | 2026-09-29 13:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3b1c7662-a529-33c7-bc49-74e24d49ac4e | -9.9595 | -50.1431 | 2026-09-29 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| cffa9d83-8539-3e1a-ba58-287c73969ef3 | -11.1771 | -44.8064 | 2026-09-29 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 463.4 |
| eabdd036-305c-34d5-b295-2d6c0c4d981a | -10.1245 | -45.1313 | 2026-09-29 13:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| bcc7a4fb-d4b9-331a-b532-e05bf7befd17 | -11.1775 | -44.7832 | 2026-09-29 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 636.7 |
| 12a0037c-624e-3a84-977c-4d5149071259 | -10.3895 | -61.231 | 2026-09-29 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 37f67efe-225e-3946-8d23-73be4b8d7626 | -9.1337 | -49.9656 | 2026-09-29 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e42741a5-eb37-34c9-8537-67eff0d10545 | -13.1992 | -48.5603 | 2026-09-29 13:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 92416403-501d-329e-b870-5fee1e00c93d | -8.6826 | -45.3677 | 2026-09-29 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 02497b39-a68a-392e-ab6e-186f3f314924 | -8.3614 | -45.424 | 2026-09-29 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 761537f5-f82d-3197-83ed-9f515c11d055 | -7.064 | -42.0648 | 2026-09-29 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 797143ae-1548-3ba2-8bd2-5aea6ba1cb97 | -9.4702 | -45.8023 | 2026-09-29 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 62a5755b-4059-3fa2-80c6-62754883eab1 | -11.4302 | -43.4596 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 31ee169b-89ea-3421-b701-0958a586a146 | -12.704 | -47.2515 | 2026-09-29 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 55db92e1-5d6d-378e-bb6a-7975afb0c6be | -10.1095 | -50.2135 | 2026-09-29 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 32eea349-db86-3f1e-aa08-f900881a2ebf | -11.4119 | -43.415 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 890b7c30-317f-3a4b-a575-c63db37a9263 | -12.7421 | -47.2684 | 2026-09-29 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 45dfc14a-b987-3834-b4fb-145dd51b7637 | -6.3101 | -52.6184 | 2026-09-29 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4d48c97f-78a1-35ae-93f6-c3d1920c16cf | -12.761 | -47.2881 | 2026-09-29 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| fd689bbc-1733-3a0b-8568-8183860f6c6d | -5.6083 | -37.0076 | 2026-09-29 13:30:00 | GOES-19 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 6ec6b042-2fcd-3e5f-896e-69b6ae63ae37 | -14.5168 | -48.2958 | 2026-09-29 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f3091e7f-36da-395f-81e2-c743eb33c35e | -12.2894 | -50.2927 | 2026-09-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ba457f8a-d8f8-369c-ad72-5d96defab38c | -10.8299 | -48.7115 | 2026-09-29 13:30:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a5a225a8-a377-3015-88e5-f1533f23e781 | -10.3894 | -61.2502 | 2026-09-29 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 8df93455-1d5f-3185-bb5a-a99617fb3d07 | -6.1598 | -52.9134 | 2026-09-29 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e336347c-86de-3787-aa6e-3a00266f4c7f | -14.1115 | -46.2834 | 2026-09-29 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 261.3 |
| 76506c74-89e1-385f-a1b3-26828a009246 | -11.1327 | -50.0624 | 2026-09-29 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 34c37b17-dcaf-345c-bbc4-63e69c055c31 | -12.2911 | -50.1849 | 2026-09-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b0fff8d5-8bdf-341a-8a4e-0c9f54651605 | -13.6762 | -45.7822 | 2026-09-29 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 402.6 |
| dc3b5109-bbb0-3c18-bad2-dec7f3c0ef9b | -11.4311 | -43.4121 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3c01b72a-fd6d-3c6b-9159-7d822c5aa173 | -7.3967 | -42.6261 | 2026-09-29 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 29bdecfe-6f13-3a2a-848d-4bb6eacaf032 | -11.1583 | -44.7859 | 2026-09-29 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 15c0bbe3-f7ec-39be-a5e1-4117bf3ccbcf | -10.7255 | -44.4291 | 2026-09-29 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ab44d723-77a5-31f5-b1ce-93d06ebf08e2 | -8.3611 | -45.4468 | 2026-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 404a2e4f-967d-3d51-b70f-c94facb782fc | -11.1327 | -50.0624 | 2026-09-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6e591ef0-d322-3112-83bb-5db3e583171e | -12.6463 | -47.2598 | 2026-09-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 1c26198d-0d73-30dc-8fa9-70ddbfc983f2 | -10.3894 | -61.2502 | 2026-09-29 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 2319e32d-8773-32cf-b78d-33e767d65073 | -14.639 | -52.1307 | 2026-09-29 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 68938e7b-2210-3d38-b20f-84088a6aa5ef | -11.411 | -43.4625 | 2026-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 07e070f7-130a-3652-95c2-f7fe34f6be26 | -10.7913 | -48.7596 | 2026-09-29 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0a20cf9f-eeb0-3fdd-afb8-3d351c3b2554 | -12.7421 | -47.2684 | 2026-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 427.5 |
| fd3c2f0e-60c4-377e-85fa-a766cf8cf8c7 | -14.1115 | -46.2834 | 2026-09-29 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 16524939-7681-3d95-b255-d9381bb23319 | -11.9612 | -50.568 | 2026-09-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d6baf255-82c2-3e83-8a13-760aee75f905 | -9.9593 | -50.1644 | 2026-09-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5219a822-969e-3b07-90a7-40ef021a3732 | -14.5168 | -48.2958 | 2026-09-29 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 594a7ee4-4391-3f3e-8ecb-cec35c74cf44 | -11.4298 | -43.4833 | 2026-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 6ee30a06-9220-314a-80e5-d433b515c60f | -11.1771 | -44.8064 | 2026-09-29 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 297.4 |
| d76cde79-3712-37df-9362-19e51f835dcc | -12.761 | -47.2881 | 2026-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| c6f846eb-7b07-3cff-ba87-61b2e65fbec2 | -12.7417 | -47.2909 | 2026-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 195e15bb-e599-35ee-978a-d799c71478fa | -12.6848 | -47.2542 | 2026-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6c0f3e30-48f2-3374-a9a4-9daa705e5ee9 | -7.3967 | -42.6261 | 2026-09-29 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| ce700e52-7c24-3404-acd9-4afffdc4a4b3 | -9.4702 | -45.8023 | 2026-09-29 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9694e0e4-459c-37a4-8343-b7de8809c8af | -13.1799 | -48.5631 | 2026-09-29 13:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| cc7e6114-49c0-3978-85c7-ec6fc3ba2258 | -14.5362 | -48.2927 | 2026-09-29 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f5a1787f-deb7-3450-99a8-7657fa9e5eef | -12.2901 | -50.2496 | 2026-09-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6add1065-7a46-3cdd-9aa1-aaf14db0d1d7 | -11.4302 | -43.4596 | 2026-09-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 0fe490e0-d73d-3b58-a49a-5943e6bd7a46 | -12.6271 | -47.2626 | 2026-09-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 2bc45249-1b50-3fb5-870d-4e830a471f77 | -7.3965 | -42.6498 | 2026-09-29 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 08cebb58-132f-34cd-992c-4a60c9932918 | -11.1775 | -44.7832 | 2026-09-29 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 579.4 |
| 60822975-f097-3538-b123-b4298f41f868 | -10.7916 | -48.7377 | 2026-09-29 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| be52eb6a-9dbe-32db-b162-c7eeffff6632 | -9.9973 | -50.1393 | 2026-09-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 95d70c3e-db4d-35bd-8023-eee8ecc409d2 | -12.704 | -47.2515 | 2026-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 55c62bf7-8ad4-355a-9e5a-a99a4a8d1a2c | -8.9633 | -44.1655 | 2026-09-29 13:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ad51b8b9-694c-305d-8716-9832142be6f9 | -12.6078 | -47.2653 | 2026-09-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f4fa50b5-3f82-3313-99bc-7b7d2e88cf45 | -15.3998 | -47.9261 | 2026-09-29 13:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7ee8bcf8-b578-35e5-88fb-96284fcb3137 | -10.3895 | -61.231 | 2026-09-29 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| f81b8ceb-8f92-3516-9457-2cddbb42200b | -8.0355 | -42.866 | 2026-09-29 13:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |
| b25fd12d-1a15-3505-a747-f2af8d4836bb | -8.6451 | -45.3489 | 2026-09-29 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c3d78580-0cc3-3220-8887-4493db6c17ff | -14.1309 | -46.2801 | 2026-09-29 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 141.0 |
| a10d5d10-3041-3f14-a232-3ea1bb54f419 | -8.9823 | -44.1633 | 2026-09-29 13:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7e1deeb9-6b20-3fa1-a199-d8806777940b | -11.1517 | -50.0603 | 2026-09-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1641ab4c-cda7-3a5d-8ac3-d4ff9daec230 | -11.1897 | -50.056 | 2026-09-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| dbe09dc3-be81-38a0-92cf-824b2109f1ba | -13.1992 | -48.5603 | 2026-09-29 13:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1b78ee09-adf2-3879-87e7-d44293fd496c | -18.1144 | -44.3988 | 2026-09-29 13:40:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 147.1 |
| cf6da1fd-c936-30e6-b2d6-9bb813de399a | -18.1151 | -44.3745 | 2026-09-29 13:40:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 76f2476e-25dd-3b3d-91d2-a07dcd3b5cc4 | -11.152 | -50.0388 | 2026-09-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 13585c3d-93e8-33b9-84f4-4494a7cf5b76 | -13.6762 | -45.7822 | 2026-09-29 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 96a50ab9-849e-3381-9d15-cbc90ab7924e | -11.0241 | -49.7088 | 2026-09-29 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 123d02d0-2dbb-3de0-b22e-f28cf996ec85 | -12.8847 | -44.8015 | 2026-09-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 38dab86c-06f8-3dd7-a04e-7b277f5e16a1 | -10.7056 | -50.8341 | 2026-09-29 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 95fd2aa5-800a-3b07-8694-57b250844893 | -12.2897 | -50.2712 | 2026-09-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f831e62e-dd1f-3e15-a247-5633d2a257fa | -13.3469 | -46.8169 | 2026-09-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 93285b25-b2c3-333a-8c1f-d3ef390cc5a5 | -14.4839 | -47.0414 | 2026-09-29 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 1109e543-ee7d-396d-899d-fb4b5c1d469e | -8.3614 | -45.424 | 2026-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0e259912-f23b-37db-a9ba-625a1af54122 | -9.9595 | -50.1431 | 2026-09-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| dc9918aa-0860-3cb2-a4d5-1ef1bba6ead3 | -9.9784 | -50.1412 | 2026-09-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 43bfe0d3-eede-3d90-b18e-105538ab3925 | -11.1958 | -44.8269 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 48957fe4-44c1-345b-a053-41bad50f3658 | -12.1731 | -50.4142 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |


[Clique aqui para ver as próximas entradas](README78.md)
