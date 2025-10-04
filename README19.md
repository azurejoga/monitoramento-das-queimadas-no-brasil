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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03149637-87c2-33e2-a53f-073ae52ec419 | -6.28042 | -45.08399 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c401933-d942-3be2-85f2-1bf5bb7ab2c5 | -6.27678 | -44.04521 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ea44d6d-d774-3ec9-93e4-ea9521234954 | -4.61145 | -43.14919 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c7d3640-506a-365a-a4e4-11e76c52d30d | -11.41987 | -43.48629 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b57da1f-1eb2-35c0-ad3a-c810db224ff3 | -6.71247 | -42.1652 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d419e1ac-a072-3289-98d2-11ebfa2c5962 | -6.6977 | -42.83353 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25812437-8274-391f-84cf-96dcc039efa6 | -6.27122 | -44.04931 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a075d45b-8d7b-34bc-80e2-63c882830723 | -11.4796 | -44.98305 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d022fc-4733-3542-82fc-023234c46c48 | -10.6402 | -49.14241 | 2025-10-04 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72d0ee01-149b-3db8-9d48-7ec74038aed4 | -8.92047 | -46.6103 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e4b5dd0-cf29-3021-9653-7f81f981e4a0 | -6.17128 | -43.91982 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6779edaf-7b93-3052-b626-2b7dffd73c6f | -10.33731 | -50.33884 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 632049a7-905d-3b4d-9546-74155c7ca458 | -6.09801 | -43.45054 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbfc465d-9356-3e55-93ed-966393cd1dda | -9.91094 | -43.79415 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a436660f-a4d0-3a34-a6f8-80f785b9a9a2 | -7.04846 | -42.77956 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bcc56e4b-b0f3-35a0-926b-2e6638f4c425 | -5.82186 | -42.87658 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ae8f09a-be39-34ad-9ce4-c83c8bb775cc | -11.48306 | -44.98671 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16552bc7-954f-30dd-bda7-3a6198533447 | -6.24218 | -45.34867 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c89984d-b08a-3a5e-b861-a38f75bbb668 | -5.30814 | -43.10012 | 2025-10-04 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adc8bf30-fd1f-3a5c-8bca-39905859bae5 | -11.48107 | -45.02801 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cec4c18-d7a4-363c-8a34-3ef209fe81f1 | -6.66181 | -42.82506 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6309bd0b-f2f5-3658-b560-897559a83da0 | -6.35565 | -43.44876 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b58880c-e715-3215-adae-68204d85588d | -6.70335 | -42.82643 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a326d128-b47a-3eaa-bd32-1ce96eaff07e | -9.99733 | -48.28005 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56536807-7e7e-38cb-aff6-d8049f3486d3 | -7.76252 | -42.52082 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eaa59b5a-82ac-3b91-a65d-a9a29dca3dc1 | -6.5569 | -43.10146 | 2025-10-04 03:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff621cd2-2da2-3daf-9bfe-ce1e0455eb8e | -8.229 | -46.80878 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd1476d1-5427-3d56-a162-bc5dbf7bfc5c | -11.44758 | -43.4992 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1759a410-ac6d-3b9d-ac4b-f1c979d3f019 | -7.86302 | -48.20358 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 461c1327-6887-3fac-a088-5eed85fd13d6 | -6.19101 | -42.71573 | 2025-10-04 03:51:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5435d3f-0811-3b37-987c-00c9dc7565fc | -10.80436 | -48.8221 | 2025-10-04 03:51:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f9a09be-4e45-385b-a2bd-510d45dedd87 | -7.16118 | -44.99446 | 2025-10-04 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5268dc71-b4d8-339b-83b6-25dd510800b3 | -6.64667 | -42.80984 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 70868e42-d801-3d43-89fa-d3c926e21b29 | -10.83597 | -41.27625 | 2025-10-04 03:51:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8dcbe77f-8547-3bcd-96f9-4b2e347ad6db | -11.17643 | -47.74858 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d404301-2f65-3d71-be5f-fe9e7da70bf4 | -5.88426 | -44.27139 | 2025-10-04 03:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a53c4a-2989-3048-8b1e-126bd9dda365 | -9.9138 | -43.80337 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7905627-e5e6-322f-a1ac-727d4020fd63 | -7.69826 | -42.57162 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d9cd0764-72b9-3879-bc99-d1fb512aa99a | -6.34439 | -43.46057 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 137a1aa8-4f21-3e92-8bec-1ed76dfd2367 | -6.67403 | -42.81687 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f030e16e-a4f3-3d5a-8461-0cf65492d470 | -6.35284 | -43.44603 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08d98896-0d4a-3c50-b194-ae77df007285 | -8.90659 | -46.05488 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d3d13f1-6461-3309-8d65-c6e289b53ab0 | -11.09865 | -47.71111 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc7f234-59f5-3c1a-89be-afbd96b16d31 | -6.2478 | -45.3368 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 037d8d9d-48e0-399f-af9e-416445f19cb3 | -5.73559 | -42.93377 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cce4961e-2348-3a89-b93e-b2cac5a33762 | -11.08883 | -47.88068 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66015095-9cb3-3be0-95bf-88c4f84dedc5 | -7.72164 | -42.56014 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2ea66904-c230-3668-933c-ccd62c333bf5 | -6.65233 | -42.8025 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f001d11-4b9c-394d-84d4-307f0d396238 | -4.71437 | -46.12832 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f32c980a-c706-3934-9536-80bb3bb155b2 | -6.36361 | -43.90401 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e1f334c5-3bd5-3ff2-b499-a163515d7c9e | -7.6976 | -42.5754 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b94cf7e1-324c-30a6-a33c-d2f9d510c04d | -5.72418 | -42.68526 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 06f1e0b8-9cc5-3f2c-b5d3-731985436c93 | -6.87841 | -47.23592 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bb9b355b-5729-39ff-b3c1-af21204cb6c1 | -10.9908 | -46.67403 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3afcda8f-3070-33bd-a14c-7c88035c7017 | -7.74315 | -46.3052 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f3da68b-bb0f-3ba3-b243-f9b6d1757540 | -7.04623 | -42.76694 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b28bef9-1b01-3fbb-8e4b-5fbb23dac736 | -9.93235 | -50.24591 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 151ab6f1-3c6d-33da-8be0-d6487a8b6ed6 | -6.34459 | -43.44012 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dad768b3-6714-32c4-afda-89eaeb95fd34 | -11.50139 | -45.01579 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f976f090-4fd5-34c2-ae6c-05010041d3b9 | -6.87714 | -47.24152 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 287508f2-f58c-3766-9a90-017ee2602e79 | -7.70526 | -42.58059 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49591de7-973b-3b23-bcd2-66872fe917a7 | -7.85949 | -48.1962 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7aaeea0-3581-306d-9122-be8f62def77d | -11.45082 | -44.95888 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f842c7-703a-3253-a812-f26f679f7c1d | -8.19246 | -47.00227 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a331fd98-0a95-30b7-8fe3-f913139a8f2d | -11.47589 | -45.02523 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9d60e89-da85-3774-90b5-5744bbabf148 | -11.7064 | -44.43731 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 111c8e5a-5c26-371b-8712-58bb9cf460ea | -6.37538 | -43.89096 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c27be0cf-8c0c-3690-af57-823504d5db54 | -7.79693 | -42.55303 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cfb2eed6-6c60-3e27-b228-252e4a4a6f93 | -7.72709 | -46.30245 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05f00a89-7d4d-3008-8974-23fa8cfdca20 | -9.3214 | -45.76508 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0aef8437-6837-3e48-8cc6-b8f55f78473d | -5.89711 | -42.53946 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3c9ff2f-3db0-36d0-ad84-e2c3792b3529 | -5.82986 | -42.88242 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2833bd51-f1ec-3475-88bd-a3c3a5d47029 | -7.77339 | -42.60813 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 07d6a6a2-6830-39a3-8a50-d241b6976e28 | -11.44343 | -43.49841 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f78d0943-670e-3eb9-a77e-9ee6bd05c17b | -6.34599 | -43.45862 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed0ee443-3afd-3451-9fcf-b577e6e3ce57 | -11.47484 | -45.0363 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a8c764f-f11e-30e4-a0da-876ea2f833ca | -5.33333 | -43.34446 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50ae4b34-c7a2-3d2a-a6f3-f78d73fa78a9 | -4.44161 | -43.24338 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4806907a-551d-3c16-a3f2-bff9a70eb122 | -11.63427 | -45.06073 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655e1ce6-384a-38f9-bb00-ca11cfff0c26 | -7.01714 | -44.85404 | 2025-10-04 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c72a54-3dce-3205-af47-7eed40601e6c | -6.687 | -42.84424 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5ddb0b7-2643-32b9-9a74-01e3800da677 | -11.05681 | -47.78878 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e661899-6fbc-326e-9649-84c273a45735 | -6.37258 | -43.89309 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9e8d9d7-a199-309c-a652-7bbe5fe179e3 | -10.32081 | -50.35315 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6f93fa8d-3e6d-389c-9783-7d14dce1ab9e | -7.73529 | -46.3182 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 670518aa-bce9-3bd9-a578-7aef4cad01e2 | -6.35048 | -43.4595 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7549f66-bb75-3135-bbb7-e7d74ba9e6b5 | -7.73877 | -42.6101 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 206e81b6-c9e6-3692-b5df-271acd4d2498 | -5.98839 | -43.49041 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bfd3b7a1-3e10-365a-a758-67ee9f85004f | -8.53254 | -47.21835 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b12875-41ac-3729-a3e9-f8f5fd1da8fc | -6.60496 | -44.29699 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebf28506-d40c-32f2-adb8-3af0876cdc93 | -4.44544 | -43.24882 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0376d79a-573c-3141-b806-89a3e4e816bb | -7.46792 | -46.85471 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29137f45-bb02-3103-9603-47c2d10f798d | -6.29466 | -42.49012 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 231c1465-81c0-3ec0-8b97-caceca06956c | -7.86825 | -48.20905 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89b693b4-5c3e-3760-a816-c1f7b849bc02 | -10.34368 | -50.32819 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0829f4a2-db9e-3ff0-acd1-56918a3e536a | -4.70014 | -45.60706 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc109be1-c178-3b71-a127-d3b942e94ed6 | -9.91244 | -50.50379 | 2025-10-04 03:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ec0ecf0-0a75-3432-8445-8fe471e155b4 | -6.69342 | -42.83265 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a74e2f21-e592-3fc1-bd7a-a3d2271c1499 | -8.20181 | -46.99201 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1660b14-f3e8-3dbc-9de1-1f31f822220a | -6.37456 | -43.89582 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README20.md)
