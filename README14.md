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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3d251cd-e4f4-32c4-9c75-6c5a9ee879f1 | -7.66952 | -42.57854 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0fa0867f-7b50-3520-b244-ce209d4d0536 | -8.51353 | -46.13807 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a3d45c9-733a-32e8-a8cd-5dbfeb48401b | -12.39366 | -40.92265 | 2025-10-10 03:40:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 69975d1a-14e7-3c13-923d-5b389f40d9cc | -11.77052 | -45.04627 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c585ad-af5f-3069-996c-55e1e021c2dd | -6.72925 | -42.88306 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 44630a77-d6bc-378e-b095-c4fa9ee5150c | -11.46275 | -41.89715 | 2025-10-10 03:40:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af0016b4-8f07-3b46-b3ee-c2d218539277 | -7.73704 | -42.41841 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79f8aad6-dd67-3083-ab79-fc894b41e38b | -6.73169 | -42.86916 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4a3008c3-0cc8-32aa-a3b2-d3cd81c2137a | -6.58859 | -44.21472 | 2025-10-10 03:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55782461-e1e5-3346-a87e-b567dff11c61 | -7.70965 | -42.37904 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ecc329d-da34-375c-9002-86848e1ee6b7 | -5.93065 | -44.0673 | 2025-10-10 03:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff033691-03e0-34c3-b9bf-d79c258bf22a | -7.09845 | -43.25464 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| db981d07-78d8-357d-b5f4-2d531e822639 | -9.33302 | -46.11101 | 2025-10-10 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8424ad78-7375-33c3-ac14-913d38df657a | -12.43252 | -45.78166 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e27811f-983a-3433-9582-0b7ce3e11a11 | -7.40436 | -39.78985 | 2025-10-10 03:40:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84352288-8eb6-3eae-bd7d-adb8f4d8e034 | -13.06857 | -43.84389 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db5cad32-aef7-3587-a95a-d7640f0f2211 | -5.6496 | -45.97016 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a774868-f340-3e95-aabf-004f203377cb | -10.17351 | -44.55357 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84bbcc37-26c6-3466-bfc1-30cde4d5b4b4 | -7.42528 | -42.98473 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f1fb5a5-9a5e-3233-ae3f-635fd6a3c7be | -7.79395 | -44.19608 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c22d749e-5295-3335-9e11-002f9c0db15f | -6.75537 | -42.84628 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2c4048b3-4f2a-3c04-9ba0-3e20f391196a | -6.75176 | -42.84878 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3e34fb2b-cac7-34e0-9f0f-c20d548095d8 | -10.16416 | -44.60299 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acd79ccd-ad1e-30cc-a7ce-ff754c9f436b | -7.84362 | -44.54765 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c72f2f-740f-3784-a057-961071a8c7e0 | -6.46034 | -44.58411 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aadbd757-30ef-3fb8-b799-6f3ace7c39a7 | -7.78395 | -44.05701 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70da7ee3-4999-3367-8237-429486c5f939 | -6.456 | -44.57407 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 172c3a93-8b2e-3ce6-9aff-83078b212329 | -6.75115 | -42.85224 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1630e163-7533-322a-93c5-b59fc8c5518b | -7.70457 | -42.37809 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ff55b419-7bbe-3e82-839f-96b99dbb321a | -7.26198 | -44.9086 | 2025-10-10 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 970ec138-2a73-38e7-a966-eb2a3d138e5a | -13.0629 | -43.84585 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cb7805cd-cf1c-3554-9243-44d4d93d6cc9 | -7.39669 | -45.16894 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1a5319b-1f98-36cb-b331-286d6c63c8e8 | -6.4595 | -44.58867 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caf7f270-d889-3dbf-a7aa-79e2c6869932 | -7.54623 | -44.60494 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 04958441-ccb0-375a-94fa-bcb3cf3415ce | -7.39581 | -45.1759 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef8c1523-49a4-3e7f-9ee0-5aa9984b28e8 | -10.16798 | -44.55204 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5a079a6-9129-384f-9103-edf1b343110c | -12.95668 | -43.94355 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d473934-4bfd-3020-9d7e-1e5f1fe2b00b | -5.64582 | -45.9697 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1d455ca-82e1-3dab-8ea0-7b99f6c2ef0c | -12.72032 | -45.83925 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 388abba8-b3a1-38be-a19a-4f6573e06330 | -11.78228 | -45.04594 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cbaf0c3-835e-3022-b744-82870123df8d | -11.77677 | -45.04425 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c05a7686-e48d-3be4-8e91-1f8f5a1b7abf | -6.74525 | -42.82318 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b583c3f6-03b8-3607-9204-b9bdefcaf865 | -7.71015 | -42.37616 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6631181d-aed2-3f3a-bb63-507e97ac4753 | -13.01527 | -41.4313 | 2025-10-10 03:40:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9cc908bb-4d76-39d0-9fd5-934b492bffda | -7.67005 | -42.57552 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da0dacfe-5dcc-30f4-a995-bd2b9b5c313f | -7.40367 | -45.16552 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d421560-aac5-3261-bd67-b042e19a915f | -8.50841 | -46.15723 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fb5e5b3-e00b-310b-a521-1ec501b41886 | -8.50821 | -46.13153 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ad82e7e-46ed-37d7-ab13-3843cc97869b | -8.50086 | -46.20296 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4047de0-4eef-33eb-ae34-ed2ea6d5729b | -11.56375 | -41.89105 | 2025-10-10 03:40:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7fcaceb-8a81-34e0-b59e-5d184771e6da | -10.16156 | -44.58589 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3e572e1-2826-3112-8407-aff0b172094c | -6.48572 | -39.81622 | 2025-10-10 03:40:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a18fff7a-c8ab-30b3-b2c8-97d510f2e3e5 | -12.57732 | -43.86195 | 2025-10-10 03:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caad7109-1091-32aa-be7a-1ebef5caad1d | -7.8004 | -44.19305 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d926683d-ebaa-346c-a2bf-92a970ac9b6e | -7.7993 | -42.60971 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83d15bf1-ed2d-3e1d-93d3-e5bb11abf53b | -7.39754 | -45.16445 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c3d84e7-b6fa-34af-82cb-6bd3e332d6fb | -11.63605 | -47.53918 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09a233ca-4d75-3dbb-ae6c-7952367896dd | -7.73865 | -42.40947 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc28100e-7791-30e9-be12-6991997f823f | -8.49969 | -46.20901 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50e2d1ba-244a-3ad2-a40c-5741b3d1bab4 | -8.50609 | -46.13446 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c604799b-f2b7-3c3e-bcd4-8c5a66266953 | -7.67542 | -42.39476 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6b2c7df-f1bc-386e-90be-08357756b6e2 | -7.41072 | -45.1617 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5c297c9-a7d3-3bc3-b728-6dfb15d87d99 | -11.09568 | -41.05164 | 2025-10-10 03:40:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ae24c032-b3f6-3f0d-8c7e-50301b1dfd19 | -6.73044 | -42.84497 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f37cd93d-915e-34d7-88a2-ede94317d369 | -12.63594 | -45.05942 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cecd7162-76c6-3ba3-a664-85b12c03306b | -8.50938 | -46.15203 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8651ed0-6c3b-31fa-84b6-5930912ef7f4 | -7.83777 | -44.54659 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b695f7c6-f8b2-3126-b948-fd325aadd74a | -12.4292 | -45.76776 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78d14a54-98e9-3e92-870d-dd357b90147f | -8.16645 | -43.31939 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f82e4af-e69b-348a-b7fc-8f8cf77af8bc | -7.80103 | -44.19602 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f4a5ad6-581c-3611-a060-519e2684093b | -12.40569 | -46.70671 | 2025-10-10 03:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9897fd87-4d14-3678-9dff-c31801f7e5ed | -7.80228 | -42.40572 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9e8ea66e-1fd8-3d6a-a8c6-98b7114b0ebf | -7.76967 | -42.41215 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 77baaa5c-b4c5-3507-a598-316341a3a15b | -8.44786 | -36.34026 | 2025-10-10 03:40:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d79733e8-80c9-3eb4-8d7f-990608d6b062 | -10.16574 | -44.5639 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7c44797-1e75-368b-a893-f42cfdf7bc61 | -6.73226 | -42.8659 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5f5fecac-b3cf-3cf2-a1de-df2a3a799c77 | -9.89655 | -43.55884 | 2025-10-10 03:40:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4ae846b-48b5-3a53-b238-d1e6a8829011 | -8.21085 | -43.36273 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0858eebd-3ca5-3a45-a443-2d9cc00d2912 | -12.42673 | -45.78025 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6153d4f-e184-3942-83cf-b89942f301c9 | -7.77971 | -44.0482 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2684d3c8-fca1-3d39-888f-9dd7b18fb2b8 | -6.66063 | -41.98642 | 2025-10-10 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f42d45fb-d1fc-394f-be51-0d50be718ada | -8.51456 | -46.13281 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86b7cbd3-6632-3791-86da-5e8dca582b54 | -8.20317 | -43.34407 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 274f022a-9972-3e6f-81f8-f2de3ef32402 | -11.96519 | -45.21181 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce365881-4397-342d-accb-9ec5204ef773 | -12.22511 | -43.7897 | 2025-10-10 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00e5c952-397f-3fbc-993b-da5540408749 | -7.79603 | -44.19118 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a0bd3f-e470-3866-97ba-8cd159c4f324 | -7.39746 | -45.16691 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c08b4c49-d491-3745-ac06-56806eb4de20 | -11.63211 | -47.53654 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a887f770-bcf8-3976-8c99-3c97a9bf351e | -8.49333 | -46.20759 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a053402-b5c6-300f-9077-d2d386065dda | -6.07496 | -42.59647 | 2025-10-10 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c370627f-ebe8-3b6a-9ab8-293c0352816f | -13.06662 | -43.09731 | 2025-10-10 03:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f81c2ed9-7c16-3ade-985b-6b1ab858af79 | -12.22456 | -43.79253 | 2025-10-10 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aea05f57-54de-3e3f-afeb-5380a463eb22 | -13.06349 | -43.84282 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 232823c8-fdf6-347f-b509-cca4891a5750 | -7.79873 | -42.61283 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 353acacd-4484-3365-8e3e-10548a250bae | -11.6334 | -47.53017 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b864238-c59a-389b-9403-8264456c5c94 | -10.16299 | -44.57838 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fef9f7b0-2a3f-3421-a0f3-63f7769d789b | -5.74985 | -43.37659 | 2025-10-10 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4c0b1bd-4705-34f6-adbf-e36a39eac5c5 | -8.20607 | -43.3585 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a45ffca6-b1da-36cc-9062-aa271e7da2e5 | -6.75471 | -42.83187 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7af90c24-bdbb-3d76-b6d1-6fef2dfe86ac | -7.09365 | -43.25005 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
