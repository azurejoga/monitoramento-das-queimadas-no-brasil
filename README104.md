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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ce210aa-1699-344a-9430-14240e5d2685 | -10.09121 | -59.16464 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81e200d8-c99a-376f-a8f3-67f27d86c118 | -7.26789 | -57.57506 | 2025-09-13 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31eff653-42aa-34a6-9a77-c410be565ba3 | -8.3604 | -62.7601 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91331778-4c19-3a8e-8527-75665af1d185 | -9.49775 | -55.96777 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 862d8603-c8e1-39cb-8588-db624546e75b | -9.24215 | -51.22602 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79e35dd5-0642-32a4-86a0-b9b77cab10fa | -9.80708 | -61.51638 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d3f6bb-b801-34e1-bc5e-e42ec059a20f | -9.24485 | -51.24955 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 21565165-0694-380f-8e23-f155e5fff567 | -9.23971 | -51.24495 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3d14600-dbdc-31d4-b3bf-9b217ff78f96 | -9.49882 | -55.96037 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79b73392-9b65-3d62-be0f-428753402654 | -8.27425 | -64.05204 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d3f7064-d4d3-30cb-ba10-5af05c2c03c5 | -10.3714 | -50.5027 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4513fa1-7c81-357f-8ec3-4db525e09478 | -9.49721 | -55.97148 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6ca4fab5-bcd8-31b8-a3bc-460464ab53e1 | -10.32898 | -58.01994 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71332624-8db0-3033-b9a2-c0c60f42ff7d | -11.18469 | -51.41815 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 34f4729d-75b1-327c-8a1e-6dff84e631cd | -9.23726 | -51.2639 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5d47c70-b412-3f0f-b575-fba5151643bb | -10.40162 | -60.81509 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea5cbdd-9c59-343f-affb-32b1e1dfbfcf | -3.43758 | -59.57078 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac3b7205-1caa-31af-ab52-defb8a734c98 | -4.93116 | -55.78377 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01733c32-9783-3156-864e-c3984e32d4c9 | -10.79198 | -50.53629 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78f0e711-3778-3930-82c7-dc575801de97 | -9.70532 | -47.5338 | 2025-09-13 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7e0a503-e7c4-3d54-b14b-a0e316789aab | -11.10036 | -51.4355 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5264c2db-4783-3da1-a166-9dfa0b1748ba | -11.0874 | -51.4314 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac354d0f-c924-3879-a10a-47b441fbc744 | -9.80486 | -61.50884 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8a06bd4-752f-3e35-84c0-fd59e3a4a806 | -7.66676 | -61.12336 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b673755-0c90-3eb6-bd53-2725e1856b5a | -11.13522 | -50.71783 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1220123f-303a-31aa-89ab-602b3b91a77c | -9.26872 | -59.41345 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2d498ad0-b157-3a73-8d29-de39781e882f | -5.75643 | -57.57718 | 2025-09-13 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 391f7bc8-d045-3071-8785-bd94ee72b2ad | -9.27727 | -59.40336 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d349cfe3-7656-39a0-a2e5-5526a12f8209 | -10.64715 | -48.97102 | 2025-09-13 05:25:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce0e5087-4753-3c5f-b8a6-1cba765cd4aa | -10.51468 | -51.54112 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f8e4ace-2010-3fb0-b8db-38ea9562bee5 | -9.80116 | -59.10331 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f414b50d-cd01-36b2-b3b2-3b62f1a9fdf5 | -11.77632 | -50.55367 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43951b42-e0b8-3935-98a5-928d83e82485 | -11.57547 | -50.57192 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 497bc242-2f76-3479-a959-8512341f60d6 | -9.27158 | -59.41769 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa95c334-8d3e-330f-b2e7-2510bd6cab7a | -9.90653 | -60.21249 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ccddf9d-d4b3-3198-9d18-74a856100070 | -10.39939 | -60.8075 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bad278f6-bdfb-3064-9cca-ccedff6b4c3e | -10.36596 | -50.49748 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcf3bf35-65d8-3f63-90d4-4cf85129a147 | -11.41958 | -50.73885 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42751c51-ed3f-3fc0-aa1e-af3384e915bc | -10.32523 | -48.82931 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e643be1c-cdc4-3eb9-8e94-4e5a2bc29ee6 | -11.09261 | -51.43607 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c7e6d97-cbad-3866-b78b-ed06f27ba769 | -11.04368 | -51.40974 | 2025-09-13 05:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b76a214-43e2-3b74-890f-e1ab5e144687 | -10.42182 | -60.465 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0f4eff5-7fe2-32d9-afb0-b204d2031822 | -11.18483 | -51.41044 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| e535910b-6cc7-3518-a5fb-004d5b2cfba5 | -9.49471 | -55.95979 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb4cef06-b8d2-37d0-ab67-160177c35c1f | -11.83233 | -50.55126 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d13f6f2e-386d-3960-ae01-99c5e74fdec3 | -10.51326 | -51.5522 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05dc2663-93c3-3486-b031-949a56bbfe8c | -9.25958 | -59.40442 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5e3ff592-b4ae-3c85-8cf0-fb2cd4059c6a | -9.88825 | -58.33565 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88ea52d0-41a4-3527-9f3d-7d9b150b8b3b | -3.44145 | -59.56784 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5000ef19-b9eb-310b-b11a-f28636fffc6a | -11.81526 | -50.54336 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fe11a935-1a8f-3a71-b00b-77fb2a88cde7 | -10.51922 | -57.76792 | 2025-09-13 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7477159a-51d6-30ba-9cbb-4bedfcd78491 | -10.48742 | -57.95815 | 2025-09-13 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b110d9e8-057e-37cd-8b23-b311aed28723 | -9.7351 | -51.01041 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d697d7-dca4-33bd-bf3f-1161a1f06472 | -9.16576 | -60.30572 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 253a3b55-92c6-3330-bdbe-8facfac6c6a6 | -9.32157 | -60.27516 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 682b7d65-561c-3814-a60a-bc66910f997e | -5.3477 | -47.28859 | 2025-09-13 05:25:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9461791-96ee-37ec-bfad-b08497acca6e | -10.78365 | -50.53789 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb7a4a08-0f62-31dd-9505-ca852ca064fe | -10.33265 | -58.0205 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ebc847-acc6-38ea-bf68-671b6b20b146 | -9.28173 | -56.89898 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d1f589e-df8e-3220-be18-38c3cdcb5238 | -9.89716 | -51.86569 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 752acd08-ec9f-343b-a349-e60e29def378 | -9.27271 | -59.41027 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0813b33-c6d7-39c7-b79b-b5fcfcc3fca5 | -11.09933 | -51.42895 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 13f2014e-6aaa-3a41-bca0-ed12d7554699 | -9.12247 | -65.52048 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bbfe54bf-e16a-3b30-9980-27f03efcec21 | -11.0837 | -51.4293 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5dfbeef6-a637-37a6-882a-1661c9bac643 | -10.36773 | -50.50144 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fce0678a-27f5-3c8d-9250-cc6f7e768a2c | -11.08846 | -51.43795 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 494ea346-ad06-3416-9dff-eb43ddb49d59 | -9.37006 | -59.48187 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afdcb108-a0ae-3258-ae86-9e6ff83de049 | -10.36172 | -50.50064 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7827b15c-1b7a-32d2-956c-461cab6f9d16 | -10.70272 | -48.6524 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bc54d8a-1dc5-3961-8bfb-c7be49eb318c | -9.28533 | -60.18958 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cfc909b-c968-3141-a0d7-09c10c1cbd94 | -11.84756 | -50.58514 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68b7ef21-d52b-37f2-92ca-0e334e879b9d | -11.1796 | -51.40574 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 297c7360-c5e6-3b2b-b270-10e78681a736 | -9.20412 | -60.62271 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5092a6d7-b40c-34de-afd6-3e63d7fbd865 | -10.50415 | -51.53399 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58dd9be1-cfa4-3aca-9eb1-061f45e9d276 | -11.10511 | -51.44415 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d56ad5c1-364b-3245-9a7e-499c2419f254 | -10.51373 | -51.54857 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd5ac659-63b8-30ab-a2b0-23a3e12064c5 | -9.23456 | -51.24035 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4c7be40-bb33-3d66-921e-a8b1ed89ca36 | -9.28924 | -60.18655 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 766a306f-40c4-3d8b-b1f6-9f8b2ebe687a | -10.09526 | -59.16137 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cfc7015-a6c3-3b30-9166-f618974c6903 | -8.27506 | -64.06934 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 025eb5a5-89fa-31f2-bd72-922ff999d047 | -11.77687 | -50.54903 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f05d5d-5375-3822-b963-ec0d2c8cccc5 | 0.69057 | -50.64855 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 74ae2a6b-bf03-330d-b0f7-a42cf8e5e2fd | -9.73942 | -65.0111 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dbeb70f-895c-32dd-8f10-35008b1ab0eb | -8.27064 | -64.05144 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dac74991-7082-35da-8f54-1ddb0b8318dc | -10.6495 | -48.97696 | 2025-09-13 05:25:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1fc39b2c-b342-3497-81d3-4db873189f67 | -10.77497 | -50.52491 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72a907dc-0361-3633-8d1f-bfaf08d526bf | -11.40758 | -50.7373 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2387c597-3ebf-3088-bfae-a4d8cd946721 | -7.67009 | -61.16682 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d89ba51-0140-3f7d-a1d5-1b6521c86599 | -9.83619 | -54.5349 | 2025-09-13 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fc0687-15d4-3204-a8ff-5cd9c1a97b43 | -9.25136 | -57.06667 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcf4c44c-bec5-3c3a-939a-8cea59ca61c5 | -9.69203 | -59.21525 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20fc2ac3-029c-34bb-9149-fc14e65f9250 | -11.85026 | -50.56197 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e9ecdb2-ed2d-3ab5-b24c-287a7fad0126 | -8.27717 | -64.05682 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41719d0b-10e8-30dd-8633-15fa0e523150 | -7.96812 | -55.30666 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd6d5d23-507d-3559-8eea-3da5fc7f8414 | -10.70912 | -54.4448 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0934281-a1c9-349f-b9db-5d5d37e57746 | -9.90532 | -51.88855 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6c2fcd8-5ab0-31a4-affe-3151c7d4dc5f | -9.25559 | -59.40763 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95f7f425-b193-3b09-931e-ee21d9faa228 | -10.51847 | -51.51157 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca92e84-01af-3169-aa76-33424ef2a5bb | -9.79987 | -61.51882 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7a92ef5-f9dc-3f02-a6e4-b88896d083be | -10.36827 | -50.49698 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README105.md)
