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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d521f19c-8161-3a5e-a327-cc00cc9aa1e7 | -11.0455 | -55.3773 | 2025-06-28 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 2105fa95-c831-3c5f-a93b-79d87c021b60 | -9.7228 | -56.183 | 2025-06-28 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 69cdd1f0-1c86-3a22-994c-0471ff475355 | -11.0457 | -55.3571 | 2025-06-28 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 808ded25-fd93-3ee4-baf4-875df21e1efe | -11.0644 | -55.3757 | 2025-06-28 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b5c1f012-7f84-3f5a-9274-204ef1ffb506 | -9.1208 | -49.4743 | 2025-06-28 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a40efeb8-2f61-353b-bb59-6fda04848ace | -12.2715 | -46.7739 | 2025-06-28 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 11ec5a67-d148-3a84-b0fa-708eb67114e8 | -9.7041 | -56.1843 | 2025-06-28 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2943fba5-005b-3430-974b-573061d4e4e6 | -9.1205 | -49.4958 | 2025-06-28 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0ef90c07-6c77-32bf-b1d6-94af9017c1d6 | -7.2217 | -43.0917 | 2025-06-28 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 211ee980-af0c-31fe-91f9-a3fc8f14114a | -9.7228 | -56.183 | 2025-06-28 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1acf7e8a-b795-32bd-88da-fe32b52c2378 | -11.0457 | -55.3571 | 2025-06-28 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ec3c4c5c-2ba4-307d-b375-152d78fe786b | -9.7041 | -56.1843 | 2025-06-28 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9dfe748f-7a05-313b-b9c3-5ce5a0e607ef | -9.1208 | -49.4743 | 2025-06-28 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4b6533c3-6401-3b24-ad30-ab87dbcf7b18 | -11.2853 | -52.7508 | 2025-06-28 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 98fe4094-44aa-3094-ba5b-aaeef9c36a17 | -6.9416 | -42.8834 | 2025-06-28 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| ad37ed13-8e16-3564-bffe-5c93ac46ca60 | -7.2219 | -43.0682 | 2025-06-28 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| cc717e67-b997-3256-ad00-76487d21ce0d | -9.1205 | -49.4958 | 2025-06-28 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4c642906-4c35-3251-8ace-eeca8a9fb7c8 | -7.2217 | -43.0917 | 2025-06-28 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| c1c1ca61-a3c9-33cf-9fb6-fab7f0c994eb | -4.5429 | -48.0151 | 2025-06-28 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 50b48d2b-6ee9-3af0-acb2-961ae1d1b7a3 | -11.2664 | -52.7527 | 2025-06-28 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cd88d946-c642-3dce-9df5-3c72d95c366d | -11.0455 | -55.3773 | 2025-06-28 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 523a882f-f9e5-3c9a-b0b8-5d92c3bf8b72 | -11.0644 | -55.3757 | 2025-06-28 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 98c429f0-f8c3-3449-9054-aca5235d3e1e | -6.9108 | -43.9834 | 2025-06-28 02:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| beb00726-1145-3358-a4e6-583fbb4f8315 | -11.2664 | -52.7527 | 2025-06-28 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 520f9233-7f18-3962-892f-94813abfe1ce | -11.0455 | -55.3773 | 2025-06-28 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 173.4 |
| fee7cfac-b7b2-365a-a8f8-74da02bf7375 | -11.0457 | -55.3571 | 2025-06-28 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ca4d6050-26c5-337d-8666-dbed5227bbbb | -11.0644 | -55.3757 | 2025-06-28 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| de83061a-4c32-39c0-89f9-9f228274c5d5 | -9.1205 | -49.4958 | 2025-06-28 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7e388901-0026-3ff7-8563-2ad628244cb3 | -9.7041 | -56.1843 | 2025-06-28 03:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5b62f22e-1101-3748-b0fe-fb41f6e4cf0d | -7.2219 | -43.0682 | 2025-06-28 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 4f47603c-9ab1-3544-bc18-7e0e9137c15c | -7.2217 | -43.0917 | 2025-06-28 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| fbe7afaf-7124-3851-8006-3c55c20149c9 | -9.7228 | -56.183 | 2025-06-28 03:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f2074a3c-f543-36b9-939d-de5a5929a409 | -4.5429 | -48.0151 | 2025-06-28 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0177f60e-f2be-3b08-ae41-22bee95fba81 | -9.1208 | -49.4743 | 2025-06-28 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7227292c-e0ab-3f45-8832-87b992da0550 | -6.9416 | -42.8834 | 2025-06-28 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| a1e3d2c8-742a-3429-b77a-c9b0f628032c | -6.9108 | -43.9834 | 2025-06-28 03:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2f254ed0-183c-3e53-bddc-8a5e29ec79cd | -4.5429 | -48.0151 | 2025-06-28 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a399c65a-7441-32dd-a1f6-3abb7d5b4c75 | -11.2664 | -52.7527 | 2025-06-28 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 2900a8c3-e28f-3a92-b3d7-2a353f2aad84 | -9.1208 | -49.4743 | 2025-06-28 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 0f568626-2281-3fed-94cb-a28b2771a1d4 | -11.0644 | -55.3757 | 2025-06-28 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3e3edeb1-eb57-3171-9862-9628b8a5ea60 | -6.9416 | -42.8834 | 2025-06-28 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 5a958e33-da6c-30fb-b77d-96729329fceb | -11.0455 | -55.3773 | 2025-06-28 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 0e6354b4-f7e5-3344-8914-53cedcdd526e | -7.2219 | -43.0682 | 2025-06-28 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 44ed6d6e-4e05-3ec9-bdb3-b9ae114c55f7 | -9.1205 | -49.4958 | 2025-06-28 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 27299d25-88a7-3be5-8ab4-ca780d7fc062 | -11.2853 | -52.7508 | 2025-06-28 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 14162838-ef2d-3d15-b6f5-4129ad110612 | -11.0457 | -55.3571 | 2025-06-28 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e7cd81fb-a680-34bd-9a8d-029f7e7d99c6 | -6.9108 | -43.9834 | 2025-06-28 03:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f26520ff-d070-3030-9c9d-b03eaae8cffb | -9.7041 | -56.1843 | 2025-06-28 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 35595e07-2a7e-3512-9b39-b547cb3ae235 | -9.7228 | -56.183 | 2025-06-28 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ffaddf0c-ee18-3685-8441-facc58274eba | -5.24582 | -35.68699 | 2025-06-28 03:10:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1f391514-0f86-3004-98d0-e934fc6b9f28 | -13.94454 | -43.24085 | 2025-06-28 03:13:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c904889e-7c3a-36fd-b0f7-3458beaf7ff9 | -21.33419 | -45.41557 | 2025-06-28 03:15:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 9045ac5e-8cec-37e2-bc9e-2dff7eb28a14 | -21.33235 | -45.42298 | 2025-06-28 03:15:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 1dadfe6c-579f-30f0-91e1-388a7797d52d | -21.1104 | -45.71427 | 2025-06-28 03:15:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fa975925-454f-33c0-8d5b-641a9733ca70 | -21.33075 | -45.42437 | 2025-06-28 03:15:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| e56c79fc-126a-3731-a2af-72359ec31f99 | -21.10671 | -45.71414 | 2025-06-28 03:15:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 682e960c-a144-37a7-af18-a07830665dc2 | -21.33262 | -45.417 | 2025-06-28 03:15:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 719a9abc-fa3f-372e-bbcf-08d944e57181 | -20.85254 | -45.53526 | 2025-06-28 03:15:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b34a3ff8-6125-31ce-897a-d4bb2fb57a8d | -9.7041 | -56.1843 | 2025-06-28 03:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 81cbb686-503d-332e-bf8a-f7572a0b62fd | -9.7228 | -56.183 | 2025-06-28 03:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 91b4bd5c-86a6-37f6-8ce4-957b84058805 | -11.0455 | -55.3773 | 2025-06-28 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| c5c865d3-7619-3a92-9672-1663a56d7baf | -11.2664 | -52.7527 | 2025-06-28 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 836750a6-bfc5-328e-9f90-3074f8a568dc | -9.1205 | -49.4958 | 2025-06-28 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ee1e3a7b-3ecc-3dbe-bd08-1ded531ff858 | -11.2666 | -52.7318 | 2025-06-28 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b5914d08-cf39-3db4-93af-396707344047 | -11.0644 | -55.3757 | 2025-06-28 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0611fc74-8465-34ce-a738-1dbe4a4208bf | -12.2523 | -46.7766 | 2025-06-28 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 2a9041ff-edb2-37cc-b9e8-584f3a9b2c6b | -4.5429 | -48.0151 | 2025-06-28 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 893e114e-4028-3987-9292-d7c170961c4f | -11.0457 | -55.3571 | 2025-06-28 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5e92702e-5a07-383d-82fe-90fd5532df0b | -9.1208 | -49.4743 | 2025-06-28 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| eba3f6f9-068c-3a31-86fc-da970901deb5 | -4.5427 | -48.0367 | 2025-06-28 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b91e3adb-abb4-3ea3-820a-8815ee786e9a | -7.2219 | -43.0682 | 2025-06-28 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 295902d9-0626-35ce-a0dd-621a7cc75656 | -11.2853 | -52.7508 | 2025-06-28 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2c092ce5-72f2-3b37-8654-48608c9351e3 | -6.9108 | -43.9834 | 2025-06-28 03:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9a4e740c-fa6f-32e2-aa83-0064d0f06be6 | -11.0457 | -55.3571 | 2025-06-28 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d71f6a28-12ea-3fea-8e02-4ff9678756a3 | -11.0455 | -55.3773 | 2025-06-28 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 329ae8d4-eb94-365a-b714-8eb8d3167b80 | -9.7041 | -56.1843 | 2025-06-28 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ee6bb558-4d49-3aa0-9be4-91d44e33ca28 | -11.0644 | -55.3757 | 2025-06-28 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| f8d20f33-710c-378c-a81b-84f526460117 | -7.2219 | -43.0682 | 2025-06-28 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 265d31f1-712d-390f-93ef-6d10062f3d3d | -9.1205 | -49.4958 | 2025-06-28 03:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6cea47fe-0e64-32cf-86b1-acbd974e57dc | -9.7228 | -56.183 | 2025-06-28 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7679085f-e29f-3ead-8547-af8bcd266b30 | -4.5429 | -48.0151 | 2025-06-28 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b6d08c5b-52fd-3088-a1ce-a4372f43be38 | -9.1208 | -49.4743 | 2025-06-28 03:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ccccb532-53b8-34f0-b21d-d86075a481fd | -6.9108 | -43.9834 | 2025-06-28 03:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fe2bf988-d758-39c6-9306-16ea6e8caddf | -11.2664 | -52.7527 | 2025-06-28 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 7bdaa59f-1573-3b9c-8859-66e762cf76d7 | -11.2853 | -52.7508 | 2025-06-28 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8ccb4bd7-baa9-34d8-986f-83bd48d2a4bd | -12.2523 | -46.7766 | 2025-06-28 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| abb218a0-c533-3e12-b7f9-e866215f67cc | -11.2664 | -52.7527 | 2025-06-28 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 20f55fb4-38b4-37fc-a250-54e58edac599 | -9.7228 | -56.183 | 2025-06-28 03:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 37539b85-8066-3623-b877-cb7d2d643e4d | -11.0457 | -55.3571 | 2025-06-28 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1e19c6bf-1e73-334f-910e-9f7ca050b401 | -4.5429 | -48.0151 | 2025-06-28 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| afc298a8-673a-3134-a1b8-bb500e527d89 | -11.0455 | -55.3773 | 2025-06-28 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 96c26631-de73-3610-8189-da501b50c207 | -11.0644 | -55.3757 | 2025-06-28 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5bbe6ac2-3f8b-3cca-a279-8c7fbe3bcadf | -9.7041 | -56.1843 | 2025-06-28 03:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0b594617-699c-3814-8221-2f86254e98f5 | -6.9108 | -43.9834 | 2025-06-28 03:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b80249dd-480f-3a59-acab-66f75479f070 | -11.0644 | -55.3757 | 2025-06-28 03:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a66bb4f9-239c-305b-b67a-6f21544c899a | -6.9108 | -43.9834 | 2025-06-28 03:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e6196473-7b92-3ac8-9d47-c9b6f5eacca7 | -12.2523 | -46.7766 | 2025-06-28 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c9a14232-4fcc-3bf5-954c-9abb69f42844 | -9.1205 | -49.4958 | 2025-06-28 03:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 407d8d5a-2f2d-35d7-a585-023976f648f6 | -4.5429 | -48.0151 | 2025-06-28 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 762afbd1-6c6a-39ca-8ca6-0688d36d4a2a | -9.7228 | -56.183 | 2025-06-28 03:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |


[Clique aqui para ver as próximas entradas](README9.md)
