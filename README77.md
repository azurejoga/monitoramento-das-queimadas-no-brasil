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
| 1e97b6ef-f907-31ad-a0a9-ef9449acfa93 | -11.64201 | -48.52915 | 2025-10-29 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6865d6bb-435b-31b0-b7a2-5cd02d320e1a | -11.01181 | -47.56854 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 502fcd01-ecb4-3fc2-b085-6ac6b445352f | -10.64213 | -47.9019 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba27bff9-7fff-3bf3-82cf-4cf982f00e2e | -10.76798 | -47.88781 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 102a2629-de8d-3671-9aef-9f41520885ff | -11.34004 | -54.39178 | 2025-10-29 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4fe462f9-ed28-345b-81e6-465f1245b5dc | -13.64607 | -46.46434 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 135f142b-000b-3e86-84af-3e16123f8fa0 | -14.61213 | -48.4004 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b223b3-158b-368d-83b9-95e4f8332990 | -13.2346 | -47.72542 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6775063d-cc85-37fc-963e-a3b3c2b9b231 | -10.75071 | -44.75637 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe8e7b6-2568-3bb5-9490-484d8c040364 | -10.21326 | -45.95384 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f46e2f68-c4ff-3ca2-a280-0d2b560b86ca | -13.56569 | -47.34555 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9b794be-dbd3-371c-af9a-1ac6ec4ad94f | -13.60833 | -46.48412 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f68935f-a2c0-3ce4-bc11-9f11939d4dff | -12.65624 | -52.62333 | 2025-10-29 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74df739d-461d-3637-9b58-5b1f0bc7aeed | -10.51861 | -47.74219 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d14d9856-6495-344c-9aaf-285bd3bc3e1e | -14.26616 | -47.31683 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0500ca48-2661-382e-8ba8-a8abe97ebc7d | -10.76356 | -47.8917 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e4d92ff-db8e-3b07-a99d-cf63a6517e86 | -13.698 | -47.67337 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c25a50ec-556d-3729-88ab-1f9569dcc2ad | -9.92865 | -47.6816 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17457fb6-536c-379d-979d-200fd310e06f | -13.63628 | -46.52312 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75832ef4-9de1-355f-a9ba-213d02f699b8 | -10.8708 | -48.62693 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b166a8c-ae47-3da2-aaa5-2deae6f080c1 | -13.05301 | -48.62542 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e4cf53e-b9c4-35f7-b501-a4f1c5feedf0 | -11.41798 | -51.40166 | 2025-10-29 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3840750-bbc6-3fc2-8723-81bcdc4c0131 | -13.58752 | -48.52879 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cab9c56-fcbb-3929-bf3b-52dcdaf7b43e | -13.70329 | -47.68053 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5cebcf6-791d-3896-8093-5758be5ca24b | -12.35652 | -50.15445 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 886eacfd-d2a8-3829-bb61-fb7b07387d84 | -13.57814 | -49.59509 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d6cb1e94-3aa2-33c7-81e8-cf7e5dc20fc7 | -13.2108 | -47.06186 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1f007b2-d4de-32e3-89a3-05f869748758 | -13.56651 | -47.15347 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 955eaee2-ce49-3c86-8c46-450ae57185b3 | -14.51868 | -48.00658 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771b07ee-6721-3245-af70-694355f791d1 | -13.55286 | -47.17023 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d45e5655-e251-3412-9093-0b70adbee1b0 | -12.09269 | -47.25671 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cd8b975-0869-39ab-8f34-d6cb00f3d717 | -13.05608 | -48.46732 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b50abb41-a556-35dc-b5f6-57a6951a2247 | -11.25751 | -47.81391 | 2025-10-29 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71fd0a54-0731-3376-9b5d-c8b7671c20b6 | -13.64058 | -46.52369 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26b168c6-1fe2-3a41-9718-adb9f2b123b6 | -9.33359 | -49.82201 | 2025-10-29 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f88699ae-e41d-3df8-8cc1-34a51e0624a7 | -10.60148 | -49.61375 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8fac0a4c-8189-3a28-945f-a84f810821b3 | -13.64476 | -46.50595 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81d49165-5a91-38bb-82e5-558a7429e467 | -14.31231 | -46.51979 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ce21449-91d9-3c3a-923e-f028343ee1b5 | -14.19437 | -48.35543 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 567f30b5-2171-3235-90e5-8c81176a0b2b | -9.08946 | -47.81684 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a94e64b-4527-3bbf-b1a9-bd36e08eb630 | -13.6442 | -46.51003 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a08da173-f9ca-383e-b1eb-c8db0fd410f6 | -14.14032 | -44.14339 | 2025-10-29 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05b900d4-8687-36dc-ad3f-ec08f9df0e0e | -11.35639 | -49.98657 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7e527ce-af96-35e1-8980-c7ba63af73bc | -13.60724 | -46.49227 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2805566c-8ca2-35a5-87d7-72470c3201cd | -10.77211 | -44.62837 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d60a98c-d5bc-39ae-9861-1704d061742c | -13.05671 | -48.46275 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4585613b-2cf2-3ead-bf18-962a9d73f375 | -13.63682 | -46.51899 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b18a4e28-bca6-393f-8776-929feaf6ed06 | -13.36092 | -47.38711 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 156d0169-00a4-30b4-a188-5ea10e66c867 | -13.91827 | -48.45686 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e78d7f3f-63dd-33d9-ba94-261fc2fcf486 | -10.5275 | -50.00582 | 2025-10-29 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5905a5c3-6e19-300e-be94-9fc4a4de7f86 | -8.72524 | -49.76785 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2776d98-e46c-3f00-b6a5-93936696e9f8 | -9.43876 | -46.90681 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| f489de1a-cf75-3dc8-ac03-58b820433835 | -13.6427 | -46.50733 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4201dfdf-a36d-3d39-b3a2-916096554a1c | -9.88279 | -44.88564 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9cc558b-065a-3ec7-bc65-73ff23a1b34d | -9.56565 | -44.71476 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ee2809b-e7d6-39c8-a432-0b4decd697e0 | -13.64709 | -47.02383 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc093b3f-780f-31d5-951e-038fc7272aaf | -10.85747 | -48.64215 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 797db2fa-06cf-3526-b2c7-893e761bff3c | -10.97338 | -50.25143 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a956449c-c6ff-3282-931f-9fb456a0e964 | -14.28027 | -47.3056 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65019038-30c6-3a0d-ae21-ffac2055c9a1 | -13.36927 | -47.38627 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3fc5ecc-3cff-3c6e-acd5-4f04c2350adc | -8.10517 | -55.09076 | 2025-10-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a87fef0-1648-3f56-8a04-925880e123f7 | -12.69756 | -46.30166 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b6766a3-1e6d-3959-acf1-719cccf25585 | -10.62223 | -47.88003 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80f2ba98-ae45-3540-9bd0-0279ccc06fd3 | -11.34 | -41.6715 | 2025-10-29 04:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75081c93-3a04-38ec-8a83-0a0db8b685ca | -15.11211 | -43.26646 | 2025-10-29 04:46:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da9d88ea-3f22-300f-8f5c-d189185dca71 | -15.15802 | -47.23072 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 577a5c21-19f1-37fc-a427-bea5a8fbe471 | -19.38492 | -43.63286 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec097e9c-e11f-36ef-a809-a267138e2b98 | -19.37782 | -43.64685 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11451986-d5d3-3f4d-b046-97397625e3e3 | -19.33733 | -43.05432 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 661743b6-9fc6-3a70-95be-8e52a8682bd1 | -19.86809 | -48.33311 | 2025-10-29 04:49:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6b217eb-11f9-3f19-8917-e2a7f6305dc5 | -18.8286 | -41.95426 | 2025-10-29 04:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5909198e-40ad-3410-bae1-1f22663a260e | -17.25804 | -45.29015 | 2025-10-29 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b49c7947-b780-391f-b90e-7cc4e5b453a1 | -17.53166 | -44.62041 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f23d724-6e2b-3106-a4a7-1f91eadacf9d | -19.46184 | -43.58327 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af540452-6c59-339c-a28d-8ed2042f6f28 | -20.99923 | -42.80101 | 2025-10-29 04:49:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4f078b01-9076-3462-a6c7-cd0e53efd172 | -19.33238 | -43.04483 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8ebe78a-7416-35ea-9fb0-c51b76fbe951 | -20.80095 | -42.75451 | 2025-10-29 04:49:00 | NOAA-20 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f4a3ec56-a8fb-3d26-958a-6e5dca153aee | -18.82815 | -41.95931 | 2025-10-29 04:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8da4a4a-16f0-31a0-b956-364e42eacaea | -19.3316 | -43.05268 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dd6696f5-b48b-39cd-9610-bbcd41a7e26a | -17.20815 | -47.00569 | 2025-10-29 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 933d73c1-c8ca-3cd1-8f1a-9a0d017957ef | -19.42366 | -48.06709 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 675e3945-bf88-3c0c-b45d-1798cc5a69fa | -21.00154 | -42.79957 | 2025-10-29 04:49:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 322a7943-4f6a-3998-bc6d-25a36f0dea48 | -18.92595 | -45.0493 | 2025-10-29 04:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0a3d6a9-bb2d-3ee3-96c5-3bc62643acbc | -17.2027 | -44.45557 | 2025-10-29 04:49:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ea28c3e-492b-3f35-85c5-00eb365fa7dc | -19.33811 | -43.04635 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b73e702-c8c7-3e58-bbc5-3d9de56ecafc | -19.41896 | -48.0705 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c60cbb4d-a969-381a-82ee-38047e71a24c | -17.56892 | -44.75131 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23b1bacb-a71d-3f97-be46-eb6e9f97527c | -17.53743 | -44.61544 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b50ad9-4719-320b-8ea3-338ceaab95c9 | -19.42835 | -48.06376 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29cb85fc-fb06-39c6-a2bc-5c0ef4fe19b3 | -19.48217 | -49.27976 | 2025-10-29 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 577d6f63-90c3-3ddb-87b3-2e47ef4e4b40 | -17.56856 | -44.75444 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28112468-d5d7-3caf-9144-f7604995ba9c | -19.42786 | -48.06769 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fe1416f-5089-3548-9598-09a6550b033e | -19.33773 | -43.05025 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd46adce-9e24-3840-954d-dcaa6241d964 | -19.33117 | -43.05707 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3561813-7d18-3aa6-a0fb-3284ae1ea677 | -18.9263 | -45.04625 | 2025-10-29 04:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91c38bca-07bf-3c94-8802-47a903ae467f | -17.53198 | -44.61755 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4581093e-9cb6-38e2-ba01-b4b4c45bee61 | -19.332 | -43.04861 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1b302dd-ec5e-3fa2-bf62-8bb76cff7af7 | -17.13109 | -45.37983 | 2025-10-29 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46bc31dd-23ef-3232-9b5a-e35b6e46d933 | -17.1366 | -45.37495 | 2025-10-29 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430352ef-0ced-3f7a-9ff7-37d9301cc57c | -18.20108 | -44.33355 | 2025-10-29 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README78.md)
