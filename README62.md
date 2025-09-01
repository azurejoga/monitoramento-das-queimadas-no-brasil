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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9277fcc8-f233-345d-a4e7-62d943f1cc65 | -15.54713 | -51.72179 | 2025-09-01 04:34:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2155698-6b48-3d2c-924d-6829c2f30d13 | -14.03328 | -44.47567 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff9ec9d1-87f1-349a-8704-ca932a2cc562 | -11.04422 | -47.00073 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3e5bef-cb44-3c88-a732-aa50feb2ccd2 | -11.0746 | -52.06349 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ed241b9-a080-39e9-9dc6-ffa04c097178 | -11.01782 | -46.84954 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0601f090-93b9-3aa2-a8fc-9df7ea77687c | -15.32769 | -46.09777 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 31e0dc86-4781-3956-abe5-bcddfc028910 | -11.04536 | -46.99321 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 881b9f3a-c39e-3ea5-a045-8a885faf7951 | -13.52229 | -46.98362 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba2f7da7-6162-3ea0-b698-8468bde44e6c | -11.03223 | -47.05651 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8ac81a7-9d01-34a3-b9cd-ad540b7a9bbc | -12.97535 | -48.1152 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 842e366e-210d-3509-bcdc-cc59507d5452 | -12.39119 | -46.47743 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 122b6fd0-37c5-3956-914f-3e70fd386530 | -15.72961 | -48.96045 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e33a2276-fdf2-380b-84d1-739139709e4f | -8.74279 | -62.40509 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fc254b3-5cfd-3169-8cf9-7659af5a1c25 | -11.87661 | -46.73743 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 415fe61e-acad-3180-a14b-a940e4f3eb08 | -15.71568 | -49.0067 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31227f16-ad5e-312b-b7dd-0d75aa8f49d6 | -12.30575 | -45.68097 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| caba9b05-d126-3ff1-889c-1fd18ec042c5 | -13.51008 | -46.9935 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24b9291d-0509-342c-b487-152d1919447c | -12.30943 | -45.68153 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc04841c-684f-312e-a79e-c4d161de2d7d | -13.29274 | -46.9009 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdbaa704-8446-3fdd-bfed-938abca426f8 | -13.50658 | -46.99297 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46647b26-e23d-3666-8e73-d4600710cdca | -11.68363 | -47.58312 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1b159ba-647b-3b95-88e6-46a9b8de6820 | -16.97169 | -49.30928 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 579c0f5a-8e7c-3776-9fbf-4ef9ca08f90d | -12.41301 | -47.78166 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e07137-ec0d-3f3d-9822-dab97317c99c | -15.72347 | -49.00059 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6b16891c-81d8-3f62-9ab8-d16fd9184ec5 | -12.91488 | -56.98817 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae348d04-4773-3506-9009-613d6a64e8e1 | -12.90821 | -56.99767 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f282c3c8-161a-3bec-b50d-85b18f6b360b | -14.60603 | -48.68063 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76e7af55-0bd7-39bf-92b1-04f129880bbe | -10.28139 | -54.25432 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65641745-813d-3ef0-9463-cc668f24e7bd | -14.04441 | -44.57704 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 493ff52f-b385-3577-ba6d-62ad4ed11a69 | -14.8483 | -47.09864 | 2025-09-01 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d1ef738-bbbb-3211-b3f2-3855f91ffa8c | -13.49773 | -46.98006 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a2b0890-a735-3cac-bf29-865f36b99f25 | -10.88107 | -55.75389 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca463583-5a18-39d7-bc3a-4ff7c2a98263 | -11.95434 | -45.83886 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a07be4f1-d82a-317c-babd-6a8a8354b880 | -13.16889 | -45.28612 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fb23c9bd-ae87-3922-b868-667b7b6d09c0 | -12.86655 | -48.1619 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23b018c0-e7c7-3b71-b4d9-72aa952ac889 | -12.9647 | -48.11729 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a652eef-4cb8-3668-8439-4a43b83ae760 | -15.59218 | -48.32147 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc732696-e64e-369c-bea5-297bc7cd2a36 | -11.68587 | -47.56842 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e383633-7010-3df2-9276-53ad790a5ab8 | -12.56676 | -48.21857 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 380d6634-d1df-3e2c-9ea1-8c398201c3ca | -11.68925 | -47.56895 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 489cd50f-4f29-3096-8216-84acfa0f13f3 | -11.04825 | -46.90466 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f9c5eff-8a9d-3ffa-8708-efd955b4b1c1 | -14.74256 | -46.73335 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1925f857-bfed-3096-8c9c-39db3e489033 | -11.80345 | -46.42286 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9546a33d-37d8-3503-bd9e-6fba14d52cd0 | -15.69722 | -48.90284 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 42f294af-ac46-39fe-865f-785e95aa0255 | -15.70334 | -48.90779 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 51cbf9d1-a222-3f80-807b-d8e688ad417a | -15.59274 | -48.31774 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc156feb-4944-3294-b598-44188faca868 | -18.49984 | -46.99544 | 2025-09-01 04:34:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e59e56-fea2-387a-b188-e47cd8ddaf9e | -14.74603 | -46.76009 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c5ecb7-5db7-3503-b1a1-fb3ef2ecc952 | -13.68296 | -46.92381 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 496812ea-cb03-326a-bf62-c098f22507de | -12.60355 | -48.18012 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8abbc21b-fd0c-3710-acb2-493e1ee2d251 | -13.16509 | -45.28554 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 743d566e-257a-3a16-8996-afddf50002c2 | -15.72565 | -48.89648 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a10c119f-5869-3d78-adcb-a927ff6e02ce | -13.48293 | -46.93413 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdd00365-3f9d-31a2-9cb0-1e9bde2b601f | -13.69346 | -46.92581 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd8f9334-3644-3bba-9ad5-c5da26cf6a6c | -11.48647 | -46.80474 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b25b030f-97f6-353c-bbf9-33dd27ea7fd6 | -10.7235 | -49.58017 | 2025-09-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc517a87-0421-3215-bf42-bff2e02a78ee | -14.0465 | -44.59197 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46eeb427-ba28-31ae-94fc-eb84ed786974 | -11.47725 | -46.79531 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6ac5e15-01f1-3732-88be-aaca844d2ad5 | -13.70802 | -46.92468 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f7d0bf6-04ba-324e-8d61-51b65f5c582b | -12.56342 | -48.21803 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e93c016d-6bac-335a-b9fc-7e9c48c6a212 | -11.44898 | -46.81854 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 627c89a9-20b4-3f4a-a32b-82b859822b81 | -11.37992 | -43.63178 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df370530-0916-3b45-a5f9-47ec1dfd98c6 | -13.52174 | -46.98734 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6eff6420-8068-35f6-a787-c30949e3d131 | -15.5431 | -51.72497 | 2025-09-01 04:34:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 979e0126-635f-3b3a-b99b-2c54746930f4 | -15.7129 | -49.0025 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f541bc86-d94d-3a4b-9dec-2c5f1257ee7a | -14.78547 | -46.74089 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55c7f6f8-49ef-3a03-8d42-3b5e421525ce | -14.8223 | -46.72626 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a90fbc0-4297-3c39-80dd-da676a4311fe | -15.72291 | -49.00422 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f0860f90-b4a3-3508-baaf-d59a1f00058b | -8.73294 | -62.41764 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95097ef6-62f5-3e2e-ac34-eeaad2ba1147 | -11.65218 | -57.35756 | 2025-09-01 04:34:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 861f6127-2755-389b-b660-2d688e4746e8 | -10.36995 | -52.28355 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e64c9b3-74fd-3ea5-8795-b9ac556a1368 | -11.3748 | -43.57711 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e50935e-2b76-3c44-9b2b-2801d0ddc4cf | -13.48146 | -46.99325 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5689864-0d65-3631-8f00-0907bd76e36a | -13.65305 | -46.92971 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed5f8a49-5751-38db-aa4e-98af1913fcd3 | -14.49062 | -52.98396 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f59cb0d3-47ea-372f-ba77-38c0b142a3e1 | -13.516 | -46.83055 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 566a332c-a675-36b3-89df-690c7f2684dc | -12.85009 | -48.07804 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ecf0f7f-5f68-304d-8c29-97fe5dd95c17 | -14.77829 | -46.76497 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae021b36-f4fe-389f-b868-62eb3d8e2abe | -11.42433 | -46.91297 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ab31ae1-876d-3a60-9dd9-e82ad3edc003 | -17.15671 | -46.08705 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b4a626-eedd-328e-934f-1daa643a1b58 | -15.7741 | -47.80196 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 76661180-6896-3e9e-ab7a-d7c55ebf91a7 | -15.6911 | -48.94313 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e954beae-9fba-3408-abb5-e3695f4a246c | -10.72739 | -49.57718 | 2025-09-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ea5cf33-7248-3358-9202-7ee2bdd96bde | -11.59128 | -55.55175 | 2025-09-01 04:34:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97333f7c-ba90-3b75-8dda-0c8e77a29c7b | -12.02106 | -49.70913 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d905ab-8480-3113-86ee-8400af1045a6 | -12.56787 | -48.21136 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 281925d0-fc5d-3d74-8430-c33c8541fc6d | -11.08733 | -52.03157 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb131496-1822-3a05-93ee-ca885c9dac36 | -14.02923 | -44.47511 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d0a8236-8f55-35f6-a696-a5c0be8e292a | -11.89407 | -46.73996 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2de97eaa-cb4d-368b-920e-52ba9bca3060 | -13.34236 | -46.95332 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6671fc8-fbfa-3bac-aa57-1a467cb4aa84 | -14.78189 | -46.7654 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb15292-5b33-37e9-9c89-6159f957b235 | -15.69994 | -52.74786 | 2025-09-01 04:34:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a77201e6-5e2c-32cc-8d9b-9557f6124af6 | -15.68666 | -48.94976 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1a92edb-f877-330e-ba20-43c57dad885a | -14.98431 | -46.71053 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1fc25ea-10a7-367a-9645-0813e8abc28e | -16.0768 | -43.62223 | 2025-09-01 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e95bab57-d0ed-36ce-99f1-980654f408d5 | -13.30795 | -46.89508 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 028ad39b-f30f-3bfb-a0ec-3baa6f4dd03f | -15.73017 | -48.9568 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e0a9b13-af04-3f0e-b9f2-b094e0036dfe | -12.06423 | -46.66015 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93c013fb-9473-345f-a6a4-210cc5404e37 | -16.96946 | -49.30146 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eda3e525-f072-3efa-9050-73ea15f05b79 | -12.57512 | -48.20881 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |


[Clique aqui para ver as próximas entradas](README63.md)
