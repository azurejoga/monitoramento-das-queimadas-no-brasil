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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e027671-7890-37cc-bb3c-40ed32e68b3d | -11.2259 | -50.1807 | 2026-07-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8771a17d-b878-311e-8c24-7244fe4b7774 | -11.9641 | -50.3747 | 2026-07-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 443f4f15-2c3b-333e-9458-d81df91d4d75 | -11.2449 | -50.1786 | 2026-07-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 785b80da-4302-3a0f-8f57-a274be43f80c | -11.9451 | -50.377 | 2026-07-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 75c84f8f-7851-3fa8-a684-bbad27b7ad54 | -9.5277 | -47.1187 | 2026-07-23 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 15d8795b-11ab-340d-9599-c1f8711554c2 | -12.3833 | -50.3888 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 465521aa-0669-3fea-99a4-b4a35d98f8f6 | -11.2449 | -50.1786 | 2026-07-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 303.6 |
| 73e7c5f7-b684-3592-bf35-6ee9c7770c1f | -11.9832 | -50.3725 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2adb15ad-4ac0-32d2-86c9-a3583716df4b | -12.4021 | -50.408 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d1160f67-9da4-3637-983b-cf6f49c86a4b | -17.0609 | -45.043 | 2026-07-23 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 466cf316-3e78-316a-b5cd-29bd4baf1f2f | -11.9451 | -50.377 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 777fa9e3-44c6-35b0-accb-3ecd83135828 | -11.2259 | -50.1807 | 2026-07-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f03a119c-f142-3c1e-bc91-048cc7e7008f | -11.926 | -50.3792 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 06687f9c-d115-3943-a108-9eb2adcfe67d | -12.4024 | -50.3864 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| eef9f2ed-deb0-306e-bef8-ca7b784418f3 | -11.5758 | -48.4028 | 2026-07-23 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0b9846be-c7b7-39ab-b142-a017c997a13b | -9.5277 | -47.1187 | 2026-07-23 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7c134b9b-cb32-3b8c-8310-b650ceaea075 | -11.9641 | -50.3747 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 35243f6d-8d79-3126-b796-5e41b92eca0d | -12.0404 | -50.3657 | 2026-07-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b14135a4-b044-31ae-89e6-a6f542e95c94 | -11.926 | -50.3792 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| bcf768a4-23c5-353b-a35d-2390db7b52f9 | -11.2259 | -50.1807 | 2026-07-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 99f146b0-9c45-3a67-9793-5b0f574bad50 | -11.9641 | -50.3747 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| dd14858b-e6ca-3bfa-a21f-6b7d2dc3647a | -11.2449 | -50.1786 | 2026-07-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 247.8 |
| b5f8662d-c5e6-3953-895e-765f435c5d03 | -11.8879 | -50.3837 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b3eb6d78-aeb0-3d60-a8da-62a6139a861e | -13.3746 | -54.2952 | 2026-07-23 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| fbb72bb0-c97d-3f01-afd7-04eaeba4e1e5 | -12.3833 | -50.3888 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 93956277-400c-3442-80e3-6bee8f590476 | -12.4021 | -50.408 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f22979cf-626d-3338-8503-7386ee9b0fe2 | -9.1752 | -59.0744 | 2026-07-23 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 126b6070-54b2-3032-8d65-14ffb2028670 | -9.5277 | -47.1187 | 2026-07-23 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ec47fb9e-965b-39d6-8bd8-0f3cb15f6041 | -11.9451 | -50.377 | 2026-07-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 1b745fdb-ba27-3b7d-ac03-d26a3ffd9031 | -14.3117 | -52.0889 | 2026-07-23 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b23537e9-9391-3184-8603-114d66b069a1 | -11.9451 | -50.377 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| d785a54d-607a-3ebc-a8d0-05844b561d0e | -11.926 | -50.3792 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 99afa973-9c2b-3f87-9211-f3ecfee5dc92 | -13.3363 | -54.2993 | 2026-07-23 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 33e10485-0672-38c9-b041-c115df08dab8 | -11.2449 | -50.1786 | 2026-07-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 273.1 |
| d1116c7f-0f84-36e0-b65a-7bacd4e79818 | -11.8879 | -50.3837 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 815482bd-a666-30b2-a915-c84d15a5dd7c | -7.6009 | -44.4722 | 2026-07-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 38fddfa2-24d9-36b5-b490-49cc3946fe68 | -11.5758 | -48.4028 | 2026-07-23 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4ab31dcc-c033-32db-86a2-a377eb8596db | -6.0334 | -47.6672 | 2026-07-23 14:40:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| edcea73e-8340-3976-add5-c3ead4f831a6 | -11.2259 | -50.1807 | 2026-07-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 72c56fa1-dc5b-3da7-8e6a-9fbe0880e602 | -11.9832 | -50.3725 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9c408b79-2ab2-3875-af54-1a381336567e | -11.9641 | -50.3747 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 3c01f83f-2239-33a1-b8a8-7f769aa0c22a | -12.3833 | -50.3888 | 2026-07-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 23549421-eae8-3c14-952d-84bf712835d4 | -12.3833 | -50.3888 | 2026-07-23 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| fb55fc5b-9c83-30ef-9180-9529cf36aa42 | -13.3555 | -54.2973 | 2026-07-23 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 3634ce2f-4bdd-36be-b38a-b4d2c1004b2b | -11.2259 | -50.1807 | 2026-07-23 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2fec4f3f-bc13-3255-95f7-a0e0239c8477 | -6.0334 | -47.6672 | 2026-07-23 14:50:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9bc90d89-7f57-3d84-9188-75956043e1d0 | -5.7613 | -49.0895 | 2026-07-23 14:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2cd1ba9b-a771-31c5-ac49-c8925415743c | -12.4021 | -50.408 | 2026-07-23 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| e2cc2247-db93-3048-9981-78dfa3f99b51 | -11.2449 | -50.1786 | 2026-07-23 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| d0faef85-8cd1-3b72-8139-804189c65849 | -14.3117 | -52.0889 | 2026-07-23 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 42e2911b-798f-3191-ba35-604ae72cbf90 | -12.4024 | -50.3864 | 2026-07-23 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 2caaf4f1-8f29-3a32-ac77-ff842cbe5584 | -12.4048 | -50.2355 | 2026-07-23 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8e502d27-8578-3cc7-9a0a-8a6c7659aa2b | -13.3746 | -54.2952 | 2026-07-23 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 938d2639-694f-3e1f-a11d-739493daf69c | -13.3552 | -54.3179 | 2026-07-23 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 74c31678-34da-349a-84e3-ecf2e1bd09d0 | -13.3743 | -54.3159 | 2026-07-23 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 57dbc486-7224-3596-9f41-3f06542ccf98 | -11.9451 | -50.377 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 29bb3ccc-3a74-3e86-83e2-6bdc0d9348a4 | -11.8879 | -50.3837 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 597ef10b-e673-3442-be54-422add81f2e9 | -5.7613 | -49.0895 | 2026-07-23 15:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b9864c87-64dd-31f9-8f02-bb7ae2c5e68f | -11.9641 | -50.3747 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 8a56292e-3690-3f10-a751-6a9d88b5adcb | -12.4021 | -50.408 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| f949ec69-748b-388e-8e0d-0076f3f92e52 | -11.926 | -50.3792 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| ccdcca84-ea61-3b3f-a036-3bb0bf70dcc6 | -9.4724 | -45.6433 | 2026-07-23 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ab796239-73a7-3e61-ac95-045a45b96923 | -13.3169 | -54.3221 | 2026-07-23 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 7305810b-4499-324a-a8f2-f7156908a171 | -14.3117 | -52.0889 | 2026-07-23 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8e84175b-59a8-3b52-8176-bd6cea576edf | -13.3555 | -54.2973 | 2026-07-23 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5e045265-c640-395e-bade-3321c8ba10a2 | -8.8026 | -49.3748 | 2026-07-23 15:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d89da61c-003c-3e50-a70a-9e3cb8748417 | -12.3833 | -50.3888 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 77e76c85-119a-3d1a-b656-cfd47e6fc53a | -13.3746 | -54.2952 | 2026-07-23 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c9b8898a-adf1-3ec5-8fe9-ea5f004c34e0 | -9.4535 | -45.6455 | 2026-07-23 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ebc4f4b4-0c77-3f74-b7c2-3246480a85b0 | -12.4024 | -50.3864 | 2026-07-23 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 002e051d-7b8d-374c-ac0f-540a0b3539df | -11.2449 | -50.1786 | 2026-07-23 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 885106b2-0cfd-3178-92cf-27cfe6d3ebd0 | -12.4024 | -50.3864 | 2026-07-23 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ef41d27d-7c5e-3f01-9880-df1f1523aa79 | -13.3169 | -54.3221 | 2026-07-23 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 36751c5d-c893-3080-8873-15bac677b2fe | -9.1235 | -61.0653 | 2026-07-23 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 232c04de-68f3-3c29-93e9-421d5a5b3bbd | -11.2449 | -50.1786 | 2026-07-23 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 56f6c00d-cc7e-334d-957c-c4650285c0b6 | -5.7613 | -49.0895 | 2026-07-23 15:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 3e48acde-0377-3624-ad03-52c24e1b9ffd | -15.7254 | -48.2299 | 2026-07-23 15:10:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4edfae57-dfa0-3513-a5a9-55a04e40ef6a | -12.3833 | -50.3888 | 2026-07-23 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 94381015-faf8-3711-8747-e493b0adc5e3 | -14.3117 | -52.0889 | 2026-07-23 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3453e2e0-2587-345b-ace7-894a1102023b | -12.0404 | -50.3657 | 2026-07-23 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b3461487-6d84-3758-8bf3-f78b7ff2d1c5 | -9.1234 | -61.0844 | 2026-07-23 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 132eabee-0931-3017-a349-3014909445d2 | -9.1235 | -61.0653 | 2026-07-23 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0da80fa3-b75a-3891-9abd-4e70bccdfceb | -13.3743 | -54.3159 | 2026-07-23 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 5fae7c38-086f-364b-83ba-1394509ca1fa | -14.3117 | -52.0889 | 2026-07-23 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| fd2f87ef-1513-3003-8de2-f6207dd0909f | -12.0404 | -50.3657 | 2026-07-23 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 82350864-7ee5-3f77-a11f-df2e230ccac7 | -13.3746 | -54.2952 | 2026-07-23 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9f85a927-f3d1-318a-8d7e-cbc3ef79f7c0 | -13.3935 | -54.3138 | 2026-07-23 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7a36e7ce-0047-354a-be44-2546b4f9480d | -9.4724 | -45.6433 | 2026-07-23 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2737a1bf-cf29-3b0a-baa0-f797e9184e50 | -9.1234 | -61.0844 | 2026-07-23 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| baee0444-414a-382d-8c1f-e501a5217b20 | -12.3833 | -50.3888 | 2026-07-23 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b98d8d47-f3cf-334e-b71e-ba6bd95991d7 | -11.2449 | -50.1786 | 2026-07-23 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 9762d342-bfcc-3417-8140-e94cc74d32a9 | -10.6527 | -46.6078 | 2026-07-23 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7c54c346-5e17-37d1-8f4f-262c394d096a | -12.4024 | -50.3864 | 2026-07-23 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 10523966-b4c5-3f3b-b789-346fe1e22141 | -15.7254 | -48.2299 | 2026-07-23 15:20:00 | GOES-19 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b69f3c7e-c7f0-3f6b-a0b7-e943109fba78 | -12.4021 | -50.408 | 2026-07-23 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| ecb28a54-9e4a-3e7b-96c8-eb75989ad2c2 | -14.3117 | -52.0889 | 2026-07-23 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 63c7d8d0-dac1-3b92-8e59-2773b56bb039 | -11.926 | -50.3792 | 2026-07-23 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 96253036-7ef6-35dc-acb0-b10b4adbfbce | -11.2449 | -50.1786 | 2026-07-23 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1d03d085-fa23-3fb7-a9fd-515edb5dd838 | -7.6067 | -55.2798 | 2026-07-23 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9c92ef97-2629-3dd5-993d-0b6229498939 | -12.0404 | -50.3657 | 2026-07-23 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |


[Clique aqui para ver as próximas entradas](README21.md)
