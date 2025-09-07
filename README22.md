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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09efd243-de2e-3953-9a68-f1894ff92f93 | -22.42209 | -47.44477 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f2fa6be5-88b6-38b5-8b1c-76dda0710e53 | -19.74035 | -42.12622 | 2025-09-07 03:34:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f1734396-6d29-3ad4-a149-a93db78d4324 | -22.3307 | -49.37498 | 2025-09-07 03:34:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7311792f-6e46-3e15-a094-65d255df69d5 | -17.67269 | -43.53263 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c323c4c1-1266-310b-9d56-84bafd4e4137 | -17.87957 | -44.3368 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 864114e9-f1a3-331c-99a8-87119b79ecf5 | -22.41762 | -47.43525 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 024008e7-17a0-3e69-a912-018168525c6a | -17.55515 | -44.4032 | 2025-09-07 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b4a04d24-56d0-3050-8f25-b20d994fea5e | -19.50953 | -42.56757 | 2025-09-07 03:34:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2eb5d995-7ba2-33ca-8915-c49446bd461c | -16.90342 | -45.76563 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1fd6a62-7307-3ec0-a9e5-01c96d2a4f8d | -19.89537 | -41.44699 | 2025-09-07 03:34:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3ec341c-f345-3186-8885-2149610556fa | -22.4166 | -47.43958 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| c7f2ebf8-d10f-3931-80f9-05b3016e5210 | -19.42382 | -42.32771 | 2025-09-07 03:34:00 | NOAA-21 | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f29e61a9-48b9-3c65-b7a0-36072476d4be | -18.03403 | -47.09601 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1e2ca5a-64f4-3902-a16a-9079a52114bf | -18.6899 | -44.45234 | 2025-09-07 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f6cb707-43af-337a-89ac-4ed61fed0829 | -17.70301 | -44.48386 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53279305-09cc-3586-ac2e-147409e3a0a9 | -19.83339 | -44.24028 | 2025-09-07 03:34:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d47ed9b-96cf-3dc7-ad28-7416697e08d1 | -17.87585 | -44.32837 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab2bfc29-a69c-3385-8291-74aaee30c5cc | -20.54978 | -46.44676 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dd6f1178-c2d3-3320-8486-1aaf3ce7b628 | -21.48316 | -45.56174 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| abc2c6d6-b8a4-39b0-a52a-3a18bb4f9c6e | -22.41719 | -47.43945 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f2ef2866-07ff-3688-8328-f5a9d2d1049c | -17.69056 | -43.54327 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d51f061a-0552-3c64-b470-9d657ed2f3f9 | -18.63744 | -42.77145 | 2025-09-07 03:34:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b1ef6bca-1fdf-3231-ae21-15a54aa56a3b | -16.9208 | -45.79831 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7bb29ccb-758b-3f61-bc11-08614e986364 | -16.90778 | -45.77995 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 586c94cb-9e92-3c31-8dc8-a6d2e5fec535 | -20.54658 | -46.43468 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3e0bf929-c5fd-33aa-ac03-fab02ff188d1 | -17.71856 | -44.48927 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3d34889-a128-3edf-b458-9534e22c3f6c | -22.70045 | -46.92008 | 2025-09-07 03:34:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bb1f6578-66f4-311c-a44d-c76e7c602f65 | -18.37331 | -43.89248 | 2025-09-07 03:34:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40a2f88d-d490-34a2-9751-23dbc8457a35 | -17.22432 | -46.71989 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6b89a43-088c-3c60-a265-865874bae7ce | -18.01651 | -44.90893 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ab1c4e35-6f64-3551-88f4-e45cb5eae9ab | -20.53642 | -46.44575 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b8f3ae5-4e63-3eef-9ee0-2810824eb251 | -20.45912 | -42.52436 | 2025-09-07 03:34:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7f59a99e-8085-38ed-8ad7-ceaee7e0272f | -22.42344 | -47.4365 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 54aca484-4f17-3a13-97a1-dbefa776d08a | -18.35819 | -43.91499 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f9d4184-3765-30ef-a0d1-0d721dad2d20 | -17.68631 | -44.51104 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4be315f-76d2-3e94-bf4f-29e28852cf7d | -18.54784 | -43.82265 | 2025-09-07 03:34:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77793138-784e-3b92-ae6a-fcfcbce68829 | -22.69479 | -46.91907 | 2025-09-07 03:34:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8637787e-8b25-34dc-a477-5bc7916fbe78 | -16.92175 | -45.79394 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b7b75c2-8348-3582-ac18-4187c3a9ad2d | -17.69591 | -43.52088 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e33e377b-c67d-3342-9c68-78e7859a43fc | -20.34677 | -43.89392 | 2025-09-07 03:34:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3cee02d6-1c6e-35eb-a79f-cadceffc80cb | -19.8341 | -44.23693 | 2025-09-07 03:34:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91a8d611-59ba-3f90-9012-53839a2895bc | -17.55434 | -44.40711 | 2025-09-07 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10ef631a-18fc-3674-8769-770f8bfa79e2 | -18.68958 | -44.45188 | 2025-09-07 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48dc76f8-7434-35b0-b79f-7980891e2911 | -17.68073 | -43.54024 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6097ef5-a6c8-30ca-8db8-54f717d13231 | -17.70003 | -44.48753 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b5c006-174c-37c6-83e0-7741fd6758ec | -16.96843 | -45.83328 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f014ebd-5961-325d-86f2-5fea9fce56c7 | -17.69077 | -43.54673 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13d691a5-3ed2-3dd2-a44e-debd3393cc97 | -17.71767 | -44.49362 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a9282ba-b5c4-3e0b-9320-5df117b030ce | -18.01571 | -44.91273 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31ccce57-52ce-3a54-9951-5da6fdd65c0a | -17.68431 | -43.54817 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a94e981-3cf9-368d-b061-1f425861d8cb | -19.64885 | -46.07191 | 2025-09-07 03:34:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb962418-1783-30a8-8481-a4b490b6d9f8 | -17.22005 | -46.70603 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34a9c997-e0e4-37d9-bf1e-08dc99214c80 | -16.94015 | -45.76538 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86a36e79-d5e5-35a2-bab1-3ca6fb74c21c | -18.03501 | -47.0917 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75365547-9bfb-3279-8948-156d25a7ccbe | -17.69123 | -43.54003 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f56bd3b-3204-351e-9d14-93ebd29a5cf0 | -18.23641 | -42.66625 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| acc6c7ef-a77b-3696-b8f1-bfc674e1ef97 | -17.8766 | -44.3248 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 060e423a-a7e3-3e87-ada9-b4cbb937375d | -21.34006 | -45.87267 | 2025-09-07 03:34:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a8e7aeeb-933b-3182-9819-469644c16bac | -17.38267 | -49.23663 | 2025-09-07 03:34:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0eebb2c-654b-38fc-9bd9-fc8dbd15249b | -17.69614 | -44.49025 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42d058e6-60f0-35c2-a5c6-86e07964e822 | -17.68366 | -43.5513 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eb46b74-b748-32d9-a87c-a6748d2edc0e | -17.95109 | -45.30099 | 2025-09-07 03:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66a85ce4-a267-3d4d-8ab7-b9a6099e0dd7 | -18.03088 | -47.08912 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c36c1713-d67c-3457-83bf-66ac6ffaf629 | -20.35866 | -43.88542 | 2025-09-07 03:34:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 92e0d1b5-8ec6-35a9-9516-9c188279d8f2 | -17.95234 | -42.77346 | 2025-09-07 03:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78299a90-96f9-33d7-9c7a-77bce3d212a3 | -17.86393 | -44.33292 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d37fd9bb-aa70-3a1b-a57a-bbb8e6be84b1 | -19.88293 | -45.03084 | 2025-09-07 03:34:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b31c729-e843-3046-8a76-c94426eaec5a | -20.54281 | -46.4438 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0315a959-1c54-3634-b1d2-29f026a0e655 | -17.40432 | -49.31578 | 2025-09-07 03:34:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a7e8a0da-66cc-35df-86e0-a5e1ba8709c1 | -18.37265 | -43.89578 | 2025-09-07 03:34:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e575fdaf-0452-338f-aba1-f332e2761128 | -20.54703 | -46.45171 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| da9f6f3a-bcb1-3e1e-beac-60eeb84d79a6 | -17.63419 | -44.79037 | 2025-09-07 03:34:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fd40bba-a654-38b2-a096-9aea69e08e32 | -20.22063 | -44.20632 | 2025-09-07 03:34:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff9687dd-6927-3d8c-a6fb-e8be46636540 | -20.35738 | -43.8798 | 2025-09-07 03:34:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 40a497fd-dafe-3a55-8736-c4d66837e443 | -22.70134 | -46.91619 | 2025-09-07 03:34:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a9a222c6-f541-3620-b857-72672ef32bce | -17.95698 | -42.7725 | 2025-09-07 03:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0127cf0b-c39d-3ea0-b40c-fbba5bd5b1af | -19.48024 | -47.77753 | 2025-09-07 03:34:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27f78fe9-4cd6-38da-9b44-a3d0c82f40cb | -19.36654 | -43.65779 | 2025-09-07 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73560588-509c-34c9-8401-60751beb90dc | -23.22239 | -47.05738 | 2025-09-07 03:34:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 19c48848-1c65-35a0-af4c-aa570540f69f | -17.40203 | -49.31069 | 2025-09-07 03:34:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7426a996-d1dc-3eb0-b557-cf32c6f06086 | -21.46996 | -43.91173 | 2025-09-07 03:34:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 313489de-0827-3d51-843a-291525f7f9be | -21.33511 | -49.1232 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 48904d7f-216e-35b1-94d5-e0592b7ac78b | -18.59979 | -43.6454 | 2025-09-07 03:34:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b1e25d5-9410-306f-9cfc-c3dd208c8eb7 | -19.50912 | -42.57112 | 2025-09-07 03:34:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ad28a692-1f40-335c-a4c8-871db9ed391d | -22.42245 | -47.44072 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 933565ac-e314-322f-92c9-f7c256b2f1b8 | -21.33334 | -49.12712 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 5123c63b-00ca-38f3-9e4c-fe5f38b5ee1c | -19.06824 | -46.77445 | 2025-09-07 03:34:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b5367db-2c76-3301-acaf-099e0a3efdf7 | -17.86317 | -44.33648 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16c6b7a4-8dd7-380d-aa88-30868d375d56 | -19.34489 | -42.17238 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b7cc91d-6fed-316f-b26e-4d92587a7800 | -17.40895 | -49.31287 | 2025-09-07 03:34:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6687f70b-1a7b-3877-bb93-3f194c0e17a9 | -18.38163 | -43.89487 | 2025-09-07 03:34:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 195858b7-0138-3cc5-8e24-35cc57cbc85c | -17.67024 | -43.54484 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 489e26a8-41a0-3e35-ac13-e2211cc67c9b | -21.62791 | -44.01146 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 31d3be3c-6c3e-3405-ac9d-96eb6fa587b2 | -21.3416 | -45.87277 | 2025-09-07 03:34:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1c7b66b4-b700-39ac-8b0b-12a30b2985d8 | -17.69156 | -44.51252 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6807d7f7-ee96-3968-8b56-7d5b7b57128f | -21.63243 | -44.01701 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ca5ddb0f-6685-3c44-b247-d76908615679 | -19.53479 | -41.54789 | 2025-09-07 03:34:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1dc81269-dbc0-3137-bff2-f51874f6d723 | -18.35695 | -43.92106 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20fcdb13-4759-3999-89b6-5b26d2fb4c18 | -18.03592 | -47.08765 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6705e289-e02b-355d-b77c-a7fb6afb3f9d | -18.02193 | -44.91013 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README23.md)
