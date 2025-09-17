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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8efe4cf-e8df-360d-8689-a9ec0b8559b9 | -5.99571 | -45.82069 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2130c5-405a-3ebb-bbd8-f769080fe535 | -6.68406 | -46.30415 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 76796625-43ae-3a28-afda-712f7498f4c4 | -10.15605 | -45.29475 | 2025-09-17 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 028879cc-c3db-3503-a628-6f0757b47fd8 | -8.39806 | -47.24313 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc3d9973-8280-3944-a526-8791adad2608 | -7.26039 | -46.61066 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ca2f70-0aea-3c91-a00e-9afa87bfd353 | -9.71968 | -47.40361 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be914890-2168-38a3-af04-9f3a0cd02ea5 | -5.78404 | -43.93484 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eca2a8a6-1df4-3f0b-8450-edd623f1f38d | -11.16735 | -45.32184 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e517d96-ceed-3237-a36c-5d6d07ee71ac | -9.17763 | -46.93987 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 471d5439-b891-3a61-bb8d-b8c1eb5ef3e3 | -7.72263 | -45.29481 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a1d56a5-870d-3975-9e9b-185e67f57c04 | -7.47852 | -47.39141 | 2025-09-17 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e32819c7-04fb-3b78-9b33-fe202e205a0c | -8.63373 | -46.42412 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a861ed98-26d4-3b90-9b13-9067914234e2 | -7.86246 | -48.16819 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50c42359-bfa1-3373-b2e9-da232b1d5c8e | -5.63526 | -51.70852 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7af2274f-8aef-38d7-9798-cc15304759a1 | -9.45588 | -40.37474 | 2025-09-17 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04ef8e08-7589-3d06-8958-0ce01497b61d | -6.87339 | -43.96586 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8caf3712-d060-360b-a2f6-75188204000e | -6.25826 | -44.68 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d539048a-0ac5-3d2d-b7f4-39f5a247019a | -6.214 | -43.90372 | 2025-09-17 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a33722e-7acc-3d56-909d-c86d5294f6bf | -6.25028 | -43.45816 | 2025-09-17 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13447412-c6f0-3a93-93b4-816ed160d7e8 | -8.68225 | -46.40462 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5128502b-eacc-3523-b9a2-6ab0b7f97390 | -6.30172 | -42.40203 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 664cb06f-9def-379d-ba51-dada39591abe | -6.9565 | -44.56144 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 241b0ae8-6b6d-3515-a5b4-ca768b4ddc53 | -5.78314 | -45.95093 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67d7456-9f16-3f3b-8ac3-6625480c1d7c | -8.63377 | -46.42392 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3393f4f-9520-344a-bddb-50cbe16a46f3 | -7.88673 | -48.16492 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ef9e359-8560-38bc-aef5-35fea7682413 | -8.97238 | -44.19061 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6123ea6-b399-397e-8d39-22c8e0a402b8 | -5.01012 | -50.91265 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 968136df-bc02-3bd1-bddc-b1bf12fdb5fe | -9.54857 | -46.29663 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f14fc3fd-eefe-31af-8853-b890f145003d | -7.67591 | -44.47094 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c151f8b-c345-3a91-b4d3-9f5f64e2936a | -5.53095 | -42.18669 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2870a27-a253-3c49-bb80-d69e20c4500a | -6.73871 | -46.99615 | 2025-09-17 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6efd1655-3df8-3581-b767-d7d1cbfa96dd | -8.57269 | -46.34179 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ffa52c7-87d8-3427-a01b-ec011cb67a31 | -10.48372 | -49.37355 | 2025-09-17 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61702395-cfdd-3d8c-a18c-1458057a4842 | -10.80051 | -50.70844 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bd468b0-98fa-3f15-b89e-19d3beeb26d0 | -4.0543 | -47.50459 | 2025-09-17 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 98ee854d-0563-3700-afd0-59ff3aec97e3 | -7.41638 | -49.99157 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1e0408-4795-3f0c-99be-df0f5281e9be | -5.47323 | -45.34609 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dfb3191-eca5-3206-8746-e6821fcbf0eb | -9.07634 | -50.30973 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f34f265e-b35e-3567-8721-6e86108ea54b | -8.6748 | -46.36123 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99eeadd4-8960-3836-856d-f36600dfd181 | -7.58714 | -44.56682 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a0e72f3-d26b-3f62-97b4-8bec823b709e | -9.17876 | -46.93257 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c5aa26d-6ac3-3982-af79-feae6801fb3f | -5.49222 | -43.99194 | 2025-09-17 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2a6df19-d176-3cee-a5ae-c712dfda1822 | -7.17273 | -44.34107 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b351812-8871-37e0-b46e-b9b88a0f1957 | -8.96402 | -44.19439 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3dcab7e-306b-3a79-9451-f862e9be95e6 | -5.64604 | -48.60726 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4b799dd-5d32-37a1-a5b0-1bc720cb435a | -4.92074 | -47.86794 | 2025-09-17 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f55ffee-c072-37a4-b666-c8b00501c72c | -5.78097 | -43.92986 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 269b77b1-1ad1-3cc8-921f-474c92b43550 | -7.48955 | -46.12285 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f751401-1920-32f7-878d-1cfb1d50c3f2 | -10.4296 | -50.65962 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7edc0de-345c-329b-b9a6-31b001cfb20a | -9.15636 | -47.01064 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ad55e40-c16a-3bed-a80c-f9e82ddf6ac3 | -8.56527 | -46.36752 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c31a145a-3c93-33d0-a16f-d81f01593814 | -4.64935 | -50.99274 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d018f33-5cae-36fb-9805-daddfcdaaa38 | -7.82889 | -46.14756 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1929d15-81ee-3b87-9b59-7b0d3502f512 | -6.41113 | -43.35213 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf97f451-343f-3448-8585-58dfdf180525 | -8.98241 | -46.26775 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17366784-7183-3da5-a005-cb1e525a837b | -7.8812 | -48.15693 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab0dc8dc-30ee-3380-8413-bd9762a4a908 | -7.58385 | -44.58857 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41822c53-6269-3d29-9953-9a2cb498fe95 | -8.96659 | -46.33197 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84e4d791-4ec2-3bc4-9357-a2a7b46170e7 | -4.13202 | -51.08344 | 2025-09-17 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317ceda0-3b45-31ac-b0d4-cfb0152d1593 | -7.67126 | -47.78613 | 2025-09-17 04:32:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4290e0b-19f9-392b-b752-b4b2bfd69c75 | -6.31353 | -44.56074 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2e304ae-393c-3761-a1ca-4329db02e4e6 | -7.45208 | -49.50837 | 2025-09-17 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97959f07-61dc-35ef-b83b-592300c6016e | -3.50772 | -48.44754 | 2025-09-17 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca8a8abb-68e0-385e-a128-9ce22f9d1a2f | -8.66172 | -46.40129 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 280da127-b721-3774-8ace-c4414d67fa61 | -6.97967 | -44.45906 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0291d1d-48ea-357b-bdb5-d994edeb0661 | -5.60091 | -44.11419 | 2025-09-17 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 807040f9-9f97-31f2-be36-80503af0d5a6 | -7.0244 | -45.63585 | 2025-09-17 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8558fe04-e827-362e-b8a3-5d6469f85fd0 | -6.612 | -45.5882 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92355bec-39ca-3c3f-afce-3cbfebaf53d2 | -7.26937 | -46.59726 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec9b1071-ef1b-3363-b5b9-3d4652cc9cd7 | -8.92646 | -46.27145 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91b160f3-a1a1-3047-b688-9463bee70a75 | -5.2126 | -45.1793 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39ab90ce-d7e6-3451-811d-d474477439c1 | -6.51468 | -51.19751 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a78cf545-2629-3c22-ae4a-cf45fe1376ae | -7.33602 | -39.71553 | 2025-09-17 04:32:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 828a4dca-51e8-3202-8e58-1e665f3d6a7c | -7.48185 | -47.39193 | 2025-09-17 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f9e8c67-5f3d-360c-90e4-76e259c438af | -9.10223 | -50.4948 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c18b4f-07d6-367b-9868-617d0cc6a9d5 | -4.05815 | -47.50167 | 2025-09-17 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0624497f-908f-3487-b231-7d2bf3f95825 | -9.07173 | -44.95021 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66c1ec1b-60e0-3355-8f56-925f90ee3fc4 | -10.63014 | -48.75038 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f610a2fd-054f-3fea-b97f-b9ee3a18111e | -8.96373 | -46.32764 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 353af461-057b-354c-83b2-d0a685307337 | -7.68332 | -44.47205 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0389a6b5-9468-3514-8a21-ec0ad0119600 | -5.77087 | -43.94645 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c159b81-65b7-3435-a003-12528a8fcd6d | -8.5401 | -48.97298 | 2025-09-17 04:32:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 584f1b39-858a-3479-a5a4-734d80768894 | -6.96178 | -44.77687 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77de0059-44ff-3e0e-a9d1-2cb2c8fc1a05 | -8.68623 | -46.37844 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42313de4-5769-3fac-8657-556ee4dd0ed8 | -7.50724 | -44.35376 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ff36f4-8be0-31f4-8ff5-fa2515780e76 | -7.76836 | -44.72734 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ffdcdc6-7326-3a1f-b985-da119ef22d77 | -6.86514 | -43.96941 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dd17c69-6634-33c7-9d2f-1ee4aed0c5ce | -6.96879 | -44.5545 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcbcf138-5449-30da-9702-5e0ae93b61f4 | -5.44416 | -46.67986 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dffe5c4e-4996-39a7-aae2-0a6c6d227707 | -5.60194 | -45.37707 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78e00b2c-e86a-3135-963f-a7b2885ebfe2 | -4.03949 | -49.07416 | 2025-09-17 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c141dc1b-be6d-344f-87af-7a1944238c42 | -9.95528 | -45.9183 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07d1d0ba-5993-3e62-ab30-915af35e8513 | -5.77247 | -45.90458 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f529ac61-7406-3766-801c-510fa09f93db | -9.17819 | -46.93622 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4444f90f-492f-3789-967f-bfc39a7750f0 | -6.8758 | -43.97565 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da6111fe-b45d-3b6a-b84d-311051d8191e | -8.9184 | -46.27811 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0366bae0-c61d-376d-ae2d-bde4311508a9 | -6.15801 | -44.5297 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1eceeee1-e2af-349d-9597-a4d6a7190729 | -7.58648 | -44.57117 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46dc5833-c86f-38c5-b597-332e64999fdd | -6.97667 | -44.45409 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e8eaa1c-f0e3-393e-b22e-16a7d53d1b41 | -8.58012 | -46.33908 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README37.md)
