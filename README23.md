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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa0df801-1d9b-3a49-950f-9b883963fec3 | -15.03528 | -48.11174 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c04a504-360a-354b-96e6-5c5faccfc121 | -16.31046 | -45.70586 | 2025-09-04 03:38:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2685576d-6f77-3cfb-8e63-20ddb8261d7b | -15.04655 | -50.06405 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da3e29fa-ec2d-3f99-8956-bc38c0fb1ae1 | -20.0942 | -44.12972 | 2025-09-04 03:38:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a3f8fb2d-e5a1-3315-bf99-67f36c04f6e5 | -19.64005 | -43.98203 | 2025-09-04 03:38:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 359c5a75-8256-3bba-8e2d-274f904560b4 | -17.17245 | -46.25888 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9f78c278-c8a4-3a8a-a6ba-3cc5d60f8a6b | -13.85479 | -47.98436 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a4f52e8-becb-3b12-8da8-ede2db35e8a0 | -15.53055 | -48.3443 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b28ccb6-a0a7-38ed-8da0-995378885a25 | -13.34532 | -46.83135 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd89a162-628d-3e97-ab3a-c1e60efb119a | -14.55624 | -48.07673 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f269f3-4241-32a6-b634-0512d2426761 | -17.17239 | -46.23138 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a5acde5-45c4-3cce-9d58-a36a8c23ca29 | -14.53706 | -48.07233 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 358d4b40-5782-378f-b96c-107f13206267 | -19.2222 | -44.48211 | 2025-09-04 03:38:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddc938ea-2f8e-363a-b1e7-4646bd9dfa1f | -12.46659 | -48.08239 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75477084-c8e6-358c-ab28-33863d65964b | -12.85283 | -42.96904 | 2025-09-04 03:38:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ed4c18ed-c58a-3be8-92fb-bb00862c9d94 | -14.20401 | -48.08443 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dbd6251-9a30-3233-8a19-ecaa34941677 | -14.28328 | -45.22435 | 2025-09-04 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21b4eb68-f610-3352-a891-1ec2c575528a | -16.30339 | -45.70475 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce4a3bc4-e750-3993-b605-601dfb380c2d | -12.00459 | -46.74545 | 2025-09-04 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04e4dbb-6ccd-38d8-a6db-1983415b7fb4 | -16.46035 | -49.51812 | 2025-09-04 03:38:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14c80cac-587b-33a6-b1eb-b40fe764b104 | -14.81396 | -48.22728 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f68237c-9a7f-3f0a-b4cd-f385bb5cc354 | -20.25026 | -42.02152 | 2025-09-04 03:38:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a86a166-d4b8-3fbc-b4cb-7d4f081de1f7 | -15.03771 | -50.08472 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 997042fa-8bdf-3952-8f22-f91e78c9ce33 | -20.57008 | -42.238 | 2025-09-04 03:38:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1d384435-6e6b-3a73-9bbc-fc6c173be0fb | -22.6567 | -43.6825 | 2025-09-04 03:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 6bcf0ae1-9000-358c-b5a3-a409eb3e12fe | -17.1888 | -46.261 | 2025-09-04 03:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3d4be425-1a0d-3441-a5d8-e778c581c9cb | -12.9006 | -56.9488 | 2025-09-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bd025468-6710-3da6-8bd3-65f5e60502d5 | -6.7649 | -63.1292 | 2025-09-04 03:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 46d4432b-3f28-325d-9deb-b414f545a6d7 | -6.7504 | -58.7268 | 2025-09-04 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| bd4457db-3517-3721-beed-c88ed31be565 | -6.7318 | -58.7469 | 2025-09-04 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 94e9e27f-faff-3ba2-873f-12a1219051b0 | -12.9009 | -56.9287 | 2025-09-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 68d189f1-b590-3fce-a33f-8583bfbc867e | -4.9951 | -56.256 | 2025-09-04 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 6234d0eb-54c7-36d0-b5ca-cfb8d61f3ec9 | -6.6796 | -48.4049 | 2025-09-04 03:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 206e97bb-7eef-3d32-b10e-b033e9ddcb04 | -6.7503 | -58.7462 | 2025-09-04 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e7bfc88b-3140-3375-8b5d-5bf24e1db440 | -6.7319 | -58.7276 | 2025-09-04 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7ab9389b-de6a-3593-81f5-57d55db5d832 | -2.9619 | -49.365 | 2025-09-04 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f11f6642-63fb-3e08-9102-6271f4af9041 | -22.64696 | -43.6859 | 2025-09-04 03:40:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 06887f30-738e-3e0c-aae3-d6f34a83ff5f | -23.51326 | -47.16847 | 2025-09-04 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 629ec505-6a5e-38d3-91f9-f9e55f72085a | -23.4254 | -47.05532 | 2025-09-04 03:40:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3e10f7a-5648-3d28-bbac-f913c80ae5f1 | -22.54483 | -43.56163 | 2025-09-04 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 241d5564-5214-38aa-b0d5-b7cf1d022d81 | -21.33767 | -45.64313 | 2025-09-04 03:40:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 59e3641d-69f9-3340-a79d-ab6948afe7ee | -23.40084 | -46.84123 | 2025-09-04 03:40:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ad97adab-5a35-34ac-891e-c86139538d98 | -22.77626 | -42.8947 | 2025-09-04 03:40:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6b243a79-914b-3179-a165-7a5796414472 | -21.13713 | -43.77032 | 2025-09-04 03:40:00 | NOAA-20 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af115c35-1896-384b-8f4f-7ea32ae1ad48 | -23.76901 | -47.45043 | 2025-09-04 03:40:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b700487-e728-355b-b7ff-0f775ac38e5c | -19.68068 | -49.37173 | 2025-09-04 03:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bee12ba-cb3f-3803-97ce-7355c5d30389 | -22.26332 | -49.55752 | 2025-09-04 03:40:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5583564e-ee4e-39a1-999f-741715272b7d | -23.31109 | -48.81448 | 2025-09-04 03:40:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a935e828-f9c1-3c5b-8f0a-fcf672add623 | -23.36554 | -47.17205 | 2025-09-04 03:40:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37247499-4656-30b6-b80f-4e8d89c92294 | -22.27975 | -47.63508 | 2025-09-04 03:40:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf93976c-a50e-3bd8-9fff-ab5204846e93 | -21.4779 | -46.7619 | 2025-09-04 03:40:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5bd6170d-6b81-3771-9e98-821dbb92da64 | -20.2892 | -46.71003 | 2025-09-04 03:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 602a8e40-b2ef-3200-95e9-779117028902 | -20.29404 | -46.71345 | 2025-09-04 03:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ed8c5142-850f-375f-ab70-6748edaa2fb9 | -20.1663 | -46.59491 | 2025-09-04 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ced341a-e551-376c-9b79-876cd0e46a7d | -22.65121 | -43.68661 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e51ec160-abe0-35f8-9523-4585dde7dac3 | -19.71467 | -49.14069 | 2025-09-04 03:40:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 678b3b87-9746-3904-9a92-ef3c6d56f5e5 | -22.54916 | -43.56179 | 2025-09-04 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6a8280e5-a80a-38ce-bc1c-a24c0fd0ddac | -21.47863 | -46.7585 | 2025-09-04 03:40:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6e7b8bcd-cbf4-33a0-a4a9-69ee51f275a1 | -19.68329 | -49.36049 | 2025-09-04 03:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1421cd21-1dd4-31d7-8d12-51922fafdfe7 | -22.40208 | -45.802 | 2025-09-04 03:40:00 | NOAA-20 | CONCEIÇÃO DOS OUROS | MINAS GERAIS | Brasil | 3117801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96ffd5dc-592b-31c2-a36a-74b2799e1bcc | -21.5586 | -43.98592 | 2025-09-04 03:40:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a611ef6-7722-380f-91ca-e215c955e555 | -19.68204 | -49.36587 | 2025-09-04 03:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5e44f9d-70a2-38e4-bcad-c39e70d68ca4 | -22.65887 | -43.69224 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| dcfcda4f-ee93-37b5-8def-a9adaf46b82f | -23.00767 | -47.08601 | 2025-09-04 03:40:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 312f07c5-d119-337c-bbaa-e67f1cedda0d | -23.50958 | -47.16871 | 2025-09-04 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2c9fc216-c901-30ac-bddc-77510c7a8004 | -22.54389 | -43.56639 | 2025-09-04 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a98db147-f9fa-3fa9-b175-6e0bda870dee | -23.51252 | -47.17186 | 2025-09-04 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d000250c-e6aa-3fa6-a7e8-657a427f3885 | -23.42463 | -47.05875 | 2025-09-04 03:40:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 618f3acd-7eae-3b66-8dff-b518fd37d1c3 | -23.76875 | -47.45049 | 2025-09-04 03:40:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dcfb24e5-9a45-36ad-89ed-1075a784fd68 | -22.33742 | -49.89039 | 2025-09-04 03:40:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2a8a596-9bc0-3884-a079-e3edc3213b27 | -19.71346 | -49.14586 | 2025-09-04 03:40:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0ab6f614-bced-3337-bd6a-77c9b4e67383 | -23.4227 | -47.05801 | 2025-09-04 03:40:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0ed73eb-24ad-3647-a10a-06a19911fce7 | -23.36041 | -47.17084 | 2025-09-04 03:40:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4e11c98-3253-3ac4-9abf-0170fb6cd119 | -20.10028 | -50.01474 | 2025-09-04 03:40:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8ff1f600-4253-3c08-b8ca-87a7c34586ed | -22.46123 | -47.54781 | 2025-09-04 03:40:00 | NOAA-20 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fb9ae2d1-5018-3e65-b74b-47ffb1f99bc5 | -23.39521 | -46.84273 | 2025-09-04 03:40:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 01633035-93fa-373f-8647-efca5ddd0383 | -22.33872 | -49.88501 | 2025-09-04 03:40:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3eaaed03-0665-385a-ba75-c3c8ae9d6955 | -22.8168 | -47.72679 | 2025-09-04 03:40:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9ec07db-aab4-3083-bd27-b0d817fcce24 | -19.71956 | -49.14775 | 2025-09-04 03:40:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2c8b8381-09e0-3317-b883-81547e7fb348 | -22.65546 | -43.6873 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| d14f8237-c3ac-3049-95ea-133fa2ce55a1 | -20.29324 | -46.71719 | 2025-09-04 03:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2fa93b2d-1d91-34ed-afb3-2263e5e3a100 | -23.51469 | -47.16993 | 2025-09-04 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7387f3f-3894-3005-8d20-4fe9982ddbc3 | -22.66315 | -43.69283 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 92178558-754a-36a0-a4ec-b754757b5973 | -21.34047 | -45.64449 | 2025-09-04 03:40:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 718b690d-dc28-3fb5-996b-bcee2109cc2b | -20.28836 | -46.71395 | 2025-09-04 03:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bac87e24-405a-3925-bb26-6213b85c66f3 | -23.42344 | -47.05461 | 2025-09-04 03:40:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ba29ddb-0794-346f-97eb-0ead01c7fb61 | -20.16007 | -46.59806 | 2025-09-04 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cec9d0ea-9533-392c-bc28-466eefc7b86a | -19.5699 | -49.43863 | 2025-09-04 03:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5121ae7-de58-3697-b57a-6432987933da | -22.26212 | -49.56261 | 2025-09-04 03:40:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3caf3a8a-16b6-3e9e-9d73-71f1cb245de3 | -22.65973 | -43.68787 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 1907e36e-e06e-395f-9d11-6dd69336ee4d | -20.29243 | -46.72095 | 2025-09-04 03:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d51f6208-7ad1-3680-9b1c-b48530983944 | -22.81599 | -47.73045 | 2025-09-04 03:40:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 317b2d80-1e45-3ca7-b0a3-f06c49f159c0 | -23.40016 | -46.84431 | 2025-09-04 03:40:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2587a922-3d6a-3534-9095-6276adf08643 | -22.91551 | -42.42348 | 2025-09-04 03:40:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6274efa7-111b-3535-b3b9-d370a7154ca3 | -22.65459 | -43.69171 | 2025-09-04 03:40:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 4b75fb12-dfd1-3d06-8dcd-b2a39f896cfd | -20.0952 | -50.00735 | 2025-09-04 03:40:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6dc54b8a-942a-301c-80cf-3ad25268faed | -20.16085 | -46.59449 | 2025-09-04 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5aa3e1f-f463-3685-a646-bb61656c07bb | -22.27354 | -47.63748 | 2025-09-04 03:40:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33fe90bd-9136-3d42-a78f-0e176f5fa13b | -20.10163 | -50.00901 | 2025-09-04 03:40:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b5d150f-becd-3cd5-b8ef-6653872e182d | -23.63141 | -46.8358 | 2025-09-04 03:40:00 | NOAA-20 | EMBU DAS ARTES | SÃO PAULO | Brasil | 3515004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
