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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e46e20b8-aad6-3905-bf9d-d2c580458be4 | -11.6717 | -52.189 | 2025-09-02 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 8352ab21-cc62-35e6-92bd-ddf6231d1dda | -8.8659 | -45.7788 | 2025-09-02 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 54956b79-6cb6-3f4e-aa59-ef42a1b67aa7 | -13.3082 | -46.8229 | 2025-09-02 11:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 666bfd29-6a6b-38cc-96c6-f403f811e961 | -6.8911 | -45.8538 | 2025-09-02 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| a2a2941e-b4b1-3891-a482-f530b3584760 | -11.8141 | -51.5208 | 2025-09-02 11:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 50975515-5b22-3c36-bf98-9770f3897d3b | -11.6715 | -52.21 | 2025-09-02 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 1e40b622-5b48-37ee-a090-3d4f26ac6d4d | -11.5694 | -47.6081 | 2025-09-02 11:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 91358541-f243-3d37-b662-fd4c8e6c4d94 | -15.5671 | -48.3244 | 2025-09-02 11:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 4816506d-5eac-3d7d-8741-55f4984f79e1 | -17.901 | -47.1801 | 2025-09-02 11:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0f1ad698-7e1b-34c1-9c5d-be05890a1e44 | -8.8848 | -45.7767 | 2025-09-02 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c928ff27-3a67-3280-9d18-d61c03338baa | -10.0623 | -48.0978 | 2025-09-02 11:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f3e6f11c-3e8b-37ed-9236-3199844221e0 | -12.996 | -48.1022 | 2025-09-02 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| b55357ab-80a3-34f4-b834-5080cdf7b06a | -10.8487 | -47.4546 | 2025-09-02 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9837609d-a27f-37c8-888f-84443cf57efa | -11.6527 | -52.191 | 2025-09-02 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 569ec8cb-1dbd-3fa8-81bd-7230bb89750c | -13.3082 | -46.8229 | 2025-09-02 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 187.8 |
| c27ec3dd-c6fd-3ca7-9e5a-0176c9e759c1 | -11.9876 | -51.3532 | 2025-09-02 11:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a2337833-3486-32ba-a836-7bbc14fa6f6c | -11.1033 | -44.6548 | 2025-09-02 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| ed5d1543-01f7-3f9e-8749-86c70ddc9fd9 | -8.8659 | -45.7788 | 2025-09-02 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2891f23a-2339-3f7d-a59c-c4604a4f6ddd | -6.8724 | -45.8554 | 2025-09-02 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 6ac61ee0-5ced-324b-a086-6191412e789b | -11.6717 | -52.189 | 2025-09-02 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| d46e5316-f317-3db2-aa28-f6b043059664 | -11.4297 | -46.8223 | 2025-09-02 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 1650b80e-0918-3234-ae1a-fc0e075edc8d | -8.8656 | -45.8014 | 2025-09-02 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| cf15a702-890e-31f6-85ce-5269807547fa | -11.1033 | -44.6548 | 2025-09-02 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 4c0cba6b-0d05-3820-8121-816d92a66a01 | -11.653 | -52.17 | 2025-09-02 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d313b7ec-0aff-3686-bce9-5105f6aaa7f9 | -11.6527 | -52.191 | 2025-09-02 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| b967e043-ddcf-3552-aa49-38a764e0b38e | -8.8659 | -45.7788 | 2025-09-02 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 80b595e8-f79e-335d-ac46-54159be04901 | -11.9807 | -45.8858 | 2025-09-02 11:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3d2d91b4-4a8c-38fa-9365-2e7195c26b77 | -11.5694 | -47.6081 | 2025-09-02 11:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 97749fa6-f842-3aa9-b7d2-b68d229329d0 | -11.6715 | -52.21 | 2025-09-02 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 6320bb6e-d303-32c4-b021-ffcc43eb0805 | -13.3082 | -46.8229 | 2025-09-02 11:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 5ccb39b5-c361-3594-a326-2551683d85e1 | -10.8487 | -47.4546 | 2025-09-02 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d9982c5e-e81f-304c-b65c-8559738ba19e | -8.8467 | -45.8034 | 2025-09-02 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 63d8e0e1-8443-3cbb-bc65-0572ded3c8e6 | -8.02 | -44.084 | 2025-09-02 11:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0f5be184-ad7a-3cae-8a18-08dd23480488 | -11.6717 | -52.189 | 2025-09-02 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| c9186aa9-d96a-3809-af65-90aecf985e0b | -17.901 | -47.1801 | 2025-09-02 11:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 58b9dbc9-3cac-3e46-bb8a-e1d4b42be70f | -8.0011 | -44.0859 | 2025-09-02 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| b45c78dc-2b06-3185-9837-b0e632a1f59e | -11.1033 | -44.6548 | 2025-09-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 0b1fd486-3cfa-38c7-bc25-2b449e2ac3ed | -11.6715 | -52.21 | 2025-09-02 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| bade69df-3476-3f2b-90c9-21776c8b9ee9 | -8.8656 | -45.8014 | 2025-09-02 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 0cde9d3d-fffb-3367-9053-cbf66a0e5168 | -8.8467 | -45.8034 | 2025-09-02 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 07b17ec5-aedd-3a84-93c0-47423a58add7 | -11.9807 | -45.8858 | 2025-09-02 12:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d7744a77-5b9c-330d-ac1b-9085c5f69c74 | -13.3082 | -46.8229 | 2025-09-02 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8a90380c-05ad-30ec-983a-2a809d68a831 | -11.5694 | -47.6081 | 2025-09-02 12:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0ae891fc-6a6a-339f-90cb-d658d32550a3 | -20.0548 | -47.8236 | 2025-09-02 12:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 8faaf304-adee-39a3-ba90-f5a580000bca | -11.0841 | -44.6575 | 2025-09-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| e7168fd3-a3a7-31c2-bf56-5056fc256fff | -6.8911 | -45.8538 | 2025-09-02 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| be5f402a-fbd6-3418-99a9-ed422b38889b | -12.8432 | -48.0573 | 2025-09-02 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7fac9337-2827-3439-9b27-dffed039f0b9 | -12.8625 | -48.0545 | 2025-09-02 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9c0103ac-5aed-3462-8701-8c5cd3f44e4a | -6.8724 | -45.8554 | 2025-09-02 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| de5d22c6-f1b0-36d9-a186-8dd922217eb7 | -11.6527 | -52.191 | 2025-09-02 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 627d6eb6-a135-377b-8521-019ee088d2db | -5.9698 | -44.2923 | 2025-09-02 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 74b6433f-806e-3ca8-8840-348688bccc78 | -11.6717 | -52.189 | 2025-09-02 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 85e95603-9e93-3f22-bc91-0251ef1fabc3 | -11.4297 | -46.8223 | 2025-09-02 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9d392cb2-960b-33e0-881f-70c86ad66997 | -8.02 | -44.084 | 2025-09-02 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| bf5f574e-5e5e-34ce-bdb9-e59651f80193 | -6.0514 | -45.6048 | 2025-09-02 12:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 86dc1608-a7ef-3eb5-b9fe-fb4a4544aeb2 | -11.653 | -52.17 | 2025-09-02 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 80fd0e1f-4ec2-35ff-a673-3f6d2ab7d386 | -11.1037 | -44.6315 | 2025-09-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 96fb7ee1-de09-30b0-a05f-d12af25cae0c | -7.9163 | -46.4577 | 2025-09-02 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 04420827-e50b-3090-b37a-83a3e213fbc3 | -10.0623 | -48.0978 | 2025-09-02 12:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 657c25cd-6863-3429-ad81-c767a552e3c8 | -8.02 | -44.084 | 2025-09-02 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| e1e1fea9-28e0-3740-bb4e-b7c7274bcbbb | -11.5694 | -47.6081 | 2025-09-02 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e6983448-f478-3f50-8710-ee5362666119 | -11.1037 | -44.6315 | 2025-09-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 45abf6af-084e-3aee-bed9-3079bc40e29d | -7.9351 | -46.4559 | 2025-09-02 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f79c54f7-504f-30c6-b0c3-cbb52349ec5b | -11.1033 | -44.6548 | 2025-09-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 95bd54da-9236-388b-a69d-535101752305 | -11.653 | -52.17 | 2025-09-02 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 5b82e4b0-f357-33aa-a610-48a9d8bfa994 | -17.901 | -47.1801 | 2025-09-02 12:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 066b6ae0-9dd0-3a2f-8caa-6a1b3a7b975f | -6.8724 | -45.8554 | 2025-09-02 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 29cd72fc-6215-3034-bba9-e6c9b8453590 | -11.6527 | -52.191 | 2025-09-02 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| f5150357-eb19-3667-80e6-bde040170432 | -8.0203 | -44.0608 | 2025-09-02 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e4440c14-9c0e-3ed5-8e57-710936766a0c | -6.8911 | -45.8538 | 2025-09-02 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 00d2328f-2cb7-3ef6-96b7-63d8d1f4378a | -11.6717 | -52.189 | 2025-09-02 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 003bb986-6040-356d-8af6-0d1b32eb2f73 | -8.8467 | -45.8034 | 2025-09-02 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 39ef989e-1d03-3ac8-ab0b-263bcfd54d65 | -11.6715 | -52.21 | 2025-09-02 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 485e8a02-0c3e-31c2-a501-9145ddf3e393 | -8.8659 | -45.7788 | 2025-09-02 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b762f46c-df86-302f-8ca0-737a8de32f40 | -7.9163 | -46.4577 | 2025-09-02 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 87897b79-5412-3633-baab-d11919103457 | -11.9415 | -50.6131 | 2025-09-02 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c2541d37-75aa-3776-8f0c-ec807e7d97b9 | -8.8638 | -50.5847 | 2025-09-02 12:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| ea1279c2-328f-3e2d-87f9-b293d32db927 | -20.0548 | -47.8236 | 2025-09-02 12:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 83990afd-514b-3166-87cb-8b236fd94413 | -8.8656 | -45.8014 | 2025-09-02 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 9dbe02d7-bd89-3f96-be2a-007cdcd28d03 | -11.853 | -51.453 | 2025-09-02 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 335a7e64-9e7d-312b-974e-6d6165f55152 | -5.8694 | -43.0003 | 2025-09-02 12:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| fab790ca-a474-3018-b2b5-5ea3e9fb8a5f | -11.1033 | -44.6548 | 2025-09-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 15891dd6-ec35-307f-9b4f-59515cd34e6d | -10.062 | -48.1197 | 2025-09-02 12:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 82aaabee-9dcd-3c26-9a36-25c34811eaac | -11.8518 | -51.5378 | 2025-09-02 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 18c1faaa-ec46-3db2-aa70-2a0c855cdc0a | -7.9163 | -46.4577 | 2025-09-02 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 32c05edf-01f6-3164-812f-572807815e58 | -6.8724 | -45.8554 | 2025-09-02 12:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| bd74ac85-75f9-3303-9f01-7631937f2ad0 | -11.653 | -52.17 | 2025-09-02 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 3b5fe9b4-3353-306d-9380-ce70ef00ed8e | -8.8638 | -50.5847 | 2025-09-02 12:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 6d0154af-4cd3-32d2-b1a8-3e284fc3c9fd | -11.6717 | -52.189 | 2025-09-02 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| f89f1297-decc-3359-909f-8816e91e2650 | -5.8882 | -42.9988 | 2025-09-02 12:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 61f4f7ae-5100-3532-bbab-467752687028 | -6.4859 | -45.1647 | 2025-09-02 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 182.4 |
| ec5db4bd-b827-306f-8485-47bb535b8713 | -11.6715 | -52.21 | 2025-09-02 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 1735b59e-3d15-37be-a320-d21cb1adf433 | -11.1037 | -44.6315 | 2025-09-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| dad345fc-e5db-301c-8d6c-2ef2913e2726 | -5.9511 | -44.2937 | 2025-09-02 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f794f9c1-2e3c-3a53-9228-71676696d88c | -7.9351 | -46.4559 | 2025-09-02 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a1fa29d8-5101-32b1-9c48-0d7c1ba1f0d4 | -10.0623 | -48.0978 | 2025-09-02 12:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c76db32a-acaf-3b70-a252-ba0d014044a0 | -11.5694 | -47.6081 | 2025-09-02 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| de4bba79-cb6b-3341-9966-3ddf67cc75ff | -11.8527 | -51.4742 | 2025-09-02 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 4d051e3c-c22d-3de3-ada4-2df48ec54b88 | -11.672 | -52.168 | 2025-09-02 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 613dda56-b875-329c-93d3-b7d60ec435c7 | -7.9165 | -46.4354 | 2025-09-02 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README89.md)
