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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0cff721-e7f1-34c7-8fa5-274b22fde3b9 | -5.21122 | -46.06974 | 2025-08-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c633e09a-7bee-3342-89ef-3d76b31a9afb | -3.8207 | -41.5598 | 2025-08-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31a58953-aaf4-3a2a-bf2f-dc8f4156da9c | -5.83888 | -42.94875 | 2025-08-09 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb750044-765b-391c-9b00-ffd3d3599054 | -5.08489 | -48.31532 | 2025-08-09 05:01:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c77d6ae-56cc-3749-99ea-124c8207ec20 | -8.90396 | -60.54166 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b4f77f-9071-3c4f-aaff-15491b833d60 | -8.9303 | -60.75181 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6adcca31-b46f-31c1-8de2-e2ec3319e2d5 | -7.05522 | -59.18029 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| cd07c1a5-df3a-3b73-976f-46799ad8d7d7 | -7.06577 | -59.16083 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4efec04-3f80-301d-9589-da2750056a3e | -9.05822 | -45.08086 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 535bb647-12d0-301f-9653-0c2735413697 | -7.07121 | -59.1957 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6df3934e-06b7-3aa3-85c5-d4baa989c15e | -7.07504 | -59.18179 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f12f3587-5a03-38c8-a6cb-eb18ad42b60d | -7.08804 | -59.19254 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2de3f0bb-fcf5-3555-8dce-6d6ac6ddeb68 | -9.51787 | -45.4325 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba60069a-bc57-33f3-a8b9-7d9d380c62ff | -6.59386 | -43.39486 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 264bbcb8-0b1d-3b04-ba86-6b716fd04952 | -11.77512 | -47.39302 | 2025-08-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 423cfcd0-cd0d-3f63-b7b0-d9461d7f97be | -7.06736 | -59.17382 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 200fdf09-e674-3737-82bc-0971d0dd7800 | -7.2448 | -59.99258 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f880e346-1d06-313f-b7ca-71a31ebcc18a | -8.59421 | -62.6548 | 2025-08-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2415eefc-b731-30e6-8810-7a8804bc30d4 | -8.93042 | -46.73841 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cbc6fcf-1799-3551-a99b-52258ae77eb1 | -7.07255 | -59.18741 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| dd03bd63-c92b-3fc0-8e03-59b387106796 | -7.08583 | -59.1836 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 2ed4f23a-be4e-3b73-99b6-a3bdb7c09668 | -9.93943 | -60.48149 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 620fa775-d362-3723-8b17-8fa256c0b9ce | -7.08792 | -59.17112 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| d8733a10-2c46-34e0-98b6-70458d96ebe2 | -9.26008 | -60.77718 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3315df66-6491-30f3-b49e-9630cc679608 | -7.08861 | -59.16697 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7b02efed-93b6-35db-8bea-294f6937b8b2 | -7.07781 | -59.16523 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 1453cb8a-6363-3a1c-89a2-71ec4f1b0b11 | -9.2647 | -60.77308 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 390344f5-fa91-3ef6-a8a6-bdd17e0c50e8 | -11.77377 | -47.40398 | 2025-08-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d69a846-3200-37fb-b654-fea0ca72de4a | -10.13503 | -57.78 | 2025-08-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e4452e-cf3f-39f6-9851-e4e48a2dedc6 | -6.09528 | -59.92759 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee494235-ae0c-3fcb-ad63-ddbb40cea0f6 | -6.59558 | -43.39846 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb5c882f-ed73-3d1e-979a-218fb2fb9af9 | -6.15724 | -55.80981 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc885470-f5c2-3798-868d-edf0810537fc | -9.93867 | -60.48598 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c9b97a-a6f3-3e3c-8b05-218278c6de95 | -6.60129 | -43.38962 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6d8b9e4a-1c30-360e-ad53-d754c6966987 | -9.86618 | -49.96237 | 2025-08-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1ca7674-7987-38b0-a453-8bd4deb6135f | -7.1694 | -44.39849 | 2025-08-09 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ba589e6-db95-35bf-b845-c56b7779db17 | -11.25129 | -50.18939 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23a70da0-3dd4-35fc-a539-53dee21f12ec | -7.07548 | -59.19217 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af76cd67-50a1-3e8a-8e42-2a902afe5b6e | -6.17227 | -58.07108 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36a5b03e-1d8f-3ff5-b698-d82c5603ce1c | -7.07226 | -59.1984 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0d5f34d-bd73-3161-9679-6529ed12b689 | -8.92972 | -60.73197 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ef6181e-2a00-3fd3-8aa3-be064852bff8 | -7.06041 | -59.19386 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0d9ae2b2-3a45-3395-9e38-1f5944b108bd | -6.87639 | -59.83001 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 127a14bb-c65e-37a8-addc-12d941b3beda | -7.09234 | -59.18896 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 37ccb979-5ab6-30fd-8d7d-be69e54038ba | -7.07096 | -59.17439 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c7dca2a5-9e0d-3f98-9f62-5215abfb07d5 | -8.93192 | -60.74221 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8f657470-56f7-38d6-98d4-69eae15a6708 | -10.60489 | -48.3654 | 2025-08-09 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f8b17944-8525-3843-a54d-846cd64bf75e | -10.12306 | -57.7742 | 2025-08-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52c40e8-e91c-393c-ba5b-191019fe1824 | -7.40598 | -60.00587 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a8858c4-2d96-391c-97ee-98f0770dccc4 | -7.3925 | -59.99445 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86218cba-6471-324e-a060-85787fd2ff11 | -9.9297 | -60.49366 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebbe6867-dc2b-3be4-8d62-ea50a3aa8ad0 | -7.39999 | -59.99567 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9fd5067-285e-3b37-a070-36bd1d3508ee | -7.07163 | -59.17025 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 27794feb-9c24-3c87-aa5a-a8bcf5526613 | -12.56064 | -47.10597 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d38c9993-fa75-3cff-a4b1-4e7180c2438c | -7.07712 | -59.16937 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 83680a0f-dc75-327c-9cfc-29b59fc19db4 | -7.08017 | -59.16309 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 39669a3a-6d42-3184-a8f3-fb116cdf51ff | -7.06401 | -59.19446 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 06848f1f-e3b5-39dd-a041-57459e423d77 | -7.09164 | -59.19314 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 938cb898-3e8b-3944-96d0-5f0675173e9f | -12.56403 | -47.12574 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 95af9576-9f01-3c6a-9d9c-0440c888ba1b | -7.06962 | -59.18265 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| af4226e5-a3bd-3c17-8231-caa86b503560 | -13.06475 | -43.83863 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3496537f-6053-396f-aceb-4485b62050ce | -5.90337 | -57.7128 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a673df1-acd0-3282-ba3a-4b314d76a223 | -6.13895 | -42.97445 | 2025-08-09 05:04:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 701c0ab5-e8fe-36a1-942c-e6af1ba107a5 | -7.09455 | -59.19791 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 39a9b14b-83df-3a2d-b142-7cdb9e48882c | -7.05748 | -59.18911 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bb6d8f4b-728a-34aa-bbd3-16dc8c562f78 | -12.6086 | -48.10693 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8856de98-57e9-3c13-bf30-34ef3f139d51 | -7.04892 | -59.19629 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ce04661-c91b-33c1-9f4b-7bfd7ffcd2aa | -8.92101 | -60.76006 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e84f530f-400f-3318-9865-cdf23861aaf1 | -12.7124 | -47.79337 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72636ef8-77c2-3581-b412-39971f7e7d0b | -11.31821 | -55.22457 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 878b9d6e-2faf-318b-9bef-e481441678a2 | -8.05251 | -46.32931 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd4cd6d8-23b5-3c45-8527-d8c311c63e25 | -9.5503 | -62.72392 | 2025-08-09 05:04:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a726bb1-99e2-3eff-bcc1-e3ffa1aef5f5 | -5.344 | -55.90401 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43daecc3-c1d2-394c-8296-3ea27e4ab1b0 | -7.0821 | -59.16167 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 026e30c9-55bc-31a1-91b4-970f47e7cca2 | -7.07188 | -59.19156 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dbb66960-0e97-3526-9816-184c80c1aee3 | -7.24856 | -59.99319 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01f88617-5fe0-3885-8ad8-8230739b5f2b | -10.00448 | -48.12941 | 2025-08-09 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c80911ab-8c31-310b-810c-e13c4b54f42b | -7.25994 | -44.32006 | 2025-08-09 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6778cef7-a85a-3e7a-80b6-cd3ecb5cb634 | -7.1115 | -46.10447 | 2025-08-09 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 528f22b8-9108-3caa-9674-2b957c70f1ac | -7.0687 | -59.16553 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2030288f-58bf-3274-b304-f2c9da1d1d12 | -6.60197 | -43.38445 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c93ef29f-547c-3420-9a03-477a499c3ade | -6.60329 | -43.37424 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba8f88c4-013e-3072-810e-346838b953f4 | -6.09245 | -59.92434 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ca7b8d6-719a-3546-a442-b0c7fcbc4a1c | -12.49552 | -47.50562 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12df2319-58f1-384a-a832-78e462b60346 | -9.93561 | -60.50396 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c5a6dc-feb8-3921-8ec6-c262d376a07d | -7.46627 | -60.41031 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83d3b3d7-557a-3f47-8719-4e9da338b765 | -8.9281 | -60.74155 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d91d15e7-5ac6-3ad5-916a-b7398214f2c0 | -8.92043 | -60.74024 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc63467d-2771-36ba-ade5-da45958c4b77 | -13.07063 | -43.84052 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccb4d69f-72b3-366c-85ef-de7042695626 | -10.68327 | -56.55416 | 2025-08-09 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bed9310-35f5-381a-9996-eb006fd059ce | -9.05764 | -45.0853 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4dedc39b-4b98-3bd7-9346-2178afda6e6d | -11.93234 | -44.54785 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 991f7c84-c999-3e71-8991-6e9d38afb33a | -6.15448 | -55.80584 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1228610-ba27-3b92-aad4-6d140544668c | -12.40461 | -47.78468 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e7a4a85-f132-34ba-8733-f217b792669e | -7.05095 | -59.18383 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69d57ee6-ad2a-38fd-b50e-2675db17fdbb | -7.25958 | -44.65804 | 2025-08-09 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e0c324f-4957-3f45-bc5a-d7a5505ec3fe | -8.8666 | -47.27632 | 2025-08-09 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04b7fdfd-970a-322c-bcc7-43dbe1a6bfa7 | -8.05771 | -46.33332 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf3a509-af49-33c7-a483-4032b029ad50 | -7.0532 | -59.19269 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f58724d-d4db-3d83-ae9d-c4a758c5990f | -9.05767 | -45.07809 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |


[Clique aqui para ver as próximas entradas](README25.md)
