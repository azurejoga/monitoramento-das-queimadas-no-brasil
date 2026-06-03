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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99bf776d-263e-3f44-ab17-ef82db85aed5 | -18.72377 | -56.57396 | 2026-06-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a57e9911-82ac-3ec9-8b00-32b0c3432756 | -17.93963 | -52.21884 | 2026-06-03 04:29:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f79941a-0e46-3530-b09a-1e951a059424 | -18.37702 | -55.72258 | 2026-06-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| feab706e-f860-31b8-9e6a-59bc44d860f3 | -16.14506 | -58.49645 | 2026-06-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5e09fef2-5d90-3ebf-854d-7ba40542aa3d | -16.14582 | -58.49281 | 2026-06-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7c288327-08a3-3dbe-97c5-cd43c9aebde8 | -18.61951 | -49.19014 | 2026-06-03 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ad6f2570-3d2a-358f-8cf8-8b8c62114031 | -16.9071 | -51.85699 | 2026-06-03 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cf1905d-09b1-3576-9fb7-ec8678ee3e19 | -17.52441 | -49.22922 | 2026-06-03 04:29:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1cd0c12a-99ab-3b12-a7c1-fbea0c28ad7a | -20.88539 | -48.98488 | 2026-06-03 04:29:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1513f38-bfa8-38f6-a6e8-d457d0ea7db2 | -17.4448 | -42.62685 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3c60bd60-f828-3fba-ad49-7334d2a23256 | -21.45926 | -41.11546 | 2026-06-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a8dfc1e6-31b9-3e0e-88ac-ff74b87bac43 | -16.58259 | -45.88252 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62e005a4-7e72-3de7-bd25-c351d7b5fab1 | -16.81361 | -49.22584 | 2026-06-03 04:29:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10ed9cd4-0bb8-320f-a186-a851f8d850d9 | -16.58666 | -45.87902 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5d1b14a5-130f-3d31-8155-37f5368baaa8 | -18.71916 | -56.57297 | 2026-06-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ae2651aa-cb7b-3ce4-a621-992286784f2e | -19.72149 | -40.15646 | 2026-06-03 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69016f5f-1587-3800-8078-d899b7c90122 | -16.57966 | -45.87792 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ea6d09f-df0a-3a57-aaf6-d44f809e86cb | -16.14034 | -58.49165 | 2026-06-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5ce666df-b08d-39bb-a7e2-d9f1655d0e2c | -17.4443 | -42.62553 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 86622d4e-ce5b-36fb-8b29-cd97e8a61c8f | -16.58609 | -45.88306 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c48d4a76-bb73-3fe5-9948-b72af274f4e4 | -19.16901 | -55.18834 | 2026-06-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9958a68d-a591-3e82-aa0f-5916c2394697 | -16.78382 | -49.30607 | 2026-06-03 04:29:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c6bbca8d-8e1d-3cc2-a594-08a11d5c6410 | -17.44373 | -42.63514 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39f4b9bc-a254-3443-906c-a08cbc4909c8 | -17.4433 | -42.63384 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 671fcec0-1d6e-341c-aa89-d1a6f2714419 | -17.4438 | -42.62969 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a7368137-3071-383e-aa3f-54b03265952f | -16.91143 | -51.85332 | 2026-06-03 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db81d771-7ccc-341f-8714-30a087347ba4 | -21.45819 | -41.11578 | 2026-06-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6062280b-7462-376d-9014-6cfb34672ce9 | -16.13958 | -58.49529 | 2026-06-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1eab9e19-af1b-3e87-b721-20a5f489f2f5 | -20.875 | -47.64761 | 2026-06-03 04:29:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89fbdd9c-53bf-3193-aac6-d4278434d02f | -20.55033 | -47.20525 | 2026-06-03 04:29:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e11e3456-fe3e-3243-8f07-f84350665604 | -20.15333 | -47.53373 | 2026-06-03 04:29:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ffb48960-4fe2-34bf-bf63-ec6ff2388916 | -14.1888 | -52.87974 | 2026-06-03 04:29:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b05253f3-6ca1-3e06-ae40-64144ff26d8d | -19.16977 | -55.18424 | 2026-06-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 29cf5539-8122-331a-966a-7782a334200d | -18.71815 | -56.57802 | 2026-06-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 90deaf89-faf1-3d19-9311-7befb0572d56 | -20.8887 | -48.98545 | 2026-06-03 04:29:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff62dfdf-9561-315a-b92a-b20edaba1803 | -21.29364 | -56.10436 | 2026-06-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3dd0f29-bd68-3cef-9994-342a82ca54b2 | -22.96658 | -52.69435 | 2026-06-03 04:32:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0365e0fa-e25c-35b0-a075-3152f26e9171 | -21.8158 | -49.1239 | 2026-06-03 04:32:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 04f49d77-3b36-347b-a700-ef87130e1d03 | -21.70202 | -48.4108 | 2026-06-03 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ded005e-60dd-3adf-8747-6772936c1647 | -21.70145 | -48.41462 | 2026-06-03 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 250af6a3-8121-39ce-b9df-05de7fa5796a | -22.96239 | -52.69778 | 2026-06-03 04:32:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1776b867-3f98-39fa-957d-6bd6a654b9a3 | -21.80973 | -49.11903 | 2026-06-03 04:32:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a15c3ce1-f890-3d30-81ef-2cdb474cb3b0 | -23.79032 | -49.2952 | 2026-06-03 04:32:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f84cdf6b-bc62-3d70-a3a6-b49b7d6ebd16 | -21.20776 | -49.21053 | 2026-06-03 04:32:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7ff678f4-6904-349f-8060-0d8ff633654c | -26.26572 | -49.17296 | 2026-06-03 04:32:00 | NOAA-21 | JARAGUÁ DO SUL | SANTA CATARINA | Brasil | 4208906 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c3bf714-cc86-330a-8eb0-b5174befeb89 | -25.26925 | -50.65244 | 2026-06-03 04:32:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21175976-4418-3ed2-b4f3-eddd01f50c81 | -21.29187 | -56.10376 | 2026-06-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccfd7d60-b266-3c7a-b94c-ad32489f5800 | -21.11779 | -48.63925 | 2026-06-03 04:32:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 80b5ba14-8da9-3b86-af77-b4ee6c455fea | -21.81637 | -49.12018 | 2026-06-03 04:32:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b3a9833a-2548-39e9-8aa4-7250f3a631c3 | -21.20389 | -49.21364 | 2026-06-03 04:32:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f139d80f-9a1e-35cd-a352-e4fb0aaadb05 | -21.0039 | -48.89909 | 2026-06-03 04:32:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a28731b3-7274-3a06-b52f-78d530d71647 | -23.64111 | -51.00236 | 2026-06-03 04:32:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e2acc2c0-2acd-3219-b8d7-3ef9df645a4d | -27.37718 | -51.46526 | 2026-06-03 04:32:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe74fd23-fba5-3de9-a80b-8f70178bed2e | -22.78917 | -49.33714 | 2026-06-03 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72492242-b856-3f4a-ad00-4fcce246674b | -21.00002 | -48.90224 | 2026-06-03 04:32:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 21c70380-7ce4-3469-81bc-e0ead34c47cf | -22.21208 | -51.34629 | 2026-06-03 04:32:00 | NOAA-21 | REGENTE FEIJÓ | SÃO PAULO | Brasil | 3542404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 802316f9-f902-3b8c-a64c-968449616a75 | -22.96311 | -52.69362 | 2026-06-03 04:32:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 439d73db-f7ba-3b7e-941a-9bc737d83520 | -21.81248 | -49.12333 | 2026-06-03 04:32:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 314bbbfa-bb9e-371d-863b-df54f3f9000e | -21.81305 | -49.11961 | 2026-06-03 04:32:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c4bac893-c659-3006-aeef-1be8fe0b49d0 | -5.30247 | -47.24143 | 2026-06-03 04:59:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ee1f4b-789e-343e-b42b-ce5f71682488 | -5.43359 | -47.25584 | 2026-06-03 04:59:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67bcb6bc-5fea-30eb-9934-2070898f861d | -5.84438 | -43.49099 | 2026-06-03 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dec0a98-a836-3b17-9960-c86e5ae384f0 | -5.92441 | -43.48152 | 2026-06-03 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aa5e474-8e23-3cf5-93da-0d2a65ec712f | -5.72412 | -45.02971 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a949cfcb-865d-3184-a107-8bd7ed62b0d2 | -5.72819 | -45.03566 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5305dbab-005c-3da5-ba6a-4d1c77da5646 | -5.72713 | -45.03268 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e7113386-eff1-3cc4-9c31-95b6ba717d58 | -6.30571 | -43.64302 | 2026-06-03 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79e0cd19-8b7e-366b-a327-d0400742aeab | -5.84009 | -43.49322 | 2026-06-03 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de71a82-6e4c-3584-99c0-f233f6541610 | -5.72334 | -45.03495 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5bae3801-28a6-3e00-9772-1515be283fbe | -5.72639 | -45.03794 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4f80d521-7cd0-3b2d-a858-e2d1f3e4cc81 | -6.30032 | -43.64232 | 2026-06-03 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81a223a2-3609-3ae6-8ded-b8b6a2502244 | -6.29054 | -43.63387 | 2026-06-03 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15afe79d-55fc-3103-9262-c15629462001 | -6.29103 | -43.63035 | 2026-06-03 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87dda586-d4d1-3d64-afb5-0af0a398daa2 | -5.92489 | -43.47816 | 2026-06-03 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cd26f9c-975f-3a80-a2d2-07fdc1993416 | -5.93032 | -43.47881 | 2026-06-03 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d34b11c-4843-3c09-93b4-af456d25f681 | -5.72228 | -45.03195 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ae425941-3780-368f-b2d0-bacf576bb06e | -5.30714 | -47.23844 | 2026-06-03 04:59:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28495bdc-3ee1-3ecb-99f9-2f7edf8a7ed0 | -5.8385 | -43.49354 | 2026-06-03 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 536a5172-2245-31af-a349-530ad086ad1d | -5.72303 | -45.02662 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71558e08-94aa-376c-ae3f-9b23ce686ad5 | -5.84056 | -43.48986 | 2026-06-03 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7be6dee8-7072-3476-a82a-2ea5c89f2393 | -5.92983 | -43.48221 | 2026-06-03 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a3ef528-85c1-3825-a821-fe27c8be4f33 | -5.72256 | -45.04025 | 2026-06-03 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 591ab2f1-f359-377f-96cc-394b3592c2fa | -8.06002 | -46.18492 | 2026-06-03 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e8cb38fa-5e9e-3f19-9027-848d42f7cde1 | -6.75774 | -45.00735 | 2026-06-03 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31afd0fd-6439-36c9-96ee-da231cd73be0 | -11.57503 | -56.32863 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc6ac6d1-ce40-37e0-bcb4-690271603eca | -13.96372 | -46.02884 | 2026-06-03 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c23711c-8602-37c0-864c-fe34f316f241 | -11.56698 | -54.58644 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 565421fa-e1f3-3bb4-85d7-a57053af6b44 | -6.991 | -42.88164 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a73bbaab-68dc-30cb-9330-d6044bb6a0b1 | -10.56941 | -57.32298 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 828b9e45-6a19-30d7-a960-5b70df9b727c | -11.2633 | -53.9682 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05a0ed5-cd54-3fae-bfca-0a5ac5a71716 | -11.94977 | -43.40257 | 2026-06-03 05:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8e4524-4fe8-327b-a715-532902ad61f5 | -11.57437 | -56.33252 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649109f9-b4cd-3d08-b0e7-3b94aab6a2dc | -12.73606 | -46.97237 | 2026-06-03 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e94bd322-5421-34d2-9729-e5f612872740 | -7.05077 | -45.0625 | 2026-06-03 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91bd2a55-4beb-3d26-85c8-02650e07c547 | -10.57235 | -57.32803 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7dc5df9-b3ce-3e4a-a813-e7cbac57a5ef | -11.81529 | -57.35664 | 2026-06-03 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 653807c2-1745-332d-accc-5f27ef35da8f | -7.50748 | -55.00184 | 2026-06-03 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af7cc651-f517-32f7-a325-0b6d0b83f336 | -11.04025 | -56.92749 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb6a819-c50a-320e-a966-8bbc3bec8cdd | -10.03288 | -59.34794 | 2026-06-03 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34f8db09-09db-34f2-9a17-e11936319071 | -11.26471 | -48.35951 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README7.md)
