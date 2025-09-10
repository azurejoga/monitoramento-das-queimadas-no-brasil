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
| 75d51e94-588a-3bbf-a6af-f2f6d748b77e | -18.01932 | -47.14092 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 65815046-67df-3cd2-8260-47e4add2a96c | -19.29396 | -47.98904 | 2025-09-10 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 02c9e666-b614-3460-83e1-9d13dee2d2fd | -15.96058 | -49.62341 | 2025-09-10 04:44:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 625401f3-f624-3a4c-8c20-fac470ab3bce | -19.91835 | -46.15387 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 626f5845-3928-3e06-b108-ee18d37b6ba5 | -15.51102 | -52.76773 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c5d6cd4-0eb2-3cdc-9850-18ae278931fa | -15.95714 | -49.62284 | 2025-09-10 04:44:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb6b7331-f3ca-3ac1-9acf-0df859a5e877 | -17.39798 | -49.30681 | 2025-09-10 04:44:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4600cb4b-d7ff-377b-8691-666e3b67223a | -18.02329 | -47.14164 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a1068d14-c801-3eaa-862f-6154aae01792 | -13.79276 | -46.28959 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6df86f50-765c-31c2-b998-73482534411c | -12.42277 | -47.81256 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf2d00ed-3b95-39ab-9a1b-4ad26b10abeb | -12.05155 | -51.04689 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88a6f69c-c77c-3e41-9fe0-5194de3b0306 | -18.43579 | -45.93533 | 2025-09-10 04:44:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73615a78-283b-3aed-8c14-c3738f197fb5 | -15.95006 | -50.22604 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4b61c7a-83d7-361e-99aa-623a45579f8f | -16.12288 | -55.86119 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3630c175-9152-360d-97eb-56462c8f5ee4 | -14.92156 | -50.11428 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c92cd23-28d1-32e1-8c43-3ade2f8cc670 | -11.2143 | -54.98947 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b12bd52-924a-3e21-b6d1-a8d326dd0593 | -14.4421 | -52.95746 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f95370c9-9aee-337f-9594-70b0c64d0e87 | -19.51896 | -45.01906 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6298742e-4e4f-3a68-bb2c-e82b0deb914f | -16.52698 | -55.11686 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5e411a70-e8b8-345e-9bba-b1ac55bd0476 | -16.53063 | -55.11749 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 837980b0-3b3e-3ca0-9f8c-a24db8484d8d | -13.97409 | -48.24034 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e905f3cd-f76e-3f3d-b2e9-e03254564c53 | -15.14285 | -52.3887 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a802f809-daeb-3c44-8462-0c5ed9348573 | -15.84694 | -52.27281 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3b98a16-a884-33ac-a5fd-bc69b518e884 | -15.95356 | -48.10954 | 2025-09-10 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f6e2669-92e8-3b3b-a8a9-e524c1507c1a | -16.27244 | -49.16623 | 2025-09-10 04:44:00 | NPP-375D | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f21e7851-4870-3811-b79d-f5d25a32b6fe | -13.02485 | -48.01887 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4014e676-2457-32d5-bb05-ed41cff72952 | -15.25613 | -53.77267 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729f939c-5a44-3f18-b5b9-2f504e2ec2f1 | -16.52234 | -55.14303 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 93870d02-d0ca-3fea-b3c1-2d31af638791 | -16.05534 | -49.96683 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44ab38e-0163-33d2-9d5d-6442121a61e0 | -15.01455 | -48.02881 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5633820-b43f-363d-81a2-9888e228d1c4 | -16.34488 | -52.94801 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ef7cf13-9a7d-3d3c-8be6-cb42b83c8fb4 | -11.60171 | -52.20889 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4d1d44b-c225-3225-94d5-74f82c440140 | -17.2481 | -46.08186 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd6f17ac-1d89-3e07-a2b2-25b136a16865 | -14.93207 | -55.94013 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c8e6fa6-c158-30e1-8621-02253f2417c7 | -12.99208 | -48.03273 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 931dca5b-109e-3fbb-9a45-0c24ce788599 | -12.05268 | -51.03981 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ee266b04-6784-30f6-bdc5-de755fbcd5a4 | -19.17621 | -43.06343 | 2025-09-10 04:44:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bc268339-07eb-3676-88a9-2f1b1dacf610 | -15.81209 | -52.24433 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc800199-fdb6-3a5b-b61c-235536a35a0a | -12.01937 | -51.03434 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d273df31-2439-3e2b-a306-10501c47d5ea | -15.51439 | -52.76833 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f4e9f02-c409-3715-a306-e7cfe3f53d7b | -12.60854 | -56.96703 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77254299-0360-393c-92d0-d56ad6a1a475 | -15.15046 | -44.02723 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6c2a727-207f-3b80-a14a-69ec89870657 | -11.60132 | -52.21201 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49fa3cd4-d985-3d3a-bf04-f585ce433e23 | -15.95416 | -48.1053 | 2025-09-10 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 976033fb-5862-3f93-a32c-95de72fb9d41 | -15.10729 | -50.08622 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eb8f295c-307a-34e8-8915-a6615df78a65 | -19.74954 | -45.71888 | 2025-09-10 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49725f52-9d3d-3fe8-afa2-3b7f270d84b1 | -14.89963 | -50.12201 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 42df766b-c3f4-3d19-9fe1-7b5d419b0f05 | -19.4891 | -45.30208 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f806acac-dcde-3825-925a-9c2f48b0c2e9 | -16.67427 | -48.52289 | 2025-09-10 04:44:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41544dcf-8d3e-377d-8c58-79fd99e1bbb4 | -17.56236 | -44.53673 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c6ae621-54fc-3c87-a382-306c0c2d5043 | -15.52927 | -48.37646 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7fadd69-e3ff-3f54-b7aa-b700b45caca7 | -17.57569 | -51.062 | 2025-09-10 04:44:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e6fa35-9b31-3998-8031-4bedcb186ef0 | -12.06651 | -51.06025 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 98127186-3f05-3adc-8484-27c953d20786 | -15.81135 | -52.27039 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9154783-e231-39ef-ba45-b17ac9388fd2 | -13.96511 | -48.22655 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2f43053-ebb7-3d8b-91b7-1b3ba63d48ce | -16.62834 | -49.77208 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2116156-5f79-31f6-a806-b9cec2bd4ab3 | -13.89678 | -53.97153 | 2025-09-10 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1d9ed6c-0c63-3dab-a666-92eec163a6bc | -16.48083 | -51.97532 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00fb6af8-c02c-3e4b-95ee-ac62d842ca76 | -14.92514 | -55.93391 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6baa6b1-8640-36d7-89e3-36853954d982 | -12.99331 | -48.02441 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a307059-7dd5-3fbe-b2cf-74b2a4c8269f | -15.39638 | -52.9156 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8132116c-ddb6-3854-bcc0-359a568eaf09 | -19.7747 | -45.78975 | 2025-09-10 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4120697c-70c7-383a-8d08-69bdeeb654b3 | -14.92606 | -50.10744 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95758491-f157-33ff-a432-6ce3d2e67b8e | -15.28263 | -53.78562 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a08223f-eee3-3fca-8ae1-412cbad2c7e9 | -15.13776 | -52.39882 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 017c7daa-a8ff-3d54-be1a-44fb10ce81fb | -19.64277 | -45.05014 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe807dae-8b35-3264-b860-808c62d5cf2d | -13.18286 | -47.25863 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a998abb-f2d1-3a34-90f5-58948f74fa5a | -15.81267 | -52.2407 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 593d14ed-1bed-3273-b185-4d63ab77317d | -15.01332 | -48.03738 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf53979a-63e5-3984-af78-936731014fe2 | -13.79606 | -46.29513 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7d8fdb17-d456-3f62-94c9-6c0f35811a30 | -12.75772 | -53.99384 | 2025-09-10 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1be88cd8-8e1b-3684-86e4-aacea68430bc | -14.91986 | -50.10272 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5daae28-0aae-3ca3-8eb6-b2ccd220f8d8 | -12.92898 | -54.75605 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bc8be989-cbdd-3700-adbb-b3947aee41f7 | -16.57678 | -49.22201 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78dabbf1-401d-34c9-84d0-15d2c07edf80 | -14.35584 | -47.31143 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9f252bf-939b-3922-9b6b-2303a51b799b | -14.3877 | -47.33075 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2ef783e-e60b-38e1-9635-298134e45dd6 | -18.02726 | -47.14241 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c975bbc8-4ab0-33f2-bf44-af6181288b7f | -13.01826 | -48.01388 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a0b351d-0aad-3228-a02a-1182e86eae2f | -16.40709 | -50.88759 | 2025-09-10 04:44:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75829e93-956f-3ee3-b3ca-9095118e07f0 | -12.47945 | -53.8278 | 2025-09-10 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 078835b1-1f99-3af4-a745-05f8123c68cc | -18.34597 | -49.3359 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 697bd292-95fe-3521-8533-37a4ff12a721 | -11.94692 | -51.04442 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 743b87a4-c8c2-384e-af52-39031775c72b | -12.92711 | -54.7889 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d52b34d6-27ce-314b-8e7e-5ae2ae2d3f1f | -18.13573 | -51.7286 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29e275b7-e6c3-3af4-9bee-788f360fd884 | -15.83505 | -48.96242 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e3174e4-08e2-3360-b88f-0874ab9ca3a5 | -13.18906 | -45.27804 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba804a7b-ed2b-39b1-9ed8-0d38bd5ab19f | -14.90412 | -50.11522 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63bec725-e474-30c3-af28-bff3a6957a35 | -18.30762 | -49.33175 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7320f558-6fa6-37e0-a07a-aee6237fd408 | -13.75085 | -49.09797 | 2025-09-10 04:44:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69b071da-0da1-334f-a1ab-94741a3f4643 | -16.8866 | -45.75794 | 2025-09-10 04:44:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 376465fa-5e6c-3134-afca-ca7598a13522 | -14.91426 | -50.11677 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82bd3c8e-33d5-3f3f-8fd8-0b0a0cf8b251 | -15.87802 | -52.20771 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a49859b-1fe1-302a-8a0d-1a5217774435 | -16.57672 | -49.73945 | 2025-09-10 04:44:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 690d76e2-41b1-3002-a568-5cf3799790a0 | -16.4558 | -51.98219 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0661aa11-42d3-37fb-be5c-84f8c3cc4c72 | -17.20063 | -50.15867 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d5f1fcf-df6c-30f8-a86d-d813341fc663 | -18.13354 | -51.72073 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b00be6c-f14f-32d1-ad5f-e1f39cf5ee50 | -15.69986 | -49.90039 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 023a0281-c3eb-3c83-8886-38789942b55d | -15.82274 | -52.23138 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23779d8b-4eb6-3fa0-8f46-fd5a457b90f1 | -20.21963 | -40.36039 | 2025-09-10 04:44:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31736438-c3bc-3e30-9b0a-6e4ac072c693 | -15.13659 | -52.40606 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |


[Clique aqui para ver as próximas entradas](README74.md)
