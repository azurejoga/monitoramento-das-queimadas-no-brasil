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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda265a0-b19b-3fdf-b9cb-97f703970feb | -7.93888 | -38.91108 | 2026-09-21 16:01:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0c6383bd-1181-3f85-b6c1-b5d4101f7d56 | -11.44652 | -47.29509 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 77475e57-3833-3d46-9e16-059ae8083214 | -11.3444 | -43.37029 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37a26cd0-c899-355e-8c78-f986d599efe3 | -12.5221 | -40.3567 | 2026-09-21 16:01:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fbfd60cd-7412-3cfe-8ae8-198a854e87e6 | -9.54621 | -46.51481 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55776592-6553-309e-9d24-7ec7eb0adfb1 | -13.0532 | -50.62466 | 2026-09-21 16:01:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 183e58bf-a745-3c30-9bb8-30edf2035d3c | -9.77936 | -45.05836 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| abc0ac88-fcf0-3d81-b856-84d1cda4980e | -12.02993 | -50.03909 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fc4a6467-39f5-3457-8a60-86e8d052f805 | -8.7815 | -45.86042 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 67f8a13b-e4eb-3ff9-b447-e6b1cc032de3 | -9.40585 | -48.32664 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c99154e2-fa38-3f51-b7ab-dd5546570582 | -11.94617 | -46.50851 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 008f76e8-f568-3619-93c6-65fc418d43a5 | -9.5475 | -46.52483 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 900ff3b1-6a06-3a2f-a759-96b679ea4b73 | -11.09399 | -48.32059 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c8125023-e5c9-3ecd-b9a5-a01b71aee838 | -11.39041 | -44.05384 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 22a6d571-d915-37d8-9cdf-0223587a13ec | -11.09366 | -48.32281 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f2ca06c-2c6d-3e37-9c38-25e55456b2d7 | -9.77711 | -48.33316 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 601e07b5-ad3e-3014-aa67-bd065bf7f5d5 | -9.90677 | -45.83327 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 09d15033-548f-3132-b91b-2506b3d3e098 | -9.62219 | -45.81131 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fa6e36a7-bc42-309f-a4f9-f47bf77c7ee5 | -11.65685 | -47.78553 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 19c52a29-466b-3c60-b019-cf9e65215d09 | -11.42043 | -47.33111 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 706e4d37-a065-3913-996a-dfd926136a3b | -13.76831 | -45.39567 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6b99b80-2ffe-3a2e-9693-d34b760c63fa | -11.93302 | -46.49161 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 884cfb40-e737-3523-94da-31a040f94047 | -9.1695 | -50.00358 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 6ab6008a-6279-3cf5-8556-fc6189501a8b | -11.32739 | -50.72138 | 2026-09-21 16:01:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 279f9f6a-1810-3f62-bfc5-ab331124dec2 | -9.78006 | -45.06366 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c3cf6724-f21e-3741-934d-321f261ba4cd | -11.29231 | -46.76346 | 2026-09-21 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f1336b08-fd54-302f-bfc3-05cabdfe56e1 | -11.19188 | -45.39649 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9726a6cb-16fd-3fcf-8195-19f7f63f2119 | -12.66774 | -45.04649 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d96e300e-d247-3fe7-9b71-df53ed39903a | -8.8437 | -44.93155 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| efabfd57-7dec-355c-85be-db4f5d1cd039 | -12.44163 | -47.07255 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 06ec2367-1729-3956-bad6-fcc01047fa2f | -11.43207 | -45.35827 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ba267191-c081-33c7-b2c9-44b90f23a3e9 | -9.16503 | -50.02173 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 856640a5-9992-301c-a267-08710e52ae90 | -8.76172 | -45.86633 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 47cb851e-e88c-3a81-812a-3f28442b9dba | -10.72945 | -50.83956 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5732410c-1ab9-341c-8f61-7c8f148fce3d | -12.26657 | -50.15709 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8fe47b60-304f-32cc-844f-01164a9133dc | -12.29453 | -50.66388 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8a9330d2-b0f8-320b-bc46-06eab4b3d3f0 | -8.5216 | -36.17855 | 2026-09-21 16:01:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2a4e8d0b-1040-32f1-ac09-0df4e5e4774a | -11.66872 | -43.45328 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 437bffc9-49e4-3531-a88a-5d01f9ccc2fc | -10.95452 | -50.58599 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 8cffe062-fb65-3cb5-833e-62cd783598b2 | -10.72492 | -50.7979 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| bb95d91b-6d8e-3541-86f5-58ba43e3def7 | -11.26785 | -43.40244 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 64d166de-798b-39c0-ba45-86315f7aaa03 | -13.92847 | -43.7407 | 2026-09-21 16:01:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac71e8e9-2b2b-3736-9900-f44d2e277cb0 | -12.38074 | -47.00171 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fd512723-dc57-3e77-afa8-ea802274f9f9 | -11.81203 | -49.84082 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 01db5f7b-4802-38ba-9848-7a84b64d4147 | -11.34168 | -43.38405 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 289297d1-4c4f-3bbe-85f7-2877cc287576 | -8.50216 | -44.86702 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c4860647-4528-3c8d-9b40-376b71919fae | -8.32255 | -44.75703 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 72d5578b-611c-3004-86aa-26d6b4681a7d | -11.45497 | -47.65572 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54f25298-d94e-3479-bb8a-b2ed48247420 | -12.43095 | -47.03257 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5b32e3c2-6f36-3f31-97e8-e57437f8587b | -9.26704 | -48.216 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d514a6bc-36c6-3ff7-8001-340f6bd26a88 | -12.43709 | -47.07159 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 96693a6b-8731-3a3d-a39f-8f3509c975e5 | -10.16167 | -45.55879 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1f47582e-fe52-317b-ae61-339532307abf | -9.853 | -48.39928 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2ceb976f-a4b2-3ba1-a51b-dee0752a204f | -11.67059 | -43.45709 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 68482193-f6de-3261-a1d4-0fbd0e9c7e11 | -11.94032 | -46.51031 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 359b358a-7000-3f71-8088-87ada8f7b769 | -10.82685 | -50.14074 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| dd7a7b49-b5fb-3a9b-9ff4-2f6793ba6635 | -10.82756 | -50.14699 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 090f3fb2-dfbe-347d-866c-a1434127dc0b | -12.4252 | -47.03323 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 07409aa1-7122-3483-bbd5-d973798b764b | -9.17023 | -50.00941 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| c15ca30f-6b5a-3e85-b3da-021cd219f0af | -13.47023 | -46.92399 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4cf4aad2-6b68-3a58-a77c-426847143fa7 | -14.21596 | -42.1913 | 2026-09-21 16:01:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ed6b2f9f-c64d-353b-aa59-77c3702f8b70 | -12.06761 | -50.07011 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5a591f56-458c-37b7-9a76-3e91fe56f534 | -10.70154 | -50.69939 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 789fbdc0-e050-3a26-a9c6-e6006f67ab9e | -11.38032 | -44.23077 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e1cf4f4e-f7cb-3a60-bd76-8cde76aa1147 | -12.5472 | -50.03055 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 028e6abd-fa54-39bf-a118-8323755981b2 | -8.78485 | -44.26479 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 90283869-9090-38fd-8a61-752942f29e43 | -10.75149 | -46.31559 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc5a546a-c299-3632-a455-b34edc0f2c31 | -11.95096 | -46.50584 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 890845c3-e703-3617-9dab-34505014f3ac | -13.89238 | -45.49886 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bc7471f9-6169-37d9-b15a-d2b2482d189b | -11.27285 | -43.40625 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 87bbb953-9d19-3538-80d8-2f7714896d85 | -11.67433 | -43.46169 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 402b54c1-8551-34c1-88d1-29e2253b73c9 | -12.81802 | -44.2179 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3eb5b771-509f-36d4-879d-a6aba0112dcf | -8.32794 | -44.76188 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 54538273-9d21-35c1-bceb-457851eb7fe7 | -12.82653 | -44.20507 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e21034d1-f95e-356d-bfac-66adcdf09462 | -13.02805 | -46.97985 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 643f6266-fe30-344a-9060-0179168b941d | -10.08533 | -50.2837 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 819460cb-c4cd-33ea-b00c-5200e6566bed | -11.7993 | -49.8088 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a8998bb2-613e-36da-ad36-f1b95c3a595c | -9.85479 | -48.39887 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8595e11f-a718-307a-94ce-3455abc01894 | -9.17241 | -50.02678 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 531e7c55-693f-3cfa-984b-bb309abdcf18 | -9.73958 | -46.07058 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ecaf6b1-f258-3b6b-866e-b80286f0aa69 | -9.85772 | -48.47394 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94c0c00f-6e31-3276-a764-f58bc8508849 | -12.07669 | -50.02136 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| aacb3134-94ac-30f4-9a8f-87a30b6b1167 | -10.21078 | -44.15116 | 2026-09-21 16:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 884b0194-b99c-3ca2-8dcb-b39aba33e3bd | -11.19694 | -45.39576 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 274f50fb-0bdf-3ca7-8274-f61cfb4367f7 | -12.27368 | -50.1549 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 921be480-baa6-3b2a-b92a-3865ccc04d80 | -12.42578 | -47.02343 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 517e9e10-8725-304c-9d04-5e38401bda6f | -12.77723 | -47.10978 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 59570de1-043b-3949-93bd-1510202f00d1 | -9.27557 | -45.92376 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 99992603-7c42-3173-a3d6-2ca3d1f62c9b | -10.75372 | -50.59861 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 238c48f5-1d42-34ca-aa42-0d287baf9077 | -9.5402 | -47.95041 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 204.7 |
| c198c150-204c-3ecb-b47e-4c7845cf1f8d | -11.06718 | -49.74861 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a4aa06cd-30fa-32c5-aa2a-b49fd5fe4c91 | -11.86784 | -46.84759 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e39f6104-088c-3040-90d6-f80789a7a105 | -10.75816 | -46.32504 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 79e82fec-9397-35ac-a219-9478434630f7 | -12.43911 | -47.03827 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a426c0c-de47-3e64-b26e-7ab84a18a73d | -9.56168 | -46.55031 | 2026-09-21 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d7a74e89-0aa3-31a6-80c2-c6b2f8c3c40b | -11.44168 | -45.39353 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5f74ee1f-0e95-3b2b-a5ca-0ad8f79cd072 | -9.47018 | -45.42179 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 18480ec0-00f0-3013-90d6-ddf11d3b1eea | -10.57867 | -46.53055 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1eb0460e-c69b-3aa8-9892-2941881b0f94 | -9.03439 | -49.82855 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 391aa0c7-6979-384e-968d-eb3f3e5e523c | -8.76665 | -46.92891 | 2026-09-21 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README152.md)
