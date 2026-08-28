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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96b2cd5c-3a89-3bea-98db-899995e2ebbb | -1.35638 | -54.63098 | 2026-08-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1456ebb-6047-34e8-8e9e-291fe9b2c40c | -2.72678 | -47.03839 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4668d611-7597-3c55-8ab1-2262d34f4b45 | -2.80536 | -48.62905 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f352707-b372-3296-8f97-35fd7a0c71c6 | -1.59534 | -47.35873 | 2026-08-28 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e9c05bc-e2eb-3a9f-8cbe-6e26612dd341 | -3.06102 | -48.74744 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d176687-1dc2-3294-bc62-d2d4afe1c7ab | -2.50065 | -48.13999 | 2026-08-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7cbaada-9e17-36e9-bf31-7b95f0cfa8aa | 2.5218 | -50.85446 | 2026-08-28 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 895c43dc-6d45-3a31-a89a-d1f9059d1c39 | -0.29759 | -50.41737 | 2026-08-28 05:08:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe7798c-a447-3ab8-9deb-f5e6c7c4af87 | -2.73092 | -47.04468 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cec6b426-5737-3908-b154-71b6bf98729b | -2.89747 | -48.27473 | 2026-08-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53179c86-e8cd-38b5-981f-8392a154d868 | -1.61144 | -55.44597 | 2026-08-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9b45bf50-53ee-3ce7-99ae-a225a948c8cc | -2.72939 | -47.0546 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d359e86-ab42-3e2b-b542-8607136680ea | -1.36336 | -54.63162 | 2026-08-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68313686-66fc-3608-957b-20a9d2db2928 | 0.30229 | -60.4481 | 2026-08-28 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ebaeeef-7e56-39f1-abf9-28b313833cb3 | -3.22149 | -48.61057 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82d16797-e685-3bf9-92d8-09dcda3e02fa | -1.59054 | -47.35804 | 2026-08-28 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e3014be-1d9b-3344-911b-63dd362479fd | -2.09499 | -48.21719 | 2026-08-28 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5bc1298-388b-3a92-a118-7826909bfc8e | -1.35308 | -54.63046 | 2026-08-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 71b6dfea-f708-302f-a5a4-f0effedc529a | -2.1803 | -54.47075 | 2026-08-28 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c4c7bdc-5c74-3ea4-b5eb-723c5516f2e3 | -1.85961 | -55.2095 | 2026-08-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da85c445-3d08-3b20-9743-127f1d727874 | -1.35969 | -54.63149 | 2026-08-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2590f75-af69-3706-9d2f-d7b8a004398e | -2.73026 | -47.04893 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00b27d34-1ecd-3401-bb2e-201a1602e5b4 | -6.1656 | -57.7988 | 2026-08-28 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3dba2468-d88a-3833-b5fe-13b99a2ae9d4 | -7.2661 | -45.8443 | 2026-08-28 05:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0619982a-cd8e-3683-99e2-c2772c692f0a | -11.2301 | -51.2243 | 2026-08-28 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3b144be3-c879-3d41-bac4-17c82af4cf6a | -16.1641 | -58.5851 | 2026-08-28 05:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 197.4 |
| 946b4792-d3e7-3164-997d-38c102d61852 | -16.1644 | -58.565 | 2026-08-28 05:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| c35e481a-708a-3f02-982b-88906900141c | -7.2474 | -45.846 | 2026-08-28 05:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e53e78eb-b541-3057-9c9f-53a56dd91ea5 | -11.2111 | -51.2264 | 2026-08-28 05:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 170.5 |
| cf41d77b-5952-341c-861d-8a18a592262b | -16.1638 | -58.6053 | 2026-08-28 05:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| eea41a36-053b-3421-9f0b-88f03e51429b | -10.4981 | -64.5005 | 2026-08-28 05:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 26f8c2fc-6037-36d7-8f7f-9aedd862ffdb | -11.1922 | -51.2284 | 2026-08-28 05:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9ca4e0e0-eac2-38bb-be08-dd179eeae2a6 | -16.1447 | -58.5871 | 2026-08-28 05:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 33c58606-8b59-303e-b5dd-eae72e73315a | -10.9367 | -50.5332 | 2026-08-28 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9504585c-6aa6-3b95-8fc6-6230a6d44397 | -7.2471 | -45.8685 | 2026-08-28 05:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 24eda93d-3be0-3d59-b021-ac1c66cd1e46 | -6.1657 | -57.7793 | 2026-08-28 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7b215a77-2c16-3f56-818c-38168fe96025 | -10.498 | -64.5193 | 2026-08-28 05:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 8ac0490c-8ae6-37b4-bad9-5e6e35289563 | -11.2109 | -51.2476 | 2026-08-28 05:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 83488ca9-d434-3b48-8247-f399f2132b39 | -10.5166 | -64.5186 | 2026-08-28 05:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ddb89196-28ac-3c20-9ce9-c142243036b2 | -12.43 | -43.4182 | 2026-08-28 05:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8f7607f1-9ed5-3ea0-8ad1-fd122fe24b33 | -9.61679 | -55.11535 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 32a533a9-3209-3059-b670-6cdd48db7ebf | -8.21656 | -54.95432 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6c7e6d9-a12b-3a09-a556-7e11a8d68b82 | -6.17835 | -57.7911 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 235b1f06-5b03-3a05-b969-c1d2a37e0078 | -6.33017 | -57.74272 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7778da54-0d99-3360-b9a1-d276566bda5d | -6.12435 | -53.53065 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb67e154-3fb8-3973-b7cf-2f9bc8145172 | -8.59409 | -54.77578 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebd2a680-83c9-358d-9f43-59a70603af72 | -4.05493 | -56.23347 | 2026-08-28 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22913844-b609-32b4-bc3f-a367cfe5e0e8 | -8.51094 | -55.3551 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f1c68f7-bad6-3957-9430-6db3196b56d7 | -10.55035 | -50.48175 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceb73cac-b7dd-32c3-beaf-5fcd81a56f3d | -8.1493 | -54.9766 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| faa5b126-7f59-383e-90cf-ef75f4900f96 | -6.44342 | -54.98306 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53f3e8e9-b6eb-3bf4-b325-ff571cfea059 | -7.26552 | -45.35447 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6cfc061a-4eea-3633-b837-b53d7ca451d3 | -7.57441 | -61.31007 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee9ac295-11d9-33ae-b96f-1822703f8d72 | -6.231 | -55.49376 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef1f70d-369b-39dc-a486-a3e99698ca9c | -9.96889 | -53.94134 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b6d561a5-fad8-347b-b188-823c9f2e5a6f | -5.81771 | -46.22218 | 2026-08-28 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3918fa8-04a8-37fa-bb78-afb93a802c17 | -5.8172 | -46.2258 | 2026-08-28 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c48d807d-d32a-3d00-a8e8-5b3be2a11075 | -4.05437 | -56.23695 | 2026-08-28 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82570f12-0a29-3a6e-a240-2cf7267b24bb | -6.1393 | -53.80216 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c66703-7ffb-379e-89be-25a175d73c53 | -6.12319 | -53.53832 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c79d4ad2-f623-3072-819a-c9d865d5104d | -6.23154 | -55.4903 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a8bc955-235a-3bb9-8151-2d793f12eba2 | -6.00295 | -57.83543 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3027a92-b35f-31e5-8925-b1e5801f0bb1 | -5.8219 | -61.28394 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e6a24d8-41ab-373f-9abd-a38bf38a43c5 | -7.35267 | -55.16424 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 247c42e3-b2aa-3d4d-b546-203bfb6cbb06 | -10.89682 | -46.63247 | 2026-08-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d9d758aa-9621-316d-9acb-f9320ad6996c | -7.25405 | -45.86601 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 41eca25e-5e27-39da-8194-c9298cc6fa3f | -9.15503 | -49.971 | 2026-08-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dbc4af9-1c3f-39f8-9b00-e4d76a7b776f | -9.22828 | -51.53582 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88795632-00b2-3b05-b08d-123afa7b4836 | -8.5924 | -54.76421 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd88b357-8cc7-3e0e-b876-e598823f97ea | -6.16129 | -57.78833 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 239df010-d3e7-315a-866e-a4f21333c7c0 | -6.3225 | -54.73917 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b372fb99-1106-3b91-951d-8fdadb88967f | -7.87389 | -46.09718 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1fbde138-6c48-3341-a471-13d813d4ec43 | -8.78151 | -50.07391 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ed5871-16fa-317f-8906-631bdb4d37dd | -6.28182 | -53.37481 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90e5e90f-42bc-3e73-b9fd-651529aa4f28 | -9.46214 | -51.58327 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7689a3f-392b-317e-b20c-5fcc8b27925b | -4.93054 | -55.76953 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57ec4574-1215-3db4-b378-9ccf08fb85ae | -6.25569 | -55.42297 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54013b2f-2069-3c28-964f-a8d1ecfb1636 | -8.24475 | -54.99516 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d46886e-870d-3589-b001-c645f596306a | -6.259 | -55.4235 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51285303-2bb6-32df-badc-75180b2b2c72 | -7.03257 | -55.68815 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70ccdbe-bd29-3262-8a1a-78d313031dcb | -9.16015 | -49.96712 | 2026-08-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfc6fba-0b61-3f81-b28e-ed60dd8f1264 | -7.35546 | -55.1683 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764631b3-1c76-3be9-8e6f-374c94a59721 | -6.24059 | -53.48044 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d60c1110-709a-3a86-b1a3-74181272cd69 | -9.2267 | -51.54695 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01ce0ca-27ef-3e1a-aa79-a9be48c00192 | -7.25984 | -45.86672 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b9a1c6d4-6a76-31cb-bcd5-e957531e2814 | -6.16529 | -57.7852 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01b66842-d053-321d-94ec-475370a91361 | -6.39685 | -54.95746 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 419c0c93-d401-30bc-96c9-1adb3de81fb1 | -9.21815 | -51.54909 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029b3781-0b25-3250-bd5a-37c123023f8a | -10.55783 | -50.48923 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6743f88-1d2d-3b5d-b7cc-4ff94b21916a | -6.5282 | -55.24454 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ab40ef0-f696-3693-b6d5-f841d68d35de | -8.95213 | -50.17256 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 877fc791-2230-3f80-95be-77a84f9b5e3c | -5.29174 | -50.93645 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c76fc93-a4bd-31bf-bfee-d7d4befd057f | -9.45549 | -51.71566 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f610725-820e-3e2d-9488-75b17bc1e7b0 | -6.76097 | -55.6877 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7cb5959-51b9-3d79-a184-783e54894020 | -6.06632 | -53.77172 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 104ea851-8dbd-3525-bba5-f175bd04daea | -9.66408 | -55.08507 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8de9a4f3-bbaa-3a67-b1f4-d8fee0603d3c | -7.07096 | -46.26071 | 2026-08-28 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247d6356-da27-31ca-ae74-5d4e0a643388 | -8.58899 | -54.78627 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 514c44e7-5725-35bf-b98f-0270a9c8ff18 | -6.84453 | -59.9423 | 2026-08-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5e4c843-a4fb-3cf2-aa49-37b7561e431e | -6.97506 | -55.64351 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
