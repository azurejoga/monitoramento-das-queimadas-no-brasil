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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8ae413a-f7c2-38c9-80a9-c8232e31249a | -5.47829 | -45.11805 | 2026-07-30 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 431ac645-c5a5-3be6-a12f-4439ebc7e1b3 | -6.67382 | -39.49148 | 2026-07-30 03:53:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5593986c-752d-3c59-8afc-87e6a92fb21d | -9.611 | -47.76296 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0712b6ad-d00b-3ebc-b323-7fcb8f008ffd | -9.61255 | -47.76596 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0d9fdd1-7e09-3b30-a19f-cf5e7070a4fc | -10.93333 | -43.05562 | 2026-07-30 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06d5174b-6e71-3fc2-9fb0-b3b3ff959e50 | -9.61199 | -47.75793 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3828115b-6cdb-3a48-94ee-b580a8dbe58f | -9.61717 | -47.7644 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf269c4d-5981-3fcf-bf9c-0908250c8679 | -7.6305 | -44.81784 | 2026-07-30 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 597e1ea1-1bf9-3743-8f89-f74c53e636fb | -10.63039 | -47.48731 | 2026-07-30 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 773e4c22-dab5-3afc-a508-006868b98373 | -7.34731 | -45.8504 | 2026-07-30 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e7758a9-3b12-33bc-86db-1b8dae414399 | -7.63106 | -44.81472 | 2026-07-30 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6e3ec8c-6cce-36c5-93c9-cc8aa580351a | -7.20061 | -44.87784 | 2026-07-30 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98c6151b-7247-347c-b197-1dd1abd68aa3 | -5.83224 | -44.1378 | 2026-07-30 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca716541-101a-37ed-91aa-9b7b62fb52ed | -6.85905 | -46.01089 | 2026-07-30 03:53:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52213c5c-fef0-3546-87ac-a9d151c2b76c | -11.93129 | -43.43879 | 2026-07-30 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85e36a10-b092-395e-86e1-6901a520c95b | -7.19999 | -44.88127 | 2026-07-30 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51284aad-890a-3f5e-8a69-7c8c6d81aa1a | -7.34657 | -45.85444 | 2026-07-30 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0ead95a-19e6-3991-bdce-a0952aa2aa85 | -10.1979 | -42.21221 | 2026-07-30 03:53:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e1ea8341-4058-365d-bb25-ea82a7d11e77 | -7.24505 | -46.05609 | 2026-07-30 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ebb33f8-7879-3bcd-9bc0-89136accf622 | -7.20165 | -45.50134 | 2026-07-30 03:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2081df83-8ec0-38c9-a710-f51421a4804e | -10.93615 | -43.06547 | 2026-07-30 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ac66486e-4a98-38fe-a7b3-aefb99232f90 | -5.47575 | -45.11941 | 2026-07-30 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86fd3ad4-2154-302f-8f91-1ffaa0c1d2ac | -9.61872 | -47.76744 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e131e1c9-4451-3abc-87fa-0ec96bac53cc | -10.63632 | -47.48888 | 2026-07-30 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5191f36f-1357-3f44-bf1a-ffae6bf77afe | -9.60735 | -47.75941 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 378f2ee0-29a3-3dfd-9efc-5afe211efe07 | -8.9041 | -37.9709 | 2026-07-30 03:53:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b7fc5f4-9734-3fac-a590-1a103523e7de | -6.83926 | -42.89782 | 2026-07-30 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a3c9b6f-e018-3642-bb94-9d63ce5a98d0 | -5.82644 | -44.14004 | 2026-07-30 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3efd474a-83a0-3a15-a537-eecce8b92cbb | -11.08647 | -47.80368 | 2026-07-30 03:53:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cc9e541-7b27-3b49-8d91-be9b89c726ff | -6.84664 | -42.88319 | 2026-07-30 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 783d50c9-21c6-3748-a2a9-0c2390c3e47d | -10.93698 | -43.06096 | 2026-07-30 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 518cdade-1f56-3380-98e0-85a4f15c3158 | -9.61348 | -47.76109 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 297093f4-9071-3c8e-af34-4382e08bc6cf | -7.19606 | -45.50017 | 2026-07-30 03:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97fdfe9b-a37b-3a9c-a6f4-264326e269cb | -8.47085 | -36.28036 | 2026-07-30 03:53:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7abfbb2a-f010-3572-9ba3-5428809f9d11 | -7.64844 | -37.26931 | 2026-07-30 03:53:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 886f1986-52b3-3152-905c-95ff97037a15 | -10.9378 | -43.05646 | 2026-07-30 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee6fc7b4-6f61-365b-b974-37a0c9b2195e | -6.30949 | -43.6559 | 2026-07-30 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae1a144d-f14f-3e4c-a199-dcb9c62b7489 | -10.93251 | -43.06012 | 2026-07-30 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 9d555dd5-18b9-3b06-90db-196a05d007c7 | -6.86554 | -46.00837 | 2026-07-30 03:53:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 900a7950-15d6-39e2-aeb9-6bace553c9fe | -9.61006 | -47.76771 | 2026-07-30 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9f2e31b7-ed79-3a7a-862c-b5433600f033 | -9.66067 | -37.83611 | 2026-07-30 03:53:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba3cabfb-83b6-30f7-ae65-36081fdc745f | -9.41584 | -40.79426 | 2026-07-30 03:53:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45fd914d-44af-3274-8d3e-a7a667ee6cb3 | -11.92156 | -43.43455 | 2026-07-30 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89efe655-aedd-32c9-a882-bbf5ceb94f8b | -7.13721 | -38.28169 | 2026-07-30 03:53:00 | NPP-375D | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e8ddf50-03c2-3693-ae4c-1478972efd3b | -6.30899 | -43.65876 | 2026-07-30 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92ed9246-bada-3b16-96bf-4b6a82a6761b | -10.63109 | -47.48948 | 2026-07-30 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80f5c4fe-26e6-3b19-af45-def24352c806 | -6.85973 | -46.00718 | 2026-07-30 03:53:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27353077-acd5-32f9-8ed5-57b1ca1e02ec | -5.47643 | -45.11544 | 2026-07-30 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3ef6465-96e2-3c59-a822-390cd4f4c9d9 | -9.94627 | -37.45874 | 2026-07-30 03:53:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 09c77189-9b0d-3cee-b929-fd8c4422bb95 | -11.09245 | -47.80537 | 2026-07-30 03:53:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de3491ec-2e1a-301e-b5d8-ae6111ce10d2 | -13.3154 | -43.59415 | 2026-07-30 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8375c046-ba76-39fd-a3d9-d57c18e22268 | -14.1855 | -43.99833 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2077bbe7-cbbf-3f9f-8fb5-6ebd7d584787 | -18.22874 | -42.21594 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| 88b238f5-dd4e-3d78-8178-e37a03773a88 | -13.60424 | -42.93468 | 2026-07-30 03:55:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cdb2bb40-bc29-3133-ae8a-0074ab0c7c25 | -18.22642 | -42.20844 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f69e2e5b-0d3b-3d1c-a5ff-5a1655168cba | -14.19448 | -44.00013 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14cdfe47-4e35-3829-8381-4636b61924af | -11.55354 | -47.56303 | 2026-07-30 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adf5de5a-db54-3ee6-a8fb-d93ab83008c0 | -16.50003 | -43.13312 | 2026-07-30 03:55:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b664775e-c59b-3c05-9f36-f9c279997be0 | -14.19703 | -43.9863 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d90177f6-b522-3fc0-b6b9-c85f85f6cf1b | -14.39118 | -48.03548 | 2026-07-30 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f52d1dc-b79d-35b6-aa7b-a88ff48cda54 | -12.93822 | -39.62974 | 2026-07-30 03:55:00 | NPP-375D | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce8da963-2067-34ae-afae-f53a92c6188d | -13.32069 | -43.59053 | 2026-07-30 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8346031c-0a58-3bbd-b1a4-4e593050ac0d | -14.18721 | -43.98911 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae38bbcd-a637-34e1-9afb-65e33bdede6a | -17.83502 | -41.9661 | 2026-07-30 03:55:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43c4c828-d7fe-3935-9af4-922e19b38d89 | -14.18101 | -43.99743 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76489d65-f336-31d6-ac1d-d0b649342764 | -14.18999 | -43.99923 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d23ac4c-d990-3d09-8318-ac0a7be13836 | -16.49932 | -43.13698 | 2026-07-30 03:55:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ffe6f1e-55ea-3c5e-ae52-157c0a5ee7e0 | -18.22582 | -42.21062 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| 364d55f7-e6ef-3070-a247-ddef6c4a96b2 | -17.93551 | -44.3397 | 2026-07-30 03:55:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f999c59b-26eb-3486-aa23-a698a472f7c4 | -12.14518 | -48.95226 | 2026-07-30 03:55:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce916e6-4e74-3774-9a8b-bb4ef7164f14 | -17.21828 | -41.5305 | 2026-07-30 03:55:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6774f701-5a8d-3a00-9fd0-4bde95487aa5 | -18.22668 | -42.20592 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 1bd8026b-7d7e-3b47-8ddd-61b781a28c3e | -18.2334 | -42.21177 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| bdde3cb8-5c4c-3d78-8a82-e737c9f65213 | -14.19631 | -43.99844 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b2a5718-f8dc-3904-b892-efbd973b4cea | -18.41599 | -40.02243 | 2026-07-30 03:55:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c549c19-c299-376d-ade5-2ed9061a603a | -14.38569 | -48.03276 | 2026-07-30 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bcd0e80-0bc3-3fcb-b714-700ab821c8b4 | -18.22725 | -42.20374 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5cf4c0f9-fdf7-3737-b033-80b61925c225 | -15.37387 | -42.65025 | 2026-07-30 03:55:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c888b290-1c22-3735-ab93-b2ccd691cbe4 | -18.35838 | -47.1983 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c8bcddd-fe76-3110-9e2a-2251c872d39d | -17.22195 | -41.5313 | 2026-07-30 03:55:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| abd56081-40a6-3728-b2fd-f715b59a7832 | -12.81593 | -41.95972 | 2026-07-30 03:55:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 803059d4-3436-3d29-98e8-e579a96cd15a | -14.19982 | -43.99643 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dbc7893-84f8-33ac-9302-912b1a9eae39 | -14.18465 | -44.00295 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a487d919-c311-396c-8813-53dada0b74dc | -18.22937 | -42.21373 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 1f1fc626-af5f-3e16-aa27-2689746ab85c | -16.42828 | -40.86996 | 2026-07-30 03:55:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0b7d000-d4d5-3c24-abfe-c27265bf63e6 | -18.8982 | -46.07113 | 2026-07-30 03:55:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3d984e3-d8dc-35db-b6ee-b50639efde7a | -14.19543 | -44.00305 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7d3b7f0-4636-3b7f-9007-e2e894d62244 | -18.21884 | -42.2073 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e5400fd8-0fb4-3bee-8f54-a33fa910d1b1 | -18.22289 | -42.20533 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bc9a236a-cd3e-336b-845f-b39a958bed37 | -14.18636 | -43.99371 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86ad98e4-a6b0-315d-af2f-033cc0cf8358 | -13.31625 | -43.58967 | 2026-07-30 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eecf0f41-5107-321a-859c-e5014d9c775c | -18.2302 | -42.20901 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0dba571c-df75-3807-b4a0-43d5445eecda | -12.81997 | -41.96041 | 2026-07-30 03:55:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57a878ea-4cf7-3594-898f-e5b1b500c4f0 | -17.02175 | -41.22137 | 2026-07-30 03:55:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29886c9a-59ff-3c07-a587-98ed998fedce | -18.22203 | -42.21006 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 95433452-e167-3af1-8cb0-aaf45929ba5e | -11.41287 | -50.08957 | 2026-07-30 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff244c00-b7eb-39a5-8569-5be8b80ea67d | -18.35902 | -47.19527 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0629cb5e-457a-3e98-bb54-d117a647f79c | -18.23047 | -42.20652 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6c669fa0-f90a-3133-9ba8-b762455faa7d | -18.36347 | -47.19953 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef6f403-8206-39e2-94d3-b56dc1604ead | -19.38661 | -41.44297 | 2026-07-30 03:55:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README5.md)
