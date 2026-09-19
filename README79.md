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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c68403e-6f7e-3011-b033-64d3d036493e | -5.76419 | -57.45867 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ef1a349d-2ca5-36b2-84f5-cc1c64381b62 | -4.50768 | -54.9673 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4081134a-f4fc-399b-b27d-7d7d276aa9e6 | -3.55498 | -51.53668 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef042487-dc45-35cf-8f15-ed13814e8440 | -7.44105 | -44.6995 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8118d52-aff9-30c2-9364-dc24c4a42ca8 | -9.76218 | -53.80558 | 2026-09-19 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee7f5a1-e3fc-32ab-907c-15570de78da8 | -6.18984 | -53.47358 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7354b113-74ed-3374-9bb1-93f42f759e52 | -7.55585 | -61.32795 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8976533e-f29a-3611-8628-506d06f31577 | -3.73829 | -54.6428 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a3f72fc-17d4-3c86-aa8e-d1ccbcae2736 | -10.20886 | -46.58991 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d6f70cb-5f19-3f27-946a-220aba6162b9 | -11.06939 | -48.32092 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd46cb04-2287-3111-8936-7ee10467b8e3 | -5.85869 | -51.94036 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9589f55-3a33-33c4-82bf-049d544e9f58 | -7.32289 | -45.33126 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f5e61829-e876-3f32-bd9d-df70307fca00 | -10.50176 | -46.27255 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6b4dbd4-1b49-3b11-84f7-8b71c2147d75 | -8.76941 | -46.91358 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 86395b30-5229-38ef-b77c-9ef34f4f5ef3 | -9.92816 | -46.59019 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 02217b2b-d3e3-3c1f-b14c-8eca4a643903 | -4.36007 | -47.78312 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d3f2dae-898d-3221-ac56-5f0da5b15e49 | -3.82118 | -50.74781 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce0c4041-5720-3464-b0ac-b2a24a7d8ce8 | -3.36028 | -50.44439 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e54acc3-e266-39e1-b0db-9895e1be4c9e | -8.0936 | -54.86594 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9c08880-d61d-3245-b841-f4017b1c378e | -5.99909 | -51.8046 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da7c5948-53b8-3bfa-8f1a-9531ff657f37 | -5.85167 | -52.07128 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f76f0e8e-9abe-3203-8125-4219da8cfec4 | -3.45087 | -50.60282 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b1a12f6-63df-374a-a4a1-5ad8a1af2249 | -10.80334 | -50.89624 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5128a04-0fa4-3b67-9df3-09c6bf38e315 | -5.97612 | -55.36314 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a68c9646-a54a-32a1-bbf8-7f692630a08d | -5.85593 | -51.9363 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6023de14-4a98-37ad-adf9-86c9e0efa704 | -10.16968 | -48.51645 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2051f8e-f46a-3069-90c3-2ecc40ffac6d | -6.36029 | -58.28471 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a341787-0f70-31d0-9c68-4c14cbbc06ab | -6.75683 | -56.32663 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0abe3991-8fd6-3d1d-a9b0-52084ef05e50 | -10.4771 | -51.33564 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| beecbd1a-de21-30c2-ba37-b7e72c94c5e6 | -11.30565 | -46.75836 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c6a16ce-b753-3991-ab69-ffa12e8f9941 | -4.51282 | -54.98023 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01411f92-ac01-3b0b-9895-7441b43e5f0b | -9.69919 | -54.83119 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48142c85-8a23-3d92-8fe3-32c95c6a9373 | -3.73704 | -54.65047 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a13ba1c-a293-390a-9ce5-4c672ade0adc | -6.08601 | -55.55534 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea904e0-b72c-3ddb-88d0-4e8c83495259 | -5.86146 | -51.94442 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73facdfd-acdd-3a32-b382-96d1464203f4 | -3.49866 | -49.51485 | 2026-09-19 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f83d48a-cef7-34d0-8d02-ec964d1c21e2 | -4.51055 | -54.97188 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6635bcc-cc39-3177-bcc0-0a0b4aba89c7 | -9.71277 | -54.81121 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44dc4b8-9a91-3993-8c4e-c527fee9b07c | -3.76 | -51.13913 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f1ef958-00f1-33c9-9980-b7956667b59a | -6.65519 | -50.92653 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96ae19d0-839a-3bdc-ba28-1ce4e3718618 | -10.40079 | -48.32312 | 2026-09-19 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ac6c0a3-9d79-39a9-9a4f-4b5147355dbd | -9.89829 | -46.53759 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1867b65f-5225-3735-9029-1f6e235ce5ef | -8.44267 | -45.70076 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b9bebcc-3771-3d73-9746-dd1ac640d905 | -5.86201 | -51.94092 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beacf467-9ac9-3672-9599-64c20b773abe | -3.43897 | -53.29633 | 2026-09-19 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e48fa9-8939-3d36-8251-49c96a88ceb1 | -10.09661 | -48.41652 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3e06ff4-dcd3-36ed-8c7e-a402d1765380 | -8.44295 | -45.70038 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5602965-d0a4-3dc9-a449-3873c3957364 | -2.89746 | -54.18568 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e9bb27-a9d6-328f-adfa-4070eea5adbe | -8.50242 | -57.63558 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a23d9ef-fabe-32b1-ab94-3e242f1e81d2 | -6.65923 | -50.90043 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19bc7b04-56a8-31c9-a2e9-5b6a937ba78d | -6.57832 | -44.16074 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9699b1-8235-3294-b84c-0dbed5e840c9 | -10.00371 | -50.27656 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1fac262-b5ab-33b5-9357-ebe23bc5f718 | -9.03389 | -48.75856 | 2026-09-19 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c728118f-d42c-33b8-b745-6cd92c726513 | -5.86974 | -52.04249 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0353bfa-bcbe-3af3-bd79-fd28b1565f11 | -11.46594 | -45.71214 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92366605-09ad-318a-8681-9e5c72ab8645 | -11.33389 | -47.35907 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9db7b23-0bae-34d2-83c4-7c57207fea0c | -5.73705 | -52.23824 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9022b6e2-73d9-3366-bf6c-c2fb54629cf6 | -8.006 | -61.37544 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 742b2ce9-3cb1-3691-b287-d17ab1a4b993 | -9.90975 | -46.58742 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7f5f200-de63-3f9c-b891-d187f40f4714 | -8.41575 | -54.71926 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e1a539-a3e5-30ed-83d7-e739d6ee0947 | -5.2276 | -47.56323 | 2026-09-19 04:57:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93c4d350-59d3-378e-9be8-21d699233611 | -10.45276 | -48.68419 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e16bc4da-6219-3293-898d-5ea6ed906cdb | -9.1568 | -49.99556 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df1ca06-7235-34f3-9c74-215d143d5e13 | -8.0058 | -61.37339 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9c0e0ba-fbeb-3b63-a078-30c752d0c1c1 | -5.75578 | -57.44494 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bdec090-e77a-3763-b5f0-23837daf14a9 | -9.34079 | -48.19031 | 2026-09-19 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33c14bf8-f32b-333e-90e7-33fc561a03d1 | -9.35201 | -50.11432 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d173ea0e-6580-36c4-b48b-4f4b2197bb54 | -7.61231 | -45.43026 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a0f43cc-11cf-3730-a08a-a678ab03ff93 | -10.93185 | -47.91645 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a477aa4-5a64-361c-8190-c25103f4db42 | -8.60283 | -54.5982 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a41b4e09-cb58-3175-a0f9-842dab43d209 | -9.76664 | -46.07719 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 244f9467-ff13-3768-88c4-b0e47290ad85 | -8.01077 | -61.37428 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adb9ce66-3659-3c8d-be0d-b85f02224c45 | -6.66889 | -50.92867 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a52dc7b4-3e16-313d-9162-00fd848efd9b | -7.79274 | -44.85056 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bc2d539-af7b-319a-aef9-a306145ae256 | -7.19462 | -50.83423 | 2026-09-19 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| faac879d-6389-3626-bd08-2faf2bd90644 | -9.71948 | -54.81229 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb13b27f-1993-38f1-afda-b949469e6b79 | -8.42469 | -54.72815 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ae4db78-90a6-3f58-960e-0c8ac35265cf | -8.66721 | -45.44188 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abc406f6-aef0-3191-a8b6-4e3da1721eb0 | -6.32604 | -55.28183 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990184b6-1af8-345a-992b-98531d9649b8 | -10.98376 | -48.29531 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 896fe3c0-18eb-39aa-9a00-9b152b73dde5 | -3.46608 | -50.61625 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57803b92-c661-3407-b8c2-e1a3672c7c76 | -10.92715 | -47.85443 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ca5d4c-f850-3e95-a6c4-e753bb43d158 | -7.38212 | -47.75365 | 2026-09-19 04:57:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 523f0437-e99d-3386-a9d7-8e15e37230ff | -9.5643 | -45.48082 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0a1b359-fa94-39b5-80e4-0d51eadf3c2d | -9.70767 | -54.82143 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9439904d-734f-37ad-a3a5-313d0d29e01a | -3.55444 | -51.54015 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b65c556-f083-38e3-8cdf-2e0a9f672adf | -9.04936 | -48.73529 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 547f2286-372a-3ceb-be6e-bff7cae467f1 | -3.03988 | -51.37762 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c43f8f1-a996-300b-b96b-959d01ffdc98 | -7.40929 | -49.84449 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1224b8a-ba64-30b8-b171-aef715ccf390 | -7.75506 | -46.72431 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d716b449-aa6b-3a06-8064-f5f9aca184b9 | -3.51877 | -50.7967 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c29f873b-e707-3c95-a24b-2d45f98828fe | -7.37503 | -44.73479 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 387bcdc1-7040-3aa4-b62f-18f0d242c93c | -7.64518 | -46.1024 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82e513cf-2087-32c5-81b4-411c5720fd7b | -10.0961 | -48.42019 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5736e983-79e1-38d8-8638-b420009813a0 | -4.88115 | -56.07035 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a68684f9-31b9-3a25-bd28-ef4dcadd01b4 | -2.89057 | -57.79855 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a610fed-a18f-3c70-96d8-abab3f836d7b | -10.36562 | -50.4562 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50894c8a-1f66-35e9-9138-025975238ea0 | -4.43574 | -55.07728 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48a4effe-971e-309a-9a00-a4f081bf9345 | -10.79929 | -50.87463 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d68cfb0e-c0ff-3d26-8219-25a8f48b80dd | -10.23794 | -48.84562 | 2026-09-19 04:57:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README80.md)
