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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af2c9b5e-369a-3441-8cb6-c068082a91a1 | -6.40166 | -56.41313 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea253498-7489-357d-9321-6a7cb1b25a8e | -3.01628 | -53.87983 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67e42c45-fb0f-3363-96e3-2399a9855572 | -3.2235 | -54.31453 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75979c82-f21a-34ef-a893-b0e3a1ef860d | -6.52229 | -55.38925 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72696075-8fc1-3553-bf39-f4ba91b77b88 | -4.26585 | -50.74185 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cab38173-0f1d-30cb-afb5-735961b55428 | -3.29335 | -53.84621 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4a18516a-8583-3b16-8b19-9d1c686bf7fe | -5.30038 | -55.87707 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7bd1596-d618-3cb4-9570-7332497c23e1 | -4.29262 | -50.78419 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2579b4c-479e-3fe2-ad59-37edc064afd0 | -3.0152 | -53.8867 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 600dbd67-a6f6-3c77-99b4-7d7499c5a45d | -3.01904 | -53.88377 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23457825-cadc-342b-a5f8-d71e84489e45 | -7.0307 | -55.63958 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e891a78-f96b-32e3-81dd-b40361575c85 | -6.11138 | -55.6612 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03bca97b-119a-33d5-a41c-dd578e366149 | -3.49242 | -54.72709 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c61bc43-e80f-3344-b14f-b3e9fcfd180c | -4.04668 | -54.23235 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1785da83-e65a-37bc-8f46-719d7eaa94d5 | -4.27402 | -50.78552 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0da56fbb-f22f-3003-9f87-7a3f68dcdc2d | -6.74508 | -46.89466 | 2026-10-02 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1cebe58a-cbbd-3200-a188-9c92d392c458 | -3.18543 | -54.10382 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3ff23ead-4da4-3c2f-a141-20c2c37618bb | -6.3415 | -55.3277 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4df54a85-a8ac-313d-8627-4d902ad56447 | -2.89164 | -54.11031 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cbcf05c-00ac-330e-8ba4-03ee38ce740f | -6.09319 | -47.67386 | 2026-10-02 04:57:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cafd18cd-645c-3951-bc0b-e44635ef450f | -2.89117 | -54.13493 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19e058a7-11e6-3cd5-88b2-5d79d0c97d06 | -6.00459 | -53.54385 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05c1c0eb-b5e8-38ae-b80f-d21e3f02c13b | -4.31844 | -50.78392 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52169d8-1e58-3306-a134-84d594e161ee | -8.16111 | -54.83423 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc2fd6f3-4a51-3ad6-aee8-8495d22b7d3b | -7.40326 | -55.58672 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9abdbfe-3c0b-3944-a56c-ac775cd4b821 | -6.4085 | -56.41422 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5905f54-066d-3b0d-8c87-d1b8ae416cba | -2.92828 | -54.20071 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c81b83-4863-3937-9f24-f19bdef14a6e | -4.26447 | -50.7756 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09261d5a-5e77-3a83-9f5c-02961ba2d597 | -4.94197 | -56.00592 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e1ed195-7f1f-3ce1-89f4-bb07817a3e58 | -6.73665 | -52.95667 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b7e9252-ecc9-38ed-8b2c-4cbd6dc12d2c | -5.11522 | -56.02167 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c19712dd-f4b6-3573-8f9b-8d9393d15f86 | -6.89059 | -55.55589 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ee835b-19e1-3b6d-98c0-e0d438be0955 | -6.3487 | -55.32524 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c4e45fc-fe2f-3f88-b987-929e77db601b | -1.63091 | -55.13633 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd7e392e-4dd5-36f9-939c-8f69b3839e0f | -7.72399 | -54.75786 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3631f3-0397-3f9d-8e25-147540ed048c | -7.46719 | -55.00727 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8baf1859-e32f-3177-b3ca-af48001d9256 | -7.72123 | -54.75389 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dd2a54c-e828-38a5-8d54-088817779dcb | -8.15002 | -54.79703 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fabdef0-f172-393b-ac02-88549f30aa78 | -2.99693 | -54.17611 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70b2c3a-e2f7-37dc-9d55-f720faf38385 | -3.17108 | -54.08374 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a75ed2e-b874-3f2d-bee6-7b0bb0c643bb | -3.02596 | -53.96915 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 136d15e1-93e1-3bd7-92a3-125a85ce7838 | -7.06074 | -55.62255 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b4ce39c-5291-3b8d-9069-ebe5455cab93 | -7.83985 | -55.12775 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8befffc-f223-3c2d-8853-b6eadc6f6cbd | -2.17767 | -56.30907 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8ee604a-b966-3d95-a872-e0188c425599 | -7.86747 | -44.17887 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5448492-5581-31cf-a28c-52428b7227d8 | -7.49962 | -54.99464 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddd6a92c-d4ae-39d3-8df7-103f168e1128 | -3.10818 | -50.29541 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adcd2c65-5b86-339c-9c7b-a9d83aebac1c | -2.8967 | -54.14285 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79263d6a-70ff-3355-9517-38d2ebc149f8 | -8.16982 | -54.80013 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c65574a-7795-3a47-9fbf-c1f5907679e1 | -7.4941 | -54.98668 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eb7e92e-265e-3c59-8ff3-e01a06395a11 | -7.39757 | -55.21312 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3dd2fd71-b4ac-3eef-8fa2-18cbd30a32ba | -8.74777 | -47.58796 | 2026-10-02 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a966fd5a-e67e-3dcc-8565-bd13a2f3f35d | -7.42022 | -55.58641 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4ec250b-c857-331e-8668-f44e548c50dd | -5.86744 | -50.15667 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2d3c3485-fc35-3eb1-ab5f-1d3d776e6fef | -8.16376 | -54.79563 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1291316-4480-3996-8792-8277dc9b904d | -7.88678 | -54.72029 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c70100ff-07aa-37a6-a43a-c747ca1012fa | -4.01887 | -48.94554 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e187bd1-6fe9-35e5-ae49-cf358228f3a9 | -5.00704 | -56.28418 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d3a4d67-15a8-3136-a25d-12952af5df8b | -6.43866 | -55.80858 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb4ec12d-cd88-338d-9c52-2dd4fca84726 | -6.23447 | -53.13342 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b4ee85f-9fa1-369c-9ee5-7e8195c20b89 | -7.41358 | -55.58531 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf5323b1-5250-3e4c-b2c7-c972f826c926 | -6.43923 | -55.805 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621f37d9-d624-3736-9fa6-f7ceeb4dbaf7 | -7.27599 | -55.59546 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7840dbca-4fd5-366e-b8aa-4daccb34beca | -2.60576 | -48.2543 | 2026-10-02 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 712b3d5c-66f8-316b-aa69-8cb29281a26e | -6.14721 | -47.46797 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 414d40d1-067b-3a54-9a24-080ddd42289b | -4.19666 | -54.5775 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbf4224d-0d18-3dda-8e3f-84985fb47541 | -6.91512 | -43.67467 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e25a307f-7c7a-37b0-b9f4-9026fd779255 | -6.1795 | -53.17937 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4262a11a-0a6d-3558-95f8-ef8922f27ab9 | -1.63373 | -55.14051 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1bc3514-a518-379a-9e0e-9248ecb842d7 | -8.15835 | -54.83025 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 484069e6-a1c3-3323-ac56-b9c50b0260cd | -5.98406 | -55.37159 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ba76bd-986f-354d-ab65-1f06c4f85a68 | -7.83049 | -55.12273 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1877739-997f-3fce-854d-2260464e18cb | -1.45248 | -48.91525 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3c0fd0f-2891-360a-a0f2-6e17b03e4683 | -1.18776 | -54.21243 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc5a4a54-ef67-3e57-a9c6-5b456c48f013 | -5.98684 | -55.37563 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009ace3a-6e36-392d-9ede-b6c6b982dcf5 | -6.4353 | -55.80804 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f135088-e3cd-37be-9135-2eb24f68ad85 | -3.88108 | -51.89532 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7febf08-18fc-3a8a-b7f3-26947c54370f | -8.16706 | -54.79615 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd31433f-06e4-3264-945c-25c30c7cd623 | -6.19985 | -52.80894 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95df3107-7fa2-3915-aeca-f07e13af268e | -7.86984 | -54.73817 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62478ee6-8a8a-3e50-96d2-138a27804bfc | -2.84543 | -53.99037 | 2026-10-02 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 479acece-c7cd-3572-afa7-18943dc18953 | -7.71589 | -54.80972 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c77cf3-5d35-394c-b4d3-a9453b5efcf0 | -3.01958 | -53.88034 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73680353-a16f-32d2-a6b6-02d81365db54 | -6.24489 | -43.76979 | 2026-10-02 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 343172e4-9512-3bcb-bfe5-2c19a64b1674 | -6.23892 | -53.12681 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a27c9ff-188c-3371-86b9-d905f65f158e | -7.87933 | -44.17368 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e963b948-5f30-3bce-8741-24dd04729455 | -2.86598 | -54.18755 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7fc3f4a-3130-3c5f-a191-ccb5e2b830dc | -3.14178 | -53.75237 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17cbcf06-c7ef-3f9e-a748-93ea7359064e | -4.30108 | -50.77703 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b69edd6a-78da-3aaa-80cf-113c7c9b8654 | -6.40237 | -55.20105 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc45e2aa-2256-3040-885c-5ef0ae81d65d | -6.39198 | -56.40779 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f35e535e-ffc8-32f9-a50f-4b596428b010 | -7.74997 | -54.80797 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a04646b-0fc0-3948-901d-e7c46b70517a | -5.48445 | -45.86448 | 2026-10-02 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01bcc693-8e9e-33ed-88a0-2179d0562d59 | -7.52705 | -50.53352 | 2026-10-02 04:57:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5d05c39-d9ed-3d69-b688-15b72a03a174 | -4.27948 | -50.77376 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58eaa9fd-34ac-3585-80ab-8061173d1626 | -6.74505 | -46.89654 | 2026-10-02 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1238e38-6bcf-3cc3-a39a-90dcb631f3ab | -7.65715 | -55.09828 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 157d26da-4e9f-3a02-87d9-df3932a52731 | -8.16268 | -54.80256 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edeb57a1-b292-378d-bf2f-f9d2b91db19a | -1.95622 | -52.73297 | 2026-10-02 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd1161de-600f-348f-9650-cd64b5afb781 | -2.99102 | -51.02642 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
