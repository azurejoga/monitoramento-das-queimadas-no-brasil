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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b147ed71-8a71-36cd-a97b-cc6192bb9a4d | -5.87378 | -43.87375 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b882f95-53a0-3838-88ee-bc4c334842e9 | -7.47142 | -41.51919 | 2025-10-16 04:38:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b2b921c-6d1e-33c7-8058-d718b62ebb49 | -3.27138 | -45.84377 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b249a50-1441-340e-be14-524a97d56bd2 | -6.24822 | -44.01423 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb2aa191-eaa5-3d09-8e14-e957880c2176 | -5.87649 | -42.81118 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 821c68b8-aa71-33ff-9324-f94cf969703d | -7.0981 | -45.27789 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aba7da87-c19d-3c93-ba55-f74c9ab3d9c5 | -4.01779 | -44.17952 | 2025-10-16 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 784ea5f1-ab02-3bb8-821c-cb6343736aa3 | -6.83088 | -44.64329 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdcc69d1-c561-3986-a826-a1db13a57ff1 | -7.48475 | -42.13444 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3be0023e-93c0-3634-945a-e04847f79b19 | -4.3884 | -43.38403 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 526b355d-2724-3fb7-b807-78706da2a204 | -6.53482 | -44.69429 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc1e6445-7b79-3c1c-938c-7ee8c31b63d7 | -6.44293 | -43.38181 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bd7535e-ed3f-3216-9acc-de54f0270ab4 | -3.28845 | -50.15104 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11cacbb8-a233-3ce5-aac2-9ec579ac0060 | -4.28572 | -43.05468 | 2025-10-16 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 561207c2-8aa7-37d2-9b44-a37e20b6de34 | -5.91268 | -42.84282 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd3fcc5b-9599-3614-a40e-96ca32b1be72 | -7.35555 | -43.86169 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4f466fe7-4d02-3ca2-8078-e2c768a27382 | -6.18258 | -42.59826 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 89683cb2-5242-31c0-a0a2-dfd274d20e0b | -6.1325 | -41.76236 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dc90bcf4-fa85-3ae3-aaf1-224618ec3c5e | -8.29591 | -43.41172 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b0d8c0b8-b87a-3102-a2d1-a130c172a0cf | -4.88062 | -43.33116 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea9a35c7-8590-3d15-80bd-39e93b6781fd | -6.53191 | -44.73798 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8c67b96-c999-30b6-a1b1-b17c495f8bf8 | -4.91397 | -41.5527 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4e2beba-15da-329f-b3d7-4c48771cc520 | -6.06213 | -44.52255 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79b319eb-9c0e-36d6-8618-7581dc513609 | -5.71331 | -51.12556 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6dd0187-db7c-30eb-8c5f-d752d0acf0f3 | -5.4451 | -44.27044 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd982506-3750-3e28-8c6b-7004d056488f | -3.23283 | -43.45558 | 2025-10-16 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 47ffd6b3-6a96-39b2-84af-fead1c1ad6b8 | -7.4669 | -41.51509 | 2025-10-16 04:38:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5731bc1f-dc6a-373b-add9-b7589ea343e3 | -4.94094 | -41.71041 | 2025-10-16 04:38:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 965a5568-6814-3415-8191-919a63974234 | -1.88903 | -48.39804 | 2025-10-16 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9b5855c-2e72-3aeb-8155-875f97fb19ed | -6.22384 | -44.15393 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fac2aaa-3a8b-3408-9f14-51570e33323d | -3.81718 | -54.07222 | 2025-10-16 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847696f1-c35d-3728-ad4d-2f5f31e91653 | -6.04236 | -41.91359 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b4bb7f4-3186-3b36-9d14-5328f660b82c | -6.14949 | -41.78051 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cca0dec0-3eb3-3d50-b03c-a727c521ef6e | -1.49101 | -55.4425 | 2025-10-16 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd752373-4b19-3fdc-a4f2-14d30868c9d8 | -2.33903 | -49.60726 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c0a19a-567f-35f4-819b-933cd6562dd1 | -4.0158 | -48.96481 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c222731c-67d6-3ae7-bfc4-ac1d72b522f1 | -4.37006 | -43.3928 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7ab830ab-fc15-346b-bc88-6a28e951beed | -3.84755 | -41.56784 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 14812110-be5f-37e3-b570-05359a63aac2 | -6.18133 | -46.74422 | 2025-10-16 04:38:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 046e69f0-96a4-3124-b719-2ef507d42919 | -6.38217 | -41.47866 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6bf76c37-8784-3d48-87b4-f6ad167b2fe6 | -7.47947 | -42.74896 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8cbdae73-ef21-3210-96b1-84d229646aee | -5.96151 | -42.24601 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd3b9d1c-3f01-3d75-b398-5e591f5da914 | -3.53136 | -50.31032 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7efa06-acb2-3a76-a104-288ad12c8a48 | -6.18607 | -44.30088 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8607ffb8-ec76-36e7-886f-1b4ac296389a | -6.16506 | -40.9066 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 7c87f608-4360-3332-9452-0bdbeb4cf795 | -6.43296 | -41.8887 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3130af46-b082-3fe8-9476-d882a25e8a84 | -7.17008 | -42.51598 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d3242731-0fe2-353c-a370-34bfc4a75af1 | -3.272 | -45.83976 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77e2c006-7acf-3586-b4c2-5b8118f61a68 | -4.382 | -43.39861 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 81508b11-d19c-36d9-bf1e-3b1aacc9b6c3 | -4.10574 | -48.01913 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 9ec27a0a-5d25-3e31-b481-49e58f7717c3 | -4.87064 | -44.57393 | 2025-10-16 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e07ba67e-c93b-3d4a-8691-ed1240caa640 | -5.86665 | -41.23737 | 2025-10-16 04:38:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39dc13b8-563c-37b8-b2f7-1dca467f0fe0 | -4.1566 | -46.79727 | 2025-10-16 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4b0cf20-211c-3626-b595-e9f6d53cbace | -3.4167 | -51.47844 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 060c8755-7d52-3dba-9b6f-674810e28ac8 | -6.04965 | -41.93015 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 86a4f963-3192-3706-a799-fa2ce221cb83 | -5.05123 | -44.46638 | 2025-10-16 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e02a7c6c-94c4-3592-a242-b01bb1c0c566 | -4.6683 | -44.105 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 281fa9a9-36ec-324f-aeb7-633c562439df | -5.73209 | -41.31888 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 054d2c34-8012-3122-87b6-4c192c05a908 | -6.89412 | -43.0569 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 635a0fd2-3982-3617-839b-e4ae2d41e263 | -4.25534 | -48.5669 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdb833e2-ee88-3ddb-8a29-017458f2728b | -5.3403 | -43.73656 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 707275a3-4330-346d-9e6b-3e176e71ec79 | -1.38275 | -49.3033 | 2025-10-16 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 653ef6f3-1edb-3b9b-8087-21af39f23c07 | -3.09184 | -42.49214 | 2025-10-16 04:38:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeb2f288-afbe-315c-9391-25189153c9d1 | -5.8566 | -42.88726 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 400fef23-bd28-3dfe-9150-04ac75f4cd6b | -3.04918 | -47.01807 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97c047d5-a5b0-3fc3-9f4d-b6b6d7b028bb | -7.15275 | -44.37911 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ff521bc-5cee-3102-826f-3d9ebc072ddf | -5.32011 | -44.8384 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 070d51b3-70c0-31ae-8b4c-a13dd3b3d2c0 | -2.70431 | -49.86288 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb4dab2-fc0a-309f-abca-746c92dcbcc9 | -7.74949 | -42.48682 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ad744e0-2103-3cf8-8ffd-4f57e6dc52bb | -6.15956 | -40.90882 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| c337d1bc-44ad-37d9-a9fe-02f528267eb2 | -3.43869 | -50.25183 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc2b4bd-4517-3dc5-a689-ddb184513409 | -7.27298 | -42.94946 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9df3b74-1cc9-3237-9ac5-80be16294fc8 | -4.65209 | -45.33612 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1077347-ccb6-31f4-b102-ecfca429ecfc | -6.71595 | -44.37892 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b4aa52e-a711-3d2b-89a0-fccdd969273a | -3.46474 | -51.06047 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f04ddc80-b20d-3647-94ee-d9798f3d5dc4 | -7.57685 | -42.68775 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54b73940-6ac7-3fb6-af3d-92ae83f39618 | -5.79431 | -35.59867 | 2025-10-16 04:38:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 494e7617-e5a2-3aee-9468-8a1663e7dc40 | -7.09803 | -44.26707 | 2025-10-16 04:38:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70a6eaee-7440-37f7-ba55-5362db576154 | -5.24883 | -45.59953 | 2025-10-16 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a5c17ac-c1e6-36e6-84d8-4e1ea9a6822a | -5.67945 | -45.09982 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 746adaf6-bf1f-3e90-b8d3-dc0a7b79cc6b | -6.18299 | -44.29367 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d7d56f-04fd-329d-8249-ee027e6454c0 | -6.93936 | -44.47329 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e5aa315-d4b8-3753-a59c-329b22c9bc5d | -4.36951 | -43.39659 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ca96bb9e-6601-3d8a-a738-c43f208d33a9 | -4.67784 | -44.09597 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dd7d4bf-d9ff-3f3c-9760-ec7419baae8f | -6.2642 | -45.38782 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37269ecd-7064-3ba7-b6d6-caf091f76f93 | -3.61028 | -41.58313 | 2025-10-16 04:38:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9630f3b-08a6-3802-bc6b-b50b98288875 | -8.24996 | -44.0448 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 342fb1ce-083d-3ed8-8c95-adba09065cdd | -7.40762 | -44.75277 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c662b4-f9f7-30d5-a2e3-0d9fd5e08ef0 | -6.56743 | -42.97733 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 354ca89e-6df9-392e-88ec-d1fb6ab7fe3a | -4.90359 | -50.71737 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae80c39-75e3-36a2-bdee-b53fcfb169c3 | -4.38616 | -43.39926 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 65c04c98-1c03-387c-9700-b552fab91a56 | -5.42568 | -44.2353 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55ac2fec-49bb-3d7a-b309-c3211236938c | -4.8202 | -46.83815 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51c42f1-286f-3a2a-bd88-b99049dcac2e | -4.76299 | -40.86684 | 2025-10-16 04:38:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24dd3596-e757-3994-848f-1af7b14eee7d | -5.68804 | -42.68298 | 2025-10-16 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 903a7c7c-6bb8-3cc8-be51-c46eb82a16d5 | -7.40413 | -44.74871 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b8b18d9-89ed-30ba-943d-53521e796a17 | -3.65987 | -51.75252 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5305c344-d45a-33f4-a61b-c5509d444b61 | -3.08667 | -49.48498 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edf082ee-9de2-3f0e-9972-728d41116f09 | -4.37524 | -43.55935 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8502d1e8-928c-32c2-8712-6d5ded6744a8 | -4.39089 | -43.3961 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |


[Clique aqui para ver as próximas entradas](README57.md)
