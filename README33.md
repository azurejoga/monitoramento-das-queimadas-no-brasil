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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 089d0fe5-3a32-3099-8653-efedf4ba53f3 | -10.90925 | -50.15818 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a8ee379-891a-32c0-9f3e-842991d10391 | -12.3782 | -63.87316 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c445d333-5f13-3ce1-a4bf-0d1bba729320 | -11.49472 | -48.47385 | 2025-10-23 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb7a98c-da78-3bb9-86a3-d72d119f9dce | -9.23981 | -45.59901 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf9b6233-ef1a-3c3e-8d33-15542d3edf08 | -12.90671 | -48.49117 | 2025-10-23 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd32307-f3c3-3023-b032-e8b5fdd21ed1 | -14.21326 | -44.52345 | 2025-10-23 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67b5a279-0108-3fc5-ad87-c3032528f00d | -12.38531 | -57.51781 | 2025-10-23 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e7710d0-170c-31da-9a2e-e5edb574e773 | -11.36041 | -49.78775 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54d2e834-c2c9-3a3c-a18b-47eb0926cf5c | -14.39131 | -52.77045 | 2025-10-23 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 912b7208-7e3d-34b4-823f-624a5aa293fd | -12.6865 | -48.64074 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48238267-371d-34ed-b82c-8df9a860bd66 | -12.55212 | -52.22143 | 2025-10-23 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db6024a3-022f-3191-b017-e91d15e30f99 | -14.83305 | -48.3184 | 2025-10-23 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6818bc57-3f81-32ba-bf4c-fa2c55e2d08a | -13.79154 | -52.77211 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6994ebb9-b954-3f77-a498-5c18298a59a6 | -12.01845 | -46.74347 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6868fdac-199b-38eb-a9e7-213c695b1745 | -9.72274 | -64.97288 | 2025-10-23 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 124278e7-d2dc-324a-b530-6aa7a44fab47 | -12.68196 | -48.64013 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5edb0f86-5590-3fa2-a723-a48d35cf793a | -8.62464 | -44.81425 | 2025-10-23 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4576499-f5e2-3caa-9cd2-c2f2ab49855a | -9.23368 | -45.60451 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92e184a6-e2a4-3fa9-8d53-8738dd2e046b | -12.12948 | -62.97581 | 2025-10-23 04:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b85bcb0-a89b-3c6b-90c0-0e81dbc83b1a | -13.89581 | -48.3758 | 2025-10-23 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f39017b7-b348-3815-bd1e-01d04c9debd9 | -12.09499 | -63.62482 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 52ce38b2-a3ce-3845-afed-65267aa2ecfd | -10.9118 | -50.11204 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94bf397d-896b-38fb-85a2-0f9afe033d72 | -12.69832 | -61.06385 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a57c24e-7dad-334a-ac1d-957e8b0ac1a3 | -12.1279 | -46.72535 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fa68e21-8608-3cac-9fde-b8504c0746e6 | -12.09446 | -63.6237 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b6c7cd7-6d44-34ab-b1de-f879a9da51dc | -10.62249 | -48.07692 | 2025-10-23 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b43c40c-3a47-324c-a4e1-cc5febe3b735 | -11.35577 | -49.79092 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da804bf1-793b-36f6-a571-b46dd99fb11d | -12.10052 | -64.2986 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97261b0d-f5ad-3e54-bd33-efe6315ea7a7 | -10.25044 | -47.99559 | 2025-10-23 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8faedd4e-5cb3-3b8c-9b48-9fbc8edeb6df | -12.37764 | -63.8761 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 431804b0-24fb-3774-84e0-76fb19308c98 | -11.24836 | -49.87815 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| baa911ec-6ee3-3f28-b390-79dafee948a0 | -13.79598 | -52.77385 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f74f159-079e-3be8-9ff3-e528d47758dc | -11.00777 | -47.67833 | 2025-10-23 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b873d28-aaf1-3cce-becd-c6a772959d65 | -15.59773 | -45.90771 | 2025-10-23 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3084daa1-c85b-3348-9b65-4aa8a4d9d09c | -9.86637 | -47.7234 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a895c482-0fbb-3bb4-801b-87a36afd3659 | -11.99831 | -46.77875 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d85eace-69b3-3cd2-a6f4-ff77301cbf95 | -12.02173 | -46.74214 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d5e892e-e4af-3537-ac56-60c97c7eb151 | -14.83285 | -48.31624 | 2025-10-23 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d6da3a9-a818-303e-af9b-80f88a6585a6 | -10.24981 | -48.0004 | 2025-10-23 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cacdc50-ca5d-3525-b9b8-12198825c215 | -13.0404 | -47.23093 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f6e885-f697-3b4e-86d4-b64875caefa3 | -11.99792 | -46.78175 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a41355d6-70b2-3d58-a053-171cfcb66408 | -11.99754 | -46.78472 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66e2b661-1c50-37a5-bfe6-fad9d447bc3a | -9.97064 | -47.08174 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 966a3b18-77a3-3737-b2e7-9167029b93db | -11.3724 | -55.06572 | 2025-10-23 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5bb9088-a4a5-397c-ac18-1a7ebb752509 | -12.67857 | -48.63077 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ebb1192-33e8-3b2f-a425-bd9f13964416 | -11.16013 | -49.94358 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e466dfb3-cf94-3cdb-b62d-5f947cf19a14 | -8.62513 | -44.8106 | 2025-10-23 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9250ae-9595-38c4-95a5-2e0331169d09 | -11.99205 | -46.78706 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fae5303b-09d7-3b85-bf8d-14252801d57e | -9.86389 | -47.7162 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19eca964-2505-30a8-8b65-120d88ed5814 | -11.27317 | -49.79108 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee7b1d76-aaee-38ee-a06e-91ffc3a30c42 | -11.11917 | -48.34277 | 2025-10-23 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbe1e260-dcf7-3614-af5f-26509778aea3 | -11.12367 | -48.3435 | 2025-10-23 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6812d12-5b74-3263-9bf8-45021771541b | -14.095 | -44.2401 | 2025-10-23 04:57:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bff7b50-7182-3142-b2c8-6f1c6f661d5c | -10.27387 | -47.58466 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157e306e-74b2-3c6c-8df7-918fd0ecdedf | -10.97686 | -54.24906 | 2025-10-23 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a7c2e5e-6e3f-3f6a-a709-3c60e90e915c | -12.25 | -49.58934 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f66084f2-dbe8-3944-8860-aacbf40b3de4 | -12.80285 | -60.66634 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98a988b1-4ba5-3e40-9988-8d6418c072fd | -12.76706 | -47.37679 | 2025-10-23 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5e41a80-8072-3d2e-b7ef-79f1989ad366 | -11.97174 | -63.92066 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5327bd7c-613f-38b7-b75d-6ea96923a7e4 | -12.1267 | -62.96452 | 2025-10-23 04:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8348b113-74d0-37d6-aabb-17bc5c0dd362 | -12.16677 | -47.05153 | 2025-10-23 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3951f600-dbbf-347c-b89b-998ee0e091b8 | -10.39171 | -47.10204 | 2025-10-23 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1038547c-ce51-30fe-a57d-17fbf8ab6431 | -11.34727 | -51.45082 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f48a32f-3e75-3280-a8e7-a8ed0e661909 | -12.0034 | -46.77941 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83126c92-83b4-3f8a-a404-749d0d3dc470 | -12.12994 | -46.72933 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33e8d2a7-486a-336d-8e1e-aebc0207337c | -9.23322 | -45.60794 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48134149-7113-31a6-ab17-f60f94619920 | -9.23452 | -45.59814 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ac298da-c8e8-32c9-b0fb-83af61ca0d16 | -13.90048 | -48.37664 | 2025-10-23 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8543adc4-d4a1-3c1f-b7e3-cc5ddb7253aa | -12.69643 | -48.84187 | 2025-10-23 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 601df0f2-8180-3084-93c7-5d3708305cfe | -12.67918 | -48.62611 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c95f8237-4d6c-35ac-808d-ca04f09d4a94 | -9.72198 | -64.97691 | 2025-10-23 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4384b552-b85f-375d-9995-b3ac4bbd57b0 | -13.7951 | -52.77267 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 602d867a-b45a-300c-a277-2db3a8209b08 | -13.79094 | -52.77631 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e2a8346-0ce2-353f-9dac-5ba640383622 | -14.4741 | -47.91172 | 2025-10-23 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 179e8afb-68b0-3044-8335-8f1e303db092 | -13.45952 | -48.82833 | 2025-10-23 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 435afa8b-8ebf-3f6e-9f66-c7edde4de474 | -12.02135 | -46.74521 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f7ca577-f017-3c7f-b1f1-e3f1003af4e3 | -11.99244 | -46.78408 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 952bbfe7-1669-3b3e-85a5-58aa48e095e8 | -15.5973 | -45.91158 | 2025-10-23 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5385af0d-cb21-3fa8-80fb-a34aad19e4e2 | -8.61904 | -44.81387 | 2025-10-23 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26bd3ab8-9147-3a0e-8d34-bebb373239e9 | -12.37321 | -63.87216 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1902ae-1849-36d3-bd79-d248608584f2 | -13.80102 | -54.82083 | 2025-10-23 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fda1e3b-b9c4-3d54-9531-40cd20f07abe | -12.69763 | -61.0677 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfc827e0-794d-3782-ab34-05438a938f20 | -8.20277 | -46.98994 | 2025-10-23 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76364281-6c18-33e1-83bc-8dc5b9c3186a | -11.96193 | -63.13078 | 2025-10-23 04:57:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01228fde-60ca-354b-b119-0d60b730acc4 | -11.00844 | -47.67329 | 2025-10-23 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90461180-e3b6-315e-b315-a525db9fc450 | -14.20715 | -44.52297 | 2025-10-23 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a229a105-4d12-3dee-bbb7-099eb6191278 | -12.13263 | -46.729 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66e26282-d123-3a77-b6c6-2ed6e7429f5a | -12.80347 | -60.66282 | 2025-10-23 04:57:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dd579e4-0415-333b-ba6d-2ef451307743 | -9.97205 | -47.07111 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5055781-0538-3ef8-91bb-ddeba46dbf91 | -11.35473 | -49.79841 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1850893f-3c3e-3eda-a7ec-40e288b8aa9e | -12.24524 | -49.59267 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79b55237-17e2-3609-92f8-092445d06e86 | -11.53806 | -52.24015 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9a12b5-35ec-3ae3-86b3-a58448d47327 | -9.86322 | -47.72096 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cfd5630-7a1e-3281-9eff-992302f0bea4 | -15.59124 | -45.91449 | 2025-10-23 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 888a01e2-85d6-3658-830c-4cd2c119f55d | -9.2341 | -45.60129 | 2025-10-23 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 871ab013-48f7-3c37-a5c6-66463ca4c0fd | -13.04002 | -47.23386 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ad0114-78f3-37aa-b1f5-a84e1f3922aa | -9.08691 | -47.81823 | 2025-10-23 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3855648d-5036-31cb-afb5-5b5a8f4d7931 | -14.261 | -56.45213 | 2025-10-23 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67a5ce76-89de-3b2d-a5c6-30fe0c151495 | -10.24988 | -47.99816 | 2025-10-23 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 743a1243-2e4d-36f7-a00e-ab83402e4dfd | -13.89648 | -48.37049 | 2025-10-23 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README34.md)
