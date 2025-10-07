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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c7b371e-9d25-3b07-81dd-01e8d0576569 | -5.8452 | -42.84642 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4f8fefe8-c698-359b-b37f-d4cd078b1168 | -8.1918 | -50.31519 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| dd6fa1b3-f721-3dc3-91ae-b8d9780964c3 | -5.66814 | -42.76651 | 2025-10-07 00:13:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8c588442-05ac-3906-aa2e-09db21b97076 | -4.0086 | -43.28704 | 2025-10-07 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd1e5077-ac6b-367a-9712-a905cfef9f5f | -7.56598 | -40.51418 | 2025-10-07 00:13:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 445567f8-1ca0-3379-8008-7228d80f9285 | -7.11611 | -45.08806 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 28ec8b6a-6604-3b65-9e1f-8a95612220d4 | -8.19259 | -50.30838 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 40145e92-b066-3e35-b02b-c91d2e085f57 | -4.21815 | -49.98813 | 2025-10-07 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9880d06c-e402-3aa9-9a3b-0ad0acb53dca | -5.37359 | -41.00376 | 2025-10-07 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d76bf3b6-42d5-322e-90b4-2eca32558a3e | -3.92002 | -45.36937 | 2025-10-07 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c21dec6-c441-3bc9-b501-2bf13c3bc1ae | -8.50519 | -46.31604 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1185dbc4-dccc-38c5-9178-70995c43f411 | -6.15733 | -44.08777 | 2025-10-07 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 69403567-1578-3680-84f8-c23249135e67 | -6.66283 | -42.7594 | 2025-10-07 00:13:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5b54d3c6-0cc2-35b5-becd-7e59991d53d2 | -6.45016 | -44.59415 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1da677f0-05c2-3133-a449-6ddae8f0804b | -6.2365 | -43.26683 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0977fed5-a603-3b83-b1a5-d545a7dcb609 | -6.42426 | -47.82723 | 2025-10-07 00:13:00 | TERRA_M-M | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9db5ade3-5fd0-356f-8c86-365eb782e738 | -6.33277 | -44.02335 | 2025-10-07 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 731806b7-8795-3bf3-985d-21bd44e6aefc | -8.60524 | -44.9217 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 7ad84aff-9d23-39a4-8484-548fcc9d8ff9 | -4.00471 | -48.99107 | 2025-10-07 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ed548ebf-41e8-3309-827a-5d49ad544dec | -4.57921 | -41.30367 | 2025-10-07 00:13:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c74263f3-9f6d-3dfe-bb19-ef9e6fc8229d | -7.23684 | -46.31965 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fa0cd6fe-445e-3240-83ef-a5b37d83db24 | -3.41951 | -43.16369 | 2025-10-07 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 396a4858-2b46-3a01-b903-18b6e5cebbcf | -8.17597 | -43.35787 | 2025-10-07 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 201ce3fc-951a-3b38-8cfb-ec234115fc93 | -5.66951 | -42.77615 | 2025-10-07 00:13:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3bc43fd7-5ada-3735-9f17-514063075f5a | -9.09223 | -47.95282 | 2025-10-07 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9ff1d40d-7b4a-31c5-8dd2-509cb9317548 | -8.61661 | -44.93859 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b14594d6-afb6-320b-9583-43a0eb45a8db | -8.64186 | -46.29088 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 19069a43-5f98-3c06-9977-1d287fe276f3 | -7.49668 | -45.17567 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be38c881-b762-31d1-827d-8fa583ba21fd | -7.13868 | -45.04205 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2559909b-db6e-3101-92b3-da7d6daa162c | -9.08758 | -47.95913 | 2025-10-07 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 61586506-da35-30e8-b26a-03da741db5df | -6.98147 | -42.00763 | 2025-10-07 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 51951597-1d05-382c-831d-3a250970704d | -10.09196 | -48.17399 | 2025-10-07 00:13:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 86f90720-6a93-3a78-9833-6879466e9c57 | -7.02782 | -42.79734 | 2025-10-07 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7e31458b-ecd3-3ba6-97c4-b0a4973bd390 | -7.61202 | -45.47927 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d2faadc7-5832-36dc-a25d-25420ccebb94 | -10.0377 | -48.29045 | 2025-10-07 00:13:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| cef7eb94-86eb-3f30-a597-dea345d28f5f | -6.33345 | -41.61533 | 2025-10-07 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cfaec543-abb1-32b8-9282-9db08a35f788 | -5.66765 | -44.26913 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1851a7a8-830f-3d55-a32e-9901aa365ac6 | -5.95403 | -42.7657 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ba1d24b6-52b7-367c-8dbc-cb0eb98dea24 | -7.46446 | -42.62622 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0fb4d8c0-118c-3875-aa86-ae25a3e830f7 | -8.61292 | -44.91141 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 223cdc94-d4a7-31de-a49d-58a3886ea1ef | -7.6991 | -42.39793 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7cf4005f-459f-387a-8380-83c9214fa0a2 | -7.4071 | -45.19398 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 62fda3c7-adf3-32f0-8031-11603ae254de | -6.87092 | -46.05786 | 2025-10-07 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b49ae8a7-2625-3608-a944-94db99e99289 | -6.97061 | -41.99884 | 2025-10-07 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6ab0845e-2f91-3a0f-93b3-2289b611d3bc | -7.71882 | -42.40489 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 7178e2bf-d301-3308-b9ed-af3c2842efa4 | -5.49053 | -43.07656 | 2025-10-07 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3a249dc7-546e-3d63-870a-8ddd9a1b50fb | -4.29012 | -42.01022 | 2025-10-07 00:13:00 | TERRA_M-M | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a0b53409-dd22-3a08-8428-995444434f17 | -6.87224 | -46.06753 | 2025-10-07 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 545a07b7-4037-351d-b4ae-356a2009f9d3 | -5.61302 | -43.94266 | 2025-10-07 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| af5d9173-3156-3f8f-9a74-b2e5b10ad1e3 | -6.13536 | -42.67762 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 10ead8eb-ad9b-3070-a3e3-1a28758f52a8 | -3.9188 | -45.36055 | 2025-10-07 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64c0d912-5768-3522-b9e3-726238d8a5a7 | -5.59894 | -44.43751 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fed50e5-6a27-3c98-a6f2-e71c455751cf | -6.72322 | -46.32666 | 2025-10-07 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d76c47cf-dac2-3ceb-8754-d6c93fb53b3e | -5.02143 | -43.67002 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f014150a-00ee-3d18-a387-fdd3a7260743 | -8.66068 | -46.28815 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 41615e46-de35-388e-8c3d-1b1e2c22b196 | -9.92647 | -49.97692 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 70e92070-f75c-377d-a397-feccd51041fa | -8.61538 | -44.92952 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 490.9 |
| 1950ea9e-5d88-388b-82e2-c3a67e4dfb77 | -10.18741 | -45.5309 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e748705f-5dff-30be-b2a3-ca5b2762f4ab | -8.49905 | -46.31223 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2dc0146e-ed7a-3d2a-8c30-05da6fcdeecc | -8.95704 | -44.59954 | 2025-10-07 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a94dee1-a30c-3995-9e11-077fb70a52bb | -7.22053 | -45.17716 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c1c50db-a2d0-3e0e-aeec-a76279929094 | -7.29742 | -44.78904 | 2025-10-07 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5b5bde86-9f02-38c4-973d-ffd8d43f1d4d | -5.57907 | -43.57198 | 2025-10-07 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 7b4005e9-53ff-3b21-a440-ae9d02b2c5ca | -10.38165 | -48.00027 | 2025-10-07 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0d370d2e-dfa9-3629-b8be-178b6cf963c3 | -5.10795 | -43.17172 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 65073e22-c80e-31fe-88c3-219877855341 | -5.63896 | -43.60958 | 2025-10-07 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9586e351-4b31-3a03-85c0-231c49c60586 | -6.16643 | -42.57861 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| dfbb246f-bb58-3eb2-bb9a-a2143aaa2701 | -6.36482 | -42.86582 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f8b675cd-725f-37e4-bc71-82113f678613 | -6.70221 | -42.19125 | 2025-10-07 00:13:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5a0ed7d8-46ad-37ab-b23f-efc299bedfb4 | -7.35485 | -45.21059 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a95a2c4-6a38-3ddc-801c-2e0b36e73234 | -7.68292 | -42.4065 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| de479e25-3cf3-3305-902c-5d05eda150be | -4.4899 | -46.36333 | 2025-10-07 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7d214107-f2c7-3aae-b1f5-073b9794eb17 | -8.56606 | -44.63329 | 2025-10-07 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 04c01d5a-c5f4-3700-a921-4088036c8843 | -5.84247 | -42.82724 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6127457f-5ccb-314d-b7a8-ea5fb22faf2f | -4.48244 | -44.30025 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9319d0ae-57e3-31f6-8ddf-c3c0a0a03906 | -9.96834 | -43.78173 | 2025-10-07 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 89f67792-94c1-38c1-bf86-938f04bf17b8 | -7.01741 | -42.78929 | 2025-10-07 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8faa1304-4254-32e1-990a-cfabdc5fbd24 | -6.1572 | -42.57991 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 6233f1de-055c-3765-89ea-e8b49d0b24f3 | -5.32391 | -45.24621 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5c2426c0-6858-390c-a6bc-9ca8f941069f | -5.63231 | -42.71281 | 2025-10-07 00:13:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3cc7382b-7dc1-3af6-8ab5-4ed230b6100f | -10.94713 | -51.18072 | 2025-10-07 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5364cb35-c3b8-3c22-a8c5-4a5e1dd36962 | -10.87329 | -51.03893 | 2025-10-07 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 19624d47-cc6d-3bc6-ad9e-cd1321a90e5d | -6.59231 | -44.63058 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 94996092-096c-38c9-ae71-73f2919f2bab | -4.79387 | -44.61549 | 2025-10-07 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4f515a49-e48d-3b53-97ee-99dd8b642479 | -7.85962 | -46.78149 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1e001882-d4a2-3c3d-81f4-60e8676eb8a5 | -9.9798 | -48.01301 | 2025-10-07 00:13:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9724622f-a841-3151-a669-a59571fa0474 | -4.49118 | -46.37275 | 2025-10-07 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c263a47b-a6a9-3144-b961-1989495f85bc | -8.56475 | -48.25451 | 2025-10-07 00:13:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e6c5405a-6b31-35da-91f6-97f201fd0243 | -8.18931 | -50.29591 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| cc909583-7c56-315b-bf94-138774a64e46 | -5.39236 | -40.9887 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 40277da8-1e5e-36cd-91c1-9173b5560365 | -6.12976 | -44.61898 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 07679dfb-4f54-3608-abb7-fc1d8df256bb | -7.6966 | -46.24577 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0cfd4e87-307d-317d-bdee-842c5cd4f6c1 | -5.73652 | -42.5314 | 2025-10-07 00:13:00 | TERRA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ec9d9136-5f10-351a-a633-308d0b206b15 | -5.39412 | -41.00074 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 7f04bee9-b607-3796-87bd-a1248adcc859 | -7.70197 | -48.0631 | 2025-10-07 00:13:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e41a1149-aaf4-37f0-a223-6d24574bcf8b | -6.31527 | -46.10378 | 2025-10-07 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65ad60c8-9408-362b-80b3-cc5789916711 | -7.11487 | -45.07906 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b85b6635-58c0-343f-b1a7-20f23786f5a3 | -8.1722 | -43.33091 | 2025-10-07 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4e16c62d-7e85-3aee-a09c-d29ff1f5a3ba | -7.90949 | -46.86164 | 2025-10-07 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9ea55f34-c6d6-35ba-a2e1-1c87853dc916 | -6.69578 | -42.86071 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |


[Clique aqui para ver as próximas entradas](README7.md)
