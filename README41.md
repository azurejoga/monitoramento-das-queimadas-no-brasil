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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5f63b42-8eeb-3535-82c2-a8ce8b46dc35 | -22.36126 | -49.30806 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 989b8057-8ff2-344e-ab9d-d2153c3d09df | -22.36257 | -49.34686 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| be24e1dc-d292-3640-b266-4342b2a8eccf | -21.58331 | -47.89858 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 42c1b18e-2f7c-3bd5-9a9c-2106839817fe | -22.3631 | -49.31595 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 8fe4b0f0-5ec5-3289-aaeb-0d96243d7bed | -22.36452 | -49.33932 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| c142dc55-14db-390e-ba22-c47e851fd13f | -22.36493 | -49.30894 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4fdbdaa5-edbd-3826-b66d-30a9c160b992 | -22.36639 | -49.33215 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| 0cfc9aa5-e9c0-3bdf-ad6e-31ca2d9ef2de | -22.36675 | -49.30193 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 289d0bfc-19c5-3d06-a63f-e26f1bcc0a0c | -22.36758 | -49.35649 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 4e3ec3d4-e325-3aec-9b6f-9d21144a92e1 | -22.36829 | -49.32484 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 1e8f7072-0d50-31d0-be66-cde8e36001c8 | -22.36955 | -49.34892 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 685d0ef1-63f6-32d8-bd1b-51f1a1b78406 | -22.37013 | -49.31778 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 7ac1b183-8dac-3fb8-a99b-66ad594c82ea | -22.3714 | -49.34179 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| df08099c-baaf-33d0-ab23-d628ae2e1cea | -22.37186 | -49.31113 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| f64ddd35-aaa5-3b9d-a694-2c8bd9362961 | -22.37327 | -49.33459 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| 1a6ef2d7-cc27-39f7-9bde-69a6cfae84c3 | -22.37372 | -49.30397 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| efb45fd4-4fba-3284-a4ef-932ce2b2b878 | -22.37722 | -49.31939 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 73adbb86-56b9-3400-adc2-64cc69e15675 | -22.379 | -49.31256 | 2024-10-01 03:28:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 20fc55b5-bd69-3213-a161-dbd38f3f2503 | -20.62153 | -48.75388 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| da51685d-f3fa-3d09-ae2f-b834ec5a4ab3 | -20.62425 | -48.75743 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 665df388-9922-323a-b394-86d094acdc68 | -20.62866 | -48.75541 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| eb186b49-a4c0-316f-ba06-1e40377cf7cc | -20.6314 | -48.75888 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 21b4b7aa-0596-343c-95ab-5d3af5766f0b | -21.58284 | -47.84452 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| edfb9b64-b4d8-31c4-bf56-a6c20766a4d7 | -23.41359 | -47.52031 | 2024-10-01 03:28:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cbccd2dd-7b85-3798-bf87-d6c6ef291224 | -22.67537 | -48.34955 | 2024-10-01 03:28:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eecbb364-0335-36f0-bd39-b886a50a7288 | -20.64285 | -48.75873 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5e39e7c8-b7e1-357f-acb7-50208d285af3 | -20.64466 | -48.75139 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 81f7c399-9041-37b4-8052-548279b129d3 | -20.64041 | -48.75305 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b0f4bdd8-6632-3b89-9865-8f7b6698428c | -20.63757 | -48.74974 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| afd65ba2-26c0-33ea-98a2-df6c3c01889a | -20.6358 | -48.75688 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2543ab2d-862f-3f65-bd97-6121ab87fbbc | -22.35559 | -49.34476 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| cf3af0b6-c9d2-325f-bda9-4c062efa6503 | -22.74087 | -43.7575 | 2024-10-01 03:28:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9baa4755-66f0-3c37-be05-64e8b9258d05 | -22.73578 | -43.75611 | 2024-10-01 03:28:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0e24e033-b569-3b68-b952-fb80eabe17a7 | -22.67579 | -42.8534 | 2024-10-01 03:28:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6a7250e8-3a3a-3124-bcd0-e047414573f7 | -22.77978 | -46.81514 | 2024-10-01 03:28:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7f3af61f-ba5e-3e7a-952e-94646dd3c6d4 | -22.77843 | -46.82069 | 2024-10-01 03:28:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6c65d229-bae8-330f-8d84-1d541ca674f2 | -22.72383 | -46.67387 | 2024-10-01 03:28:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 2ebf2baa-6bd5-334c-98ee-553d65d38267 | -22.72272 | -46.67851 | 2024-10-01 03:28:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 1da0d2c9-fb46-39f4-baf1-b631b8232da3 | -22.7213 | -46.68442 | 2024-10-01 03:28:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| ab7254a1-fc36-3995-bcd8-9f2b8900f32b | -22.71977 | -46.6908 | 2024-10-01 03:28:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 62a1683e-ae77-3c2d-a8e1-837aa245ca22 | -19.47719 | -40.60085 | 2024-10-01 03:28:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7be9b9b0-46bd-3516-b16d-36556f8d3558 | -20.50205 | -41.06625 | 2024-10-01 03:28:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f336727-0700-3f7c-b4f5-64ada3a6ebbc | -20.50198 | -41.06379 | 2024-10-01 03:28:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3e1cc860-5270-3d74-a23a-96765fc4459e | -19.71653 | -40.35323 | 2024-10-01 03:28:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e584653e-9c79-33af-91f5-5549624972d5 | -21.93497 | -41.55321 | 2024-10-01 03:28:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| af9fd6c1-bafd-3b36-8382-f00f33f0e470 | -21.93465 | -41.55459 | 2024-10-01 03:28:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ae79edca-284e-36f3-b6ac-2e39777aaefd | -21.93394 | -41.55818 | 2024-10-01 03:28:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30f73e40-c9b7-3572-8c21-333666444cdd | -2.3863 | -50.3299 | 2024-10-01 03:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 6454121e-6b59-3fed-b628-770714fb1922 | -2.4046 | -50.3505 | 2024-10-01 03:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| ffc8c3a1-39a7-3be9-87a4-7f4f5a132d96 | -2.4047 | -50.3295 | 2024-10-01 03:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 405.3 |
| 5e88bcd2-94c1-3795-bb43-8af494ba2d15 | -2.4048 | -50.3085 | 2024-10-01 03:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| d7507128-3081-3380-87ab-77e6f86c5207 | -2.4231 | -50.3291 | 2024-10-01 03:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 043894ed-d453-3788-9c46-69a5f2c653a2 | -3.0282 | -51.3345 | 2024-10-01 03:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4d7e07d7-76f2-3f5a-ba3d-d59b2607cd7d | -5.9786 | -45.3847 | 2024-10-01 03:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 144c1e13-a664-3f3f-9e6e-836f93f4f192 | -5.9788 | -45.3621 | 2024-10-01 03:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5185183e-5e0e-3d41-a0e0-464e4efb72f8 | -12.1406 | -50.0524 | 2024-10-01 03:36:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 03bacef4-fa7a-3a98-b9b8-7a3e57764f75 | -12.2735 | -53.9979 | 2024-10-01 03:36:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c778d340-7df2-345e-9af8-1a7b02e877ce | -12.2738 | -53.9773 | 2024-10-01 03:36:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4ebed863-553b-3a53-80e2-f8dc01f358d5 | -12.7636 | -62.9036 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fbd4f5e7-619c-3b08-a3c6-36c791172521 | -12.7826 | -62.9025 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| edc94d35-ad48-3b06-ae5f-35a37e9a09ec | -12.7827 | -62.8832 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 40d4f60f-82d8-3ef4-86d2-1c8f2d725bda | -12.9245 | -51.2002 | 2024-10-01 03:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6ec5bdc7-4f28-3e29-9cf3-ce2d5c4577a1 | -12.8206 | -62.881 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 935f31e0-bc7a-321c-9409-c35e89780467 | -12.8397 | -62.8607 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a913f083-7b14-3f20-99a9-61a6b85e15f6 | -12.8588 | -62.8403 | 2024-10-01 03:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 908d6a0a-a74d-3a21-9ad1-b15756d0ec93 | -13.2112 | -51.2287 | 2024-10-01 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c1e79f01-c617-3e5b-931a-d95b68b343b6 | -13.2116 | -51.2073 | 2024-10-01 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 6b5e97da-0beb-3ba1-8701-c34f4523d012 | -13.2304 | -51.2262 | 2024-10-01 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2dc1f120-3428-311b-bc74-8aa70a173c9a | -13.2308 | -51.2048 | 2024-10-01 03:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 38a6a820-524f-3a43-9513-8bde8ea35b7f | -14.7402 | -48.7721 | 2024-10-01 03:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d149ba57-c3cb-335b-a229-556fa1e33039 | -14.7406 | -48.7498 | 2024-10-01 03:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 74892ad2-5652-3f75-b8e5-5cc178c41738 | -15.9127 | -57.1733 | 2024-10-01 03:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 5d1168c2-a575-3e00-8152-d0b52f81b54b | -16.474 | -57.3553 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 062e02de-e0b9-31be-8147-9a312a60a504 | -16.4743 | -57.3349 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| a79e2aaf-6019-3e67-94c2-57c6033d5033 | -16.4935 | -57.3531 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 4b4a4e4f-cd08-3262-98a7-7415c6b773bf | -16.4939 | -57.3327 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 67b34203-ac72-3226-b031-cbf13e737c85 | -16.5131 | -57.3509 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 20243696-4b99-3df5-bc28-91e3f83d15fa | -16.5134 | -57.3305 | 2024-10-01 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 3bfec3ec-8136-3fea-b431-7c32bccaf9d1 | -16.6126 | -56.0043 | 2024-10-01 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| ac5a94ef-b56b-30ce-9248-e40c0fde5df4 | -16.613 | -55.9836 | 2024-10-01 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 6532a539-ad80-3ab0-8053-b8ea174968d2 | -16.6133 | -55.9628 | 2024-10-01 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| fd516d9c-afaf-3554-b0fb-dd901e11f742 | -16.6136 | -55.9421 | 2024-10-01 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| af0e87fd-95e9-32ff-b27d-a1519c0150af | -16.6329 | -55.9604 | 2024-10-01 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 7b9189a1-bbb2-3f81-8891-7862f6c8b5cb | -16.6455 | -55.2117 | 2024-10-01 03:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| b0502851-c454-3c87-a52c-818cde270dc5 | -16.6459 | -55.1908 | 2024-10-01 03:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 96f58d50-aabc-3b8e-b0bf-e42af3a45e0b | -16.6505 | -57.2944 | 2024-10-01 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| a93252e4-7471-3af7-9d8d-0853e505086e | -16.6508 | -57.2739 | 2024-10-01 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| d0e97311-7e69-3221-9f7c-78b65cb044ee | -16.6512 | -57.2535 | 2024-10-01 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 1bb86916-0107-3627-a010-212251581997 | -16.6701 | -57.2922 | 2024-10-01 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| a99422e1-4374-3032-8693-dd6f2dbfaa1d | -18.6973 | -57.333 | 2024-10-01 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| a41e7100-99f2-3e57-a722-abeef3b9e5ae | -18.6977 | -57.3123 | 2024-10-01 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 860e3d49-23d5-3143-8db2-6c4825eef836 | -18.7176 | -57.3097 | 2024-10-01 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 6f7dc61c-cf05-303c-af0c-1e3c18f75c6e | -19.1329 | -57.4628 | 2024-10-01 03:36:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 4745f4fc-50c6-32b5-acce-2841b7357096 | -19.6646 | -48.7843 | 2024-10-01 03:36:55 | GOES-16 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 8007f088-55b3-3b1c-add8-b60b79f6c565 | -19.6849 | -48.78 | 2024-10-01 03:36:55 | GOES-16 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3b21a3d2-2f34-3894-aacb-560d78d3862d | -22.3498 | -49.3293 | 2024-10-01 03:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 043996c6-e8c0-3abd-a637-1ba105e3f5b6 | -22.37 | -49.3477 | 2024-10-01 03:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.4 |
| 059a388b-3760-3edc-85fb-16d850b8be7f | -22.3707 | -49.3244 | 2024-10-01 03:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 308.6 |
| 03f813f2-3407-3dda-b1dc-9947fdeba3fb | -22.3713 | -49.3011 | 2024-10-01 03:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| dcadb9a9-3280-3f81-83dc-d88674d6033c | -22.3916 | -49.3194 | 2024-10-01 03:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |


[Clique aqui para ver as próximas entradas](README42.md)
