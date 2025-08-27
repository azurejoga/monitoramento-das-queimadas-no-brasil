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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daec9e16-c200-339e-92c4-8263deed8753 | -20.67805 | -47.54166 | 2025-08-27 04:29:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82d15a9f-608f-3678-8ab7-9237a8b0cab7 | -20.39816 | -46.72894 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4db28cad-63f3-3847-8a78-a5f39eedc1e4 | -20.11012 | -44.32645 | 2025-08-27 04:29:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 10db149a-bfbf-388e-849e-cdaa31f64f68 | -21.00559 | -44.17752 | 2025-08-27 04:29:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69496f8e-7431-37f5-ab57-30806ca45398 | -21.35132 | -46.89576 | 2025-08-27 04:29:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| efe98124-3519-399b-aed7-a0e7f92b5cf5 | -21.7202 | -46.80881 | 2025-08-27 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6cf9c77d-013c-3b7f-a512-c8202475dba0 | -20.5406 | -43.83985 | 2025-08-27 04:29:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e46640a8-fb8b-3812-aeab-3991335e2bd4 | -21.57958 | -47.47933 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b92a543-fb0e-318d-b14d-51114cf23644 | -23.42626 | -53.72765 | 2025-08-27 04:29:00 | NOAA-20 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99a361f8-3c53-3471-93a5-9ecb514faf76 | -20.87228 | -55.0049 | 2025-08-27 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ce87919-54bf-3918-900b-a8ff47407305 | -20.98413 | -40.9563 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f386f737-1a38-3822-a4a3-807593f105a1 | -22.16221 | -47.07228 | 2025-08-27 04:29:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf3168f2-2ac5-3522-9d3f-b542991af842 | -23.54947 | -54.65197 | 2025-08-27 04:29:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fd4e3d4-331e-3712-a81a-6710e6e604e0 | -20.98447 | -40.95319 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd853404-19a1-3988-9752-5886afb14dcc | -20.53499 | -43.96677 | 2025-08-27 04:29:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8850f76e-25d6-3ab2-b352-f00c50a8aa64 | -20.75586 | -44.76323 | 2025-08-27 04:29:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 9d2781a1-66ee-38cc-96fa-7ee987b46162 | -9.4065 | -60.4941 | 2025-08-27 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a603ac12-9229-3f6b-9356-79e2a1e6d36d | -9.4064 | -60.5133 | 2025-08-27 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 26c4fa51-c0c2-3278-bf48-ddcb1d73b8cf | -8.9664 | -65.961 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7d7760e6-2e80-3dc4-8268-2f114c14544c | -8.9296 | -65.9248 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7a756407-bb6f-3eca-b3f6-6c7da54e6305 | -8.948 | -65.9429 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 2d1d45cd-7955-32f8-81ff-27d67a0a2e36 | -9.1009 | -49.5621 | 2025-08-27 04:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f6be0b7a-40a2-3987-a863-10ce6e93fb4e | -6.8412 | -58.9746 | 2025-08-27 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3ecf58dd-2d15-3baf-b372-e1bd1db1972e | -8.9665 | -65.9424 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| ad06ecaf-03bb-36e9-a6ca-804e1a360aee | -8.9295 | -65.9435 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| badb2796-fa79-3ccd-8259-7e5ba523324b | -8.9479 | -65.9616 | 2025-08-27 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 259d502e-1572-32cd-84a6-64ccda3af433 | -9.4062 | -60.5326 | 2025-08-27 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5943e506-f0ab-31d9-9d50-c9d6927694ca | -6.8413 | -58.9552 | 2025-08-27 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8d9b13c5-8b23-39e8-b5e3-6b0553e7786e | -31.26031 | -54.24289 | 2025-08-27 04:32:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| f6f6eaa0-734e-3906-91d6-d6107cb18d6a | -8.948 | -65.9429 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 441e70ae-0cac-367d-98c4-28e64c63af6a | -8.9479 | -65.9616 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 4ab042e2-f60a-3ea3-a0aa-acc68b1940e1 | -9.4062 | -60.5326 | 2025-08-27 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ec740fd7-0916-339f-a95a-b06403ec42f4 | -8.9295 | -65.9435 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| dc400bcc-7c22-3756-b56f-5a5e1546cfde | -9.1529 | -59.5609 | 2025-08-27 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f5ad53a8-3f1e-3247-bb60-23b5101f0b5d | -8.9664 | -65.961 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b5a7c7a4-962f-35fe-bd99-c0ac04098ccb | -6.8413 | -58.9552 | 2025-08-27 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5fbed445-6061-367b-a09e-bfa071c22c42 | -8.9665 | -65.9424 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 33c54624-6f20-379b-bb3f-757eea450d77 | -8.9296 | -65.9248 | 2025-08-27 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| de2f1d8d-4b64-300e-a1b8-eaf96d6a83da | -9.4064 | -60.5133 | 2025-08-27 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d4fa7fae-6eaf-3be6-a7b0-2ff5b74a2b69 | -9.4065 | -60.4941 | 2025-08-27 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 60264aca-1147-3c5a-877c-c05dc9dd9874 | -10.7977 | -47.0601 | 2025-08-27 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2d2afb13-a800-37a0-82b4-9db883dcee91 | -13.0674 | -46.3153 | 2025-08-27 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 039a7fe5-3250-30d3-a2a2-6161ee18f7bc | -10.779 | -47.04 | 2025-08-27 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1d986aec-92e2-3256-8027-5176cf6e1089 | -6.8413 | -58.9552 | 2025-08-27 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d2538551-9605-3fa4-9af3-967e7b9f2a60 | -10.7787 | -47.0624 | 2025-08-27 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f7e3e7f4-e3eb-3ae2-aee2-d913b27ab4c6 | -13.3838 | -46.9017 | 2025-08-27 04:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4459f3b0-87be-3275-a4e2-430636abb41a | -9.4065 | -60.4941 | 2025-08-27 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5ca6d390-bcad-3fed-859d-936ca35f0bd8 | -9.4062 | -60.5326 | 2025-08-27 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 13a04a53-f751-3fe9-b7a0-cb238b3b6ba5 | -9.4064 | -60.5133 | 2025-08-27 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3dcad569-187a-3b26-8d82-c7a17044f20f | -10.2743 | -64.4907 | 2025-08-27 04:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 361adfab-a74c-3717-a3eb-58c1a3853d24 | -9.4064 | -60.5133 | 2025-08-27 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 2098e41c-1a0d-3a6d-afcd-6def95566afc | -8.9296 | -65.9248 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 61f8f50a-cfc6-3ab6-b340-9a202e43bf0a | -10.7974 | -47.0824 | 2025-08-27 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 32543322-c73b-3369-8223-c9f6ba942554 | -10.7977 | -47.0601 | 2025-08-27 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 9e230e8c-c821-32d9-b8a5-3bd3d8d7e741 | -8.9479 | -65.9616 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 87e82596-ea2e-3b44-bf07-e0da816c806b | -10.7787 | -47.0624 | 2025-08-27 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3d0597bf-1cad-3519-ab8a-3e802bc5e0c7 | -9.4062 | -60.5326 | 2025-08-27 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 34283699-e971-3e84-89ed-0daabc0172f7 | -9.4065 | -60.4941 | 2025-08-27 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 77d66df1-cd86-3717-9045-09e680d4d49e | -8.9665 | -65.9424 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6ddac3ec-6212-3e06-bd25-d8d7f07e919b | -8.9664 | -65.961 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 76c90d0a-1e16-371d-a408-67ceab9e8434 | -6.8413 | -58.9552 | 2025-08-27 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 2b815126-e49f-3e86-beea-471c95a51bac | -8.948 | -65.9429 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 2b446674-ea17-302f-ba6b-d32029d82c3d | -8.9295 | -65.9435 | 2025-08-27 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a8d30e86-0a85-3e69-9aae-b29074b2b71f | -8.9479 | -65.9616 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.5 |
| a1dda56c-2ee9-33cf-8cf8-c5900d95f047 | -9.4062 | -60.5326 | 2025-08-27 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6b9a2ebd-e23f-3006-adc9-beed91cf81e2 | -8.9664 | -65.961 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d92130aa-3549-3dc8-81c4-25797da8fa4a | -8.9296 | -65.9248 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 58be7c15-d380-3940-91b8-13c6209e30a3 | -8.948 | -65.9429 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 162.9 |
| ec46ba5f-0768-3941-b3dd-265828a90634 | -8.9665 | -65.9424 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| fb770374-1e71-332f-9f35-1115d5f2e1bf | -8.9295 | -65.9435 | 2025-08-27 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a073e086-3f81-3c06-a9b9-83edb2bd3e33 | -9.4064 | -60.5133 | 2025-08-27 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 72744f4a-cff6-380b-ab01-1a4942b3db54 | -10.7974 | -47.0824 | 2025-08-27 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 05bbe88c-7716-324e-96c1-468f4a4be7d3 | -9.4065 | -60.4941 | 2025-08-27 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 13167024-b85a-31c8-8e62-1a29c8526668 | -10.7977 | -47.0601 | 2025-08-27 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 36773898-991b-3e30-8550-ccddc18f82fd | -4.79405 | -47.27603 | 2025-08-27 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73759f32-74eb-3930-a1e0-7d0398f14b70 | -3.39212 | -59.4558 | 2025-08-27 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f501189d-aec6-3402-88bf-f5640bc360c6 | -3.42597 | -49.04321 | 2025-08-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a602f3a-6e6f-3c31-81ca-35155e070536 | -3.19831 | -52.2564 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2cfbcafd-40d7-3557-958a-267f547c2eb6 | -3.38273 | -59.68527 | 2025-08-27 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e428c8a-21d3-35f2-963a-648ac00665c2 | -2.58705 | -51.92216 | 2025-08-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc8df222-5d56-3ff2-bff0-07e5b19c2505 | -5.6292 | -45.72562 | 2025-08-27 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 019ac88b-557e-319e-822c-36d62ef52966 | -3.98475 | -51.05562 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701cb24e-b44b-3f0d-a5b1-7f352764a8fa | -3.8022 | -51.19163 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b97dbf0c-8749-39b1-b3c5-9382260fc694 | -2.92066 | -48.3072 | 2025-08-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd479224-efdb-3ed3-ac58-45233199a702 | -5.23701 | -56.06249 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e157dd5-3b1c-3c01-8fa1-fb023a1d9dca | -5.76363 | -53.7636 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7d6f29-7e7e-30e6-a88c-95b8734cdf02 | -5.22872 | -59.99785 | 2025-08-27 05:16:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06810c54-471d-3f7a-b86a-4ca82206a49e | -4.96248 | -55.81664 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc263265-75ec-34f7-875d-ee89def6940c | -3.80311 | -51.26402 | 2025-08-27 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fad2340b-573b-317d-9130-650e907d2ac4 | -5.22816 | -60.00139 | 2025-08-27 05:16:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a3da3c0-a353-3a80-a5d2-550df6f6593a | -5.75956 | -53.76299 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d323cc-b762-3f20-91b8-84d2c640174d | -3.4265 | -49.03962 | 2025-08-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ce6f962-2fbe-39c2-87f6-11aecc9cba91 | -3.42545 | -49.04676 | 2025-08-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c1f2f0b-d67e-3dfc-a515-dd75bb26a910 | -4.79281 | -47.27594 | 2025-08-27 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| feaa167b-b669-3481-b4f7-c9c0eb01e427 | -6.578 | -47.38157 | 2025-08-27 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ca25672-c9f6-3353-8cff-c796cbd67c91 | -5.23718 | -56.06104 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24b57635-3d86-316a-a831-d7c1da1dbfbb | -3.97915 | -51.06046 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 517063be-8804-35e0-863f-fbd6e6a9cd39 | -4.55362 | -55.96028 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d6bf36-0d60-3fd8-a68f-213502e1ad8b | -6.57735 | -47.3866 | 2025-08-27 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a1847e7-bab7-329d-90b0-9b22d1f595ae | -3.59297 | -59.66777 | 2025-08-27 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
