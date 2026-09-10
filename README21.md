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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cffe3b35-a764-35e3-93b6-c6953c306ec7 | -6.26603 | -53.11892 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99b2c869-8bcc-31e7-b147-903a517e263b | -6.75937 | -58.96145 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec45114a-f9b2-335c-a885-b24c03f120b0 | -7.52403 | -45.01064 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4136825-edf8-3d84-8926-21919e2d955c | -9.71451 | -43.39706 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 459e44c3-68c7-3b76-88be-97c0eb06eb83 | -6.26801 | -46.37152 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3323ea35-af4a-3a22-83b8-5fa208a6eb2c | -8.97936 | -44.97827 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a4a842-aa28-336e-922b-e46b01631c69 | -6.09977 | -44.1343 | 2026-09-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1acc0eba-3a48-3442-9293-64e9e8603a93 | -6.78013 | -58.89264 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7865b48b-1e50-31b5-9653-f3ce7198dd0f | -6.8016 | -58.95695 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15b48d7b-3995-397c-8f2c-ab72dac425a7 | -7.75015 | -49.20272 | 2026-09-10 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2fe86707-bd95-3c58-96bc-dba15fa79ae4 | -8.23752 | -44.75 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3fde293a-e5c4-3764-8d56-033050ec6c93 | -7.12177 | -42.14116 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0d430bd-c489-3fd2-9488-07f93943102c | -7.99239 | -43.96987 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a96a8bf7-548a-385e-a70e-630cca7a9233 | -7.5611 | -47.81518 | 2026-09-10 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 510bb458-0447-31e3-98a5-cb721f9d504c | -4.94256 | -47.65622 | 2026-09-10 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 177ca9ba-5671-3c5b-8da5-90e9eed2af2c | -8.04703 | -46.89423 | 2026-09-10 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f238b7c3-e833-3b33-8e80-de3a81c88e5f | -2.30041 | -48.58525 | 2026-09-10 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e2fb221-6844-354d-90b8-dc5a2762ac28 | -9.72138 | -43.46858 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04d2c82f-13b6-3229-a7fc-dcac998741b6 | -5.92404 | -44.94751 | 2026-09-10 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b5735ad7-25cb-3e6f-902f-2f40d3d11908 | -5.7668 | -45.08161 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 1d507962-0b1d-3970-a9ff-685d10a62a39 | -6.24331 | -51.67934 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1443b324-1722-3045-b249-050f7b17182a | -7.27342 | -44.64053 | 2026-09-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f62094b-b14b-3cd0-b93f-0289de831495 | -6.78386 | -58.89403 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f64f1337-40fc-36fd-809f-4557a96df14e | -9.68824 | -45.2202 | 2026-09-10 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a59946-1ebf-300c-a65d-e50cca3b2815 | -9.59209 | -40.36383 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f17bb6e-c798-3032-8fa7-4f9cca6585bb | -2.73119 | -57.62266 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 20b73743-b254-3842-ae92-0fdea5dc6b34 | -8.08331 | -54.86263 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3543d68d-f5f3-3875-8402-1cdd3ac3678c | -6.77487 | -42.733 | 2026-09-10 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f6bacb5-fc33-34cd-b79a-99606382ae77 | -9.68396 | -43.48236 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4ac84de9-e45c-34e9-9673-41d1cefcba60 | -6.49544 | -47.59566 | 2026-09-10 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17339532-459d-3726-9cf4-497c9634d057 | -7.97899 | -43.98985 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abfd53c6-4360-30d1-8eb4-31221ee0d44c | -5.76956 | -45.08559 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| f0c207de-2949-3552-9aad-b7c9f513b6e1 | -5.11723 | -46.00398 | 2026-09-10 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 793d62fb-e0ff-3945-8d65-f93c46b52962 | -3.24936 | -47.9122 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e1ca36-b6ac-381c-a3dc-ad43d8e95119 | -3.19731 | -51.02156 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e762f692-235c-35fa-9146-9f2f8bf053bb | -9.68799 | -43.47907 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a5f415b-063f-3d3a-ab9f-39fc37a4657c | -8.68596 | -47.98457 | 2026-09-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3109fd96-2807-3f38-b029-086ed1fc6efe | -6.09258 | -44.13674 | 2026-09-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 914d683a-8f78-38fd-b919-b4d564da1c0c | -7.99184 | -43.97343 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7eede62-ffa2-3f4c-b42b-0c3b1d629806 | -9.79065 | -43.49454 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d08e2641-608e-3939-b90f-a8a5d2ab3faf | -7.5121 | -45.25745 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25f88388-e476-3e9f-943f-66489587dd0c | -2.70244 | -49.50964 | 2026-09-10 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7df2377-9ae1-366d-84b3-ce20a5f5ca9c | -4.85996 | -56.01998 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91fb433e-0ac5-3c6f-85a4-c2321bc707dd | -6.09645 | -44.13377 | 2026-09-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65d24252-4576-31d3-a081-ce62b3dc3135 | -7.66852 | -42.15949 | 2026-09-10 04:25:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bf4fe11-9d8a-3f3e-bd7b-7288626aab07 | -5.17245 | -45.46463 | 2026-09-10 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce122216-1802-386a-b0a9-a79c04cbfb5f | -9.54328 | -45.68688 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd02ccd5-314a-39a1-8637-295f2b930c8a | -7.11416 | -42.11922 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 50d7ba83-4719-322d-8b5f-02a798cdec66 | -2.93485 | -50.47456 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76720329-694e-33e0-a74a-6b4b951bec87 | -9.78892 | -43.48255 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f9f21ed-4530-3604-8cc0-6752a4d465d0 | -7.4895 | -45.27161 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0e9dbf5-f777-38cc-92a8-d8f3e343c75e | -9.30315 | -44.36362 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d25bfd-61d7-3b14-a445-247a28769338 | -8.08659 | -54.84426 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505a2767-7ace-3a4a-9c3c-1b976114906f | -7.97843 | -43.99343 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 851c3776-8cad-3c96-ac49-0d7a7fb5a5e5 | -8.08464 | -54.85519 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ce24a5c-4104-382e-a7b6-b34810bd9e28 | -9.72481 | -43.49251 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6af4c8b-4051-3460-9627-3afa584fc196 | -6.77675 | -58.89271 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a42fe73-7126-3dab-9597-3a829c30126b | -4.01 | -51.03083 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6e0f7d-d814-3946-b55f-88f7cb5e5e0b | -6.82114 | -43.04836 | 2026-09-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f5d8c9b-4518-3818-87b1-ceb6d522412c | -8.09074 | -54.85251 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3c8be87-d57f-35db-b705-4503f9e1193e | -5.60633 | -44.85103 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1eefe0e8-f4d0-32d2-a361-6e27d7e98610 | -6.86494 | -46.01611 | 2026-09-10 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 974ab22a-9fd7-33a4-a00f-bc2109c9e4c2 | -5.76735 | -45.07815 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d6cf8a52-1b89-36ee-abd4-252cdecae6ef | -9.71047 | -43.40035 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bf57c15e-f993-30c4-a5f6-41130cec8e98 | -6.76308 | -58.61789 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6a08c7b-13b3-3bcb-9353-0a9fbc893223 | -7.5077 | -45.26385 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae773448-e201-3707-a272-a62a676c7a4c | -9.77968 | -43.44977 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3001700-0eac-366f-ba08-ffb0129be9c5 | -5.37616 | -46.29348 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1987d8cb-4120-303e-ab55-4ce42f189b05 | -7.98124 | -43.99751 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b899692-8f1b-37a0-ba8a-8a48cc938045 | -7.18284 | -44.95671 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53c47527-12c9-3437-8dd6-6c5d35ae0c3e | -7.26212 | -45.35578 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 553631f6-5414-35e5-9989-cf315c232120 | -8.36144 | -41.26032 | 2026-09-10 04:25:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad18d9b6-1c7c-3577-84ef-840364d308d1 | -6.16538 | -44.64617 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 920c0567-eee4-331a-a1bb-4f9b5cee8e84 | -9.69719 | -43.4649 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 813c7817-3b13-3e4b-a184-f18a03740064 | -7.98064 | -43.9791 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2880de41-af1e-35ee-bbf4-69d931f21d9e | -5.76515 | -45.092 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3732c35c-b13d-3b90-9ffc-3047dac7a9ee | -1.70391 | -53.69827 | 2026-09-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a78705a-3561-385b-9095-52bb964fdae1 | -9.68339 | -43.48618 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e63836ae-4b98-3405-8da5-a310994d545e | -6.82057 | -43.0521 | 2026-09-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 557cf0f5-ef9e-3a46-bb24-acd98852800c | -2.94224 | -50.48479 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b19c7788-1eb5-37af-88c1-4b9efc934bcf | -7.11835 | -42.11569 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97aadf71-6a16-3649-9d7a-ab3e9d639164 | -7.05608 | -42.70828 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2aa1eb33-92f4-3ede-9dde-e2d6e37638c6 | -7.50934 | -45.25346 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39850d43-4e4e-3b40-9508-379e9e541583 | -7.46963 | -46.14245 | 2026-09-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09a4d7cb-6cdb-364c-b039-5c38c975b919 | -7.14873 | -46.95897 | 2026-09-10 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 638fb2d1-f656-32c9-a382-3e2ebf2b90d7 | -1.70455 | -53.69448 | 2026-09-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62275d0b-e930-3a6d-b9c0-ce63ede86440 | -7.12192 | -42.11623 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d95806c-1946-3445-9f81-5afd94c5440e | -8.23861 | -44.74302 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e87e8e-4993-3837-b74f-e3abfcdf1635 | -8.98267 | -44.97881 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 221b5f3b-835c-3d77-a614-7862fed6f4f0 | -6.78962 | -58.90259 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d29ad2a7-16cb-3ebe-aea7-6520bb66103f | -7.98618 | -43.94321 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe9118d7-adc4-365d-8bb3-020e2222f55c | -9.67879 | -43.49327 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ef46056-1c58-36c1-8889-7ea56acd5843 | -7.50879 | -45.25692 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2723f4df-04c5-33f5-b13e-c7dfb6b7edce | -4.82752 | -55.77201 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32d3dc37-1084-3c6f-bca2-8cdd093520bd | -7.25936 | -45.35178 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4faa2c8-0f9c-3f7a-bf0f-f431cd33f278 | -9.70239 | -43.40694 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6d13e697-d35e-34be-ab4c-bf352478da32 | -6.5011 | -58.38775 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 39615ec8-b710-36e6-b02c-b833655ee208 | -7.5066 | -45.27078 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9675d4da-2d79-363e-9d87-e74fc350e96c | -5.28487 | -55.96644 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b143eb6-feee-386e-8a17-b5805482b423 | -6.81921 | -58.99631 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README22.md)
