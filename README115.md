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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 970bce0c-0bfd-3f03-b4ae-3fcddce8b5ec | -9.34291 | -64.71204 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b73ab75f-b0d2-3060-b0a8-823a1c639f1c | -9.10951 | -67.70856 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1f1ea8b-1c34-3d28-9900-a9f23aa53524 | -9.97346 | -68.82237 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81275c4b-dcd4-341d-9da3-f5913cfd8eb5 | -10.452 | -69.30117 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c66c2d0-e8a3-3b8f-b91c-65e2710ff6b3 | -8.8653 | -68.77605 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 465df866-774b-36f7-a3ff-14130a9bef76 | -9.11355 | -67.70927 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ac315a3-51b7-3bf3-8bd3-42a7c89c324a | -9.2345 | -67.87422 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b652af77-2dd3-3a46-a286-f7b89b8bd6d3 | -9.1131 | -67.83099 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4d3f0e4-1213-3f5a-a552-1cbbd3fa91dd | -9.0715 | -67.7351 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60a216a7-81aa-3f5d-9c1f-07c3c453012e | -9.1178 | -67.8281 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 992b263c-3837-3ec1-bcb5-7d15f28974d4 | -8.86168 | -68.77112 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab47df2b-5a97-3006-8eb6-66d69d63677b | 2.75521 | -60.0194 | 2026-10-07 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cb47952-bd31-3802-b78f-9d584a99fa0a | 1.77236 | -55.57113 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bfb11bb-8d59-3bf4-a55f-c04c3488d850 | 1.73341 | -55.60134 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc5c487-d6d4-3ff0-9494-94a7c92df883 | 3.15326 | -60.58995 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e0b090-d977-313a-8798-44b3ae8907ec | 1.53061 | -56.01823 | 2026-10-07 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8684ed5d-00e0-3127-a891-34043255440a | 1.71748 | -55.61855 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d775a2dd-7224-32de-b372-f0f7a74cc955 | 1.63912 | -55.78899 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8ad3cff-09e2-3ffe-8acf-36e404fbb30f | 1.70756 | -55.63414 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5aeda225-4951-3d4c-82e3-89240bfb9bb7 | 1.64061 | -55.79791 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e11c248-fed7-3efe-a0dc-923845de21ed | 1.73419 | -55.60603 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec0a7f2c-71f0-3653-9e17-354a0a69d9e0 | 3.1414 | -60.58982 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 447d4801-8b92-3946-9a04-83b3c8b52f0b | 3.14825 | -60.60515 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d386e233-9579-3b5b-a977-e8b13b1d7dd0 | 3.15393 | -60.59395 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fff65ec-99bf-340a-9915-f31794b972f4 | 3.15461 | -60.59795 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7d7e09d-792b-3d3e-bd83-34442f29f396 | 4.2807 | -60.14883 | 2026-10-07 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d480babf-6f91-33ca-8d01-0526b5a7b2d6 | 1.70222 | -55.64193 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a8a6505-b521-36f5-8f3d-2b3a728e5445 | 1.7167 | -55.61395 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de9c2b41-5744-3f0f-a1e7-10577dfed04b | 3.14567 | -60.58913 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f8459f6-cf82-3f56-9053-62083594acba | 3.08422 | -60.56199 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8d809f6-49e7-3f33-a171-6cfb3f7d716c | 1.52763 | -56.02053 | 2026-10-07 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aa4ce53-5e66-386f-8fd1-6983872655f5 | 1.72281 | -55.61296 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4be85077-daa8-38f5-b8d5-693837dcda5d | 3.15122 | -60.59645 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c2dc74a-133d-3791-8ee5-f4e17c6e525c | 1.70834 | -55.63875 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81047b0b-0dee-3e83-ab83-f2be2b16520e | 3.15102 | -60.60263 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92290364-161c-3aed-a7c3-dd59234006f1 | 1.70224 | -55.63971 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f688f51-5997-3af8-8a9d-e9ead8a8bc36 | 4.28506 | -60.14835 | 2026-10-07 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f05621f-2d65-3213-aa8f-dc3b29eed3ac | 3.15485 | -60.59175 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec3587a-d1aa-3f20-9d45-4cbacba6e505 | 1.76726 | -55.57566 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e127d5a-3989-32ee-8614-0edeb7322eeb | 3.15187 | -60.60046 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51c448b3-e84f-3e7f-939b-fce0ffaaf031 | 3.15169 | -60.60662 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3766c5e-46a9-3318-b421-cae88abf52b4 | 1.71289 | -55.62859 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78ecef6c-c988-312b-bed3-ac5b035741db | 1.52837 | -56.02493 | 2026-10-07 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7407f596-8a91-32fb-82af-92b8f23fd686 | 1.52534 | -56.02354 | 2026-10-07 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32e9a2c8-4267-35b0-aad6-7bf62c79be89 | 1.76647 | -55.57103 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5a3c9b4-1e67-365d-95a0-a34bab9f7f60 | 1.76625 | -55.57213 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed68a9b5-9aa5-3e6a-b426-846a98840177 | 1.72357 | -55.61754 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3118f0a0-e823-354e-b2f3-17929afe16b8 | 1.64137 | -55.80241 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a26773d-766d-325f-a75c-d7b74754f521 | 3.15251 | -60.60447 | 2026-10-07 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ceab621-1c42-3b04-a83a-e3bf45a7b773 | 1.77337 | -55.57468 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa4ffee-602a-3029-9a8e-126cc9005972 | 1.70682 | -55.63168 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6760fca4-ab55-3831-b191-023e571e014b | 1.70757 | -55.6363 | 2026-10-07 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9577428-69e3-3ea2-9a89-b278503eabe1 | -1.80345 | -57.11126 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51cc8d26-bf0a-3f0f-9959-eeab7ab43e2c | -3.10066 | -54.18533 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddd69753-0f71-3edd-9ba7-54880d2f5d7a | -1.29658 | -54.55929 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44d6b0e3-7d9d-3eb4-92c0-6cb7c664b726 | -3.51239 | -54.6548 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c5a00c4-ac5d-32eb-85c4-9ab1a383c5e5 | -2.87259 | -54.15278 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99776581-d5e8-3e47-86d8-f5029aaea949 | -3.0809 | -54.29055 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 633d300b-1e3e-3ad2-b9a4-d5531f51ba94 | -3.51047 | -54.66796 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19d61427-8ee1-3414-bb6c-e9e84dc0b585 | -3.99282 | -56.2561 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f8d62e8-37dc-3c1f-8bd2-882581715b7b | -2.77383 | -54.08157 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3906dc74-ff74-33c4-840c-92c71b50e967 | -4.15977 | -55.14111 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8a8514f8-f641-3df5-ae46-d1e230c3b4bd | -3.09376 | -54.28342 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83203675-c746-3c1e-adff-a80bd88cc5aa | -3.38702 | -58.20015 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c04acf9-003f-3402-9f10-3ef07992d883 | -3.00189 | -54.13742 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3f3ed2e-73ff-34a0-aa93-4343e474689b | -2.93438 | -54.17744 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c7132a-e875-3ea0-a8a6-252fe4421c7d | -3.98053 | -56.21908 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d04fa76d-50f9-365a-b043-38ce09afe88b | -3.08101 | -54.24168 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 218a3692-9cdd-3854-8dee-5fff29130461 | -3.07745 | -54.24585 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc0f7666-e91e-32e9-8086-30f097aaa32d | -2.94265 | -54.07178 | 2026-10-07 05:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 972e83f8-0672-3be1-ad9f-5b81222a0d7f | -3.85939 | -55.99621 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c33d7e9-6b11-3f2a-aec8-24891afb31eb | -2.77218 | -54.116 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1744c6f9-1a68-3b1b-b1c0-053788c8243c | -3.56183 | -59.4817 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4fbfe08-14b9-3fe7-9a68-9e9ed8b39fad | -1.79767 | -57.10991 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e5df67b-fcfa-3fd0-b642-6dc2c34f9a3e | -2.84126 | -54.06997 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef89b6ee-39ed-3594-959a-d6add21e9ee1 | -3.55579 | -59.48699 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd27bb3-738f-33e7-8264-20346bd4c02f | -2.78693 | -57.66927 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a6e95d9-9710-394a-bb7f-52cb3a38dd19 | -3.54128 | -54.65199 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12e17f1e-4666-3ae2-aecb-17b216c59839 | -3.9847 | -56.22336 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba5a4648-d505-3b7d-a166-203156adcc08 | 1.03441 | -59.45239 | 2026-10-07 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c970e5a-bebb-3267-b72c-6ab00a064bcd | -3.41107 | -58.91184 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79b7b7a5-b793-3f6a-82a0-9a5d8341a414 | -3.05468 | -54.22368 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa1ce9f1-3b8a-3479-b112-c24fe52aaff6 | -2.77517 | -54.09527 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51990626-f19e-346d-8db3-79e0ac3fd307 | -2.84341 | -54.07712 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae6de42f-276f-3ef2-892f-c040d5a0acc9 | -3.97597 | -56.06142 | 2026-10-07 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e31205-1e6a-3533-99f5-9d5911cae6f1 | -3.5014 | -54.63252 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 285e889b-5dcc-3039-979f-6dfffa7ed2c2 | -4.15799 | -55.15308 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 698857b1-74d9-3b8a-9d15-837221e1265f | -3.55157 | -59.48016 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60078cb6-e2e4-3c13-95d3-2fd985d09c8f | -3.09771 | -54.15518 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38a53771-8743-32d2-a9ae-d657962c89a0 | -2.77318 | -54.10907 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6378f083-d9dd-36f2-8238-39fc090534c0 | -3.6815 | -55.94588 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5450041-c945-3c3b-8271-46f3cd7b7b54 | -3.3918 | -59.51721 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0490f545-19cb-3cc6-b71e-8865e57bb260 | -3.50641 | -54.64705 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e775cfdc-04cc-3723-9c15-9bdb91456f97 | -3.07293 | -54.24721 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4b4f22f-dc73-3794-9f1a-a2a6b834dc83 | -3.79565 | -58.29232 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4e0ac35-9b43-32e6-a159-20090df0a8ff | -3.53428 | -54.65117 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 812efb60-675d-3cf1-a098-8d11688a22e7 | -3.10372 | -54.16405 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81b751da-8212-30ee-a261-31e2a398cd55 | -2.94152 | -54.17822 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef27f91f-1a75-3e9f-b4ea-1021d8d00e88 | -1.8028 | -57.11541 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f8a1cf1-06cb-3f32-8dcd-fe91b3894dfb | -2.93538 | -54.1706 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README116.md)
