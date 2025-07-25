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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210dd928-d271-337d-8c27-49c713f39452 | -13.71551 | -45.69126 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6107d254-ec34-3e5c-b8cb-ac87c885a627 | -12.04211 | -45.42988 | 2025-07-25 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f73f2ea-2617-3327-9f7e-53e4300bbbbf | -8.07086 | -49.71593 | 2025-07-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e38d4c0-e172-3f0d-9837-a1dbeaace8ad | -13.708 | -45.68332 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43981543-522e-35f1-9e39-4459be62d0c0 | -14.94778 | -46.98512 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a04b4f8-0e5d-37ae-9591-3db3dcc851da | -14.15846 | -49.15078 | 2025-07-25 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60206bdb-46e0-3cae-bdbb-4a6afb21e4fd | -9.97141 | -64.95592 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad22e6c-7559-3c69-9784-9bee53a8824c | -11.74277 | -58.34422 | 2025-07-25 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 998df5e6-4f9c-31a4-a681-5ea7a93fe3e9 | -12.65698 | -45.04135 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96de24fa-c3d3-3581-9719-3448b9a98986 | -14.30613 | -43.79882 | 2025-07-25 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd617985-1066-343d-9498-f21cf0aa6e5c | -8.89024 | -45.57621 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 325f8ffd-a8cc-3317-8be4-51a63b40c54a | -13.09854 | -52.13661 | 2025-07-25 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51bb734c-2580-3823-a1fb-7215a210f3ea | -13.71723 | -45.68456 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f874759-5d47-3dbb-a32c-4c530d6186f5 | -14.94825 | -46.98145 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60efd85c-3982-3741-9c9a-da18159d10cd | -12.57723 | -56.97544 | 2025-07-25 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdec16c-e4e9-389a-ad51-432e41e68937 | -11.45731 | -45.12065 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2cb0d92e-a28b-3424-9333-6dd8eeef53d9 | -8.92721 | -47.34536 | 2025-07-25 04:46:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f4bd288-d484-366a-ac71-ee616c1662a0 | -12.4277 | -45.37504 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 389dfcd2-0b74-31ff-93b3-bd4d8b9ac3c2 | -12.70287 | -46.97868 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94a16921-e332-3f18-96b1-ef2d7d71fc18 | -11.67613 | -58.49639 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 871ab4e8-28a4-3021-98b9-03aa88901f35 | -15.79659 | -41.96024 | 2025-07-25 04:46:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1271d32f-9720-34d2-9b44-5b6f79485c2e | -15.59723 | -46.51939 | 2025-07-25 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aad5fa9-f763-3cc8-8ecf-cfc03860c4e3 | -12.04733 | -45.42568 | 2025-07-25 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f68ca2-b970-32b5-8257-9e70d92bbb2f | -11.31947 | -55.21715 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b58b710e-1040-373a-85ab-475728b750d7 | -8.89204 | -45.57547 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f166d48b-07c9-33cc-9dbf-832a8274e2bf | -10.04235 | -59.10472 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b81289e-39e0-3652-9fae-829aeddb2ea7 | -11.45201 | -45.12497 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7fd55452-d933-36c6-a845-8912aa4bbe38 | -9.37824 | -48.0074 | 2025-07-25 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91e2310b-5745-3e07-8e0b-bb350762bc34 | -15.66611 | -48.18211 | 2025-07-25 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7ae8fe8-96b3-321f-a1ed-af614ce0e16b | -9.96873 | -64.95296 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4246658f-bbbb-3310-b0a9-4c7f0f007792 | -11.45137 | -45.12986 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 48d0313e-4997-34ce-94e0-b2a78c193e9e | -9.05779 | -46.62046 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d05c2e1-8636-38c5-93ed-03d2c12eb9a9 | -14.30534 | -43.80552 | 2025-07-25 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 280afeba-c249-3aa1-a8f9-db44f3e87f35 | -13.70871 | -45.67043 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a6053ef-cacc-3dc1-ae05-8e8266363298 | -13.71272 | -45.67597 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09bd5508-7528-3aed-a91c-400f428ff38c | -10.60978 | -45.24356 | 2025-07-25 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e38a96ad-2cf6-301d-8593-6a00f8f4f307 | -8.12652 | -50.46495 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8bc604b-b444-380b-828a-c5408353c800 | -11.31394 | -55.22303 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ebf5a44-a25d-3abc-91d1-45f083346125 | -12.25692 | -44.58611 | 2025-07-25 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| adb141a8-69d6-31a5-b767-8ec43e89ebc0 | -11.31592 | -55.21655 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a380ff0-c1ce-3537-b2ad-0831b7a6d081 | -12.4625 | -44.65385 | 2025-07-25 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 01ee7c73-0142-3bf8-9171-8d58082c6a59 | -15.04832 | -47.68929 | 2025-07-25 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 358cbe91-6d3c-3275-9044-0f29bb015171 | -10.43065 | -44.18324 | 2025-07-25 04:46:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbbba904-e227-39b7-90f1-3da36d56b029 | -13.71789 | -45.67966 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cda4d50b-0598-3987-a751-3b2384893bac | -14.76861 | -48.26757 | 2025-07-25 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d02bbf2-c62e-33ba-8533-3a3a530af1aa | -9.59197 | -46.33833 | 2025-07-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aca11a9c-8418-3e06-8b28-a07b7dea0c71 | -13.7115 | -45.68575 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8cf9b12-9d3c-3dad-a10e-2d93bfbcdde8 | -10.6217 | -44.76535 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71d02de0-9824-399b-87a5-f462960877bf | -11.44272 | -45.12373 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| acf40102-6274-3ae0-8875-77429e45f654 | -8.89221 | -45.59315 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3011aaf1-3c1f-3bba-b374-b9d568156b8f | -10.62016 | -44.76332 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1471cc1d-4ba5-399a-b9ca-c68e6a372e2f | -13.71211 | -45.68087 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2d79cd1-c07b-3556-ac86-82d2b0210d6c | -13.72012 | -45.6919 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9460957b-3aa0-3eeb-90c7-a3e58918c4c8 | -13.7081 | -45.67533 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99c7c74c-7e83-3697-9c8c-fedd19cefff9 | -8.11705 | -50.45982 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72a7591-87df-3f5c-94e6-4a293b51e27b | -14.93975 | -46.97937 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84546383-b257-3deb-a146-eece7e44c7ca | -8.89696 | -45.5719 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5dc0ba0c-2b42-33cc-b4ee-75e3b9eddf82 | -10.44581 | -49.05208 | 2025-07-25 04:46:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81170a7a-f403-30cb-8fc6-7f859dfd0047 | -11.94529 | -58.76243 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 89fd11fc-d912-3d0b-bf05-d433dd3caebc | -14.94401 | -46.98032 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6d3d12-8f83-3822-b3a6-af1dbb624571 | -13.09744 | -52.14371 | 2025-07-25 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 461458f6-acf7-38e9-ab17-269ce3dec9dd | -14.95157 | -46.98978 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f773b69-cce6-3b4e-99e6-70ee4a67acbb | -8.36718 | -51.0784 | 2025-07-25 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e9ea874-0aba-37a5-8b6b-643b1bcf49b0 | -11.44208 | -45.12863 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2028b86-adda-3403-9ea0-d630211f0757 | -13.71456 | -45.66925 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0442739-336a-303d-9cbe-5541190ef229 | -12.73559 | -46.98815 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef95b3d7-802d-341c-9de8-a7feb327c433 | -8.30853 | -55.10662 | 2025-07-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba3f78dd-e428-3725-9778-363a52f103dc | -15.05242 | -47.68995 | 2025-07-25 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff00f1d1-febc-3be7-883f-fc4c8131680f | -9.74442 | -65.11237 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a66fbd5-a4ba-3ea1-9d3b-55e0bd734576 | -14.21286 | -43.95386 | 2025-07-25 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb6687d9-ed38-3738-8ce5-5976f593965e | -11.94607 | -58.75814 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23dd1034-255c-3a09-88c1-2b677eaeab5e | -12.43103 | -45.38546 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d33743c5-9a39-3b6a-8543-c66c2f6bb371 | -8.85952 | -45.60546 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e686e2f4-507b-3ad6-a188-f369aedd6087 | -11.94448 | -58.76693 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4a879a3-bd06-343c-b75d-d0e8402719b9 | -8.894 | -45.58085 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95040868-8904-3a2b-a255-f40dc0525cdc | -12.6966 | -46.99382 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 396ca383-12ad-3476-b551-edc1d4661267 | -10.63297 | -55.31178 | 2025-07-25 04:46:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e7f4ce-d550-3fca-86fa-783cc8cdfbcd | -8.12318 | -50.46444 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d7c04d4-c047-3df2-a564-d43daf144451 | -8.8211 | -44.51369 | 2025-07-25 04:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60303f03-cf3f-3c7e-88f1-9a886e6c1488 | -9.73762 | -65.11124 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71648d7d-9f98-359e-b807-85c87b2b664d | -13.71197 | -45.68882 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0b3f11f-d0a6-3279-b2c4-aa32e056a1a2 | -11.46132 | -45.12609 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbecbea0-b1f5-3ed8-81fd-3023975127ca | -11.7812 | -47.32739 | 2025-07-25 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a848eb0-e0f8-376a-aa18-e716ba29ec98 | -9.19958 | -59.68259 | 2025-07-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86847a6d-97b9-32e8-9cee-d1564c938c97 | -11.67688 | -58.4922 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfea60f6-6966-3d52-a170-2ce507bd9d2c | -15.60113 | -46.52454 | 2025-07-25 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c10111-f013-38fd-b92f-2fda85ba70f9 | -9.12996 | -63.92245 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ab2dd73-ad30-3a79-b485-44f84afecf70 | -9.20539 | -59.67812 | 2025-07-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052fb569-9700-31f9-8cd6-ddf0eef91a7c | -8.12597 | -50.46852 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3ad9808-2f23-36a5-844d-c3887e0ca453 | -10.61495 | -45.23963 | 2025-07-25 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c783e3ec-a7bb-35d8-864c-84f305add203 | -15.59606 | -46.52864 | 2025-07-25 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb3411f-4cb8-33e0-8285-c54ce7880342 | -9.65953 | -40.5945 | 2025-07-25 04:46:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f3227c43-fd9d-3680-885f-d730cf6a3f8b | -11.31959 | -55.21136 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56457c36-6cf6-3dc4-b02f-f5933b172d55 | -11.95042 | -58.75893 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0fc4bc6-270f-3b49-910a-c03ba21b671b | -9.73283 | -48.01907 | 2025-07-25 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db6bfb11-670c-3c9d-af00-35cd07c1a646 | -10.38939 | -51.50241 | 2025-07-25 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a677647-3c00-35d6-b4c9-03c6eb4c7f88 | -8.84709 | -45.59972 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0e2fb86-6a68-352b-914f-f574f4f37f1d | -12.25644 | -44.78414 | 2025-07-25 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07e94002-8d71-36be-ae94-772958cfb3e7 | -9.05374 | -46.61984 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb87f00e-43c7-3f20-b2bf-76f21ebe8155 | -11.44801 | -45.11946 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
