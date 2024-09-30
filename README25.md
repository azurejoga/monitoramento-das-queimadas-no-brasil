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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3e79983-9847-3e73-b83e-8d1d5baa5188 | -17.63852 | -46.66876 | 2024-09-30 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86da6a1f-2242-367c-8407-80262574d256 | -17.63702 | -46.66784 | 2024-09-30 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d886e582-4a87-395e-bff7-ee5a7815f1d2 | -17.63347 | -46.66767 | 2024-09-30 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9acc513b-8bf6-30ab-858f-f68170ccf3ae | -17.63284 | -46.67079 | 2024-09-30 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f0effcd-0c2d-344c-ba07-8f834014626a | -17.14421 | -44.83868 | 2024-09-30 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6882d333-eccf-365c-98ec-10f92174b7cb | -17.09649 | -43.80487 | 2024-09-30 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5650c8-8655-38b3-8128-00177ece5ec4 | -17.00087 | -45.30599 | 2024-09-30 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 933a2f3a-6c14-3a42-a563-b86a20368f85 | -16.92027 | -47.17507 | 2024-09-30 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff7b775d-51fb-371d-bf6b-1168ea5c61e7 | -16.90646 | -45.33165 | 2024-09-30 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dc7555d-31a9-3c60-a834-64d94cf75a8e | -16.90278 | -45.3254 | 2024-09-30 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 075846e5-9ca5-3cfb-9076-cedc34e35071 | -16.34873 | -43.69696 | 2024-09-30 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 158e2c69-ac80-381b-8deb-f7d7fa2fdf1e | -16.11595 | -50.36706 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2002d4d3-bbd7-3412-bf47-b3949065953b | -16.11468 | -50.36842 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85c01010-3db2-3c99-b82f-2e639ad41bf6 | -16.11092 | -50.35886 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5966220-07fe-3b1d-86c4-fa230cc0f16a | -16.10973 | -50.36008 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6c475b8f-3cc8-3c00-9d77-70a1fcbfb4d9 | -16.10971 | -50.36443 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00b341a9-4539-3aec-82a8-a27ea688e588 | -16.10843 | -50.36586 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89f0a6cf-3225-30c0-ba03-e67f5dd95832 | -16.10469 | -50.35622 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2c95c2ac-3000-38bc-8428-c2b4802f4b3b | -16.10467 | -50.35227 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d661861d-fda1-336c-b826-3d58aa4ad353 | -16.1035 | -50.35747 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fd34065-50bf-3237-a3e0-d647eb5a354c | -16.09966 | -50.34805 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36eb88f0-bfd4-3204-be82-16c55b5de162 | -16.09854 | -50.34923 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfa75e05-17ed-3788-890f-cb540c247c79 | -16.08174 | -50.3632 | 2024-09-30 03:47:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93eba99c-1c87-3ed7-b879-f5d70ac68c4c | -16.08161 | -50.36821 | 2024-09-30 03:47:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 780fda11-a0bd-3432-b99b-347d4f159dd6 | -16.08026 | -50.37437 | 2024-09-30 03:47:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 96770792-6c09-3fc3-a5c0-1274875e5220 | -16.08024 | -50.36975 | 2024-09-30 03:47:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 81c00492-6624-3084-8b47-dc34f18318cd | -16.07889 | -50.38058 | 2024-09-30 03:47:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 40995e12-e48c-3244-be12-74069ecb6dcc | -16.07884 | -50.37593 | 2024-09-30 03:47:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 38bc925c-b459-311a-ab6a-6c98b855cc2b | -16.07734 | -50.38254 | 2024-09-30 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5f502b13-e831-3824-84c3-a9c5381b91c0 | -16.07667 | -50.35968 | 2024-09-30 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff65ceec-ee3e-3c76-b77c-e47d529d397b | -16.07516 | -50.36209 | 2024-09-30 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba8aa851-0012-3369-82fa-2a048e69a429 | -16.009 | -42.25179 | 2024-09-30 03:47:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8c02832b-b00d-3637-a21f-dea943380e71 | -15.9795 | -47.23089 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dde670b0-dee2-3167-9686-eeffa182f40b | -15.97414 | -47.22949 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a34bbb47-9359-39c2-a283-c6fd9203140c | -15.88918 | -45.0578 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 654de607-39bf-33e8-b518-db491c26f437 | -15.88819 | -45.06302 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0574fd31-c0e6-38f3-bf6b-c87b79ccb7dd | -15.88633 | -45.05406 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45287295-ec20-3661-acbf-bc88885dd7bb | -15.88546 | -45.05164 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65593112-5225-3020-b0c4-df68e23a7106 | -15.88531 | -45.05925 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c33f08f6-3dc0-3135-9415-98d898dbeb9e | -15.88447 | -45.05684 | 2024-09-30 03:47:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b8b7f66-e966-3ecd-8df9-9c85644223ca | -15.33442 | -47.50284 | 2024-09-30 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 650411cb-323f-3bf6-b626-e5528edbf9f7 | -15.32888 | -47.50158 | 2024-09-30 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cd22af11-e7d6-3fde-915a-a533e9a9494f | -15.32811 | -47.50532 | 2024-09-30 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2e06104d-07e7-38ac-985f-048dd9ca01d1 | -15.32335 | -47.50024 | 2024-09-30 03:47:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35bcfcf3-966a-3d49-8ce5-85b1296dc27b | -15.29389 | -47.47453 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44d9c66b-9cd3-3861-a504-16300fe565be | -15.29054 | -47.49054 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b75d1f97-f377-36e0-b8a2-2e7697341f91 | -15.28986 | -47.49382 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cd32760-6a9b-3e46-b065-e462adb9adf7 | -15.28914 | -47.49723 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed76b743-6235-33a3-81e0-3627a319d807 | -15.28831 | -47.50119 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27ed6f4d-800c-39c9-9799-40cf2fe96650 | -15.28745 | -47.50529 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbe6098f-8f41-3cf5-b906-d92002cac035 | -15.28465 | -47.49858 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fdaf381-b127-373e-82d3-5affa0bc4c72 | -15.20601 | -46.23288 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a4dd6f8-d9a0-37c3-9b3f-931598c0522d | -15.2009 | -46.23163 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe9172d3-a154-308a-84b5-9c18c3a9d350 | -14.9413 | -51.09415 | 2024-09-30 03:47:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c0c66e6-e034-3b74-a654-618428f6046e | -14.76539 | -48.75428 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ca126ea-69c2-3439-87bb-d5caacec59bb | -14.76213 | -48.73972 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 34d87f26-425b-3e39-bdb6-9fe96d394be9 | -14.76124 | -48.74391 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dc8cda0b-e61c-373a-9860-40d7a2f20dec | -14.76028 | -48.74848 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f56f44f3-33c9-3383-bc45-36d36e6cea23 | -14.75926 | -48.75329 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8f02d1d3-6813-3b70-92f7-b3e31bb12c72 | -14.7592 | -48.35673 | 2024-09-30 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 036f4338-28c5-3dfd-8107-94727165ecb7 | -14.7584 | -48.75734 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 50d01075-f245-3aa5-8650-6319372cab19 | -14.75593 | -48.73908 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5eeb0eeb-b8b1-3554-9063-44c83ea3d3eb | -14.75503 | -48.74331 | 2024-09-30 03:47:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0d68d6a1-710c-3220-be32-320ea75d61dd | -23.13132 | -45.56386 | 2024-09-30 03:49:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf96a8dd-5f8e-3b19-a03d-f2cca1bc56f9 | -23.07912 | -45.40932 | 2024-09-30 03:49:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e91a6f19-1fab-327f-a0e9-5ab517d6f682 | -23.07822 | -45.41384 | 2024-09-30 03:49:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| eaf16eff-f8a0-32fb-917b-20a77803e6b1 | -22.67643 | -45.52202 | 2024-09-30 03:49:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 464de755-e51e-33f2-a10d-aa50e3c93f9f | -23.49814 | -47.22614 | 2024-09-30 03:49:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61c79eb2-d685-3222-aa0c-b702ca759adb | -23.35198 | -46.99212 | 2024-09-30 03:49:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4e1e2b79-b2d7-3f06-938e-c163e8c84639 | -23.33982 | -46.77332 | 2024-09-30 03:49:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 43b99213-8334-3c5e-9070-b3435a495c1e | -23.31285 | -47.13401 | 2024-09-30 03:49:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa83b18a-12ca-3d38-a452-78236d5cb5c1 | -23.25813 | -46.45861 | 2024-09-30 03:49:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2f1fa80-b95e-3e7c-9514-f1562a890c69 | -23.25581 | -46.46067 | 2024-09-30 03:49:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30db5b57-dffb-3791-8fcf-557acdd19154 | -23.17271 | -49.59227 | 2024-09-30 03:49:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7d7a282-d2f2-330e-bf41-5710ea382bfc | -23.11162 | -50.40854 | 2024-09-30 03:49:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b60683c7-22df-3f34-9185-cc39db7918e0 | -23.11061 | -50.41286 | 2024-09-30 03:49:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ff59cf72-b5f1-3b14-be14-c13d2e148fbc | -23.10956 | -50.41738 | 2024-09-30 03:49:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2061b693-9a2d-3d54-8ea6-8b3ae4ebfd91 | -22.78048 | -46.62256 | 2024-09-30 03:49:00 | NOAA-21 | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e3e3bd13-c3f1-3f94-90d3-3c7f0debe508 | -22.77043 | -46.806 | 2024-09-30 03:49:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1895ff2a-2afd-38b6-a082-4a9134e60b2a | -22.7693 | -46.81137 | 2024-09-30 03:49:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97dea834-88b2-3197-bbc9-159b29511891 | -22.73358 | -47.02718 | 2024-09-30 03:49:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 68121eba-9879-392f-bc70-ec36f1c86fdb | -22.54756 | -47.45838 | 2024-09-30 03:49:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 92342e49-1c0e-3cbd-8bbf-861c4c1242e7 | -22.25024 | -49.67426 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1fe8246-e161-310e-8f8e-6570c4bbe844 | -22.24889 | -49.67278 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fcb7ec82-62bf-3515-94ee-7cdf3bb737f7 | -22.24795 | -49.67684 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6256a314-9821-39e2-8004-772bf29d56bb | -22.24466 | -49.67304 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 74525af2-c2a3-39f9-b4c2-86188d909526 | -22.24376 | -49.67708 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 827bfe9f-edcd-399f-8f18-1806ddda5c5f | -22.24331 | -49.67158 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6e19fcd-e8a6-3003-99e9-60439fd1d209 | -22.24237 | -49.67563 | 2024-09-30 03:49:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b8c2312-45f8-3bf4-8a67-59da83f07d92 | -28.69023 | -50.41127 | 2024-09-30 03:49:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ae5529f-51bf-39ca-a3ea-6a775ff67732 | -28.50936 | -50.66298 | 2024-09-30 03:49:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 534cc115-bd7f-3992-a4ae-cb8090c00468 | -28.50767 | -50.67009 | 2024-09-30 03:49:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26cfc9a0-4d12-36b0-a8f8-160a03932468 | -28.50852 | -50.66653 | 2024-09-30 03:49:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f17efbf-f4b7-3a91-90cd-d27d6457fbea | -29.73187 | -51.13823 | 2024-09-30 03:49:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| be8253f9-8950-3a4b-8d2e-4fa21dc806b6 | -29.73101 | -51.14177 | 2024-09-30 03:49:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 3641146d-fd1b-3708-bced-c0f080ad6d53 | -11.15 | -45.74 | 2024-09-30 04:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50bcfb8c-5855-3c7d-9b54-b5b59951cbfb | -1.21196 | -46.73148 | 2024-09-30 04:27:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a955f2c-a973-3b94-b171-c3a2b203baf3 | -1.21142 | -46.73491 | 2024-09-30 04:27:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07157f8c-53f1-373e-8b9d-078203fc38e9 | -0.74648 | -47.5101 | 2024-09-30 04:27:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53712fa2-2aaa-3ccf-8254-1796c4fbf377 | -0.85398 | -48.54232 | 2024-09-30 04:27:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
