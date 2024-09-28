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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325f75e9-331a-3bb1-836c-e803ac1b31ca | -4.48783 | -54.99337 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df6b0a9d-f9dd-3b4b-9137-81e82772671a | -4.48099 | -54.96989 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b4cc2f1-f6b5-3c16-b1a0-34d39e94c79d | -4.48042 | -54.97356 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1bac5a1-4efa-3944-b885-c779bf720f15 | -4.38973 | -55.44826 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3822c5a9-3548-3489-881d-4ab6cbad5fbe | -4.37402 | -55.43855 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8581eb2f-e9d4-310f-8953-f700fda2d385 | -4.34683 | -55.22527 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6a56643-bec0-3418-a507-08689e8262fd | -4.34627 | -55.22887 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d236453c-8486-3195-a64f-00803f4e5cb0 | -4.34571 | -55.23247 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70c7375d-981b-3c3d-8158-52cee8d3e283 | -4.34289 | -55.22835 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 612c140b-7028-3ba4-bab6-72c89187847f | -4.31586 | -55.22417 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7380327c-9d47-3cd2-bedf-1c7930c8b61e | -4.3153 | -55.22779 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caf6c4c8-24af-3544-8d30-46f1f4179b15 | -4.31248 | -55.22365 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f918631-581b-3621-94f3-71b8a58be7c6 | -4.1932 | -55.1351 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa6c8d2f-dea4-32f1-8f2b-1428329bcf18 | -4.19264 | -55.13873 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d2bfc37-5880-388d-a45f-740fd53f9907 | -4.12819 | -54.89715 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb3a36f0-ea42-3a8e-a91f-6ddf6847ed47 | -3.95179 | -55.33746 | 2024-09-28 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43c4a6a4-36a4-3c76-85b0-3b45c613b5be | -3.64927 | -55.29848 | 2024-09-28 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c61570c-e72a-3159-a977-8037dd2edaa6 | -3.64872 | -55.30204 | 2024-09-28 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d640b462-d871-3b70-a6f2-905597af88d6 | -3.64536 | -55.30153 | 2024-09-28 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebef1760-351e-30f3-b4f3-ce4d96f896db | -3.62809 | -54.52631 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0466ed17-5e34-35e9-beae-298c59d9156a | -3.62516 | -54.52708 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcffc9cb-df5a-3dfe-adeb-935edc39c638 | -4.07192 | -54.10285 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8a5a299-251d-3d44-b55a-24a0a14c14f0 | -4.07132 | -54.10677 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 610a73ee-a766-3541-b255-c7f9acd5893f | -4.06901 | -54.0984 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79bff6ed-327e-3021-951b-67c75425b62b | -4.0684 | -54.10231 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0bc378-5817-3994-b850-685cd5da4d7d | -4.06489 | -54.10178 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 58c96d1c-eeeb-3aa4-b343-7f7c0b379f5e | -4.06429 | -54.10569 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54849013-8461-35bf-838a-d15eda3f9f23 | -3.72366 | -54.22634 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 133a4565-5e4b-33f4-baa7-760f4da1e6bc | -3.71959 | -54.22962 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e504633f-ac76-3681-a28a-0be5b083158f | -7.99953 | -55.02667 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 731fd420-960d-37bb-9fb4-09c4979928ec | -7.99862 | -55.0271 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a206ed9-2d65-329b-adc0-5bed694f3f84 | -7.99571 | -55.02262 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc5b88b-895d-3757-98a8-ddf83070cfb5 | -7.99511 | -55.02657 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ec128e-c082-3163-8da8-694b34b7f01a | -7.978 | -55.06816 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3f2f4a8-b876-34cd-8ac0-38e018463c34 | -7.9774 | -55.07207 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9073776a-a8a6-3956-a59b-71fc4cf85aba | -7.30761 | -55.30445 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb63f30e-2acf-361a-a20a-04c818249b63 | -6.99587 | -55.58295 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 348a1d4e-dc36-3210-a1c3-3e5c3f054fc6 | -8.221 | -54.89681 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6327983b-eabb-37ff-a8a1-af288ff9ea04 | -8.11435 | -55.07926 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e8182d9-84bd-354d-aea2-a8c1ebea081d | -8.11376 | -55.0832 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cb4a9f6-c590-34fb-a52c-c011752592e3 | -8.11254 | -55.35259 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f291f073-f597-3d96-ba99-bf076230de59 | -8.11201 | -55.07084 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d673d3f6-017e-3452-ac67-8033a6f5c026 | -8.11196 | -55.35644 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89dab917-99bf-3940-a312-64e2e2116163 | -8.11143 | -55.07478 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2877ca8e-acf5-33bc-a065-88d1dec95073 | -8.11084 | -55.07872 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 227440ea-ee31-3daf-8852-de19bb0aefbc | -8.11026 | -55.08265 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ae066cd-667f-35b7-8a4e-bd771ca4b32b | -8.09175 | -55.39645 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 882403a4-d6f5-3663-93a2-e58a3a9f4985 | -8.09117 | -55.40027 | 2024-09-28 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e709c6f6-606f-3d5f-9b70-329b65530c98 | -1.54763 | -54.95094 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37408ea6-03e2-3884-91ce-8aa92932d9e8 | -1.54429 | -54.9504 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dd45925-283e-3624-b7af-a0774534189e | -1.48852 | -55.87032 | 2024-09-28 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94de9ddd-70d6-32d3-af39-63a0b35053bd | -1.48521 | -55.86981 | 2024-09-28 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c4837d6-7183-3cb1-9ae8-62a2171664de | -1.44069 | -55.20079 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcb4b3af-ac2a-317b-8b0d-9e1150ab2316 | -1.43522 | -56.05899 | 2024-09-28 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50044d7e-1b7d-370c-93ec-aba16915284d | -1.26439 | -55.9131 | 2024-09-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 928c994d-caac-35f3-a530-5d0fa3fac3d3 | -1.26108 | -55.91259 | 2024-09-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a37d128-bcd8-3581-8981-24dfb8c9581d | -2.02502 | -55.9155 | 2024-09-28 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d86c35b1-bbe8-3872-aa00-1449e2b3204b | -2.60708 | -56.51344 | 2024-09-28 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6cde747-0748-31ae-8285-e092003c9725 | -2.52652 | -56.07467 | 2024-09-28 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93d9d522-ed0a-3d9e-9ac6-5496a264dba5 | -2.52321 | -56.07416 | 2024-09-28 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3520fd9-29c3-321f-b57a-f24497887129 | -2.51991 | -56.07365 | 2024-09-28 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a3df1ba-b100-3a54-9eb5-87d61a9915a5 | -2.51937 | -56.07709 | 2024-09-28 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de24e708-cd37-3e3c-8c2a-1ed485ab428c | -2.27929 | -56.41586 | 2024-09-28 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1df9556c-aff6-3823-8452-3ab2b0f112df | -3.76434 | -56.80062 | 2024-09-28 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd3d3113-8dd3-3515-895f-909c92b34b28 | -7.96846 | -56.69178 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7888e49-6175-3068-84c3-f85424c01edf | -7.86197 | -56.7217 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f92048b1-b258-3416-a5a5-72e385c8fcbd | -7.85864 | -56.72119 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe377ce-9620-3a88-ad19-154d448e2b27 | -7.82673 | -56.60084 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed83d6ba-fe1c-35d4-bdfa-ddba39ac119d | -7.79356 | -56.66069 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7475523c-f1c0-39c4-8928-bde99cc2d940 | -7.01583 | -56.66211 | 2024-09-28 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef3dc90b-706d-320e-b3c5-ee6d1c1dcdf6 | -3.68848 | -57.11008 | 2024-09-28 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f25d2a45-1ffe-39c5-a9ad-d09f0b7ac4e3 | -3.16876 | -56.85195 | 2024-09-28 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7486f7cc-3388-337c-aa1b-5002959c8633 | -3.77323 | -57.02429 | 2024-09-28 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8ada1ec-8ef9-30b4-8a36-c855299176f7 | -3.7157 | -57.19583 | 2024-09-28 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8a31a8a-a915-3a8e-bb1d-d6c193b8cea9 | -3.70853 | -57.19825 | 2024-09-28 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c482b0b-61af-3fb0-bbab-38ec82b1c59e | -0.7421 | -57.95665 | 2024-09-28 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df342c2a-d131-3c22-874b-0422eb4c7203 | -6.08866 | -59.95227 | 2024-09-28 05:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c935574-f2ab-3c29-b7c3-302b59bb2394 | -7.44989 | -59.77792 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c74282e-a5b3-3aaa-a6fb-5d7fd43c44a9 | -7.44703 | -59.77352 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6813f23e-3ec7-3bcb-86c1-11a61e7f730f | -7.41502 | -59.83929 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff7bfa2-f7e2-35db-b71b-1a2480a8a7fd | -7.40897 | -59.81059 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a0d986e-3f27-34a5-b39f-dfbd2ebffe17 | -7.40607 | -60.29475 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fa344a1-e681-39f9-8585-297d2efa1d5d | -7.4055 | -59.81004 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e79da235-4261-307e-b4ca-1c01cc3159a8 | -7.40474 | -60.3028 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35924756-f5b9-3422-86a0-126ffb2d827b | -7.40186 | -60.29818 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b7691d-e77f-3f34-913f-38a509b4423b | -7.39832 | -60.29757 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95dc9289-cb28-3a62-beb7-2d0aecde742e | -7.39765 | -60.30161 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5d0ef28-09cc-3f3b-a28b-56c74cc62eed | -7.38388 | -60.30003 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3733e046-e90b-3174-ba11-27cca52db723 | -7.32632 | -59.89307 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23c4e08-010e-3bed-b47b-4224ccd81334 | -7.28493 | -59.58374 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c68de6c8-b060-395f-b289-bbc071001d40 | -7.28148 | -59.58315 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3029ed1a-38c8-36a7-ad47-74283b96fa36 | -6.98698 | -59.95282 | 2024-09-28 05:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9f9ebe2-251b-32d8-82f9-eec129517cb7 | -9.24136 | -68.30796 | 2024-09-28 05:10:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 498117d5-80fa-3dba-8b7c-ca8b33c8d3f5 | -9.2406 | -68.31193 | 2024-09-28 05:10:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 22c676f3-aca0-32af-91bb-0a6356f975e8 | -9.24037 | -68.30785 | 2024-09-28 05:10:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be461621-e49f-33d4-bb08-7ff5dc30a9bd | -9.23964 | -68.31181 | 2024-09-28 05:10:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6d2bc01-cab8-3800-a440-e60c1d3a0772 | -9.11772 | -67.89591 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f79ecb-ed44-3d14-8e32-8b1f6a27b357 | -9.11703 | -67.89973 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec300f85-8ed1-3b97-9e0d-50a70cabaac8 | -9.11641 | -67.89175 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f96a10c5-f34f-310a-a3e6-72f41fb1da70 | -9.11569 | -67.89556 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README75.md)
