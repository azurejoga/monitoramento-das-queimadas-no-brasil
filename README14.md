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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fc22edf-e97f-3afc-9dd0-2162d415c0d3 | -5.7975 | -43.64529 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ec4849d-552b-333d-a5c8-ef01daeeb792 | -5.55433 | -42.15917 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9134fa8c-c992-3bb7-b386-ada07a9eab65 | -5.06062 | -49.94812 | 2025-09-20 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff3c308-4c16-37be-be67-177f9220b193 | -1.17037 | -54.13856 | 2025-09-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da533ae9-ef3a-3454-9f67-5ba71c89abaf | -4.66136 | -46.03576 | 2025-09-20 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6481e98d-6cc5-305e-b335-4d4020fc41b7 | -8.147 | -43.63842 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43eaa7eb-6491-3a82-8a98-8526ca9e6c4e | -5.78837 | -42.7813 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 660f206d-fb70-3ef8-b174-a58761834c18 | -4.27688 | -48.63624 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae3e879-8ab5-337d-aa84-5c363793846b | -5.19732 | -45.47835 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddf44a90-7a14-38fe-a14a-2bcf6f646af7 | -5.13652 | -45.01429 | 2025-09-20 04:25:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03ff5962-03ca-3ea3-91f6-a06be9b28468 | -2.79893 | -49.61824 | 2025-09-20 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a108e7e6-5ebb-377a-8582-b73455063373 | -5.69633 | -43.32948 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a5f6ea3-ff58-318f-98fe-ab7faccfe7cf | -5.50992 | -45.45951 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6afec2d9-00ca-324b-bc66-4cf18506ddd1 | -5.78871 | -43.65601 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c55c7785-e6a7-32f7-b76a-6bb7419dac4d | -7.24014 | -46.62411 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8fad64f-f445-3369-951a-c0ef07b087d3 | -6.39722 | -43.31632 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a670b4a-f6a3-34cf-a1fd-d35bd7f9bf23 | -5.74646 | -42.58597 | 2025-09-20 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 48794043-c3c1-3ea6-b853-0a4ec91a35e2 | -4.67423 | -43.63663 | 2025-09-20 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283ba95a-2b65-3353-8252-d2775fff7b0f | -5.82595 | -43.88012 | 2025-09-20 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ac2d41a-6eaf-3e3e-9168-e6b08818057a | -5.7893 | -43.65209 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 993a8a33-e3bd-3693-9cdb-0d463fe8611f | -7.83248 | -45.63755 | 2025-09-20 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4ec5087-051a-31f5-bfc0-4fd95fa34079 | -5.55501 | -42.15454 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 18a9b9fd-d0c0-38e8-a2f2-6f8a3bc9b8c3 | -5.69461 | -51.74796 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70c5db93-9a60-361d-be3c-395ff0c42a5d | -6.31626 | -42.93145 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd315b34-0150-317d-ba42-47e9c3693183 | -5.53177 | -43.87138 | 2025-09-20 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7b411f89-878e-3d29-bab4-3f1217c4dbb3 | -4.94375 | -49.92662 | 2025-09-20 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7d0704-78aa-3d3f-9897-4e9379b9f3bc | -5.42904 | -43.25488 | 2025-09-20 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aa4625c-af2f-3af8-b8ca-fd9010fbafb7 | -7.41742 | -48.37708 | 2025-09-20 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74030000-38b2-3843-b144-dc70dd7f8dd2 | -4.35569 | -46.28999 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09bd90b0-266c-35d0-aa3e-9599d8369468 | -5.78445 | -42.78252 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 79e837a9-8148-3282-b0aa-973f4b38e578 | -5.86275 | -45.90472 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3629336-0352-31f7-80d5-8bc40998ed58 | -2.7942 | -47.15473 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f124d7a2-0d2f-3afe-8cad-5557a45bdd96 | -6.48226 | -39.69434 | 2025-09-20 04:25:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5bfe9714-6361-3bab-8a23-e48ee5de8739 | -3.96907 | -47.57156 | 2025-09-20 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61eb9adf-3514-386b-93f4-b2279a94a358 | -6.11061 | -43.65848 | 2025-09-20 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d8c9e11-fd7e-337b-a930-45cb1cfb163b | -7.33408 | -44.5668 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcc54ca2-7053-3abb-b82a-c2351b4bc541 | -7.09094 | -47.33578 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c00da038-9730-37cf-8d0d-4dadc62e0235 | -5.08511 | -41.14125 | 2025-09-20 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 640f986f-8d3f-365d-8f9e-6fda95f2fe2b | -7.60548 | -44.51073 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d09cd34d-e169-3f1e-80bf-0429070209eb | -7.25655 | -45.49049 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1819b929-c8ac-3322-9d47-86883287da74 | -5.83055 | -46.2841 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5748b1d1-33d8-348d-a8d1-a5583bb13535 | -6.18193 | -45.42498 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c15d4c2-1615-33ef-841b-1ef438be9ac2 | -3.5168 | -52.74689 | 2025-09-20 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0242e176-c31d-33e7-b4bb-f2d6ee1303c0 | -3.46131 | -51.21211 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 19b518af-1f77-34dc-a0d5-386bbb8770e0 | -5.93533 | -45.08394 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ddd29f-4d14-334c-9809-366231c61b48 | -3.83273 | -49.13892 | 2025-09-20 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae98f429-0e3b-359f-a16c-45b5d784ea77 | -7.83302 | -45.63401 | 2025-09-20 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa519433-e752-3f59-aeb5-8064cd9bb0b3 | -5.11111 | -43.20147 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 99007fe7-8e31-315d-8185-a7da7c5bcdfa | -5.0931 | -41.14254 | 2025-09-20 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a31ee9a0-dbcc-3fa4-afa7-dc2aadbb16a5 | -5.19293 | -45.48478 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b656176-a9f8-3953-b432-db1eee88ca98 | -6.90707 | -45.20036 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba605c19-3848-3a61-80f8-5b69aee61591 | -3.85871 | -40.34418 | 2025-09-20 04:25:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9abf87f7-9db9-3f88-9695-4d2d77c04901 | -5.79222 | -43.65654 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c489f836-9eb8-3204-9fa4-a7adaae43ea2 | -5.84375 | -46.28616 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e96525-d284-3678-b0b6-6a7dae75c84a | -4.29596 | -48.27167 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f42cde8-abaa-3a49-a29c-8d157be5e8ea | -6.19681 | -45.10624 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e32e3145-45e1-3c74-8ea1-b4e4926d582b | -5.53523 | -43.87193 | 2025-09-20 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c010d44c-c6f6-3b58-8f6a-64a37648bf0b | -5.60123 | -45.13341 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12a638b9-4694-3629-bb5b-b67687a2c8ca | -3.34665 | -48.39447 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 563004af-952c-33b3-9f53-83d9852c498d | -5.85391 | -45.89627 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6faed1a8-3260-386c-bfae-411c8684df4b | -6.37147 | -43.34161 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79b86cbc-2cf3-315b-9c94-3dbccf3ad149 | -5.79927 | -43.63353 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab9d91b2-4f05-3d3e-ba73-59a6791ea83b | -6.09455 | -40.89781 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d96bac51-bcdd-327c-9dbf-61b7b0cef733 | -6.9619 | -42.43428 | 2025-09-20 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c1de5a4-bc49-3a68-97b6-48f55da66431 | -4.07551 | -40.47419 | 2025-09-20 04:25:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0de5261-b530-3bd0-87e9-0034feaed264 | -2.63046 | -46.83225 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd342328-c4c3-3f36-9376-31f7efb6d786 | -3.80668 | -52.35357 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29465cd0-7c52-36be-8011-4f1931fb4ddb | -5.23825 | -43.6793 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f16a1c-1893-30a0-aae2-e996056aa72d | -2.3826 | -47.62982 | 2025-09-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43b93e2-5dd6-3a71-a8eb-8962b1b408a3 | -5.30401 | -45.57987 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 694cd76a-2813-34f4-9a84-1a285dab7a7d | -5.08962 | -41.13837 | 2025-09-20 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 714fcc37-8e34-3577-a1a7-2adbdd859e15 | -6.1963 | -41.2281 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cbb6f241-978e-357d-9ea3-0487f7ce6d95 | -5.78989 | -43.64817 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97499410-70e0-3e77-bdc7-8aaba864627d | -4.40951 | -46.27443 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efdb90b0-ed4b-38c3-9ff5-6c5620605ac0 | -8.05794 | -44.09476 | 2025-09-20 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dac81560-7f29-3c67-8aaf-2dec60ac37f3 | -6.05955 | -42.69432 | 2025-09-20 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1df26f1f-f7ec-3dc8-b3d1-645fa47c93e8 | -5.79108 | -43.6403 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6000e2c8-529e-3994-a454-1350a788e384 | -7.59234 | -45.49549 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4e3676b-04f5-3e0d-b310-9c2cc5368ded | -5.86605 | -45.90524 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b906fe-de0a-35b8-b1df-b8a87f83067f | -7.5907 | -45.50616 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9e692a8-4c87-3e7b-b70f-d16f32999c0e | -6.3126 | -42.931 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72e18c65-fae6-3f99-930e-9c240371ddc6 | -7.37863 | -47.04324 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c89caac7-235e-3436-8032-7ec0e294fdc7 | -5.63183 | -45.94586 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eb7019d-359a-3948-96a8-fff23acf66f6 | -3.34376 | -48.38997 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 081e9bff-9d52-36eb-81d0-bbaa25412510 | -3.51603 | -52.75161 | 2025-09-20 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0bbe183-5d62-3957-a416-4eb39dce210e | -5.68242 | -43.1364 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93c246d8-9550-3e50-8fa7-34e4cb31eda6 | -5.67742 | -43.16947 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b2867194-247e-3cbe-82d2-9a907459c715 | -5.03314 | -43.09571 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 186b196c-3345-3713-8128-cbeda43f6d38 | -3.98183 | -51.0637 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e75b48-f41a-3558-9012-27d62dfb0490 | -4.94749 | -49.92724 | 2025-09-20 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb171de6-141b-39b5-b75b-e9bbe9bb7e69 | -6.05217 | -42.6932 | 2025-09-20 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b821166e-7348-3a52-ad73-0954496bdff1 | -8.14553 | -43.63505 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e04e1640-bf1e-37c1-a668-8d9abcbecef9 | -9.35907 | -54.52753 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ebba83e-0387-3f72-86bd-473746388aa9 | -9.11841 | -44.65863 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2735de6-0481-3ced-a004-ee46d6066ed8 | -11.64251 | -52.86237 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00cfc5dd-7848-327a-a7a5-d2b2faf6a46c | -12.2703 | -45.276 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bbffe67-211e-3c67-b9ce-0abdc8ad7b0c | -10.25992 | -46.05812 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b597338-0643-3c05-a5da-86bf8a16c5f6 | -9.36001 | -54.52228 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e138f8e-b9b1-37a4-bc20-86dcb2639357 | -11.28831 | -47.47944 | 2025-09-20 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e091bfb7-699a-385c-9b26-79c5ec6f8a12 | -8.88168 | -47.24456 | 2025-09-20 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
