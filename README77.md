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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbda52da-e674-34aa-8e7b-44f36e7d11f6 | -23.19168 | -50.34282 | 2025-09-06 04:42:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39818da9-bfaf-3b91-8d3e-ba3c893ac9a4 | -17.60496 | -50.55808 | 2025-09-06 04:42:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b99583a-5d22-3e5a-8af0-5cf037915fb0 | -19.97654 | -43.39391 | 2025-09-06 04:42:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27d8b0b7-e35d-33e4-9350-7cbd67956fff | -18.0858 | -45.80321 | 2025-09-06 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cc754f6-7d3a-35ea-9f5e-0b52f8b8f7e1 | -19.89985 | -57.92836 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0140fd45-7984-3e24-950b-a0d31687764e | -18.73188 | -46.88515 | 2025-09-06 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1baa0dd-a42f-33d6-82b2-fda052f05bdf | -19.17466 | -49.51691 | 2025-09-06 04:42:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2e0a51e-2681-39c1-adaf-c4327c5a863c | -22.24895 | -48.76458 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 4f6a2774-d1a8-3596-8002-6c9676aec717 | -22.27702 | -49.57052 | 2025-09-06 04:42:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3add43fd-58fe-3ac5-bd46-c3c4124eed4c | -20.5398 | -46.45969 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b494e84a-779f-304b-9ef8-786706fcc5b0 | -19.81176 | -57.9753 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8712cf16-05f4-394b-bbd5-ad5926fcc12b | -21.30291 | -48.55616 | 2025-09-06 04:42:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a75a18da-2b6f-3418-858d-fe011409d44f | -19.20708 | -42.87542 | 2025-09-06 04:42:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc2a56fd-f660-3984-b77d-6c3b548647f8 | -17.6044 | -50.56185 | 2025-09-06 04:42:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f77448d8-b8a2-3763-803a-eb7c63b536ec | -17.86777 | -51.7258 | 2025-09-06 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 987dd684-c1b8-3a65-b696-012fba7fcdc9 | -18.81102 | -53.26979 | 2025-09-06 04:42:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a27e631-ff37-3d2f-8f1f-4e24a92af3d6 | -18.14446 | -51.77924 | 2025-09-06 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f25ba946-8a0e-35af-a171-bdafcd689201 | -20.53445 | -46.46783 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03a1af35-c795-344d-9f1f-cf4b09ae4235 | -20.0974 | -43.81067 | 2025-09-06 04:42:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9bb9ec0-274a-319d-9123-c226b2d0dad1 | -22.24961 | -48.75961 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| fef2cc4b-db7b-3708-8ff5-2f0b76b48519 | -19.20668 | -42.87934 | 2025-09-06 04:42:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e4001cd-e5fa-399b-aa84-8c8463073aff | -23.42086 | -47.0449 | 2025-09-06 04:42:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a099b920-a39d-3799-8619-95393affeb70 | -20.53007 | -46.4678 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 392cfb16-cf26-343c-936b-47f1afcd7036 | -19.80798 | -57.95127 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2012c8cf-c87f-316a-9e19-153aa18d11b9 | -21.49017 | -46.19405 | 2025-09-06 04:42:00 | NOAA-20 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b960e59b-f572-342c-9cc3-1ea73aad524b | -23.19109 | -50.34714 | 2025-09-06 04:42:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b205f9db-8bed-334e-afac-8b912b922723 | -19.89253 | -57.92295 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 35261cb1-7a88-3e69-9784-de0095019672 | -18.11986 | -44.4594 | 2025-09-06 04:42:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f291d2f-c0ec-33ad-b2af-9f522181ea30 | -19.90054 | -57.92466 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 76a797e7-16ca-31d1-92e1-7c6fed5ce02f | -19.89653 | -57.92381 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 837f0250-c9db-3394-be89-348028694a4b | -23.33207 | -50.88387 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dc10b533-30d0-31b0-9343-4158ecb561fd | -19.46365 | -46.27466 | 2025-09-06 04:42:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c2e3fdc-6216-3488-adf1-9cdd3940a5b6 | -23.10277 | -49.84936 | 2025-09-06 04:42:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ff2f8f65-7213-3e75-b3c3-29448552a08e | -18.00315 | -49.26123 | 2025-09-06 04:42:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4cfcec4-d65d-3709-8faf-86ebe407d423 | -23.08987 | -47.05012 | 2025-09-06 04:42:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa835c2f-088c-3705-8954-23e422753b00 | -21.99969 | -49.91721 | 2025-09-06 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91d6a016-30fb-3d75-909f-2623fe16bec3 | -19.69389 | -47.96627 | 2025-09-06 04:42:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d57f66d-a84e-3f15-a93d-d58480187fa2 | -23.33266 | -50.87973 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d1b5334e-c43a-3c3b-b1d9-ae8193bf78f7 | -22.244 | -48.76116 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 58ce3bc5-0827-3453-8e3f-918cacebb27b | -20.53931 | -46.46379 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 352bdb7a-ced4-34ef-8ab5-901142afe0c6 | -23.33794 | -50.86775 | 2025-09-06 04:42:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97a9f320-4602-3bfb-8d1f-bfd8eff60f78 | -16.30462 | -58.11148 | 2025-09-06 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2434240c-6f5d-3d62-849c-3a6e0eef97e0 | -22.27026 | -49.56502 | 2025-09-06 04:42:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 49fcad98-a453-307a-9bf8-996b1b0dcd14 | -23.36574 | -47.17909 | 2025-09-06 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b379ce2e-3b83-3f49-841f-2ee9407d9a17 | -23.09038 | -47.04583 | 2025-09-06 04:42:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0252f41b-e5ce-3533-aff2-c0cd0366086c | -21.18383 | -50.27263 | 2025-09-06 04:42:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4c8b2af6-efef-3531-87b9-69ceee3abfbf | -19.40325 | -44.31299 | 2025-09-06 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4dffc722-ba8a-3dab-aca4-88539ae8a07c | -22.25159 | -48.74467 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b79154a4-5aeb-3456-945b-09681b8ffeb3 | -20.46656 | -48.7893 | 2025-09-06 04:42:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7a7c6e0e-8a3d-36d0-a0c0-c61569a08e79 | -22.65668 | -46.82972 | 2025-09-06 04:42:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6c19a838-063b-37b1-a8df-e073236650ca | -22.69841 | -46.31147 | 2025-09-06 04:42:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 814de9fd-9b69-3817-975d-59b42d44331c | -16.30542 | -58.10726 | 2025-09-06 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dc1a14a4-5771-3f19-a506-e103d396e299 | -23.32976 | -50.87495 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8a874359-0fc4-36bf-a353-fd8dd644aae6 | -19.93245 | -43.60702 | 2025-09-06 04:42:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e1833b25-66e1-36f1-af51-d8cc41557f0a | -24.51093 | -50.74779 | 2025-09-06 04:44:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d3a6a551-af63-34cf-87bf-073d1ec9b414 | -24.15069 | -49.51899 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2c44db8b-70a3-387a-9dbe-f0730af1dc87 | -24.14758 | -49.51341 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f938b80a-e707-30b4-aac8-437daef55006 | -24.51448 | -50.74839 | 2025-09-06 04:44:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc8c2cd0-ccf0-3ae3-9ade-834e00016706 | -24.14381 | -49.51293 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ebaeec77-8669-3b33-ba49-756aebff994b | -24.14691 | -49.5186 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ab2f726c-dc71-3c54-97e1-743333450677 | -24.14314 | -49.51805 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 808ca25b-a168-36db-a130-a1ba9e50e70a | -24.14825 | -49.5083 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3da66dd5-8b64-3a62-bff6-cb987315a740 | -24.14448 | -49.50778 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 967669ba-93d9-3dce-b5a5-e89faa727d63 | -24.15002 | -49.52411 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7ffd5a8d-19b2-3cd4-8e37-30e259b69262 | -24.14136 | -49.50223 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de5b3bdb-13a9-3a03-be33-53fe28259825 | -24.1407 | -49.50735 | 2025-09-06 04:44:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c53a958-98e0-3c50-8079-4de79498e496 | -13.0044 | -54.8282 | 2025-09-06 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0167e73f-e9a8-3b91-a7e5-59f2f4bd0816 | -14.18 | -53.0564 | 2025-09-06 05:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f84076f3-9c9e-3116-9dfa-16e06fcac8f3 | 4.39831 | -59.75941 | 2025-09-06 05:25:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da0f238b-05ff-30c5-9a08-f4c8a90e4db0 | -3.1658 | -49.48169 | 2025-09-06 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d379ddf4-2696-32fc-8e3d-7bad9423b4c9 | -2.8548 | -49.50717 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a4dddd2-260c-343a-b548-7a19bb7d9665 | -4.27373 | -48.18103 | 2025-09-06 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 33115abc-8965-34f2-8671-dbec210fde18 | -3.32892 | -54.90793 | 2025-09-06 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e5e5ef-9239-3df9-bf69-d1d62aed2856 | -2.8556 | -49.50184 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d597e3ba-e03d-3d22-ade2-edf1b4c50bb2 | -3.23869 | -50.80664 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4a287227-af1b-303b-a0fa-b2c8df79738f | -3.16097 | -48.60686 | 2025-09-06 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1eed1068-ec8d-3337-8bda-2c0eb0cacea8 | -3.69033 | -49.57061 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 425d1d79-42d5-3fc6-9fc4-8ca9278a07de | -3.16015 | -49.47507 | 2025-09-06 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86ba2a43-a2be-3536-8cd5-ae38681abcc2 | -3.25058 | -50.80837 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78204b8b-40d7-3acf-b735-2afdaa934863 | 0.94319 | -59.92885 | 2025-09-06 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21589814-f883-35b9-ad5a-2370476ad1f7 | -3.69745 | -49.57334 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d95fcf2-7277-3b4a-a430-a765a9e15369 | -3.1576 | -59.04702 | 2025-09-06 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0244d620-3492-3c34-b2d9-469907e12c4e | -2.67781 | -52.17139 | 2025-09-06 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e85ec30-fc86-3ce3-b7d0-c271f7cc7292 | -3.37954 | -50.84808 | 2025-09-06 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b01fc6-1b9c-39c6-8ea9-bf1b79083aef | -3.2459 | -50.79889 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9076b330-60d3-35a5-b0b4-94480eb0d791 | -3.37629 | -50.84616 | 2025-09-06 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1e0bedc-7138-3bf6-8984-07193b6e3546 | -3.25122 | -50.80405 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65530ada-b054-3b06-b064-c359e3e61706 | -3.24527 | -50.80317 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28cae78a-9e29-369e-823f-142052b5fd61 | -3.38015 | -50.84378 | 2025-09-06 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 769f1143-7957-341a-85bb-1f7a59eae819 | -3.69098 | -49.57244 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8754c1b8-62df-3328-aebe-82d68013de66 | -1.34542 | -55.47136 | 2025-09-06 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a625dc4a-7558-385e-b67b-486ebca86bc1 | 0.75581 | -60.45152 | 2025-09-06 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57b75662-1ae8-38c9-b3ce-0f159fd2c4be | -2.5565 | -48.39243 | 2025-09-06 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 296a16d6-0be0-3320-a507-571abd1aa891 | -3.69679 | -49.57153 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3deb4578-99cd-38c1-b82f-401176a10a3c | -3.37564 | -50.85052 | 2025-09-06 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e9ae724-d711-3fc5-81d9-a2e0cff0ad4a | -3.69475 | -49.54556 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d89e5ff-c86c-39d5-bf75-191fa8739e40 | -3.31612 | -48.71244 | 2025-09-06 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92b9556e-2141-3b56-902d-4613ddb6e376 | -3.69427 | -49.54385 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17448df4-de71-3e8b-8f87-21521cd0275e | -3.24464 | -50.80746 | 2025-09-06 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 14db2532-f6d3-3021-964e-9ea18a3d10fa | -3.15936 | -49.48066 | 2025-09-06 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README78.md)
