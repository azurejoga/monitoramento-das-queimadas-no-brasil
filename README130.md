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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bdc231d-023b-3a03-88e9-d1f05694c049 | -19.54076 | -56.70434 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8ea475ee-7f72-3164-b8b7-595fc69bba30 | -19.53551 | -56.70491 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 58ab7a0f-61a9-39a8-9dfc-5e5192b1c97f | -19.53531 | -56.90815 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| f453d798-d326-3375-99df-55833dfc3b27 | -19.53516 | -56.70156 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 6abe89e0-7907-350f-bf9a-073ef201da27 | -19.53026 | -56.70548 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 567047d2-67d1-38bc-87c4-6d986c7a8c07 | -19.52991 | -56.70212 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 028de26b-1772-3489-bd01-a75ad5da1781 | -19.52956 | -56.69878 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 8de1c4a3-3fdc-365f-b397-c43a87808742 | -19.52921 | -56.69543 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| a0dab1c0-adae-33b4-b915-4a1c42642ddb | -19.52886 | -56.69208 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 76d1d988-0b4c-3371-80b6-4b7dd2b4d0a3 | -19.52851 | -56.68873 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 3b5cfaff-69fe-349d-8cf1-d1943221dc37 | -19.52432 | -56.69934 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e8b46776-9511-3ed8-9fa9-403248a15cd2 | -19.52397 | -56.69599 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9bcd8639-90e9-3764-aeed-fb4e9996ce2e | -22.14229 | -56.5785 | 2024-10-25 16:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a84e7c2-a035-3b11-9a6b-9f40d7c393b4 | -17.30241 | -39.50597 | 2024-10-25 16:48:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.9 |
| 0aa61c2e-90f7-3fe9-925b-c683cb192442 | -17.3013 | -39.50713 | 2024-10-25 16:48:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 0c03341c-961a-37ef-9651-923abe826c18 | -17.30016 | -39.5013 | 2024-10-25 16:48:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| f4e9b44e-791d-3d6e-aeb7-fc02d49ac53d | -17.18079 | -39.3937 | 2024-10-25 16:48:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0e4f28c2-c0ed-3ac8-9ec3-82637c5c71fc | -17.14101 | -39.53226 | 2024-10-25 16:48:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 2f46f9b8-3ce0-35a1-a610-2bd71a6b4a6d | -17.13234 | -39.54026 | 2024-10-25 16:48:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 88a249f9-2928-3b6d-a746-202022f4a55c | -17.11875 | -39.54932 | 2024-10-25 16:48:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 298d6c96-1c8d-3a06-a329-0708cef0e76b | -17.11382 | -39.55032 | 2024-10-25 16:48:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 75ae5689-25ad-3bff-a994-ee42acbb5c00 | -17.11261 | -39.54433 | 2024-10-25 16:48:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 61764fb2-a509-3e18-b9a4-f83c0ac59f21 | -16.18484 | -40.26025 | 2024-10-25 16:48:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 15cf3a89-98f1-362b-b7b7-f482ed069e7b | -16.18004 | -40.26118 | 2024-10-25 16:48:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 55b8ea42-794a-3dbd-8ee0-975a0dc6abf3 | -16.97606 | -40.25539 | 2024-10-25 16:48:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 25f9f93f-d8ff-36e1-b1a3-66ac5ab728ed | -16.85117 | -41.16771 | 2024-10-25 16:48:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3f8a5608-a317-3adb-a66c-6d9d77b127a4 | -16.83621 | -41.0125 | 2024-10-25 16:48:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| c859f99d-653c-349c-8d81-3900a7b0b980 | -16.83235 | -41.00986 | 2024-10-25 16:48:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 985defa8-a12f-3d53-b6e8-40bc1781ce6a | -16.80597 | -40.77689 | 2024-10-25 16:48:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| cc22eac7-4f63-3637-b5c8-e04fd22f9f29 | -19.09381 | -40.9921 | 2024-10-25 16:48:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e3db20c7-84c6-3737-ba0a-418f66c5c0e8 | -18.80578 | -40.25533 | 2024-10-25 16:48:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 95a48d68-5784-3f8d-82ea-635e0a7b4783 | -20.24621 | -41.49783 | 2024-10-25 16:48:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 48d0c961-d06e-30a9-b52a-f9c7c0c12e47 | -20.06774 | -41.82283 | 2024-10-25 16:48:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7c2e4385-f8aa-3d23-b5b5-05ecfdc376f3 | -19.44851 | -41.65155 | 2024-10-25 16:48:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 532d7385-447e-3762-a959-2385ec9d8e1a | -19.44788 | -41.64819 | 2024-10-25 16:48:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| d2442b75-fa0a-3a32-b13e-bca0d241f091 | -19.44439 | -41.65244 | 2024-10-25 16:48:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 2e408ada-de1e-38e8-8376-64b4a52951a8 | -19.44032 | -41.65361 | 2024-10-25 16:48:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1f0ec794-6c92-3a75-becb-f1f209b015b9 | -21.30338 | -40.98668 | 2024-10-25 16:48:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 027ee47c-5812-3b3e-9672-ddab48c3b4a8 | -21.30209 | -40.98562 | 2024-10-25 16:48:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 6ec5b572-fb0a-3436-ab21-5c48dfc163fa | -17.64277 | -42.03162 | 2024-10-25 16:48:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3d0ff679-b344-3982-bdb0-f5ee91c4f0fb | -17.38317 | -41.6868 | 2024-10-25 16:48:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| c46fb70c-f75f-3e03-abb4-5e5a1fdae3b5 | -17.38107 | -41.77126 | 2024-10-25 16:48:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 4e89aee3-5b38-358c-b510-7c9bd0a081c0 | -17.38031 | -41.76714 | 2024-10-25 16:48:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 3eff6f7d-f077-38a1-aeb6-9baf7a6eff63 | -17.37894 | -41.68785 | 2024-10-25 16:48:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| cc17ef60-d355-3283-9a39-ed5112dd89a7 | -17.33921 | -42.13704 | 2024-10-25 16:48:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c67035d5-50eb-3aff-9db1-640b060c3c31 | -17.13829 | -41.87519 | 2024-10-25 16:48:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 6ee73013-26c3-309f-b15a-f7ffbb42c3bb | -17.07774 | -41.87636 | 2024-10-25 16:48:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| ae82c1b1-8847-3187-bc01-7d33fd08762d | -17.05653 | -41.90425 | 2024-10-25 16:48:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 39d6fe87-851a-30d1-a17b-1e0ec1a54799 | -17.0523 | -41.90512 | 2024-10-25 16:48:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 14df7862-a433-3c81-9034-308f73ebb312 | -16.91002 | -41.89202 | 2024-10-25 16:48:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d0d43086-6fce-3d33-8c44-d663e2b1fe53 | -16.79782 | -41.63764 | 2024-10-25 16:48:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 001e57e8-0601-31fe-bd8f-841823388334 | -16.78863 | -42.27187 | 2024-10-25 16:48:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 882fbe9e-558a-33ab-a70c-a42d7d2a159c | -18.09097 | -42.18924 | 2024-10-25 16:48:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f0e8bc7c-4897-36e9-b4f4-730bd14f0308 | -16.88038 | -42.79728 | 2024-10-25 16:48:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a7ee3241-3512-3079-9dae-cc897657878e | -16.7188 | -42.85704 | 2024-10-25 16:48:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| afaf26e3-c589-3646-bfde-6a3a3fcb2d89 | -19.58655 | -43.94581 | 2024-10-25 16:48:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9b535ee0-d7d5-3868-9b34-c16997443a3b | -17.57103 | -44.62743 | 2024-10-25 16:48:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e3b326a8-b272-34a8-9bf4-a2bc155f9fd8 | -17.43873 | -44.92387 | 2024-10-25 16:48:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 66ccbdaf-bc2f-3641-996d-de711e55ce64 | -23.09179 | -47.05821 | 2024-10-25 16:48:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d870f3c-a0dd-335e-acda-ed848805b62a | -10.63852 | -47.97554 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 41c365ea-7d6c-3a3a-9429-801962778c01 | -10.63793 | -47.97185 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2113d9d8-3c07-3dfc-91ec-ccf66880571b | -10.63455 | -47.97234 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| c631065a-f8c1-36f2-bcaf-9522f1ee5483 | -10.62776 | -47.97328 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f5c65696-a95c-3095-af18-37e23b677beb | -10.62642 | -47.97374 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b1a1cb37-b786-31fe-8157-5be2199192e3 | -10.51059 | -48.17129 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 90edebff-2cb9-3b35-98c3-8c231ac26426 | -10.51002 | -48.16766 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4b81bcf1-36ac-3413-bde9-e3584c6ebd9f | -10.50723 | -48.17185 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b3b4962a-1b69-3a83-8778-d326c6c213e7 | -10.40367 | -48.05114 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 570dda0c-3cea-3df9-83d5-1c98daa2e9b0 | -10.40309 | -48.04744 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 591a11df-57f2-30b5-8828-46cbd18e2d40 | -10.40029 | -48.05169 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| cbb5df49-23d4-3531-b4ef-db1d05fa30fd | -10.39972 | -48.04799 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| af519cbc-cd9e-36de-8e33-bf7797f92b31 | -10.39114 | -48.01551 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05027f22-2cb1-3d6a-9c86-2cd680f447f6 | -10.37715 | -48.03667 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57aae1d8-fb5e-3039-97fd-30b2e20e4c50 | -10.32586 | -48.13896 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80fafe10-212a-3fe7-98f2-d13fa7a0f59f | -10.21463 | -48.47458 | 2024-10-25 16:50:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 688d2036-6c04-3ddc-9b51-99c67325c5ac | -10.17723 | -47.90654 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a826ad5d-62ec-38ce-8349-5e3e5fe62d25 | -10.17442 | -47.91082 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08839b82-6644-34c9-97c9-4588953a0abd | -10.14663 | -48.30483 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90f4a5ce-a087-33d9-af93-3288dcb33309 | -10.12312 | -48.71659 | 2024-10-25 16:50:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48eb0ba8-4e79-3a2d-8f19-b5842ff3a877 | -10.09198 | -48.2994 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e10a803b-4363-37c5-a354-bfb50817977a | -10.07911 | -48.86937 | 2024-10-25 16:50:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ce1e126-df83-3e81-8a32-44f5b156dc5b | -10.05753 | -48.05867 | 2024-10-25 16:50:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8365001f-a1a1-3515-b909-ad12c4edc126 | -10.05685 | -48.94511 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd897e97-d8af-306d-a5ce-5012e4ea74a7 | -10.04916 | -48.20289 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a94d4a9-7cf2-3099-a86d-0cbf42112592 | -10.01819 | -48.82826 | 2024-10-25 16:50:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14bb7825-bab1-3429-bcd1-b44ffbc1ff48 | -9.99453 | -48.85013 | 2024-10-25 16:50:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d58e34bd-2c13-35b2-b0d5-f63ca4b99e79 | -9.99175 | -48.8542 | 2024-10-25 16:50:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 50470c26-b284-3d62-b846-bbcf4262588f | -9.9912 | -48.85065 | 2024-10-25 16:50:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4d0ad18d-33a9-300d-a193-3e8e23dc9276 | -9.96794 | -48.09232 | 2024-10-25 16:50:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a70e5c10-654b-33b4-ac59-01116b7be707 | -9.94841 | -48.9479 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2fc0500d-ed2f-3cf1-a797-93a9c4247e5a | -9.94786 | -48.94437 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4a28fd6-0b62-3933-a12f-385de20c2d26 | -9.94509 | -48.94843 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 19d94d8f-1301-3506-9953-8d172d230085 | -9.93825 | -48.27676 | 2024-10-25 16:50:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a05170f-c4c2-307c-a64a-d2ffc7e240da | -9.93742 | -48.87731 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 697e0547-d3b6-3727-8aed-f0b6fb3f6204 | -9.92143 | -48.14884 | 2024-10-25 16:50:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1d1def3-2f34-3751-b048-a1c466ccf345 | -9.91856 | -48.90929 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e771a452-dcff-349f-bbc3-c0932e25235a | -9.86817 | -48.73658 | 2024-10-25 16:50:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9586f7f1-42a9-3eb9-8246-941e21f74757 | -9.85411 | -48.8875 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d5f6996-6378-383b-8287-848d2d3c78e4 | -9.85078 | -48.88803 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15a512df-e455-3b82-827f-4e754bf75533 | -9.73243 | -48.41716 | 2024-10-25 16:50:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README131.md)
