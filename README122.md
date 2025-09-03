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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4606944-06a1-3554-a786-5589fcf94ccf | -6.6538 | -45.2417 | 2025-09-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 267.9 |
| f60c67ca-9282-3509-837b-61917bef94c4 | -6.9563 | -43.2578 | 2025-09-03 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 0161249e-9951-3abb-8b92-82b773800016 | -6.3689 | -45.6483 | 2025-09-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5a28102c-67c6-3e03-b59b-bac60e94b652 | -15.0254 | -50.071 | 2025-09-03 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c2dbfb9d-b474-3da0-bc08-c749e17a87a0 | -6.7741 | -44.4792 | 2025-09-03 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 62af4bb6-25a8-3aa4-970e-7d6ddcd69274 | -6.2221 | -43.3927 | 2025-09-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 393.3 |
| 5af87ab2-5392-3d13-8b4c-3ccbb557e17c | -6.818 | -45.68 | 2025-09-03 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 565a749e-c3bd-3520-bad6-ca3551f30ed4 | -5.908 | -57.7311 | 2025-09-03 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| 24aa9ace-152d-3baa-af31-92c25c4f0462 | -11.8533 | -51.4318 | 2025-09-03 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 350c1568-7536-3f00-bd97-4ceccea71194 | -9.6229 | -47.0638 | 2025-09-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 0812df92-1f42-3ead-81e9-bc6b060746c0 | -5.8455 | -45.6421 | 2025-09-03 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| afeec041-5d4f-30d5-a514-19b0b1eaee75 | -6.35 | -45.6723 | 2025-09-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 4570ae1f-8bad-3a29-83e6-65c5a170c7cb | -5.7152 | -45.5838 | 2025-09-03 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 5ea7ee16-8889-353b-a0b8-647c94cb017a | -6.6725 | -45.2402 | 2025-09-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1a95c7e0-4b32-3fa6-8c74-b32992a06e52 | -7.5302 | -47.4443 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 421dbc7d-f010-3710-b311-c24d2eeff374 | -25.021 | -49.3799 | 2025-09-03 14:30:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 167.4 |
| 374cedea-4d0e-3d68-86cd-f0fdb80b228f | -5.9081 | -57.7116 | 2025-09-03 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 67a3d606-1126-34bf-8c45-41bbf4c4b242 | -8.8845 | -45.7994 | 2025-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 68005afd-9a9d-35d7-a514-b26412efd1a0 | -5.7922 | -43.2405 | 2025-09-03 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1ecbc8d9-92dd-35c5-9a0b-1e622e73afe3 | -12.6341 | -56.9926 | 2025-09-03 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5ff1921b-7cac-31e8-ad68-06aac32ee7bc | -12.1125 | -50.6358 | 2025-09-03 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a6de1ba6-f0ab-30af-a315-43fbfc7320f8 | -13.5167 | -47.0167 | 2025-09-03 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 422260d1-52ee-3db1-80b2-d0d51ce03c0b | -6.7967 | -44.1091 | 2025-09-03 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 13326b75-56a0-3cdd-80ec-5d614c674118 | -12.6339 | -57.0127 | 2025-09-03 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1924fc2c-f890-3195-be60-56193e46c4e0 | -14.4071 | -53.3013 | 2025-09-03 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b8aed0fd-4123-31e6-ae9d-bbb03c21ee17 | -6.6982 | -48.4035 | 2025-09-03 14:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 712aec18-2c6f-3f78-8ced-840a853e43f7 | -8.8278 | -45.8054 | 2025-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 83d21174-3d36-3e12-8108-ac59a69af7ed | -8.0794 | -45.3844 | 2025-09-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.5 |
| d16e04ff-2638-3b83-98a6-85bfbd51aa72 | -7.7224 | -48.7572 | 2025-09-03 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 138.1 |
| cedf0b7d-5d84-338f-87c4-34911d358309 | -5.8896 | -57.7318 | 2025-09-03 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 38982a6e-529a-3c21-8769-da28bd2fe847 | -6.797 | -44.0859 | 2025-09-03 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| c06d24bf-7678-31a6-8929-6aca59c8d4be | -5.7343 | -45.5375 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 676531fa-4002-3aa1-97b9-80b08ab7fb3c | -12.9861 | -54.7685 | 2025-09-03 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a28e9db3-9573-3b70-a134-9f1e4ae2115c | -14.4149 | -51.6917 | 2025-09-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6feef45e-57b4-3fdd-808c-3ac79556ba07 | -5.8711 | -57.752 | 2025-09-03 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 1b6208dd-2d10-3c05-9572-0d93a4e07757 | -8.3646 | -48.2899 | 2025-09-03 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 59c11808-6813-318b-a005-7372ef3b2004 | -11.0249 | -47.121 | 2025-09-03 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3233c67c-f29e-305d-bc97-7ab1a230a47e | -10.4497 | -54.7988 | 2025-09-03 14:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ade143e7-a86c-3ff8-821d-dd73faeb67a2 | -10.45 | -54.7785 | 2025-09-03 14:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 3576a3fa-a664-35ce-8124-7a7834088535 | -9.1373 | -49.6659 | 2025-09-03 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 3cdddb68-fa2d-318c-b933-96fd6302d308 | -11.5966 | -52.134 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b114f8a6-4493-36f2-817d-17d605662ee8 | -9.4023 | -48.0365 | 2025-09-03 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a5cfb235-b65e-372b-bb1f-1ce9ac3f305e | -8.0796 | -45.3617 | 2025-09-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 2f48dbcf-959f-3eb5-823f-a55ac61eb33c | -9.6226 | -47.0861 | 2025-09-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 234.5 |
| dcc1cd53-88eb-31d3-9513-a0530520591b | -5.7181 | -45.2453 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 740b82dd-5e4b-3dd1-9cef-674cf2671a1f | -16.5501 | -55.0782 | 2025-09-03 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 449.2 |
| a4e17a04-6e8a-360d-84f3-9532bbca1082 | -8.3832 | -48.3099 | 2025-09-03 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 567e26f5-ab27-3e8c-9701-5d61ee362f31 | -8.02 | -44.084 | 2025-09-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 06470f4e-ff23-3da3-a547-776100273899 | -7.9341 | -44.9436 | 2025-09-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 1c308252-19c6-3287-ba2a-49f46ee90fc6 | -12.6341 | -56.9926 | 2025-09-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d60ccaba-5626-3349-8b24-75fd5ac3e2ec | -6.3502 | -45.6498 | 2025-09-03 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 496ce128-cc22-3b61-8cc1-4c9097c77175 | -6.185 | -43.3491 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| d961c2cf-775c-3911-b46e-a6b6bd491032 | -8.3832 | -48.3099 | 2025-09-03 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e5be94d9-fe10-3025-9732-93b3d5a504dc | -15.1576 | -52.3586 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a4885bdd-df23-3617-80db-4fa123549580 | -5.886 | -43.2331 | 2025-09-03 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 03b5c088-cb00-3ee2-a614-0e035d59134e | -6.8279 | -52.8348 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 823cc817-27b7-31f6-b5ff-220dbbf56914 | -6.0291 | -46.0103 | 2025-09-03 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 134d6d8f-4691-3d3d-b263-b2571e4d3b1c | -11.6836 | -57.3518 | 2025-09-03 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 6fecbbaf-89dc-3ce7-87b5-1b931ecd2143 | -16.5501 | -55.0782 | 2025-09-03 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 225.6 |
| 3ac02f62-0e1f-3d87-8d6a-737d0743e6b8 | -5.9264 | -57.7303 | 2025-09-03 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 076ce69e-f06c-387c-8df1-6a277e9cfaf4 | -11.8533 | -51.4318 | 2025-09-03 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| df232cfc-e07b-3d63-917a-178524b39cbd | -6.7909 | -52.8165 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e96bf6e6-fec5-32b8-9be3-158bf2647777 | -10.463 | -53.6338 | 2025-09-03 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8c9c9983-ea17-3fa6-9528-02476c87a0f1 | -5.6817 | -45.1347 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f6d8dd9a-4684-336a-ad1a-c724fc3ff83b | -6.635 | -45.2433 | 2025-09-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 38cbf7b4-03ed-3e3c-acc9-fd2116a4c06d | -6.2395 | -43.531 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 12441873-65fc-306b-9324-b18c2008741a | -6.797 | -44.0859 | 2025-09-03 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 61967f9a-4f63-32ac-89ed-48176ddd6f00 | -10.4816 | -53.6527 | 2025-09-03 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 56f654b1-4e67-3f2b-8d51-c8ef22ac0b03 | -7.5995 | -46.2409 | 2025-09-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e943670b-f0b0-3f23-acf5-8e1b7ce4a974 | -8.8845 | -45.7994 | 2025-09-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 56b26ead-f3a8-33f4-b4e5-4ab9127566dc | -7.484 | -44.8272 | 2025-09-03 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8503558b-91be-39da-b563-9949134e1455 | -8.0796 | -45.3617 | 2025-09-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| a278600f-f8f0-338f-946f-0269bf8d450b | -11.0181 | -51.5001 | 2025-09-03 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 977a94f4-1bf4-3bd1-bb56-dcbd2e4e4393 | -7.4332 | -46.0093 | 2025-09-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 00a9ebca-1287-3697-ae16-a9725312afab | -6.6538 | -45.2417 | 2025-09-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 281.1 |
| 4a1b8054-8dd8-3abe-99d1-d63352a234ac | -11.6156 | -52.132 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 728151ed-283e-3343-878c-43b732991aa6 | -8.0197 | -44.1072 | 2025-09-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b5dfdc67-14ef-3c2f-a007-676818376540 | -7.7036 | -48.7587 | 2025-09-03 14:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 9e4b6a36-1d57-3e3c-bf8d-e9bb37d0d556 | -11.3705 | -43.5868 | 2025-09-03 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 67223942-e02a-358f-b4f1-a743b044a64b | -8.0017 | -44.0396 | 2025-09-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c6acb337-e430-3072-9723-f8706e10b56c | -5.7181 | -45.2453 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 223.9 |
| d00156d7-a7e7-3bb3-93dd-24c6f54d480c | -11.5972 | -52.092 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 10651c74-6853-3dd7-b092-b88ac557fb4e | -5.7923 | -45.3078 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| fbdbb3f9-b9a1-358b-9835-03e8bf5594ac | -8.8842 | -45.822 | 2025-09-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| fdb724d1-e67c-3623-92ea-47fee7053918 | -6.1234 | -45.9139 | 2025-09-03 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8f12e0e9-bda9-3a40-a471-2b4103068a5e | -5.8455 | -45.6421 | 2025-09-03 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ce34d91b-4587-37c4-89c9-1c877efac673 | -8.3646 | -48.2899 | 2025-09-03 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b5637d26-f93b-39a6-8b75-59db30614963 | -5.7004 | -45.1333 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| caaa5134-74be-30ff-949f-1d4f425f5c66 | -7.549 | -47.4427 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6ea7fd1b-39db-364d-8c71-0b9c269fad79 | -15.1965 | -52.3533 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f9513459-6e63-34be-a2e3-e1cbe3fd09a6 | -14.4146 | -51.7131 | 2025-09-03 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4742ef62-b2f9-31ed-9254-d08d95a4ca07 | -16.2949 | -52.9656 | 2025-09-03 14:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 529e7395-82f4-3be0-97f9-31cf8c96b8c4 | -6.8569 | -45.5415 | 2025-09-03 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 96e7a1d5-0d26-3892-adbc-9d84a8581290 | -7.4842 | -44.8043 | 2025-09-03 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5131c6a4-4621-38f2-9b78-024e258b92a0 | -10.4818 | -53.6321 | 2025-09-03 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f18fe262-af5a-3fb9-855f-0810749051f1 | -11.9606 | -50.6108 | 2025-09-03 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 3ce71322-556c-39fb-ab8a-d023fc1e0dff | -5.2575 | -44.4581 | 2025-09-03 14:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d3b58d79-517f-3d91-ad9f-7208f53ecd15 | -7.5998 | -46.2185 | 2025-09-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8ea512ed-22c6-3e87-805e-68e51ac17dfb | -14.0688 | -54.01 | 2025-09-03 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bb87b543-941e-3f36-b669-ba23e771f35e | -8.0794 | -45.3844 | 2025-09-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |


[Clique aqui para ver as próximas entradas](README123.md)
