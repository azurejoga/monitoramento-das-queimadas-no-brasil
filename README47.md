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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1b41624-11a1-3952-a882-56a560f08f67 | -6.83158 | -56.44613 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b232b1fa-3c57-397a-9ee8-4577463662dc | -6.77934 | -55.84527 | 2026-08-16 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fbd7732-ac01-3535-8b10-c2f23c26834f | -6.86279 | -56.41306 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18a2c620-f9c2-35af-bd6b-a12207d682dd | -2.95773 | -49.2706 | 2026-08-16 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f966f440-6067-380e-abe3-c2f64b0045b6 | -3.51103 | -58.94884 | 2026-08-16 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1f2315a-0f10-3631-9355-b9822d757a6a | -6.8261 | -56.45364 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5581ebc2-ad82-3dc9-a3fc-93d6bd1d1f0c | -6.86096 | -56.42539 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 216e34ad-b1c7-3466-9533-32b055b52a38 | -6.6007 | -56.36949 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb4f2ac2-25a0-34a6-b0f5-3912c06ae0e2 | -6.86157 | -56.4213 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff8664c2-fab2-3a41-8518-b0975b98c8f8 | -6.54314 | -55.17199 | 2026-08-16 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42f1fd2f-8f9c-36ad-a84c-4b7950d00313 | -3.49982 | -59.58502 | 2026-08-16 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e55dce5-fc63-34f5-8fee-a262216c9740 | -6.54243 | -55.17703 | 2026-08-16 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb497359-efdf-3059-b928-ebb9437c2713 | -6.83038 | -56.45433 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f0cf56-f65a-3d8a-be08-bc9252bad4a6 | -6.6358 | -56.39952 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8e1fefb-2d22-3ae4-b498-5a08eed01ad9 | -6.85235 | -56.42421 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6698a323-2cd4-3da5-8ebb-55cc28bc145f | -6.84444 | -56.4481 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fbe6e20-7334-3a53-aa54-bcf870d37148 | -6.3755 | -58.31872 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f548bda0-ed4b-3b51-9316-caeca66b0c78 | -3.50385 | -59.5818 | 2026-08-16 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfbfc328-1672-368d-a7cd-24849978fd68 | -6.24533 | -55.62273 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08beb9b8-1d4e-3529-b9b8-308636807dfc | -6.84076 | -56.44333 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2276e5fe-d1d8-33e2-a8b9-76ddf43c45b4 | -3.59511 | -58.61899 | 2026-08-16 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37d4f36-1808-32f9-add2-174e357bd7b5 | -6.85543 | -56.43311 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6af6bc5-1e36-3902-a73b-220b17c74b33 | -6.85604 | -56.42899 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f06ba1-dbe7-3b12-b2a6-60c4ea4b1fd2 | -6.81813 | -56.44818 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5100d1fa-ad47-379b-88ca-e9d5cccf6985 | -2.74653 | -60.23727 | 2026-08-16 05:33:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 707c606d-b680-344e-b318-09fb697cb3c5 | -6.83647 | -56.44264 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58db39ea-44b2-32f5-aa68-707b4a1f5dfa | -6.84504 | -56.44406 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f047884-4e65-3c06-bc21-2a7e0318a6d8 | -6.84564 | -56.43999 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0b9cb06-43ca-3897-90ed-4bf9f4591a7c | -6.58475 | -56.35821 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddfb76f4-3fed-3d3c-b3f6-6ed7ada2db86 | -6.83406 | -56.4591 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d3bd455-c976-3f7a-99b8-c728d888bb6a | -6.78508 | -55.83707 | 2026-08-16 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37b96371-d41d-3575-b944-69f247d76414 | -6.54963 | -56.542 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276684fa-bc4e-30fd-bb3c-0da9bbeb5f9b | -2.95857 | -49.26501 | 2026-08-16 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df12b7d7-9dd1-3f49-859e-db36e4554e9c | -6.82909 | -56.43318 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d3454be-110a-3090-801c-ad323b0dcc09 | -6.86833 | -56.40538 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd85ab8b-17f1-3675-ae54-b2f9adb3f110 | -6.81695 | -56.45628 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08aaf21f-1348-370c-895d-2d43371ffe5e | -6.81577 | -56.46442 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd8dc36-a525-3c5c-96d6-7c3a90cdb94d | -6.86588 | -56.42191 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60f8b5a4-4784-3d01-b2b4-a77585d484fb | -3.7398 | -55.9766 | 2026-08-16 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e0fda8-1e8f-34af-868f-ec097ea5ef81 | -6.83278 | -56.43795 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a202771-5a29-3750-8ab3-32c8e62f4cb9 | -2.9594 | -49.25946 | 2026-08-16 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed7dc6b8-98d5-3c63-83d0-d4da8f958520 | 0.49015 | -60.59578 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca1e6183-72e9-311f-ae14-7b9193d497b9 | -6.6352 | -56.40356 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91dcac81-b521-3e93-afb1-516bd1ab2001 | 0.49291 | -60.59183 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f5e2bbf-bd04-3cc1-a3cc-c3dcb5a5bcc5 | -6.36724 | -58.32219 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b0e9d0b-bbaa-3df1-820c-3bdef001dbe7 | -6.84993 | -56.44062 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e36953c8-8418-3e0c-a0f3-aa1345990d84 | -6.53707 | -55.18126 | 2026-08-16 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f247b9d6-1778-35c4-a565-1360e7ef29d0 | -6.81872 | -56.44413 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 341b2ca7-0e94-30d8-b3f8-eda39791ffe2 | -6.86527 | -56.42595 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2ae66c6-5099-3594-96da-f3cda0682501 | -6.86648 | -56.41781 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53702bc6-0ffe-3fbc-a1ea-2f4e3070d7bd | -2.49804 | -56.05745 | 2026-08-16 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1463d76-3a8a-3d99-8a1d-cbf25a9f7b94 | -6.83218 | -56.44203 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05d1da1c-bae5-3ca1-af24-c45401805b1a | -3.74205 | -59.33006 | 2026-08-16 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2719680c-472c-3126-9fa5-4e88713a6395 | -6.82063 | -56.46105 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b289589-5f6d-3ec3-a27b-c838ca9ce108 | -6.82432 | -56.46577 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fd773f2-59b6-358a-ab78-f95347d6eaf7 | -6.82849 | -56.43729 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f12e818-146f-35e9-b603-bfaf18684808 | -6.85482 | -56.43721 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6017f776-a580-3eac-a2f0-c56adafad175 | -6.83457 | -56.42572 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d316f4a0-cdc0-3ccf-8618-f392c755076a | -6.84745 | -56.42768 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44f48e39-e4d5-33f8-8f6f-802c64b02db3 | -6.81443 | -56.44347 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e67a946d-ae3c-3c30-94d3-c13122b1ae3b | 0.48961 | -60.59235 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb773149-c235-3822-9ac6-8a3e565058b7 | -6.58903 | -56.35904 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17fcb7f0-3f30-3e06-b60d-b055fdf1b21b | -6.82182 | -56.45292 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e466212d-d9b3-3d74-8480-46bc7368c1f9 | -7.23953 | -49.87614 | 2026-08-16 05:33:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05cf7b17-f589-3b2a-9873-c4800641da7e | -4.46028 | -61.04708 | 2026-08-16 05:33:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ad9fc2-3249-3163-ae87-ad1a08b3fb08 | -6.85727 | -56.42067 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d7b988d-725a-3399-8d49-c96d060f8f5a | -6.78381 | -55.84595 | 2026-08-16 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a31aa2c7-2c1f-39cc-97af-f0370ee3d367 | -6.86218 | -56.41719 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c60b59e-57ec-3884-ae92-87f623906e6e | -6.81326 | -56.45152 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59c4bb4b-7dfb-3ad3-aa07-292d595df844 | -6.83147 | -56.41688 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c000c26-4037-3f36-8bbd-7615fb82d81e | -6.36416 | -58.31703 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b97491c-951d-3043-8af1-9d1ee1d34f9f | -6.84866 | -56.41946 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7d87b3d-8e67-325b-9910-a887a8f6526d | -3.24373 | -60.12422 | 2026-08-16 05:33:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7de8e2e9-d26c-3ee8-a652-90315ac51eac | -6.81149 | -56.46374 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfac1626-0754-3628-a761-891e1a9ecebb | -6.81385 | -56.44748 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d4a30d0-f7f1-30f7-aa4f-049340fd3449 | 0.49345 | -60.59526 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aecaad90-5637-351f-98aa-525fcc48d103 | -6.85113 | -56.43248 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf764af2-ed4c-3d2e-9782-96076d8dde2b | -6.3748 | -58.32332 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11871168-2af0-373e-a871-a6e22d4f4c8a | -3.14754 | -60.26299 | 2026-08-16 05:33:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c210538-5937-3abd-ad23-f0200faba872 | -6.24598 | -55.61819 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa4680c5-1e07-3c80-92cc-98706727b67a | -6.81636 | -56.46035 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c006ed9-c39c-3d69-8ed5-6eb7a581f773 | -6.37858 | -58.32388 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abb052ee-2dab-303f-8214-4ea376b6abbf | -6.84135 | -56.43929 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b58257d1-4799-3616-8995-aded45a4a1a3 | -6.87765 | -56.50948 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a4b147f-9127-308d-b5d1-af80e97351c7 | -6.77998 | -55.84083 | 2026-08-16 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a673ea5-b11b-3179-879f-02f0f0184aaa | -2.76735 | -48.56983 | 2026-08-16 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 874325d2-16e3-3268-90b5-6b56482b49a0 | -6.82004 | -56.46511 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61ad07f4-7069-326c-905b-242bb52a54ec | -6.63153 | -56.39872 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e49cdc7-62b0-36c6-8ca3-d5107874e944 | -6.37577 | -58.31643 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9371af2d-0ea5-377a-9831-0f8b24716a0b | -6.82717 | -56.41621 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0baf6f1-48dd-34c5-974e-d47496657563 | -6.83098 | -56.45023 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fc9531c-3c87-3e10-aee3-39d0127f1a87 | -6.37442 | -58.32563 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad93e17f-5d47-3462-b02c-f58d8d4b1184 | -6.84805 | -56.42358 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2549d3ac-126f-333b-9710-b389b80e2140 | -6.82669 | -56.44957 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d127c17-f9fc-3729-b15b-98e536ce2556 | -4.9632 | -62.33767 | 2026-08-16 05:33:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ea3853e-623a-3fe5-b364-7a7e677d902c | -5.49745 | -60.14335 | 2026-08-16 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5ede5c-b82d-30a0-89c5-2958e6784261 | -6.8255 | -56.45769 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c3fc69a-61d6-31ab-9ca5-2ea91d9f8a73 | -6.81267 | -56.45558 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08f046e6-41ca-353b-bd1f-64f4aef0bf03 | -6.37509 | -58.32104 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 826db92c-78fd-3f8c-828c-7fbaeaa2c2e8 | -6.37409 | -58.32792 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README48.md)
