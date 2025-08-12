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
| 0c94a318-1ceb-3bc6-869b-d9572c977ec0 | -11.70417 | -50.1258 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a088cb3-bf4a-36e3-8e39-6d6ecc75cc0f | -7.06521 | -59.18502 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cb9d398-3ae3-3039-9df6-0f570e477b02 | -7.90029 | -61.52362 | 2025-08-12 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45d7005f-05e9-3bea-8d6f-b12c017d6f70 | -11.73199 | -50.10445 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a20ea266-e1da-3d41-ae2b-f9adbb4f61f5 | -8.57106 | -54.70998 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 709b7c57-517e-305a-9946-c6229498f29a | -7.87899 | -63.27172 | 2025-08-12 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4a1d182-22c4-3781-9ff7-399bb96fff9f | -7.06648 | -59.20318 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a934404-5cc1-3c5e-940e-448d04383720 | -11.68645 | -51.58871 | 2025-08-12 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db4080e7-5e31-3f7e-8b3c-a402e075d095 | -7.06465 | -59.21075 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12466e8-e4a3-323e-84b0-cafba3b46b78 | -8.56669 | -54.70933 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7a7ad99-b0de-3dad-91ca-3dcea56dfb91 | -7.20015 | -59.85007 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44999b3c-7889-31e9-b9ee-5018e1041f1a | -7.06127 | -59.21024 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265f32ea-8be8-349a-96c8-19b9be34ee00 | -10.31091 | -54.15981 | 2025-08-12 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df0610ca-77f6-3686-b42e-43665ddc33fe | -7.06183 | -59.20664 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 865d867f-4ea0-3ed8-b34b-563575f6a06c | -7.75032 | -62.31836 | 2025-08-12 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c3ac24f-5138-372a-b34c-d7626fbb314a | -9.26388 | -60.77764 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff960494-f612-3400-8e1e-b0277fc0413a | -9.18605 | -59.66441 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 609f6feb-d23a-32cf-9b58-b1bcd169c66c | -9.20353 | -59.66337 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35fb2129-184e-37b8-9be6-690769316805 | -11.45038 | -50.17041 | 2025-08-12 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca40e07a-4bf7-30b3-af3a-b01ac3fea44b | -8.02953 | -61.90717 | 2025-08-12 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94dc386c-c104-3f07-8eec-30fe0130db4f | -9.38455 | -61.53548 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00fbcc5c-d925-3c2f-a763-00562e5476ed | -9.384 | -61.53899 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1fcea0-106f-32b8-8d3c-6aa767178917 | -7.12811 | -60.12157 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 427070d7-af7f-3ea6-a23a-af3e3e9f90f9 | -9.38234 | -61.52794 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f48e00dd-c4ae-3953-99cf-b607b8e7fc6d | -6.97364 | -59.28493 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c1ac4c3-959a-343b-b8fb-4e7b3fea37dc | -9.71876 | -49.48294 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b605a8f-0798-3f21-83bf-258457eb583a | -7.12866 | -60.11809 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9772a022-96f8-3dc4-9cf7-2624420e1e1f | -11.68361 | -51.58949 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5641e28d-371e-3828-9240-e445ec1f9fd4 | -7.07269 | -59.20781 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 98243b3c-136e-320f-b24d-eb02a65f3543 | -9.9259 | -60.47898 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a21e7c4-833c-3827-a6ea-411be511de42 | -11.724 | -50.11834 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1de628b-bdcf-3dd8-b806-82dfce1cf3c0 | -3.43223 | -49.04204 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c61ec7e-b005-380e-abbf-8859a9c4b73a | -8.92466 | -60.76345 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 585abd0a-705f-3e0b-94ec-f27ff2488862 | -8.92133 | -60.76292 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 751939c4-5cde-31c8-bb46-6dea6701f965 | -9.38123 | -61.53494 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14698c36-58b7-3883-bc43-128a7c378697 | -11.67698 | -51.59636 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e6ca0bc-a359-327b-966a-3d4ee889ae59 | -7.48659 | -68.33808 | 2025-08-12 05:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2412d308-2fe8-3ccb-95d9-f4f4ac8e60df | -9.93038 | -60.49418 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff2a50c-6f62-331c-8e69-81b0dae513c6 | -3.43159 | -49.04647 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed9fac94-0b10-35b4-bfa6-fd9e43faf5c2 | -3.83076 | -47.74396 | 2025-08-12 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 963fea06-f73c-3110-888a-bb9a2c05b06f | -9.38511 | -61.53198 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d597887b-e870-3a4b-932f-d22b32c31040 | -8.93291 | -60.73255 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdb98642-3bbb-338d-8819-ca7c9942decc | -8.96222 | -68.79819 | 2025-08-12 05:25:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fb5014c-83a2-38e4-bd01-6fee6061d9e5 | -7.07717 | -59.20111 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb983297-0d9d-3819-b734-ff0c00c978be | -16.29207 | -52.91755 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9c1d973d-b6cd-3a04-80bc-0ea5cc3f20c4 | -14.68362 | -53.71947 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3904be6-f76e-3fc1-910e-a11d87d5c197 | -14.68909 | -53.71723 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 676451a3-029b-3113-9678-c3dd96efcded | -17.21873 | -54.12381 | 2025-08-12 05:27:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6573ad8e-2dfc-38bc-aeab-23a0d9a10fb4 | -16.2974 | -52.91365 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a201ed1-13bd-313e-985c-f477201e9529 | -16.38854 | -50.89732 | 2025-08-12 05:27:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc0d949d-1911-39e3-832e-052f14c0bf11 | -16.29229 | -52.90926 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7e5c13e9-5752-3059-a63d-dac643e3bb55 | -16.29724 | -52.92116 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3a71a7a-357b-3036-bd72-9374ab92da5d | -16.286 | -52.91574 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 11f8d8ec-40ba-33d6-9611-f569fe2da576 | -16.28654 | -52.91711 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 682d0e39-b705-320b-b20d-f4108339c89b | -16.29286 | -52.91076 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e387735e-6351-3a6e-a8c7-4de4c75a6ff1 | -16.39053 | -50.8998 | 2025-08-12 05:27:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4347287e-6ffd-3aef-a8d7-165a0154ac7f | -16.29189 | -52.91292 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 432bf17f-4ccb-34d7-b8ec-82ca4b56f9db | -16.39721 | -50.89658 | 2025-08-12 05:27:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1ceffba-ec59-311b-81f0-30f983a2f0d7 | -14.69385 | -53.72082 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79145465-b291-3d39-903e-cdec8c2205a7 | -16.29761 | -52.91801 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 19b46f8c-2739-3a0f-ae86-fb84581924f9 | -16.29671 | -52.91993 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b862bcd-1229-3af4-8f7c-6d606f5f09b8 | -16.29152 | -52.9163 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c9e4bcbe-acad-361c-8bc7-fbd711da3a62 | -16.29836 | -52.91153 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 036b8eec-3901-347d-b17e-e1fceb4b4f33 | -16.29329 | -52.90696 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46613722-ef8e-3044-bac6-1c970012d8cf | -15.30133 | -59.23689 | 2025-08-12 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcd5d5ee-9368-3e79-a34d-1d6affbbdced | -14.69347 | -53.72388 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 436addc3-d62b-3ec5-9931-0917e18cb64b | -16.30256 | -52.91749 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67b2e5f1-25d3-3bcb-8421-6e94e28e204e | -21.42701 | -54.69389 | 2025-08-12 05:27:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dee68f58-3647-3d86-bce6-bab159dcd883 | -16.29116 | -52.91965 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72448346-04cc-3340-98c4-15ac877d7a64 | -14.68835 | -53.72326 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b119cb71-de97-324d-b697-5e9eeffd1c59 | -16.29796 | -52.9149 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ca45d542-cd81-3ce6-8556-cd2f7c68b515 | -16.29705 | -52.91684 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de03748a-19c2-363d-8802-737ec7301d96 | -16.30841 | -52.91506 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| abb4a080-7159-3c33-ba09-3673444d0422 | -16.3077 | -52.92159 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a59b4689-3922-3153-a69c-302282c13154 | -14.68872 | -53.72022 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6d0c5c5-2998-30de-95a8-143935c5f9a7 | -16.29245 | -52.91428 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6534f223-fd21-32c9-adf7-ccb2442009f6 | -14.69458 | -53.71489 | 2025-08-12 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b4ffa97-e9b5-32dc-bd8a-bd025fdfcb2a | -15.71112 | -56.38972 | 2025-08-12 05:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 676caeb7-c765-37d8-a841-1c534374f9d8 | -16.28737 | -52.90985 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97e36198-d262-3512-9135-2004510a8f15 | -16.29635 | -52.92329 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cdf95daa-8251-3de2-a565-090315bbf702 | -16.28695 | -52.91352 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 81299536-3dbf-3c23-8065-b1a22c6ca533 | -16.28639 | -52.91211 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 236672ed-a7c2-3b64-b431-1b09179cfe73 | -16.29169 | -52.92088 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc1908df-b1c1-3fcb-93c0-826b1a4d20cb | -16.30805 | -52.91833 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 22448a93-8806-3dbc-8f0c-814af7426445 | -16.29778 | -52.91009 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a114aa3a-745c-3e39-b273-587d7f3b1aba | -16.39519 | -50.89421 | 2025-08-12 05:27:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f907c08-7ee9-347c-8c20-644bc7e3bc37 | -16.30292 | -52.91425 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa54ac0b-2866-3c08-bccf-5814a2a59516 | -16.28679 | -52.9084 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8ba841ff-aa9e-31ec-8320-3351f0c814f9 | -16.3033 | -52.91069 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45ceaae6-62a5-3d60-b84b-f59a516254b4 | -16.30922 | -52.90768 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 97437d23-92a1-3694-adeb-d84fe051e915 | -16.29685 | -52.92458 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 501d381b-ef0d-394a-b4b7-5b1135289eba | -16.30221 | -52.92071 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d7de45e-3bc1-3e7e-9aa6-cd48efd6581b | -16.30879 | -52.91156 | 2025-08-12 05:27:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6e7db2ff-1ba0-37eb-a471-4dfc3ae4b51d | -16.39471 | -50.89903 | 2025-08-12 05:27:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8a73b4f-adfc-3655-b6c0-d7d72166fd32 | -22.19239 | -54.76706 | 2025-08-12 05:29:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28f7c4f3-efeb-3cb1-9cc8-09084eca87b6 | -3.9684 | -47.8901 | 2025-08-12 05:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| eae33944-2cf5-39df-9bf3-31c39b8e45b8 | -8.5211 | -43.3063 | 2025-08-12 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 20d23929-415d-3c3c-bd89-1a6e1e8cb75d | -9.9192 | -46.1793 | 2025-08-12 05:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8794f25f-d4dd-3cc8-8d51-9aaba9ffea89 | -6.5856 | -44.564 | 2025-08-12 05:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ecaac4ca-7833-38cd-9204-9a976f5f6231 | -12.555 | -47.0034 | 2025-08-12 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |


[Clique aqui para ver as próximas entradas](README34.md)
