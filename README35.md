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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcbd4560-acb0-3a9b-ac9e-9f513f08f37c | -11.80796 | -44.26783 | 2025-08-15 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9d0ecc-04ab-31eb-b277-fdc006d0866e | -12.67323 | -44.95006 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2882a69e-e00c-3244-b799-04fe49580bfb | -11.54185 | -47.25055 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 280c1ffe-73c4-3bb9-b172-537704ad11d2 | -12.49202 | -47.01239 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80bdff03-4750-355a-a201-790ad5894795 | -9.1718 | -59.66296 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 00ce7d88-0f43-3ef6-9b62-1752ccfd26af | -9.17867 | -59.67767 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30c1a7da-bec6-3050-a276-4d6e2140fc1f | -9.15309 | -59.66645 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07f6f5b9-4436-399c-b1a1-ef6a277e8a3d | -9.20998 | -59.65973 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6fcbfedf-5d0c-3ad3-ae0f-7698e53877d8 | -13.12531 | -57.16042 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26977921-1e54-3f41-8cfb-e6fbd681af6b | -17.3637 | -44.13986 | 2025-08-15 04:29:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f57f209a-392b-3e9c-a11a-2f0d6268b7f0 | -14.23495 | -44.5832 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9bf2d0a-b39c-3ed8-81ea-dfe4ba940ee9 | -14.79656 | -42.72339 | 2025-08-15 04:29:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 058772e7-9f43-33a4-931e-a26c94ae9950 | -12.58895 | -46.95137 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9fd3880c-e6e4-36ca-b12d-d777d89095c3 | -12.35494 | -49.90968 | 2025-08-15 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d2491a-7e56-3362-b500-fa9a12b024ee | -13.57408 | -46.96549 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9ee92de-2ba8-3f30-b152-17ed0b241b31 | -14.90511 | -45.18318 | 2025-08-15 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c27b40c-f4a4-3c81-affc-dc4f664e3720 | -9.1688 | -59.65733 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 08a44f9a-6d23-34ff-840c-7e6afb80936d | -10.35921 | -50.81238 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f84e6a11-000b-3901-af01-7eafee79688e | -9.49925 | -60.53678 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 67ab129b-9f96-3615-b93b-676131ba4a3a | -9.39612 | -60.54304 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60af53ca-8b9b-3b2f-9e91-95fa8456edd5 | -11.40834 | -58.54023 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0339414-58f5-3655-8096-9b7b536062d2 | -11.7757 | -47.39631 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cbbdda8-86dd-337a-bf54-9b4a36129108 | -9.50162 | -60.51171 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4d50d37-8643-331b-b123-a7f6611f9780 | -11.34688 | -55.40866 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1713ca42-28d4-34d7-99b2-ca3cc28bf6ca | -13.11616 | -46.84902 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b93aaf1-7bb7-3f99-be08-19ad55f59fc8 | -9.15959 | -59.65425 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee20c706-328f-352e-b436-59a863fbb69c | -12.58749 | -46.94778 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1be64aa-ecd9-36b5-a04a-655bbed87db3 | -9.18418 | -59.68497 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5788a712-0896-37bf-b0cd-7e460cdd769b | -9.15501 | -59.69172 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12d7f5a2-795a-3d71-9e55-3de5f5ce1e7c | -14.23861 | -44.58372 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d9dcc5c-afe6-36ab-a7e4-7f83f05abd57 | -12.78804 | -45.96532 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59324836-fea4-3dd2-a697-69dacb68d7b2 | -9.94208 | -60.4797 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab7bed7d-d0e5-3590-a0c6-93d210eaea30 | -13.48048 | -56.66709 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2bea037-cb4f-3325-8e62-f81957eb8589 | -11.34974 | -55.42093 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a431c6c-6a7f-3bbc-90d4-ffefb9ffe151 | -11.0283 | -45.06855 | 2025-08-15 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50737450-f668-3186-a8f8-52724f7e1036 | -11.34088 | -55.41351 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f58cbbf-1af4-3337-bc6b-4596a478224b | -16.5992 | -47.04181 | 2025-08-15 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 386043f5-f622-321b-9ba7-00566ecb26e9 | -17.35981 | -44.13925 | 2025-08-15 04:29:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b2fb3ca-5acb-3ad2-9053-1ed09f554e67 | -14.24107 | -44.58717 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03d9d639-425c-3494-9132-025f0303c39d | -12.35145 | -49.90907 | 2025-08-15 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dbac45f-a186-3e5a-8db6-3669d639306e | -12.76194 | -44.41062 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ef61eeff-9e9a-35ab-873a-f8a3b9228422 | -13.56796 | -46.96072 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47096388-fca6-3649-9424-fc93b5021b33 | -16.37429 | -50.89261 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dbe4aaa-48c4-32ad-9b44-cc822864f864 | -14.23802 | -44.58228 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6cdce483-4fe5-310e-ad66-d05637704766 | -11.34891 | -55.4274 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3302c679-7e32-39d1-a702-23f32fc15979 | -14.90807 | -45.18788 | 2025-08-15 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38bb9048-688e-3167-a7a8-7675ab4e6874 | -9.1834 | -59.65375 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d2a2da4-3f68-3607-b174-70a72d308449 | -14.91127 | -55.0911 | 2025-08-15 04:29:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21371dd0-438e-3022-9f46-7d1000fe9d6b | -16.59637 | -47.03751 | 2025-08-15 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85f0161b-0b8e-39ab-8909-2788b848ccf0 | -9.51142 | -60.53489 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88e6b3ef-cb0b-3395-b750-b90a80fc137a | -9.1695 | -59.67496 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c55a1eab-eea7-35fe-b358-b73274ecd62e | -12.58082 | -46.94669 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2f47770-5fbc-34e5-96e4-0c3d110b96de | -13.15289 | -46.86944 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8939b6b-9a92-3a1d-a29e-34897547849e | -9.15822 | -59.69755 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b205a44a-1af9-385c-8027-0f4df4a3efae | -12.30668 | -44.34507 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c358a45c-c7cf-3b0a-85bb-586aeee699e8 | -12.58415 | -46.94724 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 001fd45a-7d75-3f51-bffb-fd305c008c11 | -14.23741 | -44.58663 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec0b6325-f5e9-32a4-9935-a06ed2c8a49b | -10.11761 | -57.7702 | 2025-08-15 04:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63d0d3b4-635c-337a-b8a4-f836adf1686f | -13.33004 | -45.2288 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fbdedca-89f0-37fa-95b7-3bc253652795 | -13.11531 | -57.15461 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab5574b-ceef-3042-8107-7e51aee651b6 | -12.58582 | -46.95845 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e3649d6-eee3-397b-b136-556c58341100 | -9.92012 | -60.48138 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01ba6943-5c53-3060-a6f5-572281e2c57a | -15.95539 | -48.09084 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22cfee07-7756-395d-a941-e91a91caa0cb | -9.18108 | -59.66548 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a00b614f-f450-3e9d-9a69-19664f212c79 | -13.31307 | -45.22211 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73517f26-a6a0-31b4-b8a3-1636191b08a1 | -12.75722 | -44.41607 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7bce58d-2d8c-3ffc-8d44-1210d14f2f21 | -13.31483 | -45.23458 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20384681-b53f-3c78-b1a5-acc97b7c8506 | -12.5895 | -46.94781 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c071884a-e382-3f0b-ae79-bf22fe35d400 | -14.57074 | -52.04472 | 2025-08-15 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d14c4f-83b3-3f92-8c35-fc8738558a48 | -9.16495 | -59.69876 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90cd50ea-ebc2-36fe-bd1b-5905dd45c246 | -15.39773 | -46.59496 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af862f73-3135-3490-a02f-30e1ddfea3df | -9.20766 | -59.6716 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af934a2f-b8b9-3fa8-8123-eab0c5e7bf50 | -9.50309 | -60.54005 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62849d30-fcda-3685-a0e2-f08073d9fee1 | -10.96941 | -49.57115 | 2025-08-15 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50456904-3309-3d52-8bea-addb28015882 | -10.4571 | -48.81073 | 2025-08-15 04:29:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c5a912b-229f-3c3d-bcd7-4e659cde9ce4 | -12.58693 | -46.95134 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46c05979-af7d-3567-8be3-d00fc613e6d9 | -12.79428 | -45.9701 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f377d6e-2ce2-3157-877c-32989201e3af | -15.17399 | -49.73985 | 2025-08-15 04:29:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c66bccac-cc99-3761-b2e8-b0c6249b1687 | -15.32329 | -51.51226 | 2025-08-15 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bb7149c-a0ac-3222-9dc1-d439cf8784e2 | -14.90686 | -45.18616 | 2025-08-15 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9544889-a050-347b-b772-af4f46f74ee7 | -11.34375 | -55.42577 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6ba8ed16-b720-3328-9f5b-827363c4b0f8 | -10.96656 | -49.56663 | 2025-08-15 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25fc1b2c-bf97-31c9-ad65-a0f84e32405a | -14.07014 | -46.31425 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 462fe41a-384c-330d-b599-093be514cc7d | -13.31132 | -45.23404 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 489ca4d1-a8ef-34c8-8873-dc94a871bec0 | -11.4543 | -47.33017 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f0ffff8-4419-388e-98a9-89ad4292ebdf | -16.38062 | -50.89771 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a6054a6-efb9-3bb2-9637-f9056b97e73a | -12.5884 | -46.95494 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb4a3b75-fed0-3a1e-8764-776915b83371 | -13.32594 | -45.23224 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e78c20c4-9f72-39fd-9259-f0de3eaff3ca | -9.1574 | -59.67974 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48017e0f-ca5b-35aa-bc44-b739fc33aa0e | -15.93197 | -48.15318 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c021e2f-40da-3143-8f6d-8025d02b955a | -12.43379 | -47.88051 | 2025-08-15 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c93ade4-3d66-32b5-a578-7b257df1deb1 | -14.06448 | -46.30569 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f559af-169f-31d3-9040-bb0e4e1789e8 | -11.40928 | -58.53558 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14cf85ee-0217-3ee4-a749-a26279d7fbbf | -10.96307 | -49.56604 | 2025-08-15 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ba872e0-6e5d-33fc-9ecc-860259dcc662 | -11.28456 | -49.11476 | 2025-08-15 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e99bdcad-332a-3709-b3ea-b36eeea66a8d | -11.93035 | -43.44159 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82f1eb7f-de95-38e8-a2fe-46ca0152c778 | -11.5352 | -47.24947 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e23fcba-cc9f-32df-a430-a7e6c62af385 | -9.16173 | -59.69295 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d7a9458-c3e1-3dfe-b34b-76f8290d13d5 | -13.12274 | -57.14515 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72fa26ec-71a6-3026-a2b3-6ad3010647b2 | -9.49656 | -60.55041 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README36.md)
