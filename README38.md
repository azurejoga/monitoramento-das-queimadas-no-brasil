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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52730b7a-bbdf-3604-b9bd-5263d03ddc21 | -3.86327 | -49.82241 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13abaeae-6f26-35ec-9f92-5100a840d4a3 | -4.24185 | -44.68768 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf0e2291-00a6-353b-81fb-600b40176d49 | -3.46983 | -52.40056 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57e72b6-dc71-346c-aaf0-73076ae932e0 | -4.44384 | -43.22319 | 2025-10-19 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9d8e6ba-fb17-348e-87a4-ec4435aaf43f | -3.861 | -49.8139 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1bb89d7-327e-398f-9ff2-14fa5097577a | -3.77939 | -51.76704 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba0f67a3-d238-3800-8c5b-a417d8e98dd6 | -4.28972 | -45.47826 | 2025-10-19 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71e3aa37-bc76-3e77-addf-0f5b2727db15 | -5.22644 | -42.02162 | 2025-10-19 04:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5d8688c-50a7-3169-966a-04d241274f7b | -1.04433 | -47.7903 | 2025-10-19 04:29:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56297f6-5eb4-3569-91b7-9a916d520985 | -3.82119 | -48.64846 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be97bcb6-3c19-369e-bc87-55c571c59494 | -2.86739 | -50.73277 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e123fa-8413-364d-82a7-673f8671bfdd | -4.58201 | -45.37991 | 2025-10-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7424190b-1d9b-3099-adcb-e5b0a8395b64 | -4.7749 | -46.61076 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b20757af-7b50-3c85-a932-6f03f3c687c7 | -2.47733 | -44.16741 | 2025-10-19 04:29:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b211ab33-7308-3d76-bacf-d27f64de0b3e | -5.1761 | -45.2746 | 2025-10-19 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b60c80-b15e-3bcc-9117-dd7892940743 | -3.70209 | -51.0134 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5469cadd-2db9-3c55-916e-d9f1971bb399 | -2.69718 | -49.54953 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 041566ab-1297-3ae4-9ee6-480977f40543 | -2.44762 | -49.36675 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf14af0e-a384-31a1-8699-43f98a8e8e40 | -4.28068 | -50.54417 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0481a17-3855-3e50-9e28-16cd2ab70539 | -3.29435 | -50.01012 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb959201-4f00-3fda-934d-220df717e152 | -4.23197 | -44.68219 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78ce5b00-b887-3051-968d-790f09c1b87f | -3.82738 | -48.65313 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce7d9c2-df91-374d-ad40-b0951dead1ee | -4.41266 | -49.76102 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2c9fb84-a1a6-3416-85a4-f78a25ab94a6 | -3.71907 | -46.86664 | 2025-10-19 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d022bdab-9371-3ea8-adf3-538bfdaa9a59 | -3.08541 | -49.22234 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6abae3a7-cb12-3a64-99e7-b07a1bfd621c | -5.21239 | -43.74116 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4970d3b-5186-3ca6-9b88-b90f50f81b73 | -4.20941 | -48.35777 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6871554d-3821-3349-a8a7-3083a5042f95 | -4.91627 | -45.41479 | 2025-10-19 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea155d15-20eb-3b47-920a-40965ae5ace2 | -4.52065 | -48.8398 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a1a140-2daf-3165-bb40-6e39d2347ca0 | -2.44348 | -49.37011 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d960440-3e3b-3b7a-9b8f-d8547b12f5ae | -5.13189 | -45.49305 | 2025-10-19 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0bb042-f8a3-3e53-9d37-7ca670d844c5 | -2.86812 | -50.72828 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 980a42a8-9dc2-3c33-967d-4b41ec1a09dd | -1.18986 | -47.66755 | 2025-10-19 04:29:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afbf4675-47fc-3010-969f-2dfd1a0f51e6 | -0.91837 | -47.75601 | 2025-10-19 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae3e31c-5f5e-3275-aeae-9b185a9adfb6 | -3.3299 | -45.62754 | 2025-10-19 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2154757-2815-3b50-81ed-b1b2372255b8 | -5.47696 | -43.02663 | 2025-10-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f68a07c2-291a-3aa0-b48a-c7ac016af24a | -4.6854 | -46.05076 | 2025-10-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88868ec6-ca11-31f0-8564-ab2524badcc2 | -4.29136 | -47.56688 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7dad09bf-2e13-36fa-8121-5607f633c8c8 | -4.14073 | -47.65961 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b24b0822-1fda-3a67-801b-e8d37d17cc21 | -4.15842 | -51.09234 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3feeace0-5597-3773-a7a8-9b60bf6e3517 | -4.83809 | -42.74731 | 2025-10-19 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 68a023b4-df91-36ef-aa71-8ce97493580d | -2.91304 | -52.72718 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3930c092-530c-365c-9c31-c23dbc21b448 | -2.78939 | -49.65286 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 751c5532-7b2d-39b7-bb23-4bd337b9057b | -3.87491 | -50.41397 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a5b56d-5bd5-39e9-b89b-090960907137 | -4.24637 | -48.55696 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1498e9f4-3164-3159-be64-c2def9a15232 | -3.39974 | -54.06501 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23149134-8905-389a-85f1-34350164d4d3 | -5.26809 | -44.81646 | 2025-10-19 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59619cd-e097-39dd-ad79-8c881d10e06b | -4.23425 | -44.69049 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a623a3f0-a510-378a-acfb-a11af11c056f | -2.30157 | -48.56914 | 2025-10-19 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4fe2a15-5c74-3b90-b576-1c1784a175ec | -3.12005 | -49.21906 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 839f1d92-d918-3695-9711-351aa90ff816 | 0.32195 | -50.96771 | 2025-10-19 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f265152-b9e4-3b82-8d87-e1a70f60d84e | -3.48485 | -51.47683 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15719b1f-840a-3f3f-a60c-1c562b012480 | -3.80623 | -51.65355 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 016f1176-a348-38a5-87f7-b9b6620be03f | -2.69075 | -49.54443 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c59395ad-1b3c-3c37-8478-14304c4440cd | -2.65634 | -47.86858 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa2ef3d-107a-37fc-97cf-805765b9dac1 | -2.97963 | -50.2968 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f36c645-f678-3472-8d7a-8cf7b3042739 | -4.95887 | -45.09111 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8bffcd7-ef5c-30a2-9250-b69b20b18934 | -4.60351 | -46.53436 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc9be136-fb8d-3f10-8edd-cf0d9007b301 | -3.79997 | -44.15353 | 2025-10-19 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 813ad1dd-c002-3445-95ff-37ac0887c1f5 | -0.39173 | -51.94934 | 2025-10-19 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351feb3a-77f0-3200-a046-7857bc0ef168 | -2.78812 | -49.66088 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9a01d24-ee74-3347-bdab-79bacbec1a8c | -2.43934 | -49.37346 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c326e77-bd50-3172-be89-93418a423118 | -3.2209 | -53.1398 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 758cd7d1-7bf0-3c3c-a168-fdb8e22f3d41 | -4.82767 | -43.0605 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 390169ba-74cd-3650-810e-214e612fc71e | -4.27204 | -48.88242 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a46aafe-6839-3259-acf2-5b6693c136f8 | -2.86518 | -50.74629 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 641f9bdb-92da-3c72-82d2-1370948b4515 | -2.70338 | -49.87141 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277e961e-0359-3291-ba58-148069255774 | -2.69428 | -49.54499 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4b79343-025a-33e5-80ba-d9bffc7d945a | -5.03259 | -45.1412 | 2025-10-19 04:29:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c21990-5fb9-397a-ac48-9bbf2d3a488c | -3.52249 | -51.66779 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e32fa13-d136-394a-b20f-1679b1f3fdb8 | -4.96557 | -45.91134 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2c539ffe-031a-33bd-adbb-27577b58b094 | -3.21676 | -50.21915 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4054d8b9-a420-37a3-aaaa-992c57b9a4a0 | -2.65029 | -49.52583 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40b4035d-3925-3bea-810c-0366fa5a6b5e | -4.30049 | -48.06592 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8da705f7-a06a-3d16-b01e-8d69301fc03a | -1.66572 | -46.76526 | 2025-10-19 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53da04d1-a28c-3418-94d6-f9b30ecaf135 | -2.86217 | -50.74117 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 752f302b-f61d-3729-b444-9ab492ff9224 | -4.8536 | -44.59523 | 2025-10-19 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a705bc0b-8e16-3bfb-a92f-ed0f411f66ca | -4.24081 | -44.67913 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a61173ff-f62d-3a27-9e94-139820e40b78 | -2.87562 | -50.72948 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5994abfb-424f-38dc-ae94-5f62d1e57cee | -4.28519 | -45.48503 | 2025-10-19 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99620a61-2dc2-3380-9261-36dc36c66ed5 | -4.9095 | -37.41141 | 2025-10-19 04:29:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd314148-5634-39db-8bb1-53d9d6e69739 | -4.30437 | -48.06297 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 026faedd-0ee3-3821-93e1-bc87a469e840 | -4.44006 | -43.22259 | 2025-10-19 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0877af52-178c-3f5a-9ec9-494fa921018e | -4.22279 | -48.35991 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f7e1a6e-996a-3d34-991c-7472f414aee3 | -2.69365 | -49.54897 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 639e9667-2c86-3342-82c4-ecd5c5aa7b9d | -2.86592 | -50.74178 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e1d9cf8-b36d-3176-bbb3-88e56be61cbf | -3.51901 | -49.93945 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52ba4b38-6d33-3f31-afcd-be429f1d9569 | -3.81637 | -52.14354 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 407addfc-d4d5-31db-96ef-17ab982a88ee | -3.51609 | -49.9348 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ff70708-71a1-3c70-ad42-aa9d81aa500f | -2.64676 | -49.52526 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ae8f4d6-f8bd-300d-8259-517f3c4ac287 | -4.14847 | -47.67497 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba738a7b-85d2-3bc4-88cb-eff9575feb31 | -4.42213 | -47.75016 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c678d7dd-9751-3b6c-b3fd-02f1845fbf00 | 1.79119 | -55.72301 | 2025-10-19 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27257cda-ee68-3ccb-94d9-2c3ed0633519 | -2.97895 | -50.30109 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 149e2f97-5b81-309d-a1f8-4dfa0b11e8ce | -3.80313 | -51.64798 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34301752-eb18-37ab-bc2c-eaa563594f34 | -3.83645 | -41.78089 | 2025-10-19 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9886b0ec-0f39-339c-a886-9947bf2a62b9 | -4.23802 | -43.10176 | 2025-10-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea4a2f2a-459c-3434-82c7-4a16614941d0 | -2.70535 | -49.85915 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e33b91c4-aefe-3f8b-9362-f12cff9a8d70 | -2.87187 | -50.72888 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 679275a6-15dd-3a36-9a9a-112c33fbd055 | -4.20717 | -48.35755 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
