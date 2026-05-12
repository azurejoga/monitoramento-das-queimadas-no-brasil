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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad27e887-f37d-3762-9589-c0b37fa5b73d | -14.14599 | -52.89439 | 2026-05-12 03:53:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff1a554e-8533-3dbd-883c-ac911004e153 | -18.48617 | -51.70057 | 2026-05-12 03:53:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11a58f79-b4fe-36cb-ade8-cff684b0df1e | -14.14328 | -52.89472 | 2026-05-12 03:53:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4da889b4-e111-3804-a73d-c52f1eb3a58f | -15.87887 | -43.09312 | 2026-05-12 03:53:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| efbec5de-7704-3d79-8907-e65949354473 | -20.39896 | -45.33955 | 2026-05-12 03:53:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 24584048-6914-3a85-96e2-1e82c62cda61 | -14.13896 | -52.8924 | 2026-05-12 03:53:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18af34d2-d073-3519-9d4f-d274e4640b40 | -16.37449 | -42.31434 | 2026-05-12 03:53:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d0809f7-f5a1-3ab6-a583-cd5c7613a83f | -20.81385 | -45.18172 | 2026-05-12 03:53:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2924e672-1a6b-3822-b404-31e2edf2436c | -17.59123 | -46.64032 | 2026-05-12 03:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f7c441b-7c88-3463-afee-ddcdae58f9c6 | -20.52046 | -45.12178 | 2026-05-12 03:53:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66074d26-636d-3897-b603-fe2e89ee0f4e | -18.47896 | -51.70382 | 2026-05-12 03:53:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8aba692-7f47-34a4-bd08-468849ca9008 | -15.87802 | -43.09782 | 2026-05-12 03:53:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 775bb873-54ce-3c4a-ae7b-2c6228f42c7b | -14.14763 | -52.8871 | 2026-05-12 03:53:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1c1a97c-a43f-3d8d-8144-a4d0f1cea207 | -18.48352 | -51.70394 | 2026-05-12 03:53:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09e56593-fd78-3f88-9407-7e9af08d03f6 | -18.48467 | -51.69893 | 2026-05-12 03:53:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c949502-6718-30eb-8042-e1fb00dd1d92 | -18.68323 | -40.11565 | 2026-05-12 03:53:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 247ef812-ec2f-3985-afec-530eb5480bf4 | -21.33245 | -47.08337 | 2026-05-12 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b0056ea-dfeb-3ba3-acb4-dff665b31a92 | -21.33421 | -47.07439 | 2026-05-12 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bab8334-c4be-3776-9c07-80af7c530328 | -21.33187 | -47.0814 | 2026-05-12 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 816bc911-ff14-39db-a524-87d63f9f508d | -22.73908 | -42.25082 | 2026-05-12 03:55:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 759014b0-77f9-3071-aad0-ec97114557b1 | -22.74248 | -42.25149 | 2026-05-12 03:55:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 359f5f94-a815-32c4-9fcd-4f6daa838446 | -20.12981 | -50.49328 | 2026-05-12 03:55:00 | NOAA-20 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b73d211e-3cf1-3461-81b3-3717c4b25002 | -20.13539 | -50.49454 | 2026-05-12 03:55:00 | NOAA-20 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 140ed28d-4cc9-3fcf-a347-a9de43631283 | -21.28428 | -48.60175 | 2026-05-12 03:55:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 08214e3e-a1b1-3af0-bce7-0f8d706a48d8 | -21.33278 | -47.07692 | 2026-05-12 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b606478-4095-370e-be3a-0e569c18fe27 | -21.33333 | -47.07887 | 2026-05-12 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44b0fa17-8797-3870-b018-ae242ab8c9ee | -31.88638 | -51.82446 | 2026-05-12 03:57:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 51ca0181-114f-3812-9587-1e7fe617f46c | -11.0022 | -46.49036 | 2026-05-12 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9401eef3-3e53-3659-ba3a-32a528800238 | -11.52599 | -43.33018 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80ca4040-132a-37ae-8307-fab394eb4407 | -11.76189 | -43.63783 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 514829bc-f08a-3776-8c05-04319f094ef8 | -9.07429 | -48.65238 | 2026-05-12 04:40:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1594032-7050-3bd9-93f7-de255333b392 | -10.63576 | -48.01437 | 2026-05-12 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99719a59-1cdc-39fa-aa52-ad48f7bc50e3 | -8.70645 | -47.98419 | 2026-05-12 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa7684f-2dbd-3f04-adc0-46830a36b73b | -12.05307 | -45.28539 | 2026-05-12 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01c05698-c318-321b-9a3e-334becfa78f0 | -10.63978 | -48.01111 | 2026-05-12 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22698d59-a4eb-34c1-9205-d178a4d5839f | -9.64511 | -42.95551 | 2026-05-12 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 57f1a6b2-a456-38e0-a87f-e6bf3e5c2dfd | -11.97288 | -46.78516 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e81e5dd1-d796-3716-974f-b96d325390b3 | -11.76145 | -43.63498 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d72ced4-c112-3ef6-adbb-70c673e9bc6f | -11.52535 | -43.33506 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bdb810c-4c9c-3bd3-b0a9-05aa21e8d134 | -11.766 | -43.63563 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e552620-4635-3af8-b9f9-6a2d24ad81bd | -11.97468 | -46.78371 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc038401-1043-356a-9f72-c7b78e5d0fe1 | -9.42457 | -50.73201 | 2026-05-12 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8bbc69a-5416-3e46-8210-59f411400884 | -11.98034 | -46.78624 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 855b7d64-a570-3120-bb72-49ac49f51067 | -11.97405 | -46.78827 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b27a85f-4baa-3f2c-be74-d7a73b256bef | -10.63117 | -48.02149 | 2026-05-12 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a162944a-280f-3803-bd38-abae4239973a | -10.23794 | -52.22284 | 2026-05-12 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a50f597-b2b3-3f26-868b-775c1358a2ed | -11.05586 | -52.48699 | 2026-05-12 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95d6b6e8-ef5f-30bd-ae09-7ad56efd3827 | -10.13096 | -47.92416 | 2026-05-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b54a8950-65a1-3cd6-9a98-258287ce0986 | -11.97841 | -46.78425 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e1c11ff-71dc-32eb-8024-41956a404b87 | -11.7625 | -43.63308 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29e7ed1f-aa1a-34b3-b399-0916f8d8f5b9 | -10.63632 | -48.01059 | 2026-05-12 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a6db9b4-1f50-37d0-9300-8e382cbf9355 | -9.45593 | -47.82131 | 2026-05-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df22f46d-87fe-3128-92f4-813faf0a6765 | -11.97968 | -46.79077 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e7054c6-952e-3ba2-a43c-2b028d91dfd0 | -9.42512 | -50.7285 | 2026-05-12 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b17058-955f-3853-8ed0-e3f44ba2ba2a | -11.75626 | -43.63902 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd8db6c-d02c-36e8-9a1f-b6987ce07e4d | -9.62959 | -48.8843 | 2026-05-12 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8194eb8-a745-3de8-92ca-ea4fd6503bb8 | -11.73423 | -44.52728 | 2026-05-12 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 152433f7-8ab3-35f8-8a93-e5eff04cb5a0 | -9.44952 | -47.79285 | 2026-05-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3920a268-99e3-3ab7-b3af-444f9adb2c2a | -11.27688 | -44.6522 | 2026-05-12 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0080d6a-37f0-3d3f-bc72-ab7f2bc2f86d | -8.88241 | -50.04839 | 2026-05-12 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 937187a7-e9ef-3625-8a22-b1bc9a14ba26 | -10.13384 | -47.92854 | 2026-05-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4a9eb69-ac01-36cd-822f-1fe370b2b593 | -10.35349 | -45.16522 | 2026-05-12 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f9b57a-e1bc-3156-85e1-310f020d9469 | -9.45298 | -47.79341 | 2026-05-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc8b1402-0433-3ccb-be83-9051cd72022d | -11.05929 | -52.48756 | 2026-05-12 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b729265-f872-3066-8721-d7b773b4ed9e | -9.07764 | -48.65293 | 2026-05-12 04:40:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5a76b7-fbf1-3a0b-a75e-e9220ecc3ad7 | -9.39797 | -48.44202 | 2026-05-12 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d496585-b89b-3283-8f56-065040e656d6 | -11.00283 | -46.48596 | 2026-05-12 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10ad9859-b5a4-358a-a478-f7d38c461a04 | -9.64974 | -42.95614 | 2026-05-12 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 76c44af7-e135-3ca2-a4ab-7f7a1091a3ca | -11.06273 | -52.48813 | 2026-05-12 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23a64f41-0030-39dc-b279-b3b8438cb055 | -11.75674 | -43.64188 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68fb0019-2a6b-31fa-901f-b51176ed36ff | -11.05242 | -52.48643 | 2026-05-12 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c76b0cf2-11a4-32ac-870a-5c6e840a835f | -11.73536 | -44.51907 | 2026-05-12 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46ad879b-c4af-3676-8132-38c81cf1d993 | -6.98293 | -42.86667 | 2026-05-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c92ea317-f08b-3993-9c59-724af70defd0 | -11.76081 | -43.63971 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f991eb1-63b9-35f4-a868-b752c331ab8b | -11.97661 | -46.7857 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b8b916f-ff99-3120-99b8-fb74c37694d5 | -11.75734 | -43.63715 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcc7dbbc-4e1d-3041-8231-9fad1c70966a | -8.95262 | -48.11607 | 2026-05-12 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff4c673-78af-3f05-8d1f-f7665d102a81 | -11.76705 | -43.63374 | 2026-05-12 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b65039fa-0a0b-3d11-bf3e-b05d70f25c14 | -11.98214 | -46.7848 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab7f8982-4e4c-3c57-b125-3af979b169ce | -11.97778 | -46.7888 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 585d0044-8b1f-3d81-a9c3-43882f79e591 | -9.10223 | -47.96244 | 2026-05-12 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0df3d57e-2029-3544-b8f9-02aec9a02797 | -11.00655 | -46.48669 | 2026-05-12 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da2cd501-8d6b-35c8-86a5-ef34dc07eea2 | -10.13038 | -47.92802 | 2026-05-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56b2e5da-8ed7-33d4-b90d-82780065b0fc | -11.98151 | -46.78934 | 2026-05-12 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d188c3a-a8ba-3de6-ad4c-adb5f4cc4371 | -11.7348 | -44.52318 | 2026-05-12 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e380f28c-4c16-35d8-9a85-92c1c13c5515 | -10.24136 | -52.22341 | 2026-05-12 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6c76b0-3226-358f-a3d2-0ff93e914a37 | -8.53832 | -45.98113 | 2026-05-12 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2ff56fb-9fe0-3ed0-894e-79cfad5e425a | -13.18492 | -52.7062 | 2026-05-12 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d73e7b16-17c4-3641-8a2f-781e3b5ae8ee | -11.3013 | -54.02273 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4db8cf9-efa3-328b-aba2-b9c28ce83821 | -11.29687 | -54.02653 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7291ce4-9cf7-3d0e-a811-d1d7229d044e | -14.14593 | -52.88995 | 2026-05-12 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fb5f3651-f6eb-3429-b5c5-635ee40b430e | -14.70427 | -53.04202 | 2026-05-12 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 756cf5c1-79cb-303a-a7b5-9774c2d4f507 | -14.15867 | -45.42064 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1493be6-6af1-3615-8d77-a2a2a209d896 | -14.15449 | -45.42005 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4743e5d-6d81-38b2-95d2-63ce8d9ce554 | -11.74447 | -54.24747 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dc989f9-e15a-3462-b232-51d28b6fa912 | -14.1354 | -45.33718 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3658658a-87d5-3d3e-9921-8f0b4036652c | -14.72003 | -46.51797 | 2026-05-12 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b61815cc-ae78-3b0b-a523-2473633da137 | -11.73709 | -54.24615 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce68c59e-7831-389f-98aa-819708dc5d71 | -15.8773 | -43.09774 | 2026-05-12 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3b58a67d-8e2e-3d3f-9320-8a3d97c1444a | -13.46159 | -47.72963 | 2026-05-12 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
