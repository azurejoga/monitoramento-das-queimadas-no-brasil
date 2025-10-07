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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b44ae91c-771d-3b9e-8734-3676543ac101 | -6.40011 | -43.59209 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98e6a887-ecbf-3fdc-9e72-4cef7349be49 | -6.08104 | -42.54754 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cc942ef9-6d30-3116-8a35-3e41b2967dc5 | -6.75714 | -42.23275 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b85030e-a5b5-3da1-a4a2-6be0a816bf58 | -10.41768 | -50.3936 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd65a77-3d33-3bf7-bf95-d06d880edcbf | -8.87765 | -47.67809 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b564c602-2b6d-3404-9ed8-071932cfc872 | -10.88054 | -51.02932 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 5725a4e0-48ff-39b9-aaa4-e59ec174ea37 | -5.25208 | -46.56249 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a2c0853-0132-3c53-baaf-e9e42de3ab24 | -4.68833 | -49.49895 | 2025-10-07 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcb1b328-223b-3110-a8d2-c3a75567f63f | -5.90928 | -42.51327 | 2025-10-07 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e30048c3-aa44-3d17-9192-11a84e6f1b93 | -10.94954 | -51.18361 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d674688c-e349-3bc8-aa5f-691e52df5a02 | -8.91288 | -50.60411 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecb33184-195f-36c0-8e63-b7665e9e7a25 | -8.61551 | -44.92694 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7aa560e-4692-36f4-973c-30994f24c3ff | -10.30732 | -43.43802 | 2025-10-07 04:08:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e73794b-0940-36f8-92f4-a209314e497e | -6.72175 | -42.80176 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e38cd61-1fa7-3d1d-ad1a-ba75d4365cb8 | -11.03067 | -50.9183 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fef6a027-73df-3272-a9ca-ca5350699bf2 | -11.95489 | -45.49076 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1346ed4b-7e7d-3f1a-a814-3527e64a34cc | -10.41879 | -48.09524 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 465a8281-9b16-3727-825a-12b93e90eaa7 | -6.13991 | -42.66963 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3007a06a-dda3-3466-8a87-8c597a3c0d52 | -7.67813 | -42.58728 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65b19417-03c3-35ce-8223-8e54ec06440a | -7.6886 | -42.41398 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1e75316b-619e-3c95-8a37-7c340e14cbe1 | -5.31354 | -43.09142 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13b80112-e36e-3421-837a-40942936c3a0 | -8.61263 | -44.92231 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8a80410-3cc6-3982-ac4f-586f53bd7404 | -8.52865 | -54.85727 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e11e9bc9-82d0-3928-b7a8-46da7a5671e0 | -11.8654 | -44.9388 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9476d8a-83a1-36ba-b2e9-5dce71f4d8bb | -8.18313 | -50.30141 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2cc7c0f-9511-392d-be88-9297fa7f1d15 | -4.69177 | -45.8414 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8a79afbc-b03c-3bdd-af32-9c0bcc143511 | -10.58519 | -51.47064 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a94780ce-28a2-3bfd-ba50-16021addd7c0 | -6.36446 | -42.8651 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4868f4c-fba0-3567-91ca-031487748b34 | -8.61197 | -44.92635 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 072fb34a-bbb8-3d8c-b70e-55c50c014b36 | -6.71823 | -42.84169 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 875be51c-b2d9-38eb-833b-02bbad459e68 | -5.92839 | -50.21524 | 2025-10-07 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f30c80-1eaa-3d67-801d-ffef073e1a21 | -11.12208 | -47.2105 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eac35e5d-d004-3302-9c66-05f54c909814 | -7.6484 | -43.89336 | 2025-10-07 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7e88149-661c-33f2-bcd1-421bd90b6f2f | -7.1497 | -39.72166 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1223faf5-9bfd-3877-a0e8-5dc7a8d38a46 | -10.88053 | -47.22773 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfd4e9d7-a70d-3d98-9cb5-cb203b867834 | -6.69999 | -42.85273 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4faf3e59-b458-317b-b75a-ac89abe856f1 | -8.52494 | -46.24856 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60da1879-2842-3421-8cad-aac6e1b8f0d2 | -10.93292 | -44.25192 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c6248f0-130c-3e92-9c48-28e078a3b756 | -7.48215 | -42.62062 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a906bb68-76fc-3059-900c-cbfb91233908 | -6.24994 | -43.28025 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4228aa6f-47f2-32c7-b7ff-3e56a7ee05c0 | -11.94867 | -46.43693 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3b8febf-7611-3ff2-b75d-e804484c4ac6 | -6.71798 | -42.18041 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71dadb2f-91e7-3dec-89dd-6ceec406b9a5 | -7.80414 | -42.5649 | 2025-10-07 04:08:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43032d4e-4372-30f3-a3f9-bee0072920f5 | -11.93912 | -46.44858 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21410a91-f2b2-394c-acfe-112bd067e6e1 | -5.25618 | -46.48853 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47e57f0e-257c-3b71-9419-7ca55b3200c4 | -10.27263 | -44.35741 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cb096c0-d981-3804-8ef6-49312e245a5a | -5.80547 | -46.5548 | 2025-10-07 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35be2b69-3d97-3323-8457-1888351985f0 | -8.541 | -46.24605 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8fa50793-f378-3d0c-ba3d-f6de5ab874f3 | -6.72832 | -42.8215 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1978ddc8-e64a-3301-9837-9b0f2f2f9fd1 | -11.12511 | -47.21604 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa3d74a4-0593-39fb-ac2a-31356f81b086 | -11.38763 | -43.49537 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aca156c5-37e0-320d-9945-fd951ea2778d | -5.59556 | -44.42839 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dd42eab-085a-3e75-b547-0556c27c9265 | -8.46429 | -47.2116 | 2025-10-07 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa4a1878-3d44-3d1f-bdd0-b3343a91767e | -4.68883 | -49.49601 | 2025-10-07 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8da63d71-f749-37f5-92f6-1f8e878df47d | -5.74741 | -44.98831 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b29ddec8-9ad7-30e9-81ba-a20e6e96c843 | -10.22959 | -48.18736 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 11f33de3-1307-3b14-ace7-0dade9539194 | -11.7304 | -45.37702 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05652364-d8d1-36f2-9113-450bace26f0e | -10.1868 | -45.5322 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a1ff952-43ad-32d6-b876-1c57483d4cdc | -6.23707 | -44.2128 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 735a3f73-2553-3fec-a0c8-089bb673410f | -5.87164 | -44.29582 | 2025-10-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61f47999-8ff4-3ccf-845c-cdbfb6057cf0 | -8.18813 | -50.30233 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f35217f1-393c-387d-aa1d-8e08da1afa35 | -11.22814 | -47.76704 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86e86902-be98-31cb-8e82-f67a1f581534 | -7.79089 | -42.60575 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e090bcc-1dbd-3867-a5fc-dc955da6a082 | -5.74373 | -44.98769 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f5a118f-ae81-353f-a7dd-619795c4e57d | -9.6888 | -48.39433 | 2025-10-07 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe4cdbe2-d40e-3275-9df2-c7a36777b80d | -6.87025 | -46.07158 | 2025-10-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9887b76a-a1d8-39c1-8fc0-3d7aff78e42e | -6.72327 | -42.83161 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a824bc7-f962-3138-98e6-402ba862139d | -11.1204 | -47.22011 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 99e09b73-0e08-3c23-9467-d028f617210e | -6.14047 | -42.6661 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e4cf1ac-a0fe-354d-a03f-851f5fe6ffdf | -6.98318 | -42.86897 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 679f0c42-600c-32b5-b016-be6e0e6bc432 | -5.64856 | -43.61008 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ca522b5-e4c4-336b-a5fa-2571d0e7eabd | -5.88289 | -42.55243 | 2025-10-07 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7e7911d5-ad1b-3dec-8d4f-17a92eb18ab7 | -6.32978 | -41.61642 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53a89827-988d-382a-9d85-80d2fd912d67 | -11.80905 | -45.04407 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24c7282d-0a7a-31f9-aa4d-8a5fc761ef38 | -6.09345 | -43.09156 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c6ff7620-5fa2-3736-b3f3-78cda8756bc3 | -5.42729 | -45.99845 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf6910c-fb2e-3a1d-b9d7-3f7dae039a5c | -12.21617 | -44.25288 | 2025-10-07 04:08:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b76b1d9f-454a-305c-b340-f54a2e7b897a | -7.06339 | -42.76991 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9561ca11-0c15-346a-98b8-1bb3f6e7675d | -5.25534 | -43.10123 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7e0805d-4aed-3b10-9b5f-80870adaf661 | -6.16274 | -44.08775 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2147b256-b247-3ac9-bb42-bf8594e37686 | -5.22926 | -43.79658 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 652eac43-9019-32e6-a8b9-b55fc6c67e7d | -7.63317 | -43.06409 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 301cdcf0-2fa9-336a-980a-5d3418eb3a7b | -11.15913 | -47.94981 | 2025-10-07 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52839624-6430-3e6b-b7c0-7b9f468f4d58 | -9.40593 | -49.36871 | 2025-10-07 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b05bd61e-8325-3432-a4a6-9f07ec062fa7 | -10.38413 | -50.30367 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c11630c2-e8e3-336c-af30-540fe2755ac7 | -6.08589 | -43.46997 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0051e7e7-6724-3a5b-9ed9-60a142185d16 | -11.2275 | -47.77082 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c627f1d9-7465-3863-8949-b03dca5171c7 | -8.52653 | -46.239 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2c3f9cd-bcbf-3ee3-9de4-07ecfcd66adc | -7.41943 | -41.13032 | 2025-10-07 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 628f6a19-f99c-337d-a33f-5345d2aad48a | -6.73064 | -42.1646 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48fcb0e8-f20b-339d-842e-c14010abf8be | -7.78208 | -44.19839 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8e4b365-df19-36cf-9f86-d75afd8b1a22 | -11.80938 | -45.1273 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d43b940-dc84-3cb6-a66e-f94d356e489c | -11.9537 | -45.48204 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cf81868-cf91-31c6-b401-992396ddd166 | -6.73009 | -42.16807 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 674ca394-7e2b-3225-8f5c-961f730fd7b7 | -7.04227 | -42.75507 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eda04200-0693-381a-a2b9-4a80fd90c0b7 | -7.06616 | -42.77395 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 753ba653-de03-3963-827c-c4281280d103 | -6.41479 | -43.60992 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d04438aa-efc7-3d86-b2af-dd3427701688 | -6.45984 | -44.58466 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27d0f659-fc39-390e-aa78-120e011aca5a | -8.53415 | -46.2402 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| b819c0bc-f07b-3cba-ab43-1593162dcfb3 | -8.5432 | -46.25646 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README30.md)
