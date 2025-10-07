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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb5e79dc-2f1e-31f1-920e-d6c1877495e4 | -22.5489 | -44.45075 | 2025-10-07 04:12:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c8d0ae13-439e-3ab8-9d8a-afd0ef436cee | -21.62345 | -45.293 | 2025-10-07 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e11cd119-8a3d-3c4f-9f92-c2496466a54e | -21.56752 | -45.27969 | 2025-10-07 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3c594906-26d3-34a3-aa02-40b021884533 | -22.01211 | -49.71852 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6407add9-7ff0-34e7-af9e-21ef477507dd | -21.092 | -44.17778 | 2025-10-07 04:12:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bfe9d536-b6af-38de-90f7-b361afa75abb | -20.57472 | -46.30363 | 2025-10-07 04:12:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 868eab01-ff08-3238-bf33-765650e30111 | -21.61854 | -43.99715 | 2025-10-07 04:12:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| edc74d46-dfdd-3ac7-9cc2-7914e2c2784d | -22.00469 | -49.73764 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7f418d7f-6f10-35d6-a5f8-93edda93c4b1 | -20.41352 | -46.0419 | 2025-10-07 04:12:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 800d75fb-854e-318d-8173-448b1bd029bb | -23.27979 | -45.5123 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 62703f91-137c-3dcb-ae21-9fd45f10bfd2 | -21.80856 | -45.64952 | 2025-10-07 04:12:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 876a71b8-9c56-306b-a774-66fe5b86ad10 | -21.81228 | -47.3792 | 2025-10-07 04:12:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13b4258a-de29-37fc-9e62-34af61c209b9 | -22.01074 | -49.74124 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ef1178b2-70f3-3e43-bb37-07adffae1e3e | -21.80746 | -47.38668 | 2025-10-07 04:12:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 21681bb7-939d-3bc5-889e-26823c0b190e | -22.18075 | -49.36879 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6abd247-605c-338e-bdaf-ad55e474d602 | -21.80403 | -47.38605 | 2025-10-07 04:12:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32698b76-cb6a-3761-87a2-521468ab97e5 | -22.00938 | -49.73352 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 56249694-9bf8-3dc3-89cc-127a751484a5 | -21.67933 | -50.07732 | 2025-10-07 04:12:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7df8f884-a978-36e7-85a8-7fed67338688 | -22.23736 | -47.59222 | 2025-10-07 04:12:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d305737d-4f26-3946-8b01-188012b726cf | -20.78928 | -46.42944 | 2025-10-07 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04b6cecc-84dd-3b0b-84d9-202f4fa3450d | -22.01936 | -49.54953 | 2025-10-07 04:12:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 005f5be8-55a4-3558-800f-d24efb798194 | -22.8843 | -43.7263 | 2025-10-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7ee6ee83-818f-35f0-b7ed-b44fd8257c52 | -22.90422 | -45.58663 | 2025-10-07 04:12:00 | NOAA-21 | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 38f865dc-e2bd-3698-987d-be33393d2bba | -23.135 | -47.11866 | 2025-10-07 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a52a5af0-620a-3058-a876-869dd42db97e | -23.20829 | -47.24203 | 2025-10-07 04:12:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 032bad53-0c52-36ab-96ef-63a359d4a3d6 | -22.01029 | -49.72857 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a884873a-1872-3a85-b057-b33747b1d5a1 | -20.50846 | -47.01404 | 2025-10-07 04:12:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fa5a1e9-ec2a-3333-9fea-4e94a949a375 | -22.00832 | -49.71774 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 601058d7-4cbd-3429-aeb7-b73a3e3f358b | -22.17875 | -42.47058 | 2025-10-07 04:12:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 20c9a7ad-d7ce-3edc-bee0-2bb97b07bc9e | -22.01972 | -49.72004 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 233d0240-2fa4-3e85-a1df-73174533dde6 | -21.9998 | -49.7212 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6057315d-39a3-30dd-88f0-a39a436a5194 | -22.54444 | -44.45763 | 2025-10-07 04:12:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0d051fea-db03-31cd-ad8d-2d3e1f3be6b1 | -21.39569 | -45.05229 | 2025-10-07 04:12:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3084b668-9045-32be-9c96-989057022e48 | -21.08003 | -46.89987 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4665fa92-5f11-3f53-b819-10271305aa06 | -21.76784 | -47.78307 | 2025-10-07 04:12:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17cc4cd6-a386-301a-a641-089e6a3d2f81 | -22.0036 | -49.72202 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bf8c1fc4-8b08-3d9a-8259-edb9ed704cfd | -21.4912 | -46.01302 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 983abec2-e88f-3c1b-b3d5-1f67863ff0d9 | -21.6191 | -43.99337 | 2025-10-07 04:12:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1160ae58-74e7-3e76-9c56-00ca5257c790 | -22.01355 | -49.72631 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c5cffb64-b92c-31bc-a852-d0f0ef2452e0 | -21.22973 | -47.55061 | 2025-10-07 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f1672aa-f577-3128-b756-e1567ccc1b87 | -21.03215 | -46.4262 | 2025-10-07 04:12:00 | NOAA-21 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08a3f93f-e0bc-3178-807d-71d3dc92c22c | -23.31554 | -46.94057 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4173b568-5bb5-3717-8a87-219ac4235e2b | -21.57256 | -45.26922 | 2025-10-07 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 962207b5-bef0-3c72-bd50-7b782c85c11f | -22.99792 | -46.15294 | 2025-10-07 04:12:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 503435c7-20a3-3bfd-8c6b-87a046547765 | -21.74469 | -44.4213 | 2025-10-07 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c53e8d8b-929a-370e-a7c3-9e7a6e08dc50 | -21.57644 | -45.26613 | 2025-10-07 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 55f0b00c-fa5f-31e5-bfab-67a16e341161 | -21.57973 | -45.26672 | 2025-10-07 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 490ce385-68ab-3d83-9966-ad96383266b2 | -22.09222 | -44.79461 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b163200-8a44-3ae1-a31c-33aaecadc0ff | -21.85369 | -44.99617 | 2025-10-07 04:12:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 85e9e745-7812-32c9-a47a-a15329fa0889 | -21.77131 | -47.7838 | 2025-10-07 04:12:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 562f2409-832b-3d19-b7bd-8c98d0a25ab5 | -22.17988 | -49.37362 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 199ff58d-8385-36fe-bb72-cf91d9237cd7 | -22.0183 | -49.72203 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| cc6d2467-a49a-3aac-8b70-c0e62674602e | -20.58477 | -46.30552 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca0009e0-8828-307a-aa8e-7abdcc1f982b | -22.01591 | -49.71929 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5e40fad6-16a0-3c5f-b0a8-5b0f60d78c95 | -21.49332 | -46.02107 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f07c54e6-8628-3d4d-a730-8e98ac12079b | -21.52053 | -45.59796 | 2025-10-07 04:12:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 86583c45-23e8-3967-a54c-4834cab81f3d | -22.02211 | -49.72277 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 123fc0ed-75d4-3856-b161-947c1bb17f22 | -22.17443 | -49.38249 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60459461-1203-37f1-b29b-db33485b651d | -21.30359 | -45.95257 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 348ed366-15b2-3e69-b630-a2fbaaf15b31 | -23.38171 | -47.19766 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37d15e2b-10f8-3ff1-add4-c44e91e6e7ca | -22.00739 | -49.7228 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 75e53c75-eafb-3109-a87e-ccf05d5f0948 | -22.17355 | -49.38738 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f1de7c-1f1f-35f8-a841-4006ce70e390 | -23.37809 | -45.38424 | 2025-10-07 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4a12b3c-39e2-38a7-a215-8e097978f53a | -21.74525 | -44.41759 | 2025-10-07 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 60b61edf-0249-3a99-a121-21f2be3fe4b2 | -21.61186 | -43.99606 | 2025-10-07 04:12:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 85b0e2ad-912b-3d8a-82c5-f3f988804a97 | -21.10127 | -44.20531 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b74d0f55-ef9c-326d-86bd-0486c1848875 | -21.57728 | -46.40523 | 2025-10-07 04:12:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ee644ed-f829-3d8f-8e2e-a18ad197d8be | -22.54572 | -44.98397 | 2025-10-07 04:12:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 31944de0-531e-3afa-82fc-63d96de6840e | -23.23719 | -46.71243 | 2025-10-07 04:12:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b596f6b-dafb-3819-b59b-1334b8aee29d | -21.10403 | -44.20959 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 330f9bbe-3320-373e-9f8e-f776ebf4ae86 | -21.18825 | -45.67533 | 2025-10-07 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a9bc4f9-c26b-330b-ac28-aef0d19f9204 | -23.3728 | -47.16788 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 833e3f60-389d-3fce-9417-46bc7b4fe5a8 | -23.37867 | -45.3805 | 2025-10-07 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 07b34aaa-a0a5-3e69-8019-25561bfc5493 | -22.01318 | -49.73432 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bdd260cb-151d-3e26-9e47-c2d4ccaf8db5 | -22.00618 | -45.12933 | 2025-10-07 04:12:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a63fe163-7041-345c-8581-4e0cc8ce465f | -24.06083 | -49.62288 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f17c9dda-008e-3525-a409-d87b59061924 | -22.17813 | -49.38334 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 44db4672-ba41-3b55-bf95-411817a9c6e7 | -21.31629 | -45.21217 | 2025-10-07 04:12:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d4d5ec0-1015-3000-96e2-80eb2fbddc35 | -23.19206 | -47.23492 | 2025-10-07 04:12:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c54457cf-8571-3235-b86b-1682020b49c3 | -22.01409 | -49.72932 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eba5b62f-5594-39c6-bb3c-e9bc13f6673b | -23.22774 | -46.56113 | 2025-10-07 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2bca6f0-7acd-3457-afae-97e3f3965e94 | -23.16343 | -45.56059 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c7da4e1-16b3-3049-880c-f56a142f1b92 | -23.26385 | -45.50554 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| bc54bd79-1dde-348c-9bb3-d1be4f4ac063 | -22.01544 | -49.71628 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| f2b5bfe1-159d-3f22-9ee8-7fdf90806abf | -22.54833 | -44.45448 | 2025-10-07 04:12:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c784cd25-de47-3481-9540-58af53d04edf | -22.16984 | -49.38655 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c80500e-9a59-36c0-b0d1-e27538b4ba7e | -23.37899 | -47.19315 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8cac1865-d1cf-3750-9e51-fbb5db8b54b5 | -21.62074 | -45.28871 | 2025-10-07 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eac73b62-1a10-36de-8dbb-eb15df52c647 | -21.05657 | -46.23555 | 2025-10-07 04:12:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73f6f8f8-165b-3069-bb71-4b243c21ed5c | -21.48861 | -45.84036 | 2025-10-07 04:12:00 | NOAA-21 | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ce772629-e4b2-36ea-934e-340e0f259758 | -21.90834 | -44.88428 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 5bfd37e8-9149-34a3-b6cd-cc5dc90daa1b | -23.13356 | -47.11913 | 2025-10-07 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05977322-ac82-3911-ac0f-d6ba097c09ab | -21.90446 | -44.88738 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ecc59c7f-9d5e-3355-b990-c6e763148a07 | -21.90504 | -44.88369 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c349d6e-4967-3e13-b7f1-b81e25b4c6cd | -21.52112 | -45.59425 | 2025-10-07 04:12:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2858713d-a39e-3bc7-b948-dca0894021a0 | -22.23668 | -47.59623 | 2025-10-07 04:12:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 144f17d7-62ce-3741-bbd5-ee09ba6f4b5c | -22.795 | -54.66865 | 2025-10-07 04:12:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b9501b75-4a54-3469-bfd3-9145daa439c4 | -22.38897 | -43.97593 | 2025-10-07 04:12:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c964271-8ad0-3192-92c2-11b04e479774 | -22.78996 | -54.66746 | 2025-10-07 04:12:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 4e71cc05-af7c-391a-989f-80b320233253 | -22.01682 | -49.71428 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


[Clique aqui para ver as próximas entradas](README48.md)
