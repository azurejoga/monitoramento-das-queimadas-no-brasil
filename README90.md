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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c516168-1c42-36b1-b1ab-d89eb191ed54 | -4.10657 | -49.12709 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3f8a3b7e-9b22-3841-83a2-eb9c6834e5cc | -7.14564 | -41.11145 | 2024-11-10 04:38:00 | NPP-375D | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3350836f-5be3-34aa-a932-25598897c0d5 | -2.92921 | -49.5097 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e3c6751-d8ee-36a8-bacd-b190428ed40e | -2.29942 | -50.46364 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8c4a41d-200a-34ee-801d-36fe2f05cbe1 | -2.32126 | -51.27827 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f9b7d0-939f-3d96-bac0-87a3103399b3 | -4.12865 | -48.23472 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b696e17f-2723-3802-ad6e-d33021c25e5b | -3.12114 | -53.12104 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c5e2abf-87c5-36b7-9b61-d04fe166c8ef | -2.97663 | -50.49072 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb7af664-1c73-3480-aca0-8231ed347cc1 | -4.76672 | -48.67185 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a48ba94c-a643-33f8-9a51-7162ed83a72c | -3.85167 | -54.22366 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 217a0f19-e769-3b56-9f5c-35c55e92ffd7 | -3.2367 | -50.30478 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 150a8fc8-c71c-3245-9e2c-2d7db403fcce | -3.08716 | -49.5555 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa5483d0-2f4e-32f8-89ca-1880ba69a3da | -3.19464 | -50.30566 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 457be22a-a7a6-359a-a27a-70d820eb6163 | -2.66242 | -49.89307 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6474d8-dd5a-39dc-9e79-c55e21e8cb53 | -3.05799 | -49.71727 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b00499b-b6cd-3174-a42b-ef04ddd0d083 | -2.82027 | -46.64762 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c51da68-a53d-333a-ba0e-391e07cc2ee6 | -3.17211 | -50.60109 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c715f6-860b-3fca-88f9-7337ac26cc28 | -6.28813 | -47.34681 | 2024-11-10 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b603fe-b600-3218-b3a7-8b45fb049ed1 | -3.70283 | -47.64165 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 222d31d9-45ed-3cc9-a164-75d0655843d3 | -2.93813 | -54.07905 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d520939b-c9e6-3720-8540-d54fa937e1ad | -4.57421 | -45.40697 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00b3c24c-32ce-3985-aaa4-1d7be87434af | -4.1186 | -55.04945 | 2024-11-10 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7182d3b-e4ba-39e3-934f-1b73d7d0b68f | -4.24761 | -48.35632 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b14d86-3091-3657-8880-5f1902ab17f2 | -4.10619 | -48.97834 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| aaa3a725-bccb-3957-9a68-47eb3e354bba | -3.04693 | -51.34048 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fd0473e-eb08-3231-a228-105d6211cda6 | -5.30088 | -47.8903 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8918e4d-e3c8-3df3-82c8-9aa0b6a25b6a | -2.40707 | -51.30288 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55daf64f-9a5c-3de4-b0d8-d1472d944f45 | -3.72911 | -50.17682 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5ba1e6c-ff16-3be4-9bfe-d9a5106061db | -4.02134 | -49.91891 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6291fae7-5512-3bcc-931b-863bd9092d06 | -2.9585 | -48.72446 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9fe7e26-0c77-3b16-9e87-44d30a968f5c | -2.46051 | -53.69376 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5e30569-bef8-3564-9eb6-098b61d957a1 | -2.70934 | -49.3349 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad07b3c3-691c-3caf-874e-e8f13f09573c | -2.42402 | -50.51743 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 368e9b36-221d-3358-acc6-c18a89034288 | -3.96153 | -48.17311 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ebf7300a-ef4b-3cbb-b316-f3167b99b54d | -3.22249 | -50.30628 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea1908ea-4b0e-37d4-9d47-6859bfef867a | -2.76731 | -49.39472 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210e3ad5-82cc-3d13-ab94-3a1ef0c80d5e | -2.25556 | -50.41549 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c500bf71-9b05-351b-aee0-18a5f6a7fb86 | -3.95502 | -46.70568 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adba4a4c-9527-3e7c-9f20-d6c9a5788bea | -3.45281 | -47.66793 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30411504-b5a1-3f79-8496-cb4faac0728a | -2.73668 | -51.71668 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6b5b7f7-353b-325b-9070-3f74eb4b5799 | -2.4276 | -50.49492 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 605dc0c2-9fc1-3088-9bc4-c6e2530820b5 | -3.03433 | -50.32576 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb656bdd-4f00-315c-ad49-c905b77f03f8 | -3.07543 | -49.5861 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 663c2b58-a607-367f-98b5-b7b42e0b88b3 | -3.49195 | -49.62616 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd722659-10fa-3d85-afc8-c7fa68184a82 | -8.39745 | -44.10793 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb700bf3-0f00-35a8-a06b-8c1fa2fe8c69 | -2.37886 | -53.8493 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98faad56-6554-3285-a872-458de6e219d7 | -3.22989 | -50.3037 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9e442f5-20ff-38c1-adc3-3b6f98d19a87 | -2.86668 | -49.22073 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61494755-e319-3d2c-9fc7-ada52c028adc | -3.02674 | -53.25478 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c1d60cb-8bb3-3111-8b0a-4a484a0924b6 | -3.13418 | -50.44732 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a78199c5-7726-36e5-a859-40c55b6c2d45 | -5.90627 | -46.71323 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdbe73c8-2780-3d22-9613-696ca1650402 | -2.41901 | -48.85922 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df2cb3af-8193-37b5-8d73-29596f2705e1 | -2.69114 | -49.87226 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 291c7cde-1efc-354c-ae10-5b0d63aa8dd8 | -4.33333 | -48.60769 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dad93dea-03bc-3464-bf1e-c032ba889ba7 | -2.81505 | -51.8102 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 111a90ee-0fcb-3667-bc3a-e8c9d5906ad0 | -4.06162 | -50.01255 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6de28759-d738-39b3-98fc-5d283c15a2d2 | -3.22931 | -50.30735 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50f8cee4-144d-309d-b09f-fa5e22b5bf00 | -2.69411 | -51.70322 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a006843-14a8-333e-826b-2b38e47583b1 | -3.14785 | -45.9542 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b5c31b-fca9-3dcf-a4a1-c6753dfd4162 | -4.05442 | -48.25163 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6bc20f-949b-3acc-b82e-24e101f84ebe | -2.15656 | -50.72602 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5655394-b0d2-3332-82d9-9131ce21b705 | -2.15064 | -50.80807 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d462f20-bd12-31aa-93e8-5de06111566b | -6.24912 | -43.5613 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c6e5e26-a760-3d4b-9089-f7ded4664306 | -2.87476 | -50.40709 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f62d094-dab9-3abe-bd41-7e9beab7c777 | -7.23763 | -48.72863 | 2024-11-10 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6193cf5c-a47c-3bfe-a20b-94f76a9f9945 | -7.43501 | -39.76968 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c368da46-e596-37e1-b900-156ba80a308f | -2.16547 | -50.47046 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34b03f43-4cb7-367b-a172-28aff73a394f | -2.33872 | -49.88763 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 544e69fd-0f7f-3a2a-bcdb-4ae3da1a04f1 | -5.96245 | -45.38292 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a47d96e-86fa-3ab8-b99e-1a1fbe9c362b | -3.05598 | -48.01823 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9365f344-4eec-36ca-8013-e3bd502de36f | -2.58555 | -51.11374 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccdbc4f2-7dd0-3858-8497-8c480cc6396e | -3.20203 | -46.50578 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10052f2-8feb-3fdc-9271-7e0c490ad6b1 | -8.38733 | -44.11837 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 704ea84d-c1b9-3321-803d-47479c624068 | -4.57696 | -46.03602 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f4aa159-2e32-3477-8f05-8126ae464a94 | -2.8437 | -46.655 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ecd138d-2118-3342-b739-4f817b2537cb | -3.62382 | -41.57838 | 2024-11-10 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| af41da39-d44e-32c1-aa08-abcfd953c6d5 | -4.40714 | -48.61214 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53b4f308-ca42-3e3e-b8d7-5652721f5885 | -3.98874 | -46.41472 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45730b80-34e5-3642-b99c-54dafca7df7e | -2.2408 | -50.71848 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afad06ad-63df-37e5-af8f-166e7188bfb5 | -3.96435 | -49.94257 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f122ef6-fd6e-3652-9045-6d50bd2d646d | -4.09606 | -49.12898 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 963bfc8c-0aca-3374-b4d5-f896413f5e1d | -3.73246 | -50.61515 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3863346d-82e1-359c-901c-d1b9d6639a79 | -3.22605 | -50.43848 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37cca9c0-a830-3a86-9fd8-eeb0a141f2a4 | -2.88072 | -51.65756 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6e3648b-84ee-359c-adbb-035197b0c80d | -2.89893 | -46.81334 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49d16e1a-b5e4-36ea-a9ef-b8c5a943ceed | -4.58822 | -45.67518 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b3e69d8-5bf3-3955-9e96-236fd939cc1f | -4.36453 | -48.49562 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ed79135-43a6-3d98-8d9b-4903e4699495 | -4.49521 | -48.46279 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d156242-a02a-3dc8-aa81-01be14aa673a | -4.56745 | -49.59779 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d7dd1ca-1701-3d64-b790-9c097609c5ab | -3.69642 | -54.61691 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469f1e4f-73a1-346f-8a7d-b5b7ff3e74cf | -4.28311 | -48.19461 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c87f30e-187c-3c72-bca9-1004b2d155da | -4.89499 | -48.61029 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea436b04-70d8-355b-8ed5-15f4efdec462 | -3.25002 | -48.74134 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea24b86f-7a3f-33b7-98d0-2ec34ad392f3 | -1.57277 | -54.63551 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3080deb9-dee9-3c8d-9e0e-cd402bdf1f91 | -3.03143 | -51.1002 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e69ee5be-2ccd-35ac-8db1-9bdec44bf22e | -3.95519 | -49.40188 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bff256a3-dd89-3df0-aad8-b487d966ea87 | -2.95433 | -51.06387 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3dea5b-8dea-34b1-8a9e-a8b82937795c | -2.21113 | -50.33973 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1295c0-08a1-37b9-b14e-bec5d49794ce | -4.40768 | -48.60868 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac8b18d-6409-3d07-ba66-6df552f07d6f | -4.40338 | -49.40828 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README91.md)
