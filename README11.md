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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eeffcf8a-aa5b-306e-b3a3-5ec56eca29fe | -10.1855 | -44.8709 | 2025-09-30 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| ddecb895-8cb8-35b8-a79e-d5e1c2b4d115 | -21.0564 | -45.6881 | 2025-09-30 00:40:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 747caaf9-574c-3d7d-a0be-5009510a7a70 | -11.7712 | -44.7432 | 2025-09-30 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a915cda3-18fa-32b9-8234-a7bd9aeb5c83 | -11.071 | -47.8262 | 2025-09-30 00:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 83e441da-719e-36b0-9c32-f04ea1ebac79 | -15.5973 | -47.8243 | 2025-09-30 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 246cdd38-b3b4-39e2-a6f4-84f8423bd2a5 | -15.2658 | -49.7052 | 2025-09-30 00:40:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 768ce809-a51a-3a49-a393-1b813076594f | -20.0491 | -41.3251 | 2025-09-30 00:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.2 |
| 9fb11ebc-5a11-371a-9c9c-0c6e6288f5ea | -12.8643 | -46.8904 | 2025-09-30 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c9791cf8-a564-36c4-b771-bfcbcd34b90e | -11.1548 | -54.1054 | 2025-09-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 40da8196-ae7b-3aab-83f1-0444b4272eb1 | -5.214 | -45.2341 | 2025-09-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 46d99a24-6214-3167-94e7-686fac62728c | -11.2135 | -47.2309 | 2025-09-30 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4f3930eb-7566-3bfa-ae13-4c269cc42ed8 | -14.5522 | -48.4684 | 2025-09-30 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4976f114-e377-3584-a741-6c11265475be | -9.4192 | -54.7172 | 2025-09-30 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 12c5dd38-856a-375f-8628-847571399413 | -19.6027 | -45.8861 | 2025-09-30 00:50:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 46.6 |
| efbacaad-62fb-3555-b3b3-f7d40f7f9621 | -20.0491 | -41.3251 | 2025-09-30 00:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| fbbcbbb3-63bd-3811-a013-92b27078af68 | -11.8864 | -48.0545 | 2025-09-30 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 57e02a88-f520-3f46-9889-5b305a5a0914 | -11.8868 | -48.0323 | 2025-09-30 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 393f9bf7-d788-3bef-a15d-16c7f1e9fac9 | -11.1546 | -54.126 | 2025-09-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 2df4fe48-8717-38bd-a8b4-b68e752570eb | -7.0481 | -45.1856 | 2025-09-30 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9a33f700-b196-3fa1-94c2-7234a2ae86dc | -4.3538 | -45.5997 | 2025-09-30 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b914b61d-35f8-31fd-b6bf-ca57924a4c7b | -11.071 | -47.8262 | 2025-09-30 00:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2d6ae5ac-9329-3379-829a-f9a6c8a46fa4 | -4.3991 | -44.3966 | 2025-09-30 00:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6ee56d91-990c-32aa-82e9-5ea65362b963 | -10.2041 | -44.8915 | 2025-09-30 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 270.0 |
| df8c3014-5a27-3b45-a429-8381eac77dbb | -3.1013 | -47.0082 | 2025-09-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 80212700-0b5d-3326-b75a-1c1c9b67d2d9 | -10.1851 | -44.8939 | 2025-09-30 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 33a16a4e-2db9-3c1a-845e-37ee197ff9d7 | -11.1548 | -54.1054 | 2025-09-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1b6405f3-a136-3091-9359-c86287811303 | -21.0564 | -45.6881 | 2025-09-30 00:50:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5286a5c1-2e80-3238-a670-629481d2dd0a | -11.7524 | -44.7228 | 2025-09-30 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 92f8deed-fc9f-3fb4-82a9-86d48183d128 | -13.0139 | -44.1243 | 2025-09-30 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 68138961-eb2e-35ca-bff4-499fe54a9844 | -11.7519 | -44.7461 | 2025-09-30 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 499311a9-fe1e-3397-be8e-a97f2a7b9670 | -5.5243 | -43.8647 | 2025-09-30 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6ecea482-5487-3485-8eee-8841c45a3123 | -10.1855 | -44.8709 | 2025-09-30 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| bd65c637-65c0-352e-b9cc-cefe5cc399e6 | -11.1735 | -54.1242 | 2025-09-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 65c697cc-888e-39f6-8cd5-5c004cabd34a | -5.5241 | -43.8878 | 2025-09-30 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 0b1c2416-afec-3e21-9d22-dc1f4183d01a | -4.354 | -45.5773 | 2025-09-30 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 3ac6616f-cf33-37c1-83fa-1fb830d7f9aa | -11.1357 | -54.1277 | 2025-09-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c73b10bd-e6cf-3619-84ac-73a34c7a70ec | -10.2045 | -44.8684 | 2025-09-30 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8dedc736-98f1-3f37-983e-a53ec256d6ca | -21.0572 | -45.6638 | 2025-09-30 00:50:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| be89417b-2cb3-350e-96e8-8afa97ece5d9 | -14.5141 | -48.4299 | 2025-09-30 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4e9792df-f2d7-301a-bcf0-5458ee9ad892 | -11.2138 | -47.2086 | 2025-09-30 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 8c269de6-7463-38c9-8ada-69f174062c6b | -11.7712 | -44.7432 | 2025-09-30 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 4ff81438-8cff-301e-a300-37346b783faf | -11.7524 | -44.7228 | 2025-09-30 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 59dc4935-27f4-3807-b5ae-e8ab064f32b5 | -14.5522 | -48.4684 | 2025-09-30 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 651d7e21-1059-3460-975d-0671abff3694 | -11.8864 | -48.0545 | 2025-09-30 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8749d65d-2c5c-3119-9e23-4ed94a4a5fa7 | -11.8868 | -48.0323 | 2025-09-30 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cd57cc46-a0a2-3b10-baf1-7619e8d67bcf | -14.7137 | -48.1525 | 2025-09-30 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6656ed94-4aeb-3932-83a0-1fca31015e80 | -14.6942 | -48.1557 | 2025-09-30 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a07a9713-48bc-3601-8b75-347c4aa1c4bc | -5.5241 | -43.8878 | 2025-09-30 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a81672ab-cb0e-3eac-b9f6-672c0d50fd67 | -12.8429 | -47.0063 | 2025-09-30 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bce039f5-7cbc-3ec3-b4de-9aeb343f2fa9 | -11.1944 | -47.2334 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3d31be55-6790-3246-ab27-acb1c3fb5740 | -17.4049 | -47.1431 | 2025-09-30 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 93f0a139-1f42-35e6-b7b8-7d76ab239000 | -11.2138 | -47.2086 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 309.7 |
| 8f03296f-0014-31d8-a64a-6c099044dd10 | -10.1855 | -44.8709 | 2025-09-30 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| dfd0d5e2-5823-3ea9-96ef-1c7f83075986 | -10.0717 | -50.2173 | 2025-09-30 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 713b8158-2168-36c8-99b0-0393aa0145b8 | -8.2659 | -45.5244 | 2025-09-30 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f79b3a64-c678-3e7d-a848-ae7be0cfaa7a | -8.2471 | -45.5263 | 2025-09-30 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| db5060eb-f83a-3b40-8fb7-61bc2d7e3e72 | -13.4005 | -48.0657 | 2025-09-30 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7486d471-7439-3c53-91a5-30f22f5ac729 | -12.8433 | -46.9837 | 2025-09-30 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b1715765-6280-3759-8be1-d41bdc94ab2a | -11.1548 | -54.1054 | 2025-09-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 62210149-1caa-3849-9b98-473f0941376f | -15.7058 | -59.5126 | 2025-09-30 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9b212334-8ebb-3e2c-8652-1875d63cf991 | -4.3991 | -44.3966 | 2025-09-30 01:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 23d8a864-943b-3975-b8e1-b7d15514caf4 | -10.2041 | -44.8915 | 2025-09-30 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 86433196-8e68-3e14-8da6-5649ef3b2809 | -3.1013 | -47.0082 | 2025-09-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d96d08bc-4eaa-3522-a495-ec1d403c76f3 | -11.2326 | -47.2285 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b0e9a083-b910-33c6-874b-9ace2a7e41b0 | -14.5327 | -48.4715 | 2025-09-30 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 98c4984a-d465-33b3-a6e6-d9aa7ac10def | -15.5973 | -47.8243 | 2025-09-30 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 829767dc-b633-3b5f-a9d2-ae752fea78e6 | -15.8024 | -59.5235 | 2025-09-30 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 65cc37b7-a82e-3d66-9483-e762e1dab368 | -11.1948 | -47.211 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| bff861a1-c68d-38af-9d34-5c24161ce191 | -5.5243 | -43.8647 | 2025-09-30 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0efe9f24-1a22-31f3-bfc2-353b07b349cc | -10.0714 | -50.2387 | 2025-09-30 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 466f4345-09d5-3b1b-85a8-6e0604bd8b51 | -11.7519 | -44.7461 | 2025-09-30 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 2f9242f3-56f4-367c-ae5c-65ff6c212bc7 | -21.0564 | -45.6881 | 2025-09-30 01:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1aab79fe-f9f8-304b-9671-dfeca357ea12 | -10.2045 | -44.8684 | 2025-09-30 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 683a8b9c-a4f6-3bcf-a60f-784c1842d06c | -10.1851 | -44.8939 | 2025-09-30 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 122204f0-a780-304c-9050-6a60294e4b4a | -13.0144 | -44.1006 | 2025-09-30 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 502c031d-28eb-3200-94df-a19975dcf162 | -11.1737 | -54.1037 | 2025-09-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ba8d683d-92e7-30ca-8b18-1a3931b32174 | -11.2135 | -47.2309 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 16015150-a2ea-32fc-bc01-79afb902a735 | -11.1546 | -54.126 | 2025-09-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 83dcfb01-bbc4-3df5-949f-3e39d94cef3e | -14.5141 | -48.4299 | 2025-09-30 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| aee331b3-7ad1-3c3d-903a-3820eee638fb | -11.1735 | -54.1242 | 2025-09-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5e0b8cce-e888-39f7-abff-8fe7f48dc28f | -15.7251 | -59.5108 | 2025-09-30 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 23391ed4-27fe-3409-baa4-78168eefbc60 | -11.2329 | -47.2061 | 2025-09-30 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 50ffbad4-8eec-385f-bd57-3bd88e6b7430 | -13.0139 | -44.1243 | 2025-09-30 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e64938e3-8c74-3837-83c3-cfa7764bf21a | -5.5243 | -43.8647 | 2025-09-30 01:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4ae1449a-6f93-3fa0-858d-57f517b37121 | -11.7519 | -44.7461 | 2025-09-30 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4c3b3ae5-36d8-3fa1-8bd3-e10f227d0c61 | -17.4049 | -47.1431 | 2025-09-30 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bdfa0fdf-cb23-312f-8471-3df596bdab07 | -14.5752 | -48.2865 | 2025-09-30 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0a814354-6856-3c02-ada1-e26e517876b4 | -21.0564 | -45.6881 | 2025-09-30 01:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 758bc96b-3e80-3d32-a398-af76b1015ebd | -12.8433 | -46.9837 | 2025-09-30 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 96462e1f-e240-36ff-bf83-f04bff14f920 | -4.354 | -45.5773 | 2025-09-30 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 1d8d221d-e975-36ae-8709-9c6a67911562 | -15.8024 | -59.5235 | 2025-09-30 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 53761632-7e14-331c-a8c9-bccabdc78067 | -21.6839 | -48.0698 | 2025-09-30 01:10:00 | GOES-19 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2d830bf2-f48e-3772-9a07-6d188d1203ca | -11.1548 | -54.1054 | 2025-09-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| b16cd875-d80e-3f2c-a7c9-97bc6a2494e3 | -10.2045 | -44.8684 | 2025-09-30 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 974d3c2d-1c5a-30fe-bb95-d12bba52d7fd | -11.1546 | -54.126 | 2025-09-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 6a6904fa-ca90-3106-8901-c3a535bd9d1f | -5.5241 | -43.8878 | 2025-09-30 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4f7e0699-1539-3192-b796-d17d8bd489b9 | -11.7712 | -44.7432 | 2025-09-30 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c380c546-ebae-3775-b351-c9d247d37544 | -10.1855 | -44.8709 | 2025-09-30 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| e282d415-eab7-3496-b4a0-991c859297bb | -12.8241 | -46.9866 | 2025-09-30 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 79ed72e9-55ac-3249-b134-d0129afbb135 | -4.3353 | -45.5782 | 2025-09-30 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 35.0 |


[Clique aqui para ver as próximas entradas](README12.md)
