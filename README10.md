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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90d6cd8a-9e44-39f5-9f66-40455bc7bf0e | -10.82284 | -46.52584 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 352191e3-583c-3899-a282-3273c001dfed | -12.44981 | -49.58447 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e708d97d-38cd-35c3-9d18-e46d04ecd0da | -12.68681 | -48.20692 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1868d873-7fda-34d6-9db8-7acf2e9aa7cd | -10.81861 | -47.39683 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97ee9fa3-abfc-395e-bfd1-7eae706ca3d1 | -12.1162 | -49.93878 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c61e9661-21b2-3772-8141-e23d5f6a759b | -5.53037 | -47.49153 | 2026-07-17 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47ac745f-93b7-34b2-b998-4e2d14d88f4e | -13.43821 | -43.85133 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| faa69d4d-fc7c-3b4c-b674-2d0c49a738d4 | -8.51059 | -48.07878 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a43bcfe-4795-3585-bb4d-e0a9e21ca7a4 | -13.00462 | -48.52455 | 2026-07-17 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 802c5414-9f3d-3b26-b582-bab419b16e68 | -10.81968 | -46.53288 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ed4cd14-6c8f-3883-b69a-a66b2a846fa3 | -10.86466 | -46.49953 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6302ecc6-737e-3bfd-907c-c1a146c8ee08 | -12.45539 | -49.5931 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aba14f3-e0d5-3a27-9c3e-b841e987c79d | -7.83634 | -47.10342 | 2026-07-17 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85033088-1236-3ace-824a-55162a66aba2 | -12.45662 | -49.58563 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9aa3d49e-03e3-3c19-bbef-29778781096f | -10.81577 | -46.53591 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d227f5b-5fb5-3b3f-a41b-8dbc794c3fba | -13.2451 | -45.1142 | 2026-07-17 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| a2539980-8f7a-35a1-8f4b-a4d9dc763830 | -13.2649 | -45.0877 | 2026-07-17 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8e8f953c-c3a5-3035-89cf-f903338237ff | -13.2456 | -45.0909 | 2026-07-17 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1c8437f2-5dc3-3e0f-9f19-63713be8f35f | -13.2645 | -45.111 | 2026-07-17 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8de57d15-a954-3f55-8ae0-c7db9984c227 | -13.55111 | -47.78931 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d534214a-c630-349a-9c4f-7c14cfc0c5ef | -20.33714 | -46.63489 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d475680-d687-34d5-a84b-11fa7eae2cf8 | -20.64288 | -41.40679 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0ce3daaa-a1bc-38eb-ab11-8595cbf96d79 | -13.55996 | -47.798 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5f48519-7121-3529-97f2-ac907f964089 | -19.17801 | -47.35402 | 2026-07-17 04:40:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e371bcd-9492-3c66-89e4-94af72d652b1 | -20.65413 | -50.10963 | 2026-07-17 04:40:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b117eb44-8399-3651-8e0d-f1118fe145c3 | -13.55055 | -47.79286 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e9f2d77-0a6c-36cb-8e6c-8ad301c94a8c | -20.43632 | -43.69528 | 2026-07-17 04:40:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 114dffd5-0b0f-31e0-a181-deee12e70452 | -16.52158 | -47.73423 | 2026-07-17 04:40:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2a909037-b7b1-3aac-bb04-c0091f653b7d | -13.64548 | -45.54747 | 2026-07-17 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a485d70-e008-36f3-89c8-e4c93b18ead7 | -20.7318 | -47.325 | 2026-07-17 04:40:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 270992a9-0593-3901-b195-5fb8d5497c43 | -13.55 | -47.79641 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebed2616-10ff-3388-8e0b-bbe66acdd113 | -13.88648 | -46.35058 | 2026-07-17 04:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7f672b2-5aab-3ef5-a218-5a7932b842d6 | -20.32874 | -46.64248 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 821a9423-f80b-3012-9463-eccf1e2bfb5f | -17.34082 | -48.68595 | 2026-07-17 04:40:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9613381e-3315-3b91-980a-5efc3eaadb0e | -13.52383 | -47.79607 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1dd3f6-63a0-3169-b034-3044c891bbfd | -15.11164 | -48.55787 | 2026-07-17 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4cf3190-d063-3d77-b8dd-be3cee1bac73 | -15.65598 | -43.32393 | 2026-07-17 04:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0baaa647-f518-3521-9a75-d058bd899684 | -13.54834 | -47.78521 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89de6e68-745f-3321-a1cc-3be34059bf92 | -20.63865 | -41.39975 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3907ad8-4633-31a4-8cfd-3bd42ae2acde | -20.33658 | -46.63888 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7f209b7-fbef-3f88-a777-64e7ea687236 | -20.63874 | -41.40019 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17613804-765e-39b4-a20b-50e716055528 | -19.88334 | -51.94778 | 2026-07-17 04:40:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4202931d-1afb-3c15-8267-a4a73b238814 | -19.83906 | -49.076 | 2026-07-17 04:40:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c8bdc7d-2259-34ff-be93-6de86c9fdba9 | -20.33294 | -46.63869 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 570dc3e4-af42-319c-9c0c-1229f0ec16e4 | -18.55504 | -56.81515 | 2026-07-17 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 304c358d-8675-3710-9c8f-eaeadbc05daa | -14.73217 | -47.14443 | 2026-07-17 04:40:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd1f029a-738d-3a7b-9841-b0a9a2ed96d5 | -20.6508 | -50.10904 | 2026-07-17 04:40:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae2a3aff-4f3d-3ce9-93bb-6df54fca0ba8 | -12.41544 | -58.40094 | 2026-07-17 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9347820-3c07-3b9b-8631-6b6acc63f271 | -13.51995 | -47.79906 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0656ac33-a56d-3523-bc3a-c2d79e5114de | -12.41523 | -58.40379 | 2026-07-17 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fc419dd-a646-3dbf-a96e-befb832f7e18 | -16.7846 | -49.37422 | 2026-07-17 04:40:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4bc5839-311a-3aa4-81b3-0a1e9b3332e9 | -14.7288 | -47.14389 | 2026-07-17 04:40:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5d583b2-17c6-3103-905f-bbcd441eca91 | -14.88876 | -48.46919 | 2026-07-17 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4918a2ba-6b67-34e9-8751-0d2329866982 | -13.55167 | -47.78575 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d773b424-2589-3752-a842-4ae1106b260b | -15.2413 | -48.57193 | 2026-07-17 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cbaabf0-43af-308c-be7e-badcce4e2975 | -19.17742 | -47.358 | 2026-07-17 04:40:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67f65bdd-745a-3902-a0d3-fea28371c62c | -21.27728 | -44.51012 | 2026-07-17 04:40:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 86d035f0-3890-3c75-ba52-a7fa52624293 | -20.34134 | -46.6311 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78e9b731-bc75-3d81-ada3-285a42b32a98 | -20.33238 | -46.64271 | 2026-07-17 04:40:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2489235-676c-3a20-9c7d-b21c0ff35d95 | -13.56882 | -47.80672 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d334703-6e7d-3a16-a1d6-2421e69f46a9 | -13.64196 | -45.54692 | 2026-07-17 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d04399ef-34d1-3207-b220-5798721b2748 | -13.53331 | -47.75753 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ade5cecc-fccf-3c60-a4c3-72bca396273e | -13.54599 | -47.78517 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38cb2484-3c1f-325c-acbf-4edc5e4f775c | -19.18146 | -47.35456 | 2026-07-17 04:40:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25532ad6-e4da-36c9-90bf-08e179e5ead1 | -19.13811 | -51.7383 | 2026-07-17 04:40:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eba072eb-3997-301a-8195-dc1e9847b511 | -13.56549 | -47.80619 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4546159-c67b-3563-9d30-2c8e63259aab | -15.24073 | -48.5755 | 2026-07-17 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ccb8f0-a76d-31d4-a853-f04a2b4fdc59 | -19.17859 | -47.35003 | 2026-07-17 04:40:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91192bcf-e5d9-3b3c-914c-1669aaca7bd4 | -17.59179 | -44.60025 | 2026-07-17 04:40:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b731c02-4bb3-3962-a9ce-4c53486a9e00 | -13.56494 | -47.80974 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 364fe27e-ab40-333d-a06a-b93003de67e3 | -14.13942 | -46.26831 | 2026-07-17 04:40:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8e58c00-cc36-3fb9-b9c2-6b473ab76fa7 | -13.61223 | -46.15793 | 2026-07-17 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4069a6b0-7f47-3567-bce7-810880673949 | -14.14229 | -46.27267 | 2026-07-17 04:40:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db3aa10-b43e-333a-93bd-547da6767692 | -13.25478 | -54.39233 | 2026-07-17 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3b4fbe-38a0-3989-aa47-34cb423b17a6 | -20.64303 | -41.40723 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3df666a1-0973-36fd-b917-b8b8016f0f03 | -13.55387 | -47.7934 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad12a4d-2b3b-32ac-b2bb-641bcca4e2fc | -12.41606 | -58.3997 | 2026-07-17 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a399e09-aa1c-3791-bce4-4bdeae691da8 | -20.63819 | -41.40541 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 45159837-6e8d-364d-a165-7d4b2847ec36 | -12.41464 | -58.40506 | 2026-07-17 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d7250c3-26da-3563-a6d8-57c0b8f37d95 | -20.63806 | -41.40499 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 454c1a5b-c096-3315-90fa-c9dfc59d3f36 | -20.70794 | -47.29155 | 2026-07-17 04:40:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a6083d-db7d-3234-b808-b4ad9ebd02ee | -20.6144 | -46.29419 | 2026-07-17 04:40:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1566aec-fa74-377b-906b-a6ed3f37bfa7 | -13.50795 | -47.54927 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91752276-57dd-3304-8567-e6ce361f548f | -18.55867 | -56.82124 | 2026-07-17 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2ee0c4bf-4fb2-3484-91ff-bab7a09355a5 | -18.55966 | -56.81619 | 2026-07-17 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 276760e7-7fca-3a48-b0fe-85f90e08b107 | -13.56605 | -47.80264 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d1062f0-42e4-3da2-8837-12b2a00daec3 | -14.14286 | -46.26887 | 2026-07-17 04:40:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a65e9d5-7b84-3390-8e2f-93856c04b2d4 | -13.56329 | -47.79854 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe818eb-a61a-314c-8704-9c894cff205c | -20.63753 | -41.40968 | 2026-07-17 04:40:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f32dbe80-d0e6-31ad-8664-3230de3d526b | -16.14627 | -43.63539 | 2026-07-17 04:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db41e250-0b17-390c-8967-e78d078fc599 | -14.1463 | -46.26942 | 2026-07-17 04:40:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab0abd10-1f59-3f95-b0db-b48eff11798b | -15.8391 | -50.88961 | 2026-07-17 04:40:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521159f3-9752-3244-bf43-d08db57be142 | -17.00462 | -48.28497 | 2026-07-17 04:40:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f464dba0-6c14-389e-8483-9044d8322076 | -14.72803 | -47.14381 | 2026-07-17 04:40:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6741ead-6392-30e3-b2c3-cbabca12ba05 | -13.50235 | -47.65062 | 2026-07-17 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c88f79c0-cb9f-3acf-918d-4837e539bdd2 | -18.95671 | -49.57201 | 2026-07-17 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae3c460d-79f6-3fc9-a907-a984643fb2dd | -21.68211 | -47.93832 | 2026-07-17 04:42:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4cf68a0-a542-39c1-ad42-a0ff6a252940 | -22.91909 | -49.20266 | 2026-07-17 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 308486a1-89d9-3441-9bde-439baa49ea97 | -22.21981 | -56.10656 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5275ca4a-58a3-344e-a962-963e7a810fb2 | -19.81846 | -57.96883 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |


[Clique aqui para ver as próximas entradas](README11.md)
