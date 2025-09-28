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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90d23baa-7ffc-3f86-ad51-33071990cdc4 | -15.1965 | -48.46143 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca12a89-3342-32a4-bb40-d45a36334c7f | -11.71496 | -44.4308 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fc34be6-9734-38cb-a65c-7138c40154c6 | -12.97897 | -46.90311 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17fcaf7f-0fe0-30b6-a906-addec0c171e8 | -13.39811 | -48.15264 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9119480-b9ef-333a-a1de-989a7f8a6b6e | -11.20928 | -47.74615 | 2025-09-28 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f7b7b25-3a76-3f11-9b21-25957417208a | -15.08506 | -48.33331 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92baea99-1432-3b7b-ba40-d4e3d0fc5ca9 | -13.50918 | -47.39655 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f241d3a-d2a6-30d8-9659-32eb8c650bf9 | -11.41963 | -45.02829 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a862a40-87e4-3ca3-8c4b-45e11aa03116 | -11.79223 | -44.90614 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef0427a5-25db-36a2-937b-3a1910cea2df | -15.2562 | -43.08886 | 2025-09-28 04:06:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21249cfa-11dd-363d-a42d-97dc81a5fe1e | -10.41149 | -46.14364 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db18002c-fab8-39c9-b826-022d5010bf23 | -11.42999 | -46.64837 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 180fbf95-027e-3a53-846e-f51d4ff70697 | -9.90024 | -49.12098 | 2025-09-28 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f55c0b42-0b76-3caf-9970-a1814179899e | -11.60217 | -45.43549 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a595b90f-fd92-39d6-84cb-66031c21ca7c | -13.62688 | -48.06977 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 973e3a47-0c85-31c0-9469-9978194b3a9d | -14.43064 | -44.87782 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9538d064-c219-3b1a-87e2-af5f7171667b | -12.00212 | -47.90474 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c737d163-5616-3118-91c5-5179012a87e4 | -15.2395 | -42.71527 | 2025-09-28 04:06:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 782b1ebe-bf6d-3855-aa0e-65ee96feeb7d | -11.50399 | -43.53965 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93b73ab4-1fdf-30ff-91f2-36fdae95ed8e | -12.78676 | -47.75361 | 2025-09-28 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b64ca9b-2ceb-3bac-a75c-a1c099c97fed | -11.43737 | -44.9241 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa98d772-cdf6-37ec-9307-f4d6662c0b92 | -12.96513 | -47.21656 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497cf144-608a-319c-a2c5-5825bb3ad5eb | -11.64987 | -48.27164 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d6ef85c-b240-3f98-abd3-c316d46e64da | -11.71132 | -44.43016 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b2e3490-bd88-3d93-8028-f22f82f20ff6 | -13.61052 | -48.08488 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e59c68b-2cb1-3610-9c10-4dd7e9a1c40b | -15.90126 | -46.2137 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9f47ce1-f8a0-3df0-ab1f-378f4dea755e | -11.57994 | -45.49623 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf61c997-241c-34aa-b7fb-c6367844e88b | -11.7164 | -44.42227 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9edf79e-f62d-31f9-99c6-c0cb0a9afb9f | -12.01955 | -47.92196 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dd4dead-997f-3c39-952b-3de8f780d3ab | -12.00941 | -47.97625 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e93b8fe-5fe2-3084-b427-fe7c5e58bb5d | -13.60514 | -47.31899 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 181c3e07-2ec6-39b4-96b7-c0ed7fca4070 | -13.34573 | -47.29197 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcc267cd-1d0a-34af-b0ec-3651f5b78f2c | -15.02593 | -46.97093 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e652419-8bc1-3f87-ac21-00381429184e | -15.02193 | -46.97015 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c6d116-7d16-3f42-b30b-8f6f1e1c97ac | -10.96928 | -49.5672 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b16504-f127-32e3-b820-1776cbbe2f54 | -12.00894 | -47.94398 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a372ba8-2fa0-36f8-81c1-36d85054aa6e | -10.96516 | -49.57307 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1d00539-20e0-31d6-8cbe-4b63372aa2fa | -15.26826 | -51.47728 | 2025-09-28 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d9db3aa-c908-3ac8-9f83-a09a0fd04a30 | -11.97769 | -46.58807 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57367895-7d0a-36f4-a53e-58d3eb366146 | -12.92138 | -45.18153 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9688bfd5-6320-362c-9514-088fe003bdcb | -11.42327 | -44.91635 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1e95402-8359-39b1-aedb-c9d7de2da35e | -11.6946 | -44.46243 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08c0f7b9-3139-3928-b301-a3c16c3fa17b | -11.00107 | -45.60149 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad7f169-5d70-38e3-bc60-d792564f2e51 | -10.94258 | -44.31564 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf87d444-6665-331e-a39f-c55d6628b728 | -13.63519 | -48.06852 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55133a37-01ca-393e-925b-37bff19f6ebd | -14.78203 | -45.63671 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cc47a15-5dba-3b61-b8f4-a8e7bb39323f | -14.5388 | -48.42537 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51ba7bf4-e792-331e-995c-b002ec1d78b2 | -11.35736 | -44.96382 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07683c31-fbda-3aa0-9065-d33378fd052f | -12.68382 | -46.88085 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f20fa3f-d2cb-3212-9d3d-72e32391feea | -13.51756 | -47.39837 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8acef50c-0553-38ed-9322-19562bbd362f | -14.53936 | -48.40474 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eae1828-b3fc-3922-a5e3-2353248c3665 | -12.00012 | -47.04388 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1bff44b-d8fc-3298-b7c9-bef6ddbd685e | -12.93657 | -45.11486 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e5d6f87-23d6-347b-af09-a0e5bf934969 | -11.97673 | -47.07652 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2a786696-8d2e-3f14-acdf-1143896e87de | -13.00922 | -49.45427 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58baa452-a62e-33a0-91eb-0478a9e582db | -13.7725 | -47.867 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74b71874-51a1-362a-b8d4-4bfd307b4d7a | -14.4935 | -48.55456 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e57a217d-2e81-36d0-8420-f6521eb2002c | -15.44791 | -48.23054 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e74cd7d2-e489-30ef-866c-e9baafd1e56e | -12.00577 | -47.9616 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3603ec4c-2055-3e07-b864-4401aa595460 | -15.88007 | -46.20121 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbcea377-e6f3-3302-8395-44290d1679f0 | -11.36266 | -44.999 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 719ffe3b-6f34-3616-a4f8-b127479dda32 | -13.29182 | -50.69093 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a23944-86b6-3789-8f18-2a47347f94fc | -13.63924 | -44.41376 | 2025-09-28 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7f35464-6e83-3fd4-8c3a-ae28757ab6f0 | -16.39934 | -43.72145 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ec680e9-de8c-308f-88b1-024e8638b7f5 | -15.20353 | -48.47226 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 786b6eeb-dbd6-33ad-84ca-2a4f1f148ca6 | -11.43365 | -44.92328 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e9f2db5-6076-3425-bdbe-501d5419205a | -13.39311 | -48.16659 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f29165d-a84c-342a-8b29-9fc860a3fc97 | -15.44204 | -48.23801 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e918f72-7419-306e-98c4-18684b9b0f6a | -12.47607 | -44.91675 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01e0e51c-5f09-337d-b59a-b2363f7b74ec | -15.53736 | -47.91766 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57756de-4b65-36c7-b467-52b78e0a9114 | -13.3416 | -47.29088 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89d1db11-06a4-3188-8d8b-8ebcdc5d8dff | -15.33225 | -47.87903 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fee80654-709d-348a-b539-bcb0d2eae57b | -14.46852 | -46.35102 | 2025-09-28 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a35f230d-97b2-336c-ad22-40d9a9bf4fb0 | -12.011 | -47.95828 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7143106d-1a0e-3ecf-9191-e44f90292140 | -11.36488 | -44.96507 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d9664a9-c0d0-3a37-b644-f0690b7072b8 | -12.95425 | -45.14577 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 613b6e58-b557-3a31-85da-5b94a5ec8fcd | -11.71277 | -44.42163 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04dec5c6-e9af-3e29-8cc4-19d6f7f46064 | -13.61723 | -48.0729 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb39e8b6-1c11-3b39-94de-0f874660d8ed | -11.61956 | -52.85949 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef35909e-0f78-3918-94d8-06f61cc725e9 | -12.89768 | -45.16331 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e31bc4af-edaa-35a0-b18b-8200528deb5b | -12.8887 | -45.17099 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2ac2195-ba65-393b-b39f-3c50e1599ece | -12.01203 | -47.96223 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6aae693c-50f2-3a57-9dc3-17198c5a9214 | -13.60985 | -48.10639 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d9ed2c59-ca62-3571-98da-74434a8e7a71 | -11.71713 | -44.41801 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e7126d8-7c6e-390a-8be4-4eaf78b58806 | -13.65416 | -43.01082 | 2025-09-28 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e121e7dc-8425-35f5-a0ca-470b8c841e89 | -12.93135 | -45.12309 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10e2e8dc-1f20-3d6f-a025-303727b84f17 | -12.0032 | -47.97596 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e378294e-a97c-365a-941f-df850f97f1d9 | -15.02769 | -46.96802 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb1f45a1-f2bc-3b16-8284-ff43da802478 | -14.3375 | -44.49714 | 2025-09-28 04:06:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1df512b1-8444-3203-87ab-6f7ab1c0ef8d | -11.72003 | -44.4229 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31870c74-89e0-3456-81c7-5f096195a2a1 | -12.83053 | -44.68343 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54934cfc-4898-3916-a4bc-b2b6d92b1ecc | -11.98228 | -48.01469 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52bbde8d-cd6c-3c72-a16d-28b81b80fe0b | -13.62341 | -47.31349 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db99b615-c19e-3e37-b022-c4b5095197b8 | -12.9513 | -45.1406 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a02ca73c-b20c-3579-8d5d-ce12ce26b5ab | -15.62353 | -48.35361 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4d2cae9-039b-3678-89b1-2dfd7bbf2d0f | -10.13205 | -51.62963 | 2025-09-28 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f187dbff-3e9c-3b3d-8827-068cf0fd7301 | -11.68662 | -44.42144 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 571f29ce-e7c5-3053-8bff-90c8d9ba501d | -10.41839 | -46.1523 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e562cb9-7220-3a4e-9bd0-05a09ba6001c | -12.00296 | -47.90004 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87516b3d-4619-3b90-8b21-a563cce65623 | -11.78711 | -44.86843 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README45.md)
