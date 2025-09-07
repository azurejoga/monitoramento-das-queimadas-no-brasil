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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b550fb22-a3df-36b9-a1d4-e62bb6b5d0b1 | -6.80994 | -52.81699 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6532bce9-90fb-3a4a-9f11-6b4c922695c0 | -6.27737 | -53.42988 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49b7fc61-3529-3124-a764-c6e55f412873 | -8.35577 | -48.2683 | 2025-09-07 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bbfffa3-3206-3ae9-a6e9-2ed5b18fca22 | -12.87617 | -47.99145 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 225b5db7-2cb3-34e1-91d5-fb18eca3419c | -13.00628 | -45.22057 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b12dadc-9894-3780-aca5-857c86ed20f9 | -8.15805 | -44.86089 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b60c7c3-d834-37ad-98d3-5ab9a66051fd | -6.91594 | -45.19981 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210380af-3813-3593-8f39-a90d38be9f42 | -6.55816 | -42.94799 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80de11a5-ee0a-373d-bf76-461ac1f37314 | -7.99429 | -45.46834 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8605f9df-6e11-372f-a706-3a593b3c4a41 | -8.14812 | -44.85931 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c097012c-9a32-3fde-ba01-fa7ce03562c3 | -8.51186 | -51.3168 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d96ec67-20b5-3cc9-b701-b73e6c56cf0c | -5.94843 | -53.79974 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f0d0fb7-4185-3c1c-93be-c3bcd029b840 | -6.19368 | -45.04218 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cadb80a1-85e1-3b60-9a5b-e3d5e418aa57 | -10.17422 | -46.24331 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5c9f7e5-454c-3d8c-9e98-e737f2310464 | -11.38167 | -50.32399 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b603691e-86eb-355b-b849-001533c01458 | -8.01858 | -45.44368 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8f35383-1040-3bb0-84bb-6d20967fa05b | -6.5933 | -43.99046 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2db5ca4e-2b36-32b8-b445-fc3ff0e96866 | -8.03775 | -44.08895 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 550b8024-b23a-3f38-a8f3-a90fde7f060c | -8.48875 | -45.17683 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90c9b49a-ca79-33cd-85d2-aa21360042ad | -6.19647 | -43.59414 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45787410-f4ef-3ff3-9714-5d29f935fab9 | -6.23612 | -42.58006 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6f4e756-d6f3-35eb-a410-c376ef33c3e1 | -11.77574 | -47.55762 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a5d76a-276e-3569-b505-dee8850e36ac | -6.29653 | -43.32515 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf36f08-13df-3644-9f60-143558064ec5 | -11.14083 | -48.38773 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f8ad56b-0b42-36f1-9cb8-29725800c18b | -6.22528 | -42.60983 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4d240f7a-0118-3895-bf9c-c4a285cee8f9 | -7.97506 | -44.94571 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 426598d2-044f-3997-89fa-3be5fea3442f | -11.09574 | -52.06087 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb25bee7-ab86-3299-9719-88db6fd17e7b | -8.43822 | -47.30448 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f24db1ca-0815-33c9-b854-4b5c852647b8 | -6.06261 | -43.34401 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb226c38-7257-3c28-aaca-0397203fcbcd | -11.02216 | -52.04007 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dcb8b17-3f7c-341f-8f15-ea85599835c1 | -11.56802 | -47.75328 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74f4c7ea-8a10-3005-a41c-f71069f84532 | -6.19157 | -43.3675 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d394482-b2f1-3a8b-be8d-1980860aeee2 | -7.72471 | -50.33695 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 242cc90c-901c-3b33-bbcb-a994a71a3394 | -6.14273 | -43.30494 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cce6a6db-be70-3b0d-ac8e-f4eafb072bb4 | -6.14888 | -44.24884 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f3ffb92-776c-34a7-b68a-6ff4803971e2 | -7.73386 | -50.30829 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b343ad2-5f9a-30e2-87c0-339b2f44f842 | -10.8358 | -55.1 | 2025-09-07 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9faed075-3691-3c62-8a91-f459100437f7 | -11.57731 | -47.73935 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e2eb14f-a92a-3719-beb9-e5d914dc181a | -6.22294 | -43.2989 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f71970ed-dd69-3f71-8084-400c61b471ed | -8.29561 | -47.41143 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7455578e-6139-3e2e-9c73-def8296f3d19 | -11.37739 | -43.5432 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f519ccdd-4449-3cc3-ae3b-13792d1a58cc | -11.40491 | -43.6104 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc5b4d2-783b-3347-b165-4851fec697b1 | -11.58417 | -47.17733 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f832bdf2-258d-3d63-a542-31e5d12031ae | -11.31722 | -46.55201 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a1bd343-3a32-37f9-a818-9768d518fb6e | -6.59216 | -43.97597 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad553971-1409-3321-8519-04fc25d3e1c0 | -10.06308 | -48.06738 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea6d0db-ff74-3d79-af19-7c64f384d769 | -12.89566 | -48.00294 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51bbf6da-9f0b-3921-a4ac-0634c107dd19 | -8.68208 | -45.30767 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 830c8fff-089c-30c7-ab50-d75adb05ff5e | -6.60725 | -48.05578 | 2025-09-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21cbb767-32a2-39ab-9df4-e88bc42e19bc | -7.67978 | -47.3293 | 2025-09-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fde34f11-4361-3678-af2b-47b941f6d41b | -6.21563 | -43.32359 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70d681ef-c025-3d8a-a8de-1e741c58b12a | -11.31779 | -46.54848 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8293b4cc-5927-395a-b6df-005152faf305 | -12.62173 | -44.61395 | 2025-09-07 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac6e6059-e532-359b-975b-6c8dbcc261b1 | -6.38557 | -42.99772 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8f0020c-89bc-3ad8-a150-46f4f9212893 | -7.75381 | -50.74633 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dd7e993-dd40-3281-a293-12db6d64af8f | -12.00921 | -47.77987 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02dbf2f2-59ea-3645-8251-eb5240f750af | -10.75538 | -47.7439 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf2d376-435f-32b0-8f7b-d20866c660bc | -6.18513 | -42.6419 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e3d425e9-f6c3-3e1b-8adf-a6c8cd75979c | -7.75448 | -48.81733 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9787e1bc-e8a2-3f0c-9cf8-4279b6b0b14e | -11.40785 | -43.63837 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a6395de-9b52-342b-8d6f-c63be1086cb5 | -6.07795 | -43.55379 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c58c7f1-5f8c-3fe6-a5a9-b684b3aa759e | -11.39298 | -43.55749 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29eebbdb-5a55-32a5-84e6-e1da9644dc20 | -6.19357 | -53.26021 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cc03269-1194-34cd-845d-1284231afda8 | -7.75 | -48.82117 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 15de7413-6e34-35b9-a419-94f93b4104ab | -12.57446 | -44.62906 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 571f8abf-3175-3934-b015-625b68143a01 | -13.04394 | -47.09703 | 2025-09-07 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6af32c-a1e7-340b-8319-42793665cb82 | -11.1442 | -48.36736 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcbb9519-812f-35bf-a916-2c616ed96f30 | -6.17606 | -44.31339 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a94d93c-dc41-34f7-89c3-0c12b78e5f66 | -6.20315 | -43.59521 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3514666e-4395-3194-9c3b-50c9f1c39906 | -6.81112 | -50.8567 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 657499ca-8a91-3e06-a500-a7e459b84640 | -11.37045 | -43.54214 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a969617-a68d-3895-a037-1d830818bc2c | -11.04865 | -54.17255 | 2025-09-07 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 37f8ef06-a40f-3f6e-9c82-9036ca3b8e63 | -6.72671 | -50.45836 | 2025-09-07 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff4b41d-e71c-345d-9c7c-1d2da0d40bb2 | -11.60231 | -47.16136 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 704a5e8d-1579-3ae3-918d-09edd4e450f4 | -9.81728 | -46.83231 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c495992-7d7a-35d3-bb66-329a46506932 | -6.83228 | -46.39752 | 2025-09-07 04:19:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f090515-78dd-398d-98ef-645dce1b268e | -10.8066 | -47.73278 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54833fa3-ff2c-333e-bc63-a72bb62fa847 | -8.44825 | -45.02443 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 730574c9-c964-30cc-82db-c2348ffde73d | -6.13454 | -44.25369 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e429850f-0100-34f0-a963-11f90fd2ae1c | -13.47755 | -43.50651 | 2025-09-07 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d39ac88-36ac-38e6-846d-6a120b4f5d21 | -8.11471 | -49.25772 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cadaa2e6-cb70-38b2-89cb-f4d636607254 | -12.83225 | -48.00325 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc642d6e-62fd-3d64-99bf-85aa964d542a | -10.05609 | -48.06617 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7da4b88b-f1df-399d-8891-7071adbf20ec | -7.60515 | -44.6632 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05605695-9875-344a-bcd6-c240272bd62c | -9.97703 | -51.66141 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93a41118-effc-3d20-80b3-1ad5ed3407f4 | -5.85396 | -45.29818 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11dcfcb1-fc7f-3e42-8ce3-7d09762b4868 | -6.2763 | -53.43607 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 526558c1-9fc0-338f-8c75-2294be1c43d7 | -11.6029 | -47.15774 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f940fd4-79e6-31da-8a2e-f74ec2d0b5f1 | -6.15087 | -43.18471 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7178eb2e-507a-309a-a029-196c8aa6fece | -6.20233 | -53.27065 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c28b2c62-84e4-3b0e-a769-572bac744f4f | -9.06706 | -50.44954 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2520b997-7a4a-346f-a780-706ced6ee4b3 | -6.16609 | -43.19812 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b865375-12ea-31f0-ac5b-611f9adb5f15 | -11.81146 | -48.2357 | 2025-09-07 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42a13016-c7fc-310a-b1f8-6047be54bbaa | -8.33932 | -48.27842 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a522bb48-98b4-3637-a007-074d58e4fc40 | -6.27274 | -53.42582 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca4de66d-61e7-3eb3-8edd-fbd4a5552bcd | -5.48141 | -45.91369 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f887138-ccea-3424-9601-8ee9e113df3f | -12.46532 | -48.03693 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331c2d4f-7df6-3964-be03-73424584507d | -8.62794 | -54.65263 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df6e8695-4448-36ef-9be1-513df05743b7 | -5.69425 | -49.19749 | 2025-09-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b73283f-c6a2-3df8-b726-22c68d1b5abb | -6.43762 | -43.61646 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
