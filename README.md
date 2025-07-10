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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2a5144f-f7eb-3129-8e4a-e6ec1537c461 | -13.3568 | -52.9242 | 2025-07-10 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 193d128f-fb18-324d-97c3-37535ea5cf91 | -11.3619 | -48.6923 | 2025-07-10 00:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e89fb702-7246-39e8-b1cc-dd0b370c5443 | -6.6808 | -46.2961 | 2025-07-10 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b021feec-b958-3fb0-bbde-af41cc56dbd5 | -10.5776 | -49.1316 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4896ec67-6bcd-3b26-a7cc-eb96edc6c2f8 | -10.6675 | -49.4679 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 247.0 |
| c3ebeed6-b669-3010-be41-11049c7a299e | -10.6489 | -49.4483 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 362fc57f-be12-305a-9219-b8d68f9805ef | -12.424 | -43.7274 | 2025-07-10 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 3348c374-2191-31e4-824a-d9ffb6845a64 | -10.6486 | -49.47 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| d44fa727-3884-3a4e-b3ee-b2515f6fa9d1 | -12.4244 | -43.7037 | 2025-07-10 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c9569764-a35a-3d95-9fa0-c8b0b3f181c4 | -8.5028 | -43.2614 | 2025-07-10 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 97842feb-790e-33e9-a0c4-4c7baf3d5900 | -13.3376 | -52.9264 | 2025-07-10 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 35ecc1d1-c593-3ddb-bfd1-276da3e758cf | -12.4433 | -43.7242 | 2025-07-10 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c1a563c9-9839-3cab-b508-455021402681 | -10.5773 | -49.1533 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 014f3f4e-5315-38d2-b4a0-e427121f3348 | -6.8485 | -42.7979 | 2025-07-10 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 6f26bb6e-0faf-3d4f-a1ce-ecf99aebfb6f | -11.3616 | -48.7142 | 2025-07-10 00:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 377b4cd8-a1b0-39ae-8ae1-7b20d08dde35 | -9.2067 | -48.6019 | 2025-07-10 00:00:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2f8763c2-6cc3-33fe-b89a-b9bc69113485 | -13.338 | -52.9054 | 2025-07-10 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e9243de8-7503-30fb-ba86-4f6eeafbc2f0 | -3.75 | -47.1144 | 2025-07-10 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f0466f53-8a05-3fc3-89dd-57274af63f22 | -10.6678 | -49.4462 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 1912d36d-7338-3d53-808e-354d4f0203ea | -10.5586 | -49.1337 | 2025-07-10 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 3f366193-4a14-3b95-a70d-2dcd20ba2cc4 | -13.3571 | -52.9032 | 2025-07-10 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 93128202-ae3f-37e2-999a-c1842d7ffb1b | -12.4433 | -43.7242 | 2025-07-10 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 11ee1145-ce85-359d-bae8-c3b63c3fc86f | -11.3619 | -48.6923 | 2025-07-10 00:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f436969c-04ee-33de-90b0-0b2cd43d5ef0 | -4.2322 | -47.2022 | 2025-07-10 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a7abd78d-6e42-3537-b41e-ccd2be646a2d | -10.5773 | -49.1533 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7a81f634-97a5-394a-bd50-29ee449b9e0a | -13.3571 | -52.9032 | 2025-07-10 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 49f034ea-579d-3ea5-a926-13b5cb143443 | -9.2255 | -48.6 | 2025-07-10 00:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e022e62a-cc7a-3ae9-921e-06f04d1bfbb9 | -13.3376 | -52.9264 | 2025-07-10 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 33bf3879-10da-3497-95a2-769aada63663 | -10.6675 | -49.4679 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 90e1a095-5f33-3f49-a94b-ee4c8c7ccc6e | -10.6678 | -49.4462 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 95cae073-a299-327e-8edd-22e56b14a86a | -11.3616 | -48.7142 | 2025-07-10 00:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3019b1ab-3676-3062-8b49-0a3af00ff94a | -13.338 | -52.9054 | 2025-07-10 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 162.4 |
| ddacb453-0faf-3559-98e5-4007a5a6b1ab | -6.8485 | -42.7979 | 2025-07-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 6f6abdbc-5f5e-392d-b08b-ecd9459d5ce1 | -3.75 | -47.1144 | 2025-07-10 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 60053d48-29ea-3842-9014-69f72d4c5d15 | -10.5776 | -49.1316 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| eaa0dde6-c8ed-3fb1-84c9-146771aa0f71 | -12.4438 | -43.7005 | 2025-07-10 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 83f62353-af4c-38a4-814e-b5127a637609 | -12.4244 | -43.7037 | 2025-07-10 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3da85ac7-42d3-35ce-8c37-fcd2fb4f3f0a | -13.3568 | -52.9242 | 2025-07-10 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 27efb261-9fd9-354e-8711-60d795b780d8 | -10.6489 | -49.4483 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 585c1f72-9b77-3831-ba00-839dfa00c1fb | -12.424 | -43.7274 | 2025-07-10 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 6a049e01-69ad-3b34-a9f8-d4fc56f022a2 | -10.6486 | -49.47 | 2025-07-10 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 43fc2337-7f6c-35e3-b990-56ee142ac668 | -7.9515 | -49.637402 | 2025-07-10 00:11:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f91f721-7049-375e-b56e-6b72d3fbab31 | -8.4951 | -43.292702 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 78515429-80c6-39c6-bf64-90ca0a1306f9 | -9.2223 | -48.589401 | 2025-07-10 00:11:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6bce28f-8c93-3c40-8be9-bcca286d9836 | -8.3353 | -49.184898 | 2025-07-10 00:11:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f08f4cb-bc21-3b2a-b8ee-ba8915ecc55a | -8.4927 | -43.2827 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86a3d5b4-f550-37f6-8c52-0c1bebb905fb | -12.4337 | -43.711601 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4247e5a-151a-3fd1-ba9f-d70f0a573b02 | -3.7507 | -47.1147 | 2025-07-10 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20f436d-27b5-3d73-b5be-d21a29dc0b10 | -10.655 | -49.453499 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 763008da-e357-3d26-bda8-b0005644d5fc | -6.8502 | -42.789101 | 2025-07-10 00:11:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b569d96a-0dbc-3914-a5af-d2224064345c | -5.5538 | -43.889999 | 2025-07-10 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa09d3b-1f01-3b35-b3ff-310f3585aa9c | -8.5002 | -43.270401 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae307448-c075-351c-bdc4-e6439dba36dd | -5.2314 | -45.209202 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1187451-fea3-3ac2-85df-76e6cce179df | -10.5679 | -49.146198 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb60b12-53af-3318-9189-8ad8481b3db9 | -6.9973 | -43.4991 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdfce0b-b51a-3f5b-a46a-1703a7442f7b | -5.0716 | -43.721298 | 2025-07-10 00:11:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35d194bc-60db-3727-a2e4-6f8f4160bed4 | -12.5738 | -52.2122 | 2025-07-10 00:11:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42f82c3a-b713-3257-8dc6-35f01deea385 | -8.3902 | -44.030201 | 2025-07-10 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46e9b3c7-ac36-3a93-a551-16246cf00a8f | -9.0934 | -47.9622 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97ae532e-6dd9-363c-b3b6-b82883450bd5 | -8.4978 | -43.260399 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08c49e3a-0e09-3e9b-977c-ad78c74b415a | -8.8907 | -47.332901 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1ff911-7992-34ba-8f13-b706eb786631 | -5.3469 | -45.263401 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 194b863f-d610-39ba-a183-4a2def349dfa | -11.7371 | -48.521801 | 2025-07-10 00:11:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 912d3a42-4ddd-3d92-9691-d03bc8c35152 | -7.7006 | -45.770401 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9029ec09-dc78-3fe5-9fd1-91a46f458d03 | -5.2334 | -45.2178 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4a3e0d8-c1e0-3653-877c-94546fd679e2 | -19.4461 | -48.529499 | 2025-07-10 00:11:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53518478-2ffd-3e3b-86b4-7b99b4a9e3b6 | -13.3722 | -43.750099 | 2025-07-10 00:11:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29da8e2d-5569-3d8c-87bd-09b8b3331770 | -6.8556 | -42.8116 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c421863e-b6e8-378d-af67-c25a95d5fcac | -11.4666 | -45.1026 | 2025-07-10 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 540fa5a5-5042-323c-94ba-995d1994a1a7 | -8.4759 | -49.590801 | 2025-07-10 00:11:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d654d0-a5aa-3752-b839-222073a72400 | -9.2125 | -48.591499 | 2025-07-10 00:11:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9289629-07d5-3d7c-9396-0693e1385fe9 | -7.7087 | -45.760601 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c80b34-f2e9-310d-8d6f-0ac6eb1538d9 | -11.833 | -48.2075 | 2025-07-10 00:11:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 822e892b-5019-34cc-96a4-5a77649fb34c | -13.4634 | -43.1283 | 2025-07-10 00:11:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e473e2e5-b9fc-33b3-94e0-a80dec8afd21 | -11.3638 | -48.695499 | 2025-07-10 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f5e1fed-f4b4-3489-a328-855d4b39df9e | -12.4259 | -43.7225 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83f25796-b697-3814-af43-ffc7b71078b0 | -6.9923 | -43.521702 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 093560a1-7003-30c4-9027-9df38d05a702 | -6.9997 | -43.5093 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f81187ac-98be-36ee-806f-f31eaa4832bc | -6.6782 | -43.764099 | 2025-07-10 00:11:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5477882b-271b-33d0-9bad-f2dd34692c42 | -11.4551 | -45.097301 | 2025-07-10 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81c082bf-fc8c-3177-ba04-2ef4446ab4fa | -7.2261 | -43.071201 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0a85850-ebdb-32c5-935a-efc52082afa6 | -9.3021 | -44.8438 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53fa0085-44f5-32b6-b6ef-6fa8ac119a5a | -12.5719 | -48.867401 | 2025-07-10 00:11:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7c58c60-b34d-3e6b-a8a0-63db6eb259a8 | -5.8924 | -45.573601 | 2025-07-10 00:11:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec94a133-f5ed-3f5c-8d32-8f5f59565ce0 | -6.9949 | -43.488998 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74b1bfe3-5413-3215-b4ee-3bc3d971abb6 | -8.9972 | -47.439899 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6bf803-d531-3e33-a8bf-b30b1d3d9645 | -10.5777 | -49.1441 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15d00640-e28d-375e-95d2-6195ddc9a5a0 | -8.3337 | -49.177799 | 2025-07-10 00:11:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d793d4e-9d2b-38ac-a30c-a1f90c17b6db | -10.969 | -49.243698 | 2025-07-10 00:11:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0402d91e-04c8-3304-9355-61e4f4e791ce | -3.8095 | -42.546299 | 2025-07-10 00:11:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d6b3a61-2165-3ae5-8e51-eb6d87419248 | -6.6772 | -46.298401 | 2025-07-10 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df47a089-a727-3cd4-87f1-1acf3be0ad0b | -10.6648 | -49.451401 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3f4fde4-7a68-3131-94ac-877e9c2cf610 | -10.6287 | -45.227299 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec5bd9a9-38db-3c9d-b508-82e9595714b1 | -8.5072 | -43.3004 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e3862ab-fb12-3fb7-baaa-0aeb0cb05bb7 | -19.447901 | -48.538101 | 2025-07-10 00:11:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 27640b25-8d3b-3bb2-aa69-f4b231a42f6b | -17.7824 | -52.412998 | 2025-07-10 00:11:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81493e09-b93d-3155-a229-f5c2a13fddfd | -7.6989 | -45.762798 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa239b35-bf32-39fe-8bf5-47c5e44806fb | -10.668 | -49.4664 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d821a175-0c8b-35fe-9d44-5271d261a4ae | -13.0027 | -46.281898 | 2025-07-10 00:11:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 605bdb9d-5285-355d-84c7-e148637f2136 | -10.6664 | -49.4589 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
