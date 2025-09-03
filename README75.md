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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76924bc0-54f2-38c4-a37c-47249455857b | -12.63466 | -57.00538 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d765d66-ab3f-3d84-9ab5-ecb6ab07fdc6 | -15.9025 | -48.16851 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c31cb176-3ae3-3d8d-a7b0-40a067d3460c | -16.34924 | -46.92009 | 2025-09-03 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 148e8f5b-e640-3c6c-8a17-e2ac47831727 | -12.98518 | -48.08413 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7b88ca6b-7e56-3ba5-a07d-0567149d305a | -15.5656 | -48.4057 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 902afbd9-9a8d-32e5-aa4f-b034cc465c48 | -14.27163 | -51.22591 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4c11e77-1d1e-3ca7-8d48-5df677487d44 | -16.30327 | -52.94487 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22603bc4-a323-328a-a9be-ebc258d92dc3 | -12.51817 | -49.5771 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb606176-d8d1-3f04-ae31-1059ff393390 | -14.78794 | -47.50671 | 2025-09-03 04:49:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 417b6c25-cc8e-3e4d-9b4b-569035496ab2 | -12.88823 | -48.0887 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e722697-c305-327e-9088-5354e24131a3 | -13.49502 | -46.82396 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f23ee6e-95ea-3b68-b121-203931b0a7b8 | -15.74471 | -53.69138 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92164880-2b49-3cf3-a596-9b64dc2a937e | -12.93463 | -57.00192 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 154180ca-4d56-3344-9266-d60612ae7a85 | -15.54674 | -48.31451 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a13a44f8-73f2-3490-85ac-7a103932622c | -12.84908 | -48.02686 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5928014b-fe07-38a6-8950-301be868dca5 | -15.00601 | -50.06153 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fb8fd23-6350-3a71-8fc0-e07852bdd948 | -16.30657 | -52.96749 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8aa9b16c-eab3-3a85-aaf6-efc94032b5c4 | -13.35912 | -51.73081 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46ab8a4f-b82e-3480-8f22-58ab9904f67b | -14.55958 | -53.05283 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e2e80d-1ab3-3efd-84d7-5576cc8ad4fe | -13.33835 | -46.83355 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae66e1b-6424-3411-988a-70dc0f34fc94 | -15.24413 | -53.80199 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebdc71de-84f5-3b05-8b42-eaeeaef372d9 | -15.03407 | -50.04432 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d83b369-82a5-3a1c-b4a4-03b188a42a84 | -13.0003 | -48.09377 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f581d3e-485d-3f9a-8d55-1a46f17ec2bd | -14.40806 | -51.69431 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39a0bde0-1ad7-317b-9347-7003a506d3b5 | -11.85836 | -51.54613 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f90242e-2ba0-346f-afcc-e57175ce805c | -16.30492 | -52.9562 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e54abdf-a7a7-3af4-abcb-9c1a51933f5d | -12.92263 | -56.94174 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6dce619-6c60-36e7-ab05-e7831ac9a3cf | -13.52446 | -47.02318 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ec06ee7-40e4-3f96-b9cd-fe2f721245ab | -14.56399 | -53.04628 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f36b85b2-a1a9-38ba-a66a-f80e1cfbe26d | -11.85496 | -51.52369 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 240eb0fa-d71d-3496-9c13-1ae7ece855e0 | -11.86879 | -52.42479 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1750981a-b906-31b7-9e4c-5b1ca059fdfc | -12.94101 | -56.98803 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 65541fe9-eefc-3e91-a6d1-3cb3223e58f3 | -14.57064 | -53.00371 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7dbcd64-dc0a-394b-b487-68105da4c18a | -14.58546 | -54.57393 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4b461a-6ecb-3d1d-a253-b733985b2bc8 | -15.1599 | -52.35705 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 583f578d-b416-3c2a-99b6-0467512b2fb8 | -12.92203 | -48.08036 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8413628f-755d-3fee-b655-8c1041cfa604 | -13.00747 | -48.0996 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 281f0aef-62cc-35c6-ade4-5a65de6a7f6c | -13.27509 | -46.88713 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a90507-21f7-327c-be32-abb019bcde52 | -14.81011 | -48.37704 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d13d460-8505-34e0-8a7b-ca9a7f9dd024 | -14.58684 | -48.04635 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd46ed17-0c44-3396-878a-855b206474ca | -14.99243 | -48.80645 | 2025-09-03 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a44d0389-66b2-3d81-83d0-c198befb1bc5 | -14.79797 | -48.20198 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c81681e-fb4e-395c-a846-8a94cc3fa231 | -15.22322 | -53.78377 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaee3e81-fea6-329f-a816-da4e810c9363 | -13.27016 | -46.89266 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4fb81a-0605-3d25-9da2-fd825e557a53 | -12.29208 | -50.00818 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57727e54-edfb-36bc-957b-4a8289da4a75 | -12.64102 | -56.99155 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a21fc032-fdb1-3d5b-81df-2a17cf93cea1 | -12.64018 | -56.9964 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae168e06-bb0e-3f31-83cf-41dbe675d191 | -11.86769 | -52.4318 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94bf63f-e173-3764-9726-22d20dd35fb4 | -14.2722 | -51.22215 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1908c75d-e56c-3001-bce5-c2266c38a313 | -12.60397 | -56.99992 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e8ddede-f102-3729-a6d3-8d970a1b7533 | -16.59759 | -48.97642 | 2025-09-03 04:49:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11c14ebb-b728-3a88-b2f8-1ec3d30c0930 | -15.54997 | -48.32059 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97126217-d62e-3b5f-b563-25ec8f3364d4 | -12.99365 | -48.08051 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbb44fff-8967-37c1-93ce-66b44d395e64 | -13.5034 | -47.02032 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a780a765-a3bb-3278-b860-ecdba0c7dbe0 | -11.87485 | -52.42936 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b9a8e21-ff68-3d5c-97ec-8d94b4ecb0fb | -14.61875 | -48.11058 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57a847cb-8039-38d6-9a97-8265146a9d6d | -15.55835 | -48.39941 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07ebf051-0231-3a4a-9978-8d07bd6a6600 | -12.94228 | -56.95842 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f9882810-8926-3a54-9bd8-b3e873ac80ae | -14.57209 | -48.06518 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29898e41-4a23-359b-8642-99836220513f | -14.81848 | -48.34425 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d53eb239-12cf-31c4-b7e0-65595149b367 | -13.81643 | -56.6084 | 2025-09-03 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af7df720-c162-362d-ab63-146174b6e0e7 | -12.88796 | -48.03408 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9bd7eec-282b-38ca-8d1f-95f777a2aca9 | -15.17702 | -48.01352 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a97908e-88c7-3281-b23d-f997529d0364 | -14.96821 | -50.20593 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a7ccb2-972b-3115-974b-3fb7d78f4880 | -13.27789 | -46.8348 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ee1b38-1933-348b-9d0f-012cc80580fe | -14.57442 | -51.40261 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91f932d6-586a-33a4-8e7f-0bf9adbdbd00 | -12.90313 | -48.1024 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e16a4faa-c654-38d9-8c98-7c2c2d588c1c | -14.61275 | -48.09509 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee9547f6-86f3-33d0-bd88-9abdb67d9537 | -12.18087 | -53.88585 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ae0ced8-cb49-3008-abbc-18ab173df185 | -15.02394 | -50.06424 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc0eaf4d-5f6b-36b9-a44f-9a89bbfba3da | -13.20805 | -51.81057 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a730c98-67fd-31a5-b4a9-3348948ec6bb | -14.76149 | -48.1418 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b86fadb-488f-3ba5-bec6-272be94a2eb8 | -11.86603 | -52.42075 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b3c71e-b5b3-3743-9cf0-c223d75aa555 | -13.00615 | -48.10936 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8493c082-82bc-36e8-aa35-fd75362e5a13 | -13.4545 | -46.9323 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b39d55e-38fa-3515-8eed-834a506db092 | -13.46339 | -46.93026 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12bdcecb-81c0-35c8-8622-f89e818b44dc | -11.659 | -57.35224 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 438023fa-4f17-315a-93b4-491cf11d823e | -12.89302 | -48.05474 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b3487e7-ece4-300b-add3-12b69a991336 | -12.60498 | -48.19986 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e98942a-df7d-3203-865e-014d29afacf6 | -12.92343 | -56.937 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb840392-c484-3991-b81e-7593bba63dc0 | -12.90193 | -56.94806 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fddd3869-ef2c-389e-bee8-104cd3f408e8 | -14.50955 | -53.15322 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d465b950-4a4c-36da-8d4d-4e96b3ae2f2a | -17.53892 | -46.62152 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae00ae4-6acc-3879-8569-7b5e4301a4e0 | -17.94494 | -47.2295 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2d8433e-d3e5-3b62-8839-e35c95933366 | -17.37349 | -50.34853 | 2025-09-03 04:49:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c35d5df1-6ce1-3e1c-b8cc-85047cb80f3f | -14.56124 | -53.04219 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21c21df2-a953-365d-8bc9-49b5251f5fa7 | -15.01435 | -50.05427 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9175cdce-98b9-36a9-bb4e-08c46a83d32c | -12.62399 | -56.99853 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ea1937-97ff-3a69-9a6f-e43c54a8d3e2 | -12.91222 | -48.09402 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fbe2121b-86bb-3d62-99e0-8e43aeb4d32d | -15.55759 | -48.41299 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cf577b0-9bd3-3a60-bbf1-74684a57a78e | -15.3795 | -52.78608 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a2aea19-b490-3f54-8908-2da68742d3e1 | -12.94397 | -56.99358 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd31b0cf-cd16-326a-8ef4-e79151a42c5f | -14.57395 | -53.00426 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c7c51cb-c050-3660-ac95-a0f736c0ad5c | -14.04838 | -44.62233 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e9f9722-6398-33eb-b0be-1be1a140942f | -12.92995 | -57.0061 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f33b0509-a156-3996-8ad1-b8af7d24eea1 | -14.57255 | -48.06173 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdd551e3-746c-3bab-81bf-6e49888fd057 | -12.94143 | -56.96323 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27989543-b1b2-31fd-af56-ec9a2bf999d5 | -14.26767 | -51.22913 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd530625-1ac6-3cb8-9d3a-31a776c4dd84 | -15.55508 | -48.39354 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 881f4b04-1232-3422-85a6-7f5770588dfa | -15.71686 | -49.04235 | 2025-09-03 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README76.md)
