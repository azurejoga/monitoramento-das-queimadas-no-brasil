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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1374972-46eb-39a4-84da-994db5ce0275 | -13.60681 | -48.09675 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3ee7a6ab-3946-3b86-aa1c-21419db0d890 | -11.4422 | -45.00301 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88e0660d-a9b2-3e77-90fb-b01eaf7c897a | -12.68502 | -46.88279 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43201197-1dfa-33bc-9d7e-c6e95e0be820 | -10.91017 | -45.73607 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea17eac7-db43-3fe0-8b15-456da47feed5 | -9.97818 | -46.63532 | 2025-09-28 03:38:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d9910db-7794-3ab2-8ab9-09512bbd2af1 | -11.04899 | -45.87934 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9592d3d4-8bf6-3672-b0b2-c68ea4ba2d7f | -9.43648 | -43.7014 | 2025-09-28 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f95a4ec-ba01-34da-8d78-80b17e16ebc9 | -15.52929 | -42.33782 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f7f85b81-cb9a-3fd5-bb5e-4dcad051f24c | -11.71429 | -44.42632 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5feb1488-2240-3291-97b3-cc7f4199fcb6 | -11.94953 | -47.93461 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3769599f-519e-3c49-90e6-74e106b1f1fc | -14.20616 | -44.60061 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 863c2e72-89f9-3f6f-9312-2578e9171ef8 | -11.36969 | -45.01684 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78427a10-6dee-33d0-9be7-14e7bcb13228 | -11.44438 | -44.99175 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da3e0921-fe97-38d5-a6df-2e4e5ef9661f | -11.42331 | -44.92133 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9a4aa57-ac18-35fe-86ca-d520077fc4e1 | -11.44137 | -44.97734 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3264493-bf81-353c-bed2-06f5801b48d8 | -9.21679 | -46.7735 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7ad480fb-ac70-3090-819d-de6c4d80d14e | -11.36815 | -45.02459 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e902e229-ee9b-38de-90d3-d05d689d0978 | -9.12198 | -46.67437 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| add62349-147e-3f95-a2f3-4773e59bf8ac | -11.9982 | -47.89886 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d2b989f-f0c9-3038-aa48-5710b7eac52f | -11.41433 | -44.90814 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07812c89-a053-3008-9b18-e687e3fbab1e | -9.44176 | -43.70264 | 2025-09-28 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b27f9553-7de2-3466-84c6-c55318692eb0 | -15.21625 | -48.06588 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec60e774-5bc6-34d5-a786-cfc6b4d25090 | -9.87541 | -45.93829 | 2025-09-28 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66768ead-3a11-31f6-b492-c9db064bd23f | -14.72759 | -46.83418 | 2025-09-28 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60198f86-8033-3ce7-9c83-2eede57ad748 | -11.70423 | -44.42077 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d04331a8-1c46-3685-ad4f-c530e25ca396 | -12.26079 | -44.10072 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 484e1ec1-1eca-3c6a-b835-019d892fabd1 | -11.9921 | -47.03774 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebc4d5e3-7ae0-3cca-9352-179e9a5fe406 | -9.45238 | -43.70492 | 2025-09-28 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6e044ea5-663b-3da1-ab4e-064c637acc8f | -12.00669 | -47.09474 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01eada92-9f82-3650-907e-a22c169e3447 | -12.67863 | -46.88269 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 95ace649-bcd0-34bb-8a7f-7b1b4af032e7 | -14.78699 | -45.63781 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b64ad94-056b-3739-98ea-ab1283062dc2 | -15.62043 | -46.2575 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b732fa-3d47-3e60-863d-cdde0c570aa0 | -11.9773 | -47.07801 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc76b471-75b8-388c-ac2b-8e7030c617d0 | -12.97687 | -46.85501 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd517b73-6c6f-3e9b-a197-33c2d7557add | -15.28285 | -46.45676 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d754a85-9c5c-39fe-99e8-13e09444c638 | -15.44166 | -48.23837 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fea0663-750e-310b-9c18-cb4a5d95c1ee | -11.70228 | -44.41691 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f257e390-0242-3379-bd28-ed2deb6d6e5d | -13.59147 | -47.33097 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecdb6be0-0f1e-3b90-88e1-effa17a7a975 | -12.41619 | -44.1086 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 865ef97e-945b-39da-84ab-f1fc99cadc2f | -12.92437 | -45.18193 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65419e4b-de71-3332-92f8-0038056aed70 | -13.39663 | -48.1657 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e500af9d-bed2-3e9d-9c39-46b720da3df8 | -15.21402 | -48.06367 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ba827fb-658e-3708-9f48-009a786c7884 | -12.69714 | -45.47229 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17016c5c-326b-34cc-9568-691b25754273 | -10.90386 | -45.75442 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bcf5dc71-8758-3fd2-9c69-a45ea4631bcf | -13.59005 | -47.30655 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfb57316-3841-3b7a-b04b-45dd028b5b55 | -11.99395 | -47.88593 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| be4695ce-2abf-3eee-b170-8a90855acf60 | -13.79821 | -47.92973 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75396c5a-a7fb-3e2e-8e2d-06e1eb66a9c4 | -15.03075 | -46.96889 | 2025-09-28 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d576af57-55db-389f-b563-22e778f14db8 | -15.32239 | -47.89701 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79ad4d2a-371e-322c-8948-cdcd7daa75df | -12.69639 | -45.4762 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3cb7fe85-fcb4-3def-a1b2-cc5775e5bacd | -15.87806 | -46.23206 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a7b016f-125c-3d72-8204-03054b85dc4f | -13.4032 | -48.16694 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d00b82d-b3e1-3903-8d06-3faa63a68254 | -15.08991 | -48.33263 | 2025-09-28 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3688364f-58ec-34a4-b2ae-57514e423b03 | -11.44776 | -45.00431 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23b198d3-798c-39ab-bd5b-dcc908dada15 | -13.58731 | -47.31981 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a89f4f4-ea78-39aa-9876-ad33e96d19c1 | -11.38582 | -44.96471 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74b9ecb0-64a2-3329-93b0-be002f008190 | -13.59876 | -47.29577 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94a03dd5-e41f-3401-b572-4825d73a3f53 | -13.3978 | -48.16016 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02448d1b-b47a-3e59-8f07-75780393597f | -11.99838 | -47.039 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b032c6-70f4-3537-988d-d77901265c00 | -11.41031 | -44.90621 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7372e9f-522b-3471-b91d-e6443350ce74 | -11.38143 | -44.93658 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c2a8615-b289-3242-a166-3e813f649bd9 | -13.60273 | -47.32918 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f95a457-fddd-3bb0-a2da-b54f00067365 | -11.97497 | -46.5911 | 2025-09-28 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f33e3c6-61b5-35d0-a90a-2b48c211582d | -15.54166 | -47.91661 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c7ce35e-65a9-32ee-96b3-96b68553b124 | -12.00062 | -47.88692 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1fe0625-c03c-3ea7-aa14-d29324fbc92c | -12.26204 | -44.09422 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35f00869-816a-3608-bb85-69c1013f1e39 | -13.6064 | -47.2901 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af10ac87-1965-34c3-b7d9-add22add3eed | -15.53365 | -42.33874 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 89cffdb5-0441-3c0a-bb11-06fbd540b41e | -12.69267 | -45.47891 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9a118962-a017-3959-903d-e7b3048f446b | -10.91769 | -45.72889 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 523e5b86-6b5f-3aad-a9b1-5d32382cdbde | -15.97501 | -42.01063 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8dc87a57-5129-39c9-8c4a-e7d2b9908f89 | -10.28557 | -45.20552 | 2025-09-28 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cc22ce1-6bec-37a9-bf56-2167089aef93 | -9.10721 | -45.87864 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5b8c59f-6a7f-38b7-9c2c-8dc075acb29d | -11.71566 | -44.41935 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bbd892cb-84a9-36a9-90c5-3dea15eedf9f | -15.21161 | -48.07506 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41bb6441-634a-362c-a8da-46c956361bf2 | -11.40935 | -44.90406 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77dba75f-d1b7-3c7c-a4f9-32ad9ba8320c | -11.44074 | -44.98057 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0572277-8c5e-3f39-a516-148a5da2e333 | -13.7763 | -47.87037 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| beb7c5cc-981d-379b-a155-b4094fb109c9 | -14.59171 | -48.25996 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f840d1fa-32d9-3f7a-881f-03aa9f2bd0dc | -15.53779 | -47.91349 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 87f58d83-066a-379e-af48-109f94aebdfc | -13.80153 | -47.91442 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da3de474-d61e-3ba7-bd3c-0fd4c03f00e6 | -13.31666 | -47.31176 | 2025-09-28 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bb17ac3-5ddd-305a-a074-cf3d8f222c64 | -11.95077 | -47.92858 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0fbbb373-06ba-3ba2-bb60-bbddb938b6b4 | -11.44991 | -44.99315 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d05120a-2692-3e1b-a076-334b089eac0e | -13.63373 | -48.06584 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0e78ef4-2953-34a8-bb64-c313014ea9b1 | -11.43783 | -44.96566 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e8998a9-8d2b-3571-abdb-9e5febb1df57 | -9.7781 | -47.76325 | 2025-09-28 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f0ee004-41ba-35fc-86ac-7dfdb1885a44 | -13.77051 | -47.86623 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 906cf1af-7721-3510-a7d6-7885d7b6838b | -13.78084 | -47.88048 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 78c42605-7622-3f6d-89d5-c3f036db168c | -9.07133 | -45.53426 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05dfc4d-e7d5-3f30-a092-508cd6db650d | -11.36892 | -45.02073 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21fac0cb-6b39-3b9e-b235-b4790c5bfae3 | -9.1062 | -45.88388 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd273169-0da7-3b69-b2be-a878ad5a2dfb | -11.99945 | -47.89267 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bac8572e-53ae-36d5-a904-a019d11b6fb0 | -12.27957 | -44.08714 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 772d708d-952a-3996-a6ec-b7e7883a09e6 | -13.63844 | -44.41724 | 2025-09-28 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6a9e56d2-ef91-3906-afda-2080151d03a7 | -12.00462 | -47.88888 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dfa0019-180e-33d5-b66c-46155e95622e | -12.95294 | -45.15299 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc4b0053-98b3-3f1c-bdf0-27570ce4ac55 | -11.9853 | -46.60302 | 2025-09-28 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 545e933c-c514-3502-8fcb-30aaccc8295e | -12.97789 | -46.8501 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 351c7c15-5e8a-346f-ab91-24ea0f02f3a1 | -12.99453 | -49.43377 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README18.md)
