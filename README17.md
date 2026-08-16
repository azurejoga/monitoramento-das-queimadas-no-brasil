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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3439f9f-98d7-38ed-96d4-3bf200d887b6 | -11.88844 | -50.23064 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 157ddfa2-ca53-34d6-bf8e-314ee67b02d4 | -6.61107 | -59.00094 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e7cc83-d5ff-3e15-9214-87b103ac54df | -3.73834 | -59.32971 | 2026-08-16 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a6f2870-10d7-3d3d-bbdf-1a7f6e89f5d1 | -6.83517 | -56.44856 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b139a649-6c56-3fc7-86fd-6e1928f88037 | -7.46414 | -55.30819 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f6400e8e-546a-3a5a-a193-6bfbe0efa0b0 | -8.46534 | -45.42566 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46171cfd-ef74-3ce1-b0aa-b07a5ca10c40 | -7.83966 | -61.34868 | 2026-08-16 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab4b126-a8aa-316a-a693-fb5f29bdaedf | -8.97582 | -60.52169 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 97f7330c-f102-347a-b9f4-d5d17d310c69 | -7.63083 | -49.51659 | 2026-08-16 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 825667af-4a9f-3589-ab4c-09138f0fd8c9 | -12.46974 | -46.65532 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95b7b649-f015-33b5-9da5-485847f6be10 | -6.60086 | -58.99577 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46ce2ea7-0ae4-3a89-9cec-407d1f947910 | -8.98079 | -60.52681 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 07d0a029-e358-38d4-953a-cceca8d4bfaf | -8.60136 | -54.69371 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6bbaa92-fcf4-3ac2-9951-7265c402d334 | -4.79391 | -49.39157 | 2026-08-16 04:40:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0bb889e-e649-38da-8f24-b80e6a0343b3 | -10.52123 | -44.85688 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dc96efc2-e302-30c1-b6d6-36ec532cdf6a | -8.10554 | -51.65942 | 2026-08-16 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12271972-2299-30f2-8e34-1dc7cf31e24a | -8.80155 | -45.79129 | 2026-08-16 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6e452c1-1e12-313b-8905-2d5c9b615b7c | -6.58811 | -58.99318 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d785403-707e-3d50-aee8-d683be5a2616 | -11.89374 | -45.96217 | 2026-08-16 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e47f5f6-2748-3dbd-9c5d-5fe7c1e7a73d | -7.40826 | -60.01186 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb430710-3bd1-36ec-8974-28de09418d55 | -9.47419 | -60.51112 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6e23fe6-82e8-3979-bd43-95ce63bf3914 | -11.84095 | -51.79263 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a46e712-2292-3c7d-bcb9-37a493487722 | -11.82647 | -51.79757 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4c7c0e-bb10-3cbf-aba8-04f49e2b278a | -6.5429 | -55.17562 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e5c9990-8958-3f33-8e66-280ba62e5194 | -6.62935 | -59.05466 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aecfdec8-7a57-3da2-acd7-eb62ea24d433 | -5.75978 | -47.3457 | 2026-08-16 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e6ce0f-b2b6-3818-98ec-c00529d0c7f2 | -8.43174 | -62.68549 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3d99a45b-1d08-3337-bce1-78a498251381 | -10.27726 | -48.29332 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 39beddfa-b477-3e16-8811-3f9737a8df50 | -12.45893 | -46.64884 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d13f09c2-7e23-3188-ae13-a4c8dafc7d97 | -12.01341 | -46.43223 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9246fe22-ef48-388e-ba7e-3f3e35fe25be | -10.26924 | -48.29988 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca69994c-f78c-34d1-952f-6c765411b96f | -8.59044 | -54.68673 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41328376-a32f-35f5-b60b-e2ec68f24379 | -7.44085 | -55.30859 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b747ddbd-ba6e-3f88-a639-05e8b5d600c1 | -6.62583 | -59.04308 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98d74c70-5111-3a69-a143-b04e472eacbf | -6.9623 | -59.28845 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fc68610-8f2e-3c1f-b64d-e0f181e68a76 | -12.47223 | -46.66542 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98501f24-ef26-366e-ad8a-cbecb778e85a | -6.31295 | -43.61516 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 623781fd-6d28-3278-96e2-b74c008551c5 | -6.29818 | -47.74818 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47ac806b-0538-31f3-ae32-c1d60bb7ebc0 | -6.85103 | -56.41768 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f1b1bd-0cec-3849-8659-72e2ab86facb | -6.42926 | -60.07141 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 808ca6c4-79f2-335e-ae5e-4f23e879b4b3 | -8.9545 | -60.57232 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a72dedc-4f69-308d-88fc-ceb21bdf4a3d | -6.37456 | -58.32409 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42672dad-a9de-311f-93e3-2eaa9df47730 | -9.14296 | -59.64817 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0658607-317a-3aee-9ac5-646141f8a3e8 | -6.86118 | -58.96563 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91062556-88b8-3a1f-8f3e-3439b49aec14 | -9.10653 | -46.38646 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73cde553-de4c-3816-82db-9d3b7c2c3d05 | -9.70655 | -45.77413 | 2026-08-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e9e3c19-fc3b-3cb6-a439-53418e8dd171 | -6.8585 | -56.42826 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6323ec1-21d8-3622-bbe7-1ed3baee5bbb | -10.25371 | -50.42577 | 2026-08-16 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84553d2a-9621-3c7d-a963-8a6cebb460eb | -7.00899 | -45.90891 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18ddab32-e8f7-3a19-aabc-dcaabed62db8 | -11.04804 | -47.25255 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf6084cc-d605-34d7-aa9b-4f2c4ff17cad | -8.95329 | -60.54702 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0665c01c-3428-3b57-abff-ce31df649f1c | -6.716 | -58.94127 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65624110-1828-301e-bb82-3e67b0f5856e | -8.60051 | -54.69875 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22a583f8-08d6-3d48-9690-d496bc98df41 | -8.35623 | -45.98089 | 2026-08-16 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16e518f9-775b-3307-9fa9-f354d467df10 | -6.60878 | -58.98273 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b541a463-3600-3c05-97cb-0d05c30e0bb7 | -7.00089 | -45.91225 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 182903aa-b0a4-33af-9ded-ef618921b2bd | -6.59893 | -58.99493 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ad782e6-7c2c-3fc1-ab41-f610cb8aaa03 | -6.96041 | -59.29922 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 030a549f-c101-3b87-a96c-eba4dbcac2c6 | -6.72079 | -58.93019 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1deeb577-3244-32a9-ae66-64efb57fb54a | -6.1321 | -55.81237 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec57e0a-e95c-39f5-a960-c5884a484baf | -6.70473 | -58.94243 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 548062c7-bc35-3542-9a5e-d3f815e9548a | -8.97082 | -60.5167 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a8e1fe3-d641-3afc-ab92-a2dc5737f8d1 | -6.93512 | -43.64236 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be209e32-33d6-3b0c-946d-6dcfea80ae46 | -7.55474 | -61.17923 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adbc62b5-a25f-38cb-9dc9-48c1333d28be | -9.09843 | -46.38996 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc3e8a9-6af6-3f81-a6f6-e8b08ba17052 | -7.21952 | -41.53649 | 2026-08-16 04:40:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 72a1c81f-58c2-31b3-8f14-16d889047ff5 | -6.86056 | -58.96907 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fea97fbe-fa1d-3627-a468-7732ab2e4b5e | -6.70235 | -58.95612 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df3d1f52-e951-3749-880e-af34d4349d27 | -8.95861 | -60.51863 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ccf409e-2690-3eff-b583-561d069e012b | -6.21301 | -47.73126 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8e2ccfc3-b952-3aaa-87ad-5127134c1c85 | -9.48873 | -51.64539 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 934e0dcb-ffb6-3e7d-92b1-f8289fadb8f6 | -12.00154 | -46.41864 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4315765-dab3-3561-84ad-1d7285f7af91 | -6.96356 | -59.28131 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3424cc46-1b15-3544-93c4-3ba1dd4d034e | -6.60023 | -58.99922 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 038e201b-4458-31c7-bc6f-566cafa69102 | -5.14037 | -50.84969 | 2026-08-16 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94fe0b87-38fb-3b70-92ef-cfe53d8702c4 | -6.64548 | -56.43251 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69041444-348e-3534-8429-56d7db61e054 | -6.8366 | -58.97913 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9876ea0b-18e0-3bf2-bcff-b666581908a5 | -6.31178 | -43.62321 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a79dc808-703b-35bb-91d3-5ff19f61788d | -8.4164 | -62.65904 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67091d60-9f59-39f4-8823-e6556d452dde | -8.65981 | -54.75225 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 531ce049-7182-3274-889f-aa7c7fda15ce | -6.82974 | -56.43298 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbbc5548-4d45-33d1-9ffb-c6fd7f33bc25 | -8.97731 | -60.51367 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 427000ac-307f-3330-b14f-2b53bd4d82e5 | -8.89954 | -60.57594 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1a557c6-2b21-3255-bbde-3d511d111560 | -10.93902 | -57.11128 | 2026-08-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcbee020-a633-3078-901a-dbbe37b56de7 | -9.42611 | -60.32941 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1211c0f-d31c-3821-b4a2-a2b2635ca32e | -8.95222 | -60.58448 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1fa32e-bd42-384f-b8ea-62c3a6c9e8b7 | -9.47702 | -60.50867 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7406c99-21a6-31e1-a7e1-c3e06f5ebd69 | -6.54353 | -55.17188 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c63e0a18-7bab-332c-b1b2-ccc8b2a335f2 | -6.61357 | -58.98705 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2983a674-acb8-30bf-89dc-1c42d82114bc | -12.56854 | -47.85487 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ede7267a-9817-33b1-a3e2-c7cda025449c | -6.84047 | -56.44471 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63a05f55-73ae-3a39-b016-2c944044ffca | -6.39749 | -47.34716 | 2026-08-16 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cd0056b-9ecb-3cf1-8b76-0337dfc5a0d5 | -6.9724 | -59.01001 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2263637a-cfd4-365b-be02-56badcfb9e17 | -6.24587 | -55.62214 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e533b03-978b-3a6c-a468-e1d751a52cd3 | -6.86473 | -58.97676 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 543dc76d-d58b-30c8-b63b-2083b383c495 | -9.20779 | -59.67132 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 129c4887-da65-32d7-b06a-0cab46cc2586 | -6.61788 | -59.05632 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6eabb0c-7ffc-3ce7-994b-4163589050ad | -12.03611 | -47.81629 | 2026-08-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 286d43ce-7b12-3919-8f3d-6920f04c2141 | -8.96706 | -60.53687 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a44f93c9-87eb-3618-8669-bab1d8c5161d | -11.8768 | -51.94954 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
