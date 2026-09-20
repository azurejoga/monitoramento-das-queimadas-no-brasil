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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 527bd939-9b02-3739-b118-b7819f726167 | -8.63647 | -47.62083 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 508e402c-0b63-364d-9dc3-a5df38b5aacf | -10.26764 | -48.11426 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5ab7fc9-f693-34d1-8d7c-8934288196bc | -6.95649 | -43.09513 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d85a3bad-cdc6-3330-88f3-ab5bcabc3832 | -3.99128 | -46.95724 | 2026-09-20 04:19:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0b8e3a0-f597-3396-ae8e-d6f7c3445778 | -7.76632 | -49.19603 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b43efd22-2307-3205-80e2-b15e6c4e2bcb | -7.6386 | -45.82182 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5768f4d1-4cc8-344e-8a94-e6fd71d8f5b4 | -7.1946 | -44.5405 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd75d3a0-4a5a-3369-801b-5671b735c289 | -7.63011 | -46.7582 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08225593-9755-3cce-b9c8-5f63b97c9b3f | -6.91859 | -42.91533 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 001695b3-407a-38c2-952b-65285f680106 | -6.56168 | -45.5812 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a7e4e93-460b-388f-aea6-9125fc34ac46 | -6.30563 | -47.63056 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0ee3fc0-0c13-39ba-b841-d886d2dabb09 | -11.47572 | -47.79099 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c42bb4e6-7615-3bb2-899b-e08de507ad33 | -7.75601 | -49.19933 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3b5fbff-5b87-3ac2-9ad5-6c21de9eb449 | -5.84535 | -53.57194 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ade44fa-16f9-3199-8cc3-19557d3f24f1 | -11.66786 | -43.42556 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac104f83-c4de-3efb-8da4-f5107e0694d4 | -6.68494 | -43.6322 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fa0f3a5-e35a-381f-a6f9-a75b78380249 | -6.98552 | -45.80964 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ed8d87-4eac-36e6-a377-273f2b8c4f3e | -5.83809 | -53.53796 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94ac9b13-d63f-3b48-820f-2fe41e17251c | -10.28642 | -50.21404 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ba0b41e-d4eb-32c9-9424-538829287058 | -10.31288 | -50.22017 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6c30f191-ac78-305a-b7af-df6e6935ec22 | -7.19578 | -44.54345 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfab231d-d521-337e-a2fa-0dbd610f98e7 | -5.85654 | -53.54665 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9272d9e9-3239-3dfc-87cd-701f62e52f86 | -10.54764 | -46.73896 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f33f30-2cda-34e8-b37d-96f0b33ee55f | -9.26638 | -48.20646 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe11b8de-23bf-3370-bd89-219f760ebafc | -4.84039 | -42.83073 | 2026-09-20 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63657067-44ab-3828-8cd0-586e6d6a389c | -5.23056 | -47.5798 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 287e1ea2-74f1-3db6-8219-781287162e20 | -3.45133 | -50.60709 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b40a18ab-9b48-36e3-a7f5-78991c1ed5c7 | -5.85644 | -53.54425 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab0667ed-ed0f-3277-88e2-4191b4d8fd3e | -6.30354 | -41.76252 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 440a209e-e2ab-3c63-906e-fe2a963debc9 | -5.4136 | -44.2785 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1178ab7d-2487-3b2b-9007-7c349fbfac79 | -7.08994 | -44.7292 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04ebc376-3c84-3800-a3ea-da26e359c156 | -6.81491 | -47.88914 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c146eb98-4493-3341-b53f-ea2d668d2e5d | -5.79719 | -43.76724 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 208b14d3-058a-33fb-a9e7-2703fbda7e14 | -8.84978 | -44.91997 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d068a654-973a-3a92-b633-9282801e044d | -11.08783 | -48.29958 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e510405-ff55-3acb-82b8-79b69601c5a4 | -5.85192 | -53.53263 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daffa002-76e4-3d5d-a8f3-e9bfbfbfaa38 | -7.86128 | -44.84887 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4916bff2-f457-3a9b-a005-9ec884fc72d0 | -8.79078 | -48.7089 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 148745be-8aac-3a03-a0c1-6716d59f294f | -7.80517 | -44.94138 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cc1cb45-dadd-3b07-801d-3ae66c2bcb27 | -9.82962 | -46.43863 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abf437e0-7ddc-3813-8f07-f86df957a142 | -9.21298 | -46.22145 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a135eb3-d192-3ce4-af57-9b993598e225 | -5.21808 | -47.57311 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0af137e0-2b8c-336b-aa99-4fd30b744b73 | -8.42262 | -54.72652 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91735d49-7873-3456-8680-823a3425fdf7 | -9.79156 | -45.07306 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f62603-2162-39a3-9718-e6d5da019236 | -9.01771 | -51.42258 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e10a06f-c1b6-3930-ae74-04a04ff3bc95 | -5.5071 | -45.66262 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c235dcc-33db-3fc6-a201-93f12dd0ebe0 | -7.1591 | -47.46103 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c09c6d-9d12-3ba9-a19b-d799fd8938f8 | -4.68179 | -46.39456 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d80722b-110b-32f7-bd8e-4fe9dce29b1a | -5.83998 | -53.52738 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76c152ab-dc9d-35e4-9d7e-c94616dad60b | -10.46218 | -45.09668 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52d8c51f-2fb9-3e50-bfab-adacf217e327 | -5.84191 | -53.51664 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42df9ae7-496f-3d16-91e8-d601338e81c1 | -7.04023 | -45.23275 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c4259a-117c-3d70-9c22-4ede8a63bf72 | -9.79002 | -48.32829 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee3e3a06-3a85-3667-9c07-3bb50795a064 | -10.28054 | -50.24633 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ec099c45-97e4-37e7-9477-e4a787efead7 | -8.75627 | -48.65727 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95b1ed14-9c50-3af2-9e64-e7e169872e7e | -5.40417 | -44.26859 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a56c43d2-c59d-3bea-8ac3-b49ca45fc81a | -7.79708 | -44.92323 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 417b9aae-bae1-378e-b898-0f3ccf7cceed | -7.7825 | -44.82798 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea16d27-cf1c-39e1-929d-baeb796f6a1e | -4.18383 | -49.40809 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b642244-2790-3d53-ba89-9491661c51ed | -8.66999 | -45.33053 | 2026-09-20 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcc1cbda-3b9e-3ac5-bfc0-21f24bf4e6cb | -10.56771 | -46.55472 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fd7a0f7-07eb-33a4-91f3-69b22f635dd3 | -9.7878 | -45.05169 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8c9a808-a0ec-3405-8a73-f86149727b21 | -10.3048 | -50.26319 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f1175a8-61e3-3a4a-a6e3-eb4f0db17f60 | -9.70197 | -54.82201 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fab6d007-b29b-368f-bc40-27c73f2b0341 | -7.3089 | -42.26961 | 2026-09-20 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ac38b507-fb55-372b-84ac-0b3c382555cd | -11.242 | -48.38137 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb82f796-fbbc-3182-85ae-9d55bce8226d | -11.45085 | -45.38427 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ada3a7b-691f-363b-a3e6-e747c4519515 | -9.78513 | -45.06779 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 436376e4-3d6e-3435-b1f0-f2fba7ceec28 | -9.76542 | -46.04346 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e378e454-aa12-377a-9136-01cf0417c473 | -6.19786 | -45.32731 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b81ea22-c793-3d4c-ba29-5ad77f9ebc19 | -6.54167 | -44.1385 | 2026-09-20 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a00648ba-6fbc-3c05-8e93-88a9f7341390 | -8.42156 | -54.73217 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93615c1b-810b-3e09-b315-0acd8b371e3e | -7.56258 | -46.93304 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04e2b31d-be82-3878-aa38-b33f018c8cfe | -7.59767 | -46.97284 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5673288b-ee27-357c-892a-fd0940a3b928 | -6.97212 | -42.58033 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6169d3e7-c8d8-36a8-a8f7-94758fd2ff54 | -7.48826 | -46.71212 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20dadbd8-cd03-36f6-a04b-69957e60a92c | -3.73829 | -51.81557 | 2026-09-20 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 19fe75f2-4d90-308a-84aa-08689da925a9 | -6.30114 | -47.60442 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ebd26c7-ef3d-3103-9e5f-23c6fe61338d | -7.54764 | -45.43516 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae29f9ad-d6e8-3add-9c85-c2c64017db78 | -11.44951 | -45.39231 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc97f28-7bec-39d1-b437-78a77dea86d9 | -9.83016 | -46.39001 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59aa2ca6-0950-3a14-abee-7cf4f83e6fc9 | -5.01802 | -42.85528 | 2026-09-20 04:19:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac34f8c6-5d4f-3b76-bc6c-9dc60a3e5da3 | -7.43576 | -44.75742 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1d9b0008-da01-3451-96ee-4a9ad3e4c2e2 | -11.08654 | -48.30692 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46e9e862-8455-31a0-9524-c866d8138698 | -7.76544 | -49.20107 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5488d797-f9a3-3f84-8144-2976410b7ef2 | -11.00649 | -48.31755 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 360f5374-6bdb-3ed1-9899-475086a3f1fe | -7.42632 | -44.74751 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca67bac8-de24-3f8e-bde7-7c5b0903d823 | -9.72865 | -47.21056 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b604868-1aa8-36eb-93a3-99bd26322857 | -11.66117 | -43.42445 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 580cae89-c5c3-3cad-af2c-4d9aefc4b957 | -5.45138 | -44.31841 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a294048-b7f5-377a-8e63-47cf25c081a3 | -8.38416 | -46.52044 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f8717e1-cc88-35d0-b1d7-73849f8812c8 | -6.3185 | -41.75421 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 074199d4-af87-3124-a6c5-3899c72c64a2 | -11.235 | -48.37185 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c89ff6ee-b392-352a-8668-f57d1fdc41b7 | -5.85008 | -53.54546 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9540b339-d4aa-38e3-af12-0ff976f5d474 | -8.23249 | -45.59782 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee2b55c3-acd7-3647-a8a5-821d69e8b427 | -9.82879 | -46.44345 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b9ba087-1da4-3724-a726-dbe98d881ee8 | -11.4978 | -47.73605 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 489a5022-c5fe-3f11-8320-e3270a077307 | -8.7911 | -60.7935 | 2026-09-20 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a6b177ba-6750-3142-8f69-b756a2f7a552 | -12.47606 | -50.05303 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f644f0f8-8816-3bbe-9080-82ca18d59884 | -14.92857 | -49.91269 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
