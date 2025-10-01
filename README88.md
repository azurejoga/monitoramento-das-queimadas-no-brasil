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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 703d0997-e5e3-352c-9566-f7dc826bc265 | -4.91344 | -48.4178 | 2025-10-01 04:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b058eb9-d978-3f1f-a4a3-1e43f05f3b11 | -6.28134 | -43.65385 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e47324fc-0a7a-3448-a9a2-c395a7cbaa5e | -5.85986 | -43.40253 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ae4f75db-7086-3542-b7d1-3414baf45163 | -8.85946 | -47.65195 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 673a8e0c-023d-3f46-ba87-95a554043d06 | -7.21623 | -44.75549 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86d3c5a1-add1-3ba0-9a3f-fea77b7057e1 | -6.48408 | -52.84373 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24714804-54fa-39d2-ad8d-6c97084f9276 | -4.00875 | -43.2763 | 2025-10-01 04:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6a511f7-27e8-31eb-b88e-5e95134adb35 | -6.02901 | -43.77755 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32c7fa86-a9df-358c-a688-011ecf2e7aca | -8.58837 | -44.7364 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20574665-db55-3182-befc-19357c34cf97 | -4.39961 | -50.84797 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3dc577d8-66e1-39eb-9e75-6b5b23e827b1 | -5.78575 | -43.30038 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f195698-2fe1-366a-8dc5-6075dcf4830a | -7.62841 | -45.45009 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 702efd1d-b5c0-300b-9312-53e7d8208854 | -5.47491 | -43.07379 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0036ad51-b163-389f-8926-bc7140aa68b0 | -6.45999 | -43.94117 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33758a21-6373-35d2-9496-f1d8bee51c76 | -6.72911 | -49.63804 | 2025-10-01 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 900ec187-e765-3e8e-a1b5-0151a10199a8 | -7.79802 | -42.51306 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0d6feb4-6e00-3ef9-9b38-b064dfe15675 | -7.02194 | -44.47612 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9852eb4-b3c6-3a81-a9c6-d7f874e6c9f1 | -8.52306 | -44.66948 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17569eb6-09eb-3759-8dc5-02bce2ffe032 | -7.0524 | -46.4211 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e380075-7ba4-3a80-9b72-352b2021954b | -6.79383 | -44.74302 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bf602bc-d2e6-3e32-9966-54ae3155d018 | -5.85504 | -43.40187 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0b9b0b9b-d0a4-3e0e-b78b-335a0eab45d9 | -6.10307 | -42.68139 | 2025-10-01 04:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3bfe8311-a01c-3b6a-a6f9-72771a7d49d5 | -8.16842 | -46.24804 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 692d0b25-ec8b-3f5c-aa38-ae8e35a4edba | -5.94893 | -45.87344 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77e42265-0e14-3936-8fad-0e006d594dce | -8.55302 | -44.72258 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fb53bec-41a0-31cc-920d-cdf3468ac6ba | -5.99069 | -43.43546 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 407bab65-48ff-38cf-8c58-1ddf486e2dc4 | -3.09199 | -47.00668 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| fa677a9b-c23a-3a19-accd-029adb7787d6 | -7.79319 | -42.50922 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a52387e5-e187-3829-9a99-786e2824ff11 | -5.94061 | -45.90099 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79e97bdb-3588-3236-a453-6a530047b81e | -3.52093 | -49.44609 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6921fb7-6b4c-3f6e-a61b-5b016b4693d5 | -5.98385 | -42.6564 | 2025-10-01 04:49:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3edee38-c074-3ff0-bda8-826f5f009d66 | -8.16278 | -46.25834 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daecf9a7-031f-3f31-a4db-efeae4e22dea | -7.09247 | -49.17716 | 2025-10-01 04:49:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c083d5f9-9b5d-3be5-b23c-b2228d8f3ef0 | -4.15302 | -44.85748 | 2025-10-01 04:49:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1b8c887-355a-3f08-a8ee-fa86d39f91f7 | -14.50457 | -48.44279 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4156d0f5-cda2-3f62-bdde-6f40f79d8393 | -11.47463 | -45.09581 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eb267b4-7045-3768-a826-0269b3730517 | -14.69107 | -48.12457 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8ea434e-0a40-3d26-a4f4-bf0b33bd7eb5 | -16.40219 | -47.04358 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a47e09-df52-3847-88ee-6f2c5190d142 | -11.82648 | -44.96362 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8fe2d12-5117-32d1-80ef-6067b7fb2692 | -14.34671 | -45.90411 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68542ffc-fb5c-3c32-8bda-933996f571d1 | -14.95126 | -47.51331 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb492f5f-392c-3a66-932d-cb4908ca5a9a | -15.2766 | -52.8957 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b739d8-e92a-38db-b2ba-1c53476f5345 | -12.39717 | -44.75866 | 2025-10-01 04:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d65d2c0-dd10-35ca-983e-0088c6fa7fbe | -14.92597 | -47.81758 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f27a95f5-07f5-30be-a2dd-6d68a6fefbac | -11.83758 | -48.06344 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 38df4f16-42cb-3d1d-b8b9-4e29b7e3f2e8 | -13.78351 | -51.21728 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 966333a0-9981-3623-87ba-e3cfa30ce3c5 | -11.76187 | -46.86806 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad0d80bb-5606-3f2d-9101-2a55d8f5e0ff | -11.29745 | -54.88684 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb96499b-8bee-3231-a3a2-2db3d90d5eb5 | -10.48122 | -55.62243 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f214fd12-816b-32ee-a691-b6c1557d1eb4 | -16.0191 | -50.90905 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7560ed87-9596-3d76-bd30-da183bab3108 | -12.41594 | -44.09542 | 2025-10-01 04:51:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4704f0-25de-308c-868f-55375da58868 | -13.37326 | -47.31758 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e86b3a4-b531-39c6-a3b2-bf4687f87dd4 | -11.19202 | -47.19846 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dc50911-8614-3266-a416-2279a004c51a | -13.33295 | -47.81776 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eeb906e-dda4-3b8d-8434-e3d68a1326a4 | -14.60283 | -48.21993 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b5d5ce2-d1e6-3a96-a7fe-4ab006232e8b | -14.52689 | -48.36522 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80b7204a-5884-3164-89a5-d985e6d5e615 | -10.64362 | -48.53372 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 85a53081-836f-3bb4-96f9-fd5623ca9397 | -14.61437 | -48.31102 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31df9131-f451-36a3-891d-c1a6adba5346 | -16.05751 | -51.01236 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 352c08d2-0473-3b18-a153-c56bdec2d7b4 | -13.16659 | -47.7906 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ceba8bd-121e-33ea-8df7-92dba144ab1b | -14.61367 | -48.31606 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aad196dc-e2a1-31df-813d-44257e15d98c | -12.97799 | -48.42329 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ff25cb5-55ad-33fb-ab56-f4513e2cdd9e | -15.48642 | -45.91026 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79952091-5ec1-3c72-9172-245230953baf | -12.28103 | -47.83056 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62885150-0f01-3957-a748-2cae65111ee7 | -15.12711 | -46.45655 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e926d542-4490-3898-8316-1b2cf6553496 | -14.91341 | -47.82043 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c382c5-de68-32d9-bfcf-7949863daa38 | -15.31254 | -46.41016 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcb76a4b-c611-318d-b711-ba8cf51c819b | -14.51127 | -48.48101 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c5e1e770-af3a-33b2-9a31-e6f73f4944a4 | -10.75025 | -45.37107 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6db9c433-5e1e-3167-a212-0a38c0027d00 | -14.72405 | -48.15065 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc9fb1f1-7329-3b97-b478-ac4b1ec83cee | -15.2353 | -48.7369 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9e3e6d3f-24ed-3429-9d62-cb800f23e200 | -12.956 | -46.42241 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b06259d3-d0b2-3d6a-b2d8-035d99a1b2e2 | -11.84271 | -44.98607 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 856f74c8-23db-30fe-b501-70272499b8db | -9.56808 | -50.94645 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44a3f4dd-a0e8-3bf2-9ac1-735e3521c880 | -13.17658 | -47.38754 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46083c56-5fc4-3ede-9a27-e9f0da12172c | -15.24479 | -48.73461 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc6ea41-ad51-35fa-8dde-c80d8b44fef3 | -13.76798 | -48.41028 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f204d0a8-3d5a-31a6-88e6-836ab340fef4 | -9.92414 | -43.6741 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e567fa92-9f99-3e5d-bbe8-54e3eaed495c | -12.8362 | -47.04408 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94c1fc9b-22e9-36c7-949e-57a9a9bba8b2 | -13.91837 | -48.08245 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69f44483-c9e9-3406-bc98-d9300133257c | -13.06168 | -47.08718 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccd59a07-050d-3932-8acb-e532b0ca394b | -15.99673 | -51.18321 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 657ee1a9-cea3-324a-b490-67c6c900e86f | -15.23832 | -48.75321 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a993b4f8-be9e-335c-a7ac-494a04449d75 | -14.53088 | -48.36951 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a23352c1-90a4-32aa-a488-bb445e34def0 | -11.39805 | -44.90021 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2caccb57-5323-39e3-9380-c59820d91135 | -8.94551 | -51.68261 | 2025-10-01 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a6f2dee-411a-3376-9e10-fb19cfc2b038 | -11.06297 | -47.82086 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5b86929-4d54-329e-9074-c65616d54112 | -14.70223 | -48.13218 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ce1e9cd-e8bf-325e-bb79-0d44b3f44ed4 | -16.40876 | -47.06055 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e27031a6-224c-3085-a577-4170f02eaf8c | -16.0226 | -50.90958 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 260b4cac-0925-36dc-adc3-8ef0c1a675c2 | -14.18652 | -46.10552 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 385005aa-85de-3319-bcc3-c0cce237df3d | -16.00982 | -50.89901 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e777336-3d4d-364a-9663-be7deea6e883 | -11.80385 | -46.62392 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 6e1cf7e6-b9d6-3cad-8e21-4e553a8ebc37 | -11.38008 | -45.07156 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f07952a4-9cf9-3e61-b447-f4f90c1b02b1 | -9.40544 | -54.71778 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eea9d08-2809-3920-a53b-8d42e8e09a25 | -11.4666 | -45.08487 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0826f053-08cf-3e41-888e-126ce474a38f | -10.90761 | -46.56151 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89e8efbe-bbe3-356e-8a32-ecec406638c8 | -13.72861 | -48.81649 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bfe3786-2523-3a58-bfeb-9f2bb62975c9 | -11.16411 | -54.11592 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0b1cc5-a610-3864-a9fb-8775826758de | -15.24127 | -50.08523 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README89.md)
