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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d008da92-1b9c-333a-9d85-3c71924f0aad | -4.27587 | -50.77324 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0f1b73-2078-307b-b9f9-c5757a14a597 | -7.46276 | -54.9924 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a1abfa7-628f-3507-a3b2-ddf041b33570 | -3.17116 | -54.10488 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5690da5c-c398-3439-bf2f-5b9326862f4f | -7.83215 | -55.13366 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc625c9-7417-37fc-902b-1601792d2e9f | -6.34209 | -43.36395 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6bcaf33-f958-3e39-81d2-975a8ee75704 | -4.29748 | -50.77647 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35caac07-88b6-3338-ad97-f4264a073299 | -3.04045 | -53.87653 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d7f3785-22f8-30cf-be3c-85e7cfcca20f | -3.14615 | -53.74602 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1405e640-1d26-3acf-b3a5-dd40061d6969 | -7.69706 | -54.75718 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef4f50d9-617c-3c8d-bb5e-0064d72d7b7d | -6.40818 | -56.41742 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85512fa1-6e66-3cee-9351-7599426d65f1 | -6.24565 | -53.14975 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4f55f56-571a-3dc6-ba8a-b1a6999f7fb0 | -3.11314 | -50.28745 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66326919-3ecd-35c8-8694-e52c52d707a3 | -4.28543 | -50.7831 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e9ed594-1fa2-3511-8868-ecd8d76e362c | -3.29389 | -53.84277 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d2462257-34af-3211-a4db-73eb766df887 | -4.19997 | -54.57802 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10299130-50e7-3bd7-8cbc-064b03302007 | -4.25378 | -50.74854 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea971cce-e748-3db8-bc0a-e2c1d3629041 | -3.14891 | -53.74995 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5158136-2e5c-32ef-9696-04e1f7268772 | -3.57408 | -54.61831 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dce2d9a4-2ffa-3a17-8f3a-c3246dd9671a | -7.05796 | -55.61848 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8363f0b1-5bcc-358c-8434-5fe21b79e3b3 | -4.2801 | -50.76961 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 201cb213-770d-324b-a7d7-0746e833716a | -4.42942 | -54.84935 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee4fc4dc-d61e-3a67-98ea-63d36d246383 | -7.1948 | -52.61328 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07ea3af5-db6e-3ef4-b6d6-0467f7696313 | -7.03707 | -50.73042 | 2026-10-02 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e260b2de-c5e3-38f1-a652-263595f7f3f4 | -3.16501 | -54.07928 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4ec8b0c6-d930-3e31-8f69-82eb9b18d79d | -6.10404 | -55.68568 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b4e07e9-1704-38bf-a472-3e57ee59614f | -4.24659 | -50.74734 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52f1ea1a-4df2-3bf2-a5d2-27a824217774 | -6.72247 | -44.27691 | 2026-10-02 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32035d5c-679e-39c8-a608-1811ecbd4dbc | -7.46059 | -55.00624 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7f79c2d-318f-3f03-b528-c78730eb37a3 | -6.74799 | -55.0812 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36b4440c-1983-34f7-947f-aeb238ed1898 | -4.03954 | -54.23476 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc2de5f2-89ab-3de6-ae70-1e176bf7496d | -6.71676 | -44.27601 | 2026-10-02 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8fab9c98-ba91-369c-9b4e-3e155fba9baa | -6.85589 | -59.04266 | 2026-10-02 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77797f17-569a-3585-b9a3-e8937b8663c9 | -7.49578 | -54.99759 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a459ae10-29df-3c3a-b024-73200af20077 | -6.15242 | -47.46397 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f8b29c3b-8add-3656-9872-d4c7183ed7ca | -7.73239 | -54.8123 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ad63931-c626-3e35-bf0a-70e1549f28ea | -7.73785 | -54.79899 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50f2e9fa-eb3a-325d-be56-e7ce89f9d99c | -3.14393 | -53.73865 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc71c5ce-d510-3c3f-918a-c258492a54a4 | -3.92806 | -55.75708 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60bde548-bb50-340a-9570-07736bd46cc2 | -6.76123 | -55.08327 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dcd959c-1d9b-32a9-a013-b658dd852ee0 | -4.27839 | -50.75652 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7cd6fb-e4de-3509-b3d0-5f945cf748e3 | -2.05386 | -56.86717 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0cec64eb-d832-3e93-8058-6cb6337f8fa4 | -9.52902 | -45.33315 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a8a754f-88fc-386a-ad3a-7cc6145fe754 | -6.1931 | -52.80798 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6c1fd73-9e7f-3983-ba39-93a912b08d6f | -5.89972 | -53.49556 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 68b04fad-cbac-3fa7-a532-a81e0fc616f9 | -1.48469 | -55.87098 | 2026-10-02 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d98818e8-7b62-38f5-ba16-6a2f3b268539 | -8.09033 | -54.87626 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1e3b8e2-f155-3542-b6a1-62f68564393a | -6.39079 | -56.41524 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca4fcf9d-3a67-3393-89fb-1c5f12c75266 | -2.90055 | -54.13991 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0675b99-7cab-3db1-b934-17eb540830c9 | -6.14869 | -52.80497 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a40d542-8d19-3d43-89b5-e30e8ce644ae | -6.43749 | -55.62195 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23a73205-ea98-3820-a919-464e6d71b411 | -4.039 | -54.2382 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 192e4dea-9566-35ab-8349-ef40cbbc41f3 | -3.15511 | -54.07776 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d1fe8ec-2fb4-3b55-a9b9-f890aad49da2 | -6.40567 | -56.40993 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4b36500-4d67-30b8-a7f7-6b143b2afc44 | -6.07834 | -53.30799 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2193c94-f2f2-3168-ac12-28ae6a53b847 | -3.11446 | -50.27897 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 19c851f4-34cf-38d1-98f8-58d1927ef3f8 | -2.89562 | -54.14973 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25b27f92-0a90-3e34-985c-c0a56c0b821f | -5.85427 | -53.48148 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e6a73e-701f-34e2-9b47-0d082a05515a | -3.10462 | -48.67582 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb23d2c2-9f08-3d77-868b-baa1fc9be7cf | -6.40449 | -56.41743 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 461d689f-d917-34f5-a48d-37801dcc0d86 | -9.52788 | -45.34084 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c85c34d-695c-3928-bbda-10a033f2463f | -2.98088 | -54.14891 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9170e674-6a21-3be9-b7de-0444adbea600 | -7.83103 | -55.11926 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26cc9ae-9305-38ee-9be7-e9a25621c2ec | -7.86767 | -44.17178 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7e7b2ad-7b27-31ca-9c73-ef59e220a376 | -4.28183 | -50.78255 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a1fe9dc-0a46-3f45-9674-c7a88796ea62 | -3.15787 | -54.08171 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db6ae3ed-4cf1-3566-a5a4-c5f4c2604593 | -4.68482 | -55.79205 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d3b941c-0073-356c-8004-4748e88eff6f | -4.30341 | -50.7859 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb733f02-0fd9-3e1d-a1fc-e991b514dc1a | -5.87477 | -53.50257 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ba2e9f0-224e-3eeb-a33e-b0ef630a5fa6 | -8.10528 | -55.34484 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 273806ff-7a8b-3cd3-81a3-4c1f327918bb | -4.17514 | -56.34394 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 289cdcaf-7d16-3e0e-ac31-d89d987de809 | -7.72303 | -54.80729 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceda93bb-1cb6-3162-bd69-8dfd6c645b05 | -8.25713 | -54.74363 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fccfcb6-f4a7-314e-90ce-56878b18af7f | -3.16885 | -54.07635 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b94f5a7-9e0f-3e8f-8811-ba7baa4ce083 | -7.83491 | -55.13765 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 224be089-9346-3a6e-881b-f9a3dfe6da5c | -6.19475 | -55.54663 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4fabd3a-947f-3d32-8e8c-bb02fa21f75c | -2.90385 | -54.14042 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e550a2bc-3c24-37a5-bc11-bd6e40572b9e | -7.57032 | -55.13078 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27c7dbce-4dfb-30a2-b349-230d2f9a1828 | -6.44083 | -55.62248 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d7c2009-0c55-3d8d-9c1f-2f8fe865b6c8 | -6.90563 | -43.70047 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f77283-f275-3c4a-ab35-7ac9d6c1f3d0 | -6.40791 | -56.41798 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ba2175f-7f78-3791-9a37-681b79bd47d2 | -4.30171 | -50.77287 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63b7fa44-a454-3580-99bf-53c0716f9425 | -7.74797 | -49.20122 | 2026-10-02 04:57:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a99ac787-5ba0-3579-90ca-9f7191645dac | -4.29451 | -50.77177 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d988a66d-6c62-3cdb-8367-7be9271a5adf | -6.89302 | -52.49985 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f86986e-fd1f-35bd-9112-d07cdb408e92 | -2.46094 | -56.08032 | 2026-10-02 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5085e0e1-4fe4-3e59-bff2-b6122f73fd1a | -1.26502 | -54.56348 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bde397fb-778d-3049-b9c1-6f10bfbc4b5c | -7.27987 | -55.59247 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc1d042e-7b05-31ee-ae4b-73f598fd76e5 | -4.28088 | -50.73997 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8b8709c-fc11-3586-8025-7ea459e030da | -6.40343 | -56.40192 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444449e0-595a-3419-9177-7431ddf3b9b6 | -8.1775 | -54.79424 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf4d0ce2-466e-3451-a222-ffe3087d66ea | -5.83014 | -53.52765 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0668b5f3-562e-3d81-9dfb-b547a06ed6b4 | -5.26877 | -56.04922 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9feee770-954a-30e3-8688-7f751456510c | -3.17884 | -54.09903 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33f4f33e-f7db-3981-925d-0c8b80b737cd | -7.74499 | -54.79657 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4bda4fb-410a-3c61-9839-27dc2fd9c5d5 | -3.29889 | -57.85575 | 2026-10-02 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d5d200f-2343-32ea-a666-4a5ee5e81ba1 | -7.39535 | -55.20568 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 2b8b92ce-3efa-3120-8f80-3a5f17697cce | -3.00205 | -54.22987 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc477e00-926d-3018-b644-a320de84576f | -6.3183 | -54.78233 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4ef479e-18ba-3f0d-a73e-ae3b481e6ed4 | -2.49755 | -56.83566 | 2026-10-02 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3751c4b-96c1-393e-b531-9df5ba4dd5e7 | -5.86752 | -53.48367 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
