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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e9d701-986c-3ddb-b4d8-3ee3b1314ab0 | -13.379 | -44.01285 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74886cdb-b201-30ac-9527-b20c22f41dac | -18.48797 | -45.13031 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45b2aa81-a826-3069-81be-471943827d30 | -18.89636 | -43.8031 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e15e86ff-84bf-33e9-b84c-d2fa6d1f6105 | -12.83763 | -50.62669 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60b49cb-0a19-3c72-9a29-e52d83c5702c | -12.25089 | -50.25074 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df87b79e-d28e-3e13-b17b-d7bc29b83514 | -13.37841 | -46.82448 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7506c2e8-a804-3129-ac66-d0643a527602 | -16.11258 | -48.3252 | 2026-09-30 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 825b8241-af81-3c07-9b43-ca4c7f952827 | -19.24992 | -46.68516 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d5dc92f-23c4-3cc2-8a9e-05f5c39eb290 | -12.25497 | -50.25977 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c4b99ee-ccdb-3aa5-9aec-fc215fe583aa | -14.10662 | -46.27338 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f43ab2d2-d4a3-3803-b67d-17c300146592 | -15.25396 | -41.36843 | 2026-09-30 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ee3e9b8-9e95-3516-9958-062afa566d01 | -16.91227 | -42.10704 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f1911ed0-427a-3ca1-9445-184f91d7de70 | -13.41679 | -43.56639 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbb834e7-ed64-3147-998f-704461c3c639 | -12.24445 | -50.25357 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e18645ce-0631-3fa2-81b8-f94a171763d7 | -19.36284 | -41.50856 | 2026-09-30 03:57:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81d0b50a-e5ce-378c-87b0-58c177fceb2c | -12.24187 | -50.25359 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8de07219-b98c-3279-b4a8-56a907b14d26 | -12.77664 | -54.02419 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc52655c-702d-3a57-9f04-b46963335af4 | -15.09431 | -47.82981 | 2026-09-30 03:57:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0df03f2d-93ed-351f-8317-afc56b91a227 | -14.8161 | -42.77082 | 2026-09-30 03:57:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2879f1be-f453-3de8-ada6-4498de9a7126 | -18.17995 | -39.6281 | 2026-09-30 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22bd1e2c-cc7c-3c76-926c-7b84ba7e0b68 | -18.88331 | -43.81699 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35dfe012-300f-3cb4-a064-46755bccb396 | -12.51744 | -43.08231 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfb6a85b-dd22-3c9f-822a-a42852a824ab | -12.24264 | -50.24961 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2d15031-86e1-3d87-bc70-30ec908c8cca | -15.21329 | -41.9812 | 2026-09-30 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 729383a8-ff2b-360b-884c-adfdffd0aa3b | -13.36955 | -46.8228 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ade3efa-134e-371b-8cee-b029b461b7cf | -12.25182 | -50.27562 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bc8d41d-dbb1-3ca0-81d8-7c02efffd061 | -12.56682 | -43.07354 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e915c801-7ea2-31bc-b30c-2d390a0ec9ad | -15.09001 | -48.33213 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a74413c0-6bc5-37c5-82e8-469906d9b57f | -12.31344 | -47.95614 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 26290199-db83-37da-ad88-9d841e5a689a | -19.42989 | -40.35148 | 2026-09-30 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ec04860-6585-3191-8ce8-f461c0847928 | -13.38314 | -44.02113 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6753756c-ed0f-3802-b472-d68c483b7a3b | -13.32672 | -43.93818 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b60cbb4-1223-317e-9d07-cb0a62e21f70 | -17.79377 | -47.16846 | 2026-09-30 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c95c976c-660f-3e55-bae3-9f2d255985b7 | -16.08123 | -41.11052 | 2026-09-30 03:57:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7f01247e-990f-3112-a4f7-dd38567a8333 | -14.94098 | -49.75412 | 2026-09-30 03:57:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b15d68e7-2d48-31f5-96b5-4217d1b48ade | -14.9096 | -41.68952 | 2026-09-30 03:57:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 44b227e9-6877-3af9-8597-bef9845a3c54 | -15.77463 | -46.03128 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48de398c-ec58-3b9b-9587-50ea548af587 | -15.63542 | -43.23537 | 2026-09-30 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 20.5 |
| ef3f3079-639c-33a0-8165-376400547ad8 | -14.98682 | -41.48616 | 2026-09-30 03:57:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43ec9380-276b-301f-9bc9-2b5328c1a25b | -19.35766 | -41.49667 | 2026-09-30 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c82c850-645d-332b-a097-9434e220d86a | -12.71341 | -46.96548 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62bb6e34-88d9-3525-9eea-7d06cbde878b | -15.9783 | -48.1407 | 2026-09-30 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3de26d42-f533-311b-a54a-a845c3e6fbad | -18.10165 | -44.4061 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11b1a55-e71f-337b-906e-32feeb747de3 | -12.77953 | -54.01046 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e52000a-6c8e-30aa-b0d8-099b1beab312 | -12.81038 | -50.66949 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53011e4a-b270-30bb-964e-44ce97e7c7cf | -13.69069 | -44.08036 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09db17ab-ace8-37db-9424-5e8cd58d0630 | -18.23559 | -53.02761 | 2026-09-30 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cdb44df-8017-3dbc-a3c4-8a63c056b66d | -12.95378 | -46.64025 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2aba5c3-1be4-36fa-b54f-1d3de6ad0be3 | -18.51729 | -46.27393 | 2026-09-30 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 397c8734-6c39-3009-9eb9-cf974b02cb4b | -14.12226 | -46.25938 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa760ad7-5c01-3c45-81d7-331cbb84d15a | -18.88606 | -43.82174 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6372544d-0a60-3ec2-9c1f-57a1802fcb86 | -14.80147 | -45.95964 | 2026-09-30 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeb3f456-fc17-340e-834b-4620708dd301 | -12.7865 | -54.012 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60869c25-519c-3b56-8c6a-582384ecd159 | -12.05107 | -50.22485 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acfc2919-8b0a-3314-a05f-8322dd5d26b8 | -15.08531 | -48.33097 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be142028-77bc-3629-b6a5-46b9ec28c934 | -14.53724 | -48.2991 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 579a2c4a-d0b8-3234-9779-72d223ce1afa | -18.88745 | -43.81364 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dcb464a-6045-3978-bb01-546189e17d83 | -14.94086 | -49.7534 | 2026-09-30 03:57:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 721f776a-3c10-30e5-8d3c-3a09c910f991 | -12.8319 | -50.62553 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22619e90-ba6e-3b3f-98f8-f91b0c42dd3b | -14.85184 | -48.18225 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc33e404-7c00-3d1a-acbb-038f714cf7bb | -14.91104 | -43.41462 | 2026-09-30 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a32ceb49-5149-3002-a15d-af5b920d4cb2 | -20.24861 | -41.40931 | 2026-09-30 03:57:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7740ded5-6578-36c0-9306-d3755cde884b | -17.78881 | -47.17172 | 2026-09-30 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae2fb420-4bbf-3c08-b0d5-121b2fc5b02b | -13.33392 | -43.96292 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 648543e8-67e8-3fec-bfc9-94f19c733041 | -15.20037 | -46.14089 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68ca0ba7-b5f8-3924-bb01-4f08b5c5b46c | -16.90893 | -42.10646 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 859b2f5b-4b6e-35f8-934e-d224a413cad0 | -15.16046 | -43.57164 | 2026-09-30 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee23d1dd-ad99-39c8-a7c7-c83853596437 | -12.24603 | -50.24566 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24c1f3f7-8ecf-359c-9c80-e0c5ee8436d6 | -13.33763 | -43.96357 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 04ff8d33-0408-37b4-9e96-171cfd14909b | -18.30776 | -42.2166 | 2026-09-30 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 819607f8-42a7-3bbb-9552-df30cfd9f968 | -14.53343 | -48.29302 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2439146d-dd53-37ec-9574-111c4b5dcba9 | -16.90285 | -42.10162 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40f5baf1-30b9-3db5-9361-c9183c845861 | -12.81613 | -50.67067 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38ed2b48-024f-3bef-aef2-e6e9bf37ac12 | -13.6829 | -44.28777 | 2026-09-30 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5e12a6f-58b6-3410-8ff6-83c1a21efaca | -20.17422 | -41.75656 | 2026-09-30 03:57:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be604650-8e5e-3032-b3d3-f1e21891e64a | -19.1911 | -46.81337 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b5efd11-c486-3d33-84dc-8c04eb2a0d80 | -12.31446 | -47.95064 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe6b9396-4bf2-3732-916a-416c62f71bd8 | -16.1921 | -42.87378 | 2026-09-30 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d598a7db-9a3a-3c83-9e4d-d79a89310802 | -18.88634 | -46.94027 | 2026-09-30 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 56945be4-8eaa-3caa-84c8-14f77faf4c2b | -12.30281 | -47.9591 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 54bfe762-25e8-3c4c-be0b-63dd0b3086f0 | -18.6323 | -46.97548 | 2026-09-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2d7c2e7-1e43-3a2e-bf02-5e4d92ea30df | -13.52274 | -44.3124 | 2026-09-30 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8753f79d-cdde-303f-b348-93b651f4bfff | -19.34134 | -43.7323 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce3007d0-4252-3ba5-a6b2-1a11847b4f6d | -18.59517 | -43.44127 | 2026-09-30 03:57:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0d75f4a5-1322-324b-9c8b-83ce939a53b9 | -14.50562 | -48.28284 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac6145b-6ceb-326d-a120-bddb7be7b102 | -13.37175 | -46.81086 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 994e628e-72a3-3451-af05-6035c2c14853 | -12.43052 | -44.16706 | 2026-09-30 03:57:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3344560c-705e-3924-a713-11f933ee4be8 | -13.64453 | -45.56263 | 2026-09-30 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9669d759-0d96-3df4-8174-1d731c838387 | -16.80503 | -42.57244 | 2026-09-30 03:57:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75deac68-452e-3608-864a-63e0ac720065 | -12.15035 | -47.20202 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ae07a18-ff3e-3dd9-a3b6-325772a23b37 | -16.3567 | -42.58302 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f429605d-f53e-3d0e-932d-8a33b5105eeb | -12.62624 | -48.35884 | 2026-09-30 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc790288-f658-3680-8f6c-e23120a50854 | -11.84513 | -47.78593 | 2026-09-30 03:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d93e77d-3ee8-319b-8775-7d633f1f443c | -12.76943 | -47.25325 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ea03079b-2a9a-3012-a878-c07ae7ffda43 | -13.39721 | -40.06902 | 2026-09-30 03:57:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5772b3e2-4f3d-3c10-894c-98b1bc4c30b7 | -12.04054 | -50.21857 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 978faa4f-5a17-358a-801a-f57ad935b45b | -15.1976 | -46.13984 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6041e5e9-06ed-3614-8820-4bb5571eb338 | -12.4373 | -44.17318 | 2026-09-30 03:57:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43377e31-b748-31ce-abf8-948912e2004d | -12.06985 | -46.46525 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9dbaa02d-fdea-389a-b1ca-1c38a7147af3 | -18.88676 | -43.81764 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
