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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 462704f5-2255-3ce3-99e6-81c3ce4a6d7d | -2.40467 | -46.70478 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7158f69-e592-38ce-a2e5-eb5fc96e5819 | -2.39456 | -46.72506 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e61628f-e980-348e-8375-20be7ce7bbe8 | -2.39121 | -46.72453 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 335123dc-5e97-379f-aa10-8ec522152d46 | -2.36639 | -46.98878 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c58e37f2-c2ac-3a53-8c67-e7f849cdd503 | -2.34791 | -46.20667 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff97341-7097-3b17-93be-bcd69e159460 | -2.34459 | -46.20615 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea600a44-aeac-391a-9ee4-55b20d0c1b82 | -2.34182 | -46.20215 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb6a88d5-faaf-36bb-8dba-3560f824f414 | -2.34127 | -46.20563 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb4d24c1-ac2e-367b-b551-495538cae813 | -2.3298 | -46.59899 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a9dceab-1158-3adb-b933-d013053ce4b7 | -2.32586 | -46.64553 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63e55397-8eac-3a4a-a966-d18ccc7383ce | -2.3254 | -46.49706 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98e5ff92-0468-306d-8c14-ee660b77423f | -2.32251 | -46.645 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71a0b66b-e248-3408-853e-fad2200d7f89 | -2.32206 | -46.49654 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ad37f0-1273-395b-9be8-bd3eea873e7a | -2.32194 | -46.64856 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28cef8cf-514b-3530-b790-45b7edeadd69 | -2.32138 | -46.65211 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc248c50-c003-382e-84b0-1d389b568911 | -2.32028 | -46.63738 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05cac213-4a39-3b6b-903d-68cd4fca0f99 | -2.32026 | -46.65922 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e50aab9a-4e9d-307b-b2bb-b688305f685f | -2.31972 | -46.64093 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73b85cf4-1c98-32c7-abaa-ef52f621111c | -2.31916 | -46.64448 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e62679bd-f3ba-3356-a3f2-774170b9f5f4 | -2.31859 | -46.64803 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f8aeb33-caaf-3ae1-93d2-b24e358f08b0 | -2.31693 | -46.63686 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1934bc18-327c-3f0c-9936-3925e390c888 | -2.3169 | -46.65868 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0580ccf5-f161-3e80-9c65-30dd8f19d7c4 | -2.31355 | -46.65816 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05aa6643-c5ae-393b-8991-73cd54b64040 | -2.31076 | -46.65408 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d905c6e7-2bb4-3c89-8262-e4566bb742d1 | -2.3102 | -46.65763 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f078ddaa-9ff3-3e3b-b158-a014da863b54 | -2.30741 | -46.65355 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46a02415-8351-37a4-ab72-a82514c0f6b4 | -2.30684 | -46.6571 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bc6388b-8337-365e-b952-5e3a8538395e | -4.00631 | -46.44223 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11ebc016-15eb-333f-a042-4ccbcf513622 | -2.30406 | -46.65302 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c471deb-cded-31d4-83e0-06a855b9547b | -2.29735 | -46.65197 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82973935-21b5-3e70-8d08-09325a8fb938 | -2.29456 | -46.6479 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b83090-7fb0-38ba-86b5-ee59be8687fb | -2.28822 | -46.75262 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a005aae-0f90-374b-a299-eae782de7f66 | -2.28765 | -46.75619 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2df71d6-2d7c-3094-9d33-b42636435d6a | -2.28571 | -46.60314 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2ed43a-75bc-3327-97fb-8371069dde0d | -2.28543 | -46.74853 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03544f0c-099b-3d7d-a93a-665969abcb92 | -2.2849 | -46.73019 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b243fc6-12b8-329c-9c84-83b33985e40f | -2.28486 | -46.75209 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a955e169-94df-31be-af0f-6d58809b6380 | -2.28429 | -46.75566 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18125b44-1884-3077-8440-3d5fe012139c | -2.28207 | -46.748 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4538001-13e5-359d-85a9-f7c6d9610a19 | -2.28154 | -46.72966 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea93073-6928-3ca9-888a-2f45c8e2bb55 | -3.53085 | -46.28912 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 687326dc-9aa8-337f-8030-a9b2a1e0e185 | -3.52753 | -46.28859 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1a1ba6d8-53d6-3eda-85d8-328f3537b371 | -3.44313 | -46.39266 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 491af23e-dc9d-3bcb-b510-c6574cee2823 | -3.33258 | -46.27576 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92aab472-9ce6-3120-b93f-a278b97b93c6 | -3.22829 | -46.50505 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12bac83a-2e6a-3b69-a20d-9ea7e32fb8f3 | -3.22053 | -46.511 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e6d8504-156e-3936-bec0-020e18484c06 | -3.2172 | -46.51048 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb74f983-bddd-367f-bcc1-272e0579931f | -3.1761 | -46.51484 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 606049ca-03e2-39de-acc6-ba4a0404f4ad | -4.6053 | -47.52976 | 2024-10-27 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4e94397-27cd-32ae-b3cb-c07259731e75 | -4.60473 | -47.53336 | 2024-10-27 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f00d6e3-8d73-358c-91b2-3bf404fc3ff4 | -4.60077 | -47.53643 | 2024-10-27 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f4ca2fb-2f1f-35bd-b21c-bdcdcb597543 | -3.79766 | -47.49421 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a09eb208-0dac-353f-944a-b6ce8fe694ab | -3.7913 | -47.51208 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa10da20-d9ba-3b90-b4a9-0888d09e94c3 | -5.00293 | -46.47828 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa0bd33e-658c-32ec-8179-7a1b33ff7387 | -4.97868 | -46.48154 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da88f4f9-44b6-37a0-8e6c-78a2620be874 | -4.96711 | -46.49036 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3fb8054-7fac-307b-9d8f-af9a61d3361f | -4.90708 | -46.84796 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79055f38-3912-3634-a246-ec2ea12e3a9f | -4.8582 | -46.87982 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb3fe11-1662-34e2-9dfe-e0fd70dcc894 | -4.85487 | -46.8793 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4dc2ec0-fa29-310c-b7b5-9f6c0e33ba12 | -4.81825 | -46.87349 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c142fccd-870c-3b8f-9274-c2ae0729da89 | -4.81492 | -46.87296 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ed4ae2-90a9-3f22-b3a4-cb1b4e4fedff | -4.81215 | -46.86892 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0599ab18-0073-33b0-8a6e-4df648ed86ce | -4.81159 | -46.87244 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 672d5a02-5023-3bf1-b170-53c09668e124 | -4.78332 | -46.59961 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62d3095f-409f-30c9-a3ed-15152387b166 | -4.74795 | -46.58689 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d535e7e0-d7a9-371b-b308-a3ca1cc5759e | -4.65703 | -46.32438 | 2024-10-27 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53d9eefe-64cb-3fae-8dc3-6e90466eb802 | -4.65648 | -46.32783 | 2024-10-27 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ca69b5d-a760-3956-8e6f-4369023e9026 | -4.64188 | -46.52759 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732f2fd3-3a2c-33bb-be5d-50a206d8d873 | -4.56814 | -46.45588 | 2024-10-27 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ea81a14-791c-367f-a8ff-72bbf4d6debb | -4.53111 | -46.41106 | 2024-10-27 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72ccc3a1-551d-3206-9618-6046d9421d7e | -4.36649 | -47.08805 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ef03b075-afd2-3763-9c36-2584c7a568fa | -4.36593 | -47.0916 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c0a48c71-3e95-3cc4-a8cf-5180c2205d5e | -4.36314 | -47.08749 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5792a014-f5ef-326f-85ca-313a01c80c2f | -4.36258 | -47.09105 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d371deda-883f-3f19-9a3b-3196ca9b31d1 | -4.26903 | -46.28454 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2427ecac-cc05-3b4a-a94d-aff4a74e6a5d | -4.22825 | -46.86309 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3423f5ed-8a9c-33b6-8c8c-d22fb5a16e62 | -4.10887 | -46.73983 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94966a2f-3ccb-3406-bc01-7b73288af1d3 | -4.10609 | -46.73578 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ab8f69f-8f6e-3417-a1c4-456a12b69d0c | -4.10141 | -46.48496 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e136818b-0dc3-32c0-add6-4156f452bee1 | -4.0981 | -46.48443 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2fd23cf8-6cb2-3477-ad24-b96b5d1a43c4 | -4.0712 | -47.3612 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e0efb96-3e27-390f-a2aa-a361bf39e032 | -4.00975 | -46.52808 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7996cb9-ddd8-38e0-8fdc-60737b46b0e2 | -4.00299 | -46.44169 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d882c3a0-2cb4-3387-88f3-cb9138cf5208 | -3.95602 | -46.41644 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21aab53d-e5e6-3ebf-850b-d6b63124c66a | -3.95427 | -46.40523 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a2f0c49-201a-358f-9670-24b3929313b0 | -3.95264 | -46.41558 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 994032ab-bc24-3fff-9baa-065a9b6f27a8 | -3.86825 | -46.62705 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 490d9bd5-138f-31be-b6d7-4a5b5095a324 | -3.8677 | -46.63052 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257ab7c5-0f13-3f8f-8078-5be93e4a9a6b | -3.82687 | -46.48127 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c9c908c-c126-33e6-8eef-8d404818a878 | -3.81587 | -46.93616 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa0f853c-996e-382f-95b8-5330f141972f | -3.8153 | -46.93974 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10d193fc-8a35-363a-a0eb-e58b9e463c89 | -3.81309 | -46.93205 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21375332-32e3-3451-8ba4-c3b1610458ca | -3.81252 | -46.93563 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd1c04d0-5c38-3ef2-8905-91798c692a16 | -3.72394 | -47.31838 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 107f7c06-1cb1-358e-9976-9e62ebedcd50 | -3.72336 | -47.322 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39473cf9-430e-3f4d-8f84-39c110d31818 | -3.61077 | -47.25986 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92e22e7d-a004-3323-84d0-39f49ce92e6a | -3.61019 | -47.26347 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95171a77-9a66-3c10-907d-7487671fdc5b | -3.60961 | -47.2671 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3694aee-4517-33ee-bef4-9bd0223ab28b | -3.60739 | -47.2593 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60015e93-2a28-38d5-a406-3b0ae8596c7c | -3.60672 | -47.52467 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README45.md)
