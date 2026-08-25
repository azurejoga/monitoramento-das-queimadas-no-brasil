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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df6c1aed-90f3-315b-b194-233243aa5ae9 | -11.1447 | -44.4632 | 2026-08-25 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 55e2f466-f19f-3244-8d51-57c2acb71625 | -11.4306 | -44.5148 | 2026-08-25 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6150964b-e798-3dc3-ad4c-df2d0efc5553 | -7.2901 | -45.3683 | 2026-08-25 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5a9ba308-9838-3ac4-a00b-c3cfb2698a9a | -7.2471 | -45.8685 | 2026-08-25 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 09edfe27-f5eb-354f-a658-da4bbf720c4c | -10.3727 | -45.0537 | 2026-08-25 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 9e827902-982e-3cbe-8344-43fe31c50e41 | -12.7797 | -44.2576 | 2026-08-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 2cb21e60-61cd-331a-996c-8d239c5f61f0 | -10.3723 | -45.0767 | 2026-08-25 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c5cc114c-cf08-34a6-aaf9-6b4e085f2395 | -12.799 | -44.2544 | 2026-08-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8458474d-96ef-3b79-b6e7-fc7a1fde7ff6 | -16.3946 | -49.9191 | 2026-08-25 01:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 53f2e583-4a86-34c6-ba47-748425d04f84 | -6.6226 | -58.4995 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 218.8 |
| bcbd636f-5df6-3447-86bf-28a094a52332 | -7.529 | -61.3635 | 2026-08-25 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2ed660c3-b2ac-3347-9e36-167a0bfec600 | -7.2661 | -45.8443 | 2026-08-25 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6bb27188-c222-349a-a5f4-ac728aa3353b | -6.1286 | -57.8198 | 2026-08-25 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ff55c50f-d871-3667-ad33-c1e8216c52a1 | -7.2713 | -45.37 | 2026-08-25 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 69b061cc-4d38-331d-9e53-f7bd325b45b7 | -11.1443 | -44.4865 | 2026-08-25 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 29b8fe98-0775-3e97-b0eb-9a22285fc29f | -10.3536 | -45.0561 | 2026-08-25 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fcdc9937-5dad-3090-9dc2-ebb9a6f5cffe | -3.5221 | -48.1896 | 2026-08-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2c7c4f45-6f44-3095-90f9-5f95d81a2d8a | -6.641 | -58.4987 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 221.5 |
| 1a8f93f2-74bc-300e-b31b-168a081f9a2a | -7.2474 | -45.846 | 2026-08-25 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 49c444b9-66cd-35bb-9f2a-21e708278543 | -3.5222 | -48.168 | 2026-08-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7781e867-c52b-35f2-8dde-cbd77216c015 | -3.5407 | -48.1673 | 2026-08-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 5f4e4e1f-87ce-35e1-9c74-17d954b33a7a | -7.4286 | -43.1182 | 2026-08-25 01:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 38523c6b-0671-38b5-a7a6-4a4ce41a8a29 | -7.2903 | -45.3456 | 2026-08-25 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6bef9f87-24fe-30e3-9eae-16e2fd5ebfc9 | -6.6227 | -58.4801 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 60fa6649-4297-395d-b6ff-448708a6b429 | -12.7792 | -44.2812 | 2026-08-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 0236bde4-0f12-3a4d-b409-4b15e86ba5af | 2.5983 | -60.697 | 2026-08-25 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 5c564885-8aff-3778-ab19-a544843efe93 | -6.6411 | -58.4793 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7e1405d0-7d68-3421-b297-b147a1a9ec2b | -7.0057 | -59.2575 | 2026-08-25 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 0138c0bd-cca5-3944-8038-f3a35bafe219 | -11.4302 | -44.5382 | 2026-08-25 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 10a0acf5-541b-3934-a172-cfe118254e40 | -6.6225 | -58.5189 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 01fee723-d746-3eee-ad4c-31d889ee6f63 | -7.2858 | -44.0644 | 2026-08-25 01:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 39841c1a-d346-3435-9912-341a224fe5ab | -6.6409 | -58.5181 | 2026-08-25 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| cf476bb0-b76b-3003-9948-7f6ff184f2ce | -6.1464 | -57.9359 | 2026-08-25 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f68bb5f8-776c-37fe-ae57-041dce6f8a75 | -7.0058 | -59.2382 | 2026-08-25 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| f640f512-e889-3e5b-85da-57d738965327 | -7.2659 | -45.8668 | 2026-08-25 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cf66b84c-a287-3e8c-9aba-2010251f6b82 | -3.5406 | -48.1889 | 2026-08-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 9dc05d6c-a751-34bf-825a-26f31c7cc178 | -7.2471 | -45.8685 | 2026-08-25 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 71227803-8329-3431-90f3-e3c2e72c92db | -7.2903 | -45.3456 | 2026-08-25 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1883f28f-7770-3487-bc3c-f204d90b8af4 | -10.3727 | -45.0537 | 2026-08-25 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 244.9 |
| cefe775e-2ff2-345d-ba31-2e7e51c0d817 | -11.1447 | -44.4632 | 2026-08-25 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 2656e71b-fcb8-36c4-935d-6043f067ae4d | -6.1464 | -57.9359 | 2026-08-25 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e1a07c4e-d87c-318a-b8db-4db9d58b73c4 | -12.7986 | -44.278 | 2026-08-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 93c6c31b-b9e1-3c76-89ce-31c6ad71bcf8 | -7.2474 | -45.846 | 2026-08-25 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 16348400-45f2-3940-80ac-aa523e8120c5 | -7.2901 | -45.3683 | 2026-08-25 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 91775784-df20-3550-8c83-f782233dbe35 | -12.7792 | -44.2812 | 2026-08-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 83613e8b-a179-39c8-ac4c-4624133552e6 | 2.58 | -60.6973 | 2026-08-25 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 9ef1046d-6971-3c82-b8f9-7727bc173daf | -7.2713 | -45.37 | 2026-08-25 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 73a60c09-cd21-371b-95af-e7cb35852ea8 | -12.799 | -44.2544 | 2026-08-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b26ced17-84bf-3851-bd88-c75ba0ec8393 | -6.641 | -58.4987 | 2026-08-25 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 19125ca5-d33c-3ffd-b4af-4b034d4ecef6 | -11.4306 | -44.5148 | 2026-08-25 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 0139e4a4-3543-3af2-b0a6-655f0dd14c26 | -7.2661 | -45.8443 | 2026-08-25 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| a7c23d0b-588b-324b-a4cc-7782af87914d | -12.7797 | -44.2576 | 2026-08-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 9e3fbcb2-3c01-327d-a369-82555a055ac6 | -3.5406 | -48.1889 | 2026-08-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 2993566c-a039-3f79-9962-33f8a8df77c7 | -7.2659 | -45.8668 | 2026-08-25 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 815c4f36-1b5c-3d94-935c-faa860a59735 | -7.4286 | -43.1182 | 2026-08-25 01:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 6e093179-5c34-3b17-8cec-1f2134bdc2d6 | -10.3723 | -45.0767 | 2026-08-25 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| f34db86e-16d4-3e72-86fd-88e1e86cd516 | -11.4302 | -44.5382 | 2026-08-25 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 76df6b05-05f7-3778-ab41-3d934f566777 | -3.5222 | -48.168 | 2026-08-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2a7401b3-83d4-31a1-88a6-5f478ccd4033 | -3.5221 | -48.1896 | 2026-08-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f010322a-bce3-3c5c-9d36-93b32b6f9c52 | -11.1443 | -44.4865 | 2026-08-25 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| b56977a8-782c-32a3-a3d6-c67eebf12124 | -7.0058 | -59.2382 | 2026-08-25 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| b1d48e92-b041-3454-aefb-aa270c1a682a | -6.6411 | -58.4793 | 2026-08-25 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| dece3127-4868-33db-8015-3c8b153d168c | -12.7603 | -44.2608 | 2026-08-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b992c1fa-6ce6-312b-8618-08f2106da5d1 | -6.6227 | -58.4801 | 2026-08-25 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2c839dfa-8703-374a-93a5-f7b5edff9da6 | -3.5407 | -48.1673 | 2026-08-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cdaf7003-71cf-3932-a5e5-39174ac757ea | -7.0057 | -59.2575 | 2026-08-25 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| d570af79-08e8-3724-ac22-b4db0f38777c | -6.1286 | -57.8198 | 2026-08-25 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 60a96735-931f-3f74-8cd6-b55498889a6a | 2.5983 | -60.697 | 2026-08-25 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| cf0a8e8e-0717-352b-8713-a45f4449b093 | -7.5475 | -61.3627 | 2026-08-25 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 69330134-4873-3f45-872f-802850a2b962 | -6.6226 | -58.4995 | 2026-08-25 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| f0aaa58b-d574-3668-8d7f-10d6e81174ce | -2.9466 | -40.3578 | 2026-08-25 01:50:00 | GOES-19 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 61f0ac16-580a-33ec-8bac-964c19c57db2 | -11.58 | -46.9594 | 2026-08-25 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 4e6f98d7-0b5e-32aa-8fe2-cba26afa9b68 | -9.4578 | -40.3392 | 2026-08-25 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.9 |
| cd114022-a5ec-3b50-86e8-51e743d53195 | -7.0057 | -59.2575 | 2026-08-25 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 36af0dd7-9d61-3623-8a5a-ddc6835aac53 | -7.2661 | -45.8443 | 2026-08-25 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| ce1af833-307f-3b0a-8561-0af4e87ae444 | -3.5407 | -48.1673 | 2026-08-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ddaa8cec-a0dc-3b80-8034-e21e968acabb | -7.2713 | -45.37 | 2026-08-25 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 90705aac-ef3d-306b-9149-614ea0c22d6b | -6.1286 | -57.8198 | 2026-08-25 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bef2289b-0810-34be-bc15-88f72d833aa5 | -6.6226 | -58.4995 | 2026-08-25 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 1c335f6b-71e6-3aac-9980-b0d1729ab88b | -6.641 | -58.4987 | 2026-08-25 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 99b30177-215d-3e9c-940c-283dfb764ab4 | -6.6411 | -58.4793 | 2026-08-25 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9e876979-0cca-38af-9619-9751a045ae0f | -7.5475 | -61.3627 | 2026-08-25 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f8fa2077-3af1-3182-baee-7457b302c081 | -7.2856 | -44.0875 | 2026-08-25 02:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 5a1cb8d5-09da-33eb-9ba0-be86111caa15 | -12.7797 | -44.2576 | 2026-08-25 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| a45c2fe8-614c-346e-9ede-f9aea972d60d | -6.6227 | -58.4801 | 2026-08-25 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ae5df4a8-2cfa-3c2a-bd4c-04c79f01f2fc | -7.0058 | -59.2382 | 2026-08-25 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| d18deb10-9b51-3f59-9efd-7691b6b16914 | -11.1443 | -44.4865 | 2026-08-25 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 436ced53-310f-3899-a550-9ced875055c9 | -12.799 | -44.2544 | 2026-08-25 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7240b7a5-a50c-33b2-a3f5-a3ce20611322 | -10.3723 | -45.0767 | 2026-08-25 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4787cb15-84d9-377d-b2a6-5b229f1a2ed7 | -11.1256 | -44.4659 | 2026-08-25 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5ad998b7-5b5b-3af2-822b-6e3aea927085 | -10.3727 | -45.0537 | 2026-08-25 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 6f25ce50-b957-38c2-be47-b3254b7a6b41 | -12.7792 | -44.2812 | 2026-08-25 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b95b59e8-b35a-38da-8725-ee73e0c54060 | -7.2901 | -45.3683 | 2026-08-25 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2e663bb4-8d21-3277-93ca-cfe1b97fe783 | -7.2858 | -44.0644 | 2026-08-25 02:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c9071d40-bc12-3022-80f7-eff9ee4d1671 | -10.3536 | -45.0561 | 2026-08-25 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9ef7ac1c-30bb-302d-9b2e-7139d61e036f | -10.3918 | -45.0512 | 2026-08-25 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 07ed4650-6bd9-3d2c-96a2-d6ce0a58e86a | -3.5406 | -48.1889 | 2026-08-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| ad3e2533-ccad-3fe2-b415-23b83a59001b | -11.1252 | -44.4892 | 2026-08-25 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 70f76e66-789e-37c9-bddd-36d211bcbf1e | -3.5221 | -48.1896 | 2026-08-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| dea3b8e9-fb24-3c0d-9bf7-de1914fee4cb | -7.2474 | -45.846 | 2026-08-25 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README14.md)
