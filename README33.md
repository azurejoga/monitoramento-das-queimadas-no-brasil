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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d626ffc5-33ec-3485-b34a-248c977d78fd | -17.60398 | -46.6824 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ace7c83-8f88-3207-9d52-d97cada1f08e | -14.05477 | -46.29068 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c076c3bf-b27f-304e-9ab2-a58afc121a56 | -16.30408 | -52.92611 | 2025-08-16 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3262187-df8d-3bf5-8794-1ba9a8473d8b | -14.94058 | -54.75777 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3c01a38f-8994-31f0-84f5-18326566ef6f | -13.00113 | -56.8717 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be0aa443-9b0f-3c32-ba5d-6afeccc3d566 | -17.25152 | -42.70783 | 2025-08-16 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbaecf05-213d-3fa9-a74b-997827759c7e | -14.5792 | -47.91291 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a44a44f-9b90-3739-a2c9-53d2daee5d03 | -14.60687 | -47.9391 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e17faff-29f0-33a6-8188-fe25f6acae9f | -14.58406 | -47.90826 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a76d945f-09e7-3788-b122-0d8fd756cdf8 | -18.86919 | -46.8963 | 2025-08-16 04:12:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7cc1b9c-a473-3f1e-90d0-20b589d4ed74 | -14.96422 | -54.73869 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 689367b2-4483-3628-bcb5-1cae5f6772c3 | -13.11701 | -57.13887 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54d542cc-5a1b-349f-9d5b-c0a8325d4ddd | -13.99428 | -49.64095 | 2025-08-16 04:12:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb3f90e6-07ed-32ba-80a4-0c9b17598fb7 | -17.88574 | -39.76524 | 2025-08-16 04:12:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 12e4b079-8ba0-3bc0-937d-cd1ea3955526 | -14.97353 | -54.72424 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56120b70-f0e8-3e34-b805-0139df9b181e | -16.23595 | -51.12758 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acfadc55-4f93-30d9-8613-dedeb1742405 | -12.99957 | -56.87883 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 352fbb1a-9ef1-3f15-8e37-3e66202406dc | -17.6075 | -46.68306 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 987f5e3a-8251-38b2-bc3a-d12821067c7a | -13.12479 | -57.17184 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed1e156c-b79a-3c33-be2c-5bc849f10ad3 | -17.61032 | -46.68783 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b37541a4-b15e-3f39-ae7d-51bbd581ef67 | -14.95136 | -54.73584 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef1906b6-4a14-3d30-a518-2e6e7b2bd487 | -14.96654 | -54.72768 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf19af70-92e3-3719-9617-633463b7d39b | -14.52761 | -48.59574 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0bb1e377-ecfb-33ef-a8c0-2134aef1edb9 | -15.62187 | -47.85199 | 2025-08-16 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82be17df-64a0-3b72-b9cf-b4380d43f67b | -14.59999 | -47.9323 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e35364-1614-3e11-8455-e3edd5edaaaf | -14.94546 | -54.7037 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8ecedb9f-bed7-33c5-a48d-96f92111539d | -13.44531 | -56.6668 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd8f15ff-2ec3-3796-a05e-94a87ee70b52 | -14.94651 | -54.75941 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35dd2afb-0c8f-319c-80b4-90f577b5b6ef | -20.04593 | -44.63945 | 2025-08-16 04:12:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76aba786-6261-3b76-a952-1491d58bc285 | -18.15416 | -42.77548 | 2025-08-16 04:12:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22da6304-5558-3fee-83da-07d4c321a3e6 | -13.13344 | -57.16618 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f890927e-7483-39af-bc2f-5830035f97b7 | -14.53169 | -48.59645 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e461efa-a88e-3bd4-a27a-e83fd4a53e78 | -17.61807 | -46.70625 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bed0b149-864b-31de-8c83-4446cb5a348a | -13.4449 | -56.67461 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a88086-3eac-3327-9852-88b70e393106 | -19.92179 | -44.13859 | 2025-08-16 04:12:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7d6d3ad7-dbe7-3075-8c09-9fb57ee69769 | -14.21308 | -44.77806 | 2025-08-16 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a826219-6aa8-3540-8498-91a4538b2924 | -16.23797 | -51.11725 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38348ffb-7b18-3af5-a70e-ac0eeebea672 | -14.04998 | -46.29147 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e8bf850-099e-3908-a20d-f04eb03a1265 | -14.28261 | -43.28437 | 2025-08-16 04:12:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 689f206f-87d2-3cb6-ad8c-87e12563322a | -14.95391 | -54.75774 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a602f1-e5d1-3c4c-8f92-208e7a16a086 | -19.81237 | -42.09908 | 2025-08-16 04:12:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9760e7f6-a115-33ed-9794-6b14f597b20b | -17.61102 | -46.68372 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| faf5a4d6-387e-36eb-8296-701f6085d499 | -18.95112 | -41.00887 | 2025-08-16 04:12:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8f1518ee-46ef-39bc-a53e-d4167d21a50d | -16.7537 | -45.06206 | 2025-08-16 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6beca1a-9cd3-3482-ad9a-71cae55edcc6 | -18.72587 | -39.81837 | 2025-08-16 04:12:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 632987f8-92d2-372d-b25c-2a68158dfbb4 | -14.48161 | -47.71763 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41e2949f-48cb-3ed8-9d83-02455e33aee6 | -19.93596 | -41.23988 | 2025-08-16 04:12:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53a1694e-0bd1-318c-9b0f-f7b966cd188e | -13.11858 | -57.13156 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 985199b8-6116-3d13-8c6c-aa74276b730c | -14.16009 | -45.35159 | 2025-08-16 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2399bc9e-c2cc-3303-a79c-278e9b0f0aa5 | -12.99695 | -56.87246 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80ead719-e328-39f9-bbee-6177963c33f9 | -19.92512 | -44.13916 | 2025-08-16 04:12:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c8f8932b-8ee7-35ba-a0ac-05ec4d451f04 | -17.3352 | -46.56464 | 2025-08-16 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f68b723-e7f6-31b6-812c-b6f41bf68421 | -16.24526 | -51.12952 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26b00084-7181-331b-b373-654078fb09ce | -14.59517 | -47.93671 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3be1058b-bd2e-3181-91c5-8f4b8af593da | -14.93125 | -54.71202 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 18ae6179-6fec-3501-94ed-60f32f1f7c03 | -14.59126 | -47.93597 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f3a6af-773e-303f-b9e6-a12954618c7a | -13.4463 | -56.66806 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06e4ad56-79d3-3d10-bf85-db79e4d1a218 | -13.44245 | -56.67979 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be09b8c7-2cb4-38fd-af1f-d1f681b18bbd | -15.62606 | -49.27204 | 2025-08-16 04:12:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48c40da3-7253-3d50-aab2-a19abe5f3dbb | -14.6183 | -47.91999 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c11dc09-7674-3dac-8407-7298f6e8b61f | -13.441 | -56.68639 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58f59f3-323b-3221-af3e-f1249b849924 | -18.04266 | -47.72455 | 2025-08-16 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 78f77d00-f5e3-318c-9cab-ade199b014bd | -14.94662 | -54.69804 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5e289be9-eecf-3231-a7e5-42efdfd8ceb2 | -14.52828 | -48.59204 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ffbae2a-d09b-38e5-899e-f12a67359873 | -14.04566 | -46.29509 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cb8af5a-c03d-3e87-9ea3-c89038102fae | -17.28322 | -44.87659 | 2025-08-16 04:12:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0de332e0-abb8-367a-97b2-14dca08f59a5 | -13.43555 | -56.67836 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca166e2b-2f2d-33e6-b10e-7989ef4cd9b9 | -15.60746 | -42.33018 | 2025-08-16 04:12:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29f8be8e-5238-3804-aedb-a8bc25fc9033 | -13.14051 | -57.1679 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e150bf-9283-3423-a96b-950a99df7c8c | -20.29621 | -41.34601 | 2025-08-16 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79666b96-d453-3b64-9a23-26eaceed82ec | -14.07133 | -46.32394 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3529dd6-f38d-30ae-8a9b-1cfca9bf039f | -14.9519 | -54.73768 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b6af7ff-f466-3251-862f-f6f408e8e28d | -18.87147 | -40.14337 | 2025-08-16 04:12:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b795c41a-2e42-3e8f-8e72-5e9cb900b569 | -20.00495 | -46.43341 | 2025-08-16 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90342714-e869-3c5c-83fa-7c14d51b97bf | -15.02466 | -41.19797 | 2025-08-16 04:12:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0bd57e23-45d3-3f7a-bdef-7862767ac5b3 | -17.21219 | -49.58856 | 2025-08-16 04:12:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d98ec63f-641d-314b-8963-778a9e48fe52 | -13.44352 | -56.6811 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc441edd-47b1-34f0-a794-b9a5e6be2e2a | -17.73198 | -43.52326 | 2025-08-16 04:12:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8d3b2b6-c3ad-3bf8-9362-594490d0d8ea | -17.78837 | -48.61637 | 2025-08-16 04:12:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f06d63ef-8d4e-38cd-916a-7cec02cd8865 | -17.37559 | -48.15961 | 2025-08-16 04:12:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bacc907-345c-3e70-ac36-49f79a1ef7cb | -15.50675 | -40.75436 | 2025-08-16 04:12:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| afe68156-f46d-3bf3-9d2d-1bc326334e00 | -20.00903 | -46.43014 | 2025-08-16 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1815abdb-906e-38f1-80c9-956ce8ba3424 | -18.50939 | -43.6486 | 2025-08-16 04:12:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c9fe2c9-5287-33cf-a119-a2ca87061000 | -15.90078 | -41.60604 | 2025-08-16 04:12:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b0f94208-e683-3d03-abaa-879713d2f977 | -15.62264 | -49.26716 | 2025-08-16 04:12:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb00944f-fccf-3dad-a71b-cbc2e6d825c2 | -13.00805 | -56.87359 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 219e535b-72c2-37e2-abd9-10099bde73b0 | -15.90022 | -41.60985 | 2025-08-16 04:12:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34f0d2f4-ce91-3f18-8c93-c4e2329c7cf1 | -18.2264 | -45.22267 | 2025-08-16 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 741129a8-9811-3cbf-ad37-74b8d9e534e4 | -19.29752 | -46.21054 | 2025-08-16 04:12:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c618e32-a83e-34d2-aa27-bc597fd34da0 | -14.9485 | -54.69488 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11b0025b-73ea-327b-b523-d3e620f4c32b | -13.44387 | -56.67334 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb7ec1a8-ec11-3fa7-aea7-3feb609c79fe | -17.61455 | -46.7056 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5200bf97-4dc9-31e4-8b25-ca8379d5bcea | -19.93534 | -41.2444 | 2025-08-16 04:12:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fc0c2cb0-2984-3696-b7d8-a0d0b44199a4 | -14.9389 | -54.71054 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f4b35907-750b-3e67-ac65-565746ee5b73 | -19.17964 | -46.26519 | 2025-08-16 04:12:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ba1057f-2048-3142-a077-a8dbc844b868 | -19.30093 | -46.21113 | 2025-08-16 04:12:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bebe0c83-81c2-340a-92f4-b6915cbb030f | -14.95095 | -54.74214 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40a60d95-470c-3c10-8e9a-e2f153fd0ed2 | -14.93189 | -54.71405 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 111e4ba7-1049-38fe-b377-717a53b52b11 | -19.91649 | -44.70701 | 2025-08-16 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f5dece8-70fa-329e-9f2c-63541ad870b7 | -14.60592 | -47.94451 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README34.md)
