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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b1adeb3-17dc-3b5d-854d-344817a78702 | -8.3181 | -44.15779 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9bb1a7e-392d-359d-81fb-ee9dbfae259e | -8.31701 | -44.10048 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0bbcf7e-36a7-3289-8152-4cfbe8fa6054 | -8.31479 | -44.15728 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43d7f5ec-c7ce-39e3-ad67-de909b31c091 | -8.31039 | -44.09945 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a7dfcf9-0f22-3fc8-8408-8b73bd7d6475 | -8.2988 | -44.10834 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1286063c-f14a-3072-bb74-cf4601fc6201 | -8.29825 | -44.11182 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77efa022-d56a-3326-9b2c-30b3a6c10c97 | -8.29107 | -44.13568 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70d5af86-8458-3d8c-81d0-6c17062aa0e0 | -8.29052 | -44.13916 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ad9d75-0492-3650-8230-5660a5423648 | -8.27127 | -44.08959 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d89cec-edfa-3151-a30d-e63349eec08d | -8.21222 | -44.39589 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b953d73e-38db-37b8-8529-6ede1af569b4 | -8.13023 | -44.41871 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd2d97c1-d4cd-3b54-9813-59991047898a | -8.1269 | -44.41818 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4517349f-105c-3e4d-8e19-1eb5a3e63759 | -8.12634 | -44.42171 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f3d4990-03bc-3428-96fb-cc3fd3de4d87 | -8.12577 | -44.42523 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78bdbdc8-f76f-3921-8e04-dd898d593deb | -8.12301 | -44.42118 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06e6227d-9ae0-354c-847b-f3c65472e675 | -8.12245 | -44.42471 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fad7436-a172-3228-98cf-d3d4f74e304a | -8.00542 | -44.36919 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ebc3684-77fa-3777-8aa5-5c96286104df | -8.00485 | -44.37271 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bbab591-f81f-3927-b507-6ee39730a3aa | -8.00429 | -44.37623 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cedeecf9-2729-3968-8e03-bb75de5bd1e6 | -8.00378 | -44.35813 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6d9b477-fb4e-339e-99d3-e806e89192a9 | -8.00373 | -44.37975 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb7dde9a-b28b-3a3f-b13c-753a7874ccb8 | -8.00322 | -44.36164 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6adb9ca0-30a5-3753-9c41-ec5047f0f0bf | -8.00316 | -44.38327 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 470d97e4-dc57-345a-80e7-9500241b4341 | -8.00209 | -44.36867 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7efe44-2e32-3375-84ed-99da0a2a838c | -8.54132 | -45.4646 | 2024-10-09 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fcaf92a-56ca-30f6-b9c2-e58d80ba8854 | -3.56051 | -45.21695 | 2024-10-09 04:14:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34e02137-2f66-384e-9fe5-fc64973ab9a5 | -3.11 | -45.89586 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7041070f-63a7-3d43-9e24-02eb90c68c09 | -5.0126 | -45.82432 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a6cbade-1559-3127-8032-0316c11898f4 | -4.96651 | -45.61394 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 343552c5-e661-3f76-a57a-ae4e4d01337a | -4.96645 | -45.61362 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 665349ef-81c3-30fd-b5a9-173bcb40e823 | -4.96588 | -45.61792 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d78b686-a562-3e5d-b255-5785637b8606 | -4.9658 | -45.61759 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7409e4df-df60-3d15-9443-40aa0c0d3e0b | -4.95995 | -45.51852 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44229bf7-23ef-38ea-91a7-62b090515143 | -4.93203 | -45.67044 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30363d90-2b76-32a5-938d-ec0c237d18f0 | -4.93138 | -45.67447 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73087f80-ef03-32a2-8dd0-a428c3ae957b | -4.92783 | -45.67389 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c0efa86-d48f-3654-ac7c-ace6b48624d8 | -4.85292 | -45.41712 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73b3c9fa-93f9-366b-b1c6-a9f94ed4bf19 | -4.80689 | -45.3454 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6ffa35f-d0fe-3a8f-8e4e-2f11152ffb66 | -4.78721 | -45.25901 | 2024-10-09 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b8c3c0f-452d-3394-8230-8c20091bf7eb | -4.76123 | -45.76009 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a450e0f-3ea8-3faa-8d32-0e5ee8ae5ed8 | -4.73878 | -45.67336 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c07db65-08c1-37f8-9893-877c564f4dbc | -4.73634 | -45.66994 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 139d345c-bb5f-3333-b274-49ef782c8e67 | -4.73571 | -45.67393 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1dfda75b-6262-3cbf-8f58-d171481c4770 | -4.70816 | -45.64064 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce4bd569-db77-3f72-b257-ffe017e0621f | -4.68997 | -45.86898 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 98d00e0e-3615-32bb-96d4-1a893c43bfc3 | -4.68931 | -45.87307 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1135a4a0-4b90-3a56-acdd-bde08f052c05 | -4.68866 | -45.8772 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f995bdf-cf88-3999-8b92-7a7984408f2c | -4.68653 | -45.82131 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dcbf4bb-4c76-3495-8400-eaedbfcecec9 | -4.68571 | -45.87251 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 924d7291-5d6e-3d91-a4f5-7b9b7776e62e | -4.68505 | -45.87663 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba236fc3-51fa-3a3f-bdc0-39380957a6c9 | -4.68293 | -45.82079 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cded5e03-793b-37b8-a841-a5b2f2898a45 | -4.6821 | -45.87204 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a511cb31-df01-3374-a070-38abbf2fb752 | -4.67848 | -45.87154 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d730b5-2d86-3478-98ed-34873ca52276 | -4.6218 | -45.61462 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 463faf1b-dbde-3ee9-ab2c-751498c0a10b | -4.61406 | -45.61743 | 2024-10-09 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 427ec667-11d7-388a-894b-43f3d942b09b | -4.60344 | -46.08321 | 2024-10-09 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 203edd52-8dec-38f0-a876-97d588de5240 | -4.46618 | -45.90775 | 2024-10-09 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e79e0f1e-a88e-3e03-a3ff-d2547f38a542 | -4.46254 | -45.90727 | 2024-10-09 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81de9613-ce01-3259-950f-0024ff5e635d | -4.87463 | -44.81976 | 2024-10-09 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad561871-3739-3be0-99a4-e25b2c4c6174 | -3.99401 | -46.06935 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40a3f6f2-3202-3cf4-8285-7f9cf6f9e6e1 | -3.9903 | -45.34297 | 2024-10-09 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d73b01f0-623f-3627-b41f-e89b0fa9f26c | -3.98676 | -45.34241 | 2024-10-09 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af8124d3-3606-3959-a6fc-5b73d01a0cc5 | -3.91992 | -45.3288 | 2024-10-09 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a62c4d48-b940-3f1b-b95f-f0e28eef53e3 | -3.91638 | -45.32825 | 2024-10-09 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39c75e7e-0fb3-3235-a007-a879e39bcc88 | -3.75143 | -44.94925 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61c0909c-81b7-3102-acf5-ec2ab5f0795b | -3.7103 | -45.11833 | 2024-10-09 04:14:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9cedd7-8e0c-3827-ba0c-f2a96eabc25d | -5.58331 | -46.31304 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39d7ae6b-c441-38cd-8eaf-2a45bef7ae22 | -5.5013 | -45.38102 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46b7ec75-c01f-3ae2-bff2-e498959c3a9f | -5.49843 | -45.37667 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56ffad89-025b-38b1-9019-95291f5a4c30 | -5.4978 | -45.38054 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3025c87f-f900-3d1b-a18c-8d60f8f976a4 | -5.47992 | -45.51377 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 83f14490-6529-32fa-ab9a-ff3a670081c0 | -5.47929 | -45.51771 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef0e238a-3cb9-3ef3-8957-66386db2e2ce | -5.45441 | -45.49355 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 636c7838-7433-36fa-b040-1f4c57532402 | -5.45378 | -45.49746 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14eee70d-b206-3a0d-856b-d6bd2709df35 | -5.44485 | -45.88988 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c651681c-2f50-364d-96d6-26b671b49d7e | -5.43352 | -46.00645 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b15b4a7b-457f-385f-a7bd-63f4258cd077 | -5.32414 | -46.38342 | 2024-10-09 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85113fa7-0c81-3323-b8cb-7b0a94035ef0 | -5.32345 | -46.38765 | 2024-10-09 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57041a19-e83a-3c08-a9a6-896e0c752748 | -5.32024 | -45.42038 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7e9f2fc-d398-3bed-a4ce-20b852cb856a | -5.31962 | -45.42426 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e21686bc-9d38-304b-9fe9-62f86135a616 | -5.31943 | -45.4764 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfac54a8-05cf-35fe-bedd-42e4751e9a16 | -5.31879 | -45.4803 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ede0cea-6efe-3385-9e3b-61807fe4a514 | -5.31855 | -45.47624 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9904cdec-c3ed-3c36-b6f9-31515da957aa | -5.31815 | -45.48421 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ca1b98-da0f-3dfe-8b3d-4082361a81f9 | -5.31793 | -45.48015 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d43a417c-6fc7-318a-943c-7f1b912841a4 | -5.31731 | -45.48406 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f706199-a9cd-3dcc-bee9-10213aa1d907 | -5.28436 | -45.44265 | 2024-10-09 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b32eb46f-9716-35b7-b6a1-de268a06ce0d | -5.28374 | -45.44656 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fbe00e5-c456-3427-8a0b-9fad77e8a492 | -5.28024 | -45.44595 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99e7e054-dfe2-3470-bf72-8650d9365bdf | -5.26484 | -46.14754 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c5e1c9f-4346-3902-8573-4fe091ddc4de | -5.26121 | -46.14694 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b05a62d2-d16e-3ec5-bc5a-07cd5e37b4ea | -5.22722 | -45.14125 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3b8be20-6f7c-32af-b498-7400900bb756 | -5.18066 | -46.01846 | 2024-10-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dab78227-7b9a-3ea4-b220-8a763c130940 | -6.37208 | -45.87797 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d48e1f40-e853-3e31-b013-a27cfa16838c | -6.34581 | -46.33186 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3fa30fb-942d-3550-b20a-5ef58587a630 | -6.32778 | -45.72526 | 2024-10-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 266d4115-5534-36c5-8fd6-dadbb55c78fb | -6.22184 | -45.09509 | 2024-10-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fa5cb1d-cfbe-38dc-aeac-64ed7b2f0ef8 | -6.08483 | -46.48323 | 2024-10-09 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c728588-3422-3b3b-87ce-0619eaf1c58f | -5.93855 | -45.39314 | 2024-10-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e95acd6-1a26-3abe-ac56-479a46d52c9b | -5.84702 | -46.23494 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README76.md)
