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

## Dados Diários - Página 233

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c890633b-8dcc-3d32-897b-2791378b4f37 | -9.93626 | -43.55589 | 2026-10-09 11:21:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2f950b13-d23f-3f97-a710-2474e3820224 | -11.0566 | -44.03867 | 2026-10-09 11:21:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e37ee453-e6a0-3812-860d-ec5d3ee1fe8b | -18.32871 | -42.36812 | 2026-10-09 11:23:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 55434e84-9356-3576-85f4-2aea634dda27 | -19.55556 | -43.83976 | 2026-10-09 11:23:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 085e317e-df2f-3d59-9b73-716c5c63e5ef | -18.08288 | -42.2694 | 2026-10-09 11:23:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d0b0845b-0ccc-3b6e-bbe8-ae0a487bab40 | -19.55426 | -43.84914 | 2026-10-09 11:23:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4297a036-e792-337e-ba64-35fbc343fd57 | -19.46352 | -41.18568 | 2026-10-09 11:23:00 | TERRA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 55abe726-c869-3174-9ab4-4a7613f100b7 | -17.23603 | -47.71452 | 2026-10-09 11:23:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d730dc97-ef1a-39b5-b88d-eda053d9068b | -18.06466 | -44.59748 | 2026-10-09 11:23:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae4ed45f-62e3-396d-9508-64143131df13 | -17.5519 | -46.54642 | 2026-10-09 11:23:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 102d127c-a38f-3f1b-9a0f-3a89bdf3e616 | -21.28393 | -48.54328 | 2026-10-09 11:23:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 05f50f07-c9a9-3d0c-aeab-d6a6e4bcede2 | -17.43038 | -41.58691 | 2026-10-09 11:23:00 | TERRA_M-M | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 556df6a5-c8e6-3cd3-b8b6-3e82854a541d | -17.23399 | -47.72717 | 2026-10-09 11:23:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5aea36d8-8b9d-3b38-8faf-437c034a102f | -18.63809 | -41.33872 | 2026-10-09 11:23:00 | TERRA_M-M | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 009559d3-1f81-3d5f-82fc-0701e0d63916 | -17.09968 | -41.56615 | 2026-10-09 11:23:00 | TERRA_M-M | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2db63478-8a0f-34f9-a5e7-5e1b5187c7d0 | -17.9339 | -43.95662 | 2026-10-09 11:23:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 064e9010-7f8a-321d-9c2f-9434fdd65c57 | -18.72661 | -46.46765 | 2026-10-09 11:23:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da29f2df-d7a5-3ee0-beee-a914d0668adb | -17.45576 | -44.01264 | 2026-10-09 11:23:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 65ab9cf7-e24e-30fb-8ad3-b9809561a16f | -18.05236 | -44.55791 | 2026-10-09 11:23:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 23bb61c7-b843-35c5-bbfb-8e3e41be4d3a | -17.51403 | -43.66538 | 2026-10-09 11:23:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4f91337-10b4-3216-8acd-57161912dfce | -17.92045 | -39.74062 | 2026-10-09 11:23:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 854dd0fc-1d80-3df7-bfef-4df9ce109cfd | -18.13332 | -42.52098 | 2026-10-09 11:23:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| bf340c27-a862-340d-bd75-0b6bad213561 | -18.63661 | -41.35025 | 2026-10-09 11:23:00 | TERRA_M-M | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 10213667-958a-31d4-8cd4-f039353e0e62 | -18.62692 | -41.34868 | 2026-10-09 11:23:00 | TERRA_M-M | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 12c34f3e-67b1-3567-906d-fc5ea32e17a4 | -18.78961 | -46.47362 | 2026-10-09 11:23:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89e67c12-8b05-3db7-bbe2-e7ee176096cb | -17.29866 | -41.21954 | 2026-10-09 11:23:00 | TERRA_M-M | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 197b13af-be93-3e20-bca8-57fad61e724a | -18.13196 | -42.53094 | 2026-10-09 11:23:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 95fa5e37-4456-331a-bfb1-f16abb372b27 | -16.6398 | -47.20529 | 2026-10-09 11:23:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7ae03970-8ad8-3edc-84bd-283e6b9ce123 | -18.32734 | -42.37833 | 2026-10-09 11:23:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 751df69b-ac0b-31d7-9a10-bae24ead7401 | -18.7912 | -46.46335 | 2026-10-09 11:23:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2fcacb3-1701-3c1f-a8bf-66022f32868a | -12.0058 | -43.464 | 2026-10-09 11:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| d4618c2d-4120-3129-ba7d-96495cbf5033 | -11.9865 | -43.4671 | 2026-10-09 11:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 4b9fede8-c64b-3755-bb8d-40a8f1769a77 | -11.9861 | -43.4908 | 2026-10-09 11:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 72d8f455-ecc9-3ea3-a895-bc419a0f3205 | -10.4633 | -47.8545 | 2026-10-09 11:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b494b5f5-f1ee-35f6-9fae-5742e7a0bf03 | -12.0054 | -43.4878 | 2026-10-09 11:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| fd6432b9-789e-3244-b2b5-c885cd682e5a | -9.8986 | -50.49 | 2026-10-09 11:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 9cfaa3da-8f60-3c1b-83d5-503528db6104 | -11.5801 | -43.6492 | 2026-10-09 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 85393535-5498-309d-9b85-99a4f837e11b | -11.9865 | -43.4671 | 2026-10-09 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 459.9 |
| c7a03985-8260-3168-b4f5-f56c4df99ebd | -12.0054 | -43.4878 | 2026-10-09 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| ef23d292-41cd-30bd-856c-9c9de2243f17 | -17.2322 | -47.7273 | 2026-10-09 11:40:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e1a5c03d-0a2f-3b93-a5e7-59fe39e54dea | -10.4901 | -47.3201 | 2026-10-09 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b953ff65-de4d-3cfc-9dfd-60aeaae2ca7e | -11.5801 | -43.6492 | 2026-10-09 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 5b7a3b33-288b-3017-8cbc-62409821ea37 | -11.0562 | -44.0561 | 2026-10-09 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| d8d353ca-3dc2-337e-ba2d-31d4b1c92290 | -11.0558 | -44.0796 | 2026-10-09 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 62cdf4ec-7fb8-3a73-a3c7-34949536e61a | -11.8307 | -43.5866 | 2026-10-09 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 925e1fba-1b63-3e12-a8ce-c1f71e26784a | -11.9861 | -43.4908 | 2026-10-09 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 494.3 |
| cae48f8c-aae8-34cc-b0a2-4c9654c3b1ea | -12.0058 | -43.464 | 2026-10-09 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 437.8 |
| 2ce28b21-5209-38f6-95d9-67dcc164ea59 | -12.2348 | -57.0871 | 2026-10-09 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e7125eb1-708a-3f00-ab88-7bab34c4486b | -11.075 | -44.0768 | 2026-10-09 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 4dd01743-0779-3dc8-bc63-eb467e67837a | -11.0754 | -44.0534 | 2026-10-09 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 4728494a-8c02-3a56-82b3-b3125c61a10b | -12.2346 | -57.1071 | 2026-10-09 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 0ccafdfb-2dd8-308c-a588-9ecb9b592680 | -14.0048 | -48.7522 | 2026-10-09 11:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 213f5417-7afb-3218-a172-781b898bdac8 | -12.0063 | -43.4402 | 2026-10-09 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| effe5ae5-59f2-38de-8a29-020dc508aeae | -12.0063 | -43.4402 | 2026-10-09 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| f0b4455c-1839-3fa1-a1f3-a966876635cf | -11.0562 | -44.0561 | 2026-10-09 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| d29ca44e-47c5-3b6e-95ab-a28b3b7a950c | -11.9865 | -43.4671 | 2026-10-09 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1210.4 |
| ee4b8150-b0c3-3f5e-abe8-a0389d5a6714 | -11.8307 | -43.5866 | 2026-10-09 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| b70ec0f2-9d09-3f23-858f-2048caaccf5e | -10.7479 | -46.5959 | 2026-10-09 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| df47f3f4-20b4-3999-a654-7732dffc6dc0 | -10.7475 | -46.6184 | 2026-10-09 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 06145b08-05c6-3593-a1d7-bcd4f7c311f1 | -11.1242 | -45.6865 | 2026-10-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e8849b0b-e55a-3b3e-a564-820f28d2d6e6 | -8.5377 | -49.5699 | 2026-10-09 11:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 270dc940-af0c-3244-aba3-e806dde798e5 | -11.2475 | -46.3058 | 2026-10-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c7e6545a-5bef-3e1e-9634-14bad45cd2fc | -13.1636 | -54.3591 | 2026-10-09 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d85d172b-0c30-3cf8-99b7-284cf976fd80 | -11.1051 | -45.689 | 2026-10-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 026132d6-91e8-3d18-bf34-3c9ffb1f52ec | -14.0048 | -48.7522 | 2026-10-09 11:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d5d6b34d-5d57-3cea-a421-fc6f65eb34cb | -12.0054 | -43.4878 | 2026-10-09 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 480.3 |
| 09fd615f-718b-3054-aa6f-6630d4b7ec01 | -9.8818 | -47.4788 | 2026-10-09 11:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 510e1ab8-ab6a-36c2-abbe-d5e3276391f6 | -12.2348 | -57.0871 | 2026-10-09 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 3b6278d6-7fa7-36a7-9b38-f577386335d1 | -10.4901 | -47.3201 | 2026-10-09 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e2ab7d08-ac2a-31d7-ba2c-82d87fb5d17f | -10.917 | -45.5317 | 2026-10-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 18f1e17d-c408-393e-a475-e2e10640292a | -11.4173 | -47.5833 | 2026-10-09 11:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 82899073-7209-3f3f-afc2-f3208ae1d1e5 | -13.1827 | -54.3571 | 2026-10-09 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f9126ab3-4912-3ecc-bd8e-905c8c714bcc | -12.2346 | -57.1071 | 2026-10-09 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| bb9d0464-e28b-3964-8150-e33898e2b41d | -12.0058 | -43.464 | 2026-10-09 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 686.3 |
| 8f4dd021-d5a5-3916-8c54-47e3396bb706 | -11.1054 | -45.6662 | 2026-10-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0c258572-6281-318e-9d75-78c9ba22ca5d | -17.2322 | -47.7273 | 2026-10-09 11:50:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 42836554-5623-332b-b97f-fa9a737b789d | -11.9861 | -43.4908 | 2026-10-09 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1159.2 |
| f768a22f-e45f-3b93-a28e-5dd416edaad6 | -11.8307 | -43.5866 | 2026-10-09 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 9f3200db-472d-3931-add3-976d2462c9f4 | -13.1827 | -54.3571 | 2026-10-09 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 0d93fcbb-5822-34d9-8346-169c67126e49 | -11.1051 | -45.689 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| d4faa923-ba39-31b4-9cb1-18bb571801ea | -11.2259 | -45.3064 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4a093515-2604-3229-94a8-99fe6d3719be | -11.4131 | -46.6671 | 2026-10-09 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 355.4 |
| 6ec946c7-b746-3d20-ab24-d42e03c694a0 | -8.9775 | -45.9023 | 2026-10-09 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 8490913c-953c-3027-b591-cf8d245308d3 | -13.1824 | -54.3778 | 2026-10-09 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6e2af7b0-f482-396d-b386-257dcef8e1a0 | -11.5801 | -43.6492 | 2026-10-09 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 7651909d-7092-3101-aa35-dd8dcf8da350 | -13.1636 | -54.3591 | 2026-10-09 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 9187d8da-6925-35cd-8c80-e7cc745376ac | -11.5993 | -43.6462 | 2026-10-09 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7a5a27cb-e357-31b6-a372-921d006cf349 | -12.2348 | -57.0871 | 2026-10-09 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d0eaba1f-41c5-37cf-b716-0c89ab067b88 | -8.9964 | -45.9002 | 2026-10-09 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 80a90b5d-540a-3866-8436-f6219ec65924 | -11.1242 | -45.6865 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 3c43a4cc-b041-3461-9ed5-e0244ebad0ff | -12.2346 | -57.1071 | 2026-10-09 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a1ea833a-0d75-3f1c-ae22-677195533dc2 | -10.8983 | -45.5114 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| eb6911f7-2c1f-349c-b9dc-23e80bd827ba | -10.917 | -45.5317 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 0f3eb605-8398-31f6-aa10-a3908ef5fff1 | -11.0562 | -44.0561 | 2026-10-09 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| dcf2760b-99d5-3455-9e56-40bdd5487280 | -13.1639 | -54.3385 | 2026-10-09 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a5489f70-3c93-396b-9b13-68ba61ee262c | -11.2475 | -46.3058 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 8c1dad01-b851-316a-a86c-75cfc2e7bf53 | -10.3161 | -46.2668 | 2026-10-09 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 35019284-6c85-329e-bc7c-a76245716208 | -11.5797 | -43.6728 | 2026-10-09 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 86450feb-a594-346b-af66-6cd35df1d9b0 | -11.1054 | -45.6662 | 2026-10-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 8a6c36fc-6842-3129-9a62-f6faea39bce1 | -11.4128 | -46.6897 | 2026-10-09 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |


[Clique aqui para ver as próximas entradas](README234.md)
