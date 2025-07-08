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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12f760b8-34e4-3a4d-9c31-4788daba3082 | -9.92349 | -59.90298 | 2025-07-08 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715cf390-a495-322b-8dd7-252577c1d1a5 | -12.58037 | -56.98715 | 2025-07-08 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a73b0c4b-a11d-31da-b8b1-d2243382e5b7 | -11.44998 | -45.10609 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d6f4d456-80af-3b9f-afdc-46858b04d96e | -10.57499 | -49.12053 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f2dcde8d-295a-3242-a0fe-1902b341373a | -10.63219 | -49.45303 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f490b191-63a3-3780-90a4-4e8d4c6a8de1 | -11.4312 | -45.11891 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43b69e77-d898-30dd-ba51-29d947bef080 | -11.84348 | -43.79438 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2619f881-b2dc-3565-8c2f-b04b701e4f01 | -9.22174 | -48.59712 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c1743a-d9fd-3217-a938-d4a5b9ab566f | -10.63554 | -49.45356 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c1f21993-30f8-360d-a709-b743e8b67f97 | -11.80859 | -44.26978 | 2025-07-08 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e723a337-7971-3c0d-8d44-e0f85d93e28a | -14.18978 | -45.50699 | 2025-07-08 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55d8ca6-9d3a-3538-a568-97f7d6dcb517 | -11.87957 | -58.7117 | 2025-07-08 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bf4c5c6-6252-3661-9b0b-ee5c52556292 | -12.98569 | -44.88562 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75edbf95-a1e6-3f04-ad53-10e90a57c910 | -11.87854 | -58.7172 | 2025-07-08 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b86fc0-157f-3222-abfc-ada616224f1c | -11.42034 | -45.10574 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f9dedf9-e562-3819-b510-280145e52bee | -9.81023 | -48.25379 | 2025-07-08 04:42:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5244bfeb-5f1f-3a54-bd04-631d6c7550dd | -13.40459 | -47.89108 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9e1466d7-6290-3bc1-933d-c58bb1f06f4d | -8.70074 | -50.01532 | 2025-07-08 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93d9659d-add6-316c-8144-0e092d14154e | -9.70426 | -56.18327 | 2025-07-08 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5badff79-c061-36f6-9345-069276595eba | -9.37663 | -48.95373 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6181b8b4-560a-3939-9a46-b6fac5203fac | -12.99055 | -44.88205 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e37c32c9-f529-3f4a-a555-728954f4ac4d | -10.97243 | -45.11556 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0633d956-e097-3721-9101-f2b4191e42fe | -10.82777 | -54.02709 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4450b577-db30-3286-95dd-49b5e2bc7097 | -12.98308 | -44.89014 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3d91a73-ef0a-3250-b26a-67d3a6c35b82 | -10.41533 | -49.76452 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55bd6994-1083-34e1-834a-ff85e73f752a | -10.64839 | -49.45926 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 584a3f71-0475-355f-8726-38059625ffe1 | -10.22653 | -56.76715 | 2025-07-08 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c075a90d-8911-38a9-bc17-c282b7453f97 | -13.65275 | -46.8134 | 2025-07-08 04:42:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aade7b85-8bdf-3d92-b8e1-08ad92069480 | -11.89791 | -44.91496 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fad22a-663f-3b52-bbf5-550a2bcddbcb | -9.37501 | -48.95381 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b62e7fe-2709-35bf-93f4-b1f5ceefff8e | -8.74322 | -48.03308 | 2025-07-08 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0badc3-391b-3952-a6dc-5a68ee47795b | -10.82295 | -49.55202 | 2025-07-08 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b155a45f-6fa4-31b6-9367-75604d8524a3 | -13.24172 | -49.83889 | 2025-07-08 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5524a83e-82e5-31ed-9f0d-3e691d7a3f39 | -9.21414 | -48.59641 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7aaea09-eb40-3daf-bd95-2f6d4ed81124 | -10.64673 | -49.46995 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d00c2cde-0948-330b-87e4-7aba473f9ed8 | -14.0467 | -46.24279 | 2025-07-08 04:42:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d439eecd-d6f0-3700-8b41-8431a1278299 | -11.83891 | -43.79372 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa9bbc9a-3597-3c5d-b370-bcd7e48ce48c | -13.28915 | -49.15579 | 2025-07-08 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7fd6cbd-156a-3d09-8641-2a40cfcc8ac1 | -9.87217 | -48.46956 | 2025-07-08 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75d1c109-65bc-3750-91f6-ce21ba214400 | -9.22908 | -48.59454 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4031e370-7956-3135-bfb9-e96847dc06a7 | -12.98423 | -44.88181 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd8bd931-1fcf-322c-8da4-50e8518cadd8 | -10.83286 | -54.03025 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfcdb48e-db5b-3ed4-8b35-62cf71cb0a46 | -10.82556 | -54.01759 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 750aaf00-b62d-3e73-8e31-e731d31c8629 | -11.3285 | -55.21789 | 2025-07-08 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 060d6d41-e1ed-312c-a813-59747773ed63 | -13.36743 | -47.79005 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e81fa9f5-7ea3-3cb6-9421-88f7c0fe69df | -10.64114 | -49.46177 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba94b0d6-df22-3a85-8084-def03adb9505 | -12.5831 | -56.98201 | 2025-07-08 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc260ca0-de02-3035-806d-667f041d075c | -9.34577 | -58.84364 | 2025-07-08 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685dc265-6672-3e66-9224-3c8dd92f2f86 | -13.41243 | -47.88803 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65c2cea7-2a2f-307a-bbad-60bce56a87bb | -10.65119 | -49.46335 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5cfe66b4-3fb3-3966-90e9-07ac0b6e9f67 | -11.89739 | -44.9187 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 038eacec-2694-3813-91f9-ddf319f5d5d9 | -12.98678 | -44.87722 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d521d1fb-1431-3a3f-895e-c86abaefa984 | -13.24071 | -49.83866 | 2025-07-08 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e457e0e-6865-3b9b-9c4a-68580b32fa79 | -12.09803 | -44.73625 | 2025-07-08 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd283736-9915-3223-8a14-691c9b90bc8a | -10.97295 | -45.11182 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 017f691d-500c-3eb6-95c3-2b1cb8df7bec | -12.5811 | -56.98301 | 2025-07-08 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d6bf78a-1d6a-3a4c-b895-3cab28f3eea6 | -9.12766 | -47.59205 | 2025-07-08 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4856890f-ac67-3693-bb26-a6e2d25e91d4 | -10.64728 | -49.46638 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c26e97b7-b56a-3159-bbe4-205e65b28961 | -10.63548 | -46.37218 | 2025-07-08 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47fc24bf-3292-3b4b-8550-6387f9ebda2c | -10.57836 | -49.12108 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7f8cfc80-cc6c-30fc-b731-777b85c02bf9 | -11.45119 | -45.10918 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a8cae92-c866-35bf-ba65-2517d8fb8369 | -10.58173 | -49.12161 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35816b56-f129-3fc0-8142-6c8dd074641d | -9.22852 | -48.59818 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24c4f5d5-c714-3158-bbfd-8b02739d7819 | -10.82777 | -54.01569 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a64afd7-e4ca-32bb-8db2-210bc9c2605f | -11.43335 | -45.10373 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 59925049-cef4-3178-8997-743dbdc4e065 | -10.62829 | -49.45606 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59af9c3b-98c1-3549-80e1-88a563051e8f | -10.82851 | -54.02264 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b7e90f7-adbd-3110-80e3-b58b2d28fb6f | -12.10232 | -44.7369 | 2025-07-08 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41713015-5b4f-3d74-b14a-aa6d48141722 | -10.41255 | -49.76046 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 997ffa7b-51e3-30e8-bbc2-4e02e38cd542 | -10.65454 | -49.46387 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6b3de693-bee6-3c5c-9e9a-3c248ed55e3b | -11.42503 | -45.10254 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3a33cb22-13d6-3634-9a2f-3c03419088b2 | -14.01359 | -46.21593 | 2025-07-08 04:42:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1f87d5c-97cf-3f19-8b90-5843a8933d77 | -10.63944 | -49.45053 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4f5e06d1-acd9-3aeb-b6cd-bb925486e04d | -14.07842 | -50.15961 | 2025-07-08 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a811f2be-37e0-32d1-85fc-022782f48626 | -10.63609 | -49.45 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 79e32255-e75c-3e7c-a298-d7af2c5ced11 | -13.41438 | -47.87481 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d80220c6-3a83-3db6-aeea-4d5360693a2a | -10.8307 | -54.02073 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5f0f1f9-14fc-32ea-8b3f-5c1ba8f40a23 | -9.17577 | -50.18076 | 2025-07-08 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 34d07ab5-5176-36ef-9172-b1b2f8612776 | -10.23854 | -47.45999 | 2025-07-08 04:42:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d620854-29de-3f9b-a9ac-bfc06ee10775 | -13.64821 | -46.81768 | 2025-07-08 04:42:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25566846-0f5c-38be-80d3-bb7f435d9c30 | -11.42088 | -45.10195 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aa92af47-347b-36bc-b4ba-931576286274 | -10.8207 | -49.54435 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dee3ed0b-831b-3431-b87b-ad946bab7af9 | -10.6319 | -46.37404 | 2025-07-08 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4a40d48-2bbf-30ce-939c-85d868f74dc8 | -13.37107 | -47.79054 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3697d604-5c31-3b65-8dac-fe364d248a2b | -10.65174 | -49.45978 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe4bee3b-f20d-3831-b3c7-0e8d0c786206 | -9.21891 | -48.59295 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ba3a5f47-a2a7-3007-bab3-1aff123276bf | -9.86875 | -48.46903 | 2025-07-08 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b91df9d-ff84-341c-861e-fb9e30ab7103 | -8.96012 | -47.27246 | 2025-07-08 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfee354f-ab66-3b96-b1bb-d3d01de55d11 | -10.282 | -49.55098 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb59b153-026c-388b-af50-ebbff7eee731 | -10.82994 | -54.02516 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 671a0c23-77f7-39c7-b35e-cd146ca672fc | -10.13141 | -57.77938 | 2025-07-08 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f51d5b94-c0be-3928-9169-c41942b099f4 | -10.57892 | -49.11746 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 70952770-6aab-3c57-a042-89771977acca | -11.42397 | -45.11013 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b1fb5b1f-0060-379c-bbaa-df3e913c9098 | -10.57555 | -49.11691 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f74959d4-bfbb-35c4-bdd3-955004900254 | -11.44005 | -45.1163 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66f17654-7f2c-3c69-a09e-f489368ab19b | -10.64059 | -49.46533 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13388f1f-2400-3c87-bf23-8bf9ecaab60f | -10.95886 | -48.22355 | 2025-07-08 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e37c3c6b-7b28-38b0-92b1-bd4610d62f7e | -10.9527 | -49.25279 | 2025-07-08 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab3142ee-94cc-3e2e-85a9-7b79a42e3685 | -8.70351 | -50.01934 | 2025-07-08 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c396e38e-879a-3f09-a50a-82e73c782897 | -13.41009 | -47.87878 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
