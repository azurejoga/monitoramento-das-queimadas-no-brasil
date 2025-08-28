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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5de6b3ab-5e97-349b-8160-95ece0482068 | -12.78057 | -48.17001 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da4db425-9e39-3823-b088-18d8029249d1 | -13.385 | -46.88588 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 975f3b1a-b767-3755-864c-5842331f1380 | -13.63231 | -48.21544 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e100d2f8-ab16-37c4-ab81-52c54fcd21d2 | -11.33136 | -43.53204 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fdf7611b-5863-3c44-af34-87fa5f0a53a0 | -10.81205 | -46.3681 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9467158-a69a-3047-ad1e-d12dbd920c5e | -13.17842 | -45.27958 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6d9a9d4-185d-3d63-a91a-a44e16b79751 | -13.54381 | -46.89225 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7042b53a-fb05-3ae2-94ac-1c3d4b41c9e8 | -12.92769 | -46.33383 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc8648f-6557-37ff-9567-3906164049b8 | -13.17724 | -45.28568 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0bf820a-e86e-38aa-a0ea-32daf1cf2d34 | -12.80815 | -48.16039 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a504e53b-5ab1-3cfe-b40d-3e419d4724c5 | -12.67461 | -48.16997 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aaba863-47a8-30b6-895c-9aea2cefa9f4 | -11.80577 | -46.78955 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f41ac8ea-c34a-395a-ac78-75c5b1e39c20 | -12.71733 | -48.17445 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5f1d2f37-ad1e-3384-908f-f8a8213a45d0 | -13.50946 | -46.86002 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8948f2-c01c-3ee2-b657-54972697b989 | -11.32576 | -43.53611 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0760bb62-ceb5-3b0c-a590-85ae4dbef1af | -12.79777 | -48.14872 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fca8c138-5ef3-31c0-883d-fa799d15ff7c | -21.14947 | -42.4494 | 2025-08-28 03:47:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7eb45740-f2a7-3ff2-a49c-b665b70f8279 | -12.79163 | -48.14749 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec829194-e17a-30ba-8de3-12256490d05b | -13.66853 | -46.8817 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25d2d9e9-87ae-30b2-8322-ba8e674a146c | -10.37226 | -45.17064 | 2025-08-28 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a4093ff-be58-33c5-a43f-c540803ffb07 | -13.14192 | -40.66671 | 2025-08-28 03:47:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b57bc62-78fa-3a36-a0ae-6525ddd68691 | -13.52631 | -46.92158 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51787f48-4f89-3304-b41d-49fab846284c | -13.51724 | -46.87933 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77f1c701-aa23-3502-a0e4-597419047a91 | -12.79059 | -48.18348 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 481bbb64-0272-3fe1-b303-6dee5cb8b2c3 | -13.17275 | -45.28161 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 927833b2-0c11-34e6-98ff-ab6f41c07c97 | -11.55011 | -46.35743 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b5f76fb-07e9-3a27-a94a-2b22850963ac | -12.69271 | -48.16946 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 366afe35-6683-36cf-ab45-4c1d50568b82 | -12.69174 | -48.17422 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a692f7cb-b6e3-3e43-a37d-0b6dcc52e531 | -12.8961 | -48.10417 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cb710bf-13e1-32b0-a39e-e7de4c8e1454 | -12.95886 | -44.57491 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c1505a9c-fe5c-37f2-8629-62650067ce72 | -13.17783 | -45.28263 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13b737af-1137-32d9-8e12-ba3f120e3381 | -22.67962 | -46.84158 | 2025-08-28 03:47:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d24df3be-1087-3877-aeab-bb62ebf33249 | -12.69111 | -44.40839 | 2025-08-28 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 396d31ab-8a64-393b-bc0c-8b8614a0d566 | -13.08586 | -46.33777 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d51895b-1adc-3999-9896-e81e0a277a9f | -21.60699 | -49.70202 | 2025-08-28 03:47:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ae3d2cef-dcee-379d-8f85-9d4f3a1f7dd2 | -12.44498 | -48.71422 | 2025-08-28 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4b7f604-a134-3015-b827-86d5dda97d05 | -12.92839 | -46.32866 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c69d59c-b4a3-31b5-bc51-3d0a355600df | -13.97375 | -46.35443 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fab9b40-a7b8-3971-8290-0aa6a8e6f35e | -11.33512 | -43.5379 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0340fff2-a3a4-3861-80aa-f8373b399b74 | -22.67929 | -44.42414 | 2025-08-28 03:47:00 | NPP-375D | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c170c6f4-b245-3455-89ce-ba76d8585f13 | -12.06435 | -46.62926 | 2025-08-28 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37023925-fcfc-38ef-a303-520bd8c83f93 | -13.51884 | -46.9297 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bbdfd04-7394-366c-9e19-5513e0fb942e | -15.08322 | -48.51516 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dc658e4-0a2b-3880-9746-fd59537c5e34 | -12.79355 | -48.16916 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37579478-79ba-34e7-9d68-8b3eb4253402 | -13.43906 | -46.96706 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b58a86d-d45b-3860-91cf-f83938744721 | -16.80869 | -41.22982 | 2025-08-28 03:47:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6368950c-94e4-3fd0-b71b-5c4d478756f8 | -12.40994 | -47.78932 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f4e59b1-9e3d-31cc-ae6f-c179346a04f6 | -12.43047 | -45.97044 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c39fa6f-e5a6-3060-8c38-9913ff9aae7a | -20.08888 | -43.7562 | 2025-08-28 03:47:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bc0c251e-2d2c-3198-b305-d571dfaa50e1 | -11.57281 | -46.39056 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2dd4235-e6f1-33bd-8aa4-894a7bc8e4f3 | -11.34357 | -43.54462 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9b53aa3b-7f09-3667-9db9-5e491e69ce9a | -10.71554 | -47.02403 | 2025-08-28 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a900dc30-99f6-37f6-b73a-033f46f3070e | -11.3276 | -43.52619 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b45e6ea-479c-35a8-a92d-0e63ddc487aa | -13.51422 | -46.86528 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 563352c9-8aa5-312b-8a9a-969c56860fe9 | -10.52882 | -46.6899 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41e8343d-069a-350c-8548-2fc76671038c | -21.14531 | -46.97149 | 2025-08-28 03:47:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e800bb4-03dc-350e-be35-74cdfbfdc577 | -11.31925 | -43.54514 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 070ce6cd-90d7-3623-b295-fa28cb59d0e0 | -13.41562 | -46.84962 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d27c488a-6f43-30aa-a56e-c273bc93ed51 | -22.67523 | -44.4233 | 2025-08-28 03:47:00 | NPP-375D | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8267e6e8-3a70-3af6-b802-4cb3d99d8808 | -11.34267 | -43.54957 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 459fa251-5b0d-3cc4-89e2-ad02c549d62a | -10.53646 | -46.71305 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df18a676-f902-3db9-a3e5-605f41b40469 | -20.30477 | -46.03176 | 2025-08-28 03:47:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c435ecee-9f16-3f69-82dc-620b3bbd58eb | -11.55932 | -46.34011 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 194f25d5-2eaf-36c2-8b58-db244aa2d881 | -11.24476 | -44.97741 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2795cb26-00f0-3904-b2ec-eb929fe32db4 | -11.33695 | -43.52795 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0af5ce7-024d-3599-9fa7-4a7d5ff128cd | -12.67302 | -48.17166 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1f6a82d-a5fb-35c8-9f84-59915e5d1612 | -13.39588 | -46.86082 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219c2147-de9f-3d95-b866-fe7d8bbd9ea1 | -13.43148 | -46.98478 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b010d5a8-c8f1-3461-b2b8-2968f99c253f | -12.82409 | -48.14505 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398139bf-c664-31f6-80de-373f5f73ff40 | -11.24464 | -45.00346 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e74e2d8e-35f5-38c8-8387-0baabb720a72 | -13.43524 | -46.98656 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dde1bb94-a712-3be5-9bea-21b66d97fea5 | -13.83366 | -46.68762 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7903410d-ce8d-380c-b373-64d72ed56b83 | -12.06357 | -46.63322 | 2025-08-28 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e701d87a-4eb3-3d6a-8b99-df3a0d7c6aab | -13.42679 | -46.97899 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76615032-4470-3aaa-9076-38c06dbd49ce | -15.08444 | -48.51215 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bede4ca9-74bb-3539-bc71-70f666d6e4d4 | -13.61989 | -48.24557 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fa456f5-2b18-370a-829e-4b26457de106 | -12.6799 | -48.17557 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f265769-a5d9-3c47-bb9d-edd965f7c290 | -12.96265 | -44.58152 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8769cb7f-660a-306a-b987-a0e84253f73f | -13.43353 | -46.96537 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6575f416-e220-322d-9c24-d31f2940543d | -13.07819 | -46.34788 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4df2ece-3d96-365e-8072-2da4a9aba0f1 | -13.45154 | -46.84468 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a951afb9-b36b-3571-95cc-5237e312aa42 | -19.67335 | -49.37018 | 2025-08-28 03:47:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdf466b0-9bfa-3bfe-8bb3-60d6564c482c | -12.41058 | -46.48227 | 2025-08-28 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33067457-5e40-3e5e-8771-aca0a1177f24 | -12.80401 | -48.14945 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91494554-2413-3617-87ae-a6d569143c67 | -13.42486 | -46.98836 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24aa7391-c304-3f6e-bca1-5cba235e9485 | -12.18796 | -47.1859 | 2025-08-28 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62b9a2a0-2f4c-33c5-b196-4cb1c127a73d | -13.42054 | -47.00144 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cd7d5d3-d2ef-3879-a6bf-9687df75fa1b | -16.80772 | -41.22713 | 2025-08-28 03:47:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d7ca25a-9ec7-3afd-9b40-af8e657d7a5f | -13.52984 | -46.93319 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da91f63a-c0e5-31b0-b845-a61b8c8514dd | -12.67368 | -48.17464 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3999216-577a-3677-8373-2a1b9ed3bbde | -13.08109 | -46.3332 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8654d0d4-d0f6-31f5-90c0-bd74af5870bd | -11.54934 | -46.36138 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8562c8bf-6c16-3206-b9e5-4c79f1d9db7b | -13.6708 | -46.91441 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8aac136-aae9-3a38-aded-01f1bc1ad23f | -20.44063 | -46.01559 | 2025-08-28 03:47:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26679026-41b3-3f51-aa96-9751282300da | -11.32668 | -43.53115 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ce549ee-ca15-3fed-af48-fe58565fa4a0 | -11.7993 | -46.79209 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e2a1a46-1780-379d-b662-0ed6c4f5c81a | -12.78313 | -48.16568 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cc6c4bb-5688-3c7d-ac0f-aaf16001019d | -13.50399 | -46.85826 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c32bd124-3224-3773-ab2f-bde7f931380f | -13.45398 | -46.98078 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c61e24f2-9247-3d84-9277-c85c71e8dff4 | -13.59523 | -48.14962 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
