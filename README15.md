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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf279923-7883-3805-a417-6993bf4cd23a | -15.18914 | -41.72213 | 2026-09-06 04:04:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ef0929a-b2a4-3f08-b64e-bcd6d39bccd9 | -14.91842 | -44.66821 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f8d2fd19-1778-343d-bd4a-420298e81117 | -13.7474 | -51.66839 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b46af06-8084-38c1-b959-6f5928cab2da | -15.32838 | -43.64836 | 2026-09-06 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3233d0a-58af-3544-bad0-52a2cacddd19 | -16.39736 | -49.20198 | 2026-09-06 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 336a8bd4-4376-3266-a6cf-3d6eef454764 | -14.91757 | -44.67294 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 40ea7029-e7d4-3f1d-bfe0-e1ba32cfb49b | -18.3091 | -40.92386 | 2026-09-06 04:04:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 348d8628-8b31-33f8-ae97-a73b76e37e6f | -15.36725 | -42.12015 | 2026-09-06 04:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e323e295-2b6d-3e4e-9e84-123a3f408cf5 | -14.91377 | -44.67446 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 5d4b3bd7-620c-3b53-a10d-1b7a065b4f23 | -14.91459 | -44.66971 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 39579f5f-18b5-32c0-94c3-a4b4b5c6cf14 | -17.43087 | -40.02534 | 2026-09-06 04:04:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 282ea08e-4a63-3a9f-a3bf-c23f949824ab | -13.74835 | -51.66378 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ec21d53-2a92-3dad-aaa2-8cd3309db6a5 | -17.94425 | -50.36517 | 2026-09-06 04:04:00 | NOAA-20 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e3117a-3bd3-3363-80be-c4e3b73a0ad8 | -14.90621 | -44.67299 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44084d28-3716-3453-9c5c-b68aa8016ee8 | -13.7553 | -51.66053 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e10b6a78-3952-36d4-8335-452466b45853 | -18.16064 | -39.67354 | 2026-09-06 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d9388008-bac1-3bb5-9084-1f7b0fd17032 | -14.8688 | -40.90563 | 2026-09-06 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06f71d4b-59cf-3bd6-a5a4-0585a8907d1e | -13.75434 | -51.66517 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d47d2ac-75ca-30e3-a853-49870c822b64 | -17.43144 | -40.02164 | 2026-09-06 04:04:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 22768795-594b-384f-a85b-4665f4aa6a29 | -15.71269 | -43.69758 | 2026-09-06 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46e374bb-afb7-3750-938c-e5ba5096904d | -18.20592 | -39.64973 | 2026-09-06 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afc5d254-5887-308e-9fa6-eddc8b953090 | -14.86435 | -40.91219 | 2026-09-06 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7db29eb7-daa2-3ecf-bd60-dcb0d32f58d0 | -30.80424 | -52.80965 | 2026-09-06 04:08:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 1e6ac3c0-160d-3129-867c-cdb0b88c5f89 | -5.1423 | -56.2703 | 2026-09-06 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 31ef6a7a-dde3-39a7-b45a-f54ec9e88620 | -5.3645 | -56.0447 | 2026-09-06 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 33adcce8-a5a5-35a6-8881-91915e41cebc | -5.3646 | -56.0249 | 2026-09-06 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 81186f5e-16fc-35fa-b3c9-d43959b89bfd | -5.3462 | -56.0256 | 2026-09-06 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 53bfd96e-f785-347b-a3fe-e5b7c095b317 | -5.1423 | -56.2703 | 2026-09-06 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3053d1fb-ec8d-312f-85fb-bf5995dfc5b7 | -5.1439 | -55.9543 | 2026-09-06 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b0b5bec6-dcfe-3041-be61-2fa8b0c836d1 | -5.3645 | -56.0447 | 2026-09-06 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6723f20e-f9c4-3ed0-bd2d-136e73eed862 | -5.3646 | -56.0249 | 2026-09-06 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| b1f0d38d-2afc-3cfb-bbb1-ea0392be093a | -5.3645 | -56.0447 | 2026-09-06 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a328c4e6-0200-347a-94b7-75cb64d3c3bf | -5.1423 | -56.2703 | 2026-09-06 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5ae4c01d-d7e9-3a7d-b52e-452d5e8e0c4b | -5.1439 | -55.9543 | 2026-09-06 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9bf5d254-4244-3515-96f0-50a7288b5190 | -5.3646 | -56.0249 | 2026-09-06 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 2a979d14-c76b-387c-bfaa-9abac488baa2 | -5.3645 | -56.0447 | 2026-09-06 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 45d51bbb-2e2e-3d0b-895d-9f8d92d494ca | -5.1423 | -56.2703 | 2026-09-06 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5fc4fdac-33ec-36c1-b998-334eaa8929f2 | -5.3646 | -56.0249 | 2026-09-06 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a7bd8558-2aa7-38eb-aa23-b72f92b182e0 | -3.2443 | -47.24933 | 2026-09-06 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e2b501c-9d67-32e8-99cf-5309f5a67a02 | -2.86121 | -50.47215 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7b6072-bd09-3c64-a70f-6fb70ed46cfd | 4.19726 | -59.95711 | 2026-09-06 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94b35ffc-2db0-377a-8a15-c0fb569cf3e3 | -2.86612 | -50.46235 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69627149-15ec-3d34-893f-0d131bec51c3 | -1.62361 | -55.16843 | 2026-09-06 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 391b5441-5c78-3004-81c4-64e530a77231 | 2.3684 | -50.76408 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c56962b-b338-3c3d-b6d2-c4dc36577427 | -3.22407 | -48.61254 | 2026-09-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554c6bf6-ffd1-3ce9-91c7-40d9534823e5 | -1.3878 | -55.17809 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d716871-4dd1-32ff-aae6-c3b8f2b4dd99 | 2.37177 | -50.76357 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c35db3-2e60-3df8-b221-045445d6b6c7 | -1.42665 | -53.76158 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 500046da-c1a9-3ae8-9e87-951a883f3380 | 2.38391 | -50.76488 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35e7c59a-19a2-3d10-a390-77de1cfb67f9 | 2.44809 | -50.77726 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74e3ae21-8c3d-3654-9bb8-d63f9441362e | -2.86336 | -50.45841 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff460428-08a4-37b9-87e7-5f40d566202b | -2.85735 | -49.53579 | 2026-09-06 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a028786a-6e65-3d17-a466-d2e378e7d908 | -1.39241 | -55.17516 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2988778d-5e62-3692-a49e-cbd3189d72be | -2.30112 | -48.58916 | 2026-09-06 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8eab272c-8ede-3780-8af4-168ba42819c3 | -2.85845 | -50.4682 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4038bda9-1fad-3ad0-9b33-c2aa82ec3701 | -2.86175 | -50.46871 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db0a2ea-3692-304b-9be6-7431f31823b2 | 2.50184 | -51.68573 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ccf3f21-c717-3b54-a6c7-cbd77b58f3e0 | -1.49158 | -54.81656 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e557885-020c-3231-8ad5-e6ab61d79a7e | -2.89731 | -48.27537 | 2026-09-06 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ae6055-8f3e-34ea-809d-ccfb5306b64b | -1.70746 | -54.97813 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eced73a-89ec-3d86-a8e2-0c43fabf6c55 | -1.84677 | -47.94616 | 2026-09-06 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950069f3-1661-3389-9c2c-fe467b38d2d1 | -1.6671 | -55.50127 | 2026-09-06 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b417a3-40b7-3951-8b59-0fbd960d971b | 2.44753 | -50.77366 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10a54eba-7af2-3bc1-830d-935a6d775c69 | -2.86666 | -50.45892 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e723605-b78b-3a9d-b1dc-632b86a057a0 | -1.2052 | -47.76187 | 2026-09-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f1429a90-e4aa-3dd9-88a6-53c5d8984ff6 | -1.3913 | -55.18229 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8b9b23e-f4bc-30bb-bf88-0a6d32abd4d7 | -1.18741 | -53.82672 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a4da60-4b3e-3301-8f0d-0c19f8dab1c4 | 0.8306 | -51.18321 | 2026-09-06 04:44:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 549ab5c6-aa50-345d-9997-48bb51310d6a | -2.86559 | -50.46579 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37598388-5651-358e-8ca2-5cad837e9b34 | -2.42781 | -48.63813 | 2026-09-06 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd038c53-d2f6-33af-b543-45ad188a27cb | -3.60368 | -42.97314 | 2026-09-06 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a2cec9-3bcd-3d40-a0de-0cf12fc6fc2b | -2.25081 | -53.76759 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 704d853d-1f8d-3ba5-9225-1d1c98f47d92 | 4.36216 | -59.75321 | 2026-09-06 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31bac22-9a59-3d17-bb3b-75acc7843207 | -1.39695 | -55.17587 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70af398e-c93a-301c-b94f-2b7c408b1f48 | -1.39174 | -55.18237 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcc9854a-6e5d-3d5a-88e3-df53c08fa444 | 1.29004 | -50.79299 | 2026-09-06 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51340ce0-5bcd-360a-abbd-858ea1d2308b | -1.38835 | -55.17453 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1629897c-2b39-3942-8b4b-1b4e29ae97fd | -1.39232 | -55.1788 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e547eef-557a-33d3-9f3b-efb8eda47455 | 3.04427 | -60.87238 | 2026-09-06 04:44:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5271caf-ab9f-3962-9f85-a8f39572d96c | -2.8755 | -50.46731 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b034ea0f-c2cc-358a-89c7-fec23f1275ee | -2.02305 | -52.10538 | 2026-09-06 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d3dfa1e-eb15-39d2-926b-ddba8994b797 | -2.86505 | -50.46922 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca695967-da03-35d4-a5e3-00b239880c78 | -2.25148 | -53.76326 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6669e01-5e2e-3331-add7-e4602763abba | -1.3929 | -55.17525 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c928f2ef-ffae-34ac-9992-e6c466d1a9bd | 2.36896 | -50.76768 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb551023-2c07-3d07-a7eb-0e5e82ec7ca8 | 1.20876 | -50.92643 | 2026-09-06 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fee5a2b1-22d8-3992-9a77-27fc4e8a1140 | -2.45804 | -49.37 | 2026-09-06 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16642646-135f-3a2f-89c2-3af95db67b02 | -2.86282 | -50.46184 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20f3b6b1-6622-396d-89da-95eb8eb289ee | 4.36147 | -59.74849 | 2026-09-06 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9c1da5c-966c-3d4d-90a8-2fa993bed50e | 2.37998 | -50.76179 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c7f89ca-651f-36a8-80ac-0167b232b279 | -2.87603 | -50.46387 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8fd1766-2d7a-3a09-b4ba-a61a8a551395 | -2.87657 | -50.46045 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532b4b9b-b8bc-3e42-865d-51eef6982a6d | -2.85952 | -50.46133 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb642e6-970a-370e-aef0-ecabb35720d0 | -2.87327 | -50.45993 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c5338a9-cd4a-3dbd-9174-a96229b3d793 | -2.86943 | -50.46286 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb804d7d-ed00-33bc-a74e-15c81ebc342d | -1.56278 | -55.78436 | 2026-09-06 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8ed8980-933c-30f7-810a-ad7681b3bc65 | -1.39701 | -55.17224 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9658504-b184-3ad6-a2e5-d8468260f64e | -1.56216 | -55.78824 | 2026-09-06 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2773ad1b-731e-3f2f-a9f1-be62efb98c77 | -2.8722 | -50.4668 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3161aca-ccfa-303c-99a5-4c6960f750b3 | -2.24781 | -53.7627 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
