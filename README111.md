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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ccc384b-00df-3a46-8a5e-3f1437126979 | -9.0507 | -52.97717 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 143f9c8b-5204-32eb-a617-f0ee6e71aced | -8.93917 | -52.78121 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 140ab8a8-97f4-3043-b268-3ace211beade | -8.93694 | -52.77081 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec30ee8a-d311-3ab3-9520-cc50deeca31c | -8.89907 | -52.75805 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bed63010-173c-356c-a1bb-6e11c4a0e6ae | -9.02983 | -52.10738 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 855d4453-092a-31ce-9d79-a1b42e39fc72 | -9.02904 | -52.11203 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9a037a2-6569-3a09-9321-3bfd69bc6a6e | -9.02826 | -52.11663 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93ad2a16-86d5-343d-aca0-4a5e1dd92bbf | -9.02611 | -52.10668 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 962c8a59-73ae-313d-9272-e1d5fcea3aac | -9.02238 | -52.10605 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4603d59-b7fb-3738-9758-3d4a17db4c2f | -9.02163 | -52.11044 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c9f3507-6915-3e62-ab5e-1027f8c6069a | -9.01865 | -52.10542 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58285b4d-b10b-3cda-b98f-4cf0f61f99a0 | -9.01848 | -52.129 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dced3ca0-980d-3671-8aaf-c7a53d488243 | -9.01475 | -52.12833 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89b9bc16-4fc6-364a-acbd-528a52e7926f | -9.01339 | -52.09116 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7a05227-50bb-3cab-a7b5-f46ef3803c77 | -9.01316 | -52.08887 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eb282e2-852a-3b58-ad03-5119148c5e9a | -9.00968 | -52.0904 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51559e5e-d4d3-30fd-af7c-ca4e89cbcd31 | -9.00944 | -52.08813 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff6268a-4b58-34b2-9d3d-bff8bf0732d8 | -9.00598 | -52.08963 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 811b2297-d769-3b45-9610-0f90433deca6 | -8.94973 | -52.12404 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4e3b8ae-097d-31de-8a6d-11e04658db5f | -8.22529 | -51.7406 | 2024-10-04 04:32:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4bf557-ba76-34b5-a5e3-92a20af65a44 | -9.75978 | -53.16621 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6713c1a-8207-3238-a15b-893fa0e7c8c4 | -9.75585 | -53.16552 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e8a1715-4397-37d3-ad0d-94c98615afc3 | -9.73668 | -53.18287 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bb878c5-7834-34d0-887a-6e8cebb0e5d7 | -9.68948 | -53.18344 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff8afabd-d48b-3e58-bb3d-9ab1226d2b37 | -9.68769 | -53.18477 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd9151c2-953d-37f0-880f-f7aaa0ae6549 | -9.68723 | -53.17269 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cb503c4-339e-3367-b0be-4655339388f5 | -9.68554 | -53.18276 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23c297ee-b262-3189-afb0-fb2fef32d6ff | -9.68551 | -53.17405 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9edbd302-8def-3cf2-9115-ec85683a22eb | -9.68463 | -53.17907 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c878f1a-33c9-30c1-9d72-244f357aacd7 | -9.68414 | -53.16697 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3156418d-8db6-395e-ab37-e6e088b57311 | -9.68375 | -53.1841 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf0faa9-ab93-33cb-8cac-793f876ddbfb | -9.68245 | -53.16834 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd6bb6e-0282-3a87-a386-77b783b0d355 | -9.6802 | -53.16628 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7aa27bd7-e79b-3ad2-b0a1-1336fce332db | -9.61333 | -53.20155 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10d9df76-086f-30b9-be11-c979a9c7d7e2 | -9.60939 | -53.20082 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e77f07ab-349c-378b-aa55-320a35aecca9 | -10.40396 | -52.91878 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00702684-6e92-302f-bbc8-2f21f1cd88c0 | -10.40013 | -52.91811 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a0975aa-2b0e-3f18-8e1c-3534c35bfa23 | -10.24563 | -52.73946 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58cf98fe-aa8d-3953-9362-1a7e072725a8 | -10.24483 | -52.74419 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79e680c9-b3ea-32b9-8992-90cd78d7783b | -10.24183 | -52.73877 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b72ecf1-1e67-305a-b4a9-421f0996ce9c | -10.24103 | -52.7435 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 614a70cd-ed69-3263-9363-97b6cad9daee | -10.23803 | -52.73808 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e01142-0333-3f12-a854-f497c29eaed6 | -10.23723 | -52.74281 | 2024-10-04 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 018add56-f857-3eb5-81b8-55cfd2d6280e | -9.84409 | -52.06976 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f96a9bd7-550c-3e94-807d-89dfe5a37e0b | -9.84335 | -52.07418 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e584c1be-12af-322f-88dc-e2114952bfe6 | -9.84189 | -52.08299 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f8fb9eb-cda9-3dbe-9c44-c7ffde49833d | -9.84116 | -52.08736 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0079064-00d9-3d76-adf7-23bb2a63bf29 | -9.84111 | -52.06491 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63a5f55e-a89a-39b2-9275-3043be240915 | -9.84039 | -52.06919 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39f7673a-7498-36dc-b6c5-c39d00623b0e | -9.83747 | -52.08672 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ffdeda-0e7a-3b76-8fd9-5a04c4a8858c | -9.83741 | -52.06436 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f014cd28-be78-386c-8fe6-7c67d6593267 | -9.83672 | -52.09123 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1674ed1-be06-309d-88a9-7281ef7cdbde | -9.80868 | -52.05487 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1c38020-cf9a-36a3-bdae-7b37226c5f98 | -10.27918 | -53.31949 | 2024-10-04 04:32:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f65269d0-cbf8-3f88-9ef7-685e75a673d5 | -2.95323 | -52.78413 | 2024-10-04 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cca0dc61-37ac-3055-a29f-b701e70994a6 | -2.95215 | -52.78283 | 2024-10-04 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 153c3a66-f7a7-3649-9990-b0b68939ef3c | -2.95151 | -52.78669 | 2024-10-04 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8301b19f-ce29-326c-b295-889a2118ba76 | -3.76734 | -53.42033 | 2024-10-04 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70eb7483-79e7-3cb3-8302-24ab73f45d83 | -8.56275 | -53.33203 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c27d648-4bba-3c6e-ace4-28d11f0a487d | -8.56215 | -53.33565 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685c5f3e-68ca-337b-b5e9-e7cc57ce528a | -3.45496 | -53.98462 | 2024-10-04 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76629582-0053-3753-af3b-30a248e1b1ac | -3.46031 | -53.98073 | 2024-10-04 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9744b7e-adfd-37e1-a958-96293d0b0f93 | -2.95296 | -53.70423 | 2024-10-04 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53e9120e-a8db-39ea-906b-546c65ff2132 | -2.95221 | -53.70879 | 2024-10-04 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5715287d-39fc-3855-9484-092dcbbfb496 | -2.94842 | -53.70348 | 2024-10-04 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21342ca3-6e46-3f72-82f2-67a3191486bf | -2.8987 | -53.86263 | 2024-10-04 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc79c2f0-b6d4-34ac-ba10-abea4637da0c | -4.11699 | -54.91504 | 2024-10-04 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5fea4a5-35cc-34c8-9eb6-8b7db06e1c18 | -7.98136 | -55.06748 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9388d3-9803-3aec-b4e0-2db388ab460b | -7.70726 | -55.2075 | 2024-10-04 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 806f130d-c0b3-3d5f-a7f4-caf1fb8db28d | -7.70419 | -55.20987 | 2024-10-04 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea57f662-d569-325a-b4b3-1568d42e77f7 | -8.51417 | -55.15941 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d66276d-55c2-3661-a668-0b51ece2ed09 | -8.5096 | -55.15863 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d610691d-f611-37e5-8d6a-95683ec5ab34 | -8.49048 | -55.00055 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 397cbbb0-b4d1-3d04-b363-9cfac2058d05 | -6.47141 | -56.00215 | 2024-10-04 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3e0b1a3-a7f4-3df6-b0a4-31cc267f1f7c | -6.46543 | -56.00689 | 2024-10-04 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f2e748c-5021-360b-bf5a-df83f1b211d0 | -6.97226 | -59.09969 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e68682e5-2a74-3201-a8ed-8a1b1e34a95a | -6.87554 | -59.04462 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09d26d85-d00d-3369-9dd0-c07fec9edf57 | -6.87385 | -59.05389 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99a3e53d-7875-3c32-9867-61888ff883dc | -6.87118 | -59.03413 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db817c53-7d90-364d-91f2-27b8ea465f8f | -6.87992 | -59.05503 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d3ec411-df55-30f8-8b81-8815ef8edcbc | -6.87639 | -59.03996 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd775760-27ed-3d8f-8265-b21dd128ef10 | -7.1399 | -59.31668 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d8a4bfa-64cb-3803-9f76-140204054607 | -7.139 | -59.32158 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc5ae701-d628-3199-a14e-46ecacd98632 | -7.13375 | -59.31554 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f95d75-1129-3061-bb73-91b647c2b8be | -7.05559 | -59.29953 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5fe2a94-1b25-3c92-a87e-eeb97b72d98d | -7.05472 | -59.30427 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d8cf8e0-742d-39e3-9615-6ffab60495a1 | -7.04857 | -59.30312 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe4de43-379a-3b10-b290-f556603a8e54 | -6.81363 | -60.10965 | 2024-10-04 04:32:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33943cb5-c488-32f9-8fef-9d46e77116cb | -6.8071 | -60.10866 | 2024-10-04 04:32:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 580a20a0-fc08-3d88-a702-fd22f3e36fe3 | -6.71468 | -59.13104 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32cf59c2-04ad-3e9d-acaf-c000ebfad75a | -6.7138 | -59.13577 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73d8b2d6-73d9-31b7-813d-3754670d2a1f | -6.70894 | -59.1333 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93f765c1-a03a-38ac-9dbf-70eac64a1b2a | -6.70772 | -59.13442 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57ade006-e1de-310c-8b5c-839e19147877 | -6.80808 | -60.10334 | 2024-10-04 04:32:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b4bd0a-d194-382b-9a7c-19bc9bda8219 | -6.71586 | -59.12991 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93595862-8296-3d78-b22b-89597e7b0068 | -6.71554 | -59.12638 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5386240a-a212-37be-85a1-2861de23be89 | -6.71502 | -59.13463 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d79838-42cf-3aa9-9b07-42094c6edd10 | -6.7081 | -59.13801 | 2024-10-04 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5d00d0-88af-3a98-ba54-ae61c782c18d | -20.50366 | -42.37751 | 2024-10-04 04:34:00 | AQUA_M-M | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 7549f0d8-0e8d-3e42-b925-33aa1b02dffc | -21.83782 | -48.38852 | 2024-10-04 04:34:00 | AQUA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 147.0 |


[Clique aqui para ver as próximas entradas](README112.md)
