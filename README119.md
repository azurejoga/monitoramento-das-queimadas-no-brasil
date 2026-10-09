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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 892a142e-2738-346f-a593-8bfc8d5d5851 | -14.35046 | -55.02745 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b11cbe33-6f6f-364b-84cb-c99dd6de26b0 | -14.73659 | -48.22168 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18d8dfb6-6de7-3179-b136-576431dc82fc | -16.58605 | -46.75928 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1cacbce-ac1c-3e50-bc72-5526e88b98fc | -19.08842 | -43.99266 | 2026-10-09 04:29:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d61d461-9d1a-3148-a717-60b063c0de38 | -17.97234 | -44.34924 | 2026-10-09 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9154ce0c-2404-3368-9ab1-43dc6ea988fc | -18.66832 | -44.25611 | 2026-10-09 04:29:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b8a2749-9c65-383c-b4a2-7bacb3fdebe0 | -16.99496 | -41.17645 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72df1b05-4cac-321b-accc-5748c8913b3f | -18.89783 | -54.72532 | 2026-10-09 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d80ef06d-a356-3c9d-a619-bed1a6af5709 | -14.91921 | -48.12051 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7671dad7-ae1e-3ca9-9726-68556aabae0a | -15.98428 | -49.54655 | 2026-10-09 04:29:00 | NOAA-21 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be35288f-0007-3519-ad21-81a0a50ce11b | -16.02409 | -45.13434 | 2026-10-09 04:29:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b91a32-cf95-3800-b4e0-b6fbeadb4a43 | -14.972 | -50.38485 | 2026-10-09 04:29:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d16878c-0347-3704-b1e1-68ddfec4909a | -15.10668 | -43.64266 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 480dca6b-a541-38b6-ba8d-e2a5fa3edb45 | -18.63894 | -41.34347 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 98082195-d40c-39a3-97fb-c24e50517368 | -14.52054 | -49.33262 | 2026-10-09 04:29:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18977aaa-c522-39e5-ac08-ff06e341a9f4 | -15.25568 | -42.36335 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| bbefab7f-cad3-3ff7-b988-5ff963aac065 | -15.99944 | -53.68869 | 2026-10-09 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb47c2f7-6ee1-39a6-8ab7-535ac53bbe0e | -16.12855 | -43.75198 | 2026-10-09 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e9eabdd-8c61-3766-9f25-9b43a6193008 | -19.42251 | -44.46967 | 2026-10-09 04:29:00 | NOAA-21 | INHAÚMA | MINAS GERAIS | Brasil | 3131000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 769a50ee-2d05-37ac-9847-c99ba0846fdd | -14.52652 | -48.0417 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe49757e-fa86-37e7-b210-73736d341d1a | -14.92526 | -48.12512 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65fad27f-9168-3970-b91d-83d226b802e8 | -15.21287 | -47.89097 | 2026-10-09 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0fe1b78-dd19-3890-96aa-7cc74599ef07 | -18.05917 | -44.59819 | 2026-10-09 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d88216a8-43b8-3291-b395-da078974d387 | -15.56459 | -44.51765 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b208fbab-2a05-3eb6-a06b-3a95a59902c3 | -15.78499 | -44.68275 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9951382d-0389-3003-a2c9-7ee070bfa740 | -17.36819 | -48.17777 | 2026-10-09 04:29:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bff5de7-97ee-30f5-ada2-43df700a22d4 | -15.11473 | -48.524 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a95903ee-0eff-300e-acd4-1b3d51cec171 | -18.29103 | -49.51072 | 2026-10-09 04:29:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3280f6f-1860-37e2-9e85-4209b8e93912 | -18.78747 | -46.4663 | 2026-10-09 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 402d14b6-d603-3375-893a-cd7b4184b71b | -16.59004 | -46.75598 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6013ad75-0efc-3bc6-b839-aa0b5f88061e | -15.34409 | -42.77597 | 2026-10-09 04:29:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a444c60-39f2-3a36-9115-2768a15f45e0 | -17.09955 | -41.35182 | 2026-10-09 04:29:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c37b56f-1464-340b-a36c-9e30c91dac40 | -15.56146 | -44.51248 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f727e5f-6f78-3236-b1ad-c91b8bffa2ac | -18.08502 | -42.27145 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9fd8ea27-e818-3469-abf0-522597ad71c8 | -16.99487 | -41.17081 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ced8d19-466e-33cb-a48d-34222279f9e9 | -14.93406 | -48.09012 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1028ec36-4c1e-3aea-a7d4-4fd310623da5 | -17.01506 | -51.89586 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7271ae02-5097-3e2c-af32-7a12a9a6a113 | -15.11804 | -48.52454 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b3ace3f-d16e-38af-9618-7bbd5dbc05ea | -16.30636 | -49.4493 | 2026-10-09 04:29:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6404e54e-d508-38b3-8c14-0d5c08c5cb31 | -14.94342 | -48.09526 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b3f1d3-c370-3656-a6f6-ed7dc23fb9a8 | -16.63989 | -47.20771 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dbb804f-63aa-381c-9e36-42d328373a58 | -15.42821 | -43.24562 | 2026-10-09 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 2fc3201c-8968-344e-abb9-a4ec345c55de | -15.51844 | -50.39893 | 2026-10-09 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 831f0e03-0bd2-3da6-8a0c-4fbb0f8f3c63 | -18.32836 | -42.375 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 8db57759-e666-3203-8ad4-eb643de480cb | -14.73384 | -48.21759 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d694c500-7c79-3e4d-abd2-f85627823fa8 | -15.25322 | -42.36943 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 65a65bad-8f37-3fe4-9d58-e9aed04e2dfa | -16.96815 | -41.23282 | 2026-10-09 04:29:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a49c287-027f-37e9-b09d-c292afde5d83 | -15.95681 | -41.08816 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 96eac911-537f-34bf-9b5b-1dd1cd0456a6 | -14.55411 | -50.03505 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0822bd58-c730-3d93-a3b5-24091f0986e5 | -13.79029 | -52.79734 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc348ca8-187e-3a80-b543-d39a1bf785d4 | -14.94617 | -48.09933 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59bc70f2-0e10-3260-81fb-bf8fd675d167 | -14.32705 | -52.77938 | 2026-10-09 04:29:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 760acffc-0e78-383d-b984-fb35d0ce4247 | -15.38857 | -41.89315 | 2026-10-09 04:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f1a1275c-2ae3-359a-ba64-7ec6ef3fb1f4 | -20.32311 | -42.01752 | 2026-10-09 04:29:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f407e0e-a638-322c-9909-7611a76c76a6 | -14.96701 | -47.54214 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 719220d6-a2a4-3403-a30f-4bfb3d5883f9 | -18.32779 | -42.37974 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 641af8ef-82f7-3ee6-9cfe-c85ab5543cad | -15.21232 | -47.89454 | 2026-10-09 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64c3526d-566b-3ad3-9ef2-aecd5970931d | -18.05853 | -44.60299 | 2026-10-09 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 904be92e-6f2c-38f3-9329-e163387dae9a | -19.0889 | -43.98888 | 2026-10-09 04:29:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c8c4989-3c48-3887-87fa-08f4b462b374 | -14.92745 | -48.08909 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40fde36d-9754-3988-a839-408a20339fa0 | -19.9958 | -49.08826 | 2026-10-09 04:29:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71950b3d-1468-3507-8cfb-42aae2aab4f0 | -15.71526 | -50.01099 | 2026-10-09 04:29:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a6c6af2-895a-30a6-9612-9f1e0277fde3 | -15.25375 | -42.36525 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2e079a83-3fbf-3d0e-96f7-f3cb479c8d99 | -14.92581 | -48.12156 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1762297a-fe6b-3d3e-a89f-cb37f539c5e9 | -14.56839 | -48.01557 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c44d21cb-2132-3747-97b3-fb2a492180f8 | -17.77475 | -49.24525 | 2026-10-09 04:29:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7c2aa15-e8ba-3266-b8ff-ba53b75d8c72 | -18.47787 | -42.2536 | 2026-10-09 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 79f250ad-2b33-3869-b9e7-d2f88f8ff01d | -15.4287 | -43.24191 | 2026-10-09 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 27b2f48a-b571-3cce-9d31-d291dde5f37d | -15.44645 | -45.44239 | 2026-10-09 04:29:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4fec68f-9ed4-326a-9efc-cd0b50b226e7 | -18.05403 | -44.60715 | 2026-10-09 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2c15572-8674-3ace-a55d-246863fa2b30 | -16.58548 | -46.76314 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7c23eaf-6686-36d6-b005-f85c94826fb5 | -17.15611 | -46.12288 | 2026-10-09 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8d97bcb-4fc2-3c73-b694-9553323d77a9 | -16.57385 | -51.6245 | 2026-10-09 04:29:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2651d2c4-2890-3262-ae2c-0a4425ce9f9c | -14.92801 | -48.10738 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b4f02f2-7647-3673-a7a5-2033bbba3ec5 | -15.00209 | -44.05875 | 2026-10-09 04:29:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 636128cd-b3de-3db5-baf9-0000665bd237 | -15.11201 | -43.6328 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3dfef1f1-1ab3-3cf1-9659-d40f3f72e1df | -15.51906 | -50.39519 | 2026-10-09 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adbd8227-2655-31c6-9d72-327ac4ac0073 | -15.01445 | -46.25193 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b96d0d9-c92c-3f36-b209-0c6249918dcc | -15.9708 | -40.69585 | 2026-10-09 04:29:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce61b347-13ec-35e4-a1f0-850c52835c72 | -15.49775 | -44.41294 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 668a75a1-c887-332d-8a9f-9d0ad455404b | -15.78873 | -44.68332 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97a4a8a2-9cd4-3923-a459-82dd4b66232e | -13.78641 | -52.79665 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc87b027-4bc1-3432-9044-c5da7cf04976 | -14.52386 | -49.33319 | 2026-10-09 04:29:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c0cf16f-07d0-3358-b64e-60d8aa257967 | -14.97643 | -47.54733 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0842f966-a9c1-3d24-a73f-f693cecac58d | -14.99825 | -44.05819 | 2026-10-09 04:29:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f0b27aa8-a0cc-3231-8006-ee7a3e15beac | -16.71144 | -41.88518 | 2026-10-09 04:29:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 924dc5c2-78eb-3f9f-83e4-fdd5611e4d11 | -15.10343 | -43.63687 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1b6b6416-f3c2-31ae-bb15-a6dd20827c0e | -16.12519 | -43.74685 | 2026-10-09 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 34260bde-ec50-3189-9ea6-ba6342317af1 | -16.12122 | -43.74626 | 2026-10-09 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 752db349-cbf9-388c-ba1b-92c7a08ffc23 | -15.95892 | -41.08447 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2c979a12-ec27-3f14-bb89-d5543223aed0 | -15.69695 | -49.68382 | 2026-10-09 04:29:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf97878d-aeaa-3c05-b899-dd4ecf9f67e6 | -15.34388 | -50.58175 | 2026-10-09 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c4faecb-6e4a-3375-9a5f-bce7e8fa020f | -18.33343 | -42.37067 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 1f1ad781-2a12-34b8-89d7-14d0d68ee064 | -18.78687 | -46.47054 | 2026-10-09 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9b8a9888-e58f-3a7d-9cb4-015c992fa22f | -18.21123 | -50.93679 | 2026-10-09 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af88c5c-3cb6-350d-ab51-ea9d1e431f18 | -16.12457 | -43.75148 | 2026-10-09 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3528c3a5-cb99-31b0-9761-4a87a5e48aaa | -17.17814 | -51.74961 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccfea449-5695-3a56-89bc-6a08f41a42cc | -16.99426 | -41.17589 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d832cdae-809f-3324-8b11-7b0f98618703 | -17.25493 | -39.46912 | 2026-10-09 04:29:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c1f44222-352c-305d-8358-83e2cb89a8a8 | -15.56523 | -44.51302 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README120.md)
