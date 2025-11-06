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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6dfd423-7760-3ce9-888b-6ae21f058319 | -4.5747 | -43.325 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ecca13fc-8d25-3429-af26-a2552ec23d41 | -4.593 | -43.3704 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a30dd4f0-3695-312f-afb5-6389c2d4abb7 | -4.5745 | -43.3483 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0c720b6f-ef31-396e-9240-7bd16ea09410 | -3.4436 | -45.3284 | 2025-11-06 06:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e3260b2c-39d9-3d13-80fe-353eadf94188 | -3.4437 | -45.3059 | 2025-11-06 06:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a19244c2-2885-3eb5-a3d1-973e9ed8f063 | 0.4466 | -60.4873 | 2025-11-06 06:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bdf473ea-bf88-3383-afc9-93729a033baf | 0.4466 | -60.4873 | 2025-11-06 07:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 788f0452-9a69-3ac1-a10c-417ef572ad0c | 0.44872 | -60.48355 | 2025-11-06 07:05:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cae389b4-2c11-3f35-8095-1e363edeef98 | 0.43095 | -60.48613 | 2025-11-06 07:05:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a214650a-4100-3edf-a547-c4c0f38b6cf3 | 0.44737 | -60.47458 | 2025-11-06 07:05:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7331dc1c-070a-39d8-a076-9d410dfde17b | -2.98132 | -52.8189 | 2025-11-06 07:07:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| bc916cd1-528a-3cad-bf5c-2c873bffc0b7 | 0.4466 | -60.4873 | 2025-11-06 07:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f63566a3-3775-3eff-bad7-f20cda5c9bd8 | 0.4466 | -60.4873 | 2025-11-06 07:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f3b969f4-7f43-33ee-9667-de77fc2bcadd | 0.84311 | -50.17068 | 2025-11-06 12:36:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 364a2bc0-b567-3dc4-bd3f-16f8686381fc | -1.02767 | -47.6531 | 2025-11-06 12:36:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 412c93bf-2e21-3dc3-9adc-64fa04532475 | -0.36221 | -51.74804 | 2025-11-06 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1a6976e1-e89a-3205-911b-1d080d64a81f | -0.36347 | -51.7393 | 2025-11-06 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 05e1fbf8-ddfe-32c2-bfb7-0b9ea7585f63 | -0.37226 | -51.74052 | 2025-11-06 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e84daa88-b435-3fb9-acb4-7dd0fcaf7018 | 0.84441 | -50.1797 | 2025-11-06 12:36:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 74012a6a-2199-384b-a374-e1305c22c10b | 2.00812 | -50.89565 | 2025-11-06 12:36:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b4d6e9b-a9b4-38af-8d38-2747345c15c6 | 2.6255 | -51.00647 | 2025-11-06 12:36:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27ee3b5a-550e-3070-8295-8db5a446d94e | -3.90415 | -42.55205 | 2025-11-06 12:38:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| c9472f22-2bee-3244-b29f-9b227e0602ba | -3.08326 | -41.92683 | 2025-11-06 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f8059307-a29f-39b3-a7d5-de012f82910f | -3.61985 | -43.51981 | 2025-11-06 12:38:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| f42e07ae-82cf-352f-bdf1-686ef7dccbc7 | -2.36763 | -48.4385 | 2025-11-06 12:38:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fa5cd2ee-4ed8-342c-a314-9a49efbc1aef | -3.47113 | -42.00226 | 2025-11-06 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 175.5 |
| 24a37fbd-ad8c-3799-aa48-04fa2bc933cb | -3.4862 | -41.99731 | 2025-11-06 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 399.8 |
| 91eb0b3e-6830-3537-bcbe-ba006e1cd393 | -2.66876 | -49.48941 | 2025-11-06 12:38:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b1876616-a310-33e6-8920-727acbba7f2a | -2.36594 | -48.45036 | 2025-11-06 12:38:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 6db6c256-755f-3897-b2a6-25b6fa7bd309 | -3.60443 | -43.51798 | 2025-11-06 12:38:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a7b923be-c40f-3b97-acfb-924c86beed93 | -1.43268 | -47.17019 | 2025-11-06 12:38:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ff58665a-a1a6-34ad-ac94-b39fe97cf1b6 | -2.66729 | -49.49975 | 2025-11-06 12:38:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 728ec700-e11e-3f6e-bacc-ebd98f633643 | -0.8874 | -52.01004 | 2025-11-06 12:38:00 | TERRA_M-T | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8bfbb5cc-5d60-3472-b745-a071d8ba81f5 | -1.29559 | -47.90823 | 2025-11-06 12:38:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 691a4352-c213-397e-abef-9833761c96eb | -3.60832 | -43.51167 | 2025-11-06 12:38:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7cad1b39-e521-33ac-be73-169b31de1103 | -13.65406 | -53.59134 | 2025-11-06 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09f07654-3f9c-3b7e-b3a9-28af26b01327 | -13.01277 | -53.4215 | 2025-11-06 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50457c75-22e6-3f27-86df-34974ad1070c | -12.41585 | -51.53742 | 2025-11-06 12:40:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 5a53df92-43fe-3534-b550-1913dd85301a | -12.1298 | -54.75708 | 2025-11-06 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b6193f1-194b-3909-a92a-b01381df64ad | -16.31824 | -49.5088 | 2025-11-06 12:40:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b61c8006-39d2-3f25-91a3-31ca1ca89a4f | -13.24793 | -54.17157 | 2025-11-06 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 166016c8-a87a-35db-9939-0a1b2fe284d1 | -12.60077 | -54.50711 | 2025-11-06 12:40:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4698cc0-ac66-3082-93b2-c74f4fb0f030 | -12.60208 | -54.4981 | 2025-11-06 12:40:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 674cb48e-dfe7-3d7e-909f-7a38c26b337d | -13.37513 | -54.25766 | 2025-11-06 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 12d0c49f-7f13-3372-a5cb-7a2b4aa7b178 | -12.15764 | -54.56693 | 2025-11-06 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e549552-7af6-360d-84dd-8ee26909ab57 | -13.24922 | -54.16258 | 2025-11-06 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7713138a-0128-35c8-b576-72eb1ed8899a | -12.2071 | -54.85881 | 2025-11-06 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9f317823-b132-3296-9d71-014d6429533a | -11.18283 | -55.91581 | 2025-11-06 12:40:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0bd09d8f-38ce-3ebb-86a3-50be0c2e2faf | -12.1488 | -54.56563 | 2025-11-06 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fd2fb8f7-61a7-333b-b24a-a6d0a071e686 | -16.32015 | -49.49225 | 2025-11-06 12:40:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 15abc981-e036-362b-b268-ddc5aab260ad | -12.20576 | -54.86794 | 2025-11-06 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cc4e097a-f867-39d7-8090-8445c33082a1 | -26.88231 | -50.92585 | 2025-11-06 12:42:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 4fb7fbee-14a7-313a-9f21-f848da3ef090 | -24.97315 | -54.19973 | 2025-11-06 12:42:00 | TERRA_M-T | SANTA HELENA | PARANÁ | Brasil | 4123501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 638e21c4-7cde-36d5-86c5-5e046cb8fe54 | -27.00361 | -52.67147 | 2025-11-06 12:42:00 | TERRA_M-T | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| afc86a2d-7f70-338c-b46f-f671cf3f2634 | -26.08001 | -53.05171 | 2025-11-06 12:42:00 | TERRA_M-T | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 6f19ecca-9ba0-3edb-a3c5-662ecf83be94 | -25.78659 | -53.3042 | 2025-11-06 12:42:00 | TERRA_M-T | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| aced613b-817a-3ab3-adee-bef46fb12abc | -26.25635 | -53.6315 | 2025-11-06 12:42:00 | TERRA_M-T | BARRACÃO | PARANÁ | Brasil | 4102604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2c4ad6f9-de15-3550-b520-c8ea550a3aa8 | -26.89075 | -50.92105 | 2025-11-06 12:42:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| f7d93dd7-0936-38f4-be75-9338184e07b5 | -24.28845 | -53.83582 | 2025-11-06 12:42:00 | TERRA_M-T | PALOTINA | PARANÁ | Brasil | 4117909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 32c0b872-2596-3a7c-be41-305a700ebb9c | -24.62422 | -53.32285 | 2025-11-06 12:42:00 | TERRA_M-T | CAFELÂNDIA | PARANÁ | Brasil | 4103453 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e50b92d2-efee-3051-a100-adb8e540198b | -23.49994 | -52.01044 | 2025-11-06 12:42:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 1e755b1f-596d-35df-896f-f4affaeeb9f2 | -27.07443 | -51.32568 | 2025-11-06 12:42:00 | TERRA_M-T | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 63d9a165-de9a-32ae-980e-d5d23cc8124b | -27.0726 | -51.34409 | 2025-11-06 12:42:00 | TERRA_M-T | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 4c20f392-f753-38d4-9933-7d4c84c815a4 | -25.3573 | -54.25244 | 2025-11-06 12:42:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d696c9e8-c732-35ce-be64-00a2c3c2186e | -25.16569 | -52.34559 | 2025-11-06 12:42:00 | TERRA_M-T | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 05c96b1e-026a-3fa0-89ae-b280c4883428 | -25.17644 | -52.34693 | 2025-11-06 12:42:00 | TERRA_M-T | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 9d29da68-cb0c-3f93-8066-da92d077c87e | -30.9538 | -52.32287 | 2025-11-06 12:44:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 9.7 |
| 13082224-7b33-3ac1-a870-27662ad55763 | -29.22933 | -51.33415 | 2025-11-06 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 44aeed9b-5269-38e1-9ce8-1d9d86d44b2c | -27.7628 | -50.07348 | 2025-11-06 12:44:00 | TERRA_M-T | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 124e7891-4861-31c6-91ac-6e34ef1411ec | -30.3122 | -51.92882 | 2025-11-06 12:44:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 62.2 |
| 600add08-0945-3802-82c6-597ffa606884 | -29.03449 | -51.17028 | 2025-11-06 12:44:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 7be77e29-c803-382a-8840-5d7083e25a19 | -30.31401 | -51.90996 | 2025-11-06 12:44:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 28.3 |
| a0ea98ad-1176-329f-be27-ff273cc56202 | -30.95206 | -52.34145 | 2025-11-06 12:44:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 24.2 |
| 73cb48ec-2dac-3a0b-a51e-c85e733fe639 | -27.94423 | -52.917 | 2025-11-06 12:44:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 88ff6f89-1876-382c-b520-680a17981522 | -28.9379 | -51.54119 | 2025-11-06 12:44:00 | TERRA_M-T | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 107c37b2-8c6c-3feb-8c4a-3d31c03b117f | -5.9231 | -41.3298 | 2025-11-06 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 8b00b9e3-6b14-3b57-a610-c7297ee98fa6 | -5.9234 | -41.3056 | 2025-11-06 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| a6af529d-eadb-380f-bc7d-72379c033dba | -5.9234 | -41.3056 | 2025-11-06 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 4cc98c48-7979-34de-9af1-eb4d141e560e | -5.9231 | -41.3298 | 2025-11-06 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| ca8a30e3-eb42-38c3-a3bd-13b3aa11ad9b | -4.8873 | -39.375 | 2025-11-06 13:10:00 | GOES-19 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 88.6 |
| b479f8b6-b5c0-3bb5-9d9d-8efe3abac37a | -5.1533 | -41.2468 | 2025-11-06 13:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 7c1eeeb8-a344-37ee-81f6-f1c161f11fdb | -5.9234 | -41.3056 | 2025-11-06 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 09c76ae4-ab17-3b64-8f1c-fc1cc9e12c02 | -5.9231 | -41.3298 | 2025-11-06 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 8fdaf421-ed07-36af-be64-de4822d983de | -5.9234 | -41.3056 | 2025-11-06 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| f147fd07-7cda-370a-bf33-360ac1ca0cd9 | -5.1533 | -41.2468 | 2025-11-06 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 1c08bdbd-c17f-3ed7-bc2a-d0c7b61a5555 | -5.9231 | -41.3298 | 2025-11-06 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 0bdc75e5-0678-3955-90d6-1b1147fdc8af | -5.1345 | -41.2482 | 2025-11-06 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 0fd0c6e0-7119-3012-807a-03be588246cc | -5.9231 | -41.3298 | 2025-11-06 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| a642bed1-48b1-311b-a288-0a8cbdf4a001 | -5.9229 | -41.354 | 2025-11-06 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 4807aac5-25bb-3b83-a912-ebf5e888be50 | -5.9045 | -41.3072 | 2025-11-06 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| a24caeb7-0f7f-38ef-ab3f-536f3dc39fcd | -5.9234 | -41.3056 | 2025-11-06 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| a86a5e23-f872-3452-959e-7cb28433a982 | -5.1535 | -41.2226 | 2025-11-06 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| ff572243-b6c1-3b82-9f9a-ff2d51781c9c | -5.9422 | -41.304 | 2025-11-06 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 43aea702-32ee-333a-b85e-a20bd24f200a | -5.1533 | -41.2468 | 2025-11-06 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 80163c7a-eeb0-3e21-a9aa-91d84c904218 | -5.1345 | -41.2482 | 2025-11-06 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| a952c6e1-652d-3a63-9e43-511b8a146eae | -5.9234 | -41.3056 | 2025-11-06 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| ff8ceb48-1d07-3ccd-8154-4c72756b66ae | -5.1345 | -41.2482 | 2025-11-06 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 3f2ff02f-a2a4-3ae5-a133-cdc7ea832715 | -5.9043 | -41.3314 | 2025-11-06 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| c39fb50f-a948-31f8-96f8-81574b4392b9 | -5.1535 | -41.2226 | 2025-11-06 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 790e514f-a4b1-32a0-b8c5-5692b7906974 | -6.456 | -39.1091 | 2025-11-06 13:50:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 99.6 |


[Clique aqui para ver as próximas entradas](README28.md)
