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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413340fb-c5d4-3664-98d0-d4781a941cb3 | -7.18539 | -45.47732 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35baaaa2-60d8-3b4f-883d-780f5cb7136b | -5.5939 | -51.12877 | 2025-08-06 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 064c0078-01c3-3217-9eeb-b96644dc2c2a | 1.6906 | -61.07518 | 2025-08-06 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db050a6f-868c-3ded-bda5-07a9f907f82a | -7.06775 | -44.39191 | 2025-08-06 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d082b04-d371-39f7-bf4a-ee116f49cd21 | -4.12883 | -54.89931 | 2025-08-06 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec3fa8c-f9f0-3e66-84fa-efb231e99717 | -5.02887 | -56.1938 | 2025-08-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c42baaa-1c46-3302-b5ff-6daaf9f2368f | -5.7225 | -49.10054 | 2025-08-06 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b71a8b36-dabd-3457-8766-ea9bd7ff0a0c | -4.82088 | -47.3143 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98e1bcb9-c561-39c7-88e7-9c73ea519571 | -3.32228 | -52.62255 | 2025-08-06 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f026f5e1-008d-35a5-9162-a7ee5ab15de1 | -8.24196 | -45.06536 | 2025-08-06 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4993dfdc-76a5-325c-82ea-ece85b0370ff | -7.91314 | -45.5304 | 2025-08-06 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb6a74d4-a65c-38ba-8433-026402949f87 | -7.1912 | -45.48347 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9b38eb-96e5-3c85-91be-e55370ddaa5e | -3.04343 | -59.91412 | 2025-08-06 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 5a2380a0-207b-3dc5-9ba5-90004adedf16 | -4.77955 | -45.32998 | 2025-08-06 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f8744d4-02ba-3835-9d6a-289c2d13af60 | -6.2437 | -55.60804 | 2025-08-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9610eb6b-9d6f-37be-89fc-f2e8164b4837 | -3.0477 | -59.91055 | 2025-08-06 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 5cce5482-5410-312e-b87a-7bd09b2e30ec | -8.2547 | -45.07343 | 2025-08-06 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c557975-fb06-3ca0-97fc-280a96ab718e | -3.03533 | -49.43675 | 2025-08-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82184d2d-4916-3306-8dda-43e40223cee6 | -3.03607 | -49.43171 | 2025-08-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9be6d58-cf8a-332b-aaed-d9743378579d | -4.02557 | -48.06438 | 2025-08-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87c3a6b0-626e-3a4f-bf61-814190b1454b | -7.90577 | -45.53088 | 2025-08-06 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31401635-f76a-3ca0-9b65-b5e014cb7c84 | -7.1845 | -45.4828 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 57fb7756-0093-3cb1-9083-e1b4c8283931 | -7.19192 | -45.47803 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa834b7-a8c2-3a6e-96c1-8821ecd74655 | -4.82038 | -47.31788 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9f0cfb-00c4-3f0e-bf53-c8e379fc4c91 | -3.05278 | -47.38225 | 2025-08-06 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7352be0c-41ef-3051-bcd4-3e5b09070e4b | -6.67932 | -49.78909 | 2025-08-06 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6421b9f6-b91a-36e0-b7e7-596bac2f06fc | -6.68494 | -49.78445 | 2025-08-06 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3765b569-ee7e-3d77-8a55-fb028719fd2b | -7.68163 | -45.10449 | 2025-08-06 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03c36319-8c85-3b37-9573-536d6b051882 | -6.42164 | -53.36301 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 150eba92-d6bc-3521-a137-b9dc5f008169 | -7.37064 | -44.15675 | 2025-08-06 05:10:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f0d4d25-e407-3218-a085-8e9fa985babb | -3.04704 | -59.91466 | 2025-08-06 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| faca32f6-4b9d-3676-a57b-e1e260f29368 | -7.19171 | -45.47812 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6e873cf-848b-3684-af38-de2bcacba31b | -4.77665 | -45.33244 | 2025-08-06 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0f66f08-a4e1-34f0-9f8a-77f474499f9a | -7.4528 | -49.25875 | 2025-08-06 05:10:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1935f320-b848-336a-8568-592da6b61191 | -5.04557 | -56.19638 | 2025-08-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01446ad9-2492-3196-91b7-5ed8fbeb2bf3 | -3.71315 | -53.37638 | 2025-08-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc7835e7-7b60-3fef-b9ed-f8a9857f447b | -4.81988 | -47.32148 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5eabd4b-3179-3c8d-87fb-70d40996fb4e | -3.7376 | -53.73307 | 2025-08-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea9121ee-5585-303a-a8e2-f547d3988e81 | -6.41782 | -53.36245 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fe1805e-f4f1-3ca0-b367-2a4817232f40 | -8.26144 | -45.07448 | 2025-08-06 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83a042a7-9d16-3ee0-af48-3fe425cae0df | -4.82174 | -47.32165 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3af6523e-bb46-315b-973d-ca4a6f6f983e | -3.71381 | -53.37193 | 2025-08-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1d487a1-ce8d-3914-9d2f-5089cedb1cec | -5.72753 | -49.10133 | 2025-08-06 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cce33fa-03b8-36db-b4ad-b174b95cbf73 | -7.64117 | -44.58196 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2af4fd44-45c5-3e6c-a483-5b8a3b8d1e58 | -6.42046 | -53.36471 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8e8c387-4bb9-359b-a2d4-79c7dc5fce20 | -6.4164 | -53.37184 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22dd5f2c-91b5-3a23-8d3e-7c13cb664f44 | -7.07388 | -44.39905 | 2025-08-06 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f63b0f5-0127-3766-9fcc-bc49a98ccbaa | -6.27315 | -53.63412 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c4073e84-0ea4-3dea-8af0-42bdebf0139d | -7.5812 | -44.89845 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65de471b-688a-3530-86af-cdfe40b91f6a | -3.88478 | -54.21211 | 2025-08-06 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcbab899-9925-3157-9242-09a1c7e4c061 | -6.63462 | -56.29202 | 2025-08-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d1d5da3-cbab-3af0-928b-b0377bafe87a | -6.26815 | -53.63581 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 002ee49d-7761-378a-b76b-4cadb180db17 | -4.82645 | -47.31539 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f33db24-1b2e-3135-ae74-e34f3f1e2719 | -4.01983 | -48.06674 | 2025-08-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 411e9041-8d3d-3d4a-bd0c-1d4e93e686c2 | -6.42093 | -53.36771 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c7f3f26-207c-3eb5-b3ce-5f7cf5ff91a0 | -5.75714 | -45.11223 | 2025-08-06 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6249960-d691-3674-8c15-dad4187b2778 | -6.27258 | -53.6319 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43f8acec-fa70-3803-bc86-1dafc01eb697 | -7.24381 | -44.60999 | 2025-08-06 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5cfbb0b-c96e-35df-a0dc-17a76f05c4c4 | -7.64071 | -44.58349 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6591c72-0a4e-3c5c-96a4-63d89f3af52b | -6.41188 | -53.37597 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bbd3e13-1fd6-33d2-bff1-6ff115f5d592 | -4.03036 | -48.06842 | 2025-08-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2164c83-9ba9-3c41-a3a1-ed37b8ec596a | -6.26941 | -53.63343 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fc2edeae-7ccc-3e4b-940f-e9b4ecd4123b | -6.41911 | -53.37411 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 177f8214-1da3-30b9-aeaa-21725e135439 | -5.67662 | -50.26011 | 2025-08-06 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8af92e9-298a-3c8c-8337-e212ef412534 | -4.0203 | -48.06354 | 2025-08-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72364977-a9b8-3329-bd0d-f30f496c6d06 | -8.24871 | -45.06632 | 2025-08-06 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b933651-7d0d-3660-9595-50dac527ed84 | -6.27189 | -53.63648 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3bdc386-6f9f-3320-955a-15403d2f4723 | -6.41711 | -53.36715 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9febb0a-73a5-3e8c-b451-3228a54eb9bd | -7.52237 | -44.8546 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fbd2843-8481-3051-8b16-4c880319f31e | -6.6324 | -56.29198 | 2025-08-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4faf9af5-6fc3-3bf8-8f8a-271557bd2c54 | -6.95132 | -51.63487 | 2025-08-06 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0368396-e915-3eaf-8c7c-4d647982dbbf | -6.41978 | -53.36942 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c4e9e4a-57d9-3538-ba5a-cbefd979a478 | -6.42022 | -53.3724 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 605d0acd-3b98-3f7b-9387-317a780ab9ed | -4.41204 | -54.86131 | 2025-08-06 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84fe6d0a-3a3c-3767-b19b-b337a5fb642c | -6.15307 | -55.80862 | 2025-08-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b84ca9bb-88df-3612-8a76-136bb86ba8f1 | -6.95191 | -51.63072 | 2025-08-06 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cdde128-a87c-3492-87f0-5f3f0a13d55d | -5.7271 | -49.10427 | 2025-08-06 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d75faa9e-93a4-34b2-b3e2-ecdd0c85c787 | -6.41664 | -53.36415 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8df87127-d67d-30b7-8719-ff7982663e8d | -6.29027 | -45.74585 | 2025-08-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9cd4e67-a2f4-3c47-85c5-160757b71fe2 | -7.18467 | -45.48274 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc6a5ad7-8a1d-3af3-bfe1-125e4d6251f3 | -6.42475 | -53.36827 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f917fb6-8509-3a75-8afb-a0eb9319d44b | -4.82279 | -47.31443 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ed5dcf-feac-3f63-acd2-7cf63a881473 | -6.41596 | -53.36885 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfabb508-8c93-3c96-ad25-2ff5afb94a0b | -6.74524 | -45.29956 | 2025-08-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba75ac15-8c31-3a1d-befe-642946c53b1d | -3.2344 | -60.19546 | 2025-08-06 05:10:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d507c707-6382-3767-b89d-3679baa559f3 | -7.91239 | -45.5362 | 2025-08-06 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2118b17c-072a-33f4-8d0e-faed4fa75b1d | -8.90854 | -60.59935 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5d6dce4f-c9cb-33d6-bd47-fca9962a8e84 | -8.91744 | -60.58883 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 759f6810-92d4-30fe-b563-d922b3bf140d | -11.72523 | -47.52155 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 209efebf-c022-3e78-aded-972497c37a00 | -8.90734 | -60.56319 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b200eb37-93f8-3bff-9d9d-a069c560006b | -8.92669 | -60.55434 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c8648c9-fb49-32f6-82c6-ca957262bdb1 | -9.69806 | -48.8699 | 2025-08-06 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dc75488c-a4f7-3170-99c7-5791084657fe | -8.91617 | -60.59659 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| bebb5767-ab57-377c-ad41-98f0958d6ae2 | -8.92251 | -60.60163 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 072b6920-4961-3942-aebe-850dc1237d39 | -8.90101 | -60.55817 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d965681b-d603-3969-b4ab-f60fdaf0d958 | -8.90569 | -60.59489 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| d0f7b590-5d61-3c54-aaba-893ca86a49c0 | -8.84011 | -47.61842 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbff2c6f-af50-31be-a138-c14879d8f0d0 | -11.44084 | -45.14442 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3b4402b0-fbcc-3e5b-b13f-11b829c54fcb | -8.91809 | -60.73818 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 752c8780-d92a-35d9-b9e4-3054140af45b | -9.93351 | -60.47905 | 2025-08-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
