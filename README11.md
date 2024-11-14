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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 738267f2-e9d7-3203-8013-a19bb7930feb | -4.27076 | -48.23568 | 2024-11-14 00:41:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 88305a70-e138-3745-881f-5bed0da8a68a | -2.18903 | -46.35494 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ace880d5-972a-3a11-9a74-a23f1ff13797 | -4.38408 | -45.90222 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dc231ab4-b317-38b5-bd00-9d3b7ebaec86 | -2.19026 | -46.36376 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a3ee34a-7fe1-3ba5-b3e7-fe0be3c0ee92 | -4.78138 | -46.11137 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1022c93f-4d87-3d47-90f1-cba53c8d798d | -3.05465 | -50.28028 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 74bc1a80-a7a2-3835-85e4-446714caa2a5 | -4.17187 | -46.1038 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8c5ff080-2dac-370b-b853-72758102b20f | -2.8858 | -46.85987 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cb1b0b99-0646-3e99-a066-f60f8289a033 | -3.78943 | -52.08158 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| aa90660d-4315-3c91-b533-d3c94b3cfc75 | -2.02906 | -46.93066 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 91c87d7c-a7f5-3886-981f-3316f43a5d82 | -5.62974 | -46.52501 | 2024-11-14 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cc2631a-a56b-3c60-b1ed-3f7bec9921d5 | -5.61201 | -46.39647 | 2024-11-14 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 689c26b0-3938-31b9-b7fc-f57cf25ab90f | -3.34921 | -45.42322 | 2024-11-14 00:41:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ea5950a9-9b1d-3409-8b23-5e369c99e28d | -2.61562 | -46.17476 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9918ec69-3138-3cce-94d1-d0ddbbc97c71 | -3.63635 | -50.59796 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 13fa6367-0bb8-385e-adea-cc254540bb36 | -2.82115 | -46.6638 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f6f5a859-6ce3-3ab7-88b6-2bb35b1d87e1 | -3.43046 | -43.89944 | 2024-11-14 00:41:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3678012b-fb56-3592-9dee-555d7531087e | -2.66993 | -46.8287 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 11cb0be2-7f16-314a-b2aa-6f38c0dead7d | -2.54502 | -47.12653 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 40741875-f286-39b5-9792-30a281a7efe9 | -3.17041 | -50.46082 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7fcfb82b-804b-3fd4-ba3c-93f1176d60b9 | -3.02217 | -45.65592 | 2024-11-14 00:41:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e01caf2f-2c7c-3fec-9f95-d2319e0e740e | -1.3501 | -49.15092 | 2024-11-14 00:41:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 103f5d33-1ea4-3434-8833-074c431784c2 | -3.03693 | -50.33165 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6c22f945-804f-38a8-a5f2-c252900adcbc | -3.86572 | -41.04028 | 2024-11-14 00:41:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| af845128-0aa6-334b-84b7-87e13034b5a7 | -4.9429 | -44.96022 | 2024-11-14 00:41:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e08adc98-64eb-3ebd-9b0d-99179f184ad4 | -3.07326 | -45.42677 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 250d84c0-1261-3017-ad6a-aed16e847dff | -2.3762 | -46.5057 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6c33ea8-def6-3a12-ada9-dc2e4640d5cd | -3.2346 | -46.52082 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 975cb686-d395-30de-ad7e-0d5dfbff3804 | -3.14548 | -45.28377 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e4a94e3e-06b1-325b-bcf5-c60c2bf40f0a | -4.48102 | -44.69236 | 2024-11-14 00:41:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1ced61b-49e4-34a9-98cf-ee733a70b0dd | -4.14649 | -46.25872 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cd4f69d7-1259-3519-80f5-2d4c266ed7b9 | -2.08951 | -46.62783 | 2024-11-14 00:41:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f489c0cc-c662-3bf4-a594-6213c90e785c | -5.3614 | -43.55519 | 2024-11-14 00:41:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c2549d67-a7aa-3543-bb1f-377579b48337 | -3.12819 | -50.32706 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 109d78a3-666c-305d-bde9-1dd3bee3e51e | -4.99995 | -44.25083 | 2024-11-14 00:41:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 101c46b4-6ad4-3ac8-ab2a-7cf064b8a1fd | -3.12559 | -50.22804 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| da781ab0-dddd-39d7-97f7-b75050cdbd25 | -4.79861 | -43.66935 | 2024-11-14 00:41:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2969e3bd-fbe0-3292-aaa5-e35f928e015a | -2.64462 | -46.18864 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9774295e-7ccc-3453-806e-d5f09f2bc746 | -4.25652 | -44.14231 | 2024-11-14 00:41:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9fb80904-0e2f-33c3-a484-5b19245f4388 | -4.14245 | -43.8562 | 2024-11-14 00:41:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f4e53f78-e1de-35d8-a8bf-6d753893dc64 | -2.67117 | -46.83772 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f02d83cd-0c54-3c91-9254-20032d8a1553 | -2.37892 | -48.52979 | 2024-11-14 00:41:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3fadc7eb-84a5-332e-b998-12ebe71ee5c5 | -4.44791 | -45.37409 | 2024-11-14 00:41:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 123ee9d4-d389-32c1-8845-a465f579e9be | -2.63454 | -46.18107 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6e694d60-e3dc-3489-b411-0af688177ddd | -4.2132 | -50.7019 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 50f854bc-8f27-33c5-9e8f-0eb7fc8a8ce5 | -2.64094 | -46.16221 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| c7bd8326-a8a3-36d3-b674-03970592585b | -3.13661 | -45.28504 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 25bf2c0e-6927-386e-b8c6-2eb03cf85d06 | -4.21232 | -45.32973 | 2024-11-14 00:41:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3bcd55a-0b9b-30b6-a7ca-9365df58d338 | -4.15298 | -45.7729 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| a635b6da-8651-3626-83f1-bd13e283bce9 | -3.0745 | -45.43561 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 93647cbf-7840-3121-a8f2-fdacb59caa38 | -3.86766 | -43.93348 | 2024-11-14 00:41:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d021528b-8495-30df-b463-f06e835e73a5 | -3.47459 | -50.25547 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 80c23ba6-a43e-3049-baee-60657be307ad | -2.47831 | -45.85012 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 036a33c7-aee1-3b7a-b615-47761801418a | -4.15175 | -45.76408 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2180621-ee25-3236-9bb7-a39a9e2dd83c | -2.41733 | -46.26879 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa3c70b8-43d2-3881-89c2-806ac5ee58fb | -4.16491 | -46.24983 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8b14f0da-32c5-318b-a28f-3e73c14f7611 | -2.66744 | -46.81064 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 476b0749-fa10-3f0a-9f15-5e9279927a96 | -4.44845 | -46.57357 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b3efc46d-70d6-36b4-a77d-11a4934300bd | -2.11149 | -46.5253 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a8607e0-b80f-3001-9fd9-0751b2cf9e4f | -2.70607 | -45.56619 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 3146b30a-9ede-3702-842e-aa52a94a8960 | -3.55633 | -49.91122 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fdebd8f1-256b-3667-8dab-34248b7241f7 | -5.15572 | -46.0889 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b16120c3-d33b-3e51-87c2-902362fd6559 | -3.25351 | -50.40543 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dca752af-69dc-3561-a3da-f960ae6854ac | -2.1118 | -50.69376 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| eeed7164-d6e3-3a9f-a317-48d5e74ae3cf | -2.62857 | -45.14242 | 2024-11-14 00:41:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38d190a8-0b64-3e83-b31c-90fe2b014147 | -3.96993 | -46.70826 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1e6ad58-50f1-3e82-9c61-1f33569040ee | -4.27212 | -43.73695 | 2024-11-14 00:41:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 19448184-4bb3-3416-b632-dec86f3712e2 | -4.44668 | -45.36526 | 2024-11-14 00:41:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1991c763-07c6-3a7a-ad53-d4278a44b5bb | -4.06081 | -50.00581 | 2024-11-14 00:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f4e418f5-1462-3467-9b53-e8bc77e6ab04 | -2.67887 | -46.82741 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 55a8fb6e-c34f-3c79-8100-9e89877cb74e | -3.8858 | -46.09941 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 826f94d3-00bd-3b27-ab97-7dd11015db20 | -2.11272 | -46.53415 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fbe65e34-2941-3538-88e7-129e2c369cdd | -2.24455 | -47.48521 | 2024-11-14 00:41:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 75f99ba4-8b4d-3c3d-9941-4624b7d4196b | -2.63152 | -46.82149 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0981b3f1-0db2-3f69-be05-042ab6361e28 | -5.35689 | -44.3676 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e4deefc-ed0f-31e0-b883-4db9c194cdff | -4.03992 | -47.21777 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 524fb9f2-b120-3e80-95aa-59f3227ac737 | -2.3679 | -48.52066 | 2024-11-14 00:41:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 812a9b48-d967-3d8b-9c01-f71d30ec550e | -2.24325 | -47.47586 | 2024-11-14 00:41:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 26fe97f3-5c1e-345c-bffc-0fbae54056ea | -2.67461 | -46.99977 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0149871e-25db-3da6-98b8-a11a8c3f339e | -3.10397 | -45.97054 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 75bd5ea0-6f81-3222-8971-d7d2a5eacd37 | -2.08092 | -46.56572 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 918f2129-baee-39b2-895a-a0d73d4beff5 | -3.12625 | -50.31301 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 14a23793-7c63-316a-8eec-e38961598fe0 | -4.01383 | -45.56523 | 2024-11-14 00:41:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 904cfa77-9679-3c64-9438-5b367be37946 | -1.92978 | -46.2842 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 238808d1-9acc-393b-95aa-589d37077ff9 | -4.38144 | -49.92949 | 2024-11-14 00:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2daed432-c34a-3f88-b6c6-56bf4d578ebe | -2.95863 | -45.39483 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9eb48690-6006-3751-bd27-bd1c07aa028f | -3.41408 | -50.30697 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 2f868eb9-131c-3bf3-b044-fbab19a6c6f5 | -4.77414 | -45.73251 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1dab929-f7d1-305b-a0e5-45a38f787f88 | -5.00658 | -44.49763 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc8dc13a-b306-3483-bce6-cd10413b0a38 | -4.24539 | -43.93235 | 2024-11-14 00:41:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 720e6428-1552-335c-85f9-dcfe5a56c77f | -2.12159 | -46.5329 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 510ccb49-5e7b-3198-830d-905ab3d8f2f9 | -4.1411 | -43.84667 | 2024-11-14 00:41:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a4d11856-7b8e-3921-9a96-79daa53860c1 | -4.05167 | -47.2355 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4f32663a-a478-3187-8df1-6522768c04df | -4.53294 | -45.92007 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a3d40288-603f-3f81-85d6-49b5c2db7647 | -3.3805 | -43.94604 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 55f57ecb-a3e3-30be-b97e-9c9ad1f673a5 | -3.48755 | -50.26804 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8af90687-8e55-38c8-8235-b7b963e7183b | -3.42773 | -44.99204 | 2024-11-14 00:41:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bc9f7ca0-e9c7-39d3-8208-15958a36ca2d | -2.12036 | -46.52405 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58a1f68b-59a9-3183-a8ab-ddc30f7360e8 | -2.95364 | -48.02172 | 2024-11-14 00:41:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 57d020b9-19c7-3c06-9c44-46b03869870c | -3.30299 | -43.51002 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README12.md)
