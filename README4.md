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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e026c1ff-acf7-376c-9872-6f11ac879977 | -8.6889 | -47.8664 | 2026-06-25 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b3483369-52ef-35f3-a633-dd41b72132e6 | -12.7369 | -44.4756 | 2026-06-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ef9f252d-fa8c-379b-9e7f-e6419b99725d | -17.365 | -42.6035 | 2026-06-25 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a26470b5-a133-317e-8083-9cf0770f49e4 | -12.216 | -55.4968 | 2026-06-25 00:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 49354647-1a1b-3459-8de4-ad098a986f8e | -17.3442 | -42.6333 | 2026-06-25 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 5b690be8-f513-3ada-8d20-1a45cdad6414 | -12.7562 | -44.4724 | 2026-06-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 8168756f-8451-3156-90c6-efe57c9dea31 | -12.7373 | -44.4521 | 2026-06-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 493ee55a-4a64-3b8a-a588-0284829cd948 | -12.7566 | -44.449 | 2026-06-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1713327c-c4b3-34de-aec7-8ab025fc9b1a | -7.7498 | -44.6184 | 2026-06-25 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e02f2296-df89-3d2b-9bcb-9546313a8f68 | -6.9793 | -42.8798 | 2026-06-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 9de38d99-6672-3727-bf7b-e055df132199 | -17.3449 | -42.6084 | 2026-06-25 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f3c53a86-ce5f-3b08-b533-1efca0aef6d4 | -8.6889 | -47.8664 | 2026-06-25 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1de82cb5-ea2c-35c3-910f-7a7952594741 | -17.3643 | -42.6284 | 2026-06-25 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 8e3b9913-4122-3461-ad75-3de1e635e735 | -12.7566 | -44.449 | 2026-06-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 831aa3e9-e96c-31ec-9606-47c335acff87 | -6.9791 | -42.9034 | 2026-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 3215e4c6-d9b1-3585-b41c-7d9ec8ea5d20 | -12.2158 | -55.5171 | 2026-06-25 00:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8ae5f3c8-730c-3b55-9376-7ff29ea1d3a8 | -7.7498 | -44.6184 | 2026-06-25 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| cdeaf333-8130-33c2-b528-51f190c2530e | -17.3449 | -42.6084 | 2026-06-25 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 788e8450-83e1-360b-8428-a3908a280b30 | -12.7373 | -44.4521 | 2026-06-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| f3da2a71-09c2-32fe-99d5-5f7fca4c1391 | -10.423 | -46.7258 | 2026-06-25 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b5fe5dec-55cb-32aa-a8ac-661a411b4543 | -6.9982 | -42.878 | 2026-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 9e53c5ae-cb3f-3d1c-92b9-b1862be5c723 | -12.7562 | -44.4724 | 2026-06-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ca473eb8-3368-32e7-a0d8-36891e195f57 | -12.7369 | -44.4756 | 2026-06-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c3f872ca-a30d-30bb-b373-759a7bd8cc50 | -6.9793 | -42.8798 | 2026-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 3a486304-6525-385b-b9f7-afdb9097bf3c | -17.3442 | -42.6333 | 2026-06-25 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| b4bd9caa-984d-31fb-a480-469a7fd6ff72 | -12.216 | -55.4968 | 2026-06-25 00:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| fa6556d6-6ec5-3bea-af42-6414bf3cbf7e | -12.235 | -55.495 | 2026-06-25 00:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b9e3f33b-21a0-3698-9ede-919885f69d2a | -17.3449 | -42.6084 | 2026-06-25 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 90526b32-5c7b-3e03-905c-20c9cda49fd3 | -12.235 | -55.495 | 2026-06-25 01:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 57a53fce-8822-30d3-84cb-f6f83d4fec20 | -17.365 | -42.6035 | 2026-06-25 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| de35bbba-9713-3754-ba4d-3058937835d6 | -6.9791 | -42.9034 | 2026-06-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 375685cb-cbe6-3cea-ba03-a227f140d299 | -6.9793 | -42.8798 | 2026-06-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| f33f4e96-9bfd-331e-925a-a75df19c523f | -12.216 | -55.4968 | 2026-06-25 01:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| ae9ae9c4-d78e-38fa-b8ca-949165b1c003 | -17.3442 | -42.6333 | 2026-06-25 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| da99573b-9cd0-3890-8b73-cdb5176a9715 | -12.2158 | -55.5171 | 2026-06-25 01:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 319c86b5-5783-3035-bc47-d64872a39380 | -12.7373 | -44.4521 | 2026-06-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 008f1e0a-de74-36a3-abf0-1f9b63fb7ecc | -8.6889 | -47.8664 | 2026-06-25 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f45428e1-433a-390d-b9d3-a3f42d0f7333 | -7.7498 | -44.6184 | 2026-06-25 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 70c84a4f-de7a-35ed-84d6-1d78c402f6b3 | -12.7566 | -44.449 | 2026-06-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| cb785d6c-096d-3bc5-a03a-6d849ad8958e | -9.1933 | -45.3114 | 2026-06-25 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bfe69790-fe77-3e90-a659-0cdb89d21356 | -17.3643 | -42.6284 | 2026-06-25 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d8f1a7c2-c76a-3fc6-9bda-01df6fd81186 | -12.7369 | -44.4756 | 2026-06-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7686bda0-d41f-3f4b-9fa1-0f58f73dfb22 | -9.193 | -45.3342 | 2026-06-25 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6325ecb5-d34c-354e-b509-ba7574ba0290 | -9.1933 | -45.3114 | 2026-06-25 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| fcf7eb3e-28d1-3f82-8bc6-2a17fcf0e3cb | -17.3442 | -42.6333 | 2026-06-25 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 79f033ed-1560-3ac5-beb6-a32296341267 | -17.3643 | -42.6284 | 2026-06-25 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5e34d49e-d863-3f27-bbac-6281d32084d4 | -12.7562 | -44.4724 | 2026-06-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 40c7729b-6706-3da5-a25d-32eb322ee44c | -6.9791 | -42.9034 | 2026-06-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| d1416247-c9e0-35df-9a8f-2122d60a7f05 | -12.7566 | -44.449 | 2026-06-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e02e78b9-9d07-3f38-8958-2feea9b590a2 | -6.9793 | -42.8798 | 2026-06-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| ce434d15-2a64-30f1-aa91-6586d5689e0a | -17.365 | -42.6035 | 2026-06-25 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2d8c2709-dc0d-3e58-a168-4baec09a7047 | -12.7373 | -44.4521 | 2026-06-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 630a0187-ca6b-381b-aa2e-931f851387d8 | -12.216 | -55.4968 | 2026-06-25 01:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 43d167f7-a7c4-3fdb-9f31-b1a5d83d0246 | -7.7498 | -44.6184 | 2026-06-25 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d3f49379-c781-36d2-a474-88dbdd28a3f9 | -17.3449 | -42.6084 | 2026-06-25 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 5b1f0ddc-cca4-36eb-b4b8-d5821825ff44 | -8.6889 | -47.8664 | 2026-06-25 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7d3b6cc4-6dec-3160-a4de-2f0605906de9 | -12.7369 | -44.4756 | 2026-06-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1cf305fc-91b6-3b43-abd6-eb7665bf98b3 | -12.235 | -55.495 | 2026-06-25 01:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 603de99b-5321-39ff-ab66-417713cd6131 | -12.235 | -55.495 | 2026-06-25 01:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8015a3f0-49ae-3a06-a2e3-b7589fe6f73d | -12.7369 | -44.4756 | 2026-06-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b579dc62-04ba-364a-9e30-2c7a4a961829 | -6.9791 | -42.9034 | 2026-06-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| e4481bea-b237-38e8-95cb-35e0b8066a5c | -12.216 | -55.4968 | 2026-06-25 01:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 019afc04-4cdc-3d1e-aebd-e862bb72ce24 | -9.2123 | -45.3092 | 2026-06-25 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5631d6bb-3e54-33d4-ba49-a0bf2312bc4b | -17.3449 | -42.6084 | 2026-06-25 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e5f6b216-6110-390a-9077-e49ff71cd9a3 | -9.193 | -45.3342 | 2026-06-25 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 5a21de5f-34c3-304a-a2d2-5a607f0c8063 | -8.6889 | -47.8664 | 2026-06-25 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2ec3a1a6-d27e-314f-9ef5-28ccd7baa024 | -17.3442 | -42.6333 | 2026-06-25 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5168d943-2402-3582-93af-de8e402c6c09 | -12.7373 | -44.4521 | 2026-06-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| fafd65c6-96d0-3299-a6e4-6a9d21d7f794 | -6.9793 | -42.8798 | 2026-06-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 1de16db3-7250-3790-88d3-e8c36a809ff9 | -9.1933 | -45.3114 | 2026-06-25 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7b0bc2d5-5db9-3a6f-a47b-5f4cebb0798d | -12.7566 | -44.449 | 2026-06-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cea389e1-0b2b-3fe8-9390-6d6732d16e74 | -7.7498 | -44.6184 | 2026-06-25 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 9406f968-42d2-3d8b-b99d-f3351894ad70 | -7.7498 | -44.6184 | 2026-06-25 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0b18377d-7f5d-385d-8208-b5372b4290b2 | -17.3442 | -42.6333 | 2026-06-25 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3a6fcf93-c363-397b-945b-aa02f8eab3ab | -8.6889 | -47.8664 | 2026-06-25 01:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 9f3b0cdb-b7dc-34d8-b44a-33c149fb4c4f | -9.193 | -45.3342 | 2026-06-25 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b14b204e-4552-34e6-89d8-fdc951587748 | -6.9791 | -42.9034 | 2026-06-25 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 856e2c40-2952-3f2f-8b30-4b7921125f76 | -9.2123 | -45.3092 | 2026-06-25 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 2c4bc83f-707f-3983-b756-7cb75ce8102f | -9.1933 | -45.3114 | 2026-06-25 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5a03f940-ee54-308d-9ae2-bd2c81fd9571 | -12.7566 | -44.449 | 2026-06-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f958701c-915d-3a3a-b831-247e18a478a0 | -12.235 | -55.495 | 2026-06-25 01:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 430eb240-ed61-32b0-98da-891f9fa0af75 | -17.3449 | -42.6084 | 2026-06-25 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c926fb6a-1237-34a8-a486-b2af37289aa6 | -12.7373 | -44.4521 | 2026-06-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f2be1e4a-9695-30b5-bf93-0eed59af1735 | -6.9793 | -42.8798 | 2026-06-25 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 5d5be8b8-33f7-3a21-9261-d8890c755bfb | -12.216 | -55.4968 | 2026-06-25 01:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 61f22cfe-038a-3eb5-b9b7-c39810aae3a5 | -9.212 | -45.3321 | 2026-06-25 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 6b4c2acc-629b-3ce2-a0ac-b4570a91ba32 | -12.7369 | -44.4756 | 2026-06-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a5d0d150-c224-3fb0-b207-6223bcc26098 | -17.6926 | -40.275 | 2026-06-25 01:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 3ae810c7-7cef-3f8b-9bc0-ef5ca40aa019 | -12.7373 | -44.4521 | 2026-06-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| fe87b5e0-fc0f-386b-9767-faf8a9a1c37a | -6.9791 | -42.9034 | 2026-06-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 25472504-509e-3b61-bd4d-5d20752a1de4 | -12.7369 | -44.4756 | 2026-06-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fca83351-5f5f-3d63-b6b8-0c8613460682 | -12.7566 | -44.449 | 2026-06-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5eee038d-a366-3ef5-8aa3-a44bace4b1e7 | -9.212 | -45.3321 | 2026-06-25 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 52ae1301-6d41-3bdf-8b6b-79f2216fb227 | -7.7498 | -44.6184 | 2026-06-25 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3ee3154b-7b3e-3a62-ba85-67efcc11b186 | -9.1933 | -45.3114 | 2026-06-25 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0b11f1cc-3970-3d56-ae10-86f72e6e33ad | -17.6934 | -40.249 | 2026-06-25 01:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 157.8 |
| 0a5a1403-c2c4-35ec-9184-0054605549a3 | -6.9793 | -42.8798 | 2026-06-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| c6fd2e79-7dd5-3670-b5cc-8e4fb7cf83a4 | -17.3442 | -42.6333 | 2026-06-25 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0a6f6ff0-991c-35cc-a8b9-087ab2d47b29 | -12.216 | -55.4968 | 2026-06-25 01:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a03b25d4-5d47-30b7-9c9d-7130dbab35af | -8.6889 | -47.8664 | 2026-06-25 01:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |


[Clique aqui para ver as próximas entradas](README5.md)
