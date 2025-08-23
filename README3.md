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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 685516c2-ae43-3633-885a-5b3e72b8cf15 | -11.44945 | -47.34262 | 2025-08-23 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e964a9df-443e-3b19-b4b1-9032ec993e37 | -6.98183 | -44.03084 | 2025-08-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 01209ee6-476c-35e3-b6b6-a08aa7e5b36d | -7.20852 | -45.30478 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1c3c57e6-4a82-38a2-8334-3ab776506bf2 | -6.31677 | -43.74679 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| fd044f23-9806-3a0d-910e-2dea20cdf7d4 | -11.12838 | -44.76007 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7d117bcb-b308-3adc-a21c-de1140d9a77d | -14.47929 | -46.04628 | 2025-08-23 00:09:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a926caa0-0214-350a-bf76-cbbf2f75cc34 | -5.90092 | -37.81836 | 2025-08-23 00:09:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 93abe934-6380-37de-999b-43b10c2b14a6 | -12.99284 | -45.22249 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e677e126-e06c-3bb6-8b83-27574b2c2442 | -7.18309 | -48.42499 | 2025-08-23 00:09:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 534bd45f-ab73-3052-b5fb-80ebafe6b0f8 | -12.31171 | -49.9821 | 2025-08-23 00:09:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 38557cac-c328-3a25-8bd4-515192abdd76 | -16.50322 | -46.7389 | 2025-08-23 00:09:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a255a48f-9671-3bc6-97d7-3c6e261cb19d | -13.18954 | -44.04213 | 2025-08-23 00:09:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b52ac8c8-544a-3c21-aa3d-783357ff91f4 | -6.42643 | -41.22307 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 326.4 |
| a62428b9-a29e-3519-9eaa-e7bcd87b189b | -12.31345 | -49.9886 | 2025-08-23 00:09:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 7b137915-150d-3fdb-b068-2ac79a94478d | -11.32765 | -44.95449 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 26eb00a0-2726-3de6-a22b-bf6c8c19e38f | -11.11853 | -44.76144 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 032f1efb-8d6e-36e6-baef-961dc512f94e | -14.81603 | -47.93951 | 2025-08-23 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 72f4ed5d-5153-3b03-8c3b-b979dba41fb8 | -7.22023 | -45.17253 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fa8de0e4-44bb-32ef-9c10-3dab9c626885 | -13.38906 | -47.51531 | 2025-08-23 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4cad28e0-033e-39b9-a8ee-b3d1d9bd2674 | -6.41467 | -41.20564 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3e3a3d7b-b2a0-3dc7-8f81-d7965aa9e959 | -7.08678 | -44.06123 | 2025-08-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1e32325e-728c-34a1-9f04-dc52ab07c615 | -11.11705 | -44.75023 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d1b219d0-c57f-3c33-9095-7d118c35cb45 | -15.27424 | -49.85996 | 2025-08-23 00:09:00 | TERRA_M-M | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5c5f991f-c09b-3524-9e95-5796be5d8199 | -7.62976 | -45.23889 | 2025-08-23 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 61d4198b-e0f1-3468-a3c1-2af170f04ac0 | -6.77933 | -44.9915 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed1ea6ed-077d-341c-8117-10c51e9aa232 | -6.42509 | -41.21373 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 292.0 |
| 8fa646d8-167e-34d8-b5f9-d4b223e6215b | -14.81841 | -47.96162 | 2025-08-23 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 9f00a724-77a3-3519-8a6f-5427141b12ca | -9.63871 | -44.61439 | 2025-08-23 00:09:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aca17764-3e9a-3328-8b8a-2ba2db240b46 | -7.65119 | -46.27316 | 2025-08-23 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bc0ee817-3273-357b-a435-32a07b213e5e | -6.94229 | -44.28692 | 2025-08-23 00:09:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a59091c1-1bb8-3509-8e48-ac02fb427c96 | -12.94473 | -46.3107 | 2025-08-23 00:09:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2ebce930-58c2-38d7-89b8-121f01ebb3f1 | -13.41827 | -46.25277 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| f5851342-3761-3d5c-8191-7c5b87b40b73 | -7.26463 | -43.67466 | 2025-08-23 00:09:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 56bdc026-ad6c-3a08-a435-ef736b8274e8 | -13.53463 | -51.50169 | 2025-08-23 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 88b036c9-3ea4-3fb4-8156-c6b79c056d3a | -15.96444 | -43.8992 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f04bcaf5-d40b-310f-9fd6-fbd94e9c3784 | -7.30148 | -44.55532 | 2025-08-23 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 463133a6-793b-3f85-ade1-003c63e33985 | -13.5385 | -51.54185 | 2025-08-23 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c75196e8-d03e-35fc-acfc-cc75751ec2f0 | -7.13849 | -44.16965 | 2025-08-23 00:09:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d9e1485e-5c63-3db0-b86d-d1778fe3c8e8 | -12.78165 | -48.71757 | 2025-08-23 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5701a459-b94d-356a-a2f0-4cee3dda7291 | -14.78773 | -45.48204 | 2025-08-23 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| efdc6ae2-757a-3c13-ae19-4a7c56bf64f1 | -7.40474 | -48.1105 | 2025-08-23 00:09:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e39ac28f-08e0-3d57-a66c-33be97292409 | -13.4165 | -46.24704 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 27598644-cb2b-3be6-8968-e503ce1377e1 | -10.65214 | -50.14086 | 2025-08-23 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5561b544-83d1-380a-912b-82677d40d140 | -11.05605 | -44.58852 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e2f51c69-4e02-3291-b533-4a922033aac9 | -14.90381 | -47.99803 | 2025-08-23 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 77c86fc9-ab34-372c-9dd0-347e06d274ad | -15.05423 | -48.47134 | 2025-08-23 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bfc8b05b-0e90-3027-b341-3ea5ad3af046 | -7.60798 | -44.37845 | 2025-08-23 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd3b9f86-7dd7-33d5-8616-6caf3e323800 | -8.54301 | -48.84477 | 2025-08-23 00:09:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fbf62136-b2fc-3537-9c23-c026a6b02878 | -6.61232 | -44.57295 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2803e6bc-a692-3796-a859-a609b32bab0f | -14.79528 | -45.43169 | 2025-08-23 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ac8f2150-db33-33c5-9f62-ad66ec1e1991 | -7.63946 | -45.2375 | 2025-08-23 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7f612202-5a41-39dd-8f1c-2e8f6835639e | -11.44256 | -47.33733 | 2025-08-23 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 18b260e0-dd86-3194-bc12-52cbfb75ddd1 | -7.42747 | -45.41804 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 778915a6-5d03-34f6-8223-be8a0a7824d2 | -11.05748 | -44.59956 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e1ddac44-160c-3e85-bf24-56c36e32b7de | -9.45026 | -47.64032 | 2025-08-23 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d6d4fae7-5c46-31c5-84d5-296c2598ad3d | -6.43202 | -45.5423 | 2025-08-23 00:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ee3d4f36-218a-355c-a1db-cfdb42c922e4 | -7.31077 | -44.55396 | 2025-08-23 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 05a154c6-b29c-34bc-9dcd-b05f3a45eda8 | -12.99447 | -45.23539 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ab73cd7e-8631-3386-824f-56caf6636fd7 | -12.6783 | -43.97201 | 2025-08-23 00:09:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a5453074-c8a3-390f-aaa0-e089ab8d6b93 | -6.31801 | -43.7559 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a8c821d4-6349-316c-b175-ce23d7590e55 | -15.2029 | -48.23044 | 2025-08-23 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 562f8267-f548-3312-89e2-dc30f9928725 | -13.3754 | -47.49252 | 2025-08-23 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8752bbd3-dd33-3211-a530-d56653d8acc8 | -14.6706 | -54.9142 | 2025-08-23 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| dc4f850e-0b1f-316b-8a95-f890288b93ea | -17.5979 | -46.5715 | 2025-08-23 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| a300ce63-66a7-37f0-a743-1d04f30e257a | -9.4452 | -47.6364 | 2025-08-23 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| aa01a790-687d-39d5-81c4-08a174601c55 | -9.1909 | -59.4619 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5b86180a-446b-34de-9eb8-2a9dcce2bb22 | -17.2757 | -46.7538 | 2025-08-23 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 73fd7747-e089-3a0c-a1ba-4ea7dfaee5e2 | -17.5785 | -46.5523 | 2025-08-23 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b949e5c7-1038-3958-8b75-751721667542 | -9.1895 | -59.6364 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 8a9eabd3-cdde-35ff-9df2-9eff8274e0c6 | -5.7431 | -57.5814 | 2025-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 198.3 |
| 5e884817-da3a-3686-8ee9-77f94aebab51 | -8.8921 | -62.4297 | 2025-08-23 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ff91b808-47ca-387f-b58f-c50d6f785b24 | -6.4324 | -41.2357 | 2025-08-23 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 55937ec1-67ce-384b-b51c-601834c9248e | -20.0976 | -47.7442 | 2025-08-23 00:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e4178d1d-c4cd-33a8-8df8-c5533abd5925 | -17.2956 | -46.7497 | 2025-08-23 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 329d6f47-f499-3b87-805d-fbc0cd307527 | -9.2391 | -60.4834 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b0278692-5a5c-34db-a2a1-874b678ae58d | -21.4767 | -47.4159 | 2025-08-23 00:10:00 | GOES-19 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7ca9de5d-b02e-3702-8f69-13d0c88392f3 | -6.433 | -41.1872 | 2025-08-23 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| c02dbcb2-0867-315f-85b9-20ec988b42ad | -17.2751 | -46.777 | 2025-08-23 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| aaddeed7-aa31-3c19-b02a-5fdaa12f2d9d | -7.8131 | -63.5468 | 2025-08-23 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 320a634e-f277-364b-87aa-b336cdfd83ae | -6.5781 | -59.871 | 2025-08-23 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1c1f0f72-de68-351a-bc4c-e0e853aff2a0 | -3.444 | -49.0297 | 2025-08-23 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| fa0ba7a2-fc04-3f69-ba7b-5cba5b495a67 | -3.4439 | -49.051 | 2025-08-23 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f5091d24-5c2e-318b-9537-f95a1908162b | -20.097 | -47.7676 | 2025-08-23 00:10:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 112.5 |
| f730f0f3-ea7f-33fe-99df-322112948798 | -18.9683 | -46.9278 | 2025-08-23 00:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8a685779-1564-3b24-a910-75377a8a8c49 | -14.665 | -56.5952 | 2025-08-23 00:10:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4cc59b05-d554-3aff-99bc-ec456b770376 | -18.9689 | -46.9043 | 2025-08-23 00:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 273586b9-2668-391c-a8fe-109a2f63834f | -6.6044 | -44.5624 | 2025-08-23 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 9d9166c1-ebfa-332e-b713-c2fca804704e | -6.5856 | -44.564 | 2025-08-23 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fb916baa-2589-3378-84f9-675f92e67536 | -9.1897 | -59.6171 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 182.3 |
| b2f89f2c-aa57-3bf1-8905-087a2064c7b6 | -5.7614 | -57.6002 | 2025-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9f3ef9ad-7a9f-34e3-b522-f14ed0b9f880 | -20.0766 | -47.7723 | 2025-08-23 00:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 9b958bbc-d0b5-33c4-9857-1fdfe1f090cc | -29.0083 | -49.4735 | 2025-08-23 00:10:00 | GOES-19 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 122.5 |
| 74f0bc10-d8f3-36d8-8973-781478526339 | -15.1984 | -48.2296 | 2025-08-23 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 96226573-44c6-3bbd-bcbe-2d47176398e5 | -5.7429 | -57.6009 | 2025-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 248.2 |
| 28ffe958-25c9-3caf-8708-06b9ec786183 | -5.0992 | -43.2211 | 2025-08-23 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 23dcda55-55dc-389e-87a3-e7c93eea66a0 | -9.4449 | -47.6585 | 2025-08-23 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9d9a09d5-487b-30c1-9b65-63d744da1812 | -12.9921 | -45.2252 | 2025-08-23 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fb043e29-0030-357e-a4bb-d0c52ca8b91a | -5.7615 | -57.5807 | 2025-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 29668ae7-361a-3e16-bafa-43b2ddae4d69 | -15.0186 | -54.8735 | 2025-08-23 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8334324b-f083-34e9-bcb6-34c234680ff9 | -7.813 | -63.5656 | 2025-08-23 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |


[Clique aqui para ver as próximas entradas](README4.md)
