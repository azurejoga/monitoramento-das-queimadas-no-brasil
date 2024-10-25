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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f95a6b70-1678-3f80-866c-4aa869103db5 | -13.45849 | -47.23429 | 2024-10-25 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de451dc4-c9ed-36a4-bb54-9842f00c2488 | -13.45785 | -47.2381 | 2024-10-25 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b39bc24-6eb4-375b-8304-2ab4e4e4182e | -13.38447 | -47.84669 | 2024-10-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7622100-da78-3b68-af13-69088de8da36 | -13.32849 | -47.61915 | 2024-10-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 455584f0-3b4f-3060-861a-1557b62b3545 | -13.29811 | -47.18985 | 2024-10-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d2cd9d9-125d-3d67-8c6e-acdccfb4a04c | -13.23916 | -46.69415 | 2024-10-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c788ccd6-6e4a-3145-a516-412975e527d0 | -13.23511 | -46.69735 | 2024-10-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 405f5d1a-fdf0-33a7-9675-b448f04ea3bf | -13.23169 | -46.69675 | 2024-10-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd2d9e9d-1174-3882-978e-b79604dd2fc3 | -13.09544 | -47.14106 | 2024-10-25 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3d429ed-c8b6-3f17-bd51-2a6ad36876ce | -12.93484 | -47.68722 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b18917-c855-3454-bb32-fd7d9106aa08 | -12.9341 | -47.69156 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 237bd4c0-71cc-3c45-af60-ccabb02fd482 | -12.9305 | -47.69102 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f62dc5d-7552-3da3-be6b-f796a5594597 | -12.892 | -46.77322 | 2024-10-25 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb628a93-03f6-3799-b724-39474274d764 | -12.83603 | -46.8749 | 2024-10-25 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 712d8578-8d25-35f5-9f8e-b61a27dcd833 | -12.8012 | -47.89696 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec759307-2d2d-3e30-9928-52d6325da582 | -12.7414 | -47.41333 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21382148-52ac-3c28-adfd-ab420bb97612 | -12.7102 | -47.96679 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff6ca81d-c1cd-3f11-ad8b-ac1508254d8e | -12.63224 | -47.54337 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2044ce9-0a4e-3e1c-9abb-c6a35ba4c2de | -12.53813 | -46.80675 | 2024-10-25 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e9f27a-8aee-394f-b386-0171f48f73e7 | -12.51253 | -46.87457 | 2024-10-25 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8212e99-59a9-3613-a2fe-5f7efd1f18ce | -12.50058 | -47.29049 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31847b8c-b7a4-39de-8e07-eb1f5e240e2e | -12.3684 | -46.90321 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8769582-7a39-3901-adac-0f33158635ed | -12.36557 | -46.89868 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e76697a-476e-3bdf-b70e-fe7b928f46a1 | -12.36492 | -46.90262 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b249bea-669f-3bc9-ac78-df4f02e330de | -12.26956 | -47.64314 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f163f7d8-cd32-3e08-9d0f-36675d55d773 | -14.07693 | -47.00838 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48918490-7ebd-3d03-a0b8-0e8216192a6d | -9.27547 | -48.26211 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1537b83-5c77-3a96-bdd2-c14392d7cd5b | -9.27255 | -47.9119 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7476f5-65ca-38dc-b952-179ce3b1bdf3 | -9.27163 | -47.91422 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e632842-331b-37c2-b5b9-008902265fcc | -9.26875 | -47.91123 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b6a9905-ae19-3ce7-896b-4ca16738b076 | -9.26783 | -47.91357 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3a36b99-77d3-3b2e-9752-a6838cff4061 | -9.26495 | -47.91056 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 523b391f-4846-3043-a6e1-b33648a71810 | -9.26403 | -47.9129 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ba7e55e-409e-342c-bddc-ad57c3a98ada | -9.2497 | -48.31955 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78fa0d41-2b1a-3a6b-81ae-78a8417d324a | -9.24885 | -48.32453 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f91726e-00c5-3db6-ac57-6302ce6a4942 | -9.248 | -48.32953 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d943c20b-9aca-30fe-b28c-fe919eb16320 | -9.2458 | -48.31888 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ab0fce6-3e38-3925-a61f-65aa92c2a33b | -9.24495 | -48.32387 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3914cfdb-e075-3b01-8287-4bb87e3c65bd | -9.24409 | -48.32888 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b359696d-e7a7-35b8-a9b0-e8ea279b0298 | -9.23146 | -48.28565 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eccd4c09-6757-3e8e-ac68-1b7885013f72 | -9.2306 | -48.29063 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fb5b4fa-942e-3b88-8786-a17360766e11 | -9.20808 | -47.78515 | 2024-10-25 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edbf887a-c16f-3eb3-a504-ed0b7fadfbc1 | -9.10649 | -47.65149 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c059a97-3c25-3aee-9e4c-2dfe7df4c463 | -9.1057 | -47.65607 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0258f4db-55a3-32a4-869b-826ace773015 | -9.07551 | -47.99335 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63857392-fdc1-36ee-9e67-014ee0302097 | -9.07469 | -47.99817 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e9b8b69-a725-345d-bfba-73fdb810b7cd | -9.07387 | -48.00299 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab686003-4b89-3459-9d5f-c3cd185b2de9 | -9.07086 | -47.9975 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05789346-b6cb-37bb-bd0d-6b3555e3f082 | -9.07004 | -48.00232 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b59e54b-930c-378d-849d-0923bb5e0dda | -9.04685 | -47.81934 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81eed170-f2e5-3d2b-80b4-c47c86fe8eb1 | -9.04306 | -47.81868 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a65e93ad-5ec0-310e-99ce-ca1270810aaa | -9.03927 | -47.81801 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ecc0ac0-6c02-319f-b697-54a21f252a41 | -9.01839 | -47.75678 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7042bbb2-7a3d-30e2-a18c-99ce0318e2ec | -8.96015 | -47.63995 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03f22cd7-00a3-3ea2-8a62-5c052ee9a409 | -8.95658 | -47.22926 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31b9d071-1011-3bf6-8681-858ac6ce7483 | -8.95639 | -47.63934 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 81890fc5-e643-33cf-8b6f-e30c6d214493 | -8.95263 | -47.63871 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb9cc691-6a8d-33e7-9c55-19f181a715e9 | -8.91151 | -47.72203 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a3952fb-d271-3b0d-a22c-125ae4a95e47 | -8.91073 | -47.72667 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98883ca1-b504-3a20-9b93-a3f50cb47c49 | -8.8234 | -47.94012 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b60c96b-fdd8-3356-ab12-84260e01b8e0 | -8.82136 | -47.93736 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aad3ed98-64ca-35d1-b948-daacf0d2e472 | -8.8137 | -47.93605 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d73570d-5e13-3a6d-838c-b67a66ab1d97 | -8.80986 | -47.93541 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f284c4a6-b9b6-3937-9b7f-de0deb2c0848 | -8.67582 | -47.87484 | 2024-10-25 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68f394c1-4927-30ef-8abf-592dcc36963d | -8.56067 | -48.14914 | 2024-10-25 04:17:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f06f08e-8481-388b-a6e8-7fcdd7e948c2 | -8.46888 | -47.81075 | 2024-10-25 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a505e1d-f54c-3efb-919f-90b857766bbd | -8.46505 | -47.81013 | 2024-10-25 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a193663c-6fcf-3e51-9d13-30679c5005a3 | -8.42661 | -48.10895 | 2024-10-25 04:17:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f07a1a9-fdf3-31ee-a09a-437896babd0b | -9.03624 | -48.71364 | 2024-10-25 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e1e0343-be04-3931-8063-bfb5faadc5bc | -9.0356 | -48.71729 | 2024-10-25 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eed187f-7568-3fef-af1d-73f0aa759cd4 | -8.90997 | -48.53989 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 31610a8c-1f18-3495-b788-b2ac5eb97e93 | -8.90938 | -48.54336 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8fde594a-52ec-34e3-965d-7b6c0b6693bc | -8.90712 | -48.53258 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 839be4ef-c366-30d1-98c5-03cea0ba2530 | -8.90598 | -48.53933 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f33af3a8-3543-302a-9910-94e3e64306c3 | -8.9054 | -48.54277 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 847100a1-9657-3f1b-9a74-2ceecb8ce839 | -8.90429 | -48.52519 | 2024-10-25 04:17:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55ba65ed-b173-36ae-9a9c-091670a941d0 | -9.60586 | -48.87917 | 2024-10-25 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 915a8fd1-786e-3575-a614-a8f33169ee7d | -9.93686 | -48.87663 | 2024-10-25 04:17:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f763ffe-1f98-313f-8b9a-41af17ddb495 | -9.93287 | -48.87595 | 2024-10-25 04:17:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fbff9bb9-94dd-376f-a629-0e47f891186b | -9.91887 | -48.90951 | 2024-10-25 04:17:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f9c493-4331-3f11-a44d-b4c41df83a28 | -10.69244 | -49.10624 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db9e05b-1e78-357d-9b2c-454de16cd213 | -10.69184 | -49.10977 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e62df38-b78e-3e87-95ac-f6470acdb180 | -10.68843 | -49.10555 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8328d0f3-2ce8-3d28-bc58-9aa7ed06300b | -10.68783 | -49.10909 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3ef1950-d24c-3c97-aec6-cde6f97e9186 | -10.68722 | -49.11263 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 175cb522-5cca-3fdb-85da-034e6b3219be | -10.68382 | -49.10841 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a06c63-f16e-3c2a-960a-9fa8b0fd6b4d | -10.42221 | -48.98112 | 2024-10-25 04:17:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc56086e-3898-316e-9496-e21641eb3295 | -10.2894 | -48.89279 | 2024-10-25 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 226bc39f-ecd7-313e-9fc0-9fb51ed44300 | -9.95432 | -47.9508 | 2024-10-25 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b85a50-719d-3f77-a0b6-54f0f917b2a2 | -9.92698 | -48.13391 | 2024-10-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6b028a7-7683-3da5-ba60-4c86f7ec124e | -9.92453 | -47.84832 | 2024-10-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e09fe9-39b2-396f-8773-3585f34887b0 | -9.92317 | -48.13326 | 2024-10-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7451bbe2-8fd7-3adc-ac75-31128c93b4ae | -9.87182 | -48.20277 | 2024-10-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1bd296b-61d3-322b-b9ef-ebf09abad246 | -9.83539 | -47.56962 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70094538-a3ab-34fe-83b5-972163b8e6b7 | -9.79814 | -48.13476 | 2024-10-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68c28074-644d-38c2-a4b1-77857f2808f4 | -9.76916 | -47.78098 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 206f4006-3747-3662-b5e2-dda583e73fef | -9.71493 | -47.66095 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 749cd761-793c-3008-ba02-05d78bfddd9b | -9.65235 | -47.64589 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8beb43cc-5516-3c76-8fd5-34df8f846e13 | -9.63245 | -47.71721 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbd3c76a-099d-3bde-bca8-01a20d03a1f7 | -9.63174 | -47.71437 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README43.md)
