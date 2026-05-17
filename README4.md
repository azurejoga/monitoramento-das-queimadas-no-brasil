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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcfb0d66-0e7f-31f1-87c3-8297ba0beb25 | -11.54357 | -48.27539 | 2026-05-17 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41493460-1924-3f03-9628-b407091e6324 | -11.44643 | -54.09298 | 2026-05-17 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f91bb850-bf12-329d-bfee-2fb3539a1125 | -11.04566 | -49.59944 | 2026-05-17 04:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d25732d-8ae6-3b21-a51c-7db81a594a6b | -11.459 | -55.11714 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff6cfda7-8076-3c95-873e-311750ba9a88 | -11.54423 | -48.27087 | 2026-05-17 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d320ad6-52b3-35f7-b053-ffc1d8dcfb1a | -12.26382 | -43.50803 | 2026-05-17 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| adf1c3af-eb5b-30fc-ae84-60d584f10e23 | -11.87568 | -48.99514 | 2026-05-17 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b41a20f5-6f1a-3fa3-910b-69184aa250db | -11.5455 | -48.27305 | 2026-05-17 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51221f2a-d961-3055-93d7-cd38f0e60374 | -11.46615 | -55.11835 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c987581-e31a-332f-94d0-f3e25c8b867e | -10.91486 | -54.11985 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13899537-510f-3160-940f-2dedd305d5f4 | -11.88392 | -43.81038 | 2026-05-17 04:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 07a56e8d-46c3-342e-91ef-2c5d6454cdfd | -11.61008 | -47.10035 | 2026-05-17 04:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 957bac34-ec06-3456-8b6c-d91d5d627c6d | -12.26461 | -43.50176 | 2026-05-17 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 63d1ea27-4644-3b5d-82f3-5d5c2155d0ac | -11.08309 | -48.25229 | 2026-05-17 04:49:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b06f135d-bf34-3dbe-8f72-2124f0105cb8 | -16.05155 | -47.22522 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92c8173a-8c6d-34ce-bed1-85a89a508fd0 | -12.73083 | -54.19246 | 2026-05-17 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d3de7d-0a3d-3ce9-b862-b0253c4b79ac | -17.56431 | -44.94529 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b07b3355-7e97-3011-a5b5-03927882786e | -12.72681 | -54.19564 | 2026-05-17 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d9e284-dcef-360c-9f66-9a8abad3fef0 | -12.99128 | -54.68123 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4728da66-3898-3eff-83c1-1055c35306d8 | -17.57934 | -44.94412 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 694396d3-03f5-3ca9-9160-e3baf9d69d38 | -12.56106 | -54.75451 | 2026-05-17 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb63bf87-9428-36e7-8de8-373aab285827 | -17.56929 | -44.94277 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4724841d-54be-3aef-8a34-9e8e1e62a1ee | -17.56466 | -44.94223 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0322b081-8e10-3818-b7d0-0cc919c3a056 | -16.04733 | -47.2246 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0edeaca2-7908-3936-bf8c-cc8df28e62f6 | -12.49409 | -57.74835 | 2026-05-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea01ddea-c2c5-3dba-8ca2-032cb292ea4b | -12.98783 | -54.68065 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702460a6-c869-3170-a866-53c24fe4a313 | -16.04633 | -47.23249 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c2b4131-a46d-3039-823f-1ad8a8dd3762 | -17.56896 | -44.94583 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e330c1ba-7937-3bee-99b3-bcc21a8a44d8 | -17.56361 | -44.94818 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23ae61d9-33cf-366b-9a65-45644e288542 | -17.56968 | -44.94291 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f55b0e04-6296-3b5f-a812-a65437d16669 | -17.56426 | -44.94207 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27d14922-8d8c-3b10-90a0-953cdc247cf0 | -14.16249 | -52.88497 | 2026-05-17 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48b462c-8e3d-3275-8a93-cf73f3186ea8 | -17.57901 | -44.94717 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90838aa3-02d4-3e77-867b-28f7c895b1d1 | -12.49 | -57.74759 | 2026-05-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8c9f276-50a1-3d25-82fd-96bbc4207106 | -15.65037 | -56.07469 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 157dfeab-e192-3522-9e62-583cc210f058 | -17.56863 | -44.94886 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1332adee-ccbf-3597-bc28-1daa57ad34f3 | -14.15974 | -52.88089 | 2026-05-17 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2799cb9-8a0a-300c-b3bb-e9f5c373a57a | -14.15478 | -52.89096 | 2026-05-17 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 557195c3-998e-3871-9923-dc0dd96184e4 | -12.57971 | -54.74969 | 2026-05-17 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc28e33a-fb58-3ef4-a0ca-aae2a124233f | -14.16194 | -52.88851 | 2026-05-17 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 295ec85b-366d-3351-b242-fddd95184712 | -16.05105 | -47.22915 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 45d80913-313d-32bd-9298-46a17cea9ad3 | -17.56396 | -44.94832 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e978461b-262f-3011-87e6-cd45ded9d669 | -14.15919 | -52.88443 | 2026-05-17 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 592706f0-0192-3cd5-b41f-28a5606581ff | -17.56898 | -44.94899 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b8c5080-8ded-3966-9eec-95d380cb4577 | -17.56393 | -44.94515 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8356d17-dded-3dab-b688-00b18ddc7f7b | -16.04683 | -47.22854 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7151e252-1f87-393b-8d38-98fa797055c6 | -13.18125 | -52.70177 | 2026-05-17 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd41f26a-5786-3e08-9677-0ae761e3bbf2 | -17.56933 | -44.94597 | 2026-05-17 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e66b42e1-2aa1-3eb8-af87-47b091e8fb39 | -17.3557 | -47.81226 | 2026-05-17 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af50956-dade-320a-a2ec-52efddf21763 | -14.61924 | -52.35249 | 2026-05-17 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25db24bc-6c32-3068-ae83-7814da1b2e4a | -16.05055 | -47.23312 | 2026-05-17 04:49:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6990061b-20ce-3205-8da8-e4753e6f65d3 | -21.07956 | -55.74491 | 2026-05-17 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba78b2c4-6c59-3160-ab15-224fae245553 | -19.71636 | -53.2401 | 2026-05-17 04:51:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dbe9bfa-18bd-3455-8497-d3d01edbfd47 | -28.82155 | -49.2546 | 2026-05-17 04:53:00 | NOAA-21 | BALNEÁRIO RINCÃO | SANTA CATARINA | Brasil | 4220000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 50301a07-cc38-3a45-8db9-dab3cb64ed0c | -12.4477 | -49.58686 | 2026-05-17 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d4f3b43-6e7f-3f62-a78e-358d02ba292f | -9.22748 | -46.65354 | 2026-05-17 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 198daf52-0575-3b49-893e-58cec07d9ba0 | -11.6109 | -47.09542 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff219be3-44f7-3053-9a4f-d32738ea058e | -9.46834 | -46.11378 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68c0cfd5-112d-3b3f-b386-6f70bea59296 | -11.43534 | -54.09272 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd72ea5f-1fe8-3705-a789-6418abcfbac3 | -9.45533 | -46.11234 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c503fa45-8eb9-32cb-b15b-f7133fd8c0e6 | -12.45309 | -49.58765 | 2026-05-17 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb38dece-2a8f-3341-8a53-d1e4eae09237 | -10.91703 | -54.12139 | 2026-05-17 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe0f4c0-f17b-3fd4-b6b5-e5c8d6c5b656 | -11.61655 | -47.10134 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 064ec4cc-491f-3960-9978-7af1acc3ee53 | -11.61028 | -47.10053 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc497d1c-9f33-3488-9d1e-204caa92f083 | -11.43517 | -54.08934 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03e0688f-852f-3812-9af0-c4763b9c6f70 | -10.40859 | -44.93151 | 2026-05-17 05:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95b2df4a-fb71-3365-a1a3-6f097e50d0fc | -10.91313 | -54.12082 | 2026-05-17 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e062153d-a0f4-316e-8bd6-c0ab06d2580d | -11.02789 | -48.92894 | 2026-05-17 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5ccaa4c-dfa2-3586-81a7-c677e5ceddb2 | -11.44321 | -54.09388 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8441200f-18bc-3d13-92d1-e70bd1727697 | -11.44304 | -54.09053 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0a92966-4e16-3d10-82c5-4e7ca5a864b9 | -11.02743 | -48.93257 | 2026-05-17 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2e1ebe6-91e9-37c4-a953-199bc22d11c2 | -11.43911 | -54.08995 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fb2e7d7-2057-3873-918d-36b7e340b351 | -9.27914 | -56.24387 | 2026-05-17 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b58e1927-0d99-3ed2-97f5-e897eb4cc7fc | -9.74197 | -63.33674 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d93c5401-deb5-322b-a19c-bd875d527460 | -11.44698 | -54.09111 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb737fe4-d75d-36a1-9717-94ece85c395b | -11.43927 | -54.0933 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b76abb2-5290-385c-b717-dea05e67d14f | -11.44234 | -54.09558 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 898426a7-de2d-35dc-b3f9-d6f2a6c4acc2 | -9.23374 | -46.65434 | 2026-05-17 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10cadcbb-5ee9-3341-b55e-bfe21f9d7e71 | -11.61376 | -47.0963 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdf0fbb1-274b-3c1c-9801-fe22e9f3da0c | -8.85955 | -50.21264 | 2026-05-17 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a84a48f-f99d-3d0c-a3cd-80e4cf6f2269 | -11.61316 | -47.10146 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b6f1aea-6ecc-310a-89d7-541a3be04d09 | -11.60689 | -47.1006 | 2026-05-17 05:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 135fee02-7fec-3032-bf4a-7eae3263cb71 | -9.73795 | -63.33601 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f81f1f1b-a443-3083-abad-fda38bbcb613 | -11.44395 | -54.08884 | 2026-05-17 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa906ed4-d99a-3e6c-9001-e8d88ba2f1a6 | -8.72578 | -48.32661 | 2026-05-17 05:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b57f597e-b9c7-33b6-b819-4dcb8cd33f05 | -9.44883 | -46.11162 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51a37026-4a13-30ed-a16b-d1e9e29cbf35 | -8.86048 | -50.21353 | 2026-05-17 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71e03a41-dc57-3ecc-b8e8-7b9bc9634e12 | -10.4078 | -44.93838 | 2026-05-17 05:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79abcb44-903f-3e1e-918b-cf0d5a7dd207 | -10.41084 | -44.93729 | 2026-05-17 05:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f0a3a52-e9e7-3a8d-acb4-4ea8342dbbf8 | -9.46766 | -46.11923 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58dcad85-4ef7-3d7d-b2c8-3ae9070ae3af | -9.45599 | -46.10709 | 2026-05-17 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc65da44-9f21-31d8-8355-24e298f79a75 | -12.51227 | -57.20627 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ede6d251-3f21-3b2f-900a-87d373939424 | -12.50655 | -57.19768 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 407dbb47-6276-3977-af74-6b834381ab94 | -12.49745 | -57.21159 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 333b147d-358c-38a0-9b43-a79839751bb4 | -12.5134 | -57.19875 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ab8101-9d25-3de0-95bb-abb7dcbb2ce2 | -12.72977 | -54.19462 | 2026-05-17 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5522f38a-0772-3195-a43e-b61c9572793a | -12.502 | -57.20465 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe884f8-82ac-34c3-8084-ae85c6be2546 | -12.37561 | -54.45397 | 2026-05-17 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e063a70-dffe-3dd4-b0f4-49cac0b168ba | -12.50088 | -57.21214 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3d01198-fff6-34b3-9a76-7f292a4f0dcc | -12.48885 | -57.74711 | 2026-05-17 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
