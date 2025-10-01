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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7172ad6-6794-32ed-81f2-f8be0403d8b7 | -11.83803 | -44.96282 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15e3e977-9d33-3792-a481-8bcef444f5c9 | -14.78909 | -45.80468 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0253c841-c065-311d-8d8e-8b6760b1f906 | -12.37577 | -50.20369 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ac62d8b-ce99-37f0-b0c7-c730e5ac162f | -14.71057 | -48.22142 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76fb9e08-ad23-3962-b7ca-52860aee8923 | -15.44064 | -43.64309 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 403ff235-0f2f-3fc0-9077-c26945a37206 | -12.15377 | -51.42453 | 2025-10-01 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3ce474b-918e-3a8e-b4e7-7efd9b9cbd09 | -10.95902 | -48.83028 | 2025-10-01 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83396928-411a-3857-880c-916e48601d63 | -12.69375 | -48.55737 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1223d5ef-be97-325f-aa79-2e83df1c21a6 | -11.75577 | -46.83966 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62ff5aef-9079-3e87-b515-a0605ba28b17 | -13.7186 | -48.65226 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9345f599-2451-39a6-a125-363c89f8b430 | -12.82892 | -47.00584 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e3d2a9e-1560-3568-ba7d-5882125c48bc | -14.89432 | -48.13469 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 142e33a3-6212-3fc7-b793-589b090890e3 | -11.84201 | -45.00353 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7656f48-183b-32f7-9498-e87fa04fdbc4 | -9.57377 | -50.9478 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3d18ab-08a4-3626-a9ed-1eccece0942f | -11.46584 | -44.97343 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1925b38-231e-35a2-b576-e30fc65f7520 | -12.39919 | -44.75899 | 2025-10-01 04:21:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f869ab0-51be-3ea8-93ce-2739a410bf6f | -15.31907 | -46.40355 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2888b613-7d74-3db2-9aab-3a47e24fa75f | -15.21415 | -48.17829 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 127f756f-b2c3-3d8f-9814-fedea03738f9 | -11.05998 | -47.82026 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b6d42e4-a713-3cdc-9309-728e6b895592 | -11.40311 | -44.89456 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ce0fd0-83d8-3c4a-aa6c-23c076d5e2a1 | -14.06197 | -44.37376 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11d5a55e-7906-3d07-a0d2-0aca2f9f0ca7 | -15.1046 | -44.95143 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5f77f84-828b-3884-b158-bbf862fb7617 | -10.65412 | -48.52517 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6836a87-6dd3-3b20-a729-8926228d3925 | -11.4659 | -44.99536 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df6ae584-d640-36ad-8f2d-911f2a11299d | -12.89054 | -45.26017 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef0a1501-ff0e-32cd-9fa7-2d797f2bb9a6 | -9.4343 | -54.70946 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bc2c398-c31f-30a2-ae5d-b71c4b6ca281 | -10.90319 | -44.26709 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe66c8d0-386f-3546-bd84-d57a64595240 | -14.9633 | -46.87685 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae997032-4f0f-3246-9997-1656b04a708d | -10.08457 | -50.57523 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d61f6a9-9a91-3c81-be41-dea9b7e571bc | -14.73186 | -45.21822 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35df37ee-3b06-35b5-b546-6ff1c1639718 | -14.39307 | -46.21212 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31a11d1e-2597-38f8-88e6-3f9a85a6c386 | -16.8679 | -44.2724 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d898be1-be32-37fb-a292-e1e4cfe8eccc | -15.17996 | -46.40276 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe5864d8-d53d-3f64-84a2-01e95343d8a4 | -13.80108 | -48.02671 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 232849da-b6a1-3639-acd2-dc055b9cffa6 | -9.57314 | -50.95148 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2db3d84-f3ed-347c-81cf-2b719974d38e | -16.19739 | -49.99105 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b7837058-e7f3-3edd-afb3-3004c4d71e75 | -10.73403 | -45.37656 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cb34c0e-0e10-31a8-a9d6-cc23e2b6ae9a | -10.74393 | -45.37812 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 11e31c31-0198-37ce-a8f1-8d9718f6caf8 | -12.85898 | -46.94506 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33f02496-369c-3f75-9570-5c7589dc162d | -15.26917 | -56.77543 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d21168f3-386d-3b93-b1b7-32ccd66dbe5b | -16.05298 | -51.0104 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 332144a7-cfee-3ff9-84b8-49c9ae128296 | -9.58616 | -54.58883 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f50f2a2-4cb9-3a8f-886b-5e5af6b9f225 | -16.40268 | -47.04761 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ee7240-3527-3b7e-90a1-cd72488d1928 | -14.50645 | -48.48308 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bef06288-c042-34cf-a961-05564e694aa1 | -15.24009 | -49.7207 | 2025-10-01 04:21:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58755c62-28c5-324e-8799-c5097a96708e | -13.22908 | -48.44382 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a1c4e31-d5ee-39d2-bcbe-b6684f21469f | -11.5693 | -50.1866 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3abaf9c8-61d0-3bc4-9dda-5a104d75c58e | -10.83856 | -45.4039 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59d13822-9d2e-37b7-8974-50f3437bbd25 | -12.8479 | -46.95063 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9916756a-4d48-365f-ba81-9e1d8aec04bc | -14.05402 | -45.02227 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0142120c-acb9-3bd3-bffd-4eafa2f6abd4 | -14.63141 | -46.97452 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 727af2c8-ecb3-3592-b53f-4389202f243a | -11.94461 | -47.06428 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89f23070-d9b2-3e98-b027-3271735d3aec | -11.63765 | -47.48909 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e808d891-8d71-3b7c-ab07-66f1658d72fa | -14.98945 | -46.96861 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b609f19-e0bb-374f-917f-8b91f30accdb | -12.76173 | -46.91468 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc63770f-b2f3-3a27-976a-21915ae4423a | -12.83271 | -47.02475 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b79ac5-c7fc-3fa7-aa69-8bcef890b2bf | -12.96966 | -46.42022 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be06614d-a533-3786-a038-0567dfe2642a | -14.96497 | -46.86622 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 244b22f5-6253-3904-9023-8d3c851e333c | -9.51577 | -54.73597 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c6472fe-a8ae-35fa-8fe6-b69f2bed2d84 | -13.55858 | -47.27676 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd678842-114f-3cf5-805e-eb8f7883fcde | -10.91352 | -44.33577 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f4971c8-cdc5-3218-9ef0-1d0d6832265b | -15.27063 | -46.41013 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbcb2841-bcd2-38ba-bfbf-8b95522f5493 | -11.81587 | -44.97393 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4bda361a-aec4-32b9-b10e-5b9ab3adf862 | -13.64599 | -48.0233 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23a76d87-e57c-37d4-857b-00bbd7f43dae | -13.63468 | -47.64797 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae533e33-29de-32ea-8060-c7d0aa9fd795 | -13.37065 | -47.30095 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a71363c1-24bc-307e-9cd2-1bd16df987b3 | -13.30777 | -47.2058 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfcb95a1-546b-3ff6-836c-3f5e9ce3ef93 | -11.46946 | -45.08312 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5fa6630-5014-3b1f-9f28-7fafe3f407d3 | -14.66662 | -48.13055 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb374e51-743d-362b-b8e5-4e6b00efebd4 | -14.14361 | -49.19743 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d22717f5-b114-37a9-953e-823bdd3243b2 | -11.54683 | -45.06589 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9dbd7e7-29a0-30a5-aece-b9e5610545f9 | -16.25323 | -50.93852 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 53a2ffee-d0dc-394d-b7d7-80bca3a310e9 | -12.76229 | -46.91114 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0540823b-0344-3f05-b44d-1c526bd028f5 | -13.78865 | -47.9859 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 184de2d7-b349-3f5c-b213-7c79d4819719 | -12.78138 | -46.87772 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ea69a14-9f29-3dca-9d9a-ff12bc67b3e6 | -12.36824 | -50.20237 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f6e3020-88e4-3d44-bc88-c48f67a01aca | -13.29878 | -47.58126 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 038df18d-2177-3051-bb52-321264157e9e | -11.1241 | -49.78446 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa22b184-6eeb-3f80-a404-e551338e92a5 | -11.12489 | -49.77989 | 2025-10-01 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3a40a12-1da7-336f-a96b-9bfb9c8ebfe9 | -11.46197 | -44.97649 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ddb29fd-3f45-3c48-8581-893ff3263257 | -11.68718 | -44.29649 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aca1ff06-06d5-3a15-89ac-d6737f9ed6e1 | -11.47779 | -45.0953 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d24fbfa9-05cf-31d4-b6e6-45c7a4ad2ba6 | -12.86269 | -46.98595 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf54a41-5b2a-3222-a461-c2aa6d275de1 | -11.81642 | -44.97035 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f0346b5-5d40-306a-ac4c-5a28baf83280 | -13.36326 | -47.28519 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea9101d0-f583-3b48-b315-e1f21c50ee61 | -14.10396 | -49.75232 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e81c4f8-9664-3518-87bb-b36c9f26e541 | -14.70919 | -48.18734 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d45e7f28-cf38-347c-ba7a-69b2c8bbcf06 | -13.37611 | -47.30936 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e700aeba-19cf-3350-a0e0-14283f10034e | -14.52847 | -48.37089 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 246a9764-9518-3f12-b948-224e01138609 | -16.57061 | -45.10691 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90681e71-b2dc-34b6-a020-67338486a73a | -14.61117 | -48.20483 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb5730e8-debc-38de-a938-45b507a3a471 | -13.08044 | -47.07319 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ca9cb4f-0572-3ec2-a8e9-0f1f91a7f0af | -12.93835 | -47.1958 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8cedcc2f-5aba-3a15-85ce-288aa66964e1 | -14.39528 | -46.21974 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17afde1a-be29-34b7-aeb5-8326fa479e55 | -11.85085 | -44.99035 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 4d92a0ee-6d5a-37bc-962b-5fc8b19caebb | -11.96567 | -46.59099 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70ef7caf-507b-3693-996f-8dca4de3112e | -13.38024 | -48.08172 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8d82cda-06da-3033-9d6e-7d1c2c7b299b | -11.81696 | -44.96678 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42864747-99b7-3d8a-b018-69ae9d13b6d4 | -14.7232 | -48.14368 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1275497d-1ee6-310f-98f8-3b70617ae14d | -13.63262 | -47.64418 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README51.md)
