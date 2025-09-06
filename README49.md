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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1484fe17-ebbe-301f-bdc8-169f94a59de2 | -11.01457 | -45.95713 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 687961c1-f363-381e-a247-77da3ecb9688 | -20.36031 | -47.78477 | 2025-09-06 04:19:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc89a527-3d26-3ab7-837f-dd5185370ded | -18.12255 | -44.45792 | 2025-09-06 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7871b79-724c-3709-8512-dd37e8f6fe00 | -22.84693 | -49.17543 | 2025-09-06 04:19:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ac96837-fd7f-32e7-9359-ec3605234240 | -19.90019 | -57.92387 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9042389c-f39d-371f-8c8c-f1db475b36f5 | -11.13492 | -46.34728 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2c509c79-b753-3853-8738-35b786d0a028 | -11.01486 | -45.93391 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6644248-da3b-3162-93a9-adc812b9a076 | -9.24083 | -57.08245 | 2025-09-06 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5edcfe44-29b6-3f49-97fe-1d5597e36cbc | -9.25556 | -57.07843 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09702c7b-2a60-3673-ba30-e383995c2a74 | -17.70284 | -44.49374 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c440fdfa-0203-3b71-8ab1-855d07bd96dd | -21.13535 | -46.2734 | 2025-09-06 04:19:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e969040f-9187-30ca-ad27-350a4f43ecc6 | -11.61965 | -52.20854 | 2025-09-06 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b031221-3062-3c0f-88f0-56cb0eddbf20 | -19.79437 | -40.84513 | 2025-09-06 04:19:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90e7091b-f32c-39a8-bd42-3ef5c10d40fb | -19.52131 | -46.0893 | 2025-09-06 04:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03c1e524-7de1-31c0-813b-f17cfc6de951 | -10.46143 | -53.61658 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d37f254d-655f-3ebe-a520-73b370a23a86 | -9.24905 | -57.07698 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c18b7d6-921d-3a64-88eb-4fa59a06ceea | -9.9759 | -51.64198 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd08daa0-63fd-3668-b935-6ded2b7cf669 | -15.7219 | -53.58904 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b142b73a-0095-3b07-828e-cb0094cbcfdc | -13.18268 | -44.4852 | 2025-09-06 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a9eb04b-805c-3163-9983-86dbdf4e8b3a | -12.69172 | -44.96503 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a8d3308-ab09-3f47-b8c1-191b524191e6 | -10.21341 | -49.7231 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6cf0285-aad5-3b2d-924b-83d177f0e9d9 | -23.36975 | -47.17823 | 2025-09-06 04:19:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a447ba1b-c12e-3630-94ea-c8fca887c542 | -19.6917 | -49.45774 | 2025-09-06 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fe43930-75e8-3e20-8daa-79a4b06749c1 | -16.32103 | -52.94173 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3e4b538-4366-3b85-b63f-c11b6ff7e216 | -10.79408 | -47.74206 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65541b65-2a3f-3388-977b-84eafb78da3a | -19.88936 | -57.9161 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8ddcc182-7b42-3d0b-963f-b2bc0ab8210d | -15.72422 | -53.57727 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af4d9941-1253-3b4d-ab82-1ada8342df9c | -9.24867 | -57.0771 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94bf4c2c-3de5-3dc9-a5e2-bcdbfbacbde9 | -11.01424 | -45.93768 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14fd88d1-ca21-389b-8313-ecf5203107ad | -12.65361 | -41.83854 | 2025-09-06 04:19:00 | NPP-375D | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1016337-26bd-328b-8359-b72094c320ce | -22.6578 | -46.8266 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1a31d9e6-5043-3567-b515-7ef8dcdb7559 | -11.21235 | -55.02055 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5bfc415-9085-3e12-b4ec-31fdb914b586 | -11.00706 | -45.91717 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c7d33c0-30a2-3202-a9a0-22e6c8bb16fc | -17.26091 | -49.00304 | 2025-09-06 04:19:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 591ef506-2ba9-3999-b84e-ea6e8b8b6507 | -10.75467 | -46.34974 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf652c53-86b9-340a-9b60-dc93d1ab7ae5 | -18.61102 | -48.2111 | 2025-09-06 04:19:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f8ab176-c48e-3522-9cec-0b01a0bd389e | -11.22283 | -46.18121 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 929bc722-7d21-3a34-91aa-00cd5a9c9e84 | -18.08217 | -45.44091 | 2025-09-06 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ce72295-e4ca-3694-bb43-d64edccbfc77 | -20.54028 | -46.46624 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6630fd25-f2ce-319c-83b5-56c7399bb694 | -11.62466 | -52.21606 | 2025-09-06 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7350d5b5-ca7f-3096-a86f-ad889797e015 | -11.93323 | -46.65024 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc91a395-f8a7-3eba-8f4b-dc68f42272e2 | -20.18157 | -44.24124 | 2025-09-06 04:19:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c6955918-cfc6-317b-a3a0-8bf835d28de6 | -9.99161 | -51.62591 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 475df94a-fe5e-31c3-bcba-9f83ea22936b | -18.10305 | -46.93287 | 2025-09-06 04:19:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ba3a2e2-b266-3732-94b7-710ebd8663e4 | -10.97532 | -45.9814 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f11adf-4adb-3ee0-b7e2-b7d0a33e4c8f | -10.77349 | -48.27256 | 2025-09-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c7cd380-3f84-34c4-8d15-2dd00d117532 | -21.8395 | -46.4602 | 2025-09-06 04:19:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 975b2705-fb9b-3206-bddf-331e98ca67e8 | -10.21696 | -49.72785 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52df04e2-5474-3fac-b391-8a9ba95f70e2 | -17.23431 | -46.71266 | 2025-09-06 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a634185-9ad4-359a-9bd3-9c44bf983184 | -21.30445 | -48.55545 | 2025-09-06 04:19:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec47b457-6dca-3b20-a96d-cd26232d9e25 | -11.54006 | -47.31364 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e63718c9-3985-30ce-8df3-7ec763dcf763 | -22.24795 | -48.74701 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 72058fdd-5b84-372e-9a30-874e41cf51c9 | -22.76699 | -46.45681 | 2025-09-06 04:19:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1197ff0b-6684-3ddd-a5cd-3b27a21cd1c1 | -20.46138 | -48.78769 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d329aca8-fc9b-3366-b5d5-f25798f57bad | -11.88505 | -50.59718 | 2025-09-06 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb541cf6-c0ed-32b9-a61c-721294c7e1ce | -12.01793 | -47.77693 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bf3d038-3da0-36f5-a0d1-63ecfb68f7e6 | -20.46188 | -48.7863 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3debca8-1471-3e57-9c93-d3dce314997a | -18.26716 | -43.02071 | 2025-09-06 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d437506d-5d3c-33b2-8a62-99e60c5c9f7f | -15.73459 | -53.60318 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1718ecc4-5693-3c2c-9e18-bd2d96940204 | -20.53755 | -46.46194 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70b4c077-c82a-3807-a870-318f43bf4682 | -16.32858 | -52.95336 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7e304bd-6787-3fd3-a74c-e80bcbcf2810 | -16.32008 | -52.9467 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f83a7a42-eda8-3edb-b6c8-302dac853e25 | -11.55016 | -47.31977 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6278196-286c-3d91-a7a2-0b2fa6400726 | -12.68725 | -44.97159 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 985a0e6e-b118-32b9-bffd-256d88d59be1 | -11.21736 | -55.02622 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 437c6bb6-7267-3d94-8c4c-ee2f28913479 | -10.79033 | -47.74156 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 65228d38-472f-3a60-864d-7b7140ebb46d | -11.38882 | -44.96653 | 2025-09-06 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f7e1bd2-ec04-3809-be20-ae97d06faf7f | -10.77263 | -48.27766 | 2025-09-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e30cb98-e819-3040-9bc7-34762bfa5a0a | -15.71205 | -53.58666 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f293f46-9263-34e6-b9ba-9c1c81b8a7ca | -11.9262 | -46.64611 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d81ce364-b449-3cb0-8bd2-c5282707b3db | -19.50619 | -42.56956 | 2025-09-06 04:19:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bc5836a-c196-3800-bfca-46c459520cf7 | -18.44991 | -43.84713 | 2025-09-06 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ffde7faa-1dc2-3ee2-bbd8-7dd220d86e96 | -9.24312 | -57.06927 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0add4794-3f76-30be-b1a5-640ca5df6dea | -19.90996 | -57.93631 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 42b92e93-1a45-3ff2-aa09-4295d6f6ec74 | -11.36365 | -43.51788 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7c1662f-a2a4-3e71-a758-401e679c9341 | -22.76424 | -46.45245 | 2025-09-06 04:19:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7aaae3a-de06-30ba-bf63-eb0c5dd6fe41 | -11.01548 | -45.93014 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dee4705-d07b-3a2f-af89-6f20411e91e2 | -22.27898 | -49.5689 | 2025-09-06 04:19:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ec0002b-f1a0-323a-b8d5-a3057f1a5246 | -10.86285 | -47.27454 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d20fcee0-408b-3d89-af5f-a82cac9a82b4 | -10.47384 | -53.64117 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f4bf02b-ab36-3111-8276-850f8e2c77fe | -20.53813 | -46.45825 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a09a140-dc6b-3184-a738-e9692b363cf7 | -17.60779 | -50.55877 | 2025-09-06 04:19:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d71626fa-1bcf-34e6-9961-042f00851892 | -17.8721 | -44.31837 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c3ae9f6-2409-386b-a00e-f1f1f6dd269d | -17.71075 | -44.50983 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97bf8c83-c41d-3d04-b702-6fded8063e7d | -11.21148 | -55.02493 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f54e7ea5-b779-334e-8528-44a6e88ccc80 | -10.7688 | -48.27698 | 2025-09-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5fd3d0a-b16e-30d6-8b33-bbc47a176551 | -17.72685 | -42.66141 | 2025-09-06 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 57092402-40cb-3af8-ab45-b140f1988cee | -16.32572 | -52.94276 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a23e7999-3ab6-36aa-9ef1-f27d65054c9e | -18.44306 | -45.93489 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7400910-088f-3e64-a6b3-f6152c14bc6b | -11.75317 | -47.74781 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcb327fd-0e25-3f4d-b039-51e88bd84275 | -17.60287 | -50.56328 | 2025-09-06 04:19:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f15079d2-6653-381a-9b27-24dbc60839e5 | -9.9845 | -51.62173 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 555c9e28-71a9-30ce-8b80-dd423b9fc70e | -12.46848 | -48.0383 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c23bb1e-b272-3ed9-92fa-e435bb1feee7 | -10.47317 | -53.64478 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9be3c4e9-d310-3c9f-926b-6302230c118d | -10.21263 | -49.72205 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08b3ce19-f96d-366f-a55b-37d6b90ae662 | -20.46417 | -48.79247 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 55991c24-cd7a-36e0-be6a-9b72b0eb8f34 | -9.39608 | -54.74918 | 2025-09-06 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfa9e3c7-4da3-3e01-ae18-31e8d50fdb90 | -10.46683 | -53.61657 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25797fc8-f4af-3d80-a117-e9204affd7ae | -18.56129 | -43.82423 | 2025-09-06 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b871d301-b006-3b12-98e3-e0dc09a7a7f6 | -11.36087 | -50.30161 | 2025-09-06 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
