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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64f7410a-be52-3d8f-a249-09f9901305c6 | -5.0624 | -48.446098 | 2024-10-11 00:46:26 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485cb22b-f89f-3c3d-879b-b44fec5633ad | -5.679 | -51.2897 | 2024-10-11 00:46:27 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13345f1d-d4b4-3023-b307-fb98d76dc4aa | -5.6805 | -51.296501 | 2024-10-11 00:46:27 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 293ec908-e46a-30a2-a5b6-b948e0db5da6 | -5.6187 | -51.159302 | 2024-10-11 00:46:27 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c91c1291-bcf9-3da0-a4b3-7dc807e6cb5d | -5.5378 | -50.983101 | 2024-10-11 00:46:28 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5deec3db-0b66-3b91-b152-7d47545d8818 | -4.8216 | -48.206799 | 2024-10-11 00:46:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610f759c-a872-3567-8ace-e6acabee51a2 | -4.8236 | -48.215199 | 2024-10-11 00:46:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb439544-b1ae-3a6f-a65f-1ba7fa655aab | -5.4685 | -51.041901 | 2024-10-11 00:46:29 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a60cdb2f-15ff-3cfb-927d-f3105c111ff6 | -6.5651 | -56.010502 | 2024-10-11 00:46:29 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa52a8d8-0c1b-31e7-8c24-43655e99f8eb | -4.8725 | -48.472401 | 2024-10-11 00:46:30 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c9a63f-03b8-3860-b6b2-f0c2fdb8f727 | -4.8744 | -48.480499 | 2024-10-11 00:46:30 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb63eae4-c98e-3138-8fd3-ea877df0398e | -6.5531 | -56.002201 | 2024-10-11 00:46:30 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02d64d44-04b4-3ee1-ae0b-5afe703274c4 | -6.5553 | -56.0126 | 2024-10-11 00:46:30 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40de6533-7c90-38ad-adf4-a0f8181bd4b7 | -3.7976 | -44.047501 | 2024-10-11 00:46:30 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5377e8b7-e6ac-36f9-b3f9-de8271fe6df9 | -3.8013 | -44.063202 | 2024-10-11 00:46:30 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8684913a-c2e7-33a4-bccd-c0d18eb72fa3 | -3.7879 | -44.049801 | 2024-10-11 00:46:30 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8f7472a-9999-3c96-a62a-034a7b81fc42 | -5.9186 | -53.425301 | 2024-10-11 00:46:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f22d9f9-87e5-32a1-b45b-1c47e277a6aa | -5.3421 | -50.9837 | 2024-10-11 00:46:31 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013d6dc2-1d40-3f22-b967-a786d9a14acf | -5.3436 | -50.990601 | 2024-10-11 00:46:31 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d588915c-7009-352e-880f-7cbe38875da6 | -5.3065 | -50.962898 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb54c18-40fc-3d76-9da3-17922187a375 | -4.8337 | -48.9314 | 2024-10-11 00:46:32 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25922b0f-c46d-3620-ae35-2253aca842c1 | -7.1013 | -59.261501 | 2024-10-11 00:46:32 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1288d653-0fc8-33c6-9aa4-b221228f7ee2 | -4.0023 | -45.3946 | 2024-10-11 00:46:32 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 536c8234-d994-3e63-94bc-d45f2e7bfdbd | -5.2822 | -50.946602 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d335d470-2ce3-3e2f-9347-62c086c0c789 | -5.2838 | -50.953499 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc9309a-4ed6-3af6-916a-23fdc4a8dc5a | -5.29 | -50.9809 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebc76e36-3bd7-3b83-88d4-2ff3914369fc | -5.2802 | -50.983101 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 214232c8-47c4-37df-87b5-db6b6526f990 | -5.2817 | -50.990002 | 2024-10-11 00:46:32 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22eb119b-6b09-38e1-aacc-9939be6a397d | -7.0845 | -59.375801 | 2024-10-11 00:46:33 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c91ce8c2-4168-3408-8de2-df5b7a90ee6c | -7.0747 | -59.3778 | 2024-10-11 00:46:33 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 685ff72a-9676-3071-90b5-377bfbc2e90a | -7.065 | -59.379799 | 2024-10-11 00:46:33 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dce5715d-8759-3b62-93de-026a9db5b58c | -4.9497 | -49.754002 | 2024-10-11 00:46:33 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1caf4024-9e08-3fc5-aa80-96ad3b134661 | -4.9513 | -49.7612 | 2024-10-11 00:46:33 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6471c55-8e21-374c-9f3e-3952abbca853 | -4.2069 | -46.8867 | 2024-10-11 00:46:34 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89d1e7d0-1839-34c6-9f04-793071936535 | -4.2092 | -46.896801 | 2024-10-11 00:46:34 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce232d4-7087-3c99-b8d3-4390ef977ea0 | -4.4773 | -48.098801 | 2024-10-11 00:46:35 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20821015-08db-36ce-8869-7279534b7551 | -4.4793 | -48.1073 | 2024-10-11 00:46:35 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8630666-10f3-32e0-80eb-0e4b67fc3fdb | -4.8812 | -49.9058 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3eed2c-6803-3db1-935d-219691f3e09a | -4.8829 | -49.912998 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea06b111-55b9-3aa4-a1c6-74fe453815de | -4.9887 | -50.424099 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1577ba80-c5e4-30e1-8009-1c423b53a013 | -4.9903 | -50.431099 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b985c7c-eda4-34ac-b160-70a5e24865fc | -4.8436 | -49.876499 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05ec30bd-97cc-3b5e-9c01-004572b106a4 | -4.8453 | -49.883701 | 2024-10-11 00:46:35 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f20ce345-71ec-3934-9430-333749dc1328 | -3.8065 | -45.480099 | 2024-10-11 00:46:36 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02ce3d5d-626a-3c5e-a3b4-12b91872c856 | -3.8094 | -45.492599 | 2024-10-11 00:46:36 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e78fdef2-eb41-3255-9780-dc61aab2b5a6 | -4.3137 | -47.702801 | 2024-10-11 00:46:36 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe906038-1128-30fe-9a7d-49481c36fcac | -3.6118 | -44.7822 | 2024-10-11 00:46:36 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7732a5b-25f5-3de1-85b1-e97467e61921 | -3.5987 | -44.770302 | 2024-10-11 00:46:36 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08e71847-419c-33e9-88ce-06e76e31867c | -3.602 | -44.7845 | 2024-10-11 00:46:36 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc98fd4d-3d11-305d-83e3-900e9efb0edb | -3.6053 | -44.7985 | 2024-10-11 00:46:36 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edc631cb-133c-327a-a9c4-2a2eff1ec8c0 | -6.7728 | -59.292599 | 2024-10-11 00:46:37 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd838437-aebb-3079-a699-f43519a176c3 | -6.7631 | -59.294601 | 2024-10-11 00:46:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91b0535b-0514-3a0a-a47b-7f7a04ebf707 | -6.7533 | -59.2966 | 2024-10-11 00:46:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9ffcd19-dce9-3f46-af65-05501d24033f | -6.757 | -59.314098 | 2024-10-11 00:46:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e776fe69-4e3d-3722-b14f-5b798d679f7e | -6.7436 | -59.298599 | 2024-10-11 00:46:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4f8f0d1-013f-3601-808d-24bdbc6b73ce | -6.7473 | -59.316101 | 2024-10-11 00:46:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca191b3-ea11-37bc-bce0-f8499608d4b6 | -4.3787 | -48.610401 | 2024-10-11 00:46:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2e4de3-8568-3892-971f-7e00a1ea5156 | -4.3805 | -48.6185 | 2024-10-11 00:46:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93be9120-7d62-35a5-90a8-eea74c362cad | -4.832 | -50.641899 | 2024-10-11 00:46:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9803f26e-3814-32af-8221-ebb9f3b41e15 | -3.3688 | -44.360199 | 2024-10-11 00:46:38 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54a5b052-9ae9-31de-adc8-dd1d77dd76b8 | -3.359 | -44.362499 | 2024-10-11 00:46:39 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05434fa9-c7f2-354c-9f68-e5e5e6d3f13c | -3.3626 | -44.377701 | 2024-10-11 00:46:39 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc0e1e2f-42a4-3b87-8710-d1ab2fd1377a | -4.8323 | -50.7799 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ed8bb9-985d-3796-beea-ce036cf26854 | -4.8339 | -50.7868 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61713d68-97c4-3924-9d4a-629b9eb3a48a | -4.8354 | -50.793701 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ac057f-f24a-3c34-be62-41d8f3f759b2 | -4.8241 | -50.789001 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1570640e-b6e0-35e7-9503-7ad19f47d64e | -4.2051 | -48.125 | 2024-10-11 00:46:39 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12faf5b2-eaac-3b55-a746-2321130f4b53 | -4.8408 | -50.908199 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed0be89-cae5-308e-9737-48fe8cdabb26 | -4.8423 | -50.915001 | 2024-10-11 00:46:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d09f6fd9-3f8d-3618-9560-490589993cc4 | -4.3101 | -48.625999 | 2024-10-11 00:46:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 457ccc8e-13e6-391c-9a5b-819534e1e120 | -4.312 | -48.634102 | 2024-10-11 00:46:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf61d680-c486-3759-93c9-abf58886aa64 | -4.2868 | -48.6143 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8b58ce0-a2a4-3907-8c3b-f10f4ed01d3c | -4.2887 | -48.622398 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df425671-5054-33f7-a0ad-1a9d1c91417b | -4.2905 | -48.630501 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3e1009c-e5a7-30a9-81ad-5da1e24aec58 | -4.2789 | -48.624599 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb6952aa-b960-37c8-8a7c-57713a3f87ec | -4.2513 | -48.6394 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c14b5a12-d001-327d-aa58-c1fe96e973db | -4.2532 | -48.647499 | 2024-10-11 00:46:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d4a9d80-bbe8-3f2f-a1cf-ad5a65759cd9 | -4.5856 | -50.418999 | 2024-10-11 00:46:41 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c23aee35-0677-3dea-bced-6f08deb4c6cc | -5.8079 | -55.7295 | 2024-10-11 00:46:41 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec88c516-ca9d-3abd-b983-ecd665b460f9 | -5.81 | -55.7393 | 2024-10-11 00:46:41 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7827453f-4b54-3ba6-878f-b9181506eb27 | -4.1172 | -48.234699 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe24a22-27d7-34d9-9be7-a4e45b7c7fcc | -4.1191 | -48.243198 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df18c764-19bf-3718-8c3f-78c4cef49f8e | -5.7981 | -55.731602 | 2024-10-11 00:46:41 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ffef9f-5f1f-3cef-85e2-5d569a9914ef | -4.1054 | -48.228401 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c30ff0e4-eede-3716-b635-102e8ec421a6 | -4.1074 | -48.2369 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25038d6a-0b36-3761-aeb3-c00ba13ebb95 | -4.1093 | -48.245399 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c31a70f-7ee1-354d-aa83-e2e51c937768 | -4.1113 | -48.253899 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42312279-7461-307a-84df-25f0d4749158 | -4.0956 | -48.230701 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447397e9-e27f-3aa1-89cb-d68c7b2898b0 | -4.0976 | -48.239201 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d14f6ef-3fd4-31d0-9455-e32fb0b60378 | -4.0995 | -48.2477 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84704d4f-43d7-38d8-9816-47254c9b0911 | -4.1015 | -48.256199 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1287c86-0a73-3a57-8ba6-bee05ac286a2 | -4.0878 | -48.241402 | 2024-10-11 00:46:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcaadb15-c2ff-332b-861c-c685784bbaa9 | -4.3859 | -49.812599 | 2024-10-11 00:46:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66587b9b-f757-3d16-9ca5-5c6c9ce2a8c8 | -4.3875 | -49.819801 | 2024-10-11 00:46:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903733fe-28f3-3357-af17-f2727cca60bd | -3.9495 | -47.9547 | 2024-10-11 00:46:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083f8c43-fc8c-3f5b-931a-4ee203974e98 | -4.3777 | -49.821999 | 2024-10-11 00:46:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97a80f70-8425-3f4e-af09-eae5081a82e2 | -3.809 | -47.479698 | 2024-10-11 00:46:43 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4accc274-e27f-31b4-a6b8-0449a9f97869 | -3.7992 | -47.481899 | 2024-10-11 00:46:43 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf4eb98-879c-3f5c-9616-39c12b4ddf96 | -6.5534 | -59.989201 | 2024-10-11 00:46:43 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58ed350d-0eae-360b-8a36-c64dd4d42581 | -6.5575 | -60.008598 | 2024-10-11 00:46:43 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
