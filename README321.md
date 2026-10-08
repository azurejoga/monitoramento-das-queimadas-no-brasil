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

## Dados Diários - Página 321

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc3f5923-091f-3b6e-aa9b-6d08f44fe043 | -12.24451 | -44.75083 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 4be6d4d8-97f5-36a5-8fed-df771581db3f | -19.34722 | -45.60493 | 2026-10-08 16:37:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42a74263-2453-3647-a1bf-999d79902075 | -12.20199 | -44.64954 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 0be9f81d-2120-31d0-97a3-bdec06e74764 | -6.8525 | -41.74365 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 3d1693a5-dad0-3afc-b4f5-811476123413 | -5.72243 | -41.63665 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 1dd74284-77a4-31db-8bbd-08f128f70686 | -8.21326 | -46.42233 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9254345e-9c8e-3c80-b0cb-26b4b077a651 | -8.87882 | -41.44756 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 57.6 |
| e466c58b-ffaa-3574-b850-cb38afbcd949 | -5.98781 | -40.93695 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5ad6aba8-35b8-3d00-b797-90ba992c2242 | -12.24291 | -44.74028 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2c9bef7c-770f-3350-920c-0dcad212ee53 | -13.38567 | -43.48016 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ef6b2823-e7ad-35c1-b83d-f09e87253357 | -4.93756 | -37.37711 | 2026-10-08 16:37:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| faa9b2c5-1b15-3385-98ed-8cefbbd46524 | -8.06644 | -45.60947 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c6091f7a-5bd1-3c24-9507-3f6e533aea6e | -10.53508 | -47.2645 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 328608b2-57e7-3bb1-b542-99f1dcbef4f3 | -18.96746 | -41.17365 | 2026-10-08 16:37:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7db880ae-4f50-34e1-a902-6638cdc9944f | -11.77104 | -45.54649 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b9175d28-f0c3-355d-a38f-7e8aa32f33c1 | -11.0714 | -44.0319 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 71fcdbb9-5e63-3482-bb3d-96947db0c8fd | -6.96912 | -43.89157 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0df1dff5-72d8-31af-ad1e-306b131bdf69 | -11.57923 | -43.67395 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 737f6945-b38c-3df3-a2d4-2c2dd2fbc1ec | -12.15582 | -44.74678 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3fec22d1-07a6-309d-998a-c551074d4d0a | -6.17541 | -44.03647 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf06ca5c-a751-312e-badb-d4ca15f598f7 | -11.21384 | -44.86697 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 89a10f9e-bacb-36cb-bd93-9a83748df7a1 | -7.04454 | -44.33038 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cab85bf1-6c9b-32dc-a802-3a048d4200d0 | -7.48904 | -42.82564 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 33d7aad3-3a2e-3fbe-af0a-2571d8f57433 | -10.9276 | -45.39489 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 029e7824-24cd-35c9-b761-f02278a232b8 | -8.93811 | -45.18569 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 57c4439c-83c4-32bd-ab4b-bae12b4835fd | -8.95886 | -45.1643 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| cb909b43-4a54-30d6-8e99-4eea97e67b26 | -5.17996 | -38.44944 | 2026-10-08 16:37:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| a1849d4d-4aa1-3c0f-8007-320ffab48dd7 | -9.84693 | -47.46501 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9e2d479-d0de-3ccf-96ed-e70f84877257 | -10.76646 | -46.53431 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a7ca0f42-3af5-3ae9-8c83-695f8ee177c6 | -8.94744 | -45.13401 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d427a621-1184-3e4d-b9f9-440c267b303a | -5.68834 | -40.88977 | 2026-10-08 16:37:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8cafa782-949f-37cf-926f-cdc6a7ef60ac | -6.88354 | -38.54485 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7bbc3556-9df9-3d87-bd74-57d4ad360675 | -7.26845 | -39.19199 | 2026-10-08 16:37:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a754d427-90cf-378b-8f7b-d15f8ce54ae0 | -13.53537 | -42.50137 | 2026-10-08 16:37:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0af4d6f8-236e-3e9a-ab2e-fa7a4738d48b | -5.96812 | -40.91779 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2aa200c3-0466-3b30-8c7d-0bad7d816026 | -7.88746 | -55.00109 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1875a96d-bc17-301b-bb1e-68502ea6b3bd | -8.28904 | -45.73408 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 3ff6eb30-f35c-30a7-9a06-7b5054b16f24 | -7.31608 | -44.00332 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6a3f68e-2fab-38d2-ae3d-e963e80a7a63 | -11.95292 | -47.76313 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c0e0e3e-2887-3757-b2ee-79a55f1d4895 | -6.8655 | -39.15319 | 2026-10-08 16:37:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 13750d16-488b-37a5-82bd-c19097531610 | -8.53227 | -54.61678 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28adbf03-cf33-3c61-beff-45bafee5656b | -5.33119 | -35.55631 | 2026-10-08 16:37:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5961736-dc25-3b84-b036-8396fb1c29c2 | -11.31115 | -44.83706 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 8c356302-dd24-30b7-b098-6e9c4d5f522c | -9.13719 | -45.84615 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 39f6cb6b-5eab-3bc8-8979-3865425b88e8 | -12.20959 | -57.09581 | 2026-10-08 16:37:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 53b28834-84c3-31c2-8f57-54e55aea75d6 | -7.62826 | -45.38504 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 96f2fb42-0953-3938-b27a-c2e2ca5205f2 | -11.10804 | -44.00422 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cff60f84-c63e-362b-975d-3897ed7869fc | -5.74815 | -41.72203 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| c367820a-327e-3ead-a9ee-c1bc9846aa2e | -8.28242 | -45.7351 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 61750207-8970-323f-976d-2dc494574388 | -8.08127 | -45.61786 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7089eb7-0fac-3310-bf48-7b37415abf20 | -13.17586 | -54.33425 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 3c6df926-5895-36ed-bd57-4e0b43a32697 | -7.7201 | -44.72615 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aecfa05c-4247-38be-af8d-14f024dd303e | -7.10786 | -45.24465 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bd7bd754-43ac-325a-89e0-94844fc0f276 | -6.38596 | -42.92471 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6a414daa-4cf6-32a0-9df9-38d104a460f1 | -8.27188 | -46.90567 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7e4ede6-8bba-3e2c-97bd-acc4c06fd242 | -6.06872 | -44.38568 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d2b0048-d6a6-3d4b-8945-666580bc1db3 | -9.82235 | -45.68974 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3281fd05-1a3a-38a2-8004-ac64da1c597d | -7.07473 | -46.45117 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81223150-c4dc-3f06-a13d-cc2ad3689381 | -7.21215 | -44.27779 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f8fa79b4-3d58-32bb-b93a-60fecddc4475 | -12.24852 | -38.6292 | 2026-10-08 16:37:00 | NOAA-20 | TEODORO SAMPAIO | BAHIA | Brasil | 2931400 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b1b26894-8ff2-331f-91ca-6c542758549c | -20.58756 | -48.45908 | 2026-10-08 16:37:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| b89d4951-8ad3-3ab6-a288-58d14e8d5cdc | -9.10445 | -45.11901 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c4392d90-0441-309f-9670-b6f2747c042e | -6.76435 | -43.7006 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ede62426-2fbd-3d25-bc24-62451fcb20be | -12.41785 | -46.44317 | 2026-10-08 16:37:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f4c4f063-8ca7-3ec0-afb7-f30db6e91775 | -11.09305 | -44.01754 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2a4b59e1-a79e-3334-8aa1-70df1a629515 | -9.80412 | -47.81959 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9fecb6e6-ba3e-3634-9ffa-390cfeb166bb | -5.74584 | -41.73227 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| c5050b17-d2ba-3bf9-b2d5-d69981dd3864 | -6.21696 | -44.84055 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| da3e88ff-499f-3381-9389-5549175c49b6 | -9.41971 | -36.73404 | 2026-10-08 16:37:00 | NOAA-20 | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 37019e9b-68b4-3cf7-89f7-b50743e7f90d | -6.82891 | -39.55611 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c29e830a-9802-33ea-a1ca-e2fba2eff6e8 | -18.29654 | -42.23314 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 221c4d12-9526-3ef6-b405-0e34a2417895 | -18.29328 | -42.32068 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dd77b307-4355-368b-8154-ec26ef48bbd2 | -13.58496 | -43.1692 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d45bba15-1a12-3f5f-8bfe-2d09141efb5d | -7.04892 | -45.43511 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 258cec86-e872-336c-a3cf-56b14fba28f2 | -11.86337 | -43.5608 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| da9c9718-367c-3597-b056-4108ddcaec26 | -8.581 | -45.69183 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 84ff3fe5-db73-3490-9c28-f97f9496eb96 | -11.07584 | -44.03848 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e03b32a9-b2c2-3967-b131-913efb87e05c | -11.77066 | -45.52119 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 922c06dc-5be6-3462-bf17-1586328482f3 | -5.75046 | -41.71179 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 9aaf2794-f3fe-3b06-a541-cab5b48a78e4 | -13.20175 | -54.50608 | 2026-10-08 16:37:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b90e882f-ce05-38f0-954d-465834c10fd9 | -5.23997 | -35.85001 | 2026-10-08 16:37:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a0eb8e04-29e5-31e7-82e8-01ad317e6157 | -8.55225 | -46.9148 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5c76c7f6-8a31-30ce-8c69-6b94236c0392 | -10.84958 | -42.8074 | 2026-10-08 16:37:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1e1ddfa2-2003-3caf-ba49-61ed92aeccb0 | -9.43631 | -44.60715 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| f9914dc5-8c8d-3214-8eae-b927b5a38c48 | -11.25519 | -45.18351 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2dd6ecb4-1a58-391f-954c-e1388a9a16c2 | -6.53489 | -45.40387 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2d301aa-2a40-3388-814d-0be88bb105fa | -4.98567 | -36.88053 | 2026-10-08 16:37:00 | NOAA-20 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dde26dc2-aee4-3ff1-8618-69efb704c77f | -10.43495 | -47.29576 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c8fbcb32-f94c-3901-870d-958be2266c19 | -12.21925 | -42.27963 | 2026-10-08 16:37:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7828436-21f9-397a-b14a-fe7736c94c5b | -11.008 | -47.96598 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 908ed5e4-01e3-3c02-8add-8720c93b8a4f | -11.08861 | -44.01097 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08d4e1dd-c5f0-3a5f-b1c3-22805d6bf234 | -11.8389 | -48.0947 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce342df1-028b-3e15-af8e-95a0cb514ad3 | -8.53039 | -46.90707 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c95917c2-8162-3773-b037-14dd1869cdc4 | -10.74304 | -48.54249 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58933df7-5647-3c0e-a6c9-563b325a5b79 | -10.60415 | -43.84559 | 2026-10-08 16:37:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cb22d2d7-061d-3b1a-b730-2c34fcc343e9 | -11.79559 | -46.78056 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 82227b0a-adcf-3839-886a-6f639d305e54 | -11.59092 | -43.66102 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 435d3897-8ceb-33dd-afce-68d4fa1af495 | -9.90568 | -44.78934 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9b3dc567-7294-3771-841e-3bdc0e6671b6 | -18.57844 | -39.83295 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 32a20009-7ac3-38c9-b41d-216c7a459664 | -11.75425 | -43.42682 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README322.md)
