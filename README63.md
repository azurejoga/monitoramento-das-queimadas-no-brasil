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
| ef0f5253-f4a1-3178-b361-f598a52be82e | -11.10798 | -51.337 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68805cd5-51c6-31fd-9613-ad4d30ed93cf | -10.21004 | -49.99533 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6120abca-b579-3770-9362-47ad2ff14dc0 | -4.98394 | -56.15044 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c31ec1d1-6fd3-38fd-b362-236cbbb2538f | -7.27494 | -55.57841 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7f0aef0-19d8-3df0-8cd7-eea8a1535b7b | -7.71515 | -54.77377 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f149d5b3-ae95-3498-a3a4-7e26aecb6469 | -6.90625 | -59.9388 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46e56a8-88f8-3439-b9ab-182405a0e53b | -6.85957 | -59.89157 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| babf1cc3-9dc5-3efa-b220-b6ca064bf94f | -9.99206 | -50.13869 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 30f4afb1-b41d-3a5b-a380-00666523c425 | -6.07208 | -57.83023 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a788970f-c8af-36e5-9a50-c146f9b68a2a | -8.03842 | -54.89718 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1095f24-4c9d-38c0-a7f3-f28396d17111 | -7.71571 | -61.24692 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa8dbc3c-f8e1-3997-bea5-d264cad05a6a | -11.10909 | -51.33029 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 702ff0bf-437e-37f5-aa9d-3ed50d916723 | -6.78033 | -59.37243 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 708c160f-2136-349d-a936-ee862a15d0c9 | -9.97812 | -50.15339 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eed64c91-d241-3cea-904d-4ea58e3b648f | -9.13292 | -62.01156 | 2026-09-28 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2a86919-a0ab-30dd-a5d6-f9e3c9436f23 | -9.94269 | -50.23581 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5cfa4f9-dfdc-31d8-9f58-6c4ad810e280 | -9.1539 | -61.3678 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e509eae2-53cb-37ec-b6bb-9ce291596515 | -10.21329 | -50.00621 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c439f31-e8cb-3cf8-b522-8c7f63843ae7 | -4.09003 | -62.09589 | 2026-09-28 05:29:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08f59291-15ef-3b13-8235-4ebdd26e41a0 | -10.11536 | -55.41281 | 2026-09-28 05:29:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5269422f-6d7e-3c9e-89e1-5e193e9363b5 | -10.01734 | -50.23877 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b82fd6b-7d0d-3c12-9c0e-27ad593af8e8 | -10.2213 | -49.99221 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b59da585-09a8-33a7-b807-b26ddfbe4536 | -7.82657 | -55.13406 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d5aade-50d4-3948-9f9a-584c8d859c4e | -10.89602 | -50.68694 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63d0c09d-cfd2-3391-b523-99513503f036 | -7.93927 | -61.52887 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78b26cdb-491f-3ac5-9cf6-35586d01a2e5 | -7.72013 | -54.77018 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebba0e1-04d4-34c2-bbfc-d9e256519e34 | -9.98473 | -50.14749 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 96eddf5a-b1dc-3827-93c5-5f67fb2e7f41 | -7.8062 | -61.61834 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e340d5c-111c-3963-a2f5-945625c560e0 | -10.20881 | -49.99057 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb4bc0cd-cd75-3d27-837f-6feb3e47a6be | -6.87735 | -59.88715 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| decf0517-ed8a-32a2-bc15-af8777c740d0 | -7.72564 | -61.2485 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae69caad-af2b-38d6-9740-5c182bf3d0b0 | -9.0833 | -61.44926 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abe4b830-5f4b-3157-9353-51d6aab5085a | -10.89748 | -50.68928 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ad74977-a019-3653-b63d-ecf956d502b5 | -9.98589 | -50.13789 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43316436-a160-38b9-93c1-85de2d5a0719 | -10.11971 | -55.41341 | 2026-09-28 05:29:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac03f994-497b-369b-9a1f-cd3247d97b37 | -7.27959 | -55.57538 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8efcbf70-fa84-34dd-9f31-45fdc5b3b153 | -6.64471 | -59.94117 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dd4c998-f396-357a-85c2-9aa674e66647 | -3.96007 | -59.34632 | 2026-09-28 05:29:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2f7cda-3077-39c4-acb9-f7a9669e50f2 | -4.97772 | -56.1521 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7966a4ef-3185-3ef6-9300-7f1433302956 | -6.07393 | -57.81812 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d80302-dc6b-3399-a6af-f724514b85d7 | -10.20504 | -49.98466 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f8d64a6-df78-398e-8903-f95716fc2f4b | -10.20646 | -50.01034 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b5860ba-7818-3d29-bc2e-84434673d747 | -6.16775 | -57.69862 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c31440-ee52-3782-9a2f-424ec1bba8ea | -8.91159 | -61.48204 | 2026-09-28 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12568ad2-0bcb-33fc-8e10-38cd270409a8 | -11.12862 | -50.06595 | 2026-09-28 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c36b8369-4a06-3463-a557-4480b3bc7ec9 | -6.0727 | -57.8262 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e192bd8f-1725-3b0e-9a60-43ed72290cbf | -8.65511 | -62.67537 | 2026-09-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 307f0e5e-3c9a-3ad6-9a5d-f8491ae984db | -8.60401 | -63.9319 | 2026-09-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27c5aafd-4c08-35d2-9a95-d097c44c377e | -8.60531 | -63.92397 | 2026-09-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15046722-3883-3dab-97bd-ab801dc14d54 | -6.78878 | -59.38479 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fecb254a-4375-3803-99c3-51bba5c1497c | -10.40285 | -53.81438 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f02c4ef-b031-3a61-944f-cd54aa03b5a2 | -11.1144 | -51.33517 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f38dd439-3f40-3eb2-a6df-51aa5b9353b0 | -5.86285 | -57.56361 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50781f1c-fe76-3f1c-8890-303580342407 | -10.22253 | -49.99693 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e5cdfcf-cae5-38f7-8c07-6ef193c913e5 | -7.71138 | -54.76893 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50d96a22-228a-339f-a0c7-2b26aa74ad9e | -6.8779 | -59.88363 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 022edb58-5025-3125-9557-5fb535db8c31 | -11.13552 | -50.06166 | 2026-09-28 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f8e935e-ba5c-308b-b0a2-4db5917ab596 | -11.07656 | -51.39965 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f1b4e28-7bf4-33f2-bd95-0d2fc1de6e4e | -10.0071 | -50.12296 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d9d151a7-ab84-3c98-96da-714fdeea7a8e | -6.85902 | -59.89508 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aef961f-6437-3af3-9d16-8f4a825d24cb | -10.9009 | -50.69675 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e27742e-124c-38f9-a8b0-e999e3369118 | -10.21504 | -50.006 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cd62dc7-4645-367e-bb88-b9f9c0de59ef | -10.10997 | -50.1976 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69cd7e83-dfa7-3fce-abd1-369b2acbe7ae | -6.78203 | -59.38375 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ea0d4ab-0c8b-3865-b6a5-65a3d1f87c31 | -10.20441 | -49.98965 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79a15b3-0d7d-3e71-b631-3a7ade428577 | -6.66839 | -60.02708 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b860a602-1f78-3ec8-8778-6afd9ec3236d | -8.72562 | -47.98255 | 2026-09-28 05:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bed30d0-f87d-329a-9e83-76e2d0cf0c09 | -8.60837 | -64.06047 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5240955a-b24a-3f98-88f8-522769893687 | -7.68566 | -54.85551 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc0ead9d-5f28-3a44-b58f-3b49baf3a794 | -8.60771 | -64.06451 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71414047-ff97-35cf-970b-98ba69d32468 | -6.07639 | -57.80202 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a95d581-91cc-3eea-9fbb-858265c735dd | -8.83672 | -62.39536 | 2026-09-28 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41eb0938-009a-326b-8eae-0fbf4a31e2fe | -8.84006 | -62.3959 | 2026-09-28 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a691b2-3fb4-3b8d-b3f8-c009cf1df3e2 | -7.82769 | -55.13482 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371fefa9-be22-3833-84ff-c4ab6500e025 | -10.00031 | -50.12697 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 56a72441-a96b-359f-b628-a7f029cf3ef4 | -10.21753 | -49.98629 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2785fabb-2674-3c9b-942b-1c4aa660c82d | -5.30782 | -55.8321 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 803c07fa-4bce-3672-858f-0bf6a5f7eb13 | -10.42084 | -53.82817 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 881722b8-8b0b-36f6-b3c3-c040b75d1c82 | -4.9785 | -56.14712 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c66074ed-5d61-3521-bd4a-8438d91475ae | -10.00674 | -50.12108 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 281b55d2-4f35-3834-9658-1155be5d7b48 | -7.69447 | -54.76213 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30af4332-5f81-306a-b8b0-520b796ce505 | -3.97061 | -59.34439 | 2026-09-28 05:29:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9e0aab9-3929-39d2-a021-ae14de8ac3dd | -7.93871 | -61.53235 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5986832a-f390-34f1-a2b2-49bce9783b5f | -11.10746 | -51.34113 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2c2425a-3800-3e8c-bfef-151c62010535 | -10.21691 | -49.9912 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e87a9cf5-d2cf-30ec-9ee8-1aeb019a90b7 | -10.21447 | -49.9963 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb539edc-a78b-30a1-b4cc-8a01e4ea5234 | -8.02595 | -54.891 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 906b09e9-2148-3d66-8065-f1636aaa3a5b | -11.10373 | -51.32394 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14a35fd2-385f-31fa-b2c3-5aad7ecaf4a5 | -6.691 | -59.96964 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3e0161a-cc33-38cb-aa5f-bad1f55cb2d5 | -7.8223 | -55.13342 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9a7c60-3b1e-3add-add0-7493b60df0a2 | -10.2094 | -49.98561 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9705b071-b79c-3319-8def-c775140139ab | -10.25486 | -57.71886 | 2026-09-28 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c00f50-ca93-3f00-ab3d-fbc0c328e54b | -10.42158 | -53.82262 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb3148e9-206a-326d-9334-1308b5e00ab8 | -8.61192 | -64.06107 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9259fce-eba4-3f2e-bef1-5ec6d781c547 | -7.71461 | -61.25386 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1f073f8-6d58-39b8-b0c8-c7445707515d | -7.81796 | -55.14161 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3feb090-975d-3c9a-9bc1-35ff5e1a27ec | -7.82062 | -55.14541 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9d17352-4057-3be1-bf77-1d5cce63095d | -11.10761 | -51.34267 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 640cdf02-c9ae-32c1-a9c0-e24936c504b1 | -9.9421 | -50.24054 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee6abc82-0581-3fc1-8312-108c4f9517c5 | -6.05789 | -57.82795 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README64.md)
