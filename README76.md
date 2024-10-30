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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d86a7b52-e706-3968-847d-08491f8b3e17 | -10.44462 | -61.27945 | 2024-10-30 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d92685f-d86a-38f1-890c-983c2dfa8099 | -10.08716 | -62.17366 | 2024-10-30 04:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12aef8f2-6d56-346c-ae2a-62dfdf0492b9 | -8.86085 | -64.23875 | 2024-10-30 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d411ff58-7dad-3b1b-9fcf-2c308aeb33b5 | -8.85971 | -64.24458 | 2024-10-30 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a61f54c-f2bc-3fc4-8bfd-0575d66d6cbf | -11.29069 | -41.86262 | 2024-10-30 04:46:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 51977d12-c715-39e7-a88c-6bf12c151975 | -10.8668 | -42.93523 | 2024-10-30 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce1644df-ff21-31af-98c1-52d90d0acb87 | -10.86245 | -42.93481 | 2024-10-30 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ca9abd5-7844-3cb7-9310-ea4204fa8bc4 | -10.86151 | -42.93449 | 2024-10-30 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f46edee-07a3-3dbd-946e-50c8e2e16175 | -13.47633 | -43.25793 | 2024-10-30 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 351f9213-7b73-3812-8781-1989da960113 | -13.47594 | -43.26135 | 2024-10-30 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 675514a6-3b67-388d-8c21-d6112a26e93b | -13.47401 | -43.2585 | 2024-10-30 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 94e5dd32-c729-3f75-ba80-e469b41d2b5b | -13.47359 | -43.2619 | 2024-10-30 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1777e4d0-f479-3810-b07d-8764a64c6984 | -13.57024 | -43.42472 | 2024-10-30 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 894c1e28-8742-3b82-908e-c0879ba6199d | -13.90024 | -43.35284 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 249f50f2-3312-353c-979a-3d58cab7af39 | -13.89985 | -43.35627 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6942ecd9-5462-3c35-ad11-c32f70604b40 | -13.89791 | -43.35341 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 149f6d1f-58b6-3835-9efa-1928e74c8201 | -13.89749 | -43.35683 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 13829a7c-3809-3eae-9cc4-fddacea60211 | -13.89488 | -43.35213 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cca90a88-e28c-364c-a009-af071c71deca | -13.89297 | -43.34931 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d5b0bad-8f0d-3934-ab11-2911f8b940d3 | -13.89255 | -43.35273 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a542d04c-44eb-3e13-bd58-fe159b2b4e59 | -13.88951 | -43.35145 | 2024-10-30 04:46:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 727e17c0-9698-3fcd-b457-b866b3445bfd | -11.88197 | -43.82417 | 2024-10-30 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19f6deb3-46c3-39c7-9b0b-7f29f60fddc4 | -11.88159 | -43.82713 | 2024-10-30 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5466c015-914b-3ac4-baaa-8e980cf2e3c8 | -11.7401 | -44.32505 | 2024-10-30 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a70e12f2-cbe2-3f54-8c76-c7f41dcbd154 | -11.61739 | -43.90786 | 2024-10-30 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caa610da-7912-3391-bc2c-18feececdeaa | -11.61239 | -43.90718 | 2024-10-30 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b9e19f-a1d1-3e99-9b83-16c626f685aa | -10.86891 | -44.41214 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dbc4b18-26e1-36f8-8f93-2126d3d8aaf5 | -10.86411 | -44.41159 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b62c429c-acb9-30a0-98f5-49ece2a603b3 | -12.88334 | -44.62008 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ad60b5b-ab68-323f-878e-8ab8186e6b01 | -12.88085 | -44.61902 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cfc2be4b-3cb6-33df-a239-73eab4226658 | -12.88013 | -44.62454 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e76b0d11-014b-342d-810f-3d29e9261a00 | -12.87916 | -44.61396 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66e19936-abfc-3f54-aee9-464552baeffe | -12.87848 | -44.61951 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7afebd56-a041-33f3-9cef-a4cff7fc85e8 | -12.8767 | -44.61292 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30febfac-cae3-3be7-b6d6-f5ebf4b343b0 | -12.87598 | -44.61845 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e9e395c-f0c9-301e-83a4-1d85a3c6a0ef | -12.87111 | -44.61788 | 2024-10-30 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 447b1cea-3005-3e54-af01-a2a0f80de561 | -12.28727 | -44.2621 | 2024-10-30 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f22ada12-3be7-3394-b683-659a579bdd43 | -12.28361 | -44.25803 | 2024-10-30 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f3a9c71b-8996-34ef-8d52-83474e56004b | -12.28306 | -44.25593 | 2024-10-30 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c40ff95-3558-3ff1-a5b6-ee9e6dbef2d0 | -12.28292 | -44.26366 | 2024-10-30 04:46:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a9116509-f606-34bf-a0f5-9d81bfec9e24 | -12.28232 | -44.26154 | 2024-10-30 04:46:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed9ddf26-db81-3ce8-a7be-5b3d0b34f022 | -10.87713 | -44.53706 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06036ed0-d307-3f61-a1d3-4e3387ca4c93 | -10.8759 | -44.53928 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d9c4c13-276d-3d41-952a-636e33d8c4dc | -10.87239 | -44.53641 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87716253-bc3a-3f74-8a30-6f04fa0d673f | -10.87174 | -44.54145 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96b83435-3d65-332a-afad-151ca0ea3383 | -10.87116 | -44.53863 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d7b9010-58e7-3c87-b3d4-e63e78b96c04 | -10.77306 | -44.62418 | 2024-10-30 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db0fd431-5a9c-3685-8783-2597d5dd133a | -10.71642 | -44.9226 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ce581e3e-ed7e-36bc-8b3c-c9a928e2ff6d | -10.71575 | -44.92739 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a266ca92-f0b2-3ae5-8fc1-a712550688b9 | -10.71549 | -44.91925 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34e7af50-5978-33b8-b628-e5e5fba73523 | -10.71487 | -44.92405 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 4468e368-1dd7-31d4-b137-4bf1ee22a80e | -10.71424 | -44.92883 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| efc5e9b5-030a-33fd-afe3-98a96cbbeaf0 | -10.71181 | -44.92192 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6e8b879e-f158-35b1-8296-62fb37ea48d9 | -10.71115 | -44.92671 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5d6eb39a-24ab-374e-9689-87bf4e601b6a | -10.71026 | -44.92335 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 71e7d295-0bd1-381e-b857-45e28bbfeb25 | -10.70963 | -44.92815 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ba6d3631-ed22-3bb5-877c-71e75fb514c6 | -10.6373 | -44.88206 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cacf02c-9448-3869-ae5f-8e4125cb7cb8 | -10.61074 | -44.944 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcfe71e5-470b-33c7-86dc-5fefba4db715 | -10.61073 | -44.94112 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d409e2f0-6a51-36d4-bbf8-4093e5f7c66c | -10.6068 | -44.93866 | 2024-10-30 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1c01bc2-147e-3eff-96cc-6edb268f4e28 | -10.60606 | -44.63277 | 2024-10-30 04:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6906ad7-c42b-37c8-ad2f-d77b98538bb0 | -10.49516 | -45.1093 | 2024-10-30 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72442e7e-cd6b-3260-b4d5-7edc83a9940c | -11.38328 | -45.14783 | 2024-10-30 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b65920f2-59cd-3073-8779-9c76528ef4a0 | -11.38265 | -45.15252 | 2024-10-30 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bf28165-a085-3a07-8cfe-6b37fd265b43 | -11.0604 | -45.3677 | 2024-10-30 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dea28204-1af9-3689-a9f8-945960eabd9b | -11.0559 | -45.36715 | 2024-10-30 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b020991f-a239-3bf5-afc1-18ab3a2592da | -9.58002 | -46.64211 | 2024-10-30 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abe3c2ac-fb6d-3e97-b967-7dd3d7d2d56e | -9.57952 | -46.64558 | 2024-10-30 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d1dfc01-67b2-3f0e-8278-fef45e21f688 | -9.57599 | -46.64143 | 2024-10-30 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b543ecb-1231-3166-b506-78dc1bad32f7 | -12.31913 | -46.75804 | 2024-10-30 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 743bafde-4551-36a2-9b0e-aba79c8dc5fd | -12.13934 | -46.99277 | 2024-10-30 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07a226fe-4ecf-39da-85c7-dc2c3d4909a6 | -12.09577 | -47.24281 | 2024-10-30 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20a97997-c0d5-36d1-8d45-f0a2ac7d355c | -12.09175 | -47.2422 | 2024-10-30 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2253a1aa-a0eb-3766-addd-4f30ab8d6f06 | -12.09125 | -47.24574 | 2024-10-30 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55f0d0e7-0a78-30a5-92b0-9d9b2a88b890 | -12.00122 | -47.65498 | 2024-10-30 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b360893-a088-3315-a7dd-f00f4d75dab2 | -11.99455 | -47.16679 | 2024-10-30 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2262d5e7-8f5d-3392-b9d5-deed0793b185 | -11.8856 | -46.5334 | 2024-10-30 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7efe4928-5e06-3aac-90b5-88619f8459f3 | -11.8814 | -46.53277 | 2024-10-30 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e1c5948-3b06-3eee-bea7-64b14296d6f6 | -11.88086 | -46.53667 | 2024-10-30 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aea4966e-4a8d-3cef-8b6e-1b9807c7f226 | -11.7848 | -47.07124 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3beba120-d55b-378e-9d0a-c0b7b15e6373 | -11.7843 | -47.07483 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 641c4ec3-690e-352f-b96b-2d1a8ae3841f | -11.78075 | -47.07064 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f21b25ca-fe5a-33cb-9953-7956cbee080e | -11.78025 | -47.07425 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d8b82253-d502-39bf-ab2e-f1c9247b1933 | -11.77518 | -47.08092 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d18cf46-3901-32b2-aa40-adb3e7a8813b | -11.77468 | -47.08452 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0087ef8c-32b1-3e4b-b679-39a190f16828 | -11.77164 | -47.07674 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1aca5c8-c031-384b-b42d-6dbf68f2e04b | -11.77063 | -47.08395 | 2024-10-30 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd97aaf7-b5d4-39af-876a-21d624d7cffe | -11.48188 | -47.17261 | 2024-10-30 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fda1e520-2e2f-3990-a4b0-7233762f5b2f | -12.43037 | -46.63055 | 2024-10-30 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f1cba7-cc59-37e7-972a-2bd758155103 | -12.2593 | -47.69084 | 2024-10-30 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9a21ebe-77ba-314a-b8c3-66fe7fff09d2 | -12.25828 | -47.69222 | 2024-10-30 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b76753f9-c824-3757-8d80-28df58d6081c | -9.28016 | -48.71132 | 2024-10-30 04:46:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de4e3bdd-5d90-31c8-b357-c9afcebd429a | -9.05183 | -48.72113 | 2024-10-30 04:46:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 947e0a16-3cd0-3f2d-a0b8-57620b18258e | -9.89593 | -48.65292 | 2024-10-30 04:46:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de5d78c3-33a5-3963-aa29-cee54b2fa6d8 | -10.29208 | -48.89357 | 2024-10-30 04:46:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0502851-b405-311a-8e47-a5826166fb11 | -10.2885 | -48.89305 | 2024-10-30 04:46:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c6a61bf-4a85-34a4-b600-47620dc30d60 | -10.09381 | -48.46909 | 2024-10-30 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd6b7696-cf04-3fd8-80f3-308a5013306b | -10.61763 | -47.71058 | 2024-10-30 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d56e01ab-3afc-33df-ab5d-be0a11a2d7d2 | -10.50769 | -49.01954 | 2024-10-30 04:46:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f61bc1-85bb-3be0-b2ee-1a3f7c147e6d | -10.50532 | -49.01087 | 2024-10-30 04:46:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README77.md)
