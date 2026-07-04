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
| bc168532-9871-3c1d-8494-5392cdbd3997 | -13.22782 | -54.35257 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0c03b687-a92d-341d-aaed-c659c3a3264b | -13.25783 | -54.34097 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 559327d0-667b-31c8-ad83-08b2423674a9 | -10.29889 | -57.1282 | 2026-07-04 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ac484f-2f55-37fc-a5dd-423be8e6e888 | -10.06974 | -67.56422 | 2026-07-04 05:23:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2cd0746-edbb-357e-a801-a3149c178b14 | -13.22964 | -54.36866 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edafa6b1-eecd-396f-a26e-726be0678c8e | -12.34858 | -47.9034 | 2026-07-04 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d4b450e-b64d-3b4f-aedf-292b8dbe7298 | -13.24988 | -54.33976 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 245767ab-7953-3b23-8781-9ce88b7fed6c | -13.22529 | -54.34147 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44fe6845-ca09-36b4-b2b4-2fad63909fa5 | -19.51052 | -52.74069 | 2026-07-04 05:23:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3131df91-e85b-3076-a4fe-e8a2c694a010 | -13.24193 | -54.33853 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9650dbb-3b54-3e7e-bcc7-f2eb50944440 | -13.23686 | -54.37499 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bfddd4f-251a-3566-b8a5-104fc40ec18a | -11.45318 | -46.55325 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3176dd4-7d53-36c8-930d-6b3a7de4b483 | -10.90541 | -56.85893 | 2026-07-04 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9bfa304-dcb7-39da-a62f-a71c7fca474f | -11.42954 | -46.58271 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6d567e6f-2249-36a5-aa45-dfe245cea7d5 | -12.3546 | -47.90425 | 2026-07-04 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a440a912-80cf-3b75-a81c-a82cece049be | -13.23432 | -54.36411 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e921a2b-dc5b-3295-b78d-6814554708dc | -11.42339 | -46.58355 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f20a0e94-3af3-36aa-81f5-da4b13fd004c | -10.06265 | -60.49591 | 2026-07-04 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f80526d-601c-3d9a-aebf-ac70b3d79409 | -13.23577 | -54.35371 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6894803d-d2a1-342a-a19c-5d9bb1830029 | -11.42934 | -46.58892 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d8b004b-595c-372e-8eb9-886e1e75cb61 | -9.43448 | -58.0213 | 2026-07-04 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b950c3-15e2-34bd-833a-beb9fa306070 | -7.24111 | -60.6436 | 2026-07-04 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 037c1590-c5a9-312d-8b07-887928804c35 | -13.25636 | -54.35146 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73db2c59-af05-311a-b4e6-c4e9a6f82e27 | -11.48825 | -52.91975 | 2026-07-04 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b2513d-ff63-3261-ad1e-f687694925a2 | -9.32705 | -58.03644 | 2026-07-04 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5bd4196-9ade-3d6c-8dde-24a3e38dcea4 | -9.5986 | -56.92274 | 2026-07-04 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f59336ad-5d93-3162-8f5b-571ab34dfb8f | -11.63139 | -59.01626 | 2026-07-04 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da528b83-dd59-361d-9680-3a26baaf1900 | -13.24915 | -54.345 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72ea8e0c-049b-3b06-a47d-235424e54e95 | -10.30015 | -57.12407 | 2026-07-04 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aba14ca-0c88-33ec-89f9-b22713c5441c | -12.51243 | -48.25503 | 2026-07-04 05:23:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93fbd2d4-be9c-39db-86df-af59fb089a7c | -13.25458 | -54.33516 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1d9447c7-76af-3646-9a03-02d66bd03d4e | -11.73947 | -57.81035 | 2026-07-04 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3cb70ac-3577-3e1a-8657-02d1ae8c8ea2 | -13.23252 | -54.34787 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 359df9e5-5713-352e-abca-7c30ff211b31 | -9.04424 | -47.74199 | 2026-07-04 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 709762b8-180a-3f90-98c8-2e6785744e0a | -11.62807 | -59.01572 | 2026-07-04 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c139acce-099f-374d-b1bb-c4bfcd31efbb | -10.90597 | -56.85521 | 2026-07-04 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe6ea6d-36b7-3865-890a-d8a0b0548f2f | -9.04367 | -47.74619 | 2026-07-04 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ac63347-59a3-3117-a945-ecece658cfb5 | -11.43826 | -46.56854 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b165606b-88ec-3f57-b675-b96e640950ba | -13.22927 | -54.34204 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a291bb10-1377-35d1-8a8f-d9dfbfcc5674 | -8.55082 | -47.23857 | 2026-07-04 05:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e7ea154-246f-3a92-b2a1-1afdda710582 | -13.24842 | -54.35024 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2ba48490-b9f8-381d-b53a-68e7cdcb8f07 | -6.42699 | -55.79547 | 2026-07-04 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aea36fe-39ad-34d7-ac18-ed7361901272 | -11.40793 | -57.81319 | 2026-07-04 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0b05492-fae2-373f-aa4d-9531c5253f5e | -8.08323 | -47.15779 | 2026-07-04 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a789179-9ada-3893-973b-89d975994e22 | -13.23723 | -54.34317 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7d49aa24-fe22-3a07-a3c7-b00685f484e2 | -9.37525 | -65.77675 | 2026-07-04 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11834302-e3f1-330e-b9cf-31b423bbbf2e | -13.23107 | -54.35836 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77541058-7a04-33c1-9143-43c9729a2c52 | -11.43796 | -46.56764 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fae8dec-fe5d-31ba-8f95-2e187428fdfb | -13.23035 | -54.36353 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6e05b6d-db5b-3291-9c04-9a62e29378e4 | -13.23868 | -54.33271 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda13312-35f6-39b5-a561-f12abf0d5960 | -9.66387 | -56.49557 | 2026-07-04 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f045b892-6802-3fab-8f70-76d892a96126 | -7.50991 | -49.52808 | 2026-07-04 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f764732-6247-3b29-b125-b42ba0691d82 | -9.04276 | -47.74338 | 2026-07-04 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7e686af-2714-32a6-81ca-c15104aecccf | -8.08698 | -47.16055 | 2026-07-04 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aba4e07-62c6-3bcf-a646-731f88364424 | -6.61273 | -55.29083 | 2026-07-04 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e061713-bd95-36cb-9c42-2d38209880be | -13.22893 | -54.3738 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0fe7569-34ff-395f-9ec7-c8cc00e36e50 | -9.56562 | -49.11147 | 2026-07-04 05:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15f39926-00b3-37a4-91ac-9dcc70d07541 | -8.03529 | -46.24071 | 2026-07-04 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5f5c65c9-cf3a-3337-9a6e-84784ebda390 | -10.12695 | -52.09763 | 2026-07-04 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 715d73a9-bb4e-391e-bccc-ed4b1f26c520 | -9.3814 | -58.20635 | 2026-07-04 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 218bf887-5064-31ad-828e-56dec66f18fe | -13.23325 | -54.34261 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4d41515c-4767-341a-9d56-ff3a481996b3 | -13.2412 | -54.34378 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dded3e31-c654-3575-aee4-68c120846e5f | -13.23504 | -54.35893 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 220d3eb5-422f-3e69-bff6-130939b53b0a | -13.24266 | -54.33332 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43e5a597-65f4-3571-bdc8-f6ecbb3837fb | -8.44504 | -51.56668 | 2026-07-04 05:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481390a9-a0b2-31cc-a4fd-6cab313d0f86 | -10.2996 | -57.12772 | 2026-07-04 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d719c3c-9be4-3943-a4b5-a317651b84cf | -13.24047 | -54.34903 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| eba273c5-066b-3c64-b705-6ea7c69dbe49 | -17.54645 | -46.94957 | 2026-07-04 05:23:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae1ff155-48a7-3ff1-aad5-36ea90001cbf | -13.24445 | -54.34963 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 556fff97-ba5b-3b53-96a6-65a3703a78b2 | -9.38195 | -58.20285 | 2026-07-04 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 981f95c2-3bcb-3f31-bc0d-bf416dcf9661 | -13.22567 | -54.36808 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1f40550-2eb2-30a7-9ac0-d1af7d2ac3c8 | -13.23361 | -54.36923 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dd6d6c2-0727-34ba-a214-f803fab4eb11 | -12.24005 | -64.36797 | 2026-07-04 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d2e1d20-bc23-3951-9d33-1c32962bf334 | -8.44949 | -51.56741 | 2026-07-04 05:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f39ffb7-774f-31a9-89d2-f3dd43b65ce1 | -13.22638 | -54.36295 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30fb1c21-0b4b-3422-bc42-8c7c60eb01b0 | -7.51032 | -49.52518 | 2026-07-04 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2141697c-428e-38bd-a9d7-357ad62d02b9 | -9.18675 | -58.06798 | 2026-07-04 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35065a28-e6c5-39f6-a52a-16b7f49ba2a1 | -9.80338 | -48.92115 | 2026-07-04 05:23:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa6a4996-8177-3df4-97c3-70df49832dc7 | -8.86298 | -62.22593 | 2026-07-04 05:23:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6c434cf-1da3-3879-87ab-020616acbd21 | -8.08625 | -46.70801 | 2026-07-04 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee603b65-ddc3-39b7-831c-ee5cd2a8112f | -13.24372 | -54.35487 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab702f33-7217-38f1-a9aa-d9fff02641ec | -11.42298 | -46.58266 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce25db9e-0688-3bf2-8520-4983227ff9c7 | -8.85918 | -62.22528 | 2026-07-04 05:23:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fbc67fa9-e515-359f-90a7-7bef1cb5af2a | -6.42357 | -55.79494 | 2026-07-04 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa7333ee-16c3-3d6c-8424-6630678b5a82 | -11.42363 | -46.57732 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f7c426f-07b0-3e5a-ac52-e9fa6474c8c5 | -10.12374 | -52.08831 | 2026-07-04 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf0e6c4-4887-3768-8a05-fe7c668a041c | -11.45259 | -46.55833 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 319d65d6-281e-355f-84a9-1187b527a469 | -11.45906 | -46.55926 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89ab4adf-ce42-31e4-8466-d23f5696b52b | -13.2571 | -54.34621 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60e2321d-dedd-3af0-a01e-4dac2a482217 | -9.46561 | -68.38776 | 2026-07-04 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dc9f5f0-7a8b-301b-a520-fc5c9fcff00c | -13.22496 | -54.37321 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 512a8b4e-1fae-3a8b-abe8-fd2611d63a29 | -10.90255 | -56.85468 | 2026-07-04 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac1d138-b806-3dc4-b04c-4a11da7840e0 | -6.78423 | -55.78907 | 2026-07-04 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cca32fd-8100-3c3d-b767-01fd0c7abc05 | -8.85997 | -62.22063 | 2026-07-04 05:23:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46b89bb0-aaf2-3ef1-b3be-a273bb78034b | -8.08089 | -47.16054 | 2026-07-04 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7401215-db8a-3375-87e9-4f741af16de5 | -8.02891 | -46.24018 | 2026-07-04 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c69d2cf0-8f82-31b7-af51-4315a526e419 | -11.43764 | -46.57386 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9583789-d448-3050-a41b-1d5b48bac586 | -11.42401 | -46.57822 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cffbe0c7-e126-35c8-92c6-5229fd6260fb | -8.08014 | -46.70682 | 2026-07-04 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca1a5317-b894-354e-a05c-2f6e32535994 | -11.42995 | -46.58362 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README19.md)
