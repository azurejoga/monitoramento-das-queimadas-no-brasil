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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4aa485b-5478-318b-804f-6dd4b636f429 | -13.0561 | -56.8489 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9725577-34cb-3355-bc13-d4458d0d3f67 | -7.4048 | -59.995998 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 678deb26-103e-3bf5-b403-f29affe1836f | -9.9253 | -60.477402 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc8d44f6-754d-3885-83bf-0582095ce5df | -22.5481 | -47.613499 | 2025-08-08 01:04:00 | METOP-C | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bfb78215-7bc2-35da-bc72-4d67e7f64443 | -9.0585 | -45.065201 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 028c08e5-f5e0-39df-ba3a-05729361e4ce | -7.0697 | -59.161201 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e889ab1-f1ad-3aef-aa00-3ae43aee8823 | -9.9323 | -60.4618 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95d4f206-378b-3e65-96ef-99e0a1153243 | -12.4951 | -47.499699 | 2025-08-08 01:04:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d63bba4-d453-3403-9034-8007980f5fbe | -11.0171 | -45.060101 | 2025-08-08 01:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1f19848-1e1c-33da-85ae-a9f3ff24d7a7 | -18.6884 | -52.710602 | 2025-08-08 01:04:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 33b6c8a3-7de9-3103-bd0c-c9c7a0409371 | -18.914 | -47.555801 | 2025-08-08 01:04:00 | METOP-C | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 641ac9b4-1d6e-345b-b26c-be94d52be57e | -9.0779 | -45.0602 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a0c0a65-9165-3ca0-a040-0337afe29547 | -7.0773 | -59.148998 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b4f28e2-6a94-385b-bd5d-062b650fe8b9 | -19.2285 | -46.564999 | 2025-08-08 01:04:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1d0707-0717-3702-820c-d4f7f6968858 | -10.835 | -49.376999 | 2025-08-08 01:04:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76e91c85-3b00-3cb7-b7d0-67fcc98ff793 | -18.911699 | -47.546398 | 2025-08-08 01:04:00 | METOP-C | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 77def20d-71e2-3342-b420-bc1756036c13 | -19.231199 | -46.5755 | 2025-08-08 01:04:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 61d73ddb-5240-35f9-9ba2-b4517301397e | -7.8792 | -45.326801 | 2025-08-08 01:04:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b13ab29b-e8a7-34bf-b553-734e343fac6d | -7.0751 | -59.138802 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 587bbc39-5016-304c-9d9f-07024eb10947 | -9.9351 | -60.475399 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6804291-c593-34a0-ac56-7e31f59ca947 | -19.233801 | -46.586102 | 2025-08-08 01:04:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8d7109-7ff3-3858-87a4-cbebcc661c0b | -13.0266 | -44.088699 | 2025-08-08 01:04:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d19629c9-0851-3764-ac98-109f24934cd9 | -23.321301 | -47.334301 | 2025-08-08 01:04:00 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1e841dc-2404-3fdc-b276-e69f22634700 | -7.38 | -44.656799 | 2025-08-08 01:04:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2171a547-a943-3379-9b2f-9ef14404974c | -13.0483 | -56.8601 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af14de3a-dd83-38a4-9493-1558cb4d8cb7 | -7.047 | -59.198002 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64f23077-5ba7-35af-8c9c-99cff4964981 | -5.8828 | -57.7397 | 2025-08-08 01:04:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c77f13e5-3754-373f-887d-b5313f530146 | -8.9187 | -60.728802 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 508181fb-48ce-3daf-b98c-9e3cbd76348d | -9.073 | -45.0816 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 023bbab6-fa90-3976-b8b7-0341df2296b1 | -7.8936 | -45.3433 | 2025-08-08 01:04:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90b4aee3-d5c8-33d3-b87d-4bb5723b2106 | -22.816601 | -46.4133 | 2025-08-08 01:04:00 | METOP-C | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ddeb8b05-e736-3e31-a1b1-dfb06abe31a7 | -21.389601 | -48.6707 | 2025-08-08 01:04:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c6322073-3cb0-3192-bc81-b48031984156 | -9.7144 | -61.274799 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1cdfe51-9cc5-38d0-9214-950e1ea800ad | -8.9285 | -60.726799 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 052faab0-b817-35d5-86db-5f47886df9c8 | -13.0581 | -56.858002 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b7fc000-5a68-3423-89e1-9bf004cf3e0f | -7.0621 | -59.173401 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bff848ff-2982-3f5b-b9a2-b0f60c5d43da | -8.9055 | -60.520802 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96b01d35-b792-34e4-b55f-6078a4fc1d7a | -7.4073 | -60.007599 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8dbfffda-f177-3d14-b732-28ffc095fcc7 | -8.5131 | -43.3144 | 2025-08-08 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 698adc19-f460-3c9d-9a86-15c5a3695630 | -19.2215 | -46.578201 | 2025-08-08 01:04:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fa33cff-c832-3e37-ae48-79cbb572e606 | -5.8196 | -59.211201 | 2025-08-08 01:04:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50c6f818-3203-3c0a-9790-f70bff1ab828 | -9.7078 | -61.292198 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0352d2-f4a5-3e36-9c36-9cc5c055f428 | -13.0502 | -56.869099 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74cb941d-b538-3e54-a148-53423d85a6e2 | -13.8978 | -51.842701 | 2025-08-08 01:04:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a78d796-97c3-3d60-805c-82cda63169d9 | -7.8888 | -45.324299 | 2025-08-08 01:04:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b068e275-f1b6-31ba-b656-ada698c5993f | -11.0217 | -45.077702 | 2025-08-08 01:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8069ab1-7a94-3445-8eae-a0837a8fda98 | -9.9408 | -60.5028 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 711e8039-e165-32fb-a86d-12c4c0dfd883 | -10.0923 | -51.642899 | 2025-08-08 01:04:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c53348a9-fdec-3cc5-9970-ff963f3d5c04 | -7.3745 | -44.635201 | 2025-08-08 01:04:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c3da898-4ba5-34a3-8556-93995b403e40 | -8.8608 | -47.2673 | 2025-08-08 01:04:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f70d30c3-e732-3170-9b65-7631a18b0d33 | -5.9804 | -44.1539 | 2025-08-08 01:04:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d018f14-d6ba-3e2d-83d3-ddffa463f1c0 | -7.0546 | -59.185799 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98a8189e-7bcc-3954-a2e5-9c71e464c5cf | -9.0835 | -45.0499 | 2025-08-08 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 803c77c2-5ef3-36fa-88fb-a12ba4053e3f | -8.5211 | -43.3063 | 2025-08-08 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4d3cd27c-627b-32e4-9f63-5b6676df00df | -5.8083 | -59.2262 | 2025-08-08 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| facd80ff-49c4-3257-900d-e7b27643cdff | -9.0832 | -45.0728 | 2025-08-08 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8bd5dcd4-8f3d-36c2-b5bf-4ff6ea9d3627 | -8.9213 | -60.7489 | 2025-08-08 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 75434b63-78c8-3d28-9b49-45f2c7d9c1da | -9.0646 | -45.052 | 2025-08-08 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 69daac73-f3c4-3e96-9d90-08444d84a25c | -9.0642 | -45.0749 | 2025-08-08 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5c4b74ce-58c9-374b-bfc1-55e2f7054bf3 | -8.9215 | -60.7297 | 2025-08-08 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1b805171-6f36-3399-bc4d-a12f6f43c40d | -7.0615 | -59.1779 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 8eeb44db-b98c-3068-9061-a0b5f292b2a8 | -8.9399 | -60.7481 | 2025-08-08 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 17fe771c-ccc4-3ff2-b7ae-85347d4cf08b | -9.0835 | -45.0499 | 2025-08-08 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6b67c1be-9f3b-3864-9e4b-cd459db32b8a | -8.9215 | -60.7297 | 2025-08-08 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f0578c14-72f4-3d15-83ee-a7caa45e76fe | -8.5211 | -43.3063 | 2025-08-08 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 61fd96d7-e955-34e3-8ae4-deea9163a53d | -7.043 | -59.1787 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| c3e467d3-da69-3010-9be1-87a108862cd2 | -9.0832 | -45.0728 | 2025-08-08 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fe72dce9-a4d9-3b10-8142-2745bfb8e2e6 | -7.0616 | -59.1586 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 870df7e1-dc56-3233-b97f-e35b402bd4e3 | -13.035 | -56.8562 | 2025-08-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 22049ccf-d873-30b7-9092-ade67cf106a0 | -7.0432 | -59.1594 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 28916ceb-1639-3123-af2d-72628f88f6d4 | -7.0429 | -59.198 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c69a51a2-a388-3508-8bb5-a4e05d3c8bc3 | -7.0801 | -59.1578 | 2025-08-08 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c629ca1a-59b2-3ad3-b780-9c6462fe496e | -13.054 | -56.8545 | 2025-08-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6c93bfb8-9e35-322e-90cb-502817fa7cae | -13.0347 | -56.8764 | 2025-08-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 464b54ac-31f9-3bcf-b2a3-3a047826a6a2 | -13.0538 | -56.8746 | 2025-08-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4cc6ef31-cc90-30c5-adb9-c069bf63ec8a | -9.0642 | -45.0749 | 2025-08-08 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 39ffcfb2-9140-3834-b384-f44d80c47547 | -8.9213 | -60.7489 | 2025-08-08 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 899722bb-da8c-35d2-ac0b-4e79318c3b4f | -8.5211 | -43.3063 | 2025-08-08 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d20b5aad-e00e-3d72-9fdb-400debde9969 | -13.0347 | -56.8764 | 2025-08-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 7763b23b-1d35-3900-bfd2-37e54412ad55 | -7.0801 | -59.1578 | 2025-08-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 82d50b23-a8c8-3c25-b751-c5a810bc4f4f | -13.035 | -56.8562 | 2025-08-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 4d2ce0f1-0b72-3c67-8ff6-dbcecadeb5fb | -9.0642 | -45.0749 | 2025-08-08 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 648079ca-51d3-34a8-9a13-ed7114db5004 | -13.0538 | -56.8746 | 2025-08-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e45e0b88-9ef9-3d7c-91a3-a507f63c9fb0 | -7.043 | -59.1787 | 2025-08-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| fd0ccd1a-f361-3c0a-aa0b-b6b160948279 | -7.3731 | -44.6546 | 2025-08-08 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6f05f10a-a270-3f51-ad9f-8acedf5c6ed3 | -8.9213 | -60.7489 | 2025-08-08 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ef69dd2e-47c6-3173-be1d-f29640b291be | -7.0616 | -59.1586 | 2025-08-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d6027f7a-3184-3cb9-ab0f-624999bea927 | -9.0646 | -45.052 | 2025-08-08 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| de002acf-c882-32da-8143-ff6a3e6dbfdf | -13.054 | -56.8545 | 2025-08-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b9476ec3-ffca-3bb7-bae6-2cdcdb4eccac | -7.8918 | -45.3348 | 2025-08-08 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a5d6b5d5-00e7-3a5b-85e2-93a31ecd567d | -7.0615 | -59.1779 | 2025-08-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 983eecb0-3d2d-3824-8072-748bc38ab6ee | -7.0429 | -59.198 | 2025-08-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f3c334b1-e685-3c23-8d1a-ae63a3e29926 | -7.9106 | -45.3329 | 2025-08-08 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3fff3d59-5ccc-33c2-b797-c7543805167c | -8.9399 | -60.7481 | 2025-08-08 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c1f48dc6-6e60-38ed-9573-d628af23262c | -7.0429 | -59.198 | 2025-08-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 5d3a4dbb-a5c2-36bf-a8fb-3e89a70d3f95 | -7.0614 | -59.1972 | 2025-08-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5885217b-05cc-3ac8-b60b-1a5d4e9db42f | -8.9213 | -60.7489 | 2025-08-08 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 4da12219-5d3f-3450-a2cd-0f541963c3bb | -7.0615 | -59.1779 | 2025-08-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f6332e58-60f6-3785-a850-049aced607c3 | -13.0347 | -56.8764 | 2025-08-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4e4283b4-fa9b-3a27-a964-17ed1595c8b6 | -10.6441 | -44.7413 | 2025-08-08 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |


[Clique aqui para ver as próximas entradas](README5.md)
