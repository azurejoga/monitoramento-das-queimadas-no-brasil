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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a158e215-0c68-36d7-9d8d-5a2439a8e663 | -11.47064 | -43.58892 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17df93c-a309-3a0a-b7a6-03fefbfcf18e | -13.19027 | -47.29167 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d836d53-f661-35c2-9df0-729fbd1904de | -12.16986 | -44.0971 | 2025-09-15 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57de93da-d02a-3777-b8f1-678c5352eb4c | -9.55212 | -45.93987 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d358f5b-7df1-35a4-b349-022918acdcbb | -13.92429 | -44.81105 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f4ebe88f-42ee-3776-8c05-6676987ddbfb | -10.75868 | -50.63705 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3f7ea22b-70a6-349a-b5f7-74d7c7ffb7e0 | -12.44757 | -44.74404 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56f7f910-ac04-3dc4-be6e-230321dbcbcc | -14.21975 | -46.17886 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f6564ef-1893-3486-8981-e5e2f10d1bcc | -13.9333 | -44.79718 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76325be0-41b9-377a-b5a5-0f06a4db71fe | -13.05579 | -50.0785 | 2025-09-15 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8536b5d7-cd71-340f-8ca5-b920b9b04a3b | -9.1236 | -46.94217 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fca11d3-8efd-309f-9d4d-c0f7e124a39e | -11.8598 | -50.52575 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 066c2f00-4a17-3ab0-ab6f-900e9e9aa187 | -12.12456 | -47.57092 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df7985d9-5c77-3f14-878b-bf57c703bd13 | -10.89474 | -45.44868 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9704f8d6-f589-391c-8ed6-e13ab5b1fa7b | -14.83326 | -51.6357 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c89ce5f-0723-3414-959e-9d8bdf34fa17 | -13.89016 | -48.30563 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32222e4d-844a-3d87-97d4-4e48b47d379f | -13.89233 | -48.31359 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12776d31-02b9-35f0-96b0-e8a91c664dcc | -10.74753 | -44.70234 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8688938-083f-3e77-8d13-4766b28604e0 | -13.21398 | -44.07446 | 2025-09-15 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c268c0-8eae-3d26-84fa-b44afb309af5 | -13.65614 | -46.9968 | 2025-09-15 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f90ed2cb-ce32-34cd-aa15-947973befbc4 | -14.94523 | -46.56639 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5941386-e159-3fa3-b267-8a82e98ef34d | -11.07939 | -49.72505 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f0a1a12-ed2c-3057-8ff9-929aee4b4918 | -11.3141 | -51.1381 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f28f3218-20b0-3334-ba00-573de698ffce | -10.16613 | -46.14645 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a64a9ca-cad2-37c3-8408-f860ee1ae9dd | -14.93036 | -46.57486 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6dbc871-8fa7-3956-9004-684495e96d4d | -10.75591 | -44.71463 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f78641e3-632c-3d16-86ed-7ec46611e354 | -15.10702 | -52.48629 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e76e42e9-1f8a-3fda-b463-da3fdca59b29 | -15.6661 | -52.24324 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9399aa8d-c68b-37e1-8064-09c54a64619f | -10.93945 | -45.50946 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa00c79c-82de-3416-87b4-a72987505311 | -11.86533 | -50.52949 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b7854d1a-d2da-3885-ac85-bf30d5b9811f | -16.39289 | -44.0452 | 2025-09-15 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0884dd0-645e-3364-81e8-b3077e7153fa | -14.45884 | -55.96275 | 2025-09-15 04:21:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc1f8a91-c7ea-3ed9-ae9c-82872b40a0d4 | -12.44365 | -44.74717 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6df9ab59-905a-3a1c-acfc-03ac4a4a505b | -10.15952 | -46.1454 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52da2fa-6845-3ac1-8495-3cad93e58cf6 | -12.04461 | -46.53486 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e716df26-cc71-39ab-abd4-f0adcbae57fa | -12.60309 | -45.72583 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32241770-c3be-32af-875a-25cec898a94f | -14.51194 | -47.35071 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba655fe3-f777-3686-ba79-c26a5c6fe192 | -10.75664 | -50.64407 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 30e6f6e6-3e69-305d-8451-96f20eea4f50 | -11.49911 | -43.70806 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab153616-9949-3288-a154-15271bb37f48 | -11.3357 | -43.51365 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56a6104e-de86-368a-835c-7703319aa1a4 | -10.76059 | -50.64476 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6683df7d-cac0-30d7-bd6f-f3c65873607b | -11.32786 | -50.86647 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c1989d0-3daa-39e6-a5eb-65419e62281b | -13.1881 | -47.28392 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 702fd743-45ba-3240-b900-f3f6e5a9b611 | -11.35661 | -43.49283 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 232221c5-d368-38c6-8908-2bf8055f2ceb | -12.00468 | -46.65848 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9b0db6b-5099-35d3-9b4b-b9a3e0b5aeb2 | -12.04791 | -46.5354 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cc5a836-2457-3637-96ff-2895e98bf397 | -9.13865 | -46.95599 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2329f1ae-e21e-3be1-b4f0-8a53088b2ff9 | -12.95264 | -48.2534 | 2025-09-15 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81909e58-9c05-3c09-a509-2d42faabc9aa | -10.73392 | -44.76945 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f59a28e-fbd8-3c18-be3a-91dde5167049 | -15.76809 | -52.21362 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34dc2f38-94eb-37e4-a951-c61e073095be | -12.43485 | -46.88558 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76096601-c21a-3bb8-8612-9273d052514a | -10.93782 | -45.51995 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f50c42e7-322e-3981-8d14-55e5b6157fb1 | -10.78173 | -45.97782 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8622e1b9-b882-330b-ad5c-aef48300a823 | -11.8546 | -50.52254 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6b20d137-fe33-388f-bbf3-e803384dafd8 | -13.21686 | -44.07888 | 2025-09-15 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de978e39-c63a-3e7a-ab8c-3233f2fe17c7 | -10.8623 | -45.46147 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b684ad7d-6704-3ac5-8857-76493ed21e6b | -10.76204 | -44.71925 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28267e6-27a2-3c55-988e-b1fd4e8981f0 | -11.08092 | -49.716 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a99f2710-a18a-3f90-ba21-24cddc7a0c0c | -15.80374 | -52.20002 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f5a7bb9-fa2f-383e-8efe-45b876859547 | -10.43075 | -44.84171 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6753866f-ecc3-332e-8325-e5faa483539f | -13.87928 | -48.13137 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54de7601-ca54-35dd-985a-10f4958e15a5 | -11.43439 | -43.53192 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e3015e3-f521-3938-9451-e6360463d366 | -17.34227 | -42.64133 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 329f3ad4-3ef6-3c3a-a2a6-e606217afa68 | -11.8705 | -50.53268 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e5a88e5e-aa32-3150-be3c-bb28b37ecc01 | -10.63857 | -44.21208 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c573d6af-3f8d-39c9-b80a-8f4c083a484e | -12.60363 | -45.7223 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e10fff78-6398-3979-9768-0721d47f095e | -10.93999 | -45.50597 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23febe55-7def-3caa-adbc-a8e55aff08ea | -11.99862 | -46.65387 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbac80f7-3a4d-3d5c-ad9c-81a1b7a1ef4d | -12.01186 | -46.65602 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4af4f1d6-1f0a-3ba1-9cac-b1f5dd6f6a22 | -14.94578 | -46.56286 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22793e71-ca70-3614-bb5f-ff01a5f8fdaa | -10.74684 | -50.63498 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 989441e0-cf0c-3928-bdc5-0c6e95217b56 | -10.63913 | -44.20841 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f3d2d43-43fc-3b8b-83e6-c46725e6636e | -14.20333 | -48.77264 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9676940-a06d-38f4-92ad-7853bc2598c5 | -14.49203 | -47.34752 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52ce57a0-38bd-3a81-9bd3-c4ad0d7524eb | -10.6699 | -48.67841 | 2025-09-15 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a1cd72f-cfb2-3e64-9abc-90c14860a4da | -10.75697 | -50.66537 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aafd4dc-00fe-33ef-9ea8-b1df712d1697 | -11.07786 | -49.73412 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2814584-1da4-320e-89b1-8b38863bf014 | -10.40145 | -48.61118 | 2025-09-15 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59a939da-64f0-3880-9157-c6ebebaa5f83 | -10.90708 | -45.56522 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1205396b-87d3-33b5-b67d-31d8ec75a06d | -10.73051 | -44.77268 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff0ad599-2202-34b5-acb6-ccf427376270 | -16.2922 | -45.68766 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee73d883-d546-3933-810e-48b2a25ab9a1 | -14.28197 | -46.12712 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a849495-7deb-3259-89ac-4a1412d81cb4 | -10.19144 | -46.16114 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69c50807-bb57-3bb6-bc7d-52b54ba0484a | -13.9521 | -44.90313 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c7699b8-ba96-3d37-804c-f936da99d184 | -9.72121 | -47.33219 | 2025-09-15 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0b1c5a-d451-3a5a-8305-3d543d3823b1 | -12.11397 | -44.83755 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d5b1337-8db1-3c92-b2b3-17020169791b | -10.63464 | -44.21525 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 211e05d1-d814-394a-85de-6e8be8075566 | -10.67127 | -46.24593 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b98f3d17-d3ea-3ba3-92d2-4b2750404fb3 | -12.1273 | -44.81757 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abbeca42-04c8-38cb-8ae5-326eb8477965 | -15.89692 | -49.98858 | 2025-09-15 04:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 811ff154-8af0-3c3b-8205-3cd415a94547 | -15.78417 | -52.21661 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 484f8df0-fcb3-3ce3-9789-c1577345f49a | -15.8044 | -52.19631 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710d09e5-4ca6-3b28-99d9-84d29c0dac79 | -14.42893 | -53.37143 | 2025-09-15 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f783bbc3-64e0-3126-860b-50f54cf0ab19 | -14.40674 | -46.39851 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c4a5fd6-80db-3566-8346-2a80036c7384 | -10.73725 | -44.77 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a72691db-d2e6-3683-8e87-456142bef4a9 | -11.07272 | -49.71923 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac0a995f-22f4-35f2-987f-e725104e5b32 | -12.07688 | -47.5668 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84efa19a-34e7-3560-89f7-e29322c6e516 | -10.89198 | -45.44467 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8f9398c-eea6-3a7b-ac4f-122b7e1d063f | -13.95488 | -44.88466 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daa2cdbf-37e4-3632-86a2-4d4556b73082 | -11.27751 | -50.85038 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
