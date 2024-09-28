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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64919316-44bc-3cc2-be39-c5160e392bec | -10.53895 | -48.05026 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bd3d06b-1d24-3c06-8013-4769f061174a | -10.53833 | -48.05404 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c8bd310-aad1-32ae-b372-21cf5a27da98 | -10.53612 | -48.04576 | 2024-09-28 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58a58e67-ec7e-37da-af8f-049115ddf482 | -10.43104 | -48.19481 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fb3e188-b6ce-3b89-84ba-6a570bbab572 | -10.43034 | -48.19903 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6ec28a5-6a20-32e3-921f-2d233df31693 | -10.42964 | -48.20328 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 520522e8-e71e-32bd-8e2a-fa463932c4d1 | -10.42751 | -48.19439 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de4e9c87-bdb2-31e7-bbc3-07143198bef3 | -10.42612 | -48.20278 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df4dd3a9-6286-35ef-92a9-c7a949b9b306 | -10.42397 | -48.19404 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbcb3340-84b0-3c77-8ffd-bd47e80512d6 | -10.42328 | -48.19818 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 296e2925-8efe-3f02-b487-e89d60db6bb0 | -10.4226 | -48.2023 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7b45cbb-7af2-32e8-9aa3-d1adb84384fa | -10.41975 | -48.19775 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eba3b375-a91a-3056-be25-0089759a258c | -10.41908 | -48.20181 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 907759e6-0f58-3c4c-b65e-07502b9074a8 | -10.41841 | -48.20585 | 2024-09-28 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea31057b-2654-35f6-b140-94db0d850afc | -12.17848 | -47.98087 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 408748d7-e522-39ef-b6ed-203a6a37a7b9 | -12.17506 | -47.98029 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6af83c5c-58fd-3087-9c56-b0458b9245fa | -12.17164 | -47.9797 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e20f00b2-9314-36ca-86d2-b1d6c0e7252e | -11.71786 | -47.83105 | 2024-09-28 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b8b849e-4c8d-36ff-a21f-334b36e6c6e3 | -11.71327 | -47.88076 | 2024-09-28 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8937d67f-2478-32e9-896b-768234f907da | -11.71159 | -48.42481 | 2024-09-28 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94bda170-a239-3e7a-bc83-00b762a510dc | -11.33007 | -48.40683 | 2024-09-28 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f6af1d4-65ea-3e70-b22a-edc2d3ee440f | -13.48164 | -48.58304 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec99a5d4-4181-3cb4-a077-2b0124e5ef6b | -13.47338 | -48.58987 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 628bfe45-a738-301c-bf1e-805e21039e4b | -13.47085 | -48.59022 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c02c2213-d393-3d0f-bd6a-e427890012f9 | -13.4674 | -48.58957 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| addc4d99-acad-35fb-bf7d-f25e94167447 | -13.46589 | -48.57711 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab09116a-b188-30f3-ac1f-8f03b55a401b | -13.46395 | -48.58892 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a87e1c1-1ee7-3d17-944c-ac63cc01dc1d | -13.46331 | -48.59282 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fadade96-74d7-39ca-98f3-f19275dcefff | -13.46267 | -48.59673 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1638bbc3-1077-3432-97c4-775806f54b1c | -13.46243 | -48.57655 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4086f3a-93f6-3450-bb56-714d8b2502f7 | -13.45985 | -48.59227 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00f80668-0991-3870-8887-12e1be786e9c | -13.45897 | -48.576 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bd1b990-f261-3705-bbcf-599edb2a6069 | -13.45832 | -48.57998 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 022fee03-e356-39d2-85fd-57f2e4db2ef5 | -13.45702 | -48.58786 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 062d7c2e-35a4-31f2-91e9-a3a863a7f0c3 | -13.45638 | -48.59177 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86194468-84e9-3e31-9e9f-253902f5744a | -13.23965 | -48.85247 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8db36f83-8d10-3000-9c8c-639478da8f48 | -13.17632 | -48.51596 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5eb1c1a6-ad50-3b56-afd9-ecfb1398072d | -13.1757 | -48.51973 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 397b3792-bb19-3495-bd6e-becd32c0201f | -13.17288 | -48.51531 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c8e9e2f-311a-36bb-a25e-dbb603135d02 | -13.17225 | -48.51907 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 925698dd-cba4-3535-a2c1-17ba791d8569 | -13.17006 | -48.51092 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da90d6cd-2754-36fe-9493-1a3186808f6c | -13.16944 | -48.51467 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 203b7137-7a2d-36b1-bdbc-4388442dd9ca | -13.16662 | -48.51029 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2c52565-1a08-3b38-8619-d04a55260e95 | -13.16599 | -48.51405 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 252d2508-ff68-3c8e-a2b3-91ef0c18b049 | -13.16191 | -48.51721 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7066235c-1d55-3141-8a69-8646b1558270 | -13.15603 | -48.51686 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f2c5c3c-b765-3694-af9d-dfc41f83d905 | -13.15498 | -48.51612 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c12be0df-1ba7-3b35-9827-77dee7f676a5 | -13.15435 | -48.51991 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39c8bf4b-c757-315a-b477-4c186c18360d | -13.15258 | -48.51628 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba7c1bab-240b-3b72-ba6b-7e48f8e3fca4 | -13.15195 | -48.52008 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6688c9ca-a1e6-39bc-8cdc-e0eda8faf418 | -13.17439 | -48.52752 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2700bad-ea46-3601-afd8-ba632c3b7012 | -13.16892 | -48.53893 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0414f81-443a-3bec-9520-7bf2b7f93c35 | -13.16478 | -48.54235 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90b17cec-0637-3a0a-8fed-ef6922e32860 | -13.16133 | -48.54173 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbbc7660-64aa-3827-81b0-ed971920ab75 | -13.02829 | -48.60913 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9392637-1c29-3434-849f-063f3e200fcf | -13.02542 | -48.60482 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d22acb64-7fae-3154-8036-21423252cda8 | -13.02479 | -48.6087 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6caa0c1f-bf9e-34be-a54f-32e5d19f1a25 | -13.02414 | -48.61261 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2a26dc1-92fc-3fdc-8169-f35e50f2d423 | -13.02193 | -48.60436 | 2024-09-28 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 678035cb-dfa4-3119-9f43-3898814ebf11 | -13.78862 | -48.30354 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 833dc143-60d7-310f-b4c0-325f918c0ae1 | -12.52106 | -47.97205 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f7ea18d-c134-3988-adbe-6f798b90a5f2 | -12.52044 | -47.97581 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464bcfa7-0b8b-399e-a34e-dbf4e0ced6ab | -12.51765 | -47.97147 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb79d8e4-c107-349e-9cd1-e658b54f646e | -12.51703 | -47.97522 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd1a39d3-3fdc-3e7b-9534-80ac01867971 | -12.51362 | -47.97464 | 2024-09-28 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b61286c4-dd8f-38b9-89ac-751bb4e11b59 | -12.49541 | -48.60984 | 2024-09-28 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0269eb49-2a05-3811-809b-453bd6a816b8 | -12.49474 | -48.61381 | 2024-09-28 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c579232-6d86-3f80-ae92-d8ecb0681bc8 | -15.05106 | -49.16885 | 2024-09-28 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36f80126-f7cf-3f21-b1c6-1996cfbdd12e | -14.85923 | -48.92812 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54f8c1fa-af55-370b-8c34-187cad1e577e | -14.85579 | -48.92747 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 891f2422-ea50-332d-97e1-48646add213a | -14.85233 | -48.92689 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e800aa48-4456-3cc8-ab06-32a05efed165 | -14.85164 | -48.93097 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0c7bd540-7a41-3ff4-abb8-d8aed4dfde21 | -14.84886 | -48.92639 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8991a6d5-f239-3741-a7ee-aa22ab49bf8f | -14.77433 | -48.89034 | 2024-09-28 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97e5d17a-9d76-3111-a1b0-6657cd50cd8b | -15.34747 | -49.5223 | 2024-09-28 04:21:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c980d6be-9c7a-3cd2-b895-9c3d324818b0 | -16.42959 | -48.89973 | 2024-09-28 04:21:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac739649-73fa-3271-b4ba-87a5882d1de7 | -16.24864 | -48.93129 | 2024-09-28 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f07644ee-3a3c-35be-acc0-e4a69359bc4b | -8.75323 | -49.78293 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ade3eaef-180c-3181-932d-7d305af77b6b | -8.75239 | -49.7879 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| fd83c48a-4722-3f67-aef4-6c93a68ed6a7 | -8.74449 | -49.59967 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c896aa7b-0b26-3740-9fde-aa1ee1a489af | -8.66518 | -49.42555 | 2024-09-28 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e91cd34-5c57-3df7-9e52-6e0c2ce4b4ee | -8.64224 | -49.4907 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 707cd576-b19e-33a4-a13f-4abef4609c57 | -8.61358 | -49.48329 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc39c593-d1a3-3986-8dd8-2d96db14fd4e | -8.55701 | -49.60814 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1caf2004-2ff6-311a-8e06-9d5009ca1c08 | -8.55396 | -49.60266 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4830bb7-4007-3a31-ae22-134aef2cad44 | -8.55314 | -49.60751 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f802fdcd-d48d-3eeb-9468-bb8ef7965b9c | -8.55232 | -49.61236 | 2024-09-28 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b36ad53-68ac-379e-878b-613327ebe78e | -9.28555 | -49.11663 | 2024-09-28 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43ef7fb7-b563-3dde-9664-8aa505214196 | -8.97563 | -49.82627 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e1d564fe-8f4b-3e71-901a-9104e68d9790 | -8.93637 | -49.72808 | 2024-09-28 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45942adc-86ab-3652-8a25-e114f58c6b8d | -8.89822 | -49.63895 | 2024-09-28 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7817934-44a2-390f-9c29-a2ecf958d12a | -10.76637 | -49.85905 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc52bdba-ccb0-3e1f-9215-8e2543c494fb | -10.76257 | -49.8584 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e143deb0-ce01-3f01-8630-eba8aea718aa | -10.74773 | -49.22378 | 2024-09-28 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0250872-0726-3a1f-ae03-ee9c1ec8d1e7 | -10.74406 | -49.22313 | 2024-09-28 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bac5f1c0-d073-3cb4-8cc4-6c1aafb3233c | -10.63951 | -49.91709 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e76ea56-2878-3db2-becd-1c297ef0c308 | -10.63723 | -49.91428 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2970990-ccc5-3ad0-b732-8d41a1d307d5 | -10.63642 | -49.91908 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35b28988-4330-3170-82ac-53310d8136d4 | -10.63568 | -49.91644 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e6c542c-2ccd-3252-bc65-ee489646529b | -10.63485 | -49.92122 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
