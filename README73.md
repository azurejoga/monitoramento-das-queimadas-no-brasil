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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 128be9c3-7944-3100-965a-2343bc051ecd | -12.97699 | -54.77233 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bb00b28-9e84-30a3-abd0-543adf0159eb | -12.99509 | -48.06911 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ff2c54-c9d1-3bd1-8a7b-c0eecf17052a | -15.30179 | -52.76102 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28550ef3-1a6d-38c2-bb4c-42f9454f10b6 | -13.45691 | -46.93694 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2875821f-aabe-3a24-90dd-f5526020d375 | -12.95817 | -48.06553 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9434ac4d-533a-3cc2-b42d-013bb8926ed5 | -15.23757 | -48.06278 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 707f48e8-c24e-35d5-aee2-7444791132ea | -11.67387 | -52.16604 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c3d927-034c-30ef-a17d-e066d8ebb400 | -15.73769 | -53.6376 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8321fd53-1898-38eb-ba08-4486b8b50185 | -14.57433 | -54.56019 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be8f94c6-dd7e-39b2-b104-69f51cf36e37 | -12.90431 | -56.93675 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb5d5f4c-261e-314a-abd8-7df05af6089b | -14.81203 | -48.22214 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81607757-8104-3632-a371-c5ba662eef06 | -13.75276 | -46.94421 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eea8692-04b4-3ac9-b6a3-e0934f7344ed | -14.20521 | -48.08851 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90677aa3-380e-34fe-80af-49992d12e63e | -11.94797 | -51.3489 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a09ca504-55aa-30da-8107-5a2834b012af | -11.58091 | -52.15968 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 919ce1cc-414a-3f8b-a975-d806211d0666 | -10.57988 | -55.4131 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23ad442f-c32d-3b0f-aceb-25ac4f6b92ca | -13.4482 | -46.93066 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0730eb9-20a7-3c08-9e20-a86b517277fb | -12.91016 | -57.00097 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14a147eb-a7fd-3d52-b661-80f52d46b43b | -15.40785 | -55.93728 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44b4019c-9f22-3b61-b50d-9c202109b1ad | -14.57895 | -53.02615 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bf627cb-5ab5-343d-a0b7-db2c1186ec2c | -17.17092 | -46.25528 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 977bcbb1-76d4-300e-b632-c56ee58121f3 | -15.00996 | -50.04774 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd3292a0-1bfc-3b5f-a842-0514a7bf6345 | -11.85613 | -52.43519 | 2025-09-04 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50e7f2ba-359c-376d-a4ac-9f184bd09b60 | -11.59565 | -52.15444 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc82ad6c-249d-34c6-8824-a8d6977e432c | -12.49228 | -53.84444 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7571da49-0b51-3348-948f-0b41cd03b9dd | -12.96973 | -54.77478 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6adb126b-f09e-36a3-8694-5b6bdc06ac09 | -12.23753 | -50.14668 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd5e6cc9-abf2-34d7-acb6-5998502f642d | -14.98772 | -59.38756 | 2025-09-04 04:55:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a1fabdc-483e-3281-9c38-ca04fe20b4ee | -12.49877 | -48.0664 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fd9afad-7c4c-32f3-a40f-dbb10181ad4a | -15.11064 | -58.87379 | 2025-09-04 04:55:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c279dcc2-e41a-343f-8dcf-40d82c52cba2 | -15.16637 | -52.35266 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ec4f10e-0715-3624-aa20-8da3ca63f988 | -11.59621 | -52.15073 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 773b19c7-0437-3c18-acf9-a416c168040c | -11.67176 | -57.35137 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ea8ce7d9-a2ec-34fe-bcb2-672fb5f5190a | -15.05083 | -50.03941 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e6a6b5-9837-37aa-b257-5af99301a523 | -13.10974 | -57.1158 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a33a31f-92a8-3447-a694-29eef5d9104b | -15.98095 | -55.9596 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 73e42c0c-f86b-3362-9ed0-9dbbeaf8c8d8 | -11.72992 | -47.75053 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f2921c9-db09-3d50-a7ea-e9de8799ac2e | -15.61022 | -52.88953 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1a4df9-9ef5-3d7b-8639-a91ae1c52026 | -14.77889 | -48.13281 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27db2d1e-6c0c-3932-9250-9795f9f2642d | -11.62854 | -52.18981 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d61f1c9-8962-3993-b952-180b1063d7d5 | -15.03175 | -50.09078 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b657d71e-b6df-3aac-a3e2-583fdd8cb94f | -10.97511 | -49.75324 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a5c68e6-5fe3-3f02-af52-91565829faec | -11.64562 | -52.21455 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82efbd76-14d0-3bfc-b735-12971637226a | -16.54787 | -55.10636 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46fde30d-d9b4-3498-be01-01e45873448c | -11.57801 | -52.11 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cc6ad57-77ce-3c9e-aecc-0b7dbb226232 | -17.15774 | -46.22181 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd017580-f936-3874-95f4-bae5c8065115 | -12.49825 | -48.07024 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3469e4f5-6076-33d1-af73-6adf443c4a66 | -14.78408 | -48.1314 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f6230b9-a479-37fb-8f83-c659e4db290e | -15.1578 | -52.37651 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90c8c10a-6504-3240-8210-f478addcc228 | -13.44551 | -46.93691 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f55deb-728d-3fe1-b465-308f1e95b8a8 | -11.58198 | -52.10683 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 379509a1-1c29-34a5-a49e-cc9649eba6f6 | -12.9111 | -57.00632 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1dd40e16-96b8-3517-a5e7-0aff136b5b58 | -15.59652 | -52.88736 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fbae0bf-5682-3b09-8d48-6c4171fbdbb1 | -15.98468 | -55.97925 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d447da59-653f-34b6-9b35-8b0bf650bb44 | -13.00214 | -48.08186 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 450fe804-ca6e-3d46-a712-357301f761b3 | -14.59373 | -48.02172 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 948cbe2f-4a59-3b74-9392-7bd6829d5371 | -17.05407 | -46.44457 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37ac6175-1df3-32ae-b679-aa6a2fd8d947 | -12.46671 | -48.0786 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11b0c4b0-d61f-325d-b90b-53bfcb5d2de9 | -12.97088 | -54.76764 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cf3629a-1708-3459-85bc-1ff15312f1de | -14.598 | -48.01514 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96068cc9-8dd4-3119-84e0-0873a2afa5e1 | -15.00742 | -50.0373 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 135c61be-1df7-3ff0-a074-bc9b635245fb | -11.54051 | -54.49188 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 110f2260-91f4-342a-9c47-f089a4b305cf | -14.3905 | -53.0722 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 888c8ca3-a4ae-36cc-803d-6bba448a6115 | -15.0402 | -48.11119 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43c40f80-4df8-345e-8010-3486ddba8d19 | -14.78328 | -48.13337 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 573856b6-8286-352d-885a-bca30f17e7ce | -11.73244 | -47.74871 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5e1bc6a-dfdd-34d0-ac25-256de52af86e | -12.89865 | -56.94859 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adf8ee69-65a5-3c7b-80ce-0d68a931721c | -11.59893 | -47.78149 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2c4f399-ed78-39d5-ad92-08b33f0bb715 | -15.60679 | -52.889 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce78f5cf-e286-3b66-986d-62b7821a0180 | -12.87098 | -48.01822 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bc3fd27f-73e7-3b42-9d4b-62a0ca7e44ce | -15.53607 | -48.34673 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77101c07-245f-349d-812a-7041a4570738 | -15.41062 | -55.9416 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57b819b8-b957-34d6-8e5a-6fa3f566c26a | -13.53391 | -47.02524 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a57f77aa-8a2c-33a9-ad4d-ba6a02d0f34d | -11.58922 | -47.78841 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd33d3da-8683-3311-80c2-21426eb81f4b | -12.48341 | -53.83574 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8883632-e229-3243-9ca0-76eb9e225c57 | -14.56357 | -48.04626 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecbd3f9b-6dc4-3bfd-ba92-a4c46de5990b | -15.55016 | -48.41002 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4754a2c-d889-3502-b073-91404f28e980 | -10.49912 | -50.44333 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6539f513-342d-354b-8790-9e3f66fe0f51 | -10.49382 | -53.65105 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fb7d50b-825e-3ba6-9f9c-ad3d14260fe2 | -11.58828 | -52.15707 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3467292-06e8-381b-b571-17ff192da8ff | -11.63653 | -52.20559 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46fdc467-349c-38a9-bf5a-b2cb897745dd | -11.61607 | -52.18029 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ba430ee-e42d-359c-bec6-5df14e8728b5 | -12.9725 | -54.77892 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe8e1897-ec10-3945-b8dc-b665c17bcfe5 | -12.97411 | -54.79021 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49345b12-1854-3a1a-8eba-d2eab50e3377 | -10.09832 | -54.76965 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e6995d4-74e9-3995-8d69-2409eacb7f06 | -12.8929 | -56.93907 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24dd23b0-dc9e-366b-b144-6ff4f55dbb01 | -12.60793 | -56.99438 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 35853de8-f270-343d-a12b-15557e1861e3 | -14.58346 | -53.01931 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7c5e541-89e4-3dd5-9f32-cc6f8755b2cb | -11.68298 | -52.19772 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9613162-0d49-3677-a264-f13113893817 | -11.86385 | -51.50484 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c138fdef-700d-350c-bf03-dcbc7e216ece | -15.73435 | -53.68224 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93f6978f-38c0-31c4-848f-4ba59257f860 | -15.03467 | -50.04133 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49000040-7a35-3d25-8ec9-9e1e1b1aa2e4 | -11.61721 | -52.1729 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f892069-dae1-36e3-98f3-65ac4f4d4077 | -11.68183 | -52.1824 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e81bb4-1360-3410-917e-1badb069b229 | -11.85216 | -51.43898 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e411e384-93c5-340f-b8a7-d773e3cc71a5 | -11.67727 | -52.16657 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a2969c-777d-3a02-8fbf-2537d0a93c77 | -10.11288 | -54.78706 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e446aa3b-e00c-3448-9b34-5576a6db62f2 | -14.82626 | -48.21511 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ef1c64f-d5aa-323f-b52d-502fe6008f30 | -11.20362 | -55.02041 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31173b9-a436-3ad5-9dc8-9c2e05226c98 | -11.2082 | -55.07757 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README74.md)
