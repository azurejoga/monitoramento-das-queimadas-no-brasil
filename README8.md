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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b1f291f-a3ac-3fa2-89b7-ee3bf49412ed | -12.55742 | -54.5887 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fc392be-d63b-30ad-b8ed-709da397bcca | -10.39354 | -56.75971 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e4532df-480e-3385-8783-ab7a4ab0c8f1 | -13.8527 | -47.14752 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f59acf48-ad56-3764-84c3-b4adb0bece43 | -9.7348 | -47.89458 | 2026-06-26 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0b356df-e156-3e2d-bf96-a2ab0f92a182 | -12.51647 | -48.27085 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31000f10-0bb1-3086-9ace-4c6f33c677ab | -15.59971 | -48.35573 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 547000d8-921a-3185-a416-01547ad853ac | -15.63923 | -46.43326 | 2026-06-26 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| facf9364-7690-3df4-91f7-05afac3cd565 | -10.9057 | -54.12903 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3005a041-8e29-31a8-9a73-ef78ff15869f | -11.91832 | -57.10653 | 2026-06-26 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3778812-c973-3a70-b7a7-7a127aa120f5 | -12.67566 | -48.2193 | 2026-06-26 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9452f5c-b207-38fe-ae9d-1801481d05b3 | -11.21099 | -54.33698 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 153554b5-ae58-39e4-9c20-904bfc6f62b7 | -12.51864 | -48.27902 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe9f1ffe-294f-322d-b048-7876d7e2c2e9 | -8.50341 | -50.15524 | 2026-06-26 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e419f59a-8c3a-3254-8a0f-835c80464823 | -9.69635 | -47.69562 | 2026-06-26 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cfb5619-b449-3aca-91a5-343de9ee43f7 | -11.93723 | -57.70263 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74952fd7-57e6-3539-859b-10ad1a17f05e | -11.20211 | -43.3506 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ba387f9-5430-3a1e-9263-91bf4d0a002f | -10.3617 | -47.34846 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f2043bf-9638-34de-b9ac-693ee3dc4b5d | -14.83334 | -48.12933 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514bbc11-58dd-3f4e-8a31-5bc9ffe99309 | -10.6333 | -47.03096 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dac1f3d2-b88d-3977-ac17-f1f9abd45b6a | -9.40543 | -50.67682 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b50a44a-790d-3e2d-be28-3c976e469dee | -12.87189 | -44.35176 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e1aa6f4-85ae-33cd-b63a-daebedba830a | -9.48213 | -57.3246 | 2026-06-26 04:32:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b2e4f32-c563-3691-9097-2150b181b2c9 | -8.44253 | -51.56224 | 2026-06-26 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f32e2d7-6a8a-3af2-99a5-ab4500a3db64 | -12.03725 | -49.20217 | 2026-06-26 04:32:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f85174d-0972-368e-a8f0-44b90fa12bc9 | -10.15852 | -56.61094 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c454090-e88f-36f3-91b9-2d989fd26e0b | -11.91029 | -43.78086 | 2026-06-26 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d00be7b5-5ee0-3ab7-a6dd-26e51722560c | -13.72427 | -54.0492 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 22bd26c0-4200-3842-91f8-23e83154f754 | -9.18965 | -45.32033 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65ccb1db-e2cf-3ed4-930f-1617485b4a00 | -12.75664 | -44.49356 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb4ab261-7efa-3094-a6e2-84d57a5a1fc9 | -13.73085 | -54.04001 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8deba40-9404-3dfd-85e4-9b10776d793f | -13.26233 | -54.43153 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| bdb3be25-855d-3c71-85a1-86de41dca1cf | -13.4551 | -47.85994 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f695284a-783a-37f9-a947-500441dd0d34 | -13.86338 | -47.12355 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfdd70a8-09a2-3d5a-8fd8-8859bbb2c5e3 | -8.67678 | -47.85583 | 2026-06-26 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b90aa06b-7132-3f12-b94f-6c68788631ce | -14.84648 | -48.11261 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19a944c0-2c84-3314-8ab7-d9c7e7e21502 | -9.47904 | -57.32373 | 2026-06-26 04:32:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57814889-8555-36f7-9bf0-eed776813d09 | -13.26123 | -54.42486 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 30a295b5-f090-30d0-a4d8-26ba976ca5a8 | -9.91114 | -45.52933 | 2026-06-26 04:32:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86daf97c-3bc1-3aeb-bbc1-d2eae8e7ba41 | -10.3623 | -47.34478 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56c9cc0b-fc34-395c-a8e5-ac2b05e522ee | -9.12878 | -47.64777 | 2026-06-26 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7561daa-b5ab-3bb6-b811-1d0405e4e08b | -14.84528 | -48.11994 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 296f99bb-b36d-30e6-8086-6506b6532c64 | -14.58837 | -47.97897 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87ff6376-efcc-32b5-a232-b896b381a318 | -12.75035 | -44.4887 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31761759-f497-3357-b271-ac134238ff0d | -14.84405 | -48.1274 | 2026-06-26 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62102b54-b871-3c2e-8605-c24c51e62924 | -12.86902 | -44.3474 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 381ac0d2-88db-35fe-b5b9-8f0871dd61e3 | -13.84328 | -47.14231 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d664a3ef-8e18-330b-9095-1262ed1f9c95 | -10.63213 | -47.03817 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecd5f242-818a-3d10-b433-9d931643256b | -12.75378 | -44.48924 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0305814-bae1-37d7-ac92-99266d867890 | -11.38954 | -47.81359 | 2026-06-26 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18e23150-16e0-38e1-80e9-c0b8836718a9 | -11.19439 | -43.35375 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8976536b-ed5f-39ae-acf7-c7765cae494d | -9.3653 | -50.54879 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 23304a1e-7508-3afd-8aa4-de9ab080508b | -11.9097 | -43.40064 | 2026-06-26 04:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b22817c8-f768-32e5-ad29-b6be3c41950f | -9.6998 | -47.69619 | 2026-06-26 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b70f9446-73be-3821-928a-2d7320547ce5 | -10.75171 | -49.11144 | 2026-06-26 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35386bd2-d4aa-3c73-a026-76e6ea9d463d | -13.26339 | -54.42601 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6785b5c7-9807-344d-a88f-fa2a3b8e953c | -12.76508 | -59.013 | 2026-06-26 04:32:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a547dca1-c838-3347-baca-0f3b7a20f071 | -9.89252 | -57.40014 | 2026-06-26 04:32:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23396673-ef51-31b3-b248-ac2d9c6e7b5c | -11.22297 | -46.40776 | 2026-06-26 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1baab196-ec76-3252-8f0a-b14bf58065ae | -9.40138 | -50.67614 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0498173-2224-3b53-a54f-66bb1e286edd | -13.87004 | -47.12466 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b180a5ba-bb58-38b0-a468-4080b0b1540f | -10.29214 | -44.69378 | 2026-06-26 04:32:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eee9502-4c8f-3e3f-8880-51d1c85570f1 | -12.76007 | -44.4941 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0dad1cd3-2ee6-30db-846d-ad8e0c754895 | -12.74692 | -44.48816 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25bba6b7-6766-31e0-b11b-b7866304b41c | -12.75606 | -44.49733 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb64e890-ab33-3471-8c61-a7cf8a705025 | -13.27306 | -54.42804 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62276db6-e6d8-37f2-9f0f-6be14fa29eaa | -12.74292 | -44.49139 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6437cd0d-a9a7-3b49-bd33-a56ee86c0d3c | -12.75949 | -44.49787 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb44f396-1ead-3fb0-9e56-4e22518d28b6 | -10.75463 | -49.11623 | 2026-06-26 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46d6cde5-dace-3033-bb6f-a6598ef3bf1c | -10.78065 | -54.10914 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8393b20f-e5cb-30db-a5db-11d94c2726e2 | -11.47741 | -47.34407 | 2026-06-26 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b91514df-34b0-3330-98e3-8c333e590b2f | -11.37524 | -47.81964 | 2026-06-26 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f95861c9-f695-38e9-9696-c33ac67c4751 | -11.91325 | -43.40119 | 2026-06-26 04:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce697d6a-668f-3cf8-aa82-12ed8178d8c9 | -10.1246 | -52.11256 | 2026-06-26 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8de0417-ac1e-3bf2-94a6-a7b2a3f23754 | -9.1891 | -45.32383 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1817ae14-c7ad-3339-90a4-3baf5e78196a | -12.51366 | -48.26647 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48da2aa9-1871-37f5-9488-2127cefe5f61 | -9.76605 | -48.25578 | 2026-06-26 04:32:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 237a7384-fa33-3e3f-9b3f-c0316d51680a | -13.8627 | -47.14912 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c78cbae4-b798-3ee6-ad78-9af2a1d4834e | -10.29269 | -44.6902 | 2026-06-26 04:32:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56565c2b-58f6-369e-8e34-0475f25e23be | -11.91246 | -57.10512 | 2026-06-26 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6127f227-9ebf-38e0-bb69-743b9a837913 | -12.5514 | -54.59333 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03634b5e-57b9-3873-9cb4-e5585cf2e1e1 | -11.77316 | -46.43975 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab6d4eca-7066-32b2-80de-7b3fd3facb32 | -9.18577 | -45.3233 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1653fca5-5236-3296-9dec-dcdad9055d48 | -10.15937 | -56.60658 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dca6cbc9-e5eb-371a-ad8b-4b921f565a79 | -10.77569 | -54.10818 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ce18588-053d-3398-8e76-1438dd8af99c | -13.85604 | -47.14806 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b22bf723-5ed6-3630-8b9d-6a6cc6012aa0 | -12.76625 | -59.00732 | 2026-06-26 04:32:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3ef97fe-770f-3cca-b965-edc14c789f0f | -10.80486 | -48.56749 | 2026-06-26 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 057860df-4483-3a24-8e59-e06a91a1f770 | -10.16355 | -56.61655 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31fd7c16-9b86-34a2-9db9-9800d6ac4305 | -10.38194 | -56.72436 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2ce9fef-14ff-3a10-a1db-a4a9338dabc2 | -9.88947 | -57.40062 | 2026-06-26 04:32:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e123efa5-2fb2-385a-bab2-cd09ceb80115 | -11.63836 | -52.86399 | 2026-06-26 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68085f0-1d24-3200-b4f2-7146634ca445 | -10.38046 | -45.12824 | 2026-06-26 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6e6939f-1160-347d-a04f-869d1b81e355 | -10.75534 | -49.11203 | 2026-06-26 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8160938-8d9c-3561-8ee3-5eaff0240e8c | -9.18632 | -45.3198 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87201c40-9ce4-33ac-b7cd-42560200e107 | -13.73646 | -54.03597 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 507aad22-da98-35a6-8f94-000645450673 | -12.86789 | -44.3315 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6996a6f0-c6ee-3f6c-9727-a585a17791e9 | -15.16298 | -49.8273 | 2026-06-26 04:32:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 866d2d62-35ab-3059-a866-5f597dcddb9e | -10.09966 | -49.59563 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b75a527-e7be-3ba1-83ae-9299fe8d1f54 | -13.86004 | -47.123 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c7a6c21-4188-39bf-808d-7082775ff37b | -9.0771 | -44.76672 | 2026-06-26 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README9.md)
