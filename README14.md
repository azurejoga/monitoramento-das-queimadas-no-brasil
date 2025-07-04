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
| 85a343af-d8ce-31ac-92d3-fb91211a2de6 | -20.57845 | -44.57338 | 2025-07-04 04:19:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b33e10b0-29dc-3fae-95b5-e33767189cdf | -19.74566 | -54.0017 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd6ecf2c-e959-3b46-8966-54238010a3d0 | -14.26352 | -45.19626 | 2025-07-04 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f86a4aa9-da7c-3971-95d8-111c31ccd160 | -18.44243 | -54.66857 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80108395-5c92-35a3-903d-958f7a26b024 | -13.40396 | -47.83651 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88a57ca-a085-31a7-a678-7e39dca7ba71 | -13.69675 | -47.74649 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a6c7b5b-b96d-3738-9e04-cdcda653e27e | -19.74669 | -53.99657 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92a19d80-fd44-3d03-b8a9-8cf29ea25555 | -13.39825 | -47.80458 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 659850a9-023a-368d-9d9a-07a0b97fbb42 | -14.88221 | -48.35694 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 261d14d5-2087-324b-9d52-08ba5ab936aa | -19.16476 | -49.13923 | 2025-07-04 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 364a2218-2645-33fd-8c9f-7a37374f31b3 | -21.04251 | -55.99891 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7037d6e6-040e-34fb-a1ef-84da7d85839d | -14.47823 | -46.35976 | 2025-07-04 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e58d73f-d77a-3b16-ba06-5caebb27a5e1 | -15.8331 | -41.77736 | 2025-07-04 04:19:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1bb20a8-ea97-36ff-a696-0eb7c60c1aac | -19.81961 | -54.41154 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60c0ed02-6842-3385-8b27-0c3727fb86a6 | -14.47884 | -46.35604 | 2025-07-04 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8de9a16-b40b-39b2-9806-abf979d2013a | -14.6055 | -48.24593 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab07828e-8a73-32ed-8772-1e398dfe65cd | -19.81559 | -54.41487 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e36bbcf5-0037-3d65-b896-40f156795e95 | -12.57851 | -56.97487 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7bbc89d-d3b0-3111-bad0-d386939fb396 | -14.79704 | -48.30706 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57e38e69-8d92-3da9-8671-093f345f347c | -14.48763 | -46.98031 | 2025-07-04 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb10ab49-d405-32ff-9703-00376554e1bf | -19.86502 | -48.33047 | 2025-07-04 04:19:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db160774-dc2b-348a-af13-bcaf7c3c091f | -12.93683 | -47.13385 | 2025-07-04 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 080ad104-2cd4-36a9-b3f7-27b41a8f7196 | -19.96847 | -44.21725 | 2025-07-04 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab425f2f-95b0-358d-9d9b-d82441a3d940 | -18.66855 | -55.74456 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2702cdeb-69a1-3e99-ac53-992120195fb1 | -12.58266 | -56.98709 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a105756-95cb-3b5f-a368-4b2c810dad8c | -10.5586 | -49.1337 | 2025-07-04 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9c09acdc-8086-3897-b2ac-cf5064f077f6 | -6.6112 | -43.8941 | 2025-07-04 04:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 11c843a7-3c72-324b-b73a-3c827c8f4626 | -27.92278 | -51.67088 | 2025-07-04 04:21:00 | NPP-375D | SANTO EXPEDITO DO SUL | RIO GRANDE DO SUL | Brasil | 4317954 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ed2d027a-465e-30fd-bb8d-e1faf4c07ecf | -6.6112 | -43.8941 | 2025-07-04 04:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 804605d9-d42e-3f95-be5d-513494903159 | -9.0783 | -48.3315 | 2025-07-04 04:30:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 41215f0e-4309-38a4-8914-53c9037cee2a | -10.64966 | -44.48827 | 2025-07-04 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12636b33-de53-3aaf-a542-f711250ec5d8 | -9.08026 | -48.3318 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| df5bfba1-de62-3eda-a587-613d173825ed | -7.07681 | -43.21847 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 509779a7-7fe5-3b42-8267-e29431c525ec | -6.01365 | -44.52813 | 2025-07-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2df81dc1-acb7-33fb-bc02-43bb711c1c16 | -6.75157 | -43.04503 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce29bd0b-3e56-3078-86c6-34e1b5bd0de7 | -4.81975 | -47.31595 | 2025-07-04 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 27992a08-8fb9-3bfe-b906-638755a49a20 | -9.08082 | -48.3281 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| fe6f98fa-7b74-3feb-b117-6a443afbaf7b | -6.80048 | -44.75242 | 2025-07-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09d18eca-7edf-39a6-a999-3996218c9787 | -6.88307 | -43.21899 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7e72bb5a-70ec-317f-be6a-6b017b611211 | -10.64166 | -44.48288 | 2025-07-04 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1631def-5f78-3a64-83d2-588626e0d417 | -6.28282 | -43.68078 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1e3741c2-b919-345c-910d-35e8fcfff392 | -9.0848 | -48.32491 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fbcba610-f46f-374c-858b-a522916fd50f | -6.74058 | -43.15195 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a402d4e-397d-3b55-9d7f-76494815adff | -6.61054 | -43.8929 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d861682-0ba1-3fb4-86e1-85621141c6db | -5.87935 | -42.62932 | 2025-07-04 04:38:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 92ecbc6b-4055-3739-9a9f-27c5f2eeef26 | -6.60745 | -43.88452 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 744ea98c-5d70-3bba-b207-86977659625a | -9.78573 | -48.57469 | 2025-07-04 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bfec95b-6957-3867-bca5-969365db592c | -6.91396 | -44.0027 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9bddc3a-a21a-3f03-af03-cad903235a62 | -6.73613 | -43.15134 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2595788d-7f67-3c93-92c7-bea5a96871fb | -6.99871 | -43.53874 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c465ff1-b881-3956-9b6d-22c3e0da0d57 | -6.66831 | -47.86829 | 2025-07-04 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c3f2d99-7609-3e94-92dc-91de0237c82b | -7.91144 | -44.54107 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de046a84-2ec6-3587-b980-8ba6aa5dfdc5 | -7.94692 | -44.84502 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a98c7cb9-4709-3530-8104-9e6e7e606974 | -9.79725 | -47.75005 | 2025-07-04 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2601496c-d022-30e0-90b0-2e7b87bbdfbd | -5.28383 | -56.01834 | 2025-07-04 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8239dd1f-98d0-3a0d-8989-6a568943e858 | -7.10084 | -49.17175 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8de1d005-fc97-3ebb-bfd5-f1b32a8e2a40 | -9.03932 | -49.71982 | 2025-07-04 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 099c7d12-61ce-3c72-ac19-6af55ee06898 | -9.18348 | -48.85208 | 2025-07-04 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7c5d66a-451d-35de-92f5-9e7241072590 | -8.30687 | -49.08035 | 2025-07-04 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d587570-dc56-3b07-a79d-b31eaf5640f2 | -9.08536 | -48.32119 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8653dd2-ec86-349e-8757-bfa5325394e5 | -8.04627 | -48.45641 | 2025-07-04 04:38:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da1f953e-29c0-30e2-90f0-982d037ba816 | -9.72932 | -49.05774 | 2025-07-04 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05f1ab67-d04b-353d-a51c-6c1f6a95df4c | -8.86708 | -47.27635 | 2025-07-04 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f85f368d-8133-3a75-9021-992f014ed877 | -9.00107 | -47.44218 | 2025-07-04 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24f2a8c7-ba0c-3d2f-84c9-2a6c3821e84d | -7.89687 | -46.57952 | 2025-07-04 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec2c7ef3-6769-3aa8-a6ac-85518a69135f | -8.08985 | -46.28382 | 2025-07-04 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faa39eb6-497e-3605-90f0-7dd3ecab4645 | -7.84183 | -44.21507 | 2025-07-04 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e860feb-5449-39ca-a2fd-f3da5d09b54f | -9.79433 | -47.74558 | 2025-07-04 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fcb1dcb-5309-3abe-9957-b4b03b8bb485 | -9.12727 | -48.53144 | 2025-07-04 04:38:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbc6c2ee-71c3-3e9d-bed2-95af8b6eb0af | -4.81918 | -47.3196 | 2025-07-04 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f1729ce-70ae-3e2b-8d21-bb6caf7ef6af | -6.84468 | -44.94165 | 2025-07-04 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7302b9f1-280b-3531-b904-1399bdf7decf | -9.73849 | -48.35407 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3810ae9-91aa-3b29-9d24-6f4fb5b01990 | -6.89256 | -43.21584 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 07abf291-4ad1-3efd-a133-7ad9d4aa0a33 | -7.07616 | -43.22288 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c82e4271-4748-3345-9aef-7bae96c55021 | -7.2202 | -43.08449 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 310f2218-8b9e-3651-8fab-d0ab1437f103 | -7.22406 | -43.08968 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4714c66f-6e80-3d28-95f3-409f2a7ce6cd | -6.74055 | -43.18316 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3843dfd9-3913-34f3-99a7-a29354a11869 | -7.08127 | -43.21204 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77393b19-469a-36ca-927e-321cd0092efd | -7.91199 | -44.53722 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e18e6638-1c7f-3cf0-bed1-474ba3dcca04 | -7.10984 | -47.84414 | 2025-07-04 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 61eb5b20-998d-35a2-a412-1cc73747dfde | -6.9975 | -43.54706 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6294f3d8-f4e4-3f24-aee6-1090038cbb67 | -6.73676 | -43.14705 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 832626bd-2555-3d78-8aaf-61a36516ad35 | -6.97436 | -55.28727 | 2025-07-04 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b8002e-8d30-3f2a-9167-687ff00bfd37 | -9.79957 | -48.25252 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b78e4609-5563-3162-a39e-157862f7fa11 | -6.11341 | -46.18282 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bd05081-3cd0-3b10-aebf-d5299176b91b | -6.66072 | -43.17218 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 71739539-7b7b-3d82-9401-a5bb4aab4779 | -8.97669 | -49.85974 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6ea457b-6392-3ad3-a34a-057f1ab594fc | -7.17952 | -44.0159 | 2025-07-04 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ea7d86e-5eb0-3f6f-b8d4-4076bacae2f8 | -3.38057 | -43.1246 | 2025-07-04 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebc47368-f947-3183-a0a3-ab089e3c0b11 | -6.29083 | -43.95101 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2f6eda4-1a80-3c59-95a3-4a58ed04c2cc | -9.08139 | -48.32438 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a3cdc2cf-3550-395f-ae72-7a883abd0519 | -9.84537 | -44.68804 | 2025-07-04 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3eb44df-7019-33f9-b1d3-2adfc1d9434d | -6.84469 | -44.94519 | 2025-07-04 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f1d9a89-170f-34fe-8938-a3ba884b45b1 | -6.61166 | -43.88516 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e0cb3f0b-8506-3738-b0e8-d9bfaf7fde66 | -6.79997 | -44.75588 | 2025-07-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc4d3129-b631-36a7-9f5f-755323f9123e | -6.28764 | -43.67746 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4efd89b-30a2-377e-88cd-a0456ef40f88 | -6.97501 | -55.28344 | 2025-07-04 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd20f81-c885-305b-b95a-902baafc80f5 | -8.97392 | -49.85574 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae25774-7c1e-3550-a457-42665587b9e5 | -6.73294 | -43.14212 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb5ca51f-32b3-3540-8d49-c7faf3b933f3 | -5.92025 | -43.44566 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README15.md)
