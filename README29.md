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
| 8a39f949-5b8b-3818-832e-ce3108be7b74 | -10.57098 | -46.06983 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8ff8fa46-05b3-337e-8f1f-b5f57d8013dd | -10.56812 | -46.04929 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b731d09-9f31-33c1-808a-2e70a4e792bf | -10.56682 | -46.05568 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b262cd01-9013-3139-b852-88ada5cb521b | -10.56668 | -46.04897 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 48550a04-27b4-3f61-9add-7a7de0685ed3 | -10.5655 | -46.06214 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 280923a6-7e60-3c14-a68c-e140d00ef9fa | -10.56541 | -46.0554 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a5a26ba-f674-3211-802e-68679a340dc8 | -10.56413 | -46.06187 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 3fc84c32-6829-3dda-96d5-7a384701babd | -10.56132 | -46.04814 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| aadc3207-8bbb-3ede-b1a9-561da302b724 | -10.56 | -46.05462 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a45d2b38-49b7-3f56-ba99-d7a7e17d24cc | -10.55988 | -46.04779 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a0e95a5-4c04-3507-95c4-4ec0e4e546a0 | -10.55867 | -46.0611 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 43ca3912-2d55-3102-a702-354b47d5c44e | -10.5586 | -46.05427 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fa09c66e-250e-3adc-bb5a-c44edb8ccc58 | -17.28836 | -39.56525 | 2024-09-28 03:30:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68d93c1f-4756-330a-bd19-76b88e9fc8e2 | -18.31212 | -39.92478 | 2024-09-28 03:30:00 | NOAA-20 | PEDRO CANÁRIO | ESPÍRITO SANTO | Brasil | 3204054 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6b2b60b9-6aeb-3d07-8cdc-cf3fe8666edc | -18.03922 | -39.92754 | 2024-09-28 03:30:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76db7160-3059-3a31-8645-5e948da45b80 | -13.33734 | -42.05811 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb2ffc84-4d4a-30eb-9972-6624dfedea0a | -17.97426 | -42.29714 | 2024-09-28 03:30:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 693496b3-cf6e-38e2-ab06-2978e01151ca | -17.92257 | -42.14074 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 05a339fd-cbef-3652-b5fa-91504258a31a | -17.91154 | -42.13519 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5c63579f-6a90-32b6-a273-0b85d500357a | -17.90689 | -42.1342 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| acbbd16a-1a61-3aaa-9f71-3f9a35aa4e6b | -17.88833 | -42.12996 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9dfa02fd-8d59-3805-af29-f7451b689f41 | -17.88652 | -42.13919 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54aeac5f-39aa-3777-af04-bcaa0a979232 | -17.88552 | -42.1443 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 99f91aea-7fe5-3d19-94ee-84b02ed1d60a | -17.88369 | -42.12893 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 482a2216-2eb4-3874-b40c-3ecbac85abf5 | -17.88186 | -42.13823 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ababd9c-d9ca-3614-ad68-08526a268f57 | -17.88086 | -42.14332 | 2024-09-28 03:30:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96fc816b-a89b-3b60-b31a-33a92c935a78 | -17.71132 | -42.32659 | 2024-09-28 03:30:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31063d22-d7d5-389f-ba47-6127417ec93c | -17.71025 | -42.33195 | 2024-09-28 03:30:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f959abc-2310-3680-b91b-03567b842dcd | -17.56286 | -42.35085 | 2024-09-28 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 799dc2d6-aa3f-374f-8b02-42b7adcecfdd | -17.77894 | -42.81081 | 2024-09-28 03:30:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 585a33b8-398d-37c7-8338-2e5062e0af6e | -17.44062 | -42.61637 | 2024-09-28 03:30:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1625c5ec-b05e-395d-98c2-d101f54a148f | -17.43952 | -42.62187 | 2024-09-28 03:30:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d8025f14-be6f-363e-983a-da0138ad64c5 | -18.29292 | -42.53925 | 2024-09-28 03:30:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| acd4a5a5-d309-34f0-8109-72ff3586bc8c | -18.29281 | -42.53831 | 2024-09-28 03:30:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4d1dab31-3d83-30fe-a868-ed83afda6685 | -18.29178 | -42.54486 | 2024-09-28 03:30:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f04f1a22-7873-3a42-bf68-403948bfd08d | -18.29172 | -42.54389 | 2024-09-28 03:30:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c475d8e9-99f9-381b-a6d9-38fcfedae46c | -18.28708 | -42.54364 | 2024-09-28 03:30:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2ebceb3e-9348-3795-b4f3-797711fc7cbf | -18.07008 | -42.66143 | 2024-09-28 03:30:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9df82134-3404-3e6f-8099-65d0c1e415eb | -18.34199 | -42.18594 | 2024-09-28 03:30:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f898c513-e4d0-377f-9ba8-e09fbe8cce06 | -18.33205 | -42.18736 | 2024-09-28 03:30:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6348b4f5-38da-3998-82f2-caee5de413c6 | -18.28609 | -42.15149 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7b5756b8-b28e-3375-a5a6-5b0f43f5ea26 | -18.28517 | -42.15612 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7164b5de-ec3d-3310-93f8-a283d6dea4b5 | -18.28247 | -42.14548 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f8855c00-c53c-3408-80c0-aae72a6b1b5b | -18.26122 | -42.15531 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| facd368f-3aad-3e54-a4b7-9266c4aaf83e | -18.25879 | -42.15352 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fadcb056-fcb3-3cf5-8f50-e08cd454c568 | -18.25844 | -42.14513 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 30d5ee30-a4d3-3d01-a580-b7bcc4c8b836 | -18.25746 | -42.15004 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0681a8a2-6744-373e-990c-bdd7381bec6e | -18.25644 | -42.1551 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4286c262-41a5-3842-8648-b6562b3e0b98 | -18.25502 | -42.14816 | 2024-09-28 03:30:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 047057df-ac4b-3245-a7fd-676a0010fda3 | -18.13678 | -42.40335 | 2024-09-28 03:30:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| cd4cb890-981a-319c-a8c1-1bafa6bfbbb0 | -18.13571 | -42.40871 | 2024-09-28 03:30:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fb5c57bb-51ad-3cc5-b65a-800ae3167d46 | -13.37648 | -42.04451 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7eab8979-90a2-37b7-ba2b-1f0515703bb2 | -13.37584 | -42.04793 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bc0295e7-c90f-3d5c-ae59-0e1f952c0937 | -13.37578 | -42.0428 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1956d12e-b027-35b4-b1c3-4bbfe9f47b46 | -13.37516 | -42.04598 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b2e0896-7f3c-3446-bc41-c59d714e8d55 | -13.36956 | -42.05353 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e21ec83d-bd5f-3e41-863f-150ef2fac154 | -13.36894 | -42.05685 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3847151-dec7-3e6b-8792-6eae9ca76114 | -13.34795 | -42.05726 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bad0fcf9-e5a8-3754-bf17-8bac3689ace5 | -13.34297 | -42.056 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca503d46-f419-3f8a-b5f2-b2e5e6e4f377 | -13.3423 | -42.05953 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dbcd2fdc-2f32-38c1-8350-1646c89699c5 | -13.33861 | -42.05143 | 2024-09-28 03:30:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5d7bc21-6d72-32b8-a130-375947d97e68 | -13.01302 | -42.22087 | 2024-09-28 03:30:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d24016c9-9f1b-329e-9086-c223f68c9a1d | -13.01241 | -42.22411 | 2024-09-28 03:30:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74c5a7bb-ff7a-3669-88ef-6c84e871aec4 | -15.1089 | -42.46576 | 2024-09-28 03:30:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 89cdbd03-5b92-3fcb-a688-29df9809c9be | -15.1083 | -42.46884 | 2024-09-28 03:30:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4715628-bd65-3bb6-83bf-f89a11873106 | -15.10391 | -42.46468 | 2024-09-28 03:30:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15547d8a-fe01-38bd-92ba-7bc3f6ea9d23 | -15.10331 | -42.46773 | 2024-09-28 03:30:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dfa15554-847f-347a-9b23-29b5b13b29c7 | -14.73024 | -42.8785 | 2024-09-28 03:30:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fd8f0da1-4cb4-3f7e-bb5d-24f04d08ecea | -14.72969 | -42.87713 | 2024-09-28 03:30:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cd05fed4-92ae-3e36-bcd8-a8ab5fe877d5 | -14.72958 | -42.88176 | 2024-09-28 03:30:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fd49e943-af29-3813-abd4-7f58d33e965a | -14.72905 | -42.8804 | 2024-09-28 03:30:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cd50cff3-6d3e-3930-8c9b-fe68718ec46b | -14.72388 | -42.87928 | 2024-09-28 03:30:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb780943-bc5f-3b47-9754-07e21d810cd4 | -13.86791 | -42.62595 | 2024-09-28 03:30:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ad7f6b3f-9130-3995-a58c-c37c9d8e71e9 | -13.86276 | -42.62478 | 2024-09-28 03:30:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 021632a1-b528-31f3-abf9-59905710fda3 | -16.34565 | -43.69828 | 2024-09-28 03:30:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36aa64b8-be66-3bac-b6ee-e76c0e372682 | -16.26351 | -43.86827 | 2024-09-28 03:30:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd216018-6f7d-34c2-a401-90e319f5be7c | -16.26287 | -43.87141 | 2024-09-28 03:30:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dceb2db9-cfd4-321f-bd95-9bac2b62046a | -16.04224 | -43.61456 | 2024-09-28 03:30:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 324787fc-8034-334b-800a-303287e46975 | -16.03695 | -43.61341 | 2024-09-28 03:30:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0055ab0-ab7f-320f-a69c-870e18635fe1 | -15.51131 | -43.55581 | 2024-09-28 03:30:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9537637d-f168-3856-b8c2-c95b92eee712 | -15.51056 | -43.55951 | 2024-09-28 03:30:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| cb010347-d763-3104-86b5-40db6574a205 | -15.50982 | -43.56314 | 2024-09-28 03:30:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f4fad693-e1cd-3717-9818-6f2b710e0c0e | -15.19512 | -43.84688 | 2024-09-28 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebc1d9ea-1642-3dd6-bdb4-3302c74633e1 | -15.19436 | -43.85057 | 2024-09-28 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67f003dc-3c9f-3fee-80cc-d2308ec797c4 | -15.19413 | -43.85008 | 2024-09-28 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f28abfc7-86d2-342b-b40a-f7980068921b | -15.1889 | -43.84939 | 2024-09-28 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6493d474-db38-3742-af6e-8fb2e59a2853 | -15.18867 | -43.84888 | 2024-09-28 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05e84668-b215-3cd3-bc30-b98a2cee7b80 | -17.96025 | -44.24791 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35d3aa2a-3e1d-37b8-9e22-3e285defec03 | -17.95948 | -44.25153 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6a30b3c-3467-3d66-995e-f163ef763159 | -17.9542 | -44.25019 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b6be83b-23d1-3d8d-91f1-926c2fdc0ff3 | -17.94565 | -44.24916 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21a3e7ba-f4ce-360c-8bb1-56c12e3655f0 | -17.9436 | -44.2477 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0902f2f0-6f82-3f0f-bc1c-b46ab71d3aea | -17.94039 | -44.24772 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e971d02-dfc7-397c-845b-cb6bcc80e6bb | -17.93835 | -44.24622 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a943e0f5-9381-3b32-b463-a935207d56a0 | -17.84323 | -44.47322 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef318f8-02b2-3bb9-8c08-873ba2887458 | -17.83781 | -44.4721 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 659712b1-c4cb-3fef-a8e4-672539809587 | -17.8334 | -44.43933 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbba9b95-a993-310c-926e-4899c612963a | -17.83261 | -44.44306 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eea8f54d-5dd3-374e-a113-4c705565b451 | -17.83184 | -44.44675 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f2b2f2c-cdf7-3d0c-af89-9ca626283f07 | -17.83108 | -44.45035 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README30.md)
