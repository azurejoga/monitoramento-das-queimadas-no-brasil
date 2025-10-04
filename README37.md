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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47fe4a84-cb23-3feb-91eb-60a2684cfc86 | -13.32416 | -48.10928 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c2f318c-9c8d-3e5f-8ec7-44684903c562 | -14.63319 | -48.23568 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e5588f9-183b-35fd-9de4-70c5aa870d61 | -11.91949 | -46.35595 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93e08e54-6644-3f21-9bc5-e4480c9840cf | -14.9187 | -46.8969 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31f49c56-4f5b-3dc2-a3ab-788508a4daf1 | -12.41015 | -45.16451 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9fb2e10-ee3a-319c-9897-cffe2896aa97 | -12.09218 | -45.17612 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6f8fdee-8644-3b02-905c-b5e46decad69 | -13.74511 | -48.07819 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 381a16eb-e751-3a53-9176-2554d90aadac | -14.88671 | -48.2795 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb057604-cbd0-388f-93cf-081378eeee73 | -14.24435 | -46.09391 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| f2214a19-2bcb-370c-a01c-66ba9a1eb6f5 | -12.09418 | -45.16955 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244ed098-1dc2-388d-826e-aa2c53ad878e | -14.98169 | -49.97268 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef88d981-b68a-3049-aad9-7c38509aa437 | -12.71512 | -48.55301 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8a763dc-13e4-3e03-b29b-afeb1e5ebd4e | -13.34975 | -47.23308 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1927f2db-ccc5-371e-a457-d5c85277e977 | -13.10356 | -47.90618 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2758ec7c-0827-34d6-ac4b-b619bbadb9ff | -13.3905 | -47.54871 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64b3181e-0e07-3667-b120-87874318c9a9 | -13.31825 | -47.25371 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af70129a-38b4-37f8-bf33-43f8707fafc5 | -17.086 | -46.23959 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e87d90c6-bdf5-38ce-9dd7-05731decdb28 | -12.30619 | -45.36803 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6d18dc1-0bbe-385f-b3b3-5a49221af4e5 | -13.34819 | -48.07328 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ad77907-de54-3833-a3c7-7cadbbf0bc85 | -12.70384 | -48.55055 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ad0c1cc0-a24a-36b6-9766-f1f79b33e0e3 | -16.82027 | -46.73026 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7b3fad0-7006-30dd-b6dc-cb716bda5fb5 | -13.31056 | -47.26604 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3362fd67-4f4c-36fb-89e6-6b64f2bac87f | -16.29184 | -45.24187 | 2025-10-04 03:53:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36b20b07-a8de-37dd-9f1b-3675fa966a55 | -13.12619 | -47.93356 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51e625c3-6eb6-3652-9459-282d8162e3a2 | -14.20799 | -46.07555 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5ae5f45-c6cc-3379-8f12-90811a90a60f | -13.32991 | -47.1925 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6de1e84b-3323-36da-80db-7f70ca96bb14 | -15.30006 | -47.94795 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4750e8e4-6006-3fe7-b86d-b42eca935532 | -13.73308 | -47.92941 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c99e91-0040-3f2d-aeef-6f5110c70f0b | -14.90343 | -48.27943 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c32e5423-ce2f-369d-8535-8e4033b69b35 | -13.26155 | -47.21516 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2208d1fd-a602-36a5-b498-128d8cfa1fab | -13.2069 | -47.81594 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 273604d8-c998-3007-941b-8964680e9a91 | -13.32023 | -47.57744 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b01acab7-bb6a-3e7e-9035-042e95b883f9 | -13.59931 | -48.1816 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4b11530-0170-3834-b248-f9dee64b7da8 | -13.38936 | -47.55444 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f4d7aa1-326f-3305-a029-6f06d7f4c558 | -12.70447 | -48.57717 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dda53b96-0154-38b6-ba6c-f894379e5be0 | -15.18988 | -46.39763 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c206c916-957d-382b-aac0-9ec5ad9d3f82 | -14.89248 | -48.27852 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44f430fd-d551-38b9-ad2e-bd6de3332f58 | -11.92525 | -46.3802 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 3a7105ee-1c5c-3788-9f39-63c32121d92d | -14.24229 | -46.10478 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 71a84d5f-1bfd-3373-8f7d-1cd0983edb11 | -13.26896 | -48.15865 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3abbcce6-7041-3ecb-9db0-547a425e385f | -17.96001 | -44.26474 | 2025-10-04 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77333fff-fbdb-36e9-adcb-6d143f125b74 | -11.78526 | -46.83825 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b69f272-fd35-32ec-bbef-4eefc4653872 | -11.87379 | -44.98448 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2120d1b1-0ca1-3f77-a0dc-28e878497780 | -13.78028 | -47.81765 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b5208e-0f51-3265-a6c4-1fcadef5f987 | -11.84137 | -45.03296 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e2be21e-7c81-3c51-a9a6-5add085122e3 | -13.76672 | -48.05397 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccd0d00d-bba0-35b1-bbdc-d9d186bb3c20 | -13.13702 | -47.93555 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f704594c-9a4d-349b-9baa-55c08c4fd405 | -11.55604 | -46.99111 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60e089da-b198-3f0f-a523-f1fdc7a6a4f2 | -11.90692 | -46.73917 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c360953-a39b-3072-a5c6-1bf0cdd322e3 | -11.54275 | -47.67229 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3eb6139-2e3f-38d2-9a1c-e2d2aec01d29 | -11.91816 | -46.39037 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 138de69a-d4af-3cc7-9253-49ab06cf905c | -13.31755 | -47.26078 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 505b5f9c-132a-3027-813c-6747ad70d2a1 | -16.02423 | -50.94893 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cb9916f-e430-32d4-8748-9369e3f7340d | -13.70556 | -47.3462 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca58eaeb-984e-3618-a68a-5ce540d9687b | -14.925 | -48.33882 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f07c1b7-21db-3973-8bfc-dbb7a7904c83 | -13.24139 | -47.83842 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcc094e4-709c-3d4c-ba01-6808be285f9d | -13.10881 | -47.90799 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 885c8c98-2976-3f36-ad31-9c563a756e45 | -13.4672 | -47.26837 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d667f52-9356-3896-9c46-d338eb63dd92 | -14.67746 | -48.27349 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5ef2971-451b-312e-bb25-1391f6b3ec10 | -13.32756 | -47.62423 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f27bb9f-701f-379a-8da2-b5f139129c44 | -14.66617 | -48.30168 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e3e93d65-bdba-31f5-8514-9f716ca8053b | -13.98333 | -48.19236 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dd664ea-3cb6-3751-8778-710ed3576761 | -13.98055 | -48.12104 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95069d9a-9662-308e-8c9d-1e55194d4e22 | -15.99724 | -50.92434 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab4b9b2a-bab3-3d52-b74c-9c9cf2dd223a | -13.26861 | -46.4812 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 478e697c-69e4-32bd-ab05-15f7ebf8e8b4 | -13.25624 | -47.24246 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b03280c-327a-37a2-afb3-4b77ae4e6dd8 | -11.83991 | -44.93851 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e81b351d-a242-32bb-b5a2-7a7f8d86b95f | -12.81614 | -46.8607 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff4ab5aa-e538-3e15-b021-3d81c3fd5bba | -13.57653 | -48.18225 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39638699-fe13-37ea-b3a7-5677b7e8f9f1 | -15.81968 | -46.25153 | 2025-10-04 03:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d72c9b9-a1fb-3538-a021-c1b1ed2749cf | -15.27702 | -47.15035 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaf76c5c-c386-3a93-af42-f8cc273131a4 | -14.8744 | -48.36802 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25d87313-eece-30cf-95d0-667cf66a916b | -13.46844 | -47.26204 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c0d6e27-1bfd-371a-a1bf-d4c3681cfb73 | -13.30099 | -47.59194 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9e9ac8f-d666-3b2e-9a34-4a0527b685ab | -17.49938 | -43.46782 | 2025-10-04 03:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e9aa98-d17a-38c6-8237-63dba79af6ff | -15.52908 | -46.80979 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38dc739f-6334-3fb0-a1d7-753bee61b0bf | -12.58891 | -47.00354 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58fe9690-7643-3705-861a-a05206f8feef | -12.03965 | -45.20806 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 784cb168-9c85-3676-8dc3-6566a047c553 | -12.36893 | -46.51032 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ad44c2d-18ea-3a1a-bf81-aebb7b74b49e | -14.9315 | -46.86373 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7b6dfcc-600d-3ee5-ae8b-96bb3103d551 | -14.20127 | -46.6629 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579bfcc5-21d0-38ac-b434-adbe2cdc9a9f | -13.30004 | -47.82285 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df1a054-7d14-35b3-8fc8-4d78d14433cb | -11.92312 | -46.39148 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0f7e0c7-73c2-3f55-a28b-a43cac41054d | -17.55853 | -46.76263 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92440134-1c50-374d-927f-9c2a99ae4acb | -15.60891 | -46.929 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d3cb7a9-b02d-316c-873b-686f03cb46b6 | -15.83611 | -42.6182 | 2025-10-04 03:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96bae876-22af-3d45-89e1-32e382b19b4a | -15.31735 | -46.37996 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f89553b5-d085-3866-b379-c5489adae198 | -13.74849 | -48.06124 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cb0c200-c1bb-3027-9529-f9c2650f633c | -12.70317 | -48.55392 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f86d7a9-21dc-3229-9684-6fea3d1d9ff1 | -11.91035 | -46.73973 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab69639-9bff-3c06-8b70-bd57929f985c | -13.3144 | -47.2459 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f93c522c-7c88-3176-85aa-5b350339d4e1 | -12.07706 | -45.1855 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d195bdf8-ca07-383d-bcff-2176fb099797 | -15.31837 | -46.3748 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 385a579a-7032-3d38-aa19-5164ea07840e | -13.54647 | -47.24442 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 950f8fd6-1171-36e9-84c0-789367760795 | -17.08321 | -46.25374 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 788733dd-4d7b-3349-9d58-bb656a33a03c | -17.1536 | -47.03737 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d39d48c-6a6b-3337-8a23-afeac29fe2d6 | -13.33986 | -47.19611 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb61ac24-9087-3ccc-846a-88dd7719aa6e | -13.33669 | -48.07436 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ec1acd-9779-36b2-a70d-f571b99ec859 | -15.57939 | -52.47307 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f68c6317-4c66-3d3e-a962-62b666dc32d6 | -12.6614 | -44.24251 | 2025-10-04 03:53:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
