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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5c0482-fd99-3558-8add-b5e346427832 | -14.80113 | -48.53764 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5adcb19-0472-34c8-bea8-0fd646a48734 | -11.39108 | -51.41765 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5766c14c-9da8-3a92-8603-21e6d78612f3 | -12.74798 | -46.20005 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36e4319d-97ba-3605-984b-332e50c9d523 | -13.94568 | -47.84459 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3cef50e-c9fd-355a-b686-0490d7e0b963 | -14.68168 | -46.69242 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d9f1c75-09ca-39ae-b3ad-96579d1f32a6 | -17.02136 | -47.15215 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 916d0287-d61d-3757-b80a-279d7985ec5e | -11.4812 | -51.477 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6cc0649-73e4-31de-9c19-92e5eded5142 | -11.0165 | -54.13951 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30525d14-058a-30c5-a79e-9a1a90ba18e8 | -10.92323 | -53.97173 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68011f4e-0ab6-3bfd-8307-85849bc65718 | -12.75598 | -46.21899 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9673251-20f9-38b1-969a-0b4a6a653cb5 | -13.26285 | -51.72727 | 2026-09-20 04:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 852cb8a5-817b-3fa7-861d-7f5b98383e74 | -11.12222 | -54.01936 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23271037-f991-338d-b0c9-ff54a3ad2e03 | -14.68679 | -46.68447 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54d7e176-9106-3259-a5ed-c69d13df09cd | -12.52926 | -50.03994 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bed30a17-6832-3415-9724-b17e3120bf52 | -11.38725 | -51.43275 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15d6bb1a-fd22-3185-b5b7-3ad3a4b14d80 | -15.67744 | -52.72619 | 2026-09-20 04:21:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e46f23b-bb5b-3421-9f39-604099536c55 | -12.0456 | -45.80096 | 2026-09-20 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21bbe692-a91d-3da0-a9e8-c06d06ae3f3e | -16.59382 | -45.33809 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e132920-32a9-300e-b999-c20687c0a042 | -13.0296 | -46.90963 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e98d83c0-c27d-3d4e-8c90-a2694d0c6590 | -16.09526 | -49.6413 | 2026-09-20 04:21:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5deaa1d-c026-3c42-9ad1-209f377a79df | -11.85379 | -47.65924 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5783d1a8-130b-3ce6-a5db-463351d88288 | -11.12637 | -54.03024 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5f9a34c2-ba81-3e70-b86b-01548673927e | -18.37693 | -49.40266 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0b72cbf4-8bce-32df-8084-46cbb25dd1e1 | -10.87863 | -54.07438 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39c9f0db-a10c-3a8e-b6e4-9be1d555d30b | -15.46621 | -48.41418 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 782c19b0-615c-37e7-b0c5-5fdbff757654 | -15.89752 | -48.06911 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 536e73f9-b379-36b7-9d5b-c8740b2c033c | -12.76375 | -46.12866 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 784a3f2b-4f2d-3e15-8110-ff4f0b7192ce | -11.83752 | -47.62778 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0d24472-c2c3-3cf6-abd8-6b4e81845866 | -11.39077 | -51.38513 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bebfb1c6-d2e6-309c-848d-18e056996d5d | -15.0564 | -48.58249 | 2026-09-20 04:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48082d6b-761a-39d5-ae66-fe4b6e8f8414 | -15.3369 | -47.03565 | 2026-09-20 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 382a38cf-40cb-3d86-bc64-0656a95e2cb8 | -16.63487 | -49.27836 | 2026-09-20 04:21:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0498a404-8c6b-3865-a1a0-d6c3151c3c97 | -12.65646 | -49.48315 | 2026-09-20 04:21:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df15f172-a4c1-3e00-872b-5e8cdfef23c4 | -11.03718 | -54.16417 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 511d3e0b-827d-34dd-98a9-7a7772e173c4 | -11.69422 | -47.73246 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9cc13df-9316-302e-89e1-155318f63620 | -12.0153 | -51.47673 | 2026-09-20 04:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d07ab4a-d857-3706-babc-5d831e48d21c | -11.37016 | -51.41003 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aad81d8-0b42-395f-8185-7c5a08cdafdd | -11.37472 | -51.41414 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 672fe072-80d1-3ad0-8665-411c54dfb5a3 | -13.22552 | -46.94073 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b818921c-acc1-39ac-bb61-0156038ccb48 | -17.03616 | -47.28336 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea6543e4-b18a-3f76-8b43-ee6530c226a0 | -11.2191 | -54.07441 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1628085e-8ca8-3e80-8f88-0b71fcf75b70 | -15.17074 | -48.1576 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 581732d5-efe5-3085-96b7-06b58f1afd75 | -10.87073 | -56.22625 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebe413ad-3bea-3944-a60c-f720eeb7d27f | -16.73676 | -49.36108 | 2026-09-20 04:21:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1cd1432-16d0-3aca-a0ca-65cd148bca80 | -10.87428 | -56.23233 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20eb393d-f99f-344f-88ca-05bf1c9915bc | -11.21031 | -54.08487 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e87cb37-0521-321e-a30e-e134cd995b72 | -12.74651 | -46.18668 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e24478f9-bbdb-397f-8b9d-9783ee7cd497 | -12.9936 | -46.91661 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d374b1a-fc96-34f2-8853-982a52316460 | -16.59443 | -45.33434 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 365fa256-1fc1-3513-8d11-862dba237d68 | -11.83538 | -46.85463 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89743af9-8c66-35de-8964-894a98acdccd | -12.15274 | -47.03582 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 066c1db7-651a-34a6-ae86-4fd940304adf | -11.85894 | -47.67636 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0aa17550-fbcb-3f52-ae7f-928cfaa8d478 | -15.47025 | -48.43697 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 610e5580-05f5-3764-84f0-08d10f356f80 | -11.38622 | -51.38106 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49484ffa-0d61-3478-a09d-d299c8423e5d | -10.92697 | -53.95306 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59d28e89-a0af-3ddd-bc2e-eac369096962 | -15.47515 | -48.43243 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa99dcb7-ba30-34c1-a6a6-fcc7fe49d0ac | -12.34187 | -50.69558 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6402cfe0-d703-394f-a1a5-721ee4d2c6fc | -13.39004 | -49.44627 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c1ccd70-01f6-3723-aac6-38c8056d43d9 | -11.08886 | -54.0313 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ae759041-db0d-3afc-a043-3bd9feb8888c | -14.05225 | -52.08694 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3aa4687-ccfe-31a0-a4b6-612f4d24763e | -10.87954 | -54.06973 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22a94295-dbdc-340c-b437-044d720ec85b | -13.38938 | -49.44767 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929b0012-4d54-3821-9caa-bdc094dd2bd9 | -14.18487 | -47.87675 | 2026-09-20 04:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae475d6e-41b5-34ce-baa9-795c8efee593 | -13.6121 | -46.96788 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4d5f431-d33e-30fd-aa25-9253f6c87742 | -11.21729 | -54.08373 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ef33fb4-e8cf-33f2-80f2-2fdc88bd07f1 | -11.38928 | -51.42695 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cebd60e6-8083-3275-a88b-4c56c6392d5f | -11.39253 | -51.38263 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe80a751-6f69-3af6-831e-d9987a532b7a | -13.58457 | -46.94371 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae2c10d1-9da7-32b5-9a2c-40b03730f19c | -17.01849 | -47.14723 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4786bdc1-923c-39e6-a18c-78b9330453e1 | -13.61454 | -46.97044 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71660f66-7c55-3393-be3d-08fadb5d24e5 | -13.3857 | -49.44537 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bdee095-4a79-38d8-8ffd-24dd6dbc5819 | -11.20417 | -54.08378 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e2db0db-1d44-3b52-ba06-3c2217833b33 | -15.86329 | -49.91078 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6794d2ab-047c-3ca0-8a49-2272c6635007 | -12.53476 | -50.03602 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2be5fa-5071-3ac4-baab-8ecb45f7f741 | -15.67761 | -52.72604 | 2026-09-20 04:21:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b375195-c8c5-34d5-8bc0-05172f96d4d7 | -11.12212 | -54.02323 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| efd2c40b-c338-339b-a046-bdb010627dbc | -12.2902 | -47.11746 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ae51560d-00c7-3521-a6f9-61c3efed91bd | -16.33563 | -49.51636 | 2026-09-20 04:21:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b0c4728-c2d7-3159-b5bb-7113b10928e2 | -16.49681 | -49.21196 | 2026-09-20 04:21:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efef67ea-f317-369d-b951-14178c95ce6f | -11.20512 | -54.07911 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b911df2-99f4-3a24-a2c7-b0911474cfa6 | -13.89132 | -48.58732 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c3d68598-4083-3597-b531-8733256b6f4a | -10.87589 | -54.08845 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36edb560-ab42-3ce2-b124-c8d9b2653a82 | -19.32366 | -46.36818 | 2026-09-20 04:21:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb417e1-8b37-349c-9e26-42deb25cb783 | -16.57553 | -51.62484 | 2026-09-20 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e169d8-ce97-3e6e-8175-0c06fa8681f0 | -12.75232 | -46.19648 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7c508e1-a74e-3037-8bca-293c8e03820c | -13.58316 | -46.9518 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf723035-fc69-331b-b73a-d880cd926932 | -11.05169 | -54.17856 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e608fd4-f85f-3073-bc42-0a4ea4486cfd | -11.10008 | -54.03476 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2d38ae70-e950-3b64-bd71-0be77aa86b07 | -11.87315 | -49.00777 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00501151-4243-31db-805e-18f2c9805ca1 | -18.37887 | -49.39902 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b34723a-5378-3eb5-80fb-99127d2ffa9e | -14.91812 | -49.91744 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbf25f11-3bcd-3943-8067-88bf29d5cdcd | -15.17375 | -48.1633 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c299fbbe-9040-3918-b22e-0f497ea7e50e | -11.3959 | -51.38615 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9818a893-abf3-3fc3-97a7-9827480b4dfd | -11.10105 | -54.03381 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 511453d5-301c-31d6-942a-0292527b6ea6 | -14.61331 | -48.1048 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac8168a3-d601-3059-8b84-936397bba7d7 | -14.91463 | -49.91467 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43b32192-d108-31ee-b8a4-4b74a59337e4 | -12.75374 | -46.18802 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a13c57a9-5cda-3408-8fca-c72bb2784025 | -12.69372 | -50.75954 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91def9d6-ed88-389a-adc4-c2c4f73d39ac | -15.47124 | -48.43151 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a27f68ea-e540-387b-ba5a-65dd06e0dc4f | -13.02512 | -46.91317 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README46.md)
