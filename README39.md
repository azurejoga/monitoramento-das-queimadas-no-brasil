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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d45f56d-1606-303a-8cff-6c3e35a32a48 | -10.47393 | -49.38644 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 159a5e5e-fa65-343f-a0fd-29b369de700e | -11.45274 | -50.21059 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7711a03-0ac5-3086-b675-627a67494179 | -11.11136 | -54.04834 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2c8413d-34a3-3748-b92d-49c05c2f35ef | -11.29512 | -44.92667 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c33612e4-c573-33b6-966c-179ac2566311 | -11.81343 | -45.13646 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed96127-80c4-3fda-851f-c379b8a717bb | -11.93844 | -51.47645 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fa7e5b3-dc72-3e4c-94f3-d7dfb4934199 | -11.33913 | -56.20245 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 756a6992-4366-39f5-9ea8-e5e65324ec27 | -11.16996 | -54.86953 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbd6258c-3ca8-3783-9879-516b23be35a2 | -11.78926 | -45.05195 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b527cea7-c5eb-365d-a51e-4a10e8c8347d | -3.35165 | -42.32926 | 2025-10-08 04:17:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d8eb165-c433-32b9-aef5-f864424bdc47 | -7.77996 | -42.4043 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fbc3190-9153-38c3-aa03-7fb1ba65570d | -13.25684 | -47.15731 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1597ce40-7563-3ad6-9eb4-95e326b5f4e0 | -10.40393 | -45.36954 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f49dbbad-9a9c-3961-96eb-d896f4779ec2 | -5.23831 | -45.40836 | 2025-10-08 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6d90d60-f548-3731-bc9d-a99443a35596 | -7.01676 | -42.89097 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 40b19204-eb9c-3dba-a011-9f700e73e4ac | -12.42051 | -45.62245 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007fb559-f10e-370b-abca-42819a7e5aff | -10.42251 | -48.09567 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8aa1d1d6-5637-33b3-a7d6-fb7dfcd4a883 | -11.16413 | -54.86849 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cd6db95-49f6-3a06-88f8-8a452f592542 | -11.63994 | -44.2698 | 2025-10-08 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c4cdde9-9ea9-3a5f-92c4-fc68ff553d9c | -11.70518 | -50.97052 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5dcf9d9-0546-37c8-be06-789a0537f35a | -10.73215 | -47.65877 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 660cb0b8-2890-3f1c-b5e4-c4c9aaa71e39 | -5.73433 | -45.26292 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3933a54e-fc64-33ed-b4fb-62fde5e69413 | -7.52364 | -42.98147 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca1ae843-c197-379e-b730-c47ab0d30010 | -5.80867 | -44.05201 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b2eaf9-70a8-3130-8198-152caf4444ad | -11.76452 | -46.81461 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a4fb66e-7537-3aa6-9adf-a50516b2c078 | -4.4996 | -46.36786 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 629fbaca-b00e-305d-9b2b-7aa8dd6238a8 | -4.48289 | -49.71189 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0428c44c-6750-308f-8801-ff2d23b4dd9e | -12.74558 | -44.7207 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26219b31-78c1-3eab-901c-243d292e67cf | -12.36412 | -46.49522 | 2025-10-08 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a9053ee-1b0e-363d-9ad8-73f7259ed35c | -11.72683 | -50.96392 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00c5f91b-632c-3a96-a87c-51f8a46b0971 | -7.47679 | -43.0671 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90635f11-fac0-3e77-ad6a-1769d9ffdb32 | -10.64615 | -47.45743 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c3fe951-1ed5-3c51-9c3a-8ed7080386ea | -7.02064 | -42.88801 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| e76bffa4-119a-3427-b129-bc9714b9161c | -11.14584 | -54.86956 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b954fe31-619b-3985-b057-ee1e82c753ec | -12.38953 | -51.1423 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e50dbf48-8cbe-3740-9273-9ac4228dea3d | -10.68229 | -47.55115 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d668959-b53d-302a-9018-15e5bd4e9be4 | -5.91596 | -44.19624 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a8a7c2b-a640-33ea-9b1e-d96802da1849 | -11.11758 | -54.0457 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c000c863-6dc8-3558-b983-db56f575d343 | -5.25438 | -43.15001 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c4f78f4-c984-38e4-b77b-91cd884fac50 | -11.77438 | -45.14459 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e3ebb10-4bba-3209-a61b-f6e2970a6af4 | -12.93274 | -46.84593 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4dc90b9-5758-33ae-9d3f-bab32989dbe0 | -5.75954 | -45.75663 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d432859c-187c-3357-b485-b22505d5ff49 | -12.37639 | -50.2999 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b40c90a-4fa8-3f7b-bb38-bf05ea709448 | -7.31628 | -39.25307 | 2025-10-08 04:17:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5d0a065-fda2-34f2-8ae5-6f2345ef0bc4 | -11.84312 | -44.90786 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ccf495f-db1c-3bbf-8aed-c491ef826b99 | -6.66436 | -41.38907 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5feec840-6452-3f56-85b6-d26fd1aeecad | -13.23691 | -47.18996 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1197eb8-e61e-3439-96c1-fa59121bcc33 | -6.17242 | -44.68414 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 281058a1-bf44-3e91-9331-6e72a2a0fcc4 | -7.44863 | -43.13764 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3629dd50-33f2-3b5a-b216-2a7e5675fd14 | -1.41149 | -46.70274 | 2025-10-08 04:17:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02520b8d-2c61-3c12-bf3d-820932091859 | -12.94405 | -46.86388 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 092fa280-bc17-3f4e-a2a0-d797f50ec2e7 | -3.14334 | -50.44606 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da92afe-6221-303f-a039-d06890042b9b | -5.82877 | -44.08786 | 2025-10-08 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ac77870-b4a5-35c3-8f18-e8c0e4866727 | -11.16757 | -54.87543 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e29b7a96-81b3-3bd8-aa48-a340e8091fa9 | -5.31525 | -43.08857 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 674a6ee8-31b9-3ce2-baa0-83ca0736e05c | -12.01317 | -45.19806 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5526091a-6223-3da4-9ee7-cad958506cef | -4.4966 | -46.36287 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1fcf7755-49ea-3adf-9dfc-7bd9a2ad85b3 | -12.02654 | -45.20029 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0d2a5fa-d9a1-3311-81c7-c8a7d145b3b3 | -7.43865 | -43.13606 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 132af548-6705-35a0-a961-2ec857f0032f | -7.24355 | -44.14969 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7920a05d-a615-38cc-8047-061a849dd3e4 | -6.06631 | -44.32257 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e84a34b8-3f5d-3c79-a4e8-3cccfbdc7eda | -7.23856 | -45.33127 | 2025-10-08 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a329262-44aa-3e12-8dde-529e6f13b045 | -12.74502 | -44.72425 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e57b9859-9c8c-3411-907e-285d8c88fb15 | -2.88242 | -50.72895 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0983d2d-0316-3b58-bf21-3c33279491e7 | -4.08569 | -48.04593 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10adb538-85da-3380-a9f3-2123e64d0c1c | -10.67155 | -54.69765 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc6756a-05aa-3aab-9ccd-f8979cd71e94 | -12.93711 | -46.86266 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b252898d-647e-3b6d-8600-a34db0983ae5 | -3.22219 | -49.35915 | 2025-10-08 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 537ea8d9-705b-3adb-a904-f44b33e12e85 | -7.00453 | -42.88189 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ead348a2-f310-3d83-95b0-4d571e98ea0b | -12.86475 | -42.62645 | 2025-10-08 04:17:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 89c6230e-f35f-3f17-bb07-78126eae9eeb | -13.23129 | -47.79357 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0155cab8-9638-3483-9006-dced0c103393 | -5.64667 | -43.62202 | 2025-10-08 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09dcb08d-ab36-31cc-91e6-55c7211486d3 | -11.48077 | -43.48911 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0f6f718-178f-36ec-a215-1e130ad3b43e | -11.15926 | -54.88681 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55fdc95b-b89d-3774-a40d-221026593dce | -3.09187 | -50.57167 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d37f897-46da-3839-a90b-c374f63bd765 | -6.57142 | -44.15084 | 2025-10-08 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 930333eb-0ed7-3bc8-aa46-935a11b398b2 | -11.22126 | -47.7659 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e3b7fd-b917-38ed-b846-fd65f940f3ab | -5.7187 | -43.61547 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0eafac14-39f4-33f7-9769-bc910db8f5c5 | -11.76943 | -45.13272 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22034d8b-7842-3304-8658-85597d8d9f5f | -0.90012 | -47.55038 | 2025-10-08 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2dd44846-ed4e-3744-8c0f-012905d5227c | -10.41791 | -48.09976 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a817c07-254d-3287-8be7-a1bdff310adc | -5.96695 | -44.83207 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec99ec4-2fa9-329f-b644-9a19862ed573 | -5.71814 | -43.61897 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db3cdc99-ff1f-3c03-843b-00588fadfd12 | -11.17655 | -54.86659 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2231951-3234-3eaa-8199-f9102e998e8d | -10.64744 | -47.79857 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfc2aad6-8c87-37b7-a9ef-9c7e9f906c25 | -13.36849 | -47.22477 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75546e6b-028a-3090-b438-1a98ff623f0c | -11.15247 | -54.86644 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 219a2f85-8a6a-3916-8ad2-a4007b377d96 | -5.20483 | -37.62854 | 2025-10-08 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e5d2258-bd0d-3189-9751-02cc13d9e641 | -12.16095 | -51.44418 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf85c887-f2c0-35dc-9539-b84b02113eb8 | -11.77496 | -45.141 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83bf832f-60ff-3181-8df2-8d783a153c22 | -11.78499 | -45.14268 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34bdb3dc-b1eb-3e1e-87d9-9900a03eba3a | -5.86693 | -44.30213 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0604b7dc-08a2-3b25-8e3d-32190a60ec66 | -4.68462 | -45.83504 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b086ed64-f4e8-3552-bcb1-ef0d5aab5a93 | -10.73288 | -47.65441 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9cec57f9-fb99-378f-87c5-52ca42956181 | -4.41942 | -40.74831 | 2025-10-08 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 123e9ffa-ee79-3f11-8b92-2827ceee09fb | -10.85688 | -47.1182 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a6c07b7-06fb-34e2-bf76-8b1908f69289 | -11.11625 | -54.04593 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f33bd67-58aa-389f-8d95-00f3f2a92cf0 | -10.04494 | -48.2877 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2d7805f-2a8e-30f3-9cd6-18b8bedf7578 | -4.50553 | -46.35509 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 121cf5ba-34bf-34ab-b125-22146969b94a | -7.28437 | -41.97968 | 2025-10-08 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README40.md)
