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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f26bf2c3-d5de-3de7-a98f-4d1eadabfddf | -18.33627 | -52.97146 | 2025-12-01 04:08:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f559e6a-42fd-3a6e-98ad-a128f4225749 | -17.75283 | -47.29354 | 2025-12-01 04:08:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 474790e6-9011-39fd-a833-9a5d3a447a55 | -13.94174 | -44.34896 | 2025-12-01 04:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce87c892-e94f-3202-b142-72b1e056dd18 | -13.60964 | -43.97934 | 2025-12-01 04:08:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21d002b6-8b0c-385f-a0b3-7c7843886f2f | -16.96851 | -48.20137 | 2025-12-01 04:08:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa5a3092-2796-30d1-9676-0af7a16aa32c | -16.46937 | -46.42448 | 2025-12-01 04:08:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19030a2c-5ce4-31c4-bc90-97b4a86a3e6c | -13.72594 | -48.7369 | 2025-12-01 04:08:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e2529de-2121-3d0f-9d79-5bd040364a2b | -19.82852 | -42.4565 | 2025-12-01 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 655bfc56-ba36-3d55-abbc-261e7a67c235 | -14.19432 | -44.45942 | 2025-12-01 04:08:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3b31de3-46bc-3cec-ad52-a960d164be3d | -13.4866 | -46.71084 | 2025-12-01 04:08:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83b4981f-94f0-3596-ace8-874b900fd2f0 | -16.49301 | -40.80094 | 2025-12-01 04:08:00 | NPP-375D | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7eb59227-bf35-30f9-bcfe-953fe45d32e9 | -14.42815 | -44.84492 | 2025-12-01 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cd22aa9-1f0c-3765-8d2a-9b14cfe1ebed | -12.01754 | -49.26649 | 2025-12-01 04:08:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b9881fe-0254-36b1-b6d0-92557c82bc0c | -12.92175 | -41.14594 | 2025-12-01 04:08:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18dffd50-d658-33cb-9907-506dda1e8ecc | -15.65348 | -43.57368 | 2025-12-01 04:08:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb5f59e-590c-3e79-9850-da770a0a1bbd | -13.94105 | -44.35299 | 2025-12-01 04:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35aef8f1-c300-3992-b861-df4fd4000e04 | -19.83186 | -42.45707 | 2025-12-01 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3a6ef36f-5f8c-389e-a60a-88c17595e84e | -19.83243 | -42.45338 | 2025-12-01 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 319abf16-c1d0-374f-84a2-e14c551529d1 | -14.42888 | -44.8407 | 2025-12-01 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b96c0318-30c4-3526-b806-785d6cc3c0df | -13.47288 | -44.54929 | 2025-12-01 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe755794-d23b-3c2c-b302-776efee5b4b1 | -3.6009 | -47.2521 | 2025-12-01 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| dd0a8a09-5cd8-3c5c-9d55-e8e09df1aa05 | -4.4064 | -43.3351 | 2025-12-01 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1c3ea0d7-ecf9-3f52-9469-e61dfffa9247 | -4.3879 | -43.3129 | 2025-12-01 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 35f7c91b-23d5-3d42-bacf-d89cb0fb2284 | -4.3877 | -43.3362 | 2025-12-01 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8c8cd22d-3280-3bed-b8cd-416fc8023863 | -4.3703 | -43.1508 | 2025-12-01 04:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e42c3b7f-27b3-3b5d-81d3-d7b04e111aab | -3.6008 | -47.2739 | 2025-12-01 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 085bbf21-4200-3b26-990f-874bda797a61 | -5.3211 | -43.5549 | 2025-12-01 04:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c6d18a6a-810a-3555-a22e-0514c29f8089 | -5.3209 | -43.5781 | 2025-12-01 04:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 09d8f465-c026-3a9d-8d99-0593a1a1f7a9 | -21.0598 | -47.11428 | 2025-12-01 04:10:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5701235c-535e-37c1-a357-7cb38cbb84b6 | -20.02232 | -57.44207 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8e789e31-5c30-3ffb-a688-6bf026e8b992 | -20.02468 | -57.43732 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 8237d1c2-23a1-348e-b704-327cbff157eb | -20.02745 | -57.45071 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f6ab66ce-519e-3f11-bc8b-d7cf7f155b0f | -20.01952 | -57.42865 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| ef3d1795-3c6d-3474-852b-f5f2db2cb3a4 | -23.18301 | -45.66437 | 2025-12-01 04:10:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86dd1068-d06d-39c4-94b1-4061222941f7 | -23.12036 | -45.29002 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c306f7ee-ef49-3f62-be44-f81750b16178 | -22.52494 | -46.92625 | 2025-12-01 04:10:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b752f8db-6e15-30dd-8d75-4d03d473f931 | -20.02304 | -57.44406 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| e911f03c-3e31-321e-a68e-ce49bf605fd9 | -20.92348 | -46.79523 | 2025-12-01 04:10:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ec072f0-a8a7-3f35-adc2-a689eaf37c1d | -20.02577 | -57.45746 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8faa21bf-9b7e-3701-92b1-dffa3242a315 | -21.99054 | -41.11254 | 2025-12-01 04:10:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 881fadd8-8b94-3373-b753-fab09f4cc4b6 | -20.01788 | -57.43539 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 33989332-0f05-36c4-a4a3-94eb52042138 | -21.76241 | -44.29975 | 2025-12-01 04:10:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d0f6324-4449-32ed-8baf-826b8008c86a | -23.11764 | -45.28549 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 02d2a1a0-78b8-3b3b-b85d-38000f18ff1e | -22.72767 | -47.36283 | 2025-12-01 04:10:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7f316676-c519-3d86-9dd5-312dc47aee9a | -23.12101 | -45.28615 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 646119fd-b640-38f6-9692-811d75259925 | -24.11953 | -50.1451 | 2025-12-01 04:10:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a7f2159e-ebcb-35b1-a525-d86c139948d9 | -24.12284 | -50.15018 | 2025-12-01 04:10:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be2878b9-a020-3970-8657-578453c3a945 | -21.83863 | -44.55687 | 2025-12-01 04:10:00 | NPP-375D | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 77357132-53ba-3de0-9135-58f3d5bac87f | -23.12709 | -45.29135 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 00fa40e4-da4e-362d-874c-706e2470f6f0 | -20.0214 | -57.45083 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a68ed0fa-5dff-3fd8-a856-a60a43c2f05e | -22.19359 | -43.33741 | 2025-12-01 04:10:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 610f59d4-10aa-3f98-8a92-b0a697834933 | -21.54779 | -48.89464 | 2025-12-01 04:10:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb5990a9-5527-3ba3-8744-e78516352128 | -19.97682 | -57.39508 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 725e344c-b27d-3b87-a2c0-e01ddaf780f4 | -21.53083 | -49.52952 | 2025-12-01 04:10:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b40e24e-d110-3c62-852e-1164d9d67abc | -20.368 | -45.3003 | 2025-12-01 04:10:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 820747fb-ba3d-3601-adb9-e92ddfedea12 | -19.97166 | -57.38649 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| abc71343-ba43-3f7d-99a4-47dec532cc08 | -21.5518 | -48.89556 | 2025-12-01 04:10:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d94732-9dd3-3a2b-ad22-bdc330c9fb87 | -23.12373 | -45.29068 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 898d8c76-62b6-3d36-892c-0740c432c881 | -19.799 | -47.80687 | 2025-12-01 04:10:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| afb6886c-f8eb-36dc-b6b6-a04db8d6bd42 | -21.95614 | -44.87985 | 2025-12-01 04:10:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fee4fc75-002e-3276-8ed8-7556483a9913 | -23.81425 | -50.36277 | 2025-12-01 04:10:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fff331cb-4c33-3f67-9092-80cc8f9a20bf | -21.535 | -49.53045 | 2025-12-01 04:10:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a3e3c893-11f6-3171-96be-2b96fc41fada | -23.11699 | -45.28936 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b44a058-a516-323d-9b2b-e60156e0140b | -19.97126 | -57.38968 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bcbb8161-5994-3f79-9eee-951ed6390b99 | -23.13046 | -45.29202 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34e917ed-ca13-3891-994e-7129459fed09 | -20.02064 | -57.4488 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 154a9218-5b1f-37d6-b205-a47ae0694305 | -20.91989 | -46.79436 | 2025-12-01 04:10:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 389f5c73-c5a9-3741-aa39-348de4db9561 | -20.024 | -57.43536 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 9a82db71-5133-3b65-93b8-c1c7b5339e4f | -20.02986 | -57.446 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 83438d6b-5588-3104-b90e-88db9cee8cfb | -21.02601 | -48.41266 | 2025-12-01 04:10:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59dd82cf-5915-396a-8bcc-ff166f665141 | -22.72848 | -47.35829 | 2025-12-01 04:10:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| cf8b00d5-046c-30c4-9a1a-39fcfca81fa4 | -20.59365 | -44.28131 | 2025-12-01 04:10:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d47bd207-ca76-378d-ba95-173e43542c78 | -23.12774 | -45.28747 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3b0e3124-2510-31f5-bf09-9ff8071d0fde | -21.84246 | -44.59643 | 2025-12-01 04:10:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0918d7b-a836-3858-80a6-2f43ddc03a70 | -19.97806 | -57.39159 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ed99bf23-3d99-3600-9368-3f52e359c771 | -20.02914 | -57.44397 | 2025-12-01 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fab3d88f-a85e-3f59-9379-d2692c4a2a2a | -23.12437 | -45.2868 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ecb682cb-f904-3b70-956e-c52af51a0de0 | -21.98067 | -44.52042 | 2025-12-01 04:10:00 | NPP-375D | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fa111eba-7644-3279-9637-9c017de2260b | -23.12644 | -45.29523 | 2025-12-01 04:10:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 15e97985-9761-3796-8e29-90bf47420888 | -20.37143 | -45.30093 | 2025-12-01 04:10:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 712db85e-a0e6-3a00-82d9-15e2fe740fd8 | -4.3703 | -43.1508 | 2025-12-01 04:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 18405fe2-5334-374e-a2bf-bced59445869 | -5.3398 | -43.5535 | 2025-12-01 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a25c9cd5-d987-33a9-84e3-0bbae0ea2d8c | -4.3877 | -43.3362 | 2025-12-01 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 296aa349-5e9d-3bf4-9769-862be66b83ea | -4.4064 | -43.3351 | 2025-12-01 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 8c38df2c-a092-3a41-b521-d96a8a830208 | -10.145 | -36.1406 | 2025-12-01 04:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| f42ff651-8b42-3e14-9f7f-65e41641208e | -4.3879 | -43.3129 | 2025-12-01 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1fcac57a-9348-3c62-8791-8617c9e81eaf | 2.00426 | -55.72826 | 2025-12-01 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed29184a-38d3-3b86-b230-49cbf672e17f | 2.01108 | -55.73192 | 2025-12-01 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 185014a8-4306-392a-988f-d3cca84d275e | 2.01103 | -55.72877 | 2025-12-01 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 562aa11d-aeae-3913-9361-d6051893fbe3 | 2.00417 | -55.72509 | 2025-12-01 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c67d90b8-5c53-32ea-be8e-62aa6db35b27 | 3.35789 | -51.30585 | 2025-12-01 04:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00528ef7-0c9f-35f1-8187-930cce34e408 | 3.35323 | -51.30656 | 2025-12-01 04:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3f57175-ac83-30ad-83c5-ac8525711e0a | 2.01038 | -55.72715 | 2025-12-01 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8eebea-6e5a-3c21-91a4-06e36cdc4ad9 | -2.93921 | -53.28636 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25d2aa84-1cbc-3b52-8a40-de656a329893 | -4.96793 | -45.82106 | 2025-12-01 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c0489f-4b72-3417-9a56-3dcd730330be | -3.40747 | -52.83298 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c41b143-c1c1-31aa-9488-d84e85e0284f | -3.61144 | -50.36757 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94efcdb5-2532-3010-8941-4a0b5e491a4a | -2.04213 | -46.67956 | 2025-12-01 04:25:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4fa367bc-9cb0-31af-8c7b-2c0560440142 | -3.7077 | -45.9039 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 431338bf-cfbe-3dd2-b847-2700ba089e50 | -4.21917 | -45.5261 | 2025-12-01 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
