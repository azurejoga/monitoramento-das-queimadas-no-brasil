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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fbbb3e4-a7ce-396a-8066-36256579bf8a | -8.1549 | -48.307701 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e66268f4-784a-37db-a785-97eb0154b54e | -4.2958 | -42.9062 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c484ef6e-cfd3-34bf-b898-e6f387771061 | -6.6062 | -52.8377 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a83ea2-b630-318f-9bd8-a85fb347c513 | -5.5272 | -49.3125 | 2025-09-06 00:15:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d57f01a3-bd6c-3632-b184-7bb3046eeefc | -11.0151 | -55.047298 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aaf5bae5-211f-3e81-b5d5-58f869e02959 | -10.7485 | -44.877701 | 2025-09-06 00:15:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aee45f8d-40df-3416-a7c2-534196e6965f | -10.2703 | -53.6497 | 2025-09-06 00:15:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c954bc2f-e8a1-3de9-8c9e-83dac597b22c | -5.7936 | -49.2603 | 2025-09-06 00:15:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d59d097a-eac2-36e3-8ba8-fc25dedf3fc2 | -6.6178 | -52.844002 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adea50e-bab4-373b-9540-84267490e033 | -9.8623 | -48.110901 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5567a696-71c5-3128-9c64-4b49a329fdd3 | -12.5895 | -48.192501 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed454bbf-6fab-39d6-98f2-dd0707b224e1 | -5.9969 | -43.4049 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea2a8a6-26b1-3240-aaeb-cef88395ed81 | -20.341499 | -46.513199 | 2025-09-06 00:15:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b423dd6-438f-3e32-83c6-17d01ac65956 | -9.8325 | -48.161701 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0caf579-ca9b-3463-a799-d676d75f7357 | -14.646 | -48.2323 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4c5db3-3a32-3cce-894d-52a1d848f18c | -9.5792 | -46.954399 | 2025-09-06 00:15:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35cf89ff-dae7-3ddc-9c3f-3ae726c096c1 | -7.8918 | -45.3675 | 2025-09-06 00:15:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9df06a-886a-389e-b97c-54ad11a0b492 | -5.9542 | -43.225201 | 2025-09-06 00:15:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 3f5cce8d-af3d-361a-a540-552dbf1edc97 | -20.159401 | -48.680901 | 2025-09-06 00:15:00 | METOP-B | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 920746a7-0403-3467-8e9c-bdfd4528613c | -7.588 | -52.161098 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255cb8e1-13c4-3598-8885-f13afa6094e4 | -7.611 | -47.546299 | 2025-09-06 00:15:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66d7447d-cd12-3390-83a7-ad10c04b9778 | -6.6276 | -52.8419 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8701ccd4-eecd-392f-9617-2142efb08af5 | -5.6661 | -46.0816 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c02cd8bb-c29f-3144-b383-08a80936985e | -16.1029 | -50.511902 | 2025-09-06 00:15:00 | METOP-B | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9557cfdc-09ba-332a-8f3e-fd7dce64532a | -11.5523 | -47.790699 | 2025-09-06 00:15:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| faf4817b-0370-367f-a494-f74a709fddff | -15.2479 | -47.178699 | 2025-09-06 00:15:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93a2bf14-2562-3d47-94a7-1235eb08164c | -12.8169 | -48.103802 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d093e978-fddf-3a13-a467-5539ca6c4459 | -10.4008 | -44.3675 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 914d58c2-a070-309a-bd93-b45cd9ddc827 | -5.7317 | -43.068401 | 2025-09-06 00:15:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2dea085f-321a-3457-9272-99a90e7d8f67 | -5.3595 | -46.583599 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df0744fe-d2e9-3921-8776-bfc787088024 | -21.1814 | -51.757198 | 2025-09-06 00:15:00 | METOP-B | PAULICÉIA | SÃO PAULO | Brasil | 3536406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae16d76b-4cf4-33d5-a1e4-cddfcbcd27d8 | -4.8637 | -45.419399 | 2025-09-06 00:15:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae99d092-b44a-32cf-a106-674b12804c1c | -5.7654 | -43.643902 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc03151b-ef64-3974-a6e4-b3fa9f7be59f | -8.1564 | -48.314602 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f5bc13d-5fa5-31f9-8042-b24163bed412 | -3.6047 | -50.063099 | 2025-09-06 00:15:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e9afdb-2cc5-3b7e-afcf-8ef95b4b7167 | -12.8172 | -48.759201 | 2025-09-06 00:15:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94ca490c-d2f3-3874-92df-f9364564ad21 | -6.3379 | -49.527901 | 2025-09-06 00:15:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278b318f-4df0-3525-8c67-5e57d5acccf1 | -8.1615 | -52.583099 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a37fee1a-5750-3aa5-9323-96d3c8487191 | -15.6585 | -52.310398 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c239b420-f662-3225-98c0-a1c92d8ff633 | -10.5642 | -47.795799 | 2025-09-06 00:15:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18bf1db4-cb95-3438-a15c-0f2f1634bc9b | -7.1857 | -50.933201 | 2025-09-06 00:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44711a79-aadf-3ed6-a3f3-dc2f9151d6e3 | -8.1732 | -52.5896 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72b359f7-d048-3973-9412-64d2c6235260 | -14.3743 | -48.071701 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af36817d-fca6-356b-94c6-b71750694ddc | -8.1713 | -52.581001 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd227c69-7254-35bc-8807-ad10144e13cd | -8.6642 | -47.282001 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6878ac2-3651-331f-8fd7-742a9606a6e3 | -12.978 | -44.522999 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81d6eda2-d864-3501-b5d7-735a953c181f | -2.3484 | -48.423599 | 2025-09-06 00:15:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1956bb44-fcf1-391a-8a0a-05af5f3418f9 | -9.9591 | -46.2733 | 2025-09-06 00:15:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 749ccddc-42fc-37cc-8197-47999749ab51 | -8.3153 | -51.3507 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeed9768-c236-3a2e-b27b-dc1ad55cbdb9 | -9.4841 | -51.151901 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73cde19b-3a6a-3ea5-9e64-f85a207e34dd | -7.5271 | -50.336899 | 2025-09-06 00:15:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43a765cf-affa-3a86-9c03-85213c68d7d9 | -23.2244 | -47.085602 | 2025-09-06 00:15:00 | METOP-B | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61db967b-0b73-3a97-aed2-ae801013fbd1 | -22.0672 | -47.690899 | 2025-09-06 00:15:00 | METOP-B | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| abe2adfe-6d3b-3e59-8d61-26c344aee9ed | -18.8703 | -41.206699 | 2025-09-06 00:15:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3deffbff-5bcb-38a3-ba3a-9dc96dc2f401 | -14.3671 | -48.132702 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3617b00-ccd9-3b21-936c-a9ea3e3e0f88 | -14.9968 | -52.4156 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86f3038b-bd48-3e85-9f5a-b52de924b9ce | -8.3235 | -51.341 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5915f4cc-1e8e-30ae-8ac8-ff1874a45862 | -5.3576 | -46.575298 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4101e8b4-0532-34e1-a9bc-bf123b67323b | -6.1915 | -46.125198 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6156f7e3-8d30-3914-978f-11468318c9eb | -9.4808 | -51.1366 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0fe7ef-1740-39a4-b80a-d1617add1199 | -6.0066 | -43.402599 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82afe985-a514-3f19-b4a0-21226ca2e0d9 | -3.8109 | -48.967098 | 2025-09-06 00:15:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5afd6aa-7998-38c3-ada6-73fe03c271d9 | -22.546101 | -47.077999 | 2025-09-06 00:15:00 | METOP-B | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06bf9ac0-0918-3381-8c16-077f077f7005 | -9.1989 | -54.7799 | 2025-09-06 00:15:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8aa759e-cf37-3a39-b693-9d7e6b306c8f | -3.5505 | -49.0914 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a44f4bc-0687-37a4-a5ea-635354ef64c2 | -5.7808 | -53.617802 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b87f6b91-4b8a-315f-8b24-62ec34f0e7c4 | -12.2988 | -53.8955 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1e2dca-a1c6-3aed-bfc9-4849778ba3a8 | -11.4303 | -52.251598 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c44c6f9c-dd45-3bcd-b4d2-520bb478c0d8 | -9.5096 | -49.530602 | 2025-09-06 00:15:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6887181-5efe-316a-b004-4e1370b2f9ff | -2.4285 | -46.872799 | 2025-09-06 00:15:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d733b5-8a17-3b5e-84be-424463aa6f2b | 0.3564 | -53.793301 | 2025-09-06 00:15:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe5542b-6c17-34c9-9cb2-02e152e0d30b | -7.1238 | -48.533199 | 2025-09-06 00:15:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f24043b-8074-395f-add0-00a3e832ff87 | -9.4775 | -51.121399 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0674e3c-a9e8-3987-a0ad-74de2d652cde | -9.8689 | -48.0947 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1470b54c-7337-32ce-958a-fbc6c46a8cda | -11.0347 | -50.725899 | 2025-09-06 00:15:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 633a3926-aa10-3cb3-a61c-b3a43172b2e2 | -23.962099 | -49.5518 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| a1742cd9-aeb0-33b5-9e4c-06ee12321e26 | -15.2577 | -47.176399 | 2025-09-06 00:15:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f15100a1-079e-3d0c-9464-3e432001f3bd | -10.022 | -49.755001 | 2025-09-06 00:15:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 850dce7e-a918-35e5-ae77-e463e585a310 | -5.8041 | -46.7243 | 2025-09-06 00:15:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af0f9041-b22d-32c5-ba72-55f1a73a2444 | -10.4106 | -44.365101 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b012569-352f-30d0-8dea-37262361abde | -7.5752 | -51.1143 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efc852f7-f803-385b-8740-b82435a4ef46 | -12.3184 | -53.891499 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2700d4d8-8548-35cf-8b71-cc355ff0aa1e | -13.0044 | -54.8282 | 2025-09-06 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 76efaab1-ef7f-3e0d-8043-35bf89977497 | -9.723 | -49.4806 | 2025-09-06 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a0d32c1a-614f-3189-a2b8-9857ee06abce | -4.5033 | -42.862 | 2025-09-06 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| a3dbac6b-1acd-3b7f-b0c1-c8b7753d782c | -10.6131 | -44.3051 | 2025-09-06 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| a9bd81b2-1f81-3570-ba25-c9058f9a4042 | -24.1456 | -49.4915 | 2025-09-06 00:20:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ca1d6867-2c26-3ecc-8ec0-9016e4cf65f0 | -6.8095 | -52.8154 | 2025-09-06 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0506c06f-8c4d-3ffb-8018-715a1a7fae7f | -24.1449 | -49.5151 | 2025-09-06 00:20:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 120.7 |
| d79ba5df-246e-373c-8972-f70cc9f88b8a | -24.1662 | -49.5097 | 2025-09-06 00:20:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ee0d3149-6068-3592-9639-35bf7b0e58cd | -6.5393 | -49.5101 | 2025-09-06 00:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 12a2e9e3-d0ca-34d5-b98a-7a13342eff4f | -12.9668 | -54.791 | 2025-09-06 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3db3a493-4447-3de4-afb9-60e6dfa4f5aa | -12.5036 | -53.8505 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d4360f51-7f81-3d5e-b99b-b787fa1f42fd | -12.4843 | -53.8732 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| dc4faa3c-ab2b-3e6d-b486-e932cfbf5b82 | -9.7041 | -49.4825 | 2025-09-06 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 0c22ed89-95e6-3645-9789-5e9849f15026 | -9.6877 | -49.2902 | 2025-09-06 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 33748dce-ee0c-3b6f-9716-2b97285ba790 | -12.5033 | -53.8712 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 62b94471-c63d-3dfe-9455-73658d8b1fb9 | -9.7227 | -49.5021 | 2025-09-06 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 5aca8a8c-25c7-37ec-b4c2-2ffa873e5b0d | -15.7381 | -53.5717 | 2025-09-06 00:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5eb42c40-1422-372f-ab16-42e6b49a1422 | -12.4846 | -53.8525 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |


[Clique aqui para ver as próximas entradas](README8.md)
