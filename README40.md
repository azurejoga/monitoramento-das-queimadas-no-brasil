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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0f0fdbe-4f45-358a-b2ed-7b21d4fb1b22 | -11.70922 | -47.74662 | 2025-08-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2821a55-f9cd-3b2e-a071-47d58936759f | -10.61693 | -50.12623 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16a4f994-b841-3173-a652-d50fe3175e93 | -9.68021 | -48.34506 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e7d4ec7-5311-32ec-b442-ff3f388afcd9 | -10.70872 | -51.58473 | 2025-08-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54b4f2d7-0232-388a-bb18-342824add4cc | -9.2108 | -59.61127 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8f1d5f2-6c55-3640-99d3-d5facaefe569 | -11.51289 | -51.86084 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2b81f36-a172-325b-95f9-09dae9e455a1 | -11.94943 | -43.9236 | 2025-08-24 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd4d5a85-a99b-37fc-8502-28c249fe3fea | -9.16497 | -59.47528 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4e9fb163-b196-30ed-a16a-ac3685b5a01d | -11.52445 | -50.47064 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62edb2a1-2096-37ba-851c-535d21393077 | -6.97717 | -44.43386 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc8f9b71-d04e-3dc2-9f24-2e42cfde17bd | -7.62734 | -45.23816 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b80fcd31-4ee7-3066-9f9a-accd2ac4a68e | -11.17858 | -55.02359 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2998a58b-397a-37d4-bf15-5a47c04ff713 | -8.89299 | -62.4383 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d727f2d-1e58-37cd-aa1b-3d1ed9f1efe9 | -8.18278 | -45.07934 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b90f5591-f164-3ea1-8e81-402fad1a4a18 | -7.53603 | -45.22155 | 2025-08-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c916568f-8f39-30d8-b9c7-584ad871650a | -9.19077 | -59.46027 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ced86fbb-8c17-37d3-a82a-434aa8dd3486 | -8.76476 | -46.75439 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2121a57b-55fc-383a-ba53-8b23d708b8ec | -11.51653 | -51.88213 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e5a46fe-29ff-37c0-bf9d-fc87d62cdbd5 | -10.57729 | -47.14427 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80f5d21d-4f52-3702-b24c-7e6e17f22f14 | -9.9433 | -60.16158 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ceef027-8285-3c78-b17e-dbb3479e8a85 | -10.24969 | -49.09721 | 2025-08-24 04:34:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a9e99b2-4e85-3b27-b7b2-9cbf3f9d7dee | -10.86812 | -50.82922 | 2025-08-24 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d282945b-5dd4-3eb5-a565-b26d3c82b6f2 | -8.70836 | -51.14265 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dbfdea4-fdb1-3f27-9868-4f26581c07e7 | -9.16735 | -59.4625 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a8f6c6e6-136c-304a-9d2c-1af1dc305caf | -9.95789 | -60.18338 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 987d1cd5-1a21-340e-a7eb-25f467f37d9e | -9.14974 | -59.45926 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a2cd0c5-f93c-3bd5-97ef-7e6cab110f6c | -10.75623 | -48.26693 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b08e87e1-9918-3c79-9865-7b32c3f18838 | -13.03319 | -45.22063 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7c75d41-297d-358f-9c52-ce3e0645e178 | -13.44437 | -47.03758 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90d1772d-f2ca-3663-961d-423a6eba959d | -6.89834 | -45.67826 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37f788e8-b80a-36f2-8375-4839bc06ad51 | -11.5164 | -51.86141 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 071962cb-59e2-36c2-b277-8360cae7ab81 | -12.94843 | -46.29316 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d620a5de-c1ca-3fe8-9df4-3a01826be986 | -13.38917 | -47.52562 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbda7fa-992d-3e18-83f5-86da3f696766 | -7.60496 | -46.26511 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aea90ce-be00-3895-85fb-987106e571b9 | -7.02383 | -44.64606 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e18701a-0941-360f-a343-120c908a86dc | -13.43619 | -47.04445 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8bbc479-4d32-303b-8c25-919fa969a058 | -9.14237 | -60.78554 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7132454d-a3fb-3469-a58f-1e08e2c5e198 | -5.74907 | -57.58163 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 301c4b0b-f783-33d8-99e0-dd91216e1df2 | -6.88438 | -45.67619 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 255e7cfe-d8b0-3b0d-acc8-c3884647668b | -9.62149 | -48.32869 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f71e2433-6ec9-3823-aca1-07af18dff15f | -13.50327 | -47.03363 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c7828d-1b98-3de1-b947-0e6cab607258 | -9.1607 | -59.46563 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f94b8dd6-38a2-34c1-807b-32e2d97e22f7 | -7.44598 | -57.61911 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ca50c3f-cb7d-38a0-b702-a674007af8de | -5.79585 | -59.21542 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdabc20a-c724-38e8-8490-e4e40a1e1f48 | -6.9912 | -44.15823 | 2025-08-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cefd031-ea8a-373d-aad6-821d685475f9 | -6.60505 | -48.04528 | 2025-08-24 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b0081c1-a643-38cf-9b80-3430986b7cf7 | -13.39009 | -47.52226 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e51f5221-710c-3a34-8201-19dfb98e35db | -8.7533 | -46.71467 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c5d748c-87aa-3189-9efc-fc95edb429f5 | -13.04785 | -45.22776 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e390f966-76a5-3033-a298-71c245ff469f | -9.13549 | -60.7759 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a57e7ba-689b-321e-ae67-a031957991f2 | -13.05483 | -45.23372 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec3999ab-c215-37cf-b283-46eee449e582 | -9.19647 | -59.62217 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79d4ecff-845a-3400-b279-73150ad2f1dc | -9.2347 | -60.9243 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 70c29b63-1ea6-3492-b80d-7b49e7ed40c0 | -9.52376 | -60.55455 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc9b2ebf-b956-300c-a045-05bcecb9fff1 | -10.40882 | -47.17202 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0cd9538-0ebe-3467-9f88-ae003bcc5118 | -9.17831 | -59.46888 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5fe13327-72f1-337a-b5d8-1625e5b579f6 | -13.62693 | -48.16925 | 2025-08-24 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ac8725-39ac-3887-9231-a8c883bcda53 | -12.20209 | -47.22042 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 611aaec0-2d6e-3280-bcc2-4a45ab56ca70 | -8.71251 | -51.1393 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60251abf-f6ce-3f11-8557-4481ac6f5d76 | -9.22095 | -59.62244 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80f6721-1bd6-3e32-a977-57f0e2d3ecdc | -7.81362 | -46.62228 | 2025-08-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56a1238b-234f-324d-bace-fdf9345dfee6 | -6.89313 | -45.66556 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a19ee903-8fa0-3d20-8f27-451153022ab2 | -8.91408 | -62.44231 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffd8bf25-7521-3bc3-90af-a3fee2a196d3 | -9.25564 | -59.63366 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e28d050-9342-3a89-95ff-25d5d09134ea | -11.14019 | -44.78047 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58071ccd-2a99-3b0c-a2b0-90d0adff7bfc | -10.81301 | -46.38935 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37b132cd-cb80-36fa-8816-59717ab9c63b | -5.42726 | -60.1708 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 722adf80-defa-3f33-be01-0ed0db6865c8 | -13.47696 | -47.04193 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e54886e-ca6d-3d83-960d-5cfe9d87a267 | -8.74159 | -45.47665 | 2025-08-24 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2566dd4c-e9b7-3baf-afb6-1a5137032193 | -9.15562 | -59.46028 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a73b1a39-76f4-3c4f-872b-823b047810e3 | -13.14165 | -44.90355 | 2025-08-24 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 152de3df-482a-34ed-8401-0aa1e609ca5f | -5.42074 | -60.16969 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6f478947-a882-3b4b-be48-1dbb38151c82 | -7.01952 | -44.64986 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16a432d3-f480-3ab3-bb1c-8d0fbb4e9bc4 | -11.59869 | -46.23618 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49cf73f6-8c66-37bc-8eed-00591a9b824b | -13.19152 | -47.20755 | 2025-08-24 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd2d7e6-2250-3ff3-98eb-c98893e54c74 | -13.66751 | -47.98937 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8871b4f-b4c7-34e6-a835-6ed95fc002fd | -7.06744 | -55.59039 | 2025-08-24 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73072d5e-50f1-3dfd-a8b7-bb1ad926fd5d | -11.53714 | -51.91029 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4270270-2856-3a26-9da3-6c136a7a1e3d | -11.52896 | -51.85115 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4e01deeb-fe33-33c5-a48d-154e8e857401 | -7.19307 | -45.1651 | 2025-08-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e63d4137-3c71-33a9-888c-4a52fa7525c8 | -11.53597 | -51.85239 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 1d38dd39-b35b-3133-87b6-56cde6419893 | -5.10252 | -56.97812 | 2025-08-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8149564a-9c35-3d76-8ef9-6fd014d1f397 | -5.87653 | -57.76136 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de37a64-f3e0-3bed-99c8-b84431b6848e | -8.54061 | -48.86897 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49720ee2-1217-3922-8a3b-2f7b666fe6c3 | -9.03377 | -47.64245 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ea62b01-ab64-3790-b99d-67f2c39269fa | -7.59699 | -46.24839 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157268a8-1e7d-312e-84f6-a34205c72849 | -8.19779 | -45.10339 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77117356-3832-3365-ad4c-e6b689cc025f | -13.44842 | -47.03441 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be17e0d2-e7aa-3cdf-888a-1c945882d5c0 | -11.93859 | -46.7284 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5be017f6-8b8e-3109-b98c-21de0acb49c3 | -12.9587 | -46.32448 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 362f170e-cee6-3c2b-9e7d-48472f17dbf3 | -11.31571 | -47.85005 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee9c1ebb-a12d-346a-96d4-76d126dba03f | -11.18349 | -55.02038 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65ffdbd1-b789-3dd5-ae34-2de63d0cc192 | -11.70198 | -60.19164 | 2025-08-24 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb97479-4cc6-306d-ac91-149d2cc89866 | -9.13717 | -60.77848 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa7c6885-9b8b-3b1d-9dae-7bc5fd2d1807 | -13.41775 | -51.78524 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa17f2af-e4f7-326a-925b-a998fae78cda | -5.74333 | -57.58235 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff8c5bfb-783b-349a-acc1-5e6f247f3de6 | -13.37061 | -47.48772 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ff79b9d-b6ec-3879-b359-b99b08f7411a | -6.87634 | -59.8137 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8c6b4d5-3521-35c8-8e31-468e3265f92d | -7.25933 | -43.66965 | 2025-08-24 04:34:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6fb70ed-51eb-3d3d-9caa-c46ad97d5547 | -8.01612 | -45.49224 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README41.md)
