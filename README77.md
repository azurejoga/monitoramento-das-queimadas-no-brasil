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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69170deb-93b2-317c-8b3c-4a77ba811c42 | -7.2234 | -44.21587 | 2026-09-18 05:16:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c34bb7a-c06b-3992-9a1a-651b302306ba | -4.56699 | -54.91216 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc380af7-a488-364e-99e0-e7fab62cb6c9 | -6.4538 | -52.84732 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7f62e8-0716-3fae-a2fd-dc1400708329 | -4.41856 | -55.50457 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e78296e2-26d5-3de7-9751-7f5929071ce1 | -3.42939 | -58.19074 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28235d83-1e2b-3dc1-a8fb-33b7f6044bf5 | -3.70215 | -60.63396 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50056563-38be-32b2-9286-742e8d7b0bc6 | -8.55518 | -44.89609 | 2026-09-18 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df056144-bee7-30c6-aed1-306e98adf362 | -6.65546 | -50.9199 | 2026-09-18 05:16:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10313a1d-7809-3768-b682-22a98e623065 | -6.65365 | -51.49151 | 2026-09-18 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c0c5421-7fb8-3581-91b2-337fd8d30aa4 | -3.21176 | -53.94591 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 745620e6-6ce8-33b5-a5ad-8e53bb929e8e | -3.30596 | -57.87485 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a13432d2-f600-3609-a5d3-ad1ffc3a1ed6 | -4.4963 | -55.50167 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c54fad9-417c-3f32-85f6-18d6778d91a9 | -5.63926 | -44.80628 | 2026-09-18 05:16:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 16e2c9e5-58ca-3dd5-88f7-9fa7639ee375 | -6.43564 | -59.98112 | 2026-09-18 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 38f15e3a-d55e-37ed-b6d6-47517fbf1d9a | -7.66364 | -46.08691 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c658e0e6-0133-384a-a16c-f4a1ba5c2b5b | -7.05841 | -46.22228 | 2026-09-18 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0519ff22-deb7-3ed5-ab67-966347fcf621 | -2.18949 | -56.84185 | 2026-09-18 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d28632-9b29-3f54-a885-e34af86a4e40 | -5.8562 | -52.06443 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f2b62ce-e7ef-3231-a53c-500bf7078773 | -4.50564 | -54.97321 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 281691ba-695e-30ac-ba4c-6571b7529873 | -6.10978 | -57.63614 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3405ca6c-ad5f-3808-a671-b5d8a619ec34 | -1.70222 | -54.88587 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dadda0c8-cf01-390e-af8d-246d025e55b7 | -2.90383 | -54.18203 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a8ec45-eaf5-3b15-b97d-5ab03de3804d | -4.88235 | -56.07423 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c88e1b9d-e95f-3d4b-b79b-5411ab85a4b4 | -3.71593 | -57.1782 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33db49f-425c-327a-a370-d9e99fc69546 | -7.8054 | -44.82087 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea7dabc4-fe22-36d6-a94d-0bc31661b63d | -1.38251 | -49.36627 | 2026-09-18 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da0f2d5-04e7-361e-8a76-5ae46623d59d | -6.01122 | -51.77388 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bb48019-fc5f-3836-81b8-56782508cf68 | -5.63344 | -44.79923 | 2026-09-18 05:16:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 74e917c2-6101-3836-8b89-0aefa269b692 | -3.07077 | -49.51698 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aa7091d-f451-38fc-bff3-892ec7d9b957 | -2.89478 | -56.93568 | 2026-09-18 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaa9c6e2-5f3d-3ae3-8e7d-2986b4e4654c | -3.26611 | -54.27137 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7c269a8-5f8c-3877-8c17-18cfab06d816 | -7.05829 | -47.48083 | 2026-09-18 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5e9ee91-61f6-3f00-bee8-16b48fb99ea7 | -3.36957 | -50.45498 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa824441-2415-3cb6-8274-d93aa58252ab | -4.47742 | -54.97279 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1947b6e3-f9af-3198-ae2c-24c16d5c52e4 | -4.53923 | -54.93134 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 507f352a-6c7a-39b1-aa1c-12b23a568970 | -3.47024 | -54.69566 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d61089c3-1f74-3bac-8bff-c857b77c0362 | -6.52011 | -58.30298 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f303b7b-f0c9-303c-b239-328ec94f92b6 | -4.50505 | -54.97695 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6693c958-b87f-35b4-978f-2eaa97e3a274 | -1.21378 | -54.22327 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed91aa31-39e4-3452-a797-c48237a0243e | -6.14872 | -57.71298 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1d39dd4-a21f-3d52-bd60-606cd399d916 | -3.71399 | -60.63136 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5434370f-7a88-3d31-9371-2af2028173f9 | -2.84189 | -57.63277 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a83968ed-0d7e-3716-bf9a-3d939a007951 | -2.57422 | -57.47963 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10e2e407-d0a1-30cb-9ae7-799fbce03416 | -5.89425 | -49.77892 | 2026-09-18 05:16:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53bb1a7f-5296-317e-afd5-053a4a47eb1e | -5.14215 | -47.60473 | 2026-09-18 05:16:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32703989-e9c1-3a74-aaf8-fb1272fc1084 | -4.5693 | -54.92015 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f9d6a6-5c1e-323f-8782-46acd9b2729a | -2.56188 | -54.74298 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d8d4e78-477c-31b8-827d-e25a131d402d | -3.60227 | -59.06404 | 2026-09-18 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a3aaec3-0de0-3d8f-9065-5c73b46350f9 | -3.70657 | -60.63015 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac7035c-1d32-3e0b-b100-cd93f7a1fd87 | -5.83566 | -52.0317 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5c86562-a1af-39fa-abf7-35d6950cae96 | -1.70278 | -54.88225 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74ff42d3-1cab-323b-b2e4-80588a5a544a | -7.10961 | -55.12446 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e87bcf4-446f-34e1-bb23-888b54224c00 | -3.37977 | -50.44745 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d517bc6e-f4b3-37e9-b289-a109e877d504 | -3.04182 | -51.37592 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e930ad4b-1399-356d-b441-213febcbd268 | -2.898 | -54.1731 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb8ce5b0-373b-37e8-b711-0ab61cb0e157 | -4.44826 | -55.47554 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b07e8ab-2afe-3e74-afe5-454a9bb8518e | -2.69665 | -56.72802 | 2026-09-18 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d60841a-40a6-382f-8c71-37ec4040fc7c | -4.38354 | -55.0359 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 051d0d08-2ca6-391d-82ea-eb035b5c154e | -4.49009 | -55.49697 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f8c7020-84a1-3630-ab02-a00fa4cf9e34 | -2.29318 | -47.87986 | 2026-09-18 05:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a44a403-92a1-32d1-b499-4b2d80fd8f0e | -6.10156 | -57.68799 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97c7d14f-38b5-3902-b2d8-021fbf684eac | -2.93682 | -54.15501 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10358e0e-e899-3cf3-bd6d-91e08ae7ca9c | -2.89558 | -54.18568 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c811a12-0932-37bf-9e0c-ecf82289ff67 | -3.36135 | -50.44923 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 50087076-77f2-337b-8eaa-490298335dbc | -4.17067 | -54.41063 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 668a9dc5-80e8-36ba-a32a-6942b92c3e99 | -3.19153 | -57.84571 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813d20cf-1a34-3f2c-89be-11604dfc9e61 | -7.80298 | -44.90452 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f248de03-fd66-3a30-9377-96cfc7bb2340 | -0.54063 | -49.14017 | 2026-09-18 05:16:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02bd1ff9-e9e8-36f4-809b-1ae8884d1bea | -3.33646 | -53.26464 | 2026-09-18 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c37dfa5-120d-378c-8a2f-f29ef47827fd | -1.15983 | -47.63458 | 2026-09-18 05:16:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69178f05-48f6-3052-8c6e-2069c0fbfba5 | -2.8968 | -54.18093 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f8147a7-2a0c-383c-920d-fe6d5eef00b2 | -5.89051 | -52.08899 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e01be348-7480-37ef-bf96-3d55ecd39fd5 | -4.88012 | -56.06663 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7450d40e-3c89-3770-a4e2-ae65621f043b | -4.43306 | -55.52891 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37034830-d6b0-3bf6-8888-ef94c777a612 | -3.69844 | -60.63334 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82fcd280-1601-370c-9f1a-87ff242b36be | -3.7132 | -57.19541 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e655d3-f0dc-301d-9352-65c4ddefcfc9 | -4.51028 | -54.96621 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 154f956f-0fc1-3aae-bc4d-14df3da469ed | -3.80791 | -58.89657 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d42f62-9344-3a7c-aa45-6a2669e9adca | -4.5085 | -54.97749 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7093b7e2-7a70-329b-b123-903d7dd60184 | -3.37022 | -50.4506 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4446606-b2f5-3fc6-a9b9-4bc828a782a0 | -3.72731 | -60.60948 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd9cecb7-8525-36b8-b530-0dcbb3ffc7f9 | -3.02146 | -51.34201 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebf58220-0b23-3df0-b9db-e909e3fc4692 | -2.90158 | -54.17057 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 249e4731-0844-3e4e-8d11-b6d530b09874 | -3.47665 | -54.69144 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068a1f14-e83a-3f89-81c7-21a2dc7922f4 | -4.48029 | -54.97706 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90bdb221-8d83-39a3-8fb3-9e5a6f317b6e | -2.81799 | -50.47622 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 67c1dec5-87ed-3a14-9231-d5741f0ac177 | -4.51037 | -54.98106 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3010a22-95d1-387b-a7e1-e4597260e661 | -8.53653 | -44.54592 | 2026-09-18 05:16:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dadb2c7f-af31-3e70-a363-1117ceaf8e4d | -6.45125 | -58.15948 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91ddf6a0-570b-3be7-98b7-c4c7b74fb4e2 | -7.55155 | -45.67823 | 2026-09-18 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7922d2a9-a964-3c63-b7cd-251bc7462ca3 | -7.22457 | -44.22179 | 2026-09-18 05:16:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01e1c98a-a800-3279-9bd2-0fa8a3dce3e4 | -3.70462 | -54.17315 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 086f6644-0585-3708-bba9-186cbe204e06 | -2.91509 | -54.15569 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b658eb10-bdcb-3af3-9afd-1216ed7cf42e | -5.86048 | -52.03533 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf4f5667-806c-3a28-9774-38b59af6b8aa | -3.76042 | -51.14122 | 2026-09-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f14d63fd-dae2-3e62-8e2d-f89d29354b9d | -3.35759 | -50.45001 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b82031b4-cd5b-3530-8682-a557e95f8e42 | -7.79694 | -44.89752 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9edfe699-872e-3679-b9bd-51998f1c903a | -3.48236 | -54.72333 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aae22925-9b34-3f57-acf6-d2bb8ddb2a5a | -3.73407 | -52.27755 | 2026-09-18 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d68007f5-cba1-344e-89c5-8c1423cae585 | -6.36237 | -58.29187 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README78.md)
