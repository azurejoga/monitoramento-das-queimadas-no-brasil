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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4f091db-a5e7-3ff5-b9b9-2f8f5df24e65 | -11.84717 | -47.60019 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43614f61-b8be-38ff-bc47-ae53d5b50674 | -10.16842 | -49.31591 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 867425af-fcbf-38e4-9e16-214a220f801a | -12.20395 | -49.62274 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 387a059a-e5ac-3ab1-9fa8-46010335cfed | -6.81214 | -39.14705 | 2025-11-16 04:08:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a44e530d-1357-36fd-afd1-9c3eaa1b0fb7 | -10.8056 | -47.99355 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08500a06-b5e8-3d07-ae64-d3a7a5ab4549 | -10.25395 | -45.06748 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c69925b-5861-3314-b807-6ed4a9dd1417 | -6.69794 | -40.80248 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c98cb3e2-34f5-331e-bf5b-2af533284b81 | -12.4252 | -43.17788 | 2025-11-16 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9067ab5f-98a4-3e34-bb56-2bd7b0fe3b41 | -6.05131 | -46.60912 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63a1f157-19fb-3cb0-a37d-e3c840509b84 | -6.71959 | -42.94165 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 56eb9aeb-8def-3117-a07f-dc2a7e121050 | -6.13479 | -48.05244 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c4bfda7-9bec-3981-a53e-76abf4a780f2 | -5.96159 | -43.75408 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6e28c1f-15aa-3e71-a140-9e35375256b3 | -6.58677 | -42.04829 | 2025-11-16 04:08:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 942de736-b663-39f2-9a74-8dd8b265fe39 | -8.33917 | -41.25296 | 2025-11-16 04:08:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8fba4965-272a-3704-bda0-7e72f8204296 | -8.55453 | -47.7859 | 2025-11-16 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2c21e73-c75c-35ac-b0c9-4a3ab73ed2b1 | -10.55927 | -44.92801 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb744936-459e-364f-94ec-6f6260d37d3f | -8.05916 | -43.10455 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 2c40cd4f-f32f-324c-9b58-c18a6ef6de6a | -7.25151 | -46.32106 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6230d166-b28f-39fd-b63c-dd1da5f1269c | -6.80924 | -39.14262 | 2025-11-16 04:08:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01afeb4f-fec7-3552-b97d-463f652e5227 | -7.21171 | -47.9804 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5de53231-8dbc-309c-a2e4-185673dba17c | -11.91137 | -46.18785 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d3f9c7-4646-354c-b282-7ce5b623eac4 | -8.89968 | -44.43408 | 2025-11-16 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78f47263-c4fd-3713-adc1-0cf06bda2a19 | -11.13987 | -44.93291 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfffb41a-22e3-3e53-9035-52da05312e0b | -6.41292 | -41.47102 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf44465a-92e6-30b8-97ce-6768b9fd6a32 | -7.92594 | -47.105 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84d919fa-c293-30f1-aff7-7ea3100a5893 | -9.74332 | -43.96682 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4e5abafc-7642-3ff2-9e57-6777eb8da6b8 | -8.10623 | -46.03328 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 18d6971d-747b-3f4f-96de-9606b70dd765 | -6.62974 | -43.69858 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e819e383-0dea-3beb-93bb-eaec39097628 | -6.59266 | -43.79733 | 2025-11-16 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d53e34d-e590-3087-b15c-deda6867c136 | -10.14216 | -44.23689 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fcd11b1-ee54-3a4b-afa3-e1c20f2c2193 | -12.05851 | -48.19804 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c99fdf4-def1-3d5e-bf41-330866f2accc | -7.22915 | -47.98338 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfc273cf-1701-3767-9472-7a46abad45b1 | -8.20566 | -43.56436 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01a6849d-bf32-3871-8455-4509cbd7d5b9 | -6.431 | -42.06583 | 2025-11-16 04:08:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 63fd304b-324b-3804-a3e0-52ce43d8b5ea | -9.05983 | -44.74266 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11ae12a9-1e9b-3115-a6bd-1bda5a870bdf | -5.72355 | -42.91971 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8f71e31e-33e2-3c0f-a9e5-0b3227b3e602 | -6.96742 | -41.53086 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4fcdb04-58be-346a-a865-73a8aeb8a6db | -5.35961 | -44.90682 | 2025-11-16 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f7d8c2-1edb-3ae9-bf24-a64573e7bab8 | -8.90182 | -50.22879 | 2025-11-16 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 940c6222-8ee9-380d-8b91-0cbc3e98c3bf | -8.09131 | -43.01145 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42651f9a-796a-3be3-9f28-65632aa6cb81 | -9.75268 | -43.9796 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9954e414-ccd1-3209-96b0-e05ffb7b2e1f | -12.6804 | -46.77981 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4648532-cea4-3f5b-acc9-d7f11be92dea | -6.61793 | -46.64142 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9cb73a-2c87-3dd3-8f8d-04a7438dafcc | -6.54333 | -43.40533 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d2b7661-422c-370c-b6af-ef97cfec1bf8 | -12.69817 | -46.78773 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82a4bdc3-6ae7-3e74-91a1-9146b7dfae6e | -12.38143 | -48.09733 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 978a2d4d-3066-3e66-97d5-c591167caec3 | -6.68689 | -40.80789 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3eb0d822-e605-3831-9e31-fb30c363b0ef | -11.05467 | -45.1572 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6727774b-45e4-3db1-bab3-6e2672c05103 | -9.11202 | -40.46362 | 2025-11-16 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7fcfe39-673c-340d-bad8-f338a70e7f77 | -10.55863 | -44.93191 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6326b54-38c6-38e4-b763-d8d7e8c4ed94 | -9.85314 | -47.61103 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 563805b4-7599-3b64-adc1-a160469081eb | -6.08675 | -41.59986 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 21c48bf0-aef4-3cf5-9663-c606e3a0bf64 | -11.91061 | -46.1923 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c44321b-5412-3b52-8299-3b2dd23731ea | -7.41303 | -40.07344 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28259f01-4649-3729-8a0a-059342f08e40 | -4.30868 | -50.87574 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9990ccfa-4331-3774-a013-f38a5061a635 | -12.00378 | -49.27862 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| adbcd2bc-c0b2-30d0-b02e-b4571839a2d2 | -9.81272 | -48.16882 | 2025-11-16 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf6100a4-b31a-342f-b9a7-7968e7ab4711 | -9.8519 | -44.71701 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e12fa68-617a-34a8-8d73-373536b17b65 | -10.00482 | -44.77388 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72bac57f-4cb7-36a6-9e32-25546a8e4b30 | -6.57021 | -47.90243 | 2025-11-16 04:08:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 665755df-cfa8-31e1-a57a-a9fbf2aba677 | -7.36362 | -46.58398 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea28a2fb-421d-3b42-8a73-3938a4d6e76d | -5.45327 | -46.44081 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04714615-a342-39a7-a82b-4b10b74ad273 | -7.4136 | -40.06979 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2ef04da-5024-33c1-93cf-eee280ab5fc3 | -6.11208 | -46.18426 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dab80e6-8119-3ae8-80e3-3bb972f621eb | -11.41277 | -43.32592 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d57fe884-6d29-3211-b992-cc87c9ec6439 | -6.85505 | -42.83851 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12e135b4-4a36-30bb-865b-cb978e60ddd0 | -6.38011 | -42.32195 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 045989c8-ea91-34a8-9278-0841a20023bb | -11.97773 | -44.96038 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46c49eba-a5ec-3ff6-8448-493b0759ad41 | -7.71509 | -42.94381 | 2025-11-16 04:08:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7639ab6-b938-3eec-a78d-30e4d2ba02f4 | -7.454 | -46.88351 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aae4b9d-b5bb-3d01-b7dc-e880a582b4e4 | -11.41552 | -43.32999 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bf6b326-262d-3e7b-9fc8-e4dafad3134e | -8.21596 | -41.10757 | 2025-11-16 04:08:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cf5a3a72-1385-36b1-87cd-26d6afbe6aa5 | -11.70865 | -48.39201 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 852780d5-32ff-33b4-afea-8814578ab51d | -8.06308 | -43.10154 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3f980511-5684-3dd4-8e69-72aed13df015 | -5.99236 | -41.91792 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 708f8534-0284-3eb1-98bc-27d86d46f217 | -6.45394 | -42.36935 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 675e63cf-f92c-3628-8164-ff1ccf39a974 | -5.57956 | -46.1492 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0842bb52-7103-3316-891c-66502782565b | -9.83901 | -47.61989 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 722afe8a-4ffa-3ec9-94a3-4d6a38f61234 | -11.8128 | -45.55014 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94fdf1ef-5445-3fa3-9382-694388d149e8 | -11.9786 | -44.97633 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02bf4392-8f9b-3fd4-a8d7-8ec9b01c5c52 | -11.96257 | -44.94963 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee62de77-9d69-3242-bd64-5e82b58d8e3f | -6.13329 | -48.05007 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 729291bf-d045-3305-b77d-c96764583bfe | -7.11519 | -42.73891 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b172b84c-b9b2-37c8-bcec-69319240dd8f | -7.22058 | -47.98465 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215e9831-9fc8-32a2-8569-9b7a48f2dbd6 | -11.71135 | -48.39338 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c0e46ec-2342-3b73-a246-787a6846a1a5 | -10.5427 | -44.14624 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bcbf9ff-da9f-325c-8fde-4ddc5572e98d | -10.33012 | -44.60853 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d950bc97-a3b3-31f0-a4e6-f8089885a5ef | -6.85393 | -42.84555 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e3e6e9c-97b6-3ccb-90b4-223bc48c557c | -7.01889 | -45.16819 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec7328d1-90cb-3d1c-b5eb-fd4d32a325fa | -6.26602 | -41.41304 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 957ae8f5-f698-3e5c-b919-84524b898c12 | -11.16275 | -47.46248 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2cd2d1-610e-379a-990d-d3c1c9fba5c9 | -7.09251 | -42.73505 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 32d0b410-c6d3-3bef-8d33-8cb5d4315be2 | -7.3632 | -43.32892 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1776c185-f240-3aad-a90f-1b2799381ec2 | -6.67415 | -40.80233 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03fbf5be-ed6c-3ead-84a5-862f61328b85 | -9.86063 | -44.17599 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e6245ad-46a9-3dd9-a80a-e4e95d4951b3 | -11.56559 | -42.42606 | 2025-11-16 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6180842-4a25-3e79-b7ea-ff12e70792bc | -7.35863 | -43.33565 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741bf13e-546c-3157-87a9-a0c3ddecf869 | -10.12191 | -43.90854 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfeb4e79-92b5-3ead-a864-041ba4af8b49 | -10.81092 | -47.9875 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| addf9bf5-cdb1-3f00-a8d8-9ebed83d048d | -10.70557 | -44.52445 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README43.md)
