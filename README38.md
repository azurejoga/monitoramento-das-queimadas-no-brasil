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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6d0ea32-d5cd-3c06-a7b2-47c9a46ffe6c | -9.80116 | -46.05507 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3637faa3-078a-3184-afe0-5be8cb71ce42 | -12.56115 | -44.8028 | 2025-08-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d761d11-f31d-3b05-a1d1-15c8961c2dde | -11.84535 | -46.38297 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 122f4b5c-9e83-3ae9-903a-0442cf897af4 | -15.76683 | -47.76399 | 2025-08-30 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8120d4c-ed79-3e20-87de-35c26ab207be | -11.9295 | -46.68952 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b9b835-1db4-398e-845c-a13170d5a915 | -13.9834 | -46.32379 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc07eb82-597c-311b-b93e-bba15b588912 | -11.34019 | -43.59433 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58b07854-762b-3dd3-8f88-437e112feca6 | -9.69501 | -48.30816 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e25610e-81c2-3b15-a95f-f18ba87e6f38 | -13.38232 | -46.96857 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc49b7d7-cde3-3e2d-8e1f-49a34b2d9858 | -13.6681 | -46.92508 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67692231-23d9-32fe-a122-e642de9a2123 | -11.87344 | -46.37675 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7402702-7ebe-3e56-9d1e-8586259f66e0 | -11.72756 | -51.75732 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54378d73-8426-3197-81e9-27cbbfafa7e0 | -14.02689 | -44.4879 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6501994-011f-37c6-9cb0-dca2c9b58e21 | -13.41198 | -47.0172 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0adc32f6-8efa-3ce6-954c-f8c536951ff7 | -14.49666 | -52.99897 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 676e2de9-b4ef-3321-977e-2706444d77bf | -9.10845 | -46.04718 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6209671-e969-3a22-8311-f4a357be263d | -12.68739 | -48.1533 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0545ae43-2d38-3c38-a05e-06e5a8e121a8 | -10.68892 | -47.063 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc305ae0-f321-3a4b-a054-02440199e284 | -11.30095 | -43.64378 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4a2ced1-e8b8-361f-8bc6-ad2ead0a2f27 | -10.18065 | -46.58097 | 2025-08-30 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 200def60-6094-3a39-8b1f-cb7767ce343c | -10.64978 | -48.65985 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d98ea46a-d59b-32ad-adb8-d7c2bf75ac56 | -12.05337 | -46.63742 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cef7561e-b204-3565-b2dc-7d1842b9132d | -9.43614 | -47.64151 | 2025-08-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af7c0b1b-74c8-3ec1-8efd-ef9b22152118 | -12.94103 | -48.12658 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1518e47-588f-31b4-a570-f4ac5370f0f6 | -14.44951 | -53.38158 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ffd0c7c-03d3-3179-a321-b83dbe21d4f1 | -22.68534 | -46.84634 | 2025-08-30 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dc5b6e0a-5cab-3057-b750-ed0cb3d71f01 | -20.08936 | -48.26979 | 2025-08-30 04:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e67df32-9457-39f4-9992-d28904848534 | -22.21528 | -46.75931 | 2025-08-30 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c7342f6-5c06-3012-8a37-345199ca2bb3 | -22.68874 | -46.84694 | 2025-08-30 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| abafb343-9968-397d-a3d1-1708fd683dda | -20.08605 | -48.26921 | 2025-08-30 04:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba242b7e-631d-3922-be56-08b2af744a8b | -19.29352 | -48.96578 | 2025-08-30 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78317afb-2485-3599-a8f7-d56da2c84245 | -22.0599 | -46.69459 | 2025-08-30 04:23:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e627c546-d4d2-3189-8495-81e0cc9d8e8b | -20.38361 | -54.57145 | 2025-08-30 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43542ce5-2cd8-3419-8a30-e761b4681508 | -18.41708 | -51.97239 | 2025-08-30 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c08f8042-ba90-397b-9efc-1169e35f28d7 | -21.05973 | -46.57165 | 2025-08-30 04:23:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ecd1878-f377-30e8-b041-c9ef0f4b0bff | -18.41679 | -51.97053 | 2025-08-30 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cbcf607-6392-3120-b3b9-2ca910b3c58e | -19.44901 | -44.29795 | 2025-08-30 04:23:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38388003-53a3-323c-a2a9-9ff48a976210 | -19.12401 | -46.44968 | 2025-08-30 04:23:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8770bae-689e-330c-b4b9-3158d1b4ef93 | -20.4336 | -53.7668 | 2025-08-30 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f8001e-0c47-3692-bae8-7b5ebec60b8f | -22.21473 | -46.75964 | 2025-08-30 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40ce4da0-8866-30d8-9410-ce6263a581b2 | -20.09209 | -48.27403 | 2025-08-30 04:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 296008ff-2f40-336c-84c0-eca4c4b04187 | -17.70086 | -47.27929 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f2d3650-f506-343f-9c6c-b5db30926080 | -17.71573 | -44.39491 | 2025-08-30 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4e23037-7616-3155-b28e-9e8f7e41eb08 | -17.91787 | -46.84068 | 2025-08-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bb55acf-4f27-37b5-a4e3-5a09582f4030 | -16.53373 | -55.04383 | 2025-08-30 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c9a7f1b9-ca6c-33a6-a697-7cb8489fbc6c | -17.69369 | -47.28178 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 480c4bd1-19ca-303a-ac1e-ccf2d82d43cb | -17.66412 | -46.6793 | 2025-08-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66969df4-18e1-3399-a7a9-90b26e9acadc | -17.91455 | -46.84013 | 2025-08-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e183b42e-ed80-3377-9449-14fd32e2c239 | -17.45018 | -44.48551 | 2025-08-30 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31ab3b3e-7602-3312-9a55-9d68f43328cb | -15.21896 | -53.80694 | 2025-08-30 04:23:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2f069cc-70a5-3068-9db8-72b37622b900 | -17.70305 | -47.28707 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdae6b34-7146-30bb-878e-5865f6ee4a87 | -16.25425 | -48.97346 | 2025-08-30 04:23:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70b54ad-1e6a-3794-a8e2-91f80d51e647 | -16.73421 | -49.08866 | 2025-08-30 04:23:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80a1ad4c-d677-339b-aea6-c697e63ea2f6 | -16.58477 | -54.65077 | 2025-08-30 04:23:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5932e7f3-3b66-3311-9a7b-51354ee7e315 | -17.45316 | -44.49009 | 2025-08-30 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24097ec2-e34b-3d93-aaa9-c97bb16cf7ab | -18.8547 | -40.33067 | 2025-08-30 04:23:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93b21b6d-e6d3-303a-92a5-ced7412a4e19 | -17.92119 | -46.84122 | 2025-08-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d727aeb5-7e5f-3cd8-b06f-b9385b7e4eec | -15.21983 | -53.80227 | 2025-08-30 04:23:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51fa20b7-716d-3b34-b4a8-9aac7ed509fb | -16.58013 | -54.64992 | 2025-08-30 04:23:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 825821cf-d9a6-326d-b04d-5950753a10e6 | -17.53781 | -46.90417 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b73afb8d-e1b7-3e76-b56c-d612b63212f3 | -18.85141 | -40.32944 | 2025-08-30 04:23:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4f22e5b-813b-3425-b409-9dadc9d368ee | -17.70142 | -47.27569 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32bda715-72ea-3710-bcc7-759ae23303d0 | -18.1045 | -46.93069 | 2025-08-30 04:23:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd21042d-0a57-31c6-9dfb-b2634944f9fd | -16.39107 | -47.04195 | 2025-08-30 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf1125e-d597-39b9-8e20-7618c6ebd64c | -16.29696 | -47.93915 | 2025-08-30 04:23:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eeed3ae-7052-3bee-a708-f067b266d051 | -17.45373 | -44.486 | 2025-08-30 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66be26a3-40c8-3e37-a9b0-c2d44515548d | -18.80062 | -40.15606 | 2025-08-30 04:23:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2393efc9-aced-395c-9a4b-3a4922150acf | -17.70417 | -47.27985 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d0f032-69a6-3d90-8086-4f08321851a4 | -16.6168 | -54.48327 | 2025-08-30 04:23:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeed4058-18d8-35de-8eb3-bb1e035ff1e2 | -17.37799 | -44.27706 | 2025-08-30 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1011c9df-f4ae-3be3-bb80-960ea99cf198 | -17.24832 | -46.66336 | 2025-08-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d760ed96-fa1d-3237-a914-bccf440912c7 | -15.2207 | -53.79762 | 2025-08-30 04:23:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 950735fc-9bcd-3e10-b9ae-74b65b54291a | -16.58382 | -54.65574 | 2025-08-30 04:23:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 664b1f5b-fc79-32c2-bf66-55a4993ba44c | -17.69756 | -47.27873 | 2025-08-30 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e94d94f0-fc88-352b-a16c-34a4e8e3daeb | -15.59 | -56.02032 | 2025-08-30 04:23:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68aa7d79-025e-34f0-b832-9b80b21869d1 | -15.01984 | -59.91636 | 2025-08-30 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ac020f-cd32-375e-a56a-c528050a0616 | -16.53386 | -55.04566 | 2025-08-30 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1d1cdb84-8f29-3719-bacc-4c394ea2468c | -17.4496 | -44.48962 | 2025-08-30 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73da9ee5-bb42-3040-a474-251228cd9edb | -22.93973 | -46.55965 | 2025-08-30 04:25:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c30c9dff-d0d8-34f9-af95-da05fb7f063a | -22.19494 | -54.84 | 2025-08-30 04:25:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 39dc9faf-b53a-39bb-97cc-7e4c74550f29 | -28.72374 | -55.64108 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 5bb19ac6-b7ae-3622-965b-1a55373740fb | -29.03162 | -52.36997 | 2025-08-30 04:25:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 806628b4-3a3b-336b-a7bf-b3e8389f10e2 | -28.72878 | -55.63636 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| a8facfd9-7d55-3521-b33c-708ca68a8e4c | -22.84546 | -47.49352 | 2025-08-30 04:25:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 38d96f9c-0a61-336a-ae31-70ca3484b766 | -28.72099 | -55.59285 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| b59613ab-243c-331e-9bb6-584345f51143 | -28.7226 | -55.64682 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.6 |
| d12da137-d705-30e4-843d-c184a501036b | -22.84881 | -47.49411 | 2025-08-30 04:25:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83e31ec0-2a34-33ed-b70f-c6e105e0a76f | -29.16544 | -55.00369 | 2025-08-30 04:25:00 | NOAA-21 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 713e69ee-49a0-3772-a7db-8f945fff985c | -28.72537 | -55.65359 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.6 |
| 997eb265-d9f3-3a0b-af82-bb4e4fad5388 | -28.59237 | -53.6231 | 2025-08-30 04:25:00 | NOAA-21 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 943bc300-affe-3410-9402-c5a5c126ede8 | -28.72651 | -55.64784 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.6 |
| 6cb68e87-762f-38a4-a8e1-3855601a7707 | -28.71596 | -55.59755 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| c3aa5a7d-3456-39ac-bda4-598488dab755 | -22.81246 | -47.1552 | 2025-08-30 04:25:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86f11558-b9de-3ec9-b1a5-2ae5bcf6ee03 | -23.32176 | -46.10072 | 2025-08-30 04:25:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da24c00d-2f37-3811-8090-e6c4bd6af36f | -28.72765 | -55.64209 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 2e44b2b5-0f84-38be-97cc-49966f7c82e1 | -23.22371 | -45.74044 | 2025-08-30 04:25:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 697102db-cb69-3d64-8d44-94d6415004aa | -24.43468 | -50.10274 | 2025-08-30 04:25:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2185193-c204-3f53-a218-6f8598d4849f | -22.84211 | -47.49294 | 2025-08-30 04:25:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 6d609f3c-8797-3ac0-a646-95f5d554dc93 | -28.71708 | -55.5919 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 13e068d0-b221-366b-8593-27e6769ebb4c | -28.7249 | -55.59378 | 2025-08-30 04:25:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |


[Clique aqui para ver as próximas entradas](README39.md)
