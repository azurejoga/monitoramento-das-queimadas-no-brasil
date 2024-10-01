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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea99adfd-5133-3d4d-8146-aedca58cb916 | -10.5746 | -48.0178 | 2024-10-01 13:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 2dab30d9-69bd-3d14-bd71-b3121dd1b84f | -10.6978 | -46.1514 | 2024-10-01 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| d2f0c726-5ff8-3368-b0dd-3d14fc200332 | -10.6794 | -46.1085 | 2024-10-01 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| e0c2d919-c5d2-34e2-b053-e00a2c741c25 | -11.1016 | -49.5922 | 2024-10-01 13:06:09 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 963dd93b-b7e5-30af-942f-a901c4e7e7fc | -11.258 | -45.6682 | 2024-10-01 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 598e0c9e-3120-3ab4-bb79-89cf1e31e897 | -11.158 | -49.6289 | 2024-10-01 13:06:09 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0389caf1-c800-39b0-8af6-af1a39fc33cb | -11.922 | -44.8829 | 2024-10-01 13:06:13 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 86d055a3-99b2-3fdf-a00e-924893f7c5ac | -11.9102 | -50.1663 | 2024-10-01 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ca4188b9-1e96-34ab-b0b7-2d6fd2a27162 | -12.1406 | -50.0524 | 2024-10-01 13:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 6c7f9caf-125a-3fca-be5c-e3ec65fbcfb9 | -12.21 | -50.4956 | 2024-10-01 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 474c8e70-e1cc-3faa-a797-e587fbb3f182 | -12.2103 | -50.4741 | 2024-10-01 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dd4732b4-749c-3fd1-bd35-954e57f84b88 | -12.1593 | -50.0717 | 2024-10-01 13:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 01d8c59b-bbb5-3974-90e3-f932415ab47f | -12.1402 | -50.074 | 2024-10-01 13:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6cecd566-9a48-3a76-95c9-56b83e5ef374 | -12.3934 | -50.9658 | 2024-10-01 13:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 56f78487-caf2-3ccf-844a-936446fbaaa3 | -12.9433 | -51.2192 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9e3defb2-949a-3e9c-b078-27099d7c4e1d | -12.9629 | -51.1955 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5889ae12-1b88-3128-a093-9c9f22b27f84 | -12.94 | -51.4327 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9f8e5a67-4990-3267-9295-a3325b575aec | -12.9803 | -51.3 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f76f4ac3-2081-3a12-bb18-02676b3b716d | -12.9437 | -51.1979 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 730d553f-6302-3a06-95ca-117698037dd2 | -12.8398 | -62.8414 | 2024-10-01 13:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| bb2b764a-8a1b-3c30-a667-aebfd6644ce8 | -12.8397 | -62.8607 | 2024-10-01 13:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 28e4d6e8-d4a3-3974-9792-2d22bf991a1c | -12.9625 | -51.2169 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| feeed0d3-08f2-3b15-b5c6-e8a33b78678b | -12.9807 | -51.2786 | 2024-10-01 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1ae4c9a2-bc79-352e-b717-53b6387b9e1e | -13.192 | -51.2311 | 2024-10-01 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 76de5c0a-8a03-3ee6-ae45-2cae53e1706c | -13.218 | -48.5797 | 2024-10-01 13:06:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e7908590-d2b7-3a06-87fd-cc7964d41e8b | -13.1924 | -51.2097 | 2024-10-01 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| b110a2bc-29e3-3889-8b55-d2fb72d57fd2 | -13.0375 | -51.3143 | 2024-10-01 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 69043c06-1ca6-3e40-94a3-f55c2f855b97 | -13.0183 | -51.3166 | 2024-10-01 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d9bb4a4c-e05b-3315-ad4c-4fd4b32b39c7 | -13.2112 | -51.2287 | 2024-10-01 13:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4c35d44c-49bb-3b33-8d56-1204b7f20883 | -13.558 | -51.1417 | 2024-10-01 13:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| cc091c6c-4552-3e63-bbce-f33f2c603f25 | -13.5576 | -51.1632 | 2024-10-01 13:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 70c3e8cf-d13a-3aa3-aa69-0dee25e85982 | -13.5765 | -51.1821 | 2024-10-01 13:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2c6db075-0803-389e-a0d0-10fc2a59005f | -14.7735 | -48.0757 | 2024-10-01 13:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 157.8 |
| ff30bb2d-1171-34b1-a7f5-093aa40efde5 | -14.754 | -48.0788 | 2024-10-01 13:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c36c1dcf-2c42-3832-87f6-b4a88c28e94f | -16.4536 | -57.4188 | 2024-10-01 13:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 362.1 |
| ad22d8a5-b06f-3892-9ec5-cafa9cc1f554 | -16.4743 | -57.3349 | 2024-10-01 13:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| f8a617c5-6260-36c3-9184-1ad6707fa053 | -16.474 | -57.3553 | 2024-10-01 13:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 5d31e8a7-0d38-36b2-b5e7-6600756e0876 | -16.4539 | -57.3984 | 2024-10-01 13:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.4 |
| 42a3e36f-282a-3dcf-81d7-090971b2ed15 | -16.7724 | -55.798 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 3c8d3114-abab-39ae-90e5-d8c60fde1c73 | -16.7528 | -55.8005 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 56692d02-0fdd-3814-ade3-530b5bda33eb | -16.6521 | -55.9787 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 4e6a5920-3c0f-3628-9ee4-751ce6468b14 | -16.6455 | -55.2117 | 2024-10-01 13:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 504ab9b9-e6be-3a9f-8749-0efcef869964 | -16.7728 | -55.7773 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 170.0 |
| d2062c43-c630-3cc8-91fa-f8dd761eae3a | -16.6259 | -55.2142 | 2024-10-01 13:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| fee35863-1d65-3662-9afc-6c86c07123b5 | -16.7532 | -55.7797 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| a18ef2f5-c4f6-3395-8852-e25db8afb4d9 | -16.6525 | -55.958 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 2c2812f7-fabd-318f-a05a-c2b1c2834fcd | -16.6528 | -55.9373 | 2024-10-01 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 57a36368-283e-3193-b104-198f8d8f8b1a | -16.6263 | -55.1934 | 2024-10-01 13:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| f1045fb3-f646-3ff2-b488-ee6ac2b1c37f | -16.8983 | -57.6949 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 6c6a60d4-ec5a-3a70-81ad-071d858283f3 | -16.7796 | -57.7898 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 9c6f81e6-8b86-3b3e-a658-a77f4099eb47 | -16.8784 | -57.7175 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 90ff233f-4e15-3cc2-8543-5ae437fb8f10 | -16.76 | -57.792 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| a1a32297-e2de-38e7-950e-53c0cd15ff6f | -16.8591 | -57.6993 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| ac7d7eb6-59a0-3429-a615-4c34a038e3e9 | -16.898 | -57.7153 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 38d9db5b-1b94-331c-b928-3c70a8522331 | -16.8787 | -57.6971 | 2024-10-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 222.2 |
| 100ddb91-ab76-3226-a62c-2e00c9f721f0 | -17.0805 | -56.1114 | 2024-10-01 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 81030ba6-c9b2-3ebb-a410-0eafc7423273 | -17.1381 | -56.1869 | 2024-10-01 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 65d0ae57-6922-3281-b4aa-1cb5f25a55b4 | -17.1377 | -56.2076 | 2024-10-01 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| e18190d8-37e8-35f1-b18b-54eb82bcd52b | -17.0802 | -56.1321 | 2024-10-01 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 17095d9d-2389-3c42-b2e7-25b2943cd601 | -17.197 | -57.3741 | 2024-10-01 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| ddafdf30-e581-38fd-a4d1-0ab6681601ad | -17.1767 | -56.2234 | 2024-10-01 13:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 152.7 |
| a3b58008-5a25-33f5-8400-446a601edb0a | -17.2167 | -57.3718 | 2024-10-01 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| d27ec82e-c6a9-34d3-9459-30e5b502df45 | -17.1964 | -56.2209 | 2024-10-01 13:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| ddaf3a53-3e64-3b27-b9e0-174883959491 | -17.157 | -56.2259 | 2024-10-01 13:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| bf1c5c55-186b-3300-b521-17a8962922bb | -18.5236 | -49.4241 | 2024-10-01 13:06:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 2bcc1728-6cbb-3543-9b89-583d8800dc5a | -18.7172 | -57.3305 | 2024-10-01 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 266f963b-ceec-3add-825b-b68f7d38c15c | -18.7176 | -57.3097 | 2024-10-01 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 2678dd5a-7bef-31e8-bed1-35642a056014 | -18.6977 | -57.3123 | 2024-10-01 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.9 |
| 9dc952d8-b49c-3137-bc27-896d2207e382 | -18.6973 | -57.333 | 2024-10-01 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| bb5703d0-2402-3690-8fe0-9cbfe63d359f | -19.7878 | -47.953 | 2024-10-01 13:06:56 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e73e040b-322d-3e90-bcee-b0dd1c36619d | -20.9359 | -49.1023 | 2024-10-01 13:07:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 262.6 |
| 12cb0135-a91c-31ac-b1de-16f24c4d4b42 | -20.9153 | -49.1069 | 2024-10-01 13:07:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.6 |
| 8adda681-7172-3feb-b0f1-a4b826d3d708 | -22.3713 | -49.3011 | 2024-10-01 13:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 249.6 |
| 0cb29753-fb64-39d9-a4a0-3b686b21ece2 | -22.3916 | -49.3194 | 2024-10-01 13:07:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.6 |
| 8867e5ff-41a7-34b6-bc3b-9ca83a6a05f5 | -22.37 | -49.3477 | 2024-10-01 13:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.1 |
| 1645a39b-a2b7-3d27-b11b-8716824da09a | -22.3498 | -49.3293 | 2024-10-01 13:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.5 |
| 5b12ea57-4fdd-32ed-8e9a-c5485eb1c57d | -22.3707 | -49.3244 | 2024-10-01 13:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 291.5 |
| 9934cc95-9864-3061-85f7-09e6d2778774 | -8.2364 | -44.8672 | 2024-10-01 13:15:52 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 171e7299-7481-3116-a5fd-d02ba22e2520 | -8.7612 | -45.1314 | 2024-10-01 13:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 718bc557-a1f1-3e31-9838-85b891e59787 | -10.052 | -50.2833 | 2024-10-01 13:16:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1749a04e-2ff9-36af-8dd5-6631148443d0 | -10.2314 | -46.8606 | 2024-10-01 13:16:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d03702f8-0a31-3c23-b34e-4f9222d8b853 | -10.4582 | -48.207 | 2024-10-01 13:16:05 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 956c4322-034c-3271-a40e-af839088cb33 | -10.6787 | -46.1538 | 2024-10-01 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f02998a4-873d-3a2a-a2fa-0e0ac4a4cb82 | -10.6978 | -46.1514 | 2024-10-01 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 991ba8ed-8731-3262-b039-da3b45fd0134 | -10.5746 | -48.0178 | 2024-10-01 13:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 281a67b1-c82e-39b0-84a4-95dc00d68ed3 | -10.5743 | -48.0399 | 2024-10-01 13:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 79f6047e-7b61-3c09-b050-d616bf625a26 | -10.5553 | -48.0421 | 2024-10-01 13:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 56d4ca80-a79a-37be-937f-f311f889d63d | -11.1016 | -49.5922 | 2024-10-01 13:16:09 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d256738b-b958-3a76-89ea-32706d61de12 | -11.258 | -45.6682 | 2024-10-01 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b1dbbe8d-3661-3d2b-a16d-4a4e168c9214 | -12.1593 | -50.0717 | 2024-10-01 13:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2b772532-a0bb-3117-b79c-6c175411b765 | -12.1406 | -50.0524 | 2024-10-01 13:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| da889774-ce76-301e-99c4-6c0807f37670 | -12.8398 | -62.8414 | 2024-10-01 13:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 9e0033c9-c21a-360c-b0a3-ec67de7e6ec6 | -12.8397 | -62.8607 | 2024-10-01 13:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 929b68f8-5669-3667-a3a1-14a8e6a93bcf | -12.9625 | -51.2169 | 2024-10-01 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 48183470-673e-3cb5-8dfe-976e078c7171 | -12.7636 | -62.9036 | 2024-10-01 13:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e5eb7627-a53b-36af-8830-4717385b4cb6 | -12.9433 | -51.2192 | 2024-10-01 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f2989503-3353-30c7-b324-24827fc10c02 | -12.9828 | -44.7155 | 2024-10-01 13:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ddfc56b7-f6b8-3512-9044-2cd3d71440e0 | -13.0375 | -51.3143 | 2024-10-01 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8ddf3661-64c1-365c-b233-2505b0b5c49f | -13.0183 | -51.3166 | 2024-10-01 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 428b352b-b7cb-341b-b9a4-cb522a7a9f91 | -13.192 | -51.2311 | 2024-10-01 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |


[Clique aqui para ver as próximas entradas](README167.md)
