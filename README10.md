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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0e569f4-8217-35cf-ab65-e7c7e38e4c14 | -15.88692 | -43.45393 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 239f9bd2-45b3-3115-958d-663345d9e4cc | -21.71602 | -47.11346 | 2025-12-27 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d2ff575-444a-3c56-9db2-715f19626282 | -17.42277 | -43.82655 | 2025-12-27 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8814dddc-a6c2-3824-becd-4013903ad6e7 | -19.19935 | -48.15655 | 2025-12-27 04:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03e5e014-4e37-3fab-a6ac-9843e6fb8440 | -18.31022 | -46.40223 | 2025-12-27 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0b0e0f1-eb51-39f5-9224-c8ac4f848090 | -20.18417 | -43.64103 | 2025-12-27 04:23:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c9eba690-281d-3af8-a17f-f138b0c95469 | -18.44385 | -48.73661 | 2025-12-27 04:23:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5894abfe-4650-356c-bfc9-1cc09291d5b1 | -15.91344 | -43.22737 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6be2a4e9-810e-38d4-a6f3-0919a89e3d17 | -17.19779 | -47.02649 | 2025-12-27 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77fc21c2-bc17-31f9-8d34-e90fb6443088 | -18.90648 | -46.59269 | 2025-12-27 04:23:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8332fa94-80ba-39c2-b877-d2102c2834e1 | -21.71269 | -47.11285 | 2025-12-27 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4adc3ca8-0dd7-3617-948c-4353ccfcfb06 | -18.31355 | -46.40281 | 2025-12-27 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf2a4dc1-bcaa-35f8-af42-40f606d5157c | -15.88749 | -43.45007 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9f5e1e88-cff9-34b5-ac2e-87551329e969 | -21.71329 | -47.10913 | 2025-12-27 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9372216-25af-3b7a-822e-286615e9458d | -29.97926 | -51.20358 | 2025-12-27 04:25:00 | NPP-375D | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6f2c60cb-df86-3a8c-beef-f9c48131c936 | -23.82429 | -47.29779 | 2025-12-27 04:25:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b213bdef-c9f1-318e-b8c4-cd964ce463cf | -23.59821 | -46.77555 | 2025-12-27 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fefc364c-cfb2-38a3-8b04-24d786f1df6b | -22.93924 | -43.39256 | 2025-12-27 04:25:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 271e2b6f-603e-328f-9eb4-d80e841d4e03 | -23.76123 | -46.76505 | 2025-12-27 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42a007e1-3c8d-33ee-961b-6fbcd0406580 | -15.8955 | -43.4523 | 2025-12-27 04:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3122a76a-e5fb-3b76-a763-068d3d5c8365 | -0.0828 | -51.2738 | 2025-12-27 04:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 55772b4f-9ea7-3c51-a523-d73d8a019d7a | 2.5247 | -61.0009 | 2025-12-27 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 98a52233-5eb7-3c61-8989-b7b4126c31e8 | 2.5247 | -60.982 | 2025-12-27 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4122ecd3-6abf-3ac0-8c22-be25ce640713 | 2.5064 | -61.0012 | 2025-12-27 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9220a8a3-361b-3f21-a312-a3e418e3ce6c | 2.5065 | -60.9822 | 2025-12-27 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 806fd45f-24ac-378e-ae08-e13bcf412a3f | -3.90172 | -42.55801 | 2025-12-27 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| db80ed26-cf74-355a-9bca-1fff547d4472 | -3.90616 | -42.55868 | 2025-12-27 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ee48a2e8-b4fb-39be-8032-8872ed9c061d | -2.89914 | -52.59339 | 2025-12-27 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301736d6-52b0-35b3-9ec1-01359eac0af2 | -0.08804 | -51.28181 | 2025-12-27 04:38:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2fd7e6ac-8e87-352e-9c2f-0fdde6d43e9a | 2.52403 | -60.99875 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a412a495-f194-3823-aa53-2bfed74981b8 | 2.51503 | -60.98667 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| cbf30f9e-bb5d-315e-acf7-5031abd2eed2 | -2.90167 | -47.81639 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f6f5512-9f8a-3a76-bcc5-9dd957953b7d | -3.30943 | -47.38144 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66725638-5deb-34ef-a975-48159d1debec | 2.5208 | -60.98745 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3730f9dd-2413-3711-a7af-c7d8154c6512 | -3.31732 | -47.37524 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc8a352-1e95-3165-b56d-b259b259546e | -3.76607 | -43.55641 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| beb00300-a0c1-3379-a8c3-5e4094672a53 | -2.85753 | -52.80108 | 2025-12-27 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f31b9330-3fdc-329c-9e2d-726c833c6e1b | -3.65136 | -43.51661 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0165dd00-9729-3769-a760-04cb4343e516 | -3.31281 | -47.38196 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30454be3-3e86-3849-8ed2-5de166b52856 | -3.32492 | -45.99997 | 2025-12-27 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e841ffc-7abb-35bc-8995-2035095361da | 2.51382 | -60.98864 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cca893bd-538b-3ce7-b5f6-c96e63aa0a36 | -2.45958 | -47.77655 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5295bea5-a2fc-3560-a462-cca3fe250974 | -3.66078 | -43.51035 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9001ed9-534c-3d07-ba81-ef331cddf5ca | -2.9643 | -46.78585 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a4d175b-c635-3abb-8975-aa6b9dcfd9b0 | 2.52273 | -61.00072 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d898c04d-0dfc-317c-b454-d3113fc953dd | -3.31 | -47.37782 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a80c8bfa-c3a0-3bf8-a570-dcbe4c0874e0 | -2.60762 | -47.31465 | 2025-12-27 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6783de0-4339-3801-9827-211f0d052445 | -3.77022 | -43.55697 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6b87bcb-15b3-384d-8771-3c9f364427aa | 2.51287 | -60.98205 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 95b3a422-ce70-3675-ba20-1b48bcf63dae | 2.52177 | -60.99408 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| da7fbe8d-85a3-3c75-8f72-240453cb09d5 | -2.46291 | -47.77705 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db9e7d26-5736-32f0-b163-48ed1163badf | -3.90239 | -42.55366 | 2025-12-27 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ebe81663-03cb-3c8e-8508-8db7537eed18 | -3.31967 | -45.98676 | 2025-12-27 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10972665-e236-3546-be99-3b98c554346c | -2.6871 | -42.75294 | 2025-12-27 04:38:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c061200-75b2-3a29-9229-0c2025ef4729 | -3.65191 | -43.51286 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba667ac-764e-3113-b728-8ac2bf788dbc | 1.83486 | -60.87627 | 2025-12-27 04:38:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fc99dfc-45db-3db6-94a6-963b4e597542 | -3.90509 | -42.55667 | 2025-12-27 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 28059fbf-713e-3742-82d9-0e2a8bad14b8 | -3.65606 | -43.51348 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c77aa42-9e80-30fb-8440-5799f3632b33 | -3.30662 | -47.37731 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97d3b28c-fba0-301f-becf-c84a856b275c | -3.31338 | -47.37834 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e674ccc-b0d1-3f3b-baa8-70f6038b19a8 | -3.97356 | -43.40803 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85895da2-66eb-3a85-a30b-0dc49604bc2b | -1.47448 | -54.20145 | 2025-12-27 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35802d26-32b9-3c74-bcbe-fda5a15b80ea | 2.52302 | -60.99213 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f666c481-29fe-3ff9-a1f2-b71a50c12412 | -3.7608 | -43.56333 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c37f692a-1cf2-3fc1-9d2a-f8becb290aef | 2.51479 | -60.99529 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| bee4fc13-7c5f-3e89-bde8-4e4a94478fc2 | -1.4787 | -54.20217 | 2025-12-27 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0ab7fa2-f730-3572-b492-dc90958fa53d | -3.65717 | -43.50605 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9905267-2734-39ab-9507-a3e5c7f030ff | -2.45516 | -47.78299 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 453849dd-b05c-35db-a026-a11025bff7f1 | -2.45903 | -47.78003 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2eaad166-dd5a-3788-9945-7807e891837d | 2.51603 | -60.99327 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e8a6ea9f-483e-3e01-beda-c506bbb2b8a0 | -3.31225 | -47.38558 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0532d6c2-890f-3d4d-977b-b8616d30094a | -3.31676 | -47.37886 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6a36c78-fa8f-37da-9de3-fb6071e659b5 | -3.32261 | -45.99135 | 2025-12-27 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 333cd8af-2986-3f34-9611-e71bf5d692fd | -3.31563 | -47.3861 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd923aa4-84d6-3785-be3b-227eee6478af | -3.32555 | -45.99592 | 2025-12-27 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4f0c59f-3a98-3f0c-bfc7-770ae7ae09ea | -3.76551 | -43.56016 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 61078372-eb2d-3763-a6ac-34d8b9376654 | -2.45625 | -47.77604 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b9c46358-8755-378b-a36b-dfb4b49ebd8f | 2.51704 | -60.99991 | 2025-12-27 04:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a8d1543a-cf82-3ae5-b691-1dd8a90fb41e | -3.32324 | -45.98729 | 2025-12-27 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 644fdf10-89a1-3939-b609-e75ede9e6ae5 | -3.90064 | -42.55601 | 2025-12-27 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 6d8aa2b2-f937-362a-b6f6-fa9c56809339 | -3.31394 | -47.37472 | 2025-12-27 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e604da03-a10b-33f9-8d40-eee25175fa98 | -3.76495 | -43.5639 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28d132da-7118-38ae-aa81-90ef3fef0dc7 | -2.8954 | -52.5928 | 2025-12-27 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfaee88a-5f26-3c78-9303-60265f0549a5 | -2.13919 | -48.0013 | 2025-12-27 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253bf638-3774-3e96-b7a0-61962bde05c7 | -2.4557 | -47.77949 | 2025-12-27 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 600d754d-bc59-34f8-b9e8-0d683013e157 | 1.82797 | -60.8773 | 2025-12-27 04:38:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 049575fb-e47e-3068-baa4-904c3dc2cec1 | -3.76025 | -43.56702 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03949827-1bd0-39a2-86a1-3fd103e6e6bf | -2.89612 | -52.58839 | 2025-12-27 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 010edc2f-31a5-3cf9-84d6-9ecb07a2edbf | -3.65662 | -43.50975 | 2025-12-27 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a95fdc1-4168-3087-ad06-9622e64e9d56 | -2.68527 | -42.75189 | 2025-12-27 04:38:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d81591-ea28-376e-b69f-8aa66c827687 | -2.85827 | -52.79656 | 2025-12-27 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de2c3384-cb38-3953-98c9-c45364c031f2 | -2.13587 | -48.00079 | 2025-12-27 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ebb8f65-50eb-365b-b148-c15a2fb5376d | -2.89888 | -52.22691 | 2025-12-27 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1948d506-3d2c-3f2e-8594-34f49eb78b0c | 2.5247 | -61.0009 | 2025-12-27 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2d746b24-91a9-3a40-a5c6-e3d017d41ec2 | -10.4889 | -44.9235 | 2025-12-27 04:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 96e50d63-46f5-33fa-8a73-e1d0efac54d1 | 2.5247 | -60.982 | 2025-12-27 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 74b9efc9-a631-3741-863c-b598827103d7 | -0.0828 | -51.2738 | 2025-12-27 04:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2282d455-5863-3f67-b977-707640a8eccb | 2.5065 | -60.9822 | 2025-12-27 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0e035984-4e20-3d8b-b24d-8b466a06b05a | -12.17483 | -38.81685 | 2025-12-27 04:40:00 | NOAA-20 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de4b1090-81b7-3c68-988b-3c818b5fd798 | -6.63726 | -39.29997 | 2025-12-27 04:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
