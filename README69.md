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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7aa1bd2-73bb-3690-b019-7f2c1d83db57 | -8.5918 | -67.1418 | 2026-10-05 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d8b6baa3-4b54-392b-ad11-21f80b7f904e | -9.1334 | -65.9 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 92273849-5fa2-37f0-8268-e46addfddc83 | -9.1445 | -67.7577 | 2026-10-05 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 35eb804c-2868-3cc0-806c-a3e1e17f2bf4 | -13.5008 | -61.1137 | 2026-10-05 15:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 95b540aa-e756-3c14-a381-f44a1f176808 | -8.5554 | -66.9945 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 68059f2b-da3b-353c-827c-0019d0a1ab78 | -9.1149 | -65.9006 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c3e50602-6a51-3102-afb3-4ef8ba8d4a7c | -9.1257 | -67.8322 | 2026-10-05 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 42379d18-7fc0-33a8-96ff-b7417c766b52 | -9.077 | -66.0881 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 86194a93-9811-3cff-8bef-79eae2a95d87 | -9.1429 | -68.2202 | 2026-10-05 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5ac5baf8-e448-3456-b03c-51e8ac445dbf | -9.1333 | -65.9186 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c1155de5-01c0-32ef-b503-a66700d1a801 | -9.1259 | -67.7581 | 2026-10-05 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 630b9187-4827-3998-949d-bbdf5db263a7 | -9.7499 | -65.075 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7671b2c5-1aff-3b3d-a068-0994f808169a | -9.9629 | -67.2162 | 2026-10-05 15:40:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c3b56d0d-9f4d-317f-a128-09c51b1a00c8 | -9.1535 | -65.5634 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 3573309d-0126-3542-bf7a-5051cc91e011 | -8.593 | -66.8081 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6a06befd-0e56-3091-a5d1-2db8693e73bc | -9.0045 | -65.7174 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e1d782b1-c7db-3184-81e2-acc93a9cd6b1 | -8.5929 | -66.8266 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| b586b624-35ac-3c27-958a-7d85031cc674 | -9.0584 | -66.1073 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ef3df41c-dc36-3afd-905e-2a1576e2e7a9 | -9.1407 | -64.4024 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d60ae43f-5d72-35fa-b212-6b9979e2aba6 | -9.8061 | -64.9979 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0a9652ac-f9ed-3e5c-a296-c8126ea977c7 | -9.0232 | -65.6982 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b05aef17-408e-360a-88b3-7ae5cabb8c95 | -9.8246 | -65.016 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 117dae45-4a64-31a3-82ef-d2d6d96b0059 | -13.5007 | -61.1333 | 2026-10-05 15:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 55fc713e-527c-347a-8158-c935332e0b87 | -9.0982 | -65.4904 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 253482e6-dd3a-3eb1-8215-f3f729416eb0 | -9.0046 | -65.6988 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| af13d80b-d6c9-3c32-a7d4-1ed6cb513e7b | -9.7874 | -65.0173 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 2c02cdc8-2087-32bb-b7a5-1b30081e02dd | -9.8059 | -65.0354 | 2026-10-05 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 34d267e2-512f-33e5-afaa-a900e0c40eb1 | -9.0231 | -65.7169 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 561038b0-d4a1-3e3e-b488-8922f674d009 | -9.0981 | -65.5091 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f92bf08f-095c-3360-a837-cfdaf4ec427d | -9.2366 | -67.885 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 19553ac4-0506-33ea-854d-017a9aa0e717 | -7.7127 | -73.1158 | 2026-10-05 15:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 91.1 |
| e1a546cf-d333-37a3-8dd3-d796858dea33 | -9.0584 | -66.1073 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a697f825-93c6-3181-a92c-db347d43ff80 | -9.006 | -65.4 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0ee7f869-c264-3201-bc7b-d82a4941f6e9 | -9.1244 | -68.2021 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 031302f4-b0ba-34b5-a8fd-c21d40e3071d | -8.9196 | -64.1285 | 2026-10-05 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d1676c2b-c10f-3557-ab59-f859f713f59d | -8.5929 | -66.8266 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1fdb8f44-aaae-30ef-b203-1b14b8c018f8 | -9.1905 | -65.5809 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 94fce2e8-478d-3adb-8c06-db08a1581bfc | -9.7499 | -65.075 | 2026-10-05 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8930fc4f-1fc6-3929-bce2-f7e651624cee | -9.1535 | -65.5634 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f1c9fd95-433c-3a16-9745-b1dcf2cd31fa | -9.0769 | -66.1068 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 771d2119-953d-3db4-ae53-737d22574f1f | -8.9195 | -64.1473 | 2026-10-05 15:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f31b7627-d3f8-3bc8-ab7a-f31b046eddfe | -7.364 | -72.6079 | 2026-10-05 15:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 66a5caf4-427b-31f2-955b-d80927fd5e67 | -9.1335 | -65.8813 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fd30f5ff-b2a6-38a7-81ad-4b8dce4cf6b9 | -9.1408 | -64.3836 | 2026-10-05 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 48ecd13e-56b0-369b-bb7c-61f9140be7d9 | -9.1259 | -67.7581 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 375.0 |
| 9c06494a-95c6-3719-81b5-c3b50c8f914b | -9.1445 | -67.7577 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 421f80cd-076b-39d8-bd1b-94e475749693 | -9.1147 | -65.9379 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d95113ae-8775-33ad-9657-de7468137950 | -9.4116 | -65.8912 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8b35cecb-15f6-3d6b-92c4-035d9e76f41f | -13.5008 | -61.1137 | 2026-10-05 15:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 74fc4284-4f9e-3b96-89c4-7173b3883dc9 | -8.593 | -66.8081 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| e8000e5e-aefb-3b71-a4fc-cae8b2d881c2 | -9.0046 | -65.6988 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d7a66d31-79b6-3aa9-b2f5-161af4ae2749 | -9.0981 | -65.5091 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6157e5a8-6b98-34ef-be55-d24ac6f976b7 | -8.5745 | -66.8086 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e6e34505-3e99-390b-810f-292bf399c8cf | -9.0232 | -65.6982 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 258552c7-d342-39b5-9ec2-a455b053ad04 | -9.1261 | -67.7211 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cb2b33a0-a481-34fe-9729-b88f7a41a3e9 | -9.1333 | -65.9186 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| eadcec05-a6f3-328d-8621-9d35f1a58abc | -9.077 | -66.0881 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 42c1c65c-ae9a-3a60-b0ae-362eea693b6e | -8.5733 | -67.1422 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d3098efd-3d7b-3f75-84dd-b808494a6cf3 | -8.5554 | -66.9945 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 884459a4-94c5-3c67-89ee-fbb6edf74482 | -9.0982 | -65.4904 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4bf99ad4-ed7e-3d79-a52a-2ad7e73845ca | -9.0045 | -65.7174 | 2026-10-05 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c3184019-743e-34ef-b58a-50c095397c85 | -9.2365 | -67.9035 | 2026-10-05 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6b3f561b-2fe1-3e9c-a3e9-fb62a1e231da | -9.4565 | -64.3344 | 2026-10-05 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9e332e91-3b07-3cd6-86de-4eb5d434ef47 | -9.7126 | -65.0951 | 2026-10-05 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9085281d-94e1-3434-9d9a-641f5dd57649 | -21.63487 | -41.23077 | 2026-10-05 15:50:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9327d421-85da-37ca-8087-651e11d13035 | -21.66867 | -41.23843 | 2026-10-05 15:50:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0d418926-1a1b-384c-bea7-f9467a18aa13 | -21.63523 | -41.23448 | 2026-10-05 15:50:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9315bcdb-6a1a-3c67-8f52-f90e09936ad3 | -15.73354 | -40.51397 | 2026-10-05 15:52:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 690a3cc0-96ca-30e7-adf4-af9b10e5b039 | -18.30917 | -42.23008 | 2026-10-05 15:52:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| d2ef5aaa-dc60-38f2-b121-72856aff14ab | -15.39802 | -42.99671 | 2026-10-05 15:52:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1445feb1-b3ae-346f-bf11-10f0b743b2dc | -12.80803 | -43.31593 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ce205778-ec3d-3cd9-b180-58dc3477227f | -13.3268 | -39.0699 | 2026-10-05 15:52:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| b774af2d-6bf2-3bcd-b5b9-aec4b55a4487 | -16.58537 | -41.53917 | 2026-10-05 15:52:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a96120e1-dec2-3b19-b4ef-4e108167436d | -12.82466 | -41.83128 | 2026-10-05 15:52:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2372f007-d20c-346f-8a8e-5a74396fca3e | -18.33099 | -41.79435 | 2026-10-05 15:52:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dd48dc42-59db-3579-93a8-ee1f3064ba2e | -14.04949 | -42.49407 | 2026-10-05 15:52:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9c4987db-7588-395d-9208-b5e578ffd603 | -12.62498 | -40.46361 | 2026-10-05 15:52:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 68d2aac9-25c8-3662-bda6-3d14f95fdf40 | -12.03868 | -38.27361 | 2026-10-05 15:52:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0b674743-3d5b-370a-9006-d165a40dfa6a | -12.86289 | -39.92525 | 2026-10-05 15:52:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 4414639c-d286-32c8-8a93-db568fd1342b | -17.08644 | -41.69626 | 2026-10-05 15:52:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 22354f23-d5a8-3144-9495-f3d562a81287 | -16.16497 | -41.2295 | 2026-10-05 15:52:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 2fca1776-547a-3566-9658-34e7b7bd7ba6 | -13.60279 | -42.50381 | 2026-10-05 15:52:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| f0189931-09dd-3ecc-ae92-3a62447d20f9 | -14.00022 | -41.49651 | 2026-10-05 15:52:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21e38f60-a4c1-3221-9153-2879baaeb400 | -15.64581 | -41.18496 | 2026-10-05 15:52:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| a24cae33-08d7-3926-85ae-7ea4a40a7d31 | -14.94294 | -41.34518 | 2026-10-05 15:52:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1cfb33d5-fa50-3868-87b3-f63fb7804f77 | -15.6908 | -39.78383 | 2026-10-05 15:52:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7a91532d-3835-325a-b984-22d92b9bcfc3 | -14.37588 | -41.92142 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a178b957-815c-3a0f-b527-f738b200bbb5 | -18.58902 | -41.27932 | 2026-10-05 15:52:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 09975687-3c55-365b-88b5-c3fab412a640 | -13.3701 | -43.84816 | 2026-10-05 15:52:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 38fad1a8-1575-3993-af27-00a9fee28c6d | -15.14383 | -42.15958 | 2026-10-05 15:52:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| f2b70e1f-64f5-3ca9-8478-cd9eaa9b6886 | -14.28421 | -41.49357 | 2026-10-05 15:52:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b673be11-9d20-34e9-bae6-6a1fbde9bd75 | -12.81788 | -43.30325 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f4a1c387-e59e-3089-997e-bd35f2e86f67 | -12.69936 | -40.53677 | 2026-10-05 15:52:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 4ff6f034-ca24-3525-98c8-995f860a0124 | -13.02176 | -41.04691 | 2026-10-05 15:52:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88644d66-0e27-3645-8a3e-405fdba8f3f6 | -12.1629 | -39.91381 | 2026-10-05 15:52:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| ec741269-f699-34d1-b4f1-ab4a083b3834 | -14.61268 | -41.38878 | 2026-10-05 15:52:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56130cf5-fcf2-3f3e-b483-bdf4a3f510b7 | -18.58938 | -41.28269 | 2026-10-05 15:52:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| f9281a5c-df9c-3dbe-ad9a-e8a47d818091 | -14.55535 | -42.40637 | 2026-10-05 15:52:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ac5a929e-39a2-3fd4-b4b5-8c313be53225 | -15.66791 | -40.89751 | 2026-10-05 15:52:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0cc26005-5873-36db-8c90-5e88eed73359 | -14.8295 | -41.64202 | 2026-10-05 15:52:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README70.md)
