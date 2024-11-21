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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d381f0f-0c53-3ced-b9dc-d0675ff9fed2 | -5.08047 | -47.94194 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 520f2f93-9d24-39f0-8059-315e29980d25 | -4.44598 | -46.53812 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49539afc-b541-3156-b56a-cc4664262457 | -3.00658 | -48.04403 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fb3cf2a-87ae-369f-a18a-886d0a0d50da | -4.69881 | -49.62261 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af944f8c-be90-32c8-af22-9e10a92c81d3 | -2.61112 | -49.25266 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21318e11-a3a4-3d43-9320-1d30e222fa02 | -2.63478 | -48.07084 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3df1f3e-481d-396e-878a-583abecfefe3 | -4.4098 | -42.14982 | 2024-11-21 04:08:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d663f51-ce40-3c0e-b7af-31ca9d221bcb | -5.45137 | -43.23687 | 2024-11-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 573346d5-7bfa-37c9-806f-3233f9db1d68 | -3.41708 | -49.22775 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d429da-6227-34cd-b27b-2be1560969bb | -4.53791 | -46.43484 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c206e5e-2ed3-3856-be1e-1cf9af7232dc | -4.95066 | -46.72049 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f552a7c7-01be-3696-977f-e505cf74f853 | -5.47287 | -46.47069 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43b9157e-a23d-3d99-991d-fbd7fe363bc3 | -4.48786 | -46.71441 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69bbac75-a54b-3afe-a46b-e1b7b605cfaf | -5.94987 | -44.23961 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 855ce3ce-b642-380e-adb2-e10f71424656 | -1.43384 | -46.00711 | 2024-11-21 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a4496cb-8254-3a5b-8aca-66a65bd87edf | -5.62182 | -43.95057 | 2024-11-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec9544cc-b486-3da8-89a0-cee1a38c1ef3 | -2.9472 | -45.19261 | 2024-11-21 04:08:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f66b82b1-fe11-3024-ab81-9bc242ad3576 | -2.68531 | -46.24477 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9248059a-4174-3e63-8aee-a4a26af1d7e3 | -4.68804 | -48.97693 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd18eb10-6ee3-34aa-bdd6-440a9232bd26 | -2.95017 | -48.06955 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f361cdb7-e62f-33ad-86a3-e2537371f644 | -2.83445 | -51.82003 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fc6bd3e-f003-3343-ab2d-9b6072933b8c | -4.6394 | -49.54819 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e0cbe835-bcda-3b61-a6eb-8773126d5466 | -3.33582 | -50.49116 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87175825-1732-3bcc-b0a3-574bbe101c4b | -3.33679 | -51.16319 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 190fafe9-98d9-3fa9-b625-eb5f0c9bc661 | -4.62924 | -45.57002 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7873531c-3e6e-3614-a282-bf4603614bbe | -2.20095 | -53.65633 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 996e333f-c0c8-3e17-81b1-4d277f6fb167 | -4.47865 | -45.65975 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd0f996-ef52-3cfa-a33c-e3dbb008fdea | -2.78939 | -51.72317 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42ae6b28-86bb-331e-97a1-b5da953551e2 | -3.38423 | -52.45464 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54daf511-afa0-3c60-819f-85eaa559912f | -3.60111 | -51.47391 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7957ec0-1b26-3e23-95bf-0f5e3c305708 | -3.4631 | -54.56596 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ea4cdc0-6497-3687-8c94-38f6edab78a1 | -3.48893 | -50.31736 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 417b6d15-f037-3261-af33-38c87d2f540a | -4.24524 | -46.1072 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea98aca9-0b48-3aed-8412-1a4f900fab5c | -3.35425 | -50.18362 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e96c6a-8a2b-311b-9d2c-f0a8f2513ac3 | -3.37729 | -52.45809 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3b75a045-59b6-34a0-95ac-8fd9af7d82ef | -2.7619 | -52.10942 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8242e7c3-ecc9-3af0-aaa0-425d112ecef7 | -3.64021 | -42.06837 | 2024-11-21 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 549337a4-2d69-3ff4-a93b-187223fca26c | -3.57693 | -54.6879 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0d81784-34d4-3f27-9314-b76cce6180ce | -4.29868 | -50.14702 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58682580-8a89-3d53-95f8-69a558f80c32 | -3.54102 | -50.19271 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f5725f-437f-3ba1-a8fc-0cfe7bdc0a65 | -6.90743 | -34.89573 | 2024-11-21 04:08:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3904d37-9047-32b0-9c23-98f5a28b6aba | -4.66291 | -46.53894 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8a4cea5-58df-3521-87ef-e8a9585ea562 | -5.9596 | -45.55366 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa43a2d-b26c-325a-a186-ce02776c2d3b | -0.94231 | -51.72329 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4f833da-e086-31e9-8265-db3c9447f0c4 | -6.81046 | -35.21864 | 2024-11-21 04:08:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 645e35b2-a2fd-3b7a-b5c9-10b8b35a823f | -3.72522 | -47.67235 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61080cc1-0f3d-30ef-9aa0-1e183ab1a6d3 | -3.32792 | -50.25415 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9be3a729-9772-3c90-b8b6-3e34ef7e66ed | -1.46667 | -52.67276 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6cbfb3a-70bd-3a6d-85f6-789efcf6a027 | -6.12134 | -42.51368 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 415d3040-7966-3e89-b6c8-2be155b14fe9 | -2.84868 | -46.67823 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b5b2cd1-a91a-348e-88a1-054e5d75e89c | -3.10992 | -50.20293 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82adabc9-30c5-3523-9626-27a102319f0f | -1.12119 | -53.39582 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a87377a7-7adc-3e9e-b5ff-8733ddf4fc0b | -3.57437 | -50.41833 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6e960822-e33f-3ee1-a7fc-bd1c5f2419c1 | -2.09477 | -46.39895 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203b99c0-708d-33ca-b650-cae91e5e11d3 | -3.12132 | -45.44915 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e524218e-9c03-3077-bf25-9237240ad83a | -4.25516 | -43.80881 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e543da64-03fc-3209-94b7-ec04af371790 | -5.13496 | -45.11339 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07227f0e-56d7-3761-98c4-8b467bfd0059 | -1.14078 | -53.66564 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d3a2ac0-88f7-3e94-bee6-e02b2bb75899 | -3.00791 | -51.30906 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 73dd592a-5175-3377-9dcc-f7e8b064a16e | -2.63064 | -48.48563 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 346e9454-5212-33d9-a802-52156f1605e2 | -2.78344 | -51.72227 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bf9e616-98fb-32d9-93d5-87c59dcc4df2 | -3.08528 | -45.96761 | 2024-11-21 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6be33db-3f42-360e-aee4-f732be47e791 | -2.719 | -46.08979 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2e5be3-92f1-303d-b618-8bb9cd4d4542 | -2.76113 | -52.11406 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fecfb588-230f-3209-94bc-bf2d3952e9a6 | -4.38789 | -47.76123 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5e9b5cf5-de36-37b4-9def-86e74bbade2a | -3.80766 | -51.267 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d69ec0-d6bc-3085-8656-1a7c8ea2dbfe | -1.59409 | -47.49122 | 2024-11-21 04:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a924b7a0-f12e-3f87-a7e5-98b127892fb4 | -4.08059 | -49.28889 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9eca2565-a62d-3edc-8886-ba34e5b931ae | -5.46315 | -46.47969 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e91764-52fa-3abf-bf36-97c2fb613fc3 | -3.30437 | -50.36536 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b29c2b3-bcb6-3c76-94d0-333170d0a029 | -3.06417 | -51.36668 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80659fac-31b5-397f-83b4-788657bcb608 | -6.66425 | -39.23758 | 2024-11-21 04:08:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7a5cd69e-a7a9-359f-9b80-48acbfaf4d76 | -2.66026 | -48.48504 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 42800ce1-a4ee-366e-aaea-f16b69e1a86a | -1.46495 | -52.68326 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbbc5474-d460-34e2-85ed-e22e8d25f182 | -4.22807 | -47.18754 | 2024-11-21 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1fb70ce9-e065-35bc-bb7a-f97dc16ced04 | -4.24467 | -46.11067 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7302aae-196e-3ad1-897d-17fdf6aac444 | -2.00934 | -46.85856 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3a96d4b-1630-3ae8-ba14-a19eeb0dde82 | -4.49366 | -47.93567 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d389d94-de27-3dd1-8921-6a684e0e3076 | -3.00213 | -51.30819 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 36753d65-149c-329b-a740-1060f4b00dd1 | -3.64471 | -50.21698 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78edc32-4604-3a0e-ac09-f6baf6fb4f80 | -3.80166 | -52.22523 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d74c1826-c184-3f27-a006-cdaa2f504a3f | -3.18705 | -54.31971 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17465f7d-9bc6-339c-8961-73e5e853ac62 | -4.25148 | -46.11896 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b91af9cc-4927-3f69-9702-dd4356261afe | -3.84616 | -46.6301 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecb05920-9bb1-39d3-b706-407f3f01522a | -1.19552 | -53.67461 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b05fbe3-8858-3fee-952d-acac7199d698 | -4.7707 | -44.49041 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 789198d3-13f3-3d35-b011-11f8ff4e4a52 | -3.39707 | -50.25526 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3526345c-fff8-3bdc-a4c9-73cd9c5c805c | -4.06528 | -50.90492 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c63ff71-190e-32f0-9502-47fb28ee07ee | -3.2944 | -45.54438 | 2024-11-21 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83ede3e-9897-374b-bcb8-5068113f3ee3 | -1.96909 | -48.38562 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63fa5586-25e0-3398-b95e-147d92f182f7 | -4.72874 | -43.2524 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3355adb7-fd2d-3af9-bfa4-ec63bcbf26b1 | -1.05154 | -51.74499 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1fc438f-567c-3090-98b7-4b308a04b247 | -4.48133 | -44.75275 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e971f7-964f-3a72-bd1f-31c43aa93230 | -2.21444 | -47.99376 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8f2dcc6-3fb0-34ef-b7f1-e3528e7d6456 | -4.24808 | -46.11482 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6f9053e2-56eb-379c-98ef-1ce2c762d8b8 | -3.71772 | -49.42989 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b83c198-f7be-341b-8286-d53247a29614 | -3.01142 | -51.0068 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adc1c150-9a6b-3cc9-9e1e-2a4be0b99b52 | -2.83602 | -46.67621 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14531e7c-3b6f-3fd0-92ed-0db87450c118 | -3.2798 | -53.82537 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ef35dfd-9e8d-3433-ae62-44d090476b24 | -2.24528 | -48.16134 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README13.md)
