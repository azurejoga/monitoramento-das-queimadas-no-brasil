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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65a7d5a9-356c-300d-8846-4c15b243796b | -6.60406 | -39.53286 | 2025-12-10 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67859e69-65a2-3400-9bc0-8e1bc6527359 | -6.01093 | -42.32759 | 2025-12-10 04:36:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1881c791-0d12-3e85-aed7-1b645114f4dc | -2.48504 | -47.77575 | 2025-12-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63da3686-bc8a-3910-960e-720662fdd29d | -2.79769 | -47.34219 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b54a49df-e7f4-31d3-99de-53aecb2f9a3d | -6.00525 | -40.37434 | 2025-12-10 04:36:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4dc10db9-b42e-35c1-a6e6-86c66d53ea87 | -5.29949 | -43.5176 | 2025-12-10 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0f84d5d-3cb5-311a-b69a-6f03b431c817 | -3.37806 | -52.89841 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4764988-498f-32b4-bd51-e1bc215f3e76 | -2.30329 | -45.56547 | 2025-12-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb24be0-c2ed-3c66-ba8c-df61c4ceb687 | -2.91177 | -40.34647 | 2025-12-10 04:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 300f3b84-18fa-3834-892e-77c89a6b29f8 | -4.98366 | -41.29825 | 2025-12-10 04:36:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7408a7fa-ce4d-30f7-90a9-9b339bbeebea | -3.3982 | -42.46199 | 2025-12-10 04:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d3060feb-b83d-3f8d-b030-aeb24905f199 | -2.07974 | -52.04952 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 478f07a8-6a68-3f31-97b7-e7831c41a510 | -2.79883 | -47.3565 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f25ef89c-4717-3f70-a3ca-dd5cb9bd9785 | -3.68298 | -43.82644 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2daec55e-d474-3089-9db5-2d822788b081 | -1.41491 | -54.29352 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27670f59-8a2f-353c-8f29-e781f31c8caf | -3.8307 | -43.32015 | 2025-12-10 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2eeede9-9bbc-3df9-b81b-45ff992350e4 | -2.00794 | -54.13714 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d93f0afb-248e-35c0-88f1-3c32e6831012 | 0.33184 | -49.76883 | 2025-12-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4cd92c1-49ce-30e2-a381-75f87ea355dc | -3.15133 | -45.7462 | 2025-12-10 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a06bed8-7242-3ef2-9048-08ebfa215ee9 | -5.74429 | -42.06133 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d05ce9ea-7b2a-320c-8064-3364e6bd0517 | -3.68803 | -43.81834 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1c13c79-dbfd-32f7-aa8f-b4a7a61fa5ab | -2.80046 | -47.34615 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb3c364d-6525-31f0-befd-7ece0b468c46 | -1.73547 | -46.50467 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd6926aa-e0db-3519-9a68-adda84bef126 | -2.64458 | -46.96173 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c57fb78-1275-346d-bfd3-0500b0f91dc3 | -3.68231 | -43.83076 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4f9cc05-8946-3041-86b1-5dfb3138619e | -2.71798 | -53.19158 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d580d0-c489-35b1-9fc2-09140c710095 | -2.36393 | -47.68569 | 2025-12-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 939b03e6-d67b-3b41-8e11-0ccee4662514 | -4.54761 | -45.90347 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba4a2e8-8a51-3b5b-a7dc-02f2a98c992b | -2.42032 | -48.26984 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1bcb58-761d-3ad7-b75a-db1ae1ef351a | -0.59761 | -51.81959 | 2025-12-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88ce6c50-a540-3151-90cc-5b8cd1f9287c | -2.07915 | -52.05309 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2eab62a0-b232-36aa-8502-281cad6f64ee | -5.58929 | -39.7665 | 2025-12-10 04:36:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42e1e7a5-f892-370e-b2bb-6bc34a7018fc | -2.37344 | -45.80629 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01257b81-dabb-3ac1-8608-f94e3a3e3deb | -5.74372 | -42.06525 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7ccc923-0db0-3b34-909c-15baa5d5b4f1 | -2.88773 | -45.24342 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 14976e15-f329-3708-a8b2-947bd846c95d | -2.77505 | -54.53069 | 2025-12-10 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d2fcb91-47a4-3beb-939e-2b820e99b81c | -3.15076 | -45.7498 | 2025-12-10 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fc68d61-81db-33b5-b775-51caca0ad726 | -2.92459 | -48.22547 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fefd7c1-5afa-3a88-a3c7-0861da14529a | -5.33207 | -43.56117 | 2025-12-10 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c968ad14-e7c8-3b39-90ba-5d71c7b54664 | -5.74546 | -42.05342 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31185ea0-e179-386b-a742-b951bc432e22 | -2.29226 | -46.10418 | 2025-12-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d740b2b3-10e1-3385-a30a-914e460db680 | -2.51653 | -45.43108 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a175495-8eec-3d78-8e9c-d8d34e3e5e4b | -3.23115 | -47.47069 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 066533d1-cad4-3b52-b02b-41f87ca6e3f5 | -3.72313 | -47.1205 | 2025-12-10 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d57b8fc3-9896-3ea3-95f3-d8d6a04a47d9 | -1.47378 | -54.20201 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 68a86d9b-dc41-33c6-a0a0-d8c28cdf326b | -5.73754 | -42.04831 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 53a8a7b4-8987-32de-bef5-1b644f64e91c | -1.58521 | -54.11916 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 737bb1f2-0f4d-3c8c-af58-83a8bcae5278 | -2.374 | -45.80274 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee759b2-4df7-3e17-a6a4-88e6f99ccd20 | -1.47695 | -53.54041 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fae17f28-c392-3bf5-b739-fc5949a77672 | -5.16396 | -43.11769 | 2025-12-10 04:36:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ab54f7b-63bd-3822-861f-2b4cb454ed0e | -1.87543 | -54.69051 | 2025-12-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4154de8b-255c-373b-80ca-4d016c5eb636 | -5.53106 | -41.65778 | 2025-12-10 04:36:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3f037a1-3694-3535-b1a1-60cbb7f11f46 | -2.13945 | -47.88601 | 2025-12-10 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 342f4698-c445-342b-8519-e23eb2e53d5d | -3.96497 | -41.5266 | 2025-12-10 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3ef10920-b4f2-3c33-a942-07f56453f674 | -3.82575 | -43.3525 | 2025-12-10 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47d73365-8a1c-3447-a83a-22e65a5d4db4 | -2.44379 | -45.60147 | 2025-12-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0747525-e530-3eb4-ad34-479d3958006b | -3.69744 | -43.80652 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2eac4b22-8c91-326b-9a2b-e8671d1a2236 | -3.01149 | -52.68328 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd631d62-b953-3405-8dc7-515a38857b64 | -1.73438 | -46.51158 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d21d4ff-e436-3592-a1c7-341dbf42bbb5 | -3.69239 | -43.81461 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bede5cc-3806-3588-9b0e-a6a16db52210 | -2.82379 | -45.27588 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc42953a-c57c-3fee-91b9-d08721ffa2b1 | -3.69307 | -43.81028 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69a8edb9-57c8-325d-9b96-b26a1a107ce7 | -6.23498 | -40.63296 | 2025-12-10 04:36:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 166711df-ff32-3eb5-a3a0-2f12ef7312f4 | -5.41369 | -40.65924 | 2025-12-10 04:36:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51e59133-b3f6-3884-b26d-291469e05af8 | -2.82095 | -45.27166 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 001c0474-be3e-354a-ad02-3f8afc68ed20 | -2.88831 | -45.23972 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2f31af7c-2b0e-39ad-9cc9-2f7dbbbf50d1 | -5.32752 | -43.56536 | 2025-12-10 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 26bf68af-d2a7-39cd-8b55-9fe385145156 | -2.63339 | -45.39646 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8c88c2d-c793-36f0-bb02-51497f46b1e0 | -2.48782 | -47.77975 | 2025-12-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5916ae88-a586-352e-a913-4880637f3c60 | -2.81694 | -45.27481 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3545810c-7534-3f86-b0fe-2d305d19af77 | -5.85005 | -42.44703 | 2025-12-10 04:36:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c35a4514-81df-367e-84f2-0164738eceff | -4.91136 | -43.46453 | 2025-12-10 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2932afa1-8266-321c-a183-1803442c89dd | -2.06121 | -46.49879 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5849d33d-611b-38ee-9413-826c4a4013cd | -4.00299 | -43.23419 | 2025-12-10 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15383cb1-15c3-30cf-91a5-6bc07b2373da | -3.94607 | -42.82784 | 2025-12-10 04:36:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b7b20ec-ee77-3f26-bc76-bf77744e1d2c | -1.58992 | -54.11996 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b7d339c-eaaa-3977-b383-31eed9071c93 | -1.41568 | -54.28882 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad6f8cc2-b6a6-3b79-ad0e-8c483b35716f | 0.61171 | -51.56525 | 2025-12-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620f3adb-30d4-37da-9247-28bcfcbd7d77 | -1.42044 | -54.28979 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62355ce5-4a91-3651-a59b-a042c64dd80e | -2.0838 | -52.05018 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccf7a86e-0d91-36cc-9d33-6918119377cb | -2.86172 | -46.80833 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 311e0ca6-09f2-39af-93d0-346b72b2cf7b | -3.2306 | -47.47414 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f5792817-5a49-3573-8039-548f6f29e70b | -3.84421 | -50.97177 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cd07d76-408a-353e-b385-44d6affad946 | -3.68366 | -43.82211 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9b4ee15-64a7-364d-9b70-b6c7a925ddb8 | -2.74715 | -48.38998 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69f80766-a00e-3faa-8f7f-28e58b6cb27c | -5.53047 | -41.66188 | 2025-12-10 04:36:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1f51009-3e15-3eae-a0fc-e7617c3a37db | -2.6457 | -45.56192 | 2025-12-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ff426a1-55bf-345a-8e43-dc4868216e76 | -6.60921 | -39.53335 | 2025-12-10 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bddfad7-156d-37ae-8387-7bfaaa80f9d6 | -2.06289 | -49.00112 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bed02e81-4a32-36b3-ab5d-ca9672925200 | -3.8345 | -43.32075 | 2025-12-10 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4716c895-8fdc-3d6c-a18d-2ff84c4f511f | -1.58911 | -54.125 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86ce3692-6c7d-3534-a8b4-549e483385aa | -3.22786 | -49.1234 | 2025-12-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7c07b62-606d-305d-9724-52e22817c143 | -2.00325 | -54.13635 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5217912c-69c7-3c8e-9eb1-74b96d75171d | -1.19737 | -54.1914 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e14845-57d6-3276-8f56-2f5f9934e5ab | -2.02595 | -52.04831 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dc01618-2ab5-3fcf-a1a9-da5f5c155424 | -1.87854 | -54.68679 | 2025-12-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 179625b5-befa-32a3-809a-02891031428b | -5.84308 | -42.46505 | 2025-12-10 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e647230-7ef7-3fd9-89c1-050190cb5f22 | -5.32824 | -43.56065 | 2025-12-10 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d09b1ea4-dbfa-3aad-b9cf-272f9a95e05b | -2.42164 | -45.83899 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dc5a934-e877-3ca6-9c92-d76cab9e805c | -3.44266 | -41.64981 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
