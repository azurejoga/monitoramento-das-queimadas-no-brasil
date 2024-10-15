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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93e3ca53-6986-38d1-b884-ab6a274e0998 | -5.28009 | -46.38758 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8702dc9d-ec00-389b-a4b5-852134baaa8d | -5.27935 | -46.36452 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08328ad0-ebf5-3260-91f6-7c3f4efe25fd | -5.27932 | -46.39211 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d2bb005-d184-37d6-93f5-cb9a09b0515c | -5.27856 | -46.36919 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65ec1ce4-2823-39c3-8d30-adcc8f9db7fe | -5.27781 | -46.37366 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d4d11d1-3792-33d4-8b15-717861dfe4fd | -5.27707 | -46.37804 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0c9af4c-6382-3499-9137-6cab6e10e10e | -5.27632 | -46.38249 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 806dfcdd-4f20-362d-8ac5-853c24cd8c75 | -5.27489 | -46.36361 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c56ecad-048d-3be1-b723-45110d1cd10b | -5.2741 | -46.3683 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b76bfb4d-5d78-3a67-b614-b4d2df1a0586 | -5.2393 | -45.4912 | 2024-10-15 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 459c2e24-1a52-3531-8601-38a1ba4a9120 | -5.19411 | -46.17185 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1315f68-6adc-337c-871a-fd7037aacf46 | -5.16741 | -46.14659 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1405294f-2179-3bf1-bd6d-60a901195a98 | -5.16673 | -46.14508 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e1c1ce4-7645-3506-a12c-dbd4b6af9bf5 | -5.16599 | -46.14941 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d81762-614f-33a6-9e2e-5876b5091d49 | -5.16296 | -46.14594 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a4b1c2f-e781-3721-bdec-8ddeab131330 | -5.13988 | -46.09269 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d356b932-7f9f-317c-aab0-49e787b0baf0 | -5.13545 | -46.09199 | 2024-10-15 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a0a1735-c7c2-3d9b-97f8-9c11b6a94cef | -7.90613 | -45.65949 | 2024-10-15 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 252a5180-7eec-3b0b-8f84-b4ecdf6d165e | -7.55656 | -45.95018 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0cb6b325-e9a0-38a9-9d14-0e9a56b52b17 | -7.5559 | -45.95407 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb1c8631-9c53-3ef7-9c54-0b90e7084eea | -7.55301 | -45.94555 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef248c21-3527-3df3-bc94-d22b131055fa | -7.55235 | -45.94946 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9b754e9-53e8-320a-8e83-101fa201b308 | -7.5488 | -45.94484 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d948ec2-f607-32a2-bd40-382398244754 | -7.61277 | -46.65901 | 2024-10-15 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a29bfebd-446b-3c97-a94c-d9040485e8c1 | -7.99358 | -46.86315 | 2024-10-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18322b38-738b-3d68-b222-ac43d5fe465e | -8.95004 | -47.16895 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e09f18d-6db9-3b4b-aa71-6720e266010b | -8.94925 | -47.17346 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fca688ee-6c5d-3520-b632-a70c01a7ca46 | -8.94478 | -47.17273 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 741847fb-6251-34b8-a7f7-139befcd796f | -8.72563 | -46.63771 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c135efb-1ce9-367c-9d7a-00d44f1c8c59 | -8.69043 | -46.63532 | 2024-10-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cb777bb-a5eb-3144-a449-64c54f684ab8 | -9.95599 | -46.19629 | 2024-10-15 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec8b5e02-cde3-3623-8757-c9ae5ee025e8 | -9.95185 | -46.19574 | 2024-10-15 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dbc20e8-ed01-3f8d-9d8e-db6ff9df4e6c | -9.96347 | -47.25401 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e9dce6e8-7265-3a86-90d3-f795235617ec | -9.9632 | -47.25252 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d40de694-2427-370e-a6e6-2e51e32f44c8 | -9.92874 | -47.27042 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57c6536e-84c7-3678-8427-817a6e997d24 | -9.91526 | -47.2952 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a7fc46d8-3f89-3394-901f-d4e0e8e8288c | -9.91084 | -47.29437 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c0972b08-f606-3554-ad29-1e874a397e18 | -9.69172 | -47.14913 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ef3fb55-8431-3344-9832-9ec05c13780b | -9.68782 | -46.482 | 2024-10-15 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43805c0-5276-30d7-9a1c-59661af39637 | -9.6732 | -46.91717 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02822abb-ba73-356d-b020-b23d77033297 | -9.66958 | -46.91229 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94c13aa9-1907-31d5-b3d8-285e216c0b9e | -9.60489 | -46.63379 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f55c9a32-169a-310b-a0ce-6c8c6f3bfb97 | -9.58582 | -46.64248 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eb35c1b-4a51-32d8-8c16-54f271ba561d | -9.58509 | -46.64666 | 2024-10-15 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f0f3c95-8acc-3a01-81d0-55be3933acc1 | -10.28508 | -47.20045 | 2024-10-15 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a03f67c-8cde-34c1-90e6-82c3a4456e6d | -3.31405 | -47.01236 | 2024-10-15 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d48c30bc-050c-3402-a39a-a11f3b698894 | -5.0082 | -46.49157 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f65bfaf-604d-3406-ae48-f716afa45d3a | -4.89819 | -46.69508 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48185370-64d7-3c73-9a96-c9b668648301 | -4.87303 | -47.10458 | 2024-10-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75e58aa6-884b-3489-96db-6b9a2ab9de6b | -4.87217 | -47.10979 | 2024-10-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d075d080-3360-3f52-b784-c0ddf0860315 | -4.86907 | -47.09901 | 2024-10-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cbabd58a-1db7-3d19-a657-0d4fdc744d7c | -4.72116 | -46.71456 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6aab1e7d-ba51-38ac-a584-9f5e554fc999 | -4.95496 | -47.84838 | 2024-10-15 04:02:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c6ca77-04a0-3d61-9cb9-e5930ea4ac4d | -4.89341 | -47.64113 | 2024-10-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| e0ea8572-1cf9-36e9-91fa-0258267c3f67 | -4.89221 | -47.63897 | 2024-10-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| fc18e672-0cc0-30e0-bdd9-1e16a2d91719 | -4.47465 | -47.73589 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ec529eb-4dda-335f-8d17-fc83871a0140 | -4.47413 | -47.7389 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06d2e6cc-3abc-3325-b65b-cd6dfdcaa503 | -3.82725 | -47.48173 | 2024-10-15 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78163a55-2afd-3718-bc35-e43fb4b7c64b | -4.54419 | -46.56044 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0103f0bf-6ae8-397d-ab81-5b465e4745a4 | -4.54385 | -46.55917 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fce7246-b04a-3a86-b288-d7117ccec7d0 | -4.54341 | -46.56519 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf8957e8-8f53-33b1-adfc-effb85c6c824 | -4.54334 | -46.59464 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e5ce856-601b-3aee-85e0-6c342e2f4754 | -8.46534 | -47.81274 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 80b37235-aa9c-3603-9472-b480d2262654 | -4.54302 | -46.56398 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72011d12-28cb-3470-a950-d91f5e33fab7 | -4.54029 | -46.58425 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f397f40-22f2-352f-9434-1658f2c0c327 | -4.53977 | -46.58291 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 568d4470-8429-3cd2-9ee4-524b7ef4ff97 | -4.5396 | -46.55959 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47d7121e-8cd5-3a0d-a5e2-1ed926816de7 | -4.53925 | -46.55837 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e1ee47-8efc-37a1-a8ff-ea9af0032d91 | -4.53843 | -46.56311 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c42ab12f-eec3-34fa-9be2-75e2997520a0 | -4.53569 | -46.58343 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c868006c-2de7-3f71-bbd2-fcac328a15b9 | -4.53516 | -46.58211 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e503b3dc-d8f3-364f-a3cd-63e1b0bd09f9 | -4.53487 | -46.5884 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4546a8ab-adad-334e-b768-f09ca99788aa | -4.5343 | -46.58711 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 851084b5-6f60-3da0-a5b1-b7b28e60cd11 | -4.52573 | -46.55751 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44ee9e06-b6dd-33ad-b382-ec4d1b539bbf | -4.362 | -47.27578 | 2024-10-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f37bf1ac-f627-33ed-b641-cee425b98274 | -4.33548 | -46.73415 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8705e54b-5359-312a-a733-00c4564d61f9 | -4.15538 | -46.25951 | 2024-10-15 04:02:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 301ec7c7-78b9-39e1-bca6-76f69bd09af5 | -4.14718 | -47.17735 | 2024-10-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 761104fe-836d-300e-95ab-d47db4f8a9ce | -4.02759 | -47.21539 | 2024-10-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ff303b1-3c71-34b4-9384-7da3ee7d9590 | -4.01666 | -46.53477 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6070fa-528e-3016-88c0-aa346a06be63 | -3.95223 | -46.43528 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ae6fa6d0-e1e7-3ceb-98ac-f34709b0bd65 | -3.95142 | -46.44008 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1ba623d6-bfd4-31ee-a404-6a4be5824551 | -3.94683 | -46.43915 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 638c3037-8a32-3265-a775-73dcb30df3da | -3.94302 | -46.43362 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65fcbba6-25b1-30f6-b66e-57b6bba09614 | -3.94222 | -46.43838 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41c153af-6813-3e40-a0cd-7b9d67ea505f | -3.94153 | -46.41431 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06958175-1603-361f-b4ee-dc13906db140 | -3.93256 | -46.41437 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 5f68a8e2-f278-34be-9197-8d1c59a895cf | -3.93229 | -46.41296 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 89195bb1-4401-3bdd-bd9a-f444023fb1dc | -3.93151 | -46.41755 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6c71d6eb-f185-3f99-9ad4-497297b840a3 | -3.92795 | -46.41362 | 2024-10-15 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 078174cb-1729-32f3-9828-368d76197ae1 | -3.85847 | -46.90604 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a7c0b3c-b6f8-3493-b997-10af7ee1c6cb | -3.85761 | -46.9111 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e88cd25-b38f-3eda-a1ca-a36740932cf1 | -3.85672 | -46.91636 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c62e500-d8dd-3144-99e7-e66f1d1834c4 | -3.85386 | -46.90191 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7079dadb-f9f6-34f7-a4e5-98f6e11f20e4 | -3.85374 | -46.90496 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 322f7e3f-cc40-322c-bd25-9cdf4c785163 | -3.85304 | -46.90698 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73d0504b-9e04-35b2-9963-78cef86189a7 | -3.84908 | -46.90112 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2043ef99-e03d-3ca3-ab5b-c67fcd2283b6 | -3.84897 | -46.90417 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccd475c3-f1a3-3b2f-af17-fda5c8e101de | -3.84826 | -46.90619 | 2024-10-15 04:02:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2e375f2-81af-33ed-b2ad-ae14d74507a3 | -5.28607 | -46.40706 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README29.md)
