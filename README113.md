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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49dd9012-eb5a-3f01-8b02-b1915e16edd5 | -3.63628 | -60.54848 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c45b62-8f12-336c-a82c-6d4632c0f8a2 | -3.90363 | -55.88742 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c88202-4e0a-39a0-8e7f-83ef3f02b9b3 | -10.28707 | -50.55251 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7dd29c-c736-3a2d-a584-6bc9fd339a7e | -4.42041 | -55.50007 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e41da6-69bf-3b1f-81cc-7b8228f2474a | -3.04396 | -54.3977 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7f04ac-d66f-3ac5-84b1-fe79d6fd65eb | -3.89652 | -60.58865 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf405fec-86b1-3d2b-aaaf-268cb733709b | -12.32287 | -50.22175 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df802edf-bd1e-376a-801c-b648aa0ff4ee | -6.18104 | -52.79894 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4f395ce-255c-3873-8227-d46261f8a865 | -3.33864 | -59.86925 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2283662a-d46b-3b96-85dc-65e0a567d75a | -9.65907 | -54.33958 | 2026-09-23 05:23:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b8b5d46-2b83-3fd0-b52a-3511ea7026ef | -3.78702 | -60.74889 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8037cfa6-f61c-3ab5-b24c-c018abac22e5 | -3.33979 | -59.86209 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 501b1b3a-f99f-3d49-bdaa-6064e8c42bac | -3.64723 | -60.61156 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb93926-2a4b-307a-8db8-9c5f60c53602 | -8.23058 | -62.83691 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b8575dc-b708-3c19-984c-6945d1948c9c | -3.10661 | -60.72623 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18f9061-792d-31a6-8506-a94fd4dffa80 | -4.45397 | -55.06768 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a538a92e-ed42-36eb-8821-f00af8f988b4 | -3.2886 | -57.85329 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3dd871d-aa12-397f-a2da-1bd3753f5b44 | -3.29796 | -57.85867 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c2d5305-984d-3faf-9d0b-4ef44d7a33e4 | -5.89484 | -52.09757 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe2c44a8-991e-3870-bfad-95765fd1ffeb | -11.12419 | -49.45731 | 2026-09-23 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ead3a56-2737-3553-9033-0d431f9de0ab | -4.42906 | -55.08173 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df943ad8-39e5-39b8-baef-53ca51a6835f | -9.16308 | -61.3605 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e84a63a-9205-305a-bf6a-94fe017da3b1 | -9.55312 | -65.99404 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0800c8f8-0e86-3bc3-ab10-348cebdea954 | -10.27257 | -49.97231 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a76c337-6a63-3de0-be70-ffc5bec2b180 | -8.23629 | -62.82484 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a326b6-7c3a-3848-831a-7fb4f74a2902 | -10.29017 | -50.52765 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b2e005a-7251-3634-b165-5d022c3cc22a | -10.82612 | -48.47783 | 2026-09-23 05:23:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4824ef8e-9dc5-3a90-9c02-efa3993c7639 | -5.88689 | -52.28411 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffbd90ff-e4de-3993-b2c8-299c7160a15b | -3.78642 | -60.75267 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdf2b4bf-cc69-3840-89ea-6b0e39cb84cf | -2.76298 | -57.03209 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e27c449-a3d0-3996-bb46-ddc59ffa71e8 | -11.69402 | -50.77938 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25a9bf3d-8a99-3109-8cf4-dded183f3751 | -9.08828 | -61.01383 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27e8c372-d770-357b-9b23-dd2d1169369c | -9.93596 | -48.47086 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8128881b-a7e9-36c6-a66b-dfc648853f9d | -3.22743 | -61.05755 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a2b679-72d2-301a-96b0-78869ff6e046 | 0.97717 | -59.38018 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb31be2d-6c37-3709-8da1-73e446f7842d | -9.16226 | -61.38671 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd8071b-57ef-3f1d-bb29-f55e5e0ef746 | -9.16646 | -61.36106 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e37be68e-3010-373c-a9ac-19563b7beabe | -2.7448 | -51.54523 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d601cafe-00d9-37e5-b9fd-578d0040629d | -9.93539 | -48.47558 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e20d44b-688a-3360-a53a-53048e5b295a | -10.31513 | -50.50566 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e32c4f0c-3528-3805-92f1-f412b9c3b711 | -9.71555 | -48.33463 | 2026-09-23 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 669c314f-d072-367b-a1d6-9a1a72de4327 | -8.31246 | -54.78624 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb226e85-d847-311f-8d65-70519fbf03e7 | -10.26025 | -49.97851 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee0a5771-168d-300b-8474-99f7264d69a1 | -6.88825 | -46.56736 | 2026-09-23 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b2c6b91-1b2b-3072-a1bb-3c1f7db797c5 | -3.08662 | -61.16727 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74777b5-216f-32c4-b14b-7f9f5c6a3b0a | -4.04991 | -56.31736 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94124d51-4242-3776-830e-ec58a5f72b41 | -3.93844 | -59.64747 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd86cff7-e521-3860-ae16-c54792120dff | -3.44709 | -58.18282 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc6abc44-47e4-33d1-8bfc-e67908c18aac | -5.29958 | -56.09961 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e149c301-148f-3e36-937f-218264e42cb2 | -4.51475 | -54.98001 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7832dd50-bda5-3b82-9339-94cb8c7e11be | -3.19415 | -57.78527 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0a58bd3-d86b-3a68-987c-ab278de727a5 | 0.78268 | -59.1923 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf62a7a7-4b71-3649-b080-5b9bdd82cfd4 | -9.25792 | -65.44278 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 278be68b-6a76-3a3e-af38-64153f572d5e | -3.39223 | -61.06697 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b81eeed5-ce2a-3ab0-ace8-ec5fdad64256 | -9.11139 | -60.94789 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee6c5e0f-6e8b-3cca-a3d5-bfc3664542a9 | -8.18421 | -61.18388 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cec75b9-0441-31b3-8faf-010311f35454 | -9.09487 | -61.43236 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 184f6fad-8884-3ee0-92cb-57aa355a6cc6 | -3.92911 | -56.05046 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2e249f2-2e9e-33fa-add1-50a3f597aaf4 | -11.65781 | -50.98221 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 519e528b-d90f-37f4-99cc-ddcd3c833550 | -4.4593 | -47.92152 | 2026-09-23 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1547f1af-e0be-3b9b-9216-255c5256a90c | -3.78176 | -60.75968 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2b780b1-1500-3d1f-89f2-5a3fbb2ef620 | -4.15275 | -50.45684 | 2026-09-23 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0da6e182-2fa9-3b60-ac04-85e65d3be409 | -6.87771 | -46.57084 | 2026-09-23 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f4d6eb2-62f9-3dbb-b686-aa0797bf411a | -10.29562 | -50.52838 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3c8f0b1-b5f3-33b9-b75e-869f7036718e | -3.63474 | -58.84386 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cca90ed-f909-30dd-bc9d-fe361e9d369b | -2.28567 | -58.09513 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6cbdfe2-b002-3014-8da0-e705e24f4745 | -3.82145 | -59.33503 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ada8346-3560-3c35-8900-a0c656a309dc | -3.18958 | -59.70002 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05877b03-d258-3632-afb7-3f28ad378b2b | -7.83206 | -63.41634 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dcc426a6-e6d3-3d26-b8c2-116c7134add9 | -1.91585 | -58.26207 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26228b56-98ee-3aa4-878f-c6218114f230 | -3.94148 | -49.9938 | 2026-09-23 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48fbfaab-dc89-3a16-bbfa-b0e0b8798ddf | -11.78136 | -50.97694 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b73089b-08e8-330f-a198-4b6339f87bdd | -3.83837 | -55.86512 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 355468a6-3628-343c-bc68-cc577751f77e | -4.06899 | -56.21821 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a8d0ce1-0a37-3d34-adb3-8303a5c7e8d8 | -3.06692 | -61.29166 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50abca4a-e8d9-3dd2-a261-e56aa6210e0d | -7.87754 | -61.17533 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7573a14-a907-3adb-ba80-b34e640a2254 | -3.81153 | -58.88627 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c79ecc0-9e0a-3db8-9385-8a8fa4d28d31 | -10.29918 | -50.49991 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8da0b66-1afc-35f2-9da3-577f6db8dc32 | -7.83662 | -63.41529 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9e97a631-4588-31ee-ba79-ae7704f03688 | -5.37125 | -56.05626 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 808db7f0-2270-3c45-93c0-4dcd2f763a39 | -5.89325 | -52.04504 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91210a5b-438b-3b40-b611-943638c36b13 | -2.92336 | -57.77875 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f2e8a43-ef41-31ff-a78d-5ff126bbeecd | -3.77951 | -60.75156 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddb29708-a55c-3ae4-b7aa-5a3d9d8716dd | -3.07566 | -54.39315 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72672e0e-a961-315b-95b8-22c1a72c38b1 | -3.29464 | -57.85815 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae402e50-7bd5-37a2-8194-8a2294d0fad1 | -3.92305 | -60.55474 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 015df43a-7570-3a81-87b7-d6b15169de56 | -9.0785 | -61.42589 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6d3458-63a4-3d71-963e-7de49b40ce82 | 1.90758 | -60.58265 | 2026-09-23 05:23:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49b4ded4-d10e-372b-9ce8-660916ea7e95 | -3.02957 | -59.16651 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db2f41b-dd9a-303a-b465-727d1106f7c7 | -9.09088 | -61.43548 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b348444d-885d-3e6e-9d78-d331791766fd | -3.15824 | -60.07825 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48998eb2-b5fa-3d45-bb67-089fd999461c | -10.30827 | -50.5088 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 21b0d596-e1f1-3a8d-9047-439007711f45 | -8.58619 | -53.11414 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee94972b-15cb-3bf0-973a-4b64fd72554c | -3.70993 | -61.00744 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a4d9467-ae6c-3ee7-830a-fc827bf7af16 | -5.81224 | -49.1546 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8c8ae5-b45f-39dd-b500-7ecf5aefac44 | -9.93193 | -48.46358 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 179d8a32-860d-36fa-8675-8b5bcafd4b1c | 1.17138 | -60.37234 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 491c3ac0-d19b-3646-8256-bbce728a70ee | -12.36707 | -50.15738 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f40d3678-4469-3202-9547-48d62710a480 | -6.18166 | -52.79469 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1897539-b10d-3798-9da2-4100078f42a1 | -5.85317 | -52.02937 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README114.md)
