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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b782ee6-b648-3047-b7a1-748fdb656922 | -13.9997 | -46.345402 | 2025-08-29 00:31:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a446928-cf26-356d-8680-926e2049a733 | -6.5469 | -43.915798 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58871fa-9adc-3145-a20f-2a9e78842dd6 | -13.5995 | -46.8703 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc0c27a9-e46f-3f32-8dc2-50cb30b89b45 | -14.2505 | -48.0588 | 2025-08-29 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c1638d7-4085-3d2c-bf44-eddf14992f0e | -12.0491 | -50.642899 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adb326d3-9f72-3924-8469-c0ef0e48fab9 | -9.3181 | -43.0933 | 2025-08-29 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9817e080-1a44-3a1a-8dcf-51794d52abcd | -6.5387 | -44.102402 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a86dad98-3403-3db0-9f12-c8213aaafa85 | -13.5109 | -46.8396 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a197ed7c-7398-3b12-b934-a56683c12a2c | -10.9514 | -46.878201 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39fb6182-a726-37b0-92b4-0c340f749a30 | -6.4973 | -43.526001 | 2025-08-29 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f435e5d-573b-3ac2-98e6-a71256809437 | -11.3234 | -43.5467 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa3816b8-7ca7-3615-be39-5cb4cdca3ce1 | -11.042 | -45.0686 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 709df659-c0f5-39f6-86cc-272fb9e691bb | -13.4191 | -46.9856 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb5f47f7-fd0b-37fb-b305-e5b9fda86d45 | -6.4737 | -50.191399 | 2025-08-29 00:31:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2583951d-1698-339f-862b-0333815286dc | -10.707 | -47.075199 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c5755e7-6eac-333a-ab33-4676d3e42fe4 | -7.0433 | -44.3647 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86d6ae5b-043f-342f-b216-bfb4080d790c | -15.8453 | -41.845798 | 2025-08-29 00:31:00 | METOP-C | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25522426-fbcb-3c84-bd12-84c246bd3246 | -6.5567 | -43.913601 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98399965-a00a-3cc9-9f3c-861ddc70176d | -12.9061 | -48.137402 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39f242a4-89f3-3ee5-b197-1cfbe4b4dcd6 | -3.7952 | -49.423199 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce73660-8369-3a53-81b7-c7215d870242 | -13.6686 | -46.905399 | 2025-08-29 00:31:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50d99027-c5ef-3aa4-8a6e-70d1a4182f23 | -4.511 | -43.682701 | 2025-08-29 00:31:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3203d98c-210f-3203-b583-4e11264957cc | -8.4691 | -43.703499 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa398b58-937e-3df7-854c-8db786efbb41 | -11.603 | -46.381901 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 543b3966-d041-3668-ae5b-a2d700ee154b | -9.3198 | -43.1008 | 2025-08-29 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08ad33f6-c6d0-3258-b310-5603a79682e6 | -13.4094 | -46.845299 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8176a5bd-dddb-33f4-a019-f8d999b7ed90 | -3.7372 | -48.939301 | 2025-08-29 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e1a227-4577-39cc-a754-7758b6809c0d | -15.0407 | -45.650002 | 2025-08-29 00:31:00 | METOP-C | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 74b289d3-3319-3d9b-b037-49be2ec7f7bd | -7.6352 | -46.546101 | 2025-08-29 00:31:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e05ce8c-4118-30fd-91ed-9b8daf98a261 | -5.1246 | -43.2173 | 2025-08-29 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa55fbe-96eb-3988-b1aa-9eae8a600eae | -8.2117 | -49.559101 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e88ab45d-e48b-3e0a-b967-6ecc75e06d49 | -5.5973 | -45.521702 | 2025-08-29 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68949c0b-92d7-3c15-b219-580ac7bf929d | -7.6243 | -42.696899 | 2025-08-29 00:31:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c59a89f9-0d05-32c1-a441-27cc75226073 | -3.4304 | -49.039398 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cec38f5-f038-3d3f-a756-4d7a2735ea73 | -6.8379 | -42.8209 | 2025-08-29 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd1ce7aa-5210-3e34-bee5-726c18abd85b | -10.9858 | -46.894299 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3ab0ae-4a53-3ad2-bc01-b3218a06931c | -7.5506 | -47.4977 | 2025-08-29 00:31:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53fdff67-6f16-3153-b3ee-bd953d53358a | -10.9563 | -46.853401 | 2025-08-29 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 684ff18d-02f7-3c7b-b188-22979d66af8a | -11.1017 | -44.741001 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 335920a7-bfd1-3288-82b0-e30cb43802a1 | -13.5488 | -46.873001 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd0d36d-1fca-3454-8182-7e0ee6b7c501 | -13.1906 | -45.2803 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1a3b887-db1d-3285-a42b-082934fe447b | -7.0482 | -44.386002 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac9bfebc-f7c5-3c12-94f2-4bb8ba6400c3 | -8.2137 | -49.568401 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 495dedad-1a8a-3524-9bed-a4476cda77a5 | -13.5356 | -46.859299 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6861d17a-2492-34f9-b101-674fd446157a | -9.4884 | -45.400002 | 2025-08-29 00:31:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97c7c647-389c-3bf8-8d02-391e70c29029 | -13.539 | -46.875198 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68fe7c4d-5f2c-3fc1-9349-3d3413a8c0e4 | -6.7375 | -43.5821 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78da09d9-68b5-3a85-9540-9af5e2bd0cca | -8.1758 | -61.3755 | 2025-08-29 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 22bbe739-ffdd-3de8-a867-bdf2514d3e5b | -6.7074 | -49.4561 | 2025-08-29 00:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| fdc4d41a-5573-3d13-b259-38cacb0d3cc2 | -5.6081 | -45.0038 | 2025-08-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 191.8 |
| e784d404-f422-3a90-b315-64623e5e072f | -9.4263 | -47.6384 | 2025-08-29 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 55192440-f973-3949-8441-cfe9d9aec80f | -9.426 | -47.6605 | 2025-08-29 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7e6bb8d2-fb1a-37dd-b29c-864ea1ebb7ee | -12.0976 | -44.717 | 2025-08-29 00:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1600be75-2a01-3af2-95a4-8b16579ae606 | -10.3624 | -57.8258 | 2025-08-29 00:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6eb3732a-c1c9-37a3-b802-6553400a40c9 | -10.3812 | -57.8245 | 2025-08-29 00:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 513635b0-daf2-3d94-af69-b4d1b719adfb | -17.3435 | -42.6581 | 2025-08-29 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c0f30bfe-afd7-3638-9211-de52d72eba0a | -9.4618 | -60.5682 | 2025-08-29 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 5b4bba06-a9f4-37c0-b97f-71e3a1f49142 | -5.6266 | -45.0252 | 2025-08-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 459359b3-23e0-3b5d-ad1e-5b2192ab9a25 | -13.558 | -46.8745 | 2025-08-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 14878970-45f0-33b1-a00f-0e5b9eb2ad0b | -3.7693 | -54.8286 | 2025-08-29 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5ca65815-f9d1-3743-b2a6-f2d042a78fe2 | -22.6756 | -46.8439 | 2025-08-29 00:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.1 |
| 38218fb8-78c4-3e26-9f0d-93e7cbf26c2c | -5.6079 | -45.0265 | 2025-08-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| f073b023-b734-39d3-a8e3-7937dfb25abf | -24.1861 | -49.5515 | 2025-08-29 00:40:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 102.3 |
| a4c9b504-948e-3de6-ad68-cacb54c82786 | -14.2555 | -58.5084 | 2025-08-29 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 09ed1643-565c-3998-bb20-ae12996a9b22 | -14.2747 | -58.5066 | 2025-08-29 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1244c413-ff6c-3485-9fbb-905b2cd94cd2 | -14.2558 | -58.4884 | 2025-08-29 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d9c8c516-b1d7-3975-b3f6-f1096d88f5fe | -9.2178 | -60.8689 | 2025-08-29 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d9a5f9e6-7ca1-34a4-b37f-8f148b09c215 | -13.5391 | -46.8548 | 2025-08-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f014bd63-5703-39b9-8670-576308f7e843 | -3.4254 | -49.0517 | 2025-08-29 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 86d865d2-f932-38c9-99bd-9927935ecdb0 | -13.5386 | -46.8775 | 2025-08-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| cf0ed9f1-de8e-3672-b804-d63e83d19ac6 | -8.176 | -61.3564 | 2025-08-29 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d9770eb7-ec66-3ae2-9440-5c5883a84748 | -5.6268 | -45.0025 | 2025-08-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 203.4 |
| b5a35d98-9a82-3a18-9e15-1ab1d0a9c0e7 | -6.5546 | -43.9221 | 2025-08-29 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 9a379e73-c96c-339d-b78d-8f8d4356c7b9 | -9.5424 | -65.7002 | 2025-08-29 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5c2d17bb-69be-3d47-b80b-669fc7efb49a | -12.0784 | -44.7199 | 2025-08-29 00:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 045196d9-7bd8-3140-8e8b-6d71bb527aa7 | -12.4345 | -63.9173 | 2025-08-29 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 116b2c3a-3d9a-340d-8703-1bf54b2770a8 | -6.5358 | -43.9237 | 2025-08-29 00:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 6949fae7-95e9-3cc1-9aab-bdb87c07b09a | -9.4432 | -60.5692 | 2025-08-29 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 83f41388-7cb5-3671-8d84-4cf4d87d1f85 | -13.2031 | -45.2834 | 2025-08-29 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 19878987-97c4-30c3-8eeb-4aa3da8b40b1 | -13.0342 | -56.9166 | 2025-08-29 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 539bb9d3-953e-31e9-a9e6-454671126370 | -12.9961 | -56.9201 | 2025-08-29 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7aabd6e8-f9e1-3930-8f18-1d104dfc5fd5 | -13.1837 | -45.2865 | 2025-08-29 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 303.4 |
| 2307dd47-7b4d-3ed6-aa0d-3799c51e21cb | -13.1842 | -45.2633 | 2025-08-29 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 61ce0e20-77ee-373e-85ef-2565e7d07b61 | -13.1833 | -45.3098 | 2025-08-29 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 66ee2b93-9409-3433-bb15-3416b3d4af89 | -9.462 | -60.549 | 2025-08-29 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 56e8b4a2-70b5-34ef-9a72-9c64f0dad853 | -11.5726 | -46.2617 | 2025-08-29 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 1c6d827c-6b3f-3443-a53b-8298af57e245 | -7.0569 | -44.3623 | 2025-08-29 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e95c0913-cc36-3132-b1f7-226e7227414f | -8.1944 | -61.3747 | 2025-08-29 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| fd49073e-d466-323c-b6e1-4262875807a1 | -13.2036 | -45.2601 | 2025-08-29 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b153bca9-436b-3b0e-9a7b-85131d36d5af | -13.5584 | -46.8517 | 2025-08-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a8603533-ba42-3b29-8d3e-54645d2c7ec0 | -8.2867 | -61.409 | 2025-08-29 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d4f1ed39-7045-3af9-a7f9-3e89d32231b1 | -10.381 | -57.8443 | 2025-08-29 00:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a20ffc31-a4ef-3ce0-8368-b41f9240a9f2 | -9.4452 | -47.6364 | 2025-08-29 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 742777ad-baff-3f3b-b15c-c5362fce27f9 | -17.3442 | -42.6333 | 2025-08-29 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 7b64c516-c2b5-3b06-9b1e-ddc54ee7fec9 | -13.0151 | -56.9184 | 2025-08-29 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 79d19a4b-ff5a-3628-af13-e351503dce8b | -17.3643 | -42.6284 | 2025-08-29 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2cfddbba-10ee-3a46-931f-454dccae1f4e | -24.1853 | -49.5751 | 2025-08-29 00:40:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 361d877b-1c5b-3d5b-8f75-41b38648d2e6 | -10.4551 | -57.9378 | 2025-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5b193973-1282-3bf8-9304-e86fb0876690 | -28.69839 | -55.58273 | 2025-08-29 00:45:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 19.9 |
| a5a62c57-a0e2-3c25-bb4b-4fca8f58ddd9 | -24.17923 | -49.5615 | 2025-08-29 00:48:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 24.8 |


[Clique aqui para ver as próximas entradas](README9.md)
