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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d562f604-b73e-3565-ba72-380d327acd76 | -15.38163 | -41.9014 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| de02714e-f772-3f46-a6bc-0c45af1f8ecd | -11.95499 | -43.49141 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 411522da-2771-397f-b8c7-37daa5da7366 | -11.0787 | -44.10663 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2a58568-9593-39ae-8982-43aa0f9ffa86 | -13.25601 | -44.00382 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd01cb38-572b-3a22-91ca-0416a2f2f669 | -13.37784 | -43.90265 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3cb73a97-18bb-31c4-914c-86ae839f7df5 | -14.05663 | -43.83253 | 2026-10-10 03:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84d3db55-871c-3cb6-a835-d949b2ebc28f | -11.94966 | -43.48353 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df313197-7f90-330c-9c83-43ae90b4dac8 | -11.59778 | -43.71962 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9cbc8ce9-83be-35a2-9bba-2dda61a936f8 | -11.84219 | -43.60861 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c955ef-943c-3c77-be49-ac59968eb390 | -11.01347 | -44.06189 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac871346-abd9-3db2-8b97-61bb7d2d7a82 | -15.85294 | -42.03756 | 2026-10-10 03:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a058f402-750b-3d10-9679-d12684a7a541 | -14.4551 | -43.95167 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5744587d-29fd-3ef6-960d-3896e60eb132 | -11.04129 | -44.05526 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f07381a6-9c97-33df-a590-d42a52a3ad4f | -14.96645 | -41.69905 | 2026-10-10 03:25:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 21caff68-b4b4-39c4-bbad-014f30fbb1ee | -11.59505 | -43.73245 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5b3ca726-abad-35a8-bb33-be03118f31ac | -14.97301 | -41.69627 | 2026-10-10 03:25:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c0c3656f-58ae-33fd-9718-e50306b16dd6 | -11.96167 | -43.49296 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fae6d663-7010-37ce-a0ce-389c5d479dae | -17.09661 | -41.56941 | 2026-10-10 03:25:00 | NOAA-20 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6043bf31-2703-3031-a355-ea08acead6ea | -13.37046 | -43.91584 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e67ea3c-b4f8-30db-b378-7d5d4549e249 | -14.4556 | -43.96167 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f7335b04-5740-376e-b8ca-ae14ecf2a9ad | -12.22851 | -44.69511 | 2026-10-10 03:25:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07b8d98e-89df-3983-8d44-503ee257b8ea | -11.60682 | -43.74438 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ef80e4b-1113-3db0-86a2-d14eaed40ae5 | -12.03409 | -43.38181 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 864fa40c-b2cc-31cd-accd-1f544c33af59 | -13.26163 | -44.01064 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df6c0ff0-d219-32b0-8987-78ecd92301ca | -11.98018 | -43.49308 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e56154a-43d1-317f-a137-2f3f87bf063a | -11.94722 | -43.48309 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf22aa8b-62b0-3d72-9a99-5fbc0c4cd402 | -11.98477 | -43.47077 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d225d537-04e4-3f3c-975f-3fbc5b003924 | -11.97953 | -43.46221 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1078eb32-2ef6-34f3-9b3a-614168337214 | -15.36938 | -41.93114 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 27ca526e-717b-332b-a1f2-0af661bf856a | -11.83665 | -43.60742 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5e246fa-2f1c-30ba-b638-0e3df5703134 | -11.96836 | -43.49446 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a58a4a2-1381-330c-a47c-d7d7542eac0d | -12.05043 | -43.40347 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e390cdb9-f71b-34fd-beef-f38624f19204 | -14.32379 | -44.67118 | 2026-10-10 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ecb5ad3-dd0f-3cc6-8404-e7114ccc47e1 | -15.37126 | -41.92215 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8991d08a-9672-3140-8ebf-8f6a807c5582 | -11.95251 | -43.49136 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a28ae03e-4e6f-3ef8-b3b8-dea8f2f85aff | -13.37911 | -43.89668 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cb31f13-6f14-3cf1-891c-2b4590b99603 | -11.95079 | -43.47828 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8c11876-8deb-3ca6-884c-f9e95094db34 | -14.46064 | -43.93817 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 79b58e4a-10ef-3602-856c-ef9454b81397 | -15.84724 | -42.03607 | 2026-10-10 03:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96ddb53e-c382-376d-b03c-8f7bb3356862 | -11.94856 | -43.4887 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bde8692b-eda8-3d9d-b068-9808edf913df | -11.97044 | -43.48472 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e61f28b5-2e47-3c30-8447-a73d0ccaed25 | -11.94063 | -43.4811 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f999f0c6-1c85-32b5-bd1f-ddb21be4f0bb | -11.96903 | -43.47925 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f344f9eb-972a-3052-bfc7-1a58b8676746 | -12.77644 | -44.89336 | 2026-10-10 03:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bac4fd3-4c93-31b4-8ac3-d95b3838b534 | -11.96935 | -43.48985 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78e47b91-f8a2-38b2-8cc9-9d2c49aa6027 | -15.38077 | -41.90554 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9eba401a-8655-3734-a9f4-51cc4d139a45 | -11.97296 | -43.47287 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ab5e381-6db9-3b6e-9dd2-6d1992e10281 | -11.60445 | -43.72185 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d14362c-3daa-3880-a736-93e8ae7c51f5 | -15.38249 | -41.8973 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b80b6444-7105-34fa-9ef2-1ebf613783cd | -11.66514 | -43.70475 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ccd9ad2-8fa7-3b29-ace6-c33866480ced | -11.95722 | -43.481 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8ad761f-6ef1-35fe-96c1-1b29b45877e3 | -13.46181 | -41.35014 | 2026-10-10 03:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c6eefc85-2800-3ba8-9f13-cc5546a72e91 | -12.22145 | -44.69318 | 2026-10-10 03:25:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a700e2e-8cbb-32fc-a301-0c01b298ec9d | -14.45812 | -43.94991 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d684709-980b-39d5-95df-edf18d13ebb9 | -11.01736 | -44.06432 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 195060cd-29ad-3cb7-85a5-6a9b722640f7 | -14.43802 | -43.96626 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abd7dc0e-0fc8-3514-9deb-dd940f7858d2 | -11.85281 | -43.5979 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2dede1a4-f825-306c-873e-b6692dc2ee7b | -11.83532 | -43.61366 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbf0acba-e0d7-30fc-bb78-7f4af536b975 | -14.45114 | -43.93835 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65926a97-6a5c-3942-a39e-88fc2f68d6d1 | -14.44877 | -43.92916 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 452e5844-dc6c-3e54-b582-b44706e2a1db | -11.83416 | -43.6133 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18f51f5d-7d79-37d6-859a-cda161bb2c40 | -11.9983 | -43.43879 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65e805ef-504a-3790-bc0b-5439280eedb3 | -11.02583 | -44.05899 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24636245-f416-35e0-80b9-9b6484134107 | -14.45432 | -43.96759 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0234d75-5867-33b2-95dd-f9fdceb5f179 | -11.97173 | -43.46611 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e26706a7-6772-39f7-bc66-e24aa721c0fa | -11.98607 | -43.46439 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07ade74c-5bbf-3501-80ed-d5b1b6b48ba4 | -11.45439 | -43.38196 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae709ed9-652d-3278-a772-679525401756 | -14.45938 | -43.94405 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| abc385a2-dcbf-3253-ac6b-6b20ebb90504 | -14.05901 | -43.83384 | 2026-10-10 03:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bc36d7b-4350-32f9-8792-07e79fc095a8 | -17.34383 | -42.68 | 2026-10-10 03:25:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cc77b39-5ef1-3984-ace5-e74cf13c1aaf | -12.2232 | -44.69668 | 2026-10-10 03:25:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 42a3d24f-c7bf-3f52-9fa9-fe29523573bf | -14.05534 | -43.83841 | 2026-10-10 03:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48311c53-71b8-318a-b122-d9a8aecc9134 | -11.96265 | -43.48835 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12a0af01-5ce1-3e74-ba00-ecaac63287d3 | -11.99534 | -43.45328 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d3d9105-67c5-3215-a556-653fc776fd09 | -14.45282 | -43.94241 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6201fdf9-ebc4-3ba0-9a16-a6b9a02c8529 | -11.97349 | -43.49154 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abaebf02-a6a1-3be5-b861-d40b34e41e6f | -11.94172 | -43.47587 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5636079f-2a9f-3a43-9305-fad6ac8ef4c3 | -11.46655 | -43.39095 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23315ac3-cfa6-3a85-b592-d59940ab78f4 | -15.49419 | -41.47378 | 2026-10-10 03:25:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 73f0e598-9629-3658-b049-a5e3ab6c1fac | -14.4538 | -43.95755 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 79c280ab-8345-3205-b132-1c250bd6c3a3 | -14.43458 | -43.96289 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e199bb5-97cd-3455-8735-9ba5b32b3c33 | -11.04274 | -44.04834 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f3ac92b-1b67-3075-8a37-2d1068c8de59 | -11.9733 | -43.45851 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c9bb196-b63b-3b81-9ed6-a58e17bc1292 | -13.25479 | -44.00956 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45c196c9-285e-3a52-bb6f-b19204bf0669 | -13.36639 | -43.90239 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff58604d-441c-32c1-b7d3-603e254b6c2f | -16.71658 | -41.88422 | 2026-10-10 03:25:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 657f6590-0f59-3432-9af8-2abb20d27146 | -13.39175 | -43.88274 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58f10ff1-df52-377a-9fb0-23e7ed80e691 | -16.71095 | -41.88309 | 2026-10-10 03:25:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25792a2d-2198-33db-859d-9f649a280621 | -11.12118 | -43.25541 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98fa22da-405c-3695-adf9-7dfcd62e9457 | -15.38737 | -41.90273 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e5d4e2c1-5245-3363-9018-1942d05fd994 | -13.63167 | -44.42347 | 2026-10-10 03:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d04562e-f937-32a3-8f24-99bc3a1e6cb8 | -11.46536 | -43.38726 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6949c99d-d378-37c6-b9e1-82cd3e80e745 | -11.83545 | -43.60704 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc52434d-95f6-3ab0-98ab-119230026041 | -11.60435 | -43.75649 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e64fe92-ef1b-3945-99db-71aecb7e1f5c | -11.03428 | -44.05369 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c10ae84-aa47-36ae-a7f7-171863dc9ea3 | -11.98087 | -43.46859 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e059c40-da2d-3ea2-8de4-af21ed33ee92 | -11.08018 | -44.09967 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 10fea46f-5855-3962-a238-0480f13d2019 | -14.05776 | -43.83975 | 2026-10-10 03:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f244065-038b-31a9-962a-206610cf89e8 | -15.39867 | -41.90619 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 94e354e8-8382-3a58-a002-b9dd2f2ac579 | -13.38837 | -43.88604 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README27.md)
