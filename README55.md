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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3a31a7a-be44-3ed0-ad18-6f88b6c609b3 | -4.27776 | -50.76072 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a934f363-53c5-37ca-ab12-6ebe09a4e4f5 | -6.7412 | -44.13688 | 2026-10-02 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e07e2a7-2788-39c3-9ae9-d1a3dca123fe | -7.72729 | -54.75838 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cfbabd9-b565-3098-b57b-5e4a35bf85df | -3.27529 | -54.00501 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19cbf862-a3d6-38bc-beda-ec3cb5411544 | -7.39426 | -55.2126 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f294d86-dae7-3f20-871e-13cd1630c1e3 | -7.51017 | -55.03959 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1db359d-ea28-37e6-86d6-69cdb7dbeccf | -7.04738 | -55.6422 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c46fb1cf-2a0d-3c93-8e89-b7cf3d3b0641 | -3.02266 | -53.96864 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5d57a420-7305-35bc-a63c-8dcda276fad7 | -7.03961 | -55.62648 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddeb1f6b-7b22-3a7d-af2f-af5ab412fad0 | -7.48863 | -55.0 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f0da7ea9-c2c4-38ae-a782-f04fe30c9f3f | -2.53901 | -54.01266 | 2026-10-02 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8e07b7-3b22-3e0c-934d-6108f7d766d6 | -2.8735 | -54.11809 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85b873da-eed8-3f23-8a30-8ae60443e59e | -6.39422 | -56.41579 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c16dab91-b52a-3081-9167-9458a2d1c61e | -6.70171 | -56.14288 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e2652a2-235a-3727-8a8f-e136253576d5 | -3.03492 | -53.86865 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd0c9ea8-e487-3a0f-8398-d957af3d76b8 | -7.49464 | -54.98322 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f76ede-f3fa-323c-bf0b-320b4ecbb000 | -7.59391 | -55.08826 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d4b415d-53c3-3c67-8ab8-58d5c195ecd2 | -7.4974 | -54.9872 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da3c1bc3-1513-3fec-8a84-4092d99fad9f | -8.16214 | -54.80602 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26183bb9-7663-39cd-b615-69131025b75b | -3.0119 | -53.88619 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaf08191-be81-3d04-a546-2cf0c6d989eb | -7.82994 | -55.12619 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 588b2e99-46e7-3683-a264-cae38698b773 | -4.08491 | -49.49369 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f327b9-bab9-3e6e-a6ea-4b75ceae88d8 | -6.38689 | -55.23441 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c7122b4-fc2f-3091-9f63-cfab45fb585f | -6.66278 | -55.08191 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55d71f91-1525-3dec-a340-06310c25bcdb | -7.55583 | -55.02898 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a375f5-0100-39dd-8740-0f9bc7c131ca | -5.73803 | -53.61618 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b5eda9-40c9-3269-b7a6-b66ab07c7b7e | -4.06569 | -51.10896 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d582e5a-f8e2-30fb-854d-828e9c9f2c06 | -4.2544 | -50.74439 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1af0278-05fb-3082-a483-3c24405fc2d3 | -6.34031 | -43.37704 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa124a41-4445-3f66-bc37-d785922a715c | -5.97405 | -55.37008 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65b48346-1ca3-391c-bb68-dd0cb9c606c1 | -7.56313 | -47.20869 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54800972-1103-32f9-b34e-ba06acb39998 | -8.02866 | -47.47933 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a17ea6b-047d-3cd9-9de1-49a21d168035 | -7.78373 | -55.6337 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84679d3f-f82f-3e7d-a3c2-f23ac8f477b9 | -7.74613 | -54.81091 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39317d5e-773e-307f-9f92-a3a76f46f7a3 | -3.61843 | -51.79936 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eab14e14-d964-3276-b821-92986ec9f205 | -7.68224 | -54.76548 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2e388b5-477b-3e90-bf76-acd9eef1b1c1 | -6.87711 | -55.64059 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77990860-5124-3286-abda-1d5c7a2d3825 | -8.15781 | -54.83371 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 018544f5-afd7-30b3-bb1a-e1827cadb388 | -8.24974 | -54.66094 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 798d7222-8df9-361b-b2d1-aef9b4f4d708 | -7.82058 | -55.12117 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8477d278-bf46-3f45-8792-79b8fcec8c48 | -5.97961 | -55.37811 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2beccc5-4425-3757-989a-1a2f9a76147d | -7.73839 | -54.79553 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a70947e3-ef6d-31fa-90d2-a8db6ba0f2f4 | -6.11125 | -55.70512 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 374af405-3ef7-309d-8e2b-3bae3b3631f9 | -7.03014 | -55.6431 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1742ab06-75b4-3346-a3af-e543d216e48f | -3.14232 | -53.74894 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d94e1a5-125f-35fa-9b76-b4b0c227ac02 | -3.12666 | -50.2747 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a1171f-f92e-3aab-89e7-c221acfb5d62 | -7.86664 | -44.17987 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 257f7d1a-3355-3e5d-9a8a-e56c8e1b6447 | -4.42609 | -54.84884 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ebae77-f1e7-3242-9ce4-fbcffcf2b5a0 | -4.27104 | -50.78086 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3b1cf3f-c7e2-3df8-9f0c-06019bc36fa8 | -6.34704 | -55.33577 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86dacd2e-78a3-32d0-b923-df5ed66a9a26 | -5.9874 | -55.3721 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70afc4df-049c-3e3a-ac23-301d8df859b5 | -8.07935 | -54.88162 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57293c98-25af-3ac5-b2f8-865fb54dbc4d | -7.19138 | -52.61277 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 022dcbbb-7b9c-3969-8ae4-62171d70c5d9 | -7.56737 | -55.02013 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d925066-bcd5-36f3-9821-a3d0824cfd87 | -1.86394 | -54.88689 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce976ff-79b7-3957-9cf1-9944b6c5d4bc | -7.72627 | -54.78655 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22bc3626-27ea-3e3f-b6de-c4fd4fa9242d | -7.73455 | -54.79847 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2499de6d-23f9-31ad-8280-840507ee733a | -3.10453 | -50.29487 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2768b83f-39dd-3c58-bb09-73b9fdfef7ae | -6.9206 | -44.56276 | 2026-10-02 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c82ae023-3715-3aa0-a42c-f8495b9830da | -6.71899 | -45.56868 | 2026-10-02 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6b24535-00db-3bb1-993f-3cf90d290461 | -2.26625 | -54.79944 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ab7e3b5-2ca4-3086-8798-cf03fe3772fd | -3.11509 | -50.27723 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6622440-05d8-3d86-aa22-cca821d0813e | -4.30155 | -54.79713 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9123d0c-94b8-3491-b437-83c3898f8b26 | -4.301 | -54.80061 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5904631f-75af-35f3-800b-74e0bad59095 | -7.32897 | -54.93583 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ccb8322-306b-3ba2-8b31-64b46d2d785b | -6.19061 | -53.17379 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eebf900-ac62-39e2-a211-487aa1963aec | -7.51446 | -47.33963 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 389743de-b1f4-30f2-9b77-ce3cea236ed0 | -3.07832 | -54.37341 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52705625-b112-3037-8663-9be0b7fb5d8e | -6.66223 | -55.08539 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 566beee2-b812-3ae0-9982-cf1a7b41434d | -5.29651 | -55.8728 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b956697f-4047-3379-9da8-b796e0cd6838 | -3.17545 | -54.07738 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c53c09bf-0eb7-3230-9124-1359254fad3e | -7.48972 | -54.99308 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 108d5850-b714-31f5-aea6-b6954f42d08a | -7.72027 | -54.80332 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54a01cc3-8db8-3d2c-b923-b39c6c3c599a | -7.34103 | -55.22554 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e03043-3d10-3a09-9b32-a42158083449 | -8.20482 | -54.71064 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2e49f8-5467-381e-b9ec-527deeab5174 | -3.29282 | -53.84964 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4928ce6b-f254-38c9-bdd1-bbf10930004b | -6.40106 | -56.41688 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 74f43c5d-7b4b-3625-8ef6-ca33b9c97de3 | -2.93651 | -54.19138 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35e5f80b-df84-3b6d-a8c1-36e9aeadf391 | -6.24341 | -53.14208 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f033f71-6b7f-3552-8b35-d57693fe459f | -8.9807 | -48.93795 | 2026-10-02 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af24bffa-e5d7-37fc-9af3-edcf7b863bb9 | -5.87253 | -53.49515 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 693f9aea-8f88-3e3e-b968-12b3feef3a40 | -1.26893 | -54.56046 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b1a2052-c8aa-310f-9702-9395e8bf8965 | -7.32411 | -54.98829 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec5bbc2b-2ef2-35a8-a303-6f450597d487 | -1.63547 | -55.12953 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef15c18-4968-34ab-ad81-163cac05f67f | -5.9835 | -55.37511 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce22899f-c9e3-31f8-88e3-666b40719772 | -6.33608 | -43.36297 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89ff3bb7-3d45-3868-944c-f0174c6639ab | -7.04794 | -55.63866 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd7e8e9b-0671-362d-9bbf-a04f58292860 | -5.85374 | -53.48493 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ea1df3-e7fb-3043-b0ee-62f665d4e144 | -3.72641 | -52.39611 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71d53959-957d-330d-a369-a3009ca271e2 | -6.40284 | -56.40565 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffe49205-c271-30fb-b058-326c720fbfaa | -7.87742 | -54.71528 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a025cdf9-5ddc-3401-b3cb-8f25350a785d | -6.34754 | -43.36909 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72f8a66c-1699-3953-8bbb-2e237957ddd6 | -6.51897 | -55.38873 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58855dc7-7346-3d8e-a043-9b4e4fe13e2c | -6.02348 | -55.33809 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 452b7dd3-e544-32e1-80b4-cedc8c24fd1f | -5.6982 | -47.16498 | 2026-10-02 04:57:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2d7284b-b22c-35c7-b438-d982ec06f2ee | -7.1997 | -46.54816 | 2026-10-02 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4aa4299-8fc2-358c-88b1-563caa66aad6 | -8.24314 | -54.65991 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9087c30-c5d5-3ba0-a2cb-d1915e039981 | -5.26921 | -56.0491 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6db8a92e-4ef7-389e-8d24-71acc9e25dcf | -7.55032 | -55.02101 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d3c7f3-8ef2-31a3-a3c2-6eb8fa6cb9ea | -8.17036 | -54.79667 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
