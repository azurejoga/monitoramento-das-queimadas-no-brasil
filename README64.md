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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b476c49-d324-3556-952d-49242fa56ee6 | -9.91637 | -47.73093 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f6d33a1-7e4c-30f2-ab3e-3ac19ac0dba5 | -9.90242 | -47.72871 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d6f9a7-a0ed-3b21-b0d9-23e48b59d5c1 | -9.8877 | -48.27188 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b782763-2f74-303b-8b97-42f88e09f58a | -9.88428 | -48.27137 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d646ad-5c37-3f0b-be0a-3830248ecd5b | -9.86096 | -48.24067 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cad22a0e-9380-37ae-af5e-14427cc5322f | -9.85754 | -48.24012 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8cb6a67-73e4-3b73-a296-b2901278f2ea | -9.74962 | -48.30441 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e4af2a8-229e-3c54-9f1d-e54e169cdbad | -9.73992 | -48.29939 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e90a6c9-ac3c-35db-ba29-06ddf66bbccb | -9.73767 | -48.29118 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40dbb6f2-93b4-3323-9f98-5e1a852efc26 | -9.73708 | -48.29508 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 178a232a-fc99-3a3e-9844-4bd24d4b7ee8 | -9.7365 | -48.2989 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afdcc5fc-19b7-37a2-a78e-8f11bbd93c91 | -9.73425 | -48.29069 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6eb47b6-3545-3bf4-a615-eb5535392d4b | -9.70703 | -47.77316 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74cf9555-15bb-34dc-b993-53227ab85654 | -9.65681 | -48.5956 | 2024-10-13 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 742c0a1f-0e8a-394c-90ca-2383816c2527 | -9.6511 | -48.56478 | 2024-10-13 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd0ff2c9-eeb2-3c4f-bc63-bc8e287efdd8 | -9.52965 | -47.8062 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e707b95-4daa-3e49-a027-190f80b99718 | -9.52738 | -47.80623 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faa4f887-6a95-3a2a-882c-8ce031b60ca2 | -9.52332 | -47.80957 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6f78b0e-64a6-33f2-b69c-e48dd17c7331 | -9.51986 | -47.80903 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9df04655-d88b-36bb-8c65-e09c24cdca0f | -9.51639 | -47.80848 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d59f25f0-c7e0-3ce6-b9be-1f7adb1413e7 | -9.51293 | -47.80794 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b05e5f9-889f-36a8-9af6-ea567a41e574 | -12.1871 | -47.98724 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a224fbd-0cda-3e56-b972-7932e2043140 | -12.17757 | -48.05173 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3078fc35-d4b7-3ecf-844d-06b948084f53 | -11.87199 | -48.16632 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 445ac8a6-62c6-360b-a164-af38a3a4cc19 | -11.83776 | -48.80171 | 2024-10-13 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dd3d6da-17d0-3e04-b656-e0e29a00140a | -11.74465 | -48.36691 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a3aeafc7-4b45-3984-9e09-2a28e2a618fe | -11.74409 | -48.37077 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| efa677e1-1d4e-3745-a1b7-4ab62d20f1ea | -11.7412 | -48.36637 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0767268d-6c06-3546-99cf-281578d60e02 | -11.74063 | -48.37023 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e054788a-9b06-305b-9a59-c688c5594a43 | -11.66183 | -49.06314 | 2024-10-13 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1482a0e9-8353-3771-adad-cda1d54a19a1 | -11.66127 | -49.06681 | 2024-10-13 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52c7532a-d7e9-3951-8670-be038768dee5 | -11.63676 | -48.38671 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b069ed7e-11db-3660-9dc3-2039a1a9bd1b | -11.63619 | -48.39056 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6b9b4ab-cf37-3100-a5c4-f0a0b823c5fa | -11.63562 | -48.39441 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9a82a59-aa57-39e1-a61c-510d816cbe00 | -11.63387 | -48.38232 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2b1bdb3-01c7-37e7-886b-9a031aae5f72 | -11.6333 | -48.38618 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c07ec91e-2c2d-3dfb-aff8-c2c57e1479db | -11.63217 | -48.39388 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5eed14b-d2ad-37e6-8a88-a0f79d6d202c | -11.63098 | -48.37794 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a6dcdd36-b523-3b91-acab-a16011a40937 | -11.62809 | -48.37355 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5b8cae89-49f2-3fd4-8e26-5b3c0568d8ca | -11.62753 | -48.37741 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3c87795-346c-36fe-890c-c1676cd9ee18 | -11.62583 | -48.38897 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdfcd0da-d471-3273-beeb-17aed23a380b | -11.6235 | -48.38073 | 2024-10-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b2f9eaae-1a7d-38a6-8aed-913bfbb5fd4f | -11.59535 | -48.47949 | 2024-10-13 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7174cee6-5f4f-3144-b779-f89d9feee76c | -11.59477 | -48.48331 | 2024-10-13 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eabb7896-dc93-3a5c-ae03-ee3391db77dd | -11.59419 | -48.48713 | 2024-10-13 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e21aa2f1-cf9e-3203-ba6c-0798d107f49e | -11.49363 | -48.59586 | 2024-10-13 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4787d2ca-283e-3f2a-8c6e-fc5f14e06dc5 | -11.20848 | -47.85197 | 2024-10-13 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d28bc4ef-eba2-3466-bedd-ef20d67be861 | -11.20555 | -47.84745 | 2024-10-13 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5abdba08-6dd5-32d8-a83f-b3b8df2cc189 | -11.20497 | -47.85143 | 2024-10-13 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e376ad31-a8d6-35e2-a04b-3cc55f5f0b0d | -5.0645 | -48.06158 | 2024-10-13 04:40:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4a24802-ee61-323c-acee-6c58d8a22315 | -5.06395 | -48.06509 | 2024-10-13 04:40:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afcfdef6-802a-3222-a0c7-0161e0e6f541 | -4.9884 | -48.46439 | 2024-10-13 04:40:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3397ea64-e210-3352-bd82-eb468e7d631a | -4.93033 | -48.00509 | 2024-10-13 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 839626f2-f4d1-3752-9fee-cc97e5a604d8 | -4.84035 | -48.93222 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc7f998c-1096-31f2-bad0-ada56e9e2ae8 | -4.83981 | -48.93565 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4226f063-1cec-3162-922e-3c4248b4246b | -4.83927 | -48.93909 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e6fedd-2b99-3631-ba40-d72e52712dbd | -4.83873 | -48.94253 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b63d2a1-7ed9-3b5f-b3e7-64827c71cf49 | -4.78919 | -48.08355 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4c9dfe4-397b-3324-8a10-f307401d2042 | -4.78864 | -48.08704 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8fd0324-c1c6-35d1-bb0e-223a38ec579b | -4.78011 | -48.88001 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83b40be-c51b-3296-acf3-4c2d0318a725 | -4.77681 | -48.8795 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52ca5a0e-cbeb-3db8-a843-1409636fabf1 | -4.74107 | -48.87042 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5795f90d-f529-3ea0-a11a-1095501b082f | -4.73837 | -48.88761 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5793ab1-610e-3f67-8290-ae00d9f1e40d | -4.7383 | -48.86647 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4a966de-7c52-3c81-9636-3ad73310cc86 | -4.73783 | -48.89104 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 915b27db-918b-352e-8083-39f460d1449c | -4.73777 | -48.86991 | 2024-10-13 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7d63119-c9d1-34fa-ba81-950246787747 | -6.06268 | -48.13986 | 2024-10-13 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca9d01d8-d209-3409-a4a8-d0360ef4c6b1 | -6.05933 | -48.13935 | 2024-10-13 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 848a59ee-80fa-3424-9ddf-cb5d08a53b0f | -7.02042 | -48.32413 | 2024-10-13 04:40:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd8033c2-7fd6-3012-8de9-58b905840ce5 | -7.92444 | -49.07473 | 2024-10-13 04:40:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41f1147a-dd19-306c-a25f-b9ac8c5cb3c9 | -7.73283 | -49.21264 | 2024-10-13 04:40:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bcda02f-7178-3d1c-a21a-fd5416441400 | -7.58267 | -49.58572 | 2024-10-13 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c726aa69-ba0e-3baf-8c9a-62b1e21c293c | -7.57937 | -49.58521 | 2024-10-13 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7836a6-a15e-33ed-8498-18662d66d720 | -7.29079 | -48.77469 | 2024-10-13 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b12cabc8-f99f-3f20-871a-35b2cf2c865f | -7.26389 | -49.51384 | 2024-10-13 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ff0084-b62d-3b37-a2ea-58e801c3990e | -7.15289 | -49.15984 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 765db37c-ae59-3e72-ab05-3f0d77202203 | -7.12087 | -49.14424 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5256dd2a-ca16-317d-aea6-2ea93a55581f | -7.11756 | -49.14372 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3610c354-7d80-32f1-abbf-f33406aab3d3 | -7.11426 | -49.1432 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e4de84e-a9a2-372d-a059-b563e41d8e9c | -7.11372 | -49.14667 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8b527ad-aae0-3e10-bf67-d091a161fc69 | -7.10879 | -49.15654 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20d73982-c3b9-3d67-86c5-68195e804ccd | -7.08816 | -49.87516 | 2024-10-13 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63193950-42d2-3ac1-8366-b6848ee33842 | -7.08761 | -49.87862 | 2024-10-13 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efbd4ad5-949a-35d2-8956-8a909af13cb1 | -7.01299 | -49.31518 | 2024-10-13 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d878852-d5cf-3db4-8520-5c3c98317871 | -8.13922 | -49.1373 | 2024-10-13 04:40:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ea9d167-0cbf-3085-928f-8a82f8cae547 | -8.0564 | -49.38472 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71154077-b033-3e88-9fe4-6b37f784def8 | -7.98125 | -49.69223 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63b53bda-1a4f-3f36-9734-7f8f9827828e | -7.97405 | -49.45707 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 599e2193-e736-39dd-8155-9540b8dc98a2 | -7.97351 | -49.46053 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c09cd89-c790-3e32-8674-c9fe0c17db39 | -7.97075 | -49.45655 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84d8284d-0570-3fef-b337-e612e81f4096 | -7.97021 | -49.46001 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 771122fe-ac3a-3853-8a30-4e60b2530522 | -9.30269 | -49.63966 | 2024-10-13 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08e14a25-136c-3d77-ad67-0cc72d816b73 | -9.18058 | -49.65916 | 2024-10-13 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd700488-7b43-37b1-8914-4e1b887bad42 | -9.18004 | -49.66264 | 2024-10-13 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90faf25e-60c8-3232-a7e4-198e99bad3e5 | -9.17674 | -49.66212 | 2024-10-13 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 206f1018-3544-3ec4-a706-39aadeddac74 | -8.96426 | -49.03618 | 2024-10-13 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7d0cd9b-6026-308e-8af0-a9e5d22a6b9e | -8.81577 | -49.86081 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f848969-27ab-3450-a5c1-8b4f382532a0 | -8.80754 | -49.87017 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e10a2b-64bd-3dff-9f4d-45d96eaf1720 | -8.75606 | -49.78394 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d66dc2c-f27f-3b9e-a5c9-d4dabbedb3af | -8.74522 | -49.61507 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README65.md)
