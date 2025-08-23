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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7774d5a-2559-3bb9-aa90-60052ae7e84a | -20.39805 | -45.44725 | 2025-08-23 03:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| de9cfe5f-76e2-3302-9773-1927f24a26fe | -22.9195 | -43.50338 | 2025-08-23 03:42:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e08f6821-5bbf-31f4-aa6d-17c7ebcfa212 | -20.09992 | -47.77724 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b16092cd-743b-3941-b04d-198f3dddbfc1 | -19.93899 | -44.94215 | 2025-08-23 03:42:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f034a66c-7c50-3f91-bc93-a7cd1dff698e | -22.54206 | -43.59004 | 2025-08-23 03:42:00 | NPP-375D | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ea051943-7720-3069-bbac-ab10c7a1ebb8 | -22.1757 | -43.28194 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cad497c3-1df5-3d68-ae0c-91c7f8e6c762 | -22.89944 | -46.39501 | 2025-08-23 03:42:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2baeaa3a-5c5b-33ab-8b74-30deef9f5d00 | -22.49221 | -43.82098 | 2025-08-23 03:42:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4327dc15-b8f0-3cd1-a525-df04486039d7 | -20.27234 | -46.6812 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c238b2e-2d8d-3c30-9ddb-633336db7712 | -20.35325 | -46.52468 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03819c0f-be50-3894-a665-0843889c3a82 | -22.17069 | -43.28517 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 65d2a412-50f0-3b98-8bd2-ac595981f614 | -21.55068 | -43.49272 | 2025-08-23 03:42:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7b0528f0-7907-352e-87bf-48c250610c9f | -20.46017 | -45.95493 | 2025-08-23 03:42:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84897bc9-583c-3d83-b2b6-2a8de70a66af | -22.53267 | -43.72915 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 678e6dd6-2b2e-3703-9f62-ca591d055f50 | -20.09608 | -47.76732 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670348e5-0103-33e7-81e7-0c7f141fd16a | -18.86615 | -47.39275 | 2025-08-23 03:42:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ba22c9a-318d-3b7f-8126-61c1e55ac5ec | -22.22263 | -48.36526 | 2025-08-23 03:42:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b36054de-27c7-3b5b-a626-34d4984df9cc | -22.17779 | -43.28918 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a8ed4c9d-41b2-37de-b26b-90069e0eb683 | -20.86935 | -42.54433 | 2025-08-23 03:42:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 83aa9b16-cfb8-36ae-b316-e457be869d70 | -22.63105 | -47.43171 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02e45628-e940-30a2-91af-0132f9f1f6ee | -20.16219 | -45.33777 | 2025-08-23 03:42:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| df81b0b2-4251-31f3-a381-66daeb75536e | -20.44746 | -42.12608 | 2025-08-23 03:42:00 | NPP-375D | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 34f3067c-c497-3993-bd77-2d2ecc09b3aa | -20.87351 | -42.54493 | 2025-08-23 03:42:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0d7f8545-76e0-3214-ab69-7d9c3122f5d3 | -23.49937 | -45.9993 | 2025-08-23 03:42:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a79ba65-9115-3296-bc18-d0258d5e1688 | -22.30496 | -43.17446 | 2025-08-23 03:42:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 071eb381-837e-3dd1-a132-addab1321a1b | -20.27301 | -46.67807 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8926ace-05db-322c-9cbc-8095808485bb | -22.48072 | -44.28419 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3190f83f-0ec9-3237-9be8-52d2d07a0a33 | -19.38625 | -41.44699 | 2025-08-23 03:42:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| fdc8f7fa-43b1-3f0a-9a6a-895a4ee4cd3c | -20.28199 | -46.64485 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08ee6bac-1411-3e1f-931a-88001e76c7b5 | -22.31001 | -43.17077 | 2025-08-23 03:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c5d9caf-7271-35a5-b04d-75a509c8807e | -22.62897 | -47.43649 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 651038f6-a55c-3a8d-8da8-e53b1a504a77 | -19.38723 | -41.44158 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 02d8d214-2740-3331-82d4-95fa4a82456b | -22.42267 | -44.50064 | 2025-08-23 03:42:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3942b618-92b4-38ba-becb-f6af063a37ed | -20.36085 | -46.54109 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b8b3f92-9b05-3a33-adff-66a0b823157b | -22.53393 | -43.72833 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1dd74e66-9480-3e57-8cac-fb3b8104768a | -19.95972 | -47.51389 | 2025-08-23 03:42:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29a0445c-eaf7-32cc-9282-d13cdbf3675b | -20.09511 | -47.77164 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b4c9ea9f-a92f-3f0e-a7ce-acbcc3c3209e | -20.16717 | -45.33879 | 2025-08-23 03:42:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 356b61af-a326-3949-a5d6-cd75cb981c0c | -20.28108 | -46.64893 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84632eaf-4924-3429-8324-282deb2768a7 | -19.38134 | -41.44195 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 7488f0cc-f075-3324-aced-ec33d21016c0 | -20.08727 | -46.12048 | 2025-08-23 03:42:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15cf9fc0-d087-3fc1-8c02-ced3e861da5a | -20.08789 | -46.1227 | 2025-08-23 03:42:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca5490cb-e0a8-38a3-a665-2353e72eb163 | -20.01179 | -46.43161 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7907d51e-6590-39e3-94ce-d3dbe3bdee1a | -20.09321 | -47.78012 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b13a2c90-7210-3593-822c-4f16e99dafe6 | -22.52922 | -43.72392 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7b03541-d024-3347-a471-e63ac1ad9282 | -20.22229 | -43.80249 | 2025-08-23 03:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 471f8f51-4b0e-3363-9bbc-f93b587bb3a3 | -18.86713 | -47.38832 | 2025-08-23 03:42:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78a479ac-cd00-39af-9eed-cf6ff3789335 | -20.28725 | -46.63782 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39846532-95d6-3ce9-97c2-0538c1ccbcc4 | -22.64365 | -46.66808 | 2025-08-23 03:42:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 500da7ae-7249-35a1-941d-35fdda149755 | -20.08875 | -47.74601 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9c3c60-d370-3aaf-b4cb-d41609695187 | -20.28642 | -46.64171 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67824f22-2194-370c-9715-56f891d708a2 | -22.74692 | -46.54769 | 2025-08-23 03:42:00 | NPP-375D | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28e4bde3-4233-31e6-ab8c-814251317f23 | -19.38329 | -41.44072 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 1c394b5c-5827-3901-ac18-8c90b934755b | -22.47275 | -44.27772 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f70f010-1ad8-35e0-beb6-7ebc44ff6b6a | -22.47465 | -44.26834 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d6a21c26-9164-308e-a7f0-12813c993a59 | -19.78343 | -45.66116 | 2025-08-23 03:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 132ffb88-0327-3566-a7a2-dfe7fbf5f7dc | -20.26616 | -46.68367 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1883018a-57ec-34ef-b0f3-f589450c0aff | -22.17151 | -43.28094 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 05da4c30-bbbb-3d72-82dd-91c40353365c | -20.09417 | -47.77583 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f4daa594-7753-36b8-9eed-1b1b91a84ca4 | -19.67939 | -43.8701 | 2025-08-23 03:42:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2104fe0-d709-37d7-8317-160538ea2492 | -22.16893 | -43.27165 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc38b73a-e2cc-3853-a6f0-e396294a7e18 | -20.27836 | -46.6531 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63604c6e-0a78-3c10-8869-8a4b85b6bc68 | -22.76967 | -43.68397 | 2025-08-23 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93faa224-3c08-34b3-b374-12c5456440c8 | -24.90885 | -49.27491 | 2025-08-23 03:45:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 391f177b-634d-3251-b273-f5add86db810 | -23.67653 | -51.82079 | 2025-08-23 03:45:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 77b359a7-20a3-3511-b1d0-170459947550 | -25.17081 | -50.08117 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba520260-43c0-3380-82e8-cf71bd6f20c2 | -25.57198 | -51.0616 | 2025-08-23 03:45:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa1ea819-504c-3805-a43a-d8a30923af41 | -23.68493 | -51.81597 | 2025-08-23 03:45:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| c2d4e5ed-cfcf-3800-ae7a-cc0513c8ab28 | -25.16499 | -50.07914 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c822b8e2-67cc-3c8d-8164-e7f2c4dcc6ba | -23.74413 | -51.1002 | 2025-08-23 03:45:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bf85b37a-23cc-36c7-b0bd-503c625b8ccc | -25.16616 | -50.07425 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bf96ef87-af10-3fb5-9dd9-23f3cac62cbb | -25.17237 | -50.08362 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 26baa037-ab14-3961-9ced-74cf29d1ecdf | -24.90803 | -49.27625 | 2025-08-23 03:45:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b4368ef2-7763-314d-a70e-9f14855a217a | -25.17197 | -50.07632 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 96aa9e5e-b55f-39ef-b565-908ff6b5ac8b | -24.9077 | -49.27965 | 2025-08-23 03:45:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 59d24ded-9df3-3275-a3bc-7dd745b29882 | -23.67826 | -51.81409 | 2025-08-23 03:45:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| e3096751-977d-37fb-ba6a-67979671017d | -25.16776 | -50.07671 | 2025-08-23 03:45:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 43bd82c8-5968-38c8-810e-ddfdf9878d6d | -25.5659 | -51.05943 | 2025-08-23 03:45:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| adc23db2-b1c6-3af1-a7b7-308da347acd0 | -23.68315 | -51.82292 | 2025-08-23 03:45:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| f6dcb4ed-2853-34e2-a850-6a6a627e3005 | -9.9493 | -60.1947 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 268.1 |
| ea81b4ec-5b87-3d67-aed8-7f3fe5646cfe | -5.7429 | -57.6009 | 2025-08-23 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b127b983-1f3b-39e9-ad95-bb4c22156998 | -9.9681 | -60.1743 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 4d54b0a3-4a4c-3a6a-b88b-d9fc49252d17 | -9.5177 | -60.5653 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 63ebd365-8152-34a2-be7f-5c382253f95a | -14.2744 | -58.5266 | 2025-08-23 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e5e3abe7-7a68-3ef5-88dd-9b64da9ac378 | -5.7615 | -57.5807 | 2025-08-23 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f781e81c-e3dc-35dd-a7f2-50c0de725dc6 | -6.37 | -45.5356 | 2025-08-23 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 005c3386-0280-30e9-98f4-6e8737d6cefb | -6.3698 | -45.5582 | 2025-08-23 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| a5003013-cf57-385c-8775-620876d1f04c | -6.3887 | -45.5342 | 2025-08-23 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 538277e3-610f-3e1c-9f18-d09d874a9ff8 | -9.5179 | -60.5461 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 91c24c54-9abc-3174-a98b-1738d67d58ef | -6.6044 | -44.5624 | 2025-08-23 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4e5f6b1c-cfca-3d1e-8631-53cf526b85bb | -4.3482 | -46.4695 | 2025-08-23 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| bcf14bd2-0448-3a3c-a26f-949d4c6237f6 | -9.9495 | -60.1754 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| f6325af4-75fb-3293-a5c9-225dfd63ef42 | -8.5943 | -62.6315 | 2025-08-23 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 90f5242f-6d9a-3b48-83f8-9c87d691925c | -5.7614 | -57.6002 | 2025-08-23 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 31061013-9d86-3443-b09f-4009e409204f | -9.1897 | -59.6171 | 2025-08-23 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 131b4dad-d6dd-3e5c-9e99-bf8c4cf53e87 | -8.613 | -62.6118 | 2025-08-23 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5a85d371-fa8b-314d-a4cb-ea54f3a17f0a | -5.7431 | -57.5814 | 2025-08-23 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fa73a1c0-af2b-3477-819d-47d8e23dad47 | -6.3885 | -45.5567 | 2025-08-23 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| a33aaa85-3c21-39bf-bbc0-2e0c0965d12c | -8.5944 | -62.6126 | 2025-08-23 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 129cfcc4-bc3a-38c9-a88f-6004b48b44c8 | -9.518 | -60.5268 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |


[Clique aqui para ver as próximas entradas](README21.md)
