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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f059ce34-1a04-3514-a6ad-8f92ce75c8b8 | -21.80872 | -47.25047 | 2025-07-24 04:44:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 200162b8-f068-3ce5-86e3-cdf110593a48 | -20.35341 | -50.19128 | 2025-07-24 04:44:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 252cfe51-d261-3e8d-b002-d717b0b7510b | -20.29609 | -54.07542 | 2025-07-24 04:44:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d1dea42-6875-3f0e-9ddb-3c5db5ec2387 | -19.45648 | -47.25569 | 2025-07-24 04:44:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 697d6266-5045-375b-82dc-b6e15056d65f | -20.79006 | -49.38597 | 2025-07-24 04:44:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb55ce6a-0af7-3cbc-a96f-be02ae752d94 | -18.81412 | -50.62302 | 2025-07-24 04:44:00 | NPP-375D | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b4f1ecf-a324-30bb-bb48-3ad9eeb379da | -14.37182 | -50.32727 | 2025-07-24 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a11e0c4c-5c25-3c16-8395-244565555982 | -19.74591 | -50.19438 | 2025-07-24 04:44:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 629d82fe-4e31-35ba-877a-9867f2cb2bdf | -17.57538 | -47.5029 | 2025-07-24 04:44:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4a48904-0e7e-385c-8de2-6d16169bb495 | -17.57084 | -47.50732 | 2025-07-24 04:44:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ae538ab-3470-3163-9fcf-1a24f5d636ec | -20.40244 | -54.63184 | 2025-07-24 04:44:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc2fbee9-cf80-317c-9b7a-b0dd25f12159 | -15.57945 | -49.8375 | 2025-07-24 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11483a67-6124-3d5b-8460-922bd9da4107 | -21.73349 | -52.25373 | 2025-07-24 04:44:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aff0b634-86e4-3914-8b08-d2e5f9b33a4b | -14.37517 | -50.32782 | 2025-07-24 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94ed1276-d089-3e96-b459-59b342968e27 | -16.68006 | -49.09188 | 2025-07-24 04:44:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dd62dfb-871c-3e21-82bc-3692b843afff | -22.69924 | -43.34741 | 2025-07-24 04:44:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 17b47408-fc13-35d8-bc8f-b10e9a77c777 | -16.33974 | -52.07916 | 2025-07-24 04:44:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e10b2111-bb37-3207-8424-52e9603cc3b2 | -19.67479 | -43.23275 | 2025-07-24 04:44:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e08fd048-06a8-39ff-85ca-2d466db75f8e | -18.11478 | -44.63256 | 2025-07-24 04:44:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee7da1f4-afa0-353d-86ba-b1cfbf504b9e | -14.76769 | -48.27263 | 2025-07-24 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af9d6f13-c1e6-3958-8cee-4ee8631c547c | -19.80719 | -47.25119 | 2025-07-24 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c7d82c2-48e0-3d38-ab12-7e91bccb5717 | -17.76403 | -48.26742 | 2025-07-24 04:44:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c7db55-97b9-3a40-a791-3ad4c233d7a9 | -15.73606 | -46.86335 | 2025-07-24 04:44:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaaf90f5-fb37-3fcd-8561-0bece02a0fc2 | -20.84783 | -45.28332 | 2025-07-24 04:44:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3b2212b-975a-331a-813b-5d934cb4b0a2 | -15.28121 | -47.13281 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0de995fc-2543-3388-8b11-88850e516b0f | -19.39813 | -44.25319 | 2025-07-24 04:44:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 320bc0b0-b44f-38e9-ad69-5f1907f27258 | -20.60802 | -46.35766 | 2025-07-24 04:44:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af9dc003-4b9e-349f-a058-134b3bdd904f | -16.69461 | -48.0713 | 2025-07-24 04:44:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5397c70-dfab-3840-93f1-4ec2a7d4cc33 | -21.3111 | -48.57055 | 2025-07-24 04:44:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d07024-900f-3d8b-8ac8-e2cce754dde9 | -20.29208 | -54.07858 | 2025-07-24 04:44:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba7c652-5788-302c-b72c-73f1499d76b3 | -18.87901 | -47.9631 | 2025-07-24 04:44:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5536f570-6c51-3510-9764-a4bbce2e6b76 | -21.3648 | -48.53453 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a7587a88-2898-372b-84a9-b3d40210af8c | -16.34249 | -52.08333 | 2025-07-24 04:44:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bba8886b-f5cb-32b8-967f-c0980a7032c8 | -18.81733 | -50.62311 | 2025-07-24 04:44:00 | NPP-375D | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8d9b5060-1226-3f8b-a229-31139bec1761 | -15.76004 | -47.77622 | 2025-07-24 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03ff2425-9c65-33c4-8232-1692697b1751 | -19.05989 | -48.33578 | 2025-07-24 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d622b249-39a9-3334-b03d-ba630fe328ee | -22.69452 | -43.3491 | 2025-07-24 04:44:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7246a628-eaa2-3689-9ccb-e7b13ba12b76 | -20.28707 | -55.49607 | 2025-07-24 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91289ff6-50c3-3b18-aeba-3c32bbbddff2 | -15.30029 | -47.3816 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2302ee1-d546-3f18-8006-250c7a63ec00 | -17.80739 | -52.66056 | 2025-07-24 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c97e984-3230-3b7a-b5ed-dcb4d34a6de3 | -14.37127 | -50.33089 | 2025-07-24 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7245e6d-c61e-3391-9b0b-f2b598b44822 | -22.70027 | -43.34626 | 2025-07-24 04:44:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 09290b05-e4c7-300b-98f9-65f8878f5ec6 | -20.29271 | -54.07479 | 2025-07-24 04:44:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 420a4874-8a07-31e3-9583-edc96ce5ea05 | -15.28429 | -47.13883 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e36ffb9-ee13-3105-bcc7-1d905e416629 | -19.67444 | -43.2361 | 2025-07-24 04:44:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 75355b85-0b28-36a4-8b1d-9d11ddd445da | -17.81013 | -52.66481 | 2025-07-24 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56b9c537-d3d7-3b84-8034-ae34ac071f81 | -18.26266 | -51.13669 | 2025-07-24 04:44:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddaa33ce-fff0-32b5-aa20-9192df8b8192 | -21.36297 | -48.53272 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b4eea213-195d-3274-aef2-13f9b54adc0d | -15.7584 | -43.36768 | 2025-07-24 04:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0475dc80-0144-3db2-a5fe-fa60cc72f762 | -15.27663 | -47.1375 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc3c7f07-b6a3-3fd8-a43f-cf93a0b3dcc4 | -16.21945 | -45.97007 | 2025-07-24 04:44:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e476c3f4-4aae-3649-aa92-c808f5e793e3 | -18.83128 | -41.98363 | 2025-07-24 04:44:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e0984e19-b135-3768-beaf-9bb248ed5bb6 | -14.87656 | -48.34015 | 2025-07-24 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3a00cb-73e9-362b-a0ee-2250d3223792 | -19.3673 | -52.03604 | 2025-07-24 04:44:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93bb000f-ac12-3a19-9cb1-2cdd4edc9fd8 | -19.83492 | -47.29386 | 2025-07-24 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4b0f94-8a1b-3f61-990e-dde3e0663be1 | -18.40228 | -53.3274 | 2025-07-24 04:44:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0887fffd-ab32-3fed-bf45-d77076807938 | -21.36748 | -48.52828 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e494f4d0-7a25-3ebf-a0c1-6926174fe02d | -15.27739 | -47.13204 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebe68022-4450-330c-8d9f-84b743edbced | -22.69992 | -43.35001 | 2025-07-24 04:44:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c2128cea-a035-3fd4-94ba-75e272fb2606 | -14.33938 | -52.10152 | 2025-07-24 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 864b6d70-4d6e-3508-9881-50b26bafb928 | -20.29546 | -54.07921 | 2025-07-24 04:44:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c3b6d80-4f90-3cb3-8a22-b2fd81dc61bc | -15.27283 | -47.13666 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f1658e1-feea-3898-82c4-ec8f58476b12 | -19.45697 | -47.25188 | 2025-07-24 04:44:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f44faaf4-8e6e-37f7-8a23-7d0088b68e81 | -21.31176 | -48.56556 | 2025-07-24 04:44:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75db3de1-c590-3304-9012-569975f4c88c | -20.16003 | -50.98811 | 2025-07-24 04:44:00 | NPP-375D | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a13b1bb-b975-3945-a107-639bc1b13928 | -15.58229 | -49.8418 | 2025-07-24 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d09aac05-14db-3867-b583-f7da498c127f | -21.36682 | -48.53316 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 992546b8-4f79-313a-a5ab-c369f5b70378 | -14.87299 | -48.33943 | 2025-07-24 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4d1122d-78dd-361a-a405-fc20dcf104ba | -20.04205 | -45.64983 | 2025-07-24 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8ec608a-cdc8-333a-a0c3-457000c23eb3 | -15.82485 | -45.77776 | 2025-07-24 04:44:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c6593b4-48e2-362f-9a2e-6501b5144ae6 | -22.2428 | -47.05466 | 2025-07-24 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dd3710e-838c-3ad2-b3d6-54511d0caa16 | -21.34319 | -45.44574 | 2025-07-24 04:44:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9fd9c3bf-5c65-37f2-952d-a5130729caca | -18.11413 | -44.63784 | 2025-07-24 04:44:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1b7d087-3034-366d-92d7-7337e0fdc8d9 | -21.5658 | -48.50488 | 2025-07-24 04:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a973213-b9fe-3639-a8ce-1ec64289291d | -16.74292 | -49.18085 | 2025-07-24 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cea027d-6763-314e-90dd-720425fd28aa | -18.87837 | -47.96796 | 2025-07-24 04:44:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a04de687-b85e-337e-b930-9c03f49ec705 | -18.84965 | -47.9626 | 2025-07-24 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b4eafb83-317d-3060-9690-562e91a5fd3b | -15.58554 | -56.02541 | 2025-07-24 04:44:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b13a069-e9fd-3bd7-8a29-06572d348933 | -18.11572 | -44.63508 | 2025-07-24 04:44:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0903242-da37-34e3-a227-dab782660d23 | -15.62802 | -45.90524 | 2025-07-24 04:44:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff69814c-6e27-3464-9313-25a71d019ccb | -15.58286 | -49.83805 | 2025-07-24 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4aa194a-fc21-3bfd-8c6e-6a9d3c75f0f9 | -21.36814 | -48.52333 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db10cb7d-de60-3b85-9f8c-283cd52aa365 | -20.47708 | -53.67676 | 2025-07-24 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1816a07-abbb-3505-a0a6-b4b5a3e47102 | -18.82807 | -41.98122 | 2025-07-24 04:44:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f6efe9e8-f6d1-32c1-b5ea-8e0e16fc2840 | -21.36991 | -48.52515 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 999309c5-0b1c-3669-8d83-adb925d78c67 | -19.05612 | -48.33521 | 2025-07-24 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef90b91-b1bf-3cca-bef6-9db6f62ffa78 | -22.24331 | -47.05044 | 2025-07-24 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 390284da-1524-3a17-b2a4-9768c1e7bd3c | -20.04151 | -45.65448 | 2025-07-24 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c5ab8e7-bd44-3483-b249-f8b4029f636f | -15.30105 | -47.3797 | 2025-07-24 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c353da88-e106-3fcb-a706-560db0434ef7 | -21.76429 | -52.75359 | 2025-07-24 04:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcd9fbb0-f9c3-3e59-8ec2-cbc8272ac687 | -23.92101 | -49.10345 | 2025-07-24 04:46:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b470fe25-40a6-3343-a0b1-27fc09615b28 | -22.39999 | -49.79283 | 2025-07-24 04:46:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa553009-8539-3b33-974d-e20e8cfc8270 | -21.444 | -54.57688 | 2025-07-24 04:46:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33718937-dcad-3999-94c0-5854493a6f6c | -22.86949 | -47.10035 | 2025-07-24 04:46:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b8832bf7-e5e0-3829-82fc-ae9826cb0ce5 | -22.81698 | -47.15091 | 2025-07-24 04:46:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 73deed98-dffc-3543-9232-02b13db20d26 | -21.4863 | -57.11444 | 2025-07-24 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8133e5e-a3cf-316d-8dae-951b2e548eaa | -21.49893 | -57.06664 | 2025-07-24 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fda35b0-add9-35ca-ac31-6ea214e03d9f | -22.18457 | -52.74626 | 2025-07-24 04:46:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf71800d-0abe-3dcb-ae5e-c2434f2e4b85 | -24.10686 | -48.5724 | 2025-07-24 04:46:00 | NPP-375D | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a0f4d56-a7eb-3d94-9587-d50e62538d99 | -24.58633 | -52.82122 | 2025-07-24 04:46:00 | NPP-375D | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README20.md)
