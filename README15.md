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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 406fd873-1404-3b7a-93ba-e59c5b8633fa | -7.80934 | -44.02946 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| aff40313-69cc-3a84-8fa4-1e9c4e51b17f | -7.78387 | -44.01914 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c485d8-75dd-390b-8dca-0561dd9106bf | -7.60528 | -45.7509 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eed8cae5-24b1-3e62-87f8-5db5150031eb | -8.35221 | -48.45396 | 2025-07-02 04:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f078dad3-a0ed-35a6-8a2b-b836887f0667 | -7.09271 | -44.38366 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86098fba-c12f-31f0-bde4-1141e5440b2f | -7.80543 | -44.01896 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 78af7ad7-cb96-3b7c-b3b6-f0b707d1e5aa | -8.1965 | -49.67025 | 2025-07-02 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64cbbbcc-6659-3463-a855-eca9535ecb07 | -7.7988 | -44.0279 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c210497-69b8-3cf3-b3db-fa16169719c6 | -7.2886 | -45.37043 | 2025-07-02 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67712d10-b247-3ab1-95c6-71bdd5eebbeb | -7.8202 | -50.64408 | 2025-07-02 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 072f1249-3125-3d3b-a49f-b7fe26e50663 | -7.16267 | -49.51153 | 2025-07-02 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2545d18e-8183-3a6d-b409-f60139c20824 | -7.80999 | -44.01937 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3f79a7ac-e83d-3d61-b004-6353899b9758 | -7.77904 | -44.01515 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83bfdc6b-b3c7-31cf-855d-655ffc78b7b4 | -7.82035 | -44.02775 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e06958-8620-395f-b60a-f22b65e5b067 | -7.03821 | -55.50199 | 2025-07-02 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f82b5f8-36c4-32aa-ab09-48bd35d1c439 | -8.8959 | -48.33345 | 2025-07-02 04:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bd85637-fc8a-381b-9d0d-4f7a36ccbfbd | -7.87983 | -47.89246 | 2025-07-02 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59c4fd00-f29f-3567-b0b8-7c2671233adf | -8.43751 | -49.19958 | 2025-07-02 04:53:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54718e91-460b-3a3a-bec8-b534063bb97b | -7.61131 | -45.74186 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc9d733c-f84c-3f6e-bfba-782b29ca48dc | -8.35541 | -48.45956 | 2025-07-02 04:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76873969-4474-3af1-8b52-d202249752e2 | -8.35147 | -48.459 | 2025-07-02 04:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 356ada20-0708-310a-8c65-0dd9368908bc | -6.53371 | -55.02834 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1fa78ee-0a55-324b-880e-d264bf7bd880 | -7.61597 | -45.74268 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26ddb1e6-44b7-37e0-8724-c5319993ebf4 | -7.80015 | -44.0182 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5b4bfdf8-de52-3c42-9823-cec170fa5eb2 | -7.61928 | -45.75309 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91506d3a-c9af-38f4-a180-c318194bf5c1 | -7.08332 | -49.5957 | 2025-07-02 04:53:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f34b3a5-526a-38fa-b883-8dfd26591066 | -7.80912 | -44.02588 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6a0ca8e9-0804-3667-8092-78fdc365dce1 | -7.60334 | -45.73047 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cc82557-3136-3aa4-be06-a6a3f697ce5e | -8.34752 | -48.45845 | 2025-07-02 04:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9539b16f-cd6c-3f3e-9fb9-45c730742fce | -7.26045 | -46.39923 | 2025-07-02 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57d720c9-4633-33be-8661-55843fc08d0a | -7.78959 | -44.01668 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2be95314-b669-3a8d-867b-d0d5dfacb7ba | -7.79442 | -44.02067 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb2defb3-1e09-3122-a0cd-10fa243cf435 | -7.78914 | -44.01991 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bdacb146-d477-339f-b7ee-673e130f66c1 | -7.81025 | -44.02297 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d42d5c43-836b-3b6a-a1c8-c0009fc3416a | -7.81071 | -44.01973 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1375cf2d-15b0-3456-b3cd-c3ed65e586e3 | -7.60733 | -45.73616 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53ce322a-b0f4-30a7-bee5-29c3771598cf | -7.80955 | -44.02262 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f462b956-9483-3f9f-bacf-5d850dc070ff | -8.24172 | -44.93456 | 2025-07-02 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b86fc4d3-a364-30dc-86b7-17cc04281c2f | -7.81397 | -44.0299 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| cacfc17d-1ffe-3b3c-a05a-323b7018ca92 | -7.28382 | -45.36978 | 2025-07-02 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9947035-f265-30a7-8f3f-b96f8e2faef1 | -7.79397 | -44.0239 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e38a3ef7-7c2e-3a36-95c6-2f6669caf41f | -7.81553 | -44.02374 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2d01a7f5-19c9-3f7a-b759-3b19f6ab416d | -7.7887 | -44.02313 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fd351df-7701-33d2-8b48-d3dd8f9d5e95 | -7.18502 | -45.47851 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 561bf904-4067-3beb-a096-5a20d6f811f9 | -7.80452 | -44.02545 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4fd761e-62eb-306d-8de3-da5cf3cd7350 | -7.81483 | -44.0234 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3767c345-5efa-3b85-b9fd-fd2064fa160a | -7.61268 | -45.73199 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dd34eec-e722-3167-a1ed-35b6f3e8149a | -7.61461 | -45.75236 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27858c89-fdad-3540-bc3b-682bd3e9b7eb | -7.80588 | -44.01572 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 68421377-93fb-3d0c-b746-37edf2451fcb | -7.60994 | -45.75163 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01233888-36d9-3fe3-ad8d-1590aae94903 | -7.8098 | -44.02622 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d370de64-ec5b-390e-b424-9c47df5a2ad6 | -7.31131 | -55.30891 | 2025-07-02 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13147349-e2f1-3037-bcbc-73d028f9bfdc | -7.61062 | -45.74675 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a889984-0439-3f2b-a087-ca9f6220e3be | -7.08759 | -44.38305 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e63580a-55a9-3be4-a771-3a37677a4b7b | -7.08269 | -49.59988 | 2025-07-02 04:53:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99fd03d7-1d21-3282-ab93-54399c603f49 | -7.80407 | -44.02868 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7733841-3561-3c2f-94e1-955b99a96319 | -7.79532 | -44.01419 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41fe6552-aacb-3ce6-bc31-86538ee3e4ad | -7.81507 | -44.02698 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9a8c0d79-7075-3956-8c4c-e8f0fb7ee0c4 | -6.54356 | -55.03388 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c4061ef-2c41-3b87-9189-c0bbb8dfb255 | -7.09227 | -44.38674 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 223ebdae-9d98-3651-b3a3-a99dcd8afa0d | -7.80498 | -44.02221 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| dccdb410-401b-3cdc-afc1-73dc2f6cae19 | -6.71029 | -51.41032 | 2025-07-02 04:53:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 065ed4ab-b82d-3192-a7a8-42cabd72c528 | -7.61665 | -45.7378 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9134c55b-a925-3800-af58-0fc7bf6d7cc6 | -8.31351 | -46.31344 | 2025-07-02 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0951c20a-18fc-32de-8547-9c6727eb5de9 | -6.54419 | -55.03001 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab15e58b-47c0-3716-8ea8-e70341847a26 | -7.31108 | -55.30997 | 2025-07-02 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f08405d0-bbce-3a1a-b2d3-197492e5d424 | -7.61529 | -45.74752 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e14ca625-ad4c-3857-9331-71fcec095ffd | -7.66932 | -44.65802 | 2025-07-02 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d856bd69-2de7-3e62-99e2-0181ddbe24dc | -7.08715 | -44.38616 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b35ca43-255b-3c87-b08a-f89d953a1978 | -7.30845 | -55.30441 | 2025-07-02 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a81fa63-7a6c-350e-8297-126799c79662 | -6.5372 | -55.0289 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d1e50aa-a278-31fb-a0aa-7ecb7937db2c | -15.08008 | -48.9465 | 2025-07-02 04:55:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 684f8f1f-2b82-357e-a826-3bd3bf673bbc | -14.62394 | -49.99068 | 2025-07-02 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 682b709c-b305-3729-8069-711b89bd22ea | -14.89949 | -45.14361 | 2025-07-02 04:55:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e10c782c-404c-38ad-ae46-5cc5b3ceb4be | -16.42241 | -46.55331 | 2025-07-02 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1da37e8-d6f2-35e3-8aef-41715bfed6d9 | -12.63276 | -54.21714 | 2025-07-02 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebaf6724-e06e-3b9f-9199-216f2bef6f4e | -15.92327 | -43.51296 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cc3891c-0b06-327c-95ad-6d2bdfb68162 | -15.41102 | -48.41308 | 2025-07-02 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41aad2c3-e03c-3444-be3f-0883d355d61d | -19.43921 | -48.54892 | 2025-07-02 04:55:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83747818-a8a2-318d-940b-8a4cf2ef70e5 | -16.68332 | -43.88439 | 2025-07-02 04:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 461fa26f-3576-308c-9f20-b993e4a3166f | -14.44346 | -48.86629 | 2025-07-02 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e72e5df5-015a-349f-a4ed-f2050522d1bb | -13.36448 | -46.19212 | 2025-07-02 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1921f04c-26f2-3895-b8dd-2158785b8282 | -19.16081 | -54.83398 | 2025-07-02 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ce11b1c-ae48-34b7-afd5-6d8449f1aa7d | -17.90516 | -54.10908 | 2025-07-02 04:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aff66e7c-43bd-35b3-aae6-ae53aca6aa67 | -16.42245 | -44.5188 | 2025-07-02 04:55:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 301c88f5-bdf3-36c0-b5cf-821773122261 | -15.93884 | -50.06446 | 2025-07-02 04:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e030e9d-afb5-392e-9616-53210362fc47 | -18.65984 | -55.74478 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8cb7a9c1-8ac7-317e-a9b4-57a4461e89c2 | -13.3883 | -47.85365 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be72e0cc-8ffb-32d5-9e34-93060f16bdb7 | -14.90266 | -45.14445 | 2025-07-02 04:55:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 461dd0ad-84b5-3505-a967-1319264838bb | -12.62002 | -54.21142 | 2025-07-02 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc77903-5749-34f0-bfe5-2b9a7378c1a9 | -15.8983 | -43.45868 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e8aeb9a-afb7-37c1-aacd-513d29a7c949 | -15.92401 | -43.51661 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0af7df9b-b26b-3ce1-9221-eabcf6244e0c | -14.44714 | -48.8707 | 2025-07-02 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0221fc9f-cc9a-3879-a3da-294ddd0912e7 | -13.35885 | -46.19698 | 2025-07-02 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c96b66-9bce-37d2-aaf1-dc9f7dfe2872 | -15.0071 | -48.32951 | 2025-07-02 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65a573c-2e26-34a3-924d-a8e8327c4edd | -13.35956 | -46.19135 | 2025-07-02 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135bba5e-31af-3c54-91b1-0d0948859b79 | -15.4154 | -48.41358 | 2025-07-02 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5d11df6-3738-3d61-b087-a8b3de67d5f8 | -14.44765 | -48.86686 | 2025-07-02 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 891aafcf-17b7-3bff-ba3b-7554868b091d | -18.66533 | -55.75324 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6ea109df-3d37-3f1c-a24a-fabf44fa7b03 | -14.38202 | -50.33022 | 2025-07-02 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
