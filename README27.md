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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b749277d-d919-3aa4-9661-4275f3fb7182 | -11.08276 | -44.12213 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 953e9e78-5dbc-3629-8181-96503c5f4f1c | -14.45249 | -43.96343 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 852216a7-b1d8-39bd-afb7-9ca04507c450 | -11.97957 | -43.47473 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26cfb5e8-2a1e-3aa8-b517-a193cb44e131 | -13.35261 | -43.92221 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd01e46f-2d56-3a4f-85fd-314ded6cade8 | -11.97501 | -43.49617 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13d23a38-b62e-34fc-84d6-698df694c4be | -13.63016 | -44.43035 | 2026-10-10 03:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cfe65bab-2240-32e2-bb4a-e7bc5c9168ae | -15.37707 | -41.92318 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| be053bee-6af0-375b-bec2-e9798467d894 | -16.22239 | -39.14722 | 2026-10-10 03:25:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 15776bb7-4ed4-3cd6-a7e5-48872c475cef | -14.45899 | -43.93413 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c06c4630-4ddf-364b-ad4c-b5e33a68d21a | -13.63219 | -44.4237 | 2026-10-10 03:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5b3287a8-ebe8-3887-9735-d36042dff556 | -11.94614 | -43.48828 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb2f9ee5-55f2-3b38-a22e-d774be8a3a30 | -11.76482 | -43.5309 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d85f4806-856a-3104-973f-29b95c4c2c13 | -11.60681 | -43.74453 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7c71b70-0a81-3df1-bc09-a21c314c78ff | -12.76937 | -44.89147 | 2026-10-10 03:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08548913-048d-3773-a47c-1c60a9738259 | -13.35129 | -43.92838 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08ae16bf-f9c7-36b0-a605-9fe279f180ba | -13.36509 | -43.90831 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88e4d7ef-9009-302b-8ba4-0c6831ee12a9 | -17.14937 | -41.3435 | 2026-10-10 03:25:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2efb8701-8d27-35ed-ab57-475c617a86be | -12.7751 | -44.88786 | 2026-10-10 03:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c28f1ec0-f1b2-3b9a-a34d-cc4f8dbab5ed | -11.0803 | -44.11501 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6932a617-4ab0-3277-897a-58f547e7a639 | -11.97592 | -43.45894 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f362956e-06af-3cc5-bb28-59d231c46ac6 | -15.37912 | -41.94219 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2e7553ce-279a-3c33-ab66-305bd2208b8c | -13.36377 | -43.91431 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2f0ae17-44cb-33bb-af9e-80e30fab9f48 | -11.95352 | -43.4865 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf551cfb-7fdc-37aa-a13d-af9bce48d657 | -14.45243 | -43.93254 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9553b5ab-6095-31b1-90e4-238b33da2b6b | -14.44752 | -43.93495 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7a00c9-a1a5-3594-87d3-9470b6f87105 | -11.02331 | -44.0496 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f23f8767-cf60-3605-88ae-7199a00e23f0 | -16.22289 | -39.14589 | 2026-10-10 03:25:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54b17c78-c256-3997-9a28-1903e360b586 | -11.97451 | -43.48659 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6168b793-1d11-31b7-9618-24cf67ff8004 | -15.37802 | -41.91864 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad0aaff7-02ad-367a-8b77-4bd63c85d0a5 | -11.98747 | -43.45757 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 127c10c3-020c-3077-afa9-9d819ab96372 | -11.56424 | -43.70867 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 50002281-186c-3f74-9b36-8e5ad19fa0cb | -11.65973 | -43.69652 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1341e52-8809-3264-af72-e67d80aa2f48 | -11.95602 | -43.48658 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c419dfb2-bf11-307c-b85e-68da3b92fc54 | -17.34955 | -42.68176 | 2026-10-10 03:25:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db34394-5f9c-34e2-af13-180806f7afb8 | -11.96241 | -43.47741 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af8b536d-32df-338f-8871-c9af3bb5d58e | -11.96583 | -43.49471 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d33ef9e3-03f7-3468-9605-8a785bc1f271 | -11.97604 | -43.49131 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beb8d482-7c24-30b6-ac3d-8045b7be2357 | -11.59868 | -43.74901 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4cc956d-d6ab-3e84-bf49-0148ff0d6ecb | -11.9585 | -43.47501 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac22fa8f-e0f8-35fb-9993-a9511418187a | -14.44984 | -43.9442 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d364945-0c06-362e-9033-b303a2442c83 | -14.45408 | -43.93656 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7edef42d-ae3f-3075-adef-247235db32b9 | -13.38372 | -43.88738 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6da5d65-4a85-3606-8a60-cd77822d1bdc | -13.36768 | -43.89651 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ff04d8c-711d-3adc-8d3a-298f8047926a | -13.36732 | -43.91913 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86b8d1f1-ad60-3131-ba95-7fe4df79906f | -11.60549 | -43.75065 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3caf47e6-5c35-3f62-8fc2-390f0cb61d17 | -13.38707 | -43.89219 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2233a19a-00de-3ef5-b9bc-c2475d6f2e8e | -11.99397 | -43.45995 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d55a53b5-f467-3c6b-9c52-050a3b10119c | -13.38039 | -43.89067 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f129a782-efa2-3da2-b1e2-60d806de34fd | -13.37113 | -43.90121 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37ee2eec-3034-3507-bce5-19338af15587 | -11.9601 | -43.48854 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| daf31e15-435c-3286-90a1-f0c7f8e43ff6 | -11.97249 | -43.49638 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c3b751d-0be7-3b3b-9607-6bbcd8a3e197 | -15.37519 | -41.93217 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bb75f632-64fe-389a-9167-e8119a9d416c | -11.08424 | -44.11516 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a809c7be-cd09-3f66-bdac-15d76e56ba24 | -13.36446 | -43.89963 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9064540-3b46-39c9-adb1-d4e6ee5919ed | -14.4577 | -43.93994 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e10ebbd3-9d5d-3eb9-9d74-ccecc73a0c34 | -14.32236 | -44.6778 | 2026-10-10 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ca53d6-bcb2-3168-9d55-c2e673563c81 | -11.60552 | -43.75079 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb02d589-7f78-3579-9b91-96df63cf00ce | -11.96503 | -43.47723 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 588465fe-8601-3dfe-abda-3142b4853d31 | -14.45156 | -43.94829 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2828bf5d-ab6a-353a-bb7f-59103948e332 | -11.98276 | -43.49268 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9906d40a-464a-32ed-a77a-43a3c87f201c | -11.03457 | -44.03028 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32545f2d-b2ac-33a2-b38d-8154b8017ee3 | -11.96378 | -43.48307 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 144960eb-ab6f-3de4-b5e4-2d5cdd68c407 | -11.59744 | -43.75533 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13e7b2fd-048f-33ff-8b15-1f69f6e7f351 | -14.4609 | -43.9692 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 545b4749-8f30-379b-b7fb-85fff5e5ca9a | -13.63072 | -44.43061 | 2026-10-10 03:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c029df0b-3f13-340d-82e1-9f9aa702d15c | -15.49496 | -41.47003 | 2026-10-10 03:25:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e654f0ee-bf11-34a3-bc69-55c7fbaf610f | -11.82578 | -43.59208 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0491ec3-7f5e-3d67-a5e0-6f280843f9f2 | -11.59198 | -43.74711 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9f92117-1d42-304b-babd-d16c4d6c6cb9 | -14.45907 | -43.96498 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3896d440-bded-3f8d-b0e5-cd7a67bb04ca | -14.45686 | -43.95578 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 77937abe-1f5e-3d35-9f75-fe5532a06948 | -13.26293 | -44.01092 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 74c21026-47bb-3028-b345-a8fcd87b5bd4 | -11.08588 | -44.12362 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3156b519-f864-3584-b589-9f1cf2c788b6 | -11.45989 | -43.37968 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| adbe401f-651e-3492-a916-a7a564cff572 | -14.96728 | -41.69506 | 2026-10-10 03:25:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 94a4dc16-1fc4-3504-b70c-5bb636d9c402 | -16.11098 | -42.85059 | 2026-10-10 03:25:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4a752fb-0489-34e5-bdf5-69e8c44b2884 | -15.37426 | -41.9366 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| adda97f0-0ead-3754-8743-ed196caa3e52 | -11.03284 | -44.06055 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| beec2151-580a-37d1-a8f3-0c90113c7788 | -13.25609 | -44.00983 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9a84854-fb90-3e65-beeb-c44fd44a885c | -11.01882 | -44.05742 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6854485e-8da5-39be-a1f6-57e8c8df5e84 | -11.95915 | -43.49313 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa551c47-a359-3b8a-9c20-6cb0b5fb176a | -11.0774 | -44.12902 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6474c480-4dfa-347d-b6bf-c903eb0a69c1 | -13.37438 | -43.898 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9db74d43-013b-37a5-9814-2b4b471f1386 | -11.59195 | -43.74701 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7e0b1e3-ed05-35f7-abad-e3deffdd0eb7 | -12.7735 | -44.89537 | 2026-10-10 03:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34086803-bec6-3417-b1f3-9668156be92c | -11.59736 | -43.75521 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6df91c9a-0718-3887-9864-9c58b08416c9 | -13.3724 | -43.89524 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e14c6875-0986-3a30-b8ae-89d735393b9b | -11.0219 | -44.05655 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b9d9361-392d-349c-9bbf-10f18e094786 | -11.99177 | -43.4502 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2debd17-f4e9-3a1e-825e-c4cf32b6bcae | -11.0687 | -44.11898 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d0d3548-3cbc-35cc-9a46-21e405e1c7f3 | -11.60432 | -43.72188 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22205752-413c-3f06-aadd-4ed42cb0a04a | -13.3904 | -43.88889 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fea88eaa-1623-3540-85a3-c28113bdfc79 | -14.44372 | -43.95259 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f440ca2a-f059-37ba-823c-8499d56d0ffd | -11.96378 | -43.47077 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 770e8ae2-6b13-3921-a88c-dc920b6c20c0 | -12.00128 | -43.43822 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8ca7e93-eff7-3d22-aead-105286000842 | -11.9559 | -43.47501 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1a988fe-ea77-31df-a42b-865e36654fb7 | -11.08174 | -44.10804 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 57d3fca9-b265-38bc-a19f-dc1537e254b6 | -11.59764 | -43.71964 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a1f1ef0-e2cb-3f89-a844-9b5d0a78399a | -13.3686 | -43.91311 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a807e51-026d-37c1-984c-fe0758966ebe | -14.46217 | -43.96325 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f4a4746-812b-3a20-acbc-78254710c910 | -16.82651 | -41.03369 | 2026-10-10 03:25:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
